import os
import glob
import re

PUBLIC_DIR = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"

neural_css = """
      #neural-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        opacity: 0.8; /* Amplified visibility */
        pointer-events: none;
      }
"""

neural_js = """

      // Neural Network Particle Background
      window.addEventListener('DOMContentLoaded', () => {
        const canvas = document.getElementById('neural-bg');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        let particles = [];
        const particleCount = 80; /* Increased particles */
        const maxDistance = 160;

        function resize() {
          canvas.width = window.innerWidth;
          canvas.height = window.innerHeight;
        }

        window.addEventListener('resize', resize);
        resize();

        class Particle {
          constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.vx = (Math.random() - 0.5) * 0.5;
            this.vy = (Math.random() - 0.5) * 0.5;
            this.radius = Math.random() * 2 + 0.5;
          }

          update() {
            this.x += this.vx;
            this.y += this.vy;

            if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
            if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
          }

          draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(0, 230, 138, 0.9)'; /* Brighter particles */
            ctx.fill();
          }
        }

        for (let i = 0; i < particleCount; i++) {
          particles.push(new Particle());
        }

        function animate() {
          ctx.clearRect(0, 0, canvas.width, canvas.height);
          
          for (let i = 0; i < particles.length; i++) {
            particles[i].update();
            particles[i].draw();

            for (let j = i + 1; j < particles.length; j++) {
              const dx = particles[i].x - particles[j].x;
              const dy = particles[i].y - particles[j].y;
              const distance = Math.sqrt(dx * dx + dy * dy);

              if (distance < maxDistance) {
                ctx.beginPath();
                ctx.moveTo(particles[i].x, particles[i].y);
                ctx.lineTo(particles[j].x, particles[j].y);
                ctx.strokeStyle = `rgba(10, 132, 255, ${0.4 * (1 - distance / maxDistance)})`; /* Brighter connections */
                ctx.lineWidth = 0.8;
                ctx.stroke();
              }
            }
          }
          requestAnimationFrame(animate);
        }

        animate();
      });
"""

for filepath in glob.glob(os.path.join(PUBLIC_DIR, "*.html")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update/Inject CSS
    if '#neural-bg' in content:
        # It's in index.html, replace the block.
        content = re.sub(r'#neural-bg\s*\{[^}]*\}', neural_css.strip(), content)
    else:
        # Inject into other files right before </style>
        content = content.replace('</style>', neural_css + '</style>')

    # 2. Update/Inject JS
    if 'Neural Network Particle Background' in content:
        content = re.sub(r'// Neural Network Particle Background[\s\S]*?animate\(\);\s*\}\);', neural_js.strip(), content)
    else:
        # Inject right before the first </script> that comes after toggleLanguage()
        content = re.sub(r'(function toggleLanguage\(\) \{[\s\S]*?\})\s*</script>', r'\1' + neural_js + '\n    </script>', content)

    # 3. Update/Inject Canvas
    if '<canvas id="neural-bg">' not in content:
        # Find exactly the body tag starting
        content = re.sub(r'(<body[^>]*>)', r'\1\n<canvas id="neural-bg"></canvas>', content)
        # Add 'relative' to body class if not there, for proper canvas positioning context if needed, 
        # but fixed works fine without it. Let's just add relative to be safe.
        if 'class="' in content.split('<body')[1].split('>')[0]:
            if 'relative' not in content:
                content = re.sub(r'(<body[^>]*class="[^"]*)(")', r'\1 relative\2', content)

    # 4. Fix Links
    # Update specific text matches for #
    content = content.replace('href="#"', 'href="javascript:void(0)"') # fallback for any missed
    content = re.sub(r'<a[^>]*href="[^"]*"[^>]*>\s*Privacy Policy\s*</a>', lambda m: m.group(0).replace('href="javascript:void(0)"', 'href="privacy.html"').replace('href="#"', 'href="privacy.html"'), content)
    content = re.sub(r'<a[^>]*href="[^"]*"[^>]*>\s*Terms of Service\s*</a>', lambda m: m.group(0).replace('href="javascript:void(0)"', 'href="terms.html"').replace('href="#"', 'href="terms.html"'), content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(glob.glob(os.path.join(PUBLIC_DIR, '*.html')))} files.")
