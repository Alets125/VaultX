/* ──────────────────────────────────────────────────────
   main.js — VaultX Catálogo de Videojuegos
   Handles:
    - Decode Text animation on the detail panel title
    - Game selection + detail panel population
────────────────────────────────────────────────────── */

/* Global state */
let currentGameId = null;

/* ── Decode Text Effect ───────────────────────────────────────────── */
function runDecodeText(el, text) {
  el.setAttribute('data-decode-text', text);
  el.innerHTML = '';

  const lines = text.split('|');
  lines.forEach((line, lineIdx) => {
    if (lineIdx > 0) {
      const br = document.createElement('span');
      br.className = 'decode-line-break';
      el.appendChild(br);
    }
    [...line].forEach(char => {
      if (char === ' ') {
        const sp = document.createElement('span');
        sp.className = 'decode-space';
        el.appendChild(sp);
      } else {
        const span = document.createElement('span');
        span.className = 'text-animation';
        span.textContent = char;
        el.appendChild(span);
      }
    });
  });

  const letters = el.querySelectorAll('.text-animation');
  letters.forEach((letter, i) => {
    setTimeout(() => {
      letter.classList.add('state-1');
      setTimeout(() => {
        letter.classList.add('state-2');
        setTimeout(() => {
          letter.classList.remove('state-1', 'state-2');
          letter.classList.add('state-3');
        }, 120);
      }, 120);
    }, i * 45);
  });
}

/* ── Stat bar animation ───────────────────────────────────────────── */
function animateStatBar(elId, value) {
  const el = document.getElementById(elId);
  if (!el) return;
  el.style.width = '0%';
  // Trigger reflow to restart animation
  void el.offsetWidth;
  requestAnimationFrame(() => {
    el.style.width = Math.min(100, Math.max(0, value)) + '%';
  });
}

/* ── Star rating renderer ─────────────────────────────────────────── */
function renderStars(rating) {
  const filled = '★'.repeat(rating);
  const empty  = '☆'.repeat(5 - rating);
  return `<span style="color:#f0d080">${filled}</span><span style="color:#3a2f5a">${empty}</span>`;
}

/* ── Select and display a game ────────────────────────────────────── */
function selectGame(gameId) {
  if (!window.GAMES_DATA || !GAMES_DATA.length) return;

  const game = GAMES_DATA.find(g => g.id === gameId);
  if (!game) return;

  // Update card selection style
  document.querySelectorAll('.game-card').forEach(card => card.classList.remove('selected'));
  const activeCard = document.getElementById('game-card-' + gameId);
  if (activeCard) activeCard.classList.add('selected');

  // Show detail panel
  const empty   = document.getElementById('detail-empty');
  const content = document.getElementById('detail-content');
  if (empty)   empty.style.display   = 'none';
  if (content) content.removeAttribute('hidden');

  // Cover image
  const coverEl = document.getElementById('detail-cover');
  if (coverEl) {
    coverEl.parentElement.style.display = 'block'; // Always show container
    if (game.cover_url) {
      coverEl.src = game.cover_url;
      coverEl.alt = game.title;
      coverEl.style.display = 'block';
    } else {
      coverEl.style.display = 'none';
    }
  }

  // Meta
  const badgeEl = document.getElementById('detail-category-badge');
  if (badgeEl) {
    badgeEl.textContent = game.category || 'Sin categoría';
    badgeEl.style.borderColor = game.cat_color;
    badgeEl.style.color       = game.cat_color;
  }
  const yearEl = document.getElementById('detail-year');
  if (yearEl) yearEl.textContent = game.year;

  // Saga
  const sagaEl = document.getElementById('detail-saga');
  if (sagaEl) sagaEl.textContent = game.saga ? '◈  SAGA: ' + game.saga.toUpperCase() : '';

  // Title with decode effect
  const titleEl = document.getElementById('detail-title');
  if (titleEl && game.id !== currentGameId) {
    runDecodeText(titleEl, game.title.toUpperCase());
  }

  // Rating
  const ratingEl = document.getElementById('detail-rating');
  if (ratingEl) ratingEl.innerHTML = renderStars(game.rating);

  // Stat bars
  animateStatBar('stat-strength',      game.strength);
  animateStatBar('stat-speed',         game.speed);
  animateStatBar('stat-horror',        game.horror);
  animateStatBar('stat-replayability', game.replayability);

  // Description
  const descEl = document.getElementById('detail-description');
  if (descEl) descEl.textContent = game.description;

  // Developer
  const devEl = document.getElementById('detail-developer');
  if (devEl) devEl.textContent = game.developer ? '◈ DESARROLLADOR: ' + game.developer.toUpperCase() : '';

  currentGameId = gameId;
}

/* ── On DOM ready ─────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  // Auto-select first game if available
  if (typeof GAMES_DATA !== 'undefined' && GAMES_DATA.length > 0) {
    selectGame(GAMES_DATA[0].id);
  }
});
