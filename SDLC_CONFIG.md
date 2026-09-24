# SDLC Config

> Bật/tắt module checklist theo từng dự án. Không dùng file này để chốt technical chi tiết; technical sẽ nằm trong `doc/3-TECHNICAL`.

## Project Preset

| Mục | Chọn |
| --- | --- |
| App archetype | Ride hailing + food delivery; marketplace/multi-role hybrid |
| Platform | iOS / Android / Web app / Admin-CMS / Backend-API |
| Release target | Production đầy đủ |
| Technical stack fixed? | G4 freeze: Nx, NestJS modular monolith (`backend-api` GraphQL + WebSocket), PostgreSQL/PostGIS, Prisma, Redis/BullMQ, Firebase Auth + ViHAT OTP, HERE Maps, AWS EC2/RDS/ElastiCache/S3/CloudWatch/SSM |
| Default language | Tiếng Việt |

## Optional Modules

| Module | Enabled | Notes |
| --- | --- | --- |
| Backend/API | Yes | NestJS modular monolith draft; xem `doc/3-TECHNICAL/**` |
| Admin/CMS | Yes | Quản lý region, pricing/policy, driver, food catalog, complaint/fraud, rollout |
| AI/OCR | Future | AI-first là nguyên tắc; AI OCR/menu extraction production không thuộc P0 |
| Auth/account | Yes | Customer/Driver/Admin; driver onboarding và xác minh bắt buộc |
| Payment/IAP/subscription | Yes | P0 dùng bank transfer/QR trực tiếp và payment proof; không gateway/wallet/COD/cash cho Ride/Food |
| Ads | Future | Không thuộc giai đoạn ra mắt |
| Push notification | Yes | P0 job/payment/chat/lock push; no marketing push |
| Upload/media | Yes | Payment proof, chat image, complaint/evidence |
| Offline/local-first | No | P0 không offline-first; chỉ retry/idempotency cho critical actions |
| Analytics | Yes | Marketplace, driver, customer, food, fraud, monetization metrics |
| Kids/privacy sensitive | No | Không target trẻ em; vẫn có dữ liệu GPS/device/payment proof cần consent/privacy review |
| User-generated content | Yes | Rating, complaint, chat image, evidence |
| Multi-language | Future | Ngôn ngữ chính hiện tại: Tiếng Việt; multi-country là tương lai |

## Delivery Defaults

| Mục | Giá trị mặc định |
| --- | --- |
| ORCA concurrency target | High: 4-8 tasks song song |
| Progress tracking | Markdown simple |
| Token policy | Compact task packets, reference docs by path |
| Code skeleton | Chỉ tạo sau Technical gate |
