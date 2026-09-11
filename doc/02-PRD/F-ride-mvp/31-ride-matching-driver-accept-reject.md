# PRD: Ride Matching & Driver Accept/Reject

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, API Core Backend, Admin Portal  

## 1. Objective

Match a confirmed Ride request to an eligible driver using progressive batched matching and support driver accept/reject within timeout.

## 2. Scope

In scope:

- Candidate filtering.
- Candidate ranking.
- Progressive batched offers.
- Offer timeout.
- Driver accept/reject.
- Atomic assignment.
- No-match/timeout result.
- Admin monitoring.

Out of scope:

- Driver counter-offer.
- Customer-driver negotiation in P0.
- Manual dispatch as default.

## 3. Matching Strategy

P0 uses progressive batched matching:

- Filter eligible drivers by account, lock status, online presence, service, vehicle, region, proximity.
- Rank by ETA/distance, availability, completion/cancel signals if available, and operational policy.
- Send offers to small batch, e.g. 3-5 drivers.
- Wait configured timeout, e.g. 15-20 seconds.
- If no accepted offer, expand radius/batch and retry until max attempts/time.
- First valid accept wins via atomic lock.
- Other offers become expired/cancelled.

## 4. Matching State Model

Suggested states:

- `queued`
- `batch_offered`
- `driver_accepted`
- `assigned`
- `no_driver_available`
- `expired`
- `cancelled_by_customer`

Offer states:

- `sent`
- `accepted`
- `rejected`
- `expired`
- `cancelled_assignment_taken`

## 5. User Stories

### US-01 - System filters eligible drivers

As the matching system, I need to consider only drivers who can legally and operationally serve the ride.

Acceptance criteria:

- Driver must be active, online, not locked/suspended/blocked.
- Driver vehicle type must match request.
- Driver current location must be in eligible region/polygon.
- Driver must not already be on another incompatible job.

### US-02 - Driver receives offer

As a driver, I want clear offer details so I can accept or reject safely.

Acceptance criteria:

- Offer includes pickup area, dropoff area, vehicle/service type, estimated distance/time, recommended fare, and timeout.
- Driver can accept or reject once.
- Expired offer cannot be accepted.

### US-03 - Customer waits during matching

As a customer, I want to see matching progress and have the option to cancel before assignment.

Acceptance criteria:

- Customer sees searching/matching state.
- Customer can cancel before driver assignment.
- If no driver found, app shows no-match result and retry option.

### US-04 - System assigns first valid accept

As the backend, I need atomic assignment to avoid two drivers being assigned.

Acceptance criteria:

- First valid accepted offer locks assignment.
- Later accepts fail with already-assigned response.
- Customer and assigned driver receive realtime assignment events.

## 6. Acceptance Tests

- Given two drivers accept same ride near-simultaneously, when backend processes accepts, then only one assignment succeeds.
- Given driver is locked during offer, when they accept, then accept is rejected.
- Given all batches timeout, when max attempts reached, then ride becomes no-driver-available.
- Given customer cancels during matching, when drivers still have offers, then offers are cancelled.

## 7. Admin Monitoring

- View active matching sessions.
- View candidate count, batch count, timeout, and final result.
- Inspect assignment timeline for support.

## 8. Open Questions

- Exact initial radius, expansion radius, batch size, timeout, and max attempts.
- Whether admin can manually assign in exceptional cases.
- Whether ranking includes driver acceptance history in P0.

