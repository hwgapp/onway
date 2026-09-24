# Definition Of Done

Một task chỉ được Done khi:

- [ ] Scope đúng task, không mở rộng ngoài yêu cầu.
- [ ] Acceptance criteria pass.
- [ ] Test coverage phù hợp với risk đã được thêm/cập nhật.
- [ ] Tests/verification bắt buộc đã chạy và pass.
- [ ] Nếu không thể test tự động, có lý do rõ, manual QA steps và reviewer chấp nhận.
- [ ] Không phá source-of-truth/decision log.
- [ ] Task status đã cập nhật.
- [ ] Blocker/new decision được ghi vào file phù hợp.
- [ ] Completion report ngắn, có file path và test result.

## Coding DoD

Với task có code, mặc định phải có test. Không được coi là Done nếu chỉ implement mà không có verification.

- [ ] Logic/domain có unit test.
- [ ] API/repository/integration có integration test hoặc contract test phù hợp.
- [ ] UI/component có component/widget/snapshot/golden test phù hợp với stack.
- [ ] Critical user flow có E2E hoặc manual QA script nếu E2E chưa có hạ tầng.
- [ ] Regression bug fix phải có test tái hiện bug trước hoặc cùng lúc với fix.
- [ ] Error/empty/offline/permission/paywall states được test khi thuộc scope.
- [ ] Không giảm test coverage/quality bar nếu không được ghi rõ và chấp nhận.

## Product DoD

- [ ] Core flows pass.
- [ ] Loading/empty/error/offline states đủ.
- [ ] Test plan phase/release pass ở mức phù hợp.
- [ ] Analytics/compliance cần thiết đủ.
- [ ] Design review pass.
- [ ] Release checklist pass.
