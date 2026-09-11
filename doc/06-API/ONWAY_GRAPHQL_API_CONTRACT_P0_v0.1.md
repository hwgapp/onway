# ONWAY - GraphQL API Contract P0

**Loai tai lieu:** API Contract / Technical PRD input  
**Phien ban:** 0.1  
**Trang thai:** Draft  
**Ngay cap nhat:** 11/09/2026  
**Stack:** NestJS GraphQL code-first, generated `schema.gql` for clients  
**Pham vi:** P0 API cho Customer App, Driver App, Admin Portal  

---

# 1. Muc tieu

Tai lieu nay dinh nghia GraphQL API contract P0 de Claude/dev implement resolvers, DTOs, guards va service methods.

Nguon uu tien:

1. `doc/02-PRD/ONWAY_PRD_MASTER_v0.1_VI.md`
2. `doc/05-Logic/ONWAY_LOGIC_P0_v0.1.md`
3. `doc/04-Database/ONWAY_DB_SCHEMA_P0_v0.1.md`
4. `doc/01-BRD/ONWAY_BRD_v0.5_VI.md`
5. `doc/03-Architecture/ONWAY_ARCHITECTURE_DECISIONS_v0.2_VI.md`

# 2. Contract principles

- Backend uses NestJS GraphQL code-first.
- This document is the product/API contract; generated `schema.gql` from code must match it.
- GraphQL is for business data and command mutations.
- High-frequency realtime, location, matching offers, tracking and chat delivery use WebSocket contract in Realtime doc.
- Clients must not implement business authorization locally. API returns `allowedActions`.
- Every critical mutation must be idempotent or naturally safe under retry.
- All business money is `Money { amountMinor, currencyCode }`.
- Ride/Food payment is direct bank transfer/QR only. No COD, no cash, no gateway, no wallet.

# 3. Authentication flow

Auth follows Architecture ADR-030:

1. App calls public OTP REST/GraphQL mutation to request OTP via backend.
2. Backend sends OTP through ViHAT.
3. App submits OTP.
4. Backend verifies OTP and mints Firebase custom token.
5. App signs in Firebase with custom token.
6. App calls GraphQL with Firebase ID token in `Authorization: Bearer <id_token>`.
7. Backend verifies Firebase ID token and maps to internal `Account`.

Admin accounts must already exist or be provisioned by secure admin seed/manual process. Public signup must not create admin profiles.

# 4. Common types

## 4.1 Scalars

```graphql
scalar DateTime
scalar Date
scalar Time
scalar JSON
scalar Upload
```

## 4.2 Core value types

```graphql
type Money {
  amountMinor: BigInt!
  currencyCode: String!
  formatted: String
}

type GeoPoint {
  lat: Float!
  lng: Float!
}

input GeoPointInput {
  lat: Float!
  lng: Float!
}

type AddressSnapshot {
  text: String!
  location: GeoPoint!
  providerPlaceId: String
}

input AddressInput {
  text: String!
  location: GeoPointInput!
  providerPlaceId: String
}

type PageInfo {
  hasNextPage: Boolean!
  endCursor: String
}

input PaginationInput {
  first: Int = 20
  after: String
}
```

Implementation note: GraphQL `BigInt` may be custom scalar or string-backed. If tooling is easier, use `String` for `amountMinor` in generated schema and map to bigint server-side.

## 4.3 Error payload

Use GraphQL errors for unexpected/system errors. For command validation, return typed payload:

```graphql
type UserError {
  code: ErrorCode!
  field: String
  message: String!
  metadata: JSON
}

enum ErrorCode {
  UNAUTHENTICATED
  FORBIDDEN
  INVALID_STATE
  POLICY_BLOCKED
  REGION_UNAVAILABLE
  DRIVER_NOT_ELIGIBLE
  PAYMENT_PROOF_REQUIRED
  PAYMENT_UNDER_REVIEW
  OFFER_EXPIRED
  ALREADY_ASSIGNED
  CATALOG_UNAVAILABLE
  VALIDATION_ERROR
  RATE_LIMITED
  NOT_FOUND
}

interface MutationPayload {
  ok: Boolean!
  errors: [UserError!]!
}
```

## 4.4 Actor and actions

```graphql
enum ActorRole {
  CUSTOMER
  DRIVER
  ADMIN
}

type AllowedAction {
  code: String!
  enabled: Boolean!
  disabledReason: String
}
```

# 5. Enums

```graphql
enum ServiceType { RIDE FOOD }
enum VehicleType { MOTORCYCLE CAR }
enum RegionStatus { PLANNED PILOT ACTIVE PAUSED CLOSED }
enum AvailabilityStatus { AVAILABLE UNAVAILABLE CLOSED_NOW BUSY }

enum AccountStatus {
  ACTIVE
  PENDING_VERIFICATION
  UNDER_REVIEW
  LOCKED
  SUSPENDED
  BLOCKED
  DELETED_REQUESTED
}

enum DriverRiskStatus {
  CLEAR
  UNDER_REVIEW
  TEMPORARILY_LOCKED
  SUSPENDED
  BLOCKED
}

enum DriverActivationStatus {
  INACTIVE
  PENDING_REVIEW
  PENDING_PLATFORM_FEE
  ACTIVE
  DEACTIVATED
}

enum MatchingSessionStatus {
  QUEUED
  BATCH_OFFERED
  ASSIGNED
  NO_DRIVER_AVAILABLE
  EXPIRED
  CANCELLED
}

enum MatchingOfferStatus {
  SENT
  ACCEPTED
  REJECTED
  EXPIRED
  CANCELLED_ASSIGNMENT_TAKEN
  CANCELLED_BY_CUSTOMER
}

enum DirectPaymentStatus {
  AWAITING_CUSTOMER_TRANSFER
  PROOF_SUBMITTED
  DRIVER_CONFIRMED_RECEIVED
  DRIVER_REPORTED_NOT_RECEIVED
  ADMIN_REVIEW_REQUIRED
  CONFIRMED_BY_ADMIN
  REJECTED_BY_ADMIN
  DISPUTED
}

enum ChatMessageType { TEXT IMAGE }

enum ComplaintStatus {
  SUBMITTED
  NEEDS_MORE_EVIDENCE
  OPEN_UNDER_REVIEW
  DRIVER_RESPONSE_REQUESTED
  CUSTOMER_RESPONSE_REQUESTED
  RESOLVED
  REJECTED_INVALID
  ESCALATED_FRAUD_REVIEW
  CLOSED
}
```

# 6. Identity and auth API

## 6.1 Types

```graphql
type Account {
  id: ID!
  phoneE164: String!
  displayName: String
  avatarUrl: String
  status: AccountStatus!
  roles: [ActorRole!]!
  customerProfile: CustomerProfile
  driverProfile: DriverProfile
  adminProfile: AdminProfile
  allowedActions: [AllowedAction!]!
}

type CustomerProfile {
  id: ID!
  status: AccountStatus!
  defaultRegion: Region
  createdAt: DateTime!
}

type AdminProfile {
  id: ID!
  status: String!
  roles: [AdminRole!]!
}

type AdminRole {
  code: String!
  name: String!
  permissions: [String!]!
}

type OtpChallengePayload implements MutationPayload {
  ok: Boolean!
  errors: [UserError!]!
  challengeId: ID
  expiresAt: DateTime
}

type VerifyOtpPayload implements MutationPayload {
  ok: Boolean!
  errors: [UserError!]!
  firebaseCustomToken: String
  account: Account
}
```

## 6.2 Inputs

```graphql
input RequestOtpInput {
  phoneE164: String!
  purpose: OtpPurpose!
}

enum OtpPurpose {
  CUSTOMER_LOGIN
  DRIVER_LOGIN
}

input VerifyOtpInput {
  challengeId: ID!
  otpCode: String!
  intendedRole: ActorRole!
}

input UpdateAccountDisplayNameInput {
  displayName: String!
}
```

## 6.3 Queries and mutations

```graphql
type Query {
  me: Account!
  myCustomerProfile: CustomerProfile
  myDriverProfile: DriverProfile
  myAllowedActions: [AllowedAction!]!
}

type Mutation {
  requestOtp(input: RequestOtpInput!): OtpChallengePayload!
  verifyOtp(input: VerifyOtpInput!): VerifyOtpPayload!
  createCustomerProfile: CustomerProfilePayload!
  createDriverProfile: DriverProfilePayload!
  updateAccountDisplayName(input: UpdateAccountDisplayNameInput!): AccountPayload!
}
```

Rules:

- `requestOtp` and `verifyOtp` are unauthenticated but rate-limited.
- `createDriverProfile` never activates driver.
- Admin profile creation is not public API.

# 7. Region, config, media

## 7.1 Region types

```graphql
type Region {
  id: ID!
  name: String!
  slug: String!
  status: RegionStatus!
  currencyCode: String!
  timezone: String!
  enabledServices: [ServiceType!]!
  enabledVehicles(serviceType: ServiceType): [VehicleType!]!
}

type RegionResolution {
  region: Region
  serviceAvailable: Boolean!
  vehicleAvailable: Boolean
  unavailableReason: String
}

input ResolveRegionInput {
  location: GeoPointInput!
  serviceType: ServiceType
  vehicleType: VehicleType
}
```

## 7.2 Media types

```graphql
enum MediaPurpose {
  PAYMENT_PROOF
  CHAT_IMAGE
  DRIVER_DOCUMENT
  CATALOG_IMAGE
  COMPLAINT_EVIDENCE
  PLATFORM_FEE_PROOF
}

type MediaObject {
  id: ID!
  purpose: MediaPurpose!
  mimeType: String!
  sizeBytes: BigInt!
  url: String
  status: String!
  createdAt: DateTime!
}

input CreateMediaUploadIntentInput {
  purpose: MediaPurpose!
  mimeType: String!
  sizeBytes: BigInt!
  linkedEntityType: String
  linkedEntityId: ID
}

type MediaUploadIntentPayload implements MutationPayload {
  ok: Boolean!
  errors: [UserError!]!
  mediaId: ID
  uploadUrl: String
  uploadHeaders: JSON
}

input CompleteMediaUploadInput {
  mediaId: ID!
  checksumSha256: String
  metadata: JSON
}
```

## 7.3 API

```graphql
extend type Query {
  resolveRegionByCoordinate(input: ResolveRegionInput!): RegionResolution!
  availableServices(location: GeoPointInput!): [RegionServiceAvailability!]!
}

type RegionServiceAvailability {
  serviceType: ServiceType!
  available: Boolean!
  enabledVehicles: [VehicleType!]!
  reason: String
}

extend type Mutation {
  createMediaUploadIntent(input: CreateMediaUploadIntentInput!): MediaUploadIntentPayload!
  completeMediaUpload(input: CompleteMediaUploadInput!): MediaObjectPayload!
}
```

# 8. Driver API

## 8.1 Types

```graphql
type DriverProfile {
  id: ID!
  account: Account!
  onboardingStatus: String!
  riskStatus: DriverRiskStatus!
  activationStatus: DriverActivationStatus!
  activatedAt: DateTime
  vehicles: [DriverVehicle!]!
  paymentAccounts: [DriverPaymentAccount!]!
  serviceEligibilities: [DriverServiceEligibility!]!
  allowedActions: [AllowedAction!]!
}

type DriverVehicle {
  id: ID!
  vehicleType: VehicleType!
  displayName: String
  plateNumberMasked: String
  color: String
  status: String!
}

type DriverPaymentAccount {
  id: ID!
  bankName: String!
  bankCode: String
  accountNumberMasked: String!
  accountHolderName: String!
  qrUrl: String
  status: String!
  isDefault: Boolean!
}

type DriverServiceEligibility {
  id: ID!
  region: Region!
  serviceType: ServiceType!
  vehicle: DriverVehicle!
  status: String!
}

type DriverProfilePayload implements MutationPayload {
  ok: Boolean!
  errors: [UserError!]!
  driverProfile: DriverProfile
}

type DriverVehiclePayload implements MutationPayload {
  ok: Boolean!
  errors: [UserError!]!
  vehicle: DriverVehicle
}
```

## 8.2 Inputs

```graphql
input DriverSubmitProfileInput {
  fullName: String!
  email: String
  homeCityId: ID
}

input DriverSubmitVehicleInput {
  vehicleType: VehicleType!
  displayName: String
  plateNumber: String
  color: String
}

input DriverSubmitPaymentAccountInput {
  bankName: String!
  bankCode: String
  accountNumber: String!
  accountHolderName: String!
  qrMediaId: ID
  isDefault: Boolean = true
}

input DriverGoOnlineInput {
  vehicleId: ID!
  serviceTypes: [ServiceType!]!
  location: GeoPointInput!
}
```

## 8.3 Queries/mutations

```graphql
extend type Query {
  driverOnboardingStatus: DriverProfile!
  driverEligibility: DriverProfile!
  driverVehicles: [DriverVehicle!]!
  driverPaymentAccounts: [DriverPaymentAccount!]!
}

extend type Mutation {
  driverSubmitProfile(input: DriverSubmitProfileInput!): DriverProfilePayload!
  driverSubmitVehicle(input: DriverSubmitVehicleInput!): DriverVehiclePayload!
  driverSubmitPaymentAccount(input: DriverSubmitPaymentAccountInput!): DriverPaymentAccountPayload!
  driverGoOnline(input: DriverGoOnlineInput!): DriverPresencePayload!
  driverGoOffline: DriverPresencePayload!
}
```

Rules:

- `driverGoOnline` requires active driver, active vehicle, service eligibility, active payment account, region availability and clear risk status.
- Location streaming after `driverGoOnline` is WebSocket, not GraphQL.

# 9. Platform fee API

```graphql
type PlatformFeeInstruction {
  amount: Money!
  transferReference: String!
  bankName: String!
  bankCode: String
  accountNumberMasked: String!
  accountHolderName: String!
  qrUrl: String
}

type PlatformFeePayment {
  id: ID!
  amount: Money!
  status: String!
  proof: MediaObject!
  referenceText: String
  reviewedAt: DateTime
  reviewReason: String
  createdAt: DateTime!
}

input SubmitPlatformFeeProofInput {
  proofMediaId: ID!
  referenceText: String
}

extend type Query {
  driverPlatformFeeInstruction: PlatformFeeInstruction!
  driverPlatformFeeStatus: [PlatformFeePayment!]!
}

extend type Mutation {
  driverSubmitPlatformFeeProof(input: SubmitPlatformFeeProofInput!): PlatformFeePaymentPayload!
}
```

Admin review mutations are in Admin section.

# 10. Food catalog API

## 10.1 Customer catalog types

```graphql
type FoodOutletCard {
  id: ID!
  brandName: String!
  outletName: String!
  addressText: String!
  location: GeoPoint!
  availabilityStatus: AvailabilityStatus!
  imageUrl: String
  estimatedDistanceMeters: Int
  estimatedDurationSeconds: Int
}

type FoodMenu {
  outlet: FoodOutletCard!
  categories: [FoodMenuCategory!]!
}

type FoodMenuCategory {
  id: ID!
  name: String!
  sortOrder: Int!
  items: [FoodMenuItem!]!
}

type FoodMenuItem {
  id: ID!
  name: String!
  description: String
  price: Money!
  imageUrl: String
  availabilityStatus: AvailabilityStatus!
  modifierGroups: [FoodModifierGroup!]!
}

type FoodModifierGroup {
  id: ID!
  name: String!
  isRequired: Boolean!
  minSelect: Int!
  maxSelect: Int!
  options: [FoodModifierOption!]!
}

type FoodModifierOption {
  id: ID!
  name: String!
  priceDelta: Money!
  availabilityStatus: AvailabilityStatus!
}
```

## 10.2 Customer catalog queries

```graphql
input FoodDiscoveryInput {
  location: GeoPointInput!
  search: String
  pagination: PaginationInput
}

extend type Query {
  foodDiscovery(input: FoodDiscoveryInput!): FoodOutletConnection!
  foodOutletMenu(outletId: ID!, deliveryLocation: GeoPointInput): FoodMenu!
}
```

Rules:

- Only published, active, region-valid catalog is returned.
- Effective menu applies outlet item/modifier overrides.
- Unavailable items/options are returned as disabled or filtered according to UI policy.

## 10.3 Admin catalog API

```graphql
type AdminRestaurantBrand {
  id: ID!
  name: String!
  slug: String!
  status: String!
  categoryTags: [String!]!
  createdAt: DateTime!
  updatedAt: DateTime!
}

type AdminRestaurantOutlet {
  id: ID!
  brand: AdminRestaurantBrand!
  region: Region!
  name: String!
  slug: String!
  addressText: String!
  location: GeoPoint!
  status: String!
  availabilityStatus: AvailabilityStatus!
}

input AdminCreateBrandInput {
  name: String!
  slug: String!
  categoryTags: [String!]
}

input AdminCreateOutletInput {
  brandId: ID!
  regionId: ID!
  name: String!
  slug: String!
  addressText: String!
  location: GeoPointInput!
  phone: String
}

input AdminUpsertMenuItemInput {
  menuVersionId: ID!
  categoryId: ID!
  itemId: ID
  name: String!
  description: String
  basePrice: MoneyInput!
  imageMediaId: ID
  status: String!
  sortOrder: Int = 0
}

input MoneyInput {
  amountMinor: BigInt!
  currencyCode: String!
}

extend type Query {
  adminBrands(pagination: PaginationInput, search: String): AdminBrandConnection!
  adminOutlets(brandId: ID, regionId: ID, pagination: PaginationInput): AdminOutletConnection!
  adminMenuVersion(menuVersionId: ID!): AdminMenuVersion!
}

extend type Mutation {
  adminCreateBrand(input: AdminCreateBrandInput!): AdminBrandPayload!
  adminUpdateBrand(id: ID!, input: AdminUpdateBrandInput!): AdminBrandPayload!
  adminCreateOutlet(input: AdminCreateOutletInput!): AdminOutletPayload!
  adminUpdateOutlet(id: ID!, input: AdminUpdateOutletInput!): AdminOutletPayload!
  adminCreateMenu(brandId: ID!, name: String!): AdminMenuPayload!
  adminCreateMenuVersion(menuId: ID!): AdminMenuVersionPayload!
  adminUpsertMenuCategory(input: AdminUpsertMenuCategoryInput!): AdminMenuCategoryPayload!
  adminUpsertMenuItem(input: AdminUpsertMenuItemInput!): AdminMenuItemPayload!
  adminUpsertModifierGroup(input: AdminUpsertModifierGroupInput!): AdminModifierGroupPayload!
  adminUpsertModifierOption(input: AdminUpsertModifierOptionInput!): AdminModifierOptionPayload!
  adminSetOutletItemOverride(input: AdminSetOutletItemOverrideInput!): AdminOutletOverridePayload!
  adminSetOutletModifierOptionOverride(input: AdminSetOutletModifierOptionOverrideInput!): AdminOutletOverridePayload!
  adminSubmitCatalogReview(entityType: String!, entityId: ID!, reason: String): CatalogPublishPayload!
  adminPublishCatalog(entityType: String!, entityId: ID!, reason: String!): CatalogPublishPayload!
  adminUnpublishCatalog(entityType: String!, entityId: ID!, reason: String!): CatalogPublishPayload!
}
```

# 11. Ride API

## 11.1 Types

```graphql
enum RideStatus {
  DRAFT
  PRICED
  MATCHING
  ASSIGNED
  DRIVER_EN_ROUTE_TO_PICKUP
  DRIVER_ARRIVED
  AWAITING_PAYMENT_IF_REQUIRED
  READY_TO_START
  IN_PROGRESS
  ARRIVED_AT_DESTINATION
  COMPLETED
  CANCELLED
  EXPIRED_NO_DRIVER
  DISPUTED
}

type Ride {
  id: ID!
  status: RideStatus!
  customer: CustomerProfile!
  driver: DriverProfile
  vehicleType: VehicleType!
  region: Region!
  pickup: AddressSnapshot!
  dropoff: AddressSnapshot!
  estimatedDistanceMeters: Int
  estimatedDurationSeconds: Int
  recommendedPrice: Money!
  finalPrice: Money!
  paymentRecord: DirectPaymentRecord
  chatRoom: ChatRoom
  allowedActions: [AllowedAction!]!
  requestedAt: DateTime!
  assignedAt: DateTime
  startedAt: DateTime
  completedAt: DateTime
}

type RideQuote {
  pickup: AddressSnapshot!
  dropoff: AddressSnapshot!
  vehicleType: VehicleType!
  region: Region!
  estimatedDistanceMeters: Int
  estimatedDurationSeconds: Int
  recommendedPrice: Money!
  expiresAt: DateTime!
}
```

## 11.2 Inputs

```graphql
input RideQuoteInput {
  pickup: AddressInput!
  dropoff: AddressInput!
  vehicleType: VehicleType!
}

input ConfirmRideRequestInput {
  pickup: AddressInput!
  dropoff: AddressInput!
  vehicleType: VehicleType!
  quoteToken: String
  idempotencyKey: String!
}

input CancelRideInput {
  rideId: ID!
  reason: String!
  idempotencyKey: String!
}
```

## 11.3 Queries/mutations

```graphql
extend type Query {
  rideQuote(input: RideQuoteInput!): RideQuote!
  myActiveRide: Ride
  rideDetail(id: ID!): Ride!
}

extend type Mutation {
  customerConfirmRideRequest(input: ConfirmRideRequestInput!): RidePayload!
  customerCancelRide(input: CancelRideInput!): RidePayload!
  driverMarkRideArrived(rideId: ID!, idempotencyKey: String!): RidePayload!
  driverStartRide(rideId: ID!, idempotencyKey: String!): RidePayload!
  driverCompleteRide(rideId: ID!, idempotencyKey: String!): RidePayload!
}
```

Offer accept/reject are under Matching API because they are shared by Ride/Food.

Rules:

- Ride price negotiation is not default P0.
- Ride payment timing remains policy/open decision; API supports payment record at required step.

# 12. Food order API

## 12.1 Types

```graphql
enum FoodOrderStatus {
  CART
  QUOTED
  CUSTOMER_CONFIRMED
  MATCHING
  ASSIGNED
  AWAITING_CUSTOMER_TRANSFER
  PAYMENT_PROOF_SUBMITTED
  DRIVER_CONFIRMED_PAYMENT
  DRIVER_EN_ROUTE_TO_OUTLET
  DRIVER_ARRIVED_AT_OUTLET
  ORDERING_WITH_RESTAURANT
  RESTAURANT_ORDER_PLACED
  WAITING_FOR_FOOD
  RESTAURANT_PAID
  READY_FOR_DELIVERY
  DRIVER_EN_ROUTE_TO_CUSTOMER
  DRIVER_ARRIVED_AT_CUSTOMER
  DELIVERED
  COMPLETED
  CANCELLED
  DELIVERY_FAILED
  DISPUTED
}

type FoodOrder {
  id: ID!
  status: FoodOrderStatus!
  customer: CustomerProfile!
  driver: DriverProfile
  outlet: FoodOutletCard!
  region: Region!
  deliveryAddress: AddressSnapshot!
  items: [FoodOrderItem!]!
  itemTotal: Money!
  deliveryFee: Money!
  estimatedTotal: Money!
  paymentRecord: DirectPaymentRecord
  chatRoom: ChatRoom
  allowedActions: [AllowedAction!]!
  customerConfirmedAt: DateTime
  assignedAt: DateTime
  paymentProofSubmittedAt: DateTime
  restaurantOrderPlacedAt: DateTime
  completedAt: DateTime
}

type FoodOrderItem {
  id: ID!
  itemName: String!
  quantity: Int!
  unitPrice: Money!
  totalPrice: Money!
  modifiers: [FoodOrderItemModifier!]!
  status: String!
}

type FoodOrderItemModifier {
  id: ID!
  modifierGroupName: String!
  modifierOptionName: String!
  priceDelta: Money!
}

type FoodQuote {
  outlet: FoodOutletCard!
  deliveryAddress: AddressSnapshot!
  items: [FoodOrderItemPreview!]!
  itemTotal: Money!
  deliveryFee: Money!
  estimatedTotal: Money!
  estimatedDistanceMeters: Int
  estimatedDurationSeconds: Int
  expiresAt: DateTime!
}
```

## 12.2 Inputs

```graphql
input FoodCartItemInput {
  menuItemId: ID!
  quantity: Int!
  modifierOptionIds: [ID!]!
}

input FoodQuoteInput {
  outletId: ID!
  deliveryAddress: AddressInput!
  items: [FoodCartItemInput!]!
}

input ConfirmFoodOrderInput {
  outletId: ID!
  deliveryAddress: AddressInput!
  items: [FoodCartItemInput!]!
  quoteToken: String
  idempotencyKey: String!
}

input CancelFoodOrderInput {
  foodOrderId: ID!
  reason: String!
  idempotencyKey: String!
}
```

## 12.3 Queries/mutations

```graphql
extend type Query {
  foodQuote(input: FoodQuoteInput!): FoodQuote!
  myActiveFoodOrder: FoodOrder
  foodOrderDetail(id: ID!): FoodOrder!
}

extend type Mutation {
  customerConfirmFoodOrder(input: ConfirmFoodOrderInput!): FoodOrderPayload!
  customerCancelFoodOrder(input: CancelFoodOrderInput!): FoodOrderPayload!
  driverStartToOutlet(foodOrderId: ID!, idempotencyKey: String!): FoodOrderPayload!
  driverMarkArrivedAtOutlet(foodOrderId: ID!, idempotencyKey: String!): FoodOrderPayload!
  driverMarkRestaurantOrderPlaced(foodOrderId: ID!, idempotencyKey: String!): FoodOrderPayload!
  driverMarkRestaurantPaid(foodOrderId: ID!, idempotencyKey: String!): FoodOrderPayload!
  driverMarkFoodReadyForDelivery(foodOrderId: ID!, idempotencyKey: String!): FoodOrderPayload!
  driverMarkArrivedAtCustomer(foodOrderId: ID!, idempotencyKey: String!): FoodOrderPayload!
  driverMarkFoodDelivered(foodOrderId: ID!, idempotencyKey: String!): FoodOrderPayload!
  driverCompleteFoodOrder(foodOrderId: ID!, idempotencyKey: String!): FoodOrderPayload!
}
```

Rules:

- No Food delivery fee negotiation.
- Driver cannot start restaurant purchase before required direct payment proof/confirmation state.
- `restaurantOrderPlacedAt` changes cancellation responsibility.

# 13. Matching API

```graphql
type MatchingOffer {
  id: ID!
  serviceType: ServiceType!
  status: MatchingOfferStatus!
  ride: Ride
  foodOrder: FoodOrder
  offeredPrice: Money!
  expiresAt: DateTime!
  allowedActions: [AllowedAction!]!
}

type DriverActiveOffer {
  offer: MatchingOffer!
  receivedAt: DateTime!
}

input DriverRespondOfferInput {
  offerId: ID!
  response: DriverOfferResponse!
  reason: String
  idempotencyKey: String!
}

enum DriverOfferResponse {
  ACCEPT
  REJECT
}

extend type Query {
  driverActiveOffer: DriverActiveOffer
}

extend type Mutation {
  driverRespondToOffer(input: DriverRespondOfferInput!): DriverOfferResponsePayload!
}
```

Rules:

- `driverRespondToOffer(ACCEPT)` runs atomic assignment transaction.
- Reject records response and may allow next batch.
- Expired offer returns `OFFER_EXPIRED`.
- Already assigned session returns `ALREADY_ASSIGNED`.

# 14. Direct payment API

```graphql
type DirectPaymentRecord {
  id: ID!
  serviceType: ServiceType!
  entityId: ID!
  status: DirectPaymentStatus!
  amount: Money!
  method: String!
  requiredBeforeEvent: String!
  instructions: DirectPaymentInstructions!
  proofs: [PaymentProof!]!
  confirmations: [PaymentConfirmation!]!
  allowedActions: [AllowedAction!]!
}

type DirectPaymentInstructions {
  bankName: String!
  bankCode: String
  accountNumberMasked: String!
  accountHolderName: String!
  qrUrl: String
  transferReference: String!
}

type PaymentProof {
  id: ID!
  media: MediaObject!
  referenceText: String
  amountClaimed: Money
  status: String!
  createdAt: DateTime!
}

type PaymentConfirmation {
  id: ID!
  actorRole: ActorRole!
  confirmationType: String!
  note: String
  createdAt: DateTime!
}

input SubmitPaymentProofInput {
  paymentRecordId: ID!
  proofMediaId: ID!
  referenceText: String
  amountClaimed: MoneyInput
  idempotencyKey: String!
}

input ConfirmPaymentReceivedInput {
  paymentRecordId: ID!
  idempotencyKey: String!
}

input ReportPaymentNotReceivedInput {
  paymentRecordId: ID!
  note: String!
  idempotencyKey: String!
}

extend type Query {
  paymentRecord(id: ID!): DirectPaymentRecord!
}

extend type Mutation {
  submitPaymentProof(input: SubmitPaymentProofInput!): DirectPaymentRecordPayload!
  driverConfirmPaymentReceived(input: ConfirmPaymentReceivedInput!): DirectPaymentRecordPayload!
  driverReportPaymentNotReceived(input: ReportPaymentNotReceivedInput!): DirectPaymentRecordPayload!
}
```

Rules:

- Customer can submit payment proof only for own ride/order.
- Driver can view/confirm only assigned ride/order payment.
- Proof image is required.
- Proof replacement before driver confirmation may be allowed by policy; old proof remains auditable.

# 15. Chat API

Chat delivery is realtime, but history/query and upload use GraphQL.

```graphql
type ChatRoom {
  id: ID!
  serviceType: ServiceType!
  entityId: ID!
  status: String!
  participants: [ChatParticipant!]!
  retentionDeleteAfter: DateTime!
  allowedActions: [AllowedAction!]!
}

type ChatParticipant {
  accountId: ID!
  role: ActorRole!
}

type ChatMessage {
  id: ID!
  roomId: ID!
  sender: Account!
  messageType: ChatMessageType!
  bodyText: String
  attachments: [MediaObject!]!
  status: String!
  sentAt: DateTime!
}

input SendChatMessageInput {
  roomId: ID!
  messageType: ChatMessageType!
  bodyText: String
  mediaIds: [ID!]
  clientMessageId: String!
}

extend type Query {
  chatRoom(id: ID!): ChatRoom!
  chatMessages(roomId: ID!, pagination: PaginationInput): ChatMessageConnection!
}

extend type Mutation {
  sendChatMessage(input: SendChatMessageInput!): ChatMessagePayload!
}
```

Rules:

- Room exists only after assignment.
- Only participants/admin with case permission can read.
- Chat text/image retention is 1 week unless evidence is preserved for complaint.

# 16. Food change request API

```graphql
enum FoodChangeReasonType {
  PRICE_CHANGE
  ITEM_UNAVAILABLE
  MODIFIER_UNAVAILABLE
  SUBSTITUTION
  OTHER
}

enum FoodChangeRequestStatus {
  PROPOSED
  AWAITING_CUSTOMER_DECISION
  ACCEPTED
  REJECTED
  EXPIRED
  ADMIN_REVIEW_REQUIRED
}

type FoodChangeRequest {
  id: ID!
  foodOrder: FoodOrder!
  status: FoodChangeRequestStatus!
  reasonType: FoodChangeReasonType!
  note: String
  evidence: MediaObject
  items: [FoodChangeRequestItem!]!
  createdAt: DateTime!
}

input DriverProposeFoodChangeInput {
  foodOrderId: ID!
  reasonType: FoodChangeReasonType!
  note: String
  evidenceMediaId: ID
  items: [FoodChangeRequestItemInput!]!
  idempotencyKey: String!
}

input FoodChangeRequestItemInput {
  foodOrderItemId: ID!
  changeType: String!
  newValue: JSON
  priceDelta: MoneyInput
}

extend type Mutation {
  driverProposeFoodChange(input: DriverProposeFoodChangeInput!): FoodChangeRequestPayload!
  customerAcceptFoodChange(changeRequestId: ID!, idempotencyKey: String!): FoodChangeRequestPayload!
  customerRejectFoodChange(changeRequestId: ID!, reason: String, idempotencyKey: String!): FoodChangeRequestPayload!
}
```

Rules:

- Driver cannot buy affected changed item before customer accepts.
- Change request does not update catalog automatically.

# 17. Complaint, risk and fraud API

```graphql
enum ComplaintCategory {
  PAID_BUT_DRIVER_NO_SHOW
  DRIVER_SAYS_PAYMENT_NOT_RECEIVED
  FOOD_ITEM_PRICE_ISSUE
  DRIVER_CANCELLED_AFTER_PAYMENT
  CUSTOMER_NO_SHOW
  DRIVER_BEHAVIOR_SERVICE
  CUSTOMER_BEHAVIOR_SERVICE
  SAFETY_CONCERN
  OTHER
}

enum ComplaintSeverity { LOW MEDIUM HIGH CRITICAL }

type Complaint {
  id: ID!
  submittedBy: Account!
  againstAccount: Account
  serviceType: ServiceType
  entityId: ID
  category: ComplaintCategory!
  severity: ComplaintSeverity!
  status: ComplaintStatus!
  description: String!
  qualifiesForDriverAutoLock: Boolean!
  evidence: [ComplaintEvidence!]!
  responses: [ComplaintResponse!]!
  createdAt: DateTime!
  updatedAt: DateTime!
}

type ComplaintEvidence {
  id: ID!
  sourceType: String!
  media: MediaObject
  sourceEntityType: String
  sourceEntityId: ID
  createdAt: DateTime!
}

input SubmitComplaintInput {
  serviceType: ServiceType
  entityId: ID
  againstAccountId: ID
  category: ComplaintCategory!
  description: String!
  evidenceMediaIds: [ID!]
  sourcePaymentProofIds: [ID!]
  sourceChatMessageIds: [ID!]
  idempotencyKey: String!
}

extend type Query {
  myComplaints(pagination: PaginationInput): ComplaintConnection!
  complaintDetail(id: ID!): Complaint!
}

extend type Mutation {
  submitComplaint(input: SubmitComplaintInput!): ComplaintPayload!
  driverRespondToComplaint(input: ComplaintResponseInput!): ComplaintPayload!
}
```

Admin:

```graphql
extend type Query {
  adminComplaintQueue(filter: AdminComplaintFilterInput, pagination: PaginationInput): ComplaintConnection!
  adminComplaintDetail(id: ID!): Complaint!
  adminDriverDetail(id: ID!): AdminDriverDetail!
}

extend type Mutation {
  adminResolveComplaint(id: ID!, reason: String!, idempotencyKey: String!): ComplaintPayload!
  adminRejectComplaint(id: ID!, reason: String!, idempotencyKey: String!): ComplaintPayload!
  adminRequestComplaintEvidence(id: ID!, message: String!, idempotencyKey: String!): ComplaintPayload!
  adminEscalateComplaintToFraud(id: ID!, reason: String!, idempotencyKey: String!): FraudCasePayload!
  adminLockDriver(driverProfileId: ID!, reason: String!, idempotencyKey: String!): DriverProfilePayload!
  adminUnlockDriver(driverProfileId: ID!, reason: String!, idempotencyKey: String!): DriverProfilePayload!
}
```

Rules:

- Paid-but-driver-no-show complaint requires linked payment proof.
- 2 qualifying open complaints auto-lock driver by policy.
- Auto-lock does not confirm fraud.
- Admin unlock does not delete complaint/fraud history.

# 18. Rating API

```graphql
type Rating {
  id: ID!
  serviceType: ServiceType!
  entityId: ID!
  score: Int!
  tags: [String!]!
  comment: String
  createdAt: DateTime!
}

input SubmitRatingInput {
  serviceType: ServiceType!
  entityId: ID!
  ratedAccountId: ID!
  score: Int!
  tags: [String!]
  comment: String
  idempotencyKey: String!
}

extend type Mutation {
  submitRating(input: SubmitRatingInput!): RatingPayload!
}
```

Rules:

- Rater must be participant of completed Ride/Food.
- One rating per rater/rated/entity.
- Rating does not update Trust in P0.

# 19. Admin operations API

Admin APIs require RBAC permission and audit reason for critical mutations.

```graphql
extend type Query {
  adminRides(filter: AdminRideFilterInput, pagination: PaginationInput): RideConnection!
  adminRideDetail(id: ID!): Ride!
  adminFoodOrders(filter: AdminFoodOrderFilterInput, pagination: PaginationInput): FoodOrderConnection!
  adminFoodOrderDetail(id: ID!): FoodOrder!
  adminAuditLogs(targetType: String, targetId: ID, pagination: PaginationInput): AuditLogConnection!
  adminPolicyConfigs(filter: AdminPolicyConfigFilterInput): [PolicyConfig!]!
}

extend type Mutation {
  adminCreateRegion(input: AdminCreateRegionInput!): RegionPayload!
  adminUpdateRegionPolygon(id: ID!, boundaryGeoJson: JSON!, reason: String!): RegionPayload!
  adminSetRegionServiceAvailability(input: AdminSetRegionServiceAvailabilityInput!): RegionPayload!
  adminSetPolicyConfig(input: AdminSetPolicyConfigInput!): PolicyConfigPayload!
  adminApprovePlatformFeeProof(paymentId: ID!, reason: String!, idempotencyKey: String!): PlatformFeePaymentPayload!
  adminRejectPlatformFeeProof(paymentId: ID!, reason: String!, idempotencyKey: String!): PlatformFeePaymentPayload!
}
```

# 20. Payload pattern

Each mutation payload should follow:

```graphql
type RidePayload implements MutationPayload {
  ok: Boolean!
  errors: [UserError!]!
  ride: Ride
}
```

Create similar payloads for:

- `AccountPayload`
- `CustomerProfilePayload`
- `DriverProfilePayload`
- `DriverVehiclePayload`
- `DriverPaymentAccountPayload`
- `DriverPresencePayload`
- `PlatformFeePaymentPayload`
- `AdminBrandPayload`
- `AdminOutletPayload`
- `AdminMenuPayload`
- `AdminMenuVersionPayload`
- `AdminMenuCategoryPayload`
- `AdminMenuItemPayload`
- `AdminModifierGroupPayload`
- `AdminModifierOptionPayload`
- `CatalogPublishPayload`
- `FoodOrderPayload`
- `DriverOfferResponsePayload`
- `DirectPaymentRecordPayload`
- `MediaObjectPayload`
- `ChatMessagePayload`
- `FoodChangeRequestPayload`
- `ComplaintPayload`
- `FraudCasePayload`
- `RatingPayload`
- `PolicyConfigPayload`
- `RegionPayload`

# 21. Authorization matrix

| API group | Customer | Driver | Admin |
|---|---:|---:|---:|
| `me` | yes | yes | yes |
| Customer Ride/Food create | yes | no | no |
| Driver onboarding | no | yes own | admin review |
| Driver online/offline | no | yes own | monitor/force future |
| Matching offer response | no | yes assigned offer | monitor |
| Payment proof submit | own ride/order | no | review |
| Payment receipt confirm | no | assigned driver | review/override |
| Chat | participant | participant | case-authorized |
| Catalog customer read | yes | yes optional | yes |
| Catalog write | no | no | yes |
| Complaint submit | participant | participant | yes |
| Driver lock/unlock | no | no | yes/system |

# 22. Technical acceptance tests

- Unauthenticated business query rejects.
- Customer cannot query another customer active order detail.
- Driver cannot accept offer not sent to them.
- Locked driver cannot accept active offer.
- Customer cannot submit Food order with custom delivery fee.
- Food order cannot proceed to restaurant purchase before payment proof/confirmation policy is satisfied.
- Paid-but-driver-no-show complaint without payment proof is rejected.
- Second qualifying complaint auto-locks driver.
- Admin catalog publish without valid outlet/menu/region fails.
- Chat room cannot be read by non-participant.

# 23. Open API decisions

1. Exact GraphQL BigInt scalar implementation for Flutter/Admin clients.
2. Exact connection/pagination style: Relay full spec vs simple cursor.
3. Exact admin RBAC permission codes.
4. Exact Ride payment timing and payment record creation point.
5. Exact map/search APIs that remain backend-proxied vs direct HERE client SDK.

Resolved P0 decision:

- Public OTP endpoints are GraphQL mutations in the P0 contract: `requestOtp` and `verifyOtp`. A REST compatibility wrapper can be added later only if needed.
