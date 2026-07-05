/**
 * MEDICAL AFFAIRS CONSULTING — main.js
 * Navbar, scroll animations, language switcher, FAQ accordion,
 * counter animation, cookie banner
 */

/* ============================================================
   1. NAVBAR — scroll effect + hamburger menu
   ============================================================ */
(function initNavbar() {
  const navbar = document.querySelector('.navbar');
  if (!navbar) return;

  // Cambio sfondo su scroll
  function updateNavbar() {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', updateNavbar, { passive: true });
  updateNavbar(); // check iniziale

  // Hamburger menu mobile
  const hamburger = document.querySelector('.navbar__hamburger');
  const mobileMenu = document.querySelector('.navbar__mobile');

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', function () {
      const isOpen = mobileMenu.classList.toggle('open');
      hamburger.setAttribute('aria-expanded', isOpen);
      // Previeni scroll del body quando il menu è aperto
      document.body.style.overflow = isOpen ? 'hidden' : '';

      // Animazione hamburger → X
      const spans = hamburger.querySelectorAll('span');
      if (isOpen) {
        spans[0].style.transform = 'translateY(7px) rotate(45deg)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'translateY(-7px) rotate(-45deg)';
      } else {
        spans[0].style.transform = '';
        spans[1].style.opacity = '';
        spans[2].style.transform = '';
      }
    });

    // Chiudi menu cliccando su un link
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        document.body.style.overflow = '';
        const spans = hamburger.querySelectorAll('span');
        spans[0].style.transform = '';
        spans[1].style.opacity = '';
        spans[2].style.transform = '';
      });
    });
  }

  // Evidenzia la voce di menu attiva in base all'URL
  const currentPath = window.location.pathname;
  document.querySelectorAll('.navbar__menu a, .navbar__mobile a').forEach(link => {
    const href = link.getAttribute('href');
    if (href && (currentPath.endsWith(href) || currentPath === href)) {
      link.classList.add('active');
    }
    // Caso speciale: homepage
    if ((href === 'index.html' || href === '/' || href === '../index.html') &&
        (currentPath === '/' || currentPath.endsWith('/') || currentPath.endsWith('index.html'))) {
      link.classList.add('active');
    }
  });
})();


/* ============================================================
   2. SCROLL REVEAL — IntersectionObserver
   Aggiunge la classe .visible agli elementi .reveal quando
   entrano nel viewport
   ============================================================ */
(function initReveal() {
  const revealClasses = [
    '.reveal',
    '.reveal-fade',
    '.reveal-left',
    '.reveal-right',
    '.reveal-scale'
  ];

  const elements = document.querySelectorAll(revealClasses.join(', '));
  if (!elements.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          // Una volta mostrato, non serve più osservare
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px'
    }
  );

  elements.forEach(el => observer.observe(el));
})();


/* ============================================================
   3. COUNTER ANIMATION — Conta da 0 al valore target
   Usa l'attributo data-count sull'elemento .stats-bar__number
   ============================================================ */
(function initCounters() {
  const counters = document.querySelectorAll('[data-count]');
  if (!counters.length) return;

  function animateCounter(el) {
    const target = parseInt(el.getAttribute('data-count'), 10);
    const prefix = el.getAttribute('data-prefix') || '';
    const suffix = el.getAttribute('data-suffix') || '';
    const duration = 1800; // ms
    const startTime = performance.now();

    function update(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      // Easing ease-out
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.round(eased * target);

      el.textContent = prefix + current.toLocaleString('it-IT') + suffix;

      if (progress < 1) {
        requestAnimationFrame(update);
      }
    }

    requestAnimationFrame(update);
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.3 }
  );

  counters.forEach(el => observer.observe(el));
})();


/* ============================================================
   4. FAQ ACCORDION
   ============================================================ */
(function initAccordion() {
  const items = document.querySelectorAll('.accordion__item');
  if (!items.length) return;

  items.forEach(item => {
    const trigger = item.querySelector('.accordion__trigger');
    if (!trigger) return;

    trigger.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');

      // Chiudi tutti gli altri (solo un accordion aperto alla volta)
      items.forEach(other => {
        if (other !== item) {
          other.classList.remove('open');
          const otherTrigger = other.querySelector('.accordion__trigger');
          if (otherTrigger) otherTrigger.setAttribute('aria-expanded', 'false');
        }
      });

      // Toggle corrente
      item.classList.toggle('open', !isOpen);
      trigger.setAttribute('aria-expanded', !isOpen);
    });
  });
})();


/* ============================================================
   5. COOKIE BANNER
   ============================================================ */
(function initCookieBanner() {
  const banner = document.querySelector('.cookie-banner');
  if (!banner) return;

  // Mostra solo se non è stato già accettato/rifiutato
  if (!localStorage.getItem('mac-cookie-consent')) {
    banner.classList.add('visible');
  }

  const btnAccept = banner.querySelector('[data-cookie-accept]');
  const btnDecline = banner.querySelector('[data-cookie-decline]');

  if (btnAccept) {
    btnAccept.addEventListener('click', () => {
      localStorage.setItem('mac-cookie-consent', 'accepted');
      banner.classList.remove('visible');
    });
  }

  if (btnDecline) {
    btnDecline.addEventListener('click', () => {
      localStorage.setItem('mac-cookie-consent', 'declined');
      banner.classList.remove('visible');
    });
  }
})();


/* ============================================================
   6. CONTACT TABS — Switcher tra i 3 form contatti
   ============================================================ */
(function initContactTabs() {
  const tabs = document.querySelectorAll('.contact-tab');
  const panels = document.querySelectorAll('.contact-form-panel');
  if (!tabs.length) return;

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const target = tab.getAttribute('data-tab');

      tabs.forEach(t => t.classList.remove('active'));
      panels.forEach(p => p.classList.remove('active'));

      tab.classList.add('active');
      const panel = document.getElementById(target);
      if (panel) panel.classList.add('active');
    });
  });
})();


/* ============================================================
   7. FORM NETLIFY — Feedback di invio
   ============================================================ */
(function initForms() {
  document.querySelectorAll('form[data-netlify]').forEach(form => {
    form.addEventListener('submit', function (e) {
      // Non preveniamo il submit — Netlify gestisce il tutto lato server
      // Ma mostriamo un messaggio di successo dopo il reindirizzamento
      // Se la pagina ha un parametro ?success=true, mostra il messaggio
    });
  });

  // Mostra messaggio di successo se siamo tornati dalla redirect Netlify
  if (window.location.search.includes('success=true')) {
    const msg = document.querySelector('.form-success');
    if (msg) msg.classList.add('visible');
  }
})();


/* ============================================================
   8. SMOOTH SCROLL — per link interni (#anchor)
   ============================================================ */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      const navbarHeight = parseInt(
        getComputedStyle(document.documentElement).getPropertyValue('--navbar-height')
      ) || 76;
      const top = target.getBoundingClientRect().top + window.scrollY - navbarHeight - 16;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});


/* ============================================================
   9. SCROLL PROGRESS BAR (opzionale)
   ============================================================ */
(function initScrollProgress() {
  const bar = document.querySelector('.scroll-progress');
  if (!bar) return;

  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    bar.style.width = pct + '%';
  }, { passive: true });
})();


/* ============================================================
   10. LANGUAGE SWITCHER — Gestione link IT/EN
   Aggiunge la classe active al link della lingua corrente
   ============================================================ */
(function initLangSwitcher() {
  const isEnglish = window.location.pathname.includes('/en/');
  document.querySelectorAll('.lang-switcher a').forEach(link => {
    const isEnLink = link.getAttribute('href')?.includes('/en/') ||
                     link.textContent.trim() === 'EN';
    const isItLink = link.textContent.trim() === 'IT';

    link.classList.remove('active');
    if (isEnglish && isEnLink) link.classList.add('active');
    if (!isEnglish && isItLink) link.classList.add('active');
  });
})();
