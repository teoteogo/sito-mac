# Bozze da confermare

File generato da `_src/build.py`: non modificarlo a mano. Elenca ogni blocco pubblicato come
**bozza** (marcatore giallo nelle pagine). I marcatori sono identici in inglese e in italiano.
Quando un dato è confermato, si toglie il `c.draft(...)` corrispondente in `_src/pages/` e si
rilancia il build. `python3 _src/build.py --release` fallisce finché resta anche una sola bozza.

## Tutte le pagine (footer)

- [ ] numero REA
- [ ] capitale sociale versato

## Il sistema PV (`pv-system.html` · `it/sistema-pv.html`)

- [ ] numero di titolari AIC con sistema completo: non compare nella company presentation
- [ ] durata tipica reale di una transizione
- [ ] adeguamento effettivo di contratti e procedure al Reg. (UE) 2025/1466; testo del regolamento da rileggere sulla fonte ufficiale
- [ ] perimetro del supporto in ispezione

## Servizi (`services.html` · `it/servizi.html`)

- [ ] servizio attivo? In caso contrario il riquadro va tolto
- [ ] servizio attivo? (supporto alla ricerca clinica)

## Chi siamo (`about.html` · `it/chi-siamo.html`)

- [ ] profilo dell EU-QPPV: testo da fornire; pubblicare il nome?
- [ ] profilo del responsabile QA: testo da fornire; pubblicare il nome?

## Contatti (`contact.html` · `it/contatti.html`)

- [ ] numero di centralino

## FAQ (`faq.html` · `it/faq.html`)

- [ ] sede dei dati e fornitori cloud
- [ ] ruolo esatto verso MHRA e Swissmedic; risposta da scrivere

## Numeri

- [x] Valori di `data/numeri.json` verificati sulla company presentation 2026.
- [ ] `full_systems` (titolari AIC con sistema completo) non compare nella presentazione: da confermare.
