# Implementation Notes

## Nguồn sự thật

- Token: `tokens.json` (sinh từ CSS custom properties của design system). Khi lệch, CSS thắng.
- Tên token giữ nguyên giữa web và mobile: `color.surface.card` ↔ `--surface-card` ↔ `Colors.surfaceCard`.
- Không hard-code hex trong component; luôn qua token semantic (`surface-*`, `text-*`, `border-*`, `action-*`), không qua ramp (`ink-*`, `red-*`) trừ khi định nghĩa token mới.

## Theme

- Mặc định sáng cho Customer, Driver, Admin.
- `[data-theme="dark"]` override 44 token semantic — để dành chế độ ban đêm Driver App (P1).

## Map (HERE)

- Placeholder `MapSurface` chỉ dùng cho mockup.
- Production: cấu hình HERE map style theo `tokens.json › map` (land, block, park, water, road, road-major, label). Route, pin và polygon vẽ bằng layer overlay của app, dùng token `map.route*`, `map.pin*`, `map.region*`.
- Polygon S-017: active = nét đứt than; selected = nét liền đỏ + fill đỏ 10%; paused = cam; invalid/overlap = đỏ chấm + fill đỏ 16%. Không xoá cứng polygon (P0).

## Thanh toán & chứng từ

- Ảnh chứng từ là private media: signed URL ngắn hạn, không cache public, không hiển thị ngoài job/case.
- `ProofUpload` giữ file cục bộ khi upload lỗi để thử lại không cần chọn lại.

## Status

- Map trạng thái backend → key `StatusPill` (xem `tokens.json › status`). Không tạo màu trạng thái mới; thêm key vào đúng nhóm tone.

## Thứ tự task đề xuất (DS trước UI)

| # | Task | Phụ thuộc |
| --- | --- | --- |
| DS-01 | Token package (web CSS vars + mobile theme) | — |
| DS-02 | Font + icon setup (Be Vietnam Pro, JetBrains Mono, Lucide) | DS-01 |
| DS-03 | Core: Button, IconButton, Icon, Card, Badge, Tag, Avatar | DS-01, DS-02 |
| DS-04 | Form: Input, Select, Checkbox, Radio, Switch, SegmentedControl | DS-03 |
| DS-05 | Navigation: TopBar, TabBar, Tabs, SidebarNav, ListRow | DS-03 |
| DS-06 | Feedback/overlay: Toast, Banner, Skeleton, EmptyState, Dialog, Sheet, Tooltip, ProgressBar | DS-03 |
| DS-07 | StatusPill + JobStatusHeader + Timeline | DS-03 |
| DS-08 | MapSurface/HERE style + pins + polygon layer | DS-01 |
| DS-09 | ProofUpload + private media | DS-06, DS-07 |
| DS-10 | DataTable + FilterBar + Admin Drawer | DS-04, DS-06 |
| DS-11 | Pattern còn thiếu: Address Picker, Chat Room, Complaint Form, Region Editor Toolbar, Catalog Editor, Policy Config Form | DS-04…DS-10 |

UI task của từng screen (S-001…S-021) phụ thuộc DS task tương ứng trong `component-inventory.md › Used In Screens`.

## Design Fix List

| ID | Package | Issue | Impact | Needed Before | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| DF-001 | Design System | CMP-042 Chat Room chưa đóng gói component | S-015 thiếu spec state retention/upload failed | UI task S-015 | Design | Open |
| DF-002 | Design System | CMP-051 Admin Drawer chưa có component | S-019/S-020/S-021 detail panel | UI task admin | Design | Open |
| DF-003 | Design System | CMP-053 Region Editor Toolbar chưa có component | S-017 | UI task S-017 | Design | Open |
| DF-004 | Design System | CMP-041 Address Picker chưa đóng gói | S-002, S-006 | UI task S-002 | Design | Open |
| DF-005 | UI Workflow | Chưa có mockup theo Screen ID | Không break được UI task | UI task breakdown | Design | Open |
