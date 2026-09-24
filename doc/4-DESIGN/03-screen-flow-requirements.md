# Screen Flow Requirements

| Flow | Screens | Required States | Notes |
| --- | --- | --- | --- |
| UF-001 Ride request to completed trip | S-001, S-002, S-003, S-004, S-009, S-015 | default, loading, matching, driver rejected, no driver, proof pending, payment disputed, money received confirmed, error, offline, complaint | Include platform final price, map, status header, chat/call and payment proof before driver arrives |
| UF-002 Food order to delivered | S-001, S-005, S-006, S-007, S-008, S-009, S-015 | default, loading, empty menu, outlet closed, no driver, proof pending, payment disputed, issue, delivered | Include proof upload and driver money received state |
| UF-003 Food change proposal | S-008, S-014, S-015 | proposal pending, accepted, rejected, timeout, supplemental payment needed, error | Customer decision before affected purchase; default timeout 5 minutes |
| UF-004 Driver onboarding and activation | S-010, S-011, S-012 | incomplete, pending review, rejected, unpaid, proof pending, active | Include platform fee proof |
| UF-005 Complaint and fraud/dispute | S-009, S-021 | submitted, evidence missing, under review, finalized, appeal, auto-lock, unlock | Admin evidence review must be clear |
| UF-006 Admin region/policy rollout | S-016, S-017, S-018 | draft, invalid polygon, overlap blocked, published, paused, resumed | Include polygon editor/map UI; no hard delete P0 |
| UF-007 Active chat/direct call | S-015 | message sending, upload failed, offline, closed, retention expired | Text and image chat; 1 image per message P0 |

## Required Deliverable From Claude Design

Claude Design phải cung cấp UI workflow cho tất cả màn hình trong screen inventory:

- Mỗi Screen ID có mockup/frame tương ứng.
- Mỗi core flow có đường đi rõ: entry, success, failure, exit.
- Mỗi screen có state variants cần thiết.
- Navigation/route/tab/back behavior rõ.
- Nếu một screen dùng component đặc biệt, map về component inventory.

## Screen Handoff Table

| Screen ID | Frame/Mockup | Flow | States Delivered | Components Used | Notes |
| --- | --- | --- | --- | --- | --- |
| All P0 screens | Required from Claude Design | UF-001 to UF-007 | default + relevant states above | Must map to component inventory | Frame names must match output contract |
