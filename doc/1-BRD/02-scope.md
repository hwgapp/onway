# Scope

## In Scope - Phase 1

- Customer Super App cho Ride và Food.
- Driver App cho Ride và Food.
- Admin/CMS cho region, rollout, pricing/policy, driver, Food catalog, complaint/dispute, fraud/risk tối thiểu và audit.
- Backend/API cho marketplace core, matching, pricing recommendation, payment proof, evidence, chat, P0 push notification cho job/payment/chat/lock, account/activation và policy config.
- Ride: xe máy và ô tô; tài xế chỉ active sau xác minh bắt buộc.
- Ride pricing P0: platform đề xuất một final price; customer không thỏa thuận/tăng/giảm giá thủ công; driver Accept/Reject giá hệ thống đưa ra.
- Food: target outlet list ban đầu, brand/canonical menu, outlet override, order flow khách chuyển tiền trực tiếp cho tài xế rồi tài xế đặt món.
- P0 payment: bank transfer/QR trực tiếp Customer -> Driver, payment proof bắt buộc.
- Region: quốc gia, thành phố, vùng phục vụ trong thành phố, Admin polygon tool, service/vehicle availability, lifecycle Planned/Pilot/Active/Paused/Closed.
- Complaint/dispute và fraud/risk tối thiểu: tiếp nhận khiếu nại, evidence, risk status, manual/admin lock, auto-lock tạm thời theo rule cấu hình được và audit trail.
- Driver onboarding và platform usage fee/subscription launch package.

## Out Of Scope - Phase 1

- COD, tiền mặt, OnePAY/payment gateway, wallet, escrow hoặc Onway-held order payment cho Ride/Food.
- Ride customer price negotiation/manual offer.
- Food delivery fee negotiation.
- Merchant App bắt buộc.
- Driver Mission, Community Truth, AI OCR/menu extraction production, AI Restaurant Lifecycle production.
- Trust Engine đầy đủ và Trust-based privileges.
- Referral rewards production.
- Quảng cáo trong app.
- Corporate Ride, grocery, parcel delivery, shopping, cross-border.
- Onway Credits, tiền ảo, loyalty program chính xác, leaderboard/season/team challenge/streak.
- Insurance, bank guarantee, escrow.

## Later Phases

- Merchant App miễn phí, cập nhật menu/trạng thái/giờ mở cửa và nhận đơn sớm.
- Ride priority bonus/surge hoặc cơ chế khuyến khích tài xế sau khi có dữ liệu match rate P0.
- Mission Engine, Community Truth Engine và AI Operations Engine.
- Referral khách/tài xế sau core launch.
- Ads: Sponsored Restaurant, Sponsored Brand, Sponsored Search Result, Sponsored Mission, driver ads hoặc contextual advertising.
- Merchant Premium/value-added service nếu được chốt.
- Mở rộng Hà Nội, Đà Nẵng, các khu vực khác tại Việt Nam và đa quốc gia.
- Trust levels cho Customer/Driver, gamification XP/Level/Badge/Mission.

## Non-Goals

- BRD không chốt ngôn ngữ lập trình, database, API chi tiết, cloud, AI provider hoặc cấu trúc mã nguồn.
- Onway không chủ động markup giá món để hưởng chênh lệch.
- Onway không quay lại mô hình commission cho Ride/Food trong scope hiện tại.
- P0 không tối ưu mọi năng lực AI; chỉ cần dữ liệu/audit/evidence đủ sạch để mở rộng.
