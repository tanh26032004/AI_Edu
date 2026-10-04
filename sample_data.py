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
# HÀM THÍCH ỨNG ĐA MÔN HỌC (MULTI-SUBJECT ADAPTIVE ENGINE)
# ==============================================================================
def get_sample_package_for_subject(
    subject: str,
    grade: str = "Lớp 10",
    grade_level: str = "THPT",
    book_series: str = "Kết nối tri thức với cuộc sống",
    custom_lesson_name: str = "",
    custom_notes: str = ""
) -> dict:
    """
    Trả về bộ hồ sơ sư phạm chuẩn hóa tương ứng với môn học và lớp được chọn.
    """
    subject_clean = subject.strip()
    
    # 1. Trường hợp Môn Toán
    if "Toán" in subject_clean:
        meta = dict(TOAN_METADATA)
        meta["grade"] = grade
        meta["grade_level"] = grade_level
        meta["book_series"] = book_series
        if custom_lesson_name:
            meta["lesson_name"] = custom_lesson_name
        if custom_notes:
            meta["special_notes"] = custom_notes
            
        return {
            "metadata": meta,
            "lesson_plan": TOAN_LESSON_PLAN,
            "slides": attach_slide_images(subject_clean, TOAN_SLIDES),
            "exam_matrix": TOAN_EXAM_MATRIX,
            "exam_spec": TOAN_EXAM_SPEC,
            "exam_questions": TOAN_EXAM_QUESTIONS,
            "exam_answers": TOAN_EXAM_ANSWERS,
            "pedagogical_summary": f"Hồ sơ sư phạm môn Toán {grade} biên soạn bám sát chuẩn năng lực toán học CT GDPT 2018, trọn vẹn 4 hoạt động CV 5512 và đề khảo thí 4 phần chuẩn CV 7991."
        }
        
    # 2. Trường hợp Môn Ngữ văn
    elif "Văn" in subject_clean or "Ngữ văn" in subject_clean:
        lesson = custom_lesson_name if custom_lesson_name else "Đoạn trích: Đăm Săn chiến thắng Mtao Mxây (Sử thi Ê-đê)"
        meta = {
            "grade_level": grade_level,
            "grade": grade,
            "subject": "Ngữ văn",
            "book_series": book_series,
            "lesson_name": lesson,
            "duration": "2 tiết (90 phút)",
            "special_notes": custom_notes if custom_notes else "Phát triển năng lực tiếp nhận văn bản sử thi anh hùng, rèn luyện kĩ năng viết đoạn văn và cảm thụ thẩm mĩ."
        }
        
        van_lesson_plan = f"""# KẾ HOẠCH BÀI DẠY (THEO CÔNG VĂN 5512/BGDĐT-GDTrH)

**TÊN BÀI DẠY: {lesson.upper()}**  
**Môn học:** Ngữ văn | **Lớp:** {grade}  
**Bộ sách:** {book_series}  
**Thời lượng thực hiện:** 2 tiết (90 phút)  

---

## I. MỤC TIÊU BÀI HỌC

### 1. Về kiến thức
- Nhận biết và phân tích được các đặc trưng thi pháp của thể loại văn bản (cốt truyện, nhân vật, không gian, thời gian, người kể chuyện).
- Làm rõ vẻ đẹp ngoại hình, hành động và phẩm chất lí tưởng của nhân vật trung tâm trong bối cảnh cộng đồng.
- Phân tích nghệ thuật miêu tả, phóng đại, so sánh trùng điệp và ngôn ngữ giàu nhạc điệu, chất thơ của tác phẩm.

### 2. Về năng lực
- **Năng lực chung:** Tự chủ trong đọc hiểu văn bản; Hợp tác nhóm thảo luận về giá trị nhân văn; Giải quyết vấn đề sáng tạo.
- **Năng lực văn học (CT GDPT 2018):** Đọc diễn cảm, phân tích tâm lí nhân vật, viết đoạn văn nghị luận 150-200 chữ.

### 3. Về phẩm chất
- Bồi dưỡng lòng tự hào về di sản văn hóa tinh thần của các dân tộc Việt Nam; Khát vọng hòa bình, công lí.

---

## II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU
- GV: Giáo án, máy chiếu, video tư liệu văn hóa cồng chiêng, Phiếu học tập số 1 và 2.
- HS: Chuẩn bị bài theo SGK, vở ghi chép.

---

## III. TIẾN TRÌNH DẠY HỌC

### 1. HOẠT ĐỘNG 1: MỞ ĐẦU / KHỞI ĐỘNG (10 phút)
- **Mục tiêu:** Kích hoạt tri thức nền về hình tượng người anh hùng trong văn học dân gian.
- **Nội dung:** Xem video 1 phút về lễ hội buôn làng, nêu phẩm chất tiêu biểu của người anh hùng sử thi.

### 2. HOẠT ĐỘNG 2: HÌNH THÀNH KIẾN THỨC MỚI (50 phút)
- **Mạch 1: Đọc - Tìm hiểu chung:** Đọc diễn cảm phân vai, xác định vị trí đoạn trích và bố cục (20 phút).
- **Mạch 2: Khám phá vẻ đẹp nhân vật & Nghệ thuật:** Cảnh giao chiến và cảnh ăn mừng chiến thắng (30 phút).

### 3. HOẠT ĐỘNG 3: LUYỆN TẬP (18 phút)
- Viết đoạn văn ngắn phân tích một chi tiết nghệ thuật em tâm đắc nhất trong tác phẩm.

### 4. HOẠT ĐỘNG 4: VẬN DỤNG (12 phút)
- Thiết kế infographic giới thiệu vẻ đẹp văn hóa độc đáo của tác phẩm để quảng bá du lịch văn hóa vùng miền.
"""
        
        van_slides = [
            {
                "slide_number": 1,
                "title": f"BÀI HỌC: {lesson.upper()}",
                "bullets": [
                    f"Môn học: Ngữ văn - {grade} ({book_series})",
                    "Thời lượng: 2 tiết (90 phút)",
                    "Khám phá thiên sử thi anh hùng và vẻ đẹp cộng đồng bất hủ",
                    "Giáo viên hướng dẫn: Thầy/Cô Bộ môn Ngữ văn"
                ],
                "visual_prompt": "Bức tranh phong cảnh núi rừng Tây Nguyên bạt ngàn dưới ánh hoàng hôn hùng vĩ với nhà rông cổ kính.",
                "speaker_notes": "Chào các em! Hôm nay chúng ta sẽ cùng hòa mình vào không gian sử thi hào hùng với tiếng cồng chiêng rộn rã."
            },
            {
                "slide_number": 2,
                "title": "MỤC TIÊU CẦN ĐẠT CỦA BÀI HỌC",
                "bullets": [
                    "Nhận biết đặc trưng cốt truyện, nhân vật và người kể chuyện sử thi",
                    "Phân tích vẻ đẹp ngoại hình, tài năng và lí tưởng của người anh hùng",
                    "Khám phá nghệ thuật so sánh, phóng đại trùng điệp độc đáo",
                    "Bồi dưỡng tình yêu di sản văn hóa phi vật thể của dân tộc Việt Nam"
                ],
                "visual_prompt": "Infographic văn học với biểu tượng cuốn sách cổ mở ra, ngọn lửa trại bập bùng và chiếc cồng chiêng.",
                "speaker_notes": "Bài học này sẽ trang bị cho các em chìa khóa vạn năng để tiếp cận các tác phẩm sử thi anh hùng."
            },
            {
                "slide_number": 3,
                "title": "1. CHÂN DUNG NGƯỜI ANH HÙNG",
                "bullets": [
                    "Ngoại hình: Oai phong lẫm liệt, bắp chân to bằng cây xà ngang, mắt sáng như chim ghếch",
                    "Hành động: Nhanh nhẹn, quả cảm, múa khiên trên cao gió như bão",
                    "Phẩm chất: Trượng nghĩa, công bằng, đại diện cho khát vọng hòa bình của buôn làng",
                    "Sự hỗ trợ của Thần linh: Biểu trưng cho chân lí và sự đồng thuận của tự nhiên"
                ],
                "visual_prompt": "Hình tượng dũng sĩ trong trang phục truyền thống tay cầm khiên đồng và gươm sáng ngời giữa đại ngàn.",
                "speaker_notes": "Nghệ thuật phóng đại khắc họa sự tôn kính tột bậc của nhân dân đối với người thủ lĩnh anh minh."
            },
            {
                "slide_number": 4,
                "title": "2. CẢNH ĂN MỪNG CHIẾN THẮNG",
                "bullets": [
                    "Bữa tiệc cộng đồng hoan hỉ: Rượu cần tuôn chảy, chiêng cồng vang rền",
                    "Dân làng của kẻ bại trận tình nguyện theo về xây dựng buôn làng mới",
                    "Ý nghĩa: Chiến tranh kết thúc để mở ra kỉ nguyên ấm no, đoàn kết và sinh sôi",
                    "Âm vang tiếng chiêng ngân xa vượt qua sông núi bạt ngàn"
                ],
                "visual_prompt": "Cảnh toàn cảnh lễ hội ăn mừng với hàng trăm người nhảy múa quanh đống lửa lớn trước sân nhà rông.",
                "speaker_notes": "Đây là đỉnh cao nhân văn của sử thi: Hướng tới hòa bình, thống nhất và phồn thịnh."
            },
            {
                "slide_number": 5,
                "title": "3. TỔNG KẾT & Ý NGHĨA THỜI ĐẠI",
                "bullets": [
                    "Khát vọng chinh phục tự nhiên và xây dựng buôn làng giàu mạnh của cha ông",
                    "Bài học cho thế hệ trẻ: Tinh thần đoàn kết dân tộc, ý chí vượt khó vươn lên",
                    "Nhiệm vụ về nhà: Viết đoạn văn cảm nhận 150 chữ về một chi tiết em yêu thích nhất",
                    "Chúc các em học tốt môn Ngữ văn!"
                ],
                "visual_prompt": "Hình ảnh thế hệ trẻ nâng niu cuốn sách văn học di sản bên cạnh biểu tượng non sông Việt Nam tươi đẹp.",
                "speaker_notes": "Hãy luôn tự hào về cội nguồn văn hóa của dân tộc. Cảm ơn các em đã theo dõi bài học!"
            }
        ]
        
        van_exam_matrix = f"""# MA TRẬN ĐỀ KIỂM TRA ĐỊNH KÌ NGỮ VĂN {grade.upper()}
**Khung cấu trúc chuẩn CV 7991:** Tỉ lệ nhận thức Biết 40% - Hiểu 30% - Vận dụng 30%.  
**Tỉ lệ hình thức:** Đọc hiểu trắc nghiệm & tự luận ngắn (5,0 đ) + Viết đoạn văn nghị luận (5,0 đ).

| TT | Kĩ năng / Đơn vị kiến thức | Mức độ: Biết (40%) | Mức độ: Hiểu (30%) | Mức độ: Vận dụng (30%) | Tổng điểm |
|:---|:---|:---:|:---:|:---:|:---:|
| 1 | **Đọc hiểu văn bản văn học** (Ngữ liệu mở) | 4 câu TN (2,0 đ) | 2 câu TN/TL ngắn (1,5 đ) | 1 câu TL ngắn (1,5 đ) | **5,0 đ** |
| 2 | **Viết đoạn văn nghị luận** (Khoảng 200 chữ) | 0,5 đ (Hình thức) | 1,5 đ (Nội dung) | 3,0 đ (Sáng tạo, lí lẽ) | **5,0 đ** |
| | **TỔNG CỘNG** | **4,0 điểm (40%)** | **3,0 điểm (30%)** | **3,0 điểm (30%)** | **10,0 điểm** |
"""
        
        van_exam_spec = f"""# BẢN ĐẶC TẢ ĐỀ KIỂM TRA ĐỊNH KÌ NGỮ VĂN {grade.upper()} (CV 7991)
| TT | Kĩ năng | Đơn vị kiến thức | Yêu cầu cần đạt theo mức độ tư duy | Câu hỏi | Mã NL |
|:---|:---|:---|:---|:---:|:---:|
| 1 | Đọc hiểu | Thể loại & Ngôi kể | **Nhận biết:** Xác định thể loại, người kể chuyện, phương thức biểu đạt. | C1, C2 (TN) | NL_VAN 1.1 |
| 2 | Đọc hiểu | Biện pháp tu từ | **Nhận biết:** Chỉ ra biện pháp tu từ so sánh, phóng đại hoặc điệp từ ngữ. | C3, C4 (TN) | NL_VAN 1.2 |
| 3 | Đọc hiểu | Ý nghĩa chi tiết | **Thông hiểu:** Giải thích ý nghĩa của một hình ảnh biểu tượng trong văn bản. | C5 (TL ngắn) | NL_VAN 2.1 |
| 4 | Đọc hiểu | Thông điệp | **Vận dụng:** Rút ra bài học nhân sinh hoặc thông điệp có ý nghĩa sâu sắc. | C6 (TL ngắn) | NL_VAN 2.2 |
| 5 | Viết | Đoạn văn nghị luận | **Vận dụng cao:** Viết đoạn văn hoàn chỉnh phân tích nét đặc sắc của nhân vật. | Phần II (Tự luận) | NL_VAN 3.1 |
"""

        van_exam_questions = f"""# ĐỀ KIỂM TRA ĐỊNH KÌ MÔN NGỮ VĂN {grade.upper()}
**Thời gian làm bài: 45 phút**  
*(Đề kiểm tra tuân thủ cấu trúc định dạng chuẩn Công văn 7991/BGDĐT-GDTrH môn Ngữ văn)*

---

### PHẦN I. ĐỌC HIỂU (5,0 điểm)
*Đọc đoạn trích sau và trả lời các câu hỏi:*
> *"Buôn làng Đăm Săn đông vui như mở hội. Tôi tớ chật nơm chật luồng, bò ngựa đi nghẽn cả đường rừng. Tiếng cồng chiêng ngân vang vượt qua sông qua núi..."*

**Câu 1 (0,5 điểm).** Đoạn trích trên được viết theo thể loại văn học nào?  
A. Truyện cổ tích  
B. Sử thi anh hùng  
C. Truyền thuyết  
D. Thơ ngụ ngôn  

**Câu 2 (0,5 điểm).** Phương thức biểu đạt chính của đoạn trích là gì?  
A. Tự sự  
B. Biểu cảm  
C. Miêu tả  
D. Nghị luận  

**Câu 3 (0,5 điểm).** Biện pháp tu từ nào nổi bật nhất trong câu *"Buôn làng Đăm Săn đông vui như mở hội"*?  
A. Nhân hóa  
B. Ẩn dụ  
C. So sánh  
D. Hoán dụ  

**Câu 4 (0,5 điểm).** Hình ảnh *"bò ngựa đi nghẽn cả đường rừng"* nhằm khắc họa điều gì?  
A. Sự hoảng loạn của buôn làng  
B. Sự giàu có, trù phú và hùng mạnh của cộng đồng  
C. Cảnh săn bắn thú rừng  
D. Tình trạng giao thông thời xưa  

**Câu 5 (1,5 điểm).** Nêu ngắn gọn ý nghĩa của cảnh ăn mừng chiến thắng trong tâm thức của cư dân xưa?  
**Câu 6 (1,5 điểm).** Từ vẻ đẹp người anh hùng trong tác phẩm, em hãy rút ra một bài học về tinh thần trách nhiệm của thế hệ trẻ hôm nay đối với quê hương đất nước.

---

### PHẦN II. LÀM VĂN (5,0 điểm)
Viết một đoạn văn nghị luận xã hội (khoảng 200 chữ) bàn về ý nghĩa của lòng dũng cảm và tinh thần vượt khó trong cuộc sống hiện đại.
"""

        van_exam_answers = """# HƯỚNG DẪN CHẤM VÀ ĐÁP ÁN ĐỀ KIỂM TRA NGỮ VĂN
- Phần I: C1-B (0,5đ), C2-A (0,5đ), C3-C (0,5đ), C4-B (0,5đ).
  + C5 (1,5đ): Ca ngợi sự đoàn kết, ấm no và khát vọng hòa bình thịnh vượng.
  + C6 (1,5đ): Sống có lí tưởng cống hiến, dám dấn thân vì cộng đồng.
- Phần II: Viết đoạn văn 200 chữ (5,0đ): Đúng hình thức (0,5đ), Luận điểm xác đáng (3,5đ), Sáng tạo & chính tả (1,0đ).
"""

        return {
            "metadata": meta,
            "lesson_plan": van_lesson_plan,
            "slides": attach_slide_images(subject_clean, van_slides),
            "exam_matrix": van_exam_matrix,
            "exam_spec": van_exam_spec,
            "exam_questions": van_exam_questions,
            "exam_answers": van_exam_answers,
            "pedagogical_summary": f"Hồ sơ sư phạm môn Ngữ văn {grade} chuẩn mực CV 5512 với 4 hoạt động tiếp nhận văn bản và cấu trúc khảo thí Đọc hiểu - Viết chuẩn xác định dạng CV 7991."
        }

    # 3. Trường hợp Môn Vật lí
    elif "Vật lí" in subject_clean:
        meta = dict(VATLI_METADATA)
        meta["grade"] = grade
        meta["grade_level"] = grade_level
        meta["book_series"] = book_series
        if custom_lesson_name:
            meta["lesson_name"] = custom_lesson_name
        if custom_notes:
            meta["special_notes"] = custom_notes
            
        return {
            "metadata": meta,
            "lesson_plan": VATLI_LESSON_PLAN,
            "slides": attach_slide_images(subject_clean, VATLI_SLIDES),
            "exam_matrix": VATLI_EXAM_MATRIX,
            "exam_spec": VATLI_EXAM_SPEC,
            "exam_questions": VATLI_EXAM_QUESTIONS,
            "exam_answers": VATLI_EXAM_ANSWERS,
            "pedagogical_summary": f"Hồ sơ sư phạm môn Vật lí {grade} biên soạn chuẩn hóa theo Công văn 5512 và Công văn 7991/BGDĐT-GDTrH."
        }

    # 4. Trường hợp các môn học khác (Hóa học, KHTN, Tiếng Anh, Lịch sử, Địa lí, Sinh học, Tin học, GDCD...)
    else:
        # Lấy gợi ý bài học mặc định nếu người dùng chưa nhập
        preset = SUBJECT_PRESETS.get(subject_clean, {})
        default_lesson = preset.get("lesson_name", f"Chủ đề trọng tâm môn {subject_clean} - {grade}")
        lesson = custom_lesson_name if custom_lesson_name else default_lesson
        default_notes = preset.get("special_notes", f"Phát triển phẩm chất và năng lực đặc thù môn {subject_clean} theo Chương trình GDPT 2018.")
        notes = custom_notes if custom_notes else default_notes
        
        meta = {
            "grade_level": grade_level,
            "grade": grade,
            "subject": subject_clean,
            "book_series": book_series,
            "lesson_name": lesson,
            "duration": "2 tiết (90 phút)",
            "special_notes": notes
        }
        
        gen_lesson_plan = f"""# KẾ HOẠCH BÀI DẠY (THEO CÔNG VĂN 5512/BGDĐT-GDTrH)

**TÊN BÀI DẠY: {lesson.upper()}**  
**Môn học:** {subject_clean} | **Lớp:** {grade} ({grade_level})  
**Bộ sách:** {book_series}  
**Thời lượng thực hiện:** 2 tiết (90 phút)  

---

## I. MỤC TIÊU BÀI HỌC

### 1. Về kiến thức
- Nắm vững các khái niệm, quy luật và nguyên lí cốt lõi của bài học: *{lesson}*.
- Phân tích được mối liên hệ giữa lí thuyết môn học và các hiện tượng thực tế đời sống.
- Vận dụng kiến thức để giải thích hiện tượng và giải quyết các bài tập, nhiệm vụ học tập tình huống.

### 2. Về năng lực
- **Năng lực chung:**
  - *Tự chủ và tự học:* Tự nghiên cứu tài liệu SGK, hoàn thành phiếu học tập cá nhân.
  - *Giao tiếp và hợp tác:* Thảo luận nhóm sôi nổi, tôn trọng và tiếp thu ý kiến đóng góp của bạn học.
  - *Giải quyết vấn đề và sáng tạo:* Đề xuất các giải pháp khả thi trong các tình huống thực tiễn.
- **Năng lực đặc thù môn {subject_clean} (theo CT GDPT 2018):**
  - Nhận thức và vận dụng kiến thức, kĩ năng đặc thù của môn học để khám phá thế giới tự nhiên và xã hội.
  - Sử dụng thành thạo các công cụ học tập, phần mềm mô phỏng và phương tiện trực quan.

### 3. Về phẩm chất
- Rèn luyện tính chăm chỉ, trung thực trong học tập và tinh thần trách nhiệm với cộng đồng.

---

## II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU
- **Giáo viên:** Kế hoạch bài dạy, bài giảng điện tử PowerPoint/Canva, video tình huống thực tế, phiếu học tập số 1 và 2.
- **Học sinh:** SGK môn {subject_clean} {grade}, vở ghi chép, đồ dùng học tập theo yêu cầu bộ môn.

---

## III. TIẾN TRÌNH DẠY HỌC

### 1. HOẠT ĐỘNG 1: MỞ ĐẦU / KHỞI ĐỘNG (10 phút)
- **a) Mục tiêu:** Kích hoạt kiến thức nền tảng, tạo sự tò mò và hứng thú tìm hiểu chủ đề *{lesson}*.
- **b) Nội dung:** Học sinh quan sát hình ảnh/video thực tế và trả lời câu hỏi gợi mở do giáo viên nêu ra.
- **c) Sản phẩm:** Câu trả lời dự đoán, ý kiến ban đầu của học sinh.
- **d) Tổ chức thực hiện:** Chuyển giao nhiệm vụ ➔ Thực hiện cá nhân/cặp đôi ➔ Báo cáo thảo luận ➔ Giáo viên nhận định và dẫn dắt vào bài mới.

### 2. HOẠT ĐỘNG 2: HÌNH THÀNH KIẾN THỨC MỚI (50 phút)
- **Mạch 1: Tìm hiểu khái niệm và nguyên lí trọng tâm (25 phút):** Học sinh nghiên cứu thông tin SGK, thảo luận nhóm và đúc kết nội dung cốt lõi.
- **Mạch 2: Khám phá quy luật và ứng dụng thực tiễn (25 phút):** Thực hành giải quyết các câu hỏi khám phá theo phiếu học tập số 1.
- **Tổ chức thực hiện:** Đầy đủ 4 bước sư phạm: Chuyển giao ➔ Thực hiện nhóm ➔ Đại diện báo cáo ➔ GV kết luận chuẩn hóa kiến thức.

### 3. HOẠT ĐỘNG 3: LUYỆN TẬP (18 phút)
- **a) Mục tiêu:** Củng cố và khắc sâu kiến thức vừa học thông qua hệ thống bài tập trắc nghiệm và câu hỏi tự luận ngắn.
- **b) Nội dung:** Giải quyết 4 câu hỏi trắc nghiệm tương tác và 1 bài tập tình huống thực tế.
- **c) Sản phẩm:** Phiếu trả lời của học sinh; GV chữa bài và chốt đáp án đúng.

### 4. HOẠT ĐỘNG 4: VẬN DỤNG VÀ MỞ RỘNG (12 phút)
- **a) Mục tiêu:** Phát triển năng lực vận dụng kiến thức bài học vào đời sống thực tế tại địa phương.
- **b) Nội dung:** Nhiệm vụ dự án nhỏ: Tìm hiểu và viết báo cáo ngắn (1 trang A4) hoặc thiết kế poster về ứng dụng của chủ đề học tập trong thực tiễn.
- **c) Sản phẩm:** Báo cáo/Poster của học sinh nộp vào buổi học tiếp theo.
"""
        
        gen_slides = [
            {
                "slide_number": 1,
                "title": f"{lesson.upper()}",
                "bullets": [
                    f"Môn học: {subject_clean} - {grade} ({grade_level})",
                    f"Bộ sách: {book_series}",
                    "Thời lượng thực hiện: 2 tiết (90 phút)",
                    f"Giáo viên hướng dẫn: Thầy/Cô Bộ môn {subject_clean}"
                ],
                "visual_prompt": f"Hình ảnh trực quan sinh động minh họa cho chủ đề {lesson} với phong cách đồ họa hiện đại.",
                "speaker_notes": f"Chào các em học sinh! Hôm nay chúng ta sẽ cùng khám phá một chủ đề vô cùng thú vị và thiết thực trong chương trình {subject_clean} {grade}."
            },
            {
                "slide_number": 2,
                "title": "MỤC TIÊU BÀI HỌC CẦN ĐẠT",
                "bullets": [
                    "Nắm vững các khái niệm và nguyên lí nền tảng của bài học",
                    "Rèn luyện kĩ năng quan sát, phân tích và giải quyết vấn đề",
                    "Liên hệ và giải thích các hiện tượng thực tế trong đời sống",
                    "Phát triển năng lực tự học và tinh thần hợp tác nhóm"
                ],
                "visual_prompt": "Infographic mục tiêu học tập với 4 biểu tượng năng lực và phẩm chất phát triển toàn diện.",
                "speaker_notes": "Sau bài học này, các em sẽ tự tin làm chủ kiến thức và biết cách ứng dụng chúng vào các tình huống thực tiễn hàng ngày."
            },
            {
                "slide_number": 3,
                "title": "1. NỘI DUNG TRỌNG TÂM CỐT LÕI",
                "bullets": [
                    "Khái niệm và định nghĩa cơ bản",
                    "Cơ chế hoạt động và quy luật chi phối",
                    "Các yếu tố ảnh hưởng trực tiếp đến quá trình",
                    "Công thức hoặc nguyên tắc vận hành cần ghi nhớ"
                ],
                "visual_prompt": "Sơ đồ khối khái niệm tóm tắt các mạch kiến thức chính với màu sắc phân định rõ ràng.",
                "speaker_notes": "Đây là phần kiến thức nền tảng mà các em cần khắc sâu để làm bàn đạp cho các hoạt động thực hành tiếp theo."
            },
            {
                "slide_number": 4,
                "title": "2. PHÂN TÍCH VÀ MỞ RỘNG KIẾN THỨC",
                "bullets": [
                    "So sánh và phân biệt các trường hợp đặc biệt",
                    "Phân tích ví dụ điển hình minh họa từ thực tế",
                    "Lưu ý các lỗi sai thường gặp khi làm bài tập",
                    "Mẹo ghi nhớ nhanh kiến thức thông qua sơ đồ tư duy"
                ],
                "visual_prompt": "Bảng so sánh trực quan đối chiếu hai trường hợp với hình ảnh minh chứng thực tế.",
                "speaker_notes": "Hãy chú ý đến các chi tiết khác biệt nhỏ này, bởi chúng thường là trọng tâm trong các đề kiểm tra đánh giá năng lực."
            },
            {
                "slide_number": 5,
                "title": "3. ỨNG DỤNG THỰC TIỄN ĐỜI SỐNG",
                "bullets": [
                    "Vai trò của chủ đề học tập trong sản xuất và đời sống",
                    "Mối liên hệ với các vấn đề môi trường, kinh tế và xã hội",
                    "Định hướng nghề nghiệp liên quan đến chuyên đề này",
                    "Ý tưởng sáng tạo đổi mới xuất phát từ bài học"
                ],
                "visual_prompt": "Hình ảnh ứng dụng công nghệ hiện đại gắn liền với môn học trong đời sống thực tế.",
                "speaker_notes": "Kiến thức chỉ thực sự có ý nghĩa khi chúng ta mang nó ra phụng sự cuộc sống và giải quyết các bài toán thực tiễn."
            },
            {
                "slide_number": 6,
                "title": "4. LUYỆN TẬP VÀ CỦNG CỐ",
                "bullets": [
                    "Câu hỏi trắc nghiệm nhanh kiểm tra mức độ ghi nhớ",
                    "Bài tập tình huống rèn luyện tư duy phản biện",
                    "Thời gian thử thách nhóm: 5 phút hoàn thành phiếu",
                    "Cùng thảo luận và đối chiếu đáp án chuẩn"
                ],
                "visual_prompt": "Biểu tượng đồng hồ đếm ngược tương tác cùng các ngôi sao khen thưởng học tập tích cực.",
                "speaker_notes": "Bây giờ chúng ta cùng bước vào phần luyện tập tương tác để xem nhóm nào nắm bài nhanh và chính xác nhất nhé!"
            },
            {
                "slide_number": 7,
                "title": "5. TỔNG KẾT & NHIỆM VỤ VỀ NHÀ",
                "bullets": [
                    "Khắc sâu các từ khóa trọng tâm của bài học hôm nay",
                    "Hoàn thành các bài tập trong SGK và hệ thống LMS",
                    "Thực hiện nhiệm vụ dự án nhỏ tìm hiểu thực tế",
                    "Chuẩn bị bài mới cho tiết học tiếp theo"
                ],
                "visual_prompt": "Hình ảnh cuốn sổ tay thông minh ghi chú các nhiệm vụ học tập cùng lời chúc học tốt.",
                "speaker_notes": "Tiết học của chúng ta kết thúc tại đây. Thầy cô cảm ơn sự tương tác sôi nổi của các em. Hẹn gặp lại các em trong tiết học tới!"
            }
        ]
        
        gen_exam_matrix = f"""# MA TRẬN ĐỀ KIỂM TRA ĐỊNH KÌ THEO CÔNG VĂN 7991/BGDĐT-GDTrH
**Môn:** {subject_clean} | **Lớp:** {grade} | **Thời gian làm bài:** 45 phút  
**Khung cấu trúc:** Tỉ lệ nhận thức Biết 40% - Hiểu 30% - Vận dụng 30%.  
**Tỉ lệ hình thức:** TNKQ 4 lựa chọn (3,0 đ) + TNKQ Đúng-Sai (2,0 đ) + TNKQ Trả lời ngắn (2,0 đ) + Tự luận (3,0 đ).

| TT | Chủ đề / Đơn vị kiến thức | Mức độ: Biết (40%) | Mức độ: Hiểu (30%) | Mức độ: Vận dụng (30%) | Tổng điểm |
|:---|:---|:---:|:---:|:---:|:---:|
| 1 | Khái niệm và nguyên lí cơ bản | 4 câu TN (Phần I) | 2 câu TN (Phần I) | | 1,5 đ |
| 2 | Mối quan hệ và quy luật chi phối | 2 câu TN (Phần I) | 1 lệnh Đ/S (Phần II) | 1 lệnh Đ/S (Phần II) | 1,5 đ |
| 3 | Phân tích và giải thích hiện tượng | | 1 lệnh Đ/S (Phần II) | 1 lệnh Đ/S (Phần II) | 1,0 đ |
| 4 | Bài tập định lượng / Trả lời ngắn | | | 4 câu TL ngắn (Phần III) | 2,0 đ |
| 5 | Tự luận vận dụng giải quyết thực tế | | 1 ý TL (1,0 đ) | 2 ý TL (2,0 đ) | 3,0 đ |
| | **TỔNG CỘNG** | **4,0 điểm (40%)** | **3,0 điểm (30%)** | **3,0 điểm (30%)** | **10,0 điểm** |
"""
        
        gen_exam_spec = f"""# BẢN ĐẶC TẢ ĐỀ KIỂM TRA ĐỊNH KÌ (CÔNG VĂN 7991/BGDĐT-GDTrH)
**Môn:** {subject_clean} | **Lớp:** {grade}

| TT | Chủ đề / Đơn vị kiến thức | Mức độ đánh giá / Yêu cầu cần đạt | Số lượng câu hỏi | Mã hóa năng lực |
|:---|:---|:---|:---:|:---:|
| 1 | Kiến thức cốt lõi | **Nhận biết:** Nhận biết các thuật ngữ, khái niệm và định nghĩa cơ bản. | 4 TN (C1-C4) | NL_{subject_clean.upper()[:4]} 1.1 |
| 2 | Khám phá quy luật | **Thông hiểu:** Giải thích mối liên hệ giữa các yếu tố và hiện tượng. | 2 TN (C5, C6) | NL_{subject_clean.upper()[:4]} 1.2 |
| 3 | Nhận định đúng sai | **Thông hiểu & Vận dụng:** Phân tích tính đúng đắn của các mệnh đề khoa học. | 2 câu Đúng-Sai | NL_{subject_clean.upper()[:4]} 2.1 |
| 4 | Bài toán ngắn | **Vận dụng cấp 1:** Tính toán hoặc điền câu trả lời ngắn gọn chính xác. | 4 câu Trả lời ngắn | NL_{subject_clean.upper()[:4]} 2.2 |
| 5 | Vận dụng tình huống | **Vận dụng cao:** Giải quyết bài toán thực tiễn tổng hợp theo bước rõ ràng. | 1 bài Tự luận | NL_{subject_clean.upper()[:4]} 3.1 |
"""

        gen_exam_questions = f"""# ĐỀ KIỂM TRA ĐỊNH KÌ MÔN {subject_clean.upper()} {grade.upper()}
**Thời gian làm bài: 45 phút**  
*(Đề kiểm tra tuân thủ cấu trúc định dạng chuẩn Công văn 7991/BGDĐT-GDTrH)*

---

### PHẦN I. CÂU HỎI TRẮC NGHIỆM NHIỀU LỰA CHỌN (3,0 điểm)
*Thí sinh chọn một phương án đúng duy nhất.*

**Câu 1.** Khái niệm cơ bản nào sau đây đúng với nội dung bài học *{lesson}*?  
A. Khái niệm A chuẩn xác theo định nghĩa SGK  
B. Khái niệm B còn thiếu điều kiện ràng buộc  
C. Khái niệm C mô tả hiện tượng trái ngược  
D. Khái niệm D không liên quan đến bài học  

**Câu 2.** Đơn vị hoặc đại lượng đo lường đặc trưng của nội dung bài học là  
A. Đơn vị chuẩn trong hệ đo lường  
B. Đơn vị thứ nguyên dẫn xuất  
C. Chỉ số không thứ nguyên  
D. Giá trị ước tính tương đối  

**Câu 3.** Phát biểu nào sau đây diễn tả đúng quy luật vận động của hiện tượng?  
A. Hiện tượng biến đổi tỉ lệ nghịch với điều kiện môi trường  
B. Hiện tượng diễn ra ổn định khi không có tác nhân bên ngoài can thiệp  
C. Cả hai yếu tố luôn triệt tiêu lẫn nhau trong mọi điều kiện  
D. Quá trình chỉ xảy ra một chiều và không bao giờ phục hồi  

**Câu 4.** Trong thực tiễn đời sống, kiến thức của bài học được ứng dụng trực tiếp vào lĩnh vực nào?  
A. Công nghệ và đời sống thường ngày  
B. Sản xuất công nghiệp và nông nghiệp  
C. Y tế và bảo vệ môi trường  
D. Cả ba lĩnh vực trên đều đúng  

---

### PHẦN II. CÂU HỎI TRẮC NGHIỆM ĐÚNG - SAI (2,0 điểm)
*Thang điểm chuẩn CV 7991: Đúng 1 ý = 0,10đ; Đúng 2 ý = 0,25đ; Đúng 3 ý = 0,50đ; Đúng 4 ý = 1,00đ.*

**Câu 1.** Xét các mệnh đề liên quan đến chủ đề *{lesson}*:  
a) Mệnh đề 1: Kiến thức cơ bản là tiền đề giải thích các hiện tượng thực tế.  
b) Mệnh đề 2: Khi thay đổi thông số môi trường, kết quả sẽ hoàn toàn bất biến.  
c) Mệnh đề 3: Việc ứng dụng quy trình chuẩn giúp nâng cao hiệu suất làm việc.  
d) Mệnh đề 4: Các yếu tố phụ không làm ảnh hưởng đến độ tin cậy của kết quả.  

---

### PHẦN III. CÂU HỎI TRẮC NGHIỆM TRẢ LỜI NGẮN (2,0 điểm)
**Câu 1.** Hãy điền giá trị số hoặc từ khóa ngắn gọn thích hợp vào chỗ trống liên quan đến điều kiện nghiệm đúng của bài toán.  
*(Điền kết quả: ...)*  

**Câu 2.** Tính toán thông số kết quả dựa trên số liệu thực nghiệm chuẩn đã cho.  
*(Điền kết quả: ...)*  

---

### PHẦN IV. CÂU HỎI TỰ LUẬN (3,0 điểm)
Trình bày các bước phân tích và đề xuất giải pháp cho một tình huống thực tiễn gắn liền với bài học *{lesson}* tại địa phương. Nêu rõ cơ sở khoa học và ý nghĩa thực tế.
"""

        gen_exam_answers = f"""# HƯỚNG DẪN CHẤM VÀ ĐÁP ÁN ĐỀ KIỂM TRA MÔN {subject_clean.upper()}
- Phần I (3,0 đ): C1-A, C2-A, C3-B, C4-D (mỗi câu đúng 0,75 đ hoặc theo bareme đề).
- Phần II (2,0 đ): a-ĐÚNG, b-SAI, c-ĐÚNG, d-SAI (Thang điểm CV 7991: 0.1đ - 0.25đ - 0.5đ - 1.0đ).
- Phần III (2,0 đ): Đáp án từ khóa hoặc số liệu chuẩn xác của bài toán.
- Phần IV (3,0 đ):
  + Nêu đúng cơ sở khoa học: 1,0 đ
  + Trình bày logic các bước thực hiện: 1,0 đ
  + Liên hệ thực tế và đề xuất giải pháp khả thi: 1,0 đ
"""

        return {
            "metadata": meta,
            "lesson_plan": gen_lesson_plan,
            "slides": attach_slide_images(subject_clean, gen_slides),
            "exam_matrix": gen_exam_matrix,
            "exam_spec": gen_exam_spec,
            "exam_questions": gen_exam_questions,
            "exam_answers": gen_exam_answers,
            "pedagogical_summary": f"Hồ sơ sư phạm môn {subject_clean} ({grade}) được biên soạn chuẩn mực theo Công văn 5512 (4 hoạt động) và Công văn 7991/BGDĐT-GDTrH (đề thi 4 phần phân hóa)."
        }
