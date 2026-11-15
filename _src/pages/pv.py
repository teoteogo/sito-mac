"""The PV System — section 5.2 of the copy document (new page)."""


def render(c):
    t, n = c.t, c.n

    rows = [
        (t('A qualified person, resident and operating in the EU/EEA.', 'Una persona qualificata che risiede e opera in UE/SEE.'),
         t(f'We provide the EU-QPPV and a deputy, for marketing authorisation holders in Italy, Germany and Switzerland, and the local pharmacovigilance contact for Italy.',
           f'Mettiamo a disposizione EU-QPPV e deputy, per titolari AIC in Italia, Germania e Svizzera, e il referente locale di farmacovigilanza per l\'Italia.')),
        (t('A PSMF that describes the system as it is.', 'Un PSMF che descrive il sistema com\'è.'),
         t('We write it, keep it current and record deviations in it.',
           'Lo redigiamo, lo teniamo aggiornato e vi registriamo le deviazioni.')),
        (t('Serious cases submitted within 15 days, non-serious within 90.', 'Casi gravi trasmessi entro 15 giorni, non gravi entro 90.'),
         t('Intake, validity check, duplicate search, MedDRA coding, medical assessment, follow-up and E2B(R3) submission to EudraVigilance.',
           'Ricezione, verifica di validità, ricerca dei duplicati, codifica MedDRA, valutazione medica, follow-up e trasmissione E2B(R3) a EudraVigilance.')),
        (t('Medical literature monitored every week.', 'Letteratura medica monitorata ogni settimana.'),
         t('Weekly searches in PubMed and Embase, and screening of the EMA medical literature monitoring (MLM) output.',
           'Ricerche settimanali su PubMed ed Embase e screening dei risultati del servizio MLM di EMA.')),
        (t('Periodic safety update reports and risk management plans.', 'PSUR e piani di gestione del rischio.'),
         t(f'More than {n.reports} aggregate reports a year for EU and non-EU authorities; PSURs in PBRER format.',
           f'Oltre {n.reports} report aggregati l\'anno per autorità UE ed extra-UE; PSUR in formato PBRER.')),
        (t('Signals detected, validated and documented.', 'Segnali rilevati, validati e documentati.'),
         t(f'More than {n.signal_sessions} signal detection sessions a year in EVDAS, with medical review.',
           f'Oltre {n.signal_sessions} sessioni di signal detection l\'anno su EVDAS, con revisione medica.')),
        (t('Product data kept up to date.', 'Dati di prodotto aggiornati.'),
         t('Article 57 data in XEVMPD, and the transition to the EMA Product Management Service (PMS).',
           'Dati art. 57 in XEVMPD e transizione al Product Management Service (PMS) di EMA.')),
        (t('Safety variations and authority requests.', 'Variazioni di sicurezza e richieste delle autorità.'),
         t('Updates to the summary of product characteristics (SmPC) and package leaflet, and replies to EMA and AIFA requests.',
           'Aggiornamenti di RCP e foglio illustrativo, risposte alle richieste di EMA e AIFA.')),
        (t('A quality system that is audited.', 'Un sistema qualità sottoposto ad audit.'),
         t('Documented procedures, compliance indicators and risk-based audits that include our own subcontractors.',
           'Procedure documentate, indicatori di compliance e audit basati sul rischio, estesi ai nostri fornitori.')),
    ]
    table = "".join(f"""
          <tr class="reveal">
            <td class="oblig__num">{i:02d}</td>
            <th scope="row">{a}</th>
            <td>{b}</td>
          </tr>""" for i, (a, b) in enumerate(rows, 1))

    steps = c.steps([
        (t('Gap assessment and plan', 'Gap assessment e piano'),
         t('We review your current system and agree a documented transition plan with dates.',
           'Esaminiamo il sistema attuale e concordiamo un piano di transizione documentato, con le date.')),
        (t('Agreements, QPPV and PSMF', 'Accordi, QPPV e PSMF'),
         t('Contract and SDEA signed, QPPV change notified, PSMF written or transferred.',
           'Firma di contratto e SDEA, notifica del cambio di QPPV, redazione o trasferimento del PSMF.')),
        (t('Data migration', 'Migrazione dei dati'),
         t('Cases and product data move into the validated database, and the migration is verified.',
           'Casi e dati di prodotto passano nel database validato, e la migrazione viene verificata.')),
        (t('Go-live and close follow-up', 'Avvio e affiancamento'),
         t('We take over operations and review the first weeks with you.',
           'Prendiamo in carico le attività e rivediamo con voi le prime settimane.')),
    ])

    body = c.page_header(
        t('The PV System', 'Il sistema PV'),
        t('A complete pharmacovigilance system, run for you', 'Un sistema di farmacovigilanza completo, gestito per voi'),
        t(f'For {n.word("full_systems")} marketing authorisation holders we are the entire pharmacovigilance system. Legal responsibility stays with the marketing authorisation holder (MAH), as the law requires. Who does what is written into the contract and the pharmacovigilance system master file (PSMF). {c.draft("numero di titolari AIC con sistema completo: non compare nella company presentation")}',
          f'Per {n.word("full_systems")} titolari AIC siamo l\'intero sistema di farmacovigilanza. La responsabilità legale resta del titolare AIC, come prevede la normativa. Chi fa cosa è scritto nel contratto e nel PSMF. {c.draft("numero di titolari AIC con sistema completo: non compare nella company presentation")}'),
    ) + f"""

  <section class="section" aria-labelledby="oblig-title">
    <div class="container">
      <span class="section-label section-label--primary reveal">{t('Coverage', 'Copertura')}</span>
      <h2 class="reveal reveal-delay-1" id="oblig-title">{t('Your obligations, and how we cover them', 'I vostri obblighi, e come li copriamo')}</h2>
      <div class="section-divider reveal reveal-delay-2"></div>
      <table class="oblig">
        <thead>
          <tr>
            <th scope="col"><span class="sr-only">#</span></th>
            <th scope="col">{t('What the MAH must have', 'Cosa deve avere il titolare AIC')}</th>
            <th scope="col">{t('How we cover it', 'Come lo copriamo')}</th>
          </tr>
        </thead>
        <tbody>{table}
        </tbody>
      </table>
    </div>
  </section>

  <section class="section section--bg" aria-labelledby="who-title">
    <div class="container">
      <div class="split">
        <div>
          <span class="section-label section-label--primary reveal">{t('Governance', 'Governance')}</span>
          <h2 class="reveal reveal-delay-1" id="who-title">{t('Who does what', 'Chi fa cosa')}</h2>
          <div class="section-divider reveal reveal-delay-2"></div>
        </div>
        <div class="reveal reveal-delay-2">
          <p class="lead">{t('You keep the decisions that belong to the MAH. We run the operations and report on them.',
                             'A voi restano le decisioni che spettano al titolare AIC. Noi gestiamo le attività operative e ne rendiamo conto.')}</p>
          <p>{t('The contract and the safety data exchange agreement (SDEA) set out roles, data flows, timelines and your right to audit us. You receive compliance indicators at the frequency we agree, and you always know who your contacts are.',
                'Il contratto e l\'accordo di scambio dei dati di sicurezza (SDEA) definiscono ruoli, flussi di dati, tempi e il vostro diritto di sottoporci ad audit. Ricevete gli indicatori di compliance con la frequenza concordata e sapete sempre chi sono i vostri referenti.')}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="transition" aria-labelledby="transition-title">
    <div class="container">
      <span class="section-label section-label--primary reveal">{t('Transition', 'Transizione')}</span>
      <h2 class="reveal reveal-delay-1" id="transition-title">{t('Moving your system to MAC', 'Trasferire il vostro sistema a MAC')}</h2>
      <div class="section-divider reveal reveal-delay-2"></div>
      {steps}
      <p class="section-note reveal">{t('A typical transition takes', 'Una transizione tipica richiede')} {c.draft('durata tipica reale di una transizione')}.</p>
    </div>
  </section>

  <section class="section section--bg" id="regulation-2025-1466" aria-labelledby="reg-title">
    <div class="container">
      <div class="split">
        <div>
          <span class="section-label section-label--primary reveal">{t('Regulation', 'Normativa')}</span>
          <h2 class="reveal reveal-delay-1" id="reg-title">{t('What Regulation (EU) 2025/1466 asks of outsourced pharmacovigilance', 'Cosa chiede il Reg. (UE) 2025/1466 a chi esternalizza la farmacovigilanza')}</h2>
          <div class="section-divider reveal reveal-delay-2"></div>
        </div>
        <div class="reveal reveal-delay-2">
          <p>{t('Since 12 February 2026:', 'Dal 12 febbraio 2026:')}</p>
          <ul class="tick-list">
            <li>{c.icon['check']}<span>{t('Subcontracts must define roles, data exchange and audit rights.', 'I contratti di subappalto devono definire ruoli, scambio dei dati e diritti di audit.')}</span></li>
            <li>{c.icon['check']}<span>{t('A subcontractor cannot pass work on without written consent.', 'Il fornitore non può affidare attività a terzi senza consenso scritto.')}</span></li>
            <li>{c.icon['check']}<span>{t('Major and critical deviations go into the PSMF.', 'Le deviazioni maggiori e critiche vanno nel PSMF.')}</span></li>
            <li>{c.icon['check']}<span>{t('Risk-based audits cover every pharmacovigilance activity, vendors included.', 'Gli audit basati sul rischio coprono ogni attività di farmacovigilanza, fornitori inclusi.')}</span></li>
          </ul>
          <p>{t('Our contracts and procedures are built on these requirements', 'I nostri contratti e le nostre procedure sono costruiti su questi requisiti')} {c.draft('adeguamento effettivo di contratti e procedure al Reg. (UE) 2025/1466; testo del regolamento da rileggere sulla fonte ufficiale')}.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="inspection" aria-labelledby="insp-title">
    <div class="container">
      <div class="split">
        <div>
          <span class="section-label section-label--primary reveal">{t('Inspections', 'Ispezioni')}</span>
          <h2 class="reveal reveal-delay-1" id="insp-title">{t('When the inspector arrives', 'Quando arriva l\'ispettore')}</h2>
          <div class="section-divider reveal reveal-delay-2"></div>
        </div>
        <div class="reveal reveal-delay-2">
          <p class="lead">{t('We prepare the PSMF and the supporting evidence, take part in the inspection with you and manage the corrective actions that follow',
                             'Prepariamo il PSMF e le evidenze a supporto, partecipiamo all\'ispezione al vostro fianco e gestiamo le azioni correttive successive')} {c.draft('perimetro del supporto in ispezione')}.</p>
        </div>
      </div>
    </div>
  </section>
{c.cta(t('Planning to outsource, or to change provider?', 'State valutando di esternalizzare, o di cambiare fornitore?'),
       t('Plan a transition', 'Pianifichiamo la transizione'))}"""

    return {
        "title": t("Full pharmacovigilance outsourcing: EU-QPPV, PSMF, transition · MAC",
                   "Outsourcing completo della farmacovigilanza: EU-QPPV, PSMF, transizione · MAC"),
        "desc": t("What full pharmacovigilance outsourcing covers: EU-QPPV and PSMF, cases, literature, aggregate reports, signals, product data, governance and a documented transition plan.",
                  "Cosa copre l'outsourcing completo della farmacovigilanza: EU-QPPV e PSMF, casi, letteratura, report aggregati, segnali, dati di prodotto, governance e un piano di transizione documentato."),
        "body": body,
    }
