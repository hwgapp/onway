## Nguyên tắc

Đơn sắc là chính: đen, trắng, xám (`ink-*`) mang giao diện. `red-500` (`#E22240`) chỉ dùng cho CTA primary (một nút mỗi màn hình) và logo — không dùng làm màu trang trí. Mỗi màn hình vận hành (chuyến, đơn, chứng từ) đặt một `StatusPill` rõ ràng ở trên cùng để trạng thái đọc được trong một cái liếc. Giữ giao diện gọn và chuyên nghiệp: radius nhỏ (`radius-md` 8px cho control, `radius-card` 12px cho card), gần như không dùng shadow — dùng `border-width-hairline` (`border-default`) để tách lớp thay vì đổ bóng; chỉ nổi shadow khi phần tử thật sự trôi nổi (`shadow-md` cho UI nổi trên bản đồ, `shadow-sheet` cho bottom sheet, `shadow-lg` cho dialog/drawer). Tiếng Việt trước: mọi nhãn viết tiếng Việt tự nhiên, ngắn gọn; kiểm tra dấu và độ dài trước khi khoá UI.

## Màu

Dùng token semantic (`surface-*`, `text-*`, `border-*`, `action-*`) trong component; không hard-code hex và không dùng thẳng ramp (`ink-*`, `red-*`, `green-*`, `blue-*`, `amber-*`, `violet-*`) trừ khi đang định nghĩa một token mới. `surface-page` là nền trang, `surface-card` là nền card/sheet, `text-primary`/`text-secondary`/`text-tertiary` là ba bậc chữ chính. Nền màu semantic (`surface-success-subtle`, `surface-info-subtle`, `surface-warning-subtle`, `surface-accent-subtle`, `surface-danger-subtle`) luôn đi cùng chữ semantic tương ứng (`text-success`, `text-info`, `text-warning`, `text-accent`, `text-danger`) — không phối ngược cặp.

`action-primary-bg` (`red-500`) là nền CTA primary; hover `action-primary-bg-hover` (`red-600`), pressed `action-primary-bg-active` (`red-700`). `action-secondary-bg` (`ink-950`) là hành động phụ mạnh. Trạng thái destructive dùng viền + chữ `border-danger`/`text-danger` (`red-600`), không dùng nền đỏ đặc — destructive luôn xác nhận qua Dialog, không tự thực thi ngay.

Bản đồ dùng riêng nhóm `map-*` (`map-land`, `map-block`, `map-park`, `map-water`, `map-road`, `map-road-major`, `map-route`, `map-pin-pickup`, `map-pin-dropoff`, `map-pin-driver`, `map-region-*`) — không phủ màu semantic UI lên bản đồ. Polygon vùng: `active` = viền `map-region-stroke` nét đứt; `selected` = viền `map-region-selected-stroke` nét liền + `map-region-selected-fill`; `paused` = `map-region-paused-fill`; `invalid`/overlap = `map-region-invalid-fill` nét chấm.

## Tương phản

Giữ mọi cặp chữ-trên-nền tối thiểu 4.5:1 (3:1 cho chữ ≥ 24px hoặc đậm ≥ 19px, và cho mọi viền/focus-ring/icon mang nghĩa), ở cả hai theme. `text-tertiary` không xuống dưới 12px. Không dùng `text-disabled` (`ink-400`/dark `ink-600`) cho chữ cần đọc — chỉ dùng cho trạng thái disabled. Trạng thái không chỉ dựa vào màu: `StatusPill` luôn có màu + hình (chấm/✓/✕/!) + nhãn chữ; lỗi form có viền đỏ + icon + helper text; `Timeline` failed có marker vuông + chữ đỏ, không chỉ đổi màu.

## Typography — Be Vietnam Pro / JetBrains Mono

Dùng `type.groups` theo tên style, không tự đặt size rời: `display-xl/lg/md` cho landing; `heading-xl/lg/md/sm` cho tiêu đề màn và sheet; `body-lg/md/sm` cho nội dung (Admin dùng `body-sm` với hàng bảng cao 44px); `label` cho nhãn nút/form; `caption` cho metadata; `overline` (viết hoa) cho nhóm section admin; `numeric` (JetBrains Mono) cho giá, mã tham chiếu, ETA — định dạng số tiền kiểu `48.000đ`. Line-height không dưới 1.15 để không cắt dấu tiếng Việt (ố, ữ, ặ); nhãn trạng thái và nút phải co giãn hoặc xuống dòng khi cỡ chữ hệ thống lên 200% — không đặt chiều cao cố định cho vùng chứa chữ.

## Spacing & layout

Lưới 4px: `space-1`…`space-32`. Gutter mobile `space-4` (16px), web `layout-gutter` (20px). Control height theo `control-height-sm/md/lg/xl` (32/40/48/56px); touch target tối thiểu `touch-target-min` (44px) trên mọi control tương tác. Nút Accept/Reject của tài xế và xác nhận thanh toán dùng `control-height-xl` (56px), cách nhau ≥ `space-3`, không đặt sát mép home indicator — bottom action bar cộng thêm `env(safe-area-inset-bottom)`. Admin web: sidebar `layout-sidebar-width` (248px), header `layout-header-height` (64px), nội dung tối đa `layout-max-width` (1200px, bảng có thể full-width) — không dùng layout nhiều card trang trí.

## Radius

`radius-control`/`radius-field` (8px) cho control và input; `radius-card` (12px) cho card; `radius-sheet` (20px, chỉ hai góc trên) cho bottom sheet; `radius-xl` (16px) cho dialog; `radius-full` (999px) cho pill/StatusPill.

## Elevation

Viền hairline (`border-width-hairline`, `border-default`) tách lớp là mặc định. Chỉ dùng shadow khi phần tử thật sự nổi: `shadow-md` cho UI nổi trên `MapSurface`, `shadow-sheet` cho bottom sheet, `shadow-lg` cho dialog/drawer, `shadow-xl` chỉ dùng hiếm khi cần nổi cao nhất.

## Motion

Dùng token thời lượng và easing trong code (không có trong `tokens.json` — hệ thống appifact không hỗ trợ họ token chuyển động): `instant` 80ms, `fast` 140ms, `base` 200ms, `slow` 320ms, `sheet` 380ms; easing chuẩn `cubic-bezier(.2,0,0,1)`, `out` `cubic-bezier(.16,1,.3,1)`, `in` `cubic-bezier(.4,0,1,1)`, `spring` `cubic-bezier(.34,1.4,.64,1)` — spring chỉ dùng cho xác nhận đặt chuyến thành công. Nhấn nút scale `.975`. Khi `prefers-reduced-motion: reduce`: tắt pulse `StatusPill`, tắt shimmer `Skeleton`, tắt animation route/matching; Sheet/Dialog chỉ fade ≤140ms, không trượt.

## Icon

Lucide, nét 2px, kích thước 16/20/24px, kế thừa `currentColor`. `IconButton` bắt buộc có `label`/`aria-label` tiếng Việt; icon-only trên web có Tooltip.

## Logo

Nền sáng dùng `logo.svg` (chữ "On" `red-500`, "Way" `ink-800`). Nền đỏ (`red-500`) hoặc than (`ink-950`) dùng `logo-dark.svg` (toàn trắng) — `logo-white.svg` là bản trắng độc lập, `logo-ink.svg` là bản than đơn sắc (in ấn, hoá đơn). `logo-mark.svg`/`logo-mark-white.svg` là mark tròn dùng cho avatar hệ thống, loading, favicon. App icon lấy từ mark (vòng tròn) — `logo-appicon.svg` nền đỏ cho app khách, `logo-appicon-ink.svg` nền than cho app tài xế (phân biệt hai app), `logo-appicon-light.svg` cho favicon/admin. Không vẽ lại, đổi màu, xoay hay thêm hiệu ứng lên logo. Khoảng trống an toàn quanh logo bằng chiều cao chữ "O"; chiều cao tối thiểu 20px.

## StatusPill — 34 trạng thái, 6 tone

Map trạng thái nghiệp vụ backend → tone, không tạo màu trạng thái mới; thêm state mới vào đúng nhóm tone bên dưới, không hard-code màu:

- **info** (`surface-info-subtle` / `text-info`, chấm): requested, searching, matching, accepted, confirmed
- **warning** (`surface-warning-subtle` / `text-warning`, dấu !): arriving, arrived, preparing, atOutlet, pickup, proofPending, changeRequested, pendingReview, unpaid, paused
- **accent** (`surface-accent-subtle` / `text-accent`, chấm): inProgress, delivering, appeal
- **success** (`surface-success-subtle` / `text-success`, dấu ✓): completed, proofVerified, online, approved, active, published
- **danger** (`surface-danger-subtle` / `text-danger`, dấu ✕): proofRejected, disputed, issue, rejected, locked
- **neutral** (`surface-sunken` / `text-secondary`, không hình): cancelled, offline, expired, draft, finalized

Pill `sm` (22px, dùng trong bảng admin) / `md` (26px). Pulse (1.6s) chỉ cho `matching`/`searching`; tắt khi reduced motion. StatusPill không dùng làm filter — dùng `Tag`.

## Theme

Mặc định sáng cho Customer, Driver, Admin. Theme tối (`dark` trong `tokens.json`) để dành cho chế độ ban đêm của Driver App (P1) — chưa dùng ở P0.

## Component inventory

Toàn bộ 47 component (trong 48 CMP-ID của inventory gốc — CMP-032 Timeline và CMP-052 Audit Timeline là cùng một component, chỉ khác việc có truyền `actor` hay không) đã có preview trong hệ thống này, dựng trực tiếp từ `component-inventory.md`, `component-state-matrix.md`, `design-system.md` gốc do người dùng cung cấp (không có mã nguồn React đi kèm, nên đây là bản build lại từ spec, không phải import mã thật):

- **Core UI**: `Logo`, `AppIcon`, `Icon`, `Button`, `IconButton`, `Avatar`, `Card`, `Badge`, `Tag`
- **Navigation**: `TopBar`, `TabBar`, `Tabs`, `SidebarNav`, `ListRow`
- **Form**: `Input`, `Select`, `Checkbox`, `Radio`, `Switch`, `SegmentedControl`
- **Feedback/Overlay**: `Skeleton`, `Toast`, `Banner`, `Dialog`, `Sheet`, `Tooltip`, `EmptyState`, `ProgressBar`
- **Status**: `StatusPill`
- **Map**: `MapSurface`
- **Booking**: `JobStatusHeader`, `Timeline`, `PriceRow`, `QuantityStepper`, `RatingStars`, `StatCard`
- **Domain patterns** (chưa đóng gói thành component riêng trong nguồn gốc — status "Pattern" trong `component-inventory.md`, đã dựng preview ghép từ các component cơ bản đúng công thức nguồn ghi): `JobCard`, `AddressPicker`, `ChatRoom`, `ComplaintForm`, `AdminDrawer`, `RegionEditorToolbar`, `CatalogEditor`, `PolicyConfigForm`, `FilterBar`
- **Admin**: `DataTable`

## Accessibility

Screen reader: `IconButton` luôn có `aria-label` tiếng Việt; bản đồ đặt `aria-hidden`, thông tin chuyến (tài xế, ETA, giá) đặt trong Sheet/`JobStatusHeader`; thay đổi trạng thái chuyến thông báo qua `aria-live="polite"`, lỗi thanh toán dùng `assertive`; `Dialog` bắt buộc focus trap, Esc đóng, trả focus về phần tử đã mở nó. Admin web: mọi hành động đạt được bằng Tab, focus ring 2px trắng + 2px `border-focus`; `DataTable` header sort là `<button>`, checkbox có nhãn; công cụ vẽ polygon (Region Editor) có phím tắt và nút tương đương trên toolbar. Ảnh chứng từ (`ProofUpload`) là private media: signed URL ngắn hạn, không cache public, không hiển thị ngoài job/case liên quan; giữ file cục bộ khi upload lỗi để thử lại không cần chọn lại.

## Not synced

Gói nguồn người dùng cung cấp (`Onway_Design_System.zip`) là tài liệu handoff (token + spec), không kèm mã nguồn component React/CSS thật — mọi component ở trên là bản build lại từ spec chính xác trong `component-state-matrix.md`/`design-system.md`, không phải import mã gốc; 9 component có status "Pattern" trong `component-inventory.md` (`JobCard`, `AddressPicker`, `ChatRoom`, `ComplaintForm`, `AdminDrawer`, `RegionEditorToolbar`, `CatalogEditor`, `PolicyConfigForm`, `FilterBar`) vẫn chỉ là preview ghép từ các component cơ bản theo đúng công thức nguồn ghi — chưa phải component đóng gói riêng, khớp với chính trạng thái "Pattern" của nguồn. Font file `Be Vietnam Pro` và `JetBrains Mono` không có trong gói — cả hai đều là Google Fonts, nạp qua `type.families`, không cần file. Token thời lượng/easing (`motion.*`) và chiều cao sheet `76vh` không đưa vào `tokens.json` vì hệ token của appifact chỉ nhận độ dài `px/rem/em/%` và không có họ token chuyển động — đã ghi lại nguyên văn trong mục Motion ở trên. `z-index`, `breakpoint` đã chuyển thành token (`z-*`, `breakpoint-*`); riêng ký tự gạch ngang dài (–) trong breakpoint gốc đổi thành giá trị max/min-width dạng số.

## Đã chỉnh sửa tương phản so với nguồn

Hai cặp màu chữ trong nguồn không đạt AA (4.5:1) khi đo chính xác, dù tài liệu gốc ghi là đạt — đã chỉnh lại, không giữ nguyên giá trị nguồn:

- `text-warning` (nền `surface-warning-subtle`): `amber-600` `#B87F22` chỉ đạt 3.21:1. Thêm token `amber-700` `#8E621A` (đậm hơn, cùng tông) và đổi `text-warning` sang alias token này ở theme sáng — đạt 5:1.
- `text-tertiary` (trên `surface-card`): nguồn dùng `ink-500` cho cả hai theme — 4.47:1 ở theme sáng, 3.85:1 ở theme tối (dưới ngưỡng cả hai). Theme sáng chỉnh còn `#6F6E6D` (đạt 5.1:1, gần như không đổi thị giác so với `ink-500`); theme tối alias sang `ink-400` (đạt 6.7:1).
- `RatingStars`: sao đã chọn dùng `amber-500` trực tiếp làm màu glyph — chỉ đạt 2.2:1 trên nền trắng (dưới cả ngưỡng 3:1 cho đối tượng đồ hoạ không phải chữ). Đổi sang `amber-700` — đạt 5.4:1.

Đã rà lại toàn bộ token `text-*` so với mọi nền `surface-*` (page/card/raised/hover/active/sunken) ở cả hai theme; các cặp còn dưới 4.5:1 (`text-disabled`, `text-inverse`, `text-inverse-secondary`, và vài cặp cận biên như `text-tertiary`/`text-secondary` trên `surface-active`) không dùng chung với nhau trong bất kỳ component nào ở đây — `text-disabled`/`text-inverse*` có nền riêng theo đúng thiết kế, còn các cặp cận biên kia không xuất hiện trong component nào đã build.

---
