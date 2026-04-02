import os
import re

FILE_PATH = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public\book-audit.html"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

main_pattern = re.compile(r'<main[^>]*>.*?</main>', re.DOTALL)

new_main_html = """
<main class="pt-24 pb-0 relative overflow-hidden bg-surface">

    <!-- Hero Section -->
    <section class="relative min-h-[45vh] flex flex-col items-center justify-center px-6 md:px-8 mt-12 mb-16 z-10 border-b border-outline-variant/5">
        <div class="absolute inset-0 z-0 bg-primary/5 blur-[120px] rounded-full w-[800px] h-[800px] left-1/2 -translate-x-1/2 pointer-events-none"></div>
        <div class="relative z-10 max-w-5xl text-center">
            
            <div class="inline-flex items-center space-x-2 mb-6 px-4 py-1.5 rounded-full bg-surface-container-high border border-outline-variant/15">
                <span class="flex h-2 w-2 rounded-full bg-error animate-pulse"></span>
                <span class="text-xs font-label uppercase tracking-widest text-primary">Limited Audit Availability</span>
            </div>
            
            <h1 class="font-headline text-5xl sm:text-6xl md:text-7xl font-bold text-white leading-tight tracking-tight mb-8 animate-slide-up">
                Discover Where Your Business Is <span class="text-error italic">Losing Leads</span>.
            </h1>
            
            <p class="font-body text-xl md:text-2xl text-on-surface-variant max-w-4xl mx-auto mb-10 leading-relaxed font-light px-4">
                In just 15–30 minutes, we’ll analyze how your business captures leads, responds, and follows up — and show you exactly where opportunities are being lost.<br><br>
                <span class="text-white font-medium">You’ll leave with a clear understanding of what’s working, what’s not, and what can be improved.</span>
            </p>
        </div>
    </section>

    <!-- Main Content & Booking Form -->
    <section class="py-20 px-6 md:px-12 max-w-7xl mx-auto relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-start">
            
            <!-- Value Proposition Column -->
            <aside class="lg:col-span-5 space-y-12">
                
                <div>
                    <h3 class="font-headline text-3xl font-bold text-white mb-6">Why This Audit Is Different</h3>
                    <ul class="space-y-4">
                        <li class="flex items-start gap-4"><span class="material-symbols-outlined text-primary">psychology</span><span class="text-on-surface text-lg">We don’t just look at your tools — we look at how your entire system operates.</span></li>
                        <li class="flex items-start gap-4"><span class="material-symbols-outlined text-primary">psychology</span><span class="text-on-surface text-lg">We identify exactly where leads are being missed or delayed.</span></li>
                        <li class="flex items-start gap-4"><span class="material-symbols-outlined text-primary">psychology</span><span class="text-on-surface text-lg">We highlight gaps in response time and follow-up.</span></li>
                        <li class="flex items-start gap-4"><span class="material-symbols-outlined text-primary">psychology</span><span class="text-on-surface text-lg">We show how a unified system can improve consistency.</span></li>
                        <li class="flex items-start gap-4"><span class="material-symbols-outlined text-primary">psychology</span><span class="text-on-surface text-lg">You get practical insights you can act on immediately.</span></li>
                    </ul>
                </div>

                <div class="bg-surface-container-low p-8 rounded-2xl border border-outline-variant/10 relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-2 h-full bg-brand-green"></div>
                    <h3 class="font-headline text-2xl font-bold text-brand-green mb-6">What You'll Get</h3>
                    <ul class="space-y-4">
                        <li class="flex gap-3"><span class="material-symbols-outlined text-brand-green text-xl mt-0.5">task_alt</span><span class="text-on-surface-variant font-medium">A breakdown of your current lead flow.</span></li>
                        <li class="flex gap-3"><span class="material-symbols-outlined text-brand-green text-xl mt-0.5">task_alt</span><span class="text-on-surface-variant font-medium">Insight into where opportunities are lost.</span></li>
                        <li class="flex gap-3"><span class="material-symbols-outlined text-brand-green text-xl mt-0.5">task_alt</span><span class="text-on-surface-variant font-medium">Estimated impact of missed follow-up.</span></li>
                        <li class="flex gap-3"><span class="material-symbols-outlined text-brand-green text-xl mt-0.5">task_alt</span><span class="text-on-surface-variant font-medium">Recommendations tailored to your business.</span></li>
                        <li class="flex gap-3"><span class="material-symbols-outlined text-brand-green text-xl mt-0.5">task_alt</span><span class="text-on-surface-variant font-medium">A roadmap for system improvement.</span></li>
                    </ul>
                </div>

                <div>
                    <h3 class="font-headline text-2xl font-bold text-white mb-6">Who This Is For</h3>
                    <p class="text-on-surface-variant text-lg mb-4">Service businesses that depend on lead flow and want to:</p>
                    <div class="flex flex-wrap gap-3">
                        <span class="bg-surface-container border border-outline-variant/20 px-4 py-2 rounded-full text-sm text-white">Respond faster</span>
                        <span class="bg-surface-container border border-outline-variant/20 px-4 py-2 rounded-full text-sm text-white">Follow up consistently</span>
                        <span class="bg-surface-container border border-outline-variant/20 px-4 py-2 rounded-full text-sm text-white">Capture more opportunities</span>
                        <span class="bg-surface-container border border-outline-variant/20 px-4 py-2 rounded-full text-sm text-white">Operate with less manual work</span>
                    </div>
                </div>

                <!-- Guarantee -->
                <div class="inline-flex items-center gap-6 bg-brand-green/10 border border-brand-green/30 rounded-2xl px-8 py-6 max-w-2xl text-left shadow-[0_0_20px_rgba(0,230,138,0.1)] group transition-all hover:bg-brand-green/20">
                    <span class="material-symbols-outlined text-brand-green text-5xl group-hover:scale-110 transition-transform">health_and_safety</span>
                    <div>
                        <h4 class="font-bold text-white text-lg font-headline mb-1">90-Day ROI Guarantee</h4>
                        <p class="text-on-surface-variant text-sm font-body">If Cresca OS doesn't generate enough qualified opportunities to cover your setup investment within 90 days, we'll refund it in full.</p>
                    </div>
                </div>

            </aside>

            <!-- Booking Form Column -->
            <section class="lg:col-span-7">
                <div class="bg-surface-container p-8 md:p-12 rounded-[2rem] shadow-2xl shadow-primary/5 relative overflow-hidden border border-primary/20">
                    <div class="absolute -top-24 -right-24 w-64 h-64 bg-primary/10 blur-[100px] rounded-full"></div>
                    
                    <div class="mb-10 text-center relative z-10">
                        <h2 class="font-headline text-3xl font-bold text-white mb-3">Book Your Free Audit Now</h2>
                        <div class="flex items-center justify-center gap-4 text-xs font-label uppercase tracking-widest text-primary font-bold">
                            <span class="flex items-center gap-1"><span class="material-symbols-outlined text-sm">bolt</span> Un 30s</span>
                            <span class="w-1 h-1 rounded-full bg-primary/50"></span>
                            <span class="flex items-center gap-1"><span class="material-symbols-outlined text-sm">event_available</span> Instant</span>
                            <span class="w-1 h-1 rounded-full bg-primary/50"></span>
                            <span class="flex items-center gap-1"><span class="material-symbols-outlined text-sm">waving_hand</span> No Obligation</span>
                        </div>
                    </div>

                    <form class="space-y-8 relative z-10">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                            <div class="space-y-2">
                                <label class="block font-label text-sm text-on-surface-variant uppercase tracking-wider">Full Name</label>
                                <input class="w-full bg-surface-container-lowest border-0 border-b-2 border-outline-variant/15 px-0 py-3 text-on-surface placeholder:text-outline transition-all duration-200" placeholder="John Doe" type="text"/>
                            </div>
                            <div class="space-y-2">
                                <label class="block font-label text-sm text-on-surface-variant uppercase tracking-wider">Company Email</label>
                                <input class="w-full bg-surface-container-lowest border-0 border-b-2 border-outline-variant/15 px-0 py-3 text-on-surface placeholder:text-outline transition-all duration-200" placeholder="john@company.com" type="email"/>
                            </div>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                            <div class="space-y-2">
                                <label class="block font-label text-sm text-on-surface-variant uppercase tracking-wider">Company Website</label>
                                <input class="w-full bg-surface-container-lowest border-0 border-b-2 border-outline-variant/15 px-0 py-3 text-on-surface placeholder:text-outline transition-all duration-200" placeholder="www.yourbusiness.com" type="url"/>
                            </div>
                            <div class="space-y-2">
                                <label class="block font-label text-sm text-on-surface-variant uppercase tracking-wider">Est. Monthly Leads</label>
                                <select class="w-full bg-surface-container-lowest border-0 border-b-2 border-outline-variant/15 px-0 py-3 text-on-surface transition-all duration-200 appearance-none cursor-pointer">
                                    <option>0 - 50 leads/mo</option>
                                    <option>50 - 200 leads/mo</option>
                                    <option>200 - 500 leads/mo</option>
                                    <option>500+ leads/mo</option>
                                </select>
                            </div>
                        </div>
                        <div class="space-y-2">
                            <label class="block font-label text-sm text-on-surface-variant uppercase tracking-wider">Your Biggest Operational Bottleneck</label>
                            <textarea class="w-full bg-surface-container-lowest border-0 border-b-2 border-outline-variant/15 px-0 py-3 text-on-surface placeholder:text-outline transition-all duration-200 resize-none" placeholder="What is currently slowing down your growth?" rows="4"></textarea>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                            <div class="space-y-2">
                                <label class="block font-label text-sm text-on-surface-variant uppercase tracking-wider">Desired Timeline</label>
                                <select class="w-full bg-surface-container-lowest border-0 border-b-2 border-outline-variant/15 px-0 py-3 text-on-surface transition-all duration-200 appearance-none cursor-pointer">
                                    <option>Immediate (As soon as possible)</option>
                                    <option>Within 30 days</option>
                                    <option>Within 90 days</option>
                                    <option>Just exploring options</option>
                                </select>
                            </div>
                        </div>
                        <div class="pt-6">
                            <button class="w-full signature-texture text-on-primary font-label font-bold py-5 rounded-xl text-lg flex items-center justify-center gap-3 transition-transform hover:scale-[1.02] shadow-[0_0_20px_rgba(10,132,255,0.3)] uppercase tracking-widest" type="submit">
                                Book My Free Audit →
                            </button>
                            <p class="mt-6 text-center text-[10px] text-error font-label uppercase tracking-widest font-bold">
                                Limited audit spots available each week.
                            </p>
                        </div>
                    </form>
                </div>
            </section>
        </div>
    </section>

</main>
"""

updated_html = re.sub(main_pattern, new_main_html, html)

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(updated_html)

print("book-audit.html has been successfully overwritten with the new copy.")
