# PRD: Canonical Menu & Catalog Management

**Phase:** P0  
**Status:** Draft  
**Platforms:** Admin Portal, API Core Backend  

## 1. Objective

Allow admins to create and maintain canonical menus for brands and menu data for Food ordering before Merchant App, driver missions, or AI extraction exist.

## 2. Scope

In scope:

- Canonical brand menu.
- Categories.
- Items.
- Prices.
- Modifiers/options.
- Item images optional.
- Menu versioning/publishing relationship.
- Manual admin entry/import.

Out of scope:

- AI OCR production workflow.
- Merchant menu self-service.
- Driver menu capture in MVP.

## 3. Menu Model

Minimum entities:

- Menu.
- Menu version.
- Category.
- Item.
- Modifier group.
- Modifier option.
- Price.
- Availability.

## 4. User Stories

### US-01 - Admin creates canonical menu

As admin, I want to create a canonical menu for a brand so multiple outlets can reuse the same base catalog.

Acceptance criteria:

- Menu belongs to brand.
- Menu can remain draft until complete.
- Categories and items can be ordered.
- Menu changes create version/history.

### US-02 - Admin creates menu item

As admin, I want to create item name, description, price, and optional image so customers can order accurately.

Acceptance criteria:

- Item name and price are required.
- Price uses region/outlet currency context.
- Item can be active/unavailable/draft.
- Changes write audit log.

### US-03 - Admin configures modifiers

As admin, I want to define options like size, topping, sugar/ice, or required choices.

Acceptance criteria:

- Modifier group can be required or optional.
- Min/max selections are validated.
- Option price deltas are supported if needed.
- Cart validation uses modifier constraints.

### US-04 - Admin imports or uploads menu source

As admin, I want to upload menu images/files as reference while manually entering structured catalog.

Acceptance criteria:

- Source media can be attached to brand/menu/outlet.
- Upload does not auto-publish structured items.
- Admin can use source as evidence/reference.

## 5. Acceptance Tests

- Given required modifier has no selected option, when customer checks out, then cart validation fails.
- Given menu item has negative price, when admin saves, then validation blocks.
- Given menu is draft, when customer opens Food discovery, then draft items are not visible.
- Given admin edits published item price, when saving, then new version/audit event is created according to publishing policy.

## 6. Admin UI Requirements

- Menu tree/category list.
- Item editor.
- Modifier group editor.
- Drag/reorder.
- Bulk status changes.
- Preview published customer menu.

## 7. Open Questions

- Whether CSV/XLSX import is needed in P0.
- Required image specs for menu items.
- Price tax/fee display rules.

