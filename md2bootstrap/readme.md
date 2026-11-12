# Md2Bootstrap — supports de cours Markdown vers Moodle et Blackboard

[👉 Ouvrir l'outil](https://fxpar.github.io/artifacts/md2bootstrap/)

Convertit un support de cours rédigé en Markdown (par exemple généré par une IA) en page HTML mise en forme avec Bootstrap 5 et les icônes Font Awesome, prête à être collée dans Moodle ou Blackboard.

## Deux sorties

| Version | Contenu | Usage |
| - | - | - |
| **Moodle** | Un simple bloc `<div>` | À coller dans une page ou une étiquette Moodle (Moodle charge déjà Bootstrap) ; compatible mode clair / sombre |
| **Blackboard** | Une page HTML complète, avec les liens vers Bootstrap et Font Awesome | À déposer comme fichier HTML dans Blackboard |

Chaque version peut être copiée ou enregistrée en `.html`.

## Mise en forme appliquée

- `#` titre → bannière colorée ; `##` et `###` → titres avec icônes ;
- tableaux → tableaux Bootstrap responsives et rayés ;
- citations `>` → encarts « idée / à retenir » ;
- listes → listes stylisées avec coches ; `[ ]` / `[x]` → cases à cocher ;
- blocs de code → cartes sombres.

## Confidentialité

La conversion se fait entièrement dans le navigateur.

## Bibliothèques

[Marked](https://marked.js.org), [Bootstrap 5](https://getbootstrap.com), [Font Awesome](https://fontawesome.com), [Bootstrap Icons](https://icons.getbootstrap.com)
