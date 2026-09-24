# Route Map

| Route ID | Path / Navigation | Screen ID | Auth/Permission | Notes |
| --- | --- | --- | --- | --- |
| C-R-001 | Customer App / Home | S-001 | Customer auth | Service selector, region unavailable state |
| C-R-002 | Customer App / Ride request | S-002 | Customer auth | Pickup/dropoff, vehicle, recommended/final platform price |
| C-R-003 | Customer App / Ride matching | S-003 | Customer auth | Matching, driver Accept/Reject, timeout, no driver |
| C-R-004 | Customer App / Active Ride | S-004 | Customer auth + service participant | Tracking, payment proof before driver arrives, payment disputed state, chat/call |
| C-R-005 | Customer App / Food browse | S-005 | Customer auth | Brand/outlet/menu |
| C-R-006 | Customer App / Food cart/checkout | S-006 | Customer auth | Delivery fee, total estimate |
| C-R-007 | Customer App / Food payment proof | S-007 | Customer auth + matched order | VietQR/bank transfer proof, payment disputed state |
| C-R-008 | Customer App / Active Food order | S-008 | Customer auth + service participant | Tracking, change proposal, proposal timeout, chat/call |
| C-R-009 | Customer App / Rating report complaint | S-009 | Customer auth | 5-star rating + quick tags; Ride/Food reports |
| D-R-001 | Driver App / Onboarding | S-010 | Driver auth | Phone, identity, documents |
| D-R-002 | Driver App / Platform fee | S-011 | Driver auth | Launch package proof/reference |
| D-R-003 | Driver App / Online jobs | S-012 | Activated driver | Online/offline, job cards |
| D-R-004 | Driver App / Ride job | S-013 | Activated driver + assigned ride | Ride offer Accept/Reject and lifecycle |
| D-R-005 | Driver App / Food job | S-014 | Activated driver + assigned order | Payment confirmation, order-at-restaurant |
| X-R-001 | Customer/Driver App / Chat | S-015 | Active service participant | Text/image, 1 image per message, retention 1 week unless dispute |
| A-R-001 | Admin Portal / Dashboard | S-016 | Admin role | Basic ops overview/dashboard |
| A-R-002 | Admin Portal / Region polygon editor | S-017 | Super Admin/Ops Admin | Polygon, lifecycle, service/vehicle rollout, overlap publish block |
| A-R-003 | Admin Portal / Pricing policy config | S-018 | Super Admin/Ops Admin | Versioned policy config |
| A-R-004 | Admin Portal / Driver management | S-019 | Super Admin/Driver Ops/Risk scope | Verification, activation, risk/manual lock, auto-lock appeal/review |
| A-R-005 | Admin Portal / Food catalog | S-020 | Super Admin/Catalog Manager/Ops limited | Brand/outlet/menu/override |
| A-R-006 | Admin Portal / Complaint fraud cases | S-021 | Super Admin/Risk/Fraud/Support scoped | Manual lifecycle and evidence |
