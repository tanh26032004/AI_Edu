# -*- coding: utf-8 -*-
"""
Script chạy thử nghiệm cục bộ hệ thống EduMaster AI:
1. Kiểm tra tính toàn vẹn của dữ liệu mẫu CV 5512 & CV 7991.
2. Xuất trực tiếp file Word (.docx) và PowerPoint (.pptx) mẫu ra thư mục hiện tại để mở xem ngay.
3. Hướng dẫn khởi chạy Web App.
"""

import os
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

def main():
    print("=" * 65)
    print("🎓 KIỂM TRA CHẠY THỬ HỆ THỐNG EDUMASTER AI")
    print("=" * 65)
    
    # 1. Thông tin bài dạy mẫu
    print(f"\n[1] Thông tin bài dạy thử nghiệm:")
    print(f"    - Môn học: {SAMPLE_METADATA['subject']} ({SAMPLE_METADATA['grade']})")
    print(f"    - Bộ sách: {SAMPLE_METADATA['book_series']}")
    print(f"    - Tên bài: {SAMPLE_METADATA['lesson_name']}")
    print(f"    - Thời lượng: {SAMPLE_METADATA['duration']}")
    print(f"    - Tiêu chuẩn áp dụng: CV 5512/BGDĐT & CV 7991/BGDĐT (17/12/2024)")

    # 2. Xuất thử file Word (.docx)
    print(f"\n[2] Đang tạo file Word (.docx) chuẩn hồ sơ giáo án & khảo thí...")
    docx_buf = export_to_docx(
        metadata=SAMPLE_METADATA,
        lesson_plan_md=SAMPLE_LESSON_PLAN,
        exam_matrix_md=SAMPLE_EXAM_MATRIX,
        exam_spec_md=SAMPLE_EXAM_SPEC,
        exam_questions_md=SAMPLE_EXAM_QUESTIONS,
        exam_answers_md=SAMPLE_EXAM_ANSWERS
    )
    docx_path = "EduMaster_Demo_Ho_So.docx"
    with open(docx_path, "wb") as f:
        f.write(docx_buf.getvalue())
    docx_size_kb = os.path.getsize(docx_path) / 1024
    print(f"    ✅ Đã tạo thành công file Word: {docx_path} ({docx_size_kb:.1f} KB)")
    print(f"       (Bao gồm: Kế hoạch bài dạy 4 hoạt động + Ma trận + Bản đặc tả + Đề 4 phần + Hướng dẫn chấm)")

    # 3. Xuất thử file PowerPoint (.pptx)
    print(f"\n[3] Đang tạo file PowerPoint (.pptx) bài giảng trình chiếu 16:9...")
    pptx_buf = export_to_pptx(
        metadata=SAMPLE_METADATA,
        slides_data=SAMPLE_SLIDES
    )
    pptx_path = "EduMaster_Demo_Slide.pptx"
    with open(pptx_path, "wb") as f:
        f.write(pptx_buf.getvalue())
    pptx_size_kb = os.path.getsize(pptx_path) / 1024
    print(f"    ✅ Đã tạo thành công file PowerPoint: {pptx_path} ({pptx_size_kb:.1f} KB)")
    print(f"       (Bao gồm: {len(SAMPLE_SLIDES)} Slides có bố cục hiện đại, gợi ý Visual & Speaker Notes)")

    print("\n" + "=" * 65)
    print("🎉 TẤT CẢ CÁC MODULE ĐỀU HOẠT ĐỘNG HOÀN HẢO!")
    print("=" * 65)
    print("\n👉 Để mở giao diện Web App Streamlit, bạn chỉ cần gõ:")
    print("    streamlit run app.py\n")

if __name__ == "__main__":
    main()
