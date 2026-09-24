# Gate Checklists

Không qua gate nếu checklist bắt buộc chưa pass hoặc chưa có assumption/open question rõ.

## G0 - Project Init

- [x] Project folder đã copy template.
- [x] `PROJECT_STATUS.md` có tên dự án/gate hiện tại.
- [x] `SDLC_CONFIG.md` có preset ban đầu hoặc TBD rõ.
- [x] User xác nhận chưa tạo code skeleton cố định.

## G1 - Business Discovery

- [x] App archetype tạm xác định.
- [x] User chính xác định.
- [x] Vấn đề/giá trị cốt lõi rõ.
- [x] Monetization tạm xác định hoặc ghi TBD.
- [x] Risk/open questions được ghi.

## G2 - BRD Freeze

- [x] `00-business-brief.md` đủ tóm tắt.
- [x] `02-scope.md` có in/out/later scope.
- [x] `03-personas.md` có persona chính.
- [x] `04-business-rules.md` có rule quan trọng.
- [x] `05-monetization.md` phù hợp config.
- [x] Decision log có quyết định đã chốt.
- [x] User review/chốt.

## G3 - PRD Freeze

- [x] Feature inventory đủ phase 1.
- [x] Screen inventory đủ platform phase 1.
- [x] Core user flows đủ success/error/edge.
- [x] Feature specs có AC.
- [x] Analytics events có nếu cần.
- [x] Permission matrix có nếu nhiều role/auth.
- [x] Release scope rõ.

## G4 - Technical Freeze

- [x] Stack đã chọn cho project này.
- [x] Architecture/module boundary rõ.
- [x] Data model/API/state đủ để break task.
- [x] Security/privacy/compliance có nếu cần.
- [x] Test strategy và test commands ban đầu được xác định trong `08-test-plan.md`.
- [x] Technical decisions được ghi.
- [x] Code skeleton path được quyết định nếu sẽ implement.

## G5 - Claude Design Handoff

- [ ] Design brief đủ audience/style/reference.
- [ ] Prompt Claude Design sẵn copy.
- [ ] Design system requirements rõ.
- [ ] Screen flow requirements map screen inventory.
- [ ] Design review checklist sẵn.
- [ ] Handoff yêu cầu rõ 2 deliverables: design system và UI workflow tất cả màn hình.
- [ ] Output contract cho Claude Design được đính kèm.
- [ ] Có bảng dự kiến map design system -> implementation tasks.
- [ ] Có bảng dự kiến map UI workflow/screen -> implementation tasks.

## G6 - Delivery Task Graph

- [ ] Claude Design output đã được import ngược vào `doc/4-DESIGN/system/` và `doc/4-DESIGN/mockups/`.
- [ ] Epic/story/task breakdown có ID ổn định.
- [ ] Dependency map không có cycle.
- [ ] Parallel plan có low/medium/high credit.
- [ ] Mỗi task code có test coverage expected.
- [ ] Có task implementation cho design system.
- [ ] Có task implementation cho UI workflow/screens.
- [ ] UI tasks phụ thuộc đúng DS/component tasks.
- [ ] Task status khởi tạo.
- [ ] ORCA task template sẵn.
- [ ] Traceability matrix map business -> task.

## G7 - ORCA Implementation Ready

- [ ] Task Ready không còn dependency blocker.
- [ ] Allowed/forbidden paths rõ.
- [ ] Schema/codegen permission rõ.
- [ ] Test requirements/DoD rõ.
- [ ] Progress tracking sẵn cập nhật.

## G8 - QA / Release

- [ ] Critical flows test pass.
- [ ] Automated test suite pass.
- [ ] Manual QA pass cho phần chưa automate.
- [ ] Test gaps được ghi rõ và chấp nhận.
- [ ] App Store/Google Play checklist pass nếu mobile.
- [ ] Compliance/privacy checklist pass.
- [ ] Monetization checklist pass nếu có ads/IAP/subscription.
- [ ] Release notes và known issues sẵn.
