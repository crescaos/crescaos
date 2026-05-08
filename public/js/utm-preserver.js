/**
 * Cresca OS UTM Preserver
 * Appends URL parameters (like UTM tags) to diagnostic funnel links
 * so tracking is preserved as the user navigates the site.
 */

(function() {
    function preserveUTMs() {
        const queryString = window.location.search;
        if (!queryString) return; // No parameters to preserve

        const urlParams = new URLSearchParams(queryString);
        
        // Find all links that point to the diagnostic funnel
        const diagnosticLinks = document.querySelectorAll('a[href*="/diagnostic.html"]');
        
        diagnosticLinks.forEach(link => {
            try {
                // Parse the link's href
                const linkUrl = new URL(link.href);
                
                // Add all current URL params to the link
                for (const [key, value] of urlParams) {
                    if (!linkUrl.searchParams.has(key)) {
                        linkUrl.searchParams.append(key, value);
                    }
                }
                
                // Update the href
                link.href = linkUrl.toString();
            } catch (e) {
                console.error("Error preserving UTMs for link:", link.href, e);
            }
        });
    }

    // Run on load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', preserveUTMs);
    } else {
        preserveUTMs();
    }
})();
