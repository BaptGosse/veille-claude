---
date: 2026-11-12
auteur: Baptiste Gosselin
axe: Modèles
type: revue
tags: [evaluation, version]
---

# Comment lire une annonce de modèle sans se faire avoir

Quatre modèles sont sortis entre le 22 septembre et le 9 novembre. J'ai lu les quatre
annonces en entier, en cherchant uniquement ce qui est vérifiable. Voici ce que j'en
retire, et surtout comment je les lirai la prochaine fois.

## Séparer ce qui est chiffré du reste

Une annonce mélange trois choses. Des chiffres contractuels, des chiffres de mesure, et
des adjectifs. Seuls les premiers engagent.

Sur les quatre sorties, les chiffres contractuels tiennent en deux lignes par modèle.
Opus 5.5 passe de 5 et 25 dollars par million de tokens à 4 et 20, soit vingt pour cent de
moins. Fable 5.2 fait exactement le même saut, de 10 et 50 à 8 et 40. Sonnet 5.5 ne bouge
pas, il reste à 2 et 10. Haiku 5.5 divise son tarif par dix sous 100 000 tokens d'invite.

Le reste, « plus intelligent », « communique mieux », n'est pas mesurable et ne sert pas à
décider.

Au passage, ni la fenêtre de contexte ni la sortie maximale ne changent. Les quatre
modèles sont à un million et 128 000. Ce n'est mentionné dans aucune annonce, c'est dans
le tableau de la documentation. Les annonces communiquent sur ce qui bouge, pas sur ce qui
compte.

## Le coût par tâche n'est pas le prix

Opus 5.5 annonce « quarante pour cent moins cher à faire tourner » alors que son prix au
token baisse de vingt pour cent. Les deux chiffres sont exacts. Le premier mesure un coût
par tâche, parce que le modèle consomme moins de tokens pour le même travail. Le second
est le tarif.

Dans une discussion de budget, c'est le second qui engage. Le premier dépend de la charge,
et la note de bas de page de l'annonce Haiku le dit à demi-mot : le tokenizer a changé,
donc une même tâche compte un peu plus de tokens qu'avant.

## Les scores sont relevés à fond

Voici la phrase qui m'a fait reprendre toute ma lecture, en petit sous un tableau d'Opus
5.5 : sauf mention contraire, tous les résultats sont obtenus à l'effort maximum.

L'effort est le réglage qui décide de la quantité de raisonnement produite avant de
répondre. Les scores publiés sont donc relevés au maximum, alors que les applications et
les outils tournent souvent au réglage intermédiaire. Celui qui compare un chiffre
d'annonce à ce qu'il obtient en production ne compare pas la même chose.

Pire, le même modèle n'a pas le même score selon la page qui le cite. Opus 5.5 est donné à
40,0 pour cent sur un benchmark dans sa propre annonce et à 42,5 dans celle de Fable 5.2.
Sur un autre, 81,8 chez lui et 87,2 chez Fable. Dans sa propre annonce, un troisième score
vaut 57,8 dans le tableau et 52,5 dans le texte, cette fois au réglage par défaut.

Ce ne sont pas des erreurs. Ce sont des conditions de mesure différentes dont une partie
seulement est affichée.

Quand le protocole est donné, il est utile et il refroidit. Sur un benchmark, Anthropic
indique un écart type de 2,6 points et précise que le classement public tourne sur cinq
essais par tâche. Un écart de deux points entre deux modèles ne veut donc rien dire. Une
note d'une autre annonce signale même que deux évaluations ont tourné sur une préversion
affectée par un bug susceptible de dégrader les réponses, donc avec un score probablement
sous-estimé.

Le meilleur argument vient d'Anthropic. Dans l'annonce d'Opus 5.5, les écarts de benchmark
sont décrits comme devenus un guide moins fiable des différences réelles.

## La règle que j'applique maintenant

Aucun score n'entre dans une fiche ou dans une synthèse sans trois choses : le niveau
d'effort, le harnais utilisé, le nombre d'essais. S'il en manque une, le score est noté
avec la mention à confirmer et ne sert pas à départager deux modèles.

Ça paraît sévère. En pratique ça élimine la quasi-totalité des chiffres qui circulent, et
ça rend les quelques-uns qui restent beaucoup plus utiles.

## Ce qu'il faut lire en plus

Deux changements de comportement se cachent dans les annonces et ce ne sont pas des
améliorations. Opus 5.5 ne s'utilise plus avec le raisonnement désactivé, et Sonnet 5.5
demande un réglage particulier pour s'en approcher. Pour quelqu'un qui appelle ces modèles
depuis du code existant, c'est une rupture.

Et il y a la page que personne ne regarde, celle des dépréciations. C'est elle qui m'a
appris que Sonnet 4.5 est retiré le 30 novembre, et que trois paramètres d'API ont déjà
disparu le 21 octobre avec une erreur 400 à la clé. Aucune annonce du fil d'actualités
entre le 18 septembre et le 10 novembre ne le mentionne.

Une annonce dit ce qui arrive. Elle ne dit pas ce qui s'arrête.
