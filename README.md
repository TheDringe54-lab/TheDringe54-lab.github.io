# ethanledorze.fr

Portfolio d'**Ethan Ledorze**, assistant informaticien en Gendarmerie, en recherche d'un poste de technicien support ou de technicien / administrateur systèmes & réseaux en Normandie (Eure, Seine-Maritime).

**Site en ligne : https://ethanledorze.fr**

Contact : contact@ethanledorze.fr · [LinkedIn](https://www.linkedin.com/in/ethan-ledorze-32000025a/)

---

## Modifier le contenu

Le contenu se modifie depuis un **panneau d'administration**, sans toucher au code :

1. Aller sur **https://app.pagescms.org** et se connecter avec GitHub.
2. Ouvrir ce dépôt, puis **Contenu du site**.
3. Modifier les textes, les listes ou la photo, puis cliquer sur **Save**.
4. Le site en ligne est mis à jour en une ou deux minutes.

Dans les champs de texte, `**mot**` s'affiche en **gras** et `*mot*` en *italique*.

On peut aussi modifier directement le fichier [`_data/contenu.yml`](_data/contenu.yml) sur GitHub.

## Structure du dépôt

| Fichier | Rôle |
|---|---|
| `_data/contenu.yml` | Tous les textes du site : en-tête, chiffres clés, profil, compétences, parcours, FAQ, contact |
| `index.html` | Mise en page, styles et scripts (modèle Jekyll qui lit `contenu.yml`) |
| `_includes/icone.html` | Les icônes des compétences |
| `_includes/md.html` | Gère le gras et l'italique dans les textes |
| `assets/` | Images, dont la photo de profil |
| `.pages.yml` | Configuration des formulaires du panneau Pages CMS |
| `_config.yml` | Configuration de Jekyll |
| `CNAME` | Nom de domaine personnalisé (`ethanledorze.fr`) |

## Technique

- **Page unique** en HTML, CSS et JavaScript, sans framework.
- **Générée par Jekyll**, que GitHub Pages lance automatiquement à chaque modification.
- **Style éditorial** : polices Playfair Display, Source Serif 4 et JetBrains Mono ; accent bleu `#1D3A6E`.
- **Thème clair ou sombre**, automatique ou au choix du visiteur.
- **Accessibilité** : contrastes ≥ 4,5:1, zones cliquables ≥ 44 px, lien d'évitement, respect de `prefers-reduced-motion`. Le contenu reste lisible même sans JavaScript.
- **Responsive**, testé jusqu'à 375 px de large.

## Hébergement

- **Hébergement** : GitHub Pages (gratuit), publié depuis la branche `main`, à la racine du dépôt.
- **Domaine** : `ethanledorze.fr`, enregistré chez OVH. Il pointe vers GitHub Pages grâce à quatre enregistrements `A` (`185.199.108.153` à `185.199.111.153`) et à un `CNAME` pour `www`. Le HTTPS est fourni par GitHub.
- **Statistiques** : [GoatCounter](https://www.goatcounter.com), sans cookies, donc sans bandeau de consentement.

## Aperçu en local (facultatif)

```bash
gem install jekyll
jekyll serve
# puis ouvrir http://localhost:4000
```

---

© Ethan Ledorze. Tous droits réservés.
