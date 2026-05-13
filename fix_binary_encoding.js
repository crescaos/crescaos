const fs = require('fs');
const path = require('path');

const baseDir = 'public';

function getAllFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  files.forEach(file => {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      getAllFiles(filePath, fileList);
    } else if (file.endsWith('.html') || file.endsWith('.js')) {
      fileList.push(filePath);
    }
  });
  return fileList;
}

const allFiles = getAllFiles(baseDir);

// These are patterns that appear when UTF-8 bytes are read as windows-1252/latin1
const replacements = [
  { p: /ðŸ¢/g, r: '&#x1F7E2;' }, // 🟢
  { p: /ðŸ¡/g, r: '&#x1F7E1;' }, // 🟡
  { p: /ðŸ”´/g, r: '&#x1F534;' }, // 🔴
  { p: /ðŸš€/g, r: '&#x1F680;' }, // 🚀
  { p: /ðŸ‘‰/g, r: '&#x1F449;' }, // 👉
  { p: /ðŸ§/g, r: '&#x1F3E0;' },  // 🏠
  { p: /ðŸ ¥/g, r: '&#x1F3E5;' }, // 🏥
  { p: /ðŸ ¢/g, r: '&#x1F4BC;' }, // 💼
  { p: /ðŸš—/g, r: '&#x1F697;' }, // 🚗
  { p: /ðŸ“¦/g, r: '&#x1F4E6;' }, // 📦
];

allFiles.forEach(file => {
  // Read as latin1 to preserve the raw bytes as single characters
  let content = fs.readFileSync(file, 'binary');
  let original = content;

  // We need to match the raw bytes. 
  // For example, 🟢 is f0 9f 9f a2.
  // In latin1, that's ðŸ¢.
  
  replacements.forEach(rep => {
    // Convert the pattern to a binary string if it's not already
    content = content.split(rep.p.source).join(rep.r);
  });

  if (content !== original) {
    fs.writeFileSync(file, content, 'binary');
    console.log(`Fixed encoding in ${file}`);
  }
});
