import os
import gradio as gt
from pypdf import PdfReader, PdfWriter

def parse_page_range(range_str, max_pages):
    pages = set()
    parts = range_str.split(',')
    
    for part in parts:
        part = part.strip()
        if '-' in part:
            try:
                start, end = map(int, part.split('-'))
                if start <= end:
                    for i in range(start, end + 1):
                        if 1 <= i <= max_pages:
                            pages.add(i)
            except ValueError:
                continue
        else:
            try:
                page = int(part)
                if 1 <= page <= max_pages:
                    pages.add(page)
            except ValueError:
                continue
                
    # On trie et on passe en index 0 (Python commence à 0, les humains à 1)
    return [p - 1 for p in sorted(list(pages))]

def extraire_pdf(pdf_file, page_range, dossier_destination):
    if not pdf_file:
        return "❌ Erreur : Veuillez sélectionner un fichier PDF."
    if not page_range.strip():
        return "❌ Erreur : Veuillez indiquer les pages à extraire."
    if not dossier_destination.strip() or not os.path.exists(dossier_destination):
        return "❌ Erreur : Le dossier de destination n'existe pas ou est invalide."

    try:
        # Lecture du PDF (pypdf gère très bien les fichiers corrompus/chiffrés)
        reader = PdfReader(pdf_file.name)
        total_pages = len(reader.pages)
        
        # Calcul des pages
        page_indices = parse_page_range(page_range, total_pages)
        
        if not page_indices:
            return f"❌ Aucune page valide trouvée. Le PDF contient {total_pages} pages."
        
        # Création du nouveau PDF
        writer = PdfWriter()
        for idx in page_indices:
            writer.add_page(reader.pages[idx])
            
        # Construction du chemin de sortie
        nom_origine = os.path.splitext(os.path.basename(pdf_file.name))[0]
        nom_sortie = f"{nom_origine}_extraire.pdf"
        chemin_complet = os.path.join(dossier_destination, nom_sortie)
        
        # Écriture du fichier
        with open(chemin_complet, "wb") as f_out:
            writer.write(f_out)
            
        return f"✅ Succès ! Fichier enregistré ici :\n{chemin_complet}"
        
    except Exception as e:
        return f"❌ Une erreur est survenue : {str(e)}"

# Création de l'interface graphique ultra-légère
with gt.Blocks(title="Extracteur PDF Pro") as app:
    gt.Markdown("# 📄 Détacher des pages PDF")
    
    with gt.Row():
        fichier = gt.File(label="1. Choisir le fichier PDF", file_types=[".pdf"])
    
    with gt.Row():
        pages = gt.Textbox(label="2. Pages à extraire", placeholder="Ex: 2-4,5,8-10")
        
    with gt.Row():
        dossier = gt.Textbox(
            label="3. Dossier de destination (Chemin absolu)", 
            placeholder="Ex: C:\\Users\\VotreNom\\Desktop ou /home/user/Documents"
        )
        
    bouton = gt.Button("Démarrer l'extraction", variant="primary")
    statut = gt.Textbox(label="Résultat / Statut", interactive=False)
    
    bouton.click(
        fn=extraire_pdf, 
        inputs=[fichier, pages, dossier], 
        outputs=statut
    )

# Lancement de l'application
if __name__ == "__main__":
    app.launch(inbrowser=True)