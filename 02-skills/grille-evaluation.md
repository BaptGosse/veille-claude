# Grille d'évaluation d'une skill tierce

Dernière mise à jour : 12 novembre 2026.

**Ce n'est pas une grille officielle.** Le guide de sécurité de la fondation fait partie
de sa feuille de route et n'est pas publié. Celle-ci est ma synthèse de ce que la
documentation recommande, et elle sera à revoir quand le guide sortira.

Verdict possible pour chaque skill testée : adoptée, écartée, ou à surveiller.

| Point | Ce qu'on regarde | Rédhibitoire si |
| --- | --- | --- |
| Provenance | auteur, dépôt, historique des commits, champ `license` | auteur inconnu et dépôt sans historique |
| Lecture intégrale | tous les fichiers, pas seulement `SKILL.md` | on n'a pas lu les scripts |
| Scripts | ce qu'ils font, leurs dépendances, versions épinglées ou non | dépendances non épinglées sur une skill qui touche des données |
| `allowed-tools` | l'étendue réelle des droits pré-approuvés | droits larges sans justification dans la description |
| Appels réseau | URL citées dans le corps, requêtes sortantes des scripts | appel vers un domaine sans rapport avec la fonction |
| `compatibility` | cohérence entre ce qui est déclaré et ce que font les scripts | écart entre les deux |
| Description | cohérence entre ce qu'elle annonce et le comportement réel | description trop large qui déclenche la skill tout le temps |
| Test isolé | essai sur des données sans valeur avant tout usage réel | pas encore testée |

## Pourquoi la lecture des scripts n'est pas négociable

Le code des scripts n'entre jamais dans la fenêtre de contexte, seule leur sortie y
arrive. Pendant la session, ni l'agent ni l'utilisateur ne voit ce que le script fait.
L'audit se fait avant, ou il ne se fait pas.

## Ce que la grille ne couvre pas

Une skill qui se comporte mal sans être malveillante. La documentation du scanner
Enterprise le reconnaît pour son propre outil, et c'est vrai pour cette grille aussi.

## Skills évaluées

| Skill | Date | Verdict | Motif |
| --- | --- | --- | --- |
| | | | |
