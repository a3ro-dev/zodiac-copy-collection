from pathlib import Path
import json
import math
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageOps
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "diffusion"
OUT.mkdir(parents=True, exist_ok=True)
GEN = OUT / "source-art"
MM_TO_PX = 300 / 25.4
W, H = round(56 * MM_TO_PX), round(156 * MM_TO_PX)
TRIM = 3 * MM_TO_PX
GOLD = (218, 189, 137)
IVORY = (241, 232, 211)
FONT_TITLE = r"C:\Windows\Fonts\georgia.ttf"
FONT_BODY = r"C:\Windows\Fonts\georgiai.ttf"

DESIGNS = [
    ("aries", "The First Spark", "exec-154d3c1f-c8c7-4b05-9fcf-e553ff013457.png"),
    ("cancer", "The Silver Tide", "exec-42b6bf19-2b50-49a4-b508-94f6ca4086a3.png"),
    ("leo", "The Golden Hour", "exec-29e34362-fa9f-4535-a2c5-cdc6367a7afb.png"),
    ("scorpio", "The Red Moon", "exec-7cb2adc9-5f46-4805-9875-8af2ad24e5f2.png"),
    ("pisces", "The Dream Current", "exec-d4c7edf7-00a6-4766-b847-c494f28b9379.png"),
]

def centered(draw, y, line, font, color):
    box = draw.textbbox((0, 0), line, font=font)
    draw.text(((W - (box[2] - box[0])) / 2, y), line, font=font, fill=color)

def wrap_to_width(draw, sentence, font, max_width):
    words = sentence.split()
    lines, line = [], ""
    for word in words:
        test = f"{line} {word}".strip()
        if line and draw.textlength(test, font=font) > max_width:
            lines.append(line)
            line = word
        else:
            line = test
    if line:
        lines.append(line)
    return lines

manifest = []
previews = []
for sign, title, source in DESIGNS:
    data = json.loads((ROOT.parent / "zodiac-copy-collection" / sign / "matter.json").read_text(encoding="utf-8"))
    quote = data["matter"]["poetic_lines"][0]
    artwork = Image.open(GEN / source).convert("RGB")
    artwork = ImageOps.fit(artwork, (W, H), method=Image.Resampling.LANCZOS, centering=(0.5, 0.47))
    draw = ImageDraw.Draw(artwork)
    title_font = ImageFont.truetype(FONT_TITLE, 61)
    sign_font = ImageFont.truetype(FONT_TITLE, 32)
    body_font = ImageFont.truetype(FONT_BODY, 29)
    # A quiet, consistent type panel over the generated dark lower field.
    rule_y = round(H * 0.795)
    draw.line((W * .18, rule_y, W * .82, rule_y), fill=GOLD, width=2)
    centered(draw, rule_y + 26, sign.upper(), sign_font, GOLD)
    centered(draw, rule_y + 80, title, title_font, IVORY)
    lines = wrap_to_width(draw, quote, body_font, W - 2 * (TRIM + 51))
    start = rule_y + 177
    for n, line in enumerate(lines):
        centered(draw, start + n * 42, line, body_font, IVORY)
    png = OUT / f"{sign}-front-bleed-300dpi.png"
    artwork.save(png, dpi=(300, 300), optimize=True)
    pdf = OUT / f"{sign}-front-print.pdf"
    c = canvas.Canvas(str(pdf), pagesize=(56 / 25.4 * 72, 156 / 25.4 * 72), pageCompression=1)
    c.drawImage(ImageReader(artwork), 0, 0, width=56 / 25.4 * 72, height=156 / 25.4 * 72)
    c.setTitle(f"{sign.title()} bookmark front — 50 × 150 mm + 3 mm bleed")
    c.showPage()
    c.save()
    reader = PdfReader(str(pdf))
    writer = PdfWriter()
    page = reader.pages[0]
    pt = 72 / 25.4
    page.trimbox = RectangleObject((3 * pt, 3 * pt, 53 * pt, 153 * pt))
    page.bleedbox = RectangleObject((0, 0, 56 * pt, 156 * pt))
    writer.add_page(page)
    with pdf.open("wb") as output:
        writer.write(output)
    previews.append(artwork)
    manifest.append({"sign":sign,"title":title,"copy":quote,"method":"diffusion artwork with typeset copy","source_art":source,"png":png.name,"pdf":pdf.name,"bleed_size_mm":[56,156],"trim_size_mm":[50,150],"bleed_mm":3,"raster_dpi":300})

thumb_w = 220
thumb_h = round(thumb_w * H / W)
gap = 20
sheet = Image.new("RGB", (gap + 5 * (thumb_w + gap), thumb_h + 2 * gap), "#e9e4da")
for i, im in enumerate(previews):
    sheet.paste(im.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS), (gap + i * (thumb_w + gap), gap))
sheet.save(OUT / "contact-sheet.jpg", quality=92)
(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
