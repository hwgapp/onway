# PRD: Food Delivery, Completion & Rating

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, API Core Backend, Admin Portal  

## 1. Objective

Support Food delivery after restaurant purchase through driver route to customer, delivery completion, payment state closure, and rating.

## 2. Scope

In scope:

- Ready for delivery.
- Driver en route to customer.
- Arrival at delivery address.
- Delivered/completed state.
- Customer/driver rating.
- Basic issue reporting.

Out of scope:

- Merchant confirmation.
- In-app proof of delivery requirement unless configured.
- Trust score update.

## 3. Delivery State Model

Suggested states:

- `ready_for_delivery`
- `driver_en_route_to_customer`
- `driver_arrived_at_customer`
- `delivered`
- `completed`
- `delivery_failed`
- `disputed`

## 4. User Stories

### US-01 - Customer tracks delivery

As a customer, I want to see when driver is bringing my food.

Acceptance criteria:

- Customer sees driver location/ETA if available.
- Customer sees order state.
- Chat remains available while active.

### US-02 - Driver marks delivered

As a driver, I want to mark order delivered after giving food to customer.

Acceptance criteria:

- Order must be in deliverable state.
- Completion captures timestamp and location snapshot where allowed.
- Customer receives delivered/completed event.

### US-03 - Customer rates Food delivery

As a customer, I want to rate the delivery after completion.

Acceptance criteria:

- Rating opens after completed order.
- Customer can rate driver/service.
- Low rating can offer complaint path.

### US-04 - Driver rates customer

As a driver, I want to rate customer handoff experience.

Acceptance criteria:

- Driver can submit once per completed order.
- Rating is tied to order.
- Rating does not auto-lock customer in P0.

## 5. Acceptance Tests

- Given order not ready for delivery, when driver marks delivered, then API rejects.
- Given driver arrives at customer, when customer opens order, then state reflects arrival.
- Given order completed, when customer submits rating, then rating is stored and visible to admin.
- Given delivery failed, when complaint is filed, then order timeline is linked.

## 6. Open Questions

- Whether proof of delivery photo is required.
- Whether driver can complete when customer unreachable.
- Customer wait/no-show at delivery address policy.

