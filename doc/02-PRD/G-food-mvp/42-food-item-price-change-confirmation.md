# PRD: Food Item / Price Change Confirmation

**Phase:** P0  
**Status:** Draft  
**Platforms:** Driver App, Customer App, API Core Backend, Admin Portal  

## 1. Objective

Handle real-world restaurant changes such as price mismatch, item unavailable, modifier unavailable, or substitution before driver purchases affected items.

## 2. Scope

In scope:

- Driver proposes item/price/status change.
- Customer accepts/rejects change.
- Order total recalculation.
- Additional transfer proof if needed.
- Cancellation/failure route if rejected.
- Admin visibility.

Out of scope:

- Automatic catalog update.
- Driver menu verification.
- Community Truth.

## 3. Change State Model

Suggested states:

- `change_proposed`
- `awaiting_customer_decision`
- `accepted_by_customer`
- `rejected_by_customer`
- `expired`
- `admin_review_required`

## 4. User Stories

### US-01 - Driver proposes price change

As a driver, I want to report actual restaurant price when it differs from catalog.

Acceptance criteria:

- Driver selects affected item.
- Driver enters actual price and optional note/photo.
- Proposal is sent to customer before purchase.
- Proposal does not update catalog automatically.

### US-02 - Driver proposes unavailable item

As a driver, I want to report that an item is unavailable.

Acceptance criteria:

- Driver marks item unavailable.
- Driver can suggest remove/substitute if supported.
- Customer must accept resulting cart/order change.

### US-03 - Customer accepts or rejects change

As a customer, I want to approve changes before driver spends my money on affected items.

Acceptance criteria:

- Customer sees original vs proposed item/price/change.
- Customer can accept/reject.
- If accepted and extra amount is required, additional transfer/proof flow is triggered if policy requires.
- If rejected, order continues without affected item or cancels according to policy.

### US-04 - Admin can inspect change history

As admin, I want to see change proposals during dispute.

Acceptance criteria:

- Proposal, customer decision, timestamps, and evidence are in order timeline.
- Catalog remains unchanged unless separate catalog workflow updates it.

## 5. Acceptance Tests

- Given driver reports higher price, when customer has not accepted, then driver cannot mark affected item purchased.
- Given customer rejects unavailable item substitution, when order continues, then affected item is removed or order status follows policy.
- Given price increase requires extra transfer, when customer accepts, then app requests additional proof if configured.
- Given driver submits change, when admin opens order, then proposal and decision history are visible.

## 6. Open Questions

- Whether customer timeout auto-rejects or cancels.
- Whether small price differences can proceed without confirmation.
- Whether substitutions are P0 or simple remove-only.

