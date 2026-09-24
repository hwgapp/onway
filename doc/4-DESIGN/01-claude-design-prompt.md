# Claude Design Prompt

> Copy prompt này sang Claude Design sau khi BRD/PRD đủ rõ.

```text
Bạn là product designer. Hãy thiết kế design system và UI flows cho dự án sau.

Product summary:
- Onway là marketplace Ride Hailing + Food Delivery cho Việt Nam, P0 gồm Customer App, Driver App, Admin Portal và Landing Web.
- Định vị: 0% commission, money-light, minh bạch giá, customer trả trực tiếp cho driver bằng bank transfer/QR và upload payment proof.
- P0 không có Ride negotiation/customer manual offer; customer dùng giá platform đề xuất, driver thấy final platform price để Accept/Reject.
- P0 không có wallet, COD/cash, payment gateway, Food delivery fee negotiation, Trust full, Mission, Ads hoặc Merchant App bắt buộc.

Audience:
- Customer ban đầu: nhân viên văn phòng và sinh viên.
- Driver: tài xế xe máy/ô tô, cần nhận job nhanh, xem trạng thái rõ, chat/gọi, xem payment proof và xác nhận đã nhận tiền.
- Admin/Operator: đội vận hành quản lý region, driver, catalog, pricing/policy, complaint/fraud, evidence và audit.

Platforms:
- iOS/Android Customer App.
- iOS/Android Driver App.
- Web Admin Portal.
- Landing Web.

Brand assets:
- Logo SVG: `/Users/vod/Documents/ONW/design/logo.svg`
- Logo PNG: `/Users/vod/Documents/ONW/design/logo.png`
- Logo source dimensions: SVG/PNG 4493 x 1300.
- Brand red: `#E22240`.
- Brand charcoal: `#302F2F` / `#2F2E2E`.
- Logo background: transparent.
- Preserve logo proportions and clear space. Do not redraw the logo manually if SVG can be used.
- Provide required logo variants: full wordmark, compact/symbol app icon candidate, light/dark background usage, monochrome/fallback usage if needed.

Required outputs:
1. Design system đầy đủ:
   - Design tokens
   - Typography
   - Color system
   - Spacing/radius/motion
   - Icon/asset guidance
   - Component library với variants/states
   - Component catalog theo `doc/4-DESIGN/06-design-system-component-catalog.md`
2. UI workflow của tất cả màn hình:
   - Tất cả screen trong `doc/2-PRD/02-screen-inventory.md`
   - Flow navigation giữa màn hình
   - State variants: loading/empty/error/offline/no-permission/paywall/success
   - Responsive/device variants nếu platform cần
3. Component inventory map component -> screen.
4. Mockup/frame export map frame name -> Screen ID.
5. Design handoff notes để code implementation.
6. Output theo contract trong `doc/4-DESIGN/07-claude-design-output-contract.md`.

Rules:
- Theo BRD/PRD đã chốt.
- Không tự thêm business flow ngoài scope.
- Không thay đổi logo source hoặc brand colors nếu không nêu rõ là proposal.
- Mọi màn hình cần loading/empty/error/offline/no-permission/paywall nếu phù hợp.
- Xuất mockup/frame name khớp `doc/2-PRD/02-screen-inventory.md`.
- Phân biệt rõ phần design system và phần UI workflow/screens.
- Với mỗi component, mô tả anatomy, variants, states, usage rules và screen usage.
- Cung cấp screen-map, flow-map và state-coverage để Codex import ngược vào SDLC.
```
