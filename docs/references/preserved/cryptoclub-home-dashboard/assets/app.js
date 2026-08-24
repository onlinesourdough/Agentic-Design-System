(function () {
  const fmtDkk = (n) =>
    new Intl.NumberFormat("da-DK", {
      style: "currency",
      currency: "DKK",
      maximumFractionDigits: 0,
    }).format(n);

  const icons = {
    home: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 10.5 12 4l8 6.5V20a1 1 0 0 1-1 1h-5v-6H10v6H5a1 1 0 0 1-1-1v-9.5Z"/></svg>',
    portfolio:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 7h16M4 12h10M4 17h16"/><circle cx="18" cy="12" r="2.5"/></svg>',
    classroom:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 4 3 8.5 12 13l9-4.5L12 4Z"/><path d="M5 10.5V16c0 1.2 3.1 3 7 3s7-1.8 7-3v-5.5"/></svg>',
    chat: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 6.5h14a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2H9l-4 3v-3.5H5a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2Z"/></svg>',
    ecosystem:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="6" cy="6" r="2"/><circle cx="18" cy="6" r="2"/><circle cx="12" cy="18" r="2"/><path d="M8 6h8M7.2 7.6 10.8 16.4M16.8 7.6 13.2 16.4"/></svg>',
    grid: '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="5" cy="5" r="1.6"/><circle cx="12" cy="5" r="1.6"/><circle cx="19" cy="5" r="1.6"/><circle cx="5" cy="12" r="1.6"/><circle cx="12" cy="12" r="1.6"/><circle cx="19" cy="12" r="1.6"/><circle cx="5" cy="19" r="1.6"/><circle cx="12" cy="19" r="1.6"/><circle cx="19" cy="19" r="1.6"/></svg>',
    search:
      '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
    menu: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    arrow:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 12h14m-5-5 5 5-5 5"/></svg>',
    external:
      '<svg class="external-glyph" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14 5h5v5M19 5l-8 8"/><path d="M17 13v5a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1h5"/></svg>',
    signal:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 17 9 12l3 3 7-8"/><path d="M14 7h5v5"/></svg>',
    ai: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3.5a6.5 6.5 0 0 0-3.8 11.8L7.5 20l4.2-2a6.5 6.5 0 1 0 .3-14.5Z"/><path d="M9.5 10.3h.01M14.5 10.3h.01M9.6 13.2c1.5 1 3.3 1 4.8 0"/></svg>',
    user: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="8" r="3.5"/><path d="M5 20c.7-4 3-6 7-6s6.3 2 7 6"/></svg>',
    settings:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="3"/><path d="M19 13.5v-3l-2-.7-.6-1.4.9-1.9-2.1-2.1-1.9.9-1.4-.6L10.5 3h-3l-.7 2-1.4.6-1.9-.9-2.1 2.1.9 1.9-.6 1.4-2 .7v3l2 .7.6 1.4-.9 1.9 2.1 2.1 1.9-.9 1.4.6.7 2h3l.7-2 1.4-.6 1.9.9 2.1-2.1-.9-1.9.6-1.4 2-.7Z" transform="translate(2.5 0) scale(.8)"/></svg>',
    help: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M9.8 9a2.4 2.4 0 1 1 3.8 2c-1 .7-1.6 1.1-1.6 2.5M12 17h.01"/></svg>',
    logout:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M10 5H5v14h5M14 8l4 4-4 4M8 12h10"/></svg>',
    chevron:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="m8 10 4 4 4-4"/></svg>',
  };

  const navItems = [
    { id: "dashboard", label: "Dashboard", href: "index.html", icon: "home" },
    {
      id: "intelligence",
      label: "Market Intelligence",
      href: "intelligence.html",
      icon: "signal",
    },
    {
      id: "portfolio",
      label: "Portfolio",
      href: "portfolio.html",
      icon: "portfolio",
    },
    {
      id: "classroom",
      label: "Classroom",
      href: "classroom.html",
      icon: "classroom",
      badge: () => CryptoClubMock.classroom.activeModules,
    },
    {
      id: "chat",
      label: "Chat",
      href: "chat.html",
      icon: "chat",
      badge: () => CryptoClubMock.chat.unread,
    },
    {
      id: "ecosystem",
      label: "Økosystem",
      href: "ecosystem.html",
      icon: "ecosystem",
    },
  ];

  function showToast(message) {
    let toast = document.querySelector(".toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.className = "toast";
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.dataset.show = "true";
    window.clearTimeout(showToast._t);
    showToast._t = window.setTimeout(() => {
      toast.dataset.show = "false";
    }, 2400);
  }

  function renderSparkline(values, width, height, stroke) {
    const min = Math.min(...values);
    const max = Math.max(...values);
    const range = max - min || 1;
    const pts = values
      .map((v, i) => {
        const x = (i / (values.length - 1)) * width;
        const y = height - ((v - min) / range) * (height - 8) - 4;
        return `${x},${y}`;
      })
      .join(" ");
    return `<svg viewBox="0 0 ${width} ${height}" role="img" aria-label="Udvikling 7 dage"><polyline fill="none" stroke="${stroke}" stroke-width="2.2" points="${pts}"/></svg>`;
  }

  function renderAreaChart(values, width, height) {
    const min = Math.min(...values);
    const max = Math.max(...values);
    const range = max - min || 1;
    const points = values.map((value, index) => {
      const x = (index / (values.length - 1)) * width;
      const y = height - ((value - min) / range) * (height - 20) - 8;
      return [x, y];
    });
    const line = points.map(([x, y]) => `${x},${y}`).join(" ");
    const area = `0,${height} ${line} ${width},${height}`;
    const last = points.at(-1);
    return `<svg viewBox="0 0 ${width} ${height}" role="img" aria-label="Porteføljens udvikling de seneste syv dage" preserveAspectRatio="none">
      <defs><linearGradient id="portfolioFill" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#5b91df" stop-opacity=".22"/><stop offset="1" stop-color="#5b91df" stop-opacity="0"/></linearGradient></defs>
      <path d="M0 ${height - 1}H${width}" stroke="#292929" stroke-width="1"/>
      <polygon points="${area}" fill="url(#portfolioFill)"/>
      <polyline points="${line}" fill="none" stroke="#6d9ddd" stroke-width="2" vector-effect="non-scaling-stroke"/>
      <circle cx="${last[0]}" cy="${last[1]}" r="3" fill="#8db4eb" stroke="#171717" stroke-width="2" vector-effect="non-scaling-stroke"/>
    </svg>`;
  }

  function renderDonut(segments, size) {
    const r = size / 2 - 8;
    const c = 2 * Math.PI * r;
    let offset = 0;
    const arcs = segments
      .map((s) => {
        const len = (s.pct / 100) * c;
        const dash = `${len} ${c - len}`;
        const rot = (offset / c) * 360 - 90;
        offset += len;
        return `<circle cx="${size / 2}" cy="${size / 2}" r="${r}" fill="none" stroke="${s.color}" stroke-width="14" stroke-dasharray="${dash}" transform="rotate(${rot} ${size / 2} ${size / 2})"/>`;
      })
      .join("");
    return `<svg viewBox="0 0 ${size} ${size}" role="img" aria-label="Allokering">${arcs}<text x="50%" y="50%" text-anchor="middle" dominant-baseline="middle" fill="#ececec" font-size="13" font-family="ui-monospace, monospace">DKK</text></svg>`;
  }

  function renderGauge(value, label) {
    const angle = (value / 100) * 180;
    const rad = (angle * Math.PI) / 180;
    const x = 80 + 60 * Math.cos(Math.PI - rad);
    const y = 80 - 60 * Math.sin(Math.PI - rad);
    return `<svg viewBox="0 0 160 90" role="img" aria-label="Fear and Greed ${value}"><path d="M20 80 A60 60 0 0 1 140 80" fill="none" stroke="#2f2f2f" stroke-width="10"/><path d="M20 80 A60 60 0 0 1 ${x} ${y}" fill="none" stroke="#f7c35b" stroke-width="10"/><text x="80" y="72" text-anchor="middle" fill="#ececec" font-size="18" font-weight="600">${value}</text><text x="80" y="88" text-anchor="middle" fill="#9b9b9b" font-size="11">${label}</text></svg>`;
  }

  function mountShell() {
    const page = document.body.dataset.page;
    const navHtml = navItems
      .map((item) => {
        const current = item.id === page ? ' aria-current="page"' : "";
        const badge = item.badge ? item.badge() : 0;
        const badgeHtml = badge ? `<span class="badge">${badge}</span>` : "";
        return `<a href="${item.href}"${current}>${icons[item.icon]}${item.label}${badgeHtml}</a>`;
      })
      .join("");

    const shell = document.getElementById("app-shell");
    if (!shell) return;

    shell.innerHTML = `
      <aside class="sidebar" aria-label="Primær navigation">
        <a class="brand" href="index.html">
          <img src="assets/logo.png" width="34" height="34" alt="" />
          <div><strong>Crypto Club</strong></div>
        </a>
        <div class="nav-section">Overblik</div>
        <nav class="nav">${navHtml}</nav>
        <div class="nav-section">Værktøjer</div>
        <nav class="nav">
          <a href="https://app.cryptoclub.dk" target="_blank" rel="noopener">${icons.ai}AI Matthæus${icons.external}</a>
        </nav>
        <div class="profile-anchor">
          <button class="sidebar-profile" id="profileTrigger" type="button" aria-expanded="false" aria-controls="profileMenu">
            <span class="profile-avatar" aria-hidden="true">👤</span><div><strong>Test bruger</strong><span>Inner Circle medlem</span></div>${icons.chevron}
          </button>
          <div class="profile-menu" id="profileMenu" hidden>
            <div class="profile-menu-head"><span class="profile-avatar large" aria-hidden="true">👤</span><div><strong>Test bruger</strong><span>test@cryptoclub.dk</span><em>Inner Circle medlem</em></div></div>
            <nav aria-label="Profilmenu">
              <a href="settings.html#profile">${icons.user}<span><strong>Profil</strong><small>Navn og medlemskab</small></span></a>
              <a href="settings.html#preferences">${icons.settings}<span><strong>Indstillinger</strong><small>Notifikationer og visning</small></span></a>
              <button type="button" data-demo="Hjælpecenteret åbnes i den færdige app">${icons.help}<span><strong>Hjælp & support</strong><small>Guides og kontakt</small></span></button>
            </nav>
            <button class="profile-logout" type="button" data-demo="Log ud er deaktiveret i previewet">${icons.logout}Log ud</button>
          </div>
        </div>
      </aside>
      <div class="main">
        <main class="page" id="page-content"></main>
      </div>
      <dialog id="switcher" aria-label="App-vælger">
        <div class="dialog-head"><strong>Apps</strong><button class="btn btn-ghost" type="button" id="closeSwitcher" style="height:32px;padding:0 10px">Luk</button></div>
        <div class="dialog-body"><div class="apps" id="appsGrid"></div></div>
      </dialog>`;
  }

  function bindShell() {
    const dialog = document.getElementById("switcher");
    const closeBtn = document.getElementById("closeSwitcher");
    const appsGrid = document.getElementById("appsGrid");
    const profileTrigger = document.getElementById("profileTrigger");
    const profileMenu = document.getElementById("profileMenu");
    const searchInput = document.getElementById("globalSearch");
    const searchResults = document.getElementById("searchResults");

    closeBtn?.addEventListener("click", () => dialog?.close());
    dialog?.addEventListener("click", (e) => {
      const rect = dialog.getBoundingClientRect();
      const inside =
        e.clientX >= rect.left &&
        e.clientX <= rect.right &&
        e.clientY >= rect.top &&
        e.clientY <= rect.bottom;
      if (!inside) dialog.close();
    });

    if (appsGrid)
      appsGrid.innerHTML = CryptoClubMock.apps
        .map((app) => {
          const icon =
            app.icon === "logo"
              ? '<img src="assets/logo.png" alt="" />'
              : `<span class="tile-icon ${app.tone || "neutral"}" aria-hidden="true">${icons[app.icon] || icons.grid}</span>`;
          const target = app.internal ? "" : ' target="_blank" rel="noopener"';
          return `<a class="app-tile" href="${app.href}"${target}>${icon}<strong>${app.name}</strong><span>${app.desc}</span><em>${app.internal ? "Crypto Club" : "Ekstern app"}</em></a>`;
        })
        .join("");

    profileTrigger?.addEventListener("click", () => {
      const open = profileMenu.hidden;
      profileMenu.hidden = !open;
      profileTrigger.setAttribute("aria-expanded", String(open));
    });
    profileMenu?.addEventListener("click", (event) => event.stopPropagation());
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && profileMenu && !profileMenu.hidden) {
        profileMenu.hidden = true;
        profileTrigger?.setAttribute("aria-expanded", "false");
        profileTrigger?.focus();
      }
    });
    document.addEventListener("click", (event) => {
      if (
        profileMenu &&
        !profileMenu.hidden &&
        !event.target.closest(".profile-anchor")
      ) {
        profileMenu.hidden = true;
        profileTrigger?.setAttribute("aria-expanded", "false");
      }
    });
    bindDemoActions(profileMenu);

    let selected = -1;
    function renderSearch(q) {
      const query = q.trim().toLowerCase();
      const hits = query
        ? CryptoClubMock.searchIndex.filter((item) =>
            `${item.title} ${item.subtitle} ${item.kind}`
              .toLowerCase()
              .includes(query),
          )
        : [];
      if (!hits.length) {
        searchResults.dataset.open = "false";
        searchResults.innerHTML = "";
        selected = -1;
        return;
      }
      searchResults.dataset.open = "true";
      searchResults.innerHTML = hits
        .map(
          (hit, i) =>
            `<button type="button" class="search-hit" data-href="${hit.href}" data-i="${i}" role="option">${hit.title}<small>${hit.subtitle} · ${hit.kind}</small></button>`,
        )
        .join("");
    }

    searchInput?.addEventListener("input", (e) => renderSearch(e.target.value));
    searchInput?.addEventListener("keydown", (e) => {
      const hits = [...searchResults.querySelectorAll(".search-hit")];
      if (!hits.length) return;
      if (e.key === "ArrowDown") {
        e.preventDefault();
        selected = Math.min(selected + 1, hits.length - 1);
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        selected = Math.max(selected - 1, 0);
      } else if (e.key === "Enter" && selected >= 0) {
        e.preventDefault();
        const href = hits[selected].dataset.href;
        if (href?.startsWith("http")) window.open(href, "_blank");
        else window.location.href = href;
        return;
      } else if (e.key === "Escape") {
        searchResults.dataset.open = "false";
        return;
      } else return;
      hits.forEach((el, i) =>
        el.setAttribute("aria-selected", i === selected ? "true" : "false"),
      );
    });

    searchResults?.addEventListener("click", (e) => {
      const btn = e.target.closest(".search-hit");
      if (!btn) return;
      const href = btn.dataset.href;
      if (href?.startsWith("http")) window.open(href, "_blank");
      else window.location.href = href;
    });

    document.addEventListener("click", (e) => {
      if (searchResults && !e.target.closest(".search-wrap"))
        searchResults.dataset.open = "false";
    });
  }

  function bindTabs(root) {
    root?.querySelectorAll("[data-tabs]").forEach((tabs) => {
      const buttons = [...tabs.querySelectorAll(".tab")];
      const panels = [
        ...tabs.parentElement.querySelectorAll("[data-tab-panel]"),
      ];
      buttons.forEach((btn) => {
        btn.addEventListener("click", () => {
          const id = btn.dataset.tab;
          buttons.forEach((b) =>
            b.setAttribute("aria-selected", b === btn ? "true" : "false"),
          );
          panels.forEach((p) => {
            p.hidden = p.dataset.tabPanel !== id;
          });
        });
      });
    });
  }

  function bindAccordion(root) {
    root?.querySelectorAll(".accordion-trigger").forEach((btn) => {
      btn.addEventListener("click", () => {
        const item = btn.closest(".accordion-item");
        const open = item.dataset.open === "true";
        item.dataset.open = open ? "false" : "true";
        btn.setAttribute("aria-expanded", open ? "false" : "true");
      });
    });
  }

  function bindDemoActions(root) {
    root?.querySelectorAll("[data-demo]").forEach((el) => {
      el.addEventListener("click", () => showToast(el.dataset.demo));
    });
  }

  window.CryptoClubUI = {
    fmtDkk,
    icons,
    showToast,
    renderSparkline,
    renderAreaChart,
    renderDonut,
    renderGauge,
    mountShell,
    bindShell,
    bindTabs,
    bindAccordion,
    bindDemoActions,
  };
})();
