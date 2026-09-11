# ONWAY - TÀI LIỆU YÊU CẦU NGHIỆP VỤ

**Loại tài liệu:** Business Requirements Document (BRD) / Nguồn sự thật nghiệp vụ  
**Phiên bản:** 0.5 (bản làm việc)  
**Trạng thái:** Đang thu thập và làm rõ yêu cầu  
**Ngày cập nhật:** 11/09/2026  
**Ngôn ngữ chính:** Tiếng Việt  
**Phạm vi:** Gọi xe và giao đồ ăn

## Lịch sử phiên bản

| Phiên bản | Ngày | Nội dung |
|---|---|---|
| 0.2 | 10/09/2026 | Tổng hợp Master Business & Product Context và BRD ban đầu của dự án. |
| 0.3 | 10/09/2026 | Đổi thương hiệu thành Onway; bổ sung khách hàng mục tiêu, định vị giá, quản lý region, thương lượng phí giao đồ ăn, cập nhật giá thực tế và ưu đãi tài xế 18 tháng. |
| 0.4 | 10/09/2026 | Chốt phạm vi ưu đãi toàn app, refund, thời điểm trả trước Food, hủy đơn sau khi đặt món, biên độ deal ±10%, region polygon, dùng số điện thoại thật và hoãn quảng cáo. |
| 0.5 | 11/09/2026 | Đồng bộ quyết định PRD P0: bỏ COD/tiền mặt/payment gateway cho Ride/Food, chỉ dùng bank transfer/QR có payment proof; bỏ thương lượng phí giao Food; Trust Engine đầy đủ hoãn sau launch; Food supply ban đầu do Admin quản trị. |

## Quy ước trạng thái

| Trạng thái | Ý nghĩa |
|---|---|
| **ĐÃ CHỐT** | Quyết định nghiệp vụ hiện hành, được dùng để xây PRD. |
| **QUYẾT ĐỊNH HIỆN TẠI** | Hướng đang áp dụng nhưng có thể tiếp tục tinh chỉnh. |
| **GIẢ THUYẾT** | Giá trị hoặc chính sách cần kiểm chứng trước khi triển khai thương mại. |
| **ỨNG VIÊN** | Ý tưởng được cân nhắc nhưng chưa được duyệt vào MVP. |
| **CHƯA CHỐT** | Cần quyết định nghiệp vụ rõ ràng. |
| **HOÃN LẠI** | Không nằm trong phạm vi hiện tại. |
| **CẦN PHÁP LÝ** | Cần được tư vấn pháp lý trước khi ra mắt thương mại. |

Khi nội dung cũ mâu thuẫn với quyết định mới, quyết định mới hơn được ưu tiên. Các giá trị tiền, ngưỡng, thời gian và chính sách có khả năng thay đổi phải được quản lý bằng cấu hình, không được hard-code.

---

# 1. Mục đích tài liệu

Tài liệu này mô tả yêu cầu nghiệp vụ cốt lõi của Onway, làm cơ sở cho:

- phân rã thành PRD;
- thiết kế sản phẩm và trải nghiệm người dùng;
- xây dựng kiến trúc và phần mềm;
- xây dựng tiêu chí nghiệm thu và kiểm thử;
- đánh giá vận hành, rủi ro và tuân thủ pháp luật.

BRD chỉ mô tả mục tiêu, quy tắc và hành vi nghiệp vụ. BRD không quyết định ngôn ngữ lập trình, cơ sở dữ liệu, API, hạ tầng cloud hoặc cấu trúc mã nguồn.

# 2. Tầm nhìn sản phẩm

Onway là nền tảng gọi xe và giao đồ ăn theo mô hình:

> **AI-native, cộng đồng cùng vận hành, 0% commission và hạn chế giữ tiền giao dịch.**

Onway không chỉ là một ứng dụng tương tự Grab hoặc ShopeeFood với commission thấp hơn. Mục tiêu là thay đổi cấu trúc chi phí trung gian để:

- tài xế giữ lại toàn bộ giá trị dịch vụ họ tạo ra;
- nhà hàng không mất phần trăm doanh thu cho nền tảng;
- khách hàng nhận mức giá cạnh tranh và minh bạch;
- AI và cộng đồng tài xế thực hiện phần lớn công việc vận hành thường xuyên;
- bộ máy vận hành và kỹ thuật có thể duy trì gọn khi quy mô tăng.

## 2.1 Định vị cốt lõi - ĐÃ CHỐT

> Onway là marketplace dịch vụ vận hành bằng AI và cộng đồng, nơi nhà cung cấp dịch vụ giữ lại giá trị họ tạo ra.

## 2.2 Định hướng dài hạn

Sau Ride và Food, Onway có thể mở rộng sang giao hàng, mua sắm và các dịch vụ địa phương khác. Thị trường hiện tại chỉ là Việt Nam; mở rộng đa quốc gia là định hướng tương lai.

# 3. Nguyên tắc kinh doanh

## BP-001 - AI First - ĐÃ CHỐT

AI là lớp vận hành cốt lõi, không phải tính năng trang trí. AI được ưu tiên khi có thể giảm chi phí, tăng quy mô hoặc tăng chất lượng trong các lĩnh vực:

- phân tích yêu cầu, lập trình, kiểm thử và tài liệu;
- gợi ý giá, matching và ETA;
- OCR, chuẩn hóa menu và phát hiện thay đổi;
- kiểm tra chất lượng hình ảnh;
- tạo và phân phối Mission;
- xác minh dữ liệu nhà hàng;
- phát hiện gian lận và referral fraud;
- hỗ trợ khách hàng, tài xế và xử lý khiếu nại;
- phát hiện bất thường và hỗ trợ vận hành.

Lưu ý P0: không phải mọi năng lực AI ở trên đều thuộc launch MVP. AI OCR/menu extraction production, Mission, Community Truth và AI Restaurant Lifecycle được đưa sang phase sau; P0 chỉ cần dữ liệu/audit/evidence đủ sạch để mở rộng.

## BP-002 - Con người xử lý ngoại lệ - ĐÃ CHỐT

> AI xử lý trường hợp thông thường. Con người xử lý ngoại lệ.

Con người tham gia khi độ tin cậy thấp, bằng chứng mâu thuẫn, rủi ro an toàn hoặc tài chính cao, có quyết định khóa vĩnh viễn, hoặc pháp luật yêu cầu.

## BP-003 - Cộng đồng cùng vận hành - ĐÃ CHỐT

Khi một công việc thực địa có thể được tài xế thực hiện an toàn, AI kiểm tra và nhiều thành viên độc lập xác minh, Onway ưu tiên mô hình cộng đồng thay vì xây đội ngũ hiện trường lớn.

## BP-004 - 0% commission - ĐÃ CHỐT

Onway không thu phần trăm trên:

- giá chuyến xe;
- phí giao hàng;
- giá trị món ăn;
- thu nhập tài xế;
- doanh thu nhà hàng.

## BP-005 - Money-light - ĐÃ CHỐT

Tiền giao dịch không đi qua Onway trong phạm vi hiện tại:

- Ride: Khách hàng -> Tài xế.
- Food: Khách hàng -> Tài xế -> Nhà hàng.

Onway tránh thu hộ, giữ số dư đơn hàng, đối soát và thanh toán lại cho tài xế hoặc nhà hàng. Onway chỉ nhận các khoản là doanh thu trực tiếp của Onway như phí nền tảng, subscription, quảng cáo và dịch vụ giá trị gia tăng trong tương lai.

## BP-006 - Subscription và quảng cáo - ĐÃ CHỐT

Nguồn doanh thu chính dự kiến:

1. Phí sử dụng nền tảng hoặc subscription của tài xế.
2. Quảng cáo trong ứng dụng.
3. Dịch vụ giá trị gia tăng trong tương lai.

## BP-007 - Không markup giá món - ĐÃ CHỐT

Onway không chủ động tăng giá món ăn để hưởng chênh lệch. Giá trên ứng dụng dựa trên dữ liệu nhà hàng được xác minh gần nhất. Chênh lệch do dữ liệu cũ hoặc nhà hàng thay đổi giá là vấn đề chất lượng dữ liệu, không phải markup của Onway.

## BP-008 - Yêu cầu rõ ràng - ĐÃ CHỐT

Yêu cầu phải nguyên tử, rõ nghĩa, kiểm thử được, truy vết được và ưu tiên cấu hình:

`Business Requirement -> Functional Requirement -> User Story -> Acceptance Criteria -> Test`

# 4. Mục tiêu kinh doanh

- **BO-001:** Tài xế giữ 100% giá chuyến xe và phí giao hàng đã thỏa thuận.
- **BO-002:** Nhà hàng trả 0% commission trên giá trị món ăn.
- **BO-003:** Tạo mức giá cạnh tranh cho khách nhờ giảm chi phí trung gian.
- **BO-004:** Không markup giá món ăn.
- **BO-005:** Giảm chi phí thu hút và vận hành nhà hàng.
- **BO-006:** Dùng cộng đồng tài xế để xây dựng và duy trì dữ liệu thực địa.
- **BO-007:** Dùng AI để hạn chế quy mô bộ máy vận hành.
- **BO-008:** Tạo doanh thu định kỳ từ subscription.
- **BO-009:** Tạo nguồn doanh thu quảng cáo khi có đủ lưu lượng người dùng.
- **BO-010:** Xây nền tảng có thể mở rộng sang dịch vụ và quốc gia khác trong tương lai.

# 5. Khách hàng mục tiêu và giá trị cung cấp

## 5.1 Nhóm khách hàng ban đầu - QUYẾT ĐỊNH HIỆN TẠI

- Nhân viên văn phòng.
- Sinh viên đại học và cao đẳng.

## 5.2 Lý do khách hàng chuyển sang Onway - ĐÃ CHỐT

- Giá dịch vụ thấp hơn.
- Giá món không bị Onway markup.
- Có thể đề xuất giá chuyến xe một lần trong biên độ ±10% giá Onway đề xuất.
- Có thể đề xuất phí giao đồ ăn một lần trong biên độ ±10% giá Onway đề xuất.
- Giá món và phí giao hàng được trình bày riêng, minh bạch.

# 6. Phạm vi địa lý và region

## 6.1 Lộ trình thị trường - ĐÃ CHỐT

1. TP. Hồ Chí Minh.
2. Hà Nội.
3. Đà Nẵng.
4. Các khu vực khác tại Việt Nam.
5. Đa quốc gia trong tương lai.

MVP và giai đoạn thương mại hiện tại chỉ phục vụ Việt Nam.

## 6.2 Phạm vi ra mắt TP. Hồ Chí Minh - ĐÃ CHỐT

Onway ưu tiên các quận nội thành trước, không bắt buộc phủ toàn thành phố từ ngày đầu. Danh sách và ranh giới quận ban đầu chưa được chốt.

## 6.3 Quản lý region - ĐÃ CHỐT

- **BR-GEO-001:** Onway ra mắt thương mại tại TP. Hồ Chí Minh trước.
- **BR-GEO-002:** Onway mở rộng đến Hà Nội rồi Đà Nẵng khi marketplace đạt điều kiện phù hợp.
- **BR-GEO-003:** Hệ thống nghiệp vụ phải hỗ trợ quốc gia, thành phố và vùng phục vụ trong thành phố.
- **BR-GEO-004:** Admin cấu hình dịch vụ được phép hoạt động theo region.
- **BR-GEO-005:** Admin cấu hình loại phương tiện được phép hoạt động theo region.
- **BR-GEO-006:** Admin cấu hình thời gian hoạt động và tạm dừng dịch vụ theo region.
- **BR-GEO-007:** Region kiểm tra tính hợp lệ của điểm đón, điểm trả, địa chỉ giao hàng, vị trí tài xế và outlet.
- **BR-GEO-008:** Region có vòng đời tối thiểu: Planned, Pilot, Active, Paused và Closed.
- **BR-GEO-009:** Mô hình region phải sẵn sàng cho nhiều quốc gia nhưng chưa yêu cầu triển khai nghiệp vụ cross-border.
- **BR-GEO-010:** Admin phải có công cụ vẽ và chỉnh sửa polygon trực tiếp trên bản đồ để xác định ranh giới region.
- **BR-GEO-011:** Hệ thống phải xác định một tọa độ có nằm trong polygon đang hoạt động hay không để áp dụng quy tắc region.

# 7. Phạm vi sản phẩm ban đầu

## 7.1 Dịch vụ ra mắt - ĐÃ CHỐT

Ride Hailing và Food Delivery được ra mắt đồng thời tại các region được phê duyệt ở TP. Hồ Chí Minh.

## 7.2 Customer Super App - ĐÃ CHỐT

Một ứng dụng khách hàng hỗ trợ:

- gọi xe;
- đặt và giao đồ ăn;
- thanh toán trực tiếp cho tài xế;
- theo dõi đơn/chuyến;
- đánh giá, báo cáo và khiếu nại;
- chat với tài xế trong active Ride/Food.

Referral và quyền lợi dựa trên Trust là phase sau.

## 7.3 Driver App - ĐÃ CHỐT

Một ứng dụng tài xế hỗ trợ:

- Ride;
- Food Delivery;
- online/offline;
- nhận và xử lý job;
- location/tracking;
- chat với khách;
- xem payment proof và xác nhận đã nhận tiền.

Onway Missions, referral, gamification, Trust và thu thập/xác minh dữ liệu nhà hàng/menu qua tài xế là phase sau.

## 7.4 Phương tiện Ride - ĐÃ CHỐT

Giai đoạn đầu hỗ trợ:

- xe máy;
- ô tô.

## 7.5 Merchant App - TƯƠNG LAI

Merchant App không bắt buộc trong giai đoạn Food ban đầu. Sau này có thể hỗ trợ nhận đơn sớm, chuẩn bị món trước khi tài xế đến, cập nhật menu, tình trạng món và giờ mở cửa.

# 8. Các actor

| Actor | Vai trò nghiệp vụ |
|---|---|
| Customer | Đặt Ride/Food, trả tiền trực tiếp cho tài xế, đánh giá và khiếu nại. Thương lượng giá Ride là phase sau/feature-flag nếu được duyệt. |
| Driver | Cung cấp Ride/Food, nhận tiền trực tiếp. Mission, xác minh dữ liệu cộng đồng và referral là phase sau nếu được bật. |
| Merchant | Nhà hàng/cửa hàng cung cấp hàng hóa; chưa bắt buộc dùng Merchant App ban đầu. |
| Operator | Nhân sự Onway xử lý ngoại lệ và trường hợp cần quyết định con người. |
| Admin | Quản lý cấu hình giá, region, subscription/platform fee, driver, Food catalog, fraud/risk, complaint/dispute và rollout P0. Trust, Mission và quảng cáo là phase sau. |
| AI | Tác nhân hỗ trợ hoặc tự động xử lý trong giới hạn rủi ro và guardrail được phê duyệt; AI/OCR production không thuộc P0 launch. |

## 8.1 Liên lạc giữa khách và tài xế - ĐÃ CHỐT

- **BR-COMM-001:** Khách và tài xế tự gọi trực tiếp cho nhau bằng số điện thoại thật.
- **BR-COMM-002:** MVP chưa yêu cầu ẩn số hoặc gọi thoại trong ứng dụng.
- **BR-COMM-003:** MVP có chat giữa khách và tài xế trong active Ride/Food, hỗ trợ text và hình ảnh, retention 1 tuần.

# 9. Gọi xe

## 9.1 Điều kiện tài xế

- **BR-RIDE-001:** Ride giai đoạn đầu hỗ trợ xe máy và ô tô.
- **BR-RIDE-002:** Tài xế chỉ được kích hoạt sau khi hoàn thành xác minh bắt buộc.
- **BR-RIDE-003:** Quy định hồ sơ phải cấu hình được theo loại phương tiện và dịch vụ.

## 9.2 Commission và thu nhập

- **BR-RIDE-004:** Onway thu 0% commission trên giá chuyến xe.
- **BR-RIDE-005:** Tài xế nhận 100% giá chuyến xe đã thống nhất với khách.

## 9.3 Giá đề xuất

- **BR-RIDE-PRICE-001:** Onway cung cấp Recommended Price cho mỗi yêu cầu chuyến đi.
- **BR-RIDE-PRICE-002:** Recommended Price chỉ là giá đề xuất, không phải mức giá bắt buộc.
- **BR-RIDE-PRICE-003:** Gợi ý giá có thể dùng khoảng cách, thời gian, giao thông, thời tiết, cung, cầu, lịch sử chấp nhận, độ khó điểm đón và tín hiệu được duyệt khác.
- **BR-RIDE-PRICE-004:** AI phải hoạt động trong guardrail nghiệp vụ có thể cấu hình.

## 9.4 Thương lượng giá Ride - HOÃN SAU P0

- **BR-RIDE-NEG-000:** Ride Price Negotiation không phải dependency của launch P0 vì Trust Engine đầy đủ được hoãn sau launch.
- **BR-RIDE-NEG-001:** Khi tính năng được bật ở phase sau, khách đủ điều kiện được gửi đúng một mức giá đề xuất cho mỗi yêu cầu chuyến đi.
- **BR-RIDE-NEG-002:** Giá khách đề xuất phải nằm trong biên độ từ `-10%` đến `+10%` so với Recommended Price của Onway.
- **BR-RIDE-NEG-003:** Tài xế chỉ có thể Accept hoặc Reject giá khách đề xuất.
- **BR-RIDE-NEG-004:** Tài xế không gửi Counter Offer trong luồng triển khai ban đầu của tính năng negotiation.
- **BR-RIDE-NEG-005:** Nếu tài xế Accept, mức giá khách đề xuất trở thành Final Price.
- **BR-RIDE-NEG-006:** Các tỷ lệ biên độ phải được quản lý bằng cấu hình.

## 9.5 Thanh toán Ride

- **BR-PAY-RIDE-001:** Tiền chuyến xe không đi qua Onway.
- **BR-PAY-RIDE-002:** P0 chỉ hỗ trợ khách chuyển khoản ngân hàng trực tiếp cho tài xế, có thể bằng QR.
- **BR-PAY-RIDE-003:** P0 không hỗ trợ tiền mặt, COD, payment gateway, wallet, escrow hoặc Onway-held payment cho Ride.
- **BR-PAY-RIDE-004:** Payment proof là bắt buộc trong flow thanh toán Ride; thời điểm thanh toán cụ thể sẽ chốt trong PRD Ride chi tiết.
- **BR-PAY-RIDE-005:** Onway chỉ lưu trạng thái, bằng chứng và audit trail cần thiết cho dịch vụ, fraud/risk, dispute, kiểm toán hoặc tuân thủ.

# 10. Giao đồ ăn

## 10.1 Chiến lược ban đầu

Onway ưu tiên chuỗi có nhiều outlet, thương hiệu quen thuộc, vị trí rõ ràng và menu tương đối chuẩn hóa để mở rộng nhanh.

Danh sách ứng viên:

- Cà phê/trà: Highlands Coffee, Katinat, Phê La, Starbucks, Phúc Long, Trung Nguyên Legend, The Coffee House, Gong Cha, KOI Thé, Mixue.
- Đồ ăn nhanh: KFC, McDonald's, Lotteria, Jollibee, Texas Chicken, Popeyes.
- Pizza: Pizza Hut, Domino's, Pizza 4P's.
- Bánh/tráng miệng: BreadTalk, Tous les Jours, Dairy Queen.
- Cửa hàng tiện lợi: GS25, Circle K, FamilyMart.

Danh sách được cấu hình theo thành phố và không phải cam kết hợp tác thương mại.

## 10.2 Luồng đơn hàng cơ bản

1. Khách chọn outlet, món và địa chỉ giao.
2. Onway hiển thị giá món ước tính, phí giao đề xuất và tổng tiền ước tính.
3. Khách xác nhận mức phí giao do hệ thống đề xuất; P0 không có thương lượng phí giao Food.
4. Hệ thống tìm tài xế; tài xế Accept hoặc Reject job với phí giao đã hiển thị.
5. Sau khi tìm được tài xế, khách chuyển tiền trực tiếp cho tài xế.
6. Sau khi payment proof/confirmation đạt điều kiện theo policy, tài xế đến nhà hàng và trực tiếp đặt món.
7. Tài xế chờ nhà hàng chuẩn bị.
8. Tài xế trả tiền nhà hàng.
9. Tài xế giao món cho khách.

## 10.3 Phí giao Food và không thương lượng - ĐÃ CHỐT

- **BR-FOOD-PRICE-001:** Onway cung cấp Recommended Delivery Fee.
- **BR-FOOD-PRICE-002:** P0 không cho khách thương lượng hoặc nhập mức phí giao khác.
- **BR-FOOD-PRICE-003:** Customer chỉ có thể chấp nhận mức phí giao hệ thống đề xuất để đặt đơn hoặc không đặt.
- **BR-FOOD-PRICE-004:** Tài xế chỉ có thể Accept hoặc Reject Food job; không có Counter Offer.
- **BR-FOOD-PRICE-005:** Recommended Delivery Fee trở thành Final Delivery Fee khi đơn được customer xác nhận và driver accept.
- **BR-FOOD-PRICE-006:** Công thức, ngưỡng và guardrail tính phí giao phải được quản lý bằng cấu hình.
- **BR-FOOD-PRICE-007:** Giá món ăn không được thương lượng.

## 10.4 Thanh toán Food

- **BR-PAY-FOOD-001:** Tiền đơn Food không đi qua Onway.
- **BR-PAY-FOOD-002:** Luồng mặc định là Khách hàng -> Tài xế -> Nhà hàng.
- **BR-PAY-FOOD-003:** P0 không hỗ trợ COD, tiền mặt, payment gateway, wallet, escrow hoặc Onway-held payment cho Food.
- **BR-PAY-FOOD-004:** P0 chỉ hỗ trợ bank transfer/QR trực tiếp từ customer sang driver.
- **BR-PAY-FOOD-005:** Với đơn trả trước, khách chuyển tiền trực tiếp cho tài xế sau khi hệ thống đã tìm được tài xế nhận đơn.
- **BR-PAY-FOOD-006:** Payment proof là bắt buộc.
- **BR-PAY-FOOD-007:** Tài xế chỉ bắt đầu đặt món sau khi payment proof/confirmation đạt điều kiện theo policy.

## 10.5 Giá hoặc tình trạng món thay đổi - ĐÃ CHỐT

Khi tài xế đến nhà hàng và phát hiện sai giá, hết món, thay đổi modifier hoặc điều kiện khác:

1. Tài xế gọi cho khách để trao đổi.
2. Tài xế nhập giá hoặc thay đổi thực tế và gửi đề xuất trên app.
3. Khách Accept hoặc Reject trước khi tài xế mua món bị ảnh hưởng.
4. Đơn hàng lưu bằng chứng về đề xuất và quyết định của khách.

- **BR-FOOD-CHANGE-001:** Driver App cho phép đề xuất giá/tình trạng món thực tế.
- **BR-FOOD-CHANGE-002:** Khách phải xác nhận thay đổi ảnh hưởng đến đơn hiện tại.
- **BR-FOOD-CHANGE-003:** Đề xuất của một tài xế không tự động ghi đè menu chung.
- **BR-FOOD-CHANGE-004:** P0 không tự động cập nhật menu từ đề xuất của tài xế. Đề xuất cập nhật menu đi vào admin review; AI QA, Community Truth và xác minh độc lập là phase sau.

## 10.6 Hủy đơn sau khi tài xế đặt món - ĐÃ CHỐT

- **BR-FOOD-CANCEL-001:** Sau khi tài xế đã đặt món với nhà hàng, khách không còn quyền hủy để nhận lại tiền.
- **BR-FOOD-CANCEL-002:** Khách có thể chọn nhận hoặc không nhận món, nhưng nếu không nhận thì khoản tiền đã trả không được hoàn.
- **BR-FOOD-CANCEL-003:** Mốc tài xế đã đặt món phải được ghi nhận rõ trên đơn và có audit trail.
- **BR-FOOD-CANCEL-004:** Chính sách này áp dụng cho việc khách đổi ý hoặc từ chối nhận sau khi món đã được đặt; lỗi do tài xế, nhà hàng hoặc hệ thống cần chính sách xử lý riêng.

## 10.7 Waiting Fee

Waiting Fee được cấu hình theo Brand:

- thời gian chờ miễn phí;
- thời điểm bắt đầu tính phí;
- cách tính theo phút hoặc block;
- mức phí tối đa;
- chính sách không tính phí.

Outlet override có thể được bổ sung sau. AI có thể dự đoán thời gian chờ để cải thiện Recommended Delivery Fee, nhưng chính sách thu phí phải xác định bằng cấu hình.

# 11. Menu và dữ liệu nhà hàng

## 11.1 Canonical Brand Menu - ĐÃ CHỐT

- **BR-MENU-001:** Mỗi Brand nên có một Canonical Menu dùng chung khi phù hợp.
- **BR-MENU-002:** Không nhân bản toàn bộ menu cho từng outlet nếu outlet dùng menu chung.
- **BR-MENU-003:** Outlet có thể override giá, tình trạng món, sản phẩm, modifier, giờ mở cửa và trạng thái đóng cửa.
- **BR-MENU-004:** Outlet Override không được thay đổi Canonical Menu của toàn Brand.

## 11.2 Thu thập dữ liệu qua tài xế - TƯƠNG LAI

P0 Food supply do Admin Portal quản trị trước. Tài xế không tạo, sửa hoặc xác minh restaurant/menu trong launch MVP.

Onway tạo trước Target Outlet List. Tài xế không tự do tạo nhà hàng bất kỳ trong luồng Mission ban đầu.

## 11.3 Quy tắc chụp bằng chứng - TƯƠNG LAI

- Chỉ dùng camera trong Onway.
- Không nhận ảnh từ gallery cho Mission xác minh.
- Lưu GPS, timestamp, device information, mission session và metadata cần thiết.
- AI kiểm tra blur, glare, độ phân giải, crop, góc chụp, thiếu vùng menu, ảnh trùng và dấu hiệu tái sử dụng.
- Nếu chất lượng không đạt, tài xế phải chụp lại khi còn ở outlet.

## 11.4 Xác minh full menu - TƯƠNG LAI

- Mỗi lần xác minh menu phải chụp mới toàn bộ menu.
- Nút xác nhận một lần như `Menu đúng` không được xem là bằng chứng chính.
- Full menu được chụp lại ít nhất mỗi 6 tháng.
- Báo cáo sai menu có thể tạo Mission chụp lại ngay trước kỳ 6 tháng.

## 11.5 Xác minh nhiều tài xế - TƯƠNG LAI

- Cần ít nhất hai tài xế độc lập trước khi dữ liệu đạt trạng thái Verified.
- Nếu hai bằng chứng xung đột, yêu cầu tài xế thứ ba hoặc đưa vào exception handling.
- AI đánh giá tính độc lập qua thiết bị, quan hệ referral, lịch sử vị trí, pattern hành vi và lịch sử xác minh.

## 11.6 Bất thường giá - TƯƠNG LAI

| Mức chênh lệch | Xử lý ban đầu |
|---|---|
| `<= 5%` | Xác minh bình thường. |
| `> 5%` đến `15%` | Yêu cầu xác minh bổ sung. |
| `> 15%` | Anomaly. |
| `> 30%` | High-risk anomaly. |

Ngưỡng phải cấu hình được. Chênh lệch lớn không ngăn tài xế gửi bằng chứng nhưng dữ liệu không được auto-publish trước khi đủ Verification Confidence.

## 11.7 Hình ảnh và danh tính outlet - TƯƠNG LAI

- Hình ảnh gồm mặt tiền, bảng hiệu, khu vực đặt món, nội thất và ảnh tổng quan.
- Có thể chụp lại khoảng mỗi 6 tháng hoặc sớm hơn khi AI phát hiện thay đổi.
- Nếu outlet đổi tên, outlet cũ được xem là Closed.
- Tên mới tạo Outlet record mới.
- Không tự động chuyển menu, review, Community Truth hoặc lịch sử xác minh sang outlet mới.

## 11.8 Community Truth - TƯƠNG LAI

Dữ liệu quan trọng được quản lý theo mô hình:

> **Giá trị + Bằng chứng + Độ tin cậy**

Mỗi trường phù hợp có thể chứa giá trị, trạng thái xác minh, số người xác minh độc lập, thời điểm xác minh gần nhất, confidence và lịch sử bằng chứng.

# 12. Driver Onboarding và phí nền tảng

## 12.1 Onboarding

- **BR-DRV-ONB-001:** Tài xế đăng ký tài khoản.
- **BR-DRV-ONB-002:** Xác minh số điện thoại.
- **BR-DRV-ONB-003:** Xác minh danh tính.
- **BR-DRV-ONB-004:** Cung cấp giấy tờ theo loại xe và dịch vụ.
- **BR-DRV-ONB-005:** Hoàn thành yêu cầu pháp lý/background áp dụng.
- **BR-DRV-ONB-006:** Chỉ được Activated khi hoàn thành điều kiện bắt buộc.

## 12.2 Gói tài xế ban đầu - QUYẾT ĐỊNH HIỆN TẠI

- Tài xế đóng `1.000.000 VND` trước khi kích hoạt.
- Khoản này là phí sử dụng phần mềm/nền tảng, không phải tiền cọc, ký quỹ, bảo đảm hoặc quỹ bồi thường fraud.
- Phần trả phí bao gồm 12 tháng.
- Ưu đãi ra mắt tặng thêm 6 tháng.
- Tổng quyền sử dụng ban đầu là 18 tháng.
- Không thu subscription định kỳ khác trong 18 tháng này trừ khi chính sách được thay đổi rõ ràng.
- Ưu đãi được áp dụng ở cấp toàn bộ ứng dụng Onway, không tách hạn mức hoặc chính sách riêng theo từng thành phố.

## 12.3 Phí đăng ký/xử lý hồ sơ

- Phí dự kiến trong tương lai: `500.000 VND`.
- Nhóm tài xế thuộc chương trình ra mắt trên toàn ứng dụng được miễn toàn bộ khoản này.
- Khoản miễn phí phải được hiển thị như quyền lợi đăng ký.
- Đây không phải tiền mặt, số dư, wallet credit hoặc tiền có thể rút/hoàn.
- Điều kiện kết thúc chương trình miễn phí và thời điểm thu phí trong tương lai chưa chốt.

## 12.4 Hoàn phí - ĐÃ CHỐT VỀ NGHIỆP VỤ

Phần phí trả cho 12 tháng được chia thành bốn giai đoạn, mỗi giai đoạn 3 tháng và `250.000 VND`, tính từ ngày kích hoạt tài xế, không theo quý lịch.

| Thời điểm dừng | Hoàn phí phần 12 tháng |
|---|---:|
| Trong quý sử dụng 1 | `750.000 VND` |
| Trong quý sử dụng 2 | `500.000 VND` |
| Trong quý sử dụng 3 | `250.000 VND` |
| Trong quý sử dụng 4 | `0 VND` |

Khi đã bước vào một quý, quý đó được xem là đã sử dụng. Chỉ quý chưa bắt đầu mới được hoàn. Sáu tháng tặng thêm không quy đổi thành tiền và không có giá trị hoàn lại. Cách diễn đạt hợp đồng vẫn cần thẩm định pháp lý.

## 12.5 Quan hệ giữa hoàn phí và fraud

Platform Fee và Fraud Liability là hai nghĩa vụ tách biệt. Không được mô tả `1.000.000 VND` là tiền Onway giữ để bù fraud.

Nếu tài xế có nghĩa vụ fraud đã Finalized nhưng chưa thanh toán, Onway có thể khóa tài khoản và từ chối hoàn phần phí chưa dùng, tùy kết quả thẩm định pháp lý.

## 12.6 Subscription tương lai - GIẢ THUYẾT

| Phương tiện | Tháng | Năm |
|---|---:|---:|
| Xe máy | `499.000 VND` | `4.999.000 VND` |
| Ô tô | `999.000 VND` | `9.999.000 VND` |

Giá và thời điểm kích hoạt phải cấu hình được. Onway có thể trì hoãn thu subscription nếu marketplace chưa đủ đơn, thu nhập tài xế hoặc tính thanh khoản.

# 13. Trust - HOÃN SAU P0

Trust là hệ thống kiểm soát rủi ro, tách biệt với membership, loyalty và gamification. Trust Engine đầy đủ không phải dependency của launch P0.

Trong P0, hệ thống chỉ dùng các trạng thái tối thiểu như account status, driver activation status, driver risk status, eligibility, complaint status và manual/admin lock. COD, Food delivery fee negotiation và Trust-based privilege không có trong P0.

## 13.1 Customer Trust

| Level | Ý nghĩa | Quyền điển hình |
|---|---|---|
| T0 - New | Khách mới | Future trust level; P0 vẫn chỉ dùng bank transfer/QR. |
| T1 - Verified | Đã xác minh và có lịch sử ban đầu | Quyền cơ bản đã xác minh. |
| T2 - Trusted | Lịch sử tốt, ít hủy, không fraud nghiêm trọng | Có thể mở Ride negotiation trong phase sau nếu policy duyệt. |
| T3 - Preferred | Lịch sử mạnh hơn | Có thể mở đặc quyền rủi ro thấp trong tương lai nếu policy duyệt; COD không thuộc P0 và cần quyết định riêng nếu từng xem lại. |
| T4 - Elite | Lịch sử dài và chất lượng cao | Đặc quyền tương lai được duyệt. |

- Ngưỡng Trust cấu hình được.
- Trust có thể giảm khi hành vi rủi ro tăng.
- Fraud nghiêm trọng có thể giảm hoặc khóa đặc quyền ngay.
- Trả tiền hoặc mua membership không được vượt qua risk control.

## 13.2 Driver Trust

| Level | Ý nghĩa |
|---|---|
| D0 - Applicant | Chưa hoạt động, không nhận đơn. |
| D1 - Verified | Đủ điều kiện nhận đơn cơ bản. |
| D2 - Trusted | Được nhận cơ hội có giá trị cao hơn. |
| D3 - Pro | Có thể nhận Food giá trị cao hoặc Mission ưu tiên. |
| D4 - Elite | Nhóm Trust cao nhất. |

Driver Trust có thể dựa trên tỷ lệ hoàn thành, hủy, khiếu nại, fraud, tuổi tài khoản, chất lượng xác minh, GPS anomaly, referral và đóng góp cộng đồng. Onway không bắt buộc công khai công thức chính xác để tránh bị gaming.

# 14. Gamification và Mission - TƯƠNG LAI / P2

## 14.1 Gamification - ĐÃ CHỐT VỀ HƯỚNG DÀI HẠN

Khi bật sau core launch, hệ thống có thể sử dụng bốn khái niệm:

1. XP.
2. Level.
3. Badge.
4. Mission.

Không tạo tiền ảo Onway Credits trong giai đoạn đầu nếu chưa có quyết định riêng. Trust và XP phải tách biệt.

## 14.2 XP tham khảo

| Hoạt động | XP ứng viên |
|---|---:|
| Hoàn thành Ride | `+10` |
| Hoàn thành Food | `+10` |
| Xác minh nhà hàng được chấp nhận | `+10` |
| Chụp full menu được chấp nhận | `+30` |
| Referral khách đủ điều kiện | `+50` |
| Referral tài xế đủ điều kiện | `+200` |

Mọi giá trị XP phải cấu hình được.

## 14.3 Level và Badge - ỨNG VIÊN

Level đề xuất: Starter -> Explorer -> Pro -> Expert -> Master -> Legend.

Badge đề xuất: Founding Driver, Road Master, Food Explorer, Community Builder, City Builder và Restaurant Expert.

Level/Badge không tự động tăng Trust hoặc mở đặc quyền rủi ro cao.

## 14.4 Quy tắc an toàn - ĐÃ CHỐT

Không tạo phần thưởng khuyến khích chạy quá tốc độ, làm việc liên tục không an toàn, hoàn thành số chuyến phi thực tế hoặc vi phạm an toàn giao thông.

## 14.5 Onway Missions

Mission có thể gồm:

- xác minh outlet;
- chụp full menu;
- xác minh giờ mở cửa;
- chụp hình nhà hàng;
- xác minh giá;
- xác minh đóng cửa;
- referral khách;
- referral tài xế.

AI có thể tạo Mission khi dữ liệu cũ, đủ 6 tháng, có báo cáo sai, bằng chứng xung đột hoặc phát hiện anomaly.

Mission Reward không được trả chỉ vì tài xế bấm Submit. Luồng phải qua AI QA, xác minh, data accepted, fraud check rồi mới Reward Eligible và Paid. Việc xác minh dữ liệu hiện tại vẫn đúng vẫn có thể được thưởng.

# 15. Referral - P1 / SAU CORE LAUNCH

## 15.1 Driver Referral

Giá trị tham khảo: `50.000 VND` cho mỗi tài xế được giới thiệu và đủ điều kiện.

Không trả thưởng chỉ vì đăng ký. Điều kiện dự kiến gồm xác minh, kích hoạt, hoàn thành yêu cầu truy cập nền tảng, hoàn thành ít nhất một chuyến thật và qua fraud check.

## 15.2 Customer Referral

Giả thuyết ban đầu:

- `10.000 VND` sau đơn hợp lệ đầu tiên;
- `5.000 VND` cho mỗi đơn đủ điều kiện trong 10 đơn tiếp theo.

Mọi giá trị phải cấu hình được và chỉ trả sau fraud validation.

## 15.3 Referral Fraud

AI/Fraud Engine cần phát hiện fake account, self-referral, multi-accounting, device farm, referral ring, fake order, thông đồng tài xế-khách, cluster bất thường và giá trị đơn bất thường. Phần thưởng có thể có thời gian fraud hold trước khi được trả.

# 16. Khiếu nại và gian lận

## 16.1 Khiếu nại

- Onway cung cấp kênh tiếp nhận khiếu nại.
- Hồ sơ khiếu nại được lưu theo chính sách và pháp luật.
- Khiếu nại dịch vụ không tự động trở thành Fraud Case.
- Trong P0, khiếu nại có thể ảnh hưởng risk status, matching eligibility và lock state. Customer/Driver Trust đầy đủ là phase sau.
- Vấn đề an toàn hoặc tuân thủ nghiêm trọng có thể dẫn đến hạn chế tạm thời và human review.

## 16.2 Phân biệt service issue và fraud - ĐÃ CHỐT

Ví dụ có thể là fraud:

- nhận tiền Food nhưng cố ý không mua hoặc không giao;
- giả hoàn thành chuyến;
- fake GPS;
- bằng chứng nhà hàng hoặc hình ảnh giả/tái sử dụng;
- fake referral hoặc fake account;
- thông đồng để lấy tiền/thưởng;
- cố ý cung cấp thông tin sai để nhận Mission Reward.

Không tự động xem là fraud:

- thái độ không tốt;
- giao trễ;
- hủy đơn;
- chất lượng thấp;
- nhầm đơn không cố ý;
- hiểu nhầm thật sự.

## 16.3 Vòng đời Fraud Case

P0/manual:

`REPORTED -> EVIDENCE_COLLECTION -> DRIVER_RESPONSE -> HUMAN_REVIEW -> HUMAN_DECISION -> CONFIRMED/REJECTED -> APPEAL -> FINALIZED`

Future/AI-assisted:

`REPORTED -> AI_TRIAGE -> EVIDENCE_COLLECTION -> DRIVER_RESPONSE -> AI_RECOMMENDATION -> HUMAN_DECISION -> CONFIRMED/REJECTED -> APPEAL -> FINALIZED`

Khiếu nại của khách không đồng nghĩa fraud đã được xác nhận. Tài khoản rủi ro cao có thể bị hạn chế tạm thời trong thời gian điều tra theo chính sách.

## 16.4 Trách nhiệm tài chính - GIẢ THUYẾT / CẦN PHÁP LÝ

Khi fraud được xác nhận và Finalized, giả thuyết hiện tại là tài xế chịu:

1. Thiệt hại thực tế của khách, nếu có.
2. `200.000 VND` Fraud Case Processing Charge.

Khoản phí phải cấu hình được và cần thẩm định pháp lý. Không gọi khoản này là phạt `200%`.

# 17. AI Operations - TƯƠNG LAI / KHÔNG PHỤ THUỘC P0

AI Operations là hướng phát triển sau khi core Ride/Food/Admin/Driver/Customer đã chạy ổn. P0 chỉ cần audit/evidence/data structure đủ sạch để sau này có thể thêm AI mà không phá luồng vận hành.

## 17.1 Phân cấp rủi ro

| Mức | Cách xử lý | Ví dụ |
|---|---|---|
| Low | AI được tự động thực hiện sau khi feature được bật | Từ chối ảnh mờ, tạo Mission, cấp XP, phát hiện ảnh trùng. |
| Medium | AI tự động với audit trail | Cập nhật dữ liệu hoặc thao tác vận hành đã được policy cho phép. |
| High | AI đề xuất, con người duyệt | Trách nhiệm tài chính, khóa vĩnh viễn, fraud giá trị cao, bồi thường lớn. |

## 17.2 AI Support

AI có thể thu thập đơn liên quan, lịch sử hai bên, GPS, chat, bằng chứng, future Trust, fraud history và dữ liệu giao dịch; sau đó phân loại, tóm tắt và đề xuất hành động. Operator tập trung vào Approve, Reject hoặc Request More Evidence.

## 17.3 AI Restaurant Lifecycle

AI có thể nhận diện Brand/Outlet, OCR menu, chuẩn hóa món, phát hiện thay đổi, duplicate, closure, location anomaly, tính confidence, tạo Mission, chọn tài xế phù hợp, kết hợp bằng chứng và auto-update khi đạt ngưỡng.

# 18. Quảng cáo - TƯƠNG LAI / KHÔNG THUỘC GIAI ĐOẠN RA MẮT

Onway không triển khai quảng cáo trong giai đoạn ra mắt ban đầu. Sau khi sản phẩm launch thành công và có đủ traffic, Onway mới đánh giá mô hình quảng cáo.

Các hình thức ứng viên:

- Sponsored Restaurant;
- Sponsored Brand;
- Sponsored Search Result;
- Sponsored Mission;
- quảng cáo cho tài xế;
- contextual advertising.

- **BR-ADS-001:** Nội dung tài trợ phải được ghi rõ là quảng cáo.
- **BR-ADS-002:** Quảng cáo không được tác động Trust, Community Truth, Verification Confidence, fraud decision hoặc organic rating.

# 19. Chiến lược Merchant và white-label

## 19.1 Merchant acquisition

Mô hình ưu tiên:

> Target Outlet List do hệ thống tạo + Driver Capture + AI + Community Verification.

Onway tránh mở rộng đội sales theo từng nhà hàng nếu cộng đồng và AI có thể làm an toàn, chính xác.

## 19.2 Merchant App tương lai

Merchant App dự kiến miễn phí và giữ nguyên hướng 0% commission. Dịch vụ Merchant Premium trong tương lai chưa chốt.

## 19.3 White-label - ĐÃ CHỐT VỀ HƯỚNG

Onway có thể mua giải pháp white-label chi phí thấp để rút ngắn time-to-market. Phải xác định yêu cầu Onway trước rồi đánh giá từng phần là Supported, Customize hoặc Rewrite.

Có thể tái sử dụng map, GPS tracking, online/offline, lifecycle cơ bản, dispatch, push notification, chat, history và admin cơ bản.

Onway phải sở hữu hoặc kiểm soát logic khác biệt gồm Trust, Missions, Community Truth, AI Restaurant Operations, Referral Fraud, Price Negotiation, Subscription, Gamification và Fraud Operations.

# 20. Các engine nghiệp vụ cốt lõi

Không phải engine nào cũng thuộc P0. P0 ưu tiên Matching, Pricing Recommendation, Fraud/Risk tối thiểu, Complaint/Dispute, Media/Evidence và Policy Config.

| Engine | Phase | Mục đích |
|---|---|---|
| Matching Engine | P0 | Kết nối khách và tài xế cho Ride/Food. |
| Pricing Recommendation Engine | P0 | Đề xuất giá/phí trong guardrail; Food không có delivery fee negotiation P0. |
| Complaint/Dispute Engine | P0 | Tiếp nhận khiếu nại, evidence, xử lý paid/no-show và lock driver theo rule. |
| Fraud/Risk Controls | P0 tối thiểu | Risk status, manual lock/unlock, auto-lock sau 2 qualifying paid/no-show complaint. |
| Policy Config Engine | P0 | Quản lý region, currency, service availability, timeout, threshold, fee policy. |
| Trust Engine | Future | Quyết định privilege/risk nâng cao sau launch. |
| Mission Engine | Future | Biến cộng đồng tài xế thành mạng lưới công việc thực địa. |
| Community Truth Engine | Future | Duy trì dữ liệu bằng bằng chứng, nhiều verifier và confidence. |
| AI Operations Engine | Future | Tự động xử lý bình thường và chuyển ngoại lệ cho con người. |

# 21. Admin và cấu hình

Admin cần quản lý tối thiểu:

- quốc gia, thành phố, region và rollout;
- dịch vụ và phương tiện theo region;
- pricing guardrail và waiting policy;
- phí nền tảng, promotion, waiver và subscription;
- future Trust policy và privilege;
- future Mission, reward và XP;
- restaurant, Brand, Canonical Menu và outlet override;
- fraud, complaint và dispute;
- quảng cáo future;
- threshold, trạng thái và audit trail.

# 22. Chỉ số kinh doanh

## Marketplace

Active Customers, Active Drivers, Ride Requests, Food Orders, Match Rate, Acceptance Rate, Completion Rate, Cancellation Rate và Average Match Time.

## Driver

Activation Rate, Retention, Trips per Driver, Driver Earnings, Subscription Conversion và Referral Rate sau khi referral được bật.

## Customer

Acquisition, First Order Conversion, Repeat Rate và Orders per Customer. Referral Rate và Trust Distribution là metric phase sau.

## Food

Active Outlets, Menu Accuracy, Average Menu Age, Verification Rate, Average Waiting Time và Price Mismatch Rate.

## Mission và AI Operations - FUTURE

Missions Generated/Accepted/Completed, Verification Acceptance Rate, Mission Fraud Rate, Cost per Verified Outlet, AI Auto-resolution Rate, Human Escalation Rate, False Positive Rate và Cost per Case.

## Fraud và doanh thu

Fraud Rate, Fraud Value, Fraud Recovery Rate, Platform Fee Revenue, Subscription Revenue, ARPU và Driver Subscription Conversion. Referral Fraud, Mission Fraud và Advertising Revenue là metric phase sau.

# 23. Tiêu chí thành công chiến lược

1. Tài xế giữ 100% giá Ride/phí Delivery.
2. Nhà hàng trả 0% commission.
3. Onway không giữ tiền giao dịch Ride/Food.
4. Khách nhận giá món không bị Onway markup.
5. AI xử lý phần lớn hoạt động bình thường.
6. Cộng đồng tài xế thực hiện phần lớn xác minh thực địa.
7. Dữ liệu Merchant tăng mà nhân sự Operations/Sales không tăng tuyến tính.
8. Đội kỹ thuật duy trì tương đối nhỏ nhờ AI.
9. Subscription tạo doanh thu định kỳ.
10. Quảng cáo có thể trở thành nguồn doanh thu bổ sung sau khi launch thành công.
11. Con người tập trung vào ngoại lệ.

# 24. Hạng mục cần thẩm định pháp lý

- `LEGAL-001`: Phân loại pháp lý của tài xế.
- `LEGAL-002`: Điều khoản Platform Usage Fee.
- `LEGAL-003`: Chính sách hoàn phí và 6 tháng tặng thêm.
- `LEGAL-004`: Mất quyền hoàn phí khi còn Fraud Liability đã Finalized.
- `LEGAL-005`: Fraud Case Processing Charge `200.000 VND`.
- `LEGAL-006`: Nghĩa vụ của nền tảng vận tải/gọi xe.
- `LEGAL-007`: Tiếp nhận, lưu trữ và xử lý khiếu nại.
- `LEGAL-008`: Mô hình niêm yết nhà hàng không tích hợp trực tiếp.
- `LEGAL-009`: Sử dụng nhãn hiệu, menu và hình ảnh Brand.
- `LEGAL-010`: Quyền riêng tư, profiling, AI, GPS và device evidence.
- `LEGAL-011`: Phí đăng ký/xử lý hồ sơ tài xế và cách công bố waiver.

# 25. Ngoài phạm vi hoặc hoãn lại

- Community Listed Outlet.
- Merchant monetization ngoài hướng hiện tại.
- Customer paid membership.
- Loyalty program chính xác.
- Favorite/Preferred Driver chính thức.
- Onway Credits hoặc tiền ảo.
- Leaderboard, season, team challenge và streak.
- Insurance, bank guarantee và escrow.
- Wallet và Onway-held order payment.
- COD và tiền mặt cho Ride/Food trong P0.
- Payment gateway cho Ride/Food trong P0.
- Food delivery fee negotiation.
- Trust Engine đầy đủ trong P0.
- Corporate Ride.
- Grocery, parcel delivery và shopping.
- Cross-border.
- Giá quảng cáo chính xác.
- Công thức Trust chính xác.
- Chi tiết AI model/provider và các lựa chọn kỹ thuật nằm ngoài BRD; xem Architecture v0.2 và các technical spec liên quan.

# 26. Các quyết định đang mở

1. Chương trình ưu đãi toàn app kết thúc theo ngày, số lượng tài xế hay điều kiện kinh doanh nào?
2. Phí hồ sơ `500.000 VND` trong tương lai thu lúc nộp hồ sơ hay sau khi được duyệt?
3. Ride payment timing: customer chuyển khoản trước khi tài xế đến đón, lúc bắt đầu chuyến, hay lúc kết thúc chuyến?
4. Định nghĩa "2 khiếu nại hợp lệ đang mở" để auto lock driver cần tiêu chí nào?
5. Danh sách và ranh giới polygon TP. Hồ Chí Minh ban đầu gồm những khu vực nào?
6. Có cho phép chuyến bắt đầu trong region nhưng kết thúc ngoài region không?
7. Chính sách hoàn/bồi thường khi lỗi hủy Food đến từ tài xế, nhà hàng hoặc hệ thống là gì?
8. Ngoài subscription, Onway có thu phí cố định từ khách theo đơn/chuyến trong giai đoạn đầu không?
9. Tiêu chí nào được xem là launch thành công để bắt đầu đánh giá quảng cáo?

# 27. Bộ lọc quyết định nghiệp vụ

Trước khi thêm tính năng hoặc quy trình, cần hỏi:

1. Có phù hợp AI First không?
2. Community + AI có thể thực hiện thay vì tăng nhân sự không?
3. Có buộc Onway đứng giữa tiền giao dịch không?
4. Có đưa Onway trở lại commission không?
5. Chi phí vận hành thủ công có tăng tuyến tính theo đơn không?
6. Có thể thiết kế theo hướng xử lý ngoại lệ không?
7. Giá trị kinh doanh có đủ lớn so với độ phức tạp không?

# Phụ lục A - Giá trị cấu hình hiện tại

| Hạng mục | Giá trị/giả thuyết hiện tại |
|---|---|
| Phí nền tảng tài xế ban đầu | `1.000.000 VND`, thu trước kích hoạt |
| Thời gian trả phí | 12 tháng |
| Thời gian tặng thêm | 6 tháng |
| Tổng thời gian ban đầu | 18 tháng |
| Phạm vi ưu đãi | Toàn ứng dụng, không tách theo thành phố |
| Giá trị hoàn của 6 tháng tặng | `0 VND` |
| Phí đăng ký/xử lý hồ sơ tương lai | `500.000 VND`, miễn cho chương trình ra mắt toàn app |
| Đơn vị hoàn phí phần trả tiền | `250.000 VND/3 tháng` |
| Biên độ deal Ride | Future/P1, nếu bật: `-10%` đến `+10%` so với giá Onway đề xuất |
| Food Delivery Fee | P0 dùng phí hệ thống đề xuất; không deal/negotiation |
| Số lần khách đưa giá Ride | Future/P1, nếu bật: 1 lần/yêu cầu |
| Phản hồi của tài xế với Food | P0 Accept hoặc Reject; không Counter Offer |
| Subscription xe máy | `499.000 VND/tháng` hoặc `4.999.000 VND/năm` |
| Subscription ô tô | `999.000 VND/tháng` hoặc `9.999.000 VND/năm` |
| Driver Referral | `50.000 VND` |
| Customer Referral đơn đầu | `10.000 VND` |
| Customer Referral 10 đơn sau | `5.000 VND/đơn` |
| Fraud Case Processing Charge | `200.000 VND` |
| Full menu recapture | 6 tháng |
| Restaurant imagery refresh | Khoảng 6 tháng |
| Xác minh menu tối thiểu | 2 tài xế độc lập |
| Xung đột bằng chứng | Tài xế thứ 3 hoặc manual exception |

# Phụ lục B - State machine nghiệp vụ đề xuất

## Driver Referral

`REFERRED -> REGISTERED -> VERIFIED -> ACTIVATED -> FIRST_TRIP_COMPLETED -> FRAUD_CHECK -> REWARD_ELIGIBLE -> REWARDED`

## Customer Referral

`REFERRED -> REGISTERED -> VERIFIED -> FIRST_SUCCESSFUL_ORDER -> FRAUD_CHECK -> REWARD_ELIGIBLE -> REWARDED`

## Restaurant Mission - FUTURE/P2

`AVAILABLE -> ACCEPTED -> CAPTURING -> SUBMITTED -> AI_QA -> AWAITING_INDEPENDENT_VERIFICATION -> VERIFIED -> FRAUD_CHECK -> REWARD_ELIGIBLE -> PAID`

Trạng thái ngoại lệ: `REJECTED`, `RETAKE_REQUIRED`, `CONFLICT`, `MANUAL_REVIEW`, `EXPIRED`.

## Fraud Case - P0 SHELL, AI STEPS FUTURE/OPTIONAL

P0/manual:

`REPORTED -> EVIDENCE_COLLECTION -> DRIVER_RESPONSE -> HUMAN_REVIEW -> HUMAN_DECISION -> CONFIRMED/REJECTED -> APPEAL -> FINALIZED`

Future/AI-assisted:

`REPORTED -> AI_TRIAGE -> EVIDENCE_COLLECTION -> DRIVER_RESPONSE -> AI_RECOMMENDATION -> HUMAN_DECISION -> CONFIRMED/REJECTED -> APPEAL -> FINALIZED`

## Ride Fee Negotiation - FUTURE/P1

`REQUEST_CREATED -> RECOMMENDED_PRICE_SHOWN -> CUSTOMER_OFFERED_ONCE -> OFFER_RANGE_VALIDATED -> DRIVER_ACCEPTED/DRIVER_REJECTED -> PRICE_AGREED/NEGOTIATION_REJECTED`

Food Delivery Fee negotiation khong thuoc P0.

# Phụ lục C - Tóm tắt ngắn

> **Onway là marketplace Ride + Food 0% commission, ban đầu phục vụ nhân viên văn phòng và sinh viên tại các region polygon nội thành TP. Hồ Chí Minh. Khách nhận giá món không markup; Ride dùng giá đề xuất ở P0 và Food dùng phí giao hàng hệ thống đề xuất, không có thỏa thuận phí giao Food. Tiền giao dịch Ride/Food nằm ngoài Onway: khách chuyển khoản/QR trực tiếp cho tài xế và upload payment proof. Với Food trả trước, tài xế chỉ đi đặt món sau khi payment proof/confirmation đạt điều kiện theo policy; khách không được hoàn nếu đổi ý sau khi tài xế đã đặt món. Doanh thu giai đoạn đầu đến từ phí nền tảng/subscription; quảng cáo, Mission, Community Truth và AI OCR/menu extraction production chỉ được xem xét sau core launch. Tài xế trong chương trình ra mắt toàn app đóng 1.000.000 VND cho 12 tháng, được tặng thêm 6 tháng không quy đổi thành tiền và được miễn phí hồ sơ dự kiến 500.000 VND.**
