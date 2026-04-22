"""Generate GitHub social preview images (1280×640) for every public repo.

Run: python3 generate_repo_social.py
Output: og/repos/<repo-name>.png
Upload manually at: https://github.com/<org>/<repo>/settings (Social preview).
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import os

ROOT = Path('/home/support/glitch-brand-assets')
SRC = ROOT / 'mascot/raw/cobra-mascot.png'
OUT_DIR = ROOT / 'og/repos'
OUT_DIR.mkdir(parents=True, exist_ok=True)

W, H = 1280, 640
BG = (10, 10, 15, 255)
GREEN = (0, 255, 136, 255)
WHITE = (255, 255, 255, 255)
MUTED = (160, 160, 180, 255)
DIM = (100, 100, 120, 255)
LINE_COLOR = {
    'Trade': (255, 176, 32, 255),
    'Edge': (64, 164, 255, 255),
    'Grow': GREEN,
    'Labs': GREEN,
}

REPOS = [
    # (repo, product_line, short_name, tagline)
    ('glitch-grow-ai-seo-agent', 'Grow', 'SEO Agent', 'AI SEO audit · structured data · Shopify'),
    ('glitch-grow-ai-ads-agent', 'Grow', 'Ads Agent', 'Cross-store ROAS · Meta · Amazon · Telegram HITL'),
    ('glitch-grow-ai-social-media-agent', 'Grow', 'Social Agent', 'Short-form video · ORM · human guardrails'),
    ('glitch-grow-cod-confirm', 'Grow', 'COD Confirm', 'Voice AI · Hindi + English · RTO reduction'),
    ('glitch-grow-site', 'Grow', 'glitch-grow', 'AI digital marketing for D2C'),
    ('glitch-trade-site', 'Trade', 'glitch-trade', 'AI trading systems · multi-strategy execution'),
    ('glitch-trade-core', 'Trade', 'Core', 'Oracle coordination · shared risk'),
    ('glitch-trade-ouroboros-snake-strategy', 'Trade', 'Ouroboros', '8-bot ensemble · portfolio-aware risk'),
    ('glitch-trade-terciopelo', 'Trade', 'Terciopelo', 'Relative value · mean reversion · news-aware'),
    ('glitch-trade-indian-king-cobra', 'Trade', 'Indian King Cobra', 'Momentum · ML-gated · timeframe-aware'),
    ('glitch-edge-site', 'Edge', 'glitch-edge', 'Betting & sports intelligence'),
    ('glitch-edge-betting-core', 'Edge', 'Core', 'Odds · pricing · staking primitives'),
    ('glitch-edge-nba-engine', 'Edge', 'NBA Engine', 'Pregame intelligence · pricing · lineups'),
    ('glitch-edge-cricket-engine', 'Edge', 'Cricket Engine', 'IPL · PSL · live match-state · paper-first'),
    ('glitch-exec-labs', 'Labs', 'Glitch Executor Labs', 'One builder · Trade · Edge · Grow'),
    ('glitch-executor-labs-portfolio', 'Labs', 'Portfolio', 'One builder · three AI product domains'),
    ('glitch-executor-labs-brand-assets', 'Labs', 'Brand Assets', 'Logos · wordmarks · OG images'),
]

mascot = Image.open(SRC).convert('RGBA')

font_paths = {
    'bold': '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
    'reg': '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
}
F_LINE = ImageFont.truetype(font_paths['bold'], 28)
F_BIG = ImageFont.truetype(font_paths['bold'], 96)
F_BIG_SM = ImageFont.truetype(font_paths['bold'], 72)
F_TAG = ImageFont.truetype(font_paths['reg'], 32)
F_FOOT = ImageFont.truetype(font_paths['reg'], 24)


def make(repo: str, line: str, short: str, tagline: str) -> Path:
    img = Image.new('RGBA', (W, H), BG)

    # Green glow behind mascot
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    cx, cy = 300, 320
    accent = LINE_COLOR[line]
    for r in range(420, 0, -20):
        alpha = max(0, 28 - (420 - r) // 16)
        gd.ellipse([cx - r, cy - r, cx + r, cy + r],
                   fill=(accent[0], accent[1], accent[2], alpha))
    img = Image.alpha_composite(img, glow)

    # Mascot left
    m = mascot.resize((480, 480), Image.LANCZOS)
    img.paste(m, (60, 80), m)

    draw = ImageDraw.Draw(img)
    tx = 600

    # Product line pill
    pill_text = f'GLITCH {line.upper()}'
    pill_w = draw.textlength(pill_text, font=F_LINE) + 32
    draw.rounded_rectangle([tx, 110, tx + pill_w, 160], radius=25,
                           outline=accent, width=2)
    draw.text((tx + 16, 118), pill_text, font=F_LINE, fill=accent)

    # Short name (auto-fit)
    name_font = F_BIG if draw.textlength(short, font=F_BIG) < (W - tx - 60) else F_BIG_SM
    draw.text((tx, 195), short, font=name_font, fill=WHITE)

    # Tagline
    draw.text((tx, 360), tagline, font=F_TAG, fill=MUTED)

    # Footer: repo path + domain
    draw.text((tx, 510), f'github.com/glitch-exec-labs/{repo}', font=F_FOOT, fill=DIM)
    draw.text((tx, 545), 'glitchexecutor.com', font=F_FOOT, fill=DIM)

    out = OUT_DIR / f'{repo}.png'
    img.convert('RGB').save(out, 'PNG', optimize=True)
    return out


if __name__ == '__main__':
    for repo, line, short, tag in REPOS:
        p = make(repo, line, short, tag)
        print(f'{p.name:50s} {os.path.getsize(p)//1024}KB')
    print(f'\n{len(REPOS)} images written to {OUT_DIR}')
