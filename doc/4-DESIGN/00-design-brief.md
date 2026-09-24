# Design Brief

## Product

Onway là marketplace Ride Hailing + Food Delivery cho Việt Nam, định vị 0% commission, money-light và minh bạch giá. P0 gồm Customer App, Driver App, Admin Portal, Web/Landing và Backend/API.

## Audience

- Customer ban đầu: nhân viên văn phòng và sinh viên.
- Driver: tài xế xe máy/ô tô nhận Ride/Food job, cần thao tác nhanh, rõ trạng thái và ít nhầm lẫn.
- Admin/Operator: đội vận hành quản lý region, driver, catalog, pricing/policy, complaint/fraud và audit.

## Style Direction

- Hiện đại, rõ ràng, tốc độ cao, đáng tin cậy.
- Mobile-first cho Customer/Driver; Admin Portal ưu tiên scan nhanh, bảng dữ liệu, trạng thái và hành động vận hành.
- Không dùng phong cách quá vui nhộn/game hóa cho P0; thương hiệu cần cảm giác năng động nhưng vẫn chắc chắn vì liên quan di chuyển, thanh toán trực tiếp và tranh chấp.
- Giao diện phải hỗ trợ bản đồ, trạng thái job/order, payment proof, chat/call, complaint và admin review evidence.

## Brand Assets

| Asset | Path | Notes |
| --- | --- | --- |
| Onway logo SVG | `/Users/vod/Documents/ONW/design/logo.svg` | Vector source, 4493 x 1300 viewBox, transparent background |
| Onway logo PNG | `/Users/vod/Documents/ONW/design/logo.png` | PNG source, 4493 x 1300, RGBA |

Logo wordmark: `OnWay`/`Onway` visual lockup with red `On` and charcoal `Way`. SVG colors:

- Brand red: `#E22240`
- Brand charcoal 1: `#302F2F`
- Brand charcoal 2: `#2F2E2E`
- Background: transparent

Design handoff must preserve logo proportions, clear space and contrast. Do not redraw the logo manually if the SVG asset can be used.

## Reference Apps / Screens

- Ride hailing: Grab, Be, Gojek for map/job lifecycle patterns only.
- Food delivery: ShopeeFood/GrabFood for browse/cart/order tracking patterns only.
- Admin/Ops: quiet SaaS operations UI with dense tables, filters, drawers, timelines and audit trails.

## Must Avoid

- Không dùng màu đỏ cho mọi thứ; red là brand/accent/primary có kiểm soát, danger/error cần phân biệt rõ bằng tone/label/icon.
- Không làm UI marketing quá bóng bẩy cho admin; admin cần utilitarian, dense và dễ scan.
- Không thêm business flow ngoài BRD/PRD: không wallet, COD, cash, gateway, Ride negotiation/customer manual offer, Food negotiation, Trust full, Mission, Ads trong P0. Driver app hiển thị final platform price để Accept/Reject.
- Không dùng logo bị méo, crop, thiếu clear space hoặc đặt trên nền làm mất contrast.
- Không dùng app icon chỉ là wordmark dài; cần biến thể symbol/icon phù hợp kích thước nhỏ.
