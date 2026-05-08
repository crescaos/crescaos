import os
import glob
import shutil
import re

public_dir = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"
es_dir = os.path.join(public_dir, "es")

if not os.path.exists(es_dir):
    os.makedirs(es_dir)

html_files = glob.glob(os.path.join(public_dir, "*.html"))

# Regex patterns for removing Google Translate
gt_div = re.compile(r'<div id="google_translate_element"></div>\s*')
gt_init_script = re.compile(r'<script type="text/javascript">\s*function googleTranslateElementInit\(\).*?</script>\s*', re.DOTALL)
gt_src_script = re.compile(r'<script[^>]*src=["\']https://translate\.google\.com/translate_a/element\.js\?cb=googleTranslateElementInit["\'][^>]*></script>\s*')
gt_toggle_script = re.compile(r'<script>\s*function toggleLanguage\(\).*?</script>\s*', re.DOTALL)

# Also removing: #lang-toggle
lang_toggle = re.compile(r'<span[^>]*id="lang-toggle"[^>]*onclick="toggleLanguage\(\)"[^>]*>.*?</span>\s*', re.DOTALL)

for filepath in html_files:
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine paths and links
    en_link = f'/{filename}'
    es_link = f'/es/{filename}'

    # Remove Google Translate artifacts
    content = gt_div.sub('', content)
    content = gt_init_script.sub('', content)
    content = gt_src_script.sub('', content)
    content = gt_toggle_script.sub('', content)

    # Replace old lang toggle
    # In English root files, link to ES:
    es_toggle_html = f'<a href="{es_link}" class="text-[#8f9095] font-label text-sm hover:text-[#dae2fd] transition-colors">ES</a>'
    content = lang_toggle.sub(es_toggle_html, content)

    # We also need to fix links inside the ES folder to point to other /es/ pages, 
    # but initially we'll just create the architecture. Actually, updating the navbar links is better.
    
    # Save English version back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    # -------------------------------------------------------------
    # Create Spanish versions
    # -------------------------------------------------------------
    es_content = content
    # In ES version, link to EN:
    en_toggle_html = f'<a href="{en_link}" class="text-[#00E68A] font-label text-sm hover:text-[#dae2fd] transition-colors font-bold">EN</a>'
    es_content = es_content.replace(es_toggle_html, en_toggle_html)
    
    # Change language declarative
    es_content = es_content.replace('<html class="dark scroll-smooth" lang="en">', '<html class="dark scroll-smooth" lang="es">')
    
    # Update local links in ES version (so navigation stays in /es/)
    # For a href="something.html" -> a href="/es/something.html"
    for other_file in html_files:
        other_name = os.path.basename(other_file)
        es_content = es_content.replace(f'href="{other_name}"', f'href="/es/{other_name}"')
        es_content = es_content.replace(f'href="/{other_name}"', f'href="/es/{other_name}"')

    # Also fix asset references in ES folder (assets/ -> ../assets/)
    es_content = es_content.replace('href="assets/', 'href="../assets/')
    es_content = es_content.replace('src="assets/', 'src="../assets/')
    es_content = es_content.replace("url('assets/", "url('../assets/")

    es_filepath = os.path.join(es_dir, filename)
    with open(es_filepath, 'w', encoding='utf-8') as f:
        f.write(es_content)

print("Translation architecture deployed successfully!")
