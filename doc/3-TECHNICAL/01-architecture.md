# Architecture

## Goals

- Build nhanh MVP Ride + Food nhưng vẫn giữ module boundary rõ để scale/tách service sau này.
- Hỗ trợ money-light Ride/Food với payment proof/evidence/audit thay vì payment gateway.
- Hỗ trợ realtime location, matching, tracking và chat với WebSocket riêng.
- Hỗ trợ region polygon, distance/geofence và service availability bằng PostGIS.
- Cho phép mở rộng future Trust, Mission, Community Truth và AI Ops mà không phá core flow.
- Admin Portal đủ vận hành day 1, không phụ thuộc script/manual DB cho luồng chính.

## System Context

```text
Customer App / Driver App / Admin Portal / Landing Web
  -> GraphQL API: profile, Ride/Food lifecycle, menu, admin config, complaint/fraud
  -> WebSocket Gateway in backend-api: location, availability, matching, tracking, chat events

NestJS Modular Monolith: one deployable backend-api for GraphQL + WebSocket in P0
  -> PostgreSQL + PostGIS: system of record, region, orders, audit, evidence metadata
  -> Redis: presence, cache, active offer lock, ephemeral matching state, BullMQ
  -> S3: media/evidence storage
  -> Firebase Auth: identity token verification
  -> ViHAT: OTP/SMS
  -> HERE Maps: maps/geocoding/routing
```

## Module Boundaries

| Module | Responsibility | Notes |
| --- | --- | --- |
| identity | Auth mapping, Firebase ID token verification, internal user identity | ViHAT OTP flow creates Firebase custom token |
| customer | Customer profile, customer status, preferences | P0 |
| driver | Driver profile, onboarding, verification, activation status | P0 |
| admin | Admin user/role mapping, admin operations | P0, RBAC draft in `doc/2-PRD/07-permission-matrix.md` |
| region | Country/city/region, polygon, service area lifecycle | P0, PostGIS-heavy |
| vehicle | Vehicle types, driver vehicle/service eligibility | P0 |
| pricing | Ride recommended price, Food delivery fee, guardrails | P0 |
| matching | Candidate selection, wave dispatch, locks, offer lifecycle | P0, Redis + PostGIS |
| ride | Ride request/trip lifecycle | P0 |
| food-order | Food order lifecycle, prepaid confirmation, order-at-restaurant flow | P0 |
| restaurant | Brand/outlet management | P0 admin-first |
| menu | Canonical menu, outlet override, item/modifier state | P0 admin-first |
| complaint | Complaint intake and manual dispute workflow | P0 |
| fraud | Risk status, fraud case lifecycle, manual/admin lock, rule-based auto-lock event handling | P0 minimal |
| subscription / platform-fee | Driver platform fee, proof/reference, admin verification | P0 |
| notification | Push notifications for job, payment, chat and lock events | P0 baseline; no marketing push P0 |
| media-evidence | Upload, S3 private/public classification, proof/evidence metadata | P0 |
| device-risk | Device id/fingerprint, risk signals, abuse correlation | P0 minimal; privacy/legal review required |
| audit-log | Audit trail for policy/config/state/admin/human/AI decisions | P0 |
| policy-config | Config for region, timeout, thresholds, fee policy, guardrails | P0 |
| app-version | Mobile min-version/force-update config | P0 |
| map-routing | HERE geocode/routing abstraction, cache and fallback | P0 |
| trust | Trust levels/privileges | Future shell only; no P0 runtime logic |
| mission | Driver field tasks | Future shell only; no P0 runtime logic |
| community-truth | Evidence/confidence/verified data model | Future shell only; no P0 runtime logic |
| referral | Customer/driver referral lifecycle | Future shell only; no P0 runtime logic |
| reward | Reward eligibility/payment workflow | Future shell only; no P0 runtime logic |
| ai-ops | AI recommendation/triage/support workflows | Future shell only; no P0 runtime logic |

## Folder Structure

Planned only; do not scaffold before G4 freeze.

```text
apps/
  backend-api/        # NestJS modular monolith
  admin-portal/       # ReactJS
  landing-web/        # Next.js
  mobile-user/        # Flutter Customer App
  mobile-driver/      # Flutter Driver App
packages/
  contracts/          # GraphQL schema, generated types, shared DTO docs
  config/             # shared lint/test/build config
  ui-admin/           # admin UI components if needed
  mobile-shared/      # Flutter shared packages/components
  test-utils/
tools/
  scripts/
```

P0 uses one NestJS deployment for API + WebSocket in `apps/backend-api`. A separate realtime deployable can be introduced after load/ownership requires it.

## G4 Defaults

- Scaffold path after G4: `apps/backend-api`, `apps/admin-portal`, `apps/landing-web`, `apps/mobile-user`, `apps/mobile-driver`, `packages/contracts`, `packages/config`, `packages/ui-admin`, `packages/mobile-shared`, `packages/test-utils`.
- Future modules may be reserved as folders/interfaces during scaffold, but should not be wired into runtime or given fake business logic until their gate is reopened.
- Keep GraphQL schema/query documents in `packages/contracts` so Flutter and React Admin codegen use the same source of truth.
