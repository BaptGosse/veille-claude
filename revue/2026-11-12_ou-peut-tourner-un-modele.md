---
date: 2026-11-12
auteur: Baptiste Gosselin
axe: Modèles
type: revue
tags: [hebergement, tarification]
---

# Où peut tourner un modèle Claude, et ce que ça coûte de choisir

Quand on monte une plateforme pour une entreprise qui ne veut pas que ses données partent
n'importe où, la première question n'est pas de savoir quel modèle est le meilleur. C'est
de savoir où il s'exécute. J'ai passé la journée dans la documentation d'Anthropic pour
répondre à cette question. La réponse est courte et elle n'est pas agréable.

## Deux zones, et aucune n'est l'Europe

Il existe un réglage qui décide de l'endroit où tourne l'inférence, requête par requête.
Il s'appelle `inference geo` et la documentation est explicite sur ses valeurs possibles :
seulement `us` et `global`. Le défaut est `global`, c'est-à-dire n'importe où.

Le stockage au repos obéit à un second réglage, et là c'est encore plus net, une seule
valeur est disponible, `us`.

Il y a un détail qui pique. Forcer l'exécution aux États-Unis coûte 1,1 fois le tarif
standard. On paie donc un supplément pour restreindre la zone, et la seule zone qu'on peut
acheter est précisément celle qu'on cherchait à éviter.

J'ai regardé les autres voies. Microsoft Foundry propose un mode où tout reste chez Azure,
et la documentation s'y engage clairement, seules les métadonnées d'usage et les contenus
signalés par les systèmes de sûreté en sortent. Sauf que les déploiements proposés sont
américain ou mondial. Le confinement existe, mais pas là où on en aurait besoin.

Conclusion pour un périmètre européen : par les voies documentées côté Anthropic, on ne
peut pas aujourd'hui garantir une inférence en Europe.

Deux pistes restent ouvertes et je ne les ai pas encore instruites. La documentation note
que Bedrock propose des points d'accès régionaux avec un routage garanti, sans dire
lesquels. Et un hôte portant « eu » dans son nom apparaît dans la voie Google managed,
sans que rien n'explique ce qu'il garantit. Tant que je ne les ai pas ouvertes, la réponse
reste non.

## La décision qui vient avant le choix du modèle

En cherchant, je suis tombé sur quelque chose que je ne cherchais pas et qui compte
davantage que la liste des modèles.

Il existe six façons de faire tourner un modèle Claude. L'API directe, Claude Platform on
AWS, Amazon Bedrock, deux variantes chez Google, et Microsoft Foundry. Aucune page ne les
récapitule, il faut recouper quatre pages pour reconstituer la liste.

Ce qui les sépare n'est pas l'interface. C'est une phrase de la page de rétention : sur
Bedrock et sur la voie Google managed, c'est le fournisseur de cloud qui est responsable
de traitement. Sur les voies opérées par Anthropic, c'est Anthropic.

Autrement dit, choisir sa voie de déploiement, c'est choisir à qui on confie
juridiquement ses données. C'est une question de contrat avant d'être une question de
performance, et elle se tranche avant de comparer le moindre score.

## Le piège du haut de gamme

Dernière trouvaille, et c'est celle qui m'a le plus surpris.

Le principe général est rassurant. Les invites et les réponses ne sont pas conservées par
défaut, et il existe un accord dit zero data retention sous lequel rien n'est stocké après
l'appel.

Mais une liste d'exceptions existe, et elle vise exactement le haut de la gamme. Fable 5.2
et Mythos 5.2, comme leurs versions précédentes, imposent trente jours de rétention et
sont exclus de cet accord sauf autorisation expresse.

Donc prendre le modèle le plus capable fait perdre une garantie contractuelle qu'on
croyait acquise. Opus, Sonnet et Haiku ne sont pas concernés. Le choix d'un modèle est
aussi, sans que ce soit dit nulle part dans les annonces, un choix de régime de rétention.

Et l'accord lui-même ne s'active pas tout seul. Il se demande au service commercial, et il
vaut par organisation, ce qui veut dire qu'un nouveau projet qui crée sa propre
organisation repart sans.

## Ce que j'en retire

Un tableau de comparaison de modèles qui ne contient que des prix et des scores est
inutilisable pour décider dans un contexte contraint. Il manque trois colonnes : où ça
tourne, qui est responsable de traitement, et quel régime de rétention s'applique.

J'ai ajouté ces colonnes au comparatif du dépôt. Elles changent le classement. Le modèle
le mieux placé sur le prix et les capacités n'est pas celui qu'on peut déployer.

Une dernière chose, pour ceux que la question de la veille intéresse plus que celle des
modèles. Aucune de ces informations n'est fausse ni cachée. Tout est dans la
documentation officielle, écrit noir sur blanc. Simplement, ça se trouve sur six pages
différentes, dont deux que personne ne lit, et aucune annonce ne le mentionne. C'est
assez bien résumé l'intérêt de l'exercice.
