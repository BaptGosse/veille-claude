---
date: 2026-11-12
axe: evaluations
source: https://www.anthropic.com/claude-opus-5-5
type: primaire
fiabilite: haute
tags: [evaluation]
lien-autre-partie: agents
---

## En une phrase

Un score publié ne veut rien dire tant qu'on ne connaît pas le niveau d'effort et le
harnais, au point que le même modèle affiche des résultats différents selon l'annonce qui
le cite.

## Ce que j'ai retenu

La phrase qui change tout est en petit sous les tableaux d'Opus 5.5 : « Unless otherwise
noted, all Claude Opus 5.5 results use adaptive thinking at max effort. » Les scores sont
donc relevés à l'effort maximum, pas au réglage par défaut. Celui qui compare un chiffre
d'annonce à ce qu'il obtient en production ne compare pas la même chose. Fable 5.2 dit la
même chose autrement : « All scores show each model's highest-available effort unless
otherwise noted. »

Le même modèle n'a pas le même score selon la page. Opus 5.5 est donné à 40,0 pour cent
sur AutomationBench dans sa propre annonce et à 42,5 dans celle de Fable 5.2. Sur
OSWorld 2.1 il est à 81,8 chez lui et à 87,2 chez Fable, avec des libellés de sous-ensemble
différents. Dans sa propre annonce, CursorBench le donne à 57,8 dans le tableau et à 52,5
dans le texte, cette fois au réglage par défaut. Ces écarts ne sont pas des erreurs, ce
sont des conditions de mesure différentes qui ne sont pas toutes affichées.

Quand le protocole est donné, il est utile. Terminal-Bench 4.0 pour Opus 5.5 est mesuré à
l'effort xhigh avec un écart type de 2,6 points, et le classement public tourne sur cinq
essais par tâche. Un écart de deux points entre deux modèles ne veut donc rien dire.
Ailleurs c'est plus mince, Haiku 5.5 publie un tableau de scores sans niveau d'effort ni
nombre d'essais.

Une note de l'annonce Sonnet 5.5 mérite d'être citée, parce qu'elle est rare : deux
évaluations ont tourné sur un déploiement de préversion « found to have a bug that could
degrade responses ». L'éditeur publie un score en disant lui-même qu'il est probablement
sous-estimé.

Le meilleur argument vient d'Anthropic. Dans l'annonce d'Opus 5.5, les écarts de benchmark
sont décrits comme devenus « a less reliable guide to real-world differences ».

## Pourquoi ça compte pour le groupe

Ça répond à ma deuxième question de départ, et la réponse est utilisable tout de suite.

Règle que j'applique à partir de maintenant sur cet axe, et que je propose aux quatre
autres. Aucun score n'entre dans une fiche ou dans une synthèse sans trois choses : le
niveau d'effort, le harnais utilisé, le nombre d'essais. S'il en manque une, le score est
noté avec la mention à confirmer et ne sert pas à départager deux modèles.

Pour l'axe Agents, c'est la même difficulté sous un autre nom. Évaluer un agent, c'est
évaluer un modèle plus un harnais, et les annonces montrent que le harnais pèse autant
que le modèle.

## À creuser

Le protocole complet est dans les system cards, qui sont des PDF hébergés ailleurs et qui
n'ont pas été ouverts. C'est là qu'il faut aller pour instruire sérieusement la question,
et ça vaut une séance entière plutôt qu'un passage de quinze minutes.
