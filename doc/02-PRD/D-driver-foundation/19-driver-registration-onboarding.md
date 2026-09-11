# PRD: Driver Registration & Onboarding

**Phase:** P0  
**Status:** Draft  
**Platforms:** Driver App, Admin Portal, API Core Backend  

## 1. Objective

Allow prospective drivers to register and move through onboarding while preventing job access until required verification and activation steps are complete.

## 2. Scope

In scope:

- Driver account creation.
- Phone verification through backend ViHAT OTP and Firebase custom-token sign-in.
- Basic profile collection.
- Identity/document placeholder workflow.
- Admin review status.
- Onboarding progress display.
- Activation dependency on platform fee verification and service eligibility.

Out of scope:

- Final document checklist details.
- Automated KYC vendor integration.
- Full Trust Engine.

## 3. Onboarding State Model

Suggested states:

- `draft`
- `phone_verified`
- `profile_submitted`
- `documents_required`
- `documents_submitted`
- `admin_review`
- `changes_requested`
- `approved_pending_platform_fee`
- `rejected`
- `activated`

## 4. User Stories

### US-01 - Driver creates account

As a driver applicant, I want to create an account with phone verification so I can begin onboarding.

Acceptance criteria:

- Driver completes ViHAT OTP verification through backend.
- Backend returns Firebase custom token; app signs in to Firebase.
- Backend creates driver profile linked to Firebase UID.
- Driver starts in non-active onboarding state.
- App shows next required step.

### US-02 - Driver submits profile information

As a driver applicant, I want to provide personal and vehicle/service intent information so Onway can review eligibility.

Acceptance criteria:

- Required fields are validated.
- Driver can save draft before final submission where appropriate.
- Submission changes state and writes audit event.

### US-03 - Driver submits required documents placeholder

As a driver applicant, I want to upload required documents once document policy is defined.

Acceptance criteria:

- App displays document requirements returned by backend config.
- Each required document has status: missing, uploaded, rejected, approved.
- Driver cannot bypass required document status.

### US-04 - Admin reviews onboarding

As a driver review admin, I want to approve, reject, or request changes.

Acceptance criteria:

- Admin sees profile, documents, vehicle/service intent, and history.
- Admin decision requires reason.
- Driver receives status update.
- Approval does not activate driver until platform fee/payment policy is satisfied.

## 5. Acceptance Tests

- Given driver only verified phone, when tapping online, then app blocks with onboarding incomplete.
- Given admin requests changes, when driver opens onboarding, then rejected fields/reason are visible.
- Given driver documents are all approved but platform fee is not verified, when activation check runs, then driver remains not active.
- Given admin rejects driver, when matching searches candidates, then driver is excluded.

## 6. Admin Requirements

- Onboarding queue with filters by status, city, vehicle type, submitted date.
- Driver detail page.
- Document viewer.
- Approve/reject/request changes actions.
- Audit timeline.

## 7. Open Questions

- Exact driver document list by vehicle/service.
- Whether background check is manual or vendor-based.
- Whether rejection can be appealed in MVP.
