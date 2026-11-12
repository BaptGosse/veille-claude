# Glossaire - Skills

**AAIF, Agentic AI Foundation** - la fondation sous la Linux Foundation à qui Anthropic a
donné le standard Agent Skills le 22 octobre 2026.

**allowed-tools** - champ facultatif et expérimental du `SKILL.md` qui liste des outils.
Attention au contresens : dans Claude Code, c'est une pré-approbation, pas une
restriction. Il élargit les droits, il ne les réduit pas.

**Chargement progressif** - le mécanisme en trois niveaux. Le nom et la description au
démarrage, environ cent tokens. Le corps du `SKILL.md` à l'activation. Les ressources à la
demande.

**description** - champ obligatoire, de 1 à 1024 caractères. C'est lui qui est comparé à
la demande pour décider de charger la skill. Le champ qui décide de tout.

**name** - champ obligatoire, 64 caractères maximum, minuscules, chiffres et tirets, et
identique au nom du dossier.

**Scanner** - l'outil d'analyse des skills tierces en offre Enterprise. Rend un verdict
pass, warn ou fail. Ne couvre ni les skills de l'API ou de la console, ni celles passées
par un serveur MCP.

**SKILL.md** - le fichier obligatoire d'une skill. Un frontmatter YAML puis du Markdown
libre. Recommandé sous 500 lignes.

**skills-ref** - l'outil de validation de référence de la spécification.
