# -*- coding: utf-8 -*-
"""
EduMaster AI - Hệ thống Soạn giảng & Khảo thí chuẩn Công văn 7991 & 5512
Ứng dụng Web dành cho Giáo viên THCS và THPT (tỉnh Vĩnh Long và toàn quốc).
"""

import os
import streamlit as st
import io

from sample_data import (
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
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS PHONG CÁCH SƯ PHẠM CAO CẤP
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Hero Header */
    .hero-container {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 55%, #0284C7 100%);
        padding: 2.2rem 2.4rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 1.8rem;
        box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.25);
    }
    .hero-title {
        font-size: 2.1rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #E0E7FF;
        line-height: 1.5;
        max-width: 950px;
    }
    .hero-badges {
        display: flex;
        gap: 10px;
        margin-top: 1rem;
        flex-wrap: wrap;
    }
    .badge-pill {
        background: rgba(255, 255, 255, 0.18);
        backdrop-filter: blur(8px);
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: #FFFFFF;
    }
    
    /* Quick Action / Metric Card */
    .metric-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.06);
    }
    .metric-label {
        font-size: 0.8rem;
        color: #64748B;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .metric-value {
        font-size: 1.15rem;
        font-weight: 700;
        color: #1E293B;
        margin-top: 4px;
    }
    
    /* Slide Preview Card */
    .slide-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-top: 4px solid #2563EB;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    }
    .slide-num {
        display: inline-block;
        background: #EFF6FF;
        color: #1D4ED8;
        font-weight: 700;
        font-size: 0.8rem;
        padding: 3px 10px;
        border-radius: 6px;
        margin-bottom: 0.6rem;
    }
    .slide-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 0.8rem;
    }
    .visual-box {
        background: #F8FAFC;
        border-left: 3px solid #6366F1;
        padding: 0.75rem 1rem;
        border-radius: 0 8px 8px 0;
        font-size: 0.88rem;
        color: #334155;
        margin-top: 0.8rem;
    }
    .notes-box {
        background: #FEF3C7;
        border-left: 3px solid #D97706;
        padding: 0.75rem 1rem;
        border-radius: 0 8px 8px 0;
        font-size: 0.88rem;
        color: #78350F;
        margin-top: 0.6rem;
    }
    
    /* Buttons */
    .stButton>button {
        border-radius: 10px;
        font-weight: 600;
        padding: 0.55rem 1.2rem;
        transition: all 0.2s ease;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# KHỞI TẠO STATE
# ==========================================
if "current_package" not in st.session_state:
    # Mặc định nạp dữ liệu mẫu chất lượng cao để giáo viên trải nghiệm ngay
    st.session_state["current_package"] = {
        "metadata": SAMPLE_METADATA,
        "lesson_plan": SAMPLE_LESSON_PLAN,
        "slides": SAMPLE_SLIDES,
        "exam_matrix": SAMPLE_EXAM_MATRIX,
        "exam_spec": SAMPLE_EXAM_SPEC,
        "exam_questions": SAMPLE_EXAM_QUESTIONS,
        "exam_answers": SAMPLE_EXAM_ANSWERS,
        "pedagogical_summary": "Bài dạy được thiết kế bám sát định hướng phát triển năng lực môn Vật lí theo CT GDPT 2018, hoàn chỉnh 4 hoạt động CV 5512 và hệ thống đề khảo thí 4 phần chuẩn xác tỉ lệ điểm CV 7991."
    }

# ==========================================
# SIDEBAR - CẤU HÌNH ĐẦU VÀO SƯ PHẠM
# ==========================================
with st.sidebar:
    st.markdown("### 🎓 Cấu hình Hệ thống")
    
    # 1. API Key
    default_api_key = os.environ.get("GEMINI_API_KEY", "")
    if not default_api_key:
        try:
            default_api_key = st.secrets.get("GEMINI_API_KEY", "")
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
        st.caption("🟢 **Đã phát hiện API Key** - Sẵn sàng khởi tạo.")
    else:
        st.caption("🟡 Chưa có API Key: Bạn vẫn có thể **trải nghiệm dữ liệu mẫu** và xuất file trực tiếp bên dưới.")

    model_choice = st.selectbox(
        "Mô hình AI (Gemini Model):",
        options=["gemini-2.5-flash", "gemini-1.5-flash", "gemini-1.5-pro"],
        index=0,
        help="gemini-2.5-flash: Tốc độ siêu tốc, tư duy sư phạm chuẩn xác và cấu trúc chặt chẽ."
    )
    
    st.divider()
    st.markdown("### 📚 Thông tin Hồ sơ Dạy học")
    
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
            "Ngữ văn", "Toán", "Tiếng Anh", "Khoa học tự nhiên (KHTN)",
            "Lịch sử & Địa lí", "Tin học", "Giáo dục công dân (GDCD)",
            "Công nghệ", "Âm nhạc", "Mĩ thuật", "Hoạt động trải nghiệm hướng nghiệp"
        ]
    else:
        subject_list = [
            "Vật lí", "Toán", "Ngữ văn", "Tiếng Anh", "Hóa học", "Sinh học",
            "Lịch sử", "Địa lí", "Tin học", "Giáo dục kinh tế & Pháp luật (GDKT&PL)",
            "Công nghệ", "Hoạt động trải nghiệm hướng nghiệp"
        ]
        
    subject = st.selectbox("Môn học:", subject_list, index=0)

    # 4. Bộ sách giáo khoa
    book_series = st.selectbox(
        "Bộ sách giáo khoa:",
        ["Kết nối tri thức với cuộc sống", "Cánh diều", "Chân trời sáng tạo"],
        index=0
    )

    # 5. Tên bài học / Chủ đề
    lesson_name = st.text_input(
        "Tên bài học / Chủ đề:",
        value="Bài 26: Cơ năng và định luật bảo toàn cơ năng",
        placeholder="Ví dụ: Đoạn trích Trong lòng mẹ, Sóng ánh sáng,..."
    )

    # 6. Thời lượng
    duration = st.selectbox(
        "Thời lượng bài dạy:",
        ["1 tiết (45 phút)", "2 tiết (90 phút)", "3 tiết (135 phút)", "4 tiết (180 phút)", "Tùy chỉnh khác"],
        index=1
    )

    # 7. Ghi chú sư phạm bổ sung
    special_notes = st.text_area(
        "Mục tiêu đặc biệt / Ghi chú sư phạm (Tùy chọn):",
        placeholder="Ví dụ: Ứng dụng mô hình STEM, rèn luyện làm việc nhóm, học sinh khá giỏi, tích hợp công nghệ số...",
        value="Tích hợp mô phỏng thí nghiệm ảo PhET và liên hệ tình huống kỹ thuật thực tiễn (tàu lượn, đập thủy điện)."
    )

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 8. Nút tạo nội dung AI
    btn_generate = st.button("🚀 XUẤT BẢN TRỌN BỘ TÀI LIỆU SƯ PHẠM", type="primary", use_container_width=True)
    
    # Nút nạp lại bản mẫu
    btn_sample = st.button("🎯 Nạp dữ liệu chuẩn mẫu (Demo ngay)", use_container_width=True)
    if btn_sample:
        st.session_state["current_package"] = {
            "metadata": SAMPLE_METADATA,
            "lesson_plan": SAMPLE_LESSON_PLAN,
            "slides": SAMPLE_SLIDES,
            "exam_matrix": SAMPLE_EXAM_MATRIX,
            "exam_spec": SAMPLE_EXAM_SPEC,
            "exam_questions": SAMPLE_EXAM_QUESTIONS,
            "exam_answers": SAMPLE_EXAM_ANSWERS,
            "pedagogical_summary": "Dữ liệu mẫu chuẩn hóa 100% theo Công văn 5512 và Công văn 7991/BGDĐT-GDTrH."
        }
        st.success("✅ Đã nạp trọn bộ dữ liệu mẫu chuẩn thành công!")
        st.rerun()

    st.divider()
    st.markdown("""
    <div style="font-size: 0.75rem; color: #64748B; line-height: 1.4;">
        <b>Khung pháp lý tích hợp:</b><br>
        • <b>CV 5512/BGDĐT-GDTrH</b>: Khung kế hoạch bài dạy 4 hoạt động.<br>
        • <b>CV 7991/BGDĐT-GDTrH (17/12/2024)</b>: Định dạng đề kiểm tra 4 phần & tỉ lệ nhận thức Biết (40%) - Hiểu (30%) - Vận dụng (30%).
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# XỬ LÝ SỰ KIỆN TẠO MỚI NỘI DUNG VỚI AI
# ==========================================
if btn_generate:
    if not api_key_input:
        st.error("⚠️ Vui lòng nhập Google Gemini API Key trong thanh cấu hình bên trái để kích hoạt AI tạo mới nội dung.")
    elif not lesson_name.strip():
        st.warning("⚠️ Vui lòng nhập tên bài học hoặc chủ đề cần soạn.")
    else:
        with st.spinner("🤖 EduMaster AI đang phân tích dữ liệu sư phạm, thiết lập ma trận CV 7991 và tiến trình 4 hoạt động CV 5512..."):
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
                    "pedagogical_summary": new_data.get("pedagogical_summary", "Đã khởi tạo hoàn tất hồ sơ sư phạm chất lượng cao.")
                }
                st.toast("🎉 Đã xuất bản trọn bộ hồ sơ sư phạm thành công!", icon="✨")
                st.rerun()
            except Exception as e:
                st.error(f"❌ Có lỗi xảy ra trong quá trình khởi tạo: {str(e)}")


# ==========================================
# GIAO DIỆN CHÍNH (MAIN CONTENT)
# ==========================================
current_pkg = st.session_state["current_package"]
cur_meta = current_pkg.get("metadata", {})

# 1. Hero Header Banner
st.markdown(f"""
<div class="hero-container">
    <div class="hero-title">
        <span>🏛️ EduMaster AI</span>
        <span style="font-size: 1.1rem; font-weight: 500; opacity: 0.9; background: rgba(255,255,255,0.15); padding: 4px 12px; border-radius: 20px;">
            Phiên bản Sư phạm 2025
        </span>
    </div>
    <div class="hero-subtitle">
        Hệ thống Soạn Kế hoạch bài dạy chuẩn <b>Công văn 5512/BGDĐT-GDTrH</b> và Thiết kế Đề kiểm tra định kì chuẩn hóa 
        theo <b>Công văn 7991/BGDĐT-GDTrH</b> ngày 17/12/2024 của Bộ GDĐT dành cho Giáo viên THCS & THPT.
    </div>
    <div class="hero-badges">
        <span class="badge-pill">✅ Chuẩn CV 5512/BGDĐT-GDTrH</span>
        <span class="badge-pill">✅ Chuẩn CV 7991/BGDĐT-GDTrH (17/12/2024)</span>
        <span class="badge-pill">✅ CT GDPT 2018 (Phát triển Năng lực)</span>
        <span class="badge-pill">📍 Giáo dục Vĩnh Long & Toàn quốc</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 2. Thẻ tóm tắt thông tin hiện hành (Overview Metrics)
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Môn học & Lớp</div>
        <div class="metric-value">{cur_meta.get('subject', 'Vật lí')} - {cur_meta.get('grade', 'Lớp 10')}</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Bộ sách & Thời lượng</div>
        <div class="metric-value" style="font-size: 0.95rem;">{cur_meta.get('book_series', 'KNTT')} ({cur_meta.get('duration', '2 tiết')})</div>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Trình chiếu Slide</div>
        <div class="metric-value">{len(current_pkg.get('slides', []))} Slides + Lời giảng</div>
    </div>
    """, unsafe_allow_html=True)
with c4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Ma trận Đề kiểm tra</div>
        <div class="metric-value">4 Phần (Biết 4 - Hiểu 3 - VD 3)</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 3. TRUNG TÂM XUẤT BẢN & TẢI FILE (DOWNLOAD CENTER)
st.markdown("### 📥 Trung tâm Xuất bản Tài liệu Thực tế")

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
    st.warning(f"Lưu ý tạo file Word: {e_docx}")

try:
    pptx_bytes = export_to_pptx(
        metadata=cur_meta,
        slides_data=current_pkg.get("slides", [])
    )
except Exception as e_pptx:
    pptx_bytes = None
    st.warning(f"Lưu ý tạo file PowerPoint: {e_pptx}")

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
        clean_name = cur_meta.get('lesson_name', 'Ho_So_Su_Pham').replace(' ', '_').replace(':', '')
        st.download_button(
            label="📄 Tải Hồ sơ Giáo án & Đề thi (.docx)",
            data=docx_bytes.getvalue(),
            file_name=f"EduMaster_{clean_name}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            type="primary",
            use_container_width=True,
            help="File Word hoàn chỉnh với bảng biểu, căn lề chuẩn hành chính, viền kẻ và định dạng sẵn sàng in ấn."
        )

with col_d2:
    if pptx_bytes:
        clean_name = cur_meta.get('lesson_name', 'Bai_Giang_Slide').replace(' ', '_').replace(':', '')
        st.download_button(
            label="📊 Tải Bài giảng Trình chiếu (.pptx)",
            data=pptx_bytes.getvalue(),
            file_name=f"EduMaster_{clean_name}.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            type="secondary",
            use_container_width=True,
            help="File PowerPoint chuẩn tỉ lệ 16:9, có bố cục thẻ nội dung, ý tưởng trực quan và Speaker Notes tích hợp."
        )

with col_d3:
    st.download_button(
        label="📋 Tải toàn văn Markdown (.md)",
        data=full_markdown_text.encode('utf-8'),
        file_name=f"EduMaster_{cur_meta.get('lesson_name', 'tai_lieu')}.md",
        mime="text/markdown",
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# 4. KHU VỰC HIỂN THỊ KẾT QUẢ VỚI 3 TAB CHÍNH
tab1, tab2, tab3 = st.tabs([
    "📝 TAB 1: KẾ HOẠCH BÀI DẠY (CV 5512)",
    "🖥️ TAB 2: DÀN Ý & TRÌNH CHIẾU SLIDE",
    "📑 TAB 3: ĐỀ KIỂM TRA & MA TRẬN ĐẶC TẢ (CV 7991)"
])

# === TAB 1: KẾ HOẠCH BÀI DẠY (CV 5512) ===
with tab1:
    st.markdown("#### 📋 Kế hoạch bài dạy chuẩn khung Công văn 5512/BGDĐT-GDTrH")
    st.caption("Gồm 4 hoạt động bắt buộc: Khởi động, Hình thành kiến thức mới, Luyện tập, Vận dụng; Đầy đủ 4 bước chuyển giao - thực hiện - báo cáo - kết luận.")
    
    st.markdown("---")
    st.markdown(current_pkg.get("lesson_plan", "*Chưa có nội dung kế hoạch bài dạy.*"))


# === TAB 2: DÀN Ý & TRÌNH CHIẾU SLIDE ===
with tab2:
    slides = current_pkg.get("slides", [])
    st.markdown(f"#### 🖥️ Dàn ý Trình chiếu Điện tử ({len(slides)} Slide trực quan)")
    st.caption("Được cấu trúc tối ưu cho màn hình 16:9, mỗi slide có gạch đầu dòng cô đọng, gợi ý hình ảnh và Lời giảng của giáo viên.")
    
    st.markdown("---")
    
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
                <div class="slide-card">
                    <span class="slide-num">SLIDE #{slide_no:02d}</span>
                    <div class="slide-title">{title}</div>
                """, unsafe_allow_html=True)
                
                # Hiển thị gạch đầu dòng
                for b in bullets:
                    st.markdown(f"• **{b}**")
                    
                # Hộp Visual Hint
                if visual:
                    st.markdown(f"""
                    <div class="visual-box">
                        <b>🎨 Ý tưởng minh họa / Visual:</b> {visual}
                    </div>
                    """, unsafe_allow_html=True)
                    
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Expander Speaker Notes
                if notes:
                    with st.expander(f"🎙️ Xem Lời giảng của Giáo viên (Speaker Notes) - Slide {slide_no}"):
                        st.markdown(f"*{notes}*")
                
                st.write("")


# === TAB 3: ĐỀ KIỂM TRA ĐỊNH KÌ (CV 7991) ===
with tab3:
    st.markdown("#### 📑 Đề kiểm tra định kì & Ma trận đặc tả theo Công văn 7991/BGDĐT-GDTrH")
    st.caption("Văn bản mới nhất ngày 17/12/2024 của Bộ GDĐT quy định định dạng đề kiểm tra định kì: 4 phần (TNKQ Nhiều lựa chọn, Đúng - Sai, Trả lời ngắn, Tự luận) với tỉ lệ Biết 40% - Hiểu 30% - Vận dụng 30%.")
    st.markdown("---")

    sub_tab_a, sub_tab_b, sub_tab_c, sub_tab_d = st.tabs([
        "📊 3.1. Ma trận đề kiểm tra",
        "📋 3.2. Bản đặc tả đề kiểm tra",
        "✍️ 3.3. Đề kiểm tra chi tiết (4 Phần)",
        "🔑 3.4. Hướng dẫn chấm & Đáp án"
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
# FOOTER BẢN QUYỀN & HƯỚNG DẪN DỰ THI
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 0.85rem; padding: 1rem 0;">
    <b>EduMaster AI</b> • Giải pháp Chuyển đổi số Sư phạm & Nâng cao năng lực Khảo thí THCS/THPT<br>
    Ứng dụng Trí tuệ Nhân tạo thế hệ mới đồng hành cùng Thầy Cô tỉnh Vĩnh Long và toàn quốc.<br>
    <i>Tuân thủ nghiêm ngặt Công văn số 5512/BGDĐT-GDTrH và Công văn số 7991/BGDĐT-GDTrH (17/12/2024) của Bộ GDĐT.</i>
</div>
""", unsafe_allow_html=True)
