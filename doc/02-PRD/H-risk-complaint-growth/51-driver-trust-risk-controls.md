# PRD: Driver Trust & Risk Controls

**Phase:** P2  
**Status:** Draft  
**Platforms:** Driver App, Admin Portal, API Core Backend  

## 1. Objective

Reserve future Driver Trust system for risk-aware job eligibility, priority, high-value orders, mission access, and account restrictions after MVP launch.

## 2. MVP Position

P0 uses basic account/risk statuses and manual/threshold lock. Full Driver Trust levels D0-D4 are not required for launch.

## 3. Future Scope

- Driver Trust levels D0-D4.
- Completion/cancellation/complaint/fraud signals.
- GPS anomaly signals.
- Mission quality signals.
- Eligibility restrictions.
- Admin visibility/override.

## 4. User Stories

### US-01 - System computes driver trust

As Onway, I want driver trust to reflect reliability and risk.

Acceptance criteria:

- Trust uses approved signals.
- Formula is not fully exposed to prevent gaming.
- Trust history is auditable.

### US-02 - Matching considers driver trust

As matching system, I want trust/risk to influence job eligibility and ranking.

Acceptance criteria:

- Low trust can restrict high-value or sensitive jobs.
- Trust cannot override locked/suspended state.
- Ranking use is configurable.

### US-03 - Admin reviews driver trust

As admin, I want to understand why a driver is restricted.

Acceptance criteria:

- Admin sees level, restrictions, recent signal summary.
- Manual override requires reason.
- Override is audited.

## 5. Acceptance Tests

- Given driver is locked, when Trust level is high, then matching still excludes driver.
- Given driver has repeated confirmed complaints, when trust recalculates, then level/restriction updates according to policy.
- Given admin overrides restriction, then audit log records action and expiry if any.

## 6. Open Questions

- Exact trust formula.
- Whether driver sees their level.
- Whether trust affects subscription/refund decisions.

