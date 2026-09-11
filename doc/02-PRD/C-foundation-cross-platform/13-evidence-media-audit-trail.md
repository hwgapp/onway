# PRD: Evidence, Media & Audit Trail

**Phase:** P0  
**Status:** Draft  
**Platforms:** All  

## 1. Objective

Provide a reliable evidence and audit foundation for payment proof, chat images, driver onboarding documents, catalog images, complaints, and admin actions.

## 2. Scope

In scope:

- Media upload references and metadata.
- Payment proof evidence.
- Chat image evidence.
- Driver document media.
- Catalog/menu images.
- Complaint attachments.
- Audit trail for critical state changes.

Out of scope:

- Production OCR/AI image verification during launch P0.
- Long-term evidence retention policy beyond specific PRD defaults.

## 3. Evidence Metadata

Each evidence object should store:

- Evidence ID.
- Linked entity type/id.
- Uploader actor type/id.
- Media type.
- Storage key/reference.
- Original filename if safe.
- MIME type.
- Size.
- Uploaded at.
- GPS/device/timestamp metadata where relevant and permitted.
- Visibility rules.
- Retention category.

## 4. User Stories

### US-01 - Customer uploads payment proof

As a customer, I need payment proof to be attached to the ride/order so driver and admin can verify transfer.

Acceptance criteria:

- Proof is required before continuing in configured payment flows.
- Proof links to trip/order and payment step.
- Driver and admin can view proof according to role.

### US-02 - Admin audits critical decisions

As admin/auditor, I need to see who changed what and why.

Acceptance criteria:

- Driver lock/unlock, catalog publish, region config, payment dispute decisions are audited.
- Audit cannot be edited/deleted through normal admin UI.
- Audit entry includes actor, action, target, timestamp, reason, and safe before/after summary.

### US-03 - Evidence is used in dispute review

As a support operator, I want all relevant evidence visible in one case timeline.

Acceptance criteria:

- Complaint page includes payment proof, chat images, driver/customer messages, state timeline, and admin actions.
- Evidence has timestamps and uploader identity.

## 5. Acceptance Tests

- Given customer submits payment proof, when admin opens the related case, then proof appears with timestamp and uploader.
- Given admin locks a driver, when audit log is queried, then lock action includes admin, reason, and target driver.
- Given unauthorized driver requests unrelated payment proof, when API checks access, then request is denied.
- Given media upload fails, when customer attempts continue, then payment step remains incomplete.

## 6. Storage Requirements

- Store binary objects in S3 or equivalent object storage.
- Store metadata in database.
- Use signed URLs or controlled media access.
- Avoid exposing raw private storage keys to unauthorized clients.

## 7. Open Questions

- Exact file size/type limits.
- Image compression rules.
- Retention behavior per evidence category.
