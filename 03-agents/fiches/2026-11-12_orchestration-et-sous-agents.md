---
date: 2026-11-12
axe: orchestration
source: https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration
type: primaire
fiabilite: haute
tags: [orchestration, sous-agent]
lien-autre-partie: claude-code
---

## En une phrase

Trois façons de faire travailler plusieurs agents ensemble, trois schémas qui marchent, et
des limites chiffrées que je ne connaissais pas.

## Ce que j'ai retenu

Trois approches sont documentées. Les sous-agents, à qui on délègue. Les workflows
dynamiques, où l'agent écrit lui-même un programme qui lance plusieurs agents par phases
et combine leurs résultats. Et l'advisor, qu'on consulte.

La documentation nomme trois schémas qui fonctionnent : parallélisation, spécialisation,
escalade.

Le point d'architecture le plus important : chaque sous-agent tourne dans son propre fil
de session, un flux d'événements isolé avec son propre historique. C'est ce qui évite que
tout le monde se marche dessus dans un contexte commun.

Les limites sont chiffrées et je ne les avais vues nulle part. La délégation ne descend
que d'un niveau. Une session a au maximum vingt-cinq fils enfants simultanés, ceux qui ne
font rien compris. Une liste prédéfinie peut contenir jusqu'à vingt agents. Et l'advisor
n'est consultable que par le fil principal, pas par les sous-agents.

Les sous-agents sont persistants, on peut leur réécrire plus tard.

## Pourquoi ça compte pour le groupe

C'est ma deuxième question de départ, celle qui venait de ce que j'avais observé chez un
collègue qui faisait tourner plusieurs agents en parallèle. Je comprends maintenant la
mécanique derrière : l'isolation du contexte par fil, et une profondeur de délégation
volontairement limitée à un cran.

La limite d'un seul niveau est un choix de conception intéressant. Elle empêche l'arbre
d'agents de devenir impossible à suivre, au prix de la souplesse. C'est exactement le
compromis entre gain de parallélisation et perte de maîtrise que je voulais comprendre.

Pour l'axe Claude Code, les sous-agents existent aussi côté SDK, avec leur propre
documentation que je n'ai pas lue. À voir si les limites sont les mêmes.

## À creuser

La page sur les fils de session, qui détaille les permissions des sous-agents, n'a pas été
lue. C'est elle qui dira si un sous-agent hérite des droits de son parent, ce qui est la
vraie question de sécurité derrière la délégation.

Les workflows dynamiques sont arrivés le 9 octobre 2026 en bêta. Fonctionnalité récente,
donc à surveiller de près.
