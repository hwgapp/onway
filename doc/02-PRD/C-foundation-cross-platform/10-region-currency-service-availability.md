# PRD: Region, Currency & Service Availability

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, Admin Portal, API Core Backend  

## 1. Objective

Allow Onway to launch services region by region with configurable country, city, polygon, currency, service availability, vehicle availability, and lifecycle state.

## 2. Scope

In scope:

- Country/city/region data model.
- Region polygon management.
- Currency per region.
- Service availability per region.
- Vehicle availability per region.
- Region lifecycle.
- Coordinate validation for pickup, dropoff, delivery address, driver location, outlet.

## 3. Region Lifecycle

Minimum states:

- `planned`
- `pilot`
- `active`
- `paused`
- `closed`

## 4. User Stories

### US-01 - Admin creates a service region

As an admin, I want to create a region polygon and configure services so Onway can launch gradually.

Acceptance criteria:

- Region must belong to country and city.
- Region must have currency.
- Region must have polygon before active state.
- Admin can enable Ride/Food independently.
- Admin can enable motorcycle/car independently.

### US-02 - Customer sees only available services

As a customer, I want the app to check my location and show services available in that region.

Acceptance criteria:

- Pickup/order coordinates are tested against active region polygon.
- If location is outside region, service request cannot proceed.
- Displayed money uses region currency.

### US-03 - Driver can go online only in eligible region

As a driver, I want to receive jobs only when my current location is in a valid active region for my services and vehicle.

Acceptance criteria:

- Driver location is validated against active region.
- Driver service and vehicle eligibility must match region config.
- If region pauses, driver stops receiving new offers.

### US-04 - Outlet is visible only if region-valid

As the system, I need Food outlets to appear only when outlet is inside active Food region and catalog is published.

Acceptance criteria:

- Outlet coordinate must be in active Food region.
- Customer cannot order from unpublished or out-of-region outlet.

## 5. Acceptance Tests

- Given region currency is VND, when customer views fare/menu, then prices display as VND.
- Given Ride is disabled in region, when customer selects pickup there, then Ride request is blocked.
- Given driver moves outside active polygon, when matching searches candidates, then driver is excluded.
- Given outlet is in paused region, when customer opens Food discovery, then outlet is hidden/unavailable.

## 6. Admin UI Requirements

- Map-based polygon draw/edit.
- Region list with state, city, currency, services, vehicle types.
- Validation errors before activate.
- Audit log for polygon and service changes.

## 7. Backend/Data Requirements

- Use PostGIS for polygon containment, distance, geofence, and availability checks.
- Currency must be stored as ISO-like code string, e.g. `VND`.
- Region config changes must be auditable and cache-invalidated.

## 8. Open Questions

- Initial HCMC region polygons.
- Whether trip can start inside region and end outside.
- Region overlap rules.

