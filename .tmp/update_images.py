import os
import glob
import shutil
import re

BRAIN_DIR = r"C:\Users\12132\.gemini\antigravity\brain\a396d052-5f1b-48fb-9f8d-b7ec0388fa1e"
ASSETS_DIR = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public\assets"
PUBLIC_DIR = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"

# We know the prefixes, we need to find the latest file matching each prefix
prefixes = [
    "industries_solar",
    "industries_architecture",
    "elsalvador_workspace",
    "elsalvador_arch",
    "cyber_command",
    "about_office"
]

images = {}
for prefix in prefixes:
    files = glob.glob(os.path.join(BRAIN_DIR, f"{prefix}_*.png"))
    if files:
        latest_file = max(files, key=os.path.getmtime)
        images[prefix] = latest_file

# Copy to assets and standardise names
for prefix, filepath in images.items():
    dest = os.path.join(ASSETS_DIR, f"{prefix}.png")
    shutil.copy2(filepath, dest)

# Now replace in HTML
replacements = {
    "industries.html": [
        (r'src="https://lh3.googleusercontent[^"]*"([^>]*data-alt="Solar panels[^"]*")', r'src="assets/industries_solar.png"\1'),
        (r'data-alt="Solar panels[^"]*"[^>]*src="https://lh3.googleusercontent[^"]*"', r'data-alt="Solar panels on a residential roof" src="assets/industries_solar.png"'),
        (r'src="https://lh3.googleusercontent[^"]*"([^>]*data-alt="Modern architectural building[^"]*")', r'src="assets/industries_architecture.png"\1'),
        (r'data-alt="Modern architectural building[^"]*"[^>]*src="https://lh3.googleusercontent[^"]*"', r'data-alt="Modern architectural building with glass reflections" src="assets/industries_architecture.png"'),
    ],
    "el-salvador.html": [
        (r'src="https://lh3.googleusercontent[^"]*"([^>]*data-alt="Modern high-rise office building[^"]*")', r'src="assets/elsalvador_arch.png"\1'),
        (r'data-alt="Modern high-rise office building[^"]*"[^>]*src="https://lh3.googleusercontent[^"]*"', r'data-alt="Modern high-rise office building with glass facade at dusk" src="assets/elsalvador_arch.png"'),
        (r'src="https://lh3.googleusercontent[^"]*"([^>]*data-alt="Modern technology workspace[^"]*")', r'src="assets/elsalvador_workspace.png"\1'),
        (r'data-alt="Modern technology workspace[^"]*"[^>]*src="https://lh3.googleusercontent[^"]*"', r'data-alt="Modern technology workspace with minimalist aesthetics" src="assets/elsalvador_workspace.png"'),
    ],
    "book-audit.html": [
        (r'src="https://lh3.googleusercontent[^"]*"([^>]*data-alt="Sophisticated dark server room[^"]*")', r'src="assets/cyber_command.png"\1'),
        (r'data-alt="Sophisticated dark server room[^"]*"[^>]*src="https://lh3.googleusercontent[^"]*"', r'data-alt="Sophisticated dark server room with green status lights" src="assets/cyber_command.png"'),
    ],
    "about.html": [
        (r'src="https://lh3.googleusercontent[^"]*"([^>]*data-alt="High-end corporate office interior[^"]*")', r'src="assets/about_office.png"\1'),
        (r'data-alt="High-end corporate office interior[^"]*"[^>]*src="https://lh3.googleusercontent[^"]*"', r'data-alt="High-end corporate office interior with deep shadows and natural lighting" src="assets/about_office.png"'),
    ]
}

for filename, rules in replacements.items():
    filepath = os.path.join(PUBLIC_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for rule in rules:
            content = re.sub(rule[0], rule[1], content)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Images copied and HTML files updated.")
