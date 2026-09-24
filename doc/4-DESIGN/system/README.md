# Onway — Design System Package

Package theo `doc/4-DESIGN/07-claude-design-output-contract.md` §2. Copy nguyên thư mục này vào `doc/4-DESIGN/system/` trong repo `hwgapp/onway`.

| File | Nội dung |
| --- | --- |
| `tokens.json` | Toàn bộ token: color, typography, spacing, radius, border, shadow, motion, zIndex, breakpoint, map, status, asset |
| `design-system.md` | Nguyên tắc, foundation và spec từng component P0 |
| `component-inventory.md` | Danh sách CMP-ID, priority, platform, screen sử dụng, trạng thái build |
| `component-state-matrix.md` | Variant × state × hành vi × accessibility |
| `accessibility.md` | Contrast, touch target, dynamic type, reduced motion, screen reader |
| `implementation-notes.md` | Hướng dẫn Codex: mapping token → code, thứ tự task, dependency |
| `assets/` | Logo SVG chính thức, mark, app icon |

## Trạng thái handoff

| Package | Status | Source Artifact | Imported To | Notes |
| --- | --- | --- | --- | --- |
| Design System | Ready for import | Claude Design project "Onway Design System" (2026-09-24) | `system/` | 37 component đã build; 9 component P0 còn ở dạng pattern, xem inventory |
| UI Workflow | Pending | — | `mockups/` | Làm sau khi Design System được duyệt |

## Quyết định đã chốt

- Chỉ hai màu thương hiệu: đỏ `#E22240`, than `#2F2E2E`. Mã `#302F2F` trong tài liệu cũ được thay bằng `#2F2E2E`.
- Đen–trắng–xám là chủ đạo; đỏ chỉ dùng cho CTA chính (một nút mỗi màn hình) và logo.
- Font: Be Vietnam Pro (UI), JetBrains Mono (số, mã tham chiếu).
- Driver App dùng theme sáng cho P0. Theme tối vẫn có token (`[data-theme="dark"]`) cho chế độ ban đêm sau này.
- Merchant App không nằm trong P0, đã loại khỏi design system.
- Bản đồ: placeholder theo style HERE Maps vẽ bằng token `map.*`; production thay bằng HERE tile layer và giữ nguyên token màu.
