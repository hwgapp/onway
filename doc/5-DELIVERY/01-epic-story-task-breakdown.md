# Epic / Story / Task Breakdown

## Task Metadata Required

| Field | Required |
| --- | --- |
| Task ID | Yes |
| Epic/Story | Yes |
| Lane | Yes |
| Depends On | Yes |
| Blocks | Yes |
| Can Run Parallel With | Yes |
| Cannot Run Parallel With | Yes |
| Allowed Paths | Yes |
| Forbidden Paths | Yes |
| Acceptance Criteria | Yes |
| Tests | Yes |
| Test Coverage Expected | Yes |
| Design Source | Required for UI/DS tasks |

## Tasks

| Task ID | Title | Phase | Lane | Size | Depends On | Blocks | Parallel | Test Coverage | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-001 | TBD | P0 | Docs | S | - | TBD | TBD | Docs check | Todo |

## Required Design Implementation Epics

Sau Claude Design handoff, task breakdown phải có tối thiểu 2 nhóm epic này nếu project có UI:

### Epic DS - Design System Implementation

| Task ID | Title | Depends On | Output | Test Coverage |
| --- | --- | --- | --- | --- |
| DS-001 | Implement design tokens/theme | Claude Design design system | Tokens/theme in code | Token/theme tests or visual verification |
| DS-002 | Implement shared components | DS-001 | Component library | Component/widget/story/golden tests |
| DS-003 | Implement component states/variants | DS-002 | Variants/states | State tests/visual review |

### Epic UI - UI Workflow Implementation

| Task ID | Title | Depends On | Output | Test Coverage |
| --- | --- | --- | --- | --- |
| UI-001 | Implement navigation/screen shell | DS-001 | App shell/routes/tabs | Navigation smoke tests |
| UI-002 | Implement core flow screens | UI-001, DS-002 | Screens from UI workflow | UI/widget tests + manual QA |
| UI-003 | Implement screen states | UI-002 | Loading/empty/error/offline/etc. | State tests |
| UI-004 | Critical flow verification | UI-002/003 | E2E/manual QA | E2E or manual QA script |

Các task thật phải thay `UI-002` bằng từng flow/screen group cụ thể từ `doc/4-DESIGN/03-screen-flow-requirements.md` và `doc/2-PRD/02-screen-inventory.md`.
