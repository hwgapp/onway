# PRD: Ride Rating

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, API Core Backend, Admin Portal  

## 1. Objective

Allow customer and driver to rate each other after completed Ride to support quality monitoring and future Trust/risk models.

## 2. Scope

In scope:

- Post-ride customer rating for driver.
- Post-ride driver rating for customer.
- Optional tags/comment.
- Rating visibility rules.
- Admin review access.

Out of scope:

- Public detailed reviews.
- Trust scoring automation.
- Rating-based incentives.

## 3. Rating Model

Suggested fields:

- Entity: ride ID.
- Rater actor.
- Rated actor.
- Star score or simple sentiment.
- Tags.
- Comment optional.
- Created timestamp.
- Visibility/admin status.

## 4. User Stories

### US-01 - Customer rates driver

As a customer, I want to rate my ride experience after completion.

Acceptance criteria:

- Rating is available only after eligible completed ride.
- Customer can submit once per ride.
- Low rating can offer complaint/report path.

### US-02 - Driver rates customer

As a driver, I want to rate customer behavior after ride.

Acceptance criteria:

- Driver can submit once per ride.
- Rating is tied to completed ride.
- Rating does not automatically lock customer in P0.

### US-03 - Admin reviews ratings

As admin, I want ratings to appear in ride history and driver/customer profile.

Acceptance criteria:

- Admin can view rating history.
- Ratings are filterable by low score/tag.
- Ratings can link to complaint if one exists.

## 5. Acceptance Tests

- Given ride is not completed, when customer tries to rate, then API rejects.
- Given customer already rated, when submitting again, then API rejects or updates only if policy allows.
- Given low rating with complaint tag, when submitted, then app offers complaint flow.
- Given admin opens driver profile, then related ride ratings are visible.

## 6. Open Questions

- Star scale vs thumbs up/down.
- Required tags for low ratings.
- Whether ratings are shown to the other party.

