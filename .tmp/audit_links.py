import os
import glob
import re

PUBLIC_DIR = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"

# Find all HTML files
html_files = glob.glob(os.path.join(PUBLIC_DIR, "*.html"))

# Regex to find href attributes
href_regex = re.compile(r'href="([^"]+)"')

all_links = set()
broken_links_candidate = []

print("Extracting ALL links...")
for filepath in html_files:
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links = href_regex.findall(content)
    for link in links:
        all_links.add(link)
        # Check if the link is suspicious (not http, not standard html, not #, etc)
        if not link.startswith('http') and not link.startswith('mailto:') and not link.startswith('#') and not link.startswith('tel:'):
            if link not in [os.path.basename(f) for f in html_files]:
                if not link.startswith('https://fonts'):
                    broken_links_candidate.append((filename, link))

print("\n--- ALL UNIQUE LINKS ---")
for link in sorted(list(all_links)):
    print(link)

print("\n--- SUSPICIOUS LINKS (Target file doesn't exist locally) ---")
for filename, link in broken_links_candidate:
    print(f"[{filename}] -> {link}")
