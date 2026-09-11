# PRD: Ride Cancellation, Timeout & No-Show

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, Admin Portal, API Core Backend  

## 1. Objective

Define how Ride requests/trips can be cancelled, expire, or become no-show cases across customer, driver, matching, and admin workflows.

## 2. Scope

In scope:

- Customer cancellation before match.
- Customer cancellation after assignment.
- Driver cancellation after assignment.
- Matching timeout/no driver.
- Customer no-show.
- Driver no-show.
- Payment-related no-show escalation.

Out of scope:

- Cancellation fee automation in MVP unless separately decided.
- Trust scoring impact.

## 3. State Model

Suggested ride cancellation states:

- `cancelled_by_customer_before_match`
- `cancelled_by_customer_after_assignment`
- `cancelled_by_driver`
- `expired_no_driver`
- `customer_no_show_reported`
- `driver_no_show_reported`
- `cancelled_by_admin`
- `disputed`

## 4. User Stories

### US-01 - Customer cancels before match

As a customer, I want to cancel while matching if I no longer need a ride.

Acceptance criteria:

- Cancel is allowed before assignment.
- Active offers are cancelled.
- Customer sees cancelled state.

### US-02 - Driver cancels assigned ride

As a driver, I need a way to cancel if I cannot continue.

Acceptance criteria:

- Driver must choose reason.
- Customer is notified.
- Backend records timeline.
- Matching/retry behavior follows policy.

### US-03 - Driver reports customer no-show

As a driver, I want to report if customer does not appear at pickup.

Acceptance criteria:

- Driver must be at/near pickup or wait configured time unless policy override.
- Report writes timeline.
- Customer receives notification/dispute option.

### US-04 - Customer reports driver no-show

As a customer, I want to report if driver does not arrive or stops responding.

Acceptance criteria:

- Customer can submit report with optional chat/payment proof.
- If payment proof exists, case can enter paid-but-driver-no-show dispute path.
- Driver risk counters may update if complaint qualifies.

## 5. Acceptance Tests

- Given customer cancels before assignment, when driver later accepts stale offer, then accept is rejected.
- Given driver cancels after assignment, when customer app receives event, then ride is cancelled/retry option appears.
- Given customer paid and reports driver no-show, when complaint qualifies, then driver complaint count updates.
- Given matching reaches max attempts, then ride becomes expired_no_driver.

## 6. Open Questions

- Cancellation fee policy.
- Minimum wait time for no-show.
- Whether immediate rematch is supported after driver cancellation.

