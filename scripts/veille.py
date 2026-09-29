#!/usr/bin/env python3
"""Veille techno automatique.

Récupère les derniers articles de quelques flux RSS / Atom et les écrit dans
_data/veille.json, que le site affiche dans la rubrique « Veille techno ».
Lancé chaque jour par .github/workflows/veille.yml. Aucune dépendance externe.
"""
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

SOURCES_FICHIER = Path("_data/veille_sources.json")
SORTIE = Path("_data/veille.json")
PAR_THEME = 3
RESUME_MAX = 160
ATOM = "{http://www.w3.org/2005/Atom}"


def telecharger(url):
    req = urllib.request.Request(url, headers={"User-Agent": "veille-ethanledorze.fr/1.0 (+https://ethanledorze.fr)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def texte(el):
    return "".join(el.itertext()).strip() if el is not None else ""


def nettoyer(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > RESUME_MAX:
        s = s[:RESUME_MAX].rsplit(" ", 1)[0].rstrip(" ,.;:") + "…"
    return s


def lire_date(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        d = parsedate_to_datetime(s)  # RSS : "Tue, 29 Sep 2026 10:00:00 +0200"
    except (TypeError, ValueError):
        try:
            d = datetime.fromisoformat(s.replace("Z", "+00:00"))  # Atom : ISO 8601
        except ValueError:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d.astimezone(timezone.utc)


def analyser(contenu):
    """Renvoie une liste de dicts {titre, lien, date, resume} depuis un flux RSS ou Atom."""
    racine = ET.fromstring(contenu)
    articles = []
    if racine.tag == ATOM + "feed":
        for e in racine.findall(ATOM + "entry"):
            lien = ""
            for l in e.findall(ATOM + "link"):
                if l.get("rel", "alternate") == "alternate":
                    lien = l.get("href", "")
                    break
            articles.append({
                "titre": texte(e.find(ATOM + "title")),
                "lien": lien,
                "date": lire_date(texte(e.find(ATOM + "published")) or texte(e.find(ATOM + "updated"))),
                "resume": texte(e.find(ATOM + "summary")) or texte(e.find(ATOM + "content")),
            })
    else:
        for i in racine.iter("item"):
            articles.append({
                "titre": texte(i.find("title")),
                "lien": texte(i.find("link")),
                "date": lire_date(texte(i.find("pubDate")) or texte(i.find("{http://purl.org/dc/elements/1.1/}date"))),
                "resume": texte(i.find("description")),
            })
    return [a for a in articles if a["titre"] and a["lien"].startswith(("https://", "http://"))]


def main():
    config = json.loads(SOURCES_FICHIER.read_text(encoding="utf-8"))
    ancien = {}
    if SORTIE.exists():
        try:
            ancien = {t["id"]: t for t in json.loads(SORTIE.read_text(encoding="utf-8")).get("themes", [])}
        except (ValueError, KeyError):
            ancien = {}

    themes, erreurs = [], 0
    for theme in config["themes"]:
        articles = []
        for src in theme["sources"]:
            try:
                for a in analyser(telecharger(src["flux"])):
                    a["source"] = src["nom"]
                    articles.append(a)
            except Exception as ex:  # une source en panne ne doit pas bloquer les autres
                erreurs += 1
                print(f"⚠ {src['nom']} : {ex}", file=sys.stderr)
        vus, choisis = set(), []
        for a in sorted(articles, key=lambda a: a["date"] or datetime.min.replace(tzinfo=timezone.utc), reverse=True):
            if a["lien"] in vus:
                continue
            vus.add(a["lien"])
            choisis.append({
                "titre": nettoyer(a["titre"]),
                "lien": a["lien"],
                "source": a["source"],
                "date": a["date"].strftime("%Y-%m-%d") if a["date"] else "",
                "resume": nettoyer(a["resume"]),
            })
            if len(choisis) == PAR_THEME:
                break
        if not choisis and theme["id"] in ancien:
            # toutes les sources du thème sont en panne : on garde les articles de la veille
            choisis = ancien[theme["id"]]["articles"]
        themes.append({"id": theme["id"], "titre": theme["titre"], "titre_en": theme["titre_en"], "articles": choisis})

    if not any(t["articles"] for t in themes):
        print("Aucun article récupéré, fichier inchangé.", file=sys.stderr)
        return 1
    if [ancien.get(t["id"], {}).get("articles") for t in themes] == [t["articles"] for t in themes]:
        print("Aucun nouvel article, fichier inchangé.")
        return 0
    sortie = {"mise_a_jour": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "themes": themes}
    SORTIE.write_text(json.dumps(sortie, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{sum(len(t['articles']) for t in themes)} articles écrits dans {SORTIE} ({erreurs} source(s) en erreur).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
