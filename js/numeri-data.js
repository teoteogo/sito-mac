/* ==========================================================================
   DATI SEZIONE "I NUMERI" (servizi.html)
   Crescita del team per area di competenza, in linea con l'organigramma.
   - "clusters": le aree mostrate nel grafico (colore, etichetta, ruoli
     che la compongono — i ruoli sono solo testo informativo in legenda)
   - "serie": un oggetto per anno con il numero di persone per ciascuna
     area (chiave = "id" del cluster corrispondente)
   Aggiungi o togli righe in "serie" per aggiungere/togliere anni.
   ========================================================================== */
window.NUMERI_DATA = {
  clusters: [
    {
      id: 'pv',
      label: 'Farmacovigilanza operativa',
      ruoli: 'DSO Senior, DSO Junior, DEO',
      color: 'var(--color-primary-dark)'
    },
    {
      id: 'ma',
      label: 'Medical Affairs',
      ruoli: 'Medical Expert Senior',
      color: 'var(--color-primary)'
    },
    {
      id: 'qa',
      label: 'Qualità & Compliance',
      ruoli: 'QA PV Senior, QA PV Junior',
      color: 'var(--color-accent)'
    },
    {
      id: 'support',
      label: 'Funzioni di supporto',
      ruoli: 'IT, KPO Engineer, Data Protection',
      color: 'var(--color-muted)'
    }
  ],
  serie: [
    { anno: 2019, valori: { pv: 3,  ma: 4, qa: 1, support: 2 } },
    { anno: 2020, valori: { pv: 5,  ma: 4, qa: 1, support: 2 } },
    { anno: 2021, valori: { pv: 7,  ma: 4, qa: 1, support: 2 } },
    { anno: 2022, valori: { pv: 9,  ma: 4, qa: 1, support: 2 } },
    { anno: 2023, valori: { pv: 12, ma: 4, qa: 1, support: 2 } },
    { anno: 2024, valori: { pv: 14, ma: 5, qa: 1, support: 3 } },
    { anno: 2025, valori: { pv: 15, ma: 6, qa: 2, support: 3 } },
    { anno: 2026, valori: { pv: 17, ma: 7, qa: 2, support: 3 } }
  ]
};
