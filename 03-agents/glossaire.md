# Glossaire - Agents

C'est le glossaire de référence du groupe. Un terme employé ailleurs dans le rendu vient
d'ici, ou bien il y est ajouté.

**Advisor** - un agent qu'on consulte sans lui déléguer. Seul le fil principal d'une
session peut le consulter, pas les sous-agents.

**Agent** - un système où le modèle dirige lui-même son déroulement et son usage des
outils. S'oppose à l'enchaînement, où les étapes sont écrites à l'avance dans du code.

**Boucle d'outils** - le mécanisme de base. Tant que le modèle demande un outil, on
l'exécute et on poursuit la conversation. Côté outils serveur, la boucle a un plafond
d'itérations et renvoie un état de pause quand elle l'atteint.

**Budget** - un plafond de dépense posé à la création d'une session. Compte les tokens, les
recherches web et le temps d'exécution. Appliqué entre deux requêtes, pas au milieu d'une
requête, donc dépassable d'une requête.

**Correcteur, grader** - ce qui décide si un essai est réussi. Trois familles, par code,
par modèle, humain.

**Enchaînement, workflow** - des étapes écrites à l'avance. Prévisible et constant, moins
cher qu'un agent. Cinq schémas nommés : chaînage de prompts, routage, parallélisation,
orchestrateur et exécutants, évaluateur et optimiseur.

**Fil de session** - le flux d'événements isolé dans lequel tourne un sous-agent, avec son
propre historique. C'est ce qui évite que les agents se marchent dessus.

**pass@k** - la métrique qui compte un succès si au moins un essai sur k réussit. Mesure
ce dont un agent est capable.

**pass^k** - la métrique qui exige que les k essais réussissent. Mesure ce sur quoi on peut
compter. C'est celle qui vaut pour la production.

**Politique de permission** - trois valeurs. `always_allow`, `always_ask`, et `auto` où le
serveur décide seul. Attention, `auto` n'est pas un point de contrôle humain.

**Sous-agent** - un agent à qui on délègue. La délégation ne descend que d'un niveau, et
une session a au plus vingt-cinq fils enfants simultanés.

**Transcription, trace, trajectoire** - l'enregistrement de ce qu'un agent a fait pendant
un essai. Le conseil qui revient le plus souvent dans la littérature d'évaluation est de
les lire.

**Workflow dynamique** - un programme écrit par l'agent lui-même, qui lance plusieurs
agents par phases et combine leurs résultats. En bêta depuis le 9 octobre 2026.
