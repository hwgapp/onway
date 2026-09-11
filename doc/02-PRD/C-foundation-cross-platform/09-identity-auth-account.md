# PRD: Identity, Auth & Account

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, Admin Portal, API Core Backend  

## 1. Objective

Provide a secure identity foundation using ViHAT OTP through the backend, Firebase custom token sign-in, and internal Onway account records, actor roles, and account status controls.

## 2. Scope

In scope:

- ViHAT OTP request/verification through backend.
- Firebase custom token sign-in after OTP verification.
- Firebase ID token verification for API/WebSocket sessions.
- Internal account mapping.
- Actor roles: customer, driver, admin/operator.
- Account statuses.
- Basic session handling.
- Locked/suspended status enforcement.

Out of scope:

- Full Trust Engine.
- Social login unless supported by Firebase and separately prioritized.
- Merchant identity until P2.

## 3. Account Status Model

Minimum statuses:

- `active`
- `pending_verification`
- `pending_driver_review`
- `pending_platform_fee`
- `under_review`
- `locked`
- `suspended`
- `blocked`
- `deleted_requested`

## 4. User Stories

### US-01 - Customer signs up with phone

As a customer, I want to sign up and verify my phone number so I can request services.

Acceptance criteria:

- Customer completes ViHAT OTP verification through backend.
- Backend returns Firebase custom token and app signs in to Firebase.
- Backend creates or links internal customer profile.
- Duplicate phone identity does not create duplicate active accounts.
- Customer account starts active or minimum allowed customer status according to policy.

### US-02 - Driver signs up but cannot work yet

As a driver applicant, I want to create an account but understand I must complete review before receiving jobs.

Acceptance criteria:

- Driver Firebase identity, created from backend custom-token flow, maps to driver profile.
- Driver starts in non-active status.
- Online toggle and job receiving are blocked until activation.

### US-03 - Admin logs into portal

As an admin, I want secure portal login with role authorization.

Acceptance criteria:

- Admin identity must map to internal admin user.
- Admin without portal permission cannot access portal APIs.
- Admin role is included in authorization checks but not trusted only from client.

### US-04 - Locked account is blocked consistently

As the system, I need locked/suspended/blocked accounts to be prevented from disallowed actions across all apps.

Acceptance criteria:

- Locked driver cannot go online or receive offers.
- Suspended customer cannot create new Ride/Food requests.
- Status changes are pushed to active sessions where possible.

## 5. Acceptance Tests

- Given a customer authenticated with Firebase ID token after ViHAT OTP custom-token flow, when they first call `me`, then backend creates/returns internal profile according to policy.
- Given a driver is `pending_platform_fee`, when they attempt online, then API rejects with next required step.
- Given admin has readonly role, when they attempt lock driver mutation, then API rejects.
- Given driver is locked mid-session, when WebSocket receives status event, then Driver App disables online/job receiving.

## 6. Data Requirements

- Firebase UID created/linked by backend custom-token flow.
- Phone number.
- Actor type/profile links.
- Account status and status reason.
- Created/updated timestamps.
- Last login/session metadata where needed.
- Audit log for admin status changes.

## 7. Open Questions

- Whether one phone can hold both customer and driver profiles.
- Exact customer verification requirements beyond phone.
- Account deletion/export process details.
