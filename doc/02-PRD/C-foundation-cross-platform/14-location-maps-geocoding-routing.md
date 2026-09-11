# PRD: Location, Maps, Geocoding & Routing

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, Admin Portal, API Core Backend  

## 1. Objective

Provide location, maps, geocoding, routing, distance, and ETA capabilities required by Ride, Food, matching, tracking, region validation, and admin polygon management.

## 2. Scope

In scope:

- HERE Maps integration.
- Address search/geocoding.
- Reverse geocoding where useful.
- Map point selection.
- Driver GPS collection.
- Route/distance/ETA estimate.
- Region polygon validation through PostGIS.
- Admin polygon draw/edit.

Out of scope:

- Multi-provider map abstraction beyond current HERE decision unless needed.
- Advanced traffic model ownership by Onway.

## 3. User Stories

### US-01 - Customer selects pickup/dropoff

As a customer, I want to search or pin locations so I can request a ride accurately.

Acceptance criteria:

- App supports address search and map pin.
- Selected coordinate is validated against service region rules.
- Display name and coordinate are stored in request draft.

### US-02 - Customer selects delivery address

As a customer ordering Food, I want to choose a delivery address and see whether the outlet can serve it.

Acceptance criteria:

- Delivery coordinate is validated against active Food region.
- Distance/ETA can be estimated from outlet to destination.
- Order placement blocks invalid address.

### US-03 - Driver shares realtime location

As a driver, I want the app to share my location while online/on job so matching and tracking work.

Acceptance criteria:

- Driver location updates flow through WebSocket.
- Backend stores last known presence in Redis.
- Important snapshots are persisted for audit/dispute where policy requires.

### US-04 - Admin manages region polygons

As admin, I want to draw/edit polygons so launch boundaries are controlled.

Acceptance criteria:

- Admin can create and edit polygon on map.
- Polygon validity is checked before activation.
- Polygon changes write audit log.

## 4. Acceptance Tests

- Given pickup is outside active Ride polygon, when customer requests ride, then request is blocked.
- Given driver is outside region, when matching searches candidates, then driver is excluded.
- Given admin creates self-intersecting polygon, when saving, then validation blocks it.
- Given driver location updates during active trip, when customer views tracking, then map marker updates.

## 5. Data Requirements

- Coordinate latitude/longitude.
- Human-readable address.
- Place provider ID when available.
- Region containment result.
- Route distance/time estimate.
- Location timestamp.
- Driver device/location accuracy when available.

## 6. Open Questions

- Minimum GPS accuracy threshold for driver matching.
- Whether routes are cached.
- Whether customer can save favorite addresses in MVP.

