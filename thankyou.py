from pathlib import Path
import webbrowser

# Folder containing thankyou.py
folder = Path(__file__).resolve().parent

# Your existing photo in the repository
photo_name = "photo.jpg"
photo_path = folder / photo_name

if photo_path.exists():
    print("Photo found:", photo_path)
else:
    print("Photo not found. Check the filename and folder.")

output = folder / "index.html"