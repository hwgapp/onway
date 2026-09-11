# PRD: Driver Platform Fee, Subscription & Refund

**Phase:** P0  
**Status:** Draft  
**Platforms:** Driver App, Admin Portal, API Core Backend  

## 1. Objective

Define MVP driver platform fee flow, manual bank transfer/QR proof, admin verification, activation dependency, and refund policy tracking.

## 2. Scope

In scope:

- Initial platform fee: `1.000.000 VND`.
- Includes 12 paid months plus 6 launch bonus months.
- Driver bank transfer/QR proof upload.
- Admin manual verification.
- Activation dependency.
- Refund calculation record for unused paid quarters.
- Future subscription placeholder.

Out of scope:

- Payment gateway.
- Wallet.
- Automatic bank reconciliation.
- Final legal wording.

## 3. Fee Rules

- Fee is platform/software usage fee, not deposit or escrow.
- Launch offer gives total 18 months usage: 12 paid + 6 bonus.
- No recurring subscription during first 18 months unless policy changes.
- Refund applies only to unused paid quarters of the 12-month paid portion.
- Bonus 6 months has no cash/refund value.

## 4. User Stories

### US-01 - Driver sees fee instruction

As a driver applicant, I want clear transfer instructions so I can pay platform fee and become eligible for activation.

Acceptance criteria:

- Driver sees amount, recipient account/QR, transfer note/reference, and proof requirement.
- Copy does not call fee deposit/guarantee/fraud fund.
- Driver cannot be activated until fee is verified or waived.

### US-02 - Driver uploads platform fee proof

As a driver applicant, I want to upload transfer proof and reference so admin can verify.

Acceptance criteria:

- Proof image is required.
- Optional transfer reference/note can be submitted.
- Submission creates verification record.
- Driver sees pending review status.

### US-03 - Admin verifies fee

As a driver review admin, I want to approve/reject platform fee proof.

Acceptance criteria:

- Admin sees proof image, submitted metadata, driver profile, and history.
- Admin can approve/reject/request resubmission with reason.
- Approval can unlock activation if other requirements are met.
- Decision writes audit log.

### US-04 - Admin sees refund schedule

As admin/support, I want refund information based on activation date so cancellation/support cases can be handled consistently.

Acceptance criteria:

- System stores activation date.
- Refund schedule computes unused paid quarters.
- Bonus months show zero refund value.

## 5. Acceptance Tests

- Given driver has approved onboarding but fee pending, when activation check runs, then driver remains pending platform fee.
- Given admin approves fee proof, when all other conditions are met, then driver can become active.
- Given driver stops in first paid quarter, when refund estimate is requested, then unused paid quarters equal 750,000 VND according to policy.
- Given admin rejects proof, when driver app refreshes, then status shows resubmission required.

## 6. Open Questions

- Exact bank account/QR owner per region.
- Legal-approved fee/refund copy.
- Whether future 500,000 VND application fee is collected before or after approval.

