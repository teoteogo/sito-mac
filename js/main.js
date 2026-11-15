/**
 * MEDICAL AFFAIRS CONSULTING — main.js
 * Navbar, scroll animations, FAQ accordion, counter animation
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

      el.textContent = prefix + current.toLocaleString(document.documentElement.lang === 'it' ? 'it-IT' : 'en-GB') + suffix;

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
   8. SMOOTH SCROLL — per link interni (#anchor)
   ============================================================ */
document.querySelectorAll('a[href^="#"]:not([href="#"])').forEach(anchor => {
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
