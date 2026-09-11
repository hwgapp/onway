# PRD: Restaurant Brand / Chain Management

**Phase:** P0  
**Status:** Draft  
**Platforms:** Admin Portal, API Core Backend  

## 1. Objective

Allow admins to create and manage restaurant brands/chains that act as parent entities for outlets and canonical menus.

## 2. Scope

In scope:

- Brand creation/editing.
- Brand status.
- Brand category/type.
- Brand-level metadata.
- Brand-level waiting policy linkage.
- Relationship to outlets and canonical menu.

Out of scope:

- Merchant self-service brand creation.
- Brand advertising/sponsorship.
- Legal trademark approval workflow.

## 3. Brand State Model

Suggested states:

- `draft`
- `active`
- `paused`
- `archived`

## 4. User Stories

### US-01 - Admin creates brand

As an operations admin, I want to create a brand/chain so outlets and menus can be organized consistently.

Acceptance criteria:

- Brand name is required.
- Duplicate detection warns on similar brand names.
- Brand can be saved as draft.
- Create/edit actions write audit log.

### US-02 - Admin categorizes brand

As admin, I want to categorize brands so customer discovery and admin filtering can work.

Acceptance criteria:

- Brand can have cuisine/service categories.
- Categories are configurable or selected from controlled list.
- Category changes affect discovery only after catalog publish rules are satisfied.

### US-03 - Admin pauses brand

As admin, I want to pause a brand if data is wrong or service should stop.

Acceptance criteria:

- Paused brand hides or disables related outlets according to policy.
- Existing active orders are not silently deleted.
- Pause requires reason and audit log.

## 5. Acceptance Tests

- Given admin creates brand without name, when saving, then validation blocks.
- Given brand is paused, when customer opens Food discovery, then related outlets are unavailable/hidden.
- Given duplicate-like brand exists, when creating similar name, then admin receives warning.
- Given brand is archived, when creating new outlet, then brand cannot be selected.

## 6. Data Requirements

- Brand ID.
- Name.
- Display name.
- Category/tags.
- Status.
- Logo/image references optional.
- Default waiting policy reference optional.
- Audit metadata.

## 7. Open Questions

- Whether brand logo is required for MVP.
- Exact initial brand list for HCMC launch.
- Trademark/legal review requirements.

