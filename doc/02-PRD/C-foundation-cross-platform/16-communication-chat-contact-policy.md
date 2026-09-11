# PRD: Communication, Chat & Contact Policy

**Phase:** P0  
**Status:** Draft  
**Platforms:** Customer App, Driver App, Admin Portal, API Core Backend  

## 1. Objective

Enable customer-driver coordination through chat with text/image messages and define contact policy for direct communication.

## 2. Scope

In scope:

- Chat room per ride/order.
- Text messages.
- Image messages.
- Message delivery state.
- Admin/support visibility for dispute within retention window.
- Chat retention of 1 week.
- Direct phone contact policy if exposed.

Out of scope:

- Voice call inside app.
- Number masking.
- Group chat.
- Long-term chat archive.

## 3. Chat Room Lifecycle

Suggested states:

- `created`
- `active`
- `closed`
- `retention_pending`
- `content_deleted`

Room is created after driver assignment. Chat closes after ride/order completion/cancellation plus configured grace period.

## 4. User Stories

### US-01 - Customer sends driver a message

As a customer, I want to message the assigned driver so pickup/delivery coordination is easier.

Acceptance criteria:

- Chat is available only after driver assignment.
- Customer can send text.
- Driver receives realtime event.
- Message is stored with timestamp and sender.

### US-02 - Driver sends customer an image

As a driver, I want to send an image when restaurant/order/pickup context needs visual proof.

Acceptance criteria:

- Driver can send image in active room.
- Image has upload progress and failure state.
- Customer receives image in room.
- Image is visible to admin during retention window.

### US-03 - Admin reviews chat during dispute

As support admin, I want to review chat and images attached to a complaint while retained.

Acceptance criteria:

- Admin can access chat only for cases they are authorized to review.
- Chat view includes message timestamps, sender, image preview, and linked ride/order.
- Access is audited if policy requires.

## 5. Acceptance Tests

- Given no driver assigned, when customer opens chat, then chat is unavailable.
- Given active order room, when driver sends image, then customer receives it realtime.
- Given chat older than 1 week, when retention job runs, then content is deleted or processed according to retention policy.
- Given unrelated driver requests room, when API checks access, then request is denied.

## 6. Retention Requirement

- Chat text/image content retention: 1 week.
- Metadata retention after content deletion is an open decision for privacy/audit PRD.
- If complaint is filed before deletion, case evidence handling must preserve necessary evidence according to dispute policy.

## 7. Open Questions

- Exact image size/type/count limits.
- Whether user can report a chat message directly.
- Whether phone numbers are visible in MVP once chat exists.

