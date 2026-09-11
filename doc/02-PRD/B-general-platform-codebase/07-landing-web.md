# PRD General: Landing Web

**Phase:** P1  
**Status:** Draft  
**Platform:** Next.js Landing Web  

## 1. Objective

Define the future Landing Web scope for public Onway information, app download conversion, and driver/merchant interest capture. This does not block MVP core launch.

## 2. Scope

Future Landing Web may include:

- Onway positioning.
- Ride/Food value proposition.
- App download CTA.
- Driver signup CTA.
- Merchant interest CTA.
- FAQ.
- Policy/legal links.
- Launch city coverage summary.

Out of scope for P0:

- Full CMS.
- SEO content engine.
- Merchant dashboard.
- Paid ads landing variations.

## 3. User Stories

### US-01 - Visitor understands Onway

As a visitor, I want to quickly understand what Onway offers so I can decide whether to download the app or sign up as driver.

Acceptance criteria:

- First viewport clearly identifies Onway and service category.
- CTAs for customer app and driver signup are visible.
- Copy does not imply unsupported features like COD/wallet.

### US-02 - Driver prospect can start signup

As a prospective driver, I want a clear path to download/open driver signup.

Acceptance criteria:

- Driver CTA routes to app download or signup interest flow.
- Platform fee/promotion claims match current policy.
- Legal disclaimers are accessible.

### US-03 - Merchant prospect can express interest

As a merchant, I want to register interest even though Merchant App is future.

Acceptance criteria:

- Form captures brand/outlet/contact basics if implemented.
- Messaging clearly says merchant integration is future/coming later when applicable.

## 4. Acceptance Tests

- Given Landing Web is deployed, when user opens on mobile, then app CTAs are visible without layout overlap.
- Given Onway MVP has no COD, when landing copy is scanned, then no COD promise appears.
- Given driver fee policy changes, when content is reviewed, then landing content can be updated without code-heavy release if CMS/config is chosen.

## 5. Dependencies

- Brand/content decisions.
- App store links.
- Driver signup flow decision.
- Legal/privacy pages.

## 6. Open Questions

- Exact landing content and brand style.
- Whether merchant interest form is needed before Merchant App.
- Whether landing deploys with same monorepo pipeline.

