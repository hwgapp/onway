# ONWAY - PRD MASTER MVP

**Loai tai lieu:** Product Requirements Document (PRD) Master  
**Phien ban:** 0.1 (ban lam viec)  
**Trang thai:** Dang review  
**Ngay cap nhat:** 11/09/2026  
**Ngon ngu chinh:** Tieng Viet  
**Pham vi:** Onway MVP - Ride Hailing va Food Delivery  

---

# 1. Muc dich tai lieu

Tai lieu nay la PRD goc cho Onway MVP, dung de chot:

- san pham Onway MVP gom nhung platform nao;
- pham vi launch ban dau;
- cac quyet dinh san pham quan trong da chot sau BRD/Architecture;
- thu tu PRD con can viet;
- cach chia PRD theo journey de build xong flow nao thi test duoc flow do.

PRD Master khong thay the cac PRD chi tiet. Cac PRD chi tiet se duoc tach theo platform va theo journey/vertical slice.

# 2. Nguon dau vao

- `doc/01-BRD/ONWAY_BRD_v0.5_VI.md`
- `doc/03-Architecture/ONWAY_ARCHITECTURE_DECISIONS_v0.2_VI.md`
- Cac quyet dinh san pham bo sung trong qua trinh review PRD ngay 11/09/2026.

Khi PRD Master mau thuan voi BRD hien tai, PRD Master ghi ro do la quyet dinh moi can dong bo nguoc lai BRD.

# 3. Tam nhin san pham

Onway la nen tang goi xe va giao do an theo huong:

> AI-native, cong dong cung van hanh, 0% commission va han che giu tien giao dich.

Gia tri cot loi:

- Tai xe giu lai gia tri dich vu ho tao ra.
- Nha hang khong mat commission tren gia tri mon an.
- Khach hang nhan gia minh bach, canh tranh.
- Onway van hanh gon bang cau hinh, AI, audit trail va quy trinh xu ly ngoai le.

# 4. Platform map MVP

Onway MVP gom cac platform sau:

| Platform | MVP | Vai tro |
|---|---:|---|
| API Core Backend | Co | Xu ly domain business, GraphQL API, realtime, matching, audit, policy config. |
| Customer App | Co | Khach dat xe, dat do an, chat voi tai xe, chuyen khoan, theo doi va khieu nai. |
| Driver App | Co | Tai xe online/offline, nhan job Ride/Food, chat voi khach, cap nhat trang thai, upload bang chung. |
| Web Admin Portal | Co | Onway quan tri region, driver, catalog Food, monitoring, dispute, fraud/risk lock va audit. |
| Landing Web | P1 | Gioi thieu thong tin, CTA tai app/dang ky; noi dung chi tiet lam sau. |
| Merchant App | P2 | Future platform cho nha hang; khong thuoc MVP launch. |

# 5. Tech stack da chot

Theo Architecture Decisions:

- Monorepo: Nx.
- Backend API: Node.js + NestJS, modular/domain architecture.
- API chinh: GraphQL.
- Realtime: WebSocket Gateway rieng cho location, matching, tracking va chat/realtime events.
- Database: PostgreSQL + PostGIS.
- Cache/presence/ephemeral matching state: Redis.
- Auth: Firebase Auth.
- Map provider: HERE Maps.
- SMS/OTP tai Viet Nam: ViHAT.
- Landing Web: Next.js.
- Admin Portal: ReactJS, shadcn/ui, Animate UI.
- Customer App: Flutter.
- Driver App: Flutter.
- Cloud: AWS.

# 6. Pham vi launch MVP

## 6.1 Dich vu

MVP launch gom:

- Ride Hailing.
- Food Delivery.

## 6.2 Dia ly

- Launch thuong mai dau tien tai TP. Ho Chi Minh.
- Chi mo trong cac region/polygon duoc admin cau hinh va phe duyet.
- Danh sach quan/polygon cu the se duoc chot trong PRD `Region, Currency & Service Availability`.

## 6.3 Currency

- Currency la setting theo region.
- MVP tai Viet Nam cau hinh currency mac dinh la `VND`.
- Khong hard-code currency o cap toan he thong.

# 7. Quyet dinh san pham da chot cho PRD

## 7.1 Payment MVP

MVP chi ho tro mot phuong thuc thanh toan cho Ride/Food:

> Chuyen khoan ngan hang truc tiep giua khach va tai xe, co the thuc hien bang QR.

Khong co trong MVP:

- COD.
- Tien mat.
- Payment gateway.
- Wallet.
- Onway-held payment.
- Escrow/ky quy/giu tien don chuyen.

He thong can luu:

- trang thai chuyen khoan do nguoi dung xac nhan;
- anh/bang chung chuyen khoan bat buoc;
- chat va hinh anh lien quan neu co;
- GPS/timeline/order state can thiet;
- audit trail;
- du lieu phuc vu dispute, fraud/risk review va compliance.

## 7.2 Dieu kien "co tien thi di"

Tai xe chi duoc tiep tuc thuc hien dich vu sau khi payment proof duoc ghi nhan theo flow cua app.

Food:

- Khach phai chuyen khoan cho tai xe truoc.
- Tai xe chi di den nha hang/dat mon sau khi co payment proof.

Ride:

- Flow thanh toan chi tiet se duoc chot trong PRD Ride, nhung MVP van chi dung bank transfer/QR va co payment proof.

## 7.3 Bank transfer proof

- Payment proof la bat buoc trong MVP.
- Customer phai upload hoac chup anh bang chung chuyen khoan.
- Bang chung duoc luu kem order/trip, metadata va audit trail.
- Driver co the xac nhan da nhan tien.
- Neu co tranh chap, admin xem payment proof, chat, timeline va GPS/location de xu ly.

## 7.4 COD va Trust

- MVP tam thoi bo qua Trust logic.
- Khong co COD trong MVP.
- Khong dung Trust de gate payment, Food ordering hoac launch flow.
- Cac logic Trust/privilege chuyen sang phase sau.

## 7.5 Food delivery fee negotiation

MVP bo thoa thuan phi giao Food.

- He thong tinh/de xuat delivery fee.
- Customer chap nhan fee de dat don hoac khong dat.
- Driver chi Accept/Reject Food job.
- Driver khong gui Counter Offer.
- Customer khong de xuat delivery fee khac.

Quyet dinh nay da duoc dong bo sang BRD v0.5 va Architecture v0.2.

## 7.6 Ride price negotiation

Vi MVP tam thoi bo qua Trust logic, Ride price negotiation khong phai dependency bat buoc cho launch.

Huong PRD:

- P0 co the chi dung recommended price.
- Negotiation Ride co the dua vao P1 hoac feature flag sau khi co policy ro.
- Neu giu trong P0, can co gating don gian khong phu thuoc Trust Engine day du.

Quyet dinh cuoi cung se chot trong PRD Ride.

## 7.7 Chat customer-driver

MVP co chat giua customer va driver.

Yeu cau:

- Chat theo ride/order room.
- Ho tro text va gui hinh.
- Chat duoc luu trong 1 tuan.
- Chat/hinh co the duoc dung lam bang chung khi co khieu nai trong thoi gian retention.
- Sau retention 1 tuan, chinh sach xoa/luu toi thieu metadata se duoc chot trong PRD Privacy/Data Retention.

## 7.8 Complaint va risk lock

Bat buoc co flow xu ly truong hop customer da chuyen khoan nhung tai xe khong den/khong thuc hien.

Rule P0:

- Customer tao khieu nai va gui bang chung.
- Neu mot driver co 2 khieu nai hop le dang mo lien quan den viec da nhan/chua thuc hien, he thong tu dong lock driver.
- Driver bi lock khong duoc nhan job moi.
- Admin co the thao tac lock/unlock driver thu cong.
- Admin review evidence, chat, payment proof, GPS/location, timeline va order/trip state.
- Admin quyet dinh unlock, tiep tuc suspend, block/ban hoac xu ly trach nhiem tai chinh theo policy.

## 7.9 Food supply admin-first

Truoc khi customer co the dat mon, Admin Portal phai co du lieu Food supply.

MVP Food catalog do admin tao va quan ly:

- brand/chain;
- outlet/store;
- region cua outlet;
- dia chi/toa do;
- gio mo cua;
- trang thai hoat dong;
- menu/category/item/modifier/option;
- gia mon;
- hinh anh menu/mon neu co;
- publish/unpublish;
- outlet override va availability.

Tai xe chua can thiep menu/restaurant trong launch MVP.

## 7.10 Mission, Community Truth va AI Restaurant Operations

- Khong la dependency cua launch MVP.
- Chuyen sang P2/post-launch.
- PRD Master van giu vi day la huong scale dai han.

## 7.11 Advertising

- Khong thuoc launch MVP.
- Chuyen sang P2/post-launch.

# 8. Nguyen tac chia PRD

PRD se duoc chia theo 3 lop:

1. PRD Master: chot san pham cap platform va roadmap.
2. General Platform PRD: chot vai tro, architecture boundary va app shell cua tung platform.
3. Journey/Vertical Slice PRD: chot flow end-to-end di qua Customer App, Driver App, Admin Portal va Backend.

Nguyen tac quan trong:

> Build theo journey. Xong flow nao thi phai test duoc flow do end-to-end.

Moi Journey PRD can co:

- actor va goal;
- preconditions;
- user/driver/admin flow;
- screens hoac app surfaces lien quan;
- backend modules/API/realtime events;
- data state machine;
- business rules;
- edge cases;
- admin controls;
- evidence/audit;
- notifications/chat neu co;
- analytics;
- acceptance criteria;
- test scenarios.

# 9. PRD roadmap

## A. Master

| # | PRD | Phase | Ghi chu |
|---:|---|---|---|
| 1 | PRD Master: Onway MVP | P0 | Vision, scope, actors, business rules, platform map, dependency, roadmap. |

## B. General Platform / Codebase

| # | PRD | Phase | Ghi chu |
|---:|---|---|---|
| 2 | PRD General: System Architecture & Codebase | P0 | Nx monorepo, shared types/contracts, environment, CI/CD, testing. |
| 3 | PRD General: API Core Backend | P0 | Backend modules, GraphQL, realtime, audit, config, shared services. |
| 4 | PRD General: Customer App | P0 | App shell, navigation, auth, Ride/Food entry points, profile. |
| 5 | PRD General: Driver App | P0 | App shell, onboarding, Ride/Food jobs, location, profile. |
| 6 | PRD General: Web Admin Portal | P0 | RBAC, configuration, driver review, catalog, risk lock, dispute, monitoring. |
| 7 | PRD General: Landing Web | P1 | Lam sau MVP core. |
| 8 | PRD General: Merchant App Future | P2 | Placeholder cho merchant integration sau. |

## C. Foundation / Cross-Platform

| # | PRD | Phase | Ghi chu |
|---:|---|---|---|
| 9 | PRD: Identity, Auth & Account | P0 | Firebase Auth, role mapping, session/account status. |
| 10 | PRD: Region, Currency & Service Availability | P0 | Country/city/region, polygon, currency, service/vehicle availability. |
| 11 | PRD: Policy Config & Admin Controls | P0 | Tat ca threshold/business number configurable. |
| 12 | PRD: Notification & Realtime Events | P0 | Push, WebSocket, job/matching/tracking/chat events. |
| 13 | PRD: Evidence, Media & Audit Trail | P0 | Evidence, metadata, audit history. |
| 14 | PRD: Location, Maps, Geocoding & Routing | P0 | Address search, GPS, route, distance, ETA. |
| 15 | PRD: Direct Bank Transfer & Payment Confirmation | P0 | QR/bank transfer, payment proof bat buoc, tien khong qua Onway. |
| 16 | PRD: Communication, Chat & Contact Policy | P0 | Chat text/image, direct contact policy, retention 1 tuan. |
| 17 | PRD: Privacy, Consent & Data Retention | P0 | GPS, identity, evidence, chat retention, consent. |
| 18 | PRD: AI Operations & Decision Governance | P1 | AI First, Human by Exception, risk levels; khong chan launch MVP. |

## D. Driver Foundation

| # | PRD | Phase | Ghi chu |
|---:|---|---|---|
| 19 | PRD: Driver Registration & Onboarding | P0 | Phone, identity, documents placeholder, approval. |
| 20 | PRD: Driver Profile, Vehicle & Service Eligibility | P0 | Motorcycle/car, Ride/Food eligibility. |
| 21 | PRD: Driver Platform Fee, Subscription & Refund | P0 | 1M nam dau, quarterly refund, future subscription. |
| 22 | PRD: Driver Online/Offline & Location Presence | P0 | Online state, current location, receiving jobs. |
| 23 | PRD: Driver Risk Lock & Manual Admin Action | P0 | Auto lock sau 2 khieu nai hop le dang mo; admin lock/unlock thu cong. |

## E. Food Supply - MVP Admin-First

| # | PRD | Phase | Ghi chu |
|---:|---|---|---|
| 24 | PRD: Restaurant Brand / Chain Management | P0 | Admin tao brand/chain. |
| 25 | PRD: Outlet / Store Management | P0 | Admin tao outlet/location/hours/region. |
| 26 | PRD: Canonical Menu & Catalog Management | P0 | Admin nhap/quan ly menu ban dau. |
| 27 | PRD: Catalog Publishing | P0 | Draft -> Pending Review -> Published -> Needs Reverification -> Unpublished/Archived. |
| 28 | PRD: Outlet Override & Availability | P0 | Gia, mon, gio, trang thai outlet. |
| 29 | PRD: AI Menu Extraction & Normalization | P2 | Sau launch. |

## F. Ride MVP

| # | PRD | Phase | Ghi chu |
|---:|---|---|---|
| 30 | PRD: Ride Request & Price Recommendation | P0 | Pickup/dropoff, vehicle, recommended price. |
| 31 | PRD: Ride Matching & Driver Accept/Reject | P0 | Progressive batched matching, timeout, assignment. |
| 32 | PRD: Ride Tracking & In-Trip Flow | P0 | Arrival, start, tracking, communication/chat. |
| 33 | PRD: Ride Completion & Direct Bank Transfer Confirmation | P0 | QR bank transfer + proof + completion. |
| 34 | PRD: Ride Rating | P0 | Customer/Driver rating. |
| 35 | PRD: Ride Cancellation, Timeout & No-Show | P0 | Before/after matching rules. |
| 36 | PRD: Ride Price Negotiation | P1 | Tam hoan do Trust logic lam sau; co the feature flag. |

## G. Food MVP

| # | PRD | Phase | Ghi chu |
|---:|---|---|---|
| 37 | PRD: Food Discovery & Cart | P0 | Outlet, menu, modifier, cart. |
| 38 | PRD: Food Order Placement & Delivery Fee Recommendation | P0 | Khong negotiation; customer accept fee hoac khong dat. |
| 39 | PRD: Food Driver Matching & Accept/Reject | P0 | Matching Food. |
| 40 | PRD: Food Direct QR Bank Transfer Confirmation | P0 | Customer -> Driver truc tiep, payment proof bat buoc. |
| 41 | PRD: Driver Restaurant Purchase Flow | P0 | Driver toi quan, order, tra restaurant sau khi co tien. |
| 42 | PRD: Food Item / Price Change Confirmation | P0 | Sai gia, het mon, customer confirm. |
| 43 | PRD: Food Waiting Policy | P0 | Config theo Brand. |
| 44 | PRD: Food Delivery, Completion & Rating | P0 | Delivery lifecycle. |
| 45 | PRD: Food Cancellation & Financial Responsibility | P0 | Khong dung generic refund vi tien khong qua Onway. |

## H. Risk / Complaint / Growth

| # | PRD | Phase | Ghi chu |
|---:|---|---|---|
| 46 | PRD: Complaint & Dispute Journey | P0 | Complaint intake, evidence, operator/admin review. |
| 47 | PRD: Paid-but-Driver-No-Show Dispute | P0 | Customer da chuyen khoan, driver khong den; risk lock flow. |
| 48 | PRD: Fraud Case Journey | P0 | Manual/system triage P0, human decision, appeal; AI-assisted future. |
| 49 | PRD: Referral Journey | P1 | Driver/customer referral + fraud gating; co the sau core launch. |
| 50 | PRD: Customer Trust & Privileges | P2 | T0-T4, future privileges; COD requires separate decision if ever revisited. |
| 51 | PRD: Driver Trust & Risk Controls | P2 | D0-D4, risk restrictions future. |
| 52 | PRD: Gamification, XP, Level & Badge | P2 | Sau core launch. |

## I. Post-Launch Community / AI / Monetization

| # | PRD | Phase | Ghi chu |
|---:|---|---|---|
| 53 | PRD: Mission Engine | P2 | Driver missions. |
| 54 | PRD: Restaurant Mission Capture | P2 | In-app camera, GPS, full menu capture. |
| 55 | PRD: Community Truth Verification | P2 | 2-3 drivers, confidence, conflict. |
| 56 | PRD: AI Restaurant Lifecycle | P2 | Stale data, menu changes, auto missions. |
| 57 | PRD: Advertising & Sponsored Placement | P2 | Sau launch. |

# 10. MVP critical path de build va test

De launch som, PRD chi tiet nen uu tien theo thu tu:

1. Identity, Auth & Account.
2. Region, Currency & Service Availability.
3. Direct Bank Transfer & Payment Confirmation.
4. Communication, Chat & Contact Policy.
5. Driver Registration, Platform Fee va Activation.
6. Driver Online/Offline & Location Presence.
7. Food Supply Admin-First: Brand, Outlet, Menu, Publishing.
8. Ride Request -> Matching -> Tracking -> Payment Confirmation -> Rating.
9. Food Discovery -> Order -> Payment Confirmation -> Driver Purchase -> Delivery -> Rating.
10. Complaint/Dispute va Paid-but-Driver-No-Show Risk Lock.
11. Admin Monitoring va Manual Lock/Unlock.

# 11. Out of scope MVP

Khong thuoc launch MVP:

- COD.
- Tien mat.
- Payment gateway.
- Wallet.
- Escrow/Onway-held payment.
- Trust Engine day du.
- Food delivery fee negotiation.
- Ride price negotiation mac dinh.
- Merchant App.
- Driver Mission/Community Truth cho restaurant/menu.
- AI Menu Extraction/OCR production workflow.
- Advertising.
- Customer paid membership.
- Loyalty program day du.
- Corporate Ride.
- Grocery/parcel/shopping.
- Cross-border.

# 12. Open decisions

Cac diem can chot trong PRD chi tiet:

1. Ride payment timing: customer chuyen khoan truoc khi tai xe den don, luc bat dau chuyen, hay luc ket thuc chuyen.
2. Dinh nghia "2 khieu nai hop le dang mo" de auto lock driver: can criteria nao de tranh abuse.
3. Admin SLA xu ly khieu nai payment/no-show.
4. Driver document list cu the theo xe may/o to va theo Ride/Food.
5. Polygon/quanh vung TP. Ho Chi Minh ban dau.
6. Cac trang thai chi tiet cua ride/order/payment proof/dispute.
7. Chat image limits: dung luong, so luong, loai file va moderation/report.
8. Retention sau 1 tuan: xoa noi dung chat/hinh hoan toan hay giu metadata/audit toi thieu.
