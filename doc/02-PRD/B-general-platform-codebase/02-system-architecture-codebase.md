# PRD General: System Architecture & Codebase

**Phase:** P0  
**Status:** Draft  
**Platforms:** All  

## 1. Objective

Define the product-level codebase boundaries and architecture requirements that allow all Onway apps to be built in one coherent Nx monorepo.

## 2. Scope

In scope:

- Nx monorepo structure.
- Shared contracts and shared types.
- Backend, web, mobile app boundaries.
- Environment strategy.
- CI/CD baseline.
- Testing conventions.
- API/realtime contract ownership.

Out of scope:

- Detailed implementation of each feature module.
- Cloud infrastructure provisioning details beyond MVP constraints.

## 3. Architecture Requirements

- The repo must separate deployable apps from shared libraries.
- Backend must use NestJS modular/domain architecture.
- Business APIs use GraphQL.
- High-frequency realtime uses a dedicated WebSocket Gateway.
- PostgreSQL/PostGIS is the system of record for business/geospatial data.
- Redis is used for presence, cache, ephemeral matching state, and possibly queues.
- Firebase Auth provides external authentication; internal database maps roles and account profiles.
- Mobile apps use Flutter.
- Admin Portal uses ReactJS with shadcn/ui and Animate UI.
- Landing Web uses Next.js.

## 4. Suggested Monorepo Boundaries

Apps:

- `apps/api`
- `apps/admin-portal`
- `apps/landing-web`
- `apps/customer-app`
- `apps/driver-app`

Libraries:

- `libs/contracts`
- `libs/types`
- `libs/config`
- `libs/ui-admin`
- `libs/domain`
- `libs/testing`
- `libs/observability`

## 5. User Stories

### US-01 - Developer can find domain ownership

As a developer, I want domain modules and shared libraries to have clear ownership so I can implement a journey without scattering logic across unrelated apps.

Acceptance criteria:

- Each backend domain module owns its entities, services, policies, GraphQL resolvers, and events.
- Shared types/contracts contain cross-app schemas only, not business side effects.
- Mobile app screens consume API/realtime contracts rather than duplicating backend rules.

### US-02 - Developer can implement a vertical journey

As a developer, I want a journey PRD to map cleanly to backend modules, app screens, admin surfaces, events, and tests.

Acceptance criteria:

- Each journey PRD lists touched apps and backend modules.
- Each journey has unit, integration, and end-to-end test expectations.
- Realtime events used by the journey are versioned or documented.

### US-03 - CI catches broken contracts

As a product/engineering team, I want CI to catch broken shared contracts before deployment.

Acceptance criteria:

- CI runs lint, typecheck, unit tests, and builds for changed apps/libs.
- GraphQL schema changes are checked against generated clients or contract tests.
- Flutter builds/tests run for customer and driver app changes before release.

## 6. Acceptance Tests

- Given a backend schema change, when generated app clients are stale, then CI fails.
- Given a shared type changes, when admin/mobile code imports it incorrectly, then typecheck fails.
- Given a PR touches matching realtime contracts, when WebSocket event tests are missing, then CI should flag coverage according to repo policy.
- Given a feature flag is disabled in config, when app surfaces render, then unavailable features are hidden or disabled consistently.

## 7. Implementation Notes

- Keep domain logic in backend, not mobile/web clients.
- Keep app UI state separate from source-of-truth business states.
- Use stable IDs and explicit state machines for Ride, Food, Payment Proof, Driver Lock, Complaint, and Catalog Publishing.
- All business numbers must be policy-configurable unless explicitly constant.

## 8. Open Questions

- Exact Nx plugin layout for Flutter apps.
- Exact deployment pipeline split for mobile/web/backend.
- Whether GraphQL schema registry is needed before MVP.

