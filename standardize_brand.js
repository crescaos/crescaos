const fs = require('fs');
const path = require('path');

const baseDir = 'public';

const LOGO_SVG = `<svg class="w-8 h-8" fill="none" height="32" viewbox="0 0 48 48" width="32" xmlns="http://www.w3.org/2000/svg">
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

const BRAND_MARKUP = `<div class="flex items-center gap-3">
${LOGO_SVG}
<div class="flex items-baseline font-serif text-2xl font-bold tracking-tighter">
<span class="text-white">CRESCA</span><span class="text-[#00E68A] ml-px">OS</span>
</div>
</div>`;

const NAV_CTA_CLASS = 'hidden md:inline-flex signature-texture text-white px-5 py-2.5 rounded-lg font-label font-bold transition-all duration-300 hover:scale-105 uppercase tracking-widest text-[10px] shadow-lg shadow-primary/20';

function getAllFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  files.forEach(file => {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      getAllFiles(filePath, fileList);
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  });
  return fileList;
}

const allFiles = getAllFiles(baseDir);

allFiles.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  let original = content;

  // 1. Standardize Navigation Brand (Logo + Text)
  // Look for any <a> tag that looks like a brand link
  content = content.replace(/<a class="flex items-center gap-3 hover:opacity-80 transition-opacity" href="\/">[\s\S]*?<\/a>/, 
    `<a class="flex items-center gap-3 hover:opacity-80 transition-opacity" href="/">${BRAND_MARKUP}</a>`);

  // 2. Standardize Navigation CTA
  // Look for buttons or links with specific phrases
  const ctaPhrases = ['Get Your Growth Score', 'Obtén tu Growth Score', 'Get Your Free Revenue Score'];
  ctaPhrases.forEach(phrase => {
    const regex = new RegExp(`<a href="\/diagnostic(?:\.html)?" class="[^"]*">${phrase}<\/a>`, 'g');
    content = content.replace(regex, `<a href="/diagnostic" class="${NAV_CTA_CLASS}">${phrase}</a>`);
  });

  // 3. Fix Encoding (Literal match for the problematic sequences)
  content = content.replace(/ðŸ‘‰/g, '&#x1F449;');
  content = content.replace(/dY`%/g, '&#x1F449;');
  content = content.replace(/ESPAÃ‘OL/g, 'ESPA&Ntilde;OL');

  // 4. Pricing Page Specific: Add logo to cards
  if (file.includes('pricing.html')) {
    // Add logo to card headers
    // Match the start of each card
    content = content.replace(/<div class="bg-surface-container p-10 rounded-\[2rem\] border border-outline-variant\/10 flex flex-col h-full hover:border-primary\/30 transition-all">/g, 
      `<div class="bg-surface-container p-10 rounded-[2rem] border border-outline-variant/10 flex flex-col h-full hover:border-primary/30 transition-all">
<div class="mb-6 opacity-40">${LOGO_SVG}</div>`);
  }

  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    console.log(`Standardized brand and logo in ${file}`);
  }
});
