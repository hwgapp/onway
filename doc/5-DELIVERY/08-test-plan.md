# Test Plan

Test là tiêu chí bắt buộc để đảm bảo stability. Mọi task code phải có verification tương ứng với risk.

## Test Strategy

| Layer | Required? | Notes |
| --- | --- | --- |
| Unit | Yes for domain/logic | Logic, formatter, validator, state reducer, calculation |
| Integration | Yes for API/data/integration | API contract, repository, DB, external service fakes; no Ride/Food payment gateway P0 |
| UI/Widget/Component | Yes for reusable/critical UI | Components, screen states, form validation |
| E2E | Required for critical flows before release | Core happy path + at least one failure path |
| Manual QA | Required when automation unavailable | Must include exact steps and expected result |

## Coverage Expectations

| Task Type | Minimum Verification |
| --- | --- |
| Business logic | Unit tests for success, edge, failure |
| API/backend | Unit + integration/contract test |
| Data model/migration | Migration apply + seed/rollback or drift check |
| UI component | Component/widget test for variants/states |
| Screen/flow | UI test or manual QA, E2E if critical |
| Bug fix | Regression test that fails before/without fix |
| Refactor | Existing tests pass + targeted test if behavior risk |
| Docs only | Link/check consistency, no code test required |

## Test Commands

Command chính xác có thể đổi theo package manager khi scaffold Nx monorepo, nhưng G4 baseline là:

| Area | Command | Notes |
| --- | --- | --- |
| All | `npm run lint && npm run typecheck && npm test && npm run build` | Wrapper scripts should call Nx/Flutter after scaffold |
| Nx all | `npx nx run-many -t lint,test,build` | Runs configured projects |
| Backend unit | `nx test backend-api` | NestJS domain/module unit tests |
| Backend integration | `nx test backend-api --configuration=integration` | DB/API/integration tests with local Postgres/PostGIS and Redis |
| Admin | `nx test admin-portal` | React component/unit tests |
| Landing | `nx test landing-web` | Nếu có test setup |
| Mobile Customer | `cd apps/mobile-user && flutter test` | Flutter widget/unit tests |
| Mobile Driver | `cd apps/mobile-driver && flutter test` | Flutter widget/unit tests |
| E2E/API | `nx test backend-api --configuration=e2e` | API critical flows; browser/mobile E2E added after scaffold |

## Critical Flows

| Flow | Test Type | Owner | Status |
| --- | --- | --- | --- |
| Customer Ride request -> match -> direct payment proof -> trip complete | E2E/API + manual QA | Backend/Mobile/QA | Todo |
| Customer Food order -> match -> payment proof -> driver confirm -> order at restaurant -> delivered | E2E/API + manual QA | Backend/Mobile/QA | Todo |
| Food price/item change proposal -> customer accept/reject | API/UI/manual QA | Backend/Mobile/QA | Todo |
| Driver onboarding -> platform fee proof -> admin verify -> activate | API/Admin/manual QA | Backend/Admin/QA | Todo |
| Region polygon/service availability blocks out-of-region request | Integration/API | Backend/Admin/QA | Todo |
| Complaint -> fraud case manual lifecycle -> final decision | API/Admin/manual QA | Backend/Admin/QA | Todo |
| Driver location WebSocket -> matching/tracking update | Integration/E2E | Backend/Mobile/QA | Todo |
| Customer-driver chat text/image retention behavior | Integration/manual QA | Backend/Mobile/QA | Todo |

## Manual QA Template

```text
Scenario:
Preconditions:
Steps:
Expected:
Evidence:
```

## Release Quality Gate

- [ ] All critical automated tests pass.
- [ ] Manual QA scripts for non-automated critical flows pass.
- [ ] No known P0/P1 bugs.
- [ ] Test gaps documented and accepted.
