# PRD: Driver Online/Offline & Location Presence

**Phase:** P0  
**Status:** Draft  
**Platforms:** Driver App, API Core Backend, Admin Portal  

## 1. Objective

Allow active eligible drivers to go online, share location, and become discoverable by matching while preventing unavailable or risky drivers from receiving jobs.

## 2. Scope

In scope:

- Online/offline toggle.
- Location permission requirement.
- WebSocket location updates.
- Redis presence.
- Region/service/vehicle validation.
- Automatic offline handling.
- Admin visibility of current driver availability.

Out of scope:

- Driver schedule/calendar.
- Heatmap incentives.
- Trust-based priority.

## 3. Presence State Model

Suggested states:

- `offline`
- `going_online`
- `online_available`
- `online_on_offer`
- `on_job`
- `temporarily_unavailable`
- `forced_offline`

## 4. User Stories

### US-01 - Driver goes online

As an active driver, I want to go online when I am ready to receive jobs.

Acceptance criteria:

- Driver account must be active and not locked/suspended.
- Location permission must be granted.
- Current location must be inside eligible active region.
- Driver selects or confirms active vehicle/service availability if needed.

### US-02 - System tracks driver presence

As the matching system, I need current driver location and availability.

Acceptance criteria:

- Driver app sends location updates through WebSocket.
- Redis stores last known location and presence with expiry.
- Matching reads candidate drivers from presence first.
- Important location snapshots may be persisted for active jobs/disputes.

### US-03 - Driver is forced offline when restricted

As the system, I need to force offline drivers who become locked, suspended, out-of-region, or lose required permissions.

Acceptance criteria:

- Status change event reaches driver app.
- Online state turns off or becomes forced offline.
- Driver cannot receive new offers.
- Reason is visible in app where appropriate.

## 5. Acceptance Tests

- Given inactive driver taps online, then API rejects and app shows activation requirement.
- Given active driver denies location permission, then online toggle is blocked.
- Given driver location update stops beyond TTL, then presence expires and matching excludes driver.
- Given admin locks online driver, then driver receives forced-offline event and new offers stop.

## 6. Admin Monitoring

- Driver list by online/offline/on job/locked.
- Map or table view of active drivers.
- Last location timestamp.
- Service/vehicle eligibility indicators.
- Manual force offline if needed.

## 7. Open Questions

- Location update frequency.
- Presence TTL.
- Background location behavior on iOS/Android.
- Battery optimization strategy.

