/**
 * Cresca OS Language Manager
 * Handles soft language detection, user preference persistence, and localized routing.
 */

(function() {
    const PREF_KEY = 'cresca_lang_pref';
    const isSpanishPage = window.location.pathname.includes('/es/');
    
    // 1. Language Detection & Banner
    function checkLanguage() {
        const savedPref = localStorage.getItem(PREF_KEY);
        const browserLang = navigator.language || navigator.userLanguage;
        const isBrowserSpanish = browserLang.startsWith('es');

        // Only show banner if no preference saved and browser is Spanish, but on English page
        if (!savedPref && isBrowserSpanish && !isSpanishPage) {
            showLanguageBanner();
        }
    }

    function showLanguageBanner() {
        const banner = document.createElement('div');
        banner.id = 'lang-suggestion-banner';
        banner.className = 'fixed bottom-4 left-4 right-4 md:left-auto md:right-8 md:max-w-md bg-[#0a0f1d] border border-[#00E68A]/30 text-white p-4 rounded-xl shadow-2xl z-[9999] animate-fade-in-up';
        banner.innerHTML = `
            <div class="flex items-start gap-4">
                <div class="bg-[#00E68A]/10 p-2 rounded-lg">
                    <span class="material-symbols-outlined text-[#00E68A]">language</span>
                </div>
                <div class="flex-1">
                    <p class="text-sm font-medium mb-2">¿Prefieres navegar en español?</p>
                    <div class="flex gap-3">
                        <button id="btn-switch-es" class="text-xs bg-[#00E68A] text-black px-3 py-1.5 rounded-lg font-bold hover:bg-[#00c978] transition-colors">Cambiar a ES</button>
                        <button id="btn-ignore-lang" class="text-xs text-gray-400 hover:text-white px-2 py-1.5 transition-colors">Cerrar</button>
                    </div>
                </div>
            </div>
        `;
        document.body.appendChild(banner);

        document.getElementById('btn-switch-es').onclick = () => {
            localStorage.setItem(PREF_KEY, 'es');
            const targetUrl = window.location.pathname === '/' ? '/es/index.html' : '/es' + window.location.pathname;
            window.location.href = targetUrl;
        };

        document.getElementById('btn-ignore-lang').onclick = () => {
            localStorage.setItem(PREF_KEY, 'en'); // Save 'en' so we don't bug them again
            banner.remove();
        };
    }

    // 2. Preference Persistence for Switcher
    // This part is handled by static links in the HTML, but we update the preference on click
    document.addEventListener('click', (e) => {
        const langLink = e.target.closest('[data-lang-switch]');
        if (langLink) {
            const lang = langLink.getAttribute('data-lang-switch');
            localStorage.setItem(PREF_KEY, lang);
        }
    });

    // 3. Initialize
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', checkLanguage);
        document.addEventListener('DOMContentLoaded', preserveUTMs);
    } else {
        checkLanguage();
        preserveUTMs();
    }

    // 4. UTM Preserver Logic
    function preserveUTMs() {
        const queryString = window.location.search;
        if (!queryString) return; // No parameters to preserve

        const urlParams = new URLSearchParams(queryString);
        
        // Find all links that point to the diagnostic funnel
        const diagnosticLinks = document.querySelectorAll('a[href*="/diagnostic.html"]');
        
        diagnosticLinks.forEach(link => {
            try {
                // Parse the link's href
                const linkUrl = new URL(link.href, window.location.origin);
                
                // Add all current URL params to the link
                for (const [key, value] of urlParams) {
                    if (!linkUrl.searchParams.has(key)) {
                        linkUrl.searchParams.append(key, value);
                    }
                }
                
                // Update the href relative or absolute as appropriate
                // Keep relative path if it was relative
                if (link.getAttribute('href').startsWith('/')) {
                    link.setAttribute('href', linkUrl.pathname + linkUrl.search + linkUrl.hash);
                } else if (!link.getAttribute('href').startsWith('http')) {
                    // if it was like "diagnostic.html"
                    link.setAttribute('href', linkUrl.pathname.split('/').pop() + linkUrl.search + linkUrl.hash);
                } else {
                    link.href = linkUrl.toString();
                }
            } catch (e) {
                console.error("Error preserving UTMs for link:", link.href, e);
            }
        });
    }
})();
