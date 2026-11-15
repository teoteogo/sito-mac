"""Insights — the three real columns: PV Glossary, Regulatory Update, Quality."""
import build


def render(c):
    t, I = c.t, c.icon

    columns = [
        ('PV Glossary', t('One pharmacovigilance term at a time, explained in plain words.',
                          'Un termine di farmacovigilanza alla volta, spiegato in parole semplici.')),
        ('Regulatory Update', t('What changes in EU and Italian pharmacovigilance rules, and what it means in practice.',
                                'Cosa cambia nelle regole di farmacovigilanza europee e italiane, e cosa significa in pratica.')),
        ('Quality', t('Controls, method and quality in day-to-day pharmacovigilance work.',
                      'Controlli, metodo e qualità nel lavoro quotidiano di farmacovigilanza.')),
    ]
    cols = "".join(f"""
        <div class="point reveal">
          <h3 class="point__title">{a}</h3>
          <p class="point__text">{b}</p>
        </div>""" for a, b in columns)

    body = c.page_header(
        t('Insights', 'Approfondimenti'),
        t('Pharmacovigilance, explained and kept up to date', 'La farmacovigilanza, spiegata e aggiornata'),
        t('Three columns written by our team: PV Glossary, Regulatory Update and Quality.',
          'Tre rubriche scritte dal nostro team: PV Glossary, Regulatory Update e Quality.'),
    ) + f"""

  <section class="section" aria-labelledby="columns-title">
    <div class="container">
      <h2 class="sr-only" id="columns-title">{t('Columns', 'Rubriche')}</h2>
      <div class="point-grid point-grid--3">{cols}
      </div>
    </div>
  </section>

  <section class="section section--bg" aria-labelledby="posts-title">
    <div class="container">
      <span class="section-label section-label--primary reveal">{t('Latest', 'Ultimi articoli')}</span>
      <h2 class="reveal reveal-delay-1" id="posts-title">{t('Articles', 'Articoli')}</h2>
      <div class="section-divider reveal reveal-delay-2"></div>
      <div class="filters" role="group" aria-label="{t('Filter by column', 'Filtra per rubrica')}"></div>
      <div id="blog-container" class="grid-3"></div>
      <noscript><p>{t('Our articles are published on', 'I nostri articoli sono pubblicati su')} <a href="{build.LINKEDIN}">LinkedIn</a>.</p></noscript>
    </div>
  </section>
{c.cta(t('New articles appear first on LinkedIn.', 'I nuovi articoli escono prima su LinkedIn.'),
       t('Follow MAC on LinkedIn', 'Seguite MAC su LinkedIn'), href=build.LINKEDIN)}"""

    return {
        "title": t("Insights: PV Glossary, Regulatory Update, Quality · MAC",
                   "Approfondimenti: PV Glossary, Regulatory Update, Quality · MAC"),
        "desc": t("Articles by the MAC team on pharmacovigilance terms, regulatory changes and quality in drug safety.",
                  "Articoli del team MAC su termini di farmacovigilanza, novità normative e qualità nella drug safety."),
        "scripts": ["js/blog.js"],
        "body": body,
    }
