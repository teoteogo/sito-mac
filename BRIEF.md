# BRIEF — Sito Web Medical Affairs Consulting
> Documento di progetto per Claude Code. Leggi tutto prima di iniziare a scrivere codice.

---

## 1. IDENTITÀ E OBIETTIVO

- **Azienda**: Medical Affairs Consulting (MAC)
- **Sito attuale**: www.med-af-consulting.com (su Wix, da sostituire)
- **Email**: contactus@med-af-consulting.it / info@med-af-consulting.it
- **Sede**: Corso Italia, 39 – Saronno (VA)
- **Attività dal**: 2001
- **Lingue**: Italiano + Inglese (tutte le pagine devono esistere in entrambe le lingue)
- **Target**: Titolari di AIC, Sponsor, aziende farmaceutiche italiane ed europee (B2B professionale)
- **Obiettivo del sito**: Trasmettere autorevolezza, competenza e affidabilità nel settore della farmacovigilanza e medical affairs. Il sito deve essere uno strumento di acquisizione clienti e vetrina professionale.

---

## 2. STACK TECNICO

- **HTML5 + CSS3 + JavaScript vanilla** — nessun framework, nessun CMS
- **Nessuna dipendenza esterna** salvo Google Fonts e Lucide Icons (CDN)
- **Hosting**: Netlify (file statici, deploy via drag & drop o Git)
- **Dati dinamici**: file JSON nella cartella `/data/` per eventi e blog
- **Multilingua**: cartella `/en/` per le versioni inglesi (stesso HTML, testi tradotti)
- **Mobile-first**: responsive su tutti i breakpoint

---

## 3. STRUTTURA FILE DEL PROGETTO

```
mac-website/
│
├── index.html                  ← Homepage IT
├── servizi.html                ← Servizi IT
├── chi-siamo.html              ← Chi siamo IT
├── calendario.html             ← Calendario eventi IT
├── blog.html                   ← Blog / Rubriche IT
├── lavora-con-noi.html         ← Lavora con noi IT
├── contatti.html               ← Contatti IT
├── faq.html                    ← FAQ IT
│
├── en/
│   ├── index.html              ← Homepage EN
│   ├── services.html
│   ├── about.html
│   ├── events.html
│   ├── blog.html
│   ├── careers.html
│   ├── contact.html
│   └── faq.html
│
├── css/
│   ├── style.css               ← Stile globale, variabili CSS, componenti
│   └── animations.css          ← Animazioni scroll e transizioni
│
├── js/
│   ├── main.js                 ← Menu, scroll, language switcher
│   ├── calendario.js           ← Legge eventi.json, genera card, esporta .ics
│   └── blog.js                 ← Legge blog.json, genera card
│
├── data/
│   ├── eventi.json             ← ⬅ AGGIORNARE QUI per nuovi eventi
│   └── blog.json               ← ⬅ AGGIORNARE QUI per nuovi post
│
├── img/
│   ├── logo.svg                ← Logo MAC (placeholder fino a fornitura)
│   ├── favicon.ico
│   ├── hero/                   ← Immagini sezione hero
│   ├── blog/                   ← Anteprime post blog
│   └── certificazioni/         ← Loghi certificazioni (ISO 9001, ecc.)
│
└── BRIEF.md                    ← Questo file
```

---

## 4. DESIGN SYSTEM

### 4.1 Palette colori

```css
:root {
  --color-primary: #1A9E75;      /* Teal principale — dal brochure MAC */
  --color-primary-dark: #0F6E56; /* Teal scuro — hover, accenti */
  --color-primary-light: #E1F5EE;/* Teal chiarissimo — sfondi sezioni */
  --color-accent: #E8593C;       /* Arancio/corallo — numeri chiave, badge */
  --color-accent-green: #3B9E22; /* Verde — badge secondari */
  --color-bg: #F7F7F5;           /* Sfondo principale (quasi bianco, caldo) */
  --color-bg-white: #FFFFFF;     /* Bianco puro — card, sezioni alternate */
  --color-text: #1A1A1A;         /* Testo principale */
  --color-text-muted: #6B6B6B;   /* Testo secondario */
  --color-border: #E5E5E0;       /* Bordi leggeri */
}
```

### 4.2 Tipografia

- **Font principale**: `Inter` (Google Fonts) — per tutto il corpo testo
- **Font titoli**: `Inter` weight 700/800 — titoli molto grandi e arieggiati
- **Dimensioni titoli hero**: 64–80px desktop, 36–48px mobile
- **Dimensioni titoli sezione**: 42–52px desktop
- **Corpo testo**: 17px, line-height 1.7
- **Label sezione** (sopra il titolo): 12px uppercase, letterspacing 0.1em, colore muted

### 4.3 Stile generale (ispirazione dagli screenshot forniti)

- Sfondo `#F7F7F5` (grigio caldo chiarissimo), non bianco puro
- Sezioni alternate: sfondo `#F7F7F5` / sfondo `#FFFFFF`
- Titoli molto grandi, peso 800, molto spazio intorno
- Pulsanti CTA: bordi arrotondati (border-radius 50px), colore teal
- Card: border-radius 16px, ombra leggera (`box-shadow: 0 2px 20px rgba(0,0,0,0.07)`)
- Numeri chiave (stats): font 64px bold, con label piccola sotto, separatore linea
- Icone: Lucide Icons (CDN), stroke 1.5px, non filled
- **Animazioni scroll**: elementi entrano con `opacity 0 → 1` + `translateY(20px → 0)` usando IntersectionObserver
- **Hero animato**: titolo grande con immagine "pill" (border-radius 100px) che appare inline nel testo, si espande con CSS animation (come negli screenshot Ampul forniti)
- Foto team: NON presenti (solo competenze)
- Immagini generiche farmaceutiche: sì (capsule, laboratorio) per le sezioni hero

### 4.4 Componenti standard

- **Navbar**: fissa in alto, logo a sinistra, menu al centro, switcher IT/EN + CTA a destra. Mobile: hamburger menu
- **Footer**: logo, link pagine, contatti, social, copyright
- **CTA Banner**: sezione colorata (teal) con headline e bottone, ripetuta più volte nelle pagine
- **Card servizio**: icona + titolo + testo + link
- **Badge numerico**: cerchio/badge colorato con numero grande + label
- **Accordion FAQ**: apertura/chiusura con animazione
- **Form contatto**: campi stilizzati, validazione JS, no backend (usa Netlify Forms)

---

## 5. PAGINE — CONTENUTO DETTAGLIATO

### 5.1 HOMEPAGE (`index.html`)

**Sezioni in ordine:**

1. **Hero** — Titolo grande (es. "Il tuo partner in Farmacovigilanza e Medical Affairs"), sottotitolo, CTA "Contattaci" + "Scopri i servizi". Immagine pill animata inline nel titolo (come screenshot Ampul). Sfondo: immagine capsule farmaceutiche in dissolvenza.

2. **Stats bar** — 4 numeri chiave orizzontali:
   - `+10` anni di esperienza (dal 2001)
   - `+10.000` casi processati (2023)
   - `0` PSUSA issues riportate da EMA
   - `+300` idee Kaizen annuali per il miglioramento

3. **"Perché sceglierci"** — Layout a 2 colonne: sinistra titolo grande + testo, destra lista caratteristiche con icone (come screenshot "What Makes Us Different" con linee verticali)

4. **Servizi (anteprima)** — 3 card principali: Farmacovigilanza, Informazione Medica, Consulenza Kaizen. Ogni card: icona + titolo + breve testo + link alla pagina servizi.

5. **Il metodo M.A.C.** — Sezione con sfondo teal chiaro. Obiettivi + Valori dal brochure. Layout: testo a sinistra, elemento grafico/cerchio a destra (come screenshot con cerchi concentrici e punti).

6. **Dati aggiuntivi** — Tabella/card con: +20% crescita team, +15.000 ICSRs, +50 aggregate reports.

7. **CTA Contatto #1** — Banner teal: "Pronti a supportare la vostra azienda. Contattaci oggi." + bottone.

8. **Blog/Rubriche (anteprima)** — Ultime 3 card dal blog.json con link a Instagram/LinkedIn.

9. **FAQ (anteprima)** — Accordion con le 3 domande più frequenti + link alla pagina FAQ completa.

10. **CTA Contatto #2** — Footer CTA prima del footer.

---

### 5.2 SERVIZI (`servizi.html`)

**Contenuto dal brochure:**

- **Farmacovigilanza** — EU-QPPV, PSMF, gestione database sicurezza, ICSRs/SAEs/SUSARs, Eudravigilance, XEVMPD (art. 57)
- **Rapporti periodici** — PSUR/PBRER, RMP, analisi segnali
- **Informazione Medica** — Supporto Responsabile Servizio Scientifico, D.Lgs. 219/2006 art. 126
- **Qualità e compliance** — Redazione SOP, ricerche bibliografiche, supporto audit e ispezioni
- **Materiali promozionali** — Chiarezza, accuratezza e conformità normativa materiali pubblicitari

**Layout**: Ogni servizio = sezione con titolo, testo descrittivo, lista punti con icone, eventuale CTA.

---

### 5.3 CHI SIAMO (`chi-siamo.html`)

**Sezioni:**

1. **Storia** — Dal 2001, evoluzione dell'azienda, missione.

2. **Valori** — Dal brochure: "Valorizziamo le persone: il nostro asset più importante. La loro curiosità ed energia sono il capitale intangibile che guida l'innovazione e la crescita sostenibile."

3. **Obiettivi** — "Assicurare l'eccellenza nella Farmacovigilanza, Informazione Medica e promuovere una cultura del Cambiamento in ottica Kaizen durante tutto il ciclo di vita del farmaco."

4. **Il Team — Competenze** (NO foto, NO nomi visibili — solo ruoli e competenze):
   - **Managing Director** — Leadership strategica, esperienza pluridecennale nel settore farmaceutico
   - **Strategic PV & QA PV Consultant** — Farmacovigilanza strategica, Quality Assurance PV
   - **IT Consultant / System Admin** — Consulente Microsoft certificato, gestione sistemi e infrastrutture IT per il settore farmaceutico
   - **Quality Assurance PV** — Professionista QA con esperienza in ambienti regolatori
   - **Data Protection** — GDPR, protezione dati in ambito farmaceutico
   - **Kaizen Promotion Officer** — Ingegnere esperto Lean Thinking e cultura Kaizen, miglioramento continuo dei processi
   - **Medical Expert Sr** (6 figure) — Team di medici, farmacisti e biologi con competenze cliniche e regolatorie
   - **Drug Safety Officer Sr** (5 figure) — Esperti senior farmacovigilanza
   - **Drug Safety Officer Jr** (7 figure) — Professionisti farmacovigilanza
   - **Data Entry Officer** (2 figure) — Gestione dati e sistemi

   **Layout**: Card per ogni ruolo/area con icona, titolo ruolo, descrizione competenze. Senza nomi o foto.

5. **Certificazioni** — Sezione placeholder con testo "In aggiornamento" per ISO 9001 e altre. Da completare.

6. **Partner** — Menzione collaborazioni con partner aziendali per formazione, materiali promozionali, Lean Thinking.

---

### 5.4 CALENDARIO EVENTI (`calendario.html`)

**Funzionamento tecnico:**
- Il file `data/eventi.json` contiene l'elenco degli eventi
- JavaScript legge il JSON e genera le card automaticamente
- Ogni card ha: titolo, data, organizzatore, descrizione breve, link iscrizione, bottone "Aggiungi al calendario" (scarica file `.ics`)
- Il file `.ics` è generato dinamicamente da JS (compatibile con Google Calendar, Apple Calendar, Outlook)
- Possibilità di "Salva su schermata home telefono" (PWA-ready con manifest.json)

**Struttura `eventi.json`:**
```json
[
  {
    "id": "001",
    "titolo": "Webinar EMA — Farmacovigilanza 2025",
    "titolo_en": "EMA Webinar — Pharmacovigilance 2025",
    "data": "2025-06-15",
    "ora": "14:00",
    "organizzatore": "EMA",
    "tipo": "webinar",
    "descrizione": "Aggiornamenti normativi sulla farmacovigilanza europea.",
    "descrizione_en": "Regulatory updates on European pharmacovigilance.",
    "link": "https://www.ema.europa.eu",
    "gratuito": true
  }
]
```

**Layout**: Filtri per tipo (webinar / corso / congresso), lista card con badge colorati per tipo, sezione "Prossimi eventi" in evidenza.

---

### 5.5 BLOG / RUBRICHE (`blog.html`)

**Funzionamento tecnico:**
- Il file `data/blog.json` contiene i post
- Ogni post ha: titolo, categoria/rubrica, immagine anteprima (caricata nella cartella `/img/blog/`), link al post originale su Instagram o LinkedIn, data
- JavaScript genera le card automaticamente

**Struttura `blog.json`:**
```json
[
  {
    "id": "001",
    "titolo": "Titolo del carosello",
    "titolo_en": "Carousel title",
    "rubrica": "Farmacovigilanza",
    "data": "2025-05-01",
    "immagine": "img/blog/post-001.jpg",
    "link_instagram": "https://www.instagram.com/p/...",
    "link_linkedin": "",
    "descrizione": "Breve descrizione del contenuto."
  }
]
```

**Layout**: Card con immagine anteprima + titolo + rubrica badge + icone social con link. Filtro per rubrica.

---

### 5.6 LAVORA CON NOI (`lavora-con-noi.html`)

**Sezioni:**
1. Headline + testo introduttivo sui valori del team
2. **Posizioni aperte** — Sezione con eventuali card posizioni (inizialmente: "Nessuna posizione aperta al momento, ma inviaci la tua candidatura spontanea")
3. **Candidatura spontanea** — Form con: Nome, Cognome, Email, Ruolo di interesse, Allegato CV (Netlify Forms), messaggio libero
4. CTA "Scopri il nostro team" → link a Chi siamo

---

### 5.7 CONTATTI (`contatti.html`)

**Tre form separati:**

1. **Form Clienti** — Azienda, Nome, Ruolo, Email, Telefono, Servizio di interesse (select), Messaggio
2. **Form Collaboratori/Partner** — Nome, Azienda, Email, Tipo di collaborazione, Messaggio
3. **Form Generico** — Nome, Email, Messaggio

**Informazioni di contatto:**
- Email: contactus@med-af-consulting.it / info@med-af-consulting.it
- Indirizzo: Corso Italia, 39 – Saronno (VA)
- Web: www.med-af-consulting.com

**Tutti i form**: gestiti con Netlify Forms (attributo `netlify` nell'HTML), nessun backend necessario.

---

### 5.8 FAQ (`faq.html`)

**Formato**: Accordion (domanda cliccabile che espande la risposta, animazione fluida).

**Categorie suggerite:**
- Farmacovigilanza e normativa
- I nostri servizi
- Come lavorare con noi
- Formazione e webinar

*(Contenuto delle domande da fornire — inserire placeholder per ora)*

---

## 6. ELEMENTI TRASVERSALI

### Navbar (tutte le pagine)
- Logo a sinistra (SVG placeholder)
- Menu: Home | Servizi | Chi siamo | Calendario | Blog | Contatti
- A destra: switcher `IT | EN` + bottone CTA "Contattaci" (teal, bordi arrotondati)
- Su scroll: navbar diventa bianca con ombra leggera (transition CSS)
- Mobile: hamburger menu con menu a tendina

### Footer (tutte le pagine)
- Logo + claim breve
- Colonne: Servizi | Azienda | Contatti
- Social: LinkedIn, Instagram
- Copyright + Privacy Policy + Cookie Policy
- Certificazioni (placeholder)

### Cookie Banner
- Banner semplice in basso: accetta / rifiuta
- Nessun tracciamento fino ad accettazione

### PWA / Mobile
- `manifest.json` per "Aggiungi a schermata home" (utile per il Calendario)
- Meta tag Open Graph per condivisione social

---

## 7. ANIMAZIONI E INTERATTIVITÀ

- **Scroll animations**: IntersectionObserver — ogni sezione entra con fade-up (opacity 0→1, translateY 30px→0, duration 0.6s, easing ease-out)
- **Hero pill image**: immagine inline nel titolo, si espande da 0 a dimensione piena con CSS keyframes (vedi screenshot Ampul)
- **Counter animation**: i numeri nelle stats (10.000, 300, ecc.) si contano da 0 al valore finale quando entrano nel viewport
- **Navbar scroll**: background transparent → white + box-shadow su scroll
- **FAQ accordion**: smooth height transition
- **Hover card**: leggero lift (`transform: translateY(-4px)`) con transition

---

## 8. SEO E PERFORMANCE

- Meta title e description personalizzati per ogni pagina (IT e EN)
- Heading gerarchici corretti (H1 unico per pagina, H2/H3 per sezioni)
- Alt text su tutte le immagini
- Lazy loading immagini (`loading="lazy"`)
- Font preload
- Minificazione CSS/JS (manuale o con script)
- `robots.txt` e `sitemap.xml` di base

---

## 9. TONO DELLA COMUNICAZIONE

- **Italiano**: professionale, diretto, caldo — non freddo né burocratico. "Voi" come forma di cortesia.
- **Inglese**: professional, confident, client-focused. Terminologia regolatoria corretta (EMA, ICH, GVP).
- Evitare gergo troppo tecnico nelle parti introduttive. Approfondire nei dettagli di servizio.
- Parole chiave: eccellenza, affidabilità, esperienza, approccio su misura, partnership.

---

## 10. ISTRUZIONI PER CLAUDE CODE

1. **Inizia** creando la struttura completa delle cartelle e tutti i file vuoti
2. **Costruisci** prima `css/style.css` con tutto il design system (variabili, reset, componenti base)
3. **Poi** `css/animations.css`
4. **Poi** `js/main.js` (navbar, scroll, language switcher)
5. **Poi** `index.html` (homepage completa, sezione per sezione)
6. **Poi** tutte le altre pagine IT
7. **Poi** le versioni EN (adattando i testi)
8. **Infine** `js/calendario.js`, `js/blog.js`, i file JSON di esempio
9. **Usa placeholder** per: logo (SVG con testo "MAC"), immagini (CSS colored blocks o servizio placeholder), loghi certificazioni
10. **Testa** aprendo `index.html` nel browser dopo ogni pagina completata
11. **Ogni file** deve essere completo e funzionante — non lasciare TODO o sezioni vuote
12. **Commenta** il codice CSS e JS in italiano per facilità di manutenzione futura

---

*Documento creato il 21 marzo 2026 — Medical Affairs Consulting*
*Riferimenti visivi: brochure MAC 2024, cartolina MAC EN, screenshot sito Ampul/Lunira (stile, non contenuto)*
