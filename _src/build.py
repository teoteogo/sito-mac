#!/usr/bin/env python3
"""Static site generator for the MAC website.

    python3 _src/build.py            # build all pages (drafts allowed, flagged on the page)
    python3 _src/build.py --release  # fail if any draft marker is left

English is the reference language and lives at the site root; Italian lives under /it/.
Every page is written once in _src/pages/<name>.py with both languages side by side,
so menu, footer, figures (data/numeri.json) and draft markers come from one source.
Generated HTML is committed: GitHub Pages serves the repository as it is.
"""
import datetime
import html
import importlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_src"
sys.path.insert(0, str(SRC))

BASE = "https://www.med-af-consulting.com/"
EMAIL = "contactus@med-af-consulting.it"
LINKEDIN = "https://www.linkedin.com/company/med-af-consulting"
INSTAGRAM = "https://www.instagram.com/medafconsulting/"

# page key -> file name per language (EN at the root, IT under it/)
FILES = {
    "home": {"en": "index.html", "it": "index.html"},
    "pv": {"en": "pv-system.html", "it": "sistema-pv.html"},
    "services": {"en": "services.html", "it": "servizi.html"},
    "quality": {"en": "quality.html", "it": "qualita.html"},
    "about": {"en": "about.html", "it": "chi-siamo.html"},
    "insights": {"en": "insights.html", "it": "approfondimenti.html"},
    "contact": {"en": "contact.html", "it": "contatti.html"},
    "faq": {"en": "faq.html", "it": "faq.html"},
    "careers": {"en": "careers.html", "it": "lavora-con-noi.html"},
    "privacy": {"en": "privacy.html", "it": "privacy.html"},
    "privacy-clients": {"en": "privacy-clients-suppliers.html", "it": "privacy-clienti-fornitori.html"},
    "privacy-candidates": {"en": "privacy-candidates.html", "it": "privacy-candidati.html"},
    "cookie": {"en": "cookie.html", "it": "cookie.html"},
}
LEGAL = ["privacy", "privacy-clients", "privacy-candidates", "cookie"]
CONTENT_PAGES = ["home", "pv", "services", "quality", "about", "insights", "contact", "faq", "careers"]

MENU = [  # key, EN label, IT label
    ("home", "Home", "Home"),
    ("pv", "The PV System", "Il sistema PV"),
    ("services", "Services", "Servizi"),
    ("quality", "Quality &amp; Data", "Qualità e dati"),
    ("about", "About", "Chi siamo"),
    ("insights", "Insights", "Approfondimenti"),
]

# Old URLs (before EN moved to the root) -> new location, as small redirect pages.
REDIRECTS = {
    "servizi.html": "it/servizi.html",
    "qualita.html": "it/qualita.html",
    "contatti.html": "it/contatti.html",
    "blog.html": "it/approfondimenti.html",
    "lavora-con-noi.html": "it/lavora-con-noi.html",
    "calendario.html": "it/",
    "privacy-candidati.html": "it/privacy-candidati.html",
    "privacy-clienti-fornitori.html": "it/privacy-clienti-fornitori.html",
    "en/index.html": "",
    "en/services.html": "services.html",
    "en/quality.html": "quality.html",
    "en/contact.html": "contact.html",
    "en/faq.html": "faq.html",
    "en/careers.html": "careers.html",
    "en/blog.html": "insights.html",
    "en/events.html": "",
    "en/privacy.html": "privacy.html",
    "en/privacy-candidati.html": "privacy-candidates.html",
    "en/privacy-clienti-fornitori.html": "privacy-clients-suppliers.html",
    "en/cookie.html": "cookie.html",
}

ICON = {
    "arrow": '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>',
    "mail": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>',
    "pin": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>',
    "linkedin": '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>',
    "instagram": '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>',
    "plus": '<svg class="accordion__icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>',
    "check": '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    "activity": '<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>',
    "book": '<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>',
    "chat": '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>',
    "stethoscope": '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3v6a4 4 0 0 0 8 0V3"></path><path d="M10 13v3a5 5 0 0 0 10 0v-2"></path><circle cx="20" cy="12" r="2"></circle></svg>',
    "shield": '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>',
    "clipboard": '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="4" width="14" height="17" rx="2"></rect><path d="M9 4V3h6v1"></path><polyline points="9 13 11 15 15 11"></polyline></svg>',
}

WORDS = {
    "en": {3: "three", 27: "twenty-seven"},
    "it": {3: "tre", 27: "ventisette"},
}


class Figures:
    """Single source for every number on the site (data/numeri.json)."""

    def __init__(self, lang):
        self.lang = lang
        self.d = json.loads((ROOT / "data" / "numeri.json").read_text(encoding="utf-8"))

    def __getattr__(self, name):
        if name not in self.d:
            raise AttributeError(name)
        v = self.d[name]
        if isinstance(v, int) and v >= 10000:
            s = f"{v:,}"
            return s if self.lang == "en" else s.replace(",", ".")
        return str(v)

    def word(self, name, cap=False):
        w = WORDS[self.lang].get(self.d[name], str(self.d[name]))
        return w.capitalize() if cap else w


class Ctx:
    def __init__(self, lang, key):
        self.lang = lang
        self.key = key
        self.a = "" if lang == "en" else "../"  # prefix for shared assets
        self.n = Figures(lang)
        self.drafts = []  # (scope, note)
        self.icon = ICON

    def t(self, en, it):
        return en if self.lang == "en" else it

    def url(self, key, anchor=""):
        return FILES[key][self.lang] + (f"#{anchor}" if anchor else "")

    def alt(self, key=None):
        """Relative link to the same page in the other language."""
        key = key or self.key
        if self.lang == "en":
            return "it/" + FILES[key]["it"]
        return "../" + FILES[key]["en"]

    def abs(self, key=None, lang=None):
        key = key or self.key
        lang = lang or self.lang
        f = FILES[key][lang]
        return BASE + ("" if lang == "en" else "it/") + ("" if f == "index.html" else f)

    def draft(self, note, scope="page"):
        """Inline marker for text that must be confirmed before publication."""
        if (scope, note) not in self.drafts:  # t(en, it) evaluates both branches
            self.drafts.append((scope, note))
        return (f'<span class="draft"><span class="draft__tag">Bozza</span> '
                f'da confermare: {html.escape(note)}</span>')

    # ---- shared components -------------------------------------------------
    def page_header(self, label, h1, sub, bg=None):
        style = ""
        if bg:
            style = (' style="background: linear-gradient(135deg, rgba(13,46,85,.82) 0%, rgba(26,80,116,.74) 60%, '
                     f"rgba(38,112,158,.66) 100%), url('{self.a}img/{bg}') center/cover no-repeat;\"")
        return f"""
  <section class="page-header"{style}>
    <div class="container">
      <span class="section-label section-label--primary reveal">{label}</span>
      <h1 class="reveal reveal-delay-1">{h1}</h1>
      <p class="reveal reveal-delay-2">{sub}</p>
    </div>
  </section>"""

    def cta(self, h2, btn, text="", href=None, label=None):
        href = href or self.url("contact")
        lab = f'<span class="section-label reveal">{label}</span>' if label else ""
        txt = f'<p class="reveal reveal-delay-2">{text}</p>' if text else ""
        return f"""
  <section class="cta-banner" aria-labelledby="cta-title">
    <div class="container">
      <div class="cta-banner__inner">
        {lab}
        <h2 class="reveal reveal-delay-1" id="cta-title">{h2}</h2>
        {txt}
        <div class="cta-banner__actions reveal reveal-delay-3">
          <a href="{href}" class="btn btn--white btn--lg">{btn} {ICON['arrow']}</a>
        </div>
      </div>
    </div>
  </section>"""

    def steps(self, items):
        out = ['<div class="how-steps">']
        for i, (title, desc) in enumerate(items, 1):
            out.append(f"""
        <div class="how-step reveal reveal-delay-{i - 1}">
          <div class="how-step__num">{i}</div>
          <h3 class="how-step__title">{title}</h3>
          <p class="how-step__desc">{desc}</p>
        </div>""")
        out.append("</div>")
        return "".join(out)


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
def head(c, page):
    t = c.t
    robots = page.get("robots")
    og_title = page.get("og_title", page["title"])
    links = [
        f'<link rel="canonical" href="{c.abs()}">',
        f'<link rel="alternate" hreflang="en" href="{c.abs(lang="en")}">',
        f'<link rel="alternate" hreflang="it" href="{c.abs(lang="it")}">',
        f'<link rel="alternate" hreflang="x-default" href="{c.abs(lang="en")}">',
    ]
    jsonld = ""
    if page.get("jsonld"):
        jsonld = ('\n  <script type="application/ld+json">'
                  + json.dumps(page["jsonld"], ensure_ascii=False) + "</script>")
    return f"""<!DOCTYPE html>
<html lang="{c.lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page['title']}</title>
  <meta name="description" content="{page['desc']}">{f'''
  <meta name="robots" content="{robots}">''' if robots else ''}
  {chr(10).join('  ' + l for l in links).strip()}

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Medical Affairs Consulting">
  <meta property="og:locale" content="{t('en_GB', 'it_IT')}">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{page['desc']}">
  <meta property="og:url" content="{c.abs()}">
  <meta property="og:image" content="{BASE}img/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">

  <link rel="icon" type="image/x-icon" href="{c.a}img/icona_MAC.ico">
  <link rel="stylesheet" href="{c.a}css/fonts.css">
  <link rel="stylesheet" href="{c.a}css/style.css">
  <link rel="stylesheet" href="{c.a}css/animations.css">
  <link rel="stylesheet" href="{c.a}css/pages.css">{jsonld}
  <!-- Avacy Cookie Consent -->
  <script id='oil-configuration' type='application/configuration' data-remote-config='https://mac.avacy-cdn.com/config/mac/65ab896f-76fb-4433-afff-9be727943f87/banner.json'></script>
  <script src='https://mac.avacy-cdn.com/current/dist/oilstub.min.js'></script>
  <script src='https://mac.avacy-cdn.com/current/dist/oil.min.js'></script>
</head>
<body>

<a class="skip-link" href="#main">{t('Skip to content', 'Vai al contenuto')}</a>
<div class="scroll-progress" aria-hidden="true"></div>
"""


def navbar(c):
    t = c.t
    items, mobile = [], []
    for key, en, it in MENU:
        cur = ' class="active" aria-current="page"' if key == c.key else ""
        items.append(f'        <li><a href="{c.url(key)}"{cur}>{t(en, it)}</a></li>')
        mobile.append(f'    <a href="{c.url(key)}"{cur}>{t(en, it)}</a>')
    en_href = c.url(c.key) if c.lang == "en" else c.alt()
    it_href = c.url(c.key) if c.lang == "it" else c.alt()
    en_cls = ' class="active" aria-current="true"' if c.lang == "en" else ""
    it_cls = ' class="active" aria-current="true"' if c.lang == "it" else ""
    lang = (f'<a href="{en_href}" lang="en" hreflang="en"{en_cls}>EN</a>'
            f'<span aria-hidden="true">|</span>'
            f'<a href="{it_href}" lang="it" hreflang="it"{it_cls}>IT</a>')
    contact = t("Contact us", "Contattateci")
    return f"""<header>
  <nav class="navbar" aria-label="{t('Main navigation', 'Navigazione principale')}">
    <div class="navbar__inner">
      <a href="{c.url('home')}" class="navbar__logo" aria-label="Medical Affairs Consulting — Home">
        <img src="{c.a}img/mac-logo.png" alt="MAC — Medical Affairs Consulting" width="180" height="44">
      </a>

      <ul class="navbar__menu" role="list">
{chr(10).join(items)}
      </ul>

      <div class="navbar__actions">
        <div class="lang-switcher" aria-label="{t('Select language', 'Seleziona la lingua')}">{lang}</div>
        <a href="{c.url('contact')}" class="btn btn--primary">{contact}</a>
      </div>

      <button class="navbar__hamburger" aria-label="{t('Open menu', 'Apri il menu')}" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>

  <div class="navbar__mobile" aria-label="{t('Mobile menu', 'Menu mobile')}">
{chr(10).join(mobile)}
    <div class="lang-switcher mt-4">{lang}</div>
    <a href="{c.url('contact')}" class="btn btn--primary">{contact}</a>
  </div>
</header>
"""


def footer(c):
    t = c.t
    d = lambda note: c.draft(note, scope="footer")
    legal_en = (f"Medical Affairs Consulting S.r.l. · Corso Italia 39, 21047 Saronno (VA), Italy · VAT IT04027560129 · "
                f"REA VA-{d('numero REA')} · Share capital €{d('capitale sociale versato')} fully paid up")
    legal_it = (f"Medical Affairs Consulting S.r.l. · Corso Italia 39, 21047 Saronno (VA) · P.IVA 04027560129 · "
                f"REA VA-{d('numero REA')} · Cap. soc. €{d('capitale sociale versato')} i.v.")
    return f"""
<footer class="footer" aria-labelledby="footer-heading">
  <h2 id="footer-heading" class="sr-only">Footer</h2>
  <div class="container">
    <div class="footer__top">
      <div class="footer__brand">
        <a href="{c.url('home')}" aria-label="Medical Affairs Consulting — Home">
          <img src="{c.a}img/mac-logo.png" alt="MAC — Medical Affairs Consulting" width="160" height="38" style="filter:brightness(0) invert(1)" loading="lazy">
        </a>
        <p>{t('Pharmacovigilance and Medical Affairs for marketing authorisation holders. Since 2001.',
              'Farmacovigilanza e Medical Affairs per i titolari AIC. Dal 2001.')}</p>
        <p class="footer__anniv">{t('2001–2026 · 25 years in pharmacovigilance', '2001–2026 · 25 anni di farmacovigilanza')}</p>
        <div class="footer__social">
          <a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{ICON['linkedin']}</a>
          <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{ICON['instagram']}</a>
        </div>
      </div>

      <div class="footer__col">
        <h3 class="footer__title">{t('What we do', 'Cosa facciamo')}</h3>
        <nav class="footer__links" aria-label="{t('Service links', 'Link ai servizi')}">
          <a href="{c.url('pv')}">{t('The PV System', 'Il sistema PV')}</a>
          <a href="{c.url('services', 'pv-modules')}">{t('Pharmacovigilance modules', 'Moduli di farmacovigilanza')}</a>
          <a href="{c.url('services', 'medical-affairs')}">Medical Affairs</a>
          <a href="{c.url('quality')}">{t('Quality &amp; Data', 'Qualità e dati')}</a>
        </nav>
      </div>

      <div class="footer__col">
        <h3 class="footer__title">{t('Company', 'Azienda')}</h3>
        <nav class="footer__links" aria-label="{t('Company links', 'Link aziendali')}">
          <a href="{c.url('about')}">{t('About', 'Chi siamo')}</a>
          <a href="{c.url('insights')}">{t('Insights', 'Approfondimenti')}</a>
          <a href="{c.url('faq')}">FAQ</a>
          <a href="{c.url('careers')}">{t('Careers', 'Lavora con noi')}</a>
          <a href="{c.url('contact')}">{t('Contact', 'Contatti')}</a>
        </nav>
      </div>

      <div class="footer__col">
        <h3 class="footer__title">{t('Contact', 'Contatti')}</h3>
        <address style="font-style:normal;">
          <div class="footer__contact-item">{ICON['mail']}<a href="mailto:{EMAIL}">{EMAIL}</a></div>
          <div class="footer__contact-item">{ICON['pin']}<span>Corso Italia 39, 21047 Saronno (VA){t(', Italy', '')}</span></div>
        </address>
      </div>
    </div>

    <p class="footer__legal">{t(legal_en, legal_it)}</p>

    <div class="footer__bottom">
      <p>© 2026 Medical Affairs Consulting S.r.l.</p>
      <nav class="footer__bottom-links" aria-label="{t('Legal links', 'Link legali')}">
        <a href="{c.url('privacy')}">{t('Privacy notice', 'Informativa privacy')}</a>
        <a href="{c.url('privacy-clients')}">{t('Privacy for clients and suppliers', 'Privacy clienti e fornitori')}</a>
        <a href="{c.url('privacy-candidates')}">{t('Privacy for candidates', 'Privacy candidati')}</a>
        <a href="{c.url('cookie')}">{t('Cookies', 'Cookie')}</a>
        <a href="#" onclick="if(window.AS_OIL){{AS_OIL.showPreferenceCenter();}}return false;">{t('Cookie preferences', 'Preferenze cookie')}</a>
      </nav>
    </div>
  </div>
</footer>
"""


def render_page(c, page):
    body = page["body"]
    foot = footer(c)
    page_drafts = [n for s, n in c.drafts if s == "page"]
    ribbon = ""
    if page_drafts:
        ribbon = (f'\n<div class="draft-ribbon" role="note"><strong>Bozza di lavoro</strong> · '
                  f'{len(page_drafts)} {"punto" if len(page_drafts) == 1 else "punti"} da confermare in questa pagina</div>')
    scripts = "".join(f'\n<script src="{c.a}{s}"></script>' for s in ["js/main.js"] + page.get("scripts", []))
    return (head(c, page) + navbar(c) + f'\n<main id="main">{body}\n</main>\n' + foot
            + ribbon + scripts + "\n</body>\n</html>\n")


# ---------------------------------------------------------------------------
# Legal pages: bodies kept as approved, only wrapped in the shared layout
# ---------------------------------------------------------------------------
LEGAL_META = {
    "privacy": ("Privacy notice · MAC", "Informativa privacy · MAC"),
    "privacy-clients": ("Privacy notice for clients and suppliers · MAC", "Informativa privacy clienti e fornitori · MAC"),
    "privacy-candidates": ("Privacy notice for candidates · MAC", "Informativa privacy candidati · MAC"),
    "cookie": ("Cookie policy · MAC", "Cookie policy · MAC"),
}
LEGAL_DESC = {
    "privacy": ("Privacy notice of Medical Affairs Consulting S.r.l. pursuant to Article 13 GDPR.",
                "Informativa sul trattamento dei dati personali ai sensi del Regolamento UE 2016/679 (GDPR)."),
    "privacy-clients": ("Privacy notice of Medical Affairs Consulting S.r.l. for clients and suppliers, pursuant to Article 13 GDPR.",
                        "Informativa sul trattamento dei dati personali di clienti e fornitori ai sensi dell'art. 13 del Regolamento UE 2016/679 (GDPR)."),
    "privacy-candidates": ("Recruitment privacy notice of Medical Affairs Consulting S.r.l. for candidates, pursuant to Article 13 GDPR.",
                           "Informativa sul trattamento dei dati personali dei candidati ai sensi dell'art. 13 del Regolamento UE 2016/679 (GDPR)."),
    "cookie": ("Information on the use of cookies and similar technologies on med-af-consulting.com.",
               "Informativa sull'uso dei cookie e di tecnologie simili sul sito med-af-consulting.com."),
}


def legal_page(c):
    body = (SRC / "legal" / c.lang / f"{c.key}.html").read_text(encoding="utf-8")
    body = body.replace("@@alt@@", c.alt())
    body = re.sub(r"@@([a-z-]+)@@", lambda m: c.url(m.group(1)), body)
    i = 0 if c.lang == "en" else 1
    return {"title": LEGAL_META[c.key][i], "desc": LEGAL_DESC[c.key][i],
            "robots": "noindex, follow", "body": "\n  " + body.strip()}


def redirect_page(old, new):
    depth = old.count("/")
    rel = "../" * depth + (new or "index.html")
    if new.endswith("/"):
        rel = "../" * depth + new + "index.html"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Page moved · Medical Affairs Consulting</title>
  <meta name="robots" content="noindex">
  <link rel="canonical" href="{BASE}{new}">
  <meta http-equiv="refresh" content="0; url={rel}">
</head>
<body>
  <p>This page has moved. La pagina è stata spostata. <a href="{rel}">{BASE}{new}</a></p>
</body>
</html>
"""


def page_404():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex">
  <title>Page not found · MAC</title>
  <link rel="icon" type="image/x-icon" href="/img/icona_MAC.ico">
  <link rel="stylesheet" href="/css/fonts.css">
  <link rel="stylesheet" href="/css/style.css">
</head>
<body>
  <main style="min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:2rem;">
    <div style="max-width:560px;">
      <a href="/" aria-label="Medical Affairs Consulting — Home">
        <img src="/img/mac-logo.png" alt="MAC — Medical Affairs Consulting" width="180" height="44" style="margin:0 auto 2rem;">
      </a>
      <h1>404</h1>
      <p style="margin:1rem auto 0;">The page you are looking for does not exist or has been moved.</p>
      <p style="margin:.5rem auto 2rem;" lang="it">La pagina che cercate non esiste o è stata spostata.</p>
      <a href="/" class="btn btn--primary">Back to home</a>
      <a href="/it/" class="btn btn--outline" style="margin-left:.5rem;" lang="it">Torna alla home</a>
    </div>
  </main>
</body>
</html>
"""


def sitemap():
    today = datetime.date.today().isoformat()
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for key in CONTENT_PAGES:
        en, it = Ctx("en", key).abs(), Ctx("it", key).abs()
        for loc in (en, it):
            out += ["  <url>", f"    <loc>{loc}</loc>", f"    <lastmod>{today}</lastmod>",
                    f'    <xhtml:link rel="alternate" hreflang="en" href="{en}"/>',
                    f'    <xhtml:link rel="alternate" hreflang="it" href="{it}"/>',
                    f'    <xhtml:link rel="alternate" hreflang="x-default" href="{en}"/>',
                    "  </url>"]
    out.append("</urlset>")
    return "\n".join(out) + "\n"


def drafts_report(report, footer_notes):
    labels = dict((k, it.replace("&amp;", "&")) for k, _, it in MENU)
    labels.update(contact="Contatti", faq="FAQ", careers="Lavora con noi")
    out = ["# Bozze da confermare",
           "",
           "File generato da `_src/build.py`: non modificarlo a mano. Elenca ogni blocco pubblicato come",
           "**bozza** (marcatore giallo nelle pagine). I marcatori sono identici in inglese e in italiano.",
           "Quando un dato è confermato, si toglie il `c.draft(...)` corrispondente in `_src/pages/` e si",
           "rilancia il build. `python3 _src/build.py --release` fallisce finché resta anche una sola bozza.",
           "",
           "## Tutte le pagine (footer)", ""]
    out += [f"- [ ] {n}" for n in footer_notes]
    for key, notes in report:
        if notes:
            out += ["", f"## {labels[key]} (`{FILES[key]['en']}` · `it/{FILES[key]['it']}`)", ""]
            out += [f"- [ ] {n}" for n in notes]
    out += ["", "## Numeri", "",
            "- [ ] Tutti i valori di `data/numeri.json` vanno ricontrollati sulla company presentation 2026",
            "      (oggi sono quelli riportati dall'audit del 25 ottobre 2026).", ""]
    return "\n".join(out)


def main():
    release = "--release" in sys.argv
    report, footer_notes, total = [], [], 0
    for key in CONTENT_PAGES + LEGAL:
        notes_en = None
        for lang in ("en", "it"):
            c = Ctx(lang, key)
            if key in LEGAL:
                page = legal_page(c)
            else:
                page = importlib.import_module(f"pages.{key.replace('-', '_')}").render(c)
            out = render_page(c, page)
            dest = ROOT / ("" if lang == "en" else "it") / FILES[key][lang]
            dest.parent.mkdir(exist_ok=True)
            dest.write_text(out, encoding="utf-8")
            notes = [n for s, n in c.drafts if s == "page"]
            footer_notes = [n for s, n in c.drafts if s == "footer"]
            if lang == "en":
                notes_en = notes
            elif notes != notes_en:
                sys.exit(f"{key}: draft markers differ between EN and IT\n  EN: {notes_en}\n  IT: {notes}")
        report.append((key, notes_en))
        total += len(notes_en)
    for old, new in REDIRECTS.items():
        dest = ROOT / old
        dest.parent.mkdir(exist_ok=True)
        dest.write_text(redirect_page(old, new), encoding="utf-8")
    (ROOT / "404.html").write_text(page_404(), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    (ROOT / "BOZZE.md").write_text(drafts_report(report, footer_notes), encoding="utf-8")
    print(f"Built {len(CONTENT_PAGES + LEGAL) * 2} pages, {len(REDIRECTS)} redirects. "
          f"Drafts: {total} on pages + {len(footer_notes)} in the footer.")
    if release and (total or footer_notes):
        sys.exit("Release build refused: draft markers remain (see BOZZE.md).")


if __name__ == "__main__":
    main()
