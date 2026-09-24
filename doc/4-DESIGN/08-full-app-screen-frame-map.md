# Full App Screen / Frame Map

Tài liệu này bung `S-001...S-021` từ PRD thành danh sách màn hình/frame chi tiết để đưa Claude Design thiết kế UI Workflow.

Quy ước:

- `Screen ID` trong PRD vẫn là container nghiệp vụ lớn.
- `Frame ID` dưới đây là frame/mockup cụ thể cần thiết kế.
- Đây là design handoff, không tự thêm business scope mới. Nếu frame chỉ là permission, empty, error, modal, sheet hoặc drawer thì vẫn cần thiết kế vì ảnh hưởng implementation.
- Frame name khi export nên dùng format: `<Frame ID> - <Frame Name> - <Platform>`.

## Summary

| App / Surface | Main PRD Screens | Suggested UI Frames | Notes |
| --- | ---: | ---: | --- |
| Customer App | 10 | 68 | Bao gồm auth/account, Ride, Food, chat, rating/report, history/case tracking và common states |
| Driver App | 7 | 60 | Bao gồm onboarding, platform fee, online/jobs, Ride/Food jobs, chat, appeal, history/case tracking và settings |
| Admin Portal | 6 | 77 | Bao gồm dashboard, region/polygon, policy, driver ops, finance proof, catalog, complaint/fraud, evidence/audit |
| Landing Web | 0 PRD screen riêng | 11 | Cần thiết cho public web/app download/driver acquisition/legal/contact |
| Total | 23 counted by app usage | 216 | `S-015 Chat` dùng chung Customer + Driver nên PRD unique vẫn là 21 |

## Customer App

| Frame ID | PRD Screen | Frame Name | Type | Required States / Variants | Primary Flow |
| --- | --- | --- | --- | --- | --- |
| C-000 | Common | Splash / launch | Screen | loading, force update | App start |
| C-001 | F-001 | Phone login | Screen | default, validation error, rate limited | Auth |
| C-002 | F-001 | OTP verification | Screen | default, invalid OTP, resend cooldown | Auth |
| C-003 | F-001 | Basic profile setup | Screen | default, validation error | Auth |
| C-004 | Common | Location permission | Screen | rationale, denied, limited | App start |
| C-005 | Common | Notification permission | Screen | rationale, denied | App start |
| C-006 | S-001 | Home / service selector | Screen | default, loading, region unavailable, offline | UF-001, UF-002 |
| C-007 | S-001 | Home search/service empty | State frame | no active region, no service | UF-001, UF-002 |
| C-008 | Common | Notification center | Screen | empty, list, unread | Push baseline |
| C-009 | Common | Account / settings | Screen | default | Account |
| C-010 | Common | Profile and phone visibility settings | Screen | default, validation error | Account |
| C-011 | Common | Privacy / consent settings | Screen | default, export/delete request entry | Account |
| C-012 | S-002 | Ride request map | Screen | default, no permission, no region | UF-001 |
| C-013 | S-002 | Pickup address search | Sheet | search, loading, no result, error | UF-001 |
| C-014 | S-002 | Dropoff address search | Sheet | search, loading, no result, outside-region warning | UF-001 |
| C-015 | S-002 | Map pin adjust pickup/dropoff | Screen | default, GPS weak, geocode failed | UF-001 |
| C-016 | S-002 | Vehicle type selection | Sheet | motorbike, car, unavailable vehicle | UF-001 |
| C-017 | S-002 | Ride price review | Sheet | default, route recalculating, pricing unavailable | UF-001 |
| C-018 | S-002 | Destination outside polygon warning | Dialog/Sheet | continue, go back | UF-001 |
| C-019 | S-003 | Ride matching | Screen | matching, timeout countdown | UF-001 |
| C-020 | S-003 | Driver rejected / searching next | State frame | retry wave | UF-001 |
| C-021 | S-003 | No driver found | Screen | retry, change pickup/dropoff, cancel | UF-001 |
| C-022 | S-003 | Ride cancel before match | Dialog | reason optional, confirm | UF-001 |
| C-023 | S-004 | Matched ride / driver assigned | Screen | driver profile, ETA, chat/call | UF-001 |
| C-024 | S-004 | Ride payment instructions | Sheet | bank/QR info, amount, copy action | UF-001 |
| C-025 | S-004 | Ride proof upload | Sheet | empty, uploading, failed, submitted | UF-001 |
| C-026 | S-004 | Ride proof rejected / supplement needed | Screen/Sheet | transfer more, upload again | UF-001 |
| C-027 | S-004 | Ride payment disputed | Screen | waiting review, contact support | UF-001 |
| C-028 | S-004 | Active ride - driver en route | Screen | default, connection issue | UF-001 |
| C-029 | S-004 | Active ride - driver arrived | Screen | waiting pickup, proof required warning | UF-001 |
| C-030 | S-004 | Active ride - in trip | Screen | route, ETA, chat/call | UF-001 |
| C-031 | S-004 | Ride completed summary | Screen | success, receipt/evidence summary | UF-001 |
| C-032 | S-004 | Ride issue/report entry | Sheet | categories, evidence optional | UF-005 |
| C-033 | S-005 | Food browse home | Screen | default, loading, unavailable region | UF-002 |
| C-034 | S-005 | Food outlet/brand search | Screen | search, empty, error | UF-002 |
| C-035 | S-005 | Outlet menu | Screen | default, closed, item unavailable, stale price warning | UF-002 |
| C-036 | S-005 | Menu item detail | Sheet | quantity, unavailable, price note | UF-002 |
| C-037 | S-006 | Food cart | Screen | default, item unavailable, price changed | UF-002 |
| C-038 | S-006 | Delivery address selection | Sheet | search, map pin, outside polygon warning | UF-002 |
| C-039 | S-006 | Food checkout price review | Screen | item total, delivery fee, transfer total | UF-002 |
| C-040 | S-007 | Food matching | Screen | matching, timeout | UF-002 |
| C-041 | S-007 | No Food driver found | Screen | retry, cancel | UF-002 |
| C-042 | S-007 | Food driver matched / payment instructions | Screen | QR/bank info, amount | UF-002 |
| C-043 | S-007 | Food proof upload | Sheet | empty, uploading, failed, submitted | UF-002 |
| C-044 | S-007 | Food proof rejected / disputed | Screen | supplement, upload again, support | UF-002 |
| C-045 | S-008 | Active Food - driver going to outlet | Screen | tracking, chat/call | UF-002 |
| C-046 | S-008 | Active Food - driver at outlet | Screen | ordering, waiting | UF-002 |
| C-047 | S-008 | Food change proposal | Screen/Sheet | pending, accept, reject, timer | UF-003 |
| C-048 | S-008 | Supplemental payment required | Sheet | amount, proof upload | UF-003 |
| C-049 | S-008 | Food proposal timeout | State frame | canceled/review needed | UF-003 |
| C-050 | S-008 | Active Food - delivering | Screen | route, ETA | UF-002 |
| C-051 | S-008 | Food delivered summary | Screen | success, rating entry | UF-002 |
| C-052 | S-009 | Rating after Ride/Food | Screen | 5 stars, quick tags | UF-001, UF-002 |
| C-053 | S-009 | Complaint/report form | Screen | category, description, evidence, validation error | UF-005 |
| C-054 | S-009 | Complaint submitted | Screen | case ref, next steps | UF-005 |
| C-055 | S-015 | Chat room | Screen | text, image, read status | UF-007 |
| C-056 | S-015 | Chat image upload failed | State frame | retry, remove | UF-007 |
| C-057 | S-015 | Chat offline / reconnecting | State frame | queued message | UF-007 |
| C-058 | S-015 | Chat closed / retention expired | State frame | read-only, evidence preserved notice | UF-007 |
| C-059 | Common | Activity / Ride & Food history | Screen | empty, filtered, loading | Account, UF-001, UF-002 |
| C-060 | Common | Ride history detail | Screen | completed, canceled, disputed | UF-001, UF-005 |
| C-061 | Common | Food order history detail | Screen | delivered, canceled, disputed | UF-002, UF-005 |
| C-062 | Common | Case / complaint list | Screen | empty, under review, finalized | UF-005 |
| C-063 | Common | Case / complaint detail | Screen | timeline, evidence, decision | UF-005 |
| C-064 | Common | Direct call confirmation | Sheet | call driver, call support, unavailable | UF-001, UF-002, UF-007 |
| C-065 | S-008 | Food customer cancel after driver ordered | Dialog/Sheet | warning, customer liable, continue | F-018 |
| C-066 | Common | Saved places / recent addresses | Screen | empty, edit, remove | UF-001, UF-002 |
| C-067 | Common | Data export/delete request | Screen | request, submitted, restricted by legal/audit | Privacy |

## Driver App

| Frame ID | PRD Screen | Frame Name | Type | Required States / Variants | Primary Flow |
| --- | --- | --- | --- | --- | --- |
| D-000 | Common | Splash / launch | Screen | loading, force update | App start |
| D-001 | F-001 | Phone login | Screen | default, validation error, rate limited | Auth |
| D-002 | F-001 | OTP verification | Screen | default, invalid OTP, resend cooldown | Auth |
| D-003 | S-010 | Driver profile setup | Screen | default, validation error | UF-004 |
| D-004 | S-010 | Service / vehicle selection | Screen | motorbike, car, both, unavailable | UF-004 |
| D-005 | S-010 | Document upload checklist | Screen | incomplete, uploading, failed | UF-004 |
| D-006 | S-010 | Identity document capture | Screen | front/back/selfie, rejected | UF-004 |
| D-007 | S-010 | Vehicle document upload | Screen | required-by-service, rejected | UF-004 |
| D-008 | S-010 | Bank/QR receiving info setup | Screen | default, validation error | UF-004 |
| D-009 | S-010 | Onboarding review pending | Screen | pending review | UF-004 |
| D-010 | S-010 | Onboarding rejected | Screen | reason, resubmit | UF-004 |
| D-011 | S-010 | Onboarding approved | Screen | next step platform fee/online | UF-004 |
| D-012 | S-011 | Platform fee package | Screen | unpaid, expired, active | UF-004 |
| D-013 | S-011 | Platform fee proof upload | Screen | empty, uploading, submitted, rejected | UF-004 |
| D-014 | S-011 | Platform fee active/validity | Screen | active, expiring soon, expired | UF-004 |
| D-015 | S-012 | Driver online home | Screen | offline, online, no jobs | UF-001, UF-002 |
| D-016 | S-012 | Service toggles / availability | Screen | Ride/Food, paused region, locked | UF-001, UF-002 |
| D-017 | S-012 | Job list / job cards | Screen | empty, loading, error | UF-001, UF-002 |
| D-018 | S-012 | Region unavailable / no service | State frame | no region, paused service | UF-006 |
| D-019 | S-013 | Ride offer received | Screen | countdown, final price, accept/reject | UF-001 |
| D-020 | S-013 | Ride offer accepted | Screen | success, navigate to pickup | UF-001 |
| D-021 | S-013 | Ride offer rejected / timeout | State frame | return to online | UF-001 |
| D-022 | S-013 | Ride pickup navigation | Screen | route, customer info, chat/call | UF-001 |
| D-023 | S-013 | Ride payment proof review | Screen | proof submitted, image viewer, confirm received | UF-001 |
| D-024 | S-013 | Ride money not received | Sheet | mark disputed, message customer | UF-001 |
| D-025 | S-013 | Ride arrived pickup | Screen | arrived action, wait timer | UF-001 |
| D-026 | S-013 | Ride start trip | Screen | start action locked until money confirmed | UF-001 |
| D-027 | S-013 | Ride in trip | Screen | route, complete action | UF-001 |
| D-028 | S-013 | Ride completed | Screen | earnings summary, rating prompt | UF-001 |
| D-029 | S-013 | Ride canceled / issue | Screen | reason, next steps | UF-001 |
| D-030 | S-014 | Food offer received | Screen | countdown, pickup/outlet, total, accept/reject | UF-002 |
| D-031 | S-014 | Food accepted / go to outlet | Screen | route to outlet, customer chat/call | UF-002 |
| D-032 | S-014 | Food payment proof review | Screen | proof, amount, confirm received | UF-002 |
| D-033 | S-014 | Food money not received | Sheet | disputed, message customer | UF-002 |
| D-034 | S-014 | At outlet / order items | Screen | menu snapshot, order checklist | UF-002 |
| D-035 | S-014 | Food change needed form | Screen | unavailable, price changed, modifier, note | UF-003 |
| D-036 | S-014 | Food proposal waiting customer | Screen | timer 5 min, call customer | UF-003 |
| D-037 | S-014 | Proposal accepted | State frame | continue purchase | UF-003 |
| D-038 | S-014 | Proposal rejected / timeout | Screen | cancel/review path | UF-003 |
| D-039 | S-014 | Supplemental payment pending | Screen | wait proof/confirmation | UF-003 |
| D-040 | S-014 | Food picked up | Screen | start delivery | UF-002 |
| D-041 | S-014 | Food delivering | Screen | route, ETA | UF-002 |
| D-042 | S-014 | Food delivered | Screen | completion summary | UF-002 |
| D-043 | S-014 | Food issue/cancel reason | Screen | outlet closed, customer unreachable, other | UF-002, UF-003 |
| D-044 | S-015 | Chat room | Screen | text, image, read status | UF-007 |
| D-045 | S-015 | Chat image upload failed | State frame | retry, remove | UF-007 |
| D-046 | S-015 | Chat offline / reconnecting | State frame | queued message | UF-007 |
| D-047 | S-019 | Driver locked notice | Screen | short reason, no sensitive evidence | UF-005 |
| D-048 | S-019 | Lock appeal form | Screen | reason, evidence, submitted | UF-005 |
| D-049 | Common | Earnings/history | Screen | empty, list, detail entry | Driver ops |
| D-050 | Common | Notifications | Screen | job/payment/chat/lock | Push baseline |
| D-051 | Common | Account/settings | Screen | profile, bank/QR, privacy, logout | Account |
| D-052 | Common | Help/support | Screen | FAQ/contact, case links | Support |
| D-053 | Common | Job history | Screen | Ride/Food filter, empty, list | Driver ops |
| D-054 | Common | Job history detail | Screen | completed, canceled, disputed | UF-001, UF-002, UF-005 |
| D-055 | Common | Case / complaint list | Screen | empty, under review, appeal, finalized | UF-005 |
| D-056 | Common | Case / complaint detail | Screen | timeline, evidence, decision | UF-005 |
| D-057 | Common | Direct call confirmation | Sheet | call customer, call support, unavailable | UF-001, UF-002, UF-007 |
| D-058 | Common | Proof/evidence image viewer | Modal | image zoom, expired signed URL | F-023 |
| D-059 | Common | Privacy / consent settings | Screen | location consent, evidence consent, device risk notice | Privacy |

## Admin Portal

| Frame ID | PRD Screen | Frame Name | Type | Required States / Variants | Primary Flow |
| --- | --- | --- | --- | --- | --- |
| A-000 | Common | Admin login | Screen | default, invalid, locked | Admin auth |
| A-001 | Common | OTP / second factor if enabled | Screen | default, error | Admin auth |
| A-002 | Common | Admin shell / sidebar | Layout | collapsed, expanded, unread badges | Admin baseline |
| A-003 | Common | Permission denied | Screen | no access | RBAC |
| A-004 | Common | Global search / command palette | Overlay | empty, results | Admin baseline |
| A-005 | S-016 | Dashboard overview | Screen | default, loading, error | Ops baseline |
| A-006 | S-016 | Marketplace health widgets | Section/frame | Ride/Food metrics, fraud alerts | Ops baseline |
| A-007 | S-016 | Live ops queue | Section/frame | no queue, queued items | Ops baseline |
| A-008 | S-016 | Recent activity/audit preview | Section/frame | empty, list | Ops baseline |
| A-009 | S-016 | Dashboard empty/new launch | State frame | no data | Ops baseline |
| A-010 | S-017 | Region list | Screen | active, paused, planned, empty | UF-006 |
| A-011 | S-017 | Region detail drawer | Drawer | view metadata, audit | UF-006 |
| A-012 | S-017 | Create city/region | Dialog/Form | validation error | UF-006 |
| A-013 | S-017 | Polygon editor map | Screen | draft, selected, map loading | UF-006 |
| A-014 | S-017 | Draw polygon | Mode frame | add points, close shape | UF-006 |
| A-015 | S-017 | Edit polygon vertices | Mode frame | drag, undo, invalid | UF-006 |
| A-016 | S-017 | Polygon overlap blocked | State frame | same service/vehicle overlap | UF-006 |
| A-017 | S-017 | Service/vehicle availability panel | Drawer/Form | Ride/Food, motorbike/car | UF-006 |
| A-018 | S-017 | Region lifecycle controls | Drawer/Form | Planned/Pilot/Active/Paused/Closed | UF-006 |
| A-019 | S-017 | Publish region config | Dialog | reason required, confirm | UF-006 |
| A-020 | S-017 | Pause/resume region | Dialog | reason required | UF-006 |
| A-021 | S-017 | Region publish conflict | State frame | version conflict | UF-006 |
| A-022 | S-018 | Pricing/policy config list | Screen | draft, published, loading | UF-006 |
| A-023 | S-018 | Ride pricing guardrails form | Screen/Form | validation error | UF-006 |
| A-024 | S-018 | Food delivery fee policy form | Screen/Form | validation error | UF-006 |
| A-025 | S-018 | Matching timeout/wave policy form | Screen/Form | validation error | UF-006 |
| A-026 | S-018 | Auto-lock/fraud threshold policy | Screen/Form | validation error | UF-005 |
| A-027 | S-018 | Policy publish confirmation | Dialog | reason required | UF-006 |
| A-028 | S-018 | Policy audit timeline | Drawer | actor/time/diff | UF-006 |
| A-029 | S-019 | Driver list | Screen | pending, active, locked, filtered | UF-004, UF-005 |
| A-030 | S-019 | Driver detail drawer | Drawer | profile, services, documents | UF-004 |
| A-031 | S-019 | KYC/document viewer | Drawer/Modal | image/PDF, approve/reject | UF-004 |
| A-032 | S-019 | Driver approval/rejection | Dialog | reason required | UF-004 |
| A-033 | S-019 | Platform fee proof review | Drawer | proof image, approve/reject | UF-004 |
| A-034 | S-019 | Driver service eligibility editor | Form | vehicle/service flags | UF-004 |
| A-035 | S-019 | Manual lock driver | Dialog | reason required | UF-005 |
| A-036 | S-019 | Auto-lock review queue | Screen | SLA, reason, severity | UF-005 |
| A-037 | S-019 | Driver appeal detail | Drawer | appeal text, evidence | UF-005 |
| A-038 | S-019 | Unlock driver | Dialog | reason required, role check | UF-005 |
| A-039 | S-019 | Driver audit timeline | Drawer | actor/time/action | UF-004, UF-005 |
| A-040 | S-020 | Food brand list | Screen | empty, search, inactive | Food catalog |
| A-041 | S-020 | Brand detail/editor | Screen/Drawer | draft, published | Food catalog |
| A-042 | S-020 | Outlet list | Screen | closed, active, missing data | Food catalog |
| A-043 | S-020 | Outlet detail/editor | Screen/Drawer | hours, address, region | Food catalog |
| A-044 | S-020 | Menu item list | Screen | missing price, conflict | Food catalog |
| A-045 | S-020 | Menu item editor | Drawer/Form | validation error | Food catalog |
| A-046 | S-020 | Outlet override editor | Drawer/Form | price/status override | Food catalog |
| A-047 | S-020 | Catalog conflict review | Screen | duplicate/conflict | Food catalog |
| A-048 | S-020 | Import/upload catalog placeholder | Screen/Modal | future/manual import note | Food catalog |
| A-049 | S-020 | Publish catalog changes | Dialog | reason required | Food catalog |
| A-050 | S-021 | Complaint/case queue | Screen | new, under review, appeal, finalized | UF-005 |
| A-051 | S-021 | Case detail | Screen/Drawer | service ref, participants, status | UF-005 |
| A-052 | S-021 | Evidence viewer | Modal | payment proof, chat image, complaint image | UF-005 |
| A-053 | S-021 | Payment proof dispute review | Screen/Drawer | conflicting evidence | UF-001, UF-002, UF-005 |
| A-054 | S-021 | Request user response | Dialog/Form | customer/driver, deadline | UF-005 |
| A-055 | S-021 | Fraud escalation | Dialog | category, severity, reason | UF-005 |
| A-056 | S-021 | Case decision form | Screen/Form | confirmed, rejected, finalized | UF-005 |
| A-057 | S-021 | Appeal review | Screen/Drawer | accept/reject appeal | UF-005 |
| A-058 | S-021 | Case audit timeline | Section/frame | immutable | UF-005 |
| A-059 | S-021 | Case finalized summary | Screen/State | decision, next steps | UF-005 |
| A-060 | Common | Media/evidence signed URL expired | State frame | reload, access denied | Evidence |
| A-061 | Common | Audit log search | Screen | filter, empty, export future note | Audit |
| A-062 | Common | Admin user / RBAC list | Screen | role list, viewer | RBAC |
| A-063 | Common | Admin user detail / role assignment | Drawer | permission matrix | RBAC |
| A-064 | Common | Sensitive action reason dialog | Dialog | required reason, validation | Admin baseline |
| A-065 | Common | Config version diff | Drawer | before/after | Admin baseline |
| A-066 | Common | Basic ops dashboard drilldown | Screen | Ride/Food/fraud metrics | Analytics |
| A-067 | Common | System health / queue status | Screen | degraded, normal | Ops baseline |
| A-068 | Common | Admin settings | Screen | profile, notifications, logout | Admin baseline |
| A-069 | Common | Empty/error/loading template | State frame | global admin states | Admin baseline |
| A-070 | Common | Finance proof queue | Screen | platform fee proofs, filtered, SLA | F-003 |
| A-071 | Common | Finance proof detail | Drawer | payment proof, driver profile, approve/reject | F-003, F-023 |
| A-072 | Common | Customer management light | Screen | search, customer detail, case-linked only | Support |
| A-073 | Common | Customer detail / history | Drawer | Ride/Food refs, complaints, evidence links | Support, UF-005 |
| A-074 | Common | Notification template/config baseline | Screen | job/payment/chat/lock templates | F-034 |
| A-075 | Common | Data/privacy request queue | Screen | export/delete requests, legal exceptions | Privacy |
| A-076 | Common | Data/privacy request detail | Drawer | user refs, decision, audit | Privacy |

## Landing Web

| Frame ID | PRD Screen | Frame Name | Type | Required States / Variants | Primary Flow |
| --- | --- | --- | --- | --- | --- |
| L-001 | Landing | Landing home hero | Section/Page | desktop, mobile | Public |
| L-002 | Landing | Customer value section | Section | Ride + Food | Public |
| L-003 | Landing | Driver acquisition section | Section | 0% commission, launch package | Driver acquisition |
| L-004 | Landing | How Onway works | Section | direct transfer/payment proof explained | Public trust |
| L-005 | Landing | Safety / dispute / connection model | Section | Onway as connector, legal-safe wording | Public trust |
| L-006 | Landing | App download / waitlist CTA | Section | iOS, Android, unavailable app links | Public |
| L-007 | Landing | FAQ | Section/Page | customer, driver | Public |
| L-008 | Landing | Footer / legal links | Section | privacy, terms, contact | Public |
| L-009 | Landing | Terms page | Page | public legal content placeholder | Legal |
| L-010 | Landing | Privacy page | Page | public data/privacy content placeholder | Legal/Privacy |
| L-011 | Landing | Contact/support page | Page | customer, driver, partner contact | Support |

## P0 Coverage Audit

| P0 Feature / Flow | Covered By Frames | Coverage |
| --- | --- | --- |
| Phone OTP/account | C-001...C-003, D-001...D-003, A-000...A-001 | Covered |
| Customer Ride request/matching/payment/trip | C-012...C-032, D-019...D-029, A-053 | Covered |
| Customer Food browse/cart/matching/payment/order | C-033...C-051, D-030...D-043, A-040...A-049, A-053 | Covered |
| Food change proposal / supplemental payment | C-047...C-049, D-035...D-039 | Covered |
| Food cancellation after driver ordered | C-065, D-043, A-050...A-059 | Covered |
| Driver onboarding/KYC/activation | D-003...D-014, A-029...A-039, A-070...A-071 | Covered |
| Region/polygon/service availability | C-006...C-018, D-015...D-018, A-010...A-021 | Covered |
| Pricing/policy/auto-lock config | A-022...A-028 | Covered |
| Chat/direct call | C-055...C-058, C-064, D-044...D-046, D-057 | Covered |
| Rating/report/complaint/fraud/appeal | C-052...C-054, C-062...C-063, D-047...D-048, D-055...D-056, A-050...A-059 | Covered |
| Evidence/media/audit | C-025, C-043, D-023, D-032, D-058, A-052, A-058, A-060...A-061, A-065 | Covered |
| Push notifications | C-008, D-050, A-074 | Covered |
| RBAC/admin permissions | A-002...A-004, A-062...A-064 | Covered |
| Analytics/basic ops dashboard | A-005...A-009, A-066...A-067 | Covered |
| Privacy/data request/legal pages | C-011, C-067, D-059, A-075...A-076, L-009...L-010 | Covered baseline |
| Landing/public acquisition | L-001...L-011 | Covered baseline |

## Explicitly Not Covered In P0

Các flow sau **không thiếu** mà đang bị loại khỏi P0 theo BRD/PRD:

- Wallet, cash/COD, payment gateway/escrow/Onway-held payment.
- Ride price negotiation/customer manual offer.
- Food delivery fee negotiation, tip.
- Merchant App.
- Ads, referral rewards, Mission, Community Truth, Trust full.
- AI OCR/menu extraction production.
- Grocery, parcel, shopping, corporate ride, cross-border.

## Claude Design Instructions For UI Workflow

Use `doc/4-DESIGN/system/` as the visual source of truth. Do not redesign the design system unless a frame exposes a missing component.

Required output:

1. `mockups/screen-map.md`: map every `Frame ID` above to a Claude frame/mockup name.
2. `mockups/flow-map.md`: show navigation through UF-001...UF-007 using the frame IDs above.
3. `mockups/state-coverage.md`: indicate which frames cover default/loading/empty/error/offline/no-permission/locked/success.
4. `mockups/frame-export-notes.md`: include export names, platform, viewport, and known gaps.
5. Visual mockups/frames for all P0 frame IDs above, prioritizing critical flow frames first:
   - Critical Customer: C-006, C-012...C-031, C-033...C-054, C-055.
   - Critical Driver: D-015...D-043, D-047...D-048.
   - Critical Admin: A-005, A-010...A-039, A-040...A-059.

Do not add these P0-excluded flows: wallet, cash/COD, payment gateway/escrow, Ride price negotiation/manual offer, Food delivery fee negotiation, tip, Merchant App, ads, referral rewards, Trust full, Mission, Community Truth or AI OCR production.
