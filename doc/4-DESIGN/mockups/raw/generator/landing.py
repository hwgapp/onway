from lib import *
from reg import frame

LW = 1440


def nav(active=""):
    links = "".join(f'<a href="#" style="text-decoration: none; color: {C["t1"] if l == active else C["t2"]}; {TY["lbl"]}; font-size: 14px">{l}</a>' for l in ["Đi xe", "Đặt món", "Tài xế", "Cách hoạt động", "Hỏi đáp"])
    return (f'<header style="height: 72px; display: flex; align-items: center; gap: 40px; padding: 0 80px; border-bottom: 1px solid {C["b1"]}; background: #FFFFFF; flex-shrink: 0">{logo_img(28)}'
            f'<nav aria-label="Điều hướng" style="display: flex; gap: 28px; flex-grow: 1">{links}</nav>{btn("Đăng ký tài xế", "outline", "md")}{btn("Tải ứng dụng", "primary", "md", "download")}</header>')


def page(inner, h_, bg="#FFFFFF"):
    return f'<div style="width: {LW}px; height: {h_}px; overflow: hidden; background: {bg}; font-family: {FONT}; color: {C["t1"]}; display: flex; flex-direction: column; border: 1px solid {C["b2"]}; box-sizing: border-box">{inner}</div>'


def sec(inner, pad="96px 80px", bg="#FFFFFF", gap=48):
    return f'<section style="padding: {pad}; background: {bg}; display: flex; flex-direction: column; gap: {gap}px">{inner}</section>'


def eyebrow(s, c=None):
    return f'<div style="{TY["ovl"]}; font-size: 12px; color: {c or C["brand"]}">{s}</div>'


def store_btns(unavail=False, dark=False):
    def b(ic, top, name):
        bg = "#FFFFFF" if dark else C["inverse"]
        fg = C["t1"] if dark else "#FFFFFF"
        op = "opacity: .45; " if unavail else ""
        return (f'<a href="#" style="{op}display: inline-flex; align-items: center; gap: 12px; height: 56px; padding: 0 20px; border-radius: 12px; background: {bg}; color: {fg}; text-decoration: none">'
                f'{icon(ic, 24, fg)}<span style="display: flex; flex-direction: column"><span style="font-size: 11px; opacity: .8">{top}</span><span style="font-size: 17px; font-weight: 700">{name}</span></span></a>')
    return row(b("smartphone", "Tải trên" if not unavail else "Sắp có trên", "App Store"), b("smartphone", "Tải trên" if not unavail else "Sắp có trên", "Google Play"), gap=12)


def mini_phone(inner, w=300, h_=620):
    return f'<div style="width: {w}px; height: {h_}px; border-radius: 40px; border: 8px solid {C["inverse"]}; overflow: hidden; background: #FFFFFF; position: relative; flex-shrink: 0; box-shadow: {SH_LG}">{inner}</div>'


def hero_phone():
    m = map_svg(284, 604, route=[(0.72, 0.47), (0.72, 0.42), (0.52, 0.42), (0.52, 0.24), (0.3, 0.24), (0.3, 0.17)], pins=[("pickup", 0.72, 0.47), ("dropoff", 0.3, 0.17)], driver=(0.9, 0.3), labels=False)
    sheet = (f'<div style="position: absolute; left: 0; right: 0; bottom: 0; background: #FFFFFF; border-radius: 20px 20px 0 0; box-shadow: {SH_SHEET}; padding: 16px; display: flex; flex-direction: column; gap: 10px">'
             f'{row(pill("accepted"), spacer(), num("48.000đ", 16, weight=700))}{txt("Hùng đang đến · 4 phút", "hsm")}{row(avatar("TH", 36), col(txt("Trần Văn Hùng", "bsm", extra="font-weight: 600"), mono("59-X2 123.45", 12), gap=0), gap=10)}</div>')
    return mini_phone(f'<div style="position: absolute; inset: 0">{m}</div>{sheet}')


@frame("L-001", "Landing home hero", "Landing")
def l001():
    desk = page(nav() + sec(row(
        col(eyebrow("TP. HỒ CHÍ MINH · RA MẮT 2026"),
            f'<h1 style="margin: 0; {TY["dxl"]}">Đi xe, đặt món.<br>Giá rõ ràng,<br><span style="color: {C["red"]}">0% hoa hồng.</span></h1>',
            txt("Onway kết nối bạn với tài xế gần nhất. Bạn trả đúng giá hiển thị, chuyển khoản thẳng cho tài xế — Onway không lấy phần trăm nào.", "blg", C["t2"], extra="max-width: 520px"),
            store_btns(), row(icon("check", 18, C["ok"]), txt("Không phí dịch vụ cho khách", "bsm", C["t2"]), icon("check", 18, C["ok"]), txt("Tài xế nhận 100% tiền chuyến", "bsm", C["t2"]), gap=8), gap=28, extra="flex-grow: 1"),
        hero_phone(), gap=64), pad="80px 80px 96px"), 900)
    mob = (f'<div style="width: 390px; height: 900px; overflow: hidden; background: #FFFFFF; font-family: {FONT}; color: {C["t1"]}; display: flex; flex-direction: column; border: 1px solid {C["b2"]}; box-sizing: border-box">'
           f'<header style="height: 64px; display: flex; align-items: center; justify-content: space-between; padding: 0 16px; border-bottom: 1px solid {C["b1"]}">{logo_img(24)}{ibtn("menu", "Mở menu", "ghost", 44)}</header>'
           f'<div style="padding: 32px 16px; display: flex; flex-direction: column; gap: 20px">{eyebrow("TP. HỒ CHÍ MINH · RA MẮT 2026")}'
           f'<h1 style="margin: 0; {TY["dmd"]}; font-size: 38px">Đi xe, đặt món. Giá rõ ràng, <span style="color: {C["red"]}">0% hoa hồng.</span></h1>'
           f'{txt("Trả đúng giá hiển thị, chuyển khoản thẳng cho tài xế.", "bmd", C["t2"])}{col(btn("Tải ứng dụng", "primary", "lg", "download", full=True), btn("Đăng ký tài xế", "outline", "lg", full=True), gap=10)}</div>'
           f'<div style="display: flex; justify-content: center">{hero_phone().replace("width: 300px; height: 620px", "width: 260px; height: 540px")}</div></div>')
    return [("Desktop", desk), ("Mobile", mob)]


def feature(ic, t, d):
    return card(icon_tile(ic, 48, C["sunken"]) + txt(t, "hsm") + txt(d, "bmd", C["t2"]), pad=28, gap=14, extra="flex: 1")


@frame("L-002", "Customer value section", "Landing")
def l002():
    return [("Đi xe + Đặt món", page(sec(col(eyebrow("CHO KHÁCH HÀNG"), f'<h2 style="margin: 0; {TY["dlg"]}; font-size: 44px; max-width: 760px">Một ứng dụng cho chuyến đi và bữa ăn hằng ngày</h2>', gap=14)
                                             + row(feature("bike", "Đi xe máy & ô tô", "Giá Onway tính sẵn theo quãng đường. Không tăng giá bất ngờ, không mặc cả."),
                                                   feature("utensils", "Đặt món quán quen", "Chuỗi quán quen ở TP.HCM. Nếu giá tại quán khác, tài xế hỏi bạn trước khi mua."),
                                                   feature("banknote", "Không phí cho khách", "Bạn chỉ trả tiền chuyến hoặc tiền món + phí giao, chuyển thẳng cho tài xế."), gap=24), bg=C["page"]), 640, C["page"]))]


@frame("L-003", "Driver acquisition section", "Landing")
def l003():
    pkg = card(row(eyebrow("GÓI RA MẮT", C["red"]), spacer(), pill("active", "Đang mở đăng ký")) + row(num("1.000.000đ", 44, "#FFFFFF", 700), txt("/ 12 tháng", "blg", C["tinv2"]), gap=10, align="baseline")
               + row(icon("plus", 18, "#5CC795"), txt("Tặng thêm 6 tháng — tổng 18 tháng", "bmd", "#5CC795", extra="font-weight: 600"), gap=8)
               + txt("Phí sử dụng nền tảng, không phải tiền cọc. Dừng sớm được hoàn theo quý đã dùng.", "bsm", C["tinv2"]), pad=32, gap=16, bg=C["inverse2"], extra="border-color: rgba(255,255,255,.14); width: 480px; flex-shrink: 0")
    bullets = col(*[row(icon_tile(i, 44, "rgba(255,255,255,.08)", "#FFFFFF"), col(txt(t, "hsm", "#FFFFFF"), txt(d, "bmd", C["tinv2"]), gap=4), gap=16, align="flex-start") for i, t, d in [
        ("banknote", "0% hoa hồng", "Nhận 100% tiền chuyến và phí giao. Khách chuyển khoản thẳng vào tài khoản của bạn."),
        ("navigation", "Nhận hay từ chối là quyền của bạn", "Thấy giá cuối cùng trước khi nhận. Không phạt khi từ chối."),
        ("shield", "Xử lý tranh chấp minh bạch", "Mọi khoá tài khoản đều có lý do, hồ sơ và quyền kháng nghị trong 24 giờ.")]], gap=28)
    return [("0% hoa hồng + gói ra mắt", page(sec(col(eyebrow("CHO TÀI XẾ", "#E9506D"), f'<h2 style="margin: 0; {TY["dlg"]}; font-size: 44px; color: #FFFFFF; max-width: 760px">Chạy bao nhiêu, nhận bấy nhiêu.</h2>', gap=14)
                                                  + row(bullets, pkg, gap=64, align="flex-start") + row(btn("Đăng ký làm tài xế", "primary", "lg", "arrow-right"), btn("Xem điều kiện", "inverse", "lg"), gap=12), bg=C["inverse"]), 820, C["inverse"]))]


@frame("L-004", "How Onway works", "Landing")
def l004():
    steps = [("1", "Đặt chuyến hoặc đơn", "Chọn điểm đến hoặc món. Xem giá cuối cùng trước khi xác nhận."), ("2", "Onway ghép tài xế", "Tài xế gần nhất thấy giá và chọn nhận."),
             ("3", "Chuyển khoản cho tài xế", "Quét VietQR của tài xế, gửi ảnh chứng từ. Tài xế xác nhận đã nhận đủ."), ("4", "Đi hoặc nhận món", "Theo dõi trực tiếp, nhắn tin hoặc gọi tài xế khi cần.")]
    items = "".join(f'<div style="flex: 1; display: flex; flex-direction: column; gap: 14px"><div style="width: 48px; height: 48px; border-radius: 999px; background: {C["inverse"]}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-family: {MONO}; font-size: 20px; font-weight: 700">{n}</div>{txt(t, "hsm")}{txt(d, "bmd", C["t2"])}</div>' for n, t, d in steps)
    return [("Chuyển khoản trực tiếp + chứng từ", page(sec(col(eyebrow("CÁCH HOẠT ĐỘNG"), f'<h2 style="margin: 0; {TY["dlg"]}; font-size: 44px">Tiền đi thẳng tới tài xế</h2>', gap=14)
                                                          + f'<div style="display: flex; gap: 32px">{items}</div>'
                                                          + banner("info", "Onway không giữ tiền của bạn", "Onway không có ví, không thu hộ và không nhận tiền mặt trong giai đoạn đầu. Ảnh chứng từ giúp xử lý nhanh khi có nhầm lẫn.")), 640))]


@frame("L-005", "Safety / dispute / connection model", "Landing")
def l005():
    cols_ = row(feature("scale", "Onway là nền tảng kết nối", "Onway kết nối khách, tài xế và quán. Khi có sai sót, bên nào có lỗi, bên đó chịu trách nhiệm theo điều khoản."),
                feature("file-lock", "Bằng chứng được lưu riêng tư", "Chứng từ, ảnh và tin nhắn liên quan khiếu nại được lưu có kiểm soát, chỉ người xử lý được xem."),
                feature("user-check", "Con người ra quyết định", "Mọi khiếu nại và khoá tài khoản đều có người xem xét, có lý do và có quyền kháng nghị."), gap=24)
    return [("Mô hình kết nối, an toàn", page(sec(col(eyebrow("AN TOÀN & MINH BẠCH"), f'<h2 style="margin: 0; {TY["dlg"]}; font-size: 44px; max-width: 800px">Rõ ràng khi mọi việc suôn sẻ, công bằng khi có sự cố</h2>', gap=14) + cols_
                                                  + txt("Nội dung pháp lý chi tiết đang được rà soát và sẽ được công bố trong Điều khoản sử dụng.", "cap", C["t3"]), bg=C["page"]), 680, C["page"]))]


@frame("L-006", "App download / waitlist CTA", "Landing")
def l006():
    def v(unav):
        extra = (row(f'<div style="width: 360px">{field("", "", "Số điện thoại của bạn", ic="phone")}</div>', btn("Báo tôi khi ra mắt", "inverse", "lg"), gap=10) if unav else "")
        h2 = '<h2 style="margin: 0; ' + TY['dlg'] + '; font-size: 44px; color: #FFFFFF">' + ('Onway sắp có mặt trên kho ứng dụng' if unav else 'Tải Onway, đi thử chuyến đầu tiên') + '</h2>'
        inner = (f'<div style="display: flex; align-items: center; gap: 64px; padding: 72px 80px; background: {C["red"]}">'
                 f'<div style="flex-grow: 1; display: flex; flex-direction: column; gap: 20px">{h2}'
                 f'{txt("Có trên iOS và Android. Đang phục vụ tại TP. Hồ Chí Minh." if not unav else "Để lại số điện thoại, chúng tôi nhắn bạn ngay khi ứng dụng sẵn sàng.", "blg", "rgba(255,255,255,.9)")}'
                 f'{store_btns(unav, True)}{extra}</div><img src="{APPICON}" alt="" width="160" height="160" style="width: 160px; height: 160px; border-radius: 36px; border: 4px solid rgba(255,255,255,.3)"></div>')
        return page(inner, 440, C["red"])
    return [("Có link tải", v(False)), ("Chưa có link — waitlist", v(True))]


def faq_item(q, a="", open_=False):
    body_ = f'<div style="{TY["bmd"]}; color: {C["t2"]}; padding: 0 0 20px">{a}</div>' if open_ else ""
    return (f'<div style="border-bottom: 1px solid {C["b2"]}"><button type="button" aria-expanded="{"true" if open_ else "false"}" style="display: flex; width: 100%; align-items: center; gap: 16px; padding: 20px 0; border: none; background: transparent; font-family: {FONT}; text-align: left; color: {C["t1"]}">'
            f'<span style="flex-grow: 1; {TY["hsm"]}">{q}</span>{icon("minus" if open_ else "plus", 20)}</button>{body_}</div>')


@frame("L-007", "FAQ", "Landing")
def l007():
    def v(tab):
        if tab == 0:
            qs = [("Tôi thanh toán thế nào?", "Sau khi có tài xế, bạn chuyển khoản hoặc quét VietQR của tài xế, rồi gửi ảnh chứng từ trong ứng dụng. Onway không thu tiền hộ.", True),
                  ("Có trả tiền mặt được không?", ""), ("Nếu giá món tại quán khác trên ứng dụng?", ""), ("Tôi có thể huỷ đơn món không?", "")]
        else:
            qs = [("Onway thu phí tài xế như thế nào?", "Gói ra mắt 1.000.000đ cho 12 tháng, tặng thêm 6 tháng. Onway thu 0% hoa hồng trên mọi chuyến và đơn.", True),
                  ("Tôi cần giấy tờ gì để đăng ký?", ""), ("Nếu khách không chuyển tiền?", ""), ("Vì sao tài khoản bị tạm khoá?", "")]
        return page(sec(col(eyebrow("HỎI ĐÁP"), f'<h2 style="margin: 0; {TY["dlg"]}; font-size: 44px">Câu hỏi thường gặp</h2>', gap=14)
                        + f'<div style="width: 420px">{segmented(["Khách hàng", "Tài xế"], tab)}</div>' + f'<div style="max-width: 880px">{"".join(faq_item(*q) for q in qs)}</div>', gap=32), 820)
    return [("Khách hàng", v(0)), ("Tài xế", v(1))]


def footer():
    colh = lambda t, items: col(txt(t, "lbl", "#FFFFFF"), *[f'<a href="#" style="{TY["bsm"]}; font-size: 14px; color: {C["tinv2"]}; text-decoration: none">{i}</a>' for i in items], gap=12)
    return (f'<footer style="padding: 64px 80px 40px; background: {C["inverse"]}; display: flex; flex-direction: column; gap: 48px">'
            + row(col(logo_img(28, True), txt("Nền tảng kết nối Đi xe & Đặt món. 0% hoa hồng.", "bsm", C["tinv2"]), gap=16, extra="flex-grow: 1"),
                  colh("Sản phẩm", ["Đi xe", "Đặt món", "Tài xế"]), colh("Hỗ trợ", ["Hỏi đáp", "Liên hệ", "Khiếu nại"]), colh("Pháp lý", ["Điều khoản sử dụng", "Chính sách quyền riêng tư"]), gap=80, align="flex-start")
            + f'<div style="border-top: 1px solid rgba(255,255,255,.14); padding-top: 24px; display: flex; {TY["cap"]}; color: {C["tinv2"]}"><span style="flex-grow: 1">© 2026 Công ty TNHH Onway · [ĐỊA CHỈ ĐĂNG KÝ KINH DOANH]</span><span>[MÃ SỐ DOANH NGHIỆP]</span></div></footer>')


@frame("L-008", "Footer / legal links", "Landing")
def l008():
    return [("Quyền riêng tư, điều khoản, liên hệ", page(footer(), 360, C["inverse"]))]


def legal_page(title, updated, sections):
    toc = col(*[f'<a href="#" style="{TY["bsm"]}; font-size: 14px; color: {C["t1"] if i == 0 else C["t2"]}; text-decoration: none; font-weight: {600 if i == 0 else 400}">{i + 1}. {s[0]}</a>' for i, s in enumerate(sections)], gap=12, extra="width: 260px; flex-shrink: 0")
    body_ = "".join(f'<h2 style="margin: 0; {TY["hmd"]}">{i + 1}. {t}</h2><p style="margin: 0; {TY["blg"]}; color: {C["t2"]}">{p}</p>' for i, (t, p) in enumerate(sections))
    return page(nav() + sec(col(f'<h1 style="margin: 0; {TY["dmd"]}">{title}</h1>', txt(updated, "bsm", C["t3"]), banner("warning", "Bản nháp chờ rà soát pháp lý", "Nội dung dưới đây là khung cấu trúc; văn bản chính thức sẽ thay thế trước khi ra mắt."), gap=12)
                            + row(toc, f'<div style="max-width: 720px; display: flex; flex-direction: column; gap: 20px">{body_}</div>', gap=64, align="flex-start"), pad="64px 80px", gap=40), 1200)


@frame("L-009", "Terms page", "Landing")
def l009():
    return [("Khung nội dung pháp lý", legal_page("Điều khoản sử dụng", "Cập nhật: [NGÀY HIỆU LỰC]", [
        ("Onway là nền tảng kết nối", "Onway cung cấp phần mềm kết nối khách hàng, tài xế và quán. Onway không phải bên vận chuyển hay bán món. [NỘI DUNG PHÁP LÝ]"),
        ("Giá và thanh toán", "Giá chuyến và phí giao do Onway đề xuất, hiển thị trước khi xác nhận. Khách chuyển khoản trực tiếp cho tài xế. Onway không giữ tiền. [NỘI DUNG PHÁP LÝ]"),
        ("Phí nền tảng của tài xế", "Gói ra mắt và chính sách hoàn phí theo quý. Phí nền tảng không phải tiền cọc hay ký quỹ. [NỘI DUNG PHÁP LÝ]"),
        ("Khiếu nại và tranh chấp", "Nguyên tắc bên nào có lỗi bên đó chịu trách nhiệm; quy trình xem xét và kháng nghị. [NỘI DUNG PHÁP LÝ]"),
        ("Tạm khoá tài khoản", "Điều kiện khoá tạm, thời hạn xem xét 24 giờ và quyền kháng nghị. [NỘI DUNG PHÁP LÝ]")]))]


@frame("L-010", "Privacy page", "Landing")
def l010():
    return [("Khung nội dung quyền riêng tư", legal_page("Chính sách quyền riêng tư", "Cập nhật: [NGÀY HIỆU LỰC]", [
        ("Dữ liệu Onway thu thập", "Số điện thoại, hồ sơ, vị trí khi dùng ứng dụng, ảnh chứng từ, mã thiết bị đã mã hoá. [NỘI DUNG PHÁP LÝ]"),
        ("Mục đích sử dụng", "Kết nối chuyến/đơn, xử lý khiếu nại, chống gian lận. Onway không dùng AI tự động kết luận vi phạm. [NỘI DUNG PHÁP LÝ]"),
        ("Thời gian lưu trữ", "Chat lưu 7 ngày trừ khi liên quan khiếu nại; GPS, KYC, bằng chứng và audit theo chính sách lưu trữ. [NỘI DUNG PHÁP LÝ]"),
        ("Quyền của bạn", "Xem, tải xuống, yêu cầu xoá dữ liệu; ngoại lệ theo nghĩa vụ pháp lý và tranh chấp đang mở. [NỘI DUNG PHÁP LÝ]"),
        ("Liên hệ", "[EMAIL BẢO VỆ DỮ LIỆU]")]))]


@frame("L-011", "Contact/support page", "Landing")
def l011():
    def ct(ic, t, d, a):
        return card(icon_tile(ic, 48) + txt(t, "hsm") + txt(d, "bmd", C["t2"]) + a, pad=28, gap=12, extra="flex: 1")
    return [("Khách, tài xế, đối tác", page(nav() + sec(col(eyebrow("LIÊN HỆ"), f'<h2 style="margin: 0; {TY["dlg"]}; font-size: 44px">Chúng tôi có thể giúp gì?</h2>', gap=14)
                                                             + row(ct("user", "Khách hàng", "Vấn đề với chuyến đi hoặc đơn món? Gửi khiếu nại ngay trong ứng dụng để được xử lý nhanh nhất.", btn("Mở ứng dụng", "outline", "md")),
                                                                   ct("bike", "Tài xế", "Hỏi về đăng ký, phí nền tảng, khoá tài khoản.", txt("[SỐ TỔNG ĐÀI TÀI XẾ]", "bmd", extra="font-weight: 600")),
                                                                   ct("store", "Quán & đối tác", "Muốn đưa quán lên Onway hoặc hợp tác?", txt("[EMAIL ĐỐI TÁC]", "bmd", extra="font-weight: 600")), gap=24)
                                                             + card(row(f'<div style="flex: 1">{field("Họ tên", "")}</div>', f'<div style="flex: 1">{field("Số điện thoại", "")}</div>', gap=16) + select("Bạn là", "Khách hàng")
                                                                    + field("Nội dung", "", textarea=True) + row(btn("Gửi liên hệ", "primary", "lg"), spacer()), pad=32, gap=16, extra="max-width: 880px")), 1280))]
