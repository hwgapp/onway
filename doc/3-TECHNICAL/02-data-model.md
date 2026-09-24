# Data Model

## Entities

| Entity | Purpose | Key Fields | Relations |
| --- | --- | --- | --- |
| UserIdentity | Internal identity mapped from Firebase | id, firebaseUid, phone, status, createdAt | CustomerProfile, DriverProfile, AdminUser |
| CustomerProfile | Customer account data | userId, name, phoneVerified, riskStatus | RideRequest, FoodOrder, Complaint |
| DriverProfile | Driver account and operational status | userId, activationStatus, riskStatus, onlineStatus, platformFeeStatus | Vehicle, MatchingOffer, RideTrip, FoodOrder |
| DriverDocument | Driver KYC/service documents | driverId, type, status, fileId, reviewedBy | DriverProfile, MediaEvidence |
| AdminUser | Admin/operator account | userId, roleIds, status | AuditLog |
| Role/Permission | Admin RBAC | role, permission, scope | AdminUser |
| DeviceIdentity | Pseudonymous device/risk identity | userId, hashedDeviceId, platform, appVersion, riskSignals, lastSeenAt | CustomerProfile, DriverProfile, FraudCase |
| Country/City/Region | Service geography | name, lifecycle, polygon, serviceConfig | ServiceAvailability, VehicleAvailability |
| VehicleType | Motorbike/car and future vehicles | code, name, enabled | DriverVehicle, Region config |
| DriverVehicle | Driver vehicle details | driverId, vehicleType, docsStatus, active | DriverProfile |
| PolicyConfig | Runtime policy/threshold/fee config | key, scope, value, version, status | AuditLog |
| RateLimitBucket | Abuse protection counter | subjectType, subjectKey, limitId, windowStart, count, expiresAt | UserIdentity, DeviceIdentity |
| PriceRecommendation | Suggested Ride price/Food delivery fee | service, amount, inputsSnapshot, policyVersion | RideRequest, FoodOrder |
| DriverPresence | Online/presence snapshot | driverId, location, serviceFlags, lastSeen | Redis primary ephemeral; snapshots in DB if needed |
| MatchingOffer | Offer sent to driver | requestId, driverId, wave, expiresAt, status | RideRequest/FoodOrder |
| RideRequest/RideTrip | Ride lifecycle | customerId, driverId, pickup, dropoff, price, status | PaymentProof, ChatRoom, Complaint |
| Brand | Restaurant brand | name, status, category | Outlet, CanonicalMenu |
| Outlet | Physical food outlet | brandId, location, regionId, status, overrides | FoodOrder, MenuOverride |
| MenuItem/Modifier | Canonical food menu | brandId, name, price, status, modifierGroups | OutletOverride |
| OutletMenuOverride | Outlet-specific menu differences | outletId, itemId, price/status/hours override | Outlet, MenuItem |
| FoodOrder | Food order lifecycle | customerId, driverId, outletId, itemsSnapshot, deliveryFee, status | PaymentProof, ChangeProposal, ChatRoom |
| FoodChangeProposal | Driver-proposed item/price/status change | orderId, driverId, changeSnapshot, customerDecision | FoodOrder |
| PaymentProof | Direct bank transfer/QR evidence | serviceType, serviceId, payerId, receiverDriverId, mediaId, status | MediaEvidence, AuditLog |
| PlatformFee | Driver platform usage fee/subscription | driverId, amount, coveragePeriod, proofMediaId, verificationStatus | DriverProfile |
| MediaEvidence | S3 media/evidence metadata | bucketKey, classification, owner, linkedCase, retentionClass | PaymentProof, Complaint, FraudCase |
| ChatRoom/ChatMessage | Active Ride/Food chat | roomId, participants, serviceRef, messageType, mediaId, expiresAt | RideTrip/FoodOrder |
| Complaint | Service issue intake | reporterId, serviceRef, status, category, evidence | FraudCase optional |
| FraudCase | Fraud investigation lifecycle | complaintId, subjectUserId, status, decision, liability | Complaint, AuditLog |
| AuditLog | Immutable event/action trail | actor, action, entityRef, before/after, metadata, timestamp | Cross-cutting |
| NotificationJob | Async notification work | target, channel, payload, status | BullMQ/DB if persisted |
| PushToken | Mobile push registration | userId, deviceId, platform, tokenHash, status, lastSeenAt | NotificationJob |
| ConsentRecord | User privacy consent | userId, consentType, version, status, acceptedAt, revokedAt | UserIdentity, AuditLog |
| AppVersionPolicy | Mobile release guard | app, platform, minVersion, latestVersion, forceUpdate, message | PolicyConfig |
| MapRouteCache | HERE route/geocode cache | originHash, destinationHash, mode, provider, result, expiresAt | RideRequest/FoodOrder optional |

## Rules

- PostgreSQL is system of record for orders/trips, fraud, evidence metadata, payment proof, audit and policies.
- Redis is not system of record for orders/trips, fraud, evidence, payment proof or audit.
- PostGIS owns polygon, region containment, distance/geofence and spatial queries.
- Complex PostGIS raw SQL must be isolated in repository/service layers for `region`, `matching` and `location`, not scattered in resolvers.
- S3 stores media/evidence; DB stores metadata, classification, links, status and audit.
- Food order/item/menu snapshots must preserve the values shown/accepted at order time.
- Payment proof image is evidence, not official bank confirmation.
- Payment proof statuses include `PENDING_UPLOAD`, `SUBMITTED`, `MONEY_RECEIVED`, `PAYMENT_DISPUTED`, `CANCELED`, `CASE_LINKED`.
- Chat retention P0 is 1 week unless attached/preserved for complaint/dispute policy.
- Device/fingerprint data should be minimized, hashed/pseudonymized where possible, and used for fraud/risk rather than general tracking.
- Consent records are required for background location, device/risk collection, phone visibility and sensitive evidence processing.
