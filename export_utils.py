# -*- coding: utf-8 -*-
"""
EduMaster AI - Module Xuất bản Tài liệu Sư phạm
Hỗ trợ xuất file Word (.docx) và PowerPoint (.pptx) chuẩn hóa định dạng.
"""

import io
import re
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

import pptx
from pptx.util import Inches as PptxInches, Pt as PptxPt
from pptx.dml.color import RGBColor as PptxRGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE


# ==========================================
# CẤU HÌNH MÀU SẮC & STYLES WORD
# ==========================================
COLOR_PRIMARY_HEX = "1E3A8A"      # Deep Navy
COLOR_SECONDARY_HEX = "0284C7"    # Sky Blue
COLOR_BG_HEADER_HEX = "E0F2FE"    # Light Sky Blue
COLOR_BORDER_HEX = "CBD5E1"       # Slate 300

COLOR_PRIMARY_RGB = RGBColor(30, 58, 138)
COLOR_SECONDARY_RGB = RGBColor(2, 132, 199)
COLOR_TEXT_MAIN_RGB = RGBColor(15, 23, 42)
COLOR_MUTED_RGB = RGBColor(71, 85, 105)


def set_cell_background(cell, hex_color: str):
    """Đặt màu nền cho cell trong table Word."""
    shading_xml = f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Thiết lập padding cho cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def set_table_borders(table, color="B0C4DE", sz="4", val="single"):
    """Đặt viền thanh lịch cho bảng Word."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:left w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)


def clean_markdown_inline(text: str) -> list[tuple[str, bool, bool]]:
    """
    Phân tích chuỗi markdown đơn giản thành các đoạn (text, is_bold, is_italic).
    """
    # Xóa các kí tự công thức LaTeX đơn giản cho đẹp trong Word
    text = text.replace("$", "").replace("\\frac", "").replace("\\times", "×")
    text = text.replace("\\Leftrightarrow", "⇔").replace("\\Rightarrow", "⇒")
    text = text.replace("\\alpha", "α").replace("\\mu", "μ")
    
    # Tokenize bold và italic
    tokens = []
    # Pattern tìm **bold** hoặc *italic*
    pattern = re.compile(r'(\*\*[^*]+\*\*|\*[^*]+\*)')
    parts = pattern.split(text)
    for part in parts:
        if not part:
            continue
        if part.startswith('**') and part.endswith('**'):
            tokens.append((part[2:-2], True, False))
        elif part.startswith('*') and part.endswith('*'):
            tokens.append((part[1:-1], False, True))
        else:
            tokens.append((part, False, False))
    return tokens


def add_markdown_paragraph(doc, text: str, style='Normal', space_after=Pt(4), align=WD_ALIGN_PARAGRAPH.LEFT):
    """Thêm một đoạn văn bản có xử lý inline markdown (in đậm, in nghiêng)."""
    p = doc.add_paragraph(style=style)
    p.alignment = align
    p.paragraph_format.space_after = space_after
    p.paragraph_format.line_spacing = 1.15
    
    tokens = clean_markdown_inline(text)
    if not tokens:
        p.add_run("")
        return p
        
    for chunk, is_bold, is_italic in tokens:
        run = p.add_run(chunk)
        run.bold = is_bold
        run.italic = is_italic
        run.font.name = 'Times New Roman'
        run.font.size = Pt(11)
        run.font.color.rgb = COLOR_TEXT_MAIN_RGB
    return p


def render_markdown_section_to_docx(doc, markdown_content: str):
    """
    Chuyển đổi văn bản Markdown đầy đủ (kèm bảng | ... |) thành các thành phần Word tương ứng.
    """
    lines = markdown_content.splitlines()
    in_table = False
    table_rows = []
    
    for line in lines:
        stripped = line.strip()
        
        # Kiểm tra dòng bảng
        if stripped.startswith("|") and stripped.endswith("|"):
            in_table = True
            # Kiểm tra dòng phân cách |:---|:---:|
            if re.match(r'^\|[\s\-:|]+\|$', stripped):
                continue
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            table_rows.append(cells)
            continue
        else:
            # Nếu vừa kết thúc 1 bảng, render bảng đó ra Word
            if in_table and table_rows:
                create_word_table(doc, table_rows)
                table_rows = []
                in_table = False
                
        if not stripped:
            continue
            
        # Tiêu đề cấp 1
        if stripped.startswith("# "):
            h1 = doc.add_paragraph()
            h1.paragraph_format.space_before = Pt(14)
            h1.paragraph_format.space_after = Pt(6)
            run = h1.add_run(stripped[2:].strip())
            run.bold = True
            run.font.name = 'Times New Roman'
            run.font.size = Pt(15)
            run.font.color.rgb = COLOR_PRIMARY_RGB
            continue

        # Tiêu đề cấp 2
        if stripped.startswith("## "):
            h2 = doc.add_paragraph()
            h2.paragraph_format.space_before = Pt(10)
            h2.paragraph_format.space_after = Pt(4)
            run = h2.add_run(stripped[3:].strip())
            run.bold = True
            run.font.name = 'Times New Roman'
            run.font.size = Pt(13)
            run.font.color.rgb = COLOR_PRIMARY_RGB
            continue

        # Tiêu đề cấp 3
        if stripped.startswith("### "):
            h3 = doc.add_paragraph()
            h3.paragraph_format.space_before = Pt(8)
            h3.paragraph_format.space_after = Pt(3)
            run = h3.add_run(stripped[4:].strip())
            run.bold = True
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            run.font.color.rgb = COLOR_SECONDARY_RGB
            continue

        # Tiêu đề cấp 4
        if stripped.startswith("#### "):
            h4 = doc.add_paragraph()
            h4.paragraph_format.space_before = Pt(6)
            h4.paragraph_format.space_after = Pt(2)
            run = h4.add_run(stripped[5:].strip())
            run.bold = True
            run.italic = True
            run.font.name = 'Times New Roman'
            run.font.size = Pt(11.5)
            run.font.color.rgb = COLOR_PRIMARY_RGB
            continue

        # Đường kẻ ngang
        if stripped in ["---", "***", "___"]:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            run = p.add_run("―" * 50)
            run.font.color.rgb = COLOR_MUTED_RGB
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            continue

        # Danh sách dấu chấm (bullets)
        if stripped.startswith("- ") or stripped.startswith("* "):
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            tokens = clean_markdown_inline(stripped[2:].strip())
            for chunk, is_bold, is_italic in tokens:
                run = p.add_run(chunk)
                run.bold = is_bold
                run.italic = is_italic
                run.font.name = 'Times New Roman'
                run.font.size = Pt(11)
            continue

        # Đoạn văn bản thông thường
        add_markdown_paragraph(doc, stripped)
        
    # Trường hợp file kết thúc bằng một bảng
    if in_table and table_rows:
        create_word_table(doc, table_rows)


def create_word_table(doc, rows: list[list[str]]):
    """Tạo bảng Word chuẩn từ danh sách các hàng tế nhị và thanh lịch."""
    if not rows:
        return
        
    num_cols = max(len(r) for r in rows)
    num_rows = len(rows)
    
    table = doc.add_table(rows=num_rows, cols=num_cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    set_table_borders(table, color="94A3B8", sz="4")
    
    for row_idx, row_data in enumerate(rows):
        is_header = (row_idx == 0)
        table_row = table.rows[row_idx]
        
        # Đảm bảo header lặp lại ở đầu mỗi trang
        if is_header:
            trPr = table_row._tr.get_or_add_trPr()
            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
            
        for col_idx in range(num_cols):
            cell = table_row.cells[col_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=120, bottom=120, left=150, right=150)
            
            cell_text = row_data[col_idx] if col_idx < len(row_data) else ""
            cell.text = ""  # Xóa default paragraph rỗng
            
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.line_spacing = 1.1
            
            if is_header:
                set_cell_background(cell, COLOR_BG_HEADER_HEX)
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                tokens = clean_markdown_inline(cell_text)
                for chunk, _, _ in tokens:
                    run = p.add_run(chunk)
                    run.bold = True
                    run.font.name = 'Times New Roman'
                    run.font.size = Pt(10.5)
                    run.font.color.rgb = COLOR_PRIMARY_RGB
            else:
                if row_idx % 2 == 1:
                    set_cell_background(cell, "F8FAFC")
                tokens = clean_markdown_inline(cell_text)
                for chunk, is_bold, is_italic in tokens:
                    run = p.add_run(chunk)
                    run.bold = is_bold
                    run.italic = is_italic
                    run.font.name = 'Times New Roman'
                    run.font.size = Pt(10)
                    run.font.color.rgb = COLOR_TEXT_MAIN_RGB
                    
    doc.add_paragraph().paragraph_format.space_after = Pt(6)


def export_to_docx(metadata: dict, lesson_plan_md: str, exam_matrix_md: str, exam_spec_md: str, exam_questions_md: str, exam_answers_md: str) -> io.BytesIO:
    """
    Xuất trọn bộ hồ sơ sư phạm ra file .docx gồm:
    1. Trang bìa & Thông tin quản lý
    2. Kế hoạch bài dạy chuẩn CV 5512
    3. Ma trận & Bản đặc tả đề kiểm tra chuẩn CV 7991
    4. Đề kiểm tra chi tiết
    5. Hướng dẫn chấm & Thang điểm
    """
    doc = docx.Document()
    
    # Thiết lập lề trang chuẩn hành chính (Top: 2cm, Bottom: 2cm, Left: 2.5cm, Right: 2cm)
    for section in doc.sections:
        section.top_margin = Inches(0.79)     # ~2.0 cm
        section.bottom_margin = Inches(0.79)  # ~2.0 cm
        section.left_margin = Inches(0.98)    # ~2.5 cm
        section.right_margin = Inches(0.79)   # ~2.0 cm
        
        # Header / Footer
        header = section.header
        p_hdr = header.paragraphs[0]
        p_hdr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r_hdr = p_hdr.add_run("EduMaster AI • Hồ sơ Dạy học & Khảo thí Chuẩn CV 5512 & CV 7991")
        r_hdr.font.name = 'Times New Roman'
        r_hdr.font.size = Pt(8.5)
        r_hdr.font.italic = True
        r_hdr.font.color.rgb = COLOR_MUTED_RGB

    # --- KHỐI TIÊU ĐỀ QUỐC GIA & ĐƠN VỊ ---
    header_table = doc.add_table(rows=1, cols=2)
    header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(header_table, val="none")
    
    cell_left = header_table.rows[0].cells[0]
    p_l = cell_left.paragraphs[0]
    p_l.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p_l.add_run("SỞ GIÁO DỤC VÀ ĐÀO TẠO VĨNH LONG\n")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(10)
    r1.font.color.rgb = COLOR_TEXT_MAIN_RGB
    r2 = p_l.add_run("TRƯỜNG THCS & THPT TỈNH VĨNH LONG")
    r2.bold = True
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = COLOR_PRIMARY_RGB
    
    cell_right = header_table.rows[0].cells[1]
    p_r = cell_right.paragraphs[0]
    p_r.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r3 = p_r.add_run("CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM\n")
    r3.bold = True
    r3.font.name = 'Times New Roman'
    r3.font.size = Pt(10.5)
    r4 = p_r.add_run("Độc lập - Tự do - Hạnh phúc\n")
    r4.bold = True
    r4.font.name = 'Times New Roman'
    r4.font.size = Pt(10)
    r5 = p_r.add_run("―" * 15)
    r5.font.color.rgb = COLOR_MUTED_RGB
    
    doc.add_paragraph().paragraph_format.space_after = Pt(10)
    
    # --- TIÊU ĐỀ CHÍNH BỘ HỒ SƠ ---
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(2)
    r_t = p_title.add_run("HỒ SƠ SƯ PHẠM BÀI DẠY VÀ ĐÁNH GIÁ ĐỊNH KÌ")
    r_t.bold = True
    r_t.font.name = 'Times New Roman'
    r_t.font.size = Pt(16)
    r_t.font.color.rgb = COLOR_PRIMARY_RGB

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(14)
    r_s = p_sub.add_run(f"TÊN BÀI: {metadata.get('lesson_name', '').upper()}")
    r_s.bold = True
    r_s.font.name = 'Times New Roman'
    r_s.font.size = Pt(13)
    r_s.font.color.rgb = COLOR_SECONDARY_RGB
    
    # --- BẢNG THÔNG TIN SƯ PHẠM ---
    info_table = doc.add_table(rows=3, cols=2)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(info_table, color="94A3B8", sz="4")
    
    metadata_fields = [
        ("Môn học & Cấp lớp:", f"{metadata.get('subject', '')} - {metadata.get('grade', '')} ({metadata.get('grade_level', '')})"),
        ("Bộ sách giáo khoa:", f"{metadata.get('book_series', '')}"),
        ("Thời lượng bài dạy:", f"{metadata.get('duration', '')}"),
        ("Khung pháp lý áp dụng:", "Công văn 5512/BGDĐT-GDTrH & Công văn 7991/BGDĐT-GDTrH"),
        ("Ghi chú sư phạm:", f"{metadata.get('special_notes', 'Dạy học tích hợp theo CT GDPT 2018')}"),
        ("Hệ thống khởi tạo:", "EduMaster AI (Trợ lý Giáo dục THCS/THPT)")
    ]
    
    for idx, (label, val) in enumerate(metadata_fields):
        r_idx = idx // 2
        c_idx = idx % 2
        cell = info_table.rows[r_idx].cells[c_idx]
        set_cell_background(cell, "F1F5F9" if c_idx == 0 and r_idx % 2 == 0 else "FFFFFF")
        set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.1
        rl = p.add_run(label + " ")
        rl.bold = True
        rl.font.name = 'Times New Roman'
        rl.font.size = Pt(10)
        rv = p.add_run(val)
        rv.font.name = 'Times New Roman'
        rv.font.size = Pt(10)
        
    doc.add_paragraph().paragraph_format.space_after = Pt(16)
    
    # --- PHẦN 1: KẾ HOẠCH BÀI DẠY (CV 5512) ---
    render_markdown_section_to_docx(doc, lesson_plan_md)
    
    doc.add_page_break()
    
    # --- PHẦN 2: MA TRẬN ĐỀ KIỂM TRA (CV 7991) ---
    render_markdown_section_to_docx(doc, exam_matrix_md)
    
    # --- PHẦN 3: BẢN ĐẶC TẢ ĐỀ KIỂM TRA (CV 7991) ---
    render_markdown_section_to_docx(doc, exam_spec_md)
    
    doc.add_page_break()
    
    # --- PHẦN 4: ĐỀ KIỂM TRA CHI TIẾT ---
    render_markdown_section_to_docx(doc, exam_questions_md)
    
    doc.add_page_break()
    
    # --- PHẦN 5: ĐÁP ÁN & HƯỚNG DẪN CHẤM ---
    render_markdown_section_to_docx(doc, exam_answers_md)
    
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer


# ==========================================
# CẤU HÌNH & XUẤT POWERPOINT (.pptx)
# ==========================================

def export_to_pptx(metadata: dict, slides_data: list[dict]) -> io.BytesIO:
    """
    Xuất trọn bộ Slide bài giảng trình chiếu 16:9 Widescreen gồm:
    - Bìa bài giảng chuyên nghiệp
    - Các slide nội dung có phân khu trực quan và gợi ý hình ảnh
    - Ghi chú người thuyết trình (Speaker Notes) tích hợp sẵn
    """
    prs = pptx.Presentation()
    # 16:9 Widescreen (13.333 x 7.5 inches)
    prs.slide_width = PptxInches(13.333)
    prs.slide_height = PptxInches(7.5)
    
    blank_layout = prs.slide_layouts[6]
    
    # Palette PPTX
    c_navy = PptxRGBColor(30, 58, 138)       # #1E3A8A
    c_sky = PptxRGBColor(2, 132, 199)        # #0284C7
    c_card_bg = PptxRGBColor(248, 250, 252)  # #F8FAFC
    c_visual_bg = PptxRGBColor(238, 242, 255)# #EEF2FF
    c_text_dark = PptxRGBColor(15, 23, 42)   # #0F172A
    c_text_muted = PptxRGBColor(71, 85, 105) # #475569
    c_white = PptxRGBColor(255, 255, 255)
    c_gold = PptxRGBColor(217, 119, 6)       # Amber 600
    
    for idx, slide_info in enumerate(slides_data):
        slide = prs.slides.add_slide(blank_layout)
        
        # 1. Thêm Speaker Notes
        speaker_notes = slide_info.get("speaker_notes", "")
        if speaker_notes:
            notes_slide = slide.notes_slide
            tf = notes_slide.notes_text_frame
            tf.text = speaker_notes
            
        is_title_slide = (idx == 0)
        
        if is_title_slide:
            # === SLIDE BÌA (TITLE SLIDE) ===
            # Nền màu Navy sang trọng
            bg_rect = slide.shapes.add_shape(
                MSO_SHAPE.RECTANGLE,
                PptxInches(0), PptxInches(0), PptxInches(13.333), PptxInches(7.5)
            )
            bg_rect.fill.solid()
            bg_rect.fill.fore_color.rgb = c_navy
            bg_rect.line.fill.background()
            
            # Khối thông tin trường / cấp học
            badge = slide.shapes.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                PptxInches(1.2), PptxInches(1.0), PptxInches(5.0), PptxInches(0.5)
            )
            badge.fill.solid()
            badge.fill.fore_color.rgb = c_sky
            badge.line.fill.background()
            badge_tf = badge.text_frame
            badge_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            p_badge = badge_tf.paragraphs[0]
            p_badge.alignment = PP_ALIGN.CENTER
            r_b = p_badge.add_run()
            r_b.text = f"GIÁO DỤC {metadata.get('grade_level', 'THPT')} • {metadata.get('grade', 'LỚP 10').upper()}"
            r_b.font.bold = True
            r_b.font.size = PptxPt(13)
            r_b.font.color.rgb = c_white
            
            # Hộp Tiêu đề Bài học
            title_box = slide.shapes.add_textbox(
                PptxInches(1.2), PptxInches(1.8), PptxInches(11.0), PptxInches(2.5)
            )
            tf_title = title_box.text_frame
            tf_title.word_wrap = True
            p_t = tf_title.paragraphs[0]
            p_t.text = slide_info.get("title", metadata.get("lesson_name", "BÀI GIẢNG ĐIỆN TỬ"))
            p_t.font.bold = True
            p_t.font.size = PptxPt(38)
            p_t.font.color.rgb = c_white
            
            # Dải phân cách vàng kim
            accent_line = slide.shapes.add_shape(
                MSO_SHAPE.RECTANGLE,
                PptxInches(1.2), PptxInches(4.4), PptxInches(3.0), PptxInches(0.08)
            )
            accent_line.fill.solid()
            accent_line.fill.fore_color.rgb = c_gold
            accent_line.line.fill.background()
            
            # Hộp Thông tin phụ (Bộ sách, Môn, Thời lượng, Câu hỏi khởi động)
            sub_box = slide.shapes.add_textbox(
                PptxInches(1.2), PptxInches(4.6), PptxInches(11.0), PptxInches(2.4)
            )
            tf_sub = sub_box.text_frame
            tf_sub.word_wrap = True
            
            bullets = slide_info.get("bullets", [])
            for bullet in bullets:
                p = tf_sub.add_paragraph()
                p.text = f"• {bullet}"
                p.font.size = PptxPt(16)
                p.font.color.rgb = PptxRGBColor(224, 231, 255)
                p.space_after = PptxPt(6)
                
        else:
            # === CÁC SLIDE NỘI DUNG (CONTENT SLIDES) ===
            # Nền trắng thanh lịch
            bg_rect = slide.shapes.add_shape(
                MSO_SHAPE.RECTANGLE,
                PptxInches(0), PptxInches(0), PptxInches(13.333), PptxInches(7.5)
            )
            bg_rect.fill.solid()
            bg_rect.fill.fore_color.rgb = PptxRGBColor(255, 255, 255)
            bg_rect.line.fill.background()
            
            # Thanh Header trên cùng
            top_bar = slide.shapes.add_shape(
                MSO_SHAPE.RECTANGLE,
                PptxInches(0), PptxInches(0), PptxInches(13.333), PptxInches(1.3)
            )
            top_bar.fill.solid()
            top_bar.fill.fore_color.rgb = c_navy
            top_bar.line.fill.background()
            
            # Badge số slide nhỏ
            num_box = slide.shapes.add_textbox(
                PptxInches(11.8), PptxInches(0.2), PptxInches(1.2), PptxInches(0.9)
            )
            tf_num = num_box.text_frame
            p_num = tf_num.paragraphs[0]
            p_num.alignment = PP_ALIGN.RIGHT
            p_num.text = f"#{slide_info.get('slide_number', idx + 1):02d}"
            p_num.font.bold = True
            p_num.font.size = PptxPt(18)
            p_num.font.color.rgb = c_sky
            
            # Tiêu đề Slide
            title_box = slide.shapes.add_textbox(
                PptxInches(0.8), PptxInches(0.15), PptxInches(10.8), PptxInches(1.0)
            )
            tf_title = title_box.text_frame
            tf_title.word_wrap = True
            p_t = tf_title.paragraphs[0]
            p_t.text = slide_info.get("title", f"SLIDE {idx + 1}")
            p_t.font.bold = True
            p_t.font.size = PptxPt(26)
            p_t.font.color.rgb = c_white
            
            # Card Trái: Nội dung kiến thức cốt lõi (Chiếm 62% chiều rộng)
            card_left = slide.shapes.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                PptxInches(0.8), PptxInches(1.6), PptxInches(7.8), PptxInches(5.3)
            )
            card_left.fill.solid()
            card_left.fill.fore_color.rgb = c_card_bg
            card_left.line.color.rgb = PptxRGBColor(226, 232, 240)
            card_left.line.width = PptxPt(1.5)
            
            # Text trong Card Trái
            content_box = slide.shapes.add_textbox(
                PptxInches(1.1), PptxInches(1.8), PptxInches(7.2), PptxInches(4.9)
            )
            tf_content = content_box.text_frame
            tf_content.word_wrap = True
            
            p_ch = tf_content.paragraphs[0]
            p_ch.text = "NỘI DUNG TRỌNG TÂM:"
            p_ch.font.bold = True
            p_ch.font.size = PptxPt(15)
            p_ch.font.color.rgb = c_sky
            p_ch.space_after = PptxPt(10)
            
            bullets = slide_info.get("bullets", [])
            for bullet in bullets:
                p_b = tf_content.add_paragraph()
                p_b.text = f"• {bullet}"
                p_b.font.size = PptxPt(16)
                p_b.font.color.rgb = c_text_dark
                p_b.space_after = PptxPt(10)
                p_b.line_spacing = 1.2
                
            # Card Phải: Ý tưởng Visual / Hình ảnh minh họa (Chiếm 33% chiều rộng)
            card_right = slide.shapes.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                PptxInches(8.9), PptxInches(1.6), PptxInches(3.7), PptxInches(5.3)
            )
            card_right.fill.solid()
            card_right.fill.fore_color.rgb = c_visual_bg
            card_right.line.color.rgb = PptxRGBColor(199, 210, 254)
            card_right.line.width = PptxPt(1.5)
            
            # Text trong Card Phải
            vis_box = slide.shapes.add_textbox(
                PptxInches(9.1), PptxInches(1.8), PptxInches(3.3), PptxInches(4.9)
            )
            tf_vis = vis_box.text_frame
            tf_vis.word_wrap = True
            
            p_vh = tf_vis.paragraphs[0]
            p_vh.text = "🎨 GỢI Ý MINH HỌA (VISUAL)"
            p_vh.font.bold = True
            p_vh.font.size = PptxPt(14)
            p_vh.font.color.rgb = PptxRGBColor(67, 56, 202)  # Indigo 700
            p_vh.space_after = PptxPt(12)
            
            p_desc = tf_vis.add_paragraph()
            p_desc.text = slide_info.get("visual_prompt", "Hình ảnh hoặc sơ đồ minh họa sinh động cho nội dung bài giảng.")
            p_desc.font.size = PptxPt(13.5)
            p_desc.font.color.rgb = PptxRGBColor(30, 27, 75)
            p_desc.line_spacing = 1.25
            p_desc.space_after = PptxPt(16)
            
            # Badge nhắc nhở Speaker Notes
            p_note_badge = tf_vis.add_paragraph()
            p_note_badge.text = "🎙️ Đã tích hợp lời giảng (Speaker Notes) ở góc dưới của trang slide này."
            p_note_badge.font.italic = True
            p_note_badge.font.size = PptxPt(11.5)
            p_note_badge.font.color.rgb = c_text_muted

    buffer = io.BytesIO()
    prs.save(buffer)
    buffer.seek(0)
    return buffer
