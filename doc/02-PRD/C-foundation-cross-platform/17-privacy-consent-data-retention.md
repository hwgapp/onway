# PRD: Privacy, Consent & Data Retention

**Phase:** P0  
**Status:** Draft  
**Platforms:** All  

## 1. Objective

Define MVP privacy, consent, and retention expectations for identity, GPS, payment proof, chat, media evidence, driver documents, and audit data.

## 2. Scope

In scope:

- Consent surfaces for location, notifications, camera/media, identity/documents.
- Chat retention: 1 week.
- Evidence retention categories.
- Admin access controls for sensitive data.
- Data deletion/export direction.

Out of scope:

- Final legal policy language.
- Cross-border privacy handling.
- Advanced privacy automation.

## 3. Sensitive Data Categories

- Phone number.
- Identity documents.
- Vehicle documents.
- GPS/location.
- Device metadata.
- Payment proof images.
- Chat text/images.
- Complaint/fraud evidence.
- Audit/admin decisions.

## 4. User Stories

### US-01 - Customer grants required permissions

As a customer, I want to understand why Onway needs location, camera/media, and notifications.

Acceptance criteria:

- App requests permissions at relevant time.
- Denied permission produces clear fallback or blocked action.
- Payment proof upload cannot proceed without camera/gallery/media access required by implementation.

### US-02 - Driver consents to location tracking while online

As a driver, I need clear permission handling for location tracking while online/on job.

Acceptance criteria:

- Driver cannot go online without required location permission.
- App explains location use for matching/tracking/safety.
- Location updates stop when offline except allowed job/fallback policy.

### US-03 - Admin access is limited and audited

As the company, Onway needs sensitive evidence access to be permissioned.

Acceptance criteria:

- Admin must have role permission to view identity/payment/chat evidence.
- Critical evidence access may write audit log.
- Sensitive media is not exposed through public URLs.

### US-04 - Chat content expires after 1 week

As a user, I expect chat content not to be retained indefinitely.

Acceptance criteria:

- Chat text/image content follows 1-week retention.
- Cases filed before expiration preserve required evidence according to dispute policy.
- Retention jobs are monitored and auditable.

## 5. Acceptance Tests

- Given driver denies location permission, when tapping online, then app blocks.
- Given chat message is older than 1 week and not preserved by complaint, when retention job runs, then content is removed/processed.
- Given admin lacks evidence permission, when requesting payment proof, then API denies.
- Given customer requests data deletion, when status is recorded, then account enters deletion workflow placeholder if not fully automated.

## 6. Open Questions

- Exact retention for payment proof and driver documents.
- Whether chat metadata remains after content deletion.
- Data export/delete implementation timeline.
- Legal review outcome for phone number visibility.

