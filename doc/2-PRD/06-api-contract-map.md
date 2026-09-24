# API Contract Map

> Cấp product contract. Technical chi tiết ở `doc/3-TECHNICAL/03-api-design.md`.

| Contract ID | Feature | Operation / Endpoint | Input Summary | Output Summary | Notes |
| --- | --- | --- | --- | --- | --- |
| API-001 | Auth | `startOtpChallenge` | Phone number | Challenge status | ViHAT OTP provider abstraction |
| API-002 | Auth | `verifyOtp` | Challenge id, OTP | Firebase custom token | App signs in Firebase, then uses ID token |
| API-003 | Device risk | `upsertDeviceIdentity` | Hashed/pseudonymous device id and risk signals | Device/risk record | Fraud/risk only, privacy review required |
| API-004 | Ride request | `createRideRequest` | Pickup, dropoff, vehicle type | Ride request, recommended/final platform price | Pickup/start must be active region; dropoff may be outside if policy allows; no customer manual offer P0 |
| API-005 | Ride matching | `acceptRideOffer` | Offer id | Assigned ride | First valid accept wins; driver sees platform final price |
| API-005A | Ride matching | `rejectRideOffer` | Offer id, reason optional | Offer rejected state | Driver rejects customer/recommended offer; no Counter Offer |
| API-006 | Ride lifecycle | `updateRideState` | Ride id, transition, metadata | Updated ride state | Audit required |
| API-007 | Food order | `createFoodOrder` | Outlet, items, delivery address | Food order, delivery fee, estimated total | No Food delivery fee negotiation P0 |
| API-008 | Food matching | `acceptFoodOffer` | Offer id | Assigned food order | Driver Accept/Reject only |
| API-009 | Direct payment proof | `submitPaymentProof` | Service ref, image/media, transfer metadata | Proof status | Evidence only, not bank confirmation |
| API-010 | Direct payment confirmation | `confirmMoneyReceived` | Service ref | Payment confirmation state | Driver button confirms "received full amount"; required before Food order-at-restaurant unless policy override |
| API-010A | Direct payment dispute | `markPaymentDisputed` | Service ref, reason code, evidence optional | Payment disputed state | SOP/manual review, not gateway verification |
| API-011 | Food change proposal | `submitFoodChangeProposal` | Order id, changed item/price/status, evidence/note | Proposal with 5-minute default timeout | Customer must decide before affected purchase; supplemental transfer required before buying affected item when price increases |
| API-012 | Food change decision | `decideFoodChangeProposal` | Proposal id, accept/reject | Updated order/proposal state | Audit required |
| API-013 | Chat | `sendChatMessage` | Room id, text/media | Chat message | WebSocket pushes events |
| API-014 | Complaint | `createComplaint` | Service ref, category, description, evidence | Complaint record | Complaint does not equal fraud confirmed |
| API-015 | Fraud/dispute | `advanceFraudCase` | Case id, transition, decision/evidence | Fraud case state | Human review P0 |
| API-015A | Driver risk lock | `applyDriverRiskLock` | Driver id, lock type, reason, source, case ref optional | Updated risk/lock state | Supports manual/admin lock and auto-lock events; audit required |
| API-015B | Driver lock appeal | `submitDriverLockAppeal` | Lock id, driver statement, evidence optional | Appeal case | Driver app appeal form |
| API-016 | Region admin | `upsertRegion` | Region fields, polygon, lifecycle | Region config | Admin polygon tool; no hard delete P0 |
| API-016A | Region publish | `publishRegionConfig` | Region/version id | Published config or validation error | Blocks overlap for same service/vehicle |
| API-017 | Policy admin | `updatePolicyConfig` | Scope, key, value, version | Draft/published config | Audit required |
| API-018 | Driver onboarding | `submitDriverDocuments` | Driver profile, vehicle/service docs | Review status | Driver Ops review |
| API-019 | Platform fee | `submitPlatformFeeProof` | Driver id, proof media, reference | Pending verification | Finance Ops verifies manually |
| API-020 | Catalog admin | `upsertBrandOutletMenu` | Brand/outlet/menu/modifier/override data | Catalog draft/published state | Food P0 admin-first |
| API-021 | Rating | `submitRating` | Service ref, 5-star rating, tags | Rating record | Separate from complaint/fraud |
| API-022 | Notification | `registerPushToken` | Device token, platform, user context | Push token registration | Job/payment/chat/lock push only in P0 |
| WS-001 | Driver realtime | `driver.location` | Location, heading/speed, service flags | Ack | Rate limit covered by OQ-015 |
| WS-002 | Matching realtime | `matching.offer` | Server to driver offer payload | Driver sees offer | One active offer per driver |
| WS-003 | Tracking realtime | `tracking.update` | Server to service room | Customer/driver/admin tracking update | Room-scoped |
| WS-004 | Chat realtime | `chat.message_created/read/delivered` | Server to participants | Message status | Reconnect must refetch sequence gaps |
