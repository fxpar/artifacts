
# 🎵 Outils d'Indexation pour Songbooks & PDF

Ce dépôt contient un ensemble de scripts Python conçus pour automatiser et simplifier la gestion, l'extraction de sommaires et l'injection de signets (index) dans des fichiers PDF volumineux, particulièrement adaptés aux recueils de partitions de musique (*songbooks*).

> 💡 **Note importante au lancement**
> Certains de ces scripts lancent une interface graphique moderne directement dans votre navigateur internet via un serveur local **Gradio**. Lors de l'exécution, un lien de type `[http://127.0.0.1:7860](http://127.0.0.1:7860)` s'affichera dans votre terminal : il suffit de cliquer dessus pour ouvrir l'application ou de copier l'adresse dans un navigateur pour voir le résultat.

---

## 📋 Présentation des Scripts

### 1. `pdf-signets-extracteur.py`

* **Son utilité :** Il scanne l'intégralité du dossier courant à la recherche de fichiers PDF. Il extrait ensuite la liste de tous les signets existants pour générer un fichier d'index au format `JSON`.
* **Le petit + :** Il liste en priorité (au tout début du fichier) tous les PDF qui ne possèdent **aucun signet**, vous permettant de savoir immédiatement quels livres restent à indexer.
* **Personnalisation simple :** Vous pouvez modifier la variable `PROFONDEUR_MAX` directement dans le script. Par exemple, réglez-la sur `1` pour n'extraire que les grands titres (idéal pour les songbooks avec un morceau par page) ou augmentez-la si vous voulez les sous-sections.

### 2. `pdf-pages-extracteur.py`

* **Son utilité :** Ce script fournit une interface graphique simple pour découper vos fichiers PDF. Il vous permet de sélectionner un document et d'extraire précisément une ou plusieurs pages de votre choix pour créer un nouveau fichier PDF plus léger.

* **Exemple de syntaxe:** La formule 15,3,5-8,10 créera un fichier pdf avec les pages 15,3,5,6,7,8 et 10. Le trait d'union veut dire "jusqu'à".

* **Le petit + :** Contrairement à d'autre librairies, ce script ne tient pas compte de la "restriction admin" qui parfois bloque l'extraction. (Ce contournement du mot de passe ne s'applque qu'au mot de passe "propriétaire", pas au mot de passe utilisateur).

### 3. `json-pdf-sommaires.py`

* **Son utilité :** Une interface graphique dédiée à la préparation de vos documents. En chargeant le fichier `JSON` généré par le premier script, il vous liste tous les PDF qui n'ont pas de signets.
* **Le fonctionnement :** Vous sélectionnez un fichier dans la liste, déterminez les pages correspondantes au sommaire du livre (ex: `1, 3-5`), et le script isole automatiquement ces pages dans un sous-dossier appelé `sommaires`. Vous n'avez plus qu'à envoyer ces sommaires légers à une IA pour qu'elle en extrait les titres au propre ! (ou vous pouvez demander à une IA en local de faire l'analyse, si les données sont confidentielles).

### 4. `pdf-insertion-signets.py`

* **Son utilité :** L'outil final pour injecter vos index en une fois dans les pdf. Cette interface graphique vous permet de sélectionner votre dossier de travail, de coller la liste textuelle des morceaux générée par votre IA (titre + numéro de page) et d'automatiser la création des signets dans le PDF original.
* **Le petit + :** Il intègre la gestion d'un "Offset" (décalage de pages) si la numérotation du sommaire papier ne correspond pas tout à fait aux pages réelles du fichier PDF.

* **Format attendu :** chaque ligne contient un signet et se termine par le numéro de page.

---

## ⚙️ Configuration & Personnalisation de base

Les scripts ont été conçus pour être simples et ne demandent aucune compétence technique avancée. Voici les seuls ajustements que vous pouvez faire directement au début ou à la fin des fichiers `.py` avec un simple éditeur de texte :

* **Lettres de partitions (Lecteurs Windows) :** Dans le script `pdf-insertion-signets.py`, tout en bas du fichier, vous pouvez modifier le paramètre `allowed_paths=["C:/", "D:/"]` dans la ligne `demo.launch(...)`. Ajoutez-y les lettres des disques durs de votre ordinateur où sont stockés vos PDF pour que l'application puisse ouvrir vos liens instantanément sans restriction de sécurité.
* **Profondeur d'extraction :** Dans `pdf-signets-extracteur.py`, modifiez le chiffre de `PROFONDEUR_MAX = 1` pour filtrer le niveau de détail des index que vous récupérez.

---

*Développé pour les musiciens et les amoureux de PDF bien organisés ! 🎸🎹*