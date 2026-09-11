# PRD: Food Cancellation & Financial Responsibility

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, Admin Portal, API Core Backend  

## 1. Objective

Define Food cancellation and financial responsibility rules in a money-light model where payment is direct between customer and driver and Onway does not hold funds.

## 2. Scope

In scope:

- Cancellation before driver assignment.
- Cancellation after driver assignment before payment proof.
- Cancellation after payment proof before restaurant order placed.
- Cancellation after restaurant order placed.
- Driver/restaurant/system fault paths.
- Complaint/dispute escalation.

Out of scope:

- Generic refund processing by Onway.
- Wallet credit.
- Payment gateway refund.

## 3. Cancellation State Model

Suggested states:

- `cancelled_before_assignment`
- `cancelled_after_assignment_before_payment`
- `cancelled_after_payment_before_purchase`
- `customer_cancelled_after_restaurant_ordered`
- `driver_cancelled`
- `restaurant_unavailable`
- `system_cancelled`
- `financial_dispute_opened`

## 4. Financial Principles

- Onway does not hold order money.
- Customer transfers directly to driver.
- Driver pays restaurant directly.
- After driver has placed order with restaurant, customer cannot cancel for refund due to customer change of mind.
- Fault by driver, restaurant, or system requires separate dispute/fair responsibility handling.

## 5. User Stories

### US-01 - Customer cancels before assignment

As a customer, I want to cancel before a driver is assigned.

Acceptance criteria:

- Cancellation is allowed.
- No transfer prompt has appeared.
- Order ends with no financial dispute.

### US-02 - Customer cancels after payment before purchase

As a customer, I may need to cancel after transferring but before driver orders.

Acceptance criteria:

- App explains money is direct to driver and requires direct/admin-assisted resolution.
- Cancellation opens financial state if transfer proof exists.
- Driver and admin are notified according to policy.

### US-03 - Customer cancels after restaurant order placed

As the system, I need to enforce no-refund/customer responsibility once driver has ordered food.

Acceptance criteria:

- Customer cancellation does not mark money refundable by Onway.
- App shows clear consequence before cancellation.
- Order records restaurant_order_placed timestamp.

### US-04 - Driver cancels after receiving payment

As Onway, I need to detect serious risk if driver cancels or disappears after payment proof.

Acceptance criteria:

- Cancellation after proof creates review/dispute trigger.
- Driver may be prevented from new jobs depending on policy.
- Complaint can qualify for auto-lock count.

## 6. Acceptance Tests

- Given order has no assigned driver, when customer cancels, then order ends without payment dispute.
- Given customer paid and driver has not ordered, when customer cancels, then order enters direct financial resolution state.
- Given restaurant_order_placed is recorded, when customer cancels, then no-refund/customer responsibility copy is shown and timeline records decision.
- Given driver cancels after proof submitted, when complaint opens, then risk lock workflow can count it.

## 7. Open Questions

- Exact responsibility policy for driver fault vs restaurant fault vs system fault.
- Whether admin mediates direct return transfer.
- Customer timeout behavior after driver proposes item/price change.

