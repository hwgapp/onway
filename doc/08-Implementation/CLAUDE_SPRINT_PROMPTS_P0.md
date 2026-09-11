# ONWAY - Claude Sprint Prompts P0

**Loai tai lieu:** Ready-to-use coding prompts  
**Phien ban:** 0.1  
**Trang thai:** Draft  
**Ngay cap nhat:** 11/09/2026  
**Muc tieu:** Cung cap prompt ngan gon theo sprint/sub-sprint de dua vao Claude/dev agent khi bat dau code  

---

# 1. Cach dung

Moi lan chi giao mot sprint hoac sub-sprint. Khong giao "build all Onway".

Tat ca prompt duoi day deu giu cac guardrail P0:

- No COD.
- No cash payment.
- No payment gateway.
- No wallet/escrow/Onway-held Ride/Food money.
- No Food delivery fee negotiation.
- No full Trust Engine.
- No Merchant App.
- No driver-managed restaurant/menu.
- No production AI OCR/menu extraction.
- No Ads.

# 2. Base prompt bat buoc

Dung block nay o dau moi prompt neu can:

```txt
You are implementing Onway MVP in this repository.

Read these docs first:
1. doc/08-Implementation/CLAUDE_HANDOFF.md
2. doc/08-Implementation/ONWAY_IMPLEMENTATION_BACKLOG_P0_v0.1.md
3. doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md
4. Relevant PRD/API/Realtime/DB/UI docs for this sprint.

Non-negotiable P0 exclusions:
- Do not implement COD, cash, payment gateway, wallet, escrow or Onway-held Ride/Food payment.
- Do not implement Food delivery fee negotiation.
- Do not implement full Trust Engine, Merchant App, Mission, Community Truth, Ads, or production AI OCR/menu extraction.
- Do not let drivers manage restaurant/menu data in P0.

Before coding:
1. State the sprint/sub-sprint you are implementing.
2. List docs read.
3. List files/modules you expect to create/change.
4. Confirm excluded features remain excluded.

After coding:
1. Run available lint/typecheck/tests.
2. Summarize changed files.
3. Summarize what works, what is stubbed, and remaining gaps.
```

# 3. Sprint 0 prompt

```txt
Implement Sprint 0 only: repo scaffold and standards.

Read:
- doc/08-Implementation/CLAUDE_HANDOFF.md
- doc/08-Implementation/ONWAY_IMPLEMENTATION_BACKLOG_P0_v0.1.md
- doc/03-Architecture/ONWAY_ARCHITECTURE_DECISIONS_v0.2_VI.md
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md

Scope:
- Create or normalize Nx monorepo skeleton.
- Create placeholders for api, admin portal, landing web, customer app, driver app.
- Create shared libs for types, config, database, testing and admin UI.
- Add lint/typecheck/test/build scripts.
- Add local dev README.

Output:
- Repo builds with empty app shells.
- Commands are documented.
- No business feature implemented.
```

# 4. Sprint 1 prompt

```txt
Implement Sprint 1 only: backend core infrastructure.

Read:
- doc/04-Database/ONWAY_DB_SCHEMA_P0_v0.1.md
- doc/04-Database/ONWAY_DB_MIGRATION_STRATEGY_P0_v0.1.md
- doc/05-Logic/ONWAY_LOGIC_P0_v0.1.md sections 2-5, 8-9, 31-33
- doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md common types
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md Sprint 1 DoD

Scope:
- NestJS API app.
- Prisma setup.
- PostgreSQL/PostGIS local config.
- Base modules: config, database, auth guard skeleton, audit-log, media-evidence, policy-config, notification outbox shell.
- Initial migrations for extensions and core tables.

Acceptance:
- Fresh DB migrates.
- PostGIS extension exists.
- API starts and health/me placeholder works.
- Audit/media/policy shell tests pass.
```

# 5. Sprint 2 prompt

```txt
Implement Sprint 2 only: identity, auth, region and policy.

Read:
- doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md sections Identity/Auth and Region
- doc/06-API/ONWAY_GRAPHQL_SCHEMA_P0_v0.1.graphql
- doc/05-Logic/ONWAY_LOGIC_P0_v0.1.md sections 6-8
- doc/07-Realtime/ONWAY_REALTIME_EVENT_CONTRACT_P0_v0.1.md auth principles
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md Sprint 2 DoD

Scope:
- ViHAT OTP abstraction with mock provider for local/test.
- Verify OTP -> Firebase custom token.
- Firebase ID token verification guard.
- Account/customer/driver profile mapping.
- Secure admin seed/provisioning only, no public admin creation.
- Region/currency/service availability and PostGIS region containment.
- Minimal admin policy config CRUD/server lookup.

Acceptance:
- Public user cannot create admin.
- Region outside polygon returns unavailable.
- Currency is region-based.
- Policy values are server-loaded.
```

# 6. Sprint 3 prompt

```txt
Implement Sprint 3 only: driver foundation.

Read:
- doc/02-PRD/D-driver-foundation/19-driver-registration-onboarding.md
- doc/02-PRD/D-driver-foundation/20-driver-profile-vehicle-service-eligibility.md
- doc/02-PRD/D-driver-foundation/21-driver-platform-fee-subscription-refund.md
- doc/02-PRD/D-driver-foundation/22-driver-online-offline-location-presence.md
- doc/02-PRD/D-driver-foundation/23-driver-risk-lock-manual-admin-action.md
- doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md Driver and Platform Fee API
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md Sprint 3 DoD

Scope:
- Driver profile/onboarding state.
- Vehicle create/review.
- Service eligibility.
- Driver payment account create/review.
- Platform fee instruction/proof/admin approval.
- Driver activation logic.
- Go online/offline API without full matching yet.

Acceptance:
- Inactive/ineligible/locked driver cannot go online.
- Driver without active payment account cannot go online.
- Admin decisions write audit.
```

# 7. Sprint 4 prompt

```txt
Implement Sprint 4 only: Admin Portal foundation.

Read:
- doc/02-PRD/B-general-platform-codebase/06-web-admin-portal.md
- doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md Admin screens
- doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md Admin operations
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md Sprint 4 DoD

Scope:
- React Admin shell.
- Login/auth integration.
- RBAC-aware navigation.
- Sidebar, topbar, content, table/detail page shells.
- Placeholder pages for dashboard, regions, drivers, platform fees, food catalog, monitoring, complaints and audit logs.

Acceptance:
- Unauthorized admin routes blocked.
- Readonly/unauthorized admin actions hidden or disabled.
- Loading/empty/error states exist.
```

# 8. Sprint 5 prompts

## 8.1 Sprint 5A - Brand and outlet

```txt
Implement Sprint 5A only: Food brand and outlet admin management.

Read:
- doc/02-PRD/E-food-supply-admin-first/24-restaurant-brand-chain-management.md
- doc/02-PRD/E-food-supply-admin-first/25-outlet-store-management.md
- doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md Food catalog API
- doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md ADM-FOOD-001 and ADM-FOOD-002
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md Food catalog tests

Scope:
- Admin brand CRUD.
- Admin outlet CRUD.
- Opening hours/status basics.
- Region/PostGIS validation for outlet.

Acceptance:
- Outlet outside active Food region cannot be published.
- Customer APIs do not expose unpublished catalog.
```

## 8.2 Sprint 5B - Menu and modifiers

```txt
Implement Sprint 5B only: canonical menu/category/item/modifier management.

Read:
- doc/02-PRD/E-food-supply-admin-first/26-canonical-menu-catalog-management.md
- doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md Food catalog API
- doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md ADM-FOOD-003
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md Food catalog tests

Scope:
- Menu versioning.
- Category/item CRUD.
- Modifier group/option CRUD.
- Required modifier validation.

Acceptance:
- Empty menu cannot be published.
- Required modifier min/max validation works.
```

## 8.3 Sprint 5C - Overrides and publishing

```txt
Implement Sprint 5C only: outlet overrides, catalog publish and effective menu.

Read:
- doc/02-PRD/E-food-supply-admin-first/27-catalog-publishing.md
- doc/02-PRD/E-food-supply-admin-first/28-outlet-override-availability.md
- doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md Food catalog API
- doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md ADM-FOOD-004
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md Food catalog tests

Scope:
- Outlet item override.
- Outlet modifier option override.
- Catalog review/publish/unpublish.
- Customer effective menu query.

Acceptance:
- Customer sees only published/effective catalog.
- Outlet item and modifier option overrides apply.
```

# 9. Sprint 6 prompt

```txt
Implement Sprint 6 only: realtime and matching foundation.

Read:
- doc/07-Realtime/ONWAY_REALTIME_EVENT_CONTRACT_P0_v0.1.md
- doc/07-Realtime/ONWAY_REALTIME_EVENT_CATALOG_P0_v0.1.json
- doc/05-Logic/ONWAY_LOGIC_P0_v0.1.md matching sections
- doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md Matching API
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md Sprint 6 DoD

Scope:
- WebSocket gateway auth/rooms.
- Driver presence in Redis.
- Driver location ack.
- Matching sessions/offers.
- Progressive batch/wave dispatch.
- Driver offer accept/reject through GraphQL.
- Atomic assignment.

Acceptance:
- Locked/ineligible/offline driver excluded.
- Expired offer cannot be accepted.
- Simultaneous accepts produce one assignment.
- Reconnect gap requires GraphQL resync.
```

# 10. Sprint 7 prompt

```txt
Implement Sprint 7 only: Customer and Driver app shells.

Read:
- doc/02-PRD/B-general-platform-codebase/04-customer-app.md
- doc/02-PRD/B-general-platform-codebase/05-driver-app.md
- doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md Customer and Driver screen inventory
- doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md
- doc/07-Realtime/ONWAY_REALTIME_EVENT_CONTRACT_P0_v0.1.md
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md Sprint 7 DoD

Scope:
- Flutter customer app shell.
- Flutter driver app shell.
- Shared auth/networking/models.
- OTP login.
- Customer home/profile.
- Driver home/onboarding/profile.
- Basic map/location permission.
- Realtime connection manager.

Acceptance:
- Customer and Driver can login and call me.
- Driver location permission denial blocks online.
- Region service availability displays.
```

# 11. Sprint 8 prompts

## 11.1 Sprint 8A - Ride request and quote

```txt
Implement Sprint 8A only: Ride quote/request.

Read:
- doc/02-PRD/F-ride-mvp/30-ride-request-price-recommendation.md
- doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md Ride API
- doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md CUS-RIDE-001
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md Ride tests

Scope:
- Customer ride quote.
- Customer ride confirm.
- Region/vehicle validation.
- Recommended price only; no default Ride negotiation in P0.

Acceptance:
- Customer cannot request ride outside enabled region/service.
- Created ride enters matching flow.
```

## 11.2 Sprint 8B - Ride matching and active trip

```txt
Implement Sprint 8B only: Ride matching, assignment and active trip state changes.

Read:
- doc/02-PRD/F-ride-mvp/31-ride-matching-driver-accept-reject.md
- doc/02-PRD/F-ride-mvp/32-ride-tracking-in-trip-flow.md
- doc/07-Realtime/ONWAY_REALTIME_EVENT_CONTRACT_P0_v0.1.md Ride/matching events
- doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md CUS-RIDE-002, CUS-RIDE-003, DRV-RIDE-001

Scope:
- Ride offer to driver.
- Assignment.
- Chat room creation.
- Driver en-route, arrived, start, complete states.
- Customer/driver active ride screens.
- Admin ride monitoring P0-lite.

Acceptance:
- Timeline matches Ride state machine.
- Buttons follow allowedActions.
```

## 11.3 Sprint 8C - Ride payment, cancel and rating

```txt
Implement Sprint 8C only: Ride payment proof if policy requires, cancellation/no-show basics and rating.

Read:
- doc/02-PRD/F-ride-mvp/33-ride-completion-direct-bank-transfer-confirmation.md
- doc/02-PRD/F-ride-mvp/34-ride-rating.md
- doc/02-PRD/F-ride-mvp/35-ride-cancellation-timeout-no-show.md
- doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md Direct payment and Rating API
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md Ride E2E

Scope:
- Direct bank transfer/QR proof.
- Driver payment confirmation/dispute.
- Ride rating after completed.
- Basic cancellation/no-show.

Acceptance:
- No COD/cash/gateway UI or API path.
- Rating only after completion.
```

# 12. Sprint 9 prompts

## 12.1 Sprint 9A - Food discovery, cart and order

```txt
Implement Sprint 9A only: Food discovery, cart, quote and order creation.

Read:
- doc/02-PRD/G-food-mvp/37-food-discovery-cart.md
- doc/02-PRD/G-food-mvp/38-food-order-placement-delivery-fee-recommendation.md
- doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md Food order API
- doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md CUS-FOOD-001, CUS-FOOD-002, CUS-FOOD-003
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md Food E2E

Scope:
- Customer Food discovery from published catalog.
- Cart item/modifier validation.
- Food quote with system delivery fee.
- Food order confirm.

Acceptance:
- Customer cannot edit/negotiation delivery fee.
- Unavailable item/option cannot be ordered.
```

## 12.2 Sprint 9B - Food matching and prepaid proof

```txt
Implement Sprint 9B only: Food matching and prepaid bank transfer/QR proof.

Read:
- doc/02-PRD/G-food-mvp/39-food-driver-matching-accept-reject.md
- doc/02-PRD/G-food-mvp/40-food-direct-qr-bank-transfer-confirmation.md
- doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md Matching and Direct payment API
- doc/07-Realtime/ONWAY_REALTIME_EVENT_CONTRACT_P0_v0.1.md Food/payment events
- doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md CUS-FOOD-004, DRV-MATCH-001

Scope:
- Food offer accept/reject.
- Food assignment.
- Direct payment record and QR instructions.
- Customer proof upload.
- Driver payment confirmation/not received report.

Acceptance:
- Food offer has no fee negotiation.
- Driver cannot proceed to restaurant purchase before payment gate.
```

## 12.3 Sprint 9C - Food purchase, change and delivery

```txt
Implement Sprint 9C only: Food restaurant purchase, item/price change, delivery and completion.

Read:
- doc/02-PRD/G-food-mvp/41-driver-restaurant-purchase-flow.md
- doc/02-PRD/G-food-mvp/42-food-item-price-change-confirmation.md
- doc/02-PRD/G-food-mvp/43-food-waiting-policy.md
- doc/02-PRD/G-food-mvp/44-food-delivery-completion-rating.md
- doc/02-PRD/G-food-mvp/45-food-cancellation-financial-responsibility.md
- doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md active Food screens

Scope:
- Driver outlet arrival/order placed/paid/waiting/ready/delivery/completion states.
- Food change request and customer decision.
- Rating after completed.
- Cancellation responsibility based on restaurantOrderPlacedAt.

Acceptance:
- Change request does not auto-update catalog.
- Food reaches completed in happy path.
```

# 13. Sprint 10 prompt

```txt
Implement Sprint 10 only: chat, media and evidence polish.

Read:
- doc/02-PRD/C-foundation-cross-platform/13-evidence-media-audit-trail.md
- doc/02-PRD/C-foundation-cross-platform/15-direct-bank-transfer-payment-confirmation.md
- doc/02-PRD/C-foundation-cross-platform/16-communication-chat-contact-policy.md
- doc/02-PRD/C-foundation-cross-platform/17-privacy-consent-data-retention.md
- doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md Chat/payment/evidence screens
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md Sprint 10 DoD

Scope:
- Media signed upload URLs.
- Payment proof upload UX/API integration.
- Chat text/image.
- Chat room authorization.
- Chat close/retention marker.
- Admin evidence viewer.
- Retention job skeleton.

Acceptance:
- Non-participant cannot read chat.
- Chat retention policy is represented as 1 week.
- Complaint can preserve/link evidence.
```

# 14. Sprint 11 prompt

```txt
Implement Sprint 11 only: complaint, risk and fraud shell.

Read:
- doc/02-PRD/H-risk-complaint-growth/46-complaint-dispute-journey.md
- doc/02-PRD/H-risk-complaint-growth/47-paid-but-driver-no-show-dispute.md
- doc/02-PRD/H-risk-complaint-growth/48-fraud-case-journey.md
- doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md Complaint/risk/fraud API
- doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md complaint and locked-account screens
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md Sprint 11 DoD

Scope:
- Complaint intake in Customer/Driver apps.
- Paid-but-driver-no-show complaint.
- Evidence linkage.
- Admin complaint queue/detail.
- Driver response.
- Auto-lock after 2 qualifying open complaints.
- Manual lock/unlock.
- Fraud case shell/escalation.

Acceptance:
- Paid/no-show requires payment proof.
- First qualifying complaint does not auto-lock.
- Second qualifying complaint auto-locks driver.
- Locked driver cannot go online or receive jobs.
```

# 15. Sprint 12 prompt

```txt
Implement Sprint 12 only: hardening and launch QA.

Read all P0 docs and especially:
- doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md
- doc/08-Implementation/ONWAY_IMPLEMENTATION_BACKLOG_P0_v0.1.md Sprint 12

Scope:
- E2E test suite.
- Seed data.
- Observability/logging.
- Error handling consistency.
- Basic load tests for matching/realtime.
- Deployment scripts/runbook.
- Security/privacy review checklist.

Acceptance:
- Fresh DB migration + seed works.
- Ride happy path E2E passes.
- Food happy path E2E passes.
- Paid/no-show auto-lock E2E passes.
- Admin can operate core flows.
```

