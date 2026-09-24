# State Management

## Client State

- Customer App and Driver App use Flutter app-local state plus generated API models once GraphQL client strategy is chosen.
- Admin Portal uses React state/data-fetching around GraphQL typed operations.
- Client state must model loading, empty, error, offline/reconnect, no permission and policy-blocked states for critical flows.
- Driver App must clearly show online/offline, active offer, active ride/order, background location state and payment confirmation state.

## Server State / Cache

- PostgreSQL is system of record for trips/orders, users, policies, evidence metadata, fraud/complaint and audit.
- Redis stores short-lived presence, last known driver location, active offer locks, matching wave state, cache and BullMQ queues.
- Matching uses atomic lock in Redis or database so one driver has only one active offer.
- Driver presence/location in Redis can be snapshotted to PostgreSQL when needed for audit, dispute or analytics.
- Policy/config values must be versioned and auditable; avoid hard-code for fees, thresholds and timeouts.

## State Machines

| Flow | States |
| --- | --- |
| Ride | REQUESTED -> MATCHING -> MATCHED -> PAYMENT_PENDING -> MONEY_RECEIVED -> DRIVER_EN_ROUTE -> ARRIVED -> STARTED -> COMPLETED; terminal/side states: CANCELED, PAYMENT_DISPUTED, EXPIRED |
| Food | CREATED -> MATCHING -> MATCHED -> PAYMENT_PENDING -> MONEY_RECEIVED -> DRIVER_TO_OUTLET -> ORDERING -> ORDER_PLACED -> PICKED_UP -> DELIVERED; terminal/side states: CANCELED, PAYMENT_DISPUTED |
| Food change proposal | PROPOSED -> ACCEPTED/REJECTED/TIMEOUT; default timeout 5 minutes configurable |
| Fraud case | REPORTED -> EVIDENCE_COLLECTION -> DRIVER_RESPONSE -> HUMAN_REVIEW -> HUMAN_DECISION -> CONFIRMED/REJECTED -> APPEAL -> FINALIZED |
| Region config | PLANNED -> PILOT -> ACTIVE -> PAUSED -> CLOSED; publish blocked when invalid polygon or overlap same service/vehicle |
| Driver lock | UNLOCKED -> MANUAL_LOCKED/AUTO_LOCKED -> UNDER_REVIEW -> UNLOCKED/FINAL_LOCKED; SLA review target 24h |

## Offline / Sync

- Driver and Customer apps must handle WebSocket reconnect and refetch history when sequence gaps occur.
- Chat supports retry/refetch; room is open only for active Ride/Food and authorized admin/operator.
- Offline-first is not a P0 requirement, but critical actions need safe retry/idempotency where duplicate taps/network retries can happen.
- Background location requires consent, visible status, battery strategy and retention policy before implementation.
- Mobile apps must call min-version policy on app start and show soft/hard update UI when backend config requires it.
