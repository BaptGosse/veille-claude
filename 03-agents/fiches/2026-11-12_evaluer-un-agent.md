---
date: 2026-11-12
axe: evaluation
source: https://www.anthropic.com/research/demystifying-evals-for-ai-agents
type: primaire
fiabilite: haute
tags: [evaluation, garde-fou]
lien-autre-partie: modeles
---

## En une phrase

Évaluer un agent n'est pas évaluer un modèle, et la différence tient dans une métrique :
réussir une fois sur trois essais n'est pas la même chose que réussir trois fois sur
trois.

## Ce que j'ai retenu

Le vocabulaire d'abord, parce qu'il manquait à notre glossaire commun. Une tâche, un
essai, un correcteur, et une transcription, aussi appelée trace ou trajectoire. Les
correcteurs se répartissent en trois familles, par code, par modèle, et humains, et une
évaluation sérieuse combine les trois.

La métrique est le point central. `pass@k` compte un succès si au moins un essai sur k
réussit. `pass^k` exige que les k essais réussissent. L'exemple de l'article est
parlant : un agent qui réussit trois fois sur quatre en moyenne ne réussit trois essais
d'affilée que dans environ quarante-deux pour cent des cas.

Pour un système qu'on met en production, c'est la seconde métrique qui compte. La
première mesure ce dont un agent est capable, la seconde ce sur quoi on peut compter.

Deux usages distincts sont rappelés. Les évaluations de capacité démarrent avec un taux de
réussite bas, c'est normal. Les évaluations de non-régression visent presque cent pour
cent.

Les conseils pratiques sont modestes et c'est ce qui les rend crédibles. Vingt à cinquante
tâches tirées de vraies défaillances suffisent pour commencer. Juger le résultat plutôt
que le chemin suivi. Et une recommandation répétée, lire les transcriptions.

Côté outillage, l'article liste des plateformes d'évaluation et cite des benchmarks
d'agents existants. Côté plateforme, un export OpenTelemetry est en bêta depuis le
14 octobre 2026, qui permet de tracer les sessions dans son propre outil d'observabilité.

## Pourquoi ça compte pour le groupe

C'est l'autre moitié de ma troisième question, et c'est la partie que je ne savais pas
formuler. Je cherchais comment savoir qu'un agent est fiable. La réponse est qu'il faut
d'abord décider de quelle fiabilité on parle, capacité ou constance, et que la deuxième
est beaucoup plus dure.

Pour l'axe Modèles, ça rejoint directement ce qui a été écrit sur la lecture d'un score.
Un chiffre sans nombre d'essais ne dit pas s'il s'agit de la meilleure tentative ou de la
pire. Avec le vocabulaire de cet article, la question devient simplement de savoir si on
lit du `pass@k` ou du `pass^k`.

## À creuser

Aucun classement public d'agents n'a été trouvé, contrairement aux modèles. Les benchmarks
cités existent mais il n'y a pas de tableau de bord officiel.

La page de documentation sur le développement de tests n'a pas été lue, et c'est celle qui
dirait ce que la plateforme propose en propre.
