# draw.py — renders the news-image-20261118 front page (1024x1024 PNG) with PIL.
# One image that sums up the world's news of Wednesday 18 November 2026:
# 3 lead stories, a small world map, 6 continent sections x 4 stories,
# and 3 "also today" briefs = 30 verified stories in total.
# Every headline and figure below was checked against reporting dated
# 17-18 November 2026 (AP, BBC, Reuters, Al Jazeera, CNN, NASA, IMD, WHO,
# UN News and others; full list of sources is in README.md). Nothing here
# is invented: where a report was a claim, the label says so ("Tehran
# claims...", "Iran says..."). Several stories broke on Tuesday evening
# and were first reported in Wednesday's editions (the Knesset vote, the
# Nvidia results, the Nations League finals, Dhoni's retirement); they are
# the stories in the world's Wednesday 18 November front pages, and the
# README records the date basis of each one. Events scheduled for
# Wednesday itself (the Marcos meeting, the Dragon undocking, the SSL
# draw, the Zoric homecoming) are stated as Wednesday events.
# Run: python3 draw.py  ->  writes entry.png next to this file.
# Deterministic: fixed fonts, fixed layout, no randomness, no network.

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (251, 246, 233)
INK = (26, 26, 26)
NAVY = (20, 50, 79)
RED = (179, 39, 30)
TEAL = (46, 107, 138)
MAP_BG = (220, 233, 242)
MAP_LAND = (46, 107, 138)
GREY = (90, 90, 90)
RULE = (180, 170, 150)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


F_TITLE = font(SERIF_B, 56)
F_DATE = font(SANS_B, 15)
F_KICK = font(SANS_B, 11)
F_LEAD_H = font(SANS_B, 16)
F_LEAD_S = font(SANS, 12)
F_MAP_T = font(SANS_B, 13)
F_MAP_L = font(SANS_B, 10)
F_SEC = font(SANS_B, 13)
F_HEAD = font(SANS_B, 12)
F_SUB = font(SANS, 10)
F_FOOT = font(SANS, 11)
F_SRC = font(SANS, 9)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit `width` pixels."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


LEADS = [
    ("GULF  |  LEAD 1", RED,
     "US says Hormuz stays open as Gulf war grinds on",
     "US Central Command says shipping 'continues to flow' and 900m barrels passed under escort since May; Tehran insists the strait stays shut."),
    ("ASIA  |  LEAD 2", NAVY,
     "Trump meets Marcos in Manila on Asia tour",
     "A day after his first Quad summit, Trump touts a 'Pax Silica' AI pact with the Philippines; on Thursday he joins Xi and Putin in Shenzhen."),
    ("ECONOMY  |  LEAD 3", TEAL,
     "Nvidia beats forecasts in first results without Huang",
     "Revenue $115.8bn, up 103%, tops estimates; a $130bn Q4 guide lifts shares 3% after hours under interim chief Colette Kress."),
]

# (continent, colour, [(headline, sub), ...]) — 4 stories each, 24 total.
SECTIONS = [
    ("NORTH AMERICA", NAVY, [
        ("SpaceX Dragon leaves station with science",
         "The CRS-35 Dragon undocks on Wednesday with 6,300 lb of science, including a 3D-printed blood vessel."),
        ("SpaceX and China fly back-to-back launches",
         "SpaceX flies classified USSF-317 from Vandenberg on Wednesday night, hours after China's launch."),
        ("FAA halts new router rollout after chaos",
         "The FAA pauses Juniper router deployment after last week's ground stop cancelled 18,000-plus flights."),
        ("Xi meets Carney; Canada-China extend trade",
         "China's Xi and Canada's Carney agree wider trade cooperation ahead of the APEC summit in Shenzhen."),
    ]),
    ("EUROPE", (122, 62, 20), [
        ("Haaland's late penalty sends Norway through",
         "Norway fight back from 2-0 down to beat Denmark 3-2; Portugal top the group after a 3-2 win in Wales."),
        ("UEFA backs Diallo to challenge Infantino",
         "Europe's governing body backs France's Diallo to stand against Gianni Infantino in next year's FIFA election."),
        ("UN warns over EU plan to send seekers to Rwanda",
         "Rights chief Volker Türk raises concerns about a proposal to transfer people from five EU states to Rwanda."),
        ("Estonia's Russia border shutdown hits families",
         "Tallinn's decision to close its three crossings from December strands families on both sides, Reuters reports."),
    ]),
    ("ASIA", (90, 40, 110), [
        ("Knesset elects Eisenkot ally as speaker",
         "Matan Kahana wins 66-52, replacing a Netanyahu ally and giving the opposition control of Israel's legislative agenda."),
        ("Cyclone Akvan strengthens off India",
         "Akvan becomes a severe cyclonic storm in the Bay of Bengal; landfall on India's east coast is due on Friday."),
        ("Japan scrambles jets over Russian planes",
         "Two suspected Russian aircraft enter Japanese airspace near Okinoshima; Tokyo protests, a first since 2024."),
        ("Dhoni retires from IPL; CSK name him mentor",
         "MS Dhoni, 45, ends a 19-year playing career; Chennai keep him as team mentor for IPL 2027."),
    ]),
    ("AFRICA", (30, 110, 60), [
        ("Ebola toll passes 5,300 in DR Congo",
         "The outbreak tops 11,000 cases, the second-worst on record; Kenya and Nigeria contained imported cases."),
        ("Mofokeng brace lifts South Africa in Nairobi",
         "South Africa beat Kenya 2-1 to top their AFCON qualifying group; Mofokeng scores twice in the second half."),
        ("Tinubu presses for cheaper climate cash",
         "Nigeria's president urges rich nations to cut the cost of climate finance as COP31's high-level segment continues."),
        ("Nigeria clears two suspected Ebola cases",
         "Tests on two suspected cases in the north-east come back negative; no secondary infections were found."),
    ]),
    ("SOUTH AMERICA", (150, 90, 10), [
        ("Colombia mine collapse kills 14",
         "An illegal gold mine collapses in Narino, south-west Colombia; seven more are injured and the search ends."),
        ("Catholics fall to 55% in Latin America",
         "A 30-year survey finds Catholic identification down from 80% in 1995; Evangelicals now lead in three nations."),
        ("US names Guatemalan gang a terror group",
         "Washington designates Los Lorenzanas a foreign terrorist organisation as Guatemala fights drug violence."),
        ("Sailing's Gold Cup: 40 nations set for Rio",
         "The SSL Gold Cup final line-up is complete; the draw for the opening ties takes place on Wednesday."),
    ]),
    ("OCEANIA", (150, 60, 90), [
        ("Surfing prodigy, 14, flies home a champion",
         "Leihani Zoric returns to the Gold Coast a double world champion, the youngest-ever ISA open women's winner."),
        ("Silver Ferns beat Diamonds 62-50",
         "New Zealand take a 2-0 Constellation Cup lead over Australia in Christchurch; the series moves to Sydney."),
        ("Debate reignites: should NZ join Australia?",
         "A call for New Zealand to become Australia's seventh state draws wide rejection; ex-PM Palmer rebuts it."),
        ("Australia leads COP31 fossil-fuel draft",
         "Australia's draft deal urges an immediate shift from fossil fuels and $120bn in adaptation aid for poor nations."),
    ]),
]

ALSO = ("ALSO TODAY:  Trump, Xi and Putin to hold first trilateral nuclear talks in Shenzhen on Thursday  •  "
        "Fed minutes due on Wednesday as markets watch for rate signals  •  "
        "India re-elected to the UN telecom council for 2027-30.")
SOURCES = ("Sources, all reported 17-18 Nov 2026: AP, BBC, Reuters, Al Jazeera, CNN, NASA, IMD, WHO, UN News. "
           "Claims are labelled as claims; Tuesday-evening events are those in Wednesday's editions.")


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    d.text((W // 2, 14), "THE WORLD TODAY", font=F_TITLE, fill=NAVY, anchor="ma")
    d.text((W // 2, 76), "WEDNESDAY, 18 NOVEMBER 2026  •  30 STORIES  •  6 CONTINENTS",
           font=F_DATE, fill=RED, anchor="ma")
    d.line([(24, 100), (1000, 100)], fill=RULE, width=2)

    # ---- Lead row: 3 big stories ---------------------------------------
    lx, ly, lw, lh, gap = 24, 112, 314, 138, 13
    for i, (kick, colour, head, sub) in enumerate(LEADS):
        x = lx + i * (lw + gap)
        d.rectangle([x, ly, x + lw, ly + lh], fill=(255, 255, 255),
                    outline=RULE, width=1)
        d.rectangle([x, ly, x + lw, ly + 5], fill=colour)
        d.text((x + 12, ly + 13), kick, font=F_KICK, fill=colour)
        for j, line in enumerate(wrap(d, head, F_LEAD_H, lw - 24)):
            d.text((x + 12, ly + 34 + j * 19), line, font=F_LEAD_H, fill=INK)
        for j, line in enumerate(wrap(d, sub, F_LEAD_S, lw - 24)[:3]):
            d.text((x + 12, ly + 76 + j * 15), line, font=F_LEAD_S, fill=(60, 60, 60))

    # ---- World map strip -------------------------------------------------
    mx, my, mw, mh = 24, 262, 976, 108
    d.rectangle([mx, my, mx + mw, my + mh], fill=MAP_BG, outline=RULE, width=1)
    d.text((mx + 12, my + 7), "WHERE IT HAPPENED", font=F_MAP_T, fill=NAVY)
    d.text((mx + mw - 12, my + 7), "30 STORIES ON 6 CONTINENTS",
           font=F_MAP_T, fill=NAVY, anchor="ra")
    # Simplified continent shapes (schematic, equirectangular-ish).
    continents = {
        "N. AMERICA": ([(70, 312), (150, 300), (235, 306), (255, 326), (215, 348),
                        (150, 358), (95, 346), (58, 324)], (150, 322)),
        "S. AMERICA": ([(255, 336), (295, 338), (302, 362), (278, 368), (258, 352)],
                        (278, 350)),
        "EUROPE": ([(468, 300), (520, 296), (542, 308), (520, 320), (480, 318)],
                    (505, 306)),
        "AFRICA": ([(480, 324), (532, 322), (548, 346), (522, 368), (496, 354)],
                    (514, 344)),
        "ASIA": ([(548, 298), (705, 292), (765, 306), (742, 336), (682, 346),
                  (600, 342), (556, 322)], (655, 318)),
        "OCEANIA": ([(782, 346), (832, 342), (852, 356), (802, 364)], (815, 350)),
    }
    for name, (poly, dot) in continents.items():
        d.polygon(poly, fill=MAP_LAND)
        d.ellipse([dot[0] - 4, dot[1] - 4, dot[0] + 4, dot[1] + 4],
                  fill=RED, outline=(255, 255, 255), width=1)
    d.text((58, 360), "NORTH AMERICA", font=F_MAP_L, fill=NAVY)
    d.text((306, 350), "S. AMERICA", font=F_MAP_L, fill=NAVY)
    d.text((452, 288), "EUROPE", font=F_MAP_L, fill=NAVY)
    d.text((418, 344), "AFRICA", font=F_MAP_L, fill=NAVY)
    d.text((640, 350), "ASIA", font=F_MAP_L, fill=NAVY)
    d.text((782, 330), "OCEANIA", font=F_MAP_L, fill=NAVY)

    # ---- Continent sections: 3 columns x 2 rows, 4 stories each ---------
    gx, gy = 24, 382
    bw, bh, gap = 314, 272, 13
    for s, (name, colour, stories) in enumerate(SECTIONS):
        x = gx + (s % 3) * (bw + gap)
        y = gy + (s // 3) * (bh + gap)
        d.rectangle([x, y, x + bw, y + bh], fill=(255, 255, 255),
                    outline=RULE, width=1)
        d.rectangle([x, y, x + bw, y + 26], fill=colour)
        d.text((x + 10, y + 6), name, font=F_SEC, fill=(255, 255, 255))
        d.text((x + bw - 10, y + 6), "4 STORIES", font=F_SEC,
               fill=(255, 255, 255), anchor="ra")
        sy = y + 36
        for head, sub in stories:
            for j, line in enumerate(wrap(d, head, F_HEAD, bw - 20)[:2]):
                d.text((x + 10, sy + j * 14), line, font=F_HEAD, fill=INK)
            n_head = len(wrap(d, head, F_HEAD, bw - 20)[:2])
            for j, line in enumerate(wrap(d, sub, F_SUB, bw - 20)[:2]):
                d.text((x + 10, sy + n_head * 14 + j * 13), line,
                       font=F_SUB, fill=(70, 70, 70))
            sy += 58
            if (head, sub) is not stories[-1]:
                d.line([(x + 10, sy - 6), (x + bw - 10, sy - 6)],
                       fill=(225, 218, 200), width=1)

    # ---- Footer: also-today briefs + sources ----------------------------
    fy = gy + 2 * bh + gap + 6
    d.line([(24, fy), (1000, fy)], fill=RULE, width=2)
    for j, line in enumerate(wrap(d, ALSO, F_FOOT, 976)):
        d.text((24, fy + 8 + j * 15), line, font=F_FOOT, fill=INK)
    d.text((24, fy + 8 + 2 * 15 + 4), SOURCES, font=F_SRC, fill=GREY)

    img.save("entry.png", "PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
