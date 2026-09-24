# Integrations

| Integration | Purpose | Auth/Security | Environment | Notes |
| --- | --- | --- | --- | --- |
| Firebase Auth | Identity provider and ID token verification | Backend verifies Firebase ID token, maps to internal users | All | ViHAT OTP flow creates Firebase custom token; not Firebase phone auth directly |
| ViHAT SMS/OTP | OTP delivery in Vietnam | Backend owns OTP challenge/verification; provider abstraction `SmsProvider` | Vietnam MVP | Rate limit: 5 request/phone/hour, 10 request/device/day |
| HERE Maps | Map, geocoding/routing, map UI support | API keys/secrets managed securely | All | Retry transient failure, cache route/geocode where valid, fail gracefully when no route/geocode |
| AWS RDS PostgreSQL | Primary relational database | Private networking/IAM/secrets | Production | PostGIS required; automated backup/PITR if cost acceptable |
| PostGIS | Geospatial queries | DB-level extension and controlled raw SQL | Production/local dev | Region polygon, distance, geofence, containment |
| ElastiCache Redis | Cache, presence, ephemeral matching state, BullMQ | Private network, auth/TLS where supported by environment | Production | Not system of record |
| BullMQ | Async jobs | Runs on Redis | Backend | Notifications, fraud/risk, evidence, audit/analytics, future AI/OCR/Mission |
| AWS S3 | Media/evidence storage | Private bucket/prefix by default, signed URL for sensitive files | Production | Public/CDN only after review/policy |
| CloudWatch | Logs/metrics baseline | AWS IAM | Production | MVP minimum; Sentry/OpenTelemetry not a blocker now |
| AWS Secrets Manager/SSM | Secrets/config storage | IAM | Production | Alternative env file only if tightly controlled early |
| EC2 | Backend deployment target | SSH/deploy user, firewall/security group | Production | Simple MVP deployment |
| GitHub Actions | CI/CD | Repo secrets, SSH key or artifact deploy credentials | CI/CD | Lint/typecheck/test/build, deploy to EC2 |
| Dynamic VietQR | Direct customer -> driver bank transfer QR | Encodes driver bank/account, amount, order/trip reference | Ride/Food P0 | Onway does not collect or guarantee bank transaction |
| OnePAY / payment gateway | Not used for Ride/Food P0 | n/a | Excluded P0 | D-025: keep direct customer -> driver transfer; revisit only with a new payment decision |
