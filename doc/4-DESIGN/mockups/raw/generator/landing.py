from lib import *
from reg import frame
import customer as cu
import driver as dr

LW = 1440
G_HOME = "Landing · Trang chủ (xếp dọc như trang web)"
G_SUB = "Landing · Trang phụ"


# ---------- building blocks ----------
def nav(active="", dark=False):
    fg = "#FFFFFF" if dark else C["t1"]
    fg2 = C["tinv2"] if dark else C["t2"]
    links = "".join(f'<a href="#" style="text-decoration: none; color: {fg if l == active else fg2}; {TY["lbl"]}; font-size: 14px">{l}</a>' for l in ["Đi xe", "Đặt món", "Tài xế", "Cách hoạt động", "An toàn", "Hỏi đáp"])
    return (f'<header style="height: 76px; display: flex; align-items: center; gap: 40px; padding: 0 80px; flex-shrink: 0; position: relative; z-index: 2">{logo_img(28, dark)}'
            f'<nav aria-label="Điều hướng" style="display: flex; gap: 28px; flex-grow: 1">{links}</nav>'
            f'<a href="#" style="{TY["lbl"]}; font-size: 14px; color: {fg}; text-decoration: none">Đăng ký tài xế</a>{btn("Tải ứng dụng", "primary", "md", "download")}</header>')


def page(inner, h_, bg="#FFFFFF", w=LW):
    return f'<div style="position: relative; width: {w}px; height: {h_}px; overflow: hidden; background: {bg}; font-family: {FONT}; color: {C["t1"]}; display: flex; flex-direction: column; border: 1px solid {C["b2"]}; box-sizing: border-box">{inner}</div>'


def eyebrow(s, c=None):
    return f'<div style="{TY["ovl"]}; font-size: 12px; color: {c or C["brand"]}">{s}</div>'


def h2(s, color=None, size=48, maxw=760):
    return f'<h2 style="margin: 0; font-size: {size}px; line-height: 1.08; font-weight: 800; letter-spacing: -0.035em; color: {color or C["t1"]}; max-width: {maxw}px">{s}</h2>'


def lead(s, color=None, maxw=620):
    return f'<p style="margin: 0; {TY["blg"]}; font-size: 19px; color: {color or C["t2"]}; max-width: {maxw}px">{s}</p>'


def device(ph, s=0.62, shadow=True, extra=""):
    import re as _re
    ph = _re.sub(r'href="[A-Z]-\d+\.dc\.html"', 'href="#"', ph)
    w, hh = round(390 * s), round(844 * s)
    sh = f"box-shadow: 0 30px 60px rgba(15,14,14,.22), 0 8px 20px rgba(15,14,14,.12); " if shadow else ""
    return (f'<div style="{sh}width: {w + 14}px; height: {hh + 14}px; flex-shrink: 0; border-radius: {round(36 * s) + 9}px; background: {C["inverse"]}; padding: 7px; box-sizing: border-box{"; " + extra if extra else ""}">'
            f'<div style="width: {w}px; height: {hh}px; overflow: hidden; border-radius: {round(36 * s) + 2}px; position: relative">'
            f'<div style="width: 390px; height: 844px; transform: scale({s}); transform-origin: 0 0">{ph}</div></div></div>')


def store_badge(name, sub="Tải trên", dark_bg=True, dim=False):
    bg = C["inverse"] if dark_bg else "#FFFFFF"
    fg = "#FFFFFF" if dark_bg else C["t1"]
    op = "opacity: .5; " if dim else ""
    ic = ('<svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true" fill="' + fg + '"><path d="M16.5 12.6c0-2.4 2-3.6 2.1-3.7-1.1-1.7-2.9-1.9-3.5-1.9-1.5-.2-2.9.9-3.7.9-.8 0-1.9-.9-3.2-.8-1.6 0-3.1 1-4 2.4-1.7 3-.4 7.4 1.2 9.8.8 1.2 1.8 2.5 3 2.4 1.2 0 1.7-.8 3.2-.8s1.9.8 3.2.8c1.3 0 2.2-1.2 3-2.4.9-1.4 1.3-2.7 1.3-2.8 0 0-2.6-1-2.6-3.9zM14.1 5.5c.7-.8 1.1-1.9 1-3-1 0-2.1.7-2.8 1.5-.6.7-1.2 1.8-1 2.9 1.1.1 2.1-.6 2.8-1.4z"/></svg>'
          if name == "App Store" else
          '<svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M3.6 2.3 13.4 12l-9.8 9.7c-.4-.2-.6-.6-.6-1.1V3.4c0-.5.2-.9.6-1.1z" fill="#4C7DF0"/><path d="m16.8 8.6-3.4 3.4-9.8-9.7c.2-.1.5-.1.8 0l12.4 6.3z" fill="#2E9E6B"/><path d="M16.8 15.4 4.4 21.7c-.3.1-.6.1-.8 0l9.8-9.7 3.4 3.4z" fill="#E22240"/><path d="m20.4 12-3.6 3.4-3.4-3.4 3.4-3.4 3.6 1.8c.8.4.8 1.2 0 1.6z" fill="#E2A33C"/></svg>')
    return (f'<a href="#" style="{op}display: inline-flex; align-items: center; gap: 10px; height: 52px; padding: 0 18px; border-radius: 12px; background: {bg}; color: {fg}; text-decoration: none; border: 1px solid {"rgba(255,255,255,.2)" if dark_bg else C["b2"]}">'
            f'{ic}<span style="display: flex; flex-direction: column; line-height: 1.1"><span style="font-size: 11px; opacity: .75">{sub}</span><span style="font-size: 17px; font-weight: 700">{name}</span></span></a>')


def stores(dark_bg=True, dim=False, sub="Tải trên"):
    return row(store_badge("App Store", sub, dark_bg, dim), store_badge("Google Play", sub, dark_bg, dim), gap=12)


def float_chip(inner, pos, extra=""):
    return f'<div style="position: absolute; {pos}; background: #FFFFFF; border: 1px solid {C["b2"]}; border-radius: 14px; box-shadow: 0 16px 40px rgba(15,14,14,.14); padding: 14px 16px; display: flex; flex-direction: column; gap: 6px; z-index: 3{"; " + extra if extra else ""}">{inner}</div>'


def check_item(s, color=None, icolor=None):
    return row(f'<span style="width: 22px; height: 22px; border-radius: 999px; background: {C["ok_bg"] if not icolor else "rgba(255,255,255,.1)"}; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{icon("check", 14, icolor or C["ok"], 3)}</span>',
               txt(s, "bmd", color or C["t1"]), gap=10)


def fact(num_, lab, sub, dark=False):
    return (f'<div style="flex: 1; display: flex; flex-direction: column; gap: 6px; padding: 28px 28px 24px; border-left: 1px solid {"rgba(255,255,255,.14)" if dark else C["b2"]}">'
            f'<span style="font-family: {MONO}; font-size: 40px; font-weight: 700; letter-spacing: -0.02em; color: {"#FFFFFF" if dark else C["t1"]}">{num_}</span>'
            f'<span style="{TY["bmd"]}; font-weight: 700; color: {"#FFFFFF" if dark else C["t1"]}">{lab}</span><span style="{TY["bsm"]}; font-size: 14px; color: {C["tinv2"] if dark else C["t2"]}">{sub}</span></div>')


def dotgrid(w, h_, color="rgba(15,14,14,.07)"):
    return f'<svg width="{w}" height="{h_}" aria-hidden="true" style="position: absolute; inset: 0"><defs><pattern id="dg" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.3" fill="{color}"/></pattern></defs><rect width="{w}" height="{h_}" fill="url(#dg)"/></svg>'


# ---------- L-001 hero ----------
def hero_visual(w=660, h_=760, scale_a=0.78, scale_b=0.64):
    mp = map_svg(w, h_, route=[(0.78, 0.62), (0.78, 0.42), (0.52, 0.42), (0.52, 0.24), (0.3, 0.24)], pins=[("pickup", 0.78, 0.62), ("dropoff", 0.3, 0.24)], driver=(0.64, 0.42), labels=False)
    a = device(cu.active_ride(), scale_a)
    b = device(cu.food_active("delivering"), scale_b)
    chip1 = float_chip(row(icon_tile("check-circle", 36, C["ok_bg"], C["ok"], 999), col(txt("Tài xế đã nhận đủ tiền", "lbl", extra="font-size: 14px"), txt("48.000đ · chuyển khoản trực tiếp", "cap", C["t3"]), gap=2), gap=10), "left: -20px; top: 150px")
    chip2 = float_chip(col(txt("Onway giữ lại", "cap", C["t3"]), num("0đ", 30, weight=700), txt("0% hoa hồng trên mỗi chuyến", "cap", C["ok"], extra="font-weight: 600"), gap=2), "right: -12px; top: 70px")
    chip3 = float_chip(row(pill("delivering"), txt("Cơm Tấm Sà Bì · 12 phút", "lbl"), gap=8), "right: 10px; bottom: 60px")
    return (f'<div style="position: relative; width: {w}px; height: {h_}px; flex-shrink: 0">'
            f'<div style="position: absolute; inset: 0; border-radius: 36px; overflow: hidden; opacity: .9">{mp}</div>'
            f'<div style="position: absolute; inset: 0; border-radius: 36px; background: linear-gradient(90deg, rgba(255,255,255,.55), rgba(255,255,255,0) 40%)"></div>'
            f'<div style="position: absolute; left: 110px; top: 40px; z-index: 2">{a}</div>'
            f'<div style="position: absolute; left: 380px; top: 250px; z-index: 1">{b}</div>{chip1}{chip2}{chip3}</div>')


def hero_desktop():
    left = col(
        f'<span style="display: inline-flex; align-self: flex-start; align-items: center; gap: 8px; height: 32px; padding: 0 14px; border-radius: 999px; background: {C["brand_bg"]}; color: {C["brand"]}; {TY["lbl"]}"><span style="width: 8px; height: 8px; border-radius: 999px; background: {C["red"]}"></span>Đang phục vụ tại TP. Hồ Chí Minh</span>',
        f'<h1 style="margin: 0; font-size: 72px; line-height: 1.02; font-weight: 800; letter-spacing: -0.04em">Đi xe, đặt món.<br>Giá rõ ràng.<br><span style="color: {C["red"]}">0% hoa hồng.</span></h1>',
        lead("Onway kết nối bạn với tài xế gần nhất. Bạn thấy giá cuối cùng trước khi đặt, chuyển khoản thẳng cho tài xế — Onway không lấy phần trăm nào."),
        row(btn("Tải ứng dụng", "primary", "xl", "download"), btn("Đăng ký làm tài xế", "outline", "xl", icon_right="arrow-right"), gap=12),
        row(check_item("Không phí dịch vụ cho khách"), check_item("Tài xế nhận 100%"), gap=24),
        gap=28, extra="flex-grow: 1; padding-top: 40px")
    body_ = f'<div style="display: flex; gap: 40px; padding: 24px 80px 0; align-items: flex-start">{left}{hero_visual()}</div>'
    return page(f'<div style="position: absolute; inset: 0">{dotgrid(LW, 900)}</div>' + nav("Đi xe") + body_, 900, C["ink25"])


def hero_mobile():
    return (f'<div style="width: 390px; height: 1100px; overflow: hidden; background: {C["ink25"]}; font-family: {FONT}; color: {C["t1"]}; display: flex; flex-direction: column; border: 1px solid {C["b2"]}; box-sizing: border-box">'
            f'<header style="height: 64px; display: flex; align-items: center; justify-content: space-between; padding: 0 16px">{logo_img(24)}{ibtn("menu", "Mở menu", "ghost", 44)}</header>'
            f'<div style="padding: 20px 16px 28px; display: flex; flex-direction: column; gap: 18px">'
            f'<span style="display: inline-flex; align-self: flex-start; align-items: center; gap: 8px; height: 28px; padding: 0 12px; border-radius: 999px; background: {C["brand_bg"]}; color: {C["brand"]}; {TY["cap"]}; font-weight: 600">Đang phục vụ tại TP.HCM</span>'
            f'<h1 style="margin: 0; font-size: 40px; line-height: 1.05; font-weight: 800; letter-spacing: -0.035em">Đi xe, đặt món. Giá rõ ràng. <span style="color: {C["red"]}">0% hoa hồng.</span></h1>'
            f'{txt("Thấy giá trước khi đặt, chuyển khoản thẳng cho tài xế.", "bmd", C["t2"])}'
            f'{col(btn("Tải ứng dụng", "primary", "lg", "download", full=True), btn("Đăng ký làm tài xế", "outline", "lg", full=True), gap=10)}</div>'
            f'<div style="position: relative; height: 620px; margin: 0 16px; border-radius: 28px; overflow: hidden">{map_svg(358, 620, labels=False)}'
            f'<div style="position: absolute; left: 50%; top: 36px; transform: translateX(-50%)">{device(cu.active_ride(), 0.62)}</div></div></div>')


@frame("L-001", "Landing home hero", G_HOME)
def l001():
    return [("Desktop", hero_desktop()), ("Mobile", hero_mobile())]


# ---------- L-002 customer value ----------
def service_card(ic, title, sub, bullets, dev, tone):
    bl = col(*[check_item(b) for b in bullets], gap=12)
    return (f'<div style="flex: 1; position: relative; height: 560px; border-radius: 28px; background: {tone}; overflow: hidden; display: flex; padding: 40px; box-sizing: border-box; gap: 24px">'
            f'<div style="flex-grow: 1; display: flex; flex-direction: column; gap: 18px; min-width: 0">{icon_tile(ic, 56, "#FFFFFF", C["t1"], 16)}'
            f'<h3 style="margin: 0; font-size: 32px; line-height: 1.1; font-weight: 800; letter-spacing: -0.03em">{title}</h3>{txt(sub, "bmd", C["t2"])}{bl}</div>'
            f'<div style="flex-shrink: 0; margin-bottom: -120px; align-self: flex-end">{dev}</div></div>')


@frame("L-002", "Customer value section", G_HOME)
def l002():
    facts = f'<div style="display: flex; border-top: 1px solid {C["b2"]}; border-bottom: 1px solid {C["b2"]}; margin: 0 -1px">{fact("0đ", "Phí dịch vụ cho khách", "Bạn chỉ trả tiền chuyến hoặc tiền món + phí giao.")}{fact("100%", "Tiền đến tay tài xế", "Chuyển khoản trực tiếp, không qua ví trung gian.")}{fact("5 phút", "Để quyết định đổi món", "Tài xế hỏi bạn trước khi mua món có giá khác.")}{fact("24 giờ", "Phản hồi khiếu nại", "Có mã hồ sơ, theo dõi được trong ứng dụng.")}</div>'
    ride = service_card("bike", "Đi xe máy & ô tô", "Nhập điểm đến, chọn loại xe và thấy ngay giá cuối cùng Onway tính theo quãng đường.",
                        ["Giá cố định trước khi đặt, không mặc cả", "Thấy tài xế, biển số và thời gian đến", "Chat hoặc gọi tài xế trong chuyến"],
                        device(cu.vehicle_sheet("bike"), 0.56), C["page"])
    food = service_card("utensils", "Đặt món quán quen", "Chuỗi quán quen ở TP.HCM. Tài xế mua món bằng tiền bạn chuyển trước và giao tận nơi.",
                        ["Giá món lấy từ quán, Onway không cộng thêm", "Giá tại quán khác? Tài xế hỏi bạn trước", "Theo dõi từ lúc đặt món tới khi giao"],
                        device(cu.outlet_menu(), 0.56), C["warn_bg"])
    return [("Đi xe + Đặt món", page(f'<div style="padding: 0 80px">{facts}</div>'
                                        + f'<section style="padding: 88px 80px 96px; display: flex; flex-direction: column; gap: 48px">{row(col(eyebrow("CHO KHÁCH HÀNG"), h2("Một ứng dụng cho chuyến đi và bữa ăn hằng ngày"), gap=14), spacer(), lead("Không phí ẩn, không tăng giá bất ngờ. Bạn biết chính xác số tiền cần chuyển trước khi xác nhận.", maxw=420), align="flex-end")}'
                                        + f'{row(ride, food, gap=24)}</section>', 1000))]


# ---------- L-003 driver ----------
@frame("L-003", "Driver acquisition section", G_HOME)
def l003():
    calc = (f'<div style="border-radius: 20px; background: {C["inverse2"]}; border: 1px solid rgba(255,255,255,.12); padding: 28px; display: flex; flex-direction: column; gap: 14px; width: 460px; box-sizing: border-box">'
            f'{row(eyebrow("VÍ DỤ 1 THÁNG", "#E9506D"), spacer(), txt("Minh hoạ, không phải cam kết thu nhập", "cap", C["tinv2"]))}'
            + "".join(f'<div style="display: flex; justify-content: space-between; align-items: baseline; padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,.08)"><span style="{TY["bmd"]}; color: {C["tinv2"]}">{k}</span><span style="font-family: {MONO}; font-size: 17px; font-weight: 600; color: {c}">{v}</span></div>'
                      for k, v, c in [("Tiền khách chuyển cho bạn", "12.000.000đ", "#FFFFFF"), ("Hoa hồng Onway (0%)", "0đ", "#5CC795"), ("Phí nền tảng (1.000.000đ ÷ 18 tháng)", "≈ 55.600đ", "#FFFFFF")])
            + f'<div style="display: flex; justify-content: space-between; align-items: baseline; padding-top: 6px"><span style="{TY["hsm"]}; color: #FFFFFF">Bạn giữ lại</span><span style="font-family: {MONO}; font-size: 30px; font-weight: 700; color: #FFFFFF">≈ 11.944.400đ</span></div></div>')
    pkg = float_chip(col(row(txt("Gói ra mắt", "lbl"), spacer(), pill("active", "Đang mở")), row(num("1.000.000đ", 26, weight=700), txt("/ 12 tháng", "bsm", C["t2"]), gap=6, align="baseline"),
                         row(icon("plus", 14, C["ok"]), txt("Tặng 6 tháng — tổng 18 tháng", "bsm", C["ok"], extra="font-weight: 600"), gap=6), gap=6), "left: -40px; bottom: 90px; width: 280px")
    visual = (f'<div style="position: relative; width: 520px; height: 780px; flex-shrink: 0"><div style="position: absolute; right: 30px; top: 0">{device(dr.offer("ride", 12), 0.84)}</div>{pkg}</div>')
    bullets = col(*[row(icon_tile(i, 48, "rgba(255,255,255,.08)", "#FFFFFF", 12), col(txt(t, "hsm", "#FFFFFF"), txt(d, "bmd", C["tinv2"]), gap=4), gap=16, align="flex-start") for i, t, d in [
        ("banknote", "0% hoa hồng", "Nhận 100% tiền chuyến và phí giao. Khách chuyển khoản thẳng vào tài khoản của bạn."),
        ("navigation", "Thấy giá trước khi nhận", "Giá cuối cùng hiện trên yêu cầu. Bạn chọn Nhận hoặc Từ chối."),
        ("shield", "Tạm khoá luôn có lý do", "Mọi lần khoá đều có hồ sơ, xem xét trong 24 giờ và quyền kháng nghị.")]], gap=24)
    left = col(eyebrow("CHO TÀI XẾ", "#E9506D"), h2("Chạy bao nhiêu,<br>nhận bấy nhiêu.", "#FFFFFF", 56), bullets, calc,
               row(btn("Đăng ký làm tài xế", "primary", "xl", icon_right="arrow-right"), btn("Giấy tờ cần chuẩn bị", "inverse", "xl"), gap=12), gap=32, extra="flex-grow: 1")
    return [("0% hoa hồng + gói ra mắt", page(f'<div style="position: absolute; inset: 0">{dotgrid(LW, 1040, "rgba(255,255,255,.06)")}</div>'
                                                 + f'<section style="position: relative; padding: 96px 80px; display: flex; gap: 48px; align-items: flex-start">{left}{visual}</section>', 1040, C["inverse"]))]


# ---------- L-004 how it works ----------
@frame("L-004", "How Onway works", G_HOME)
def l004():
    steps = [("1", "Đặt chuyến hoặc đơn", "Chọn điểm đến hoặc món. Giá cuối cùng hiện trước khi xác nhận.", cu.price_review()),
             ("2", "Onway ghép tài xế", "Tài xế gần nhất thấy giá và chọn nhận. Bạn thấy tên, biển số, thời gian đến.", cu.matched()),
             ("3", "Chuyển khoản cho tài xế", "Quét VietQR của tài xế, gửi ảnh chứng từ. Tài xế xác nhận đã nhận đủ.", phone(sheet_over(cu.matched(), cu.pay_info(), title="Chuyển khoản cho tài xế"))),
             ("4", "Lên đường", "Theo dõi trực tiếp trên bản đồ, nhắn tin hoặc gọi tài xế khi cần.", cu.active_ride())]
    cols_ = ""
    for n, t, d, ph in steps:
        cols_ += (f'<div style="flex: 1; display: flex; flex-direction: column; gap: 16px; align-items: flex-start">'
                  f'<div style="display: flex; align-items: center; gap: 12px; width: 100%"><span style="width: 44px; height: 44px; border-radius: 999px; background: {C["inverse"]}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-family: {MONO}; font-size: 18px; font-weight: 700; flex-shrink: 0">{n}</span>'
                  f'<span style="flex-grow: 1; height: 2px; background: {C["b2"] if n != "4" else "transparent"}"></span></div>'
                  f'{txt(t, "hsm", extra="font-size: 20px")}{txt(d, "bmd", C["t2"], extra="min-height: 72px")}'
                  f'<div style="width: 100%; display: flex; justify-content: center; padding: 28px 0 0; border-radius: 20px; background: {C["page"]}; height: 420px; overflow: hidden; box-sizing: border-box">{device(ph, 0.6, False)}</div></div>')
    note = card(row(icon_tile("banknote", 44, C["brand_bg"], C["brand"], 999), col(txt("Onway không giữ tiền của bạn", "hsm"), txt("Không ví, không thu hộ, không tiền mặt trong giai đoạn đầu. Ảnh chứng từ giúp xử lý nhanh khi có nhầm lẫn — bên nào sai, bên đó chịu trách nhiệm.", "bmd", C["t2"]), gap=4), gap=16), pad=24)
    return [("Chuyển khoản trực tiếp + chứng từ", page(f'<section style="padding: 96px 80px; display: flex; flex-direction: column; gap: 48px">{col(eyebrow("CÁCH HOẠT ĐỘNG"), h2("Tiền đi thẳng tới tài xế, trong 4 bước"), gap=14)}'
                                                          f'<div style="display: flex; gap: 24px">{cols_}</div>{note}</section>', 1100))]


# ---------- L-005 safety ----------
@frame("L-005", "Safety / dispute / connection model", G_HOME)
def l005():
    stages = [("flag", "Gửi khiếu nại", "Có mã hồ sơ ngay"), ("paperclip", "Thu thập bằng chứng", "Chứng từ, ảnh, chat"), ("message", "Hai bên phản hồi", "Hạn 24 giờ"),
              ("user-check", "Con người kết luận", "Không để máy tự quyết"), ("scale", "Kháng nghị", "Nếu chưa đồng ý")]
    flow = ""
    for i, (ic, t, s) in enumerate(stages):
        arrow = f'<div style="flex-shrink: 0; color: {C["b3"]}; padding-top: 18px">{icon("arrow-right", 20)}</div>' if i < len(stages) - 1 else ""
        flow += (f'<div style="flex: 1; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 8px">{icon_tile(ic, 56, "#FFFFFF" if i != 3 else C["inverse"], C["t1"] if i != 3 else "#FFFFFF", 999)}'
                 f'{txt(t, "lbl", extra="font-size: 14px")}{txt(s, "cap", C["t3"])}</div>{arrow}')
    diagram = f'<div style="display: flex; align-items: flex-start; gap: 4px; padding: 28px 24px; border-radius: 20px; background: {C["page"]}; border: 1px solid {C["b2"]}">{flow}</div>'
    principles = col(*[row(icon_tile(i, 48, C["sunken"], C["t1"], 12), col(txt(t, "hsm"), txt(d, "bmd", C["t2"]), gap=4), gap=16, align="flex-start") for i, t, d in [
        ("scale", "Onway là nền tảng kết nối", "Onway kết nối khách, tài xế và quán. Khi có sai sót, bên nào có lỗi, bên đó chịu trách nhiệm theo điều khoản."),
        ("file-lock", "Bằng chứng được lưu riêng tư", "Chứng từ, ảnh và tin nhắn liên quan khiếu nại chỉ người xử lý hồ sơ được xem, mọi lượt xem đều ghi lại."),
        ("user-check", "Tạm khoá có lý do, có kháng nghị", "Tài khoản bị tạm khoá luôn có hồ sơ, được xem xét trong 24 giờ và có quyền kháng nghị.")]], gap=28)
    visual = f'<div style="position: relative; width: 460px; height: 640px; flex-shrink: 0; border-radius: 28px; background: {C["ok_bg"]}; display: flex; justify-content: center; padding-top: 48px; box-sizing: border-box; overflow: hidden">{device(cu.case_detail(), 0.66)}</div>'
    return [("Mô hình kết nối, an toàn", page(f'<section style="padding: 96px 80px; display: flex; flex-direction: column; gap: 48px">'
                                                 f'{row(col(eyebrow("AN TOÀN & MINH BẠCH"), h2("Rõ ràng khi suôn sẻ, công bằng khi có sự cố"), principles, gap=24, extra="flex-grow: 1"), visual, gap=64, align="flex-start")}'
                                                 f'{diagram}{txt("Nội dung pháp lý chi tiết đang được rà soát và sẽ được công bố trong Điều khoản sử dụng.", "cap", C["t3"])}</section>', 1100))]


# ---------- L-006 download ----------
@frame("L-006", "App download / waitlist CTA", G_HOME)
def l006():
    def v(unav):
        title = "Onway sắp có mặt trên kho ứng dụng" if unav else "Tải Onway, đi thử chuyến đầu tiên"
        sub = "Để lại số điện thoại, chúng tôi nhắn bạn ngay khi ứng dụng sẵn sàng." if unav else "Có trên iOS và Android. Đang phục vụ tại TP. Hồ Chí Minh."
        action = (row(f'<div style="width: 340px">{field("", "", "Số điện thoại của bạn", ic="phone")}</div>', btn("Báo tôi khi ra mắt", "secondary", "lg"), gap=10) + stores(True, True, "Sắp có trên")
                  if unav else stores(True))
        qr = (f'<div style="background: #FFFFFF; border-radius: 20px; padding: 16px; display: flex; flex-direction: column; align-items: center; gap: 8px; flex-shrink: 0">{qr_svg(132)}'
              f'<span style="{TY["cap"]}; color: {C["t2"]}; font-weight: 600">Quét để tải ứng dụng</span></div>') if not unav else ""
        inner = (f'<div style="position: absolute; inset: 0">{dotgrid(LW, 560, "rgba(255,255,255,.12)")}</div>'
                 f'<div style="position: relative; display: flex; align-items: center; gap: 48px; padding: 0 80px; height: 100%">'
                 f'<div style="flex-grow: 1; display: flex; flex-direction: column; gap: 20px">{h2(title, "#FFFFFF", 52, 640)}{lead(sub, "rgba(255,255,255,.9)")}{action}</div>{qr}'
                 f'<div style="align-self: flex-end; margin-bottom: -180px">{device(cu.home(), 0.7)}</div></div>')
        return page(inner, 560, C["red"])
    return [("Có link tải", v(False)), ("Chưa có link — waitlist", v(True))]


# ---------- L-007 FAQ ----------
def faq_item(q, a="", open_=False):
    body_ = f'<div style="{TY["bmd"]}; font-size: 16px; color: {C["t2"]}; padding: 0 48px 22px 0">{a}</div>' if open_ else ""
    return (f'<div style="border-bottom: 1px solid {C["b2"]}"><button type="button" aria-expanded="{"true" if open_ else "false"}" style="display: flex; width: 100%; align-items: center; gap: 16px; padding: 22px 0; border: none; background: transparent; font-family: {FONT}; text-align: left; color: {C["t1"]}">'
            f'<span style="flex-grow: 1; {TY["hsm"]}">{q}</span><span style="width: 32px; height: 32px; border-radius: 999px; background: {C["inverse"] if open_ else C["sunken"]}; color: {"#FFFFFF" if open_ else C["t1"]}; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{icon("minus" if open_ else "plus", 16)}</span></button>{body_}</div>')


@frame("L-007", "FAQ", G_HOME)
def l007():
    def v(tab):
        if tab == 0:
            qs = [("Tôi thanh toán thế nào?", "Sau khi có tài xế, bạn chuyển khoản hoặc quét VietQR của tài xế, rồi gửi ảnh chứng từ trong ứng dụng. Tài xế xác nhận đã nhận đủ trước khi đón bạn. Onway không thu tiền hộ.", True),
                  ("Có trả tiền mặt được không?", ""), ("Nếu giá món tại quán khác trên ứng dụng?", ""), ("Tôi có thể huỷ đơn món không?", ""), ("Tôi chuyển nhầm số tiền thì sao?", "")]
        else:
            qs = [("Onway thu phí tài xế như thế nào?", "Gói ra mắt 1.000.000đ cho 12 tháng, tặng thêm 6 tháng. Onway thu 0% hoa hồng trên mọi chuyến và đơn. Dừng sớm được hoàn phí theo quý đã dùng.", True),
                  ("Tôi cần giấy tờ gì để đăng ký?", ""), ("Nếu khách không chuyển tiền?", ""), ("Vì sao tài khoản bị tạm khoá?", ""), ("Tôi có phải ứng tiền mua món không?", "")]
        side = col(eyebrow("HỎI ĐÁP"), h2("Câu hỏi thường gặp", size=44, maxw=380), f'<div style="width: 320px">{segmented(["Khách hàng", "Tài xế"], tab)}</div>',
                   card(row(icon_tile("help", 44, C["sunken"], C["t1"], 999), col(txt("Vẫn cần hỗ trợ?", "hsm"), txt("Đội hỗ trợ trả lời trong giờ hành chính.", "bsm", C["t2"]), gap=2), gap=12) + btn("Liên hệ chúng tôi", "outline", "md", full=True), pad=20, extra="width: 380px; margin-top: 16px"), gap=18, extra="width: 400px; flex-shrink: 0")
        return page(f'<section style="padding: 96px 80px; display: flex; gap: 80px; align-items: flex-start">{side}<div style="flex-grow: 1; border-top: 1px solid {C["b2"]}">{"".join(faq_item(*q) for q in qs)}</div></section>', 760)
    return [("Khách hàng", v(0)), ("Tài xế", v(1))]


# ---------- L-008 footer ----------
@frame("L-008", "Footer / legal links", G_HOME)
def l008():
    colh = lambda t, items: col(txt(t, "lbl", "#FFFFFF", extra="font-size: 14px"), *[f'<a href="#" style="{TY["bsm"]}; font-size: 14px; color: {C["tinv2"]}; text-decoration: none">{i}</a>' for i in items], gap=14)
    top = (f'<div style="display: flex; align-items: center; gap: 24px; padding: 32px; border-radius: 20px; background: {C["inverse2"]}; border: 1px solid rgba(255,255,255,.1)">'
           f'<img src="{APPICON}" alt="" width="64" height="64" style="width: 64px; height: 64px; border-radius: 16px">'
           f'<div style="flex-grow: 1">{txt("Onway — Đi xe & Đặt món", "hsm", "#FFFFFF")}{txt("0% hoa hồng. Giá rõ ràng. Tiền đi thẳng tới tài xế.", "bmd", C["tinv2"])}</div>{stores(True)}</div>')
    body_ = (f'<footer style="padding: 64px 80px 40px; display: flex; flex-direction: column; gap: 56px">{top}'
             + row(col(logo_img(28, True), txt("Nền tảng kết nối Đi xe & Đặt món tại Việt Nam.", "bsm", C["tinv2"], extra="font-size: 14px; max-width: 280px"), gap=16, extra="flex-grow: 1"),
                   colh("Sản phẩm", ["Đi xe", "Đặt món", "Cách hoạt động"]), colh("Tài xế", ["Đăng ký", "Phí nền tảng", "Giấy tờ cần có"]), colh("Hỗ trợ", ["Hỏi đáp", "Liên hệ", "Gửi khiếu nại"]),
                   colh("Pháp lý", ["Điều khoản sử dụng", "Chính sách quyền riêng tư"]), gap=72, align="flex-start")
             + f'<div style="border-top: 1px solid rgba(255,255,255,.14); padding-top: 24px; display: flex; {TY["cap"]}; font-size: 13px; color: {C["tinv2"]}"><span style="flex-grow: 1">© 2026 Công ty TNHH Onway · [ĐỊA CHỈ ĐĂNG KÝ KINH DOANH]</span><span>MST: [MÃ SỐ DOANH NGHIỆP]</span></div></footer>')
    return [("Quyền riêng tư, điều khoản, liên hệ", page(body_, 560, C["inverse"]))]


# ---------- sub pages ----------
def legal_page(title, updated, sections):
    toc = col(txt("Mục lục", "lbl", C["t3"]), *[f'<a href="#" style="{TY["bsm"]}; font-size: 14px; color: {C["t1"] if i == 0 else C["t2"]}; text-decoration: none; font-weight: {600 if i == 0 else 400}; padding: 6px 0 6px 12px; border-left: 2px solid {C["inverse"] if i == 0 else C["b2"]}">{i + 1}. {s[0]}</a>' for i, s in enumerate(sections)], gap=4, extra="width: 260px; flex-shrink: 0")
    body_ = "".join(f'<h2 style="margin: 0; {TY["hmd"]}">{i + 1}. {t}</h2><p style="margin: 0; {TY["blg"]}; color: {C["t2"]}">{p}</p>' for i, (t, p) in enumerate(sections))
    head = (f'<div style="padding: 56px 80px 48px; background: {C["page"]}; border-bottom: 1px solid {C["b2"]}; display: flex; flex-direction: column; gap: 12px">'
            f'{txt("Pháp lý", "lbl", C["t3"])}<h1 style="margin: 0; {TY["dmd"]}">{title}</h1>{txt(updated, "bsm", C["t3"])}</div>')
    return page(nav() + head + f'<section style="padding: 48px 80px; display: flex; gap: 64px; align-items: flex-start">{toc}<div style="max-width: 760px; display: flex; flex-direction: column; gap: 20px">'
                f'{banner("warning", "Bản nháp chờ rà soát pháp lý", "Nội dung dưới đây là khung cấu trúc; văn bản chính thức sẽ thay thế trước khi ra mắt.")}{body_}</div></section>', 1280)


@frame("L-009", "Terms page", G_SUB)
def l009():
    return [("Khung nội dung pháp lý", legal_page("Điều khoản sử dụng", "Cập nhật: [NGÀY HIỆU LỰC]", [
        ("Onway là nền tảng kết nối", "Onway cung cấp phần mềm kết nối khách hàng, tài xế và quán. Onway không phải bên vận chuyển hay bán món. [NỘI DUNG PHÁP LÝ]"),
        ("Giá và thanh toán", "Giá chuyến và phí giao do Onway đề xuất, hiển thị trước khi xác nhận. Khách chuyển khoản trực tiếp cho tài xế. Onway không giữ tiền. [NỘI DUNG PHÁP LÝ]"),
        ("Phí nền tảng của tài xế", "Gói ra mắt và chính sách hoàn phí theo quý. Phí nền tảng không phải tiền cọc hay ký quỹ. [NỘI DUNG PHÁP LÝ]"),
        ("Khiếu nại và tranh chấp", "Nguyên tắc bên nào có lỗi bên đó chịu trách nhiệm; quy trình xem xét và kháng nghị. [NỘI DUNG PHÁP LÝ]"),
        ("Tạm khoá tài khoản", "Điều kiện khoá tạm, thời hạn xem xét 24 giờ và quyền kháng nghị. [NỘI DUNG PHÁP LÝ]")]))]


@frame("L-010", "Privacy page", G_SUB)
def l010():
    return [("Khung nội dung quyền riêng tư", legal_page("Chính sách quyền riêng tư", "Cập nhật: [NGÀY HIỆU LỰC]", [
        ("Dữ liệu Onway thu thập", "Số điện thoại, hồ sơ, vị trí khi dùng ứng dụng, ảnh chứng từ, mã thiết bị đã mã hoá. [NỘI DUNG PHÁP LÝ]"),
        ("Mục đích sử dụng", "Kết nối chuyến/đơn, xử lý khiếu nại, chống gian lận. Onway không dùng AI tự động kết luận vi phạm. [NỘI DUNG PHÁP LÝ]"),
        ("Thời gian lưu trữ", "Chat lưu 7 ngày trừ khi liên quan khiếu nại; GPS, KYC, bằng chứng và audit theo chính sách lưu trữ. [NỘI DUNG PHÁP LÝ]"),
        ("Quyền của bạn", "Xem, tải xuống, yêu cầu xoá dữ liệu; ngoại lệ theo nghĩa vụ pháp lý và tranh chấp đang mở. [NỘI DUNG PHÁP LÝ]"),
        ("Liên hệ", "[EMAIL BẢO VỆ DỮ LIỆU]")]))]


@frame("L-011", "Contact/support page", G_SUB)
def l011():
    def ct(ic, t, d, a, tone):
        return (f'<div style="flex: 1; display: flex; flex-direction: column; gap: 12px; padding: 28px; border-radius: 20px; background: {tone}">{icon_tile(ic, 52, "#FFFFFF", C["t1"], 14)}'
                f'{txt(t, "hsm", extra="font-size: 20px")}{txt(d, "bmd", C["t2"])}{a}</div>')
    form = card(txt("Gửi tin nhắn cho Onway", "hmd") + row(f'<div style="flex: 1">{field("Họ tên", "")}</div>', f'<div style="flex: 1">{field("Số điện thoại", "")}</div>', gap=16)
                + select("Bạn là", "Khách hàng") + field("Nội dung", "", textarea=True) + row(btn("Gửi liên hệ", "primary", "lg", "send"), spacer(), txt("Phản hồi trong 1 ngày làm việc", "cap", C["t3"])), pad=32, gap=16, extra="flex: 3")
    info = col(txt("Thông tin liên hệ", "hsm"), row(icon("mail", 18, C["t2"]), txt("[EMAIL HỖ TRỢ]", "bmd"), gap=10), row(icon("phone", 18, C["t2"]), txt("[SỐ TỔNG ĐÀI]", "bmd"), gap=10),
               row(icon("map-pin", 18, C["t2"]), txt("[ĐỊA CHỈ VĂN PHÒNG], TP. Hồ Chí Minh", "bmd"), gap=10),
               f'<div style="height: 200px; border-radius: 16px; overflow: hidden; border: 1px solid {C["b2"]}; margin-top: 8px">{map_svg(420, 200, pins=[("dropoff", 0.5, 0.6)], labels=False)}</div>', gap=14, extra="flex: 2")
    return [("Khách, tài xế, đối tác", page(nav() + f'<section style="padding: 64px 80px 96px; display: flex; flex-direction: column; gap: 40px">{col(eyebrow("LIÊN HỆ"), h2("Chúng tôi có thể giúp gì?"), gap=14)}'
                                                  + row(ct("user", "Khách hàng", "Vấn đề với chuyến đi hoặc đơn món? Gửi khiếu nại ngay trong ứng dụng để được xử lý nhanh nhất.", btn("Mở ứng dụng", "outline", "md"), C["page"]),
                                                        ct("bike", "Tài xế", "Hỏi về đăng ký, phí nền tảng, khoá tài khoản hoặc kháng nghị.", txt("[SỐ TỔNG ĐÀI TÀI XẾ]", "bmd", extra="font-weight: 700"), C["warn_bg"]),
                                                        ct("store", "Quán & đối tác", "Muốn đưa quán lên Onway hoặc hợp tác?", txt("[EMAIL ĐỐI TÁC]", "bmd", extra="font-weight: 700"), C["ok_bg"]), gap=20)
                                                  + row(form, info, gap=40, align="flex-start") + "</section>", 1400))]
