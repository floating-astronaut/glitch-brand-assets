"""Generate all brand asset variants from the source mascot."""
from PIL import Image, ImageDraw, ImageFont
import os, subprocess

SRC = '/home/support/glitch-brand-assets/mascot/raw/cobra-mascot.png'
ROOT = '/home/support/glitch-brand-assets'

src = Image.open(SRC).convert('RGBA')
print(f'Source: {src.size}, mode {src.mode}')

# ── Mascot square variants (PNG, dark bg preserved) ──
sizes_mascot = [64, 128, 256, 512, 1024]
for s in sizes_mascot:
    out = src.resize((s, s), Image.LANCZOS)
    path = f'{ROOT}/mascot/web/mascot-{s}.png'
    out.save(path, 'PNG', optimize=True)
    print(f'mascot-{s}.png → {os.path.getsize(path)//1024}KB')

# ── Favicons ──
for s in [16, 32, 48]:
    out = src.resize((s, s), Image.LANCZOS)
    path = f'{ROOT}/favicon/favicon-{s}.png'
    out.save(path, 'PNG', optimize=True)

# Multi-resolution .ico
ico_imgs = [src.resize((s, s), Image.LANCZOS) for s in [16, 32, 48]]
ico_imgs[0].save(f'{ROOT}/favicon/favicon.ico', format='ICO',
                 sizes=[(16, 16), (32, 32), (48, 48)],
                 append_images=ico_imgs[1:])

# Apple touch icon (180×180)
src.resize((180, 180), Image.LANCZOS).save(f'{ROOT}/favicon/apple-touch-icon.png', 'PNG', optimize=True)

# PWA icons
for s in [192, 512]:
    src.resize((s, s), Image.LANCZOS).save(f'{ROOT}/favicon/icon-{s}.png', 'PNG', optimize=True)

print('Favicons done.')

# ── OG image: 1200×630 with mascot + wordmark ──
og = Image.new('RGBA', (1200, 630), (10, 10, 15, 255))  # base color #0a0a0f

# Subtle radial-ish gradient (using a green glow circle behind mascot)
glow = Image.new('RGBA', (1200, 630), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
# Green glow centered behind the mascot
cx, cy = 350, 315
for r in range(400, 0, -20):
    alpha = max(0, 30 - (400 - r) // 15)
    gd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 255, 136, alpha))
og = Image.alpha_composite(og, glow)

# Place mascot on the left
m = src.resize((520, 520), Image.LANCZOS)
og.paste(m, (90, 55), m)

# Wordmark on the right
draw = ImageDraw.Draw(og)
# Use Inter if available, fall back to default
try:
    font_paths = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        '/usr/share/fonts/TTF/DejaVuSans-Bold.ttf',
    ]
    font_big = None
    font_small = None
    font_mono = None
    for p in font_paths:
        if os.path.exists(p):
            font_big = ImageFont.truetype(p, 88)
            font_med = ImageFont.truetype(p, 36)
            font_small = ImageFont.truetype(p.replace('Bold', ''), 28)
            break
    if font_big is None:
        font_big = ImageFont.load_default()
        font_med = font_big
        font_small = font_big
except Exception as e:
    print(f'Font fallback: {e}')
    font_big = ImageFont.load_default()
    font_med = font_big
    font_small = font_big

# Text positioning (right side)
tx = 670
draw.text((tx, 180), 'Glitch', font=font_big, fill=(255, 255, 255, 255))
draw.text((tx, 280), 'Executor', font=font_big, fill=(0, 255, 136, 255))
draw.text((tx, 400), 'AI Systems Lab', font=font_med, fill=(160, 160, 180, 255))
draw.text((tx, 460), 'glitchexecutor.com', font=font_small, fill=(100, 100, 120, 255))

og.convert('RGB').save(f'{ROOT}/og/og-image.png', 'PNG', optimize=True)
print(f'OG image: {os.path.getsize(f"{ROOT}/og/og-image.png")//1024}KB')

# Smaller OG variants
og_small = og.resize((600, 315), Image.LANCZOS)
og_small.convert('RGB').save(f'{ROOT}/og/og-image-small.png', 'PNG', optimize=True)

print('All assets generated.')
