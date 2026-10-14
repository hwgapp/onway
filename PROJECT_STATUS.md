# Project Status

> File dashboard ngắn. Cập nhật sau mỗi gate hoặc sau mỗi batch ORCA.

## Snapshot

| Mục | Giá trị |
| --- | --- |
| Tên dự án | Onway |
| Gate hiện tại | G5 - Claude Design Handoff |
| Phase hiện tại | Design handoff preparation |
| Trạng thái | BRD/PRD/Technical frozen; Design System + UI Workflow (216 frame) imported, chờ review G5/G6 |
| Người phụ trách quyết định | User |
| Cập nhật lần cuối | 2026-09-24 |

## Progress

| Nhóm | % | Ghi chú |
| --- | ---: | --- |
| Business / BRD | 100% | G2 pass; cập nhật D-024: bỏ Ride negotiation P0, giữ Ride+Food, auto-lock tối giản và Admin polygon tool |
| PRD | 100% | G3 pass; đã chốt direct transfer, payment proof/dispute, Food proposal, polygon, auto-lock, RBAC, push/chat/rating/analytics |
| Technical | 100% | G4 pass; đã chốt stack, module boundary, API/data/state, security/privacy baseline, test commands và scaffold paths |
| Design handoff | 95% | Design System + UI Workflow đã import (`doc/4-DESIGN/mockups/`, 216/216 frame); còn review G5/G6 và chốt OQ-022…OQ-026 |
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
| G5-002 | Cần user chốt OQ-022…OQ-026 (thời gian chờ Ride, xử lý từ chối đề xuất Food, ẩn số điện thoại, số liệu cấu hình mẫu, nội dung pháp lý) | User | G5/G6 |

## Next Actions

1. User review canvas Onway UI Workflow và trả lời OQ-022…OQ-026.
2. Chạy `doc/4-DESIGN/05-design-review-checklist.md` cho G5/G6.
3. Cập nhật traceability matrix DS/UI mapping, rồi phân rã Delivery Task Graph.
4. Sau G4, được phép tạo code skeleton theo paths đã chốt khi user giao implement.
