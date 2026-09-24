# Screen Inventory

| Screen ID | Screen | Platform | Feature | States Required | Notes |
| --- | --- | --- | --- | --- | --- |
| S-001 | Home / service selector | Customer app | Ride/Food entry | loading, error, region unavailable | Super App entry |
| S-002 | Ride request | Customer app | F-006 | loading, no region, no vehicle, error | Pickup/dropoff, vehicle type, recommended/final platform price |
| S-003 | Ride matching | Customer app | F-008 | loading, driver rejected, timeout, no driver, canceled | Shows matching status and final platform price |
| S-004 | Active Ride | Customer app | F-010, F-019 | loading, connection issue, complaint/report, proof pending, payment disputed | Tracking, call, chat, payment proof before driver arrives |
| S-005 | Food browse | Customer app | F-011, F-012 | loading, empty, closed outlet, unavailable region, error | Brand/outlet/menu |
| S-006 | Food cart/checkout | Customer app | F-012, F-013 | price changed, item unavailable, error | Shows item price, delivery fee, total |
| S-007 | Food matching/payment proof | Customer app | F-014, F-015 | no driver, proof rejected/pending, payment disputed, timeout | Customer pays driver after driver found |
| S-008 | Active Food order | Customer app | F-016, F-017, F-019 | driver waiting, change requested, proposal timeout, canceled, issue | Track, chat/call, accept/reject changes |
| S-009 | Rating/report/complaint | Customer app | F-020 | loading, validation error, submitted | 5-star rating + quick tags; separate report/complaint |
| S-010 | Driver onboarding | Driver app | F-002 | incomplete, rejected, pending review, approved | Phone/identity/documents |
| S-011 | Driver subscription/platform fee | Driver app | F-003 | unpaid, pending proof, active, expired | Driver submits proof/reference for Onway platform fee; Finance Ops verifies manually |
| S-012 | Driver online/jobs | Driver app | F-008, F-014 | no region, paused service, no jobs, error | Ride/Food job cards |
| S-013 | Driver Ride job | Driver app | F-008, F-010 | offer received, accepted, rejected, arrived, started, completed, canceled | Driver sees platform final price; includes Accept/Reject and proof/received confirmation |
| S-014 | Driver Food job | Driver app | F-014, F-016, F-017 | proof pending, at outlet, change needed, delivered | Order-at-restaurant flow |
| S-015 | Chat | Customer/Driver app | F-019 | loading, offline, retention expired, upload failed | Active Ride/Food only; one image per message in P0 |
| S-016 | Admin dashboard | Admin web | Admin baseline | loading, empty, error | Rollout and ops overview |
| S-017 | Region/polygon editor | Admin web | F-004 | invalid polygon, overlapping polygon, paused, no service, draft, published | Create/draw/edit/pause/resume/publish polygon on map; no hard delete P0 |
| S-018 | Pricing/policy config | Admin web | F-007, F-013, F-024 | validation error, draft/published | Guardrails, thresholds, waiting policy |
| S-019 | Driver management | Admin web | F-002, F-003, F-022 | pending, rejected, active, locked, appeal pending | Activation/risk/manual lock/auto-lock review |
| S-020 | Food catalog management | Admin web | F-011 | missing data, conflict, inactive outlet | Brand/menu/outlet override |
| S-021 | Complaint/fraud case management | Admin/Operator web | F-021, F-022 | evidence missing, awaiting response, appeal, finalized | Manual P0 lifecycle |
