from PIL import Image, ImageDraw, ImageFont
import os

public_dir = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public"

# Generate favicon.ico
img = Image.new('RGB', (64, 64), color = (10, 132, 255))
d = ImageDraw.Draw(img)
# Draw a simple C
try:
    font = ImageFont.truetype("arial.ttf", 48)
except IOError:
    font = ImageFont.load_default()
d.text((12, 6), "C", fill=(0, 230, 138), font=font)
img.save(os.path.join(public_dir, 'favicon.ico'), format='ICO', sizes=[(64,64)])

# Generate og-image.jpg
og = Image.new('RGB', (1200, 630), color = (11, 19, 38))
dog = ImageDraw.Draw(og)
try:
    font_og = ImageFont.truetype("arialbd.ttf", 80)
    font_sub = ImageFont.truetype("arial.ttf", 40)
except IOError:
    font_og = ImageFont.load_default()
    font_sub = ImageFont.load_default()

dog.text((100, 200), "Cresca OS", fill=(10, 132, 255), font=font_og)
dog.text((100, 300), "Business Automation System", fill=(0, 230, 138), font=font_sub)
og.save(os.path.join(public_dir, 'og-image.jpg'), format='JPEG')

print("Favicon and OG image generated")
