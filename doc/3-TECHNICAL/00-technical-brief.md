# Technical Brief

## Stack Summary

- Monorepo: Nx.
- Backend: Node.js + NestJS modular monolith, modular/domain architecture.
- API: GraphQL là API chính cho business operations; NestJS GraphQL code-first.
- Realtime: WebSocket gateway chạy trong cùng NestJS app P0 cho location, presence, matching, tracking và chat events; có thể tách deploy sau.
- Database: PostgreSQL trên AWS RDS, bắt buộc PostGIS cho geospatial.
- Data access: Prisma; PostGIS query phức tạp dùng raw SQL có kiểm soát.
- Cache/presence/queue: Redis, BullMQ.
- Auth: Firebase Auth với ViHAT OTP qua backend custom token flow.
- Maps: HERE Maps.
- Frontend: Next.js landing, ReactJS Admin Portal, Flutter Customer App và Driver App.
- Cloud/deploy: AWS, EC2 simple deployment, RDS, ElastiCache Redis, S3, CloudWatch, Secrets Manager hoặc SSM.
- Typed clients: generate typed GraphQL client cho Flutter; React Admin dùng typed GraphQL codegen nếu không có blocker tooling.

## Architecture Summary

MVP dùng modular monolith thay vì microservices để giữ tốc độ thay đổi nhanh trong khi domain còn đang được làm rõ. Boundary vẫn tách theo module để sau này có thể tách service nếu traffic hoặc ownership yêu cầu.

GraphQL xử lý business data/profile/order/admin config. WebSocket xử lý realtime tần suất cao như driver location, availability, matching, tracking và chat events. Redis giữ presence/location ngắn hạn và lock/ephemeral matching state; PostgreSQL/PostGIS là system of record cho nghiệp vụ, polygon, audit, evidence và state quan trọng.

## Key Decisions

- Nx monorepo cho backend, web, admin, mobile apps và shared packages.
- Backend MVP là NestJS modular monolith.
- GraphQL code-first là API business chính.
- Không dùng GraphQL Subscription làm kênh chính cho location/matching.
- PostgreSQL/PostGIS là primary database/geospatial layer.
- Firebase Auth không dùng phone auth trực tiếp; ViHAT OTP -> backend -> Firebase custom token.
- Ride/Food payment không dùng OnePAY/gateway/wallet/escrow; chỉ lưu proof/evidence/audit cho direct customer -> driver transfer.
- Platform fee là module riêng, tách khỏi Ride/Food direct payment proof.
- Admin Portal là bắt buộc day 1.
- Device id/fingerprint được thu thập ở mức tối thiểu để phục vụ fraud/risk, ưu tiên hash/pseudonymous identifiers.
- Observability MVP dùng CloudWatch tối thiểu; Sentry/OpenTelemetry không phải blocker ban đầu.
- Rate limits P0: OTP `5 request/phone/hour`, `10 request/device/day`; GraphQL/WS/location có throttle theo user/device/IP.
- Driver location frequency: `5s` khi online, `2s` khi active trip/order; spam hoặc impossible jump bị throttle/flag risk.
- Mobile release P0 có min-version/force-update config; dùng TestFlight và Google Play Internal Testing trước production.
- AI OCR/menu extraction, Mission, Community Truth là future sau P0.

## Risks

- Code scaffold chỉ được tạo sau G4 pass theo path trong `01-architecture.md`; chưa tạo trong tài liệu này.
- Một production environment duy nhất có rủi ro deploy/migration nếu không có local dev DB, backup, rollback và health check tốt.
- Data retention, device identity, RBAC, rate limit và privacy consent đã có G4 baseline; legal review vẫn cần trước production.
- Payment proof không phải xác nhận ngân hàng chính thức, dễ phát sinh dispute nếu flow/audit không rõ.
- Background location cần consent, UX trạng thái rõ ràng, battery strategy và retention policy.
