# Business Brief

## Tóm Tắt

Onway là nền tảng gọi xe và giao đồ ăn tại Việt Nam theo mô hình marketplace nhiều bên, AI-native, cộng đồng cùng vận hành, 0% commission và hạn chế giữ tiền giao dịch.

Phạm vi launch hiện tại tập trung Ride Hailing và Food Delivery tại TP. Hồ Chí Minh, ưu tiên các region nội thành được phê duyệt. Sau HCM, hướng mở rộng là Hà Nội, Đà Nẵng, các khu vực khác tại Việt Nam, rồi đa quốc gia trong tương lai.

Nguồn: business note "ONWAY - TÀI LIỆU YÊU CẦU NGHIỆP VỤ", version 0.5, cập nhật 2026-09-11.

## Vấn Đề

- Nền tảng gọi xe/giao đồ ăn hiện hữu thường lấy commission làm giảm thu nhập tài xế và doanh thu nhà hàng.
- Giá món có thể bị markup hoặc thiếu minh bạch giữa giá món, phí giao hàng và chi phí nền tảng.
- Mở rộng dữ liệu nhà hàng, menu, vận hành và hỗ trợ khách hàng theo cách thủ công dễ làm chi phí tăng tuyến tính theo quy mô.
- Khiếu nại, fraud, sai lệch giá/menu và vận hành ngoại lệ cần audit trail rõ ràng để xử lý công bằng.

## Giải Pháp

- Ride/Food marketplace với 0% commission trên giá chuyến xe, phí giao hàng, giá trị món ăn, thu nhập tài xế và doanh thu nhà hàng.
- Money-light: tiền giao dịch Ride/Food không đi qua Onway trong P0; khách chuyển khoản/QR trực tiếp cho tài xế và upload payment proof.
- AI-first và cộng đồng tài xế hỗ trợ vận hành sau core launch; P0 cần dữ liệu, audit và evidence đủ sạch để mở rộng.
- Admin quản lý region, service availability, pricing guardrail, food catalog, driver, complaint, fraud/risk và policy config.

## User Chính

- Customer: nhóm ban đầu gồm nhân viên văn phòng và sinh viên đại học/cao đẳng.
- Driver: cung cấp Ride/Food, nhận tiền trực tiếp từ khách, đăng ký và xác minh trước khi hoạt động.
- Merchant: nhà hàng/cửa hàng cung cấp món; Merchant App chưa bắt buộc trong giai đoạn Food ban đầu.
- Admin/Operator: quản lý cấu hình, rollout, dữ liệu Food, khiếu nại, fraud/risk và ngoại lệ.

## Giá Trị Khác Biệt

- Tài xế giữ 100% giá chuyến xe và phí giao hàng đã thống nhất.
- Nhà hàng trả 0% commission và Onway không chủ động markup giá món.
- Khách hàng thấy giá món và phí giao hàng riêng, minh bạch.
- Onway ưu tiên AI và cộng đồng để giảm bộ máy vận hành khi scale.
- P0 tránh wallet, escrow, payment gateway, cash/COD và Onway-held order payment cho Ride/Food.

## Business Model

- Doanh thu chính dự kiến từ phí sử dụng nền tảng/subscription của tài xế.
- Chương trình ra mắt: tài xế đóng `1.000.000 VND` trước kích hoạt cho 12 tháng, tặng thêm 6 tháng, tổng 18 tháng.
- Quảng cáo trong app và dịch vụ giá trị gia tăng là nguồn doanh thu tương lai, không thuộc giai đoạn ra mắt.
- Onway không thu commission trên Ride/Food và không hưởng chênh lệch markup giá món.
