# PRD: Outlet Override & Availability

**Phase:** P0  
**Status:** Draft  
**Platforms:** Admin Portal, API Core Backend, Customer App  

## 1. Objective

Allow outlet-specific overrides to canonical menu and availability so customer ordering reflects local store differences.

## 2. Scope

In scope:

- Outlet-specific item availability.
- Outlet-specific item price override.
- Outlet-specific modifier override.
- Opening hours override.
- Temporary closure.
- Waiting policy override placeholder.

Out of scope:

- Merchant self-service updates.
- Driver-submitted updates in MVP.
- AI-detected changes.

## 3. Override Principles

- Canonical menu remains source template.
- Outlet override does not mutate canonical menu.
- Customer sees effective menu calculated from canonical + outlet overrides.
- All overrides are auditable.

## 4. User Stories

### US-01 - Admin marks item unavailable at outlet

As admin, I want to mark an item unavailable at a specific outlet without affecting other outlets.

Acceptance criteria:

- Override applies only to selected outlet.
- Customer cannot add unavailable item to cart.
- Existing carts are revalidated before checkout.

### US-02 - Admin overrides item price

As admin, I want to set local outlet price when it differs from canonical menu.

Acceptance criteria:

- Override price must be valid non-negative money.
- Customer sees effective outlet price.
- Audit log records old/new value and reason.

### US-03 - Admin sets temporary closure

As admin, I want to close an outlet temporarily.

Acceptance criteria:

- Closure has start/end or manual reopen.
- Customer cannot place new orders during closure.
- Existing orders require operations policy if impacted.

### US-04 - System validates cart against latest availability

As the system, I need to prevent checkout with stale unavailable items or changed prices.

Acceptance criteria:

- Cart validation checks effective menu at order placement.
- Customer is shown changed/unavailable items before confirming.
- Order stores snapshot of accepted item names/prices/modifiers.

## 5. Acceptance Tests

- Given outlet override marks item unavailable, when customer opens menu, then item is disabled/unavailable.
- Given customer cart has item that became unavailable, when checkout starts, then app requires customer to remove/update.
- Given outlet price override exists, when order is created, then order uses override price not canonical price.
- Given admin removes override, when customer refreshes menu, then canonical value applies again.

## 6. Open Questions

- Whether outlet override requires review before publish.
- Whether waiting policy override is P0 or P1.
- How customers are notified about price changes in cart.

