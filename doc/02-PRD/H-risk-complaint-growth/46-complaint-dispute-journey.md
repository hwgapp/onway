# PRD: Complaint & Dispute Journey

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, Admin Portal, API Core Backend  

## 1. Objective

Provide a structured complaint and dispute workflow so customers, drivers, and admins can handle service issues, payment concerns, and safety/risk cases.

## 2. Scope

In scope:

- Customer complaint intake.
- Driver complaint/response path.
- Complaint categories.
- Evidence attachments.
- Admin/operator review queue.
- Case timeline.
- Decision recording.
- Link to driver risk lock when applicable.

Out of scope:

- Automated financial recovery.
- Full legal escalation workflow.
- AI triage as required P0 dependency.

## 3. Complaint Categories

Initial categories:

- Paid but driver did not arrive/continue.
- Driver says payment not received.
- Food item/price issue.
- Driver cancelled after payment.
- Customer no-show.
- Driver behavior/service issue.
- Customer behavior/service issue.
- Safety concern.
- Other.

## 4. Complaint State Model

Suggested states:

- `submitted`
- `needs_more_evidence`
- `open_under_review`
- `driver_response_requested`
- `customer_response_requested`
- `resolved`
- `rejected_invalid`
- `escalated_fraud_review`
- `closed`

## 5. User Stories

### US-01 - Customer submits complaint

As a customer, I want to submit a complaint tied to a ride/order so support can investigate.

Acceptance criteria:

- Complaint must link to ride/order where applicable.
- Customer selects category and provides description.
- Customer can attach payment proof, chat images, or additional evidence.
- Complaint receives case ID/status.

### US-02 - Driver responds to complaint

As a driver, I want to respond to a complaint with context and evidence.

Acceptance criteria:

- Driver sees complaint summary when response is requested.
- Driver can submit text and evidence.
- Response is timestamped and visible to admin.

### US-03 - Admin reviews complaint

As support admin, I want a queue and case detail page so I can resolve disputes.

Acceptance criteria:

- Queue can filter by category, status, severity, driver, customer, service type.
- Case detail shows timeline, state history, payment proof, chat, media, GPS snapshots, and related account history.
- Admin decision requires reason.

### US-04 - Complaint can escalate to fraud

As admin, I want to escalate serious cases to fraud review.

Acceptance criteria:

- Escalation creates/links fraud case.
- Original complaint remains traceable.
- Driver/customer status actions are separate auditable decisions.

## 6. Acceptance Tests

- Given customer submits complaint with payment proof, when admin opens case, then proof is visible.
- Given admin requests driver response, when driver app opens support, then response task is visible.
- Given complaint is rejected invalid, when driver risk count is calculated, then complaint does not qualify.
- Given complaint escalates to fraud, when audit timeline is viewed, then escalation event appears.

## 7. Open Questions

- Admin SLA by complaint category.
- Exact severity levels.
- Whether customer/driver can reopen closed cases.

