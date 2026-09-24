# Review Checklist

## Code Review

- [ ] Đúng scope task.
- [ ] Không hard-code business rule đã có config/contract.
- [ ] Không duplicate constants/status.
- [ ] Error/edge case rõ.
- [ ] Tests đầy đủ so với risk và test requirements của task.
- [ ] Bug fix có regression test.
- [ ] Không bỏ qua failing/flaky tests nếu chưa có lý do và owner.

## Product Review

- [ ] Flow đúng PRD.
- [ ] Copy/text đúng terminology.
- [ ] State đủ.
- [ ] Monetization/paywall/ads đúng config nếu có.

## Documentation Review

- [ ] Docs liên quan được cập nhật.
- [ ] Decision mới được ghi.
- [ ] Task status/progress được cập nhật.

## Test Review

- [ ] Unit tests cover domain/logic quan trọng.
- [ ] Integration/contract tests cover API/data boundaries.
- [ ] UI tests cover variants/states quan trọng.
- [ ] Critical flow có E2E hoặc manual QA script.
- [ ] Test gaps được ghi rõ trong completion report.
