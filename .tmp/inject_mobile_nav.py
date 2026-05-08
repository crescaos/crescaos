import os
import glob
import re

PUBLIC_DIR = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"
html_files = glob.glob(os.path.join(PUBLIC_DIR, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already injected
    if 'id="mobile-menu-btn"' in content:
        continue

    # Find the end of the top nav
    nav_end_idx = content.find('</nav>')
    if nav_end_idx == -1:
        continue

    # We need to insert the hamburger button inside the "flex justify-between items-center" div
    # To do this safely, we reverse search for the last </div> before </nav>
    last_div_idx = content.rfind('</div>\n</div>\n</nav>')
    if last_div_idx == -1:
        # Fallback search
        last_div_idx = content.rfind('</div>\n</div>\n</nav>')

    # Let's do a reliable regex replace. We want to place the button next to the Book Audit button.
    # The block ends with:
    #                 Book Audit
    #             </a>
    # </div>
    # </div>
    # </nav>

    # Instead of brittle replacements, let's insert before </nav>
    
    mobile_nav_html = """
    <!-- Mobile Menu Button (Absolute positioned to top right for safety) -->
    <button id="mobile-menu-btn" class="md:hidden absolute top-5 right-6 text-on-surface focus:outline-none z-[60]">
        <span class="material-symbols-outlined text-3xl">menu</span>
    </button>

    <!-- Mobile Menu Overlay -->
    <div id="mobile-menu" class="fixed inset-0 bg-surface-dim/95 backdrop-blur-2xl z-[55] hidden flex-col pt-24 px-8 transform transition-transform duration-300 translate-x-full">
        <div class="flex flex-col space-y-8 font-headline text-3xl">
            <a href="solutions.html" class="text-on-surface hover:text-primary transition-colors">Solutions</a>
            <a href="industries.html" class="text-on-surface hover:text-primary transition-colors">Industries</a>
            <a href="pricing.html" class="text-on-surface hover:text-primary transition-colors">Pricing</a>
            <a href="about.html" class="text-on-surface hover:text-primary transition-colors">About</a>
            <a href="el-salvador.html" class="text-on-surface hover:text-primary transition-colors">El Salvador</a>
        </div>
        <div class="mt-12">
            <a class="bg-primary text-on-primary px-6 py-3 rounded-lg font-label font-bold uppercase tracking-widest text-sm inline-block w-full text-center" href="book-audit.html">Book Your Free Audit</a>
        </div>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const btn = document.getElementById('mobile-menu-btn');
            const menu = document.getElementById('mobile-menu');
            if(btn && menu) {
                btn.addEventListener('click', () => {
                    const isHidden = menu.classList.contains('translate-x-full');
                    if (isHidden) {
                        menu.classList.remove('hidden');
                        // tiny delay to allow display:block to apply before animating transform
                        setTimeout(() => {
                            menu.classList.remove('translate-x-full');
                            menu.classList.add('translate-x-0');
                        }, 10);
                        btn.innerHTML = '<span class="material-symbols-outlined text-3xl text-error">close</span>';
                    } else {
                        menu.classList.remove('translate-x-0');
                        menu.classList.add('translate-x-full');
                        setTimeout(() => menu.classList.add('hidden'), 300);
                        btn.innerHTML = '<span class="material-symbols-outlined text-3xl">menu</span>';
                    }
                });
            }
        });
    </script>
"""
    
    # We will inject `mobile_nav_html` right before `</nav>`
    content = content.replace("</nav>", mobile_nav_html + "\n</nav>", 1)
    
    # Let's also adjust the "Book Audit" button wrapper padding natively on mobile to not overlap the absolute button
    # Actually, top-5 right-6 is safe because the Book Audit button is gap-6 away.
    # To be perfectly safe, let's just make the Book Audit button disappear on mobile or add `mr-12` on mobile.
    content = content.replace('gap-6"', 'gap-6 mr-10 md:mr-0"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injected Mobile Navigation gracefully into all files.")
