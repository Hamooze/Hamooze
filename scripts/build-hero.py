"""Build self-contained GitHub profile artwork using only SVG primitives."""
from pathlib import Path
import random

OUT = Path(__file__).resolve().parents[1] / "assets"

def stars(w, h, count):
    rng = random.Random(422)
    items = []
    for _ in range(count):
        x, y = rng.randrange(35, w - 35), rng.randrange(30, h - 30)
        r = rng.choice([1, 1, 1.5, 2])
        items.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fdfdfd" opacity="{rng.choice([.12,.18,.24,.4])}"/>')
    return '\n'.join(items)

def planet(x, y, scale=1):
    return f'''<g transform="translate({x} {y}) scale({scale}) rotate(-24)">
      <ellipse rx="167" ry="51" fill="none" stroke="#00f5d4" stroke-width="8"/>
      <circle r="94" fill="#39ff14" stroke="#fdfdfd" stroke-width="9"/>
      <path d="M-79-47A92 92 0 0 1 82 44" fill="none" stroke="#050505" stroke-opacity=".16" stroke-width="16"/>
      <path d="M-167 0A167 51 0 0 0 167 0" fill="none" stroke="#050505" stroke-width="21"/>
      <path d="M-167 0A167 51 0 0 0 167 0" fill="none" stroke="#fdfdfd" stroke-width="9"/>
      <path d="M-150 23A167 51 0 0 0 104 40" fill="none" stroke="#00f5d4" stroke-width="8"/>
    </g>'''

def spark(x,y,fill='#fee440',scale=1):
    return f'<g transform="translate({x} {y}) scale({scale})"><path d="M0-12 3-3 12 0 3 3 0 12-3 3-12 0-3-3Z" fill="{fill}"/></g>'

def header(w,h,description):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
  <title id="title">Hamza Tahayneh — Welcome to my orbit.</title>
  <desc id="desc">{description}</desc>
  <defs><clipPath id="artboard"><rect width="{w}" height="{h}"/></clipPath></defs>
  <g clip-path="url(#artboard)">
  <rect width="{w}" height="{h}" fill="#050505"/>
  <g aria-hidden="true">{stars(w,h,80 if w>700 else 60)}</g>
'''

desktop = header(1200,480,'A neon green ringed planet and starfield frame Hamza Tahayneh, software, networks, and cybersecurity. UAE / Jordan.') + f'''
  <g fill="none" aria-hidden="true">
    <ellipse cx="1054" cy="154" rx="289" ry="268" stroke="#ff007f" stroke-opacity=".28" stroke-width="2" stroke-dasharray="7 7"/>
    <ellipse cx="1036" cy="184" rx="327" ry="306" stroke="#9d4edd" stroke-opacity=".22" stroke-width="2"/>
    <path d="M758 453 1168 50" stroke="#fdfdfd" stroke-opacity=".07" stroke-width="2"/>
  </g>
  <path d="M39 454H1177V40" fill="none" stroke="#fdfdfd" stroke-width="9"/>
  <rect x="25" y="25" width="1138" height="414" fill="none" stroke="#fdfdfd" stroke-width="5"/>
  <g font-family="'Courier New',Courier,monospace" font-weight="700">
    <path d="M61 59H450V111H99L82 128V111H61Z" fill="#fdfdfd"/>
    <text x="78" y="93" fill="#050505" font-size="23">Welcome to my orbit.</text>
    <circle cx="942" cy="79" r="5" fill="#39ff14"/>
    <text x="961" y="85" fill="#fdfdfd" font-size="18" letter-spacing="1">UAE / JORDAN</text>
  </g>
  <g font-family="'Arial Black',Arial,Helvetica,sans-serif" font-size="100" font-weight="900" letter-spacing="-3">
    <g fill="#9d4edd" transform="translate(7 7)"><text x="58" y="227">HAMZA</text><text x="56" y="330">TAHAYNEH</text></g>
    <g fill="#fdfdfd"><text x="58" y="227">HAMZA</text><text x="56" y="330">TAHAYNEH</text></g>
  </g>
  <text x="62" y="389" fill="#00f5d4" font-family="'Courier New',Courier,monospace" font-size="21" font-weight="700" letter-spacing=".4">SOFTWARE / NETWORKS / CYBERSECURITY</text>
  <g aria-hidden="true">
    {planet(957,262)}
    <g transform="translate(799 143) rotate(12)"><rect x="-15" y="-15" width="30" height="30" fill="#ff007f" stroke="#fdfdfd" stroke-width="5"/></g>
    {spark(1097,384)}
    {spark(822,363,'#00f5d4',.75)}
    <path d="M1117 166h20m-10-10v20" stroke="#9d4edd" stroke-width="5"/>
    <path d="M745 54h17m-8.5-8.5v17" stroke="#00f5d4" stroke-width="3"/>
  </g>
  </g>
</svg>
'''

mobile = header(640,650,'A neon green ringed planet and starfield frame Hamza Tahayneh, software, networks, and cybersecurity. UAE / Jordan.') + f'''
  <g fill="none" aria-hidden="true">
    <ellipse cx="520" cy="506" rx="245" ry="262" stroke="#ff007f" stroke-opacity=".28" stroke-width="2" stroke-dasharray="7 7"/>
    <ellipse cx="522" cy="498" rx="277" ry="297" stroke="#9d4edd" stroke-opacity=".22" stroke-width="2"/>
  </g>
  <path d="M27 636H628V28" fill="none" stroke="#fdfdfd" stroke-width="8"/>
  <rect x="16" y="16" width="598" height="606" fill="none" stroke="#fdfdfd" stroke-width="4"/>
  <g font-family="'Courier New',Courier,monospace" font-weight="700">
    <path d="M44 48H433V100H82L65 117V100H44Z" fill="#fdfdfd"/>
    <text x="61" y="82" fill="#050505" font-size="23">Welcome to my orbit.</text>
  </g>
  <g font-family="'Arial Black',Arial,Helvetica,sans-serif" font-size="85" font-weight="900" letter-spacing="-3">
    <g fill="#9d4edd" transform="translate(6 6)"><text x="40" y="206">HAMZA</text><text x="38" y="294">TAHAYNEH</text></g>
    <g fill="#fdfdfd"><text x="40" y="206">HAMZA</text><text x="38" y="294">TAHAYNEH</text></g>
  </g>
  <g fill="#00f5d4" font-family="'Courier New',Courier,monospace" font-size="22" font-weight="700" letter-spacing=".5">
    <text x="44" y="344">SOFTWARE / NETWORKS /</text>
    <text x="44" y="376">CYBERSECURITY</text>
  </g>
  <g aria-hidden="true">
    {planet(445,502,.79)}
    <g transform="translate(185 478) rotate(12)"><rect x="-14" y="-14" width="28" height="28" fill="#ff007f" stroke="#fdfdfd" stroke-width="5"/></g>
    {spark(566,400)}
    {spark(276,563,'#00f5d4',.8)}
    <path d="M88 432h17m-8.5-8.5v17" stroke="#9d4edd" stroke-width="4"/>
  </g>
  <circle cx="49" cy="580" r="5" fill="#39ff14"/>
  <text x="64" y="587" fill="#fdfdfd" font-family="'Courier New',Courier,monospace" font-weight="700" font-size="18" letter-spacing="1">UAE / JORDAN</text>
  </g>
</svg>
'''

for filename,svg in [('orbit-hero.svg',desktop),('orbit-hero-mobile.svg',mobile)]:
    (OUT/filename).write_text(svg)
    print(OUT/filename)
