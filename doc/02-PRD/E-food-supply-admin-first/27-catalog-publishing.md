# PRD: Catalog Publishing

**Phase:** P0  
**Status:** Draft  
**Platforms:** Admin Portal, API Core Backend, Customer App  

## 1. Objective

Define how brand/outlet/menu data moves from internal draft to customer-visible published catalog.

## 2. Scope

In scope:

- Catalog state machine.
- Publish validations.
- Unpublish/archive.
- Needs reverification state.
- Customer visibility rules.
- Audit trail.

Out of scope:

- Community verification P2.
- Merchant approval workflow.
- AI auto-publishing.

## 3. Catalog State Model

Suggested states:

- `draft`
- `pending_review`
- `published`
- `needs_reverification`
- `unpublished`
- `archived`

## 4. User Stories

### US-01 - Admin submits catalog for review

As catalog admin, I want to move completed menu/outlet data to review before publishing.

Acceptance criteria:

- Required fields are validated.
- Missing outlet coordinate, active region, opening hours, or menu item blocks progression.
- Reviewer can see diff/summary.

### US-02 - Admin publishes catalog

As authorized admin, I want to publish catalog so customers can discover and order.

Acceptance criteria:

- Only authorized role can publish.
- Publish requires brand active, outlet valid, menu valid, region Food enabled.
- Published catalog becomes visible to Customer App.
- Publish writes audit event and version.

### US-03 - Admin marks catalog needs reverification

As admin/support, I want to mark catalog as needs reverification when data may be stale or disputed.

Acceptance criteria:

- State is visible in admin.
- Customer visibility follows policy: still visible with caution or hidden/unavailable.
- Reason and source are recorded.

### US-04 - Admin unpublishes catalog

As admin, I want to remove inaccurate catalog from customer ordering.

Acceptance criteria:

- Unpublish requires reason.
- New orders are blocked.
- In-flight orders are preserved for operations handling.

## 5. Acceptance Tests

- Given outlet has no published menu, when customer opens Food, then outlet cannot be ordered.
- Given admin publishes valid catalog, when customer refreshes Food discovery, then outlet/menu appears.
- Given menu is marked needs reverification and policy hides it, when customer searches, then menu is not orderable.
- Given admin archives old menu version, when audit history is opened, then previous version remains traceable.

## 6. Open Questions

- Whether `pending_review` requires a second admin.
- Customer behavior for `needs_reverification`.
- Version rollback behavior.

