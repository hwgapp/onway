# PRD: AI Menu Extraction & Normalization

**Phase:** P2  
**Status:** Draft  
**Platforms:** Admin Portal, API Core Backend  

## 1. Objective

Define future AI-assisted menu extraction and normalization to reduce manual catalog work after MVP launch.

## 2. MVP Position

This is not a launch blocker. P0 Food catalog is admin-first manual setup. Drivers do not capture menu data in MVP.

## 3. Future Scope

AI may support:

- OCR from menu images.
- Item/category extraction.
- Price extraction.
- Modifier detection.
- Duplicate item detection.
- Normalization across outlets.
- Confidence scoring.
- Human review queue.

## 4. User Stories

### US-01 - Admin uploads menu image for AI extraction

As admin, I want to upload a menu image and receive structured draft items to review.

Acceptance criteria:

- AI output is draft, not auto-published.
- Extracted fields include confidence.
- Original image remains linked as evidence.

### US-02 - Admin reviews AI output

As admin, I want to approve/edit/reject extracted items before catalog publish.

Acceptance criteria:

- Admin can compare image to extracted structured data.
- Low-confidence fields are highlighted.
- Approved data enters normal catalog workflow.

### US-03 - System detects likely menu changes

As operations, I want AI to flag stale or changed menus so admin/community verification can follow up.

Acceptance criteria:

- AI can create review suggestions.
- Suggestions do not mutate published catalog automatically unless future policy allows.
- Actions are auditable.

## 5. Acceptance Tests

- Given AI extracts wrong price, when admin rejects field, then rejected value is not published.
- Given extraction confidence is low, when review queue displays item, then item is highlighted.
- Given AI service fails, when admin uploads image, then manual catalog workflow still works.

## 6. Open Questions

- AI provider/model.
- Supported file/image types.
- Confidence thresholds.
- Whether driver-captured menu images feed the same workflow in P2.

