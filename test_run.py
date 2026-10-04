# -*- coding: utf-8 -*-
"""
Script chạy thử nghiệm cục bộ hệ thống EduMaster AI đa môn học:
1. Kiểm tra tính toàn vẹn của dữ liệu mẫu CV 5512 & CV 7991 cho nhiều môn học (Toán, Văn, Vật lí...).
2. Xuất trực tiếp file Word (.docx) và PowerPoint (.pptx) mẫu theo từng môn.
"""

import os
from sample_data import get_sample_package_for_subject, SUBJECT_PRESETS
from export_utils import export_to_docx, export_to_pptx

def test_subject(subject_name, grade="Lớp 10"):
    print("\n" + "-" * 60)
    print(f"👉 KIỂM THỬ MÔN: {subject_name} ({grade})")
    print("-" * 60)
    pkg = get_sample_package_for_subject(subject_name, grade=grade)
    meta = pkg["metadata"]
    print(f"• Tên bài: {meta['lesson_name']}")
    print(f"• Bộ sách: {meta['book_series']} | Thời lượng: {meta['duration']}")
    print(f"• Số lượng slide trình chiếu: {len(pkg['slides'])} trang (kèm Lời giảng)")
    
    # Xuất docx
    docx_buf = export_to_docx(
        metadata=meta,
        lesson_plan_md=pkg["lesson_plan"],
        exam_matrix_md=pkg["exam_matrix"],
        exam_spec_md=pkg["exam_spec"],
        exam_questions_md=pkg["exam_questions"],
        exam_answers_md=pkg["exam_answers"]
    )
    clean_subj = subject_name.replace(" ", "_").replace("(", "").replace(")", "")
    docx_path = f"EduMaster_{clean_subj}.docx"
    with open(docx_path, "wb") as f:
        f.write(docx_buf.getvalue())
    print(f"  ✅ Đã xuất Word: {docx_path} ({len(docx_buf.getvalue())/1024:.1f} KB)")

    # Xuất pptx
    pptx_buf = export_to_pptx(meta, pkg["slides"])
    pptx_path = f"EduMaster_{clean_subj}.pptx"
    with open(pptx_path, "wb") as f:
        f.write(pptx_buf.getvalue())
    print(f"  ✅ Đã xuất PowerPoint: {pptx_path} ({len(pptx_buf.getvalue())/1024:.1f} KB)")

def main():
    print("=" * 65)
    print("🎓 KIỂM TRA CHẠY THỬ HỆ THỐNG EDUMASTER AI ĐA MÔN HỌC")
    print("=" * 65)
    
    # Kiểm thử 3 môn đại diện chính
    test_subject("Toán", "Lớp 10")
    test_subject("Ngữ văn", "Lớp 10")
    test_subject("Vật lí", "Lớp 10")
    test_subject("Khoa học tự nhiên (KHTN)", "Lớp 8")

    print("\n" + "=" * 65)
    print("🎉 TẤT CẢ CÁC MÔN HỌC ĐỀU XUẤT FILE WORD VÀ POWERPOINT THÀNH CÔNG!")
    print("=" * 65)
    print("\n👉 Để mở giao diện Web App, hãy chạy:")
    print("    streamlit run app.py\n")

if __name__ == "__main__":
    main()
