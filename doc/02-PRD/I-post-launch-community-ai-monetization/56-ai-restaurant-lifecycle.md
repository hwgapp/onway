# PRD: AI Restaurant Lifecycle

**Phase:** P2  
**Status:** Draft  
**Platforms:** API Core Backend, Admin Portal  

## 1. Objective

Define future AI-assisted restaurant lifecycle operations for stale data detection, menu changes, duplicate/closure detection, mission generation, and admin review.

## 2. MVP Position

Not required for P0 launch. P0 restaurant lifecycle is admin-created and admin-maintained.

## 3. Future Scope

- Brand/outlet recognition support.
- OCR/menu extraction.
- Stale menu detection.
- Price anomaly detection.
- Closure/location anomaly detection.
- Mission generation.
- Confidence scoring.
- Admin exception queue.

## 4. User Stories

### US-01 - AI flags stale menu

As operations, I want AI to identify menus needing reverification.

Acceptance criteria:

- Stale threshold is configurable.
- AI creates review/mission suggestion.
- Published menu is not changed automatically without policy.

### US-02 - AI detects price anomaly

As admin, I want suspicious price changes flagged before publish.

Acceptance criteria:

- Anomaly thresholds are configurable.
- High-risk anomaly requires human review.
- Evidence and confidence are visible.

### US-03 - AI suggests outlet closure/duplicate

As operations, I want AI to detect duplicate or closed outlets.

Acceptance criteria:

- Suggestion enters review queue.
- Admin confirms/rejects.
- Confirmed closure/duplicate action is audited.

## 5. Acceptance Tests

- Given menu age exceeds configured threshold, when lifecycle job runs, then reverification suggestion is created.
- Given price change over high-risk threshold, then auto-publish is blocked.
- Given AI suggests closure, when admin rejects, then outlet remains active and decision is recorded.

## 6. Open Questions

- AI provider/model.
- Confidence thresholds.
- Which lifecycle actions can be automated.

