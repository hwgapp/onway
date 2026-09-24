# Acceptance Criteria

## Product-Level AC

- AC-PROD-001: P0 supports Customer Ride/Food, Driver Ride/Food and Admin operations without requiring wallet, cash, COD, payment gateway, escrow or Onway-held Ride/Food payment.
- AC-PROD-002: Ride/Food service requests can only start from active region/service/vehicle policy; destination outside region is allowed only when policy/pricing/matching guardrails permit it.
- AC-PROD-003: All direct bank transfer/QR payment flows store user-confirmed state, payment proof/evidence and audit trail; UI must not present proof as official bank confirmation.
- AC-PROD-003A: Fraud/dispute scenarios from direct transfer do not block G3 when covered by minimum complaint/fraud intake, audit, manual review hooks and a clearly marked SOP task before launch.
- AC-PROD-004: Admin Portal can manage region polygon, service/vehicle rollout, pricing/policy config, driver verification, platform fee verification, Food catalog, complaint/fraud/dispute and audit log for P0.
- AC-PROD-005: Sensitive admin actions require reason and audit trail, including policy changes, driver activation/deactivation, manual lock/risk status changes, fraud decisions and sensitive evidence/KYC access.
- AC-PROD-006: P0 supports manual/admin lock and conservative rule-based auto-lock; every lock requires reason/audit and auto-lock must enter a human review/unlock/override queue.
- AC-PROD-007: Customer-driver chat is available only for active Ride/Food participants, supports text/image, and uses 1-week retention unless preserved for complaint/dispute.
- AC-PROD-007A: P0 push notifications cover job, payment, chat and lock events; marketing push is excluded.
- AC-PROD-008: Device id/fingerprint collection is limited to fraud/risk purpose, uses minimized/pseudonymous signals where possible and follows retention draft pending legal review.
- AC-PROD-009: Flutter clients use generated typed GraphQL client/models from schema/query documents after scaffold; React Admin should use typed GraphQL codegen unless tooling blocks it.
- AC-PROD-010: Core flows have documented tests/QA before release: Ride, Food, Driver onboarding/platform fee, Region policy, Complaint/Fraud, Chat, Realtime location/matching.

## Feature-Level AC

| Feature | AC | Notes |
| --- | --- | --- |
| Ride request | Customer can create request with pickup/dropoff/vehicle type and see Recommended/final platform price. | P0 has no customer manual offer/price negotiation |
| Ride matching | Matching sends driver offers by wave; driver sees platform final price; first valid accept wins; one driver has one active offer. | Wave values configurable; driver no Counter Offer |
| Ride payment proof | Customer can complete bank transfer/QR and upload proof before driver arrives; driver confirms received money before going/continuing to pickup; system stores proof state/evidence/audit. | Direct payment only; proof is evidence, not bank confirmation; fraud details handled by SOP/manual review |
| Ride payment dispute | If driver does not confirm received money, service can enter `Payment disputed`; if amount is missing/incorrect, app prioritizes supplemental payment before dispute escalation. | SOP/manual review handles fraud detail |
| Ride completion | Completed ride stores lifecycle state, final price, payment proof state/evidence if required and audit. | Direct payment only |
| Food checkout | Customer sees item estimate, Recommended Delivery Fee and total amount to transfer to driver before confirming. | No Food fee negotiation; no tip P0 |
| Food direct payment | After driver matched, customer can upload payment proof and driver can confirm money received. | Driver orders food only after confirmation unless policy override; fraud details handled by SOP/manual review |
| Food order-at-outlet | Driver can mark ordered-at-outlet; after this customer cannot cancel for refund if merely changing mind. | Fault-based dispute policy applies |
| Food change proposal | Driver can propose item/price/status change in app; app proposal is source of truth; customer must Accept/Reject before affected purchase; timeout default is 5 minutes configurable. | Proposal does not update shared menu automatically; if price increases, customer must transfer supplemental amount before purchase |
| Driver onboarding | Driver cannot receive jobs until phone, identity/documents, vehicle/service eligibility and platform fee policy are satisfied. | Background/legal checks pending legal/Ops policy |
| Platform fee verification | Driver can submit proof/reference; Finance Ops/Admin can verify manually and audit action. | Onway revenue only |
| Region admin | Admin can create/draw/edit/pause/resume/publish polygon and publish lifecycle/service/vehicle config; no hard delete P0; overlap is blocked for same service/vehicle. | HCM polygons are operational config created through Admin tool before rollout; destination outside polygon has customer/driver warning |
| Catalog admin | Catalog Manager/Admin can manage Brand/Outlet/Canonical Menu/Outlet Override. | P0 admin-first Food supply |
| Complaint/dispute | User can submit complaint; admin can review, collect evidence and finalize manual decision. | Complaint does not equal fraud |
| Fraud/risk | Risk/Fraud Analyst can update risk status/manual lock with reason/audit; auto-lock can temporarily lock driver from paid/no-show, severe safety/fraud, 3 valid complaints/30 days or repeated payment dispute and requires human review. | Lock lasts until admin handles; SLA target 24h; short reason notification; in-app appeal; unlock by Super Admin/Risk-Fraud |
| Chat | Active participants can send text/image; unauthorized users cannot access room/history. | Retention 1 week; 1 image per message in P0 |
| Rating | Completed Ride/Food can collect 5-star rating plus quick tags, separate from complaint/report. | Rating is not fraud decision |
| RBAC | Each Admin Portal action follows permission matrix. | Role set accepted for P0 |
| Analytics | Critical events are emitted for auth, Ride, Food, onboarding, payment proof, complaint/fraud, region/policy, chat, push, rating and auto-lock; Admin has basic ops dashboard. | Avoid unnecessary sensitive raw data; no complex real-time BI P0 |
