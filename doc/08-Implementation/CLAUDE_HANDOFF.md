# CLAUDE HANDOFF - ONWAY MVP

You are implementing Onway MVP from documentation in this repository.

## Read order

1. `doc/08-Implementation/ONWAY_IMPLEMENTATION_BACKLOG_P0_v0.1.md`
2. `doc/02-PRD/ONWAY_PRD_MASTER_v0.1_VI.md`
3. `doc/05-Logic/ONWAY_LOGIC_P0_v0.1.md`
4. `doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md`
5. `doc/07-Realtime/ONWAY_REALTIME_EVENT_CONTRACT_P0_v0.1.md`
6. `doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md`
7. `doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md`
8. `doc/04-Database/ONWAY_DB_SCHEMA_P0_v0.1.md`
9. `doc/04-Database/ONWAY_DB_MIGRATION_STRATEGY_P0_v0.1.md`
10. Relevant detailed PRD under `doc/02-PRD/*/*.md`
11. `doc/01-BRD/ONWAY_BRD_v0.5_VI.md`
12. `doc/03-Architecture/ONWAY_ARCHITECTURE_DECISIONS_v0.2_VI.md`

## Source priority

If documents conflict, use this priority:

1. Implementation handoff/backlog.
2. PRD Master and P0 detailed PRDs.
3. Logic/API/Realtime/UI/Testing/Database technical specs.
4. BRD v0.5.
5. Architecture v0.2.

Do not use older assumptions from previous versions if they conflict with current P0 decisions.

## Non-negotiable P0 decisions

- No COD.
- No cash payment.
- No payment gateway for Ride/Food.
- No wallet, escrow, or Onway-held Ride/Food payment.
- Only direct bank transfer/QR between customer and driver for Ride/Food.
- Payment proof is required.
- Food has no delivery fee negotiation.
- Full Trust Engine is postponed.
- Merchant App is postponed.
- Driver does not manage restaurant/menu in P0.
- Food catalog is admin-first.
- Chat supports text and image.
- Chat content/image retention is 1 week.
- Driver auto-locks after 2 qualifying open paid/no-show complaints.
- Admin can manually lock/unlock driver.

## Architecture decisions

- Nx monorepo.
- Backend: Node.js + NestJS modular monolith.
- GraphQL: NestJS code-first.
- Realtime: separate WebSocket Gateway.
- DB: PostgreSQL + PostGIS.
- ORM/DAL: Prisma, with controlled raw SQL for PostGIS.
- Redis: presence, cache, BullMQ queues, ephemeral matching state.
- Auth: ViHAT OTP through backend -> Firebase custom token -> Firebase ID token for API/WebSocket.
- Admin Portal: ReactJS + shadcn/ui + Animate UI.
- Customer App and Driver App: Flutter.
- Map provider: HERE Maps.
- Cloud target: AWS.

## Before coding any sprint

1. State which sprint/sub-sprint you are implementing.
2. List docs read.
3. List modules/files you expect to create/change.
4. Confirm excluded features remain excluded.
5. Implement only the requested sprint scope.
6. Run available lint/typecheck/tests.
7. Summarize what works, what is stubbed, and what remains.
8. Check the sprint Definition of Done in `doc/10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md`.

## Coding boundaries

- Keep business logic server-side.
- Clients render `allowedActions`; they do not decide business permissions.
- Use transactions for state transitions.
- Emit realtime events only after commit.
- Write audit logs for critical admin/system decisions.
- Keep raw SQL inside repositories/services, not resolvers.
- Use policy config for business values.
