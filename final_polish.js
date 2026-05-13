const fs = require('fs');
const path = require('path');

const baseDir = 'public';

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

const replacements = [
  // Fix the Spanish word in the mobile menu toggle
  { p: /ESPAÃ‘OL/g, r: 'ESPA&Ntilde;OL' },
  { p: />ESPAÑOL</g, r: '>ESPA&Ntilde;OL<' },
  
  // Fix the "Point Right" emoji in pricing page
  { p: /ðŸ‘‰/g, r: '&#x1F449;' },
  { p: /dY`%/g, r: '&#x1F449;' },
  
  // Ensure all Nav CTAs are standardized
  { p: /class="hidden md:inline-flex signature-texture text-white px-5 py-2.5 rounded-lg font-label font-bold transition-all duration-300 hover:scale-105 uppercase tracking-widest text-\[10px\] shadow-lg shadow-primary\/20"/g,
    r: 'class="hidden md:inline-flex signature-texture text-white px-5 py-2.5 rounded-lg font-label font-bold transition-all duration-300 hover:scale-105 uppercase tracking-widest text-[10px] shadow-lg shadow-primary/20"' },

  // Fix malformed icons in diagnostic again (just in case)
  { p: /e:'🟢'/g, r: "e:'&#x1F7E2;'" },
  { p: /e:'🟡'/g, r: "e:'&#x1F7E1;'" },
  { p: /e:'🔴'/g, r: "e:'&#x1F534;'" },
  { p: /e:'🚀'/g, r: "e:'&#x1F680;'" },
  { p: /e:'👉'/g, r: "e:'&#x1F449;'" },
  { p: /e:'🏠'/g, r: "e:'&#x1F3E0;'" },
  { p: /e:'🏥'/g, r: "e:'&#x1F3E5;'" },
  { p: /e:'💼'/g, r: "e:'&#x1F4BC;'" },
  { p: /e:'🚗'/g, r: "e:'&#x1F697;'" },
  { p: /e:'📦'/g, r: "e:'&#x1F4E6;'" },
];

allFiles.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  let original = content;

  replacements.forEach(rep => {
    content = content.replace(rep.p, rep.r);
  });

  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    console.log(`Polished ${file}`);
  }
});
