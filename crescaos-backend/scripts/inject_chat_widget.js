const fs = require('fs');
const path = require('path');

const scriptToInject = `
    <!-- GHL Chat Widget -->
    <script 
      src="https://widgets.leadconnectorhq.com/loader.js"  
      data-resources-url="https://widgets.leadconnectorhq.com/chat-widget/loader.js" 
      data-widget-id="69d3ebd934c0448115bc10d9"> 
    </script>
`;

function injectIntoDir(dir) {
    const files = fs.readdirSync(dir);
    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);
        if (stat.isDirectory()) {
            injectIntoDir(filePath);
        } else if (file.endsWith('.html')) {
            let content = fs.readFileSync(filePath, 'utf8');
            if (content.includes('data-widget-id="69d3ebd934c0448115bc10d9"')) {
                console.log(`Skipping ${filePath} - already installed`);
                return;
            }
            if (content.includes('</body>')) {
                content = content.replace('</body>', `${scriptToInject}\n</body>`);
                fs.writeFileSync(filePath, content);
                console.log(`Injected into ${filePath}`);
            }
        }
    });
}

const publicDir = path.join(__dirname, '..', '..', 'public');
injectIntoDir(publicDir);
