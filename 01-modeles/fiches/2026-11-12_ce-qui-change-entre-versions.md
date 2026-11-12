---
date: 2026-11-12
axe: versions
source: https://www.anthropic.com/news
type: primaire
fiabilite: haute
tags: [version, tarification]
lien-autre-partie: claude-code
---

## En une phrase

Sur les quatre sorties des sept dernières semaines, ce qui change vraiment et se vérifie
tient en deux lignes par modèle, le prix et la vitesse, le reste est qualitatif.

## Ce que j'ai retenu

J'ai lu les quatre annonces et je n'ai gardé que ce qui est chiffré.

**Opus 5.5**, 22 septembre, face à Opus 5. Prix de 5 et 25 dollars à 4 et 20, soit vingt
pour cent de moins. Lecture de cache de 0,50 à 0,20. Sortie annoncée « more than 30%
faster ». Et un changement d'API qui n'a rien de cosmétique : le modèle ne s'utilise plus
avec le raisonnement désactivé.

**Sonnet 5.5**, 28 septembre, face à Sonnet 5. Prix inchangé à 2 et 10. « 30%+ faster ».
Là aussi un changement d'usage, il faut passer au réglage `between_tools` si on ne veut
pas du raisonnement en continu. Un seul score vraiment parlant, Terminal-Bench 4.0 à
70,6 pour cent contre 10,3 à la version précédente.

**Haiku 5.5**, 7 octobre, face à Haiku 4.5, pas face à un Haiku 5. Entrée à 0,10 et sortie
à 0,50 jusqu'à 100 000 tokens d'invite. Premier modèle de sa classe avec un réglage
d'effort. Les gains annoncés contre Haiku 4.5 sont spectaculaires, par exemple
Terminal-Bench 4.0 à 39,2 pour cent contre 0,0.

**Fable 5.2**, 9 novembre, face à Fable 5.1. De 10 et 50 à 8 et 40, encore vingt pour
cent. « up to 30% faster ». Mode rapide jusqu'à 2,5 fois, facturé 16 et 80. Environ
cinquante-cinq pour cent de blocages en moins qu'avec la version précédente.

Trois constantes se dégagent. Le prix baisse de vingt pour cent à chaque montée de
version, sauf Sonnet qui reste au même tarif. La vitesse gagne environ trente pour cent à
chaque fois. Et ni la fenêtre de contexte ni la sortie maximale ne bougent, elles sont
identiques pour les quatre modèles, un million et 128 000.

Dernier point, le plus utile en réunion : les annonces communiquent sur le coût par tâche,
pas par token. Opus 5.5 annonce « 40% less to run » alors que son prix au token baisse de
vingt pour cent. L'écart vient du fait que le modèle consomme moins de tokens pour le même
travail. Les deux chiffres sont vrais, ils ne mesurent pas la même chose, et seul celui au
token est contractuel.

## Pourquoi ça compte pour le groupe

Quatre sorties en sept semaines. Un arbitrage de modèle rendu fin septembre portait sur une
gamme qui a changé deux fois depuis, et à chaque fois avec une baisse de prix. Refaire
l'arbitrage coûte une heure, ne pas le refaire coûte vingt pour cent par an et par token.

Pour l'axe Claude Code, les deux changements de comportement sur le raisonnement sont à
connaître, ce sont des ruptures d'usage et pas des améliorations.

## À creuser

Une contradiction non tranchée sur le prix de Haiku 5.5 au-delà de 100 000 tokens
d'invite. La page de tarification a été lue comme donnant 2 et 2,50 dollars, l'annonce
donne 0,50 et 2,50. L'annonce est cohérente avec sa propre note, qui parle de cinquante
pour cent d'économie au-delà du seuil par rapport à Haiku 4.5 facturé 1 et 5, ce qui
tombe bien sur 0,50 et 2,50. Mais tant que la page de tarification n'est pas relue sur ce
point précis, le comparatif porte la mention à vérifier.

C'est la règle de recoupement qui a servi ici. Deux lectures, deux chiffres, donc on ne
tranche pas, on note.
