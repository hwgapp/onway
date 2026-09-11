# PRD General: Customer App

**Phase:** P0  
**Status:** Draft  
**Platform:** Flutter Customer App  

## 1. Objective

Define the Customer App shell and baseline capabilities for customers to use Ride and Food services in MVP.

## 2. Scope

Customer App must support:

- Firebase login/signup and phone verification flow.
- Region-aware home screen.
- Ride entry point.
- Food entry point.
- Profile and account status.
- Address search, map selection, and saved recent locations.
- Ride/Food tracking.
- Customer-driver chat with image sending.
- QR/bank transfer payment proof upload.
- Rating and complaint/dispute intake.

Out of scope:

- COD.
- Cash.
- Wallet.
- Full Trust dashboard.
- Loyalty and paid membership.

## 3. Navigation Areas

- Home.
- Ride.
- Food.
- Activity/history.
- Chat.
- Profile/account.
- Support/complaint.

## 4. User Stories

### US-01 - Customer sees available services

As a customer, I want the home screen to show only services available in my current region so I do not start unsupported flows.

Acceptance criteria:

- App checks active region by coordinate or selected city.
- Ride/Food entry points are hidden or disabled when unavailable.
- Disabled state includes clear reason and does not create a draft order/trip.

### US-02 - Customer completes a bank transfer proof step

As a customer, I want to upload proof after bank transfer so my driver and admin can verify payment if needed.

Acceptance criteria:

- Payment screen shows driver bank/QR details after match when applicable.
- Customer can upload or capture proof image.
- App validates image is present before continuing.
- Successful upload updates trip/order state.

### US-03 - Customer chats with assigned driver

As a customer, I want to chat and send images to the driver after matching so we can coordinate pickup, delivery, or order issues.

Acceptance criteria:

- Chat is only available for assigned active ride/order room.
- Text and image messages are supported.
- Message delivery state is shown.
- Chat retention is communicated through policy, not noisy in-flow UI.

### US-04 - Customer reports a payment/no-show issue

As a customer, I want to file a complaint when I transferred money but driver did not come or continue service.

Acceptance criteria:

- Complaint can attach payment proof, chat images/messages, and description.
- App shows submitted status and case reference.
- Customer sees that admin review is pending.

## 5. Acceptance Tests

- Given Food is unavailable in selected region, when customer opens app, then Food entry point is disabled.
- Given matched Food order requires prepayment, when customer tries to continue without proof, then app blocks progression.
- Given assigned ride is active, when customer sends image in chat, then driver receives it in same ride room.
- Given payment/no-show complaint is submitted, when customer views support history, then complaint status is visible.

## 6. Backend Dependencies

- Identity/auth account APIs.
- Region/service availability APIs.
- Ride/Food GraphQL operations.
- WebSocket tracking/chat events.
- Media evidence upload.
- Complaint/dispute APIs.

## 7. Open Questions

- Ride payment timing in Customer App.
- Exact customer account verification requirements beyond Firebase/phone.
- Whether image upload uses direct S3 signed URL or backend proxy.

