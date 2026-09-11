# PRD: Restaurant Mission Capture

**Phase:** P2  
**Status:** Draft  
**Platforms:** Driver App, API Core Backend, Admin Portal  

## 1. Objective

Define future driver capture flow for restaurant/outlet/menu evidence using in-app camera, GPS, timestamp, and device metadata.

## 2. MVP Position

Not part of P0. Drivers do not capture or update restaurant/menu data for launch MVP.

## 3. Future Scope

- In-app camera capture.
- No gallery upload for mission evidence.
- GPS/timestamp/device metadata.
- Full menu capture.
- Outlet photo capture.
- Evidence quality validation.
- Submission review.

## 4. User Stories

### US-01 - Driver captures outlet evidence

As a driver, I want to capture required outlet photos for mission.

Acceptance criteria:

- Camera opens inside Driver App.
- GPS/timestamp/device metadata attach to evidence.
- Gallery upload is blocked for mission verification evidence.

### US-02 - Driver captures full menu

As a driver, I want to capture all menu pages/boards needed for verification.

Acceptance criteria:

- Mission requires a full menu evidence set.
- Driver can review captured images before submit.
- Missing required sections block submission.

### US-03 - System checks evidence quality

As Onway, I want low-quality evidence rejected before review.

Acceptance criteria:

- Blur/glare/crop/duplicate checks may flag image.
- Driver can retake while at outlet.
- Failed checks are recorded.

## 5. Acceptance Tests

- Given driver tries gallery image, when mission requires live capture, then app blocks.
- Given photo lacks GPS or is far from outlet, when submitted, then review flags/rejects according to policy.
- Given image is blurry, when quality check runs, then retake is requested.

## 6. Open Questions

- Quality thresholds.
- Offline capture support.
- Required outlet photo checklist.

