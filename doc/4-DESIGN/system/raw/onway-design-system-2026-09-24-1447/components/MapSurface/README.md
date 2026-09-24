Map background for every location screen (S-002…S-004, S-007, S-008, S-012…S-014, S-017) — this preview is a placeholder built from the `map.*` tokens only; production wires a HERE tile layer to the same land/block/park/water/road tokens.

- `variant="route"`: 5px route line (`map-route`, white casing), pickup dot (`map-pin-pickup`), drop-off pin (`map-pin-dropoff`).
- `variant="region"`: polygon fill/stroke from `map-region-*` — dashed = active, solid red = selected, amber = paused, dotted red = invalid/overlap.
- Full-bleed on mobile; UI floating over it uses `surface-card` + `shadow-md`, never a flat color wash over the map itself.
- `aria-hidden` — ride/trip facts belong in `Sheet` / `JobStatusHeader`, never only on the map.
