/* @ds-bundle: {"format":4,"namespace":"Onway","components":[{"name":"Logo"},{"name":"AppIcon"},{"name":"Icon"},{"name":"Button"},{"name":"IconButton"},{"name":"Avatar"},{"name":"Card"},{"name":"Badge"},{"name":"Tag"},{"name":"TopBar"},{"name":"TabBar"},{"name":"Tabs"},{"name":"SidebarNav"},{"name":"ListRow"},{"name":"Input"},{"name":"Select"},{"name":"Checkbox"},{"name":"Radio"},{"name":"Switch"},{"name":"SegmentedControl"},{"name":"Skeleton"},{"name":"Toast"},{"name":"Banner"},{"name":"Dialog"},{"name":"Sheet"},{"name":"Tooltip"},{"name":"EmptyState"},{"name":"ProgressBar"},{"name":"StatusPill"},{"name":"MapSurface"},{"name":"JobStatusHeader"},{"name":"Timeline"},{"name":"PriceRow"},{"name":"QuantityStepper"},{"name":"RatingStars"},{"name":"StatCard"},{"name":"JobCard"},{"name":"ProofUpload"},{"name":"AddressPicker"},{"name":"ChatRoom"},{"name":"ComplaintForm"},{"name":"DataTable"},{"name":"AdminDrawer"},{"name":"RegionEditorToolbar"},{"name":"CatalogEditor"},{"name":"PolicyConfigForm"},{"name":"FilterBar"}]} */
(function () {
  var h = window.React.createElement;

  /* ---------- shared status data (StatusPill, JobStatusHeader, JobCard) ---------- */
  var STATUS_TONE = {
    requested: "info", searching: "info", matching: "info", accepted: "info", confirmed: "info",
    arriving: "warning", arrived: "warning", preparing: "warning", atOutlet: "warning", pickup: "warning",
    proofPending: "warning", changeRequested: "warning", pendingReview: "warning", unpaid: "warning", paused: "warning",
    inProgress: "accent", delivering: "accent", appeal: "accent",
    completed: "success", proofVerified: "success", online: "success", approved: "success", active: "success", published: "success",
    proofRejected: "danger", disputed: "danger", issue: "danger", rejected: "danger", locked: "danger",
    cancelled: "neutral", offline: "neutral", expired: "neutral", draft: "neutral", finalized: "neutral"
  };
  var TONE_MARK = { info: "dot", warning: "!", accent: "dot", success: "✓", danger: "✕", neutral: null };
  var STATUS_LABEL_VI = {
    requested: "Đã yêu cầu", searching: "Đang tìm tài xế", matching: "Đang ghép", accepted: "Đã nhận", confirmed: "Đã xác nhận",
    arriving: "Đang đến", arrived: "Đã đến điểm đón", preparing: "Đang chuẩn bị", atOutlet: "Tại cửa hàng", pickup: "Đang lấy hàng",
    proofPending: "Chờ chứng từ", changeRequested: "Yêu cầu đổi", pendingReview: "Chờ duyệt", unpaid: "Chưa thanh toán", paused: "Tạm dừng",
    inProgress: "Đang thực hiện", delivering: "Đang giao", appeal: "Đang khiếu nại",
    completed: "Hoàn tất", proofVerified: "Đã xác nhận", online: "Trực tuyến", approved: "Đã duyệt", active: "Đang hoạt động", published: "Đã đăng",
    proofRejected: "Chứng từ bị từ chối", disputed: "Đang tranh chấp", issue: "Có sự cố", rejected: "Bị từ chối", locked: "Đã khoá",
    cancelled: "Đã huỷ", offline: "Ngoại tuyến", expired: "Hết hạn", draft: "Bản nháp", finalized: "Đã chốt"
  };

  /* ---------- brand ---------- */
  function Logo(props) {
    props = props || {};
    var variant = props.variant || "light"; // light | dark | ink | white
    var src = { light: "../../assets/Logos/logo.svg", dark: "../../assets/Logos/logo-dark.svg", ink: "../../assets/Logos/logo-ink.svg", white: "../../assets/Logos/logo-white.svg" }[variant];
    return h("img", { className: "onway-logo", src: src, alt: "Onway", style: { height: (props.height || 24) + "px" } });
  }

  function AppIcon(props) {
    props = props || {};
    var variant = props.variant || "customer"; // customer | driver | favicon
    var src = { customer: "../../assets/Logos/logo-appicon.svg", driver: "../../assets/Logos/logo-appicon-ink.svg", favicon: "../../assets/Logos/logo-appicon-light.svg" }[variant];
    return h("img", { className: "onway-appicon", src: src, alt: "Onway app icon", style: { width: (props.size || 56) + "px", height: (props.size || 56) + "px", borderRadius: "var(--radius-xl)" } });
  }

  var ICON_PATHS = {
    home: "M4 11 12 4l8 7v8a1 1 0 0 1-1 1h-5v-6H10v6H5a1 1 0 0 1-1-1z",
    search: "M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14zM21 21l-4.3-4.3",
    bell: "M6 10a6 6 0 1 1 12 0v4l2 3H4l2-3z M10 20a2 2 0 0 0 4 0",
    car: "M5 16h14v-3l-2-5H7l-2 5zM7 16v2M17 16v2",
    check: "M4 12l5 5L20 6",
    close: "M6 6l12 12M18 6L6 18",
    plus: "M12 5v14M5 12h14",
    filter: "M4 5h16M7 12h10M10 19h4",
    wifiOff: "M2 8.8C5 6 8.3 5 12 5s7 1 10 3.8M5 12.5c2-1.6 4.4-2.5 7-2.5s5 .9 7 2.5M8.5 16c1-.8 2.2-1.3 3.5-1.3s2.5.5 3.5 1.3M2 2l20 20 M12 19.5h.01"
  };
  function Icon(props) {
    props = props || {};
    var name = props.name || "check";
    var size = props.size || 20;
    return h(
      "svg", { className: "onway-icon", width: size, height: size, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: 2, strokeLinecap: "round", strokeLinejoin: "round", "aria-hidden": "true" },
      h("path", { d: ICON_PATHS[name] || ICON_PATHS.check })
    );
  }

  /* ---------- core ---------- */
  function Button(props) {
    props = props || {};
    var variant = props.variant || "primary";
    var size = props.size || "lg";
    var state = props.state || "default";
    var cls = ["onway-btn", "onway-btn--" + variant, "onway-btn--" + size, "onway-btn--" + state].join(" ");
    var isDisabled = state === "disabled" || state === "loading";
    return h(
      "button",
      { className: cls, disabled: isDisabled, "aria-busy": state === "loading" ? "true" : undefined, "aria-disabled": state === "disabled" ? "true" : undefined },
      state === "loading" ? h("span", { className: "onway-btn__spinner", "aria-hidden": "true" }) : null,
      h("span", { className: "onway-btn__label" }, props.children || "Đặt xe")
    );
  }

  function IconButton(props) {
    props = props || {};
    var variant = props.variant || "toolbar";
    return h(
      "button",
      { className: "onway-iconbtn onway-iconbtn--" + variant, "aria-label": props.label || "Hành động", title: props.label || "Hành động" },
      h("span", { className: "onway-iconbtn__glyph", "aria-hidden": "true" }, props.glyph || "⊕")
    );
  }

  function Avatar(props) {
    props = props || {};
    var size = props.size || 40;
    var initials = props.initials || "NM";
    return h(
      "div",
      { className: "onway-avatar", style: { width: size + "px", height: size + "px" } },
      props.src ? h("img", { src: props.src, alt: props.name || "" }) : h("span", null, initials)
    );
  }

  function Card(props) {
    props = props || {};
    return h("div", { className: "onway-card" }, props.children);
  }

  function Badge(props) {
    props = props || {};
    var count = typeof props.count === "number" ? props.count : 3;
    var display = count > 99 ? "99+" : String(count);
    return h("span", { className: "onway-badge", "aria-label": display + " thông báo" }, display);
  }

  function Tag(props) {
    props = props || {};
    var selected = !!props.selected;
    return h(
      "button",
      { className: "onway-tag" + (selected ? " onway-tag--selected" : ""), "aria-pressed": selected ? "true" : "false" },
      props.children || "Thẻ"
    );
  }

  /* ---------- navigation ---------- */
  function TopBar(props) {
    props = props || {};
    return h(
      "header",
      { className: "onway-topbar" },
      h(IconButton, { label: "Quay lại", glyph: "←" }),
      h("span", { className: "onway-topbar__title" }, props.title || "Đặt xe"),
      h(IconButton, { label: "Thông báo", glyph: "●" })
    );
  }

  function TabBar(props) {
    props = props || {};
    var items = props.items || [
      { label: "Ride", icon: "car", active: true },
      { label: "Food", icon: "home" },
      { label: "Hoạt động", icon: "bell", badge: 3 },
      { label: "Tài khoản", icon: "search" }
    ];
    return h(
      "nav",
      { className: "onway-tabbar", "aria-label": "Điều hướng chính" },
      items.map(function (it, i) {
        return h(
          "div",
          { key: i, className: "onway-tabbar__item" + (it.active ? " onway-tabbar__item--active" : "") },
          h("div", { className: "onway-tabbar__icon-wrap" },
            h(Icon, { name: it.icon, size: 22 }),
            it.badge ? h(Badge, { count: it.badge }) : null
          ),
          h("span", null, it.label)
        );
      })
    );
  }

  function Tabs(props) {
    props = props || {};
    var items = props.items || ["Tất cả", "Đang chạy", "Hoàn tất", "Đã huỷ"];
    var active = typeof props.active === "number" ? props.active : 0;
    return h(
      "div",
      { className: "onway-tabs", role: "tablist" },
      items.map(function (label, i) {
        return h("button", { key: i, role: "tab", "aria-selected": i === active ? "true" : "false", className: "onway-tabs__tab" + (i === active ? " onway-tabs__tab--active" : "") }, label);
      })
    );
  }

  function SidebarNav(props) {
    props = props || {};
    var items = props.items || [
      { label: "Tổng quan", active: true },
      { label: "Chuyến & đơn", badge: 12 },
      { label: "Tài xế" },
      { label: "Khu vực" },
      { label: "Catalog" },
      { label: "Case" }
    ];
    return h(
      "nav",
      { className: "onway-sidebar", "aria-label": "Điều hướng quản trị" },
      h(Logo, { variant: "light", height: 22 }),
      h("div", { className: "onway-sidebar__list" },
        items.map(function (it, i) {
          return h(
            "div",
            { key: i, className: "onway-sidebar__item" + (it.active ? " onway-sidebar__item--active" : "") },
            h("span", null, it.label),
            it.badge ? h(Badge, { count: it.badge }) : null
          );
        })
      )
    );
  }

  function ListRow(props) {
    props = props || {};
    return h(
      "div",
      { className: "onway-row" },
      h("div", { className: "onway-row__main" },
        h("div", { className: "onway-row__title" }, props.title || "Địa chỉ nhà"),
        props.subtitle ? h("div", { className: "onway-row__subtitle" }, props.subtitle) : null
      ),
      props.trailing ? h("div", { className: "onway-row__trailing" }, props.trailing) : h(Icon, { name: "check", size: 16 })
    );
  }

  /* ---------- form ---------- */
  function Input(props) {
    props = props || {};
    var state = props.state || "default";
    var id = props.id || "onway-input";
    return h(
      "div",
      { className: "onway-field onway-field--" + state },
      h("label", { className: "onway-field__label", htmlFor: id }, props.label || "Nhãn"),
      h("input", {
        id: id,
        className: "onway-field__input",
        type: "text",
        defaultValue: props.value,
        placeholder: props.placeholder || "",
        disabled: state === "disabled",
        "aria-invalid": state === "error" ? "true" : undefined,
        "aria-describedby": state === "error" ? id + "-helper" : undefined
      }),
      state === "error"
        ? h("span", { className: "onway-field__helper onway-field__helper--error", id: id + "-helper" }, props.helper || "Thông tin chưa hợp lệ.")
        : null
    );
  }

  function Select(props) {
    props = props || {};
    var options = props.options || ["Xe 4 chỗ", "Xe 7 chỗ", "Xe máy"];
    return h(
      "div",
      { className: "onway-field" },
      h("label", { className: "onway-field__label" }, props.label || "Loại xe"),
      h("select", { className: "onway-field__input onway-field__select" }, options.map(function (o, i) { return h("option", { key: i }, o); }))
    );
  }

  function Checkbox(props) {
    props = props || {};
    return h(
      "label",
      { className: "onway-checkrow" },
      h("input", { type: "checkbox", className: "onway-checkbox", defaultChecked: props.checked }),
      h("span", null, props.children || "Tôi đồng ý")
    );
  }

  function Radio(props) {
    props = props || {};
    var options = props.options || ["Xe 4 chỗ", "Xe 7 chỗ"];
    return h(
      "div",
      { role: "radiogroup", "aria-label": props.label || "Chọn loại xe", style: { display: "flex", flexDirection: "column", gap: "8px" } },
      options.map(function (o, i) {
        return h("label", { key: i, className: "onway-checkrow" }, h("input", { type: "radio", name: "onway-radio", className: "onway-radio", defaultChecked: i === 0 }), h("span", null, o));
      })
    );
  }

  function Switch(props) {
    props = props || {};
    return h(
      "label",
      { className: "onway-switchrow" },
      h("span", null, props.children || "Trực tuyến"),
      h("span", { className: "onway-switch" + (props.checked ? " onway-switch--on" : ""), role: "switch", "aria-checked": props.checked ? "true" : "false" },
        h("span", { className: "onway-switch__knob" }))
    );
  }

  function SegmentedControl(props) {
    props = props || {};
    var items = props.items || ["Ride", "Food"];
    var active = typeof props.active === "number" ? props.active : 0;
    return h(
      "div",
      { className: "onway-segmented", role: "tablist" },
      items.map(function (label, i) {
        return h("button", { key: i, role: "tab", "aria-selected": i === active ? "true" : "false", className: "onway-segmented__item" + (i === active ? " onway-segmented__item--active" : "") }, label);
      })
    );
  }

  /* ---------- feedback / overlay ---------- */
  function Skeleton(props) {
    props = props || {};
    var variant = props.variant || "line";
    return h("div", { className: "onway-skeleton onway-skeleton--" + variant, role: "status", "aria-label": "Đang tải" });
  }

  function Toast(props) {
    props = props || {};
    var tone = props.tone || "success";
    return h(
      "div",
      { className: "onway-toast onway-toast--" + tone, "aria-live": tone === "danger" ? "assertive" : "polite" },
      h("span", null, props.children || "Đặt chuyến thành công."),
      props.action ? h("button", { className: "onway-toast__action" }, props.action) : null
    );
  }

  function Banner(props) {
    props = props || {};
    var tone = props.tone || "info";
    return h(
      "div",
      { className: "onway-banner onway-banner--" + tone, role: tone === "danger" ? "alert" : "status" },
      h("span", { className: "onway-banner__icon", "aria-hidden": "true" }),
      h("span", { className: "onway-banner__text" }, props.children || "Thông báo."),
      props.action ? h("button", { className: "onway-banner__action" }, props.action) : null
    );
  }

  function Dialog(props) {
    props = props || {};
    var critical = props.critical;
    return h(
      "div",
      { className: "onway-dialog-scrim" },
      h(
        "div",
        { className: "onway-dialog", role: "alertdialog", "aria-modal": "true" },
        h("div", { className: "heading-sm" }, props.title || "Huỷ chuyến này?"),
        h("div", { className: "onway-dialog__body body-sm" }, props.children || "Hành động này không thể hoàn tác."),
        critical ? h(Input, { label: "Lý do", id: "dialog-reason" }) : null,
        h("div", { className: "onway-dialog__actions" },
          h(Button, { variant: "ghost", size: "md" }, "Đóng"),
          h(Button, { variant: "destructive", size: "md", state: critical ? "disabled" : "default" }, "Xác nhận"))
      )
    );
  }

  function Sheet(props) {
    props = props || {};
    return h(
      "div",
      { className: "onway-sheet" },
      h("div", { className: "onway-sheet__handle", "aria-label": "Kéo để mở rộng" }),
      h("div", { className: "onway-sheet__body" }, props.children || h(JobStatusHeader, { status: "arriving" }))
    );
  }

  function Tooltip(props) {
    props = props || {};
    return h(
      "span",
      { className: "onway-tooltip-wrap" },
      h(IconButton, { label: props.label || "Sửa", glyph: "✎" }),
      h("span", { className: "onway-tooltip", role: "tooltip" }, props.children || props.label || "Sửa")
    );
  }

  function EmptyState(props) {
    props = props || {};
    return h(
      "div",
      { className: "onway-empty" },
      h(Icon, { name: props.icon || "search", size: 28 }),
      h("div", { className: "heading-sm" }, props.title || "Không có dữ liệu"),
      h("div", { className: "body-sm", style: { color: "var(--text-secondary)" } }, props.description || "Thử thay đổi bộ lọc để xem thêm kết quả.")
    );
  }

  function ProgressBar(props) {
    props = props || {};
    var value = typeof props.value === "number" ? props.value : 60;
    var steps = props.steps;
    if (steps) {
      return h(
        "div",
        { className: "onway-progress-steps", role: "progressbar", "aria-valuenow": value },
        steps.map(function (s, i) {
          return h("div", { key: i, className: "onway-progress-steps__step" + (i < (props.currentStep || 1) ? " onway-progress-steps__step--done" : "") });
        })
      );
    }
    return h(
      "div",
      { className: "onway-progress", role: "progressbar", "aria-valuenow": value, "aria-valuemin": 0, "aria-valuemax": 100 },
      h("div", { className: "onway-progress__fill", style: { width: value + "%" } })
    );
  }

  function StatusPill(props) {
    props = props || {};
    var status = props.status || "requested";
    var tone = STATUS_TONE[status] || "neutral";
    var size = props.size || "md";
    var label = props.label || STATUS_LABEL_VI[status] || status;
    var mark = TONE_MARK[tone];
    var pulse = props.pulse && (status === "matching" || status === "searching");
    return h(
      "span",
      { className: "onway-pill onway-pill--" + tone + " onway-pill--" + size + (pulse ? " onway-pill--pulse" : "") },
      mark ? h("span", { className: "onway-pill__mark", "aria-hidden": "true" }, mark === "dot" ? "" : mark) : null,
      h("span", { className: "onway-pill__label" }, label)
    );
  }

  /* ---------- map ---------- */
  function MapSurface(props) {
    props = props || {};
    var variant = props.variant || "route"; // route | region
    return h(
      "div",
      { className: "onway-map", "aria-hidden": "true" },
      h("svg", { viewBox: "0 0 400 220", width: "100%", height: "220" },
        h("rect", { width: 400, height: 220, fill: "var(--map-land)" }),
        h("rect", { x: 40, y: 30, width: 120, height: 60, fill: "var(--map-block)" }),
        h("rect", { x: 220, y: 110, width: 100, height: 70, fill: "var(--map-park)" }),
        h("rect", { x: 0, y: 170, width: 400, height: 50, fill: "var(--map-water)" }),
        h("rect", { x: 0, y: 95, width: 400, height: 14, fill: "var(--map-road-major)" }),
        variant === "route"
          ? h(window.React.Fragment, null,
              h("path", { d: "M60 60 C 140 60, 180 160, 340 150", stroke: "var(--map-route-casing)", strokeWidth: 7, fill: "none", strokeLinecap: "round" }),
              h("path", { d: "M60 60 C 140 60, 180 160, 340 150", stroke: "var(--map-route)", strokeWidth: 4, fill: "none", strokeLinecap: "round" }),
              h("circle", { cx: 60, cy: 60, r: 6, fill: "var(--map-pin-pickup)" }),
              h("rect", { x: 333, y: 143, width: 14, height: 14, rx: 4, fill: "var(--map-pin-dropoff)", transform: "rotate(45 340 150)" })
            )
          : h("polygon", { points: "150,40 260,60 250,150 140,140", fill: "var(--map-region-selected-fill)", stroke: "var(--map-region-selected-stroke)", strokeWidth: 2 })
      )
    );
  }

  /* ---------- booking ---------- */
  function JobStatusHeader(props) {
    props = props || {};
    var status = props.status || "arriving";
    var issue = status === "issue" || status === "disputed" || status === "cancelled";
    return h(
      "div",
      { className: "onway-jobheader" },
      h(StatusPill, { status: status, pulse: true }),
      h("div", { className: "onway-jobheader__headline" }, props.headline || "Anh Minh đang đến điểm đón"),
      h("div", { className: "onway-jobheader__meta body-sm" }, props.meta || "ETA 4 phút · 48.000đ"),
      h("div", { className: "onway-jobheader__steps" },
        [0, 1, 2, 3].map(function (i) {
          return h("span", { key: i, className: "onway-jobheader__step" + (i <= (props.step || 1) ? (issue ? " onway-jobheader__step--issue" : " onway-jobheader__step--done") : "") });
        })
      )
    );
  }

  function Timeline(props) {
    props = props || {};
    var items = props.items || [
      { label: "Đã xác nhận", time: "14:02", state: "done" },
      { label: "Tài xế đang đến", time: "14:04", state: "current" },
      { label: "Đón khách", state: "pending" },
      { label: "Hoàn tất", state: "pending" }
    ];
    return h(
      "div",
      { className: "onway-timeline" },
      items.map(function (it, i) {
        return h(
          "div",
          { key: i, className: "onway-timeline__row" },
          h("span", { className: "onway-timeline__marker onway-timeline__marker--" + it.state, "aria-hidden": "true" }),
          h("div", { className: "onway-timeline__content" },
            h("div", { className: "body-sm" }, it.label),
            (it.time || it.actor) ? h("div", { className: "caption", style: { color: "var(--text-tertiary)" } }, [it.time, it.actor].filter(Boolean).join(" · ")) : null
          )
        );
      })
    );
  }

  function PriceRow(props) {
    props = props || {};
    var rows = props.rows || [
      { label: "Cước phí", value: "45.000đ" },
      { label: "Phí quãng đường", value: "3.000đ" },
      { label: "Hoa hồng nền tảng", value: "0đ" }
    ];
    return h(
      "div",
      { className: "onway-pricerow" },
      rows.map(function (r, i) {
        return h("div", { key: i, className: "onway-pricerow__row" }, h("span", { className: "body-sm" }, r.label), h("span", { className: "onway-pricerow__value" }, r.value));
      }),
      h("div", { className: "onway-pricerow__row onway-pricerow__row--total" }, h("span", null, "Tổng cộng"), h("span", { className: "onway-pricerow__value" }, "48.000đ"))
    );
  }

  function QuantityStepper(props) {
    props = props || {};
    var value = typeof props.value === "number" ? props.value : 1;
    return h(
      "div",
      { className: "onway-stepper" },
      h(IconButton, { label: "Giảm số lượng", glyph: "−" }),
      h("span", { className: "onway-stepper__value numeric" }, value),
      h(IconButton, { label: "Tăng số lượng", glyph: "+" })
    );
  }

  function RatingStars(props) {
    props = props || {};
    var value = typeof props.value === "number" ? props.value : 4;
    return h(
      "div",
      { className: "onway-stars", role: "img", "aria-label": value + " trên 5 sao" },
      [1, 2, 3, 4, 5].map(function (i) { return h("span", { key: i, className: "onway-stars__star" + (i <= value ? " onway-stars__star--on" : "") }, "★"); })
    );
  }

  function StatCard(props) {
    props = props || {};
    return h(
      "div",
      { className: "onway-statcard" },
      h("div", { className: "caption", style: { color: "var(--text-tertiary)" } }, props.label || "Chuyến hôm nay"),
      h("div", { className: "onway-statcard__value numeric" }, props.value || "1.284"),
      props.delta ? h("div", { className: "caption onway-statcard__delta" }, props.delta) : null
    );
  }

  function JobCard(props) {
    props = props || {};
    return h(
      "div",
      { className: "onway-card onway-jobcard" },
      h("div", { className: "onway-jobcard__top" },
        h(StatusPill, { status: props.status || "inProgress", size: "sm" }),
        h("span", { className: "caption", style: { color: "var(--text-tertiary)" } }, props.id || "#A1029")
      ),
      h("div", { className: "body-md", style: { fontWeight: 600 } }, props.customer || "Nguyễn Văn Minh"),
      h(PriceRow, { rows: [{ label: "Quãng đường", value: props.distance || "4.2 km" }] })
    );
  }

  /* ---------- upload / map patterns ---------- */
  function ProofUpload(props) {
    props = props || {};
    var state = props.state || "empty";
    if (state === "empty") {
      return h("div", { className: "onway-proof onway-proof--empty" }, h(Icon, { name: "plus", size: 20 }), h("span", { className: "body-sm" }, "Chụp hoặc chọn ảnh chứng từ"));
    }
    return h(
      "div",
      { className: "onway-proof onway-proof--filled" },
      h("div", { className: "onway-proof__thumb" }),
      h("div", { className: "onway-proof__info" },
        h(StatusPill, { status: state === "verified" ? "proofVerified" : state === "rejected" ? "proofRejected" : state === "uploading" ? "requested" : "proofPending", size: "sm" }),
        h("div", { className: "caption" }, props.filename || "chuyen-khoan.jpg"),
        h("div", { className: "numeric caption" }, props.amount || "48.000đ · REF9284"),
        state === "uploading" ? h(ProgressBar, { value: 55 }) : null,
        state === "rejected" ? h("div", { className: "caption", style: { color: "var(--text-danger)" } }, props.reason || "Ảnh mờ, không đọc được số tiền.") : null
      )
    );
  }

  function AddressPicker(props) {
    props = props || {};
    return h(
      "div",
      { className: "onway-addresspicker" },
      h(Input, { label: "Điểm đón", value: "227 Nguyễn Văn Cừ" }),
      h(ListRow, { title: "Vincom Đồng Khởi", subtitle: "72 Lê Thánh Tôn, Q1" }),
      h(ListRow, { title: "Sân bay Tân Sơn Nhất", subtitle: "Trường Sơn, Tân Bình" })
    );
  }

  function ChatRoom(props) {
    props = props || {};
    var messages = props.messages || [
      { from: "them", text: "Em ơi anh đang ở cổng B nhé." },
      { from: "me", text: "Dạ em ra ngay ạ." },
      { from: "them", text: "[Ảnh đã hết hạn]", expired: true }
    ];
    return h(
      "div",
      { className: "onway-chat" },
      messages.map(function (m, i) {
        return h("div", { key: i, className: "onway-chat__bubble onway-chat__bubble--" + m.from + (m.expired ? " onway-chat__bubble--expired" : "") }, m.text);
      })
    );
  }

  function ComplaintForm(props) {
    props = props || {};
    return h(
      "div",
      { className: "onway-form" },
      h(Radio, { label: "Lý do khiếu nại", options: ["Sai lộ trình", "Thái độ tài xế", "Tính phí sai"] }),
      h(Input, { label: "Mô tả thêm", placeholder: "Mô tả chi tiết vấn đề" }),
      h(ProofUpload, { state: "empty" })
    );
  }

  /* ---------- admin ---------- */
  function DataTable(props) {
    props = props || {};
    var rows = props.rows || [
      { id: "TX-3021", name: "Trần Văn A", status: "online" },
      { id: "TX-3022", name: "Lê Thị B", status: "offline" },
      { id: "TX-3023", name: "Phạm Văn C", status: "locked" }
    ];
    return h(
      "table",
      { className: "onway-table" },
      h("thead", null, h("tr", null, h("th", null, h("input", { type: "checkbox", className: "onway-checkbox" })), h("th", null, "Mã"), h("th", null, "Tên"), h("th", null, "Trạng thái"))),
      h("tbody", null, rows.map(function (r, i) {
        return h("tr", { key: i }, h("td", null, h("input", { type: "checkbox", className: "onway-checkbox" })), h("td", { className: "numeric" }, r.id), h("td", null, r.name), h("td", null, h(StatusPill, { status: r.status, size: "sm" })));
      }))
    );
  }

  function AdminDrawer(props) {
    props = props || {};
    return h(
      "div",
      { className: "onway-drawer" },
      h("div", { className: "onway-drawer__header" },
        h("span", { className: "heading-sm" }, props.title || "Chi tiết tài xế"),
        h(IconButton, { label: "Đóng", glyph: "✕" })
      ),
      h("div", { className: "onway-drawer__body" }, props.children || h(Timeline, { items: [{ label: "Đã duyệt hồ sơ", time: "12/09", actor: "admin.hoa", state: "done" }] }))
    );
  }

  function RegionEditorToolbar(props) {
    props = props || {};
    return h(
      "div",
      { className: "onway-toolbar" },
      h(IconButton, { label: "Vẽ vùng", glyph: "⬚" }),
      h(IconButton, { label: "Chọn", glyph: "↖" }),
      h(IconButton, { label: "Xoá điểm", glyph: "⌫" }),
      h(Button, { variant: "primary", size: "sm" }, "Xuất bản")
    );
  }

  function CatalogEditor(props) {
    props = props || {};
    return h(
      "div",
      { className: "onway-card", style: { padding: 0, overflow: "hidden" } },
      h(Tabs, { items: ["Món ăn", "Danh mục", "Combo"] }),
      h("div", { style: { padding: "var(--space-4)", display: "flex", flexDirection: "column", gap: "var(--space-3)" } },
        h(Input, { label: "Tên món", value: "Phở bò tái" }),
        h(StatusPill, { status: "draft", size: "sm" })
      )
    );
  }

  function PolicyConfigForm(props) {
    props = props || {};
    return h(
      "div",
      { className: "onway-form" },
      h(Select, { label: "Chính sách huỷ chuyến", options: ["Miễn phí trong 2 phút", "Phí cố định 10.000đ"] }),
      h(Switch, { checked: true }, "Bật xác nhận hai bước"),
      h(Button, { variant: "secondary", size: "md" }, "Lưu thay đổi")
    );
  }

  function FilterBar(props) {
    props = props || {};
    return h(
      "div",
      { className: "onway-filterbar" },
      h(Input, { label: "", placeholder: "Tìm theo mã, tên, số điện thoại" }),
      h(Tag, { selected: true }, "Đang hoạt động"),
      h(Tag, {}, "Đã khoá"),
      h(Select, { label: "", options: ["Tất cả khu vực", "Q1", "Q3", "Bình Thạnh"] })
    );
  }

  window.Onway = {
    Logo: Logo, AppIcon: AppIcon, Icon: Icon,
    Button: Button, IconButton: IconButton, Avatar: Avatar, Card: Card, Badge: Badge, Tag: Tag,
    TopBar: TopBar, TabBar: TabBar, Tabs: Tabs, SidebarNav: SidebarNav, ListRow: ListRow,
    Input: Input, Select: Select, Checkbox: Checkbox, Radio: Radio, Switch: Switch, SegmentedControl: SegmentedControl,
    Skeleton: Skeleton, Toast: Toast, Banner: Banner, Dialog: Dialog, Sheet: Sheet, Tooltip: Tooltip, EmptyState: EmptyState, ProgressBar: ProgressBar,
    StatusPill: StatusPill, MapSurface: MapSurface, JobStatusHeader: JobStatusHeader, Timeline: Timeline,
    PriceRow: PriceRow, QuantityStepper: QuantityStepper, RatingStars: RatingStars, StatCard: StatCard, JobCard: JobCard,
    ProofUpload: ProofUpload, AddressPicker: AddressPicker, ChatRoom: ChatRoom, ComplaintForm: ComplaintForm,
    DataTable: DataTable, AdminDrawer: AdminDrawer, RegionEditorToolbar: RegionEditorToolbar, CatalogEditor: CatalogEditor, PolicyConfigForm: PolicyConfigForm, FilterBar: FilterBar
  };
})();
