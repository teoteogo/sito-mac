"""Quality & Data — section 5.4 of the copy document."""


def render(c):
    t, I = c.t, c.icon

    def points(items, cls=""):
        return f'<div class="point-grid {cls}">' + "".join(f"""
        <div class="point reveal">
          <h3 class="point__title">{a}</h3>
          <p class="point__text">{b}</p>
        </div>""" for a, b in items) + "\n      </div>"

    qms = points([
        (t('Written procedures', 'Procedure scritte'),
         t('Standard operating procedures (SOPs) cover case management, literature monitoring, aggregate reports, signal management, vendor management, internal audits and corrective actions.',
           'Le SOP coprono gestione dei casi, monitoraggio della letteratura, report aggregati, signal management, gestione dei fornitori, audit interni e azioni correttive.')),
        (t('Checks against the source', 'Controlli sulla fonte'),
         t('Data entry is verified against the original documents, and the source of every case stays accessible.',
           'Il data entry è verificato sui documenti originali e la fonte di ogni caso resta accessibile.')),
        (t('Internal audits', 'Audit interni'),
         t('Every year we audit our own compliance with EU good pharmacovigilance practices (GVP).',
           'Ogni anno verifichiamo la nostra conformità alle GVP.')),
        (t('Trained people', 'Persone formate'),
         t('Each role has a training plan and documented proof of competence. Training is updated whenever a regulation changes.',
           'Ogni ruolo ha un piano di formazione e una verifica documentata delle competenze. La formazione si aggiorna a ogni cambiamento normativo.')),
    ], "point-grid--2")

    improve = [
        (t('We measure.', 'Misuriamo.'),
         t('Compliance indicators, such as on-time submissions, are tracked and reviewed with each client.',
           'Gli indicatori di compliance, come la puntualità delle sottomissioni, sono monitorati e rivisti con ogni cliente.')),
        (t('We record deviations.', 'Registriamo le deviazioni.'),
         t('A late case or a process error is logged, not explained away. Major and critical deviations go into the PSMF.',
           'Un caso in ritardo o un errore di processo viene registrato, non giustificato. Le deviazioni maggiori e critiche entrano nel PSMF.')),
        (t('We find the cause and fix it.', 'Troviamo la causa e la correggiamo.'),
         t('Each deviation gets a root cause analysis and a corrective and preventive action (CAPA), with an owner and a due date.',
           'Ogni deviazione ha un\'analisi della causa e un\'azione correttiva e preventiva (CAPA), con un responsabile e una scadenza.')),
        (t('We check that the fix worked.', 'Verifichiamo che la correzione abbia funzionato.'),
         t('Actions are closed only after their effectiveness is verified.',
           'Le azioni si chiudono solo dopo la verifica di efficacia.')),
        (t('We keep up with the rules.', 'Seguiamo le norme.'),
         t('New guidance and regulations are assessed for impact and brought into procedures through change control.',
           'Nuove linee guida e nuovi regolamenti sono valutati per impatto e recepiti nelle procedure tramite change control.')),
    ]
    improve_html = "".join(f"""
          <li class="timeline__item reveal">
            <span class="timeline__num">{i}</span>
            <div>
              <h3 class="timeline__title">{a}</h3>
              <p class="timeline__text">{b}</p>
            </div>
          </li>""" for i, (a, b) in enumerate(improve, 1))

    security = points([
        (t('Access by role and project', 'Accesso per ruolo e per progetto'),
         t('Access to each client project is granted by role and after project-specific training. Project authorisations are mapped.',
           'L\'accesso a ogni progetto cliente è concesso per ruolo e dopo la formazione specifica sul progetto. Le autorizzazioni ai progetti sono mappate.')),
        (t('Controlled access', 'Accesso controllato'),
         t('VPN with multi-factor authentication.', 'VPN con autenticazione a più fattori.')),
        (t('Validated systems', 'Sistemi validati'),
         t('Safety databases validated to GAMP 5 under a documented IT validation procedure.',
           'Database di sicurezza validati GAMP 5 con una procedura documentata di validazione IT.')),
        (t('Continuity', 'Continuità'),
         t('Automatic backups, a disaster recovery plan and on-call cover around the clock.',
           'Backup automatici, piano di disaster recovery e reperibilità 24 ore su 24.')),
        (t('Our role under GDPR', 'Il nostro ruolo ai sensi del GDPR'),
         t('We act as data processor for the marketing authorisation holder, under a written agreement (Article 28 GDPR). Product and commercial information is covered by confidentiality agreements.',
           'Operiamo come responsabile del trattamento per conto del titolare AIC, con atto di nomina (art. 28 GDPR). Le informazioni di prodotto e commerciali sono coperte da accordi di riservatezza.')),
    ], "point-grid--3")

    standards = [
        t('EU good pharmacovigilance practices (GVP)', 'Good pharmacovigilance practices (GVP) dell\'UE'),
        t('Implementing Regulation (EU) No 520/2012 as amended by Regulation (EU) 2025/1466',
          'Reg. di esecuzione (UE) n. 520/2012 come modificato dal Reg. (UE) 2025/1466'),
        'ICH E2B(R3)', 'GAMP 5', 'GDPR',
    ]

    ethics = [
        (t('Regulatory compliance', 'Conformità normativa'),
         t('We uphold good practices (GxP) and national and international sector regulations, and support clients in meeting every regulatory obligation.',
           'Rispettiamo e promuoviamo le Good Practices (GxP) e le normative nazionali e internazionali del settore, supportando i clienti nel rispetto di tutti gli obblighi regolatori.')),
        (t('Integrity and anti-corruption', 'Integrità e anticorruzione'),
         t('Every relationship is managed ethically and documented. We do not tolerate conflicts of interest, favouritism or any practice that could compromise our credibility.',
           'Ogni rapporto è gestito in modo etico, documentato e conforme. Non tolleriamo conflitti di interesse, favoritismi o qualsiasi pratica che comprometta la nostra credibilità.')),
        (t('Professional independence', 'Indipendenza professionale'),
         t('Our analyses, assessments and recommendations are objective and based on reliable, verifiable data.',
           'Le nostre analisi, valutazioni e raccomandazioni sono obiettive e basate su dati affidabili e verificabili.')),
        (t('Client relationships', 'Rapporti con i clienti'),
         t('Legal responsibility stays with the marketing authorisation holder, as the law requires. Roles and responsibilities are defined in the contract and in the PSMF.',
           'La responsabilità legale resta del titolare AIC, come previsto dalla normativa. Ruoli e responsabilità sono definiti nel contratto e nel PSMF.')),
        (t('Confidentiality', 'Riservatezza'),
         t('We protect clients\' technical, scientific and commercial information under confidentiality agreements and in line with the GDPR.',
           'Proteggiamo le informazioni tecniche, scientifiche e commerciali dei clienti con accordi di riservatezza e nel rispetto del GDPR.')),
        (t('Partners and suppliers', 'Partner e fornitori'),
         t('We build partnerships on legality, quality and mutual respect, with partners who share high professional and ethical standards.',
           'Costruiamo collaborazioni su legalità, qualità e rispetto reciproco, con partner che condividono elevati standard professionali ed etici.')),
    ]
    ethics_html = "".join(f"""
        <div class="etica-item">
          <div class="etica-item-top"><span class="etica-num">{i:02d}</span><h3>{a}</h3></div>
          <p>{b}</p>
        </div>""" for i, (a, b) in enumerate(ethics, 1))

    body = c.page_header(
        t('Quality &amp; Data', 'Qualità e dati'),
        t('Quality and data protection', 'Qualità e protezione dei dati'),
        t('The guarantees behind the system: documented procedures, validated databases, and health data handled under clear rules.',
          'Le garanzie dietro al sistema: procedure documentate, database validati e dati sanitari trattati con regole chiare.'),
        bg="bussola.webp",
    ) + f"""

  <section class="section" id="quality-system" aria-labelledby="qms-title">
    <div class="container">
      <span class="section-label section-label--primary reveal">{t('Quality system', 'Sistema qualità')}</span>
      <h2 class="reveal reveal-delay-1" id="qms-title">{t('A quality system built on GVP', 'Un sistema qualità costruito sulle GVP')}</h2>
      <div class="section-divider reveal reveal-delay-2"></div>
      {qms}
    </div>
  </section>

  <section class="section section--bg" id="improvement" aria-labelledby="improve-title">
    <div class="container">
      <div class="split split--top">
        <div>
          <span class="section-label section-label--primary reveal">{t('Improvement', 'Miglioramento')}</span>
          <h2 class="reveal reveal-delay-1" id="improve-title">{t('How the system improves', 'Come il sistema migliora')}</h2>
          <div class="section-divider reveal reveal-delay-2"></div>
          <p class="lead reveal reveal-delay-2">{t(
              'A quality system is judged by what happens when something goes wrong or something changes. This is what happens here.',
              'Un sistema qualità si giudica da ciò che accade quando qualcosa va storto o qualcosa cambia. Da noi accade questo.')}</p>
        </div>
        <ol class="timeline">{improve_html}
        </ol>
      </div>
    </div>
  </section>

  <section class="section" id="data-protection" aria-labelledby="sec-title">
    <div class="container">
      <span class="section-label section-label--primary reveal">{t('Data', 'Dati')}</span>
      <h2 class="reveal reveal-delay-1" id="sec-title">{t('Security and data protection', 'Sicurezza e protezione dei dati')}</h2>
      <div class="section-divider reveal reveal-delay-2"></div>
      {security}
    </div>
  </section>

  <section class="section section--bg" id="standards" aria-labelledby="std-title">
    <div class="container">
      <span class="section-label section-label--primary reveal">{t('References', 'Riferimenti')}</span>
      <h2 class="reveal reveal-delay-1" id="std-title">{t('Standards we work to', 'Gli standard con cui lavoriamo')}</h2>
      <div class="section-divider reveal reveal-delay-2"></div>
      <ul class="standards reveal">{''.join(f'<li>{I["check"]}<span>{s}</span></li>' for s in standards)}</ul>
    </div>
  </section>

  <section class="section" id="ethics-code" aria-labelledby="ethics-title">
    <div class="container">
      <span class="section-label section-label--primary reveal">{t('Code of ethics', 'Codice etico')}</span>
      <h2 class="reveal reveal-delay-1" id="ethics-title">{t('The principles behind every working relationship', 'I principi dietro ogni rapporto di lavoro')}</h2>
      <div class="section-divider reveal reveal-delay-2"></div>
      <div class="etica-grid reveal">{ethics_html}
      </div>
    </div>
  </section>
{c.cta(t('Qualifying us as a vendor?', 'Ci state qualificando come fornitore?'),
       t('Request our quality documentation', 'Richiedete la documentazione'),
       t('Ask for our quality documentation.', 'Chiedete la nostra documentazione di qualità.'))}"""

    return {
        "title": t("GVP quality system and data protection · MAC", "Sistema qualità GVP e protezione dei dati · MAC"),
        "desc": t("How MAC's quality system works: written procedures, source checks, internal audits, deviations closed with CAPA, validated databases and protection of patient data.",
                  "Come funziona il sistema qualità di MAC: procedure scritte, controlli sulla fonte, audit interni, deviazioni chiuse con CAPA, database validati e protezione dei dati dei pazienti."),
        "body": body,
    }
