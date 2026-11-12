---
date: 2026-11-12
axe: hebergement
source: https://platform.claude.com/docs/en/manage-claude/data-residency
type: primaire
fiabilite: haute
tags: [hebergement]
lien-autre-partie: mcp
---

## En une phrase

La documentation ne propose que deux zones d'exécution, mondiale ou États-Unis, et
aucune région européenne, ce qui répond par la négative à la question la plus importante
de mon axe.

## Ce que j'ai retenu

Deux réglages existent. L'`inference geo` décide où tourne l'inférence, requête par
requête : « Controls where model inference runs, on a per-request basis. » Le
`workspace geo` décide du stockage au repos.

Les valeurs possibles sont écrites noir sur blanc : « Inference geo: Only "us" and
"global" are available. » Et pour le stockage, « Currently, "us" is the only available
workspace geo. » Le défaut est `global`, donc n'importe où.

Forcer l'exécution aux États-Unis coûte 1,1 fois le tarif standard. On paie donc un
supplément pour restreindre la zone, et la seule zone qu'on peut acheter n'est pas
l'Europe.

Du côté de Microsoft Foundry, un mode garde tout chez Azure : « For deployments hosted on
Azure, prompts and completions remain within Azure. Only usage metadata and content
flagged by Anthropic's safety systems egress to Anthropic. » C'est intéressant sur le
principe, sauf que les déploiements proposés sont US Data Zone ou Global Standard, et que
choisir Data Zone « keeps inference within the United States ». Donc pas d'Europe non
plus par cette voie.

## Pourquoi ça compte pour le groupe

C'est la réponse à « où un modèle peut-il tourner quand les données ne doivent pas sortir
d'un périmètre défini ». Aujourd'hui, par les voies documentées, on ne peut pas garantir
une inférence européenne. On peut garantir une inférence américaine, ce qui est une
contrainte, pas une garantie, quand le périmètre à tenir est européen.

Ça explique après coup pourquoi l'auto-hébergement de modèles ouverts revenait dans nos
discussions à l'alternance. Ce n'était pas une préférence technique, c'était la seule
option qui répondait à la contrainte.

Pour l'axe MCP, la conséquence est directe. Un serveur MCP peut rester chez soi, le
modèle qui l'appelle, non. Le périmètre se casse au niveau du modèle, pas des outils.

## À creuser

Deux pistes, aucune confirmée, à ouvrir au prochain passage.

Un hôte `aiplatform.eu.rep.googleapis.com` apparaît dans le tableau de la voie Google
managed. Il porte « eu » dans son nom mais rien dans les pages lues n'explique ce que ça
garantit. La sous-page google-managed n'a pas été ouverte.

La page des modèles note par ailleurs que « Bedrock offers global endpoints (dynamic
routing) and regional endpoints (guaranteed data routing) for Claude Sonnet 4.5 and
later ». Des points d'accès régionaux avec routage garanti, c'est exactement ce qu'il
faudrait. Reste à savoir quelles régions, et la page Bedrock n'a pas été lue.

Tant que ces deux pistes ne sont pas instruites, la conclusion ci-dessus tient pour les
voies documentées côté Anthropic, pas pour l'ensemble des possibilités.
