/* 3학년 2학기 시험 정리 — 사이드바 / 테마 / 목차 / 검색 */
(function () {
  "use strict";

  /* ── 테마 ─────────────────────────────── */
  var root = document.documentElement;
  try {
    var saved = localStorage.getItem("theme");
    if (saved === "light" || saved === "dark") root.setAttribute("data-theme", saved);
  } catch (e) { /* 프라이빗 모드 등 */ }

  var themeBtn = document.querySelector(".theme-btn");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var cur = root.getAttribute("data-theme");
      var isDark = cur === "dark" ||
        (cur !== "light" && window.matchMedia("(prefers-color-scheme: dark)").matches);
      var next = isDark ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
    });
  }

  /* ── 모바일 사이드바 ──────────────────── */
  var menuBtn = document.querySelector(".menu-btn");
  if (menuBtn) {
    menuBtn.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      menuBtn.setAttribute("aria-expanded", String(open));
    });
    document.addEventListener("click", function (e) {
      if (!document.body.classList.contains("nav-open")) return;
      if (e.target.closest(".sidebar") || e.target.closest(".menu-btn")) return;
      document.body.classList.remove("nav-open");
      menuBtn.setAttribute("aria-expanded", "false");
    });
  }

  /* ── 코드 블록 복사 버튼 ──────────────── */
  document.querySelectorAll(".codehilite").forEach(function (box) {
    var code = box.querySelector("code");
    if (!code) return;
    var btn = document.createElement("button");
    btn.className = "copy-btn";
    btn.type = "button";
    btn.textContent = "복사";
    btn.addEventListener("click", function () {
      var text = code.innerText;
      var done = function () {
        btn.textContent = "복사됨";
        setTimeout(function () { btn.textContent = "복사"; }, 1400);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () {});
      } else {
        var ta = document.createElement("textarea");
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand("copy"); done(); } catch (e) {}
        document.body.removeChild(ta);
      }
    });
    box.appendChild(btn);
  });

  /* ── 우측 목차 현재 위치 표시 ─────────── */
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc-rail a[href^='#']"));
  if (tocLinks.length && "IntersectionObserver" in window) {
    var byId = {};
    tocLinks.forEach(function (a) { byId[decodeURIComponent(a.getAttribute("href").slice(1))] = a; });
    var heads = Object.keys(byId)
      .map(function (id) { return document.getElementById(id); })
      .filter(Boolean);
    var visible = new Set();
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) visible.add(en.target.id); else visible.delete(en.target.id);
      });
      var first = heads.find(function (h) { return visible.has(h.id); });
      tocLinks.forEach(function (a) { a.classList.remove("active"); });
      if (first && byId[first.id]) byId[first.id].classList.add("active");
    }, { rootMargin: "-60px 0px -70% 0px" });
    heads.forEach(function (h) { io.observe(h); });
  }

  /* ── 검색 ─────────────────────────────── */
  var input = document.getElementById("search");
  var panel = document.getElementById("search-results");
  if (!input || !panel) return;

  var index = null, loading = false, sel = -1, items = [];

  function load() {
    if (index || loading) return Promise.resolve();
    loading = true;
    return fetch(window.SEARCH_INDEX_URL)
      .then(function (r) { return r.json(); })
      .then(function (j) { index = j; })
      .catch(function () { index = []; })
      .finally(function () { loading = false; });
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function highlight(text, terms) {
    var out = esc(text);
    terms.forEach(function (t) {
      if (!t) return;
      out = out.replace(new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "gi"), "<mark>$1</mark>");
    });
    return out;
  }

  // 검색 인덱스의 URL은 루트(index.html) 기준이므로,
  // 상단 브랜드 링크가 가리키는 루트 경로를 앞에 붙여 현재 페이지 깊이를 보정한다.
  function resolve(url) {
    var base = document.querySelector(".brand");
    var prefix = base ? base.getAttribute("href").replace(/index\.html$/, "") : "";
    return prefix + url;
  }

  function render(q) {
    var terms = q.trim().toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length) { panel.hidden = true; return; }

    var scored = [];
    (index || []).forEach(function (row) {
      var hay = (row.heading + " " + row.page + " " + row.text).toLowerCase();
      var score = 0, ok = true;
      terms.forEach(function (t) {
        if (hay.indexOf(t) === -1) { ok = false; return; }
        if (row.heading.toLowerCase().indexOf(t) !== -1) score += 10;
        if (row.page.toLowerCase().indexOf(t) !== -1) score += 4;
        score += 1;
      });
      if (ok) scored.push({ row: row, score: score });
    });

    scored.sort(function (a, b) { return b.score - a.score; });
    items = scored.slice(0, 25);
    sel = -1;

    if (!items.length) {
      panel.innerHTML = '<div class="sr-empty">검색 결과가 없습니다</div>';
      panel.hidden = false;
      return;
    }

    panel.innerHTML = items.map(function (it) {
      var r = it.row;
      return '<a class="sr-item" href="' + esc(resolve(r.url)) + '">' +
        '<div class="sr-head">' + highlight(r.heading || r.page, terms) + "</div>" +
        (r.heading ? '<div class="sr-page">' + esc(r.page) + "</div>" : "") +
        '<div class="sr-text">' + highlight(r.text, terms) + "</div>" +
        "</a>";
    }).join("");
    panel.hidden = false;
  }

  function move(delta) {
    var els = panel.querySelectorAll(".sr-item");
    if (!els.length) return;
    if (sel >= 0) els[sel].classList.remove("sel");
    sel = (sel + delta + els.length) % els.length;
    els[sel].classList.add("sel");
    els[sel].scrollIntoView({ block: "nearest" });
  }

  input.addEventListener("input", function () {
    var q = input.value;
    if (!q.trim()) { panel.hidden = true; return; }
    load().then(function () { render(q); });
  });

  input.addEventListener("focus", load);

  input.addEventListener("keydown", function (e) {
    if (e.key === "ArrowDown") { e.preventDefault(); move(1); }
    else if (e.key === "ArrowUp") { e.preventDefault(); move(-1); }
    else if (e.key === "Enter") {
      var els = panel.querySelectorAll(".sr-item");
      if (sel >= 0 && els[sel]) { e.preventDefault(); location.href = els[sel].getAttribute("href"); }
    } else if (e.key === "Escape") {
      input.value = ""; panel.hidden = true; input.blur();
    }
  });

  document.addEventListener("click", function (e) {
    if (!e.target.closest("#search-results") && e.target !== input) panel.hidden = true;
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "/" && document.activeElement !== input &&
        !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) {
      e.preventDefault();
      input.focus();
      input.select();
    }
  });
})();
