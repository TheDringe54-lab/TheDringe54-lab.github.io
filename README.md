# ethanledorze.fr

Portfolio d'**Ethan Ledorze**, assistant informaticien en Gendarmerie, en recherche d'un poste de technicien support ou de technicien / administrateur systèmes & réseaux en Normandie (Eure, Seine-Maritime).

**Site en ligne : https://ethanledorze.fr**

Contact : contact@ethanledorze.fr · [LinkedIn](https://www.linkedin.com/in/ethan-ledorze-32000025a/)

---

## Modifier le contenu

Le contenu se modifie depuis un **panneau d'administration**, sans toucher au code :

1. Aller sur **https://app.pagescms.org** et se connecter avec GitHub.
2. Ouvrir ce dépôt, puis **Contenu du site**, **Mentions légales** ou **Réglages**.
3. Modifier les textes, les listes ou la photo, puis cliquer sur **Save**.
4. Le site en ligne est mis à jour en une ou deux minutes.

Dans les champs de texte, `**mot**` s'affiche en **gras** et `*mot*` en *italique*.

On peut aussi modifier directement le fichier [`_data/contenu.yml`](_data/contenu.yml) sur GitHub.

## Structure du dépôt

| Fichier | Rôle |
|---|---|
| `_data/contenu.yml` | Textes du site : en-tête, chiffres clés, profil, compétences, parcours, FAQ, contact |
| `_data/veille.json` | Articles de la rubrique « Veille », mis à jour automatiquement (ne pas modifier à la main) |
| `_data/veille_sources.json` | Liste des flux RSS utilisés pour la veille |
| `scripts/veille.py`, `.github/workflows/veille.yml` | Script et robot de mise à jour quotidienne de la veille |
| `_data/reglages.yml` | Réglages du site (clé du formulaire de contact) |
| `_data/ui.yml` | Textes fixes de l'interface (menu, boutons, titres de sections) |
| `index.html` | Page d'accueil |
| `en/index.html` | Redirige l'ancienne adresse de la version anglaise vers l'accueil |
| `mentions-legales.md` | Page des mentions légales |
| `404.html` | Page affichée quand une adresse n'existe pas |
| `_layouts/` | Gabarits : `base` (en-tête, menu, pied de page), `portfolio` (page d'accueil), `page` (pages de texte) |
| `_includes/head.html` | Balises `<head>` : référencement, aperçu de partage, icônes, données structurées |
| `_includes/icone.html` | Les icônes des compétences |
| `_includes/md.html` | Gère le gras et l'italique dans les textes |
| `assets/css/style.css` | Styles du site |
| `assets/fonts/` | Polices hébergées sur le site |
| `assets/` | Photo de profil, image d'aperçu de partage (`og-image-fr.png`), favicons |
| `robots.txt` | Indique aux moteurs de recherche où trouver le plan du site |
| `.pages.yml` | Configuration du panneau Pages CMS |
| `_config.yml` | Configuration de Jekyll |
| `CNAME` | Nom de domaine personnalisé (`ethanledorze.fr`) |

## Technique

- **Site statique** en HTML, CSS et JavaScript, sans framework.
- **Générée par Jekyll**, que GitHub Pages lance automatiquement à chaque modification.
- **Style éditorial** : polices Playfair Display, Source Serif 4 et JetBrains Mono ; accent bleu `#1D3A6E`.
- **Thème clair ou sombre**, automatique ou au choix du visiteur.
- **Accessibilité** : contrastes ≥ 4,5:1, zones cliquables ≥ 44 px, lien d'évitement, respect de `prefers-reduced-motion`. Le contenu reste lisible même sans JavaScript.
- **Responsive**, testé de 320 px au grand écran.
- **Référencement** : plan du site généré automatiquement (`jekyll-sitemap`), balise canonique, données structurées schema.org (`Person`).
- **Aperçu de partage** : balises Open Graph avec une image 1200 × 630.
- **Polices hébergées sur le site**, sans appel à Google Fonts.

## Veille techno automatique

La rubrique « Veille » se met à jour toute seule, chaque matin vers 7 h :

1. Le robot GitHub Actions [`.github/workflows/veille.yml`](.github/workflows/veille.yml) lance le script [`scripts/veille.py`](scripts/veille.py).
2. Le script lit les flux RSS listés dans [`_data/veille_sources.json`](_data/veille_sources.json) (CERT-FR, LinuxFR, IT-Connect, ActuIA, Siècle Digital) et garde les 3 articles les plus récents de chaque thème.
3. S'il y a du nouveau, il enregistre `_data/veille.json` et le site est republié.

Pour lancer une mise à jour à la main : onglet **Actions** → **Veille techno** → **Run workflow**.
Pour ajouter ou retirer une source, modifier `_data/veille_sources.json`.

## Hébergement

- **Hébergement** : GitHub Pages (gratuit), publié depuis la branche `main`, à la racine du dépôt.
- **Domaine** : `ethanledorze.fr`, enregistré chez OVH. Il pointe vers GitHub Pages grâce à quatre enregistrements `A` (`185.199.108.153` à `185.199.111.153`) et à un `CNAME` pour `www`. Le HTTPS est fourni par GitHub.
- **Formulaire de contact** : [Web3Forms](https://web3forms.com) (gratuit). La clé se colle dans le panneau, rubrique **Réglages** ; tant qu'elle est vide, le formulaire est masqué.
- **Statistiques** : [GoatCounter](https://www.goatcounter.com), sans cookies, donc sans bandeau de consentement.

## Aperçu en local (facultatif)

```bash
gem install jekyll jekyll-sitemap
jekyll serve
# puis ouvrir http://localhost:4000
```

---

© Ethan Ledorze. Tous droits réservés.
