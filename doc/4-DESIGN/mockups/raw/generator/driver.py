from lib import *
from reg import frame
import customer as cu

M = cu.M


# ================= AUTH / ONBOARDING =================
@frame("D-000", "Splash / launch", "Khởi động & đăng nhập")
def d000():
    splash = phone(
        f'<div style="flex-grow: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 16px">{logo_img(56, True)}'
        f'<div style="{TY["ovl"]}; color: rgba(255,255,255,.7); padding: 4px 10px; border: 1px solid rgba(255,255,255,.3); border-radius: 999px">TÀI XẾ</div></div>'
        f'<div style="display: flex; justify-content: center; padding-bottom: 72px">{spinner(28, "#FFFFFF").replace(C["b2"], "rgba(255,255,255,.3)")}</div>', bg=C["inverse"])
    force = phone(dialog_over(f'<div style="flex-grow: 1; display: flex; align-items: center; justify-content: center; background: {C["inverse"]}">{logo_img(56, True)}</div>',
                              "Cần cập nhật ứng dụng", "Bản Onway Tài xế 1.0.4 không còn nhận chuyến. Cập nhật lên 1.1.0 để tiếp tục trực tuyến.",
                              btn("Cập nhật ngay", "primary", "lg", "download", full=True), ic="download", tone="info"))
    return [("Đang tải", splash), ("Bắt buộc cập nhật", force)]


@frame("D-001", "Phone login", "Khởi động & đăng nhập")
def d001():
    return [("Mặc định", cu.login_screen("default", "d")), ("Lỗi định dạng số", cu.login_screen("error", "d")), ("Giới hạn gửi mã", cu.login_screen("limited", "d"))]


@frame("D-002", "OTP verification", "Khởi động & đăng nhập")
def d002():
    return [("Mặc định", cu.otp_screen("default", "d")), ("Sai mã OTP", cu.otp_screen("invalid", "d")), ("Chờ gửi lại mã", cu.otp_screen("cooldown", "d"))]


def onb_head(step, total=6, title="", sub=""):
    return (f'<div style="padding: {TOP}px 16px 12px; background: #FFFFFF; display: flex; flex-direction: column; gap: 12px; border-bottom: 1px solid {C["b1"]}">'
            + row(ibtn("arrow-left", "Quay lại", "ghost", 44), txt(f"Bước {step}/{total}", "lbl", C["t2"]), spacer(), btn("Lưu & thoát", "ghost", "sm"), gap=4)
            + progress(int(step / total * 100)) + "</div>")


def drv_profile(err=False):
    return phone(onb_head(1) + body(
        col(h("Thông tin tài xế", "hxl"), txt("Tên phải trùng với CCCD. Khách sẽ thấy tên và ảnh đại diện của bạn.", "bmd", C["t2"]), gap=8)
        + row(avatar("TH", 72), col(btn("Chụp ảnh chân dung", "outline", "md", "camera"), txt("Ảnh rõ mặt, không đeo kính râm", "cap", C["t3"]), gap=6), gap=16)
        + field("Họ và tên (theo CCCD)", "Trần Văn Hùng")
        + field("Ngày sinh", "12/03/1990" if not err else "12/03/2010", error="Tài xế phải đủ 18 tuổi." if err else None, mono=True)
        + select("Thành phố hoạt động", "TP. Hồ Chí Minh")
        + field("Số điện thoại liên hệ khẩn cấp", "" if err else "0912 345 678", error="Nhập số người thân để Onway liên hệ khi khẩn cấp." if err else None, mono=True), bg="#FFFFFF", gap=16)
        + bottom(btn("Tiếp tục", "primary", "lg", full=True, href="D-004.dc.html")))


@frame("D-003", "Driver profile setup", "Đăng ký tài xế")
def d003():
    return [("Mặc định", drv_profile()), ("Lỗi nhập liệu", drv_profile(True))]


def svc_card(ic, title, sub, on, dis=False, note=""):
    bd = f"1.5px solid {C['inverse']}" if on else f"1px solid {C['b2']}"
    op = "opacity: .5; " if dis else ""
    chk = f'<span style="width: 24px; height: 24px; border-radius: 6px; background: {C["inverse"] if on else "#FFFFFF"}; border: 1.5px solid {C["inverse"] if on else C["b3"]}; display: flex; align-items: center; justify-content: center">{icon("check", 16, "#FFFFFF", 3) if on else ""}</span>'
    n = f'<div style="{TY["cap"]}; color: {C["warn"]}; margin-top: 4px">{note}</div>' if note else ""
    return (f'<button type="button" aria-pressed="{"true" if on else "false"}" style="{op}display: flex; gap: 14px; align-items: center; width: 100%; padding: 16px; border-radius: 12px; border: {bd}; background: #FFFFFF; font-family: {FONT}; text-align: left; color: {C["t1"]}">'
            f'{icon_tile(ic, 48)}<div style="flex-grow: 1"><div style="{TY["bmd"]}; font-weight: 700">{title}</div><div style="{TY["cap"]}; font-size: 13px; color: {C["t3"]}">{sub}</div>{n}</div>{chk}</button>')


def drv_service(state="bike"):
    bike = state in ("bike", "both")
    car = state in ("car", "both")
    un = state == "unavail"
    return phone(onb_head(2) + body(
        col(h("Bạn chạy loại xe nào?", "hxl"), txt("Giấy tờ cần nộp phụ thuộc loại xe và dịch vụ bạn chọn.", "bmd", C["t2"]), gap=8)
        + ovl("Phương tiện")
        + svc_card("bike", "Xe máy", "Nhận Đi xe và Đặt món", bike or un)
        + svc_card("car", "Ô tô 4 chỗ", "Chỉ nhận Đi xe", car, dis=un, note="Chưa mở đăng ký ô tô tại TP. Hồ Chí Minh" if un else "")
        + ovl("Dịch vụ")
        + checkbox("Đi xe — chở khách", True, "Giá do Onway tính, bạn chọn Nhận hoặc Từ chối")
        + checkbox("Đặt món — mua & giao món", bike or un, "Bạn trả tiền quán bằng tiền khách đã chuyển"), bg="#FFFFFF", gap=14)
        + bottom(btn("Tiếp tục", "primary", "lg", full=True, href="D-005.dc.html")))


@frame("D-004", "Service / vehicle selection", "Đăng ký tài xế")
def d004():
    return [("Xe máy", drv_service()), ("Ô tô", drv_service("car")), ("Cả hai", drv_service("both")), ("Loại xe chưa mở", drv_service("unavail"))]


def doc_row(title, sub, st, href="D-006.dc.html"):
    right = {"done": pill("approved", "Đã tải lên", "sm"), "todo": pill("unpaid", "Chưa có", "sm"), "uploading": pill("pendingReview", "Đang tải", "sm"),
             "failed": pill("rejected", "Lỗi tải lên", "sm"), "rejected": pill("rejected", "Cần nộp lại", "sm")}[st]
    return list_row(title, sub, {"done": "check-circle", "todo": "file", "uploading": "upload", "failed": "alert-circle", "rejected": "x-circle"}[st], right=right, href=href, pad="14px 0")


def doc_checklist(state="incomplete"):
    rows = [("CCCD mặt trước & sau", "Ảnh rõ 4 góc, không loá", "done"), ("Ảnh chân dung cầm CCCD", "Để đối chiếu khuôn mặt", "done"),
            ("Giấy phép lái xe hạng A1", "Còn hạn", "todo" if state == "incomplete" else ("uploading" if state == "uploading" else "failed")),
            ("Đăng ký xe (cà vẹt)", "Xe đứng tên bạn hoặc giấy uỷ quyền", "todo"), ("Bảo hiểm TNDS xe máy", "Còn hạn", "todo"),
            ("Lý lịch tư pháp", "Nếu được yêu cầu theo quy định", "todo")]
    b = ""
    if state == "failed":
        b = banner("danger", "Tải lên thất bại", "Ảnh giấy phép lái xe chưa gửi được. Ảnh vẫn lưu trên máy — bấm để thử lại.", action=btn("Thử lại", "outline", "sm", "refresh"))
    lst = "".join(doc_row(*r, href="D-006.dc.html" if i < 2 else "D-007.dc.html") for i, r in enumerate(rows))
    return phone(onb_head(3) + body(col(h("Giấy tờ bắt buộc", "hxl"), txt("2/6 giấy tờ đã tải lên · Xe máy · Đi xe + Đặt món", "bmd", C["t2"]), gap=8) + progress(33) + b
                                    + f'<div>{lst}</div>', bg="#FFFFFF", gap=14)
                 + bottom(btn("Tiếp tục", "disabled", "lg", full=True) + txt("Hoàn tất đủ giấy tờ để gửi hồ sơ", "cap", C["t3"], extra="text-align: center")))


@frame("D-005", "Document upload checklist", "Đăng ký tài xế")
def d005():
    return [("Chưa đủ", doc_checklist()), ("Đang tải lên", doc_checklist("uploading")), ("Tải lên lỗi", doc_checklist("failed"))]


def id_capture(state="front"):
    lab = {"front": "Mặt trước CCCD", "back": "Mặt sau CCCD", "selfie": "Chân dung cầm CCCD", "rejected": "Mặt trước CCCD"}[state]
    frame_ = (f'<div style="position: relative; height: {360 if state == "selfie" else 230}px; border-radius: 16px; background: #1C1B1B; display: flex; align-items: center; justify-content: center; overflow: hidden">'
              f'<div style="width: {200 if state == "selfie" else 300}px; height: {260 if state == "selfie" else 190}px; border-radius: {999 if state == "selfie" else 12}px; border: 2.5px dashed rgba(255,255,255,.8)"></div>'
              f'<span style="position: absolute; bottom: 12px; {TY["cap"]}; color: rgba(255,255,255,.8)">Đặt {lab.lower()} vào khung</span></div>')
    b = ""
    if state == "rejected":
        b = banner("danger", "Ảnh trước đó bị từ chối", "Lý do: Ảnh bị loá, không đọc được số CCCD. Chụp lại nơi đủ sáng, không dùng đèn flash.")
    tips = col(row(icon("check", 16, C["ok"]), txt("Đủ 4 góc giấy tờ, không che ngón tay", "bsm", C["t2"]), gap=8),
               row(icon("check", 16, C["ok"]), txt("Chữ rõ, không loá, không mờ", "bsm", C["t2"]), gap=8), gap=6)
    seg = segmented(["Mặt trước", "Mặt sau", "Chân dung"], {"front": 0, "back": 1, "selfie": 2, "rejected": 0}[state])
    return phone(onb_head(3) + body(h(lab, "hlg") + seg + b + frame_ + tips, bg="#FFFFFF", gap=14)
                 + bottom(btn("Chụp ảnh", "primary", "lg", "camera", full=True) + btn("Chọn từ thư viện", "ghost", "lg", "image", full=True)))


@frame("D-006", "Identity document capture", "Đăng ký tài xế")
def d006():
    return [("Mặt trước", id_capture()), ("Mặt sau", id_capture("back")), ("Chân dung", id_capture("selfie")), ("Bị từ chối", id_capture("rejected"))]


def vehicle_docs(rej=False):
    items = (card(row(icon_tile("id-card", 40), col(txt("Giấy phép lái xe", "bmd", extra="font-weight: 600"), txt("Bắt buộc cho Xe máy · hạng A1 trở lên", "cap", C["t3"]), gap=2), spacer(), pill("approved", "Đã có", "sm"), gap=12)
                  + row(photo(150, 96, "Mặt trước", "image", 8), photo(150, 96, "Mặt sau", "image", 8), gap=8), pad=14)
             + card(row(icon_tile("file", 40), col(txt("Đăng ký xe (cà vẹt)", "bmd", extra="font-weight: 600"), txt("Biển số sẽ hiển thị cho khách", "cap", C["t3"]), gap=2), spacer(),
                        pill("rejected", "Cần nộp lại", "sm") if rej else pill("unpaid", "Chưa có", "sm"), gap=12)
                    + (banner("danger", "Bị từ chối", "Biển số trên cà vẹt (59-X2 123.45) không khớp biển số bạn khai (59-X2 123.54).") if rej else "")
                    + field("Biển số xe", "59-X2 123.54" if rej else "59-X2 123.45", mono=True, error="Kiểm tra lại biển số." if rej else None)
                    + upload_tile("empty", "Ảnh 2 mặt cà vẹt"), pad=14)
             + card(row(icon_tile("shield", 40), col(txt("Bảo hiểm TNDS", "bmd", extra="font-weight: 600"), txt("Bắt buộc cho Xe máy và Ô tô", "cap", C["t3"]), gap=2), spacer(), pill("unpaid", "Chưa có", "sm"), gap=12), pad=14))
    return phone(onb_head(4) + body(col(h("Giấy tờ phương tiện", "hxl"), txt("Theo loại xe đã chọn: Xe máy.", "bmd", C["t2"]), gap=8) + items, bg="#FFFFFF", gap=14)
                 + bottom(btn("Lưu giấy tờ", "primary", "lg", full=True, href="D-008.dc.html")))


@frame("D-007", "Vehicle document upload", "Đăng ký tài xế")
def d007():
    return [("Theo dịch vụ đã chọn", vehicle_docs()), ("Bị từ chối", vehicle_docs(True))]


def bank_setup(err=False):
    return phone(onb_head(5) + body(
        col(h("Tài khoản nhận tiền", "hxl"), txt("Khách chuyển khoản trực tiếp vào tài khoản này. Onway tạo mã VietQR từ thông tin bên dưới.", "bmd", C["t2"]), gap=8)
        + select("Ngân hàng", "Vietcombank")
        + field("Số tài khoản", "1023 4567 89", mono=True, error="Số tài khoản phải có 9–14 chữ số." if err else None)
        + field("Tên chủ tài khoản", "TRAN VAN HUNG" if not err else "NGUYEN THI MAI", error="Tên chủ tài khoản phải trùng với tên trên CCCD (TRẦN VĂN HÙNG)." if err else None, helper=None if err else "Viết in hoa, không dấu, trùng tên CCCD.")
        + card(row(qr_svg(72), col(txt("Xem trước mã VietQR", "bsm", extra="font-weight: 600"), txt("Khách quét mã này sau khi bạn nhận chuyến", "cap", C["t3"]), gap=2), gap=12), pad=12)
        + banner("info", "Onway không giữ tiền của bạn", "Mọi tiền chuyến và tiền món đi thẳng vào tài khoản này. Onway thu 0% hoa hồng."), bg="#FFFFFF", gap=14)
        + bottom(btn("Gửi hồ sơ", "primary", "lg", full=True, href="D-009.dc.html")))


@frame("D-008", "Bank/QR receiving info setup", "Đăng ký tài xế")
def d008():
    return [("Mặc định", bank_setup()), ("Lỗi nhập liệu", bank_setup(True))]


def status_screen(ic, tone, pill_, title, body_, extra, cta):
    bg, fg = {"warn": (C["warn_bg"], C["warn"]), "ok": (C["ok_bg"], C["ok"]), "err": (C["err_bg"], C["err"])}[tone]
    return phone(f'<div style="height: {TOP}px; background: #FFFFFF"></div>' + body(
        f'<div style="width: 72px; height: 72px; border-radius: 999px; background: {bg}; display: flex; align-items: center; justify-content: center; margin-top: 24px">{icon(ic, 34, fg)}</div>'
        + pill_ + h(title, "hxl") + txt(body_, "bmd", C["t2"]) + extra, bg="#FFFFFF", gap=14) + bottom(cta, border=False))


@frame("D-009", "Onboarding review pending", "Đăng ký tài xế")
def d009():
    return [("Chờ duyệt", status_screen("clock", "warn", pill("pendingReview"), "Hồ sơ đang được xét duyệt",
                                         "Đội Driver Ops kiểm tra giấy tờ trong 1–2 ngày làm việc. Onway sẽ gửi thông báo khi có kết quả.",
                                         card(timeline([("Gửi hồ sơ", "24/09 09:40", "done"), ("Kiểm tra giấy tờ", "Đang thực hiện", "current"), ("Thanh toán phí nền tảng", "Sau khi hồ sơ được duyệt", "todo"), ("Kích hoạt", "", "todo")], True), pad=16),
                                         btn("Xem hồ sơ đã gửi", "outline", "lg", full=True)))]


@frame("D-010", "Onboarding rejected", "Đăng ký tài xế")
def d010():
    return [("Bị từ chối", status_screen("x-circle", "err", pill("rejected", "Cần bổ sung"), "Hồ sơ chưa được duyệt",
                                          "Bạn cần nộp lại 1 giấy tờ. Các giấy tờ khác đã hợp lệ và được giữ nguyên.",
                                          card(doc_row("Đăng ký xe (cà vẹt)", "Biển số không khớp với biển số đã khai", "rejected", "D-007.dc.html") + doc_row("CCCD mặt trước & sau", "Hợp lệ", "done") + txt("Người duyệt: Driver Ops · 25/09 10:12", "cap", C["t3"]), pad=14, gap=0),
                                          btn("Nộp lại giấy tờ", "primary", "lg", full=True, href="D-007.dc.html") + btn("Liên hệ hỗ trợ", "ghost", "lg", full=True)))]


@frame("D-011", "Onboarding approved", "Đăng ký tài xế")
def d011():
    return [("Đã duyệt", status_screen("check-circle", "ok", pill("approved"), "Chúc mừng, hồ sơ đã được duyệt!",
                                        "Bước cuối: thanh toán phí sử dụng nền tảng để kích hoạt tài khoản và bắt đầu nhận chuyến.",
                                        card(kv("Loại xe", "Xe máy · 59-X2 123.45") + kv("Dịch vụ", "Đi xe, Đặt món") + kv("Khu vực", "TP. Hồ Chí Minh"), pad=14, gap=8),
                                        btn("Thanh toán phí nền tảng", "primary", "lg", full=True, href="D-012.dc.html")))]


def fee_pkg(state="unpaid"):
    st = {"unpaid": pill("unpaid"), "expired": pill("expired"), "active": pill("active")}[state]
    b = ""
    if state == "expired":
        b = banner("warning", "Gói đã hết hạn ngày 20/09/2026", "Bạn không thể trực tuyến nhận chuyến cho tới khi gia hạn.")
    if state == "active":
        b = banner("success", "Gói đang hoạt động đến 24/03/2028", "Bạn có thể trực tuyến và nhận chuyến.")
    pkg = card(row(f'<span style="{TY["ovl"]}; color: {C["brand"]}">GÓI RA MẮT</span>', spacer(), st)
               + row(num("1.000.000đ", 32, weight=700), txt("/ 12 tháng", "bmd", C["t2"]), gap=8, align="baseline")
               + row(icon("plus", 16, C["ok"]), txt("Tặng thêm 6 tháng — tổng 18 tháng sử dụng", "bmd", C["ok"], extra="font-weight: 600"), gap=6)
               + divider()
               + row(icon("check", 16), txt("0% hoa hồng trên mọi chuyến và đơn", "bsm"), gap=8) + row(icon("check", 16), txt("Nhận toàn bộ tiền khách chuyển trực tiếp", "bsm"), gap=8)
               + row(icon("check", 16), txt("Không giới hạn số chuyến", "bsm"), gap=8), pad=18, gap=10)
    refund = card(txt("Chính sách hoàn phí (12 tháng trả phí)", "lbl") + kv("Dừng trong quý 1", "Hoàn 750.000đ", True) + kv("Dừng trong quý 2", "Hoàn 500.000đ", True)
                  + kv("Dừng trong quý 3", "Hoàn 250.000đ", True) + kv("Dừng trong quý 4", "Không hoàn", True) + txt("6 tháng tặng không được hoàn. Phí nền tảng không phải tiền cọc hay ký quỹ.", "cap", C["t3"]), pad=14, gap=8)
    cta = {"unpaid": btn("Thanh toán 1.000.000đ", "primary", "lg", full=True, href="D-013.dc.html"), "expired": btn("Gia hạn gói", "primary", "lg", full=True, href="D-013.dc.html"),
           "active": btn("Xem hiệu lực gói", "secondary", "lg", full=True, href="D-014.dc.html")}[state]
    return phone(topbar("Phí sử dụng nền tảng", state != "unpaid") + body(b + pkg + refund, bg="#FFFFFF", gap=14) + bottom(cta))


@frame("D-012", "Platform fee package", "Phí nền tảng")
def d012():
    return [("Chưa thanh toán", fee_pkg()), ("Hết hạn", fee_pkg("expired")), ("Đang hoạt động", fee_pkg("active"))]


def fee_proof(state="empty"):
    info = card(row(qr_svg(96), col(txt("Chuyển khoản cho Onway", "cap", C["t3"]), num("1.000.000đ", 24, weight=700), txt("CÔNG TY TNHH ONWAY · Techcombank", "cap", C["t3"]),
                                    num("1903 8888 0000", 14, weight=600), num("ONWFEE 0901234567", 13, C["t2"]), gap=3), gap=14), pad=14)
    extra = ""
    if state == "rejected":
        extra = banner("danger", "Chứng từ bị từ chối", "Finance Ops: Chưa thấy giao dịch với nội dung ONWFEE 0901234567. Gửi lại ảnh có mã giao dịch ngân hàng.")
    if state == "submitted":
        extra = banner("info", "Đã gửi — chờ Finance Ops xác minh", "Thường trong 4 giờ làm việc. Bạn sẽ nhận thông báo khi gói được kích hoạt.")
    up = upload_tile({"empty": "empty", "uploading": "uploading", "submitted": "done", "rejected": "empty"}[state], "Ảnh giao dịch có mã tham chiếu").replace("Đã gửi cho tài xế lúc 08:14", "Đã gửi lúc 10:32")
    cta = {"empty": btn("Gửi chứng từ", "disabled", "lg", full=True), "uploading": btn("Đang gửi…", "disabled", "lg", full=True),
           "submitted": btn("Về trang chủ", "secondary", "lg", full=True), "rejected": btn("Gửi lại chứng từ", "disabled", "lg", full=True)}[state]
    return phone(topbar("Thanh toán phí nền tảng", True) + body(
        (pill("proofPending", "Chờ xác minh") if state == "submitted" else (pill("proofRejected") if state == "rejected" else "")) + info
        + field("Mã giao dịch ngân hàng (không bắt buộc)", "FT24268093415" if state != "empty" else "", "VD: FT24268093415", mono=True) + up + extra, bg="#FFFFFF", gap=14) + bottom(cta))


@frame("D-013", "Platform fee proof upload", "Phí nền tảng")
def d013():
    return [("Chưa có ảnh", fee_proof()), ("Đang tải lên", fee_proof("uploading")), ("Đã gửi", fee_proof("submitted")), ("Bị từ chối", fee_proof("rejected"))]


def fee_validity(state="active"):
    pct, st, left, until = {"active": (22, pill("active"), "Còn 14 tháng 3 ngày", "24/03/2028"), "soon": (96, pill("unpaid", "Sắp hết hạn"), "Còn 12 ngày", "06/10/2026"),
                            "expired": (100, pill("expired"), "Đã hết hạn", "20/09/2026")}[state]
    b = ""
    if state == "soon":
        b = banner("warning", "Gói sắp hết hạn", "Gia hạn trước 06/10 để không bị gián đoạn nhận chuyến.")
    if state == "expired":
        b = banner("danger", "Không thể trực tuyến", "Gói phí nền tảng đã hết hạn. Gia hạn để tiếp tục nhận chuyến.")
    return phone(topbar("Gói của tôi", True) + body(
        b + card(row(txt("Gói ra mắt 18 tháng", "hsm"), spacer(), st) + row(txt(left, "hmd"), spacer()) + progress(pct, C["ok"] if state == "active" else (C["warn_b"] if state == "soon" else C["b3"]), 8)
                 + row(txt("Kích hoạt 24/09/2026", "cap", C["t3"]), spacer(), txt(f"Hết hạn {until}", "cap", C["t3"])), pad=16, gap=10)
        + card(kv("Đã trả", "1.000.000đ", True) + kv("12 tháng trả phí", "24/09/2026 – 24/09/2027") + kv("6 tháng tặng", "24/09/2027 – 24/03/2028") + kv("Mã chứng từ", "FEE-240924-0331", True), pad=14, gap=8)
        + list_row("Yêu cầu dừng & hoàn phí", "Hoàn theo quý đã dùng", "banknote", pad="14px 0"), bg="#FFFFFF", gap=14)
        + bottom(btn("Gia hạn gói", "primary" if state != "active" else "outline", "lg", full=True, href="D-013.dc.html")))


@frame("D-014", "Platform fee active/validity", "Phí nền tảng")
def d014():
    return [("Đang hiệu lực", fee_validity()), ("Sắp hết hạn", fee_validity("soon")), ("Đã hết hạn", fee_validity("expired"))]


# ================= ONLINE / JOBS =================
def online_toggle(on):
    bg = C["ok_bg"] if on else C["sunken"]
    return (f'<div style="display: flex; align-items: center; gap: 12px; padding: 12px 14px; border-radius: 12px; background: #FFFFFF; border: 1px solid {C["b2"]}; box-shadow: {SH_MD}">'
            f'<span style="width: 10px; height: 10px; border-radius: 999px; background: {C["ok_b"] if on else C["b3"]}"></span>'
            f'<div style="flex-grow: 1"><div style="{TY["bmd"]}; font-weight: 700">{"Đang trực tuyến" if on else "Bạn đang ngoại tuyến"}</div><div style="{TY["cap"]}; color: {C["t3"]}">{"Đi xe · Đặt món · Quận 1" if on else "Bật để bắt đầu nhận chuyến"}</div></div>'
            f'<span role="switch" aria-checked="{"true" if on else "false"}" aria-label="Trực tuyến" style="position: relative; width: 52px; height: 30px; border-radius: 999px; background: {C["ok"] if on else C["b3"]}; flex-shrink: 0">'
            f'<span style="position: absolute; top: 3px; {"left: 25px" if on else "left: 3px"}; width: 24px; height: 24px; border-radius: 999px; background: #FFFFFF"></span></span></div>')


def drv_home(state="online"):
    on = state in ("online", "nojobs")
    m = M(pins=[("me", 0.52, 0.36)], regions=[([(0.06, 0.08), (0.94, 0.05), (0.97, 0.62), (0.1, 0.66)], "active")], dim=not on)
    top = row(circle_btn("menu", "Menu"), spacer(), circle_btn("bell", "Thông báo")) + online_toggle(on)
    stats = row(card(col(txt("Hôm nay", "cap", C["t3"]), num("412.000đ", 18, weight=700), gap=2), pad=12, extra="flex: 1"),
                card(col(txt("Chuyến", "cap", C["t3"]), num("9", 18, weight=700), gap=2), pad=12, extra="flex: 1"),
                card(col(txt("Giờ trực tuyến", "cap", C["t3"]), num("5:40", 18, weight=700), gap=2), pad=12, extra="flex: 1"), gap=8)
    if state == "offline":
        inner = f'<div style="padding: 4px 16px {BOT}px; display: flex; flex-direction: column; gap: 14px">{stats}{btn("Bật trực tuyến", "primary", "xl", "power", full=True, href="D-017.dc.html")}{txt("Gói phí nền tảng còn hiệu lực đến 24/03/2028", "cap", C["t3"], extra="text-align: center")}</div>'
    elif state == "nojobs":
        inner = f'<div style="padding: 4px 16px {BOT}px; display: flex; flex-direction: column; gap: 14px">{row(spinner(18), txt("Đang chờ chuyến gần bạn…", "bmd", extra="font-weight: 600"), gap=10)}{txt("Chưa có yêu cầu trong khu vực. Khu vực đông khách lúc này: Quận 3, Quận 10.", "bsm", C["t2"])}{stats}</div>'
    else:
        inner = f'<div style="padding: 4px 16px {BOT}px; display: flex; flex-direction: column; gap: 14px">{row(txt("Đang nhận chuyến", "hsm"), spacer(), btn("Dịch vụ", "ghost", "sm", "sliders", href="D-016.dc.html"))}{stats}{tabbar_mini()}</div>'
    return phone(map_screen(m, inner, top, float_right=circle_btn("locate", "Về vị trí của tôi")))


def tabbar_mini():
    return row(*[f'<a href="{h_}" style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 4px; padding: 8px 0; border-radius: 10px; border: 1px solid {C["b2"]}; text-decoration: none; color: {C["t1"]}; {TY["cap"]}; font-weight: 600">{icon(i, 20)}{l}</a>'
                 for i, l, h_ in [("history", "Lịch sử", "D-053.dc.html"), ("banknote", "Thu nhập", "D-049.dc.html"), ("scale", "Khiếu nại", "D-055.dc.html"), ("user", "Tài khoản", "D-051.dc.html")]], gap=8)


@frame("D-015", "Driver online home", "Trực tuyến & nhận việc")
def d015():
    return [("Ngoại tuyến", drv_home("offline")), ("Trực tuyến", drv_home()), ("Chưa có chuyến", drv_home("nojobs"))]


def svc_toggles(state="default"):
    b = ""
    ride_on, food_on = True, True
    if state == "paused":
        b = banner("warning", "Đặt món tạm dừng tại Quận 1", "Ops tạm dừng dịch vụ Food từ 22:00 đến 06:00. Bạn vẫn nhận Đi xe.")
        food_on = False
    if state == "locked":
        b = banner("danger", "Tài khoản đang bị tạm khoá", "Bạn không thể bật dịch vụ nào. Xem lý do và gửi kháng nghị.", "lock", btn("Xem chi tiết", "outline", "sm", href="D-047.dc.html"))
        ride_on = food_on = False
    dis = "opacity: .5; " if state == "locked" else ""
    return phone(topbar("Dịch vụ nhận việc", True) + body(
        b + f'<div style="{dis}display: flex; flex-direction: column; gap: 4px">'
        + card(switch(ride_on, "Đi xe — chở khách", "Xe máy · 59-X2 123.45"), pad=14)
        + card(switch(food_on, "Đặt món — mua & giao", "Tạm dừng tại khu vực hiện tại" if state == "paused" else "Cần đủ tiền mặt trong tài khoản? Không — khách chuyển trước"), pad=14)
        + "</div>"
        + ovl("Khu vực của bạn") + card(row(icon_tile("map", 40), col(txt("Quận 1 · TP. Hồ Chí Minh", "bmd", extra="font-weight: 600"), txt("Vùng đang hoạt động", "cap", C["t3"]), gap=2), spacer(), pill("paused" if state == "paused" else "active", "Food tạm dừng" if state == "paused" else None, "sm"), gap=12), pad=12)
        + txt("Lưu ý: bạn chỉ nhận được chuyến có điểm đón nằm trong vùng hoạt động.", "cap", C["t3"]), bg="#FFFFFF", gap=12))


@frame("D-016", "Service toggles / availability", "Trực tuyến & nhận việc")
def d016():
    return [("Mặc định", svc_toggles()), ("Khu vực tạm dừng", svc_toggles("paused")), ("Bị khoá", svc_toggles("locked"))]


def job_card(kind, price, pick, drop, dist, eta, extra=""):
    ic = "bike" if kind == "ride" else "utensils"
    lab = "Đi xe" if kind == "ride" else "Đặt món"
    return (f'<a href="{"D-019.dc.html" if kind == "ride" else "D-030.dc.html"}" style="display: flex; flex-direction: column; gap: 10px; padding: 14px; border-radius: 12px; border: 1px solid {C["b2"]}; background: #FFFFFF; text-decoration: none; color: {C["t1"]}">'
            f'{row(icon_tile(ic, 32, r=8), txt(lab, "lbl"), spacer(), num(price, 20, weight=700), gap=8)}{addr_block(pick, drop)}'
            f'{row(txt(dist, "cap", C["t3"]), txt("·", "cap", C["t3"]), txt(eta, "cap", C["t3"]), spacer(), extra, gap=6)}</a>')


def job_list(state="list"):
    head = topbar("Việc gần bạn", True, right=ibtn("refresh", "Làm mới", "ghost", 44))
    if state == "loading":
        c = "".join(skel("100%", 150, 12) for _ in range(4))
    elif state == "empty":
        c = empty_state("navigation", "Chưa có việc gần bạn", "Giữ ứng dụng mở, Onway sẽ gửi yêu cầu ngay khi có khách trong khu vực.")
    elif state == "error":
        c = empty_state("alert-circle", "Không tải được danh sách việc", "Mất kết nối tới máy chủ. Bạn vẫn đang trực tuyến và sẽ nhận yêu cầu khi có mạng lại.", btn("Thử lại", "outline", "md", "refresh"))
    else:
        c = (job_card("ride", "48.000đ", "Toà nhà Bitexco, Q.1", "ĐH Kinh tế, Q.3", "Cách 1,2 km", "3,2 km chuyến")
             + job_card("food", "137.000đ", "Cơm Tấm Sà Bì, Nguyễn Trãi", "142 Lê Văn Sỹ, Phú Nhuận", "Cách 0,8 km", "3,4 km giao", pill("proofPending", "Khách chuyển trước", "sm"))
             + job_card("ride", "32.000đ", "Chợ Bến Thành, Q.1", "Nhà thờ Tân Định, Q.3", "Cách 1,9 km", "2,1 km chuyến"))
    return phone(head + body(segmented(["Tất cả", "Đi xe", "Đặt món"], 0) + c, gap=12, extra="justify-content: center" if state in ("empty", "error") else ""))


@frame("D-017", "Job list / job cards", "Trực tuyến & nhận việc")
def d017():
    return [("Danh sách", job_list()), ("Đang tải", job_list("loading")), ("Trống", job_list("empty")), ("Lỗi", job_list("error"))]


@frame("D-018", "Region unavailable / no service", "Trực tuyến & nhận việc")
def d018():
    def s(title, body_, reg_kind):
        m = M(pins=[("me", 0.82, 0.5)], regions=[([(0.05, 0.05), (0.62, 0.02), (0.66, 0.3), (0.2, 0.36)], reg_kind, "Vùng Quận 1")], dim=True)
        inner = f'<div style="padding: 4px 16px {BOT}px; display: flex; flex-direction: column; gap: 14px">{banner("warning", title, body_)}{btn("Chỉ đường về vùng hoạt động", "secondary", "lg", "navigation", full=True)}</div>'
        return phone(map_screen(m, inner, row(circle_btn("menu", "Menu"), spacer()) + online_toggle(False)))
    return [("Ngoài vùng hoạt động", s("Bạn đang ở ngoài vùng hoạt động", "Onway chỉ gửi chuyến khi bạn ở trong vùng có viền nét đứt. Di chuyển vào vùng để trực tuyến.", "active")),
            ("Dịch vụ tạm dừng", s("Vùng Quận 1 đang tạm dừng", "Ops tạm dừng nhận chuyến đến 06:00 do thời tiết xấu. Bạn sẽ nhận thông báo khi mở lại.", "paused"))]


# ================= RIDE JOB =================
def offer(kind="ride", sec=12):
    m = M(route=cu.ROUTE, pins=cu.PINS, driver=(0.9, 0.3)) if kind == "ride" else M(route=cu.F_ROUTE, pins=[("outlet", 0.3, 0.44), ("dropoff", 0.72, 0.17)], driver=(0.1, 0.3))
    ring = (f'<div style="position: relative; width: 64px; height: 64px; flex-shrink: 0"><svg width="64" height="64" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="28" fill="none" stroke="{C["b1"]}" stroke-width="5"/>'
            f'<circle cx="32" cy="32" r="28" fill="none" stroke="{C["inverse"]}" stroke-width="5" stroke-dasharray="{176 * sec / 15:.0f} 176" stroke-linecap="round" transform="rotate(-90 32 32)"/></svg>'
            f'<span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-family: {MONO}; font-size: 20px; font-weight: 700">{sec}</span></div>')
    if kind == "ride":
        top = row(icon_tile("bike", 36, r=8), txt("Đi xe · Xe máy", "lbl"), spacer(), gap=8)
        price = col(txt("Giá chuyến (Onway tính)", "cap", C["t3"]), num("48.000đ", 34, weight=700), gap=0)
        det = addr_block(cu.PICK, cu.DROP, "Cách bạn 1,2 km · 4 phút", "3,2 km · 14 phút")
        info = txt("Khách chuyển khoản cho bạn trước khi bạn đến đón.", "bsm", C["t2"])
        acc = "D-020.dc.html"
    else:
        top = row(icon_tile("utensils", 36, r=8), txt("Đặt món · 3 món", "lbl"), spacer(), gap=8)
        price = row(col(txt("Phí giao (của bạn)", "cap", C["t3"]), num("22.000đ", 34, weight=700), gap=0), spacer(), col(txt("Khách chuyển tổng", "cap", C["t3"]), num("137.000đ", 17, weight=600), gap=0, extra="text-align: right"), align="flex-end")
        det = addr_block("Cơm Tấm Sà Bì · Nguyễn Trãi", "142 Lê Văn Sỹ, Phú Nhuận", "Quán cách bạn 0,8 km", "3,4 km giao")
        info = txt("Bạn dùng 115.000đ khách chuyển trước để trả tiền quán.", "bsm", C["t2"])
        acc = "D-031.dc.html"
    sheet = (f'<div style="padding: 4px 16px {BOT}px; display: flex; flex-direction: column; gap: 14px" role="alertdialog" aria-live="assertive">{row(col(top, price, gap=10, extra="flex-grow: 1"), ring, align="flex-start")}'
             f'{divider()}{det}{info}<div style="display: flex; gap: 12px">{btn("Từ chối", "outline", "xl", full="grow", href="D-021.dc.html")}{btn("Nhận chuyến", "primary", "xl", full="grow", href=acc, extra="flex-grow: 2")}</div></div>')
    return phone(map_screen(m, sheet))


@frame("D-019", "Ride offer received", "Đi xe · Nhận chuyến")
def d019():
    return [("Đếm ngược 12 giây", offer("ride", 12)), ("Còn 3 giây", offer("ride", 3))]


def ride_job(state):
    ref = num("R-7Q2K9", 13, C["t3"])
    cust = person_row("Minh Anh", "Khách · 4,9 ★ · 38 chuyến", "MA")
    if state == "accepted":
        m = M(route=cu.TO_PICK, pins=[("pickup", 0.72, 0.47)], driver=(0.9, 0.3))
        head = job_header("accepted", "Đã nhận chuyến", "Chờ khách chuyển khoản 48.000đ", ref)
        body_ = cust + banner("info", "Khách đang chuyển khoản", "Bạn sẽ nhận thông báo khi khách gửi ảnh chứng từ. Kiểm tra tài khoản rồi xác nhận đã nhận đủ tiền.") + btn("Chỉ đường đến điểm đón", "secondary", "xl", "navigation", full=True, href="D-022.dc.html")
    elif state == "nav":
        m = M(route=cu.TO_PICK, pins=[("pickup", 0.72, 0.47)], driver=(0.9, 0.34))
        head = job_header("proofPending", "Đến điểm đón · 4 phút", cu.PICK + " · Cổng Hải Triều", ref)
        body_ = cust + card(row(icon("message", 18, C["t2"]), txt("“Mình đứng ở cổng Hải Triều, áo xanh nhé.”", "bsm", C["t1"]), gap=10), pad=12, bg=C["ink25"]) + btn("Xem chứng từ khách gửi", "primary", "xl", "image", full=True, href="D-023.dc.html")
    elif state == "arrived":
        m = M(pins=[("pickup", 0.72, 0.47)], driver=(0.74, 0.46))
        head = job_header("proofVerified", "Đã nhận đủ 48.000đ", "Đi tới điểm đón", ref)
        body_ = cust + addr_block(cu.PICK, cu.DROP, cu.PICK_S) + btn("Tôi đã đến điểm đón", "primary", "xl", "map-pin", full=True, href="D-026.dc.html")
    elif state == "waiting":
        m = M(pins=[("pickup", 0.72, 0.47)], driver=(0.73, 0.465))
        head = job_header("arrived", "Đang chờ khách", "Đã chờ 01:48 · thời gian chờ tối đa 5 phút", ref)
        body_ = cust + progress(36, C["warn_b"]) + btn("Bắt đầu chuyến", "primary", "xl", "play", full=True, href="D-027.dc.html") + btn("Khách không đến", "ghost", "lg", full=True, href="D-029.dc.html")
    elif state == "locked":
        m = M(pins=[("pickup", 0.72, 0.47)], driver=(0.73, 0.465))
        head = job_header("proofPending", "Chưa xác nhận tiền", "Khách chưa gửi chứng từ", ref)
        body_ = (cust + banner("warning", "Chưa thể bắt đầu chuyến", "Chỉ bắt đầu khi bạn đã xác nhận nhận đủ 48.000đ. Nhắn hoặc gọi khách để nhắc chuyển khoản.")
                 + btn("Bắt đầu chuyến", "disabled", "xl", "lock", full=True) + btn("Tôi đã nhận đủ tiền", "secondary", "lg", full=True, href="D-023.dc.html"))
    elif state == "trip":
        m = M(route=cu.ROUTE[1:], pins=[("dropoff", 0.3, 0.17)], driver=(0.72, 0.42))
        head = job_header("inProgress", "Đến ĐH Kinh tế · 9 phút", "2,6 km · " + cu.DROP_S, ref)
        body_ = cust + btn("Hoàn thành chuyến", "primary", "xl", "check", full=True, href="D-028.dc.html") + row(btn("Báo sự cố", "ghost", "md", "flag", href="D-029.dc.html"), spacer())
    top = row(circle_btn("chevron-down", "Thu nhỏ"), spacer(), circle_btn("navigation", "Mở bản đồ dẫn đường"))
    sheet = head + f'<div style="padding: 0 16px {BOT}px; display: flex; flex-direction: column; gap: 12px">{body_}</div>'
    return phone(map_screen(m, sheet, top))


@frame("D-020", "Ride offer accepted", "Đi xe · Nhận chuyến")
def d020():
    return [("Đã nhận chuyến", ride_job("accepted"))]


@frame("D-021", "Ride offer rejected / timeout", "Đi xe · Nhận chuyến")
def d021():
    b = drv_home("nojobs")
    t = toast("Đã bỏ qua yêu cầu. Bạn vẫn đang trực tuyến.", "info")
    t2 = toast("Hết thời gian phản hồi — yêu cầu đã chuyển cho tài xế khác.", "clock")
    wrap = lambda tt: b.replace('</div></div></div>', '</div></div></div>', 1)[:-6] + f'<div style="position: absolute; left: 16px; right: 16px; top: 190px">{tt}</div></div>'
    return [("Đã từ chối", wrap(t)), ("Hết thời gian", wrap(t2))]


@frame("D-022", "Ride pickup navigation", "Đi xe · Đón khách & thanh toán")
def d022():
    return [("Đến điểm đón", ride_job("nav"))]


def proof_review(service="ride"):
    amt, ref, name = ("48.000đ", "R-7Q2K9", "Minh Anh") if service == "ride" else ("137.000đ", "F-3M8TP", "Minh Anh")
    return phone(topbar("Chứng từ của khách", True, sub=ref) + body(
        pill("proofPending") + h(f"Kiểm tra tài khoản đã nhận {amt}", "hlg")
        + f'<a href="D-058.dc.html" style="display: block; text-decoration: none">{photo("100%", 260, "Ảnh chuyển khoản khách gửi · 08:14 · bấm để phóng to", "zoom-in", 12)}</a>'
        + card(kv("Số tiền cần nhận", amt, True) + kv("Nội dung", "ONW " + ref.replace("-", ""), True) + kv("Người gửi", name) + kv("Gửi lúc", "08:14"), pad=14, gap=8)
        + txt("Mở ứng dụng ngân hàng để kiểm tra. Chỉ bấm xác nhận khi tiền đã vào tài khoản.", "bsm", C["t2"]), bg="#FFFFFF", gap=14)
        + bottom(btn("Tôi đã nhận đủ tiền", "primary", "xl", "check", full=True, href="D-025.dc.html" if service == "ride" else "D-034.dc.html")
                 + btn("Chưa nhận được / chưa đủ", "danger", "lg", full=True, href="D-024.dc.html" if service == "ride" else "D-033.dc.html")))


@frame("D-023", "Ride payment proof review", "Đi xe · Đón khách & thanh toán")
def d023():
    return [("Chứng từ đã gửi", proof_review())]


def not_received(service="ride"):
    amt = "48.000đ" if service == "ride" else "137.000đ"
    inner = (f'<div style="padding: 0 16px {BOT}px; display: flex; flex-direction: column; gap: 12px">'
             f'{txt("Chọn tình huống. Hãy nhắn khách trước — đa số trường hợp chỉ là chuyển chậm hoặc thiếu.", "bsm", C["t2"])}'
             f'{radio("Chưa nhận được tiền", True)}{radio("Nhận chưa đủ số tiền")}{radio("Ảnh chứng từ không khớp giao dịch")}'
             f'{field("Số tiền đã nhận (nếu có)", "", "VD: 40.000", mono=True, helper="Không bắt buộc. Giúp khách biết cần chuyển thêm bao nhiêu.")}'
             f'{btn("Nhắn khách kiểm tra lại", "secondary", "lg", "message", full=True)}{btn("Báo tranh chấp thanh toán", "danger", "lg", "flag", full=True)}'
             f'{txt("Báo tranh chấp sẽ tạm dừng " + ("chuyến" if service == "ride" else "đơn") + " và chuyển cho Onway xem xét. Không bắt đầu chuyến/mua món khi chưa nhận đủ " + amt + ".", "cap", C["t3"])}</div>')
    return phone(sheet_over(proof_review(service), inner, title="Chưa nhận được tiền?"))


@frame("D-024", "Ride money not received", "Đi xe · Đón khách & thanh toán")
def d024():
    return [("Báo chưa nhận tiền", not_received())]


@frame("D-025", "Ride arrived pickup", "Đi xe · Đón khách & thanh toán")
def d025():
    return [("Đến điểm đón", ride_job("arrived")), ("Đang chờ khách", ride_job("waiting"))]


@frame("D-026", "Ride start trip", "Đi xe · Trong chuyến")
def d026():
    return [("Bắt đầu bị khoá (chưa nhận tiền)", ride_job("locked")), ("Sẵn sàng bắt đầu", ride_job("waiting"))]


@frame("D-027", "Ride in trip", "Đi xe · Trong chuyến")
def d027():
    return [("Trong chuyến", ride_job("trip"))]


@frame("D-028", "Ride completed", "Đi xe · Trong chuyến")
def d028():
    return [("Hoàn thành", phone(topbar("", False, right=ibtn("x", "Đóng", "ghost", 44), border=False) + body(
        f'<div style="display: flex; flex-direction: column; align-items: center; gap: 8px; text-align: center">'
        f'<div style="width: 64px; height: 64px; border-radius: 999px; background: {C["ok_bg"]}; display: flex; align-items: center; justify-content: center">{icon("check", 32, C["ok"], 2.5)}</div>'
        f'{h("Hoàn thành chuyến", "hlg")}{txt("Bạn nhận", "cap", C["t3"])}{num("48.000đ", 36, weight=700)}{txt("100% — Onway thu 0% hoa hồng", "bsm", C["ok"], extra="font-weight: 600")}</div>'
        + card(kv("Mã chuyến", "R-7Q2K9", True) + kv("Quãng đường", "3,2 km · 14 phút") + kv("Thanh toán", "Khách chuyển khoản · đã xác nhận 08:16") + kv("Hôm nay", "10 chuyến · 460.000đ"), pad=14, gap=8)
        + card(col(txt("Đánh giá khách Minh Anh", "bmd", extra="font-weight: 600"), stars(5, 0, 28), gap=8), pad=14), bg="#FFFFFF", gap=14)
        + bottom(btn("Tiếp tục nhận chuyến", "primary", "xl", full=True, href="D-015.dc.html") + btn("Báo vấn đề với khách", "ghost", "lg", "flag", full=True), border=False)))]


def issue_screen(service="ride", sel=0):
    opts = (["Khách không đến điểm đón", "Khách huỷ sau khi chuyển tiền", "Tranh chấp thanh toán", "Sự cố an toàn / tai nạn", "Lý do khác"] if service == "ride"
            else ["Quán đóng cửa", "Món hết, khách từ chối đề xuất", "Không liên lạc được khách", "Tranh chấp thanh toán", "Lý do khác"])
    head = "Huỷ chuyến / báo sự cố" if service == "ride" else "Huỷ đơn / báo sự cố"
    rs = "".join(radio(o, i == sel) for i, o in enumerate(opts))
    note = ("Nếu khách đã chuyển tiền mà không đi, bạn chờ đủ 5 phút rồi báo. Việc hoàn tiền cho khách do hai bên tự xử lý theo kết luận của Onway."
            if service == "ride" else "Nếu bạn chưa mua món, hãy hoàn lại tiền món cho khách theo hướng dẫn sau khi Onway xác nhận. Bên nào có lỗi, bên đó chịu trách nhiệm.")
    return phone(topbar(head, True, sub="R-7Q2K9" if service == "ride" else "F-3M8TP") + body(
        txt("Chọn lý do", "lbl") + col(rs, gap=0) + field("Mô tả thêm", "Đã chờ 6 phút, gọi 3 lần khách không nghe." if sel == 0 and service == "ride" else "", textarea=True)
        + row(photo(80, 80, "Ảnh", "camera", 10), txt("Thêm ảnh (VD: ảnh điểm đón, ảnh quán đóng cửa)", "cap", C["t3"]), gap=10)
        + banner("info", "Onway xem xét trong 24 giờ", note), bg="#FFFFFF", gap=12)
        + bottom(btn("Gửi báo cáo", "primary", "lg", full=True)))


@frame("D-029", "Ride canceled / issue", "Đi xe · Trong chuyến")
def d029():
    return [("Chọn lý do", issue_screen("ride"))]


# ================= FOOD JOB =================
@frame("D-030", "Food offer received", "Đặt món · Nhận đơn")
def d030():
    return [("Đếm ngược", offer("food", 11))]


def food_job(state):
    ref = num("F-3M8TP", 13, C["t3"])
    cust = person_row("Minh Anh", "Khách · giao đến 142 Lê Văn Sỹ", "MA")
    top = row(circle_btn("chevron-down", "Thu nhỏ"), spacer(), circle_btn("navigation", "Mở bản đồ dẫn đường"))
    if state == "to_outlet":
        m = M(route=[(0.1, 0.24), (0.3, 0.24), (0.3, 0.44)], pins=[("outlet", 0.3, 0.44)], driver=(0.1, 0.24))
        head = job_header("proofPending", "Chờ khách chuyển 137.000đ", "Quán cách 0,8 km · đi tới quán trong lúc chờ", ref)
        b = cust + banner("warning", "Chưa đặt món khi chưa nhận đủ tiền", "Khi khách gửi chứng từ, kiểm tra tài khoản rồi xác nhận.") + btn("Xem chứng từ khách gửi", "primary", "xl", "image", full=True, href="D-032.dc.html")
    elif state == "picked":
        m = M(pins=[("outlet", 0.3, 0.44)], driver=(0.31, 0.43))
        head = job_header("pickup", "Đã lấy đủ món", "Kiểm tra túi món trước khi đi", ref)
        b = (card(checkbox("2 × Cơm tấm sườn bì chả", True) + checkbox("1 × Trà đá", True) + checkbox("Hoá đơn của quán", True, "Chụp ảnh hoá đơn làm bằng chứng"), pad=14, gap=8)
             + row(photo(72, 72, "", "camera", 8), txt("Ảnh hoá đơn 120.000đ · 11:28", "bsm", C["t2"]), gap=10) + btn("Bắt đầu giao", "primary", "xl", "navigation", full=True, href="D-041.dc.html"))
    elif state == "delivering":
        m = M(route=cu.F_ROUTE[1:], pins=[("dropoff", 0.72, 0.17)], driver=(0.52, 0.36))
        head = job_header("delivering", "Giao đến khách · 12 phút", "142 Lê Văn Sỹ, Phường 10, Phú Nhuận", ref)
        b = cust + card(row(icon("message", 18, C["t2"]), txt("Ghi chú: “Hẻm 142, cổng sắt màu xanh, gọi khi tới.”", "bsm", C["t1"]), gap=10), pad=12, bg=C["ink25"]) + btn("Đã giao cho khách", "primary", "xl", "check", full=True, href="D-042.dc.html")
    sheet = head + f'<div style="padding: 0 16px {BOT}px; display: flex; flex-direction: column; gap: 12px">{b}</div>'
    return phone(map_screen(m, sheet, top))


@frame("D-031", "Food accepted / go to outlet", "Đặt món · Nhận đơn")
def d031():
    return [("Đi tới quán", food_job("to_outlet"))]


@frame("D-032", "Food payment proof review", "Đặt món · Nhận đơn")
def d032():
    return [("Kiểm tra chứng từ", proof_review("food"))]


@frame("D-033", "Food money not received", "Đặt món · Nhận đơn")
def d033():
    return [("Báo chưa nhận tiền", not_received("food"))]


def at_outlet():
    items = (card(row(checkbox("2 × Cơm tấm sườn bì chả", False, "Cơm thường · giá trên Onway 55.000đ/phần"), spacer()) + row(checkbox("1 × Trà đá", False, "Ly 500 ml · 5.000đ"), spacer())
                  + divider() + kv("Tổng tiền món theo Onway", "115.000đ", True) + kv("Khách đã chuyển (gồm phí giao)", "137.000đ", True), pad=14, gap=10))
    return phone(topbar("Tại quán", True, sub="Cơm Tấm Sà Bì · F-3M8TP") + body(
        pill("atOutlet") + h("Đặt món theo danh sách", "hlg")
        + txt("Đây là ảnh chụp thực đơn lúc khách đặt. Nếu giá hoặc món khác, gửi đề xuất cho khách <b>trước khi mua</b>.", "bmd", C["t2"])
        + items + card(row(icon("store", 18, C["t2"]), txt("Ghi chú của khách cho quán: “ít mỡ hành”", "bsm"), gap=10), pad=12, bg=C["ink25"]), bg="#FFFFFF", gap=14)
        + bottom(btn("Đã mua & lấy đủ món", "primary", "xl", "check", full=True, href="D-040.dc.html") + btn("Món/giá khác — gửi đề xuất", "outline", "lg", "pencil", full=True, href="D-035.dc.html")))


@frame("D-034", "At outlet / order items", "Đặt món · Tại quán")
def d034():
    return [("Danh sách món", at_outlet())]


def change_form():
    return phone(topbar("Đề xuất thay đổi", True, sub="F-3M8TP") + body(
        txt("Loại thay đổi", "lbl") + chip_row([tag("Giá khác", True), tag("Hết món"), tag("Tuỳ chọn khác"), tag("Khác")])
        + select("Món bị ảnh hưởng", "2 × Cơm tấm sườn bì chả")
        + row(f'<div style="flex: 1">{field("Giá trên Onway", "55.000", mono=True, disabled=True)}</div>', f'<div style="flex: 1">{field("Giá tại quán", "60.000", mono=True)}</div>', gap=10, align="flex-start")
        + card(kv("Khách cần chuyển thêm", "+10.000đ", True), pad=12, bg=C["warn_bg"], extra=f"border-color: {C['warn_b']}55")
        + field("Ghi chú cho khách", "Quán tăng giá từ tuần trước ạ.") + row(photo(80, 80, "Bảng giá", "camera", 10), txt("Ảnh bảng giá/menu tại quán (khuyến khích)", "cap", C["t3"]), gap=10)
        + txt("Khách có 5 phút để trả lời. Không mua món bị ảnh hưởng khi khách chưa đồng ý.", "cap", C["t3"]), bg="#FFFFFF", gap=12)
        + bottom(btn("Gửi đề xuất cho khách", "primary", "lg", "send", full=True, href="D-036.dc.html")))


@frame("D-035", "Food change needed form", "Đặt món · Tại quán")
def d035():
    return [("Giá khác", change_form())]


def proposal_wait(state="waiting"):
    if state == "waiting":
        top = pill("changeRequested", "Chờ khách trả lời")
        t = h("Đang chờ khách đồng ý", "hlg")
        timer = card(row(icon("timer", 22, C["warn"]), num("04:32", 28, C["warn"], 700), spacer(), txt("Hết giờ: Onway xem xét đơn", "cap", C["t2"], extra="max-width: 140px; text-align: right"), gap=10), pad=14, bg=C["warn_bg"], extra=f"border-color: {C['warn_b']}55")
        cta = btn("Gọi khách", "secondary", "lg", "phone", full=True) + btn("Huỷ đề xuất", "ghost", "lg", full=True)
    elif state == "accepted":
        top = pill("confirmed", "Khách đã đồng ý")
        t = h("Khách đồng ý +10.000đ", "hlg")
        timer = banner("success", "Đơn đã cập nhật", "Tổng mới 147.000đ. Chờ khách chuyển bổ sung rồi mới mua phần món thay đổi.")
        cta = btn("Xem thanh toán bổ sung", "primary", "xl", full=True, href="D-039.dc.html")
    elif state == "rejected":
        top = pill("rejected", "Khách từ chối")
        t = h("Khách không đồng ý thay đổi", "hlg")
        timer = banner("danger", "Không mua món bị ảnh hưởng", "Chọn bước tiếp theo. Nếu huỷ đơn, hoàn lại tiền khách đã chuyển cho phần chưa mua.")
        cta = btn("Mua phần còn lại (1 × Trà đá)", "secondary", "lg", full=True) + btn("Huỷ đơn & báo Onway", "danger", "lg", full=True, href="D-043.dc.html")
    else:
        top = pill("expired", "Hết thời gian")
        t = h("Khách không trả lời sau 5 phút", "hlg")
        timer = banner("warning", "Đơn chuyển Onway xem xét", "Đừng mua món bị ảnh hưởng. Onway sẽ báo bạn huỷ hay giao phần còn lại trong vài phút.")
        cta = btn("Gọi khách lần nữa", "secondary", "lg", "phone", full=True) + btn("Liên hệ hỗ trợ", "ghost", "lg", full=True)
    return phone(topbar("Đề xuất thay đổi", True, sub="F-3M8TP") + body(top + t + timer
                                                                       + card(kv("Món", "2 × Cơm tấm sườn bì chả") + kv("Giá trên Onway → tại quán", "110.000đ → 120.000đ") + kv("Chênh lệch", "+10.000đ", True), pad=14, gap=8),
                                                                       bg="#FFFFFF", gap=14) + bottom(cta))


@frame("D-036", "Food proposal waiting customer", "Đặt món · Tại quán")
def d036():
    return [("Chờ 5 phút", proposal_wait())]


@frame("D-037", "Proposal accepted", "Đặt món · Tại quán")
def d037():
    return [("Khách đồng ý", proposal_wait("accepted"))]


@frame("D-038", "Proposal rejected / timeout", "Đặt món · Tại quán")
def d038():
    return [("Khách từ chối", proposal_wait("rejected")), ("Hết thời gian", proposal_wait("timeout"))]


@frame("D-039", "Supplemental payment pending", "Đặt món · Tại quán")
def d039():
    return [("Chờ tiền bổ sung", phone(topbar("Thanh toán bổ sung", True, sub="F-3M8TP") + body(
        pill("proofPending") + h("Chờ khách chuyển thêm 10.000đ", "hlg")
        + card(timeline([("Khách đồng ý đề xuất", "11:16", "done"), ("Khách chuyển 10.000đ & gửi chứng từ", "Đang chờ", "current"), ("Bạn xác nhận đã nhận đủ", "", "todo"), ("Mua phần món thay đổi", "", "todo")], True), pad=16)
        + card(kv("Tổng mới", "147.000đ", True) + kv("Đã nhận", "137.000đ", True) + kv("Còn chờ", "10.000đ", True), pad=14, gap=8), bg="#FFFFFF", gap=14)
        + bottom(btn("Tôi đã nhận đủ 10.000đ", "disabled", "xl", full=True) + btn("Nhắn khách", "outline", "lg", "message", full=True))))]


@frame("D-040", "Food picked up", "Đặt món · Giao món")
def d040():
    return [("Đã lấy món", food_job("picked"))]


@frame("D-041", "Food delivering", "Đặt món · Giao món")
def d041():
    return [("Đang giao", food_job("delivering"))]


@frame("D-042", "Food delivered", "Đặt món · Giao món")
def d042():
    return [("Đã giao", phone(topbar("", False, right=ibtn("x", "Đóng", "ghost", 44), border=False) + body(
        f'<div style="display: flex; flex-direction: column; align-items: center; gap: 8px; text-align: center">'
        f'<div style="width: 64px; height: 64px; border-radius: 999px; background: {C["ok_bg"]}; display: flex; align-items: center; justify-content: center">{icon("check", 32, C["ok"], 2.5)}</div>'
        f'{h("Đã giao đơn", "hlg")}{txt("Phí giao bạn nhận", "cap", C["t3"])}{num("22.000đ", 36, weight=700)}</div>'
        + card(kv("Khách đã chuyển", "137.000đ", True) + kv("Bạn đã trả quán", "115.000đ", True) + divider() + kv("Phí giao (100% của bạn)", "22.000đ", True) + kv("Mã đơn", "F-3M8TP", True), pad=14, gap=8)
        + card(col(txt("Đánh giá khách", "bmd", extra="font-weight: 600"), stars(5, 0, 28), gap=8), pad=14), bg="#FFFFFF", gap=14)
        + bottom(btn("Tiếp tục nhận việc", "primary", "xl", full=True, href="D-015.dc.html"), border=False)))]


@frame("D-043", "Food issue/cancel reason", "Đặt món · Giao món")
def d043():
    return [("Quán đóng cửa", issue_screen("food", 0)), ("Không liên lạc được khách", issue_screen("food", 2))]


# ================= CHAT / LOCK =================
@frame("D-044", "Chat room", "Chat & gọi điện")
def d044():
    return [("Văn bản, ảnh, đã xem", cu.chat("default", "d"))]


@frame("D-045", "Chat image upload failed", "Chat & gọi điện")
def d045():
    return [("Ảnh gửi lỗi", cu.chat("failed", "d"))]


@frame("D-046", "Chat offline / reconnecting", "Chat & gọi điện")
def d046():
    return [("Đang kết nối lại", cu.chat("offline", "d"))]


@frame("D-047", "Driver locked notice", "Khoá tài khoản & kháng nghị")
def d047():
    return [("Bị khoá tạm", status_screen("lock", "err", pill("locked", "Tạm khoá"), "Tài khoản tạm khoá",
                                          "Bạn tạm thời không thể trực tuyến trong lúc Onway xem xét. Đây chưa phải kết luận vi phạm.",
                                          card(kv("Lý do", "Nhiều khiếu nại thanh toán trong 30 ngày") + kv("Bắt đầu", "24/09 14:05") + kv("Hạn xem xét", "Trong 24 giờ") + kv("Mã hồ sơ", "RK-240924-0007", True), pad=14, gap=8)
                                          + txt("Vì lý do bảo mật, chi tiết bằng chứng của người khiếu nại không được hiển thị.", "cap", C["t3"]),
                                          btn("Gửi kháng nghị", "primary", "lg", full=True, href="D-048.dc.html") + btn("Liên hệ hỗ trợ", "ghost", "lg", full=True)))]


def appeal(done=False):
    if done:
        return status_screen("check-circle", "ok", pill("appeal", "Đã gửi kháng nghị"), "Onway đã nhận kháng nghị",
                             "Risk/Fraud Analyst sẽ xem xét cùng hồ sơ RK-240924-0007 và phản hồi trong 24 giờ.",
                             card(timeline([("Tạm khoá", "24/09 14:05", "done"), ("Bạn gửi kháng nghị", "24/09 14:40", "done"), ("Onway xem xét", "Trước 25/09 14:05", "current"), ("Kết luận", "", "todo")], True), pad=16),
                             btn("Về trang chủ", "secondary", "lg", full=True))
    return phone(topbar("Kháng nghị", True, sub="RK-240924-0007") + body(
        txt("Giải thích tình huống và gửi bằng chứng (sao kê, ảnh chat…). Onway xem xét trung lập với cả hai bên.", "bmd", C["t2"])
        + field("Nội dung kháng nghị", "Các khiếu nại ngày 20 và 22/09 là do khách chuyển nhầm tài khoản, tôi đã nhắn và khách đã chuyển lại. Tôi gửi kèm sao kê.", textarea=True)
        + txt("Bằng chứng", "lbl") + row(photo(88, 88, "Sao kê", "file", 10), photo(88, 88, "Ảnh chat", "image", 10), f'<button type="button" style="width: 88px; height: 88px; border-radius: 10px; border: 1.5px dashed {C["b3"]}; background: {C["ink25"]}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; font-family: {FONT}; font-size: 12px; color: {C["t2"]}">{icon("plus", 20)}Thêm</button>', gap=8)
        + checkbox("Tôi xác nhận thông tin trên là đúng sự thật", True), bg="#FFFFFF", gap=14)
        + bottom(btn("Gửi kháng nghị", "primary", "lg", full=True)))


@frame("D-048", "Lock appeal form", "Khoá tài khoản & kháng nghị")
def d048():
    return [("Soạn kháng nghị", appeal()), ("Đã gửi", appeal(True))]


# ================= COMMON =================
def earnings(state="list"):
    if state == "empty":
        return phone(topbar("Thu nhập", True) + body(empty_state("banknote", "Chưa có thu nhập", "Hoàn thành chuyến đầu tiên để xem thu nhập ở đây."), bg="#FFFFFF", extra="justify-content: center"))
    bars = "".join(f'<div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 6px"><div style="width: 100%; height: {v}px; border-radius: 4px; background: {C["inverse"] if i == 6 else C["b3"]}"></div><span style="{TY["cap"]}; color: {C["t3"]}">{d}</span></div>'
                   for i, (v, d) in enumerate(zip([60, 84, 40, 96, 72, 110, 88], ["T5", "T6", "T7", "CN", "T2", "T3", "T4"])))
    return phone(topbar("Thu nhập", True) + body(
        segmented(["Hôm nay", "Tuần này", "Tháng này"], 1) + card(row(col(txt("Tuần 23–29/09", "cap", C["t3"]), num("2.846.000đ", 30, weight=700), gap=2), spacer(), txt("62 chuyến/đơn", "bsm", C["t2"]))
                                                                  + f'<div style="display: flex; gap: 8px; align-items: flex-end; height: 140px">{bars}</div>', pad=16)
        + row(stat("Đi xe", "1.920.000đ"), stat("Phí giao", "926.000đ"), gap=8)
        + txt("Thu nhập = 100% tiền khách chuyển cho bạn. Onway không trừ hoa hồng.", "cap", C["t3"])
        + list_row("Lịch sử chuyến và đơn", "62 mục tuần này", "history", href="D-053.dc.html", pad="14px 0"), bg="#FFFFFF", gap=12))


@frame("D-049", "Earnings/history", "Tài khoản & hỗ trợ")
def d049():
    return [("Danh sách", earnings()), ("Trống", earnings("empty"))]


@frame("D-050", "Notifications", "Tài khoản & hỗ trợ")
def d050():
    items = (cu.notif_item("bike", "Yêu cầu chuyến mới", "Bitexco → ĐH Kinh tế · 48.000đ", "Vừa xong", True)
             + cu.notif_item("banknote", "Khách đã gửi chứng từ", "Minh Anh gửi ảnh chuyển khoản 48.000đ · R-7Q2K9", "1 phút trước", True)
             + cu.notif_item("message", "Tin nhắn mới", "Minh Anh: “Mình đứng ở cổng Hải Triều…”", "2 phút trước")
             + cu.notif_item("lock", "Tài khoản được mở khoá", "Onway đã kết luận hồ sơ RK-240910-0003. Bạn có thể trực tuyến.", "12/09, 16:20")
             + cu.notif_item("check-circle", "Phí nền tảng đã xác minh", "Gói 18 tháng hoạt động đến 24/03/2028.", "24/09, 10:40"))
    return [("Việc, thanh toán, chat, khoá", phone(topbar("Thông báo", True, right=btn("Đọc hết", "ghost", "sm")) + f'<div style="flex-grow: 1; background: #FFFFFF; overflow: hidden">{items}</div>'))]


@frame("D-051", "Account/settings", "Tài khoản & hỗ trợ")
def d051():
    rows = (list_row("Hồ sơ tài xế", "Trần Văn Hùng · 0901 234 567", "user")
            + list_row("Xe & giấy tờ", "Honda Vision · 59-X2 123.45", "id-card")
            + list_row("Tài khoản nhận tiền", "Vietcombank · ••• 4567 89", "bank")
            + list_row("Gói phí nền tảng", "Hiệu lực đến 24/03/2028", "banknote", href="D-014.dc.html", right=pill("active", size="sm"))
            + list_row("Quyền riêng tư & đồng ý", "Vị trí, thiết bị, chứng từ", "shield", href="D-059.dc.html")
            + list_row("Trợ giúp", "", "help", href="D-052.dc.html", border=False))
    return [("Mặc định", phone(topbar("Tài khoản", True) + body(row(avatar("TH", 56), col(txt("Trần Văn Hùng", "hsm"), row(stars(5, 5, 14), txt("4,9 · 1.204 chuyến", "cap", C["t3"]), gap=6), gap=4), gap=14)
                                                               + f'<div style="margin: 0 -16px; border-top: 1px solid {C["b1"]}">{rows}</div>' + btn("Đăng xuất", "outline", "lg", "log-out", full=True), bg="#FFFFFF", gap=14)))]


@frame("D-052", "Help/support", "Tài khoản & hỗ trợ")
def d052():
    faq = "".join(list_row(q, "", "help", pad="14px 0") for q in ["Khách chưa chuyển tiền thì làm gì?", "Giá món tại quán khác trên ứng dụng?", "Vì sao tài khoản bị tạm khoá?", "Hoàn phí nền tảng thế nào?"])
    return [("Mặc định", phone(topbar("Trợ giúp", True) + body(search_bar("Tìm câu hỏi") + ovl("Câu hỏi thường gặp") + f'<div style="margin-top: -8px">{faq}</div>'
                                                                + ovl("Hồ sơ của tôi") + list_row("Khiếu nại & kháng nghị", "2 hồ sơ đang mở", "scale", href="D-055.dc.html", pad="14px 0")
                                                                + row(btn("Gọi tổng đài", "secondary", "lg", "phone", full="grow"), btn("Gửi email", "outline", "lg", "mail", full="grow"), gap=8), bg="#FFFFFF", gap=12)))]


def job_hist(state="list"):
    if state == "empty":
        c = empty_state("history", "Chưa có chuyến nào", "Lịch sử Đi xe và Đặt món sẽ hiển thị ở đây.")
    else:
        its = [("bike", "Bitexco → ĐH Kinh tế", "Hôm nay 08:27 · R-7Q2K9", "48.000đ", "completed", "D-054.dc.html"),
               ("utensils", "Cơm Tấm Sà Bì → Lê Văn Sỹ", "Hôm qua 11:02 · F-3M8TP", "22.000đ", "completed", "D-054.dc.html"),
               ("bike", "Bến Thành → Tân Định", "22/09 18:10 · R-2H8QD", "32.000đ", "disputed", "D-054.dc.html"),
               ("bike", "Nhà thờ Đức Bà → Q.4", "21/09 07:50 · R-9L4AB", "30.000đ", "cancelled", "D-054.dc.html")]
        if state == "ride":
            its = [i for i in its if i[0] == "bike"]
        c = "".join(cu.hist_item(*i) for i in its)
    return phone(topbar("Lịch sử", True, right=ibtn("filter", "Lọc", "ghost", 44)) + body(segmented(["Tất cả", "Đi xe", "Đặt món"], 1 if state == "ride" else 0) + f'<div style="margin-top: -8px">{c}</div>', bg="#FFFFFF", gap=12))


@frame("D-053", "Job history", "Tài khoản & hỗ trợ")
def d053():
    return [("Danh sách", job_hist()), ("Lọc Đi xe", job_hist("ride")), ("Trống", job_hist("empty"))]


def job_hist_detail(state="completed"):
    p = {"completed": pill("completed"), "cancelled": pill("cancelled"), "disputed": pill("disputed")}[state]
    b = {"completed": "", "cancelled": banner("neutral", "Khách huỷ trước khi đón", "Không phát sinh thanh toán."),
         "disputed": banner("danger", "Đang tranh chấp thanh toán", "Hồ sơ CS-240922-0098 — Onway yêu cầu bạn gửi sao kê trước 25/09 18:00.", action=btn("Phản hồi", "outline", "sm", href="D-056.dc.html"))}[state]
    return phone(topbar("Chi tiết chuyến", True, sub="R-7Q2K9") + body(row(p, spacer(), txt("24/09/2026", "bsm", C["t2"])) + b
                                                                      + card(addr_block(cu.PICK, cu.DROP, "08:27", "08:41"), pad=14)
                                                                      + card(kv("Khách", "Minh Anh") + kv("Giá chuyến", "48.000đ", True) + kv("Thanh toán", "Đã xác nhận 08:16") + kv("Quãng đường", "3,2 km"), pad=14, gap=8),
                                                                      bg="#FFFFFF", gap=12) + bottom(btn("Báo vấn đề", "outline", "lg", "flag", full=True)))


@frame("D-054", "Job history detail", "Tài khoản & hỗ trợ")
def d054():
    return [("Hoàn thành", job_hist_detail()), ("Đã huỷ", job_hist_detail("cancelled")), ("Tranh chấp", job_hist_detail("disputed"))]


def drv_cases(state="list"):
    if state == "empty":
        return phone(topbar("Khiếu nại & kháng nghị", True) + body(empty_state("scale", "Không có hồ sơ nào", "Khiếu nại liên quan đến bạn và kháng nghị sẽ xuất hiện ở đây."), bg="#FFFFFF", extra="justify-content: center"))
    c = (list_row("Tranh chấp thanh toán · R-2H8QD", "CS-240922-0098 · Cần bạn phản hồi trước 25/09 18:00", "banknote", right=pill("changeRequested", "Cần phản hồi", "sm"), href="D-056.dc.html", pad="14px 0")
         + list_row("Kháng nghị tạm khoá", "RK-240924-0007 · Gửi 24/09 14:40", "lock", right=pill("appeal", size="sm"), href="D-056.dc.html", pad="14px 0")
         + list_row("Thái độ phục vụ · R-1K3ZP", "CS-240910-0021 · Kết luận 12/09", "user", right=pill("finalized", size="sm"), href="D-056.dc.html", pad="14px 0"))
    return phone(topbar("Khiếu nại & kháng nghị", True) + body(c, bg="#FFFFFF", gap=0))


@frame("D-055", "Case / complaint list", "Khoá tài khoản & kháng nghị")
def d055():
    return [("Danh sách", drv_cases()), ("Trống", drv_cases("empty"))]


@frame("D-056", "Case / complaint detail", "Khoá tài khoản & kháng nghị")
def d056():
    return [("Yêu cầu phản hồi", phone(topbar("Hồ sơ", True, sub="CS-240922-0098") + body(
        row(pill("changeRequested", "Cần phản hồi"), spacer(), txt("Thanh toán · R-2H8QD", "bsm", C["t2"]))
        + card(timeline([("Khách gửi khiếu nại", "22/09 18:40", "done"), ("Onway thu thập bằng chứng", "23/09 09:00", "done"), ("Chờ bạn phản hồi", "Hạn 25/09 18:00", "current"), ("Kết luận", "", "todo")], True), pad=16)
        + card(ovl("Onway yêu cầu") + txt("Gửi ảnh sao kê tài khoản Vietcombank ngày 22/09 từ 18:00–18:30 để đối chiếu giao dịch 32.000đ.", "bmd"), pad=14, bg=C["warn_bg"], extra=f"border-color: {C['warn_b']}55")
        + field("Phản hồi của bạn", "", "Mô tả những gì đã xảy ra", textarea=True) + upload_tile("empty", "Ảnh sao kê"), bg="#FFFFFF", gap=12)
        + bottom(btn("Gửi phản hồi", "primary", "lg", full=True))))]


@frame("D-057", "Direct call confirmation", "Chat & gọi điện")
def d057():
    inner = (f'<div style="padding: 0 16px {BOT}px; display: flex; flex-direction: column; gap: 12px">{row(avatar("MA", 48), col(txt("Minh Anh (khách)", "bmd", extra="font-weight: 700"), num("0901 ••• 567", 14, C["t2"]), gap=2), gap=12)}'
             f'{txt("Gọi bằng số thật qua nhà mạng. Chỉ gọi để trao đổi về chuyến/đơn đang diễn ra.", "bsm", C["t2"])}{btn("Gọi khách", "primary", "lg", "phone", full=True)}{btn("Gọi tổng đài Onway", "outline", "lg", "help", full=True)}</div>')
    un = (f'<div style="padding: 0 16px {BOT}px; display: flex; flex-direction: column; gap: 12px">{banner("neutral", "Khách đã ẩn số điện thoại", "Khách chọn không hiển thị số. Hãy nhắn tin trong ứng dụng.", "phone")}{btn("Nhắn tin cho khách", "secondary", "lg", "message", full=True)}</div>')
    return [("Gọi khách / tổng đài", phone(sheet_over(ride_job("nav"), inner, title="Gọi điện"))), ("Không khả dụng", phone(sheet_over(ride_job("nav"), un, title="Gọi điện")))]


@frame("D-058", "Proof/evidence image viewer", "Chat & gọi điện")
def d058():
    def v(expired=False):
        c = (f'<div style="flex-grow: 1; display: flex; align-items: center; justify-content: center; padding: 16px">'
             + (empty_state("clock", "Liên kết ảnh đã hết hạn", "Ảnh chứng từ được bảo vệ bằng liên kết tạm thời. Tải lại để xem tiếp.", btn("Tải lại ảnh", "inverse", "md", "refresh")).replace(C["t1"], "#FFFFFF").replace(C["t2"], C["tinv2"]).replace(C["sunken"], C["inverse2"])
                if expired else f'<div role="img" aria-label="Ảnh chuyển khoản của khách" style="width: 320px; height: 560px; border-radius: 8px; background: #2F2E2E; display: flex; align-items: center; justify-content: center; color: #A3A2A0">{icon("image", 40)}</div>')
             + "</div>")
        head = f'<div style="display: flex; align-items: center; gap: 8px; padding: {TOP}px 8px 8px">{ibtn("x", "Đóng", "ghost", 44).replace(C["t1"], "#FFFFFF")}<div style="flex-grow: 1; {TY["bmd"]}; color: #FFFFFF; font-weight: 600">Chứng từ · R-7Q2K9</div>{ibtn("zoom-in", "Phóng to", "ghost", 44).replace(C["t1"], "#FFFFFF")}</div>'
        foot = f'<div style="padding: 12px 16px {BOT}px; {TY["cap"]}; color: {C["tinv2"]}; text-align: center">Ảnh riêng tư · không lưu vào thư viện máy · chụp màn hình được ghi nhận</div>'
        return phone(head + c + foot, bg=C["inverse"])
    return [("Xem & phóng to", v()), ("Liên kết hết hạn", v(True))]


@frame("D-059", "Privacy / consent settings", "Tài khoản & hỗ trợ")
def d059():
    return [("Mặc định", phone(topbar("Quyền riêng tư & đồng ý", True) + body(
        ovl("Vị trí")
        + switch(True, "Vị trí nền khi trực tuyến", "Bắt buộc để nhận chuyến. Gửi vị trí 5 giây/lần khi trực tuyến, 2 giây/lần khi đang chạy. Tắt khi bạn ngoại tuyến.")
        + ovl("Chứng từ & bằng chứng")
        + switch(True, "Lưu ảnh chứng từ, hoá đơn, ảnh chat", "Lưu riêng tư để xử lý tranh chấp, chỉ người liên quan và đội xử lý xem.")
        + card(row(icon("shield", 18, C["t2"]), txt("<b>Thông tin thiết bị & rủi ro:</b> Onway ghi mã thiết bị đã mã hoá và tín hiệu bất thường (VD: vị trí nhảy bất thường) để chống gian lận. Onway không dùng AI tự động kết luận vi phạm.", "bsm", C["t2"]), gap=10, align="flex-start"), pad=14, bg=C["ink25"])
        + list_row("Tải xuống dữ liệu của tôi", "", "download", pad="14px 0") + list_row("Yêu cầu xoá tài khoản", "Dữ liệu KYC, tài chính giữ theo luật", "trash", pad="14px 0", border=False)
        + txt("Phiên bản đồng ý: v2 · 24/09/2026", "cap", C["t3"]), bg="#FFFFFF", gap=12)))]
