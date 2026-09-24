Text field. Label always visible — never use a placeholder in place of a label.

- `state="error"` shows a red border + helper text, `aria-invalid` and `aria-describedby`; trigger it on blur or submit, not on every keystroke.
- `state="disabled"` uses `surface-sunken` fill and `text-disabled`.
- Focus uses a 1.5px `border-focus` outline (`border-width-strong`).
