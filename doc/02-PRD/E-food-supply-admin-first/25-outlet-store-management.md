# PRD: Outlet / Store Management

**Phase:** P0  
**Status:** Draft  
**Platforms:** Admin Portal, API Core Backend  

## 1. Objective

Allow admins to create and manage physical outlets/stores under brands, including location, region, opening hours, service status, and discovery readiness.

## 2. Scope

In scope:

- Outlet create/edit.
- Brand relationship.
- Address and coordinate.
- Region validation.
- Opening hours.
- Store status.
- Service availability.
- Outlet contact/info fields.

Out of scope:

- Merchant-managed outlet data.
- Driver-created outlets.
- Automatic closure detection.

## 3. Outlet State Model

Suggested states:

- `draft`
- `pending_review`
- `active`
- `paused`
- `temporarily_closed`
- `closed`
- `archived`

## 4. User Stories

### US-01 - Admin creates outlet

As admin, I want to create an outlet with brand, address, coordinate, and region so it can later be published for Food ordering.

Acceptance criteria:

- Brand is required.
- Address and coordinate are required for active/published outlet.
- Coordinate is validated against configured region.
- Outlet cannot be customer-visible until required catalog conditions pass.

### US-02 - Admin configures opening hours

As admin, I want to set opening hours so customers only order when outlet is serviceable.

Acceptance criteria:

- Hours support days of week.
- Temporary closure can override hours.
- Timezone is derived from region/city or explicitly configured.
- Changes write audit log.

### US-03 - Admin pauses outlet

As admin, I want to pause an outlet if menu/location/hours are unreliable.

Acceptance criteria:

- Paused outlet is hidden or shown unavailable in Customer App.
- Existing in-flight orders keep their state and require operations handling if needed.
- Reason is required.

## 5. Acceptance Tests

- Given outlet coordinate outside active region, when admin tries to publish, then validation blocks.
- Given outlet is closed today, when customer views Food discovery, then outlet is unavailable.
- Given outlet is temporarily closed, when customer has item in cart, then checkout blocks.
- Given admin changes coordinate, when saving, then audit log records before/after.

## 6. Data Requirements

- Outlet ID.
- Brand ID.
- Name/display name.
- Address.
- Coordinate.
- Region ID.
- Phone/contact optional.
- Opening hours.
- Status.
- Availability flags.
- Audit metadata.

## 7. Open Questions

- Exact handling for outlets inside overlapping regions.
- Whether customer sees closed outlets or hides them.
- Initial HCMC outlet list.

