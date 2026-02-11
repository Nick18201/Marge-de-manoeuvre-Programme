import os
import urllib.request
import ssl

# --- CONFIGURATION ---
FONTS_DIR = r"c:\Users\nblum\LLM_LAB\PROJETS\MDM programme\00_Gestion_Projet\assets\fonts"

# URLs directes vers les versions "Static"
fonts_to_download = [
    {
        "name": "Montserrat-Bold.ttf",
        "url": "https://github.com/google/fonts/raw/main/ofl/montserrat/static/Montserrat-Bold.ttf"
    },
    {
        "name": "Caveat-Regular.ttf",
        "url": "https://github.com/google/fonts/raw/main/ofl/caveat/static/Caveat-Regular.ttf"
    },
    {
        "name": "AmaticSC-Regular.ttf",
        "url": "https://github.com/google/fonts/raw/main/ofl/amaticsc/AmaticSC-Regular.ttf" 
    },
    {
        "name": "Lato-Regular.ttf",
        "url": "https://github.com/google/fonts/raw/main/ofl/lato/Lato-Regular.ttf"
    },
    {
        "name": "Lato-Italic.ttf",
        "url": "https://github.com/google/fonts/raw/main/ofl/lato/Lato-Italic.ttf"
    }
]

# --- FONCTIONS ---

def download_fonts():
    # 1. Création du dossier
    if not os.path.exists(FONTS_DIR):
        try:
            os.makedirs(FONTS_DIR)
            print(f"[OK] Dossier créé : {FONTS_DIR}")
        except OSError as e:
            print(f"[ERREUR] Impossible de créer le dossier : {e}")
            return

    # 2. Configuration pour contourner les erreurs SSL (pare-feu / proxy)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # 3. Boucle de téléchargement
    print("--- Démarrage des téléchargements ---")
    
    for font in fonts_to_download:
        dest_path = os.path.join(FONTS_DIR, font["name"])
        
        # Optionnel: Supprimer si taille 0 (téléchargement échoué précédent)
        if os.path.exists(dest_path) and os.path.getsize(dest_path) == 0:
             os.remove(dest_path)

        if os.path.exists(dest_path):
            print(f"[INFO] {font['name']} existe déjà ({os.path.getsize(dest_path)} octets). Passé.")
            continue

        print(f"Téléchargement de {font['name']} depuis {font['url']}...")
        
        try:
            # On utilise un 'User-Agent' pour ne pas être bloqué par GitHub
            req = urllib.request.Request(
                font["url"], 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            
            with urllib.request.urlopen(req, context=ctx, timeout=30) as response:
                with open(dest_path, 'wb') as out_file:
                    out_file.write(response.read())
            
            size = os.path.getsize(dest_path)
            print(f"[SUCCÈS] {font['name']} téléchargé ({size} octets).")
            
        except Exception as e:
            print(f"[ÉCHEC] Erreur sur {font['name']} : {e}")

    print("--- Terminé ---")
    print(f"Vérifiez vos fichiers dans : {FONTS_DIR}")

if __name__ == "__main__":
    download_fonts()
