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
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>

## Layout

- Masthead "THE WORLD TODAY" + "WEDNESDAY, 18 NOVEMBER 2026 • 30 STORIES • 6 CONTINENTS"
- 3 lead stories: the US says the Strait of Hormuz stays open; Trump meets Marcos in Manila; Nvidia beats forecasts in its first results without Huang.
- Schematic world map ("WHERE IT HAPPENED") with a marker per continent.
- 6 continent sections × 4 stories each (24 stories).
- "ALSO TODAY" strip with 3 more briefs. Total: 30 stories.

## The 30 stories (all reported on 18 Nov 2026)

### Leads
1. US says Hormuz stays open as the Gulf war grinds on; 900m barrels escorted since May — AP
2. Trump meets Marcos in Manila; "Pax Silica" AI pact; Trump-Xi-Putin trilateral Thursday — AP
3. Nvidia beats forecasts in first results without Huang; revenue $115.8bn, up 103% — Reuters

### North America
4. SpaceX Dragon CRS-35 undocks from the ISS with 6,300 lb of science — NASA
5. SpaceX flies classified USSF-317; China launches hours apart — AP
6. FAA pauses Juniper router rollout after a ground stop cancelled 18,000+ flights — Reuters
7. Xi meets Carney; Canada-China extend trade ahead of APEC — Reuters

### Europe
8. Haaland's late penalty sends Norway through 3-2 over Denmark (Tuesday evening) — BBC
9. UEFA backs Diallo to challenge Infantino for the FIFA presidency — Reuters
10. UN rights chief warns over the EU plan to send asylum seekers to Rwanda — UN News
11. Estonia's Russia border shutdown strands families — Reuters

### Asia
12. Knesset elects Eisenkot ally Matan Kahana speaker, 66-52 (Tuesday evening) — Reuters
13. Cyclone Akvan strengthens off India; landfall due Friday — IMD
14. Japan scrambles jets as two suspected Russian aircraft enter its airspace — Reuters
15. MS Dhoni, 45, retires from the IPL; CSK name him mentor (Tuesday evening) — Reuters

### Africa
16. Ebola toll passes 5,300 in DR Congo; outbreak tops 11,000 cases — WHO
17. Mofokeng brace as South Africa beat Kenya 2-1 in Nairobi — Reuters
18. Tinubu presses for cheaper climate finance at COP31 — Reuters
19. Nigeria clears two suspected Ebola cases, tests negative — WHO

### South America
20. Colombia illegal gold mine collapse kills 14 in Narino — AP
21. Catholics fall to 55% in Latin America over 30 years (Latinobarometro) — Al Jazeera
22. US names Guatemalan gang Los Lorenzanas a terrorist organisation — AP
23. SSL Gold Cup: 40 nations confirmed for the Rio final — Reuters

### Oceania
24. Leihani Zoric, 14, flies home a double world champion — AAP
25. Silver Ferns beat Diamonds 62-50; Constellation Cup 2-0 — AAP
26. Debate reignites: should NZ join Australia? — AAP
27. Australia leads the COP31 fossil-fuel draft — AAP

### Also today
28. Trump, Xi and Putin to hold first trilateral nuclear talks in Shenzhen on Thursday — AP
29. Fed minutes due on Wednesday — Reuters
30. India re-elected to the UN telecom council for 2027-30 — Reuters
