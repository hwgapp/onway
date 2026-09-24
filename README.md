# SDLC Template

Template này dùng để khởi tạo nhiều dự án phần mềm theo cùng một quy trình:

```text
Business intake -> BRD -> PRD -> Technical -> Design handoff -> Delivery task graph -> ORCA implementation -> QA/release
```

Nguyên tắc chính:

- Không khóa technical stack ở template.
- Tài liệu mặc định viết bằng tiếng Việt.
- Codex phỏng vấn theo từng gate bằng câu hỏi chọn đáp án.
- Task cho ORCA phải có dependency, khả năng chạy song song, allowed/forbidden paths, acceptance criteria và test.
- Theo dõi tiến độ đơn giản bằng Markdown.
- Tiết kiệm token: task trỏ đến file/section thay vì copy dài nội dung.

## Bắt Đầu Dự Án Mới

1. Copy toàn bộ template này vào folder dự án mới.
2. Mở `PROJECT_STATUS.md` và đặt tên dự án, gate hiện tại.
3. Dùng `doc/0-INBOX/06-question-bank.md` để Codex phỏng vấn business.
4. Ghi câu trả lời vào `doc/0-INBOX/03-intake-answers.md`.
5. Đi lần lượt qua gate trong `doc/5-DELIVERY/11-gate-checklists.md`.
6. Chỉ tạo code skeleton sau khi qua gate Technical.

## File Quan Trọng

- `AGENTS.md`: luật làm việc cho Codex/ORCA/Claude Code.
- `SDLC_CONFIG.md`: cấu hình bật/tắt theo dự án.
- `PROJECT_STATUS.md`: dashboard ngắn.
- `doc/00-source-of-truth.md`: thứ tự ưu tiên khi tài liệu mâu thuẫn.
- `doc/5-DELIVERY/04-task-status.md`: bảng trạng thái task.
- `doc/5-DELIVERY/05-orca-task-template.md`: mẫu giao task cho ORCA.

