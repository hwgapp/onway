# API Design

## API Style

GraphQL is the primary API for structured business operations: profile, Ride/Food lifecycle, restaurant/menu data, admin portal, policy/config, complaint/fraud and future Trust/Mission workflows.

NestJS GraphQL uses code-first. Backend generates `schema.gql` in CI as the frontend contract. Flutter should use generated typed GraphQL clients/models from schema + query documents. React Admin should also use typed GraphQL codegen unless tooling blocks it.

WebSocket Gateway is separate from GraphQL at protocol/module level for high-frequency realtime, but runs inside the same NestJS `backend-api` deployable in P0. GraphQL Subscription is not the main channel for location/matching.

## Abuse Limits

| Area | G4 Default |
| --- | --- |
| OTP request | `5 request/phone/hour`, `10 request/device/day`, provider/IP anomaly logging |
| OTP verify | `5 attempts/challenge`, lock challenge after failure burst |
| GraphQL mutation | Per user/device throttle; stricter limits for auth, payment proof, complaint and admin publish actions |
| WebSocket connect | Exponential backoff on reconnect, capped attempts per device/IP/window |
| Driver location | Accept every `5s` when online, every `2s` during active trip/order; drop/throttle faster spam and flag impossible jumps |

## Contracts

| Operation | Input | Output | Errors | Notes |
| --- | --- | --- | --- | --- |
| `startOtpChallenge` | phone number | challenge id/status | rate limited, invalid phone | Backend sends OTP via ViHAT |
| `verifyOtp` | challenge id, OTP | Firebase custom token | expired, invalid, too many attempts | App signs in Firebase with custom token |
| GraphQL auth context | Firebase ID token | internal user/customer/driver/admin | unauthorized, disabled user | Backend verifies token |
| `upsertDeviceIdentity` | hashed/pseudonymous device id, app/platform signals | device identity/risk record | forbidden, invalid signal, rate limited | Used for fraud/risk; privacy review required |
| `recordConsent` | consent type, version, decision | consent record | invalid version, forbidden | Background location/device/evidence/phone visibility |
| `getAppVersionPolicy` | app, platform, current version | min/latest version, force-update flag | unsupported app/platform | Mobile force update/min version |
| `createRideRequest` | pickup, dropoff, vehicle type | ride request + recommended/final platform price | outside region, no service, validation | Ride P0 has no customer manual offer/price negotiation |
| `acceptRideOffer` | offer id | assigned ride | expired, active offer conflict, risk blocked | First valid accept wins |
| `updateRideState` | ride id, transition | updated state | invalid transition, forbidden | Audit required |
| `createFoodOrder` | outlet, items, address | order + delivery fee + estimate | outlet closed, item unavailable, outside region | Food fee not negotiable P0 |
| `acceptFoodOffer` | offer id | assigned food order | expired, active offer conflict, risk blocked | Driver no counter offer |
| `submitPaymentProof` | service ref, media, transfer metadata | proof status | invalid state, upload failed, rate limited | Required for Ride/Food payment flows |
| `confirmMoneyReceived` | order/trip ref | payment state | forbidden, invalid state, rate limited | Driver confirms full amount received before proceeding |
| `markPaymentDisputed` | service ref, reason, optional evidence | payment disputed state | forbidden, invalid state, duplicate | Direct-transfer SOP/manual review |
| `submitFoodChangeProposal` | order id, item/price/status change | proposal with default 5-minute timeout | invalid state | Customer must accept/reject before affected purchase |
| `decideFoodChangeProposal` | proposal id, accept/reject | order update | expired, invalid state | Audit required |
| `sendChatMessage` | room id, text/media | message | room closed, forbidden, upload failed | WebSocket pushes events |
| `createComplaint` | service ref, category, description, evidence | complaint | invalid service, duplicate recent complaint, rate limited | Complaint != fraud confirmed |
| `advanceFraudCase` | case id, transition/decision | case state | forbidden, invalid transition | Human review P0 |
| `applyDriverRiskLock` | driver id, lock type, reason, source, case ref optional | risk/lock state | forbidden, invalid reason, policy disabled | Supports manual/admin lock and auto-lock events |
| `upsertRegion` | polygon/config | region | invalid polygon, overlap same service/vehicle, validation | Admin only |
| `updatePolicyConfig` | scope, key, value, version | published/draft config | validation, conflict | Audit required |
| WebSocket `driver.location` | location, heading/speed, service flags | ack | unauthorized, rate limited | Driver online/active only |
| WebSocket `matching.offer` | server -> driver | offer payload | n/a | One active offer per driver |
| WebSocket `tracking.update` | server -> customer/admin | driver/order location | n/a | Room-scoped |
| WebSocket `chat.message_created` | server -> participants | message event | n/a | Use sequence handling for reconnect gaps |
