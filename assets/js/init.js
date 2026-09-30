// Chargé dans <head> : applique le thème mémorisé avant l'affichage (évite un flash de couleur)
document.documentElement.classList.add('js');
try { var t = localStorage.getItem('theme'); if (t) document.documentElement.dataset.theme = t; } catch (e) {}
