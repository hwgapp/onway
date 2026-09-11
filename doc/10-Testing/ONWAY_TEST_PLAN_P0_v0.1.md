# ONWAY - Test Plan P0

**Loai tai lieu:** QA / Engineering Definition of Done  
**Phien ban:** 0.1  
**Trang thai:** Draft  
**Ngay cap nhat:** 11/09/2026  
**Muc tieu:** Dinh nghia test strategy, E2E critical paths va quality gate de Claude/dev code theo sprint co the verify duoc truoc khi merge  

---

# 1. Source priority

QA/dev doc theo thu tu:

1. `doc/08-Implementation/CLAUDE_HANDOFF.md`
2. `doc/08-Implementation/ONWAY_IMPLEMENTATION_BACKLOG_P0_v0.1.md`
3. `doc/02-PRD/ONWAY_PRD_MASTER_v0.1_VI.md`
4. `doc/05-Logic/ONWAY_LOGIC_P0_v0.1.md`
5. `doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md`
6. `doc/06-API/ONWAY_GRAPHQL_SCHEMA_P0_v0.1.graphql`
7. `doc/07-Realtime/ONWAY_REALTIME_EVENT_CONTRACT_P0_v0.1.md`
8. `doc/07-Realtime/ONWAY_REALTIME_EVENT_CATALOG_P0_v0.1.json`
9. `doc/04-Database/ONWAY_DB_SCHEMA_P0_v0.1.md`
10. Relevant PRD file under `doc/02-PRD/*/*.md`
11. `doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md`

# 2. Non-negotiable P0 regression rules

These must be tested continuously:

- No COD appears in API, UI, seed data, fixtures, or tests as an enabled P0 payment option.
- No cash payment appears as an enabled P0 payment option.
- No payment gateway, wallet, escrow, or Onway-held Ride/Food money flow is implemented.
- Food delivery fee negotiation does not exist in P0 UI/API.
- Payment proof is required for direct bank transfer/QR flows.
- Food purchase flow is blocked until the required payment proof/driver confirmation state is satisfied.
- Driver auto-lock triggers after 2 qualifying open paid/no-show complaints.
- Locked driver is excluded from matching and cannot go online.
- Chat supports text and image between assigned customer/driver.
- Chat retention marker/job supports 1 week retention.
- Food catalog is admin-first; driver cannot edit restaurant/menu in P0.
- Full Trust Engine, Mission Engine, Community Truth, Ads and Merchant App are not P0 blockers.

# 3. Test pyramid

| Layer | Purpose | Owner | Required before merge |
|---|---|---|---|
| Unit | Pure functions, policies, guards, state machines | Backend/frontend module owner | Yes for changed logic |
| Integration | DB repository, Prisma/raw SQL, GraphQL resolver/service, WebSocket gateway | Backend owner | Yes for backend sprint |
| Contract | GraphQL schema compatibility, realtime event envelope/catalog | Backend + app owners | Yes when contract changes |
| E2E API | Auth -> command -> DB state -> event outbox | Backend owner | Yes for vertical slices |
| E2E UI | Admin/customer/driver critical paths | App owner | Required by sprint 8+ |
| Manual exploratory | Maps, location permission, upload proof, live chat, mobile background behavior | QA/founder/dev | Required before launch candidate |

# 4. Suggested tool choices

Actual tools depend on repo setup, but recommended defaults:

| Area | Suggested tool |
|---|---|
| Backend unit/integration | Jest/Vitest, TestingModule for NestJS |
| DB integration | Testcontainers or Docker Compose Postgres/PostGIS |
| GraphQL contract | Generated `schema.gql` diff against intended SDL |
| Realtime | WebSocket integration tests with fake Firebase token verifier |
| Admin UI | Playwright component/E2E, React Testing Library |
| Flutter unit/widget | `flutter test` |
| Flutter integration | `integration_test`, fake backend, later real dev env |
| Static checks | ESLint, TypeScript, Dart analyzer, Prettier/dart format |

# 5. Required test data seeds

Seed scenarios:

1. Active region Ho Chi Minh with VND currency and Ride/Food enabled.
2. Paused region or out-of-polygon location.
3. Customer account active.
4. Driver pending review.
5. Driver active with motorcycle and active payment account.
6. Driver active but platform fee pending.
7. Driver locked by admin.
8. Driver auto-locked by complaint threshold.
9. Restaurant brand with one active outlet.
10. Published Food menu with categories, items, required modifier and optional modifier.
11. Outlet override price/availability.
12. Ride ready for matching.
13. Food order ready for matching.
14. Direct payment record awaiting customer transfer.
15. Chat room with text and image messages.
16. Complaint with payment proof evidence.

# 6. Backend unit test matrix

## 6.1 Policy and allowed actions

| Case | Expected |
|---|---|
| Customer outside active region tries Ride quote | `REGION_UNAVAILABLE` |
| Food region disabled | Food order create blocked |
| Driver activation incomplete | Online action disabled |
| Driver has no active payment account | Online action disabled |
| Driver risk locked | Online and offer accept disabled |
| Food order awaits payment proof | Driver purchase action disabled |
| Payment confirmed by driver | Next Food purchase action enabled |

## 6.2 State machines

Ride state tests:

- `MATCHING -> ASSIGNED`
- `ASSIGNED -> DRIVER_EN_ROUTE_TO_PICKUP`
- `DRIVER_EN_ROUTE_TO_PICKUP -> DRIVER_ARRIVED`
- `DRIVER_ARRIVED -> READY_TO_START`
- `READY_TO_START -> IN_PROGRESS`
- `IN_PROGRESS -> COMPLETED`
- Invalid backwards transition rejected.
- Unauthorized actor transition rejected.

Food state tests:

- `CUSTOMER_CONFIRMED -> MATCHING`
- `MATCHING -> ASSIGNED`
- `ASSIGNED -> AWAITING_CUSTOMER_TRANSFER`
- `AWAITING_CUSTOMER_TRANSFER -> PAYMENT_PROOF_SUBMITTED`
- `PAYMENT_PROOF_SUBMITTED -> DRIVER_CONFIRMED_PAYMENT`
- `DRIVER_CONFIRMED_PAYMENT -> DRIVER_EN_ROUTE_TO_OUTLET`
- `DRIVER_ARRIVED_AT_OUTLET -> ORDERING_WITH_RESTAURANT`
- `ORDERING_WITH_RESTAURANT -> RESTAURANT_ORDER_PLACED`
- `RESTAURANT_ORDER_PLACED -> WAITING_FOR_FOOD`
- `WAITING_FOR_FOOD -> READY_FOR_DELIVERY`
- `READY_FOR_DELIVERY -> DRIVER_EN_ROUTE_TO_CUSTOMER`
- `DRIVER_EN_ROUTE_TO_CUSTOMER -> DRIVER_ARRIVED_AT_CUSTOMER`
- `DRIVER_ARRIVED_AT_CUSTOMER -> DELIVERED`
- `DELIVERED -> COMPLETED`
- Driver cannot skip payment confirmation when policy requires it.

## 6.3 Matching

- Candidate excludes offline driver.
- Candidate excludes locked driver.
- Candidate excludes driver without service eligibility.
- Candidate excludes driver with active offer/job.
- First valid accept wins under concurrent accept.
- Expired offer returns `OFFER_EXPIRED`.
- Offer rejected by all candidates advances next wave.
- No candidates ends session with no-driver status.

## 6.4 Direct payment

- Payment record created with method `BANK_TRANSFER_QR`.
- Customer proof requires media purpose `PAYMENT_PROOF`.
- Customer cannot submit proof for unrelated ride/order.
- Driver cannot confirm payment for unrelated ride/order.
- Driver report not received sets admin review/dispute state.
- Proof remains auditable if replaced by policy.

## 6.5 Complaints and lock

- Paid/no-show complaint without payment proof rejected.
- First qualifying open paid/no-show complaint does not auto-lock.
- Second qualifying open paid/no-show complaint auto-locks driver.
- Auto-lock creates audit log/risk action.
- Admin manual lock prevents online/matching.
- Admin unlock restores eligibility only if other conditions pass.

## 6.6 Food catalog

- Admin cannot publish outlet outside active Food region.
- Admin cannot publish empty menu.
- Effective customer menu only shows published catalog.
- Outlet item price override applies.
- Outlet modifier option override applies.
- Unavailable item/option cannot be added to cart.
- Required modifier min/max validation works.

# 7. GraphQL contract tests

Every backend PR that changes GraphQL types must:

1. Generate `schema.gql` from NestJS code.
2. Compare against `doc/06-API/ONWAY_GRAPHQL_SCHEMA_P0_v0.1.graphql`.
3. If intentionally different, update both:
   - API markdown contract.
   - SDL contract.
4. Run smoke introspection query.

Minimum contract smoke queries:

```graphql
query ContractSmoke {
  __schema {
    queryType { name }
    mutationType { name }
  }
}
```

```graphql
query MeSmoke {
  me {
    id
    roles
    allowedActions { code enabled disabledReason }
  }
}
```

# 8. Realtime contract tests

Minimum gateway tests:

- `connection.init` with invalid token returns `connection.error`.
- Valid customer can subscribe to own `customer:{id}` room.
- Customer cannot subscribe to unrelated `ride:{id}` room.
- Driver can receive `matching.offer_sent`.
- Offer expiry emits `matching.offer_expired`.
- `driver.location_update` from offline driver rejected.
- Valid active job location update emits `presence.driver_location_changed`.
- Chat text/image mutation emits `chat.message_created`.
- Stale `connection.resume` returns `room.resync_required`.
- Duplicate event id/client id does not create duplicate UI-visible record.

# 9. E2E critical paths

## 9.1 E2E-RIDE-001 Ride happy path

Input:

- Active customer.
- Active driver.
- Active region with Ride motorcycle enabled.
- Driver online in pickup radius.

Steps:

1. Customer requests Ride quote.
2. Customer confirms Ride.
3. Matching creates offer to driver.
4. Driver accepts offer.
5. Ride assigned, chat room created.
6. Driver marks arrived.
7. Ride starts.
8. Ride completes.
9. Customer rates driver.

Expected:

- Ride reaches `COMPLETED`.
- Matching session reaches `ASSIGNED`.
- Driver active offer cleared.
- Audit/timeline events exist.
- No COD/cash/gateway state appears.

## 9.2 E2E-FOOD-001 Food happy path with prepaid QR

Input:

- Active customer.
- Active driver with payment account/QR.
- Published Food outlet/menu in active region.

Steps:

1. Customer opens Food discovery.
2. Customer adds item/modifier to cart.
3. Customer confirms Food order.
4. Matching offers job to driver.
5. Driver accepts offer.
6. System creates direct payment record.
7. Customer views bank transfer/QR instructions.
8. Customer uploads payment proof.
9. Driver confirms payment received.
10. Driver goes to outlet.
11. Driver marks restaurant order placed.
12. Driver marks food ready/picked up.
13. Driver delivers.
14. Customer rates.

Expected:

- Food reaches `COMPLETED`.
- Delivery fee is system-provided and not customer-negotiated.
- Driver cannot mark restaurant purchase before payment proof/confirmation gate.
- Payment proof remains visible to authorized admin.

## 9.3 E2E-FOOD-002 Food item/price change

Steps:

1. Food order assigned and payment flow satisfied.
2. Driver reports item unavailable or price changed.
3. Customer receives change request.
4. Customer accepts.
5. Food order continues.

Expected:

- Change request recorded.
- Customer decision recorded.
- Food order total/timeline updates.
- Catalog does not auto-update.

## 9.4 E2E-DISPUTE-001 Paid but driver no-show

Steps:

1. Customer completes transfer proof on Ride/Food.
2. Driver does not proceed or customer files paid/no-show complaint.
3. Complaint is created with linked proof.
4. Admin opens complaint queue/detail.
5. System counts qualifying open complaints.

Expected:

- Complaint category is `PAID_BUT_DRIVER_NO_SHOW`.
- Complaint requires payment proof.
- Admin can review evidence/timeline/chat.
- First qualifying complaint does not auto-lock.

## 9.5 E2E-DISPUTE-002 Auto-lock after second qualifying complaint

Steps:

1. Driver has one qualifying open paid/no-show complaint.
2. New qualifying paid/no-show complaint is submitted with proof.
3. System runs auto-lock rule.
4. Driver tries to go online or accept offer.

Expected:

- Driver risk status becomes `TEMPORARILY_LOCKED`.
- `driver.auto_locked` and `driver.status_changed` events emitted.
- Driver cannot go online.
- Driver is excluded from matching.
- Admin can manually unlock with reason.

## 9.6 E2E-CHAT-001 Text/image chat

Steps:

1. Ride/Food is assigned.
2. Customer sends text message.
3. Driver receives realtime event.
4. Driver uploads image and sends image message.
5. Customer receives realtime event.
6. Non-participant attempts to read room.

Expected:

- Messages stored and returned by GraphQL history.
- Image stored as media object.
- Non-participant blocked.
- Chat room has `retentionDeleteAfter` approximately 1 week after close.

## 9.7 E2E-ADMIN-FOOD-001 Admin-first catalog

Steps:

1. Admin creates brand.
2. Admin creates outlet in active Food region.
3. Admin creates menu/category/item/modifier/option.
4. Admin sets outlet override.
5. Admin publishes catalog.
6. Customer opens Food discovery/menu.

Expected:

- Customer sees only published/effective catalog.
- Override price/availability applies.
- Driver has no menu edit API/UI path in P0.

# 10. UI QA minimum gates

Admin:

- Login blocked for non-admin.
- Sidebar/topbar/navigation work.
- Tables support loading/empty/error state.
- Detail pages show status, timeline, evidence and allowed actions.
- Critical admin actions require reason/note where defined.

Customer App:

- OTP login works.
- Region unavailable state works.
- Ride request/matching/active/completed screens render.
- Food discovery/cart/checkout/payment/active/completed screens render.
- Payment proof upload handles success/failure/retry.
- Chat text/image handles sending/uploading/error.

Driver App:

- OTP login works.
- Onboarding pending states render.
- Online toggle blocked with reasons when ineligible.
- Offer card countdown renders for Ride/Food.
- Food offer has no fee negotiation UI.
- Active job action buttons follow `allowedActions`.
- Locked account state blocks work actions.

# 11. Sprint Definition of Done

## Sprint 0

- Repo scaffold builds.
- Lint/test/build scripts exist.
- No business feature sneaks in.

## Sprint 1

- API starts locally.
- DB migrates locally.
- PostGIS extension enabled.
- Health/me placeholder works.
- Audit/media/policy shell tests pass.

## Sprint 2

- OTP/Firebase custom token flow works with mock provider.
- Account/profile mapping tests pass.
- Region/currency/service availability tests pass.
- Public cannot create admin.

## Sprint 3

- Driver onboarding/vehicle/payment account/platform fee tests pass.
- Driver cannot go online until eligible.
- Admin decisions audit logged.

## Sprint 4

- Admin login and route guard work.
- Admin shell/pages created.
- RBAC hides or disables unauthorized actions.
- UI states exist for core queues.

## Sprint 5

- Admin Food catalog CRUD works.
- Publish validation works.
- Effective customer menu query works.
- No driver menu management path.

## Sprint 6

- WebSocket auth/subscribe works.
- Driver presence/location works.
- Matching waves/offers/atomic accept work.
- Locked/ineligible/offline drivers excluded.

## Sprint 7

- Customer/Driver app shells run.
- Auth/me flow works.
- Region/service availability shown.
- Driver location permission denial blocks online.

## Sprint 8

- Ride happy path E2E passes.
- Ride payment proof path works if policy requires payment step.
- Ride admin monitoring works.
- Rating after completion only.

## Sprint 9

- Food happy path E2E passes.
- Payment proof/driver confirmation gate blocks purchase correctly.
- Food item/price change flow works.
- No Food delivery fee negotiation UI/API.

## Sprint 10

- Chat text/image E2E passes.
- Media signed upload/view path works.
- Evidence viewer works for admin.
- Chat retention marker/job exists.

## Sprint 11

- Complaint intake and admin review work.
- Paid/no-show proof requirement works.
- Second qualifying complaint auto-locks driver.
- Manual lock/unlock works.

## Sprint 12

- Fresh migration + seed works.
- Critical E2E suite passes.
- Observability/logging basic ready.
- Deployment runbook exists.
- Launch QA checklist signed off.

# 12. PR review checklist for Claude/dev

Before final handoff for each sprint:

- State sprint/sub-sprint implemented.
- List docs read.
- List files changed.
- Confirm excluded P0 features remain excluded.
- Include commands run and result.
- Include screenshots for UI changes when possible.
- Include generated schema/event contract diff if changed.
- Note stubs and follow-up tasks.

