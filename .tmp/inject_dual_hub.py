import os

INDEX_FILE = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public\index.html"

with open(INDEX_FILE, "r", encoding="utf-8") as f:
    html = f.read()

injection_block = """
    <!-- Global Execution Matrix -->
    <section class="border-y border-outline-variant/10 flex flex-col md:flex-row min-h-[500px] w-full relative z-10 bg-surface">
        <!-- US Strategy -->
        <div class="flex-1 relative p-12 md:p-20 flex flex-col justify-center items-center text-center overflow-hidden group">
            <div class="absolute inset-0 bg-[url('assets/ny_la_skyline.png')] bg-cover bg-center transition-transform duration-1000 group-hover:scale-105 opacity-30 mix-blend-luminosity"></div>
            <div class="absolute inset-0 bg-gradient-to-t from-surface via-surface/80 to-surface/40 group-hover:bg-surface/50 transition-colors duration-500"></div>
            
            <span class="material-symbols-outlined text-primary text-[60px] mb-6 relative z-10 opacity-90 drop-shadow-[0_0_15px_rgba(10,132,255,0.5)]">public</span>
            <h3 class="font-headline text-3xl md:text-5xl font-bold text-white mb-6 relative z-10 tracking-tight">U.S. Strategy</h3>
            <p class="text-on-surface-variant text-lg md:text-xl max-w-md relative z-10 font-light leading-relaxed">Executive-level architecture, market analysis, and compliance-first engineering based in North America.</p>
            
            <div class="mt-12 flex items-center gap-3 relative z-10 bg-surface-container bg-opacity-80 backdrop-blur-md border border-outline-variant/20 rounded-full px-6 py-2">
                <span class="w-2.5 h-2.5 rounded-full bg-primary animate-pulse shadow-[0_0_10px_rgba(10,132,255,0.8)]"></span>
                <span class="font-label text-[10px] md:text-xs uppercase tracking-[0.2em] text-white">NEW YORK / LOS ANGELES</span>
            </div>
        </div>
        
        <!-- Execution Hub -->
        <div class="flex-1 relative p-12 md:p-20 flex flex-col justify-center items-center text-center overflow-hidden group border-t md:border-t-0 md:border-l border-outline-variant/10">
            <div class="absolute inset-0 bg-[url('assets/san_salvador_skyline.png')] bg-cover bg-center transition-transform duration-1000 group-hover:scale-105 opacity-30 mix-blend-luminosity"></div>
            <div class="absolute inset-0 bg-gradient-to-t from-surface via-surface/80 to-surface/40 group-hover:bg-surface/50 transition-colors duration-500"></div>
            
            <span class="material-symbols-outlined text-brand-green text-[60px] mb-6 relative z-10 opacity-90 drop-shadow-[0_0_15px_rgba(0,230,138,0.5)]">stacks</span>
            <h3 class="font-headline text-3xl md:text-5xl font-bold text-white mb-6 relative z-10 tracking-tight">Execution Hub</h3>
            <p class="text-on-surface-variant text-lg md:text-xl max-w-md relative z-10 font-light leading-relaxed">Rapid deployment and high-performance engineering hub located in the heart of El Salvador's tech corridor.</p>
            
            <div class="mt-12 flex items-center gap-3 relative z-10 bg-surface-container bg-opacity-80 backdrop-blur-md border border-outline-variant/20 rounded-full px-6 py-2">
                <span class="w-2.5 h-2.5 rounded-full bg-brand-green animate-pulse shadow-[0_0_10px_rgba(0,230,138,0.8)]"></span>
                <span class="font-label text-[10px] md:text-xs uppercase tracking-[0.2em] text-white">SAN SALVADOR</span>
            </div>
        </div>
    </section>
"""

# Inject before the Social Proof section
target_anchor = '<!-- Social Proof -->'
if target_anchor in html:
    html = html.replace(target_anchor, injection_block + "\n    " + target_anchor)

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print("Injected dual-hub execution matrix into index.html")
