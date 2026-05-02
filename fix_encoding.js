const fs = require('fs');
const path = require('path');

const publicDir = path.join(__dirname, 'public');

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
  
  content = content.replace(/Â©/g, '©');
  content = content.replace(/Â&copy;/g, '&copy;');
  content = content.replace(/â€™/g, "'");
  content = content.replace(/â€œ/g, '"');
  content = content.replace(/â€\x9D/g, '"'); // Right quote
  content = content.replace(/â€”/g, '—'); // em dash
  content = content.replace(/â€“/g, '–'); // en dash
  content = content.replace(/â€¢/g, '•'); // bullet
  content = content.replace(/â†’/g, '→'); // right arrow
  
  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    changedFiles.push(file);
  }
});

console.log('Fixed encoding in:', changedFiles.length, 'files');
console.log(changedFiles.join('\n'));
