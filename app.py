# -*- coding: utf-8 -*-
"""
EduMaster AI - Hệ thống Soạn giảng & Khảo thí chuẩn Công văn 7991 & 5512
Ứng dụng Web dành cho Giáo viên THCS và THPT (tỉnh Vĩnh Long và toàn quốc).
Tối ưu hóa hiển thị Mobile-First, Tinh gọn cài đặt, Trực quan hóa kết quả và Slide kèm hình ảnh minh họa thực tế.
"""

import os
import streamlit as st
import io
import textwrap


def render_html(html_str: str):
    """Hiển thị HTML thuần túy, loại bỏ khoảng trắng đầu dòng để Markdown không bao giờ hiểu nhầm thành code block."""
    cleaned = "\n".join(line.strip() for line in html_str.split("\n") if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)

from sample_data import (
    SUBJECT_PRESETS,
    get_sample_package_for_subject,
    generate_tailored_package,
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
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        flex-shrink: 0;
    }
    .brand-text-box {
        display: flex;
        flex-direction: column;
    }
    .brand-title {
        font-weight: 800;
        font-size: 1.05rem;
        letter-spacing: -0.3px;
        line-height: 1.2;
    }
    .brand-sub {
        font-size: 0.72rem;
        color: #BFDBFE;
        font-weight: 500;
        margin-top: 2px;
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
    
    /* Onboarding Welcome Screen */
    .welcome-container {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 2rem 2.2rem;
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.05);
        margin-top: 0.8rem;
    }
    .welcome-header {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 1.5rem;
    }
    .welcome-icon {
        width: 56px;
        height: 56px;
        background: linear-gradient(135deg, #2563EB, #1D4ED8);
        color: white;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.6rem;
        flex-shrink: 0;
        box-shadow: 0 8px 16px rgba(37, 99, 235, 0.25);
    }
    .welcome-step-card {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 1.3rem;
        height: 100%;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .welcome-step-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.06);
    }
    .welcome-step-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 0.76rem;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 20px;
        background: #EFF6FF;
        color: #2563EB;
        margin-bottom: 0.8rem;
    }
    .welcome-feature-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-top: 0.8rem;
        display: flex;
        align-items: flex-start;
        gap: 14px;
    }
    .feature-icon-box {
        width: 40px;
        height: 40px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.15rem;
        flex-shrink: 0;
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
        gap: 16px;
        margin-bottom: 1.2rem;
    }
    .visual-summary-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 1.1rem 1.25rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02);
    }
    .visual-summary-head {
        font-size: 0.88rem;
        font-weight: 700;
        margin-bottom: 0.6rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .visual-summary-head.blue { color: #2563EB; }
    .visual-summary-head.purple { color: #7C3AED; }
    .visual-summary-head.amber { color: #D97706; }

    /* Activity Flow Timeline */
    .activity-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #2563EB;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .activity-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 0.5rem;
        flex-wrap: wrap;
        gap: 8px;
    }
    .activity-title {
        font-weight: 700;
        font-size: 1.02rem;
        color: #0F172A;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .activity-duration {
        font-size: 0.76rem;
        font-weight: 600;
        background: #EFF6FF;
        color: #1D4ED8;
        padding: 3px 9px;
        border-radius: 20px;
    }
    .activity-steps-flow {
        display: flex;
        gap: 8px;
        margin-top: 0.6rem;
        flex-wrap: wrap;
    }
    .step-pill {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 4px 10px;
        font-size: 0.78rem;
        color: #334155;
        font-weight: 500;
        display: inline-flex;
        align-items: center;
        gap: 5px;
    }

    /* Slide Card with Real Illustrations */
    .slide-card-container {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 1.2rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    }
    .slide-header-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 0.8rem;
        border-bottom: 1px solid #F1F5F9;
        padding-bottom: 0.6rem;
    }
    .slide-badge-num {
        background: #EFF6FF;
        color: #1D4ED8;
        font-weight: 700;
        font-size: 0.78rem;
        padding: 4px 10px;
        border-radius: 8px;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    .slide-grid-layout {
        display: grid;
        grid-template-columns: 320px 1fr;
        gap: 18px;
    }
    .slide-illustration-box {
        position: relative;
        border-radius: 10px;
        overflow: hidden;
        border: 1px solid #E2E8F0;
        background: #F8FAFC;
    }
    .slide-illustration-img {
        width: 100%;
        height: 190px;
        object-fit: cover;
        display: block;
        transition: transform 0.3s ease;
    }
    .slide-illustration-img:hover {
        transform: scale(1.03);
    }
    .slide-visual-hint {
        padding: 8px 10px;
        font-size: 0.75rem;
        color: #475569;
        background: #F8FAFC;
        border-top: 1px solid #E2E8F0;
        line-height: 1.4;
    }
    .slide-title-text {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 0.6rem;
    }
    .slide-bullet-item {
        font-size: 0.9rem;
        color: #334155;
        margin-bottom: 0.45rem;
        display: flex;
        align-items: flex-start;
        gap: 8px;
        line-height: 1.45;
    }
    .speaker-notes-box {
        margin-top: 0.8rem;
        background: #FFFBEB;
        border: 1px solid #FDE68A;
        border-radius: 10px;
        padding: 0.75rem 0.9rem;
        font-size: 0.83rem;
        color: #92400E;
        line-height: 1.45;
    }

    /* Exam CV 7991 KPI Grid */
    .exam-kpi-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
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
    st.session_state["active_subject"] = "Ngữ văn"

if "active_grade" not in st.session_state:
    st.session_state["active_grade"] = "Lớp 9"

if "lesson_input_value" not in st.session_state:
    st.session_state["lesson_input_value"] = ""

# Mặc định chưa chọn gì -> KHÔNG HIỂN THỊ HỒ SƠ CỐ ĐỊNH BAN ĐẦU
if "current_package" not in st.session_state:
    st.session_state["current_package"] = None


# ==========================================
# SIDEBAR - CẤU HÌNH ĐẦU VÀO TINH GỌN (SIMPLIFIED SETTINGS)
# ==========================================
with st.sidebar:
    render_html("""
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
        grade_level = st.radio("Cấp học:", options=["THCS", "THPT"], index=0)
        
    with col_grade:
        if grade_level == "THCS":
            grade = st.selectbox("Khối lớp:", ["Lớp 6", "Lớp 7", "Lớp 8", "Lớp 9"], index=3)
        else:
            grade = st.selectbox("Khối lớp:", ["Lớp 10", "Lớp 11", "Lớp 12"], index=0)

    # 2. Môn học
    if grade_level == "THCS":
        subject_list = [
            "Ngữ văn", "Toán", "Khoa học tự nhiên (KHTN)", "Tiếng Anh",
            "Lịch sử & Địa lí", "Tin học", "Giáo dục công dân (GDCD)",
            "Công nghệ", "Âm nhạc", "Mĩ thuật", "Hoạt động trải nghiệm hướng nghiệp"
        ]
    else:
        subject_list = [
            "Ngữ văn", "Toán", "Vật lí", "Hóa học", "Sinh học", "Tiếng Anh",
            "Lịch sử", "Địa lí", "Tin học", "Giáo dục kinh tế & Pháp luật (GDKT&PL)",
            "Công nghệ", "Hoạt động trải nghiệm hướng nghiệp"
        ]
        
    def_idx = 0
    if st.session_state["active_subject"] in subject_list:
        def_idx = subject_list.index(st.session_state["active_subject"])
        
    subject = st.selectbox("Môn học:", subject_list, index=def_idx)

    # Cập nhật state môn học và lớp mà KHÔNG tự ý ép mẫu
    if subject != st.session_state.get("active_subject") or grade != st.session_state.get("active_grade"):
        st.session_state["active_subject"] = subject
        st.session_state["active_grade"] = grade

    # 3. Bộ sách giáo khoa
    book_series = st.selectbox(
        "Bộ sách giáo khoa:",
        ["Kết nối tri thức với cuộc sống", "Cánh diều", "Chân trời sáng tạo"],
        index=0
    )

    # 4. Tên bài học / Chủ đề (Mặc định để trống, không bắt buộc bài mẫu)
    lesson_name = st.text_input(
        "Tên bài học / Chủ đề:",
        value=st.session_state.get("lesson_input_value", ""),
        placeholder="Ví dụ: Chuyện người con gái Nam Xương, Hàm số, Cơ năng..."
    )
    st.session_state["lesson_input_value"] = lesson_name

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
            value="",
            placeholder="Ví dụ: Dạy học tích hợp, phát triển năng lực đọc hiểu..."
        )

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 6. Nút kích hoạt chính
    btn_generate = st.button(f"🚀 XUẤT BẢN HỒ SƠ BÀI DẠY ({subject.upper()})", type="primary", use_container_width=True)
    btn_sample = st.button(f"💡 Nạp Gợi ý Mẫu ({subject} - {grade})", use_container_width=True)
    
    if btn_sample:
        preset = SUBJECT_PRESETS.get(subject, {})
        sample_topic = preset.get("lesson_name", f"Chủ đề trọng tâm môn {subject} - {grade}")
        st.session_state["lesson_input_value"] = sample_topic
        st.session_state["current_package"] = generate_tailored_package(
            subject=subject,
            grade=grade,
            grade_level=grade_level,
            book_series=book_series,
            lesson_name=sample_topic,
            special_notes=preset.get("special_notes", "")
        )
        st.toast(f"Đã nạp gợi ý bài học: '{sample_topic}'", icon="💡")
        st.rerun()

    st.caption("⚡ *Hồ sơ xuất bản sẽ khớp 100% với tên bài học và môn học Thầy/Cô đã chọn.*")


# ==========================================
# XỬ LÝ SỰ KIỆN TẠO MỚI NỘI DUNG VỚI AI HOẶC ENGINE THÔNG MINH
# ==========================================
if btn_generate:
    if not lesson_name.strip():
        st.warning("⚠️ Thầy/Cô vui lòng nhập **Tên bài học / Chủ đề** ở thanh bên trái trước khi xuất bản hồ sơ.")
    elif not api_key_input:
        with st.spinner(f"EduMaster AI đang chuẩn hóa hồ sơ bài dạy '{lesson_name}' môn {subject} ({grade})..."):
            st.session_state["current_package"] = generate_tailored_package(
                subject=subject,
                grade=grade,
                grade_level=grade_level,
                book_series=book_series,
                lesson_name=lesson_name,
                special_notes=special_notes if 'special_notes' in locals() else ""
            )
            st.toast(f"Đã xuất bản thành công hồ sơ bài học '{lesson_name}' ({subject} - {grade})!", icon="✅")
            st.rerun()
    else:
        with st.spinner(f"EduMaster AI (Gemini) đang biên soạn hồ sơ bài học '{lesson_name}' môn {subject} ({grade}) chuẩn CV 5512 & CV 7991..."):
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
                    "pedagogical_summary": new_data.get("pedagogical_summary", f"Đã khởi tạo hoàn tất hồ sơ sư phạm môn {subject} chất lượng cao."),
                    "summary_knowledge": [
                        f"Nắm vững các khái niệm, quy luật và nguyên lí trọng tâm của bài học: {lesson_name}.",
                        "Phân tích mối quan hệ logic giữa lí thuyết môn học và thực tiễn đời sống.",
                        "Vận dụng kiến thức bài học giải quyết các bài tập và nhiệm vụ tình huống."
                    ],
                    "summary_competencies": [
                        f"Năng lực chung: Tự chủ trong tự học SGK {book_series}; Hợp tác nhóm thảo luận hiệu quả.",
                        f"Năng lực đặc thù môn {subject}: Nhận thức bản chất khoa học và mô hình hóa giải quyết vấn đề."
                    ],
                    "summary_qualities": [
                        "Chăm chỉ: Tích cực tìm tòi, ghi chép và rèn luyện kĩ năng.",
                        "Trách nhiệm: Hoàn thành đúng tiến độ nhiệm vụ được phân công."
                    ],
                    "activities": [
                        {
                            "name": "Hoạt động 1: Mở đầu / Khởi động",
                            "duration": "10 phút",
                            "objective": f"Tạo mâu thuẫn nhận thức và kích thích tư duy tìm hiểu {lesson_name}.",
                            "content": "Quan sát hình ảnh/video thực tế và trả lời câu hỏi gợi mở của giáo viên.",
                            "steps": ["GV chiếu tình huống", "HS thảo luận cặp đôi", "Đại diện phát biểu ý kiến", "GV nhận xét và vào bài"]
                        },
                        {
                            "name": "Hoạt động 2: Hình thành kiến thức mới",
                            "duration": "50 phút",
                            "objective": "Nghiên cứu tài liệu SGK, khám phá quy luật và chuẩn hóa kiến thức cốt lõi.",
                            "content": "Phân chia các mạch kiến thức trọng tâm giải quyết theo phiếu học tập nhóm.",
                            "steps": ["Giao phiếu học tập", "HS thảo luận xử lí dữ liệu", "Đại diện thuyết trình", "GV chuẩn hóa kiến thức"]
                        },
                        {
                            "name": "Hoạt động 3: Luyện tập củng cố",
                            "duration": "18 phút",
                            "objective": "Khắc sâu kiến thức qua hệ thống bài tập trắc nghiệm và câu hỏi rèn luyện.",
                            "content": "Giải quyết các câu trắc nghiệm tương tác và bài tập tình huống thực tế.",
                            "steps": ["Giao bài tập độc lập", "HS làm bài vào vở", "Lên bảng chữa bài", "GV nhận xét, sửa lỗi"]
                        },
                        {
                            "name": "Hoạt động 4: Vận dụng thực tiễn",
                            "duration": "12 phút",
                            "objective": "Vận dụng kiến thức bài học vào giải quyết vấn đề thực tế đời sống.",
                            "content": "Nhiệm vụ dự án nhỏ tìm hiểu ứng dụng thực tiễn tại quê hương hoặc trong đời sống.",
                            "steps": ["Giao nhiệm vụ dự án", "HS lập kế hoạch", "Thực hiện tại nhà", "Nộp trên LMS buổi sau"]
                        }
                    ]
                }
                st.toast(f"Đã xuất bản trọn bộ tài liệu môn {subject} thành công!", icon="✅")
                st.rerun()
            except Exception as e:
                st.error(f"Có lỗi xảy ra: {str(e)}")


# ==========================================
# GIAO DIỆN CHÍNH (MAIN CONTENT)
# ==========================================
current_pkg = st.session_state.get("current_package")

# TRƯỜNG HỢP 1: KHI CHƯA CHỌN HOẶC CHƯA BẤM XUẤT BẢN -> MÀN HÌNH CHÀO MỪNG & HƯỚNG DẪN
if current_pkg is None:
    # 1. Hero Header Banner
    render_html("""
    <div class="hero-container">
        <div class="hero-title">
            <span>EduMaster AI</span>
            <span class="hero-version-pill">
                <i class="fa-solid fa-sparkles"></i> Sư phạm 2025
            </span>
        </div>
        <div class="hero-subtitle">
            Hệ thống Trợ lý Soạn Kế hoạch bài dạy chuẩn <b>Công văn 5512</b> và Thiết kế Đề kiểm tra định kì chuẩn hóa 
            theo <b>Công văn 7991</b> (ngày 17/12/2024) của Bộ GDĐT dành cho Giáo viên THCS & THPT.
        </div>
        <div class="hero-badges">
            <span class="badge-pill"><i class="fa-solid fa-file-shield" style="color: #38BDF8;"></i> CV 5512/BGDĐT</span>
            <span class="badge-pill"><i class="fa-solid fa-scale-balanced" style="color: #4ADE80;"></i> CV 7991/BGDĐT</span>
            <span class="badge-pill"><i class="fa-solid fa-layer-group" style="color: #A78BFA;"></i> CT GDPT 2018</span>
            <span class="badge-pill"><i class="fa-solid fa-location-dot" style="color: #FBBF24;"></i> Vĩnh Long & Toàn quốc</span>
        </div>
    </div>
    """)

    # 2. Onboarding Quick Guide
    render_html("""
    <div class="welcome-container">
        <div class="welcome-header">
            <div class="welcome-icon">
                <i class="fa-solid fa-compass-drafting"></i>
            </div>
            <div>
                <div style="font-size: 1.35rem; font-weight: 800; color: #0F172A; letter-spacing: -0.3px;">
                    Chào mừng Thầy/Cô đến với EduMaster AI
                </div>
                <div style="font-size: 0.92rem; color: #64748B; margin-top: 4px;">
                    Hệ thống sẽ biên soạn hồ sơ sư phạm hoàn chỉnh bám sát đúng lựa chọn và bài dạy của Thầy/Cô.
                </div>
            </div>
        </div>
        <div style="font-size: 1.05rem; font-weight: 700; color: #1E293B; margin-bottom: 0.8rem;">
            <i class="fa-solid fa-list-check" style="color: #2563EB;"></i> 3 Bước Khởi tạo Hồ sơ Bài dạy Nhanh chóng:
        </div>
    </div>
    """)

    col_w1, col_w2, col_w3 = st.columns(3)
    with col_w1:
        render_html("""
        <div class="welcome-step-card">
            <span class="welcome-step-badge"><i class="fa-solid fa-1"></i> BƯỚC 1</span>
            <div style="font-weight: 700; font-size: 1rem; color: #0F172A; margin-bottom: 0.4rem;">
                Chọn Thông tin Đầu vào
            </div>
            <div style="font-size: 0.88rem; color: #475569; line-height: 1.45;">
                Tại thanh bên trái, chọn Cấp học (THCS/THPT), Khối lớp, Môn học và Bộ SGK tương ứng của Thầy/Cô.
            </div>
        </div>
        """)

    with col_w2:
        render_html("""
        <div class="welcome-step-card">
            <span class="welcome-step-badge"><i class="fa-solid fa-2"></i> BƯỚC 2</span>
            <div style="font-weight: 700; font-size: 1rem; color: #0F172A; margin-bottom: 0.4rem;">
                Nhập Tên Bài học / Chủ đề
            </div>
            <div style="font-size: 0.88rem; color: #475569; line-height: 1.45;">
                Nhập tên bài dạy Thầy/Cô chuẩn bị lên lớp (Ví dụ: <i>Chuyện người con gái Nam Xương, Hàm số bậc hai, Quang hợp...</i>).
            </div>
        </div>
        """)

    with col_w3:
        render_html("""
        <div class="welcome-step-card">
            <span class="welcome-step-badge"><i class="fa-solid fa-3"></i> BƯỚC 3</span>
            <div style="font-weight: 700; font-size: 1rem; color: #0F172A; margin-bottom: 0.4rem;">
                Bấm Xuất bản Hồ sơ
            </div>
            <div style="font-size: 0.88rem; color: #475569; line-height: 1.45;">
                Nhấn nút màu xanh <b>[🚀 XUẤT BẢN HỒ SƠ BÀI DẠY]</b> để xem ngay Giáo án 5512, Slide trình chiếu và Đề thi 7991.
            </div>
        </div>
        """)

    render_html("""
    <div style="margin-top: 1.8rem; font-size: 1.05rem; font-weight: 700; color: #1E293B;">
        <i class="fa-solid fa-certificate" style="color: #0D9488;"></i> Quy chuẩn Sư phạm & Khảo thí Tích hợp Sẵn:
    </div>
    
    <div class="welcome-feature-box">
        <div class="feature-icon-box" style="background: #EFF6FF; color: #2563EB;">
            <i class="fa-solid fa-file-contract"></i>
        </div>
        <div>
            <div style="font-weight: 700; font-size: 0.95rem; color: #0F172A;">
                Kế hoạch bài dạy chuẩn Công văn 5512/BGDĐT-GDTrH
            </div>
            <div style="font-size: 0.86rem; color: #475569; line-height: 1.45; margin-top: 2px;">
                Thiết kế trọn vẹn tiến trình 4 hoạt động: Khởi động ➔ Hình thành kiến thức ➔ Luyện tập ➔ Vận dụng. Mỗi hoạt động đều có cấu trúc 4 bước rõ ràng: Chuyển giao, Thực hiện, Báo cáo và Kết luận.
            </div>
        </div>
    </div>

    <div class="welcome-feature-box">
        <div class="feature-icon-box" style="background: #F0FDF4; color: #16A34A;">
            <i class="fa-solid fa-clipboard-check"></i>
        </div>
        <div>
            <div style="font-weight: 700; font-size: 0.95rem; color: #0F172A;">
                Đề kiểm tra định kì chuẩn hóa theo Công văn 7991/BGDĐT-GDTrH (17/12/2024)
            </div>
            <div style="font-size: 0.86rem; color: #475569; line-height: 1.45; margin-top: 2px;">
                Tích hợp Ma trận tỉ lệ 40% Biết - 30% Hiểu - 30% Vận dụng; Bản đặc tả mã hóa năng lực (NL_...); Đề thi 4 phần phân hóa (TN 4 lựa chọn, TN Đúng-Sai quy tắc điểm 0.1-1.0đ, TN Trả lời ngắn, Tự luận) và Hướng dẫn chấm chi tiết.
            </div>
        </div>
    </div>

    <div class="welcome-feature-box">
        <div class="feature-icon-box" style="background: #FAF5FF; color: #9333EA;">
            <i class="fa-solid fa-images"></i>
        </div>
        <div>
            <div style="font-weight: 700; font-size: 0.95rem; color: #0F172A;">
                Dàn ý Slide Trình chiếu 16:9 kèm Hình ảnh minh họa & Xuất bản Office
            </div>
            <div style="font-size: 0.86rem; color: #475569; line-height: 1.45; margin-top: 2px;">
                Mỗi slide có hình ảnh minh họa chân thực, nội dung cô đọng và Lời giảng giáo viên (Speaker Notes). Hỗ trợ tải trực tiếp file Word (.docx) và bài giảng PowerPoint (.pptx).
            </div>
        </div>
    </div>
    """)


# TRƯỜNG HỢP 2: KHI ĐÃ CÓ HỒ SƠ BÀI DẠY THEO LỰA CHỌN NGƯỜI DÙNG
else:
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
            Hồ sơ Sư phạm Bài dạy: <b>{cur_meta.get('lesson_name')}</b> • Môn <b>{cur_meta.get('subject')} ({cur_meta.get('grade')})</b> • Bộ sách <b>{cur_meta.get('book_series')}</b>.
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
        render_html(f"""
        <div class="metric-card-box">
            <div>
                <div class="metric-info-label">Môn học & Lớp</div>
                <div class="metric-info-val">{cur_meta.get('subject', subject)} - {cur_meta.get('grade', grade)}</div>
            </div>
            <div class="metric-icon-circle icon-blue"><i class="fa-solid fa-book-open"></i></div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        render_html(f"""
        <div class="metric-card-box">
            <div>
                <div class="metric-info-label">Bộ sách & Thời lượng</div>
                <div class="metric-info-val" style="font-size: 0.92rem;">{cur_meta.get('book_series', 'KNTT')} (2 tiết)</div>
            </div>
            <div class="metric-icon-circle icon-teal"><i class="fa-solid fa-clock"></i></div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        render_html(f"""
        <div class="metric-card-box">
            <div>
                <div class="metric-info-label">Slide có hình ảnh</div>
                <div class="metric-info-val">{len(current_pkg.get('slides', []))} Trang Slide</div>
            </div>
            <div class="metric-icon-circle icon-indigo"><i class="fa-solid fa-images"></i></div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        render_html(f"""
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

    # === TAB 1: KẾ HOẠCH BÀI DẠY (TRỰC QUAN HÓA, KHỚP 100% VỚI BÀI HỌC ĐÃ CHỌN) ===
    with tab1:
        render_html(f"""
        <div style="font-size: 1.2rem; font-weight: 700; color: #0F172A; margin-bottom: 0.8rem;">
            <i class="fa-solid fa-file-lines" style="color: #2563EB;"></i> Kế hoạch bài dạy: {cur_meta.get('lesson_name')}
        </div>
        """, unsafe_allow_html=True)
        
        # Thẻ tóm tắt 3 Trụ cột Mục tiêu lấy ĐỘNG từ chính bài học
        knowledge_list = current_pkg.get("summary_knowledge", [
            "Nắm vững các định nghĩa, công thức và nguyên lí nền tảng của bài học.",
            "Phân tích mối liên hệ logic giữa lí thuyết khoa học và hiện tượng thực tiễn.",
            "Biết cách vận dụng kiến thức giải quyết bài toán và nhiệm vụ học tập."
        ])
        competency_list = current_pkg.get("summary_competencies", [
            "Năng lực chung: Tự chủ, tự học và hợp tác nhóm hiệu quả.",
            "Năng lực đặc thù: Nhận thức môn học và mô hình hóa giải quyết vấn đề đời sống."
        ])
        quality_list = current_pkg.get("summary_qualities", [
            "Chăm chỉ: Chủ động tìm tòi, ghi chép số liệu trung thực.",
            "Trách nhiệm: Hoàn thành đúng tiến độ nhiệm vụ chung.",
            "Bồi dưỡng tình yêu khoa học và ý thức cộng đồng."
        ])
        
        knowledge_html = "<br>".join([f"• {item}" for item in knowledge_list])
        competency_html = "<br>".join([f"• {item}" for item in competency_list])
        quality_html = "<br>".join([f"• {item}" for item in quality_list])
        
        render_html(f"""
        <div class="visual-summary-container">
            <div class="visual-summary-card">
                <div class="visual-summary-head blue">
                    <i class="fa-solid fa-brain"></i> 1. Kiến thức trọng tâm
                </div>
                <div style="font-size: 0.88rem; color: #334155; line-height: 1.45;">
                    {knowledge_html}
                </div>
            </div>
            <div class="visual-summary-card">
                <div class="visual-summary-head purple">
                    <i class="fa-solid fa-gears"></i> 2. Năng lực cốt lõi
                </div>
                <div style="font-size: 0.88rem; color: #334155; line-height: 1.45;">
                    {competency_html}
                </div>
            </div>
            <div class="visual-summary-card">
                <div class="visual-summary-head amber">
                    <i class="fa-solid fa-heart"></i> 3. Phẩm chất rèn luyện
                </div>
                <div style="font-size: 0.88rem; color: #334155; line-height: 1.45;">
                    {quality_html}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Tiến trình 4 Hoạt động Dạy học (Chuẩn CV 5512/BGDĐT-GDTrH)")

        activities = current_pkg.get("activities", [])
        if activities:
            colors = ["#2563EB", "#0D9488", "#6366F1", "#D97706"]
            bg_colors = ["#EFF6FF", "#F0FDFA", "#EEF2FF", "#FFFBEB"]
            text_colors = ["#1D4ED8", "#0F766E", "#4338CA", "#B45309"]
            icons = ["fa-bolt", "fa-lightbulb", "fa-pen-ruler", "fa-earth-americas"]
            
            for idx, act in enumerate(activities):
                color = colors[idx % len(colors)]
                bg_color = bg_colors[idx % len(bg_colors)]
                text_color = text_colors[idx % len(text_colors)]
                icon = icons[idx % len(icons)]
                
                steps_html = "".join([
                    f'<span class="step-pill"><i class="fa-solid fa-{i+1}"></i> {step}</span>'
                    for i, step in enumerate(act.get("steps", []))
                ])
                
                render_html(f"""
                <div class="activity-card" style="border-left-color: {color};">
                    <div class="activity-header">
                        <span class="activity-title"><i class="fa-solid {icon}" style="color: {color};"></i> {act.get('name')}</span>
                        <span class="activity-duration" style="background: {bg_color}; color: {text_color};">{act.get('duration', '15 phút')}</span>
                    </div>
                    <div style="font-size: 0.88rem; color: #334155; margin-bottom: 0.4rem;">
                        <b>Mục tiêu & Nhiệm vụ:</b> {act.get('objective', '')}
                    </div>
                    <div style="font-size: 0.88rem; color: #334155; margin-bottom: 0.4rem;">
                        <b>Nội dung trọng tâm:</b> {act.get('content', '')}
                    </div>
                    <div class="activity-steps-flow">
                        {steps_html}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            # Fallback nếu dùng văn bản markdown trực tiếp
            st.markdown(current_pkg.get("lesson_plan", ""))

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
                render_html(f"""
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
                    render_html(f"""
                    <div class="slide-bullet-item">
                        <i class="fa-solid fa-circle-check" style="color: #2563EB; font-size: 0.85rem; margin-top: 3px; flex-shrink: 0;"></i>
                        <span><b>{b}</b></span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                if notes:
                    render_html(f"""
                    <div class="speaker-notes-box">
                        <i class="fa-solid fa-microphone-lines" style="color: #D97706;"></i> <b>Lời giảng của Giáo viên (Speaker Notes):</b><br>
                        <i>"{notes}"</i>
                    </div>
                    """, unsafe_allow_html=True)
                    
                render_html("""
                        </div>
                    </div>
                </div>
                """)
                st.write("")


    # === TAB 3: ĐỀ KIỂM TRA ĐỊNH KÌ (CV 7991 - TRỰC QUAN HÓA THANG ĐIỂM) ===
    with tab3:
        st.markdown(f"""
        <div style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin-bottom: 0.6rem;">
            <i class="fa-solid fa-clipboard-check" style="color: #2563EB;"></i> Đề kiểm tra định kì chuẩn hóa theo Công văn 7991/BGDĐT-GDTrH
        </div>
        """, unsafe_allow_html=True)
        
        # 4 Thẻ KPI Phân bổ điểm 7991
        render_html("""
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
render_html("""
<div style="text-align: center; color: #64748B; font-size: 0.82rem; padding: 0.5rem 0; line-height: 1.5;">
    <b>EduMaster AI</b> • Giải pháp Chuyển đổi số Sư phạm & Nâng cao năng lực Khảo thí THCS/THPT<br>
    <i>Tuân thủ nghiêm ngặt Công văn số 5512/BGDĐT-GDTrH và Công văn số 7991/BGDĐT-GDTrH (17/12/2024) của Bộ GDĐT.</i>
</div>
""", unsafe_allow_html=True)
