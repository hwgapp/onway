# Component State Matrix

| Component ID | Variant | State | Visual Requirement | Behavior | Accessibility |
| --- | --- | --- | --- | --- | --- |
| CMP-003 | Primary | Default | Nền `red-500`, chữ trắng, cao 48 (mobile) / 40 (web) | Một nút primary mỗi màn | Contrast 4.6:1 |
| CMP-003 | Primary | Pressed | Nền `red-700`, scale .975 | — | — |
| CMP-003 | Primary | Loading | Spinner thay icon, giữ nguyên độ rộng | Chặn submit lặp | `aria-busy`, đọc "Đang xử lý" |
| CMP-003 | Primary | Disabled | Nền `ink-100`, chữ `ink-400` | Không nhận tap | `aria-disabled` + lý do gần đó |
| CMP-003 | Secondary | Default | Nền `ink-950`, chữ trắng | Hành động phụ mạnh | 18:1 |
| CMP-003 | Outline / Ghost | Hover | Viền → `ink-950` / nền `ink-100` | — | Focus ring 2+2px |
| CMP-003 | Destructive | Default | Viền + chữ `red-600`, icon cảnh báo | Luôn qua Dialog xác nhận | Không chỉ dựa vào màu |
| CMP-004 | Toolbar / Row | Default | 40×40 (web), 44×44 (mobile) | — | `aria-label` bắt buộc; Tooltip trên web |
| CMP-013 | Info | matching / searching | Nền info-subtle, chấm nhấp nháy | Pulse 1.6s | Tắt pulse khi reduced motion |
| CMP-013 | Warning | proofPending / pendingReview | Nền warning-subtle, dấu ! | — | Nhãn chữ đầy đủ |
| CMP-013 | Success | completed / proofVerified | Nền success-subtle, dấu ✓ | — | — |
| CMP-013 | Danger | proofRejected / disputed / locked | Nền danger-subtle, dấu ✕ hoặc ! | — | Hình + chữ, không chỉ màu đỏ |
| CMP-013 | Neutral | cancelled / expired / draft | Nền sunken, chữ secondary | — | — |
| CMP-016 | Text | Focus | Viền `ink-950` 1.5px | — | Label luôn hiển thị, không dùng placeholder thay label |
| CMP-016 | Text | Error | Viền `red-600`, icon + helper text đỏ | Hiện khi blur hoặc submit | `aria-invalid`, `aria-describedby` |
| CMP-016 | Text | Disabled | Nền sunken, chữ disabled | — | — |
| CMP-020 | Line / Block | Loading | Shimmer 1.4s trên `surface-sunken` | Giữ đúng kích thước nội dung thật | `role=status` "Đang tải"; tắt shimmer khi reduced motion |
| CMP-022 | Offline | Persistent | Nền inverse, icon wifi-off | Tự ẩn khi có mạng; action "Thử lại" | `role=status` |
| CMP-022 | Warning | Region unavailable | Nền warning-subtle | Chặn CTA đặt xe | — |
| CMP-022 | Locked | No permission | Nền sunken, icon lock | Không hiện dữ liệu | Giải thích cách xin quyền |
| CMP-022 | Danger | Error | Nền danger-subtle | Có action khôi phục | `role=alert` |
| CMP-024 | Success / Error | Visible | Nền inverse, 4s | Tự đóng; tối đa 1 action | `aria-live=polite` (error: assertive) |
| CMP-025 | Confirm | Open | Overlay `surface-overlay`, radius 16 | Esc/nút huỷ đóng | Focus trap, trả focus khi đóng |
| CMP-025 | Critical | Reason required | Input lý do bắt buộc | Nút xác nhận disabled đến khi có lý do | — |
| CMP-026 | Detail / Action | Expanded / Collapsed | Radius 20 trên, handle 36×4 | Kéo để mở rộng | Handle có `aria-label` |
| CMP-030 | Default | Route | Route than 5px viền trắng; đón = chấm than, đến = pin đỏ, tài xế = puck than | — | Ẩn với screen reader; thông tin nằm ở Sheet |
| CMP-030 | Region | active / selected / paused / invalid | Polygon nét đứt than / nét liền đỏ / cam / đỏ chấm | Admin chọn để sửa | Trạng thái lặp lại bằng StatusPill |
| CMP-030 | Overlay | loading / noPermission / offline | Thẻ nổi đáy bản đồ, icon + chữ | loading làm xám bản đồ | `role=status` |
| CMP-031 | Ride / Food | In progress | Pill pulse, headline 18/700, step bar | Cập nhật realtime | `aria-current=step` |
| CMP-031 | Ride / Food | Issue / Disputed / Cancelled | Step hiện tại chuyển đỏ | Hiện action hỗ trợ | Pill có hình ! / ✕ |
| CMP-032 | Route / Audit | done / current / pending / failed | Chấm than / đỏ có halo / rỗng / vuông đỏ | Audit không sửa được | Failed có chữ, không chỉ màu |
| CMP-040 | Customer | Empty | Khung nét đứt, icon, hướng dẫn định dạng | Tap mở camera/thư viện | Nút có nhãn đầy đủ |
| CMP-040 | Customer | Uploading | Pill "Đang tải lên", progress bar | Không cho gửi lần hai | `role=progressbar` |
| CMP-040 | Customer | Failed | Viền đỏ, lý do + "Thử lại" | Giữ file cục bộ để thử lại | — |
| CMP-040 | Customer | Submitted | Pill "Chờ xác nhận", ghi chú tài xế sẽ xác nhận | Chờ tài xế | — |
| CMP-040 | Driver/Admin | Verified / Rejected | Pill success / danger + lý do | Rejected cho khách tải lại | Ảnh chứng từ chỉ mở trong job/case |
| CMP-050 | Dense | Loading | 5 hàng skeleton | Giữ header | — |
| CMP-050 | Dense | Empty | "Không có dữ liệu phù hợp bộ lọc." | Gợi ý xoá bộ lọc | — |
| CMP-050 | Dense | Error | Icon + thông báo + "Thử lại" | — | — |
| CMP-050 | Selectable | Selected | Hàng nền `surface-hover` | Toolbar bulk action hiện | `aria-selected`, checkbox có nhãn |
| CMP-050 | Sortable | Sorted | Mũi tên lên/xuống, header chữ primary | Click đổi chiều | `aria-sort` |
