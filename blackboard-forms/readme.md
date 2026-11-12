# Rapport d'enquête Blackboard

[👉 Ouvrir l'outil](https://fxpar.github.io/artifacts/blackboard-forms/)

Transforme l'export des réponses d'un formulaire ou d'une enquête Blackboard (CSV ou Excel) en rapport lisible et imprimable en PDF.

## Fonctionnalités

- Lit les exports Blackboard en français ou en anglais (`Nom d'utilisateur…Réponse` ou `Username…Answer`), en CSV (virgule, point-virgule ou tabulation), en `.xls` / `.xlsx`, ou en copier-coller depuis Excel.
- Détecte automatiquement le type de chaque question :
  - **question à choix** → graphique en barres avec nombre et pourcentage ;
  - **réponse libre** → liste de citations, avec regroupement des réponses identiques (« no ×6 »).
- Bouton ⇄ pour forcer le type d'une question si la détection se trompe (choix mémorisé dans le navigateur).
- Taux de réponse par question, nombre de participants.
- Réponses anonymisées par défaut (option pour afficher les noms).
- Ignore les lignes techniques (« Contenu supplémentaire », `<Unanswered>`, `<br>`…).
- Mise en page optimisée pour l'impression (Ctrl+P → Enregistrer au format PDF).

## Confidentialité

Les fichiers sont lus et traités dans votre navigateur : aucune réponse d'étudiant n'est envoyée à un serveur.

## Bibliothèques

- [Tailwind CSS](https://tailwindcss.com) (mise en page)
- [SheetJS](https://sheetjs.com) (lecture des fichiers Excel)
