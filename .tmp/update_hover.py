import os

public_dir = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"
about_files = [
    os.path.join(public_dir, "about.html"),
    os.path.join(public_dir, "es", "about.html")
]

for fpath in about_files:
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # The existing classes might contain mix-blend-luminosity
        content = content.replace(
            "opacity-90 mix-blend-luminosity hover:mix-blend-normal",
            "grayscale hover:grayscale-0 opacity-90 transition-all duration-700"
        )
        
        # In case the old classes weren't exactly matched, look for just the image tag
        if "mix-blend-luminosity" in content:
            content = content.replace("mix-blend-luminosity hover:mix-blend-normal", "grayscale hover:grayscale-0")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

print("Grayscale effect updated.")
