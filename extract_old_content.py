import subprocess
import os
import re

def get_git_content(commit, path):
    try:
        # Run git show command
        result = subprocess.run(['git', 'show', f'{commit}:{path}'], 
                                capture_output=True, text=True, encoding='utf-8', errors='ignore')
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"Error getting {path} from {commit}: {result.stderr}")
            return None
    except Exception as e:
        print(f"Exception for {path}: {str(e)}")
        return None

def extract_main_content(html):
    if not html:
        return None
    # Look for <main>...</main>
    match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    
    # Fallback: look for content between navigation and footer
    # This is a bit risky but we can try to find common markers
    return None

pages = [
    "public/pricing.html",
    "public/es/pricing.html",
    "public/integrations.html",
    "public/es/integrations.html",
    "public/el-salvador.html",
    "public/es/el-salvador.html",
    "public/how-we-work.html",
    "public/es/how-we-work.html"
]

commit = "26ed9a8"

for page in pages:
    content = get_git_content(commit, page)
    if content:
        main_content = extract_main_content(content)
        if main_content:
            # Save the extracted content for inspection
            filename = page.replace("/", "_") + "_content.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(main_content)
            print(f"Extracted content for {page}")
        else:
            print(f"COULD NOT EXTRACT MAIN CONTENT FOR {page}")
            # Let's save the whole file to see why
            with open(page.replace("/", "_") + "_full_old.html", "w", encoding="utf-8") as f:
                f.write(content)
    else:
        print(f"Failed to get {page} from git")
