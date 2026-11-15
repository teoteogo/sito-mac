# Sito MAC — note di progetto

Sito statico di Medical Affairs Consulting S.r.l. su GitHub Pages (`www.med-af-consulting.com`).

## Come si lavora

- **Non modificare a mano gli HTML generati.** Le pagine nascono da `_src/pages/<nome>.py`
  (inglese e italiano affiancati con `t('EN', 'IT')`) e si rigenerano con:

  ```bash
  python3 _src/build.py
  ```

- Menu, footer, meta, hreflang, sitemap, redirect e 404 stanno in `_src/build.py`.
- I testi legali (privacy, cookie) sono in `_src/legal/<lingua>/`: si cambiano solo su richiesta.
- **Numeri:** un'unica fonte, `data/numeri.json`. Mai scrivere un numero a mano nelle pagine.
- **Bozze:** un dato non confermato si marca con `c.draft('nota')`; il build lo elenca in `BOZZE.md`
  e lo evidenzia in giallo. `python3 _src/build.py --release` fallisce finché ne resta una.
  Nessun testo va su `main` con una bozza aperta.
- Stili: `css/style.css` (design system) e `css/pages.css` (componenti delle pagine).

## Lingue e URL

- **Inglese = lingua di riferimento, alla radice.** Italiano sotto `/it/`, tradotto blocco per blocco,
  con gli stessi numeri e le stesse FAQ nello stesso ordine.
- I vecchi indirizzi (`/en/...`, `servizi.html`, ecc.) sono pagine di redirect generate dal build.

## Posizionamento

MAC è un **sistema di farmacovigilanza esternalizzato e verificabile**; il Medical Affairs è il
secondo pilastro. Non una consulenza generalista. Promessa: “Your pharmacovigilance system,
inspection-ready.” Percorso del lettore: Home → The PV System → Quality & Data → Contact.

Menu (identico ovunque): Home · The PV System · Services · Quality & Data · About · Insights · [Contact us].
Nel footer: FAQ, Careers, tre informative privacy, cookie, riga legale.

Ogni pagina: H1 (promessa) → sottotitolo → prova (numero datato o fatto) → sezioni H2 che aprono
con la risposta → un solo pulsante principale, verso Contact.

## Tono e regole di scrittura

- Inglese britannico (*authorisation*, *specialised*, *programme*). “We” e “you”; in italiano
  “noi” e “voi”, il “tu” solo in Lavora con noi.
- Frasi brevi, verbo attivo. Prove al posto degli aggettivi. Vietati: leader, excellence,
  cutting-edge, 360°, passion, promesse assolute (“guaranteed compliance”, “zero risk”).
- **Fuori dal sito:** Lean, Kaizen, Asaichi, KPO, “km 0”, Oracle Argus, VigiBase, badge ISO 9001.
  Il miglioramento si mostra con KPI di compliance, deviazioni, CAPA, change control.
- Ogni numero ha un periodo (“a year”, “in 24 months”). EN 15,000+ · IT 15.000+.
- Sigle sciolte alla prima occorrenza di ogni pagina. Norme in forma estesa: “Regulation (EU)
  2025/1466”, in italiano “Reg. (UE) 2025/1466”.
- Pulsanti: verbo + oggetto. Mai “Learn more”. Un solo impegno di risposta: “within one working day”.

## Lessico (forma da usare)

| English | Italiano | Da evitare |
| --- | --- | --- |
| marketing authorisation holder (MAH) | titolare AIC | MA holder, pharma company |
| suspected adverse reaction | sospetta reazione avversa | side effect, effetto avverso |
| individual case safety report (ICSR), poi “case” | ICSR, “caso” | “segnalazioni” per i casi gestiti |
| serious / non-serious | grave / non grave | severe |
| submission, to submit | trasmissione, trasmettere | reporting, sottomettere |
| EU-QPPV | EU-QPPV | QP, Qualified Person da solo |
| PSUR (in PBRER format) | PSUR (in formato PBRER) | “PSUR and PBRER” come due documenti |
| risk management plan (RMP) | piano di gestione del rischio | RMP tra i rapporti periodici |
| signal management: detection, validation, assessment | rilevazione, validazione, valutazione | automatic signal detection |
| corrective and preventive action (CAPA), change control, deviation | idem | Kaizen, Lean |

Vincoli GVP Module VI: casi gravi entro 15 giorni di calendario, non gravi entro 90; il giorno
zero parte quando chiunque lavori per il titolare, fornitori compresi, riceve le informazioni
minime; letteratura almeno settimanale; SUSAR 7/15 giorni solo nelle sperimentazioni; i singoli
SAE non si notificano all'autorità; il QPPV lo nomina il titolare, MAC mette a disposizione la persona.

## Fatti confermati dal titolare (15 novembre 2026)

- MAC **non ha mai ricevuto ispezioni AIFA**: nessuna frase sull'esito di ispezioni.
- Fondatore unico: Dr. Stefano Franchini (non tre fondatori).
- Numeri di sintesi con il “+” (15,000+, 50+, 100+), non “~”.
- Sicurezza dei dati: non si parla di “un ambiente per cliente”; l'accesso ai progetti è per ruolo
  e formazione sul progetto, con autorizzazioni mappate. Niente riquadri “Patient data” e “Masking”.
- Numeri verificati sulla company presentation 2026, tranne `full_systems` (ancora bozza).

## Materiali di riferimento

Audit del sito (25 ottobre 2026), documento “Sito MAC — struttura, gerarchia e testi”
(13 novembre 2026) e GVP Module VI con Addendum I e II. Non sono nel repository, perché tutto
ciò che è nel repository viene pubblicato da GitHub Pages: vanno ricaricati in sessione se servono.
