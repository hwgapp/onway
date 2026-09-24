# Design System Requirements

## Tokens

- Color: include brand red `#E22240`, brand charcoal `#302F2F`/`#2F2E2E`, neutral/background/surface/text/border, semantic success/warning/danger/info. Red must not be the only signal for danger/error.
- Typography: define mobile Customer/Driver hierarchy and dense Admin/table typography. Must handle Vietnamese text.
- Spacing: define mobile safe-area spacing, bottom action bars, map overlays, dense admin table spacing.
- Radius: controls/cards/dialogs/sheets; keep operational UI compact and professional.
- Motion: fast, restrained, useful for job status, matching, payment proof, upload and success/error feedback.
- Elevation: map overlays, bottom sheets, admin drawers, modals and evidence viewers.
- Asset: include Onway logo SVG/PNG paths, full wordmark, compact/symbol variant guidance, app icon guidance and favicon/web usage.

## Components

Claude Design phải dùng `06-design-system-component-catalog.md` để chọn component phù hợp với archetype dự án.

Tối thiểu mọi project có UI cần:

- App/screen shell.
- Navigation.
- Button/action system.
- Form/input basics.
- Card/list/tile pattern.
- Status/badge/label system.
- Dialog/bottom sheet/popover nếu platform cần.
- Loading/empty/error/offline/no-permission/paywall states nếu phù hợp.
- Toast/snackbar/inline feedback.
- Progress/stepper nếu flow nhiều bước.

Project có admin/table-heavy, game, learning, AI, payment, map, upload... phải bật thêm component domain tương ứng trong catalog.

For Onway P0, Claude Design must include these domain groups from the catalog:

- Core UI.
- Forms and inputs.
- Feedback/state/overlays.
- Data display and admin components.
- Mobile app patterns.
- Map/location/booking components.
- Content/CMS components for Food catalog.
- Legal/settings utility components.
- Upload/media/evidence components.
- Brand/logo asset usage.

## Required Deliverable From Claude Design

Claude Design phải cung cấp design system đủ để implementation không phải tự chế style:

- Token source: màu, typography, spacing, radius, border, shadow/elevation, motion, z-index nếu cần.
- Component library: component name, variants, states, anatomy, usage rules.
- Platform notes: mobile/web/admin/game nếu có nhiều platform.
- Accessibility rules: contrast, touch target, dynamic type/text scaling, reduced motion.
- Asset guidance: icon, illustration, image, sound/motion nếu liên quan.

## Implementation Handoff

Mỗi component nên có:

| Component | Required? | Variants | States | Used In Screens | Implementation Notes |
| --- | --- | --- | --- | --- | --- |
| Logo / Brand Mark | Core | full wordmark, compact symbol, monochrome, light/dark usage | normal, disabled/fallback/loading asset | splash, app header, landing, admin login/sidebar | Use `/Users/vod/Documents/ONW/design/logo.svg` as source |
| App Icon Candidate | Core | customer, driver, admin/favicon if needed | normal | app stores, launcher, favicon | Should derive from logo symbol, not long wordmark |
| Button / Action System | Core | primary, secondary, outline, ghost, destructive, icon | default, pressed, loading, disabled, success/error | all screens | Primary likely brand red, but danger must be distinct |
| Map Canvas / Overlay | Core | customer, driver, admin region editor | loading, no permission, offline, selected | Ride/Food/map/admin region | HERE Maps style must fit brand |
| Job / Order Status Header | Core | Ride, Food, driver, customer | requested, matching, accepted, active, issue, complete, cancelled | Ride/Food flows | Status must be readable at a glance |
| Payment Proof Upload | Core | customer upload, driver/admin review | empty, uploading, failed, submitted, verified/rejected | payment proof screens, admin cases | Evidence-sensitive UI |
| Admin Data Table / Filter | Core | dense, selectable, editable | loading, empty, error, filtered | admin screens | No decorative card-heavy layout |

## Accessibility

- Contrast: logo and brand red must meet contrast requirements when used for text/CTA; provide alternate dark/light usages.
- Touch target: mobile controls at least platform-standard touch size, especially driver accept/reject and payment confirmation actions.
- Dynamic type: Vietnamese labels and long status text must not overflow.
- Reduced motion: matching/loading/route animations must respect reduced motion.
