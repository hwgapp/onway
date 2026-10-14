# Flow Map

Các mã frame trong cột Steps có liên kết Play trên canvas (nút CTA chính dẫn tới frame kế tiếp).

| Flow ID | Flow Name | Entry Screen | Steps / Screens | Success Exit | Failure / Edge Screens |
| --- | --- | --- | --- | --- | --- |
| UF-001 | Khách đặt Ride đến hoàn thành | C-006 | C-006 → C-012 → C-014 → C-015 → C-016 → C-017 → C-019 → C-023 → C-024 → C-025 → C-028 → C-029 → C-030 → C-031 → C-052; phía tài xế/phụ: D-015 → D-019 → D-020 → D-022 → D-023 → D-025 → D-026 → D-027 → D-028 | C-031 / D-028 | C-007, C-018, C-020, C-021, C-022, C-026, C-027, C-032, D-021, D-024, D-029, A-053 |
| UF-002 | Khách đặt Food đến đã giao | C-006 | C-006 → C-033 → C-035 → C-036 → C-037 → C-038 → C-039 → C-040 → C-042 → C-043 → C-045 → C-046 → C-050 → C-051 → C-052; phía tài xế/phụ: D-015 → D-030 → D-031 → D-032 → D-034 → D-040 → D-041 → D-042 | C-051 / D-042 | C-034, C-041, C-044, C-065, D-033, D-043, A-053 |
| UF-003 | Thay đổi giá/món tại quán | D-034 | D-034 → D-035 → D-036 → C-047 → C-048 → D-037 → D-039 | D-037 → D-040 | C-049, D-038, D-043 |
| UF-004 | Đăng ký & kích hoạt tài xế | D-001 | D-001 → D-002 → D-003 → D-004 → D-005 → D-006 → D-007 → D-008 → D-009 → A-030 → A-031 → A-032 → D-011 → D-012 → D-013 → A-070 → A-071 → D-014 | D-014 → D-015 | D-010, A-032 (từ chối), D-013 (bị từ chối) |
| UF-005 | Khiếu nại & xử lý gian lận/tranh chấp thủ công | C-053 | C-053 → C-054 → A-050 → A-051 → A-052 → A-053 → A-054 → A-055 → A-056 → A-059 → C-063; phía tài xế/phụ: A-036 → D-047 → D-048 → A-037 → A-038 | A-059 / A-038 | A-057, A-060, D-055, D-056, C-062 |
| UF-006 | Admin rollout vùng & chính sách | A-010 | A-010 → A-012 → A-013 → A-014 → A-015 → A-017 → A-018 → A-019 → A-022 → A-023 → A-027 | A-019 / A-027 | A-016, A-020, A-021, A-065, C-007, D-018 |
| UF-007 | Chat & gọi trực tiếp | C-028 | C-028 → C-055 → C-064 → D-022 → D-044 → D-057 | C-055 / D-044 | C-056, C-057, C-058, D-045, D-046 |

## Luồng phụ

| Flow | Steps / Screens | Ghi chú |
| --- | --- | --- |
| Khởi động khách | C-000 → C-001 → C-002 → C-003 → C-004 → C-005 → C-006 | C-000 có trạng thái bắt buộc cập nhật |
| Khởi động tài xế | D-000 → D-001 → D-002 → D-003 | Tài xế mới vào UF-004; tài xế đã kích hoạt vào D-015 |
| Tài khoản khách | C-009 → C-010 / C-011 / C-066 / C-059 / C-062 → C-067 | C-067 có trạng thái bị hạn chế do khiếu nại đang mở |
| Lịch sử & hồ sơ tài xế | D-051 → D-049 / D-053 → D-054 / D-055 → D-056 | |
| Admin đăng nhập | A-000 → A-001 → A-005 | A-003 khi thiếu quyền; A-004 tìm nhanh ⌘K |
| Danh mục Food | A-040 → A-041 → A-042 → A-043 → A-044 → A-045 → A-046 → A-047 → A-049 | A-048 nhập file thủ công (không AI/OCR) |
| Phí nền tảng (Finance) | A-070 → A-071 | cùng dữ liệu với A-033 |
| Quyền riêng tư | C-067 / D-059 → A-075 → A-076 | |
| Landing | L-001 → L-002 → L-003 → L-004 → L-005 → L-006 → L-007 → L-008; L-009, L-010, L-011 | |
