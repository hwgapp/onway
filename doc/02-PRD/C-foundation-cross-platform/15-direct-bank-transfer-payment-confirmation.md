# PRD: Direct Bank Transfer & Payment Confirmation

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, Admin Portal, API Core Backend  

## 1. Objective

Define MVP direct bank transfer/QR payment confirmation flows where money moves directly between customer and driver and never through Onway.

## 2. Scope

In scope:

- Driver bank/QR details display.
- Customer payment proof upload.
- Driver receipt confirmation or issue report.
- Payment state machine.
- Admin evidence review.
- Audit trail.

Out of scope:

- COD.
- Cash.
- Payment gateway.
- Wallet.
- Onway settlement or payout.
- Automated bank reconciliation.

## 3. Payment State Model

Suggested states:

- `not_required_yet`
- `awaiting_customer_transfer`
- `proof_submitted`
- `driver_confirmed_received`
- `driver_reported_not_received`
- `admin_review_required`
- `confirmed_by_admin`
- `rejected_by_admin`
- `disputed`

## 4. User Stories

### US-01 - Customer uploads required transfer proof

As a customer, I want to upload payment proof after transferring so service can continue.

Acceptance criteria:

- Customer sees transfer recipient details and amount.
- Customer cannot continue without required proof.
- Proof upload links to ride/order.
- Proof submission timestamp is recorded.

### US-02 - Driver confirms or disputes receipt

As a driver, I want to confirm I received transfer or report a payment issue.

Acceptance criteria:

- Driver sees payment proof for assigned job only.
- Driver can mark received.
- Driver can report not received with reason.
- Both actions write timeline and audit events.

### US-03 - Admin reviews payment dispute

As admin, I want to inspect proof, chat, timeline, and account history to decide a dispute.

Acceptance criteria:

- Admin case view shows payment evidence and linked job.
- Admin can mark confirmed/rejected/disputed with reason.
- Decision updates job/payment state if policy allows.

## 5. Acceptance Tests

- Given proof is required, when customer submits order without proof, then API rejects.
- Given customer submits proof, when driver opens job, then proof is visible.
- Given driver reports not received, when admin portal opens monitoring, then job is flagged.
- Given payment state is confirmed, when customer attempts replacing proof, then API blocks unless admin flow permits.

## 6. Security & Abuse Controls

- Payment proof is evidence, not guaranteed payment verification.
- App copy must avoid implying Onway processed or held money.
- Payment evidence must be role-protected.
- Suspicious repeated payment disputes should feed risk/complaint workflow.

## 7. Open Questions

- Exact Ride timing for transfer.
- Whether proof image requires in-app camera or can use gallery.
- Whether customer can upload multiple proof images.

