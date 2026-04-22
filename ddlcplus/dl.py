import os
import requests
from urllib.parse import unquote

# The live source server
BASE_REMOTE_URL = "https://selenite.cc/resources/semag/ddlcplus/"

# Corrected paths based on official internal naming
file_paths = [
    "game/images/gallery_images/gallery_default_wallpaper.png",
    "game/images/gallery_thumbnails/gallery_default_wallpaper_th.png",
    # Standard Gallery Thumbnails (Common naming pattern)
    "game/images/gallery_thumbnails/gallery_sayori_th.png",
    "game/images/gallery_thumbnails/gallery_natsuki_th.png",
    "game/images/gallery_thumbnails/gallery_yuri_th.png",
    "game/images/gallery_thumbnails/gallery_monika_th.png",
    # Backgrounds and CGs
    "game/images/bg/residential.png",
    "game/images/bg/warning.png",
    "game/images/bg/warning2.png",
    "game/images/cg/s_kill_early.png",
    # Launcher Assets (Note: %20 is used for spaces in the URL)
    "game/images/LauncherAssets/JukeboxImages/DDLC%20Plus%20OST%20cover.png"
]

def download_files():
    print(f"Targeting: {BASE_REMOTE_URL}")
    print("Mode: OVERWRITE (Fresh Download)")
    print("="*50)
    
    for path in file_paths:
        url = f"{BASE_REMOTE_URL}{path}"
        
        # Clean local path for your OS (e.g. converting %20 to a real space)
        clean_path = unquote(path)
        local_path = os.path.join(os.getcwd(), clean_path)
        
        # Ensure folders exist
        directory = os.path.dirname(local_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        print(f"[!] Fetching: {clean_path}...", end=" ", flush=True)
        
        try:
            # We use stream=True for better handling of larger image files
            response = requests.get(url, stream=True, timeout=15)
            
            if response.status_code == 200:
                with open(local_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print("✅ SUCCESS")
            elif response.status_code == 404:
                print("❌ NOT FOUND (404)")
            else:
                print(f"❌ ERROR ({response.status_code})")
        
        except Exception as e:
            print(f"❌ EXCEPTION: {e}")

if __name__ == "__main__":
    download_files()
    print("\n" + "="*50 + "\nProcess complete.")