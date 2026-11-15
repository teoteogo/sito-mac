"""FAQ — section 5.7 of the copy document. Same questions, same order, in both languages."""
import re


def render(c):
    t, n, I = c.t, c.n, c.icon

    qa = [
        (t('Can you run our whole PV system?', 'Potete gestire l\'intero sistema PV?'),
         t(f'Yes. For {n.word("full_systems")} marketing authorisation holders (MAHs) we are the entire pharmacovigilance (PV) system: QPPV, PSMF, database, cases, reports and signals. You can also contract single modules.',
           f'Sì. Per {n.word("full_systems")} titolari AIC siamo l\'intero sistema di farmacovigilanza (PV): QPPV, PSMF, database, casi, report e segnali. Potete anche affidarci singoli moduli.')),
        (t('Who stays responsible?', 'Chi resta responsabile?'),
         t('The marketing authorisation holder. Outsourcing transfers tasks, not legal responsibility. The contract and the pharmacovigilance system master file (PSMF) define who does what.',
           'Il titolare AIC. L\'outsourcing trasferisce le attività, non la responsabilità legale. Contratto e PSMF definiscono chi fa cosa.')),
        (t('What are the submission deadlines?', 'Quali sono le scadenze di trasmissione?'),
         t('After authorisation: serious cases within 15 days, non-serious within 90. In clinical trials: fatal or life-threatening suspected unexpected serious adverse reactions (SUSARs) within 7 days, other SUSARs within 15.',
           'Dopo l\'autorizzazione: casi gravi entro 15 giorni, non gravi entro 90. Nelle sperimentazioni: SUSAR fatali o pericolose per la vita entro 7 giorni, altre SUSAR entro 15.')),
        (t('When does the clock start?', 'Da quando decorre il termine?'),
         t('From the day anyone working for the marketing authorisation holder, contractors included, first receives the minimum information for a valid case. That is why cases reach our team directly.',
           'Dal giorno in cui chiunque lavori per il titolare AIC, fornitori compresi, riceve le informazioni minime per un caso valido. Per questo i casi arrivano direttamente al nostro team.')),
        (t('How does a transition work?', 'Come avviene la transizione?'),
         t(f'In four steps: gap assessment and plan; agreements, QPPV and PSMF; data migration; go-live. Dates are set in a documented plan. <a href="{c.url("pv", "transition")}">Moving your system to MAC</a>',
           f'In quattro passi: gap assessment e piano; accordi, QPPV e PSMF; migrazione dei dati; avvio. Le date sono fissate in un piano documentato. <a href="{c.url("pv", "transition")}">Trasferire il vostro sistema a MAC</a>')),
        (t('Where is our data kept?', 'Dove sono conservati i dati?'),
         t(f'{c.draft("sede dei dati e fornitori cloud")} Access to each client project is granted by role and project training, through VPN with multi-factor authentication.',
           f'{c.draft("sede dei dati e fornitori cloud")} L\'accesso a ogni progetto cliente è concesso per ruolo e formazione sul progetto, tramite VPN con autenticazione a più fattori.')),
        (t('What changes with Regulation (EU) 2025/1466?', 'Cosa cambia con il Reg. (UE) 2025/1466?'),
         t('Since 12 February 2026, subcontracts must set out roles, data exchange and audit rights, and audits must cover vendors. We can review your existing contracts against it.',
           'Dal 12 febbraio 2026 i contratti di subappalto devono definire ruoli, scambio dei dati e diritti di audit, e gli audit devono coprire i fornitori. Possiamo verificare i vostri contratti esistenti.')),
        (t('Do you cover the UK and Switzerland?', 'Coprite Regno Unito e Svizzera?'),
         c.draft('ruolo esatto verso MHRA e Swissmedic; risposta da scrivere')),
        (t('What is the legal basis?', 'Qual è la base giuridica?'),
         t('Regulation (EC) No 726/2004 and Directive 2001/83/EC, as amended in 2010, and Implementing Regulation (EU) No 520/2012 as amended by Regulation (EU) 2025/1466.',
           'Reg. (CE) n. 726/2004 e Direttiva 2001/83/CE, come modificati nel 2010, e Reg. di esecuzione (UE) n. 520/2012 come modificato dal Reg. (UE) 2025/1466.')),
    ]

    items = "".join(f"""
          <div class="accordion__item">
            <h2 class="accordion__heading"><button class="accordion__trigger" aria-expanded="false">{q}{I['plus']}</button></h2>
            <div class="accordion__body"><div class="accordion__content"><p>{a}</p></div></div>
          </div>""" for q, a in qa)

    # Structured data only for answers that are not drafts.
    strip = lambda s: re.sub(r"<[^>]+>", "", s).strip()
    jsonld = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
                       for q, a in qa if 'class="draft"' not in a],
    }

    body = c.page_header(
        'FAQ',
        t('Frequently asked questions', 'Domande frequenti'),
        t('Short answers on outsourcing pharmacovigilance to MAC. If yours is not here, write to us.',
          'Risposte brevi su come esternalizzare la farmacovigilanza a MAC. Se la vostra domanda non c\'è, scriveteci.'),
    ) + f"""

  <section class="section section--bg">
    <div class="container" style="max-width:900px;">
      <div class="accordion reveal">{items}
      </div>
    </div>
  </section>
{c.cta(t('Did not find your question?', 'Non avete trovato la vostra domanda?'),
       t('Ask the team', 'Chiedete al team'),
       t('We reply within one working day.', 'Rispondiamo entro un giorno lavorativo.'))}"""

    return {
        "title": t("Pharmacovigilance outsourcing: frequently asked questions · MAC",
                   "Outsourcing della farmacovigilanza: domande frequenti · MAC"),
        "desc": t("Who stays responsible, submission deadlines, day zero, transition, data location and Regulation (EU) 2025/1466: answers for marketing authorisation holders.",
                  "Chi resta responsabile, scadenze di trasmissione, giorno zero, transizione, sede dei dati e Reg. (UE) 2025/1466: risposte per i titolari AIC."),
        "jsonld": jsonld,
        "body": body,
    }
