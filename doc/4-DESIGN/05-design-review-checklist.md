# Design Review Checklist

## Product Fit

- [ ] Design đúng target user.
- [ ] Không thêm flow ngoài PRD.
- [ ] Các CTA chính rõ.
- [ ] Có state loading/empty/error/offline/no permission/paywall khi phù hợp.

## Design System

- [ ] Có token màu/chữ/spacing/radius/motion.
- [ ] Logo Onway dùng đúng asset nguồn `logo.svg`/`logo.png`, không méo/crop/sai màu.
- [ ] Có hướng dẫn clear space, minimum size, light/dark usage, monochrome/fallback cho logo.
- [ ] Có compact symbol/app icon candidate phù hợp kích thước nhỏ.
- [ ] Có component inventory.
- [ ] Component có variants/states.
- [ ] Text không overflow trên mobile.
- [ ] Component map được sang implementation tasks.

## Handoff

- [ ] Frame/screen name map được với screen inventory.
- [ ] Mockup không mâu thuẫn business rule.
- [ ] Assets/font/icon cần dùng được liệt kê.
- [ ] Brand asset map rõ logo dùng ở splash/login/header/sidebar/landing/app icon/favicons.
- [ ] Có đủ UI workflow cho tất cả màn hình phase hiện tại.
- [ ] Mỗi flow có success/error/edge state cần thiết.
- [ ] Có bảng map Design System -> implementation tasks.
- [ ] Có bảng map Screen/Flow -> implementation tasks.

## Output Contract

- [ ] Design System Package có đủ required files hoặc bản tóm tắt tương đương.
- [ ] UI Workflow Package có `screen-map`, `flow-map`, `state-coverage`.
- [ ] Component ID và Screen ID ổn định.
- [ ] Raw artifact được lưu hoặc reference rõ.
- [ ] Design output đã được import ngược vào `system/` và `mockups/`.
- [ ] Traceability matrix đã cập nhật DS/UI mapping.
