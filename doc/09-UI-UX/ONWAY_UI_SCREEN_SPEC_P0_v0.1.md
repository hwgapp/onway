# ONWAY - UI Screen Spec P0

**Loai tai lieu:** UI Screen Spec / Design System Intake  
**Phien ban:** 0.1  
**Trang thai:** Draft, cho reference UI tu founder  
**Ngay cap nhat:** 11/09/2026  
**Muc tieu:** Dinh nghia man hinh toi thieu, state, action, data contract va tieu chuan UI de team co the code tung flow theo sprint ma khong lac scope  

---

# 1. Nguyen tac tai lieu

Tai lieu nay khong chot visual style cuoi cung. Visual direction, color, typography, component feel va motion se chot sau khi founder dua mau/reference.

Tai lieu nay chot cac diem sau:

- Moi app can co nhung man hinh nao trong P0.
- Moi man hinh can doc/ghi du lieu gi.
- Moi man hinh co action nao, state nao, validation nao.
- UI phai hien thi dung cac quyet dinh san pham da chot:
  - Khong COD.
  - Khong tien mat.
  - Khong payment gateway.
  - Chi bank transfer/QR truc tiep customer -> driver.
  - Bat buoc co payment proof.
  - Food khong thoa thuan phi giao hang.
  - Driver khong quan ly nha hang/menu trong P0.
  - Food catalog do admin quan tri truoc.
  - Chat giua customer va driver co text + image.
  - Chat retention 1 tuan.
  - Driver bi auto-lock sau 2 khieu nai qualifying paid/no-show dang mo.

# 2. UI source priority

Khi code UI, doc theo thu tu:

1. `doc/09-UI-UX/ONWAY_UI_SCREEN_SPEC_P0_v0.1.md`
2. `doc/08-Implementation/ONWAY_IMPLEMENTATION_BACKLOG_P0_v0.1.md`
3. `doc/06-API/ONWAY_GRAPHQL_API_CONTRACT_P0_v0.1.md`
4. `doc/07-Realtime/ONWAY_REALTIME_EVENT_CONTRACT_P0_v0.1.md`
5. `doc/05-Logic/ONWAY_LOGIC_P0_v0.1.md`
6. Relevant PRD under `doc/02-PRD/*/*.md`

Neu UI reference sau nay mau thuan voi product/logic/API, product/logic/API thang. Visual co the doi, business rule khong duoc tu y doi.

# 3. Design-system intake checklist

Founder can cung cap cac input nay truoc khi chot design system:

| Nhom | Can co | Vi du |
|---|---|---|
| Brand | Logo, mau brand, tone of voice | Tre trung, tin cay, dia phuong, nhanh gon |
| Reference app | App/web ban thich va khong thich | Grab, Be, Gojek, ShopeeFood, Lalamove |
| Admin reference | UI dashboard/ops mong muon | Linear, Retool, Base, Ant Design, custom ops console |
| Mobile style | Map-first hay list-first | Ride home uu tien ban do, Food uu tien danh sach |
| Visual density | Thoang hay dam dac | Admin can scan nhanh, mobile can ro rang |
| Component feel | Roundness, shadow, border, icon style | shadcn/ui strict hay custom hon |
| Motion | It animation hay co transition nhieu | Matching/offers co countdown, status timeline |
| Content language | VI only hay VI/EN | MVP nen VI first |
| Accessibility | Font size toi thieu, contrast | Mobile ngoai duong, tai xe xem nhanh |

# 4. Provisional design-system contract

Chua chot gia tri token cu the. Khi co reference, can chot cac token sau:

## 4.1 Color tokens

- `color.bg.default`
- `color.bg.subtle`
- `color.surface.default`
- `color.surface.raised`
- `color.text.primary`
- `color.text.secondary`
- `color.text.muted`
- `color.border.default`
- `color.action.primary`
- `color.action.secondary`
- `color.status.success`
- `color.status.warning`
- `color.status.danger`
- `color.status.info`
- `color.map.route`
- `color.map.pickup`
- `color.map.dropoff`

## 4.2 Type tokens

- `font.family.base`
- `font.family.numeric`
- `type.mobile.title`
- `type.mobile.body`
- `type.mobile.caption`
- `type.admin.pageTitle`
- `type.admin.sectionTitle`
- `type.admin.tableCell`
- `type.admin.formLabel`

## 4.3 Layout tokens

- `space.1` to `space.8`
- `radius.control`
- `radius.card`
- `radius.sheet`
- `height.button.mobile`
- `height.button.admin`
- `height.input.mobile`
- `height.input.admin`
- `width.admin.sidebar`
- `z.modal`
- `z.toast`
- `z.bottomSheet`

## 4.4 Motion tokens

- `motion.fast`
- `motion.normal`
- `motion.slow`
- `motion.ease.standard`
- `motion.ease.exit`

# 5. Shared UI rules

## 5.1 Business-rule display rules

- UI khong hien COD/cash/payment gateway trong P0.
- UI khong hien wallet balance/escrow.
- Food checkout khong cho customer nhap delivery fee.
- Food driver offer chi co accept/reject, khong co negotiate fee.
- Payment screen phai co:
  - driver bank account/QR
  - amount
  - transfer content if configured
  - upload proof action
  - proof status
- Driver active job screen phai block buoc mua mon Food neu order yeu cau proof va proof chua duoc chap nhan.
- Account locked state phai hien thi ro ly do va next step.

## 5.2 Client-side logic rules

- Client khong tu quyet dinh business permission.
- Client chi render theo `allowedActions` tu API.
- Moi mutation can handle:
  - loading
  - success
  - validation error
  - permission error
  - stale state error
  - network error
- Realtime event chi cap nhat UI nhanh. Neu mat event/sequence gap thi refetch GraphQL.

## 5.3 Core states moi man hinh can co

- Loading state.
- Empty state.
- Error state.
- Permission denied state.
- Offline/reconnecting state.
- Region unavailable state if location-sensitive.
- Locked/restricted account state if actor-sensitive.
- Mutation pending state.
- Stale state recovery state.

# 6. Route and screen ID convention

Screen ID format:

```txt
<APP>-<DOMAIN>-<NUMBER>
```

App prefixes:

- `ADM`: Web Admin Portal.
- `CUS`: Customer App.
- `DRV`: Driver App.
- `LND`: Landing Web.
- `MRC`: Merchant App future.

Priority:

- `P0`: must build for launch path.
- `P1`: useful shortly after launch.
- `P2`: post-launch/future.

# 7. Admin Portal P0 screen inventory

Admin portal target: desktop-first operations tool. UI should be dense, scan-friendly, table/detail driven, with strong filters, status badges, audit trail, and cautious destructive actions.

## 7.1 ADM-AUTH-001 Login

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/login` |
| Actor | Admin |
| Goal | Admin dang nhap vao portal |
| Query | `me` after auth |
| Mutation | Firebase/admin auth integration TBD |
| Realtime | none |
| Primary actions | Login, logout |
| Empty/loading/error | Loading session, invalid credential, unauthorized |
| Acceptance | Non-admin bi chan khoi admin routes |

## 7.2 ADM-DASH-001 Operations Dashboard

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/` |
| Actor | Admin/Ops |
| Goal | Xem tinh trang van hanh nhanh |
| Query | dashboard summary query TBD |
| Realtime | Admin monitoring events |
| Data | active rides, active food orders, pending driver reviews, pending payment proofs, open complaints, locked drivers |
| Primary actions | Navigate to queue/detail |
| States | Normal, degraded realtime, no active work |
| Acceptance | Admin thay duoc cac queue can xu ly trong 1 man hinh |

## 7.3 ADM-REGION-001 Region Management

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/regions` |
| Actor | Admin |
| Goal | Quan ly region, currency va service availability |
| Query | `adminRegions`, `regionPolicyConfigs` |
| Mutation | create/update region, service availability, currency |
| Data | polygon, currency, service flags, status |
| Primary actions | Create region, edit polygon/status, enable Ride/Food |
| Validation | Currency bat buoc theo region, polygon hop le |
| Acceptance | Khu vuc ngoai polygon khong duoc tao order/ride |

## 7.4 ADM-POLICY-001 Policy Config

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/policies` |
| Actor | Admin |
| Goal | Quan ly policy/runtime config khong can deploy code |
| Query | `adminPolicyConfigs` |
| Mutation | update policy config |
| Data | matching timeout, radius, fee policy, retention, complaint threshold |
| Primary actions | Edit, publish, rollback version |
| Validation | Type/range check theo policy key |
| Acceptance | Business logic doc policy tu server, khong hardcode client |

## 7.5 ADM-DRIVER-001 Driver Queue

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/drivers` |
| Actor | Admin/Ops |
| Goal | Tim, loc, review tai xe |
| Query | `adminDrivers` |
| Mutation | none on list |
| Data | status, onboarding state, vehicle state, payment account state, risk state, online state |
| Primary actions | Filter, search, open detail |
| States | Empty, loading, filter no result |
| Acceptance | Admin loc duoc driver pending/locked/active |

## 7.6 ADM-DRIVER-002 Driver Detail and Review

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/drivers/:driverId` |
| Actor | Admin/Ops |
| Goal | Review ho so driver va thao tac lock/unlock |
| Query | `adminDriver` |
| Mutation | approve/reject profile, approve/reject vehicle, approve/reject payment account, lock/unlock driver |
| Data | profile, vehicle, documents, payment account, platform fee, complaints, audit |
| Primary actions | Approve, reject, lock, unlock, add note |
| Validation | Action yeu cau note khi reject/lock/unlock |
| Acceptance | Moi admin decision ghi audit log |

## 7.7 ADM-FEE-001 Platform Fee Review

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/platform-fees` |
| Actor | Finance/Admin |
| Goal | Review proof phi nen tang cua driver |
| Query | `adminPlatformFeePayments` |
| Mutation | approve/reject proof |
| Data | driver, amount, QR/bank target, proof image, status |
| Primary actions | Approve, reject, open driver |
| Acceptance | Driver chi active khi fee proof hop le va cac dieu kien khac pass |

## 7.8 ADM-FOOD-001 Brand Management

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/food/brands` |
| Actor | Food Admin |
| Goal | Quan ly brand/chain nha hang |
| Query | `adminRestaurantBrands` |
| Mutation | create/update brand |
| Data | name, status, contact, metadata |
| Primary actions | Create, edit, archive, open outlets |
| Acceptance | Brand tao xong co the gan outlet va menu |

## 7.9 ADM-FOOD-002 Outlet Management

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/food/outlets` |
| Actor | Food Admin |
| Goal | Quan ly cua hang/outlet |
| Query | `adminFoodOutlets` |
| Mutation | create/update outlet, update hours |
| Data | brand, address, geo, region, opening hours, availability |
| Primary actions | Create, edit, set hours, toggle availability |
| Validation | Geo phai nam trong region ho tro Food |
| Acceptance | Outlet ngoai region ho tro Food khong duoc publish |

## 7.10 ADM-FOOD-003 Menu Builder

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/food/menus/:menuId` |
| Actor | Food Admin |
| Goal | Tao menu canonical, category, item, modifier |
| Query | `adminMenu` |
| Mutation | CRUD menu/category/item/modifier/option |
| Data | item name, price, image, availability, modifier rules |
| Primary actions | Add category, add item, add modifier, reorder, preview |
| Validation | Price >= 0, modifier min/max valid, item can publish only when required fields complete |
| Acceptance | Menu co it nhat 1 active item moi publish duoc |

## 7.11 ADM-FOOD-004 Outlet Overrides and Publish

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/food/outlets/:outletId/catalog` |
| Actor | Food Admin |
| Goal | Dieu chinh menu theo outlet va publish effective catalog |
| Query | `adminOutletCatalog`, `effectiveOutletMenuPreview` |
| Mutation | update outlet overrides, publish catalog |
| Data | item overrides, modifier option overrides, availability, price |
| Primary actions | Override price, mark unavailable, publish, unpublish |
| Acceptance | Customer chi thay published/effective catalog |

## 7.12 ADM-OPS-001 Live Ride Monitoring

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/ops/rides` |
| Actor | Ops/Admin |
| Goal | Theo doi Ride dang matching/active/problem |
| Query | `adminRideOrders` |
| Realtime | `ride.*`, `matching.*`, `payment.*`, `complaint.*` |
| Primary actions | Open ride detail, open payment proof, open complaint |
| Acceptance | Admin thay timeline va status gan realtime |

## 7.13 ADM-OPS-002 Live Food Monitoring

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/ops/food-orders` |
| Actor | Ops/Admin |
| Goal | Theo doi Food order dang matching/payment/purchase/delivery/problem |
| Query | `adminFoodOrders` |
| Realtime | `food.*`, `matching.*`, `payment.*`, `complaint.*` |
| Primary actions | Open order detail, open payment proof, open complaint |
| Acceptance | Admin thay ro order nao bi ket o payment/purchase/delivery |

## 7.14 ADM-EVIDENCE-001 Evidence Viewer

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | Embedded drawer/modal |
| Actor | Admin/Ops |
| Goal | Xem payment proof, chat image, complaint evidence |
| Query | media/evidence query TBD |
| Mutation | mark evidence reviewed |
| Data | image, uploader, createdAt, linked entity, retention flag |
| Primary actions | View, zoom, mark reviewed, attach to complaint |
| Acceptance | Admin co the inspect proof de xu ly tranh chap |

## 7.15 ADM-COMPLAINT-001 Complaint Queue

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/complaints` |
| Actor | Ops/Admin |
| Goal | Xu ly khieu nai va tranh chap |
| Query | `adminComplaints` |
| Mutation | none on list |
| Data | complaint type, severity, status, driver/customer, related order, qualifying lock count |
| Primary actions | Filter, open complaint |
| Acceptance | Paid/no-show complaint noi bat de xu ly nhanh |

## 7.16 ADM-COMPLAINT-002 Complaint Detail

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/complaints/:complaintId` |
| Actor | Ops/Admin |
| Goal | Review evidence, request response, resolve complaint |
| Query | `adminComplaint` |
| Mutation | assign, request driver response, resolve, lock/unlock driver, create fraud case |
| Data | timeline, evidence, payment proof, chat refs, driver risk status |
| Primary actions | Resolve, escalate, lock driver, unlock driver |
| Acceptance | Complaint thu 2 qualifying paid/no-show trigger auto-lock neu chua lock |

## 7.17 ADM-AUDIT-001 Audit Log

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/audit-logs` |
| Actor | Admin |
| Goal | Tra cuu thay doi quan trong |
| Query | `auditLogs` |
| Mutation | none |
| Data | actor, action, entity, before/after summary, createdAt |
| Primary actions | Search/filter/export future |
| Acceptance | Critical admin/system action co audit |

# 8. Customer App P0 screen inventory

Customer app target: mobile-first, task-focused, easy to use in Vietnamese. Home should expose Ride and Food clearly by region availability.

## 8.1 CUS-AUTH-001 OTP Login

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/auth/phone`, `/auth/verify` |
| Goal | Customer dang nhap bang phone OTP |
| Query | `me` |
| Mutation | `startOtpLogin`, `verifyOtpLogin` |
| States | Enter phone, waiting OTP, verify, resend countdown, error |
| Acceptance | Verify thanh cong nhan Firebase custom token va vao app |

## 8.2 CUS-HOME-001 Home and Service Availability

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/home` |
| Goal | Chon Ride/Food trong region hien tai |
| Query | `me`, `resolveRegion`, service availability |
| Data | current region, Ride availability, Food availability, active order/ride |
| Primary actions | Book ride, order food, resume active job |
| States | No location, region unavailable, service disabled |
| Acceptance | Service bi disable thi CTA khong tao order |

## 8.3 CUS-RIDE-001 Ride Request

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/ride/new` |
| Goal | Nhap pickup/dropoff va xem gia goi y |
| Query | address/geocoding/routing, `rideQuote` |
| Mutation | `createRideOrder` |
| Data | pickup, dropoff, route, distance, duration, recommended fare |
| Primary actions | Set pickup/dropoff, confirm ride |
| Validation | Pickup/dropoff trong region ho tro Ride |
| Acceptance | Tao ride order thanh cong thi qua matching |

## 8.4 CUS-RIDE-002 Ride Matching

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/ride/:rideId/matching` |
| Goal | Cho tai xe nhan chuyen |
| Query | `rideOrder` |
| Realtime | `matching.session_started`, `matching.offer_*`, `ride.assigned`, `matching.no_driver_found` |
| Primary actions | Cancel while matching |
| States | Searching, driver assigned, no driver found, cancelled |
| Acceptance | No driver found hien retry/cancel |

## 8.5 CUS-RIDE-003 Active Ride

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/ride/:rideId` |
| Goal | Theo doi tai xe va trang thai ride |
| Query | `rideOrder` |
| Realtime | `driver.location_updated`, `ride.*`, `chat.message_created` |
| Data | driver, vehicle, route, status timeline, payment state |
| Primary actions | Chat, call/contact policy, upload proof if required, cancel/report |
| Acceptance | Timeline khop state machine Ride |

## 8.6 CUS-PAY-001 Ride Payment Proof

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/ride/:rideId/payment` |
| Goal | Chuyen khoan truc tiep cho driver va upload proof |
| Query | `rideOrder`, driver payment account |
| Mutation | `createMediaUpload`, `submitPaymentProof` |
| Data | amount, bank account/QR, transfer content, proof image |
| Primary actions | Copy amount/content, upload proof, submit |
| Acceptance | Khong hien COD/cash/gateway; proof thanh cong cap nhat payment status |

## 8.7 CUS-RIDE-004 Ride Completion and Rating

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/ride/:rideId/complete` |
| Goal | Xac nhan hoan tat va danh gia |
| Query | `rideOrder` |
| Mutation | `rateRide` |
| Data | fare, driver, rating, tags, comment |
| Acceptance | Chi rating duoc ride completed |

## 8.8 CUS-FOOD-001 Food Discovery

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/food` |
| Goal | Xem outlet/mon an co the dat |
| Query | `foodOutlets`, `effectiveOutletMenu` |
| Data | outlet, opening status, categories, items, prices |
| Primary actions | Search/filter future, open outlet, add item |
| States | No Food service, no outlet, outlet closed |
| Acceptance | Chi hien published/effective catalog |

## 8.9 CUS-FOOD-002 Outlet Menu and Cart

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/food/outlets/:outletId` |
| Goal | Chon mon, modifier, quantity |
| Query | `effectiveOutletMenu` |
| Data | items, modifier groups, options, cart |
| Primary actions | Add/update/remove item, view cart |
| Validation | Required modifier min/max |
| Acceptance | Cart tinh subtotal dung theo menu effective |

## 8.10 CUS-FOOD-003 Checkout

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/food/checkout` |
| Goal | Tao food order voi delivery fee he thong de xuat |
| Query | `foodQuote` |
| Mutation | `createFoodOrder` |
| Data | items, item subtotal, delivery fee, total estimate, address |
| Primary actions | Confirm order |
| Validation | Khong cho customer nhap/sua delivery fee |
| Acceptance | Order tao xong qua matching/payment flow |

## 8.11 CUS-FOOD-004 Food Payment Proof

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/food/orders/:orderId/payment` |
| Goal | Chuyen khoan truc tiep cho driver truoc khi driver mua mon |
| Query | `foodOrder`, driver payment account |
| Mutation | `createMediaUpload`, `submitPaymentProof` |
| Data | item subtotal, delivery fee, total transfer, QR/bank account, proof |
| Acceptance | Driver bi block mua mon neu proof chua duoc submit/confirmed theo policy |

## 8.12 CUS-FOOD-005 Active Food Order

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/food/orders/:orderId` |
| Goal | Theo doi trang thai food order |
| Query | `foodOrder` |
| Realtime | `food.*`, `payment.*`, `chat.message_created` |
| Data | outlet, driver, items, status timeline, payment state |
| Primary actions | Chat, confirm item/price change, report issue, rate after complete |
| Acceptance | Timeline hien ro dang cho payment/proof/purchase/delivery |

## 8.13 CUS-FOOD-006 Food Change Request

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | Embedded sheet |
| Goal | Khach confirm thay doi mon/gia khi tai xe bao nha hang het mon/tang gia |
| Query | `foodChangeRequest` |
| Mutation | `customerRespondFoodChangeRequest` |
| Data | old item/price, new item/price, delta amount, note, images optional |
| Primary actions | Accept, reject |
| Acceptance | Reject/timeout xu ly theo policy cancellation/next step |

## 8.14 CUS-CHAT-001 Job Chat

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/chat/:roomId` |
| Goal | Chat voi driver trong active Ride/Food |
| Query | `chatMessages` |
| Mutation | `sendChatMessage`, `createMediaUpload` |
| Realtime | `chat.message_created`, `chat.room_closed` |
| Data | text, image, sender, timestamp |
| Acceptance | Non-participant khong doc/gui duoc; retention 1 tuan |

## 8.15 CUS-COMPLAINT-001 Complaint Intake

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/complaints/new` |
| Goal | Tao khieu nai, dac biet paid/no-show |
| Query | related order/ride |
| Mutation | `createComplaint` |
| Data | type, description, evidence, related payment proof |
| Validation | Paid/no-show can payment proof |
| Acceptance | Complaint tao xong hien status va admin queue nhan duoc |

# 9. Driver App P0 screen inventory

Driver app target: mobile-first for work context. UI must be fast, readable outdoors, with large primary actions and clear locked/blocked states.

## 9.1 DRV-AUTH-001 OTP Login

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/auth/phone`, `/auth/verify` |
| Goal | Driver dang nhap bang phone OTP |
| Query | `me`, `driverProfile` |
| Mutation | `startOtpLogin`, `verifyOtpLogin` |
| Acceptance | Driver vao onboarding neu chua active |

## 9.2 DRV-ONB-001 Driver Onboarding

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/onboarding` |
| Goal | Driver nop thong tin ho so co ban |
| Query | `driverProfile` |
| Mutation | update driver profile, create media upload |
| Data | name, phone, avatar, document placeholders |
| Acceptance | Giay to cu the se chot sau, UI can support upload evidence slots |

## 9.3 DRV-VEH-001 Vehicle and Service Eligibility

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/vehicle` |
| Goal | Driver khai bao xe va service muon chay |
| Query | `driverVehicles`, `regionServices` |
| Mutation | create/update vehicle, request service eligibility |
| Data | plate, type, documents, Ride/Food eligibility |
| Acceptance | Admin approval required before online |

## 9.4 DRV-PAY-001 Payment Account and Platform Fee

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/payment-account` |
| Goal | Driver khai bao tai khoan nhan tien va nop phi nen tang |
| Query | driver payment account, platform fee invoice |
| Mutation | create/update payment account, submit platform fee proof |
| Data | bank name, account number, account holder, QR/proof |
| Acceptance | Khach se thay account/QR nay tren payment screen sau khi assigned |

## 9.5 DRV-HOME-001 Driver Home

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/home` |
| Goal | Xem trang thai va bat/tat online |
| Query | `driverProfile`, `driverAvailability` |
| Mutation | `goOnline`, `goOffline`, `updateDriverLocation` |
| Realtime | account/risk events |
| Data | activation status, blocked reasons, service toggles, current region |
| Acceptance | Locked/ineligible driver khong online duoc |

## 9.6 DRV-MATCH-001 Incoming Offer

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | Modal/fullscreen offer |
| Goal | Driver accept/reject Ride/Food offer |
| Query | offer detail maybe via `matchingOffer` |
| Mutation | `acceptMatchingOffer`, `rejectMatchingOffer` |
| Realtime | `matching.offer_sent`, `matching.offer_expired`, `matching.assignment_confirmed` |
| Data | service, pickup, dropoff/outlet, distance, estimated earning, timeout |
| Acceptance | Food offer khong co negotiate fee |

## 9.7 DRV-RIDE-001 Active Ride

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/rides/:rideId` |
| Goal | Xu ly Ride tu nhan chuyen den hoan tat |
| Query | `rideOrder` |
| Mutation | driver arrived, start ride, complete ride, confirm/dispute payment |
| Realtime | `ride.*`, `payment.*`, `chat.message_created` |
| Data | customer, route, fare, payment proof, status timeline |
| Primary actions | Navigate, chat, arrived, start, complete, confirm payment |
| Acceptance | Action buttons render theo `allowedActions` |

## 9.8 DRV-FOOD-001 Active Food Order

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/food/orders/:orderId` |
| Goal | Xu ly Food order tu nhan don, xac nhan payment, mua mon, giao hang |
| Query | `foodOrder` |
| Mutation | confirm/dispute payment, mark arrived outlet, mark purchased, request item/price change, pickup, complete |
| Realtime | `food.*`, `payment.*`, `chat.message_created` |
| Data | outlet, items, customer address, proof, purchase status |
| Acceptance | Khong cho mark purchased/truoc restaurant purchase khi payment proof chua hop le |

## 9.9 DRV-FOOD-002 Food Change Request

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | Embedded sheet |
| Goal | Driver bao mon het/gia doi va xin customer confirm |
| Query | `foodOrder` |
| Mutation | `createFoodChangeRequest` |
| Data | affected item, new option, old/new price, note, image optional |
| Acceptance | Order cho customer response va UI hien pending |

## 9.10 DRV-CHAT-001 Job Chat

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/chat/:roomId` |
| Goal | Chat voi customer bang text/image |
| Query | `chatMessages` |
| Mutation | `sendChatMessage`, `createMediaUpload` |
| Realtime | `chat.message_created`, `chat.room_closed` |
| Acceptance | Chat dong theo job/retention policy |

## 9.11 DRV-COMPLAINT-001 Complaint and Response

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | `/complaints`, `/complaints/:id` |
| Goal | Driver tao khieu nai hoac phan hoi khieu nai |
| Query | driver complaints |
| Mutation | create complaint, respond complaint |
| Data | type, description, evidence, admin status |
| Acceptance | Driver bi lock thay ro complaint lien quan va next step |

## 9.12 DRV-RISK-001 Locked Account State

| Field | Spec |
|---|---|
| Priority | P0 |
| Route | Global blocking state |
| Goal | Thong bao driver khi account bi lock |
| Query | `driverProfile`, `driverRiskStatus` |
| Mutation | none, maybe contact/support future |
| Data | lock reason, lock source, complaint refs, status |
| Acceptance | Locked driver khong thay go-online/offer actions |

# 10. Landing Web P0/P1 placeholder

Landing page lam sau theo founder content. Toi thieu can co structure:

| Screen | Priority | Purpose |
|---|---:|---|
| LND-HOME-001 | P1 | Gioi thieu Onway |
| LND-DRIVER-001 | P1 | Dang ky tai xe |
| LND-RESTAURANT-001 | P1 | Dang ky nha hang/future merchant interest |
| LND-DOWNLOAD-001 | P1 | Tai app customer/driver |
| LND-LEGAL-001 | P1 | Terms, privacy, contact |

Landing khong nam trong P0 core flow code neu founder chua chot noi dung.

# 11. Merchant App future placeholder

Merchant App lam sau, khong code P0.

Future screen ideas:

- MRC-AUTH-001 Merchant login.
- MRC-OUTLET-001 Outlet dashboard.
- MRC-MENU-001 Menu edit request.
- MRC-ORDER-001 Order visibility.
- MRC-PROMO-001 Promotion future.

# 12. Component inventory

## 12.1 Admin components

- `AdminShell`
- `SidebarNav`
- `Topbar`
- `DataTable`
- `FilterBar`
- `StatusBadge`
- `MoneyCell`
- `DateTimeCell`
- `ActorCell`
- `EntityLink`
- `DetailHeader`
- `Timeline`
- `AuditTrail`
- `EvidenceGallery`
- `ImageLightbox`
- `MapPreview`
- `ActionBar`
- `ActionDrawer`
- `ConfirmDialog`
- `RejectWithReasonDialog`
- `LockDriverDialog`
- `PolicyEditor`
- `OpeningHoursEditor`
- `MenuTree`
- `ModifierEditor`
- `PublishChecklist`

## 12.2 Mobile shared components

- `AppShell`
- `AuthPhoneForm`
- `OtpInput`
- `ServiceCard`
- `AddressSearchInput`
- `MapView`
- `RouteSummary`
- `FareSummary`
- `PaymentInstruction`
- `QrDisplay`
- `ProofUploader`
- `ProofStatusCard`
- `StatusTimeline`
- `DriverCard`
- `CustomerCard`
- `OfferCard`
- `CountdownRing`
- `ChatThread`
- `ChatComposer`
- `ImageMessage`
- `ComplaintForm`
- `RatingSheet`
- `BlockedState`
- `OfflineBanner`
- `ReconnectBanner`

# 13. Minimum GraphQL binding per screen

Moi screen khi implement can khai bao:

```txt
screenId:
route:
ownerApp:
queries:
mutations:
subscriptions:
requiredPermissions:
allowedActionsUsed:
emptyStates:
errorStates:
analyticsEvents:
```

Analytics events co the stub P0 neu chua co analytics provider.

# 14. Screen acceptance template

Moi screen PR/UI spec sau nay can co:

1. Purpose.
2. Actor.
3. Route/deep link.
4. Entry points.
5. Exit points.
6. Data dependencies.
7. Mutations/actions.
8. Realtime events.
9. Permissions.
10. Loading/empty/error/offline states.
11. Validation rules.
12. Copy requirements.
13. Accessibility requirements.
14. Acceptance tests.
15. Out of scope.

# 15. Accessibility and mobile constraints

- Mobile primary actions phai bam duoc bang 1 tay trong flow tai xe.
- Button critical action can co confirm neu irreversible/dispute-sensitive.
- Text payment amount phai ro, de copy.
- Error payment proof phai actionable: upload lai, lien he support/admin, cho driver confirm.
- Map screen phai co fallback text address/list info.
- Chat image phai co upload progress, failed retry.
- Admin table phai co keyboard-friendly filter/search where possible.

# 16. UI acceptance gates before coding a flow

Truoc khi code moi vertical slice, phai chot:

- Screens in slice.
- Data queries/mutations/subscriptions.
- Allowed actions.
- UI states.
- Empty/error/loading copy.
- Admin monitoring page needed for the slice.
- Evidence/audit visibility.
- Design-system token mapping if visual reference already chot.

# 17. UI work sequencing

Suggested UI sequencing theo implementation sprint:

| Sprint | UI work |
|---:|---|
| 4 | Admin shell, nav, tables, detail shell, login |
| 5 | Food admin brand/outlet/menu/publish screens |
| 7 | Customer/Driver app shells, auth, home, navigation |
| 8 | Ride customer/driver/admin monitoring screens |
| 9 | Food customer/driver/admin monitoring screens |
| 10 | Chat, payment proof, evidence viewer polish |
| 11 | Complaint/risk/lock screens |
| 12 | Full UX QA, accessibility, responsive polish |

# 18. Open UI decisions

Can founder confirm:

1. Brand direction and references.
2. Admin portal visual density.
3. Customer app home priority: Ride-first, Food-first, or balanced.
4. Driver app map-first vs job-list-first when online.
5. Payment proof UX: require image only, or image + transfer note.
6. Chat attachment limits and compression target.
7. Exact driver document slots for onboarding.
