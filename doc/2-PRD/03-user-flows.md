# User Flows

## Core Flows

### UF-001 - Customer Ride Request To Completed Trip

- Goal: Customer đặt chuyến Ride trong active region, được match driver, thanh toán trực tiếp và hoàn tất chuyến.
- Entry: Customer app home -> Ride.
- Steps:
  1. Customer nhập pickup/dropoff và chọn vehicle type.
  2. App kiểm tra pickup/start nằm trong active region; dropoff có thể ngoài region nếu policy cho phép.
  3. Hệ thống hiển thị Recommended Price/final platform price.
  4. Customer xác nhận đặt Ride theo giá hệ thống đưa ra; P0 không có customer price negotiation/manual offer.
  5. Matching Engine gửi offer theo wave cho driver đủ điều kiện.
  6. Driver thấy final platform price rồi Accept hoặc Reject; driver không Counter Offer.
  7. First valid accept wins.
  8. Customer và driver chat/gọi trực tiếp nếu cần.
  9. Customer thanh toán trực tiếp cho driver bằng bank transfer/QR trước khi driver đến.
  10. Driver bấm "Đã nhận đủ tiền" rồi mới đi/tiếp tục đến điểm đón theo policy; P0 không yêu cầu driver nhập số tiền đã nhận ở case thường.
  11. Nếu driver báo chưa nhận tiền hoặc proof mâu thuẫn, service chuyển `Payment disputed` và xử lý theo SOP/manual review.
  12. Nếu customer chuyển thiếu/sai tiền, app ưu tiên yêu cầu bổ sung trước khi mở dispute.
  13. Payment proof được upload/ghi nhận trước mốc driver đến/pickup theo policy.
  14. Driver/customer hoàn tất trip lifecycle.
- Success: Ride completed, final platform price/evidence/state/audit saved, rating/report available.
- Failure/edge: outside service region, drivers reject/timeout, no driver, customer cancel before match, payment proof missing/rejected, driver does not confirm received money, complaint raised. Fraud/dispute details follow ops SOP, not gateway verification in P0.
- Analytics: ride_request_created, ride_recommended_price_shown, ride_match_started, ride_driver_offer_sent, ride_driver_accepted, ride_completed, ride_cancelled, payment_proof_uploaded.

### UF-002 - Customer Food Order To Delivered

- Goal: Customer đặt Food, thanh toán trực tiếp cho driver, driver đặt món tại outlet và giao thành công.
- Entry: Customer app home -> Food.
- Steps:
  1. Customer chọn brand/outlet/menu item và delivery address.
  2. App kiểm tra outlet/start trong active region; destination có thể ngoài region nếu policy cho phép.
  3. App hiển thị item price estimate, Recommended Delivery Fee và estimated total gồm tiền món + phí giao customer cần chuyển cho driver.
  4. Customer xác nhận mức delivery fee hệ thống đề xuất; P0 không negotiation.
  5. Matching Engine tìm driver theo wave.
  6. Driver Accept/Reject; không Counter Offer.
  7. Sau khi matched, app hiển thị dynamic VietQR/bank transfer info của driver nếu có.
  8. Customer chuyển tiền trực tiếp cho driver, bấm "Đã chuyển tiền" và upload payment proof.
  9. Driver tự kiểm tra/tro chuyện với customer và bấm "Đã nhận đủ tiền".
  10. Driver đến outlet, đặt món, trả tiền nhà hàng, nhận món và giao cho customer.
  11. Customer/driver hoàn tất order lifecycle.
- Success: Food delivered, order state/evidence/audit saved, rating/report available.
- Failure/edge: outlet closed, item unavailable, no driver, payment proof missing, driver does not confirm money received, order change needed, customer refuses after driver ordered, complaint/dispute. Fraud/dispute details follow ops SOP, not gateway verification in P0.
- Analytics: food_order_created, food_delivery_fee_shown, food_match_started, food_driver_accepted, food_payment_proof_uploaded, food_driver_money_received, food_order_placed_at_outlet, food_delivered.

### UF-003 - Food Price Or Item Change At Outlet

- Goal: Xử lý khi driver phát hiện giá/tình trạng món khác so với app.
- Entry: Driver Food active job -> change needed.
- Steps:
  1. Driver có thể gọi customer để trao đổi, nhưng proposal trong app là source of truth.
  2. Driver nhập thay đổi thực tế: item unavailable, price changed, modifier changed hoặc note khác.
  3. App gửi proposal cho customer với timeout mặc định 5 phút, cấu hình được.
  4. Customer Accept hoặc Reject trước khi driver mua món bị ảnh hưởng.
  5. Nếu giá tăng, customer phải chuyển bổ sung cho driver trước khi driver mua phần bị ảnh hưởng.
  6. Hệ thống lưu decision, evidence và audit trail.
- Success: Accepted change updates current order snapshot; rejected change follows cancellation/partial fulfillment policy to be detailed under Food dispute policy.
- Failure/edge: customer unreachable, proposal timeout after default 5 minutes, driver already bought before confirmation, dispute.
- Analytics: food_change_proposed, food_change_accepted, food_change_rejected, food_change_timeout.

### UF-004 - Driver Onboarding And Activation

- Goal: Driver đăng ký, xác minh và được activate sau khi hoàn thành điều kiện bắt buộc.
- Entry: Driver app -> Sign up.
- Steps:
  1. Driver nhập phone, verify OTP qua ViHAT/Firebase custom token flow.
  2. Driver tạo profile và gửi giấy tờ theo vehicle/service.
  3. Driver nộp platform usage fee proof/reference nếu thuộc launch package.
  4. Admin/Driver Ops review identity/documents.
  5. Finance Ops verify platform fee proof cho khoản Onway thu.
  6. Driver Ops/Super Admin activate driver khi đủ điều kiện.
- Success: Driver status Activated, service/vehicle eligibility set, driver có thể online.
- Failure/edge: document rejected, platform fee proof rejected, missing bank info, risk hold, legal/background requirement not met.
- Analytics: driver_signup_started, driver_otp_verified, driver_documents_submitted, platform_fee_proof_uploaded, driver_activated, driver_rejected.

### UF-005 - Complaint And Manual Fraud/Dispute Review

- Goal: Tiếp nhận complaint, phân biệt service issue/fraud, xử lý bằng chứng và human decision.
- Entry: Customer/Driver app report flow hoặc Admin/Operator case creation.
- Steps:
  1. User tạo complaint gắn với Ride/Food service ref.
  2. App thu category, description và evidence nếu có.
  3. Support Operator/Risk Analyst review complaint.
  4. Nếu cần, case chuyển sang fraud/dispute lifecycle.
  5. Risk/Fraud Analyst thu thập evidence, yêu cầu driver/customer response.
  6. Auto-lock có thể khóa tạm driver theo paid/no-show, severe safety/fraud signal, 3 complaint hợp lệ trong 30 ngày hoặc repeated payment dispute nếu threshold policy được kích hoạt.
  7. Driver nhận thông báo lý do ngắn, không lộ evidence nhạy cảm, và có thể gửi appeal trong app.
  8. Auto-lock kéo dài đến khi admin xử lý; SLA review mục tiêu là 24 giờ.
  9. Super Admin hoặc Risk/Fraud Analyst có quyền unlock theo policy; Driver Ops chỉ đề xuất trong case vận hành.
  10. Human decision: confirmed/rejected/appeal/finalized.
  11. Nếu có lỗi/trách nhiệm, nguyên tắc business là bên nào sai bên đó chịu; Onway là phần mềm kết nối, pending terms/legal.
- Success: Complaint/case resolved, decision/audit saved, risk status/manual lock/auto-lock updated nếu policy cho phép.
- Failure/edge: missing evidence, conflicting evidence, user appeal, legal hold, case timeout.
- Analytics: complaint_created, complaint_escalated_to_fraud, fraud_case_created, fraud_decision_finalized, risk_status_changed.

### UF-006 - Admin Region And Policy Rollout

- Goal: Admin cấu hình region, service/vehicle availability và policy guardrail để rollout P0 an toàn.
- Entry: Admin Portal -> Region/Policy.
- Steps:
  1. Ops Admin/Super Admin tạo country/city/region.
  2. Admin tạo/vẽ/chỉnh polygon trên bản đồ.
  3. Admin cấu hình lifecycle Planned/Pilot/Active/Paused/Closed.
  4. Admin cấu hình service, vehicle, operating time và pricing/policy guardrails.
  5. Admin publish config version; không hard delete polygon trong P0, chỉ pause/close/publish version mới.
  6. System chặn publish nếu polygon overlap cùng service/vehicle trong cùng city.
  7. System audit mọi thay đổi.
- Success: Customer/driver apps áp dụng service availability theo active config; destination ngoài polygon có warning riêng cho customer/driver nếu policy cho phép đi ngoài vùng.
- Failure/edge: invalid polygon, overlapping polygon same service/vehicle, publish conflict, rollback/manual republish needed.
- Analytics: admin_region_created, admin_region_published, policy_config_published, service_region_paused.

### UF-007 - Active Chat And Direct Call

- Goal: Customer và driver liên lạc trong active Ride/Food.
- Entry: Active Ride/Food screen -> Chat/Call.
- Steps:
  1. User mở chat room của active service.
  2. User gửi text/image; P0 cho 1 ảnh mỗi message, image upload vào private media storage.
  3. WebSocket gửi message/delivered/read events.
  4. Room đóng khi service kết thúc theo policy.
  5. Chat retention P0 là 1 tuần, trừ message/evidence được preserve cho complaint/dispute.
- Success: Participant nhận được message, reconnect/refetch xử lý sequence gap.
- Failure/edge: upload failed, user offline, room closed, unauthorized participant.
- Analytics: chat_message_sent, chat_image_uploaded, chat_room_closed, direct_call_started.
