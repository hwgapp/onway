# ONWAY - Implementation Backlog P0

**Loai tai lieu:** Sprint Backlog / Agent Coding Plan  
**Phien ban:** 0.1  
**Trang thai:** Draft  
**Ngay cap nhat:** 11/09/2026  
**Muc tieu:** Chia viec de code Onway MVP theo sprint co input/output/test gate ro rang  

---

# 1. Source priority

Claude/dev must read in this order:

1. `doc/08-Implementation/CLAUDE_HANDOFF.md`
2. `doc/02-PRD/ONWAY_PRD_MASTER_v0.1_VI.md`
3. `doc/05-Logic/ONWAY_LOGIC_P0_v0.1.md`
4. `doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md`
5. `doc/07-Realtime/ONWAY_REALTIME_EVENT_CONTRACT_P0_v0.1.md`
6. `doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md`
7. `doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md`
8. `doc/04-Database/ONWAY_DB_SCHEMA_P0_v0.1.md`
9. `doc/04-Database/ONWAY_DB_MIGRATION_STRATEGY_P0_v0.1.md`
10. Relevant PRD file under `doc/02-PRD/*/*.md`
11. `doc/01-BRD/ONWAY_BRD_v0.5_VI.md`
12. `doc/03-Architecture/ONWAY_ARCHITECTURE_DECISIONS_v0.2_VI.md`

# 2. P0 product guardrails

Never implement in P0 unless explicitly asked later:

- COD.
- Cash payment.
- Payment gateway.
- Wallet/escrow/Onway-held Ride/Food money.
- Food delivery fee negotiation.
- Full Trust Engine.
- Merchant App.
- Driver-managed restaurant/menu data.
- Production AI OCR/menu extraction.
- Advertising.

Must implement/prepare in P0:

- Direct bank transfer/QR payment proof.
- Customer-driver chat with image.
- Chat retention policy 1 week.
- Admin-first Food catalog.
- Driver auto-lock after 2 qualifying open paid/no-show complaints.
- Admin manual lock/unlock.

# 3. Sprint overview

| Sprint | Theme | Main output |
|---:|---|---|
| 0 | Repo scaffold and standards | Nx monorepo skeleton, app placeholders, lint/test/build foundation. |
| 1 | Backend core infrastructure | NestJS API, Prisma, config, auth skeleton, audit/media foundations. |
| 2 | Identity, region, policy | ViHAT OTP -> Firebase custom token, account/profile mapping, region/currency/service availability. |
| 3 | Driver foundation | Onboarding, vehicle/service eligibility, payment account, platform fee verification. |
| 4 | Admin portal foundation | React Admin shell, RBAC, layout, core queues/pages. |
| 5 | Food supply admin-first | Brand/outlet/menu/modifiers/overrides/publishing/effective menu. |
| 6 | Realtime and matching foundation | WebSocket gateway, driver presence, matching sessions/offers, atomic accept. |
| 7 | Customer/Driver app shells | Flutter app shells, auth, navigation, shared API client, basic maps/location. |
| 8 | Ride MVP vertical | Ride quote/request/matching/tracking/payment proof/completion/rating/cancel. |
| 9 | Food MVP vertical | Discovery/cart/order/matching/prepay proof/purchase/change/delivery/rating/cancel. |
| 10 | Chat/media/evidence polish | Text/image chat, media signed URLs, retention job, evidence viewers. |
| 11 | Complaint/risk/fraud shell | Complaint, paid-no-show, auto-lock, admin review, fraud shell. |
| 12 | Hardening and launch QA | E2E tests, seed data, observability, deployment scripts, bug fixing. |

# 4. Sprint 0 - Repo scaffold and standards

## Input docs

- Architecture ADR-001, ADR-020, ADR-021, ADR-022, ADR-041.
- PRD General System Architecture & Codebase.

## Scope

- Create Nx monorepo if not present.
- Create app placeholders:
  - `apps/api`
  - `apps/admin-portal`
  - `apps/landing-web`
  - `apps/customer-app`
  - `apps/driver-app`
- Create shared libs:
  - `libs/types`
  - `libs/config`
  - `libs/database`
  - `libs/testing`
  - `libs/ui-admin`
- Establish lint/typecheck/test/build scripts.

## Output

- Repo builds with empty app shells.
- Standard README for local dev.
- Basic CI script or local commands documented.

## Acceptance

- `npm install` or chosen package install works.
- `npm run lint`, `npm run test`, `npm run build` or Nx equivalents exist.
- No business feature implemented yet.

# 5. Sprint 1 - Backend core infrastructure

## Input docs

- DB schema.
- DB migration strategy.
- Logic sections 2-5, 8-9, 31-33.
- API common types.

## Scope

- NestJS API app.
- Prisma setup.
- PostgreSQL/PostGIS local config.
- Base modules:
  - config
  - database
  - auth guard skeleton
  - audit-log
  - media-evidence
  - policy-config
  - notification outbox shell
- Create initial migrations for extensions and core tables.

## Output

- API starts.
- Prisma client generated.
- DB migrates locally.
- Health check endpoint.
- Audit/media/policy services have unit tests.

## Acceptance

- Fresh DB migrates successfully.
- PostGIS extension exists.
- App can connect to DB.
- Basic GraphQL server returns health/me placeholder.

# 6. Sprint 2 - Identity, auth, region, policy

## Input docs

- API Identity/Auth.
- API Region.
- Logic sections 6-8.
- Realtime auth principles.

## Scope

- OTP challenge via ViHAT abstraction.
- Verify OTP -> Firebase custom token.
- Verify Firebase ID token in GraphQL.
- Account/profile mapping.
- Admin profile seed.
- Region/currency/service availability.
- Admin policy config CRUD minimal.
- PostGIS region containment.

## Output

- Customer/driver can authenticate.
- Admin seed can log in.
- Region resolution API works.
- Policy config lookup works.

## Acceptance

- Public user cannot create admin.
- Region outside polygon returns unavailable.
- Currency is region-based.
- Policy values are loaded server-side.

# 7. Sprint 3 - Driver foundation

## Input docs

- PRD 19-23.
- DB driver tables.
- Logic sections 10-13.
- API Driver and Platform Fee.

## Scope

- Driver profile/onboarding state.
- Vehicle create/review.
- Service eligibility.
- Driver payment account create/review.
- Platform fee instruction/proof/admin approval.
- Driver activation logic.
- Go online/offline API without full matching yet.

## Output

- Driver can register and submit basic onboarding.
- Admin can approve driver/vehicle/payment account/platform fee.
- Driver activation status changes correctly.
- Driver cannot go online until eligible.

## Acceptance

- Inactive driver blocked from online.
- Driver without active payment account blocked.
- Platform fee approval can activate only when all conditions pass.
- Admin decisions write audit.

# 8. Sprint 4 - Admin portal foundation

## Input docs

- PRD General Web Admin Portal.
- API Admin operations.
- UI screen spec.

## Scope

- React Admin app shell.
- Login/auth integration.
- RBAC-aware navigation.
- Layout: sidebar, topbar, content, tables, detail pages.
- Core pages placeholders:
  - Dashboard
  - Regions
  - Drivers
  - Platform Fees
  - Food Catalog
  - Ride/Food Monitoring
  - Complaints
  - Audit Logs

## Output

- Admin can log in.
- Admin navigation works.
- Placeholder pages call real/placeholder GraphQL queries.

## Acceptance

- Unauthorized admin route blocked.
- Readonly admin cannot see mutation buttons.
- Layout responsive enough for desktop operations.

# 9. Sprint 5 - Food supply admin-first

## Input docs

- PRD 24-28.
- DB food catalog.
- API Food catalog.
- Logic section 14 and 19.

## Scope

- Brand CRUD.
- Outlet CRUD with PostGIS region validation.
- Opening hours.
- Menu/category/item/modifier/modifier option CRUD.
- Outlet overrides.
- Catalog publishing.
- Customer effective menu query.

## Output

- Admin can create a brand/outlet/menu and publish.
- Customer API can list Food discovery and menu.

## Acceptance

- Cannot publish outlet outside active Food region.
- Cannot publish menu without active item.
- Customer only sees published/effective catalog.
- Outlet override price/availability applies.

# 10. Sprint 6 - Realtime and matching foundation

## Input docs

- Realtime contract.
- Logic sections 13 and 16.
- DB matching tables.
- API Matching.

## Scope

- WebSocket gateway auth.
- Rooms/subscription.
- Driver presence in Redis.
- Driver location update ack.
- Matching sessions/offers.
- Progressive batch matching.
- Driver offer accept/reject through GraphQL.
- Atomic assignment.

## Output

- Online driver can receive matching offer.
- Driver accept assigns Ride/Food entity.
- Realtime assignment events are emitted.

## Acceptance

- Locked/ineligible/offline driver excluded.
- Expired offer cannot be accepted.
- Two simultaneous accepts produce one assignment.
- Reconnect requires GraphQL resync if sequence gap.

# 11. Sprint 7 - Customer/Driver app shells

## Input docs

- PRD General Customer App.
- PRD General Driver App.
- API contract.
- Realtime contract.

## Scope

- Flutter workspace/apps.
- Shared networking/auth models.
- Login flow using OTP/custom token.
- Customer home/navigation/profile.
- Driver home/onboarding/navigation/profile.
- Basic map/location permission integration.
- Realtime connection manager.

## Output

- Customer/Driver apps can login and call `me`.
- Driver can attempt online and see blocked reasons.
- Customer sees region service availability.

## Acceptance

- Token refresh works.
- App handles loading/error/empty states for auth.
- Driver location permission denial blocks online.

# 12. Sprint 8 - Ride MVP vertical

## Input docs

- PRD 30-35.
- API Ride/Matching/Payment/Rating.
- Realtime Ride events.
- Logic sections 15-18, 25, 30.

## Scope

- Customer Ride quote/request.
- Driver Ride offer.
- Assignment and chat room creation.
- Ride states: en route, arrived, start, complete.
- Direct bank transfer proof at policy-defined step.
- Driver payment confirmation/dispute.
- Ride rating.
- Ride cancellation/no-show basic.
- Admin ride monitoring.

## Output

- End-to-end Ride happy path works.
- Ride payment proof is stored.
- Admin can inspect ride timeline.

## Acceptance

- No COD/cash UI.
- Payment proof required where policy says.
- Driver cannot start/complete against invalid state.
- Rating only after completed.

# 13. Sprint 9 - Food MVP vertical

## Input docs

- PRD 37-45.
- API Food/Payment/Food Change.
- Realtime Food events.
- Logic sections 19-24, 25.

## Scope

- Customer Food discovery/cart/quote/order.
- No delivery fee negotiation.
- Food matching and assignment.
- Customer QR/bank transfer proof required.
- Driver confirms payment.
- Driver restaurant purchase flow.
- Food item/price change request.
- Delivery and completion.
- Rating and cancellation policy.
- Admin food monitoring.

## Output

- End-to-end Food happy path works from published catalog.
- Payment proof blocks/permits restaurant purchase correctly.
- Item/price change customer confirmation works.

## Acceptance

- Driver cannot go to restaurant/order before required payment state.
- Customer cannot submit custom delivery fee.
- Restaurant order placed timestamp changes cancellation responsibility.
- Customer sees no COD/cash.

# 14. Sprint 10 - Chat/media/evidence polish

## Input docs

- PRD 13, 15, 16, 17.
- API Chat/Media/Payment.
- Realtime Chat events.

## Scope

- Media upload signed URLs.
- Payment proof upload UX/API integration.
- Chat text/image.
- Chat room authorization.
- Chat close/retention marker.
- Admin evidence viewer.
- Retention job skeleton.

## Output

- Customer-driver chat supports text/image.
- Admin can see evidence for authorized cases.
- Chat content retention policy represented in data/job.

## Acceptance

- Non-participant cannot read chat.
- Chat older than retention is processed by job.
- Complaint can preserve/link evidence before deletion.

# 15. Sprint 11 - Complaint/risk/fraud shell

## Input docs

- PRD 46-48.
- API Complaint/Risk/Fraud.
- Logic sections 27-29.

## Scope

- Complaint intake in Customer/Driver apps.
- Paid-but-driver-no-show complaint.
- Evidence linkage.
- Admin complaint queue/detail.
- Driver response.
- Auto-lock after 2 qualifying open complaints.
- Manual lock/unlock.
- Fraud case shell/escalation.

## Output

- Payment/no-show dispute can be filed and reviewed.
- Driver auto-lock works.
- Admin can unlock/keep locked.

## Acceptance

- Paid/no-show requires payment proof.
- First qualifying complaint does not auto-lock.
- Second qualifying complaint auto-locks driver and prevents matching.
- Fraud confirmation requires admin/human action.

# 16. Sprint 12 - Hardening and launch QA

## Input docs

- All P0 docs.
- Critical path from PRD Master.

## Scope

- E2E test suite.
- Seed data.
- Observability/logging.
- Error handling consistency.
- Basic load testing for matching/realtime.
- Deployment scripts.
- Production config checklist.
- Security/privacy review checklist.

## Output

- Launch candidate build.
- E2E Ride/Food/dispute scenarios pass.
- Deployment runbook.

## Acceptance

- Fresh DB migration + seed works.
- Ride happy path E2E passes.
- Food happy path E2E passes.
- Paid/no-show auto-lock E2E passes.
- Admin can operate core flows.

# 17. How to assign work to Claude

Do not assign "build all Onway".

Use sprint-level or smaller prompts:

```txt
Read CLAUDE_HANDOFF.md, then implement Sprint 2 only.
Do not implement COD, cash, wallet, Trust Engine, Food fee negotiation, Merchant App or Ads.
Before coding, list exact files/modules you will create.
After coding, run lint/typecheck/tests and summarize remaining gaps.
```

For large sprints, split by module:

- Sprint 5A: brand/outlet.
- Sprint 5B: menu/modifiers.
- Sprint 5C: publishing/effective menu.
- Sprint 8A: ride quote/request.
- Sprint 8B: ride matching.
- Sprint 8C: ride payment/completion/rating.
- Sprint 9A: food discovery/cart/order.
- Sprint 9B: food matching/payment.
- Sprint 9C: restaurant purchase/change/delivery.

# 18. Current blockers before actual coding

These are not product blockers, but implementation details Claude may need:

1. Package manager: npm, pnpm, yarn.
2. Exact Nx setup command/preference.
3. Local Postgres strategy: Docker Compose or existing local DB.
4. Firebase project credentials strategy for local dev.
5. ViHAT credentials mock strategy.
6. HERE Maps API key management.
7. Flutter package choices for GraphQL, maps, state management.
8. Admin/mobile UI reference and design-system decisions.
