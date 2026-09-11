# PRD: Food Direct QR Bank Transfer Confirmation

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, API Core Backend, Admin Portal  

## 1. Objective

Ensure Food orders proceed only after customer transfers money directly to assigned driver and uploads required proof.

## 2. Scope

In scope:

- Payment prompt after driver assignment.
- Driver bank/QR display.
- Customer proof upload.
- Driver receipt confirmation.
- Blocking driver purchase until proof exists.
- Payment/no-show dispute link.

Out of scope:

- COD.
- Cash.
- Payment gateway.
- Wallet/escrow.

## 3. Food Payment State Model

Suggested states:

- `awaiting_driver_assignment`
- `awaiting_customer_transfer`
- `proof_submitted`
- `driver_confirmed_received`
- `driver_reported_not_received`
- `payment_disputed`
- `admin_review_required`

## 4. User Stories

### US-01 - Customer sees assigned driver transfer details

As a customer, I want to transfer order amount directly to the driver after assignment.

Acceptance criteria:

- App shows driver bank/QR details.
- Amount includes item estimate and delivery fee according to order policy.
- Copy clarifies payment is direct to driver, not to Onway.

### US-02 - Customer uploads payment proof

As a customer, I must upload payment proof before driver buys food.

Acceptance criteria:

- Proof image is mandatory.
- Proof links to Food order.
- Proof submission triggers driver notification.
- Customer can view proof submitted state.

### US-03 - Driver waits for payment proof before purchase

As a driver, I cannot start restaurant purchase flow until customer payment proof is submitted.

Acceptance criteria:

- Purchase/start-to-restaurant action is blocked until proof state meets policy.
- Driver can view proof.
- Driver can confirm received or report not received.

### US-04 - Customer disputes driver no-show after payment

As a customer, I want to complain if I transferred money and driver does not proceed.

Acceptance criteria:

- Complaint flow can prefill order and proof.
- Case type routes to paid-but-driver-no-show dispute.
- Driver risk lock counter can update.

## 5. Acceptance Tests

- Given Food order assigned, when customer has not uploaded proof, then driver cannot start purchase flow.
- Given customer uploads proof, when driver opens order, then proof is visible.
- Given driver reports not received, then order enters payment dispute/admin review state.
- Given customer files no-show complaint after proof, then complaint links to order and proof automatically.

## 6. Open Questions

- Whether amount includes estimated food total plus delivery fee or separate transfers.
- Whether proof can be replaced before driver confirms.
- Whether admin can override payment state.

