# PRD Master: Onway MVP

**Phase:** P0  
**Status:** Draft  
**Parent:** `doc/02-PRD/ONWAY_PRD_MASTER_v0.1_VI.md`  

## 1. Objective

Define the MVP product surface for Onway across API Core Backend, Customer App, Driver App, Web Admin Portal, Landing Web, and future Merchant App. This PRD is the product anchor for all downstream platform and journey PRDs.

## 2. MVP Positioning

Onway MVP is a ride hailing and food delivery marketplace with:

- 0% commission on ride fare, delivery fee, food value, driver earnings, and merchant revenue.
- Direct bank transfer/QR payment between customer and driver.
- No COD, cash, payment gateway, wallet, escrow, or Onway-held payment in MVP.
- Admin-first restaurant catalog and menu setup for Food.
- Realtime driver location, matching, tracking, and customer-driver chat.
- Admin-managed exception handling for complaints, payment disputes, and driver risk lock.

## 3. Platforms In Scope

| Platform | MVP Role |
|---|---|
| API Core Backend | Domain logic, GraphQL, WebSocket realtime, matching, audit, policy config. |
| Customer App | Ride/Food request, chat, payment proof, tracking, rating, complaint. |
| Driver App | Online status, job accept/reject, tracking, chat, payment confirmation, fulfillment. |
| Web Admin Portal | Region, driver review, food catalog, monitoring, risk lock, dispute, audit. |
| Landing Web | P1 marketing/information surface. |
| Merchant App | P2 future merchant integration. |

## 4. MVP Exclusions

- COD and cash.
- Payment gateway integration.
- Wallet, escrow, or Onway-held payment.
- Full Trust Engine.
- Food delivery fee negotiation.
- Default Ride price negotiation.
- Merchant App.
- Driver-sourced menu/restaurant operations.
- AI menu extraction production workflow.
- Advertising.

## 5. Master User Stories

### US-01 - Customer can use core services

As a customer, I want to sign in, request a ride, order food, chat with the assigned driver, upload bank transfer proof, track service progress, and rate/report after completion.

Acceptance criteria:

- Customer can create/login to an account.
- Customer can see only services available in the current active region.
- Customer can request Ride and Food without COD/cash options.
- Customer must upload payment proof when the flow requires bank transfer confirmation.
- Customer can open chat with assigned driver after match.
- Customer can create a complaint with payment proof, chat evidence, and description.

### US-02 - Driver can receive and complete jobs

As a driver, I want to register, be approved, pay/verify platform fee, go online, receive Ride/Food offers, chat with customer, confirm payment, and complete jobs.

Acceptance criteria:

- Driver cannot receive jobs before account is active and service eligible.
- Driver location is visible to matching/tracking while online or on job.
- Driver can accept/reject offers within timeout.
- Driver cannot receive new jobs when locked, suspended, or under disqualifying review.
- Driver can view payment proof submitted by customer for assigned job.

### US-03 - Admin can operate MVP safely

As an admin/operator, I want to configure regions, review drivers, create food supply, monitor jobs, inspect evidence, and lock/unlock risky drivers.

Acceptance criteria:

- Admin can configure region, currency, service availability, and vehicle availability.
- Admin can manage brand, outlet, menu, publishing, and availability.
- Admin can see ride/order state timeline, chat evidence, payment proof, and location snapshots.
- Admin can manually lock/unlock driver accounts with reason and audit trail.
- System auto-locks a driver when the configured complaint threshold is met.

## 6. Cross-Platform Acceptance Tests

- Given no active region contains a customer coordinate, when customer opens Ride/Food, then services are unavailable with clear reason.
- Given a customer places a Food order, when no payment proof is uploaded, then driver purchase flow cannot start.
- Given two qualifying paid-but-driver-no-show complaints exist for one driver, when the second complaint is accepted as open/qualifying, then driver is automatically locked from new jobs.
- Given admin changes a policy config value, when related flow runs next, then the new value applies without redeploy.
- Given a chat room is older than 1 week, when retention job runs, then chat content/image handling follows privacy retention policy.

## 7. Dependencies

- Architecture/codebase foundation.
- Identity/auth/account.
- Region/currency/service availability.
- Direct bank transfer/payment confirmation.
- Communication/chat/contact policy.
- Evidence/media/audit trail.
- Admin monitoring and manual risk action.

## 8. Open Decisions

- Exact Ride bank transfer timing.
- Exact definition of qualifying complaint for auto-lock.
- Admin SLA for dispute handling.
- Initial HCMC polygons.
- Driver document checklist.

