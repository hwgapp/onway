# UI Workflow Package

Output UI Workflow cho P0 theo `../07-claude-design-output-contract.md` và `../08-full-app-screen-frame-map.md`.

- Canvas: [Onway UI Workflow](https://claude.ai/artifact/4cHL1pqQYuNLWsi2m2H44Y) — 216 frame, 371 trạng thái (Customer 68, Driver 60, Admin 77, Landing 11).
- `screen-map.md`: Frame ID → artboard, trạng thái đã vẽ.
- `flow-map.md`: UF-001…UF-007 và luồng phụ.
- `state-coverage.md`: default/loading/empty/error/offline/no permission/locked/success theo frame.
- `frame-export-notes.md`: quy ước export, asset, known gaps (DF-001…DF-008).
- `raw/`: `canvas.json`, `manifest.json` và `generator/` (nguồn sinh artboard từ token Onway).
