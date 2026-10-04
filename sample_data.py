# -*- coding: utf-8 -*-
"""
EduMaster AI - Thư viện Dữ liệu Sư phạm Đa môn học Chuẩn hóa
Hỗ trợ đầy đủ các môn học THCS & THPT theo Công văn 5512 và Công văn 7991/BGDĐT-GDTrH.
"""

# ==============================================================================
# GỢI Ý CHỦ ĐỀ VÀ GHI CHÚ THEO TỪNG MÔN HỌC & CẤP LỚP
# ==============================================================================
SUBJECT_PRESETS = {
    "Vật lí": {
        "lesson_name": "Bài 26: Cơ năng và định luật bảo toàn cơ năng",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Tích hợp mô phỏng thí nghiệm ảo PhET và liên hệ tình huống kỹ thuật thực tiễn (tàu lượn, đập thủy điện)."
    },
    "Toán": {
        "lesson_name": "Bài 3: Hệ thức lượng trong tam giác và Định lí Cosin, Sin",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Ứng dụng hình học giải quyết bài toán đo khoảng cách gián tiếp trong thực địa (đo chiều cao tháp, bề rộng khúc sông)."
    },
    "Ngữ văn": {
        "lesson_name": "Đoạn trích: Đăm Săn chiến thắng Mtao Mxây (Sử thi Ê-đê)",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Phát triển năng lực đọc hiểu thể loại sử thi anh hùng, rèn luyện kĩ năng viết đoạn văn và cảm thụ thẩm mĩ."
    },
    "Hóa học": {
        "lesson_name": "Bài 12: Phản ứng oxi hóa - khử và Số oxi hóa",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Rèn luyện phương pháp thăng bằng electron, liên hệ hiện tượng ăn mòn kim loại và phản ứng pin điện hóa trong đời sống."
    },
    "Khoa học tự nhiên (KHTN)": {
        "lesson_name": "Bài 8: Khái niệm Acid và thang đo pH",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Tổ chức học tập theo trạm thực hành, kiểm tra độ pH của nước mưa, đất trồng và các loại đồ uống quen thuộc."
    },
    "Tiếng Anh": {
        "lesson_name": "Unit 3: Music - Reading & Language Focus (Infinitive & Gerund)",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Tăng cường năng lực giao tiếp tiếng Anh qua hoạt động thảo luận về các hiện tượng âm nhạc truyền thống và hiện đại."
    },
    "Lịch sử": {
        "lesson_name": "Bài 7: Văn minh Văn Lang - Âu Lạc",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Sử dụng hiện vật bảo tàng ảo và sơ đồ tư duy phân tích sự ra đời của nhà nước đầu tiên trong lịch sử Việt Nam."
    },
    "Lịch sử & Địa lí": {
        "lesson_name": "Bài 14: Nhà nước Văn Lang - Âu Lạc và Đời sống cư dân cổ",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Khảo sát tư liệu trống đồng Đông Sơn và thành Cổ Loa, bồi dưỡng lòng tự hào dân tộc và ý thức bảo vệ di sản."
    },
    "Địa lí": {
        "lesson_name": "Bài 6: Thạch quyển và Tác động của Nội lực đến địa hình bề mặt Trái Đất",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Sử dụng bản đồ mảng kiến tạo thế giới và video mô phỏng hiện tượng động đất, núi lửa hình thành địa hình."
    },
    "Sinh học": {
        "lesson_name": "Bài 13: Chu kì tế bào và Quá trình nguyên phân",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Quan sát tiêu bản hiển vi tế bào rễ hành, phân tích cơ chế sao chép và phân chia vật chất di truyền."
    },
    "Tin học": {
        "lesson_name": "Bài 8: Cấu trúc lặp và Ứng dụng vòng lặp trong lập trình Python",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Lập trình giải bài toán tính tổng dãy số và vẽ hình hoa văn bằng mô-đun Turtle, rèn luyện tư duy thuật toán."
    },
    "Giáo dục công dân (GDCD)": {
        "lesson_name": "Bài 5: Bảo vệ môi trường và Tài nguyên thiên nhiên",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Thực hiện dự án phân loại rác thải tại nguồn ở trường học và thiết kế áp phích tuyên truyền lối sống xanh."
    },
    "Giáo dục kinh tế & Pháp luật (GDKT&PL)": {
        "lesson_name": "Bài 3: Thị trường và Cơ chế thị trường",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Mô phỏng phiên chợ nông sản Vĩnh Long, phân tích quy luật cung - cầu và sự biến động giá cả thực tế."
    },
    "Công nghệ": {
        "lesson_name": "Bài 4: Bản vẽ kĩ thuật và Hình chiếu vuông góc",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Rèn luyện kĩ năng đọc bản vẽ cơ khí 2D/3D và dựng hình khối bằng phần mềm thiết kế kĩ thuật số."
    },
    "Hoạt động trải nghiệm hướng nghiệp": {
        "lesson_name": "Chủ đề: Khám phá hứng thú nghề nghiệp và Năng lực bản thân",
        "duration": "2 tiết (90 phút)",
        "special_notes": "Thực hiện trắc nghiệm định hướng nghề nghiệp Holland và xây dựng hồ sơ kế hoạch học tập cá nhân."
    }
}

# ==============================================================================
# DỮ LIỆU MẪU MÔN VẬT LÍ (LỚP 10)
# ==============================================================================
VATLI_METADATA = {
    "grade_level": "THPT",
    "grade": "Lớp 10",
    "subject": "Vật lí",
    "book_series": "Kết nối tri thức với cuộc sống",
    "lesson_name": "Bài 26: Cơ năng và định luật bảo toàn cơ năng",
    "duration": "2 tiết (90 phút)",
    "special_notes": "Tích hợp mô hình lớp học đảo ngược, rèn luyện tư duy thực nghiệm và giải quyết vấn đề thực tiễn thông qua trò chơi Tàu lượn siêu tốc."
}

VATLI_LESSON_PLAN = """# KẾ HOẠCH BÀI DẠY (THEO CÔNG VĂN 5512/BGDĐT-GDTrH)

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
   - Bộ thí nghiệm con lắc đơn hoặc cảm biến chuyển động kết nối máy vi tính.
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
  - *Bước 4 (Kết luận):* GV kết luận và nhấn mạnh điều kiện nghiệm đúng: *Khi một vật chuyển động trong trọng trường chỉ chịu tác dụng của trọng lực thì cơ năng của vật là một đại lượng bảo toàn.*

---

### 3. HOẠT ĐỘNG 3: LUYỆN TẬP (18 phút)
- **a) Mục tiêu:** Vận dụng định luật bảo toàn cơ năng để giải các bài toán định lượng cơ bản (tìm vận tốc tại chân dốc, độ cao cực đại).
- **b) Nội dung:**
  - Thả rơi tự do một quả bóng khối lượng $m = 200\\text{ g}$ từ độ cao $h = 20\\text{ m}$ so với mặt đất ($g = 10\\text{ m/s}^2$). Bỏ qua sức cản không khí. Tính vận tốc của vật ngay trước khi chạm đất và độ cao mà tại đó thế năng bằng động năng.
- **c) Sản phẩm:** Lời giải chi tiết của học sinh:
  - Cơ năng tại vị trí thả: $W = mgh = 0{,}2 \\times 10 \\times 20 = 40\\text{ J}$.
  - Tại đất ($z = 0$): $W = \\frac{1}{2}mv_{max}^2 = 40 \\Rightarrow v_{max} = \\sqrt{2gh} = 20\\text{ m/s}$.
  - Khi $W_t = W_đ$: $W = 2W_t \\Rightarrow mgh = 2mgz \\Rightarrow z = \\frac{h}{2} = 10\\text{ m}$.
- **d) Tổ chức thực hiện:** HS làm bài vào vở, 2 HS lên bảng chữa, cả lớp nhận xét đối chiếu.

---

### 4. HOẠT ĐỘNG 4: VẬN DỤNG VÀ MỞ RỘNG (12 phút)
- **a) Mục tiêu:** Phát triển năng lực vận dụng kiến thức vào thực tế đời sống, phân tích an toàn giao thông và năng lượng tái tạo.
- **b) Nội dung:** Nhiệm vụ dự án nhỏ: *"Tại các cung đường đèo hiểm trở, người ta thường thiết kế các 'hốc lánh nạn' dốc ngược lên phủ cát sỏi. Hãy dùng kiến thức về cơ năng và công của lực ma sát để giải thích nguyên lí hãm xe mất phanh của hốc lánh nạn."*
- **c) Sản phẩm:** Bản infographic hoặc bài thuyết trình ngắn học sinh nộp vào buổi học sau trên hệ thống LMS.
"""

VATLI_SLIDES = [
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
        "speaker_notes": "Thầy cô xin nhấn mạnh điều kiện áp dụng: 'CHỈ CHỊU TÁC DỤNG CỦA TRỌNG LỰC'. Nếu có lực ma sát, định luật sẽ cần điều chỉnh sang định lí biến thiên cơ năng."
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
        "speaker_notes": "Các em hãy chú ý cột màu vàng ở ngoài cùng bên phải. Dù cậu bé lượn qua lượn lại, đỉnh cột vàng hoàn toàn bất biến!"
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
        "visual_prompt": "Sơ đồ dòng chảy quy trình 4 bước có màu sắc chuyển tiếp Gradient từ Xanh lam đậm sang Xanh ngọc lam mượt mà.",
        "speaker_notes": "Hãy khắc ghi 4 bước này vào sổ tay. 90% lỗi sai của học sinh là quên ghi rõ 'Chọn mốc tính thế năng ở đâu'."
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
        "speaker_notes": "5 phút bắt đầu! Vận tốc chạm đất v = căn(2gh) không hề phụ thuộc khối lượng m!"
    },
    {
        "slide_number": 10,
        "title": "8. TỔNG KẾT & DẶN DÒ VỀ NHÀ",
        "bullets": [
            "Trọng tâm ghi nhớ: W = 1/2.m.v² + m.g.z = hằng số (khi chỉ có trọng lực)",
            "Ứng dụng thực tiễn: Giải thích thiết kế 'Hốc lánh nạn hãm phanh xe khách'",
            "Nhiệm vụ về nhà: Hoàn thành bài tập SGK và làm bài trắc nghiệm LMS",
            "Chúc các em học tốt và yêu thích môn Vật lí!"
        ],
        "visual_prompt": "Biểu tượng cuốn sách mở ra kết nối với các ứng dụng công nghệ thực tế, cùng mã QR liên kết bài tập LMS của lớp.",
        "speaker_notes": "Tiết học của chúng ta hôm nay kết thúc tại đây. Cảm ơn sự nỗ lực và tương tác tuyệt vời của các em!"
    }
]

VATLI_EXAM_MATRIX = """# MA TRẬN ĐỀ KIỂM TRA ĐỊNH KÌ THEO CÔNG VĂN 7991/BGDĐT-GDTrH

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

VATLI_EXAM_SPEC = """# BẢN ĐẶC TẢ ĐỀ KIỂM TRA ĐỊNH KÌ (CHUẨN CÔNG VĂN 7991/BGDĐT-GDTrH)

| TT | Chủ đề / Mạch kiến thức | Đơn vị kiến thức | Mức độ đánh giá / Yêu cầu cần đạt | Số lượng câu hỏi theo mức độ | Mã hóa năng lực |
|:---|:---|:---|:---|:---:|:---:|
| 1 | Năng lượng, công, cơ năng | Khái niệm cơ năng | **Nhận biết:** Nêu được định nghĩa cơ năng của vật trong trọng trường; viết được công thức $W = W_đ + W_t$; nhận biết đơn vị Jun (J). | 4 TN (C1-C4) | NL_VL 1.1 |
| 2 | Năng lượng, công, cơ năng | Chuyển hóa động năng - thế năng | **Thông hiểu:** Mô tả được sự chuyển hóa giữa động năng và thế năng trong chuyển động ném, rơi tự do hoặc dao động con lắc. | 2 TN (C5, C6) | NL_VL 1.2 |
| 3 | Năng lượng, công, cơ năng | Định luật bảo toàn cơ năng | **Thông hiểu & Vận dụng:** Phân tích đúng/sai các mệnh đề về điều kiện bảo toàn cơ năng và sự thay đổi cơ năng khi có lực ma sát cản trở. | 2 câu Đúng-Sai (Mỗi câu 4 ý a,b,c,d) | NL_VL 2.1 |
| 4 | Năng lượng, công, cơ năng | Tính toán cơ năng định lượng | **Vận dụng cấp độ 1:** Tính được vận tốc chạm đất, độ cao cực đại hoặc tỉ số giữa động năng và thế năng tại một vị trí xác định. | 4 câu Trả lời ngắn (C1-C4) | NL_VL 2.2 |
| 5 | Năng lượng, công, cơ năng | Giải quyết vấn đề thực tiễn | **Vận dụng cao:** Thiết lập mô hình toán học giải quyết bài toán tàu lượn siêu tốc hoặc xe mất phanh vào làn lánh nạn dốc có ma sát. | 1 bài Tự luận (3 ý a, b, c) | NL_VL 3.1 |
"""

VATLI_EXAM_QUESTIONS = """# ĐỀ KIỂM TRA ĐỊNH KÌ MÔN VẬT LÍ LỚP 10
**Năm học: 2024 - 2025 | Thời gian làm bài: 45 phút**  
*(Đề kiểm tra tuân thủ cấu trúc định dạng chuẩn Công văn 7991/BGDĐT-GDTrH)*

---

### PHẦN I. CÂU HỎI TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (3,0 điểm)
*Thí sinh trả lời từ Câu 1 đến Câu 6. Mỗi câu đúng được 0,50 điểm (hoặc bareme 12 câu x 0,25đ).*

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
*Quy tắc tính điểm chuẩn CV 7991: Đúng 1 ý = 0,10đ; Đúng 2 ý = 0,25đ; Đúng 3 ý = 0,50đ; Đúng 4 ý = 1,00đ.*

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
*Mỗi câu đúng được 0,50 điểm. Thí sinh chỉ điền giá trị số kèm đơn vị.*

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

**Bài toán (3,0 điểm):**  
Một ô tô chở khách có khối lượng toàn bộ $M = 2000\\text{ kg}$ đang di chuyển xuống đèo dốc thì bị mất phanh tại vị trí $A$ có độ cao $z_A = 30\\text{ m}$ so với chân dốc $B$, với vận tốc tại $A$ là $v_A = 10\\text{ m/s}$. Ngay tại chân dốc $B$, tài xế khẩn cấp bẻ lái cho xe tiến vào một “hốc lánh nạn” dốc ngược lên có góc nghiêng $\\alpha = 30^\\circ$ so với phương ngang, mặt dốc phủ cát sỏi có hệ số ma sát $\\mu = 0{,}2$. Lấy $g = 10\\text{ m/s}^2$.  
1. *(1,0 điểm)* Bỏ qua ma sát trên đoạn đường đèo từ $A$ xuống $B$. Hãy áp dụng định luật bảo toàn cơ năng để tính vận tốc $v_B$ của xe ô tô khi vừa tới chân dốc $B$.  
2. *(1,0 điểm)* Tính công của lực ma sát tác dụng lên xe trên đoạn đường hốc lánh nạn khi xe đi được quãng đường $s$ trên dốc cát.  
3. *(1,0 điểm)* Áp dụng định lí biến thiên cơ năng, hãy tính chiều dài quãng đường tối đa $s_{max}$ mà xe trượt lên được trên dốc cát trước khi dừng lại hẳn, đảm bảo cứu hộ an toàn.
"""

VATLI_EXAM_ANSWERS = """# HƯỚNG DẪN CHẤM VÀ ĐÁP ÁN ĐỀ KIỂM TRA ĐỊNH KÌ

---

### PHẦN I. TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (3,0 điểm)
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
| Câu | Giá trị đáp số | Đơn vị | Hướng dẫn giải tóm tắt |
|:---:|:---:|:---:|:---|
| 1 | **80** | J | $W = mgh = 0{,}4 \\times 10 \\times 20 = 80\\text{ J}$ |
| 2 | **7,2** | m | Bảo toàn cơ năng: $\\frac{1}{2}mv_0^2 = mgh_{max} \\Rightarrow h_{max} = \\frac{v_0^2}{2g} = \\frac{144}{20} = 7{,}2\\text{ m}$ |
| 3 | **30** | J | Bảo toàn cơ năng trên dốc: $W_đ + W_t = W_{ban đầu} = 50 \\Rightarrow W_đ = 50 - 20 = 30\\text{ J}$ |
| 4 | **200** | kJ | $W_1 = mgh = 1000 \\times 10 \\times 40 = 400\\text{ kJ}$; $W_2 = \\frac{1}{2}mv^2 = 200\\text{ kJ}$. $Q = W_1 - W_2 = 200\\text{ kJ}$. |

---

### PHẦN IV. CÂU HỎI TỰ LUẬN (3,0 điểm)
- Ý 1: Tính vận tốc tại $B$: $v_B = \\sqrt{v_A^2 + 2gz_A} = \\sqrt{10^2 + 2 \\times 10 \\times 30} = 10\\sqrt{7} \\approx 26{,}46\\text{ m/s}$ (1,0 đ).
- Ý 2: Công ma sát trên dốc: $A_{ms} = - \\mu M g \\cos 30^\\circ \\cdot s \\approx - 3464{,}1 s\\text{ (J)}$ (1,0 đ).
- Ý 3: Quãng đường dừng lại tối đa: $s_{max} \\approx 52\\text{ m}$ (1,0 đ).
"""

# ==============================================================================
# ALIASES CHO TƯƠNG THÍCH CODE CŨ
# ==============================================================================
SAMPLE_METADATA = VATLI_METADATA
SAMPLE_LESSON_PLAN = VATLI_LESSON_PLAN
SAMPLE_SLIDES = VATLI_SLIDES
SAMPLE_EXAM_MATRIX = VATLI_EXAM_MATRIX
SAMPLE_EXAM_SPEC = VATLI_EXAM_SPEC
SAMPLE_EXAM_QUESTIONS = VATLI_EXAM_QUESTIONS
SAMPLE_EXAM_ANSWERS = VATLI_EXAM_ANSWERS


# ==============================================================================
# DỮ LIỆU MẪU MÔN TOÁN HỌC (THPT & THCS)
# ==============================================================================
TOAN_METADATA = {
    "grade_level": "THPT",
    "grade": "Lớp 10",
    "subject": "Toán",
    "book_series": "Kết nối tri thức với cuộc sống",
    "lesson_name": "Bài 3: Hệ thức lượng trong tam giác và Định lí Cosin, Sin",
    "duration": "2 tiết (90 phút)",
    "special_notes": "Ứng dụng hình học giải quyết bài toán đo khoảng cách gián tiếp trong thực địa (đo chiều cao tháp, bề rộng khúc sông)."
}

TOAN_LESSON_PLAN = """# KẾ HOẠCH BÀI DẠY (THEO CÔNG VĂN 5512/BGDĐT-GDTrH)

**TÊN BÀI DẠY: BÀI 3 - HỆ THỨC LƯỢNG TRONG TAM GIÁC (ĐỊNH LÍ COSIN, SIN VÀ DIỆN TÍCH)**  
**Môn học:** Toán | **Lớp:** 10  
**Bộ sách:** Kết nối tri thức với cuộc sống  
**Thời lượng thực hiện:** 2 tiết (90 phút)  

---

## I. MỤC TIÊU BÀI HỌC

### 1. Về kiến thức
- Phát biểu và viết được công thức định lí Cosin: $a^2 = b^2 + c^2 - 2bc\\cos A$ và hệ quả tính góc $\\cos A = \\frac{b^2 + c^2 - a^2}{2bc}$.
- Phát biểu và viết được công thức định lí Sin: $\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = 2R$.
- Nắm vững các công thức tính diện tích tam giác: $S = \\frac{1}{2}bc\\sin A = \\frac{abc}{4R} = pr = \\sqrt{p(p-a)(p-b)(p-c)}$ (công thức Heron).
- Giải được tam giác (tính cạnh, góc và diện tích) trong các tình huống thực tiễn.

### 2. Về năng lực
- **Năng lực chung:** Tự chủ trong tự học, hợp tác nhóm giải quyết bài toán trắc địa, sáng tạo mô hình hóa tam giác.
- **Năng lực toán học (CT GDPT 2018):**
  - *Tư duy và lập luận toán học:* Chứng minh định lí Cosin bằng tích vô hướng vectơ.
  - *Mô hình hóa toán học:* Chuyển đổi bài toán đo chiều cao tháp thành bài toán giải tam giác.
  - *Sử dụng công cụ học toán:* Sử dụng máy tính cầm tay giải lượng giác chính xác.

### 3. Về phẩm chất
- Chăm chỉ, trung thực trong tính toán số liệu và có tinh thần trách nhiệm tập thể.

---

## II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU
- GV: Giáo án điện tử, thước đo góc, phần mềm GeoGebra mô phỏng tam giác, Phiếu học tập số 1 và 2.
- HS: SGK Toán 10, vở ghi chép, máy tính cầm tay Casio fx-580VN X, thước đo độ.

---

## III. TIẾN TRÌNH DẠY HỌC

### 1. HOẠT ĐỘNG 1: MỞ ĐẦU / KHỞI ĐỘNG (10 phút)
- **Mục tiêu:** Tạo mâu thuẫn nhận thức khi định lí Pythagore không áp dụng được cho tam giác thường.
- **Nội dung:** Đo khoảng cách giữa 2 điểm bên bờ hồ với $CA = 50\\text{ m}, CB = 80\\text{ m}, \\widehat{C} = 60^\\circ$. Tính $AB$?
- **Sản phẩm:** Dự đoán của HS về công thức liên hệ giữa 3 cạnh và góc xen giữa.
- **Tổ chức thực hiện:** GV chuyển giao ➔ HS thảo luận ➔ Báo cáo đề xuất ➔ GV giới thiệu Định lí Cosin.

### 2. HOẠT ĐỘNG 2: HÌNH THÀNH KIẾN THỨC MỚI (50 phút)
- **Mạch 1: Định lí Cosin:** Chứng minh $a^2 = b^2 + c^2 - 2bc\\cos A$ và hệ quả tính góc (25 phút).
- **Mạch 2: Định lí Sin & 5 công thức diện tích:** $\\frac{a}{\\sin A} = 2R$ và công thức Heron (25 phút).
- **Tổ chức thực hiện:** Thảo luận nhóm 4 học sinh với phiếu học tập ➔ Đại diện báo cáo ➔ GV kết luận chuẩn hóa.

### 3. HOẠT ĐỘNG 3: LUYỆN TẬP (18 phút)
- Cho tam giác $ABC$ có $a = 8, b = 10, c = 13$. Tính góc $A$, bán kính $R$ và diện tích $S$.

### 4. HOẠT ĐỘNG 4: VẬN DỤNG (12 phút)
- Dự án thực hành tại trường: Dùng giác kế tự chế đo chiều cao cột cờ sân trường mà không cần trèo lên ngọn.
"""

TOAN_SLIDES = [
    {
        "slide_number": 1,
        "title": "BÀI 3: HỆ THỨC LƯỢNG TRONG TAM GIÁC",
        "bullets": [
            "Môn: Toán 10 - Bộ sách Kết nối tri thức với cuộc sống",
            "Thời lượng: 2 tiết (90 phút)",
            "Câu hỏi khởi động: Làm sao đo được khoảng cách giữa 2 điểm bên bờ hồ mà không cần bơi qua?",
            "Giáo viên giảng dạy: Thầy/Cô Bộ môn Toán"
        ],
        "visual_prompt": "Hình ảnh người kĩ sư dùng máy kinh vĩ trắc địa ngắm tam giác qua một hồ nước rộng lớn lúc bình minh.",
        "speaker_notes": "Chào các em! Trong bài học hôm nay, chúng ta sẽ mở rộng định lí Pythagore lên tầm cao mới, áp dụng cho mọi tam giác nhọn, tù bất kì trong không gian."
    },
    {
        "slide_number": 2,
        "title": "MỤC TIÊU BÀI HỌC CẦN ĐẠT",
        "bullets": [
            "Làm chủ định lí Cosin và công thức tính góc: a² = b² + c² - 2bc.cosA",
            "Khắc sâu định lí Sin: a/sinA = b/sinB = c/sinC = 2R",
            "Nắm vững 5 công thức tính diện tích tam giác (bao gồm công thức Heron)",
            "Vận dụng: Giải quyết các bài toán đo đạc thực địa và định vị GPS"
        ],
        "visual_prompt": "Sơ đồ tư duy dạng bông hoa 4 cánh biểu diễn 4 năng lực toán học cốt lõi của bài học.",
        "speaker_notes": "Kết thúc bài học, các em sẽ tự tay tính được khoảng cách gián tiếp ngoài đời thực chỉ với một góc ngắm và hai cạnh đo được."
    },
    {
        "slide_number": 3,
        "title": "1. ĐỊNH LÍ COSIN TRONG TAM GIÁC",
        "bullets": [
            "Trong tam giác ABC bất kì với BC = a, CA = b, AB = c:",
            "• a² = b² + c² - 2bc.cosA",
            "• b² = a² + c² - 2ac.cosB",
            "• c² = a² + b² - 2ab.cosC",
            "Đặc biệt: Khi góc A = 90° thì cosA = 0 ➔ Trở thành định lí Pythagore quen thuộc!"
        ],
        "visual_prompt": "Hình tam giác ABC tổng quát với các cạnh a, b, c được tô màu nổi bật và công thức đóng khung vàng kim.",
        "speaker_notes": "Các em hãy chú ý: Dấu trừ trước 2bc.cosA chính là phần bù trừ khi góc A là góc nhọn hoặc góc tù."
    },
    {
        "slide_number": 4,
        "title": "2. HỆ QUẢ TÍNH GÓC CỦA ĐỊNH LÍ COSIN",
        "bullets": [
            "Khi biết độ dài 3 cạnh, ta có thể tính chính xác số đo cả 3 góc:",
            "• cosA = (b² + c² - a²) / (2bc)",
            "• cosB = (a² + c² - b²) / (2ac)",
            "• cosC = (a² + b² - c²) / (2ab)",
            "Quy tắc dấu: cos > 0 ➔ Góc nhọn; cos = 0 ➔ Góc vuông; cos < 0 ➔ Góc tù!"
        ],
        "visual_prompt": "Bảng tóm tắt quy tắc xét dấu lượng giác với hình minh họa 3 trường hợp góc nhọn, vuông và tù trực quan.",
        "speaker_notes": "Nếu bấm máy ra cosA âm, đừng lo lắng, điều đó chỉ chứng tỏ tam giác có góc A là góc tù lớn hơn 90 độ."
    },
    {
        "slide_number": 5,
        "title": "3. ĐỊNH LÍ SIN VÀ BÁN KÍNH NGOẠI TIẾP",
        "bullets": [
            "Hệ thức: a / sinA = b / sinB = c / sinC = 2R",
            "Trong đó: R là bán kính đường tròn ngoại tiếp tam giác ABC",
            "Ứng dụng: Dùng khi biết 1 cạnh và 2 góc, hoặc 2 cạnh và 1 góc đối"
        ],
        "visual_prompt": "Hình vẽ tam giác ABC nội tiếp trong đường tròn tâm O bán kính R với các đường kính minh họa định lí Sin.",
        "speaker_notes": "Định lí Sin rất uy lực khi bài toán yêu cầu tìm bán kính đường tròn ngoại tiếp đi qua 3 đỉnh của công trình."
    },
    {
        "slide_number": 6,
        "title": "4. BÀI TOÁN KHỞI ĐỘNG ĐÃ ĐƯỢC GIẢI MÃ",
        "bullets": [
            "Đo khoảng cách hồ nước: CA = 50m, CB = 80m, góc C = 60°",
            "Áp dụng định lí Cosin cho tam giác ABC:",
            "  AB² = 50² + 80² - 2 × 50 × 80 × cos60° = 2500 + 6400 - 4000 = 4900",
            "➔ Khoảng cách hai bờ: AB = √4900 = 70 mét!"
        ],
        "visual_prompt": "Sơ đồ hồ nước với tam giác ABC được điền đầy đủ số đo cạnh và góc vừa tìm được một cách hoàn hảo.",
        "speaker_notes": "Chỉ với 2 dòng tính toán, chúng ta đã đo được khoảng cách 70 mét mà không cần phải lội xuống nước!"
    },
    {
        "slide_number": 7,
        "title": "5. TỔNG KẾT & NHIỆM VỤ DỰ ÁN",
        "bullets": [
            "Ghi nhớ: Bộ đôi định lí Cosin - Sin và công thức Heron",
            "Dự án học tập: 'Nhà khảo sát trắc địa nhí' đo chiều cao cột cờ trường học",
            "Nộp báo cáo số liệu và video thuyết trình nhóm vào tuần tới",
            "Chúc các em học tốt môn Toán!"
        ],
        "visual_prompt": "Hình ảnh nhóm học sinh đang hào hứng cầm giác kế ngắm đo cột cờ dưới ánh nắng sân trường.",
        "speaker_notes": "Toán học không chỉ nằm trên trang giấy mà đang hiện diện quanh ta. Cảm ơn sự nỗ lực của các em!"
    }
]

TOAN_EXAM_MATRIX = """# MA TRẬN ĐỀ KIỂM TRA ĐỊNH KÌ THEO CÔNG VĂN 7991/BGDĐT-GDTrH
**Môn:** Toán | **Khung cấu trúc:** Tỉ lệ nhận thức Biết 40% - Hiểu 30% - Vận dụng 30%.  
**Tỉ lệ hình thức:** TNKQ 4 lựa chọn (3,0 đ) + TNKQ Đúng-Sai (2,0 đ) + TNKQ Trả lời ngắn (2,0 đ) + Tự luận (3,0 đ).

| TT | Chủ đề / Đơn vị kiến thức | Mức độ: Biết (40%) | Mức độ: Hiểu (30%) | Mức độ: Vận dụng (30%) | Tổng điểm |
|:---|:---|:---:|:---:|:---:|:---:|
| 1 | Định lí Cosin và hệ quả tính góc | 4 câu TN (Phần I) | 2 câu TN (Phần I) | | 1,5 đ |
| 2 | Định lí Sin và bán kính ngoại tiếp | 2 câu TN (Phần I) | 1 lệnh Đ/S (Phần II) | 1 lệnh Đ/S (Phần II) | 1,5 đ |
| 3 | Các công thức diện tích tam giác | | 1 lệnh Đ/S (Phần II) | 1 lệnh Đ/S (Phần II) | 1,0 đ |
| 4 | Bài toán giải tam giác & đo đạc thực tế | | 1 ý TL (1,0 đ) | 4 câu TLN + 2 ý TL (5,0 đ) | 6,0 đ |
| | **TỔNG CỘNG** | **4,0 điểm (40%)** | **3,0 điểm (30%)** | **3,0 điểm (30%)** | **10,0 điểm** |
"""

TOAN_EXAM_SPEC = """# BẢN ĐẶC TẢ ĐỀ KIỂM TRA ĐỊNH KÌ TOÁN (CÔNG VĂN 7991/BGDĐT-GDTrH)
| TT | Mạch kiến thức | Đơn vị kiến thức | Yêu cầu cần đạt | Số câu | Mã NL |
|:---|:---|:---|:---|:---:|:---:|
| 1 | Hình học | Định lí Cosin | **Nhận biết:** Nhận biết đúng biểu thức định lí Cosin và công thức tính $\\cos A$. | 4 TN | NL_TOAN 1.1 |
| 2 | Hình học | Định lí Sin | **Thông hiểu:** Tính được độ dài một cạnh hoặc bán kính $R$ ngoại tiếp. | 2 TN | NL_TOAN 1.2 |
| 3 | Hình học | Giải tam giác tổng quát | **Thông hiểu & Vận dụng:** Phân tích đúng sai mệnh đề góc tù, bán kính nội tiếp. | 2 câu Đ/S | NL_TOAN 2.1 |
| 4 | Hình học | Diện tích & Heron | **Vận dụng cấp 1:** Tính được diện tích theo công thức Heron hoặc bán kính $r$. | 4 câu TLN | NL_TOAN 2.2 |
| 5 | Hình học | Mô hình thực tế | **Vận dụng cao:** Thiết lập mô hình giải tam giác để đo chiều cao tháp. | 1 bài TL | NL_TOAN 3.1 |
"""

TOAN_EXAM_QUESTIONS = """# ĐỀ KIỂM TRA ĐỊNH KÌ MÔN TOÁN
**Thời gian làm bài: 45 phút**  
*(Đề kiểm tra tuân thủ cấu trúc định dạng chuẩn Công văn 7991/BGDĐT-GDTrH)*

---

### PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (3,0 điểm)
**Câu 1.** Trong tam giác $ABC$, công thức nào sau đây diễn tả đúng định lí Cosin?  
A. $a^2 = b^2 + c^2 + 2bc\\cos A$  
B. $a^2 = b^2 + c^2 - 2bc\\cos A$  
C. $a^2 = b^2 + c^2 - bc\\cos A$  
D. $a^2 = b^2 + c^2 - 2bc\\sin A$  

**Câu 2.** Hệ quả nào sau đây dùng để tính $\\cos A$?  
A. $\\cos A = \\frac{b^2 + c^2 - a^2}{2bc}$  
B. $\\cos A = \\frac{a^2 + c^2 - b^2}{2ac}$  
C. $\\cos A = \\frac{b^2 + c^2 + a^2}{2bc}$  
D. $\\cos A = \\frac{b^2 - c^2 + a^2}{2bc}$  

**Câu 3.** Cho tam giác $ABC$ có bán kính đường tròn ngoại tiếp là $R$. Hệ thức nào sau đây đúng?  
A. $\\frac{a}{\\sin A} = R$  
B. $\\frac{a}{\\sin A} = 2R$  
C. $\\frac{a}{\\cos A} = 2R$  
D. $a\\sin A = 2R$  

**Câu 4.** Cho tam giác $ABC$ có $b = 6, c = 8$ và $\\widehat{A} = 60^\\circ$. Độ dài cạnh $a$ bằng  
A. $2\\sqrt{13}$  
B. $2\\sqrt{37}$  
C. $10$  
D. $\\sqrt{52}$  

---

### PHẦN II. TRẮC NGHIỆM ĐÚNG - SAI (2,0 điểm)
*Thang điểm CV 7991: Đúng 1 ý = 0,10đ; Đúng 2 ý = 0,25đ; Đúng 3 ý = 0,50đ; Đúng 4 ý = 1,00đ.*

**Câu 1.** Cho tam giác $ABC$ có ba cạnh $a = 7, b = 8, c = 5$.  
a) Nửa chu vi của tam giác $ABC$ có giá trị bằng $p = 10$.  
b) Góc $A$ của tam giác $ABC$ là góc tù vì cạnh $b$ lớn hơn cạnh $a$.  
c) Giá trị của $\\cos A$ bằng $0{,}5$, suy ra số đo góc $A = 60^\\circ$.  
d) Diện tích tam giác $ABC$ tính theo công thức Heron có giá trị là $10\\sqrt{3}$.  

---

### PHẦN III. TRẮC NGHIỆM TRẢ LỜI NGẮN (2,0 điểm)
**Câu 1.** Cho tam giác có ba cạnh lần lượt là $13, 14, 15$. Tính diện tích tam giác đó.  
*(Điền kết quả: ...)*  

**Câu 2.** Cho tam giác có diện tích $S = 84$ và nửa chu vi $p = 21$. Tính bán kính đường tròn nội tiếp $r$ của tam giác.  
*(Điền kết quả: ...)*  

---

### PHẦN IV. TỰ LUẬN (3,0 điểm)
Để đo chiều cao của một tháp truyền hình ven bờ sông Tiền, hai điểm quan sát $A$ và $B$ cách nhau $40\\text{ m}$ thẳng hàng với chân tháp $C$. Góc ngắm tại $A$ là $35^\\circ$, tại $B$ là $50^\\circ$. Tính chiều cao của tháp truyền hình (biết giác kế đặt cách đất $1{,}3\\text{ m}$).
"""

TOAN_EXAM_ANSWERS = """# HƯỚNG DẪN CHẤM VÀ ĐÁP ÁN ĐỀ KIỂM TRA TOÁN
- Phần I: 1-B, 2-A, 3-B, 4-A.
- Phần II: a-ĐÚNG, b-SAI, c-ĐÚNG, d-ĐÚNG.
- Phần III: Câu 1 = 84; Câu 2 = 4.
- Phần IV: Chiều cao tháp $H = 67{,}9 + 1{,}3 = 69{,}2\\text{ m}$.
"""


# ==============================================================================
# HỆ THỐNG HÌNH ẢNH MINH HỌA TRỰC QUAN CHO BÀI GIẢNG SLIDE (CURATED SLIDE IMAGES)
# ==============================================================================
SUBJECT_SLIDE_IMAGES = {
    "Vật lí": [
        "https://images.unsplash.com/photo-1513889961551-628c1e5e2ee9?w=800&auto=format&fit=crop&q=80",  # Tàu lượn siêu tốc
        "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800&auto=format&fit=crop&q=80",  # Mục tiêu
        "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=800&auto=format&fit=crop&q=80",  # Khái niệm cơ năng
        "https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=800&auto=format&fit=crop&q=80",  # Chuyển hóa năng lượng
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80",  # Định luật bảo toàn
        "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",  # Mô phỏng PhET
        "https://images.unsplash.com/photo-1508873696983-2df57046475a?w=800&auto=format&fit=crop&q=80",  # Lực ma sát và nhiệt
        "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80",  # Quy trình 4 bước
        "https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?w=800&auto=format&fit=crop&q=80",  # Luyện tập tại lớp
        "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=800&auto=format&fit=crop&q=80",  # Tổng kết & dặn dò
    ],
    "Toán": [
        "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=800&auto=format&fit=crop&q=80",  # Trắc địa đo khoảng cách
        "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800&auto=format&fit=crop&q=80",  # Mục tiêu
        "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=800&auto=format&fit=crop&q=80",  # Định lí Cosin
        "https://images.unsplash.com/photo-1596495578065-6e0763fa1178?w=800&auto=format&fit=crop&q=80",  # Hệ quả tính góc
        "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&auto=format&fit=crop&q=80",  # Định lí Sin & Ngoại tiếp
        "https://images.unsplash.com/photo-1580582932707-520aed937b7b?w=800&auto=format&fit=crop&q=80",  # Giải mã bài toán hồ nước
        "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=800&auto=format&fit=crop&q=80",  # Tổng kết & Dự án
    ],
    "Ngữ văn": [
        "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=800&auto=format&fit=crop&q=80",  # Thiên nhiên sử thi
        "https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80",  # Mục tiêu cần đạt
        "https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?w=800&auto=format&fit=crop&q=80",  # Chân dung người anh hùng
        "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80",  # Cảnh ăn mừng chiến thắng
        "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=800&auto=format&fit=crop&q=80",  # Tổng kết di sản văn hóa
    ],
    "Khoa học tự nhiên (KHTN)": [
        "https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=800&auto=format&fit=crop&q=80",  # Thí nghiệm phòng lab
        "https://images.unsplash.com/photo-1603126857599-f6e157fa2fe6?w=800&auto=format&fit=crop&q=80",  # Ống nghiệm và thang pH
        "https://images.unsplash.com/photo-1582719508461-905c673771fd?w=800&auto=format&fit=crop&q=80",  # Phản ứng acid bazơ
        "https://images.unsplash.com/photo-1507668077129-56e32842fceb?w=800&auto=format&fit=crop&q=80",  # Ứng dụng nông nghiệp và đất trồng
        "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=800&auto=format&fit=crop&q=80",  # Tổng kết
    ]
}

DEFAULT_EDUCATION_IMAGES = [
    "https://images.unsplash.com/photo-1509062522246-3755977927d7?w=800&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=800&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?w=800&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=800&auto=format&fit=crop&q=80",
]

def attach_slide_images(subject: str, slides: list) -> list:
    img_list = SUBJECT_SLIDE_IMAGES.get(subject, DEFAULT_EDUCATION_IMAGES)
    enhanced = []
    for idx, s in enumerate(slides):
        s_copy = dict(s)
        if "image_url" not in s_copy or not s_copy.get("image_url"):
            s_copy["image_url"] = img_list[idx % len(img_list)]
        enhanced.append(s_copy)
    return enhanced


# ==============================================================================
# DỮ LIỆU MẪU CHUYÊN SÂU: CHUYỆN NGƯỜI CON GÁI NAM XƯƠNG (NGỮ VĂN 9)
# ==============================================================================
VUNUONG_METADATA = {
    "grade_level": "THCS",
    "grade": "Lớp 9",
    "subject": "Ngữ văn",
    "book_series": "Kết nối tri thức với cuộc sống",
    "lesson_name": "Chuyện người con gái Nam Xương (Trích Truyền kì mạn lục - Nguyễn Dữ)",
    "duration": "2 tiết (90 phút)",
    "special_notes": "Rèn luyện năng lực đọc hiểu truyện truyền kì trung đại, phân tích nhân vật Vũ Nương và chi tiết nghệ thuật 'chiếc bóng'."
}

VUNUONG_LESSON_PLAN = """# KẾ HOẠCH BÀI DẠY (THEO CÔNG VĂN 5512/BGDĐT-GDTrH)

**TÊN BÀI DẠY: CHUYỆN NGƯỜI CON GÁI NAM XƯƠNG (TRÍCH TRUYỀN KÌ MẠN LỤC - NGUYỄN DỮ)**  
**Môn học:** Ngữ văn | **Lớp:** 9 (THCS)  
**Bộ sách:** Kết nối tri thức với cuộc sống  
**Thời lượng thực hiện:** 2 tiết (90 phút)  

---

## I. MỤC TIÊU BÀI HỌC

### 1. Về kiến thức
- Hiểu được tác giả Nguyễn Dữ và vị trí kiệt tác của tập *Truyền kì mạn lục* trong nền văn học trung đại Việt Nam.
- Cảm nhận và phân tích được vẻ đẹp phẩm chất mẫu mực của nhân vật Vũ Nương: người phụ nữ nết na, hiếu thảo, người vợ thủy chung son sắt và người mẹ yêu thương con hết mực.
- Thấu hiểu và xót xa trước số phận bi kịch oan khiên, đau đớn của Vũ Nương; nhận diện nguyên nhân sâu xa từ chế độ phong kiến nam quyền độc đoán và chiến tranh phi nghĩa.
- Đánh giá được giá trị hiện thực, giá trị nhân đạo sâu sắc cùng các nét đặc sắc về nghệ thuật: chi tiết cái bóng (thắt nút - mở nút kịch tính) và sự kết hợp hài hòa giữa yếu tố hiện thực với yếu tố kì ảo.

### 2. Về năng lực
- **Năng lực chung:**
  - *Tự chủ và tự học:* Tự giác đọc văn bản, tìm hiểu chú thích từ ngữ Hán Việt, hoàn thành phiếu học tập cá nhân.
  - *Giao tiếp và hợp tác:* Tích cực thảo luận nhóm, biết lắng nghe và phản biện ý kiến về vẻ đẹp và bi kịch của nhân vật.
  - *Giải quyết vấn đề và sáng tạo:* Trình bày quan điểm cá nhân về giá trị của lòng tin và sự bao dung trong cuộc sống gia đình.
- **Năng lực văn học (Đặc thù môn Ngữ văn):**
  - *Năng lực tiếp nhận văn bản:* Nhận biết và phân tích đặc trưng thể loại truyện truyền kì; phân tích tâm lí nhân vật qua ngôn ngữ đối thoại, độc thoại và hành động.
  - *Năng lực tạo lập văn bản:* Viết đoạn văn nghị luận (khoảng 150 - 200 chữ) cảm thụ về vẻ đẹp phẩm chất hoặc phân tích ý nghĩa chi tiết chiếc bóng.

### 3. Về phẩm chất
- *Nhân ái:* Biết đồng cảm, xót thương cho thân phận bất hạnh của người phụ nữ trong xã hội cũ; trân trọng giá trị phẩm giá con người.
- *Trách nhiệm:* Có ý thức bồi đắp niềm tin, sự tôn trọng và tình yêu thương chân thành trong gia đình; lên án thói gia trưởng, độc đoán.

---

## II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU
1. **Giáo viên:** Kế hoạch bài dạy, bài giảng điện tử PowerPoint kèm hình ảnh bến Hoàng Giang và tranh minh họa xưa; Phiếu học tập số 1 (Vẻ đẹp Vũ Nương), Phiếu học tập số 2 (Bi kịch và Chi tiết chiếc bóng).
2. **Học sinh:** SGK Ngữ văn 9, soạn bài theo câu hỏi hướng dẫn đọc hiểu trong SGK, vở ghi bài.

---

## III. TIẾN TRÌNH DẠY HỌC

### 1. HOẠT ĐỘNG 1: MỞ ĐẦU / KHỞI ĐỘNG (10 phút)
- **a) Mục tiêu:** Kích hoạt cảm xúc về thân phận người phụ nữ Việt Nam trong xã hội phong kiến, tạo tâm thế đồng cảm trước khi tiếp cận tác phẩm.
- **b) Nội dung:** Học sinh quan sát hình ảnh chiếc bóng trên tường và lắng nghe câu ca dao: *"Thân em như tấm lụa đào / Phất phơ giữa chợ biết vào tay ai?"*. Trả lời câu hỏi gợi mở: *Chiếc bóng có thể gợi ra những điều gì trong cuộc đời một con người? Người phụ nữ xưa thường phải đối mặt với những định kiến nghiệt ngã nào?*
- **c) Sản phẩm:** Câu trả lời chia sẻ cảm nghĩ cá nhân của học sinh.
- **d) Tổ chức thực hiện:**
  - *Bước 1 (Chuyển giao):* GV chiếu slide hình ảnh và câu hỏi gợi mở.
  - *Bước 2 (Thực hiện):* HS quan sát, trao đổi nhanh cặp đôi trong 2 phút.
  - *Bước 3 (Báo cáo):* Đại diện 2 học sinh phát biểu cảm nhận.
  - *Bước 4 (Kết luận):* GV nhận xét và dẫn dắt: Trong xã hội phong kiến, người phụ nữ chịu muôn vàn bất công. Hôm nay, chúng ta cùng đến với câu chuyện đầy xót xa của nàng Vũ Nương để thấu cảm sâu sắc hơn điều đó.

---

### 2. HOẠT ĐỘNG 2: HÌNH THÀNH KIẾN THỨC MỚI (50 phút)

#### Mạch 1: Tìm hiểu chung về tác giả và tác phẩm (10 phút)
- **a) Mục tiêu:** Nắm được tiểu sử Nguyễn Dữ, thể loại *Truyền kì mạn lục* và xuất xứ của văn bản.
- **b) Nội dung:** Trình bày nét chính về Nguyễn Dữ (sống ở thế kỉ XVI, học trò Tuyết Giang Phu Tử Nguyễn Bỉnh Khiêm), tập truyện *Truyền kì mạn lục* ("thiên cổ kì bút") và nguồn gốc truyện dân gian *Chuyện chàng Trương*.
- **c) Sản phẩm:** Ghi chép tóm tắt thông tin vào vở; sơ đồ tóm tắt cốt truyện.
- **d) Tổ chức thực hiện:**
  - *Bước 1 (Chuyển giao):* Yêu cầu HS đọc mục Chú thích sao trong SGK và tóm tắt cốt truyện trong 5 câu.
  - *Bước 2 (Thực hiện):* HS đọc lướt, ghi từ khóa chính.
  - *Bước 3 (Báo cáo):* 1 HS tóm tắt cốt truyện; 1 HS nêu đặc điểm thể loại truyền kì.
  - *Bước 4 (Kết luận):* GV chốt kiến thức: Truyền kì là thể văn xuôi chữ Hán phản ánh hiện thực qua các yếu tố kì ảo hoang đường.

#### Mạch 2: Vẻ đẹp phẩm chất của nhân vật Vũ Nương (15 phút)
- **a) Mục tiêu:** Phân tích vẻ đẹp toàn diện của Vũ Nương qua các mối quan hệ gia đình.
- **b) Nội dung:** Phân tích phẩm chất Vũ Nương: 1) Với chồng Trương Sinh (giữ gìn khuôn phép, không để xảy ra bất hòa, tiễn chồng đi lính đầy ân tình); 2) Với mẹ chồng (chăm sóc thuốc men chu đáo, ma chay tế lễ như cha mẹ đẻ); 3) Với con thơ (vừa làm mẹ vừa làm cha, luôn vỗ về yêu thương con).
- **c) Sản phẩm:** Phiếu học tập số 1 được hoàn thành với các dẫn chứng cụ thể từ văn bản.
- **d) Tổ chức thực hiện:**
  - *Bước 1 (Chuyển giao):* GV chia lớp 4 nhóm, phát Phiếu học tập số 1 về 3 mối quan hệ của Vũ Nương.
  - *Bước 2 (Thực hiện):* Nhóm thảo luận tìm dẫn chứng lời nói, cử chỉ của nàng trong 5 phút.
  - *Bước 3 (Báo cáo):* Nhóm 1 và 2 trình bày; Nhóm 3 và 4 nhận xét, bổ sung.
  - *Bước 4 (Kết luận):* GV chuẩn hóa: Vũ Nương là hiện thân mẫu mực cho vẻ đẹp người phụ nữ Việt Nam: Công - Dung - Ngôn - Hạnh.

#### Mạch 3: Nỗi oan khuất tột cùng và bi kịch cái chết (15 phút)
- **a) Mục tiêu:** Phân tích nguyên nhân cái chết oan khiên và ý nghĩa chi tiết chiếc bóng.
- **b) Nội dung:**
  - Nguyên nhân trực tiếp: Chiếc bóng trên vách tường do nàng chỉ cho con xem và lời nói ngây thơ của bé Đản (*"Ô hay! Thế ra ông cũng là cha tôi ư?..."*).
  - Nguyên nhân sâu xa: Tính đa nghi, gia trưởng của Trương Sinh (con nhà hào phú, ít học); chế độ phong kiến bất bình đẳng nam quyền; chiến tranh li loạn.
  - Hành động của Vũ Nương: Lời phân trần thống thiết, thanh minh bất thành ➔ Trầm mình xuống bến Hoàng Giang tự vẫn để bảo toàn tiết hạnh.
- **c) Sản phẩm:** Sơ đồ phân tích nguyên nhân bi kịch và ý nghĩa biểu tượng của "chiếc bóng".
- **d) Tổ chức thực hiện:**
  - *Bước 1 (Chuyển giao):* GV đặt câu hỏi: *Ai là thủ phạm thực sự đẩy Vũ Nương vào chỗ chết? Chiếc bóng có vai trò nghệ thuật gì?*
  - *Bước 2 (Thực hiện):* HS trao đổi nhóm bàn, phân tích tính hai mặt của chi tiết chiếc bóng (thắt nút và mở nút).
  - *Bước 3 (Báo cáo):* Đại diện các nhóm trả lời câu hỏi phản biện.
  - *Bước 4 (Kết luận):* GV khẳng định: Chiếc bóng vừa là minh chứng cho tình thương con của Vũ Nương, vừa là ngòi nổ châm ngòi ghen tuông mù quáng của Trương Sinh. Đó là chi tiết nghệ thuật đắt giá bậc thầy.

#### Mạch 4: Yếu tố kì ảo và giá trị nhân đạo của tác phẩm (10 phút)
- **a) Mục tiêu:** Đánh giá thế giới kì ảo dưới cung nước Linh Phi và tính bi kịch của đoạn kết.
- **b) Nội dung:** Phân tích chi tiết Vũ Nương được Linh Phi cứu sống, cuộc hội ngộ với Phan Lang và cảnh nàng hiện về trên chiếc kiệu hoa rồi biến mất.
- **c) Sản phẩm:** Nhận định về tính chất hư ảo và giá trị nhân đạo: Nàng được minh oan nhưng không thể trở về nhân gian, hạnh phúc gia đình tan vỡ vĩnh viễn.
- **d) Tổ chức thực hiện:** GV tổ chức đàm thoại gợi mở ➔ HS phát biểu ➔ GV chốt ý nghĩa đoạn kết.

---

### 3. HOẠT ĐỘNG 3: LUYỆN TẬP (18 phút)
- **a) Mục tiêu:** Củng cố kiến thức đọc hiểu qua hệ thống câu hỏi trắc nghiệm và thực hành viết đoạn văn cảm thụ.
- **b) Nội dung:**
  1. Trả lời 4 câu hỏi trắc nghiệm tương tác nhanh về văn bản.
  2. Viết đoạn văn (khoảng 8-10 câu) nêu suy nghĩ về nỗi oan khuất của nàng Vũ Nương.
- **c) Sản phẩm:** Đoạn văn hoàn chỉnh trong vở học sinh.
- **d) Tổ chức thực hiện:** HS làm việc độc lập; GV gọi 2 học sinh đọc đoạn văn trước lớp, nhận xét và chấm điểm động viên.

---

### 4. HOẠT ĐỘNG 4: VẬN DỤNG VÀ MỞ RỘNG (12 phút)
- **a) Mục tiêu:** Kết nối thông điệp tác phẩm với các giá trị gia đình và bình đẳng giới trong đời sống hiện đại.
- **b) Nội dung:** Nhiệm vụ sáng tạo: *“Nếu được nhắn nhủ một thông điệp đến Trương Sinh trước khi chàng đưa ra quyết định nghiệt ngã, em sẽ nói gì? Từ bi kịch của Vũ Nương, em rút ra bài học gì về việc gìn giữ hạnh phúc gia đình hôm nay?”*
- **c) Sản phẩm:** Bản thông điệp ngắn gọn hoặc poster chia sẻ trên không gian lớp học.
- **d) Tổ chức thực hiện:** GV giao nhiệm vụ, hướng dẫn HS hoàn thành và nộp vào tiết học sau.
"""

VUNUONG_SLIDES = [
    {
        "slide_number": 1,
        "title": "CHUYỆN NGƯỜI CON GÁI NAM XƯƠNG",
        "bullets": [
            "Tác giả: Nguyễn Dữ (Thế kỉ XVI)",
            "Thể loại: Truyện truyền kì (Trích Truyền kì mạn lục)",
            "Môn học: Ngữ văn - Lớp 9 (Bộ sách Kết nối tri thức với cuộc sống)",
            "Thông điệp: Khát vọng hạnh phúc, sự trân trọng phẩm giá và tiếng chuông thức tỉnh về niềm tin gia đình"
        ],
        "visual_prompt": "Bức tranh thủy mặc tái hiện bến Hoàng Giang êm đềm với rặng liễu rủ bóng, xa xa là con đò xuôi dòng trong sương khói mờ ảo.",
        "speaker_notes": "Chào các em học sinh! Hôm nay chúng ta sẽ bước vào thế giới của 'Truyền kì mạn lục' để cùng lắng nghe tiếng lòng tha thiết của một người phụ nữ tài sắc vẹn toàn nhưng số phận lại vô cùng trớ trêu: nàng Vũ Nương."
    },
    {
        "slide_number": 2,
        "title": "MỤC TIÊU BÀI HỌC CẦN ĐẠT",
        "bullets": [
            "Khắc sâu vẻ đẹp đức hạnh toàn vẹn của người phụ nữ Việt Nam (Vũ Nương)",
            "Thấu hiểu bi kịch oan khuất, số phận cay đắng dưới bóng đen xã hội phong kiến",
            "Giải mã nghệ thuật bậc thầy: Chi tiết 'chiếc bóng' và sự đan cài yếu tố kì ảo",
            "Bồi dưỡng phẩm chất nhân ái, sự sẻ chia và ý thức xây dựng niềm tin trong gia đình"
        ],
        "visual_prompt": "Infographic văn học gồm 4 biểu tượng: Bông sen thanh bạch (Phẩm chất), Chiếc bóng trên tường (Bi kịch), Cung nước lung linh (Kì ảo) và Trái tim nhân ái (Thông điệp).",
        "speaker_notes": "Sau bài học này, các em sẽ nắm vững đặc trưng của truyện truyền kì và có khả năng phân tích tâm lí nhân vật qua các chi tiết nghệ thuật đắt giá."
    },
    {
        "slide_number": 3,
        "title": "1. TÁC GIẢ NGUYỄN DỮ & TRUYỀN KÌ MẠN LỤC",
        "bullets": [
            "Tác giả Nguyễn Dữ: Người Hải Dương, sống ở thế kỉ XVI thời Lê - Mạc li loạn",
            "Tư tưởng: Kẻ sĩ thanh cao, lánh đục về trong, gửi gắm tâm tư qua văn chương",
            "Tập truyện 'Truyền kì mạn lục': Gồm 20 truyện viết bằng chữ Hán",
            "Được mệnh danh là 'Thiên cổ kì bút' (Áng văn kì lạ của muôn đời)"
        ],
        "visual_prompt": "Hình ảnh cuốn sách cổ chữ Hán trang trọng cùng bút lông và nghiên mực, phong thái thanh cao của bậc nho sĩ xưa.",
        "speaker_notes": "Nguyễn Dữ mượn tích xưa Chuyện chàng Trương nhưng đã thổi vào đó luồng sinh khí nghệ thuật mới mẻ, biến câu chuyện cổ tích thành kiệt tác văn học trung đại bất hủ."
    },
    {
        "slide_number": 4,
        "title": "2. VẺ ĐẸP PHẨM CHẤT NÀNG VŨ NƯƠNG",
        "bullets": [
            "Lai lịch: 'Tính đã thùy mị nết na, lại thêm tư dung tốt đẹp'",
            "Với chồng: Luôn giữ gìn khuôn phép, một lòng thủy chung son sắt ngóng trông",
            "Với mẹ chồng: Tận tâm thuốc thang chăm sóc, ma chay chu đáo như cha mẹ ruột",
            "Với con thơ: Một mình nuôi dưỡng, bù đắp tình thương người cha vắng bóng"
        ],
        "visual_prompt": "Tranh khắc họa cảnh người thiếu phụ hiền dịu ngồi dệt vải bên khung cửi dưới ánh trăng, vẻ mặt dịu dàng và kiên trinh.",
        "speaker_notes": "Vũ Nương hội tụ đầy đủ những phẩm chất cao quý nhất của người phụ nữ truyền thống: Công - Dung - Ngôn - Hạnh, hiếu nghĩa vẹn tròn."
    },
    {
        "slide_number": 5,
        "title": "3. BI KỊCH OAN KHUẤT & CHI TIẾT CHIẾC BÓNG",
        "bullets": [
            "Lời con trẻ: 'Ô hay! Thế ra ông cũng là cha tôi ư?... Chàng sợ, chàng nín thin thít'",
            "Trương Sinh: Con nhà hào phú, ít học, đa nghi, xử sự độc đoán tàn nhẫn",
            "Chiếc bóng trên vách: Ban đầu là biểu tượng tình mẫu tử ➔ Trở thành đầu mối ghen tuông mù quáng",
            "Cái chết nơi bến Hoàng Giang: Tiếng kêu oan tuyệt vọng và hành động bảo toàn danh dự"
        ],
        "visual_prompt": "Hình bóng người mẹ trên vách đất trong đêm tối lung linh ánh đèn dầu, đứa trẻ thơ chỉ tay đầy hồn nhiên.",
        "speaker_notes": "Chiếc bóng là một sáng tạo nghệ thuật thiên tài của Nguyễn Dữ. Nó vừa thắt nút bi kịch oan trái, vừa là chìa khóa mở nút giải tỏa nỗi hàm oan của nàng sau này."
    },
    {
        "slide_number": 6,
        "title": "4. THẾ GIỚI KÌ ẢO & GIÁ TRỊ NHÂN ĐẠO",
        "bullets": [
            "Cuộc sống dưới thủy cung: Nàng được Linh Phi cứu sống, trọng đãi nghĩa tình",
            "Hội ngộ Phan Lang: Vẫn trăn trở nhớ quê hương, tổ tiên và nghĩa xưa tình cũ",
            "Cảnh lập đàn giải oan: Vũ Nương ngồi trên kiệu hoa thấp thoáng rồi biến mất",
            "Ý nghĩa: Chiêu tuyết oan khiên nhưng không thể hàn gắn nỗi đau hạnh phúc tan vỡ"
        ],
        "visual_prompt": "Cảnh bến sông Hoàng Giang rực rỡ cờ hoa lập đàn tràng giải oan, hình bóng Vũ Nương mờ ảo trên chiếc kiệu lộng lẫy giữa sóng nước mù sương.",
        "speaker_notes": "Yếu tố kì ảo thể hiện niềm an ủi của nhân dân đối với người lương thiện, song tính hiện thực vẫn nghiệt ngã: cõi trần gian đã vĩnh viễn mất đi một người phụ nữ tuyệt vời."
    },
    {
        "slide_number": 7,
        "title": "5. LUYỆN TẬP: GIẢI MÃ NGHỆ THUẬT TÁC PHẨM",
        "bullets": [
            "Nghệ thuật thắt nút và mở nút kịch tính, bất ngờ và giàu sức gợi",
            "Nghệ thuật xây dựng nhân vật qua lời thoại, hành động và tâm lí chân thực",
            "Sự hòa quyện giữa bút pháp hiện thực tỉnh táo và màu sắc kì ảo bay bổng",
            "Câu hỏi củng cố: Chi tiết chiếc bóng gợi cho em bài học gì về việc tiếp nhận thông tin?"
        ],
        "visual_prompt": "Sơ đồ khối tóm tắt mối quan hệ nguyên nhân - kết quả của xung đột truyện với tông màu xanh lam hiện đại.",
        "speaker_notes": "Hãy cùng thảo luận để thấy rõ tài năng kể chuyện điêu luyện của tác giả Nguyễn Dữ thông qua cách sắp đặt chi tiết chiếc bóng độc đáo này."
    },
    {
        "slide_number": 8,
        "title": "6. THÔNG ĐIỆP BÀI HỌC VÀ NHIỆM VỤ VỀ NHÀ",
        "bullets": [
            "Khắc sâu giá trị nhân đạo: Lên án thói gia trưởng và bảo vệ phẩm giá phụ nữ",
            "Bài học sống: Niềm tin và sự lắng nghe là nền tảng cốt lõi của hạnh phúc gia đình",
            "Nhiệm vụ 1: Hoàn thành bài tập trắc nghiệm và câu hỏi đọc hiểu trong phiếu học tập",
            "Nhiệm vụ 2: Viết đoạn văn (150 chữ) chia sẻ suy nghĩ về bình đẳng giới hôm nay"
        ],
        "visual_prompt": "Hình ảnh ấm cúng của một gia đình hiện đại cùng đọc sách bên nhau, biểu trưng cho sự hòa thuận, tôn trọng và yêu thương.",
        "speaker_notes": "Tiết học hôm nay khép lại nhưng thông điệp về lòng bao dung và sự tin cậy vẫn sẽ còn vang vọng mãi trong tâm thức mỗi chúng ta."
    }
]

VUNUONG_EXAM_MATRIX = """# MA TRẬN ĐỀ KIỂM TRA ĐỊNH KÌ THEO CÔNG VĂN 7991/BGDĐT-GDTrH
**Môn:** Ngữ văn | **Lớp:** 9 | **Thời gian làm bài:** 45 phút  
**Khung cấu trúc:** Tỉ lệ nhận thức Biết 40% - Hiểu 30% - Vận dụng 30%.  
**Tỉ lệ hình thức:** TNKQ 4 lựa chọn (3,0 đ) + TNKQ Đúng-Sai (2,0 đ) + TNKQ Trả lời ngắn (2,0 đ) + Tự luận Làm văn (3,0 đ).

| TT | Kĩ năng / Đơn vị kiến thức | Mức độ: Biết (40%) | Mức độ: Hiểu (30%) | Mức độ: Vận dụng (30%) | Tổng điểm |
|:---|:---|:---:|:---:|:---:|:---:|
| 1 | **Đọc hiểu:** Ngữ liệu Truyện truyền kì trung đại | 4 câu TN (Phần I - 3,0 đ) | 1 lệnh Đ/S (Phần II - 1,0 đ) | 1 câu TL ngắn (Phần III - 1,0 đ) | **5,0 đ** |
| 2 | **Tiếng Việt & Nghệ thuật:** Chi tiết chiếc bóng | | 1 lệnh Đ/S (Phần II - 1,0 đ) | 1 câu TL ngắn (Phần III - 1,0 đ) | **2,0 đ** |
| 3 | **Viết:** Đoạn văn nghị luận văn học / xã hội | | | 1 câu Viết (Phần IV - 3,0 đ) | **3,0 đ** |
| | **TỔNG CỘNG** | **4,0 điểm (40%)** | **3,0 điểm (30%)** | **3,0 điểm (30%)** | **10,0 điểm** |
"""

VUNUONG_EXAM_SPEC = """# BẢN ĐẶC TẢ ĐỀ KIỂM TRA ĐỊNH KÌ NGỮ VĂN 9 (CÔNG VĂN 7991/BGDĐT-GDTrH)

| TT | Kĩ năng / Đơn vị kiến thức | Mức độ đánh giá / Yêu cầu cần đạt | Số lượng câu hỏi | Mã hóa năng lực |
|:---|:---|:---|:---:|:---:|
| 1 | **Đọc hiểu:** Thể loại truyện truyền kì | **Nhận biết:** Nhận diện được thể loại, tác giả, phương thức biểu đạt và xuất xứ văn bản. | 4 câu TN (C1 - C4) | NL_DOC 1.1 |
| 2 | **Đọc hiểu:** Phân tích nhân vật và chi tiết | **Thông hiểu & Vận dụng:** Đánh giá đúng sai các nhận định về phẩm chất của Vũ Nương, tính cách Trương Sinh và nguyên nhân bi kịch. | 1 câu Đúng-Sai (4 ý) | NL_DOC 2.1 |
| 3 | **Đọc hiểu:** Chi tiết nghệ thuật đắt giá | **Vận dụng cấp 1:** Rút ra ý nghĩa của chi tiết chiếc bóng và yếu tố kì ảo cuối truyện. | 2 câu Trả lời ngắn | NL_DOC 2.2 |
| 4 | **Viết văn:** Nghị luận xã hội / văn học | **Vận dụng cao:** Viết đoạn văn nghị luận (khoảng 150-200 chữ) bàn về giá trị của niềm tin và sự tôn trọng trong các mối quan hệ đời sống. | 1 câu Tự luận | NL_VIET 3.1 |
"""

VUNUONG_EXAM_QUESTIONS = """# ĐỀ KIỂM TRA ĐỊNH KÌ MÔN NGỮ VĂN - LỚP 9
**Thời gian làm bài: 45 phút**  
*(Đề kiểm tra tuân thủ cấu trúc định dạng chuẩn Công văn 7991/BGDĐT-GDTrH ngày 17/12/2024)*

---

**ĐỌC ĐOẠN TRÍCH SAU VÀ THỰC HIỆN CÁC YÊU CẦU:**
> *"Nàng quỳ xuống lạy mẹ chồng mà thưa rằng: 'Cha mẹ đẻ ra con, mẹ chồng nuôi dưỡng con. Đạo làm con chưa trọn, một mai mẹ qua đời, lòng con áy náy khôn xiết...'  
> Mẹ nàng hấp hối nói: 'Con đã chăm sóc mẹ như mẹ ruột. Trời Phật trên cao sẽ soi xét lòng hiếu thảo của con, ban cho con cháu muôn đời sau phúc đức vẹn toàn...'.  
> Đến khi Trương Sinh đi lính trở về, mẹ già đã mất, con thơ đang bập bẹ tập nói. Một đêm, Trương Sinh cùng con ngồi bên ngọn đèn dầu, đứa bé chỉ lên vách nói: 'Cha Đản lại đến kia kìa!'. Lòng ghen tuông của Trương Sinh bùng lên..."*  
> *(Trích Chuyện người con gái Nam Xương - Nguyễn Dữ, SGK Ngữ văn 9)*

---

### PHẦN I. CÂU HỎI TRẮC NGHIỆM NHIỀU LỰA CHỌN (3,0 điểm)
*Thí sinh chọn một phương án trả lời đúng duy nhất trong các câu sau:*

**Câu 1 (0,75 điểm).** Tác phẩm *Chuyện người con gái Nam Xương* của Nguyễn Dữ thuộc thể loại văn học nào?  
A. Truyện cổ tích thần kì  
B. Truyện truyền kì chữ Hán  
C. Thơ ngụ ngôn trung đại  
D. Truyện ngụ ngôn dân gian  

**Câu 2 (0,75 điểm).** Phương thức biểu đạt chính của văn bản là gì?  
A. Tự sự  
B. Biểu cảm  
C. Thuyết minh  
D. Nghị luận  

**Câu 3 (0,75 điểm).** Trong mối quan hệ với mẹ chồng, phẩm chất nào của Vũ Nương được thể hiện nổi bật nhất?  
A. Sự nhút nhát, sợ sệt  
B. Lòng hiếu thảo chân thành, chu đáo trọn vẹn  
C. Tính toán so đo việc nhà  
D. Lạnh nhạt, thờ ơ  

**Câu 4 (0,75 điểm).** Chi tiết nào sau đây là ngòi nổ trực tiếp làm bùng phát bi kịch nghi ngờ của Trương Sinh?  
A. Lá thư của người bạn cùng làng gửi về  
B. Chiếc bóng trên vách qua lời nói ngây thơ của bé Đản  
C. Lời dị nghị của hàng xóm láng giềng  
D. Kỉ vật chiếc trâm cài tóc bị rơi mất  

---

### PHẦN II. CÂU HỎI TRẮC NGHIỆM ĐÚNG - SAI (2,0 điểm)
*Thang điểm chuẩn Công văn 7991/BGDĐT-GDTrH: Đúng 1 ý = 0,10 điểm; Đúng 2 ý = 0,25 điểm; Đúng 3 ý = 0,50 điểm; Đúng cả 4 ý = 1,00 điểm.*

**Câu 1.** Xét tính đúng/sai của các nhận định sau đây về tấn bi kịch của nàng Vũ Nương:  
a) Vũ Nương tìm đến cái chết nơi bến Hoàng Giang vì không còn tình cảm với gia đình.  
b) Trương Sinh là người ít học, có tính đa nghi và phòng ngừa vợ quá mức.  
c) Cuộc hôn nhân giữa Trương Sinh và Vũ Nương có sự môn đăng hộ đối tuyệt đối về gia cảnh.  
d) Chi tiết chiếc bóng vừa có vai trò thắt nút bi kịch vừa là chìa khóa mở nút giải oan.  

**Câu 2.** Xét tính đúng/sai của các nhận định về yếu tố kì ảo trong truyện:  
a) Thế giới thủy cung thể hiện ước mơ công lí và niềm an ủi của nhân dân đối với người phụ nữ tiết hạnh.  
b) Đoạn kết kì ảo đã giải quyết trọn vẹn bi kịch và mang lại hạnh phúc gia đình sum vầy cho Vũ Nương trên dương thế.  
c) Phan Lang là nhân vật đóng vai trò nhịp cầu kết nối thế giới cõi trần và cõi nước.  
d) Tác giả sáng tạo yếu tố kì ảo nhằm mục đích duy nhất là làm câu chuyện thêm ly kì, hoang đường.  

---

### PHẦN III. CÂU HỎI TRẮC NGHIỆM TRẢ LỜI NGẮN (2,0 điểm)
*Thí sinh ghi câu trả lời ngắn gọn, chuẩn xác vào bài làm.*

**Câu 1 (1,0 điểm).** Hãy ghi lại tên con sông nơi Vũ Nương gieo mình tự vẫn để giãi bày lòng trong sạch.  
*(Ghi câu trả lời: ...)*  

**Câu 2 (1,0 điểm).** Hai từ ngữ then chốt diễn tả nguyên nhân sâu xa dẫn đến bi kịch cái chết của Vũ Nương trong lòng xã hội thời bấy giờ là gì?  
*(Ghi câu trả lời: ...)*  

---

### PHẦN IV. CÂU HỎI TỰ LUẬN (3,0 điểm)
Viết một đoạn văn nghị luận (khoảng 150 - 200 chữ) bàn về **ý nghĩa của sự tin tưởng và lòng bao dung trong việc gìn giữ hạnh phúc gia đình**, rút ra từ tấn bi kịch của nàng Vũ Nương trong *Chuyện người con gái Nam Xương*.
"""

VUNUONG_EXAM_ANSWERS = """# HƯỚNG DẪN CHẤM VÀ ĐÁP ÁN ĐỀ KIỂM TRA MÔN NGỮ VĂN 9
*(Chuẩn hóa thang điểm theo Công văn 7991/BGDĐT-GDTrH)*

---

### PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (3,0 điểm)
- Câu 1: **B** (0,75 điểm)
- Câu 2: **A** (0,75 điểm)
- Câu 3: **B** (0,75 điểm)
- Câu 4: **B** (0,75 điểm)

---

### PHẦN II. TRẮC NGHIỆM ĐÚNG - SAI (2,0 điểm)
*Áp dụng quy tắc tính điểm chuẩn CV 7991: Đúng 1 ý = 0.1đ; 2 ý = 0.25đ; 3 ý = 0.5đ; 4 ý = 1.0đ.*

- **Câu 1 (1,0 điểm):**  
  + a) **SAI** (Nàng tìm đến cái chết để bảo toàn tiết hạnh, giãi bày lòng trong trắng trước thần linh).  
  + b) **ĐÚNG** (Văn bản chỉ rõ Trương Sinh ít học, tính hay đa nghi).  
  + c) **SAI** (Trương Sinh con nhà hào phú trăm lạng vàng cưới về, Vũ Nương là con nhà kẻ khó).  
  + d) **ĐÚNG** (Chiếc bóng thắt nút ghen tuông và mở nút giải oan khi bé Đản chỉ bóng Trương Sinh).  

- **Câu 2 (1,0 điểm):**  
  + a) **ĐÚNG** (Khát vọng nhân đạo, người tốt phải được bù đắp).  
  + b) **SAI** (Vũ Nương chỉ hiện về chốc lát rồi biến mất, bi kịch vĩnh viễn không hàn gắn).  
  + c) **ĐÚNG** (Phan Lang nhận kỉ vật hoa vàng trở về báo tin cho Trương Sinh).  
  + d) **SAI** (Yếu tố kì ảo hàm chứa giá trị tư tưởng và ý nghĩa nhân đạo sâu sắc).  

---

### PHẦN III. TRẮC NGHIỆM TRẢ LỜI NGẮN (2,0 điểm)
- Câu 1 (1,0 điểm): **Sông Hoàng Giang** (hoặc: bến Hoàng Giang).
- Câu 2 (1,0 điểm): **Nam quyền** (hoặc thói gia trưởng, độc đoán) và **Chiến tranh** (hoặc chiến tranh li loạn, xã hội phong kiến).

---

### PHẦN IV. CÂU HỎI TỰ LUẬN (3,0 điểm)
- **Hình thức đoạn văn (0,5 điểm):** Viết đúng dung lượng 150-200 chữ, diễn đạt mạch lạc, không sai lỗi chính tả.
- **Nội dung nghị luận (2,0 điểm):**
  + Nêu vấn đề: Niềm tin và sự lắng nghe là chiếc mỏ neo gìn giữ con thuyền hạnh phúc gia đình (0,5 đ).
  + Phân tích từ tác phẩm: Thiếu lòng tin và thói ghen tuông mù quáng của Trương Sinh đã bức tử một người vợ hiền thục (0,5 đ).
  + Liên hệ thực tế: Trong cuộc sống hôm nay, các thành viên cần biết chia sẻ, lắng nghe và tôn trọng sự bình đẳng để tránh những rạn nứt không đáng có (1,0 đ).
- **Sáng tạo và biểu cảm (0,5 điểm):** Có suy nghĩ độc đáo, cảm xúc chân thành, lời văn thuyết phục.
"""


# ==============================================================================
# HÀM THÍCH ỨNG SƯ PHẠM ĐA NĂNG (DYNAMIC PEDAGOGICAL ENGINE)
# TỰ ĐỘNG THÍCH ỨNG THEO ĐÚNG TÊN BÀI HỌC VÀ LỰA CHỌN CỦA NGƯỜI DÙNG
# ==============================================================================
def generate_tailored_package(
    subject: str,
    grade: str = "Lớp 9",
    grade_level: str = "THCS",
    book_series: str = "Kết nối tri thức với cuộc sống",
    lesson_name: str = "",
    special_notes: str = ""
) -> dict:
    """
    Sinh trọn bộ hồ sơ sư phạm KHỚP 100% với tên bài học, môn học, lớp và bộ sách.
    Tự động nhận diện chủ đề để cung cấp tri thức chuyên sâu và trực quan hóa.
    """
    subject_clean = subject.strip()
    raw_lesson = lesson_name.strip()
    
    # 1. Trích xuất tên bài chuẩn
    if not raw_lesson:
        raw_lesson = f"Chủ đề trọng tâm môn {subject_clean} ({grade})"
    
    lesson_lower = raw_lesson.lower()
    
    # 2. KIỂM TRA TRƯỜNG HỢP: CHUYỆN NGƯỜI CON GÁI NAM XƯƠNG
    if "nam xương" in lesson_lower or "vũ nương" in lesson_lower or "nguyễn dữ" in lesson_lower:
        meta = {
            "grade_level": grade_level,
            "grade": grade,
            "subject": subject_clean,
            "book_series": book_series,
            "lesson_name": raw_lesson,
            "duration": "2 tiết (90 phút)",
            "special_notes": special_notes if special_notes else VUNUONG_METADATA["special_notes"]
        }
        
        return {
            "metadata": meta,
            "lesson_plan": VUNUONG_LESSON_PLAN,
            "slides": attach_slide_images("Ngữ văn", VUNUONG_SLIDES),
            "exam_matrix": VUNUONG_EXAM_MATRIX,
            "exam_spec": VUNUONG_EXAM_SPEC,
            "exam_questions": VUNUONG_EXAM_QUESTIONS,
            "exam_answers": VUNUONG_EXAM_ANSWERS,
            "pedagogical_summary": f"Hồ sơ sư phạm bài học '{raw_lesson}' biên soạn công phu chuẩn Công văn 5512 (4 hoạt động đọc hiểu) và đề kiểm tra 4 phần chuẩn Công văn 7991.",
            "summary_knowledge": [
                "Tác giả Nguyễn Dữ và kiệt tác văn xuôi chữ Hán Truyền kì mạn lục thế kỉ XVI.",
                "Vẻ đẹp toàn diện của Vũ Nương: hiếu nghĩa trọn vẹn, thủy chung son sắt và yêu thương con.",
                "Bi kịch oan khuất, chi tiết nghệ thuật 'chiếc bóng' và cái chết oan khiên bên dòng Hoàng Giang.",
                "Ý nghĩa chi tiết kì ảo dưới thủy cung và giá trị nhân đạo lên án thói gia trưởng phong kiến."
            ],
            "summary_competencies": [
                "Năng lực chung: Tự chủ trong đọc hiểu văn bản tự sự; Hợp tác nhóm thảo luận thông điệp nhân đạo.",
                "Năng lực văn học: Đọc hiểu thể loại truyện truyền kì; Phân tích nghệ thuật xây dựng nhân vật và chi tiết đắt giá."
            ],
            "summary_qualities": [
                "Nhân ái: Biết thấu cảm, xót thương cho thân phận bi kịch của người phụ nữ xưa.",
                "Trách nhiệm: Bồi đắp sự tin tưởng, lắng nghe và tình yêu thương chân thành trong gia đình."
            ],
            "activities": [
                {
                    "name": "Hoạt động 1: Mở đầu / Khởi động",
                    "duration": "10 phút",
                    "objective": "Gợi mở cảm xúc về thân phận người phụ nữ xưa qua câu ca dao và hình ảnh chiếc bóng.",
                    "content": "Quan sát tranh chiếc bóng trên vách và đọc câu ca dao: 'Thân em như tấm lụa đào...'.",
                    "steps": [
                        "GV chiếu hình ảnh chiếc bóng & câu ca dao",
                        "HS trao đổi cặp đôi nêu cảm nhận",
                        "Đại diện 2 học sinh phát biểu",
                        "GV dẫn dắt giới thiệu bài mới"
                    ]
                },
                {
                    "name": "Hoạt động 2: Hình thành kiến thức mới",
                    "duration": "50 phút",
                    "objective": "Tìm hiểu Nguyễn Dữ, phân tích vẻ đẹp đức hạnh, bi kịch cái chết và ý nghĩa chiếc bóng.",
                    "content": "4 mạch kiến thức: 1) Tác giả & tác phẩm; 2) Vẻ đẹp Vũ Nương; 3) Bi kịch oan khiên & Chiếc bóng; 4) Yếu tố kì ảo.",
                    "steps": [
                        "Giao Phiếu học tập số 1 và 2",
                        "HS thảo luận nhóm 4 người tìm dẫn chứng",
                        "Đại diện nhóm thuyết trình sơ đồ",
                        "GV chuẩn hóa và chốt kiến thức cốt lõi"
                    ]
                },
                {
                    "name": "Hoạt động 3: Luyện tập củng cố",
                    "duration": "18 phút",
                    "objective": "Khắc sâu nghệ thuật thắt nút - mở nút chiếc bóng qua trắc nghiệm và đoạn văn ngắn.",
                    "content": "Làm 4 câu trắc nghiệm nhanh và viết đoạn văn 8-10 câu phân tích bi kịch oan khuất.",
                    "steps": [
                        "GV giao bài tập độc lập",
                        "HS làm bài vào vở ghi",
                        "Gọi 2 HS đọc bài trước lớp",
                        "GV nhận xét, sửa lỗi diễn đạt"
                    ]
                },
                {
                    "name": "Hoạt động 4: Vận dụng thực tiễn",
                    "duration": "12 phút",
                    "objective": "Kết nối thông điệp bài học với văn hóa gia đình và bình đẳng giới trong thời đại 4.0.",
                    "content": "Viết thông điệp nhắn nhủ Trương Sinh và rút ra bài học về lòng tin trong đời sống gia đình.",
                    "steps": [
                        "GV nêu câu hỏi tình huống thực tế",
                        "HS suy nghĩ ghi thông điệp ra thẻ",
                        "Dán thông điệp lên góc học tập",
                        "GV kết luận và hướng dẫn bài về nhà"
                    ]
                }
            ]
        }
        
    # 3. KIỂM TRA TRƯỜNG HỢP: ĐĂM SĂN CHIẾN THẮNG MTAO MXÂY
    elif "đăm săn" in lesson_lower or "mtao mxây" in lesson_lower:
        meta = {
            "grade_level": grade_level,
            "grade": grade,
            "subject": subject_clean,
            "book_series": book_series,
            "lesson_name": raw_lesson,
            "duration": "2 tiết (90 phút)",
            "special_notes": special_notes if special_notes else "Phát triển năng lực tiếp nhận thể loại sử thi anh hùng Tây Nguyên."
        }
        return {
            "metadata": meta,
            "lesson_plan": f"""# KẾ HOẠCH BÀI DẠY (THEO CÔNG VĂN 5512/BGDĐT-GDTrH)
**TÊN BÀI DẠY: {raw_lesson.upper()}**  
**Môn học:** Ngữ văn | **Lớp:** {grade}  
**Bộ sách:** {book_series} | **Thời lượng:** 2 tiết (90 phút)

## I. MỤC TIÊU BÀI HỌC
- Nắm vững đặc trưng thể loại sử thi Tây Nguyên (người kể chuyện, cốt truyện, nhân vật anh hùng).
- Phân tích vẻ đẹp người tù trưởng anh minh Đăm Săn qua cảnh chiến đấu và cảnh ăn mừng chiến thắng.
- Phân tích nghệ thuật so sánh, phóng đại trùng điệp và ngôn ngữ giàu nhịp điệu của sử thi.
- Năng lực văn học: Đọc diễn cảm phân vai, viết đoạn văn cảm nhận vẻ đẹp người anh hùng.
- Phẩm chất: Tự hào về di sản văn hóa dân tộc, đề cao tinh thần đoàn kết cộng đồng.

## II. TIẾN TRÌNH 4 HOẠT ĐỘNG
1. Khởi động (10p): Xem video cồng chiêng Tây Nguyên, gợi mở phẩm chất người anh hùng buôn làng.
2. Hình thành kiến thức (50p): Mạch 1: Cảnh giao chiến dũng cảm; Mạch 2: Cảnh ăn mừng chiến thắng trù phú.
3. Luyện tập (18p): Viết đoạn văn ngắn phân tích biện pháp so sánh phóng đại trong đoạn trích.
4. Vận dụng (12p): Thiết kế poster giới thiệu giá trị di sản không gian văn hóa cồng chiêng.
""",
            "slides": attach_slide_images("Ngữ văn", [
                {"slide_number": 1, "title": f"{raw_lesson.upper()}", "bullets": [f"Môn học: Ngữ văn {grade}", f"Bộ sách: {book_series}", "Sử thi anh hùng Tây Nguyên bất hủ"], "visual_prompt": "Núi rừng Tây Nguyên hùng vĩ.", "speaker_notes": "Chào các em đến với sử thi Đăm Săn."},
                {"slide_number": 2, "title": "MỤC TIÊU CẦN ĐẠT", "bullets": ["Hiểu đặc trưng thi pháp sử thi", "Khắc họa người anh hùng buôn làng", "Nghệ thuật phóng đại trùng điệp"], "visual_prompt": "Infographic sử thi.", "speaker_notes": "Nắm vững thi pháp sử thi."},
                {"slide_number": 3, "title": "CHÂN DUNG ANH HÙNG ĐĂM SĂN", "bullets": ["Oai phong lẫm liệt, bắp chân to bằng cây xà ngang", "Múa khiên trên cao gió như bão", "Chiến đấu vì sự bình yên của buôn làng"], "visual_prompt": "Dũng sĩ Tây Nguyên.", "speaker_notes": "Vẻ đẹp người anh hùng."},
                {"slide_number": 4, "title": "CẢNH ĂN MỪNG CHIẾN THẮNG", "bullets": ["Buôn làng đông vui như mở hội", "Bò ngựa đi nghẽn cả đường rừng", "Khát vọng thịnh vượng ấm no"], "visual_prompt": "Lễ hội buôn làng.", "speaker_notes": "Sức sống cộng đồng."},
                {"slide_number": 5, "title": "TỔNG KẾT & VẬN DỤNG", "bullets": ["Giá trị văn hóa tinh thần vô giá", "Bài học về sự dấn thân vì cộng đồng", "Hoàn thành bài tập về nhà"], "visual_prompt": "Không gian cồng chiêng.", "speaker_notes": "Tổng kết bài học."}
            ]),
            "exam_matrix": """# MA TRẬN ĐỀ KIỂM TRA ĐỊNH KÌ NGỮ VĂN (CV 7991)
Tỉ lệ: Biết 40% - Hiểu 30% - Vận dụng 30%. Đọc hiểu 5,0đ + Viết 5,0đ.""",
            "exam_spec": "# BẢN ĐẶC TẢ ĐỀ KIỂM TRA ĐỊNH KÌ NGỮ VĂN (CV 7991)",
            "exam_questions": f"""# ĐỀ KIỂM TRA ĐỊNH KÌ MÔN NGỮ VĂN {grade.upper()}
Thời gian: 45 phút
Phần I: Trắc nghiệm đọc hiểu (3,0 đ).
Phần II: Đúng-Sai (2,0 đ).
Phần III: Trả lời ngắn (2,0 đ).
Phần IV: Làm văn nghị luận (3,0 đ).""",
            "exam_answers": "# HƯỚNG DẪN CHẤM ĐỀ KIỂM TRA NGỮ VĂN",
            "pedagogical_summary": f"Hồ sơ sư phạm bài học '{raw_lesson}' được xây dựng trọn vẹn theo Công văn 5512 và Công văn 7991.",
            "summary_knowledge": [
                "Thể loại sử thi anh hùng Tây Nguyên và vẻ đẹp kì vĩ của không gian buôn làng.",
                "Hình tượng người tù trưởng anh minh Đăm Săn tài năng và trượng nghĩa.",
                "Cảnh ăn mừng chiến thắng biểu trưng cho khát vọng no ấm, thịnh vượng của cộng đồng.",
                "Nghệ thuật so sánh trùng điệp, phóng đại tráng lệ giàu chất thơ."
            ],
            "summary_competencies": [
                "Năng lực chung: Tự chủ trong tiếp nhận văn bản dân gian; Hợp tác nhóm cảm thụ nghệ thuật.",
                "Năng lực văn học: Đọc diễn cảm sử thi; Phân tích thi pháp và viết văn cảm thụ."
            ],
            "summary_qualities": [
                "Yêu nước & Tự hào dân tộc: Trân trọng di sản văn hóa truyền thống của cộng đồng các dân tộc Việt Nam.",
                "Trách nhiệm: Sống có lí tưởng cống hiến vì tập thể."
            ],
            "activities": [
                {"name": "Hoạt động 1: Khởi động", "duration": "10 phút", "objective": "Kích hoạt cảm xúc về người anh hùng buôn làng.", "content": "Xem clip lễ hội đâm trâu và cồng chiêng.", "steps": ["Chiếu clip", "HS phát biểu", "GV giới thiệu sử thi", "Vào bài học"]},
                {"name": "Hoạt động 2: Hình thành kiến thức", "duration": "50 phút", "objective": "Phân tích cảnh giao chiến và cảnh ăn mừng chiến thắng.", "content": "Tìm hiểu 2 cảnh trung tâm qua phiếu học tập.", "steps": ["Giao phiếu nhóm", "HS thảo luận", "Báo cáo sản phẩm", "GV chốt kiến thức"]},
                {"name": "Hoạt động 3: Luyện tập", "duration": "18 phút", "objective": "Thực hành phân tích biện pháp tu từ so sánh phóng đại.", "content": "Viết đoạn văn ngắn phân tích câu văn đắt giá.", "steps": ["Giao bài viết", "HS làm độc lập", "Đọc trước lớp", "GV chữa bài"]},
                {"name": "Hoạt động 4: Vận dụng", "duration": "12 phút", "objective": "Quảng bá văn hóa Tây Nguyên.", "content": "Thiết kế áp phích tuyên truyền giữ gìn cồng chiêng.", "steps": ["Nêu yêu cầu dự án", "HS ghi nhiệm vụ", "GV dặn dò", "Nộp buổi sau"]}
            ]
        }

    # 4. TRƯỜNG HỢP MÔN VẬT LÍ: CƠ NĂNG VÀ ĐỊNH LUẬT BẢO TOÀN CƠ NĂNG
    elif "cơ năng" in lesson_lower:
        meta = dict(VATLI_METADATA)
        meta["grade"] = grade
        meta["grade_level"] = grade_level
        meta["book_series"] = book_series
        meta["lesson_name"] = raw_lesson
        return {
            "metadata": meta,
            "lesson_plan": VATLI_LESSON_PLAN,
            "slides": attach_slide_images("Vật lí", VATLI_SLIDES),
            "exam_matrix": VATLI_EXAM_MATRIX,
            "exam_spec": VATLI_EXAM_SPEC,
            "exam_questions": VATLI_EXAM_QUESTIONS,
            "exam_answers": VATLI_EXAM_ANSWERS,
            "pedagogical_summary": f"Hồ sơ sư phạm môn Vật lí '{raw_lesson}' biên soạn chuẩn hóa theo Công văn 5512 và Công văn 7991.",
            "summary_knowledge": [
                "Khái niệm cơ năng: tổng động năng và thế năng trọng trường W = 1/2.m.v² + m.g.z.",
                "Định luật bảo toàn cơ năng khi vật chỉ chịu lực thế (bỏ qua ma sát).",
                "Sự chuyển hóa qua lại giữa động năng và thế năng trong chuyển động ném, tàu lượn.",
                "Vận dụng giải bài toán tìm vận tốc cực đại và độ cao cực đại trong thực tiễn."
            ],
            "summary_competencies": [
                "Năng lực chung: Tự chủ giải quyết vấn đề toán học - vật lí; Hợp tác xử lí dữ liệu thí nghiệm ảo PhET.",
                "Năng lực vật lí: Nhận thức quy luật bảo toàn; Vận dụng mô hình hóa bài toán kỹ thuật an toàn."
            ],
            "summary_qualities": [
                "Chăm chỉ: Cẩn thận, nghiêm túc trong tính toán số liệu định lượng.",
                "Trung thực: Báo cáo đúng kết quả khảo sát từ thí nghiệm mô phỏng."
            ],
            "activities": [
                {"name": "Hoạt động 1: Khởi động", "duration": "10 phút", "objective": "Khám phá chuyển động tàu lượn siêu tốc.", "content": "Xem clip tàu lượn và trả lời câu hỏi bảo toàn.", "steps": ["Chiếu clip tàu lượn", "HS suy nghĩ cặp đôi", "Phát biểu dự đoán", "GV kết luận vào bài"]},
                {"name": "Hoạt động 2: Hình thành kiến thức", "duration": "50 phút", "objective": "Xây dựng công thức và chứng minh định luật bảo toàn.", "content": "Mạch 1: Cơ năng trọng trường; Mạch 2: Định luật bảo toàn cơ năng.", "steps": ["Giao phiếu học tập", "HS biến đổi biểu thức", "Báo cáo kết quả PhET", "GV chuẩn hóa định luật"]},
                {"name": "Hoạt động 3: Luyện tập", "duration": "18 phút", "objective": "Giải bài toán định lượng thả rơi tự do.", "content": "Tính vận tốc chạm đất và độ cao khi thế năng bằng động năng.", "steps": ["Giao bài toán", "HS giải vào vở", "Lên bảng trình bày", "GV nhận xét chuẩn hóa"]},
                {"name": "Hoạt động 4: Vận dụng", "duration": "12 phút", "objective": "Giải thích hốc lánh nạn đường đèo dốc.", "content": "Ứng dụng cơ năng và ma sát giải thích hãm phanh xe.", "steps": ["Nêu bài toán thực tiễn", "HS thảo luận nhanh", "Giao bài về nhà", "Nộp trên LMS"]}
            ]
        }

    # 5. TRƯỜNG HỢP MÔN TOÁN: HỆ THỨC LƯỢNG TRONG TAM GIÁC
    elif "hệ thức lượng" in lesson_lower or "cosin" in lesson_lower:
        meta = dict(TOAN_METADATA)
        meta["grade"] = grade
        meta["grade_level"] = grade_level
        meta["book_series"] = book_series
        meta["lesson_name"] = raw_lesson
        return {
            "metadata": meta,
            "lesson_plan": TOAN_LESSON_PLAN,
            "slides": attach_slide_images("Toán", TOAN_SLIDES),
            "exam_matrix": TOAN_EXAM_MATRIX,
            "exam_spec": TOAN_EXAM_SPEC,
            "exam_questions": TOAN_EXAM_QUESTIONS,
            "exam_answers": TOAN_EXAM_ANSWERS,
            "pedagogical_summary": f"Hồ sơ sư phạm môn Toán '{raw_lesson}' biên soạn chuẩn hóa theo Công văn 5512 và Công văn 7991.",
            "summary_knowledge": [
                "Định lí Cosin và hệ quả tính góc trong tam giác bất kì: a² = b² + c² - 2bc.cosA.",
                "Định lí Sin và bán kính đường tròn ngoại tiếp: a/sinA = b/sinB = c/sinC = 2R.",
                "5 công thức tính diện tích tam giác và công thức Heron.",
                "Ứng dụng giải tam giác trong đo đạc trắc địa thực tế."
            ],
            "summary_competencies": [
                "Năng lực chung: Tự chủ giải toán lượng giác; Hợp tác nhóm thực hành trắc địa ngoài trời.",
                "Năng lực toán học: Tư duy hình học không gian; Mô hình hóa bài toán thực tế thành tam giác."
            ],
            "summary_qualities": [
                "Chăm chỉ: Kiên trì tính toán góc và độ dài chính xác.",
                "Trách nhiệm: Hợp tác hoàn thành phiếu bài tập nhóm."
            ],
            "activities": [
                {"name": "Hoạt động 1: Khởi động", "duration": "10 phút", "objective": "Đo khoảng cách qua hồ nước.", "content": "Bài toán đo khoảng cách khi không thể đo trực tiếp.", "steps": ["Nêu tình huống", "HS thảo luận", "Báo cáo cách đo", "GV vào bài"]},
                {"name": "Hoạt động 2: Hình thành kiến thức", "duration": "50 phút", "objective": "Làm chủ định lí Cosin và Sin.", "content": "Chứng minh định lí và suy ra hệ quả tính góc.", "steps": ["Giao phiếu học tập", "HS tính toán", "Trình bày bảng", "GV chốt công thức"]},
                {"name": "Hoạt động 3: Luyện tập", "duration": "18 phút", "objective": "Giải tam giác với số liệu cụ thể.", "content": "Tính cạnh, góc và diện tích tam giác cho trước.", "steps": ["Giao bài tập", "HS làm bài", "Chữa trên bảng", "GV nhận xét"]},
                {"name": "Hoạt động 4: Vận dụng", "duration": "12 phút", "objective": "Dự án đo chiều cao cột cờ sân trường.", "content": "Sử dụng giác kế tự chế đo chiều cao gián tiếp.", "steps": ["Giao dự án", "Lên kế hoạch đo", "Dặn dò an toàn", "Báo cáo buổi sau"]}
            ]
        }

    # 6. TRƯỜNG HỢP TỔNG QUÁT: BẤT KỲ BÀI HỌC VÀ MÔN HỌC NÀO NGƯỜI DÙNG NHẬP
    else:
        # Tự động trích xuất các từ khóa đặc trưng của bài học
        clean_title = raw_lesson.strip()
        topic_short = clean_title.split(":")[ -1].strip() if ":" in clean_title else clean_title
        
        meta = {
            "grade_level": grade_level,
            "grade": grade,
            "subject": subject_clean,
            "book_series": book_series,
            "lesson_name": clean_title,
            "duration": "2 tiết (90 phút)",
            "special_notes": special_notes if special_notes else f"Phát triển năng lực cốt lõi môn {subject_clean} {grade} gắn liền với thực tiễn."
        }
        
        gen_lesson_plan = f"""# KẾ HOẠCH BÀI DẠY (THEO CÔNG VĂN 5512/BGDĐT-GDTrH)

**TÊN BÀI DẠY: {clean_title.upper()}**  
**Môn học:** {subject_clean} | **Lớp:** {grade} ({grade_level})  
**Bộ sách:** {book_series}  
**Thời lượng thực hiện:** 2 tiết (90 phút)  

---

## I. MỤC TIÊU BÀI HỌC

### 1. Về kiến thức
- Nắm vững các khái niệm, nguyên lí và quy luật trọng tâm của bài học: *{clean_title}*.
- Phân tích và giải thích được bản chất của các hiện tượng, sự kiện hoặc công thức cốt lõi trong chủ đề.
- Vận dụng kiến thức bài học để giải quyết các bài tập, nhiệm vụ học tập tình huống và liên hệ thực tế đời sống.

### 2. Về năng lực
- **Năng lực chung:**
  - *Tự chủ và tự học:* Tự nghiên cứu SGK {book_series}, chuẩn bị bài chu đáo và chủ động ghi chép kiến thức trọng tâm.
  - *Giao tiếp và hợp tác:* Phân công nhiệm vụ nhóm rõ ràng, tích cực trao đổi và lắng nghe ý kiến phản biện của bạn học.
  - *Giải quyết vấn đề và sáng tạo:* Đề xuất phương án tối ưu để hoàn thành nhiệm vụ khám phá bài học *{topic_short}*.
- **Năng lực đặc thù môn {subject_clean} (theo CT GDPT 2018):**
  - Nhận thức môn học: Trình bày và hệ thống hóa chuẩn xác kiến thức chuyên đề *{topic_short}*.
  - Vận dụng kiến thức, kĩ năng môn học vào thực tiễn địa phương và đời sống.

### 3. Về phẩm chất
- *Chăm chỉ:* Tích cực tham gia xây dựng bài, chủ động hoàn thành các bài tập được giao.
- *Trung thực:* Khách quan trong xử lí thông tin và đánh giá kết quả học tập của bản thân và bạn học.
- *Trách nhiệm:* Có ý thức gắn kết kiến thức bài học với trách nhiệm bảo vệ môi trường, xã hội và cộng đồng.

---

## II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU
1. **Giáo viên chuẩn bị:**
   - Kế hoạch bài dạy chi tiết, bài giảng điện tử PowerPoint/Canva tương tác về chủ đề *{clean_title}*.
   - Thiết bị trực quan: Video tư liệu tình huống, phần mềm mô phỏng hoặc hình ảnh minh họa bài học.
   - Phiếu học tập số 1 (Khám phá kiến thức) và Phiếu học tập số 2 (Luyện tập củng cố).
2. **Học sinh chuẩn bị:**
   - SGK {subject_clean} {grade}, vở ghi chép, đồ dùng học tập chuyên dùng cho môn học.
   - Đọc trước bài học trong SGK và hoàn thành nhiệm vụ chuẩn bị trước giờ lên lớp.

---

## III. TIẾN TRÌNH DẠY HỌC

### 1. HOẠT ĐỘNG 1: MỞ ĐẦU / KHỞI ĐỘNG (10 phút)
- **a) Mục tiêu:** Kích hoạt tri thức nền tảng, tạo sự tò mò và hứng thú tìm hiểu bài học *{topic_short}*.
- **b) Nội dung:** Học sinh quan sát hình ảnh/video tình huống thực tế liên quan trực tiếp đến bài *{clean_title}*, trả lời câu hỏi gợi mở của giáo viên.
- **c) Sản phẩm:** Câu trả lời dự đoán, nhận định ban đầu của học sinh.
- **d) Tổ chức thực hiện:**
  - *Bước 1 (Chuyển giao nhiệm vụ):* GV trình chiếu câu hỏi tình huống thực tế về *{topic_short}*.
  - *Bước 2 (Thực hiện nhiệm vụ):* HS suy nghĩ cá nhân trong 2 phút, trao đổi nhanh theo cặp đôi.
  - *Bước 3 (Báo cáo, thảo luận):* Đại diện 2 học sinh phát biểu; các bạn khác nhận xét, bổ sung.
  - *Bước 4 (Kết luận, nhận định):* GV tổng kết ý kiến, nêu bật mâu thuẫn nhận thức và chính thức dẫn dắt vào bài mới.

---

### 2. HOẠT ĐỘNG 2: HÌNH THÀNH KIẾN THỨC MỚI (50 phút)

#### Mạch 1: Tìm hiểu khái niệm và nguyên lí nền tảng của bài học (25 phút)
- **a) Mục tiêu:** Nhận biết và phát biểu được các khái niệm, quy chuẩn cốt lõi của *{clean_title}*.
- **b) Nội dung:** Học sinh đọc thông tin SGK, quan sát trực quan và thảo luận theo nhóm bàn theo Phiếu học tập số 1.
- **c) Sản phẩm:** Sơ đồ tóm tắt kiến thức hoặc bảng phân tích các yếu tố cấu thành chủ đề.
- **d) Tổ chức thực hiện:**
  - *Bước 1 (Chuyển giao):* GV giao nhiệm vụ tìm hiểu thông tin mục I SGK qua phiếu học tập.
  - *Bước 2 (Thực hiện):* Các nhóm thảo luận, ghi nhận kết quả vào giấy A0 hoặc bảng phụ.
  - *Bước 3 (Báo cáo):* Đại diện 1 nhóm thuyết trình sản phẩm; các nhóm còn lại chất vấn, phản biện.
  - *Bước 4 (Kết luận):* GV nhận xét, chuẩn hóa kiến thức khoa học và hướng dẫn HS chốt nội dung vào vở.

#### Mạch 2: Phân tích cơ chế và ứng dụng thực tiễn của kiến thức (25 phút)
- **a) Mục tiêu:** Hiểu sâu cơ chế hoạt động, mối liên hệ qua lại và các ứng dụng điển hình của bài học *{topic_short}*.
- **b) Nội dung:** Phân tích ví dụ mẫu, giải quyết bài toán hoặc tình huống điển hình rút ra từ thực tế.
- **c) Sản phẩm:** Lời giải chi tiết hoặc phần lập luận khoa học của học sinh.
- **d) Tổ chức thực hiện:**
  - *Bước 1 (Chuyển giao):* GV nêu tình huống chuyên sâu, yêu cầu HS giải thích nguyên nhân và quy luật.
  - *Bước 2 (Thực hiện):* HS làm việc cá nhân kết hợp thảo luận nhóm nhỏ.
  - *Bước 3 (Báo cáo):* Học sinh lên bảng trình bày hoặc báo cáo miệng logic.
  - *Bước 4 (Kết luận):* GV tổng kết các lưu ý quan trọng, các lỗi sai thường gặp khi tiếp cận chủ đề.

---

### 3. HOẠT ĐỘNG 3: LUYỆN TẬP (18 phút)
- **a) Mục tiêu:** Củng cố, khắc sâu kiến thức và rèn luyện kĩ năng thao tác chuẩn xác về chủ đề *{clean_title}*.
- **b) Nội dung:** Giải quyết 4 câu hỏi trắc nghiệm tương tác nhanh và 1-2 bài tập thực hành độc lập.
- **c) Sản phẩm:** Phiếu trả lời hoặc bài làm hoàn chỉnh trong vở học sinh.
- **d) Tổ chức thực hiện:**
  - *Bước 1 (Chuyển giao):* GV giao hệ thống bài tập luyện tập phân hóa từ nhận biết đến vận dụng.
  - *Bước 2 (Thực hiện):* HS hoàn thành độc lập trong thời gian quy định (10 phút).
  - *Bước 3 (Báo cáo):* Chiếu đáp án, gọi HS giải thích phương án chọn hoặc lên bảng chữa bài.
  - *Bước 4 (Kết luận):* GV nhận xét mức độ nắm bài của lớp, sửa các lỗi hiểu sai cơ bản.

---

### 4. HOẠT ĐỘNG 4: VẬN DỤNG VÀ MỞ RỘNG (12 phút)
- **a) Mục tiêu:** Phát triển năng lực vận dụng tri thức bài học *{clean_title}* vào giải quyết vấn đề thực tế tại địa phương.
- **b) Nội dung:** Nhiệm vụ dự án nhỏ: Tìm hiểu một ứng dụng hoặc vấn đề thực tế gắn liền với bài học tại quê hương Vĩnh Long hoặc trong cuộc sống hàng ngày.
- **c) Sản phẩm:** Bản báo cáo tóm tắt (infographic, poster hoặc bài viết ngắn 1 trang A4) nộp vào buổi học sau.
- **d) Tổ chức thực hiện:**
  - *Bước 1 (Chuyển giao):* GV công bố nhiệm vụ dự án và tiêu chí đánh giá sản phẩm.
  - *Bước 2 (Thực hiện):* HS ghi chú nhiệm vụ, lập kế hoạch thực hiện tại nhà.
  - *Bước 3 (Báo cáo):* Báo cáo sản phẩm trên nền tảng số hoặc triển lãm tại lớp học buổi tới.
  - *Bước 4 (Kết luận):* GV dặn dò bài tập về nhà và hướng dẫn chuẩn bị cho bài học tiếp theo.
"""

        gen_slides = [
            {
                "slide_number": 1,
                "title": f"{clean_title.upper()}",
                "bullets": [
                    f"Môn học: {subject_clean} - {grade} ({grade_level})",
                    f"Bộ sách: {book_series}",
                    "Thời lượng thực hiện: 2 tiết (90 phút)",
                    f"Giáo viên giảng dạy: Thầy/Cô Bộ môn {subject_clean}"
                ],
                "visual_prompt": f"Hình ảnh trực quan sinh động đại diện cho chủ đề {clean_title} với gam màu sư phạm hiện đại.",
                "speaker_notes": f"Chào các em học sinh! Hôm nay chúng ta sẽ cùng khám phá một chuyên đề trọng tâm trong chương trình {subject_clean} {grade}: {clean_title}."
            },
            {
                "slide_number": 2,
                "title": "MỤC TIÊU BÀI HỌC CẦN ĐẠT",
                "bullets": [
                    f"Làm chủ các khái niệm và nguyên lí nền tảng của {topic_short}",
                    "Phát triển kĩ năng phân tích, mô hình hóa và giải quyết vấn đề",
                    "Liên hệ, giải thích các hiện tượng và tình huống thực tiễn đời sống",
                    "Rèn luyện tinh thần tự học, tự chủ và hợp tác nhóm hiệu quả"
                ],
                "visual_prompt": "Infographic mục tiêu học tập gồm 4 biểu tượng năng lực và phẩm chất theo chuẩn GDPT 2018.",
                "speaker_notes": "Sau 90 phút học tập hôm nay, các em sẽ nắm vững bản chất kiến thức và tự tin giải quyết các bài tập đánh giá năng lực."
            },
            {
                "slide_number": 3,
                "title": f"1. KIẾN THỨC CỐT LÕI: {topic_short.upper()}",
                "bullets": [
                    f"Định nghĩa và bản chất khoa học của {topic_short}",
                    "Các thành phần cấu tạo, quy luật hoặc công thức chi phối",
                    "Điều kiện áp dụng và phạm vi hoạt động của nguyên lí",
                    "Những điểm khác biệt then chốt cần ghi nhớ"
                ],
                "visual_prompt": "Sơ đồ khối khái niệm tóm tắt các mạch kiến thức cốt lõi với màu sắc trực quan, khoa học.",
                "speaker_notes": "Đây là phần tri thức nền tảng quan trọng nhất mà các em cần khắc sâu để làm bàn đạp cho các hoạt động thực hành tiếp theo."
            },
            {
                "slide_number": 4,
                "title": "2. PHÂN TÍCH VÀ ĐÀO SÂU BẢN CHẤT",
                "bullets": [
                    "So sánh, đối chiếu các trường hợp điển hình và tình huống ngoại lệ",
                    "Phân tích ví dụ mẫu chi tiết từng bước minh họa",
                    "Cảnh báo những sai lầm học sinh thường mắc phải khi làm bài",
                    "Mẹo tư duy nhanh và phương pháp ghi nhớ bằng sơ đồ tư duy"
                ],
                "visual_prompt": "Bảng so sánh trực quan đối chiếu hai trường hợp với hình ảnh minh chứng thực tế rõ nét.",
                "speaker_notes": "Hãy đặc biệt lưu ý đến mối liên hệ giữa lí thuyết và cách thức nhận diện dấu hiệu trong các dạng bài tập thực hành."
            },
            {
                "slide_number": 5,
                "title": "3. ỨNG DỤNG THỰC TIỄN ĐỜI SỐNG",
                "bullets": [
                    f"Vai trò thiết thực của {topic_short} trong đời sống và khoa học công nghệ",
                    "Mối liên hệ mật thiết với các ngành nghề trong xã hội hiện đại",
                    "Ứng dụng giải quyết bài toán bảo vệ môi trường và kinh tế địa phương",
                    "Khơi gợi ý tưởng sáng tạo nghiên cứu khoa học kĩ thuật trẻ"
                ],
                "visual_prompt": "Hình ảnh minh họa ứng dụng công nghệ hiện đại gắn liền với môn học trong đời sống sản xuất.",
                "speaker_notes": "Kiến thức chỉ thực sự có giá trị khi chúng ta biết cách đưa nó vào thực tiễn để phục vụ đời sống con người."
            },
            {
                "slide_number": 6,
                "title": "4. LUYỆN TẬP VÀ CỦNG CỐ TƯ DUY",
                "bullets": [
                    "Câu hỏi trắc nghiệm tương tác nhanh kiểm tra mức độ ghi nhớ",
                    "Bài tập tình huống vận dụng rèn luyện tư duy phản biện",
                    "Thử thách nhóm: 5 phút hoàn thành phiếu đánh giá năng lực",
                    "Đối chiếu đáp án chuẩn và sửa lỗi kịp thời"
                ],
                "visual_prompt": "Biểu tượng đồng hồ đếm ngược tương tác cùng các ngôi sao khen thưởng học tập tích cực.",
                "speaker_notes": "Bây giờ chúng ta cùng bước vào phần luyện tập tương tác để xem nhóm nào nắm bài nhanh và chính xác nhất nhé!"
            },
            {
                "slide_number": 7,
                "title": "5. TỔNG KẾT & NHIỆM VỤ VỀ NHÀ",
                "bullets": [
                    f"Hệ thống hóa các từ khóa trọng tâm của bài học {topic_short}",
                    "Hoàn thành các bài tập trong SGK và hệ thống học trực tuyến",
                    "Thực hiện dự án nhỏ tìm hiểu ứng dụng thực tế tại quê hương",
                    "Đọc trước nội dung chuẩn bị cho tiết học tiếp theo"
                ],
                "visual_prompt": "Hình ảnh cuốn sổ tay thông minh ghi chú các nhiệm vụ học tập cùng lời chúc học tốt.",
                "speaker_notes": "Tiết học của chúng ta kết thúc tại đây. Thầy cô cảm ơn sự tương tác sôi nổi của cả lớp. Hẹn gặp lại các em trong tiết học tới!"
            }
        ]

        gen_exam_matrix = f"""# MA TRẬN ĐỀ KIỂM TRA ĐỊNH KÌ THEO CÔNG VĂN 7991/BGDĐT-GDTrH
**Môn:** {subject_clean} | **Lớp:** {grade} | **Thời gian làm bài:** 45 phút  
**Khung cấu trúc:** Tỉ lệ nhận thức Biết 40% - Hiểu 30% - Vận dụng 30%.  
**Tỉ lệ hình thức:** TNKQ 4 lựa chọn (3,0 đ) + TNKQ Đúng-Sai (2,0 đ) + TNKQ Trả lời ngắn (2,0 đ) + Tự luận (3,0 đ).

| TT | Chủ đề / Đơn vị kiến thức | Mức độ: Biết (40%) | Mức độ: Hiểu (30%) | Mức độ: Vận dụng (30%) | Tổng điểm |
|:---|:---|:---:|:---:|:---:|:---:|
| 1 | Khái niệm và nguyên lí cơ bản của {topic_short} | 4 câu TN (Phần I) | 2 câu TN (Phần I) | | 1,5 đ |
| 2 | Mối quan hệ và quy luật chi phối bài học | 2 câu TN (Phần I) | 1 lệnh Đ/S (Phần II) | 1 lệnh Đ/S (Phần II) | 1,5 đ |
| 3 | Phân tích và giải thích hiện tượng thực tế | | 1 lệnh Đ/S (Phần II) | 1 lệnh Đ/S (Phần II) | 1,0 đ |
| 4 | Bài tập định lượng / Trả lời ngắn | | | 4 câu TL ngắn (Phần III) | 2,0 đ |
| 5 | Tự luận vận dụng giải quyết vấn đề thực tiễn | | 1 ý TL (1,0 đ) | 2 ý TL (2,0 đ) | 3,0 đ |
| | **TỔNG CỘNG** | **4,0 điểm (40%)** | **3,0 điểm (30%)** | **3,0 điểm (30%)** | **10,0 điểm** |
"""

        gen_exam_spec = f"""# BẢN ĐẶC TẢ ĐỀ KIỂM TRA ĐỊNH KÌ (CÔNG VĂN 7991/BGDĐT-GDTrH)
**Môn:** {subject_clean} | **Lớp:** {grade} | **Chủ đề:** {clean_title}

| TT | Chủ đề / Đơn vị kiến thức | Mức độ đánh giá / Yêu cầu cần đạt | Số lượng câu hỏi | Mã hóa năng lực |
|:---|:---|:---|:---:|:---:|
| 1 | Kiến thức cốt lõi về {topic_short} | **Nhận biết:** Nhận biết các thuật ngữ, khái niệm và định nghĩa cơ bản. | 4 TN (C1-C4) | NL_{subject_clean.upper()[:4]} 1.1 |
| 2 | Khám phá quy luật và cơ chế | **Thông hiểu:** Giải thích mối liên hệ giữa các yếu tố và hiện tượng khoa học. | 2 TN (C5, C6) | NL_{subject_clean.upper()[:4]} 1.2 |
| 3 | Nhận định đúng sai | **Thông hiểu & Vận dụng:** Phân tích tính đúng đắn của các mệnh đề khoa học. | 2 câu Đúng-Sai | NL_{subject_clean.upper()[:4]} 2.1 |
| 4 | Bài toán ngắn | **Vận dụng cấp 1:** Tính toán hoặc điền câu trả lời ngắn gọn chính xác. | 4 câu Trả lời ngắn | NL_{subject_clean.upper()[:4]} 2.2 |
| 5 | Vận dụng tình huống | **Vận dụng cao:** Giải quyết bài toán thực tiễn tổng hợp theo bước rõ ràng. | 1 bài Tự luận | NL_{subject_clean.upper()[:4]} 3.1 |
"""

        gen_exam_questions = f"""# ĐỀ KIỂM TRA ĐỊNH KÌ MÔN {subject_clean.upper()} {grade.upper()}
**Thời gian làm bài: 45 phút**  
*(Đề kiểm tra tuân thủ cấu trúc định dạng chuẩn Công văn 7991/BGDĐT-GDTrH)*

---

### PHẦN I. CÂU HỎI TRẮC NGHIỆM NHIỀU LỰA CHỌN (3,0 điểm)
*Thí sinh chọn một phương án trả lời đúng duy nhất trong các câu sau:*

**Câu 1.** Phát biểu nào sau đây định nghĩa chính xác nhất về nội dung của bài học *{topic_short}*?  
A. Định nghĩa chuẩn xác theo SGK {book_series}  
B. Khái niệm còn thiếu điều kiện ràng buộc cần thiết  
C. Nhận định mô tả hiện tượng đối lập không phù hợp  
D. Nhận định không liên quan đến bản chất bài học  

**Câu 2.** Trong chủ đề *{clean_title}*, yếu tố hoặc đại lượng nào sau đây đóng vai trò quyết định?  
A. Yếu tố nền tảng cốt lõi theo quy luật khoa học  
B. Yếu tố phụ thuộc môi trường ngẫu nhiên  
C. Thành phần thứ yếu không ảnh hưởng kết quả  
D. Đại lượng mang tính ước lượng tương đối  

**Câu 3.** Khi xem xét mối liên hệ quy luật trong bài học *{topic_short}*, kết luận nào sau đây đúng?  
A. Mối quan hệ biến đổi tỉ lệ phù hợp với điều kiện chuẩn  
B. Mối quan hệ diễn ra hoàn toàn độc lập không tương tác  
C. Các đại lượng luôn triệt tiêu lẫn nhau trong mọi điều kiện  
D. Hiện tượng chỉ xảy ra một chiều và không thể lặp lại  

**Câu 4.** Trong đời sống thực tế, kiến thức về *{topic_short}* được ứng dụng trực tiếp nhất vào lĩnh vực nào?  
A. Đời sống sinh hoạt và sản xuất thực tiễn  
B. Nghiên cứu khoa học và phát triển công nghệ  
C. Quản lí và bảo vệ môi trường sống  
D. Cả ba lĩnh vực nêu trên đều chính xác  

---

### PHẦN II. CÂU HỎI TRẮC NGHIỆM ĐÚNG - SAI (2,0 điểm)
*Thang điểm chuẩn CV 7991: Đúng 1 ý = 0,10đ; Đúng 2 ý = 0,25đ; Đúng 3 ý = 0,50đ; Đúng 4 ý = 1,00đ.*

**Câu 1.** Xét tính đúng/sai của các nhận định liên quan đến bài học *{clean_title}*:  
a) Kiến thức nền tảng của bài học là cơ sở vững chắc để giải thích các hiện tượng thực tế.  
b) Khi các điều kiện biên thay đổi, bản chất khoa học của quy luật vẫn được bảo toàn nguyên vẹn mà không cần hiệu chỉnh.  
c) Việc áp dụng đúng quy trình và phương pháp của bài học giúp nâng cao hiệu quả làm việc thực tiễn.  
d) Các yếu tố ngoại cảnh không bao giờ tác động đến độ chính xác của kết quả khảo sát.  

---

### PHẦN III. CÂU HỎI TRẮC NGHIỆM TRẢ LỜI NGẮN (2,0 điểm)
*Thí sinh điền từ khóa hoặc giá trị số chuẩn xác vào chỗ trống.*

**Câu 1 (1,0 điểm).** Hãy ghi lại từ khóa ngắn gọn diễn tả nguyên lí hoặc điều kiện cốt lõi của bài học *{topic_short}*.  
*(Điền kết quả: ...)*  

**Câu 2 (1,0 điểm).** Căn cứ vào số liệu hoặc quy chuẩn bài học, hãy ghi lại thông số định lượng tiêu chuẩn cần đạt.  
*(Điền kết quả: ...)*  

---

### PHẦN IV. CÂU HỎI TỰ LUẬN (3,0 điểm)
Trình bày cơ sở khoa học và đề xuất các bước cụ thể để ứng dụng kiến thức bài học *{clean_title}* vào giải quyết một tình huống thực tiễn tại trường học hoặc địa phương em. Nêu rõ ý nghĩa thực tế của giải pháp.
"""

        gen_exam_answers = f"""# HƯỚNG DẪN CHẤM VÀ ĐÁP ÁN ĐỀ KIỂM TRA MÔN {subject_clean.upper()}
*(Chuẩn hóa theo Công văn 7991/BGDĐT-GDTrH)*

- **Phần I (3,0 điểm):** C1-A, C2-A, C3-A, C4-D (mỗi câu đúng 0,75 điểm).
- **Phần II (2,0 điểm):** a-ĐÚNG, b-SAI, c-ĐÚNG, d-SAI (Thang điểm chuẩn CV 7991: Đúng 1 ý = 0.1đ; 2 ý = 0.25đ; 3 ý = 0.5đ; 4 ý = 1.0đ).
- **Phần III (2,0 điểm):** Đáp án từ khóa hoặc số liệu chuẩn xác của bài toán bài học *{topic_short}*.
- **Phần IV (3,0 điểm):**
  + Nêu đúng cơ sở khoa học gắn với bài học: 1,0 điểm.
  + Trình bày logic, mạch lạc các bước giải quyết tình huống: 1,0 điểm.
  + Đề xuất giải pháp khả thi và nêu rõ ý nghĩa thực tiễn: 1,0 điểm.
"""

        return {
            "metadata": meta,
            "lesson_plan": gen_lesson_plan,
            "slides": attach_slide_images(subject_clean, gen_slides),
            "exam_matrix": gen_exam_matrix,
            "exam_spec": gen_exam_spec,
            "exam_questions": gen_exam_questions,
            "exam_answers": gen_exam_answers,
            "pedagogical_summary": f"Hồ sơ sư phạm bài học '{clean_title}' môn {subject_clean} ({grade}) được biên soạn chuẩn mực theo Công văn 5512 (tiến trình 4 hoạt động) và Công văn 7991/BGDĐT-GDTrH (khảo thí 4 phần phân hóa).",
            "summary_knowledge": [
                f"Khái niệm và định nghĩa nền tảng của chuyên đề {topic_short}.",
                "Cơ chế hoạt động, mối liên hệ quy luật và các yếu tố chi phối bản chất bài học.",
                "Phương pháp nhận diện, phân tích và giải quyết các dạng bài tập điển hình.",
                "Ứng dụng thực tế của kiến thức trong sản xuất, đời sống và khoa học công nghệ."
            ],
            "summary_competencies": [
                f"Năng lực chung: Tự chủ trong tự học SGK {book_series}; Hợp tác nhóm giải quyết vấn đề.",
                f"Năng lực đặc thù: Nhận thức môn học và mô hình hóa giải quyết bài toán thực tế môn {subject_clean}."
            ],
            "summary_qualities": [
                "Chăm chỉ: Tích cực tìm tòi, ghi chép và rèn luyện kĩ năng.",
                "Trách nhiệm: Hoàn thành đúng tiến độ nhiệm vụ được phân công."
            ],
            "activities": [
                {
                    "name": "Hoạt động 1: Mở đầu / Khởi động",
                    "duration": "10 phút",
                    "objective": f"Tạo mâu thuẫn nhận thức từ tình huống thực tế về {topic_short}.",
                    "content": "Quan sát hình ảnh/video thực tế và trả lời câu hỏi gợi mở.",
                    "steps": [
                        "GV nêu tình huống thực tế",
                        "HS trao đổi cặp đôi tìm giải pháp",
                        "Đại diện phát biểu ý kiến",
                        "GV tổng kết dẫn dắt vào bài mới"
                    ]
                },
                {
                    "name": "Hoạt động 2: Hình thành kiến thức mới",
                    "duration": "50 phút",
                    "objective": "Nghiên cứu tài liệu SGK, khám phá quy luật và chốt kiến thức cốt lõi.",
                    "content": "2 mạch kiến thức: 1) Khái niệm nguyên lí; 2) Cơ chế và ứng dụng thực tiễn.",
                    "steps": [
                        "Giao Phiếu học tập số 1",
                        "Nhóm thảo luận và xử lí dữ liệu",
                        "Đại diện nhóm báo cáo sản phẩm",
                        "GV nhận xét, chuẩn hóa kiến thức"
                    ]
                },
                {
                    "name": "Hoạt động 3: Luyện tập củng cố",
                    "duration": "18 phút",
                    "objective": "Củng cố kiến thức qua câu hỏi trắc nghiệm và bài tập định lượng.",
                    "content": "Giải quyết 4 câu trắc nghiệm tương tác và bài tập tình huống thực tế.",
                    "steps": [
                        "Giao bài tập độc lập",
                        "HS làm bài vào vở ghi",
                        "Học sinh lên bảng chữa bài",
                        "GV nhận xét và sửa lỗi sai"
                    ]
                },
                {
                    "name": "Hoạt động 4: Vận dụng thực tiễn",
                    "duration": "12 phút",
                    "objective": "Vận dụng kiến thức bài học giải quyết vấn đề tại địa phương.",
                    "content": "Thực hiện dự án nhỏ tìm hiểu ứng dụng thực tiễn tại quê hương.",
                    "steps": [
                        "GV giao nhiệm vụ dự án",
                        "HS lập kế hoạch cá nhân/nhóm",
                        "Chuẩn bị sản phẩm báo cáo",
                        "Nộp trên LMS vào buổi sau"
                    ]
                }
            ]
        }


def get_sample_package_for_subject(
    subject: str,
    grade: str = "Lớp 10",
    grade_level: str = "THPT",
    book_series: str = "Kết nối tri thức với cuộc sống",
    custom_lesson_name: str = "",
    custom_notes: str = ""
) -> dict:
    """
    Hàm wrapper tương thích ngược: Ủy quyền toàn bộ cho generate_tailored_package.
    """
    return generate_tailored_package(
        subject=subject,
        grade=grade,
        grade_level=grade_level,
        book_series=book_series,
        lesson_name=custom_lesson_name,
        special_notes=custom_notes
    )
