# Korean Vocab Farm V4 (lớp chuyển động, xây trên V3)

Chạy: để `Korean_Vocab_Farm_V4.html` cạnh thư mục `assets/`, bấm đúp để mở. Khóa dữ liệu vẫn là `hanvocab.v1`. V3 không bị ghi đè.

## Đã nâng cấp (khối `<style id="v4">` và `<script id="v4js">`)
- Nông trại: mặt trời tỏa sáng, 3 đám mây trôi ở 3 tốc độ, chim bay, bướm bay quỹ đạo cong, cỏ đung đưa trong gió, parallax nhẹ khi cuộn (assets/scene: cloud, bird, sun).
- Mascot: các trạng thái idle (thở), walk, run, work, celebrate, surprise, encourage, hello, happy, sad, sleep (chữ Z bay). Có bong bóng thoại tiếng Việt, chạm vào để tương tác, tự làm việc ngẫu nhiên mỗi 9-16 giây khi ở nông trại.
- Vật nuôi: mỗi loài có kiểu chuyển động riêng, idle ngẫu nhiên, chạm vào thì phản ứng, có tiếng kêu dạng chữ và hạt sáng.
- Cây: cây chín phát sáng nhấp nhẹ, cây bệnh rung, thu hoạch có hạt sáng.
- Boss: thở khi idle, thanh HP giảm mượt, hộp thưởng bật mở có hạt sáng.
- UI: nút có phản hồi nhấn/hover, chuyển trang mờ dần, XP bay về thanh trạng thái, pháo hạt khi lên cấp.
- Hiệu năng: không dùng thư viện ngoài (không GSAP), dừng animation khi ẩn tab, giảm hạt và ẩn chim/bướm trên máy yếu hoặc điện thoại, hỗ trợ prefers-reduced-motion, tự quay về emoji nếu thiếu assets.

## Chưa làm (cần các vòng sau)
Vẽ lại SVG theo từng khung (chân, cánh, hàm) cho mascot/vật nuôi/boss; cối xay gió quay và nước giếng gợn sóng (cần tách cánh quạt khỏi windmill.svg); phân tách 5 giai đoạn cây mới; làm lại thẻ từ vựng, cửa hàng, bản đồ; âm thanh mới.

## Kiểm thử đã chạy
Mở bằng Chromium headless (màn 420x860): không lỗi JS, bật giao diện nông trại có đủ 8 lớp môi trường, chuyển qua các tab không lỗi, bấm mascot hoạt động, localStorage chỉ có khóa `hanvocab.v1`. Lỗi duy nhất là Google Fonts không tải được trong môi trường không có mạng (V3 cũng có).
Chưa kiểm thủ công: từng chế độ học, mua đồ, boss, import/export, backup/restore (logic V3 không bị chỉnh nên dự kiến giữ nguyên, nhưng cần bạn thử).
