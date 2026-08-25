from pathlib import Path

import numpy as np
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(r"C:/Users/2awan/Downloads/Telegram Desktop/photo_2026-08-25_09-31-06.jpg")
FONT_DIR = ROOT / "public" / "fonts"
FONT_PATH = FONT_DIR / "zawanah-hand.ttf"
SPECIMEN_PATH = FONT_DIR / "zawanah-hand-specimen.png"

UPM = 1000
ASCENT = 820
DESCENT = -220
THRESHOLD = 145


def glyph_name(char: str) -> str:
    if char == " ":
        return "space"
    return f"uni{ord(char):04X}"


def component_segments(mask: np.ndarray, min_ink: int = 2, gap: int = 1):
    cols = np.where(mask.sum(axis=0) > min_ink)[0]
    if len(cols) == 0:
        return []

    segments = []
    start = prev = int(cols[0])
    for raw_x in cols[1:]:
        x = int(raw_x)
        if x - prev > gap:
            if prev - start > 2:
                segments.append((start, prev))
            start = x
        prev = x

    if prev - start > 2:
        segments.append((start, prev))
    return segments


def crop_mask(page_mask: np.ndarray, x1: int, x2: int, y1: int, y2: int):
    mask = page_mask[y1 : y2 + 1, x1 : x2 + 1]
    ys, xs = np.where(mask)
    if len(xs) == 0:
        return mask
    pad = 3
    top = max(int(ys.min()) - pad, 0)
    bottom = min(int(ys.max()) + pad, mask.shape[0] - 1)
    left = max(int(xs.min()) - pad, 0)
    right = min(int(xs.max()) + pad, mask.shape[1] - 1)
    return mask[top : bottom + 1, left : right + 1]


def dilate(mask: np.ndarray, iterations: int = 1):
    out = mask.copy()
    for _ in range(iterations):
        padded = np.pad(out, 1, mode="constant", constant_values=False)
        out = (
            padded[1:-1, 1:-1]
            | padded[:-2, 1:-1]
            | padded[2:, 1:-1]
            | padded[1:-1, :-2]
            | padded[1:-1, 2:]
        )
    return out


def glyph_from_mask(mask: np.ndarray, target_height: int, baseline: int = 90):
    if mask.size == 0 or not mask.any():
        pen = TTGlyphPen(None)
        return pen.glyph(), 360, 0

    mask = dilate(mask, 1)
    h, w = mask.shape
    scale = target_height / max(h, 1)
    advance = int(w * scale + 120)
    lsb = 45
    y_offset = baseline

    pen = TTGlyphPen(None)
    for row in range(h):
        cols = np.where(mask[row])[0]
        if len(cols) == 0:
            continue
        start = prev = int(cols[0])
        runs = []
        for raw_x in cols[1:]:
            x = int(raw_x)
            if x != prev + 1:
                runs.append((start, prev))
                start = x
            prev = x
        runs.append((start, prev))

        y_top = y_offset + int((h - row) * scale) + 3
        y_bottom = y_offset + int((h - row - 1) * scale) - 3
        for x1, x2 in runs:
            left = lsb + int(x1 * scale)
            right = lsb + int((x2 + 1) * scale)
            pen.moveTo((left, y_bottom))
            pen.lineTo((right, y_bottom))
            pen.lineTo((right, y_top))
            pen.lineTo((left, y_top))
            pen.closePath()

    return pen.glyph(), advance, lsb


def empty_glyph():
    pen = TTGlyphPen(None)
    return pen.glyph()


def build_font():
    FONT_DIR.mkdir(parents=True, exist_ok=True)
    image = Image.open(SOURCE).convert("L")
    page_mask = np.array(image) < THRESHOLD

    lower_segments = [
        (23, 56),
        (60, 77),
        (90, 112),
        (119, 144),
        (155, 174),
        (183, 202),
        (203, 223),
        (233, 263),
        (268, 282),
        (283, 298),
        (309, 332),
        (343, 357),
        (359, 390),
        (401, 420),
        (431, 448),
        (454, 475),
        (485, 509),
        (516, 538),
        (540, 558),
        (568, 588),
        (597, 620),
        (630, 646),
        (657, 685),
        (692, 716),
        (733, 753),
        (764, 787),
    ]

    upper_segments = component_segments(page_mask[104:140, :], gap=1)
    digit_segments = component_segments(page_mask[171:204, :], gap=6)
    punct_segments = component_segments(page_mask[236:293, :], gap=6)

    rows = {}
    for char, bounds in zip("abcdefghijklmnopqrstuvwxyz", lower_segments):
        rows[char] = (*bounds, 23, 81, 560)

    for char, bounds in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", upper_segments):
        rows[char] = (*bounds, 104, 139, 650)

    for char, bounds in zip("0123456789", digit_segments):
        rows[char] = (*bounds, 171, 203, 620)

    punct_chars = list(".,;:!?'\"()[]{}-/&@#%+")
    for char, bounds in zip(punct_chars, punct_segments):
        rows[char] = (*bounds, 236, 292, 560)

    chars = sorted(rows.keys(), key=ord)
    glyph_order = [".notdef", "space"] + [glyph_name(char) for char in chars]

    glyphs = {".notdef": empty_glyph(), "space": empty_glyph()}
    metrics = {".notdef": (500, 0), "space": (320, 0)}
    cmap = {ord(" "): "space"}

    for char in chars:
        x1, x2, y1, y2, target_height = rows[char]
        mask = crop_mask(page_mask, x1, x2, y1, y2)
        glyph, advance, lsb = glyph_from_mask(mask, target_height)
        name = glyph_name(char)
        glyphs[name] = glyph
        metrics[name] = (advance, lsb)
        cmap[ord(char)] = name

    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(glyph_order)
    fb.setupCharacterMap(cmap)
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=ASCENT, descent=DESCENT)
    fb.setupOS2(
        sTypoAscender=ASCENT,
        sTypoDescender=DESCENT,
        usWinAscent=ASCENT,
        usWinDescent=abs(DESCENT),
    )
    fb.setupNameTable(
        {
            "familyName": "Zawanah Hand",
            "styleName": "Regular",
            "uniqueFontIdentifier": "Zawanah Hand Regular 0.1",
            "fullName": "Zawanah Hand Regular",
            "psName": "ZawanahHand-Regular",
            "version": "Version 0.1",
        }
    )
    fb.setupPost()
    fb.setupMaxp()
    fb.save(FONT_PATH)


def build_specimen():
    font = ImageFont.truetype(str(FONT_PATH), 80)
    canvas = Image.new("RGB", (1200, 520), "#f7f4ed")
    draw = ImageDraw.Draw(canvas)
    lines = [
        "AI Integration",
        "Playbook Part 2",
        "redesign workflows with context",
        "0123456789  !?&@#%",
    ]
    y = 58
    for line in lines:
        draw.text((70, y), line, fill="#26312c", font=font)
        y += 104
    canvas.save(SPECIMEN_PATH)


if __name__ == "__main__":
    build_font()
    build_specimen()
    print(FONT_PATH)
    print(SPECIMEN_PATH)
