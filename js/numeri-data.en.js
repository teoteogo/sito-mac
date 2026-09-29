/* ==========================================================================
   DATA FOR THE "KEY FIGURES" SECTION (en/services.html)
   Team growth by area of expertise, in line with the org chart.
   English counterpart of js/numeri-data.js — keep both files in sync
   whenever the underlying figures change.
   ========================================================================== */
window.NUMERI_DATA = {
  clusters: [
    {
      id: 'pv',
      label: 'Operational Pharmacovigilance',
      ruoli: 'Senior DSO, Junior DSO, DEO',
      color: 'var(--color-primary-dark)'
    },
    {
      id: 'ma',
      label: 'Medical Affairs',
      ruoli: 'Senior Medical Expert',
      color: 'var(--color-primary)'
    },
    {
      id: 'qa',
      label: 'Quality & Compliance',
      ruoli: 'Senior QA PV, Junior QA PV',
      color: 'var(--color-accent)'
    },
    {
      id: 'support',
      label: 'Support functions',
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
