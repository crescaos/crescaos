const fs = require('fs');
const path = require('path');

const baseDir = 'public';

function getAllHtmlFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  files.forEach(file => {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      getAllHtmlFiles(filePath, fileList);
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  });
  return fileList;
}

const htmlFiles = getAllHtmlFiles(baseDir);

const standardNavBtnClass = 'hidden md:inline-flex signature-texture text-white px-5 py-2.5 rounded-lg font-label font-bold transition-all duration-300 hover:scale-105 uppercase tracking-widest text-[10px] shadow-lg shadow-primary/20';

htmlFiles.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  let original = content;

  // More robust regex: find <a> tags containing "hidden md:inline-flex" and href to diagnostic
  content = content.replace(/<a\s+([^>]*hidden md:inline-flex[^>]*)>(.*?)<\/a>/gs, (match, attrs, text) => {
    if (attrs.includes('href="/diagnostic') || attrs.includes('href="/es/diagnostic')) {
      const hrefMatch = attrs.match(/href="([^"]+)"/);
      const href = hrefMatch ? hrefMatch[1] : '/diagnostic';
      return `<a href="${href}" class="${standardNavBtnClass}">${text.trim()}</a>`;
    }
    return match;
  });

  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    console.log(`Updated Nav CTA in ${file}`);
  }
});
