# PRD: Gamification, XP, Level & Badge

**Phase:** P2  
**Status:** Draft  
**Platforms:** Driver App, Customer App, Admin Portal, API Core Backend  

## 1. Objective

Define future gamification concepts that motivate healthy participation without creating unsafe driving incentives or bypassing risk controls.

## 2. MVP Position

Gamification is not required for P0 launch. Trust and XP must remain separate.

## 3. Scope

Future scope:

- XP events.
- Levels.
- Badges.
- Mission rewards.
- Driver/customer referral recognition.
- Admin config.

Out of scope:

- Onway credits or money-like virtual currency unless separately approved.
- Leaderboards/streaks that encourage unsafe behavior.

## 4. User Stories

### US-01 - Driver earns XP for safe completed actions

As a driver, I want recognition for completed rides/orders and accepted contributions.

Acceptance criteria:

- XP event is tied to completed legitimate action.
- Fraud/reversed actions can remove or invalidate XP.
- XP does not increase Trust automatically.

### US-02 - Driver earns badge

As a driver, I want badges for meaningful milestones.

Acceptance criteria:

- Badge criteria are configurable.
- Badges do not unlock high-risk privileges by themselves.
- Unsafe driving incentives are disallowed.

### US-03 - Admin configures gamification

As admin, I want to configure XP values and badges.

Acceptance criteria:

- XP values are configurable.
- Changes are auditable.
- High-risk reward changes require permission.

## 5. Acceptance Tests

- Given ride completes legitimately, when XP event runs, then driver receives configured XP.
- Given fraud case reverses a mission reward, then XP/reward can be revoked according to policy.
- Given badge criteria encourages unrealistic trip count, when admin tries save, then policy review may block or warn.

## 6. Open Questions

- Exact XP values.
- Which badges launch first.
- Whether customers have gamification.

