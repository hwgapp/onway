# Analytics Events

| Event | Trigger | Properties | Platform | Notes |
| --- | --- | --- | --- | --- |
| app_opened | App foreground/open | app, version, user_type, region | Customer/Driver | Baseline |
| otp_requested | User requests OTP | user_type, country_code, provider | Customer/Driver/Admin | Abuse monitoring |
| otp_verified | OTP success | user_type | Customer/Driver/Admin | Auth funnel |
| device_identity_recorded | Device id/fingerprint recorded | user_type, platform, risk_signal_count | Customer/Driver | Fraud/risk only |
| ride_request_created | Customer confirms Ride request | pickup_region, dropoff_region, vehicle_type, recommended_price | Customer | Do not log exact sensitive location in analytics if not needed |
| ride_recommended_price_shown | Recommended price displayed | vehicle_type, region, price_bucket | Customer | Guardrail quality |
| ride_match_started | Matching starts for Ride | region, vehicle_type, candidate_count_bucket | Backend | Marketplace health |
| ride_driver_offer_sent | Driver offer sent | wave, eta_bucket, distance_bucket | Backend/Driver | Matching diagnostics |
| ride_driver_accepted | Driver accepts Ride offer | wave, eta_bucket, driver_status | Driver | Acceptance |
| ride_driver_rejected | Driver rejects Ride offer | wave, reason_code | Driver | Matching quality |
| ride_payment_disputed | Ride direct payment enters disputed state | reason_code, state, time_from_proof_bucket | Customer/Driver/Backend | SOP/manual review |
| ride_completed | Ride completed | region_start, region_end, vehicle_type, duration_bucket, price_bucket | Customer/Driver | Core success |
| ride_cancelled | Ride cancelled | actor, state, reason_code | Customer/Driver/Backend | Cancellation analysis |
| ride_rating_submitted | Customer/driver submits Ride rating | rating_bucket, tag_count, actor | Customer/Driver | 5-star + quick tags |
| food_order_created | Customer confirms Food order | outlet_id, brand_id, region, item_count, total_bucket | Customer | Core demand |
| food_delivery_fee_shown | Delivery fee shown | region, distance_bucket, fee_bucket | Customer | Pricing quality |
| food_match_started | Matching starts for Food | region, outlet_id, candidate_count_bucket | Backend | Marketplace health |
| food_driver_accepted | Driver accepts Food offer | wave, outlet_region, delivery_region | Driver | Acceptance |
| food_payment_proof_uploaded | Customer uploads proof | order_id, amount_bucket, media_type | Customer | Evidence flow |
| food_driver_money_received | Driver confirms received money | order_id, time_from_proof_bucket | Driver | Direct payment flow |
| food_payment_disputed | Food direct payment enters disputed state | reason_code, state, time_from_proof_bucket | Customer/Driver/Backend | SOP/manual review |
| food_order_placed_at_outlet | Driver marks order placed | outlet_id, wait_estimate_bucket | Driver | Cancellation boundary |
| food_delivered | Food order delivered | region_start, region_end, duration_bucket, total_bucket | Customer/Driver | Core success |
| food_change_proposed | Driver proposes item/price/status change | reason_code, amount_delta_bucket | Driver | Menu accuracy |
| food_change_accepted | Customer accepts change | reason_code | Customer | Order change |
| food_change_rejected | Customer rejects change | reason_code | Customer | Order change |
| food_change_timeout | Food change proposal times out | reason_code, timeout_seconds | Backend | Default 5 minutes, configurable |
| food_rating_submitted | Customer/driver submits Food rating | rating_bucket, tag_count, actor | Customer/Driver | 5-star + quick tags |
| driver_signup_started | Driver starts onboarding | platform, source | Driver | Driver funnel |
| driver_documents_submitted | Driver submits documents | vehicle_type, service_types | Driver | KYC funnel |
| platform_fee_proof_uploaded | Driver uploads platform fee proof | amount_bucket | Driver | Monetization |
| driver_activated | Driver activated by admin | vehicle_type, service_types | Admin | Supply readiness |
| driver_online | Driver goes online | region, service_flags | Driver | Supply |
| driver_offline | Driver goes offline | region, reason_code | Driver | Supply |
| chat_message_sent | Text chat sent | service_type, sender_type | Customer/Driver | Support/contact |
| chat_image_uploaded | Chat image uploaded | service_type, sender_type | Customer/Driver | Evidence/privacy sensitive |
| direct_call_started | User taps direct call | service_type, caller_type | Customer/Driver | Phone visibility |
| complaint_created | Complaint submitted | service_type, reporter_type, category | Customer/Driver/Admin | Quality/risk |
| complaint_escalated_to_fraud | Complaint escalated | category, service_type | Admin | Risk |
| auto_lock_triggered | Driver auto-lock triggered | trigger_type, threshold_id, case_id | Backend | paid/no-show, repeated complaint, severe risk, repeated payment dispute |
| driver_lock_appeal_submitted | Driver submits lock appeal | lock_reason_bucket, time_from_lock_bucket | Driver | Appeal in app |
| fraud_decision_finalized | Fraud case finalized | decision, service_type | Admin | Risk |
| risk_status_changed | User/driver risk status changed | subject_type, old_status, new_status, actor_role | Admin | Audit-sensitive |
| admin_region_published | Region config published | region_id, lifecycle, service_flags | Admin | Rollout |
| admin_region_publish_blocked | Region publish blocked | reason_code, service_flags | Admin | Invalid/overlap guardrail |
| policy_config_published | Policy config published | scope, key, version | Admin | Audit |
| push_notification_sent | Push notification sent | notification_type, target_type, delivery_status | Backend | Job, payment, chat, lock; no marketing push P0 |
