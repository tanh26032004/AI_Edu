# -*- coding: utf-8 -*-
"""
EduMaster AI - Hệ thống Soạn giảng & Khảo thí chuẩn Công văn 7991 & 5512
Ứng dụng Web dành cho Giáo viên THCS và THPT (tỉnh Vĩnh Long và toàn quốc).
Giao diện tối ưu phong cách EdTech SaaS Hiện đại - Tinh tế - Trực quan.
Tự động thích ứng đa môn học và đa khối lớp (Toán, Ngữ văn, Vật lí, Hóa học, KHTN, Tiếng Anh...).
"""

import os
import streamlit as st
import io

from sample_data import (
    SUBJECT_PRESETS,
    get_sample_package_for_subject,
    SAMPLE_METADATA,
    SAMPLE_LESSON_PLAN,
    SAMPLE_SLIDES,
    SAMPLE_EXAM_MATRIX,
    SAMPLE_EXAM_SPEC,
    SAMPLE_EXAM_QUESTIONS,
    SAMPLE_EXAM_ANSWERS
)
from export_utils import export_to_docx, export_to_pptx
from gemini_service import generate_pedagogical_package

# ==========================================
# CẤU HÌNH TRANG WEB STREAMLIT
# ==========================================
st.set_page_config(
    page_title="EduMaster AI - Soạn giảng & Khảo thí chuẩn 7991 & 5512",
    page_icon="https://cdn-icons-png.flaticon.com/512/3976/3976625.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS PHONG CÁCH SƯ PHẠM SAAS HIỆN ĐẠI
# ==========================================
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .block-container {
        padding-top: 1.8rem;
        padding-bottom: 3rem;
    }

    /* Sidebar Brand Card */
    .sidebar-brand-card {
        display: flex;
        align-items: center;
        gap: 12px;
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        padding: 14px 16px;
        border-radius: 12px;
        color: white;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
    }
    .brand-icon-box {
        width: 40px;
        height: 40px;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.25rem;
    }
    .brand-title {
        font-weight: 800;
        font-size: 1.15rem;
        letter-spacing: -0.3px;
        line-height: 1.2;
    }
    .brand-sub {
        font-size: 0.72rem;
        color: #BFDBFE;
        font-weight: 500;
    }
    
    .sidebar-section-title {
        font-size: 0.78rem;
        font-weight: 700;
        color: #475569;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Status Indicator */
    .status-indicator {
        padding: 6px 12px;
        border-radius: 8px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-top: 4px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .status-indicator.ready {
        background: #ECFDF5;
        color: #065F46;
        border: 1px solid #A7F3D0;
    }
    .status-indicator.demo {
        background: #EFF6FF;
        color: #1E40AF;
        border: 1px solid #BFDBFE;
    }

    /* Hero Header */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 50%, #2563EB 100%);
        padding: 2.2rem 2.4rem;
        border-radius: 18px;
        color: white;
        margin-bottom: 1.6rem;
        box-shadow: 0 12px 30px -6px rgba(30, 58, 138, 0.28);
        position: relative;
        overflow: hidden;
    }
    .hero-container::after {
        content: "";
        position: absolute;
        top: -60px;
        right: -60px;
        width: 220px;
        height: 220px;
        background: radial-gradient(circle, rgba(56, 189, 248, 0.25) 0%, rgba(56, 189, 248, 0) 70%);
        border-radius: 50%;
        pointer-events: none;
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.6px;
        margin-bottom: 0.6rem;
        display: flex;
        align-items: center;
        gap: 14px;
    }
    .hero-version-pill {
        font-size: 0.82rem;
        font-weight: 600;
        background: rgba(255, 255, 255, 0.16);
        border: 1px solid rgba(255, 255, 255, 0.25);
        padding: 4px 12px;
        border-radius: 20px;
        letter-spacing: 0.2px;
    }
    .hero-subtitle {
        font-size: 1.02rem;
        color: #E2E8F0;
        line-height: 1.6;
        max-width: 980px;
    }
    .hero-badges {
        display: flex;
        gap: 10px;
        margin-top: 1.2rem;
        flex-wrap: wrap;
    }
    .badge-pill {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(8px);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.22);
        color: #F8FAFC;
        display: inline-flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Overview Metric Card */
    .metric-card-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 1.1rem 1.25rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02);
        transition: all 0.2s ease;
    }
    .metric-card-box:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.06);
        border-color: #CBD5E1;
    }
    .metric-info-label {
        font-size: 0.78rem;
        color: #64748B;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .metric-info-val {
        font-size: 1.12rem;
        font-weight: 700;
        color: #0F172A;
        margin-top: 4px;
    }
    .metric-icon-circle {
        width: 44px;
        height: 44px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
    }
    .icon-blue { background: #EFF6FF; color: #2563EB; }
    .icon-teal { background: #F0FDFA; color: #0D9488; }
    .icon-indigo { background: #EEF2FF; color: #4F46E5; }
    .icon-amber { background: #FFFBEB; color: #D97706; }

    /* Section Header */
    .section-head-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0F172A;
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 0.8rem;
    }
    
    /* Slide Preview Card */
    .slide-card-container {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-top: 4px solid #2563EB;
        border-radius: 14px;
        padding: 1.3rem 1.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .slide-header-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 0.8rem;
    }
    .slide-badge-num {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #EFF6FF;
        color: #1D4ED8;
        font-weight: 700;
        font-size: 0.78rem;
        padding: 4px 10px;
        border-radius: 6px;
        border: 1px solid #DBEAFE;
    }
    .slide-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0F172A;
    }
    .slide-visual-card {
        background: #F8FAFC;
        border-left: 3px solid #6366F1;
        padding: 0.85rem 1.1rem;
        border-radius: 0 10px 10px 0;
        font-size: 0.88rem;
        color: #334155;
        margin-top: 0.9rem;
        line-height: 1.5;
    }
    
    /* Modern Streamlit Buttons */
    .stButton>button {
        border-radius: 10px;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
        transition: all 0.2s ease;
    }

    /* Style cho các Tab */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        border-bottom: 2px solid #E2E8F0;
        padding-bottom: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 48px;
        font-size: 0.92rem;
        font-weight: 600;
        border-radius: 8px 8px 0 0;
        padding: 0 18px;
        color: #64748B;
    }
    .stTabs [aria-selected="true"] {
        color: #2563EB !important;
        border-bottom: 3px solid #2563EB !important;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# KHỞI TẠO SESSION STATE
# ==========================================
if "current_package" not in st.session_state:
    st.session_state["current_package"] = get_sample_package_for_subject(
        subject="Vật lí",
        grade="Lớp 10",
        grade_level="THPT",
        book_series="Kết nối tri thức với cuộc sống"
    )

if "active_subject" not in st.session_state:
    st.session_state["active_subject"] = "Vật lí"

if "active_grade" not in st.session_state:
    st.session_state["active_grade"] = "Lớp 10"

if "lesson_input_value" not in st.session_state:
    st.session_state["lesson_input_value"] = SUBJECT_PRESETS["Vật lí"]["lesson_name"]

if "notes_input_value" not in st.session_state:
    st.session_state["notes_input_value"] = SUBJECT_PRESETS["Vật lí"]["special_notes"]


# ==========================================
# SIDEBAR - CẤU HÌNH ĐẦU VÀO SƯ PHẠM
# ==========================================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand-card">
        <div class="brand-icon-box">
            <i class="fa-solid fa-graduation-cap"></i>
        </div>
        <div class="brand-text-box">
            <div class="brand-title">EduMaster AI</div>
            <div class="brand-sub">Trợ lý Sư phạm 2025</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="sidebar-section-title">
        <i class="fa-solid fa-sliders"></i> Cấu hình Hệ thống
    </div>
    """, unsafe_allow_html=True)
    
    # 1. API Key
    default_api_key = os.environ.get("GEMINI_API_KEY", "")
    if not default_api_key:
        try:
            secrets_path = os.path.join(os.path.dirname(__file__), ".streamlit", "secrets.toml")
            if os.path.exists(secrets_path) and hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
                default_api_key = st.secrets["GEMINI_API_KEY"]
        except Exception:
            default_api_key = ""
            
    api_key_input = st.text_input(
        "Google Gemini API Key",
        value=default_api_key,
        type="password",
        help="Khóa API cá nhân từ Google AI Studio (https://aistudio.google.com/app/apikey).",
        placeholder="AIzaSy..."
    )
    
    if api_key_input:
        st.markdown("""
        <div class="status-indicator ready">
            <i class="fa-solid fa-circle-check"></i> Đã kết nối Gemini API
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="status-indicator demo">
            <i class="fa-solid fa-circle-info"></i> Chế độ mẫu chuẩn sẵn sàng (Không cần Key)
        </div>
        """, unsafe_allow_html=True)

    model_choice = st.selectbox(
        "Mô hình AI (Gemini Model):",
        options=["gemini-2.5-flash", "gemini-1.5-flash", "gemini-1.5-pro"],
        index=0,
        help="gemini-2.5-flash: Tốc độ siêu tốc, tư duy sư phạm chuẩn xác và cấu trúc chặt chẽ."
    )
    
    st.markdown("""
    <div class="sidebar-section-title" style="margin-top: 1.4rem;">
        <i class="fa-solid fa-book-bookmark"></i> Thông tin Hồ sơ Dạy học
    </div>
    """, unsafe_allow_html=True)
    
    # 2. Cấp học & Khối lớp
    col_level, col_grade = st.columns([1, 1])
    with col_level:
        grade_level = st.radio("Cấp học:", options=["THCS", "THPT"], index=1)
        
    with col_grade:
        if grade_level == "THCS":
            grade = st.selectbox("Khối lớp:", ["Lớp 6", "Lớp 7", "Lớp 8", "Lớp 9"], index=2)
        else:
            grade = st.selectbox("Khối lớp:", ["Lớp 10", "Lớp 11", "Lớp 12"], index=0)

    # 3. Môn học
    if grade_level == "THCS":
        subject_list = [
            "Toán", "Ngữ văn", "Khoa học tự nhiên (KHTN)", "Tiếng Anh",
            "Lịch sử & Địa lí", "Tin học", "Giáo dục công dân (GDCD)",
            "Công nghệ", "Âm nhạc", "Mĩ thuật", "Hoạt động trải nghiệm hướng nghiệp"
        ]
    else:
        subject_list = [
            "Vật lí", "Toán", "Ngữ văn", "Tiếng Anh", "Hóa học", "Sinh học",
            "Lịch sử", "Địa lí", "Tin học", "Giáo dục kinh tế & Pháp luật (GDKT&PL)",
            "Công nghệ", "Hoạt động trải nghiệm hướng nghiệp"
        ]
    
    # Xác định index mặc định cho subject
    default_sub_idx = 0
    if st.session_state["active_subject"] in subject_list:
        default_sub_idx = subject_list.index(st.session_state["active_subject"])
        
    subject = st.selectbox("Môn học:", subject_list, index=default_sub_idx)

    # 4. Tự động đồng bộ khi Thầy/Cô đổi môn học
    if subject != st.session_state.get("active_subject") or grade != st.session_state.get("active_grade"):
        st.session_state["active_subject"] = subject
        st.session_state["active_grade"] = grade
        preset = SUBJECT_PRESETS.get(subject, {})
        new_lesson = preset.get("lesson_name", f"Chủ đề trọng tâm môn {subject} - {grade}")
        new_notes = preset.get("special_notes", f"Phát triển phẩm chất và năng lực đặc thù môn {subject} theo CT GDPT 2018.")
        st.session_state["lesson_input_value"] = new_lesson
        st.session_state["notes_input_value"] = new_notes
        # Tự động nạp gói dữ liệu mẫu cho môn mới chọn
        st.session_state["current_package"] = get_sample_package_for_subject(
            subject=subject,
            grade=grade,
            grade_level=grade_level,
            book_series="Kết nối tri thức với cuộc sống",
            custom_lesson_name=new_lesson,
            custom_notes=new_notes
        )
        st.rerun()

    # 5. Bộ sách giáo khoa
    book_series = st.selectbox(
        "Bộ sách giáo khoa:",
        ["Kết nối tri thức với cuộc sống", "Cánh diều", "Chân trời sáng tạo"],
        index=0
    )

    # 6. Tên bài học / Chủ đề
    lesson_name = st.text_input(
        "Tên bài học / Chủ đề:",
        value=st.session_state.get("lesson_input_value", f"Chủ đề môn {subject}"),
        placeholder=f"Nhập tên bài dạy môn {subject}..."
    )

    # 7. Thời lượng
    duration = st.selectbox(
        "Thời lượng bài dạy:",
        ["1 tiết (45 phút)", "2 tiết (90 phút)", "3 tiết (135 phút)", "4 tiết (180 phút)", "Tùy chỉnh khác"],
        index=1
    )

    # 8. Ghi chú sư phạm bổ sung
    special_notes = st.text_area(
        "Ghi chú sư phạm / Phương pháp (Tùy chọn):",
        value=st.session_state.get("notes_input_value", ""),
        placeholder="Ví dụ: Tích hợp STEM, rèn luyện làm việc nhóm, học sinh khá giỏi..."
    )

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 9. Nút tạo nội dung AI
    btn_generate = st.button(f"Xuất bản Trọn bộ Tài liệu ({subject})", type="primary", use_container_width=True)
    
    # Nút nạp lại mẫu chuẩn của môn đang chọn
    btn_sample = st.button(f"Nạp Dữ liệu Mẫu ({subject} - {grade})", use_container_width=True)
    if btn_sample:
        st.session_state["current_package"] = get_sample_package_for_subject(
            subject=subject,
            grade=grade,
            grade_level=grade_level,
            book_series=book_series,
            custom_lesson_name=lesson_name,
            custom_notes=special_notes
        )
        st.toast(f"Đã nạp trọn bộ dữ liệu mẫu môn {subject} ({grade}) thành công!", icon="✅")
        st.rerun()

    st.divider()
    st.markdown("""
    <div style="font-size: 0.74rem; color: #64748B; line-height: 1.5;">
        <i class="fa-solid fa-scale-balanced" style="color: #2563EB;"></i> <b>Khung pháp lý áp dụng:</b><br>
        • <b>CV 5512/BGDĐT-GDTrH</b>: Khung bài dạy 4 hoạt động.<br>
        • <b>CV 7991/BGDĐT-GDTrH (17/12/2024)</b>: Định dạng đề kiểm tra 4 phần & tỉ lệ nhận thức Biết (40%) - Hiểu (30%) - Vận dụng (30%).
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# XỬ LÝ SỰ KIỆN TẠO MỚI NỘI DUNG VỚI AI
# ==========================================
if btn_generate:
    if not lesson_name.strip():
        st.warning(f"Vui lòng nhập tên bài học môn {subject}.")
    elif not api_key_input:
        # Nếu chưa có API Key: Tự động khởi tạo trọn bộ mẫu chuẩn hóa cho môn và chủ đề đang nhập
        st.session_state["current_package"] = get_sample_package_for_subject(
            subject=subject,
            grade=grade,
            grade_level=grade_level,
            book_series=book_series,
            custom_lesson_name=lesson_name,
            custom_notes=special_notes
        )
        st.info(f"ℹ️ **Chế độ xem thử chuẩn hóa:** Đã khởi tạo hồ sơ sư phạm môn **{subject} ({grade})** với bài **{lesson_name}**. Hãy nhập Gemini API Key để kích hoạt AI sáng tạo nội dung tùy biến trực tiếp!")
        st.rerun()
    else:
        with st.spinner(f"EduMaster AI đang biên soạn hồ sơ sư phạm môn {subject} ({grade}) chuẩn CV 5512 và CV 7991..."):
            try:
                new_data = generate_pedagogical_package(
                    api_key=api_key_input,
                    grade_level=grade_level,
                    grade=grade,
                    subject=subject,
                    book_series=book_series,
                    lesson_name=lesson_name,
                    duration=duration,
                    special_notes=special_notes,
                    model_name=model_choice
                )
                
                # Cập nhật session state
                st.session_state["current_package"] = {
                    "metadata": {
                        "grade_level": grade_level,
                        "grade": grade,
                        "subject": subject,
                        "book_series": book_series,
                        "lesson_name": lesson_name,
                        "duration": duration,
                        "special_notes": special_notes
                    },
                    "lesson_plan": new_data.get("lesson_plan_markdown", ""),
                    "slides": new_data.get("slides", []),
                    "exam_matrix": new_data.get("exam_matrix_markdown", ""),
                    "exam_spec": new_data.get("exam_spec_markdown", ""),
                    "exam_questions": new_data.get("exam_questions_markdown", ""),
                    "exam_answers": new_data.get("exam_answers_markdown", ""),
                    "pedagogical_summary": new_data.get("pedagogical_summary", f"Đã khởi tạo hoàn tất hồ sơ sư phạm môn {subject} chất lượng cao.")
                }
                st.toast(f"Đã xuất bản trọn bộ tài liệu môn {subject} thành công!", icon="✅")
                st.rerun()
            except Exception as e:
                st.error(f"Có lỗi xảy ra trong quá trình khởi tạo AI: {str(e)}")


# ==========================================
# GIAO DIỆN CHÍNH (MAIN CONTENT)
# ==========================================
current_pkg = st.session_state["current_package"]
cur_meta = current_pkg.get("metadata", {})

# 1. Hero Header Banner
st.markdown(f"""
<div class="hero-container">
    <div class="hero-title">
        <span>EduMaster AI</span>
        <span class="hero-version-pill">
            <i class="fa-solid fa-sparkles"></i> Sư phạm 2025
        </span>
    </div>
    <div class="hero-subtitle">
        Hệ thống Tự động hóa Soạn Kế hoạch bài dạy chuẩn <b>Công văn 5512/BGDĐT-GDTrH</b> và Thiết kế Đề kiểm tra định kì chuẩn hóa 
        theo <b>Công văn 7991/BGDĐT-GDTrH</b> ngày 17/12/2024 của Bộ GDĐT dành cho Giáo viên THCS & THPT.
    </div>
    <div class="hero-badges">
        <span class="badge-pill"><i class="fa-solid fa-file-shield" style="color: #38BDF8;"></i> Chuẩn CV 5512/BGDĐT-GDTrH</span>
        <span class="badge-pill"><i class="fa-solid fa-scale-balanced" style="color: #4ADE80;"></i> Chuẩn CV 7991/BGDĐT-GDTrH (17/12/2024)</span>
        <span class="badge-pill"><i class="fa-solid fa-layer-group" style="color: #A78BFA;"></i> CT GDPT 2018 (Phát triển Năng lực)</span>
        <span class="badge-pill"><i class="fa-solid fa-location-dot" style="color: #FBBF24;"></i> Giáo dục Vĩnh Long & Toàn quốc</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 2. Thẻ tóm tắt thông tin hiện hành (Overview Metrics)
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"""
    <div class="metric-card-box">
        <div>
            <div class="metric-info-label">Môn học & Lớp</div>
            <div class="metric-info-val">{cur_meta.get('subject', subject)} - {cur_meta.get('grade', grade)}</div>
        </div>
        <div class="metric-icon-circle icon-blue">
            <i class="fa-solid fa-book-open"></i>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card-box">
        <div>
            <div class="metric-info-label">Bộ sách & Thời lượng</div>
            <div class="metric-info-val" style="font-size: 0.95rem;">{cur_meta.get('book_series', 'KNTT')} ({cur_meta.get('duration', '2 tiết')})</div>
        </div>
        <div class="metric-icon-circle icon-teal">
            <i class="fa-solid fa-clock"></i>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card-box">
        <div>
            <div class="metric-info-label">Trình chiếu Slide</div>
            <div class="metric-info-val">{len(current_pkg.get('slides', []))} Trang + Lời giảng</div>
        </div>
        <div class="metric-icon-circle icon-indigo">
            <i class="fa-solid fa-chalkboard-user"></i>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card-box">
        <div>
            <div class="metric-info-label">Đề khảo thí 7991</div>
            <div class="metric-info-val">4 Phần (40 - 30 - 30)</div>
        </div>
        <div class="metric-icon-circle icon-amber">
            <i class="fa-solid fa-clipboard-check"></i>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 3. TRUNG TÂM XUẤT BẢN & TẢI FILE (DOWNLOAD CENTER)
st.markdown("""
<div class="section-head-title">
    <i class="fa-solid fa-cloud-arrow-down" style="color: #2563EB;"></i> Trung tâm Xuất bản Tài liệu Thực tế
</div>
""", unsafe_allow_html=True)

try:
    docx_bytes = export_to_docx(
        metadata=cur_meta,
        lesson_plan_md=current_pkg.get("lesson_plan", ""),
        exam_matrix_md=current_pkg.get("exam_matrix", ""),
        exam_spec_md=current_pkg.get("exam_spec", ""),
        exam_questions_md=current_pkg.get("exam_questions", ""),
        exam_answers_md=current_pkg.get("exam_answers", "")
    )
except Exception as e_docx:
    docx_bytes = None

try:
    pptx_bytes = export_to_pptx(
        metadata=cur_meta,
        slides_data=current_pkg.get("slides", [])
    )
except Exception as e_pptx:
    pptx_bytes = None

# Tạo nội dung Markdown tổng hợp để tải nhanh
full_markdown_text = f"""# {cur_meta.get('lesson_name', 'HỒ SƠ SƯ PHẠM')}
**Môn:** {cur_meta.get('subject')} | **Lớp:** {cur_meta.get('grade')} | **Bộ sách:** {cur_meta.get('book_series')}
**Thời lượng:** {cur_meta.get('duration')} | **Khung chuẩn:** CV 5512 & CV 7991

---

{current_pkg.get('lesson_plan', '')}

---

{current_pkg.get('exam_matrix', '')}

---

{current_pkg.get('exam_spec', '')}

---

{current_pkg.get('exam_questions', '')}

---

{current_pkg.get('exam_answers', '')}
"""

col_d1, col_d2, col_d3 = st.columns([1.2, 1.2, 1])

with col_d1:
    if docx_bytes:
        clean_subj = cur_meta.get('subject', 'Mon').replace(' ', '_').replace('(', '').replace(')', '')
        clean_name = cur_meta.get('lesson_name', 'Ho_So_Su_Pham').replace(' ', '_').replace(':', '')[:30]
        st.download_button(
            label=f"Tải Giáo án & Đề thi ({cur_meta.get('subject')}) (.docx)",
            data=docx_bytes.getvalue(),
            file_name=f"EduMaster_{clean_subj}_{clean_name}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            type="primary",
            use_container_width=True,
            help="File Word hoàn chỉnh với bảng biểu, căn lề chuẩn hành chính (Top/Bottom 2cm, Left 2.5cm, Right 2cm), viền kẻ sẵn sàng in ấn."
        )

with col_d2:
    if pptx_bytes:
        clean_subj = cur_meta.get('subject', 'Mon').replace(' ', '_').replace('(', '').replace(')', '')
        clean_name = cur_meta.get('lesson_name', 'Bai_Giang').replace(' ', '_').replace(':', '')[:30]
        st.download_button(
            label=f"Tải Bài giảng Trình chiếu ({cur_meta.get('subject')}) (.pptx)",
            data=pptx_bytes.getvalue(),
            file_name=f"EduMaster_{clean_subj}_{clean_name}.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            type="secondary",
            use_container_width=True,
            help="File PowerPoint chuẩn tỉ lệ 16:9, có bố cục thẻ nội dung, ý tưởng trực quan và Speaker Notes tích hợp."
        )

with col_d3:
    clean_subj = cur_meta.get('subject', 'Mon').replace(' ', '_').replace('(', '').replace(')', '')
    st.download_button(
        label=f"Tải Toàn văn Markdown (.md)",
        data=full_markdown_text.encode('utf-8'),
        file_name=f"EduMaster_{clean_subj}.md",
        mime="text/markdown",
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# 4. KHU VỰC HIỂN THỊ KẾT QUẢ VỚI 3 TAB CHÍNH
tab1, tab2, tab3 = st.tabs([
    "KẾ HOẠCH BÀI DẠY (CV 5512)",
    "DÀN Ý & BÀI GIẢNG SLIDE",
    "ĐỀ KIỂM TRA & MA TRẬN ĐẶC TẢ (CV 7991)"
])

# === TAB 1: KẾ HOẠCH BÀI DẠY (CV 5512) ===
with tab1:
    st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.8rem;">
        <div style="font-size: 1.1rem; font-weight: 700; color: #0F172A;">
            <i class="fa-solid fa-file-lines" style="color: #2563EB;"></i> Kế hoạch bài dạy môn {cur_meta.get('subject')} - {cur_meta.get('grade')}
        </div>
        <span style="font-size: 0.8rem; background: #EFF6FF; color: #1D4ED8; padding: 4px 10px; border-radius: 6px; font-weight: 600;">
            Chuẩn CV 5512/BGDĐT
        </span>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Quy trình 4 hoạt động: Khởi động ➔ Hình thành kiến thức mới ➔ Luyện tập ➔ Vận dụng; Đầy đủ 4 bước sư phạm: Chuyển giao - Thực hiện - Báo cáo - Kết luận.")
    st.divider()
    st.markdown(current_pkg.get("lesson_plan", "*Chưa có nội dung kế hoạch bài dạy.*"))


# === TAB 2: DÀN Ý & TRÌNH CHIẾU SLIDE ===
with tab2:
    slides = current_pkg.get("slides", [])
    st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.8rem;">
        <div style="font-size: 1.1rem; font-weight: 700; color: #0F172A;">
            <i class="fa-solid fa-display" style="color: #2563EB;"></i> Dàn ý & Trình chiếu Bài giảng môn {cur_meta.get('subject')} ({len(slides)} Trang Slide)
        </div>
        <span style="font-size: 0.8rem; background: #F5F3FF; color: #6D28D9; padding: 4px 10px; border-radius: 6px; font-weight: 600;">
            Tỉ lệ chuẩn 16:9 + Lời giảng
        </span>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Bố cục thẻ thông tin cô đọng, có gợi ý ý tưởng hình ảnh trực quan và Lời giảng cụ thể của giáo viên trong từng slide.")
    st.divider()
    
    if not slides:
        st.info("Chưa có danh sách slide.")
    else:
        for idx, slide in enumerate(slides):
            slide_no = slide.get("slide_number", idx + 1)
            title = slide.get("title", f"Slide {slide_no}")
            bullets = slide.get("bullets", [])
            visual = slide.get("visual_prompt", "")
            notes = slide.get("speaker_notes", "")
            
            with st.container():
                st.markdown(f"""
                <div class="slide-card-container">
                    <div class="slide-header-bar">
                        <span class="slide-badge-num">
                            <i class="fa-solid fa-tv"></i> SLIDE #{slide_no:02d}
                        </span>
                    </div>
                    <div class="slide-card-title">{title}</div>
                """, unsafe_allow_html=True)
                
                # Hiển thị gạch đầu dòng
                for b in bullets:
                    st.markdown(f"• **{b}**")
                    
                # Hộp Visual Hint
                if visual:
                    st.markdown(f"""
                    <div class="slide-visual-card">
                        <i class="fa-solid fa-wand-magic-sparkles" style="color: #6366F1;"></i> <b>Gợi ý minh họa trực quan:</b> {visual}
                    </div>
                    """, unsafe_allow_html=True)
                    
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Expander Speaker Notes
                if notes:
                    with st.expander(f"Lời giảng của Giáo viên (Speaker Notes) - Slide {slide_no}"):
                        st.markdown(f"*{notes}*")
                
                st.write("")


# === TAB 3: ĐỀ KIỂM TRA ĐỊNH KÌ (CV 7991) ===
with tab3:
    st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.8rem;">
        <div style="font-size: 1.1rem; font-weight: 700; color: #0F172A;">
            <i class="fa-solid fa-clipboard-check" style="color: #2563EB;"></i> Đề kiểm tra định kì môn {cur_meta.get('subject')} - {cur_meta.get('grade')}
        </div>
        <span style="font-size: 0.8rem; background: #ECFDF5; color: #047857; padding: 4px 10px; border-radius: 6px; font-weight: 600;">
            Chuẩn CV 7991 (17/12/2024)
        </span>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Khung ma trận 4 phần chuẩn xác: TN nhiều lựa chọn (3,0đ), Đúng - Sai (2,0đ), Trả lời ngắn (2,0đ), Tự luận (3,0đ). Tỉ lệ nhận thức: 40% Biết - 30% Hiểu - 30% Vận dụng.")
    st.divider()

    sub_tab_a, sub_tab_b, sub_tab_c, sub_tab_d = st.tabs([
        "1. Ma trận đề kiểm tra",
        "2. Bản đặc tả đề kiểm tra",
        "3. Đề kiểm tra chi tiết (4 Phần)",
        "4. Hướng dẫn chấm & Đáp án"
    ])
    
    with sub_tab_a:
        st.markdown(current_pkg.get("exam_matrix", "*Chưa có ma trận đề kiểm tra.*"))
        
    with sub_tab_b:
        st.markdown(current_pkg.get("exam_spec", "*Chưa có bản đặc tả đề kiểm tra.*"))
        
    with sub_tab_c:
        st.markdown(current_pkg.get("exam_questions", "*Chưa có câu hỏi đề kiểm tra.*"))
        
    with sub_tab_d:
        st.markdown(current_pkg.get("exam_answers", "*Chưa có hướng dẫn chấm và đáp án.*"))


# ==========================================
# FOOTER BẢN QUYỀN
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 0.85rem; padding: 1rem 0; line-height: 1.6;">
    <b>EduMaster AI</b> • Giải pháp Chuyển đổi số Sư phạm & Nâng cao năng lực Khảo thí THCS/THPT<br>
    Ứng dụng Trí tuệ Nhân tạo đồng hành cùng Thầy Cô tỉnh Vĩnh Long và toàn quốc.<br>
    <i>Tuân thủ nghiêm ngặt Công văn số 5512/BGDĐT-GDTrH và Công văn số 7991/BGDĐT-GDTrH (17/12/2024) của Bộ GDĐT.</i>
</div>
""", unsafe_allow_html=True)
