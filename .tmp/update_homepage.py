import os
import re

INDEX_FILE = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public\index.html"

with open(INDEX_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# Pattern to isolate the exact <main> tag and its contents
main_pattern = re.compile(r'<main[^>]*>.*?</main>', re.DOTALL)

new_main_html = """
<main class="pt-24 pb-0">
    
    <!-- Background Blur Effect -->
    <div class="absolute inset-0 pointer-events-none z-0 flex justify-center overflow-hidden">
        <div class="w-[800px] h-[800px] bg-primary/5 rounded-full blur-[120px] -translate-y-1/4"></div>
    </div>

    <!-- Hero Section -->
    <section class="relative min-h-[90vh] flex flex-col items-center justify-center px-6 md:px-8 mt-12 mb-20 z-10">
        <div class="relative z-10 max-w-6xl text-center">
            
            <h1 class="font-headline text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-bold text-on-background leading-[1.1] tracking-tight mb-8 animate-slide-up">
                One System. <span class="text-brand-green italic leading-tight">Total Control<br></span> Over Your Business.
            </h1>
            
            <p class="font-body text-xl md:text-2xl text-on-surface-variant max-w-4xl mx-auto mb-12 leading-relaxed font-light px-4">
                Cresca OS replaces your disconnected tools with one unified system that captures leads, responds instantly, books appointments, and follows up automatically — so your business runs faster and more efficiently.<br><br>
                <span class="text-white font-medium block mt-2">We design, build, and manage everything for you.</span>
            </p>

            <div class="flex flex-col sm:flex-row gap-6 justify-center items-center mb-16 w-full px-4">
                <a class="signature-texture text-on-primary px-10 py-5 rounded-xl font-label font-bold tracking-widest text-sm uppercase shadow-[0_0_30px_rgba(0,230,138,0.3)] transition-all duration-300 hover:scale-105 block w-full sm:w-auto text-center" href="book-audit.html">
                    Book Free Audit
                </a>
                <a class="bg-surface-container-high border border-outline-variant/30 text-white px-10 py-5 rounded-xl font-label tracking-widest text-sm uppercase transition-all duration-200 hover:bg-surface-bright block w-full sm:w-auto text-center" href="solutions.html">
                    See How It Works
                </a>
            </div>

            <!-- Guarantee & Supporting Line -->
            <div class="flex flex-col items-center gap-8">
                <!-- Supporting Line -->
                <div class="flex flex-wrap items-center justify-center gap-x-4 gap-y-2 bg-surface-container bg-opacity-60 backdrop-blur-md border border-outline-variant/10 rounded-full px-8 py-3 font-label text-[10px] md:text-xs uppercase tracking-[0.2em] text-outline text-center">
                    <span>Live in under 14 days</span>
                    <span class="hidden sm:inline w-1 h-1 rounded-full bg-primary/50"></span>
                    <span>Unlimited users</span>
                    <span class="hidden sm:inline w-1 h-1 rounded-full bg-primary/50"></span>
                    <span>Built for service businesses</span>
                </div>

                <!-- Guarantee Banner -->
                <div class="inline-flex flex-col sm:flex-row items-center gap-6 bg-brand-green/5 border border-brand-green/20 rounded-2xl px-8 py-6 max-w-2xl text-center sm:text-left shadow-lg transform transition-transform hover:-translate-y-1 hover:bg-brand-green/10">
                    <span class="material-symbols-outlined text-brand-green text-5xl">health_and_safety</span>
                    <div>
                        <h4 class="font-bold text-white text-lg font-headline mb-1">90-Day ROI Guarantee</h4>
                        <p class="text-on-surface-variant text-sm font-body">Recover your setup investment in qualified opportunities or we'll refund it in full.</p>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- Problem Section -->
    <section class="py-32 px-6 md:px-8 bg-surface-container-lowest relative z-10 border-y border-outline-variant/5">
        <div class="max-w-4xl mx-auto text-center">
            <span class="text-xs font-label tracking-[0.2em] text-[#ff8c82] uppercase font-bold mb-6 block">The Real Problem</span>
            <h2 class="font-headline text-4xl md:text-5xl lg:text-7xl font-bold mb-10 text-white leading-tight">Your Business Isn't Broken.<br><span class="text-outline-variant italic">Your Systems Are.</span></h2>
            
            <p class="text-on-surface-variant text-xl md:text-2xl leading-relaxed mb-8 max-w-3xl mx-auto font-light">
                Most service businesses are using multiple tools that don’t work together. Leads slip through the cracks, responses take too long, and follow-up is inconsistent.
            </p>
            <p class="text-on-surface-variant text-xl md:text-2xl leading-relaxed mb-12 max-w-3xl mx-auto font-light">
                Your team ends up doing manual work that should already be automated. The result is <strong class="text-[#ff8c82] font-semibold">lost opportunities, slower growth, and constant operational friction.</strong>
            </p>
        </div>
    </section>

    <!-- Solution Section (Bento Grid) -->
    <section class="py-32 px-6 md:px-8 relative z-10">
        <div class="max-w-7xl mx-auto">
            
            <div class="max-w-3xl mb-16">
                <span class="text-xs font-label tracking-[0.2em] text-primary uppercase font-bold mb-6 block">Introducing Cresca OS</span>
                <h2 class="font-headline text-4xl md:text-6xl font-bold mb-8 text-white">A Complete System Built and Managed for You</h2>
                <p class="text-on-surface-variant text-xl leading-relaxed font-light">
                    Cresca OS brings everything your business needs into one system — so nothing gets missed and everything runs consistently.<br><br>
                    Instead of juggling tools and processes, you get a single operating system that:
                </p>
            </div>

            <!-- Bento Features -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
                <div class="bg-surface-container rounded-2xl p-8 border border-outline-variant/10 hover:border-primary/30 transition-colors">
                    <span class="material-symbols-outlined text-brand-green text-3xl mb-4">phonelink_ring</span>
                    <p class="text-white font-medium text-lg">Captures leads from every channel</p>
                </div>
                <div class="bg-surface-container rounded-2xl p-8 border border-outline-variant/10 hover:border-primary/30 transition-colors">
                    <span class="material-symbols-outlined text-brand-green text-3xl mb-4">bolt</span>
                    <p class="text-white font-medium text-lg">Responds instantly to new inquiries</p>
                </div>
                <div class="bg-surface-container rounded-2xl p-8 border border-outline-variant/10 hover:border-primary/30 transition-colors">
                    <span class="material-symbols-outlined text-brand-green text-3xl mb-4">event_available</span>
                    <p class="text-white font-medium text-lg">Books appointments automatically</p>
                </div>
                <div class="bg-surface-container rounded-2xl p-8 border border-outline-variant/10 hover:border-primary/30 transition-colors">
                    <span class="material-symbols-outlined text-brand-green text-3xl mb-4">mark_email_read</span>
                    <p class="text-white font-medium text-lg">Follows up with every single lead</p>
                </div>
                <div class="bg-surface-container rounded-2xl p-8 border border-outline-variant/10 hover:border-primary/30 transition-colors">
                    <span class="material-symbols-outlined text-brand-green text-3xl mb-4">stacks</span>
                    <p class="text-white font-medium text-lg">Keeps your pipeline organized</p>
                </div>
                <div class="bg-surface-container rounded-2xl p-8 border border-outline-variant/10 hover:border-primary/30 transition-colors">
                    <span class="material-symbols-outlined text-brand-green text-3xl mb-4">published_with_changes</span>
                    <p class="text-white font-medium text-lg">Helps re-engage past customers</p>
                </div>
            </div>

            <div class="bg-primary/5 border border-primary/20 rounded-2xl p-8 text-center max-w-4xl mx-auto shadow-xl">
                <p class="text-xl text-primary font-body italic font-semibold">"Everything works together — so your business runs smoother without more effort."</p>
            </div>
            
            <!-- Key Differentiators -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 mt-24">
                <div class="border-t-2 border-primary pt-6">
                    <h4 class="font-headline text-2xl font-bold text-white mb-3">Done-for-You Setup</h4>
                    <p class="text-on-surface-variant text-sm">We build and launch your system for you. No technical work required.</p>
                </div>
                <div class="border-t-2 border-brand-green pt-6">
                    <h4 class="font-headline text-2xl font-bold text-white mb-3">Built for Real Business</h4>
                    <p class="text-on-surface-variant text-sm">Designed around how service businesses actually run day to day.</p>
                </div>
                <div class="border-t-2 border-primary pt-6">
                    <h4 class="font-headline text-2xl font-bold text-white mb-3">All-in-One System</h4>
                    <p class="text-on-surface-variant text-sm">No more switching between tools or losing critical information.</p>
                </div>
                <div class="border-t-2 border-brand-green pt-6">
                    <h4 class="font-headline text-2xl font-bold text-white mb-3">Ongoing Optimization</h4>
                    <p class="text-on-surface-variant text-sm">We continue improving your system as your business grows.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- How It Works & Why Cresca OS -->
    <section class="py-32 px-6 md:px-8 bg-[#0b1326] relative z-10 border-y border-outline-variant/5">
        <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-24">
            
            <!-- How It Works -->
            <div>
                <span class="text-xs font-label tracking-[0.2em] text-brand-green uppercase font-bold mb-6 block">Simple 3-Step Process</span>
                <h2 class="font-headline text-4xl md:text-5xl font-bold mb-12 text-white">From Disconnected Tools to a Fully Working System</h2>
                
                <div class="space-y-12">
                    <div class="flex gap-6 relative">
                        <!-- Connecting Line -->
                        <div class="absolute left-6 top-12 bottom-[-48px] w-0.5 bg-outline-variant/20 -z-10 hidden sm:block"></div>
                        
                        <div class="w-12 h-12 shrink-0 rounded-full bg-surface-container border border-primary/30 flex items-center justify-center font-headline font-bold text-xl text-primary z-10">1</div>
                        <div>
                            <h3 class="font-headline text-2xl font-bold text-white mb-3">Business Systems Audit</h3>
                            <p class="text-on-surface-variant text-lg">We look at how your business currently captures leads, responds, and follows up — and identify where opportunities are being lost.</p>
                        </div>
                    </div>
                    
                    <div class="flex gap-6 relative">
                        <div class="absolute left-6 top-12 bottom-[-48px] w-0.5 bg-outline-variant/20 -z-10 hidden sm:block"></div>
                        <div class="w-12 h-12 shrink-0 rounded-full bg-surface-container border border-brand-green/30 flex items-center justify-center font-headline font-bold text-xl text-brand-green z-10">2</div>
                        <div>
                            <h3 class="font-headline text-2xl font-bold text-white mb-3">Build & Deploy</h3>
                            <p class="text-on-surface-variant text-lg">We design and implement your complete system, tailored to your business and workflow.</p>
                        </div>
                    </div>

                    <div class="flex gap-6">
                        <div class="w-12 h-12 shrink-0 rounded-full signature-texture flex items-center justify-center font-headline font-bold text-xl text-on-primary z-10">3</div>
                        <div>
                            <h3 class="font-headline text-2xl font-bold text-white mb-3">Optimize & Scale</h3>
                            <p class="text-on-surface-variant text-lg">We monitor performance and improve your system over time so it keeps delivering results.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Why Cresca OS -->
            <div class="bg-surface-container-low p-10 md:p-12 rounded-[2rem] border border-outline-variant/10 shadow-2xl">
                <span class="text-xs font-label tracking-[0.2em] text-primary uppercase font-bold mb-6 block">Why Cresca OS</span>
                <h2 class="font-headline text-4xl md:text-4xl font-bold mb-10 text-white leading-tight">The System Behind Your Growth</h2>
                
                <ul class="space-y-6">
                    <li class="flex items-start gap-4">
                        <span class="material-symbols-outlined text-primary mt-0.5 shrink-0">task_alt</span>
                        <span class="text-on-surface text-lg"><strong>No per-user fees</strong> — your team can grow without increasing costs</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <span class="material-symbols-outlined text-primary mt-0.5 shrink-0">task_alt</span>
                        <span class="text-on-surface text-lg"><strong>Fully managed</strong> — no need to set up or maintain anything yourself</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <span class="material-symbols-outlined text-primary mt-0.5 shrink-0">task_alt</span>
                        <span class="text-on-surface text-lg"><strong>Built for service businesses</strong> — not generic software</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <span class="material-symbols-outlined text-primary mt-0.5 shrink-0">task_alt</span>
                        <span class="text-on-surface text-lg"><strong>Faster response</strong> and better follow-up built in</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <span class="material-symbols-outlined text-primary mt-0.5 shrink-0">task_alt</span>
                        <span class="text-on-surface text-lg"><strong>Designed to help you</strong> capture more opportunities and close more jobs</span>
                    </li>
                </ul>
            </div>

        </div>
    </section>

    <!-- Social Proof -->
    <section class="py-32 px-6 md:px-8 relative z-10">
        <div class="max-w-7xl mx-auto">
            <div class="text-center mb-16">
                <span class="text-xs font-label tracking-[0.2em] text-outline-variant uppercase font-bold mb-4 block">Real Businesses. Real Results.</span>
                <h2 class="font-headline text-4xl md:text-5xl font-bold text-white">Don't Just Take Our Word For It</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bg-surface-container rounded-2xl p-10 border border-outline-variant/10 relative">
                    <span class="material-symbols-outlined text-6xl text-outline-variant/20 absolute top-6 left-6 -z-10">format_quote</span>
                    <p class="text-xl text-on-surface font-light leading-relaxed mb-6 italic z-10 relative">"Within the first month we improved our response time and started booking more appointments without adding more work."</p>
                    <div class="flex items-center gap-4">
                        <div class="w-12 h-12 bg-surface-bright rounded-full flex items-center justify-center text-outline font-bold">SB</div>
                        <span class="font-label font-bold text-white uppercase tracking-widest text-xs">— Service Business Owner</span>
                    </div>
                </div>
                
                <div class="bg-surface-container rounded-2xl p-10 border border-outline-variant/10 relative">
                    <span class="material-symbols-outlined text-6xl text-outline-variant/20 absolute top-6 left-6 -z-10">format_quote</span>
                    <p class="text-xl text-on-surface font-light leading-relaxed mb-6 italic z-10 relative">"We finally have one system that keeps everything organized. No more missed leads or forgotten follow-ups."</p>
                    <div class="flex items-center gap-4">
                        <div class="w-12 h-12 bg-surface-bright rounded-full flex items-center justify-center text-outline font-bold">OM</div>
                        <span class="font-label font-bold text-white uppercase tracking-widest text-xs">— Operations Manager</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Final CTA Section -->
    <section class="max-w-5xl mx-auto px-6 md:px-8 mb-32 text-center relative z-10">
        <div class="signature-texture p-12 md:p-24 rounded-[2.5rem] overflow-hidden relative shadow-2xl">
            <div class="absolute inset-0 bg-[url('assets/hero_viz.png')] bg-cover bg-center opacity-10 mix-blend-overlay"></div>
            <div class="relative z-10">
                <h2 class="font-headline text-4xl md:text-6xl font-bold text-on-primary mb-8 leading-tight">How Many Leads Are You Losing Every Week?</h2>
                <p class="text-on-primary/90 text-xl mb-12 max-w-3xl mx-auto leading-relaxed font-medium">
                    Book your free Business Systems Audit and we'll show you where your current setup is costing you opportunities — and how to fix it.
                </p>
                <p class="text-white font-label font-bold tracking-widest uppercase text-sm mb-12 opacity-80">No pressure. Just clarity.</p>
                
                <div class="flex flex-col sm:flex-row justify-center items-center gap-6">
                    <a href="book-audit.html" class="bg-surface text-white px-10 py-5 rounded-xl font-label font-bold tracking-widest uppercase transition-all hover:bg-surface-variant hover:scale-105 w-full sm:w-auto shadow-xl">Book Your Free Audit Now</a>
                    <a href="solutions.html" class="bg-transparent border-2 border-white text-white px-10 py-5 rounded-xl font-label tracking-widest uppercase transition-colors hover:bg-white/10 w-full sm:w-auto">Watch Quick Overview</a>
                </div>
                
                <div class="mt-8 flex justify-center items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-error animate-pulse"></span>
                    <p class="text-xs text-white uppercase tracking-widest font-bold">Limited audit spots available each week.</p>
                </div>
            </div>
        </div>
    </section>

</main>
"""

updated_html = re.sub(main_pattern, new_main_html, html)

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(updated_html)

print("Homepage has been successfully rewritten with the revised copy.")
