# Admin Portal — frames added after gap analysis (A-077 … A-092) + richer versions of thin frames.
from lib import *
from reg import frame
import admin as ad
acts = ad.acts

G_MON = "Giám sát chuyến & đơn"
G_RISK = "Rủi ro & thiết bị"


def bar_chart(vals, labels, hi=None, h_=140, color=None):
    mx = max(vals) or 1
    bars = "".join(
        f'<div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 6px"><div style="width: 100%; height: {round(v / mx * h_)}px; border-radius: 4px 4px 0 0; background: {C["inverse"] if i == hi else (color or C["b3"])}"></div>'
        f'<span style="{TY["cap"]}; font-size: 11px; color: {C["t3"]}">{l}</span></div>' for i, (v, l) in enumerate(zip(vals, labels)))
    return f'<div style="display: flex; gap: 6px; align-items: flex-end; height: {h_ + 22}px">{bars}</div>'


def kvs(*pairs, gap=8):
    return col(*[kv(k, v, m) for k, v, m in pairs], gap=gap)


def tl_row(t, who, st, note=""):
    return (t, who, st, note)


# ================= LIVE MAP =================
def live_map(sel=False):
    W, H = 820, 740
    regs = [([(0.06, 0.06), (0.5, 0.04), (0.54, 0.5), (0.1, 0.54)], "active", "Quận 1"), ([(0.56, 0.04), (0.95, 0.08), (0.92, 0.48), (0.58, 0.5)], "active", "Quận 3"),
            ([(0.12, 0.6), (0.52, 0.58), (0.54, 0.95), (0.14, 0.96)], "paused", "Quận 4")]
    idle = [(0.2, 0.2), (0.32, 0.36), (0.44, 0.14), (0.66, 0.2), (0.8, 0.3), (0.72, 0.4), (0.25, 0.44), (0.88, 0.16), (0.4, 0.3), (0.62, 0.32)]
    pins = [("driver-idle", x, y) for x, y in idle]
    extra = ""
    trips = [((0.3, 0.24), (0.52, 0.24), (0.52, 0.42)), ((0.72, 0.42), (0.72, 0.24), (0.9, 0.24)), ((0.1, 0.42), (0.3, 0.42))]
    for t in trips:
        d = " ".join(("M" if i == 0 else "L") + f" {x*W:.0f} {y*H:.0f}" for i, (x, y) in enumerate(t))
        extra += f'<path d="{d}" fill="none" stroke="#2F2E2E" stroke-width="3" stroke-dasharray="1 0" opacity=".55"/>'
    for (x, y), warn in [((0.52, 0.33), False), ((0.72, 0.3), True), ((0.2, 0.42), False)]:
        cx, cy = x * W, y * H
        ring = f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="22" fill="none" stroke="#E2A33C" stroke-width="3"/>' if warn else ""
        extra += f'{ring}<circle cx="{cx:.0f}" cy="{cy:.0f}" r="13" fill="#0F0E0E" stroke="#FFFFFF" stroke-width="3"/>'
    if sel:
        extra += f'<circle cx="{0.72*W:.0f}" cy="{0.3*H:.0f}" r="30" fill="rgba(226,34,64,.12)" stroke="#E22240" stroke-width="2"/>'
    mp = map_svg(W, H, pins=pins, regions=regs, labels=True, extra_svg=extra)
    legend = (f'<div style="position: absolute; left: 16px; bottom: 16px; background: #FFFFFF; border: 1px solid {C["b2"]}; border-radius: 10px; box-shadow: {SH_MD}; padding: 10px 12px; display: flex; gap: 16px; {TY["cap"]}">'
              f'<span style="display: flex; gap: 6px; align-items: center"><span style="width: 12px; height: 12px; border-radius: 999px; background: #FFFFFF; border: 1px solid #C9C8C6"></span>Rảnh (412)</span>'
              f'<span style="display: flex; gap: 6px; align-items: center"><span style="width: 12px; height: 12px; border-radius: 999px; background: #0F0E0E"></span>Đang chạy (200)</span>'
              f'<span style="display: flex; gap: 6px; align-items: center"><span style="width: 12px; height: 12px; border-radius: 999px; border: 2.5px solid #E2A33C"></span>Kẹt trạng thái (7)</span></div>')
    layers = (f'<div style="position: absolute; top: 16px; left: 16px; display: flex; gap: 8px">{segmented(["Tất cả", "Đi xe", "Đặt món"], 0, False).replace("background: " + C["sunken"], "background: #FFFFFF; box-shadow: " + SH_MD)}'
              f'<button type="button" style="display: inline-flex; align-items: center; gap: 6px; height: 40px; padding: 0 12px; border-radius: 8px; border: 1px solid {C["b2"]}; background: #FFFFFF; box-shadow: {SH_MD}; font-family: {FONT}; font-size: 13px; font-weight: 600">{icon("layers", 16)}Lớp: vùng, tài xế, chuyến</button></div>')
    mapbox = f'<div style="position: relative; width: {W}px; height: {H}px; border-radius: 12px; overflow: hidden; border: 1px solid {C["b2"]}; flex-shrink: 0">{mp}{layers}{legend}</div>'
    stats = col(*[row(txt(k, "bsm", C["t2"], extra="flex-grow: 1; font-size: 14px"), num(v, 16, c, 600), gap=8) for k, v, c in [
        ("Tài xế trực tuyến", "612", None), ("Đang rảnh", "412", None), ("Chuyến/đơn đang chạy", "200", None), ("Đang tìm tài xế", "18", None), ("Chờ xác nhận tiền > 5 phút", "23", C["warn"]), ("Tranh chấp đang mở", "5", C["err"])]], gap=10)
    if sel:
        side = section_card("R-4N7XA · Kẹt trạng thái", pill("proofPending", "Chờ xác nhận tiền 12 phút") + kvs(("Khách", "Trần Bảo Ngọc", False), ("Tài xế", "Lê Văn Tài · 51F-123.45", False), ("Giá", "96.000đ", True), ("Khách gửi chứng từ", "08:31", False))
                            + banner("warning", "Tài xế chưa xác nhận sau 12 phút", "Gọi tài xế hoặc mở hồ sơ hỗ trợ nếu hai bên báo khác nhau.")
                            + row(btn("Mở chi tiết", "secondary", "md", href="A-079.dc.html"), btn("Gọi tài xế", "outline", "md", "phone"), gap=8), extra="width: 300px")
    else:
        side = section_card("Cần chú ý", "".join(row(pill(p, size="sm"), txt(t, "bsm", extra="flex-grow: 1; font-size: 13px"), mono(m, 12, C["t3"]), gap=8) for p, t, m in [
            ("proofPending", "R-4N7XA · chưa xác nhận tiền", "12′"), ("proofPending", "F-8KQ2M · chưa xác nhận tiền", "9′"), ("changeRequested", "F-3M8TP · đề xuất sắp hết giờ", "1′"),
            ("searching", "R-7HH21 · tìm tài xế lượt 3", "1′"), ("issue", "R-1TT90 · báo sự cố an toàn", "4′")]), extra="width: 300px")
    content = (ad.page_head("Bản đồ vận hành trực tiếp", "TP. Hồ Chí Minh · cập nhật mỗi 5 giây · vị trí tài xế ẩn danh khi không có chuyến", acts(btn("Toàn màn hình", "outline", "md", "zoom-in")))
               + row(mapbox, col(section_card("Hiện trạng", stats, extra="width: 300px"), side, gap=16), gap=16, align="flex-start"))
    return admin("live", ["Bản đồ trực tiếp"], content)


@frame("A-077", "Live ops map", G_MON)
def a077():
    return [("Tổng quan", live_map()), ("Chọn chuyến bị kẹt", live_map(True))]


# ================= RIDE LIST / DETAIL =================
RIDE_ROWS = [
    [ad.tbl_link("R-7Q2K9"), mono("08:27"), "Minh Anh", "Trần Văn Hùng", "Xe máy", mono("48.000đ"), pill("completed", size="sm"), muted("Hoàn thành 08:41")],
    [ad.tbl_link("R-4N7XA"), mono("08:24"), "Trần Bảo Ngọc", "Lê Văn Tài", "Ô tô", mono("96.000đ"), pill("proofPending", "PAYMENT_PENDING", "sm"), f'<span style="color: {C["warn"]}; font-weight: 600">Kẹt 12 phút</span>'],
    [ad.tbl_link("R-9KD31"), mono("08:22"), "Lê Tuấn Anh", "Võ Khánh", "Xe máy", mono("35.000đ"), pill("inProgress", "STARTED", "sm"), muted("ETA 08:44")],
    [ad.tbl_link("R-7HH21"), mono("08:21"), "Hoàng Lan", "—", "Xe máy", mono("41.000đ"), pill("matching", "MATCHING", "sm"), muted("Lượt 3/3")],
    [ad.tbl_link("R-2H8QD"), mono("22/09"), "Minh Anh", "Võ Khánh", "Xe máy", mono("32.000đ"), pill("disputed", "PAYMENT_DISPUTED", "sm"), muted("CS-240922-0098")],
    [ad.tbl_link("R-5T1WM"), mono("20/09"), "Minh Anh", "—", "Ô tô", mono("168.000đ"), pill("cancelled", "CANCELED", "sm"), muted("Khách huỷ trước ghép")],
    [ad.tbl_link("R-3PZ84"), mono("08:18"), "Phạm Quân", "Đỗ Quân", "Xe máy", mono("27.000đ"), pill("arrived", "ARRIVED", "sm"), muted("Chờ 02:10")],
]


def ride_list(stuck=False, overlay=""):
    rows = [r for r in RIDE_ROWS if stuck is False or "Kẹt" in r[7] or "MATCHING" in r[6]]
    chips = row(*[tag(t, i == (1 if stuck else 0)) for i, t in enumerate(["Tất cả 1.302", "Kẹt trạng thái 7", "Đang chạy 164", "Tranh chấp 5", "Đã huỷ 38"])], gap=8)
    return admin("trips", ["Chuyến & đơn", "Đi xe"], ad.page_head("Chuyến & đơn", "Theo dõi vòng đời REQUESTED → COMPLETED. Mọi chuyển trạng thái đều có thời điểm và người thực hiện.", acts(btn("Xuất (có lý do)", "outline", "md", "download", href="A-091.dc.html")))
                 + tabs(["Đi xe", "Đặt món"], 0) + chips + filter_bar([("Hôm nay", True), ("Vùng", False), ("Loại xe", False), ("Trạng thái", False)], "Mã chuyến, SĐT, biển số")
                 + table(["Mã", "Tạo lúc", "Khách", "Tài xế", "Loại xe", "Giá", "Trạng thái", "Ghi chú"], rows, ["110px", "80px", "1.2fr", "1.2fr", "90px", "100px", "190px", "1.3fr"], selected=1 if stuck else None), overlay)


@frame("A-078", "Ride trip list", G_MON)
def a078():
    return [("Tất cả", ride_list()), ("Lọc kẹt trạng thái", ride_list(True))]


def ride_detail(state="done"):
    W, H = 600, 260
    mp = map_svg(W, H, route=[(0.82, 0.8), (0.82, 0.42), (0.52, 0.42), (0.52, 0.24), (0.3, 0.24), (0.3, 0.12)], pins=[("pickup", 0.82, 0.8), ("dropoff", 0.3, 0.12)], driver=(0.52, 0.42) if state != "done" else None, labels=False)
    states = [("REQUESTED", "08:26:40", "done"), ("MATCHING · lượt 1", "08:26:41", "done"), ("MATCHED · Trần Văn Hùng nhận", "08:27:05", "done"), ("PAYMENT_PENDING", "08:27:05", "done"),
              ("MONEY_RECEIVED · tài xế xác nhận", "08:16" if False else "08:29:12", "done"), ("DRIVER_EN_ROUTE", "08:29:12", "done"), ("ARRIVED", "08:31:40", "done"), ("STARTED", "08:33:02", "done"), ("COMPLETED", "08:41:18", "done")]
    if state == "dispute":
        states = states[:4] + [("PAYMENT_DISPUTED · tài xế báo chưa nhận", "22/09 18:19", "failed"), ("Chờ kết luận hồ sơ", "CS-240922-0098", "current")]
    tl = timeline([(a, b, c) for a, b, c in states], True)
    pay = section_card("Thanh toán trực tiếp", kvs(("Giá cuối cùng", "48.000đ" if state == "done" else "32.000đ", True), ("Phiên bản chính sách giá", "Giá Đi xe · Xe máy v5", False),
                                                   ("Tài khoản nhận", "VCB ••• 4567 89 · TRAN VAN HUNG", False), ("Chứng từ khách", "Gửi 08:28:40" if state == "done" else "Gửi 18:14", False),
                                                   ("Tài xế xác nhận", "08:29:12" if state == "done" else "Báo chưa nhận 18:19", False))
                       + row(f'<div style="filter: blur(6px)">{photo(120, 90, "", "image", 8)}</div>', col(txt("Ảnh chứng từ bị ẩn", "lbl"), txt("Chỉ xem khi gắn với hồ sơ khiếu nại (RBAC).", "cap", C["t3"]), btn("Xem có lý do", "outline", "sm", "eye", href="A-064.dc.html"), gap=4), gap=12))
    people = section_card("Các bên", row(avatar("MA", 40), col(txt("Nguyễn Minh Anh", "lbl", extra="font-size: 14px"), mono("0901 ••• 567", 12, C["t3"]), gap=2), spacer(), btn("Hồ sơ", "ghost", "sm", href="A-073.dc.html"), gap=10)
                          + row(avatar("TH", 40), col(txt("Trần Văn Hùng · 4,9★", "lbl", extra="font-size: 14px"), mono("59-X2 123.45", 12, C["t3"]), gap=2), spacer(), btn("Hồ sơ", "ghost", "sm", href="A-083.dc.html"), gap=10))
    links = section_card("Liên quan", list_row("Chat của chuyến (14 tin, 1 ảnh)", "Lưu 7 ngày · còn 6 ngày", "message", href="A-082.dc.html", pad="10px 0")
                         + (list_row("CS-240922-0098 · Tranh chấp thanh toán", "Đang xem xét", "scale", href="A-051.dc.html", pad="10px 0", border=False) if state == "dispute" else list_row("Đánh giá của khách", "5★ · Đúng giờ, Lái xe an toàn", "star", chevron=False, pad="10px 0", border=False)))
    head = ad.page_head("R-7Q2K9" if state == "done" else "R-2H8QD", "Xe máy · Quận 1 → Quận 3 · 3,2 km · 14 phút", acts(btn("Tạo hồ sơ hỗ trợ", "outline", "md", "plus"), btn("Ghi chú nội bộ", "ghost", "md", "pencil")),
                        pill("completed") if state == "done" else pill("disputed", "PAYMENT_DISPUTED"))
    left = col(f'<div style="height: {H}px; border-radius: 12px; overflow: hidden; border: 1px solid {C["b2"]}">{mp}</div>', pay, gap=16, extra=f"width: {W}px; flex-shrink: 0")
    right = col(people, section_card("Vòng đời chuyến (F-010)", tl), links, gap=16, extra="flex-grow: 1")
    return admin("trips", ["Chuyến & đơn", "Đi xe", "R-7Q2K9" if state == "done" else "R-2H8QD"], head + row(left, right, gap=16, align="flex-start"))


@frame("A-079", "Ride trip detail", G_MON)
def a079():
    return [("Hoàn thành", ride_detail()), ("Tranh chấp thanh toán", ride_detail("dispute"))]


FOOD_ROWS = [
    [ad.tbl_link("F-3M8TP"), mono("11:00"), "Cơm Tấm Sà Bì · NT", "Minh Anh", "Lê Quốc Bảo", mono("137.000đ"), pill("changeRequested", "CHANGE_PROPOSED", "sm"), f'<span style="color: {C["warn"]}; font-weight: 600">Hết giờ sau 01:12</span>'],
    [ad.tbl_link("F-8KQ2M"), mono("10:58"), "Phở Gánh 1975", "Tuấn Anh", "Phạm Tú", mono("94.000đ"), pill("proofPending", "PAYMENT_PENDING", "sm"), f'<span style="color: {C["warn"]}; font-weight: 600">Kẹt 9 phút</span>'],
    [ad.tbl_link("F-2BC71"), mono("10:51"), "Trà Sữa Mây", "Bảo Ngọc", "Võ Khánh", mono("86.000đ"), pill("delivering", "DELIVERING", "sm"), muted("ETA 11:20")],
    [ad.tbl_link("F-1ZX09"), mono("10:47"), "Cơm Tấm Sà Bì · VVT", "Hoàng Lan", "Đỗ Quân", mono("72.000đ"), pill("atOutlet", "ORDERED_AT_OUTLET", "sm"), muted("Không huỷ hoàn tiền")],
    [ad.tbl_link("F-7RT55"), mono("10:30"), "Bánh Mì Cô Ba", "Phạm Quân", "—", mono("45.000đ"), pill("cancelled", "CANCELED", "sm"), muted("Quán đóng cửa")],
]


@frame("A-080", "Food order list", G_MON)
def a080():
    chips = row(*[tag(t, i == 0) for i, t in enumerate(["Tất cả 436", "Có đề xuất 9", "Kẹt trạng thái 3", "Đang giao 61", "Đã huỷ 12"])], gap=8)
    return [("Tất cả", admin("trips", ["Chuyến & đơn", "Đặt món"], ad.page_head("Chuyến & đơn", "Đơn món: ảnh chụp thực đơn lúc đặt, đề xuất thay đổi và mốc đã đặt món tại quán.")
                                + tabs(["Đi xe", "Đặt món"], 1) + chips + filter_bar([("Hôm nay", True), ("Quán", False), ("Trạng thái", False)], "Mã đơn, SĐT, quán")
                                + table(["Mã", "Tạo lúc", "Quán", "Khách", "Tài xế", "Tổng", "Trạng thái", "Ghi chú"], FOOD_ROWS, ["100px", "70px", "1.4fr", "1fr", "1fr", "100px", "190px", "1.3fr"])))]


def food_detail(state="proposal"):
    items = table(["Món", "Ảnh chụp lúc đặt", "Thực tế tại quán", "Trạng thái"],
                  [["2 × Cơm tấm sườn bì chả", mono("110.000đ"), mono("120.000đ"), pill("changeRequested", "Chờ khách" if state == "proposal" else "Khách đồng ý", "sm") if state == "proposal" else pill("confirmed", "Khách đồng ý", "sm")],
                   ["1 × Trà đá", mono("5.000đ"), mono("5.000đ"), pill("approved", "Khớp", "sm")]], ["1.6fr", "130px", "130px", "130px"])
    money = kvs(("Tiền món (lúc đặt)", "115.000đ", True), ("Phí giao (chính sách v4)", "22.000đ", True), ("Khách đã chuyển", "137.000đ", True), ("Bổ sung đề xuất", "+10.000đ" + (" (chờ)" if state == "proposal" else " (đã nhận)"), True))
    props = timeline([("Tài xế gửi đề xuất: giá khác", "11:14 · ảnh bảng giá đính kèm", "done"),
                      ("Khách trả lời", "Hết giờ lúc 11:19" if state == "proposal" else "Đồng ý 11:16", "current" if state == "proposal" else "done"),
                      ("Khách chuyển bổ sung 10.000đ", "", "todo" if state == "proposal" else "done"), ("Tài xế mua phần thay đổi", "", "todo" if state == "proposal" else "done")], True)
    life = timeline([("REQUESTED", "11:00", "done"), ("MATCHED · Lê Quốc Bảo", "11:02", "done"), ("MONEY_RECEIVED", "11:05", "done"), ("DRIVER_AT_OUTLET", "11:12", "done"),
                     ("CHANGE_PROPOSED", "11:14", "current" if state == "proposal" else "done")] + ([] if state == "proposal" else [("ORDERED_AT_OUTLET", "11:20 · ảnh hoá đơn 120.000đ", "done"), ("PICKED_UP", "11:31", "done"), ("DELIVERED", "11:46", "done")]), True)
    left = col(section_card("Món & ảnh chụp thực đơn", items + row(photo(140, 100, "Ảnh bảng giá tại quán", "image", 8), photo(140, 100, "Ảnh hoá đơn" if state != "proposal" else "Chưa có hoá đơn", "file", 8), gap=10)),
               row(section_card("Tiền", money, extra="flex: 1"), section_card("Đề xuất thay đổi (UF-003)", props, extra="flex: 1"), gap=16, align="flex-start"), gap=16, extra="width: 760px; flex-shrink: 0")
    right = col(section_card("Vòng đời đơn", life),
                section_card("Liên quan", list_row("Chat của đơn", "9 tin · lưu 7 ngày", "message", href="A-082.dc.html", pad="10px 0") + list_row("Quán Sà Bì — Nguyễn Trãi", "5 đề xuất giá lệch trong 7 ngày", "store", href="A-047.dc.html", pad="10px 0", border=False)), gap=16, extra="flex-grow: 1")
    head = ad.page_head("F-3M8TP", "Cơm Tấm Sà Bì — Nguyễn Trãi → 142 Lê Văn Sỹ · tài xế Lê Quốc Bảo", acts(btn("Tạo hồ sơ hỗ trợ", "outline", "md", "plus")),
                        pill("changeRequested", "CHANGE_PROPOSED") if state == "proposal" else pill("completed", "DELIVERED"))
    warn = banner("warning", "Đề xuất hết giờ sau 01:12", "Nếu khách không trả lời, đơn chuyển vào hàng đợi vận hành để Ops quyết định huỷ hay giao phần còn lại (OQ-023).") if state == "proposal" else ""
    return admin("trips", ["Chuyến & đơn", "Đặt món", "F-3M8TP"], head + warn + row(left, right, gap=16, align="flex-start"))


@frame("A-081", "Food order detail", G_MON)
def a081():
    return [("Đang có đề xuất", food_detail()), ("Đã giao", food_detail("done"))]


@frame("A-082", "Case-linked chat transcript", G_MON)
def a082():
    def m(who, t, time, me=False, img=False):
        bg = C["sunken"] if not me else C["info_bg"]
        content = photo(180, 120, "Ảnh chứng từ (ẩn)", "image", 8) if img else f'<span style="{TY["bsm"]}; font-size: 14px">{t}</span>'
        return (f'<div style="display: flex; gap: 10px; align-items: flex-start">{avatar("MA" if who == "Khách" else "TH", 28)}<div style="display: flex; flex-direction: column; gap: 4px">'
                f'<span style="{TY["cap"]}; color: {C["t3"]}"><b style="color: {C["t1"]}">{who}</b> · {time} · đã xem</span><div style="padding: 10px 12px; border-radius: 10px; background: {bg}; max-width: 520px">{content}</div></div></div>')
    msgs = (m("Khách", "Chào bạn, mình đứng ở cổng Hải Triều, áo xanh nhé.", "18:12") + m("Tài xế", "Dạ 2 phút nữa em tới. Anh chuyển khoản giúp em trước nha.", "18:13", True)
            + m("Khách", "", "18:14", img=True) + m("Tài xế", "Em chưa thấy tiền về anh ơi, anh kiểm tra lại giúp em.", "18:19", True) + m("Khách", "Mình chuyển rồi mà, có ảnh đó.", "18:20"))
    side = col(section_card("Phiên xem", kvs(("Hồ sơ", "CS-240922-0098", True), ("Lý do xem", "Xử lý tranh chấp thanh toán", False), ("Người xem", "Minh Khoa · Risk", False), ("Ghi audit", "18:40:12", False))),
               section_card("Lưu trữ", banner("info", "Đã giữ lại làm bằng chứng", "Chat thường xoá sau 7 ngày. Chat gắn hồ sơ được giữ đến khi hồ sơ kết luận.") + kvs(("Tin nhắn", "14", False), ("Ảnh", "1", False))), gap=16, extra="width: 340px; flex-shrink: 0")
    body_ = row(f'<div style="flex-grow: 1; background: #FFFFFF; border: 1px solid {C["b2"]}; border-radius: 12px; padding: 20px; display: flex; flex-direction: column; gap: 16px">{row(txt("R-2H8QD · Minh Anh ↔ Võ Khánh", "hsm"), spacer(), pill("locked", "Chỉ đọc", "sm"))}{msgs}</div>', side, gap=16, align="flex-start")
    return [("Chỉ đọc, gắn hồ sơ", admin("case", ["Khiếu nại & gian lận", "CS-240922-0098", "Chat"], ad.page_head("Lịch sử chat của chuyến", "Chỉ mở được từ hồ sơ khiếu nại/tranh chấp. Không chỉnh sửa, không xoá.") + body_))]


# ================= DRIVER PERFORMANCE / DOC CONFIG =================
@frame("A-083", "Driver performance & ratings", "Tài xế · Duyệt & quản lý")
def a083():
    dist = col(*[row(txt(f"{s}★", "bsm", extra="width: 28px"), f'<div style="flex-grow: 1">{progress(p)}</div>', mono(f"{p}%", 12, C["t3"]), gap=10) for s, p in [(5, 86), (4, 9), (3, 3), (2, 1), (1, 1)]], gap=8)
    reviews = "".join(row(stars(5, s, 14), txt(t, "bsm", extra="flex-grow: 1; font-size: 14px"), mono(d, 12, C["t3"]), gap=12, extra=f"padding: 10px 0; border-bottom: 1px solid {C['b1']}")
                      for s, t, d in [(5, "Đúng giờ · Lái xe an toàn", "24/09"), (5, "Thân thiện", "23/09"), (3, "Đến trễ 5 phút", "22/09"), (5, "Biết đường", "22/09")])
    content = (row(avatar("TH", 56), col(row(txt("Trần Văn Hùng", "hmd", extra="font-size: 20px"), pill("active", size="sm"), pill("active", "Phí đến 03/2028", "sm"), gap=8), mono("DRV-000611 · 0901 234 567 · Honda Vision 59-X2 123.45", 13, C["t3"]), gap=4), spacer(),
                   btn("Khoá tài xế", "danger", "md", "lock", href="A-035.dc.html"), btn("Sửa dịch vụ", "outline", "md", href="A-034.dc.html"), gap=12)
               + tabs(["Hồ sơ", "Giấy tờ", "Hiệu suất", "Đánh giá", "Rủi ro", "Phí nền tảng", "Audit"], 2)
               + row(ad.stat("Tỷ lệ nhận chuyến", "78%", "", "30 ngày · 412/528 offer"), ad.stat("Tỷ lệ huỷ sau nhận", "1,9%", "", "8 chuyến"), ad.stat("Đánh giá TB", "4,9", "", "1.204 lượt"),
                     ad.stat("Khiếu nại hợp lệ", "1", "", "ngưỡng khoá: 3/30 ngày"), ad.stat("Giờ trực tuyến", "142h", "", "30 ngày"), gap=12)
               + row(section_card("Chuyến/đơn 14 ngày", bar_chart([18, 22, 14, 25, 30, 12, 9, 21, 26, 28, 31, 24, 19, 27], [str(i) for i in range(11, 25)], 13), extra="flex: 2"),
                     section_card("Phân bố đánh giá", dist, extra="flex: 1"), gap=16, align="flex-start")
               + section_card("Đánh giá gần đây", reviews))
    return [("Hiệu suất & đánh giá", admin("driver", ["Tài xế", "Trần Văn Hùng"], content))]


@frame("A-084", "Document requirement config", "Tài xế · Duyệt & quản lý")
def a084():
    Y = icon("check", 16, C["ok"], 2.5)
    O = muted("Tuỳ chọn")
    N = muted("—")
    rows = [["CCCD 2 mặt", Y, Y, Y, mono("Không"), muted("Hết hạn theo giấy")], ["Ảnh chân dung cầm CCCD", Y, Y, Y, mono("Không"), muted("—")],
            ["GPLX hạng A1", Y, N, Y, mono("Có"), muted("Nhắc trước 30 ngày")], ["GPLX hạng B", N, Y, N, mono("Có"), muted("Nhắc trước 30 ngày")],
            ["Đăng ký xe (cà vẹt)", Y, Y, Y, mono("Không"), muted("Biển số phải khớp")], ["Bảo hiểm TNDS", Y, Y, Y, mono("Có"), muted("Nhắc trước 30 ngày")],
            ["Lý lịch tư pháp", O, O, O, mono("Không"), muted("Bật khi luật yêu cầu")], ["Đăng kiểm ô tô", N, Y, N, mono("Có"), muted("Nhắc trước 30 ngày")]]
    content = (ad.page_head("Giấy tờ bắt buộc theo phương tiện & dịch vụ", "Tài xế thấy đúng danh sách này khi đăng ký (D-005). Thay đổi áp dụng cho hồ sơ nộp sau khi xuất bản.", acts(btn("Thêm loại giấy tờ", "outline", "md", "plus"), btn("Xuất bản", "primary", "md", "upload")), pill("draft", "Bản nháp v3"))
               + table(["Giấy tờ", "Xe máy · Đi xe", "Ô tô · Đi xe", "Xe máy · Đặt món", "Có hạn dùng", "Ghi chú"], rows, ["1.6fr", "130px", "130px", "150px", "110px", "1.4fr"])
               + banner("info", "Phí hồ sơ 500.000đ chưa áp dụng", "Chương trình ra mắt đang miễn phí hồ sơ. Khi áp dụng, phí thu lúc nộp hồ sơ (BR-DRV-FEE-002) — cấu hình ở Giá & chính sách."))
    return [("Ma trận giấy tờ", admin("driver", ["Tài xế", "Cấu hình giấy tờ"], content))]


# ================= RISK SIGNALS =================
RISK_ROWS = [
    [pill("issue", "Cao", "sm"), mono("PROOF_HASH_REUSED"), "Khách · Trần Bảo Ngọc", muted("Ảnh chứng từ trùng với CS-240918-0051"), mono("08:33"), pill("pendingReview", "Mới", "sm")],
    [pill("issue", "Cao", "sm"), mono("GPS_IMPOSSIBLE_JUMP"), "Tài xế · Đỗ Quân", muted("Nhảy 18 km trong 6 giây"), mono("08:12"), pill("pendingReview", "Mới", "sm")],
    [pill("paused", "Trung bình", "sm"), mono("MULTI_ACCOUNT_DEVICE"), "Thiết bị · d_9f2c…a41e", muted("3 tài khoản khách trên 1 thiết bị"), mono("07:50"), pill("pendingReview", "Đang xem", "sm")],
    [pill("paused", "Trung bình", "sm"), mono("OTP_ABUSE"), "SĐT · 0939 ••• 120", muted("Chạm giới hạn 5 OTP/giờ 3 lần"), mono("07:41"), pill("cancelled", "Bỏ qua", "sm")],
    [pill("neutral", "Thấp", "sm"), mono("CANCEL_AFTER_PAY"), "Khách · Lê Tuấn Anh", muted("2 lần huỷ sau khi chuyển tiền / 7 ngày"), mono("23/09"), pill("finalized", "Đã tạo hồ sơ", "sm")]]


def risk_list(overlay=""):
    content = (ad.page_head("Tín hiệu rủi ro", "Tín hiệu theo reason code, không tự kết luận vi phạm. Người xem quyết định bỏ qua hoặc tạo hồ sơ.", acts(btn("Cấu hình ngưỡng", "outline", "md", "sliders", href="A-026.dc.html")))
               + row(ad.stat("Tín hiệu mới", "4"), ad.stat("Đang xem", "1"), ad.stat("Chuyển thành hồ sơ 7 ngày", "6"), ad.stat("Bỏ qua 7 ngày", "11"), gap=16)
               + filter_bar([("Mức độ", False), ("Reason code", False), ("Đối tượng", False)], "Mã thiết bị, SĐT, tên")
               + table(["Mức độ", "Reason code", "Đối tượng", "Chi tiết", "Lúc", "Trạng thái"], RISK_ROWS, ["120px", "200px", "1.3fr", "1.8fr", "80px", "150px"], selected=2 if overlay else None))
    return admin("risk", ["Tín hiệu rủi ro"], content, overlay)


@frame("A-085", "Risk signal queue", G_RISK)
def a085():
    return [("Danh sách tín hiệu", risk_list())]


@frame("A-086", "Device identity detail", G_RISK)
def a086():
    accts = table(["Tài khoản", "Loại", "Lần cuối", "Rủi ro"], [["Lê Tuấn Anh", "Khách", mono("24/09"), pill("pendingReview", "Theo dõi", "sm")], ["Lê T. Anh 2", "Khách", mono("23/09"), pill("pendingReview", "Theo dõi", "sm")], ["Anh Lê", "Khách", mono("21/09"), pill("active", "Bình thường", "sm")]], ["1.4fr", "80px", "90px", "120px"])
    inner = (kvs(("Mã thiết bị (đã băm)", "d_9f2c…a41e", True), ("Nền tảng", "Android 14 · Onway 1.1.0", False), ("Lần đầu thấy", "19/09/2026", False))
             + txt("Tài khoản dùng thiết bị này", "lbl") + accts
             + txt("Dòng thời gian tín hiệu", "lbl") + timeline([("MULTI_ACCOUNT_DEVICE", "24/09 07:50 · tài khoản thứ 3", "current"), ("CANCEL_AFTER_PAY", "23/09 19:02", "done"), ("Đăng nhập tài khoản mới", "21/09 08:15", "done")], True)
             + field("Lý do quyết định (bắt buộc)", "", "VD: Thiết bị dùng chung trong gia đình, đã gọi xác minh", textarea=True)
             + txt("Dữ liệu thiết bị lưu 12 tháng, 5 năm nếu gắn hồ sơ gian lận/khiếu nại.", "cap", C["t3"]))
    return [("Tài khoản liên kết & quyết định", risk_list(drawer("Thiết bị d_9f2c…a41e", inner, btn("Bỏ qua", "ghost", "md") + btn("Tạo hồ sơ gian lận", "danger", "md", "shield-alert", href="A-055.dc.html"), 600, pills=pill("paused", "Trung bình"))))]


# ================= REFUNDS / CONSENT =================
def refund_queue(overlay=""):
    rows = [[ad.tbl_link("RF-241003-0004"), row(avatar("PM", 28), "Phạm Minh"), mono("12/09/2026"), "Quý 2", mono("500.000đ"), pill("pendingReview", "Chờ duyệt", "sm")],
            [ad.tbl_link("RF-240930-0002"), row(avatar("NT", 28), "Nguyễn Thị Thu"), mono("15/07/2026"), "Quý 1", mono("750.000đ"), pill("approved", "Đã duyệt · chờ chuyển", "sm")],
            [ad.tbl_link("RF-240921-0001"), row(avatar("DQ", 28), "Đỗ Quân"), mono("10/09/2025"), "Quý 4", mono("0đ"), pill("cancelled", "Không hoàn (đã vào quý 4)", "sm")]]
    content = (ad.page_head("Hoàn phí nền tảng", "Hoàn theo quý chưa bắt đầu của 12 tháng trả phí. 6 tháng tặng không hoàn. Onway chỉ xử lý khoản Onway thu.")
               + tabs(["Chứng từ phí", "Yêu cầu hoàn phí"], 1) + table(["Mã", "Tài xế", "Ngày kích hoạt", "Đang ở", "Số tiền hoàn", "Trạng thái"], rows, ["160px", "1.4fr", "130px", "100px", "130px", "1.4fr"], selected=0 if overlay else None))
    return admin("finance", ["Phí nền tảng & hoàn phí"], content, overlay)


@frame("A-087", "Platform fee refund", "Tài chính & khách hàng")
def a087():
    qs = row(*[f'<div style="flex: 1; padding: 10px; border-radius: 8px; text-align: center; background: {bg}; border: 1px solid {C["b2"]}"><div style="{TY["lbl"]}">{q}</div><div style="{TY["cap"]}; color: {C["t3"]}">{d}</div><div style="font-family: {MONO}; font-size: 13px; font-weight: 600; margin-top: 4px">{v}</div></div>'
               for q, d, v, bg in [("Q1", "12/09–11/12", "Đã dùng", C["sunken"]), ("Q2", "12/12–11/03", "Đang dùng", C["warn_bg"]), ("Q3", "12/03–11/06", "250.000đ", C["ok_bg"]), ("Q4", "12/06–11/09", "250.000đ", C["ok_bg"])]], gap=8)
    inner = (kvs(("Tài xế", "Phạm Minh · DRV-000702", False), ("Đã trả", "1.000.000đ · FEE-240912-0201", True), ("Ngày yêu cầu", "03/10/2026 — đang ở Quý 2", False))
             + txt("Tính hoàn phí (quý đã bước vào xem như đã dùng)", "lbl") + qs + row(txt("6 tháng tặng", "bsm", C["t2"], extra="flex-grow: 1"), muted("Không hoàn"))
             + divider() + row(txt("Số tiền hoàn", "hsm", extra="flex-grow: 1"), num("500.000đ", 22, weight=700))
             + field("Tài khoản nhận hoàn", "VCB ••• 2201 · PHAM MINH", disabled=True) + field("Mã giao dịch chuyển hoàn (sau khi chuyển)", "", "FT…", mono=True)
             + field("Lý do / ghi chú (bắt buộc)", "Tài xế dừng hoạt động theo yêu cầu.", textarea=True)
             + banner("warning", "Tài khoản sẽ ngừng kích hoạt", "Duyệt hoàn phí đồng thời kết thúc gói và chuyển tài xế sang Ngừng hoạt động."))
    return [("Hàng đợi", refund_queue()), ("Chi tiết & tính hoàn", refund_queue(drawer("RF-241003-0004", inner, btn("Từ chối", "danger", "md") + btn("Duyệt hoàn 500.000đ", "primary", "md", "check"), 600, pills=pill("pendingReview", "Chờ duyệt"))))]


@frame("A-088", "Terms & consent versions", "Tài chính & khách hàng")
def a088():
    rows = [[mono("location.background"), "Tài xế", mono("v2"), pill("published", size="sm"), mono("1.940 / 1.940"), muted("24/09 · Super Admin")],
            [mono("device.risk"), "Khách, Tài xế", mono("v2"), pill("published", size="sm"), mono("38.102 / 38.410"), muted("24/09 · Super Admin")],
            [mono("evidence.upload"), "Khách, Tài xế", mono("v1"), pill("published", size="sm"), mono("38.410 / 38.410"), muted("10/09 · Super Admin")],
            [mono("phone.visibility"), "Khách", mono("v1"), pill("published", size="sm"), mono("36.220 / 36.470"), muted("10/09 · Super Admin")],
            [mono("terms.customer"), "Khách", mono("v3"), pill("draft", size="sm"), mono("—"), muted("Chờ legal review")]]
    preview = section_card("Bản nháp · terms.customer v3", txt("Thay đổi so với v2: bổ sung mục “Tạm khoá tài khoản” và thời hạn lưu chat 7 ngày.", "bsm", C["t2"])
                           + switch(True, "Bắt người dùng đồng ý lại", "Hiện màn đồng ý khi mở ứng dụng lần tới") + field("Lý do xuất bản (bắt buộc)", "", textarea=True)
                           + row(btn("Xem khác biệt", "outline", "md", "diff"), btn("Xuất bản", "disabled", "md"), gap=8) + txt("Cần legal duyệt trước khi xuất bản.", "cap", C["t3"]), extra="width: 420px; flex-shrink: 0")
    content = (ad.page_head("Điều khoản & đồng ý", "Mỗi lần đồng ý lưu kèm phiên bản (ConsentRecord). Chỉ Super Admin xuất bản.") + tabs(["Phiên bản đồng ý", "Yêu cầu dữ liệu"], 0)
               + row(f'<div style="flex-grow: 1">{table(["Loại đồng ý", "Áp dụng", "Phiên bản", "Trạng thái", "Đã đồng ý", "Cập nhật"], rows, ["1.4fr", "120px", "80px", "110px", "140px", "1.2fr"], selected=4)}</div>', preview, gap=16, align="flex-start"))
    return [("Phiên bản & xuất bản", admin("privacy", ["Dữ liệu & đồng ý"], content))]


# ================= SYSTEM =================
@frame("A-089", "App version / force update config", "Bằng chứng, audit & hệ thống")
def a089():
    import landing, driver as dr
    PREVIEW_SC = section_card("Xem trước trên điện thoại", row(landing.device(dr.d000()[1][1], 0.42, False), txt("Màn D-000 · Bắt buộc cập nhật: tài xế thấy thông báo bên cạnh và nút Cập nhật ngay, không bỏ qua được.", "bsm", C["t2"], extra="max-width: 280px"), gap=20, align="center"))
    rows = [["Khách", "iOS", mono("1.1.0"), mono("1.0.3"), pill("active", "Bật", "sm"), mono("97,4%")], ["Khách", "Android", mono("1.1.0"), mono("1.0.3"), pill("active", "Bật", "sm"), mono("95,1%")],
            ["Tài xế", "iOS", mono("1.1.0"), mono("1.1.0"), pill("issue", "Bắt buộc", "sm"), mono("88,0%")], ["Tài xế", "Android", mono("1.1.0"), mono("1.1.0"), pill("issue", "Bắt buộc", "sm"), mono("91,6%")]]
    form = section_card("Onway Tài xế · Android", field("Phiên bản mới nhất", "1.1.0", mono=True) + field("Phiên bản tối thiểu", "1.1.0", mono=True)
                        + switch(True, "Bắt buộc cập nhật dưới phiên bản tối thiểu", "Tài xế bản cũ không thể trực tuyến")
                        + field("Thông báo hiển thị", "Bản Onway Tài xế 1.0.4 không còn nhận chuyến. Cập nhật lên 1.1.0 để tiếp tục trực tuyến.", textarea=True)
                        + field("Lý do (bắt buộc)", "Sửa lỗi xác nhận thanh toán trên Android 14.", textarea=True) + row(btn("Huỷ", "ghost", "md"), spacer(), btn("Xuất bản", "primary", "md", "upload"), gap=8), extra="width: 440px; flex-shrink: 0")
    content = (ad.page_head("Phiên bản ứng dụng", "Ứng dụng gọi getAppVersionPolicy khi mở. 8,4% tài xế Android còn dùng bản dưới 1.1.0.")
               + row(f'<div style="flex-grow: 1; display: flex; flex-direction: column; gap: 16px">{table(["Ứng dụng", "Nền tảng", "Mới nhất", "Tối thiểu", "Bắt buộc", "Đã cập nhật"], rows, ["1.3fr", "100px", "100px", "100px", "120px", "120px"], selected=3)}'
                     f'{PREVIEW_SC}</div>', form, gap=16, align="flex-start"))
    return [("Cấu hình theo app/nền tảng", admin("appver", ["Phiên bản ứng dụng"], content))]


@frame("A-090", "Invite admin user", "Bằng chứng, audit & hệ thống")
def a090():
    inner = (field("Email công việc", "minh.tran@onway.vn") + field("Họ tên", "Trần Quang Minh") + select("Vai trò", "Support Operator")
             + select("Phạm vi", "TP. Hồ Chí Minh") + checkbox("Bắt buộc xác minh hai bước", True, "Bắt buộc với vai trò có quyền xuất bản hoặc xem bằng chứng")
             + select("Hết hạn lời mời", "72 giờ") + txt("Chỉ Super Admin mời được quản trị viên. Lời mời và vai trò được ghi audit.", "cap", C["t3"]))
    return [("Mời có vai trò & phạm vi", ad.rbac_list(admin_dialog("Mời quản trị viên", inner, btn("Huỷ", "ghost", "md") + btn("Gửi lời mời", "primary", "md", "send"), 560)))]


@frame("A-091", "Controlled data export", "Bằng chứng, audit & hệ thống")
def a091():
    inner = (select("Dữ liệu", "Chuyến Đi xe · 01/09–24/09") + txt("Trường xuất", "lbl") + checkbox("Mã chuyến, thời gian, trạng thái, giá", True)
             + checkbox("Vùng, loại xe", True) + checkbox("SĐT khách/tài xế (che 4 số giữa)", True) + checkbox("SĐT đầy đủ", False, "Cần Super Admin duyệt")
             + field("Lý do (bắt buộc)", "Đối soát số chuyến với báo cáo vận hành tháng 9.", textarea=True)
             + banner("info", "File chỉ tải được 1 lần trong 24 giờ", "Có watermark người xuất; lượt xuất ghi vào nhật ký audit."))
    return [("Phạm vi, che dữ liệu, lý do", ride_list(overlay=admin_dialog("Xuất dữ liệu", inner, btn("Huỷ", "ghost", "md") + btn("Tạo file xuất", "secondary", "md", "download"), 560)))]


@frame("A-092", "Abuse limits & blocked identities", "Bằng chứng, audit & hệ thống")
def a092():
    lim = table(["Giới hạn", "Giá trị", "Phạm vi"], [["Gửi OTP", mono("5 / giờ"), "Số điện thoại"], ["Gửi OTP", mono("10 / ngày"), "Thiết bị"], ["Nhập OTP sai", mono("5 / mã"), "Mã OTP"], ["Gửi vị trí tài xế", mono("5s · 2s khi chạy"), "Tài xế"]], ["1.2fr", "1fr", "1fr"])
    blk = table(["Đối tượng", "Lý do", "Đến", ""], [[mono("0939 ••• 120"), muted("OTP_ABUSE"), mono("24/09 08:41"), btn("Gỡ chặn", "ghost", "sm")], [mono("d_44ab…0c1f"), muted("OTP 10/ngày"), mono("25/09 00:00"), btn("Gỡ chặn", "ghost", "sm")],
                                                    [mono("113.161.x.x"), muted("Mutation burst"), mono("24/09 09:10"), btn("Gỡ chặn", "ghost", "sm")]], ["1fr", "1fr", "120px", "100px"])
    content = (ad.page_head("Giới hạn & chống lạm dụng", "Giới hạn do kỹ thuật cấu hình (G4). Ops chỉ xem và gỡ chặn có lý do khi người dùng thật bị ảnh hưởng.")
               + row(section_card("Giới hạn đang áp dụng", lim, extra="flex: 1"), section_card("Đang bị chặn tạm", blk + txt("Gỡ chặn cần lý do và được ghi audit.", "cap", C["t3"]), extra="flex: 1"), gap=16, align="flex-start"))
    return [("Giới hạn & gỡ chặn", admin("health", ["Sức khoẻ hệ thống", "Chống lạm dụng"], content))]


# ================= RICHER VERSIONS OF THIN FRAMES =================
def queue_page():
    def qcol(title, n, tone, items):
        cards = "".join(card(row(pill(p, size="sm"), spacer(), f'<span style="font-family: {MONO}; font-size: 12px; white-space: nowrap; color: {C["err"] if "Quá" in t else C["t3"]}">{t}</span>') + txt(a, "bsm", extra="font-weight: 600; font-size: 14px") + txt(b, "cap", C["t3"])
                             + row(btn(cta, "outline", "sm", href=h_), spacer(), avatar(ow, 24) if ow else txt("Chưa nhận", "cap", C["t3"], extra="white-space: nowrap"), gap=8), pad=12, gap=6) for p, t, a, b, cta, h_, ow in items)
        return (f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 10px; background: {C["sunken"]}; border-radius: 12px; padding: 12px">'
                f'{row(txt(title, "lbl", extra="font-size: 14px"), badge(n, tone), spacer(), ibtn("more", "Tuỳ chọn", "ghost", 28))}{cards}</div>')
    cols_ = row(qcol("Khoá tự động", 3, "brand", [("issue", "Quá SLA 2h", "Lê Văn Tài", "3 khiếu nại hợp lệ / 30 ngày", "Xem xét", "A-036.dc.html", ""), ("appeal", "còn 9h", "Võ Khánh", "Kháng nghị đã gửi", "Mở kháng nghị", "A-037.dc.html", "MK")]),
                qcol("Thanh toán kẹt", 5, "brand", [("proofPending", "12′", "R-4N7XA · 96.000đ", "Tài xế chưa xác nhận", "Mở chuyến", "A-079.dc.html", ""), ("proofPending", "9′", "F-8KQ2M · 94.000đ", "Chưa gửi chứng từ", "Mở đơn", "A-081.dc.html", "HY")]),
                qcol("Đề xuất Food hết giờ", 1, "ink", [("expired", "1′", "F-3M8TP", "Khách chưa trả lời đề xuất +10.000đ", "Quyết định", "A-081.dc.html", "")]),
                qcol("Hồ sơ tài xế", 42, "ink", [("pendingReview", "1 ngày", "Nguyễn Thị Thu", "Xe máy · Ride", "Duyệt", "A-030.dc.html", "QH"), ("pendingReview", "6h", "Hồ Văn Lực", "Ô tô · Ride", "Duyệt", "A-030.dc.html", "")]),
                qcol("Phí nền tảng", 8, "ink", [("proofPending", "Quá 1h", "FEE-240924-0329", "Nguyễn Thị Thu · 1.000.000đ", "Đối soát", "A-071.dc.html", "TH")]), gap=12, align="flex-start")
    return admin("queue", ["Hàng đợi vận hành"], ad.page_head("Hàng đợi vận hành", "Mọi việc cần người xử lý, sắp theo SLA. Nhận việc để người khác không làm trùng.", acts(segmented(["Của tôi", "Tất cả"], 1, False))) + cols_)


def a007_rich():
    empty = admin("queue", ["Hàng đợi vận hành"], ad.page_head("Hàng đợi vận hành") + card(empty_state("inbox", "Không có việc tồn", "Tất cả hàng đợi đang trong SLA. Việc mới sẽ hiện ở đây theo thời gian thực."), pad=64))
    return [("Có việc tồn (bảng theo SLA)", queue_page()), ("Không có việc", empty)]


from reg import REG as _R
for _f in _R:
    if _f["id"] == "A-007":
        _f["fn"] = a007_rich
