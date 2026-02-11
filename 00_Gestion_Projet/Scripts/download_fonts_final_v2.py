import os
import urllib.request
import ssl

# --- CONFIGURATION ---
FONTS_DIR = r"c:\Users\nblum\LLM_LAB\PROJETS\MDM programme\00_Gestion_Projet\assets\fonts"

# URLs CORRIGÉES (JulietaUla pour Montserrat, Google Fonts pour Caveat)
fonts_to_download = [
    {
        "name": "Montserrat-Bold.ttf",
        # Source alternative fiable (Repo officiel auteur)
        "url": "https://github.com/JulietaUla/Montserrat/raw/master/fonts/ttf/Montserrat-Bold.ttf"
    },
    {
        "name": "Caveat-Regular.ttf",
        # URL sans le dossier 'static' qui semble poser problème
        "url": "https://github.com/google/fonts/raw/main/ofl/caveat/Caveat-Regular.ttf"
    }
]

# --- FONCTIONS ---

def download_fonts():
    # 1. Création du dossier
    if not os.path.exists(FONTS_DIR):
        try:
            os.makedirs(FONTS_DIR)
        except OSError:
            pass

    # 2. Configuration SSL
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    print("--- Démarrage des téléchargements (URLs alternatives) ---")
    
    for font in fonts_to_download:
        dest_path = os.path.join(FONTS_DIR, font["name"])
        
        print(f"Téléchargement de {font['name']} depuis {font['url']}...")
        
        try:
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

if __name__ == "__main__":
    download_fonts()
