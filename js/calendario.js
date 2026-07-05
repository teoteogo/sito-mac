/**
 * MEDICAL AFFAIRS CONSULTING — calendario.js
 * Legge data/eventi.json, genera le card degli eventi,
 * permette il download .ics per Google/Apple/Outlook Calendar
 */

const EVENTI_URL = '../data/eventi.json';
const IS_EN = window.location.pathname.includes('/en/');

/* ============================================================
   Utility — Formattazione date
   ============================================================ */
function formatData(dateStr, locale) {
  const date = new Date(dateStr + 'T00:00:00');
  return date.toLocaleDateString(locale || (IS_EN ? 'en-GB' : 'it-IT'), {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  });
}

function getDay(dateStr) {
  return new Date(dateStr + 'T00:00:00').getDate();
}

function getMonth(dateStr) {
  const date = new Date(dateStr + 'T00:00:00');
  return date.toLocaleDateString(IS_EN ? 'en-GB' : 'it-IT', { month: 'short' }).toUpperCase();
}

function getYear(dateStr) {
  return new Date(dateStr + 'T00:00:00').getFullYear();
}

/* ============================================================
   Generazione file .ics
   ============================================================ */
function generaICS(evento) {
  const dataInizio = evento.data.replace(/-/g, '');
  // Calcola la data di fine (stesso giorno + 1h o giorno successivo se tutto il giorno)
  const dateObj = new Date(evento.data + 'T00:00:00');
  dateObj.setDate(dateObj.getDate() + 1);
  const dataFine = dateObj.toISOString().slice(0, 10).replace(/-/g, '');

  const titolo = IS_EN ? (evento.titolo_en || evento.titolo) : evento.titolo;
  const descrizione = IS_EN ? (evento.descrizione_en || evento.descrizione) : evento.descrizione;
  const ora = evento.ora || '09:00';
  const oraFormatted = ora.replace(':', '') + '00';

  const icsContent = [
    'BEGIN:VCALENDAR',
    'VERSION:2.0',
    'PRODID:-//Medical Affairs Consulting//Calendario MAC//IT',
    'CALSCALE:GREGORIAN',
    'METHOD:PUBLISH',
    'BEGIN:VEVENT',
    `UID:mac-evento-${evento.id}@med-af-consulting.it`,
    `DTSTAMP:${new Date().toISOString().replace(/[-:]/g, '').slice(0, 15)}Z`,
    `DTSTART:${dataInizio}T${oraFormatted}`,
    `DTEND:${dataInizio}T${String(parseInt(oraFormatted.slice(0,2)) + 1).padStart(2,'0')}${oraFormatted.slice(2)}`,
    `SUMMARY:${titolo}`,
    `DESCRIPTION:${descrizione || ''}`,
    `ORGANIZER;CN=${evento.organizzatore}:MAILTO:info@med-af-consulting.it`,
    `URL:${evento.link || ''}`,
    'END:VEVENT',
    'END:VCALENDAR'
  ].join('\r\n');

  const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `evento-mac-${evento.id}.ics`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

/* ============================================================
   Badge tipo evento
   ============================================================ */
function getBadge(tipo) {
  const tipi = {
    webinar: { label: IS_EN ? 'Webinar' : 'Webinar', cls: 'badge--primary' },
    corso: { label: IS_EN ? 'Course' : 'Corso', cls: 'badge--accent' },
    congresso: { label: IS_EN ? 'Congress' : 'Congresso', cls: 'badge--green' },
    convegno: { label: IS_EN ? 'Convention' : 'Convegno', cls: 'badge--green' },
  };
  const t = tipi[tipo] || { label: tipo, cls: 'badge--gray' };
  return `<span class="badge ${t.cls}">${t.label}</span>`;
}

/* ============================================================
   Generazione card evento HTML
   ============================================================ */
function creaCardEvento(evento) {
  const titolo = IS_EN ? (evento.titolo_en || evento.titolo) : evento.titolo;
  const descrizione = IS_EN ? (evento.descrizione_en || evento.descrizione) : evento.descrizione;
  const dataFormatted = formatData(evento.data);
  const giorno = getDay(evento.data);
  const mese = getMonth(evento.data);
  const gratuito = evento.gratuito;

  const labelIscrizione = IS_EN ? 'Register' : 'Iscriviti';
  const labelCalendario = IS_EN ? 'Add to calendar' : 'Aggiungi al calendario';
  const labelGratuito = IS_EN ? 'Free' : 'Gratuito';

  return `
    <article class="event-card reveal" data-tipo="${evento.tipo}" data-id="${evento.id}">
      <div class="event-card__date-block">
        <span class="event-card__day">${giorno}</span>
        <span class="event-card__month">${mese}</span>
      </div>
      <div class="event-card__body">
        <div class="event-card__meta">
          ${getBadge(evento.tipo)}
          ${gratuito ? `<span class="badge badge--green">${labelGratuito}</span>` : ''}
        </div>
        <h3 class="event-card__title">${titolo}</h3>
        <p class="event-card__organizer">
          <strong>${IS_EN ? 'Organiser' : 'Organizzatore'}:</strong> ${evento.organizzatore} · ${dataFormatted}${evento.ora ? ' · ' + evento.ora : ''}
        </p>
        <p class="event-card__desc">${descrizione}</p>
        <div class="event-card__actions">
          ${evento.link ? `<a href="${evento.link}" target="_blank" rel="noopener" class="btn btn--primary btn--sm">${labelIscrizione}</a>` : ''}
          <button class="btn btn--outline btn--sm" onclick="generaICS(window.__eventi.find(e => e.id === '${evento.id}'))">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            ${labelCalendario}
          </button>
        </div>
      </div>
    </article>
  `;
}

/* ============================================================
   Filtri per tipo evento
   ============================================================ */
function initFiltri(tipi) {
  const container = document.querySelector('.filters');
  if (!container) return;

  const labelTutti = IS_EN ? 'All' : 'Tutti';
  const tipiUnici = [...new Set(tipi)];

  const tipiLabel = {
    webinar: IS_EN ? 'Webinar' : 'Webinar',
    corso: IS_EN ? 'Courses' : 'Corsi',
    congresso: IS_EN ? 'Congresses' : 'Congressi',
    convegno: IS_EN ? 'Conventions' : 'Convegni',
  };

  container.innerHTML = `
    <button class="filter-btn active" data-filter="tutti">${labelTutti}</button>
    ${tipiUnici.map(t => `<button class="filter-btn" data-filter="${t}">${tipiLabel[t] || t}</button>`).join('')}
  `;

  container.addEventListener('click', e => {
    const btn = e.target.closest('.filter-btn');
    if (!btn) return;

    container.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const filter = btn.getAttribute('data-filter');
    document.querySelectorAll('.event-card').forEach(card => {
      if (filter === 'tutti' || card.getAttribute('data-tipo') === filter) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  });
}

/* ============================================================
   Caricamento ed inizializzazione
   ============================================================ */
async function initCalendario() {
  const container = document.getElementById('eventi-container');
  const prossimi = document.getElementById('prossimi-container');
  if (!container) return;

  // Stato caricamento
  container.innerHTML = `
    <div class="loading-state">
      <div class="spinner"></div>
      <span>${IS_EN ? 'Loading events...' : 'Caricamento eventi...'}</span>
    </div>
  `;

  try {
    const res = await fetch(EVENTI_URL);
    if (!res.ok) throw new Error('Errore caricamento');
    const eventi = await res.json();

    // Rendi disponibile globalmente per il download .ics
    window.__eventi = eventi;

    // Ordina per data
    eventi.sort((a, b) => new Date(a.data) - new Date(b.data));

    // Separa eventi futuri e passati
    const oggi = new Date();
    oggi.setHours(0, 0, 0, 0);
    const futuri = eventi.filter(e => new Date(e.data + 'T00:00:00') >= oggi);
    const passati = eventi.filter(e => new Date(e.data + 'T00:00:00') < oggi);

    // Popola filtri con i tipi disponibili
    initFiltri(eventi.map(e => e.tipo));

    // Sezione prossimi eventi in evidenza
    if (prossimi && futuri.length > 0) {
      prossimi.innerHTML = futuri.slice(0, 3).map(creaCardEvento).join('');
    }

    // Lista completa
    if (futuri.length === 0 && passati.length === 0) {
      container.innerHTML = `
        <div class="loading-state">
          <p>${IS_EN ? 'No events available at the moment.' : 'Nessun evento disponibile al momento.'}</p>
        </div>
      `;
    } else {
      let html = '';

      if (futuri.length > 0) {
        const titProssimi = IS_EN ? 'Upcoming Events' : 'Prossimi eventi';
        html += `<h3 class="reveal mb-4" style="margin-bottom:1.5rem">${titProssimi}</h3>`;
        html += futuri.map(creaCardEvento).join('');
      }

      if (passati.length > 0) {
        const titPassati = IS_EN ? 'Past Events' : 'Eventi passati';
        html += `<h3 class="reveal" style="margin:3rem 0 1.5rem;color:var(--color-text-muted)">${titPassati}</h3>`;
        html += passati.map(e => {
          const card = creaCardEvento(e);
          return card.replace('<article class="event-card', '<article class="event-card" style="opacity:0.6"');
        }).join('');
      }

      container.innerHTML = html;

      // Ri-inizializza animazioni scroll sulle nuove card
      if (typeof IntersectionObserver !== 'undefined') {
        const obs = new IntersectionObserver(entries => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              entry.target.classList.add('visible');
              obs.unobserve(entry.target);
            }
          });
        }, { threshold: 0.1 });
        container.querySelectorAll('.reveal').forEach(el => obs.observe(el));
      }
    }

  } catch (err) {
    console.error('Errore calendario:', err);
    container.innerHTML = `
      <div class="loading-state">
        <p style="color:var(--color-accent)">${IS_EN ? 'Error loading events. Please try again later.' : 'Errore nel caricamento degli eventi. Riprova più tardi.'}</p>
      </div>
    `;
  }
}

// Avvia quando il DOM è pronto
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initCalendario);
} else {
  initCalendario();
}
