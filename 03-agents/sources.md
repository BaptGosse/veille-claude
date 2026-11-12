# Sources suivies - Agents

Tenu par Quentin Affholder. Toutes les URL ci-dessous ont été ouvertes et vérifiées.

## Questions de départ

| Question | État au 12/11/2026 |
| --- | --- |
| Sur quels critères confie-t-on une tâche à un agent plutôt qu'à un script ? | répondue, critères qualitatifs et chiffres de coût |
| Comment garde-t-on la main sur plusieurs exécutions en parallèle ? | répondue, trois approches et des limites chiffrées |
| Comment sait-on qu'un agent est fiable, et comment l'arrête-t-on ? | répondue, deux mécanismes de garde-fou et une métrique d'évaluation |

## Premier cercle

| Source | URL | Flux | Dernière consultation |
| --- | --- | --- | --- |
| Agents gérés, vue d'ensemble | https://platform.claude.com/docs/en/managed-agents/overview | aucun, surveillance de page | 12/11/2026 |
| Orchestration multi-agents | https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration | aucun, surveillance de page | 12/11/2026 |
| Politiques de permission | https://platform.claude.com/docs/en/managed-agents/permission-policies | aucun | 12/11/2026 |
| Budgets | https://platform.claude.com/docs/en/managed-agents/budgets | aucun | 12/11/2026 |
| Fonctionnement de la boucle d'outils | https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works | aucun | 12/11/2026 |
| Agent SDK | https://code.claude.com/docs/en/agent-sdk/overview | aucun | 12/11/2026 |
| Release notes de la plateforme | https://platform.claude.com/docs/en/release-notes/overview | aucun, surveillance de page | 12/11/2026 |

`platform.claude.com/docs/en/agent-sdk/overview` renvoie une redirection vers
`code.claude.com`. Garder la seconde adresse.

## Deuxième cercle

| Source | URL | Flux | Dernière consultation |
| --- | --- | --- | --- |
| Construire des agents efficaces | https://www.anthropic.com/engineering/building-effective-agents | aucun | 12/11/2026 |
| Système de recherche multi-agents | https://www.anthropic.com/engineering/multi-agent-research-system | aucun | 12/11/2026 |
| Évaluations d'agents, démystification | https://www.anthropic.com/research/demystifying-evals-for-ai-agents | aucun | 12/11/2026 |
| Mise à l'échelle des agents gérés | https://www.anthropic.com/engineering/managed-agents | aucun | 12/11/2026 |
| Blog d'ingénierie, liste | https://www.anthropic.com/engineering | aucun trouvé | 12/11/2026 |

Ces articles donnent le protocole et les chiffres. Ils sont de deuxième cercle parce que
ce sont des publications de l'éditeur sur ses propres produits, pas de la documentation
de référence.

## Troisième cercle

| Source | URL | Dernière consultation |
| --- | --- | --- |
| Hacker News | https://news.ycombinator.com/ | |

## À lire, pas encore ouvert

- L'article sur quand utiliser un système multi-agents et quand ne pas le faire, cité par
  la documentation. C'est la source la plus directe pour la première question.
- La page sur les fils de session, qui détaille les permissions des sous-agents.
- Les sous-pages de l'Agent SDK : boucle, sous-agents, permissions, hooks, sessions.
- La page sur l'observabilité des sessions et celle sur l'export OpenTelemetry.
- Les articles sur les harnais pour tâches longues et sur l'ingénierie du contexte.

## Tags de l'axe

`boucle`, `orchestration`, `sous-agent`, `evaluation`, `garde-fou`

## Sources écartées

Rien pour l'instant.
