# PRD: Notification & Realtime Events

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, Admin Portal, API Core Backend  

## 1. Objective

Define realtime and notification behavior for matching, tracking, chat, payment proof, state changes, and operational alerts.

## 2. Scope

In scope:

- WebSocket connection/session.
- Driver location updates.
- Matching offers and responses.
- Ride/Food tracking events.
- Chat events.
- Payment proof submitted/confirmed events.
- Account lock/status events.
- Push/in-app notification strategy.

Out of scope:

- Marketing push campaigns.
- Complex notification preferences.

## 3. Event Categories

- `presence.*`
- `matching.*`
- `ride.*`
- `food_order.*`
- `payment_proof.*`
- `chat.*`
- `driver_status.*`
- `complaint.*`
- `admin_monitoring.*`

## 4. User Stories

### US-01 - Driver receives matching offer realtime

As a driver, I need job offers to arrive instantly with timeout countdown.

Acceptance criteria:

- Offer is delivered through WebSocket when driver is connected.
- Push fallback can notify if supported and appropriate.
- Offer includes expiry timestamp from server.
- Accept/reject response is acknowledged by server.

### US-02 - Customer sees job progress

As a customer, I want live updates for driver assigned, arriving, started, purchasing, delivering, and completed states.

Acceptance criteria:

- Customer subscribes to ride/order room after creation.
- State updates are emitted after backend persistence.
- App can recover state from GraphQL after reconnect.

### US-03 - Driver/customer chat realtime

As customer and driver, I want chat messages and images to appear promptly.

Acceptance criteria:

- Chat message event includes room, sender, message type, timestamp, and delivery state.
- Image messages reference media upload ID.
- Unauthorized users cannot subscribe to room.

### US-04 - Admin sees operational events

As admin, I want monitoring screens to update when rides/orders or complaints change.

Acceptance criteria:

- Admin receives low-frequency operational events or refresh prompts.
- Admin can always query source-of-truth through GraphQL.

## 5. Acceptance Tests

- Given driver disconnects during offer, when timeout passes, then offer expires server-side.
- Given customer reconnects after app background, when they open active ride, then GraphQL state and WebSocket stream resync.
- Given locked driver receives status event, when app processes it, then online state is disabled.
- Given unauthorized customer tries to join another order room, when WebSocket auth runs, then subscription is rejected.

## 6. Reliability Requirements

- Events should be idempotent or carry sequence/timestamp where needed.
- Client must tolerate duplicated or delayed events.
- Critical transitions are persisted before events.
- WebSocket must authenticate with Firebase-derived token or backend session mechanism.

## 7. Open Questions

- Push provider details for Flutter apps.
- Event naming/versioning convention.
- Whether admin monitoring needs realtime at MVP or polling is enough.

