# Nettoyeur Yahoo Finance → Excel

[👉 Ouvrir l'outil](https://fxpar.github.io/artifacts/yahoo-finance-html-excel/)

Récupère l'historique des cours affiché sur Yahoo Finance à partir du code HTML du tableau, et le rend directement exploitable dans Excel (sans lignes parasites ni problème de format des nombres).

## Utilisation

1. Sur Yahoo Finance, ouvrez l'onglet **Historical Data** de l'action voulue.
2. Inspectez le tableau (clic droit → Inspecter), copiez l'élément `<table>` (clic droit → Copier → Copier l'élément).
3. Collez le code dans l'outil et cliquez sur **Nettoyer**.
4. Cliquez sur **Copier pour Excel** et collez dans une feuille.

## Ce que fait l'outil

- Garde uniquement : Date, Open, High, Low, Close, Adj Close, Volume.
- Supprime les lignes de dividendes et de fractionnement (splits).
- Format des nombres au choix : français (`1 234,56`) ou anglais (`1,234.56`).

## Confidentialité

Le traitement se fait dans le navigateur ; l'outil ne contacte pas Yahoo.

## Bibliothèques

Aucune (HTML, CSS et JavaScript seuls).
