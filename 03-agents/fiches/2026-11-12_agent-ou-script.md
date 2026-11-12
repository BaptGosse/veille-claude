---
date: 2026-11-12
axe: criteres
source: https://www.anthropic.com/engineering/building-effective-agents
type: primaire
fiabilite: haute
tags: [orchestration, evaluation]
lien-autre-partie:
---

## En une phrase

Le critère officiel est de prendre la solution la plus simple possible et de n'ajouter de
la complexité que quand elle est nécessaire, et un agent n'est justifié que quand on ne
peut pas prévoir le nombre d'étapes.

## Ce que j'ai retenu

Anthropic distingue deux choses qu'on confond souvent. Un enchaînement, où le modèle et
les outils sont orchestrés par du code écrit à l'avance. Un agent, où le modèle dirige
lui-même son déroulement et son usage des outils.

La recommandation tient en une phrase : « we recommend finding the simplest solution
possible, and only increasing complexity when needed ».

Le départage se fait sur la prévisibilité. Les enchaînements offrent de la prévisibilité
et de la constance pour des tâches bien définies. Les agents sont faits pour les
« open-ended problems where it's difficult or impossible to predict the required number of
steps ». Et le prix est annoncé : plus de coût, et la possibilité d'erreurs qui
s'accumulent.

L'article nomme cinq schémas d'enchaînement à combiner avant d'envisager un agent :
chaînage de prompts, routage, parallélisation, orchestrateur et exécutants, évaluateur et
optimiseur.

Pour le multi-agent, un second article donne des critères plus précis. Ça convient aux
tâches qui demandent beaucoup de parallélisation, dont l'information dépasse une seule
fenêtre de contexte, ou qui touchent à de nombreux outils complexes. Ça ne convient pas
aux domaines où tous les agents doivent partager le même contexte, ni à ceux où les
agents dépendent beaucoup les uns des autres.

Les chiffres de coût de cet article sont le meilleur argument que j'aie pour une réunion :
un agent consomme environ quatre fois les tokens d'une conversation, un système
multi-agents environ quinze fois.

## Pourquoi ça compte pour le groupe

C'est ma première question de départ, et elle a une réponse utilisable immédiatement.
Avant de proposer un agent, on vérifie qu'on ne sait pas écrire les étapes à l'avance. Si
on sait les écrire, on écrit un enchaînement, c'est moins cher et c'est reproductible.

Le facteur quinze sur les tokens est le genre de chiffre qui tranche une discussion plus
vite qu'un argument d'architecture.

## À creuser

L'article de référence date de décembre 2024 et une note y renvoie vers un article plus
récent sur les agents gérés pour l'approche actuelle. Il faut donc le lire comme un socle
conceptuel, pas comme l'état de l'art.

Un article spécifiquement intitulé sur quand utiliser le multi-agent et quand ne pas le
faire est cité par la documentation et n'a pas été lu. C'est la source la plus directe
pour cette question, à ouvrir au prochain passage.

Aucune règle chiffrée de seuil entre enchaînement et agent n'existe dans la documentation
officielle. Les critères sont qualitatifs.
