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

const replacements = [
  // Common broken sequences found in the grep
  { p: /dYY/g, r: '&#x1F7E2;' }, // 🟢 Functional
  { p: /dY`%/g, r: '&#x1F449;' }, // 👉
  { p: /dY/g, r: '&#x1F449;' },  // 👉 alternative
  { p: /dY‘/g, r: '&#x1F449;' }, // 👉 alternative
  
  // Character entities for Spanish
  { p: /Ã±/g, r: '&ntilde;' },
  { p: /Ã³/g, r: '&oacute;' },
  { p: /Ã¡/g, r: '&aacute;' },
  { p: /Ã©/g, r: '&eacute;' },
  { p: /Ã­/g, r: '&iacute;' },
  { p: /Ãº/g, r: '&uacute;' },
  { p: /Â¿/g, r: '&iquest;' },
  { p: /Â¡/g, r: '&iexcl;' },
  { p: /Â©/g, r: '&copy;' },
  { p: /Ã‘/g, r: '&Ntilde;' },
  { p: /Ã“/g, r: '&Oacute;' },
  { p: /Ã /g, r: '&Aacute;' },
  { p: /Ã‰/g, r: '&Eacute;' },
  { p: /Ã /g, r: '&Iacute;' },
  { p: /Ãš/g, r: '&Uacute;' }
];

allFiles.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  let original = content;

  replacements.forEach(rep => {
    content = content.replace(rep.p, rep.r);
  });

  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    console.log(`Fixed encoding in ${file}`);
  }
});
