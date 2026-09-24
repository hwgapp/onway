# Design System Component Catalog

File này mô tả các thành phần nên yêu cầu Claude Design thiết kế. Không phải project nào cũng cần tất cả. Codex chọn nhóm component phù hợp theo `SDLC_CONFIG.md`, PRD và screen inventory.

Nguồn kinh nghiệm tổng hợp từ các project mẫu:

- Marketplace/mobile service app: card, profile, map/list, booking status, bottom sheet, chat, notification.
- Game app: HUD, booster, board/tile, reward, result, tutorial, store creative.
- Learning app: answer option, feedback, hint, progress, lesson card, report, parent-safe settings.
- SaaS/admin app: shell, table, filter, form, drawer, timeline, attachment, audit, finance/status components.

## 1. Component Spec Format

Claude Design phải mô tả mỗi component theo format:

```text
Component name:
Purpose:
Anatomy:
Variants:
States:
Responsive behavior:
Accessibility:
Usage rules:
Do / Don't:
Used in screens:
Implementation notes:
```

## 2. Foundation Tokens

| Group | Required | Notes |
| --- | --- | --- |
| Color roles | Yes | background, surface, text, border, primary, secondary, accent, success, warning, danger, info |
| Typography | Yes | display, h1-h3, body, caption, button, numeric/table if needed |
| Spacing | Yes | scale and layout gaps |
| Radius | Yes | controls, cards, dialogs/sheets |
| Border/elevation | Yes | define flat/bordered/shadow rules |
| Motion | Yes | duration/easing for press, transition, loading, success/failure |
| Icon style | Yes | stroke/fill, size, usage, labels/tooltips |
| Imagery/illustration | Optional | required for game, learning, landing, onboarding |
| Sound/haptic | Optional | required for game/learning/mobile if used |
| Breakpoints/safe area | Yes for UI | mobile/tablet/desktop, notch/home indicator |

## 3. Core UI Components

These are default for most apps.

| Component | Variants | States | Notes |
| --- | --- | --- | --- |
| App Shell / Screen Shell | mobile, tablet, desktop, admin | loading, offline, no permission | Defines page/screen structure |
| Header / App Bar / Top Bar | standard, large title, compact, admin | scrolled, action present | Include back/search/action behavior |
| Navigation | bottom nav, tabs, sidebar, nav rail, breadcrumbs | active, disabled, badge count | Choose by platform |
| Button | primary, secondary, tonal, outline, ghost, destructive, icon | default, hover, pressed, focus, loading, disabled, success | One clear primary action per screen unless PRD says otherwise |
| Icon Button | toolbar, row action, floating | hover, pressed, disabled | Must include tooltip/label on desktop |
| Text Link | inline, standalone | default, hover, visited, disabled | For legal/help/navigation |
| Card / Panel | item card, summary card, detail panel | hover, selected, disabled, empty | Avoid nested cards |
| List Row | leading icon/avatar, metadata, action | selected, swipe/action, disabled | Mobile and dense admin variants |
| Chip / Tag | filter, selected, removable, status-like | selected, disabled, loading | Do not replace status badge unless intended |
| Badge / Status Badge | neutral, success, warning, danger, info | soft, outline, filled | Map all business statuses |
| Progress | bar, ring, steps, checklist | active, complete, blocked | Include label like `3/5` when useful |
| Divider / Section Header | simple, sticky, grouped | - | For scanability |
| Tooltip | text, rich | hover/focus | Required for icon-only actions |

## 4. Form And Input Components

Required if app has forms, filters, onboarding, settings, admin or checkout/paywall.

| Component | Variants | States | Notes |
| --- | --- | --- | --- |
| Text Field | single line, multiline, search | focus, error, disabled, loading | Include helper/error text |
| Number Input | integer, decimal, stepper | error, disabled | Useful for quantity, age, amount |
| Money Input | currency-specific | error, disabled | Required for finance/IAP/admin pricing |
| Select / Combobox | single, multi, searchable | empty, loading, disabled | Include long-list behavior |
| Date / Time Picker | date, time, range | unavailable, selected | Required for booking/schedule/report |
| Checkbox / Radio | single, group | checked, indeterminate, disabled | |
| Switch / Toggle | on/off | disabled, loading | |
| Slider / Stepper | range, value | disabled | For settings/game/quantity |
| File / Image Upload | camera, gallery, drag-drop, progress | uploading, failed, success | Required for POD/OCR/avatar/assets |
| Entity Picker | user, product, customer, item, location | empty, loading, selected | Required for admin/SaaS |
| Form Section | collapsible, grouped | error summary | For long forms |
| Validation Summary | inline, top banner | warning/error | Required for complex forms |

## 5. Feedback, State And Overlay Components

Every project should define these patterns clearly.

| Component | Variants | States | Notes |
| --- | --- | --- | --- |
| Loading / Skeleton | list, card, screen, inline | shimmer/static | Avoid layout shift |
| Empty State | first-use, filtered-empty, no-data | action/no action | Clear next step |
| Error State | recoverable, fatal, validation | retry, report | Must include useful action |
| Offline State | banner, full screen, sync queue | reconnecting, queued | Required for offline apps |
| No Permission / Locked State | role locked, feature locked, paywall | request/upgrade | |
| Toast / Snackbar | success, info, warning, error | timeout, action | |
| Banner / Alert | info, warning, danger, success | dismissible, persistent | |
| Dialog / Modal | confirm, form, critical action | loading, error | Critical actions may require reason |
| Bottom Sheet | action sheet, picker, detail, form | expanded, loading | Mobile-first pattern |
| Drawer / Side Panel | detail, edit, timeline | loading, dirty form | Admin/SaaS pattern |
| Popover / Menu | actions, filter, help | open, disabled items | |

## 6. Data Display And Admin Components

Required for SaaS/admin/CMS/operations-heavy apps.

| Component | Variants | States | Notes |
| --- | --- | --- | --- |
| Data Table | basic, dense, selectable, editable | loading, empty, error | Sticky header, pagination, sort/filter |
| Filter Bar | simple, advanced, saved filters | active, dirty | |
| Toolbar | table/page actions | disabled, overflow | |
| Pagination | page, cursor, load more | loading, end | |
| KPI / Stat Tile | number, trend, warning | loading, no data | |
| Timeline / Activity Log | audit, status history, comments | empty, loading | |
| Attachment Viewer | image, PDF, document | loading, error | |
| Document/PDF Preview | preview, print, export | loading, failed | |
| Import Wizard | upload, validate, preview, commit | errors, partial success | |
| Export / Print Action | CSV, Excel, PDF | queued, ready, failed | |
| Permission/Sensitive Action Modal | reason required, confirm | error, loading | |

## 7. Mobile App Patterns

Required for most iOS/Android apps.

| Component | Variants | States | Notes |
| --- | --- | --- | --- |
| Safe Area Layout | phone, tablet | keyboard open | |
| Bottom Action Bar | single CTA, dual action | loading, disabled | Avoid home indicator overlap |
| Bottom Navigation | 3-5 items | active, badge, disabled | |
| Pull To Refresh | list/detail | refreshing, failed | |
| Swipe Action | list row actions | confirm/destructive | |
| Floating Action Button | primary quick action | hidden, disabled | Optional |
| Permission Prompt Explainer | camera, location, notification, ATT | denied, limited | Required before OS prompt if sensitive |
| Sync Status Chip | synced, queued, failed | retry | Offline apps |

## 8. Commerce, Monetization And Growth Components

Enable only if project uses ads/IAP/subscription/paywall.

| Component | Variants | States | Notes |
| --- | --- | --- | --- |
| Paywall | modal, full screen, inline lock | loading, purchase failed, restored | Must show benefits and plan terms |
| Plan Card | monthly, yearly, lifetime, free | selected, best value | |
| Purchase / Restore Button | primary, restore | loading, error, success | |
| Feature Lock | lock card, blurred content, banner | upgrade action | |
| Ad Placement Container | rewarded, interstitial trigger, banner | loading, unavailable, capped | No misleading UI |
| Offer Banner | promo, trial, limited time | dismissed, expired | Use carefully |
| Referral / Share CTA | invite, share result | copied/shared | Optional |

## 9. Game Components

Enable for game projects.

| Component | Variants | States | Notes |
| --- | --- | --- | --- |
| Loading Screen | first load, content download, offline | progress, retry | |
| Home Entry / Level Card | normal, locked, new, completed | selected, disabled | |
| Gameplay HUD | timer, moves, objective, score | warning, paused | |
| Board / Tile / Slot | grid, shelf, draggable, locked | selected, valid, invalid, clearing | |
| Booster Button / Dock | available, empty, locked, ad-rewarded | cooldown, disabled | |
| Combo / Streak Strip | normal, milestone | animated | |
| Pause Popup | resume, restart, settings | confirm | |
| Result Popup | win, fail, last level | rewards, CTA | |
| Reward Flyout | coin, star, item | collected | |
| Daily Reward | day streak, claimable, claimed | missed, premium | |
| Mission Card | starter, daily, event | progress, claimable | |
| Leaderboard | all-time, weekly, friends | loading, empty | |
| Collection Grid | item, set, locked | complete, new | |
| Tutorial Focus | spotlight, pointer, coach mark | next, skip | |
| Store Screenshot Frame | marketing/store asset | localized | Optional but useful |

## 10. Learning / Education Components

Enable for learning/math/language/content apps.

| Component | Variants | States | Notes |
| --- | --- | --- | --- |
| Lesson Card | concept, example, quick check | locked, complete | |
| Question Container | multiple choice, numeric, drag-drop, ordering, matching | answered, reviewing | |
| Answer Option | text, image, number, tile | selected, correct, wrong, disabled | |
| Feedback Banner | correct, wrong, hint, explanation | retry, continue | No shame language |
| Hint Panel | level 1/2/3 hint, AI hint | loading, exhausted | |
| Explanation Steps | step list, math block | expanded/collapsed | |
| Progress Map / Journey | topic, skill, level | locked, needs review, mastered | |
| Badge / Achievement | earned, locked, new | claimable | |
| Report / Mastery Card | skill, topic, child profile | loading, no data | |
| Parent Gate / Parent Area | math question, PIN, confirm | failed, locked | If kids/payment/settings |
| Audio Control | play, pause, replay, speed | loading, disabled | For young learners |

## 11. AI / OCR / Assistant Components

Enable for AI products or AI features.

| Component | Variants | States | Notes |
| --- | --- | --- | --- |
| Prompt Input | text, voice, image | sending, disabled | |
| Chat / Conversation | user, assistant, system, tool result | streaming, retry, failed | |
| Image Capture / OCR Review | crop, rotate, confirm text | processing, low confidence | |
| AI Response Card | answer, steps, sources, confidence | partial, failed | |
| Quota Meter | daily, monthly, plan limit | near limit, exhausted | |
| Safety / Unclear Result Notice | low confidence, unsupported | ask user confirm | |
| History Item | saved, deleted, shared | empty | |

## 12. Map / Location / Booking Components

Enable for service, logistics, travel, marketplace and location apps.

| Component | Variants | States | Notes |
| --- | --- | --- | --- |
| Map Canvas | interactive, static, approximate | loading, no permission | |
| Map Pin / Cluster | user, provider, job, approximate | selected, unavailable | |
| Address Picker | saved, search, current location | no permission, geocode failed | |
| Schedule Picker | date, time slot, range | unavailable, full | |
| Booking / Job Card | requested, accepted, in progress, done | cancelled, attention | |
| Status Header | workflow state | warning/error | |
| Route / Stop List | pickup/dropoff/checkpoint | complete, current, failed | |
| Contact / Chat Entry | call, message, support | disabled, masked | |

## 13. Content / CMS Components

Enable for apps with admin/CMS/content operations.

| Component | Variants | States | Notes |
| --- | --- | --- | --- |
| Content Editor | rich text, blocks, structured fields | dirty, validation error | |
| Version / Publish Status | draft, review, published, archived | rollback | |
| Preview Frame | mobile, tablet, web | loading, invalid | |
| Review Queue Item | pending, approved, rejected | assigned, overdue | |
| Asset Manager | image, audio, file | uploading, missing | |
| Config Panel | remote config, feature flags | unsaved, invalid | |

## 14. Legal / Settings / Utility Components

Common for release-ready apps.

| Component | Variants | States | Notes |
| --- | --- | --- | --- |
| Settings List | grouped, detail row, toggle | disabled | |
| Account/Profile Card | avatar, child profile, business profile | editing, locked | |
| Language Picker | list, segmented | selected | |
| Privacy / Terms Page | legal, webview, embed | loading, versioned | |
| Data Deletion / Support Entry | form, mail link | submitted | |
| App Update / Maintenance Screen | optional, forced | retry | |
| About / Version Info | simple, debug | copy version | |

## 15. Component Priority Guide

| Project Type | P0 Components |
| --- | --- |
| Simple utility | Core UI, form/input, feedback states, settings, paywall if monetized |
| Learning app | Core UI, learning components, progress/report, audio, parent/paywall if needed |
| Game | Game components, reward/progress, settings, monetization if used |
| AI app | Core UI, AI/chat/OCR, quota/paywall, privacy states |
| SaaS/admin | Admin shell, table/filter/form, drawer/timeline/upload, permission/audit |
| Marketplace/service | Core UI, cards/profile, booking/job, map/location, chat/notification, paywall if needed |

## 16. Claude Design Output Checklist

- [ ] Component catalog selected for this project.
- [ ] Every selected component has anatomy, variants and states.
- [ ] Components map to screen inventory.
- [ ] Critical states are included: loading, empty, error, offline, no permission, locked/paywall.
- [ ] Accessibility rules defined.
- [ ] Responsive behavior defined.
- [ ] Implementation notes clear enough for ORCA task breakdown.
