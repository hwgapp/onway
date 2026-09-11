# PRD General: Driver App

**Phase:** P0  
**Status:** Draft  
**Platform:** Flutter Driver App  

## 1. Objective

Define the Driver App shell and baseline capabilities for driver onboarding, online availability, Ride/Food job execution, chat, payment confirmation, and risk lock visibility.

## 2. Scope

Driver App must support:

- Login/signup and phone verification.
- Onboarding status.
- Profile, vehicle, and service eligibility.
- Platform fee proof/reference submission.
- Online/offline state.
- Realtime location updates.
- Ride/Food offer accept/reject.
- Job lifecycle actions.
- Customer-driver chat with image sending.
- Payment proof viewing and receipt confirmation.
- Locked/suspended state display.

Out of scope:

- Driver Mission flows for restaurant/menu during launch P0.
- Driver-created restaurants or menus during launch P0.
- Trust/gamification dashboard during launch P0.

## 3. Navigation Areas

- Onboarding.
- Home/availability.
- Active job.
- Offers.
- Chat.
- Earnings/history.
- Profile/vehicle.
- Support.

## 4. User Stories

### US-01 - Driver cannot receive jobs before activation

As a driver applicant, I should not receive jobs until onboarding, eligibility, and platform fee verification are complete.

Acceptance criteria:

- Driver status controls access to online toggle.
- Inactive driver cannot connect as available for matching.
- App explains required pending steps.

### US-02 - Driver receives a timed offer

As an active driver, I want to receive Ride/Food job offers with enough context to accept or reject safely.

Acceptance criteria:

- Offer shows service type, pickup/outlet, destination/delivery area, estimated distance/time, fare/fee, and timeout.
- Driver can accept or reject exactly once per offer.
- Expired offers cannot be accepted.

### US-03 - Driver confirms payment state

As a driver, I want to see customer payment proof and confirm receipt so I know whether to continue service.

Acceptance criteria:

- Payment proof is visible only for assigned job.
- Driver can mark received or raise issue.
- Confirmation writes timeline/audit event.

### US-04 - Locked driver understands restriction

As a locked driver, I need to know I cannot receive new jobs and how to contact support/admin.

Acceptance criteria:

- Online toggle is disabled.
- Existing allowed actions are constrained by lock policy.
- App shows lock status and support entry point.

## 5. Acceptance Tests

- Given driver is not activated, when they tap online, then app blocks and shows pending requirements.
- Given offer timeout elapsed, when driver taps accept, then app shows expired and backend rejects.
- Given customer uploaded payment proof, when driver opens active job, then proof is visible.
- Given driver is locked by admin, when app receives event, then online state turns off and job offers stop.

## 6. Backend Dependencies

- Driver onboarding APIs.
- Platform fee verification APIs.
- Driver location WebSocket.
- Matching offer WebSocket.
- Ride/Food lifecycle APIs.
- Chat/media APIs.
- Risk lock/account status APIs.

## 7. Open Questions

- Driver documents checklist.
- Whether driver can complete an already-started job after lock.
- Exact background location permissions and battery handling.
