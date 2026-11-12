# Synthèse - Agents

Dernière mise à jour : 12 novembre 2026. Appuyée sur quatre fiches.

## Ce qu'on sait aujourd'hui

**Le critère de choix est la prévisibilité, pas la difficulté.** Si on sait écrire les
étapes à l'avance, on écrit un enchaînement. L'agent se justifie quand le nombre d'étapes
ne peut pas être prévu. La recommandation officielle est de prendre la solution la plus
simple et de n'ajouter de la complexité que quand elle est nécessaire.

**Le coût est chiffré et il tranche les discussions.** Un agent consomme environ quatre
fois les tokens d'une conversation, un système multi-agents environ quinze fois.

**L'orchestration a des limites dures.** La délégation ne descend que d'un niveau, une
session a au maximum vingt-cinq fils enfants simultanés, et une liste prédéfinie peut
contenir jusqu'à vingt agents. Chaque sous-agent tourne dans son propre fil, isolé du
contexte des autres.

**Contenir un agent se fait avant, pas pendant.** Deux mécanismes, les politiques de
permission et les budgets. Les deux ont une formulation piégeuse qu'il faut avoir lue :
`auto` n'est pas un point de contrôle humain, et un plafond de dépense s'applique entre
deux requêtes, donc se dépasse d'une requête.

**Évaluer un agent n'est pas évaluer un modèle.** La vraie question est de savoir si on
mesure ce dont l'agent est capable ou ce sur quoi on peut compter. Un agent qui réussit
trois fois sur quatre en moyenne ne réussit trois essais d'affilée que quatre fois sur
dix.

## Ce qui a changé depuis le début de la veille

Les agents gérés avancent vite. Les workflows dynamiques sont arrivés le 9 octobre en
bêta, l'export OpenTelemetry le 14 octobre, les restrictions de domaines web le 20, et les
fils de message côté API le 2 novembre. La politique de permission `auto` date du
10 septembre.

Autrement dit, tout l'outillage de contrôle et d'observation a été posé en deux mois. Ce
n'est pas anodin : c'est ce qu'on met en place quand des gens commencent à mettre ces
systèmes en production.

## Ce qui reste ouvert

**Les permissions des sous-agents.** Un sous-agent hérite-t-il des droits de son parent ?
C'est la vraie question de sécurité derrière la délégation, et la page qui y répond n'a
pas été lue.

**Les limites d'itération et de délai.** Aucune n'a été trouvée côté agents gérés. Seule
la boucle des outils serveur de l'API a un plafond documenté.

**Aucun classement public d'agents n'existe**, contrairement aux modèles. Les benchmarks
sont cités, il n'y a pas de tableau de bord.
