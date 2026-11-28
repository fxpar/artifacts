# Lecteur de parties d'échecs célèbres

> **Version finale : [Chess Famous Games](https://edu-fpar.github.io/chess-famous-games/)** ([code](https://github.com/edu-fpar/chess-famous-games)) : parties vérifiées, moments clés commentés, mode « Devinez le coup », questions pour une IA sans clé API, mode jour / nuit, FR · EN · ES. Les versions ci-dessous restent comme étapes de l'exercice.

| Version | Démo |
| - | - |
| v1 | [echec-v1.html](https://fxpar.github.io/artifacts/echec-parties-celebres/echec-v1.html) |
| v2 | [echec-v2.html](https://fxpar.github.io/artifacts/echec-parties-celebres/echec-v2.html) |
| v3 | [echec-v3.html](https://fxpar.github.io/artifacts/echec-parties-celebres/echec-v3.html) |

## Version 1

* [x] Choix de parties
* [x] Bouton lecture / pause
* [x] Compteur de coups

## Version 2

* [x] Cimetière des pièces
* [x] Boutons pour se déplacer dans la partie

## Version 3 — démonstration d'un appel à une IA

* [x] Mode nuit, choix du thème des pièces, vitesse de lecture
* [x] Import d'une partie (PGN) et enregistrement dans le navigateur
* [x] **Analyse Gemini** : en pleine partie, l'application envoie la position à l'IA et lui demande trois scénarios pour le coup suivant (⚔️ agressif, 🕵️ sournois, ⚠️ erreur à éviter).

Cette version sert à montrer aux étudiants **comment une application peut interroger une IA par une requête API** au milieu de son fonctionnement, puis exploiter la réponse (au format JSON) dans son interface.

Pour l'essayer, il faut sa propre clé API Gemini (gratuite sur [Google AI Studio](https://aistudio.google.com/apikey)). La clé est saisie dans la page ; elle n'est envoyée qu'à Google, avec la position de la partie, au moment du clic sur « Envoyer à Gemini ».

## Création

Versions 1 et 2 créées en 3 minutes avec une IA gratuite (Gemini).

Tutoriel vidéo de création : https://www.youtube.com/watch?v=JLm4EEcDnMY

## Pédagogie

Projet basé sur la « phase 2 » du modèle *Teaching to the AI-mediated Mind* : https://osf.io/nxaqb_v1 — DOI : 10.35542/osf.io/nxaqb_v1

## Bibliothèques

[chess.js](https://github.com/jhlywa/chess.js), [chessboard.js](https://chessboardjs.com), [jQuery](https://jquery.com)
