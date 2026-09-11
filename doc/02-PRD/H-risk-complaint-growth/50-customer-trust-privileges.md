# PRD: Customer Trust & Privileges

**Phase:** P2  
**Status:** Draft  
**Platforms:** Customer App, Admin Portal, API Core Backend  

## 1. Objective

Reserve future Customer Trust system for privileges such as negotiation eligibility, usage limits, risk controls, and other separately approved privileges after MVP launch.

## 2. MVP Position

P0 does not depend on Trust logic. There is no COD in MVP. Any future COD-like privilege would require a separate business/legal decision and is not assumed by this PRD. Food delivery fee negotiation is removed from MVP. Ride negotiation is P1/P2 feature-flagged.

## 3. Future Scope

- Customer Trust levels T0-T4.
- Privilege gating.
- Future privilege eligibility only after separate approval.
- Ride negotiation future eligibility.
- Risk restriction.
- Admin override.
- Trust history.

## 4. User Stories

### US-01 - System assigns customer trust level

As Onway, I want customers to have trust levels based on behavior and verification.

Acceptance criteria:

- Trust calculation is server-side.
- Trust level history is retained.
- Trust can increase/decrease.

### US-02 - Privileges use trust level

As the system, I want future privileges such as Ride negotiation eligibility or higher operational limits to require approved trust level.

Acceptance criteria:

- Privilege checks are policy-configurable.
- Customer App receives allowed actions, not raw formula.
- Trust does not override fraud/risk restrictions.

### US-03 - Admin reviews customer trust

As admin, I want to inspect trust-related history.

Acceptance criteria:

- Admin sees level, recent changes, reasons/signals where safe.
- Manual override requires permission and reason.

## 5. Acceptance Tests

- Given Trust Engine disabled, when customer opens Food checkout in MVP, then no COD appears.
- Given a future privilege requires T3, when T2 customer attempts it, then the privilege is unavailable.
- Given fraud restriction exists, when trust level is high, then restricted privilege remains blocked.

## 6. Open Questions

- Trust scoring formula.
- Whether Trust is visible to customers.
- Whether manual override expiry is required.
