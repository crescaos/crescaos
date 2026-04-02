import os
import glob
import re

PUBLIC_DIR = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"
html_files = glob.glob(os.path.join(PUBLIC_DIR, "*.html"))

# We want to replace the broken "Solutions" column in the index.html footer
# with the robust, working one from solutions.html.

broken_solutions_html = """<h6 class="text-[#4edea3] font-label text-xs uppercase tracking-widest mb-6 font-bold">Solutions</h6>
<ul class="space-y-4">
<li><a class="text-[#8f9095] hover:text-[#4edea3] transition-colors font-sans text-sm" href="solutions.html#crm">Custom CRM</a></li>
<li><a class="text-[#8f9095] hover:text-[#4edea3] transition-colors font-sans text-sm" href="solutions.html#ai">AI Automation</a></li>
<li><a class="text-[#8f9095] hover:text-[#4edea3] transition-colors font-sans text-sm" href="solutions.html#workflows">Workflow Design</a></li>
</ul>"""

robust_solutions_html = """<h6 class="text-[#4edea3] font-label text-xs uppercase tracking-widest mb-6 font-bold">Solutions</h6>
<ul class="space-y-4">
<li><a class="text-[#8f9095] hover:text-[#4edea3] transition-colors font-sans text-sm" href="solutions.html">Systems Audit</a></li>
<li><a class="text-[#8f9095] hover:text-[#4edea3] transition-colors font-sans text-sm" href="pricing.html">Pricing</a></li>
<li><a class="text-[#8f9095] hover:text-[#4edea3] transition-colors font-sans text-sm" href="industries.html">Industries</a></li>
</ul>"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if broken_solutions_html in content:
        content = content.replace(broken_solutions_html, robust_solutions_html)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Standardized all footers. Removed broken anchor links.")
