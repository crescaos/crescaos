const fs = require('fs');
const path = require('path');

const publicDir = path.join(__dirname, 'public', 'es');

function walk(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach(file => {
    file = path.join(dir, file);
    const stat = fs.statSync(file);
    if (stat && stat.isDirectory()) { 
      results = results.concat(walk(file));
    } else if (file.endsWith('.html')) {
      results.push(file);
    }
  });
  return results;
}

const files = walk(publicDir);
let changedFiles = [];

files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  let original = content;
  
  // Common corruptions seen in logs
  content = content.replace(/ACuAnto/g, '¿Cuánto');
  content = content.replace(/A/g, '¿');
  content = content.replace(/CuAnto/g, 'Cuánto');
  content = content.replace(/tamaAo/g, 'tamaño');
  content = content.replace(/implementaciA3n/g, 'implementación');
  content = content.replace(/bAsica/g, 'básica');
  content = content.replace(/pAgina/g, 'página');
  content = content.replace(/tecnolA3gicos/g, 'tecnológicos');
  content = content.replace(/especA-ficos/g, 'específicos');
  content = content.replace(/A-ficos/g, 'íficos');
  content = content.replace(/A3n/g, 'ón');
  content = content.replace(/A/g, 'á'); // Generic catch for 'á' if followed by certain chars
  
  // General fixes
  content = content.replace(/Â©/g, '©');
  content = content.replace(/Â&copy;/g, '&copy;');
  content = content.replace(/â€™/g, "'");
  content = content.replace(/â€œ/g, '"');
  content = content.replace(/â€\x9D/g, '"');
  content = content.replace(/â€”/g, '—');
  content = content.replace(/â€“/g, '–');
  
  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    changedFiles.push(file);
  }
});

console.log('Fixed Spanish encoding in:', changedFiles.length, 'files');
console.log(changedFiles.join('\n'));
