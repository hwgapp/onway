# PRD: Driver Risk Lock & Manual Admin Action

**Phase:** P0  
**Status:** Draft  
**Platforms:** API Core Backend, Admin Portal, Driver App  

## 1. Objective

Prevent drivers with repeated serious open complaints from receiving more jobs while admin investigates, especially paid-but-driver-no-show cases.

## 2. Scope

In scope:

- Driver lock status.
- Auto-lock after 2 qualifying open complaints.
- Manual admin lock/unlock.
- Driver app lock visibility.
- Matching exclusion.
- Audit trail.

Out of scope:

- Full Trust Engine.
- Permanent ban legal process details.
- Automated financial recovery.

## 3. Lock State Model

Suggested driver risk statuses:

- `clear`
- `under_review`
- `temporarily_locked`
- `suspended`
- `blocked`

P0 auto-lock should set `temporarily_locked` or `under_review_locked` depending on implementation naming.

## 4. Qualifying Complaint Concept

A complaint may qualify for auto-lock if:

- Complaint type is paid-but-driver-no-show or similar serious non-performance after transfer.
- Complaint includes required payment proof.
- Complaint is open and not rejected/invalid.
- Complaint links to a real ride/order assigned to the driver.

Exact criteria remain open and must be refined in dispute PRD.

## 5. User Stories

### US-01 - System auto-locks driver after threshold

As Onway, I want a driver to be auto-locked after 2 qualifying open complaints so they cannot continue taking jobs while risk is reviewed.

Acceptance criteria:

- Threshold is policy configurable.
- Only qualifying open complaints count.
- Auto-lock writes audit/system event.
- Matching excludes locked driver immediately.
- Driver App receives status update.

### US-02 - Admin manually locks driver

As admin, I want to lock a driver manually when I see urgent risk.

Acceptance criteria:

- Admin action requires permission and reason.
- Lock status takes effect immediately.
- Driver cannot receive new offers.
- Action is visible in audit timeline.

### US-03 - Admin unlocks driver after review

As admin, I want to unlock a driver if complaints are invalid or resolved.

Acceptance criteria:

- Unlock requires reason and permission.
- Driver eligibility is recalculated after unlock.
- Unlock does not erase complaint history.

### US-04 - Driver sees lock state

As a driver, I want to know why I cannot receive jobs.

Acceptance criteria:

- Driver App disables online/job receiving.
- App shows support/contact path.
- Sensitive investigation details are not overexposed.

## 6. Acceptance Tests

- Given driver has one qualifying open complaint, when second qualifying complaint is opened, then driver is auto-locked.
- Given driver is locked, when matching queries candidates, then driver is excluded.
- Given admin unlocks driver, when driver meets all other eligibility, then they can go online again.
- Given complaint is rejected as invalid, when count drops below threshold, then auto-unlock does not happen unless policy explicitly allows.

## 7. Open Questions

- Whether lock affects active in-progress job.
- Exact complaint qualification criteria.
- SLA and escalation for locked driver review.

