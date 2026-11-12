# Sources sans flux, à surveiller autrement

Vérifié le 12 novembre 2026.

En montant le dispositif on s'est aperçus d'un problème que le document de préparation
n'avait pas vu. On avait prévu un agrégateur RSS où toutes les sources arrivent au même
endroit. Sauf que les sources de premier cercle les plus importantes n'ont pas de flux.

Ont un flux Atom, donc vont dans l'agrégateur via `veille.opml` :

| Source | Flux |
| --- | --- |
| anthropics/claude-code | `https://github.com/anthropics/claude-code/releases.atom` |
| anthropics/anthropic-sdk-python | `https://github.com/anthropics/anthropic-sdk-python/releases.atom` |
| modelcontextprotocol/servers | `https://github.com/modelcontextprotocol/servers/releases.atom` |
| anthropics/skills | `https://github.com/anthropics/skills/releases.atom` (valide mais vide pour l'instant) |

N'ont aucun flux trouvé, il faut une surveillance de page du type ChangeDetection :

| Page | URL | Qui la surveille |
| --- | --- | --- |
| Release notes de la plateforme | https://platform.claude.com/docs/en/release-notes/overview | Modèles |
| Liste des modèles | https://platform.claude.com/docs/en/models/overview | Modèles |
| Tarification | https://platform.claude.com/docs/en/about-claude/pricing | Modèles |
| Dépréciations et retraits | https://platform.claude.com/docs/en/about-claude/model-deprecations | Modèles |
| Résidence des données | https://platform.claude.com/docs/en/manage-claude/data-residency | Modèles |
| Annonces Anthropic | https://www.anthropic.com/news | Modèles |
| Blog d'ingénierie | https://www.anthropic.com/engineering | Agents |
| Spécification Agent Skills | https://agentskills.io/specification.md | Skills |
| Spécification MCP | https://modelcontextprotocol.io/ | MCP |

Deux remarques pour le point de groupe.

`docs.claude.com` renvoie une redirection permanente vers `platform.claude.com/docs`.
C'est la deuxième URL qu'il faut garder partout.

Le dépôt `modelcontextprotocol/servers` indique que les serveurs de référence se
consultent désormais surtout via `https://registry.modelcontextprotocol.io/`. À vérifier
par l'axe MCP, et à ajouter ici si cette page bouge assez pour mériter une surveillance.

## Ajouté le 12 novembre 2026

La page des dépréciations est la plus importante des sept et la moins visible. C'est elle
qui a sorti le retrait de Sonnet 4.5 au 30 novembre, et aucune annonce du fil d'actualités
entre le 18 septembre et le 10 novembre ne le mentionne. Une page qui ne fait jamais de
bruit et qui décide de ce qui cesse de fonctionner.

La page de résidence des données y entre aussi. Elle porte la liste des zones d'exécution
disponibles, et c'est sur cette liste qu'on attend un changement.
