"""Services — section 5.3 of the copy document."""


def render(c):
    t, n, I = c.t, c.n, c.icon

    modules = [
        (t('EU-QPPV and PSMF', 'EU-QPPV e PSMF'),
         t('Qualified person responsible for pharmacovigilance (EU-QPPV) and deputy; writing and maintenance of the pharmacovigilance system master file (PSMF).',
           'Persona qualificata e deputy, redazione e manutenzione del PSMF.')),
        (t('Case management', 'Gestione dei casi'),
         t('Individual case safety reports (ICSRs) from intake to EudraVigilance submission, in SafetyDrugs® or ARISg™, E2B(R3). Submission to EMA and MHRA.',
           'ICSR dalla ricezione alla trasmissione a EudraVigilance, in SafetyDrugs® o ARISg™, E2B(R3). Trasmissione a EMA e MHRA.')),
        (t('Medical assessment', 'Valutazione medica'),
         t('Seriousness, causality and expectedness assessed by a drug safety physician.',
           'Gravità, nesso di causalità e prevedibilità valutati da un medico di drug safety.')),
        (t('Literature monitoring', 'Monitoraggio della letteratura'),
         t('Weekly searches in PubMed and Embase, MLM screening, case identification.',
           'Ricerche settimanali su PubMed ed Embase, screening MLM, identificazione dei casi.')),
        (t('Aggregate reports', 'Report aggregati'),
         t('PSURs in PBRER format, risk management plans, addenda to clinical overviews.',
           'PSUR in formato PBRER, piani di gestione del rischio, addendum to clinical overview.')),
        (t('Signal management', 'Signal management'),
         t('Detection in EVDAS, validation, assessment and documentation.',
           'Rilevazione su EVDAS, validazione, valutazione e documentazione.')),
        (t('Clinical trial safety', 'Sicurezza nelle sperimentazioni'),
         t('For sponsors: management of suspected unexpected serious adverse reactions (SUSARs) and submission within 7 or 15 days.',
           'Per gli sponsor: gestione delle SUSAR e trasmissione entro 7 o 15 giorni.')),
        (t('Product data', 'Dati di prodotto'),
         t('XEVMPD maintenance and transition to PMS.', 'Manutenzione XEVMPD e transizione a PMS.')),
        (t('Safety variations and authority requests', 'Variazioni di sicurezza e richieste delle autorità'),
         t('SmPC and package leaflet updates; replies to EMA and AIFA.',
           'Aggiornamenti di RCP e foglio illustrativo; risposte a EMA e AIFA.')),
        (t('Audits and gap assessments', 'Audit e gap assessment'),
         t('Audits of your pharmacovigilance system and of your vendors; alignment of subcontracts with Regulation (EU) 2025/1466.',
           'Audit del vostro sistema di farmacovigilanza e dei vostri fornitori; adeguamento dei contratti di subappalto al Reg. (UE) 2025/1466.')),
    ]
    mod_html = "".join(f"""
        <article class="module reveal">
          <span class="module__num">{i:02d}</span>
          <h3 class="module__title">{a}</h3>
          <p class="module__text">{b}</p>
        </article>""" for i, (a, b) in enumerate(modules, 1))

    ma = [
        (t('Scientific service', 'Servizio scientifico'),
         t('Support to the person responsible for the scientific service under Article 126 of Legislative Decree 219/2006.',
           'Supporto al responsabile del servizio scientifico ai sensi dell\'art. 126 del D.Lgs. 219/2006.')),
        (t('Medical information', 'Informazione medica'),
         t('Documented, referenced answers to enquiries from healthcare professionals and patients. Any adverse reaction mentioned in an enquiry goes straight to pharmacovigilance.',
           'Risposte documentate e referenziate alle richieste di operatori sanitari e pazienti. Ogni reazione avversa citata in una richiesta passa subito alla farmacovigilanza.')),
        (t('Review of promotional materials', 'Revisione dei materiali promozionali'),
         t('Scientific review and regulatory conformity of materials for healthcare professionals (Articles 113–120 of Legislative Decree 219/2006).',
           'Revisione scientifica e conformità normativa dei materiali per gli operatori sanitari (artt. 113–120 D.Lgs. 219/2006).')),
        (t('Training', 'Formazione'),
         t('For medical and field teams: product, guidelines, and how to recognise and report an adverse reaction.',
           'Per i team medici e di campo: prodotto, linee guida, come riconoscere e segnalare una reazione avversa.')),
    ]
    ma_html = "".join(f"""
        <article class="module module--light reveal">
          <h3 class="module__title">{a}</h3>
          <p class="module__text">{b}</p>
        </article>""" for a, b in ma)
    ma_html += f"""
        <article class="module module--light module--draft reveal">
          <h3 class="module__title">{t('Scientific exchange with experts', 'Scientific exchange con gli esperti')}</h3>
          <p class="module__text">{c.draft('servizio attivo? In caso contrario il riquadro va tolto')}</p>
        </article>
        <article class="module module--light module--draft reveal">
          <h3 class="module__title">{t('Clinical research support', 'Supporto alla ricerca clinica')}</h3>
          <p class="module__text">{c.draft('servizio attivo? (supporto alla ricerca clinica)')}</p>
        </article>"""

    steps = c.steps([
        (t('Scope', 'Perimetro'), t('Products, countries, volumes, deadlines.', 'Prodotti, paesi, volumi, scadenze.')),
        (t('Proposal', 'Proposta'), t('Modules, responsibilities, indicators.', 'Moduli, responsabilità, indicatori.')),
        (t('Agreements', 'Accordi'), t('Contract, SDEA, data protection terms.', 'Contratto, SDEA, clausole di protezione dei dati.')),
        (t('Start', 'Avvio'), t('A documented plan with agreed dates.', 'Un piano documentato con date concordate.')),
    ])

    body = c.page_header(
        t('Services', 'Servizi'),
        t('Take the whole system, or one module', 'L\'intero sistema, o un solo modulo'),
        t('Each pharmacovigilance module below can be contracted on its own and connects to your existing system. Medical Affairs services are available alongside or separately.',
          'Ogni modulo di farmacovigilanza può essere affidato singolarmente e si collega al vostro sistema esistente. I servizi di Medical Affairs sono disponibili insieme o separatamente.'),
    ) + f"""

  <nav class="anchor-nav" aria-label="{t('On this page', 'In questa pagina')}">
    <div class="container">
      <a href="#pv-modules">{t('Pharmacovigilance modules', 'Moduli di farmacovigilanza')}</a>
      <a href="#medical-affairs">Medical Affairs</a>
      <a href="#start">{t('How we start', 'Come iniziamo')}</a>
    </div>
  </nav>

  <section class="section" id="pv-modules" aria-labelledby="pv-modules-title">
    <div class="container">
      <span class="section-label section-label--primary reveal">{t('Pharmacovigilance', 'Farmacovigilanza')}</span>
      <h2 class="reveal reveal-delay-1" id="pv-modules-title">{t('Pharmacovigilance modules', 'Moduli di farmacovigilanza')}</h2>
      <div class="section-divider reveal reveal-delay-2"></div>

      <a class="full-system reveal" href="{c.url('pv')}">
        <div>
          <strong>{t('The full system', 'Il sistema completo')}</strong>
          <span>{t(f'All the modules below as one pharmacovigilance system, as we run it today for {n.word("full_systems")} marketing authorisation holders (MAHs).',
                   f'Tutti i moduli qui sotto come un unico sistema di farmacovigilanza, come lo gestiamo oggi per {n.word("full_systems")} titolari AIC.')}</span>
        </div>
        <span class="full-system__link">{t('The PV System', 'Il sistema PV')} {I['arrow']}</span>
      </a>

      <div class="module-grid">{mod_html}
      </div>
    </div>
  </section>

  <section class="section section--primary" id="medical-affairs" aria-labelledby="ma-title">
    <div class="container">
      <div class="split">
        <div>
          <span class="section-label section-label--primary reveal">Medical Affairs</span>
          <h2 class="reveal reveal-delay-1" id="ma-title">{t('Medical Affairs: scientific support that stands apart from promotion', 'Medical Affairs: supporto scientifico distinto dalla promozione')}</h2>
          <div class="section-divider reveal reveal-delay-2"></div>
        </div>
        <p class="lead lead--on-dark reveal reveal-delay-2">{t(
            'Italian law requires every marketing authorisation holder to run a scientific service that is independent of marketing. We run it with you, or for you, and keep every answer traceable.',
            'La normativa italiana richiede a ogni titolare AIC un servizio scientifico indipendente dal marketing. Lo gestiamo con voi, o per voi, e ogni risposta resta tracciabile.')}</p>
      </div>
      <div class="module-grid module-grid--2">{ma_html}
      </div>
    </div>
  </section>

  <section class="section" id="start" aria-labelledby="start-title">
    <div class="container">
      <span class="section-label section-label--primary reveal">{t('Working together', 'Lavorare insieme')}</span>
      <h2 class="reveal reveal-delay-1" id="start-title">{t('How we start', 'Come iniziamo')}</h2>
      <div class="section-divider reveal reveal-delay-2"></div>
      {steps}
    </div>
  </section>
{c.cta(t('Not sure which modules you need?', 'Non sapete quali moduli vi servono?'),
       t('Ask about a module', 'Chiedete di un modulo'),
       t('Tell us what you have in place today.', 'Diteci cosa avete oggi.'))}"""

    return {
        "title": t("Pharmacovigilance modules and Medical Affairs services · MAC",
                   "Moduli di farmacovigilanza e servizi di Medical Affairs · MAC"),
        "desc": t("Pharmacovigilance modules you can contract one by one — EU-QPPV and PSMF, case management, literature, aggregate reports, signals, audits — and Medical Affairs services.",
                  "Moduli di farmacovigilanza affidabili singolarmente — EU-QPPV e PSMF, gestione dei casi, letteratura, report aggregati, segnali, audit — e servizi di Medical Affairs."),
        "body": body,
    }
