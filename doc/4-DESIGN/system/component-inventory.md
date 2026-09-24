# Component Inventory

Status: **Built** = có component React + spec trong design system. **Pattern** = ghép từ component đã có, chưa đóng gói thành component riêng — cần làm trước UI Workflow.

| Component ID | Component | Category | Priority | Platforms | Used In Screens | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CMP-001 | Logo | Brand | P0 | iOS/Android/Web | Splash, S-001, S-016 sidebar, landing | Built. `assets/logo*.svg` |
| CMP-002 | App Icon / Favicon | Brand | P0 | iOS/Android/Web | Launcher, store, browser | Built (asset). Từ mark, không dùng wordmark |
| CMP-003 | Button | Core UI | P0 | iOS/Android/Web | Tất cả | Built. primary/secondary/outline/ghost/destructive |
| CMP-004 | IconButton | Core UI | P0 | iOS/Android/Web | Tất cả | Built. Bắt buộc `label` |
| CMP-005 | Icon | Core UI | P0 | iOS/Android/Web | Tất cả | Built. Lucide |
| CMP-006 | Card | Core UI | P0 | iOS/Android/Web | S-001, S-005, S-012, S-016 | Built. Không lồng card |
| CMP-007 | Badge | Core UI | P0 | iOS/Android/Web | TabBar, SidebarNav | Built. Đếm số |
| CMP-008 | Tag / Chip | Core UI | P0 | iOS/Android/Web | S-005 filter, S-009 quick tags, admin filter | Built |
| CMP-009 | Avatar | Core UI | P0 | iOS/Android/Web | S-004, S-008, S-013, S-019 | Built |
| CMP-010 | TopBar | Navigation | P0 | iOS/Android | Tất cả màn mobile | Built |
| CMP-011 | TabBar (bottom nav) | Navigation | P0 | iOS/Android | S-001, S-012 | Built |
| CMP-012 | Tabs | Navigation | P0 | iOS/Android/Web | S-005, S-019, S-021 | Built |
| CMP-013 | StatusPill | Status | P0 | iOS/Android/Web | S-003…S-021 | Built. 34 trạng thái, màu + hình + chữ |
| CMP-014 | SidebarNav | Navigation | P0 | Web | S-016…S-021 | Built |
| CMP-015 | ListRow | Core UI | P0 | iOS/Android/Web | Settings, S-002 địa chỉ, S-015 | Built |
| CMP-016 | Input | Form | P0 | iOS/Android/Web | S-002, S-009, S-010, S-018 | Built. text/search/multiline |
| CMP-017 | Select | Form | P0 | Web | S-018, S-019, S-020 | Built |
| CMP-018 | Checkbox | Form | P0 | iOS/Android/Web | S-010, bảng admin | Built |
| CMP-019 | Radio | Form | P0 | iOS/Android/Web | S-002 loại xe, S-009 lý do | Built |
| CMP-020 | Skeleton | Feedback | P0 | iOS/Android/Web | Mọi state loading | Built |
| CMP-021 | Switch | Form | P0 | iOS/Android/Web | S-012 online, S-018 | Built |
| CMP-022 | Banner | Feedback | P0 | iOS/Android/Web | Offline, region unavailable, no permission, proof rejected | Built |
| CMP-023 | SegmentedControl | Form | P0 | iOS/Android/Web | S-001 Ride/Food, S-016 | Built |
| CMP-024 | Toast | Feedback | P0 | iOS/Android/Web | Tất cả | Built |
| CMP-025 | Dialog | Overlay | P0 | iOS/Android/Web | Huỷ chuyến, khoá tài xế, publish polygon | Built. Hành động nhạy cảm phải có lý do |
| CMP-026 | Sheet (bottom sheet) | Overlay | P0 | iOS/Android | S-002…S-008, S-013, S-014 | Built |
| CMP-027 | Tooltip | Overlay | P0 | Web | Icon-only actions admin | Built |
| CMP-028 | EmptyState | Feedback | P0 | iOS/Android/Web | S-005, S-012, S-016…S-021 | Built. Cũng dùng cho error/no-permission toàn màn |
| CMP-029 | ProgressBar | Feedback | P0 | iOS/Android/Web | S-010 onboarding | Built. bar + steps |
| CMP-030 | MapSurface | Map | P0 | iOS/Android/Web | S-002…S-004, S-007, S-008, S-012…S-014, S-017 | Built. HERE-style placeholder |
| CMP-031 | JobStatusHeader | Booking | P0 | iOS/Android | S-003, S-004, S-007, S-008, S-013, S-014 | Built |
| CMP-032 | Timeline (Route/Stop) | Booking | P0 | iOS/Android/Web | S-004, S-008, S-013, S-014 | Built |
| CMP-033 | PriceRow | Commerce | P0 | iOS/Android/Web | S-002, S-006, S-011 | Built. Dòng 0% hoa hồng |
| CMP-034 | QuantityStepper | Commerce | P0 | iOS/Android | S-006 | Built |
| CMP-035 | RatingStars | Feedback | P0 | iOS/Android/Web | S-009, S-005, S-019 | Built |
| CMP-036 | StatCard | Data | P0 | Web | S-016 | Built |
| CMP-037 | Job / Order Card | Booking | P0 | iOS/Android/Web | S-012, S-013, S-014, S-016 | Pattern. Card + StatusPill + PriceRow |
| CMP-040 | ProofUpload | Upload/Evidence | P0 | iOS/Android/Web | S-004, S-007, S-011, S-013, S-014, S-021 | Built |
| CMP-041 | Address Picker | Map | P0 | iOS/Android | S-002, S-006 | Pattern. Input search + ListRow + Banner no-permission |
| CMP-042 | Chat / Message Room | Communication | P0 | iOS/Android/Web | S-015, S-021 | Pattern. Chưa đóng gói; cần state retention expired, upload failed |
| CMP-043 | Complaint / Case Form | Form | P0 | iOS/Android | S-009 | Pattern. Radio + Input + ProofUpload |
| CMP-050 | DataTable | Admin | P0 | Web | S-019, S-020, S-021, S-017 list | Built |
| CMP-051 | Admin Drawer / Detail Panel | Admin | P0 | Web | S-019, S-020, S-021 | Pattern. Sheet side variant cần build |
| CMP-052 | Audit Timeline | Admin | P0 | Web | S-018, S-019, S-021 | Built (Timeline với `actor`) |
| CMP-053 | Region Editor Toolbar | Map/Admin | P0 | Web | S-017 | Pattern. MapSurface region + toolbar IconButton |
| CMP-054 | Catalog Editor | CMS | P0 | Web | S-020 | Pattern. Tabs + DataTable + Input + draft/publish StatusPill |
| CMP-055 | Policy Config Form | Admin | P0 | Web | S-018 | Pattern. Input/Select + Dialog lý do + Audit Timeline |
| CMP-056 | Filter Bar | Admin | P0 | Web | S-019, S-020, S-021 | Pattern. Input search + Tag + Select |

## Asset

| Asset ID | Asset Name | Type | Used In | Required Format | Notes |
| --- | --- | --- | --- | --- | --- |
| AST-001 | Logo lockup (nền sáng) | logo | Header web, admin login, landing | svg | `logo.svg` — On `#E22240`, Way `#2F2E2E` |
| AST-002 | Logo trắng (nền đỏ/than) | logo | Splash, footer, hero tối | svg | `logo-dark.svg` / `logo-white.svg` |
| AST-003 | Logo đơn sắc than | logo | In ấn, hoá đơn | svg | `logo-ink.svg` |
| AST-004 | Mark | logo | Avatar hệ thống, loading, favicon | svg | `logo-mark.svg`, `logo-mark-white.svg` |
| AST-005 | App Icon Customer | icon | Launcher, store | svg → png 1024 | `logo-appicon.svg` (nền đỏ) |
| AST-006 | App Icon Driver | icon | Launcher, store | svg → png 1024 | `logo-appicon-ink.svg` (nền than) — đề xuất để phân biệt với app khách |
| AST-007 | Favicon / Admin | icon | Browser | svg, png 32/180 | `logo-appicon-light.svg` |
| AST-008 | Map tiles | map | Mọi màn có bản đồ | HERE tile style | Placeholder; production cấu hình HERE style theo `tokens.json › map` |
