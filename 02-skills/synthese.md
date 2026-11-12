# Synthèse - Skills

Dernière mise à jour : 12 novembre 2026. Appuyée sur quatre fiches de premier cercle.

## Ce qu'on sait aujourd'hui

**Le format a changé de mains il y a trois semaines.** Anthropic a donné le standard à
l'Agentic AI Foundation, sous la Linux Foundation, le 22 octobre 2026. Nom, logo,
organisation GitHub et domaine compris. Les mainteneurs viennent d'Anthropic, Google et
OpenAI, à titre individuel.

**La spécification est courte et stable mais pas versionnée.** Deux champs obligatoires,
quatre facultatifs, un chargement en trois niveaux. Aucun numéro de version, aucun
changelog, donc aucun moyen de savoir qu'elle a bougé à part relire ou suivre les commits.

**Il n'y a pas de guide officiel pour juger une skill tierce.** C'est annoncé dans la
feuille de route de la fondation, ce n'est pas publié. En attendant, la recommandation
officielle se résume à n'utiliser que des sources de confiance et à traiter une
installation comme une installation de logiciel.

**Une skill peut beaucoup, et son code reste invisible pendant la session.** Les scripts
sont exécutés par bash et leur code n'entre jamais dans la fenêtre de contexte. Sur l'API
l'exécution est isolée et sans réseau, dans Claude Code l'accès réseau est complet.

**Il n'existe pas d'annuaire public vérifié.** Un million de skills annoncées, aucun
catalogue consultable confirmé. La découverte se fait par les dépôts et par le bouche à
oreille.

## Ce qui a changé depuis le début de la veille

Le passage à la fondation le 22 octobre est le seul événement structurant de la période.
Les release notes de la plateforme ne mentionnent les skills qu'une fois depuis septembre.

Autrement dit, le sujet bouge peu en surface et beaucoup en gouvernance.

## Ce qui reste ouvert

**La divergence entre la spec et l'implémentation.** La documentation Anthropic ajoute des
règles sur le champ `name` qui ne sont pas dans la spécification. Une skill valide selon
le standard peut donc être refusée.

**Le site tiers** vers lequel pointe un badge du dépôt officiel, qui pourrait être le
premier annuaire de la liste.

**Les trois éléments de la feuille de route** de la fondation, versions publiées,
processus de proposition, guide de sécurité. C'est maintenant la principale chose à
surveiller sur cet axe.
