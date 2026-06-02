(() => {
  const reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isMobile = () => window.innerWidth < 880;

  /* Word-split headline */
  const h1 = document.querySelector('.editorial h1[data-words]');
  if (h1 && !isMobile()) {
    const wrapped = h1.innerHTML.replace(/<em>/g, '<<EM>>').replace(/<\/em>/g, '<</EM>>');
    h1.innerHTML = wrapped.split(/(\s+)/).map(t => {
      if (!/\S/.test(t)) return t;
      const inner = t.replace(/<<EM>>/g, '<em>').replace(/<<\/EM>>/g, '</em>');
      return `<span class="w">${inner}</span>`;
    }).join('');
  }

  /* Loader fade + reveal hero chrome */
  window.addEventListener('load', () => {
    const loader = document.querySelector('.loader');
    if (loader) setTimeout(() => loader.classList.add('hidden'), 250);
    ['.wordmark','.portrait','.editorial','.portrait-plaque','.genrenav'].forEach(s => {
      const el = document.querySelector(s); if (el){ el.style.opacity = 1; el.style.transform = 'none'; }
    });
    if (!reduced) {
      document.querySelectorAll('.editorial h1 .w').forEach((el, i) => setTimeout(() => el.classList.add('in'), 600 + i * 90));
    } else {
      document.querySelectorAll('.editorial h1 .w').forEach(el => el.classList.add('in'));
    }
  });

  /* Custom cursor */
  if (!('ontouchstart' in window) && window.innerWidth >= 880) {
    const dot = document.querySelector('.cursor-dot');
    if (dot) {
      document.addEventListener('mousemove', e => { dot.style.left = e.clientX + 'px'; dot.style.top = e.clientY + 'px'; });
      document.querySelectorAll('a, button, .cta, .btn, .wa-pill').forEach(el => {
        el.addEventListener('mouseenter', () => dot.classList.add('hover'));
        el.addEventListener('mouseleave', () => dot.classList.remove('hover'));
      });
    }
  }

  /* Hero fade-out + portrait parallax on scroll */
  const hero = document.querySelector('.hero');
  const portrait = document.querySelector('.portrait');
  function onScroll() {
    if (reduced || isMobile()) return;
    const vh = window.innerHeight, scroll = window.scrollY;
    const heroFade = Math.max(0, Math.min(1, (scroll - 0.35 * vh) / (0.6 * vh)));
    if (hero){ hero.style.opacity = String(1 - heroFade); hero.style.pointerEvents = heroFade > 0.95 ? 'none' : 'auto'; }
    if (portrait) portrait.style.transform = `translate3d(0,${scroll * 0.05}px,0)`;
  }
  window.addEventListener('scroll', onScroll, { passive: true });

  /* Section reveal */
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('in'); });
  }, { threshold: 0.12, rootMargin: '0px 0px -80px 0px' });
  document.querySelectorAll('.reveal, .brass-rule').forEach(el => io.observe(el));
})();
