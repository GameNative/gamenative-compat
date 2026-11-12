# GameNative compatibility worklist

Generated: `2026-11-12T04:15:12.765Z` · Ratings since: `2026-08-14T04:15:12.765Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 120 |
| Probably does not work | 170 |
| Fix shipped, waiting for ratings | 17 |
| First launch fails | 325 |
| Mixed | 508 |
| Works | 1023 |
| Total | 2163 |

## Does not work (120)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 69 | 82 | 84% (since fix) | Does not open (93%) | 55% | today | 42% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 2 | [ ] | Road Rash™: 30th Anniversary Edition (STEAM) | 43 | 59 | 73% (14d) | Does not open (76%) | 59% | 1d ago | 64% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 3 | [ ] | Metro 2033 Redux (STEAM) | 29 | 37 | 78% (14d) | Does not open (70%) | 41% | today | 39% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 4 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 27 | 33 | 82% (14d) | Does not open (72%) | 59% | 1d ago | 52% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 5 | [x] 2026-10-18 | Project Zomboid (STEAM) | 51 | 57 | 89% (since fix) | Does not open (65%) | 53% | today | 48% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 6 | [ ] | Counter-Strike 2 (STEAM) | 39 | 53 | 74% (since fix) | Does not open (67%) | 59% | today | 65% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 7 | [ ] | Borderlands 2 (EPIC) | 22 | 29 | 76% (14d) | Does not open (82%) | 58% | today | 50% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 8 | [ ] | Hogwarts Legacy (STEAM) | 22 | 27 | 81% (14d) | Does not open (65%) | 50% | today | 20% (drop) | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 9 | [ ] | Metro: Last Light Redux (STEAM) | 19 | 20 | 95% (14d) | Does not open (91%) | 19% | today | 14% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 10 | [ ] | Saints Row 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (96%) | 37% | today | 38% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 11 | [ ] | Saints Row 2 (GOG) | 18 | 24 | 75% (14d) | Does not open (92%) | 41% | today | 33% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 12 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 18 | 21 | 86% (14d) | Does not open (95%) | 58% | 1d ago | 12% (drop) |  |
| 13 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (76%) | 0% | 3d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 14 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 16 | 20 | 80% (14d) | Does not open (76%) | 57% | 1d ago | 40% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 15 | [ ] | Bloons TD 6 (EPIC) | 16 | 21 | 76% (14d) | Does not open (80%) | 51% | 1d ago | 21% (drop) | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 16 | [ ] | Call of Duty: Black Ops II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (77%) | 32% | today | 44% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 17 | [ ] | Fallout: New Vegas PCR (STEAM) | 17 | 20 | 85% (last 20) | Does not open (93%) | 57% | today | 52% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 18 | [ ] | Garry's Mod (STEAM) | 7 | 10 | 70% (since fix) | Does not open (81%) | 54% | 2d ago | 44% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 19 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 18 | 20 | 90% (last 20) | No graphics (46%) | 25% | 4d ago | n/a | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 20 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (96%) | 26% | 2d ago | n/a | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 21 | [ ] | Yume Nikki (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | 21% | 5d ago | 38% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 22 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (78%) | 8% | today | n/a | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 23 | [ ] | skate. (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | 10% | 1d ago | 14% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 24 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 17 | 20 | 85% (last 20) | Does not open (87%) | 44% | today | 26% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 25 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (70%) | 7% | 6d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 26 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (65%) | 5% | 18d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 27 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 10% | today | n/a | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 28 | [ ] | The Witcher: Enhanced Edition (GOG) | 19 | 20 | 95% (last 20) | Does not open (73%) | 12% | 3d ago | 0% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 29 | [ ] | Mafia II (Classic) (STEAM) | 20 | 20 | 100% (last 20) | Does not open (74%) | 7% | 4d ago | n/a | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 30 | [ ] | CPM 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (88%) | 5% | 3d ago | n/a | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 31 | [ ] | Path of Exile (STEAM) | 18 | 20 | 90% (last 20) | Does not open (91%) | 43% | 3d ago | 9% (drop) | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 32 | [ ] | Fall Guys (EPIC) | 19 | 20 | 95% (last 20) | Does not open (76%) | 15% | 2d ago | 9% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 33 | [ ] | Detroit: Become Human (STEAM) | 19 | 20 | 95% (last 20) | Does not open (75%) | 42% | 10d ago | n/a | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 34 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | 0% | 1d ago | n/a | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 35 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | No graphics (57%) | 0% | 15d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 36 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (74%) | 10% | today | n/a | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 37 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (92%) | 6% | 13d ago | n/a | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 38 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (67%) | 14% | 11d ago | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 39 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (88%) | 17% | 5d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 40 | [ ] | Borderlands GOTY (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 27% | 3d ago | n/a | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 41 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (79%) | 15% | 3d ago | 20% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 42 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (88%) | 25% | 3d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 43 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (68%) | 22% | 4d ago | n/a | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 44 | [ ] | Breath of Fire IV (STEAM) | 20 | 20 | 100% (last 20) | Does not open (58%) | 24% | 10d ago | n/a | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 45 | [ ] | MECCHA CHAMELEON (STEAM) | 15 | 20 | 75% (last 20) | Does not open (65%) | 50% | 4d ago | 25% (drop) | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 46 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 50% | 5d ago | n/a | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 47 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (73%) | 24% | today | n/a | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 48 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | 18% | 4d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 49 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (83%) | 53% | 26d ago | n/a | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 50 | [ ] | Plague Inc: Evolved (STEAM) | 14 | 20 | 70% (last 20) | Does not open (66%) | 58% | 2d ago | 64% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 51 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (83%) | 6% | today | n/a | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 52 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | 0% | 26d ago | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 53 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (56%) | 22% | 7d ago | n/a | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 54 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | 0% | 4d ago | n/a | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 55 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 17 | 20 | 85% (last 20) | Does not open (44%) | 49% | 14d ago | 40% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 56 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (86%) | 34% | 11d ago | n/a | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 57 | [ ] | Trackmania (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | 26% | today | 29% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 58 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | 45% | 33d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 59 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 26% | 3d ago | n/a | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 60 | [ ] | Black Mesa (STEAM) | 15 | 20 | 75% (last 20) | Does not open (80%) | 21% | 19d ago | 38% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 61 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (92%) | 28% | today | n/a | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 62 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 36% | today | n/a | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 63 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (47%) | 39% | 7d ago | 35% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 64 | [ ] | Watch_Dogs (STEAM) | 14 | 20 | 70% (last 20) | Does not open (90%) | 29% | 5d ago | n/a | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 65 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | 0% | 10d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 66 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (71%) | 32% | 5d ago | n/a | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 67 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 14% | 24d ago | n/a | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 68 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | 45% | 1d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 69 | [ ] | XCOM: Enemy Unknown (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | 11% | 7d ago | n/a | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 70 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 9% | 10d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 71 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | 18% | today | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 72 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 23% | 21d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 73 | [ ] | Half-Life: Blue Shift (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 33% | 3d ago | n/a | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 74 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | No graphics (62%) | 10% | 5d ago | n/a | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 75 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (82%) | 8% | 10d ago | n/a | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 76 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (60%) | 33% | 12d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 77 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 4% | today | 2% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 78 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 46% | today | n/a | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 79 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 0% | 25d ago | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 80 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (67%) | 0% | 18d ago | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 81 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 20 | 20 | 100% (last 20) | No graphics (60%) | 40% | 35d ago | 69% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 82 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 17% | 12d ago | n/a | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 83 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (81%) | 29% | 4d ago | n/a | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 84 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 6% | 7d ago | 8% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 85 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 50% | today | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 86 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | 42% | 7d ago | n/a | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 87 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (76%) | 30% | 11d ago | n/a | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 88 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 30% | 9d ago | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 89 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (91%) | 5% | 18d ago | 10% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 90 | [ ] | Changed (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 52% | 1d ago | 27% (drop) | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 91 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | 21% | 2d ago | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 92 | [ ] | Umamusume: Pretty Derby (STEAM) | 18 | 20 | 90% (last 20) | Does not open (86%) | 47% | 8d ago | n/a | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 93 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (68%) | 29% | 28d ago | n/a | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 94 | [ ] | Lost Planet: Extreme Condition (STEAM) | 15 | 20 | 75% (last 20) | Does not open (78%) | 50% | 2d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 95 | [ ] | Hotline Miami (GOG) | 15 | 20 | 75% (last 20) | Does not open (87%) | 59% | 2d ago | n/a | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 96 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 29% | 10d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 97 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (95%) | 38% | 23d ago | 31% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 98 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 45% | 9d ago | n/a | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 99 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (97%) | 31% | 10d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 100 | [ ] | Aliens vs. Predator (STEAM) | 16 | 20 | 80% (last 20) | No graphics (53%) | 17% | today | 18% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 101 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | 18% | 1d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 102 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (86%) | 42% | 12d ago | n/a | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 103 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (68%) | 39% | 1d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 104 | [ ] | Kenshi (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | 6% | 11d ago | n/a | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 105 | [ ] | Call of Duty® (STEAM) | 14 | 20 | 70% (last 20) | Does not open (67%) | 7% | today | n/a | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 106 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 42% | 26d ago | n/a | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 107 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | 41% | 12d ago | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 108 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 14 | 20 | 70% (last 20) | Does not open (56%) | 52% | 2d ago | 67% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 109 | [ ] | Zuma Deluxe (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 33% | 21d ago | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 110 | [ ] | Undisputed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 56% | 4d ago | n/a | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 111 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | 20% | 1d ago | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 112 | [ ] | Beyond Good & Evil™ (GOG) | 17 | 20 | 85% (last 20) | Does not open (100%) | 18% | 19d ago | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 113 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (67%) | 54% | 3d ago | n/a | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 114 | [ ] | skate.™ (EPIC) | 18 | 20 | 90% (last 20) | Does not open (87%) | 0% | 17d ago | n/a | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 115 | [ ] | Goose Goose Duck (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 56% | 2d ago | n/a | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 116 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | 44% | 12d ago | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 117 | [ ] | Maneater (EPIC) | 16 | 20 | 80% (last 20) | Does not open (75%) | 56% | 4d ago | n/a | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 118 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 36% | 7d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 119 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | 55% | 16d ago | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 120 | [ ] | Spark the Electric Jester (STEAM) | 14 | 20 | 70% (last 20) | Does not open (62%) | 56% | 7d ago | n/a | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |

## Probably does not work (170)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | To The Moon (GOG) | 44 | 46 | 96% (14d) | Does not open (86%) | n/a | 9d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 2 | [ ] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 34 | 58 | 59% (14d) | Does not open (64%) | 58% | today | 63% |  |
| 3 | [ ] | theHunter Classic (STEAM) | 23 | 23 | 100% (14d) | No graphics (92%) | n/a | 8d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 4 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 15 | 25 | 60% (14d) | Does not open (72%) | 54% | today | 92% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 5 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 12 | 20 | 60% (14d) | Does not open (63%) | 58% | 2d ago | 52% |  |
| 6 | [ ] | VRChat (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 37% | today | 26% |  |
| 7 | [ ] | Driver: Parallel Lines (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | n/a | 3d ago | n/a | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 8 | [ ] | Gorilla Tag (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 18% | 2d ago | 9% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 9 | [ ] | Door Kickers 2 (STEAM) | 20 | 20 | 100% (last 20) | No graphics (87%) | n/a | 29d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 10 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 32d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 11 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (35%) | n/a | 9d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 12 | [ ] | Alan Wake (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 26% | 2d ago | 72% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 13 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 16d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 14 | [ ] | Sonic Adventure™ 2  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (76%) | 50% | today | 44% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 15 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 9 | 13 | 69% (since fix) | Does not open (77%) | 20% | today | 32% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 16 | [ ] | Metro 2033 Redux (EPIC) | 10 | 20 | 50% (last 20) | Does not open (62%) | 27% | 3d ago | 43% |  |
| 17 | [ ] | GRID (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 44% | 3d ago | n/a | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 18 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 13d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 19 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 13 | 20 | 65% (last 20) | Does not open (85%) | 49% | 1d ago | 69% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 20 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (85%) | 43% | 2d ago | n/a |  |
| 21 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (93%) | n/a | today | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 22 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 7d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 23 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 33% | 4d ago | n/a | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 24 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (100%) | n/a | 1d ago | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 25 | [ ] | CODE VEIN (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 48% | 1d ago | n/a | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 26 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (85%) | n/a | 10d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 27 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | n/a | 31d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 28 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | n/a | 14d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 29 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | n/a | 7d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 30 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | n/a | 1d ago | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 31 | [ ] | Grim Dawn (GOG) | 12 | 20 | 60% (last 20) | Does not open (65%) | n/a | today | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 32 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 30d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 33 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 9d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 34 | [ ] | Dead Space 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 32% | 2d ago | 39% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 35 | [ ] | METAL SLUG 3 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 42% | today | n/a | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 36 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 29d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 37 | [ ] | Alpha Protocol (STEAM) | 17 | 20 | 85% (last 20) | Does not open (55%) | n/a | 17d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 38 | [ ] | Breathedge (STEAM) | 11 | 20 | 55% (last 20) | Does not open (57%) | 50% | 1d ago | n/a | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 39 | [ ] | DOOM Eternal (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | n/a | 20d ago | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 40 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 32% | 2d ago | n/a | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 41 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | n/a | 31d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 42 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (58%) | n/a | 31d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 43 | [ ] | WRC 7 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (65%) | n/a | 29d ago | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 44 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | n/a | 13d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 45 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 29d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 46 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 15d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 47 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | n/a | 32d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 48 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 7d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 49 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | n/a | 29d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 50 | [ ] | Borderlands 2 RU (STEAM) | 19 | 20 | 95% (last 20) | Does not open (61%) | n/a | 29d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 51 | [ ] | OneShot (STEAM) | 16 | 20 | 80% (last 20) | Does not open (96%) | n/a | 27d ago | n/a | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 52 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 3d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 53 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (81%) | n/a | 4d ago | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 54 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 15d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 55 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (57%) | n/a | 17d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 56 | [ ] | HELLDIVERS™ (STEAM) | 13 | 20 | 65% (last 20) | Does not open (60%) | 42% | 1d ago | n/a | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 57 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 40d ago | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 58 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 11d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 59 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | n/a | 20d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 60 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | 0% | 7d ago | n/a |  |
| 61 | [ ] | Euro Truck Simulator (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | today | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 62 | [ ] | Peggle Nights (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | 15d ago | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 63 | [ ] | The Survivalists (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | n/a | 57d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 64 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (47%) | n/a | 11d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 65 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | n/a | 34d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 66 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (63%) | n/a | 38d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 67 | [ ] | Metro 2033 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 36% | 8d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 68 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 20 | 20 | 100% (last 20) | Does not open (53%) | n/a | 27d ago | n/a | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 69 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 54d ago | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 70 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | 1d ago | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 71 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | n/a | 29d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 72 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 5d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 73 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 7d ago | n/a |  |
| 74 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | today | n/a |  |
| 75 | [ ] | Resident Evil Requiem (STEAM) | 20 | 20 | 100% (last 20) | Does not open (69%) | n/a | 31d ago | n/a | [#210](https://github.com/GameNative/gamenative-compat/issues/210) |
| 76 | [ ] | Marvel's Spider-Man 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | n/a | 31d ago | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 77 | [ ] | They Are Billions (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | n/a | 8d ago | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 78 | [ ] | Alien Breed: Impact (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 17d ago | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 79 | [ ] | Bionic Commando Rearmed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | n/a | 22d ago | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 80 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | n/a | 29d ago | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 81 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 18 | 20 | 90% (last 20) | Does not open (75%) | n/a | 16d ago | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 82 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (83%) | n/a | 5d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 83 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 2d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 84 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 38% | today | n/a | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 85 | [ ] | GeoGuessr Steam Edition (STEAM) | 19 | 20 | 95% (last 20) | Does not open (73%) | n/a | 24d ago | n/a | [#154](https://github.com/GameNative/gamenative-compat/issues/154) |
| 86 | [ ] | No More Room in Hell (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 25d ago | n/a | [#365](https://github.com/GameNative/gamenative-compat/issues/365) |
| 87 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 18 | 20 | 90% (last 20) | Does not open (88%) | n/a | 21d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 88 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 3d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 89 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | n/a | today | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 90 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 13d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 91 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (44%) | n/a | 10d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 92 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 14d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 93 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 7d ago | n/a |  |
| 94 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 7d ago | n/a |  |
| 95 | [ ] | Apex Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | n/a | 13d ago | n/a | [#261](https://github.com/GameNative/gamenative-compat/issues/261) |
| 96 | [ ] | Melatonin (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | n/a | 20d ago | n/a | [#272](https://github.com/GameNative/gamenative-compat/issues/272) |
| 97 | [ ] | Wuthering Waves (STEAM) | 19 | 20 | 95% (last 20) | Does not open (83%) | n/a | 14d ago | n/a | [#216](https://github.com/GameNative/gamenative-compat/issues/216) |
| 98 | [ ] | Zenless Zone Zero (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | n/a | 15d ago | n/a | [#369](https://github.com/GameNative/gamenative-compat/issues/369) |
| 99 | [ ] | Deadly Premonition: The Director's Cut (STEAM) | 18 | 20 | 90% (last 20) | Does not open (53%) | n/a | 5d ago | n/a | [#520](https://github.com/GameNative/gamenative-compat/issues/520) |
| 100 | [ ] | Lay of the Land (STEAM) | 18 | 20 | 90% (last 20) | No graphics (61%) | n/a | 11d ago | n/a | [#477](https://github.com/GameNative/gamenative-compat/issues/477) |
| 101 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 10d ago | n/a |  |
| 102 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | today | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 103 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 10 | 20 | 50% (last 20) | Does not open (86%) | 42% | 21d ago | n/a |  |
| 104 | [ ] | King's Bounty: The Legend (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | n/a | 6d ago | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 105 | [ ] | Marvel's Midnight Suns (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | n/a | 29d ago | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 106 | [ ] | PICO PARK:Classic Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 34d ago | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 107 | [ ] | ENDLESS Space™ 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | n/a | 27d ago | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 108 | [ ] | Beholder (EPIC) | 15 | 20 | 75% (last 20) | Does not open (69%) | n/a | 17d ago | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 109 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | Does not open (42%) | n/a | 2d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 110 | [ ] | Mafia II (Classic) (GOG) | 13 | 20 | 65% (last 20) | Does not open (96%) | 42% | 19d ago | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 111 | [ ] | PAYDAY: The Heist (STEAM) | 13 | 20 | 65% (last 20) | Does not open (75%) | n/a | 5d ago | n/a |  |
| 112 | [ ] | Drop Duchy (EPIC) | 12 | 20 | 60% (last 20) | Does not open (100%) | n/a | 11d ago | n/a |  |
| 113 | [ ] | Mini Metro (STEAM) | 11 | 20 | 55% (last 20) | Does not open (44%) | 40% | today | n/a |  |
| 114 | [ ] | Utopia Must Fall (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | n/a | 5d ago | n/a | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 115 | [ ] | Clive Barker's Undying (GOG) | 17 | 20 | 85% (last 20) | Does not open (75%) | n/a | 16d ago | n/a | [#388](https://github.com/GameNative/gamenative-compat/issues/388) |
| 116 | [ ] | The Elder Scrolls IV: Oblivion Remastered (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | n/a | 30d ago | n/a | [#312](https://github.com/GameNative/gamenative-compat/issues/312) |
| 117 | [ ] | Re-Volt (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (71%) | n/a | 18d ago | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 118 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (92%) | n/a | 17d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 119 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (57%) | n/a | 24d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 120 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (83%) | 38% | 10d ago | n/a | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 121 | [ ] | Mirror's Edge™ (GOG) | 10 | 20 | 50% (last 20) | No graphics (62%) | 46% | today | n/a | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 122 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (50%) | n/a | 3d ago | n/a |  |
| 123 | [ ] | F.E.A.R. 2: Project Origin + Reborn (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 12d ago | n/a | [#478](https://github.com/GameNative/gamenative-compat/issues/478) |
| 124 | [ ] | Beat Cop (STEAM) | 14 | 20 | 70% (last 20) | Does not open (72%) | n/a | 6d ago | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 125 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | n/a | 4d ago | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 126 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | n/a | 2d ago | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 127 | [ ] | Sandustry (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 2d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 128 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 1d ago | n/a |  |
| 129 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | n/a | 23d ago | n/a |  |
| 130 | [ ] | Mafia: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 48% | today | 41% |  |
| 131 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (78%) | 58% | 1d ago | n/a |  |
| 132 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 12 | 20 | 60% (last 20) | Does not open (92%) | 57% | 3d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 133 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | No graphics (57%) | 20% | 5d ago | n/a | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 134 | [ ] | Fallout Classic (GOG) | 15 | 20 | 75% (last 20) | Does not open (71%) | n/a | 28d ago | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 135 | [ ] | Dungeon Keeper™ 2 (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 18d ago | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 136 | [ ] | Blood Omen: Legacy of Kain (GOG) | 13 | 20 | 65% (last 20) | Does not open (62%) | 44% | 1d ago | n/a |  |
| 137 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (58%) | n/a | 9d ago | n/a |  |
| 138 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 7d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 139 | [ ] | Styx: Master of Shadows (EPIC) | 11 | 20 | 55% (last 20) | Does not open (65%) | 35% | 3d ago | n/a |  |
| 140 | [ ] | A Plague Tale: Innocence (GOG) | 11 | 20 | 55% (last 20) | Does not open (91%) | 50% | 19d ago | n/a |  |
| 141 | [ ] | Knights of Pen and Paper 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (42%) | n/a | 3d ago | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 142 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 13 | 20 | 65% (last 20) | No graphics (56%) | n/a | 30d ago | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 143 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | n/a | 34d ago | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 144 | [ ] | Minit (EPIC) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 4d ago | n/a |  |
| 145 | [ ] | Songs of Conquest (EPIC) | 12 | 20 | 60% (last 20) | Does not open (75%) | n/a | 10d ago | n/a |  |
| 146 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 13d ago | n/a |  |
| 147 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | n/a | today | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 148 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (73%) | 57% | today | n/a |  |
| 149 | [ ] | LET IT DIE (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 58% | 6d ago | n/a |  |
| 150 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 47% | today | n/a | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 151 | [ ] | Fogpiercer (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 25d ago | n/a | [#303](https://github.com/GameNative/gamenative-compat/issues/303) |
| 152 | [ ] | The Stanley Parable (STEAM) | 13 | 20 | 65% (last 20) | Does not open (89%) | 58% | 17d ago | n/a |  |
| 153 | [ ] | Buck Up And Drive! (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | n/a | 17d ago | n/a |  |
| 154 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | n/a | 2d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 155 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (78%) | n/a | 6d ago | n/a |  |
| 156 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 54% | 4d ago | n/a |  |
| 157 | [ ] | No More Heroes (STEAM) | 10 | 20 | 50% (last 20) | No graphics (71%) | 44% | today | n/a |  |
| 158 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 48% | 7d ago | n/a |  |
| 159 | [ ] | Turnip Boy Robs a Bank (EPIC) | 12 | 20 | 60% (last 20) | Does not open (60%) | 31% | 17d ago | n/a | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 160 | [ ] | Ys: Memories of Celceta (STEAM) | 12 | 20 | 60% (last 20) | No graphics (45%) | 31% | 12d ago | n/a |  |
| 161 | [ ] | Dex (GOG) | 12 | 20 | 60% (last 20) | Does not open (83%) | n/a | 1d ago | n/a |  |
| 162 | [ ] | Secret of Mana (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (55%) | n/a | 25d ago | n/a |  |
| 163 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | n/a | 14d ago | n/a |  |
| 164 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | n/a | 6d ago | n/a |  |
| 165 | [ ] | Crying Suns (EPIC) | 11 | 20 | 55% (last 20) | No graphics (57%) | n/a | 2d ago | n/a |  |
| 166 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | n/a | 77d ago | n/a |  |
| 167 | [ ] | Railway Chai Wala (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | n/a | 5d ago | n/a |  |
| 168 | [ ] | Asterigos: Curse of the Stars (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (50%) | n/a | 12d ago | n/a |  |
| 169 | [ ] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 15% | 7d ago | n/a |  |
| 170 | [ ] | Delver (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 48% | 4d ago | n/a |  |

## Fix shipped, waiting for ratings (17)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | Plants vs. Zombies: Game of the Year (STEAM) | 2026-11-04 | 7 | 5 | today | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 2 | Transistor (STEAM) | 2026-11-10 | 1 | 1 | today | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 3 | Max Payne 3 (STEAM) | 2026-11-04 | 1 | 1 | 5d ago | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 4 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 6 | 6 | 5d ago | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 5 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 3 | 3 | 1d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 6 | Call of Duty: Black Ops (STEAM) | 2026-10-14 | 8 | 3 | today | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 7 | L.A. Noire (STEAM) | 2026-11-04 | 0 | 0 | 9d ago | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 8 | Overwatch® (STEAM) | 2026-10-20 | 8 | 7 | 4d ago | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 9 | Necesse (STEAM) | 2026-10-29 | 5 | 0 | 3d ago | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 10 | Peggle Deluxe (STEAM) | 2026-10-29 | 0 | 0 | 7d ago | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 11 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 1 | 1 | 1d ago | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 12 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 1 | 1 | 8d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 13 | Need for Speed™ (STEAM) | 2026-11-04 | 0 | 0 | 21d ago | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 14 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 0 | 0 | 9d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 15 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 0 | 0 | 8d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 16 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 0 | 0 | 14d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 17 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 7d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |

## Works, but the first launch usually fails (325)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 143 | 163 | 88% (14d) | Does not open (83%) | 62% | today | 8% (drop) | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 70 | 87 | 80% (14d) | Does not open (62%) | 90% | today | 92% |  |
| 3 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 57 | 79 | 72% (14d) | Does not open (54%) | 82% | today | 82% |  |
| 4 | [ ] | Deskrawl: Idle ARPG (STEAM) | 55 | 66 | 83% (14d) | Does not open (60%) | 87% | 1d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 5 | [ ] | Grand Theft Auto V Legacy (STEAM) | 30 | 39 | 77% (since fix) | Does not open (87%) | 76% | today | 68% |  |
| 6 | [ ] | Valheim (STEAM) | 27 | 43 | 63% (since fix) | No graphics (53%) | 89% | today | 82% |  |
| 7 | [ ] | MONSTER HUNTER RISE (STEAM) | 43 | 69 | 62% (14d) | Does not open (82%) | 63% | 1d ago | 60% |  |
| 8 | [ ] | Cyberpunk 2077 (STEAM) | 40 | 68 | 59% (14d) | Does not open (68%) | 74% | today | 68% |  |
| 9 | [ ] | Rocket League® (EPIC) | 40 | 50 | 80% (14d) | Does not open (78%) | 60% | today | 35% (drop) | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 10 | [ ] | Half-Life (STEAM) | 39 | 62 | 63% (14d) | Does not open (57%) | 71% | today | 61% |  |
| 11 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 39 | 53 | 74% (14d) | Does not open (76%) | 78% | 1d ago | 74% |  |
| 12 | [ ] | No Man's Sky (STEAM) | 20 | 35 | 57% (since fix) | Controller issues (61%) | 79% | today | 72% |  |
| 13 | [ ] | Buckshot Roulette (STEAM) | 33 | 62 | 53% (14d) | Does not open (61%) | 79% | today | 48% (drop) |  |
| 14 | [ ] | Palworld (STEAM) | 32 | 55 | 58% (14d) | Does not open (72%) | 86% | today | 83% |  |
| 15 | [ ] | DREDGE (EPIC) | 31 | 36 | 86% (14d) | Does not open (73%) | 73% | 1d ago | 52% (drop) | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 16 | [ ] | Terraria (STEAM) | 28 | 53 | 53% (14d) | No graphics (51%) | 72% | today | 67% |  |
| 17 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 24 | 39 | 62% (14d) | Does not open (57%) | 76% | today | 63% |  |
| 18 | [ ] | ELDEN RING (STEAM) | 24 | 43 | 56% (14d) | Does not open (85%) | 75% | today | 71% |  |
| 19 | [ ] | Quake (STEAM) | 20 | 29 | 69% (14d) | Does not open (65%) | 84% | today | 54% (drop) |  |
| 20 | [ ] | Deadlock (STEAM) | 18 | 21 | 86% (14d) | Does not open (54%) | 87% | today | 81% |  |
| 21 | [ ] | BeamNG.drive (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 83% | 1d ago | 55% (drop) | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 22 | [ ] | DRAGON BALL FighterZ (STEAM) | 25 | 41 | 61% (since fix) | Does not open (89%) | 75% | today | 88% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 23 | [ ] | Batman™: Arkham Origins (STEAM) | 17 | 25 | 68% (14d) | Does not open (84%) | 75% | today | 63% |  |
| 24 | [ ] | Devil May Cry 5 (STEAM) | 17 | 29 | 59% (14d) | Does not open (83%) | 72% | 1d ago | 77% |  |
| 25 | [ ] | BioShock Remastered (EPIC) | 17 | 21 | 81% (14d) | Does not open (65%) | 73% | today | 58% |  |
| 26 | [ ] | CHRONO TRIGGER (STEAM) | 16 | 28 | 57% (14d) | Does not open (60%) | 82% | today | 96% |  |
| 27 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (88%) | 95% | 2d ago | 92% |  |
| 28 | [ ] | Monster Hunter: World (STEAM) | 14 | 28 | 50% (14d) | No graphics (56%) | 85% | today | 78% |  |
| 29 | [ ] | Clair Obscur: Expedition 33 (STEAM) | 14 | 26 | 54% (14d) | Graphics glitches (41%) | 88% | today | 79% |  |
| 30 | [ ] | Sorry We're Closed (EPIC) | 14 | 25 | 56% (14d) | Does not open (82%) | 74% | 3d ago | 53% (drop) |  |
| 31 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 73% | 3d ago | 70% |  |
| 32 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | 98% | 5d ago | 92% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 33 | [ ] | DOOM 3: BFG Edition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (72%) | 71% | 1d ago | 62% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 34 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 18 | 33 | 55% (since fix) | Does not open (75%) | 68% | today | 54% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 35 | [ ] | The Forest (STEAM) | 12 | 22 | 55% (14d) | Does not open (77%) | 85% | today | 88% |  |
| 36 | [ ] | Fallout: New Vegas (EPIC) | 15 | 20 | 75% (last 20) | Does not open (59%) | 84% | 1d ago | 69% |  |
| 37 | [ ] | Grand Theft Auto V (EPIC) | 19 | 20 | 95% (last 20) | Does not open (91%) | 75% | today | 65% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 38 | [ ] | Dead Island 2 (EPIC) | 15 | 20 | 75% (last 20) | Does not open (82%) | 81% | 1d ago | 60% |  |
| 39 | [ ] | Welcome to Elderfield (STEAM) | 13 | 20 | 65% (last 20) | Does not open (72%) | 67% | 1d ago | 66% |  |
| 40 | [ ] | Castlevania Dominus Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (92%) | 95% | 2d ago | 84% |  |
| 41 | [ ] | Marvel’s Spider-Man Remastered (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 65% | today | 78% |  |
| 42 | [ ] | Library Of Ruina (STEAM) | 11 | 21 | 52% (14d) | Does not open (69%) | 86% | 1d ago | 77% |  |
| 43 | [ ] | Red Dead Redemption 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (98%) | 83% | 2d ago | 81% |  |
| 44 | [ ] | Hogwarts Legacy (EPIC) | 15 | 20 | 75% (last 20) | Does not open (76%) | 67% | today | 50% |  |
| 45 | [ ] | Castlevania Advance Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (95%) | 89% | 3d ago | 79% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 46 | [ ] | Order of the Sinking Star (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | 65% | today | 79% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 47 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (75%) | 100% | 1d ago | n/a | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 48 | [ ] | Aniimo (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 85% | today | 71% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 49 | [ ] | Don't Starve Together (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 78% | 3d ago | 64% |  |
| 50 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 78% | today | 83% |  |
| 51 | [ ] | Darkest Dungeon® (EPIC) | 12 | 20 | 60% (last 20) | Does not open (64%) | 78% | 3d ago | 100% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 52 | [ ] | MIO: Memories in Orbit (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (52%) | 95% | 2d ago | 94% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 53 | [ ] | American Truck Simulator (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 78% | 1d ago | 67% |  |
| 54 | [ ] | ZERO Sievert (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | 90% | today | 71% |  |
| 55 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (51%) | 94% | today | 89% |  |
| 56 | [ ] | Prey (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 78% | 1d ago | 81% |  |
| 57 | [ ] | Sid Meier's Civilization VI (STEAM) | 15 | 20 | 75% (last 20) | Does not open (66%) | 86% | today | 70% |  |
| 58 | [ ] | eFootball™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (58%) | 60% | today | 36% (drop) |  |
| 59 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (74%) | 69% | 1d ago | 44% (drop) |  |
| 60 | [ ] | Need for Speed: Hot Pursuit (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 80% | 1d ago | 86% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 61 | [ ] | Ratatan (STEAM) | 18 | 20 | 90% (last 20) | Does not open (47%) | 98% | 6d ago | n/a |  |
| 62 | [ ] | Disgaea 5 Complete (STEAM) | 16 | 20 | 80% (last 20) | Does not open (76%) | 92% | today | 91% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 63 | [ ] | Dota 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (78%) | 77% | today | 93% |  |
| 64 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 15 | 20 | 75% (last 20) | Graphics glitches (44%) | 84% | today | 78% |  |
| 65 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (62%) | 96% | 1d ago | 100% |  |
| 66 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (51%) | 80% | 1d ago | 42% (drop) | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 67 | [ ] | Divinity: Original Sin 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 90% | today | 80% |  |
| 68 | [ ] | Forza Horizon 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (44%) | 67% | today | 19% (drop) | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 69 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 15 | 20 | 75% (last 20) | Does not open (48%) | 67% | 7d ago | 50% |  |
| 70 | [ ] | Abiotic Factor (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 69% | 1d ago | 75% |  |
| 71 | [ ] | Resident Evil 7 Biohazard (STEAM) | 11 | 20 | 55% (last 20) | Does not open (68%) | 79% | today | 69% |  |
| 72 | [ ] | Happy Wheels (STEAM) | 19 | 20 | 95% (last 20) | No graphics (52%) | 72% | 5d ago | 55% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 73 | [ ] | Need for Speed™ Rivals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (62%) | 76% | 1d ago | 100% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 74 | [ ] | Fable - The Lost Chapters (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (49%) | 84% | today | 84% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 75 | [ ] | Last Epoch (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 88% | today | 68% |  |
| 76 | [ ] | Cave Story+ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | 86% | 1d ago | 67% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 77 | [ ] | Poppy Playtime (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 73% | 3d ago | 65% |  |
| 78 | [ ] | Dead Space (STEAM) | 14 | 20 | 70% (last 20) | Does not open (53%) | 82% | 1d ago | 77% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 79 | [ ] | Cry of Fear (STEAM) | 13 | 20 | 65% (last 20) | Does not open (48%) | 77% | 1d ago | 71% |  |
| 80 | [ ] | Resident Evil Village (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 90% | today | 81% |  |
| 81 | [ ] | Assassin's Creed II (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | 63% | 5d ago | 70% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 82 | [ ] | River City Girls (EPIC) | 14 | 20 | 70% (last 20) | Does not open (48%) | 79% | today | 40% (drop) |  |
| 83 | [ ] | Alabaster Dawn (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (48%) | 91% | today | 89% |  |
| 84 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (82%) | 69% | today | n/a | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 85 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (82%) | 93% | today | n/a | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 86 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (54%) | 85% | today | 65% |  |
| 87 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 12 | 20 | 60% (last 20) | Does not open (100%) | 97% | 1d ago | 80% |  |
| 88 | [ ] | Bejeweled 3 (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 93% | 2d ago | 88% |  |
| 89 | [ ] | Sid Meier's Civilization V (STEAM) | 16 | 20 | 80% (last 20) | Does not open (76%) | 60% | 1d ago | 63% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 90 | [ ] | Until Then (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 82% | 1d ago | 62% |  |
| 91 | [ ] | Mini Motorways (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 70% | today | 58% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 92 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 65% | 5d ago | 64% |  |
| 93 | [ ] | Lethal Company (STEAM) | 10 | 20 | 50% (last 20) | Does not open (42%) | 81% | today | 74% |  |
| 94 | [ ] | Red Dead Redemption (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | 69% | 23d ago | n/a | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 95 | [ ] | Palia (STEAM) | 15 | 20 | 75% (last 20) | Does not open (59%) | 72% | 5d ago | n/a | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 96 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 14 | 20 | 70% (last 20) | Does not open (41%) | 74% | 4d ago | 80% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 97 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 13 | 20 | 65% (last 20) | Does not open (82%) | 72% | 3d ago | n/a | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 98 | [ ] | OMORI (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 75% | 1d ago | 50% (drop) | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 99 | [ ] | Sifu (EPIC) | 10 | 20 | 50% (last 20) | Does not open (65%) | 66% | 1d ago | 33% (drop) |  |
| 100 | [ ] | TBH: Task Bar Hero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (64%) | 87% | today | 86% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 101 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 90% | 3d ago | 79% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 102 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (57%) | 64% | today | n/a |  |
| 103 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | No graphics (35%) | 65% | 4d ago | 25% (drop) |  |
| 104 | [ ] | Cyberpunk 2077 (GOG) | 11 | 20 | 55% (last 20) | Does not open (71%) | 71% | today | 52% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 105 | [ ] | Heavy Rain (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (63%) | 86% | today | 90% |  |
| 106 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 60% | 2d ago | 33% (drop) | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 107 | [ ] | Vampire Survivors (EPIC) | 14 | 20 | 70% (last 20) | Does not open (58%) | 60% | 5d ago | 38% (drop) | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 108 | [ ] | Yakuza: Like a Dragon (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 66% | 4d ago | n/a |  |
| 109 | [ ] | Minecraft Dungeons II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (82%) | 69% | 3d ago | 65% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 110 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (52%) | 66% | today | 76% |  |
| 111 | [ ] | Dishonored - Definitive Edition (EPIC) | 11 | 20 | 55% (last 20) | Does not open (89%) | 81% | today | 71% |  |
| 112 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 19 | 20 | 95% (last 20) | Does not open (62%) | 82% | 11d ago | n/a | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 113 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (50%) | 86% | 1d ago | 71% |  |
| 114 | [ ] | Driving Rogue (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 92% | 5d ago | 82% |  |
| 115 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 60% | 3d ago | n/a | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 116 | [ ] | Call of Duty: World at War (STEAM) | 14 | 20 | 70% (last 20) | Does not open (44%) | 86% | 4d ago | 63% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 117 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 94% | 13d ago | n/a |  |
| 118 | [ ] | Fallout (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 71% | 1d ago | 73% |  |
| 119 | [ ] | Tails of Iron (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 89% | 3d ago | n/a |  |
| 120 | [ ] | Sonic Generations (STEAM) | 16 | 20 | 80% (last 20) | Does not open (69%) | 66% | 4d ago | 91% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 121 | [ ] | Moonstone Island (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (60%) | 85% | 1d ago | 71% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 122 | [ ] | The Legend of Heroes: Trails in the Sky (STEAM) | 10 | 20 | 50% (last 20) | Does not open (55%) | 94% | today | 95% |  |
| 123 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 10 | 20 | 50% (last 20) | Does not open (66%) | 83% | 4d ago | n/a |  |
| 124 | [ ] | PowerWash Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (85%) | 79% | 1d ago | 100% |  |
| 125 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 67% | 10d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 126 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 17 | 20 | 85% (last 20) | Controller issues (86%) | 93% | 3d ago | 91% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 127 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (73%) | 63% | today | n/a | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 128 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 76% | 1d ago | n/a | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 129 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 11 | 20 | 55% (last 20) | Does not open (67%) | 73% | today | 42% (drop) |  |
| 130 | [ ] | ENA: Dream BBQ (STEAM) | 10 | 20 | 50% (last 20) | Does not open (43%) | 77% | 2d ago | 58% |  |
| 131 | [ ] | A Plague Tale: Innocence (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | 86% | 13d ago | n/a | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 132 | [ ] | Max Payne (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (46%) | 89% | 7d ago | n/a |  |
| 133 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (84%) | 89% | 2d ago | 90% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 134 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 65% | 3d ago | 72% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 135 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (73%) | 85% | today | 85% |  |
| 136 | [ ] | Fallout 3 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (43%) | 91% | 2d ago | 89% |  |
| 137 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (48%) | 92% | 2d ago | 82% |  |
| 138 | [ ] | Deliver At All Costs (EPIC) | 12 | 20 | 60% (last 20) | Does not open (56%) | 70% | 3d ago | 62% |  |
| 139 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 73% | today | 71% |  |
| 140 | [ ] | Street Fighter™ 6 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (81%) | 79% | today | 73% |  |
| 141 | [ ] | Mount & Blade: Warband (STEAM) | 10 | 20 | 50% (last 20) | Does not open (86%) | 89% | 1d ago | 67% |  |
| 142 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | 93% | 10d ago | n/a | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 143 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (82%) | 94% | today | n/a | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 144 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (92%) | 61% | 13d ago | n/a | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 145 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 88% | 10d ago | 85% |  |
| 146 | [ ] | Gambonanza (STEAM) | 14 | 20 | 70% (last 20) | Does not open (60%) | 95% | today | 100% |  |
| 147 | [ ] | ABZU (EPIC) | 10 | 20 | 50% (last 20) | Does not open (86%) | 90% | 3d ago | 83% |  |
| 148 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (81%) | 70% | 10d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 149 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (78%) | 90% | today | n/a | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 150 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 75% | 5d ago | n/a |  |
| 151 | [ ] | Gothic 1 Classic (STEAM) | 12 | 20 | 60% (last 20) | Does not open (61%) | 83% | 3d ago | 59% (drop) |  |
| 152 | [ ] | Oxygen Not Included (STEAM) | 12 | 20 | 60% (last 20) | Does not open (74%) | 60% | 3d ago | 81% |  |
| 153 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (62%) | 85% | 7d ago | n/a | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 154 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (61%) | 81% | 3d ago | n/a | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 155 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | 82% | 11d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 156 | [ ] | Rivals of Aether II (STEAM) | 15 | 20 | 75% (last 20) | Does not open (54%) | 66% | today | 10% (drop) | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 157 | [ ] | Stellar Blade™ (STEAM) | 14 | 20 | 70% (last 20) | No graphics (43%) | 81% | 2d ago | 79% |  |
| 158 | [ ] | Tabletop Simulator (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 62% | 4d ago | 77% |  |
| 159 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (52%) | 65% | today | 53% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 160 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | Does not open (53%) | 84% | 3d ago | 100% |  |
| 161 | [ ] | Sonic Lost World (STEAM) | 12 | 20 | 60% (last 20) | No graphics (64%) | 81% | 5d ago | 76% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 162 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 11 | 20 | 55% (last 20) | Does not open (59%) | 73% | 9d ago | 62% |  |
| 163 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 64% | 3d ago | n/a | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 164 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 85% | 1d ago | 82% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 165 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (57%) | 62% | 10d ago | n/a | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 166 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (64%) | 65% | 1d ago | 50% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 167 | [ ] | Chained Echoes (GOG) | 14 | 20 | 70% (last 20) | Does not open (60%) | 68% | 4d ago | n/a |  |
| 168 | [ ] | Control Ultimate Edition (GOG) | 13 | 20 | 65% (last 20) | Does not open (76%) | 88% | 1d ago | 73% |  |
| 169 | [ ] | Hollow Knight: Silksong (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 61% | 1d ago | 71% |  |
| 170 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (73%) | 70% | 4d ago | n/a | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 171 | [ ] | Capcom Arcade Stadium (STEAM) | 16 | 20 | 80% (last 20) | Does not open (84%) | 70% | 12d ago | n/a | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 172 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | 73% | 4d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 173 | [ ] | Unturned (STEAM) | 12 | 20 | 60% (last 20) | Does not open (47%) | 71% | 1d ago | 75% |  |
| 174 | [ ] | Fallout 4: Game of the Year Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (50%) | 71% | 4d ago | 73% |  |
| 175 | [ ] | Counter-Strike:Global Offensive (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 77% | 2d ago | 75% |  |
| 176 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (61%) | 92% | 7d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 177 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 93% | 22d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 178 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 90% | today | 80% |  |
| 179 | [ ] | One-armed robber (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (65%) | 72% | 4d ago | 50% (drop) |  |
| 180 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 14 | 20 | 70% (last 20) | Does not open (69%) | 69% | 6d ago | n/a | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 181 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 60% | 8d ago | n/a |  |
| 182 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (82%) | 92% | 12d ago | 70% |  |
| 183 | [ ] | State of Decay: Year-One (STEAM) | 11 | 20 | 55% (last 20) | Does not open (69%) | 76% | today | 65% |  |
| 184 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 87% | 2d ago | n/a |  |
| 185 | [ ] | Dishonored 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (89%) | 84% | 3d ago | 71% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 186 | [ ] | The Witcher: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (59%) | 69% | 5d ago | n/a | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 187 | [ ] | Escape from Duckov (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (69%) | 95% | 2d ago | 100% |  |
| 188 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (47%) | 62% | 2d ago | 53% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 189 | [ ] | Subnautica 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (58%) | 60% | 1d ago | n/a | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 190 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | 95% | 1d ago | n/a | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 191 | [ ] | Digimon Survive (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (74%) | 96% | today | n/a |  |
| 192 | [ ] | Final Fantasy IV (3D Remake) (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 95% | 1d ago | n/a |  |
| 193 | [ ] | Stumble Guys (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 69% | 1d ago | 62% |  |
| 194 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (56%) | 68% | 6d ago | n/a | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 195 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (69%) | 87% | 17d ago | n/a | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 196 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (72%) | 84% | today | n/a | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 197 | [ ] | Supermarket Together (STEAM) | 15 | 20 | 75% (last 20) | Does not open (73%) | 67% | 7d ago | 77% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 198 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | 82% | today | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 199 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (62%) | 71% | today | 27% (drop) |  |
| 200 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (60%) | 66% | 2d ago | n/a |  |
| 201 | [ ] | TurretGirls (STEAM) | 12 | 20 | 60% (last 20) | No graphics (75%) | 91% | 2d ago | 80% |  |
| 202 | [ ] | Limbus Company (STEAM) | 11 | 20 | 55% (last 20) | Does not open (85%) | 82% | today | 93% |  |
| 203 | [ ] | Mortal Kombat 11 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 69% | 4d ago | n/a |  |
| 204 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 94% | 1d ago | n/a | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 205 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 88% | 6d ago | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 206 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (61%) | 94% | 7d ago | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 207 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 82% | 15d ago | n/a | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 208 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 69% | 1d ago | n/a | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 209 | [ ] | Darksiders (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 80% | 18d ago | 70% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 210 | [ ] | A Plague Tale: Innocence (EPIC) | 11 | 20 | 55% (last 20) | Does not open (71%) | 61% | 18d ago | n/a |  |
| 211 | [ ] | GOD EATER RESURRECTION (STEAM) | 14 | 20 | 70% (last 20) | Does not open (56%) | 67% | 16d ago | n/a |  |
| 212 | [ ] | My Summer Car (STEAM) | 12 | 20 | 60% (last 20) | Does not open (61%) | 81% | 1d ago | n/a |  |
| 213 | [ ] | Goat Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 73% | 4d ago | n/a |  |
| 214 | [ ] | Battle Brothers (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 73% | today | 80% |  |
| 215 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 81% | today | 73% |  |
| 216 | [ ] | The Lantern of the Laughless Saint (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 64% | 9d ago | n/a | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 217 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 90% | today | n/a |  |
| 218 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | 67% | 9d ago | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 219 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (92%) | 86% | 25d ago | n/a |  |
| 220 | [ ] | Invisible, Inc. (STEAM) | 15 | 20 | 75% (last 20) | Does not open (63%) | 69% | 13d ago | n/a |  |
| 221 | [ ] | Maneater (STEAM) | 15 | 20 | 75% (last 20) | Does not open (92%) | 64% | 6d ago | n/a |  |
| 222 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 15 | 20 | 75% (last 20) | No graphics (53%) | 75% | 1d ago | n/a | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 223 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 80% | 15d ago | n/a |  |
| 224 | [ ] | Return to Monkey Island (STEAM) | 14 | 20 | 70% (last 20) | No graphics (61%) | 77% | 5d ago | n/a |  |
| 225 | [ ] | Ultimate Custom Night (STEAM) | 14 | 20 | 70% (last 20) | No graphics (68%) | 73% | 14d ago | n/a | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 226 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 79% | today | n/a | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 227 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | 61% | 2d ago | 40% (drop) | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 228 | [ ] | CRUEL (STEAM) | 13 | 20 | 65% (last 20) | Does not open (88%) | 75% | today | n/a | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 229 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (44%) | 83% | 5d ago | n/a |  |
| 230 | [ ] | Trailmakers (STEAM) | 12 | 20 | 60% (last 20) | Does not open (44%) | 87% | today | n/a |  |
| 231 | [ ] | Jade Empire: Special Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 75% | 3d ago | n/a | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 232 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | 91% | today | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 233 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (42%) | 77% | 7d ago | n/a | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 234 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 85% | 2d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 235 | [ ] | SnowRunner (STEAM) | 13 | 20 | 65% (last 20) | Does not open (96%) | 78% | 3d ago | n/a | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 236 | [ ] | Zero Escape: The Nonary Games (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 64% | 2d ago | 70% |  |
| 237 | [ ] | Lucid Blocks (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 62% | today | 50% |  |
| 238 | [ ] | Revolution Idle (STEAM) | 12 | 20 | 60% (last 20) | Does not open (43%) | 80% | 5d ago | n/a |  |
| 239 | [ ] | Resident Evil Revelations 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (40%) | 83% | 5d ago | 71% |  |
| 240 | [ ] | Secrets of Grindea (STEAM) | 11 | 20 | 55% (last 20) | Does not open (45%) | 72% | 18d ago | n/a | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 241 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 20 | 80% (last 20) | Does not open (82%) | 63% | 19d ago | n/a | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 242 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 64% | today | n/a |  |
| 243 | [ ] | Cat Mail Co. (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 88% | today | n/a |  |
| 244 | [ ] | Deus Ex™ GOTY Edition (GOG) | 12 | 20 | 60% (last 20) | No graphics (41%) | 88% | 12d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 245 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 67% | 3d ago | n/a |  |
| 246 | [ ] | Bongo Cat (STEAM) | 15 | 20 | 75% (last 20) | Does not open (71%) | 72% | 6d ago | n/a | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 247 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 13 | 20 | 65% (last 20) | No graphics (37%) | 83% | 1d ago | n/a | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 248 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (83%) | 81% | 4d ago | n/a | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 249 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | 60% | 12d ago | 25% (drop) |  |
| 250 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (100%) | 76% | 7d ago | n/a |  |
| 251 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 95% | 4d ago | n/a |  |
| 252 | [ ] | Hero Siege (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (50%) | 72% | 1d ago | 91% |  |
| 253 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 77% | 5d ago | n/a |  |
| 254 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (44%) | 92% | 12d ago | n/a |  |
| 255 | [ ] | Tales of Zestiria (STEAM) | 14 | 20 | 70% (last 20) | Does not open (80%) | 67% | 17d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 256 | [ ] | Capcom Fighting Collection (STEAM) | 14 | 20 | 70% (last 20) | Does not open (76%) | 73% | 3d ago | n/a | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 257 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (95%) | 95% | 3d ago | 89% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 258 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (45%) | 67% | 7d ago | n/a |  |
| 259 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 12 | 20 | 60% (last 20) | Does not open (57%) | 71% | 7d ago | n/a | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 260 | [ ] | 12 is Better Than 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (45%) | 83% | 7d ago | n/a |  |
| 261 | [ ] | Big Walk (STEAM) | 11 | 20 | 55% (last 20) | Does not open (65%) | 70% | 9d ago | 36% (drop) |  |
| 262 | [ ] | Hitman: Absolution (GOG) | 11 | 20 | 55% (last 20) | Does not open (85%) | 77% | 6d ago | n/a |  |
| 263 | [ ] | Hatred (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 88% | 4d ago | n/a |  |
| 264 | [ ] | Football Manager 2024 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (91%) | 70% | 4d ago | 30% (drop) |  |
| 265 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 94% | today | 86% |  |
| 266 | [ ] | Chef Knight (STEAM) | 14 | 20 | 70% (last 20) | Does not open (100%) | 64% | 16d ago | n/a |  |
| 267 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 14 | 20 | 70% (last 20) | Does not open (85%) | 67% | 4d ago | n/a | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 268 | [ ] | Timberborn (STEAM) | 13 | 20 | 65% (last 20) | No graphics (62%) | 84% | 9d ago | n/a |  |
| 269 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (89%) | 80% | 4d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 270 | [ ] | Mortal Shell (EPIC) | 13 | 20 | 65% (last 20) | No graphics (64%) | 72% | today | 20% (drop) |  |
| 271 | [ ] | AER Memories of Old (EPIC) | 13 | 20 | 65% (last 20) | Does not open (85%) | 93% | today | n/a |  |
| 272 | [ ] | Allumeria (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 69% | 2d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 273 | [ ] | Sons Of The Forest (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 72% | 5d ago | n/a |  |
| 274 | [ ] | Disgaea 4 Complete+ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (43%) | 91% | 11d ago | n/a | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 275 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (77%) | 75% | 25d ago | n/a |  |
| 276 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 67% | 3d ago | 55% |  |
| 277 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 62% | 6d ago | 73% |  |
| 278 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 88% | 4d ago | n/a |  |
| 279 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 75% | 3d ago | 67% |  |
| 280 | [ ] | Astral Party  (STEAM) | 10 | 20 | 50% (last 20) | Does not open (83%) | 94% | today | n/a |  |
| 281 | [ ] | MX Bikes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 93% | today | n/a |  |
| 282 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 75% | 2d ago | n/a |  |
| 283 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (45%) | 77% | 4d ago | n/a | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 284 | [ ] | Hylics (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 97% | 9d ago | n/a |  |
| 285 | [ ] | Antichamber (STEAM) | 11 | 20 | 55% (last 20) | Does not open (33%) | 73% | 1d ago | n/a |  |
| 286 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (57%) | 91% | 2d ago | n/a |  |
| 287 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | No graphics (70%) | 78% | 1d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 288 | [ ] | Monster Boy And The Cursed Kingdom (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (84%) | 89% | 12d ago | n/a |  |
| 289 | [ ] | This War of Mine (STEAM) | 10 | 20 | 50% (last 20) | No graphics (53%) | 61% | 12d ago | 36% (drop) |  |
| 290 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (42%) | 91% | 10d ago | 100% |  |
| 291 | [ ] | Katanaut (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | 62% | 6d ago | n/a | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 292 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 60% | 2d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 293 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | 83% | 6d ago | n/a |  |
| 294 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 81% | 40d ago | n/a |  |
| 295 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (92%) | 89% | 7d ago | n/a |  |
| 296 | [ ] | Gloomwood (STEAM) | 11 | 20 | 55% (last 20) | No graphics (57%) | 67% | 3d ago | n/a |  |
| 297 | [ ] | Pinball FX Classic (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 95% | 7d ago | n/a |  |
| 298 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 64% | 28d ago | n/a |  |
| 299 | [ ] | Intravenous (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 79% | 3d ago | n/a |  |
| 300 | [ ] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 88% | 8d ago | n/a |  |
| 301 | [ ] | Ghostwire Tokyo (EPIC) | 13 | 20 | 65% (last 20) | Does not open (88%) | 79% | 1d ago | n/a |  |
| 302 | [ ] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 68% | today | n/a | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 303 | [ ] | Legend of Grimrock 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 85% | 5d ago | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 304 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | 90% | today | n/a |  |
| 305 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (56%) | 92% | 14d ago | n/a | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 306 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (69%) | 95% | today | 100% |  |
| 307 | [ ] | Assassin's Creed Odyssey (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 67% | 5d ago | 70% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 308 | [ ] | GRANDIA II HD Remaster (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 67% | 15d ago | n/a |  |
| 309 | [ ] | Subnautica: Below Zero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 70% | 3d ago | n/a |  |
| 310 | [ ] | Need for Speed™ Unbound (STEAM) | 12 | 20 | 60% (last 20) | Does not open (87%) | 67% | 15d ago | n/a | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 311 | [ ] | Shift At Midnight (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | 80% | 6d ago | n/a |  |
| 312 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 71% | 5d ago | 70% |  |
| 313 | [ ] | Haydee (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 78% | 6d ago | n/a |  |
| 314 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 73% | 5d ago | n/a |  |
| 315 | [ ] | Killing Floor (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (100%) | 84% | 4d ago | n/a |  |
| 316 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 88% | 2d ago | 82% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 317 | [ ] | Castle in the Clouds (STEAM) | 10 | 20 | 50% (last 20) | No graphics (63%) | 78% | 12d ago | n/a |  |
| 318 | [ ] | WORLD OF FINAL FANTASY (STEAM) | 10 | 20 | 50% (last 20) | No graphics (58%) | 75% | 5d ago | n/a |  |
| 319 | [ ] | Batman™: Arkham Origins (GOG) | 10 | 20 | 50% (last 20) | Does not open (67%) | 100% | today | n/a |  |
| 320 | [ ] | Cruelty Squad (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | 94% | 9d ago | n/a |  |
| 321 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 67% | 3d ago | n/a | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 322 | [ ] | Forgive Me Father (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 64% | 4d ago | n/a |  |
| 323 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 91% | 13d ago | n/a |  |
| 324 | [ ] | Sid Meier's Civilization VI (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 82% | 9d ago | n/a |  |
| 325 | [ ] | Beatblock (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 91% | 3d ago | n/a |  |

## Recently recovered (482)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Slay the Spire (STEAM) | 1323 | 2026-11-09 | 1652 | 62% | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [x] | Grim Dawn (STEAM) | 534 | 2026-11-08 | 593 | 62% |  |
| 3 | [x] | FINAL FANTASY RESONANCE (STEAM) | 399 | 2026-10-24 | 904 | 76% |  |
| 4 | [x] | Half-Life (STEAM) | 350 | 2026-11-09 | 621 | 71% |  |
| 5 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 234 | 2026-10-19 | 293 | 74% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 6 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 231 | 2026-11-09 | 276 | 65% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 7 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 228 | 2026-11-09 | 320 | 90% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 8 | [x] | MONSTER HUNTER RISE (STEAM) | 209 | 2026-11-09 | 506 | 63% |  |
| 9 | [x] | BeamNG.drive (STEAM) | 202 | 2026-11-09 | 243 | 83% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 10 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 201 | 2026-11-09 | 358 | 76% |  |
| 11 | [x] | Devil May Cry HD Collection (STEAM) | 199 | 2026-10-19 | 284 | 80% |  |
| 12 | [x] | OMORI (STEAM) | 191 | 2026-11-09 | 235 | 75% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 13 | [x] | DRAGON BALL FighterZ (STEAM) | 183 | 2026-11-01 | 219 | 75% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 14 | [x] | Spelunky 2 (STEAM) | 180 | 2026-11-01 | 213 | 68% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 15 | [x] | Rocket League® (EPIC) | 172 | 2026-11-09 | 277 | 60% | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 16 | [x] | DREDGE (EPIC) | 172 | 2026-11-09 | 214 | 73% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 17 | [x] | Sid Meier's Civilization V (STEAM) | 168 | 2026-11-10 | 179 | 60% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 18 | [x] | BioShock (STEAM) | 152 | 2026-11-09 | 298 | 74% |  |
| 19 | [x] | Geometry Dash (STEAM) | 148 | 2026-11-11 | 442 | 48% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 20 | [x] | Prototype (STEAM) | 143 | 2026-11-11 | 208 | 57% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 21 | [x] | Burnout Paradise: The Ultimate Box (STEAM) | 137 | 2026-10-16 | 237 | 73% |  |
| 22 | [x] | Castlevania Advance Collection (STEAM) | 133 | 2026-11-09 | 204 | 89% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 23 | [x] | Team Fortress 2 (STEAM) | 132 | 2026-11-09 | 227 | 75% |  |
| 24 | [x] | Counter-Strike (STEAM) | 128 | 2026-11-11 | 208 | 47% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 25 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 128 | 2026-11-09 | 169 | 68% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 26 | [x] | Minecraft Dungeons II (STEAM) | 128 | 2026-11-09 | 147 | 69% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 27 | [x] | Mirror's Edge (STEAM) | 127 | 2026-11-09 | 178 | 71% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 28 | [x] | Far Cry® 3 (STEAM) | 124 | 2026-11-09 | 139 | 60% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 29 | [x] | Call of Duty: Black Ops III (STEAM) | 120 | 2026-10-18 | 251 | 78% |  |
| 30 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 120 | 2026-10-18 | 175 | 78% |  |
| 31 | [x] | Assassin's Creed II (STEAM) | 118 | 2026-11-10 | 123 | 63% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 32 | [x] | Caravan SandWitch (EPIC) | 116 | 2026-11-09 | 185 | 68% |  |
| 33 | [x] | Euro Truck Simulator 2 (STEAM) | 113 | 2026-11-10 | 210 | 56% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 34 | [x] | Aniimo (STEAM) | 112 | 2026-11-09 | 151 | 85% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 35 | [x] | The Witcher: Enhanced Edition (STEAM) | 112 | 2026-11-09 | 131 | 69% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 36 | [x] | Cave Story+ (STEAM) | 112 | 2026-11-09 | 123 | 86% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 37 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 107 | 2026-11-09 | 144 | 89% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 38 | [x] | Moonstone Island (STEAM) | 98 | 2026-11-09 | 131 | 85% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 39 | [x] | Happy Wheels (STEAM) | 97 | 2026-11-09 | 117 | 72% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 40 | [x] | Catherine Classic (STEAM) | 89 | 2026-11-09 | 165 | 73% |  |
| 41 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 89 | 2026-11-09 | 114 | 93% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 42 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 88 | 2026-11-09 | 142 | 70% |  |
| 43 | [x] | Hi-Fi RUSH (STEAM) | 88 | 2026-11-11 | 122 | 48% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 44 | [x] | Quake (STEAM) | 86 | 2026-11-09 | 258 | 84% |  |
| 45 | [x] | DOOM 3: BFG Edition (STEAM) | 84 | 2026-11-09 | 123 | 71% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 46 | [x] | Ultra Street Fighter IV (STEAM) | 83 | 2026-10-17 | 180 | 66% |  |
| 47 | [x] | Cry of Fear (STEAM) | 83 | 2026-10-18 | 164 | 77% |  |
| 48 | [x] | Vital Shell (STEAM) | 83 | 2026-11-09 | 128 | 86% |  |
| 49 | [x] | FINAL FANTASY XIII-2 (STEAM) | 81 | 2026-11-09 | 84 | 64% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 50 | [x] | Age of Empires II: Definitive Edition (STEAM) | 80 | 2026-11-10 | 95 | 65% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 51 | [x] | Psychonauts (STEAM) | 79 | 2026-11-09 | 143 | 94% |  |
| 52 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 79 | 2026-10-18 | 133 | 96% |  |
| 53 | [x] | STEINS;GATE (STEAM) | 79 | 2026-11-09 | 112 | 91% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 54 | [x] | Don't Starve Together (STEAM) | 75 | 2026-10-16 | 156 | 78% |  |
| 55 | [x] | Brawlhalla (STEAM) | 74 | 2026-11-09 | 147 | 73% |  |
| 56 | [x] | Ballionaire (STEAM) | 74 | 2026-11-09 | 120 | 89% |  |
| 57 | [x] | Sovereign Tower (STEAM) | 73 | 2026-11-09 | 127 | 79% |  |
| 58 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 73 | 2026-11-09 | 109 | 84% |  |
| 59 | [x] | Disgaea 5 Complete (STEAM) | 72 | 2026-11-09 | 84 | 92% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 60 | [x] | Spyro™ Reignited Trilogy (STEAM) | 70 | 2026-11-09 | 110 | 73% |  |
| 61 | [x] | Need for Speed: Hot Pursuit (STEAM) | 70 | 2026-11-09 | 104 | 80% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 62 | [x] | Dota 2 (STEAM) | 69 | 2026-11-09 | 103 | 77% |  |
| 63 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 68 | 2026-11-09 | 101 | 80% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 64 | [x] | The Sims™ 4 (STEAM) | 68 | 2026-11-09 | 90 | 73% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 65 | [x] | Bayonetta (STEAM) | 67 | 2026-10-18 | 206 | 83% |  |
| 66 | [x] | Stardew Valley (GOG) | 67 | 2026-11-11 | 119 | 65% |  |
| 67 | [x] | American Truck Simulator (STEAM) | 67 | 2026-11-09 | 111 | 78% |  |
| 68 | [x] | Fable - The Lost Chapters (STEAM) | 67 | 2026-11-09 | 104 | 84% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 69 | [x] | Diablo® IV (STEAM) | 67 | 2026-11-11 | 79 | 60% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 70 | [x] | MIO: Memories in Orbit (STEAM) | 66 | 2026-11-09 | 122 | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 71 | [x] | Cyberpunk 2077 (GOG) | 66 | 2026-11-09 | 84 | 71% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 72 | [x] | Call of Juarez Gunslinger (STEAM) | 66 | 2026-11-09 | 81 | 76% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 73 | [x] | Hogwarts Legacy (EPIC) | 65 | 2026-11-09 | 98 | 67% |  |
| 74 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 64 | 2026-11-11 | 80 | 50% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 75 | [x] | Don't Starve (STEAM) | 63 | 2026-10-16 | 156 | 80% |  |
| 76 | [x] | Fallout (STEAM) | 63 | 2026-11-09 | 98 | 71% |  |
| 77 | [x] | Order of the Sinking Star (STEAM) | 63 | 2026-11-09 | 91 | 65% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 78 | [x] | Gunfire Reborn (STEAM) | 63 | 2026-11-09 | 69 | 93% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 79 | [x] | Firewatch (STEAM) | 62 | 2026-11-10 | 118 | 66% |  |
| 80 | [x] | eFootball™ (STEAM) | 62 | 2026-11-09 | 91 | 60% |  |
| 81 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 62 | 2026-11-09 | 86 | 80% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 82 | [x] | Poppy Playtime (STEAM) | 61 | 2026-11-09 | 106 | 73% |  |
| 83 | [x] | Hollow Knight: Silksong (GOG) | 61 | 2026-11-10 | 99 | 61% |  |
| 84 | [x] | Sol Cesto (EPIC) | 61 | 2026-11-09 | 63 | 69% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 85 | [x] | Borderlands 3 (STEAM) | 60 | 2026-11-09 | 83 | 88% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 86 | [x] | Borderlands: The Pre-Sequel (STEAM) | 59 | 2026-11-09 | 93 | 65% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 87 | [x] | Darksiders (STEAM) | 59 | 2026-11-09 | 74 | 80% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 88 | [x] | Deskrawl: Idle ARPG (STEAM) | 58 | 2026-11-09 | 72 | 87% | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 89 | [x] | A Plague Tale: Innocence (STEAM) | 58 | 2026-11-09 | 61 | 86% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 90 | [x] | Mini Motorways (STEAM) | 57 | 2026-11-09 | 97 | 70% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 91 | [x] | TBH: Task Bar Hero (STEAM) | 57 | 2026-11-09 | 91 | 87% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 92 | [x] | Until Then (STEAM) | 56 | 2026-10-17 | 94 | 82% |  |
| 93 | [x] | Sonic Generations (STEAM) | 56 | 2026-11-09 | 64 | 66% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 94 | [x] | Starbound (STEAM) | 55 | 2026-11-09 | 87 | 77% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 95 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 55 | 2026-11-09 | 86 | 90% |  |
| 96 | [x] | Call of Duty: World at War (STEAM) | 54 | 2026-11-09 | 78 | 86% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 97 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 53 | 2026-10-25 | 100 | 63% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 98 | [x] | Deadlock (STEAM) | 53 | 2026-10-16 | 74 | 87% |  |
| 99 | [x] | Dead Space (STEAM) | 53 | 2026-10-18 | 67 | 82% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 100 | [x] | Alex Kidd in Miracle World DX (EPIC) | 53 | 2026-11-09 | 61 | 72% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 101 | [x] | Grand Theft Auto V (EPIC) | 53 | 2026-11-09 | 59 | 75% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 102 | [x] | Overwatch® (STEAM) | 53 | 2026-11-10 | 56 | 59% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 103 | [x] | Sonic Adventure DX (STEAM) | 51 | 2026-10-17 | 89 | 67% |  |
| 104 | [x] | A Plague Tale: Innocence (EPIC) | 51 | 2026-11-09 | 87 | 61% |  |
| 105 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 51 | 2026-11-09 | 86 | 63% |  |
| 106 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 51 | 2026-11-09 | 84 | 52% |  |
| 107 | [x] | Oxygen Not Included (STEAM) | 50 | 2026-11-11 | 84 | 60% |  |
| 108 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 50 | 2026-11-09 | 79 | 82% |  |
| 109 | [x] | Last Epoch (STEAM) | 50 | 2026-11-09 | 74 | 88% |  |
| 110 | [x] | Vampire Survivors (EPIC) | 50 | 2026-11-09 | 73 | 60% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 111 | [x] | Darkest Dungeon® (EPIC) | 49 | 2026-11-09 | 89 | 78% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 112 | [x] | Big Walk (STEAM) | 49 | 2026-11-09 | 77 | 70% |  |
| 113 | [x] | MudRunner (STEAM) | 48 | 2026-10-24 | 105 | 62% |  |
| 114 | [x] | Okami HD (STEAM) | 48 | 2026-11-09 | 93 | 91% |  |
| 115 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 48 | 2026-10-19 | 92 | 68% |  |
| 116 | [x] | Abiotic Factor (STEAM) | 48 | 2026-10-18 | 82 | 69% |  |
| 117 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 48 | 2026-11-09 | 55 | 90% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 118 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 2026-11-09 | 74 | 92% |  |
| 119 | [x] | Rivals of Aether II (STEAM) | 47 | 2026-11-09 | 66 | 66% | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 120 | [x] | Heroes of Might & Magic III - HD Edition (STEAM) | 46 | 2026-11-11 | 60 | 61% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 121 | [x] | Sheepy: A Short Adventure (STEAM) | 46 | 2026-11-09 | 55 | 82% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 122 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 45 | 2026-11-09 | 79 | 85% |  |
| 123 | [x] | Moonlighter (EPIC) | 45 | 2026-11-09 | 49 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 124 | [x] | Ace Attorney Investigations Collection (STEAM) | 44 | 2026-11-09 | 74 | 89% |  |
| 125 | [x] | Sonic Origins (STEAM) | 43 | 2026-11-09 | 76 | 85% |  |
| 126 | [x] | Tomb Raider GOTY (GOG) | 42 | 2026-10-17 | 102 | 94% |  |
| 127 | [x] | PROTOTYPE 2 (STEAM) | 42 | 2026-10-18 | 88 | 70% |  |
| 128 | [x] | Frostpunk (STEAM) | 42 | 2026-11-09 | 65 | 68% |  |
| 129 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 42 | 2026-11-09 | 63 | 70% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 130 | [x] | Sonic Lost World (STEAM) | 42 | 2026-11-09 | 60 | 81% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 131 | [x] | Guildrun Demo (STEAM) | 42 | 2026-11-09 | 59 | 78% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 132 | [x] | Forza Horizon 4 (STEAM) | 42 | 2026-11-09 | 58 | 67% | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 133 | [x] | Aggelos (STEAM) | 42 | 2026-11-09 | 57 | 94% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 134 | [x] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 42 | 2026-11-09 | 48 | 82% | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 135 | [x] | The Bazaar (STEAM) | 41 | 2026-11-09 | 70 | 82% |  |
| 136 | [x] | Tomb Raider: Anniversary (STEAM) | 41 | 2026-11-09 | 64 | 69% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 137 | [x] | Rayman Origins (STEAM) | 40 | 2026-10-17 | 92 | 85% |  |
| 138 | [x] | Digimon World: Next Order (STEAM) | 40 | 2026-11-09 | 78 | 90% |  |
| 139 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 40 | 2026-11-09 | 41 | 82% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 140 | [x] | Life is Strange™ (STEAM) | 39 | 2026-10-17 | 83 | 80% |  |
| 141 | [x] | Library Of Ruina (STEAM) | 39 | 2026-10-16 | 75 | 86% |  |
| 142 | [x] | FINAL FANTASY VII (2013) (STEAM) | 39 | 2026-11-09 | 57 | 72% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 143 | [x] | Capcom Arcade Stadium (STEAM) | 39 | 2026-11-09 | 48 | 70% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 144 | [x] | Dead by Daylight (STEAM) | 39 | 2026-11-09 | 43 | 85% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 145 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-11-09 | 40 | 81% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 146 | [x] | Amnesia: The Dark Descent (STEAM) | 38 | 2026-11-09 | 74 | 73% |  |
| 147 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 38 | 2026-11-09 | 71 | 92% |  |
| 148 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 38 | 2026-11-09 | 70 | 83% |  |
| 149 | [x] | Death Road to Canada (STEAM) | 37 | 2026-10-17 | 96 | 78% |  |
| 150 | [x] | Tales of ARISE (STEAM) | 37 | 2026-10-16 | 78 | 88% |  |
| 151 | [x] | Age of Empires II (2013) (STEAM) | 37 | 2026-11-09 | 63 | 66% |  |
| 152 | [x] | Street Fighter™ 6 (STEAM) | 37 | 2026-11-09 | 63 | 79% |  |
| 153 | [x] | Russian Fishing 4 (STEAM) | 37 | 2026-11-09 | 43 | 84% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 154 | [x] | CrossCode (GOG) | 37 | 2026-11-09 | 40 | 70% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 155 | [x] | Rogue Legacy (STEAM) | 36 | 2026-10-17 | 86 | 80% |  |
| 156 | [x] | Little Nightmares (STEAM) | 36 | 2026-10-16 | 78 | 68% |  |
| 157 | [x] | Cobalt Core (STEAM) | 35 | 2026-10-18 | 88 | 87% |  |
| 158 | [x] | POSTAL 2 (GOG) | 35 | 2026-11-09 | 70 | 92% |  |
| 159 | [x] | SurrounDead (STEAM) | 35 | 2026-11-09 | 67 | 95% |  |
| 160 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 35 | 2026-11-09 | 61 | 73% |  |
| 161 | [x] | XCOM 2 (STEAM) | 35 | 2026-11-09 | 59 | 100% |  |
| 162 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 35 | 2026-11-09 | 47 | 93% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 163 | [x] | Elite Dangerous (STEAM) | 35 | 2026-11-09 | 38 | 67% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 164 | [x] | Teardown (STEAM) | 34 | 2026-10-17 | 78 | 83% |  |
| 165 | [x] | Journey (STEAM) | 34 | 2026-10-27 | 74 | 67% |  |
| 166 | [x] | Salt and Sanctuary (STEAM) | 34 | 2026-10-18 | 74 | 81% |  |
| 167 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 34 | 2026-11-09 | 68 | 84% |  |
| 168 | [x] | Rocket League (STEAM) | 34 | 2026-10-17 | 59 | 71% |  |
| 169 | [x] | Hero Siege (STEAM) | 34 | 2026-11-09 | 57 | 72% |  |
| 170 | [x] | Need for Speed™ Rivals (STEAM) | 34 | 2026-11-10 | 47 | 76% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 171 | [x] | Romestead (STEAM) | 34 | 2026-11-09 | 45 | 65% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 172 | [x] | Super Animal Royale (STEAM) | 34 | 2026-11-09 | 45 | 63% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 173 | [x] | Ultimate Chicken Horse (STEAM) | 33 | 2026-10-23 | 68 | 73% |  |
| 174 | [x] | State of Decay: Year-One (STEAM) | 33 | 2026-10-18 | 66 | 76% |  |
| 175 | [x] | Hearts of Iron IV (STEAM) | 33 | 2026-11-09 | 61 | 72% |  |
| 176 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 2026-11-09 | 53 | 89% |  |
| 177 | [x] | Gauntlet™  (STEAM) | 33 | 2026-11-11 | 47 | 43% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 178 | [x] | Dishonored - Definitive Edition (EPIC) | 32 | 2026-10-17 | 79 | 81% |  |
| 179 | [x] | Mortal Kombat X (STEAM) | 32 | 2026-10-17 | 64 | 89% |  |
| 180 | [x] | COCOON (STEAM) | 32 | 2026-11-09 | 62 | 85% |  |
| 181 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 32 | 2026-11-11 | 60 | 37% |  |
| 182 | [x] | Deponia (STEAM) | 32 | 2026-11-09 | 60 | 60% |  |
| 183 | [x] | Max Payne (STEAM) | 32 | 2026-11-09 | 57 | 89% |  |
| 184 | [x] | Counter-Strike:Global Offensive (STEAM) | 32 | 2026-11-09 | 52 | 77% |  |
| 185 | [x] | Earthion (STEAM) | 32 | 2026-11-09 | 52 | 100% |  |
| 186 | [x] | SnowRunner (STEAM) | 32 | 2026-11-09 | 46 | 78% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 187 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-11-09 | 42 | 85% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 188 | [x] | Sable (EPIC) | 31 | 2026-10-18 | 70 | 65% |  |
| 189 | [x] | Torchlight II (STEAM) | 31 | 2026-10-20 | 70 | 88% |  |
| 190 | [x] | BioShock™ (GOG) | 31 | 2026-10-18 | 67 | 81% |  |
| 191 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 31 | 2026-11-09 | 66 | 68% |  |
| 192 | [x] | Stumble Guys (STEAM) | 31 | 2026-10-18 | 60 | 69% |  |
| 193 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 31 | 2026-11-09 | 50 | 86% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 194 | [x] | Nioh: Complete Edition (STEAM) | 31 | 2026-11-09 | 42 | 92% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 195 | [x] | Bloodstained: Curse of the Moon (STEAM) | 30 | 2026-10-16 | 75 | 72% |  |
| 196 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 30 | 2026-11-09 | 60 | 86% |  |
| 197 | [x] | Resident Evil Village (STEAM) | 30 | 2026-11-09 | 53 | 90% |  |
| 198 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 30 | 2026-11-09 | 50 | 66% |  |
| 199 | [x] | Sol Cesto (STEAM) | 30 | 2026-11-11 | 48 | 60% |  |
| 200 | [x] | Supermarket Together (STEAM) | 30 | 2026-11-09 | 42 | 67% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 201 | [x] | Red Dead Redemption (STEAM) | 30 | 2026-11-09 | 33 | 69% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 202 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 29 | 2026-11-09 | 58 | 88% |  |
| 203 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 2026-10-17 | 53 | 81% |  |
| 204 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 29 | 2026-11-09 | 53 | 67% |  |
| 205 | [x] | Aethermancer (STEAM) | 29 | 2026-10-18 | 51 | 84% |  |
| 206 | [x] | Prince of Persia: The Sands of Time (STEAM) | 29 | 2026-11-09 | 50 | 86% |  |
| 207 | [x] | Secrets of Grindea (STEAM) | 29 | 2026-11-09 | 47 | 72% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 208 | [x] | Capcom Fighting Collection 2 (STEAM) | 29 | 2026-11-09 | 46 | 75% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 209 | [x] | Yakuza: Like a Dragon (STEAM) | 29 | 2026-11-09 | 46 | 66% |  |
| 210 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 62% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 211 | [x] | Subnautica 2 (STEAM) | 29 | 2026-11-10 | 34 | 60% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 212 | [x] | Grand Theft Auto III (STEAM) | 28 | 2026-10-17 | 74 | 77% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 213 | [x] | Owlboy (STEAM) | 28 | 2026-11-02 | 60 | 60% |  |
| 214 | [x] | Heavy Rain (STEAM) | 28 | 2026-11-09 | 49 | 86% |  |
| 215 | [x] | Gambonanza (STEAM) | 28 | 2026-11-09 | 46 | 95% |  |
| 216 | [x] | Binary Domain (STEAM) | 28 | 2026-11-09 | 43 | 60% |  |
| 217 | [x] | Tower and Sword of Succubus (STEAM) | 28 | 2026-11-09 | 43 | 86% |  |
| 218 | [x] | Digimon Survive (STEAM) | 28 | 2026-11-09 | 41 | 96% |  |
| 219 | [x] | Palia (STEAM) | 28 | 2026-11-09 | 40 | 72% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 220 | [x] | Skullgirls 2nd Encore (STEAM) | 27 | 2026-11-10 | 63 | 61% |  |
| 221 | [x] | G.I. Joe Wrath of Cobra (EPIC) | 27 | 2026-11-09 | 48 | 64% |  |
| 222 | [x] | Dead Rising 2 (STEAM) | 27 | 2026-11-09 | 43 | 65% |  |
| 223 | [x] | Gothic II: Gold Classic (STEAM) | 27 | 2026-11-09 | 37 | 68% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 224 | [x] | Ultimate Custom Night (STEAM) | 27 | 2026-11-09 | 37 | 73% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 225 | [x] | CRUEL (STEAM) | 27 | 2026-11-09 | 34 | 75% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 226 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 27 | 2026-11-09 | 33 | 79% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 227 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 26 | 2026-10-19 | 95 | 94% |  |
| 228 | [x] | Dying Light (EPIC) | 26 | 2026-10-17 | 62 | 77% |  |
| 229 | [x] | Monster Hunter Stories (STEAM) | 26 | 2026-10-17 | 61 | 84% |  |
| 230 | [x] | PlateUp! (STEAM) | 26 | 2026-10-16 | 57 | 89% |  |
| 231 | [x] | Soul's Remnant (STEAM) | 26 | 2026-11-11 | 45 | n/a |  |
| 232 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 45 | 64% |  |
| 233 | [x] | Counter-Strike: Condition Zero (STEAM) | 26 | 2026-11-11 | 44 | 41% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 234 | [x] | Ratatan (STEAM) | 26 | 2026-11-09 | 38 | 98% |  |
| 235 | [x] | Bongo Cat (STEAM) | 26 | 2026-11-09 | 33 | 72% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 236 | [x] | Tales of Zestiria (STEAM) | 26 | 2026-11-09 | 32 | 67% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 237 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 26 | 2026-11-09 | 30 | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 238 | [x] | Being a DIK (STEAM) | 25 | 2026-11-09 | 46 | 64% |  |
| 239 | [x] | Battle Brothers (STEAM) | 25 | 2026-11-09 | 43 | 73% |  |
| 240 | [x] | Opus Magnum (STEAM) | 25 | 2026-11-09 | 40 | 87% |  |
| 241 | [x] | Limbus Company (STEAM) | 25 | 2026-11-09 | 39 | 82% |  |
| 242 | [x] | Return to Monkey Island (STEAM) | 25 | 2026-11-09 | 38 | 77% |  |
| 243 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 25 | 2026-11-09 | 36 | 74% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 244 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 25 | 2026-11-09 | 35 | 92% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 245 | [x] | Crab Game (STEAM) | 25 | 2026-11-09 | 33 | 95% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 246 | [x] | Path of Exile 2 (STEAM) | 25 | 2026-11-09 | 32 | 61% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 247 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-09 | 32 | 93% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 248 | [x] | Northgard: Definitive Edition (STEAM) | 25 | 2026-11-09 | 28 | 82% | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 249 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 57 | 92% |  |
| 250 | [x] | Resident Evil Revelations 2 (STEAM) | 24 | 2026-11-09 | 48 | 83% |  |
| 251 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 24 | 2026-11-09 | 46 | 97% |  |
| 252 | [x] | Unturned (STEAM) | 24 | 2026-11-09 | 43 | 71% |  |
| 253 | [x] | Prince of Persia (GOG) | 24 | 2026-11-09 | 42 | 89% |  |
| 254 | [x] | Moonlight Peaks (STEAM) | 24 | 2026-11-09 | 36 | 82% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 255 | [x] | Jade Empire: Special Edition (GOG) | 24 | 2026-11-09 | 31 | 77% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 256 | [x] | Jade Empire: Special Edition (STEAM) | 24 | 2026-11-09 | 27 | 75% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 257 | [x] | The Lantern of the Laughless Saint (STEAM) | 24 | 2026-11-09 | 25 | 64% | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 258 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 23 | 2026-10-20 | 51 | 84% |  |
| 259 | [x] | WEBFISHING (STEAM) | 23 | 2026-10-17 | 49 | 89% |  |
| 260 | [x] | Chained Echoes (GOG) | 23 | 2026-11-08 | 48 | 68% |  |
| 261 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 46 | 88% |  |
| 262 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-11-09 | 45 | 90% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 263 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 23 | 2026-11-09 | 41 | 80% |  |
| 264 | [x] | Football Manager 2024 (EPIC) | 23 | 2026-11-09 | 40 | 70% |  |
| 265 | [x] | Worms W.M.D (STEAM) | 23 | 2026-11-09 | 40 | 90% |  |
| 266 | [x] | Deus Ex™ GOTY Edition (GOG) | 23 | 2026-11-09 | 37 | 88% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 267 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 2026-11-09 | 36 | 76% |  |
| 268 | [x] | Timberborn (STEAM) | 23 | 2026-11-09 | 34 | 84% |  |
| 269 | [x] | Borderlands: The Pre-Sequel (EPIC) | 23 | 2026-11-09 | 33 | 71% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 270 | [x] | Beyond: Two Souls (STEAM) | 23 | 2026-11-09 | 32 | 65% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 271 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 95% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 272 | [x] | CarX Drift Racing Online (STEAM) | 22 | 2026-10-16 | 57 | 81% |  |
| 273 | [x] | MudRunner (EPIC) | 22 | 2026-10-18 | 46 | 79% |  |
| 274 | [x] | Goat Simulator (STEAM) | 22 | 2026-11-09 | 45 | 73% |  |
| 275 | [x] | Crazy Taxi (STEAM) | 22 | 2026-11-10 | 42 | 64% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 276 | [x] | Lucid Blocks (STEAM) | 22 | 2026-11-09 | 42 | 62% |  |
| 277 | [x] | Wizard of Legend (EPIC) | 22 | 2026-11-09 | 40 | 83% |  |
| 278 | [x] | Trailmakers (STEAM) | 22 | 2026-11-09 | 39 | 87% |  |
| 279 | [x] | Cat Mail Co. (STEAM) | 22 | 2026-11-09 | 38 | 88% |  |
| 280 | [x] | Tabletop Simulator (STEAM) | 22 | 2026-11-09 | 36 | 62% |  |
| 281 | [x] | Dishonored 2 (STEAM) | 22 | 2026-11-09 | 32 | 84% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 282 | [x] | SOMA (STEAM) | 22 | 2026-11-09 | 32 | 60% | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 283 | [x] | CarX Street (STEAM) | 22 | 2026-11-09 | 28 | 88% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 284 | [x] | Tearscape (STEAM) | 22 | 2026-11-09 | 27 | 94% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 285 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 60 | 98% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 286 | [x] | Slow Roads (STEAM) | 21 | 2026-10-22 | 46 | 87% |  |
| 287 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 21 | 2026-11-11 | 41 | 50% |  |
| 288 | [x] | Control Ultimate Edition (GOG) | 21 | 2026-11-09 | 39 | 88% |  |
| 289 | [x] | Pinball FX Classic (STEAM) | 21 | 2026-11-09 | 38 | 95% |  |
| 290 | [x] | This War of Mine (STEAM) | 21 | 2026-11-09 | 38 | 61% |  |
| 291 | [x] | Invisible, Inc. (STEAM) | 21 | 2026-11-09 | 37 | 69% |  |
| 292 | [x] | SWORN (STEAM) | 21 | 2026-11-09 | 37 | 95% |  |
| 293 | [x] | My Summer Car (STEAM) | 21 | 2026-11-09 | 36 | 81% |  |
| 294 | [x] | Life is Strange Remastered (STEAM) | 21 | 2026-11-09 | 33 | 85% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 295 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 90% |  |
| 296 | [x] | Sapphire Safari (GOG) | 21 | 2026-11-09 | 28 | 80% | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 297 | [x] | Saints Row IV (STEAM) | 20 | 2026-10-19 | 51 | 83% |  |
| 298 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-11-09 | 38 | 100% |  |
| 299 | [x] | GOD EATER RESURRECTION (STEAM) | 20 | 2026-11-09 | 31 | 67% |  |
| 300 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 20 | 2026-11-09 | 30 | 88% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 301 | [x] | Party Animals (STEAM) | 20 | 2026-11-09 | 29 | 69% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 302 | [x] | Torchlight II (EPIC) | 20 | 2026-11-09 | 28 | 81% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 303 | [x] | Tyr (STEAM) | 20 | 2026-11-09 | 28 | 73% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 304 | [x] | Dead Island (STEAM) | 20 | 2026-11-09 | 25 | 87% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 305 | [x] | Cyberpunk 2077 (EPIC) | 20 | 2026-11-12 | 24 | 62% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 306 | [x] | Titan Quest Anniversary Edition (STEAM) | 19 | 2026-10-16 | 60 | 95% |  |
| 307 | [x] | BlazBlue Centralfiction (STEAM) | 19 | 2026-10-17 | 55 | 83% |  |
| 308 | [x] | ABZÛ (STEAM) | 19 | 2026-10-21 | 47 | 97% |  |
| 309 | [x] | No Rest for the Wicked (STEAM) | 19 | 2026-10-19 | 45 | 80% |  |
| 310 | [x] | One-armed robber (STEAM) | 19 | 2026-11-09 | 35 | 72% |  |
| 311 | [x] | Sorry We're Closed (EPIC) | 19 | 2026-11-09 | 34 | 74% |  |
| 312 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 19 | 2026-11-09 | 33 | 76% |  |
| 313 | [x] | Far Far West (STEAM) | 19 | 2026-11-09 | 33 | 66% |  |
| 314 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 33 | 65% |  |
| 315 | [x] | Stick It to the Stickman (STEAM) | 19 | 2026-11-09 | 33 | 75% |  |
| 316 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 19 | 2026-11-09 | 31 | 77% |  |
| 317 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 19 | 2026-11-09 | 29 | 83% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 318 | [x] | Capcom Fighting Collection (STEAM) | 19 | 2026-11-09 | 27 | 73% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 319 | [x] | Need for Speed™ Unbound (STEAM) | 19 | 2026-11-09 | 27 | 67% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 320 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 19 | 2026-11-09 | 25 | 75% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 321 | [x] | Cave Story+ (EPIC) | 18 | 2026-10-18 | 42 | 81% |  |
| 322 | [x] | Backpack Battles (STEAM) | 18 | 2026-11-09 | 41 | 100% |  |
| 323 | [x] | Brothers - A Tale of Two Sons (EPIC) | 18 | 2026-11-09 | 34 | 64% |  |
| 324 | [x] | Maneater (STEAM) | 18 | 2026-11-09 | 28 | 64% |  |
| 325 | [x] | Arcade Paradise (EPIC) | 18 | 2026-11-09 | 27 | 67% |  |
| 326 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-09 | 23 | 67% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 327 | [x] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 2026-11-09 | 22 | 91% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 328 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 17 | 2026-10-25 | 42 | 76% |  |
| 329 | [x] | Kingdom Come: Deliverance II (STEAM) | 17 | 2026-10-20 | 41 | 86% |  |
| 330 | [x] | Spin Rhythm XD (STEAM) | 17 | 2026-10-18 | 38 | 85% |  |
| 331 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 37 | 23% |  |
| 332 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 35 | 89% |  |
| 333 | [x] | Guacamelee! Gold Edition (STEAM) | 17 | 2026-11-11 | 30 | n/a | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 334 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 17 | 2026-11-09 | 30 | 83% |  |
| 335 | [x] | Shank 2 (STEAM) | 17 | 2026-11-09 | 29 | 83% |  |
| 336 | [x] | DNF Duel (EPIC) | 17 | 2026-11-09 | 28 | 71% |  |
| 337 | [x] | Mortal Shell (EPIC) | 17 | 2026-11-09 | 27 | 72% |  |
| 338 | [x] | Sonic and SEGA All Stars Racing (STEAM) | 17 | 2026-11-09 | 26 | 69% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 339 | [x] | Katanaut (STEAM) | 17 | 2026-11-09 | 23 | 62% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 340 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 17 | 2026-11-09 | 22 | 92% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 341 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 342 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 343 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 51 | 94% |  |
| 344 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 16 | 2026-10-20 | 36 | 77% |  |
| 345 | [x] | Overlord (STEAM) | 16 | 2026-11-08 | 36 | 66% |  |
| 346 | [x] | GRIP: Combat Racing (STEAM) | 16 | 2026-11-09 | 33 | 82% |  |
| 347 | [x] | sobosuba (STEAM) | 16 | 2026-11-09 | 32 | 84% |  |
| 348 | [x] | Faster Than Light (EPIC) | 16 | 2026-11-09 | 31 | 92% |  |
| 349 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 350 | [x] | Tiny Glade (STEAM) | 16 | 2026-11-09 | 30 | 76% |  |
| 351 | [x] | GRANDIA HD Remaster (STEAM) | 16 | 2026-11-09 | 29 | 79% |  |
| 352 | [x] | Need for Speed: Undercover (STEAM) | 16 | 2026-11-11 | 29 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 353 | [x] | Assassin's Creed Odyssey (STEAM) | 16 | 2026-11-09 | 25 | 67% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 354 | [x] | Legend of Grimrock 2 (STEAM) | 16 | 2026-11-09 | 24 | 85% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 355 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 16 | 2026-11-09 | 24 | 88% |  |
| 356 | [x] | Allumeria (STEAM) | 16 | 2026-11-09 | 23 | 69% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 357 | [x] | Darksiders Warmastered Edition (EPIC) | 16 | 2026-11-09 | 21 | 63% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 358 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 359 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 360 | [x] | Sacred Gold (STEAM) | 16 | 2026-11-09 | 20 | 70% | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 361 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 15 | 2026-10-19 | 55 | 85% |  |
| 362 | [x] | Blood: Fresh Supply (STEAM) | 15 | 2026-10-16 | 40 | 78% |  |
| 363 | [x] | Grim Fandango Remastered (STEAM) | 15 | 2026-10-19 | 40 | 71% |  |
| 364 | [x] | Mark of the Ninja (STEAM) | 15 | 2026-10-26 | 32 | 76% |  |
| 365 | [x] | Killing Floor (STEAM) | 15 | 2026-10-19 | 31 | 84% |  |
| 366 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 31 | 96% |  |
| 367 | [x] | Sonic Superstars (STEAM) | 15 | 2026-10-21 | 30 | 67% |  |
| 368 | [x] | Human Fall Flat (STEAM) | 15 | 2026-10-29 | 29 | 62% |  |
| 369 | [x] | Mortal Kombat 11 (STEAM) | 15 | 2026-11-09 | 29 | 69% |  |
| 370 | [x] | Hitman: Absolution (GOG) | 15 | 2026-11-09 | 28 | 77% |  |
| 371 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 15 | 2026-11-09 | 28 | 67% |  |
| 372 | [x] | Titanfall® 2 (STEAM) | 15 | 2026-11-09 | 28 | 65% |  |
| 373 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 15 | 2026-11-11 | 27 | 62% |  |
| 374 | [x] | Car Mechanic Simulator 2018 (STEAM) | 15 | 2026-11-09 | 26 | 95% |  |
| 375 | [x] | WORLD OF FINAL FANTASY (STEAM) | 15 | 2026-11-09 | 26 | 75% |  |
| 376 | [x] | Wildermyth (STEAM) | 15 | 2026-11-09 | 26 | 81% |  |
| 377 | [x] | Batman™: Arkham Origins (GOG) | 15 | 2026-11-09 | 25 | 100% |  |
| 378 | [x] | Gloomwood (STEAM) | 15 | 2026-11-09 | 25 | 67% |  |
| 379 | [x] | Nex Machina (STEAM) | 15 | 2026-11-09 | 24 | 77% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 380 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 85% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 381 | [x] | Chef Knight (STEAM) | 15 | 2026-11-09 | 22 | 64% |  |
| 382 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 15 | 2026-11-09 | 22 | 68% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 383 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 384 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 15 | 2026-11-09 | 21 | 67% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 385 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 386 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 14 | 2026-10-21 | 42 | 82% |  |
| 387 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 92% |  |
| 388 | [x] | No Man's Sky (GOG) | 14 | 2026-10-19 | 30 | 91% |  |
| 389 | [x] | Evoland (STEAM) | 14 | 2026-11-11 | 28 | n/a |  |
| 390 | [x] | Antichamber (STEAM) | 14 | 2026-11-11 | 27 | 73% |  |
| 391 | [x] | Ultrapool (STEAM) | 14 | 2026-11-09 | 27 | 100% |  |
| 392 | [x] | AER Memories of Old (EPIC) | 14 | 2026-11-09 | 25 | 93% |  |
| 393 | [x] | 12 is Better Than 6 (STEAM) | 14 | 2026-11-09 | 23 | 83% |  |
| 394 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 23 | 75% |  |
| 395 | [x] | Sons Of The Forest (STEAM) | 14 | 2026-11-09 | 23 | 72% |  |
| 396 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 397 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-11-09 | 21 | 91% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 398 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 399 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 400 | [x] | Tom Clancy's Splinter Cell: Chaos Theory (STEAM) | 13 | 2026-10-16 | 31 | 82% |  |
| 401 | [x] | Divinity: Original Sin (Classic) (STEAM) | 13 | 2026-10-16 | 30 | 70% |  |
| 402 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 13 | 2026-10-19 | 30 | 95% |  |
| 403 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 29 | 57% |  |
| 404 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 29 | 73% |  |
| 405 | [x] | Dead Space™ 3 (STEAM) | 13 | 2026-10-20 | 28 | 69% |  |
| 406 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 27 | 80% |  |
| 407 | [x] | Rayman Origins (GOG) | 13 | 2026-11-09 | 26 | 82% |  |
| 408 | [x] | Blaster Master Zero (STEAM) | 13 | 2026-11-11 | 26 | 58% |  |
| 409 | [x] | Intravenous 2 (STEAM) | 13 | 2026-11-09 | 26 | 97% |  |
| 410 | [x] | Ready or Not (STEAM) | 13 | 2026-11-09 | 25 | 80% |  |
| 411 | [x] | Ghostwire Tokyo (EPIC) | 13 | 2026-11-09 | 23 | 79% |  |
| 412 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 13 | 2026-11-09 | 23 | 71% |  |
| 413 | [x] | Haydee (STEAM) | 13 | 2026-11-09 | 23 | 78% |  |
| 414 | [x] | Horny Villa (STEAM) | 13 | 2026-11-09 | 22 | 91% |  |
| 415 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 416 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 95% |  |
| 417 | [x] | Alabaster Dawn Demo (STEAM) | 13 | 2026-11-09 | 20 | 75% |  |
| 418 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 419 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 13 | 2026-10-23 | 20 | 61% |  |
| 420 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 80% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 421 | [x] | CULTIC (STEAM) | 12 | 2026-11-09 | 28 | 58% |  |
| 422 | [x] | Haiku, the Robot (STEAM) | 12 | 2026-10-21 | 28 | n/a |  |
| 423 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 12 | 2026-10-18 | 28 | 91% |  |
| 424 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 12 | 2026-11-01 | 27 | n/a |  |
| 425 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 12 | 2026-11-09 | 26 | 89% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 426 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 26 | 65% |  |
| 427 | [x] | Alan Wake's American Nightmare (EPIC) | 12 | 2026-11-09 | 25 | 63% |  |
| 428 | [x] | Aperture Desk Job (STEAM) | 12 | 2026-11-03 | 25 | n/a |  |
| 429 | [x] | Lust Goddess (STEAM) | 12 | 2026-11-09 | 25 | 88% |  |
| 430 | [x] | Injustice™ 2 (STEAM) | 12 | 2026-10-17 | 24 | 62% |  |
| 431 | [x] | Lost Castle 2 (STEAM) | 12 | 2026-11-09 | 24 | 94% |  |
| 432 | [x] | HITMAN World of Assassination (STEAM) | 12 | 2026-11-09 | 23 | 87% |  |
| 433 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 23 | 77% |  |
| 434 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-10 | 22 | 67% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 435 | [x] | DiRT 4 (STEAM) | 12 | 2026-11-09 | 22 | 91% |  |
| 436 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 12 | 2026-11-09 | 21 | 73% |  |
| 437 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 438 | [x] | Shift At Midnight (STEAM) | 12 | 2026-11-09 | 21 | 80% |  |
| 439 | [x] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 2026-11-12 | 21 | 90% |  |
| 440 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 441 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 442 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 2026-11-10 | 20 | 60% |  |
| 443 | [x] | Turbo Overkill (STEAM) | 12 | 2026-11-09 | 20 | 95% |  |
| 444 | [x] | Middle-earth™: Shadow of War™ (STEAM) | 11 | 2026-10-16 | 35 | 82% |  |
| 445 | [x] | Breath of Fire IV (GOG) | 11 | 2026-10-26 | 25 | 58% |  |
| 446 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 2026-10-27 | 25 | 81% |  |
| 447 | [x] | MX Bikes (STEAM) | 11 | 2026-11-09 | 24 | 93% |  |
| 448 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 23 | 76% |  |
| 449 | [x] | Castle in the Clouds (STEAM) | 11 | 2026-11-09 | 22 | 78% |  |
| 450 | [x] | Cruelty Squad (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 451 | [x] | UNDEFEATED (STEAM) | 11 | 2026-11-09 | 22 | 71% |  |
| 452 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 21 | 67% |  |
| 453 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 454 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 455 | [x] | TowerFall Ascension (STEAM) | 10 | 2026-10-16 | 31 | 70% |  |
| 456 | [x] | Distance (STEAM) | 10 | 2026-10-19 | 29 | 74% |  |
| 457 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 26 | n/a |  |
| 458 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 10 | 2026-10-23 | 24 | 82% |  |
| 459 | [x] | Coromon (GOG) | 10 | 2026-10-19 | 22 | 65% |  |
| 460 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 22 | 85% |  |
| 461 | [x] | Sid Meier's Civilization VI (EPIC) | 10 | 2026-10-19 | 21 | 82% |  |
| 462 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 10 | 2026-11-09 | 21 | 89% |  |
| 463 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 464 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 465 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 466 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 20 | 79% |  |
| 467 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 468 | [x] | The WereCleaner (STEAM) | 9 | 2026-10-22 | 30 | 95% |  |
| 469 | [x] | Possessor(s) (STEAM) | 9 | 2026-10-24 | 27 | 93% |  |
| 470 | [x] | SCP – Containment Breach (STEAM) | 9 | 2026-10-27 | 23 | 92% |  |
| 471 | [x] | SteamWorld Heist (GOG) | 9 | 2026-10-25 | 21 | n/a |  |
| 472 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 9 | 2026-10-21 | 21 | 92% |  |
| 473 | [x] | Football Manager 2024 (STEAM) | 9 | 2026-10-16 | 20 | n/a |  |
| 474 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 29% |  |
| 475 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 9 | 2026-10-20 | 20 | n/a |  |
| 476 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 8 | 2026-10-20 | 25 | 79% |  |
| 477 | [x] | Gloomhaven (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 478 | [x] | Mina the Hollower (GOG) | 8 | 2026-10-28 | 20 | 71% |  |
| 479 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 20 | 51% |  |
| 480 | [x] | Mafia II: Definitive Edition (STEAM) | 7 | 2026-10-16 | 20 | n/a |  |
| 481 | [x] | What Remains of Edith Finch (STEAM) | 6 | 2026-10-19 | 26 | 70% |  |
| 482 | [x] | Alex Kidd in Miracle World DX (STEAM) | 2 | 2026-10-16 | 34 | 93% |  |
