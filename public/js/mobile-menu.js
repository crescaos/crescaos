/**
 * Standardized Mobile Menu Logic for Cresca OS
 * Handles toggling, transitions, and accessibility (Escape key).
 */
document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('mobile-menu-btn');
    const closeBtn = document.getElementById('close-menu') || document.getElementById('mobile-menu-close');
    const menu = document.getElementById('mobile-menu');
    
    if (!btn || !menu) return;

    function toggleMenu(show) {
        if (show) {
            menu.style.display = 'flex';
            menu.classList.remove('hidden');
            // Tiny delay to allow display:flex to apply before animating transform
            setTimeout(() => {
                menu.classList.remove('translate-x-full');
                menu.classList.add('translate-x-0');
            }, 10);
            // Prevent body scroll when menu is open
            document.body.style.overflow = 'hidden';
        } else {
            menu.classList.remove('translate-x-0');
            menu.classList.add('translate-x-full');
            setTimeout(() => {
                menu.classList.add('hidden');
                menu.style.display = 'none';
                document.body.style.overflow = '';
            }, 300);
        }
    }

    btn.addEventListener('click', () => toggleMenu(true));
    
    if (closeBtn) {
        closeBtn.addEventListener('click', () => toggleMenu(false));
    }

    // Close on backdrop click (if applicable, though current design covers full screen)
    menu.addEventListener('click', (e) => {
        if (e.target === menu) {
            toggleMenu(false);
        }
    });

    // Close on escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && !menu.classList.contains('translate-x-full')) {
            toggleMenu(false);
        }
    });

    // Close menu when a link is clicked (useful for anchor links on the same page)
    const links = menu.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('click', () => toggleMenu(false));
    });

    // Handle resize: close menu if switching to desktop
    window.addEventListener('resize', () => {
        if (window.innerWidth >= 768 && !menu.classList.contains('translate-x-full')) {
            toggleMenu(false);
        }
    });
});
