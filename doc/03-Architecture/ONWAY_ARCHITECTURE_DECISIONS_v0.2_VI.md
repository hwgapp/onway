# ONWAY - Architecture Decisions

**Loai tai lieu:** Architecture Decision Notes / ADR tong hop  
**Phien ban:** 0.2  
**Ngay cap nhat:** 11/09/2026  
**Ngon ngu:** Tieng Viet  
**Pham vi:** Kien truc he thong Onway MVP  

Tai lieu nay luu lai cac quyet dinh kien truc da trao doi, de lam dau vao cho thiet ke chi tiet, PRD ky thuat, scaffold monorepo va roadmap trien khai.

---

# 1. Stack tong the

## ADR-001 - Monorepo

**Quyet dinh:** Dung Nx monorepo cho toan bo he thong.

Pham vi monorepo du kien:

- Backend API: Node.js, NestJS, modular architecture.
- Landing Web: Next.js.
- Admin Portal: ReactJS.
- Mobile Customer App: Flutter.
- Mobile Driver App: Flutter.
- Shared contracts, shared types, UI libraries, test utilities va config dung chung.

## ADR-002 - Backend

**Quyet dinh:** Backend dung Node.js + NestJS theo modular/domain architecture.

Cac domain module du kien, gom P0 va future modules:

- identity
- customer
- driver
- admin
- region
- vehicle
- pricing
- matching
- ride
- food-order
- restaurant
- menu
- mission
- community-truth
- trust
- fraud
- complaint
- subscription / platform-fee
- referral
- reward
- notification
- media-evidence
- ai-ops
- audit-log
- policy-config

## ADR-003 - API chinh

**Quyet dinh:** Dung GraphQL lam API chinh cho business operations.

GraphQL phu hop cho:

- profile;
- ride/order lifecycle;
- menu/restaurant data;
- admin portal;
- policy/config;
- fraud/risk workflows va future trust/mission workflows;
- lich su va truy van du lieu co cau truc.

---

# 2. Realtime, location va matching

## ADR-004 - Realtime layer rieng

**Quyet dinh:** Khong dung GraphQL Subscription lam kenh chinh cho location/matching. Dung WebSocket rieng cho realtime co tan suat cao.

Ly do:

- GPS/location update co tan suat cao.
- Matching can connection nhe, on dinh va de scale.
- WebSocket gateway rieng de kiem soat room, presence, backpressure va reconnect tot hon.
- GraphQL Subscription chi nen dung cho event nhe, tan suat thap neu can.

Kien truc de xuat:

```txt
Mobile/Web
  -> GraphQL API: business data, profile, order, admin config
  -> WebSocket Realtime Gateway: driver location, availability, matching, tracking

NestJS API
  -> PostgreSQL/PostGIS
  -> Redis cache/presence
  -> Queue jobs
```

Realtime flow du kien:

- Driver app gui location qua WebSocket khi online hoac dang chuyen/don.
- Redis luu driver presence va last known location ngan han.
- Matching Engine doc candidate driver tu Redis truoc.
- Postgres/PostGIS xac thuc region, polygon, distance va luu cac snapshot quan trong.
- Customer app subscribe tracking theo ride/order room.
- Admin xem trang thai realtime qua WebSocket hoac event nhe.

---

# 3. Data layer

## ADR-005 - Primary database

**Quyet dinh:** Dung PostgreSQL tren AWS RDS.

## ADR-006 - Geospatial

**Quyet dinh:** Bat buoc dung PostGIS cho cac nghiep vu dia ly.

PostGIS dung cho:

- region polygon;
- kiem tra diem don/tra/outlet co nam trong vung hoat dong khong;
- khoang cach;
- geofence;
- service availability theo region.

## ADR-007 - Redis

**Quyet dinh:** Dung Redis cho cache, realtime presence, ephemeral matching state va queue neu MVP dung BullMQ.

Redis khong phai system of record cho don/chuyen, fraud, evidence, payment proof hoac audit.

---

# 4. Auth, maps, SMS

## ADR-008 - Authentication

**Quyet dinh:** Dung Firebase Auth.

Backend se verify Firebase ID token va map sang user/customer/driver/admin trong database noi bo.

## ADR-009 - Map provider

**Quyet dinh:** Dung HERE Maps.

Ly do hien tai: Google Maps khong phu hop/khong kha dung cho pham vi Viet Nam theo quyet dinh san pham.

## ADR-010 - SMS/OTP

**Quyet dinh:** Dung ViHAT cho SMS/OTP tai Viet Nam.

Can thiet ke abstraction `SmsProvider` de sau nay co the thay doi provider neu can.

---

# 5. Payment va money-light

## ADR-011 - Ride/Food payment

**Quyet dinh:** Onway khong lam payment gateway cho tien Ride/Food trong MVP.

Theo BRD/PRD moi nhat:

- Ride: Customer tra truc tiep cho Driver.
- Food: Customer tra truc tiep cho Driver; Driver tra nha hang.
- Onway khong giu tien don/chuyen.
- MVP chi ho tro bank transfer/QR truc tiep giua customer va driver.
- MVP khong ho tro COD, tien mat, wallet, escrow hoac Onway-held payment cho Ride/Food.
- Payment proof la bat buoc cho cac flow thanh toan Ride/Food.

He thong chi luu:

- trang thai thanh toan do nguoi dung xac nhan;
- bang chung/payment proof bat buoc theo flow;
- audit trail;
- du lieu phuc vu fraud/risk, dispute va compliance.

Nen tranh dat ten module chung chung la `payment` cho Ride/Food de khong lech BRD. Ten module nen dung:

- direct-payment-proof;
- bank-transfer-confirmation;
- settlement-evidence.

## ADR-012 - Platform fee

**Quyet dinh hien tai:** Platform fee/subscription cua tai xe la khoan Onway thu truc tiep, nhung MVP chua tich hop cong thanh toan.

Huong MVP:

- Driver chuyen khoan/QR theo huong dan.
- Driver nhap ma tham chieu hoac upload bang chung.
- Admin verify thu cong.
- Sau khi verify, driver moi duoc activate theo policy.

Module rieng nen la `platform-fee`, tach khoi direct Ride/Food payment.

---

# 6. AWS va deployment

## ADR-013 - Cloud

**Quyet dinh:** Dung AWS.

Huong MVP simple:

- Backend API: EC2 simple deployment.
- Database: RDS PostgreSQL + PostGIS.
- Redis: ElastiCache Redis.
- File/evidence storage: S3.
- Logs/metrics: CloudWatch.
- Secrets: AWS Secrets Manager hoac SSM Parameter Store.
- Queue: BullMQ tren Redis.

## ADR-014 - CI/CD

**Quyet dinh:** CI/CD simple truoc, deploy len EC2.

Toi thieu:

- CI: lint, typecheck, unit test, build.
- CD: build artifact/container va deploy len EC2.
- Mobile va web deployment co the tach pipeline sau.

## ADR-015 - Environment

**Quyet dinh hien tai:** Chi co mot production environment duy nhat, connect truc tiep len RDS production.

Khuyen nghi kien truc:

- Van nen co local dev database cho lap trinh va test migration.
- Khong nen dung production data cho seed/test/migration thu.
- Chua can staging trong MVP neu muon giu don gian, nhung can quy trinh deploy can than.

## ADR-016 - Backup/restore

**Quyet dinh:** Phan tich sau.

Khuyen nghi toi thieu khi dung RDS:

- Bat automated backup.
- Bat point-in-time recovery neu chi phi chap nhan duoc.
- Dinh ky test restore khi buoc vao giai doan production that.

---

# 7. Bao mat, audit va compliance

## ADR-017 - Audit trail

**Quyet dinh:** Audit trail la bat buoc.

Can audit cac su kien:

- thay doi policy/config;
- admin/operator action;
- ride/order state transition;
- driver/customer accept/reject;
- moc driver da dat mon;
- bang chung thanh toan truc tiep;
- AI recommendation;
- human decision;
- fraud/dispute lifecycle.

## ADR-018 - Data retention

**Quyet dinh:** Phan tich sau.

Pham vi can phan tich:

- GPS history;
- trip/order trace;
- evidence images;
- fraud/complaint records;
- driver KYC/documents;
- device metadata;
- AI profiling/risk scoring data.

## ADR-019 - Legal/privacy

**Quyet dinh:** Phan tich sau.

Pham vi can phan tich:

- GPS tracking;
- device fingerprint;
- AI profiling;
- fraud scoring;
- driver/customer evidence;
- phone number visibility;
- data deletion/export;
- consent va privacy policy.

---

# 8. Frontend applications

## ADR-020 - Landing Web

**Quyet dinh:** Dung Next.js cho landing page.

## ADR-021 - Admin Portal

**Quyet dinh:** Dung ReactJS cho Admin Portal.

UI stack:

- shadcn/ui;
- Animate UI.

Admin Portal can ho tro RBAC va cac man hinh van hanh:

- region/polygon;
- service rollout;
- pricing/policy config;
- driver verification;
- platform fee verification;
- ride/food monitoring;
- fraud/dispute;
- audit log.

Future/post-launch admin modules:

- mission/community truth;
- advertising;
- AI restaurant lifecycle.

## ADR-022 - Mobile apps

**Quyet dinh:** Dung Flutter cho Customer App va Driver App.

Driver App P0 can dac biet ho tro:

- online/offline;
- realtime location;
- ride/food accept/reject;
- evidence metadata;
- QR/payment proof flow.

Driver App future/post-launch co the ho tro:

- mission capture bang camera trong app;
- trust/gamification;
- referral growth flows.

Customer App can dac biet ho tro:

- ride request;
- food order;
- direct bank transfer/QR flow;
- tracking;
- Ride price negotiation sau P0 neu feature flag/policy cho phep;
- Food khong co delivery fee negotiation trong P0;
- complaint/dispute;
- referral/trust privileges sau P0.

---

# 9. Cac viec can thiet ke tiep

1. Backend module boundary chi tiet.
2. Nx monorepo folder structure.
3. GraphQL schema strategy.
4. WebSocket protocol cho location/matching.
5. Database ERD va PostGIS model.
6. State machine cho Ride, Food, Mission, Referral, Fraud.
7. Policy/config model.
8. Admin RBAC matrix.
9. Evidence storage model.
10. Data retention va privacy/legal analysis.

---

# 10. Ra soat cau hoi kien truc ngay 11/09/2026

## 10.1 Cau hoi da chot cho P0

1. **MVP launch Ride + Food cung luc hay Ride truoc?**
   - Ride Hailing va Food Delivery launch cung nhau trong region duoc phe duyet.

2. **Co can in-app complaint ngay MVP khong?**
   - Co. Customer/Driver co complaint intake, Admin co complaint/dispute queue.

3. **Co chat trong app khong?**
   - Co. Customer-driver chat la P0, ho tro text va image, retention 1 tuan.

4. **Backend la modular monolith truoc hay microservices?**
   - Da chot modular monolith, xem ADR-023.

5. **Admin Portal co bat buoc day 1 khong?**
   - Co. Admin Portal la web, can cho van hanh P0, xem ADR-035.

6. **AI OCR menu co can ngay MVP khong?**
   - Khong. Food P0 admin-first, AI OCR/menu extraction lam sau, xem ADR-036.

7. **Matching flow la broadcast hay sequential?**
   - Dung batched parallel/wave dispatch, xem ADR-024.

8. **Timeout va driver offer concurrency?**
   - Timeout theo policy config, mac dinh Ride 15s va Food 20s moi wave. Moi driver chi mot active offer, xem ADR-025 va ADR-026.

9. **Food prepaid QR/chuyen khoan xac nhan the nao?**
   - Customer upload proof bat buoc; driver xac nhan da nhan tien; Onway khong giu/thu ho tien, xem ADR-029 va ADR-043.

10. **Firebase Auth ket hop ViHAT the nao?**
    - ViHAT OTP -> backend verify -> Firebase custom token -> Firebase ID token, xem ADR-030.

11. **Mobile app structure?**
    - Customer App va Driver App dung Flutter, tach app deploy rieng, reuse shared packages, xem ADR-033.

12. **Admin Portal goi API the nao?**
    - Goi GraphQL truc tiep trong MVP, khong dung BFF rieng, xem ADR-034.

## 10.2 Cau hoi con mo

Khong con open question nao trong muc 10 la blocker san pham P0. Cac open question thap hon ve observability, RBAC chi tiet, rate limit, device identity, retention ngoai chat va release process nam o muc 12.

---

# 11. Quyet dinh bo sung ngay 11/09/2026

## ADR-023 - Backend deployment boundary

**Quyet dinh:** Backend MVP la NestJS modular monolith.

Ly do:

- Domain Onway con dang duoc lam ro, modular monolith giup thay doi nhanh hon microservices.
- Van giu boundary theo module de sau nay tach service neu traffic hoac ownership yeu cau.
- Transaction va state machine Ride/Food/Fraud don gian hon khi o cung mot backend deployment.

## ADR-024 - Matching strategy

**Quyet dinh:** Dung batched parallel / wave dispatch, khong gui toan bo tai xe cung luc va khong chi tuan tu tung tai xe.

Flow de xuat:

1. Tim candidate driver tu Redis presence/location.
2. Loc theo service, vehicle, region, subscription/platform-fee status, online status, active offer lock va risk policy.
3. Tinh diem candidate theo ETA, khoang cach, huong di chuyen, acceptance rate, cancellation rate, completion rate, fairness va do phu hop voi loai don.
4. Neu co driver bat auto-accept va thoa guardrail, he thong co the assign ngay cho candidate co diem tot nhat.
5. Neu khong co auto-accept phu hop, gui offer theo wave nho.
6. First valid accept wins; cac offer con lai duoc revoke.

Khuyen nghi MVP:

- Wave 1: 3 tai xe tot nhat.
- Wave 2: mo rong them 3-5 tai xe neu chua co accept.
- Tang ban kinh/ETA theo tung wave.
- Tong thoi gian matching nen la config rieng theo Ride/Food va region.

Ly do:

- Tuan tu tung tai xe lam tang thoi gian cho khach.
- Broadcast toan bo tai xe gay canh tranh race, trai nghiem kem va kho kiem soat fairness.
- Wave dispatch can bang giua toc do match, fairness va kha nang scale.

## ADR-025 - Driver offer concurrency

**Quyet dinh:** Moi tai xe chi co mot active offer tai mot thoi diem.

Can co atomic lock trong Redis hoac database de tranh mot driver nhan dong thoi nhieu offer khi matching song song.

## ADR-026 - Manual accept timeout

**Quyet dinh de xuat cho MVP:** Timeout manual accept la config theo service.

Gia tri mac dinh de xuat:

- Ride: 15 giay moi offer wave.
- Food: 20 giay moi offer wave.

Ly do:

- Ride can nhanh, thong tin quyet dinh don gian hon.
- Food can doc gia tri mon, outlet, delivery fee va khoang cach nen cho them vai giay.
- Tat ca gia tri phai nam trong policy/config, khong hard-code.

## ADR-027 - Driver auto-accept

**Quyet dinh:** Ho tro ca manual accept va auto-accept; driver co the bat/tat auto-accept.

Auto-accept can co guardrail:

- Driver dang online va available.
- Khong co active offer/chuyen/don xung dot.
- Dung service/vehicle ma driver da bat.
- Nam trong max pickup distance/ETA neu driver cau hinh.
- Khong vi pham fraud/risk, subscription/platform-fee hoac region policy.
- Voi Food, phai thoa direct bank transfer/prepaid policy; COD khong co trong P0.

Khi co nhieu driver auto-accept hop le, Matching Engine chon mot driver co score tot nhat, lock driver va assign. Khong tao tinh huong nhieu driver cung "auto accept" mot don.

## ADR-028 - Cancellation before match

**Quyet dinh:** Khach huy Ride/Food truoc khi matched khong anh huong P0 risk lock. Trust Engine day du lam sau P0.

## ADR-029 - Direct Food prepaid confirmation

**Quyet dinh:** Food prepaid QR/chuyen khoan la thoa thuan truc tiep giua customer va driver.

He thong khong dung payment gateway va khong xac nhan tien thay hai ben. Tuy nhien, app can co luong ghi nhan trang thai va payment proof bat buoc de ho tro van hanh, fraud/risk va dispute.

Flow de xuat:

- Sau khi matched, app hien QR chuyen khoan dong theo don/so tien neu co thong tin ngan hang cua driver.
- Customer co the bam "Da chuyen tien".
- Customer phai upload hinh anh bill/bien lai da chuyen.
- Driver co the bam "Da nhan tien" sau khi tu kiem tra tai khoan/trao doi voi customer.
- Don Food prepaid chi nen cho driver tiep tuc buoc dat mon khi da co trang thai driver xac nhan da nhan tien, tru khi policy cho phep override.
- Tat ca thao tac va evidence phai co audit trail.

Luu y:

- Anh bill/bien lai khong duoc xem la xac nhan ngan hang chinh thuc.
- Onway van khong thu ho, khong giu tien va khong dam bao giao dich ngan hang.
- Evidence chi dung de ho tro dispute, fraud/risk va customer support.

## ADR-030 - Firebase Auth with ViHAT OTP

**Quyet dinh:** Dung ViHAT lam OTP provider. Firebase Auth khong dung phone auth truc tiep.

Flow de xuat:

1. App gui phone number ve backend.
2. Backend tao OTP challenge va gui SMS qua ViHAT.
3. User nhap OTP.
4. Backend verify OTP.
5. Backend tao Firebase custom token.
6. App sign in Firebase bang custom token.
7. App goi GraphQL/WebSocket bang Firebase ID token.
8. Backend verify Firebase ID token va map sang user/customer/driver/admin noi bo.

## ADR-031 - Driver background location

**Quyet dinh:** Driver App can background location.

Ap dung khi:

- driver online/available;
- dang matching;
- dang thuc hien Ride/Food;
- dang lam future Mission can GPS evidence, neu feature nay duoc bat sau P0.

Can co consent, UI trang thai ro rang, battery strategy va data retention policy.

## ADR-032 - Dynamic VietQR

**Quyet dinh:** QR chuyen khoan dung dynamic VietQR theo don/so tien khi co du thong tin ngan hang cua tai xe.

QR nen encode:

- bank/account cua driver;
- amount;
- transfer content/reference gan voi ride/order id;
- optional checksum/reference de phuc vu doi soat tranh chap.

Onway van khong thu ho va khong giu tien Ride/Food.

## ADR-033 - Flutter mobile structure

**Quyet dinh:** Customer App va Driver App nam trong monorepo va reuse shared packages/components.

Huong de xuat:

- Tach hai app deploy rieng: `mobile-user` va `mobile-driver`.
- Dung shared packages cho design system, networking, auth, maps, location, models va utilities.
- Khong tron hai app thanh mot binary neu trai nghiem/phat hanh/permission khac nhau.

## ADR-034 - Admin Portal API access

**Quyet dinh:** Admin Portal goi GraphQL truc tiep, khong dung BFF rieng trong MVP.

Can co:

- RBAC/permission guard o backend;
- audit trail cho mutation nhay cam;
- schema/resolver rieng cho admin domain khi can;
- Firebase/admin role mapping ro rang.

## ADR-035 - Admin Portal day 1

**Quyet dinh:** Admin Portal can day du cho MVP day 1, khong phu thuoc vao script/manual DB cho luong van hanh chinh.

Admin Portal MVP toi thieu can co:

- region/polygon;
- service/vehicle rollout;
- pricing/policy config;
- driver verification;
- platform fee verification;
- restaurant/menu/outlet management;
- ride/food monitoring;
- complaint/fraud/dispute;
- audit log.

Mission, Community Truth, advertising va AI Restaurant Operations la post-launch/future, khong bat buoc trong Admin Portal P0.

## ADR-036 - AI OCR menu after P0

**Quyet dinh:** AI OCR/menu extraction khong nam trong P0 launch. Food supply P0 la admin-first: admin/operator tao brand, outlet, menu, modifier, override va publish catalog.

Scope future:

- OCR anh menu;
- goi y brand/outlet/menu item/modifier/price;
- image quality checks co ban;
- admin/operator review truoc khi publish neu confidence chua du;
- dua du lieu vao Community Truth va verification flow.

P0 chi can schema va UI co the mo rong de gan media/evidence vao menu item/outlet neu sau nay dung OCR.

---

# 12. Cau hoi architecture con mo sau ngay 11/09/2026

## 12.1 Can chot truoc khi scaffold backend

1. **Typed client generation:** Co generate typed GraphQL client cho React/Flutter ngay tu dau khong?

## 12.2 Co the chot sau nhung nen nam trong thiet ke

1. **Observability:** CloudWatch only hay them Sentry/OpenTelemetry ngay MVP?
2. **Admin RBAC matrix:** Vai tro admin/operator cu the va permission tung module.
3. **Rate limit/abuse protection:** Gioi han OTP, GraphQL mutation, WebSocket connect/location spam.
4. **Device identity:** Co thu thap device id/fingerprint o MVP khong, muc nao phuc vu fraud.
5. **Data retention:** Chat retention da chot 1 tuan; GPS, evidence, KYC, fraud, complaint va audit log con can chot thoi gian giu rieng.
6. **Legal/privacy controls:** Consent background location, AI profiling, export/delete data.
7. **Release process mobile:** TestFlight/Google Play internal testing, versioning, force update.
8. **Map cost controls:** HERE quota, route calculation caching, fallback khi map/geocoding loi.

---

# 13. Quyet dinh ha tang va backend bo sung ngay 11/09/2026

## ADR-037 - Database access layer

**Quyet dinh:** Dung Prisma lam database access layer chinh.

Luu y voi PostgreSQL/PostGIS:

- Prisma dung tot cho model quan he, CRUD, transaction va migration thong thuong.
- Cac truy van PostGIS phuc tap co the dung raw SQL co kiem soat qua Prisma.
- Can chuan hoa cach viet raw SQL cho region polygon, distance, geofence va nearest-driver query.
- Khong nen de PostGIS logic roi rac trong resolver; nen gom vao repository/service cua module `region`, `matching` va `location`.

## ADR-038 - Queue strategy

**Quyet dinh:** Dung BullMQ + Redis cho MVP.

Dung cho:

- notification jobs;
- fraud/risk checks;
- evidence processing;
- async audit/analytics events neu can.
- future AI OCR/menu QA neu feature duoc bat;
- future mission processing neu feature duoc bat.

Ly do:

- Da co Redis trong stack.
- Don gian hon SQS/EventBridge cho MVP.
- De debug khi backend con la modular monolith.

Sau nay co the chuyen mot so job sang SQS/EventBridge khi can scale hoac can decouple manh hon.

## ADR-039 - Backend compute

**Quyet dinh:** Backend MVP deploy tren EC2 binh thuong.

Huong de xuat:

- Chay app bang Docker Compose hoac process manager nhu PM2 trong giai doan rat dau.
- Reverse proxy bang Nginx/Caddy.
- TLS qua ACM + Load Balancer neu co ALB, hoac Let's Encrypt neu di thang EC2.
- Logs day ve CloudWatch.
- Secrets dung AWS Secrets Manager/SSM hoac file env duoc quan ly chat trong giai doan dau.

Luu y:

- EC2 simple giup launch nhanh, nhung can discipline ve deploy, backup config, monitoring va rollback.
- Khi traffic tang, co the migrate sang ECS Fargate ma khong doi domain architecture neu app/container duoc dong goi tot.

## ADR-040 - Simple EC2 CI/CD

**Quyet dinh:** Dung GitHub Actions cho CI/CD simple, deploy len EC2 qua SSH hoac copy artifact.

Huong MVP de xuat:

- CI chay lint, typecheck, test va build.
- CD dung GitHub Actions SSH vao EC2 de pull/build/restart hoac copy artifact.
- Can co deploy script idempotent: backup current release, install deps/build, run migration theo policy, restart service, health check.
- Rollback toi thieu: giu lai release truoc va restart lai neu health check fail.

## ADR-041 - GraphQL schema style

**Quyet dinh:** Dung NestJS GraphQL code-first.

Ly do:

- Phu hop voi NestJS/TypeScript va modular monolith.
- Giam duplication giua resolver, DTO/input type va schema.
- Toc do build MVP nhanh hon schema-first.
- Van co the generate `schema.gql` lam contract cho frontend.

Quy uoc:

- Backend generate GraphQL schema tu code trong CI.
- React Admin co the dung GraphQL Code Generator de tao typed hooks/types.
- Flutter co the dung generated schema + query documents de tao typed models/client neu team chot tool.
- Schema generated phai duoc review khi co thay doi breaking.

## ADR-042 - S3 media/evidence access

**Quyet dinh:** Phan loai media tren S3 theo muc do nhay cam.

Private signed URL:

- KYC/driver documents;
- payment bill/transfer receipt;
- fraud/complaint evidence;
- future mission raw evidence;
- GPS/device-related evidence;
- anh co thong tin ca nhan hoac thong tin tranh chap.

Public/CDN asset:

- restaurant public image da duoc duyet;
- menu image/processed menu asset khong nhay cam;
- landing/public marketing asset;
- icon/static content.

Tat ca upload ban dau nen vao private bucket/prefix. Chi publish sang public/CDN sau khi da qua moderation/review/policy.

## ADR-043 - Food prepaid confirmation controls

**Quyet dinh:** Customer co nut xac nhan da chuyen tien; Driver co nut xac nhan da nhan tien.

Flow:

1. Sau khi matched, customer xem QR chuyen khoan dong theo don.
2. Customer chuyen tien truc tiep cho driver.
3. Customer bam "Da chuyen tien" va bat buoc upload hinh bill/bien lai/payment proof.
4. Driver tu kiem tra/tro chuyen voi customer.
5. Driver bam "Da nhan tien".
6. Sau khi driver xac nhan, don moi di tiep sang buoc driver dat mon.

Ghi chu:

- Anh bill/bien lai la evidence, khong phai xac nhan ngan hang chinh thuc.
- Onway khong thu ho, khong giu tien va khong bao dam giao dich ngan hang.
- State transition va evidence phai co audit trail.

## ADR-044 - Customer-driver chat in P0

**Quyet dinh:** Customer-driver chat la P0 cho active Ride/Food, ho tro text va image.

Kien truc de xuat:

- GraphQL dung cho query history, room metadata va mutation gui tin nhan.
- WebSocket Gateway dung de day `chat.message_created`, `chat.message_delivered`, `chat.message_read` va `chat.room_closed`.
- Anh chat upload qua media/evidence service vao S3 private prefix, truy cap bang signed URL.
- Chat room chi mo cho participant cua active Ride/Food va admin/operator co quyen hop le.
- Chat retention P0 la 1 tuan, tru khi message/evidence duoc gan vao complaint/dispute can preserve theo policy rieng.

Ghi chu:

- P0 khong can voice call trong app hoac an so dien thoai.
- Client phai handle offline/retry va refetch history khi WebSocket reconnect co sequence gap.
