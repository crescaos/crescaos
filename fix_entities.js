const fs = require('fs');
const path = require('path');

const ENTITIES = {
    'Á': '&Aacute;',
    'É': '&Eacute;',
    'Í': '&Iacute;',
    'Ó': '&Oacute;',
    'Ú': '&Uacute;',
    'Ñ': '&Ntilde;',
    'á': '&aacute;',
    'é': '&eacute;',
    'í': '&iacute;',
    'ó': '&oacute;',
    'ú': '&uacute;',
    'ñ': '&ntilde;',
    '¿': '&iquest;',
    '¡': '&iexcl;',
    '→': '&rarr;'
};

const publicDir = path.join(__dirname, 'public');

function walk(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        let isDirectory = fs.statSync(dirPath).isDirectory();
        isDirectory ? walk(dirPath, callback) : callback(dirPath);
    });
}

console.log('Starting Entity Normalization...');

walk(publicDir, (filePath) => {
    if (!filePath.endsWith('.html')) return;

    let content = fs.readFileSync(filePath, 'utf8');
    let original = content;
    let changed = false;

    // Replace based on rules
    for (let [char, entity] of Object.entries(ENTITIES)) {
        if (content.includes(char)) {
            // Special rule: Only replace accented characters in Spanish files or specific global symbols
            if (char === '→' || filePath.includes('\\es\\')) {
                const regex = new RegExp(char, 'g');
                content = content.replace(regex, entity);
                changed = true;
            }
        }
    }

    if (changed) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Updated: ${path.relative(publicDir, filePath)}`);
    }
});

console.log('Entity Normalization Complete.');
