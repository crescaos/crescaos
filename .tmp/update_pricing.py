import os
import re

PRICING_FILE = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public\pricing.html"

with open(PRICING_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# Pattern to isolate the exact <main> tag and its contents
main_pattern = re.compile(r'<main[^>]*>.*?</main>', re.DOTALL)

new_main_html = """
<main class="pt-32 pb-24 relative overflow-hidden">
    <!-- Background Accents -->
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-7xl h-full pointer-events-none z-0">
        <div class="absolute top-[10%] left-[20%] w-[500px] h-[500px] bg-primary/5 rounded-full blur-[120px]"></div>
        <div class="absolute top-[40%] right-[10%] w-[600px] h-[600px] bg-brand-green/5 rounded-full blur-[150px]"></div>
    </div>

    <!-- Hero Section -->
    <header class="max-w-4xl mx-auto px-8 mb-20 text-center relative z-10">
        <span class="inline-block font-label text-brand-green tracking-[0.2em] mb-6 uppercase text-sm font-bold animate-fade-in">Pricing & Plans</span>
        <h1 class="font-headline text-5xl md:text-6xl lg:text-7xl font-bold text-on-surface leading-tight tracking-tight mb-8 animate-slide-up">
            One System to <span class="text-primary italic">Capture</span>, <span class="text-brand-green italic">Convert</span>, and Scale Your Business
        </h1>
        <p class="font-body text-xl text-on-surface-variant leading-relaxed mb-12 animate-fade-in delay-200 shadow-sm">
            Cresca OS is a fully managed business operating system that captures leads, responds instantly, automates follow-up, and organizes your operations — so you can grow without adding complexity or headcount.
        </p>
    </header>

    <!-- 90-Day Guarantee Banner -->
    <section class="max-w-5xl mx-auto px-8 mb-24 relative z-10">
        <div class="bg-surface-container-low border border-outline-variant/20 rounded-2xl p-8 md:p-12 flex flex-col md:flex-row items-center gap-8 shadow-2xl relative overflow-hidden group hover:border-brand-green/30 transition-colors duration-500">
            <div class="absolute inset-0 bg-gradient-to-br from-brand-green/5 to-transparent pointer-events-none"></div>
            <div class="flex-shrink-0 bg-brand-green/10 p-6 rounded-full border border-brand-green/20">
                <span class="material-symbols-outlined text-brand-green text-5xl group-hover:scale-110 transition-transform duration-500">health_and_safety</span>
            </div>
            <div>
                <h3 class="font-headline text-2xl md:text-3xl font-bold text-white mb-3">90-Day ROI Guarantee</h3>
                <p class="text-on-surface-variant text-lg">If Cresca OS doesn't generate enough qualified opportunities or recovered revenue to cover your setup investment within 90 days, we'll refund it in full.</p>
            </div>
        </div>
    </section>

    <!-- Pricing Tiers Grid -->
    <section class="max-w-7xl mx-auto px-8 mb-32 relative z-10">
        <div class="text-center mb-16">
            <h2 class="font-headline text-4xl font-bold text-white mb-4">Choose Your Tier</h2>
            <p class="text-on-surface-variant text-lg">Transparent pricing for scaling service businesses.</p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 items-stretch">
            
            <!-- Launch Tier -->
            <div class="bg-surface-container rounded-2xl p-8 border border-outline-variant/10 flex flex-col relative transition-all duration-300 hover:border-primary/30 hover:-translate-y-2 hover:shadow-2xl">
                <div class="mb-8">
                    <h3 class="font-headline text-3xl font-bold text-white mb-2">Launch</h3>
                    <p class="text-on-surface-variant text-sm mb-6 h-12">Perfect for local service businesses ready to stop losing leads and respond faster.</p>
                    <div class="text-4xl font-bold text-white mb-1"><span class="text-xl text-outline-variant font-normal">$</span>397<span class="text-lg font-normal text-on-surface-variant">/mo</span></div>
                    <div class="text-sm font-label text-primary font-bold tracking-widest uppercase mb-8">Setup Fee: $2,500 <span class="text-outline-variant text-xs">(One-Time)</span></div>
                    <a href="book-audit.html" class="block w-full text-center bg-surface border border-outline-variant/30 hover:bg-surface-variant text-white font-label font-bold py-4 rounded-xl transition-colors">Start Launch Tier</a>
                </div>
                <div class="flex-grow">
                    <h4 class="font-label text-xs uppercase tracking-widest text-outline-variant mb-6 font-bold">What's Included</h4>
                    <ul class="space-y-4 mb-8">
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0 mt-0.5">check_circle</span><span class="text-sm text-on-surface-variant">Done-for-you CRM and pipeline system tailored to your business</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0 mt-0.5">check_circle</span><span class="text-sm text-on-surface-variant">Instant lead response automation so every inquiry is handled immediately</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0 mt-0.5">check_circle</span><span class="text-sm text-on-surface-variant">Lead capture from website, calls, Google Business Profile, and ads</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0 mt-0.5">check_circle</span><span class="text-sm text-on-surface-variant">Basic appointment booking with automated confirmations and reminders</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0 mt-0.5">check_circle</span><span class="text-sm text-on-surface-variant">Real-time dashboard with visibility into leads, activity, and performance</span></li>
                    </ul>
                </div>
                <div class="pt-6 border-t border-outline-variant/10 mt-auto">
                    <p class="text-xs text-on-surface-variant italic"><span class="text-brand-green font-bold not-italic">Ideal for:</span> Businesses generating 5–20 leads per month that want a reliable system without added complexity.</p>
                </div>
            </div>

            <!-- Growth Tier (Most Popular) -->
            <div class="bg-surface-container-low rounded-2xl p-8 border border-primary/50 shadow-2xl shadow-primary/10 flex flex-col relative transform lg:-translate-y-4 transition-all duration-300 hover:-translate-y-6 overflow-hidden">
                <div class="absolute top-0 inset-x-0 h-1 bg-gradient-to-r from-primary to-brand-green"></div>
                <div class="absolute top-0 right-0 bg-primary text-on-primary text-[10px] font-bold uppercase tracking-widest py-1 px-3 rounded-bl-lg">Most Popular</div>
                
                <div class="mb-8 pt-2">
                    <h3 class="font-headline text-3xl font-bold text-white mb-2">Growth</h3>
                    <p class="text-on-surface-variant text-sm mb-6 h-12">For service businesses ready to automate follow-up, improve conversions, and operate more efficiently.</p>
                    <div class="text-4xl font-bold text-white mb-1"><span class="text-xl text-outline-variant font-normal">$</span>797<span class="text-lg font-normal text-on-surface-variant">/mo</span></div>
                    <div class="text-sm font-label text-primary font-bold tracking-widest uppercase mb-8">Setup Fee: $4,500 <span class="text-outline-variant text-xs">(One-Time)</span></div>
                    <a href="book-audit.html" class="block w-full text-center bg-primary hover:bg-primary/90 text-on-primary font-label font-bold py-4 rounded-xl transition-all shadow-[0_0_20px_rgba(10,132,255,0.3)] hover:shadow-[0_0_30px_rgba(10,132,255,0.5)]">Start Growth Tier</a>
                </div>
                <div class="flex-grow">
                    <h4 class="font-label text-xs uppercase tracking-widest text-outline-variant mb-6 font-bold">What's Included</h4>
                    <p class="text-sm font-bold text-white mb-4">Everything in Launch, plus:</p>
                    <ul class="space-y-4 mb-6">
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-xl shrink-0 mt-0.5">add_circle</span><span class="text-sm text-on-surface-variant">Advanced multi-step follow-up sequences to keep leads engaged</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-xl shrink-0 mt-0.5">add_circle</span><span class="text-sm text-on-surface-variant">Intelligent lead qualification workflows tailored to high-value targets</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-xl shrink-0 mt-0.5">add_circle</span><span class="text-sm text-on-surface-variant">Multi-channel reactivation campaigns for past customers</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-xl shrink-0 mt-0.5">add_circle</span><span class="text-sm text-on-surface-variant">Full bilingual automation (EN/ES) supported by Cresca's operations</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-xl shrink-0 mt-0.5">add_circle</span><span class="text-sm text-on-surface-variant">Ongoing system optimization and monthly strategy support</span></li>
                    </ul>
                    <div class="bg-surface-dim p-4 rounded-lg border border-outline-variant/10 mb-8">
                        <p class="text-[11px] text-outline text-center">Most businesses move to Growth after seeing how much time and revenue they recover with Cresca OS.</p>
                    </div>
                </div>
                <div class="pt-6 border-t border-outline-variant/10 mt-auto">
                    <p class="text-xs text-on-surface-variant italic"><span class="text-primary font-bold not-italic">Ideal for:</span> Businesses generating 20+ leads per month that want to improve conversion rates and run more consistent operations.</p>
                </div>
            </div>

            <!-- Scale Tier -->
            <div class="bg-surface-container rounded-2xl p-8 border border-outline-variant/10 flex flex-col relative transition-all duration-300 hover:border-brand-green/30 hover:-translate-y-2 hover:shadow-2xl">
                <div class="mb-8">
                    <h3 class="font-headline text-3xl font-bold text-white mb-2">Scale</h3>
                    <p class="text-on-surface-variant text-sm mb-6 h-12">For multi-location or high-volume businesses requiring scalability.</p>
                    <div class="text-4xl font-bold text-white mb-1"><span class="text-xl text-outline-variant font-normal">$</span>1,500+<span class="text-lg font-normal text-on-surface-variant">/mo</span></div>
                    <div class="text-sm font-label text-brand-green font-bold tracking-widest uppercase mb-8">Setup Fee: Custom <span class="text-outline-variant text-xs">(starts at $8.5k)</span></div>
                    <a href="book-audit.html" class="block w-full text-center bg-surface border border-outline-variant/30 hover:bg-surface-variant text-white font-label font-bold py-4 rounded-xl transition-colors">Request Scale Custom Setup</a>
                </div>
                <div class="flex-grow">
                    <h4 class="font-label text-xs uppercase tracking-widest text-outline-variant mb-6 font-bold">What's Included</h4>
                    <p class="text-sm font-bold text-white mb-4">Everything in Growth, plus:</p>
                    <ul class="space-y-4 mb-6">
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0 mt-0.5">architecture</span><span class="text-sm text-on-surface-variant">Fully customized CRM architecture and advanced workflow design</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0 mt-0.5">architecture</span><span class="text-sm text-on-surface-variant">Custom integrations and lead routing across teams or locations</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0 mt-0.5">architecture</span><span class="text-sm text-on-surface-variant">Advanced reporting and performance management dashboards</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0 mt-0.5">architecture</span><span class="text-sm text-on-surface-variant">Dedicated optimization specialist and priority support</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0 mt-0.5">architecture</span><span class="text-sm text-on-surface-variant">Systems designed to support highly complex growth environments</span></li>
                    </ul>
                    <div class="bg-surface-dim p-4 rounded-lg border border-outline-variant/10 mb-8 mt-4">
                        <p class="text-[11px] text-error text-center font-bold">Not every business is a fit for this level.</p>
                    </div>
                </div>
                <div class="pt-6 border-t border-outline-variant/10 mt-auto">
                    <p class="text-xs text-on-surface-variant italic"><span class="text-brand-green font-bold not-italic">Ideal for:</span> Companies with multiple locations, higher lead volume, or more complex workflows.</p>
                </div>
            </div>

        </div>
    </section>

    <!-- Everything Included & Why Us -->
    <section class="max-w-7xl mx-auto px-8 mb-32 relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
            
            <!-- Included -->
            <div class="bg-surface-container-low p-10 rounded-2xl border border-outline-variant/10">
                <span class="material-symbols-outlined text-primary text-4xl mb-6">layers</span>
                <h3 class="font-headline text-3xl font-bold text-white mb-6">Everything Included in Every Plan</h3>
                <p class="text-on-surface-variant mb-8 text-lg">Every Cresca OS plan includes the core infrastructure your business needs to operate efficiently and grow with consistency.</p>
                <ul class="space-y-4">
                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-xl shrink-0">done_all</span><span class="text-on-surface">Full done-for-you implementation (live in under 14 days)</span></li>
                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-xl shrink-0">done_all</span><span class="text-on-surface">Unlimited users — no per-user pricing</span></li>
                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-xl shrink-0">done_all</span><span class="text-on-surface">Transparent usage-based billing for messaging</span></li>
                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-xl shrink-0">done_all</span><span class="text-on-surface">Ongoing system monitoring and optimization</span></li>
                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-xl shrink-0">done_all</span><span class="text-on-surface">Bilingual execution capability across English and Spanish</span></li>
                </ul>
            </div>

            <!-- Why Us -->
            <div class="bg-surface-container-low p-10 rounded-2xl border border-outline-variant/10">
                <span class="material-symbols-outlined text-brand-green text-4xl mb-6">bolt</span>
                <h3 class="font-headline text-3xl font-bold text-white mb-6">Why Cresca OS Outperforms DIY</h3>
                <p class="text-on-surface-variant mb-8 text-lg">We don't just sell you software. We build the engine that drives your business forward, saving you months of trial and error.</p>
                <ul class="space-y-4">
                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0">verified</span><span class="text-on-surface">We handle the entire system for you — no technical setup required</span></li>
                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0">verified</span><span class="text-on-surface">Faster deployment and consistent results vs. building your own</span></li>
                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0">verified</span><span class="text-on-surface">Unified system instead of multiple disconnected tools</span></li>
                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0">verified</span><span class="text-on-surface">Built to support real business operations, not just marketing tasks</span></li>
                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0">verified</span><span class="text-on-surface">Bilingual capability that supports a wider customer base</span></li>
                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-brand-green text-xl shrink-0">verified</span><span class="text-on-surface">Ongoing optimization, not one-time setup</span></li>
                </ul>
            </div>
            
        </div>
    </section>

    <!-- Final CTA Section -->
    <section class="max-w-5xl mx-auto px-8 text-center relative z-10">
        <div class="bg-primary/5 border border-primary/20 p-12 md:p-20 rounded-[2rem] overflow-hidden relative">
            <div class="absolute inset-0 bg-[url('assets/hero_viz.png')] bg-cover bg-center opacity-5 mix-blend-overlay"></div>
            <div class="relative z-10">
                <h2 class="font-headline text-4xl md:text-5xl font-bold text-white mb-6">How Much Revenue Are You Losing Every Month?</h2>
                <p class="text-on-surface-variant text-xl mb-10 max-w-3xl mx-auto leading-relaxed">
                    Book your free Business Systems Audit and we'll show you exactly where your current setup is costing you opportunities — and how Cresca OS can help you capture more leads, respond faster, and grow more efficiently.
                </p>
                <p class="text-on-surface font-label font-bold tracking-widest uppercase text-sm mb-12">No pressure. No technical overwhelm. Just clarity.</p>
                
                <div class="flex flex-col sm:flex-row justify-center items-center gap-6">
                    <a href="book-audit.html" class="bg-primary hover:bg-primary/90 text-on-primary px-10 py-5 rounded-xl font-label font-bold tracking-widest uppercase transition-all shadow-[0_0_20px_rgba(10,132,255,0.3)] hover:scale-105 w-full sm:w-auto">Book Your Free Audit Now</a>
                    <a href="el-salvador.html" class="bg-surface-container border border-outline-variant/30 hover:bg-surface-container-high text-white px-10 py-5 rounded-xl font-label tracking-widest uppercase transition-colors w-full sm:w-auto">Request Custom Proposal</a>
                </div>
                <p class="mt-6 text-[10px] text-error uppercase tracking-widest font-bold">Limited audit availability each week. Reserve your spot today.</p>
            </div>
        </div>
    </section>

</main>
"""

updated_html = re.sub(main_pattern, new_main_html, html)

with open(PRICING_FILE, "w", encoding="utf-8") as f:
    f.write(updated_html)

print("pricing.html has been completely refactored with the new copy.")
