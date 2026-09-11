# PRD: AI Operations & Decision Governance

**Phase:** P1  
**Status:** Draft  
**Platforms:** API Core Backend, Admin Portal  

## 1. Objective

Define how AI Operations will support Onway after MVP core launch while preserving human control for high-risk decisions.

## 2. MVP Position

AI Operations is aligned with Onway strategy but is not a launch blocker for P0. P0 can use manual/admin workflows and deterministic policy configs first.

## 3. Future Scope

AI may support:

- Complaint triage.
- Fraud signal summarization.
- Evidence quality checks.
- Menu extraction and normalization.
- Restaurant lifecycle monitoring.
- Mission generation.
- Anomaly detection.
- Suggested admin decisions.

## 4. Governance Model

Risk levels:

- Low: AI may auto-handle when policy allows.
- Medium: AI may auto-handle with audit trail or suggest default action.
- High: AI suggests; human approves.

High-risk examples:

- Permanent driver ban.
- Financial responsibility decision.
- Fraud finalized decision.
- Sensitive identity/document decisions.

## 5. User Stories

### US-01 - Operator receives AI summary

As an operator, I want AI to summarize a complaint case so I can decide faster.

Acceptance criteria:

- Summary cites linked evidence/timeline references.
- AI recommendation is clearly labeled as suggestion.
- Operator final decision is stored separately from AI suggestion.

### US-02 - AI action is auditable

As an auditor, I want to know when AI influenced a decision.

Acceptance criteria:

- AI output stores model/provider/version where available.
- Input references and generated recommendation are linked to case.
- Human override is recorded.

### US-03 - Admin configures AI guardrails

As admin, I want to configure which AI actions are allowed.

Acceptance criteria:

- AI automation can be enabled/disabled by module/action.
- High-risk actions require human approval.
- Policy changes are audited.

## 6. Acceptance Tests

- Given AI suggests permanent ban, when no human approves, then account is not permanently banned.
- Given AI auto-rejects blurry evidence in future workflow, when action runs, then audit entry records reason.
- Given AI provider fails, when complaint review opens, then manual review still works.

## 7. Open Questions

- AI provider/model choices.
- Data privacy review for AI processing.
- Which actions are allowed in P1 vs P2.

