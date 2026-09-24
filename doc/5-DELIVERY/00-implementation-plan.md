# Implementation Plan

## Phases

| Phase | Goal | Exit Criteria |
| --- | --- | --- |
| P0 | Decisions + baseline | TBD |
| P-DS | Design system implementation | Tokens/components implemented and tested |
| P-UI | UI workflow implementation | All designed screens/flows implemented with states |

## Strategy

- TBD

## Design Implementation Requirement

Sau khi Claude Design giao đủ 2 phần:

1. Design system.
2. UI workflow của tất cả màn hình.

Delivery plan phải break thành task implementation cho cả 2 phần:

- Design System Implementation:
  - Tokens.
  - Theme.
  - Shared components.
  - Component variants/states.
  - Component tests/storybook/widgetbook/golden tests tùy stack.
- UI Workflow Implementation:
  - Screen shell/navigation.
  - Flow-by-flow screens.
  - Loading/empty/error/offline/no-permission/paywall states.
  - Integration with mock data/API contract.
  - UI tests/E2E/manual QA for critical flows.

Không được chỉ break task backend/business mà bỏ qua design system hoặc UI workflow.
