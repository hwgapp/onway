# Business Rules

| ID | Rule | Applies To | Source | Notes |
| --- | --- | --- | --- | --- |
| BP-001 | AI là lớp vận hành cốt lõi khi giúp giảm chi phí, tăng quy mô hoặc tăng chất lượng. | All | BRD v0.5 | P0 không yêu cầu mọi năng lực AI production. |
| BP-002 | AI xử lý trường hợp thông thường; con người xử lý ngoại lệ. | Ops/AI | BRD v0.5 | Human review khi rủi ro cao, bằng chứng mâu thuẫn hoặc pháp luật yêu cầu. |
| BP-003 | Khi công việc thực địa có thể làm an toàn bởi tài xế và xác minh độc lập, ưu tiên cộng đồng thay vì đội hiện trường lớn. | Ops/Future Mission | BRD v0.5 | Mission/Community Truth là future. |
| BP-004 | Onway thu 0% commission trên giá chuyến xe, phí giao hàng, giá trị món, thu nhập tài xế và doanh thu nhà hàng. | Monetization | BRD v0.5 | Đã chốt. |
| BP-005 | Tiền giao dịch Ride/Food không đi qua Onway trong phạm vi hiện tại. | Payment | BRD v0.5 | Ride: Customer -> Driver. Food: Customer -> Driver -> Merchant. |
| BP-006 | Nguồn doanh thu chính dự kiến là platform fee/subscription tài xế, quảng cáo sau launch và value-added services tương lai. | Monetization | BRD v0.5 | Ads không thuộc P0. |
| BP-007 | Onway không chủ động markup giá món. | Food/Pricing | BRD v0.5 | Sai lệch do dữ liệu cũ là quality issue, không phải markup. |
| BR-GEO-001 | Onway ra mắt thương mại tại TP. Hồ Chí Minh trước, sau đó Hà Nội, Đà Nẵng và khu vực khác. | Region | BRD v0.5 | MVP chỉ phục vụ Việt Nam. |
| BR-GEO-002 | Hệ thống phải hỗ trợ country, city và service region trong city. | Region/Admin | BRD v0.5 | Sẵn sàng multi-country, chưa cross-border. |
| BR-GEO-003 | Admin cấu hình service, vehicle, thời gian hoạt động/tạm dừng theo region. | Admin/Region | BRD v0.5 | P0. |
| BR-GEO-004 | Region kiểm tra điểm đón/trả, địa chỉ giao, vị trí tài xế và outlet. | Ride/Food/Matching | BRD v0.5 | Cần polygon active. |
| BR-GEO-005 | Region lifecycle tối thiểu: Planned, Pilot, Active, Paused, Closed. | Admin/Region | BRD v0.5 | P0. |
| BR-GEO-006 | Admin phải tạo/vẽ/chỉnh/publish polygon trên bản đồ và hệ thống xác định tọa độ có nằm trong polygon active hay không. | Admin/Region | BRD v0.5 + User 2026-09-24 | P0; không chốt bằng danh sách quận tĩnh trong BRD. |
| BR-GEO-007 | Chuyến/job có thể bắt đầu trong active region và kết thúc ngoài region nếu policy/pricing/matching cho phép. | Ride/Food/Region | User 2026-09-24 | Pickup/start hoặc outlet/driver start phải hợp lệ trong active region; destination ngoài region cần guardrail. |
| BR-COMM-001 | Khách và tài xế tự gọi trực tiếp bằng số điện thoại thật. | Customer/Driver | BRD v0.5 | MVP chưa ẩn số/gọi thoại in-app. |
| BR-COMM-002 | MVP có chat Customer-Driver trong active Ride/Food, hỗ trợ text và hình ảnh, retention 1 tuần. | Customer/Driver/Chat | BRD v0.5 | P0. |
| BR-RIDE-001 | Ride giai đoạn đầu hỗ trợ xe máy và ô tô. | Ride | BRD v0.5 | P0. |
| BR-RIDE-002 | Driver chỉ được active sau khi hoàn thành xác minh bắt buộc. | Driver/Ride/Food | BRD v0.5 | Hồ sơ cấu hình theo vehicle/service. |
| BR-RIDE-PRICE-001 | Onway cung cấp Recommended Price cho mỗi Ride request; đây là giá đề xuất, không bắt buộc. | Ride/Pricing | BRD v0.5 | AI/algorithm phải trong guardrail cấu hình. |
| BR-RIDE-PRICE-002 | P0 không có Ride price negotiation/manual offer: customer không nhập tăng/giảm giá so với giá platform đề xuất. | Ride/Pricing | User 2026-09-24 | D-024 supersedes D-007. |
| BR-RIDE-PRICE-003 | Driver chỉ thấy giá hệ thống đưa ra cho job và chỉ có thể Accept hoặc Reject; driver không gửi Counter Offer trong P0. | Ride/Pricing | User 2026-09-24 | Nếu driver reject hoặc timeout, matching tiếp tục theo PRD Ride chi tiết. |
| BR-PAY-RIDE-001 | P0 Ride chỉ hỗ trợ bank transfer/QR trực tiếp Customer -> Driver, payment proof bắt buộc. | Ride/Payment | BRD v0.5 + User 2026-09-24 | Khách chuyển khoản trước khi tài xế đến. |
| BR-PAY-RIDE-002 | P0 không hỗ trợ cash, COD, payment gateway, wallet, escrow hoặc Onway-held payment cho Ride. | Ride/Payment | BRD v0.5 | Đã chốt. |
| BR-PAY-RIDE-003 | Ride flow P0 phải hướng customer hoàn tất chuyển khoản/QR và payment proof trước mốc driver đến/pickup. | Ride/Payment | User 2026-09-24 | Enforcement/exception detail xử lý trong PRD Ride. |
| BR-PAY-RIDE-004 | Các gian lận/tranh chấp từ direct transfer Ride được xử lý bằng SOP vận hành, complaint/fraud lifecycle và audit; BRD/P0 không yêu cầu gateway xác thực tiền tự động. | Ride/Payment/Fraud | User 2026-09-24 | SOP chi tiết là ops/legal task trước launch. |
| BR-FOOD-001 | P0 Food ưu tiên chuỗi/outlet quen thuộc, nhiều chi nhánh, menu tương đối chuẩn hóa. | Food Supply | BRD v0.5 | Danh sách ứng viên cấu hình theo city, không cam kết hợp tác. |
| BR-FOOD-PRICE-001 | Food P0 dùng Recommended Delivery Fee; customer chỉ accept hoặc không đặt. | Food/Pricing | BRD v0.5 | Không negotiation, không Counter Offer. |
| BR-FOOD-PRICE-002 | Food item price không được thương lượng. | Food/Pricing | BRD v0.5 | P0. |
| BR-PAY-FOOD-001 | P0 Food chỉ hỗ trợ bank transfer/QR Customer -> Driver, payment proof bắt buộc. | Food/Payment | BRD v0.5 | Driver chỉ đặt món sau khi proof/confirmation đạt policy. |
| BR-PAY-FOOD-002 | P0 không hỗ trợ COD, cash, gateway, wallet, escrow hoặc Onway-held payment cho Food. | Food/Payment | BRD v0.5 | Đã chốt. |
| BR-PAY-FOOD-003 | Các gian lận/tranh chấp từ direct transfer Food được xử lý bằng SOP vận hành, complaint/fraud lifecycle và audit; BRD/P0 không yêu cầu gateway xác thực tiền tự động. | Food/Payment/Fraud | User 2026-09-24 | SOP chi tiết là ops/legal task trước launch. |
| BR-FOOD-CHANGE-001 | Khi giá/tình trạng món thay đổi, driver gọi khách, nhập thay đổi thực tế, gửi đề xuất, khách Accept/Reject trước khi mua món bị ảnh hưởng. | Food/Order Change | BRD v0.5 | Đề xuất không auto-update menu chung. |
| BR-FOOD-CANCEL-001 | Sau khi driver đã đặt món với nhà hàng, customer không còn quyền hủy để nhận lại tiền nếu đổi ý/từ chối nhận. | Food/Cancellation | BRD v0.5 | Lỗi do driver/merchant/system cần policy riêng. |
| BR-DISPUTE-001 | Khi có lỗi/tranh chấp, nguyên tắc nghiệp vụ là bên nào sai bên đó chịu trách nhiệm; Onway là phần mềm kết nối và không tự động bồi thường thay các bên. | Complaint/Dispute/Food/Ride | User 2026-09-24 | Cần legal review, terms và bằng chứng/audit rõ để phân định lỗi. |
| BR-FOOD-WAIT-001 | Waiting Fee cấu hình theo Brand: free wait, start time, per-minute/block, cap và no-fee policy. | Food/Pricing | BRD v0.5 | Outlet override có thể sau. |
| BR-MENU-001 | Brand nên có Canonical Menu dùng chung khi phù hợp; outlet override giá, trạng thái món, modifier, giờ mở cửa. | Food/Menu | BRD v0.5 | Outlet override không đổi canonical menu của brand. |
| BR-MENU-002 | P0 Food supply do Admin Portal quản trị; driver không tạo/sửa/xác minh restaurant/menu trong launch MVP. | Food/Admin | BRD v0.5 | Mission/Community Truth future. |
| BR-DRV-ONB-001 | Driver đăng ký, xác minh phone, identity, giấy tờ theo vehicle/service, pháp lý/background nếu áp dụng, rồi mới Activated. | Driver Onboarding | BRD v0.5 | P0. |
| BR-DRV-FEE-001 | Driver launch package: `1.000.000 VND` trước kích hoạt cho 12 tháng, tặng thêm 6 tháng, tổng 18 tháng. | Monetization/Driver | BRD v0.5 | Không gọi là cọc/ký quỹ/quỹ bồi thường fraud. |
| BR-DRV-REFUND-001 | Refund phần 12 tháng theo quý sử dụng: Q1 `750.000`, Q2 `500.000`, Q3 `250.000`, Q4 `0`; 6 tháng tặng không hoàn tiền. | Driver Fee/Refund | BRD v0.5 | Cần legal review cách diễn đạt hợp đồng. |
| BR-DRV-FEE-002 | Phí hồ sơ/xử lý tài xế `500.000 VND` trong tương lai được thu lúc nộp hồ sơ, nếu chương trình miễn phí không còn áp dụng. | Monetization/Driver Onboarding | User 2026-09-24 | Cần legal review và copy rõ ràng. |
| BR-CUST-FEE-001 | P0 không thu phí cố định từ customer theo đơn/chuyến ngoài khoản customer trả trực tiếp cho driver/merchant theo flow. | Monetization/Customer | User 2026-09-24 | Không thêm customer platform/service fee trong P0. |
| BR-TRUST-001 | Trust Engine đầy đủ không thuộc P0; P0 chỉ dùng account status, driver activation/risk status, eligibility, complaint status, manual/admin lock và auto-lock tối giản theo rule cấu hình được. | Trust/Risk | BRD v0.5 + User 2026-09-24 | COD và trust privilege không thuộc P0. |
| BR-COMPLAINT-001 | Complaint không tự động trở thành Fraud Case. | Complaint/Fraud | BRD v0.5 | P0 có thể ảnh hưởng risk, eligibility, lock. |
| BR-FRAUD-001 | P0 fraud case manual lifecycle: REPORTED -> EVIDENCE_COLLECTION -> DRIVER_RESPONSE -> HUMAN_REVIEW -> HUMAN_DECISION -> CONFIRMED/REJECTED -> APPEAL -> FINALIZED. | Fraud/Ops | BRD v0.5 | AI-assisted lifecycle future. |
| BR-FRAUD-002 | Fraud liability và platform fee là hai nghĩa vụ tách biệt; `1.000.000 VND` không được mô tả là tiền Onway giữ để bù fraud. | Fraud/Legal/Monetization | BRD v0.5 | Cần legal review. |
| BR-FRAUD-003 | Auto-lock driver P0 là khóa tạm thời theo ngưỡng cấu hình được, ví dụ severe safety/fraud signal, nhiều complaint hợp lệ hoặc paid/no-show. | Fraud/Risk/Driver | User 2026-09-24 | Auto-lock không tự kết luận fraud/liability cuối cùng. |
| BR-FRAUD-004 | Mọi auto-lock phải có reason, audit trail, case/review queue và khả năng admin unlock/override theo quyền. | Fraud/Risk/Admin | User 2026-09-24 | Cần PRD chi tiết về threshold, notification, appeal và fairness/legal review. |
| BR-ADS-001 | Ads không thuộc launch; khi triển khai, nội dung tài trợ phải được ghi rõ là quảng cáo. | Ads/Future | BRD v0.5 | Ads không tác động Trust/Community Truth/fraud/organic rating. |
| BR-ADS-002 | Tiêu chí launch success để bắt đầu đánh giá ads sẽ được quyết sau bởi user/marketing. | Ads/Future | User 2026-09-24 | Không block P0. |
| BR-WL-001 | Có thể mua white-label chi phí thấp để rút ngắn time-to-market sau khi xác định yêu cầu Onway và phân loại Supported/Customize/Rewrite. | Build/Strategy | BRD v0.5 | Onway phải kiểm soát logic khác biệt. |
