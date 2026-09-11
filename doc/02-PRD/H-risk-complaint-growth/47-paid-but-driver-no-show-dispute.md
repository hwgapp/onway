# PRD: Paid-but-Driver-No-Show Dispute

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, Admin Portal, API Core Backend  

## 1. Objective

Protect customers and marketplace safety when a customer has submitted bank transfer proof but the driver does not arrive, does not continue, or becomes unreachable.

## 2. Scope

In scope:

- Complaint intake specialized for paid/no-show.
- Required payment proof linkage.
- Driver response request.
- Auto-lock rule after 2 qualifying open complaints.
- Admin manual lock/unlock.
- Timeline and evidence review.

Out of scope:

- Automatic bank refund.
- Onway-held escrow.
- Final legal recovery workflow.

## 3. Qualifying Complaint Rule

A complaint counts toward auto-lock only if all are true:

- It is tied to a real ride/order assigned to the driver.
- Customer submitted payment proof.
- Complaint category is paid-but-driver-no-show or driver non-performance after payment.
- Complaint is open and not rejected invalid.
- Complaint was not already counted as duplicate of another case.

Auto-lock threshold: 2 qualifying open complaints by default; configurable.

## 4. User Stories

### US-01 - Customer files paid/no-show complaint

As a customer, I want a fast complaint path when I transferred money and driver did not perform.

Acceptance criteria:

- Flow preloads ride/order and payment proof if available.
- Proof is required to submit this category.
- Customer can add chat screenshots/images/messages and description.
- Complaint enters high-priority review queue.

### US-02 - System auto-locks after threshold

As Onway, I want the driver blocked from receiving new jobs after repeated serious open complaints.

Acceptance criteria:

- System counts qualifying open complaints.
- At threshold, driver status changes to temporarily locked.
- Matching excludes driver immediately.
- Driver and admin receive status event.
- Audit log records auto-lock reason and complaint IDs.

### US-03 - Admin reviews no-show case

As support admin, I want a complete evidence timeline to decide.

Acceptance criteria:

- Admin sees payment proof, job state, GPS snapshots, chat, driver response, customer description.
- Admin can mark complaint valid/invalid/resolved/escalated.
- Admin can lock/unlock driver manually.

### US-04 - Driver responds to no-show complaint

As driver, I want to provide proof or explanation.

Acceptance criteria:

- Driver can submit response/evidence.
- Driver cannot receive new jobs if locked.
- Response does not automatically unlock driver.

## 5. Acceptance Tests

- Given first qualifying complaint opens, when driver has no other qualifying open complaints, then driver is not auto-locked.
- Given second qualifying complaint opens, when threshold is 2, then driver is auto-locked.
- Given complaint lacks payment proof, when submitted as paid/no-show, then API rejects or routes to general complaint.
- Given admin marks one complaint invalid, then driver remains locked until admin unlocks or policy explicitly auto-recalculates.

## 6. Open Questions

- SLA for first admin review.
- Whether auto-lock affects active in-progress job.
- Whether false complaints create customer restriction later.

