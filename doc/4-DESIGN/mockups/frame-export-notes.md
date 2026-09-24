# Frame Export Notes

## Nguồn

- Canvas “Customer & Driver”: [https://claude.ai/artifact/4cHL1pqQYuNLWsi2m2H44Y](https://claude.ai/artifact/4cHL1pqQYuNLWsi2m2H44Y) — trang `Tổng quan`, `Customer App`, `Driver App`.
- Canvas “Admin & Landing”: [https://claude.ai/artifact/CxkTKZioRmXx1xWKrzYf79](https://claude.ai/artifact/CxkTKZioRmXx1xWKrzYf79) — trang `Tổng quan`, `Admin Portal`, `Landing Web`.
- Tách hai canvas vì trình canvas chỉ tải tối đa 200 file mỗi canvas. Cả hai là artifact riêng tư, cần chia sẻ từ menu Share của trang.
- Design system: Onway (`claude.ai/code/artifact/3a7f770f-…`), đã cài vào canvas tại `project/ds/onway/tokens.json` để Theme menu dùng đúng màu/chữ.
- Nguồn sinh frame (Python, dựng từ token): `raw/generator/`. Chạy `python3 build.py` trong thư mục đó để sinh lại `canvas/project/*.dc.html`.

## Quy ước

| Mục | Giá trị |
| --- | --- |
| Tên artboard | `<Frame ID> - <Frame Name> - <Platform>`; file `<Frame ID>.dc.html` |
| Tên trạng thái | nhãn phía trên mỗi màn trong artboard → export `<Frame ID> - <Frame Name> - <State> - <Platform>` |
| Mobile | 390×844 (iPhone), vùng an toàn trên 44px, dưới 34px; không vẽ status bar giả |
| Admin | 1440×900, sidebar 248px, header 64px |
| Landing | 1440 rộng (chiều cao theo section); L-001 có thêm bản mobile 390×900 |
| Ngôn ngữ | Tiếng Việt; tiền tệ dạng `48.000đ` (JetBrains Mono) |
| Theme | Sáng cho cả 3 app (theme tối Driver là P1) |
| Prototype | 216 artboard; CTA chính dùng link Play sang frame kế tiếp |

## Tài sản dùng

| Asset ID | Asset Name | Type | Used In | Required Format | Notes |
| --- | --- | --- | --- | --- | --- |
| AST-001 | Logo Onway | svg | Admin sidebar, login, landing, splash | svg | `system/assets/logo.svg`, bản trắng `logo-white.svg` trên nền đỏ/than |
| AST-002 | App icon khách | svg | C-001, L-006 | svg/png | `logo-appicon.svg` nền đỏ |
| AST-003 | App icon tài xế | svg | D-001 | svg/png | `logo-appicon-ink.svg` nền than |
| AST-004 | Logo mark | svg | Admin thu gọn, bìa | svg | `logo-mark.svg` |
| AST-005 | Ảnh món/quán | placeholder | C-033…C-039, A-040…A-046 | jpg/webp | Khối màu + icon; cần ảnh thật từ catalog |
| AST-006 | Ảnh chứng từ/giấy tờ | placeholder | C-025, D-023, A-031, A-052… | — | Placeholder có nhãn; dữ liệu thật là private media |
| AST-007 | Bản đồ | placeholder | màn có bản đồ | — | SVG minh hoạ theo token `map-*`; thực tế là HERE Maps |

## Known gaps / Design fix list

| ID | Package | Issue | Impact | Needed Before | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| DF-001 | UI Workflow | Component được vẽ bằng markup theo token, chưa mount component bundle thật (README design system không công bố bundle global) | Dev dùng spec component trong `system/` làm chuẩn, mockup chỉ tham chiếu thị giác | UI implementation | Design | Open |
| DF-002 | UI Workflow | Bản đồ, ảnh món, ảnh chứng từ là placeholder | Không ảnh hưởng logic; cần asset thật khi QA hình ảnh | G8 | Design/Ops | Open |
| DF-003 | UI Workflow | Số liệu mẫu (giá/km, phí giao, wave, ngưỡng khoá) trong A-023…A-026 là ví dụ minh hoạ | Không dùng làm cấu hình thật | Cấu hình rollout | Ops/User | Open — OQ-025 |
| DF-004 | UI Workflow | Nội dung pháp lý L-009/L-010, thông tin doanh nghiệp ở footer là placeholder `[…]` | Cần legal review | Ra mắt | Legal | Open |
| DF-005 | UI Workflow | Thời gian tài xế chờ ở điểm đón (vẽ 5 phút, không phí chờ) chưa có trong BRD/PRD | Ảnh hưởng C-029, D-025, D-026, A-023 | Ride PRD detail | User | Open — OQ-022 |
| DF-006 | UI Workflow | Kết quả sau khi khách từ chối / hết giờ đề xuất Food (huỷ hay giao phần còn lại, ai hoàn tiền) vẽ theo hướng “Onway xem xét” | Ảnh hưởng C-047, C-049, D-038 | Food dispute policy | User/Legal | Open — OQ-023 |
| DF-007 | UI Workflow | Cho phép khách ẩn số điện thoại với tài xế (C-010, D-057 “Không khả dụng”) | BR-COMM-001 nói hai bên gọi số thật | PRD chi tiết | User | Open — OQ-024 |
| DF-008 | UI Workflow | Chưa có theme tối (Driver P1) và chưa vẽ trạng thái chữ 200% | Accessibility QA | G6 | Design | Deferred |
