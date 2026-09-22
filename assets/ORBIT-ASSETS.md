# Orbit artwork

The `orbit-*` and `launch-*` assets match the space theme at tahayneh.com:
near-black, hard white frames, purple offset type, mint, neon green, and pink.
Artwork is local and self-contained, without remote badge or tracking services.

Regenerate the SVG hero with `python3 scripts/build-hero.py`. Regenerate cards
and the orbital GIF with `python3 scripts/build-orbit-assets.py` (Pillow required).
Then run `node scripts/render-project-cards.cjs` with Sharp available to export
the two compact PNG project cards used in the README. The SVG originals remain
editable; PNG avoids embedding the full-size logo in every README image request.

Nemu and Barmous use the original brand images already in this repository.
The Barmous mark's white background is masked at render time; original source
files remain unchanged. Earlier artwork is retained for recovery.

The orbit GIF has a static PNG alternative for reduced-motion preferences.
README interaction uses native links and details/summary sections.
