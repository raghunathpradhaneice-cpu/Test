
from pathlib import Path
import webbrowser
import shutil
import tkinter as tk
from tkinter import filedialog

# Select a personal photo from your computer
root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True)

photo = filedialog.askopenfilename(
    title="Choose a special photo ❤️",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.webp"),
        ("All files", "*.*")
    ]
)

root.destroy()

# Folder where this Python script is saved
folder = Path(__file__).resolve().parent
output = folder / "index.html"

# Copy the selected photo into the webpage folder
photo_name = "photo.jpg"

if photo:
    source = Path(photo)
    photo_name = "photo" + source.suffix.lower()
    shutil.copy2(source, folder / photo_name)
    print("Photo added:", photo_name)
else:
    print("No photo selected. The webpage will use a placeholder.")
    photo_name = ""

# Personalized webpage
image_html = (
    f'<img class="photo" src="{photo_name}" alt="A special person">'
    if photo_name
    else '<div class="placeholder">❤️ A special memory ❤️</div>'
)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Thank You for Being in My Life ❤️</title>

<style>
* {{ box-sizing: border-box; }}

body {{
    margin: 0;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 25px 12px;
    font-family: Georgia, serif;
    text-align: center;
    color: #793b54;
    background: linear-gradient(135deg, #ffdce8, #fff0e6, #f2dfff);
}}

.card {{
    max-width: 500px;
    width: 100%;
    padding: 28px;
    border-radius: 25px;
    background: rgba(255,255,255,0.88);
    box-shadow: 0 12px 40px #b45b7730;
    animation: appear 1.2s ease;
}}

h1 {{ color: #d64e79; line-height: 1.4; }}

.photo {{
    width: 100%;
    max-height: 420px;
    object-fit: cover;
    border-radius: 18px;
    border: 3px solid white;
}}

.placeholder {{
    padding: 70px 10px;
    border-radius: 18px;
    background: #ffe0ec;
    font-size: 24px;
}}

p {{ font-size: 18px; line-height: 1.8; }}

.heart {{
    font-size: 32px;
    animation: beat 1.2s infinite;
}}

.signature {{
    color: #d64e79;
    font-size: 21px;
    font-style: italic;
}}

@keyframes beat {{
    50% {{ transform: scale(1.15); }}
}}

@keyframes appear {{
    from {{ opacity: 0; transform: translateY(20px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}
</style>
</head>

<body>
<div class="card">
    <div class="heart">❤️ 🌷 ❤️</div>

    <h1>Thank You for Being in My Life</h1>

    {image_html}

    <p>Some people enter our lives and make everything
    a little more beautiful. You are one of those people. ❤️</p>

    <p>Thank you for your kindness, your smile, your presence,
    and all those little moments that mean more than words
    can ever explain.</p>

    <p>Life feels more special because you are a part of it.
    I may not say it every day, but I am truly grateful
    to have you in my life.</p>

    <p>No matter where life takes us, I hope you always
    remember how special you are to me. 💗</p>

    <div class="heart">💖</div>
    <p class="signature">Forever grateful for you 🌹</p>
</div>
</body>
</html>
"""

output.write_text(html, encoding="utf-8")

print("\\nYour thank-you webpage is ready!")
print("HTML file:", output)
print("Remember to upload index.html and the photo to GitHub.")

webbrowser.open(output.as_uri())
