from lib import *
from reg import frame

PICK, PICK_S = "Toà nhà Bitexco", "2 Hải Triều, Bến Nghé, Quận 1"
DROP, DROP_S = "ĐH Kinh tế TP.HCM", "59C Nguyễn Đình Chiểu, Quận 3"
ROUTE = [(0.72, 0.47), (0.72, 0.42), (0.52, 0.42), (0.52, 0.24), (0.3, 0.24), (0.3, 0.17)]
PINS = [("pickup", 0.72, 0.47), ("dropoff", 0.3, 0.17)]
TO_PICK = [(0.9, 0.3), (0.9, 0.42), (0.72, 0.42), (0.72, 0.47)]


def M(**kw):
    return map_svg(PW, PH, **kw)


def back_float(label="Quay lại", ic="arrow-left"):
    return row(circle_btn(ic, label), spacer())


# ================= COMMON / AUTH =================
@frame("C-000", "Splash / launch", "Khởi động & đăng nhập")
def c000():
    splash = phone(
        f'<div style="flex-grow: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 20px">{logo_img(56, True)}'
        f'<div style="{TY["bmd"]}; color: rgba(255,255,255,.86)">Đi xe · Đặt món · 0% hoa hồng</div></div>'
        f'<div style="display: flex; justify-content: center; padding-bottom: 72px">{spinner(28, "#FFFFFF").replace(C["b2"], "rgba(255,255,255,.3)")}</div>', bg=C["red"])
    force = phone(dialog_over(
        f'<div style="flex-grow: 1; display: flex; align-items: center; justify-content: center; background: {C["red"]}">{logo_img(56, True)}</div>',
        "Cần cập nhật ứng dụng",
        "Phiên bản 1.0.2 không còn được hỗ trợ. Cập nhật lên phiên bản 1.1.0 để tiếp tục đặt xe và đặt món an toàn.",
        btn("Cập nhật ngay", "primary", "lg", "download", full=True), ic="download", tone="info"))
    return [("Đang tải", splash), ("Bắt buộc cập nhật", force)]


def login_screen(state="default", app="c"):
    err = "Số điện thoại chưa đúng. Nhập 10 số, ví dụ 0901 234 567." if state == "error" else None
    val = "0901 234" if state == "error" else "0901 234 567"
    top = ""
    if state == "limited":
        top = banner("warning", "Tạm khoá gửi mã OTP", "Số này đã yêu cầu mã 5 lần trong 1 giờ. Thử lại sau 42 phút hoặc liên hệ hỗ trợ.")
    pref = f'<span style="{TY["bmd"]}; font-weight: 600; padding-right: 10px; border-right: 1px solid {C["b2"]}">+84</span>'
    head = "Nhập số điện thoại" if app == "c" else "Đăng nhập tài xế"
    sub = "Onway gửi mã OTP 6 số qua SMS để xác minh số của bạn." if app == "c" else "Dùng số điện thoại bạn sẽ nhận chuyến. Onway gửi mã OTP 6 số qua SMS."
    cta = btn("Nhận mã OTP", "disabled" if state == "limited" else "primary", "lg", full=True, href=None if state == "limited" else ("C-002.dc.html" if app == "c" else "D-002.dc.html"))
    icn = APPICON if app == "c" else APPICON_INK
    return phone(
        f'<div style="height: {TOP}px"></div>' +
        body(f'<img src="{icn}" alt="" width="56" height="56" style="display: block; width: 56px; height: 56px; border-radius: 14px; margin-top: 24px">'
             + col(h(head, "hxl"), txt(sub, "bmd", C["t2"]), gap=8) + top
             + field("Số điện thoại", val, "0901 234 567", error=err, right="", ic=None).replace('<input', pref + '<input', 1)
             + checkbox('Tôi đồng ý với <a href="#" style="font-weight: 600">Điều khoản sử dụng</a> và <a href="#" style="font-weight: 600">Chính sách quyền riêng tư</a> của Onway.', True),
             pad=24, gap=20)
        + bottom(cta + txt("Onway là nền tảng kết nối. Bạn thanh toán trực tiếp cho tài xế.", "cap", C["t3"], extra="text-align: center"), border=False))


@frame("C-001", "Phone login", "Khởi động & đăng nhập")
def c001():
    return [("Mặc định", login_screen()), ("Lỗi định dạng số", login_screen("error")), ("Giới hạn gửi mã", login_screen("limited"))]


def otp_screen(state="default", app="c"):
    digits = "482" if state == "default" else ("482915" if state == "invalid" else "")
    err = state == "invalid"
    msg = ""
    if err:
        msg = f'<div style="display: flex; gap: 6px; align-items: center; {TY["bsm"]}; color: {C["err"]}">{icon("alert-circle", 16, C["err"])}Mã OTP không đúng. Bạn còn 3 lần thử.</div>'
    resend = (f'<div style="{TY["bsm"]}; color: {C["t2"]}">Chưa nhận được mã? <span style="font-family: {MONO}; color: {C["t1"]}; font-weight: 600">Gửi lại sau 00:45</span></div>'
              if state == "cooldown" else f'<div style="{TY["bsm"]}; color: {C["t2"]}">Chưa nhận được mã? <a href="#" style="font-weight: 600">Gửi lại mã</a></div>')
    nxt = "C-003.dc.html" if app == "c" else "D-003.dc.html"
    return phone(topbar("", True, border=False) + body(
        col(h("Nhập mã xác minh", "hxl"), txt(f'Mã 6 số đã gửi tới <span style="font-family: {MONO}; color: {C["t1"]}; font-weight: 600">0901 234 567</span>. Mã có hiệu lực 5 phút.', "bmd", C["t2"]), gap=8)
        + otp_boxes(digits, err, 3 if state == "default" else (0 if state == "cooldown" else None)) + msg + resend
        + f'<a href="#" style="{TY["bsm"]}; font-weight: 600">Đổi số điện thoại</a>', pad=24, gap=20)
        + bottom(btn("Xác nhận", "primary" if state == "default" else ("disabled" if state == "cooldown" else "primary"), "lg", full=True, href=nxt), border=False))


@frame("C-002", "OTP verification", "Khởi động & đăng nhập")
def c002():
    return [("Mặc định", otp_screen()), ("Sai mã OTP", otp_screen("invalid")), ("Chờ gửi lại mã", otp_screen("cooldown"))]


def profile_setup(err=False):
    return phone(topbar("", True, border=False) + body(
        col(h("Bạn tên là gì?", "hxl"), txt("Tài xế sẽ thấy tên này khi đón bạn hoặc giao món.", "bmd", C["t2"]), gap=8)
        + field("Họ và tên", "" if err else "Nguyễn Minh Anh", "Ví dụ: Nguyễn Minh Anh", error="Vui lòng nhập họ tên (tối thiểu 2 ký tự)." if err else None)
        + field("Email (không bắt buộc)", "minhanh@" if err else "", "ban@email.com", error="Email chưa đúng định dạng." if err else None, helper=None if err else "Dùng để nhận biên nhận chuyến đi và phản hồi khiếu nại.")
        , pad=24, gap=20) + bottom(btn("Hoàn tất", "primary", "lg", full=True, href="C-004.dc.html"), border=False))


@frame("C-003", "Basic profile setup", "Khởi động & đăng nhập")
def c003():
    return [("Mặc định", profile_setup()), ("Lỗi nhập liệu", profile_setup(True))]


def permission_screen(ic, title, body_, bullets, cta, alt, state=None, state_banner=""):
    bl = "".join(row(icon_tile(b[0], 36, C["sunken"]), col(txt(b[1], "bmd", C["t1"], extra="font-weight: 600"), txt(b[2], "bsm", C["t2"]), gap=2), gap=12, align="flex-start") for b in bullets)
    return phone(f'<div style="height: {TOP}px"></div>' + body(
        f'<div style="width: 88px; height: 88px; border-radius: 999px; background: {C["sunken"]}; display: flex; align-items: center; justify-content: center; margin-top: 32px">{icon(ic, 40)}</div>'
        + col(h(title, "hxl"), txt(body_, "bmd", C["t2"]), gap=8) + state_banner + col(bl, gap=16), pad=24, gap=24)
        + bottom(cta + alt, border=False))


@frame("C-004", "Location permission", "Khởi động & đăng nhập")
def c004():
    bl = [("map-pin", "Đón đúng chỗ", "Tự điền điểm đón từ vị trí hiện tại."), ("map", "Kiểm tra khu vực phục vụ", "Biết ngay Onway có hoạt động nơi bạn đứng."),
          ("navigation", "Theo dõi chuyến đi", "Tài xế thấy điểm đón; bạn thấy tài xế đang đến.")]
    a = permission_screen("map-pin", "Cho phép Onway dùng vị trí", "Onway chỉ dùng vị trí khi bạn mở ứng dụng hoặc đang có chuyến/đơn.", bl,
                          btn("Cho phép truy cập vị trí", "primary", "lg", full=True, href="C-005.dc.html"), btn("Để sau, tôi sẽ nhập địa chỉ", "ghost", "lg", full=True))
    d = permission_screen("map-pin", "Quyền vị trí đang tắt", "Bạn vẫn đặt xe được bằng cách nhập địa chỉ, nhưng điểm đón sẽ kém chính xác hơn.", bl[:1],
                          btn("Mở Cài đặt", "primary", "lg", "settings", full=True), btn("Nhập địa chỉ thủ công", "ghost", "lg", full=True),
                          state_banner=banner("warning", "Onway không truy cập được vị trí", "Vào Cài đặt › Onway › Vị trí › Khi dùng ứng dụng."))
    l = permission_screen("locate", "Bật vị trí chính xác", "Onway đang dùng vị trí gần đúng. Điểm đón có thể lệch 1–3 km khiến tài xế khó tìm bạn.", bl[:1],
                          btn("Bật vị trí chính xác", "primary", "lg", full=True), btn("Tiếp tục với vị trí gần đúng", "ghost", "lg", full=True),
                          state_banner=banner("info", "Chỉ có vị trí gần đúng", "Bạn nên kéo ghim để chỉnh điểm đón trước khi đặt."))
    return [("Giải thích quyền", a), ("Đã từ chối", d), ("Vị trí gần đúng", l)]


@frame("C-005", "Notification permission", "Khởi động & đăng nhập")
def c005():
    bl = [("navigation", "Trạng thái chuyến và đơn", "Tài xế đã nhận, đang đến, đã tới nơi."), ("banknote", "Xác nhận thanh toán", "Tài xế đã nhận đủ tiền hoặc cần bổ sung."),
          ("message", "Tin nhắn từ tài xế", "Không bỏ lỡ khi tài xế cần hỏi đường.")]
    a = permission_screen("bell", "Bật thông báo", "Thông báo giúp bạn không bỏ lỡ tài xế và các bước thanh toán quan trọng.", bl,
                          btn("Bật thông báo", "primary", "lg", full=True, href="C-006.dc.html"), btn("Để sau", "ghost", "lg", full=True))
    d = permission_screen("bell", "Thông báo đang tắt", "Bạn sẽ phải mở ứng dụng để xem tài xế đã nhận chuyến hay chưa.", [],
                          btn("Mở Cài đặt", "primary", "lg", "settings", full=True), btn("Tiếp tục không có thông báo", "ghost", "lg", full=True),
                          state_banner=banner("warning", "Bạn có thể bỏ lỡ tài xế", "Tài xế chỉ chờ tại điểm đón trong thời gian giới hạn."))
    return [("Giải thích quyền", a), ("Đã từ chối", d)]


# ================= HOME =================
def home(state="default"):
    greet = row(col(txt("Chào buổi sáng", "cap", C["t3"]), txt("Minh Anh", "hmd", C["t1"]), gap=2),
                spacer(), f'<span style="display: inline-flex; align-items: center; gap: 6px; height: 32px; padding: 0 12px; border-radius: 999px; border: 1px solid {C["b2"]}; {TY["lbl"]}; background: #FFFFFF">{icon("map-pin", 14)}Bến Nghé, Q.1</span>', gap=8)
    if state == "loading":
        return phone(f'<div style="height: {TOP}px; background: #FFFFFF"></div>' + body(
            row(col(skel(90, 12), skel(140, 22), gap=8), spacer(), skel(110, 32, 999)) + skel("100%", 52, 8)
            + row(skel("100%", 128, 12, "flex: 1"), skel("100%", 128, 12, "flex: 1"), gap=12) + skel(120, 18) + skel("100%", 56, 8) + skel("100%", 56, 8) + skel("100%", 56, 8), bg="#FFFFFF")
            + tabbar(0))
    off = state == "offline"
    no_reg = state == "noregion"
    b = ""
    if off:
        b = banner("neutral", "Không có kết nối mạng", "Kiểm tra Wi-Fi hoặc dữ liệu di động. Onway sẽ tự thử lại.", "wifi-off")
    if no_reg:
        b = banner("warning", "Onway chưa phục vụ tại vị trí này", "Hiện Onway hoạt động tại một số khu vực ở TP. Hồ Chí Minh. Hãy đổi vị trí để đặt.")
    dis = off or no_reg
    def svc(ic, title, sub, href, tone):
        op = "opacity: .45; " if dis else ""
        return (f'<a href="{href}" style="{op}flex: 1 1 0; display: flex; flex-direction: column; gap: 14px; padding: 16px; border-radius: 12px; border: 1px solid {C["b2"]}; background: #FFFFFF; text-decoration: none; color: {C["t1"]}">'
                f'<div style="width: 48px; height: 48px; border-radius: 12px; background: {tone}; display: flex; align-items: center; justify-content: center">{icon(ic, 26)}</div>'
                f'<div><div style="{TY["hsm"]}">{title}</div><div style="{TY["cap"]}; font-size: 13px; color: {C["t3"]}; margin-top: 2px">{sub}</div></div></a>')
    services = row(svc("bike", "Đi xe", "Xe máy · Ô tô", "C-012.dc.html", C["sunken"]), svc("utensils", "Đặt món", "Quán quen gần bạn", "C-033.dc.html", C["sunken"]), gap=12)
    search = (f'<a href="C-014.dc.html" style="display: flex; align-items: center; gap: 12px; height: 52px; padding: 0 16px; border-radius: 12px; background: {C["sunken"]}; text-decoration: none; color: {C["t2"]}; {TY["bmd"]}{"; opacity: .45" if dis else ""}">'
              f'{icon("search", 20, C["t1"])}<span style="flex-grow: 1">Bạn muốn đi đâu?</span><span style="display: inline-flex; align-items: center; gap: 4px; {TY["lbl"]}; color: {C["t1"]}">{icon("clock", 14)}Bây giờ</span></a>')
    recents = (list_row("Công ty", "Toà nhà Bitexco, 2 Hải Triều, Q.1", "briefcase", chevron=False)
               + list_row("Nhà", "142 Lê Văn Sỹ, Phường 10, Phú Nhuận", "home", chevron=False)
               + list_row("ĐH Kinh tế TP.HCM", "59C Nguyễn Đình Chiểu, Q.3", "clock", chevron=False, border=False))
    promo = card(row(icon_tile("banknote", 40, C["brand_bg"], C["brand"]), col(txt("Onway không thu phí từ khách", "bmd", C["t1"], extra="font-weight: 600"),
                                                                                 txt("Bạn trả đúng giá hiển thị, chuyển khoản trực tiếp cho tài xế.", "bsm", C["t2"]), gap=2), gap=12, align="flex-start"), pad=14)
    return phone(f'<div style="height: {TOP}px; background: #FFFFFF"></div>' + body(
        greet + b + search + services + section_title("Gần đây") + f'<div style="margin: -12px -16px 0; background: #FFFFFF">{recents}</div>' + ("" if dis else promo), bg="#FFFFFF", gap=16)
        + tabbar(0, badge_idx=2))


@frame("C-006", "Home / service selector", "Trang chủ & tài khoản")
def c006():
    return [("Mặc định", home()), ("Đang tải", home("loading")), ("Ngoài khu vực", home("noregion")), ("Mất mạng", home("offline"))]


@frame("C-007", "Home search/service empty", "Trang chủ & tài khoản")
def c007():
    a = phone(topbar("Onway", False) + body(empty_state("map", "Onway chưa có mặt ở đây",
                                                          "Onway đang phục vụ tại TP. Hồ Chí Minh. Chúng tôi sẽ thông báo khi mở rộng tới khu vực của bạn.",
                                                          col(btn("Đổi vị trí", "secondary", "lg", "map-pin"), btn("Xem khu vực đang phục vụ", "ghost", "md"), gap=8, extra="align-items: center")),
                                              extra="justify-content: center", bg="#FFFFFF") + tabbar(0))
    b = phone(topbar("Đặt món", True) + body(
        banner("warning", "Đặt món tạm dừng tại khu vực này", "Đội vận hành tạm dừng dịch vụ Food ở Quận 1 từ 22:00. Dự kiến mở lại 06:00 sáng mai.")
        + empty_state("utensils", "Chưa có quán phục vụ", "Bạn vẫn có thể đặt xe bình thường trong lúc chờ.", btn("Chuyển sang Đi xe", "secondary", "lg", "bike", href="C-012.dc.html")),
        bg="#FFFFFF") + tabbar(0))
    return [("Không có khu vực hoạt động", a), ("Dịch vụ tạm dừng", b)]


def notif_item(ic, title, body_, time, unread=False):
    dot = f'<span style="width: 8px; height: 8px; border-radius: 999px; background: {C["red"]}; flex-shrink: 0; margin-top: 8px"></span>' if unread else '<span style="width: 8px; flex-shrink: 0"></span>'
    return (f'<div style="display: flex; gap: 12px; padding: 14px 16px; border-bottom: 1px solid {C["b1"]}; background: {C["ink25"] if unread else "#FFFFFF"}">{icon_tile(ic, 40)}'
            f'<div style="flex-grow: 1; min-width: 0"><div style="{TY["bmd"]}; font-weight: {700 if unread else 500}">{title}</div><div style="{TY["bsm"]}; color: {C["t2"]}">{body_}</div>'
            f'<div style="{TY["cap"]}; color: {C["t3"]}; margin-top: 4px">{time}</div></div>{dot}</div>')


@frame("C-008", "Notification center", "Trang chủ & tài khoản")
def c008():
    items = (notif_item("check-circle", "Tài xế đã nhận đủ tiền", "Hùng xác nhận đã nhận 48.000đ cho chuyến R-7Q2K9.", "2 phút trước", True)
             + notif_item("bike", "Tài xế đã nhận chuyến", "Trần Văn Hùng · Honda Vision 59-X2 123.45 đang đến.", "5 phút trước", True)
             + notif_item("utensils", "Đơn món đã giao", "Đơn F-3M8TP từ Cơm Tấm Sà Bì đã hoàn thành.", "Hôm qua, 12:41")
             + notif_item("scale", "Cập nhật khiếu nại CS-240924-0137", "Onway đã ghi nhận phản hồi của tài xế.", "22/09, 18:02")
             + notif_item("megaphone", "Onway mở rộng khu vực Quận 3", "Đi xe và Đặt món đã hoạt động tại Quận 3.", "20/09, 09:00"))
    head = topbar("Thông báo", False, right=btn("Đọc hết", "ghost", "sm"))
    lst = phone(head + f'<div style="flex-grow: 1; background: #FFFFFF; overflow: hidden">{items}</div>' + tabbar(2))
    emp = phone(topbar("Thông báo", False) + body(empty_state("bell", "Chưa có thông báo", "Trạng thái chuyến đi, đơn món và thanh toán sẽ xuất hiện ở đây."), extra="justify-content: center", bg="#FFFFFF") + tabbar(2))
    return [("Có chưa đọc", lst), ("Trống", emp)]


@frame("C-009", "Account / settings", "Trang chủ & tài khoản")
def c009():
    rows = (list_row("Hồ sơ & số điện thoại", "Tên, email, hiển thị số điện thoại", "user", href="C-010.dc.html")
            + list_row("Địa điểm đã lưu", "Nhà, Công ty và 3 địa điểm khác", "bookmark", href="C-066.dc.html")
            + list_row("Hoạt động", "Lịch sử chuyến đi và đơn món", "list", href="C-059.dc.html")
            + list_row("Khiếu nại của tôi", "1 khiếu nại đang xử lý", "scale", href="C-062.dc.html", right=pill("pendingReview", "Đang xử lý", "sm"))
            + list_row("Quyền riêng tư & dữ liệu", "Đồng ý, xuất hoặc xoá dữ liệu", "shield", href="C-011.dc.html")
            + list_row("Trợ giúp & liên hệ", "", "help")
            + list_row("Điều khoản & chính sách", "", "file", border=False))
    prof = row(avatar("MA", 56), col(txt("Nguyễn Minh Anh", "hsm"), num("0901 234 567", 14, C["t2"]), gap=4), spacer(), gap=14)
    return [("Mặc định", phone(f'<div style="height: {TOP}px; background: #FFFFFF"></div>' + body(
        prof + f'<div style="margin: 0 -16px; border-top: 1px solid {C["b1"]}">{rows}</div>'
        + btn("Đăng xuất", "outline", "lg", "log-out", full=True) + txt("Onway 1.1.0 (240924)", "cap", C["t3"], extra="text-align: center"), bg="#FFFFFF", gap=16) + tabbar(3)))]


def profile_edit(err=False):
    return phone(topbar("Hồ sơ", True) + body(
        row(avatar("MA", 64), btn("Đổi ảnh", "outline", "sm", "camera"), gap=16)
        + field("Họ và tên", "Nguyễn Minh Anh")
        + field("Số điện thoại", "0901 234 567", disabled=True, helper="Đổi số cần xác minh lại bằng OTP.", mono=True, right=f'<a href="#" style="{TY["lbl"]}">Đổi</a>')
        + field("Email", "minhanh@gmail" if err else "minhanh@gmail.com", error="Email chưa đúng định dạng, ví dụ ban@email.com." if err else None)
        + divider()
        + switch(True, "Cho tài xế thấy số điện thoại của tôi", "Chỉ trong chuyến/đơn đang diễn ra. Onway chưa có tổng đài ẩn số — tài xế gọi trực tiếp số thật của bạn.")
        , bg="#FFFFFF", gap=18) + bottom(btn("Lưu thay đổi", "primary", "lg", full=True)))


@frame("C-010", "Profile and phone visibility settings", "Trang chủ & tài khoản")
def c010():
    return [("Mặc định", profile_edit()), ("Lỗi nhập liệu", profile_edit(True))]


@frame("C-011", "Privacy / consent settings", "Trang chủ & tài khoản")
def c011():
    return [("Mặc định", phone(topbar("Quyền riêng tư & dữ liệu", True) + body(
        ovl("Đồng ý đã cấp")
        + switch(True, "Vị trí khi dùng ứng dụng", "Tìm điểm đón, kiểm tra khu vực, chia sẻ với tài xế trong chuyến.")
        + switch(True, "Ảnh chứng từ & ảnh trong chat", "Lưu riêng tư để xử lý tranh chấp. Chat lưu 7 ngày.")
        + switch(True, "Hiển thị số điện thoại cho tài xế", "Chỉ trong chuyến/đơn đang diễn ra.")
        + card(row(icon("shield", 18, C["t2"]), txt("Thông tin thiết bị (mã thiết bị đã mã hoá) được dùng để chống gian lận và bảo vệ tài khoản. Đây là điều kiện sử dụng dịch vụ. <a href=\"#\" style=\"font-weight: 600\">Tìm hiểu thêm</a>", "bsm", C["t2"]), gap=10, align="flex-start"), pad=14, bg=C["ink25"])
        + ovl("Dữ liệu của bạn")
        + f'<div style="margin: 0 -16px; border-top: 1px solid {C["b1"]}">'
        + list_row("Tải xuống dữ liệu của tôi", "Nhận bản sao qua email trong 30 ngày", "download", href="C-067.dc.html")
        + list_row("Yêu cầu xoá tài khoản", "Một số dữ liệu được giữ theo luật và để xử lý tranh chấp", "trash", href="C-067.dc.html", border=False) + "</div>"
        + txt("Phiên bản đồng ý: v2 · cập nhật 24/09/2026", "cap", C["t3"]), bg="#FFFFFF", gap=14)))]


# ================= RIDE =================
def ride_request(state="default"):
    top = back_float()
    if state == "noperm":
        m = M()
        pick_field = field("Điểm đón", "", "Nhập điểm đón", ic="circle-dot")
        extra = banner("warning", "Chưa bật vị trí", "Nhập điểm đón thủ công hoặc bật vị trí để tự điền.", action=btn("Bật vị trí", "outline", "sm", "locate"))
    elif state == "noregion":
        m = M(regions=[([(0.05, 0.05), (0.62, 0.02), (0.66, 0.3), (0.2, 0.36)], "active", "Vùng Quận 1")], pins=[("me", 0.82, 0.44)])
        pick_field = field("Điểm đón", "Vị trí hiện tại · 88 Xô Viết Nghệ Tĩnh", ic="circle-dot", error="Điểm đón nằm ngoài khu vực phục vụ.")
        extra = banner("danger", "Chọn điểm đón trong vùng phục vụ", "Onway chỉ nhận chuyến bắt đầu trong vùng có viền nét đứt trên bản đồ. Điểm đến có thể ở ngoài vùng.")
    else:
        m = M(pins=[("me", 0.72, 0.4)])
        pick_field = field("Điểm đón", "Vị trí hiện tại · Toà nhà Bitexco", ic="circle-dot")
        extra = ""
    sheet = (f'<div style="padding: 4px 16px {BOT}px; display: flex; flex-direction: column; gap: 12px">{h("Đi đâu hôm nay?", "hmd", "h2")}{pick_field}'
             f'<a href="C-014.dc.html" style="text-decoration: none">{field("Điểm đến", "", "Bạn muốn đến đâu?", ic="map-pin")}</a>{extra}'
             + chip_row([tag("Nhà", ic="home"), tag("Công ty", ic="briefcase"), tag("ĐH Kinh tế", ic="clock")])
             + (list_row("ĐH Kinh tế TP.HCM", "59C Nguyễn Đình Chiểu, Q.3 · 3,2 km", "clock", chevron=False, pad="10px 0")
                + list_row("Chợ Bến Thành", "Lê Lợi, Bến Thành, Q.1 · 1,1 km", "clock", chevron=False, pad="10px 0", border=False) if state == "default" else "") + "</div>")
    return phone(map_screen(m, sheet, top, float_right=circle_btn("locate", "Về vị trí của tôi")))


@frame("C-012", "Ride request map", "Đi xe · Đặt chuyến")
def c012():
    return [("Mặc định", ride_request()), ("Chưa cấp quyền vị trí", ride_request("noperm")), ("Ngoài khu vực", ride_request("noregion"))]


def addr_search(mode="pickup", state="search"):
    focus_pick = mode == "pickup"
    q = "bitexco" if focus_pick else "kinh te"
    f1 = f'<div style="display: flex; align-items: center; gap: 10px; height: 44px; padding: 0 12px; border-radius: 8px; border: {"1.5px solid " + C["inverse"] if focus_pick else "1px solid " + C["b2"]}; background: #FFFFFF">' \
         f'<span style="width: 10px; height: 10px; border-radius: 999px; border: 3px solid {C["ink800"]}"></span><input type="text" aria-label="Điểm đón" value="{q if focus_pick else "Toà nhà Bitexco"}" style="flex-grow: 1; border: none; outline: none; font-family: {FONT}; font-size: 15px"></div>'
    f2 = f'<div style="display: flex; align-items: center; gap: 10px; height: 44px; padding: 0 12px; border-radius: 8px; border: {"1.5px solid " + C["inverse"] if not focus_pick else "1px solid " + C["b2"]}; background: #FFFFFF">' \
         f'<span style="width: 10px; height: 10px; border-radius: 2px; background: {C["red"]}"></span><input type="text" aria-label="Điểm đến" value="{q if not focus_pick else ""}" placeholder="Bạn muốn đến đâu?" style="flex-grow: 1; border: none; outline: none; font-family: {FONT}; font-size: 15px"></div>'
    head = f'<div style="padding: {TOP}px 16px 12px; background: #FFFFFF; border-bottom: 1px solid {C["b1"]}; display: flex; gap: 8px; align-items: flex-start">{ibtn("arrow-left", "Quay lại", "ghost", 44)}<div style="flex-grow: 1; display: flex; flex-direction: column; gap: 8px">{f1}{f2}</div></div>'
    pin_row = list_row("Chọn trên bản đồ", "Kéo ghim đến đúng vị trí", "map-pin", href="C-015.dc.html")
    if state == "loading":
        content = "".join(row(skel(40, 40, 10), col(skel(180, 14), skel(240, 12), gap=6, extra="flex-grow: 1"), gap=12, extra="padding: 12px 16px") for _ in range(5))
    elif state == "empty":
        content = empty_state("search", f"Không tìm thấy “{q}”", "Thử tên đường, toà nhà hoặc chọn điểm trực tiếp trên bản đồ.", btn("Chọn trên bản đồ", "outline", "md", "map-pin"))
    elif state == "error":
        content = empty_state("alert-circle", "Không tải được kết quả", "Dịch vụ bản đồ đang chậm. Kiểm tra kết nối và thử lại.", btn("Thử lại", "outline", "md", "refresh"))
    else:
        if focus_pick:
            res = [("Toà nhà Bitexco Financial Tower", "2 Hải Triều, Bến Nghé, Q.1 · 120 m", ""), ("Bitexco — Cổng Hồ Tùng Mậu", "Hồ Tùng Mậu, Bến Nghé, Q.1 · 180 m", ""),
                   ("Bãi xe Bitexco", "36 Hồ Tùng Mậu, Q.1 · 210 m", "")]
        else:
            res = [("ĐH Kinh tế TP.HCM — Cơ sở A", "59C Nguyễn Đình Chiểu, Q.3 · 3,2 km", ""), ("ĐH Kinh tế TP.HCM — Cơ sở B", "279 Nguyễn Tri Phương, Q.10 · 5,8 km", ""),
                   ("ĐH Kinh tế — Cơ sở N", "Khu chức năng số 15, Bình Chánh · 17 km", "outside" if state == "outside" else "")]
        content = ""
        for t, s, flag in res:
            r = pill("paused", "Ngoài vùng", "sm") if flag else ""
            content += list_row(t, s, "map-pin", chevron=False, right=r, href="C-015.dc.html")
        if state == "outside":
            content += f'<div style="padding: 12px 16px">{banner("warning", "Điểm đến ngoài khu vực phục vụ", "Bạn vẫn đặt được vì điểm đón nằm trong vùng. Onway sẽ nhắc lại trước khi xác nhận.")}</div>'
    return phone(head + f'<div style="flex-grow: 1; background: #FFFFFF; overflow: hidden">{pin_row if state not in ("loading",) else ""}{content}</div>')


@frame("C-013", "Pickup address search", "Đi xe · Đặt chuyến")
def c013():
    return [("Kết quả tìm kiếm", addr_search("pickup")), ("Đang tìm", addr_search("pickup", "loading")), ("Không có kết quả", addr_search("pickup", "empty")), ("Lỗi", addr_search("pickup", "error"))]


@frame("C-014", "Dropoff address search", "Đi xe · Đặt chuyến")
def c014():
    return [("Kết quả tìm kiếm", addr_search("drop")), ("Đang tìm", addr_search("drop", "loading")), ("Không có kết quả", addr_search("drop", "empty")), ("Điểm đến ngoài vùng", addr_search("drop", "outside"))]


def pin_adjust(state="default"):
    top = back_float() + float_card(txt("Kéo bản đồ để đặt ghim đúng chỗ bạn đứng", "bsm", C["t1"], extra="text-align: center"), "align-self: center; padding: 8px 14px; border-radius: 999px")
    b = ""
    addr = col(txt("Điểm đón", "cap", C["t3"]), txt("Cổng Hải Triều — Toà nhà Bitexco", "hsm"), txt("2 Hải Triều, Bến Nghé, Quận 1", "bsm", C["t2"]), gap=2)
    if state == "gps":
        b = banner("warning", "Tín hiệu GPS yếu", "Vị trí có thể lệch khoảng 80 m. Hãy kiểm tra ghim trước khi xác nhận.")
    if state == "geo":
        addr = col(txt("Điểm đón", "cap", C["t3"]), txt("Không xác định được địa chỉ", "hsm"), num("10.7717, 106.7043", 13, C["t2"]), gap=2)
        b = banner("danger", "Không lấy được tên đường tại đây", "Bạn vẫn có thể dùng toạ độ này. Thêm ghi chú để tài xế dễ tìm.", action=btn("Thử lại", "outline", "sm", "refresh"))
    sheet = f'<div style="padding: 4px 16px {BOT}px; display: flex; flex-direction: column; gap: 14px">{addr}{b}{field("", "", "Ghi chú cho tài xế (VD: cổng sau, áo xanh)", ic="pencil")}{btn("Xác nhận điểm đón", "primary", "lg", full=True, href="C-016.dc.html")}</div>'
    return phone(map_screen(M(pins=[("center", 0.5, 0.36)]), sheet, top, float_right=circle_btn("locate", "Về vị trí của tôi")))


@frame("C-015", "Map pin adjust pickup/dropoff", "Đi xe · Đặt chuyến")
def c015():
    return [("Mặc định", pin_adjust()), ("GPS yếu", pin_adjust("gps")), ("Không lấy được địa chỉ", pin_adjust("geo"))]


def vehicle_opt(ic, name, sub, price, eta, sel=False, dis=False):
    bd = f"1.5px solid {C['inverse']}" if sel else f"1px solid {C['b2']}"
    op = "opacity: .5; " if dis else ""
    right = num(price, 17, weight=700) if not dis else txt("Không khả dụng", "cap", C["t3"])
    return (f'<button type="button" aria-pressed="{"true" if sel else "false"}" style="{op}display: flex; align-items: center; gap: 14px; width: 100%; padding: 14px; border-radius: 12px; border: {bd}; background: #FFFFFF; font-family: {FONT}; text-align: left; color: {C["t1"]}">'
            f'{icon_tile(ic, 48, C["sunken"])}<div style="flex-grow: 1"><div style="{TY["bmd"]}; font-weight: 700">{name}</div><div style="{TY["cap"]}; font-size: 13px; color: {C["t3"]}">{sub}</div></div>'
            f'<div style="text-align: right">{right}<div style="{TY["cap"]}; color: {C["t3"]}">{eta}</div></div></button>')


def ride_map():
    return M(route=ROUTE, pins=PINS)


def vehicle_sheet(sel="bike"):
    un = sel == "unavail"
    opts = (vehicle_opt("bike", "Xe máy", "1 khách · mũ bảo hiểm có sẵn", "48.000đ", "Đón sau 3 phút", sel in ("bike", "unavail"))
            + vehicle_opt("car", "Ô tô 4 chỗ", "Tối đa 4 khách", "96.000đ" if not un else "", "Đón sau 6 phút" if not un else "Hết xe gần bạn", sel == "car", un))
    b = banner("info", "Ô tô tạm hết tại khu vực", "Thử lại sau vài phút hoặc chọn xe máy.") if un else ""
    sheet = (f'<div style="padding: 4px 16px {BOT}px; display: flex; flex-direction: column; gap: 12px">{row(h("Chọn loại xe", "hmd", "h2"), spacer(), txt("3,2 km · 14 phút", "bsm", C["t2"]))}'
             f'{opts}{b}{btn("Tiếp tục · " + ("96.000đ" if sel == "car" else "48.000đ"), "primary", "lg", full=True, href="C-017.dc.html")}</div>')
    return phone(map_screen(ride_map(), sheet, back_float()))


@frame("C-016", "Vehicle type selection", "Đi xe · Đặt chuyến")
def c016():
    return [("Xe máy", vehicle_sheet("bike")), ("Ô tô", vehicle_sheet("car")), ("Loại xe không khả dụng", vehicle_sheet("unavail"))]


def price_review(state="default"):
    if state == "loading":
        price = row(txt("Giá chuyến", "bmd", C["t2"]), spacer(), spinner(18), txt("Đang tính lại tuyến…", "bsm", C["t2"]))
        cta = btn("Đặt xe", "disabled", "lg", full=True)
        note = ""
    elif state == "error":
        price = banner("danger", "Chưa tính được giá", "Không lấy được tuyến đường cho điểm đến này. Thử lại hoặc chọn điểm đến gần đó.", action=btn("Thử lại", "outline", "sm", "refresh"))
        cta = btn("Đặt xe", "disabled", "lg", full=True)
        note = ""
    else:
        price = (row(col(txt("Giá chuyến · Xe máy", "bsm", C["t2"]), num("48.000đ", 32, weight=700), gap=2), spacer(), pill("confirmed", "Giá cố định")))
        cta = btn("Đặt xe · 48.000đ", "primary", "lg", full=True, href="C-019.dc.html")
        note = card(row(icon("banknote", 18, C["t2"]), txt("Sau khi có tài xế, bạn <b>chuyển khoản trực tiếp</b> cho tài xế trước khi họ đến đón. Onway không thu thêm phí.", "bsm", C["t2"]), gap=10, align="flex-start"), pad=12, bg=C["ink25"])
    sheet = (f'<div style="padding: 4px 16px {BOT}px; display: flex; flex-direction: column; gap: 14px">{h("Xác nhận chuyến", "hmd", "h2")}{addr_block(PICK, DROP, PICK_S, DROP_S)}{divider()}'
             f'{price}{kv("Quãng đường · thời gian", "3,2 km · 14 phút")}{kv("Thanh toán", "Chuyển khoản / VietQR cho tài xế")}{note}{cta}</div>')
    return phone(map_screen(ride_map(), sheet, back_float()))


@frame("C-017", "Ride price review", "Đi xe · Đặt chuyến")
def c017():
    return [("Mặc định", price_review()), ("Đang tính lại tuyến", price_review("loading")), ("Không tính được giá", price_review("error"))]


@frame("C-018", "Destination outside polygon warning", "Đi xe · Đặt chuyến")
def c018():
    base = phone(map_screen(M(route=[(0.72, 0.47), (0.72, 0.42), (0.52, 0.42), (0.52, 0.08), (0.52, 0.0)], pins=[("pickup", 0.72, 0.47)],
                              regions=[([(0.3, 0.2), (0.95, 0.18), (0.98, 0.58), (0.36, 0.6)], "active")]), f'<div style="height: 300px"></div>', back_float()))
    body_ = ("Điểm đón nằm trong vùng phục vụ nên chuyến vẫn được đặt. Điểm đến <b>ĐH Kinh tế — Cơ sở N (Bình Chánh)</b> nằm ngoài vùng hoạt động của Onway."
             + "<br><br>Tài xế sẽ thấy cảnh báo này trước khi nhận chuyến. Hỗ trợ tại điểm đến có thể hạn chế.")
    return [("Cảnh báo điểm đến ngoài vùng", phone(dialog_over(base.replace('<div style="position: relative; width: 390px', '<div style="position: relative; width: 390px', 1), "Điểm đến ngoài khu vực phục vụ", body_,
                                                                btn("Tiếp tục đặt xe", "primary", "lg", full=True, href="C-017.dc.html") + btn("Đổi điểm đến", "outline", "lg", full=True), ic="map-pin", tone="warning")))]


def matching(state="matching"):
    rings = "".join(f'<circle cx="{0.72*PW:.0f}" cy="{0.4*PH:.0f}" r="{r}" fill="none" stroke="rgba(58,99,204,{a})" stroke-width="2"/>' for r, a in [(60, .35), (110, .22), (160, .12)])
    m = M(pins=[("pickup", 0.72, 0.4), ("driver-idle", 0.52, 0.3), ("driver-idle", 0.9, 0.24), ("driver-idle", 0.3, 0.44)], extra_svg=rings)
    if state == "rejected":
        status = pill("searching", "Đang tìm tài xế khác")
        head = "Đang mở rộng tìm kiếm"
        sub = banner("info", "Tài xế gần nhất đã từ chối", "Onway đang gửi yêu cầu tới nhóm tài xế tiếp theo (lượt 2/3). Giá của bạn không đổi.")
    elif state == "timeout":
        status = pill("searching")
        head = "Sắp hết thời gian tìm"
        sub = banner("warning", "Còn 00:12", "Nếu chưa có tài xế, bạn có thể thử lại hoặc đổi điểm đón.")
    else:
        status = pill("matching")
        head = "Đang tìm tài xế gần bạn"
        sub = row(icon("timer", 16, C["t2"]), txt('Thời gian tìm còn <span style="font-family: ' + MONO + '; color: ' + C["t1"] + '; font-weight: 600">01:24</span>', "bsm", C["t2"]), gap=6)
    prog = progress(85 if state == "timeout" else (48 if state == "rejected" else 30), C["info"])
    sheet = (f'<div style="padding: 4px 16px {BOT}px; display: flex; flex-direction: column; gap: 14px" aria-live="polite">{row(status, spacer(), num("48.000đ", 17, weight=700))}'
             f'{h(head, "hmd", "h2")}{prog}{sub}{divider()}{addr_block(PICK, DROP)}{btn("Huỷ yêu cầu", "outline", "lg", full=True, href="C-022.dc.html")}</div>')
    return phone(map_screen(m, sheet))


@frame("C-019", "Ride matching", "Đi xe · Ghép tài xế")
def c019():
    return [("Đang ghép", matching()), ("Sắp hết giờ", matching("timeout"))]


@frame("C-020", "Driver rejected / searching next", "Đi xe · Ghép tài xế")
def c020():
    return [("Tìm lượt tiếp theo", matching("rejected"))]


@frame("C-021", "No driver found", "Đi xe · Ghép tài xế")
def c021():
    return [("Không có tài xế", phone(topbar("", False, right=ibtn("x", "Đóng", "ghost", 44), border=False) + body(
        empty_state("bike", "Chưa tìm được tài xế", "Các tài xế gần bạn đang bận hoặc đã từ chối. Yêu cầu chưa được tạo nên bạn không mất phí.")
        + card(addr_block(PICK, DROP) + divider() + kv("Xe máy", "48.000đ", True), pad=16), extra="justify-content: center", bg="#FFFFFF")
        + bottom(btn("Thử tìm lại", "primary", "lg", "refresh", full=True, href="C-019.dc.html") + btn("Đổi điểm đón / điểm đến", "outline", "lg", full=True, href="C-012.dc.html") + btn("Huỷ", "ghost", "lg", full=True), border=False)))]


@frame("C-022", "Ride cancel before match", "Đi xe · Ghép tài xế")
def c022():
    base = matching()
    reasons = "".join(radio(r, i == 0) for i, r in enumerate(["Tôi đổi kế hoạch", "Chờ lâu quá", "Đặt nhầm địa chỉ", "Lý do khác"]))
    return [("Xác nhận huỷ", phone(dialog_over(base, "Huỷ tìm tài xế?", txt("Chưa có tài xế nhận nên bạn không mất phí. Lý do (không bắt buộc):", "bmd", C["t2"]) + col(reasons, gap=0),
                                                 btn("Huỷ yêu cầu", "danger", "lg", full=True) + btn("Tiếp tục tìm", "secondary", "lg", full=True), ic="x-circle", tone="danger")))]


DRIVER = person_row("Trần Văn Hùng", "Honda Vision · Trắng", "TH", rating="4,9", plate="59-X2 123.45")


def matched():
    m = M(route=TO_PICK, pins=[("pickup", 0.72, 0.47)], driver=(0.9, 0.3))
    step = card(row(f'<span style="{TY["ovl"]}; color: {C["brand"]}">BƯỚC TIẾP THEO</span>', spacer(), num("48.000đ", 15, weight=700))
                + txt("Chuyển khoản cho tài xế trước khi tài xế đến đón", "bmd", C["t1"], extra="font-weight: 600")
                + txt("Tài xế chỉ bắt đầu chuyến sau khi xác nhận đã nhận đủ tiền.", "bsm", C["t2"]), pad=14, bg=C["brand_bg"], extra=f"border-color: {C['red']}33")
    sheet = (job_header("accepted", "Hùng đang đến · 4 phút", "Cách bạn 1,2 km") + f'<div style="padding: 0 16px {BOT}px; display: flex; flex-direction: column; gap: 14px">{DRIVER}{step}'
             f'{btn("Xem thông tin chuyển khoản", "primary", "lg", "qr", full=True, href="C-024.dc.html")}{row(btn("Huỷ chuyến", "ghost", "md"), spacer(), num("R-7Q2K9", 13, C["t3"]))}</div>')
    return phone(map_screen(m, sheet, back_float("Thu nhỏ", "chevron-down")))


@frame("C-023", "Matched ride / driver assigned", "Đi xe · Thanh toán trực tiếp")
def c023():
    return [("Đã có tài xế", matched())]


def pay_info(amount="48.000đ", ref="R-7Q2K9", note="ONW R7Q2K9", nxt="C-025.dc.html", title="Chuyển khoản cho tài xế"):
    cp = lambda: ibtn("copy", "Sao chép", "ghost", 36)
    info = (f'<div style="display: flex; gap: 16px; align-items: center"><div style="padding: 8px; border: 1px solid {C["b2"]}; border-radius: 12px; background: #FFFFFF">{qr_svg(128)}</div>'
            f'<div style="flex-grow: 1; display: flex; flex-direction: column; gap: 4px">{txt("Số tiền cần chuyển", "cap", C["t3"])}{num(amount, 28, weight=700)}'
            f'{txt("Quét mã bằng ứng dụng ngân hàng bất kỳ", "cap", C["t3"])}</div></div>')
    rows = (row(col(txt("Ngân hàng", "cap", C["t3"]), txt("Vietcombank", "bmd", extra="font-weight: 600"), gap=2), spacer(), gap=8)
            + row(col(txt("Số tài khoản", "cap", C["t3"]), num("1023 4567 89", 16, weight=600), gap=2), spacer(), cp())
            + row(col(txt("Chủ tài khoản", "cap", C["t3"]), txt("TRAN VAN HUNG", "bmd", extra="font-weight: 600"), gap=2), spacer())
            + row(col(txt("Nội dung chuyển khoản", "cap", C["t3"]), num(note, 16, weight=600), gap=2), spacer(), cp()))
    return (f'<div style="padding: 8px 16px {BOT}px; display: flex; flex-direction: column; gap: 14px">{info}{card(rows, pad=14, gap=10)}'
            f'{banner("warning", "Chuyển đúng số tiền và đúng tài khoản", "Tiền đi thẳng tới tài xế — Onway không giữ hộ và không hoàn tiền thay tài xế.")}'
            f'{btn("Tôi đã chuyển khoản", "primary", "lg", full=True, href=nxt)}</div>')


@frame("C-024", "Ride payment instructions", "Đi xe · Thanh toán trực tiếp")
def c024():
    return [("Thông tin chuyển khoản", phone(sheet_over(matched(), pay_info(), title="Chuyển khoản cho tài xế")))]


def proof_sheet(state="empty", amount="48.000đ", base=None):
    up = upload_tile(state)
    cta = {"empty": btn("Gửi chứng từ", "disabled", "lg", full=True), "uploading": btn("Đang gửi…", "disabled", "lg", full=True),
           "failed": btn("Gửi chứng từ", "disabled", "lg", full=True), "done": btn("Xong", "secondary", "lg", full=True, href="C-028.dc.html")}[state]
    extra = ""
    if state == "done":
        extra = banner("info", "Đang chờ tài xế xác nhận", "Tài xế kiểm tra tài khoản và bấm “Đã nhận đủ tiền”. Bạn sẽ nhận thông báo ngay.")
    inner = (f'<div style="padding: 8px 16px {BOT}px; display: flex; flex-direction: column; gap: 14px">'
             f'{txt("Ảnh chụp màn hình giao dịch giúp giải quyết nhanh nếu có tranh chấp. Ảnh chỉ tài xế và đội xử lý khiếu nại xem được.", "bsm", C["t2"])}'
             f'{card(kv("Số tiền đã chuyển", amount, True) + kv("Người nhận", "TRAN VAN HUNG · Vietcombank"), pad=14, gap=8)}{up}{extra}{cta}</div>')
    return phone(sheet_over(base or matched(), inner, title="Gửi ảnh chứng từ"))


@frame("C-025", "Ride proof upload", "Đi xe · Thanh toán trực tiếp")
def c025():
    return [("Chưa có ảnh", proof_sheet("empty")), ("Đang tải lên", proof_sheet("uploading")), ("Tải lên thất bại", proof_sheet("failed")), ("Đã gửi", proof_sheet("done"))]


def proof_rejected(service="ride"):
    amt, short, ref = ("48.000đ", "8.000đ", "R-7Q2K9") if service == "ride" else ("137.000đ", "17.000đ", "F-3M8TP")
    return phone(topbar("Thanh toán", True, sub=ref) + body(
        pill("proofRejected", "Tài xế chưa nhận đủ")
        + h("Tài xế báo chưa nhận đủ tiền", "hlg")
        + txt(f"Tài xế Hùng kiểm tra tài khoản và thấy số tiền nhận được chưa khớp. Thường do chuyển thiếu hoặc nhầm tài khoản.", "bmd", C["t2"])
        + card(kv("Cần chuyển", amt, True) + kv("Tài xế ghi nhận", "40.000đ" if service == "ride" else "120.000đ", True) + divider() + kv("Còn thiếu", short, True), pad=14, gap=8)
        + card(row(photo(56, 56, "", "image", 8), col(txt("Ảnh bạn đã gửi", "bsm", C["t1"], extra="font-weight: 600"), txt("08:14 · chuyen-khoan-0924.jpg", "cap", C["t3"]), gap=2), spacer(), btn("Xem", "ghost", "sm")), pad=12)
        + banner("info", "Bổ sung trước khi mở tranh chấp", "Nếu bạn chắc đã chuyển đủ, gửi lại ảnh rõ hơn hoặc nhắn tài xế. Onway chỉ xem xét khi hai bên chưa thống nhất."), bg="#FFFFFF", gap=14)
        + bottom(btn(f"Chuyển thêm {short}", "primary", "lg", "qr", full=True) + row(btn("Gửi lại ảnh", "outline", "lg", "upload", full="grow"), btn("Nhắn tài xế", "outline", "lg", "message", full="grow"), gap=8)))


@frame("C-026", "Ride proof rejected / supplement needed", "Đi xe · Thanh toán trực tiếp")
def c026():
    return [("Cần bổ sung", proof_rejected())]


def disputed(ref="R-7Q2K9", case="CS-240924-0137", service="chuyến"):
    return phone(topbar("Thanh toán", True, sub=ref) + body(
        pill("disputed") + h("Thanh toán đang được xem xét", "hlg")
        + txt(f"Tài xế báo chưa nhận được tiền và hai bên chưa thống nhất. {service.capitalize()} tạm dừng trong lúc Onway xem xét bằng chứng của cả hai bên.", "bmd", C["t2"])
        + card(timeline([("Bạn gửi ảnh chứng từ", "08:14 · 48.000đ", "done"), ("Tài xế báo chưa nhận được tiền", "08:19", "done"),
                         ("Onway đang xem xét", "Phản hồi trong vòng 24 giờ", "current"), ("Kết luận & bước tiếp theo", "", "todo")], dense=True), pad=16)
        + card(kv("Mã khiếu nại", case, True) + kv("Người xử lý", "Nhóm Hỗ trợ Onway"), pad=14, gap=8)
        + txt("Onway là nền tảng kết nối: bên nào sai bên đó chịu trách nhiệm. Onway không tự bồi thường thay các bên.", "cap", C["t3"]), bg="#FFFFFF", gap=14)
        + bottom(btn("Gửi thêm bằng chứng", "secondary", "lg", "paperclip", full=True, href="C-063.dc.html") + btn("Liên hệ hỗ trợ", "outline", "lg", "help", full=True)))


@frame("C-027", "Ride payment disputed", "Đi xe · Thanh toán trực tiếp")
def c027():
    return [("Đang tranh chấp", disputed())]


def active_ride(state="enroute"):
    if state == "trip":
        m = M(route=ROUTE[1:], pins=[("dropoff", 0.3, 0.17)], driver=(0.72, 0.42))
        head = job_header("inProgress", "Đến nơi lúc 08:42", "Còn 9 phút · 2,6 km", num("R-7Q2K9", 13, C["t3"]))
    elif state in ("arrived", "arrived_warn"):
        m = M(pins=[("pickup", 0.72, 0.47)], driver=(0.74, 0.46))
        head = job_header("arrived", "Tài xế đã đến điểm đón", "Tài xế chờ bạn tới 08:31 (còn 4:12)")
    else:
        m = M(route=TO_PICK[1:], pins=[("pickup", 0.72, 0.47)], driver=(0.9, 0.36))
        head = job_header("arriving", "Hùng đến sau 2 phút", "Cách 450 m · Hải Triều")
    top = back_float("Thu nhỏ", "chevron-down")
    if state == "conn":
        top += banner("neutral", "Mất kết nối", "Vị trí tài xế có thể chưa cập nhật. Đang kết nối lại…", "wifi-off")
    paid = row(pill("proofVerified"), txt("Tài xế đã xác nhận 08:16", "cap", C["t3"]), gap=8)
    if state == "arrived_warn":
        paid = banner("danger", "Bạn chưa hoàn tất thanh toán", "Tài xế sẽ không bắt đầu chuyến khi chưa nhận đủ 48.000đ. Chuyển khoản và gửi chứng từ ngay.", action=btn("Chuyển khoản ngay", "primary", "sm", "qr"))
    plate = ""
    if state.startswith("arrived"):
        plate = card(row(col(txt("Tìm xe có biển số", "cap", C["t3"]), num("59-X2 123.45", 24, weight=700), txt("Honda Vision · Trắng", "bsm", C["t2"]), gap=2), spacer(), icon_tile("bike", 48)), pad=14)
    rep = row(btn("Chia sẻ trạng thái", "ghost", "md", "send"), spacer(), btn("Báo sự cố", "ghost", "md", "flag", href="C-032.dc.html"))
    sheet = head + f'<div style="padding: 0 16px {BOT}px; display: flex; flex-direction: column; gap: 14px">{paid}{plate}{DRIVER}{addr_block(PICK, DROP) if state in ("enroute", "conn", "trip") else ""}{rep}</div>'
    return phone(map_screen(m, sheet, top))


@frame("C-028", "Active ride - driver en route", "Đi xe · Trong chuyến")
def c028():
    return [("Tài xế đang đến", active_ride()), ("Mất kết nối", active_ride("conn"))]


@frame("C-029", "Active ride - driver arrived", "Đi xe · Trong chuyến")
def c029():
    return [("Chờ đón", active_ride("arrived")), ("Chưa thanh toán", active_ride("arrived_warn"))]


@frame("C-030", "Active ride - in trip", "Đi xe · Trong chuyến")
def c030():
    return [("Đang trong chuyến", active_ride("trip"))]


@frame("C-031", "Ride completed summary", "Đi xe · Trong chuyến")
def c031():
    return [("Hoàn thành", phone(topbar("", False, right=ibtn("x", "Đóng", "ghost", 44), border=False) + body(
        f'<div style="display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center; padding-top: 8px">'
        f'<div style="width: 64px; height: 64px; border-radius: 999px; background: {C["ok_bg"]}; color: {C["ok"]}; display: flex; align-items: center; justify-content: center">{icon("check", 32, C["ok"], 2.5)}</div>'
        f'{h("Bạn đã đến nơi", "hlg")}{txt("08:41 · 24/09/2026", "bsm", C["t2"])}</div>'
        + card(addr_block(PICK, DROP, "08:27", "08:41") + divider() + kv("Xe máy · 3,2 km", "48.000đ", True) + kv("Thanh toán", "Chuyển khoản cho tài xế") + kv("Chứng từ", "Tài xế đã xác nhận nhận đủ") + kv("Mã chuyến", "R-7Q2K9", True), pad=16, gap=10)
        + card(row(avatar("TH", 44), col(txt("Chuyến đi với Hùng thế nào?", "bmd", extra="font-weight: 600"), stars(5, 0, 24), gap=6), gap=12), pad=14),
        bg="#FFFFFF", gap=16)
        + bottom(btn("Đánh giá tài xế", "primary", "lg", full=True, href="C-052.dc.html") + btn("Báo cáo vấn đề", "ghost", "lg", "flag", full=True, href="C-053.dc.html"), border=False)))]


@frame("C-032", "Ride issue/report entry", "Đi xe · Trong chuyến")
def c032():
    cats = [("alert-triangle", "Vấn đề an toàn", "Lái xe nguy hiểm, quấy rối, tai nạn"), ("user", "Thái độ tài xế", "Thiếu tôn trọng, đòi thêm tiền"),
            ("banknote", "Thanh toán", "Tài xế báo chưa nhận tiền, chuyển nhầm"), ("map-pin", "Sai lộ trình / điểm đón", "Đi vòng, không đến đúng chỗ"),
            ("package", "Để quên đồ", "Liên hệ tài xế tìm lại đồ"), ("more", "Vấn đề khác", "")]
    rows = "".join(list_row(t, s, i, href="C-053.dc.html") for i, t, s in cats)
    inner = f'<div style="padding: 0 0 {BOT}px">{txt("Chọn loại vấn đề. Bạn có thể thêm ảnh ở bước sau (không bắt buộc).", "bsm", C["t2"], extra="padding: 0 16px 8px")}{rows}' \
            f'<div style="padding: 12px 16px 0">{banner("danger", "Khẩn cấp?", "Gọi 113 (Công an) hoặc 115 (Cấp cứu) trước, rồi báo Onway sau.", "phone")}</div></div>'
    return [("Chọn loại sự cố", phone(sheet_over(active_ride("trip"), inner, title="Báo sự cố chuyến đi")))]


# ================= FOOD =================
OUTLET = "Cơm Tấm Sà Bì — Nguyễn Trãi"
OUT_ADDR = "212 Nguyễn Trãi, Phường Nguyễn Cư Trinh, Quận 1"
HOME_ADDR = "142 Lê Văn Sỹ, Phường 10, Phú Nhuận"
F_ROUTE = [(0.3, 0.44), (0.3, 0.42), (0.52, 0.42), (0.52, 0.24), (0.72, 0.24), (0.72, 0.17)]


def outlet_card(name, sub, dist, fee, hue, closed=False, href="C-035.dc.html"):
    op = "opacity: .55; " if closed else ""
    st = pill("paused", "Đóng cửa", "sm") if closed else ""
    return (f'<a href="{href}" style="{op}display: flex; gap: 12px; padding: 12px 0; border-bottom: 1px solid {C["b1"]}; text-decoration: none; color: {C["t1"]}">{food_img(80, 80, hue, 12, name)}'
            f'<div style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 3px"><div style="display: flex; gap: 8px; align-items: center"><span style="{TY["bmd"]}; font-weight: 700">{name}</span>{st}</div>'
            f'<div style="{TY["bsm"]}; color: {C["t2"]}">{sub}</div><div style="{TY["cap"]}; color: {C["t3"]}; display: flex; gap: 10px">'
            f'<span>{dist}</span><span>·</span><span>Phí giao đề xuất <span style="font-family: {MONO}">{fee}</span></span></div></div></a>')


def food_home(state="default"):
    head = (f'<div style="padding: {TOP}px 16px 12px; background: #FFFFFF; display: flex; flex-direction: column; gap: 12px">'
            + row(ibtn("arrow-left", "Quay lại", "ghost", 44), col(txt("Giao đến", "cap", C["t3"]), row(txt("Nhà · 142 Lê Văn Sỹ", "bmd", extra="font-weight: 700"), icon("chevron-down", 16), gap=4), gap=0), spacer(), ibtn("bag", "Giỏ hàng", "outline", 44, badge=True), gap=6)
            + f'<a href="C-034.dc.html" style="text-decoration: none">{search_bar("Tìm quán hoặc món")}</a></div>')
    if state == "loading":
        b = body(chip_row([skel(80, 36, 999) for _ in range(4)]) + "".join(row(skel(80, 80, 12), col(skel(160, 16), skel(220, 12), skel(140, 12), gap=8, extra="flex-grow: 1"), gap=12) for _ in range(5)), bg="#FFFFFF")
        return phone(head + b)
    if state == "noregion":
        return phone(head + body(empty_state("utensils", "Chưa có quán giao đến địa chỉ này", "Địa chỉ giao nằm ngoài khu vực Onway đang phục vụ món ăn. Đổi địa chỉ giao hoặc dùng dịch vụ Đi xe.",
                                               col(btn("Đổi địa chỉ giao", "secondary", "lg", "map-pin", href="C-038.dc.html"), gap=8)), extra="justify-content: center", bg="#FFFFFF"))
    chips = chip_row([tag("Tất cả", True), tag("Cơm"), tag("Phở · Bún"), tag("Bánh mì"), tag("Trà sữa"), tag("Cà phê")])
    lst = (outlet_card("Cơm Tấm Sà Bì", "Cơm tấm · Nguyễn Trãi, Q.1", "1,4 km · 20–30 phút", "22.000đ", 0)
           + outlet_card("Phở Gánh 1975", "Phở bò · Lý Tự Trọng, Q.1", "0,9 km · 15–25 phút", "18.000đ", 5)
           + outlet_card("Trà Sữa Mây", "Trà sữa · Pasteur, Q.3", "2,1 km · 25–35 phút", "24.000đ", 4)
           + outlet_card("Bánh Mì Cô Ba", "Bánh mì · Lê Thị Riêng, Q.1", "1,8 km · 20–30 phút", "22.000đ", 1, closed=True))
    note = card(row(icon("info", 18, C["t2"]), txt("Bạn chuyển khoản tiền món + phí giao cho tài xế. Tài xế trả tiền quán thay bạn. Onway không cộng thêm giá món.", "bsm", C["t2"]), gap=10, align="flex-start"), pad=12, bg=C["ink25"])
    return phone(head + body(chips + note + section_title("Quán gần bạn") + f'<div style="margin-top: -12px">{lst}</div>', bg="#FFFFFF", gap=14))


@frame("C-033", "Food browse home", "Đặt món · Chọn món")
def c033():
    return [("Mặc định", food_home()), ("Đang tải", food_home("loading")), ("Ngoài khu vực", food_home("noregion"))]


def food_search(state="results"):
    head = f'<div style="padding: {TOP}px 16px 12px; background: #FFFFFF; border-bottom: 1px solid {C["b1"]}; display: flex; gap: 8px; align-items: center">{ibtn("arrow-left", "Quay lại", "ghost", 44)}<div style="flex-grow: 1">{search_bar("Tìm quán hoặc món", "" if state == "empty_q" else ("cơm tấm" if state != "empty" else "bún mắm"))}</div></div>'
    if state == "empty":
        c = empty_state("search", "Không tìm thấy “bún mắm”", "Onway đang có số quán giới hạn trong giai đoạn đầu. Thử tên món khác hoặc xem quán gần bạn.", btn("Xem quán gần bạn", "outline", "md"))
    elif state == "error":
        c = empty_state("alert-circle", "Không tải được kết quả", "Kiểm tra kết nối mạng rồi thử lại.", btn("Thử lại", "outline", "md", "refresh"))
    else:
        c = (txt("Quán", "lbl", C["t3"]) + outlet_card("Cơm Tấm Sà Bì", "Nguyễn Trãi, Q.1", "1,4 km", "22.000đ", 0) + outlet_card("Cơm Tấm Sà Bì", "Võ Văn Tần, Q.3", "2,6 km", "26.000đ", 0)
             + txt("Món", "lbl", C["t3"], extra="margin-top: 12px")
             + list_row("Cơm tấm sườn bì chả", "Cơm Tấm Sà Bì · 55.000đ", lead=food_img(44, 44, 0, 8), chevron=False, pad="10px 0")
             + list_row("Cơm tấm sườn nướng", "Cơm Tấm Sà Bì · 45.000đ", lead=food_img(44, 44, 0, 8), chevron=False, pad="10px 0", border=False))
    return phone(head + body(c, bg="#FFFFFF", gap=4))


@frame("C-034", "Food outlet/brand search", "Đặt món · Chọn món")
def c034():
    return [("Kết quả", food_search()), ("Không có kết quả", food_search("empty")), ("Lỗi", food_search("error"))]


def menu_item(name, desc, price, hue, unavailable=False, qty=0):
    op = "opacity: .5; " if unavailable else ""
    right = (pill("cancelled", "Hết món", "sm") if unavailable else (badge(qty, "ink") if qty else ibtn("plus", f"Thêm {name}", "outline", 36)))
    return (f'<div style="{op}display: flex; gap: 12px; padding: 14px 0; border-bottom: 1px solid {C["b1"]}"><div style="flex-grow: 1; min-width: 0"><div style="{TY["bmd"]}; font-weight: 600">{name}</div>'
            f'<div style="{TY["bsm"]}; color: {C["t2"]}">{desc}</div><div style="margin-top: 6px">{num(price, 15, weight=600)}</div></div>'
            f'<div style="display: flex; flex-direction: column; align-items: flex-end; gap: 8px">{food_img(72, 72, hue, 10, name)}{right}</div></div>')


def outlet_menu(state="default"):
    hero = (f'<div style="position: relative; height: 180px; background: {C["m_major"]}; flex-shrink: 0; display: flex; align-items: center; justify-content: center; color: #B87F22">{icon("utensils", 48, "#B87F22")}'
            f'<div style="position: absolute; top: {TOP}px; left: 16px; right: 16px; display: flex; justify-content: space-between">{circle_btn("arrow-left", "Quay lại")}{circle_btn("search", "Tìm trong thực đơn")}</div></div>')
    closed = state == "closed"
    info = col(row(h("Cơm Tấm Sà Bì", "hlg"), spacer(), pill("paused", "Đóng cửa") if closed else pill("active", "Đang mở")),
               txt(OUT_ADDR, "bsm", C["t2"]), row(txt("1,4 km · 20–30 phút", "cap", C["t3"]), txt("·", "cap", C["t3"]), txt("Mở 06:00–21:00", "cap", C["t3"]), gap=6), gap=6)
    b = ""
    if closed:
        b = banner("warning", "Quán đã đóng cửa", "Quán mở lại lúc 06:00 sáng mai. Bạn có thể xem thực đơn nhưng chưa đặt được.")
    elif state == "stale":
        b = banner("warning", "Giá có thể đã thay đổi", "Giá món cập nhật lần cuối 3 ngày trước. Nếu giá tại quán khác, tài xế sẽ gửi đề xuất để bạn đồng ý trước khi mua.")
    items = (menu_item("Cơm tấm sườn bì chả", "Sườn nướng, bì, chả trứng, mỡ hành", "55.000đ", 0, qty=2 if state == "default" else 0)
             + menu_item("Cơm tấm sườn nướng", "Sườn cốt lết nướng than", "45.000đ", 0)
             + menu_item("Cơm tấm sườn trứng ốp la", "Sườn nướng, trứng ốp la", "50.000đ", 5, unavailable=state == "unavail")
             + menu_item("Trà đá", "Ly 500 ml", "5.000đ", 3))
    tabs_ = tabs(["Cơm tấm", "Món thêm", "Đồ uống"], 0)
    cart = "" if closed else bottom(btn('Xem giỏ hàng · 2 món <span style="font-family: ' + MONO + '; margin-left: 8px">110.000đ</span>', "primary", "lg", "bag", full=True, href="C-037.dc.html"))
    return phone(hero + body(info + b + tabs_ + f'<div style="margin-top: -12px">{items}</div>', bg="#FFFFFF", gap=14) + cart)


@frame("C-035", "Outlet menu", "Đặt món · Chọn món")
def c035():
    return [("Mặc định", outlet_menu()), ("Quán đóng cửa", outlet_menu("closed")), ("Món hết", outlet_menu("unavail")), ("Cảnh báo giá cũ", outlet_menu("stale"))]


def item_sheet(state="qty"):
    un = state == "unavail"
    inner = (f'<div style="padding: 0 16px {BOT}px; display: flex; flex-direction: column; gap: 14px">{food_img("100%", 160, 0, 12)}'
             + row(h("Cơm tấm sườn bì chả", "hmd", "h2"), spacer(), num("55.000đ", 18, weight=700))
             + txt("Sườn nướng than, bì trộn thính, chả trứng hấp, mỡ hành, đồ chua.", "bsm", C["t2"])
             + (banner("neutral", "Món tạm hết", "Quán báo hết món này hôm nay. Chọn món khác trong thực đơn.") if un else
                ovl("Tuỳ chọn") + radio("Cơm thường", True) + radio("Thêm cơm", False, right=num("+5.000đ", 14, C["t2"]))
                + field("Ghi chú cho quán", "", "VD: ít mỡ hành, không đồ chua"))
             + (banner("info", "Giá tham khảo", "Giá được Onway cập nhật từ quán. Nếu giá thực tế khác, tài xế sẽ hỏi ý bạn trước khi mua.") if state == "note" else "")
             + (btn("Món tạm hết", "disabled", "lg", full=True) if un else row(stepper(2 if state != "note" else 1), btn("Thêm vào giỏ · " + ("110.000đ" if state != "note" else "55.000đ"), "primary", "lg", full="grow"), gap=12))
             + "</div>")
    return phone(sheet_over(outlet_menu("stale" if state == "note" else "default"), inner))


@frame("C-036", "Menu item detail", "Đặt món · Chọn món")
def c036():
    return [("Chọn số lượng", item_sheet()), ("Món hết", item_sheet("unavail")), ("Ghi chú giá", item_sheet("note"))]


def cart_line(name, opt, qty, price, state=""):
    extra = ""
    if state == "unavail":
        extra = f'<div style="display: flex; gap: 6px; align-items: center; {TY["cap"]}; font-size: 13px; color: {C["err"]}; margin-top: 4px">{icon("alert-circle", 14, C["err"])}Món vừa hết — hãy xoá khỏi giỏ</div>'
    if state == "price":
        extra = f'<div style="display: flex; gap: 6px; align-items: center; {TY["cap"]}; font-size: 13px; color: {C["warn"]}; margin-top: 4px">{icon("alert-triangle", 14, C["warn"])}Giá cập nhật: 50.000đ → 55.000đ</div>'
    return (f'<div style="display: flex; gap: 12px; padding: 14px 0; border-bottom: 1px solid {C["b1"]}{"; opacity: .7" if state == "unavail" else ""}">{food_img(56, 56, 0, 8)}'
            f'<div style="flex-grow: 1; min-width: 0"><div style="{TY["bmd"]}; font-weight: 600">{name}</div><div style="{TY["cap"]}; color: {C["t3"]}">{opt}</div>{extra}'
            f'<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 8px">{num(price, 15, weight=600)}{btn("Xoá", "danger", "sm", "trash") if state == "unavail" else stepper(qty)}</div></div></div>')


def food_cart(state="default"):
    b = ""
    if state == "unavail":
        b = banner("danger", "Một món trong giỏ đã hết", "Xoá món hết để tiếp tục đặt.")
    if state == "price":
        b = banner("warning", "Giá món đã được cập nhật", "Tổng tiền món tăng 10.000đ so với lúc bạn thêm vào giỏ.")
    lines = (cart_line("Cơm tấm sườn bì chả", "Cơm thường", 2, "110.000đ" if state != "price" else "110.000đ", "price" if state == "price" else "")
             + cart_line("Trà đá", "Ly 500 ml", 1, "5.000đ")
             + (cart_line("Cơm tấm sườn trứng ốp la", "Cơm thường", 1, "50.000đ", "unavail") if state == "unavail" else ""))
    cta = btn("Chọn địa chỉ giao", "disabled" if state == "unavail" else "primary", "lg", full=True, href="C-039.dc.html")
    return phone(topbar("Giỏ hàng", True, sub="Cơm Tấm Sà Bì · Nguyễn Trãi") + body(b + f'<div style="margin-top: -8px">{lines}</div>'
                                                                                     + btn("Thêm món", "ghost", "md", "plus") + price_row("Tạm tính tiền món", "115.000đ", sub="Chưa gồm phí giao"),
                                                                                     bg="#FFFFFF", gap=12) + bottom(cta))


@frame("C-037", "Food cart", "Đặt món · Giỏ hàng & thanh toán")
def c037():
    return [("Mặc định", food_cart()), ("Món hết", food_cart("unavail")), ("Giá thay đổi", food_cart("price"))]


def deliv_addr(state="search"):
    if state == "pin":
        inner = (f'<div style="padding: 0 16px {BOT}px; display: flex; flex-direction: column; gap: 12px"><div style="height: 300px; border-radius: 12px; overflow: hidden; border: 1px solid {C["b2"]}">{map_svg(358, 300, pins=[("center", 0.5, 0.55)])}</div>'
                 f'{col(txt("Giao đến", "cap", C["t3"]), txt("142 Lê Văn Sỹ", "hsm"), txt("Phường 10, Phú Nhuận", "bsm", C["t2"]), gap=2)}{field("", "", "Ghi chú: số tầng, cổng, người nhận", ic="pencil")}'
                 f'{btn("Giao đến đây", "primary", "lg", full=True, href="C-039.dc.html")}</div>')
    else:
        rows = (list_row("Nhà", HOME_ADDR, "home", chevron=False) + list_row("Công ty", "Toà nhà Bitexco, 2 Hải Triều, Q.1", "briefcase", chevron=False)
                + list_row("Chọn trên bản đồ", "Kéo ghim đến đúng cửa nhà", "map-pin"))
        w = ""
        if state == "outside":
            rows = list_row("KDC Trung Sơn, Bình Chánh", "Đường số 9A · 7,8 km từ quán", "map-pin", chevron=False, right=pill("paused", "Ngoài vùng", "sm")) + rows
            w = f'<div style="padding: 0 16px">{banner("warning", "Địa chỉ giao ngoài khu vực phục vụ", "Quán nằm trong vùng nên đơn vẫn được đặt. Tài xế sẽ thấy cảnh báo và có thể từ chối; phí giao tính theo quãng đường thực tế.")}</div>'
        inner = f'<div style="padding: 0 0 {BOT}px; display: flex; flex-direction: column; gap: 8px"><div style="padding: 0 16px">{search_bar("Tìm địa chỉ giao", "trung son" if state == "outside" else "")}</div>{w}{rows}</div>'
    return phone(sheet_over(food_cart(), inner, title="Địa chỉ giao"))


@frame("C-038", "Delivery address selection", "Đặt món · Giỏ hàng & thanh toán")
def c038():
    return [("Tìm địa chỉ", deliv_addr()), ("Ghim trên bản đồ", deliv_addr("pin")), ("Ngoài khu vực", deliv_addr("outside"))]


@frame("C-039", "Food checkout price review", "Đặt món · Giỏ hàng & thanh toán")
def c039():
    return [("Mặc định", phone(topbar("Xác nhận đơn", True) + body(
        card(row(icon_tile("store", 40), col(txt("Cơm Tấm Sà Bì", "bmd", extra="font-weight: 700"), txt(OUT_ADDR, "cap", C["t3"]), gap=2), gap=12)
             + divider() + row(icon_tile("home", 40), col(txt("Giao đến · Nhà", "bmd", extra="font-weight: 700"), txt(HOME_ADDR, "cap", C["t3"]), gap=2), spacer(), btn("Đổi", "ghost", "sm"), gap=12), pad=14)
        + card(price_row("2 × Cơm tấm sườn bì chả", "110.000đ") + price_row("1 × Trà đá", "5.000đ") + divider()
               + price_row("Tiền món", "115.000đ", sub="Giá tham khảo từ quán")
               + price_row("Phí giao hàng", "22.000đ", sub="Onway đề xuất theo quãng đường 3,4 km · không thương lượng")
               + divider() + price_row("Tổng chuyển cho tài xế", "137.000đ", True), pad=16, gap=10)
        + card(timeline([("Onway tìm tài xế", "Bạn chưa cần trả tiền", "current"), ("Chuyển khoản 137.000đ cho tài xế", "Sau khi có tài xế", "todo"),
                         ("Tài xế mua món tại quán", "Nếu giá khác, tài xế hỏi bạn trước", "todo"), ("Tài xế giao món", "", "todo")], dense=True), pad=16)
        + txt("Sau khi tài xế đã đặt món với quán, bạn không thể huỷ để nhận lại tiền.", "cap", C["t3"]), bg=C["page"], gap=12)
        + bottom(btn("Đặt món · 137.000đ", "primary", "lg", full=True, href="C-040.dc.html"))))]


def food_matching(state="matching"):
    rings = "".join(f'<circle cx="{0.3*PW:.0f}" cy="{0.44*PH:.0f}" r="{r}" fill="none" stroke="rgba(58,99,204,{a})" stroke-width="2"/>' for r, a in [(60, .35), (110, .22), (160, .12)])
    m = M(pins=[("outlet", 0.3, 0.44), ("driver-idle", 0.52, 0.3), ("driver-idle", 0.1, 0.24)], extra_svg=rings)
    s = (pill("searching") if state == "timeout" else pill("matching"))
    sub = banner("warning", "Còn 00:10", "Chưa có tài xế nhận. Bạn có thể thử lại sau khi hết giờ.") if state == "timeout" else row(icon("timer", 16, C["t2"]), txt('Thời gian tìm còn <span style="font-family: ' + MONO + '; color: ' + C["t1"] + '; font-weight: 600">01:40</span>', "bsm", C["t2"]), gap=6)
    sheet = (f'<div style="padding: 4px 16px {BOT}px; display: flex; flex-direction: column; gap: 14px" aria-live="polite">{row(s, spacer(), num("137.000đ", 17, weight=700))}'
             f'{h("Đang tìm tài xế mua & giao món", "hmd", "h2")}{progress(90 if state == "timeout" else 35, C["info"])}{sub}{divider()}'
             f'{addr_block("Cơm Tấm Sà Bì · Nguyễn Trãi", "Nhà · 142 Lê Văn Sỹ")}{txt("Bạn chưa cần chuyển tiền cho đến khi có tài xế nhận đơn.", "cap", C["t3"])}{btn("Huỷ đơn", "outline", "lg", full=True)}</div>')
    return phone(map_screen(m, sheet))


@frame("C-040", "Food matching", "Đặt món · Ghép tài xế & thanh toán")
def c040():
    return [("Đang ghép", food_matching()), ("Sắp hết giờ", food_matching("timeout"))]


@frame("C-041", "No Food driver found", "Đặt món · Ghép tài xế & thanh toán")
def c041():
    return [("Không có tài xế", phone(topbar("", False, right=ibtn("x", "Đóng", "ghost", 44), border=False) + body(
        empty_state("bag", "Chưa có tài xế nhận đơn", "Các tài xế gần quán đang bận. Đơn chưa được đặt với quán và bạn chưa phải chuyển tiền.")
        + card(price_row("Tổng dự kiến", "137.000đ", True) + txt("Cơm Tấm Sà Bì · 3 món", "cap", C["t3"]), pad=14), extra="justify-content: center", bg="#FFFFFF")
        + bottom(btn("Thử tìm lại", "primary", "lg", "refresh", full=True, href="C-040.dc.html") + btn("Huỷ đơn", "ghost", "lg", full=True), border=False)))]


FOOD_DRIVER = person_row("Lê Quốc Bảo", "Yamaha Sirius · Đen", "LB", rating="4,8", plate="59-P1 456.78")


def food_matched_pay():
    return phone(topbar("Thanh toán đơn món", True, sub="F-3M8TP") + body(
        pill("accepted") + FOOD_DRIVER
        + card(txt("Chuyển khoản trước để tài xế mua món", "hsm") + txt("Tài xế chỉ đặt món với quán sau khi xác nhận đã nhận đủ tiền.", "bsm", C["t2"]), pad=14, bg=C["brand_bg"], extra=f"border-color: {C['red']}33")
        + f'<div style="margin: 0 -16px">{pay_info("137.000đ", "F-3M8TP", "ONW F3M8TP", "C-043.dc.html").replace("padding: 8px 16px 34px", "padding: 0 16px")}</div>',
        bg="#FFFFFF", gap=14))


@frame("C-042", "Food driver matched / payment instructions", "Đặt món · Ghép tài xế & thanh toán")
def c042():
    return [("QR & thông tin chuyển khoản", food_matched_pay())]


@frame("C-043", "Food proof upload", "Đặt món · Ghép tài xế & thanh toán")
def c043():
    b = food_matched_pay()
    return [(lab, proof_sheet(s, "137.000đ", b).replace("C-028.dc.html", "C-045.dc.html").replace("TRAN VAN HUNG", "LE QUOC BAO"))
            for lab, s in [("Chưa có ảnh", "empty"), ("Đang tải lên", "uploading"), ("Tải lên thất bại", "failed"), ("Đã gửi", "done")]]


@frame("C-044", "Food proof rejected / disputed", "Đặt món · Ghép tài xế & thanh toán")
def c044():
    return [("Cần bổ sung", proof_rejected("food").replace("Hùng", "Bảo")), ("Đang tranh chấp", disputed("F-3M8TP", "CS-240924-0142", "đơn"))]


def food_active(state="to_outlet"):
    steps = [("Tài xế nhận đơn", "11:02", "done"), ("Đã nhận đủ tiền", "11:05 · 137.000đ", "done"),
             ("Đến quán & đặt món", "", "todo"), ("Đang giao", "", "todo"), ("Đã giao", "", "todo")]
    if state == "to_outlet":
        m = M(route=[(0.1, 0.24), (0.3, 0.24), (0.3, 0.44)], pins=[("outlet", 0.3, 0.44)], driver=(0.1, 0.24))
        head = job_header("arriving", "Bảo đang đến quán", "Đến quán sau khoảng 6 phút", num("F-3M8TP", 13, C["t3"]))
        steps[2] = ("Đến quán & đặt món", "Dự kiến 11:12", "current")
    elif state == "at_outlet":
        m = M(pins=[("outlet", 0.3, 0.44)], driver=(0.32, 0.42))
        head = job_header("atOutlet", "Bảo đang đặt món tại quán", "Quán thường chuẩn bị trong 10–15 phút", num("F-3M8TP", 13, C["t3"]))
        steps[2] = ("Đang đặt món tại quán", "Từ 11:12", "current")
    else:
        m = M(route=F_ROUTE[1:], pins=[("outlet", 0.3, 0.44), ("dropoff", 0.72, 0.17)], driver=(0.52, 0.36))
        head = job_header("delivering", "Món đang đến · 12 phút", "Dự kiến giao lúc 11:48", num("F-3M8TP", 13, C["t3"]))
        steps[2] = ("Đã lấy món", "11:31", "done")
        steps[3] = ("Đang giao", "Dự kiến 11:48", "current")
    sheet = head + f'<div style="padding: 0 16px {BOT}px; display: flex; flex-direction: column; gap: 14px">{FOOD_DRIVER}{timeline(steps, True)}{row(btn("Huỷ đơn", "ghost", "md", href="C-065.dc.html") if state != "delivering" else "", spacer(), btn("Báo sự cố", "ghost", "md", "flag", href="C-053.dc.html"))}</div>'
    return phone(map_screen(m, sheet, back_float("Thu nhỏ", "chevron-down")))


@frame("C-045", "Active Food - driver going to outlet", "Đặt món · Theo dõi đơn")
def c045():
    return [("Đang đến quán", food_active())]


@frame("C-046", "Active Food - driver at outlet", "Đặt món · Theo dõi đơn")
def c046():
    return [("Tại quán", food_active("at_outlet"))]


def proposal(state="pending"):
    top = {"pending": pill("changeRequested"), "accepted": pill("confirmed", "Bạn đã đồng ý"), "rejected": pill("cancelled", "Bạn đã từ chối")}[state]
    timer = (card(row(icon("timer", 20, C["warn"]), col(txt("Trả lời trong", "cap", C["warn"]), num("04:32", 22, C["warn"], 700), gap=0), spacer(),
                      txt("Hết giờ, đơn chuyển Onway xem xét", "cap", C["t2"], extra="max-width: 150px; text-align: right"), gap=10), pad=12, bg=C["warn_bg"], extra=f"border-color: {C['warn_b']}55") if state == "pending" else "")
    change = card(ovl("Thay đổi tại quán")
                  + row(txt("2 × Cơm tấm sườn bì chả", "bmd", extra="font-weight: 600"), spacer(), gap=8)
                  + price_row("Giá trên Onway", "110.000đ") + price_row("Giá thực tế tại quán", "120.000đ", color=C["t1"])
                  + divider() + price_row("Cần chuyển thêm", "+10.000đ", True, color=C["warn"])
                  + row(photo(64, 64, "", "image", 8), txt("Ảnh bảng giá tại quán — tài xế chụp lúc 11:14", "cap", C["t3"]), gap=10), pad=16, gap=10)
    if state == "pending":
        acts = btn("Đồng ý & chuyển thêm 10.000đ", "primary", "lg", full=True, href="C-048.dc.html") + row(btn("Từ chối", "danger", "lg", full="grow"), btn("Gọi tài xế", "outline", "lg", "phone", full="grow"), gap=8)
    elif state == "accepted":
        acts = btn("Chuyển thêm 10.000đ", "primary", "lg", "qr", full=True, href="C-048.dc.html")
        change += banner("success", "Đã cập nhật đơn", "Tổng mới 147.000đ. Tài xế mua món sau khi nhận đủ tiền bổ sung.")
    else:
        acts = btn("Về theo dõi đơn", "secondary", "lg", full=True)
        change += banner("neutral", "Bạn đã từ chối thay đổi", "Tài xế không mua món bị ảnh hưởng. Đơn được xử lý theo chính sách huỷ/giao một phần — Onway sẽ thông báo cho bạn.")
    return phone(topbar("Đề xuất thay đổi", True, sub="F-3M8TP") + body(top + h("Giá món tại quán khác trên ứng dụng", "hlg") + txt("Tài xế Bảo gửi đề xuất trước khi mua. Đề xuất trong ứng dụng là căn cứ chính thức.", "bmd", C["t2"])
                                                                        + timer + change, bg="#FFFFFF", gap=14) + bottom(acts))


@frame("C-047", "Food change proposal", "Đặt món · Thay đổi tại quán")
def c047():
    return [("Chờ trả lời", proposal()), ("Đã đồng ý", proposal("accepted")), ("Đã từ chối", proposal("rejected"))]


QRBOX96 = '<div style="padding: 6px; border: 1px solid ' + C["b2"] + '; border-radius: 10px">' + qr_svg(96) + "</div>"


@frame("C-048", "Supplemental payment required", "Đặt món · Thay đổi tại quán")
def c048():
    inner = (f'<div style="padding: 8px 16px {BOT}px; display: flex; flex-direction: column; gap: 14px">'
             f'{row(QRBOX96, col(txt("Chuyển thêm", "cap", C["t3"]), num("10.000đ", 28, weight=700), txt("LE QUOC BAO · Vietcombank 0071 0034 5566", "cap", C["t3"]), num("ONW F3M8TP BS1", 13, C["t2"]), gap=4), gap=16)}'
             f'{upload_tile("empty", "Ảnh giao dịch bổ sung")}{banner("info", "Tài xế chờ bạn trước khi mua", "Tài xế chỉ mua phần món thay đổi sau khi xác nhận đã nhận đủ 10.000đ.")}'
             f'{btn("Gửi chứng từ bổ sung", "disabled", "lg", full=True)}</div>')
    return [("Chuyển tiền bổ sung", phone(sheet_over(proposal("accepted"), inner, title="Thanh toán bổ sung")))]


@frame("C-049", "Food proposal timeout", "Đặt món · Thay đổi tại quán")
def c049():
    return [("Hết thời gian trả lời", phone(topbar("Đề xuất thay đổi", True, sub="F-3M8TP") + body(
        pill("expired", "Hết thời gian") + h("Đề xuất đã hết hạn", "hlg")
        + txt("Bạn chưa trả lời trong 5 phút nên tài xế không mua món bị ảnh hưởng. Onway đang xem xét đơn để quyết định huỷ hay giao phần còn lại.", "bmd", C["t2"])
        + card(timeline([("Tài xế gửi đề xuất +10.000đ", "11:14", "done"), ("Hết thời gian trả lời", "11:19", "failed"), ("Onway xem xét đơn", "Thông báo trong 30 phút", "current")], True), pad=16)
        + banner("info", "Bạn sẽ không mất tiền vì món chưa mua", "Khoản cho món chưa mua được tài xế hoàn lại trực tiếp theo kết luận của Onway."), bg="#FFFFFF", gap=14)
        + bottom(btn("Gọi tài xế", "outline", "lg", "phone", full=True) + btn("Liên hệ hỗ trợ", "ghost", "lg", "help", full=True))))]


@frame("C-050", "Active Food - delivering", "Đặt món · Theo dõi đơn")
def c050():
    return [("Đang giao", food_active("delivering"))]


@frame("C-051", "Food delivered summary", "Đặt món · Theo dõi đơn")
def c051():
    return [("Đã giao", phone(topbar("", False, right=ibtn("x", "Đóng", "ghost", 44), border=False) + body(
        f'<div style="display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center">'
        f'<div style="width: 64px; height: 64px; border-radius: 999px; background: {C["ok_bg"]}; display: flex; align-items: center; justify-content: center">{icon("check", 32, C["ok"], 2.5)}</div>'
        f'{h("Món đã giao tới bạn", "hlg")}{txt("11:46 · 24/09/2026 · F-3M8TP", "bsm", C["t2"])}</div>'
        + card(price_row("Tiền món", "115.000đ") + price_row("Phí giao hàng", "22.000đ") + divider() + price_row("Đã chuyển cho tài xế", "137.000đ", True)
               + kv("Chứng từ", "Tài xế đã xác nhận nhận đủ"), pad=16, gap=10)
        + card(row(avatar("LB", 44), col(txt("Đánh giá tài xế Bảo", "bmd", extra="font-weight: 600"), stars(5, 0, 24), gap=6), gap=12), pad=14), bg="#FFFFFF", gap=16)
        + bottom(btn("Đánh giá", "primary", "lg", full=True, href="C-052.dc.html") + btn("Báo cáo vấn đề với đơn", "ghost", "lg", "flag", full=True, href="C-053.dc.html"), border=False)))]


# ================= RATING / COMPLAINT / CHAT =================
@frame("C-052", "Rating after Ride/Food", "Đánh giá & khiếu nại")
def c052():
    tags_ = f'<div style="display: flex; flex-wrap: wrap; gap: 8px">{"".join(tag(t, t in ("Đúng giờ", "Lái xe an toàn")) for t in ["Đúng giờ", "Thân thiện", "Lái xe an toàn", "Xe sạch sẽ", "Biết đường", "Hỗ trợ nhiệt tình"])}</div>'
    return [("5 sao + thẻ nhanh", phone(topbar("Đánh giá", False, right=btn("Bỏ qua", "ghost", "sm")) + body(
        f'<div style="display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center; padding-top: 12px">{avatar("TH", 72)}'
        f'{h("Chuyến đi với Hùng thế nào?", "hmd")}{txt("R-7Q2K9 · 24/09 · 08:41", "cap", C["t3"])}{stars(5, 5, 40)}{txt("Tuyệt vời", "lbl", C["t1"])}</div>'
        + txt("Điều bạn thích", "lbl") + tags_ + field("Nhận xét (không bắt buộc)", "", "Chia sẻ thêm cho tài xế", textarea=True)
        + txt("Có vấn đề cần Onway xử lý? <a href=\"C-053.dc.html\" style=\"font-weight: 600\">Gửi khiếu nại riêng</a>", "bsm", C["t2"]), bg="#FFFFFF", gap=16)
        + bottom(btn("Gửi đánh giá", "primary", "lg", full=True))))]


def complaint_form(err=False):
    return phone(topbar("Gửi khiếu nại", True, sub="Chuyến R-7Q2K9") + body(
        select("Loại vấn đề", "" if err else "Thanh toán", error="Chọn loại vấn đề." if err else None)
        + card(row(icon_tile("bike", 40), col(txt("Chuyến xe máy · 24/09 08:27", "bsm", extra="font-weight: 600"), txt("Tài xế Trần Văn Hùng · 48.000đ", "cap", C["t3"]), gap=2), gap=12), pad=12)
        + field("Mô tả chi tiết", "Tài xế" if err else "Tôi đã chuyển 48.000đ lúc 08:14 nhưng tài xế nói chưa nhận và yêu cầu chuyển lại.", textarea=True,
                error="Mô tả tối thiểu 20 ký tự để đội hỗ trợ hiểu vấn đề." if err else None, helper=None if err else "Ghi thời gian, số tiền, điều đã xảy ra.")
        + txt("Bằng chứng (không bắt buộc)", "lbl") + row(photo(88, 88, "Ảnh 1", "image", 10), f'<button type="button" style="width: 88px; height: 88px; border-radius: 10px; border: 1.5px dashed {C["b3"]}; background: {C["ink25"]}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; font-family: {FONT}; font-size: 12px; color: {C["t2"]}">{icon("plus", 20)}Thêm ảnh</button>', gap=8)
        + txt("Ảnh được lưu riêng tư, chỉ đội xử lý khiếu nại xem. Khiếu nại không tự động trở thành cáo buộc gian lận.", "cap", C["t3"]), bg="#FFFFFF", gap=14)
        + bottom(btn("Gửi khiếu nại", "primary", "lg", full=True, href="C-054.dc.html")))


@frame("C-053", "Complaint/report form", "Đánh giá & khiếu nại")
def c053():
    return [("Mặc định", complaint_form()), ("Lỗi nhập liệu", complaint_form(True))]


@frame("C-054", "Complaint submitted", "Đánh giá & khiếu nại")
def c054():
    return [("Đã gửi", phone(topbar("", False, right=ibtn("x", "Đóng", "ghost", 44), border=False) + body(
        f'<div style="display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center">'
        f'<div style="width: 64px; height: 64px; border-radius: 999px; background: {C["ok_bg"]}; display: flex; align-items: center; justify-content: center">{icon("check", 32, C["ok"], 2.5)}</div>'
        f'{h("Đã gửi khiếu nại", "hlg")}{txt("Mã khiếu nại", "cap", C["t3"])}{num("CS-240924-0137", 20, weight=700)}</div>'
        + card(txt("Điều gì xảy ra tiếp theo", "hsm") + timeline([("Onway tiếp nhận", "Vừa xong", "done"), ("Đội hỗ trợ xem xét", "Phản hồi trong 24 giờ", "current"),
                                                                   ("Có thể hỏi thêm bạn hoặc tài xế", "Qua thông báo trong ứng dụng", "todo"), ("Kết luận", "", "todo")], True), pad=16),
        bg="#FFFFFF", gap=16)
        + bottom(btn("Xem khiếu nại", "secondary", "lg", full=True, href="C-063.dc.html") + btn("Về trang chủ", "ghost", "lg", full=True), border=False)))]


def bubble(text_, me=False, time="", status="", img=False, failed=False, queued=False):
    bg = C["inverse"] if me else C["sunken"]
    fg = "#FFFFFF" if me else C["t1"]
    al = "flex-end" if me else "flex-start"
    content = (photo(200, 140, "Ảnh", "image", 10) if img else f'<div style="padding: 10px 14px; border-radius: 16px; {"border-bottom-right-radius: 4px" if me else "border-bottom-left-radius: 4px"}; background: {bg}; color: {fg}; {TY["bmd"]}">{text_}</div>')
    meta = time
    if status:
        meta += f' · {status}'
    m = f'<div style="{TY["cap"]}; color: {C["t3"]}; display: flex; gap: 4px; align-items: center">{meta}</div>'
    if failed:
        m = f'<div style="display: flex; gap: 8px; align-items: center; {TY["cap"]}; color: {C["err"]}">{icon("alert-circle", 14, C["err"])}Không gửi được ảnh <a href="#" style="font-weight: 700; color: {C["t1"]}">Thử lại</a><a href="#" style="font-weight: 600; color: {C["t2"]}">Xoá</a></div>'
    if queued:
        m = f'<div style="display: flex; gap: 6px; align-items: center; {TY["cap"]}; color: {C["t3"]}">{icon("clock", 12)}Chờ gửi khi có mạng</div>'
    op = "; opacity: .6" if (failed or queued) and img else ("; opacity: .7" if queued else "")
    return f'<div style="display: flex; flex-direction: column; align-items: {al}; gap: 4px; max-width: 80%; align-self: {al}{op}">{content}{m}</div>'


def chat(state="default", who="c"):
    other, ini, ref = ("Trần Văn Hùng", "TH", "Chuyến R-7Q2K9") if who == "c" else ("Minh Anh (khách)", "MA", "Chuyến R-7Q2K9")
    head = (f'<div style="display: flex; align-items: center; gap: 8px; padding: {TOP}px 8px 8px; border-bottom: 1px solid {C["b1"]}; background: #FFFFFF">{ibtn("arrow-left", "Quay lại", "ghost", 44)}'
            f'{avatar(ini, 40)}<div style="flex-grow: 1; min-width: 0"><div style="{TY["bmd"]}; font-weight: 700">{other}</div><div style="{TY["cap"]}; color: {C["t3"]}">{ref} · {pill("arriving", size="sm") if state != "closed" else "Đã kết thúc"}</div></div>'
            f'{ibtn("phone", "Gọi điện", "outline", 44) if state != "closed" else ""}</div>')
    me = who == "c"
    msgs = [bubble("Chào bạn, mình đang đứng ở cổng Hải Triều, áo xanh nhé.", me, "08:12", "Đã xem" if me else ""),
            bubble("Dạ em thấy rồi, 2 phút nữa em tới. Anh chuyển khoản giúp em trước nha.", not me, "08:13"),
            bubble("", me, "08:14", "Đã xem" if me else "", img=True),
            bubble("Em nhận đủ rồi ạ, cảm ơn anh.", not me, "08:16")]
    top_b = ""
    inp_dis = False
    if state == "failed":
        msgs.append(bubble("", me, "08:18", img=True, failed=True))
    if state == "offline":
        top_b = f'<div style="padding: 8px 16px; background: {C["sunken"]}; display: flex; gap: 8px; align-items: center; {TY["bsm"]}; color: {C["t2"]}">{spinner(14)}Mất kết nối — đang kết nối lại…</div>'
        msgs.append(bubble("Mình ra cổng chính rồi nhé", me, "08:18", queued=True))
    if state == "closed":
        inp_dis = True
    day = f'<div style="align-self: center; {TY["cap"]}; color: {C["t3"]}; padding: 4px 10px; border-radius: 999px; background: {C["sunken"]}">Hôm nay</div>'
    area = f'<div style="flex-grow: 1; min-height: 0; overflow: hidden; display: flex; flex-direction: column; gap: 12px; padding: 16px; background: #FFFFFF; justify-content: flex-end">{day}{"".join(msgs)}</div>'
    if inp_dis:
        comp = bottom(banner("neutral", "Cuộc trò chuyện đã đóng", "Chuyến đã kết thúc. Tin nhắn chỉ xem được 7 ngày; nội dung liên quan khiếu nại được lưu làm bằng chứng.", "lock"))
    else:
        comp = (f'<div style="display: flex; gap: 8px; align-items: center; padding: 10px 12px {BOT}px; border-top: 1px solid {C["b1"]}; background: #FFFFFF">{ibtn("camera", "Gửi ảnh", "ghost", 44)}'
                f'<div style="flex-grow: 1">{search_bar("Nhắn tin…").replace(IC["search"], IC["message"])}</div>{ibtn("send", "Gửi", "secondary", 44)}</div>')
    return phone(head + top_b + area + comp)


@frame("C-055", "Chat room", "Chat & gọi điện")
def c055():
    return [("Văn bản, ảnh, đã xem", chat())]


@frame("C-056", "Chat image upload failed", "Chat & gọi điện")
def c056():
    return [("Ảnh gửi lỗi", chat("failed"))]


@frame("C-057", "Chat offline / reconnecting", "Chat & gọi điện")
def c057():
    return [("Đang kết nối lại", chat("offline"))]


@frame("C-058", "Chat closed / retention expired", "Chat & gọi điện")
def c058():
    return [("Chỉ đọc", chat("closed"))]


# ================= HISTORY / CASES =================
def hist_item(ic, title, sub, price, st, href):
    return (f'<a href="{href}" style="display: flex; gap: 12px; padding: 14px 0; border-bottom: 1px solid {C["b1"]}; text-decoration: none; color: {C["t1"]}">{icon_tile(ic, 44)}'
            f'<div style="flex-grow: 1; min-width: 0"><div style="{TY["bmd"]}; font-weight: 600">{title}</div><div style="{TY["cap"]}; font-size: 13px; color: {C["t3"]}">{sub}</div><div style="margin-top: 6px">{pill(st, size="sm")}</div></div>'
            f'{num(price, 15, weight=600)}</a>')


def history(state="list"):
    head = topbar("Hoạt động", False)
    seg = segmented(["Tất cả", "Đi xe", "Đặt món"], 1 if state == "filtered" else 0)
    if state == "loading":
        c = "".join(row(skel(44, 44, 10), col(skel(180, 14), skel(120, 12), skel(70, 20, 999), gap=6, extra="flex-grow: 1"), skel(60, 14), gap=12, extra="padding: 12px 0") for _ in range(6))
    elif state == "empty":
        c = empty_state("list", "Chưa có hoạt động", "Chuyến đi và đơn món của bạn sẽ xuất hiện ở đây.", btn("Đặt chuyến đầu tiên", "secondary", "md", href="C-012.dc.html"))
    else:
        items = [("bike", "ĐH Kinh tế TP.HCM", "Hôm nay, 08:27 · Xe máy", "48.000đ", "completed", "C-060.dc.html"),
                 ("utensils", "Cơm Tấm Sà Bì", "Hôm qua, 11:02 · 3 món", "137.000đ", "completed", "C-061.dc.html"),
                 ("bike", "Chợ Bến Thành", "22/09, 18:10 · Xe máy", "32.000đ", "disputed", "C-060.dc.html"),
                 ("car", "Sân bay Tân Sơn Nhất", "20/09, 05:40 · Ô tô", "168.000đ", "cancelled", "C-060.dc.html"),
                 ("utensils", "Trà Sữa Mây", "19/09, 15:22 · 2 món", "86.000đ", "completed", "C-061.dc.html")]
        if state == "filtered":
            items = [i for i in items if i[0] != "utensils"]
        c = "".join(hist_item(*i) for i in items)
    return phone(head + body(seg + f'<div style="margin-top: -8px">{c}</div>', bg="#FFFFFF", gap=12) + tabbar(1))


@frame("C-059", "Activity / Ride & Food history", "Lịch sử & khiếu nại")
def c059():
    return [("Danh sách", history()), ("Lọc Đi xe", history("filtered")), ("Đang tải", history("loading")), ("Trống", history("empty"))]


def ride_detail(state="completed"):
    st = {"completed": "completed", "cancelled": "cancelled", "disputed": "disputed"}[state]
    extra = ""
    if state == "cancelled":
        extra = banner("neutral", "Chuyến đã huỷ trước khi có tài xế", "Bạn huỷ lúc 05:42 · lý do: Đổi kế hoạch. Không phát sinh thanh toán.")
    if state == "disputed":
        extra = banner("danger", "Thanh toán đang tranh chấp", "Khiếu nại CS-240922-0098 đang được xem xét.", action=btn("Xem khiếu nại", "outline", "sm", href="C-063.dc.html"))
    return phone(topbar("Chi tiết chuyến", True, sub="R-7Q2K9" if state == "completed" else ("R-5T1WM" if state == "cancelled" else "R-2H8QD")) + body(
        row(pill(st), spacer(), txt("24/09/2026", "bsm", C["t2"])) + extra
        + f'<div style="height: 150px; border-radius: 12px; overflow: hidden; border: 1px solid {C["b2"]}; flex-shrink: 0">{map_svg(358, 150, route=[(0.72, 0.8), (0.72, 0.42), (0.3, 0.42), (0.3, 0.2)], pins=[("pickup", 0.72, 0.8), ("dropoff", 0.3, 0.2)], labels=False)}</div>'
        + card(addr_block(PICK, DROP, "08:27", "08:41"), pad=14)
        + (card(kv("Xe máy · 3,2 km · 14 phút", "48.000đ", True) + kv("Tài xế", "Trần Văn Hùng · 59-X2 123.45") + kv("Thanh toán", "Chuyển khoản trực tiếp")
                + kv("Chứng từ", "Đã xác nhận 08:16" if state == "completed" else "Đang tranh chấp"), pad=14, gap=8) if state != "cancelled" else ""),
        bg="#FFFFFF", gap=12)
        + bottom(row(btn("Báo cáo vấn đề", "outline", "lg", "flag", full="grow", href="C-053.dc.html"), btn("Đặt lại", "secondary", "lg", "refresh", full="grow"), gap=8)))


@frame("C-060", "Ride history detail", "Lịch sử & khiếu nại")
def c060():
    return [("Hoàn thành", ride_detail()), ("Đã huỷ", ride_detail("cancelled")), ("Tranh chấp", ride_detail("disputed"))]


def food_detail(state="delivered"):
    st = {"delivered": "completed", "cancelled": "cancelled", "disputed": "disputed"}[state]
    extra = ""
    if state == "cancelled":
        extra = banner("neutral", "Đơn đã huỷ", "Không có tài xế nhận đơn trong thời gian tìm. Bạn chưa chuyển tiền.")
    if state == "disputed":
        extra = banner("danger", "Đơn đang tranh chấp", "Khiếu nại CS-240924-0142: tài xế báo chưa nhận đủ tiền.", action=btn("Xem khiếu nại", "outline", "sm", href="C-063.dc.html"))
    return phone(topbar("Chi tiết đơn món", True, sub="F-3M8TP") + body(
        row(pill(st, "Đã giao" if state == "delivered" else None), spacer(), txt("23/09/2026", "bsm", C["t2"])) + extra
        + card(row(icon_tile("store", 40), col(txt("Cơm Tấm Sà Bì · Nguyễn Trãi", "bmd", extra="font-weight: 600"), txt("Giao đến Nhà · 142 Lê Văn Sỹ", "cap", C["t3"]), gap=2), gap=12), pad=14)
        + card(price_row("2 × Cơm tấm sườn bì chả", "110.000đ") + price_row("1 × Trà đá", "5.000đ") + divider() + price_row("Phí giao hàng", "22.000đ") + price_row("Tổng", "137.000đ", True), pad=14, gap=8)
        + (card(timeline([("Đặt đơn", "11:00", "done"), ("Tài xế nhận đủ tiền", "11:05", "done"), ("Đã mua món", "11:28", "done"), ("Đã giao", "11:46", "done")], True), pad=14) if state == "delivered" else ""),
        bg="#FFFFFF", gap=12) + bottom(row(btn("Báo cáo vấn đề", "outline", "lg", "flag", full="grow", href="C-053.dc.html"), btn("Đặt lại", "secondary", "lg", "refresh", full="grow"), gap=8)))


@frame("C-061", "Food order history detail", "Lịch sử & khiếu nại")
def c061():
    return [("Đã giao", food_detail()), ("Đã huỷ", food_detail("cancelled")), ("Tranh chấp", food_detail("disputed"))]


def case_list(state="list"):
    if state == "empty":
        c = empty_state("scale", "Bạn chưa có khiếu nại nào", "Khi gặp vấn đề với chuyến đi hoặc đơn món, gửi khiếu nại từ màn hình chi tiết.")
    else:
        c = (list_row("Thanh toán · R-7Q2K9", "CS-240924-0137 · Gửi hôm nay 08:30", "banknote", right=pill("pendingReview", "Đang xem xét", "sm"), href="C-063.dc.html", pad="14px 0")
             + list_row("Thanh toán · R-2H8QD", "CS-240922-0098 · Chờ bạn phản hồi", "banknote", right=pill("changeRequested", "Cần phản hồi", "sm"), href="C-063.dc.html", pad="14px 0")
             + list_row("Thái độ tài xế · R-1K3ZP", "CS-240910-0021 · Kết luận 12/09", "user", right=pill("finalized", size="sm"), href="C-063.dc.html", pad="14px 0"))
    return phone(topbar("Khiếu nại của tôi", True) + body(c, bg="#FFFFFF", gap=0, extra="justify-content: center" if state == "empty" else ""))


@frame("C-062", "Case / complaint list", "Lịch sử & khiếu nại")
def c062():
    return [("Danh sách", case_list()), ("Trống", case_list("empty"))]


def case_detail(state="review"):
    if state == "final":
        tl = [("Đã gửi khiếu nại", "24/09 08:30", "done"), ("Thu thập bằng chứng", "24/09 09:10", "done"), ("Tài xế phản hồi", "24/09 10:02", "done"), ("Kết luận", "24/09 15:40", "done")]
        dec = card(ovl("Kết luận") + txt("Xác nhận tài xế đã nhận đủ 48.000đ", "hsm") + txt("Sao kê do tài xế cung cấp khớp với ảnh chứng từ của bạn. Tài xế đã xác nhận nhầm lẫn và xin lỗi. Không có khoản nào cần hoàn.", "bsm", C["t2"]), pad=14, bg=C["ok_bg"], extra=f"border-color: {C['ok_b']}55")
        p = pill("finalized")
        acts = btn("Kháng nghị kết luận", "outline", "lg", full=True)
    else:
        tl = [("Đã gửi khiếu nại", "24/09 08:30", "done"), ("Thu thập bằng chứng", "24/09 09:10", "done"), ("Chờ tài xế phản hồi", "Hạn 25/09 09:10", "current"), ("Kết luận", "", "todo")]
        dec = banner("info", "Onway có thể cần thêm thông tin", "Nếu được yêu cầu, bạn sẽ nhận thông báo và có 24 giờ để phản hồi.")
        p = pill("pendingReview", "Đang xem xét")
        acts = btn("Gửi thêm bằng chứng", "secondary", "lg", "paperclip", full=True)
    return phone(topbar("Khiếu nại", True, sub="CS-240924-0137") + body(
        row(p, spacer(), txt("Thanh toán · R-7Q2K9", "bsm", C["t2"])) + card(timeline(tl, True), pad=16)
        + txt("Bằng chứng của bạn", "lbl") + row(photo(96, 96, "Chứng từ", "image", 10), photo(96, 96, "Ảnh 2", "image", 10), gap=8) + dec, bg="#FFFFFF", gap=14)
        + bottom(acts))


@frame("C-063", "Case / complaint detail", "Lịch sử & khiếu nại")
def c063():
    return [("Đang xem xét", case_detail()), ("Đã kết luận", case_detail("final"))]


def call_sheet(state="driver"):
    if state == "unavail":
        inner = f'<div style="padding: 0 16px {BOT}px; display: flex; flex-direction: column; gap: 12px">{banner("neutral", "Không thể gọi tài xế", "Chuyến đã kết thúc. Để liên hệ lại tài xế (VD: để quên đồ), hãy gửi yêu cầu qua Onway.", "phone")}{btn("Gửi yêu cầu tìm đồ", "secondary", "lg", full=True)}{btn("Gọi tổng đài Onway", "outline", "lg", "phone", full=True)}</div>'
        base = ride_detail()
    else:
        inner = (f'<div style="padding: 0 16px {BOT}px; display: flex; flex-direction: column; gap: 12px">{row(avatar("TH", 48), col(txt("Trần Văn Hùng", "bmd", extra="font-weight: 700"), num("0908 ••• 321", 14, C["t2"]), gap=2), gap=12)}'
                 f'{txt("Cuộc gọi dùng số điện thoại thật qua nhà mạng, cước theo gói của bạn. Chỉ gọi khi cần trao đổi về chuyến đi.", "bsm", C["t2"])}'
                 f'{btn("Gọi tài xế", "primary", "lg", "phone", full=True)}{btn("Gọi tổng đài Onway", "outline", "lg", "help", full=True)}{btn("Huỷ", "ghost", "lg", full=True)}</div>')
        base = active_ride()
    return phone(sheet_over(base, inner, title="Gọi điện" if state != "unavail" else "Liên hệ tài xế"))


@frame("C-064", "Direct call confirmation", "Chat & gọi điện")
def c064():
    return [("Gọi tài xế / tổng đài", call_sheet()), ("Không khả dụng", call_sheet("unavail"))]


@frame("C-065", "Food customer cancel after driver ordered", "Đặt món · Theo dõi đơn")
def c065():
    return [("Cảnh báo huỷ", phone(dialog_over(food_active("at_outlet"), "Tài xế đã đặt món với quán",
                                               txt("Nếu huỷ bây giờ, bạn <b>không được hoàn lại</b> tiền món và phí giao đã chuyển (137.000đ), vì tài xế đã trả tiền cho quán.", "bmd", C["t2"])
                                               + txt("Nếu có vấn đề do tài xế hoặc quán, hãy gửi khiếu nại thay vì huỷ.", "bsm", C["t2"]),
                                               btn("Vẫn huỷ đơn", "danger", "lg", full=True) + btn("Giữ đơn", "secondary", "lg", full=True), ic="alert-triangle", tone="warning")))]


def saved_places(state="list"):
    if state == "empty":
        c = empty_state("bookmark", "Chưa có địa điểm đã lưu", "Lưu Nhà, Công ty để đặt xe và đặt món nhanh hơn.", btn("Thêm địa điểm", "secondary", "md", "plus"))
        return phone(topbar("Địa điểm đã lưu", True) + body(c, bg="#FFFFFF", extra="justify-content: center"))
    rows = (list_row("Nhà", HOME_ADDR, "home", right=ibtn("pencil", "Sửa Nhà", "ghost", 40), chevron=False)
            + list_row("Công ty", "Toà nhà Bitexco, 2 Hải Triều, Q.1", "briefcase", right=ibtn("pencil", "Sửa Công ty", "ghost", 40), chevron=False))
    rec = (list_row("ĐH Kinh tế TP.HCM", "59C Nguyễn Đình Chiểu, Q.3", "clock", right=ibtn("bookmark", "Lưu", "ghost", 40), chevron=False)
           + list_row("Chợ Bến Thành", "Lê Lợi, Bến Thành, Q.1", "clock", right=ibtn("bookmark", "Lưu", "ghost", 40), chevron=False, border=False))
    base = phone(topbar("Địa điểm đã lưu", True, right=ibtn("plus", "Thêm địa điểm", "ghost", 44)) + f'<div style="flex-grow: 1; background: #FFFFFF">{ovl("Đã lưu").replace("<div style=", "<div style=" + chr(34) + "padding: 16px 16px 4px; ", 1).replace(chr(34) + "padding: 16px 16px 4px; " + chr(34), chr(34) + "padding: 16px 16px 4px; ")}{rows}<div style="height: 12px"></div>{rec}</div>')
    if state == "list":
        return base
    inner = (f'<div style="padding: 0 16px {BOT}px; display: flex; flex-direction: column; gap: 14px">{field("Tên địa điểm", "Nhà")}{field("Địa chỉ", HOME_ADDR, ic="map-pin")}'
             f'{field("Ghi chú cho tài xế", "Hẻm 142, cổng sắt màu xanh")}{btn("Lưu", "primary", "lg", full=True)}{btn("Xoá địa điểm", "danger", "lg", "trash", full=True)}</div>')
    return phone(sheet_over(base, inner, title="Sửa địa điểm"))


@frame("C-066", "Saved places / recent addresses", "Trang chủ & tài khoản")
def c066():
    return [("Danh sách", saved_places()), ("Sửa / xoá", saved_places("edit")), ("Trống", saved_places("empty"))]


def data_req(state="request"):
    if state == "submitted":
        c = (f'<div style="display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center; padding-top: 16px">'
             f'<div style="width: 64px; height: 64px; border-radius: 999px; background: {C["ok_bg"]}; display: flex; align-items: center; justify-content: center">{icon("check", 32, C["ok"], 2.5)}</div>'
             f'{h("Đã nhận yêu cầu", "hlg")}{num("DR-240924-0012", 16, weight=600)}{txt("Onway xử lý trong tối đa 30 ngày và gửi kết quả qua email minhanh@gmail.com.", "bmd", C["t2"])}</div>')
        return phone(topbar("Dữ liệu của tôi", True) + body(c, bg="#FFFFFF") + bottom(btn("Xong", "secondary", "lg", full=True), border=False))
    if state == "restricted":
        c = (pill("paused", "Tạm hoãn xoá") + h("Chưa thể xoá tài khoản lúc này", "hlg")
             + txt("Bạn đang có khiếu nại CS-240924-0137 chưa kết luận. Theo quy định, Onway phải giữ dữ liệu liên quan cho tới khi xử lý xong.", "bmd", C["t2"])
             + card(ovl("Dữ liệu được giữ lại") + kv("Chứng từ & ảnh khiếu nại", "Đến khi kết luận") + kv("Lịch sử chuyến (nghĩa vụ kế toán)", "Theo luật") + kv("Nhật ký audit", "Theo luật"), pad=14, gap=8)
             + banner("info", "Bạn vẫn có thể tải xuống dữ liệu", "Yêu cầu xoá sẽ tự mở lại khi khiếu nại được kết luận."))
        return phone(topbar("Xoá tài khoản", True) + body(c, bg="#FFFFFF", gap=14) + bottom(btn("Tải xuống dữ liệu", "secondary", "lg", "download", full=True) + btn("Xem khiếu nại", "ghost", "lg", full=True)))
    c = (segmented(["Tải xuống dữ liệu", "Xoá tài khoản"], 0)
         + txt("Bạn sẽ nhận bản sao gồm hồ sơ, lịch sử chuyến/đơn, đánh giá và khiếu nại. Ảnh chứng từ chỉ gồm ảnh bạn đã gửi.", "bmd", C["t2"])
         + checkbox("Hồ sơ & cài đặt", True) + checkbox("Lịch sử chuyến đi và đơn món", True) + checkbox("Khiếu nại & bằng chứng của tôi", True)
         + field("Gửi đến email", "minhanh@gmail.com") + txt("Để bảo vệ bạn, Onway sẽ xác minh lại bằng OTP trước khi gửi.", "cap", C["t3"]))
    return phone(topbar("Dữ liệu của tôi", True) + body(c, bg="#FFFFFF", gap=14) + bottom(btn("Gửi yêu cầu", "primary", "lg", full=True)))


@frame("C-067", "Data export/delete request", "Trang chủ & tài khoản")
def c067():
    return [("Tạo yêu cầu", data_req()), ("Đã gửi", data_req("submitted")), ("Bị hạn chế (pháp lý/audit)", data_req("restricted"))]
