# PRD General: API Core Backend

**Phase:** P0  
**Status:** Draft  
**Platform:** API Core Backend  

## 1. Objective

Define the backend product boundary for Onway MVP. The API Core Backend is responsible for business truth, state transitions, policy enforcement, audit, realtime coordination, and admin operations.

## 2. Scope

Backend must support:

- Identity role mapping and account status.
- Region, currency, and service availability.
- Driver onboarding, platform fee verification, eligibility, location presence.
- Restaurant brand/outlet/menu catalog and publishing.
- Ride lifecycle.
- Food lifecycle.
- Matching lifecycle.
- Direct bank transfer confirmation and payment proof.
- Chat room metadata and media attachment references.
- Complaint/dispute/fraud/risk lock.
- Policy config and audit log.

## 3. Domain Modules

Expected modules:

- `identity`
- `customer`
- `driver`
- `admin`
- `region`
- `vehicle`
- `pricing`
- `matching`
- `ride`
- `food-order`
- `restaurant`
- `menu`
- `direct-payment-proof`
- `chat`
- `complaint`
- `fraud`
- `platform-fee`
- `notification`
- `media-evidence`
- `audit-log`
- `policy-config`

## 4. API Requirements

- GraphQL is primary API for structured business data.
- WebSocket Gateway handles realtime events: location, matching offers, tracking, chat messages, status updates.
- API must validate Firebase ID token and map to internal actor.
- API must enforce account status, driver lock, service eligibility, and region availability.
- All state transitions must be explicit and auditable.

## 5. User Stories

### US-01 - Apps can read and mutate business data

As app clients, Customer App, Driver App, and Admin Portal need GraphQL operations for profiles, orders, trips, catalog, config, and disputes.

Acceptance criteria:

- Each operation checks actor authorization.
- Mutations return updated state and next allowed actions.
- Invalid state transitions are rejected with typed errors.

### US-02 - Realtime events stay separate from business truth

As the backend, I need realtime events to update UX quickly without making Redis/WebSocket the system of record.

Acceptance criteria:

- WebSocket events reference persisted ride/order/job IDs where applicable.
- Critical state changes are persisted before final events are emitted.
- Redis presence expiry does not delete historical trip/order truth.

### US-03 - Admin can inspect state history

As an admin, I need complete state history for dispute and fraud review.

Acceptance criteria:

- Ride/order/payment/dispute state changes write audit logs.
- Audit log includes actor, action, timestamp, before/after where safe, and reason.
- Admin APIs can filter timeline by entity.

## 6. Acceptance Tests

- Given a locked driver, when matching tries to offer a job, then backend excludes the driver.
- Given a customer uploads payment proof, when proof mutation succeeds, then order/trip timeline includes proof submitted event.
- Given a driver confirms receipt, when admin opens timeline, then both customer proof and driver confirmation are visible.
- Given a stale/expired WebSocket connection, when location update is absent, then presence expires without altering persisted driver status incorrectly.

## 7. Data Principles

- PostgreSQL/PostGIS stores source-of-truth records.
- Redis stores short-lived presence and matching state.
- S3 stores media/evidence objects; database stores references and metadata.
- Audit records are append-only.
- Policy config is versioned or timestamped so decisions can be explained later.

## 8. Open Questions

- Exact GraphQL schema conventions.
- Queue technology: BullMQ on Redis or AWS SQS.
- Exact retention behavior for chat/media after 1 week.

