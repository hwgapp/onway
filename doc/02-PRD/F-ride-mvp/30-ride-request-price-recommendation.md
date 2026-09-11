# PRD: Ride Request & Price Recommendation

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, API Core Backend, Admin Portal  

## 1. Objective

Allow customers to create a valid Ride request with pickup, dropoff, vehicle type, route estimate, and recommended price before matching starts.

## 2. Scope

In scope:

- Pickup/dropoff selection.
- Region validation.
- Vehicle type selection: motorcycle/car.
- Distance/ETA estimate.
- Recommended price.
- Request draft and confirmation.
- No default negotiation in P0.

Out of scope:

- Ride price negotiation by default.
- Scheduled ride.
- Favorite driver.
- Corporate ride.

## 3. Preconditions

- Customer is authenticated and allowed to create Ride request.
- Pickup/dropoff are inside allowed service policy.
- Ride service is active in selected region.
- Vehicle type is enabled in region.
- Pricing policy exists.

## 4. Ride Request State Model

Suggested states:

- `draft`
- `priced`
- `confirmed_by_customer`
- `matching`
- `cancelled_before_match`
- `expired_no_match`

## 5. User Stories

### US-01 - Customer selects pickup and dropoff

As a customer, I want to choose pickup and dropoff so the app can estimate route and price.

Acceptance criteria:

- Customer can search address or place map pin.
- Pickup/dropoff coordinates are validated.
- Invalid/out-of-region locations block confirmation.
- App stores address label and coordinate.

### US-02 - Customer selects vehicle type

As a customer, I want to choose motorcycle or car when available.

Acceptance criteria:

- Vehicle options come from region config.
- Disabled options are hidden or disabled with reason.
- Selected vehicle type is passed to pricing and matching.

### US-03 - Customer sees recommended price

As a customer, I want to see recommended price before requesting a driver.

Acceptance criteria:

- Price displays region currency.
- Price is calculated by backend policy/engine.
- Customer sees route distance/ETA estimate where available.
- P0 does not show negotiation input by default.

### US-04 - Customer confirms request

As a customer, I want to confirm the Ride request and start matching.

Acceptance criteria:

- Confirmation persists request and transitions to matching.
- Customer cannot confirm if price/route/region validation is stale.
- Request snapshot stores pickup, dropoff, vehicle, distance, ETA, price, currency.

## 6. Acceptance Tests

- Given pickup outside active Ride region, when customer confirms, then API rejects and app shows region error.
- Given car disabled in region, when customer opens vehicle options, then car cannot be selected.
- Given price policy unavailable, when customer confirms, then request is blocked with retry/support state.
- Given valid route and price, when customer confirms, then ride enters matching state.

## 7. Analytics

- Ride request started.
- Pickup/dropoff valid/invalid.
- Vehicle selected.
- Price shown.
- Request confirmed.
- Request abandoned before matching.

## 8. Open Questions

- Whether destination outside region is allowed when pickup is inside.
- Exact price formula/guardrails.
- Whether customer can save locations in P0.

