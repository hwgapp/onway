# PRD: Mission Engine

**Phase:** P2  
**Status:** Draft  
**Platforms:** Driver App, Admin Portal, API Core Backend  

## 1. Objective

Define future Mission Engine that assigns field tasks to drivers for restaurant/menu verification, referral, and local operations after MVP launch.

## 2. MVP Position

Mission Engine is not a P0 dependency. P0 Food supply is admin-first. Drivers do not manage restaurant/menu data in launch MVP.

## 3. Future Scope

- Mission templates.
- Mission generation.
- Driver mission discovery/acceptance.
- Evidence submission.
- AI/manual QA.
- Reward eligibility.
- Fraud checks.
- Admin monitoring.

## 4. Mission Types

Potential types:

- Verify outlet.
- Capture full menu.
- Verify opening hours.
- Capture restaurant photos.
- Verify price.
- Verify closure.
- Referral customer.
- Referral driver.

## 5. User Stories

### US-01 - Admin creates mission template

As admin, I want mission templates so recurring field work is standardized.

Acceptance criteria:

- Template defines objective, required evidence, eligible drivers, region, reward, expiry.
- Template changes are audited.

### US-02 - Driver accepts mission

As a driver, I want to accept available missions near me.

Acceptance criteria:

- Driver sees missions only if eligible.
- Mission has clear instructions and expiry.
- Driver can accept/start/submit.

### US-03 - System validates mission submission

As Onway, I need submissions reviewed before reward.

Acceptance criteria:

- Submission requires required evidence.
- Reward is not paid only because driver taps submit.
- QA/fraud checks gate reward eligibility.

## 6. Acceptance Tests

- Given mission requires in-app camera photo, when driver submits without photo, then API rejects.
- Given driver not eligible, when querying missions, then mission is hidden.
- Given submission fails QA, then reward remains not eligible.

## 7. Open Questions

- Reward payment method.
- Eligibility criteria.
- Whether AI QA is required before first mission launch.

