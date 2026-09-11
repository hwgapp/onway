# PRD: Ride Completion & Direct Bank Transfer Confirmation

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, API Core Backend, Admin Portal  

## 1. Objective

Complete Ride trips with direct bank transfer/QR payment confirmation and required payment proof while keeping money outside Onway.

## 2. Scope

In scope:

- Completion trigger.
- Fare summary.
- Driver bank/QR details.
- Customer payment proof upload.
- Driver receipt confirmation.
- Payment dispute path.
- Admin review.

Out of scope:

- COD.
- Cash.
- Payment gateway.
- Wallet.

## 3. Payment Timing

Open decision from Master PRD: exact Ride transfer timing must be chot. This PRD supports either:

- before trip start; or
- at trip completion.

Implementation should model payment state flexibly so policy can choose required timing.

## 4. User Stories

### US-01 - Driver marks arrived/completed

As a driver, I want to mark the ride complete when customer reaches destination.

Acceptance criteria:

- Completion action validates active in-progress ride.
- Completion captures timestamp and location snapshot where allowed.
- Customer receives completion/payment event.

### US-02 - Customer uploads ride payment proof

As a customer, I want to transfer fare directly to driver and upload proof.

Acceptance criteria:

- App shows final fare, currency, and driver bank/QR details.
- Proof image is required.
- Proof is linked to ride.
- Customer can submit complaint if driver disputes unfairly or service issue exists.

### US-03 - Driver confirms receipt

As a driver, I want to confirm I received transfer.

Acceptance criteria:

- Driver sees submitted proof.
- Driver can mark received or report not received.
- Confirmation closes payment step according to policy.

### US-04 - Admin reviews ride payment dispute

As admin, I want to review payment proof, chat, and timeline.

Acceptance criteria:

- Disputed payment appears in admin queue.
- Admin can mark confirmed/rejected/disputed.
- Decision writes audit event.

## 5. Acceptance Tests

- Given ride is not in progress, when driver marks complete, then API rejects.
- Given payment proof is required, when customer tries to finish without proof, then app blocks next step.
- Given driver reports not received, when admin opens case, then ride timeline and proof are visible.
- Given payment confirmed, when rating flow opens, then both parties can rate if policy allows.

## 6. Data Requirements

- Final fare.
- Currency.
- Transfer recipient details snapshot.
- Payment proof evidence ID.
- Customer submitted timestamp.
- Driver confirmation timestamp.
- Dispute state.

## 7. Open Questions

- Final Ride payment timing.
- Whether fare can change after route deviation.
- Whether tip is supported in MVP.

