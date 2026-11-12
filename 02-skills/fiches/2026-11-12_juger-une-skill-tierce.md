---
date: 2026-11-12
axe: securite
source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
type: primaire
fiabilite: haute
tags: [securite, evaluation]
lien-autre-partie: claude-code
---

## En une phrase

La recommandation officielle est de n'installer que des skills de sources connues, et
quand on regarde ce qu'une skill peut faire, on comprend pourquoi.

## Ce que j'ai retenu

La documentation ne prend pas de gants : « Use Skills only from trusted sources: those you
created yourself or obtained from Anthropic. » Et pour le reste, « If you must use a Skill
from an untrusted or unknown source, exercise extreme caution and thoroughly audit it
before use. » Le résumé tient en quatre mots de la même page : traiter ça comme
l'installation d'un logiciel.

Ce qu'une skill peut faire dépend complètement de l'endroit où elle tourne. Sur l'API,
elle s'exécute dans un conteneur isolé, sans accès réseau et sans installation de paquets.
Dans Claude Code, elle a un accès réseau complet, le même que n'importe quel programme
lancé par l'utilisateur. Sur claude.ai, ça dépend des réglages.

Le détail qui m'a le plus marqué : les scripts d'une skill sont exécutés par bash, et leur
code n'entre jamais dans la fenêtre de contexte, seule leur sortie y arrive. Donc ni
l'agent ni l'utilisateur ne voit ce que le script fait pendant la session. L'audit se fait
avant, ou pas du tout.

Trois choses à savoir sur `allowed-tools`, du côté de Claude Code. Ce n'est pas une
restriction mais une pré-approbation, donc un champ qui élargit les droits et ne les
réduit pas. La confiance accordée à un dossier de travail ne le filtre pas. Et une skill
d'un dépôt qu'on clone peut donc s'accorder un accès large avant qu'on ait rien validé.
Il existe par ailleurs une syntaxe qui exécute une commande shell avant même d'envoyer le
contenu de la skill au modèle, désactivable par un réglage.

Côté organisation, un scanner existe en offre Enterprise, mais ses trous sont documentés.
Il ne traite que les skills tierces téléversées, et ne couvre ni celles déjà présentes
avant activation, ni celles créées avec Claude, ni celles partagées via un serveur MCP,
ni les skills passées par l'API ou la console. La documentation précise aussi qu'il ne
détecte pas une skill qui se comporte mal sans être malveillante.

Dernier point qui touche un autre axe : les Agent Skills ne sont pas couvertes par les
accords de zero data retention.

## Pourquoi ça compte pour le groupe

C'était ma deuxième question de départ et la réponse officielle est décevante : il n'y a
pas de critères publiés pour juger une skill tierce. Le guide de sécurité fait partie de
la feuille de route de la fondation et n'existe pas encore. En attendant, chacun se
débrouille.

Pour l'axe Claude Code, le point sur `allowed-tools` et sur l'exécution de commandes est
directement actionnable : cloner un dépôt qui contient des skills n'est pas neutre.

Pour l'axe Modèles, l'exclusion du ZDR complète la liste des choses qui font perdre cette
garantie sans qu'on s'en aperçoive.

## À creuser

Ma grille d'évaluation, que j'écris à partir de ces éléments et que je mets dans
`grille-evaluation.md`. Elle n'est pas officielle, c'est une synthèse de ce que la
documentation recommande, et elle sera à revoir quand le guide de la fondation sortira.

La page de gouvernance pour les organisations n'a pas été lue.
