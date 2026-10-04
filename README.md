# 🎓 EduMaster AI - Hệ thống Soạn giảng & Khảo thí chuẩn Công văn 7991 & 5512

> **Ứng dụng Trí tuệ Nhân tạo thế hệ mới hỗ trợ Giáo viên THCS và THPT (tỉnh Vĩnh Long và Toàn quốc)**  
> Tự động hóa soạn thảo Kế hoạch bài dạy chuẩn mực, dàn ý trình chiếu bài giảng trực quan và thiết kế ma trận, bản đặc tả, đề kiểm tra định kì chuẩn xác theo các quy định mới nhất của Bộ Giáo dục và Đào tạo.

---

## 🌟 TÍNH NĂNG VÀ ĐIỂM NHẤN CÔNG NGHỆ

### 1. Chuẩn hóa Khung pháp lý Giáo dục Việt Nam
- **Kế hoạch bài dạy theo Công văn số 5512/BGDĐT-GDTrH:**
  - Đầy đủ 3 mục tiêu trụ cột: Kiến thức, Năng lực (Năng lực chung + Năng lực đặc thù môn học theo Chương trình GDPT 2018), Phẩm chất.
  - Chuẩn bị thiết bị và học liệu chi tiết của Giáo viên & Học sinh.
  - Tiến trình dạy học gồm đúng 4 hoạt động bắt buộc:
    1. *Hoạt động 1: Mở đầu / Khởi động*
    2. *Hoạt động 2: Hình thành kiến thức mới* (chia theo các mạch nội dung)
    3. *Hoạt động 3: Luyện tập*
    4. *Hoạt động 4: Vận dụng*
  - Mỗi hoạt động đều triển khai chặt chẽ theo 4 bước sư phạm: **Chuyển giao nhiệm vụ ➔ Thực hiện nhiệm vụ ➔ Báo cáo, thảo luận ➔ Kết luận, nhận định**.

- **Đề kiểm tra định kì & Đánh giá năng lực theo Công văn số 7991/BGDĐT-GDTrH (ngày 17/12/2024):**
  - **Ma trận đề kiểm tra:** Kẻ bảng đúng khung chuẩn với tỉ lệ nhận thức: **Biết (40%) - Hiểu (30%) - Vận dụng (30%)**.
  - **Bản đặc tả đề kiểm tra:** Chi tiết yêu cầu cần đạt, mức độ tư duy và mã hóa năng lực môn học (`NL_...`).
  - **Cấu trúc đề kiểm tra 4 phần định dạng mới:**
    - *Phần I:* Câu hỏi trắc nghiệm nhiều lựa chọn (3,0 điểm).
    - *Phần II:* Câu hỏi trắc nghiệm Đúng - Sai (2,0 điểm) với **quy tắc tính điểm phân hóa chuẩn CV 7991**: Đúng 1 ý = 0,10đ; Đúng 2 ý = 0,25đ; Đúng 3 ý = 0,50đ; Đúng 4 ý = 1,00đ.
    - *Phần III:* Câu hỏi trắc nghiệm trả lời ngắn (2,0 điểm).
    - *Phần IV:* Câu hỏi tự luận giải quyết vấn đề thực tiễn (3,0 điểm).
  - **Hướng dẫn chấm & Đáp án chi tiết:** Bảng đáp án Phần I, II, III và bareme chấm chi tiết từng bước cho Phần IV.

- **Dàn ý & Trình chiếu Slide (10 - 12 slide):**
  - Cấu trúc trình bày trực quan, mỗi slide gồm các gạch đầu dòng cô đọng, gợi ý ý tưởng hình ảnh/mô phỏng (*Visual prompt*).
  - Tích hợp sẵn **Lời giảng của giáo viên (*Speaker Notes*)** trong từng slide giúp thầy cô tự tin đứng lớp thuyết trình.

### 2. Trung tâm Xuất bản Thực tế (Export Center)
- **Xuất file Word (`.docx`):** Bằng thư viện `python-docx`, tự động chuyển đổi bảng Markdown sang bảng Word có viền thanh lịch, header màu sắc nhận diện, căn lề chuẩn hành chính (Top/Bottom: 2cm, Left: 2.5cm, Right: 2cm).
- **Xuất file PowerPoint (`.pptx`):** Bằng thư viện `python-pptx`, thiết kế chuẩn tỉ lệ 16:9 Widescreen với bảng màu Navy - Sky Blue hiện đại, phân khu thẻ nội dung và tự động nạp Speaker Notes vào khung ghi chú của từng slide.
- **Dữ liệu mẫu tức thì (*Demo Mode*):** Cho phép ban giám khảo và giáo viên trải nghiệm đầy đủ giao diện, xem trước tài liệu và tải file mẫu hoàn chỉnh ngay cả khi chưa có Gemini API Key.

---

## 🚀 HƯỚNG DẪN CÀI ĐẶT & CHẠY LOCAL (MÁY CÁ NHÂN)

### Yêu cầu hệ thống
- Python 3.10 trở lên.
- Đã cài đặt `pip`.

### Bước 1: Di chuyển vào thư mục dự án
```bash
cd /Users/wocten/Documents/masteredu
```

### Bước 2: Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt
```

### Bước 3: Khởi chạy ứng dụng Web
```bash
streamlit run app.py
```
Sau khi chạy lệnh trên, trình duyệt web sẽ tự động mở địa chỉ:
`http://localhost:8501`

---

## 🌐 HƯỚNG DẪN TRIỂN KHAI LÊN STREAMLIT COMMUNITY CLOUD (LẤY LINK DỰ THI)

Để tạo link trực tuyến dạng `https://edumaster-ai.streamlit.app` gửi cho Ban Giám khảo hoặc Thầy/Cô sử dụng trực tiếp trên điện thoại và máy tính:

### Bước 1: Đẩy mã nguồn lên GitHub
1. Tạo một repository mới trên [GitHub](https://github.com/new) (ví dụ: `edumaster-ai`).
2. Khởi tạo Git và đẩy mã nguồn lên:
   ```bash
   git init
   git add .
   git commit -m "Khoi tao du an EduMaster AI"
   git branch -M main
   git remote add origin https://github.com/<tai-khoan-github>/edumaster-ai.git
   git push -u origin main
   ```

### Bước 2: Triển khai lên Streamlit Community Cloud
1. Truy cập vào [Streamlit Community Cloud](https://share.streamlit.io/) và đăng nhập bằng tài khoản GitHub.
2. Bấm nút **"Create app"** (hoặc **"New app"**).
3. Điền các thông tin:
   - **Repository:** `<tai-khoan-github>/edumaster-ai`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL:** Đặt tên tùy chọn (ví dụ: `edumaster-vinhlong.streamlit.app`).

### Bước 3: Cấu hình API Key tự động (Tùy chọn)
Trong phần **Advanced settings** ➔ **Secrets**, bạn có thể thêm dòng sau để ứng dụng tự động nhận diện API Key cho toàn bộ người dùng mà không cần nhập thủ công:
```toml
GEMINI_API_KEY = "Khóa-API-Gemini-Của-Bạn"
```

Bấm **"Deploy!"** và chờ 1-2 phút. Bạn sẽ nhận được đường link chính thức:
`https://edumaster-vinhlong.streamlit.app` sẵn sàng để nộp bài dự thi!

---

## 📁 CẤU TRÚC MÃ NGUỒN

```
masteredu/
├── .streamlit/
│   └── config.toml          # Cấu hình giao diện Streamlit (Tone màu xanh sư phạm)
├── app.py                   # Giao diện chính và luồng xử lý ứng dụng
├── gemini_service.py        # Logic tích hợp Gemini API (Dual SDK google.genai & generativeai)
├── export_utils.py          # Bộ công cụ xuất file Word (.docx) và PowerPoint (.pptx)
├── sample_data.py           # Dữ liệu chuẩn mẫu CV 5512 & CV 7991 dùng để trải nghiệm tức thì
├── requirements.txt         # Danh mục thư viện Python phụ thuộc
└── README.md                # Tài liệu hướng dẫn sử dụng & triển khai
```

---

## 🏆 ĐƠN VỊ THỰC HIỆN & BẢN QUYỀN
- Dự án: **EduMaster AI - Hệ thống Soạn giảng & Khảo thí chuẩn Công văn 7991 & 5512**
- Đối tượng thụ hưởng: Giáo viên các trường THCS & THPT tỉnh Vĩnh Long và toàn quốc.
- Công nghệ: Python, Streamlit, Google Gemini Flash/Pro, python-docx, python-pptx.
