# ONWAY - Business/Application Logic P0

**Loai tai lieu:** Business/Application Logic Spec / Technical PRD input  
**Phien ban:** 0.1  
**Trang thai:** Draft  
**Ngay cap nhat:** 11/09/2026  
**Pham vi:** P0 launch logic cho API Core Backend, Customer App, Driver App, Web Admin Portal  

---

# 1. Muc tieu

Tai lieu nay mo ta logic P0 de implement Onway MVP:

- Backend service ownership.
- Business validation.
- State machine.
- Transaction boundary.
- Audit/timeline event.
- Realtime/notification side effects.
- Edge cases.
- Technical test cases.

Tai lieu nay di sau PRD va DB schema:

- PRD tra loi "can lam gi".
- DB schema tra loi "luu cai gi".
- Logic spec tra loi "xu ly nhu the nao".

# 2. Nguyen tac logic P0

## 2.1 Backend la source of truth

Client khong duoc tu quyet dinh business rule.

- Customer App/Driver App/Admin Portal chi goi API va render `allowed_actions`.
- Backend enforce state transition, permission, region, payment proof, driver lock, eligibility.
- Moi critical mutation phai co idempotency key neu co nguy co retry.

## 2.2 State transition phai explicit

Khong update status truc tiep tu client payload.

Moi transition can:

1. Load entity hien tai.
2. Verify actor permission.
3. Verify current state.
4. Verify preconditions.
5. Mutate state trong transaction.
6. Write domain state event.
7. Write audit log neu critical.
8. Commit.
9. Emit realtime/notification sau commit.

## 2.3 Money-light

Ride/Food payment:

- Chi co bank transfer/QR truc tiep customer -> driver.
- Khong COD.
- Khong cash.
- Khong payment gateway.
- Khong wallet/escrow.
- Payment proof la bat buoc trong flow can thanh toan.
- Payment proof la bang chung, khong phai xac minh ngan hang tu dong.

## 2.4 Trust logic tam bo qua

P0 khong dung Trust Engine day du.

- Khong COD.
- Khong Food delivery fee negotiation.
- Ride price negotiation khong default P0.
- P0 chi dung account status, driver risk status, eligibility va policy config.

## 2.5 Audit before cleverness

Neu co tranh chap, Onway phai co the tra loi:

- Ai lam gi?
- Luc nao?
- Tren entity nao?
- Tu status nao sang status nao?
- Dua tren evidence nao?
- Admin/system quyet dinh vi sao?

# 3. Service/module ownership

| Module | Owns |
|---|---|
| `identity` | Firebase token verify, account/profile mapping, session actor context. |
| `rbac` / `admin` | Admin permissions, role checks. |
| `region` | Country/city/region, polygon containment, service/vehicle availability. |
| `policy-config` | Business values, thresholds, feature flags, config lookup. |
| `driver` | Driver profile, onboarding status, vehicle, eligibility, payment accounts, risk status. |
| `platform-fee` | Driver platform fee proof, manual verification, subscription period, refund records. |
| `restaurant` | Brand/outlet data. |
| `menu` | Menu versions, categories, items, modifiers, outlet overrides, effective catalog. |
| `ride` | Ride request, lifecycle, price snapshot, completion/cancellation. |
| `food-order` | Food cart/order lifecycle, item snapshots, purchase/delivery states. |
| `pricing` | Ride recommended price, Food delivery fee, waiting policy calculation hooks. |
| `matching` | Matching session, candidate filtering/ranking, offers, assignment. |
| `direct-payment` | Payment records, proof upload, receipt confirmation/dispute. |
| `chat` | Chat room, messages, images, retention markers. |
| `media-evidence` | Upload intent, media metadata, evidence linking. |
| `complaint` | Complaint intake, evidence, response, resolution. |
| `risk` | Driver auto-lock/manual lock/unlock, matching exclusion. |
| `fraud` | Fraud case workflow and linkage. |
| `rating` | Customer/driver ratings. |
| `notification` | Outbox and push/in-app dispatch coordination. |
| `audit-log` | Append-only audit writing and query. |

# 4. Common command pattern

MVP mutations should follow this pattern:

```txt
handleCommand(actor, input, idempotencyKey):
  authorize actor
  validate input shape
  begin transaction
    load entity FOR UPDATE if state changes
    validate current state
    validate business preconditions
    apply state/data changes
    insert state event
    insert audit log if critical
    insert outbox notification if needed
  commit
  emit realtime event or let outbox worker dispatch
  return updated entity + allowed_actions
```

## 4.1 Idempotency

Require idempotency key for:

- Creating Ride request.
- Confirming Food order.
- Driver accepting offer.
- Uploading payment proof finalization.
- Driver confirming payment.
- Submitting complaint.
- Lock/unlock driver.
- Publishing catalog.

Suggested idempotency behavior:

- Store command result hash in future `idempotency_keys` table if needed.
- For v0.1, service can use unique constraints plus safe retry checks.

## 4.2 Error model

API errors should be typed:

| Code | Meaning |
|---|---|
| `UNAUTHENTICATED` | Missing/invalid auth. |
| `FORBIDDEN` | Actor lacks permission. |
| `INVALID_STATE` | Entity current state does not allow action. |
| `POLICY_BLOCKED` | Policy config blocks action. |
| `REGION_UNAVAILABLE` | Region/service/vehicle invalid. |
| `DRIVER_NOT_ELIGIBLE` | Driver cannot receive/perform job. |
| `PAYMENT_PROOF_REQUIRED` | Required proof missing. |
| `PAYMENT_UNDER_REVIEW` | Payment disputed/review needed. |
| `OFFER_EXPIRED` | Matching offer expired. |
| `ALREADY_ASSIGNED` | Another driver won assignment. |
| `CATALOG_UNAVAILABLE` | Food catalog/outlet/item not orderable. |
| `VALIDATION_ERROR` | Input invalid. |
| `RATE_LIMITED` | Abuse/control limit. |

# 5. Actor authorization rules

## 5.1 Customer

Can:

- Read own profile.
- Create own Ride/Food requests.
- Upload payment proof for own assigned ride/order.
- Join own assigned ride/order chat room.
- Submit complaint for own ride/order.
- Rate own completed ride/order counterpart.

Cannot:

- Access other customer/driver private data beyond assigned job display snapshot.
- Upload payment proof for unrelated ride/order.
- Mutate driver/order state directly.

## 5.2 Driver

Can:

- Read own driver profile/onboarding/eligibility.
- Submit onboarding and platform fee proof.
- Manage own payment account subject to review policy.
- Go online if active/eligible/not locked.
- Accept/reject offers sent to self.
- Mutate assigned job states.
- Join assigned ride/order chat room.
- Confirm payment received or report not received.
- Respond to complaint where involved.

Cannot:

- Receive offers while inactive/locked/suspended/blocked.
- Start Food purchase before required payment proof state.
- Modify restaurant/menu catalog in P0.
- Access unrelated payment proof/chat.

## 5.3 Admin/operator

Can only act according to RBAC:

- Configure region/policy.
- Review driver onboarding/platform fee.
- Manage Food catalog.
- Monitor Ride/Food.
- View evidence needed for authorized case.
- Lock/unlock driver.
- Resolve complaints/fraud cases.

All risk, publish, verification and config mutations require reason and audit log.

# 6. Identity, Auth & Account logic

## 6.1 `getOrCreateAccountFromFirebase`

Input:

- Firebase ID token.
- Optional intended role: customer/driver/admin.

Logic:

1. Verify Firebase ID token.
2. Extract Firebase UID and phone.
3. Find account by Firebase UID.
4. If not found, find by phone.
5. If not found, create account with status `active` or `pending_verification` depending policy.
6. Ensure requested role profile exists if allowed.
7. Return actor context.

Validation:

- Phone must be verified for customer/driver P0.
- Admin profile cannot auto-create from public app.

Side effects:

- Update `last_login_at`.
- Write account status event only when status changes.

Tests:

- New phone creates account + customer profile.
- Existing Firebase UID returns same account.
- Same phone with different Firebase UID is blocked or linked only by explicit policy.
- Non-admin account cannot access admin portal.

## 6.2 Account status enforcement

Before every command:

- `blocked`: no service actions except support/legal allowed.
- `suspended`: cannot create/receive jobs.
- `locked`: driver cannot receive jobs; customer behavior depends status.
- `under_review`: allow only configured safe actions.

Return `allowed_actions` so clients render correctly.

# 7. Region, Currency & Availability logic

## 7.1 Resolve active region

Input:

- Coordinate.
- Service type: `ride` or `food`.
- Optional vehicle type.

Logic:

1. Query active/pilot regions whose `boundary` contains coordinate.
2. If multiple match, choose by priority policy or reject until overlap policy exists.
3. Verify `region_service_configs.status = enabled`.
4. If vehicle type provided, verify `region_vehicle_configs.status = enabled`.
5. Return region ID, city, country, currency, timezone, enabled services.

PostGIS:

```sql
ST_Contains(regions.boundary, ST_SetSRID(ST_Point(lng, lat), 4326))
```

Tests:

- Outside polygon returns unavailable.
- Paused region rejects service.
- Food enabled but Ride disabled only allows Food.
- Currency comes from region, not global hard-code.

## 7.2 Validate route/service coordinates

Ride:

- Pickup must be in active Ride region.
- Dropoff rule is open decision. Until chot, safest P0: require dropoff in same active region unless policy config allows outside dropoff.

Food:

- Outlet must be in active Food region.
- Delivery address must be in active Food region.
- Region/currency snapshot must be saved on order.

# 8. Policy Config logic

## 8.1 Get effective config

Input:

- Key.
- Context: global/country/city/region/service/brand/outlet.

Logic:

1. Load active configs matching key and scope chain.
2. Choose most specific scope.
3. Validate type.
4. Return value + config version.

Specificity:

`outlet > brand > region > city > country > global`.

Use for:

- Matching batch size/timeout/radius.
- Chat retention.
- Payment proof required before event.
- Driver auto-lock threshold.
- Food waiting policy.
- Media upload limits.

## 8.2 Admin update config

Logic:

1. Authorize admin permission.
2. Validate key is editable.
3. Validate type/range.
4. Create new version or update active record according to config strategy.
5. Insert `policy_config_events`.
6. Insert audit log.
7. Invalidate config cache.

Tests:

- Invalid value rejected.
- Unauthorized admin rejected.
- New config applies to future commands.
- Historical decisions retain policy version where needed.

# 9. Media & Evidence logic

## 9.1 Create upload intent

Input:

- Purpose: payment proof, chat image, driver document, catalog image, complaint evidence, platform fee proof.
- MIME type, size.
- Linked entity optional.

Logic:

1. Authorize actor and purpose.
2. Validate MIME/size against policy.
3. Create object key.
4. Return signed upload URL or upload token.
5. After upload complete, create `media_objects` row.

Tests:

- Customer cannot create driver document upload.
- Unsupported MIME rejected.
- Oversized image rejected.

## 9.2 Attach evidence

Logic:

1. Verify media belongs to actor or actor has admin permission.
2. Verify target entity access.
3. Insert evidence link or proof row.
4. Write timeline/audit if target is critical.

Payment proof is always linked through `payment_proofs`, not free-floating media only.

# 10. Driver onboarding logic

## 10.1 Driver onboarding progression

Allowed transitions:

| From | Action | To | Actor |
|---|---|---|---|
| none/draft | create driver profile | `draft` | driver |
| `draft` | phone verified | `phone_verified` | system |
| `phone_verified` | submit profile | `profile_submitted` | driver |
| `profile_submitted` | require docs | `documents_required` | system/admin |
| `documents_required` | submit docs | `documents_submitted` | driver |
| `documents_submitted` | send review | `admin_review` | system |
| `admin_review` | request changes | `changes_requested` | admin |
| `changes_requested` | resubmit | `admin_review` | driver |
| `admin_review` | approve | `approved_pending_platform_fee` | admin |
| `admin_review` | reject | `rejected` | admin |
| `approved_pending_platform_fee` | fee approved | `activated` | system/admin |

Activation requires:

- Account not blocked/suspended.
- Onboarding approved.
- Required vehicle approved.
- Service eligibility exists.
- Platform fee approved or waived.
- Driver payment account active if direct payment jobs require it.

Tests:

- Driver cannot skip documents_required if policy requires docs.
- Admin approval without platform fee does not activate.
- Activation creates status event/audit.

## 10.2 Admin review

Admin actions:

- Approve.
- Reject.
- Request changes.

Validation:

- Reason required for reject/request changes.
- Admin must have driver review permission.
- Decision cannot be made on stale version if optimistic lock/version used.

Side effects:

- Notify driver.
- Write audit log.

# 11. Driver platform fee logic

## 11.1 Submit platform fee proof

Driver flow:

1. Driver views fee instruction.
2. Driver transfers to Onway bank/QR externally.
3. Driver uploads proof and optional reference.
4. Backend creates `driver_platform_fee_payments` status `submitted`.
5. Admin queue receives item.

Validation:

- Proof media required.
- Amount expected from policy.
- Driver must be in allowed onboarding state.

## 11.2 Admin verifies platform fee

Approve logic:

1. Authorize admin.
2. Load payment row FOR UPDATE.
3. Verify status `submitted`.
4. Set `approved`.
5. If driver onboarding/vehicle/eligibility complete, activate driver.
6. Create subscription periods:
   - paid: 12 months from activation.
   - bonus: 6 months after paid period.
7. Audit decision.
8. Notify driver.

Reject logic:

- Set `rejected` or `resubmission_required`.
- Reason required.
- Notify driver.

Tests:

- Double approval is idempotent or rejected safely.
- Rejected proof cannot activate.
- Subscription periods are created once.

## 11.3 Refund calculation

Input:

- Driver profile.
- Activation date.
- Stop date.

Logic:

- Paid 12 months split into four 3-month periods.
- If stop occurs inside a paid quarter, that quarter is considered used.
- Only not-yet-started paid quarters refundable.
- Bonus months refund value = 0.

# 12. Driver payment account logic

Driver bank/QR account is needed so customer can transfer directly.

Create/update logic:

1. Driver submits bank name/code/account holder/account number/QR.
2. Status starts `pending_review` unless policy allows self-activation.
3. Admin approves/rejects.
4. Only active default payment account is used in payment instruction snapshots.

Validation:

- Active driver must have active default payment account before receiving Ride/Food jobs where customer pays driver.
- Account number should be encrypted or tokenized.

Tests:

- Driver with no active payment account excluded from matching.
- Payment instruction snapshot remains stable even if driver later edits bank account.

# 13. Driver online/offline and presence logic

## 13.1 Go online

Preconditions:

- Driver profile activation `active`.
- Risk status `clear` or allowed.
- Not suspended/blocked.
- Has active vehicle.
- Has service eligibility.
- Has active payment account.
- Location permission available.
- Current coordinate inside active region.

Logic:

1. Validate driver.
2. Validate region/service/vehicle.
3. Set presence in Redis:
   - driver id;
   - location;
   - vehicle;
   - service flags;
   - last seen;
   - availability `online_available`.
4. Optionally persist location snapshot for audit rules.
5. Emit `presence.driver_online`.

## 13.2 Location update

Logic:

1. Authenticate WebSocket.
2. Verify driver can remain online.
3. Validate coordinate sanity and accuracy.
4. Update Redis presence TTL.
5. If on active job, broadcast location to job room and persist snapshots at policy interval.

Edge cases:

- GPS accuracy too low: keep last good location or mark degraded.
- Driver exits region: stop new offers; active job handling follows ride/order policy.
- WebSocket disconnect: presence expires after TTL.

## 13.3 Force offline

Triggered by:

- Admin lock/suspend.
- Auto-lock.
- Account blocked.
- Region paused.
- Presence stale.

Side effects:

- Remove/update Redis presence.
- Emit event to Driver App.
- Matching excludes driver.

# 14. Food catalog admin-first logic

## 14.1 Brand create/update

Logic:

1. Admin permission `catalog.brand.write`.
2. Validate name/slug.
3. Warn on duplicate/similar names.
4. Create/update brand.
5. Audit.

Brand active is required for published customer-visible outlet.

## 14.2 Outlet create/update

Validation:

- Brand exists and not archived.
- Region exists.
- Address and location required before active/publish.
- Location must be inside region boundary.
- Opening hours required before customer-visible.

State logic:

- Draft outlet can be incomplete.
- Active outlet must pass validation.
- Paused/closed outlet cannot accept new Food orders.

## 14.3 Menu version editing

Logic:

1. Admin edits draft menu version.
2. Add categories, items, modifiers.
3. Validate prices, required modifiers, currency.
4. Published menu version should not be mutated destructively; create new version for material changes if needed.

Cart/order must snapshot item data so later catalog changes do not rewrite historical orders.

## 14.4 Effective menu calculation

Input:

- Outlet ID.

Logic:

1. Load active `outlet_menu_versions`.
2. Load published `menu_version`.
3. Load categories/items/modifiers.
4. Apply `outlet_item_overrides`.
5. Apply `outlet_modifier_option_overrides`.
6. Filter hidden/unavailable according to customer display policy.
7. Return effective menu with item/modifier availability and prices.

Tests:

- Outlet override price wins over canonical item price.
- Unavailable item cannot be added to cart.
- Modifier min/max enforced.

## 14.5 Catalog publishing

Allowed transitions:

| From | Action | To |
|---|---|---|
| `draft` | submit review | `pending_review` |
| `pending_review` | publish | `published` |
| `published` | mark stale | `needs_reverification` |
| `published` | unpublish | `unpublished` |
| any non-active | archive | `archived` |

Publish preconditions:

- Brand active.
- Outlet active and region valid.
- Food service enabled in region.
- Menu has at least one active category and one active item.
- Prices valid and currency compatible.
- Required modifiers have options.

Side effects:

- Customer discovery cache invalidation.
- Audit/publish event.

# 15. Ride request and pricing logic

## 15.1 Create ride draft/quote

Input:

- Pickup coordinate/address.
- Dropoff coordinate/address.
- Vehicle type.

Logic:

1. Authenticate customer.
2. Validate customer status allows ride.
3. Resolve pickup region.
4. Validate Ride enabled and vehicle type enabled.
5. Validate dropoff rule.
6. Get route distance/ETA from maps/routing provider or fallback.
7. Calculate recommended price from pricing policy.
8. Snapshot region/currency/route/price.
9. Return quote and allowed actions.

## 15.2 Confirm ride request

Transaction:

1. Load quote/draft if persisted, or validate request payload.
2. Revalidate region/service/vehicle.
3. Recalculate or verify quote not expired.
4. Create/update ride status `matching`.
5. Insert ride state event.
6. Create matching session.
7. Commit.
8. Start matching job/event.

Tests:

- Stale quote rejected.
- Disabled region rejects at confirm even if quote was valid earlier.
- Vehicle disabled rejects.

# 16. Matching logic

## 16.1 Candidate filtering

For Ride:

- Driver active.
- Driver risk status not locked/suspended/blocked.
- Online presence exists in Redis.
- Vehicle type matches.
- Service eligibility for Ride in region.
- Active payment account exists.
- Driver not on incompatible job.
- Distance/radius policy satisfied.

For Food:

- Same base checks.
- Food service eligibility.
- Candidate location/radius relative to outlet and/or delivery route by policy.

## 16.2 Ranking

Initial ranking inputs:

- ETA/distance to pickup/outlet.
- Driver availability state.
- Vehicle match.
- Region match.
- Basic operational signals if available.

Do not require Trust Engine P0.

## 16.3 Progressive batched matching

Algorithm:

```txt
startMatching(session):
  while session active and batch <= max:
    candidates = filterAndRank(radius)
    offers = first N candidates not previously offered
    if offers empty:
      expand radius or end no_driver_available
    create offers with expires_at
    emit matching.offer_sent to drivers
    wait until one accepted or timeout
    if accepted:
      assign atomically
      return assigned
    expire batch
    expand radius
  mark no_driver_available
```

## 16.4 Accept offer transaction

1. Begin transaction.
2. Lock `matching_sessions` row FOR UPDATE.
3. Lock `matching_offers` row.
4. Verify offer is sent and not expired.
5. Verify matching session still not assigned/cancelled.
6. Revalidate driver active/online/not locked/eligible.
7. Set offer accepted.
8. Set session assigned.
9. Set ride/order assigned driver/status.
10. Cancel other offers.
11. Create chat room.
12. For Food, create direct payment record `awaiting_customer_transfer`.
13. For Ride, create direct payment record according to Ride payment timing policy.
14. Commit.
15. Emit assignment events.

Tests:

- Double accept only assigns one.
- Locked driver accept fails.
- Expired offer accept fails.
- Customer cancelled session blocks accept.

# 17. Ride lifecycle logic

## 17.1 Allowed Ride transitions P0

| From | Action | To | Actor |
|---|---|---|---|
| `matching` | driver assigned | `assigned` | system |
| `assigned` | driver starts pickup route | `driver_en_route_to_pickup` | driver/system |
| `driver_en_route_to_pickup` | driver arrived | `driver_arrived` | driver |
| `driver_arrived` | payment precondition satisfied | `ready_to_start` | system/driver |
| `ready_to_start` | start ride | `in_progress` | driver |
| `in_progress` | arrive destination | `arrived_at_destination` | driver |
| `arrived_at_destination` | payment completed if required | `completed` | system/driver |
| active states | cancel | `cancelled` | customer/driver/admin/system |
| any payment issue | dispute | `disputed` | customer/driver/admin/system |

Ride payment timing is open decision. Logic must support payment required before `start_ride` or before `complete_ride`.

## 17.2 Mark driver arrived

Preconditions:

- Ride assigned to driver.
- Current state allows arrival.
- Driver location near pickup or override policy applies.

Side effects:

- State event.
- Customer notification.
- Chat remains active.

## 17.3 Start ride

Preconditions:

- Driver assigned.
- State `driver_arrived` or `ready_to_start`.
- Payment precondition satisfied if policy requires pre-start transfer.

Side effects:

- `started_at`.
- Location snapshot.
- Customer realtime update.

## 17.4 Complete ride

Preconditions:

- State `in_progress` or `arrived_at_destination`.
- Driver assigned.
- If payment required at completion, direct payment record must reach required state before final `completed`.

Side effects:

- `completed_at`.
- Rating prompt.
- Chat close timer.
- Notification.

# 18. Ride cancellation/no-show logic

## 18.1 Customer cancels before assignment

Allowed:

- Ride status `matching`.

Logic:

- Set ride `cancelled`.
- Set matching session `cancelled`.
- Cancel offers.
- No payment dispute if no payment proof exists.

## 18.2 Driver cancels after assignment

Logic:

- Require reason.
- Set ride cancelled or rematchable depending policy.
- Notify customer.
- If payment proof exists, may create complaint/dispute prompt.

## 18.3 Customer reports driver no-show

Logic:

1. Verify customer owns ride.
2. Verify ride assigned to driver.
3. Create complaint.
4. If payment proof exists, category can be `paid_but_driver_no_show`.
5. Evaluate auto-lock qualification.

# 19. Food discovery/cart logic

## 19.1 List outlets

Input:

- Customer coordinate/delivery coordinate/region.

Logic:

1. Resolve active Food region.
2. Query active outlets in region.
3. Require brand active, outlet active, active published menu.
4. Apply opening hours/temporary closure.
5. Return outlet cards.

## 19.2 Get effective menu

Use logic in section 14.4.

## 19.3 Cart validation

At every checkout:

- Outlet still active/orderable.
- Menu version still published.
- Items still active/available.
- Required modifiers selected.
- Quantities valid.
- Price recalculated from effective menu.
- If price changed from cart snapshot, customer must review/accept updated total.

Tests:

- Checkout blocks stale unavailable item.
- Checkout recalculates outlet override price.
- Multi-outlet cart rejected unless future policy supports it.

# 20. Food order placement and fee logic

## 20.1 Quote Food order

Input:

- Outlet.
- Cart items/modifiers.
- Delivery address.

Logic:

1. Validate customer status.
2. Validate Food region/outlet/menu/cart.
3. Validate delivery coordinate.
4. Estimate route outlet -> delivery.
5. Calculate delivery fee from pricing policy.
6. Return item total, delivery fee, estimated total, currency.

No customer delivery fee negotiation in P0.

## 20.2 Confirm Food order

Transaction:

1. Revalidate cart and quote.
2. Create `food_orders` status `matching`.
3. Insert `food_order_items` snapshots.
4. Insert `food_order_item_modifiers` snapshots.
5. Insert state event.
6. Create matching session.
7. Commit.
8. Start matching.

Tests:

- Custom delivery fee input rejected.
- Published menu required.
- Cart price change requires review.

# 21. Food matching and payment logic

## 21.1 Food assignment side effects

When driver accepts Food offer:

- Order status -> `assigned`.
- Then -> `awaiting_customer_transfer`.
- Create chat room.
- Create direct payment record:
  - payer customer;
  - payee assigned driver;
  - amount = item total + delivery fee, or policy-defined amount;
  - method `bank_transfer_qr`;
  - required_before_event `food_driver_purchase`;
  - status `awaiting_customer_transfer`;
  - payment instruction snapshot from driver active payment account.

## 21.2 Customer submits Food payment proof

Preconditions:

- Order belongs to customer.
- Order assigned to driver.
- Payment record status `awaiting_customer_transfer` or replace-allowed state.
- Proof media exists and belongs to customer.

Transaction:

1. Insert `payment_proofs`.
2. Update direct payment record `proof_submitted`.
3. Update food order `payment_proof_submitted`.
4. Set `payment_proof_submitted_at`.
5. Insert payment/order state events.
6. Commit.
7. Notify driver.

## 21.3 Driver confirms receipt

Preconditions:

- Driver assigned to order.
- Payment record status `proof_submitted`.

Logic:

- If received: status `driver_confirmed_received`; order `driver_confirmed_payment`.
- If not received: status `driver_reported_not_received`; order may enter `disputed` or `admin_review_required`.
- Write timeline/audit.

Policy:

- Driver restaurant purchase can start at `proof_submitted` or `driver_confirmed_received` depending config. Recommended safer P0: require at least `proof_submitted`; driver can report not received before purchase if needed.

# 22. Driver restaurant purchase logic

## 22.1 Start to outlet / arrived

Preconditions:

- Food order assigned to driver.
- Required payment proof state met.
- Driver not blocked from continuing active job.

Transitions:

- `driver_confirmed_payment` or `payment_proof_submitted` -> `driver_en_route_to_outlet`.
- `driver_en_route_to_outlet` -> `driver_arrived_at_outlet`.

Validate proximity for arrived if GPS reliable.

## 22.2 Mark restaurant order placed

Preconditions:

- Driver arrived or ordering state.
- No unresolved required customer confirmation for affected items.

Logic:

- Set status `restaurant_order_placed`.
- Set `restaurant_order_placed_at`.
- This timestamp changes cancellation financial responsibility.
- Notify customer.

## 22.3 Mark restaurant paid / waiting / ready

Transitions:

- `restaurant_order_placed` -> `waiting_for_food`.
- `waiting_for_food` -> `restaurant_paid` or `restaurant_paid` -> `waiting_for_food`, exact order can be policy-defined.
- `waiting_for_food`/`restaurant_paid` -> `ready_for_delivery`.

Optional:

- Receipt image proof can be added later or by policy.

# 23. Food item/price change logic

## 23.1 Driver proposes change

Input:

- Affected order item(s).
- Reason type.
- New price/remove/substitute/modifier change.
- Optional evidence image/note.

Preconditions:

- Driver assigned to order.
- Order in restaurant purchase phase before affected item purchased.

Logic:

1. Create `food_change_requests` status `awaiting_customer_decision`.
2. Create change item rows.
3. Pause affected purchase progression.
4. Notify customer.

Does not update catalog automatically.

## 23.2 Customer accepts change

Logic:

1. Validate customer owns order.
2. Validate request awaiting decision.
3. Apply accepted changes to order item snapshots.
4. Recalculate total.
5. If extra amount needed, create additional direct payment record or update payment delta according to policy.
6. Set change request `accepted`.
7. Notify driver.

## 23.3 Customer rejects change

Logic:

- Remove affected item, cancel order, or admin review depending change type/policy.
- Set change request `rejected`.
- Notify driver.

Open:

- Timeout behavior: auto-reject vs admin review vs cancel.

# 24. Food delivery/completion/cancellation logic

## 24.1 Delivery

Allowed transitions:

| From | Action | To |
|---|---|---|
| `ready_for_delivery` | leave outlet | `driver_en_route_to_customer` |
| `driver_en_route_to_customer` | arrive customer | `driver_arrived_at_customer` |
| `driver_arrived_at_customer` | mark delivered | `delivered` |
| `delivered` | complete | `completed` |

Side effects:

- Customer tracking event.
- Chat remains active until close window.
- Rating prompt after completed.

## 24.2 Cancellation financial responsibility

Before driver assignment:

- Customer can cancel. No payment issue.

After assignment before payment proof:

- Customer can cancel. Notify driver. No payment proof dispute.

After payment proof before restaurant order placed:

- Cancellation requires direct financial resolution flow.
- Onway does not auto-refund.
- Complaint/dispute can be opened.

After restaurant order placed:

- Customer change-of-mind cancellation does not create Onway refund.
- Order records customer financial responsibility.
- Driver/restaurant/system fault goes to complaint/dispute.

Tests:

- Restaurant order placed timestamp blocks generic refund wording.
- Driver cancels after proof triggers dispute/risk path.

# 25. Direct bank transfer logic

## 25.1 Create direct payment record

Create when:

- Ride reaches configured payment step.
- Food driver assigned and customer must prepay.

Validation:

- Payee driver has active payment account.
- Amount and currency snapshot are known.
- Payment method is `bank_transfer_qr`.

Snapshot:

- Bank name/code.
- Masked account number.
- Account holder.
- QR media/reference.
- Amount.
- Transfer note/reference if generated.

## 25.2 Submit payment proof

Rules:

- Proof image required.
- Customer can only submit for own ride/order.
- Proof status `submitted`.
- Payment record status `proof_submitted`.
- Notify driver.

Replacement:

- Default P0: allow replacement only before driver confirms received, and keep old proof marked `replaced`.

## 25.3 Payment dispute

Driver can report not received.

Logic:

- Payment record -> `driver_reported_not_received`.
- Entity -> `disputed` or review-needed state if service cannot continue.
- Create/flag complaint option.
- Admin queue receives case.

# 26. Chat logic

## 26.1 Create room

When driver assigned:

- Create `chat_rooms`.
- Add customer and driver participants.
- Status `active`.
- `retention_delete_after` = close time + 7 days. If no close time yet, compute/update when room closes.

## 26.2 Send message

Preconditions:

- Actor is participant.
- Room active.
- Message type valid.
- Image media exists and purpose `chat_image`.

Logic:

1. Insert `chat_messages`.
2. Insert attachment if image.
3. Emit `chat.message_created`.
4. Optionally create notification if receiver offline.

## 26.3 Close and retention

Close room when:

- Ride/order completed.
- Ride/order cancelled.
- Admin closes dispute if policy extends chat.

Retention:

- Chat text/image content retained for 1 week.
- If complaint filed before deletion, relevant messages/media can be linked/copied to complaint evidence.
- After retention, content status becomes `deleted_by_retention` or media deleted according to privacy policy.

Tests:

- Non-participant cannot read room.
- Message after room closed rejected.
- Retention job does not delete evidence already preserved for complaint.

# 27. Complaint/dispute logic

## 27.1 Submit complaint

Input:

- Service type/entity ID.
- Category.
- Description.
- Evidence IDs/media IDs.

Logic:

1. Authorize submitter belongs to related ride/order or allowed admin.
2. Validate category.
3. Validate required evidence for category.
4. Create complaint status `submitted` or `open_under_review`.
5. Link evidence.
6. Evaluate if qualifies for driver auto-lock.
7. Notify admin/support.

## 27.2 Qualify paid-but-driver-no-show

Complaint qualifies when:

- Category `paid_but_driver_no_show`.
- Entity assigned to target driver.
- Payment proof exists and links to same entity.
- Complaint is open/not invalid.
- Not duplicate.

If qualifies:

- Set `qualifies_for_driver_auto_lock = true`.
- Run auto-lock evaluation.

## 27.3 Admin review

Admin actions:

- Request more evidence.
- Request driver response.
- Resolve.
- Reject invalid.
- Escalate fraud.
- Lock/unlock driver separately.

All require reason except low-risk internal notes.

Tests:

- Complaint without required proof cannot be paid/no-show.
- Rejected invalid complaint does not count for auto-lock.
- Escalation creates linked fraud case.

# 28. Driver auto-lock logic

## 28.1 Evaluate auto-lock

Triggered by:

- Complaint created.
- Complaint category/status changed.
- Evidence added making complaint qualifying.

Logic:

```txt
evaluateDriverAutoLock(driver):
  threshold = policy("driver.auto_lock.qualifying_complaint_count", default=2)
  count = open, non-duplicate complaints against driver account where qualifies = true
  if count >= threshold and driver.risk_status not in locked/suspended/blocked:
    create driver_risk_action(auto_lock)
    set driver.risk_status = temporarily_locked
    forceOffline(driver)
    emit driver_status.locked
```

Important:

- Auto-lock does not decide fraud.
- Auto-lock prevents new jobs while review happens.
- Auto-unlock is not default P0; admin unlocks manually unless policy later allows recalculation.

Tests:

- First qualifying complaint does not lock.
- Second qualifying complaint locks.
- Duplicate complaint does not increase count.
- Invalidated complaint does not auto-unlock by default.

## 28.2 Manual lock/unlock

Manual lock:

- Admin permission required.
- Reason required.
- Takes effect immediately.
- Force offline.

Manual unlock:

- Admin permission required.
- Reason required.
- Recalculate eligibility.
- Does not erase complaint/fraud history.

# 29. Fraud case logic

## 29.1 Create fraud case

Sources:

- Complaint escalation.
- Admin action.
- Future AI suggestion.

Logic:

- Link source complaint/entity/evidence.
- Status `reported` or `triage`.
- Assign severity.
- Audit.

## 29.2 Human decision required

High-risk outcomes require human admin:

- Confirmed fraud.
- Permanent block/ban.
- Financial responsibility decision.

AI cannot finalize high-risk P0 decisions.

## 29.3 Fraud status transitions

| From | Action | To |
|---|---|---|
| `reported` | triage | `triage` |
| `triage` | collect evidence | `evidence_collection` |
| `evidence_collection` | request response | `response_requested` |
| `response_requested` | submit response | `human_review` |
| `human_review` | confirm | `confirmed` |
| `human_review` | reject | `rejected` |
| `confirmed` | appeal requested | `appeal_requested` |
| `confirmed`/`rejected` | finalize | `finalized` |

# 30. Rating logic

## 30.1 Submit rating

Preconditions:

- Ride/Food completed.
- Rater is participant.
- Rated account is counterpart.
- One rating per rater/rated/entity.

Logic:

- Validate score 1-5.
- Store tags/comment.
- Low score can prompt complaint.
- Rating does not auto-lock or update Trust in P0.

Tests:

- Rating before completion rejected.
- Duplicate rating rejected.
- Low rating prompt does not create complaint automatically without user submit.

# 31. Notification/realtime side effects

## 31.1 Emit after commit

Never emit final realtime events before transaction commit.

Events:

- `matching.offer_sent`
- `matching.offer_expired`
- `ride.assigned`
- `ride.status_changed`
- `food_order.assigned`
- `food_order.status_changed`
- `payment.proof_submitted`
- `payment.driver_confirmed`
- `chat.message_created`
- `driver.status_changed`
- `complaint.created`

## 31.2 Notification outbox

Use outbox for:

- Driver offer push fallback.
- Customer assignment update.
- Payment proof submitted.
- Complaint admin alert.
- Driver lock status.

Outbox worker:

1. Load pending rows.
2. Dispatch.
3. Mark sent/failed.
4. Retry failed with backoff.

# 32. Admin monitoring logic

Admin portal views should call query services, not direct DB ad hoc logic.

## 32.1 Ride/Food monitoring

Filters:

- Service type.
- Region.
- Status.
- Driver.
- Customer.
- Payment status.
- Dispute flag.
- Time range.

Detail page includes:

- Entity snapshot.
- State timeline.
- Matching session/offers.
- Payment proof.
- Chat/evidence within retention.
- Location snapshots.
- Complaint/fraud links.
- Audit log.

## 32.2 Driver review/risk dashboard

Shows:

- Onboarding status.
- Platform fee status.
- Vehicle/service eligibility.
- Payment account status.
- Risk status.
- Open complaints.
- Recent risk actions.

Actions:

- Approve/reject/request changes.
- Verify fee.
- Lock/unlock.
- Disable eligibility.

# 33. Scheduled jobs

## 33.1 Matching timeout job

Runs frequently or event-driven:

- Find offers expired.
- Mark expired.
- If no accepted offer in current batch, advance next batch or end no-driver.

## 33.2 Presence expiry

Redis TTL handles normal expiry.

Backend may run monitor to:

- Mark stale online drivers as unavailable.
- Notify app on reconnect.

## 33.3 Chat retention job

Runs daily/hourly:

- Find rooms past retention.
- Preserve evidence if linked to active complaint.
- Delete/mark content according to policy.
- Audit summary.

## 33.4 Policy/cache refresh

When config changes:

- Invalidate cache.
- Notify services if needed.

# 34. API command/query surface draft

Day chua phai GraphQL schema cuoi cung, nhung la command/query surface de dev tach service va resolver.

## 34.1 Identity/account

Queries:

- `me`
- `myCustomerProfile`
- `myDriverProfile`
- `myAllowedActions`

Mutations:

- `createCustomerProfile`
- `createDriverProfile`
- `updateAccountDisplayName`

Logic:

- All queries derive actor from Firebase token.
- Never trust role/profile ID from client without checking account ownership.

## 34.2 Region/config

Queries:

- `resolveRegionByCoordinate`
- `availableServices`
- `adminRegions`
- `adminPolicyConfigs`

Mutations:

- `adminCreateRegion`
- `adminUpdateRegionPolygon`
- `adminSetRegionServiceAvailability`
- `adminSetPolicyConfig`

Logic:

- Region polygon changes require admin permission and audit reason.
- Policy config mutations invalidate cache after commit.

## 34.3 Driver

Queries:

- `driverOnboardingStatus`
- `driverEligibility`
- `driverVehicles`
- `driverPaymentAccounts`
- `adminDriverReviewQueue`
- `adminDriverDetail`

Mutations:

- `driverSubmitProfile`
- `driverUploadDocument`
- `driverSubmitVehicle`
- `driverSubmitPaymentAccount`
- `driverGoOnline`
- `driverGoOffline`
- `adminApproveDriver`
- `adminRejectDriver`
- `adminApproveVehicle`
- `adminSetDriverServiceEligibility`
- `adminLockDriver`
- `adminUnlockDriver`

Logic:

- Driver online/offline is business state plus Redis presence; Redis alone is not account eligibility.
- Admin driver risk actions require reason.

## 34.4 Platform fee

Queries:

- `driverPlatformFeeInstruction`
- `driverPlatformFeeStatus`
- `adminPlatformFeeReviewQueue`

Mutations:

- `driverSubmitPlatformFeeProof`
- `adminApprovePlatformFeeProof`
- `adminRejectPlatformFeeProof`
- `adminCalculateDriverRefund`

Logic:

- Platform fee proof is separate from Ride/Food direct payment proof.
- Approval may trigger activation if all other requirements are met.

## 34.5 Catalog Food

Queries:

- `adminBrands`
- `adminOutlets`
- `adminMenuVersion`
- `foodDiscovery`
- `foodOutletMenu`

Mutations:

- `adminCreateBrand`
- `adminUpdateBrand`
- `adminCreateOutlet`
- `adminUpdateOutlet`
- `adminCreateMenu`
- `adminCreateMenuVersion`
- `adminUpsertMenuCategory`
- `adminUpsertMenuItem`
- `adminUpsertModifierGroup`
- `adminUpsertModifierOption`
- `adminSetOutletItemOverride`
- `adminSetOutletModifierOptionOverride`
- `adminSubmitCatalogReview`
- `adminPublishCatalog`
- `adminUnpublishCatalog`

Logic:

- Customer catalog queries only return published/effective menu.
- Admin mutations never directly update historical food order snapshots.

## 34.6 Ride

Queries:

- `rideQuote`
- `myActiveRide`
- `rideDetail`
- `adminRides`
- `adminRideDetail`

Mutations:

- `customerConfirmRideRequest`
- `customerCancelRide`
- `driverAcceptRideOffer`
- `driverRejectRideOffer`
- `driverMarkRideArrived`
- `driverStartRide`
- `driverCompleteRide`
- `customerSubmitRidePaymentProof`
- `driverConfirmRidePaymentReceived`
- `driverReportRidePaymentNotReceived`

Logic:

- Driver accept uses matching atomic transaction.
- Ride payment timing is policy-driven and still open.

## 34.7 Food

Queries:

- `foodQuote`
- `myActiveFoodOrder`
- `foodOrderDetail`
- `adminFoodOrders`
- `adminFoodOrderDetail`

Mutations:

- `customerConfirmFoodOrder`
- `customerCancelFoodOrder`
- `driverAcceptFoodOffer`
- `driverRejectFoodOffer`
- `customerSubmitFoodPaymentProof`
- `driverConfirmFoodPaymentReceived`
- `driverReportFoodPaymentNotReceived`
- `driverStartToOutlet`
- `driverMarkArrivedAtOutlet`
- `driverMarkRestaurantOrderPlaced`
- `driverMarkRestaurantPaid`
- `driverMarkFoodReadyForDelivery`
- `driverMarkArrivedAtCustomer`
- `driverMarkFoodDelivered`
- `driverCompleteFoodOrder`
- `driverProposeFoodChange`
- `customerAcceptFoodChange`
- `customerRejectFoodChange`

Logic:

- Food has no delivery fee negotiation.
- Driver cannot start restaurant purchase before required payment proof state.
- `restaurant_order_placed_at` is the cancellation responsibility boundary.

## 34.8 Chat/payment/evidence/support

Queries:

- `chatRoom`
- `chatMessages`
- `paymentRecord`
- `complaintDetail`
- `myComplaints`
- `adminComplaintQueue`
- `adminComplaintDetail`

Mutations:

- `createMediaUploadIntent`
- `completeMediaUpload`
- `sendChatMessage`
- `submitComplaint`
- `driverRespondToComplaint`
- `adminRequestComplaintEvidence`
- `adminResolveComplaint`
- `adminRejectComplaint`
- `adminEscalateComplaintToFraud`
- `adminCreateFraudCase`
- `adminDecideFraudCase`

Logic:

- Chat image and payment proof are both media, but must be linked through purpose-specific records.
- Complaint qualification may trigger driver auto-lock.

# 35. Allowed actions contract

Most entity detail queries should return server-computed `allowed_actions`.

Examples:

Ride for customer:

- `cancel`
- `open_chat`
- `submit_payment_proof`
- `submit_complaint`
- `rate_driver`

Ride for driver:

- `accept_offer`
- `reject_offer`
- `mark_arrived`
- `start_ride`
- `complete_ride`
- `confirm_payment_received`
- `report_payment_not_received`
- `open_chat`

Food for customer:

- `cancel`
- `submit_payment_proof`
- `accept_food_change`
- `reject_food_change`
- `open_chat`
- `submit_complaint`
- `rate_driver`

Food for driver:

- `accept_offer`
- `reject_offer`
- `confirm_payment_received`
- `report_payment_not_received`
- `start_to_outlet`
- `mark_arrived_at_outlet`
- `mark_restaurant_order_placed`
- `propose_food_change`
- `mark_ready_for_delivery`
- `mark_delivered`
- `complete_order`
- `open_chat`

Driver profile:

- `continue_onboarding`
- `submit_documents`
- `submit_platform_fee_proof`
- `go_online`
- `go_offline`
- `contact_support`

Rules:

- Clients should hide/disable actions not returned.
- Backend still validates all mutations.
- Disabled action reason should be available for important blocked states.

# 36. P0 technical test matrix

## 36.1 Unit tests

- Region containment and availability resolution.
- Effective menu calculation with overrides.
- Cart validation.
- Price/fee quote calculation wrapper.
- Payment state transition validation.
- Auto-lock qualification count.
- Refund calculation.
- Allowed actions generation.

## 36.2 Integration tests

- Customer auth -> create ride -> matching session created.
- Driver online -> receive offer -> accept -> assignment.
- Food catalog publish -> customer discovery -> cart -> order.
- Food order assigned -> payment proof -> driver purchase allowed.
- Complaint paid/no-show -> second qualifying complaint -> driver locked.
- Chat message/image authorization and retention marker.

## 36.3 E2E tests

Ride:

1. Customer creates ride.
2. Driver accepts.
3. Chat works.
4. Payment proof submitted at configured step.
5. Ride completes.
6. Rating submitted.

Food:

1. Admin creates brand/outlet/menu/publishes.
2. Customer discovers outlet.
3. Customer creates cart/order.
4. Driver accepts.
5. Customer uploads payment proof.
6. Driver places restaurant order.
7. Driver handles delivery.
8. Customer rates.

Dispute:

1. Customer pays and submits proof.
2. Driver no-shows.
3. Customer submits complaint.
4. Repeat second qualifying case.
5. System auto-locks driver.
6. Admin reviews and unlocks/keeps locked.

# 37. Recommended implementation order

Thu tu implement de co the test doc tung vertical slice:

1. Identity actor context:
   - Firebase token verify.
   - Account/profile mapping.
   - RBAC guard.

2. Core infrastructure tables/services:
   - Media upload intent.
   - Audit log.
   - Policy config lookup.
   - Notification outbox shell.

3. Region and availability:
   - Country/city/region.
   - PostGIS containment.
   - Service/vehicle availability.

4. Driver foundation:
   - Driver profile/onboarding.
   - Vehicle/service eligibility.
   - Driver payment account.
   - Platform fee proof/admin verify.
   - Driver activation.

5. Realtime foundation:
   - WebSocket auth.
   - Driver presence.
   - Basic room subscription.

6. Food supply admin-first:
   - Brand.
   - Outlet.
   - Menu/catalog.
   - Publishing.
   - Effective menu query.

7. Matching foundation:
   - Matching sessions/offers.
   - Candidate filter.
   - Accept transaction.

8. Direct bank transfer proof:
   - Payment record.
   - Payment proof upload.
   - Driver confirmation/dispute.

9. Chat:
   - Room creation on assignment.
   - Text/image messages.
   - Retention marker.

10. Ride vertical:
   - Quote/request.
   - Matching.
   - Tracking states.
   - Payment proof.
   - Completion/rating/cancel.

11. Food vertical:
   - Discovery/cart.
   - Quote/order.
   - Matching.
   - Payment proof.
   - Restaurant purchase.
   - Item/price change.
   - Delivery/rating/cancel.

12. Risk/support:
   - Complaint intake.
   - Paid-but-driver-no-show.
   - Auto-lock.
   - Admin review.
   - Fraud case shell.

13. Scheduled jobs:
   - Matching timeout.
   - Chat retention.
   - Notification dispatch.
   - Presence cleanup/monitoring.

# 38. Open logic decisions

1. Ride payment timing: before start or at completion.
2. Exact matching numbers: batch size, timeout, radius expansion, max attempts.
3. Exact definition of active job behavior when driver is locked mid-job.
4. Whether customer can replace payment proof before driver confirmation.
5. Whether chat metadata is retained after 1-week content deletion.
6. Whether admin can manually rematch Ride/Food in P0.
7. Exact complaint SLA and severity escalation.
8. Exact image/file limits for proof, chat image, documents and catalog.

Resolved P0 decision:

- Food restaurant purchase requires both customer payment proof submission and driver confirmation of received payment by default. Any admin/policy override must be explicit, auditable, and should not be a normal customer/driver path.
