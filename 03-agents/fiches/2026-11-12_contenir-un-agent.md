---
date: 2026-11-12
axe: garde-fou
source: https://platform.claude.com/docs/en/managed-agents/permission-policies
type: primaire
fiabilite: haute
tags: [garde-fou, orchestration]
lien-autre-partie: mcp
---

## En une phrase

Deux mécanismes existent pour contenir un agent, les politiques de permission et les
budgets, et tous les deux ont une formulation piégeuse qu'il faut avoir lue.

## Ce que j'ai retenu

Côté permissions, trois valeurs. `always_allow` exécute sans rien demander. `always_ask`
met en pause jusqu'à approbation. `auto` laisse le serveur évaluer chaque appel et
décider de l'exécuter, de le refuser ou de demander.

Par défaut, les outils de l'agent sont en `always_allow` et les outils MCP en
`always_ask`. Aucun jeu d'outils n'est en `auto` par défaut.

La phrase à retenir est un avertissement de la documentation elle-même : « `auto` is not a
human checkpoint. If the server determines that a call is safe, the call runs before
anyone sees it ». Le nom laisse croire à une supervision, c'est une automatisation.

Deux trous à connaître. Les politiques de permission ne s'appliquent pas aux outils
personnalisés. Et quand un appel attend une validation humaine, la session attend
indéfiniment, ce qui n'est pas un problème de sécurité mais un très bon moyen de bloquer
une chaîne de traitement sans s'en apercevoir.

Côté budgets, on peut poser un plafond de dépense à la création d'une session. Sont
comptés les tokens du modèle, les recherches web et le temps d'exécution, aux tarifs
publics.

Là aussi une formulation à lire deux fois : « The cap is enforced between model requests,
not mid-request. » Le plafond peut donc être dépassé d'une requête. Quand il est atteint,
la session passe au repos sans être terminée, et n'accepte plus que les événements qui
règlent un travail en cours.

Trois contraintes pratiques. Un budget ne peut pas être ajouté après la création de la
session. Sa suppression est irréversible. Et une session multi-agents a un seul budget
partagé entre tous ses fils.

Il existe par ailleurs un événement d'interruption, et des restrictions de domaines web.

## Pourquoi ça compte pour le groupe

C'est la moitié de ma troisième question, celle sur la façon d'arrêter un agent qui
dérive. La réponse est qu'on ne l'arrête pas en cours de route, on l'encadre avant.

Les deux formulations piégeuses sont le genre de chose qui ne se découvre qu'en lisant la
documentation en entier. `auto` qui n'est pas un point de contrôle humain, et un plafond
qui s'applique entre deux requêtes. Un ingénieur qui lit en diagonale se croit protégé
dans les deux cas.

Pour l'axe MCP, le défaut est bon à connaître : les outils MCP demandent l'autorisation
par défaut, pas les outils natifs. La frontière de confiance passe là.

## À creuser

Aucune limite d'itérations ni de délai n'a été trouvée côté agents gérés. Côté API, la
boucle des outils serveur a bien un plafond d'itérations qui renvoie un état de pause. Les
réglages équivalents du SDK n'ont pas été vérifiés.

La page sur l'observabilité des sessions n'a pas été lue.
