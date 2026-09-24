# Onway UI Workflow generator — shared primitives built from Onway design-system tokens.
import html as _html

LOGO = "/_blob/c7ff600d13e459a1bab4b80d7ba54fe0"
LOGO_WHITE = "/_blob/b0c1f38af128121144abbe2640b172e6"
MARK = "/_blob/4c72993bfe32c631035ece42b011b2fe"
MARK_WHITE = "/_blob/bfe7d08fe5a3c459cd669d208598be50"
APPICON = "/_blob/06eac3ca73fc016d5f8aa748a3291d26"
APPICON_INK = "/_blob/b27d6f6350f2ce87db18a8c7e282d191"

# ---- tokens (light theme) ----
C = {
    "page": "#F5F5F4", "card": "#FFFFFF", "sunken": "#EDEDEB", "hover": "#F5F5F4", "active": "#EDEDEB",
    "inverse": "#0F0E0E", "inverse2": "#1C1B1B", "overlay": "rgba(15,14,14,.56)",
    "t1": "#0F0E0E", "t2": "#555453", "t3": "#6F6E6D", "tdis": "#A3A2A0", "tinv": "#FFFFFF", "tinv2": "#A3A2A0",
    "brand": "#C31834", "red": "#E22240", "red600": "#C31834", "red700": "#9E1129",
    "b1": "#EDEDEB", "b2": "#E1E0DF", "b3": "#C9C8C6",
    "ok_bg": "#EFF8F3", "ok": "#238057", "ok_b": "#2E9E6B",
    "info_bg": "#F0F4FE", "info": "#3A63CC", "info_b": "#4C7DF0",
    "warn_bg": "#FDF6EA", "warn": "#8E621A", "warn_b": "#E2A33C",
    "acc_bg": "#F3F1FD", "acc": "#6354C4",
    "err_bg": "#FDF2F4", "err": "#C31834",
    "brand_bg": "#FDF2F4", "ink25": "#FAFAFA", "ink800": "#2F2E2E", "ink700": "#3E3D3D",
    "m_land": "#F1F0EC", "m_block": "#E8E7E2", "m_park": "#DCEAD6", "m_water": "#CFE0EC", "m_road": "#FFFFFF",
    "m_casing": "#DAD8D2", "m_major": "#F6E3B8", "m_label": "#787776", "m_route": "#2F2E2E",
}
FONT = "'Be Vietnam Pro',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif"
MONO = "'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,monospace"
SH_MD = "0 4px 12px rgba(11,11,13,.08)"
SH_LG = "0 12px 32px rgba(11,11,13,.12)"
SH_SHEET = "0 -8px 32px rgba(11,11,13,.14)"


def e(s):
    return _html.escape(str(s), quote=True)


def S(**kw):
    """style dict -> css string; underscores become dashes."""
    return "; ".join(f"{k.replace('_', '-')}: {v}" for k, v in kw.items() if v is not None)


# ---- type styles ----
TY = {
    "dxl": "font-size: 64px; line-height: 1.06; font-weight: 800; letter-spacing: -0.035em",
    "dlg": "font-size: 52px; line-height: 1.06; font-weight: 800; letter-spacing: -0.035em",
    "dmd": "font-size: 42px; line-height: 1.08; font-weight: 800; letter-spacing: -0.035em",
    "hxl": "font-size: 32px; line-height: 1.18; font-weight: 700; letter-spacing: -0.02em",
    "hlg": "font-size: 26px; line-height: 1.18; font-weight: 700; letter-spacing: -0.02em",
    "hmd": "font-size: 22px; line-height: 1.18; font-weight: 700; letter-spacing: -0.02em",
    "hsm": "font-size: 18px; line-height: 1.22; font-weight: 700; letter-spacing: -0.02em",
    "blg": "font-size: 17px; line-height: 1.55; font-weight: 400",
    "bmd": "font-size: 15px; line-height: 1.5; font-weight: 400",
    "bsm": "font-size: 13px; line-height: 1.5; font-weight: 400",
    "lbl": "font-size: 13px; line-height: 1.3; font-weight: 600",
    "cap": "font-size: 12px; line-height: 1.35; font-weight: 400",
    "ovl": "font-size: 11px; line-height: 1.3; font-weight: 600; letter-spacing: 0.09em; text-transform: uppercase",
    "num": f"font-family: {MONO}; font-size: 15px; line-height: 1.3; font-weight: 500",
}


def txt(s, ty="bmd", color=None, tag="div", extra=""):
    col = f"; color: {color}" if color else ""
    return f'<{tag} style="margin: 0; {TY[ty]}{col}{"; " + extra if extra else ""}">{s}</{tag}>'


def h(s, ty="hlg", tag="h1", color=None, extra=""):
    return txt(s, ty, color or C["t1"], tag, extra)


def num(s, size=15, color=None, weight=500, extra=""):
    return f'<span style="font-family: {MONO}; font-size: {size}px; line-height: 1.3; font-weight: {weight}; color: {color or C["t1"]}{"; " + extra if extra else ""}">{s}</span>'


def row(*items, gap=8, align="center", justify=None, extra=""):
    j = f"; justify-content: {justify}" if justify else ""
    return f'<div style="display: flex; flex-direction: row; align-items: {align}; gap: {gap}px{j}{"; " + extra if extra else ""}">{"".join(items)}</div>'


def col(*items, gap=8, extra=""):
    return f'<div style="display: flex; flex-direction: column; gap: {gap}px{"; " + extra if extra else ""}">{"".join(items)}</div>'


def grow(inner="", extra=""):
    return f'<div style="flex-grow: 1; min-width: 0{"; " + extra if extra else ""}">{inner}</div>'


def spacer():
    return '<div style="flex-grow: 1"></div>'


# ---- icons (Lucide, 2px stroke) ----
IC = {
    "arrow-left": '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>',
    "arrow-right": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "chevron-right": '<path d="m9 18 6-6-6-6"/>',
    "chevron-down": '<path d="m6 9 6 6 6-6"/>',
    "chevron-left": '<path d="m15 18-6-6 6-6"/>',
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "map-pin": '<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
    "navigation": '<polygon points="3 11 22 2 13 21 11 13 3 11"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "message": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
    "bell": '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
    "user": '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "home": '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "list": '<path d="M8 6h13"/><path d="M8 12h13"/><path d="M8 18h13"/><path d="M3 6h.01"/><path d="M3 12h.01"/><path d="M3 18h.01"/>',
    "bike": '<circle cx="18.5" cy="17.5" r="3.5"/><circle cx="5.5" cy="17.5" r="3.5"/><circle cx="15" cy="5" r="1"/><path d="M12 17.5V14l-3-3 4-3 2 3h2"/>',
    "car": '<path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/>',
    "utensils": '<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/>',
    "bag": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
    "camera": '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/>',
    "image": '<rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>',
    "upload": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" x2="12" y1="3" y2="15"/>',
    "copy": '<rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>',
    "qr": '<rect width="5" height="5" x="3" y="3" rx="1"/><rect width="5" height="5" x="16" y="3" rx="1"/><rect width="5" height="5" x="3" y="16" rx="1"/><path d="M21 16h-3a2 2 0 0 0-2 2v3"/><path d="M21 21v.01"/><path d="M12 7v3a2 2 0 0 1-2 2H7"/><path d="M3 12h.01"/><path d="M12 3h.01"/><path d="M12 16v.01"/><path d="M16 12h1"/><path d="M21 12v.01"/><path d="M12 21v-1"/>',
    "alert-triangle": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    "alert-circle": '<circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="8" y2="12"/><line x1="12" x2="12.01" y1="16" y2="16"/>',
    "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
    "check-circle": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="m9 11 3 3L22 4"/>',
    "x-circle": '<circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/>',
    "lock": '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "unlock": '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>',
    "shield-alert": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="M12 8v4"/><path d="M12 16h.01"/>',
    "sliders": '<line x1="21" x2="14" y1="4" y2="4"/><line x1="10" x2="3" y1="4" y2="4"/><line x1="21" x2="12" y1="12" y2="12"/><line x1="8" x2="3" y1="12" y2="12"/><line x1="21" x2="16" y1="20" y2="20"/><line x1="12" x2="3" y1="20" y2="20"/><line x1="14" x2="14" y1="2" y2="6"/><line x1="8" x2="8" y1="10" y2="14"/><line x1="16" x2="16" y1="18" y2="22"/>',
    "settings": '<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>',
    "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "flag": '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" x2="4" y1="22" y2="15"/>',
    "send": '<path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/>',
    "plus": '<path d="M5 12h14"/><path d="M12 5v14"/>',
    "minus": '<path d="M5 12h14"/>',
    "wifi-off": '<path d="M12 20h.01"/><path d="M8.5 16.429a5 5 0 0 1 7 0"/><path d="M5 12.859a10 10 0 0 1 5.17-2.69"/><path d="M19 12.859a10 10 0 0 0-2.007-1.523"/><path d="M2 8.82a15 15 0 0 1 4.177-2.643"/><path d="M22 8.82a15 15 0 0 0-11.288-3.764"/><path d="m2 2 20 20"/>',
    "refresh": '<path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/>',
    "dashboard": '<rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/>',
    "map": '<path d="M14.106 5.553a2 2 0 0 0 1.788 0l3.659-1.83A1 1 0 0 1 21 4.619v12.764a1 1 0 0 1-.553.894l-4.553 2.277a2 2 0 0 1-1.788 0l-4.212-2.106a2 2 0 0 0-1.788 0l-3.659 1.83A1 1 0 0 1 3 19.381V6.618a1 1 0 0 1 .553-.894l4.553-2.277a2 2 0 0 1 1.788 0z"/><path d="M15 5.764v15"/><path d="M9 3.236v15"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "store": '<path d="m2 7 4.41-4.41A2 2 0 0 1 7.83 2h8.34a2 2 0 0 1 1.42.59L22 7"/><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><path d="M15 22v-4a2 2 0 0 0-2-2h-2a2 2 0 0 0-2 2v4"/><path d="M2 7h20"/>',
    "banknote": '<rect width="20" height="12" x="2" y="6" rx="2"/><circle cx="12" cy="12" r="2"/><path d="M6 12h.01M18 12h.01"/>',
    "scale": '<path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>',
    "history": '<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l4 2"/>',
    "log-out": '<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/>',
    "filter": '<polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/>',
    "more": '<circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/>',
    "download": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/>',
    "trash": '<path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/>',
    "pencil": '<path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/><path d="m15 5 4 4"/>',
    "undo": '<path d="M3 7v6h6"/><path d="M21 17a9 9 0 0 0-9-9 9 9 0 0 0-6 2.3L3 13"/>',
    "redo": '<path d="M21 7v6h-6"/><path d="M3 17a9 9 0 0 1 9-9 9 9 0 0 1 6 2.3l3 2.7"/>',
    "pentagon": '<path d="M3.5 8.7c-.7.5-1 1.4-.7 2.2l2.8 8.7c.3.8 1 1.4 1.9 1.4h9.1c.9 0 1.6-.6 1.9-1.4l2.8-8.7c.3-.8 0-1.7-.7-2.2l-7.4-5.3a2.1 2.1 0 0 0-2.4 0Z"/>',
    "pointer": '<path d="M12.586 12.586 19 19"/><path d="M3.688 3.037a.497.497 0 0 0-.651.651l6.5 15.999a.501.501 0 0 0 .947-.062l1.569-6.083a2 2 0 0 1 1.448-1.479l6.124-1.579a.5.5 0 0 0 .063-.947z"/>',
    "eye": '<path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/>',
    "zoom-in": '<circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/><line x1="11" x2="11" y1="8" y2="14"/><line x1="8" x2="14" y1="11" y2="11"/>',
    "zoom-out": '<circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/><line x1="8" x2="14" y1="11" y2="11"/>',
    "locate": '<line x1="2" x2="5" y1="12" y2="12"/><line x1="19" x2="22" y1="12" y2="12"/><line x1="12" x2="12" y1="2" y2="5"/><line x1="12" x2="12" y1="19" y2="22"/><circle cx="12" cy="12" r="7"/>',
    "briefcase": '<path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/><rect width="20" height="14" x="2" y="6" rx="2"/>',
    "id-card": '<path d="M16 10h2"/><path d="M16 14h2"/><path d="M6.17 15a3 3 0 0 1 5.66 0"/><circle cx="9" cy="11" r="2"/><rect x="2" y="5" width="20" height="14" rx="2"/>',
    "help": '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>',
    "power": '<path d="M12 2v10"/><path d="M18.4 6.6a9 9 0 1 1-12.77.04"/>',
    "activity": '<path d="M22 12h-2.48a2 2 0 0 0-1.93 1.46l-2.35 8.36a.25.25 0 0 1-.48 0L9.24 2.18a.25.25 0 0 0-.48 0l-2.35 8.36A2 2 0 0 1 4.49 12H2"/>',
    "smartphone": '<rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "calendar": '<rect width="18" height="18" x="3" y="4" rx="2"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/>',
    "tag": '<path d="M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42z"/><circle cx="7.5" cy="7.5" r=".5"/>',
    "package": '<path d="M11 21.73a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73z"/><path d="M12 22V12"/><path d="m3.3 7 7.703 4.734a2 2 0 0 0 1.994 0L20.7 7"/>',
    "trending-up": '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>',
    "diff": '<circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><path d="M13 6h3a2 2 0 0 1 2 2v7"/><path d="M11 18H8a2 2 0 0 1-2-2V9"/>',
    "server": '<rect width="20" height="8" x="2" y="2" rx="2" ry="2"/><rect width="20" height="8" x="2" y="14" rx="2" ry="2"/><line x1="6" x2="6.01" y1="6" y2="6"/><line x1="6" x2="6.01" y1="18" y2="18"/>',
    "pause": '<rect x="14" y="4" width="4" height="16" rx="1"/><rect x="6" y="4" width="4" height="16" rx="1"/>',
    "play": '<polygon points="6 3 20 12 6 21 6 3"/>',
    "layers": '<path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>',
    "key": '<path d="m15.5 7.5 2.3 2.3a1 1 0 0 0 1.4 0l2.1-2.1a1 1 0 0 0 0-1.4L19 4"/><path d="m21 2-9.6 9.6"/><circle cx="7.5" cy="15.5" r="5.5"/>',
    "menu": '<line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/>',
    "database": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/>',
    "timer": '<line x1="10" x2="14" y1="2" y2="2"/><line x1="12" x2="15" y1="14" y2="11"/><circle cx="12" cy="14" r="8"/>',
    "list-checks": '<path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/><path d="M13 6h8"/><path d="M13 12h8"/><path d="M13 18h8"/>',
    "bank": '<line x1="3" x2="21" y1="22" y2="22"/><line x1="6" x2="6" y1="18" y2="11"/><line x1="10" x2="10" y1="18" y2="11"/><line x1="14" x2="14" y1="18" y2="11"/><line x1="18" x2="18" y1="18" y2="11"/><polygon points="12 2 20 7 4 7"/>',
    "user-check": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><polyline points="16 11 18 13 22 9"/>',
    "bar-chart": '<line x1="12" x2="12" y1="20" y2="10"/><line x1="18" x2="18" y1="20" y2="4"/><line x1="6" x2="6" y1="20" y2="16"/>',
    "panel-left": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 3v18"/>',
    "paperclip": '<path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l8.57-8.57A4 4 0 1 1 18 8.84l-8.59 8.57a2 2 0 0 1-2.83-2.83l8.49-8.48"/>',
    "inbox": '<polyline points="22 12 16 12 14 15 10 15 8 12 2 12"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/>',
    "circle-dot": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="1"/>',
    "route": '<circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/>',
    "wifi": '<path d="M12 20h.01"/><path d="M2 8.82a15 15 0 0 1 20 0"/><path d="M5 12.859a10 10 0 0 1 14 0"/><path d="M8.5 16.429a5 5 0 0 1 7 0"/>',
    "bookmark": '<path d="m19 21-7-4-7 4V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16z"/>',
    "briefcase-medical": '<path d="M12 11v4"/><path d="M14 13h-4"/><path d="M16 6V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/><rect width="20" height="14" x="2" y="6" rx="2"/>',
    "command": '<path d="M15 6v12a3 3 0 1 0 3-3H6a3 3 0 1 0 3 3V6a3 3 0 1 0-3 3h12a3 3 0 1 0-3-3"/>',
    "megaphone": '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
    "file-lock": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><rect width="8" height="6" x="8" y="12" rx="1"/><path d="M10 12v-2a2 2 0 1 1 4 0v2"/>',
    "gauge": '<path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>',
    "sparkle": '<path d="M12 3v18"/><path d="M3 12h18"/>',
}


def icon(name, size=20, color="currentColor", sw=2, extra=""):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0{"; " + extra if extra else ""}">{IC[name]}</svg>')


# ---- buttons ----
BTN = {
    "primary": (C["red"], C["tinv"], C["red"]),
    "secondary": (C["inverse"], C["tinv"], C["inverse"]),
    "outline": (C["card"], C["t1"], C["b2"]),
    "ghost": ("transparent", C["t1"], "transparent"),
    "danger": (C["card"], C["err"], C["err"]),
    "disabled": (C["sunken"], C["tdis"], C["sunken"]),
    "inverse": (C["card"], C["t1"], C["card"]),
}
BH = {"sm": 32, "md": 40, "lg": 48, "xl": 56}


def btn(label, kind="primary", size="lg", ic=None, href=None, full=False, extra="", aria=None, icon_right=None):
    bg, fg, bd = BTN[kind]
    hgt = BH[size]
    fs = 15 if size in ("lg", "xl") else 13
    pad = 20 if size in ("lg", "xl") else 14
    st = (f"display: inline-flex; align-items: center; justify-content: center; gap: 8px; box-sizing: border-box; "
          f"height: {hgt}px; min-height: {hgt}px; padding: 0 {pad}px; border-radius: 8px; background: {bg}; color: {fg}; "
          f"border: 1px solid {bd}; font-family: {FONT}; font-size: {fs}px; font-weight: 600; line-height: 1.2; "
          f"text-decoration: none; white-space: nowrap; cursor: pointer{'; width: 100%' if full else ''}{'; flex-grow: 1' if full == 'grow' else ''}{'; ' + extra if extra else ''}")
    inner = (icon(ic, 18 if size in ("lg", "xl") else 16) if ic else "") + (f"<span>{label}</span>" if label else "") + (icon(icon_right, 18) if icon_right else "")
    al = f' aria-label="{e(aria)}"' if aria else ""
    if href:
        return f'<a href="{href}" style="{st}"{al}>{inner}</a>'
    dis = ' disabled=""' if kind == "disabled" else ""
    return f'<button type="button" style="{st}"{al}{dis}>{inner}</button>'


def ibtn(ic, label, kind="outline", size=40, float_=False, badge=None):
    bg, fg, bd = BTN[kind]
    sh = f"; box-shadow: {SH_MD}" if float_ else ""
    b = ""
    if badge:
        b = f'<span style="position: absolute; top: 6px; right: 6px; width: 8px; height: 8px; border-radius: 999px; background: {C["red"]}; border: 2px solid {C["card"]}"></span>'
    return (f'<button type="button" aria-label="{e(label)}" style="position: relative; display: inline-flex; align-items: center; justify-content: center; '
            f'width: {size}px; height: {size}px; min-width: {size}px; border-radius: {8 if size < 48 else 12}px; background: {bg}; color: {fg}; border: 1px solid {bd}; padding: 0; cursor: pointer{sh}">'
            f'{icon(ic, 20)}{b}</button>')


def circle_btn(ic, label, size=44, float_=True):
    sh = f"; box-shadow: {SH_MD}" if float_ else ""
    return (f'<button type="button" aria-label="{e(label)}" style="display: inline-flex; align-items: center; justify-content: center; width: {size}px; height: {size}px; '
            f'border-radius: 999px; background: {C["card"]}; color: {C["t1"]}; border: 1px solid {C["b2"]}; padding: 0; cursor: pointer{sh}">{icon(ic, 20)}</button>')


# ---- status pill ----
TONES = {
    "info": (C["info_bg"], C["info"], "dot"), "warning": (C["warn_bg"], C["warn"], "!"),
    "accent": (C["acc_bg"], C["acc"], "dot"), "success": (C["ok_bg"], C["ok"], "check"),
    "danger": (C["err_bg"], C["err"], "x"), "neutral": (C["sunken"], C["t2"], None),
}
STATUS = {
    "requested": ("info", "Đã gửi yêu cầu"), "searching": ("info", "Đang tìm tài xế"), "matching": ("info", "Đang ghép tài xế"),
    "accepted": ("info", "Tài xế đã nhận"), "confirmed": ("info", "Đã xác nhận"),
    "arriving": ("warning", "Tài xế đang đến"), "arrived": ("warning", "Tài xế đã đến"), "preparing": ("warning", "Đang chuẩn bị"),
    "atOutlet": ("warning", "Tài xế tại quán"), "pickup": ("warning", "Đang lấy món"), "proofPending": ("warning", "Chờ xác nhận tiền"),
    "changeRequested": ("warning", "Đề xuất thay đổi"), "pendingReview": ("warning", "Chờ duyệt"), "unpaid": ("warning", "Chưa thanh toán"),
    "paused": ("warning", "Tạm dừng"),
    "inProgress": ("accent", "Đang trong chuyến"), "delivering": ("accent", "Đang giao"), "appeal": ("accent", "Đang kháng nghị"),
    "completed": ("success", "Hoàn thành"), "proofVerified": ("success", "Đã nhận đủ tiền"), "online": ("success", "Đang trực tuyến"),
    "approved": ("success", "Đã duyệt"), "active": ("success", "Đang hoạt động"), "published": ("success", "Đã xuất bản"),
    "proofRejected": ("danger", "Chứng từ bị từ chối"), "disputed": ("danger", "Đang tranh chấp"), "issue": ("danger", "Có sự cố"),
    "rejected": ("danger", "Bị từ chối"), "locked": ("danger", "Đã khóa"),
    "cancelled": ("neutral", "Đã hủy"), "offline": ("neutral", "Ngoại tuyến"), "expired": ("neutral", "Hết hạn"),
    "draft": ("neutral", "Bản nháp"), "finalized": ("neutral", "Đã kết luận"),
}


def pill(status, label=None, size="md"):
    tone, lab = STATUS[status] if status in STATUS else (status, label)
    bg, fg, mark = TONES[tone]
    hgt = 22 if size == "sm" else 26
    fs = 12 if size == "sm" else 13
    m = ""
    if mark == "dot":
        m = f'<span style="width: 6px; height: 6px; border-radius: 999px; background: {fg}; flex-shrink: 0"></span>'
    elif mark == "check":
        m = icon("check", 12, fg, 3)
    elif mark == "x":
        m = icon("x", 12, fg, 3)
    elif mark == "!":
        m = f'<span style="font-weight: 800; font-size: {fs}px; line-height: 1">!</span>'
    return (f'<span style="display: inline-flex; align-items: center; gap: 6px; box-sizing: border-box; min-height: {hgt}px; padding: 2px 10px; '
            f'border-radius: 999px; background: {bg}; color: {fg}; font-size: {fs}px; font-weight: 600; line-height: 1.2; white-space: nowrap; flex-shrink: 0">{m}<span>{label or lab}</span></span>')


def tag(label, selected=False, ic=None):
    bg = C["inverse"] if selected else C["card"]
    fg = C["tinv"] if selected else C["t1"]
    bd = C["inverse"] if selected else C["b2"]
    return (f'<button type="button" style="display: inline-flex; align-items: center; gap: 6px; height: 36px; padding: 0 14px; border-radius: 999px; '
            f'background: {bg}; color: {fg}; border: 1px solid {bd}; font-family: {FONT}; font-size: 13px; font-weight: 600; white-space: nowrap; flex-shrink: 0">{icon(ic, 16) if ic else ""}{label}</button>')


def badge(n, tone="brand"):
    bg = C["red"] if tone == "brand" else C["inverse"]
    return f'<span style="display: inline-flex; align-items: center; justify-content: center; min-width: 20px; height: 20px; padding: 0 6px; box-sizing: border-box; border-radius: 999px; background: {bg}; color: #FFFFFF; font-size: 11px; font-weight: 700">{n}</span>'


# ---- banner ----
def banner(tone, title, body="", ic=None, action=""):
    bg, fg = {"info": (C["info_bg"], C["info"]), "warning": (C["warn_bg"], C["warn"]), "success": (C["ok_bg"], C["ok"]),
              "danger": (C["err_bg"], C["err"]), "neutral": (C["sunken"], C["t2"]), "accent": (C["acc_bg"], C["acc"])}[tone]
    ic = ic or {"info": "info", "warning": "alert-triangle", "success": "check-circle", "danger": "alert-circle", "neutral": "info", "accent": "info"}[tone]
    b = f'<div style="{TY["bsm"]}; color: {C["t1"]}">{body}</div>' if body else ""
    a = f'<div style="margin-top: 8px">{action}</div>' if action else ""
    return (f'<div role="status" style="display: flex; gap: 12px; align-items: flex-start; padding: 12px 14px; border-radius: 12px; background: {bg}; border: 1px solid {bg}">'
            f'{icon(ic, 20, fg, extra="margin-top: 1px")}<div style="flex-grow: 1; min-width: 0"><div style="{TY["lbl"]}; font-size: 14px; color: {fg}">{title}</div>{b}{a}</div></div>')


# ---- card / list ----
def card(inner, pad=16, gap=12, extra="", bg=None):
    return f'<div style="box-sizing: border-box; background: {bg or C["card"]}; border: 1px solid {C["b2"]}; border-radius: 12px; padding: {pad}px; display: flex; flex-direction: column; gap: {gap}px{"; " + extra if extra else ""}">{inner}</div>'


def divider(m=0):
    return f'<div style="height: 1px; background: {C["b1"]}; margin: {m}px 0; flex-shrink: 0"></div>'


def icon_tile(ic, size=40, bg=None, fg=None, r=10):
    return f'<div style="width: {size}px; height: {size}px; border-radius: {r}px; background: {bg or C["sunken"]}; color: {fg or C["t1"]}; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{icon(ic, int(size * 0.5))}</div>'


def list_row(title, sub="", ic=None, right="", chevron=True, href=None, lead=None, pad="14px 16px", border=True, title_color=None):
    l = lead if lead is not None else (icon_tile(ic) if ic else "")
    s = f'<div style="{TY["cap"]}; font-size: 13px; color: {C["t3"]}; margin-top: 2px">{sub}</div>' if sub else ""
    ch = icon("chevron-right", 18, C["t3"]) if chevron else ""
    bd = f"border-bottom: 1px solid {C['b1']}; " if border else ""
    st = f'display: flex; align-items: center; gap: 12px; {bd}padding: {pad}; min-height: 56px; box-sizing: border-box; text-decoration: none; color: {C["t1"]}'
    inner = f'{l}<div style="flex-grow: 1; min-width: 0"><div style="{TY["bmd"]}; font-weight: 500; color: {title_color or C["t1"]}">{title}</div>{s}</div>{right}{ch}'
    if href:
        return f'<a href="{href}" style="{st}">{inner}</a>'
    return f'<div style="{st}">{inner}</div>'


def section_title(t, right=""):
    return row(txt(t, "hsm", C["t1"], "h2"), spacer(), right, extra="padding: 4px 0")


def price_row(label, value, bold=False, sub="", color=None, strike=None):
    fw = 700 if bold else 500
    sz = 17 if bold else 15
    s = f'<div style="{TY["cap"]}; color: {C["t3"]}">{sub}</div>' if sub else ""
    st = f'<span style="font-family: {MONO}; font-size: 13px; color: {C["t3"]}; text-decoration: line-through; margin-right: 8px">{strike}</span>' if strike else ""
    return (f'<div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 12px">'
            f'<div><div style="{TY["bmd"]}; color: {C["t1"] if bold else C["t2"]}; font-weight: {600 if bold else 400}">{label}</div>{s}</div>'
            f'<div style="white-space: nowrap">{st}<span style="font-family: {MONO}; font-size: {sz}px; font-weight: {fw}; color: {color or C["t1"]}">{value}</span></div></div>')


def avatar(initials, size=44, bg=None, fg=None):
    return (f'<div aria-hidden="true" style="width: {size}px; height: {size}px; border-radius: 999px; background: {bg or C["sunken"]}; color: {fg or C["t1"]}; '
            f'display: flex; align-items: center; justify-content: center; font-size: {int(size * 0.36)}px; font-weight: 700; flex-shrink: 0">{initials}</div>')


def stars(n=5, filled=5, size=16):
    out = ""
    for i in range(n):
        f = "#8E621A" if i < filled else "none"
        s = "#8E621A" if i < filled else C["b3"]
        out += f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{f}" stroke="{s}" stroke-width="2" stroke-linejoin="round" aria-hidden="true">{IC["star"]}</svg>'
    return f'<span role="img" aria-label="{filled} trên {n} sao" style="display: inline-flex; gap: 2px">{out}</span>'


def stepper(q=1):
    b = lambda ic, lab: f'<button type="button" aria-label="{lab}" style="width: 36px; height: 36px; border-radius: 8px; border: 1px solid {C["b2"]}; background: {C["card"]}; color: {C["t1"]}; display: flex; align-items: center; justify-content: center; padding: 0">{icon(ic, 18)}</button>'
    return row(b("minus", "Giảm"), f'<span style="min-width: 28px; text-align: center; font-family: {MONO}; font-size: 16px; font-weight: 600">{q}</span>', b("plus", "Tăng"), gap=8)


def progress(pct, color=None, h_=6):
    return f'<div role="progressbar" aria-valuenow="{pct}" aria-valuemin="0" aria-valuemax="100" style="height: {h_}px; border-radius: 999px; background: {C["sunken"]}; overflow: hidden"><div style="width: {pct}%; height: 100%; background: {color or C["inverse"]}; border-radius: 999px"></div></div>'


def switch(on=True, label="", sub=""):
    bg = C["inverse"] if on else C["b3"]
    knob = "left: 22px" if on else "left: 2px"
    s = f'<div style="{TY["cap"]}; font-size: 13px; color: {C["t3"]}">{sub}</div>' if sub else ""
    return (f'<label style="display: flex; align-items: center; gap: 12px; min-height: 44px"><div style="flex-grow: 1"><div style="{TY["bmd"]}; font-weight: 500">{label}</div>{s}</div>'
            f'<span role="switch" aria-checked="{"true" if on else "false"}" style="position: relative; width: 44px; height: 24px; border-radius: 999px; background: {bg}; flex-shrink: 0">'
            f'<span style="position: absolute; top: 2px; {knob}; width: 20px; height: 20px; border-radius: 999px; background: #FFFFFF"></span></span></label>')


def checkbox(label, on=False, sub=""):
    box = (f'<span style="width: 20px; height: 20px; border-radius: 5px; border: 1.5px solid {C["inverse"] if on else C["b3"]}; background: {C["inverse"] if on else C["card"]}; '
           f'display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 1px">{icon("check", 14, "#FFFFFF", 3) if on else ""}</span>')
    s = f'<div style="{TY["cap"]}; font-size: 13px; color: {C["t3"]}">{sub}</div>' if sub else ""
    return f'<label style="display: flex; gap: 12px; align-items: flex-start; min-height: 32px">{box}<span style="{TY["bmd"]}">{label}{s}</span></label>'


def radio(label, on=False, sub="", right=""):
    dot = (f'<span style="width: 20px; height: 20px; border-radius: 999px; border: 1.5px solid {C["inverse"] if on else C["b3"]}; display: flex; align-items: center; justify-content: center; flex-shrink: 0">'
           f'{"<span style=" + chr(34) + "width: 10px; height: 10px; border-radius: 999px; background: " + C["inverse"] + chr(34) + "></span>" if on else ""}</span>')
    s = f'<div style="{TY["cap"]}; font-size: 13px; color: {C["t3"]}">{sub}</div>' if sub else ""
    return f'<label style="display: flex; gap: 12px; align-items: center; min-height: 44px">{dot}<span style="flex-grow: 1; {TY["bmd"]}">{label}{s}</span>{right}</label>'


def segmented(opts, active=0, full=True):
    items = ""
    for i, o in enumerate(opts):
        on = i == active
        items += (f'<button type="button" aria-pressed="{"true" if on else "false"}" style="flex-grow: 1; height: 34px; border-radius: 6px; border: none; '
                  f'background: {C["card"] if on else "transparent"}; color: {C["t1"] if on else C["t2"]}; font-family: {FONT}; font-size: 13px; font-weight: 600; '
                  f'box-shadow: {"0 1px 2px rgba(11,11,13,.08)" if on else "none"}; padding: 0 12px; white-space: nowrap">{o}</button>')
    return f'<div role="group" style="display: flex; gap: 2px; padding: 3px; border-radius: 8px; background: {C["sunken"]}{"; width: 100%; box-sizing: border-box" if full else ""}">{items}</div>'


def tabs(opts, active=0):
    items = ""
    for i, o in enumerate(opts):
        on = i == active
        items += (f'<button type="button" style="height: 44px; padding: 0 4px; border: none; background: transparent; border-bottom: 2px solid {C["inverse"] if on else "transparent"}; '
                  f'color: {C["t1"] if on else C["t3"]}; font-family: {FONT}; font-size: 14px; font-weight: 600; white-space: nowrap">{o}</button>')
    return f'<div role="tablist" style="display: flex; gap: 20px; border-bottom: 1px solid {C["b2"]}">{items}</div>'


# ---- form fields ----
_fid = [0]


def field(label, value="", placeholder="", error=None, helper=None, ic=None, right="", hgt=48, disabled=False, textarea=False, mono=False):
    _fid[0] += 1
    fid = f"f{_fid[0]}"
    bd = C["err"] if error else C["b2"]
    bw = "1.5px" if error else "1px"
    ff = MONO if mono else FONT
    lead = f'<span style="display: flex; color: {C["t3"]}">{icon(ic, 18)}</span>' if ic else ""
    if textarea:
        inp = f'<textarea id="{fid}" placeholder="{e(placeholder)}" style="flex-grow: 1; min-height: 88px; border: none; outline: none; resize: none; background: transparent; font-family: {ff}; font-size: 15px; line-height: 1.5; color: {C["t1"]}; padding: 12px 0">{e(value)}</textarea>'
    else:
        inp = f'<input id="{fid}" type="text" value="{e(value)}" placeholder="{e(placeholder)}"{" disabled=" + chr(34) + chr(34) if disabled else ""} style="flex-grow: 1; min-width: 0; border: none; outline: none; background: transparent; font-family: {ff}; font-size: 15px; color: {C["t1"]}; height: 100%; padding: 0">'
    box = (f'<div style="display: flex; align-items: {"flex-start" if textarea else "center"}; gap: 10px; box-sizing: border-box; {"" if textarea else f"height: {hgt}px; "}padding: 0 14px; '
           f'border-radius: 8px; border: {bw} solid {bd}; background: {C["sunken"] if disabled else C["card"]}">{lead}{inp}{right}</div>')
    msg = ""
    if error:
        msg = f'<div style="display: flex; gap: 6px; align-items: center; {TY["cap"]}; font-size: 13px; color: {C["err"]}">{icon("alert-circle", 14, C["err"])}<span>{error}</span></div>'
    elif helper:
        msg = f'<div style="{TY["cap"]}; font-size: 13px; color: {C["t3"]}">{helper}</div>'
    lab = f'<label for="{fid}" style="{TY["lbl"]}; color: {C["t1"]}">{label}</label>' if label else ""
    return f'<div style="display: flex; flex-direction: column; gap: 6px">{lab}{box}{msg}</div>'


def select(label, value, helper=None, error=None):
    return field(label, value, right=icon("chevron-down", 18, C["t3"]), helper=helper, error=error)


def search_bar(ph="Tìm kiếm", value="", hgt=44, bg=None):
    return (f'<div style="display: flex; align-items: center; gap: 10px; height: {hgt}px; padding: 0 14px; border-radius: 8px; background: {bg or C["sunken"]}; box-sizing: border-box">'
            f'{icon("search", 18, C["t3"])}<input type="search" aria-label="{e(ph)}" value="{e(value)}" placeholder="{e(ph)}" style="flex-grow: 1; min-width: 0; border: none; outline: none; background: transparent; font-family: {FONT}; font-size: 15px; color: {C["t1"]}"></div>')


def otp_boxes(digits, error=False, active=None):
    out = ""
    for i in range(6):
        d = digits[i] if i < len(digits) else ""
        bd = C["err"] if error else (C["inverse"] if i == active else C["b2"])
        bw = "1.5px" if (error or i == active) else "1px"
        out += (f'<div style="width: 48px; height: 56px; border-radius: 8px; border: {bw} solid {bd}; background: {C["card"]}; display: flex; align-items: center; justify-content: center; '
                f'font-family: {MONO}; font-size: 22px; font-weight: 600; color: {C["t1"]}">{d}</div>')
    return f'<div role="group" aria-label="Mã OTP 6 số" style="display: flex; gap: 8px; justify-content: space-between">{out}</div>'


# ---- feedback ----
def skel(w="100%", h_=14, r=6, extra=""):
    ww = w if isinstance(w, str) else f"{w}px"
    return f'<div aria-hidden="true" style="width: {ww}; height: {h_}px; border-radius: {r}px; background: {C["sunken"]}; flex-shrink: 0{"; " + extra if extra else ""}"></div>'


def empty_state(ic, title, body="", action=""):
    return (f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 12px; padding: 32px 24px">'
            f'<div style="width: 64px; height: 64px; border-radius: 999px; background: {C["sunken"]}; color: {C["t2"]}; display: flex; align-items: center; justify-content: center">{icon(ic, 28)}</div>'
            f'<div style="{TY["hsm"]}; color: {C["t1"]}">{title}</div><div style="{TY["bmd"]}; color: {C["t2"]}; max-width: 300px">{body}</div>{action}</div>')


def toast(msg, ic="check-circle", action=""):
    a = f'<span style="margin-left: auto; font-weight: 700; color: #FFFFFF; text-decoration: underline">{action}</span>' if action else ""
    return (f'<div role="status" style="display: flex; align-items: center; gap: 10px; padding: 12px 16px; border-radius: 12px; background: {C["inverse"]}; color: #FFFFFF; '
            f'box-shadow: {SH_LG}; {TY["bsm"]}; font-size: 14px">{icon(ic, 18, "#FFFFFF")}<span>{msg}</span>{a}</div>')


def spinner(size=20, color=None):
    c = color or C["t1"]
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="9" stroke="{C["b2"]}" stroke-width="3"/>'
            f'<path d="M21 12a9 9 0 0 0-9-9" stroke="{c}" stroke-width="3" stroke-linecap="round"/></svg>')


def timeline(items, dense=False):
    """items: (title, meta, state) state in done/current/todo/failed"""
    out = ""
    n = len(items)
    for i, it in enumerate(items):
        t, m, st = it[0], it[1], it[2]
        body = it[3] if len(it) > 3 else ""
        if st == "done":
            mk = f'<span style="width: 20px; height: 20px; border-radius: 999px; background: {C["inverse"]}; display: flex; align-items: center; justify-content: center">{icon("check", 12, "#FFFFFF", 3)}</span>'
        elif st == "current":
            mk = f'<span style="width: 20px; height: 20px; border-radius: 999px; border: 2px solid {C["inverse"]}; background: {C["card"]}; display: flex; align-items: center; justify-content: center; box-sizing: border-box"><span style="width: 8px; height: 8px; border-radius: 999px; background: {C["inverse"]}"></span></span>'
        elif st == "failed":
            mk = f'<span style="width: 20px; height: 20px; border-radius: 4px; background: {C["err"]}; display: flex; align-items: center; justify-content: center">{icon("x", 12, "#FFFFFF", 3)}</span>'
        else:
            mk = f'<span style="width: 20px; height: 20px; border-radius: 999px; border: 2px solid {C["b2"]}; background: {C["card"]}; box-sizing: border-box"></span>'
        line = f'<div style="width: 2px; flex-grow: 1; background: {C["inverse"] if st == "done" else C["b2"]}; margin: 2px 0"></div>' if i < n - 1 else ""
        tc = C["err"] if st == "failed" else (C["t1"] if st != "todo" else C["t3"])
        b = f'<div style="{TY["bsm"]}; color: {C["t2"]}; margin-top: 4px">{body}</div>' if body else ""
        out += (f'<div style="display: flex; gap: 12px"><div style="display: flex; flex-direction: column; align-items: center; width: 20px; flex-shrink: 0">{mk}{line}</div>'
                f'<div style="padding-bottom: {12 if dense else 18}px; flex-grow: 1; min-width: 0"><div style="{TY["bmd"]}; font-size: {14 if dense else 15}px; font-weight: 600; color: {tc}">{t}</div>'
                f'<div style="{TY["cap"]}; color: {C["t3"]}; margin-top: 2px">{m}</div>{b}</div></div>')
    return f'<div style="display: flex; flex-direction: column">{out}</div>'


def kv(k, v, mono=False, strong=False):
    vv = num(v, 14) if mono else f'<span style="{TY["bsm"]}; font-size: 14px; color: {C["t1"]}; font-weight: {600 if strong else 500}; text-align: right">{v}</span>'
    return f'<div style="display: flex; justify-content: space-between; gap: 16px; align-items: baseline"><span style="{TY["bsm"]}; font-size: 14px; color: {C["t2"]}">{k}</span>{vv}</div>'


def photo(w="100%", h_=160, label="Ảnh chứng từ", ic="image", r=10, tone=None):
    ww = w if isinstance(w, str) else f"{w}px"
    bg = tone or "#E8E7E2"
    return (f'<div role="img" aria-label="{e(label)}" style="width: {ww}; height: {h_}px; border-radius: {r}px; background: {bg}; display: flex; flex-direction: column; '
            f'align-items: center; justify-content: center; gap: 6px; color: {C["t3"]}; flex-shrink: 0; box-sizing: border-box; border: 1px solid {C["b2"]}">{icon(ic, 24)}'
            f'<span style="{TY["cap"]}">{label}</span></div>')


def food_img(w=72, h_=72, hue=0, r=10, label=""):
    pals = [("#F6E3B8", "#E2A33C"), ("#DCEAD6", "#2E9E6B"), ("#FADCE2", "#E9506D"), ("#DEE8FC", "#4C7DF0"), ("#E7E3FA", "#7B6BE6"), ("#F9EAD1", "#B87F22")]
    a, b = pals[hue % len(pals)]
    ww = w if isinstance(w, str) else f"{w}px"
    return (f'<div role="img" aria-label="{e(label or "Ảnh món")}" style="width: {ww}; height: {h_}px; border-radius: {r}px; background: {a}; flex-shrink: 0; display: flex; align-items: center; justify-content: center; color: {b}">'
            f'{icon("utensils", max(16, min(40, int(h_ * 0.34))), b)}</div>')


def qr_svg(size=168):
    # deterministic fake QR pattern
    n = 25
    cell = size / n
    import random
    rnd = random.Random(7)
    rects = []
    def finder(x0, y0):
        rects.append(f'<rect x="{x0*cell}" y="{y0*cell}" width="{7*cell}" height="{7*cell}" fill="#0F0E0E"/>')
        rects.append(f'<rect x="{(x0+1)*cell}" y="{(y0+1)*cell}" width="{5*cell}" height="{5*cell}" fill="#FFFFFF"/>')
        rects.append(f'<rect x="{(x0+2)*cell}" y="{(y0+2)*cell}" width="{3*cell}" height="{3*cell}" fill="#0F0E0E"/>')
    for y in range(n):
        for x in range(n):
            if (x < 8 and y < 8) or (x > n - 9 and y < 8) or (x < 8 and y > n - 9):
                continue
            if rnd.random() < 0.46:
                rects.append(f'<rect x="{x*cell:.2f}" y="{y*cell:.2f}" width="{cell:.2f}" height="{cell:.2f}" fill="#0F0E0E"/>')
    finder(0, 0); finder(n - 7, 0); finder(0, n - 7)
    return f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" role="img" aria-label="Mã VietQR của tài xế"><rect width="{size}" height="{size}" fill="#FFFFFF"/>{"".join(rects)}</svg>'


# ---- map ----
def map_svg(w, h_, route=None, pins=None, driver=None, regions=None, labels=True, dim=False, seed=0, zoom=1.0, extra_svg=""):
    """route: list of (fx,fy) fractions; pins: list of (kind, fx, fy); driver: (fx,fy,kind)"""
    vx = [0.1, 0.3, 0.52, 0.72, 0.9]
    hy = [0.08, 0.24, 0.42, 0.6, 0.78, 0.94]
    parts = [f'<rect width="{w}" height="{h_}" fill="{C["m_land"]}"/>']
    xs = [0] + [v * w for v in vx] + [w]
    ys = [0] + [v * h_ for v in hy] + [h_]
    k = seed
    for i in range(len(xs) - 1):
        for j in range(len(ys) - 1):
            x0, x1, y0, y1 = xs[i] + 8, xs[i + 1] - 8, ys[j] + 8, ys[j + 1] - 8
            if x1 - x0 < 10 or y1 - y0 < 10:
                continue
            k += 1
            fill = C["m_park"] if k % 9 == 4 else C["m_block"]
            # split block into two
            if (x1 - x0) > 60 and k % 3 == 0:
                mid = (x0 + x1) / 2
                parts.append(f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{mid - x0 - 3:.1f}" height="{y1 - y0:.1f}" rx="3" fill="{fill}"/>')
                parts.append(f'<rect x="{mid + 3:.1f}" y="{y0:.1f}" width="{x1 - mid - 3:.1f}" height="{y1 - y0:.1f}" rx="3" fill="{C["m_block"]}"/>')
            else:
                parts.append(f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{x1 - x0:.1f}" height="{y1 - y0:.1f}" rx="3" fill="{fill}"/>')
    # river
    parts.append(f'<path d="M {w*0.62:.0f} {h_+10} C {w*0.7:.0f} {h_*0.86:.0f}, {w*0.98:.0f} {h_*0.84:.0f}, {w+20} {h_*0.7:.0f}" stroke="{C["m_water"]}" stroke-width="{max(26, w*0.07):.0f}" fill="none"/>')
    for v in vx:
        x = v * w
        major = v in (0.52,)
        parts.append(f'<line x1="{x:.0f}" y1="0" x2="{x:.0f}" y2="{h_}" stroke="{C["m_casing"]}" stroke-width="{12 if major else 9}"/>')
        parts.append(f'<line x1="{x:.0f}" y1="0" x2="{x:.0f}" y2="{h_}" stroke="{C["m_major"] if major else C["m_road"]}" stroke-width="{10 if major else 7}"/>')
    for v in hy:
        y = v * h_
        major = v in (0.42,)
        parts.append(f'<line x1="0" y1="{y:.0f}" x2="{w}" y2="{y:.0f}" stroke="{C["m_casing"]}" stroke-width="{12 if major else 9}"/>')
        parts.append(f'<line x1="0" y1="{y:.0f}" x2="{w}" y2="{y:.0f}" stroke="{C["m_major"] if major else C["m_road"]}" stroke-width="{10 if major else 7}"/>')
    # diagonal avenue
    parts.append(f'<line x1="{-10}" y1="{h_*0.7:.0f}" x2="{w*0.75:.0f}" y2="{-10}" stroke="{C["m_casing"]}" stroke-width="12"/>')
    parts.append(f'<line x1="{-10}" y1="{h_*0.7:.0f}" x2="{w*0.75:.0f}" y2="{-10}" stroke="{C["m_major"]}" stroke-width="10"/>')
    if labels:
        names = ["Nguyễn Huệ", "Lê Lợi", "Hai Bà Trưng", "Điện Biên Phủ", "Võ Văn Tần"]
        parts.append(f'<text x="{0.52*w+10:.0f}" y="{0.16*h_:.0f}" font-family="Be Vietnam Pro, sans-serif" font-size="10" fill="{C["m_label"]}" transform="rotate(90 {0.52*w+10:.0f} {0.16*h_:.0f})">{names[0]}</text>')
        parts.append(f'<text x="{0.14*w:.0f}" y="{0.42*h_-9:.0f}" font-family="Be Vietnam Pro, sans-serif" font-size="10" fill="{C["m_label"]}">{names[3]}</text>')
        parts.append(f'<text x="{0.56*w:.0f}" y="{0.6*h_-8:.0f}" font-family="Be Vietnam Pro, sans-serif" font-size="10" fill="{C["m_label"]}">{names[1]}</text>')
        parts.append(f'<text x="{0.74*w:.0f}" y="{0.24*h_-8:.0f}" font-family="Be Vietnam Pro, sans-serif" font-size="10" fill="{C["m_label"]}">{names[4]}</text>')
    for reg in regions or []:
        pts, kind = reg[0], reg[1]
        d = " ".join(f"{px*w:.0f},{py*h_:.0f}" for px, py in pts)
        if kind == "active":
            parts.append(f'<polygon points="{d}" fill="rgba(47,46,46,.06)" stroke="#3E3D3D" stroke-width="2" stroke-dasharray="8 6"/>')
        elif kind == "selected":
            parts.append(f'<polygon points="{d}" fill="rgba(226,34,64,.10)" stroke="#E22240" stroke-width="2.5"/>')
            for px, py in pts:
                parts.append(f'<rect x="{px*w-6:.0f}" y="{py*h_-6:.0f}" width="12" height="12" rx="2" fill="#FFFFFF" stroke="#E22240" stroke-width="2"/>')
        elif kind == "paused":
            parts.append(f'<polygon points="{d}" fill="rgba(226,163,60,.14)" stroke="#B87F22" stroke-width="2" stroke-dasharray="8 6"/>')
        elif kind == "invalid":
            parts.append(f'<polygon points="{d}" fill="rgba(195,24,52,.16)" stroke="#C31834" stroke-width="2" stroke-dasharray="2 5" stroke-linecap="round"/>')
        elif kind == "drawing":
            dd = " ".join(f"{px*w:.0f},{py*h_:.0f}" for px, py in pts)
            parts.append(f'<polyline points="{dd}" fill="none" stroke="#E22240" stroke-width="2.5"/>')
            for px, py in pts:
                parts.append(f'<circle cx="{px*w:.0f}" cy="{py*h_:.0f}" r="6" fill="#FFFFFF" stroke="#E22240" stroke-width="2"/>')
        if len(reg) > 2 and reg[2]:
            cx = sum(p[0] for p in pts) / len(pts) * w
            cy = sum(p[1] for p in pts) / len(pts) * h_
            lab = reg[2]
            parts.append(f'<rect x="{cx - len(lab)*3.6 - 10:.0f}" y="{cy-13:.0f}" width="{len(lab)*7.2+20:.0f}" height="26" rx="13" fill="#FFFFFF" stroke="#E1E0DF"/>')
            parts.append(f'<text x="{cx:.0f}" y="{cy+4:.0f}" text-anchor="middle" font-family="Be Vietnam Pro, sans-serif" font-size="12" font-weight="600" fill="#0F0E0E">{lab}</text>')
    if route:
        d = " ".join(("M" if i == 0 else "L") + f" {px*w:.0f} {py*h_:.0f}" for i, (px, py) in enumerate(route))
        parts.append(f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>')
        parts.append(f'<path d="{d}" fill="none" stroke="{C["m_route"]}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>')
    for p in pins or []:
        kind, px, py = p[0], p[1] * w, p[2] * h_
        if kind == "pickup":
            parts.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="11" fill="#FFFFFF"/><circle cx="{px:.0f}" cy="{py:.0f}" r="8" fill="#2F2E2E"/><circle cx="{px:.0f}" cy="{py:.0f}" r="3" fill="#FFFFFF"/>')
        elif kind == "dropoff":
            parts.append(f'<g transform="translate({px-14:.0f} {py-34:.0f})"><path d="M14 0C6.3 0 0 6.1 0 13.7 0 23.6 14 34 14 34s14-10.4 14-20.3C28 6.1 21.7 0 14 0z" fill="#E22240" stroke="#FFFFFF" stroke-width="2"/><circle cx="14" cy="13.5" r="5" fill="#FFFFFF"/></g>')
        elif kind == "outlet":
            parts.append(f'<g transform="translate({px-16:.0f} {py-16:.0f})"><rect width="32" height="32" rx="8" fill="#0F0E0E" stroke="#FFFFFF" stroke-width="2"/><g transform="translate(7 7) scale(0.75)" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">{IC["utensils"]}</g></g>')
        elif kind == "me":
            parts.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="22" fill="rgba(76,125,240,.16)"/><circle cx="{px:.0f}" cy="{py:.0f}" r="8" fill="#4C7DF0" stroke="#FFFFFF" stroke-width="3"/>')
        elif kind == "center":
            parts.append(f'<g transform="translate({px-18:.0f} {py-44:.0f})"><path d="M18 0C8 0 0 7.8 0 17.6 0 30.3 18 44 18 44s18-13.7 18-26.4C36 7.8 28 0 18 0z" fill="#0F0E0E" stroke="#FFFFFF" stroke-width="2"/><circle cx="18" cy="17.5" r="6" fill="#FFFFFF"/></g><ellipse cx="{px:.0f}" cy="{py+2:.0f}" rx="6" ry="2.5" fill="rgba(15,14,14,.25)"/>')
        elif kind == "driver-idle":
            parts.append(f'<g transform="translate({px-13:.0f} {py-13:.0f})"><circle cx="13" cy="13" r="13" fill="#FFFFFF" stroke="#C9C8C6"/><g transform="translate(5 5) scale(0.67)" fill="none" stroke="#3E3D3D" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">{IC["bike"]}</g></g>')
    if driver:
        px, py = driver[0] * w, driver[1] * h_
        ic = IC["car"] if (len(driver) > 2 and driver[2] == "car") else IC["bike"]
        parts.append(f'<g transform="translate({px-18:.0f} {py-18:.0f})"><circle cx="18" cy="18" r="18" fill="#0F0E0E" stroke="#FFFFFF" stroke-width="3"/><g transform="translate(8 8) scale(0.84)" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{ic}</g></g>')
    parts.append(extra_svg)
    if dim:
        parts.append(f'<rect width="{w}" height="{h_}" fill="rgba(245,245,244,.55)"/>')
    return f'<svg width="{w}" height="{h_}" viewBox="0 0 {w} {h_}" aria-hidden="true" style="display: block">{"".join(parts)}</svg>'


# ---- mobile scaffolding ----
PW, PH = 390, 844
TOP = 44  # safe area (not drawn)
BOT = 34


def phone(inner, bg=None):
    return (f'<div style="position: relative; width: {PW}px; height: {PH}px; overflow: hidden; background: {bg or C["page"]}; border-radius: 36px; '
            f'border: 1px solid {C["b2"]}; box-sizing: border-box; display: flex; flex-direction: column; font-family: {FONT}; color: {C["t1"]}; flex-shrink: 0">{inner}</div>')


def topbar(title="", back=True, right="", sub="", bg=None, border=True, large=None, left=None):
    b = left if left is not None else (ibtn("arrow-left", "Quay lại", "ghost", 44) if back else '<div style="width: 44px"></div>')
    s = f'<div style="{TY["cap"]}; color: {C["t3"]}">{sub}</div>' if sub else ""
    bd = f"border-bottom: 1px solid {C['b1']}; " if border else ""
    t = f'<div style="flex-grow: 1; min-width: 0; text-align: center"><div style="{TY["hsm"]}; font-size: 17px">{title}</div>{s}</div>' if title else '<div style="flex-grow: 1"></div>'
    r = right or '<div style="width: 44px"></div>'
    bar = (f'<div style="display: flex; align-items: center; gap: 4px; padding: {TOP}px 6px 6px; {bd}background: {bg or C["card"]}; flex-shrink: 0">{b}{t}{r}</div>')
    return bar


def body(inner, pad=16, gap=16, bg=None, extra=""):
    return f'<div style="flex-grow: 1; min-height: 0; overflow: hidden; display: flex; flex-direction: column; gap: {gap}px; padding: {pad}px{"; background: " + bg if bg else ""}{"; " + extra if extra else ""}">{inner}</div>'


def bottom(inner, gap=12, border=True, bg=None):
    bd = f"border-top: 1px solid {C['b1']}; " if border else ""
    return f'<div style="flex-shrink: 0; display: flex; flex-direction: column; gap: {gap}px; padding: 12px 16px {BOT}px; {bd}background: {bg or C["card"]}">{inner}</div>'


TABS_C = [("home", "Trang chủ"), ("list", "Hoạt động"), ("bell", "Thông báo"), ("user", "Tài khoản")]
TABS_D = [("navigation", "Nhận việc"), ("history", "Lịch sử"), ("bell", "Thông báo"), ("user", "Tài khoản")]


def tabbar(active=0, app="c", badge_idx=None):
    items = ""
    for i, (ic, lab) in enumerate(TABS_C if app == "c" else TABS_D):
        on = i == active
        dot = f'<span style="position: absolute; top: 4px; left: 50%; margin-left: 6px; width: 8px; height: 8px; border-radius: 999px; background: {C["red"]}; border: 2px solid #FFFFFF"></span>' if badge_idx == i else ""
        items += (f'<a href="#" aria-current="{"page" if on else "false"}" style="position: relative; flex: 1 1 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px; '
                  f'height: 60px; text-decoration: none; color: {C["t1"] if on else C["t3"]}; font-size: 11px; font-weight: {700 if on else 500}">{icon(ic, 22, sw=2.2 if on else 2)}<span>{lab}</span>{dot}</a>')
    return f'<nav aria-label="Điều hướng chính" style="display: flex; border-top: 1px solid {C["b1"]}; background: {C["card"]}; padding-bottom: {BOT - 10}px; flex-shrink: 0">{items}</nav>'


def map_screen(map_html, sheet_html, top_html="", sheet_h=None, float_right=""):
    """full-bleed map + floating controls + bottom sheet (absolute)"""
    sh = f"height: {sheet_h}px; " if sheet_h else ""
    fr = f'<div style="position: absolute; right: 16px; bottom: {(sheet_h or 360) + 16}px; display: flex; flex-direction: column; gap: 10px">{float_right}</div>' if float_right else ""
    return (f'<div style="position: absolute; inset: 0">{map_html}</div>'
            f'<div style="position: absolute; left: 0; right: 0; top: 0; padding: {TOP}px 16px 0; display: flex; flex-direction: column; gap: 10px">{top_html}</div>{fr}'
            f'<div style="position: absolute; left: 0; right: 0; bottom: 0; {sh}box-sizing: border-box; background: {C["card"]}; border-radius: 20px 20px 0 0; box-shadow: {SH_SHEET}; '
            f'display: flex; flex-direction: column; overflow: hidden">'
            f'<div style="display: flex; justify-content: center; padding: 8px 0 4px; flex-shrink: 0"><span style="width: 36px; height: 4px; border-radius: 999px; background: {C["b2"]}"></span></div>{sheet_html}</div>')


def sheet_over(base_html, sheet_html, sheet_h=None, title="", close=True):
    """dimmed screen + modal bottom sheet"""
    sh = f"height: {sheet_h}px; " if sheet_h else "max-height: 780px; "
    head = ""
    if title:
        head = row(txt(title, "hmd", C["t1"], "h2"), spacer(), ibtn("x", "Đóng", "ghost", 44) if close else "", extra="padding: 4px 8px 0 16px")
    return (f'<div style="position: absolute; inset: 0; display: flex; flex-direction: column">{base_html}</div>'
            f'<div style="position: absolute; inset: 0; background: {C["overlay"]}"></div>'
            f'<div role="dialog" aria-modal="true" style="position: absolute; left: 0; right: 0; bottom: 0; {sh}box-sizing: border-box; background: {C["card"]}; border-radius: 20px 20px 0 0; '
            f'box-shadow: {SH_SHEET}; display: flex; flex-direction: column; overflow: hidden">'
            f'<div style="display: flex; justify-content: center; padding: 8px 0 0; flex-shrink: 0"><span style="width: 36px; height: 4px; border-radius: 999px; background: {C["b2"]}"></span></div>{head}{sheet_html}</div>')


def dialog_over(base_html, title, body_html, actions, ic=None, tone=None, width=342):
    ict = ""
    if ic:
        bg, fg = {"danger": (C["err_bg"], C["err"]), "warning": (C["warn_bg"], C["warn"]), "info": (C["info_bg"], C["info"]), "success": (C["ok_bg"], C["ok"]), None: (C["sunken"], C["t1"])}[tone]
        ict = f'<div style="width: 48px; height: 48px; border-radius: 999px; background: {bg}; color: {fg}; display: flex; align-items: center; justify-content: center">{icon(ic, 24)}</div>'
    return (f'<div style="position: absolute; inset: 0; display: flex; flex-direction: column">{base_html}</div>'
            f'<div style="position: absolute; inset: 0; background: {C["overlay"]}; display: flex; align-items: center; justify-content: center; padding: 24px">'
            f'<div role="alertdialog" aria-modal="true" style="width: {width}px; box-sizing: border-box; background: {C["card"]}; border-radius: 16px; box-shadow: {SH_LG}; padding: 24px; display: flex; flex-direction: column; gap: 16px">'
            f'{ict}<h2 style="margin: 0; {TY["hmd"]}">{title}</h2><div style="{TY["bmd"]}; color: {C["t2"]}; display: flex; flex-direction: column; gap: 12px">{body_html}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 10px; margin-top: 4px">{actions}</div></div></div>')


def float_card(inner, extra=""):
    return f'<div style="background: {C["card"]}; border: 1px solid {C["b2"]}; border-radius: 12px; box-shadow: {SH_MD}; padding: 12px 14px; display: flex; flex-direction: column; gap: 8px{"; " + extra if extra else ""}">{inner}</div>'


def addr_block(pick, drop, pick_sub="", drop_sub=""):
    ps = f'<div style="{TY["cap"]}; color: {C["t3"]}">{pick_sub}</div>' if pick_sub else ""
    ds = f'<div style="{TY["cap"]}; color: {C["t3"]}">{drop_sub}</div>' if drop_sub else ""
    return (f'<div style="display: flex; gap: 12px"><div style="display: flex; flex-direction: column; align-items: center; padding-top: 5px; width: 14px">'
            f'<span style="width: 12px; height: 12px; border-radius: 999px; border: 3px solid {C["ink800"]}; box-sizing: border-box"></span>'
            f'<span style="width: 2px; flex-grow: 1; min-height: 22px; background: {C["b2"]}; margin: 4px 0"></span>'
            f'<span style="width: 12px; height: 12px; border-radius: 3px; background: {C["red"]}"></span></div>'
            f'<div style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 14px"><div><div style="{TY["bmd"]}; font-weight: 500">{pick}</div>{ps}</div>'
            f'<div><div style="{TY["bmd"]}; font-weight: 500">{drop}</div>{ds}</div></div></div>')


def job_header(status, headline, sub="", right=""):
    s = f'<div style="{TY["bsm"]}; color: {C["t2"]}">{sub}</div>' if sub else ""
    return (f'<div aria-live="polite" style="display: flex; flex-direction: column; gap: 8px; padding: 4px 16px 12px">{row(pill(status), spacer(), right)}'
            f'<div style="{TY["hmd"]}">{headline}</div>{s}</div>')


def person_row(name, sub, initials, actions=True, rating=None, plate=None):
    r = f'<span style="display: inline-flex; align-items: center; gap: 3px; {TY["cap"]}; color: {C["t2"]}">{icon("star", 12, "#8E621A")}{rating}</span>' if rating else ""
    p = f'<div style="margin-top: 4px"><span style="display: inline-block; padding: 2px 8px; border-radius: 6px; border: 1px solid {C["b2"]}; font-family: {MONO}; font-size: 13px; font-weight: 600">{plate}</span></div>' if plate else ""
    acts = row(ibtn("message", "Nhắn tin", "outline", 44), ibtn("phone", "Gọi điện", "outline", 44), gap=8) if actions else ""
    return row(avatar(initials, 48), f'<div style="flex-grow: 1; min-width: 0"><div style="{TY["bmd"]}; font-weight: 600">{name} {r}</div><div style="{TY["cap"]}; font-size: 13px; color: {C["t3"]}">{sub}</div>{p}</div>', acts, gap=12)


def upload_tile(state="empty", label="Ảnh chụp màn hình chuyển khoản"):
    if state == "empty":
        return (f'<button type="button" style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px; height: 148px; width: 100%; border-radius: 12px; '
                f'border: 1.5px dashed {C["b3"]}; background: {C["ink25"]}; color: {C["t1"]}; font-family: {FONT}">{icon("upload", 24)}<span style="{TY["lbl"]}; font-size: 14px">Tải ảnh chứng từ lên</span>'
                f'<span style="{TY["cap"]}; color: {C["t3"]}">{label} · JPG/PNG tối đa 10 MB</span></button>')
    if state == "uploading":
        return card(row(photo(64, 64, "", "image", 8), col(txt("chuyen-khoan-0924.jpg", "bsm", C["t1"], extra="font-weight: 600"), progress(62), txt("Đang tải lên · 62%", "cap", C["t3"]), gap=6, extra="flex-grow: 1"), gap=12))
    if state == "failed":
        return card(row(photo(64, 64, "", "image", 8), col(txt("chuyen-khoan-0924.jpg", "bsm", C["t1"], extra="font-weight: 600"),
                                                          f'<div style="display: flex; gap: 6px; align-items: center; {TY["cap"]}; font-size: 13px; color: {C["err"]}">{icon("alert-circle", 14, C["err"])}Tải lên thất bại — ảnh vẫn được giữ trên máy</div>', gap=6, extra="flex-grow: 1"), gap=12)
                    + row(btn("Thử lại", "outline", "md", "refresh", full="grow"), btn("Chọn ảnh khác", "ghost", "md"), gap=8), extra=f"border-color: {C['err']}")
    if state == "done":
        return card(row(photo(64, 64, "", "image", 8), col(txt("chuyen-khoan-0924.jpg", "bsm", C["t1"], extra="font-weight: 600"),
                                                          f'<div style="display: flex; gap: 6px; align-items: center; {TY["cap"]}; font-size: 13px; color: {C["ok"]}">{icon("check-circle", 14, C["ok"])}Đã gửi cho tài xế lúc 08:14</div>', gap=6, extra="flex-grow: 1"), gap=12))
    return ""


def chip_row(items, extra=""):
    return f'<div style="display: flex; gap: 8px; overflow: hidden; flex-shrink: 0{"; " + extra if extra else ""}">{"".join(items)}</div>'


def logo_img(h_=28, white=False):
    w = round(h_ * 4493 / 1300)
    return f'<img src="{LOGO_WHITE if white else LOGO}" alt="Onway" width="{w}" height="{h_}" style="display: block; width: {w}px; height: {h_}px">'


def mark_img(s=40, white=False):
    return f'<img src="{MARK_WHITE if white else MARK}" alt="" width="{s}" height="{s}" style="display: block; width: {s}px; height: {s}px">'


# ---- admin scaffolding ----
AW, AH = 1440, 900
NAV = [
    ("VẬN HÀNH", [("dashboard", "Tổng quan", "dash"), ("inbox", "Hàng đợi vận hành", "queue"), ("activity", "Sức khoẻ hệ thống", "health")]),
    ("KHU VỰC & CHÍNH SÁCH", [("map", "Khu vực & polygon", "region"), ("sliders", "Giá & chính sách", "policy")]),
    ("TÀI XẾ & KHÁCH", [("users", "Tài xế", "driver"), ("lock", "Khoá tự động", "autolock"), ("banknote", "Duyệt phí nền tảng", "finance"), ("user", "Khách hàng", "customer")]),
    ("FOOD", [("store", "Danh mục món", "catalog")]),
    ("RỦI RO", [("scale", "Khiếu nại & gian lận", "case"), ("history", "Nhật ký audit", "audit"), ("shield", "Yêu cầu dữ liệu", "privacy")]),
    ("HỆ THỐNG", [("key", "Quản trị viên & quyền", "rbac"), ("bell", "Mẫu thông báo", "notif"), ("settings", "Cài đặt", "settings")]),
]
NAV_BADGE = {"queue": 12, "autolock": 3, "finance": 8, "case": 17}


def _admin_logo():
    tg = '<span style="' + TY["ovl"] + '; color: ' + C["t3"] + '; padding: 2px 6px; border: 1px solid ' + C["b2"] + '; border-radius: 4px">ADMIN</span>'
    return row(logo_img(24), tg, gap=10)


def sidebar(active, collapsed=False):
    if collapsed:
        items = ""
        for sec, its in NAV:
            for ic, lab, key in its:
                on = key == active
                items += (f'<a href="#" aria-label="{lab}" style="position: relative; display: flex; align-items: center; justify-content: center; width: 44px; height: 40px; border-radius: 8px; '
                          f'background: {C["active"] if on else "transparent"}; color: {C["t1"] if on else C["t2"]}">{icon(ic, 20)}'
                          f'{"<span style=" + chr(34) + "position: absolute; top: 6px; right: 8px; width: 7px; height: 7px; border-radius: 999px; background: " + C["red"] + chr(34) + "></span>" if key in NAV_BADGE else ""}</a>')
            items += f'<div style="height: 1px; width: 32px; background: {C["b1"]}; margin: 6px 0"></div>'
        return (f'<nav aria-label="Điều hướng quản trị" style="width: 72px; flex-shrink: 0; background: {C["card"]}; border-right: 1px solid {C["b2"]}; display: flex; flex-direction: column; align-items: center; gap: 2px; padding: 0 0 16px">'
                f'<div style="height: 64px; display: flex; align-items: center">{mark_img(32)}</div>{items}</nav>')
    out = ""
    for sec, its in NAV:
        out += f'<div style="{TY["ovl"]}; color: {C["t3"]}; padding: 14px 12px 6px">{sec}</div>'
        for ic, lab, key in its:
            on = key == active
            b = badge(NAV_BADGE[key], "brand" if key in ("case", "autolock") else "ink") if key in NAV_BADGE else ""
            out += (f'<a href="#" aria-current="{"page" if on else "false"}" style="display: flex; align-items: center; gap: 10px; height: 36px; padding: 0 12px; border-radius: 8px; text-decoration: none; '
                    f'background: {C["active"] if on else "transparent"}; color: {C["t1"] if on else C["t2"]}; font-size: 14px; font-weight: {600 if on else 500}">{icon(ic, 18)}<span style="flex-grow: 1">{lab}</span>{b}</a>')
    return (f'<nav aria-label="Điều hướng quản trị" style="width: 248px; flex-shrink: 0; background: {C["card"]}; border-right: 1px solid {C["b2"]}; display: flex; flex-direction: column; box-sizing: border-box">'
            f'<div style="height: 64px; display: flex; align-items: center; justify-content: space-between; padding: 0 16px 0 20px; border-bottom: 1px solid {C["b1"]}; flex-shrink: 0">'
            f'{_admin_logo()}'
            f'{ibtn("panel-left", "Thu gọn thanh bên", "ghost", 32)}</div><div style="padding: 4px 12px 16px; display: flex; flex-direction: column; gap: 1px; overflow: hidden; flex-grow: 1">{out}</div>'
            f'<div style="border-top: 1px solid {C["b1"]}; padding: 12px 16px; display: flex; align-items: center; gap: 10px">{avatar("NL", 32)}<div style="flex-grow: 1; min-width: 0"><div style="{TY["lbl"]}">Ngọc Lan</div><div style="{TY["cap"]}; color: {C["t3"]}">Ops Admin · HCM</div></div></div></nav>')


def admin_header(crumbs):
    cr = f' <span style="color: {C["t3"]}">/</span> '.join(f'<span style="color: {C["t1"] if i == len(crumbs) - 1 else C["t3"]}; font-weight: {600 if i == len(crumbs) - 1 else 500}">{c}</span>' for i, c in enumerate(crumbs))
    return (f'<header style="height: 64px; flex-shrink: 0; display: flex; align-items: center; gap: 16px; padding: 0 24px; border-bottom: 1px solid {C["b2"]}; background: {C["card"]}; box-sizing: border-box">'
            f'<div style="{TY["bsm"]}; font-size: 14px; flex-grow: 1">{cr}</div>'
            f'<button type="button" style="display: flex; align-items: center; gap: 10px; width: 320px; height: 36px; padding: 0 12px; border-radius: 8px; border: 1px solid {C["b2"]}; background: {C["ink25"]}; color: {C["t3"]}; font-family: {FONT}; font-size: 13px">'
            f'{icon("search", 16)}<span style="flex-grow: 1; text-align: left">Tìm tài xế, mã chuyến, mã case…</span><span style="font-family: {MONO}; font-size: 11px; border: 1px solid {C["b2"]}; border-radius: 4px; padding: 1px 5px">⌘K</span></button>'
            f'<span style="display: inline-flex; align-items: center; gap: 6px; height: 28px; padding: 0 10px; border-radius: 999px; border: 1px solid {C["b2"]}; {TY["cap"]}; font-weight: 600; color: {C["t2"]}">{icon("map-pin", 14)}TP. Hồ Chí Minh</span>'
            f'{ibtn("bell", "Thông báo", "ghost", 36, badge=True)}{avatar("NL", 32)}</header>')


def admin(active, crumbs, content, overlay="", collapsed=False, pad=24):
    return (f'<div style="position: relative; width: {AW}px; height: {AH}px; overflow: hidden; display: flex; background: {C["page"]}; font-family: {FONT}; color: {C["t1"]}; border: 1px solid {C["b2"]}; box-sizing: border-box">'
            f'{sidebar(active, collapsed)}<div style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column">{admin_header(crumbs)}'
            f'<main style="flex-grow: 1; min-height: 0; overflow: hidden; padding: {pad}px; display: flex; flex-direction: column; gap: 20px">{content}</main></div>{overlay}</div>')


def page_head(title, sub="", actions="", pills=""):
    s = f'<div style="{TY["bsm"]}; font-size: 14px; color: {C["t2"]}; margin-top: 4px">{sub}</div>' if sub else ""
    return row(f'<div style="flex-grow: 1; min-width: 0"><div style="display: flex; align-items: center; gap: 10px"><h1 style="margin: 0; {TY["hlg"]}; font-size: 24px">{title}</h1>{pills}</div>{s}</div>', actions, gap=8, align="flex-end")


def table(cols, rows, widths=None, selected=None, checkbox_col=False, dense=False):
    widths = widths or ["1fr"] * len(cols)
    if checkbox_col:
        widths = ["40px"] + widths
    gt = " ".join(widths)
    rh = 44 if not dense else 40
    head_cells = ("<div></div>" if checkbox_col else "") + "".join(
        f'<div style="{TY["cap"]}; font-weight: 600; color: {C["t2"]}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{c}</div>' for c in cols)
    out = f'<div role="row" style="display: grid; grid-template-columns: {gt}; gap: 12px; align-items: center; height: 40px; padding: 0 16px; background: {C["ink25"]}; border-bottom: 1px solid {C["b2"]}">{head_cells}</div>'
    for i, r in enumerate(rows):
        sel = selected is not None and i == selected
        cb = ""
        if checkbox_col:
            cb = f'<div><span style="display: block; width: 16px; height: 16px; border-radius: 4px; border: 1.5px solid {C["b3"]}; background: #FFFFFF"></span></div>'
        cells = "".join(f'<div style="{TY["bsm"]}; color: {C["t1"]}; min-width: 0; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; display: flex; align-items: center; gap: 6px">{c}</div>' for c in r)
        out += (f'<div role="row" style="display: grid; grid-template-columns: {gt}; gap: 12px; align-items: center; min-height: {rh}px; padding: 0 16px; border-bottom: 1px solid {C["b1"]}; '
                f'background: {C["active"] if sel else C["card"]}{"; box-shadow: inset 3px 0 0 " + C["inverse"] if sel else ""}">{cb}{cells}</div>')
    return f'<div role="table" style="background: {C["card"]}; border: 1px solid {C["b2"]}; border-radius: 12px; overflow: hidden; flex-shrink: 0">{out}</div>'


def muted(s):
    return f'<span style="color: {C["t3"]}">{s}</span>'


def mono(s, size=13, color=None):
    return f'<span style="font-family: {MONO}; font-size: {size}px; color: {color or C["t1"]}">{s}</span>'


def filter_bar(chips, search="Tìm kiếm", right=""):
    return row(f'<div style="width: 300px">{search_bar(search, hgt=36, bg=C["card"]).replace("background: " + C["card"], "background: " + C["card"] + "; border: 1px solid " + C["b2"])}</div>',
               *[f'<button type="button" style="display: inline-flex; align-items: center; gap: 6px; height: 36px; padding: 0 12px; border-radius: 8px; border: 1px solid {C["inverse"] if on else C["b2"]}; background: {C["inverse"] if on else C["card"]}; color: {C["tinv"] if on else C["t1"]}; font-family: {FONT}; font-size: 13px; font-weight: 600; white-space: nowrap">{lab}{icon("chevron-down", 14) if not on else ""}</button>' for lab, on in chips],
               spacer(), right, gap=8)


def stat(label, value, delta="", sub="", ic=None, tone=None):
    d = ""
    if delta:
        col_ = C["ok"] if delta.startswith("+") else (C["err"] if delta.startswith("−") or delta.startswith("-") else C["t2"])
        d = f'<span style="{TY["cap"]}; font-weight: 600; color: {col_}">{delta}</span>'
    s = f'<div style="{TY["cap"]}; color: {C["t3"]}">{sub}</div>' if sub else ""
    i = icon(ic, 18, C["t3"]) if ic else ""
    return card(row(f'<span style="{TY["lbl"]}; color: {C["t2"]}">{label}</span>', spacer(), i) + row(num(value, 26, weight=600), d, gap=8, align="baseline") + s, pad=16, gap=6)


def drawer(title, inner, footer="", width=520, sub="", pills=""):
    s = f'<div style="{TY["bsm"]}; color: {C["t2"]}">{sub}</div>' if sub else ""
    f = f'<div style="flex-shrink: 0; display: flex; gap: 8px; justify-content: flex-end; padding: 16px 24px; border-top: 1px solid {C["b2"]}; background: {C["card"]}">{footer}</div>' if footer else ""
    return (f'<div style="position: absolute; inset: 0; background: rgba(15,14,14,.32)"></div>'
            f'<aside role="dialog" aria-modal="true" aria-label="{e(title)}" style="position: absolute; top: 0; right: 0; bottom: 0; width: {width}px; background: {C["card"]}; box-shadow: {SH_LG}; display: flex; flex-direction: column; font-family: {FONT}">'
            f'<div style="flex-shrink: 0; display: flex; align-items: flex-start; gap: 12px; padding: 20px 24px; border-bottom: 1px solid {C["b2"]}"><div style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 6px">'
            f'<div style="display: flex; align-items: center; gap: 10px"><h2 style="margin: 0; {TY["hmd"]}; font-size: 20px">{title}</h2>{pills}</div>{s}</div>{ibtn("x", "Đóng", "ghost", 36)}</div>'
            f'<div style="flex-grow: 1; min-height: 0; overflow: hidden; padding: 20px 24px; display: flex; flex-direction: column; gap: 20px">{inner}</div>{f}</aside>')


def admin_dialog(title, inner, actions, width=520, ic=None, tone=None):
    ict = ""
    if ic:
        bg, fg = {"danger": (C["err_bg"], C["err"]), "warning": (C["warn_bg"], C["warn"]), "info": (C["info_bg"], C["info"]), "success": (C["ok_bg"], C["ok"]), None: (C["sunken"], C["t1"])}[tone]
        ict = f'<div style="width: 40px; height: 40px; border-radius: 999px; background: {bg}; color: {fg}; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{icon(ic, 20)}</div>'
    return (f'<div style="position: absolute; inset: 0; background: {C["overlay"]}; display: flex; align-items: center; justify-content: center">'
            f'<div role="dialog" aria-modal="true" style="width: {width}px; background: {C["card"]}; border-radius: 16px; box-shadow: {SH_LG}; display: flex; flex-direction: column; font-family: {FONT}">'
            f'<div style="display: flex; gap: 14px; align-items: flex-start; padding: 24px 24px 0">{ict}<h2 style="margin: 0; {TY["hmd"]}; font-size: 20px; flex-grow: 1; padding-top: 6px">{title}</h2>{ibtn("x", "Đóng", "ghost", 36)}</div>'
            f'<div style="padding: 16px 24px 24px; display: flex; flex-direction: column; gap: 16px; {TY["bsm"]}; font-size: 14px; color: {C["t2"]}">{inner}</div>'
            f'<div style="display: flex; gap: 8px; justify-content: flex-end; padding: 16px 24px; border-top: 1px solid {C["b2"]}">{actions}</div></div></div>')


def section_card(title, inner, right="", pad=20, extra=""):
    return (f'<section style="background: {C["card"]}; border: 1px solid {C["b2"]}; border-radius: 12px; display: flex; flex-direction: column{"; " + extra if extra else ""}">'
            f'<div style="display: flex; align-items: center; gap: 8px; padding: 14px {pad}px; border-bottom: 1px solid {C["b1"]}"><h2 style="margin: 0; {TY["hsm"]}; font-size: 16px; flex-grow: 1">{title}</h2>{right}</div>'
            f'<div style="padding: 16px {pad}px; display: flex; flex-direction: column; gap: 12px">{inner}</div></section>')


def ovl(s):
    return f'<div style="{TY["ovl"]}; color: {C["t3"]}">{s}</div>'


# ---- artboard file ----
FONTS_LINK = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@500;600&amp;display=swap">'


def dc_file(title, root_html, w, h_):
    return f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>{e(title)}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS_LINK}
<style>
body{{margin:0;font-family:{FONT};color:#0F0E0E;background:#F5F5F4}}
a{{color:#0F0E0E}}a:hover{{color:#C31834}}
</style>
</helmet>
{root_html}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h_}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
"""


def states_board(phones):
    """phones: list of (state_label, phone_html). returns root html, w, h"""
    n = len(phones)
    w = n * PW + (n - 1) * 40
    h_ = PH + 40
    items = ""
    for lab, ph in phones:
        items += (f'<div style="display: flex; flex-direction: column; gap: 12px; width: {PW}px">'
                  f'<div style="display: flex; align-items: center; gap: 8px; height: 28px"><span style="{TY["lbl"]}; color: {C["t2"]}">{lab}</span></div>{ph}</div>')
    root = f'<div style="width: {w}px; height: {h_}px; display: flex; gap: 40px; font-family: {FONT}; background: transparent">{items}</div>'
    return root, w, h_
