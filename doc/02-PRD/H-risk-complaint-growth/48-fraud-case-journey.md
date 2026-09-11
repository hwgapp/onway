# PRD: Fraud Case Journey

**Phase:** P0  
**Status:** Draft  
**Platforms:** Admin Portal, API Core Backend, Customer App, Driver App  

## 1. Objective

Define a structured fraud case workflow for serious suspected intentional abuse while separating fraud from ordinary service complaints.

## 2. Scope

In scope:

- Fraud case creation from complaint/admin action.
- Evidence collection.
- Driver/customer response.
- Human decision.
- Appeal placeholder.
- Account restrictions.
- Audit log.

Out of scope:

- AI as required P0 decision-maker.
- Automated financial recovery.
- Final legal enforcement.

## 3. Fraud Case State Model

Suggested states:

- `reported`
- `triage`
- `evidence_collection`
- `response_requested`
- `human_review`
- `confirmed`
- `rejected`
- `appeal_requested`
- `finalized`

## 4. Fraud Examples

Potential fraud:

- Receiving customer transfer then intentionally not buying/delivering.
- Fake completion.
- Fake GPS.
- Fake/reused evidence.
- Fake referral or fake account.
- Collusion.

Not automatically fraud:

- Late delivery.
- Poor attitude.
- Mistake without intent.
- Simple cancellation.
- Low service quality.

## 5. User Stories

### US-01 - Admin creates fraud case

As admin, I want to escalate serious complaint into fraud case.

Acceptance criteria:

- Fraud case links source complaint/order/trip.
- Case includes allegation category.
- Evidence list starts from linked complaint evidence.
- Creation writes audit log.

### US-02 - Admin collects evidence

As admin, I want to gather timeline, payment proof, chat, GPS, and account history.

Acceptance criteria:

- Case page aggregates relevant evidence.
- Admin can request more evidence from customer/driver.
- Evidence additions are timestamped.

### US-03 - Human makes final decision

As Onway, high-risk fraud outcomes must be decided by a human.

Acceptance criteria:

- Confirm/reject/finalize requires authorized admin.
- Decision requires reason.
- Account action is separate but linked.
- Decision is auditable.

### US-04 - Driver/customer can appeal placeholder

As affected user, I may need an appeal route after fraud decision.

Acceptance criteria:

- P0 can record appeal requested manually or through support.
- Appeal does not automatically reverse restrictions.
- Appeal timeline remains linked.

## 6. Acceptance Tests

- Given complaint escalates, when fraud case is created, then source case is linked.
- Given admin confirms fraud, when decision saved, then audit event includes admin/reason/timestamp.
- Given AI suggestion exists in future, when no human confirms high-risk decision, then fraud cannot finalize as confirmed.
- Given fraud is rejected, when driver was locked, then unlock still requires separate admin/policy action.

## 7. Open Questions

- Fraud financial responsibility policy.
- Appeal SLA.
- Legal-approved wording for fraud outcomes.

