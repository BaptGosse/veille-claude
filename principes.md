# Règles communes

Reprises de la partie 3 du document de préparation. Elles valent pour nous cinq, quel
que soit l'outil choisi.

## Périmètre

La veille couvre les cinq axes du dépôt. Elle ne couvre pas le comparatif avec les
offres concurrentes, ni le volet commercial et contractuel, ni la recherche fondamentale
en apprentissage automatique.

Elle court du 8 septembre 2026 au 30 juin 2027.

## Rôles

Chacun est veilleur sur son axe. Trois rôles tournent chaque semaine.

| Rôle | Ce qu'il fait |
| --- | --- |
| Animateur | prépare et anime le point hebdomadaire, relance les retardataires |
| Consolidateur | tient à jour la synthèse commune et le sommaire du dépôt |
| Relecteur croisé | relit la synthèse d'un autre et signale recoupements et manques |

La rotation est notée dans `rotation.md`, à créer au premier point.

## Le cycle

1. Cibler : écrire ou revoir les questions auxquelles on veut répondre sur son axe.
2. Sourcer : trouver les sources, voir ce qu'elles valent, brancher les flux.
3. Collecter : relever ce qu'on garde, au format commun.
4. Trier et analyser : appliquer les critères, recouper, remettre dans le contexte.
5. Diffuser : poster sur le canal le jour même, puis présenter au point hebdomadaire.
6. Capitaliser : verser la fiche à la synthèse et revoir sources et questions.

La sixième relance la première. On sort du flux les sources qui n'ont rien donné et on
remplace les questions auxquelles on a répondu.

## Ce qu'on s'impose

- Trois cercles de sources : l'officiel, les analyses sérieuses, puis les forums et les réseaux.
- Rien qui vienne du troisième cercle n'entre dans la synthèse sans confirmation ailleurs.
- Chaque fiche porte sa source, son type et sa date de consultation.
- Le même modèle de fiche pour tout le monde, celui de `modele-fiche.md`.
- Fichiers nommés `AAAA-MM-JJ_sujet-en-kebab-case`, comme ça le tri par date se fait tout seul.
- Une fiche qui touche à l'axe d'un autre le dit dans `lien-autre-partie`.

## Critères de retenue

On ne garde une information que si sa source est identifiée et datée, qu'elle apporte
quelque chose de neuf par rapport aux fiches déjà écrites, qu'elle a été recoupée quand
elle vient du troisième cercle, et qu'elle répond au moins en partie à une question de
départ.

## Indicateurs

Quatre chiffres relevés en fin de cycle, à noter dans le compte rendu du point.

- Le nombre de fiches par membre et par semaine.
- La part des sources de premier cercle.
- Le nombre de questions de départ auxquelles on a répondu.
- Le nombre de renvois d'un axe vers un autre.

Le dernier est celui qui compte le plus. Il dit si on a produit un travail commun ou cinq
veilles posées côte à côte.

## Les champs de l'en-tête

| Champ | Ce qu'on y met |
| --- | --- |
| `date` | date de consultation, pas de publication |
| `axe` | le sous-thème à l'intérieur de sa partie |
| `source` | l'URL exacte |
| `type` | `primaire`, `secondaire` ou `signal` |
| `fiabilite` | `haute`, `moyenne` ou `a-confirmer` |
| `tags` | ceux de son axe, définis dans son `sources.md` |
| `lien-autre-partie` | le dossier concerné, ou vide |
