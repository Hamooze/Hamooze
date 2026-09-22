"""Generate the README's vector cards and small orbit diagram. Requires Pillow."""
from pathlib import Path
import base64
import math
import random
from PIL import Image, ImageDraw, ImageFont

ASSETS = Path(__file__).resolve().parents[1] / "assets"
WHITE, BG = "#fdfdfd", "#050505"


def svg(width, height, title, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img">
<title>{title}</title>
{body}
</svg>'''


def launch(name, title, color, symbol):
    body = f'''<path d="M12 90H512V12" fill="none" stroke="{color}" stroke-width="8"/>
<rect x="4" y="4" width="494" height="74" fill="{BG}" stroke="{WHITE}" stroke-width="5"/>
<g transform="translate(24 25)" fill="none" stroke="{color}" stroke-width="3">{symbol}</g>
<text x="75" y="51" fill="{WHITE}" font-family="Arial,Helvetica,sans-serif" font-weight="900" font-size="29">{title}</text>'''
    (ASSETS / f"launch-{name}.svg").write_text(svg(520, 96, title, body))


launch("portfolio", "ENTER MY ORBIT", "#39ff14", '<circle cx="15" cy="16" r="11"/><ellipse cx="15" cy="16" rx="20" ry="6" transform="rotate(-30 15 16)"/>')
launch("email", "START A CONVERSATION", "#00f5d4", '<rect x="0" y="4" width="34" height="24"/><path d="M0 4 17 18 34 4"/>')


def project(name, filename, color, subtitle):
    encoded = base64.b64encode((ASSETS / filename).read_bytes()).decode()
    image = f'<image href="data:image/png;base64,{encoded}" x="32" y="38" width="106" height="106"/>'
    if name == "Barmous":
        mark = f'''<defs><filter id="ink" color-interpolation-filters="sRGB">
<feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  -1 -1 -1 3 0"/>
<feComponentTransfer><feFuncA type="linear" slope="1.5" intercept="-0.1"/></feComponentTransfer>
</filter><mask id="mark" style="mask-type:alpha"><g filter="url(#ink)">{image}</g></mask></defs>
<rect width="560" height="190" fill="{color}" mask="url(#mark)"/>'''
    else:
        mark = image
    body = f'''<path d="M13 182H550V13" fill="none" stroke="{color}" stroke-width="10"/>
<rect x="4" y="4" width="530" height="162" fill="{BG}" stroke="{WHITE}" stroke-width="6"/>
<rect x="28" y="32" width="112" height="112" fill="none" stroke="{WHITE}" stroke-width="4"/>
{mark}
<text x="168" y="94" fill="{color}" font-family="Arial,Helvetica,sans-serif" font-weight="900" font-size="55">{name.upper()}</text>
<text x="169" y="126" fill="{WHITE}" font-family="Courier New,monospace" font-size="20">{subtitle}</text>'''
    (ASSETS / f"orbit-{name.lower()}.svg").write_text(svg(560, 190, f"{name} — {subtitle}", body))


project("Nemu", "nemu-stepped-mark.png", "#8b9cff", "SOFTWARE ENGINEERING")
project("Barmous", "barmous-compliance-logo.png", "#ffe078", "READINESS + GAPS")

# A simple orbital diagram, generated from primitives rather than editing a
# brand asset. GIF works in README images without inline scripts or SVG motion.
palette_colors = [(5, 5, 5), (253, 253, 253), (157, 78, 221), (0, 245, 212),
                  (57, 255, 20), (70, 66, 80), (254, 228, 64)]
palette = [v for color in palette_colors for v in color]
palette += [0] * (768 - len(palette))
rng = random.Random(422)
stars = [(rng.randrange(8, 412), rng.randrange(8, 92)) for _ in range(24)]
frames = []
for frame in range(60):
    image = Image.new("P", (420, 100), 0)
    image.putpalette(palette)
    draw = ImageDraw.Draw(image)
    for x, y in stars:
        draw.point((x, y), fill=5)
    draw.ellipse((16, 30, 164, 70), outline=3, width=1)
    angle = frame * 2 * math.pi / 60
    x, y = 90 + 74 * math.cos(angle), 50 + 20 * math.sin(angle)

    def satellite():
        draw.rectangle((round(x)-4, round(y)-4, round(x)+4, round(y)+4), fill=4, outline=1, width=1)

    if math.sin(angle) < 0:
        satellite()
    draw.ellipse((66, 26, 114, 74), fill=2, outline=1, width=3)
    draw.arc((16, 30, 164, 70), 0, 180, fill=3, width=2)
    if math.sin(angle) >= 0:
        satellite()
    draw.text((184, 31), "OPEN CHANNEL", fill=1, font=ImageFont.load_default(size=23))
    draw.text((185, 61), "LET'S BUILD SOMETHING.", fill=3, font=ImageFont.load_default(size=13))
    frames.append(image)

frames[0].convert("RGB").save(ASSETS / "orbit-signal.png")
frames[0].save(ASSETS / "orbit-signal.gif", save_all=True, append_images=frames[1:],
               duration=100, loop=0, optimize=False, disposal=1)
print("Generated project cards, launch links, and a 6-second orbital loop.")
