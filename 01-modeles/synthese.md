# Synthèse - Modèles

Dernière mise à jour : 12 novembre 2026. Appuyée sur huit fiches, toutes de sources de
premier cercle.

## Ce qu'on sait aujourd'hui

**Le choix d'un modèle ne se joue plus sur les capacités affichées.** Les quatre modèles
courants ont la même fenêtre de contexte et la même sortie maximale. Ce qui les sépare
est le prix, avec un facteur 80 entre les deux extrêmes, et la latence.

**Le prix baisse à chaque montée de version, d'environ vingt pour cent.** Opus 5.5 et
Fable 5.2 l'ont fait, Sonnet 5.5 est resté au même tarif, Haiku 5.5 a divisé le sien par
dix sous 100 000 tokens d'invite. Ne pas rejouer un arbitrage coûte donc de l'argent,
mécaniquement.

**Attention au chiffre communiqué.** Les annonces parlent de coût par tâche, qui baisse
plus vite que le prix par token, parce que les modèles consomment moins pour le même
travail. Seul le prix au token est contractuel.

**Un score publié n'est pas utilisable tel quel.** Les résultats sont relevés à l'effort
maximum, pas au réglage par défaut, et le même modèle affiche des chiffres différents
selon l'annonce qui le cite. Règle adoptée sur cet axe : pas d'effort, pas de harnais, pas
de nombre d'essais, alors le score ne départage rien.

**Le choix du modèle est aussi un choix de régime de rétention.** Fable et Mythos imposent
trente jours de conservation et sortent du zero data retention. Prendre le modèle le plus
capable fait perdre une garantie contractuelle.

**La voie de déploiement se décide avant le modèle.** Six voies existent, et selon celle
qu'on prend, le responsable de traitement est Anthropic ou le fournisseur de cloud.

## Ce qui a changé depuis le début de la veille

Quatre modèles en sept semaines, du 22 septembre au 9 novembre. Opus 5.5, Sonnet 5.5,
Haiku 5.5, puis Fable 5.2 accompagné de Mythos 5.2.

Deux ruptures d'usage au passage, qui ne sont pas des améliorations. Opus 5.5 ne
s'utilise plus avec le raisonnement désactivé, et Sonnet 5.5 demande le réglage
`between_tools` pour s'en approcher. Trois paramètres d'API ont par ailleurs disparu dans
la version du 21 octobre, avec une erreur 400 à la clé.

Une échéance proche : Sonnet 4.5 est retiré le 30 novembre 2026.

## Ce qui reste ouvert

**La zone d'exécution.** C'était la question la plus importante de l'axe et la réponse est
négative. Seules deux valeurs existent, mondiale ou États-Unis. Aucune région européenne
n'est documentée, par aucune voie. Deux pistes non instruites restent ouvertes, les points
d'accès régionaux de Bedrock et un hôte européen aperçu dans la voie Google managed.

Tant qu'elles ne sont pas vérifiées, la conclusion tient : pour garder l'inférence dans un
périmètre européen, les voies documentées ne suffisent pas.

**Les system cards** n'ont pas été lues. C'est là qu'est le protocole complet des
évaluations. Une séance entière à y consacrer plutôt qu'un passage de quinze minutes.

**Un écart entre deux pages officielles** sur la disponibilité des modèles 4.5, et une
contradiction sur le tarif de Haiku 5.5 au-delà du seuil. Les deux sont notées dans le
comparatif et attendent une relecture.
