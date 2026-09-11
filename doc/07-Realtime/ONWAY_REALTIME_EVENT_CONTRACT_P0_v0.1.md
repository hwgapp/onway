# ONWAY - Realtime Event Contract P0

**Loai tai lieu:** WebSocket/Reatime Event Contract  
**Phien ban:** 0.1  
**Trang thai:** Draft  
**Ngay cap nhat:** 11/09/2026  
**Pham vi:** Driver presence, matching, tracking, chat, payment proof, account/risk status, admin monitoring  

---

# 1. Muc tieu

Define realtime contract for high-frequency and low-latency flows:

- Driver online/offline presence.
- Driver location updates.
- Matching offers.
- Ride/Food tracking.
- Customer-driver chat text/image.
- Payment proof/confirmation events.
- Driver risk lock/status updates.
- Admin operational monitoring.

GraphQL remains source of truth. WebSocket is transport for timely updates.

# 2. Transport principles

- WebSocket gateway is separate from GraphQL.
- Client authenticates using Firebase ID token.
- Server maps token to internal account/profile.
- Events are emitted after database transaction commit.
- Clients must tolerate duplicate/out-of-order events.
- Clients must resync with GraphQL after reconnect or suspected gap.
- Redis stores presence/ephemeral state; PostgreSQL stores durable business truth.

# 3. Connection lifecycle

## 3.1 Connect

Client sends:

```json
{
  "type": "connection.init",
  "token": "firebase-id-token",
  "client": {
    "app": "customer|driver|admin",
    "platform": "ios|android|web",
    "appVersion": "1.0.0",
    "deviceId": "opaque-device-id"
  }
}
```

Server responds:

```json
{
  "type": "connection.ack",
  "connectionId": "uuid",
  "accountId": "uuid",
  "roles": ["CUSTOMER"],
  "serverTime": "2026-09-11T00:00:00Z",
  "heartbeatIntervalMs": 25000
}
```

## 3.2 Heartbeat

Client -> server:

```json
{ "type": "connection.ping", "sentAt": "..." }
```

Server -> client:

```json
{ "type": "connection.pong", "sentAt": "...", "serverTime": "..." }
```

## 3.3 Reconnect

Client sends last known event cursor per room:

```json
{
  "type": "connection.resume",
  "lastSeen": [
    { "room": "ride:uuid", "sequence": 42 },
    { "room": "chat:uuid", "sequence": 11 }
  ]
}
```

Server can:

- replay recent buffered events if available;
- or respond `resync_required` so client fetches GraphQL state.

# 4. Event envelope

Every server event uses:

```json
{
  "eventId": "uuid",
  "type": "ride.status_changed",
  "room": "ride:uuid",
  "sequence": 43,
  "occurredAt": "2026-09-11T00:00:00Z",
  "entity": {
    "type": "ride",
    "id": "uuid",
    "version": 7
  },
  "payload": {}
}
```

Fields:

- `eventId`: idempotency/dedup key.
- `type`: event name.
- `room`: authorization/channel boundary.
- `sequence`: monotonically increasing per room if supported.
- `entity.version`: optional optimistic version for UI stale detection.
- `payload`: event-specific data.

# 5. Rooms and authorization

| Room | Members | Purpose |
|---|---|---|
| `account:{accountId}` | That account's active sessions | Account status, global notifications. |
| `driver:{driverProfileId}` | Driver sessions | Offers, driver status, driver job updates. |
| `customer:{customerProfileId}` | Customer sessions | Customer job updates. |
| `ride:{rideId}` | Ride customer, assigned driver, authorized admin | Ride tracking/status/chat linkage. |
| `food_order:{foodOrderId}` | Food customer, assigned driver, authorized admin | Food status/tracking/payment. |
| `chat:{chatRoomId}` | Chat participants, authorized admin viewer | Chat messages. |
| `admin:operations` | Authorized admins | Monitoring events. |
| `admin:complaints` | Authorized support admins | Complaint/dispute queue events. |

Rules:

- User cannot subscribe to a ride/order before they are a participant.
- Driver can subscribe to offer/job room only if assigned or offer sent.
- Admin room access follows RBAC.
- Server must re-check access on subscribe and on sensitive event emit if needed.

# 6. Client commands

## 6.1 Subscribe/unsubscribe

```json
{
  "type": "room.subscribe",
  "room": "ride:uuid",
  "lastSeenSequence": 12
}
```

Response:

```json
{
  "type": "room.subscribed",
  "room": "ride:uuid",
  "resyncRequired": false,
  "currentSequence": 15
}
```

Unsubscribe:

```json
{ "type": "room.unsubscribe", "room": "ride:uuid" }
```

## 6.2 Driver location update

Driver only:

```json
{
  "type": "driver.location_update",
  "clientEventId": "uuid",
  "payload": {
    "location": { "lat": 10.77, "lng": 106.69 },
    "accuracyMeters": 12.5,
    "heading": 90,
    "speedMps": 8.1,
    "capturedAt": "2026-09-11T00:00:00Z",
    "activeEntityType": "ride|food_order|null",
    "activeEntityId": "uuid"
  }
}
```

Server response:

```json
{
  "type": "driver.location_ack",
  "clientEventId": "uuid",
  "accepted": true,
  "reason": null,
  "serverTime": "..."
}
```

Rules:

- Driver must be online/on job.
- Low accuracy can be accepted as degraded or rejected by policy.
- Matching reads current presence from Redis.
- Important active-job snapshots may be persisted in PostgreSQL.

## 6.3 Typing/read receipts

Optional P0-lite:

```json
{ "type": "chat.typing", "room": "chat:uuid", "payload": { "isTyping": true } }
```

Read receipts can be added if UI needs them; not a backend launch blocker.

# 7. Presence events

## 7.1 `presence.driver_online`

Room: `driver:{driverProfileId}`, `admin:operations`

Payload:

```json
{
  "driverProfileId": "uuid",
  "vehicleId": "uuid",
  "serviceTypes": ["RIDE", "FOOD"],
  "regionId": "uuid",
  "location": { "lat": 10.77, "lng": 106.69 },
  "available": true
}
```

## 7.2 `presence.driver_offline`

Payload:

```json
{
  "driverProfileId": "uuid",
  "reason": "manual|forced|stale|locked|region_paused"
}
```

## 7.3 `presence.driver_location_changed`

Room:

- Active `ride:{rideId}` for ride tracking.
- Active `food_order:{foodOrderId}` for food tracking.
- `admin:operations` only if monitoring enabled.

Payload:

```json
{
  "driverProfileId": "uuid",
  "location": { "lat": 10.77, "lng": 106.69 },
  "accuracyMeters": 12.5,
  "heading": 90,
  "capturedAt": "..."
}
```

# 8. Matching events

## 8.1 `matching.offer_sent`

Room: `driver:{driverProfileId}`

Payload:

```json
{
  "offerId": "uuid",
  "matchingSessionId": "uuid",
  "serviceType": "RIDE",
  "entityId": "ride-or-food-order-id",
  "batchNumber": 1,
  "offeredPrice": { "amountMinor": "45000", "currencyCode": "VND" },
  "expiresAt": "...",
  "summary": {
    "pickupAddress": "text",
    "dropoffAddress": "text",
    "outletName": null,
    "estimatedDistanceMeters": 5200,
    "estimatedDurationSeconds": 900,
    "vehicleType": "MOTORCYCLE"
  }
}
```

Driver accepts/rejects through GraphQL mutation `driverRespondToOffer`, not raw WebSocket command, unless later optimized.

## 8.2 `matching.offer_expired`

Room: `driver:{driverProfileId}`

Payload:

```json
{
  "offerId": "uuid",
  "matchingSessionId": "uuid",
  "reason": "timeout|assignment_taken|customer_cancelled|driver_ineligible"
}
```

## 8.3 `matching.assigned`

Rooms:

- `customer:{customerProfileId}`
- `driver:{driverProfileId}`
- `ride:{rideId}` or `food_order:{foodOrderId}`
- `admin:operations`

Payload:

```json
{
  "serviceType": "FOOD",
  "entityId": "uuid",
  "driverProfileId": "uuid",
  "customerProfileId": "uuid",
  "chatRoomId": "uuid",
  "nextState": "AWAITING_CUSTOMER_TRANSFER"
}
```

## 8.4 `matching.no_driver_available`

Room: `customer:{customerProfileId}`

Payload:

```json
{
  "serviceType": "RIDE",
  "entityId": "uuid",
  "reason": "max_attempts_reached"
}
```

# 9. Ride events

## 9.1 `ride.status_changed`

Room: `ride:{rideId}`

Payload:

```json
{
  "rideId": "uuid",
  "fromStatus": "ASSIGNED",
  "toStatus": "DRIVER_EN_ROUTE_TO_PICKUP",
  "changedBy": { "actorType": "DRIVER", "actorId": "uuid" },
  "allowedActionsChanged": true,
  "timestamp": "..."
}
```

## 9.2 `ride.payment_required`

Room: `ride:{rideId}`

Payload:

```json
{
  "rideId": "uuid",
  "paymentRecordId": "uuid",
  "requiredBeforeEvent": "ride_start|ride_completion",
  "amount": { "amountMinor": "45000", "currencyCode": "VND" }
}
```

## 9.3 `ride.cancelled`

Room: `ride:{rideId}`

Payload:

```json
{
  "rideId": "uuid",
  "cancelledBy": "CUSTOMER|DRIVER|ADMIN|SYSTEM",
  "reason": "text-or-code",
  "paymentProofExists": false
}
```

# 10. Food order events

## 10.1 `food_order.status_changed`

Room: `food_order:{foodOrderId}`

Payload:

```json
{
  "foodOrderId": "uuid",
  "fromStatus": "PAYMENT_PROOF_SUBMITTED",
  "toStatus": "DRIVER_CONFIRMED_PAYMENT",
  "changedBy": { "actorType": "DRIVER", "actorId": "uuid" },
  "allowedActionsChanged": true,
  "timestamp": "..."
}
```

## 10.2 `food_order.payment_required`

Room: `food_order:{foodOrderId}`

Payload:

```json
{
  "foodOrderId": "uuid",
  "paymentRecordId": "uuid",
  "amount": { "amountMinor": "185000", "currencyCode": "VND" },
  "requiredBeforeEvent": "food_driver_purchase",
  "instructionsAvailable": true
}
```

## 10.3 `food_order.change_requested`

Room: `food_order:{foodOrderId}`

Payload:

```json
{
  "foodOrderId": "uuid",
  "changeRequestId": "uuid",
  "reasonType": "PRICE_CHANGE",
  "requiresCustomerDecision": true,
  "expiresAt": "..."
}
```

## 10.4 `food_order.change_decided`

Payload:

```json
{
  "foodOrderId": "uuid",
  "changeRequestId": "uuid",
  "decision": "ACCEPTED|REJECTED",
  "decidedBy": "CUSTOMER",
  "newEstimatedTotal": { "amountMinor": "190000", "currencyCode": "VND" }
}
```

# 11. Direct payment events

## 11.1 `payment.proof_submitted`

Rooms:

- `ride:{rideId}` or `food_order:{foodOrderId}`
- `driver:{driverProfileId}`

Payload:

```json
{
  "paymentRecordId": "uuid",
  "serviceType": "FOOD",
  "entityId": "uuid",
  "proofId": "uuid",
  "submittedByAccountId": "uuid",
  "submittedAt": "..."
}
```

## 11.2 `payment.driver_confirmed`

Payload:

```json
{
  "paymentRecordId": "uuid",
  "serviceType": "FOOD",
  "entityId": "uuid",
  "status": "DRIVER_CONFIRMED_RECEIVED",
  "confirmedAt": "..."
}
```

## 11.3 `payment.driver_reported_not_received`

Payload:

```json
{
  "paymentRecordId": "uuid",
  "serviceType": "FOOD",
  "entityId": "uuid",
  "status": "DRIVER_REPORTED_NOT_RECEIVED",
  "adminReviewRequired": true
}
```

# 12. Chat events

## 12.1 `chat.message_created`

Room: `chat:{chatRoomId}`

Payload:

```json
{
  "messageId": "uuid",
  "roomId": "uuid",
  "clientMessageId": "client-uuid",
  "senderAccountId": "uuid",
  "senderRole": "CUSTOMER",
  "messageType": "TEXT|IMAGE",
  "bodyText": "hello",
  "attachments": [
    {
      "mediaId": "uuid",
      "mimeType": "image/jpeg",
      "url": "signed-or-proxied-url"
    }
  ],
  "sentAt": "..."
}
```

## 12.2 `chat.message_delivery_updated`

Optional:

```json
{
  "messageId": "uuid",
  "status": "DELIVERED|READ"
}
```

## 12.3 `chat.room_closed`

Payload:

```json
{
  "roomId": "uuid",
  "closedAt": "...",
  "retentionDeleteAfter": "..."
}
```

Rules:

- Chat content/image retention: 1 week.
- Realtime does not bypass retention or authorization.
- Non-participants cannot subscribe/read.

# 13. Account/risk events

## 13.1 `driver.status_changed`

Rooms:

- `driver:{driverProfileId}`
- `admin:operations`

Payload:

```json
{
  "driverProfileId": "uuid",
  "activationStatus": "ACTIVE",
  "riskStatus": "TEMPORARILY_LOCKED",
  "reasonCode": "AUTO_LOCK_QUALIFYING_COMPLAINTS",
  "canReceiveJobs": false
}
```

Client behavior:

- Driver App disables online toggle and offer receiving when `canReceiveJobs=false`.
- If currently online, app transitions to forced offline display.

## 13.2 `account.status_changed`

Room: `account:{accountId}`

Payload:

```json
{
  "accountId": "uuid",
  "status": "SUSPENDED",
  "reasonCode": "ADMIN_ACTION",
  "allowedActionsChanged": true
}
```

# 14. Complaint/admin events

## 14.1 `complaint.created`

Rooms:

- `account:{submitterAccountId}`
- `admin:complaints`

Payload:

```json
{
  "complaintId": "uuid",
  "category": "PAID_BUT_DRIVER_NO_SHOW",
  "severity": "HIGH",
  "serviceType": "FOOD",
  "entityId": "uuid",
  "requiresAdminReview": true
}
```

## 14.2 `complaint.status_changed`

Payload:

```json
{
  "complaintId": "uuid",
  "fromStatus": "SUBMITTED",
  "toStatus": "OPEN_UNDER_REVIEW",
  "assignedAdminId": "uuid"
}
```

## 14.3 `driver.auto_locked`

Rooms:

- `driver:{driverProfileId}`
- `admin:complaints`
- `admin:operations`

Payload:

```json
{
  "driverProfileId": "uuid",
  "reasonCode": "TWO_QUALIFYING_OPEN_COMPLAINTS",
  "complaintIds": ["uuid", "uuid"],
  "lockedAt": "..."
}
```

# 15. Admin monitoring event strategy

Admin monitoring can be P0-lite.

Approach:

- Send low-frequency change events.
- Admin UI refetches GraphQL detail/list after event.
- Avoid streaming every driver GPS point to admin unless specific map view enabled.

Admin events:

- `admin.ride_changed`
- `admin.food_order_changed`
- `admin.driver_presence_changed`
- `admin.complaint_queue_changed`
- `admin.risk_action_created`
- `admin.catalog_published`

Payload minimal:

```json
{
  "entityType": "food_order",
  "entityId": "uuid",
  "changeType": "status_changed",
  "status": "DISPUTED",
  "regionId": "uuid",
  "occurredAt": "..."
}
```

# 16. Reconnect and resync rules

Clients must refetch GraphQL state when:

- WebSocket reconnects after gap.
- Server sends `resync_required`.
- Sequence number skips.
- Critical command mutation succeeds but expected event not received in timeout.
- App returns from background into active ride/order.

Server can send:

```json
{
  "type": "room.resync_required",
  "room": "food_order:uuid",
  "reason": "sequence_gap|buffer_expired|permission_changed"
}
```

# 17. Rate limits and abuse controls

P0 suggested limits:

- Driver location update: max 1 per second active job, lower when only online.
- Chat text: configurable per room/account.
- Chat image: configurable size/count.
- Subscribe attempts: rate-limited per connection/account.
- OTP/auth not handled by WebSocket.

Server should disconnect or throttle abusive clients with typed reason:

```json
{
  "type": "connection.error",
  "code": "RATE_LIMITED",
  "message": "Too many events"
}
```

# 18. Technical acceptance tests

- Customer cannot subscribe to unrelated ride room.
- Driver cannot subscribe to another driver's offer room.
- Admin without RBAC cannot subscribe to `admin:complaints`.
- Driver receives `matching.offer_sent` and can accept through GraphQL.
- Expired offer emits `matching.offer_expired`.
- Food assignment emits `food_order.payment_required`.
- Customer proof upload emits `payment.proof_submitted` to driver.
- Driver auto-lock emits `driver.status_changed` and `driver.auto_locked`.
- Chat image sends `chat.message_created` to both participants.
- Reconnect with stale sequence returns `room.resync_required`.
- Duplicate event IDs are ignored by client.

# 19. Open realtime decisions

1. Exact WebSocket library/protocol: raw ws, Socket.IO, GraphQL WS not for high-frequency location.
2. Event buffer retention duration for replay.
3. Exact sequence implementation per room in Redis/Postgres.
4. Push notification provider and fallback behavior.
5. Driver location update frequency per app state.
6. Admin map live GPS level for P0.

Resolved P0 decision:

- Driver offer accept/reject remains GraphQL mutation in P0. WebSocket is used to deliver offers and state events, not as the source-of-truth command channel.
