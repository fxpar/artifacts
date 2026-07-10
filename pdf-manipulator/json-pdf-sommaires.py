import os
import json
from pypdf import PdfReader, PdfWriter
import gradio as gr

# Dossier cible pour isoler les sommaires
DOSSIER_SOMMAIRES = "sommaires"

def analyser_plage_pages(texte_plage, total_pages):
    """
    Convertit une chaîne du type '1,2-3,5-6' en une liste d'index de pages (0-indexed).
    """
    pages_a_extraire = set()
    if not texte_plage.strip():
        return list(pages_a_extraire)
        
    parties = texte_plage.split(',')
    for partie in parties:
        partie = partie.strip()
        if '-' in partie:
            try:
                debut, fin = partie.split('-')
                debut = int(debut.strip())
                fin = int(fin.strip())
                # Sécurité pour ne pas déborder du document
                debut = max(1, min(debut, total_pages))
                fin = max(1, min(fin, total_pages))
                for p in range(debut, fin + 1):
                    pages_a_extraire.add(p - 1)
            except ValueError:
                continue
        else:
            try:
                p = int(partie)
                if 1 <= p <= total_pages:
                    pages_a_extraire.add(p - 1)
            except ValueError:
                continue
                
    return sorted(list(pages_a_extraire))

def charger_donnees_json(fichier_json):
    """Phase de chargement (Points 1 & 2)"""
    if fichier_json is None:
        return gr.update(choices=[]), "Veuillez sélectionner un fichier JSON valide."
    
    try:
        with open(fichier_json.name, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        fichiers = data.get("fichiers_sans_signets_a_faire_a_la_main", [])
        
        if not fichiers:
            return gr.update(choices=[]), "Aucun fichier sans signet trouvé dans ce JSON."
            
        statut = f" JSON chargé avec succès. {len(fichiers)} fichiers trouvés à traiter."
        return gr.update(choices=fichiers, value=fichiers[0] if fichiers else None), statut
    except Exception as e:
        return gr.update(choices=[]), f"Erreur lors de la lecture du JSON : {str(e)}"

def selectionner_fichier(nom_fichier):
    """Affichage central (Point 4)"""
    if not nom_fichier:
        return None, "Aucun fichier sélectionné."
    
    if not os.path.exists(nom_fichier):
        return None, f"Fichier introuvable dans le dossier courant : {nom_fichier}"
        
    try:
        reader = PdfReader(nom_fichier)
        nb_pages = len(reader.pages)
        info = f"Fichier sélectionné : {nom_fichier} | Nombre total de pages : {nb_pages}"
        return nom_fichier, info
    except Exception as e:
        return None, f"Erreur lors de la lecture du PDF : {str(e)}"

def extraire_sommaire(nom_fichier, plage_pages):
    """Phase d'extraction du sommaire (Points 5 & 6)"""
    if not nom_fichier or not os.path.exists(nom_fichier):
        return "Erreur : Aucun fichier PDF valide sélectionné."
        
    if not plage_pages.strip():
        return "Erreur : Veuillez spécifier la plage de pages (ex: 1, 3-5)."

    try:
        reader = PdfReader(nom_fichier)
        total_pages = len(reader.pages)
        
        indexes_pages = analyser_plage_pages(plage_pages, total_pages)
        
        if not indexes_pages:
            return "Erreur : Aucune page valide identifiée après analyse de la saisie."
            
        # Création du sous-dossier s'il n'existe pas
        if not os.path.exists(DOSSIER_SOMMAIRES):
            os.makedirs(DOSSIER_SOMMAIRES)
            
        writer = PdfWriter()
        for idx in indexes_pages:
            writer.add_page(reader.pages[idx])
            
        nom_sortie = os.path.join(DOSSIER_SOMMAIRES, f"sommaire_{nom_fichier}")
        
        with open(nom_sortie, "wb") as f_out:
            writer.write(f_out)
            
        pages_humaines = [str(idx + 1) for idx in indexes_pages]
        return f" Extraction réussie ! Pages [{', '.join(pages_humaines)}] enregistrées dans : {nom_sortie}"
        
    except Exception as e:
        return f"Erreur lors de l'extraction : {str(e)}"

# --- Interface Web Gradio ---
with gr.Blocks(title="Indexation Songbooks - Extraction") as demo:
    gr.Markdown("# Outil d'Indexation de Songbooks — Phase 1 : Extraction")
    gr.Markdown("Téléversez votre JSON, naviguez dans vos fichiers sans signets, et isolez les pages de sommaire pour votre IA.")
    
    with gr.Row():
        # COLONNE DE GAUCHE : Contrôles et Paramètres
        with gr.Column(scale=1):
            gr.Markdown("### 1. Chargement de la liste")
            bouton_json = gr.File(label="Sélectionner le fichier JSON", file_types=[".json"])
            txt_statut_json = gr.Textbox(label="Statut du JSON", interactive=False)
            
            gr.Markdown("### 2. Sélection du Fichier")
            select_fichier = gr.Dropdown(label="Fichiers sans signets restants", choices=[], interactive=True)
            
            gr.Markdown("### 3. Extraction du Sommaire")
            input_plage = gr.Textbox(
                label="Pages du sommaire", 
                placeholder="Ex: 1, 2-3, 5", 
                info="Format : numéros séparés par des virgules ou plages (ex: 1,2-4)"
            )
            btn_extraire = gr.Button(" Extraire le Sommaire", variant="primary")
            txt_statut_extraction = gr.Textbox(label="Résultat", interactive=False)

        # COLONNE DE DROITE : Visionneuse centrale du PDF
        with gr.Column(scale=2):
            gr.Markdown("### Visionneuse de document")
            txt_info_pdf = gr.Textbox(label="Propriétés du fichier", interactive=False)
            view_pdf = gr.File(label="Aperçu du PDF sélectionné", interactive=False)

    # Définition des interactions (Logique événementielle)
    bouton_json.change(
        fn=charger_donnees_json, 
        inputs=[bouton_json], 
        outputs=[select_fichier, txt_statut_json]
    )
    
    select_fichier.change(
        fn=selectionner_fichier,
        inputs=[select_fichier],
        outputs=[view_pdf, txt_info_pdf]
    )
    
    btn_extraire.click(
        fn=extraire_sommaire,
        inputs=[select_fichier, input_plage],
        outputs=[txt_statut_extraction]
    )

if __name__ == "__main__":
    demo.launch()