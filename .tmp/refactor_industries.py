import os
import glob
import shutil
import re

BRAIN_DIR = r"C:\Users\12132\.gemini\antigravity\brain\a396d052-5f1b-48fb-9f8d-b7ec0388fa1e"
ASSETS_DIR = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public\assets"
PUBLIC_DIR = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"

# 1. Map available generated images to the missing industry needs
mappings = {
    "industry_roofing": "industry_roofing",
    "industry_hvac": "industry_hvac",
    "elsalvador_arch": "industry_realestate", # repurpose architecture for real estate
    "about_office": "industry_clinics", # repurpose luxury office for clinics
    "elsalvador_workspace": "industry_cleaning" # repurpose pristine workspace for cleaning
}

for src_prefix, target_name in mappings.items():
    files = glob.glob(os.path.join(BRAIN_DIR, f"{src_prefix}_*.png"))
    if files:
        latest_file = max(files, key=os.path.getmtime)
        dest = os.path.join(ASSETS_DIR, f"{target_name}.png")
        shutil.copy2(latest_file, dest)

# 2. Update index.html (Live Infrastructure -> System Intelligence + Mobile Optimizations)
index_path = os.path.join(PUBLIC_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# Replace metrics
index_html = index_html.replace("LIVE INFRASTRUCTURE", "SYSTEM INTELLIGENCE")
index_html = index_html.replace("14.2k", "1.2M+")
index_html = index_html.replace("Node Clusters", "Automations Fired")
index_html = index_html.replace("Sovereign", "&lt; 5s")
index_html = index_html.replace("Security Protocol", "Avg. Response Time")
index_html = index_html.replace("Efficiency Benchmark", "Process Automation")

# Mobile optimizations (padding, typography sizing)
index_html = index_html.replace('text-6xl md:text-7xl lg:text-8xl', 'text-5xl sm:text-6xl md:text-7xl lg:text-8xl')
index_html = index_html.replace('px-16 py-8', 'px-8 md:px-16 py-6 md:py-8')
index_html = index_html.replace('gap-10 items-center', 'gap-8 md:gap-10 items-center')
index_html = index_html.replace('grid-cols-4 gap-4', 'grid-cols-2 md:grid-cols-4 gap-4')
index_html = index_html.replace('col-span-2 bg-surface-container', 'col-span-2 bg-surface-container')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

# 3. Update industries.html (Rebuild Grid to 6 cards + Copy Sync)
industries_path = os.path.join(PUBLIC_DIR, "industries.html")
with open(industries_path, "r", encoding="utf-8") as f:
    ind_html = f.read()

grid_start_marker = r'<!-- Industries Bento Grid -->\s*<section class="max-w-7xl mx-auto px-8 mb-32">\s*<div class="grid grid-cols-1 md:grid-cols-12 gap-6 h-auto [^>]*">'
grid_end_marker = r'</div>\s*</section>\s*<!-- Founder Led Section \(Asymmetric Editorial\) -->'

new_grid_content = """<!-- Industries Bento Grid -->
<section class="max-w-7xl mx-auto px-8 mb-32">
<div class="grid grid-cols-1 md:grid-cols-12 gap-6">

    <!-- Solar -->
    <div class="md:col-span-6 bg-surface-container-low rounded-xl overflow-hidden group flex flex-col justify-end p-8 md:p-10 relative min-h-[400px]">
        <div class="absolute inset-0 bg-gradient-to-t from-surface-dim via-surface-dim/70 to-surface-dim/20 z-10 transition-opacity duration-500 group-hover:opacity-80"></div>
        <img class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-60" src="assets/industries_solar.png" alt="Solar panels" />
        <div class="relative z-20">
            <span class="font-label text-xs font-bold text-[#00E68A] tracking-widest uppercase mb-3 block">Solar</span>
            <h3 class="font-headline text-3xl font-bold text-white mb-3">Capture More Leads. Follow Up Faster.</h3>
            <p class="font-body text-on-surface-variant mb-0 max-w-md">Instant speed-to-lead automation across all sources, multi-touch follow-ups, and self-service appointment booking for site assessments.</p>
        </div>
    </div>

    <!-- Roofing & Contractors -->
    <div class="md:col-span-6 bg-surface-container-high rounded-xl overflow-hidden group flex flex-col justify-end p-8 md:p-10 relative min-h-[400px]">
        <div class="absolute inset-0 bg-gradient-to-t from-surface-dim via-surface-dim/70 to-surface-dim/20 z-10 transition-opacity duration-500 group-hover:opacity-80"></div>
        <img class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-60" src="assets/industry_roofing.png" alt="Roofing Construction" />
        <div class="relative z-20">
            <span class="font-label text-xs font-bold text-[#00E68A] tracking-widest uppercase mb-3 block">Roofing & Contractors</span>
            <h3 class="font-headline text-3xl font-bold text-white mb-3">More Estimates. More Jobs.</h3>
            <p class="font-body text-on-surface-variant mb-0 max-w-md">Missed call text-back so no lead goes unanswered, automated estimate follow-up sequences, and online booking for appointments.</p>
        </div>
    </div>

    <!-- HVAC & Home Services -->
    <div class="md:col-span-4 bg-surface-container rounded-xl overflow-hidden group flex flex-col justify-end p-8 relative min-h-[350px]">
        <div class="absolute inset-0 bg-gradient-to-t from-surface-dim via-surface-dim/80 to-surface-dim/40 z-10 transition-opacity duration-500 group-hover:opacity-90"></div>
        <img class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-50" src="assets/industry_hvac.png" alt="HVAC System" />
        <div class="relative z-20">
            <span class="font-label text-xs font-bold text-[#00E68A] tracking-widest uppercase mb-3 block">HVAC & Home Services</span>
            <h3 class="font-headline text-2xl font-bold text-white mb-3">Emergency Response Automation.</h3>
            <p class="font-body text-on-surface-variant text-sm mb-0">Lead routing by service type, post-service review requests, and seasonal campaign automation (pre-summer AC, pre-winter heat).</p>
        </div>
    </div>

    <!-- Real Estate -->
    <div class="md:col-span-4 bg-surface-container rounded-xl overflow-hidden group flex flex-col justify-end p-8 relative min-h-[350px]">
        <div class="absolute inset-0 bg-gradient-to-t from-surface-dim via-surface-dim/80 to-surface-dim/40 z-10 transition-opacity duration-500 group-hover:opacity-90"></div>
        <img class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-50" src="assets/industry_realestate.png" alt="Real Estate" />
        <div class="relative z-20">
            <span class="font-label text-xs font-bold text-[#00E68A] tracking-widest uppercase mb-3 block">Real Estate</span>
            <h3 class="font-headline text-2xl font-bold text-white mb-3">More Conversations. More Listings.</h3>
            <p class="font-body text-on-surface-variant text-sm mb-0">Long-term nurture sequences for buyers, automated referral campaigns for past clients, and a pipeline view by buyer/seller status.</p>
        </div>
    </div>

    <!-- Clinics & Professional -->
    <div class="md:col-span-4 bg-surface-container rounded-xl overflow-hidden group flex flex-col justify-end p-8 relative min-h-[350px]">
        <div class="absolute inset-0 bg-gradient-to-t from-surface-dim via-surface-dim/80 to-surface-dim/40 z-10 transition-opacity duration-500 group-hover:opacity-90"></div>
        <img class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-50" src="assets/industry_clinics.png" alt="Clinics" />
        <div class="relative z-20">
            <span class="font-label text-xs font-bold text-[#00E68A] tracking-widest uppercase mb-3 block">Clinics & Professional</span>
            <h3 class="font-headline text-2xl font-bold text-white mb-3">An Organized Front Office.</h3>
            <p class="font-body text-on-surface-variant text-sm mb-0">Automated new patient intake, appointment confirmations by text, and re-engagement sequences for lapsed patients.</p>
        </div>
    </div>

    <!-- Cleaning Services -->
    <div class="md:col-span-12 bg-surface-container-low rounded-xl overflow-hidden group flex flex-col justify-end p-8 md:p-12 relative mt-4">
        <div class="absolute inset-0 bg-gradient-to-r from-surface-dim via-surface-dim/80 to-transparent z-10 transition-opacity duration-500 group-hover:opacity-90"></div>
        <img class="absolute inset-0 w-full h-full object-cover object-right transition-transform duration-700 group-hover:scale-105 opacity-50" src="assets/industry_cleaning.png" alt="Cleaning Services" />
        <div class="relative z-20 max-w-2xl">
            <span class="font-label text-xs font-bold text-[#00E68A] tracking-widest uppercase mb-3 block">Cleaning Services</span>
            <h3 class="font-headline text-4xl font-bold text-white mb-4">Recurring Revenue, Automated.</h3>
            <p class="font-body text-on-surface-variant text-lg lg:max-w-xl">Instant response to inquiries, online scheduling integration, automated recurring service reminders, and win-back campaigns for customers who lapsed. Grow without the constant manual work.</p>
        </div>
    </div>

</div>
</section>
<!-- Founder Led Section (Asymmetric Editorial) -->"""

# Perform regex substitution for the industries grid
import re
ind_html = re.sub(grid_start_marker + r'.*?' + grid_end_marker, new_grid_content, ind_html, flags=re.DOTALL)

with open(industries_path, "w", encoding="utf-8") as f:
    f.write(ind_html)

print("Mapping complete. Grid refactored. Metrics enhanced.")
