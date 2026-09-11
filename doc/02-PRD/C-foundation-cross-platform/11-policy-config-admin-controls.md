# PRD: Policy Config & Admin Controls

**Phase:** P0  
**Status:** Draft  
**Platforms:** Admin Portal, API Core Backend  

## 1. Objective

Make business numbers, thresholds, limits, statuses, and operational rules configurable without redeploy whenever they may change.

## 2. Scope

Policy config includes:

- Matching timeout, batch size, radius expansion.
- Pricing guardrails.
- Food waiting policy.
- Payment proof requirements.
- Complaint threshold for driver auto-lock.
- Chat retention duration.
- Media limits.
- Driver platform fee values and refund rules.
- Region service/vehicle availability.

Out of scope:

- Full experimentation platform.
- Dynamic ML policy engine.

## 3. User Stories

### US-01 - Admin updates operational threshold

As an admin, I want to update thresholds like auto-lock complaint count so operations can adjust risk controls quickly.

Acceptance criteria:

- Config key has type, allowed range, description, owner, and default.
- Update requires permission and reason.
- Change writes audit log.
- New value applies to future decisions.

### US-02 - Backend evaluates policy consistently

As the backend, I need one policy source so Customer App, Driver App, and Admin Portal do not implement conflicting rules.

Acceptance criteria:

- Business rules are evaluated server-side.
- Apps receive allowed actions/next actions from API.
- Policy version used in decision is recorded where needed.

### US-03 - Admin can roll back bad config

As an admin, I want to revert a recent config change if it causes operational issues.

Acceptance criteria:

- Config history is visible.
- Admin can restore previous value where safe.
- Restore writes new audit event rather than deleting history.

## 4. Acceptance Tests

- Given matching timeout config changes from 20s to 15s, when new offers are created, then offer expiry uses 15s.
- Given chat retention config is 7 days, when retention job runs, then content older than policy is processed.
- Given unauthorized admin attempts config change, when mutation runs, then API rejects and logs denied attempt if policy requires.
- Given invalid config value outside range, when admin saves, then validation blocks save.

## 5. Config Data Requirements

- Key.
- Value.
- Type.
- Scope: global, country, city, region, service, vehicle, brand.
- Effective start/end if needed.
- Status.
- Version.
- Last updated by/at.
- Reason.

## 6. Admin UI Requirements

- Searchable config list.
- Safe editors by type: number, boolean, enum, duration, money, JSON where unavoidable.
- Change preview.
- History panel.
- Permission guard.

## 7. Open Questions

- Whether initial config is seeded by migration or admin UI.
- Which configs need regional override at MVP.
- Whether dual approval is required for high-risk values.

