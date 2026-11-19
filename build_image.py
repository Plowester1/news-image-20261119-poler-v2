"""Render entry.png: a 1024x1024 newspaper-style summary of 19 Nov 2026 world news."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (248, 245, 238)
INK = (20, 20, 20)
ACCENT = (140, 30, 30)
RULE = (60, 60, 60)
HAIRLINE = (150, 145, 135)

FONT_DIR = "/home/hatch/workspace/makefun/scratch/ni19-rebuild/fonts"
SERIF_BOLD = f"{FONT_DIR}/DejaVuSerif-Bold.ttf"
SANS = f"{FONT_DIR}/DejaVuSans.ttf"
SANS_BOLD = f"{FONT_DIR}/DejaVuSans-Bold.ttf"

HERO = (
    "DIPLOMACY / SHENZHEN",
    "Trump, Xi and Putin meet in Shenzhen as APEC opens",
    "Unprecedented trilateral talks on nuclear arms control and the wars in Ukraine "
    "and Iran; the New START treaty has expired.",
)

GRID = [
    ("NORTH KOREA", "IAEA warns N. Korea expanding uranium enrichment at Yongbyon",
     "A Yongbyon enrichment extension was completed by late October, with continued reactor operations."),
    ("MYANMAR / ICJ", "World Court delivers judgment in Rohingya genocide case",
     "The Gambia v. Myanmar at the ICJ; hundreds of thousands of Rohingya remain displaced."),
    ("BANGLADESH", "Yunus's ancestral home set ablaze amid protests",
     "The former interim leader's ancestral home was torched amid Awami League-linked protests."),
    ("UKRAINE / ODESA", "Russian strike on Odesa kills 4, wounds 13",
     "At least four killed and 13 injured in a Russian strike on Odesa."),
    ("UKRAINE / KERCH", "Ukraine hits Kerch Bridge again, rail traffic disrupted",
     "Another attack disrupted rail traffic across the bridge linking Russia to Crimea."),
    ("UKRAINE / ZELENSKYY", "Zelenskyy: no Ukraine deal without Ukraine",
     "Kyiv insists decisions on Ukraine's future cannot be made without Ukraine."),
    ("EUROPE / UKRAINE AID", "European Commission proposes \u20ac45bn loan to Ukraine",
     "Brussels proposes a new 45 billion euro loan for Ukraine."),
    ("EUROPE / METHANE", "EU moves to delay methane rules under US pressure",
     "EU governments move to extend methane-rule delays after US pressure."),
    ("EU / CYBER", "Cyberattack hits European Commission",
     "A cyberattack affected the Commission; cause and actor not established."),
    ("FRANCE / VAN GOGH", "Van Gogh sells for record $190.4M",
     "A record sale for the artist, after controversy over Nazi-era ownership."),
    ("IRAN / HORMUZ", "Three tankers reported ablaze in Strait of Hormuz",
     "Three oil tankers reported on fire; causes not independently established."),
    ("SAUDI / HOUTHIS", "Houthi missile intercepted over Riyadh",
     "The Saudi-led coalition intercepted a ballistic missile over the capital."),
    ("GAZA", "Israel strikes Nuseirat in central Gaza",
     "Operations in Nuseirat amid ceasefire-violation allegations."),
    ("LEBANON", "Lebanon charges 5 Hezbollah members; US sanctions financing",
     "Five charged over recruitment and weapons; Washington targets financing networks."),
    ("US / ESPIONAGE", "Russian national charged over spying on Palantir workers",
     "Charged over alleged intelligence activity targeting Palantir employees."),
    ("US / AI", "Trump slams 'globalist' AI regulation in China",
     "Criticism of international AI regulation amid US\u2013China tech competition."),
    ("US / IMMIGRATION", "Trump asks Supreme Court on Venezuelan migrant protections",
     "Another Supreme Court request over protections for Venezuelan migrants."),
    ("SUDAN", "RSF commander defects to Sudanese Armed Forces",
     "An RSF commander and accompanying personnel defected to the army."),
    ("SENEGAL", "Dozens missing as migrant boat sinks off Senegal",
     "A boat carrying about 100 migrants sank, leaving dozens missing."),
    ("FIJI", "Fiji declares state of disaster amid El Ni\u00f1o drought",
     "El Ni\u00f1o-linked drought threatens water supplies across Fiji."),
    ("INDIA / CYCLONE", "72,000 evacuated as Cyclone Akvan nears Andhra coast",
     "Nearly 72,000 evacuated as the cyclone threatens coastal communities."),
]


def load_font(path, size):
    return ImageFont.truetype(path, size)


def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_masthead(draw, fonts):
    serif = fonts["masthead"]
    sans = fonts["date"]
    title = "THE WORLD IN ONE DAY"
    tw = draw.textlength(title, font=serif)
    x = (W - tw) / 2
    draw.line([(40, 26), (W - 40, 26)], fill=RULE, width=2)
    draw.text((x, 34), title, font=serif, fill=INK)
    date = "THURSDAY, 19 NOVEMBER 2026"
    dw = draw.textlength(date, font=sans)
    draw.text(((W - dw) / 2, 96), date, font=sans, fill=INK)
    draw.line([(40, 122), (W - 40, 122)], fill=RULE, width=2)
    return 132


def draw_hero(draw, fonts, y0):
    cat_font, head_font, sum_font = fonts["cat"], fonts["hero_head"], fonts["hero_sum"]
    pad = 28
    x0, x1 = pad, W - pad
    w = x1 - x0
    cat = HERO[0]
    draw.text((x0, y0), cat, font=cat_font, fill=ACCENT)
    y = y0 + 20
    for line in wrap_text(draw, HERO[1], head_font, w):
        draw.text((x0, y), line, font=head_font, fill=INK)
        y += 40
    y += 2
    for line in wrap_text(draw, HERO[2], sum_font, w)[:2]:
        draw.text((x0, y), line, font=sum_font, fill=INK)
        y += 19
    y += 6
    draw.line([(x0, y), (x1, y)], fill=RULE, width=1)
    return y + 8


def draw_card(draw, fonts, x, y, w, h, story):
    cat_font, head_font, sum_font = fonts["cat"], fonts["head"], fonts["sum"]
    pad = 10
    tx, tw = x + pad, w - 2 * pad
    ty = y + 8
    draw.text((tx, ty), story[0], font=cat_font, fill=ACCENT)
    ty += 16
    for line in wrap_text(draw, story[1], head_font, tw)[:2]:
        draw.text((tx, ty), line, font=head_font, fill=INK)
        ty += 19
    ty += 1
    summary = wrap_text(draw, story[2], sum_font, tw)[0]
    draw.text((tx, ty), summary, font=sum_font, fill=INK)


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    fonts = {
        "masthead": load_font(SERIF_BOLD, 52),
        "date": load_font(SANS_BOLD, 20),
        "cat": load_font(SANS_BOLD, 12),
        "hero_head": load_font(SERIF_BOLD, 34),
        "hero_sum": load_font(SANS, 15),
        "head": load_font(SANS_BOLD, 16),
        "sum": load_font(SANS, 12),
    }
    y = draw_masthead(draw, fonts)
    y = draw_hero(draw, fonts, y)

    cols, rows = 3, 7
    margin = 28
    gap = 14
    grid_w = W - 2 * margin
    grid_h = H - y - 20
    cw = (grid_w - gap * (cols - 1)) / cols
    ch = (grid_h - gap * (rows - 1)) / rows
    for i, story in enumerate(GRID):
        r, c = divmod(i, cols)
        x = margin + c * (cw + gap)
        cy = y + r * (ch + gap)
        draw.rectangle([x, cy, x + cw, cy + ch], outline=HAIRLINE, width=1)
        draw_card(draw, fonts, x, cy, cw, ch, story)
        if c < cols - 1:
            draw.line([(x + cw + gap / 2, cy + 6), (x + cw + gap / 2, cy + ch - 6)],
                      fill=HAIRLINE, width=1)

    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
