# Feature Inventory

| Feature ID | Feature | Priority | Phase | Depends On | Notes |
| --- | --- | --- | --- | --- | --- |
| F-001 | Customer account and phone verification | P0 | P0 | - | Phone OTP login; Firebase custom token via backend provider abstraction |
| F-002 | Driver onboarding and mandatory verification | P0 | P0 | F-001, Admin | Documents configurable by vehicle/service |
| F-003 | Driver activation and platform fee tracking | P0 | P0 | F-002, Monetization policy | Launch package `1.000.000 VND` + 6 months gift |
| F-004 | Region/city/country management with polygon | P0 | P0 | Admin map tooling | Admin can create/draw/edit/pause/resume/publish polygons; no hard delete P0; block overlap for same service/vehicle |
| F-005 | Service and vehicle availability by region | P0 | P0 | F-004 | Ride/Food and motorbike/car rules |
| F-006 | Customer Ride request | P0 | P0 | F-004, F-007 | Recommended/final platform price, no customer manual offer in P0 |
| F-007 | Ride pricing recommendation and guardrails | P0 | P0 | Policy Config | Formula finalized in Technical/G4; PRD requires transparent final platform price and policy guardrails |
| F-008 | Ride matching and driver accept/reject | P0 | P0 | F-006, Driver online | Matching Engine P0 |
| F-009 | Ride payment proof via bank transfer/QR | P0 | P0 | F-008 | Customer pays before driver arrives; proof required by policy |
| F-010 | Ride trip tracking/lifecycle | P0 | P0 | F-008 | REQUESTED, MATCHING, MATCHED, PAYMENT_PENDING, PAYMENT_DISPUTED, MONEY_RECEIVED, DRIVER_EN_ROUTE, ARRIVED, STARTED, COMPLETED, CANCELED |
| F-011 | Food outlet/brand/catalog admin | P0 | P0 | Admin | Brand canonical menu + outlet override |
| F-012 | Customer Food browse/cart/order | P0 | P0 | F-011, F-004 | Shows estimated item price, delivery fee, total |
| F-013 | Food delivery fee recommendation | P0 | P0 | Policy Config | No negotiation P0 |
| F-014 | Food matching and driver accept/reject | P0 | P0 | F-012, Driver online | Driver no Counter Offer |
| F-015 | Food payment proof via bank transfer/QR | P0 | P0 | F-014 | Customer pays driver after driver found |
| F-016 | Food driver order-at-restaurant flow | P0 | P0 | F-015 | Driver orders after proof/confirmation passes policy |
| F-017 | Food item price/status change proposal | P0 | P0 | F-016 | In-app proposal is source of truth; customer Accept/Reject before affected purchase; 5-minute configurable timeout |
| F-018 | Food cancellation after driver ordered | P0 | P0 | F-016 | No refund if customer changes mind after order placed |
| F-019 | Customer-driver direct phone and active chat | P0 | P0 | Active Ride/Food | Real phone number; chat text/image retention 1 week; one image per message in P0 |
| F-020 | Rating/report/complaint intake | P0 | P0 | Completed/active service | 5-star rating + quick tags; complaint not automatically fraud |
| F-021 | Complaint/dispute manual lifecycle | P0 | P0 | F-020, Evidence | Human review and decision |
| F-022 | Fraud/risk minimal controls | P0 | P0 | F-021 | Risk status, eligibility, manual/admin lock and conservative auto-lock: paid/no-show, severe safety/fraud, 3 valid complaints/30 days, repeated payment dispute |
| F-023 | Media/evidence and audit trail | P0 | P0 | Cross-cutting | Payment proof, chat image, complaint evidence |
| F-024 | Policy config engine | P0 | P0 | Admin | Region, currency, timeout, threshold, fee policy |
| F-025 | Analytics/events baseline and ops dashboard | P0 | P0 | Core flows | Log critical events + basic Admin ops dashboard; no complex real-time BI P0 |
| F-026 | Merchant App | P2 | Future | Food catalog model | Not required P0 |
| F-027 | Ride price negotiation / customer manual offer | P2 | Future | F-006, F-007, F-008 | Removed from P0 by D-024; future may revisit priority bonus/surge after match-rate data |
| F-028 | Trust Engine full | P2 | Future | Fraud/risk history | Not dependency for P0 |
| F-029 | Mission Engine | P2 | Future | AI QA, Community Truth | Driver field tasks |
| F-030 | Community Truth Engine | P2 | Future | Evidence/confidence model | Verified data by multiple independent drivers |
| F-031 | AI Restaurant Lifecycle/OCR production | P2 | Future | Mission/Community Truth | OCR/menu extraction not P0 |
| F-032 | Referral rewards | P1 | Future | Fraud validation | Driver/customer referral values configurable |
| F-033 | Advertising | P2 | Future | Traffic threshold deferred to marketing/post-launch | Sponsored content clearly labeled |
| F-034 | Push notification baseline | P0 | P0 | Core flows | Job, payment, chat and lock notifications; no marketing push P0 |
