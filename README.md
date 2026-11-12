# Artifacts — petits outils pour enseignants et formateurs

Une collection de petits outils web créés avec l'aide de l'IA, pour gagner du temps au quotidien : Moodle, Blackboard, supports de cours, tableaux, données…

🌐 **Site des outils : https://fxpar.github.io/artifacts/**

Chaque outil est une simple page HTML : il s'ouvre dans le navigateur, sans installation ni compte.

> 🔒 **Vos données restent chez vous.** Les fichiers que vous déposez sont traités dans votre navigateur et ne sont envoyés à aucun serveur. Seules exceptions, signalées dans l'outil concerné : l'analyse par IA de l'échiquier v3 (envoi de la position à Google Gemini, avec votre propre clé) et le générateur de blasons (récupération des icônes sur Iconify).

## Moodle

| Outil | Description |
| - | - |
| [Sélecteur de questions](https://fxpar.github.io/artifacts/moodle-xml-selecteur/) | Extrait d'une grosse banque de questions Moodle (XML) les questions de certaines catégories, étiquettes et types, avec prévisualisation. |
| [Questions Cloze en HTML](https://fxpar.github.io/artifacts/moodle-cloze-html/quiz.html) | Transforme des questions Cloze Moodle en quiz sur une page web autonome, pour les écoles sans plateforme. |
| [Texte d'une banque de questions](https://fxpar.github.io/artifacts/moodle-xml-text/) | Extrait tout le texte d'une banque de questions, par exemple pour demander à une IA de rédiger le support de cours correspondant aux évaluations. |
| [Traduction de questions](https://fxpar.github.io/artifacts/moodle-xml-traduction/) | *(Imparfait)* Allège un fichier de questions (sans images) pour le faire traduire par une IA puis le réimporter. Certains réimports échouent encore. |

## Blackboard

| Outil | Description |
| - | - |
| [Rapport d'enquête Blackboard](https://fxpar.github.io/artifacts/blackboard-forms/) | Transforme l'export CSV / Excel d'une enquête Blackboard en rapport imprimable : graphiques pour les questions à choix, citations anonymisées pour les réponses libres. |
| [Cloze Moodle → texte à trous Blackboard](https://fxpar.github.io/artifacts/moodle-cloze-blackboard-fill-blank/) | Convertit des questions Cloze Moodle (XML) en questions « Fill in the blank » Blackboard. Le résultat est un texte à coller (Ctrl+Maj+V) dans la question, que Blackboard traite ensuite avec « Étape suivante ». |

## Supports de cours

| Outil | Description |
| - | - |
| [Md2Bootstrap](https://fxpar.github.io/artifacts/md2bootstrap/) | Met en forme un support de cours Markdown (rédigé par une IA, par exemple) avec Bootstrap 5, en deux versions : bloc pour Moodle, page complète pour Blackboard. |
| [Markdown ↔ HTML](https://fxpar.github.io/artifacts/markdown-html/) | Convertit du Markdown en HTML et inversement. Les accents et apostrophes sont convertis en entités HTML pour un code strict. |
| [Word sans titres](https://fxpar.github.io/artifacts/word-sans-titres/) | Retire les niveaux de titre d'un document Word en gardant la mise en forme : idéal pour un exercice où les étudiants doivent refaire la table des matières. |
| [Données en cartes](https://fxpar.github.io/artifacts/data-en-cards/) | Remplit un modèle de carte à partir de données JSON ou CSV, puis imprime les cartes en PDF. |
| [Radar de compétences](https://fxpar.github.io/artifacts/test-recrutement-radar/test-IA.html) | Crée un graphique radar à partir d'un référentiel de compétences et de résultats de tests. |

## Tableaux et données

| Outil | Description |
| - | - |
| [Tableau Excel / Word → HTML](https://fxpar.github.io/artifacts/tableau-excel-word-html/) | Convertit un tableau Excel ou Word en HTML, avec options : numéros de ligne et lettres de colonne, conservation des formats, symboles monétaires… |
| [Tableaux → Markdown, CSV, JSON](https://fxpar.github.io/artifacts/tableaux-excel-word-markdown-json-csv/) | Convertit des tableaux Excel ou Word en Markdown, CSV ou JSON. |
| [JSON → Markdown](https://fxpar.github.io/artifacts/json-to-markdown/) | Rend un fichier JSON lisible : les clés deviennent des titres, les tableaux des listes. |
| [JSON Visualizer](https://fxpar.github.io/artifacts/json-visualizer/) | Affiche un JSON en grand et en couleur, pour zoomer dessus à l'écran (créé pour une vidéo). |
| [Yahoo Finance → Excel](https://fxpar.github.io/artifacts/yahoo-finance-html-excel/) | Nettoie le tableau d'historique des cours copié depuis Yahoo Finance et le prépare pour Excel. |

## Chinois

| Outil | Description |
| - | - |
| [Hanzi → pinyin](https://fxpar.github.io/artifacts/chinois-pinyin-tons/) | Ajoute le pinyin avec les tons à un texte chinois : après chaque caractère, au-dessus (ruby) ou en fin de texte. |
| [Simplifié → traditionnel](https://fxpar.github.io/artifacts/chinois-simp-trad/) | Convertit un texte en caractères simplifiés vers les caractères traditionnels. |

## Graphisme

| Outil | Description |
| - | - |
| [ShieldForge](https://fxpar.github.io/artifacts/shield-generator/) | Crée des blasons et badges personnalisés (icônes, forme, banderole) et les exporte en SVG ou PNG. |

## Échecs et démonstrations d'IA

| Outil | Description |
| - | - |
| [Parties d'échecs célèbres](echec-parties-celebres) | Lecteur de parties célèbres ([v1](https://fxpar.github.io/artifacts/echec-parties-celebres/echec-v1.html), [v2](https://fxpar.github.io/artifacts/echec-parties-celebres/echec-v2.html), [v3](https://fxpar.github.io/artifacts/echec-parties-celebres/echec-v3.html)). La v3 montre aux étudiants comment une application peut interroger une IA en pleine partie pour proposer plusieurs scénarios de coups. |
| [Chess famous games reader](chess-famous-games-reader) | Version anglaise ([v1](https://fxpar.github.io/artifacts/chess-famous-games-reader/chess-v1.html), [v2](https://fxpar.github.io/artifacts/chess-famous-games-reader/chess-v2.html)). |

## Scripts Python

| Outil | Description |
| - | - |
| [pdf-manipulator](pdf-manipulator) | Scripts Python pour gérer les signets de gros PDF (recueils de partitions notamment) : extraction des sommaires et des pages, injection d'index. Nécessite Python : ne s'exécute pas dans le navigateur. |

## Autres dépôts

- [abc-notation-artifacts](https://github.com/fxpar/abc-notation-artifacts) : mini-applications autour de la notation musicale ABC, un langage texte très simple pour écrire des partitions et les écouter (pratique pour créer une boucle d'accords sur laquelle improviser).

## Licence

[MIT](LICENSE) : vous pouvez utiliser, copier, modifier et redistribuer ces outils librement, y compris à des fins commerciales, à condition de conserver la mention de copyright. Aucune garantie n'est fournie.
