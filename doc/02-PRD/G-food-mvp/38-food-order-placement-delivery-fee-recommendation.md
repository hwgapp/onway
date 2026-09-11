# PRD: Food Order Placement & Delivery Fee Recommendation

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, API Core Backend  

## 1. Objective

Allow customers to place a Food order with validated cart, delivery address, estimated item total, recommended delivery fee, and no delivery fee negotiation.

## 2. Scope

In scope:

- Delivery address validation.
- Cart validation.
- Item total estimate.
- Delivery fee recommendation.
- Total estimate.
- Customer order confirmation.
- No negotiation.

Out of scope:

- COD.
- Payment gateway.
- Food delivery fee negotiation.
- Merchant App order confirmation.

## 3. Order Draft State Model

Suggested states:

- `cart`
- `address_selected`
- `fee_quoted`
- `customer_confirmed`
- `matching`
- `cancelled_before_match`

## 4. User Stories

### US-01 - Customer selects delivery address

As a customer, I want to choose a delivery address so the app can calculate fee and validate availability.

Acceptance criteria:

- Address has coordinate.
- Coordinate is in active Food region/delivery policy.
- Distance/ETA from outlet to destination can be estimated.

### US-02 - System recommends delivery fee

As the system, I need to calculate a delivery fee for the order.

Acceptance criteria:

- Fee uses backend pricing policy.
- Fee displays currency.
- Fee is stored in order quote snapshot.
- Customer cannot edit/negotiate fee in P0.

### US-03 - Customer confirms order

As a customer, I want to confirm item total, delivery fee, and total before matching driver.

Acceptance criteria:

- Cart is revalidated at confirmation.
- Order snapshot stores accepted item prices, modifiers, delivery address, delivery fee, currency.
- Order enters matching after confirmation.

## 5. Acceptance Tests

- Given customer changes address, when quote refreshes, then delivery fee recalculates.
- Given customer tries to submit custom delivery fee, when API receives request, then API rejects.
- Given cart price changed before confirmation, when customer confirms, then app shows updated review instead of placing order.
- Given Food disabled in region, when order placement runs, then API rejects.

## 6. Analytics

- Delivery address selected.
- Delivery fee quoted.
- Order review shown.
- Order confirmed.
- Order failed validation.

## 7. Open Questions

- Delivery fee formula and minimum/maximum.
- Whether waiting fee estimate is included upfront.
- Whether small-order handling exists.

