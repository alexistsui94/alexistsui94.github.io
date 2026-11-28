/* ==========================================================================
   Alexis Tsui — site behaviour
   --------------------------------------------------------------------------
   1. Mobile navigation (English labels)
   2. Sense-group pause marks: wrap the "/" and "//" in article English lines
      with a subtle span, so the reader can see where to pause while shadowing.
      Plain text is left untouched if JavaScript is disabled.
   ========================================================================== */

/* 1. Mobile navigation ---------------------------------------------------- */
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.site-nav');

if (toggle && nav) {
  const closeMenu = () => {
    nav.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.textContent = 'Menu';
  };

  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
    toggle.textContent = open ? 'Close' : 'Menu';
  });

  nav.addEventListener('click', (event) => {
    if (event.target.closest('a')) closeMenu();
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && nav.classList.contains('open')) {
      closeMenu();
      toggle.focus();
    }
  });

  // Close the menu when the user taps outside it.
  document.addEventListener('click', (event) => {
    if (nav.classList.contains('open') && !nav.contains(event.target) && !toggle.contains(event.target)) {
      closeMenu();
    }
  });
}

/* 2. Sense-group pause marks --------------------------------------------- */
// A slash counts as a pause mark only when it stands alone between spaces
// (or at the start/end of a line). This keeps URLs like https:// and paths
// such as /v1/weather untouched.
// "/" and "//" are RESERVED for pauses inside English reading lines.
// Short labels that need a separator use "·" instead, and any .en element
// that must keep a literal slash can opt out with data-no-pause.
const PAUSE_RE = /(^|\s)(\/{1,2})(?=\s|$)/g;
const SKIP_TAGS = new Set(['CODE', 'PRE', 'A', 'SCRIPT', 'STYLE', 'SPAN']);

document.querySelectorAll('.en').forEach((el) => {
  if (el.dataset.pausesDone || el.hasAttribute('data-no-pause')) return;

  const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
  const textNodes = [];
  while (walker.nextNode()) textNodes.push(walker.currentNode);

  textNodes.forEach((node) => {
    const text = node.nodeValue;
    if (!text || !text.includes('/')) return;
    if (node.parentElement && node.parentElement !== el && SKIP_TAGS.has(node.parentElement.tagName)) return;
    if (!PAUSE_RE.test(text)) { PAUSE_RE.lastIndex = 0; return; }
    PAUSE_RE.lastIndex = 0;

    const frag = document.createDocumentFragment();
    let last = 0;
    let match;
    while ((match = PAUSE_RE.exec(text)) !== null) {
      const lead = match[1];               // the whitespace before the mark
      const mark = match[2];               // "/" or "//"
      const start = match.index + lead.length;
      if (start > last) frag.appendChild(document.createTextNode(text.slice(last, start)));
      const span = document.createElement('span');
      span.className = mark === '//' ? 'pause pause-long' : 'pause';
      span.textContent = mark;
      frag.appendChild(span);
      last = start + mark.length;
    }
    if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
    if (frag.childNodes.length) node.parentNode.replaceChild(frag, node);
  });

  el.dataset.pausesDone = 'true';
});

