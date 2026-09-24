Persistent inline notice — offline, unsupported region, no permission, error.

- Variants: `info`, `success`, `warning`, `danger`, `offline` (inverse fill), `locked` (sunken fill).
- At most one `Banner` per region of the screen; its action is a single text link. A temporary notice uses `Toast` instead.
- `offline` self-hides once the connection returns and offers "Thử lại"; `warning`/region-unavailable blocks the booking CTA; `danger` uses `role="alert"`.
