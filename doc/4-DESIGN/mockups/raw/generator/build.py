import json, os, re, datetime
import customer, driver, admin, landing
from reg import REG
from lib import *

OUT = os.path.join(os.path.dirname(__file__), "..", "canvas")
PROJ = os.path.join(OUT, "project")
os.makedirs(PROJ, exist_ok=True)

PLATFORM = {"C": "iPhone", "D": "iPhone", "A": "Web 1440", "L": "Web"}
APPNAME = {"C": "Customer App", "D": "Driver App", "A": "Admin Portal", "L": "Landing Web"}
PAGE = {"C": "customer", "D": "driver", "A": "admin", "L": "landing"}

FLOWS = [
    ("UF-001", "Khách đặt Ride đến hoàn thành", "C-006", ["C-006", "C-012", "C-014", "C-015", "C-016", "C-017", "C-019", "C-023", "C-024", "C-025", "C-028", "C-029", "C-030", "C-031", "C-052"],
     ["D-015", "D-019", "D-020", "D-022", "D-023", "D-025", "D-026", "D-027", "D-028"], "C-031 / D-028",
     "C-007, C-018, C-020, C-021, C-022, C-026, C-027, C-032, D-021, D-024, D-029, A-053"),
    ("UF-002", "Khách đặt Food đến đã giao", "C-006", ["C-006", "C-033", "C-035", "C-036", "C-037", "C-038", "C-039", "C-040", "C-042", "C-043", "C-045", "C-046", "C-050", "C-051", "C-052"],
     ["D-015", "D-030", "D-031", "D-032", "D-034", "D-040", "D-041", "D-042"], "C-051 / D-042",
     "C-034, C-041, C-044, C-065, D-033, D-043, A-053"),
    ("UF-003", "Thay đổi giá/món tại quán", "D-034", ["D-034", "D-035", "D-036", "C-047", "C-048", "D-037", "D-039"], [], "D-037 → D-040",
     "C-049, D-038, D-043"),
    ("UF-004", "Đăng ký & kích hoạt tài xế", "D-001", ["D-001", "D-002", "D-003", "D-004", "D-005", "D-006", "D-007", "D-008", "D-009", "A-030", "A-031", "A-032", "D-011", "D-012", "D-013", "A-070", "A-071", "D-014"], [],
     "D-014 → D-015", "D-010, A-032 (từ chối), D-013 (bị từ chối)"),
    ("UF-005", "Khiếu nại & xử lý gian lận/tranh chấp thủ công", "C-053", ["C-053", "C-054", "A-050", "A-051", "A-052", "A-053", "A-054", "A-055", "A-056", "A-059", "C-063"],
     ["A-036", "D-047", "D-048", "A-037", "A-038"], "A-059 / A-038", "A-057, A-060, D-055, D-056, C-062"),
    ("UF-006", "Admin rollout vùng & chính sách", "A-010", ["A-010", "A-012", "A-013", "A-014", "A-015", "A-017", "A-018", "A-019", "A-022", "A-023", "A-027"], [], "A-019 / A-027",
     "A-016, A-020, A-021, A-065, C-007, D-018"),
    ("UF-007", "Chat & gọi trực tiếp", "C-028", ["C-028", "C-055", "C-064", "D-022", "D-044", "D-057"], [], "C-055 / D-044", "C-056, C-057, C-058, D-045, D-046"),
]

SIZE_RE = re.compile(r"width: (\d+)px; height: (\d+)px")


def measure(html):
    m = SIZE_RE.search(html)
    return int(m.group(1)), int(m.group(2))


def build_board(states):
    gap = 64
    sizes = [measure(h_) for _, h_ in states]
    w = sum(s[0] for s in sizes) + gap * (len(states) - 1)
    hh = max(s[1] for s in sizes) + 40
    items = ""
    for (lab, html), (sw, sh) in zip(states, sizes):
        items += (f'<div style="display: flex; flex-direction: column; gap: 12px; width: {sw}px; flex-shrink: 0">'
                  f'<div style="height: 28px; display: flex; align-items: center; {TY["lbl"]}; font-size: 14px; color: {C["t2"]}">{lab}</div>{html}</div>')
    root = f'<div style="width: {w}px; height: {hh}px; display: flex; gap: {gap}px; align-items: flex-start; font-family: {FONT}">{items}</div>'
    return root, w, hh


def cover(keep="CDAL", other_url=None):
    W, H = 1760, 1160
    apps = [("Customer App", "68 frame", "iPhone 390×844", APPICON, "Đi xe, Đặt món, thanh toán trực tiếp, chat, đánh giá, khiếu nại, quyền riêng tư"),
            ("Driver App", "60 frame", "iPhone 390×844", APPICON_INK, "Đăng ký/KYC, phí nền tảng, nhận việc, Ride/Food job, đề xuất thay đổi, khoá & kháng nghị"),
            ("Admin Portal", "77 frame", "Web 1440×900", MARK, "Vùng & polygon, chính sách, tài xế, phí nền tảng, danh mục, khiếu nại/gian lận, audit, RBAC"),
            ("Landing Web", "11 frame", "Web 1440 · Mobile 390", MARK, "Hero, giá trị, tuyển tài xế, cách hoạt động, an toàn, FAQ, pháp lý, liên hệ")]
    apps = [a for a in apps if a[0][0] in {'C': 'C', 'D': 'D', 'A': 'A', 'L': 'L'}.keys() and {'Customer App': 'C', 'Driver App': 'D', 'Admin Portal': 'A', 'Landing Web': 'L'}[a[0]] in keep]
    other = (f'<div style="{TY["bsm"]}; font-size: 14px; color: {C["t2"]}">Phần còn lại ở canvas <a href="{other_url[1]}" style="font-weight: 600">{other_url[0]}</a> (mỗi canvas tối đa 200 file).</div>') if other_url else ''
    appc = "".join(card(row(f'<img src="{ic}" alt="" width="48" height="48" style="width: 48px; height: 48px; border-radius: 12px">', col(txt(n, "hsm"), txt(f"{c} · {p}", "cap", C["t3"]), gap=2), gap=14) + txt(d, "bsm", C["t2"]), pad=20, gap=12, extra="flex: 1")
                   for n, c, p, ic, d in apps)
    flows = ""
    for fid, name, _, chain, chain2, succ, edge in FLOWS:
        lk = lambda c, fs=12: (f'<a href="{c}.dc.html" style="font-family: {MONO}; font-size: {fs}px; text-decoration: none; color: {C["t1"]}">{c}</a>' if c[0] in keep else f'<span style="font-family: {MONO}; font-size: {fs}px; color: {C["t3"]}">{c}</span>')
        ch = " → ".join(lk(c) for c in chain)
        ch2 = (f'<div style="{TY["cap"]}; color: {C["t2"]}; margin-top: 4px">Tài xế / phụ: ' + " → ".join(lk(c) for c in chain2) + "</div>") if chain2 else ""
        flows += (f'<div style="display: grid; grid-template-columns: 90px 260px minmax(0, 1fr); gap: 16px; padding: 12px 0; border-bottom: 1px solid {C["b1"]}">'
                  f'<span style="font-family: {MONO}; font-size: 13px; font-weight: 600">{fid}</span><span style="{TY["bsm"]}; font-weight: 600; font-size: 14px">{name}</span>'
                  f'<div><div style="line-height: 1.7">{ch}</div>{ch2}<div style="{TY["cap"]}; color: {C["t3"]}; margin-top: 4px">Ngoại lệ: {edge}</div></div></div>')
    tones = row(*[pill(s) for s in ["matching", "arrived", "inProgress", "completed", "disputed", "cancelled"]], gap=8)
    root = (f'<div style="width: {W}px; height: {H}px; box-sizing: border-box; padding: 64px; background: #FFFFFF; font-family: {FONT}; color: {C["t1"]}; display: flex; flex-direction: column; gap: 32px; border: 1px solid {C["b2"]}">'
            + row(col(logo_img(40), f'<h1 style="margin: 16px 0 0; {TY["dlg"]}">UI Workflow — P0</h1>',
                      txt("216 frame · 371 trạng thái · theo 08-full-app-screen-frame-map.md và Onway Design System. Nội dung tiếng Việt; không có ví, tiền mặt, COD, cổng thanh toán hay thương lượng giá.", "blg", C["t2"], extra="max-width: 980px"), gap=6),
                  spacer(), col(txt("Cập nhật 24/09/2026", "cap", C["t3"]), tones, gap=8, extra="align-items: flex-end"), align="flex-end")
            + row(appc, gap=16) + other
            + f'<div><div style="{TY["ovl"]}; color: {C["t3"]}; margin-bottom: 4px">Luồng chính (bấm mã frame để mở — chế độ Play; mã màu xám nằm ở canvas còn lại)</div>{flows}</div>'
            + "</div>")
    return root, W, H


def main(keep="CDAL", outdir=None, title="Onway UI Workflow", other_url=None):
    files = {}
    boards = {}
    order = []
    notes = {}
    pages = [{"id": "overview", "name": "Tổng quan"}, {"id": "customer", "name": "Customer App"}, {"id": "driver", "name": "Driver App"}, {"id": "admin", "name": "Admin Portal"}, {"id": "landing", "name": "Landing Web"}]
    # cover
    global PROJ, OUT
    if outdir:
        OUT = outdir; PROJ = os.path.join(OUT, "project"); os.makedirs(PROJ, exist_ok=True)
    pages = [p for p in pages if p["id"] == "overview" or {"customer": "C", "driver": "D", "admin": "A", "landing": "L"}[p["id"]] in keep]
    root, w, hh = cover(keep, other_url)
    files["Main.dc.html"] = dc_file("Onway UI Workflow — Tổng quan", root, w, hh)
    boards["Main.dc.html"] = {"x": 0, "y": 0, "w": w, "h": hh, "title": "Tổng quan · UI Workflow P0", "page": "overview", "is_interactive": True}
    order.append("Main.dc.html")
    manifest = []
    # group frames by page then group
    by_page = {}
    for f in REG:
        p = f["id"][0]
        if p not in keep:
            continue
        by_page.setdefault(p, [])
        by_page[p].append(f)
    for p, frames in by_page.items():
        groups = []
        for f in frames:
            if not groups or groups[-1][0] != f["group"]:
                groups.append((f["group"], []))
            groups[-1][1].append(f)
        y = 0
        maxw = 9000 if p in "CD" else 12000
        for gi, (gname, fs) in enumerate(groups):
            title_y = y
            y += 260
            x = 0
            row_h = 0
            first_row = True
            vertical = "xếp dọc" in gname
            for f in fs:
                states = f["fn"]()
                root, w, hh = build_board(states)
                fn = f"{f['id']}.dc.html"
                plat = PLATFORM[p]
                btitle = f"{f['id']} - {f['name']} - {plat}"
                files[fn] = dc_file(f"{f['id']} {f['name']}", root, w, hh)
                if vertical and x == 0 and order[-1] != "Main.dc.html" and boards[order[-1]].get("page") == PAGE[p] and boards[order[-1]]["y"] >= title_y + 260:
                    pass
                if vertical:
                    x = 0
                    if row_h:
                        y += row_h + 120
                    row_h = 0
                elif x > 0 and x + w > maxw:
                    x = 0
                    y += row_h + 120
                    row_h = 0
                inter = ".dc.html\"" in root
                b = {"x": x, "y": y, "w": w, "h": hh, "title": btitle, "page": PAGE[p]}
                if inter:
                    b["is_interactive"] = True
                boards[fn] = b
                order.append(fn)
                manifest.append(dict(id=f["id"], name=f["name"], group=gname, platform=plat, states=[s[0] for s in states], file=fn, page=PAGE[p]))
                x = 0 if vertical else x + w + 80
                row_h = hh if vertical else max(row_h, hh)
            notes[f"{p}g{gi}"] = {"x": 0, "y": title_y, "text": gname, "kind": "title1", "page": PAGE[p], "maxW": 6000}
            y += row_h + 200
    now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": now}, "title": title, "launch": {"view": "canvas", "page": "overview"}, "pages": pages,
              "boards": boards, "order": order, "notes": notes,
              "designSystems": [{"title": "Onway", "namespace": "onway", "artifact": "https://claude.ai/code/artifact/3a7f770f-a60c-4755-85f8-ced071f0c577", "version": "1790235852-eb26", "copiedAt": now}]}
    for fn, s in files.items():
        open(os.path.join(PROJ, fn), "w").write(s)
    json.dump(canvas, open(os.path.join(PROJ, "canvas.json"), "w"), ensure_ascii=False, indent=1)
    json.dump(manifest, open(os.path.join(OUT, "manifest.json"), "w"), ensure_ascii=False, indent=1)
    tot = sum(len(s.encode()) for s in files.values())
    print(len(files), "files", tot // 1024, "KB")



BLOB_MAP_2 = {"c7ff600d13e459a1bab4b80d7ba54fe0": "7cfc63e835de48179cda302aa5f27f63", "b0c1f38af128121144abbe2640b172e6": "5c4bba714d01cd1491071632a2107dc8",
              "4c72993bfe32c631035ece42b011b2fe": "b7bb94bd5a21010622582625abb3a48b", "bfe7d08fe5a3c459cd669d208598be50": "d8fc197047c201371b620df2e1b8544d",
              "06eac3ca73fc016d5f8aa748a3291d26": "0c49cf03f609f41e9fe6b3d56f2744af", "b27d6f6350f2ce87db18a8c7e282d191": "d916190aa27c29427a5e7dd108d22168"}


def remap_blobs(proj):
    import glob
    for f in glob.glob(os.path.join(proj, "*.dc.html")):
        s = open(f).read()
        for a, b in BLOB_MAP_2.items():
            s = s.replace(a, b)
        open(f, "w").write(s)


if __name__ == "__main__":
    import sys
    URL1 = "https://claude.ai/artifact/4cHL1pqQYuNLWsi2m2H44Y"
    URL2 = "https://claude.ai/artifact/CxkTKZioRmXx1xWKrzYf79"
    base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    main("CD", os.path.join(base, "canvas"), "Onway UI Workflow — Customer & Driver", ("Onway UI Workflow — Admin & Landing", URL2))
    main("AL", os.path.join(base, "canvas2"), "Onway UI Workflow — Admin & Landing", ("Onway UI Workflow — Customer & Driver", URL1))
    remap_blobs(os.path.join(base, "canvas2", "project"))
