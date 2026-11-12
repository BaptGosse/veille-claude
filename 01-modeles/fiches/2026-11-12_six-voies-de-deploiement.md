---
date: 2026-11-12
axe: hebergement
source: https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/overview
type: primaire
fiabilite: haute
tags: [hebergement]
lien-autre-partie: mcp
---

## En une phrase

Il existe six façons de faire tourner un modèle Claude, elles ne se valent pas sur la
question de savoir qui est responsable de traitement, et aucune page ne les récapitule.

## Ce que j'ai retenu

Les six voies : la Claude API en direct, Claude Platform on AWS, Amazon Bedrock, Claude
Models on Google Cloud en version Anthropic managed, la même en version Google managed,
et Claude in Microsoft Foundry.

Ce qui les sépare n'est pas l'interface, c'est qui opère et qui répond des données.

Pour Google, la page de comparaison est nette. « Anthropic operates the Claude API » d'un
côté, « Google operates Claude models as part of Google Cloud's Agent Platform » de
l'autre. Tout suit : les hôtes, la facturation, les quotas, la console, les rôles IAM.

Même logique chez AWS : « Unlike Amazon Bedrock, where AWS operates the inference stack,
Anthropic operates Claude Platform on AWS. »

Et la phrase qui compte le plus pour un dataspace, tirée de la page de rétention : « On
Claude Models on Google Cloud (Google managed) and Amazon Bedrock, the cloud provider is
the data processor ». Sur les voies gérées par Anthropic, c'est Anthropic. Le choix de la
voie décide donc de l'identité du responsable de traitement, ce qui est une question de
contrat avant d'être une question technique.

Foundry propose deux modes, hébergé sur Azure ou hébergé chez Anthropic. Le premier est
le seul endroit lu où la documentation s'engage sur le confinement des contenus.

La disponibilité des modèles n'est pas la même partout. Mythos 5.2 n'apparaît ni sur
Bedrock ni sur Google managed dans les pages lues. Les modèles Fable et Mythos ne sont pas
proposés en mode hébergé sur Azure.

## Pourquoi ça compte pour le groupe

On parle souvent du choix du modèle comme si c'était la seule décision. Il y a une
décision avant, celle de la voie, et elle engage plus loin, parce qu'elle fixe qui traite
les données et sous quel contrat.

Pour l'axe MCP, c'est le même raisonnement un cran plus loin : avant de demander à quelles
conditions une entreprise ouvre son système d'information à un agent, il faut savoir qui
opère le modèle qui est au bout.

## À creuser

Aucune page ne liste les six voies au même endroit, il a fallu les reconstituer en
recoupant quatre pages. Ça mérite un tableau dans `comparatif.md`, et c'est fait.

Un écart entre deux pages officielles : la page Claude Platform on AWS liste Opus 4.5,
Sonnet 4.5 et Haiku 4.5, qui sont absents du tableau de la page data residency. Les deux
pages ne disent pas la même chose sur le même sujet. À signaler et à revérifier.

Les pages Bedrock, anthropic-managed et google-managed n'ont pas été ouvertes. Elles
contiennent le détail des points d'accès régionaux, qui est la piste ouverte dans la fiche
sur les régions.
