Primary action control, five variants and five states. One `primary` button per screen — it is the only surface allowed the solid brand red.

- Use `primary` for the one main action on a screen (`action-primary-bg`); `secondary` (`action-secondary-bg`, near-black) for a strong secondary action; `outline`/`ghost` for lower-emphasis actions; `destructive` only for actions that also open a confirm `Dialog`.
- Height is `control-height-lg` (48px) on mobile, `control-height-md` (40px) on web — pass `size`.
- `loading` disables the button, keeps its width, shows a spinner and sets `aria-busy` (announce "Đang xử lý"); block repeat submits.
- `disabled` uses `action-disabled-bg`/`action-disabled-text` and sets `aria-disabled` with a reason nearby — never disable without explanation.
- `destructive` never fires directly: always route through `Dialog` with a required reason field.
