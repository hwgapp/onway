import json, os, re, shutil
from build import FLOWS

REPO = "/home/user/onway"
MK = os.path.join(REPO, "doc/4-DESIGN/mockups")
CANVAS_URL = "https://claude.ai/artifact/4cHL1pqQYuNLWsi2m2H44Y"
CANVAS_URL2 = "https://claude.ai/artifact/CxkTKZioRmXx1xWKrzYf79"
HERE = os.path.dirname(os.path.abspath(__file__))
man = json.load(open(os.path.join(HERE, "..", "canvas", "manifest.json"))) + json.load(open(os.path.join(HERE, "..", "canvas2", "manifest.json")))
man.sort(key=lambda f: "CDAL".index(f["id"][0]) * 1000 + int(f["id"][2:]))
CV = lambda fid: "Customer & Driver" if fid[0] in "CD" else "Admin & Landing"

# frame map: id -> (prd screen, type, required states, flow)
fm = {}
for line in open(os.path.join(REPO, "doc/4-DESIGN/08-full-app-screen-frame-map.md")):
    m = re.match(r"\| ([CDAL]-\d{3}) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|", line)
    if m:
        fm[m.group(1)] = [x.strip() for x in m.groups()[1:]]

PAGE_NAME = {"customer": "Customer App", "driver": "Driver App", "admin": "Admin Portal", "landing": "Landing Web"}
os.makedirs(os.path.join(MK, "raw", "generator"), exist_ok=True)

# ---------- screen-map ----------
out = ["# Screen Map", "",
       f"Canvas (Design artifact, private — chia sẻ từ menu Share của trang): [Customer & Driver]({CANVAS_URL}) và [Admin & Landing]({CANVAS_URL2}); mỗi canvas tối đa 200 file nên tách làm hai. Mỗi `Frame ID` là một artboard; các trạng thái nằm cạnh nhau trong artboard, có nhãn trạng thái phía trên.", "",
       "Tên export theo `07-claude-design-output-contract.md`: `<Frame ID> - <Frame Name> - <State> - <Platform>`.", "",
       "| Frame ID | PRD Screen | Frame Name | Frame/Mockup Name | Canvas | Platform | Flow ID | States Delivered | Status |",
       "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for f in man:
    prd, _, typ, req, flow = (fm.get(f["id"]) or ["", "", "", "", ""])[0:5] if f["id"] in fm else ["—", "", "", "", "—"]
    prd = fm[f["id"]][0] if f["id"] in fm else "—"
    flow = fm[f["id"]][4] if f["id"] in fm else "—"
    out.append(f"| {f['id']} | {prd} | {f['name']} | `{f['id']} - {f['name']} - {f['platform']}` · `{f['file']}` | {CV(f['id'])} | {f['platform']} | {flow} | {', '.join(f['states'])} | Ready |")
missing = [k for k in fm if k not in {f['id'] for f in man}]
out += ["", f"Tổng: {len(man)} frame, {sum(len(f['states']) for f in man)} trạng thái. Frame thiếu so với frame map: {', '.join(missing) if missing else 'không có'}."]
open(os.path.join(MK, "screen-map.md"), "w").write("\n".join(out) + "\n")

# ---------- flow-map ----------
out = ["# Flow Map", "", "Các mã frame trong cột Steps có liên kết Play trên canvas (nút CTA chính dẫn tới frame kế tiếp).", "",
       "| Flow ID | Flow Name | Entry Screen | Steps / Screens | Success Exit | Failure / Edge Screens |", "| --- | --- | --- | --- | --- | --- |"]
for fid, name, entry, chain, chain2, succ, edge in FLOWS:
    steps = " → ".join(chain) + (f"; phía tài xế/phụ: {' → '.join(chain2)}" if chain2 else "")
    out.append(f"| {fid} | {name} | {entry} | {steps} | {succ} | {edge} |")
out += ["", "## Luồng phụ", "", "| Flow | Steps / Screens | Ghi chú |", "| --- | --- | --- |",
        "| Khởi động khách | C-000 → C-001 → C-002 → C-003 → C-004 → C-005 → C-006 | C-000 có trạng thái bắt buộc cập nhật |",
        "| Khởi động tài xế | D-000 → D-001 → D-002 → D-003 | Tài xế mới vào UF-004; tài xế đã kích hoạt vào D-015 |",
        "| Tài khoản khách | C-009 → C-010 / C-011 / C-066 / C-059 / C-062 → C-067 | C-067 có trạng thái bị hạn chế do khiếu nại đang mở |",
        "| Lịch sử & hồ sơ tài xế | D-051 → D-049 / D-053 → D-054 / D-055 → D-056 | |",
        "| Admin đăng nhập | A-000 → A-001 → A-005 | A-003 khi thiếu quyền; A-004 tìm nhanh ⌘K |",
        "| Danh mục Food | A-040 → A-041 → A-042 → A-043 → A-044 → A-045 → A-046 → A-047 → A-049 | A-048 nhập file thủ công (không AI/OCR) |",
        "| Phí nền tảng (Finance) | A-070 → A-071 | cùng dữ liệu với A-033 |",
        "| Quyền riêng tư | C-067 / D-059 → A-075 → A-076 | |",
        "| Landing | L-001 → L-002 → L-003 → L-004 → L-005 → L-006 → L-007 → L-008; L-009, L-010, L-011 | |"]
open(os.path.join(MK, "flow-map.md"), "w").write("\n".join(out) + "\n")

# ---------- state coverage ----------
KEYS = [("Default", ["Mặc định", "Danh sách", "Tất cả", "Desktop", "Mobile", "Đang", "Chờ", "Tại quán", "Đi tới", "Đã có", "Kết quả", "QR", "Thông tin", "Xe máy", "Chọn", "Có ", "Bản nháp", "Văn bản", "Giải thích", "Tìm", "Xem", "Đếm", "Khung", "Ride", "Đi xe", "0% ", "Hero", "Mô hình", "Khách", "Quyền", "Mẫu", "SLA", "Nội dung", "Hồ sơ", "Người", "Ma trận", "Trước", "Giá", "Loại", "Xác nhận", "Cờ", "Bằng chứng", "Đối chiếu", "Planned", "Active", "Kéo", "Thêm", "Đi ", "Ảnh", "Lịch sử", "Soạn", "Quyết định", "Ghi chú", "Bắt buộc", "Duyệt", "Hoàn thành", "Tạo", "5 sao", "Chuyển", "Mở", "Thu gọn", "Không có quyền", "Đã kết luận", "Gọi", "Dịch vụ", "Theo", "Việc", "Ngoại tuyến", "Trực tuyến", "Bình thường", "Ride/Food", "Tìm kiếm", "Khoá", "Cảnh báo", "Món", "Phạm vi", "Bất biến", "Hết hạn", "Sửa", "Nhập", "Đóng", "Mặt", "Chân dung", "PDF"]),
        ("Loading", ["Đang tải", "Đang tìm", "Đang tính", "Đang ghép", "Đang gửi"]),
        ("Empty", ["Trống", "Không có kết quả", "Chưa có", "Không có tài xế", "Không có việc", "Không có khu vực", "Chưa có dữ liệu", "Không có hoạt động"]),
        ("Error", ["Lỗi", "thất bại", "Sai ", "không hợp lệ", "Không tính được", "Không lấy được", "Bị từ chối", "Chồng", "Xung đột", "gửi lỗi", "tự cắt", "Suy giảm", "Không hợp lệ"]),
        ("Offline", ["Mất mạng", "Mất kết nối", "kết nối lại"]),
        ("No Permission", ["quyền", "Không đủ quyền", "Không có quyền", "Đã từ chối"]),
        ("Locked", ["khoá", "Khoá", "Bị khoá", "Giới hạn", "bị khoá", "Bắt buộc cập nhật", "tạm dừng", "Tạm dừng", "hạn chế", "Không khả dụng", "Hết hạn", "Hết thời gian"]),
        ("Success", ["Hoàn thành", "Đã gửi", "Đã giao", "Đã duyệt", "Đã nhận", "đồng ý", "Đã kết luận", "Đã xuất bản", "Đang hiệu lực", "Đã đóng hình", "Có quyền", "Xác nhận có lý do"])]
out = ["# State Coverage", "", "Yes = có ít nhất một trạng thái tương ứng được vẽ trong artboard; — = không vẽ riêng (không áp dụng hoặc dùng mẫu chung A-069 / pattern của frame khác, xem Notes).", "",
       "| Screen ID | Default | Loading | Empty | Error | Offline | No Permission | Paywall/Locked | Success | Notes |",
       "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for f in man:
    sts = f["states"]
    cells = []
    for i, (k, kws) in enumerate(KEYS):
        hit = any(any(kw in s for kw in kws) for s in sts)
        if k == "Default":
            hit = True
        cells.append("Yes" if hit else "—")
    out.append(f"| {f['id']} | " + " | ".join(cells) + f" | {'; '.join(sts)} |")
open(os.path.join(MK, "state-coverage.md"), "w").write("\n".join(out) + "\n")

# ---------- export notes ----------
notes = f"""# Frame Export Notes

## Nguồn

- Canvas “Customer & Driver”: [{CANVAS_URL}]({CANVAS_URL}) — trang `Tổng quan`, `Customer App`, `Driver App`.
- Canvas “Admin & Landing”: [{CANVAS_URL2}]({CANVAS_URL2}) — trang `Tổng quan`, `Admin Portal`, `Landing Web`.
- Tách hai canvas vì trình canvas chỉ tải tối đa 200 file mỗi canvas. Cả hai là artifact riêng tư, cần chia sẻ từ menu Share của trang.
- Design system: Onway (`claude.ai/code/artifact/3a7f770f-…`), đã cài vào canvas tại `project/ds/onway/tokens.json` để Theme menu dùng đúng màu/chữ.
- Nguồn sinh frame (Python, dựng từ token): `raw/generator/`. Chạy `python3 build.py` trong thư mục đó để sinh lại `canvas/project/*.dc.html`.

## Quy ước

| Mục | Giá trị |
| --- | --- |
| Tên artboard | `<Frame ID> - <Frame Name> - <Platform>`; file `<Frame ID>.dc.html` |
| Tên trạng thái | nhãn phía trên mỗi màn trong artboard → export `<Frame ID> - <Frame Name> - <State> - <Platform>` |
| Mobile | 390×844 (iPhone), vùng an toàn trên 44px, dưới 34px; không vẽ status bar giả |
| Admin | 1440×900, sidebar 248px, header 64px |
| Landing | 1440 rộng (chiều cao theo section); L-001 có thêm bản mobile 390×900 |
| Ngôn ngữ | Tiếng Việt; tiền tệ dạng `48.000đ` (JetBrains Mono) |
| Theme | Sáng cho cả 3 app (theme tối Driver là P1) |
| Prototype | {sum(1 for _ in man)} artboard; CTA chính dùng link Play sang frame kế tiếp |

## Tài sản dùng

| Asset ID | Asset Name | Type | Used In | Required Format | Notes |
| --- | --- | --- | --- | --- | --- |
| AST-001 | Logo Onway | svg | Admin sidebar, login, landing, splash | svg | `system/assets/logo.svg`, bản trắng `logo-white.svg` trên nền đỏ/than |
| AST-002 | App icon khách | svg | C-001, L-006 | svg/png | `logo-appicon.svg` nền đỏ |
| AST-003 | App icon tài xế | svg | D-001 | svg/png | `logo-appicon-ink.svg` nền than |
| AST-004 | Logo mark | svg | Admin thu gọn, bìa | svg | `logo-mark.svg` |
| AST-005 | Ảnh món/quán | placeholder | C-033…C-039, A-040…A-046 | jpg/webp | Khối màu + icon; cần ảnh thật từ catalog |
| AST-006 | Ảnh chứng từ/giấy tờ | placeholder | C-025, D-023, A-031, A-052… | — | Placeholder có nhãn; dữ liệu thật là private media |
| AST-007 | Bản đồ | placeholder | màn có bản đồ | — | SVG minh hoạ theo token `map-*`; thực tế là HERE Maps |

## Known gaps / Design fix list

| ID | Package | Issue | Impact | Needed Before | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| DF-001 | UI Workflow | Component được vẽ bằng markup theo token, chưa mount component bundle thật (README design system không công bố bundle global) | Dev dùng spec component trong `system/` làm chuẩn, mockup chỉ tham chiếu thị giác | UI implementation | Design | Open |
| DF-002 | UI Workflow | Bản đồ, ảnh món, ảnh chứng từ là placeholder | Không ảnh hưởng logic; cần asset thật khi QA hình ảnh | G8 | Design/Ops | Open |
| DF-003 | UI Workflow | Số liệu mẫu (giá/km, phí giao, wave, ngưỡng khoá) trong A-023…A-026 là ví dụ minh hoạ | Không dùng làm cấu hình thật | Cấu hình rollout | Ops/User | Open — OQ-025 |
| DF-004 | UI Workflow | Nội dung pháp lý L-009/L-010, thông tin doanh nghiệp ở footer là placeholder `[…]` | Cần legal review | Ra mắt | Legal | Open |
| DF-005 | UI Workflow | Thời gian tài xế chờ ở điểm đón (vẽ 5 phút, không phí chờ) chưa có trong BRD/PRD | Ảnh hưởng C-029, D-025, D-026, A-023 | Ride PRD detail | User | Open — OQ-022 |
| DF-006 | UI Workflow | Kết quả sau khi khách từ chối / hết giờ đề xuất Food (huỷ hay giao phần còn lại, ai hoàn tiền) vẽ theo hướng “Onway xem xét” | Ảnh hưởng C-047, C-049, D-038 | Food dispute policy | User/Legal | Open — OQ-023 |
| DF-007 | UI Workflow | Cho phép khách ẩn số điện thoại với tài xế (C-010, D-057 “Không khả dụng”) | BR-COMM-001 nói hai bên gọi số thật | PRD chi tiết | User | Open — OQ-024 |
| DF-008 | UI Workflow | Chưa có theme tối (Driver P1) và chưa vẽ trạng thái chữ 200% | Accessibility QA | G6 | Design | Deferred |
"""
open(os.path.join(MK, "frame-export-notes.md"), "w").write(notes)

readme = f"""# UI Workflow Package

Output UI Workflow cho P0 theo `../07-claude-design-output-contract.md` và `../08-full-app-screen-frame-map.md`.

- Canvas: [Customer & Driver]({CANVAS_URL}) và [Admin & Landing]({CANVAS_URL2}) — {len(man)} frame, {sum(len(f['states']) for f in man)} trạng thái (Customer 68, Driver 60, Admin 77, Landing 11).
- `screen-map.md`: Frame ID → artboard, trạng thái đã vẽ.
- `flow-map.md`: UF-001…UF-007 và luồng phụ.
- `state-coverage.md`: default/loading/empty/error/offline/no permission/locked/success theo frame.
- `frame-export-notes.md`: quy ước export, asset, known gaps (DF-001…DF-008).
- `raw/`: `canvas.json`, `manifest.json` và `generator/` (nguồn sinh artboard từ token Onway).
"""
open(os.path.join(MK, "README.md"), "w").write(readme)

# raw
json.dump(man, open(os.path.join(MK, "raw", "manifest.json"), "w"), ensure_ascii=False, indent=1)
shutil.copy(os.path.join(HERE, "..", "canvas", "project", "canvas.json"), os.path.join(MK, "raw", "canvas-customer-driver.json"))
shutil.copy(os.path.join(HERE, "..", "canvas2", "project", "canvas.json"), os.path.join(MK, "raw", "canvas-admin-landing.json"))
if os.path.exists(os.path.join(MK, "raw", "canvas.json")): os.remove(os.path.join(MK, "raw", "canvas.json"))
for fn in ["lib.py", "reg.py", "customer.py", "driver.py", "admin.py", "landing.py", "build.py"]:
    shutil.copy(os.path.join(HERE, fn), os.path.join(MK, "raw", "generator", fn))
print("ok", len(man))
