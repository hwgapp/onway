# Technical Decisions

| ID | Ngày | Decision | Reason | Impact | Status |
| --- | --- | --- | --- | --- | --- |
| ADR-001 | 2026-09-11 | Dùng Nx monorepo cho toàn bộ hệ thống. | Quản lý backend, web, admin, mobile và shared packages cùng repo. | Scaffold monorepo sau G4 freeze. | Accepted G4 |
| ADR-002 | 2026-09-11 | Backend dùng Node.js + NestJS theo modular/domain architecture. | Phù hợp TypeScript và domain module rõ. | Module boundary nằm trong `01-architecture.md`. | Accepted G4 |
| ADR-003 | 2026-09-11 | GraphQL là API chính cho business operations. | Phù hợp profile, lifecycle, admin config, menu, fraud/risk. | WebSocket riêng cho realtime cao tần. | Accepted G4 |
| ADR-004 | 2026-09-11 | Không dùng GraphQL Subscription làm kênh chính cho location/matching; dùng WebSocket riêng. | GPS/location/matching cần nhẹ, ổn định, scale và kiểm soát reconnect/backpressure. | Cần protocol WebSocket. | Accepted G4 |
| ADR-005 | 2026-09-11 | Primary database là PostgreSQL trên AWS RDS. | Relational/system of record cho core marketplace. | Local dev DB vẫn bắt buộc. | Accepted G4 |
| ADR-006 | 2026-09-11 | Bắt buộc dùng PostGIS cho geospatial. | Region polygon, containment, distance, geofence. | Raw SQL PostGIS cần kiểm soát. | Accepted G4 |
| ADR-007 | 2026-09-11 | Redis dùng cho cache, realtime presence, ephemeral matching state và BullMQ queue. | Cần tốc độ cho matching/realtime. | Redis không là system of record. | Accepted G4 |
| ADR-008 | 2026-09-11 | Dùng Firebase Auth. | Backend verify Firebase ID token, map user nội bộ. | ViHAT OTP tạo Firebase custom token. | Accepted G4 |
| ADR-009 | 2026-09-11 | Dùng HERE Maps. | Google Maps không phù hợp/khả dụng theo quyết định sản phẩm hiện tại. | Cần quota/fallback policy. | Accepted G4 |
| ADR-010 | 2026-09-11 | Dùng ViHAT cho SMS/OTP tại Việt Nam. | Local OTP provider. | Cần `SmsProvider` abstraction. | Accepted G4 |
| ADR-011 | 2026-09-11 | Onway không làm payment gateway cho tiền Ride/Food MVP. | Theo money-light BRD/PRD. | Dùng direct-payment-proof/bank-transfer-confirmation/settlement-evidence. | Accepted G4 |
| ADR-012 | 2026-09-11 | Platform fee/subscription là khoản Onway thu trực tiếp nhưng MVP chưa tích hợp cổng thanh toán. | Launch đơn giản. | Driver upload proof/reference, admin verify thủ công. | Accepted G4 |
| ADR-013 | 2026-09-11 | Dùng AWS cho cloud. | Hạ tầng phổ biến, phù hợp stack đã chọn. | EC2/RDS/ElastiCache/S3/CloudWatch/Secrets. | Accepted G4 |
| ADR-014 | 2026-09-11 | CI/CD simple trước, deploy lên EC2. | Giữ MVP đơn giản. | GitHub Actions, health check, rollback tối thiểu. | Accepted G4 |
| ADR-015 | 2026-09-11 | Hiện chỉ có một production environment duy nhất. | Giữ đơn giản MVP. | Cần local dev DB và deploy discipline; staging future. | Accepted G4 - risk accepted |
| ADR-016 | 2026-09-11 | Backup/restore baseline: RDS automated backup, PITR nếu cost acceptable và test restore trước true production. | Production cần recoverability. | G4 deployment phải có backup/restore checklist. | Accepted G4 |
| ADR-017 | 2026-09-11 | Audit trail bắt buộc. | Cần vận hành, fraud, compliance. | Audit policy cross-cutting. | Accepted G4 |
| ADR-018 | 2026-09-24 | Data retention có baseline kỹ thuật/sản phẩm trong `06-security-privacy.md`. | User yêu cầu Codex suggest; retention phải đủ vận hành/fraud/dispute nhưng không giữ quá mục đích xử lý. | Pending legal approval; không coi là legal advice. | Accepted G4 - legal review pending |
| ADR-019 | 2026-09-11 | Privacy controls baseline: explicit consent for background location, device/risk, phone visibility, evidence upload; support export/delete with legal/audit/fraud exceptions. | GPS, device, evidence, AI/risk scoring và phone visibility là sensitive. | Legal review vẫn cần trước production, nhưng không block G4. | Accepted G4 - legal review pending |
| ADR-020 | 2026-09-11 | Landing Web dùng Next.js. | Web landing tách với admin. | App trong Nx monorepo. | Accepted G4 |
| ADR-021 | 2026-09-11 | Admin Portal dùng ReactJS, shadcn/ui và Animate UI. | Admin web vận hành P0. | RBAC và module screens cần thiết kế. | Accepted G4 |
| ADR-022 | 2026-09-11 | Customer App và Driver App dùng Flutter. | Mobile cross-platform, tách binary. | Reuse shared packages. | Accepted G4 |
| ADR-023 | 2026-09-11 | Backend MVP là NestJS modular monolith. | Domain còn thay đổi, monolith giúp iterate nhanh hơn microservices. | Giữ module boundary để tách sau. | Accepted G4 |
| ADR-024 | 2026-09-11 | Matching dùng batched parallel/wave dispatch. | Cân bằng tốc độ, fairness và scale. | Wave 1 top 3, wave 2 thêm 3-5 là đề xuất config. | Accepted G4 |
| ADR-025 | 2026-09-11 | Mỗi driver chỉ có một active offer tại một thời điểm. | Tránh nhận đồng thời nhiều offer. | Cần atomic lock Redis/DB. | Accepted G4 |
| ADR-026 | 2026-09-11 | Manual accept timeout cấu hình theo service, mặc định Ride 15s/Food 20s mỗi wave. | Ride cần nhanh, Food cần đọc thêm thông tin. | Không hard-code. | Accepted G4 |
| ADR-027 | 2026-09-11 | Hỗ trợ manual accept và auto-accept với guardrail. | Tăng tốc matching nhưng cần tránh conflict/risk. | Matching chọn một driver score tốt nhất khi nhiều auto-accept hợp lệ. | Accepted G4 |
| ADR-028 | 2026-09-11 | Customer hủy trước khi matched không ảnh hưởng P0 risk lock. | Trust Engine đầy đủ sau P0. | Risk policy đơn giản hơn. | Accepted G4 |
| ADR-029 | 2026-09-11 | Food prepaid QR/bank transfer là thỏa thuận trực tiếp customer-driver, app lưu proof/trạng thái. | Onway không thu hộ/giữ tiền. | Driver đặt món sau khi confirm received trừ policy override. | Accepted G4 |
| ADR-030 | 2026-09-11 | ViHAT OTP -> backend verify -> Firebase custom token -> Firebase ID token. | Không dùng Firebase phone auth trực tiếp. | Backend quản lý OTP provider abstraction. | Accepted G4 |
| ADR-031 | 2026-09-11 | Driver App cần background location. | Driver online, matching, active Ride/Food và future Mission cần GPS. | Cần consent, battery và retention policy. | Accepted G4 |
| ADR-032 | 2026-09-11 | QR chuyển khoản dùng dynamic VietQR theo đơn/số tiền khi có bank info driver. | Giảm sai amount/reference. | QR encode account, amount, reference. | Accepted G4 |
| ADR-033 | 2026-09-11 | Customer App và Driver App tách deploy riêng trong monorepo, reuse shared packages. | Permission/trải nghiệm/phát hành khác nhau. | Không trộn hai app thành một binary. | Accepted G4 |
| ADR-034 | 2026-09-11 | Admin Portal gọi GraphQL trực tiếp, không dùng BFF MVP. | Giữ đơn giản. | Backend cần RBAC/guard/audit tốt. | Accepted G4 |
| ADR-035 | 2026-09-11 | Admin Portal bắt buộc day 1 cho vận hành P0. | Không phụ thuộc script/manual DB cho luồng chính. | Region, rollout, pricing, driver, fee, catalog, monitor, complaint/fraud, audit. | Accepted G4 |
| ADR-036 | 2026-09-11 | AI OCR/menu extraction không nằm trong P0 launch. | Food P0 admin-first. | Schema/UI nên có đường mở rộng media/evidence. | Accepted G4 |
| ADR-037 | 2026-09-11 | Dùng Prisma làm database access layer chính. | Tốt cho relational CRUD/transaction/migration. | PostGIS raw SQL có kiểm soát qua repository/service. | Accepted G4 |
| ADR-038 | 2026-09-11 | Dùng BullMQ + Redis cho MVP queue. | Đã có Redis, dễ debug với modular monolith. | Future có thể chuyển SQS/EventBridge. | Accepted G4 |
| ADR-039 | 2026-09-11 | Backend MVP deploy trên EC2 bình thường. | Launch nhanh và đơn giản. | PM2/systemd, Nginx/Caddy, logs CloudWatch. | Accepted G4 |
| ADR-040 | 2026-09-11 | Dùng GitHub Actions CI/CD simple deploy EC2 qua SSH/copy artifact. | Quy trình MVP đủ đơn giản. | Deploy script idempotent, health check, rollback. | Accepted G4 |
| ADR-041 | 2026-09-11 | NestJS GraphQL code-first. | Giảm duplication, phù hợp TypeScript/NestJS. | Generate `schema.gql`; review breaking changes. | Accepted G4 |
| ADR-042 | 2026-09-11 | S3 media phân loại private signed URL và public/CDN asset. | Bảo vệ evidence/KYC/payment proof. | Upload ban đầu vào private bucket/prefix. | Accepted G4 |
| ADR-043 | 2026-09-11 | Food prepaid confirmation có nút customer "Đã chuyển tiền" + upload proof và driver "Đã nhận tiền". | Ghi nhận trạng thái/evidence cho money-light flow. | State transition audit bắt buộc. | Accepted G4 |
| ADR-044 | 2026-09-11 | Customer-driver chat P0 cho active Ride/Food, text và image. | BRD yêu cầu chat P0, retention 1 tuần. | GraphQL history/mutations, WebSocket events, S3 private media. | Accepted G4 |
| ADR-045 | 2026-09-24 | Generate typed GraphQL client/models cho Flutter ngay từ đầu; React Admin cũng dùng typed GraphQL codegen nếu tooling cho phép. | Giảm runtime bug khi schema GraphQL thay đổi và giúp mobile contract rõ hơn. | Scaffold cần chọn Flutter GraphQL generation tool và query document convention. | Accepted G4 |
| ADR-046 | 2026-09-24 | Observability MVP dùng CloudWatch tối thiểu; Sentry/OpenTelemetry chưa là blocker. | User muốn setup sau và không ưu tiên ngay. | Vẫn cần log/metric baseline khi deploy EC2; nâng cấp observability sau. | Accepted G4 |
| ADR-047 | 2026-09-24 | MVP thu thập device id/fingerprint tối thiểu để phục vụ fraud/risk. | User chốt có thu thập device id/fingerprint. | Ưu tiên hash/pseudonymous identifiers, consent/privacy review và retention 12 tháng rolling. | Accepted G4 - legal/privacy review pending |
| ADR-048 | 2026-09-24 | Admin RBAC P0 dùng role mặc định do Codex đề xuất: Super Admin, Ops Admin, Support Operator, Driver Ops, Catalog Manager, Finance Ops, Risk/Fraud Analyst, Viewer/Auditor. | Cần đủ vận hành nhưng không quá phức tạp. | Permission matrix nằm trong `doc/2-PRD/07-permission-matrix.md`; actions nhạy cảm cần reason/audit. | Accepted G4 |
| ADR-049 | 2026-09-24 | P0 dùng một NestJS deployable `backend-api` cho cả GraphQL và WebSocket. | Giữ deployment MVP đơn giản, vẫn tách module/protocol boundary. | Separate realtime deployable là future khi traffic/ownership cần. | Accepted G4 |
| ADR-050 | 2026-09-24 | Future modules Trust/Mission/Community Truth/Referral/Ads chỉ reserve interface/folder sau scaffold, không có runtime logic P0. | Tránh scope creep nhưng giữ đường mở rộng. | Không tạo fake business logic cho future modules. | Accepted G4 |
| ADR-051 | 2026-09-24 | Rate limit baseline: OTP `5 request/phone/hour`, `10 request/device/day`, `5 verify attempts/challenge`; GraphQL/WS/location throttle theo user/device/IP. | Giảm abuse trước khi có full security tuning. | G4 implementation phải có rate-limit module và config. | Accepted G4 |
| ADR-052 | 2026-09-24 | Driver location frequency: `5s` khi online, `2s` khi active trip/order; spam/impossible jump bị throttle và risk flag. | Cân bằng realtime, pin, chi phí và fraud/risk. | WebSocket/location service cần guardrail. | Accepted G4 |
| ADR-053 | 2026-09-24 | HERE Maps fallback: retry transient error, dùng cache còn valid, fail gracefully nếu không route/geocode được. | Map provider có quota/lỗi mạng, app cần UX ổn. | Map-routing module cần cache và error policy. | Accepted G4 |
| ADR-054 | 2026-09-24 | Mobile release baseline: TestFlight, Google Play Internal Testing và backend min-version/force-update config. | Cần kiểm soát release mobile và forced update khi contract/security đổi. | App gọi `getAppVersionPolicy` khi start. | Accepted G4 |
| ADR-055 | 2026-09-24 | Evidence media/payment proof/chat image/KYC upload vào S3 private bucket/prefix; dùng signed URL có audit. | Dữ liệu nhạy cảm không public/CDN mặc định. | Media module phân loại retention/access. | Accepted G4 |
| ADR-056 | 2026-09-24 | Scaffold được phép sau G4 theo path trong `01-architecture.md`; chưa tạo trước G4. | User chốt default tạo code skeleton sau G4. | Sau G4 có thể tạo Nx/backend/mobile/admin skeleton theo task riêng. | Accepted G4 |
