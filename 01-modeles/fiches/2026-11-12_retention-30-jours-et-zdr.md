---
date: 2026-11-12
axe: hebergement
source: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
type: primaire
fiabilite: haute
tags: [hebergement, version]
lien-autre-partie:
---

## En une phrase

Choisir le modèle le plus capable fait perdre la non-conservation des données, parce que
Fable et Mythos imposent trente jours de rétention et sont exclus du zero data retention.

## Ce que j'ai retenu

Le principe général est bon. « Conversation content (your prompts and Claude's outputs)
is not retained by default ». Sous un accord de zero data retention, « Anthropic does not
store customer prompts or responses at rest after the API response is returned ».

L'exception est nommée, et elle vise précisément le haut de gamme. La page liste
« Claude Fable 5.2, Claude Mythos 5.2, Claude Fable 5.1, Claude Mythos 5.1, Claude Fable
5, and Claude Mythos 5: These models require 30-day data retention and are not available
under ZDR unless expressly authorized by Anthropic. »

Les release notes du 9 novembre le redisent pour les deux derniers : « Both models
require 30-day data retention » et « They aren't available under zero data retention
unless expressly authorized by Anthropic. »

Le ZDR n'est pas une case à cocher. « To request ZDR for your organization, contact the
Anthropic sales team », et « ZDR is enabled per organization; each new organization
requires ZDR to be enabled separately ». Donc commercial, et par organisation, ce qui veut
dire qu'un nouveau projet qui crée sa propre organisation repart sans.

Le périmètre exclut aussi des surfaces entières : la console y compris son bac à sable,
les agents gérés dont les transcriptions persistent jusqu'à suppression, les offres grand
public, les interfaces Teams et Enterprise, Claude for Excel, les intégrations tierces.
Pour Claude Code, les données de productivité remontées par le journal de métriques sont
explicitement hors ZDR.

Selon la voie choisie, le ZDR est décrit comme disponible sur demande pour Claude
Platform on AWS et pour la voie Google Anthropic managed. Pour Bedrock, Google managed et
Foundry, la documentation Anthropic ne le décrit pas et renvoie au fournisseur de cloud.

## Pourquoi ça compte pour le groupe

C'est un arbitrage qu'on ne voit pas venir. Sur le papier on compare des modèles par prix
et par capacité, et on découvre que la ligne du haut du tableau annule une garantie
contractuelle qu'on croyait acquise. Pour une plateforme qui manipule des données
sensibles, ça peut suffire à écarter Fable sans même regarder ses scores.

À l'inverse, Opus 5.5, Sonnet 5.5 et Haiku 5.5 ne sont pas dans la liste des modèles
couverts. Le choix d'un modèle devient donc aussi un choix de régime de rétention.

## À creuser

La section « Retention regardless of arrangement » n'a été lue qu'en résumé. Elle
mentionnerait une conservation possible jusqu'à deux ans pour les contenus signalés par
les systèmes de sûreté, et une conservation imposée par la loi. À relire verbatim avant
de s'appuyer dessus, parce que c'est le genre de clause qui compte dans un dataspace.

La durée de rétention par défaut hors accord particulier n'est pas donnée sur cette page,
elle renvoie à des articles de privacy.claude.com qui n'ont pas été ouverts.
