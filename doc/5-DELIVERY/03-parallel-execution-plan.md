# Parallel Execution Plan

## Concurrency Modes

| Mode | ORCA Tasks | Rule |
| --- | ---: | --- |
| Low Credit | 1 | Chạy critical path tuần tự |
| Medium Credit | 2-3 | 1 backend + 1 UI + 1 docs/test nếu không conflict |
| High Credit | 4-8 | Tách lane rõ, dùng ownership nghiêm |

## Cannot Run Together

| Task A | Task B | Reason |
| --- | --- | --- |
| TBD | TBD | Shared schema/path conflict |

## Design/UI Parallel Rules

- Design system token/theme task phải chạy trước phần lớn UI screen tasks.
- Component implementation có thể chạy song song theo nhóm component nếu allowed paths không conflict.
- UI flow/screen tasks có thể chạy song song sau khi shell/navigation và component contract đủ ổn định.
- Không chạy song song nhiều task cùng sửa một screen hoặc một shared component nếu chưa có owner rõ.
- UI mock task có thể chạy song song backend nếu dùng mock data/contract.

## Merge Order

1. TBD
