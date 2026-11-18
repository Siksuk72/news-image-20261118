# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Siksuk72/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Siksuk72/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image that sums up the world's news of Wednesday 18 November 2026:
a one-page newspaper front page drawn programmatically with Python PIL
(`draw.py`), copied to `/output/entry.png` by `main.ts` (Node 22, stdlib
only). Drawing in code — not image generation — means every word is
spelled correctly and stays legible at ~300 px.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>

## Layout

- Masthead "THE WORLD TODAY" + "WEDNESDAY, 18 NOVEMBER 2026 • 30 STORIES • 6 CONTINENTS"
- 3 lead stories: the US military saying the Strait of Hormuz stays open; Trump meeting Marcos in Manila; Nvidia beating forecasts in its first results without Huang.
- Schematic world map ("WHERE IT HAPPENED") with a marker per continent.
- 6 continent sections × 4 stories each (24 stories).
- "ALSO TODAY" strip with 3 more briefs. Total: 30 stories.

## The 30 stories (all reported on 17-18 Nov 2026)

Built early on Wednesday 18 November, from what the news services had
reported of the day by then — Wednesday events, plus Tuesday-evening
events first reported in Wednesday's editions (the rules count events
that happened, or were first reported, on 18 November). The date basis
of each story is noted below: "Wed" = happened, or was first reported,
on Wednesday 18 November; "Tue eve" = broke Tuesday evening and led
Wednesday's editions.

### Leads
1. (Wed) US says the Strait of Hormuz stays open; 900m barrels passed under escort since May — Al Jazeera (CENTCOM)
2. (Wed) Trump meets Marcos in Manila; "Pax Silica" AI pact; Thursday brings the Trump-Xi-Putin trilateral — AP, BBC, NY Post
3. (Tue eve) Nvidia beats forecasts in first results without Huang: revenue $115.8bn, up 103%; $130bn Q4 guide — CNBC, Reuters

### North America
4. (Wed) SpaceX Dragon undocks from the ISS with 6,300 lb of science — NASA
5. (Wed) SpaceX flies classified USSF-317 from Vandenberg; China launches a Long March 2D hours earlier — Astronomy, VC Star
6. (Tue eve) FAA pauses Juniper router rollout after the ground stop that cancelled 18,000-plus flights — Reuters
7. (Tue eve) Xi meets Carney; Canada and China extend trade cooperation ahead of APEC — BusinessWorld, AP

### Europe
8. (Tue eve) Haaland's 96th-minute penalty sends Norway past Denmark 3-2 into the Nations League quarters; Portugal top group — Reuters
9. (Tue eve) UEFA backs France's Diallo to challenge Infantino in next year's FIFA election — UEFA via press reports
10. (Tue eve) UN rights chief Türk warns over the EU plan to transfer asylum seekers to Rwanda — UN News
11. (Wed) COP31 talks grind on in Antalya; draft deal splits over fossil fuels — Reuters, UN News

### Asia
12. (Tue eve) Knesset elects Eisenkot ally Matan Kahana speaker, 66-52 — Reuters, CNN
13. (Wed) Cyclone Akvan strengthens to a severe cyclonic storm off India; landfall due Friday — IMD
14. (Tue eve) Japan scrambles jets as two suspected Russian aircraft enter its airspace — Japan Times, USNI News
15. (Tue eve) MS Dhoni, 45, retires from the IPL; Chennai name him mentor — CricTracker, Sportskeeda

### Africa
16. (Wed) Ebola death toll passes 5,300 in DR Congo; outbreak tops 11,000 cases — Al Jazeera, WHO
17. (Tue eve) Mofokeng scores twice as South Africa beat Kenya 2-1 to top their AFCON group — Soccer Laduma
18. (Tue eve) Tinubu presses for cheaper climate finance at COP31 — QNC News
19. (Wed) Nigeria clears two suspected Ebola cases; tests negative — Al Jazeera

### South America
20. (Tue eve) Colombia illegal gold mine collapse kills 14 in Nariño — Al Jazeera
21. (Tue eve) Catholics fall to 55% in Latin America in 30 years; Evangelicals now lead in three nations — Latinobarómetro via Christian Post
22. (Tue eve) US names Guatemalan gang Los Lorenzanas a terrorist organisation — CEPR, US State Dept.
23. (Wed) SSL Gold Cup: 40 nations confirmed for the Rio final; draw takes place Wednesday — SSL Gold Cup

### Oceania
24. (Wed) Leihani Zoric, 14, flies home a double world champion, the youngest-ever ISA open women's winner — Surfing Australia via Medianet
25. (Tue eve) New Zealand beat Australia 62-50 to lead the Constellation Cup 2-0 — Nine
26. (Tue eve) Debate reignites over whether NZ should become Australia's seventh state — The Post via press reports
27. (Tue eve) Australia's COP31 draft urges an immediate shift from fossil fuels and $120bn in adaptation aid — Pollar, Reuters

### Also today
28. Trump, Xi and Putin to hold the first trilateral nuclear talks in Shenzhen on Thursday — AP, NY Post
29. Fed minutes due on Wednesday as markets watch for rate signals — market reports
30. India re-elected to the UN telecom council for 2027-30 — Education Times

## Method & verification

- Research: web search on 18 Nov 2026 (early morning UTC) against
  reporting dated 17-18 Nov 2026; every story above traces to at least
  one named reputable source. Claims are labelled as claims ("Tehran
  insists…", "Iran claims…"). No story was invented; uncertain items
  were dropped, not guessed. Stories from 16 November or earlier were
  excluded even when they led Wednesday's headline round-ups (the FAA
  grounding and Microsoft outage of 13 Nov, the Pope's rosary incident
  and the Mamdani police reform of 16 Nov, Germany's 5-0 win over the
  Netherlands, the Trident submarine's return, and Trump's "giant step
  back" quote of 8 Nov).
- Rendering: `python3 draw.py` → `entry.png` (1024×1024 PNG, 172,684
  bytes, sha256
  `34461958b8e1a890617efe361543bbaadd38e0dc4f4dbc5635813821fbd7b755`).
  DejaVu fonts, fixed layout, no randomness, no network — re-runs are
  byte-identical. Checked visually at full size: masthead, date and lead
  headlines stay legible; every sub-line fits its two-line allowance.
- Program: `main.ts` copies `entry.png` to `/output/entry.png`; two runs
  write byte-identical output.

## License

MIT (see LICENSE).
