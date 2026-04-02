import os
import glob

public_dir = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"
html_files = glob.glob(os.path.join(public_dir, "*.html")) + glob.glob(os.path.join(public_dir, "es", "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacing the pinkish red `#ff8c82` with the theme primary blue `#0A84FF` or tailwind `text-primary`
    # The occurrences are `text-[#ff8c82]`
    content = content.replace("text-[#ff8c82]", "text-primary")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Color theme corrected across all files.")
