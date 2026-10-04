# -*- coding: utf-8 -*-
"""
EduMaster AI - Hệ thống Soạn giảng & Khảo thí chuẩn Công văn 7991 & 5512
Ứng dụng Web dành cho Giáo viên THCS và THPT (tỉnh Vĩnh Long và toàn quốc).
Tối ưu hóa hiển thị Mobile-First, Tinh gọn cài đặt, Trực quan hóa kết quả và Slide kèm hình ảnh minh họa thực tế.
"""

import os
import streamlit as st
import io

from sample_data import (
    SUBJECT_PRESETS,
    get_sample_package_for_subject,
    attach_slide_images
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
    initial_sidebar_state="auto"
)

# ==========================================
# CUSTOM CSS RESPONSIVE & MOBILE-FIRST
# ==========================================
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2.5rem;
    }

    /* Sidebar Brand Card */
    .sidebar-brand-card {
        display: flex;
        align-items: center;
        gap: 12px;
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        padding: 12px 14px;
        border-radius: 12px;
        color: white;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
    }
    .brand-icon-box {
        width: 38px;
        height: 38px;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.15rem;
        flex-shrink: 0;
    }
    .brand-title {
        font-weight: 800;
        font-size: 1.1rem;
        letter-spacing: -0.3px;
        line-height: 1.2;
    }
    .brand-sub {
        font-size: 0.72rem;
        color: #BFDBFE;
        font-weight: 500;
    }

    /* Hero Header */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 55%, #2563EB 100%);
        padding: 1.6rem 1.8rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 1.2rem;
        box-shadow: 0 10px 25px -5px rgba(30, 58, 138, 0.25);
        position: relative;
        overflow: hidden;
    }
    .hero-title {
        font-size: 1.85rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 0.4rem;
        display: flex;
        align-items: center;
        gap: 12px;
        flex-wrap: wrap;
    }
    .hero-version-pill {
        font-size: 0.78rem;
        font-weight: 600;
        background: rgba(255, 255, 255, 0.16);
        border: 1px solid rgba(255, 255, 255, 0.25);
        padding: 3px 10px;
        border-radius: 20px;
    }
    .hero-subtitle {
        font-size: 0.95rem;
        color: #E2E8F0;
        line-height: 1.5;
        max-width: 950px;
    }
    .hero-badges {
        display: flex;
        gap: 8px;
        margin-top: 0.9rem;
        flex-wrap: wrap;
    }
    .badge-pill {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(8px);
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.22);
        color: #F8FAFC;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    
    /* Overview Metric Card */
    .metric-card-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 0.9rem 1.1rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        margin-bottom: 0.5rem;
    }
    .metric-info-label {
        font-size: 0.74rem;
        color: #64748B;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }
    .metric-info-val {
        font-size: 1.05rem;
        font-weight: 700;
        color: #0F172A;
        margin-top: 2px;
    }
    .metric-icon-circle {
        width: 38px;
        height: 38px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
        flex-shrink: 0;
    }
    .icon-blue { background: #EFF6FF; color: #2563EB; }
    .icon-teal { background: #F0FDFA; color: #0D9488; }
    .icon-indigo { background: #EEF2FF; color: #4F46E5; }
    .icon-amber { background: #FFFBEB; color: #D97706; }

    /* Visual Summary Cards (Trực quan hóa Kế hoạch 5512) */
    .visual-summary-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
        margin-bottom: 1.2rem;
    }
    .visual-summary-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1rem 1.1rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.02);
    }
    .visual-summary-head {
        font-size: 0.82rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 0.5rem;
    }
    .visual-summary-head.blue { color: #2563EB; }
    .visual-summary-head.purple { color: #7C3AED; }
    .visual-summary-head.amber { color: #D97706; }

    /* Visual Activity Card (4 Bước CV 5512) */
    .activity-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #2563EB;
        border-radius: 12px;
        padding: 1.1rem 1.3rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.02);
    }
    .activity-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 0.6rem;
        flex-wrap: wrap;
        gap: 6px;
    }
    .activity-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #0F172A;
    }
    .activity-duration {
        font-size: 0.78rem;
        font-weight: 600;
        background: #EFF6FF;
        color: #1D4ED8;
        padding: 3px 8px;
        border-radius: 6px;
    }
    .activity-steps-flow {
        display: flex;
        gap: 6px;
        margin-top: 0.6rem;
        flex-wrap: wrap;
    }
    .step-pill {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 600;
        color: #334155;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }

    /* SLIDE CARD CÓ HÌNH ẢNH MINH HỌA */
    .slide-card-container {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-top: 4px solid #2563EB;
        border-radius: 14px;
        padding: 1.2rem;
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
    .slide-grid-layout {
        display: grid;
        grid-template-columns: 280px 1fr;
        gap: 16px;
        align-items: start;
    }
    .slide-illustration-box {
        position: relative;
        border-radius: 10px;
        overflow: hidden;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }
    .slide-illustration-img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        display: block;
        transition: transform 0.3s ease;
    }
    .slide-illustration-img:hover {
        transform: scale(1.03);
    }
    .slide-visual-hint {
        padding: 8px 10px;
        background: #F8FAFC;
        font-size: 0.78rem;
        color: #475569;
        line-height: 1.4;
        border-top: 1px solid #E2E8F0;
    }
    .slide-title-text {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 0.6rem;
    }
    .slide-bullet-item {
        font-size: 0.9rem;
        color: #1E293B;
        margin-bottom: 6px;
        line-height: 1.45;
        display: flex;
        gap: 8px;
    }
    .speaker-notes-box {
        background: #FFFBEB;
        border-left: 3px solid #D97706;
        padding: 0.75rem 1rem;
        border-radius: 0 8px 8px 0;
        font-size: 0.85rem;
        color: #78350F;
        margin-top: 0.8rem;
        line-height: 1.45;
    }

    /* KPI Khảo thí CV 7991 */
    .exam-kpi-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin-bottom: 1.2rem;
    }
    .exam-kpi-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 0.8rem 1rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .exam-kpi-score {
        font-size: 1.3rem;
        font-weight: 800;
        color: #2563EB;
    }
    .exam-kpi-name {
        font-size: 0.75rem;
        font-weight: 600;
        color: #64748B;
        text-transform: uppercase;
        margin-top: 2px;
    }

    /* MOBILE-FIRST RESPONSIVE MEDIA QUERIES */
    @media (max-width: 768px) {
        .block-container {
            padding-top: 0.8rem !important;
            padding-left: 0.8rem !important;
            padding-right: 0.8rem !important;
        }
        .hero-container {
            padding: 1.2rem 1.2rem !important;
            border-radius: 14px !important;
        }
        .hero-title {
            font-size: 1.45rem !important;
            gap: 8px !important;
        }
        .hero-subtitle {
            font-size: 0.86rem !important;
            line-height: 1.45 !important;
        }
        .badge-pill {
            font-size: 0.72rem !important;
            padding: 4px 10px !important;
        }
        .visual-summary-container {
            grid-template-columns: 1fr !important;
        }
        .slide-grid-layout {
            grid-template-columns: 1fr !important;
        }
        .slide-illustration-img {
            height: 160px !important;
        }
        .exam-kpi-grid {
            grid-template-columns: repeat(2, 1fr) !important;
        }
        .stButton>button {
            padding: 0.65rem 1rem !important;
            font-size: 0.9rem !important;
        }
    }

    /* Style Buttons */
    .stButton>button {
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# KHỞI TẠO STATE
# ==========================================
if "active_subject" not in st.session_state:
    st.session_state["active_subject"] = "Vật lí"

if "active_grade" not in st.session_state:
    st.session_state["active_grade"] = "Lớp 10"

if "lesson_input_value" not in st.session_state:
    st.session_state["lesson_input_value"] = SUBJECT_PRESETS["Vật lí"]["lesson_name"]

if "current_package" not in st.session_state:
    st.session_state["current_package"] = get_sample_package_for_subject(
        subject="Vật lí",
        grade="Lớp 10",
        grade_level="THPT"
    )


# ==========================================
# SIDEBAR - CẤU HÌNH ĐẦU VÀO TINH GỌN (SIMPLIFIED SETTINGS)
# ==========================================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand-card">
        <div class="brand-icon-box">
            <i class="fa-solid fa-graduation-cap"></i>
        </div>
        <div class="brand-text-box">
            <div class="brand-title">EduMaster AI</div>
            <div class="brand-sub">Soạn giảng 5512 & Khảo thí 7991</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 1. Cấp học & Khối lớp
    col_level, col_grade = st.columns([1, 1])
    with col_level:
        grade_level = st.radio("Cấp học:", options=["THCS", "THPT"], index=1)
        
    with col_grade:
        if grade_level == "THCS":
            grade = st.selectbox("Khối lớp:", ["Lớp 6", "Lớp 7", "Lớp 8", "Lớp 9"], index=2)
        else:
            grade = st.selectbox("Khối lớp:", ["Lớp 10", "Lớp 11", "Lớp 12"], index=0)

    # 2. Môn học
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
        
    def_idx = 0
    if st.session_state["active_subject"] in subject_list:
        def_idx = subject_list.index(st.session_state["active_subject"])
        
    subject = st.selectbox("Môn học:", subject_list, index=def_idx)

    # Tự động đồng bộ đề tài khi đổi môn
    if subject != st.session_state.get("active_subject") or grade != st.session_state.get("active_grade"):
        st.session_state["active_subject"] = subject
        st.session_state["active_grade"] = grade
        preset = SUBJECT_PRESETS.get(subject, {})
        new_lesson = preset.get("lesson_name", f"Chủ đề trọng tâm môn {subject} - {grade}")
        st.session_state["lesson_input_value"] = new_lesson
        st.session_state["current_package"] = get_sample_package_for_subject(
            subject=subject,
            grade=grade,
            grade_level=grade_level,
            book_series="Kết nối tri thức với cuộc sống",
            custom_lesson_name=new_lesson
        )
        st.rerun()

    # 3. Bộ sách giáo khoa
    book_series = st.selectbox(
        "Bộ sách giáo khoa:",
        ["Kết nối tri thức với cuộc sống", "Cánh diều", "Chân trời sáng tạo"],
        index=0
    )

    # 4. Tên bài học / Chủ đề
    lesson_name = st.text_input(
        "Tên bài học / Chủ đề:",
        value=st.session_state.get("lesson_input_value", f"Chủ đề môn {subject}"),
        placeholder=f"Nhập tên bài dạy môn {subject}..."
    )

    duration = "2 tiết (90 phút)"

    # 5. CÀI ĐẶT NÂNG CAO (GOM GỌN ĐỂ TRÁNH RỐI GIAO DIỆN)
    with st.expander("⚙️ Cài đặt Nâng cao (API Key & Model)", expanded=False):
        default_api_key = os.environ.get("GEMINI_API_KEY", "")
        if not default_api_key:
            try:
                secrets_path = os.path.join(os.path.dirname(__file__), ".streamlit", "secrets.toml")
                if os.path.exists(secrets_path) and hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
                    default_api_key = st.secrets["GEMINI_API_KEY"]
            except Exception:
                default_api_key = ""
                
        api_key_input = st.text_input(
            "Gemini API Key:",
            value=default_api_key,
            type="password",
            placeholder="AIzaSy...",
            help="Tùy chọn: Nhập API Key để AI sinh nội dung mới trực tiếp từ Google AI Studio."
        )

        model_choice = st.selectbox(
            "Mô hình AI:",
            options=["gemini-2.5-flash", "gemini-1.5-flash", "gemini-1.5-pro"],
            index=0
        )
        
        special_notes = st.text_area(
            "Ghi chú sư phạm riêng:",
            value=SUBJECT_PRESETS.get(subject, {}).get("special_notes", ""),
            placeholder="Ví dụ: Tích hợp STEM, dạy học theo trạm..."
        )

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 6. Nút kích hoạt chính
    btn_generate = st.button(f"🚀 XUẤT BẢN HỒ SƠ BÀI DẠY ({subject.upper()})", type="primary", use_container_width=True)
    btn_sample = st.button(f"🎯 Nạp Mẫu Chuẩn ({subject} - {grade})", use_container_width=True)
    
    if btn_sample:
        st.session_state["current_package"] = get_sample_package_for_subject(
            subject=subject,
            grade=grade,
            grade_level=grade_level,
            book_series=book_series,
            custom_lesson_name=lesson_name
        )
        st.toast(f"Đã nạp gói mẫu chuẩn môn {subject} ({grade}) thành công!", icon="✅")
        st.rerun()

    st.caption("⚡ *Hệ thống tự động đồng bộ theo môn học và lớp được chọn.*")


# ==========================================
# XỬ LÝ SỰ KIỆN TẠO MỚI NỘI DUNG VỚI AI
# ==========================================
if btn_generate:
    if not lesson_name.strip():
        st.warning(f"Vui lòng nhập tên bài học môn {subject}.")
    elif not api_key_input:
        st.session_state["current_package"] = get_sample_package_for_subject(
            subject=subject,
            grade=grade,
            grade_level=grade_level,
            book_series=book_series,
            custom_lesson_name=lesson_name
        )
        st.toast(f"Đã chuẩn hóa bài dạy môn {subject} ({grade})!", icon="✨")
        st.rerun()
    else:
        with st.spinner(f"EduMaster AI đang biên soạn hồ sơ sư phạm môn {subject} ({grade}) chuẩn CV 5512 & CV 7991..."):
            try:
                new_data = generate_pedagogical_package(
                    api_key=api_key_input,
                    grade_level=grade_level,
                    grade=grade,
                    subject=subject,
                    book_series=book_series,
                    lesson_name=lesson_name,
                    duration=duration,
                    special_notes=special_notes if 'special_notes' in locals() else "",
                    model_name=model_choice
                )
                
                # Gắn hình ảnh minh họa cho slide do AI sinh ra
                raw_slides = new_data.get("slides", [])
                slides_with_img = attach_slide_images(subject, raw_slides)
                
                st.session_state["current_package"] = {
                    "metadata": {
                        "grade_level": grade_level,
                        "grade": grade,
                        "subject": subject,
                        "book_series": book_series,
                        "lesson_name": lesson_name,
                        "duration": duration,
                        "special_notes": special_notes if 'special_notes' in locals() else ""
                    },
                    "lesson_plan": new_data.get("lesson_plan_markdown", ""),
                    "slides": slides_with_img,
                    "exam_matrix": new_data.get("exam_matrix_markdown", ""),
                    "exam_spec": new_data.get("exam_spec_markdown", ""),
                    "exam_questions": new_data.get("exam_questions_markdown", ""),
                    "exam_answers": new_data.get("exam_answers_markdown", ""),
                    "pedagogical_summary": new_data.get("pedagogical_summary", f"Đã khởi tạo hoàn tất hồ sơ sư phạm môn {subject} chất lượng cao.")
                }
                st.toast(f"Đã xuất bản trọn bộ tài liệu môn {subject} thành công!", icon="✅")
                st.rerun()
            except Exception as e:
                st.error(f"Có lỗi xảy ra: {str(e)}")


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
        Trợ lý Soạn Kế hoạch bài dạy chuẩn <b>Công văn 5512</b> và Thiết kế Đề kiểm tra định kì chuẩn hóa 
        theo <b>Công văn 7991</b> (ngày 17/12/2024) của Bộ GDĐT dành cho Giáo viên THCS & THPT.
    </div>
    <div class="hero-badges">
        <span class="badge-pill"><i class="fa-solid fa-file-shield" style="color: #38BDF8;"></i> CV 5512/BGDĐT</span>
        <span class="badge-pill"><i class="fa-solid fa-scale-balanced" style="color: #4ADE80;"></i> CV 7991/BGDĐT</span>
        <span class="badge-pill"><i class="fa-solid fa-layer-group" style="color: #A78BFA;"></i> CT GDPT 2018</span>
        <span class="badge-pill"><i class="fa-solid fa-location-dot" style="color: #FBBF24;"></i> Vĩnh Long & Toàn quốc</span>
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
        <div class="metric-icon-circle icon-blue"><i class="fa-solid fa-book-open"></i></div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card-box">
        <div>
            <div class="metric-info-label">Bộ sách & Thời lượng</div>
            <div class="metric-info-val" style="font-size: 0.92rem;">{cur_meta.get('book_series', 'KNTT')} (2 tiết)</div>
        </div>
        <div class="metric-icon-circle icon-teal"><i class="fa-solid fa-clock"></i></div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card-box">
        <div>
            <div class="metric-info-label">Slide có hình ảnh</div>
            <div class="metric-info-val">{len(current_pkg.get('slides', []))} Trang Slide</div>
        </div>
        <div class="metric-icon-circle icon-indigo"><i class="fa-solid fa-images"></i></div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card-box">
        <div>
            <div class="metric-info-label">Đề khảo thí 7991</div>
            <div class="metric-info-val">4 Phần (40 - 30 - 30)</div>
        </div>
        <div class="metric-icon-circle icon-amber"><i class="fa-solid fa-clipboard-check"></i></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 3. TRUNG TÂM XUẤT BẢN & TẢI FILE (DOWNLOAD CENTER)
try:
    docx_bytes = export_to_docx(
        metadata=cur_meta,
        lesson_plan_md=current_pkg.get("lesson_plan", ""),
        exam_matrix_md=current_pkg.get("exam_matrix", ""),
        exam_spec_md=current_pkg.get("exam_spec", ""),
        exam_questions_md=current_pkg.get("exam_questions", ""),
        exam_answers_md=current_pkg.get("exam_answers", "")
    )
except Exception:
    docx_bytes = None

try:
    pptx_bytes = export_to_pptx(
        metadata=cur_meta,
        slides_data=current_pkg.get("slides", [])
    )
except Exception:
    pptx_bytes = None

col_d1, col_d2, col_d3 = st.columns([1.2, 1.2, 1])

with col_d1:
    if docx_bytes:
        clean_subj = cur_meta.get('subject', 'Mon').replace(' ', '_').replace('(', '').replace(')', '')
        st.download_button(
            label=f"📄 Tải Hồ sơ Giáo án & Đề thi (.docx)",
            data=docx_bytes.getvalue(),
            file_name=f"EduMaster_{clean_subj}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            type="primary",
            use_container_width=True
        )

with col_d2:
    if pptx_bytes:
        clean_subj = cur_meta.get('subject', 'Mon').replace(' ', '_').replace('(', '').replace(')', '')
        st.download_button(
            label=f"📊 Tải Bài giảng Slide (.pptx)",
            data=pptx_bytes.getvalue(),
            file_name=f"EduMaster_{clean_subj}_Slide.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            type="secondary",
            use_container_width=True
        )

with col_d3:
    clean_subj = cur_meta.get('subject', 'Mon').replace(' ', '_').replace('(', '').replace(')', '')
    full_md = f"# {cur_meta.get('lesson_name')}\n\n{current_pkg.get('lesson_plan')}\n\n{current_pkg.get('exam_matrix')}\n\n{current_pkg.get('exam_questions')}"
    st.download_button(
        label="📋 Tải Toàn văn (.md)",
        data=full_md.encode('utf-8'),
        file_name=f"EduMaster_{clean_subj}.md",
        mime="text/markdown",
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# 4. KHU VỰC HIỂN THỊ KẾT QUẢ VỚI 3 TAB TRỰC QUAN
tab1, tab2, tab3 = st.tabs([
    "KẾ HOẠCH BÀI DẠY (CV 5512)",
    "BÀI GIẢNG SLIDE (KÈM HÌNH ẢNH)",
    "ĐỀ KIỂM TRA ĐỊNH KÌ (CV 7991)"
])

# === TAB 1: KẾ HOẠCH BÀI DẠY (TRỰC QUAN HÓA, ÍT CHỮ DÀY ĐẶC) ===
with tab1:
    st.markdown(f"""
    <div style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin-bottom: 0.6rem;">
        <i class="fa-solid fa-file-lines" style="color: #2563EB;"></i> Kế hoạch bài dạy: {cur_meta.get('lesson_name')}
    </div>
    """, unsafe_allow_html=True)
    
    # Thẻ tóm tắt 3 Trụ cột Mục tiêu (Visual Pillars)
    st.markdown("""
    <div class="visual-summary-container">
        <div class="visual-summary-card">
            <div class="visual-summary-head blue">
                <i class="fa-solid fa-brain"></i> 1. Kiến thức trọng tâm
            </div>
            <div style="font-size: 0.88rem; color: #334155; line-height: 1.45;">
                • Nắm vững các định nghĩa, công thức và nguyên lí nền tảng.<br>
                • Phân tích mối liên hệ logic giữa lí thuyết và hiện tượng thực tiễn.<br>
                • Biết cách vận dụng kiến thức giải quyết bài toán định lượng.
            </div>
        </div>
        <div class="visual-summary-card">
            <div class="visual-summary-head purple">
                <i class="fa-solid fa-gears"></i> 2. Năng lực cốt lõi
            </div>
            <div style="font-size: 0.88rem; color: #334155; line-height: 1.45;">
                • <b>Năng lực chung:</b> Tự chủ, tự học và hợp tác nhóm hiệu quả.<br>
                • <b>Năng lực đặc thù:</b> Nhận thức môn học và mô hình hóa giải quyết vấn đề đời sống.
            </div>
        </div>
        <div class="visual-summary-card">
            <div class="visual-summary-head amber">
                <i class="fa-solid fa-heart"></i> 3. Phẩm chất rèn luyện
            </div>
            <div style="font-size: 0.88rem; color: #334155; line-height: 1.45;">
                • <b>Chăm chỉ:</b> Chủ động tìm tòi, ghi chép số liệu trung thực.<br>
                • <b>Trách nhiệm:</b> Hoàn thành đúng tiến độ nhiệm vụ chung.<br>
                • Bồi dưỡng tình yêu khoa học và ý thức cộng đồng.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### Tiến trình 4 Hoạt động Dạy học (Chuẩn CV 5512/BGDĐT-GDTrH)")

    # Hoạt động 1
    st.markdown("""
    <div class="activity-card">
        <div class="activity-header">
            <span class="activity-title"><i class="fa-solid fa-bolt" style="color: #2563EB;"></i> Hoạt động 1: Mở đầu / Khởi động</span>
            <span class="activity-duration">10 phút</span>
        </div>
        <div style="font-size: 0.88rem; color: #334155;">
            <b>Mục tiêu & Nhiệm vụ:</b> Tạo mâu thuẫn nhận thức từ tình huống thực tế hoặc video gợi mở; kích thích tư duy tự nhiên của học sinh.
        </div>
        <div class="activity-steps-flow">
            <span class="step-pill"><i class="fa-solid fa-1"></i> Chuyển giao: GV chiếu tình huống</span>
            <span class="step-pill"><i class="fa-solid fa-2"></i> Thực hiện: HS suy nghĩ cá nhân</span>
            <span class="step-pill"><i class="fa-solid fa-3"></i> Báo cáo: Phát biểu ý kiến</span>
            <span class="step-pill"><i class="fa-solid fa-4"></i> Kết luận: GV chốt vấn đề</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Hoạt động 2
    st.markdown("""
    <div class="activity-card" style="border-left-color: #0D9488;">
        <div class="activity-header">
            <span class="activity-title"><i class="fa-solid fa-lightbulb" style="color: #0D9488;"></i> Hoạt động 2: Hình thành kiến thức mới</span>
            <span class="activity-duration" style="background: #F0FDFA; color: #0F766E;">50 phút</span>
        </div>
        <div style="font-size: 0.88rem; color: #334155;">
            <b>Nội dung trọng tâm:</b> Phân chia các mạch kiến thức rõ ràng, học sinh nghiên cứu SGK kết hợp phiếu học tập và thực hành trải nghiệm.
        </div>
        <div class="activity-steps-flow">
            <span class="step-pill"><i class="fa-solid fa-1"></i> Giao phiếu học tập nhóm</span>
            <span class="step-pill"><i class="fa-solid fa-2"></i> Thảo luận & Xử lí dữ liệu</span>
            <span class="step-pill"><i class="fa-solid fa-3"></i> Đại diện nhóm thuyết trình</span>
            <span class="step-pill"><i class="fa-solid fa-4"></i> GV chuẩn hóa kiến thức</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Hoạt động 3
    st.markdown("""
    <div class="activity-card" style="border-left-color: #6366F1;">
        <div class="activity-header">
            <span class="activity-title"><i class="fa-solid fa-pen-ruler" style="color: #6366F1;"></i> Hoạt động 3: Luyện tập củng cố</span>
            <span class="activity-duration" style="background: #EEF2FF; color: #4338CA;">18 phút</span>
        </div>
        <div style="font-size: 0.88rem; color: #334155;">
            <b>Hệ thống bài tập:</b> Trắc nghiệm tương tác nhanh và bài tập định lượng rèn luyện kĩ năng tính toán và lập luận khoa học.
        </div>
        <div class="activity-steps-flow">
            <span class="step-pill"><i class="fa-solid fa-1"></i> Giao bài tập độc lập</span>
            <span class="step-pill"><i class="fa-solid fa-2"></i> HS làm bài vào vở</span>
            <span class="step-pill"><i class="fa-solid fa-3"></i> Lên bảng trình bày</span>
            <span class="step-pill"><i class="fa-solid fa-4"></i> GV nhận xét & sửa lỗi</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Hoạt động 4
    st.markdown("""
    <div class="activity-card" style="border-left-color: #D97706;">
        <div class="activity-header">
            <span class="activity-title"><i class="fa-solid fa-earth-americas" style="color: #D97706;"></i> Hoạt động 4: Vận dụng thực tiễn & Mở rộng</span>
            <span class="activity-duration" style="background: #FFFBEB; color: #B45309;">12 phút</span>
        </div>
        <div style="font-size: 0.88rem; color: #334155;">
            <b>Dự án học tập:</b> Giao nhiệm vụ thực hành khám phá đời sống địa phương (infographic, video, mô hình) nộp trên hệ thống học trực tuyến.
        </div>
        <div class="activity-steps-flow">
            <span class="step-pill"><i class="fa-solid fa-1"></i> GV nêu bài toán thực tiễn</span>
            <span class="step-pill"><i class="fa-solid fa-2"></i> Nhóm lên kế hoạch dự án</span>
            <span class="step-pill"><i class="fa-solid fa-3"></i> Báo cáo sản phẩm vào buổi sau</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Toàn văn chi tiết khi thầy cô cần xem hoặc in ấn
    with st.expander("📄 Xem & Sao chép Toàn văn Kế hoạch bài dạy chi tiết (Văn bản in ấn)", expanded=False):
        st.markdown(current_pkg.get("lesson_plan", ""))


# === TAB 2: BÀI GIẢNG SLIDE (KÈM HÌNH ẢNH MINH HỌA THỰC TẾ) ===
with tab2:
    slides = current_pkg.get("slides", [])
    st.markdown(f"""
    <div style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin-bottom: 0.6rem;">
        <i class="fa-solid fa-display" style="color: #2563EB;"></i> Trình chiếu Slide Bài giảng ({len(slides)} Trang Slide có Hình ảnh Minh họa)
    </div>
    """, unsafe_allow_html=True)
    st.caption("Mỗi slide đều có hình ảnh minh họa thực tế, gạch đầu dòng cô đọng và Lời giảng chi tiết của giáo viên.")
    
    for idx, slide in enumerate(slides):
        slide_no = slide.get("slide_number", idx + 1)
        title = slide.get("title", f"Slide {slide_no}")
        bullets = slide.get("bullets", [])
        visual = slide.get("visual_prompt", "")
        notes = slide.get("speaker_notes", "")
        img_url = slide.get("image_url", "https://images.unsplash.com/photo-1509062522246-3755977927d7?w=800&auto=format&fit=crop&q=80")
        
        with st.container():
            st.markdown(f"""
            <div class="slide-card-container">
                <div class="slide-header-bar">
                    <span class="slide-badge-num">
                        <i class="fa-solid fa-tv"></i> SLIDE #{slide_no:02d}
                    </span>
                    <span style="font-size: 0.78rem; font-weight: 600; color: #64748B;">
                        Trình chiếu 16:9
                    </span>
                </div>
                <div class="slide-grid-layout">
                    <div class="slide-illustration-box">
                        <img src="{img_url}" class="slide-illustration-img" alt="Minh họa slide {slide_no}" loading="lazy" />
                        <div class="slide-visual-hint">
                            <i class="fa-solid fa-wand-magic-sparkles" style="color: #6366F1;"></i> <b>Gợi ý trực quan:</b> {visual}
                        </div>
                    </div>
                    <div>
                        <div class="slide-title-text">{title}</div>
            """, unsafe_allow_html=True)
            
            for b in bullets:
                st.markdown(f"""
                <div class="slide-bullet-item">
                    <i class="fa-solid fa-circle-check" style="color: #2563EB; font-size: 0.85rem; margin-top: 3px; flex-shrink: 0;"></i>
                    <span><b>{b}</b></span>
                </div>
                """, unsafe_allow_html=True)
                
            if notes:
                st.markdown(f"""
                <div class="speaker-notes-box">
                    <i class="fa-solid fa-microphone-lines" style="color: #D97706;"></i> <b>Lời giảng của Giáo viên (Speaker Notes):</b><br>
                    <i>"{notes}"</i>
                </div>
                """, unsafe_allow_html=True)
                
            st.markdown("""
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")


# === TAB 3: ĐỀ KIỂM TRA ĐỊNH KÌ (CV 7991 - TRỰC QUAN HÓA THANG ĐIỂM) ===
with tab3:
    st.markdown(f"""
    <div style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin-bottom: 0.6rem;">
        <i class="fa-solid fa-clipboard-check" style="color: #2563EB;"></i> Đề kiểm tra định kì chuẩn hóa theo Công văn 7991/BGDĐT-GDTrH
    </div>
    """, unsafe_allow_html=True)
    
    # 4 Thẻ KPI Phân bổ điểm 7991
    st.markdown("""
    <div class="exam-kpi-grid">
        <div class="exam-kpi-card">
            <div class="exam-kpi-score">3,0 đ</div>
            <div class="exam-kpi-name">Phần I: TN 4 Lựa chọn</div>
        </div>
        <div class="exam-kpi-card">
            <div class="exam-kpi-score">2,0 đ</div>
            <div class="exam-kpi-name">Phần II: TN Đúng - Sai</div>
        </div>
        <div class="exam-kpi-card">
            <div class="exam-kpi-score">2,0 đ</div>
            <div class="exam-kpi-name">Phần III: TN Trả lời ngắn</div>
        </div>
        <div class="exam-kpi-card">
            <div class="exam-kpi-score">3,0 đ</div>
            <div class="exam-kpi-name">Phần IV: Tự luận Vận dụng</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    sub1, sub2, sub3, sub4 = st.tabs([
        "Ma trận đề kiểm tra",
        "Bản đặc tả đề kiểm tra",
        "Đề kiểm tra chi tiết",
        "Hướng dẫn chấm & Đáp án"
    ])
    
    with sub1:
        st.markdown(current_pkg.get("exam_matrix", ""))
    with sub2:
        st.markdown(current_pkg.get("exam_spec", ""))
    with sub3:
        st.markdown(current_pkg.get("exam_questions", ""))
    with sub4:
        st.markdown(current_pkg.get("exam_answers", ""))


# ==========================================
# FOOTER BẢN QUYỀN
# ==========================================
st.markdown("<br>", unsafe_allow_html=True)
st.divider()
st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 0.82rem; padding: 0.5rem 0; line-height: 1.5;">
    <b>EduMaster AI</b> • Giải pháp Chuyển đổi số Sư phạm & Nâng cao năng lực Khảo thí THCS/THPT<br>
    <i>Tuân thủ nghiêm ngặt Công văn số 5512/BGDĐT-GDTrH và Công văn số 7991/BGDĐT-GDTrH (17/12/2024) của Bộ GDĐT.</i>
</div>
""", unsafe_allow_html=True)
