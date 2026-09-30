// Scripts du site : thème clair / sombre, apparition au défilement, formulaire de contact.
// Aucun script n'est écrit dans les pages elles-mêmes, ce qui permet une politique de sécurité (CSP) stricte.

// Thème clair / sombre
(function () {
  var root = document.documentElement, btn = document.getElementById('theme');
  if (!btn) return;
  btn.addEventListener('click', function () {
    var dark = root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
    root.dataset.theme = dark ? 'light' : 'dark';
    try { localStorage.setItem('theme', root.dataset.theme); } catch (e) {}
  });
})();

// Apparition douce au défilement (sans dépendance à IntersectionObserver)
(function () {
  var els = [].slice.call(document.querySelectorAll('.reveal'));
  function showAll() { els.forEach(function (el) { el.classList.add('in'); }); els = []; }
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) { showAll(); return; }
  function check() {
    var limit = window.innerHeight * 0.95;
    els = els.filter(function (el) {
      if (el.getBoundingClientRect().top < limit) { el.classList.add('in'); return false; }
      return true;
    });
    if (!els.length) { removeEventListener('scroll', check); removeEventListener('resize', check); }
  }
  addEventListener('scroll', check, { passive: true });
  addEventListener('resize', check);
  check();
  // Filet de sécurité : tout le contenu reste lisible même si l'animation ne se déclenche pas
  setTimeout(function () { if (document.hidden) showAll(); }, 1500);
  document.addEventListener('visibilitychange', check);
})();

// Formulaire de contact (Web3Forms). Les textes viennent des attributs data-* du formulaire.
(function () {
  var form = document.getElementById('contact-form');
  if (!form || !window.fetch) return; // sans JavaScript, le formulaire est envoyé normalement
  var btn = form.querySelector('button'), statut = form.querySelector('.form-status'), label = btn.firstChild.nodeValue;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    btn.disabled = true; btn.firstChild.nodeValue = form.dataset.envoi;
    statut.className = 'form-status'; statut.textContent = '';
    var donnees = {}; new FormData(form).forEach(function (v, k) { donnees[k] = v; });
    donnees.name = (donnees.prenom + ' ' + donnees.nom).trim(); // nom de l'expéditeur dans l'e-mail reçu
    fetch(form.action, { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(donnees) })
      .then(function (r) { return r.json(); })
      .then(function (j) {
        if (!j.success) throw new Error(j.message);
        form.reset(); statut.className = 'form-status ok'; statut.textContent = form.dataset.ok;
      })
      .catch(function () {
        statut.className = 'form-status erreur';
        var lien = document.createElement('a');
        lien.href = 'mailto:' + form.dataset.email; lien.textContent = form.dataset.email;
        statut.textContent = form.dataset.erreur + ' ';
        statut.appendChild(lien); statut.appendChild(document.createTextNode('.'));
      })
      .then(function () { btn.disabled = false; btn.firstChild.nodeValue = label; });
  });
})();
