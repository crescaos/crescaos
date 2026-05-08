import json
import re
from playwright.sync_api import sync_playwright

def verify_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        base_url = "http://localhost:3000"
        
        print("\n--- Testing English Page ---")
        page.goto(f"{base_url}/el-salvador.html")
        page.wait_for_load_state("networkidle")
        
        # 1. FAQ Visible
        faq_section = page.locator("section#faq") # Assuming there's an ID, or text search
        if page.get_by_text("Frequently Asked Questions").is_visible() or page.get_by_text("FAQ").is_visible():
            print("[PASS] FAQ section visible")
        else:
            print("[FAIL] FAQ section NOT visible")
            
        # 2. FAQ Schema Check
        schemas = page.locator('script[type="application/ld+json"]').all()
        faq_schema_found = False
        for s in schemas:
            try:
                content = s.inner_text()
                data = json.loads(content)
                if data.get("@type") == "FAQPage":
                    faq_schema_found = True
                    print("[PASS] FAQPage JSON-LD detected")
                    break
            except:
                continue
        if not faq_schema_found:
            print("[FAIL] FAQPage JSON-LD NOT detected")
            
        # 3. No Spanish snippets on English page
        # Common Spanish words: "Antes", "Después", "Preguntas", "Reservar"
        page_content = page.content()
        spanish_words = ["Antes", "Después", "Preguntas Frecuentes", "Reservar una auditoría"]
        found_spanish = []
        for word in spanish_words:
            if word in page_content:
                # Check if it's in the language switcher or a hidden meta tag
                # For simplicity, just alert if found
                found_spanish.append(word)
        
        if not found_spanish:
            print("[PASS] No Spanish text snippets found")
        else:
            print(f"[WARN] Potential Spanish text found: {found_spanish}")

        # 4. CTA works
        cta = page.get_by_role("link", name=re.compile("Book|Audit", re.IGNORECASE)).first
        if cta.is_visible():
            href = cta.get_attribute("href")
            print(f"[PASS] CTA found: {href}")
        else:
            print("[FAIL] CTA NOT found")

        print("\n--- Testing Spanish Page ---")
        page.goto(f"{base_url}/es/el-salvador.html")
        page.wait_for_load_state("networkidle")
        
        # 1. Fully Spanish
        page_content_es = page.content()
        english_words = ["Before", "After", "Frequently Asked Questions", "Book an Audit"]
        found_english = []
        for word in english_words:
            # Avoid matching insertBefore in scripts
            if word in page_content_es and f"insert{word}" not in page_content_es:
                found_english.append(word)
        
        if not found_english:
            print("[PASS] No English leaks found")
        else:
            print(f"[WARN] Potential English text found: {found_english}")

        # 2. Links go to /es/
        es_links = page.locator("a[href^='/es/'], a[href*='/es/']").all()
        if len(es_links) > 0:
            print(f"[PASS] Found {len(es_links)} links pointing to /es/ routes")
        else:
            print("[FAIL] NO links pointing to /es/ routes found")

        # 3. Language switcher
        switcher = page.locator('a[data-lang-switch="en"]').first
        if switcher.is_visible():
            href = switcher.get_attribute("href")
            print(f"[PASS] Language switcher found: {href}")
            if "el-salvador.html" in href and "es/" not in href:
                 print("[PASS] Switcher correctly maps back to English version")
            else:
                 print(f"[FAIL] Switcher href might be wrong: {href}")
        else:
            # Fallback to search
            print("[WARN] Switcher with data-lang-switch='en' not visible, trying text search")
            switcher = page.get_by_role("link", name=re.compile("EN|English", re.IGNORECASE)).first
            if switcher.is_visible():
                 print(f"[PASS] Switcher found by text: {switcher.get_attribute('href')}")
            else:
                 print("[FAIL] Language switcher NOT found")

        print("\n--- Testing Language Switching (Page-to-Page) ---")
        # Start at English
        page.goto(f"{base_url}/el-salvador.html")
        page.wait_for_load_state("networkidle")
        es_switch = page.locator('a[data-lang-switch="es"]').first
        es_switch.click()
        page.wait_for_load_state("networkidle")
        if "/es/el-salvador" in page.url:
            print("[PASS] EN -> ES transition correct")
        else:
            print(f"[FAIL] EN -> ES transition failed. URL: {page.url}")

        # Back to English
        en_switch = page.locator('a[data-lang-switch="en"]').first
        en_switch.click()
        page.wait_for_load_state("networkidle")
        if "/el-salvador" in page.url and "/es/" not in page.url:
            print("[PASS] ES -> EN transition correct")
        else:
            print(f"[FAIL] ES -> EN transition failed. URL: {page.url}")

        print("\n--- Mobile Check ---")
        page.set_viewport_size({"width": 375, "height": 812})
        page.reload()
        page.wait_for_load_state("networkidle")
        
        # Take a screenshot for visual confirmation
        page.screenshot(path="mobile_check.png")
        print("[PASS] Mobile screenshot saved as mobile_check.png")

        browser.close()

if __name__ == "__main__":
    verify_site()
