import os
import glob
from bs4 import BeautifulSoup
import re

public_dir = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"
html_files = glob.glob(os.path.join(public_dir, "*.html"))

for filepath in html_files:
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    
    # 1. Update Title if missing or default for specific pages
    if filename == "index.html":
        title_text = "Cresca OS | Business Automation System for Service Businesses"
        if soup.title:
            soup.title.string = title_text
        else:
            new_title = soup.new_tag("title")
            new_title.string = title_text
            if soup.head:
                soup.head.insert(0, new_title)
    elif filename == "industries.html":
        title_text = "Industries We Serve | Cresca OS"
        if soup.title:
            soup.title.string = title_text
        else:
            new_title = soup.new_tag("title")
            new_title.string = title_text
            if soup.head:
                soup.head.insert(0, new_title)

    # 2. Add Favicon, Meta Description, OG, Canonical
    head = soup.head
    if head:
        # Avoid duplicates
        def add_meta(attributes):
            if not soup.find('meta', attrs=attributes):
                meta = soup.new_tag('meta')
                for k, v in attributes.items():
                    meta[k] = v
                head.append(meta)

        add_meta({'name': 'description', 'content': 'Cresca OS replaces disconnected tools with one unified business automation system. We capture leads, respond instantly, and automate follow-ups.'})
        add_meta({'property': 'og:title', 'content': 'Cresca OS | Business Automation System for Service Businesses'})
        add_meta({'property': 'og:description', 'content': 'Cresca OS replaces disconnected tools with one unified business automation system. We capture leads, respond instantly, and automate follow-ups.'})
        add_meta({'property': 'og:image', 'content': 'https://crescaos.com/og-image.jpg'})
        add_meta({'property': 'og:url', 'content': f'https://crescaos.com/{"" if filename == "index.html" else filename.replace(".html", "")}'})
        
        if not soup.find('link', attrs={'rel': 'icon'}):
            favicon = soup.new_tag('link', rel='icon', href='/favicon.ico')
            head.append(favicon)
            
        if not soup.find('link', attrs={'rel': 'canonical'}):
            canonical = soup.new_tag('link', rel='canonical', href=f'https://crescaos.com/{"" if filename == "index.html" else filename.replace(".html", "")}')
            head.append(canonical)

    # 3. Update Footer
    footer = soup.find('footer')
    if footer:
        # Copyright 2024 -> 2026
        for p in footer.find_all('p', string=re.compile(r'© 2024')):
            p.string = p.string.replace('© 2024', '© 2026')
        
        # Adding Contact info: hello@crescaos.com if not present
        if not footer.find(string=re.compile(r'hello@crescaos\.com')):
            copyright_div = footer.find_all('div')[-1] # usually the last div with border-t
            if copyright_div and 'border-t' in copyright_div.get('class', []):
                contact_p = soup.new_tag('p', attrs={'class': 'font-sans text-xs text-[#8f9095] mt-2'})
                contact_a = soup.new_tag('a', href='mailto:hello@crescaos.com', attrs={'class': 'hover:text-[#4edea3] transition-colors'})
                contact_a.string = 'hello@crescaos.com'
                contact_p.append(contact_a)
                copyright_div.append(contact_p)

        # Update Footer links
        # Systems Audit -> book-audit.html
        for a in footer.find_all('a', string=re.compile(r'Systems Audit', re.I)):
            a['href'] = 'book-audit.html'
        
        # U.S. Strategy -> about.html
        for a in footer.find_all('a', string=re.compile(r'U\.S\. Strategy', re.I)):
            a['href'] = 'about.html'

    # 4. Form method update (book-audit.html check)
    if filename == "book-audit.html":
        form = soup.find('form')
        if form:
            form['method'] = 'POST'
            form['data-netlify'] = 'true'
            # Check if there is a 'name' attribute or 'action' for Netlify forms
            if not form.get('name'):
                form['name'] = 'audit-booking'

    # Finally, write back formatting correctly
    html = str(soup)
    # The formatter might have messed up some self-closing tags, but lxml/html.parser is usually fine.
    
    # We will do a generic replacement for © 2024 just in case beautifulsoup missed it inside whitespace
    html = html.replace('© 2024', '© 2026')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updates completed successfully.")
