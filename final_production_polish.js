const fs = require('fs');
const path = require('path');

const DRY_RUN = false; // Set to false to apply changes

const PUBLIC_DIR = path.join(__dirname, 'public');

const CORRUPTED_MAPPINGS = [
    { from: /ESPAÃ‘OL/g, to: 'ESPAÑOL' },
    { from: /Ã¡/g, to: 'á' },
    { from: /Ã©/g, to: 'é' },
    { from: /Ã­/g, to: 'í' },
    { from: /Ã³/g, to: 'ó' },
    { from: /Ãº/g, to: 'ú' },
    { from: /Ã±/g, to: 'ñ' },
    { from: /Â¿/g, to: '¿' },
    { from: /Â¡/g, to: '¡' },
    { from: /ðŸ‘‰/g, to: '👉' }
];

// Safety entity for mobile menu ESPAÑOL to avoid server encoding issues
const ESPANOL_ENTITY_FIX = {
    from: /ESPAÑOL/g,
    to: 'ESPA&Ntilde;OL'
};

// Premium Logo SVG from index.html
const PREMIUM_LOGO_SVG = `<svg class="w-8 h-8" fill="none" height="32" viewbox="0 0 48 48" width="32" xmlns="http://www.w3.org/2000/svg">
<circle cx="24" cy="24" r="18" stroke="#0A84FF" stroke-width="3"></circle>
<ellipse cx="24" cy="24" rx="13" ry="7.5" stroke="#00E68A" stroke-width="3" transform="rotate(60 24 24)"></ellipse>
<ellipse cx="24" cy="24" rx="13" ry="7.5" stroke="#00E68A" stroke-width="3" transform="rotate(-60 24 24)"></ellipse>
<circle cx="24" cy="6" fill="#0A84FF" r="2.5"></circle>
<circle cx="24" cy="42" fill="#0A84FF" r="2.5"></circle>
<circle cx="39.59" cy="15" fill="#00E68A" r="2.5"></circle>
<circle cx="8.41" cy="15" fill="#FFFFFF" r="2.5"></circle>
<circle cx="39.59" cy="33" fill="#FFFFFF" r="2.5"></circle>
<circle cx="8.41" cy="33" fill="#00E68A" r="2.5"></circle>
<circle cx="24" cy="24" fill="#FFFFFF" r="3.5"></circle>
</svg>`;

// Brand Text implementation
const BRAND_TEXT = `<div class="flex items-baseline font-serif text-2xl font-bold tracking-tighter">
<span class="text-white">CRESCA</span><span class="text-[#00E68A] ml-px">OS</span>
</div>`;

const CHARSET_META = '<meta charset="UTF-8">';

function walkDir(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        if (fs.statSync(dirPath).isDirectory()) {
            walkDir(dirPath, callback);
        } else {
            callback(dirPath);
        }
    });
}

console.log(`[POLISH] Starting ${DRY_RUN ? 'DRY RUN' : 'EXECUTION'}...`);

walkDir(PUBLIC_DIR, (filePath) => {
    if (!filePath.endsWith('.html')) return;

    let content = fs.readFileSync(filePath, 'utf8');
    let originalContent = content;
    let filename = path.relative(PUBLIC_DIR, filePath);

    // 1. Ensure Charset Meta
    if (!content.includes('charset="UTF-8"') && !content.includes('charset="utf-8"')) {
        if (content.includes('<head>')) {
            content = content.replace('<head>', `<head>\n    ${CHARSET_META}`);
            console.log(`[CHARSET] Added UTF-8 meta to ${filename}`);
        }
    }

    // 2. Targeted Encoding Fixes (Corrupted sequences)
    CORRUPTED_MAPPINGS.forEach(mapping => {
        if (mapping.from.test(content)) {
            const matches = content.match(mapping.from).length;
            content = content.replace(mapping.from, mapping.to);
            console.log(`[ENCODING] Fixed ${matches} corrupted sequence(s) in ${filename}`);
        }
    });

    // 3. Safety Entity for ESPAÑOL (Mobile Menu / Nav)
    if (ESPANOL_ENTITY_FIX.from.test(content)) {
        content = content.replace(ESPANOL_ENTITY_FIX.from, ESPANOL_ENTITY_FIX.to);
        console.log(`[ENTITY] Standardized ESPAÑOL to entity in ${filename}`);
    }

    // 4. Pricing Callout Emoji Fix
    if (filename.includes('pricing.html')) {
        if (/👉/g.test(content)) {
            content = content.replace(/👉/g, '&#x1F449;');
            console.log(`[EMOJI] Replaced literal emoji with entity in ${filename}`);
        }
    }

    // 5. Logo Normalization (Header/Footer Branding)
    // Find branding links and ensure they contain the premium logo
    // Pattern: <a ... href="/" ...><div class="flex items-center gap-3">...<svg ...>...</svg>...</div></a>
    // This is complex for regex, so we'll target specific pages first as requested
    const targetBrandingPages = ['pricing.html', 'es/pricing.html', 'how-we-work.html', 'es/how-we-work.html', 'es/integrations.html', 'es/el-salvador.html'];
    if (targetBrandingPages.includes(filename.replace(/\\/g, '/'))) {
         // Logic for branding injection would go here if we were doing it via script.
         // Given the complexity of nested DIVs/SVGs, manual replacement is safer for these 6 files.
         console.log(`[BRANDING] Target branding page identified for manual/scripted polish: ${filename}`);
    }

    if (content !== originalContent) {
        if (!DRY_RUN) {
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`[SAVED] Applied changes to ${filename}`);
        } else {
            console.log(`[SKIP] Changes detected in ${filename} (Dry Run)`);
        }
    }
});

console.log(`[POLISH] Finished ${DRY_RUN ? 'DRY RUN' : 'EXECUTION'}.`);
