"""Home — section 5.1 of the copy document."""

TOOLS = ["SafetyDrugs®", "ARISg™", "EudraVigilance (EVWEB, EVDAS)", "XEVMPD", "MLM", "MedDRA", "WHODrug", "PubMed", "Embase"]


def render(c):
    t, n, I = c.t, c.n, c.icon

    ticker_items = "".join(
        f'<span class="tech-ticker__item">{x}</span><span class="tech-ticker__sep">·</span>' for x in TOOLS)

    body = f"""
  <!-- HERO -->
  <section class="hero" aria-labelledby="hero-title">
    <div class="hero__right" aria-hidden="true"></div>
    <div class="hero__inner">
      <div class="hero__content">
        <p class="hero__eyebrow">{t('Pharmacovigilance and Medical Affairs · since 2001',
                                    'Farmacovigilanza e Medical Affairs · dal 2001')}</p>
        <h1 class="hero__title" id="hero-title">{t(
            'Your pharmacovigilance system, <span class="text-primary">inspection-ready.</span>',
            'Il vostro sistema di farmacovigilanza, <span class="text-primary">pronto per l\'ispezione.</span>')}</h1>
        <p class="hero__subtitle">{t(
            'EU-QPPV, PSMF, validated safety database, case processing, aggregate reports and signal management: one GVP system, run from Italy by a medical and scientific team.',
            'EU-QPPV, PSMF, database di sicurezza validato, gestione dei casi, report aggregati e signal management: un unico sistema GVP, gestito dall\'Italia da un team medico-scientifico.')}</p>
        <p class="hero__subtitle hero__subtitle--solution">{t(
            f'Today we run pharmacovigilance for {n.mah} marketing authorisation holders and {n.sponsors} clinical trial sponsors: more than {n.cases} cases a year, and no PSUSA findings in the past {n.psusa_months} months.',
            f'Oggi gestiamo la farmacovigilanza di {n.mah} titolari AIC e {n.sponsors} sponsor di sperimentazioni: oltre {n.cases} casi l\'anno e nessun finding PSUSA negli ultimi {n.psusa_months} mesi.')}</p>
        <div class="hero__cta">
          <a href="{c.url('contact')}" class="btn btn--primary btn--lg">{t('Discuss your PV system', 'Parliamo del vostro sistema PV')} {I['arrow']}</a>
          <a href="{c.url('pv')}" class="btn btn--outline btn--lg">{t('See how the system works', 'Come funziona il sistema')}</a>
        </div>
      </div>
    </div>
  </section>

  <!-- FIGURES BAR -->
  <section class="stats-bar" aria-label="{t('Key figures', 'Numeri chiave')}">
    <div class="container">
      <div class="stats-bar__grid">
        <div class="stats-bar__item reveal">
          <span class="stats-bar__number">{n.mah}</span>
          <p class="stats-bar__label">{t('marketing authorisation holders in Italy, Germany and Spain', 'titolari AIC in Italia, Germania e Spagna')}</p>
        </div>
        <div class="stats-bar__item reveal reveal-delay-1">
          <span class="stats-bar__number accent">{n.top10}<span class="stats-bar__of">{t(' of the 10', ' dei primi 10')}</span></span>
          <p class="stats-bar__label">{t('largest Italian pharmaceutical groups', 'gruppi farmaceutici italiani')}</p>
        </div>
        <div class="stats-bar__item reveal reveal-delay-2">
          <span class="stats-bar__number">{n.cases}+</span>
          <p class="stats-bar__label">{t('cases a year', 'casi l\'anno')}</p>
        </div>
        <div class="stats-bar__item reveal reveal-delay-3">
          <span class="stats-bar__number accent">0</span>
          <p class="stats-bar__label">{t(f'PSUSA findings in {n.psusa_months} months', f'finding PSUSA in {n.psusa_months} mesi')}</p>
        </div>
      </div>
      <p class="stats-bar__note">{t(f'Figures for {n.year}.', f'Dati {n.year}.')} {c.draft('tutti i numeri del sito, da ricontrollare sulla company presentation 2026')}</p>
    </div>
  </section>

  <!-- TWO PILLARS -->
  <section class="section" id="pillars" aria-labelledby="pillars-title">
    <div class="container">
      <span class="section-label section-label--primary reveal">{t('What we do', 'Cosa facciamo')}</span>
      <h2 class="reveal reveal-delay-1" id="pillars-title">{t('The full system, or the modules you need', 'Il sistema completo, o i moduli che vi servono')}</h2>
      <div class="section-divider reveal reveal-delay-2"></div>

      <div class="pillars-2">
        <article class="card card--service card--lead reveal">
          <div class="card__header">
            <div class="card__icon">{I['activity']}</div>
            <h3 class="card__title">{t('Pharmacovigilance', 'Farmacovigilanza')}</h3>
          </div>
          <p class="card__text">{t(
              f'For {n.word("full_systems")} marketing authorisation holders we are the entire pharmacovigilance system. For others we run single modules: EU-QPPV and PSMF, case management, literature monitoring, aggregate reports, signal management, audits.',
              f'Per {n.word("full_systems")} titolari AIC siamo l\'intero sistema di farmacovigilanza. Per altri gestiamo singoli moduli: EU-QPPV e PSMF, gestione dei casi, monitoraggio della letteratura, report aggregati, signal management, audit.')}</p>
          <a href="{c.url('pv')}" class="card__link">{t('The PV System', 'Il sistema PV')} {I['arrow']}</a>
        </article>

        <article class="card card--service reveal reveal-delay-1">
          <div class="card__header">
            <div class="card__icon">{I['book']}</div>
            <h3 class="card__title">Medical Affairs</h3>
          </div>
          <p class="card__text">{t(
              'The scientific service required by Italian law, medical information enquiries, scientific review of promotional materials and training for medical teams.',
              'Il servizio scientifico previsto dalla normativa italiana, le richieste di informazione medica, la revisione scientifica dei materiali promozionali e la formazione dei team medici.')}</p>
          <a href="{c.url('services', 'medical-affairs')}" class="card__link">{t('Medical Affairs services', 'Servizi di Medical Affairs')} {I['arrow']}</a>
        </article>
      </div>
    </div>
  </section>

  <!-- WHY MAHs STAY -->
  <section class="why-section section--bg" id="why-us" aria-labelledby="why-title">
    <div class="container">
      <div class="why-section__header">
        <span class="section-label section-label--primary reveal">{t('Why MAC', 'Perché MAC')}</span>
        <h2 class="reveal reveal-delay-1" id="why-title">{t('Why marketing authorisation holders stay with us', 'Perché i titolari AIC restano con noi')}</h2>
        <div class="section-divider reveal reveal-delay-2"></div>
      </div>

      <div class="why-cards why-cards--4">
        <div class="why-card reveal">
          <div class="why-card__icon">{I['chat']}</div>
          <h3 class="why-card__title">{t('A direct line to the people doing the work', 'Un canale diretto con chi fa il lavoro')}</h3>
          <p class="why-card__text">{t(
              'You speak to the specialists who process your cases and write your reports. No intermediaries.',
              'Parlate con gli specialisti che gestiscono i vostri casi e scrivono i vostri report. Nessun intermediario.')}</p>
        </div>
        <div class="why-card reveal reveal-delay-1">
          <div class="why-card__icon">{I['stethoscope']}</div>
          <h3 class="why-card__title">{t('Medical assessment by physicians', 'Valutazione medica fatta da medici')}</h3>
          <p class="why-card__text">{t(
              'Cases that need medical judgement are assessed by a physician on our team.',
              'I casi che richiedono un giudizio clinico sono valutati da un medico del nostro team.')}</p>
        </div>
        <div class="why-card reveal reveal-delay-2">
          <div class="why-card__icon">{I['shield']}</div>
          <h3 class="why-card__title">{t('Your data, kept separate and protected', 'I vostri dati, separati e protetti')}</h3>
          <p class="why-card__text">{t(
              'A dedicated environment for each client, access through VPN with multi-factor authentication, safety databases validated to GAMP 5.',
              'Un ambiente dedicato per ogni cliente, accesso tramite VPN con autenticazione a più fattori, database di sicurezza validati GAMP 5.')}</p>
        </div>
        <div class="why-card reveal reveal-delay-3">
          <div class="why-card__icon">{I['clipboard']}</div>
          <h3 class="why-card__title">{t('A record you can check', 'Risultati verificabili')}</h3>
          <p class="why-card__text">{t(
              f'No PSUSA findings in {n.psusa_months} months. AIFA inspections closed without critical findings {c.draft("numero e anni delle ispezioni AIFA; formulazione unica dell esito ispettivo")}. Key clients with us for more than {n.client_years} years.',
              f'Nessun finding PSUSA in {n.psusa_months} mesi. Ispezioni AIFA concluse senza rilievi critici {c.draft("numero e anni delle ispezioni AIFA; formulazione unica dell esito ispettivo")}. Clienti principali con noi da oltre {n.client_years} anni.')}</p>
        </div>
      </div>
    </div>
  </section>

  <!-- THE MAC METHOD -->
  <section class="method-section" id="method" aria-labelledby="method-title">
    <div class="container">
      <div class="method-section__header text-center">
        <span class="section-label section-label--primary reveal">{t('The MAC method', 'Il metodo MAC')}</span>
        <h2 class="reveal reveal-delay-1" id="method-title">{t('Quality is not by chance.<br>It is a method.', 'La qualità non è un caso.<br>È un metodo.')}</h2>
        <div class="section-divider reveal reveal-delay-2"></div>
      </div>

      <ol class="method-manifesto">
        <li class="method-manifesto__item reveal reveal-delay-1">
          <span class="method-manifesto__number">01</span>
          <div class="method-manifesto__body">
            <h3 class="method-manifesto__title">{t('People', 'Persone')}</h3>
            <p class="method-manifesto__text">{t(
                f'{n.team} specialists: physicians, pharmacists, biologists, quality and IT professionals. Structured GVP training and a defined competency path. {n.retention}% of the team has been with us for more than a year.',
                f'{n.team} specialisti: medici, farmacisti, biologi, professionisti della qualità e dell\'IT. Formazione GVP strutturata e un percorso di competenze definito. L\'{n.retention}% del team è con noi da oltre un anno.')}</p>
          </div>
        </li>
        <li class="method-manifesto__item reveal reveal-delay-2">
          <span class="method-manifesto__number">02</span>
          <div class="method-manifesto__body">
            <h3 class="method-manifesto__title">{t('Processes', 'Processi')}</h3>
            <p class="method-manifesto__text">{t(
                'A documented procedure for every activity. A live dashboard shows each submission deadline, so every due date has an owner and workloads stay balanced.',
                'Una procedura documentata per ogni attività. Un cruscotto in tempo reale mostra ogni scadenza di sottomissione: ogni termine ha un responsabile e i carichi restano bilanciati.')}</p>
          </div>
        </li>
        <li class="method-manifesto__item reveal reveal-delay-3">
          <span class="method-manifesto__number">03</span>
          <div class="method-manifesto__body">
            <h3 class="method-manifesto__title">{t('Measured improvement', 'Miglioramento misurato')}</h3>
            <p class="method-manifesto__text">{t(
                'We review compliance indicators with you. Deviations are investigated to root cause and closed with corrective and preventive actions. New regulations enter our procedures through change control.',
                'Rivediamo con voi gli indicatori di compliance. Le deviazioni sono analizzate fino alla causa e chiuse con azioni correttive e preventive. Le nuove norme entrano nelle procedure tramite change control.')}</p>
            <a href="{c.url('quality', 'improvement')}" class="card__link">{t('How the system improves', 'Come il sistema migliora')} {I['arrow']}</a>
          </div>
        </li>
      </ol>
    </div>
  </section>

  <!-- SYSTEMS AND SOURCES -->
  <section class="tools-band" aria-labelledby="tools-title">
    <h2 class="tools-band__title" id="tools-title">{t('Systems and sources we work with', 'Sistemi e fonti con cui lavoriamo')}</h2>
    <ul class="sr-only">{''.join(f'<li>{x}</li>' for x in TOOLS)}</ul>
    <div class="tech-ticker" aria-hidden="true">
      <div class="tech-ticker__track">{ticker_items}{ticker_items}</div>
    </div>
  </section>

  <!-- THE YEAR IN FIGURES -->
  <section class="section section--bg" aria-labelledby="figures-title">
    <div class="container">
      <div class="why-section__header">
        <span class="section-label section-label--primary reveal">{t('Results', 'Risultati')}</span>
        <h2 class="reveal reveal-delay-1" id="figures-title">{t(f'{n.year} in figures', f'Il {n.year} in numeri')}</h2>
        <div class="section-divider reveal reveal-delay-2"></div>
      </div>
      <div class="why-cards why-cards--4">
        <div class="why-card text-center reveal">
          <div class="stats-bar__number">{n.cases}+</div>
          <p class="why-card__text">{t('cases managed end to end', 'casi gestiti end-to-end')}</p>
        </div>
        <div class="why-card text-center reveal reveal-delay-1">
          <div class="stats-bar__number">~{n.reports}</div>
          <p class="why-card__text">{t('aggregate reports', 'report aggregati')}</p>
        </div>
        <div class="why-card text-center reveal reveal-delay-2">
          <div class="stats-bar__number">~{n.signal_sessions}</div>
          <p class="why-card__text">{t('signal detection sessions', 'sessioni di signal detection')}</p>
        </div>
        <div class="why-card text-center reveal reveal-delay-3">
          <div class="stats-bar__number">+{n.growth}%</div>
          <p class="why-card__text">{t('team growth between 2024 and 2026', 'crescita del team tra 2024 e 2026')}</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ABOUT PREVIEW -->
  <section class="section" id="about-preview" aria-labelledby="about-preview-title">
    <div class="container">
      <div class="about-preview">
        <div>
          <span class="section-label section-label--primary reveal">{t('2001–2026 · 25 years in pharmacovigilance', '2001–2026 · 25 anni di farmacovigilanza')}</span>
          <h2 class="reveal reveal-delay-1" id="about-preview-title">{t('In pharmacovigilance since 2001', 'Nella farmacovigilanza dal 2001')}</h2>
          <div class="section-divider reveal reveal-delay-2"></div>
        </div>
        <div class="reveal reveal-delay-2">
          <p>{t(
              f'MAC was founded by a physician who had led a drug safety unit in industry. Twenty-five years later, the same scientific discipline guides a team of {n.team}.',
              f'MAC è stata fondata da un medico che aveva diretto una drug safety unit in azienda. Venticinque anni dopo, lo stesso rigore scientifico guida un team di {n.team} persone.')}</p>
          <a href="{c.url('about')}" class="btn btn--outline mt-8">{t('About us', 'Chi siamo')} {I['arrow']}</a>
        </div>
      </div>
    </div>
  </section>
{c.cta(t('Tell us which products, countries and case volumes you need to cover.', 'Diteci quali prodotti, paesi e volumi di casi dovete coprire.'),
       t('Contact us', 'Contattateci'),
       t('We reply within one working day.', 'Rispondiamo entro un giorno lavorativo.'))}"""

    return {
        "title": t("Outsourced pharmacovigilance system and Medical Affairs · MAC",
                   "Sistema di farmacovigilanza in outsourcing e Medical Affairs · MAC"),
        "desc": t(f"EU-QPPV, PSMF, case management, aggregate reports and signal management in one GVP system. {n.mah} marketing authorisation holders, {n.cases}+ cases a year. Since 2001.",
                  f"EU-QPPV, PSMF, gestione dei casi, report aggregati e signal management in un unico sistema GVP. {n.mah} titolari AIC, {n.cases}+ casi l'anno. Dal 2001."),
        "jsonld": {
            "@context": "https://schema.org",
            "@type": "ProfessionalService",
            "name": "Medical Affairs Consulting S.r.l.",
            "alternateName": "MAC",
            "url": c.abs(),
            "logo": "https://www.med-af-consulting.com/img/mac-logo.png",
            "foundingDate": "2001",
            "email": "contactus@med-af-consulting.it",
            "vatID": "IT04027560129",
            "address": {"@type": "PostalAddress", "streetAddress": "Corso Italia 39", "postalCode": "21047",
                        "addressLocality": "Saronno", "addressRegion": "VA", "addressCountry": "IT"},
            "sameAs": ["https://www.linkedin.com/company/med-af-consulting"],
            "knowsAbout": ["Pharmacovigilance", "Medical Affairs"],
        },
        "body": body,
    }
