# Security And Privacy

Retention policy below is a product/technical draft, not legal approval. It follows the Vietnam PDPD principle that personal data should be stored only for a period appropriate to the processing purpose, with deletion handled according to applicable legal exceptions.

## Data Classes

| Data | Sensitivity | Storage | Retention | Notes |
| --- | --- | --- | --- | --- |
| Phone number | Personal data | PostgreSQL/Firebase | Account lifetime + 24 months after closure/deactivation, unless legal hold | Real phone visible between customer and driver in MVP |
| Firebase identity mapping | Personal/security | PostgreSQL | Account lifetime + 24 months after closure/deactivation, unless legal hold | Internal user/customer/driver/admin mapping |
| Driver KYC/documents | Highly sensitive | S3 private + DB metadata | Active driver lifetime + 5 years after deactivation/last platform activity, pending legal review | Signed URL only, admin access audited |
| GPS/location history | Sensitive | Redis ephemeral + PostgreSQL snapshots/history | Redis last-known/presence: hours to 24h; detailed route/location history: 90 days; case-linked GPS: follow complaint/fraud retention | Background location consent required |
| Trip/order trace | Sensitive business/personal | PostgreSQL | 5 years after completion/cancellation, pending legal review | Needed for dispute/audit |
| Payment bill/transfer receipt | Sensitive financial evidence | S3 private + DB metadata | 3 years after trip/order completion; 5 years if complaint/fraud-linked | Evidence, not official bank confirmation |
| Fraud/complaint evidence | Highly sensitive | S3 private + PostgreSQL | 5 years after case finalization; longer under legal hold | Preserve if attached to case |
| Chat messages/images | Personal/evidence | PostgreSQL/S3 private | 1 week P0 unless preserved for dispute | Active Ride/Food only |
| Device metadata/fingerprint | Sensitive | PostgreSQL, risk tables | Rolling 12 months; 5 years if fraud/complaint-linked | Collect minimum needed; hash/pseudonymize device id where possible |
| AI profiling/risk scoring | Sensitive | Not production in P0; future DB/risk store | Future default: 12 months for raw signals, 24 months for score snapshots, case-linked data follows complaint/fraud retention | Future; P0 only stores reason-code risk controls and audit |
| Audit log | Sensitive ops/compliance | PostgreSQL | 7 years, append-only where practical | Should be immutable in design |
| Admin access log | Sensitive security | PostgreSQL/CloudWatch | 2 years minimum | Includes sensitive evidence/KYC access events |

## Controls

- Auth: Firebase Auth ID token verified by backend; ViHAT OTP via backend custom token flow.
- Authorization: backend guards for customer/driver/admin/operator; Admin Portal uses RBAC draft in `doc/2-PRD/07-permission-matrix.md`.
- Encryption: TLS for all client/server traffic; S3 private signed URLs for sensitive media; database/storage encryption to be configured in AWS.
- Consent: explicit in-app consent is required for background location, device/risk collection, direct phone visibility, payment proof/evidence upload and sensitive fraud review. Consent version is stored in `ConsentRecord`.
- Background location: Driver App shows persistent visible status while online/background tracking is active; customer-facing tracking is limited to active service rooms.
- Deletion/export: support data deletion/export requests, with exceptions for legal, audit, fraud, complaint and safety retention.
- Logging/audit: audit trail required for policy/config changes, admin/operator actions, state transitions, accept/reject, driver ordered-food milestone, payment proof, AI recommendations, human decisions and fraud/dispute lifecycle.
- Abuse protection: OTP `5 request/phone/hour`, `10 request/device/day`; OTP verify `5 attempts/challenge`; GraphQL/WebSocket/location use per user/device/IP throttles, exponential reconnect backoff and impossible-jump/spam detection.
- Device identity: collect device id/fingerprint for fraud/risk in MVP, minimize fields, hash/pseudonymize stable identifiers, avoid using it for unrelated marketing.
- Privacy: AI profiling production is future; any risk scoring must be explainable to admins through reason codes and audit, not opaque automated final decisions in P0.

## Legal References

- Vietnam Decree 13/2023/ND-CP on personal data protection requires personal data storage to be appropriate to the processing purpose and provides deletion rules/exceptions. Official text: https://chinhphu.vn/?classid=1&docid=207759&pageid=27160&typegroupid=4
