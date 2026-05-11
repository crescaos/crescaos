import os
import re

def restore_page(file_path):
    print(f"Processing {file_path}...")
    
    # Construct paths
    full_current_path = os.path.join(os.getcwd(), file_path)
    content_filename = file_path.replace('/', '_') + "_content.txt"
    content_path = os.path.join(os.getcwd(), content_filename)
    
    if not os.path.exists(full_current_path):
        print(f"File {full_current_path} not found.")
        return
        
    if not os.path.exists(content_path):
        print(f"Content file {content_path} not found.")
        return

    # Read current content (shell)
    with open(full_current_path, 'r', encoding='utf-8') as f:
        current_content = f.read()

    # Read pre-extracted body content
    with open(content_path, 'r', encoding='utf-8') as f:
        body_content = f.read()

    # Extract shell components from current content
    # We want everything up to <main> and everything after </main>
    main_start_match = re.search(r'<main[^>]*>', current_content, re.IGNORECASE)
    main_end_match = re.search(r'</main>', current_content, re.IGNORECASE)
    
    if not main_start_match or not main_end_match:
        print(f"Could not find <main> tags in current {file_path}")
        # Fallback: try to find the container that holds the content if <main> is missing
        # But for this site, they should have <main>
        return
        
    header = current_content[:main_start_match.start()]
    main_tag = main_start_match.group(0)
    footer = current_content[main_end_match.end():]
    
    # Reconstruct
    # Add some indentation for the body content to look nice
    indented_body = "\n".join(["        " + line if line.strip() else line for line in body_content.split('\n')])
    
    new_content = header + main_tag + "\n" + indented_body + "\n    </main>" + footer
    
    # Save back
    with open(full_current_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully restored {file_path}")

pages = [
    'public/pricing.html',
    'public/es/pricing.html',
    'public/integrations.html',
    'public/es/integrations.html',
    'public/el-salvador.html',
    'public/es/el-salvador.html',
    'public/how-we-work.html',
    'public/es/how-we-work.html'
]

if __name__ == "__main__":
    for page in pages:
        restore_page(page)

