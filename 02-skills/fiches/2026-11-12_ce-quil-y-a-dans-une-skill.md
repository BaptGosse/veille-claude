---
date: 2026-11-12
axe: format-et-specification
source: https://agentskills.io/specification.md
type: primaire
fiabilite: haute
tags: [format]
lien-autre-partie:
---

## En une phrase

La spécification tient en six champs dont deux obligatoires, elle décrit un chargement en
trois niveaux, et elle n'a ni numéro de version ni changelog.

## Ce que j'ai retenu

Une skill est un dossier avec un `SKILL.md` dedans, du YAML puis du Markdown. Les dossiers
`scripts/`, `references/` et `assets/` sont facultatifs, et n'importe quel autre fichier
est permis. Le corps n'a aucune contrainte de format, la spec recommande seulement de
rester sous cinq cents lignes et de garder les références de fichiers à un seul niveau de
profondeur.

Deux champs sont obligatoires. `name`, soixante-quatre caractères maximum, minuscules,
chiffres et tirets, sans tiret au début ni à la fin, sans double tiret, et identique au
nom du dossier. `description`, de un à 1024 caractères, qui doit dire ce que fait la skill
et quand l'utiliser.

Quatre champs facultatifs : `license`, `compatibility`, `metadata` et `allowed-tools`. Ce
dernier est marqué expérimental dans la spec.

Le chargement se fait en trois niveaux et c'est le mécanisme central. Au démarrage, seuls
`name` et `description` sont chargés, soit environ cent tokens. À l'activation, le corps
du `SKILL.md`, avec une recommandation de rester sous cinq mille tokens. Les ressources
viennent ensuite, à la demande.

Il existe un outil de validation de référence, `skills-ref validate`.

## Pourquoi ça compte pour le groupe

La `description` fait tout le travail. C'est elle qui est comparée à la demande pour
décider de charger la skill, et elle est la seule chose que l'agent voit au démarrage.
Une skill mal décrite ne se déclenche jamais, une skill trop largement décrite se
déclenche tout le temps. C'est le point où je vais concentrer ma grille d'évaluation.

## À creuser

Une divergence entre deux sources officielles, et elle n'est pas anodine. La page de
documentation Anthropic ajoute que `name` ne peut pas contenir les mots réservés
`anthropic` et `claude`, ni de balises XML. La spécification ne mentionne aucune de ces
règles. Une skill valide selon la spec peut donc être refusée par l'implémentation.

Absence remarquable : la spec n'a ni numéro de version ni changelog. Il n'y a donc aucun
moyen de savoir si elle a changé depuis la dernière lecture, à part la relire ou suivre
les commits du dépôt. Le versionnage fait partie de la feuille de route de la fondation,
il n'est pas publié.
