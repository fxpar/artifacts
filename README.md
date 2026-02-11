# Artifacts

| English | Français |
| - | - |
| Demo v1: [chess-famous-games-reader](https://fxpar.github.io/artifacts/chess-famous-games-reader/chess-v1.html) | Démo v1: [echec-parties-celebres](https://fxpar.github.io/artifacts/echec-parties-celebres/echec-v1.html) |
| Demo v2: [chess-famous-games-reader](https://fxpar.github.io/artifacts/chess-famous-games-reader/chess-v2.html) | Démo v2: [echec-parties-celebres](https://fxpar.github.io/artifacts/echec-parties-celebres/echec-v2.html) |

_____________

# Artifacts

Artefacts (petits outils) créés par IA pour différentes utilités

## Moodle

- [Sélecteur questions moodle par catégorie et tag](moodle-xml-selecteur): Obtenir les questions moodle filtrées sur certaines catégories et certains tags et certains types, à partir d'un grand fichier de questions. Inclus une prévisualisation des questions.
- [Moodle cloze en html:](moodle-cloze-html)Convertit les questions cloze de moodle en question accessible sur une page web hors moodle. (Utile pour les écoles qui n'ont pas de plateforme).
- [moodle-xml-traduction:](moodle-xml-traduction)(imparfait) Permet d'avoir un fichier de questions allégé (sans les images) pour le faire traduire par une IA et le réinjecter dans moodle. (il y a des erreurs qui bloquent lors du réimport... impossible de voir pourquoi).
- [moodle-xml-text](moodle-xml-text): Extrait le maximum de texte du fichier d'une banque de question. Utilité: permet de donner les questions à une IA qui va construire le support de cours correspondant aux évaluations

## Blackboard

- [moodle-cloze-blackboard-fill-blank](moodle-cloze-blackboard-fill-blank): Convertit un fichier xml de questions cloze moodle en questions "FIB" (Texte à trou, fill in the blank) de Blackboard. Le résultat n'est pas un fichier d'import, mais le texte de la question à copier-coller (en texte brut Ctrl+maj+V) dans les questions FIB, qui est parfaitement traité en faisant "étape suivante" (next step) dans blackboard.

## Chinois

- [Chinois Pynyin tons](chinois-pinyin-tons)
- [Chinois Convertisseur simplifié - traditionnel](chinois-simp-trad)

## Divers

- [data-en-cards](data-en-cards): Remplit des modèles de "cartes" à partir de données json ou csv
- [word-sans-titres](word-sans-titres): Retire le "niveau de titre" tout en conservant la mise en forme (utile pour créer un exercice où les étudiants doivent refaire la table des matières)
- [tableau-excel-word-html](tableau-excel-word-html): convertit des tableaux Excel ou Word en html, en choisissant des paramètres: ajouter les numéros de ligne et lettre des colonne, conserver les formats, les symboles monétaires...
- [tableaux-excel-word-markdown-json-csv](tableaux-excel-word-markdown-json-csv): permet de transformer différents tableaux Excel / Word en markdown, csv ou json
- [markdown-html](markdown-html): Convertit du markdown en html: attention, beaucoup de caractères sont transformé en entité (l'apostrophe et les accents sont convertis pour avoir un format html strict)
