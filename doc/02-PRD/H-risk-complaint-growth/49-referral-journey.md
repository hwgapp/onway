# PRD: Referral Journey

**Phase:** P1  
**Status:** Draft  
**Platforms:** Customer App, Driver App, Admin Portal, API Core Backend  

## 1. Objective

Define future customer and driver referral flows that can support growth after core Ride/Food launch is stable.

## 2. MVP Position

Referral is not required for core P0 launch. It should be designed with fraud gating before any reward payout.

## 3. Scope

Future scope:

- Customer referral code/link.
- Driver referral code/link.
- Attribution.
- Eligibility conditions.
- Fraud hold.
- Admin review/override.
- Reward status.

Out of scope:

- Onway wallet credits in MVP.
- Instant payout without validation.

## 4. User Stories

### US-01 - Customer shares referral

As a customer, I want to share a referral code/link.

Acceptance criteria:

- Customer has unique referral identifier.
- Referred customer can apply code at signup or first order.
- Attribution is stored once and protected against self-referral.

### US-02 - Driver refers driver

As a driver, I want to refer another driver and receive reward after they qualify.

Acceptance criteria:

- Referred driver must verify, activate, complete required real activity, and pass fraud check.
- Reward remains pending during fraud hold.
- Admin can inspect referral chain.

### US-03 - System blocks suspicious referral

As Onway, I need fraud controls before reward eligibility.

Acceptance criteria:

- Self-referral and duplicate device/phone/account signals are flagged.
- Suspicious rewards are held for review.
- Rejected referrals do not pay.

## 5. Acceptance Tests

- Given referred customer has no valid first completed order, then reward remains pending.
- Given self-referral detected, when reward eligibility runs, then reward is rejected/held.
- Given admin approves held referral, then reward status changes with audit reason.
- Given referral code is reused by same person, then duplicate attribution is blocked.

## 6. Open Questions

- Reward payment method if no wallet.
- Exact customer/driver reward values at launch.
- Fraud hold duration.

