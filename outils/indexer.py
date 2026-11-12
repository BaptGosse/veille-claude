#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construit index.json, le sommaire que lit la page de consultation.

GitHub Pages ne sait pas lister un dossier. Ce script parcourt le dépôt, relève les
fichiers markdown et l'en-tête des fiches, et écrit le tout dans index.json.

    python3 outils/indexer.py

À relancer après chaque fiche ajoutée. Le dépôt est la source, index.json n'est qu'un
sommaire recalculable.
"""
import json
import os
import re

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AXES = [
    ("01-modeles", "Modèles", "Baptiste Gosselin"),
    ("02-skills", "Skills", "Brice Ramette"),
    ("03-agents", "Agents", "Quentin Affholder"),
    ("04-claude-code", "Claude Code", "Marin Jabet"),
    ("05-mcp", "MCP", "Nathan Le Biez"),
]

COMMUNS = [
    ("README.md", "Présentation"),
    ("principes.md", "Règles communes"),
    ("surveillance.md", "Sources sans flux"),
    ("modele-fiche.md", "Modèle de fiche"),
]

ENTETE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)


def lire(chemin):
    with open(os.path.join(RACINE, chemin), encoding="utf-8") as f:
        return f.read()


def titre(texte, defaut):
    for ligne in texte.split("\n"):
        if ligne.startswith("# "):
            return ligne[2:].strip()
    return defaut


def entete(texte):
    """Lit l'en-tête YAML d'une fiche. Assez de YAML pour nos six champs, pas plus."""
    m = ENTETE.match(texte)
    if not m:
        return {}
    champs = {}
    for ligne in m.group(1).split("\n"):
        if ":" not in ligne:
            continue
        cle, valeur = ligne.split(":", 1)
        valeur = valeur.strip()
        if valeur.startswith("[") and valeur.endswith("]"):
            valeur = [v.strip() for v in valeur[1:-1].split(",") if v.strip()]
        champs[cle.strip()] = valeur
    return champs


def resume(texte):
    """La section « En une phrase » d'une fiche, pour l'afficher dans le sommaire."""
    m = re.search(r"##\s*En une phrase\s*\n+(.+?)(?:\n\s*\n|\n##)", texte, re.S)
    return " ".join(m.group(1).split()) if m else ""


sommaire = {"genere": None, "communs": [], "revues": [], "axes": []}

for nom, libelle in COMMUNS:
    if os.path.exists(os.path.join(RACINE, nom)):
        sommaire["communs"].append({"chemin": nom, "titre": libelle})

# la revue : les articles destines a etre lus, par date decroissante
drevue = os.path.join(RACINE, "revue")
if os.path.isdir(drevue):
    for nom in sorted(os.listdir(drevue), reverse=True):
        if not nom.endswith(".md"):
            continue
        texte = lire("revue/" + nom)
        champs = entete(texte)
        corps = ENTETE.sub("", texte)
        m = re.search(r"^#\s+(.+)$", corps, re.M)
        apres = corps[m.end():] if m else corps
        intro = ""
        for bloc in apres.split("\n\n"):
            bloc = bloc.strip()
            if bloc and not bloc.startswith("#"):
                intro = " ".join(bloc.split())
                break
        sommaire["revues"].append({
            "chemin": "revue/" + nom,
            "titre": m.group(1).strip() if m else nom[:-3],
            "date": champs.get("date", ""),
            "auteur": champs.get("auteur", ""),
            "axe": champs.get("axe", ""),
            "tags": champs.get("tags", []),
            "resume": intro[:240],
        })

for dossier, libelle, membre in AXES:
    chemin = os.path.join(RACINE, dossier)
    if not os.path.isdir(chemin):
        continue
    bloc = {"dossier": dossier, "titre": libelle, "membre": membre,
            "pages": [], "fiches": []}
    for nom in ("synthese.md", "comparatif.md", "grille-evaluation.md",
                "sources.md", "glossaire.md"):
        if os.path.exists(os.path.join(chemin, nom)):
            texte = lire(os.path.join(dossier, nom))
            bloc["pages"].append({"chemin": f"{dossier}/{nom}",
                                  "titre": titre(texte, nom)})
    dfiches = os.path.join(chemin, "fiches")
    if os.path.isdir(dfiches):
        for nom in sorted(os.listdir(dfiches), reverse=True):
            if not nom.endswith(".md"):
                continue
            texte = lire(f"{dossier}/fiches/{nom}")
            champs = entete(texte)
            bloc["fiches"].append({
                "chemin": f"{dossier}/fiches/{nom}",
                "titre": nom[11:-3].replace("-", " ") if len(nom) > 14 else nom[:-3],
                "date": champs.get("date", ""),
                "type": champs.get("type", ""),
                "fiabilite": champs.get("fiabilite", ""),
                "tags": champs.get("tags", []),
                "lien": champs.get("lien-autre-partie", ""),
                "resume": resume(texte),
            })
    sommaire["axes"].append(bloc)

total = sum(len(a["fiches"]) for a in sommaire["axes"])
dates = [f["date"] for a in sommaire["axes"] for f in a["fiches"] if f["date"]]
sommaire["genere"] = max(dates) if dates else ""
sommaire["total_fiches"] = total

with open(os.path.join(RACINE, "index.json"), "w", encoding="utf-8") as f:
    json.dump(sommaire, f, ensure_ascii=False, indent=1)
    f.write("\n")

print("index.json écrit :", len(sommaire["axes"]), "axes,", total, "fiches,",
      len(sommaire["revues"]), "articles de revue")
