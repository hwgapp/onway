# PRD: Driver Restaurant Purchase Flow

**Phase:** P0  
**Status:** Draft  
**Platforms:** Driver App, Customer App, API Core Backend, Admin Portal  

## 1. Objective

Guide driver through arriving at restaurant, placing order directly, handling payment to restaurant, and updating customer/admin after customer prepayment proof exists.

## 2. Scope

In scope:

- Driver route to outlet.
- Arrived at outlet.
- Place order with restaurant.
- Mark restaurant order placed.
- Pay restaurant directly.
- Waiting/preparation state.
- Issue/change escalation.

Out of scope:

- Merchant App early preparation.
- Onway paying restaurant.
- Driver modifying catalog data.

## 3. Preconditions

- Food order is assigned.
- Customer payment proof is submitted.
- Driver is not locked from active continuation according to policy.
- Outlet is still serviceable or issue flow starts.

## 4. Purchase State Model

Suggested states:

- `driver_en_route_to_outlet`
- `driver_arrived_at_outlet`
- `ordering_with_restaurant`
- `restaurant_order_placed`
- `waiting_for_food`
- `restaurant_paid`
- `ready_for_delivery`
- `issue_requires_customer_confirmation`
- `cancelled_or_failed`

## 5. User Stories

### US-01 - Driver navigates to outlet

As a driver, I want outlet location and order details so I can go to the right restaurant.

Acceptance criteria:

- Driver sees outlet address/map and order item summary.
- App can open map navigation.
- Arrived action may validate proximity.

### US-02 - Driver places order

As a driver, I want to mark when I have placed the order with restaurant.

Acceptance criteria:

- Driver can only mark order placed after required payment proof state.
- Marking order placed writes timestamp.
- After this state, customer cancellation financial rules change.

### US-03 - Driver pays restaurant

As a driver, I want to record that I paid the restaurant.

Acceptance criteria:

- Driver can mark restaurant paid.
- App may allow optional receipt/proof image if policy requires.
- Timeline records event.

### US-04 - Driver reports restaurant issue

As a driver, I need to report price changes, unavailable items, or modifier issues.

Acceptance criteria:

- Driver can launch item/price change confirmation flow.
- Affected items and proposed changes are sent to customer.
- Driver cannot buy affected changed item until customer accepts.

## 6. Acceptance Tests

- Given no customer payment proof, when driver taps go/order, then app blocks.
- Given driver marks restaurant order placed, when customer tries cancel, then no-refund/customer-responsibility policy applies.
- Given item unavailable, when driver submits change, then customer confirmation is required.
- Given driver marks ready for delivery, when customer app receives event, then delivery tracking starts.

## 7. Open Questions

- Whether restaurant receipt proof is required in P0.
- Whether driver can call customer outside chat.
- Exact proximity requirement at outlet.

