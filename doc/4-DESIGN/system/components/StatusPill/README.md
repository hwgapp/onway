Unified status display for ride, food, payment, driver, region and case — 34 keys across 6 tones. Anatomy: subtle-tone fill · mark (dot/✓/✕/!) · label.

- Map the backend status key straight to `status` — never invent a new color for a new state; add the key to the right tone group instead (see `tokens.json` / the system README's StatusPill section for the full 34-key map).
- `size="sm"` (22px) in dense admin tables, `size="md"` (26px) elsewhere.
- `pulse` only animates for `matching` and `searching`; it turns off automatically under reduced motion.
- Never use `StatusPill` as a filter control — use `Tag` for that.
