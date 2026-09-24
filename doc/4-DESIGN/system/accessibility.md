# Accessibility

## Contrast (WCAG 2.1 AA)

| Cặp màu | Tỉ lệ | Dùng cho |
| --- | --- | --- |
| Trắng trên `#E22240` | 4.6:1 | CTA primary — đạt AA cho chữ ≥ 14px đậm |
| `#E22240` trên trắng | 4.6:1 | Chỉ logo và chữ đậm ≥ 14px; chữ lỗi dùng `red-600` `#C31834` (6.1:1) |
| `#2F2E2E` trên trắng | 13.6:1 | Logo, chữ |
| `ink-950` trên `ink-50` | 18:1 | Chữ chính |
| `ink-600` trên trắng | 7.4:1 | Chữ phụ |
| `ink-500` trên trắng | 4.5:1 | Chữ tertiary — tối thiểu, không dùng dưới 12px |
| Chữ semantic (`text-success/info/warning/danger`) trên nền `*-subtle` tương ứng | ≥ 4.5:1 | StatusPill, Banner |

Không dùng `ink-400` cho chữ cần đọc (chỉ cho disabled).

## Không chỉ dựa vào màu

- StatusPill: màu + hình (chấm / ✓ / ✕ / !) + nhãn chữ.
- Lỗi form: viền đỏ + icon + helper text.
- Timeline failed: marker vuông + chữ đỏ.
- Danger ≠ primary: primary là nền đỏ đặc; destructive là viền + chữ đỏ và luôn qua Dialog.

## Touch target

- Tối thiểu 44×44pt (iOS) / 48×48dp (Android) — token `--touch-target-min`.
- Nút Accept/Reject của tài xế (S-013, S-014) và xác nhận thanh toán: cao 56px (`--control-height-xl`), cách nhau ≥ 12px, không đặt sát mép home indicator.
- Bottom action bar cộng `env(safe-area-inset-bottom)`.

## Dynamic type & tiếng Việt

- Line-height không dưới 1.15 để không cắt dấu (ố, ữ, ặ).
- Nhãn trạng thái và nút phải xuống dòng hoặc co giãn khi cỡ chữ hệ thống 200%; không đặt chiều cao cố định cho vùng chứa chữ.
- Số tiền dùng JetBrains Mono, định dạng `48.000đ`.

## Reduced motion

Khi `prefers-reduced-motion: reduce`:

- Tắt pulse StatusPill, shimmer Skeleton, animation route/matching.
- Sheet/Dialog chỉ fade ≤ 140ms, không trượt.

## Screen reader

- IconButton luôn có `aria-label` tiếng Việt.
- Bản đồ `aria-hidden`; thông tin chuyến (tài xế, ETA, giá) phải có trong Sheet/JobStatusHeader.
- Thay đổi trạng thái chuyến thông báo qua `aria-live="polite"`; lỗi thanh toán `assertive`.
- Dialog: focus trap, Esc đóng, trả focus về phần tử mở.

## Bàn phím (Admin web)

- Mọi hành động đạt được bằng Tab; focus ring 2px trắng + 2px `ink-950`.
- DataTable: header sort là `<button>`, checkbox có nhãn.
- Region editor (S-017): các thao tác vẽ polygon có phím tắt và nút tương đương trên toolbar.
