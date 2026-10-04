# -*- coding: utf-8 -*-
"""
Dữ liệu mẫu chuẩn hóa theo Công văn 5512/BGDĐT-GDTrH và Công văn 7991/BGDĐT-GDTrH.
Được biên soạn đầy đủ để kiểm thử và trình diễn ngay lập tức.
"""

SAMPLE_METADATA = {
    "grade_level": "THPT",
    "grade": "Lớp 10",
    "subject": "Vật lí",
    "book_series": "Kết nối tri thức với cuộc sống",
    "lesson_name": "Bài 26: Cơ năng và định luật bảo toàn cơ năng",
    "duration": "2 tiết (90 phút)",
    "special_notes": "Tích hợp mô hình lớp học đảo ngược, rèn luyện tư duy thực nghiệm và giải quyết vấn đề thực tiễn thông qua trò chơi Tàu lượn siêu tốc."
}

SAMPLE_LESSON_PLAN = """# KẾ HOẠCH BÀI DẠY (THEO CÔNG VĂN 5512/BGDĐT-GDTrH)

**TÊN BÀI DẠY: BÀI 26 - CƠ NĂNG VÀ ĐỊNH LUẬT BẢO TOÀN CƠ NĂNG**  
**Môn học:** Vật lí | **Lớp:** 10  
**Bộ sách:** Kết nối tri thức với cuộc sống  
**Thời lượng thực hiện:** 2 tiết (90 phút)  

---

## I. MỤC TIÊU BÀI HỌC

### 1. Về kiến thức
- Phát biểu được định nghĩa cơ năng của vật chuyển động trong trọng trường là tổng động năng và thế năng trọng trường.
- Viết được công thức tính cơ năng: $W = W_đ + W_t = \\frac{1}{2}mv^2 + mgz$.
- Phát biểu và viết được biểu thức của định luật bảo toàn cơ năng trong trường hợp vật chỉ chịu tác dụng của trọng lực.
- Phân tích được sự chuyển hóa giữa động năng và thế năng trong các hiện tượng thực tế (con lắc đơn, chuyển động ném, tàu lượn).

### 2. Về năng lực
- **Năng lực chung:**
  - *Tự chủ và tự học:* Chủ động nghiên cứu SGK, tài liệu học tập, hoàn thành phiếu học tập cá nhân trước khi thảo luận nhóm.
  - *Giao tiếp và hợp tác:* Phân công nhiệm vụ rõ ràng trong nhóm thí nghiệm ảo, lắng nghe và phản biện tích cực kết quả khảo sát.
  - *Giải quyết vấn đề và sáng tạo:* Đề xuất phương án đo vận tốc của vật để kiểm chứng sự bảo toàn cơ năng trong các bài toán thực tiễn.
- **Năng lực vật lí (Đặc thù môn học theo CT GDPT 2018):**
  - *Nhận thức vật lí:* Nêu được điều kiện để cơ năng được bảo toàn (chỉ chịu tác dụng của lực thế - trọng lực/lực đàn hồi; bỏ qua lực cản).
  - *Tìm hiểu thế giới tự nhiên dưới góc độ vật lí:* Thu thập số liệu từ mô phỏng PhET (Energy Skate Park) để phân tích đồ thị động năng, thế năng và cơ năng.
  - *Vận dụng kiến thức, kĩ năng đã học:* Giải thích nguyên lí hoạt động an toàn của hệ thống tàu lượn siêu tốc và đập thủy điện.

### 3. Về phẩm chất
- *Chăm chỉ:* Tích cực tham gia xây dựng bài, nghiêm túc xử lí số liệu thực nghiệm.
- *Trung thực:* Ghi chép trung thực số liệu quan sát từ mô phỏng, không tự ý chỉnh sửa kết quả.
- *Trách nhiệm:* Hoàn thành đúng tiến độ các nhiệm vụ học tập của nhóm.

---

## II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU

1. **Giáo viên chuẩn bị:**
   - Kế hoạch bài dạy, bài giảng điện tử (PowerPoint / Canva).
   - Video tình huống: Trò chơi tàu lượn siêu tốc tại công viên giải trí.
   - Phần mềm mô phỏng PhET: "Energy Skate Park: Basics".
   - Bộ thí nghiệm con lắc đơn hoặc cảm biến chuyển động kết nối máy vi tính (nếu có phòng thực hành).
   - Phiếu học tập số 1 (Khởi động & Khám phá), Phiếu học tập số 2 (Kiểm chứng định luật).

2. **Học sinh chuẩn bị:**
   - SGK Vật lí 10, vở ghi chép, máy tính cầm tay.
   - Đọc trước bài 26 SGK; ôn lại công thức động năng ($W_đ = \\frac{1}{2}mv^2$) và thế năng trọng trường ($W_t = mgz$).

---

## III. TIẾN TRÌNH DẠY HỌC

### 1. HOẠT ĐỘNG 1: MỞ ĐẦU / KHỞI ĐỘNG (10 phút)
- **a) Mục tiêu:** Kích thích sự tò mò, tạo mâu thuẫn nhận thức về sự biến đổi qua lại giữa độ cao và vận tốc của toa tàu lượn siêu tốc khi chuyển động.
- **b) Nội dung:** Học sinh quan sát đoạn video ngắn (45 giây) về tàu lượn siêu tốc rơi từ đỉnh cao xuống thung lũng ray, trả lời câu hỏi: *“Tại sao ở vị trí cao nhất tàu chuyển động rất chậm, nhưng khi xuống đến điểm thấp nhất tàu lại lao đi với tốc độ cực đại? Có đại lượng vật lí nào được giữ nguyên không đổi trong suốt chuyến đi không?”*
- **c) Sản phẩm:** Câu trả lời dự đoán của học sinh (ở đỉnh: thế năng lớn nhất, động năng nhỏ; ở đáy: động năng cực đại; tổng năng lượng dường như không đổi nếu ma sát rất nhỏ).
- **d) Tổ chức thực hiện:**
  - *Bước 1: Chuyển giao nhiệm vụ:* GV chiếu video và phát phiếu K-W-L mini cho các bàn.
  - *Bước 2: Thực hiện nhiệm vụ:* HS xem video, thảo luận cặp đôi trong 2 phút và ghi câu trả lời ra giấy nháp.
  - *Bước 3: Báo cáo, thảo luận:* Đại diện 2 cặp trả lời; các nhóm khác nhận xét, bổ sung.
  - *Bước 4: Kết luận, nhận định:* GV tổng kết: Độ cao (thế năng) giảm thì vận tốc (động năng) tăng. Mối liên hệ toán học chính xác giữa chúng là gì? Chúng ta cùng vào bài học hôm nay.

---

### 2. HOẠT ĐỘNG 2: HÌNH THÀNH KIẾN THỨC MỚI (50 phút)

#### Mạch 1: Khái niệm cơ năng của vật trong trọng trường (20 phút)
- **a) Mục tiêu:** Định nghĩa được cơ năng, viết được biểu thức và đơn vị đo.
- **b) Nội dung:** Phân tích một vật có khối lượng $m$ chuyển động ở độ cao $z$ với vận tốc $v$. Xây dựng tổng năng lượng mà vật sở hữu.
- **c) Sản phẩm:** Công thức $W = W_đ + W_t = \\frac{1}{2}mv^2 + mgz$; đơn vị Jun (J).
- **d) Tổ chức thực hiện:**
  - *Bước 1 (Chuyển giao):* GV yêu cầu nhắc lại công thức động năng, thế năng; yêu cầu HS lập tổng năng lượng cơ học.
  - *Bước 2 (Thực hiện):* HS làm việc cá nhân, sau đó thống nhất theo bàn.
  - *Bước 3 (Báo cáo):* Một HS lên bảng ghi công thức, giải thích ý nghĩa các đại lượng và đơn vị đo.
  - *Bước 4 (Kết luận):* GV chuẩn hóa định nghĩa: *Cơ năng của vật chuyển động dưới tác dụng của trọng lực bằng tổng động năng và thế năng trọng trường của vật.*

#### Mạch 2: Định luật bảo toàn cơ năng (30 phút)
- **a) Mục tiêu:** Chứng minh toán học định luật bảo toàn cơ năng khi chỉ có trọng lực sinh công; khảo sát mô phỏng PhET kiểm chứng.
- **b) Nội dung:** Xét vật rơi tự do từ vị trí 1 ($z_1, v_1$) đến vị trí 2 ($z_2, v_2$). Sử dụng định lí biến thiên động năng: $A_P = W_{đ2} - W_{đ1}$ và công của trọng lực $A_P = W_{t1} - W_{t2}$. Rút ra hệ thức bảo toàn.
- **c) Sản phẩm:** Hệ thức $W_1 = W_2 \\Leftrightarrow \\frac{1}{2}mv_1^2 + mgz_1 = \\frac{1}{2}mv_2^2 + mgz_2 = \\text{hằng số}$.
- **d) Tổ chức thực hiện:**
  - *Bước 1 (Chuyển giao):* GV giao Phiếu học tập số 2 chia nhóm 4 học sinh: Nhiệm vụ 1: Biến đổi biểu thức giải tích; Nhiệm vụ 2: Quan sát mô phỏng PhET Energy Skate Park không ma sát và ghi nhận tổng cột năng lượng Total.
  - *Bước 2 (Thực hiện):* Các nhóm làm việc trong 10 phút, GV quan sát hỗ trợ các nhóm gặp khó khăn khi biến đổi công.
  - *Bước 3 (Báo cáo):* Đại diện nhóm 1 trình bày phép biến đổi toán học; Nhóm 3 trình bày ảnh chụp màn hình PhET chỉ ra cột Total luôn giữ mức cố định.
  - *Bước 4 (Kết luận):* GV kết luận và nhấn mạnh điều kiện nghiệm đúng: *Khi một vật chuyển động trong trọng trường chỉ chịu tác dụng của trọng lực thì cơ năng của vật là một đại lượng bảo toàn.* Mở rộng: Nếu có ma sát, cơ năng không bảo toàn mà chuyển hóa thành nhiệt năng ($W_2 - W_1 = A_{Fms} < 0$).

---

### 3. HOẠT ĐỘNG 3: LUYỆN TẬP (18 phút)
- **a) Mục tiêu:** Vận dụng định luật bảo toàn cơ năng để giải các bài toán định lượng cơ bản (tìm vận tốc tại chân dốc, độ cao cực đại).
- **b) Nội dung:**
  - *Bài tập 1:* Thả rơi tự do một quả bóng khối lượng $m = 200\\text{ g}$ từ độ cao $h = 20\\text{ m}$ so với mặt đất ($g = 10\\text{ m/s}^2$). Bỏ qua sức cản không khí. Tính vận tốc của vật ngay trước khi chạm đất và độ cao mà tại đó thế năng bằng động năng.
  - *Bài tập 2:* Trả lời nhanh 3 câu hỏi trắc nghiệm tương tác trên bảng tương tác / phần mềm Quizizz.
- **c) Sản phẩm:** Lời giải chi tiết của học sinh:
  - Cơ năng tại vị trí thả: $W = mgh = 0{,}2 \\times 10 \\times 20 = 40\\text{ J}$.
  - Tại đất ($z = 0$): $W = \\frac{1}{2}mv_{max}^2 = 40 \\Rightarrow v_{max} = \\sqrt{2gh} = 20\\text{ m/s}$.
  - Khi $W_t = W_đ$: $W = 2W_t \\Rightarrow mgh = 2mgz \\Rightarrow z = \\frac{h}{2} = 10\\text{ m}$.
- **d) Tổ chức thực hiện:**
  - *Bước 1:* GV chiếu đề bài, giao thời gian 7 phút làm bài độc lập.
  - *Bước 2:* HS làm bài vào vở, 2 HS xung phong lên bảng giải.
  - *Bước 3:* Lớp nhận xét chéo, sửa sai sót về đơn vị hoặc chọn mốc thế năng.
  - *Bước 4:* GV nhận xét, chốt quy trình 4 bước giải bài toán bảo toàn cơ năng (Chọn mốc thế năng -> Viết cơ năng trạng thái 1 -> Viết cơ năng trạng thái 2 -> Áp dụng $W_1 = W_2$).

---

### 4. HOẠT ĐỘNG 4: VẬN DỤNG VÀ MỞ RỘNG (12 phút)
- **a) Mục tiêu:** Phát triển năng lực vận dụng kiến thức vào thực tế đời sống, phân tích an toàn giao thông và năng lượng tái tạo.
- **b) Nội dung:** Nhiệm vụ dự án nhỏ: *"Tại các cung đường đèo hiểm trở (như đèo Hải Vân hay các dốc cầu lớn tại miền Tây), người ta thường thiết kế các 'hốc lánh nạn' (đoạn đường dốc ngược lên phủ cát sỏi). Hãy dùng kiến thức về cơ năng và công của lực ma sát để giải thích nguyên lí hãm xe mất phanh của hốc lánh nạn."*
- **c) Sản phẩm:** Bản thiết kế sơ đồ hoặc đoạn video ngắn/infographic học sinh nộp vào buổi học sau trên hệ thống LMS.
- **d) Tổ chức thực hiện:**
  - *Bước 1:* GV trình chiếu hình ảnh hốc cứu nạn thực tế trên đường bộ.
  - *Bước 2:* GV hướng dẫn gợi ý tiêu chí đánh giá (Rubric): Tính chính xác khoa học (5đ), Tính trực quan sáng tạo (3đ), Khả năng thuyết trình (2đ).
  - *Bước 3:* Học sinh ghi nhận nhiệm vụ về nhà làm theo nhóm 3-4 bạn.
  - *Bước 4:* GV tổng kết tiết học, dặn dò học sinh chuẩn bị bài mới.
"""

SAMPLE_SLIDES = [
    {
        "slide_number": 1,
        "title": "BÀI 26: CƠ NĂNG VÀ ĐỊNH LUẬT BẢO TOÀN CƠ NĂNG",
        "bullets": [
            "Môn: Vật lí 10 - Bộ sách Kết nối tri thức với cuộc sống",
            "Thời lượng: 2 tiết (90 phút)",
            "Câu hỏi khởi động: Điều gì giúp tàu lượn siêu tốc lao vun vút dù không có động cơ gắn trên từng toa?",
            "Giáo viên hướng dẫn: Thầy/Cô Bộ môn Vật lí"
        ],
        "visual_prompt": "Hình ảnh cận cảnh đoàn tàu lượn siêu tốc đang lao dốc ngoạn mục từ đỉnh cao xuống lòng máng ray uốn lượn, bầu trời xanh trong sáng.",
        "speaker_notes": "Chào các em học sinh! Hôm nay chúng ta sẽ giải mã bí mật đằng sau những trò chơi cảm giác mạnh ngoạn mục nhất hành tinh thông qua một trong những định luật nền tảng nhất của vật lí: Định luật bảo toàn cơ năng."
    },
    {
        "slide_number": 2,
        "title": "MỤC TIÊU BÀI HỌC CẦN ĐẠT",
        "bullets": [
            "Hiểu bản chất cơ năng là tổng hòa của động năng và thế năng",
            "Nắm vững công thức: W = Wđ + Wt = 1/2.m.v² + m.g.z",
            "Khắc sâu định luật: Cơ năng bảo toàn khi vật chỉ chịu lực thế (trọng lực)",
            "Phân tích ứng dụng: Tàu lượn, đập thủy điện, hốc lánh nạn đường đèo"
        ],
        "visual_prompt": "Infographic hiện đại với 4 biểu tượng mục tiêu: Khối óc tư duy (Kiến thức), Bánh răng thực hành (Năng lực), Trái tim nhiệt huyết (Phẩm chất) và Ứng dụng thực tiễn.",
        "speaker_notes": "Sau 90 phút hôm nay, các em không chỉ viết đúng công thức tính cơ năng mà còn có thể tự tay phân tích xem tại sao một công trình tàu lượn lại đảm bảo an toàn tuyệt đối cho hành khách."
    },
    {
        "slide_number": 3,
        "title": "1. KHÁI NIỆM CƠ NĂNG TRONG TRỌNG TRƯỜNG",
        "bullets": [
            "Khi vật chuyển động ở độ cao z, vật sở hữu đồng thời 2 dạng năng lượng:",
            "• Động năng (chuyển động): Wđ = 1/2.m.v²",
            "• Thế năng trọng trường (vị trí): Wt = m.g.z",
            "Cơ năng W = Wđ + Wt = 1/2.m.v² + m.g.z (Đơn vị: Jun - J)"
        ],
        "visual_prompt": "Sơ đồ vector một vật thể bay lượn trong không gian, mũi tên vận tốc màu cam v và độ cao z đo từ mặt đất chuẩn mốc thế năng.",
        "speaker_notes": "Lưu ý quan trọng: Vì thế năng phụ thuộc vào việc chọn mốc thế năng z=0, nên cơ năng cũng phụ thuộc vào gốc tọa độ mà chúng ta quy ước ban đầu."
    },
    {
        "slide_number": 4,
        "title": "2. SỰ CHUYỂN HÓA ĐỘNG NĂNG - THẾ NĂNG",
        "bullets": [
            "Khi vật rơi tự do: Độ cao giảm dần ➔ Thế năng giảm; Vận tốc tăng dần ➔ Động năng tăng",
            "Khi vật ném lên cao: Độ cao tăng ➔ Thế năng tăng; Vận tốc giảm dần ➔ Động năng giảm",
            "Động năng và Thế năng chuyển hóa liên tục và bù trừ lẫn nhau",
            "Câu hỏi: Tổng năng lượng cơ học có bị hao hụt trong điều kiện lý tưởng không?"
        ],
        "visual_prompt": "Đồ thị 2 đường cong đối xứng: Một đường đỏ biểu diễn Động năng đi lên, đường xanh biểu diễn Thế năng đi xuống, tổng của chúng là đường nằm ngang màu vàng rực rỡ.",
        "speaker_notes": "Các em quan sát biểu đồ trên màn hình: Khi thế năng tụt dốc bao nhiêu thì động năng vọt lên bấy nhiêu. Sự bù trừ này diễn ra vô cùng nhịp nhàng."
    },
    {
        "slide_number": 5,
        "title": "3. ĐỊNH LUẬT BẢO TOÀN CƠ NĂNG",
        "bullets": [
            "Phát biểu: Khi một vật chỉ chịu tác dụng của trọng lực, cơ năng của vật là một đại lượng bảo toàn",
            "Hệ thức toán học:",
            "  W₁ = W₂  <=>  1/2.m.v₁² + m.g.z₁ = 1/2.m.v₂² + m.g.z₂ = const",
            "Ý nghĩa: Thế năng cực đại tại đỉnh = Động năng cực đại tại gốc tọa độ"
        ],
        "visual_prompt": "Hình hộp định lý nổi bật viền xanh neon, bên trong in rõ nét hệ thức bảo toàn cơ năng mạ vàng kim sang trọng.",
        "speaker_notes": "Thầy cô xin nhấn mạnh 8 chữ vàng điều kiện áp dụng: 'CHỈ CHỊU TÁC DỤNG CỦA TRỌNG LỰC'. Nếu có lực ma sát hoặc lực kéo từ động cơ, định luật sẽ cần điều chỉnh sang định lí biến thiên cơ năng."
    },
    {
        "slide_number": 6,
        "title": "4. MÔ PHỎNG THỰC NGHIỆM ẢO PHET",
        "bullets": [
            "Phần mềm: Energy Skate Park (Đại học Colorado)",
            "Khảo sát vận động viên trượt ván trên máng ray hình chữ U:",
            "• Tại mép trên cùng: Tốc độ bằng 0 ➔ Thế năng chiếm 100%",
            "• Tại đáy lòng máng: Tốc độ lớn nhất ➔ Động năng chiếm 100%",
            "• Cột tổng năng lượng (Total Energy Bar) không hề thay đổi chiều cao!"
        ],
        "visual_prompt": "Giao diện mô phỏng 3D PhET Skate Park với cậu bé trượt ván trên ray parabol và bảng biểu đồ cột năng lượng xanh - đỏ - vàng hiển thị trực quan.",
        "speaker_notes": "Bây giờ thầy cô sẽ mở mô phỏng PhET trực tiếp. Các em hãy chú ý cột màu vàng ở ngoài cùng bên phải. Dù cậu bé lượn qua lượn lại, đỉnh cột vàng hoàn toàn bất biến!"
    },
    {
        "slide_number": 7,
        "title": "5. TRƯỜNG HỢP CÓ LỰC MA SÁT / LỰC CẢN",
        "bullets": [
            "Trong thực tế luôn tồn tại lực ma sát và lực cản của môi trường",
            "Cơ năng lúc sau luôn nhỏ hơn cơ năng lúc đầu (W₂ < W₁)",
            "Độ biến thiên cơ năng bằng công của lực không thế:",
            "  ΔW = W₂ - W₁ = A_Fms (A_Fms luôn âm)",
            "Phần cơ năng hao hụt đã biến đổi thành nhiệt năng làm nóng bề mặt tiếp xúc"
        ],
        "visual_prompt": "Hình ảnh bánh xe kim loại cọ sát ray tàu lượn phát ra tia lửa li ti, minh họa sự chuyển hóa cơ năng thành nhiệt năng.",
        "speaker_notes": "Tại sao con lắc đồng hồ để lâu lại dừng lại? Chính vì lực cản không khí đã sinh công âm, làm cơ năng vơi cạn dần và biến thành nhiệt."
    },
    {
        "slide_number": 8,
        "title": "6. QUY TRÌNH 4 BƯỚC GIẢI BÀI TOÁN BẢO TOÀN CƠ NĂNG",
        "bullets": [
            "Bước 1: Chọn mốc tính thế năng (thường chọn tại mặt đất hoặc điểm thấp nhất)",
            "Bước 2: Xác định trạng thái 1 (z₁, v₁) ➔ Viết biểu thức W₁",
            "Bước 3: Xác định trạng thái 2 (z₂, v₂) ➔ Viết biểu thức W₂",
            "Bước 4: Thiết lập phương trình W₁ = W₂ và giải tìm ẩn số (v₂ hoặc z₂)"
        ],
        "visual_prompt": "Sơ đồ dòng chảy quy trình (Flowchart) 4 bước có màu sắc chuyển tiếp Gradient từ Xanh lam đậm sang Xanh ngọc lam mượt mà.",
        "speaker_notes": "Hãy khắc ghi 4 bước thần thánh này vào sổ tay. 90% lỗi sai của học sinh là quên ghi rõ 'Chọn mốc tính thế năng ở đâu', dẫn tới tính sai dấu của z."
    },
    {
        "slide_number": 9,
        "title": "7. LUYỆN TẬP TƯƠNG TÁC TẠI LỚP",
        "bullets": [
            "Bài toán: Thả vật m = 500g từ độ cao h = 45m. Lấy g = 10 m/s². Bỏ qua ma sát.",
            "Câu hỏi 1: Tính vận tốc của vật khi vừa chạm mặt đất?",
            "Câu hỏi 2: Ở độ cao nào thì Động năng gấp 3 lần Thế năng?",
            "Thời gian thử thách: 5 phút tính toán và xung phong nhận điểm thưởng!"
        ],
        "visual_prompt": "Bảng đồng hồ đếm ngược phong cách hiện đại cùng hình ảnh minh họa bài toán ném thả vật lí với các mốc gợi ý công thức.",
        "speaker_notes": "5 phút bắt đầu! Các em hãy nhớ đổi đơn vị khối lượng sang kg nếu cần tính công, nhưng ở bài toán này vận tốc chạm đất v = căn(2gh) không hề phụ thuộc khối lượng m!"
    },
    {
        "slide_number": 10,
        "title": "8. TỔNG KẾT & DẶN DÒ VỀ NHÀ",
        "bullets": [
            "Trọng tâm ghi nhớ: W = 1/2.m.v² + m.g.z = hằng số (khi chỉ có trọng lực)",
            "Ứng dụng thực tiễn: Giải thích thiết kế 'Hốc lánh nạn hãm phanh xe khách'",
            "Nhiệm vụ về nhà:",
            "  1. Hoàn thành bài tập 1, 2, 3 trang 105 SGK",
            "  2. Đăng nhập LMS làm bài kiểm tra trắc nghiệm 10 câu",
            "  3. Chuẩn bị bài tiếp theo: Động lượng và định luật bảo toàn động lượng"
        ],
        "visual_prompt": "Biểu tượng cuốn sách mở ra kết nối với các ứng dụng công nghệ thực tế, cùng mã QR liên kết bài tập LMS của lớp.",
        "speaker_notes": "Tiết học của chúng ta hôm nay kết thúc tại đây. Thầy cô cảm ơn sự tương tác sôi nổi của các nhóm. Chúc các em vận dụng thật tốt định luật này vào đời sống!"
    }
]

SAMPLE_EXAM_MATRIX = """# MA TRẬN ĐỀ KIỂM TRA ĐỊNH KÌ THEO CÔNG VĂN 7991/BGDĐT-GDTrH

**Môn:** Vật lí 10 | **Thời gian làm bài:** 45 phút  
**Khung cấu trúc:** Tỉ lệ nhận thức Biết 40% - Hiểu 30% - Vận dụng 30%.  
**Tỉ lệ hình thức:** TNKQ 4 lựa chọn (3,0 đ) + TNKQ Đúng-Sai (2,0 đ) + TNKQ Trả lời ngắn (2,0 đ) + Tự luận (3,0 đ).

| TT | Chủ đề / Đơn vị kiến thức | Mức độ: Nhận biết (40%) | Mức độ: Thông hiểu (30%) | Mức độ: Vận dụng (30%) | Tổng số câu | Tổng điểm |
|:---|:---|:---:|:---:|:---:|:---:|:---:|
| **I** | **Cơ năng & ĐL bảo toàn cơ năng** | | | | | |
| 1 | Khái niệm & Công thức cơ năng | 4 câu TN (Phần I) | 2 câu TN (Phần I) | | 6 câu | 1,5 đ |
| 2 | Sự chuyển hóa Wđ và Wt | 2 câu TN (Phần I) | 1 lệnh Đ/S (Phần II) | 1 lệnh Đ/S (Phần II) | 2 lệnh Đ/S + 2 TN | 1,5 đ |
| 3 | Định luật bảo toàn cơ năng | | 1 lệnh Đ/S (Phần II) | 1 lệnh Đ/S (Phần II) | 2 lệnh Đ/S | 1,0 đ |
| 4 | Bài toán định lượng bảo toàn cơ năng | | | 2 câu TL ngắn (Phần III) | 2 câu TLN | 1,0 đ |
| 5 | Chuyển động có ma sát & Ứng dụng thực tiễn | | | 2 câu TL ngắn (Phần III) | 2 câu TLN | 1,0 đ |
| 6 | Bài toán tự luận tổng hợp liên hệ thực tế | | 1 ý TL (1,0 đ) | 2 ý TL (2,0 đ) | 1 bài TL | 3,0 đ |
| | **TỔNG CỘNG** | **4,0 điểm (40%)** | **3,0 điểm (30%)** | **3,0 điểm (30%)** | **19 câu hỏi** | **10,0 điểm** |
"""

SAMPLE_EXAM_SPEC = """# BẢN ĐẶC TẢ ĐỀ KIỂM TRA ĐỊNH KÌ (CHUẨN CÔNG VĂN 7991/BGDĐT-GDTrH)

| TT | Chủ đề / Mạch kiến thức | Đơn vị kiến thức | Mức độ đánh giá / Yêu cầu cần đạt | Số lượng câu hỏi theo mức độ | Mã hóa năng lực |
|:---|:---|:---|:---|:---:|:---:|
| 1 | Năng lượng, công, cơ năng | Khái niệm cơ năng | **Nhận biết:** Nêu được định nghĩa cơ năng của vật trong trọng trường; viết được công thức $W = W_đ + W_t$; nhận biết đơn vị Jun (J). | 4 TN (C1-C4) | NL_VL 1.1 |
| 2 | Năng lượng, công, cơ năng | Chuyển hóa động năng - thế năng | **Thông hiểu:** Mô tả được sự chuyển hóa giữa động năng và thế năng trong chuyển động ném, rơi tự do hoặc dao động con lắc. | 2 TN (C5, C6) | NL_VL 1.2 |
| 3 | Năng lượng, công, cơ năng | Định luật bảo toàn cơ năng | **Thông hiểu & Vận dụng:** Phân tích đúng/sai các mệnh đề về điều kiện bảo toàn cơ năng và sự thay đổi cơ năng khi có lực ma sát cản trở. | 2 câu Đúng-Sai (Mỗi câu 4 ý a,b,c,d) | NL_VL 2.1 |
| 4 | Năng lượng, công, cơ năng | Tính toán cơ năng định lượng | **Vận dụng cấp độ 1:** Tính được vận tốc chạm đất, độ cao cực đại hoặc tỉ số giữa động năng và thế năng tại một vị trí xác định. | 4 câu Trả lời ngắn (C1-C4) | NL_VL 2.2 |
| 5 | Năng lượng, công, cơ năng | Giải quyết vấn đề thực tiễn | **Vận dụng cao:** Thiết lập mô hình toán học giải quyết bài toán tàu lượn siêu tốc hoặc xe mất phanh vào làn lánh nạn dốc có ma sát. | 1 bài Tự luận (3 ý a, b, c) | NL_VL 3.1 |
"""

SAMPLE_EXAM_QUESTIONS = """# ĐỀ KIỂM TRA ĐỊNH KÌ MÔN VẬT LÍ LỚP 10
**Năm học: 2024 - 2025 | Thời gian làm bài: 45 phút**  
*(Đề kiểm tra tuân thủ cấu trúc định dạng chuẩn Công văn 7991/BGDĐT-GDTrH)*

---

### PHẦN I. CÂU HỎI TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (3,0 điểm)
*Thí sinh trả lời từ Câu 1 đến Câu 12. Mỗi câu hỏi chỉ chọn một phương án đúng. Mỗi câu đúng được 0,25 điểm.*

**Câu 1.** Cơ năng của một vật chuyển động trong trọng trường được xác định bởi công thức nào sau đây?  
A. $W = W_đ - W_t$  
B. $W = W_đ + W_t$  
C. $W = W_đ \\times W_t$  
D. $W = \\frac{W_đ}{W_t}$  

**Câu 2.** Đơn vị đo của cơ năng trong hệ SI là  
A. Oát (W).  
B. Niu-tơn (N).  
C. Jun (J).  
D. Mét trên giây (m/s).  

**Câu 3.** Một vật khối lượng $m$ đang ở độ cao $z$ so với mốc thế năng và chuyển động với vận tốc $v$. Biểu thức cơ năng của vật là  
A. $W = mv^2 + mgz$.  
B. $W = \\frac{1}{2}mv + mgz$.  
C. $W = \\frac{1}{2}mv^2 + mgz$.  
D. $W = \\frac{1}{2}mv^2 - mgz$.  

**Câu 4.** Cơ năng của vật được bảo toàn trong trường hợp nào sau đây?  
A. Vật trượt có ma sát trên mặt phẳng nghiêng.  
B. Vật rơi trong không khí có lực cản đáng kể.  
C. Vật chuyển động trong trọng trường chỉ chịu tác dụng của trọng lực.  
D. Đoàn tàu đang tăng tốc nhờ lực kéo của đầu máy.  

**Câu 5.** Một vật được ném thẳng đứng từ dưới lên cao. Trong quá trình vật bay lên (bỏ qua sức cản không khí) thì  
A. động năng tăng, thế năng giảm.  
B. động năng giảm, thế năng tăng.  
C. cả động năng và thế năng đều tăng.  
D. cả động năng và thế năng đều giảm.  

**Câu 6.** Một con lắc đơn dao động điều hòa. Tại vị trí cân bằng (chọn làm mốc thế năng) thì  
A. thế năng đạt cực đại, động năng bằng không.  
B. động năng đạt cực đại, thế năng bằng không.  
C. cơ năng bằng không.  
D. động năng bằng một nửa thế năng.  

---

### PHẦN II. CÂU HỎI TRẮC NGHIỆM ĐÚNG - SAI (2,0 điểm)
*Thí sinh trả lời từ Câu 1 đến Câu 2. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn Đúng (Đ) hoặc Sai (S).*  
*Quy tắc tính điểm chuẩn CV 7991:*  
- Thí sinh chỉ lựa chọn chính xác 01 ý trong 01 câu hỏi được **0,10 điểm**;  
- Thí sinh chỉ lựa chọn chính xác 02 ý trong 01 câu hỏi được **0,25 điểm**;  
- Thí sinh chỉ lựa chọn chính xác 03 ý trong 01 câu hỏi được **0,50 điểm**;  
- Thí sinh lựa chọn chính xác cả 04 ý trong 01 câu hỏi được **1,00 điểm**.  

**Câu 1.** Xét một vật nhỏ có khối lượng $m = 200\\text{ g}$ được thả rơi tự do không vận tốc ban đầu từ độ cao $h = 45\\text{ m}$ so với mặt đất. Lấy $g = 10\\text{ m/s}^2$, chọn mốc thế năng tại mặt đất và bỏ qua mọi lực cản của không khí.  
a) Cơ năng ban đầu của vật khi bắt đầu thả có giá trị bằng $90\\text{ J}$.  
b) Trong quá trình rơi, cơ năng của vật luôn biến thiên theo thời gian vì vận tốc tăng dần.  
c) Ngay trước khi chạm đất, vận tốc của vật đạt độ lớn là $30\\text{ m/s}$.  
d) Tại độ cao $z = 15\\text{ m}$, động năng của vật có giá trị gấp 2 lần thế năng trọng trường của nó.  

**Câu 2.** Một xe trượt khối lượng $m$ trượt từ đỉnh dốc cao $h = 5\\text{ m}$ xuống chân dốc. Lấy $g = 9{,}8\\text{ m/s}^2$.  
a) Nếu bỏ qua ma sát giữa xe và mặt dốc thì vận tốc xe ở chân dốc là $v = \\sqrt{2gh} \\approx 9{,}9\\text{ m/s}$.  
b) Nếu có ma sát, độ biến thiên cơ năng của xe trượt bằng công của trọng lực tác dụng lên xe.  
c) Thực tế đo được vận tốc xe ở chân dốc là $8\\text{ m/s}$, điều này chứng tỏ cơ năng đã bị hao hụt một lượng nhiệt năng do ma sát.  
d) Góc nghiêng của mặt dốc càng lớn thì vận tốc ở chân dốc khi không có ma sát sẽ càng lớn.  

---

### PHẦN III. CÂU HỎI TRẮC NGHIỆM TRẢ LỜI NGẮN (2,0 điểm)
*Thí sinh trả lời từ Câu 1 đến Câu 4. Mỗi câu trả lời đúng được 0,50 điểm. Thí sinh chỉ điền giá trị số kèm đơn vị.*

**Câu 1.** Thả một hòn đá có khối lượng $400\\text{ g}$ rơi tự do từ độ cao $20\\text{ m}$ xuống đất. Lấy $g = 10\\text{ m/s}^2$, chọn mốc thế năng tại mặt đất. Tính cơ năng của hòn đá theo đơn vị Jun (J).  
*(Điền kết quả: ...)*  

**Câu 2.** Một vật được ném thẳng đứng lên cao từ mặt đất với vận tốc ban đầu $v_0 = 12\\text{ m/s}$. Bỏ qua sức cản không khí, lấy $g = 10\\text{ m/s}^2$. Tính độ cao cực đại mà vật đạt được theo đơn vị mét (m).  
*(Điền kết quả: ...)*  

**Câu 3.** Một quả bóng đang chuyển động trên mặt sàn nằm ngang không ma sát với động năng $W_đ = 50\\text{ J}$. Sau đó quả bóng đi lên một dốc nghiêng. Tại độ cao mà thế năng của bóng là $W_t = 20\\text{ J}$ thì động năng của bóng còn lại bao nhiêu Jun (J)?  
*(Điền kết quả: ...)*  

**Câu 4.** Một toa tàu lượn khối lượng $1000\\text{ kg}$ bắt đầu trượt không vận tốc đầu từ đỉnh ray cao $40\\text{ m}$. Khi xuống đến chân ray ngang, do ma sát nên vận tốc thực tế của tàu chỉ đạt $20\\text{ m/s}$. Lấy $g = 10\\text{ m/s}^2$. Nhiệt lượng tỏa ra do ma sát trên cung ray đó là bao nhiêu kilo-Jun (kJ)?  
*(Điền kết quả: ...)*  

---

### PHẦN IV. CÂU HỎI TỰ LUẬN (3,0 điểm)
*Thí sinh trình bày chi tiết các bước giải bài toán sau:*

**Bài toán (3,0 điểm):**  
Một ô tô chở khách có khối lượng toàn bộ $M = 2000\\text{ kg}$ đang di chuyển xuống đèo dốc thì bị mất phanh tại vị trí $A$ có độ cao $z_A = 30\\text{ m}$ so với chân dốc $B$, với vận tốc tại $A$ là $v_A = 10\\text{ m/s}$. Ngay tại chân dốc $B$, tài xế khẩn cấp bẻ lái cho xe tiến vào một “hốc lánh nạn” dốc ngược lên có góc nghiêng $\\alpha = 30^\\circ$ so với phương ngang, mặt dốc phủ cát sỏi có hệ số ma sát $\\mu = 0{,}2$. Lấy $g = 10\\text{ m/s}^2$.  
1. *(1,0 điểm)* Bỏ qua ma sát trên đoạn đường đèo từ $A$ xuống $B$. Hãy áp dụng định luật bảo toàn cơ năng để tính vận tốc $v_B$ của xe ô tô khi vừa tới chân dốc $B$.  
2. *(1,0 điểm)* Tính công của lực ma sát tác dụng lên xe trên đoạn đường hốc lánh nạn khi xe đi được quãng đường $s$ trên dốc cát.  
3. *(1,0 điểm)* Áp dụng định lí biến thiên cơ năng, hãy tính chiều dài quãng đường tối đa $s_{max}$ mà xe trượt lên được trên dốc cát trước khi dừng lại hẳn, đảm bảo cứu hộ an toàn.
"""

SAMPLE_EXAM_ANSWERS = """# HƯỚNG DẪN CHẤM VÀ ĐÁP ÁN ĐỀ KIỂM TRA ĐỊNH KÌ

---

### PHẦN I. TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (3,0 điểm)
*Mỗi câu đúng: 0,25 điểm.*

| Câu hỏi | Đáp án đúng | Ghi chú hướng dẫn |
|:---:|:---:|:---|
| 1 | **B** | Định nghĩa cơ năng $W = W_đ + W_t$ |
| 2 | **C** | Năng lượng có đơn vị chuẩn là Jun (J) |
| 3 | **C** | $W = \\frac{1}{2}mv^2 + mgz$ |
| 4 | **C** | Điều kiện bảo toàn: chỉ chịu tác dụng của trọng lực |
| 5 | **B** | Ném lên: $v$ giảm nên $W_đ$ giảm, độ cao tăng nên $W_t$ tăng |
| 6 | **B** | Vị trí cân bằng là vị trí thấp nhất: $z=0 \\Rightarrow W_t=0$, vận tốc cực đại $\\Rightarrow W_đ$ max |

---

### PHẦN II. TRẮC NGHIỆM ĐÚNG - SAI (2,0 điểm)
*Thang điểm CV 7991: 1 ý đúng = 0,10đ; 2 ý đúng = 0,25đ; 3 ý đúng = 0,50đ; 4 ý đúng = 1,00đ.*

#### Câu 1:
- a) **ĐÚNG**. $W = mgh = 0{,}2 \\times 10 \\times 45 = 90\\text{ J}$.
- b) **SAI**. Vì bỏ qua sức cản không khí, vật chỉ chịu trọng lực nên cơ năng được bảo toàn (không đổi).
- c) **ĐÚNG**. $v = \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 45} = \\sqrt{900} = 30\\text{ m/s}$.
- d) **ĐÚNG**. Tại $z = 15\\text{ m}$: $W_t = 0{,}2 \\times 10 \\times 15 = 30\\text{ J}$. Khi đó $W_đ = W - W_t = 90 - 30 = 60\\text{ J} = 2 W_t$.

#### Câu 2:
- a) **ĐÚNG**. Khi không ma sát: $\\frac{1}{2}mv^2 = mgh \\Rightarrow v = \\sqrt{2 \\times 9{,}8 \\times 5} \\approx 9{,}9\\text{ m/s}$.
- b) **SAI**. Độ biến thiên cơ năng bằng công của lực ma sát (lực không thế), không phải công trọng lực.
- c) **ĐÚNG**. Vận tốc thực tế nhỏ hơn lí thuyết chứng tỏ một phần cơ năng đã chuyển thành nhiệt năng.
- d) **SAI**. $v = \\sqrt{2gh}$ chỉ phụ thuộc độ cao $h$, không phụ thuộc góc nghiêng khi bỏ qua ma sát.

---

### PHẦN III. TRẮC NGHIỆM TRẢ LỜI NGẮN (2,0 điểm)
*Mỗi câu đúng: 0,50 điểm.*

| Câu | Giá trị đáp số | Đơn vị | Hướng dẫn giải tóm tắt |
|:---:|:---:|:---:|:---|
| 1 | **80** | J | $W = mgh = 0{,}4 \\times 10 \\times 20 = 80\\text{ J}$ |
| 2 | **7,2** *(hoặc 7.2)* | m | Bảo toàn cơ năng: $\\frac{1}{2}mv_0^2 = mgh_{max} \\Rightarrow h_{max} = \\frac{v_0^2}{2g} = \\frac{144}{20} = 7{,}2\\text{ m}$ |
| 3 | **30** | J | Bảo toàn cơ năng trên dốc: $W_đ + W_t = W_{ban đầu} = 50 \\Rightarrow W_đ = 50 - 20 = 30\\text{ J}$ |
| 4 | **200** | kJ | $W_1 = mgh = 1000 \\times 10 \\times 40 = 400\\text{ kJ}$; $W_2 = \\frac{1}{2}mv^2 = \\frac{1}{2} \\times 1000 \\times 20^2 = 200\\text{ kJ}$. Nhiệt lượng $Q = W_1 - W_2 = 200\\text{ kJ}$. |

---

### PHẦN IV. CÂU HỎI TỰ LUẬN (3,0 điểm)

| Ý | Nội dung yêu cầu và lời giải chi tiết | Điểm |
|:---:|:---|:---:|
| **1** | Chọn gốc thế năng tại chân dốc $B$ ($z_B = 0$).<br>• Cơ năng của ô tô tại vị trí $A$:<br>$W_A = \\frac{1}{2} M v_A^2 + M g z_A = \\frac{1}{2} \\times 2000 \\times 10^2 + 2000 \\times 10 \\times 30 = 100\\,000 + 600\\,000 = 700\\,000\\text{ J}$.<br>• Cơ năng của ô tô tại vị trí $B$: $W_B = \\frac{1}{2} M v_B^2$.<br>• Áp dụng ĐL bảo toàn cơ năng trên đoạn $AB$ (bỏ qua ma sát): $W_B = W_A$<br>$\\Leftrightarrow \\frac{1}{2} \\times 2000 \\times v_B^2 = 700\\,000 \\Rightarrow v_B^2 = 700 \\Rightarrow v_B = 10\\sqrt{7} \\approx 26{,}46\\text{ m/s}$. | **1,0 đ** |
| **2** | Xét xe chuyển động lên dốc nghiêng $\\alpha = 30^\\circ$:<br>• Phản lực pháp tuyến: $N = M g \\cos \\alpha$.<br>• Lực ma sát trượt: $F_{ms} = \\mu N = \\mu M g \\cos \\alpha$.<br>• Công của lực ma sát trên quãng đường $s$:<br>$A_{ms} = - F_{ms} \\cdot s = - \\mu M g \\cos \\alpha \\cdot s = - 0{,}2 \\times 2000 \\times 10 \\times \\cos 30^\\circ \\times s = - 4000 \\frac{\\sqrt{3}}{2} s \\approx - 3464{,}1 s\\text{ (J)}$. | **1,0 đ** |
| **3** | Khi xe dừng lại ở điểm cao nhất trên dốc cát (vị trí $C$):<br>• Độ cao tại $C$: $z_C = s_{max} \\cdot \\sin \\alpha = s_{max} \\cdot \\sin 30^\\circ = 0{,}5 s_{max}$.<br>• Vận tốc tại $C$: $v_C = 0$. Cơ năng tại $C$: $W_C = M g z_C = 2000 \\times 10 \\times (0{,}5 s_{max}) = 10\\,000 s_{max}$.<br>• Áp dụng định lí biến thiên cơ năng từ $B$ đến $C$:<br>$W_C - W_B = A_{ms}$<br>$\\Leftrightarrow 10\\,000 s_{max} - 700\\,000 = - 3464{,}1 s_{max}$<br>$\\Leftrightarrow 13\\,464{,}1 s_{max} = 700\\,000 \\Rightarrow s_{max} \\approx 51{,}99\\text{ m} \\approx 52\\text{ m}$.<br>• **Kết luận:** Chiều dài tối thiểu của hốc lánh nạn cần thiết kế là khoảng $52\\text{ m}$ để xe dừng lại an toàn. | **1,0 đ** |
"""
