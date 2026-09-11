# PRD General: Merchant App Future

**Phase:** P2  
**Status:** Draft  
**Platform:** Future Merchant App  

## 1. Objective

Reserve product direction for a future Merchant App without making it a dependency for MVP launch.

## 2. Current MVP Position

Merchant App is not required in launch MVP. Food supply is managed by Onway admins through Admin Portal. Drivers do not manage restaurant/menu data in P0.

## 3. Future Scope

Merchant App may support:

- Merchant login and outlet access.
- Receive order notification earlier.
- Confirm availability.
- Prepare food before driver arrives.
- Update menu item availability.
- Update hours and temporary closure.
- View order history.
- Submit menu updates.
- Manage brand/outlet profile.

Out of scope until P2:

- Merchant payment settlement through Onway.
- Commission model.
- Merchant paid premium unless separately decided.

## 4. Future User Stories

### US-01 - Merchant can receive order signal

As a merchant operator, I want to receive order details before driver arrives so I can start preparing earlier.

Acceptance criteria:

- Merchant only sees orders for owned/authorized outlets.
- Order details exclude unnecessary customer private data.
- Merchant can accept/acknowledge preparation if enabled.

### US-02 - Merchant can manage availability

As a merchant, I want to mark items unavailable so customers do not order unavailable food.

Acceptance criteria:

- Availability update affects only authorized outlet or brand scope.
- Changes write audit trail.
- Customer App hides or marks unavailable items after config refresh.

### US-03 - Admin can approve merchant access

As an admin, I want to verify merchant ownership before granting outlet control.

Acceptance criteria:

- Merchant account starts pending review.
- Admin approves/rejects with evidence and reason.
- Merchant cannot update catalog before approval.

## 5. Acceptance Tests

- Given merchant lacks outlet permission, when they request outlet data, then API denies access.
- Given merchant marks item unavailable, when customer opens menu, then item cannot be added to cart.
- Given merchant submits menu price change, when auto-publish is disabled, then admin review is required.

## 6. Dependencies

- Identity/RBAC expansion.
- Merchant ownership verification.
- Catalog publishing workflow.
- Privacy/legal review for merchant data access.

## 7. Open Questions

- Whether merchant app is mobile, web, or responsive web.
- Merchant verification requirements.
- Premium merchant features and monetization.

