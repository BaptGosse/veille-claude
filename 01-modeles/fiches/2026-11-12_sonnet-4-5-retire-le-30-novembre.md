---
date: 2026-11-12
axe: versions
source: https://platform.claude.com/docs/en/about-claude/model-deprecations
type: primaire
fiabilite: haute
tags: [version]
lien-autre-partie: claude-code
---

## En une phrase

Sonnet 4.5 est retiré le 30 novembre 2026, dans dix-huit jours, et trois paramètres d'API
ont déjà disparu dans la version du 21 octobre.

## Ce que j'ai retenu

`claude-sonnet-4-5-20250929` a été déprécié le 30 septembre 2026 et sera retiré le
30 novembre 2026. Le remplacement indiqué est `claude-sonnet-5-5`. Le préavis fait
soixante et un jours, pour un minimum annoncé de soixante.

Plus discret et plus méchant : `temperature`, `top_p` et `top_k` sont retirés dans la
version d'API 2026-10-21. Un appel qui les envoie reçoit une erreur 400. Ce n'est pas une
dépréciation en douceur, c'est un code d'erreur.

Deux autres identifiants sont à surveiller, avec un retrait annoncé comme pas avant une
date désormais proche. `claude-opus-4-5-20251101` au 24 novembre 2026 et
`claude-haiku-4-5-20251001` au 15 octobre 2026, cette dernière étant déjà passée.

Pour les quatre modèles courants, rien à craindre dans l'année. Les dates de retrait au
plus tôt sont le 22 septembre 2027 pour Opus 5.5, le 28 septembre pour Sonnet 5.5, le
7 octobre pour Haiku 5.5 et le 9 novembre pour Fable 5.2.

## Pourquoi ça compte pour le groupe

C'est la fiche la plus actionnable des sept. Dix-huit jours, c'est un délai de production,
pas un délai de veille. Un service qui appelle encore `claude-sonnet-4-5-20250929` cesse
de fonctionner fin novembre.

C'est aussi l'illustration de ce qu'une veille apporte par rapport à une recherche. Cette
information ne se trouve pas quand on la cherche, elle se trouve parce qu'on regarde
régulièrement une page qui ne fait jamais de bruit.

J'ai vérifié au passage : aucune annonce de dépréciation n'apparaît dans le fil
d'actualités entre le 18 septembre et le 10 novembre. Les retraits ne sont pas annoncés
là où on regarde, ils sont sur une page de documentation à part. C'est pour ça qu'elle est
dans la liste des pages surveillées.

## À creuser

Vérifier si on utilise encore un identifiant daté quelque part, et lequel. La règle à
retenir est d'épingler un identifiant de modèle quelque part dans la configuration plutôt
que de le disséminer dans le code, sinon la migration se fait à la main et dans l'urgence.
