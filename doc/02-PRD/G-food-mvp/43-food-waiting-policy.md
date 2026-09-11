# PRD: Food Waiting Policy

**Phase:** P0  
**Status:** Draft  
**Platforms:** Admin Portal, Driver App, Customer App, API Core Backend  

## 1. Objective

Define configurable waiting policy for restaurant preparation delays and how waiting time affects order state, communication, and financial responsibility.

## 2. Scope

In scope:

- Brand-level waiting policy.
- Optional outlet override placeholder.
- Free waiting time.
- Start point for waiting.
- Max waiting fee/handling.
- Driver/customer visibility.

Out of scope:

- Automated payout through Onway.
- AI waiting prediction as required launch dependency.

## 3. Policy Fields

Suggested fields:

- Free wait minutes.
- Fee start event.
- Fee calculation unit: per minute/block.
- Fee amount.
- Max fee.
- No-fee conditions.
- Applies to brand/outlet/service region.

## 4. User Stories

### US-01 - Admin configures waiting policy

As admin, I want to configure waiting policy by brand so known slow restaurants are handled consistently.

Acceptance criteria:

- Policy can be set at brand level.
- Values are validated and auditable.
- Outlet override can be added later without breaking model.

### US-02 - Driver sees waiting state

As a driver, I want the app to track when I am waiting at restaurant.

Acceptance criteria:

- Driver can mark arrived and waiting.
- Waiting timer starts from configured event.
- Driver sees whether waiting fee may apply or only operational warning applies.

### US-03 - Customer sees delay

As a customer, I want to know if restaurant preparation is delayed.

Acceptance criteria:

- Customer receives order delayed status.
- Customer can chat with driver.
- Any extra amount/financial implication requires explicit policy and confirmation.

## 5. Acceptance Tests

- Given brand free wait is 10 minutes, when driver waits 12 minutes, then system records 2 minutes chargeable/over-free according to policy.
- Given waiting fee is disabled for brand, when driver waits, then no extra fee is requested.
- Given driver marks waiting without being at outlet, then API may reject based on proximity policy.
- Given order is delayed, when customer opens tracking, then waiting status is visible.

## 6. Open Questions

- Whether waiting fee is charged in P0 or only tracked.
- Whether customer must approve waiting fee before it accrues.
- Exact brand defaults.

