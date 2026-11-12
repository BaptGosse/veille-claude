---
date: 2026-11-12
axe: ecosysteme
source: https://github.com/anthropics/skills
type: primaire
fiabilite: haute
tags: [annuaire, format]
lien-autre-partie: mcp
---

## En une phrase

Il n'existe pas d'annuaire public de skills tierces que j'aie pu vérifier, et aucun flux
ne couvre l'écosystème, donc la surveillance passe par deux dépôts GitHub et un Discord.

## Ce que j'ai retenu

Le dépôt `anthropics/skills` est le point de référence. Environ 193 000 étoiles, 22 800
forks, mais seulement 62 commits sur la branche principale et 1 100 pull requests
ouvertes. Beaucoup de monde regarde, peu de choses rentrent.

Il contient un dossier `spec` avec un unique fichier, un `template`, et un dossier
`skills` d'exemples classés en quatre familles, création et design, développement et
technique, entreprise et communication, et documents. Le README est explicite sur leur
statut : ce sont des démonstrations à visée pédagogique, à tester soi-même avant tout
usage sérieux.

Côté annuaires, je n'ai rien trouvé de public et de vérifiable. Le site de la fondation ne
recense que la spécification et des guides, pas des skills. Claude.ai a un annuaire
intégré avec des skills partenaires. Claude Code a un marché de plugins officiel. Un badge
du dépôt pointe vers un site tiers que je n'ai pas ouvert.

Aucun flux Atom ne couvre l'écosystème tiers. Le flux des releases du dépôt officiel est
valide mais vide, aucune release n'a jamais été publiée.

## Pourquoi ça compte pour le groupe

C'était ma première question de départ et la réponse est concrète. Il n'y a pas d'endroit
unique où regarder, donc la surveillance se construit à la main : les commits du dépôt
officiel, l'organisation de la fondation pour les propositions de spec, la section de
documentation, et le Discord pour ce qui circule avant d'être écrit.

L'absence d'annuaire vérifié est en soi un résultat. Un écosystème d'un million de skills
annoncées sans catalogue consultable, c'est un écosystème où la découverte passe par le
bouche-à-oreille, ce qui était exactement mon point de départ.

Pour l'axe MCP, une remarque : des skills peuvent être partagées via un serveur MCP
connecté, et ces skills-là échappent au scanner de l'offre Enterprise.

## À creuser

Le site tiers vers lequel pointe le badge du dépôt officiel. S'il recense vraiment des
skills, c'est le premier annuaire de la liste et ça change ma réponse.

Le nombre exact de skills d'exemple dans le dépôt, que je n'ai pas compté.
