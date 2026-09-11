# ONWAY - Database Schema P0

**Loai tai lieu:** Database Schema / Technical PRD input  
**Phien ban:** 0.1  
**Trang thai:** Draft  
**Ngay cap nhat:** 11/09/2026  
**Database target:** PostgreSQL + PostGIS  
**Pham vi:** P0 launch schema cho Ride, Food admin-first, direct bank transfer, chat, complaint/risk lock  

---

# 1. Muc tieu

Tai lieu nay mo ta database schema P0 cho Onway de implement:

- Identity, auth mapping va RBAC.
- Region, currency, service availability.
- Driver onboarding, vehicle, eligibility, platform fee.
- Food supply admin-first: brand, outlet, menu, catalog publishing.
- Ride lifecycle.
- Food order lifecycle.
- Direct bank transfer/payment proof.
- Chat text/image retention 1 tuan.
- Media/evidence va audit trail.
- Complaint/dispute, paid-but-driver-no-show, driver risk lock.
- Basic rating va notification outbox.

Schema nay la source of truth ky thuat ban dau. Khi chuyen sang migration thuc te, co the dieu chinh theo ORM/framework nhung khong duoc lam mat business rule da chot.

# 2. Nguyen tac chung

## 2.1 PostgreSQL extensions

Can bat:

```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS citext;
```

## 2.2 Naming convention

- Ten bang: plural snake_case.
- Primary key: `id uuid PRIMARY KEY DEFAULT gen_random_uuid()`.
- Timestamp mac dinh:
  - `created_at timestamptz NOT NULL DEFAULT now()`
  - `updated_at timestamptz NOT NULL DEFAULT now()`
  - `deleted_at timestamptz NULL` neu can soft delete.
- Tien: `amount_minor bigint` + `currency_code char(3)`.
- Dia ly:
  - Point: `geometry(Point, 4326)`.
  - Polygon/MultiPolygon: `geometry(MultiPolygon, 4326)`.
- State/status: dung `text` + `CHECK` trong P0 de de mo rong hon PostgreSQL enum. Khi state on dinh moi can convert sang enum type.
- Du lieu co the thay doi theo thoi gian phai snapshot vao order/ride/payment de audit duoc lich su.

## 2.3 Actor model

`accounts` la identity goc. Mot account co the co nhieu profile:

- customer profile;
- driver profile;
- admin profile.

Khong dat bang la `users` de tranh nham voi reserved/common auth wording.

## 2.4 Money-light rule

Ride/Food money khong di qua Onway.

- Khach chuyen khoan truc tiep cho tai xe.
- Onway chi luu payment instruction snapshot, payment proof, confirmation/dispute state va audit.
- Platform fee cua driver la khoan Onway thu truc tiep, duoc tach bang rieng.

# 3. Schema overview

| Domain | Tables |
|---|---|
| Identity/RBAC | `accounts`, `account_roles`, `customer_profiles`, `driver_profiles`, `admin_profiles`, `admin_roles`, `admin_role_assignments`, `account_status_events` |
| Region/geo | `currencies`, `countries`, `cities`, `regions`, `region_service_configs`, `region_vehicle_configs` |
| Policy config | `policy_configs`, `policy_config_events` |
| Driver | `driver_vehicles`, `driver_documents`, `driver_service_eligibilities`, `driver_payment_accounts`, `driver_location_snapshots`, `driver_platform_fee_payments`, `driver_subscription_periods`, `driver_refund_records` |
| Food catalog | `restaurant_brands`, `restaurant_outlets`, `outlet_opening_hours`, `menus`, `menu_versions`, `menu_categories`, `menu_items`, `modifier_groups`, `modifier_options`, `menu_item_modifier_groups`, `outlet_menu_versions`, `outlet_item_overrides`, `outlet_modifier_option_overrides`, `catalog_publish_events` |
| Ride | `rides`, `ride_state_events`, `matching_sessions`, `matching_offers` |
| Food order | `food_orders`, `food_order_items`, `food_order_item_modifiers`, `food_order_state_events`, `food_change_requests`, `food_change_request_items` |
| Payment proof | `direct_payment_records`, `payment_proofs`, `payment_confirmations` |
| Chat | `chat_rooms`, `chat_participants`, `chat_messages`, `chat_message_attachments` |
| Media/audit | `media_objects`, `audit_logs`, `entity_state_events` |
| Risk/support | `complaints`, `complaint_evidence`, `complaint_responses`, `driver_risk_actions`, `fraud_cases`, `fraud_case_evidence` |
| Rating/notification | `ratings`, `device_tokens`, `notification_outbox` |

# 4. Identity va RBAC

## 4.1 `accounts`

Identity goc map voi Firebase Auth.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `firebase_uid` | text | yes | Unique |
| `phone_e164` | citext | yes | Unique trong MVP |
| `display_name` | text | no | Ten hien thi chung |
| `avatar_media_id` | uuid | no | FK `media_objects.id` |
| `status` | text | yes | `active`, `pending_verification`, `under_review`, `locked`, `suspended`, `blocked`, `deleted_requested` |
| `last_login_at` | timestamptz | no |  |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |
| `deleted_at` | timestamptz | no | Soft delete |

Constraints/indexes:

- `UNIQUE(firebase_uid)`.
- `UNIQUE(phone_e164) WHERE deleted_at IS NULL`.
- `CHECK status IN (...)`.
- Index `idx_accounts_status`.

## 4.2 `account_roles`

Gan role profile-level cho account.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `account_id` | uuid | yes | FK `accounts.id` |
| `role` | text | yes | `customer`, `driver`, `admin` |
| `status` | text | yes | `active`, `disabled` |
| `created_at` | timestamptz | yes |  |

Constraints:

- `UNIQUE(account_id, role)`.

## 4.3 `customer_profiles`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `account_id` | uuid | yes | FK `accounts.id`, unique |
| `status` | text | yes | `active`, `under_review`, `locked`, `suspended`, `blocked` |
| `default_region_id` | uuid | no | FK `regions.id` |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Indexes:

- `UNIQUE(account_id)`.
- `idx_customer_profiles_status`.

## 4.4 `driver_profiles`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `account_id` | uuid | yes | FK `accounts.id`, unique |
| `onboarding_status` | text | yes | Xem section Driver |
| `risk_status` | text | yes | `clear`, `under_review`, `temporarily_locked`, `suspended`, `blocked` |
| `activation_status` | text | yes | `inactive`, `pending_review`, `pending_platform_fee`, `active`, `deactivated` |
| `activated_at` | timestamptz | no | Bat dau tinh platform usage/refund |
| `home_city_id` | uuid | no | FK `cities.id` |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Constraints/indexes:

- `UNIQUE(account_id)`.
- Index `idx_driver_profiles_activation_status`.
- Index `idx_driver_profiles_risk_status`.

## 4.5 `admin_profiles`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `account_id` | uuid | yes | FK `accounts.id`, unique |
| `status` | text | yes | `active`, `disabled` |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

## 4.6 `admin_roles`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `code` | text | yes | Unique, e.g. `super_admin`, `operations_admin` |
| `name` | text | yes |  |
| `permissions` | jsonb | yes | Permission list/scope |
| `created_at` | timestamptz | yes |  |

## 4.7 `admin_role_assignments`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `admin_profile_id` | uuid | yes | FK `admin_profiles.id` |
| `admin_role_id` | uuid | yes | FK `admin_roles.id` |
| `assigned_by_admin_id` | uuid | no | FK `admin_profiles.id` |
| `created_at` | timestamptz | yes |  |

Constraints:

- `UNIQUE(admin_profile_id, admin_role_id)`.

## 4.8 `account_status_events`

Append-only history cho status changes.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `account_id` | uuid | yes | FK `accounts.id` |
| `from_status` | text | no |  |
| `to_status` | text | yes |  |
| `reason_code` | text | no |  |
| `reason_text` | text | no |  |
| `actor_type` | text | yes | `system`, `admin`, `customer`, `driver` |
| `actor_id` | uuid | no | Profile/account id theo actor |
| `created_at` | timestamptz | yes |  |

# 5. Region, currency, service availability

## 5.1 `currencies`

Currency config dung chung cho region va money display.

| Column | Type | Required | Note |
|---|---|---:|---|
| `code` | char(3) | yes | PK, e.g. `VND` |
| `name` | text | yes | e.g. Vietnamese Dong |
| `symbol` | text | no | e.g. `d` or `VND` |
| `minor_unit_exponent` | smallint | yes | VND = 0 |
| `status` | text | yes | `active`, `disabled` |
| `created_at` | timestamptz | yes |  |

## 5.2 `countries`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `iso2` | char(2) | yes | Unique, e.g. `VN` |
| `name` | text | yes |  |
| `default_currency_code` | char(3) | yes | e.g. `VND` |
| `default_timezone` | text | yes | e.g. `Asia/Ho_Chi_Minh` |
| `status` | text | yes | `planned`, `active`, `paused`, `closed` |
| `created_at` | timestamptz | yes |  |

## 5.3 `cities`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `country_id` | uuid | yes | FK `countries.id` |
| `name` | text | yes |  |
| `slug` | text | yes |  |
| `timezone` | text | yes |  |
| `status` | text | yes | `planned`, `pilot`, `active`, `paused`, `closed` |
| `created_at` | timestamptz | yes |  |

Constraints:

- `UNIQUE(country_id, slug)`.

## 5.4 `regions`

Region launch/operation boundary.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `city_id` | uuid | yes | FK `cities.id` |
| `name` | text | yes |  |
| `slug` | text | yes | Unique per city |
| `status` | text | yes | `planned`, `pilot`, `active`, `paused`, `closed` |
| `currency_code` | char(3) | yes | Region-level currency |
| `timezone` | text | yes | Usually city timezone |
| `boundary` | geometry(MultiPolygon,4326) | yes | PostGIS |
| `created_by_admin_id` | uuid | no | FK `admin_profiles.id` |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Indexes:

- `GIST(boundary)`.
- `UNIQUE(city_id, slug)`.
- `idx_regions_status`.

## 5.5 `region_service_configs`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `region_id` | uuid | yes | FK `regions.id` |
| `service_type` | text | yes | `ride`, `food` |
| `status` | text | yes | `enabled`, `disabled`, `paused` |
| `operating_windows` | jsonb | no | Weekly windows |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Constraints:

- `UNIQUE(region_id, service_type)`.

## 5.6 `region_vehicle_configs`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `region_id` | uuid | yes | FK `regions.id` |
| `service_type` | text | yes | `ride`, `food` |
| `vehicle_type` | text | yes | `motorcycle`, `car` |
| `status` | text | yes | `enabled`, `disabled`, `paused` |
| `created_at` | timestamptz | yes |  |

Constraints:

- `UNIQUE(region_id, service_type, vehicle_type)`.

# 6. Policy config

## 6.1 `policy_configs`

Generic config store cho business values.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `key` | text | yes | e.g. `matching.ride.batch_size` |
| `scope_type` | text | yes | `global`, `country`, `city`, `region`, `service`, `brand`, `outlet` |
| `scope_id` | uuid | no | Null neu global |
| `value_type` | text | yes | `string`, `number`, `boolean`, `duration`, `money`, `json` |
| `value_json` | jsonb | yes | Typed payload |
| `status` | text | yes | `active`, `inactive` |
| `version` | integer | yes | Increment |
| `effective_from` | timestamptz | no |  |
| `effective_to` | timestamptz | no |  |
| `updated_by_admin_id` | uuid | no | FK `admin_profiles.id` |
| `reason` | text | no | Required in admin flow |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Constraints/indexes:

- `UNIQUE(key, scope_type, scope_id, version)`.
- Index `idx_policy_configs_lookup(key, scope_type, scope_id, status)`.

## 6.2 `policy_config_events`

Append-only history.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `policy_config_id` | uuid | yes | FK |
| `event_type` | text | yes | `created`, `updated`, `activated`, `deactivated`, `restored` |
| `old_value_json` | jsonb | no |  |
| `new_value_json` | jsonb | no |  |
| `actor_admin_id` | uuid | no | FK |
| `reason` | text | no |  |
| `created_at` | timestamptz | yes |  |

# 7. Driver foundation

## 7.1 `driver_vehicles`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `driver_profile_id` | uuid | yes | FK `driver_profiles.id` |
| `vehicle_type` | text | yes | `motorcycle`, `car` |
| `display_name` | text | no | e.g. Honda Vision, Toyota Vios |
| `plate_number` | text | no | Can encrypt/mask if needed |
| `color` | text | no |  |
| `status` | text | yes | `draft`, `pending_review`, `approved`, `rejected`, `disabled` |
| `reviewed_by_admin_id` | uuid | no | FK |
| `reviewed_at` | timestamptz | no |  |
| `review_note` | text | no |  |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Indexes:

- `idx_driver_vehicles_driver_status`.
- `idx_driver_vehicles_type_status`.

## 7.2 `driver_documents`

Document type list se chot sau; schema can support config-driven docs.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `driver_profile_id` | uuid | yes | FK |
| `vehicle_id` | uuid | no | FK `driver_vehicles.id` neu document theo xe |
| `document_type` | text | yes | e.g. `identity_card`, `driver_license` |
| `media_id` | uuid | yes | FK `media_objects.id` |
| `status` | text | yes | `uploaded`, `approved`, `rejected`, `expired`, `replaced` |
| `expires_at` | timestamptz | no |  |
| `reviewed_by_admin_id` | uuid | no | FK |
| `reviewed_at` | timestamptz | no |  |
| `rejection_reason` | text | no |  |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Indexes:

- `idx_driver_documents_driver_type_status`.

## 7.3 `driver_service_eligibilities`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `driver_profile_id` | uuid | yes | FK |
| `vehicle_id` | uuid | yes | FK `driver_vehicles.id` |
| `region_id` | uuid | yes | FK `regions.id` |
| `service_type` | text | yes | `ride`, `food` |
| `status` | text | yes | `eligible`, `ineligible`, `paused`, `revoked` |
| `reason` | text | no |  |
| `updated_by_admin_id` | uuid | no | FK |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Constraints:

- `UNIQUE(driver_profile_id, vehicle_id, region_id, service_type)`.

## 7.4 `driver_payment_accounts`

Thong tin de customer chuyen khoan truc tiep cho driver.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `driver_profile_id` | uuid | yes | FK |
| `region_id` | uuid | no | Region-specific neu can |
| `bank_name` | text | yes |  |
| `bank_code` | text | no |  |
| `account_number_encrypted` | text | yes | Encrypt at app/service layer |
| `account_holder_name` | text | yes |  |
| `qr_media_id` | uuid | no | FK `media_objects.id` |
| `status` | text | yes | `pending_review`, `active`, `disabled`, `rejected` |
| `is_default` | boolean | yes | Default false |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Indexes:

- `idx_driver_payment_accounts_driver_status`.
- Partial unique default: one active default per driver where possible.

## 7.5 `driver_location_snapshots`

DB chi luu snapshots quan trong; realtime presence nam Redis.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `driver_profile_id` | uuid | yes | FK |
| `related_entity_type` | text | no | `ride`, `food_order`, `matching_offer` |
| `related_entity_id` | uuid | no |  |
| `location` | geometry(Point,4326) | yes |  |
| `accuracy_meters` | numeric | no |  |
| `heading` | numeric | no |  |
| `speed_mps` | numeric | no |  |
| `captured_at` | timestamptz | yes | Device/provider time |
| `created_at` | timestamptz | yes | Server time |

Indexes:

- `GIST(location)`.
- `idx_driver_location_snapshots_driver_time(driver_profile_id, captured_at DESC)`.
- `idx_driver_location_snapshots_entity(related_entity_type, related_entity_id)`.

## 7.6 `driver_platform_fee_payments`

Khoan Onway thu truc tiep tu driver, tach khoi Ride/Food direct payment.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `driver_profile_id` | uuid | yes | FK |
| `amount_minor` | bigint | yes | With VND exponent 0, `1.000.000 VND` is stored as `1000000` |
| `currency_code` | char(3) | yes | `VND` |
| `payment_method` | text | yes | `bank_transfer_qr` |
| `proof_media_id` | uuid | yes | FK `media_objects.id` |
| `reference_text` | text | no | Transfer note/ref |
| `status` | text | yes | `submitted`, `approved`, `rejected`, `resubmission_required` |
| `reviewed_by_admin_id` | uuid | no | FK |
| `reviewed_at` | timestamptz | no |  |
| `review_reason` | text | no |  |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Note: VND has no decimal in practice, but schema still uses minor units consistently. For VND, define `minor_unit_exponent = 0` in app/currency config or store VND amount as dong in `amount_minor`.

## 7.7 `driver_subscription_periods`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `driver_profile_id` | uuid | yes | FK |
| `source_payment_id` | uuid | no | FK `driver_platform_fee_payments.id` |
| `period_type` | text | yes | `paid`, `bonus`, `future_subscription` |
| `starts_at` | timestamptz | yes |  |
| `ends_at` | timestamptz | yes |  |
| `status` | text | yes | `active`, `cancelled`, `expired` |
| `created_at` | timestamptz | yes |  |

## 7.8 `driver_refund_records`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `driver_profile_id` | uuid | yes | FK |
| `source_payment_id` | uuid | yes | FK |
| `calculated_amount_minor` | bigint | yes |  |
| `currency_code` | char(3) | yes |  |
| `calculation_json` | jsonb | yes | Quarter breakdown |
| `status` | text | yes | `calculated`, `approved`, `rejected`, `paid_manually` |
| `created_by_admin_id` | uuid | no | FK |
| `created_at` | timestamptz | yes |  |

# 8. Food supply admin-first

## 8.1 `restaurant_brands`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `name` | text | yes |  |
| `slug` | text | yes | Unique |
| `status` | text | yes | `draft`, `active`, `paused`, `archived` |
| `category_tags` | text[] | no |  |
| `logo_media_id` | uuid | no | FK |
| `default_waiting_policy_config_id` | uuid | no | FK `policy_configs.id` |
| `created_by_admin_id` | uuid | no | FK |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |
| `deleted_at` | timestamptz | no |  |

Constraints:

- `UNIQUE(slug) WHERE deleted_at IS NULL`.

## 8.2 `restaurant_outlets`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `brand_id` | uuid | yes | FK `restaurant_brands.id` |
| `region_id` | uuid | yes | FK `regions.id` |
| `name` | text | yes |  |
| `slug` | text | yes | Unique per brand/region |
| `address_text` | text | yes |  |
| `location` | geometry(Point,4326) | yes |  |
| `phone` | text | no |  |
| `status` | text | yes | `draft`, `pending_review`, `active`, `paused`, `temporarily_closed`, `closed`, `archived` |
| `availability_status` | text | yes | `available`, `unavailable`, `closed_now`, `busy` |
| `created_by_admin_id` | uuid | no | FK |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |
| `deleted_at` | timestamptz | no |  |

Indexes:

- `GIST(location)`.
- `UNIQUE(brand_id, region_id, slug) WHERE deleted_at IS NULL`.
- `idx_restaurant_outlets_region_status`.

## 8.3 `outlet_opening_hours`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `outlet_id` | uuid | yes | FK |
| `day_of_week` | smallint | yes | 0-6 |
| `opens_at_local` | time | yes |  |
| `closes_at_local` | time | yes |  |
| `is_closed` | boolean | yes | default false |
| `valid_from` | date | no |  |
| `valid_to` | date | no |  |
| `created_at` | timestamptz | yes |  |

Indexes:

- `idx_outlet_opening_hours_outlet_day`.

## 8.4 `menus`

Canonical menu container.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `brand_id` | uuid | yes | FK |
| `name` | text | yes |  |
| `status` | text | yes | `draft`, `active`, `archived` |
| `created_by_admin_id` | uuid | no | FK |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

## 8.5 `menu_versions`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `menu_id` | uuid | yes | FK |
| `version_number` | integer | yes | Increment |
| `status` | text | yes | `draft`, `pending_review`, `published`, `needs_reverification`, `unpublished`, `archived` |
| `source_media_id` | uuid | no | Menu image/file ref |
| `published_at` | timestamptz | no |  |
| `published_by_admin_id` | uuid | no | FK |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Constraints:

- `UNIQUE(menu_id, version_number)`.

## 8.6 `menu_categories`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `menu_version_id` | uuid | yes | FK |
| `name` | text | yes |  |
| `description` | text | no |  |
| `sort_order` | integer | yes | default 0 |
| `status` | text | yes | `active`, `hidden` |
| `created_at` | timestamptz | yes |  |

## 8.7 `menu_items`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `menu_version_id` | uuid | yes | FK |
| `category_id` | uuid | yes | FK `menu_categories.id` |
| `name` | text | yes |  |
| `description` | text | no |  |
| `base_price_minor` | bigint | yes |  |
| `currency_code` | char(3) | yes |  |
| `image_media_id` | uuid | no | FK |
| `status` | text | yes | `active`, `unavailable`, `hidden` |
| `sort_order` | integer | yes | default 0 |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Indexes:

- `idx_menu_items_version_status`.
- Full-text/search index later if needed.

## 8.8 `modifier_groups`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `menu_version_id` | uuid | yes | FK |
| `name` | text | yes |  |
| `is_required` | boolean | yes |  |
| `min_select` | integer | yes | default 0 |
| `max_select` | integer | yes | default 1 |
| `sort_order` | integer | yes | default 0 |
| `status` | text | yes | `active`, `hidden` |
| `created_at` | timestamptz | yes |  |

Constraint:

- `CHECK (min_select >= 0 AND max_select >= min_select)`.

## 8.9 `modifier_options`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `modifier_group_id` | uuid | yes | FK |
| `name` | text | yes |  |
| `price_delta_minor` | bigint | yes | default 0 |
| `currency_code` | char(3) | yes |  |
| `status` | text | yes | `active`, `unavailable`, `hidden` |
| `sort_order` | integer | yes | default 0 |
| `created_at` | timestamptz | yes |  |

## 8.10 `menu_item_modifier_groups`

Many-to-many item -> modifier group.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `menu_item_id` | uuid | yes | FK |
| `modifier_group_id` | uuid | yes | FK |
| `sort_order` | integer | yes | default 0 |

Constraint:

- `UNIQUE(menu_item_id, modifier_group_id)`.

## 8.11 `outlet_menu_versions`

Gan published menu version cho outlet.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `outlet_id` | uuid | yes | FK |
| `menu_version_id` | uuid | yes | FK |
| `status` | text | yes | `active`, `inactive` |
| `effective_from` | timestamptz | yes | default now |
| `effective_to` | timestamptz | no |  |
| `created_at` | timestamptz | yes |  |

Constraints:

- Partial unique active menu per outlet: `UNIQUE(outlet_id) WHERE status = 'active'`.

## 8.12 `outlet_item_overrides`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `outlet_id` | uuid | yes | FK |
| `menu_item_id` | uuid | yes | FK |
| `override_price_minor` | bigint | no | Null means no price override |
| `availability_status` | text | no | `available`, `unavailable`, `hidden` |
| `reason` | text | no |  |
| `status` | text | yes | `active`, `inactive` |
| `updated_by_admin_id` | uuid | no | FK |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Constraints:

- `UNIQUE(outlet_id, menu_item_id) WHERE status = 'active'`.

## 8.13 `outlet_modifier_option_overrides`

Outlet-specific override cho modifier option, vi mot outlet co the het topping/size hoac gia option khac canonical menu.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `outlet_id` | uuid | yes | FK |
| `modifier_option_id` | uuid | yes | FK |
| `override_price_delta_minor` | bigint | no | Null means no price override |
| `availability_status` | text | no | `available`, `unavailable`, `hidden` |
| `reason` | text | no |  |
| `status` | text | yes | `active`, `inactive` |
| `updated_by_admin_id` | uuid | no | FK |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Constraints:

- `UNIQUE(outlet_id, modifier_option_id) WHERE status = 'active'`.

## 8.14 `catalog_publish_events`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `entity_type` | text | yes | `brand`, `outlet`, `menu_version` |
| `entity_id` | uuid | yes |  |
| `from_status` | text | no |  |
| `to_status` | text | yes |  |
| `actor_admin_id` | uuid | yes | FK |
| `reason` | text | no |  |
| `created_at` | timestamptz | yes |  |

# 9. Ride

## 9.1 `rides`

One row per customer Ride request/trip.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `customer_profile_id` | uuid | yes | FK |
| `driver_profile_id` | uuid | no | FK after assignment |
| `vehicle_id` | uuid | no | FK selected/assigned driver vehicle |
| `region_id` | uuid | yes | FK |
| `vehicle_type` | text | yes | `motorcycle`, `car` |
| `status` | text | yes | See ride states |
| `pickup_address_text` | text | yes | Snapshot |
| `pickup_location` | geometry(Point,4326) | yes |  |
| `dropoff_address_text` | text | yes | Snapshot |
| `dropoff_location` | geometry(Point,4326) | yes |  |
| `estimated_distance_meters` | integer | no | Snapshot |
| `estimated_duration_seconds` | integer | no | Snapshot |
| `recommended_price_minor` | bigint | yes |  |
| `final_price_minor` | bigint | yes | P0 same as recommended unless later negotiation |
| `currency_code` | char(3) | yes | Snapshot from region |
| `requested_at` | timestamptz | yes |  |
| `assigned_at` | timestamptz | no |  |
| `started_at` | timestamptz | no |  |
| `completed_at` | timestamptz | no |  |
| `cancelled_at` | timestamptz | no |  |
| `cancellation_reason` | text | no |  |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Ride statuses:

- `draft`
- `priced`
- `matching`
- `assigned`
- `driver_en_route_to_pickup`
- `driver_arrived`
- `awaiting_payment_if_required`
- `ready_to_start`
- `in_progress`
- `arrived_at_destination`
- `completed`
- `cancelled`
- `expired_no_driver`
- `disputed`

Indexes:

- `idx_rides_customer_created(customer_profile_id, created_at DESC)`.
- `idx_rides_driver_status(driver_profile_id, status)`.
- `idx_rides_region_status(region_id, status)`.
- `GIST(pickup_location)`, `GIST(dropoff_location)`.

## 9.2 `ride_state_events`

Append-only ride timeline.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `ride_id` | uuid | yes | FK |
| `from_status` | text | no |  |
| `to_status` | text | yes |  |
| `event_type` | text | yes | e.g. `customer_confirmed`, `driver_arrived` |
| `actor_type` | text | yes |  |
| `actor_id` | uuid | no |  |
| `metadata_json` | jsonb | no |  |
| `created_at` | timestamptz | yes |  |

Indexes:

- `idx_ride_state_events_ride_time(ride_id, created_at)`.

# 10. Matching

## 10.1 `matching_sessions`

Used for Ride and Food matching.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `service_type` | text | yes | `ride`, `food` |
| `entity_id` | uuid | yes | ride id or food order id |
| `region_id` | uuid | yes | FK |
| `status` | text | yes | `queued`, `batch_offered`, `assigned`, `no_driver_available`, `expired`, `cancelled` |
| `current_batch_number` | integer | yes | default 0 |
| `max_batch_count` | integer | yes | Snapshot policy |
| `batch_size` | integer | yes | Snapshot policy |
| `initial_radius_meters` | integer | yes | Snapshot policy |
| `current_radius_meters` | integer | yes |  |
| `offer_timeout_seconds` | integer | yes | Snapshot policy |
| `started_at` | timestamptz | yes |  |
| `ended_at` | timestamptz | no |  |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Constraints/indexes:

- `UNIQUE(service_type, entity_id)`.
- `idx_matching_sessions_status`.

## 10.2 `matching_offers`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `matching_session_id` | uuid | yes | FK |
| `driver_profile_id` | uuid | yes | FK |
| `vehicle_id` | uuid | no | FK |
| `batch_number` | integer | yes |  |
| `status` | text | yes | `sent`, `accepted`, `rejected`, `expired`, `cancelled_assignment_taken`, `cancelled_by_customer` |
| `offered_price_minor` | bigint | yes | Ride fare or Food delivery fee |
| `currency_code` | char(3) | yes |  |
| `expires_at` | timestamptz | yes |  |
| `responded_at` | timestamptz | no |  |
| `response_reason` | text | no |  |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Constraints/indexes:

- `UNIQUE(matching_session_id, driver_profile_id)`.
- `idx_matching_offers_driver_status(driver_profile_id, status)`.
- `idx_matching_offers_session_status(matching_session_id, status)`.
- `idx_matching_offers_expires_at(expires_at)`.

# 11. Food orders

## 11.1 `food_orders`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `customer_profile_id` | uuid | yes | FK |
| `driver_profile_id` | uuid | no | FK after assignment |
| `outlet_id` | uuid | yes | FK |
| `region_id` | uuid | yes | FK |
| `status` | text | yes | See below |
| `delivery_address_text` | text | yes | Snapshot |
| `delivery_location` | geometry(Point,4326) | yes |  |
| `item_total_minor` | bigint | yes | Snapshot |
| `delivery_fee_minor` | bigint | yes | System fee, no negotiation |
| `estimated_total_minor` | bigint | yes | Item total + delivery fee + optional waiting estimate |
| `currency_code` | char(3) | yes | Snapshot |
| `estimated_distance_meters` | integer | no | Outlet -> delivery |
| `estimated_duration_seconds` | integer | no |  |
| `customer_confirmed_at` | timestamptz | no |  |
| `assigned_at` | timestamptz | no |  |
| `payment_proof_submitted_at` | timestamptz | no |  |
| `restaurant_order_placed_at` | timestamptz | no | Financial responsibility boundary |
| `completed_at` | timestamptz | no |  |
| `cancelled_at` | timestamptz | no |  |
| `cancellation_reason` | text | no |  |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Food statuses:

- `cart`
- `quoted`
- `customer_confirmed`
- `matching`
- `assigned`
- `awaiting_customer_transfer`
- `payment_proof_submitted`
- `driver_confirmed_payment`
- `driver_en_route_to_outlet`
- `driver_arrived_at_outlet`
- `ordering_with_restaurant`
- `restaurant_order_placed`
- `waiting_for_food`
- `restaurant_paid`
- `ready_for_delivery`
- `driver_en_route_to_customer`
- `driver_arrived_at_customer`
- `delivered`
- `completed`
- `cancelled`
- `delivery_failed`
- `disputed`

Indexes:

- `idx_food_orders_customer_created(customer_profile_id, created_at DESC)`.
- `idx_food_orders_driver_status(driver_profile_id, status)`.
- `idx_food_orders_outlet_status(outlet_id, status)`.
- `idx_food_orders_region_status(region_id, status)`.
- `GIST(delivery_location)`.

## 11.2 `food_order_items`

Snapshot of ordered items.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `food_order_id` | uuid | yes | FK |
| `menu_item_id` | uuid | no | FK, nullable if item later removed/archived |
| `item_name_snapshot` | text | yes |  |
| `quantity` | integer | yes | > 0 |
| `unit_price_minor` | bigint | yes |  |
| `total_price_minor` | bigint | yes | quantity * unit + modifiers |
| `currency_code` | char(3) | yes |  |
| `status` | text | yes | `active`, `removed`, `unavailable`, `substituted` |
| `created_at` | timestamptz | yes |  |

Constraints:

- `CHECK(quantity > 0)`.

## 11.3 `food_order_item_modifiers`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `food_order_item_id` | uuid | yes | FK |
| `modifier_group_name_snapshot` | text | yes |  |
| `modifier_option_name_snapshot` | text | yes |  |
| `price_delta_minor` | bigint | yes |  |
| `currency_code` | char(3) | yes |  |
| `created_at` | timestamptz | yes |  |

## 11.4 `food_order_state_events`

Same role as ride timeline.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `food_order_id` | uuid | yes | FK |
| `from_status` | text | no |  |
| `to_status` | text | yes |  |
| `event_type` | text | yes |  |
| `actor_type` | text | yes |  |
| `actor_id` | uuid | no |  |
| `metadata_json` | jsonb | no |  |
| `created_at` | timestamptz | yes |  |

## 11.5 `food_change_requests`

When driver finds item/price/status changed at restaurant.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `food_order_id` | uuid | yes | FK |
| `driver_profile_id` | uuid | yes | FK |
| `status` | text | yes | `proposed`, `awaiting_customer_decision`, `accepted`, `rejected`, `expired`, `admin_review_required` |
| `reason_type` | text | yes | `price_change`, `item_unavailable`, `modifier_unavailable`, `substitution`, `other` |
| `note` | text | no |  |
| `evidence_media_id` | uuid | no | FK |
| `customer_decided_at` | timestamptz | no |  |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

## 11.6 `food_change_request_items`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `change_request_id` | uuid | yes | FK |
| `food_order_item_id` | uuid | yes | FK |
| `change_type` | text | yes | `price_update`, `remove_item`, `replace_item`, `modifier_update` |
| `old_value_json` | jsonb | no |  |
| `new_value_json` | jsonb | no |  |
| `price_delta_minor` | bigint | no |  |
| `created_at` | timestamptz | yes |  |

# 12. Direct payment proof

## 12.1 `direct_payment_records`

Works for Ride/Food direct transfer to driver.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `service_type` | text | yes | `ride`, `food` |
| `entity_id` | uuid | yes | `rides.id` or `food_orders.id` |
| `payer_account_id` | uuid | yes | Customer account |
| `payee_account_id` | uuid | yes | Driver account |
| `driver_payment_account_id` | uuid | yes | FK snapshot source |
| `amount_minor` | bigint | yes |  |
| `currency_code` | char(3) | yes |  |
| `method` | text | yes | `bank_transfer_qr` |
| `status` | text | yes | `awaiting_customer_transfer`, `proof_submitted`, `driver_confirmed_received`, `driver_reported_not_received`, `admin_review_required`, `confirmed_by_admin`, `rejected_by_admin`, `disputed` |
| `payment_instructions_snapshot_json` | jsonb | yes | Bank/QR details shown to customer |
| `required_before_event` | text | yes | e.g. `food_driver_purchase`, `ride_start`, `ride_completion` |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Constraints/indexes:

- `UNIQUE(service_type, entity_id, required_before_event)`.
- `idx_direct_payment_records_status`.

## 12.2 `payment_proofs`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `direct_payment_record_id` | uuid | yes | FK |
| `uploaded_by_account_id` | uuid | yes | Customer account |
| `media_id` | uuid | yes | FK `media_objects.id` |
| `reference_text` | text | no | Transfer note/ref |
| `amount_claimed_minor` | bigint | no | If customer enters amount |
| `status` | text | yes | `submitted`, `accepted_for_review`, `replaced`, `rejected` |
| `created_at` | timestamptz | yes |  |

Indexes:

- `idx_payment_proofs_record_time`.

## 12.3 `payment_confirmations`

Driver/admin confirmation or dispute.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `direct_payment_record_id` | uuid | yes | FK |
| `actor_type` | text | yes | `driver`, `admin`, `system` |
| `actor_id` | uuid | no |  |
| `confirmation_type` | text | yes | `received`, `not_received`, `confirmed_by_admin`, `rejected_by_admin` |
| `note` | text | no |  |
| `created_at` | timestamptz | yes |  |

# 13. Chat

## 13.1 `chat_rooms`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `service_type` | text | yes | `ride`, `food` |
| `entity_id` | uuid | yes | Ride/Food id |
| `status` | text | yes | `created`, `active`, `closed`, `retention_pending`, `content_deleted` |
| `opened_at` | timestamptz | yes |  |
| `closed_at` | timestamptz | no |  |
| `retention_delete_after` | timestamptz | yes | Usually opened/closed + 7 days per policy |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Constraints:

- `UNIQUE(service_type, entity_id)`.
- Index `idx_chat_rooms_retention(retention_delete_after, status)`.

## 13.2 `chat_participants`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `chat_room_id` | uuid | yes | FK |
| `account_id` | uuid | yes | FK |
| `participant_type` | text | yes | `customer`, `driver`, `admin_viewer` |
| `created_at` | timestamptz | yes |  |

Constraints:

- `UNIQUE(chat_room_id, account_id)`.

## 13.3 `chat_messages`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `chat_room_id` | uuid | yes | FK |
| `sender_account_id` | uuid | yes | FK |
| `message_type` | text | yes | `text`, `image` |
| `body_text` | text | no | Null for image-only |
| `status` | text | yes | `sent`, `delivered`, `read`, `deleted_by_retention`, `removed_by_admin` |
| `sent_at` | timestamptz | yes |  |
| `created_at` | timestamptz | yes |  |

Indexes:

- `idx_chat_messages_room_time(chat_room_id, sent_at)`.

## 13.4 `chat_message_attachments`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `chat_message_id` | uuid | yes | FK |
| `media_id` | uuid | yes | FK |
| `created_at` | timestamptz | yes |  |

Retention:

- Chat content/image retention is 1 week.
- If complaint is filed within retention window, required evidence may be copied/linked into complaint evidence according to policy before content deletion.

# 14. Media and audit

## 14.1 `media_objects`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `storage_bucket` | text | yes |  |
| `storage_key` | text | yes | Private object key |
| `mime_type` | text | yes |  |
| `size_bytes` | bigint | yes |  |
| `checksum_sha256` | text | no |  |
| `uploaded_by_account_id` | uuid | no | FK |
| `purpose` | text | yes | `payment_proof`, `chat_image`, `driver_document`, `catalog_image`, `complaint_evidence`, `platform_fee_proof` |
| `status` | text | yes | `active`, `deleted_by_retention`, `removed`, `quarantined` |
| `metadata_json` | jsonb | no | GPS/device/source metadata where allowed |
| `created_at` | timestamptz | yes |  |
| `deleted_at` | timestamptz | no |  |

Indexes:

- `idx_media_objects_purpose_status`.
- `idx_media_objects_uploader_time`.

## 14.2 `audit_logs`

Generic append-only audit log.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `actor_type` | text | yes | `system`, `admin`, `customer`, `driver` |
| `actor_id` | uuid | no |  |
| `action` | text | yes | e.g. `driver.locked`, `catalog.published` |
| `target_type` | text | yes | Table/entity type |
| `target_id` | uuid | yes | Entity id |
| `reason` | text | no | Required for admin risk actions |
| `before_json` | jsonb | no | Avoid sensitive full docs if not needed |
| `after_json` | jsonb | no |  |
| `metadata_json` | jsonb | no |  |
| `created_at` | timestamptz | yes |  |

Indexes:

- `idx_audit_logs_target(target_type, target_id, created_at)`.
- `idx_audit_logs_actor(actor_type, actor_id, created_at)`.
- `idx_audit_logs_action_created(action, created_at)`.

## 14.3 `entity_state_events`

Optional generic event stream for cross-entity timeline. Use alongside domain-specific event tables if needed.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `entity_type` | text | yes |  |
| `entity_id` | uuid | yes |  |
| `from_state` | text | no |  |
| `to_state` | text | yes |  |
| `event_type` | text | yes |  |
| `actor_type` | text | yes |  |
| `actor_id` | uuid | no |  |
| `metadata_json` | jsonb | no |  |
| `created_at` | timestamptz | yes |  |

# 15. Complaint, dispute, fraud, driver risk

## 15.1 `complaints`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `submitted_by_account_id` | uuid | yes | FK |
| `against_account_id` | uuid | no | FK |
| `service_type` | text | no | `ride`, `food` |
| `entity_id` | uuid | no | Ride/Food id |
| `category` | text | yes | e.g. `paid_but_driver_no_show` |
| `severity` | text | yes | `low`, `medium`, `high`, `critical` |
| `status` | text | yes | `submitted`, `needs_more_evidence`, `open_under_review`, `driver_response_requested`, `customer_response_requested`, `resolved`, `rejected_invalid`, `escalated_fraud_review`, `closed` |
| `description` | text | yes |  |
| `qualifies_for_driver_auto_lock` | boolean | yes | default false |
| `duplicate_of_complaint_id` | uuid | no | FK self |
| `assigned_admin_id` | uuid | no | FK |
| `resolved_by_admin_id` | uuid | no | FK |
| `resolved_at` | timestamptz | no |  |
| `resolution_reason` | text | no |  |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Indexes:

- `idx_complaints_status_severity`.
- `idx_complaints_entity(service_type, entity_id)`.
- `idx_complaints_against_status(against_account_id, status)`.
- `idx_complaints_auto_lock(against_account_id, qualifies_for_driver_auto_lock, status)`.

## 15.2 `complaint_evidence`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `complaint_id` | uuid | yes | FK |
| `media_id` | uuid | no | FK |
| `source_type` | text | yes | `payment_proof`, `chat_message`, `uploaded_media`, `location_snapshot`, `state_event` |
| `source_entity_type` | text | no |  |
| `source_entity_id` | uuid | no |  |
| `added_by_account_id` | uuid | no | FK |
| `created_at` | timestamptz | yes |  |

## 15.3 `complaint_responses`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `complaint_id` | uuid | yes | FK |
| `responder_account_id` | uuid | yes | FK |
| `body_text` | text | yes |  |
| `created_at` | timestamptz | yes |  |

## 15.4 `driver_risk_actions`

Tracks manual/automatic lock/suspend/unlock decisions.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `driver_profile_id` | uuid | yes | FK |
| `action_type` | text | yes | `auto_lock`, `manual_lock`, `manual_unlock`, `suspend`, `block`, `mark_under_review` |
| `from_risk_status` | text | no |  |
| `to_risk_status` | text | yes |  |
| `source_type` | text | yes | `complaint_threshold`, `admin_action`, `fraud_case`, `system_policy` |
| `source_id` | uuid | no | Complaint/fraud id |
| `reason` | text | yes |  |
| `actor_type` | text | yes | `system`, `admin` |
| `actor_id` | uuid | no | Admin id if admin |
| `created_at` | timestamptz | yes |  |

Indexes:

- `idx_driver_risk_actions_driver_time(driver_profile_id, created_at DESC)`.

## 15.5 `fraud_cases`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `source_complaint_id` | uuid | no | FK |
| `subject_account_id` | uuid | yes | Account under review |
| `service_type` | text | no | `ride`, `food` |
| `entity_id` | uuid | no |  |
| `category` | text | yes | `payment_non_performance`, `fake_completion`, `fake_gps`, `fake_evidence`, `referral_fraud`, `collusion`, `other` |
| `status` | text | yes | `reported`, `triage`, `evidence_collection`, `response_requested`, `human_review`, `confirmed`, `rejected`, `appeal_requested`, `finalized` |
| `severity` | text | yes | `medium`, `high`, `critical` |
| `assigned_admin_id` | uuid | no | FK |
| `decision_admin_id` | uuid | no | FK |
| `decision_reason` | text | no |  |
| `decided_at` | timestamptz | no |  |
| `created_at` | timestamptz | yes |  |
| `updated_at` | timestamptz | yes |  |

Indexes:

- `idx_fraud_cases_subject_status`.
- `idx_fraud_cases_status_severity`.

## 15.6 `fraud_case_evidence`

Same shape as complaint evidence, linked to fraud case.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `fraud_case_id` | uuid | yes | FK |
| `media_id` | uuid | no | FK |
| `source_type` | text | yes |  |
| `source_entity_type` | text | no |  |
| `source_entity_id` | uuid | no |  |
| `created_at` | timestamptz | yes |  |

# 16. Rating va notification

## 16.1 `ratings`

Works for Ride/Food customer-driver ratings.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `service_type` | text | yes | `ride`, `food` |
| `entity_id` | uuid | yes | Ride/Food id |
| `rater_account_id` | uuid | yes | FK |
| `rated_account_id` | uuid | yes | FK |
| `score` | smallint | yes | 1-5 |
| `tags` | text[] | no |  |
| `comment` | text | no |  |
| `status` | text | yes | `submitted`, `hidden`, `removed` |
| `created_at` | timestamptz | yes |  |

Constraints:

- `CHECK(score BETWEEN 1 AND 5)`.
- `UNIQUE(service_type, entity_id, rater_account_id, rated_account_id)`.

## 16.2 `device_tokens`

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `account_id` | uuid | yes | FK |
| `platform` | text | yes | `ios`, `android`, `web` |
| `token` | text | yes | Unique |
| `status` | text | yes | `active`, `disabled` |
| `last_seen_at` | timestamptz | no |  |
| `created_at` | timestamptz | yes |  |

## 16.3 `notification_outbox`

Outbox for push/in-app/email/SMS jobs if needed.

| Column | Type | Required | Note |
|---|---|---:|---|
| `id` | uuid | yes | PK |
| `recipient_account_id` | uuid | yes | FK |
| `channel` | text | yes | `push`, `in_app`, `sms`, `email` |
| `template_key` | text | yes |  |
| `payload_json` | jsonb | yes |  |
| `status` | text | yes | `pending`, `sent`, `failed`, `cancelled` |
| `scheduled_at` | timestamptz | yes | default now |
| `sent_at` | timestamptz | no |  |
| `failure_reason` | text | no |  |
| `created_at` | timestamptz | yes |  |

Indexes:

- `idx_notification_outbox_pending(status, scheduled_at)`.

# 17. Key relationships

## 17.1 Identity

- `accounts 1-1 customer_profiles`
- `accounts 1-1 driver_profiles`
- `accounts 1-1 admin_profiles`
- `admin_profiles n-n admin_roles`

## 17.2 Driver

- `driver_profiles 1-n driver_vehicles`
- `driver_profiles 1-n driver_documents`
- `driver_profiles 1-n driver_service_eligibilities`
- `driver_profiles 1-n driver_payment_accounts`
- `driver_profiles 1-n driver_platform_fee_payments`
- `driver_profiles 1-n driver_risk_actions`

## 17.3 Region

- `countries 1-n cities`
- `cities 1-n regions`
- `regions 1-n region_service_configs`
- `regions 1-n region_vehicle_configs`
- `regions 1-n restaurant_outlets`
- `regions 1-n rides`
- `regions 1-n food_orders`

## 17.4 Catalog

- `restaurant_brands 1-n restaurant_outlets`
- `restaurant_brands 1-n menus`
- `menus 1-n menu_versions`
- `menu_versions 1-n menu_categories`
- `menu_versions 1-n menu_items`
- `menu_items n-n modifier_groups`
- `modifier_groups 1-n modifier_options`
- `restaurant_outlets n-1 active menu_version via outlet_menu_versions`
- `restaurant_outlets 1-n outlet_item_overrides`
- `restaurant_outlets 1-n outlet_modifier_option_overrides`

## 17.5 Ride/Food

- `rides 1-1 matching_sessions`
- `food_orders 1-1 matching_sessions`
- `matching_sessions 1-n matching_offers`
- `rides 1-1 direct_payment_records` per payment step
- `food_orders 1-1 direct_payment_records` per payment step
- `direct_payment_records 1-n payment_proofs`
- `direct_payment_records 1-n payment_confirmations`
- `rides/food_orders 1-1 chat_rooms`
- `rides/food_orders 1-n ratings`

## 17.6 Risk/support

- `complaints` can link to `rides` or `food_orders`.
- `complaints` can link evidence from payment proofs, chat, media, location snapshots, state events.
- `fraud_cases` can originate from complaints.
- `driver_risk_actions` links account restriction decisions to complaints/fraud/admin action.

# 18. Critical indexes

Required P0 indexes:

```sql
-- Geo
CREATE INDEX idx_regions_boundary_gist ON regions USING GIST (boundary);
CREATE INDEX idx_restaurant_outlets_location_gist ON restaurant_outlets USING GIST (location);
CREATE INDEX idx_rides_pickup_location_gist ON rides USING GIST (pickup_location);
CREATE INDEX idx_rides_dropoff_location_gist ON rides USING GIST (dropoff_location);
CREATE INDEX idx_food_orders_delivery_location_gist ON food_orders USING GIST (delivery_location);
CREATE INDEX idx_driver_location_snapshots_location_gist ON driver_location_snapshots USING GIST (location);

-- Matching/offers
CREATE INDEX idx_matching_sessions_status ON matching_sessions (status, started_at);
CREATE INDEX idx_matching_offers_driver_status ON matching_offers (driver_profile_id, status);
CREATE INDEX idx_matching_offers_session_status ON matching_offers (matching_session_id, status);
CREATE INDEX idx_matching_offers_expires_at ON matching_offers (expires_at);

-- Operational queues
CREATE INDEX idx_rides_region_status ON rides (region_id, status, created_at DESC);
CREATE INDEX idx_food_orders_region_status ON food_orders (region_id, status, created_at DESC);
CREATE INDEX idx_complaints_status_severity ON complaints (status, severity, created_at DESC);
CREATE INDEX idx_fraud_cases_status_severity ON fraud_cases (status, severity, created_at DESC);

-- Auto-lock query
CREATE INDEX idx_complaints_auto_lock
  ON complaints (against_account_id, qualifies_for_driver_auto_lock, status, created_at DESC);

-- Audit/timeline
CREATE INDEX idx_audit_logs_target ON audit_logs (target_type, target_id, created_at DESC);
CREATE INDEX idx_entity_state_events_entity ON entity_state_events (entity_type, entity_id, created_at DESC);
```

# 19. Important constraints va transaction rules

## 19.1 Matching atomic assignment

When driver accepts offer:

1. Begin transaction.
2. Lock matching session row.
3. Verify session still matchable.
4. Verify offer status is `sent` and not expired.
5. Verify driver still active/online/not locked/eligible.
6. Set winning offer `accepted`.
7. Set session `assigned`.
8. Set ride/food order assigned driver.
9. Cancel remaining offers.
10. Commit.
11. Emit realtime events.

## 19.2 Food purchase blocked before payment proof

Driver cannot transition Food order into:

- `driver_en_route_to_outlet`
- `driver_arrived_at_outlet`
- `ordering_with_restaurant`
- `restaurant_order_placed`

unless direct payment record has required state:

- minimum `proof_submitted`; or
- stronger `driver_confirmed_received` if policy requires.

## 19.3 Restaurant order placed changes cancellation responsibility

Once `food_orders.restaurant_order_placed_at IS NOT NULL`, customer cancellation must not be treated as Onway refund. Any financial resolution is direct/admin-mediated and belongs to dispute policy.

## 19.4 Driver auto-lock after 2 qualifying open complaints

When a complaint becomes qualifying:

1. Count non-duplicate open complaints against driver account with `qualifies_for_driver_auto_lock = true`.
2. If count >= policy threshold, create `driver_risk_actions` with `auto_lock`.
3. Update `driver_profiles.risk_status = temporarily_locked`.
4. Force driver offline in realtime layer.
5. Matching excludes driver from new offers.

## 19.5 Chat retention 1 week

Retention job:

1. Find `chat_rooms.retention_delete_after <= now()` and status not content deleted.
2. If no linked active complaint requires preservation, mark message content/media as retention-deleted.
3. Keep minimal metadata only if privacy/legal policy allows.
4. Write audit/system event.

# 20. P1/P2 tables not required for P0

The following should not block launch:

- Trust scoring tables.
- Mission templates/submissions/rewards.
- Community Truth field/evidence/confidence tables.
- AI extraction jobs.
- Advertising campaign/placement tables.
- Merchant app ownership/account tables.
- Wallet/payment gateway/settlement tables.

These can be added later through dedicated migrations after related PRDs are detailed.

# 21. Open technical decisions

1. ORM/migration tool is decided in Architecture ADR-037: Prisma as main database access layer, with controlled raw SQL for PostGIS and advanced PostgreSQL features. See `ONWAY_DB_MIGRATION_STRATEGY_P0_v0.1.md`.
2. Whether state values remain `text CHECK` or become PostgreSQL enum types.
3. Exact foreign key delete behavior: restrict vs soft delete.
4. Exact encryption strategy for bank account number, identity docs and sensitive metadata.
5. Exact retention duration for payment proof, driver documents, complaint evidence and audit logs.
6. Whether chat content deleted after 1 week keeps metadata or is hard-deleted.
7. Exact Ride payment timing and corresponding `required_before_event`.
8. Initial HCMC region polygons and seed data.
9. Money minor unit policy per currency; VND should use exponent `0`.
