from lib import *
from reg import frame


def A(fn):
    """single-state admin frame helper"""
    return fn


def tbl_link(s):
    return f'<a href="#" style="font-weight: 600; text-decoration: none">{s}</a>'


def acts(*b):
    return row(*b, gap=8)


def map_panel(w, h_, regions, extra_top="", toolbar="", legend=True):
    lg = ""
    if legend:
        lg = (f'<div style="position: absolute; left: 16px; bottom: 16px; background: #FFFFFF; border: 1px solid {C["b2"]}; border-radius: 10px; box-shadow: {SH_MD}; padding: 10px 12px; display: flex; flex-direction: column; gap: 6px; {TY["cap"]}">'
              f'<span style="display: flex; gap: 8px; align-items: center"><span style="width: 18px; height: 0; border-top: 2px dashed #3E3D3D"></span>Đang hoạt động</span>'
              f'<span style="display: flex; gap: 8px; align-items: center"><span style="width: 18px; height: 10px; background: rgba(226,34,64,.10); border: 2px solid #E22240"></span>Đang chọn</span>'
              f'<span style="display: flex; gap: 8px; align-items: center"><span style="width: 18px; height: 10px; background: rgba(226,163,60,.14); border: 2px dashed #B87F22"></span>Tạm dừng</span>'
              f'<span style="display: flex; gap: 8px; align-items: center"><span style="width: 18px; height: 10px; background: rgba(195,24,52,.16); border: 2px dotted #C31834"></span>Không hợp lệ / chồng lấn</span></div>')
    zoom = f'<div style="position: absolute; right: 16px; bottom: 16px; display: flex; flex-direction: column; background: #FFFFFF; border: 1px solid {C["b2"]}; border-radius: 10px; box-shadow: {SH_MD}">{ibtn("zoom-in", "Phóng to", "ghost", 40)}{ibtn("zoom-out", "Thu nhỏ", "ghost", 40)}{ibtn("locate", "Về giữa", "ghost", 40)}</div>'
    return (f'<div style="position: relative; width: {w}px; height: {h_}px; border-radius: 12px; overflow: hidden; border: 1px solid {C["b2"]}; flex-shrink: 0">{map_svg(w, h_, regions=regions)}'
            f'<div style="position: absolute; top: 16px; left: 16px; right: 16px; display: flex; flex-direction: column; gap: 10px; align-items: flex-start">{toolbar}{extra_top}</div>{lg}{zoom}</div>')


REGIONS = [
    ([(0.12, 0.1), (0.46, 0.08), (0.5, 0.44), (0.16, 0.48)], "active", "Quận 1"),
    ([(0.52, 0.06), (0.84, 0.1), (0.8, 0.42), (0.54, 0.44)], "active", "Quận 3"),
    ([(0.18, 0.54), (0.5, 0.52), (0.52, 0.86), (0.2, 0.9)], "paused", "Quận 4"),
]


def toolbar(active="select"):
    items = [("pointer", "Chọn", "select", "V"), ("pentagon", "Vẽ polygon", "draw", "P"), ("pencil", "Sửa đỉnh", "edit", "E"), ("undo", "Hoàn tác", "undo", "⌘Z"), ("redo", "Làm lại", "redo", "⇧⌘Z")]
    out = ""
    for ic, lab, key, kb in items:
        on = key == active
        out += (f'<button type="button" aria-label="{lab} ({kb})" aria-pressed="{"true" if on else "false"}" style="display: inline-flex; align-items: center; gap: 6px; height: 36px; padding: 0 10px; border-radius: 8px; border: none; '
                f'background: {C["inverse"] if on else "transparent"}; color: {"#FFFFFF" if on else C["t1"]}; font-family: {FONT}; font-size: 13px; font-weight: 600">{icon(ic, 16)}{lab if key in ("select", "draw", "edit") else ""}</button>')
    return f'<div role="toolbar" aria-label="Công cụ vẽ vùng" style="display: flex; gap: 2px; padding: 4px; background: #FFFFFF; border: 1px solid {C["b2"]}; border-radius: 10px; box-shadow: {SH_MD}">{out}</div>'


def board(fn_states):
    return fn_states


# ================= AUTH / SHELL =================
def login_panel(state="default"):
    err = ""
    if state == "invalid":
        err = banner("danger", "Email hoặc mật khẩu không đúng", "Bạn còn 3 lần thử trước khi tài khoản bị khoá 30 phút.")
    if state == "locked":
        err = banner("danger", "Tài khoản tạm khoá", "Đăng nhập sai 5 lần. Thử lại sau 28 phút hoặc liên hệ Super Admin.", "lock")
    form = (f'<div style="width: 400px; display: flex; flex-direction: column; gap: 20px">{logo_img(32)}<div>{h("Đăng nhập Admin Portal", "hlg")}{txt("Chỉ dành cho nhân sự vận hành Onway.", "bsm", C["t2"], extra="margin-top: 6px")}</div>'
            f'{err}{field("Email công việc", "lan.nguyen@onway.vn")}{field("Mật khẩu", "••••••••••", error="Mật khẩu không đúng." if state == "invalid" else None)}'
            f'{btn("Đăng nhập", "disabled" if state == "locked" else "primary", "lg", full=True, href="A-001.dc.html")}{txt("Mọi phiên đăng nhập được ghi nhật ký audit.", "cap", C["t3"])}</div>')
    return (f'<div style="width: {AW}px; height: {AH}px; display: flex; font-family: {FONT}; color: {C["t1"]}; background: #FFFFFF; border: 1px solid {C["b2"]}; box-sizing: border-box">'
            f'<div style="flex: 1; display: flex; align-items: center; justify-content: center">{form}</div>'
            f'<div style="flex: 1; background: {C["inverse"]}; display: flex; flex-direction: column; justify-content: flex-end; padding: 56px; gap: 12px">{mark_img(56, True)}'
            f'<div style="{TY["dmd"]}; color: #FFFFFF; font-size: 36px; max-width: 480px">Vận hành minh bạch, mọi thao tác đều có lý do và dấu vết.</div>'
            f'<div style="{TY["bmd"]}; color: {C["tinv2"]}">Onway Ops · TP. Hồ Chí Minh</div></div></div>')


@frame("A-000", "Admin login", "Đăng nhập & khung")
def a000():
    return [("Mặc định", login_panel()), ("Sai thông tin", login_panel("invalid")), ("Bị khoá", login_panel("locked"))]


def second_factor(err=False):
    f = (f'<div style="width: 400px; display: flex; flex-direction: column; gap: 20px">{logo_img(32)}{h("Xác minh hai bước", "hlg")}'
         f'{txt("Nhập mã 6 số từ ứng dụng xác thực của bạn.", "bmd", C["t2"])}{otp_boxes("281" if not err else "281930", err, 3 if not err else None)}'
         + (f'<div style="display: flex; gap: 6px; align-items: center; {TY["bsm"]}; color: {C["err"]}">{icon("alert-circle", 16, C["err"])}Mã không đúng hoặc đã hết hạn.</div>' if err else "")
         + f'{btn("Xác minh", "primary", "lg", full=True, href="A-005.dc.html")}<a href="#" style="{TY["bsm"]}; font-weight: 600">Dùng mã dự phòng</a></div>')
    return f'<div style="width: {AW}px; height: {AH}px; display: flex; align-items: center; justify-content: center; font-family: {FONT}; color: {C["t1"]}; background: {C["page"]}; border: 1px solid {C["b2"]}; box-sizing: border-box">{card(f, pad=40)}</div>'


@frame("A-001", "OTP / second factor if enabled", "Đăng nhập & khung")
def a001():
    return [("Mặc định", second_factor()), ("Lỗi", second_factor(True))]


def dash_content(state="default"):
    if state == "loading":
        return (page_head("Tổng quan vận hành", "TP. Hồ Chí Minh · Hôm nay") + row(*[skel("100%", 104, 12, "flex: 1") for _ in range(4)], gap=16)
                + row(skel("100%", 320, 12, "flex: 2"), skel("100%", 320, 12, "flex: 1"), gap=16) + skel("100%", 200, 12))
    if state == "error":
        return page_head("Tổng quan vận hành", "TP. Hồ Chí Minh · Hôm nay") + card(empty_state("alert-circle", "Không tải được số liệu", "Dịch vụ analytics không phản hồi (mã lỗi 503). Hàng đợi vận hành vẫn hoạt động bình thường.", btn("Thử lại", "outline", "md", "refresh")), pad=40)
    if state == "empty":
        return page_head("Tổng quan vận hành", "TP. Hồ Chí Minh · Chưa ra mắt") + card(empty_state("dashboard", "Chưa có dữ liệu vận hành", "Chưa có chuyến/đơn nào. Hoàn tất các bước dưới đây để mở dịch vụ.",
                                                                                                                  col(checkbox("Tạo & xuất bản vùng hoạt động", True), checkbox("Xuất bản chính sách giá Ride/Food", True), checkbox("Duyệt ≥ 50 tài xế", False), checkbox("Xuất bản danh mục quán", False), gap=6, extra="text-align: left")), pad=40)
    kpis = row(stat("Chuyến hoàn thành", "1.284", "+8,2%", "so với hôm qua", "bike"), stat("Đơn món giao", "436", "+3,1%", "so với hôm qua", "utensils"),
               stat("Tài xế trực tuyến", "612", "", "trên 1.940 đã kích hoạt", "users"), stat("Tỷ lệ ghép thành công", "91,4%", "−1,2%", "mục tiêu ≥ 90%", "activity"), gap=16)
    return page_head("Tổng quan vận hành", "TP. Hồ Chí Minh · Hôm nay 24/09 · cập nhật 1 phút trước", acts(btn("Xuất báo cáo", "outline", "md", "download"))) + kpis + row(health_panel(), queue_panel(), gap=16, align="stretch") + audit_panel()


def health_panel(empty=False):
    bars = ""
    for i, v in enumerate([30, 42, 55, 80, 96, 88, 70, 64, 72, 90, 110, 124, 98, 76, 60, 52]):
        bars += f'<div style="flex: 1; height: {v}px; border-radius: 3px 3px 0 0; background: {C["inverse"] if i == 11 else C["b3"]}"></div>'
    inner = (row(segmented(["Đi xe", "Đặt món"], 0, False), spacer(), txt("Chuyến/giờ · hôm nay", "cap", C["t3"]))
             + f'<div style="display: flex; gap: 4px; align-items: flex-end; height: 140px; border-bottom: 1px solid {C["b2"]}">{bars}</div>'
             + row(*[col(txt(k, "cap", C["t3"]), num(v, 16, weight=600), gap=2) for k, v in [("Thời gian ghép TB", "38s"), ("Huỷ trước ghép", "4,1%"), ("Tranh chấp thanh toán", "0,6%"), ("Chờ xác nhận tiền > 5 phút", "23")]], gap=28))
    return section_card("Sức khoẻ thị trường", inner, btn("Chi tiết", "ghost", "sm", href="A-066.dc.html"), extra="flex: 2")


def queue_panel(empty=False):
    if empty:
        inner = empty_state("inbox", "Không có việc tồn", "Tất cả hàng đợi đang trong SLA.")
    else:
        q = [("lock", "Khoá tự động cần xem xét", "3", "danger", "Quá SLA: 1"), ("scale", "Khiếu nại mới", "17", "warning", "Cũ nhất 5 giờ"),
             ("banknote", "Chứng từ phí nền tảng", "8", "neutral", "SLA 4 giờ"), ("user-check", "Hồ sơ tài xế chờ duyệt", "42", "neutral", "Cũ nhất 1 ngày"),
             ("alert-triangle", "Tranh chấp thanh toán", "5", "danger", "SLA 24 giờ")]
        inner = "".join(row(icon_tile(i, 36, r=8), col(txt(t, "bsm", extra="font-weight: 600; font-size: 14px"), txt(s, "cap", C["t3"]), gap=0, extra="flex-grow: 1"),
                            num(n, 18, C["err"] if tone == "danger" else C["t1"], 700), icon("chevron-right", 16, C["t3"]), gap=12) for i, t, n, tone, s in q)
    return section_card("Hàng đợi vận hành", inner, pill("issue", "1 quá SLA", "sm") if not empty else "", extra="flex: 1")


def audit_panel(empty=False):
    if empty:
        return section_card("Hoạt động gần đây", empty_state("history", "Chưa có hoạt động", "Các thay đổi cấu hình và quyết định sẽ hiện ở đây."))
    rows = [[mono("10:42"), "Ngọc Lan (Ops Admin)", "Xuất bản cấu hình vùng", tbl_link("Quận 3 · v7"), muted("Mở rộng ranh giới phía bắc")],
            [mono("10:15"), "Minh Khoa (Risk Analyst)", "Mở khoá tài xế", tbl_link("Trần Văn Hùng"), muted("Kháng nghị hợp lệ")],
            [mono("09:58"), "Hệ thống", "Tự động khoá tạm", tbl_link("Lê Văn Tài"), muted("3 khiếu nại hợp lệ / 30 ngày")],
            [mono("09:31"), "Thu Hà (Finance Ops)", "Duyệt phí nền tảng", tbl_link("FEE-240924-0331"), muted("1.000.000đ khớp sao kê")]]
    return section_card("Hoạt động gần đây (audit)", table(["Thời gian", "Người thực hiện", "Hành động", "Đối tượng", "Lý do"], rows, ["80px", "1.3fr", "1.2fr", "1fr", "1.6fr"]).replace("border: 1px solid " + C["b2"] + "; border-radius: 12px", "border: none; border-radius: 0"),
                        btn("Xem nhật ký", "ghost", "sm", href="A-061.dc.html"), pad=0)


@frame("A-002", "Admin shell / sidebar", "Đăng nhập & khung")
def a002():
    return [("Mở rộng", admin("dash", ["Tổng quan"], dash_content())), ("Thu gọn", admin("dash", ["Tổng quan"], dash_content(), collapsed=True))]


@frame("A-003", "Permission denied", "Đăng nhập & khung")
def a003():
    return [("Không có quyền", admin("finance", ["Duyệt phí nền tảng"], card(empty_state("lock", "Bạn không có quyền truy cập trang này",
                                                                                              "Trang Duyệt phí nền tảng yêu cầu vai trò Finance Ops hoặc Super Admin. Vai trò hiện tại của bạn: Support Operator.",
                                                                                              row(btn("Yêu cầu quyền truy cập", "secondary", "md"), btn("Về Tổng quan", "ghost", "md"), gap=8)), pad=64)))]


def cmd_palette(empty=False):
    if empty:
        res = empty_state("search", "Không tìm thấy “R-00000”", "Thử mã chuyến (R-…), mã đơn (F-…), mã hồ sơ (CS-…), số điện thoại hoặc tên tài xế.")
    else:
        res = (ovl("Tài xế") + list_row("Trần Văn Hùng", "0901 234 567 · 59-X2 123.45", lead=avatar("TH", 32), right=pill("active", size="sm"), chevron=False, pad="10px 12px")
               + ovl("Chuyến & đơn") + list_row("R-7Q2K9 · Bitexco → ĐH Kinh tế", "24/09 08:27 · 48.000đ", "bike", right=pill("completed", size="sm"), chevron=False, pad="10px 12px")
               + ovl("Hồ sơ khiếu nại") + list_row("CS-240924-0137 · Thanh toán", "Khách Minh Anh · tài xế Trần Văn Hùng", "scale", right=pill("pendingReview", size="sm"), chevron=False, pad="10px 12px"))
    pal = (f'<div style="position: absolute; inset: 0; background: {C["overlay"]}; display: flex; justify-content: center; padding-top: 120px"><div role="dialog" aria-label="Tìm kiếm nhanh" style="width: 640px; height: fit-content; background: #FFFFFF; border-radius: 16px; box-shadow: {SH_LG}; overflow: hidden">'
           f'<div style="padding: 12px; border-bottom: 1px solid {C["b2"]}">{search_bar("Tìm tài xế, mã chuyến, mã case…", "R-00000" if empty else "hùng", 48, "#FFFFFF")}</div>'
           f'<div style="padding: 8px 8px 12px; display: flex; flex-direction: column; gap: 4px">{res}</div>'
           f'<div style="display: flex; gap: 16px; padding: 10px 16px; border-top: 1px solid {C["b2"]}; {TY["cap"]}; color: {C["t3"]}"><span>↑↓ di chuyển</span><span>↵ mở</span><span>Esc đóng</span></div></div></div>')
    return admin("dash", ["Tổng quan"], dash_content(), pal)


@frame("A-004", "Global search / command palette", "Đăng nhập & khung")
def a004():
    return [("Có kết quả", cmd_palette()), ("Không có kết quả", cmd_palette(True))]


# ================= DASHBOARD =================
@frame("A-005", "Dashboard overview", "Tổng quan")
def a005():
    return [("Mặc định", admin("dash", ["Tổng quan"], dash_content())), ("Đang tải", admin("dash", ["Tổng quan"], dash_content("loading"))), ("Lỗi", admin("dash", ["Tổng quan"], dash_content("error")))]


@frame("A-006", "Marketplace health widgets", "Tổng quan")
def a006():
    fraud = section_card("Cảnh báo rủi ro", "".join(row(pill(p, size="sm"), txt(t, "bsm", extra="font-size: 14px; flex-grow: 1"), num(n, 14, weight=600), gap=10) for p, t, n in [
        ("issue", "Vị trí nhảy bất thường", "4"), ("disputed", "Tranh chấp thanh toán lặp lại", "2"), ("pendingReview", "Nhiều tài khoản / 1 thiết bị", "1")]), extra="flex: 1")
    food = section_card("Food · hôm nay", row(*[col(txt(k, "cap", C["t3"]), num(v, 22, weight=600), gap=2) for k, v in [("Đơn giao", "436"), ("Có đề xuất thay đổi", "7,8%"), ("Hết giờ đề xuất", "1,1%"), ("Huỷ sau khi đặt món", "0,4%")]], gap=32), extra="flex: 2")
    return [("Ride/Food & rủi ro", admin("dash", ["Tổng quan", "Sức khoẻ thị trường"], page_head("Sức khoẻ thị trường", "Widget dùng trên Tổng quan") + row(health_panel(), fraud, gap=16, align="stretch") + row(food, gap=16)))]


@frame("A-007", "Live ops queue", "Tổng quan")
def a007():
    return [("Có việc tồn", admin("queue", ["Hàng đợi vận hành"], page_head("Hàng đợi vận hành") + row(queue_panel(), f'<div style="flex: 2"></div>', gap=16))),
            ("Không có việc", admin("queue", ["Hàng đợi vận hành"], page_head("Hàng đợi vận hành") + row(queue_panel(True), f'<div style="flex: 2"></div>', gap=16)))]


@frame("A-008", "Recent activity/audit preview", "Tổng quan")
def a008():
    return [("Danh sách", admin("dash", ["Tổng quan"], page_head("Hoạt động gần đây") + audit_panel())), ("Trống", admin("dash", ["Tổng quan"], page_head("Hoạt động gần đây") + audit_panel(True)))]


@frame("A-009", "Dashboard empty/new launch", "Tổng quan")
def a009():
    return [("Chưa có dữ liệu", admin("dash", ["Tổng quan"], dash_content("empty")))]


# ================= REGION =================
def region_rows():
    return [[tbl_link("Quận 1"), "TP. Hồ Chí Minh", "Đi xe, Đặt món", "Xe máy, Ô tô", pill("active", size="sm"), mono("v12"), muted("24/09 10:42 · Ngọc Lan")],
            [tbl_link("Quận 3"), "TP. Hồ Chí Minh", "Đi xe, Đặt món", "Xe máy, Ô tô", pill("active", size="sm"), mono("v7"), muted("24/09 10:42 · Ngọc Lan")],
            [tbl_link("Quận 4"), "TP. Hồ Chí Minh", "Đi xe", "Xe máy", pill("paused", size="sm"), mono("v3"), muted("23/09 22:00 · Quang Huy")],
            [tbl_link("Phú Nhuận"), "TP. Hồ Chí Minh", "Đi xe, Đặt món", "Xe máy", pill("inProgress", "Pilot", "sm"), mono("v2"), muted("20/09 09:12 · Ngọc Lan")],
            [tbl_link("Thủ Đức — Khu CNC"), "TP. Hồ Chí Minh", "—", "—", pill("draft", "Planned", "sm"), mono("v1"), muted("18/09 16:40 · Quang Huy")],
            [tbl_link("Quận 5 (cũ)"), "TP. Hồ Chí Minh", "—", "—", pill("cancelled", "Closed", "sm"), mono("v4"), muted("02/09 08:00 · Super Admin")]]


def region_list(state="default", overlay=""):
    head = page_head("Khu vực & polygon", "Quốc gia › Thành phố › Vùng phục vụ. Không xoá cứng polygon — chỉ tạm dừng/đóng và xuất bản phiên bản mới.",
                     acts(btn("Mở trình vẽ", "outline", "md", "map", href="A-013.dc.html"), btn("Tạo vùng", "primary", "md", "plus", href="A-012.dc.html")))
    fb = filter_bar([("TP. Hồ Chí Minh", True), ("Trạng thái", False), ("Dịch vụ", False)], "Tìm vùng")
    if state == "empty":
        return admin("region", ["Khu vực & polygon"], head + card(empty_state("map", "Chưa có vùng nào tại Hà Nội", "Tạo vùng đầu tiên và vẽ polygon để bắt đầu thử nghiệm dịch vụ.", btn("Tạo vùng", "primary", "md", "plus")), pad=48), overlay)
    return admin("region", ["Khu vực & polygon"], head + fb + table(["Vùng", "Thành phố", "Dịch vụ", "Phương tiện", "Vòng đời", "Phiên bản", "Cập nhật"], region_rows(),
                                                                   ["1.2fr", "1fr", "1fr", "1fr", "110px", "80px", "1.4fr"], selected=0 if overlay else None), overlay)


@frame("A-010", "Region list", "Khu vực & polygon")
def a010():
    return [("Active / Paused / Planned", region_list()), ("Trống", region_list("empty"))]


@frame("A-011", "Region detail drawer", "Khu vực & polygon")
def a011():
    inner = (f'<div style="height: 200px; border-radius: 12px; overflow: hidden; border: 1px solid {C["b2"]}">{map_svg(472, 200, regions=[REGIONS[0][:1] + ("selected",)], labels=False)}</div>'
             + card(kv("Thành phố", "TP. Hồ Chí Minh") + kv("Vòng đời", "Active") + kv("Dịch vụ", "Đi xe, Đặt món") + kv("Phương tiện", "Xe máy, Ô tô") + kv("Giờ hoạt động", "05:00 – 24:00")
                    + kv("Phiên bản xuất bản", "v12 · 24/09 10:42", True) + kv("Diện tích", "7,7 km²"), pad=14, gap=8)
             + txt("Nhật ký thay đổi", "lbl") + timeline([("Xuất bản v12", "Ngọc Lan · 24/09 10:42", "done", "Lý do: Mở rộng ranh giới bờ sông"), ("Tạm dừng Food 22:00–06:00", "Quang Huy · 20/09 21:55", "done"), ("Tạo vùng", "Super Admin · 01/09 08:00", "done")], True))
    return [("Xem thông tin & audit", region_list(overlay=drawer("Quận 1", inner, btn("Tạm dừng vùng", "danger", "md", "pause", href="A-020.dc.html") + btn("Sửa trên bản đồ", "secondary", "md", "map", href="A-013.dc.html"), pills=pill("active"), sub="TP. Hồ Chí Minh · REG-HCM-Q1")))]


def create_region(err=False):
    inner = (select("Quốc gia", "Việt Nam") + select("Thành phố", "TP. Hồ Chí Minh")
             + field("Tên vùng", "Quận 1" if err else "Bình Thạnh", error="Tên vùng “Quận 1” đã tồn tại trong TP. Hồ Chí Minh." if err else None)
             + field("Mã vùng", "REG-HCM-BTH", mono=True, helper="Tự sinh, dùng trong API và báo cáo.")
             + select("Vòng đời ban đầu", "Planned", helper="Vùng mới luôn bắt đầu ở Planned; xuất bản polygon trước khi chuyển Pilot/Active."))
    return region_list(overlay=admin_dialog("Tạo vùng mới", inner, btn("Huỷ", "ghost", "md") + btn("Tạo & vẽ polygon", "primary", "md", href="A-014.dc.html")))


@frame("A-012", "Create city/region", "Khu vực & polygon")
def a012():
    return [("Mặc định", create_region()), ("Lỗi trùng tên", create_region(True))]


def editor(mode="select", regions=None, top_extra="", right_panel=None, dialog="", conflict=""):
    regs = regions if regions is not None else [REGIONS[0][:2] + ("Quận 1",), REGIONS[1], REGIONS[2]]
    mp = map_panel(760, 720, regs, top_extra, toolbar(mode))
    panel = right_panel or section_card("Quận 1 · bản nháp v13", kv("Số đỉnh", "8") + kv("Diện tích", "7,9 km²") + kv("Thay đổi so với v12", "+0,2 km² phía bờ sông") + divider()
                                        + txt("Dịch vụ & phương tiện", "lbl") + checkbox("Đi xe · Xe máy", True) + checkbox("Đi xe · Ô tô", True) + checkbox("Đặt món · Xe máy", True)
                                        + divider() + select("Vòng đời", "Active") + btn("Kiểm tra chồng lấn", "outline", "md", "layers", full=True), pill("draft", size="sm"), extra="flex-grow: 1")
    content = (page_head("Trình vẽ vùng · TP. Hồ Chí Minh", "Phím tắt: V chọn · P vẽ · E sửa đỉnh · Enter đóng hình · Esc huỷ", acts(btn("Lịch sử phiên bản", "ghost", "md", "history", href="A-065.dc.html"), btn("Xuất bản", "primary", "md", "upload", href="A-019.dc.html")))
               + conflict + row(mp, f'<div style="flex-grow: 1; display: flex; flex-direction: column; gap: 16px; align-self: stretch">{panel}</div>', gap=16, align="flex-start"))
    return admin("region", ["Khu vực & polygon", "Trình vẽ"], content, dialog)


@frame("A-013", "Polygon editor map", "Khu vực & polygon")
def a013():
    sel = [REGIONS[0][:1] + ("selected", "Quận 1"), REGIONS[1], REGIONS[2]]
    loading = admin("region", ["Khu vực & polygon", "Trình vẽ"], page_head("Trình vẽ vùng · TP. Hồ Chí Minh") + row(
        f'<div style="width: 760px; height: 720px; border-radius: 12px; background: {C["m_land"]}; border: 1px solid {C["b2"]}; display: flex; align-items: center; justify-content: center; gap: 10px">{spinner(22)}{txt("Đang tải bản đồ HERE…", "bmd", C["t2"])}</div>',
        skel("100%", 400, 12, "flex-grow: 1"), gap=16, align="flex-start"))
    return [("Bản nháp", editor("select", [REGIONS[0][:2] + ("Quận 1",), REGIONS[1], REGIONS[2]])), ("Đang chọn vùng", editor("select", sel)), ("Đang tải bản đồ", loading)]


@frame("A-014", "Draw polygon", "Khu vực & polygon")
def a014():
    drawing = [([(0.56, 0.52), (0.86, 0.5), (0.9, 0.76), (0.7, 0.84)], "drawing"), REGIONS[0], REGIONS[1]]
    tip = f'<div style="background: {C["inverse"]}; color: #FFFFFF; border-radius: 8px; padding: 8px 12px; {TY["bsm"]}">Bấm để thêm đỉnh · bấm đỉnh đầu tiên hoặc Enter để đóng hình · Esc huỷ</div>'
    closed = [([(0.56, 0.52), (0.86, 0.5), (0.9, 0.76), (0.7, 0.84), (0.55, 0.72)], "selected", "Bình Thạnh"), REGIONS[0], REGIONS[1]]
    return [("Thêm điểm", editor("draw", drawing, tip)), ("Đã đóng hình", editor("select", closed, banner("success", "Đã tạo polygon 5 đỉnh", "Kiểm tra chồng lấn trước khi xuất bản.")))]


@frame("A-015", "Edit polygon vertices", "Khu vực & polygon")
def a015():
    edit = [([(0.12, 0.1), (0.46, 0.08), (0.53, 0.3), (0.5, 0.44), (0.16, 0.48)], "selected", "Quận 1"), REGIONS[1], REGIONS[2]]
    inval = [([(0.12, 0.1), (0.46, 0.08), (0.16, 0.48), (0.5, 0.44)], "invalid", "Quận 1"), REGIONS[1], REGIONS[2]]
    return [("Kéo đỉnh", editor("edit", edit, f'<div style="background: {C["inverse"]}; color: #FFFFFF; border-radius: 8px; padding: 8px 12px; {TY["bsm"]}">Kéo đỉnh để chỉnh · Alt+bấm để xoá đỉnh · ⌘Z hoàn tác</div>')),
            ("Hình không hợp lệ", editor("edit", inval, banner("danger", "Polygon tự cắt nhau", "Các cạnh không được giao nhau. Hoàn tác (⌘Z) hoặc kéo đỉnh về vị trí hợp lệ.")))]


@frame("A-016", "Polygon overlap blocked", "Khu vực & polygon")
def a016():
    ov = [([(0.4, 0.1), (0.62, 0.08), (0.66, 0.4), (0.42, 0.42)], "invalid", "Chồng lấn"), REGIONS[0], REGIONS[1], REGIONS[2]]
    return [("Chặn xuất bản", editor("select", ov, conflict=banner("danger", "Không thể xuất bản: chồng lấn với Quận 3", "Vùng Quận 1 v13 chồng 0,4 km² lên Quận 3 v7 cho cùng dịch vụ Đi xe · Xe máy. Chỉnh ranh giới hoặc tắt dịch vụ trùng ở một trong hai vùng.", action=btn("Xem vùng trùng", "outline", "sm"))))]


@frame("A-017", "Service/vehicle availability panel", "Khu vực & polygon")
def a017():
    grid = table(["Dịch vụ", "Xe máy", "Ô tô", "Giờ hoạt động"], [["Đi xe", switch(True), switch(True), mono("05:00–24:00")], ["Đặt món", switch(True), f'<span style="color: {C["t3"]}">Không áp dụng</span>', mono("06:00–22:00")]], ["1fr", "100px", "120px", "1fr"])
    inner = (grid + txt("Tạm dừng theo lịch", "lbl") + card(row(icon("calendar", 18, C["t2"]), txt("Đặt món tạm dừng hằng ngày 22:00–06:00", "bsm", extra="flex-grow: 1; font-size: 14px"), btn("Sửa", "ghost", "sm"), gap=10), pad=12)
             + banner("info", "Điểm đến ngoài vùng", "Cho phép chuyến có điểm đến ngoài polygon khi điểm đón nằm trong vùng. Khách và tài xế đều thấy cảnh báo.", action=switch(True, "Cho phép điểm đến ngoài vùng")))
    return [("Đi xe/Đặt món · Xe máy/Ô tô", region_list(overlay=drawer("Dịch vụ & phương tiện · Quận 1", inner, btn("Huỷ", "ghost", "md") + btn("Lưu vào bản nháp", "secondary", "md"), 600)))]


@frame("A-018", "Region lifecycle controls", "Khu vực & polygon")
def a018():
    stages = [("Planned", "Đang lên kế hoạch, chưa hiển thị cho người dùng", False), ("Pilot", "Mở cho nhóm tài xế/khách thử nghiệm", False), ("Active", "Mở cho mọi người dùng", True),
              ("Paused", "Tạm dừng nhận chuyến mới, chuyến đang chạy vẫn hoàn tất", False), ("Closed", "Đóng vĩnh viễn; dữ liệu và audit được giữ", False)]
    inner = "".join(radio(f'<b>{a}</b>', on, b) for a, b, on in stages) + banner("warning", "Chuyển trạng thái cần lý do", "Mọi thay đổi vòng đời được ghi audit và áp dụng khi xuất bản.")
    return [("Planned → Closed", region_list(overlay=drawer("Vòng đời · Quận 1", inner, btn("Huỷ", "ghost", "md") + btn("Lưu vào bản nháp", "secondary", "md"), 520, pills=pill("active"))))]


@frame("A-019", "Publish region config", "Khu vực & polygon")
def a019():
    inner = (card(kv("Vùng", "Quận 1") + kv("Phiên bản", "v12 → v13", True) + kv("Thay đổi", "Ranh giới +0,2 km²; Food 22:00–06:00") + kv("Ảnh hưởng", "Áp dụng cho ứng dụng trong ~1 phút"), pad=14, gap=8)
             + field("Lý do xuất bản (bắt buộc)", "Mở rộng ranh giới bờ sông theo yêu cầu Ops HCM ngày 23/09.", textarea=True) + checkbox("Đã kiểm tra không chồng lấn", True))
    return [("Xác nhận có lý do", editor(dialog=admin_dialog("Xuất bản cấu hình vùng", inner, btn("Huỷ", "ghost", "md") + btn("Xuất bản v13", "primary", "md", "upload"), ic="upload", tone="info")))]


@frame("A-020", "Pause/resume region", "Khu vực & polygon")
def a020():
    inner = (txt("Tài xế và khách trong vùng sẽ không tạo được chuyến/đơn mới. Chuyến đang chạy vẫn tiếp tục đến khi hoàn tất.", "bsm", C["t2"])
             + select("Phạm vi", "Tất cả dịch vụ") + field("Lý do (bắt buộc)", "", "VD: Mưa lớn, ngập nhiều tuyến đường", textarea=True, error="Nhập lý do để tiếp tục.")
             + select("Tự động mở lại", "Không tự mở lại"))
    return [("Bắt buộc lý do", region_list(overlay=admin_dialog("Tạm dừng vùng Quận 1?", inner, btn("Huỷ", "ghost", "md") + btn("Tạm dừng vùng", "danger", "md", "pause"), ic="pause", tone="warning")))]


@frame("A-021", "Region publish conflict", "Khu vực & polygon")
def a021():
    inner = (txt("Quang Huy đã xuất bản <b>Quận 1 v13</b> lúc 10:51 trong khi bạn đang sửa từ v12. Bản nháp của bạn chưa được áp dụng.", "bsm", C["t2"])
             + table(["", "Bản của bạn", "v13 (Quang Huy)"], [["Ranh giới", "+0,2 km² bờ sông", "Không đổi"], ["Food", "22:00–06:00 tạm dừng", "Tạm dừng 21:00–06:00"]], ["120px", "1fr", "1fr"]))
    return [("Xung đột phiên bản", editor(dialog=admin_dialog("Xung đột phiên bản", inner, btn("Huỷ bản nháp", "ghost", "md") + btn("Xem khác biệt", "outline", "md", "diff", href="A-065.dc.html") + btn("Gộp lên v13", "secondary", "md"), 620, ic="alert-triangle", tone="warning")))]


# ================= POLICY =================
def policy_list(state="default", overlay=""):
    if state == "loading":
        body_ = skel("100%", 36, 8) + skel("100%", 360, 12)
    else:
        rows = [[tbl_link("Giá Đi xe · Xe máy"), "Đi xe", "TP. Hồ Chí Minh", pill("published", size="sm"), mono("v5"), muted("20/09 · Ngọc Lan")],
                [tbl_link("Giá Đi xe · Ô tô"), "Đi xe", "TP. Hồ Chí Minh", pill("published", size="sm"), mono("v3"), muted("20/09 · Ngọc Lan")],
                [tbl_link("Phí giao Đặt món"), "Đặt món", "TP. Hồ Chí Minh", pill("draft", size="sm"), mono("v4 → v5"), muted("24/09 · Quang Huy")],
                [tbl_link("Ghép chuyến: timeout & wave"), "Matching", "Toàn quốc", pill("published", size="sm"), mono("v2"), muted("12/09 · Super Admin")],
                [tbl_link("Ngưỡng khoá tự động"), "Rủi ro", "Toàn quốc", pill("published", size="sm"), mono("v1"), muted("10/09 · Super Admin")],
                [tbl_link("Thời gian chờ đề xuất Food"), "Đặt món", "Toàn quốc", pill("published", size="sm"), mono("v1"), muted("10/09 · Super Admin")]]
        body_ = filter_bar([("Tất cả nhóm", False), ("TP. Hồ Chí Minh", True)], "Tìm chính sách") + table(["Chính sách", "Nhóm", "Phạm vi", "Trạng thái", "Phiên bản", "Cập nhật"], rows, ["1.6fr", "1fr", "1fr", "110px", "100px", "1.2fr"])
    return admin("policy", ["Giá & chính sách"], page_head("Giá & chính sách", "Guardrail giá, phí giao, ghép chuyến và ngưỡng khoá. Mọi thay đổi qua bản nháp → xuất bản có lý do.", acts(btn("Tạo bản nháp", "primary", "md", "plus"))) + body_, overlay)


@frame("A-022", "Pricing/policy config list", "Giá & chính sách")
def a022():
    return [("Bản nháp & đã xuất bản", policy_list()), ("Đang tải", policy_list("loading"))]


def policy_form(title, fields_, preview, err=None, crumb="Giá Đi xe · Xe máy"):
    left = section_card(title, fields_, pill("draft", size="sm"), extra="flex: 3")
    right = section_card("Xem trước", preview, extra="flex: 2")
    return admin("policy", ["Giá & chính sách", crumb], page_head(crumb, "Bản nháp v6 · dựa trên v5 đã xuất bản", acts(btn("Xem lịch sử", "ghost", "md", "history", href="A-028.dc.html"), btn("Huỷ bản nháp", "outline", "md"), btn("Xuất bản", "primary", "md", "upload", href="A-027.dc.html"))) + (err or "") + row(left, right, gap=16, align="flex-start"))


def two(a, b):
    return row(f'<div style="flex: 1">{a}</div>', f'<div style="flex: 1">{b}</div>', gap=12, align="flex-start")


@frame("A-023", "Ride pricing guardrails form", "Giá & chính sách")
def a023():
    def f(err):
        fields_ = (two(field("Giá mở cửa (2 km đầu)", "12.000", mono=True, right=muted("đ")), field("Giá mỗi km tiếp theo", "4.300" if not err else "43.000", mono=True, right=muted("đ"), error="Vượt guardrail tối đa 10.000đ/km." if err else None))
                   + two(field("Giá tối thiểu chuyến", "15.000", mono=True, right=muted("đ")), field("Giá tối đa chuyến", "500.000", mono=True, right=muted("đ")))
                   + two(field("Hệ số giờ cao điểm tối đa", "1,3", mono=True, right=muted("×"), helper="Giới hạn cho thuật toán Recommended Price"), field("Thời gian tài xế chờ tại điểm đón", "5", mono=True, right=muted("phút"), helper="Không thu phí chờ cho Đi xe trong P0"))
                   + switch(True, "Cho phép điểm đến ngoài vùng", "Giá tính theo quãng đường thực tế, không phụ thu"))
        pv = (kv("Chuyến mẫu 3,2 km · 14 phút", "") + price_row("Giá mở cửa", "12.000đ") + price_row("1,2 km × 4.300đ", "5.160đ") + price_row("Làm tròn / tối thiểu", "→ 15.000đ")
              + divider() + price_row("Giá hiển thị", "18.000đ", True) + txt("Giá cuối cùng tài xế thấy; không có thương lượng trong P0.", "cap", C["t3"]))
        return policy_form("Guardrail giá Đi xe · Xe máy", fields_, pv, banner("danger", "Có 1 lỗi cần sửa trước khi xuất bản", "") if err else None)
    return [("Mặc định", f(False)), ("Lỗi guardrail", f(True))]


@frame("A-024", "Food delivery fee policy form", "Giá & chính sách")
def a024():
    def f(err):
        fields_ = (two(field("Phí giao cơ bản (3 km)", "15.000", mono=True, right=muted("đ")), field("Mỗi km tiếp theo", "3.500", mono=True, right=muted("đ")))
                   + two(field("Phí giao tối thiểu", "15.000", mono=True, right=muted("đ")), field("Phí giao tối đa", "10.000" if err else "60.000", mono=True, right=muted("đ"), error="Tối đa phải lớn hơn tối thiểu (15.000đ)." if err else None))
                   + ovl("Phí chờ tại quán (theo brand)") + two(field("Miễn phí chờ", "10", mono=True, right=muted("phút")), field("Sau đó", "1.000", mono=True, right=muted("đ/phút"))) + field("Trần phí chờ", "15.000", mono=True, right=muted("đ")))
        pv = kv("Đơn mẫu 3,4 km", "") + price_row("Phí cơ bản", "15.000đ") + price_row("0,4 km × 3.500đ", "1.400đ") + divider() + price_row("Phí giao đề xuất", "16.400đ → 17.000đ", True) + txt("Khách chỉ đồng ý hoặc không đặt; không thương lượng.", "cap", C["t3"])
        return policy_form("Phí giao Đặt món", fields_, pv, banner("danger", "Có 1 lỗi cần sửa", "") if err else None, "Phí giao Đặt món")
    return [("Mặc định", f(False)), ("Lỗi", f(True))]


@frame("A-025", "Matching timeout/wave policy form", "Giá & chính sách")
def a025():
    def f(err):
        waves = table(["Wave", "Bán kính", "Số tài xế", "Thời gian chờ"], [[mono("1"), mono("1,5 km"), mono("3"), mono("15s")], [mono("2"), mono("3 km"), mono("5"), mono("15s")], [mono("3"), mono("5 km" if not err else "2 km"), mono("8"), mono("20s")]], ["60px", "1fr", "1fr", "1fr"])
        fields_ = (field("Tổng thời gian tìm tối đa", "120", mono=True, right=muted("giây")) + txt("Các wave", "lbl") + waves
                   + (f'<div style="display: flex; gap: 6px; align-items: center; {TY["bsm"]}; color: {C["err"]}">{icon("alert-circle", 14, C["err"])}Bán kính wave 3 phải lớn hơn wave 2.</div>' if err else "")
                   + field("Thời gian tài xế phản hồi offer", "15", mono=True, right=muted("giây")) + txt("Quy tắc: tài xế nhận hợp lệ đầu tiên được chuyến.", "cap", C["t3"]))
        pv = timeline([("Wave 1 · 0–15s", "3 tài xế gần nhất trong 1,5 km", "done"), ("Wave 2 · 15–30s", "5 tài xế trong 3 km", "done"), ("Wave 3 · 30–50s", "8 tài xế trong 5 km", "current"), ("Hết 120s → Không tìm được tài xế", "", "todo")], True)
        return policy_form("Ghép chuyến: timeout & wave", fields_, pv, None, "Ghép chuyến")
    return [("Mặc định", f(False)), ("Lỗi", f(True))]


@frame("A-026", "Auto-lock/fraud threshold policy", "Giá & chính sách")
def a026():
    def f(err):
        fields_ = (switch(True, "Khoá tạm khi có tín hiệu an toàn/gian lận nghiêm trọng", "Khoá ngay, xem xét trong 24 giờ")
                   + two(field("Số khiếu nại hợp lệ", "3", mono=True), field("Trong khoảng", "30" if not err else "0", mono=True, right=muted("ngày"), error="Phải từ 1 đến 90 ngày." if err else None))
                   + two(field("Tranh chấp thanh toán lặp lại", "2", mono=True), field("Trong khoảng", "14", mono=True, right=muted("ngày")))
                   + switch(True, "Khoá khi khách đã trả tiền nhưng tài xế không đến (paid/no-show)", "Sau khi hồ sơ được xác nhận hợp lệ")
                   + field("SLA xem xét", "24", mono=True, right=muted("giờ"))
                   + banner("warning", "Khoá tự động không phải kết luận vi phạm", "Mọi lần khoá tạo hồ sơ xem xét, có lý do và audit. Chỉ Super Admin/Risk Analyst được mở khoá."))
        pv = txt("30 ngày qua, cấu hình này sẽ khoá:", "bsm", C["t2"]) + num("7 tài xế", 24, weight=700) + txt("(hiện tại v1: 5 tài xế)", "cap", C["t3"])
        return policy_form("Ngưỡng khoá tự động", fields_, pv, None, "Ngưỡng khoá tự động")
    return [("Mặc định", f(False)), ("Lỗi", f(True))]


@frame("A-027", "Policy publish confirmation", "Giá & chính sách")
def a027():
    inner = (table(["Tham số", "v5 (hiện tại)", "v6 (bản nháp)"], [["Giá mỗi km", mono("4.000đ"), mono("4.300đ")], ["Hệ số cao điểm tối đa", mono("1,2×"), mono("1,3×")]], ["1.4fr", "1fr", "1fr"])
             + field("Lý do (bắt buộc)", "Điều chỉnh theo giá xăng tăng 7% từ 21/09.", textarea=True) + select("Hiệu lực", "Ngay sau khi xuất bản"))
    return [("Xác nhận có lý do", policy_list(overlay=admin_dialog("Xuất bản Giá Đi xe · Xe máy v6", inner, btn("Huỷ", "ghost", "md") + btn("Xuất bản", "primary", "md", "upload"), 600, ic="upload", tone="info")))]


@frame("A-028", "Policy audit timeline", "Giá & chính sách")
def a028():
    inner = timeline([("v6 · bản nháp", "Quang Huy · 24/09 09:12", "current", "Giá mỗi km 4.000 → 4.300đ"), ("v5 · xuất bản", "Ngọc Lan · 20/09 14:00", "done", "Lý do: Mở rộng Quận 3. Tối thiểu 14.000 → 15.000đ"),
                      ("v4 · xuất bản", "Super Admin · 12/09 08:00", "done", "Lý do: Cấu hình ra mắt"), ("v3 · bị huỷ", "Quang Huy · 11/09 17:40", "failed", "Không xuất bản")])
    return [("Người/thời gian/khác biệt", policy_list(overlay=drawer("Lịch sử · Giá Đi xe · Xe máy", inner, btn("So sánh phiên bản", "outline", "md", "diff", href="A-065.dc.html"))))]


# ================= DRIVERS =================
def driver_rows():
    return [[row(avatar("TH", 28), tbl_link("Trần Văn Hùng")), mono("0901 234 567"), "Xe máy · Ride, Food", pill("active", size="sm"), pill("active", "Phí đến 03/2028", "sm"), mono("4,9"), muted("24/09 09:40")],
            [row(avatar("LB", 28), tbl_link("Lê Quốc Bảo")), mono("0938 111 222"), "Xe máy · Ride, Food", pill("active", size="sm"), pill("active", "Phí đến 02/2028", "sm"), mono("4,8"), muted("23/09 18:02")],
            [row(avatar("NT", 28), tbl_link("Nguyễn Thị Thu")), mono("0977 555 010"), "Xe máy · Ride", pill("pendingReview", size="sm"), pill("unpaid", size="sm"), mono("—"), muted("24/09 08:11")],
            [row(avatar("LT", 28), tbl_link("Lê Văn Tài")), mono("0909 876 543"), "Ô tô · Ride", pill("locked", "Khoá tự động", "sm"), pill("active", "Phí đến 01/2028", "sm"), mono("4,2"), muted("24/09 09:58")],
            [row(avatar("PM", 28), tbl_link("Phạm Minh")), mono("0912 000 333"), "Xe máy · Food", pill("rejected", size="sm"), pill("unpaid", size="sm"), mono("—"), muted("22/09 14:20")],
            [row(avatar("VK", 28), tbl_link("Võ Khánh")), mono("0966 432 100"), "Xe máy · Ride, Food", pill("appeal", size="sm"), pill("active", "Phí đến 12/2027", "sm"), mono("4,6"), muted("21/09 10:05")]]


def driver_list(filtered=None, overlay="", sel=None):
    rows = driver_rows()
    chips = [("Tất cả trạng thái", False), ("Dịch vụ", False), ("Phí nền tảng", False)]
    if filtered == "pending":
        rows = [rows[2]]
        chips = [("Chờ duyệt", True), ("Dịch vụ", False), ("Phí nền tảng", False)]
    if filtered == "locked":
        rows = [rows[3], rows[5]]
        chips = [("Đã khoá / kháng nghị", True), ("Dịch vụ", False)]
    tb = row(*[tag(t, i == 0) for i, t in enumerate(["Tất cả 1.982", "Chờ duyệt 42", "Đang hoạt động 1.940", "Đã khoá 6", "Bị từ chối 18"])], gap=8)
    return admin("driver", ["Tài xế"], page_head("Tài xế", "Duyệt hồ sơ, eligibility dịch vụ, khoá/mở khoá.", acts(btn("Xuất CSV", "outline", "md", "download")))
                 + tb + filter_bar(chips, "Tên, SĐT, biển số") + table(["Tài xế", "SĐT", "Phương tiện · dịch vụ", "Trạng thái", "Phí nền tảng", "Đánh giá", "Cập nhật"], rows, ["1.4fr", "1fr", "1.3fr", "130px", "150px", "70px", "100px"], selected=sel, checkbox_col=True), overlay)


@frame("A-029", "Driver list", "Tài xế · Duyệt & quản lý")
def a029():
    return [("Tất cả", driver_list()), ("Lọc chờ duyệt", driver_list("pending")), ("Lọc đã khoá", driver_list("locked"))]


def driver_drawer_inner(tab=0):
    docs = "".join(row(icon_tile("file", 36, r=8), col(txt(t, "bsm", extra="font-weight: 600; font-size: 14px"), txt(s, "cap", C["t3"]), gap=0, extra="flex-grow: 1"), pill(p, size="sm"), btn("Xem", "ghost", "sm", href="A-031.dc.html"), gap=10)
                   for t, s, p in [("CCCD 2 mặt", "Tải lên 24/09 08:02", "pendingReview"), ("Ảnh chân dung cầm CCCD", "Tải lên 24/09 08:03", "pendingReview"),
                                   ("Giấy phép lái xe A1", "Hết hạn 2032", "approved"), ("Đăng ký xe", "59-X1 222.33", "pendingReview"), ("Bảo hiểm TNDS", "Hết hạn 04/2027", "approved")])
    return (row(avatar("NT", 56), col(txt("Nguyễn Thị Thu", "hsm"), mono("0977 555 010 · DRV-000812"), gap=4), gap=14)
            + tabs(["Hồ sơ", "Giấy tờ", "Dịch vụ", "Rủi ro", "Audit"], tab)
            + card(kv("Phương tiện", "Honda Wave · 59-X1 222.33") + kv("Dịch vụ đăng ký", "Đi xe") + kv("Thành phố", "TP. Hồ Chí Minh") + kv("Tài khoản nhận tiền", "ACB ••• 8812 · NGUYEN THI THU") + kv("Nộp hồ sơ", "24/09 08:11"), pad=14, gap=8)
            + txt("Giấy tờ (2/5 đã duyệt)", "lbl") + docs)


@frame("A-030", "Driver detail drawer", "Tài xế · Duyệt & quản lý")
def a030():
    return [("Hồ sơ, dịch vụ, giấy tờ", driver_list("pending", drawer("Hồ sơ tài xế", driver_drawer_inner(), btn("Từ chối", "danger", "md", href="A-032.dc.html") + btn("Duyệt hồ sơ", "primary", "md", "check", href="A-032.dc.html"), 560, pills=pill("pendingReview")), 0))]


def doc_viewer(state="image"):
    img = (f'<div role="img" aria-label="Ảnh CCCD mặt trước" style="flex-grow: 1; height: 100%; border-radius: 12px; background: #2F2E2E; display: flex; align-items: center; justify-content: center; color: #A3A2A0; flex-direction: column; gap: 8px">{icon("id-card", 64)}<span style="{TY["bsm"]}">CCCD mặt trước · 1/5</span></div>'
           if state == "image" else f'<div style="flex-grow: 1; height: 100%; border-radius: 12px; background: #FFFFFF; border: 1px solid {C["b2"]}; display: flex; flex-direction: column; padding: 32px; gap: 10px">{icon("file", 32)}{txt("Đăng ký xe — PDF trang 1/2", "hsm")}{"".join(skel("100%", 12) for _ in range(10))}</div>')
    side = (col(txt("Đối chiếu", "lbl") + kv("Họ tên", "NGUYỄN THỊ THU") + kv("Số CCCD", "079 190 •••• 21", True) + kv("Ngày sinh", "02/08/1995") + kv("Khớp ảnh chân dung", "Cần kiểm tra thủ công")
                + divider() + checkbox("Thông tin khớp hồ sơ", True) + checkbox("Ảnh rõ, không chỉnh sửa", True) + checkbox("Còn hiệu lực", False)
                + field("Ghi chú nội bộ", "", "Chỉ Driver Ops xem"), gap=10, extra="width: 320px; flex-shrink: 0"))
    modal = (f'<div style="position: absolute; inset: 0; background: {C["overlay"]}; display: flex; align-items: center; justify-content: center"><div role="dialog" aria-modal="true" style="width: 1180px; height: 760px; background: {C["page"]}; border-radius: 16px; box-shadow: {SH_LG}; display: flex; flex-direction: column; overflow: hidden">'
             f'<div style="display: flex; align-items: center; gap: 12px; padding: 14px 20px; background: #FFFFFF; border-bottom: 1px solid {C["b2"]}">{txt("Giấy tờ · Nguyễn Thị Thu", "hsm", extra="flex-grow: 1")}'
             f'{segmented(["CCCD trước", "CCCD sau", "Chân dung", "GPLX", "Đăng ký xe"], 0 if state == "image" else 4, False)}{ibtn("zoom-in", "Phóng to", "ghost", 36)}{ibtn("x", "Đóng", "ghost", 36)}</div>'
             f'<div style="flex-grow: 1; display: flex; gap: 20px; padding: 20px; min-height: 0">{img}{side}</div>'
             f'<div style="display: flex; gap: 8px; justify-content: flex-end; padding: 14px 20px; background: #FFFFFF; border-top: 1px solid {C["b2"]}">{txt("Ảnh riêng tư · liên kết tạm 10 phút · lượt xem được ghi audit", "cap", C["t3"], extra="flex-grow: 1; align-self: center")}'
             f'{btn("Từ chối giấy tờ", "danger", "md")}{btn("Duyệt giấy tờ", "secondary", "md", "check")}</div></div></div>')
    return driver_list("pending", modal, 0)


@frame("A-031", "KYC/document viewer", "Tài xế · Duyệt & quản lý")
def a031():
    return [("Ảnh", doc_viewer()), ("PDF", doc_viewer("pdf"))]


@frame("A-032", "Driver approval/rejection", "Tài xế · Duyệt & quản lý")
def a032():
    rej = (txt("Tài xế sẽ thấy lý do và nộp lại giấy tờ bị từ chối.", "bsm", C["t2"]) + select("Giấy tờ bị từ chối", "Đăng ký xe")
           + select("Lý do", "Biển số không khớp") + field("Ghi chú cho tài xế (bắt buộc)", "Biển số trên cà vẹt là 59-X1 222.38, khác biển số bạn khai.", textarea=True))
    app = (txt("Hồ sơ đạt yêu cầu. Tài xế cần thanh toán phí nền tảng trước khi được kích hoạt.", "bsm", C["t2"]) + checkbox("Đi xe · Xe máy", True) + checkbox("Đặt món · Xe máy", False, "Tài xế không đăng ký")
           + field("Lý do (bắt buộc)", "Đủ 5/5 giấy tờ hợp lệ.", textarea=True))
    return [("Từ chối có lý do", driver_list("pending", admin_dialog("Từ chối hồ sơ?", rej, btn("Huỷ", "ghost", "md") + btn("Từ chối", "danger", "md"), ic="x-circle", tone="danger"))),
            ("Duyệt có lý do", driver_list("pending", admin_dialog("Duyệt hồ sơ Nguyễn Thị Thu", app, btn("Huỷ", "ghost", "md") + btn("Duyệt hồ sơ", "primary", "md", "check"), ic="check-circle", tone="success")))]


def fee_proof_inner():
    return (row(photo(220, 300, "Ảnh chuyển khoản · 1.000.000đ", "image", 12), col(kv("Tài xế", "Trần Văn Hùng") + kv("Số tiền kỳ vọng", "1.000.000đ", True) + kv("Nội dung", "ONWFEE 0901234567", True)
                                                                                  + kv("Mã GD tài xế nhập", "FT24268093415", True) + kv("Gửi lúc", "24/09 10:32") + divider()
                                                                                  + checkbox("Đã đối chiếu sao kê Techcombank", True) + checkbox("Số tiền & nội dung khớp", True), gap=10, extra="flex-grow: 1"), gap=16, align="flex-start")
            + field("Ghi chú / lý do (bắt buộc khi từ chối)", "", "VD: Không tìm thấy giao dịch trên sao kê", textarea=True))


@frame("A-033", "Platform fee proof review", "Tài xế · Duyệt & quản lý")
def a033():
    return [("Duyệt/từ chối", driver_list(overlay=drawer("Chứng từ phí nền tảng", fee_proof_inner(), btn("Từ chối", "danger", "md") + btn("Xác nhận đã nhận", "primary", "md", "check"), 600, pills=pill("proofPending"), sub="FEE-240924-0331"), sel=0))]


@frame("A-034", "Driver service eligibility editor", "Tài xế · Duyệt & quản lý")
def a034():
    inner = (table(["Dịch vụ", "Xe máy", "Ô tô", "Điều kiện"], [["Đi xe", switch(True), switch(False), muted("GPLX A1 · Bảo hiểm")], ["Đặt món", switch(True), muted("—"), muted("GPLX A1")]], ["1fr", "90px", "90px", "1.4fr"])
             + banner("info", "Ô tô chưa đủ điều kiện", "Thiếu GPLX hạng B và đăng ký xe ô tô.") + field("Lý do thay đổi (bắt buộc)", "", "VD: Bổ sung dịch vụ Food theo yêu cầu tài xế", textarea=True))
    return [("Cờ dịch vụ/phương tiện", driver_list(overlay=drawer("Eligibility · Trần Văn Hùng", inner, btn("Huỷ", "ghost", "md") + btn("Lưu thay đổi", "secondary", "md"), 600), sel=0))]


@frame("A-035", "Manual lock driver", "Tài xế · Khoá & kháng nghị")
def a035():
    inner = (txt("Tài xế sẽ bị ngắt trực tuyến ngay. Chuyến đang chạy vẫn được hoàn tất.", "bsm", C["t2"]) + select("Loại khoá", "Tạm khoá chờ xem xét")
             + select("Lý do cho tài xế", "Vấn đề an toàn đang điều tra") + field("Ghi chú nội bộ (bắt buộc)", "", "Không hiển thị cho tài xế", textarea=True, error="Nhập ghi chú để tiếp tục.")
             + select("Liên kết hồ sơ", "CS-240924-0137"))
    return [("Bắt buộc lý do", driver_list(overlay=admin_dialog("Khoá tài xế Trần Văn Hùng?", inner, btn("Huỷ", "ghost", "md") + btn("Khoá tài xế", "danger", "md", "lock"), 560, ic="lock", tone="danger"), sel=0))]


def autolock_queue(overlay=""):
    rows = [[row(avatar("LT", 28), tbl_link("Lê Văn Tài")), "3 khiếu nại hợp lệ / 30 ngày", pill("issue", "Cao", "sm"), mono("24/09 09:58"), f'<span style="color: {C["err"]}; font-weight: 600; font-family: {MONO}">Quá SLA 2h</span>', pill("pendingReview", size="sm"), "—"],
            [row(avatar("VK", 28), tbl_link("Võ Khánh")), "Tranh chấp thanh toán lặp lại", pill("paused", "Trung bình", "sm"), mono("23/09 21:40"), mono("còn 9h"), pill("appeal", size="sm"), "Minh Khoa"],
            [row(avatar("DQ", 28), tbl_link("Đỗ Quân")), "Tín hiệu an toàn nghiêm trọng", pill("issue", "Nghiêm trọng", "sm"), mono("24/09 11:05"), mono("còn 23h"), pill("pendingReview", size="sm"), "—"]]
    return admin("autolock", ["Khoá tự động"], page_head("Hàng đợi khoá tự động", "SLA xem xét 24 giờ. Khoá tự động không phải kết luận vi phạm.", acts(btn("Cấu hình ngưỡng", "outline", "md", "sliders", href="A-026.dc.html")))
                 + row(stat("Đang chờ", "3"), stat("Quá SLA", "1", "", "", "alert-triangle"), stat("Mở khoá 7 ngày qua", "4"), stat("Giữ khoá 7 ngày qua", "2"), gap=16)
                 + table(["Tài xế", "Lý do (reason code)", "Mức độ", "Khoá lúc", "SLA", "Trạng thái", "Người xử lý"], rows, ["1.2fr", "1.6fr", "110px", "110px", "100px", "130px", "1fr"], selected=1 if overlay else None), overlay)


@frame("A-036", "Auto-lock review queue", "Tài xế · Khoá & kháng nghị")
def a036():
    return [("SLA, lý do, mức độ", autolock_queue())]


@frame("A-037", "Driver appeal detail", "Tài xế · Khoá & kháng nghị")
def a037():
    inner = (card(kv("Hồ sơ khoá", "RK-240923-0005", True) + kv("Reason code", "PAYMENT_DISPUTE_REPEAT") + kv("Khoá lúc", "23/09 21:40 · Hệ thống"), pad=14, gap=8)
             + txt("Nội dung kháng nghị", "lbl") + card(txt("“Hai lần tranh chấp đều do khách chuyển nhầm tài khoản cũ của tôi, tôi đã cập nhật tài khoản mới ngày 19/09. Gửi kèm sao kê.”", "bmd"), pad=14, bg=C["ink25"])
             + txt("Bằng chứng (2)", "lbl") + row(photo(140, 100, "Sao kê", "file", 8), photo(140, 100, "Ảnh chat", "image", 8), gap=8)
             + txt("Hồ sơ liên quan", "lbl") + list_row("CS-240920-0077 · Tranh chấp thanh toán", "Kết luận: khách chuyển nhầm", "scale", pad="10px 0") + list_row("CS-240922-0098 · Tranh chấp thanh toán", "Đang xem xét", "scale", pad="10px 0", border=False))
    return [("Nội dung & bằng chứng", autolock_queue(drawer("Kháng nghị · Võ Khánh", inner, btn("Giữ khoá", "danger", "md") + btn("Chấp nhận & mở khoá", "primary", "md", "unlock", href="A-038.dc.html"), 600, pills=pill("appeal"))))]


@frame("A-038", "Unlock driver", "Tài xế · Khoá & kháng nghị")
def a038():
    ok = (card(kv("Tài xế", "Võ Khánh") + kv("Vai trò của bạn", "Risk/Fraud Analyst ✓ có quyền mở khoá"), pad=12, gap=6) + field("Lý do mở khoá (bắt buộc)", "Kháng nghị hợp lệ: 2 tranh chấp do khách chuyển nhầm tài khoản cũ.", textarea=True)
          + checkbox("Gửi thông báo cho tài xế", True))
    deny = banner("danger", "Vai trò của bạn không được mở khoá", "Driver Ops chỉ được đề xuất mở khoá. Gửi đề xuất để Risk/Fraud Analyst hoặc Super Admin quyết định.") + field("Đề xuất (bắt buộc)", "", "Lý do đề xuất mở khoá", textarea=True)
    return [("Có quyền", autolock_queue(admin_dialog("Mở khoá tài xế?", ok, btn("Huỷ", "ghost", "md") + btn("Mở khoá", "primary", "md", "unlock"), ic="unlock", tone="success"))),
            ("Không đủ quyền", autolock_queue(admin_dialog("Mở khoá tài xế?", deny, btn("Huỷ", "ghost", "md") + btn("Gửi đề xuất", "secondary", "md"), ic="lock", tone="danger")))]


@frame("A-039", "Driver audit timeline", "Tài xế · Khoá & kháng nghị")
def a039():
    inner = timeline([("Mở khoá", "Minh Khoa (Risk) · 24/09 10:15", "done", "Lý do: Kháng nghị hợp lệ"), ("Gửi kháng nghị", "Tài xế · 23/09 22:10", "done"),
                      ("Khoá tự động", "Hệ thống · 23/09 21:40", "failed", "PAYMENT_DISPUTE_REPEAT · 2 tranh chấp / 14 ngày"), ("Kích hoạt", "Thu Hà (Finance) · 12/09 16:00", "done", "Phí nền tảng FEE-240912-0110"),
                      ("Duyệt hồ sơ", "Quang Huy (Driver Ops) · 11/09 14:20", "done"), ("Đăng ký", "Tài xế · 10/09 19:02", "done")])
    return [("Người/thời gian/hành động", driver_list(overlay=drawer("Audit · Võ Khánh", inner, btn("Xuất nhật ký", "outline", "md", "download"), 520), sel=5))]


# ================= CATALOG =================
def brand_list(state="default", overlay=""):
    if state == "empty":
        body_ = card(empty_state("store", "Chưa có brand nào", "Thêm brand và thực đơn chuẩn trước khi mở dịch vụ Đặt món.", btn("Thêm brand", "primary", "md", "plus")), pad=48)
    else:
        rows = [[row(food_img(28, 28, 0, 6), tbl_link("Cơm Tấm Sà Bì")), mono("12"), mono("24"), pill("published", size="sm"), muted("Có 1 xung đột"), muted("24/09 · Thanh Tâm")],
                [row(food_img(28, 28, 5, 6), tbl_link("Phở Gánh 1975")), mono("6"), mono("18"), pill("published", size="sm"), muted("—"), muted("22/09 · Thanh Tâm")],
                [row(food_img(28, 28, 4, 6), tbl_link("Trà Sữa Mây")), mono("9"), mono("32"), pill("draft", size="sm"), muted("Thiếu giá 3 món"), muted("24/09 · Thanh Tâm")],
                [row(food_img(28, 28, 1, 6), tbl_link("Bánh Mì Cô Ba")), mono("4"), mono("8"), pill("cancelled", "Ngưng", "sm"), muted("—"), muted("10/09 · Super Admin")]]
        if state == "search":
            rows = rows[:1]
        body_ = filter_bar([("Tất cả trạng thái", False), ("TP. Hồ Chí Minh", True)], "Tìm brand" if state != "search" else "Tìm brand") + table(["Brand", "Outlet", "Món chuẩn", "Trạng thái", "Cảnh báo", "Cập nhật"], rows, ["1.6fr", "80px", "100px", "120px", "1.2fr", "1.2fr"])
    tb = tabs(["Brand", "Outlet", "Món", "Xung đột (3)"], 0)
    return admin("catalog", ["Danh mục món", "Brand"], page_head("Danh mục món", "Brand → thực đơn chuẩn → outlet override. Tài xế không sửa danh mục trong P0.", acts(btn("Nhập danh mục", "outline", "md", "upload", href="A-048.dc.html"), btn("Thêm brand", "primary", "md", "plus"))) + tb + body_, overlay)


@frame("A-040", "Food brand list", "Danh mục món")
def a040():
    return [("Danh sách", brand_list()), ("Tìm kiếm", brand_list("search")), ("Trống", brand_list("empty"))]


@frame("A-041", "Brand detail/editor", "Danh mục món")
def a041():
    def ed(st):
        inner = (row(food_img(64, 64, 0, 12), col(field("Tên brand", "Cơm Tấm Sà Bì"), gap=0, extra="flex-grow: 1"), gap=14, align="flex-end")
                 + select("Danh mục", "Cơm") + field("Mô tả", "Cơm tấm sườn nướng than, 12 chi nhánh tại TP.HCM.", textarea=True)
                 + ovl("Phí chờ theo brand") + two(field("Miễn phí chờ", "10", mono=True, right=muted("phút")), field("Sau đó", "1.000", mono=True, right=muted("đ/phút")))
                 + txt("Thực đơn chuẩn: 24 món · 3 nhóm", "lbl") + btn("Mở thực đơn chuẩn", "outline", "md", "list", href="A-044.dc.html"))
        return brand_list(overlay=drawer("Cơm Tấm Sà Bì", inner, btn("Lưu nháp", "outline", "md") + btn("Xuất bản", "primary", "md", "upload", href="A-049.dc.html"), 560, pills=pill(st, size="sm")))
    return [("Bản nháp", ed("draft")), ("Đã xuất bản", ed("published"))]


def outlet_list(overlay=""):
    rows = [[tbl_link("Sà Bì — Nguyễn Trãi"), "212 Nguyễn Trãi, Q.1", "Quận 1", mono("06:00–21:00"), pill("active", "Đang mở", "sm"), muted("—")],
            [tbl_link("Sà Bì — Võ Văn Tần"), "88 Võ Văn Tần, Q.3", "Quận 3", mono("06:00–21:00"), pill("active", "Đang mở", "sm"), muted("2 override giá")],
            [tbl_link("Sà Bì — Hoàng Diệu"), "31 Hoàng Diệu, Q.4", "Quận 4", mono("06:00–20:00"), pill("paused", "Vùng tạm dừng", "sm"), muted("—")],
            [tbl_link("Sà Bì — Phan Xích Long"), "—", "—", mono("—"), pill("issue", "Thiếu dữ liệu", "sm"), muted("Thiếu địa chỉ, giờ mở")],
            [tbl_link("Sà Bì — Lê Văn Sỹ"), "150 Lê Văn Sỹ, Phú Nhuận", "Phú Nhuận", mono("06:00–21:00"), pill("cancelled", "Đóng cửa", "sm"), muted("Đóng từ 15/09")]]
    return admin("catalog", ["Danh mục món", "Outlet"], page_head("Outlet · Cơm Tấm Sà Bì", "12 outlet", acts(btn("Thêm outlet", "primary", "md", "plus")))
                 + tabs(["Brand", "Outlet", "Món", "Xung đột (3)"], 1) + filter_bar([("Cơm Tấm Sà Bì", True), ("Vùng", False), ("Trạng thái", False)], "Tìm outlet")
                 + table(["Outlet", "Địa chỉ", "Vùng", "Giờ mở", "Trạng thái", "Ghi chú"], rows, ["1.4fr", "1.6fr", "1fr", "120px", "140px", "1.2fr"], selected=0 if overlay else None), overlay)


@frame("A-042", "Outlet list", "Danh mục món")
def a042():
    return [("Đóng / mở / thiếu dữ liệu", outlet_list())]


@frame("A-043", "Outlet detail/editor", "Danh mục món")
def a043():
    inner = (field("Tên outlet", "Sà Bì — Nguyễn Trãi") + field("Địa chỉ", "212 Nguyễn Trãi, Phường Nguyễn Cư Trinh, Quận 1", ic="map-pin")
             + f'<div style="height: 160px; border-radius: 12px; overflow: hidden; border: 1px solid {C["b2"]}">{map_svg(512, 160, pins=[("outlet", 0.4, 0.5)], regions=[([(0.1, 0.1), (0.7, 0.08), (0.75, 0.9), (0.12, 0.92)], "active")], labels=False)}</div>'
             + banner("success", "Nằm trong vùng Quận 1 (Active)", "") + ovl("Giờ mở cửa")
             + "".join(row(txt(d, "bsm", extra="width: 90px; font-size: 14px"), mono(t), spacer(), switch(True), gap=10) for d, t in [("Thứ 2–6", "06:00 – 21:00"), ("Thứ 7–CN", "06:00 – 22:00")]))
    return [("Giờ, địa chỉ, vùng", outlet_list(drawer("Sà Bì — Nguyễn Trãi", inner, btn("Lưu nháp", "secondary", "md"), 560, pills=pill("active", "Đang mở", "sm"))))]


def item_list(overlay=""):
    rows = [[row(food_img(28, 28, 0, 6), tbl_link("Cơm tấm sườn bì chả")), "Cơm tấm", mono("55.000đ"), mono("2"), pill("published", size="sm"), muted("—")],
            [row(food_img(28, 28, 0, 6), tbl_link("Cơm tấm sườn nướng")), "Cơm tấm", mono("45.000đ"), mono("0"), pill("published", size="sm"), muted("—")],
            [row(food_img(28, 28, 5, 6), tbl_link("Cơm tấm sườn trứng ốp la")), "Cơm tấm", f'<span style="color: {C["err"]}; font-weight: 600">Thiếu giá</span>', mono("0"), pill("draft", size="sm"), pill("issue", "Thiếu giá", "sm")],
            [row(food_img(28, 28, 3, 6), tbl_link("Trà đá")), "Đồ uống", mono("5.000đ"), mono("0"), pill("published", size="sm"), muted("—")],
            [row(food_img(28, 28, 2, 6), tbl_link("Chả trứng thêm")), "Món thêm", mono("12.000đ"), mono("1"), pill("published", size="sm"), pill("changeRequested", "Xung đột", "sm")]]
    return admin("catalog", ["Danh mục món", "Món"], page_head("Thực đơn chuẩn · Cơm Tấm Sà Bì", "Giá chuẩn của brand; outlet có thể override giá/trạng thái.", acts(btn("Thêm món", "primary", "md", "plus")))
                 + tabs(["Brand", "Outlet", "Món", "Xung đột (3)"], 2) + filter_bar([("Tất cả nhóm", False), ("Cảnh báo", False)], "Tìm món")
                 + table(["Món", "Nhóm", "Giá chuẩn", "Override", "Trạng thái", "Cảnh báo"], rows, ["1.8fr", "1fr", "110px", "90px", "120px", "1fr"], selected=2 if overlay else None), overlay)


@frame("A-044", "Menu item list", "Danh mục món")
def a044():
    return [("Thiếu giá, xung đột", item_list())]


@frame("A-045", "Menu item editor", "Danh mục món")
def a045():
    inner = (field("Tên món", "Cơm tấm sườn trứng ốp la") + select("Nhóm", "Cơm tấm") + field("Giá chuẩn", "", "VD: 50.000", mono=True, right=muted("đ"), error="Nhập giá chuẩn trước khi xuất bản.")
             + field("Mô tả", "Sườn nướng, trứng ốp la", textarea=True) + ovl("Tuỳ chọn (modifier)") + row(txt("Thêm cơm", "bsm", extra="flex-grow: 1; font-size: 14px"), mono("+5.000đ"), ibtn("trash", "Xoá", "ghost", 32), gap=10) + btn("Thêm tuỳ chọn", "ghost", "sm", "plus"))
    return [("Lỗi nhập liệu", item_list(drawer("Sửa món", inner, btn("Huỷ", "ghost", "md") + btn("Lưu nháp", "secondary", "md"), 520, pills=pill("draft", size="sm"))))]


@frame("A-046", "Outlet override editor", "Danh mục món")
def a046():
    rows = [["Cơm tấm sườn bì chả", mono("55.000đ"), field("", "60.000", mono=True, hgt=36), switch(True)], ["Cơm tấm sườn nướng", mono("45.000đ"), field("", "", "Theo chuẩn", mono=True, hgt=36), switch(True)],
            ["Chả trứng thêm", mono("12.000đ"), field("", "", "Theo chuẩn", mono=True, hgt=36), switch(False)]]
    inner = (txt("Override chỉ áp dụng cho outlet này, không đổi thực đơn chuẩn của brand.", "bsm", C["t2"]) + table(["Món", "Giá chuẩn", "Giá outlet", "Còn bán"], rows, ["1.6fr", "100px", "140px", "70px"])
             + field("Lý do (bắt buộc)", "Outlet Võ Văn Tần tăng giá từ 20/09 theo xác nhận của quán.", textarea=True))
    return [("Giá/trạng thái", outlet_list(drawer("Override · Sà Bì — Võ Văn Tần", inner, btn("Huỷ", "ghost", "md") + btn("Lưu nháp", "secondary", "md"), 640)))]


@frame("A-047", "Catalog conflict review", "Danh mục món")
def a047():
    rows = [[pill("changeRequested", "Trùng món", "sm"), "“Chả trứng thêm” và “Chả trứng (thêm)”", "Cơm Tấm Sà Bì", muted("Nhập file 22/09"), acts(btn("Gộp", "outline", "sm"), btn("Giữ cả hai", "ghost", "sm"))],
            [pill("issue", "Giá lệch", "sm"), "Sườn bì chả: chuẩn 55.000đ, 5 đề xuất tài xế 60.000đ", "Sà Bì — Nguyễn Trãi", muted("7 ngày qua"), acts(btn("Tạo override", "outline", "sm"), btn("Bỏ qua", "ghost", "sm"))],
            [pill("changeRequested", "Trùng outlet", "sm"), "“Sà Bì — PXL” và “Sà Bì — Phan Xích Long”", "Cơm Tấm Sà Bì", muted("Nhập file 22/09"), acts(btn("Gộp", "outline", "sm"), btn("Giữ cả hai", "ghost", "sm"))]]
    return [("Trùng/xung đột", admin("catalog", ["Danh mục món", "Xung đột"], page_head("Xung đột danh mục", "Đề xuất thay đổi của tài xế không tự cập nhật danh mục — Ops quyết định.")
                                     + tabs(["Brand", "Outlet", "Món", "Xung đột (3)"], 3) + table(["Loại", "Mô tả", "Phạm vi", "Nguồn", "Hành động"], rows, ["120px", "2.2fr", "1.2fr", "1fr", "220px"])))]


@frame("A-048", "Import/upload catalog placeholder", "Danh mục món")
def a048():
    inner = (f'<div style="height: 160px; border-radius: 12px; border: 1.5px dashed {C["b3"]}; background: {C["ink25"]}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px">{icon("upload", 28)}{txt("Kéo thả file CSV/XLSX", "bmd", extra="font-weight: 600")}{txt("Theo mẫu cột: brand, outlet, món, nhóm, giá", "cap", C["t3"])}</div>'
             + btn("Tải file mẫu", "ghost", "sm", "download")
             + banner("info", "Nhập thủ công trong P0", "File được kiểm tra và tạo bản nháp; Ops duyệt từng xung đột trước khi xuất bản. Trích xuất menu bằng AI/OCR chưa có trong P0."))
    return [("Ghi chú nhập thủ công", brand_list(overlay=admin_dialog("Nhập danh mục", inner, btn("Huỷ", "ghost", "md") + btn("Kiểm tra file", "disabled", "md"), 560, ic="upload", tone=None)))]


@frame("A-049", "Publish catalog changes", "Danh mục món")
def a049():
    inner = (table(["Thay đổi", "Số lượng"], [["Món mới", mono("3")], ["Sửa giá chuẩn", mono("2")], ["Override outlet", mono("2")], ["Ngưng bán", mono("1")]], ["1fr", "100px"])
             + field("Lý do (bắt buộc)", "Cập nhật menu tháng 10 theo file quán gửi 23/09.", textarea=True) + txt("Ứng dụng khách nhận thay đổi trong ~1 phút. Đơn đang chạy giữ ảnh chụp thực đơn cũ.", "cap", C["t3"]))
    return [("Xác nhận có lý do", brand_list(overlay=admin_dialog("Xuất bản danh mục Cơm Tấm Sà Bì", inner, btn("Huỷ", "ghost", "md") + btn("Xuất bản", "primary", "md", "upload"), 560, ic="upload", tone="info")))]


# ================= CASES =================
def case_rows():
    return [[tbl_link("CS-240924-0137"), "Thanh toán", mono("R-7Q2K9"), "Minh Anh ↔ Trần Văn Hùng", pill("pendingReview", "Đang xem xét", "sm"), mono("còn 21h"), "Hải Yến"],
            [tbl_link("CS-240924-0142"), "Thanh toán", mono("F-3M8TP"), "Minh Anh ↔ Lê Quốc Bảo", pill("requested", "Mới", "sm"), mono("còn 23h"), "—"],
            [tbl_link("CS-240922-0098"), "Thanh toán", mono("R-2H8QD"), "Minh Anh ↔ Võ Khánh", pill("changeRequested", "Chờ phản hồi", "sm"), mono("còn 6h"), "Minh Khoa"],
            [tbl_link("CS-240921-0090"), "An toàn", mono("R-8B1TT"), "Bảo Ngọc ↔ Đỗ Quân", pill("disputed", "Gian lận/an toàn", "sm"), f'<span style="color: {C["err"]}; font-weight: 600; font-family: {MONO}">Quá 2h</span>', "Minh Khoa"],
            [tbl_link("CS-240920-0077"), "Thanh toán", mono("R-6C0PE"), "Tuấn Anh ↔ Võ Khánh", pill("appeal", size="sm"), mono("còn 18h"), "Hải Yến"],
            [tbl_link("CS-240910-0021"), "Thái độ", mono("R-1K3ZP"), "Minh Anh ↔ Phạm Tú", pill("finalized", size="sm"), muted("—"), "Hải Yến"]]


def case_queue(overlay="", sel=None, tab=0):
    return admin("case", ["Khiếu nại & gian lận"], page_head("Khiếu nại & gian lận", "Khiếu nại không tự động thành hồ sơ gian lận. Mọi kết luận do con người quyết định.", acts(btn("Tạo hồ sơ", "outline", "md", "plus")))
                 + row(*[tag(t, i == tab) for i, t in enumerate(["Tất cả 17", "Mới 4", "Đang xem xét 9", "Kháng nghị 2", "Đã kết luận 312"])], gap=8)
                 + filter_bar([("Loại", False), ("Dịch vụ", False), ("Người xử lý", False), ("SLA", False)], "Mã case, mã chuyến, SĐT")
                 + table(["Mã hồ sơ", "Loại", "Chuyến/đơn", "Các bên", "Trạng thái", "SLA", "Người xử lý"], case_rows(), ["150px", "100px", "110px", "1.6fr", "150px", "100px", "1fr"], selected=sel), overlay)


@frame("A-050", "Complaint/case queue", "Khiếu nại & gian lận")
def a050():
    return [("Tất cả", case_queue()), ("Lọc kháng nghị", case_queue(tab=3))]


def case_page(extra_right="", overlay="", status="pendingReview", status_label="Đang xem xét", decision=None):
    tl = timeline([("REPORTED · khách gửi khiếu nại", "24/09 08:30", "done"), ("EVIDENCE_COLLECTION", "24/09 09:10 · Hải Yến", "done"),
                   ("DRIVER_RESPONSE · chờ tài xế", "Hạn 25/09 09:10", "current"), ("HUMAN_REVIEW", "", "todo"), ("HUMAN_DECISION", "", "todo"), ("FINALIZED", "", "todo")], True)
    left = (section_card("Thông tin", kv("Dịch vụ", "Đi xe · R-7Q2K9 · 48.000đ") + kv("Khách", "Minh Anh · 0901 234 567") + kv("Tài xế", "Trần Văn Hùng · 59-X2 123.45") + kv("Loại", "Thanh toán · tài xế báo chưa nhận tiền"))
            + section_card("Bằng chứng (4)", row(*[f'<a href="A-052.dc.html" style="text-decoration: none">{photo(120, 90, l, i, 8)}</a>' for l, i in [("Chứng từ khách", "image"), ("Ảnh chat", "message"), ("Sao kê tài xế", "file"), ("Ảnh khách gửi", "image")]], gap=8)
                           + txt("Nhật ký chat được lưu làm bằng chứng (không bị xoá sau 7 ngày).", "cap", C["t3"])))
    right = section_card("Tiến trình", tl) + (decision or "") + extra_right
    content = (page_head("CS-240924-0137", "Mở 24/09 08:30 · SLA còn 21 giờ · Người xử lý: Hải Yến", acts(btn("Yêu cầu phản hồi", "outline", "md", "send", href="A-054.dc.html"), btn("Nâng cấp gian lận", "outline", "md", "shield-alert", href="A-055.dc.html"), btn("Ra kết luận", "primary", "md", href="A-056.dc.html")), pill(status, status_label))
               + row(f'<div style="flex: 3; display: flex; flex-direction: column; gap: 16px">{left}</div>', f'<div style="flex: 2; display: flex; flex-direction: column; gap: 16px">{right}</div>', gap=16, align="flex-start"))
    return admin("case", ["Khiếu nại & gian lận", "CS-240924-0137"], content, overlay)


@frame("A-051", "Case detail", "Khiếu nại & gian lận")
def a051():
    return [("Đang xem xét", case_page())]


def evidence_viewer(expired=False):
    img = (f'<div style="flex-grow: 1; border-radius: 12px; background: #2F2E2E; display: flex; align-items: center; justify-content: center; color: #A3A2A0; flex-direction: column; gap: 8px">{icon("image", 56)}<span style="{TY["bsm"]}">Chứng từ khách · 24/09 08:14</span></div>'
           if not expired else f'<div style="flex-grow: 1; border-radius: 12px; background: #FFFFFF; border: 1px solid {C["b2"]}; display: flex; align-items: center; justify-content: center">{empty_state("clock", "Liên kết đã hết hạn", "Liên kết xem ảnh chỉ có hiệu lực 10 phút. Tải lại để tạo liên kết mới — lượt xem sẽ được ghi audit.", btn("Tải lại", "secondary", "md", "refresh"))}</div>')
    side = col(txt("Siêu dữ liệu", "lbl"), kv("Loại", "Chứng từ thanh toán"), kv("Người tải lên", "Khách · Minh Anh"), kv("Thời điểm", "24/09 08:14:22"), kv("Kích thước", "1080×2340 · 412 KB"), kv("Hash", "sha256:9f2c…a41e", True),
               divider(), txt("Lượt xem", "lbl"), txt("Hải Yến · 24/09 09:10<br>Minh Khoa · 24/09 09:40", "bsm", C["t2"]), gap=8, extra="width: 300px; flex-shrink: 0")
    modal = (f'<div style="position: absolute; inset: 0; background: {C["overlay"]}; display: flex; align-items: center; justify-content: center"><div role="dialog" aria-modal="true" style="width: 1120px; height: 740px; background: {C["page"]}; border-radius: 16px; box-shadow: {SH_LG}; display: flex; flex-direction: column; overflow: hidden">'
             f'<div style="display: flex; align-items: center; gap: 12px; padding: 14px 20px; background: #FFFFFF; border-bottom: 1px solid {C["b2"]}">{txt("Bằng chứng · CS-240924-0137", "hsm", extra="flex-grow: 1")}{segmented(["Chứng từ", "Ảnh chat", "Sao kê", "Ảnh khiếu nại"], 0, False)}{ibtn("x", "Đóng", "ghost", 36)}</div>'
             f'<div style="flex-grow: 1; display: flex; gap: 20px; padding: 20px; min-height: 0">{img}{side}</div></div></div>')
    return case_page(overlay=modal)


@frame("A-052", "Evidence viewer", "Khiếu nại & gian lận")
def a052():
    return [("Chứng từ thanh toán", evidence_viewer())]


@frame("A-053", "Payment proof dispute review", "Khiếu nại & gian lận")
def a053():
    inner = (row(col(txt("Khách gửi", "lbl"), photo(220, 300, "Chứng từ khách · 48.000đ", "image", 10), kv("Thời gian", "08:14:22"), kv("Số tiền", "48.000đ", True), kv("TK nhận", "VCB ••• 4567 89", True), gap=8, extra="flex: 1"),
                 col(txt("Tài xế cung cấp", "lbl"), photo(220, 300, "Sao kê tài xế 08:00–08:30", "file", 10), kv("Giao dịch khớp", "Không thấy"), kv("Số dư thay đổi", "0đ", True), kv("TK tài xế", "VCB ••• 4567 89", True), gap=8, extra="flex: 1"), gap=16, align="flex-start")
             + banner("warning", "Bằng chứng mâu thuẫn", "Chứng từ khách có mã FT24268081122 nhưng sao kê tài xế không có giao dịch này. Có thể chuyển chậm (liên ngân hàng) hoặc ảnh không hợp lệ.")
             + select("Hướng xử lý", "Yêu cầu khách cung cấp xác nhận từ ngân hàng"))
    return [("Bằng chứng mâu thuẫn", case_page(overlay=drawer("Đối chiếu chứng từ thanh toán", inner, btn("Yêu cầu phản hồi", "outline", "md", "send", href="A-054.dc.html") + btn("Ra kết luận", "secondary", "md", href="A-056.dc.html"), 720, pills=pill("disputed"))))]


@frame("A-054", "Request user response", "Khiếu nại & gian lận")
def a054():
    inner = (segmented(["Khách", "Tài xế", "Cả hai"], 1, False) + select("Mẫu yêu cầu", "Cung cấp sao kê ngân hàng")
             + field("Nội dung gửi tài xế", "Vui lòng gửi ảnh sao kê tài khoản Vietcombank ngày 24/09 từ 08:00–08:30 để đối chiếu giao dịch 48.000đ.", textarea=True)
             + select("Hạn phản hồi", "24 giờ (25/09 09:10)") + txt("Hết hạn không phản hồi: hồ sơ tiếp tục xem xét với bằng chứng hiện có.", "cap", C["t3"]))
    return [("Khách/tài xế, hạn", case_page(overlay=admin_dialog("Yêu cầu phản hồi", inner, btn("Huỷ", "ghost", "md") + btn("Gửi yêu cầu", "primary", "md", "send"), 600)))]


@frame("A-055", "Fraud escalation", "Khiếu nại & gian lận")
def a055():
    inner = (txt("Chuyển khiếu nại sang quy trình gian lận thủ công (REPORTED → … → FINALIZED). Không tự động khoá tài xế.", "bsm", C["t2"])
             + select("Loại gian lận", "Chứng từ thanh toán giả") + select("Mức độ", "Cao") + field("Lý do (bắt buộc)", "Hash ảnh trùng với chứng từ trong CS-240918-0051 của khách khác.", textarea=True)
             + checkbox("Đề xuất khoá tạm tài xế", False, "Cần Risk/Fraud Analyst phê duyệt"))
    return [("Loại, mức độ, lý do", case_page(overlay=admin_dialog("Nâng cấp thành hồ sơ gian lận", inner, btn("Huỷ", "ghost", "md") + btn("Nâng cấp", "danger", "md", "shield-alert"), 560, ic="shield-alert", tone="danger")))]


@frame("A-056", "Case decision form", "Khiếu nại & gian lận")
def a056():
    def f(sel):
        inner = (radio("<b>Xác nhận</b> — khiếu nại đúng", sel == 0, "Bên bị khiếu nại chịu trách nhiệm theo nguyên tắc bên nào sai bên đó chịu")
                 + radio("<b>Bác bỏ</b> — khiếu nại không đúng", sel == 1, "Không có vi phạm")
                 + select("Bên chịu trách nhiệm", "Tài xế" if sel == 0 else "Không") + field("Kết luận gửi các bên (bắt buộc)", "Sao kê xác nhận tài xế đã nhận 48.000đ lúc 08:16. Khiếu nại không đúng." if sel == 1 else "Tài xế không cung cấp sao kê trong hạn; chứng từ khách hợp lệ. Tài xế cần hoàn 48.000đ cho khách.", textarea=True)
                 + checkbox("Cập nhật risk status tài xế", sel == 0) + txt("Onway không tự bồi thường thay các bên. Kết luận có thể bị kháng nghị trong 7 ngày.", "cap", C["t3"]))
        return case_page(overlay=admin_dialog("Kết luận hồ sơ CS-240924-0137", inner, btn("Huỷ", "ghost", "md") + btn("Lưu kết luận", "primary", "md"), 620))
    return [("Xác nhận", f(0)), ("Bác bỏ", f(1))]


@frame("A-057", "Appeal review", "Khiếu nại & gian lận")
def a057():
    inner = (card(kv("Kết luận ban đầu", "Xác nhận · tài xế chịu trách nhiệm") + kv("Người kết luận", "Hải Yến · 20/09"), pad=12, gap=6) + txt("Nội dung kháng nghị", "lbl")
             + card(txt("“Tôi đã cập nhật tài khoản nhận tiền mới từ 19/09; khách chuyển vào tài khoản cũ. Sao kê tài khoản mới đính kèm.”", "bmd"), pad=14, bg=C["ink25"])
             + row(photo(140, 100, "Sao kê mới", "file", 8), gap=8) + field("Lý do quyết định (bắt buộc)", "", textarea=True)
             + txt("Người xem xét kháng nghị phải khác người ra kết luận ban đầu.", "cap", C["t3"]))
    return [("Chấp nhận/bác kháng nghị", case_queue(drawer("Kháng nghị · CS-240920-0077", inner, btn("Bác kháng nghị", "danger", "md") + btn("Chấp nhận kháng nghị", "primary", "md"), 600, pills=pill("appeal")), 4, 3))]


@frame("A-058", "Case audit timeline", "Khiếu nại & gian lận")
def a058():
    tl = section_card("Nhật ký audit (không thể sửa)", timeline([("Xem bằng chứng: Chứng từ khách", "Minh Khoa · 24/09 09:40", "done"), ("Gửi yêu cầu phản hồi tới tài xế", "Hải Yến · 24/09 09:12", "done", "Hạn 25/09 09:10"),
                                                             ("Nhận hồ sơ", "Hải Yến · 24/09 09:10", "done"), ("Hệ thống tạo hồ sơ từ khiếu nại khách", "Hệ thống · 24/09 08:30", "done")], True), pill("locked", "Chỉ đọc", "sm"))
    return [("Bất biến", case_page(extra_right=tl))]


@frame("A-059", "Case finalized summary", "Khiếu nại & gian lận")
def a059():
    dec = section_card("Kết luận", txt("Bác bỏ khiếu nại", "hsm") + txt("Sao kê xác nhận tài xế đã nhận 48.000đ lúc 08:16. Khiếu nại do khách nhầm lẫn thời gian.", "bsm", C["t2"])
                       + kv("Bên chịu trách nhiệm", "Không") + kv("Người kết luận", "Hải Yến · 24/09 15:40") + kv("Hạn kháng nghị", "01/10/2026") + divider()
                       + txt("Bước tiếp theo: đã thông báo hai bên; không có thay đổi risk status.", "cap", C["t3"]), pill("finalized", size="sm"))
    return [("Đã kết luận", case_page(status="finalized", status_label="Đã kết luận", decision=dec))]


# ================= COMMON ADMIN =================
@frame("A-060", "Media/evidence signed URL expired", "Bằng chứng, audit & hệ thống")
def a060():
    deny = case_page(overlay=admin_dialog("Không có quyền xem bằng chứng", banner("danger", "Vai trò Support Operator không được xem sao kê tài chính", "Yêu cầu Risk/Fraud Analyst mở bằng chứng này. Lượt truy cập bị từ chối đã được ghi audit.", "lock"),
                                          btn("Đóng", "secondary", "md"), 520, ic="lock", tone="danger"))
    return [("Hết hạn — tải lại", evidence_viewer(True)), ("Không có quyền", deny)]


def audit_log(state="default"):
    rows = [[mono("24/09 10:42:13"), "Ngọc Lan", "Ops Admin", "region.publish", tbl_link("Quận 3 · v7"), muted("Mở rộng ranh giới phía bắc"), mono("113.161.x.x")],
            [mono("24/09 10:15:02"), "Minh Khoa", "Risk Analyst", "driver.unlock", tbl_link("Võ Khánh"), muted("Kháng nghị hợp lệ"), mono("113.161.x.x")],
            [mono("24/09 09:58:40"), "Hệ thống", "—", "driver.autolock", tbl_link("Lê Văn Tài"), muted("COMPLAINT_VALID_3_30D"), mono("—")],
            [mono("24/09 09:40:11"), "Minh Khoa", "Risk Analyst", "evidence.view", tbl_link("CS-240924-0137"), muted("—"), mono("113.161.x.x")],
            [mono("24/09 09:31:55"), "Thu Hà", "Finance Ops", "fee.approve", tbl_link("FEE-240924-0331"), muted("Khớp sao kê"), mono("14.232.x.x")]]
    if state == "filter":
        rows = [rows[1], rows[2]]
    body_ = (card(empty_state("history", "Không có bản ghi phù hợp", "Thử mở rộng khoảng thời gian hoặc bỏ bớt bộ lọc."), pad=48) if state == "empty"
             else table(["Thời gian", "Người thực hiện", "Vai trò", "Hành động", "Đối tượng", "Lý do", "IP"], rows, ["150px", "1fr", "110px", "140px", "1.2fr", "1.6fr", "110px"]))
    chips = [("24/09/2026", True), ("Hành động", state == "filter"), ("Người thực hiện", False)]
    return admin("audit", ["Nhật ký audit"], page_head("Nhật ký audit", "Bản ghi bất biến cho mọi thay đổi cấu hình, quyết định và lượt xem dữ liệu nhạy cảm.", acts(btn("Xuất (sắp có)", "disabled", "md", "download")))
                 + filter_bar(chips, "driver.unlock, mã đối tượng…") + body_ + txt("Xuất nhật ký sẽ có ở phiên bản sau; hiện chỉ tra cứu trong Portal.", "cap", C["t3"]))


@frame("A-061", "Audit log search", "Bằng chứng, audit & hệ thống")
def a061():
    return [("Mặc định", audit_log()), ("Có bộ lọc", audit_log("filter")), ("Trống", audit_log("empty"))]


def rbac_list(overlay=""):
    rows = [[row(avatar("SA", 28), "Super Admin"), mono("admin@onway.vn"), "Super Admin", pill("active", size="sm"), muted("24/09 08:00")],
            [row(avatar("NL", 28), "Ngọc Lan"), mono("lan.nguyen@onway.vn"), "Ops Admin", pill("active", size="sm"), muted("24/09 10:42")],
            [row(avatar("QH", 28), "Quang Huy"), mono("huy.tran@onway.vn"), "Driver Ops", pill("active", size="sm"), muted("24/09 09:12")],
            [row(avatar("TH", 28), "Thu Hà"), mono("ha.le@onway.vn"), "Finance Ops", pill("active", size="sm"), muted("24/09 09:31")],
            [row(avatar("MK", 28), "Minh Khoa"), mono("khoa.pham@onway.vn"), "Risk/Fraud Analyst", pill("active", size="sm"), muted("24/09 10:15")],
            [row(avatar("HY", 28), "Hải Yến"), mono("yen.vo@onway.vn"), "Support Operator", pill("active", size="sm"), muted("24/09 09:10")],
            [row(avatar("TT", 28), "Thanh Tâm"), mono("tam.do@onway.vn"), "Catalog Ops", pill("active", size="sm"), muted("24/09 08:40")],
            [row(avatar("BV", 28), "Bảo Vy"), mono("vy.ngo@onway.vn"), "Viewer", pill("offline", "Chưa đăng nhập", "sm"), muted("—")]]
    return admin("rbac", ["Quản trị viên & quyền"], page_head("Quản trị viên & quyền", "8 tài khoản · 7 vai trò", acts(btn("Mời quản trị viên", "primary", "md", "plus")))
                 + tabs(["Người dùng", "Vai trò"], 0) + table(["Tên", "Email", "Vai trò", "Trạng thái", "Hoạt động gần nhất"], rows, ["1.3fr", "1.6fr", "1.2fr", "150px", "1fr"], selected=2 if overlay else None), overlay)


@frame("A-062", "Admin user / RBAC list", "Bằng chứng, audit & hệ thống")
def a062():
    return [("Danh sách vai trò", rbac_list())]


@frame("A-063", "Admin user detail / role assignment", "Bằng chứng, audit & hệ thống")
def a063():
    perms = [("Xem hồ sơ tài xế", True, True), ("Duyệt/từ chối hồ sơ", True, True), ("Sửa eligibility dịch vụ", True, True), ("Khoá tài xế thủ công", True, True),
             ("Mở khoá tài xế", False, False), ("Duyệt phí nền tảng", False, False), ("Xuất bản vùng/chính sách", False, False), ("Xem sao kê tài chính", False, False)]
    mat = table(["Quyền", "Driver Ops", "Được cấp"], [[p, icon("check", 16, C["ok"]) if a else icon("x", 16, C["t3"]), icon("check", 16, C["ok"]) if b else muted("—")] for p, a, b in perms], ["1.8fr", "100px", "100px"])
    inner = row(avatar("QH", 48), col(txt("Quang Huy", "hsm"), mono("huy.tran@onway.vn"), gap=2), gap=12) + select("Vai trò", "Driver Ops") + select("Phạm vi", "TP. Hồ Chí Minh") + txt("Ma trận quyền", "lbl") + mat
    return [("Ma trận quyền", rbac_list(drawer("Quyền quản trị viên", inner, btn("Vô hiệu hoá", "danger", "md") + btn("Lưu vai trò", "secondary", "md"), 560)))]


@frame("A-064", "Sensitive action reason dialog", "Bằng chứng, audit & hệ thống")
def a064():
    def d(err):
        inner = (txt("Bạn sắp <b>xem sao kê tài chính</b> của tài xế Trần Văn Hùng. Đây là hành động nhạy cảm và được ghi audit.", "bsm", C["t2"])
                 + select("Lý do", "Xử lý hồ sơ khiếu nại") + field("Mã hồ sơ / ghi chú (bắt buộc)", "" if err else "CS-240924-0137", error="Nhập mã hồ sơ liên quan." if err else None))
        return case_page(overlay=admin_dialog("Xác nhận hành động nhạy cảm", inner, btn("Huỷ", "ghost", "md") + btn("Tiếp tục", "secondary", "md"), 520, ic="shield", tone="warning"))
    return [("Mặc định", d(False)), ("Lỗi thiếu lý do", d(True))]


@frame("A-065", "Config version diff", "Bằng chứng, audit & hệ thống")
def a065():
    diff = (row(col(txt("v12 · đã xuất bản", "lbl"), f'<div style="height: 260px; border-radius: 10px; overflow: hidden; border: 1px solid {C["b2"]}">{map_svg(270, 260, regions=[([(0.12, 0.12), (0.8, 0.1), (0.84, 0.86), (0.16, 0.9)], "active")], labels=False)}</div>', gap=8, extra="flex: 1"),
                col(txt("v13 · bản nháp", "lbl"), f'<div style="height: 260px; border-radius: 10px; overflow: hidden; border: 1px solid {C["b2"]}">{map_svg(270, 260, regions=[([(0.12, 0.12), (0.8, 0.1), (0.94, 0.5), (0.84, 0.86), (0.16, 0.9)], "selected")], labels=False)}</div>', gap=8, extra="flex: 1"), gap=12)
            + table(["Trường", "Trước", "Sau"], [["Số đỉnh", mono("4"), mono("5")], ["Diện tích", mono("7,7 km²"), mono("7,9 km²")], ["Food tạm dừng", mono("—"), mono("22:00–06:00")]], ["1fr", "1fr", "1fr"]))
    return [("Trước / sau", region_list(overlay=drawer("So sánh phiên bản · Quận 1", diff, btn("Đóng", "ghost", "md"), 640)))]


@frame("A-066", "Basic ops dashboard drilldown", "Tổng quan")
def a066():
    rows = [["Quận 1", mono("412"), mono("140"), mono("92,1%"), mono("34s"), mono("0,5%")], ["Quận 3", mono("388"), mono("122"), mono("93,4%"), mono("31s"), mono("0,4%")],
            ["Quận 4", mono("—"), mono("—"), muted("Tạm dừng"), mono("—"), mono("—")], ["Phú Nhuận", mono("206"), mono("98"), mono("88,0%"), mono("52s"), mono("1,1%")]]
    return [("Ride/Food/rủi ro theo vùng", admin("dash", ["Tổng quan", "Chi tiết"], page_head("Chi tiết vận hành", "Hôm nay · theo vùng", acts(segmented(["Hôm nay", "7 ngày", "30 ngày"], 0, False)))
                                                 + row(stat("Chuyến Đi xe", "1.284", "+8,2%"), stat("Đơn Đặt món", "436", "+3,1%"), stat("Hồ sơ gian lận mới", "2", ""), stat("Tài xế bị khoá", "6", ""), gap=16)
                                                 + table(["Vùng", "Chuyến", "Đơn món", "Ghép thành công", "Thời gian ghép TB", "Tranh chấp"], rows, ["1.2fr", "1fr", "1fr", "1fr", "1fr", "1fr"])))]


@frame("A-067", "System health / queue status", "Bằng chứng, audit & hệ thống")
def a067():
    def s(degraded):
        rows = [["GraphQL API", pill("active", "Bình thường", "sm"), mono("p95 180ms"), muted("—")],
                ["WebSocket (chat, vị trí)", pill("active", "Bình thường", "sm") if not degraded else pill("paused", "Suy giảm", "sm"), mono("12.408 kết nối"), muted("—") if not degraded else muted("Tỷ lệ reconnect 8%")],
                ["Bản đồ HERE (route/geocode)", pill("active", "Bình thường", "sm") if not degraded else pill("issue", "Lỗi một phần", "sm"), mono("p95 420ms") if not degraded else mono("lỗi 12%"), muted("—") if not degraded else muted("Đang dùng cache tuyến")],
                ["Gửi OTP (ViHAT/Firebase)", pill("active", "Bình thường", "sm"), mono("99,2% thành công"), muted("—")],
                ["Hàng đợi thông báo đẩy", pill("active", "Bình thường", "sm"), mono("tồn 14"), muted("—")],
                ["Lưu trữ bằng chứng", pill("active", "Bình thường", "sm"), mono("p95 900ms"), muted("—")]]
        b = banner("warning", "Hệ thống đang suy giảm", "Bản đồ HERE trả lỗi 12% yêu cầu từ 10:31. Ứng dụng dùng tuyến đã cache; một số khách không tính được giá.") if degraded else banner("success", "Mọi dịch vụ hoạt động bình thường", "")
        return admin("health", ["Sức khoẻ hệ thống"], page_head("Sức khoẻ hệ thống", "Cập nhật mỗi 30 giây") + b + table(["Dịch vụ", "Trạng thái", "Chỉ số", "Ghi chú"], rows, ["1.6fr", "150px", "1fr", "1.6fr"]))
    return [("Bình thường", s(False)), ("Suy giảm", s(True))]


@frame("A-068", "Admin settings", "Bằng chứng, audit & hệ thống")
def a068():
    return [("Hồ sơ, thông báo, đăng xuất", admin("settings", ["Cài đặt"], page_head("Cài đặt") + row(
        section_card("Hồ sơ", row(avatar("NL", 56), col(txt("Ngọc Lan", "hsm"), mono("lan.nguyen@onway.vn"), txt("Ops Admin · TP. Hồ Chí Minh", "cap", C["t3"]), gap=2), gap=14)
                     + btn("Đổi mật khẩu", "outline", "md", "key") + switch(True, "Xác minh hai bước", "Bắt buộc cho vai trò có quyền xuất bản"), extra="flex: 1"),
        section_card("Thông báo", switch(True, "Hồ sơ quá SLA") + switch(True, "Khoá tự động mới") + switch(False, "Mỗi xuất bản cấu hình") + switch(True, "Hệ thống suy giảm"), extra="flex: 1"), gap=16, align="flex-start")
        + row(btn("Đăng xuất", "outline", "md", "log-out"), spacer())))]


@frame("A-069", "Empty/error/loading template", "Bằng chứng, audit & hệ thống")
def a069():
    e_ = card(empty_state("inbox", "Chưa có dữ liệu", "Mẫu trạng thái trống dùng chung: icon, tiêu đề, mô tả, 1 hành động."), pad=40)
    er = card(empty_state("alert-circle", "Không tải được dữ liệu", "Mẫu lỗi: nêu nguyên nhân, mã lỗi (VD 503) và hành động thử lại.", btn("Thử lại", "outline", "md", "refresh")), pad=40)
    ld = card(col(skel(240, 20), skel("100%", 36, 8), *[skel("100%", 44, 0) for _ in range(5)], gap=8), pad=20)
    return [("Mẫu trống / lỗi / đang tải", admin("dash", ["Mẫu trạng thái"], page_head("Mẫu trạng thái dùng chung") + row(f'<div style="flex: 1">{e_}</div>', f'<div style="flex: 1">{er}</div>', f'<div style="flex: 1">{ld}</div>', gap=16, align="flex-start")))]


def finance_queue(overlay="", filtered=False):
    rows = [[tbl_link("FEE-240924-0331"), row(avatar("TH", 28), "Trần Văn Hùng"), mono("1.000.000đ"), mono("ONWFEE 0901234567"), mono("24/09 10:32"), mono("còn 2h"), pill("proofPending", size="sm")],
            [tbl_link("FEE-240924-0329"), row(avatar("NT", 28), "Nguyễn Thị Thu"), mono("1.000.000đ"), mono("ONWFEE 0977555010"), mono("24/09 09:05"), f'<span style="color: {C["err"]}; font-weight: 600; font-family: {MONO}">Quá 1h</span>', pill("proofPending", size="sm")],
            [tbl_link("FEE-240923-0318"), row(avatar("PM", 28), "Phạm Minh"), mono("900.000đ"), mono("ONWFEE 0912000333"), mono("23/09 17:40"), muted("—"), pill("proofRejected", size="sm")],
            [tbl_link("FEE-240923-0310"), row(avatar("LB", 28), "Lê Quốc Bảo"), mono("1.000.000đ"), mono("ONWFEE 0938111222"), mono("23/09 15:12"), muted("—"), pill("proofVerified", "Đã xác nhận", "sm")]]
    if filtered:
        rows = rows[:2]
    return admin("finance", ["Duyệt phí nền tảng"], page_head("Duyệt chứng từ phí nền tảng", "SLA 4 giờ làm việc. Chỉ khoản Onway thu (phí nền tảng); Onway không xử lý tiền chuyến/đơn.")
                 + row(*[tag(t, i == (1 if filtered else 0)) for i, t in enumerate(["Tất cả", "Chờ xác minh 8", "Đã xác nhận", "Bị từ chối"])], gap=8)
                 + filter_bar([("Hôm nay", True), ("SLA", False)], "Mã chứng từ, tài xế")
                 + table(["Mã chứng từ", "Tài xế", "Số tiền", "Nội dung", "Gửi lúc", "SLA", "Trạng thái"], rows, ["150px", "1.3fr", "120px", "1.4fr", "110px", "90px", "140px"], selected=0 if overlay else None), overlay)


@frame("A-070", "Finance proof queue", "Tài chính & khách hàng")
def a070():
    return [("Tất cả", finance_queue()), ("Lọc chờ xác minh", finance_queue(filtered=True))]


@frame("A-071", "Finance proof detail", "Tài chính & khách hàng")
def a071():
    inner = row(avatar("TH", 44), col(txt("Trần Văn Hùng", "bmd", extra="font-weight: 700"), mono("DRV-000611 · 0901 234 567"), gap=2), spacer(), pill("approved", "Hồ sơ đã duyệt", "sm"), gap=12) + fee_proof_inner()
    return [("Duyệt/từ chối", finance_queue(drawer("FEE-240924-0331", inner, btn("Từ chối", "danger", "md") + btn("Xác nhận & kích hoạt", "primary", "md", "check"), 640, pills=pill("proofPending"))))]


def customer_mgmt(overlay=""):
    rows = [[row(avatar("MA", 28), tbl_link("Nguyễn Minh Anh")), mono("0901 234 567"), mono("38"), mono("2"), pill("active", size="sm"), muted("24/09 08:27")],
            [row(avatar("BN", 28), tbl_link("Trần Bảo Ngọc")), mono("0933 888 777"), mono("12"), mono("1"), pill("active", size="sm"), muted("21/09 19:02")],
            [row(avatar("TA", 28), tbl_link("Lê Tuấn Anh")), mono("0968 123 456"), mono("5"), mono("1"), pill("active", size="sm"), muted("20/09 12:30")]]
    return admin("customer", ["Khách hàng"], page_head("Khách hàng", "Chỉ tra cứu phục vụ hỗ trợ và khiếu nại. Mọi lượt xem hồ sơ được ghi audit.")
                 + filter_bar([("Có khiếu nại", True)], "SĐT, tên, mã chuyến") + table(["Khách", "SĐT", "Chuyến/đơn", "Khiếu nại", "Trạng thái", "Hoạt động gần nhất"], rows, ["1.4fr", "1fr", "100px", "100px", "120px", "1fr"], selected=0 if overlay else None), overlay)


@frame("A-072", "Customer management light", "Tài chính & khách hàng")
def a072():
    return [("Tìm kiếm", customer_mgmt())]


@frame("A-073", "Customer detail / history", "Tài chính & khách hàng")
def a073():
    inner = (row(avatar("MA", 48), col(txt("Nguyễn Minh Anh", "hsm"), mono("0901 234 567 · CUS-002331"), gap=2), gap=12) + tabs(["Chuyến & đơn", "Khiếu nại", "Bằng chứng"], 0)
             + "".join(list_row(t, s, i, right=pill(p, size="sm"), pad="12px 0") for t, s, i, p in [("R-7Q2K9 · Bitexco → ĐH Kinh tế", "24/09 08:27 · 48.000đ", "bike", "completed"),
                                                                                                  ("F-3M8TP · Cơm Tấm Sà Bì", "23/09 11:02 · 137.000đ", "utensils", "completed"),
                                                                                                  ("R-2H8QD · Bến Thành → Tân Định", "22/09 18:10 · 32.000đ", "bike", "disputed")])
             + txt("Khiếu nại liên kết: CS-240924-0137, CS-240922-0098", "cap", C["t3"]))
    return [("Lịch sử & khiếu nại", customer_mgmt(drawer("Khách hàng", inner, btn("Mở khiếu nại", "outline", "md"), 560)))]


@frame("A-074", "Notification template/config baseline", "Bằng chứng, audit & hệ thống")
def a074():
    rows = [[mono("job.offer"), "Tài xế", "Yêu cầu chuyến mới", "Push", pill("published", size="sm")],
            [mono("payment.proof_submitted"), "Tài xế", "Khách đã gửi chứng từ", "Push", pill("published", size="sm")],
            [mono("payment.confirmed"), "Khách", "Tài xế đã nhận đủ tiền", "Push", pill("published", size="sm")],
            [mono("chat.message"), "Cả hai", "Tin nhắn mới", "Push", pill("published", size="sm")],
            [mono("driver.locked"), "Tài xế", "Tài khoản tạm khoá", "Push + SMS", pill("draft", size="sm")]]
    preview = section_card("Xem trước · driver.locked", card(row(mark_img(32), col(txt("Onway Tài xế", "lbl"), txt("Tài khoản tạm khoá", "bsm", extra="font-weight: 600; font-size: 14px"), txt("Tài khoản của bạn tạm khoá để xem xét: [lý do ngắn]. Mở ứng dụng để gửi kháng nghị.", "bsm", C["t2"]), gap=2), gap=10, align="flex-start"), pad=12, bg=C["ink25"])
                           + txt("Không đưa chi tiết bằng chứng nhạy cảm vào thông báo.", "cap", C["t3"]), extra="flex: 1")
    return [("Mẫu việc/thanh toán/chat/khoá", admin("notif", ["Mẫu thông báo"], page_head("Mẫu thông báo", "Mẫu tiếng Việt cho push/SMS. Biến động đặt trong dấu [ ].") + row(
        f'<div style="flex: 2">{table(["Mã", "Người nhận", "Tiêu đề", "Kênh", "Trạng thái"], rows, ["1.6fr", "90px", "1.4fr", "110px", "110px"], selected=4)}</div>', preview, gap=16, align="flex-start")))]


def privacy_queue(overlay=""):
    rows = [[tbl_link("DR-240924-0012"), "Xoá tài khoản", "Khách · Minh Anh", mono("24/09"), mono("còn 29 ngày"), pill("paused", "Tạm hoãn (có khiếu nại)", "sm")],
            [tbl_link("DR-240923-0009"), "Xuất dữ liệu", "Tài xế · Võ Khánh", mono("23/09"), mono("còn 28 ngày"), pill("pendingReview", size="sm")],
            [tbl_link("DR-240915-0004"), "Xoá tài khoản", "Khách · Hoàng Lan", mono("15/09"), muted("—"), pill("completed", "Đã xoá (giữ bản ghi luật định)", "sm")]]
    return admin("privacy", ["Yêu cầu dữ liệu"], page_head("Yêu cầu dữ liệu cá nhân", "Xuất/xoá dữ liệu theo yêu cầu. Ngoại lệ pháp lý, audit và gian lận phải ghi rõ.")
                 + table(["Mã", "Loại", "Người yêu cầu", "Ngày gửi", "Hạn", "Trạng thái"], rows, ["150px", "1fr", "1.4fr", "100px", "120px", "1.6fr"], selected=0 if overlay else None), overlay)


@frame("A-075", "Data/privacy request queue", "Tài chính & khách hàng")
def a075():
    return [("Xuất/xoá, ngoại lệ", privacy_queue())]


@frame("A-076", "Data/privacy request detail", "Tài chính & khách hàng")
def a076():
    inner = (card(kv("Người yêu cầu", "Nguyễn Minh Anh · CUS-002331") + kv("Loại", "Xoá tài khoản") + kv("Xác minh OTP", "Đã xác minh 24/09 12:10"), pad=14, gap=8)
             + banner("warning", "Ngoại lệ pháp lý", "Có khiếu nại CS-240924-0137 đang mở — dữ liệu liên quan phải giữ đến khi kết luận.")
             + txt("Quyết định", "lbl") + radio("Tạm hoãn đến khi hồ sơ kết luận", True) + radio("Xoá, giữ dữ liệu theo nghĩa vụ luật định") + radio("Từ chối")
             + field("Lý do (bắt buộc)", "Giữ dữ liệu theo chính sách lưu trữ khiếu nại.", textarea=True)
             + txt("Audit", "lbl") + timeline([("Tạo yêu cầu", "Khách · 24/09 12:10", "done"), ("Nhận xử lý", "Hải Yến · 24/09 13:00", "done")], True))
    return [("Quyết định & audit", privacy_queue(drawer("DR-240924-0012", inner, btn("Huỷ", "ghost", "md") + btn("Lưu quyết định", "secondary", "md"), 560, pills=pill("paused", "Tạm hoãn"))))]
