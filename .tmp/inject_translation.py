import os
import glob
import re

PUBLIC_DIR = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"
html_files = glob.glob(os.path.join(PUBLIC_DIR, "*.html"))

translation_css = """
      /* Seamless Translation CSS */
      body { top: 0 !important; }
      .goog-te-banner-frame { display: none !important; }
      #goog-gt-tt { display: none !important; }
      .goog-te-spinner-pos { display: none !important; }
      #google_translate_element { display: none !important; }
      font { background-color: transparent !important; box-shadow: none !important; }
"""

translation_js = """
    <!-- Headless Translation Engine -->
    <div id="google_translate_element"></div>
    <script type="text/javascript">
      function googleTranslateElementInit() {
        new google.translate.TranslateElement({pageLanguage: 'en', includedLanguages: 'es', autoDisplay: false}, 'google_translate_element');
      }
    </script>
    <script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
    <script>
      function toggleLanguage() {
        // Toggle the Google Translate cookie
        const isSpanish = document.cookie.includes('googtrans=/en/es');
        if (isSpanish) {
          document.cookie = "googtrans=/en/en; path=/";
          document.cookie = "googtrans=/en/en; domain=" + location.hostname + "; path=/";
        } else {
          document.cookie = "googtrans=/en/es; path=/";
          document.cookie = "googtrans=/en/es; domain=" + location.hostname + "; path=/";
        }
        window.location.reload();
      }

      window.addEventListener('DOMContentLoaded', () => {
        const isSpanish = document.cookie.includes('googtrans=/en/es');
        const toggleBtns = document.querySelectorAll('#lang-toggle');
        toggleBtns.forEach(btn => {
          btn.innerText = isSpanish ? 'ES/EN' : 'EN/ES';
          if (isSpanish) {
            btn.classList.add('text-[#00E68A]');
          }
        });
      });
    </script>
"""

# Patterns to replace or remove
old_js_pattern = re.compile(r'<script>\s*function toggleLanguage\(\) \{[\s\S]*?\}\s*</script>', re.MULTILINE)
old_css_pattern = re.compile(r'\.en-only \{[^\}]*\}\s*\.es-only \{[^\}]*\}\s*body\.lang-es \.en-only \{[^\}]*\}\s*body\.lang-es \.es-only \{[^\}]*\}', re.MULTILINE)

# Some files had the neural-bg script which we DO NOT WANT TO DELETE
# We must carefully inject our JS right before </head> or <body>

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Strip old toggle JS (if it exists)
    # Be careful not to strip the neural-bg script. 
    # We will just look for `function toggleLanguage()` and replace its script block.
    # Actually, the neural-bg and toggleLanguage might be in the same <script> block in some files.
    # Let's use regex to selectively remove the toggleLanguage function.
    content = re.sub(r'function toggleLanguage\(\)\s*\{[^}]+\}', '', content)
    
    # 2. Add translation CSS before </style>
    if "/* Seamless Translation CSS */" not in content:
        content = content.replace("</style>", translation_css + "\n</style>", 1)
    
    # 3. Add translation JS before </head>
    if 'id="google_translate_element"' not in content:
        content = content.replace("</head>", translation_js + "\n</head>", 1)
        
    # 4. Strip old en-only / es-only CSS
    content = old_css_pattern.sub('', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Seamless Translation Engine injected into all HTML files.")
