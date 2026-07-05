/**
 * MEDICAL AFFAIRS CONSULTING — blog.js
 * Legge data/blog.json, genera le card dei post del blog,
 * gestisce i filtri per rubrica
 */

const IS_EN_BLOG = window.location.pathname.includes('/en/');
const BLOG_URL = IS_EN_BLOG ? '../data/blog.json' : 'data/blog.json';

/* ============================================================
   Formattazione data
   ============================================================ */
function formatDataBlog(dateStr) {
  const date = new Date(dateStr + 'T00:00:00');
  return date.toLocaleDateString(IS_EN_BLOG ? 'en-GB' : 'it-IT', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  });
}

/* ============================================================
   Generazione card blog HTML
   ============================================================ */
function creaCardBlog(post) {
  const titolo = IS_EN_BLOG ? (post.titolo_en || post.titolo) : post.titolo;
  const descrizione = IS_EN_BLOG ? (post.descrizione_en || post.descrizione) : post.descrizione;
  const dataFormatted = formatDataBlog(post.data);
  const rubrica = post.rubrica;

  // Immagine o placeholder
  let imgHTML;
  if (post.immagine) {
    imgHTML = `<img src="${IS_EN_BLOG ? '../' + post.immagine : post.immagine}"
                    alt="${titolo}"
                    class="blog-card__image"
                    loading="lazy">`;
  } else {
    imgHTML = `
      <div class="blog-card__image-placeholder">
        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
          <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
          <polyline points="14 2 14 8 20 8"></polyline>
          <line x1="16" y1="13" x2="8" y2="13"></line>
          <line x1="16" y1="17" x2="8" y2="17"></line>
          <polyline points="10 9 9 9 8 9"></polyline>
        </svg>
      </div>
    `;
  }

  // Link social
  const socialLinks = [];
  if (post.link_instagram) {
    socialLinks.push(`
      <a href="${post.link_instagram}" target="_blank" rel="noopener" title="Instagram" aria-label="Leggi su Instagram">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
          <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
          <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
        </svg>
      </a>
    `);
  }
  if (post.link_linkedin) {
    socialLinks.push(`
      <a href="${post.link_linkedin}" target="_blank" rel="noopener" title="LinkedIn" aria-label="Leggi su LinkedIn">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
          <rect x="2" y="9" width="4" height="12"></rect>
          <circle cx="4" cy="4" r="2"></circle>
        </svg>
      </a>
    `);
  }

  const labelLeggi = IS_EN_BLOG ? 'Read post' : 'Leggi il post';

  return `
    <article class="blog-card reveal" data-rubrica="${rubrica}">
      ${imgHTML}
      <div class="blog-card__body">
        <div class="blog-card__meta">
          <span class="badge badge--primary">${rubrica}</span>
          <span class="blog-card__date">${dataFormatted}</span>
        </div>
        <h3 class="blog-card__title">${titolo}</h3>
        ${descrizione ? `<p class="blog-card__desc">${descrizione}</p>` : ''}
        <div class="blog-card__footer">
          ${socialLinks.length > 0 ? `
            <div class="blog-card__social">
              ${socialLinks.join('')}
            </div>
          ` : ''}
          ${(post.link_instagram || post.link_linkedin) ? `
            <a href="${post.link_instagram || post.link_linkedin}"
               target="_blank" rel="noopener"
               class="card__link">
              ${labelLeggi}
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
          ` : ''}
        </div>
      </div>
    </article>
  `;
}

/* ============================================================
   Filtri per rubrica
   ============================================================ */
function initFiltriBlog(rubriche) {
  const container = document.querySelector('.filters');
  if (!container) return;

  const labelTutte = IS_EN_BLOG ? 'All' : 'Tutte le rubriche';
  const rubricheUniche = [...new Set(rubriche)];

  container.innerHTML = `
    <button class="filter-btn active" data-filter="tutte">${labelTutte}</button>
    ${rubricheUniche.map(r => `<button class="filter-btn" data-filter="${r}">${r}</button>`).join('')}
  `;

  container.addEventListener('click', e => {
    const btn = e.target.closest('.filter-btn');
    if (!btn) return;

    container.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const filter = btn.getAttribute('data-filter');
    document.querySelectorAll('.blog-card').forEach(card => {
      if (filter === 'tutte' || card.getAttribute('data-rubrica') === filter) {
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
async function initBlog() {
  const container = document.getElementById('blog-container');
  if (!container) return;

  container.innerHTML = `
    <div class="loading-state">
      <div class="spinner"></div>
      <span>${IS_EN_BLOG ? 'Loading posts...' : 'Caricamento post...'}</span>
    </div>
  `;

  try {
    const res = await fetch(BLOG_URL);
    if (!res.ok) throw new Error('Errore caricamento');
    const posts = await res.json();

    // Ordina per data (più recenti prima)
    posts.sort((a, b) => new Date(b.data) - new Date(a.data));

    // Inizializza filtri
    initFiltriBlog(posts.map(p => p.rubrica));

    if (posts.length === 0) {
      container.innerHTML = `
        <div class="loading-state">
          <p>${IS_EN_BLOG ? 'No posts available yet.' : 'Nessun post disponibile al momento.'}</p>
        </div>
      `;
      return;
    }

    container.innerHTML = posts.map(creaCardBlog).join('');

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

  } catch (err) {
    console.error('Errore blog:', err);
    container.innerHTML = `
      <div class="loading-state">
        <p style="color:var(--color-accent)">${IS_EN_BLOG ? 'Error loading posts.' : 'Errore nel caricamento dei post.'}</p>
      </div>
    `;
  }
}

/* ============================================================
   Carica anteprime blog (usato nella homepage — max 3 post)
   ============================================================ */
async function initBlogPreview(containerId, maxItems = 3) {
  const container = document.getElementById(containerId);
  if (!container) return;

  try {
    const res = await fetch(BLOG_URL);
    if (!res.ok) throw new Error('Errore');
    const posts = await res.json();

    posts.sort((a, b) => new Date(b.data) - new Date(a.data));
    const preview = posts.slice(0, maxItems);
    container.innerHTML = preview.map(creaCardBlog).join('');

    // Animazioni
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
  } catch (err) {
    console.error('Errore blog preview:', err);
  }
}

// Avvia quando il DOM è pronto
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    // Pagina blog completa
    if (document.getElementById('blog-container')) {
      initBlog();
    }
    // Anteprima homepage
    if (document.getElementById('blog-preview')) {
      initBlogPreview('blog-preview', 3);
    }
  });
} else {
  if (document.getElementById('blog-container')) {
    initBlog();
  }
  if (document.getElementById('blog-preview')) {
    initBlogPreview('blog-preview', 3);
  }
}
