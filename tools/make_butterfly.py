#!/usr/bin/env python3
"""Draw butterfly.jpg, the default input image for deftones.pde.

The outline is the main loop of Temple H. Fay's butterfly curve,
r = e^sin(t) - 2 cos(4t), for one turn of t. Without Fay's extra
sin^5 term the curve is mirror-symmetric.
Needs Pillow (pip install pillow). Run from the sketch folder:
python3 tools/make_butterfly.py
"""
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

SIZE = 1000
OUT = Path(__file__).resolve().parent.parent / "butterfly.jpg"


def butterfly_points(scale, cx, cy, steps=2000):
    pts = []
    for k in range(steps + 1):
        t = 2 * math.pi * k / steps
        r = math.exp(math.sin(t)) - 2 * math.cos(4 * t)
        pts.append((cx + scale * r * math.cos(t), cy - scale * r * math.sin(t)))
    return pts


def main():
    img = Image.new("RGB", (SIZE, SIZE), (18, 22, 40))
    draw = ImageDraw.Draw(img)

    # Soft background rings.
    for i in range(12, 0, -1):
        rad = i * 42
        shade = 18 + i * 3
        draw.ellipse((SIZE / 2 - rad, SIZE / 2 - rad, SIZE / 2 + rad, SIZE / 2 + rad),
                     fill=(shade, shade + 4, shade + 22))

    cx, cy, scale = SIZE / 2, SIZE / 2 + 120, 95
    pts = butterfly_points(scale, cx, cy)

    # Wings: the curve filled, an inner copy in a second colour, then the outline.
    draw.polygon(pts, fill=(230, 150, 40))
    draw.polygon(butterfly_points(scale * 0.7, cx, cy), fill=(200, 70, 40))
    draw.line(pts, fill=(255, 235, 180), width=6)

    # Veins: dark lines from the body out to the wing edge.
    for k in range(0, len(pts), 40):
        draw.line([(cx, cy), pts[k]], fill=(70, 25, 20), width=3)

    # Small pale scales scattered over the wings, from a fixed seed so the
    # image is the same every time.
    wing = Image.new("L", (SIZE, SIZE), 0)
    ImageDraw.Draw(wing).polygon(pts, fill=255)
    rng = random.Random(7)
    for _ in range(900):
        x, y = rng.uniform(0, SIZE), rng.uniform(0, SIZE)
        if wing.getpixel((int(x), int(y))):
            r = rng.uniform(3, 7)
            draw.ellipse((x - r, y - r, x + r, y + r), fill=(255, 220, 150))

    # Stars in the background.
    for _ in range(160):
        x, y = rng.uniform(0, SIZE), rng.uniform(0, SIZE)
        if not wing.getpixel((int(x), int(y))):
            r = rng.uniform(2, 4)
            draw.ellipse((x - r, y - r, x + r, y + r), fill=(220, 225, 255))

    # Spots on each wing.
    for sx, sy, r in [(-190, -170, 46), (190, -170, 46), (-120, 150, 30), (120, 150, 30)]:
        draw.ellipse((cx + sx - r, cy + sy - r, cx + sx + r, cy + sy + r),
                     fill=(30, 30, 60), outline=(255, 255, 255), width=6)

    # Body and antennae.
    draw.ellipse((cx - 16, cy - 190, cx + 16, cy + 170), fill=(25, 20, 30))
    draw.line([(cx - 4, cy - 185), (cx - 70, cy - 330)], fill=(240, 240, 240), width=6)
    draw.line([(cx + 4, cy - 185), (cx + 70, cy - 330)], fill=(240, 240, 240), width=6)
    for ex in (-70, 70):
        draw.ellipse((cx + ex - 12, cy - 342, cx + ex + 12, cy - 318), fill=(240, 240, 240))

    img = img.filter(ImageFilter.SMOOTH)
    img.save(OUT, quality=90)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
