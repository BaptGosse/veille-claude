# Comparatif des modèles

C'est le tableau que les quatre autres axes viennent chercher quand ils doivent arbitrer.

**Dernière mise à jour : 12 novembre 2026.** Au-delà d'un mois sans mise à jour, ne pas
s'en servir pour décider, les sorties s'enchaînent trop vite.

Relevé sur https://platform.claude.com/docs/en/models/overview et
https://platform.claude.com/docs/en/about-claude/pricing

| Modèle | Identifiant API | Contexte | Sortie max | Prix entrée | Prix sortie |
| --- | --- | --- | --- | --- | --- |
| Fable 5.2 | `claude-fable-5-2` | 1 M | 128 k | 8 $ | 40 $ |
| Opus 5.5 | `claude-opus-5-5` | 1 M | 128 k | 4 $ | 20 $ |
| Sonnet 5.5 | `claude-sonnet-5-5` | 1 M | 128 k | 2 $ | 10 $ |
| Haiku 5.5 | `claude-haiku-5-5` | 1 M | 128 k | à partir de 0,10 $ | à partir de 0,50 $ |

Prix par million de tokens. Pour Haiku 5.5, le tarif passe à 2 $ en entrée et 2,50 $ en
sortie au-delà de 100 000 tokens d'invite. C'est le genre de seuil qui ne se voit pas sur
un poste de développeur et qui se voit très bien sur une facture de plateforme.

## Ce qui manque encore dans ce tableau

La colonne hébergement. La question de départ la plus importante de cet axe est de savoir
où un modèle peut tourner quand les données ne doivent pas sortir d'un périmètre défini,
et le tableau n'y répond pas encore. Il faut lire les pages de disponibilité par
plateforme, y compris les offres hébergées en Europe, et ajouter une colonne par
plateforme avec la région de traitement.

Tant que cette colonne est vide, le comparatif sert à arbitrer sur le coût et la
performance, pas sur la souveraineté.
