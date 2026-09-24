# Claude Design Output Contract

File này quy định cách Claude Design phải output Design System và UI Workflow, để sau đó Codex cập nhật ngược vào SDLC và dùng cho implementation/task breakdown.

## 1. Required Output Packages

Claude Design phải output 2 package chính:

```text
Design System Package
UI Workflow Package
```

Không trộn lẫn hai phần này. Design system mô tả rule/component dùng lại. UI workflow mô tả từng màn hình/flow cụ thể.

## 2. Design System Package

### 2.1. Required Files

Khi đưa ngược vào repo, lưu vào:

```text
doc/4-DESIGN/system/
  README.md
  tokens.json
  design-system.md
  component-inventory.md
  component-state-matrix.md
  accessibility.md
  implementation-notes.md
  assets/
```

Nếu Claude Design chỉ xuất một artifact lớn, Codex phải tách/summarize về các file trên.

### 2.2. `tokens.json`

Nên có cấu trúc ổn định:

```json
{
  "color": {},
  "typography": {},
  "spacing": {},
  "radius": {},
  "border": {},
  "shadow": {},
  "motion": {},
  "zIndex": {},
  "breakpoint": {},
  "asset": {}
}
```

Nếu project/game cần domain token, thêm group riêng:

```json
{
  "game": {},
  "status": {},
  "chart": {},
  "map": {}
}
```

### 2.3. `component-inventory.md`

Format bắt buộc:

| Component ID | Component | Category | Priority | Platforms | Used In Screens | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CMP-001 | Button | Core UI | P0 | iOS/Android/Web | S-001 | TBD |

### 2.4. `component-state-matrix.md`

Format bắt buộc:

| Component ID | Variant | State | Visual Requirement | Behavior | Accessibility |
| --- | --- | --- | --- | --- | --- |
| CMP-001 | Primary | Loading | Spinner + disabled label | Prevent duplicate submit | Announce loading |

### 2.5. Component Spec

Mỗi component P0/P1 cần có spec theo format:

```text
Component ID:
Name:
Category:
Purpose:
Anatomy:
Variants:
States:
Tokens:
Responsive behavior:
Accessibility:
Usage rules:
Do:
Don't:
Used in screens:
Implementation notes:
```

Có thể lưu trong một file `design-system.md` hoặc tách folder `components/<component-id>.md` nếu nhiều.

## 3. UI Workflow Package

### 3.1. Required Files

Khi đưa ngược vào repo, lưu vào:

```text
doc/4-DESIGN/mockups/
  README.md
  screen-map.md
  flow-map.md
  state-coverage.md
  frame-export-notes.md
  raw/
```

### 3.2. `screen-map.md`

Map mọi screen trong PRD sang frame/mockup của Claude Design.

| Screen ID | Screen Name | Frame/Mockup Name | Platform | Flow ID | States Delivered | Status |
| --- | --- | --- | --- | --- | --- | --- |
| S-001 | TBD | TBD | iOS | UF-001 | default, loading, error | Ready |

Rules:

- `Screen ID` phải khớp `doc/2-PRD/02-screen-inventory.md`.
- Nếu màn chưa design, status = `Missing`.
- Nếu state thiếu, ghi rõ trong `States Delivered`.

### 3.3. `flow-map.md`

Map user flow sang màn hình:

| Flow ID | Flow Name | Entry Screen | Steps / Screens | Success Exit | Failure / Edge Screens |
| --- | --- | --- | --- | --- | --- |
| UF-001 | TBD | S-001 | S-001 -> S-002 | S-003 | S-004 |

### 3.4. `state-coverage.md`

Theo dõi state coverage để implementation không sót:

| Screen ID | Default | Loading | Empty | Error | Offline | No Permission | Paywall/Locked | Success | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S-001 | Yes | Yes | N/A | Yes | TBD | N/A | N/A | Yes | TBD |

### 3.5. Frame Naming Convention

Frame/mockup nên dùng pattern:

```text
<ScreenID> - <ScreenName> - <State> - <Platform>
```

Ví dụ:

```text
S-001 - Home - Default - iPhone
S-001 - Home - Loading - iPhone
S-001 - Home - Error - iPhone
```

Với component:

```text
CMP-001 - Button - Variants
CMP-001 - Button - States
```

## 4. Asset Output

Nếu có assets, Claude Design phải ghi:

| Asset ID | Asset Name | Type | Used In | Required Format | Notes |
| --- | --- | --- | --- | --- | --- |
| AST-001 | App Icon | icon | app | png/svg | TBD |

Rules:

- Không chỉ nhắc “có ảnh”; phải map asset dùng ở đâu.
- Nếu asset cần tạo bằng ImageGen/AI, ghi prompt/brief.
- Nếu asset chỉ là placeholder, ghi rõ.

## 5. Design Handoff Status

Codex phải cập nhật `doc/4-DESIGN/README.md` hoặc file liên quan với status:

| Package | Status | Source Artifact | Imported To | Notes |
| --- | --- | --- | --- | --- |
| Design System | Pending/Imported/Needs Fix | TBD | system/ | TBD |
| UI Workflow | Pending/Imported/Needs Fix | TBD | mockups/ | TBD |

## 6. Import-Back Workflow

Sau khi Claude Design output, Codex làm theo bước:

1. Lưu raw output vào `doc/4-DESIGN/system/raw/` hoặc `doc/4-DESIGN/mockups/raw/` nếu có.
2. Tách/tóm tắt Design System vào `doc/4-DESIGN/system/*`.
3. Tách/tóm tắt UI Workflow vào `doc/4-DESIGN/mockups/*`.
4. Cập nhật `doc/4-DESIGN/04-component-inventory.md`.
5. Cập nhật `doc/4-DESIGN/03-screen-flow-requirements.md`.
6. Cập nhật `doc/5-DELIVERY/12-traceability-matrix.md` với DS/UI mapping.
7. Cập nhật `doc/5-DELIVERY/01-epic-story-task-breakdown.md` để thêm DS/UI implementation tasks.
8. Cập nhật `doc/5-DELIVERY/02-dependency-map.md` để UI tasks phụ thuộc DS tasks.
9. Chạy `doc/4-DESIGN/05-design-review-checklist.md`.

## 7. Design Review Gate

Không được dùng design để break task implementation nếu:

- Design system thiếu component inventory.
- UI workflow thiếu screen-map.
- Screen ID không map được PRD screen inventory.
- Core screen thiếu default state.
- Critical flow thiếu error/edge state.
- Mockup mâu thuẫn business rule hoặc PRD.

Nếu thiếu, ghi vào open questions hoặc design fix list trước.

## 8. Design Fix List

Format fix list:

| ID | Package | Issue | Impact | Needed Before | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| DF-001 | UI Workflow | Missing error state for S-001 | Implementation ambiguity | UI task breakdown | Design | Open |

