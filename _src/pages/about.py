"""About — section 5.5 of the copy document (new page)."""


def render(c):
    t, n = c.t, c.n

    roles = [
        (t('Physicians', 'Medici'), t('carry out the medical assessment.', 'svolgono la valutazione clinica.')),
        (t('Drug safety officers', 'Drug safety officer'), t('manage cases and reports.', 'gestiscono casi e report.')),
        (t('Quality assurance', 'Quality assurance'), t('audits the system.', 'sottopone il sistema ad audit.')),
        (t('IT', 'IT'), t('keeps the databases validated and the data safe.', 'mantiene i database validati e i dati al sicuro.')),
    ]
    roles_html = "".join(f"""
        <div class="point reveal">
          <h3 class="point__title">{a}</h3>
          <p class="point__text">{b[0].upper() + b[1:]}</p>
        </div>""" for a, b in roles)

    figures = [
        (n.team, t('specialists', 'specialisti')),
        (f'{n.retention}%', t('with us for more than a year', 'con noi da oltre un anno')),
        (f'+{n.growth}%', t('team growth between 2024 and 2026', 'crescita del team tra 2024 e 2026')),
        (f'{n.client_years}+', t('years with our key clients', 'anni con i clienti principali')),
    ]
    fig_html = "".join(f"""
        <div class="stats-bar__item reveal">
          <span class="stats-bar__number{' accent' if i % 2 else ''}">{a}</span>
          <p class="stats-bar__label">{b}</p>
        </div>""" for i, (a, b) in enumerate(figures))

    body = c.page_header(
        t('About', 'Chi siamo'),
        t('A medical and scientific team, in pharmacovigilance since 2001', 'Un team medico-scientifico, nella farmacovigilanza dal 2001'),
        t(f'{n.word("team", cap=True)} specialists in Saronno, near Milan, working for marketing authorisation holders in Italy, Germany and Spain.',
          f'{n.word("team", cap=True)} specialisti a Saronno, vicino a Milano, al lavoro per titolari AIC in Italia, Germania e Spagna.'),
    ) + f"""

  <section class="section" id="history" aria-labelledby="history-title">
    <div class="container">
      <div class="split split--top">
        <div>
          <span class="section-label section-label--primary reveal">{t('2001–2026 · 25 years in pharmacovigilance', '2001–2026 · 25 anni di farmacovigilanza')}</span>
          <h2 class="reveal reveal-delay-1" id="history-title">{t('Where we come from', 'Da dove veniamo')}</h2>
          <div class="section-divider reveal reveal-delay-2"></div>
        </div>
        <div class="reveal reveal-delay-2">
          <p>{t(
              f'MAC was founded in 2001 by Dr Stefano Franchini, a physician specialised in sports medicine, formerly a medical executive at IRCCS Don Gnocchi and Drug Safety Unit Manager at Zambon Group.',
              f'MAC è stata fondata nel 2001 dal Dr. Stefano Franchini, medico specialista in medicina dello sport, già dirigente medico all\'IRCCS Don Gnocchi e Drug Safety Unit Manager in Zambon Group.')}</p>
          <p>{t(
              'The idea was simple: give pharmaceutical companies an outsourcing partner with the same scientific discipline they expect of themselves. The company has grown steadily since then, and our key clients have been with us for more than ten years.',
              'L\'idea era semplice: offrire alle aziende farmaceutiche un partner di outsourcing con lo stesso rigore scientifico che chiedono a sé stesse. Da allora l\'azienda è cresciuta con continuità, e i clienti principali sono con noi da oltre dieci anni.')}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--bg" id="team" aria-labelledby="team-title">
    <div class="container">
      <span class="section-label section-label--primary reveal">{t('People', 'Persone')}</span>
      <h2 class="reveal reveal-delay-1" id="team-title">{t('The team', 'Il team')}</h2>
      <div class="section-divider reveal reveal-delay-2"></div>
      <p class="lead reveal reveal-delay-2">{t(
          'Physicians, pharmacists, biologists, quality managers and IT specialists work on the same cases from different angles.',
          'Medici, farmacisti, biologi, quality manager e specialisti IT lavorano sugli stessi casi da prospettive diverse.')}</p>
      <div class="point-grid point-grid--4">{roles_html}
      </div>
      <div class="stats-bar__grid stats-bar__grid--inline">{fig_html}
      </div>
    </div>
  </section>

  <section class="section" id="key-roles" aria-labelledby="roles-title">
    <div class="container">
      <span class="section-label section-label--primary reveal">{t('Accountability', 'Responsabilità')}</span>
      <h2 class="reveal reveal-delay-1" id="roles-title">{t('Key roles', 'Ruoli chiave')}</h2>
      <div class="section-divider reveal reveal-delay-2"></div>
      <div class="point-grid point-grid--2">
        <div class="point point--draft reveal">
          <h3 class="point__title">EU-QPPV</h3>
          <p class="point__text">{t('Qualifications, years in pharmacovigilance, responsibilities.', 'Titoli, anni di esperienza in farmacovigilanza, responsabilità.')}</p>
          <p class="point__text">{c.draft('profilo dell EU-QPPV: testo da fornire; pubblicare il nome?')}</p>
        </div>
        <div class="point point--draft reveal">
          <h3 class="point__title">{t('Head of Quality Assurance', 'Responsabile Quality Assurance')}</h3>
          <p class="point__text">{t('Qualifications, years in pharmacovigilance, responsibilities.', 'Titoli, anni di esperienza in farmacovigilanza, responsabilità.')}</p>
          <p class="point__text">{c.draft('profilo del responsabile QA: testo da fornire; pubblicare il nome?')}</p>
        </div>
      </div>
    </div>
  </section>
{c.cta(t('Want to meet the people who would run your system?', 'Volete conoscere le persone che gestirebbero il vostro sistema?'),
       t('Arrange a call', 'Fissiamo una call'))}"""

    return {
        "title": t("A pharmacovigilance team in Italy since 2001 · MAC", "Un team di farmacovigilanza in Italia dal 2001 · MAC"),
        "desc": t(f"MAC is a medical and scientific team of {n.team} specialists in Saronno, near Milan, working in pharmacovigilance and Medical Affairs since 2001.",
                  f"MAC è un team medico-scientifico di {n.team} specialisti a Saronno, vicino a Milano, attivo nella farmacovigilanza e nel Medical Affairs dal 2001."),
        "body": body,
    }
