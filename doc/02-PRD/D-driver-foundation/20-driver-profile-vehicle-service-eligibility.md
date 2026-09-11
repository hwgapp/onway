# PRD: Driver Profile, Vehicle & Service Eligibility

**Phase:** P0  
**Status:** Draft  
**Platforms:** Driver App, Admin Portal, API Core Backend  

## 1. Objective

Define driver profile, vehicle, and service eligibility rules so matching can safely decide which drivers can receive Ride and Food jobs.

## 2. Scope

In scope:

- Driver personal profile baseline.
- Vehicle records for motorcycle and car.
- Service eligibility for Ride/Food.
- Region eligibility.
- Admin review and status.
- Eligibility checks in matching.

Out of scope:

- Final legal compliance checklist.
- Driver Trust levels.
- Fleet/company driver accounts.

## 3. Eligibility Dimensions

Driver can be eligible by:

- Account status.
- Onboarding verification status.
- Platform fee status.
- Vehicle type.
- Service type.
- Region.
- Risk lock/suspension status.
- Required documents.

## 4. User Stories

### US-01 - Driver adds vehicle

As a driver, I want to add my motorcycle or car so Onway can determine which services I can provide.

Acceptance criteria:

- Driver selects vehicle type.
- Required vehicle fields are validated.
- Vehicle starts pending review unless policy says otherwise.
- Vehicle approval is auditable.

### US-02 - Admin approves vehicle/service eligibility

As an admin, I want to approve which services a driver can provide with a vehicle.

Acceptance criteria:

- Admin can enable Ride/Food eligibility separately.
- Admin can restrict eligibility by region.
- Approved eligibility is used by matching.
- Changes write audit log.

### US-03 - Matching filters ineligible driver

As the system, I need to exclude drivers who are not eligible for the requested service/vehicle/region.

Acceptance criteria:

- Driver must be active.
- Driver must be online.
- Driver must not be locked/suspended/blocked.
- Driver vehicle/service/region eligibility must match request.

## 5. Acceptance Tests

- Given driver has motorcycle eligible for Food only, when Ride car request is matched, then driver is excluded.
- Given admin disables Food eligibility, when driver is online, then Food offers stop.
- Given region pauses car Ride, when matching searches car drivers there, then all car offers are blocked.
- Given driver adds unapproved vehicle, when going online for that vehicle, then app blocks.

## 6. Data Requirements

- Driver profile ID.
- Vehicle type.
- Vehicle identifiers and description fields.
- Service eligibility flags.
- Region eligibility.
- Verification status.
- Admin decision and reason.
- Audit history.

## 7. Open Questions

- Exact vehicle fields and document attachments.
- Whether driver can have multiple vehicles.
- Whether a driver can switch active vehicle during the day.

