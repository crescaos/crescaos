import os
import shutil
import glob

downloads_dir = r"C:\Users\12132\Downloads"
public_dir = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"
assets_dir = os.path.join(public_dir, "assets")

# Get whatsapp image
whatsapp_img = os.path.join(downloads_dir, "WhatsApp Image 2026-03-25 at 5.50.15 PM.jpeg")
if not os.path.exists(whatsapp_img):
    # Try the other one
    whatsapp_img = os.path.join(downloads_dir, "WhatsApp Image 2026-03-25 at 5.50.15 PM (1).jpeg")

if os.path.exists(whatsapp_img):
    dest_path = os.path.join(assets_dir, "whatsapp_founder.jpeg")
    shutil.copy2(whatsapp_img, dest_path)
    
    # Update about.html
    about_files = [
        os.path.join(public_dir, "about.html"),
        os.path.join(public_dir, "es", "about.html")
    ]
    
    for fpath in about_files:
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            content = content.replace('src="assets/founder2.png"', 'src="assets/whatsapp_founder.jpeg"')
            content = content.replace('src="../assets/founder2.png"', 'src="../assets/whatsapp_founder.jpeg"')
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
    print("Image replaced successfully!")
else:
    print("Could not find WhatsApp image.")
