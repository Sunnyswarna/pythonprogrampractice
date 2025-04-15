import os
from pathlib import Path

# Get path to Desktop
desktop = Path.home() / "Desktop"

# 1. Count number of files on Desktop
desktop_files = [f for f in desktop.iterdir() if f.is_file()]
print(f"Number of files on Desktop: {len(desktop_files)}")

# 2. Define path to 'swarna sunil' folder (adjust if it's not on Desktop)
swarna_sunil_folder = desktop / "swarna_sunil"

# Check if folder exists
if swarna_sunil_folder.exists() and swarna_sunil_folder.is_dir():
    swarna_files = [f for f in swarna_sunil_folder.iterdir() if f.is_file()]
    print(f"Number of files in 'swarna sunil' folder: {len(swarna_files)}")
else:
    print("The 'swarna sunil' folder was not found on your Desktop.")
