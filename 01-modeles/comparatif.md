# Comparatif des modèles

C'est le tableau que les quatre autres axes viennent chercher quand ils doivent arbitrer.

**Dernière mise à jour : 12 novembre 2026.** Au-delà d'un mois sans mise à jour, ne pas
s'en servir pour décider. Quatre modèles sont sortis entre le 22 septembre et le
9 novembre, le tableau vieillit vite.

Relevé sur `platform.claude.com/docs/en/models/overview`,
`/about-claude/pricing`, `/manage-claude/api-and-data-retention` et
`/about-claude/model-deprecations`.

## Les modèles

| Modèle | Identifiant API | Contexte | Sortie max | Entrée | Sortie | Effort par défaut | Latence | ZDR | Retrait au plus tôt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fable 5.2 | `claude-fable-5-2` | 1 M | 128 k | 8 $ | 40 $ | high | modérée | non | 09/11/2027 |
| Mythos 5.2 | `claude-mythos-5-2` | 1 M | 128 k | 8 $ | 40 $ | non relevé | non relevé | non | 09/11/2027 |
| Opus 5.5 | `claude-opus-5-5` | 1 M | 128 k | 4 $ | 20 $ | medium | modérée | oui | 22/09/2027 |
| Sonnet 5.5 | `claude-sonnet-5-5` | 1 M | 128 k | 2 $ | 10 $ | high | rapide | oui | 28/09/2027 |
| Haiku 5.5 | `claude-haiku-5-5` | 1 M | 128 k | 0,10 $ | 0,50 $ | medium | la plus rapide | oui | 07/10/2027 |

Prix par million de tokens. Coupure de connaissances annoncée à juin 2026 pour les quatre
modèles courants. L'effort par défaut est celui de l'API, les applications et Claude Code
n'utilisent pas forcément le même.

Trois choses se lisent dans ce tableau et nulle part ailleurs.

Le contexte et la sortie maximale sont identiques partout. Le choix ne se joue pas là.

L'écart de prix en entrée va de 0,10 à 8 dollars, soit un facteur 80. C'est le seul
critère qui varie vraiment.

La colonne ZDR coûte le haut de gamme. Fable et Mythos imposent trente jours de rétention
et sont exclus du zero data retention sauf autorisation expresse.

**À vérifier.** Les tarifs de Haiku 5.5 au-delà de 100 000 tokens d'invite. Deux lectures
du 12 novembre donnent deux chiffres, 2 et 2,50 dollars d'un côté, 0,50 et 2,50 de
l'autre. Le second est cohérent avec la note de l'annonce. À trancher en relisant la page
de tarification.

**Accès restreint.** Mythos 5.2 n'est pas une option ordinaire. C'est le même modèle que
Fable 5.2 sans certains garde-fous, réservé aux organisations vérifiées par Anthropic.
Il ne se compare pas aux autres, il se demande.

## Où ça tourne

| Modèle | Claude API | Platform on AWS | Bedrock | Google, Anthropic managed | Google managed | Foundry |
| --- | --- | --- | --- | --- | --- | --- |
| Fable 5.2 | oui | oui | oui | oui | oui | chez Anthropic |
| Mythos 5.2 | oui | non listé | non listé | oui | non listé | chez Anthropic |
| Opus 5.5 | oui | oui | oui | oui | oui | Azure et Anthropic |
| Sonnet 5.5 | oui | oui | oui | oui | oui | Azure et Anthropic |
| Haiku 5.5 | oui | oui | oui | oui | oui | Azure et Anthropic |

« non listé » veut dire absent des pages lues le 12 novembre, pas forcément indisponible.
Les modèles Fable et Mythos ne sont pas proposés en mode hébergé sur Azure.

## Qui est responsable de traitement

| Voie | Qui opère l'inférence | Responsable de traitement |
| --- | --- | --- |
| Claude API | Anthropic | Anthropic |
| Claude Platform on AWS | Anthropic | Anthropic |
| Amazon Bedrock | AWS | le fournisseur de cloud |
| Google, Anthropic managed | Anthropic | Anthropic |
| Google managed | Google | le fournisseur de cloud |
| Microsoft Foundry, hébergé sur Azure | Anthropic sur infrastructure Azure | non relevé |
| Microsoft Foundry, hébergé chez Anthropic | Anthropic | non relevé |

C'est la décision qui vient avant le choix du modèle, et c'est une question de contrat
autant que de technique.

## Zone d'exécution

Deux valeurs possibles pour l'`inference geo`, `global` par défaut et `us`. Pas d'Europe.
Le stockage au repos n'accepte que `us`. Forcer les États-Unis coûte 1,1 fois le tarif
standard.

Conclusion pour un périmètre européen : aucune voie documentée côté Anthropic ne permet
aujourd'hui de garantir une inférence en Europe. Deux pistes restent à instruire, les
points d'accès régionaux de Bedrock et l'hôte européen qui apparaît dans la voie Google
managed. Tant qu'elles ne sont pas vérifiées, la réponse est non.

## Ce qui manque encore

La colonne région par plateforme, une fois les deux pistes instruites.

Le détail des protocoles d'évaluation, qui est dans les system cards. Tant qu'on ne les a
pas lues, aucun score ne sert à départager deux modèles ici.
