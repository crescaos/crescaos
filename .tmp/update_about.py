import os
import re

ABOUT_FILE = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public\about.html"

with open(ABOUT_FILE, "r", encoding="utf-8") as f:
    html = f.read()

main_pattern = re.compile(r'<main[^>]*>.*?</main>', re.DOTALL)

new_main_html = """
<main class="pt-24 pb-0 relative overflow-hidden bg-surface">

    <!-- Hero Section -->
    <section class="relative min-h-[50vh] flex flex-col items-center justify-center px-6 md:px-8 mt-12 mb-20 z-10 border-b border-outline-variant/5">
        <div class="absolute inset-0 z-0 bg-primary/5 blur-[120px] rounded-full w-[600px] h-[600px] left-1/2 -translate-x-1/2 pointer-events-none"></div>
        <div class="relative z-10 max-w-4xl text-center">
            
            <span class="inline-block font-label text-primary tracking-[0.2em] mb-6 uppercase text-sm font-bold animate-fade-in border border-primary/20 bg-primary/5 px-6 py-2 rounded-full">About Cresca OS</span>
            
            <h1 class="font-headline text-5xl sm:text-6xl md:text-7xl font-bold text-white leading-tight tracking-tight mb-8 animate-slide-up">
                Systems Designed <br><span class="text-brand-green italic leading-tight">For Scale.</span>
            </h1>
            
        </div>
    </section>

    <!-- Our Approach -->
    <section class="py-24 px-6 md:px-8 bg-surface-container-lowest relative z-10">
        <div class="max-w-7xl mx-auto flex flex-col lg:flex-row gap-20 items-center">
            
            <div class="lg:w-1/2">
                <span class="text-xs font-label tracking-[0.2em] text-brand-green uppercase font-bold mb-4 block">Our Approach</span>
                <h2 class="font-headline text-4xl md:text-5xl font-bold mb-8 text-white leading-tight">Practical Systems Thinking</h2>
                <p class="text-on-surface-variant text-xl leading-relaxed mb-8 font-light">
                    Our approach is simple and focused:
                </p>
                <ul class="space-y-4 mb-10">
                    <li class="flex items-start gap-4"><span class="material-symbols-outlined text-brand-green">rule</span><span class="text-on-surface text-lg">Build systems that reflect how real businesses operate</span></li>
                    <li class="flex items-start gap-4"><span class="material-symbols-outlined text-brand-green">rule</span><span class="text-on-surface text-lg">Focus on outcomes, not features</span></li>
                    <li class="flex items-start gap-4"><span class="material-symbols-outlined text-brand-green">rule</span><span class="text-on-surface text-lg">Reduce manual work wherever possible</span></li>
                    <li class="flex items-start gap-4"><span class="material-symbols-outlined text-brand-green">rule</span><span class="text-on-surface text-lg">Create consistent, repeatable processes</span></li>
                    <li class="flex items-start gap-4"><span class="material-symbols-outlined text-brand-green">rule</span><span class="text-on-surface text-lg">Make growth easier, not more complicated</span></li>
                </ul>
            </div>
            
            <div class="lg:w-1/2">
                <div class="bg-surface-container p-12 rounded-3xl border border-outline-variant/10 shadow-2xl relative overflow-hidden group hover:border-primary/30 transition-all duration-500">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-primary/10 blur-[50px] rounded-full point-events-none"></div>
                    <span class="material-symbols-outlined text-primary text-5xl mb-8">psychology</span>
                    <h3 class="font-headline text-2xl text-white mb-6 leading-relaxed">Every decision we make comes down to one question:</h3>
                    <p class="text-3xl font-headline text-white italic font-bold mb-8">"Does this help the business run better?"</p>
                    <div class="bg-error/10 border border-error/20 px-6 py-4 rounded-xl inline-block">
                        <p class="text-error font-label font-bold tracking-widest uppercase text-sm">If it doesn't, we don't build it.</p>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- Our Advantage & Portrait -->
    <section class="py-32 px-6 md:px-8 relative z-10 border-y border-outline-variant/5">
        <div class="max-w-7xl mx-auto flex flex-col lg:flex-row gap-16 items-center">
            
            <!-- Portrait Area -->
            <div class="lg:w-5/12 relative">
                <div class="relative rounded-3xl overflow-hidden aspect-[4/5] border border-outline-variant/10 shadow-2xl group">
                    <img src="assets/founder.png" alt="Cresca OS Execution" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-90 mix-blend-luminosity hover:mix-blend-normal">
                    <div class="absolute inset-0 bg-gradient-to-t from-surface-dim via-transparent to-transparent pointer-events-none"></div>
                </div>
                <!-- Signature Badge -->
                <div class="absolute -bottom-6 -right-6 bg-surface-container border border-primary/20 backdrop-blur-md px-8 py-6 rounded-2xl shadow-2xl">
                    <h4 class="font-headline text-white text-xl font-bold">Execution First.</h4>
                    <p class="font-label text-primary text-xs uppercase tracking-[0.2em] mt-1">Cresca OS Leadership</p>
                </div>
            </div>

            <!-- Content -->
            <div class="lg:w-7/12 lg:pl-12">
                <span class="text-xs font-label tracking-[0.2em] text-primary uppercase font-bold mb-4 block">Our Advantage</span>
                <h2 class="font-headline text-4xl md:text-5xl font-bold mb-8 text-white leading-tight">Built with a Bilingual, Global Execution Model</h2>
                <p class="text-on-surface-variant text-xl leading-relaxed mb-8 font-light">
                    Cresca OS combines strong systems with a unique operational structure.<br><br>
                    Our team spans the United States and El Salvador, allowing us to deliver:
                </p>
                <div class="space-y-6">
                    <div class="bg-surface-container-low p-6 rounded-2xl border border-outline-variant/10 flex items-start gap-4">
                        <span class="material-symbols-outlined text-primary mt-1">translate</span>
                        <div><strong class="text-white block mb-1">Bilingual Execution</strong><p class="text-on-surface-variant text-sm">Operate seamlessly across English and Spanish markets.</p></div>
                    </div>
                    <div class="bg-surface-container-low p-6 rounded-2xl border border-outline-variant/10 flex items-start gap-4">
                        <span class="material-symbols-outlined text-primary mt-1">schedule</span>
                        <div><strong class="text-white block mb-1">Real-time Support</strong><p class="text-on-surface-variant text-sm">Synchronized operations aligned strictly with US business hours.</p></div>
                    </div>
                    <div class="bg-surface-container-low p-6 rounded-2xl border border-outline-variant/10 flex items-start gap-4">
                        <span class="material-symbols-outlined text-primary mt-1">gavel</span>
                        <div><strong class="text-white block mb-1">Modern Compliance</strong><p class="text-on-surface-variant text-sm">Systems built with modern data protection and compliance standards in mind.</p></div>
                    </div>
                </div>
                <div class="mt-8 pt-6 border-t border-outline-variant/10">
                    <p class="text-lg text-primary font-medium italic">"This structure allows us to deliver consistent, high-quality results while staying responsive and efficient."</p>
                </div>
            </div>

        </div>
    </section>

    <!-- Who We Work With -->
    <section class="py-32 px-6 md:px-8 bg-surface-container-lowest relative z-10">
        <div class="max-w-7xl mx-auto">
            
            <div class="text-center mb-16 max-w-3xl mx-auto">
                <span class="text-xs font-label tracking-[0.2em] text-brand-green uppercase font-bold mb-4 block">Who We Work With</span>
                <h2 class="font-headline text-4xl md:text-5xl font-bold mb-6 text-white">Designed for Service Businesses That Depend on Lead Flow</h2>
                <p class="text-on-surface-variant text-xl leading-relaxed font-light">
                    Cresca OS is built for businesses where speed, follow-up, and organization directly impact revenue. We work with:
                </p>
            </div>

            <!-- Grid -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-surface-container p-8 rounded-2xl border border-outline-variant/10 flex items-center gap-4 hover:border-primary/30 transition-colors">
                    <span class="material-symbols-outlined text-brand-green text-3xl">solar_power</span>
                    <h3 class="font-headline text-lg font-bold text-white">Solar & Renewable Energy</h3>
                </div>
                <div class="bg-surface-container p-8 rounded-2xl border border-outline-variant/10 flex items-center gap-4 hover:border-primary/30 transition-colors">
                    <span class="material-symbols-outlined text-brand-green text-3xl">construction</span>
                    <h3 class="font-headline text-lg font-bold text-white">Contractors & Home Services</h3>
                </div>
                <div class="bg-surface-container p-8 rounded-2xl border border-outline-variant/10 flex items-center gap-4 hover:border-primary/30 transition-colors">
                    <span class="material-symbols-outlined text-brand-green text-3xl">cleaning_services</span>
                    <h3 class="font-headline text-lg font-bold text-white">Cleaning & Restoration</h3>
                </div>
                <div class="bg-surface-container p-8 rounded-2xl border border-outline-variant/10 flex items-center gap-4 hover:border-primary/30 transition-colors">
                    <span class="material-symbols-outlined text-brand-green text-3xl">real_estate_agent</span>
                    <h3 class="font-headline text-lg font-bold text-white">Real Estate & Property Mgmt</h3>
                </div>
                <div class="bg-surface-container md:col-span-2 p-8 rounded-2xl border border-outline-variant/10 flex items-center justify-center gap-4 hover:border-primary/30 transition-colors">
                    <span class="material-symbols-outlined text-brand-green text-3xl">local_hospital</span>
                    <h3 class="font-headline text-lg font-bold text-white">Clinics, Dental & Professional Services</h3>
                </div>
            </div>
            
            <div class="mt-12 text-center bg-surface-dim p-8 rounded-2xl max-w-4xl mx-auto border border-brand-green/20">
                <p class="text-xl text-white font-medium">If your business depends on capturing and converting opportunities — without adding more complexity — <span class="text-brand-green font-bold">Cresca OS is built for you.</span></p>
            </div>

        </div>
    </section>

    <!-- Closing Section -->
    <section class="max-w-5xl mx-auto px-6 md:px-8 py-32 text-center relative z-10 border-t border-outline-variant/5">
        <div class="signature-texture p-12 md:p-24 rounded-[2.5rem] overflow-hidden relative shadow-2xl">
            <div class="absolute inset-0 bg-[url('assets/hero_viz.png')] bg-cover bg-center opacity-10 mix-blend-overlay"></div>
            <div class="relative z-10">
                <h2 class="font-headline text-4xl md:text-5xl font-bold text-on-primary mb-8 leading-tight">You Don’t Need More Tools. You Need a System That Works.</h2>
                <p class="text-on-primary/90 text-xl md:text-2xl mb-12 max-w-3xl mx-auto leading-relaxed font-light">
                    Most businesses lose revenue every month through slow responses, missed follow-ups, forgotten appointments, and disorganized processes — often without realizing how much it’s costing them.<br><br>
                    <strong class="text-white font-medium">Cresca OS fixes that at the system level.</strong>
                </p>
                
                <div class="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-4xl mx-auto mb-16">
                    <div class="bg-surface/20 backdrop-blur-md rounded-xl p-4 border border-white/10 text-white font-bold text-sm">More leads captured</div>
                    <div class="bg-surface/20 backdrop-blur-md rounded-xl p-4 border border-white/10 text-white font-bold text-sm">Faster conversions</div>
                    <div class="bg-surface/20 backdrop-blur-md rounded-xl p-4 border border-white/10 text-white font-bold text-sm">Consistent operations</div>
                    <div class="bg-surface/20 backdrop-blur-md rounded-xl p-4 border border-white/10 text-white font-bold text-sm">More time back</div>
                </div>
                
                <a href="book-audit.html" class="bg-surface text-white px-10 py-5 rounded-xl font-label font-bold tracking-widest uppercase transition-all shadow-xl hover:bg-surface-variant hover:scale-105 inline-block w-full sm:w-auto mb-6">Book Your Free Business Systems Audit</a>
                <p class="text-white font-label tracking-widest uppercase text-xs opacity-80">See where your current setup is losing opportunities — and how to fix it.</p>
            </div>
        </div>
    </section>

</main>
"""

updated_html = re.sub(main_pattern, new_main_html, html)

with open(ABOUT_FILE, "w", encoding="utf-8") as f:
    f.write(updated_html)

print("About page rewritten.")
