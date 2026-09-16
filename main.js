/* NUTRICYT — main.js
   Vanilla JS, sin dependencias externas. Patrón IIFE (funciona en file://,
   FTP y cualquier hosting estático). Cada init() está aislado con safe(). */
(function () {
  "use strict";

  var data = window.__NUTRICYT__ || {};
  var $ = function (sel, scope) { return (scope || document).querySelector(sel); };
  var $$ = function (sel, scope) { return Array.prototype.slice.call((scope || document).querySelectorAll(sel)); };
  var reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;

  function safe(fn, name) {
    try { fn(); } catch (e) { if (window.console) console.warn("[" + name + "]", e); }
  }

  /* -----------------------------------------------------------
     Nav: solidify on scroll + mobile menu
     ----------------------------------------------------------- */
  function initNav() {
    var nav = $("[data-nav]");
    if (!nav) return;
    var toggle = $("[data-nav-toggle]");
    var mobile = $("[data-nav-mobile]");

    function onScroll() {
      nav.classList.toggle("is-scrolled", window.scrollY > 12);
    }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });

    if (toggle && mobile) {
      toggle.addEventListener("click", function () {
        var open = toggle.getAttribute("aria-expanded") === "true";
        toggle.setAttribute("aria-expanded", String(!open));
        mobile.classList.toggle("is-open", !open);
        nav.classList.toggle("is-open-menu", !open);
        document.body.style.overflow = !open ? "hidden" : "";
      });
      $$("a", mobile).forEach(function (a) {
        a.addEventListener("click", function () {
          toggle.setAttribute("aria-expanded", "false");
          mobile.classList.remove("is-open");
          nav.classList.remove("is-open-menu");
          document.body.style.overflow = "";
        });
      });
    }
  }

  /* -----------------------------------------------------------
     Smooth anchor scroll (native scrollTo, respects reduced motion)
     ----------------------------------------------------------- */
  function initSmoothAnchors() {
    document.addEventListener("click", function (e) {
      var a = e.target.closest ? e.target.closest('a[href^="#"]') : null;
      if (!a) return;
      var id = a.getAttribute("href");
      if (!id || id === "#") return;
      var el = document.querySelector(id);
      if (!el) return;
      e.preventDefault();
      var navH = parseInt(getComputedStyle(document.documentElement).getPropertyValue("--nav-h")) || 84;
      var top = el.getBoundingClientRect().top + window.scrollY - navH + 1;
      window.scrollTo({ top: top, behavior: reduced ? "auto" : "smooth" });
      history.pushState(null, "", id);
    });
  }

  /* -----------------------------------------------------------
     Reveal on scroll — IntersectionObserver + 6s safety net
     ----------------------------------------------------------- */
  function initReveals() {
    var targets = $$(".reveal, .reveal-stagger");
    if (!targets.length) return;

    if (!("IntersectionObserver" in window)) {
      targets.forEach(function (el) { el.classList.add("is-visible"); });
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.03, rootMargin: "0px 0px -4% 0px" });

    targets.forEach(function (el) { io.observe(el); });

    setTimeout(function () {
      targets.forEach(function (el) {
        if (!el.classList.contains("is-visible") && el.getBoundingClientRect().top < window.innerHeight) {
          el.classList.add("is-visible");
        }
      });
    }, 6000);
  }

  /* -----------------------------------------------------------
     Hero — light parallax on the background photo (native scroll)
     ----------------------------------------------------------- */
  function initHeroParallax() {
    if (reduced) return;
    var img = $("[data-hero-media]");
    var hero = $(".hero");
    if (!img || !hero) return;
    var ticking = false;
    function update() {
      var rect = hero.getBoundingClientRect();
      var progress = Math.min(Math.max(1 - rect.bottom / (rect.height + window.innerHeight), 0), 1);
      var shift = progress * 46;
      img.style.transform = "translate3d(0," + shift + "px,0) scale(1.06)";
      ticking = false;
    }
    window.addEventListener("scroll", function () {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  /* -----------------------------------------------------------
     Contact form — validates then hands off via mailto (no backend)
     ----------------------------------------------------------- */
  function initContactForm() {
    var form = $("[data-contact-form]");
    if (!form) return;
    var status = $("[data-form-status]", form);

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;

      var fd = new FormData(form);
      var nombre = (fd.get("nombre") || "").toString().trim();
      var apellido = (fd.get("apellido") || "").toString().trim();
      var email = (fd.get("email") || "").toString().trim();
      var asunto = (fd.get("asunto") || "Consulta desde la web").toString().trim();
      var mensaje = (fd.get("mensaje") || "").toString().trim();

      var to = data.contactEmail || "contacto@nutricyt.com";
      var body = "Nombre: " + nombre + " " + apellido + "\nEmail: " + email + "\n\n" + mensaje;
      var mailto = "mailto:" + encodeURIComponent(to) +
        "?subject=" + encodeURIComponent("[NUTRICYT] " + asunto) +
        "&body=" + encodeURIComponent(body);

      if (status) {
        status.textContent = "Abriendo tu cliente de correo para enviar el mensaje…";
        status.classList.remove("is-error");
      }
      window.location.href = mailto;
      form.reset();
    });
  }

  /* -----------------------------------------------------------
     WhatsApp floating widget — keyword-based chat simulation.
     No AI, no external calls: pure client-side string matching.
     ----------------------------------------------------------- */
  function initWhatsAppWidget() {
    var widget = $("[data-wa-widget]");
    if (!widget) return;
    var fab = $("[data-wa-fab]", widget);
    var panel = $("[data-wa-panel]", widget);
    var body = $("[data-wa-body]", widget);
    var form = $("[data-wa-form]", widget);
    var input = $("[data-wa-input]", widget);

    var number = data.whatsappNumber || "18097499916";
    var genericMsg = data.whatsappGenericMessage || "Hola, quiero información sobre tus consultas de nutrición";

    var GREETINGS = ["hola", "holaa", "buenas", "buenos dias", "buenos días", "buenas tardes",
      "buenas noches", "hey", "hi", "hello", "que tal", "qué tal", "saludos"];

    function isGreeting(text) {
      var t = text.toLowerCase().trim();
      return GREETINGS.some(function (g) { return t === g || t.indexOf(g) === 0; });
    }

    function waLink(message) {
      return "https://wa.me/" + number + "?text=" + encodeURIComponent(message);
    }

    function scrollToBottom() {
      body.scrollTop = body.scrollHeight;
    }

    function addMessage(text, who) {
      var div = document.createElement("div");
      div.className = "wa-msg " + who;
      div.textContent = text;
      body.appendChild(div);
      scrollToBottom();
    }

    function addContinueButton(message) {
      var a = document.createElement("a");
      a.className = "btn btn-primary btn-sm wa-cta";
      a.target = "_blank";
      a.rel = "noopener";
      a.href = waLink(message);
      a.textContent = "Continuar por WhatsApp →";
      body.appendChild(a);
      scrollToBottom();
    }

    function botReplyTo(userText) {
      if (isGreeting(userText)) {
        addMessage("¡Qué bueno saludarte! Para darte el mejor detalle sobre horarios y cupos, continúa la conversación directo por WhatsApp 👇", "bot");
      } else {
        addMessage("Gracias por escribir. Para responder eso con calma prefiero atenderte por WhatsApp — toca el botón y seguimos por ahí 👇", "bot");
      }
      addContinueButton(genericMsg);
    }

    function openPanel() {
      widget.classList.add("is-open");
      fab.setAttribute("aria-expanded", "true");
      // Idempotent: only inject the greeting if the HTML wasn't pre-populated with it.
      if (body && $$(".wa-msg", body).length === 0) {
        setTimeout(function () {
          addMessage("¡Hola! 👋 Soy el asistente virtual de NUTRICYT, ¿en qué te puedo ayudar?", "bot");
        }, 260);
      }
      setTimeout(function () { if (input) input.focus(); }, 350);
    }

    function closePanel() {
      widget.classList.remove("is-open");
      fab.setAttribute("aria-expanded", "false");
    }

    fab.addEventListener("click", function () {
      widget.classList.contains("is-open") ? closePanel() : openPanel();
    });

    if (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var text = (input.value || "").trim();
        if (!text) return;
        addMessage(text, "user");
        input.value = "";
        setTimeout(function () { botReplyTo(text); }, 420);
      });
    }
  }

  /* -----------------------------------------------------------
     Year in footer
     ----------------------------------------------------------- */
  function initFooterYear() {
    var el = $("[data-year]");
    if (el) el.textContent = new Date().getFullYear();
  }

  function boot() {
    safe(initNav, "initNav");
    safe(initSmoothAnchors, "initSmoothAnchors");
    safe(initReveals, "initReveals");
    safe(initHeroParallax, "initHeroParallax");
    safe(initContactForm, "initContactForm");
    safe(initWhatsAppWidget, "initWhatsAppWidget");
    safe(initFooterYear, "initFooterYear");
    document.documentElement.classList.add("is-ready");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
