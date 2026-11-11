# GameNative compatibility worklist

Generated: `2026-11-11T04:15:12.746Z` · Ratings since: `2026-08-13T04:15:12.746Z` · Telemetry window: `21` days on `Adreno + Turnip`

This file is rewritten every night. To mark a game as fixed, tick its box in the checklist issue linked under each section (or change `[ ]` to `[x]` on its row here). The sync remembers the tick with its date until the data agrees and the game leaves the list. Untick to undo. See the [README](README.md) for how to read it and how to help.

## How a game lands here

- **Does not work**: 20+ ratings, 70%+ one-star in the deciding window, and under 60% of users ever rendered a game window on Adreno + Turnip in the telemetry window.
- **Probably does not work**: 50%+ one-star in the deciding window and under 60% rendered, or 70%+ one-star with no telemetry (under 10 users).
- **Works, but the first launch usually fails**: 50%+ one-star but 60%+ of users render the game eventually.
- **Which ratings count**: the one-star columns show the ratings that decided the row: `(14d)` the last 14 days, `(last 20)` the newest ratings at any age, `(since fix)` ratings given after a fix shipped. "Newest rating" says how old the newest of them is.
- **Recovered**: the 90-day history alone would put the game on a broken list, but the deciding window (5+ ratings) is under 50% one-star.

"Users rendered" is the share of users on Adreno GPUs with the Turnip driver who got the game to put a frame on screen at least once in the telemetry window, on any app version. Other GPUs are not counted. "n/a" means no telemetry for that game yet.

"Newest release rendered" is the same share counted on the newest app release only. "(drop)" marks a game that renders for far fewer users on that release than across all versions, which usually points at a regression in the release.

## Counts

| Verdict | Games |
|---|---:|
| Does not work | 118 |
| Probably does not work | 165 |
| Fix shipped, waiting for ratings | 17 |
| First launch fails | 343 |
| Mixed | 490 |
| Works | 1034 |
| Total | 2167 |

## Does not work (118)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 64 | 75 | 85% (since fix) | Does not open (93%) | 57% | today | 44% |  |
| 2 | [ ] | Road Rash™: 30th Anniversary Edition (STEAM) | 43 | 59 | 73% (14d) | Does not open (76%) | 58% | today | 63% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 3 | [ ] | Metro 2033 Redux (STEAM) | 31 | 38 | 82% (14d) | Does not open (70%) | 41% | today | 38% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 4 | [x] 2026-10-18 | Project Zomboid (STEAM) | 50 | 56 | 89% (since fix) | Does not open (66%) | 54% | today | 51% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 5 | [ ] | Counter-Strike 2 (STEAM) | 38 | 52 | 73% (since fix) | Does not open (67%) | 57% | 1d ago | 63% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 6 | [ ] | Hogwarts Legacy (STEAM) | 22 | 27 | 81% (14d) | Does not open (65%) | 55% | today | 21% (drop) | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 7 | [ ] | Metro: Last Light Redux (STEAM) | 20 | 21 | 95% (14d) | Does not open (90%) | 24% | 3d ago | 18% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 8 | [ ] | Saints Row 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (96%) | 37% | 2d ago | 39% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 9 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (76%) | 0% | 2d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 10 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 18 | 25 | 72% (14d) | Does not open (76%) | 58% | today | 41% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 11 | [ ] | Saints Row 2 (GOG) | 18 | 24 | 75% (14d) | Does not open (92%) | 42% | 1d ago | 36% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 12 | [ ] | Borderlands 2 (EPIC) | 16 | 23 | 70% (14d) | Does not open (83%) | 58% | today | 44% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 13 | [ ] | Bloons TD 6 (EPIC) | 16 | 21 | 76% (14d) | Does not open (80%) | 50% | today | 17% (drop) |  |
| 14 | [ ] | Call of Duty: Black Ops II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (77%) | 33% | 1d ago | 48% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 15 | [ ] | Garry's Mod (STEAM) | 7 | 10 | 70% (since fix) | Does not open (81%) | 55% | 1d ago | 43% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 16 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (96%) | 26% | 1d ago | n/a | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 17 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 18 | 20 | 90% (last 20) | No graphics (46%) | 24% | 3d ago | n/a | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 18 | [ ] | Yume Nikki (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | 17% | 4d ago | 39% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 19 | [ ] | skate. (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | 12% | today | 15% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 20 | [ ] | CARRION (GOG) | 18 | 20 | 90% (last 20) | Does not open (78%) | 8% | 1d ago | n/a | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 21 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 18 | 20 | 90% (last 20) | Does not open (86%) | 44% | today | 19% (drop) | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 22 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (70%) | 6% | 5d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 23 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (65%) | 5% | 17d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 24 | [ ] | The Witcher: Enhanced Edition (GOG) | 19 | 20 | 95% (last 20) | Does not open (73%) | 12% | 2d ago | 0% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 25 | [ ] | CPM 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (88%) | 5% | 2d ago | n/a | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 26 | [ ] | Mafia II (Classic) (STEAM) | 20 | 20 | 100% (last 20) | Does not open (74%) | 7% | 3d ago | n/a | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 27 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 14% | 4d ago | n/a | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 28 | [ ] | Path of Exile (STEAM) | 18 | 20 | 90% (last 20) | Does not open (91%) | 50% | 2d ago | n/a | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 29 | [ ] | Fall Guys (EPIC) | 19 | 20 | 95% (last 20) | Does not open (76%) | 15% | 1d ago | 10% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 30 | [ ] | Detroit: Become Human (STEAM) | 19 | 20 | 95% (last 20) | Does not open (75%) | 43% | 9d ago | n/a | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 31 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | 0% | today | n/a | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 32 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | No graphics (54%) | 6% | 14d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 33 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 9 | 12 | 75% (since fix) | Does not open (77%) | 17% | 3d ago | 29% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 34 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (74%) | 11% | 5d ago | n/a | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 35 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (92%) | 6% | 12d ago | n/a | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 36 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (68%) | 14% | 10d ago | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 37 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (88%) | 17% | 4d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 38 | [ ] | Borderlands GOTY (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 22% | 2d ago | n/a | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 39 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (79%) | 15% | 2d ago | 20% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 40 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (88%) | 27% | 2d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 41 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (68%) | 22% | 3d ago | n/a | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 42 | [ ] | Breath of Fire IV (STEAM) | 20 | 20 | 100% (last 20) | Does not open (58%) | 23% | 9d ago | n/a | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 43 | [ ] | Spore (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | 27% | 2d ago | n/a | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 44 | [ ] | MECCHA CHAMELEON (STEAM) | 15 | 20 | 75% (last 20) | Does not open (65%) | 53% | 3d ago | 25% (drop) | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 45 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 48% | 4d ago | n/a | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 46 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | 20% | 3d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 47 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (83%) | 53% | 25d ago | n/a | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 48 | [ ] | Plague Inc: Evolved (STEAM) | 14 | 20 | 70% (last 20) | Does not open (66%) | 59% | 1d ago | 65% |  |
| 49 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | 0% | 25d ago | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 50 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (56%) | 21% | 6d ago | n/a | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 51 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 0% | 3d ago | n/a | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 52 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 17 | 20 | 85% (last 20) | Does not open (46%) | 50% | 13d ago | 46% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 53 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (86%) | 33% | 10d ago | n/a |  |
| 54 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 23% | 2d ago | n/a | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 55 | [ ] | Black Mesa (STEAM) | 15 | 20 | 75% (last 20) | Does not open (80%) | 22% | 18d ago | 50% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 56 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (84%) | 12% | 2d ago | n/a | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 57 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | 42% | 32d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 58 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (47%) | 36% | 6d ago | 35% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 59 | [ ] | Watch_Dogs (STEAM) | 14 | 20 | 70% (last 20) | Does not open (90%) | 28% | 4d ago | n/a | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 60 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (74%) | 30% | 4d ago | n/a | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 61 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | 0% | 9d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 62 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (65%) | 14% | 23d ago | n/a | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 63 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 21% | 20d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 64 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | 45% | today | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 65 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (96%) | 38% | 20d ago | n/a | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 66 | [ ] | XCOM: Enemy Unknown (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | 10% | 6d ago | n/a | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 67 | [ ] | Half-Life: Blue Shift (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 31% | 2d ago | n/a | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 68 | [ ] | Trackmania (STEAM) | 14 | 20 | 70% (last 20) | Does not open (85%) | 23% | 2d ago | 15% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 69 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 9% | 9d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 70 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (60%) | 31% | 11d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 71 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | 38% | 10d ago | n/a | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 72 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | No graphics (56%) | 10% | 4d ago | n/a | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 73 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (82%) | 7% | 9d ago | n/a | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 74 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 20 | 20 | 100% (last 20) | No graphics (60%) | 27% | 34d ago | 40% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 75 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 21% | 11d ago | n/a | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 76 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (64%) | 50% | 4d ago | n/a | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 77 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 0% | 24d ago | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 78 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (67%) | 0% | 17d ago | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 79 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 6% | 6d ago | 9% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 80 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (65%) | 58% | 1d ago | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 81 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (82%) | 40% | 30d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 82 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | 38% | 6d ago | n/a | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 83 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 30% | 8d ago | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 84 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (92%) | 5% | 17d ago | 10% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 85 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (81%) | 27% | 3d ago | n/a | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 86 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 19 | 20 | 95% (last 20) | Does not open (93%) | 8% | 10d ago | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 87 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (76%) | 30% | 10d ago | n/a | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 88 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (47%) | 59% | 1d ago | 50% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 89 | [ ] | Aliens vs. Predator (STEAM) | 17 | 20 | 85% (last 20) | No graphics (53%) | 14% | 2d ago | n/a | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 90 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (68%) | 21% | 27d ago | n/a | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 91 | [ ] | Lost Planet: Extreme Condition (STEAM) | 15 | 20 | 75% (last 20) | Does not open (78%) | 48% | 1d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 92 | [ ] | Hotline Miami (GOG) | 15 | 20 | 75% (last 20) | Does not open (87%) | 59% | 1d ago | n/a | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 93 | [ ] | Changed (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 55% | today | 30% (drop) |  |
| 94 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | 21% | 1d ago | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 95 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 31% | 9d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 96 | [ ] | Umamusume: Pretty Derby (STEAM) | 18 | 20 | 90% (last 20) | Does not open (86%) | 46% | 7d ago | n/a | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 97 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (97%) | 31% | 9d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 98 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | 18% | today | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 99 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (95%) | 44% | 22d ago | 36% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 100 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 44% | 8d ago | n/a | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 101 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (86%) | 42% | 11d ago | n/a | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 102 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (68%) | 39% | today | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 103 | [ ] | Kenshi (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | 6% | 10d ago | n/a | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 104 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 14 | 20 | 70% (last 20) | Does not open (56%) | 49% | 1d ago | 61% |  |
| 105 | [ ] | Zuma Deluxe (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 31% | 20d ago | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 106 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 41% | 25d ago | n/a | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 107 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | 41% | 11d ago | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 108 | [ ] | Undisputed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 58% | 3d ago | n/a | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 109 | [ ] | Call of Duty® (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 8% | 7d ago | n/a | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 110 | [ ] | skate.™ (EPIC) | 18 | 20 | 90% (last 20) | Does not open (87%) | 0% | 16d ago | n/a | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 111 | [ ] | Beyond Good & Evil™ (GOG) | 17 | 20 | 85% (last 20) | Does not open (100%) | 18% | 18d ago | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 112 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (67%) | 54% | 2d ago | n/a | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 113 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | 44% | 11d ago | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 114 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (82%) | 4% | 1d ago | 3% |  |
| 115 | [ ] | Goose Goose Duck (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 50% | 1d ago | n/a | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 116 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 36% | 6d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 117 | [ ] | Maneater (EPIC) | 16 | 20 | 80% (last 20) | Does not open (75%) | 53% | 3d ago | n/a | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 118 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | 55% | 15d ago | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |

## Probably does not work (165)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | To The Moon (GOG) | 44 | 46 | 96% (14d) | Does not open (86%) | n/a | 8d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 2 | [ ] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 29 | 51 | 57% (14d) | Does not open (64%) | 58% | today | 64% |  |
| 3 | [ ] | theHunter Classic (STEAM) | 23 | 23 | 100% (14d) | No graphics (92%) | n/a | 7d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 4 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 16 | 25 | 64% (14d) | Does not open (72%) | 50% | 1d ago | 90% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 5 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 14 | 22 | 64% (14d) | Does not open (63%) | 58% | 1d ago | 48% |  |
| 6 | [ ] | Driver: Parallel Lines (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | n/a | 2d ago | n/a | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 7 | [ ] | Gorilla Tag (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 19% | 1d ago | 10% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 8 | [ ] | VRChat (STEAM) | 12 | 20 | 60% (last 20) | Does not open (66%) | 37% | 1d ago | 24% |  |
| 9 | [ ] | Door Kickers 2 (STEAM) | 20 | 20 | 100% (last 20) | No graphics (87%) | n/a | 28d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 10 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 31d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 11 | [ ] | Alan Wake (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 25% | 1d ago | 70% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 12 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Does not open (34%) | n/a | 8d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 13 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 15d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 14 | [ ] | Metro 2033 Redux (EPIC) | 10 | 20 | 50% (last 20) | Does not open (62%) | 30% | 2d ago | 42% |  |
| 15 | [ ] | Sonic Adventure™ 2  (STEAM) | 10 | 20 | 50% (last 20) | Does not open (76%) | 49% | 2d ago | 45% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 16 | [ ] | GRID (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 49% | 2d ago | n/a | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 17 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 12d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 18 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 13 | 20 | 65% (last 20) | Does not open (85%) | 48% | today | 67% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 19 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (85%) | 43% | 1d ago | n/a |  |
| 20 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 6d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 21 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (96%) | 35% | 3d ago | n/a | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 22 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (100%) | n/a | today | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 23 | [ ] | CODE VEIN (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 48% | today | n/a | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 24 | [ ] | Grim Dawn (GOG) | 13 | 20 | 65% (last 20) | Does not open (65%) | n/a | 21d ago | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 25 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (85%) | n/a | 9d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 26 | [ ] | ARC Raiders (STEAM) | 18 | 20 | 90% (last 20) | Does not open (93%) | n/a | 2d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 27 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 8d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 28 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | n/a | 30d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 29 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | n/a | 13d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 30 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (69%) | n/a | 6d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 31 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | n/a | today | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 32 | [ ] | METAL SLUG 3 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 37% | today | n/a | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 33 | [ ] | Dead Space 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 29% | 1d ago | 38% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 34 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 29d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 35 | [ ] | Alpha Protocol (STEAM) | 17 | 20 | 85% (last 20) | Does not open (57%) | n/a | 16d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 36 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 28d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 37 | [ ] | Breathedge (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 48% | today | n/a | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 38 | [ ] | DOOM Eternal (STEAM) | 18 | 20 | 90% (last 20) | Does not open (69%) | n/a | 19d ago | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 39 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | n/a | 12d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 40 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 14d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 41 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 34% | 1d ago | n/a | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 42 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | n/a | 28d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 43 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (58%) | n/a | 30d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 44 | [ ] | Borderlands 2 RU (STEAM) | 19 | 20 | 95% (last 20) | Does not open (61%) | n/a | 28d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 45 | [ ] | WRC 7 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (65%) | n/a | 28d ago | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 46 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 28d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 47 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (81%) | n/a | 3d ago | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 48 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 14d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 49 | [ ] | HELLDIVERS™ (STEAM) | 13 | 20 | 65% (last 20) | Does not open (60%) | 41% | today | n/a | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 50 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | n/a | 31d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 51 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 6d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 52 | [ ] | OneShot (STEAM) | 16 | 20 | 80% (last 20) | Does not open (96%) | n/a | 26d ago | n/a | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 53 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 2d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 54 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (57%) | n/a | 16d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 55 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | 0% | 6d ago | n/a |  |
| 56 | [ ] | Peggle Nights (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | 14d ago | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 57 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 39d ago | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 58 | [ ] | The Survivalists (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | n/a | 56d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 59 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 10d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 60 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | n/a | 19d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 61 | [ ] | Metro 2033 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (61%) | 36% | 7d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 62 | [ ] | Euro Truck Simulator (STEAM) | 20 | 20 | 100% (last 20) | Does not open (93%) | n/a | 26d ago | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 63 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (50%) | n/a | 10d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 64 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | n/a | 33d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 65 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | n/a | 28d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 66 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (63%) | n/a | 37d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 67 | [ ] | Fishing Planet (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 38% | today | n/a | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 68 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 20 | 20 | 100% (last 20) | Does not open (53%) | n/a | 26d ago | n/a | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 69 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 19 | 20 | 95% (last 20) | Does not open (95%) | n/a | 53d ago | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 70 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | today | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 71 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 4d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 72 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 6d ago | n/a |  |
| 73 | [ ] | Resident Evil Requiem (STEAM) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 30d ago | n/a | [#210](https://github.com/GameNative/gamenative-compat/issues/210) |
| 74 | [ ] | Marvel's Spider-Man 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | n/a | 30d ago | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 75 | [ ] | They Are Billions (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | n/a | 7d ago | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 76 | [ ] | Alien Breed: Impact (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 16d ago | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 77 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | n/a | 28d ago | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 78 | [ ] | Bionic Commando Rearmed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | n/a | 21d ago | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 79 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | n/a | 15d ago | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 80 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (85%) | n/a | 4d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 81 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 2d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 82 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | today | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 83 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 1d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 84 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 6d ago | n/a |  |
| 85 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 6d ago | n/a |  |
| 86 | [ ] | GeoGuessr Steam Edition (STEAM) | 19 | 20 | 95% (last 20) | Does not open (75%) | n/a | 23d ago | n/a | [#154](https://github.com/GameNative/gamenative-compat/issues/154) |
| 87 | [ ] | Apex Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | n/a | 12d ago | n/a | [#261](https://github.com/GameNative/gamenative-compat/issues/261) |
| 88 | [ ] | Melatonin (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | n/a | 19d ago | n/a | [#272](https://github.com/GameNative/gamenative-compat/issues/272) |
| 89 | [ ] | No More Room in Hell (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 24d ago | n/a | [#365](https://github.com/GameNative/gamenative-compat/issues/365) |
| 90 | [ ] | Zenless Zone Zero (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | n/a | 14d ago | n/a | [#369](https://github.com/GameNative/gamenative-compat/issues/369) |
| 91 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 18 | 20 | 90% (last 20) | Does not open (88%) | n/a | 20d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 92 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 12d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 93 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (52%) | n/a | 9d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 94 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 13d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 95 | [ ] | Look Outside (GOG) | 13 | 20 | 65% (last 20) | Does not open (100%) | n/a | 2d ago | n/a |  |
| 96 | [ ] | Pathway (EPIC) | 19 | 20 | 95% (last 20) | Does not open (59%) | n/a | 12d ago | n/a | [#298](https://github.com/GameNative/gamenative-compat/issues/298) |
| 97 | [ ] | Wuthering Waves (STEAM) | 19 | 20 | 95% (last 20) | Does not open (83%) | n/a | 13d ago | n/a | [#216](https://github.com/GameNative/gamenative-compat/issues/216) |
| 98 | [ ] | Lay of the Land (STEAM) | 18 | 20 | 90% (last 20) | No graphics (61%) | n/a | 10d ago | n/a | [#477](https://github.com/GameNative/gamenative-compat/issues/477) |
| 99 | [ ] | Marvel's Midnight Suns (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | n/a | 28d ago | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 100 | [ ] | Beholder (EPIC) | 15 | 20 | 75% (last 20) | Does not open (69%) | n/a | 16d ago | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 101 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 9d ago | n/a |  |
| 102 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | Does not open (42%) | n/a | 1d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 103 | [ ] | Mafia II (Classic) (GOG) | 13 | 20 | 65% (last 20) | Does not open (96%) | n/a | 18d ago | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 104 | [ ] | Mirror's Edge™ (GOG) | 11 | 20 | 55% (last 20) | No graphics (62%) | 46% | today | n/a | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 105 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 10 | 20 | 50% (last 20) | Does not open (86%) | 42% | 20d ago | n/a |  |
| 106 | [ ] | King's Bounty: The Legend (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | n/a | 5d ago | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 107 | [ ] | Utopia Must Fall (STEAM) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 4d ago | n/a | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 108 | [ ] | PICO PARK:Classic Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 33d ago | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 109 | [ ] | ENDLESS Space™ 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | n/a | 26d ago | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 110 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (57%) | n/a | 23d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 111 | [ ] | Drop Duchy (EPIC) | 12 | 20 | 60% (last 20) | Does not open (100%) | n/a | 10d ago | n/a |  |
| 112 | [ ] | Clive Barker's Undying (GOG) | 17 | 20 | 85% (last 20) | Does not open (75%) | n/a | 15d ago | n/a | [#388](https://github.com/GameNative/gamenative-compat/issues/388) |
| 113 | [ ] | The Elder Scrolls IV: Oblivion Remastered (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | n/a | 29d ago | n/a | [#312](https://github.com/GameNative/gamenative-compat/issues/312) |
| 114 | [ ] | Re-Volt (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (71%) | n/a | 17d ago | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 115 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (92%) | n/a | 16d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 116 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (83%) | 40% | 9d ago | n/a | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 117 | [ ] | Sandustry (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 1d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 118 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | No graphics (57%) | 20% | 4d ago | n/a | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 119 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (57%) | n/a | 2d ago | n/a |  |
| 120 | [ ] | F.E.A.R. 2: Project Origin + Reborn (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 11d ago | n/a | [#478](https://github.com/GameNative/gamenative-compat/issues/478) |
| 121 | [ ] | Beat Cop (STEAM) | 14 | 20 | 70% (last 20) | Does not open (72%) | n/a | 5d ago | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 122 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | n/a | 3d ago | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 123 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | n/a | 1d ago | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 124 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (75%) | n/a | today | n/a |  |
| 125 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | n/a | 22d ago | n/a |  |
| 126 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (78%) | 58% | today | n/a |  |
| 127 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 12 | 20 | 60% (last 20) | Does not open (92%) | 58% | 2d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 128 | [ ] | Mini Metro (STEAM) | 10 | 20 | 50% (last 20) | Does not open (41%) | 42% | today | n/a |  |
| 129 | [ ] | Fallout Classic (GOG) | 15 | 20 | 75% (last 20) | Does not open (71%) | n/a | 27d ago | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 130 | [ ] | Dungeon Keeper™ 2 (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 17d ago | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 131 | [ ] | Blood Omen: Legacy of Kain (GOG) | 13 | 20 | 65% (last 20) | Does not open (62%) | 44% | today | n/a |  |
| 132 | [ ] | Mafia: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 52% | 3d ago | 38% |  |
| 133 | [ ] | Cities: Skylines (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | n/a | today | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 134 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 6d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 135 | [ ] | Styx: Master of Shadows (EPIC) | 11 | 20 | 55% (last 20) | Does not open (65%) | 40% | 2d ago | n/a |  |
| 136 | [ ] | No More Heroes (STEAM) | 11 | 20 | 55% (last 20) | No graphics (71%) | 50% | 25d ago | n/a |  |
| 137 | [ ] | A Plague Tale: Innocence (GOG) | 11 | 20 | 55% (last 20) | Does not open (91%) | 46% | 18d ago | n/a |  |
| 138 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 40% | 3d ago | n/a | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 139 | [ ] | Knights of Pen and Paper 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (42%) | n/a | 2d ago | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 140 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 13 | 20 | 65% (last 20) | No graphics (56%) | n/a | 29d ago | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 141 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | n/a | 33d ago | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 142 | [ ] | Another World: 20th Anniversary Edition (GOG) | 12 | 20 | 60% (last 20) | Does not open (67%) | 50% | 4d ago | n/a |  |
| 143 | [ ] | Minit (EPIC) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 3d ago | n/a |  |
| 144 | [ ] | Songs of Conquest (EPIC) | 12 | 20 | 60% (last 20) | Does not open (75%) | n/a | 9d ago | n/a |  |
| 145 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 12d ago | n/a |  |
| 146 | [ ] | Fogpiercer (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 24d ago | n/a | [#303](https://github.com/GameNative/gamenative-compat/issues/303) |
| 147 | [ ] | The Stanley Parable (STEAM) | 13 | 20 | 65% (last 20) | Does not open (89%) | 58% | 16d ago | n/a |  |
| 148 | [ ] | Buck Up And Drive! (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | n/a | 16d ago | n/a |  |
| 149 | [ ] | Turnip Boy Robs a Bank (EPIC) | 12 | 20 | 60% (last 20) | Does not open (65%) | 40% | 16d ago | n/a | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 150 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | n/a | 1d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 151 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (78%) | n/a | 5d ago | n/a |  |
| 152 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | n/a | 2d ago | n/a |  |
| 153 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 54% | 3d ago | n/a |  |
| 154 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 52% | 6d ago | n/a |  |
| 155 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | n/a | 5d ago | n/a |  |
| 156 | [ ] | Ys: Memories of Celceta (STEAM) | 12 | 20 | 60% (last 20) | No graphics (45%) | 31% | 11d ago | n/a |  |
| 157 | [ ] | Dex (GOG) | 12 | 20 | 60% (last 20) | Does not open (83%) | n/a | today | n/a |  |
| 158 | [ ] | Secret of Mana (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (55%) | n/a | 24d ago | n/a |  |
| 159 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | n/a | 13d ago | n/a |  |
| 160 | [ ] | Crying Suns (EPIC) | 11 | 20 | 55% (last 20) | No graphics (57%) | n/a | 1d ago | n/a |  |
| 161 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | n/a | 76d ago | n/a |  |
| 162 | [ ] | Railway Chai Wala (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | n/a | 4d ago | n/a |  |
| 163 | [ ] | Asterigos: Curse of the Stars (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (50%) | n/a | 11d ago | n/a |  |
| 164 | [ ] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 19% | 6d ago | n/a |  |
| 165 | [ ] | Delver (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 53% | 3d ago | n/a |  |

## Fix shipped, waiting for ratings (17)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | Plants vs. Zombies: Game of the Year (STEAM) | 2026-11-04 | 6 | 4 | 1d ago | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 2 | Transistor (STEAM) | 2026-11-10 | 0 | 0 | 11d ago | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 3 | Max Payne 3 (STEAM) | 2026-11-04 | 1 | 1 | 4d ago | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 4 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 6 | 6 | 4d ago | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 5 | Call of Duty: Black Ops (STEAM) | 2026-10-14 | 7 | 3 | 1d ago | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 6 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 3 | 3 | today | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 7 | L.A. Noire (STEAM) | 2026-11-04 | 0 | 0 | 8d ago | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 8 | Overwatch® (STEAM) | 2026-10-20 | 8 | 7 | 3d ago | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 9 | Necesse (STEAM) | 2026-10-29 | 5 | 0 | 2d ago | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 10 | Peggle Deluxe (STEAM) | 2026-10-29 | 0 | 0 | 6d ago | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 11 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 1 | 1 | today | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 12 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 1 | 1 | 7d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 13 | Need for Speed™ (STEAM) | 2026-11-04 | 0 | 0 | 20d ago | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 14 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 0 | 0 | 8d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 15 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 0 | 0 | 7d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 16 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 0 | 0 | 13d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 17 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 6d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |

## Works, but the first launch usually fails (343)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 132 | 156 | 85% (14d) | Does not open (83%) | 64% | today | 8% (drop) | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 68 | 87 | 78% (14d) | Does not open (63%) | 90% | today | 93% |  |
| 3 | [ ] | Deskrawl: Idle ARPG (STEAM) | 55 | 66 | 83% (14d) | Does not open (60%) | 88% | today | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 4 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 53 | 75 | 71% (14d) | Does not open (55%) | 82% | today | 81% |  |
| 5 | [ ] | Grand Theft Auto V Legacy (STEAM) | 27 | 36 | 75% (since fix) | Does not open (87%) | 77% | today | 69% |  |
| 6 | [ ] | Valheim (STEAM) | 25 | 39 | 64% (since fix) | No graphics (52%) | 89% | today | 81% |  |
| 7 | [ ] | MONSTER HUNTER RISE (STEAM) | 43 | 76 | 57% (14d) | Does not open (82%) | 63% | today | 59% |  |
| 8 | [ ] | No Man's Sky (STEAM) | 20 | 33 | 61% (since fix) | Controller issues (61%) | 79% | today | 69% |  |
| 9 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 39 | 53 | 74% (14d) | Does not open (77%) | 78% | today | 78% |  |
| 10 | [ ] | Rocket League® (EPIC) | 38 | 48 | 79% (14d) | Does not open (78%) | 64% | today | 40% (drop) | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 11 | [ ] | Half-Life (STEAM) | 36 | 57 | 63% (14d) | Does not open (57%) | 71% | today | 58% |  |
| 12 | [ ] | Cyberpunk 2077 (STEAM) | 35 | 65 | 54% (14d) | Does not open (67%) | 75% | today | 69% |  |
| 13 | [ ] | Palworld (STEAM) | 32 | 54 | 59% (14d) | Does not open (71%) | 86% | today | 83% |  |
| 14 | [ ] | DREDGE (EPIC) | 32 | 37 | 86% (14d) | Does not open (73%) | 76% | today | 49% (drop) | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 15 | [ ] | Terraria (STEAM) | 31 | 54 | 57% (14d) | No graphics (51%) | 72% | today | 66% |  |
| 16 | [ ] | Buckshot Roulette (STEAM) | 31 | 61 | 51% (14d) | Does not open (62%) | 81% | today | 52% (drop) |  |
| 17 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 28 | 34 | 82% (14d) | Does not open (72%) | 60% | today | 56% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 18 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 25 | 40 | 63% (14d) | Does not open (57%) | 77% | today | 61% |  |
| 19 | [ ] | ELDEN RING (STEAM) | 24 | 40 | 60% (14d) | Does not open (85%) | 73% | today | 67% |  |
| 20 | [ ] | WendyQuest (STEAM) | 23 | 46 | 50% (14d) | Does not open (75%) | 86% | today | 81% |  |
| 21 | [ ] | BioShock (STEAM) | 20 | 37 | 54% (14d) | Does not open (36%) | 75% | today | 64% |  |
| 22 | [ ] | BeamNG.drive (STEAM) | 20 | 21 | 95% (14d) | Does not open (81%) | 86% | today | 56% (drop) | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 23 | [ ] | Quake (STEAM) | 19 | 28 | 68% (14d) | Does not open (62%) | 84% | today | 53% (drop) |  |
| 24 | [ ] | DRAGON BALL FighterZ (STEAM) | 25 | 40 | 63% (since fix) | Does not open (89%) | 72% | 1d ago | 87% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 25 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 18 | 21 | 86% (14d) | Does not open (95%) | 64% | today | 6% (drop) |  |
| 26 | [ ] | Batman™: Arkham Origins (STEAM) | 17 | 25 | 68% (14d) | Does not open (84%) | 76% | 1d ago | 63% |  |
| 27 | [ ] | CHRONO TRIGGER (STEAM) | 17 | 26 | 65% (14d) | Does not open (60%) | 82% | today | 98% |  |
| 28 | [ ] | Devil May Cry 5 (STEAM) | 17 | 29 | 59% (14d) | Does not open (83%) | 73% | today | 78% |  |
| 29 | [ ] | Crypt of the NecroDancer (STEAM) | 17 | 34 | 50% (14d) | Does not open (49%) | 88% | today | 85% |  |
| 30 | [ ] | BioShock Remastered (EPIC) | 16 | 20 | 80% (14d) | Does not open (64%) | 75% | today | 64% |  |
| 31 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (88%) | 95% | 1d ago | 91% |  |
| 32 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 73% | 2d ago | 74% |  |
| 33 | [ ] | Monster Hunter: World (STEAM) | 14 | 28 | 50% (14d) | No graphics (56%) | 85% | today | 74% |  |
| 34 | [ ] | Clair Obscur: Expedition 33 (STEAM) | 14 | 25 | 56% (14d) | Graphics glitches (41%) | 88% | 1d ago | 79% |  |
| 35 | [ ] | Sorry We're Closed (EPIC) | 14 | 25 | 56% (14d) | Does not open (82%) | 74% | 2d ago | 53% (drop) |  |
| 36 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | 97% | 4d ago | n/a | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 37 | [ ] | DOOM 3: BFG Edition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (72%) | 71% | today | 63% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 38 | [ ] | Deadlock (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | 89% | today | 82% |  |
| 39 | [ ] | Fallout: New Vegas PCR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | 61% | today | 58% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 40 | [ ] | Fallout: New Vegas (EPIC) | 15 | 20 | 75% (last 20) | Does not open (59%) | 84% | today | 65% |  |
| 41 | [ ] | Welcome to Elderfield (STEAM) | 13 | 20 | 65% (last 20) | Does not open (72%) | 68% | today | 65% |  |
| 42 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 17 | 30 | 57% (since fix) | Does not open (74%) | 69% | 2d ago | 57% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 43 | [ ] | Castlevania Dominus Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (92%) | 95% | 1d ago | 83% |  |
| 44 | [ ] | Dead Island 2 (EPIC) | 15 | 20 | 75% (last 20) | Does not open (82%) | 79% | today | 50% (drop) |  |
| 45 | [ ] | Grand Theft Auto V (EPIC) | 19 | 20 | 95% (last 20) | Does not open (90%) | 75% | 6d ago | 62% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 46 | [ ] | Castlevania Advance Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (95%) | 91% | 2d ago | 79% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 47 | [ ] | Red Dead Redemption 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (98%) | 82% | 1d ago | 81% |  |
| 48 | [ ] | Order of the Sinking Star (STEAM) | 13 | 20 | 65% (last 20) | Does not open (63%) | 60% | today | 69% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 49 | [ ] | The Forest (STEAM) | 11 | 22 | 50% (14d) | Does not open (77%) | 85% | 2d ago | 88% |  |
| 50 | [ ] | Library Of Ruina (STEAM) | 11 | 21 | 52% (14d) | Does not open (69%) | 86% | today | 77% |  |
| 51 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (75%) | 100% | today | n/a | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 52 | [ ] | Hogwarts Legacy (EPIC) | 14 | 20 | 70% (last 20) | Does not open (76%) | 68% | 3d ago | 45% (drop) |  |
| 53 | [ ] | Marvel’s Spider-Man Remastered (STEAM) | 12 | 20 | 60% (last 20) | Does not open (49%) | 64% | today | 78% |  |
| 54 | [ ] | Darkest Dungeon® (EPIC) | 12 | 20 | 60% (last 20) | Does not open (64%) | 78% | 2d ago | 91% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 55 | [ ] | MIO: Memories in Orbit (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (52%) | 95% | 1d ago | 93% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 56 | [ ] | American Truck Simulator (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 80% | today | 71% |  |
| 57 | [ ] | Don't Starve Together (STEAM) | 10 | 20 | 50% (14d) | Does not open (60%) | 80% | 2d ago | 67% |  |
| 58 | [ ] | Prey (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 80% | today | 88% |  |
| 59 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (74%) | 70% | today | 47% (drop) |  |
| 60 | [ ] | Need for Speed: Hot Pursuit (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 79% | today | 83% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 61 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 78% | today | 83% |  |
| 62 | [ ] | Last Epoch (STEAM) | 11 | 20 | 55% (last 20) | Does not open (80%) | 93% | 3d ago | 71% |  |
| 63 | [ ] | Ratatan (STEAM) | 18 | 20 | 90% (last 20) | Does not open (47%) | 98% | 5d ago | n/a |  |
| 64 | [ ] | Noita (STEAM) | 10 | 20 | 50% (last 20) | Does not open (55%) | 76% | today | 84% |  |
| 65 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (63%) | 96% | today | 100% |  |
| 66 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (51%) | 82% | today | 46% (drop) | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 67 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 15 | 20 | 75% (last 20) | Does not open (48%) | 64% | 6d ago | n/a |  |
| 68 | [ ] | Abiotic Factor (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 66% | today | 75% |  |
| 69 | [ ] | Need for Speed™ Rivals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (62%) | 68% | today | n/a | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 70 | [ ] | Happy Wheels (STEAM) | 19 | 20 | 95% (last 20) | No graphics (52%) | 71% | 4d ago | 56% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 71 | [ ] | Poppy Playtime (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 73% | 2d ago | 59% |  |
| 72 | [ ] | Cave Story+ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | 86% | today | 59% (drop) | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 73 | [ ] | Dead Space (STEAM) | 14 | 20 | 70% (last 20) | Does not open (54%) | 81% | today | 79% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 74 | [ ] | Resident Evil 7 Biohazard (STEAM) | 12 | 20 | 60% (last 20) | Does not open (72%) | 81% | 2d ago | 71% |  |
| 75 | [ ] | Cry of Fear (STEAM) | 13 | 20 | 65% (last 20) | Does not open (48%) | 78% | today | 73% |  |
| 76 | [ ] | Sid Meier's Civilization VI (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | 86% | 3d ago | 72% |  |
| 77 | [ ] | Disgaea 5 Complete (STEAM) | 16 | 20 | 80% (last 20) | Does not open (76%) | 92% | 4d ago | n/a | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 78 | [ ] | Aniimo (STEAM) | 15 | 20 | 75% (last 20) | Does not open (75%) | 86% | 2d ago | 68% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 79 | [ ] | Dota 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 74% | 1d ago | 100% |  |
| 80 | [ ] | Counter-Strike: Source (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | 88% | 2d ago | 79% |  |
| 81 | [ ] | Assassin's Creed II (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | 62% | 4d ago | 65% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 82 | [ ] | River City Girls (EPIC) | 15 | 20 | 75% (last 20) | Does not open (48%) | 83% | 2d ago | n/a |  |
| 83 | [ ] | Mini Motorways (STEAM) | 14 | 20 | 70% (last 20) | Does not open (76%) | 68% | 2d ago | n/a | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 84 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (44%) | 84% | 1d ago | 75% |  |
| 85 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (53%) | 94% | 1d ago | 88% |  |
| 86 | [ ] | eFootball™ (STEAM) | 13 | 20 | 65% (last 20) | Does not open (55%) | 69% | 1d ago | 47% (drop) |  |
| 87 | [ ] | Bejeweled 3 (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 91% | 1d ago | 86% |  |
| 88 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (53%) | 84% | today | 61% |  |
| 89 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 12 | 20 | 60% (last 20) | Does not open (100%) | 97% | today | n/a |  |
| 90 | [ ] | Caravan SandWitch (EPIC) | 10 | 20 | 50% (last 20) | Does not open (88%) | 68% | 2d ago | 68% |  |
| 91 | [ ] | Until Then (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 83% | today | 58% (drop) |  |
| 92 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 68% | 4d ago | 70% |  |
| 93 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (80%) | 67% | 4d ago | n/a | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 94 | [ ] | Sid Meier's Civilization V (STEAM) | 16 | 20 | 80% (last 20) | Does not open (76%) | 63% | today | 68% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 95 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 13 | 20 | 65% (last 20) | Does not open (82%) | 74% | 2d ago | n/a | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 96 | [ ] | OMORI (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 74% | today | 44% (drop) | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 97 | [ ] | Sifu (EPIC) | 10 | 20 | 50% (last 20) | Does not open (65%) | 66% | today | 30% (drop) |  |
| 98 | [ ] | Red Dead Redemption (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | 72% | 22d ago | n/a | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 99 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (84%) | 92% | today | n/a | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 100 | [ ] | ZERO Sievert (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | 88% | 2d ago | 63% |  |
| 101 | [ ] | Palia (STEAM) | 15 | 20 | 75% (last 20) | Does not open (59%) | 75% | 4d ago | n/a | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 102 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 90% | 2d ago | 71% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 103 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 14 | 20 | 70% (last 20) | Does not open (41%) | 72% | 3d ago | 80% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 104 | [ ] | Heavy Rain (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (64%) | 92% | today | n/a |  |
| 105 | [ ] | Alabaster Dawn (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (48%) | 91% | today | 89% |  |
| 106 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (55%) | 71% | 11d ago | n/a |  |
| 107 | [ ] | Dishonored - Definitive Edition (EPIC) | 12 | 20 | 60% (last 20) | Does not open (89%) | 80% | today | 73% |  |
| 108 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | Does not open (33%) | 65% | 3d ago | 25% (drop) |  |
| 109 | [ ] | Ballionaire (STEAM) | 10 | 20 | 50% (last 20) | Does not open (76%) | 89% | today | 75% |  |
| 110 | [ ] | TBH: Task Bar Hero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (65%) | 86% | 1d ago | 77% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 111 | [ ] | Vampire Survivors (EPIC) | 14 | 20 | 70% (last 20) | Does not open (58%) | 61% | 4d ago | 37% (drop) | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 112 | [ ] | Forza Horizon 4 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (43%) | 67% | 1d ago | 13% (drop) | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 113 | [ ] | Minecraft Dungeons II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (82%) | 66% | 2d ago | 63% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 114 | [ ] | Fable - The Lost Chapters (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (54%) | 82% | 17d ago | 79% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 115 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (83%) | 64% | 1d ago | 38% (drop) | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 116 | [ ] | Yakuza: Like a Dragon (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 66% | 3d ago | n/a |  |
| 117 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 67% | 1d ago | 76% |  |
| 118 | [ ] | Resident Evil Village (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 91% | 2d ago | 78% |  |
| 119 | [ ] | Driving Rogue (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 92% | 4d ago | 79% |  |
| 120 | [ ] | Cyberpunk 2077 (GOG) | 10 | 20 | 50% (last 20) | Does not open (72%) | 72% | 1d ago | 53% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 121 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 19 | 20 | 95% (last 20) | Does not open (62%) | 83% | 10d ago | n/a | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 122 | [ ] | Fallout (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 71% | today | 77% |  |
| 123 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (50%) | 88% | today | 73% |  |
| 124 | [ ] | Moonstone Island (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (60%) | 85% | today | 73% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 125 | [ ] | Call of Duty: World at War (STEAM) | 14 | 20 | 70% (last 20) | Does not open (44%) | 86% | 3d ago | 64% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 126 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 95% | 12d ago | n/a |  |
| 127 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 10 | 20 | 50% (last 20) | Does not open (66%) | 86% | 3d ago | n/a |  |
| 128 | [ ] | PowerWash Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (85%) | 76% | today | 100% |  |
| 129 | [ ] | Tails of Iron (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 89% | 2d ago | n/a |  |
| 130 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 60% | 2d ago | n/a | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 131 | [ ] | Sonic Generations (STEAM) | 16 | 20 | 80% (last 20) | Does not open (69%) | 66% | 3d ago | 90% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 132 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 11 | 20 | 55% (last 20) | Does not open (63%) | 76% | today | 45% (drop) |  |
| 133 | [ ] | ENA: Dream BBQ (STEAM) | 10 | 20 | 50% (last 20) | Does not open (43%) | 77% | 1d ago | 60% |  |
| 134 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 69% | 9d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 135 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 17 | 20 | 85% (last 20) | Controller issues (86%) | 93% | 2d ago | n/a | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 136 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (71%) | 63% | 1d ago | n/a | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 137 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 73% | today | n/a | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 138 | [ ] | Fallout 3 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (43%) | 94% | 1d ago | 94% |  |
| 139 | [ ] | A Plague Tale: Innocence (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | 83% | 12d ago | n/a | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 140 | [ ] | Max Payne (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (46%) | 89% | 6d ago | n/a |  |
| 141 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (84%) | 88% | 1d ago | 90% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 142 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 64% | 2d ago | 73% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 143 | [ ] | Mount & Blade: Warband (STEAM) | 10 | 20 | 50% (last 20) | Does not open (86%) | 91% | today | 67% |  |
| 144 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (48%) | 92% | 1d ago | n/a |  |
| 145 | [ ] | Deliver At All Costs (EPIC) | 12 | 20 | 60% (last 20) | Does not open (56%) | 69% | 2d ago | 64% |  |
| 146 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 11 | 20 | 55% (last 20) | Does not open (72%) | 72% | today | 67% |  |
| 147 | [ ] | Dragon Age: Origins - Ultimate Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (48%) | 91% | today | 70% |  |
| 148 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | 94% | 9d ago | n/a | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 149 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (92%) | 62% | 12d ago | n/a | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 150 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 91% | 9d ago | 92% |  |
| 151 | [ ] | ABZU (EPIC) | 10 | 20 | 50% (last 20) | Does not open (86%) | 90% | 2d ago | 82% |  |
| 152 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (81%) | 67% | 9d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 153 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (82%) | 100% | 7d ago | n/a | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 154 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 75% | 4d ago | n/a |  |
| 155 | [ ] | Sonic Origins (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 83% | today | 82% |  |
| 156 | [ ] | Gothic 1 Classic (STEAM) | 12 | 20 | 60% (last 20) | Does not open (61%) | 83% | 2d ago | 56% (drop) |  |
| 157 | [ ] | Oxygen Not Included (STEAM) | 12 | 20 | 60% (last 20) | Does not open (74%) | 61% | 2d ago | 87% |  |
| 158 | [ ] | Street Fighter™ 6 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (81%) | 81% | today | 75% |  |
| 159 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (61%) | 75% | 2d ago | n/a | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 160 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | 80% | 10d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 161 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (78%) | 89% | today | n/a | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 162 | [ ] | Stellar Blade™ (STEAM) | 14 | 20 | 70% (last 20) | No graphics (43%) | 81% | 1d ago | 79% |  |
| 163 | [ ] | Fight'N Rage (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 91% | 6d ago | n/a |  |
| 164 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (62%) | 82% | 6d ago | n/a | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 165 | [ ] | Rivals of Aether II (STEAM) | 15 | 20 | 75% (last 20) | Does not open (54%) | 69% | 2d ago | n/a | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 166 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 11 | 20 | 55% (last 20) | Does not open (59%) | 74% | 8d ago | 64% |  |
| 167 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 61% | 2d ago | n/a | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 168 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (64%) | 68% | today | n/a | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 169 | [ ] | Tabletop Simulator (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 64% | 3d ago | 75% |  |
| 170 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (52%) | 69% | 1d ago | 54% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 171 | [ ] | Chained Echoes (GOG) | 14 | 20 | 70% (last 20) | Does not open (60%) | 65% | 3d ago | n/a |  |
| 172 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | Does not open (53%) | 85% | 2d ago | 100% |  |
| 173 | [ ] | Control Ultimate Edition (GOG) | 13 | 20 | 65% (last 20) | Does not open (76%) | 88% | today | 70% |  |
| 174 | [ ] | Hollow Knight: Silksong (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 61% | today | 71% |  |
| 175 | [ ] | Sonic Lost World (STEAM) | 12 | 20 | 60% (last 20) | No graphics (64%) | 82% | 4d ago | 76% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 176 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (73%) | 74% | 3d ago | n/a | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 177 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 82% | today | 80% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 178 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (57%) | 62% | 9d ago | n/a | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 179 | [ ] | Unturned (STEAM) | 12 | 20 | 60% (last 20) | Does not open (53%) | 72% | today | 73% |  |
| 180 | [ ] | Fallout 4: Game of the Year Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (50%) | 72% | 3d ago | 77% |  |
| 181 | [ ] | Counter-Strike:Global Offensive (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 79% | 1d ago | 75% |  |
| 182 | [ ] | Capcom Arcade Stadium (STEAM) | 16 | 20 | 80% (last 20) | Does not open (84%) | 71% | 11d ago | n/a | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 183 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (63%) | 91% | 6d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 184 | [ ] | One-armed robber (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (65%) | 72% | 3d ago | 50% (drop) |  |
| 185 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 14 | 20 | 70% (last 20) | Does not open (69%) | 69% | 5d ago | n/a | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 186 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | 73% | 3d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 187 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (82%) | 95% | 11d ago | n/a |  |
| 188 | [ ] | Gambonanza (STEAM) | 15 | 20 | 75% (last 20) | Does not open (63%) | 95% | today | 100% |  |
| 189 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 92% | 21d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 190 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 88% | 1d ago | n/a |  |
| 191 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 64% | 7d ago | n/a |  |
| 192 | [ ] | Dishonored 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (89%) | 85% | 2d ago | 73% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 193 | [ ] | State of Decay: Year-One (STEAM) | 11 | 20 | 55% (last 20) | Does not open (68%) | 76% | 2d ago | 67% |  |
| 194 | [ ] | The Witcher: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (59%) | 68% | 4d ago | n/a | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 195 | [ ] | Escape from Duckov (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (70%) | 95% | 1d ago | 100% |  |
| 196 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 15 | 20 | 75% (last 20) | Does not open (94%) | 80% | 2d ago | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 197 | [ ] | Final Fantasy IV (3D Remake) (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 96% | today | n/a |  |
| 198 | [ ] | Stumble Guys (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 73% | today | 65% |  |
| 199 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (56%) | 70% | 5d ago | n/a | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 200 | [ ] | Subnautica 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (58%) | 62% | today | n/a | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 201 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | 95% | today | n/a | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 202 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (60%) | 66% | 1d ago | n/a |  |
| 203 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (69%) | 79% | 16d ago | n/a | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 204 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (69%) | 89% | 4d ago | n/a | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 205 | [ ] | Supermarket Together (STEAM) | 15 | 20 | 75% (last 20) | Does not open (73%) | 62% | 6d ago | 73% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 206 | [ ] | Metro Exodus (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | 89% | today | n/a |  |
| 207 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 70% | today | n/a | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 208 | [ ] | TurretGirls (STEAM) | 12 | 20 | 60% (last 20) | No graphics (75%) | 92% | 1d ago | 80% |  |
| 209 | [ ] | A Plague Tale: Innocence (EPIC) | 11 | 20 | 55% (last 20) | Does not open (71%) | 61% | 17d ago | n/a |  |
| 210 | [ ] | Mortal Kombat 11 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 69% | 3d ago | n/a |  |
| 211 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 95% | today | n/a | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 212 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 100% | 5d ago | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 213 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (61%) | 94% | 6d ago | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 214 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 82% | 14d ago | n/a | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 215 | [ ] | Darksiders (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 81% | 17d ago | 70% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 216 | [ ] | Trailmakers (STEAM) | 13 | 20 | 65% (last 20) | Does not open (44%) | 89% | 2d ago | n/a |  |
| 217 | [ ] | My Summer Car (STEAM) | 12 | 20 | 60% (last 20) | Does not open (61%) | 80% | today | n/a |  |
| 218 | [ ] | Limbus Company (STEAM) | 11 | 20 | 55% (last 20) | Does not open (85%) | 79% | 2d ago | 83% |  |
| 219 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 81% | 14d ago | n/a |  |
| 220 | [ ] | CRUEL (STEAM) | 14 | 20 | 70% (last 20) | Does not open (88%) | 70% | 8d ago | n/a | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 221 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (95%) | 68% | 1d ago | n/a | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 222 | [ ] | GOD EATER RESURRECTION (STEAM) | 14 | 20 | 70% (last 20) | Does not open (56%) | 68% | 15d ago | n/a |  |
| 223 | [ ] | Digimon Survive (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (73%) | 96% | 7d ago | n/a |  |
| 224 | [ ] | DNF Duel (EPIC) | 13 | 20 | 65% (last 20) | Does not open (62%) | 73% | 2d ago | 31% (drop) |  |
| 225 | [ ] | Goat Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 77% | 3d ago | n/a |  |
| 226 | [ ] | The Lantern of the Laughless Saint (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 64% | 8d ago | n/a | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 227 | [ ] | Jade Empire: Special Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 71% | 2d ago | n/a | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 228 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 16 | 20 | 80% (last 20) | Does not open (69%) | 77% | 3d ago | n/a | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 229 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | 67% | 8d ago | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 230 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (92%) | 86% | 24d ago | n/a |  |
| 231 | [ ] | Invisible, Inc. (STEAM) | 15 | 20 | 75% (last 20) | Does not open (63%) | 71% | 12d ago | n/a |  |
| 232 | [ ] | Maneater (STEAM) | 15 | 20 | 75% (last 20) | Does not open (92%) | 64% | 5d ago | n/a |  |
| 233 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 15 | 20 | 75% (last 20) | No graphics (53%) | 76% | today | n/a | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 234 | [ ] | Return to Monkey Island (STEAM) | 14 | 20 | 70% (last 20) | No graphics (60%) | 82% | 4d ago | n/a |  |
| 235 | [ ] | Ultimate Custom Night (STEAM) | 14 | 20 | 70% (last 20) | No graphics (68%) | 71% | 13d ago | n/a | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 236 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 14 | 20 | 70% (last 20) | Does not open (53%) | 67% | 2d ago | n/a |  |
| 237 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (42%) | 78% | 6d ago | n/a | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 238 | [ ] | SnowRunner (STEAM) | 13 | 20 | 65% (last 20) | Does not open (96%) | 79% | 2d ago | n/a | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 239 | [ ] | Cat Mail Co. (STEAM) | 13 | 20 | 65% (last 20) | Does not open (89%) | 90% | 8d ago | n/a |  |
| 240 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (44%) | 82% | 4d ago | n/a |  |
| 241 | [ ] | Zero Escape: The Nonary Games (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 64% | 1d ago | 71% |  |
| 242 | [ ] | Lucid Blocks (STEAM) | 12 | 20 | 60% (last 20) | Does not open (78%) | 65% | 2d ago | n/a |  |
| 243 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 85% | 1d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 244 | [ ] | Revolution Idle (STEAM) | 12 | 20 | 60% (last 20) | Does not open (43%) | 80% | 4d ago | n/a |  |
| 245 | [ ] | Resident Evil Revelations 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (40%) | 84% | 4d ago | 69% |  |
| 246 | [ ] | Secrets of Grindea (STEAM) | 11 | 20 | 55% (last 20) | Does not open (45%) | 71% | 17d ago | n/a | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 247 | [ ] | Battle Brothers (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 74% | 1d ago | 80% |  |
| 248 | [ ] | Deadly Premonition: The Director's Cut (STEAM) | 18 | 20 | 90% (last 20) | Does not open (53%) | 75% | 4d ago | n/a | [#520](https://github.com/GameNative/gamenative-compat/issues/520) |
| 249 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 17 | 20 | 85% (last 20) | Does not open (60%) | 91% | 4d ago | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 250 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 20 | 80% (last 20) | Does not open (82%) | 63% | 18d ago | n/a | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 251 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (83%) | 87% | 3d ago | n/a | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 252 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | 64% | 11d ago | 30% (drop) |  |
| 253 | [ ] | Deus Ex™ GOTY Edition (GOG) | 12 | 20 | 60% (last 20) | Does not open (37%) | 88% | 11d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 254 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 67% | 2d ago | n/a |  |
| 255 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (44%) | 93% | 11d ago | n/a |  |
| 256 | [ ] | Bongo Cat (STEAM) | 15 | 20 | 75% (last 20) | Does not open (71%) | 76% | 5d ago | n/a | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 257 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 13 | 20 | 65% (last 20) | No graphics (37%) | 83% | today | n/a | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 258 | [ ] | PAYDAY: The Heist (STEAM) | 13 | 20 | 65% (last 20) | Does not open (75%) | 70% | 4d ago | n/a |  |
| 259 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (100%) | 77% | 6d ago | n/a |  |
| 260 | [ ] | 12 is Better Than 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (45%) | 85% | 6d ago | n/a |  |
| 261 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 95% | 3d ago | n/a |  |
| 262 | [ ] | Big Walk (STEAM) | 11 | 20 | 55% (last 20) | Does not open (65%) | 74% | 8d ago | n/a |  |
| 263 | [ ] | Hitman: Absolution (GOG) | 11 | 20 | 55% (last 20) | Does not open (85%) | 77% | 5d ago | n/a |  |
| 264 | [ ] | Hero Siege (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (50%) | 68% | today | n/a |  |
| 265 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 76% | 4d ago | n/a |  |
| 266 | [ ] | Bodycam (STEAM) | 15 | 20 | 75% (last 20) | Does not open (55%) | 90% | today | n/a |  |
| 267 | [ ] | Tales of Zestiria (STEAM) | 14 | 20 | 70% (last 20) | Does not open (80%) | 64% | 16d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 268 | [ ] | Capcom Fighting Collection (STEAM) | 14 | 20 | 70% (last 20) | Does not open (76%) | 77% | 2d ago | n/a | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 269 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (95%) | 95% | 2d ago | 88% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 270 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (45%) | 68% | 6d ago | n/a |  |
| 271 | [ ] | Disgaea 4 Complete+ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (43%) | 92% | 10d ago | n/a | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 272 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 12 | 20 | 60% (last 20) | Does not open (57%) | 75% | 6d ago | n/a | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 273 | [ ] | Hatred (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 89% | 3d ago | n/a |  |
| 274 | [ ] | Football Manager 2024 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (91%) | 76% | 3d ago | n/a |  |
| 275 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 98% | 2d ago | 89% |  |
| 276 | [ ] | Sacred Gold (STEAM) | 16 | 20 | 80% (last 20) | Does not open (92%) | 70% | 11d ago | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 277 | [ ] | Chef Knight (STEAM) | 14 | 20 | 70% (last 20) | Does not open (100%) | 64% | 15d ago | n/a |  |
| 278 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 14 | 20 | 70% (last 20) | Does not open (85%) | 67% | 3d ago | n/a | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 279 | [ ] | Timberborn (STEAM) | 13 | 20 | 65% (last 20) | No graphics (62%) | 84% | 8d ago | n/a |  |
| 280 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (89%) | 82% | 3d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 281 | [ ] | Mortal Shell (EPIC) | 13 | 20 | 65% (last 20) | No graphics (70%) | 74% | 1d ago | n/a |  |
| 282 | [ ] | Allumeria (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 69% | 1d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 283 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 76% | 1d ago | n/a |  |
| 284 | [ ] | Sons Of The Forest (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 74% | 4d ago | n/a |  |
| 285 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (77%) | 83% | 24d ago | n/a |  |
| 286 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 67% | 2d ago | 60% |  |
| 287 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 60% | 5d ago | 60% |  |
| 288 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | Does not open (42%) | 77% | 3d ago | n/a | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 289 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 88% | 3d ago | n/a |  |
| 290 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 74% | 2d ago | 64% |  |
| 291 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (42%) | 88% | 9d ago | 100% |  |
| 292 | [ ] | MX Bikes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 94% | 2d ago | n/a |  |
| 293 | [ ] | Spark the Electric Jester (STEAM) | 14 | 20 | 70% (last 20) | Does not open (62%) | 62% | 6d ago | n/a | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 294 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (58%) | 60% | 8d ago | n/a |  |
| 295 | [ ] | Hylics (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 97% | 8d ago | n/a |  |
| 296 | [ ] | Antichamber (STEAM) | 11 | 20 | 55% (last 20) | Does not open (33%) | 90% | today | n/a |  |
| 297 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (57%) | 91% | 1d ago | n/a |  |
| 298 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | No graphics (68%) | 75% | today | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 299 | [ ] | Monster Boy And The Cursed Kingdom (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (84%) | 89% | 11d ago | n/a |  |
| 300 | [ ] | This War of Mine (STEAM) | 10 | 20 | 50% (last 20) | No graphics (53%) | 64% | 11d ago | 36% (drop) |  |
| 301 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 67% | 27d ago | n/a |  |
| 302 | [ ] | Katanaut (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | 69% | 5d ago | n/a | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 303 | [ ] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 63% | 9d ago | n/a | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 304 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 60% | 1d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 305 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | 83% | 5d ago | n/a |  |
| 306 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 81% | 39d ago | n/a |  |
| 307 | [ ] | AER Memories of Old (EPIC) | 12 | 20 | 60% (last 20) | Does not open (91%) | 93% | 14d ago | n/a |  |
| 308 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (92%) | 89% | 6d ago | n/a |  |
| 309 | [ ] | Gloomwood (STEAM) | 11 | 20 | 55% (last 20) | No graphics (53%) | 69% | 2d ago | n/a |  |
| 310 | [ ] | LET IT DIE (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 62% | 5d ago | n/a |  |
| 311 | [ ] | Assassin's Creed Odyssey (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 69% | 4d ago | n/a | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 312 | [ ] | Pinball FX Classic (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | 95% | 6d ago | n/a |  |
| 313 | [ ] | Intravenous (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 77% | 2d ago | n/a |  |
| 314 | [ ] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 20 | 65% (last 20) | Does not open (82%) | 88% | 7d ago | n/a |  |
| 315 | [ ] | Ghostwire Tokyo (EPIC) | 13 | 20 | 65% (last 20) | Does not open (88%) | 79% | today | n/a |  |
| 316 | [ ] | Need for Speed™ Unbound (STEAM) | 12 | 20 | 60% (last 20) | Does not open (87%) | 67% | 14d ago | n/a | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 317 | [ ] | Legend of Grimrock 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 83% | 4d ago | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 318 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (56%) | 92% | 13d ago | n/a | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 319 | [ ] | GRANDIA II HD Remaster (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 62% | 14d ago | n/a |  |
| 320 | [ ] | Killing Floor (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (100%) | 85% | 3d ago | n/a |  |
| 321 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 81% | 1d ago | 70% |  |
| 322 | [ ] | Subnautica: Below Zero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 70% | 2d ago | n/a |  |
| 323 | [ ] | Castle in the Clouds (STEAM) | 10 | 20 | 50% (last 20) | No graphics (63%) | 82% | 11d ago | n/a |  |
| 324 | [ ] | Shift At Midnight (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | 79% | 5d ago | n/a |  |
| 325 | [ ] | Batman™: Arkham Origins (GOG) | 11 | 20 | 55% (last 20) | Does not open (67%) | 100% | 28d ago | n/a |  |
| 326 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 66% | 4d ago | n/a |  |
| 327 | [ ] | Haydee (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 78% | 5d ago | n/a |  |
| 328 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 76% | 4d ago | n/a |  |
| 329 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 87% | 1d ago | 80% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 330 | [ ] | Forgive Me Father (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 64% | 3d ago | n/a |  |
| 331 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 67% | 2d ago | n/a | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 332 | [ ] | GRIP (GOG) | 12 | 20 | 60% (last 20) | Does not open (92%) | 100% | 1d ago | n/a |  |
| 333 | [ ] | Turbo Overkill (STEAM) | 12 | 20 | 60% (last 20) | No graphics (100%) | 95% | 3d ago | n/a |  |
| 334 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (69%) | 92% | 3d ago | 92% |  |
| 335 | [ ] | Ultrapool (STEAM) | 10 | 20 | 50% (last 20) | Does not open (54%) | 100% | 2d ago | n/a |  |
| 336 | [ ] | WORLD OF FINAL FANTASY (STEAM) | 10 | 20 | 50% (last 20) | No graphics (58%) | 76% | 4d ago | n/a |  |
| 337 | [ ] | Dungeon Siege (STEAM) | 10 | 20 | 50% (last 20) | Does not open (38%) | 85% | 8d ago | n/a |  |
| 338 | [ ] | Cruelty Squad (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | 94% | 8d ago | n/a |  |
| 339 | [ ] | NiGHTS into Dreams... (STEAM) | 10 | 20 | 50% (last 20) | Does not open (44%) | 75% | 7d ago | n/a |  |
| 340 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 91% | 12d ago | n/a |  |
| 341 | [ ] | Sid Meier's Civilization VI (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 83% | 8d ago | n/a |  |
| 342 | [ ] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (67%) | 94% | 7d ago | n/a |  |
| 343 | [ ] | Beatblock (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 92% | 2d ago | n/a |  |

## Recently recovered (487)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Slay the Spire (STEAM) | 1312 | 2026-11-09 | 1645 | 64% | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [x] | Grim Dawn (STEAM) | 532 | 2026-11-08 | 591 | 61% |  |
| 3 | [x] | FINAL FANTASY RESONANCE (STEAM) | 394 | 2026-10-24 | 891 | 76% |  |
| 4 | [x] | Half-Life (STEAM) | 347 | 2026-11-09 | 614 | 71% |  |
| 5 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 238 | 2026-10-19 | 295 | 74% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 6 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 237 | 2026-11-09 | 282 | 66% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 7 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 228 | 2026-11-09 | 320 | 90% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 8 | [x] | MONSTER HUNTER RISE (STEAM) | 209 | 2026-11-09 | 506 | 63% |  |
| 9 | [x] | BeamNG.drive (STEAM) | 203 | 2026-11-09 | 244 | 86% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 10 | [x] | Devil May Cry HD Collection (STEAM) | 200 | 2026-10-19 | 287 | 80% |  |
| 11 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 198 | 2026-11-09 | 358 | 77% |  |
| 12 | [x] | OMORI (STEAM) | 191 | 2026-11-09 | 235 | 74% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 13 | [x] | DRAGON BALL FighterZ (STEAM) | 185 | 2026-11-01 | 220 | 72% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 14 | [x] | Spelunky 2 (STEAM) | 180 | 2026-11-01 | 213 | 67% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 15 | [x] | DREDGE (EPIC) | 173 | 2026-11-09 | 216 | 76% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 16 | [x] | Rocket League® (EPIC) | 171 | 2026-11-09 | 276 | 64% | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 17 | [x] | Sid Meier's Civilization V (STEAM) | 169 | 2026-11-10 | 180 | 63% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 18 | [x] | BioShock (STEAM) | 153 | 2026-11-09 | 293 | 75% |  |
| 19 | [x] | Geometry Dash (STEAM) | 146 | 2026-11-11 | 437 | 46% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 20 | [x] | Prototype (STEAM) | 141 | 2026-11-11 | 203 | 55% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 21 | [x] | Burnout Paradise: The Ultimate Box (STEAM) | 137 | 2026-10-16 | 237 | 74% |  |
| 22 | [x] | Castlevania Advance Collection (STEAM) | 133 | 2026-11-09 | 205 | 91% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 23 | [x] | Team Fortress 2 (STEAM) | 132 | 2026-11-09 | 228 | 76% |  |
| 24 | [x] | Counter-Strike (STEAM) | 130 | 2026-11-11 | 210 | 45% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 25 | [x] | Mirror's Edge (STEAM) | 129 | 2026-11-09 | 181 | 72% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 26 | [x] | Minecraft Dungeons II (STEAM) | 128 | 2026-11-09 | 147 | 66% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 27 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 127 | 2026-11-09 | 166 | 69% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 28 | [x] | Far Cry® 3 (STEAM) | 125 | 2026-11-09 | 140 | 64% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 29 | [x] | Caravan SandWitch (EPIC) | 122 | 2026-11-09 | 190 | 68% |  |
| 30 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 122 | 2026-10-18 | 177 | 78% |  |
| 31 | [x] | Call of Duty: Black Ops III (STEAM) | 121 | 2026-10-18 | 252 | 77% |  |
| 32 | [x] | Assassin's Creed II (STEAM) | 120 | 2026-11-10 | 125 | 62% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 33 | [x] | Euro Truck Simulator 2 (STEAM) | 116 | 2026-11-10 | 215 | 55% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 34 | [x] | The Witcher: Enhanced Edition (STEAM) | 113 | 2026-11-09 | 132 | 68% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 35 | [x] | Cave Story+ (STEAM) | 112 | 2026-11-09 | 124 | 86% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 36 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 108 | 2026-11-09 | 145 | 88% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 37 | [x] | Aniimo (STEAM) | 107 | 2026-11-09 | 146 | 86% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 38 | [x] | Moonstone Island (STEAM) | 98 | 2026-11-09 | 131 | 85% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 39 | [x] | Happy Wheels (STEAM) | 97 | 2026-11-09 | 117 | 71% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 40 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 94 | 2026-11-09 | 148 | 71% |  |
| 41 | [x] | Catherine Classic (STEAM) | 91 | 2026-11-09 | 171 | 73% |  |
| 42 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 89 | 2026-11-09 | 114 | 93% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 43 | [x] | Quake (STEAM) | 88 | 2026-11-09 | 262 | 84% |  |
| 44 | [x] | Hi-Fi RUSH (STEAM) | 88 | 2026-11-11 | 122 | 47% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 45 | [x] | Fallout: New Vegas PCR (STEAM) | 87 | 2026-11-09 | 117 | 61% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 46 | [x] | Vital Shell (STEAM) | 86 | 2026-11-09 | 131 | 85% |  |
| 47 | [x] | DOOM 3: BFG Edition (STEAM) | 85 | 2026-11-09 | 124 | 71% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 48 | [x] | Cry of Fear (STEAM) | 84 | 2026-10-18 | 165 | 78% |  |
| 49 | [x] | Ultra Street Fighter IV (STEAM) | 83 | 2026-10-17 | 180 | 67% |  |
| 50 | [x] | FINAL FANTASY XIII-2 (STEAM) | 81 | 2026-11-09 | 84 | 61% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 51 | [x] | Psychonauts (STEAM) | 80 | 2026-11-09 | 144 | 95% |  |
| 52 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 80 | 2026-10-18 | 134 | 96% |  |
| 53 | [x] | Age of Empires II: Definitive Edition (STEAM) | 80 | 2026-11-10 | 95 | 64% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 54 | [x] | STEINS;GATE (STEAM) | 79 | 2026-11-09 | 111 | 91% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 55 | [x] | Brawlhalla (STEAM) | 76 | 2026-11-09 | 149 | 74% |  |
| 56 | [x] | Don't Starve Together (STEAM) | 75 | 2026-10-16 | 157 | 80% |  |
| 57 | [x] | Ballionaire (STEAM) | 74 | 2026-11-09 | 118 | 89% |  |
| 58 | [x] | Sovereign Tower (STEAM) | 73 | 2026-11-09 | 127 | 81% |  |
| 59 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 73 | 2026-11-09 | 108 | 85% |  |
| 60 | [x] | Disgaea 5 Complete (STEAM) | 71 | 2026-11-09 | 83 | 92% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 61 | [x] | Spyro™ Reignited Trilogy (STEAM) | 70 | 2026-11-09 | 108 | 72% |  |
| 62 | [x] | Need for Speed: Hot Pursuit (STEAM) | 70 | 2026-11-09 | 104 | 79% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 63 | [x] | Bayonetta (STEAM) | 68 | 2026-10-18 | 207 | 82% |  |
| 64 | [x] | Dota 2 (STEAM) | 68 | 2026-11-09 | 102 | 74% |  |
| 65 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 68 | 2026-11-11 | 92 | 60% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 66 | [x] | The Sims™ 4 (STEAM) | 68 | 2026-11-09 | 88 | 71% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 67 | [x] | Stardew Valley (GOG) | 67 | 2026-11-11 | 119 | 61% |  |
| 68 | [x] | American Truck Simulator (STEAM) | 67 | 2026-11-09 | 111 | 80% |  |
| 69 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 67 | 2026-11-09 | 100 | 80% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 70 | [x] | Diablo® IV (STEAM) | 67 | 2026-11-11 | 79 | 60% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 71 | [x] | MIO: Memories in Orbit (STEAM) | 66 | 2026-11-09 | 123 | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 72 | [x] | Call of Juarez Gunslinger (STEAM) | 66 | 2026-11-09 | 81 | 73% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 73 | [x] | Hogwarts Legacy (EPIC) | 65 | 2026-11-09 | 99 | 68% |  |
| 74 | [x] | Cyberpunk 2077 (GOG) | 65 | 2026-11-09 | 83 | 72% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 75 | [x] | Fable - The Lost Chapters (STEAM) | 64 | 2026-11-09 | 101 | 82% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 76 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 64 | 2026-11-11 | 80 | 47% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 77 | [x] | Gunfire Reborn (STEAM) | 64 | 2026-11-09 | 70 | 94% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 78 | [x] | Don't Starve (STEAM) | 63 | 2026-10-16 | 154 | 78% |  |
| 79 | [x] | Firewatch (STEAM) | 63 | 2026-11-10 | 118 | 60% |  |
| 80 | [x] | Fallout (STEAM) | 63 | 2026-11-09 | 98 | 71% |  |
| 81 | [x] | Order of the Sinking Star (STEAM) | 63 | 2026-11-09 | 90 | 60% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 82 | [x] | Poppy Playtime (STEAM) | 62 | 2026-11-09 | 108 | 73% |  |
| 83 | [x] | Borderlands: The Pre-Sequel (STEAM) | 62 | 2026-11-09 | 91 | 63% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 84 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 62 | 2026-11-09 | 86 | 82% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 85 | [x] | Hollow Knight: Silksong (GOG) | 61 | 2026-11-10 | 99 | 61% |  |
| 86 | [x] | Sol Cesto (EPIC) | 61 | 2026-11-09 | 63 | 67% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 87 | [x] | eFootball™ (STEAM) | 60 | 2026-11-09 | 89 | 69% |  |
| 88 | [x] | Borderlands 3 (STEAM) | 60 | 2026-11-09 | 83 | 91% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 89 | [x] | Darksiders (STEAM) | 59 | 2026-11-09 | 74 | 81% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 90 | [x] | Deskrawl: Idle ARPG (STEAM) | 58 | 2026-11-09 | 72 | 88% | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 91 | [x] | A Plague Tale: Innocence (STEAM) | 58 | 2026-11-09 | 61 | 83% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 92 | [x] | Mini Motorways (STEAM) | 57 | 2026-11-09 | 97 | 68% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 93 | [x] | Until Then (STEAM) | 56 | 2026-10-17 | 94 | 83% |  |
| 94 | [x] | TBH: Task Bar Hero (STEAM) | 56 | 2026-11-09 | 90 | 86% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 95 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 56 | 2026-11-09 | 87 | 94% |  |
| 96 | [x] | Call of Duty: World at War (STEAM) | 56 | 2026-11-09 | 80 | 86% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 97 | [x] | Sonic Generations (STEAM) | 56 | 2026-11-09 | 64 | 66% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 98 | [x] | Starbound (STEAM) | 55 | 2026-11-09 | 86 | 76% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 99 | [x] | Dead Space (STEAM) | 55 | 2026-10-18 | 69 | 81% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 100 | [x] | Overwatch® (STEAM) | 55 | 2026-11-10 | 58 | 59% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 101 | [x] | Alex Kidd in Miracle World DX (EPIC) | 53 | 2026-11-09 | 61 | 74% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 102 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 52 | 2026-10-25 | 100 | 62% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 103 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 52 | 2026-11-09 | 87 | 64% |  |
| 104 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 52 | 2026-11-09 | 85 | 61% |  |
| 105 | [x] | Grand Theft Auto V (EPIC) | 52 | 2026-11-09 | 58 | 75% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 106 | [x] | Sonic Adventure DX (STEAM) | 51 | 2026-10-17 | 89 | 65% |  |
| 107 | [x] | A Plague Tale: Innocence (EPIC) | 51 | 2026-11-09 | 87 | 61% |  |
| 108 | [x] | Oxygen Not Included (STEAM) | 50 | 2026-11-11 | 84 | 61% |  |
| 109 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 50 | 2026-11-09 | 78 | 81% |  |
| 110 | [x] | Vampire Survivors (EPIC) | 50 | 2026-11-09 | 73 | 61% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 111 | [x] | Last Epoch (STEAM) | 50 | 2026-11-09 | 73 | 93% |  |
| 112 | [x] | Deadlock (STEAM) | 50 | 2026-10-16 | 69 | 89% |  |
| 113 | [x] | Darkest Dungeon® (EPIC) | 49 | 2026-11-09 | 89 | 78% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 114 | [x] | Big Walk (STEAM) | 49 | 2026-11-09 | 78 | 74% |  |
| 115 | [x] | MudRunner (STEAM) | 48 | 2026-10-24 | 104 | 62% |  |
| 116 | [x] | Okami HD (STEAM) | 48 | 2026-11-09 | 92 | 91% |  |
| 117 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 48 | 2026-10-19 | 92 | 70% |  |
| 118 | [x] | Abiotic Factor (STEAM) | 48 | 2026-10-18 | 82 | 66% |  |
| 119 | [x] | Heroes of Might & Magic III - HD Edition (STEAM) | 48 | 2026-11-11 | 62 | 62% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 120 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 47 | 2026-11-09 | 80 | 84% |  |
| 121 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 2026-11-09 | 74 | 92% |  |
| 122 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 47 | 2026-11-09 | 54 | 89% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 123 | [x] | Rivals of Aether II (STEAM) | 46 | 2026-11-09 | 65 | 69% | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 124 | [x] | Sheepy: A Short Adventure (STEAM) | 46 | 2026-11-09 | 56 | 82% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 125 | [x] | Ace Attorney Investigations Collection (STEAM) | 45 | 2026-11-09 | 75 | 90% |  |
| 126 | [x] | Moonlighter (EPIC) | 45 | 2026-11-09 | 49 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 127 | [x] | Sonic Origins (STEAM) | 43 | 2026-11-09 | 74 | 83% |  |
| 128 | [x] | Guildrun Demo (STEAM) | 43 | 2026-11-09 | 60 | 75% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 129 | [x] | Tomb Raider GOTY (GOG) | 42 | 2026-10-17 | 98 | 95% |  |
| 130 | [x] | PROTOTYPE 2 (STEAM) | 42 | 2026-10-18 | 88 | 71% |  |
| 131 | [x] | The Bazaar (STEAM) | 42 | 2026-11-09 | 71 | 83% |  |
| 132 | [x] | Frostpunk (STEAM) | 42 | 2026-11-09 | 66 | 68% |  |
| 133 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 42 | 2026-11-09 | 63 | 74% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 134 | [x] | Sonic Lost World (STEAM) | 42 | 2026-11-09 | 60 | 82% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 135 | [x] | Aggelos (STEAM) | 42 | 2026-11-09 | 56 | 100% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 136 | [x] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 42 | 2026-11-09 | 47 | 80% | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 137 | [x] | Rayman Origins (STEAM) | 41 | 2026-10-17 | 93 | 87% |  |
| 138 | [x] | Tomb Raider: Anniversary (STEAM) | 41 | 2026-11-09 | 64 | 68% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 139 | [x] | FINAL FANTASY VII (2013) (STEAM) | 41 | 2026-11-09 | 59 | 77% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 140 | [x] | Digimon World: Next Order (STEAM) | 40 | 2026-11-09 | 78 | 90% |  |
| 141 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 40 | 2026-11-09 | 41 | 83% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 142 | [x] | Life is Strange™ (STEAM) | 39 | 2026-10-17 | 83 | 80% |  |
| 143 | [x] | Library Of Ruina (STEAM) | 39 | 2026-10-16 | 75 | 86% |  |
| 144 | [x] | Forza Horizon 4 (STEAM) | 39 | 2026-11-09 | 54 | 67% | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 145 | [x] | Capcom Arcade Stadium (STEAM) | 39 | 2026-11-09 | 48 | 71% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 146 | [x] | Dead by Daylight (STEAM) | 39 | 2026-11-09 | 43 | 82% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 147 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-11-09 | 40 | 75% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 148 | [x] | Death Road to Canada (STEAM) | 38 | 2026-10-17 | 95 | 77% |  |
| 149 | [x] | Amnesia: The Dark Descent (STEAM) | 38 | 2026-11-09 | 73 | 72% |  |
| 150 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 38 | 2026-11-09 | 71 | 95% |  |
| 151 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 38 | 2026-11-09 | 70 | 86% |  |
| 152 | [x] | Rogue Legacy (STEAM) | 37 | 2026-10-17 | 87 | 79% |  |
| 153 | [x] | Tales of ARISE (STEAM) | 37 | 2026-10-16 | 78 | 87% |  |
| 154 | [x] | CrossCode (GOG) | 37 | 2026-11-09 | 40 | 67% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 155 | [x] | Cobalt Core (STEAM) | 36 | 2026-10-18 | 89 | 87% |  |
| 156 | [x] | Age of Empires II (2013) (STEAM) | 36 | 2026-11-09 | 62 | 67% |  |
| 157 | [x] | Street Fighter™ 6 (STEAM) | 36 | 2026-11-09 | 62 | 81% |  |
| 158 | [x] | POSTAL 2 (GOG) | 35 | 2026-11-09 | 70 | 92% |  |
| 159 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 35 | 2026-11-09 | 61 | 74% |  |
| 160 | [x] | Rocket League (STEAM) | 35 | 2026-10-17 | 59 | 70% |  |
| 161 | [x] | XCOM 2 (STEAM) | 35 | 2026-11-09 | 59 | 100% |  |
| 162 | [x] | Elite Dangerous (STEAM) | 35 | 2026-11-09 | 38 | 69% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 163 | [x] | Teardown (STEAM) | 34 | 2026-10-17 | 79 | 81% |  |
| 164 | [x] | Little Nightmares (STEAM) | 34 | 2026-10-16 | 75 | 67% |  |
| 165 | [x] | Salt and Sanctuary (STEAM) | 34 | 2026-10-18 | 74 | 84% |  |
| 166 | [x] | Journey (STEAM) | 34 | 2026-10-27 | 73 | 66% |  |
| 167 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 34 | 2026-11-09 | 68 | 84% |  |
| 168 | [x] | SurrounDead (STEAM) | 34 | 2026-11-09 | 66 | 95% |  |
| 169 | [x] | Deponia (STEAM) | 34 | 2026-11-09 | 62 | 58% |  |
| 170 | [x] | Hero Siege (STEAM) | 34 | 2026-11-09 | 57 | 68% |  |
| 171 | [x] | Need for Speed™ Rivals (STEAM) | 34 | 2026-11-10 | 47 | 68% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 172 | [x] | Romestead (STEAM) | 34 | 2026-11-09 | 45 | 68% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 173 | [x] | Russian Fishing 4 (STEAM) | 34 | 2026-11-09 | 40 | 89% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 174 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 33 | 2026-11-09 | 68 | 66% |  |
| 175 | [x] | Ultimate Chicken Horse (STEAM) | 33 | 2026-10-23 | 68 | 75% |  |
| 176 | [x] | Hearts of Iron IV (STEAM) | 33 | 2026-11-09 | 60 | 69% |  |
| 177 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 2026-11-09 | 53 | 89% |  |
| 178 | [x] | Gauntlet™  (STEAM) | 33 | 2026-11-11 | 47 | 43% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 179 | [x] | SnowRunner (STEAM) | 33 | 2026-11-09 | 47 | 79% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 180 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 33 | 2026-11-09 | 44 | 92% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 181 | [x] | Super Animal Royale (STEAM) | 33 | 2026-11-09 | 44 | 63% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 182 | [x] | Dishonored - Definitive Edition (EPIC) | 32 | 2026-10-17 | 79 | 80% |  |
| 183 | [x] | Sable (EPIC) | 32 | 2026-10-18 | 71 | 65% |  |
| 184 | [x] | State of Decay: Year-One (STEAM) | 32 | 2026-10-18 | 65 | 76% |  |
| 185 | [x] | Mortal Kombat X (STEAM) | 32 | 2026-10-17 | 64 | 85% |  |
| 186 | [x] | COCOON (STEAM) | 32 | 2026-11-09 | 62 | 86% |  |
| 187 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 32 | 2026-11-11 | 59 | 37% |  |
| 188 | [x] | Max Payne (STEAM) | 32 | 2026-11-09 | 57 | 89% |  |
| 189 | [x] | Counter-Strike:Global Offensive (STEAM) | 32 | 2026-11-09 | 52 | 79% |  |
| 190 | [x] | Earthion (STEAM) | 32 | 2026-11-09 | 52 | 100% |  |
| 191 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-11-09 | 42 | 82% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 192 | [x] | BioShock™ (GOG) | 31 | 2026-10-18 | 67 | 79% |  |
| 193 | [x] | Stumble Guys (STEAM) | 31 | 2026-10-18 | 61 | 73% |  |
| 194 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 31 | 2026-11-09 | 49 | 89% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 195 | [x] | Nioh: Complete Edition (STEAM) | 31 | 2026-11-09 | 42 | 92% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 196 | [x] | Bloodstained: Curse of the Moon (STEAM) | 30 | 2026-10-16 | 74 | 72% |  |
| 197 | [x] | Torchlight II (STEAM) | 30 | 2026-10-20 | 69 | 88% |  |
| 198 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 30 | 2026-11-09 | 60 | 83% |  |
| 199 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 30 | 2026-11-09 | 50 | 66% |  |
| 200 | [x] | Sol Cesto (STEAM) | 30 | 2026-11-11 | 48 | 64% |  |
| 201 | [x] | Yakuza: Like a Dragon (STEAM) | 30 | 2026-11-09 | 48 | 66% |  |
| 202 | [x] | Capcom Fighting Collection 2 (STEAM) | 30 | 2026-11-09 | 47 | 75% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 203 | [x] | Supermarket Together (STEAM) | 30 | 2026-11-09 | 42 | 62% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 204 | [x] | Red Dead Redemption (STEAM) | 30 | 2026-11-09 | 33 | 72% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 205 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 29 | 2026-11-09 | 58 | 91% |  |
| 206 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 2026-10-17 | 53 | 82% |  |
| 207 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 29 | 2026-11-09 | 53 | 64% |  |
| 208 | [x] | Aethermancer (STEAM) | 29 | 2026-10-18 | 52 | 85% |  |
| 209 | [x] | Prince of Persia: The Sands of Time (STEAM) | 29 | 2026-11-09 | 51 | 88% |  |
| 210 | [x] | Heavy Rain (STEAM) | 29 | 2026-11-09 | 49 | 92% |  |
| 211 | [x] | Secrets of Grindea (STEAM) | 29 | 2026-11-09 | 47 | 71% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 212 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 62% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 213 | [x] | Subnautica 2 (STEAM) | 29 | 2026-11-10 | 34 | 62% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 214 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 28 | 2026-10-19 | 95 | 92% |  |
| 215 | [x] | Grand Theft Auto III (STEAM) | 28 | 2026-10-17 | 74 | 78% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 216 | [x] | Resident Evil Village (STEAM) | 28 | 2026-11-09 | 51 | 91% |  |
| 217 | [x] | Binary Domain (STEAM) | 28 | 2026-11-09 | 43 | 64% |  |
| 218 | [x] | Tower and Sword of Succubus (STEAM) | 28 | 2026-11-09 | 43 | 86% |  |
| 219 | [x] | Palia (STEAM) | 28 | 2026-11-09 | 40 | 75% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 220 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 28 | 2026-11-09 | 32 | 77% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 221 | [x] | Skullgirls 2nd Encore (STEAM) | 27 | 2026-11-10 | 63 | 59% |  |
| 222 | [x] | Soul's Remnant (STEAM) | 27 | 2026-11-11 | 49 | n/a |  |
| 223 | [x] | Gambonanza (STEAM) | 27 | 2026-11-09 | 44 | 95% |  |
| 224 | [x] | Dead Rising 2 (STEAM) | 27 | 2026-11-09 | 43 | 68% |  |
| 225 | [x] | Return to Monkey Island (STEAM) | 27 | 2026-11-09 | 40 | 82% |  |
| 226 | [x] | Gothic II: Gold Classic (STEAM) | 27 | 2026-11-09 | 37 | 70% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 227 | [x] | Ultimate Custom Night (STEAM) | 27 | 2026-11-09 | 37 | 71% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 228 | [x] | CRUEL (STEAM) | 27 | 2026-11-09 | 33 | 70% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 229 | [x] | Dying Light (EPIC) | 26 | 2026-10-17 | 62 | 79% |  |
| 230 | [x] | Monster Hunter Stories (STEAM) | 26 | 2026-10-17 | 61 | 85% |  |
| 231 | [x] | PlateUp! (STEAM) | 26 | 2026-10-16 | 56 | 87% |  |
| 232 | [x] | G.I. Joe Wrath of Cobra (EPIC) | 26 | 2026-11-09 | 47 | 71% |  |
| 233 | [x] | Unturned (STEAM) | 26 | 2026-11-09 | 46 | 72% |  |
| 234 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 45 | 64% |  |
| 235 | [x] | Counter-Strike: Condition Zero (STEAM) | 26 | 2026-11-11 | 44 | 42% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 236 | [x] | Digimon Survive (STEAM) | 26 | 2026-11-09 | 39 | 96% |  |
| 237 | [x] | Ratatan (STEAM) | 26 | 2026-11-09 | 38 | 98% |  |
| 238 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 26 | 2026-11-09 | 36 | 91% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 239 | [x] | Bongo Cat (STEAM) | 26 | 2026-11-09 | 34 | 76% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 240 | [x] | Path of Exile 2 (STEAM) | 26 | 2026-11-09 | 33 | 68% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 241 | [x] | Tales of Zestiria (STEAM) | 26 | 2026-11-09 | 32 | 64% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 242 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 26 | 2026-11-09 | 30 | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 243 | [x] | Being a DIK (STEAM) | 25 | 2026-11-09 | 46 | 67% |  |
| 244 | [x] | Battle Brothers (STEAM) | 25 | 2026-11-09 | 42 | 74% |  |
| 245 | [x] | Opus Magnum (STEAM) | 25 | 2026-11-09 | 40 | 88% |  |
| 246 | [x] | Deus Ex™ GOTY Edition (GOG) | 25 | 2026-11-09 | 39 | 88% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 247 | [x] | Limbus Company (STEAM) | 25 | 2026-11-09 | 38 | 79% |  |
| 248 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 25 | 2026-11-09 | 36 | 72% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 249 | [x] | Crab Game (STEAM) | 25 | 2026-11-09 | 33 | 95% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 250 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-09 | 32 | 92% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 251 | [x] | Northgard: Definitive Edition (STEAM) | 25 | 2026-11-09 | 28 | 80% | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 252 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 57 | 92% |  |
| 253 | [x] | Resident Evil Revelations 2 (STEAM) | 24 | 2026-11-09 | 48 | 84% |  |
| 254 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 24 | 2026-11-09 | 46 | 97% |  |
| 255 | [x] | Prince of Persia (GOG) | 24 | 2026-11-09 | 42 | 93% |  |
| 256 | [x] | Worms W.M.D (STEAM) | 24 | 2026-11-09 | 41 | 90% |  |
| 257 | [x] | Moonlight Peaks (STEAM) | 24 | 2026-11-09 | 36 | 85% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 258 | [x] | Borderlands: The Pre-Sequel (EPIC) | 24 | 2026-11-09 | 34 | 75% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 259 | [x] | Jade Empire: Special Edition (GOG) | 24 | 2026-11-09 | 31 | 78% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 260 | [x] | Tearscape (STEAM) | 24 | 2026-11-09 | 29 | 94% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 261 | [x] | Jade Empire: Special Edition (STEAM) | 24 | 2026-11-09 | 27 | 71% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 262 | [x] | The Lantern of the Laughless Saint (STEAM) | 24 | 2026-11-09 | 25 | 64% | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 263 | [x] | Owlboy (STEAM) | 23 | 2026-11-02 | 55 | 63% |  |
| 264 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 23 | 2026-10-20 | 51 | 84% |  |
| 265 | [x] | WEBFISHING (STEAM) | 23 | 2026-10-17 | 49 | 89% |  |
| 266 | [x] | Chained Echoes (GOG) | 23 | 2026-11-08 | 48 | 65% |  |
| 267 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 46 | 89% |  |
| 268 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-11-09 | 44 | 90% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 269 | [x] | Football Manager 2024 (EPIC) | 23 | 2026-11-09 | 41 | 76% |  |
| 270 | [x] | Wizard of Legend (EPIC) | 23 | 2026-11-09 | 41 | 83% |  |
| 271 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 23 | 2026-11-09 | 41 | 83% |  |
| 272 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 2026-11-09 | 36 | 77% |  |
| 273 | [x] | Timberborn (STEAM) | 23 | 2026-11-09 | 34 | 84% |  |
| 274 | [x] | Beyond: Two Souls (STEAM) | 23 | 2026-11-09 | 31 | 69% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 275 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 95% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 276 | [x] | CarX Drift Racing Online (STEAM) | 22 | 2026-10-16 | 57 | 79% |  |
| 277 | [x] | Goat Simulator (STEAM) | 22 | 2026-11-09 | 45 | 77% |  |
| 278 | [x] | Crazy Taxi (STEAM) | 22 | 2026-11-10 | 42 | 62% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 279 | [x] | Pinball FX Classic (STEAM) | 22 | 2026-11-09 | 40 | 95% |  |
| 280 | [x] | SWORN (STEAM) | 22 | 2026-11-09 | 38 | 95% |  |
| 281 | [x] | Trailmakers (STEAM) | 22 | 2026-11-09 | 38 | 89% |  |
| 282 | [x] | Cat Mail Co. (STEAM) | 22 | 2026-11-09 | 37 | 90% |  |
| 283 | [x] | Tabletop Simulator (STEAM) | 22 | 2026-11-09 | 36 | 64% |  |
| 284 | [x] | Life is Strange Remastered (STEAM) | 22 | 2026-11-09 | 34 | 89% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 285 | [x] | Dishonored 2 (STEAM) | 22 | 2026-11-09 | 32 | 85% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 286 | [x] | SOMA (STEAM) | 22 | 2026-11-09 | 32 | 60% | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 287 | [x] | CarX Street (STEAM) | 22 | 2026-11-09 | 28 | 100% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 288 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 60 | 97% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 289 | [x] | Slow Roads (STEAM) | 21 | 2026-10-22 | 46 | 88% |  |
| 290 | [x] | MudRunner (EPIC) | 21 | 2026-10-18 | 44 | 79% |  |
| 291 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 21 | 2026-11-11 | 41 | 45% |  |
| 292 | [x] | Lucid Blocks (STEAM) | 21 | 2026-11-09 | 41 | 65% |  |
| 293 | [x] | Control Ultimate Edition (GOG) | 21 | 2026-11-09 | 39 | 88% |  |
| 294 | [x] | This War of Mine (STEAM) | 21 | 2026-11-09 | 38 | 64% |  |
| 295 | [x] | Invisible, Inc. (STEAM) | 21 | 2026-11-09 | 37 | 71% |  |
| 296 | [x] | Brothers - A Tale of Two Sons (EPIC) | 21 | 2026-11-09 | 36 | 67% |  |
| 297 | [x] | My Summer Car (STEAM) | 21 | 2026-11-09 | 36 | 80% |  |
| 298 | [x] | Sapphire Safari (GOG) | 21 | 2026-11-09 | 28 | 82% | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 299 | [x] | Saints Row IV (STEAM) | 20 | 2026-10-19 | 50 | 83% |  |
| 300 | [x] | ABZÛ (STEAM) | 20 | 2026-10-21 | 48 | 97% |  |
| 301 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-11-09 | 39 | 100% |  |
| 302 | [x] | GOD EATER RESURRECTION (STEAM) | 20 | 2026-11-09 | 31 | 68% |  |
| 303 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 20 | 2026-11-09 | 30 | 87% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 304 | [x] | Metro Exodus (STEAM) | 20 | 2026-11-09 | 29 | 89% |  |
| 305 | [x] | Party Animals (STEAM) | 20 | 2026-11-09 | 29 | 70% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 306 | [x] | Torchlight II (EPIC) | 20 | 2026-11-09 | 28 | 87% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 307 | [x] | Tyr (STEAM) | 20 | 2026-11-09 | 28 | 73% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 308 | [x] | Dead Island (STEAM) | 20 | 2026-11-09 | 25 | 79% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 309 | [x] | Titan Quest Anniversary Edition (STEAM) | 19 | 2026-10-16 | 60 | 93% |  |
| 310 | [x] | BlazBlue Centralfiction (STEAM) | 19 | 2026-10-17 | 57 | 80% |  |
| 311 | [x] | No Rest for the Wicked (STEAM) | 19 | 2026-10-19 | 45 | 76% |  |
| 312 | [x] | One-armed robber (STEAM) | 19 | 2026-11-09 | 35 | 72% |  |
| 313 | [x] | Sorry We're Closed (EPIC) | 19 | 2026-11-09 | 34 | 74% |  |
| 314 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 19 | 2026-11-09 | 33 | 94% |  |
| 315 | [x] | Far Far West (STEAM) | 19 | 2026-11-09 | 33 | 67% |  |
| 316 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 33 | 58% |  |
| 317 | [x] | Stick It to the Stickman (STEAM) | 19 | 2026-11-09 | 33 | 75% |  |
| 318 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 19 | 2026-11-09 | 30 | 81% |  |
| 319 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 19 | 2026-11-09 | 29 | 83% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 320 | [x] | Capcom Fighting Collection (STEAM) | 19 | 2026-11-09 | 27 | 77% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 321 | [x] | Need for Speed™ Unbound (STEAM) | 19 | 2026-11-09 | 27 | 67% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 322 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 19 | 2026-11-09 | 25 | 76% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 323 | [x] | Deadly Premonition: The Director's Cut (STEAM) | 19 | 2026-11-09 | 21 | 75% | [#520](https://github.com/GameNative/gamenative-compat/issues/520) |
| 324 | [x] | Cave Story+ (EPIC) | 18 | 2026-10-18 | 42 | 81% |  |
| 325 | [x] | Backpack Battles (STEAM) | 18 | 2026-11-09 | 41 | 100% |  |
| 326 | [x] | Maneater (STEAM) | 18 | 2026-11-09 | 28 | 64% |  |
| 327 | [x] | Arcade Paradise (EPIC) | 18 | 2026-11-09 | 27 | 68% |  |
| 328 | [x] | Sonic and SEGA All Stars Racing (STEAM) | 18 | 2026-11-09 | 27 | 69% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 329 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-09 | 23 | 67% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 330 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 17 | 2026-10-25 | 42 | 75% |  |
| 331 | [x] | Kingdom Come: Deliverance II (STEAM) | 17 | 2026-10-20 | 41 | 90% |  |
| 332 | [x] | Spin Rhythm XD (STEAM) | 17 | 2026-10-18 | 38 | 85% |  |
| 333 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 37 | 21% |  |
| 334 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 35 | 89% |  |
| 335 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 17 | 2026-11-09 | 31 | 82% |  |
| 336 | [x] | Guacamelee! Gold Edition (STEAM) | 17 | 2026-11-11 | 30 | n/a | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 337 | [x] | Need for Speed: Undercover (STEAM) | 17 | 2026-11-11 | 29 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 338 | [x] | Shank 2 (STEAM) | 17 | 2026-11-09 | 29 | 83% |  |
| 339 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 17 | 2026-11-09 | 25 | 88% |  |
| 340 | [x] | Katanaut (STEAM) | 17 | 2026-11-09 | 23 | 69% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 341 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 17 | 2026-11-09 | 22 | 92% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 342 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 343 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 344 | [x] | Jotunnslayer: Hordes of Hel (STEAM) | 17 | 2026-11-09 | 21 | 91% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 345 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 51 | 95% |  |
| 346 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 16 | 2026-10-20 | 36 | 76% |  |
| 347 | [x] | Overlord (STEAM) | 16 | 2026-11-08 | 36 | 63% |  |
| 348 | [x] | GRIP: Combat Racing (STEAM) | 16 | 2026-11-09 | 33 | 88% |  |
| 349 | [x] | sobosuba (STEAM) | 16 | 2026-11-09 | 32 | 86% |  |
| 350 | [x] | Faster Than Light (EPIC) | 16 | 2026-11-09 | 31 | 93% |  |
| 351 | [x] | Tiny Glade (STEAM) | 16 | 2026-11-09 | 30 | 71% |  |
| 352 | [x] | GRANDIA HD Remaster (STEAM) | 16 | 2026-11-09 | 29 | 73% |  |
| 353 | [x] | Titanfall® 2 (STEAM) | 16 | 2026-11-09 | 29 | 64% |  |
| 354 | [x] | DNF Duel (EPIC) | 16 | 2026-11-09 | 27 | 73% |  |
| 355 | [x] | Mortal Shell (EPIC) | 16 | 2026-11-09 | 26 | 74% |  |
| 356 | [x] | Gloomwood (STEAM) | 16 | 2026-11-09 | 26 | 69% |  |
| 357 | [x] | LET IT DIE (STEAM) | 16 | 2026-11-09 | 26 | 62% |  |
| 358 | [x] | Assassin's Creed Odyssey (STEAM) | 16 | 2026-11-09 | 25 | 69% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 359 | [x] | Nex Machina (STEAM) | 16 | 2026-11-09 | 25 | 77% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 360 | [x] | Legend of Grimrock 2 (STEAM) | 16 | 2026-11-09 | 24 | 83% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 361 | [x] | Allumeria (STEAM) | 16 | 2026-11-09 | 23 | 69% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 362 | [x] | Spark the Electric Jester (STEAM) | 16 | 2026-11-11 | 22 | 62% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 363 | [x] | Darksiders Warmastered Edition (EPIC) | 16 | 2026-11-09 | 21 | 63% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 364 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 365 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 366 | [x] | Sacred Gold (STEAM) | 16 | 2026-11-09 | 20 | 70% | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 367 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 15 | 2026-10-19 | 53 | 84% |  |
| 368 | [x] | Grim Fandango Remastered (STEAM) | 15 | 2026-10-19 | 40 | 69% |  |
| 369 | [x] | Mark of the Ninja (STEAM) | 15 | 2026-10-26 | 32 | 75% |  |
| 370 | [x] | Killing Floor (STEAM) | 15 | 2026-10-19 | 31 | 85% |  |
| 371 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 31 | 96% |  |
| 372 | [x] | Race The Sun (STEAM) | 15 | 2026-11-11 | 30 | 33% |  |
| 373 | [x] | Sonic Superstars (STEAM) | 15 | 2026-10-21 | 30 | 67% |  |
| 374 | [x] | Human Fall Flat (STEAM) | 15 | 2026-10-29 | 29 | 62% |  |
| 375 | [x] | Mortal Kombat 11 (STEAM) | 15 | 2026-11-09 | 29 | 69% |  |
| 376 | [x] | Hitman: Absolution (GOG) | 15 | 2026-11-09 | 28 | 77% |  |
| 377 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 15 | 2026-11-09 | 28 | 67% |  |
| 378 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 15 | 2026-11-11 | 27 | 60% |  |
| 379 | [x] | WORLD OF FINAL FANTASY (STEAM) | 15 | 2026-11-09 | 26 | 76% |  |
| 380 | [x] | Wildermyth (STEAM) | 15 | 2026-11-09 | 26 | 81% |  |
| 381 | [x] | Car Mechanic Simulator 2018 (STEAM) | 15 | 2026-11-09 | 25 | 92% |  |
| 382 | [x] | Batman™: Arkham Origins (GOG) | 15 | 2026-11-09 | 24 | 100% |  |
| 383 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 85% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 384 | [x] | Chef Knight (STEAM) | 15 | 2026-11-09 | 22 | 64% |  |
| 385 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 15 | 2026-11-09 | 22 | 63% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 386 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 387 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 15 | 2026-11-09 | 21 | 67% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 388 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 389 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 14 | 2026-10-21 | 42 | 80% |  |
| 390 | [x] | Blood: Fresh Supply (STEAM) | 14 | 2026-10-16 | 39 | 79% |  |
| 391 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 92% |  |
| 392 | [x] | No Man's Sky (GOG) | 14 | 2026-10-19 | 30 | 88% |  |
| 393 | [x] | Antichamber (STEAM) | 14 | 2026-11-11 | 28 | 90% |  |
| 394 | [x] | Evoland (STEAM) | 14 | 2026-11-11 | 28 | n/a |  |
| 395 | [x] | Blaster Master Zero (STEAM) | 14 | 2026-11-11 | 27 | 59% |  |
| 396 | [x] | Ultrapool (STEAM) | 14 | 2026-11-09 | 26 | 100% |  |
| 397 | [x] | Ghostwire Tokyo (EPIC) | 14 | 2026-11-09 | 24 | 79% |  |
| 398 | [x] | 12 is Better Than 6 (STEAM) | 14 | 2026-11-09 | 23 | 85% |  |
| 399 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 23 | 76% |  |
| 400 | [x] | Sons Of The Forest (STEAM) | 14 | 2026-11-09 | 23 | 74% |  |
| 401 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 402 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-11-09 | 21 | 92% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 403 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 404 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 405 | [x] | Middle-earth™: Shadow of War™ (STEAM) | 13 | 2026-10-16 | 38 | 80% |  |
| 406 | [x] | Tom Clancy's Splinter Cell: Chaos Theory (STEAM) | 13 | 2026-10-16 | 31 | 83% |  |
| 407 | [x] | Divinity: Original Sin (Classic) (STEAM) | 13 | 2026-10-16 | 30 | 70% |  |
| 408 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 30 | 56% |  |
| 409 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 13 | 2026-10-19 | 30 | 96% |  |
| 410 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 29 | 73% |  |
| 411 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 27 | 80% |  |
| 412 | [x] | Alan Wake's American Nightmare (EPIC) | 13 | 2026-11-09 | 26 | 60% |  |
| 413 | [x] | Rayman Origins (GOG) | 13 | 2026-11-09 | 26 | 82% |  |
| 414 | [x] | Intravenous 2 (STEAM) | 13 | 2026-11-09 | 26 | 97% |  |
| 415 | [x] | Lost Castle 2 (STEAM) | 13 | 2026-11-09 | 25 | 94% |  |
| 416 | [x] | Ready or Not (STEAM) | 13 | 2026-11-09 | 25 | 79% |  |
| 417 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 13 | 2026-11-09 | 23 | 66% |  |
| 418 | [x] | Haydee (STEAM) | 13 | 2026-11-09 | 23 | 78% |  |
| 419 | [x] | Horny Villa (STEAM) | 13 | 2026-11-09 | 22 | 91% |  |
| 420 | [x] | PAYDAY: The Heist (STEAM) | 13 | 2026-11-10 | 22 | 70% |  |
| 421 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 422 | [x] | Super Monkey Ball Banana Mania (STEAM) | 13 | 2026-11-11 | 21 | 60% |  |
| 423 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 95% |  |
| 424 | [x] | Alabaster Dawn Demo (STEAM) | 13 | 2026-11-09 | 20 | 83% |  |
| 425 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 426 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 13 | 2026-10-23 | 20 | 61% |  |
| 427 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 80% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 428 | [x] | CULTIC (STEAM) | 12 | 2026-11-09 | 28 | 61% |  |
| 429 | [x] | Haiku, the Robot (STEAM) | 12 | 2026-10-21 | 28 | n/a |  |
| 430 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 12 | 2026-10-18 | 28 | 91% |  |
| 431 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 12 | 2026-11-01 | 27 | n/a |  |
| 432 | [x] | Dead Space™ 3 (STEAM) | 12 | 2026-10-20 | 27 | 71% |  |
| 433 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 12 | 2026-11-09 | 26 | 90% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 434 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 26 | 67% |  |
| 435 | [x] | Aperture Desk Job (STEAM) | 12 | 2026-11-03 | 25 | n/a |  |
| 436 | [x] | Injustice™ 2 (STEAM) | 12 | 2026-10-17 | 24 | 61% |  |
| 437 | [x] | Lust Goddess (STEAM) | 12 | 2026-11-09 | 24 | 89% |  |
| 438 | [x] | AER Memories of Old (EPIC) | 12 | 2026-11-09 | 23 | 93% |  |
| 439 | [x] | HITMAN World of Assassination (STEAM) | 12 | 2026-11-09 | 23 | 87% |  |
| 440 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-10 | 22 | 67% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 441 | [x] | DiRT 4 (STEAM) | 12 | 2026-11-09 | 22 | 91% |  |
| 442 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 22 | 75% |  |
| 443 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 12 | 2026-11-09 | 21 | 76% |  |
| 444 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 445 | [x] | Shift At Midnight (STEAM) | 12 | 2026-11-09 | 21 | 79% |  |
| 446 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 447 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 448 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 2026-11-10 | 20 | 60% |  |
| 449 | [x] | Turbo Overkill (STEAM) | 12 | 2026-11-09 | 20 | 95% |  |
| 450 | [x] | The WereCleaner (STEAM) | 11 | 2026-10-22 | 32 | 96% |  |
| 451 | [x] | Breath of Fire IV (GOG) | 11 | 2026-10-26 | 25 | 60% |  |
| 452 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 2026-10-27 | 25 | 81% |  |
| 453 | [x] | MX Bikes (STEAM) | 11 | 2026-11-09 | 23 | 94% |  |
| 454 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 23 | 76% |  |
| 455 | [x] | Castle in the Clouds (STEAM) | 11 | 2026-11-09 | 22 | 82% |  |
| 456 | [x] | Cruelty Squad (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 457 | [x] | UNDEFEATED (STEAM) | 11 | 2026-11-09 | 22 | 69% |  |
| 458 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 21 | 62% |  |
| 459 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 460 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 461 | [x] | TowerFall Ascension (STEAM) | 10 | 2026-10-16 | 30 | 69% |  |
| 462 | [x] | Distance (STEAM) | 10 | 2026-10-19 | 29 | 71% |  |
| 463 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 26 | n/a |  |
| 464 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 10 | 2026-10-23 | 24 | 80% |  |
| 465 | [x] | Coromon (GOG) | 10 | 2026-10-19 | 22 | 65% |  |
| 466 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 22 | 84% |  |
| 467 | [x] | Sid Meier's Civilization VI (EPIC) | 10 | 2026-10-19 | 21 | 83% |  |
| 468 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 10 | 2026-11-09 | 21 | 89% |  |
| 469 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 470 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 92% |  |
| 471 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 472 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 20 | 77% |  |
| 473 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 474 | [x] | Possessor(s) (STEAM) | 9 | 2026-10-24 | 27 | 93% |  |
| 475 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 9 | 2026-10-20 | 26 | 79% |  |
| 476 | [x] | SCP – Containment Breach (STEAM) | 9 | 2026-10-27 | 23 | 92% |  |
| 477 | [x] | SteamWorld Heist (GOG) | 9 | 2026-10-25 | 21 | n/a |  |
| 478 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 9 | 2026-10-21 | 21 | 92% |  |
| 479 | [x] | Football Manager 2024 (STEAM) | 9 | 2026-10-16 | 20 | n/a |  |
| 480 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 29% |  |
| 481 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 9 | 2026-10-20 | 20 | n/a |  |
| 482 | [x] | Gloomhaven (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 483 | [x] | Mina the Hollower (GOG) | 8 | 2026-10-28 | 20 | 71% |  |
| 484 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 20 | 52% |  |
| 485 | [x] | Mafia II: Definitive Edition (STEAM) | 7 | 2026-10-16 | 20 | n/a |  |
| 486 | [x] | What Remains of Edith Finch (STEAM) | 6 | 2026-10-19 | 26 | 64% |  |
| 487 | [x] | Alex Kidd in Miracle World DX (STEAM) | 2 | 2026-10-16 | 34 | 93% |  |
