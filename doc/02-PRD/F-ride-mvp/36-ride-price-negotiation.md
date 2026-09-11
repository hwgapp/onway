# PRD: Ride Price Negotiation

**Phase:** P1  
**Status:** Draft  
**Platforms:** Customer App, Driver App, API Core Backend, Admin Portal  

## 1. Objective

Reserve a future Ride price negotiation flow while keeping P0 launch independent from full Trust logic.

## 2. MVP Position

Ride price negotiation is not default P0. P0 can launch with recommended price only. If enabled before Trust Engine, it must be behind feature flag and simple eligibility rules.

## 3. Future Scope

- Customer proposes one price within configured band.
- Default BRD band was +/-10% of recommended price.
- Driver can accept or reject.
- No driver counter-offer in MVP/future initial negotiation.
- If rejected/no match, customer may retry with recommended price if policy allows.

## 4. User Stories

### US-01 - Customer proposes price

As an eligible customer, I want to propose one ride price within allowed band.

Acceptance criteria:

- Eligibility is server-side.
- Proposed price must be within configured min/max band.
- Customer can submit only once per ride request.
- Proposed price is shown to candidate drivers.

### US-02 - Driver accepts/rejects proposed price

As a driver, I want to accept or reject the offered price without counter-offer.

Acceptance criteria:

- Driver sees final proposed price.
- Driver can accept/reject.
- No counter-offer UI exists.
- Accepted proposed price becomes final ride price.

### US-03 - Admin configures negotiation policy

As admin, I want to enable/disable negotiation and configure allowed band.

Acceptance criteria:

- Feature flag can disable negotiation by region/service.
- Band values are configurable.
- Config changes are audited.

## 5. Acceptance Tests

- Given negotiation disabled, when customer opens ride request, then no negotiation UI appears.
- Given proposed price is outside band, when customer submits, then API rejects.
- Given driver accepts proposed price, then ride final fare equals proposed price.
- Given customer tries second proposal, then API rejects.

## 6. Open Questions

- Whether P1 depends on Trust Engine or simple verified-customer rule.
- Whether retry with recommended price is always allowed.
- Exact customer UX if all drivers reject proposed price.

