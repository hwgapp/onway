# PRD: Ride Tracking & In-Trip Flow

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, API Core Backend, Admin Portal  

## 1. Objective

Support the ride lifecycle after driver assignment through driver arrival, pickup, trip start, live tracking, chat, and trip progress updates.

## 2. Scope

In scope:

- Assigned driver details.
- Driver route to pickup.
- Customer-driver chat.
- Driver arrival.
- Trip start.
- In-trip tracking.
- Basic safety/support entry point.
- Admin monitoring.

Out of scope:

- In-app voice calling.
- Number masking.
- Scheduled ride.
- Route optimization beyond provider route/ETA.

## 3. Ride State Model

Suggested states:

- `assigned`
- `driver_en_route_to_pickup`
- `driver_arrived`
- `awaiting_payment_if_required`
- `ready_to_start`
- `in_progress`
- `arrived_at_destination`
- `completed`
- `cancelled`
- `disputed`

## 4. User Stories

### US-01 - Customer sees assigned driver

As a customer, I want to see driver and vehicle details after match so I know who is coming.

Acceptance criteria:

- Customer sees driver name, rating placeholder if available, vehicle type, vehicle identifier fields if available.
- Customer sees driver ETA/location.
- Customer can open chat.

### US-02 - Driver navigates to pickup

As a driver, I want pickup location and customer contact/chat so I can reach the pickup point.

Acceptance criteria:

- Driver sees pickup address/map.
- Driver can mark arrived only near pickup or with policy override.
- Driver can chat/send image.

### US-03 - Driver starts ride

As a driver, I want to start trip only after required preconditions are complete.

Acceptance criteria:

- Required preconditions are checked server-side.
- If bank transfer is required before start, proof/confirmation state must satisfy policy.
- Start action writes timeline event.

### US-04 - Customer tracks ride

As a customer, I want to track the ride while in progress.

Acceptance criteria:

- Customer receives location updates.
- App shows ride state and route/destination summary.
- If connection drops, app can reload current state.

## 5. Acceptance Tests

- Given driver is assigned, when customer opens ride, then driver details and chat are available.
- Given driver is far from pickup, when marking arrived, then backend rejects unless override policy allows.
- Given required payment proof missing, when driver starts ride, then API blocks.
- Given driver completes trip, when customer app receives event, then completion/payment/rating flow opens.

## 6. Admin Monitoring

- Active ride list.
- Ride timeline.
- Driver/customer chat link.
- Location snapshots.
- Manual support markers.

## 7. Open Questions

- Exact ride payment timing.
- GPS distance threshold for arrived/start/complete.
- Whether phone number remains visible now chat exists.

