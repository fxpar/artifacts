import os
import re
from pypdf import PdfReader, PdfWriter
import gradio as gr

DOSSIER_SOMMAIRES = "sommaires"

def obtenir_taille_ko(chemin_fichier):
    """Retourne la taille d'un fichier en Ko formaté."""
    try:
        taille_octets = os.path.getsize(chemin_fichier)
        return f"({taille_octets // 1024} Ko)"
    except Exception:
        return ""

def lister_pdf_dossier(chemin_dossier):
    """Scanne le dossier sélectionné et met à jour la liste déroulante."""
    if not chemin_dossier or not os.path.isdir(chemin_dossier):
        return gr.update(choices=[], value=None), "Veuillez entrer un chemin de dossier valide.", "", "", ""
    
    fichiers = [f for f in os.listdir(chemin_dossier) if f.lower().endswith('.pdf')]
    fichiers.sort()
    
    if not fichiers:
        return gr.update(choices=[], value=None), "Aucun fichier PDF trouvé dans ce dossier.", "", "", ""
        
    info = f" Dossier chargé. {len(fichiers)} fichiers PDF trouvés."
    return gr.update(choices=fichiers, value=fichiers[0] if fichiers else None), info, "", "", ""

def selectionner_pdf(chemin_dossier, nom_fichier):
    """Gère la sélection et génère des liens web locaux gérés par Gradio (sans doublons)."""
    if not chemin_dossier or not nom_fichier:
        return "Sélection incomplète.", "", ""
        
    chemin_pdf_original = os.path.join(chemin_dossier, nom_fichier)
    chemin_sommaire = os.path.join(chemin_dossier, DOSSIER_SOMMAIRES, f"sommaire_{nom_fichier}")
    
    # Au lieu de file:///, on crée l'URL native que Gradio sait router de manière sécurisée
    # On remplace les anti-slashs Windows par des slashs standards
    url_original = f"/gradio_api/file={chemin_pdf_original.replace('\\', '/')}"
    url_sommaire = f"/gradio_api/file={chemin_sommaire.replace('\\', '/')}"

    # 1. Infos et lien fichier original
    if os.path.exists(chemin_pdf_original):
        taille_orig = obtenir_taille_ko(chemin_pdf_original)
        try:
            reader = PdfReader(chemin_pdf_original)
            nb_pages = len(reader.pages)
        except Exception:
            nb_pages = "?"
            
        html_orig = f' Fichier cible : <a href="{url_original}" target="_blank" style="color: #2b6cb0; font-weight: bold; text-decoration: underline;">{nom_fichier}</a> {taille_orig} — {nb_pages} pages.'
    else:
        html_orig = " Fichier original introuvable."

    # 2. Infos et lien fichier sommaire
    if os.path.exists(chemin_sommaire):
        taille_somm = obtenir_taille_ko(chemin_sommaire)
        html_somm = f' Sommaire trouvé : <a href="{url_sommaire}" target="_blank" style="color: #2b6cb0; font-weight: bold; text-decoration: underline;">{DOSSIER_SOMMAIRES}/sommaire_{nom_fichier}</a> {taille_somm}'
    else:
        html_somm = f' Aucun sommaire trouvé <span style="color: #a0aec0;">(Attendu: {DOSSIER_SOMMAIRES}/sommaire_{nom_fichier})</span>'
        
    return html_orig, html_somm

def analyser_texte_signets(texte):
    """Analyse le contenu de la textarea en temps réel."""
    text_strip = texte.strip()
    if not text_strip:
        return "Lignes : 0 | Signets valides détectés : 0"
        
    lignes = text_strip.split('\n')
    nb_lignes = len(lignes)
    
    nb_signets_valides = 0
    for ligne in lignes:
        if re.search(r'\d+\s*$', ligne.strip()):
            nb_signets_valides += 1
            
    return f"Lignes au total : {nb_lignes} | Signets valides (avec page) : {nb_signets_valides}"

def executer_insertion(chemin_dossier, nom_fichier, texte_signets, offset):
    """Injecte les signets."""
    if not chemin_dossier or not nom_fichier:
        return "Erreur : Aucun fichier sélectionné."
    if not texte_signets.strip():
        return "Erreur : Le texte des signets est vide."
        
    chemin_pdf = os.path.join(chemin_dossier, nom_fichier)
    lignes = texte_signets.strip().split('\n')
    
    try:
        reader = PdfReader(chemin_pdf)
        total_pages = len(reader.pages)
        writer = PdfWriter()
        
        for page in reader.pages:
            writer.add_page(page)
            
        if reader.outline:
            writer.append_outline_from_reader(reader)
            
        signets_ajoutes = 0
        erreurs_lignes = []
        
        for i, ligne in enumerate(lignes, 1):
            ligne_clean = ligne.strip()
            if not ligne_clean:
                continue
                
            match = re.search(r'(\d+)\s*$', ligne_clean)
            if match:
                num_page_sommaire = int(match.group(1))
                num_page_reel = num_page_sommaire + offset
                
                titre = ligne_clean[:match.start()].strip()
                titre = titre.rstrip('. -_')
                
                if 1 <= num_page_reel <= total_pages:
                    writer.add_outline_item(titre, num_page_reel - 1)
                    signets_ajoutes += 1
                else:
                    erreurs_lignes.append(f"Ligne {i}: Page réelle {num_page_reel} hors limites (1-{total_pages}) pour '{titre}'")
            else:
                erreurs_lignes.append(f"Ligne {i}: Aucun numéro de page trouvé à la fin de '{ligne_clean}'")

        with open(chemin_pdf, "wb") as f_out:
            writer.write(f_out)
            
        resultat = f" Succès ! {signets_ajoutes} signets insérés dans '{nom_fichier}'."
        if erreurs_lignes:
            resultat += "\n\n Attention, des lignes ont été ignorées :\n" + "\n".join(erreurs_lignes[:10])
            if len(erreurs_lignes) > 10:
                resultat += f"\n... et {len(erreurs_lignes) - 10} autres erreurs."
                
        return resultat

    except Exception as e:
        return f" Erreur critique lors de l'insertion : {str(e)}"

# --- Interface Graphique Gradio ---
with gr.Blocks(title="Indexation Songbooks - Insertion") as demo:
    gr.Markdown("# Outil d'Indexation de Songbooks — Phase 2 : Injection de Signets")
    gr.Markdown("Indiquez votre dossier de travail, cliquez sur les fichiers pour les ouvrir, et injectez vos signets.")
    
    with gr.Row():
        # --- COLONNE GAUCHE ---
        with gr.Column(scale=1):
            gr.Markdown("### 1. Sélection du répertoire")
            input_dossier = gr.Textbox(
                label="Chemin absolu du dossier contenant les PDF", 
                placeholder="Ex: C:/Utilisateurs/Moi/Music/Songbooks"
            )
            btn_charger = gr.Button("Charger le dossier")
            txt_statut_dossier = gr.Textbox(label="Statut du dossier", interactive=False)
            
            gr.Markdown("### 2. Choix du Songbook")
            select_fichier = gr.Dropdown(label="Sélectionner le PDF à traiter", choices=[], interactive=True)
            
            gr.Markdown("### 3. Liens d'accès rapides (Cliquables)")
            # Utilisation de gr.HTML pour rendre les liens cliquables
            txt_info_original = gr.HTML("<p style='color: #a0aec0;'>*Aucun fichier sélectionné*</p>")
            txt_info_sommaire = gr.HTML("")

        # --- COLONNE DROITE ---
        with gr.Column(scale=1):
            gr.Markdown("### 4. Configuration des Signets")
            input_texte_signets = gr.Textbox(
                label="Coller le texte du sommaire ici", 
                placeholder="Exemple :\nAu clair de la lune 5\nUne souris verte 8", 
                lines=12
            )
            txt_compteur_analyse = gr.Textbox(label="Analyse du texte (Temps réel)", value="Lignes : 0 | Signets valides : 0", interactive=False)
            
            input_offset = gr.Number(label="Offset de page (Décalage à ajouter)", value=2, precision=0)
            
            btn_inserer = gr.Button(" Insérer les signets dans le PDF", variant="primary")
            txt_resultat_final = gr.Textbox(label="Résultat de l'opération", lines=4, interactive=False)

    # --- ÉVÉNEMENTS ---
    btn_charger.click(
        fn=lister_pdf_dossier,
        inputs=[input_dossier],
        outputs=[select_fichier, txt_statut_dossier, txt_info_original, txt_info_sommaire, input_texte_signets]
    )
    
    select_fichier.change(
        fn=selectionner_pdf,
        inputs=[input_dossier, select_fichier],
        outputs=[txt_info_original, txt_info_sommaire]
    )
    
    input_texte_signets.change(
        fn=analyser_texte_signets,
        inputs=[input_texte_signets],
        outputs=[txt_compteur_analyse]
    )
    
    btn_inserer.click(
        fn=executer_insertion,
        inputs=[input_dossier, select_fichier, input_texte_signets, input_offset],
        outputs=[txt_resultat_final]
    )

if __name__ == "__main__":
    # On autorise Gradio à créer des liens directs vers les fichiers de ton ordinateur
    demo.launch(allowed_paths=["C:/","D:/", ]) # Ajoute les lettres de lecteurs où se trouvent tes PDF