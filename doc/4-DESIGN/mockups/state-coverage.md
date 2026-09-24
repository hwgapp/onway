# State Coverage

Yes = có ít nhất một trạng thái tương ứng được vẽ trong artboard; — = không vẽ riêng (không áp dụng hoặc dùng mẫu chung A-069 / pattern của frame khác, xem Notes).

| Screen ID | Default | Loading | Empty | Error | Offline | No Permission | Paywall/Locked | Success | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-000 | Yes | Yes | — | — | — | — | Yes | — | Đang tải; Bắt buộc cập nhật |
| C-001 | Yes | — | — | Yes | — | — | Yes | — | Mặc định; Lỗi định dạng số; Giới hạn gửi mã |
| C-002 | Yes | — | — | Yes | — | — | — | — | Mặc định; Sai mã OTP; Chờ gửi lại mã |
| C-003 | Yes | — | — | Yes | — | — | — | — | Mặc định; Lỗi nhập liệu |
| C-004 | Yes | — | — | — | — | Yes | — | — | Giải thích quyền; Đã từ chối; Vị trí gần đúng |
| C-005 | Yes | — | — | — | — | Yes | — | — | Giải thích quyền; Đã từ chối |
| C-006 | Yes | Yes | — | — | Yes | — | — | — | Mặc định; Đang tải; Ngoài khu vực; Mất mạng |
| C-007 | Yes | — | Yes | — | — | — | Yes | — | Không có khu vực hoạt động; Dịch vụ tạm dừng |
| C-008 | Yes | — | Yes | — | — | — | — | — | Có chưa đọc; Trống |
| C-009 | Yes | — | — | — | — | — | — | — | Mặc định |
| C-010 | Yes | — | — | Yes | — | — | — | — | Mặc định; Lỗi nhập liệu |
| C-011 | Yes | — | — | — | — | — | — | — | Mặc định |
| C-012 | Yes | — | — | — | — | Yes | — | — | Mặc định; Chưa cấp quyền vị trí; Ngoài khu vực |
| C-013 | Yes | Yes | Yes | Yes | — | — | — | — | Kết quả tìm kiếm; Đang tìm; Không có kết quả; Lỗi |
| C-014 | Yes | Yes | Yes | — | — | — | — | — | Kết quả tìm kiếm; Đang tìm; Không có kết quả; Điểm đến ngoài vùng |
| C-015 | Yes | — | — | Yes | — | — | — | — | Mặc định; GPS yếu; Không lấy được địa chỉ |
| C-016 | Yes | — | — | — | — | — | — | — | Xe máy; Ô tô; Loại xe không khả dụng |
| C-017 | Yes | Yes | — | Yes | — | — | — | — | Mặc định; Đang tính lại tuyến; Không tính được giá |
| C-018 | Yes | — | — | — | — | — | — | — | Cảnh báo điểm đến ngoài vùng |
| C-019 | Yes | Yes | — | — | — | — | — | — | Đang ghép; Sắp hết giờ |
| C-020 | Yes | — | — | — | — | — | — | — | Tìm lượt tiếp theo |
| C-021 | Yes | — | Yes | — | — | — | — | — | Không có tài xế |
| C-022 | Yes | — | — | — | — | — | — | — | Xác nhận huỷ |
| C-023 | Yes | — | — | — | — | — | — | — | Đã có tài xế |
| C-024 | Yes | — | — | — | — | — | — | — | Thông tin chuyển khoản |
| C-025 | Yes | Yes | Yes | Yes | — | — | — | Yes | Chưa có ảnh; Đang tải lên; Tải lên thất bại; Đã gửi |
| C-026 | Yes | — | — | — | — | — | — | — | Cần bổ sung |
| C-027 | Yes | — | — | — | — | — | — | — | Đang tranh chấp |
| C-028 | Yes | — | — | — | Yes | — | — | — | Tài xế đang đến; Mất kết nối |
| C-029 | Yes | — | — | — | — | — | — | — | Chờ đón; Chưa thanh toán |
| C-030 | Yes | — | — | — | — | — | — | — | Đang trong chuyến |
| C-031 | Yes | — | — | — | — | — | — | Yes | Hoàn thành |
| C-032 | Yes | — | — | — | — | — | — | — | Chọn loại sự cố |
| C-033 | Yes | Yes | — | — | — | — | — | — | Mặc định; Đang tải; Ngoài khu vực |
| C-034 | Yes | — | Yes | Yes | — | — | — | — | Kết quả; Không có kết quả; Lỗi |
| C-035 | Yes | — | — | — | — | — | — | — | Mặc định; Quán đóng cửa; Món hết; Cảnh báo giá cũ |
| C-036 | Yes | — | — | — | — | — | — | — | Chọn số lượng; Món hết; Ghi chú giá |
| C-037 | Yes | — | — | — | — | — | — | — | Mặc định; Món hết; Giá thay đổi |
| C-038 | Yes | — | — | — | — | — | — | — | Tìm địa chỉ; Ghim trên bản đồ; Ngoài khu vực |
| C-039 | Yes | — | — | — | — | — | — | — | Mặc định |
| C-040 | Yes | Yes | — | — | — | — | — | — | Đang ghép; Sắp hết giờ |
| C-041 | Yes | — | Yes | — | — | — | — | — | Không có tài xế |
| C-042 | Yes | — | — | — | — | — | — | — | QR & thông tin chuyển khoản |
| C-043 | Yes | Yes | Yes | Yes | — | — | — | Yes | Chưa có ảnh; Đang tải lên; Tải lên thất bại; Đã gửi |
| C-044 | Yes | — | — | — | — | — | — | — | Cần bổ sung; Đang tranh chấp |
| C-045 | Yes | — | — | — | — | — | — | — | Đang đến quán |
| C-046 | Yes | — | — | — | — | — | — | — | Tại quán |
| C-047 | Yes | — | — | — | — | Yes | — | Yes | Chờ trả lời; Đã đồng ý; Đã từ chối |
| C-048 | Yes | — | — | — | — | — | — | — | Chuyển tiền bổ sung |
| C-049 | Yes | — | — | — | — | — | Yes | — | Hết thời gian trả lời |
| C-050 | Yes | — | — | — | — | — | — | — | Đang giao |
| C-051 | Yes | — | — | — | — | — | — | Yes | Đã giao |
| C-052 | Yes | — | — | — | — | — | — | — | 5 sao + thẻ nhanh |
| C-053 | Yes | — | — | Yes | — | — | — | — | Mặc định; Lỗi nhập liệu |
| C-054 | Yes | — | — | — | — | — | — | Yes | Đã gửi |
| C-055 | Yes | — | — | — | — | — | — | — | Văn bản, ảnh, đã xem |
| C-056 | Yes | — | — | Yes | — | — | — | — | Ảnh gửi lỗi |
| C-057 | Yes | — | — | — | Yes | — | — | — | Đang kết nối lại |
| C-058 | Yes | — | — | — | — | — | — | — | Chỉ đọc |
| C-059 | Yes | Yes | Yes | — | — | — | — | — | Danh sách; Lọc Đi xe; Đang tải; Trống |
| C-060 | Yes | — | — | — | — | — | — | Yes | Hoàn thành; Đã huỷ; Tranh chấp |
| C-061 | Yes | — | — | — | — | — | — | Yes | Đã giao; Đã huỷ; Tranh chấp |
| C-062 | Yes | — | Yes | — | — | — | — | — | Danh sách; Trống |
| C-063 | Yes | — | — | — | — | — | — | Yes | Đang xem xét; Đã kết luận |
| C-064 | Yes | — | — | — | — | — | Yes | — | Gọi tài xế / tổng đài; Không khả dụng |
| C-065 | Yes | — | — | — | — | — | — | — | Cảnh báo huỷ |
| C-066 | Yes | — | Yes | — | — | — | — | — | Danh sách; Sửa / xoá; Trống |
| C-067 | Yes | — | — | — | — | — | Yes | Yes | Tạo yêu cầu; Đã gửi; Bị hạn chế (pháp lý/audit) |
| D-000 | Yes | Yes | — | — | — | — | Yes | — | Đang tải; Bắt buộc cập nhật |
| D-001 | Yes | — | — | Yes | — | — | Yes | — | Mặc định; Lỗi định dạng số; Giới hạn gửi mã |
| D-002 | Yes | — | — | Yes | — | — | — | — | Mặc định; Sai mã OTP; Chờ gửi lại mã |
| D-003 | Yes | — | — | Yes | — | — | — | — | Mặc định; Lỗi nhập liệu |
| D-004 | Yes | — | — | — | — | — | — | — | Xe máy; Ô tô; Cả hai; Loại xe chưa mở |
| D-005 | Yes | Yes | — | — | — | — | — | — | Chưa đủ; Đang tải lên; Tải lên lỗi |
| D-006 | Yes | — | — | Yes | — | — | — | — | Mặt trước; Mặt sau; Chân dung; Bị từ chối |
| D-007 | Yes | — | — | Yes | — | — | — | — | Theo dịch vụ đã chọn; Bị từ chối |
| D-008 | Yes | — | — | Yes | — | — | — | — | Mặc định; Lỗi nhập liệu |
| D-009 | Yes | — | — | — | — | — | — | — | Chờ duyệt |
| D-010 | Yes | — | — | Yes | — | — | — | — | Bị từ chối |
| D-011 | Yes | — | — | — | — | — | — | Yes | Đã duyệt |
| D-012 | Yes | — | — | — | — | — | Yes | — | Chưa thanh toán; Hết hạn; Đang hoạt động |
| D-013 | Yes | Yes | Yes | Yes | — | — | — | Yes | Chưa có ảnh; Đang tải lên; Đã gửi; Bị từ chối |
| D-014 | Yes | — | — | — | — | — | — | Yes | Đang hiệu lực; Sắp hết hạn; Đã hết hạn |
| D-015 | Yes | — | Yes | — | — | — | — | — | Ngoại tuyến; Trực tuyến; Chưa có chuyến |
| D-016 | Yes | — | — | — | — | — | Yes | — | Mặc định; Khu vực tạm dừng; Bị khoá |
| D-017 | Yes | Yes | Yes | Yes | — | — | — | — | Danh sách; Đang tải; Trống; Lỗi |
| D-018 | Yes | — | — | — | — | — | Yes | — | Ngoài vùng hoạt động; Dịch vụ tạm dừng |
| D-019 | Yes | — | — | — | — | — | — | — | Đếm ngược 12 giây; Còn 3 giây |
| D-020 | Yes | — | — | — | — | — | — | Yes | Đã nhận chuyến |
| D-021 | Yes | — | — | — | — | Yes | Yes | — | Đã từ chối; Hết thời gian |
| D-022 | Yes | — | — | — | — | — | — | — | Đến điểm đón |
| D-023 | Yes | — | — | — | — | — | — | — | Chứng từ đã gửi |
| D-024 | Yes | — | — | — | — | — | — | — | Báo chưa nhận tiền |
| D-025 | Yes | — | — | — | — | — | — | — | Đến điểm đón; Đang chờ khách |
| D-026 | Yes | — | — | — | — | — | Yes | — | Bắt đầu bị khoá (chưa nhận tiền); Sẵn sàng bắt đầu |
| D-027 | Yes | — | — | — | — | — | — | — | Trong chuyến |
| D-028 | Yes | — | — | — | — | — | — | Yes | Hoàn thành |
| D-029 | Yes | — | — | — | — | — | — | — | Chọn lý do |
| D-030 | Yes | — | — | — | — | — | — | — | Đếm ngược |
| D-031 | Yes | — | — | — | — | — | — | — | Đi tới quán |
| D-032 | Yes | — | — | — | — | — | — | — | Kiểm tra chứng từ |
| D-033 | Yes | — | — | — | — | — | — | — | Báo chưa nhận tiền |
| D-034 | Yes | — | — | — | — | — | — | — | Danh sách món |
| D-035 | Yes | — | — | — | — | — | — | — | Giá khác |
| D-036 | Yes | — | — | — | — | — | — | — | Chờ 5 phút |
| D-037 | Yes | — | — | — | — | — | — | Yes | Khách đồng ý |
| D-038 | Yes | — | — | — | — | — | Yes | — | Khách từ chối; Hết thời gian |
| D-039 | Yes | — | — | — | — | — | — | — | Chờ tiền bổ sung |
| D-040 | Yes | — | — | — | — | — | — | — | Đã lấy món |
| D-041 | Yes | — | — | — | — | — | — | — | Đang giao |
| D-042 | Yes | — | — | — | — | — | — | Yes | Đã giao |
| D-043 | Yes | — | — | — | — | — | — | — | Quán đóng cửa; Không liên lạc được khách |
| D-044 | Yes | — | — | — | — | — | — | — | Văn bản, ảnh, đã xem |
| D-045 | Yes | — | — | Yes | — | — | — | — | Ảnh gửi lỗi |
| D-046 | Yes | — | — | — | Yes | — | — | — | Đang kết nối lại |
| D-047 | Yes | — | — | — | — | — | Yes | — | Bị khoá tạm |
| D-048 | Yes | — | — | — | — | — | — | Yes | Soạn kháng nghị; Đã gửi |
| D-049 | Yes | — | Yes | — | — | — | — | — | Danh sách; Trống |
| D-050 | Yes | — | — | — | — | — | Yes | — | Việc, thanh toán, chat, khoá |
| D-051 | Yes | — | — | — | — | — | — | — | Mặc định |
| D-052 | Yes | — | — | — | — | — | — | — | Mặc định |
| D-053 | Yes | — | Yes | — | — | — | — | — | Danh sách; Lọc Đi xe; Trống |
| D-054 | Yes | — | — | — | — | — | — | Yes | Hoàn thành; Đã huỷ; Tranh chấp |
| D-055 | Yes | — | Yes | — | — | — | — | — | Danh sách; Trống |
| D-056 | Yes | — | — | — | — | — | — | — | Yêu cầu phản hồi |
| D-057 | Yes | — | — | — | — | — | Yes | — | Gọi khách / tổng đài; Không khả dụng |
| D-058 | Yes | — | — | — | — | — | — | — | Xem & phóng to; Liên kết hết hạn |
| D-059 | Yes | — | — | — | — | — | — | — | Mặc định |
| A-000 | Yes | — | — | Yes | — | — | Yes | — | Mặc định; Sai thông tin; Bị khoá |
| A-001 | Yes | — | — | Yes | — | — | — | — | Mặc định; Lỗi |
| A-002 | Yes | — | — | — | — | — | — | — | Mở rộng; Thu gọn |
| A-003 | Yes | — | — | — | — | Yes | — | — | Không có quyền |
| A-004 | Yes | — | Yes | — | — | — | — | — | Có kết quả; Không có kết quả |
| A-005 | Yes | Yes | — | Yes | — | — | — | — | Mặc định; Đang tải; Lỗi |
| A-006 | Yes | — | — | — | — | — | — | — | Ride/Food & rủi ro |
| A-007 | Yes | — | Yes | — | — | — | — | — | Có việc tồn; Không có việc |
| A-008 | Yes | — | Yes | — | — | — | — | — | Danh sách; Trống |
| A-009 | Yes | — | Yes | — | — | — | — | — | Chưa có dữ liệu |
| A-010 | Yes | — | Yes | — | — | — | — | — | Active / Paused / Planned; Trống |
| A-011 | Yes | — | — | — | — | — | — | — | Xem thông tin & audit |
| A-012 | Yes | — | — | Yes | — | — | — | — | Mặc định; Lỗi trùng tên |
| A-013 | Yes | Yes | — | — | — | — | — | — | Bản nháp; Đang chọn vùng; Đang tải bản đồ |
| A-014 | Yes | — | — | — | — | — | — | Yes | Thêm điểm; Đã đóng hình |
| A-015 | Yes | — | — | Yes | — | — | — | — | Kéo đỉnh; Hình không hợp lệ |
| A-016 | Yes | — | — | — | — | — | — | — | Chặn xuất bản |
| A-017 | Yes | — | — | — | — | — | — | — | Đi xe/Đặt món · Xe máy/Ô tô |
| A-018 | Yes | — | — | — | — | — | — | — | Planned → Closed |
| A-019 | Yes | — | — | — | — | — | — | Yes | Xác nhận có lý do |
| A-020 | Yes | — | — | — | — | — | — | — | Bắt buộc lý do |
| A-021 | Yes | — | — | Yes | — | — | — | — | Xung đột phiên bản |
| A-022 | Yes | Yes | — | — | — | — | — | — | Bản nháp & đã xuất bản; Đang tải |
| A-023 | Yes | — | — | Yes | — | — | — | — | Mặc định; Lỗi guardrail |
| A-024 | Yes | — | — | Yes | — | — | — | — | Mặc định; Lỗi |
| A-025 | Yes | — | — | Yes | — | — | — | — | Mặc định; Lỗi |
| A-026 | Yes | — | — | Yes | — | — | — | — | Mặc định; Lỗi |
| A-027 | Yes | — | — | — | — | — | — | Yes | Xác nhận có lý do |
| A-028 | Yes | — | — | — | — | — | — | — | Người/thời gian/khác biệt |
| A-029 | Yes | — | — | — | — | — | Yes | — | Tất cả; Lọc chờ duyệt; Lọc đã khoá |
| A-030 | Yes | — | — | — | — | — | — | — | Hồ sơ, dịch vụ, giấy tờ |
| A-031 | Yes | — | — | — | — | — | — | — | Ảnh; PDF |
| A-032 | Yes | — | — | — | — | — | — | — | Từ chối có lý do; Duyệt có lý do |
| A-033 | Yes | — | — | — | — | — | — | — | Duyệt/từ chối |
| A-034 | Yes | — | — | — | — | — | — | — | Cờ dịch vụ/phương tiện |
| A-035 | Yes | — | — | — | — | — | — | — | Bắt buộc lý do |
| A-036 | Yes | — | — | — | — | — | — | — | SLA, lý do, mức độ |
| A-037 | Yes | — | — | — | — | — | — | — | Nội dung & bằng chứng |
| A-038 | Yes | — | — | — | — | Yes | — | Yes | Có quyền; Không đủ quyền |
| A-039 | Yes | — | — | — | — | — | — | — | Người/thời gian/hành động |
| A-040 | Yes | — | Yes | — | — | — | — | — | Danh sách; Tìm kiếm; Trống |
| A-041 | Yes | — | — | — | — | — | — | Yes | Bản nháp; Đã xuất bản |
| A-042 | Yes | — | — | — | — | — | — | — | Đóng / mở / thiếu dữ liệu |
| A-043 | Yes | — | — | — | — | — | — | — | Giờ, địa chỉ, vùng |
| A-044 | Yes | — | — | — | — | — | — | — | Thiếu giá, xung đột |
| A-045 | Yes | — | — | Yes | — | — | — | — | Lỗi nhập liệu |
| A-046 | Yes | — | — | — | — | — | — | — | Giá/trạng thái |
| A-047 | Yes | — | — | — | — | — | — | — | Trùng/xung đột |
| A-048 | Yes | — | — | — | — | — | — | — | Ghi chú nhập thủ công |
| A-049 | Yes | — | — | — | — | — | — | Yes | Xác nhận có lý do |
| A-050 | Yes | — | — | — | — | — | — | — | Tất cả; Lọc kháng nghị |
| A-051 | Yes | — | — | — | — | — | — | — | Đang xem xét |
| A-052 | Yes | — | — | — | — | — | — | — | Chứng từ thanh toán |
| A-053 | Yes | — | — | — | — | — | — | — | Bằng chứng mâu thuẫn |
| A-054 | Yes | — | — | — | — | — | — | — | Khách/tài xế, hạn |
| A-055 | Yes | — | — | — | — | — | — | — | Loại, mức độ, lý do |
| A-056 | Yes | — | — | — | — | — | — | — | Xác nhận; Bác bỏ |
| A-057 | Yes | — | — | — | — | — | — | — | Chấp nhận/bác kháng nghị |
| A-058 | Yes | — | — | — | — | — | — | — | Bất biến |
| A-059 | Yes | — | — | — | — | — | — | Yes | Đã kết luận |
| A-060 | Yes | — | — | — | — | Yes | Yes | — | Hết hạn — tải lại; Không có quyền |
| A-061 | Yes | — | Yes | — | — | — | — | — | Mặc định; Có bộ lọc; Trống |
| A-062 | Yes | — | — | — | — | — | — | — | Danh sách vai trò |
| A-063 | Yes | — | — | — | — | Yes | — | — | Ma trận quyền |
| A-064 | Yes | — | — | Yes | — | — | — | — | Mặc định; Lỗi thiếu lý do |
| A-065 | Yes | — | — | — | — | — | — | — | Trước / sau |
| A-066 | Yes | — | — | — | — | — | — | — | Ride/Food/rủi ro theo vùng |
| A-067 | Yes | — | — | Yes | — | — | — | — | Bình thường; Suy giảm |
| A-068 | Yes | — | — | — | — | — | — | — | Hồ sơ, thông báo, đăng xuất |
| A-069 | Yes | — | — | — | — | — | — | — | Mẫu trống / lỗi / đang tải |
| A-070 | Yes | — | — | — | — | — | — | — | Tất cả; Lọc chờ xác minh |
| A-071 | Yes | — | — | — | — | — | — | — | Duyệt/từ chối |
| A-072 | Yes | — | — | — | — | — | — | — | Tìm kiếm |
| A-073 | Yes | — | — | — | — | — | — | — | Lịch sử & khiếu nại |
| A-074 | Yes | — | — | — | — | — | Yes | — | Mẫu việc/thanh toán/chat/khoá |
| A-075 | Yes | — | — | — | — | — | — | — | Xuất/xoá, ngoại lệ |
| A-076 | Yes | — | — | — | — | — | — | — | Quyết định & audit |
| L-001 | Yes | — | — | — | — | — | — | — | Desktop; Mobile |
| L-002 | Yes | — | — | — | — | — | — | — | Đi xe + Đặt món |
| L-003 | Yes | — | — | — | — | — | — | — | 0% hoa hồng + gói ra mắt |
| L-004 | Yes | — | — | — | — | — | — | — | Chuyển khoản trực tiếp + chứng từ |
| L-005 | Yes | — | — | — | — | — | — | — | Mô hình kết nối, an toàn |
| L-006 | Yes | — | Yes | — | — | — | — | — | Có link tải; Chưa có link — waitlist |
| L-007 | Yes | — | — | — | — | — | — | — | Khách hàng; Tài xế |
| L-008 | Yes | — | — | — | — | — | — | — | Quyền riêng tư, điều khoản, liên hệ |
| L-009 | Yes | — | — | — | — | — | — | — | Khung nội dung pháp lý |
| L-010 | Yes | — | — | — | — | Yes | — | — | Khung nội dung quyền riêng tư |
| L-011 | Yes | — | — | — | — | — | — | — | Khách, tài xế, đối tác |
