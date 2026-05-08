import os
import glob

public_dir = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"
html_files = glob.glob(os.path.join(public_dir, "*.html"))

for filepath in html_files:
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update email
    content = content.replace("hello@crescaos.com", "info@crescaos.com")

    # Update image on about.html
    if filename == "about.html":
        content = content.replace('src="assets/founder.png"', 'src="assets/founder2.png"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updates applied.")
