# -*- coding: utf-8 -*-
"""
EduMaster AI - Gemini Integration Service
Kết nối Google Gemini API với System Prompt chuyên sâu chuẩn hóa
Công văn 5512/BGDĐT-GDTrH và Công văn 7991/BGDĐT-GDTrH (ngày 17/12/2024).
"""

import os
import json
import re

SYSTEM_INSTRUCTION = """
Bạn là Kỹ sư Trí tuệ Nhân tạo Giáo dục (EdTech Specialist) kiêm Chuyên gia Phương pháp Dạy học và Khảo thí bậc THCS & THPT của Bộ Giáo dục và Đào tạo Việt Nam.
Nhiệm vụ của bạn là soạn thảo trọn bộ hồ sơ sư phạm gồm 3 phần bắt buộc:

1. PHẦN A: KẾ HOẠCH BÀI DẠY (Chuẩn Công văn số 5512/BGDĐT-GDTrH):
- Tên bài dạy, Môn, Lớp, Bộ sách, Thời lượng.
- I. Mục tiêu:
  + Kiến thức
  + Năng lực (Năng lực chung: Tự chủ & tự học, Giao tiếp & hợp tác, Giải quyết vấn đề & sáng tạo; Năng lực đặc thù môn học theo Chương trình GDPT 2018)
  + Phẩm chất (Yêu nước, Nhân ái, Chăm chỉ, Trung thực, Trách nhiệm)
- II. Thiết bị dạy học và học liệu (Chuẩn bị của Giáo viên và Học sinh)
- III. Tiến trình dạy học gồm đúng 4 hoạt động:
  + Hoạt động 1: Mở đầu / Khởi động (Mục tiêu, Nội dung, Sản phẩm, Tổ chức thực hiện: Bước 1 Chuyển giao -> Bước 2 Thực hiện -> Bước 3 Báo cáo/Thảo luận -> Bước 4 Kết luận/Nhận định).
  + Hoạt động 2: Hình thành kiến thức mới (Chia thành các mạch kiến thức rõ ràng, mỗi mạch con đều có đủ 4 bước tổ chức thực hiện).
  + Hoạt động 3: Luyện tập (Hệ thống câu hỏi, bài tập, phiếu học tập).
  + Hoạt động 4: Vận dụng (Nhiệm vụ thực tiễn, liên hệ đời sống).

2. PHẦN B: DÀN Ý & NỘI DUNG SLIDE BÀI GIẢNG TRÌNH CHIẾU (10 đến 12 Slide):
- Mỗi slide gồm: slide_number, title, bullets (3-4 ý ngắn gọn, súc tích, không viết đoạn văn dài), visual_prompt (ý tưởng hình ảnh/infographic/mô phỏng minh họa), speaker_notes (lời giảng chi tiết của giáo viên khi trình chiếu slide này).
- Cấu trúc:
  + Slide 1: Bìa bài giảng, tên bài, thông tin lớp, câu hỏi khởi động kích thích tư duy.
  + Slide 2: Mục tiêu bài học cần đạt.
  + Slide 3 đến 8: Các nội dung bài học tương ứng mạch kiến thức trọng tâm.
  + Slide 9: Bài tập củng cố nhanh / mini game tương tác.
  + Slide 10: Tổng kết trọng tâm và dặn dò nhiệm vụ về nhà.

3. PHẦN C: ĐỀ KIỂM TRA ĐỊNH KÌ & ĐÁNH GIÁ NĂNG LỰC (Tuyệt đối tuân thủ Công văn số 7991/BGDĐT-GDTrH ngày 17/12/2024 của Bộ GDĐT):
- 1. Ma trận đề kiểm tra:
  + Kẻ bảng Markdown đúng khung phụ lục CV 7991.
  + Tỉ lệ nhận thức: Nhận biết (40%) - Thông hiểu (30%) - Vận dụng (30%).
  + Tỉ lệ hình thức:
    * TNKQ Nhiều lựa chọn: 3,0 điểm (30%)
    * TNKQ Đúng - Sai: 2,0 điểm (20%)
    * TNKQ Trả lời ngắn: 2,0 điểm (20%) (Với môn Ngữ văn có thể linh hoạt chuyển sang Tự luận/Đọc hiểu)
    * Tự luận: 3,0 điểm (30%).
- 2. Bản đặc tả đề kiểm tra:
  + Bảng Markdown chi tiết: TT, Chủ đề/Mạch kiến thức, Đơn vị kiến thức, Mức độ đánh giá / Yêu cầu cần đạt, Số câu hỏi theo mức độ, Mã hóa năng lực môn học (NL_...).
- 3. Đề kiểm tra chi tiết:
  + Phần I: Trắc nghiệm 4 lựa chọn (Câu 1 đến Câu 6 hoặc 12, mỗi câu 4 phương án A, B, C, D).
  + Phần II: Trắc nghiệm Đúng - Sai (Mỗi câu gồm 4 ý a, b, c, d; kèm quy tắc tính điểm: Đúng 1 ý = 0.1đ; Đúng 2 ý = 0.25đ; Đúng 3 ý = 0.5đ; Đúng 4 ý = 1.0đ).
  + Phần III: Trắc nghiệm Trả lời ngắn (Các câu hỏi tính toán hoặc điền kết quả ngắn gọn).
  + Phần IV: Câu hỏi Tự luận (Tình huống thực tiễn vận dụng năng lực, các ý phân hóa).
- 4. Hướng dẫn chấm và Đáp án chi tiết:
  + Bảng đáp án Phần I, II, III và Bareme chấm chi tiết từng bước cho Phần IV.

ĐẦU RA BẮT BUỘC: Bạn PHẢI trả về ĐÚNG ĐỊNH DẠNG JSON với cấu trúc sau (không kèm lời chào hay văn bản ngoài JSON):
{
  "pedagogical_summary": "Tóm tắt ngắn gọn 2-3 câu về ý đồ sư phạm và điểm nhấn của bài giảng",
  "lesson_plan_markdown": "Toàn văn kế hoạch bài dạy chuẩn CV 5512 bằng định dạng Markdown hoàn chỉnh",
  "slides": [
    {
      "slide_number": 1,
      "title": "Tiêu đề Slide",
      "bullets": ["Ý 1", "Ý 2", "Ý 3"],
      "visual_prompt": "Mô tả ý tưởng hình ảnh / infographic",
      "speaker_notes": "Lời giảng chi tiết của giáo viên"
    }
  ],
  "exam_matrix_markdown": "Bảng ma trận đề kiểm tra chuẩn CV 7991 định dạng Markdown",
  "exam_spec_markdown": "Bản đặc tả đề kiểm tra chuẩn CV 7991 định dạng Markdown",
  "exam_questions_markdown": "Toàn bộ câu hỏi đề kiểm tra 4 phần (I, II, III, IV) định dạng Markdown",
  "exam_answers_markdown": "Hướng dẫn chấm và đáp án chi tiết định dạng Markdown"
}
"""


def extract_json_from_response(text: str) -> dict:
    """Trích xuất và phân tích JSON từ phản hồi của mô hình LLM."""
    text = text.strip()
    
    # 1. Thử phân tích trực tiếp
    try:
        return json.loads(text)
    except Exception:
        pass
        
    # 2. Tìm khối ```json ... ```
    match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except Exception:
            pass
            
    # 3. Tìm khối ngoặc nhọn đầu tiên và cuối cùng
    start = text.find('{')
    end = text.rfind('}')
    if start != -1 and end != -1 and end > start:
        candidate = text[start:end+1]
        try:
            return json.loads(candidate)
        except Exception:
            pass
            
    raise ValueError("Không thể phân tích dữ liệu JSON chuẩn từ phản hồi của Gemini API.")


def generate_pedagogical_package(
    api_key: str,
    grade_level: str,
    grade: str,
    subject: str,
    book_series: str,
    lesson_name: str,
    duration: str,
    special_notes: str,
    model_name: str = "gemini-2.5-flash"
) -> dict:
    """
    Gọi Gemini API để khởi tạo trọn bộ tài liệu sư phạm chuẩn CV 5512 & CV 7991.
    Tự động hỗ trợ cả google.genai (SDK mới) và google.generativeai (SDK truyền thống).
    """
    if not api_key:
        raise ValueError("Chưa cung cấp Google Gemini API Key. Vui lòng nhập API Key trong thanh cấu hình bên trái.")

    user_prompt = f"""
Hãy tạo trọn bộ Kế hoạch bài dạy (CV 5512), Dàn ý Slide trình chiếu (10-12 slide) và Đề kiểm tra ma trận đặc tả (CV 7991) cho thông tin sau:
- Cấp học: {grade_level}
- Lớp: {grade}
- Môn học: {subject}
- Bộ sách giáo khoa: {book_series}
- Tên bài dạy / Chủ đề: {lesson_name}
- Thời lượng: {duration}
- Yêu cầu sư phạm đặc biệt: {special_notes if special_notes.strip() else 'Tuân thủ chặt chẽ định hướng phát triển phẩm chất và năng lực theo CT GDPT 2018.'}

LƯU Ý QUAN TRỌNG:
1. Đảm bảo Kế hoạch bài dạy có ĐỦ 4 HOẠT ĐỘNG (Khởi động, Hình thành kiến thức, Luyện tập, Vận dụng) với 4 bước tổ chức (Chuyển giao, Thực hiện, Báo cáo/Thảo luận, Kết luận).
2. Tạo từ 10 đến 12 slide với đầy đủ tiêu đề, gạch đầu dòng cô đọng, gợi ý hình ảnh và LỜI GIẢNG CỦA GIÁO VIÊN (speaker_notes).
3. Đề kiểm tra BẮT BUỘC tuân thủ chuẩn Công văn 7991/BGDĐT-GDTrH:
   - Tỉ lệ nhận thức: 40% Biết - 30% Hiểu - 30% Vận dụng
   - Đúng cấu trúc 4 phần: Phần I (TNKQ 4 lựa chọn), Phần II (TNKQ Đúng-Sai kèm thang điểm 0.1 - 0.25 - 0.5 - 1.0), Phần III (TNKQ Trả lời ngắn), Phần IV (Tự luận vận dụng).
   - Có cả Ma trận, Bản đặc tả, Đề bài và Hướng dẫn chấm chi tiết.

Trả về kết quả ở định dạng JSON thuần theo schema đã chỉ định.
"""

    raw_text = None
    last_err = None

    # Cách 1: Thử nghiệm với google.genai (Google GenAI SDK thế hệ mới)
    try:
        from google import genai
        from google.genai import types
        
        client = genai.Client(api_key=api_key)
        
        # Cấu hình JSON output
        config = types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.4,
            response_mime_type="application/json"
        )
        
        # Thử với model chỉ định hoặc fallback
        candidate_models = [model_name, "gemini-2.5-flash", "gemini-1.5-flash", "gemini-1.5-pro"]
        # Loại bỏ trùng lặp giữ nguyên thứ tự
        seen = set()
        models_to_try = [m for m in candidate_models if not (m in seen or seen.add(m))]
        
        for m in models_to_try:
            try:
                response = client.models.generate_content(
                    model=m,
                    contents=user_prompt,
                    config=config
                )
                if response and response.text:
                    raw_text = response.text
                    break
            except Exception as e_genai_model:
                last_err = e_genai_model
                continue
                
    except Exception as e_genai:
        last_err = e_genai

    # Cách 2: Nếu chưa lấy được, thử với google.generativeai (Legacy SDK)
    if not raw_text:
        try:
            import google.generativeai as genai_legacy
            genai_legacy.configure(api_key=api_key)
            
            candidate_models = [model_name, "gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash"]
            seen = set()
            models_to_try = [m for m in candidate_models if not (m in seen or seen.add(m))]
            
            for m in models_to_try:
                try:
                    generation_config = {
                        "temperature": 0.4,
                        "response_mime_type": "application/json"
                    }
                    model = genai_legacy.GenerativeModel(
                        model_name=m,
                        system_instruction=SYSTEM_INSTRUCTION,
                        generation_config=generation_config
                    )
                    res = model.generate_content(user_prompt)
                    if res and res.text:
                        raw_text = res.text
                        break
                except Exception as e_legacy_model:
                    last_err = e_legacy_model
                    continue
        except Exception as e_legacy:
            last_err = e_legacy

    if not raw_text:
        raise RuntimeError(f"Không thể kết nối Gemini API. Chi tiết lỗi: {last_err}")

    # Phân tích dữ liệu JSON trả về
    data = extract_json_from_response(raw_text)
    return data
