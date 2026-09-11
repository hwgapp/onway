# PRD: Advertising & Sponsored Placement

**Phase:** P2  
**Status:** Draft  
**Platforms:** Customer App, Driver App, Admin Portal, API Core Backend, Landing Web  

## 1. Objective

Reserve future advertising and sponsored placement model after Onway has enough traffic and core marketplace quality.

## 2. MVP Position

Advertising is not in launch MVP. It should not block Ride, Food, Admin, Driver, or Customer core flows.

## 3. Future Scope

Potential formats:

- Sponsored restaurant.
- Sponsored brand.
- Sponsored search result.
- Sponsored mission.
- Driver-facing ads.
- Contextual ads.

## 4. Product Principles

- Sponsored content must be labeled.
- Ads must not affect Trust, Community Truth, Verification Confidence, fraud decisions, or organic rating.
- Ads must not hide safety/payment/dispute information.
- Ads should not make operational UI noisy.

## 5. User Stories

### US-01 - Admin creates sponsored placement

As admin, I want to create sponsored placements after advertising is enabled.

Acceptance criteria:

- Placement has advertiser/brand, format, region, start/end, budget placeholder, status.
- Sponsored label is required.
- Changes are audited.

### US-02 - Customer sees labeled sponsored content

As customer, I want to distinguish sponsored content from organic results.

Acceptance criteria:

- Sponsored placement is clearly labeled.
- Organic ranking and paid placement are separable in data.
- Customer can still access normal discovery.

### US-03 - Ads do not influence trust/fraud/catalog truth

As Onway, I need monetization not to corrupt marketplace integrity.

Acceptance criteria:

- Ad records are separate from rating/trust/community truth.
- Sponsored status cannot modify verification confidence.
- Fraud/admin decision workflows ignore ad spend.

## 6. Acceptance Tests

- Given sponsored restaurant appears, when customer views listing, then sponsored label is visible.
- Given brand buys ad, when Community Truth confidence is calculated, then ad status is ignored.
- Given ad expires, when discovery refreshes, then sponsored placement stops showing.

## 7. Open Questions

- Advertising pricing model.
- Sales/admin workflow.
- Legal labeling requirements.

