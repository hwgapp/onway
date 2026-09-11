# PRD: Food Driver Matching & Accept/Reject

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, API Core Backend, Admin Portal  

## 1. Objective

Match a confirmed Food order to an eligible driver who can accept/reject the delivery job with no fee negotiation.

## 2. Scope

In scope:

- Food matching candidate filtering.
- Progressive batched offers.
- Driver accept/reject.
- Atomic assignment.
- No-match flow.
- Customer waiting state.
- Admin monitoring.

Out of scope:

- Driver counter-offer.
- Customer fee negotiation.
- Merchant confirmation.

## 3. Matching Requirements

Driver must be:

- Active.
- Online.
- Not locked/suspended/blocked.
- Eligible for Food.
- In valid region.
- Close enough to outlet/customer route according to policy.
- Not on incompatible active job.

## 4. User Stories

### US-01 - Driver receives Food offer

As a driver, I want enough detail to decide whether to accept a Food job.

Acceptance criteria:

- Offer shows outlet, delivery area, estimated pickup/drop distance, item count or order summary, delivery fee, expected payment flow, timeout.
- Driver can accept/reject.
- No counter-offer UI exists.

### US-02 - Customer waits for driver assignment

As a customer, I want to know the order is finding a driver.

Acceptance criteria:

- Customer sees matching state.
- Customer can cancel before driver assignment if policy allows.
- No payment transfer prompt appears until driver is assigned.

### US-03 - System assigns first valid driver

As backend, I need one driver assigned to the Food order.

Acceptance criteria:

- Atomic accept prevents double assignment.
- Assignment triggers payment transfer step.
- Non-winning offers are cancelled/expired.

## 5. Acceptance Tests

- Given driver not Food eligible, when Food matching runs, then driver is excluded.
- Given two drivers accept same Food offer, then only one succeeds.
- Given no driver accepts, when max attempts reached, then order becomes no-driver-found and customer can retry/cancel.
- Given customer cancels before assignment, then outstanding offers are cancelled.

## 6. Admin Monitoring

- Active Food matching sessions.
- Candidate count/batches.
- Order assignment result.
- Driver response history.

## 7. Open Questions

- Whether Food matching prioritizes driver near outlet or near customer.
- Exact timeout/batch/radius policy.
- Whether driver sees full item list before accept.

