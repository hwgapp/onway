# Onway Design System

## 1. Nguyên tắc

1. **Đơn sắc là chính.** Đen, trắng, xám mang giao diện. Đỏ `#E22240` chỉ cho CTA chính và logo.
2. **Trạng thái đọc được trong một cái liếc.** Mỗi màn hình vận hành (chuyến, đơn, chứng từ) có một trạng thái rõ ràng ở trên cùng.
3. **Gọn và chuyên nghiệp.** Radius nhỏ (8/12), bóng gần như không thấy, viền hairline tách lớp.
4. **Tiếng Việt trước.** Mọi nhãn viết tiếng Việt tự nhiên, ngắn; kiểm tra dấu và độ dài trước.

## 2. Foundation

### Màu

| Vai trò | Token | Giá trị |
| --- | --- | --- |
| Brand red | `red-500` = `logo-red` | `#E22240` |
| Brand charcoal | `ink-800` = `logo-ink` | `#2F2E2E` |
| Nền trang | `surface-page` | `#F5F5F4` |
| Card | `surface-card` | `#FFFFFF` |
| Chữ chính | `text-primary` | `#0F0E0E` |
| Chữ phụ | `text-secondary` | `#555453` |
| Viền | `border-default` | `#E1E0DF` |
| CTA | `action-primary-bg` | `#E22240` |
| Hành động phụ mạnh | `action-secondary-bg` | `#0F0E0E` |
| Success / Info / Warning / Accent | `green-500` / `blue-500` / `amber-500` / `violet-500` | `#2E9E6B` / `#4C7DF0` / `#E2A33C` / `#7B6BE6` |
| Danger (chữ, viền) | `red-600` | `#C31834` |

Chi tiết đầy đủ: `tokens.json › color`.

### Typography — Be Vietnam Pro

| Vai trò | Size / line-height / weight | Dùng |
| --- | --- | --- |
| Display | 52 / 1.06 / 800 | Landing |
| Heading XL–SM | 32 · 26 · 22 · 18 / 1.18 / 700 | Tiêu đề màn, sheet |
| Body LG / MD / SM | 17 · 15 · 13 / 1.55 / 400 | Nội dung |
| Label | 13 / 1.3 / 600 | Nút, nhãn form |
| Caption | 12 | Metadata |
| Overline | 11 / +0.09em / uppercase | Nhóm section admin |
| Numeric | JetBrains Mono 15 / 500 | Giá, mã tham chiếu, ETA |

Admin dùng body 13 và row 44px cho bảng dày.

### Spacing — lưới 4px

`2 · 4 · 8 · 12 · 16 · 20 · 24 · 28 · 32 · 40 · 48 · 64 · 80 · 96 · 128`. Gutter mobile 16, web 20. Control 32/40/48/56. Touch target ≥ 44.

### Radius

Control 8 · Card 12 · Sheet 20 · Dialog 16 · Pill 999.

### Elevation

Viền hairline tách lớp; shadow chỉ khi phần tử nổi: `shadow-md` (overlay trên bản đồ), `shadow-sheet` (bottom sheet), `shadow-lg` (dialog, drawer).

### Motion

Instant 80 · Fast 140 · Base 200 · Slow 320 · Sheet 380ms. Easing `cubic-bezier(.2,0,0,1)`. Nhấn nút scale .975. Chỉ xác nhận đặt chuyến thành công được dùng spring.

### Icon

Lucide, nét 2px, 16/20/24px, kế thừa `currentColor`. Icon-only luôn có nhãn.

### Logo

- Nền sáng: `logo.svg` — On `#E22240`, Way `#2F2E2E`.
- Nền đỏ `#E22240` hoặc than: `logo-dark.svg` — toàn trắng.
- Không vẽ lại, đổi màu, xoay, thêm hiệu ứng. Khoảng trống quanh logo = chiều cao chữ O. Tối thiểu 20px chiều cao.
- App icon lấy từ mark (vòng tròn), không dùng wordmark.

## 3. Component spec (P0)

Spec rút gọn cho các component domain. Component cơ bản (Button, Input, Card…) có spec trong `components/*/<Name>.prompt.md` và `.d.ts` của design system.

### CMP-013 StatusPill

- **Purpose:** Hiển thị trạng thái nghiệp vụ thống nhất cho Ride, Food, thanh toán, tài xế, khu vực, case.
- **Anatomy:** Nền tone-subtle · mark (chấm/✓/✕/!) · nhãn.
- **Variants:** size `sm` (22px, bảng) / `md` (26px).
- **States:** 34 key, 6 tone — xem `tokens.json › status`.
- **Tokens:** `surface-*-subtle`, `text-*`, `radius-full`, `font-size-caption`.
- **Accessibility:** Hình + chữ; pulse tắt khi reduced motion.
- **Do:** Dùng đúng key từ backend. **Don't:** Dùng làm filter (dùng Tag).
- **Used in:** S-003…S-021.

### CMP-030 MapSurface

- **Purpose:** Nền bản đồ cho mọi màn vị trí.
- **Anatomy:** Land · block · park · water · road/road-major · route · pins · region polygon · overlay trạng thái.
- **Variants:** `route`, `pins`, `region` (none/active/selected/paused/invalid).
- **States:** default, loading, noPermission, offline.
- **Responsive:** Full-bleed mobile; admin chiếm vùng nội dung chính.
- **Usage:** UI nổi trên bản đồ dùng `surface-card` + `shadow-md`. Không phủ màu lên bản đồ.
- **Used in:** S-002…S-004, S-007, S-008, S-012…S-014, S-017.

### CMP-031 JobStatusHeader

- **Purpose:** Trạng thái chuyến/đơn đang chạy ở đầu sheet.
- **Anatomy:** StatusPill · meta số (ETA/giá) · headline · dòng phụ · step track.
- **States:** mọi status; issue/disputed/cancelled làm step hiện tại đỏ.
- **Usage:** Một header mỗi màn; headline viết theo người dùng ("Anh Minh đang đến điểm đón").
- **Used in:** S-003, S-004, S-007, S-008, S-013, S-014.

### CMP-032 / CMP-052 Timeline

- **Purpose:** Điểm dừng, lịch sử trạng thái, nhật ký audit.
- **Anatomy:** Marker · đường nối · tiêu đề · thời gian · mô tả · actor.
- **States:** done, current, pending, failed.
- **Usage:** Audit luôn có actor và thời gian; không cho sửa.
- **Used in:** S-004, S-008, S-013, S-014, S-018, S-019, S-021.

### CMP-040 ProofUpload

- **Purpose:** Khách tải chứng từ chuyển khoản; tài xế/Finance Ops xem và xác nhận.
- **Anatomy:** Thumbnail · StatusPill · tên file · số tiền + mã tham chiếu · progress / lý do + action.
- **States:** empty, uploading, failed, submitted, verified, rejected.
- **Usage:** Chỉ hiển thị trong job/case liên quan. Lý do từ chối phải cụ thể.
- **Used in:** S-004, S-007, S-011, S-013, S-014, S-021.

### CMP-022 Banner

- **Purpose:** Thông báo nằm lại: offline, khu vực chưa hỗ trợ, không có quyền, lỗi.
- **Variants:** info, success, warning, danger, offline, locked.
- **Usage:** Tối đa một banner mỗi vùng; action là link chữ. Thông báo tạm dùng Toast.

### CMP-020 Skeleton

- **Purpose:** Giữ chỗ khi tải. Phải cùng kích thước nội dung thật.

### CMP-050 DataTable

- **Purpose:** Bảng admin dày cho tài xế, catalog, khu vực, case, audit.
- **Anatomy:** Header sticky 36px · hàng 44px · checkbox · cột số canh phải mono.
- **States:** default, loading, empty, error, selected, sorted.
- **Usage:** Trạng thái dùng StatusPill `sm`; chi tiết mở Drawer; không đặt card trong hàng.
- **Used in:** S-017, S-019, S-020, S-021.

## 4. Platform notes

- **Customer app:** Bản đồ full-bleed + bottom sheet là bề mặt chính. TabBar 3–4 mục.
- **Driver app (sáng):** Nút Accept/Reject cao 56px, đặt trong bottom action bar; offer hiển thị giá cuối của nền tảng rõ nhất.
- **Admin web:** Sidebar 248px, header 64px, nội dung tối đa 1200px (bảng có thể full-width). Không dùng layout nhiều card trang trí.
