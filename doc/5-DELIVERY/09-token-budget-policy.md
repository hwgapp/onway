# Token Budget Policy

Mục tiêu: chạy nhiều project dài hạn nhưng không lãng phí token.

## Rules

- Task packet trỏ đến file/section, không paste tài liệu dài.
- Mỗi task đọc tối đa docs cần thiết.
- Nếu task cần đọc quá nhiều context, chia nhỏ.
- ORCA không tóm tắt lại toàn bộ dự án trong completion report.
- Mỗi folder có `README.md` để agent đọc index trước.
- Sau mỗi phase lớn, tạo summary ngắn nếu cần thay vì bắt task sau đọc lại lịch sử dài.

## Suggested Context Budget

| Size | Docs To Read | Files Expected | Notes |
| --- | ---: | ---: | --- |
| XS | 1-2 | 1-2 | Small fix/doc update |
| S | 2-3 | 2-5 | Normal task |
| M | 3-5 | 5-12 | Cohesive feature |
| L | 5-7 | 12+ | Prefer split |
| XL | N/A | N/A | Must decompose |

