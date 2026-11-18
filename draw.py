#!/usr/bin/env python3
"""Render the front page for news-image-20261118: a single image summing
up the world news of Wednesday 18 November 2026.

The page is a newspaper front page ("THE WORLD TODAY") painted with PIL:
masthead, three lead stories, a schematic map strip, six continent
sections and an also-today strip -- 30 stories in all. Everything is
deterministic: running this file twice writes byte-identical PNGs.

Usage: python3 draw.py   (writes entry.png next to this file)
"""

import os

from PIL import Image, ImageDraw, ImageFont

PAGE_W, PAGE_H = 1024, 1024
PAPER = (250, 244, 226)
INK = (22, 22, 22)
MUTED = (70, 70, 70)
RULE = (118, 108, 88)
DEEP_BLUE = (28, 55, 92)
BRICK = (158, 30, 30)
OCEAN = (210, 228, 236)
LAND = (46, 96, 124)

DEJAVU = "/usr/share/fonts/truetype/dejavu/"


def load(kind, pts):
    names = {
        "serif_b": "DejaVuSerif-Bold.ttf",
        "serif": "DejaVuSerif.ttf",
        "sans_b": "DejaVuSans-Bold.ttf",
        "sans": "DejaVuSans.ttf",
    }
    return ImageFont.truetype(DEJAVU + names[kind], pts)


class Page:
    """A drawing surface plus the small helpers a front page needs."""

    def __init__(self):
        self.img = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
        self.d = ImageDraw.Draw(self.img)

    def flow(self, x, y, text, fnt, width_px, step, colour=INK):
        """Lay wrapped text down from (x, y); return the y below it.

        Wrapping is measured, not estimated: words are added while the
        running line still fits width_px according to the real font.
        """
        rows, current = [], ""
        for word in text.split():
            trial = (current + " " + word).strip()
            if self.d.textlength(trial, font=fnt) <= width_px:
                current = trial
            else:
                if current:
                    rows.append(current)
                current = word
        if current:
            rows.append(current)
        for row in rows:
            self.d.text((x, y), row, font=fnt, fill=colour)
            y += step
        return y

    def hline(self, x0, x1, y, colour=INK, width=1):
        self.d.line([(x0, y), (x1, y)], fill=colour, width=width)

    def box(self, x, y, w, h, outline=(96, 96, 96)):
        self.d.rectangle([x, y, x + w, y + h], outline=outline, width=1)


TITLE = "THE WORLD TODAY"
DATE_LINE = "WEDNESDAY, 18 NOVEMBER 2026  \u2022  30 STORIES  \u2022  6 CONTINENTS"

TOP_STORIES = [
    dict(tag="GULF  |  LEAD 1", tint=BRICK,
         head="Hormuz stays open as Gulf war grinds on",
         body="Central Command says shipping \u2018continues to flow\u2019; 900m "
              "barrels passed under escort since May."),
    dict(tag="ASIA  |  LEAD 2", tint=DEEP_BLUE,
         head="Trump meets Marcos in Manila on Asia tour",
         body="A day after his first Quad summit, Trump touts a \u2018Pax "
              "Silica\u2019 AI pact with the Philippines."),
    dict(tag="ECONOMY  |  LEAD 3", tint=(36, 88, 118),
         head="Nvidia beats forecasts without Huang",
         body="Revenue $115.8bn, up 103%, tops estimates; a $130bn Q4 guide "
              "lifts shares 3% after hours."),
]

REGIONS = [
    ("NORTH AMERICA", DEEP_BLUE, [
        ("SpaceX Dragon leaves station with science",
         "The CRS-35 Dragon undocks on Wednesday with 6,300 lb of science, "
         "including a 3D-printed blood vessel."),
        ("SpaceX and China fly back-to-back launches",
         "SpaceX flies classified USSF-317 from Vandenberg on Wednesday "
         "night, hours from China's launch."),
        ("FAA halts new router rollout after chaos",
         "The FAA pauses Juniper router deployment after last week's ground "
         "stop cancelled 18,000-plus flights."),
        ("Xi meets Carney; Canada-China extend trade",
         "China's Xi and Canada's Carney agree wider trade cooperation ahead "
         "of the APEC summit in Shenzhen."),
    ]),
    ("EUROPE", (120, 60, 18), [
        ("Haaland's late penalty sends Norway through",
         "Norway fight back from 2-0 down to beat Denmark 3-2; Portugal top "
         "the group after a 3-2 win in Wales."),
        ("UEFA backs Diallo to challenge Infantino",
         "Europe's governing body backs France's Diallo to stand against "
         "Gianni Infantino in next year's FIFA election."),
        ("UN warns over EU plan to send seekers to Rwanda",
         "Rights chief Volker T\u00fcrk warns about a plan to move people "
         "from five EU states to Rwanda."),
        ("Estonia's Russia border shutdown hits families",
         "Tallinn's decision to close its three crossings from December "
         "strands families."),
    ]),
    ("ASIA", (94, 42, 120), [
        ("Knesset elects Eisenkot ally as speaker",
         "Matan Kahana wins 66-52, replacing a Netanyahu ally; the "
         "opposition now runs the agenda."),
        ("Cyclone Akvan strengthens off India",
         "Akvan becomes a severe cyclonic storm in the Bay of Bengal; "
         "landfall on India's east coast is due on Friday."),
        ("Japan scrambles jets over Russian planes",
         "Two suspected Russian aircraft enter Japanese airspace near "
         "Okinoshima; Tokyo protests, a first since 2024."),
        ("Dhoni retires from IPL; CSK name him mentor",
         "MS Dhoni, 45, ends a 19-year playing career; Chennai keep him "
         "as team mentor for IPL 2027."),
    ]),
    ("AFRICA", (22, 108, 60), [
        ("Ebola toll passes 5,300 in DR Congo",
         "The outbreak tops 11,000 cases, the second-worst on record; Kenya "
         "and Nigeria contained imported cases."),
        ("Mofokeng brace lifts South Africa in Nairobi",
         "South Africa beat Kenya 2-1 to top their AFCON group; Mofokeng "
         "scores twice."),
        ("Tinubu presses for cheaper climate finance",
         "Nigeria's president urges rich nations to cut the cost of climate "
         "finance at COP31."),
        ("Nigeria clears two suspected Ebola cases",
         "Tests on two suspected cases in the north-east come back "
         "negative."),
    ]),
    ("SOUTH AMERICA", (120, 86, 16), [
        ("Colombia mine collapse kills 14",
         "An illegal gold mine collapses in Nari\u00f1o, south-west Colombia; "
         "seven more are injured and the search ends."),
        ("Catholics fall to 55% in Latin America",
         "A 30-year survey finds Catholic identification down from 80% in "
         "1995; Evangelicals now lead in 3 nations."),
        ("US names Guatemalan gang a terror group",
         "Washington designates Guatemala's Los Lorenzanas a foreign "
         "terrorist organisation."),
        ("Sailing's Gold Cup: 40 nations set for Rio",
         "The SSL Gold Cup final line-up is complete; Wednesday's draw sets "
         "the opening ties."),
    ]),
    ("OCEANIA", (126, 50, 82), [
        ("Surfing prodigy, 14, flies home a champion",
         "Leihani Zoric returns a double world champion, the youngest-ever "
         "ISA open women's winner."),
        ("Silver Ferns beat Diamonds 62-50",
         "New Zealand take a 2-0 Constellation Cup lead over Australia in "
         "Christchurch."),
        ("Debate reignites: should NZ join Australia?",
         "A call for New Zealand to become Australia's seventh state draws "
         "wide rejection; ex-PM Palmer rebuts it."),
        ("Australia leads COP31 fossil-fuel draft",
         "Australia's draft urges a fast shift from fossil fuels and $120bn "
         "in aid for poor nations."),
    ]),
]

ALSO_TODAY = ("ALSO TODAY:  Trump, Xi and Putin to hold first trilateral "
              "nuclear talks in Shenzhen on Thursday  \u2022  Fed minutes due on "
              "Wednesday as markets watch for rate signals  \u2022  India "
              "re-elected to the UN telecom council for 2027-30.")
CREDITS = ("Sources, all reported 17-18 Nov 2026: AP, BBC, Reuters, Al "
           "Jazeera, CNN, NASA, IMD, WHO, UN News. Claims are labelled as "
           "claims; Tuesday-evening events are those in Wednesday's editions.")


def paint_lead(page, x, y, w, h, story):
    d = page.d
    page.box(x, y, w, h)
    d.rectangle([x, y, x + w, y + 3], fill=story["tint"])
    d.text((x + 10, y + 12), story["tag"], font=load("sans_b", 12),
           fill=story["tint"])
    y2 = page.flow(x + 10, y + 34, story["head"], load("sans_b", 20),
                   w - 20, 24)
    page.flow(x + 10, y2 + 4, story["body"], load("sans", 13), w - 20, 17,
              colour=MUTED)


def paint_map(page, x, y, w, h):
    d = page.d
    d.rectangle([x, y, x + w, y + h], fill=OCEAN, outline=(96, 96, 96),
                width=1)
    d.text((x + 10, y + 6), "WHERE IT HAPPENED", font=load("sans_b", 13),
           fill=DEEP_BLUE)
    d.text((x + w - 252, y + 6), "30 STORIES ON 6 CONTINENTS",
           font=load("sans_b", 13), fill=DEEP_BLUE)
    # Rough landmasses, kept in the strip's lower half under the titles.
    land = [
        ([(42, 34), (128, 26), (196, 34), (186, 60), (108, 68), (56, 56)],
         (118, 48), "NORTH AMERICA", (98, 72)),
        ([(212, 54), (238, 46), (254, 58), (240, 72), (220, 68)],
         (234, 60), "S. AMERICA", (210, 76)),
        ([(428, 30), (488, 24), (512, 36), (488, 48), (444, 44)],
         (470, 36), "EUROPE", (428, 54)),
        ([(468, 54), (508, 52), (522, 68), (498, 84), (476, 72)],
         (496, 68), "AFRICA", (546, 66)),
        ([(578, 28), (698, 24), (798, 36), (768, 58), (638, 62), (588, 46)],
         (686, 44), "ASIA", (662, 66)),
        ([(812, 60), (852, 54), (870, 66), (838, 76), (818, 70)],
         (842, 66), "OCEANIA", (810, 80)),
    ]
    for shape, (dx, dy), label, (lx, ly) in land:
        pts = [(x + px, y + py) for px, py in shape]
        d.polygon(pts, fill=LAND)
        d.text((x + lx, y + ly), label, font=load("sans_b", 10), fill=INK)
        d.ellipse([x + dx - 4, y + dy - 4, x + dx + 4, y + dy + 4],
                  fill=BRICK, outline=(255, 255, 255), width=1)


def paint_region(page, x, y, w, h, name, tint, stories):
    d = page.d
    page.box(x, y, w, h)
    d.rectangle([x, y, x + w, y + 26], fill=tint)
    d.text((x + 10, y + 5), name, font=load("sans_b", 14),
           fill=(255, 255, 255))
    d.text((x + w - 90, y + 5), "4 STORIES", font=load("sans_b", 12),
           fill=(255, 255, 255))
    cy = y + 34
    for pos, (head, body) in enumerate(stories):
        cy = page.flow(x + 10, cy, head, load("sans_b", 13), w - 20, 14)
        cy = page.flow(x + 10, cy + 1, body, load("sans", 11), w - 20, 12,
                       colour=MUTED)
        cy += 5
        if pos < len(stories) - 1:
            page.hline(x + 10, x + w - 10, cy - 3, colour=(202, 192, 166))


def render():
    page = Page()
    d = page.d
    d.rectangle([16, 14, PAGE_W - 16, PAGE_H - 14], outline=RULE, width=2)

    title = load("serif_b", 58)
    tw = d.textlength(TITLE, font=title)
    d.text(((PAGE_W - tw) / 2, 22), TITLE, font=title, fill=DEEP_BLUE)
    date = load("sans_b", 17)
    dw = d.textlength(DATE_LINE, font=date)
    d.text(((PAGE_W - dw) / 2, 94), DATE_LINE, font=date, fill=BRICK)
    page.hline(28, PAGE_W - 28, 120, width=2)

    col_w, gutter = 316, 12
    for i, story in enumerate(TOP_STORIES):
        paint_lead(page, 26 + i * (col_w + gutter), 130, col_w, 138, story)

    paint_map(page, 26, 278, PAGE_W - 52, 94)

    reg_w, reg_h = 316, 270
    for row in range(2):
        for col in range(3):
            name, tint, stories = REGIONS[row * 3 + col]
            paint_region(page, 26 + col * (reg_w + gutter),
                         382 + row * (reg_h + 10), reg_w, reg_h,
                         name, tint, stories)

    y = 382 + 2 * reg_h + 10 + 6
    y = page.flow(26, y, ALSO_TODAY, load("sans_b", 12), PAGE_W - 52, 16)
    page.hline(26, PAGE_W - 26, y + 4, colour=RULE)
    page.flow(26, y + 10, CREDITS, load("sans", 10), PAGE_W - 52, 13,
              colour=(96, 96, 96))
    return page.img


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    render().save(os.path.join(here, "entry.png"), "PNG", optimize=True)
    print("wrote entry.png")
