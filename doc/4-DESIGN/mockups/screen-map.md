# Screen Map

Canvas (Design artifact, private — chia sẻ từ menu Share của trang): [Customer & Driver](https://claude.ai/artifact/4cHL1pqQYuNLWsi2m2H44Y) và [Admin & Landing](https://claude.ai/artifact/CxkTKZioRmXx1xWKrzYf79); mỗi canvas tối đa 200 file nên tách làm hai. Mỗi `Frame ID` là một artboard; các trạng thái nằm cạnh nhau trong artboard, có nhãn trạng thái phía trên.

Tên export theo `07-claude-design-output-contract.md`: `<Frame ID> - <Frame Name> - <State> - <Platform>`.

| Frame ID | PRD Screen | Frame Name | Frame/Mockup Name | Canvas | Platform | Flow ID | States Delivered | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-000 | Common | Splash / launch | `C-000 - Splash / launch - iPhone` · `C-000.dc.html` | Customer & Driver | iPhone | App start | Đang tải, Bắt buộc cập nhật | Ready |
| C-001 | F-001 | Phone login | `C-001 - Phone login - iPhone` · `C-001.dc.html` | Customer & Driver | iPhone | Auth | Mặc định, Lỗi định dạng số, Giới hạn gửi mã | Ready |
| C-002 | F-001 | OTP verification | `C-002 - OTP verification - iPhone` · `C-002.dc.html` | Customer & Driver | iPhone | Auth | Mặc định, Sai mã OTP, Chờ gửi lại mã | Ready |
| C-003 | F-001 | Basic profile setup | `C-003 - Basic profile setup - iPhone` · `C-003.dc.html` | Customer & Driver | iPhone | Auth | Mặc định, Lỗi nhập liệu | Ready |
| C-004 | Common | Location permission | `C-004 - Location permission - iPhone` · `C-004.dc.html` | Customer & Driver | iPhone | App start | Giải thích quyền, Đã từ chối, Vị trí gần đúng | Ready |
| C-005 | Common | Notification permission | `C-005 - Notification permission - iPhone` · `C-005.dc.html` | Customer & Driver | iPhone | App start | Giải thích quyền, Đã từ chối | Ready |
| C-006 | S-001 | Home / service selector | `C-006 - Home / service selector - iPhone` · `C-006.dc.html` | Customer & Driver | iPhone | UF-001, UF-002 | Mặc định, Đang tải, Ngoài khu vực, Mất mạng | Ready |
| C-007 | S-001 | Home search/service empty | `C-007 - Home search/service empty - iPhone` · `C-007.dc.html` | Customer & Driver | iPhone | UF-001, UF-002 | Không có khu vực hoạt động, Dịch vụ tạm dừng | Ready |
| C-008 | Common | Notification center | `C-008 - Notification center - iPhone` · `C-008.dc.html` | Customer & Driver | iPhone | Push baseline | Có chưa đọc, Trống | Ready |
| C-009 | Common | Account / settings | `C-009 - Account / settings - iPhone` · `C-009.dc.html` | Customer & Driver | iPhone | Account | Mặc định | Ready |
| C-010 | Common | Profile and phone visibility settings | `C-010 - Profile and phone visibility settings - iPhone` · `C-010.dc.html` | Customer & Driver | iPhone | Account | Mặc định, Lỗi nhập liệu | Ready |
| C-011 | Common | Privacy / consent settings | `C-011 - Privacy / consent settings - iPhone` · `C-011.dc.html` | Customer & Driver | iPhone | Account | Mặc định | Ready |
| C-012 | S-002 | Ride request map | `C-012 - Ride request map - iPhone` · `C-012.dc.html` | Customer & Driver | iPhone | UF-001 | Mặc định, Chưa cấp quyền vị trí, Ngoài khu vực | Ready |
| C-013 | S-002 | Pickup address search | `C-013 - Pickup address search - iPhone` · `C-013.dc.html` | Customer & Driver | iPhone | UF-001 | Kết quả tìm kiếm, Đang tìm, Không có kết quả, Lỗi | Ready |
| C-014 | S-002 | Dropoff address search | `C-014 - Dropoff address search - iPhone` · `C-014.dc.html` | Customer & Driver | iPhone | UF-001 | Kết quả tìm kiếm, Đang tìm, Không có kết quả, Điểm đến ngoài vùng | Ready |
| C-015 | S-002 | Map pin adjust pickup/dropoff | `C-015 - Map pin adjust pickup/dropoff - iPhone` · `C-015.dc.html` | Customer & Driver | iPhone | UF-001 | Mặc định, GPS yếu, Không lấy được địa chỉ | Ready |
| C-016 | S-002 | Vehicle type selection | `C-016 - Vehicle type selection - iPhone` · `C-016.dc.html` | Customer & Driver | iPhone | UF-001 | Xe máy, Ô tô, Loại xe không khả dụng | Ready |
| C-017 | S-002 | Ride price review | `C-017 - Ride price review - iPhone` · `C-017.dc.html` | Customer & Driver | iPhone | UF-001 | Mặc định, Đang tính lại tuyến, Không tính được giá | Ready |
| C-018 | S-002 | Destination outside polygon warning | `C-018 - Destination outside polygon warning - iPhone` · `C-018.dc.html` | Customer & Driver | iPhone | UF-001 | Cảnh báo điểm đến ngoài vùng | Ready |
| C-019 | S-003 | Ride matching | `C-019 - Ride matching - iPhone` · `C-019.dc.html` | Customer & Driver | iPhone | UF-001 | Đang ghép, Sắp hết giờ | Ready |
| C-020 | S-003 | Driver rejected / searching next | `C-020 - Driver rejected / searching next - iPhone` · `C-020.dc.html` | Customer & Driver | iPhone | UF-001 | Tìm lượt tiếp theo | Ready |
| C-021 | S-003 | No driver found | `C-021 - No driver found - iPhone` · `C-021.dc.html` | Customer & Driver | iPhone | UF-001 | Không có tài xế | Ready |
| C-022 | S-003 | Ride cancel before match | `C-022 - Ride cancel before match - iPhone` · `C-022.dc.html` | Customer & Driver | iPhone | UF-001 | Xác nhận huỷ | Ready |
| C-023 | S-004 | Matched ride / driver assigned | `C-023 - Matched ride / driver assigned - iPhone` · `C-023.dc.html` | Customer & Driver | iPhone | UF-001 | Đã có tài xế | Ready |
| C-024 | S-004 | Ride payment instructions | `C-024 - Ride payment instructions - iPhone` · `C-024.dc.html` | Customer & Driver | iPhone | UF-001 | Thông tin chuyển khoản | Ready |
| C-025 | S-004 | Ride proof upload | `C-025 - Ride proof upload - iPhone` · `C-025.dc.html` | Customer & Driver | iPhone | UF-001 | Chưa có ảnh, Đang tải lên, Tải lên thất bại, Đã gửi | Ready |
| C-026 | S-004 | Ride proof rejected / supplement needed | `C-026 - Ride proof rejected / supplement needed - iPhone` · `C-026.dc.html` | Customer & Driver | iPhone | UF-001 | Cần bổ sung | Ready |
| C-027 | S-004 | Ride payment disputed | `C-027 - Ride payment disputed - iPhone` · `C-027.dc.html` | Customer & Driver | iPhone | UF-001 | Đang tranh chấp | Ready |
| C-028 | S-004 | Active ride - driver en route | `C-028 - Active ride - driver en route - iPhone` · `C-028.dc.html` | Customer & Driver | iPhone | UF-001 | Tài xế đang đến, Mất kết nối | Ready |
| C-029 | S-004 | Active ride - driver arrived | `C-029 - Active ride - driver arrived - iPhone` · `C-029.dc.html` | Customer & Driver | iPhone | UF-001 | Chờ đón, Chưa thanh toán | Ready |
| C-030 | S-004 | Active ride - in trip | `C-030 - Active ride - in trip - iPhone` · `C-030.dc.html` | Customer & Driver | iPhone | UF-001 | Đang trong chuyến | Ready |
| C-031 | S-004 | Ride completed summary | `C-031 - Ride completed summary - iPhone` · `C-031.dc.html` | Customer & Driver | iPhone | UF-001 | Hoàn thành | Ready |
| C-032 | S-004 | Ride issue/report entry | `C-032 - Ride issue/report entry - iPhone` · `C-032.dc.html` | Customer & Driver | iPhone | UF-005 | Chọn loại sự cố | Ready |
| C-033 | S-005 | Food browse home | `C-033 - Food browse home - iPhone` · `C-033.dc.html` | Customer & Driver | iPhone | UF-002 | Mặc định, Đang tải, Ngoài khu vực | Ready |
| C-034 | S-005 | Food outlet/brand search | `C-034 - Food outlet/brand search - iPhone` · `C-034.dc.html` | Customer & Driver | iPhone | UF-002 | Kết quả, Không có kết quả, Lỗi | Ready |
| C-035 | S-005 | Outlet menu | `C-035 - Outlet menu - iPhone` · `C-035.dc.html` | Customer & Driver | iPhone | UF-002 | Mặc định, Quán đóng cửa, Món hết, Cảnh báo giá cũ | Ready |
| C-036 | S-005 | Menu item detail | `C-036 - Menu item detail - iPhone` · `C-036.dc.html` | Customer & Driver | iPhone | UF-002 | Chọn số lượng, Món hết, Ghi chú giá | Ready |
| C-037 | S-006 | Food cart | `C-037 - Food cart - iPhone` · `C-037.dc.html` | Customer & Driver | iPhone | UF-002 | Mặc định, Món hết, Giá thay đổi | Ready |
| C-038 | S-006 | Delivery address selection | `C-038 - Delivery address selection - iPhone` · `C-038.dc.html` | Customer & Driver | iPhone | UF-002 | Tìm địa chỉ, Ghim trên bản đồ, Ngoài khu vực | Ready |
| C-039 | S-006 | Food checkout price review | `C-039 - Food checkout price review - iPhone` · `C-039.dc.html` | Customer & Driver | iPhone | UF-002 | Mặc định | Ready |
| C-040 | S-007 | Food matching | `C-040 - Food matching - iPhone` · `C-040.dc.html` | Customer & Driver | iPhone | UF-002 | Đang ghép, Sắp hết giờ | Ready |
| C-041 | S-007 | No Food driver found | `C-041 - No Food driver found - iPhone` · `C-041.dc.html` | Customer & Driver | iPhone | UF-002 | Không có tài xế | Ready |
| C-042 | S-007 | Food driver matched / payment instructions | `C-042 - Food driver matched / payment instructions - iPhone` · `C-042.dc.html` | Customer & Driver | iPhone | UF-002 | QR & thông tin chuyển khoản | Ready |
| C-043 | S-007 | Food proof upload | `C-043 - Food proof upload - iPhone` · `C-043.dc.html` | Customer & Driver | iPhone | UF-002 | Chưa có ảnh, Đang tải lên, Tải lên thất bại, Đã gửi | Ready |
| C-044 | S-007 | Food proof rejected / disputed | `C-044 - Food proof rejected / disputed - iPhone` · `C-044.dc.html` | Customer & Driver | iPhone | UF-002 | Cần bổ sung, Đang tranh chấp | Ready |
| C-045 | S-008 | Active Food - driver going to outlet | `C-045 - Active Food - driver going to outlet - iPhone` · `C-045.dc.html` | Customer & Driver | iPhone | UF-002 | Đang đến quán | Ready |
| C-046 | S-008 | Active Food - driver at outlet | `C-046 - Active Food - driver at outlet - iPhone` · `C-046.dc.html` | Customer & Driver | iPhone | UF-002 | Tại quán | Ready |
| C-047 | S-008 | Food change proposal | `C-047 - Food change proposal - iPhone` · `C-047.dc.html` | Customer & Driver | iPhone | UF-003 | Chờ trả lời, Đã đồng ý, Đã từ chối | Ready |
| C-048 | S-008 | Supplemental payment required | `C-048 - Supplemental payment required - iPhone` · `C-048.dc.html` | Customer & Driver | iPhone | UF-003 | Chuyển tiền bổ sung | Ready |
| C-049 | S-008 | Food proposal timeout | `C-049 - Food proposal timeout - iPhone` · `C-049.dc.html` | Customer & Driver | iPhone | UF-003 | Hết thời gian trả lời | Ready |
| C-050 | S-008 | Active Food - delivering | `C-050 - Active Food - delivering - iPhone` · `C-050.dc.html` | Customer & Driver | iPhone | UF-002 | Đang giao | Ready |
| C-051 | S-008 | Food delivered summary | `C-051 - Food delivered summary - iPhone` · `C-051.dc.html` | Customer & Driver | iPhone | UF-002 | Đã giao | Ready |
| C-052 | S-009 | Rating after Ride/Food | `C-052 - Rating after Ride/Food - iPhone` · `C-052.dc.html` | Customer & Driver | iPhone | UF-001, UF-002 | 5 sao + thẻ nhanh | Ready |
| C-053 | S-009 | Complaint/report form | `C-053 - Complaint/report form - iPhone` · `C-053.dc.html` | Customer & Driver | iPhone | UF-005 | Mặc định, Lỗi nhập liệu | Ready |
| C-054 | S-009 | Complaint submitted | `C-054 - Complaint submitted - iPhone` · `C-054.dc.html` | Customer & Driver | iPhone | UF-005 | Đã gửi | Ready |
| C-055 | S-015 | Chat room | `C-055 - Chat room - iPhone` · `C-055.dc.html` | Customer & Driver | iPhone | UF-007 | Văn bản, ảnh, đã xem | Ready |
| C-056 | S-015 | Chat image upload failed | `C-056 - Chat image upload failed - iPhone` · `C-056.dc.html` | Customer & Driver | iPhone | UF-007 | Ảnh gửi lỗi | Ready |
| C-057 | S-015 | Chat offline / reconnecting | `C-057 - Chat offline / reconnecting - iPhone` · `C-057.dc.html` | Customer & Driver | iPhone | UF-007 | Đang kết nối lại | Ready |
| C-058 | S-015 | Chat closed / retention expired | `C-058 - Chat closed / retention expired - iPhone` · `C-058.dc.html` | Customer & Driver | iPhone | UF-007 | Chỉ đọc | Ready |
| C-059 | Common | Activity / Ride & Food history | `C-059 - Activity / Ride & Food history - iPhone` · `C-059.dc.html` | Customer & Driver | iPhone | Account, UF-001, UF-002 | Danh sách, Lọc Đi xe, Đang tải, Trống | Ready |
| C-060 | Common | Ride history detail | `C-060 - Ride history detail - iPhone` · `C-060.dc.html` | Customer & Driver | iPhone | UF-001, UF-005 | Hoàn thành, Đã huỷ, Tranh chấp | Ready |
| C-061 | Common | Food order history detail | `C-061 - Food order history detail - iPhone` · `C-061.dc.html` | Customer & Driver | iPhone | UF-002, UF-005 | Đã giao, Đã huỷ, Tranh chấp | Ready |
| C-062 | Common | Case / complaint list | `C-062 - Case / complaint list - iPhone` · `C-062.dc.html` | Customer & Driver | iPhone | UF-005 | Danh sách, Trống | Ready |
| C-063 | Common | Case / complaint detail | `C-063 - Case / complaint detail - iPhone` · `C-063.dc.html` | Customer & Driver | iPhone | UF-005 | Đang xem xét, Đã kết luận | Ready |
| C-064 | Common | Direct call confirmation | `C-064 - Direct call confirmation - iPhone` · `C-064.dc.html` | Customer & Driver | iPhone | UF-001, UF-002, UF-007 | Gọi tài xế / tổng đài, Không khả dụng | Ready |
| C-065 | S-008 | Food customer cancel after driver ordered | `C-065 - Food customer cancel after driver ordered - iPhone` · `C-065.dc.html` | Customer & Driver | iPhone | F-018 | Cảnh báo huỷ | Ready |
| C-066 | Common | Saved places / recent addresses | `C-066 - Saved places / recent addresses - iPhone` · `C-066.dc.html` | Customer & Driver | iPhone | UF-001, UF-002 | Danh sách, Sửa / xoá, Trống | Ready |
| C-067 | Common | Data export/delete request | `C-067 - Data export/delete request - iPhone` · `C-067.dc.html` | Customer & Driver | iPhone | Privacy | Tạo yêu cầu, Đã gửi, Bị hạn chế (pháp lý/audit) | Ready |
| D-000 | Common | Splash / launch | `D-000 - Splash / launch - iPhone` · `D-000.dc.html` | Customer & Driver | iPhone | App start | Đang tải, Bắt buộc cập nhật | Ready |
| D-001 | F-001 | Phone login | `D-001 - Phone login - iPhone` · `D-001.dc.html` | Customer & Driver | iPhone | Auth | Mặc định, Lỗi định dạng số, Giới hạn gửi mã | Ready |
| D-002 | F-001 | OTP verification | `D-002 - OTP verification - iPhone` · `D-002.dc.html` | Customer & Driver | iPhone | Auth | Mặc định, Sai mã OTP, Chờ gửi lại mã | Ready |
| D-003 | S-010 | Driver profile setup | `D-003 - Driver profile setup - iPhone` · `D-003.dc.html` | Customer & Driver | iPhone | UF-004 | Mặc định, Lỗi nhập liệu | Ready |
| D-004 | S-010 | Service / vehicle selection | `D-004 - Service / vehicle selection - iPhone` · `D-004.dc.html` | Customer & Driver | iPhone | UF-004 | Xe máy, Ô tô, Cả hai, Loại xe chưa mở | Ready |
| D-005 | S-010 | Document upload checklist | `D-005 - Document upload checklist - iPhone` · `D-005.dc.html` | Customer & Driver | iPhone | UF-004 | Chưa đủ, Đang tải lên, Tải lên lỗi | Ready |
| D-006 | S-010 | Identity document capture | `D-006 - Identity document capture - iPhone` · `D-006.dc.html` | Customer & Driver | iPhone | UF-004 | Mặt trước, Mặt sau, Chân dung, Bị từ chối | Ready |
| D-007 | S-010 | Vehicle document upload | `D-007 - Vehicle document upload - iPhone` · `D-007.dc.html` | Customer & Driver | iPhone | UF-004 | Theo dịch vụ đã chọn, Bị từ chối | Ready |
| D-008 | S-010 | Bank/QR receiving info setup | `D-008 - Bank/QR receiving info setup - iPhone` · `D-008.dc.html` | Customer & Driver | iPhone | UF-004 | Mặc định, Lỗi nhập liệu | Ready |
| D-009 | S-010 | Onboarding review pending | `D-009 - Onboarding review pending - iPhone` · `D-009.dc.html` | Customer & Driver | iPhone | UF-004 | Chờ duyệt | Ready |
| D-010 | S-010 | Onboarding rejected | `D-010 - Onboarding rejected - iPhone` · `D-010.dc.html` | Customer & Driver | iPhone | UF-004 | Bị từ chối | Ready |
| D-011 | S-010 | Onboarding approved | `D-011 - Onboarding approved - iPhone` · `D-011.dc.html` | Customer & Driver | iPhone | UF-004 | Đã duyệt | Ready |
| D-012 | S-011 | Platform fee package | `D-012 - Platform fee package - iPhone` · `D-012.dc.html` | Customer & Driver | iPhone | UF-004 | Chưa thanh toán, Hết hạn, Đang hoạt động | Ready |
| D-013 | S-011 | Platform fee proof upload | `D-013 - Platform fee proof upload - iPhone` · `D-013.dc.html` | Customer & Driver | iPhone | UF-004 | Chưa có ảnh, Đang tải lên, Đã gửi, Bị từ chối | Ready |
| D-014 | S-011 | Platform fee active/validity | `D-014 - Platform fee active/validity - iPhone` · `D-014.dc.html` | Customer & Driver | iPhone | UF-004 | Đang hiệu lực, Sắp hết hạn, Đã hết hạn | Ready |
| D-015 | S-012 | Driver online home | `D-015 - Driver online home - iPhone` · `D-015.dc.html` | Customer & Driver | iPhone | UF-001, UF-002 | Ngoại tuyến, Trực tuyến, Chưa có chuyến | Ready |
| D-016 | S-012 | Service toggles / availability | `D-016 - Service toggles / availability - iPhone` · `D-016.dc.html` | Customer & Driver | iPhone | UF-001, UF-002 | Mặc định, Khu vực tạm dừng, Bị khoá | Ready |
| D-017 | S-012 | Job list / job cards | `D-017 - Job list / job cards - iPhone` · `D-017.dc.html` | Customer & Driver | iPhone | UF-001, UF-002 | Danh sách, Đang tải, Trống, Lỗi | Ready |
| D-018 | S-012 | Region unavailable / no service | `D-018 - Region unavailable / no service - iPhone` · `D-018.dc.html` | Customer & Driver | iPhone | UF-006 | Ngoài vùng hoạt động, Dịch vụ tạm dừng | Ready |
| D-019 | S-013 | Ride offer received | `D-019 - Ride offer received - iPhone` · `D-019.dc.html` | Customer & Driver | iPhone | UF-001 | Đếm ngược 12 giây, Còn 3 giây | Ready |
| D-020 | S-013 | Ride offer accepted | `D-020 - Ride offer accepted - iPhone` · `D-020.dc.html` | Customer & Driver | iPhone | UF-001 | Đã nhận chuyến | Ready |
| D-021 | S-013 | Ride offer rejected / timeout | `D-021 - Ride offer rejected / timeout - iPhone` · `D-021.dc.html` | Customer & Driver | iPhone | UF-001 | Đã từ chối, Hết thời gian | Ready |
| D-022 | S-013 | Ride pickup navigation | `D-022 - Ride pickup navigation - iPhone` · `D-022.dc.html` | Customer & Driver | iPhone | UF-001 | Đến điểm đón | Ready |
| D-023 | S-013 | Ride payment proof review | `D-023 - Ride payment proof review - iPhone` · `D-023.dc.html` | Customer & Driver | iPhone | UF-001 | Chứng từ đã gửi | Ready |
| D-024 | S-013 | Ride money not received | `D-024 - Ride money not received - iPhone` · `D-024.dc.html` | Customer & Driver | iPhone | UF-001 | Báo chưa nhận tiền | Ready |
| D-025 | S-013 | Ride arrived pickup | `D-025 - Ride arrived pickup - iPhone` · `D-025.dc.html` | Customer & Driver | iPhone | UF-001 | Đến điểm đón, Đang chờ khách | Ready |
| D-026 | S-013 | Ride start trip | `D-026 - Ride start trip - iPhone` · `D-026.dc.html` | Customer & Driver | iPhone | UF-001 | Bắt đầu bị khoá (chưa nhận tiền), Sẵn sàng bắt đầu | Ready |
| D-027 | S-013 | Ride in trip | `D-027 - Ride in trip - iPhone` · `D-027.dc.html` | Customer & Driver | iPhone | UF-001 | Trong chuyến | Ready |
| D-028 | S-013 | Ride completed | `D-028 - Ride completed - iPhone` · `D-028.dc.html` | Customer & Driver | iPhone | UF-001 | Hoàn thành | Ready |
| D-029 | S-013 | Ride canceled / issue | `D-029 - Ride canceled / issue - iPhone` · `D-029.dc.html` | Customer & Driver | iPhone | UF-001 | Chọn lý do | Ready |
| D-030 | S-014 | Food offer received | `D-030 - Food offer received - iPhone` · `D-030.dc.html` | Customer & Driver | iPhone | UF-002 | Đếm ngược | Ready |
| D-031 | S-014 | Food accepted / go to outlet | `D-031 - Food accepted / go to outlet - iPhone` · `D-031.dc.html` | Customer & Driver | iPhone | UF-002 | Đi tới quán | Ready |
| D-032 | S-014 | Food payment proof review | `D-032 - Food payment proof review - iPhone` · `D-032.dc.html` | Customer & Driver | iPhone | UF-002 | Kiểm tra chứng từ | Ready |
| D-033 | S-014 | Food money not received | `D-033 - Food money not received - iPhone` · `D-033.dc.html` | Customer & Driver | iPhone | UF-002 | Báo chưa nhận tiền | Ready |
| D-034 | S-014 | At outlet / order items | `D-034 - At outlet / order items - iPhone` · `D-034.dc.html` | Customer & Driver | iPhone | UF-002 | Danh sách món | Ready |
| D-035 | S-014 | Food change needed form | `D-035 - Food change needed form - iPhone` · `D-035.dc.html` | Customer & Driver | iPhone | UF-003 | Giá khác | Ready |
| D-036 | S-014 | Food proposal waiting customer | `D-036 - Food proposal waiting customer - iPhone` · `D-036.dc.html` | Customer & Driver | iPhone | UF-003 | Chờ 5 phút | Ready |
| D-037 | S-014 | Proposal accepted | `D-037 - Proposal accepted - iPhone` · `D-037.dc.html` | Customer & Driver | iPhone | UF-003 | Khách đồng ý | Ready |
| D-038 | S-014 | Proposal rejected / timeout | `D-038 - Proposal rejected / timeout - iPhone` · `D-038.dc.html` | Customer & Driver | iPhone | UF-003 | Khách từ chối, Hết thời gian | Ready |
| D-039 | S-014 | Supplemental payment pending | `D-039 - Supplemental payment pending - iPhone` · `D-039.dc.html` | Customer & Driver | iPhone | UF-003 | Chờ tiền bổ sung | Ready |
| D-040 | S-014 | Food picked up | `D-040 - Food picked up - iPhone` · `D-040.dc.html` | Customer & Driver | iPhone | UF-002 | Đã lấy món | Ready |
| D-041 | S-014 | Food delivering | `D-041 - Food delivering - iPhone` · `D-041.dc.html` | Customer & Driver | iPhone | UF-002 | Đang giao | Ready |
| D-042 | S-014 | Food delivered | `D-042 - Food delivered - iPhone` · `D-042.dc.html` | Customer & Driver | iPhone | UF-002 | Đã giao | Ready |
| D-043 | S-014 | Food issue/cancel reason | `D-043 - Food issue/cancel reason - iPhone` · `D-043.dc.html` | Customer & Driver | iPhone | UF-002, UF-003 | Quán đóng cửa, Không liên lạc được khách | Ready |
| D-044 | S-015 | Chat room | `D-044 - Chat room - iPhone` · `D-044.dc.html` | Customer & Driver | iPhone | UF-007 | Văn bản, ảnh, đã xem | Ready |
| D-045 | S-015 | Chat image upload failed | `D-045 - Chat image upload failed - iPhone` · `D-045.dc.html` | Customer & Driver | iPhone | UF-007 | Ảnh gửi lỗi | Ready |
| D-046 | S-015 | Chat offline / reconnecting | `D-046 - Chat offline / reconnecting - iPhone` · `D-046.dc.html` | Customer & Driver | iPhone | UF-007 | Đang kết nối lại | Ready |
| D-047 | S-019 | Driver locked notice | `D-047 - Driver locked notice - iPhone` · `D-047.dc.html` | Customer & Driver | iPhone | UF-005 | Bị khoá tạm | Ready |
| D-048 | S-019 | Lock appeal form | `D-048 - Lock appeal form - iPhone` · `D-048.dc.html` | Customer & Driver | iPhone | UF-005 | Soạn kháng nghị, Đã gửi | Ready |
| D-049 | Common | Earnings/history | `D-049 - Earnings/history - iPhone` · `D-049.dc.html` | Customer & Driver | iPhone | Driver ops | Danh sách, Trống | Ready |
| D-050 | Common | Notifications | `D-050 - Notifications - iPhone` · `D-050.dc.html` | Customer & Driver | iPhone | Push baseline | Việc, thanh toán, chat, khoá | Ready |
| D-051 | Common | Account/settings | `D-051 - Account/settings - iPhone` · `D-051.dc.html` | Customer & Driver | iPhone | Account | Mặc định | Ready |
| D-052 | Common | Help/support | `D-052 - Help/support - iPhone` · `D-052.dc.html` | Customer & Driver | iPhone | Support | Mặc định | Ready |
| D-053 | Common | Job history | `D-053 - Job history - iPhone` · `D-053.dc.html` | Customer & Driver | iPhone | Driver ops | Danh sách, Lọc Đi xe, Trống | Ready |
| D-054 | Common | Job history detail | `D-054 - Job history detail - iPhone` · `D-054.dc.html` | Customer & Driver | iPhone | UF-001, UF-002, UF-005 | Hoàn thành, Đã huỷ, Tranh chấp | Ready |
| D-055 | Common | Case / complaint list | `D-055 - Case / complaint list - iPhone` · `D-055.dc.html` | Customer & Driver | iPhone | UF-005 | Danh sách, Trống | Ready |
| D-056 | Common | Case / complaint detail | `D-056 - Case / complaint detail - iPhone` · `D-056.dc.html` | Customer & Driver | iPhone | UF-005 | Yêu cầu phản hồi | Ready |
| D-057 | Common | Direct call confirmation | `D-057 - Direct call confirmation - iPhone` · `D-057.dc.html` | Customer & Driver | iPhone | UF-001, UF-002, UF-007 | Gọi khách / tổng đài, Không khả dụng | Ready |
| D-058 | Common | Proof/evidence image viewer | `D-058 - Proof/evidence image viewer - iPhone` · `D-058.dc.html` | Customer & Driver | iPhone | F-023 | Xem & phóng to, Liên kết hết hạn | Ready |
| D-059 | Common | Privacy / consent settings | `D-059 - Privacy / consent settings - iPhone` · `D-059.dc.html` | Customer & Driver | iPhone | Privacy | Mặc định | Ready |
| A-000 | Common | Admin login | `A-000 - Admin login - Web 1440` · `A-000.dc.html` | Admin & Landing | Web 1440 | Admin auth | Mặc định, Sai thông tin, Bị khoá | Ready |
| A-001 | Common | OTP / second factor if enabled | `A-001 - OTP / second factor if enabled - Web 1440` · `A-001.dc.html` | Admin & Landing | Web 1440 | Admin auth | Mặc định, Lỗi | Ready |
| A-002 | Common | Admin shell / sidebar | `A-002 - Admin shell / sidebar - Web 1440` · `A-002.dc.html` | Admin & Landing | Web 1440 | Admin baseline | Mở rộng, Thu gọn | Ready |
| A-003 | Common | Permission denied | `A-003 - Permission denied - Web 1440` · `A-003.dc.html` | Admin & Landing | Web 1440 | RBAC | Không có quyền | Ready |
| A-004 | Common | Global search / command palette | `A-004 - Global search / command palette - Web 1440` · `A-004.dc.html` | Admin & Landing | Web 1440 | Admin baseline | Có kết quả, Không có kết quả | Ready |
| A-005 | S-016 | Dashboard overview | `A-005 - Dashboard overview - Web 1440` · `A-005.dc.html` | Admin & Landing | Web 1440 | Ops baseline | Mặc định, Đang tải, Lỗi | Ready |
| A-006 | S-016 | Marketplace health widgets | `A-006 - Marketplace health widgets - Web 1440` · `A-006.dc.html` | Admin & Landing | Web 1440 | Ops baseline | Ride/Food & rủi ro | Ready |
| A-007 | S-016 | Live ops queue | `A-007 - Live ops queue - Web 1440` · `A-007.dc.html` | Admin & Landing | Web 1440 | Ops baseline | Có việc tồn, Không có việc | Ready |
| A-008 | S-016 | Recent activity/audit preview | `A-008 - Recent activity/audit preview - Web 1440` · `A-008.dc.html` | Admin & Landing | Web 1440 | Ops baseline | Danh sách, Trống | Ready |
| A-009 | S-016 | Dashboard empty/new launch | `A-009 - Dashboard empty/new launch - Web 1440` · `A-009.dc.html` | Admin & Landing | Web 1440 | Ops baseline | Chưa có dữ liệu | Ready |
| A-010 | S-017 | Region list | `A-010 - Region list - Web 1440` · `A-010.dc.html` | Admin & Landing | Web 1440 | UF-006 | Active / Paused / Planned, Trống | Ready |
| A-011 | S-017 | Region detail drawer | `A-011 - Region detail drawer - Web 1440` · `A-011.dc.html` | Admin & Landing | Web 1440 | UF-006 | Xem thông tin & audit | Ready |
| A-012 | S-017 | Create city/region | `A-012 - Create city/region - Web 1440` · `A-012.dc.html` | Admin & Landing | Web 1440 | UF-006 | Mặc định, Lỗi trùng tên | Ready |
| A-013 | S-017 | Polygon editor map | `A-013 - Polygon editor map - Web 1440` · `A-013.dc.html` | Admin & Landing | Web 1440 | UF-006 | Bản nháp, Đang chọn vùng, Đang tải bản đồ | Ready |
| A-014 | S-017 | Draw polygon | `A-014 - Draw polygon - Web 1440` · `A-014.dc.html` | Admin & Landing | Web 1440 | UF-006 | Thêm điểm, Đã đóng hình | Ready |
| A-015 | S-017 | Edit polygon vertices | `A-015 - Edit polygon vertices - Web 1440` · `A-015.dc.html` | Admin & Landing | Web 1440 | UF-006 | Kéo đỉnh, Hình không hợp lệ | Ready |
| A-016 | S-017 | Polygon overlap blocked | `A-016 - Polygon overlap blocked - Web 1440` · `A-016.dc.html` | Admin & Landing | Web 1440 | UF-006 | Chặn xuất bản | Ready |
| A-017 | S-017 | Service/vehicle availability panel | `A-017 - Service/vehicle availability panel - Web 1440` · `A-017.dc.html` | Admin & Landing | Web 1440 | UF-006 | Đi xe/Đặt món · Xe máy/Ô tô | Ready |
| A-018 | S-017 | Region lifecycle controls | `A-018 - Region lifecycle controls - Web 1440` · `A-018.dc.html` | Admin & Landing | Web 1440 | UF-006 | Planned → Closed | Ready |
| A-019 | S-017 | Publish region config | `A-019 - Publish region config - Web 1440` · `A-019.dc.html` | Admin & Landing | Web 1440 | UF-006 | Xác nhận có lý do | Ready |
| A-020 | S-017 | Pause/resume region | `A-020 - Pause/resume region - Web 1440` · `A-020.dc.html` | Admin & Landing | Web 1440 | UF-006 | Bắt buộc lý do | Ready |
| A-021 | S-017 | Region publish conflict | `A-021 - Region publish conflict - Web 1440` · `A-021.dc.html` | Admin & Landing | Web 1440 | UF-006 | Xung đột phiên bản | Ready |
| A-022 | S-018 | Pricing/policy config list | `A-022 - Pricing/policy config list - Web 1440` · `A-022.dc.html` | Admin & Landing | Web 1440 | UF-006 | Bản nháp & đã xuất bản, Đang tải | Ready |
| A-023 | S-018 | Ride pricing guardrails form | `A-023 - Ride pricing guardrails form - Web 1440` · `A-023.dc.html` | Admin & Landing | Web 1440 | UF-006 | Mặc định, Lỗi guardrail | Ready |
| A-024 | S-018 | Food delivery fee policy form | `A-024 - Food delivery fee policy form - Web 1440` · `A-024.dc.html` | Admin & Landing | Web 1440 | UF-006 | Mặc định, Lỗi | Ready |
| A-025 | S-018 | Matching timeout/wave policy form | `A-025 - Matching timeout/wave policy form - Web 1440` · `A-025.dc.html` | Admin & Landing | Web 1440 | UF-006 | Mặc định, Lỗi | Ready |
| A-026 | S-018 | Auto-lock/fraud threshold policy | `A-026 - Auto-lock/fraud threshold policy - Web 1440` · `A-026.dc.html` | Admin & Landing | Web 1440 | UF-005 | Mặc định, Lỗi | Ready |
| A-027 | S-018 | Policy publish confirmation | `A-027 - Policy publish confirmation - Web 1440` · `A-027.dc.html` | Admin & Landing | Web 1440 | UF-006 | Xác nhận có lý do | Ready |
| A-028 | S-018 | Policy audit timeline | `A-028 - Policy audit timeline - Web 1440` · `A-028.dc.html` | Admin & Landing | Web 1440 | UF-006 | Người/thời gian/khác biệt | Ready |
| A-029 | S-019 | Driver list | `A-029 - Driver list - Web 1440` · `A-029.dc.html` | Admin & Landing | Web 1440 | UF-004, UF-005 | Tất cả, Lọc chờ duyệt, Lọc đã khoá | Ready |
| A-030 | S-019 | Driver detail drawer | `A-030 - Driver detail drawer - Web 1440` · `A-030.dc.html` | Admin & Landing | Web 1440 | UF-004 | Hồ sơ, dịch vụ, giấy tờ | Ready |
| A-031 | S-019 | KYC/document viewer | `A-031 - KYC/document viewer - Web 1440` · `A-031.dc.html` | Admin & Landing | Web 1440 | UF-004 | Ảnh, PDF | Ready |
| A-032 | S-019 | Driver approval/rejection | `A-032 - Driver approval/rejection - Web 1440` · `A-032.dc.html` | Admin & Landing | Web 1440 | UF-004 | Từ chối có lý do, Duyệt có lý do | Ready |
| A-033 | S-019 | Platform fee proof review | `A-033 - Platform fee proof review - Web 1440` · `A-033.dc.html` | Admin & Landing | Web 1440 | UF-004 | Duyệt/từ chối | Ready |
| A-034 | S-019 | Driver service eligibility editor | `A-034 - Driver service eligibility editor - Web 1440` · `A-034.dc.html` | Admin & Landing | Web 1440 | UF-004 | Cờ dịch vụ/phương tiện | Ready |
| A-035 | S-019 | Manual lock driver | `A-035 - Manual lock driver - Web 1440` · `A-035.dc.html` | Admin & Landing | Web 1440 | UF-005 | Bắt buộc lý do | Ready |
| A-036 | S-019 | Auto-lock review queue | `A-036 - Auto-lock review queue - Web 1440` · `A-036.dc.html` | Admin & Landing | Web 1440 | UF-005 | SLA, lý do, mức độ | Ready |
| A-037 | S-019 | Driver appeal detail | `A-037 - Driver appeal detail - Web 1440` · `A-037.dc.html` | Admin & Landing | Web 1440 | UF-005 | Nội dung & bằng chứng | Ready |
| A-038 | S-019 | Unlock driver | `A-038 - Unlock driver - Web 1440` · `A-038.dc.html` | Admin & Landing | Web 1440 | UF-005 | Có quyền, Không đủ quyền | Ready |
| A-039 | S-019 | Driver audit timeline | `A-039 - Driver audit timeline - Web 1440` · `A-039.dc.html` | Admin & Landing | Web 1440 | UF-004, UF-005 | Người/thời gian/hành động | Ready |
| A-040 | S-020 | Food brand list | `A-040 - Food brand list - Web 1440` · `A-040.dc.html` | Admin & Landing | Web 1440 | Food catalog | Danh sách, Tìm kiếm, Trống | Ready |
| A-041 | S-020 | Brand detail/editor | `A-041 - Brand detail/editor - Web 1440` · `A-041.dc.html` | Admin & Landing | Web 1440 | Food catalog | Bản nháp, Đã xuất bản | Ready |
| A-042 | S-020 | Outlet list | `A-042 - Outlet list - Web 1440` · `A-042.dc.html` | Admin & Landing | Web 1440 | Food catalog | Đóng / mở / thiếu dữ liệu | Ready |
| A-043 | S-020 | Outlet detail/editor | `A-043 - Outlet detail/editor - Web 1440` · `A-043.dc.html` | Admin & Landing | Web 1440 | Food catalog | Giờ, địa chỉ, vùng | Ready |
| A-044 | S-020 | Menu item list | `A-044 - Menu item list - Web 1440` · `A-044.dc.html` | Admin & Landing | Web 1440 | Food catalog | Thiếu giá, xung đột | Ready |
| A-045 | S-020 | Menu item editor | `A-045 - Menu item editor - Web 1440` · `A-045.dc.html` | Admin & Landing | Web 1440 | Food catalog | Lỗi nhập liệu | Ready |
| A-046 | S-020 | Outlet override editor | `A-046 - Outlet override editor - Web 1440` · `A-046.dc.html` | Admin & Landing | Web 1440 | Food catalog | Giá/trạng thái | Ready |
| A-047 | S-020 | Catalog conflict review | `A-047 - Catalog conflict review - Web 1440` · `A-047.dc.html` | Admin & Landing | Web 1440 | Food catalog | Trùng/xung đột | Ready |
| A-048 | S-020 | Import/upload catalog placeholder | `A-048 - Import/upload catalog placeholder - Web 1440` · `A-048.dc.html` | Admin & Landing | Web 1440 | Food catalog | Ghi chú nhập thủ công | Ready |
| A-049 | S-020 | Publish catalog changes | `A-049 - Publish catalog changes - Web 1440` · `A-049.dc.html` | Admin & Landing | Web 1440 | Food catalog | Xác nhận có lý do | Ready |
| A-050 | S-021 | Complaint/case queue | `A-050 - Complaint/case queue - Web 1440` · `A-050.dc.html` | Admin & Landing | Web 1440 | UF-005 | Tất cả, Lọc kháng nghị | Ready |
| A-051 | S-021 | Case detail | `A-051 - Case detail - Web 1440` · `A-051.dc.html` | Admin & Landing | Web 1440 | UF-005 | Đang xem xét | Ready |
| A-052 | S-021 | Evidence viewer | `A-052 - Evidence viewer - Web 1440` · `A-052.dc.html` | Admin & Landing | Web 1440 | UF-005 | Chứng từ thanh toán | Ready |
| A-053 | S-021 | Payment proof dispute review | `A-053 - Payment proof dispute review - Web 1440` · `A-053.dc.html` | Admin & Landing | Web 1440 | UF-001, UF-002, UF-005 | Bằng chứng mâu thuẫn | Ready |
| A-054 | S-021 | Request user response | `A-054 - Request user response - Web 1440` · `A-054.dc.html` | Admin & Landing | Web 1440 | UF-005 | Khách/tài xế, hạn | Ready |
| A-055 | S-021 | Fraud escalation | `A-055 - Fraud escalation - Web 1440` · `A-055.dc.html` | Admin & Landing | Web 1440 | UF-005 | Loại, mức độ, lý do | Ready |
| A-056 | S-021 | Case decision form | `A-056 - Case decision form - Web 1440` · `A-056.dc.html` | Admin & Landing | Web 1440 | UF-005 | Xác nhận, Bác bỏ | Ready |
| A-057 | S-021 | Appeal review | `A-057 - Appeal review - Web 1440` · `A-057.dc.html` | Admin & Landing | Web 1440 | UF-005 | Chấp nhận/bác kháng nghị | Ready |
| A-058 | S-021 | Case audit timeline | `A-058 - Case audit timeline - Web 1440` · `A-058.dc.html` | Admin & Landing | Web 1440 | UF-005 | Bất biến | Ready |
| A-059 | S-021 | Case finalized summary | `A-059 - Case finalized summary - Web 1440` · `A-059.dc.html` | Admin & Landing | Web 1440 | UF-005 | Đã kết luận | Ready |
| A-060 | Common | Media/evidence signed URL expired | `A-060 - Media/evidence signed URL expired - Web 1440` · `A-060.dc.html` | Admin & Landing | Web 1440 | Evidence | Hết hạn — tải lại, Không có quyền | Ready |
| A-061 | Common | Audit log search | `A-061 - Audit log search - Web 1440` · `A-061.dc.html` | Admin & Landing | Web 1440 | Audit | Mặc định, Có bộ lọc, Trống | Ready |
| A-062 | Common | Admin user / RBAC list | `A-062 - Admin user / RBAC list - Web 1440` · `A-062.dc.html` | Admin & Landing | Web 1440 | RBAC | Danh sách vai trò | Ready |
| A-063 | Common | Admin user detail / role assignment | `A-063 - Admin user detail / role assignment - Web 1440` · `A-063.dc.html` | Admin & Landing | Web 1440 | RBAC | Ma trận quyền | Ready |
| A-064 | Common | Sensitive action reason dialog | `A-064 - Sensitive action reason dialog - Web 1440` · `A-064.dc.html` | Admin & Landing | Web 1440 | Admin baseline | Mặc định, Lỗi thiếu lý do | Ready |
| A-065 | Common | Config version diff | `A-065 - Config version diff - Web 1440` · `A-065.dc.html` | Admin & Landing | Web 1440 | Admin baseline | Trước / sau | Ready |
| A-066 | Common | Basic ops dashboard drilldown | `A-066 - Basic ops dashboard drilldown - Web 1440` · `A-066.dc.html` | Admin & Landing | Web 1440 | Analytics | Ride/Food/rủi ro theo vùng | Ready |
| A-067 | Common | System health / queue status | `A-067 - System health / queue status - Web 1440` · `A-067.dc.html` | Admin & Landing | Web 1440 | Ops baseline | Bình thường, Suy giảm | Ready |
| A-068 | Common | Admin settings | `A-068 - Admin settings - Web 1440` · `A-068.dc.html` | Admin & Landing | Web 1440 | Admin baseline | Hồ sơ, thông báo, đăng xuất | Ready |
| A-069 | Common | Empty/error/loading template | `A-069 - Empty/error/loading template - Web 1440` · `A-069.dc.html` | Admin & Landing | Web 1440 | Admin baseline | Mẫu trống / lỗi / đang tải | Ready |
| A-070 | Common | Finance proof queue | `A-070 - Finance proof queue - Web 1440` · `A-070.dc.html` | Admin & Landing | Web 1440 | F-003 | Tất cả, Lọc chờ xác minh | Ready |
| A-071 | Common | Finance proof detail | `A-071 - Finance proof detail - Web 1440` · `A-071.dc.html` | Admin & Landing | Web 1440 | F-003, F-023 | Duyệt/từ chối | Ready |
| A-072 | Common | Customer management light | `A-072 - Customer management light - Web 1440` · `A-072.dc.html` | Admin & Landing | Web 1440 | Support | Tìm kiếm | Ready |
| A-073 | Common | Customer detail / history | `A-073 - Customer detail / history - Web 1440` · `A-073.dc.html` | Admin & Landing | Web 1440 | Support, UF-005 | Lịch sử & khiếu nại | Ready |
| A-074 | Common | Notification template/config baseline | `A-074 - Notification template/config baseline - Web 1440` · `A-074.dc.html` | Admin & Landing | Web 1440 | F-034 | Mẫu việc/thanh toán/chat/khoá | Ready |
| A-075 | Common | Data/privacy request queue | `A-075 - Data/privacy request queue - Web 1440` · `A-075.dc.html` | Admin & Landing | Web 1440 | Privacy | Xuất/xoá, ngoại lệ | Ready |
| A-076 | Common | Data/privacy request detail | `A-076 - Data/privacy request detail - Web 1440` · `A-076.dc.html` | Admin & Landing | Web 1440 | Privacy | Quyết định & audit | Ready |
| L-001 | Landing | Landing home hero | `L-001 - Landing home hero - Web` · `L-001.dc.html` | Admin & Landing | Web | Public | Desktop, Mobile | Ready |
| L-002 | Landing | Customer value section | `L-002 - Customer value section - Web` · `L-002.dc.html` | Admin & Landing | Web | Public | Đi xe + Đặt món | Ready |
| L-003 | Landing | Driver acquisition section | `L-003 - Driver acquisition section - Web` · `L-003.dc.html` | Admin & Landing | Web | Driver acquisition | 0% hoa hồng + gói ra mắt | Ready |
| L-004 | Landing | How Onway works | `L-004 - How Onway works - Web` · `L-004.dc.html` | Admin & Landing | Web | Public trust | Chuyển khoản trực tiếp + chứng từ | Ready |
| L-005 | Landing | Safety / dispute / connection model | `L-005 - Safety / dispute / connection model - Web` · `L-005.dc.html` | Admin & Landing | Web | Public trust | Mô hình kết nối, an toàn | Ready |
| L-006 | Landing | App download / waitlist CTA | `L-006 - App download / waitlist CTA - Web` · `L-006.dc.html` | Admin & Landing | Web | Public | Có link tải, Chưa có link — waitlist | Ready |
| L-007 | Landing | FAQ | `L-007 - FAQ - Web` · `L-007.dc.html` | Admin & Landing | Web | Public | Khách hàng, Tài xế | Ready |
| L-008 | Landing | Footer / legal links | `L-008 - Footer / legal links - Web` · `L-008.dc.html` | Admin & Landing | Web | Public | Quyền riêng tư, điều khoản, liên hệ | Ready |
| L-009 | Landing | Terms page | `L-009 - Terms page - Web` · `L-009.dc.html` | Admin & Landing | Web | Legal | Khung nội dung pháp lý | Ready |
| L-010 | Landing | Privacy page | `L-010 - Privacy page - Web` · `L-010.dc.html` | Admin & Landing | Web | Legal/Privacy | Khung nội dung quyền riêng tư | Ready |
| L-011 | Landing | Contact/support page | `L-011 - Contact/support page - Web` · `L-011.dc.html` | Admin & Landing | Web | Support | Khách, tài xế, đối tác | Ready |

Tổng: 216 frame, 371 trạng thái. Frame thiếu so với frame map: không có.
