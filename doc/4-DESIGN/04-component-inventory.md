# Component Inventory

| Component | Platform | Variants | Used By | Notes |
| --- | --- | --- | --- | --- |
| Logo / Brand Mark | Mobile/Web/Admin | full wordmark, compact symbol, monochrome, light/dark | Splash, login, header/sidebar, landing, app icon exploration | Source: `/Users/vod/Documents/ONW/design/logo.svg`; colors `#E22240`, `#302F2F`, `#2F2E2E` |
| App Icon / Favicon | Mobile/Web | customer app, driver app, admin/web favicon | App launcher, store, browser | Should derive from compact logo symbol, not full wordmark |
| App Shell / Screen Shell | Mobile/Web/Admin | customer, driver, admin, landing | All screens | Safe areas, keyboard, responsive layout |
| Navigation | Mobile/Web/Admin | bottom nav, tabs, sidebar, breadcrumbs | Customer/Driver/Admin | P0 routes from route map |
| Button / Action System | Mobile/Web/Admin | primary, secondary, outline, ghost, destructive, icon | All screens | Loading/disabled/success/error states |
| Map Canvas / Region Editor | Mobile/Admin | customer map, driver map, admin polygon editor | Ride/Food, Region Admin | HERE Maps style, active region boundaries |
| Address Picker | Mobile | pickup, dropoff, delivery address, current location | Ride/Food checkout | No permission/offline/geocode failed |
| Job / Order Card | Mobile/Admin | Ride, Food, offer, active, history | Matching, driver jobs, monitoring | State-heavy |
| Status Header / Timeline | Mobile/Admin | Ride lifecycle, Food lifecycle, complaint/fraud | Active Ride/Food, Admin cases | Clear state transitions |
| Payment Proof Upload / Viewer | Mobile/Admin | upload, review, accepted/rejected, case-linked | Customer proof, Driver/Admin review | Sensitive evidence, private media |
| Chat / Message Room | Mobile/Admin | text, image, admin view | Active Ride/Food, case review | Retention and closed-room states |
| Complaint / Case Form | Mobile/Admin | report form, evidence attach, category picker | Rating/report, complaint/fraud | Complaint does not equal fraud |
| Admin Data Table | Admin | dense, selectable, editable, filtered | Drivers, catalog, regions, complaints, audit | Sticky header, filters, pagination |
| Admin Drawer / Detail Panel | Admin | driver, order, complaint, evidence, audit | Admin workflows | Avoid nested cards |
| Catalog Editor | Admin | brand, outlet, menu, modifier, override | Food catalog | Draft/publish state |
| Policy Config Form | Admin | pricing, region, timeout, retention/risk config | Policy admin | Versioned, reason required |
| Audit Timeline | Admin | policy, case, driver, payment proof | Admin/review | Immutable-feeling history |

## Required Fields Per Component

Mỗi component trong inventory nên có:

- Purpose: component dùng để làm gì.
- Anatomy: gồm những phần nào.
- Variants: primary/secondary, compact/large, etc.
- States: default/pressed/hover/focus/loading/disabled/error/success/selected/empty.
- Tokens: màu, typography, spacing, radius, motion.
- Accessibility: touch target, keyboard, screen reader, contrast.
- Usage rules: khi nào dùng/không dùng.
- Screen usage: component xuất hiện ở screen/flow nào.
- Implementation priority: P0/P1/P2.
