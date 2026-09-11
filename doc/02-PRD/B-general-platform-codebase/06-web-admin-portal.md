# PRD General: Web Admin Portal

**Phase:** P0  
**Status:** Draft  
**Platform:** ReactJS Admin Portal  

## 1. Objective

Define the Admin Portal baseline required for Onway MVP operations: configuration, driver review, food catalog management, monitoring, disputes, risk lock, and audit.

## 2. Scope

Admin Portal must support:

- Admin login and RBAC.
- Region/polygon/currency/service rollout.
- Policy config.
- Driver onboarding review.
- Platform fee proof verification.
- Brand/outlet/menu catalog management.
- Catalog publishing and availability.
- Ride/Food monitoring.
- Complaint/dispute review.
- Driver lock/unlock manual action.
- Audit log.

## 3. Roles

Initial role model:

- Super Admin: full access.
- Operations Admin: region/catalog/monitoring/dispute.
- Driver Review Admin: onboarding and platform fee verification.
- Support Operator: complaint/dispute handling.
- Readonly Auditor: timeline/audit read access.

## 4. User Stories

### US-01 - Admin configures service availability

As an admin, I want to configure region polygons, currency, and enabled services so apps only expose valid operations.

Acceptance criteria:

- Admin can create/edit/pause/close region.
- Admin can set currency per region.
- Admin can enable/disable Ride/Food and vehicle types.
- All changes write audit log.

### US-02 - Admin creates Food supply

As an operations admin, I want to create brands, outlets, menus, and publish catalog data before Food is visible to customers.

Acceptance criteria:

- Admin can manage brand/outlet/menu.
- Outlet must belong to active/planned region before publishing.
- Published menu becomes visible in Customer App only when outlet is available.

### US-03 - Admin reviews paid-but-driver-no-show complaint

As a support operator, I want to inspect payment proof, chat, timeline, and GPS snapshots so I can decide whether to lock or unlock a driver.

Acceptance criteria:

- Case page shows customer complaint, proof, chat evidence, ride/order state, and driver history.
- Admin can lock/unlock driver with reason.
- Decision writes audit log.

## 5. Acceptance Tests

- Given admin lacks catalog permission, when they open menu management, then access is denied.
- Given admin publishes an outlet without menu items, then portal blocks publish with validation.
- Given admin locks a driver, when driver app is online, then driver is disconnected from job receiving.
- Given region currency changes, when apps refresh config, then displayed currency uses new setting.

## 6. UI Requirements

- Dense operational UI, not marketing layout.
- Tables must support search, filters, status chips, and detail drawers/pages.
- Risk actions require reason field.
- Dangerous actions require confirmation and audit reason.
- Evidence viewers must show image, metadata, upload actor, and linked entity.

## 7. Backend Dependencies

- Admin RBAC APIs.
- Region/policy/catalog APIs.
- Driver review/platform fee APIs.
- Monitoring timeline APIs.
- Complaint/fraud/risk APIs.
- Audit log APIs.

## 8. Open Questions

- Exact RBAC permission matrix.
- Whether map polygon editing uses HERE directly in admin UI.
- Admin SLA dashboards for disputes.

