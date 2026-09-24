# Traceability Matrix

Mục tiêu: đảm bảo không sót yêu cầu từ business đến implementation.

| Business Req ID | PRD Feature | Screen/Flow | API/Data | Design System/Component | UI Workflow/Mockup | Task ID | Test/AC | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BR-001 | F-001 | S-001 / UF-001 | API-001 | DS-001 | UI-001 | T-001 | AC-001 | Todo |

## Quy Tắc

- Mỗi business requirement phase 1 phải map tới ít nhất một PRD feature hoặc được ghi out-of-scope.
- Mỗi feature phase 1 phải có task implementation hoặc được ghi deferred.
- Mỗi critical flow phải có test/AC.
- Mỗi screen phase 1 phải map tới UI workflow/mockup hoặc được ghi chưa design.
- Mỗi shared component phải map tới design system implementation task.
