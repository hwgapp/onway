# Permission Matrix

RBAC draft do Codex đề xuất ngày 2026-09-24. Mục tiêu là tách quyền vận hành đủ rõ cho P0 nhưng chưa làm quá phức tạp.

## Roles

| Role | Purpose | Notes |
| --- | --- | --- |
| Super Admin | Toàn quyền hệ thống, role/permission, policy nhạy cảm, emergency override | Ít người, bắt buộc audit |
| Ops Admin | Điều phối vận hành hằng ngày, rollout region/service, monitoring | Không quản lý role và không xem/sửa mọi dữ liệu tài chính nhạy cảm nếu không cần |
| Support Operator | Xử lý ticket/khiếu nại mức thường, xem thông tin cần thiết để hỗ trợ | Không tự quyết fraud/final liability |
| Driver Ops | Xác minh tài xế, hồ sơ, vehicle/service eligibility, activation/deactivation theo policy | Có thể đề xuất lock; lock nhạy cảm cần reason/audit |
| Catalog Manager | Quản lý Brand/Outlet/Menu/Modifier/Outlet override | Không truy cập KYC/payment proof nếu không cần |
| Finance Ops | Verify platform fee/subscription proof, refund records, payment reference cho khoản Onway thu | Không xử lý Ride/Food money vì Onway không giữ tiền giao dịch |
| Risk/Fraud Analyst | Review complaint/fraud, evidence, risk status, lock/unlock theo policy | Hành động nhạy cảm cần reason và audit |
| Viewer/Auditor | Xem dashboard, records, audit log | Read-only |

## Permissions

| Action | Super Admin | Ops Admin | Support Operator | Driver Ops | Catalog Manager | Finance Ops | Risk/Fraud Analyst | Viewer/Auditor | Requires Reason | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Manage admin users/roles | Yes | No | No | No | No | No | No | No | Yes | Super Admin only |
| View operations dashboard | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | Scope filters by role |
| Manage country/city/region/polygon | Yes | Yes | No | No | No | No | No | Read | Yes for publish | Draft/publish workflow recommended |
| Pause/resume service by region | Yes | Yes | No | No | No | No | No | Read | Yes | Emergency action audited |
| Manage pricing/policy config | Yes | Yes | No | No | No | No | No | Read | Yes | Sensitive config needs version/audit |
| Review customer profile | Yes | Yes | Yes | No | No | No | Yes | Read | No | Mask sensitive fields by default |
| Review driver profile | Yes | Yes | Yes | Yes | No | Finance limited | Yes | Read | No | KYC gated separately |
| View KYC/driver documents | Yes | No by default | No | Yes | No | No | Yes if case-linked | No | Yes | Super Admin and Driver Ops primary; Risk only when case-linked; signed URL, access audited |
| Approve/reject driver verification | Yes | No | No | Yes | No | No | No | No | Yes | Driver Ops primary |
| Activate/deactivate driver | Yes | Ops Admin limited | No | Yes by policy | No | No | Risk lock only | No | Yes | Deactivation/lock audited |
| Verify platform fee proof | Yes | No | No | No | No | Yes | No | No | Yes | Only Onway revenue proof |
| Manage brand/outlet/menu/catalog | Yes | Ops Admin limited | No | No | Yes | No | No | Read | Yes for publish | Food P0 admin-first |
| View Ride/Food monitoring | Yes | Yes | Yes | Driver scope | Catalog scope for Food issues | No | Yes | Read | No | Sensitive fields masked |
| View payment proof for Ride/Food | Yes | No by default | Case-linked only | No by default | No | No by default | Case-linked only | No | Yes | Super Admin can view; Support/Risk only when case-linked; Direct payment proof is sensitive evidence |
| Create/update complaint | Yes | Yes | Yes | No | No | No | Yes | Read | Yes | Complaint does not equal fraud |
| Create/update fraud case | Yes | No | Escalate only | No | No | No | Yes | Read | Yes | Human decision required |
| Set risk status / manual lock / auto-lock override | Yes | Emergency only | No | Propose only | No | No | Yes | No | Yes | Super Admin and Risk/Fraud unlock; Driver Ops can propose ops cases; auto-lock changes require reason, audit and review queue |
| Final fraud decision / appeal decision | Yes | No | No | No | No | No | Yes, with approval policy | Read | Yes | Consider dual-control later |
| View audit log | Yes | Yes | No | Own actions only | Own actions only | Own actions only | Yes | Yes | No | Audit log should be immutable |
| Export data | Yes | No | No | No | No | Finance scoped | Risk scoped | No | Yes | Needs privacy/legal control |
