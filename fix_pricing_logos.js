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
  if (!file.includes('pricing.html')) return;

  let content = fs.readFileSync(file, 'utf8');
  let original = content;

  // Tier 1 & 3 & 4 (Revenue Hub) often share this base class
  const class1 = 'bg-surface-container p-10 rounded-[2rem] border border-outline-variant/10 flex flex-col h-full hover:border-primary/30 transition-all';
  const class2 = 'bg-surface-container-high p-10 rounded-[2rem] border-2 border-brand-green flex flex-col h-full relative transform lg:scale-105 shadow-[0_0_40px_rgba(0,230,138,0.15)] z-10';
  const class3 = 'bg-surface-container p-10 rounded-[2rem] border border-outline-variant/10 flex flex-col h-full hover:border-brand-green/30 transition-all'; // ES version has this for Revenue

  // Robust replacement: match the opening div and check if it already has the logo
  const cards = [class1, class2, class3];
  
  cards.forEach(cls => {
    const regex = new RegExp(`<div class="${cls.replace(/\[/g, '\\[').replace(/\]/g, '\\]').replace(/\//g, '\\/') }">`, 'g');
    content = content.replace(regex, (match) => {
      // If the logo isn't already there in the next 100 chars, add it
      return match + `\n<div class="mb-6 opacity-40">${LOGO_SVG}</div>`;
    });
  });

  // Cleanup: avoid double logos if script is run twice
  const doubleLogo = `<div class="mb-6 opacity-40">${LOGO_SVG}</div>\n<div class="mb-6 opacity-40">${LOGO_SVG}</div>`;
  while(content.includes(doubleLogo)) {
    content = content.replace(doubleLogo, `<div class="mb-6 opacity-40">${LOGO_SVG}</div>`);
  }

  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    console.log(`Fixed pricing logos in ${file}`);
  }
});
