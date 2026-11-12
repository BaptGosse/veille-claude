# Glossaire - Modèles

**Contexte, fenêtre de** - la quantité de texte que le modèle peut avoir sous les yeux en
une fois, invite et réponse comprises. Un million de tokens sur les modèles courants.

**Covered model** - le terme de la documentation pour un modèle soumis à des obligations
particulières de rétention. Fable et Mythos en sont. Conséquence pratique : ils sont
exclus du zero data retention.

**Effort** - le réglage qui décide de la quantité de raisonnement que le modèle produit
avant de répondre. Les scores publiés sont relevés à l'effort maximum, les usages
courants tournent souvent à medium. Comparer deux chiffres relevés à des efforts
différents n'a pas de sens.

**Fast mode** - une option qui accélère la réponse jusqu'à 2,5 fois contre un tarif plus
élevé. Facturé 16 et 80 dollars sur Fable 5.2.

**Harnais** - tout ce qui entoure le modèle pendant une évaluation, les outils dont il
dispose, le nombre d'essais, le budget de tokens. Deux harnais différents donnent deux
scores différents pour le même modèle.

**Inference geo** - le réglage qui décide de la zone où tourne l'inférence, requête par
requête. Deux valeurs seulement, `global` par défaut et `us`.

**Palier tarifaire** - un seuil à partir duquel le prix au token change. Haiku 5.5 en a un
à 100 000 tokens d'invite.

**Preserved thinking** - une protection contre la copie du raisonnement du modèle par un
tiers. Appliquée à tous les comptes depuis Fable 5.2.

**Responsable de traitement** - celui qui répond juridiquement des données traitées. Selon
la voie de déploiement, c'est Anthropic ou le fournisseur de cloud. Se décide avant le
choix du modèle.

**Token** - l'unité dans laquelle se comptent le texte traité et la facture. Ni un mot ni
un caractère, d'où la difficulté à estimer un coût à l'avance.

**Workspace geo** - la zone de stockage des données au repos. Une seule valeur disponible,
`us`.

**ZDR, zero data retention** - un accord sous lequel Anthropic ne conserve ni les invites
ni les réponses après l'appel. Ne s'active pas tout seul, se demande au commercial, et
vaut par organisation.
