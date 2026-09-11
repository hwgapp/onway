# PRD: Community Truth Verification

**Phase:** P2  
**Status:** Draft  
**Platforms:** API Core Backend, Admin Portal, Driver App  

## 1. Objective

Define future Community Truth model where important restaurant/menu data is verified by evidence, independent contributors, and confidence rather than single-user assertion.

## 2. MVP Position

Not required for P0 launch. P0 uses admin-managed catalog and manual publishing.

## 3. Future Scope

- Field value verification.
- Evidence linking.
- Multiple independent verifier requirement.
- Conflict handling.
- Confidence scoring.
- Publish/update rules.
- Admin exception review.

## 4. Community Truth Model

Each verifiable field may store:

- Current value.
- Evidence references.
- Verification status.
- Verifier count.
- Independent verifier count.
- Confidence.
- Last verified at.
- Conflict state.

## 5. User Stories

### US-01 - System combines independent evidence

As Onway, I want at least two independent drivers before important data becomes verified.

Acceptance criteria:

- Verifier independence is checked using allowed signals.
- Duplicate/suspicious evidence does not count as independent.
- Field reaches verified only after threshold and confidence policy.

### US-02 - Conflict triggers exception

As operations, I want conflicting evidence to create a review path.

Acceptance criteria:

- Conflicting submissions do not auto-publish.
- System can request third verification or admin review.
- Conflict history is visible.

### US-03 - Admin reviews truth state

As admin, I want to see value, evidence, confidence, and history.

Acceptance criteria:

- Admin can inspect evidence behind a value.
- Manual override requires reason.
- Override is audited.

## 6. Acceptance Tests

- Given one driver submits price update, then field remains unverified.
- Given two independent matching submissions exist, then field can become verified according to policy.
- Given two conflicting submissions exist, then field enters conflict/review state.

## 7. Open Questions

- Confidence formula.
- Independence signals.
- Which fields use Community Truth first.

