# PRD: Food Discovery & Cart

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, API Core Backend, Admin Portal  

## 1. Objective

Allow customers to discover published Food outlets and build a valid cart from admin-managed catalog data.

## 2. Scope

In scope:

- Food home/discovery.
- Outlet list/detail.
- Published menu display.
- Category/item/modifier selection.
- Cart creation/update.
- Cart validation against availability.

Out of scope:

- Merchant App.
- Driver-created catalog.
- AI/community catalog verification.
- Food delivery fee negotiation.

## 3. Preconditions

- Region has Food enabled.
- Outlet is active and inside Food region.
- Brand/outlet/menu are published.
- Items are available.
- Customer has valid delivery address or selects later according to UX.

## 4. User Stories

### US-01 - Customer sees available outlets

As a customer, I want to browse restaurants/stores available in my region.

Acceptance criteria:

- Only active/published outlets are shown.
- Closed/paused/unpublished outlets are hidden or unavailable according to policy.
- Outlet list uses region and delivery area rules.

### US-02 - Customer views menu

As a customer, I want to view menu categories, items, prices, and modifiers.

Acceptance criteria:

- Menu reflects canonical menu plus outlet overrides.
- Prices display region currency.
- Unavailable items cannot be added.

### US-03 - Customer builds cart

As a customer, I want to add items/modifiers to cart.

Acceptance criteria:

- Required modifiers must be selected.
- Quantity can be adjusted.
- Cart stores item/modifier price snapshot for review.
- Cart validates before checkout.

### US-04 - Cart updates when catalog changes

As the system, I need to prevent stale cart checkout.

Acceptance criteria:

- Checkout revalidates item availability and price.
- Customer must accept updated cart if price/item state changed.
- Removed/unavailable items block order placement until resolved.

## 5. Acceptance Tests

- Given outlet menu is unpublished, when customer searches Food, then outlet cannot be ordered.
- Given item requires size modifier, when customer adds without size, then app blocks.
- Given item becomes unavailable while in cart, when customer checks out, then validation requires update.
- Given outlet override price exists, when cart totals, then effective price is used.

## 6. Analytics

- Food discovery opened.
- Outlet viewed.
- Item viewed.
- Item added to cart.
- Cart validation failed.
- Cart abandoned.

## 7. Open Questions

- Search/filter/sort scope for P0.
- Whether customer can order from only one outlet per cart.
- Whether item photos are required.

