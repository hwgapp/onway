# Raw Notes

Ghi nhanh ý tưởng, yêu cầu thô, link tham khảo, đối thủ, ghi chú họp.

Không cần format đẹp. Khi đủ thông tin, Codex sẽ tổng hợp sang BRD/PRD.

## 2026-09-23

- App có 2 chức năng chính: ride hailing + food delivery.
- Platform mục tiêu: iOS, Android, Web app, Admin/CMS, Backend/API.
- Mục tiêu release: Production đầy đủ.
- Monetization: user sẽ update chi tiết sau.
- Backend: user định hướng NestJS modular, sẽ mô tả chi tiết sau.
- User cung cấp pasted business note: "ONWAY - TÀI LIỆU YÊU CẦU NGHIỆP VỤ", version 0.5, updated 2026-09-11. Nội dung đã được tổng hợp vào `doc/1-BRD/**`, `doc/2-PRD/**` ở mức inventory, và open questions.
- User cung cấp pasted technical note: "ONWAY - Architecture Decisions", version 0.2, updated 2026-09-11. Nội dung đã được tổng hợp vào `doc/3-TECHNICAL/**`, technical decisions và open questions.

## 2026-09-24

- User cung cấp logo Onway:
  - SVG: `/Users/vod/Documents/ONW/design/logo.svg`
  - PNG: `/Users/vod/Documents/ONW/design/logo.png`
  - Logo source: 4493 x 1300, transparent background.
  - Brand red: `#E22240`; brand charcoal: `#302F2F` / `#2F2E2E`.
  - Đã tổng hợp vào `doc/4-DESIGN/**`.
- User trả lời thêm:
  - Chưa cần tạo code skeleton/scaffold.
  - Ưu đãi tài xế `1.000.000 VND` kết thúc theo tiêu chí nào là phần marketing, để sau.
  - Phí hồ sơ `500.000 VND` future thu lúc nộp hồ sơ.
  - Ride payment timing: customer chuyển khoản trước khi tài xế đến.
  - Ride negotiation: làm luôn trong P0; customer offer một lần, driver Accept/Reject, không Counter Offer.
  - P0 không thu phí cố định từ customer theo đơn/chuyến ngoài khoản thanh toán trực tiếp theo flow.
  - Tiêu chí launch success để xét ads tính sau.
- User chốt BRD v1.0:
  - Auto-lock driver làm theo đề xuất P0 tối giản: tự khóa tạm theo severe safety/fraud signal, nhiều complaint hợp lệ hoặc paid/no-show; cần reason/audit/review/unlock.
  - Ride negotiation: customer được tăng/giảm `+-10%` so với giá platform đề xuất; tài xế chỉ thấy final price.
  - HCM polygon không chốt bằng danh sách tĩnh trong BRD; P0 có Admin tool tạo/vẽ/chỉnh/publish polygon.
  - Chốt BRD v1.0 với Ride + Food launch cùng lúc tại TP.HCM; legal/marketing/future items là risk/deferred và không block BRD.
- User cập nhật sau G2:
  - Bỏ chức năng thỏa thuận giá Ride khỏi P0 để đơn giản.
  - Ride P0 dùng giá platform đề xuất/final price; customer không nhập tăng/giảm giá, driver chỉ Accept/Reject.
  - Giữ hình thức khách chuyển khoản/QR trực tiếp cho tài xế; không dùng OnePAY/payment gateway/escrow trong P0.
  - Các vấn đề gian lận/tranh chấp từ direct transfer sẽ được xử lý bằng SOP vận hành sau.
- User chấp nhận toàn bộ default G3 do Codex đề xuất:
  - Payment proof: driver bấm "Đã nhận đủ tiền"; mismatch chuyển `Payment disputed`/SOP; chuyển thiếu/sai yêu cầu bổ sung trước.
  - Food: customer chuyển tiền món + phí giao; proposal trong app là source of truth; tăng giá cần chuyển thêm; timeout proposal 5 phút cấu hình được; chưa có tip.
  - Polygon: tạo/sửa/pause/resume/publish, không hard delete; chặn overlap cùng service/vehicle; status Planned/Pilot/Active/Paused/Closed đủ; destination ngoài polygon có warning.
  - Auto-lock: paid/no-show, 3 complaint hợp lệ/30 ngày, severe safety/fraud; payment dispute nếu lặp lại; lock đến khi admin xử lý, SLA 24h; thông báo lý do ngắn; appeal trong app; Super Admin + Risk/Fraud unlock.
  - RBAC/release: role hiện tại đủ; push cơ bản cho job/payment/chat/lock; chat 1 ảnh/lần; rating 5 sao + tag; log event + ops dashboard cơ bản; legal/privacy chi tiết là risk trước G4/legal review.
