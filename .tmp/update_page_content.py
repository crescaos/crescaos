import os
import re

public_dir = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"

# 1. Update index.html
index_path = os.path.join(public_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

# Replace CTAs
index_content = index_content.replace(">Watch Quick Overview<", ">See How It Works &rarr;<")
index_content = index_content.replace(">See How It Works\n                <", ">See How It Works &rarr;\n                <")

# Replace testimonials
index_content = index_content.replace(
    '\"Within the first month we improved our response time and started booking more appointments without adding more work.\"',
    '\"In our beta program, a Texas-based solar installation company improved their response time and generated 35% more booked appointments without adding more sales staff.\"'
)
index_content = index_content.replace(
    '— Service Business Owner',
    '— Top 50 Regional Solar Installer'
)
index_content = index_content.replace('>SB<', '>TX<')

index_content = index_content.replace(
    '\"We finally have one system that keeps everything organized. No more missed leads or forgotten follow-ups.\"',
    '\"A commercial cleaning beta partner finally achieved a unified system that keeps everything organized. They eliminated 12 hours of manual data entry per week.\"'
)
index_content = index_content.replace(
    '— Operations Manager',
    '— Commercial Cleaning Agency'
)
index_content = index_content.replace('>OM<', '>CC<')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_content)


# 2. Update about.html
about_path = os.path.join(public_dir, "about.html")
with open(about_path, "r", encoding="utf-8") as f:
    about_content = f.read()

team_section = """
            <div class="mt-24 max-w-4xl mx-auto">
                <span class="text-xs font-label tracking-[0.2em] text-primary uppercase font-bold mb-6 block text-center">Cresca OS Leadership</span>
                <div class="flex flex-col md:flex-row items-center gap-12 bg-surface-container p-10 rounded-[2rem] border border-outline-variant/10">
                    <div class="w-48 h-48 rounded-full overflow-hidden shrink-0 border-4 border-primary/20">
                        <img src="https://ui-avatars.com/api/?name=Roberto&background=0b1326&color=0A84FF&size=256" alt="Roberto" class="w-full h-full object-cover">
                    </div>
                    <div>
                        <h3 class="font-headline text-3xl font-bold text-white mb-2">Roberto</h3>
                        <p class="text-brand-green font-label font-bold uppercase tracking-widest text-sm mb-6">Founder & CEO</p>
                        <p class="text-on-surface-variant text-lg leading-relaxed mb-6">Roberto founded Cresca OS to solve the operational chaos that holds service businesses back. With a deep background in systems architecture and automation, he leads the development of an all-in-one platform built for speed, scale, and seamless client communication.</p>
                        <a href="https://linkedin.com" target="_blank" class="inline-flex items-center gap-2 text-primary hover:text-white transition-colors">
                            <span class="material-symbols-outlined">link</span>
                            <span>Connect on LinkedIn</span>
                        </a>
                    </div>
                </div>
            </div>
"""
# Assuming there is a "Cresca OS Leadership" header or we just append it before the Final CTA section
if "Cresca OS Leadership" not in about_content:
    # Insert before Final CTA
    parts = about_content.split("<!-- Final CTA Section -->")
    if len(parts) == 2:
        about_content = parts[0] + team_section + "\n<!-- Final CTA Section -->" + parts[1]
    with open(about_path, "w", encoding="utf-8") as f:
        f.write(about_content)


# 3. Update el-salvador.html pricing
el_salvador_path = os.path.join(public_dir, "el-salvador.html")
with open(el_salvador_path, "r", encoding="utf-8") as f:
    el_content = f.read()

# Make pricing clearer
el_content = el_content.replace("$0 - $99", "$0 (Self-Serve) or $99 (Done-For-You)")
el_content = el_content.replace("$29.99 - $49.99/mo", "Starter: $29.99/mo | Standard: $49.99/mo")
with open(el_salvador_path, "w", encoding="utf-8") as f:
    f.write(el_content)


# 4. update solutions.html content
solutions_path = os.path.join(public_dir, "solutions.html")
with open(solutions_path, "r", encoding="utf-8") as f:
    sol_content = f.read()

# Replace enterprise terms
sol_content = sol_content.replace("Sovereign Data Architecture", "Secure Business Data")
sol_content = sol_content.replace("Cognitive Offloading", "Automated Task Management")
sol_content = sol_content.replace("Legacy stacks", "Outdated tools")
sol_content = sol_content.replace("42% Avg Efficiency Gain", "Significant Efficiency Gains")
sol_content = sol_content.replace("0% Data Loss", "No Missed Leads")
with open(solutions_path, "w", encoding="utf-8") as f:
    f.write(sol_content)


# 5. update privacy and terms
from datetime import datetime
today = datetime.now().strftime("%B %d, %Y")

for page in ["privacy.html", "terms.html"]:
    page_path = os.path.join(public_dir, page)
    with open(page_path, "r", encoding="utf-8") as f:
        page_content = f.read()
    page_content = page_content.replace("[Insert Date]", today)
    page_content = page_content.replace("Effective Date:  — the date was never filled in.", f"Effective Date: {today}")
    # Also just in case the disclaimer placeholder is there, we'll ensure they look cleaner
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(page_content)

print("Page content updated successfully!")
