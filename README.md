# Veille Claude - Groupe 5, TD1

Veille technologique du groupe 5 pour la R5.03, sur Claude et l'écosystème qui s'est
construit autour. Le cadre est décrit dans `TD1_Groupe5_PrepVeille.pdf`, les règles de
fonctionnement sont reprises dans `principes.md`.

Dépôt mis en place le 12 novembre 2026.

## La revue

`revue/` contient les articles écrits pour être lus par quelqu'un qui n'a pas suivi la
veille, et la copie des messages postés sur le canal du groupe. C'est la partie diffusion
du dispositif. Les fiches des axes sont des notes de travail, la revue est ce qu'on
partage.

## Les cinq axes

| Dossier | Axe | Membre |
| --- | --- | --- |
| `01-modeles/` | Modèles | Baptiste Gosselin |
| `02-skills/` | Skills | Brice Ramette |
| `03-agents/` | Agents | Quentin Affholder |
| `04-claude-code/` | Claude Code | Marin Jabet |
| `05-mcp/` | MCP | Nathan Le Biez |

Chaque dossier contient la même chose : `sources.md` avec les sources suivies et leur
date de dernière consultation, `glossaire.md`, `fiches/` avec une fiche par information
retenue, et `synthese.md` complétée au fil de l'eau.

## Où on en est

| Axe | Sources listées | Fiches | Synthèse |
| --- | --- | --- | --- |
| Modèles | oui | 8 | à jour au 12/11/2026 |
| Skills | à faire | 0 | vide |
| Agents | à faire | 0 | vide |
| Claude Code | à faire | 0 | vide |
| MCP | à faire | 0 | vide |

Chacun remplit son `sources.md` et écrit sa première fiche. Tant qu'un axe n'a pas de
sources listées, il n'a rien à trier.

## Calendrier

| Quand | Quoi |
| --- | --- |
| 12 novembre 2026 | mise en place du dépôt, arborescence et règles communes |
| 12 novembre 2026 | premier cycle complet sur l'axe Modèles, sept fiches |
| semaine du 17 novembre | chacun remplit son `sources.md` et branche ses flux |
| à partir du 24 novembre | le cycle tourne, une fiche minimum par semaine et par personne |
| fin de chaque mois | consolidation des synthèses et relecture croisée |
| juin 2027 | restitution, démonstration des objets produits |

La veille a été définie en septembre pour courir jusqu'au 30 juin 2027. Le dépôt, lui,
démarre le 12 novembre. Les premières semaines ont servi à cadrer, pas à collecter.

## Rythme

Deux fois quinze minutes par semaine pour trier les flux, une heure pour lire et écrire
une fiche, et vingt minutes de point de groupe sur un créneau fixe.

## Comment on ajoute une fiche

1. Copier `modele-fiche.md` dans le dossier `fiches/` de son axe.
2. La nommer `AAAA-MM-JJ_sujet-en-kebab-case.md`.
3. Remplir l'en-tête et les quatre sections.
4. Commiter avec un message qui dit l'axe et le sujet.
5. Poster le lien sur le canal du groupe le jour même.

## Consulter la veille dans un navigateur

Le dépôt se lit tel quel sur GitHub, mais il est aussi publié en page web. `index.html`
charge les fichiers markdown et les affiche, avec le sommaire des cinq axes et la liste
des fiches par date.

Le sommaire vient de `index.json`, que GitHub Pages ne sait pas fabriquer tout seul. Il
faut donc le régénérer après chaque fiche ajoutée :

```
python3 outils/indexer.py
```

Puis commiter `index.json` avec la fiche. Si une fiche n'apparaît pas dans le sommaire du
site, c'est qu'on a oublié cette commande.

Pour prévisualiser avant de pousser :

```
python3 -m http.server 8000
```

puis ouvrir http://localhost:8000
