# ONWAY Documentation Index

Day la bo tai lieu lam viec cho Onway MVP. Neu dua vao Claude/dev de code, bat dau tu handoff va backlog, sau do doc cac spec theo scope sprint.

## Recommended read order for implementation

1. [08-Implementation/CLAUDE_HANDOFF.md](./08-Implementation/CLAUDE_HANDOFF.md)
2. [08-Implementation/ONWAY_IMPLEMENTATION_BACKLOG_P0_v0.1.md](./08-Implementation/ONWAY_IMPLEMENTATION_BACKLOG_P0_v0.1.md)
3. [08-Implementation/CLAUDE_SPRINT_PROMPTS_P0.md](./08-Implementation/CLAUDE_SPRINT_PROMPTS_P0.md)
4. [02-PRD/ONWAY_PRD_MASTER_v0.1_VI.md](./02-PRD/ONWAY_PRD_MASTER_v0.1_VI.md)
5. [05-Logic/ONWAY_LOGIC_P0_v0.1.md](./05-Logic/ONWAY_LOGIC_P0_v0.1.md)
6. [06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md](./06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md)
7. [06-API/ONWAY_GRAPHQL_SCHEMA_P0_v0.1.graphql](./06-API/ONWAY_GRAPHQL_SCHEMA_P0_v0.1.graphql)
8. [07-Realtime/ONWAY_REALTIME_EVENT_CONTRACT_P0_v0.1.md](./07-Realtime/ONWAY_REALTIME_EVENT_CONTRACT_P0_v0.1.md)
9. [07-Realtime/ONWAY_REALTIME_EVENT_CATALOG_P0_v0.1.json](./07-Realtime/ONWAY_REALTIME_EVENT_CATALOG_P0_v0.1.json)
10. [09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md](./09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md)
11. [10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md](./10-Testing/ONWAY_TEST_PLAN_P0_v0.1.md)
12. [04-Database/ONWAY_DB_SCHEMA_P0_v0.1.md](./04-Database/ONWAY_DB_SCHEMA_P0_v0.1.md)
13. [04-Database/ONWAY_DB_MIGRATION_STRATEGY_P0_v0.1.md](./04-Database/ONWAY_DB_MIGRATION_STRATEGY_P0_v0.1.md)
14. Relevant detailed PRD under [02-PRD](./02-PRD/README.md)
15. [01-BRD/ONWAY_BRD_v0.5_VI.md](./01-BRD/ONWAY_BRD_v0.5_VI.md)
16. [03-Architecture/ONWAY_ARCHITECTURE_DECISIONS_v0.2_VI.md](./03-Architecture/ONWAY_ARCHITECTURE_DECISIONS_v0.2_VI.md)

## P0 guardrails

- No COD, cash, payment gateway, wallet, escrow or Onway-held Ride/Food money.
- Ride/Food use direct bank transfer/QR customer -> driver with required payment proof.
- Food has no delivery fee negotiation.
- Food catalog is admin-first; driver does not manage restaurant/menu in P0.
- Chat between customer and driver supports text and image with 1 week retention.
- Driver auto-locks after 2 qualifying open paid/no-show complaints; admin can manual lock/unlock.
- Full Trust Engine, Merchant App, Mission, Community Truth, AI OCR/menu extraction production flow and Ads are post-launch/future unless explicitly reprioritized.
