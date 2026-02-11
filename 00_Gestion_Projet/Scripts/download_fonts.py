import os
import requests

FONTS_DIR = r"c:\Users\nblum\LLM_LAB\PROJETS\MDM programme\00_Gestion_Projet\assets\fonts"
os.makedirs(FONTS_DIR, exist_ok=True)

fonts_to_download = [
    {
        "name": "Montserrat-Bold.ttf",
        "candidates": [
             "https://github.com/google/fonts/raw/main/ofl/montserrat/Montserrat-Bold.ttf",
             "https://github.com/google/fonts/raw/main/ofl/montserrat/static/Montserrat-Bold.ttf"
        ]
    },
    {
        "name": "Caveat-Regular.ttf",
        "candidates": [
             "https://github.com/google/fonts/raw/main/ofl/caveat/Caveat-Regular.ttf",
             "https://github.com/google/fonts/raw/main/ofl/caveat/static/Caveat-Regular.ttf"
        ]
    }
]

for font_info in fonts_to_download:
    dest_path = os.path.join(FONTS_DIR, font_info["name"])
    print(f"Attempting to download {font_info['name']}...")
    
    success = False
    for url in font_info["candidates"]:
        try:
            print(f"Trying {url}...")
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                with open(dest_path, "wb") as f:
                    f.write(response.content)
                print(f"Success: Downloaded from {url}")
                success = True
                break
            else:
                 print(f"Failed {url} with status {response.status_code}")
        except Exception as e:
            print(f"Error for {url}: {e}")
            
    if not success:
        print(f"CRITICAL: Could not download {font_info['name']} from any source.")
