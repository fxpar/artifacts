import os
import json
from pypdf import PdfReader

def extraire_signets_rec(outline, lecteur):
    """Fonction récursive pour extraire les signets, même imbriqués."""
    liste_signets = []
    for item in outline:
        if isinstance(item, list):
            # C'est une sous-section imbriquée
            liste_signets.extend(extraire_signets_rec(item, lecteur))
        else:
            # C'est un signet direct
            titre = item.get('/Title', 'Sans titre')
            # Optionnel : récupérer le numéro de page si besoin
            try:
                page_num = lecteur.get_destination_page_number(item) + 1
                liste_signets.append(f"{titre} (Page {page_num})")
            except Exception:
                liste_signets.append(titre)
    return liste_signets

def generer_rapport_pdf():
    dossier_courant = os.getcwd()
    nom_dossier = os.path.basename(dossier_courant)
    
    fichiers_sans_signets = []
    fichiers_avec_signets = {}

    # Scanner le dossier courant pour trouver les PDF
    for fichier in os.listdir(dossier_courant):
        if fichier.lower().endswith('.pdf'):
            chemin_complet = os.path.join(dossier_courant, fichier)
            
            try:
                reader = PdfReader(chemin_complet)
                outline = reader.outline
                
                if not outline:
                    fichiers_sans_signets.append(fichier)
                else:
                    signets_extraits = extraire_signets_rec(outline, reader)
                    fichiers_avec_signets[fichier] = signets_extraits
            except Exception as e:
                print(f"Erreur lors de la lecture de {fichier} : {e}")

    # Structuration du JSON final selon tes souhaits
    data_json = {
        "nom_du_dossier": nom_dossier,
        "fichiers_sans_signets_a_faire_a_la_main": fichiers_sans_signets,
        "fichiers_avec_signets": fichiers_avec_signets
    }

    # Écriture dans le fichier JSON
    fichier_sortie = "signets_pdf.json"
    with open(fichier_sortie, 'w', encoding='utf-8') as f:
        json.dump(data_json, f, ensure_ascii=False, indent=4)
    
    print(f"Extraction terminée ! Le fichier '{fichier_sortie}' a été créé avec succès.")

if __name__ == "__main__":
    generer_rapport_pdf()