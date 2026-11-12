---
date: 2026-11-12
auteur: Baptiste Gosselin
axe: Modèles
type: canal
tags: []
---

# Messages du canal

Le dispositif prévoit qu'une information retenue part le jour même sur le canal de groupe,
une phrase et le lien. On garde une copie ici, ça fait la trace de la diffusion.

## 12 novembre 2026

> Sonnet 4.5 est retiré le 30 novembre, dans 18 jours. Si quelqu'un a encore
> `claude-sonnet-4-5-20250929` quelque part, c'est maintenant.
> https://platform.claude.com/docs/en/about-claude/model-deprecations

> `temperature`, `top_p` et `top_k` ont été retirés de l'API dans la version du
> 21 octobre. Un appel qui les envoie se prend une 400.

> Pour ceux qui ont besoin que les données restent en Europe : il n'y a que deux zones
> d'exécution possibles, mondiale ou États-Unis. Pas d'Europe, par aucune voie.
> Détail dans la revue : `revue/2026-11-12_ou-peut-tourner-un-modele.md`

> Piège à connaître avant de choisir un modèle : Fable et Mythos imposent 30 jours de
> rétention et sont exclus du zero data retention. Opus, Sonnet et Haiku non.

> Pour Quentin, sur les agents : les scores d'annonce sont relevés à l'effort maximum, et
> le même modèle affiche des chiffres différents selon la page qui le cite. Évaluer un
> agent, c'est évaluer un modèle plus un harnais, et le harnais pèse autant.

> Pour Marin : Opus 5.5 ne s'utilise plus avec le raisonnement désactivé, et Sonnet 5.5
> demande `between_tools`. Ça peut casser du code existant.

## 12 novembre 2026, axes Skills et Agents

> Les Agent Skills sont passées à l'Agentic AI Foundation, sous la Linux Foundation, le
> 22 octobre. Anthropic cède le nom, le dépôt et le domaine. Versions publiées, processus
> de proposition et guide de sécurité sont annoncés mais pas encore là.
> https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation

> Attention si vous clonez un dépôt qui contient des skills. `allowed-tools` est une
> pré-approbation, pas une restriction, et la confiance accordée au dossier ne le filtre
> pas. Le code des scripts n'apparaît jamais dans le contexte, donc l'audit se fait avant
> ou pas du tout.

> Pour Baptiste : les Agent Skills ne sont pas couvertes par les accords de zero data
> retention. Une ligne de plus pour ta liste.

> Chiffres utiles pour arbitrer agent contre script : un agent consomme environ 4 fois les
> tokens d'une conversation, un système multi-agents environ 15 fois.

> Limites d'orchestration que personne ne connaissait : la délégation ne descend que d'un
> niveau, et une session a au maximum 25 fils enfants en même temps.

> Deux formulations à lire deux fois. La permission `auto` n'est pas un point de contrôle
> humain, le serveur exécute avant que quiconque voie. Et un plafond de budget s'applique
> entre deux requêtes, donc il se dépasse d'une requête.

> Pour Nathan : par défaut les outils MCP sont en `always_ask` et les outils natifs de
> l'agent en `always_allow`. La frontière de confiance passe exactement là.
