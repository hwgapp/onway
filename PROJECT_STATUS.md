# Project Status

> File dashboard ngắn. Cập nhật sau mỗi gate hoặc sau mỗi batch ORCA.

## Snapshot

| Mục | Giá trị |
| --- | --- |
| Tên dự án | Onway |
| Gate hiện tại | G5 - Claude Design Handoff |
| Phase hiện tại | Design handoff preparation |
| Trạng thái | BRD/PRD/Technical frozen; Design System imported, chờ UI Workflow/mockups |
| Người phụ trách quyết định | User |
| Cập nhật lần cuối | 2026-09-24 |

## Progress

| Nhóm | % | Ghi chú |
| --- | ---: | --- |
| Business / BRD | 100% | G2 pass; cập nhật D-024: bỏ Ride negotiation P0, giữ Ride+Food, auto-lock tối giản và Admin polygon tool |
| PRD | 100% | G3 pass; đã chốt direct transfer, payment proof/dispute, Food proposal, polygon, auto-lock, RBAC, push/chat/rating/analytics |
| Technical | 100% | G4 pass; đã chốt stack, module boundary, API/data/state, security/privacy baseline, test commands và scaffold paths |
| Design handoff | 72% | Đã import Claude Design System bản mới có component previews/types và tạo full app screen/frame map + P0 coverage audit; còn thiếu UI Workflow/mockups từ Claude Design |
| Delivery task graph | 0% | Chưa bắt đầu |
| Implementation | 0% | Chưa bắt đầu |
| QA / Release | 0% | Chưa bắt đầu |

## Task Summary

| Status | Count |
| --- | ---: |
| Todo | 0 |
| Ready | 0 |
| Running | 1 |
| Review | 0 |
| Done | 0 |
| Blocked | 0 |

## Blockers

| ID | Blocker | Owner | Needed By |
| --- | --- | --- | --- |
| G5-001 | Chưa có Claude UI Workflow/mockups theo full frame map để import vào `doc/4-DESIGN/mockups/` | Design/User | G5/G6 |

## Next Actions

1. Lấy tiếp Claude UI Workflow/mockups theo `doc/4-DESIGN/08-full-app-screen-frame-map.md`.
2. Import UI Workflow output vào `doc/4-DESIGN/mockups/`.
3. Review G5/G6 checklist rồi phân rã Delivery Task Graph.
4. Sau G4, được phép tạo code skeleton theo paths đã chốt khi user giao implement.
