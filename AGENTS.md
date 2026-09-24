# AGENTS.md

Hướng dẫn bắt buộc cho Codex, ORCA, Claude Code và mọi coding/design agent làm việc trong dự án tạo từ template này.

## Luật Chung

1. Đọc `README.md`, `PROJECT_STATUS.md`, `SDLC_CONFIG.md` và `doc/00-source-of-truth.md` trước khi làm.
2. Không tự đoán business rule nếu còn open question quan trọng. Ghi vào `doc/0-INBOX/04-open-questions.md`.
3. Không sửa code hoặc docs ngoài scope task nếu chưa được giao.
4. Không tạo technical stack/code skeleton trước khi gate Technical được chốt.
5. Mọi quyết định mới phải ghi vào decision log tương ứng.
6. Khi task xong, cập nhật `doc/5-DELIVERY/04-task-status.md` và báo task nào được unblock.
7. Giữ output ngắn, có file path, command test và blocker nếu có.

## Thứ Tự Nguồn Sự Thật

Theo `doc/00-source-of-truth.md`. Tóm tắt:

```text
Decision log > BRD/PRD đã chốt > Technical > Design handoff/mockup > Delivery task > Inbox/raw notes
```

## Khi Giao Task Cho ORCA

Mỗi task phải có:

- Task ID ổn định.
- Dependencies.
- Parallel/cannot parallel.
- Allowed paths.
- Forbidden paths.
- Schema/codegen permission.
- Acceptance criteria.
- Tests/verification.
- Completion report.

Không giao task dạng “build app”, “làm UI”, “implement backend” nếu chưa phân rã.

## Tiết Kiệm Token

- Trỏ đến file/section thay vì paste tài liệu dài.
- Mỗi task chỉ đọc docs liên quan.
- Nếu task cần đọc quá nhiều docs, chia thành task chuẩn bị hoặc task con.
- Completion report không tóm tắt lại toàn bộ dự án.

