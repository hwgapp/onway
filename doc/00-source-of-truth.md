# Source Of Truth

Khi tài liệu mâu thuẫn, áp dụng thứ tự ưu tiên sau:

1. Decision log đã chốt:
   - `doc/1-BRD/01-decision-log.md`
   - `doc/3-TECHNICAL/08-technical-decisions.md`
2. BRD/PRD đã qua gate review:
   - `doc/1-BRD/**`
   - `doc/2-PRD/**`
3. Technical architecture và contracts:
   - `doc/3-TECHNICAL/**`
4. Design handoff, design system, mockup:
   - `doc/4-DESIGN/**`
5. Delivery task breakdown:
   - `doc/5-DELIVERY/**`
6. Inbox/raw notes:
   - `doc/0-INBOX/**`

## Quy Tắc

- Nếu business rule mâu thuẫn với mockup, theo business rule/PRD.
- Nếu technical contract mâu thuẫn với task breakdown, cập nhật task breakdown theo contract đã chốt.
- Nếu decision mới thay đổi scope, cập nhật decision log trước, sau đó cập nhật PRD/Technical/Delivery.
- Không sửa raw notes để “làm sạch lịch sử”; tạo bản tổng hợp ở BRD/PRD.

