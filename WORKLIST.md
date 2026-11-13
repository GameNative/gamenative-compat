# GameNative compatibility worklist

Generated: `2026-11-13T04:15:12.577Z` · Ratings since: `2026-08-15T04:15:12.577Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 123 |
| Probably does not work | 167 |
| Fix shipped, waiting for ratings | 15 |
| First launch fails | 325 |
| Mixed | 510 |
| Works | 1023 |
| Total | 2163 |

## Does not work (123)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 79 | 93 | 85% (since fix) | Does not open (93%) | 53% | today | 40% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 2 | [ ] | Rocket League® (EPIC) | 47 | 58 | 81% (14d) | Does not open (79%) | 58% | today | 35% (drop) | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 3 | [ ] | Metro 2033 Redux (STEAM) | 28 | 36 | 78% (14d) | Does not open (71%) | 40% | today | 39% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 4 | [x] 2026-10-18 | Project Zomboid (STEAM) | 51 | 57 | 89% (since fix) | Does not open (65%) | 53% | 1d ago | 45% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 5 | [ ] | Borderlands 2 (EPIC) | 22 | 27 | 81% (14d) | Does not open (82%) | 59% | 1d ago | 50% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 6 | [ ] | Hogwarts Legacy (STEAM) | 22 | 27 | 81% (14d) | Does not open (65%) | 46% | 1d ago | 18% (drop) | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 7 | [ ] | Saints Row 2 (GOG) | 21 | 27 | 78% (14d) | Does not open (91%) | 41% | today | 32% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 8 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 20 | 25 | 80% (14d) | Does not open (74%) | 57% | today | 50% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 9 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 19 | 22 | 86% (14d) | Does not open (95%) | 58% | today | 16% (drop) | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 10 | [ ] | Saints Row 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | 36% | today | 39% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 11 | [ ] | Metro: Last Light Redux (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 18% | 1d ago | 14% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 12 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 17 | 21 | 81% (14d) | Does not open (75%) | 56% | today | 39% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 13 | [ ] | Bloons TD 6 (EPIC) | 17 | 22 | 77% (14d) | Does not open (80%) | 47% | today | 21% (drop) | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 14 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (75%) | 0% | 4d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 15 | [ ] | Call of Duty: Black Ops II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (76%) | 31% | 1d ago | 39% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 16 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 18 | 20 | 90% (last 20) | No graphics (46%) | 24% | 5d ago | n/a | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 17 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (94%) | 24% | today | 17% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 18 | [ ] | Yume Nikki (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | 25% | 6d ago | 44% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 19 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (78%) | 8% | 1d ago | n/a | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 20 | [ ] | skate. (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | 9% | 2d ago | 15% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 21 | [ ] | Path of Exile (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | 30% | today | 9% (drop) | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 22 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 17 | 20 | 85% (last 20) | Does not open (87%) | 46% | 1d ago | 32% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 23 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (70%) | 7% | 7d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 24 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (65%) | 5% | 19d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 25 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 14% | 1d ago | 10% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 26 | [ ] | The Witcher: Enhanced Edition (GOG) | 19 | 20 | 95% (last 20) | Does not open (73%) | 13% | 4d ago | 0% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 27 | [ ] | Mafia II (Classic) (STEAM) | 20 | 20 | 100% (last 20) | Does not open (74%) | 7% | 5d ago | 10% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 28 | [ ] | CPM 2 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 6% | today | n/a | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 29 | [ ] | Fall Guys (EPIC) | 19 | 20 | 95% (last 20) | Does not open (76%) | 15% | 3d ago | 9% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 30 | [ ] | Detroit: Become Human (STEAM) | 19 | 20 | 95% (last 20) | Does not open (74%) | 44% | 11d ago | n/a | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 31 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | No graphics (57%) | 0% | 16d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 32 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | 0% | 2d ago | n/a | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 33 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (75%) | 11% | 1d ago | n/a | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 34 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (92%) | 7% | 14d ago | n/a | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 35 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (67%) | 14% | 12d ago | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 36 | [ ] | Borderlands GOTY (STEAM) | 17 | 20 | 85% (last 20) | Does not open (94%) | 29% | today | 40% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 37 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (88%) | 18% | 6d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 38 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (79%) | 15% | 4d ago | 18% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 39 | [ ] | Breath of Fire IV (STEAM) | 20 | 20 | 100% (last 20) | Does not open (60%) | 19% | today | n/a | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 40 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (88%) | 22% | 4d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 41 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 57% | 3d ago | 28% (drop) | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 42 | [ ] | Vampire Survivors (EPIC) | 14 | 20 | 70% (last 20) | Does not open (56%) | 58% | 6d ago | 41% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 43 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (67%) | 16% | 5d ago | n/a | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 44 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 57% | 6d ago | n/a | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 45 | [ ] | MECCHA CHAMELEON (STEAM) | 15 | 20 | 75% (last 20) | Does not open (64%) | 51% | 5d ago | 28% (drop) | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 46 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (73%) | 22% | 1d ago | n/a | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 47 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | 18% | 5d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 48 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (83%) | 43% | 27d ago | n/a | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 49 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (89%) | 39% | today | 36% | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 50 | [ ] | Plague Inc: Evolved (STEAM) | 14 | 20 | 70% (last 20) | Does not open (68%) | 58% | 3d ago | 64% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 51 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 6% | today | n/a | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 52 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | 0% | 27d ago | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 53 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (56%) | 25% | 8d ago | n/a | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 54 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 17 | 20 | 85% (last 20) | Does not open (44%) | 46% | 15d ago | 40% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 55 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | 0% | 5d ago | n/a | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 56 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 23% | 4d ago | 45% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 57 | [ ] | Trackmania (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | 26% | 1d ago | 29% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 58 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | 42% | 34d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 59 | [ ] | Black Mesa (STEAM) | 15 | 20 | 75% (last 20) | Does not open (80%) | 22% | 20d ago | 36% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 60 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (92%) | 29% | 1d ago | n/a | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 61 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 38% | 1d ago | n/a | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 62 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (47%) | 39% | 8d ago | 36% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 63 | [ ] | Watch_Dogs (STEAM) | 14 | 20 | 70% (last 20) | Does not open (90%) | 30% | 6d ago | n/a | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 64 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (92%) | 57% | 14d ago | n/a | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 65 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | 0% | 11d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 66 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (71%) | 35% | 6d ago | n/a | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 67 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | 18% | 1d ago | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 68 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 18% | 25d ago | n/a | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 69 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 25% | 22d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 70 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | 45% | 2d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 71 | [ ] | XCOM: Enemy Unknown (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | 11% | 8d ago | n/a | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 72 | [ ] | Half-Life: Blue Shift (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 33% | 4d ago | n/a | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 73 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | 9% | 11d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 74 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (60%) | 36% | 13d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 75 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | No graphics (59%) | 11% | 6d ago | n/a | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 76 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 15% | 11d ago | n/a | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 77 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 4% | 1d ago | 2% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 78 | [ ] | Changed (STEAM) | 15 | 20 | 75% (last 20) | Does not open (71%) | 57% | today | 33% (drop) | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 79 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 20 | 20 | 100% (last 20) | No graphics (59%) | 38% | 36d ago | 59% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 80 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 17% | 13d ago | n/a | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 81 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 46% | 1d ago | n/a | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 82 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | 38% | today | n/a | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 83 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 0% | 26d ago | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 84 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (67%) | 0% | 19d ago | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 85 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 6% | 8d ago | 8% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 86 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 50% | 1d ago | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 87 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (77%) | 26% | today | n/a | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 88 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 30% | 10d ago | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 89 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (81%) | 31% | 5d ago | n/a | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 90 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (91%) | 5% | 19d ago | 10% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 91 | [ ] | Umamusume: Pretty Derby (STEAM) | 18 | 20 | 90% (last 20) | Does not open (86%) | 50% | 9d ago | n/a | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 92 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (68%) | 33% | 29d ago | n/a | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 93 | [ ] | OneShot (STEAM) | 16 | 20 | 80% (last 20) | Does not open (96%) | 10% | 28d ago | n/a | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 94 | [ ] | Lost Planet: Extreme Condition (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | 44% | 3d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 95 | [ ] | Hotline Miami (GOG) | 15 | 20 | 75% (last 20) | Does not open (90%) | 59% | 3d ago | n/a | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 96 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | 21% | 3d ago | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 97 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 33% | 11d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 98 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 45% | 10d ago | n/a | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 99 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (97%) | 31% | 11d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 100 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | 20% | 2d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 101 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (86%) | 42% | 13d ago | n/a | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 102 | [ ] | Call of Duty® (STEAM) | 14 | 20 | 70% (last 20) | Does not open (67%) | 7% | 1d ago | n/a | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 103 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (95%) | 29% | 24d ago | 29% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 104 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | 20% | 2d ago | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 105 | [ ] | Aliens vs. Predator (STEAM) | 16 | 20 | 80% (last 20) | No graphics (53%) | 17% | 1d ago | 17% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 106 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (67%) | 42% | 2d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 107 | [ ] | Kenshi (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | 3% | 12d ago | n/a | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 108 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | 41% | 13d ago | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 109 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 14 | 20 | 70% (last 20) | Does not open (56%) | 53% | 3d ago | 67% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 110 | [ ] | Undisputed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 59% | 5d ago | n/a | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 111 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 43% | 27d ago | n/a | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 112 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | 18% | 2d ago | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 113 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | 53% | 3d ago | 33% (drop) | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 114 | [ ] | The Lantern of the Laughless Saint (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 57% | 10d ago | n/a | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 115 | [ ] | Zuma Deluxe (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 38% | today | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 116 | [ ] | Beyond Good & Evil™ (GOG) | 17 | 20 | 85% (last 20) | Does not open (100%) | 18% | 20d ago | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 117 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (67%) | 54% | 4d ago | n/a | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 118 | [ ] | skate.™ (EPIC) | 18 | 20 | 90% (last 20) | Does not open (87%) | 0% | 18d ago | n/a | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 119 | [ ] | Goose Goose Duck (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 53% | 3d ago | n/a | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 120 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 38% | 13d ago | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 121 | [ ] | Maneater (EPIC) | 16 | 20 | 80% (last 20) | Does not open (75%) | 47% | 5d ago | n/a | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 122 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 38% | 8d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 123 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | 55% | 17d ago | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |

## Probably does not work (167)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | To The Moon (GOG) | 44 | 46 | 96% (14d) | Does not open (86%) | n/a | 10d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 2 | [ ] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 37 | 65 | 57% (14d) | Does not open (64%) | 59% | today | 64% |  |
| 3 | [ ] | theHunter Classic (STEAM) | 23 | 23 | 100% (14d) | No graphics (92%) | n/a | 9d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 4 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 14 | 24 | 58% (14d) | Does not open (72%) | 55% | 1d ago | 92% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 5 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 13 | 20 | 65% (14d) | Does not open (62%) | 58% | today | 54% |  |
| 6 | [ ] | Garry's Mod (STEAM) | 7 | 11 | 64% (since fix) | Does not open (79%) | 54% | today | 43% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 7 | [ ] | Driver: Parallel Lines (STEAM) | 19 | 20 | 95% (last 20) | Does not open (65%) | n/a | 4d ago | n/a | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 8 | [ ] | VRChat (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 37% | 1d ago | 27% |  |
| 9 | [ ] | Euro Truck Simulator 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (66%) | 56% | 1d ago | 51% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 10 | [ ] | Gorilla Tag (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 18% | 3d ago | 7% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 11 | [ ] | Door Kickers 2 (STEAM) | 20 | 20 | 100% (last 20) | No graphics (86%) | n/a | 30d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 12 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 33d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 13 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (35%) | n/a | 10d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 14 | [ ] | Alan Wake (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 29% | 3d ago | 71% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 15 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 17d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 16 | [ ] | Sonic Adventure™ 2  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (76%) | 48% | 1d ago | 41% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 17 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 9 | 13 | 69% (since fix) | Does not open (78%) | 20% | 1d ago | 32% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 18 | [ ] | Metro 2033 Redux (EPIC) | 10 | 20 | 50% (last 20) | Does not open (62%) | 21% | 4d ago | 35% |  |
| 19 | [ ] | GRID (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 43% | 4d ago | 45% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 20 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 14d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 21 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 13 | 20 | 65% (last 20) | Does not open (85%) | 50% | 2d ago | 65% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 22 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (85%) | 43% | 3d ago | n/a |  |
| 23 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (93%) | n/a | 1d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 24 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (100%) | n/a | 2d ago | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 25 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 8d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 26 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 30% | 5d ago | n/a | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 27 | [ ] | CODE VEIN (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 50% | 2d ago | n/a | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 28 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | n/a | today | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 29 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (85%) | n/a | 11d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 30 | [ ] | Hollow Knight: Silksong (GOG) | 12 | 20 | 60% (last 20) | Does not open (72%) | 56% | today | 60% |  |
| 31 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 10d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 32 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | n/a | 32d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 33 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | n/a | 15d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 34 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | n/a | 8d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 35 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | n/a | 2d ago | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 36 | [ ] | Dead Space 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 32% | 3d ago | 42% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 37 | [ ] | Grim Dawn (GOG) | 12 | 20 | 60% (last 20) | Does not open (65%) | n/a | 1d ago | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 38 | [ ] | METAL SLUG 3 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 41% | today | n/a | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 39 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 30d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 40 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 31d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 41 | [ ] | Alpha Protocol (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | n/a | 18d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 42 | [ ] | Breathedge (STEAM) | 11 | 20 | 55% (last 20) | Does not open (56%) | 50% | 2d ago | 70% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 43 | [ ] | DOOM Eternal (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | n/a | 21d ago | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 44 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | n/a | 14d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 45 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 16d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 46 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 32% | 3d ago | n/a | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 47 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | 33d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 48 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 8d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 49 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | n/a | 32d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 50 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | n/a | 30d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 51 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (58%) | n/a | 32d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 52 | [ ] | Borderlands 2 RU (STEAM) | 19 | 20 | 95% (last 20) | Does not open (61%) | n/a | 30d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 53 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 30d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 54 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (81%) | n/a | 5d ago | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 55 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 16d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 56 | [ ] | HELLDIVERS™ (STEAM) | 13 | 20 | 65% (last 20) | Does not open (60%) | 42% | 2d ago | n/a | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 57 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 4d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 58 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (57%) | n/a | 18d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 59 | [ ] | Euro Truck Simulator (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | 1d ago | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 60 | [ ] | Peggle Nights (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 16d ago | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 61 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 41d ago | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 62 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 12d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 63 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | 35d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 64 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | n/a | 21d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 65 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (63%) | n/a | 39d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 66 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | n/a | 1d ago | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 67 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | 0% | 8d ago | n/a |  |
| 68 | [ ] | Metro 2033 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (61%) | 29% | 9d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 69 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (47%) | n/a | 12d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 70 | [ ] | The Survivalists (STEAM) | 18 | 20 | 90% (last 20) | Does not open (97%) | n/a | today | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 71 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | n/a | 30d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 72 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 8d ago | n/a |  |
| 73 | [ ] | A Plague Tale: Innocence (EPIC) | 11 | 20 | 55% (last 20) | Does not open (70%) | 56% | 19d ago | n/a |  |
| 74 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 20 | 20 | 100% (last 20) | Does not open (53%) | n/a | 28d ago | n/a | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 75 | [ ] | Resident Evil Requiem (STEAM) | 20 | 20 | 100% (last 20) | Does not open (69%) | n/a | 32d ago | n/a | [#210](https://github.com/GameNative/gamenative-compat/issues/210) |
| 76 | [ ] | Marvel's Spider-Man 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | n/a | 32d ago | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 77 | [ ] | They Are Billions (STEAM) | 19 | 20 | 95% (last 20) | Does not open (75%) | n/a | 9d ago | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 78 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 55d ago | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 79 | [ ] | Bionic Commando Rearmed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | n/a | 23d ago | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 80 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | n/a | 30d ago | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 81 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 18 | 20 | 90% (last 20) | Does not open (89%) | n/a | today | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 82 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 6d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 83 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 3d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 84 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 1d ago | n/a |  |
| 85 | [ ] | Alien Breed: Impact (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 18d ago | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 86 | [ ] | No More Room in Hell (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 26d ago | n/a | [#365](https://github.com/GameNative/gamenative-compat/issues/365) |
| 87 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 18 | 20 | 90% (last 20) | Does not open (75%) | n/a | 17d ago | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 88 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 4d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 89 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (83%) | n/a | 6d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 90 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 8d ago | n/a |  |
| 91 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 8d ago | n/a |  |
| 92 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 46% | 1d ago | n/a | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 93 | [ ] | Apex Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | n/a | 14d ago | n/a | [#261](https://github.com/GameNative/gamenative-compat/issues/261) |
| 94 | [ ] | GeoGuessr Steam Edition (STEAM) | 19 | 20 | 95% (last 20) | Does not open (73%) | n/a | 25d ago | n/a | [#154](https://github.com/GameNative/gamenative-compat/issues/154) |
| 95 | [ ] | Zenless Zone Zero (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | n/a | 16d ago | n/a | [#369](https://github.com/GameNative/gamenative-compat/issues/369) |
| 96 | [ ] | Deadly Premonition: The Director's Cut (STEAM) | 18 | 20 | 90% (last 20) | Does not open (53%) | n/a | 6d ago | n/a | [#520](https://github.com/GameNative/gamenative-compat/issues/520) |
| 97 | [ ] | Lay of the Land (STEAM) | 18 | 20 | 90% (last 20) | No graphics (61%) | n/a | 12d ago | n/a | [#477](https://github.com/GameNative/gamenative-compat/issues/477) |
| 98 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | n/a | 1d ago | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 99 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 14d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 100 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 11d ago | n/a |  |
| 101 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (44%) | n/a | 11d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 102 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 1d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 103 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 15d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 104 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 57% | 1d ago | n/a |  |
| 105 | [ ] | King's Bounty: The Legend (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | n/a | 7d ago | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 106 | [ ] | Marvel's Midnight Suns (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | n/a | 30d ago | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 107 | [ ] | PICO PARK:Classic Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 35d ago | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 108 | [ ] | ENDLESS Space™ 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | n/a | 28d ago | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 109 | [ ] | Beholder (EPIC) | 15 | 20 | 75% (last 20) | Does not open (69%) | n/a | 18d ago | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 110 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | Does not open (42%) | n/a | 3d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 111 | [ ] | Mafia II (Classic) (GOG) | 13 | 20 | 65% (last 20) | Does not open (95%) | 45% | 20d ago | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 112 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | 59% | 13d ago | 25% (drop) |  |
| 113 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | n/a | 22d ago | n/a |  |
| 114 | [ ] | Utopia Must Fall (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | n/a | today | n/a | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 115 | [ ] | Clive Barker's Undying (GOG) | 17 | 20 | 85% (last 20) | Does not open (75%) | n/a | 17d ago | n/a | [#388](https://github.com/GameNative/gamenative-compat/issues/388) |
| 116 | [ ] | Fallout Classic (GOG) | 15 | 20 | 75% (last 20) | Does not open (78%) | n/a | today | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 117 | [ ] | Re-Volt (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (71%) | n/a | 19d ago | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 118 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | today | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 119 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (57%) | n/a | 25d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 120 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (83%) | 35% | 11d ago | n/a | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 121 | [ ] | Drop Duchy (EPIC) | 12 | 20 | 60% (last 20) | Does not open (100%) | n/a | 12d ago | n/a |  |
| 122 | [ ] | Mini Metro (STEAM) | 11 | 20 | 55% (last 20) | Does not open (44%) | 44% | 1d ago | n/a |  |
| 123 | [ ] | F.E.A.R. 2: Project Origin + Reborn (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 13d ago | n/a | [#478](https://github.com/GameNative/gamenative-compat/issues/478) |
| 124 | [ ] | Lunarium (STEAM) | 16 | 20 | 80% (last 20) | Does not open (54%) | n/a | today | n/a |  |
| 125 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | n/a | 5d ago | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 126 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | n/a | 3d ago | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 127 | [ ] | Sandustry (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 3d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 128 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 2d ago | n/a |  |
| 129 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | n/a | 24d ago | n/a |  |
| 130 | [ ] | Mafia: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 42% | 1d ago | 37% |  |
| 131 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 56% | 7d ago | 67% |  |
| 132 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 12 | 20 | 60% (last 20) | Does not open (92%) | 58% | 4d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 133 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | No graphics (57%) | 20% | 6d ago | n/a | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 134 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (50%) | n/a | 4d ago | n/a |  |
| 135 | [ ] | Dungeon Keeper™ 2 (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 19d ago | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 136 | [ ] | Blood Omen: Legacy of Kain (GOG) | 13 | 20 | 65% (last 20) | Does not open (62%) | 44% | 2d ago | n/a |  |
| 137 | [ ] | A Plague Tale: Innocence (GOG) | 11 | 20 | 55% (last 20) | Does not open (91%) | 50% | 20d ago | n/a |  |
| 138 | [ ] | Beat Cop (STEAM) | 13 | 20 | 65% (last 20) | Does not open (72%) | n/a | today | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 139 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 13 | 20 | 65% (last 20) | No graphics (56%) | n/a | 31d ago | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 140 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | n/a | 35d ago | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 141 | [ ] | Minit (EPIC) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 5d ago | n/a |  |
| 142 | [ ] | Songs of Conquest (EPIC) | 12 | 20 | 60% (last 20) | Does not open (75%) | n/a | 11d ago | n/a |  |
| 143 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 8d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 144 | [ ] | Styx: Master of Shadows (EPIC) | 11 | 20 | 55% (last 20) | Does not open (65%) | 35% | 4d ago | n/a |  |
| 145 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (70%) | 54% | 1d ago | n/a |  |
| 146 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 43% | 1d ago | n/a | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 147 | [ ] | This War of Mine (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 53% | 13d ago | 31% (drop) |  |
| 148 | [ ] | Knights of Pen and Paper 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (42%) | n/a | 4d ago | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 149 | [ ] | Fogpiercer (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 26d ago | n/a | [#303](https://github.com/GameNative/gamenative-compat/issues/303) |
| 150 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | n/a | 3d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 151 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (78%) | n/a | 7d ago | n/a |  |
| 152 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 14d ago | n/a |  |
| 153 | [ ] | LET IT DIE (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 55% | 7d ago | n/a |  |
| 154 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 54% | 5d ago | n/a |  |
| 155 | [ ] | No More Heroes (STEAM) | 10 | 20 | 50% (last 20) | No graphics (71%) | 53% | 1d ago | n/a |  |
| 156 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 43% | 8d ago | n/a |  |
| 157 | [ ] | Turnip Boy Robs a Bank (EPIC) | 12 | 20 | 60% (last 20) | Does not open (60%) | 36% | 18d ago | n/a | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 158 | [ ] | Ys: Memories of Celceta (STEAM) | 12 | 20 | 60% (last 20) | No graphics (45%) | 33% | 13d ago | n/a |  |
| 159 | [ ] | Dex (GOG) | 12 | 20 | 60% (last 20) | Does not open (83%) | n/a | 2d ago | n/a |  |
| 160 | [ ] | Secret of Mana (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (55%) | n/a | 26d ago | n/a |  |
| 161 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | n/a | 7d ago | n/a |  |
| 162 | [ ] | Crying Suns (EPIC) | 11 | 20 | 55% (last 20) | No graphics (57%) | n/a | 3d ago | n/a |  |
| 163 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | n/a | 78d ago | n/a |  |
| 164 | [ ] | Railway Chai Wala (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | n/a | 6d ago | n/a |  |
| 165 | [ ] | Asterigos: Curse of the Stars (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (50%) | n/a | 13d ago | n/a |  |
| 166 | [ ] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 15% | 8d ago | n/a |  |
| 167 | [ ] | Delver (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 45% | 5d ago | n/a |  |

## Fix shipped, waiting for ratings (15)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | Plants vs. Zombies: Game of the Year (STEAM) | 2026-11-04 | 7 | 5 | 1d ago | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 2 | Transistor (STEAM) | 2026-11-10 | 1 | 1 | 1d ago | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 3 | Max Payne 3 (STEAM) | 2026-11-04 | 1 | 1 | 6d ago | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 4 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 6 | 6 | 6d ago | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 5 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 3 | 3 | 2d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 6 | L.A. Noire (STEAM) | 2026-11-04 | 0 | 0 | 10d ago | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 7 | Peggle Deluxe (STEAM) | 2026-10-29 | 1 | 1 | today | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 8 | Necesse (STEAM) | 2026-10-29 | 5 | 0 | 4d ago | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 9 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 1 | 1 | 2d ago | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 10 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 1 | 1 | 9d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 11 | Need for Speed™ (STEAM) | 2026-11-04 | 0 | 0 | 22d ago | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 12 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 0 | 0 | 10d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 13 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 0 | 0 | 15d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 14 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 0 | 0 | 9d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 15 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 8d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |

## Works, but the first launch usually fails (325)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 143 | 163 | 88% (14d) | Does not open (83%) | 60% | today | 8% (drop) | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 76 | 94 | 81% (14d) | Does not open (63%) | 91% | today | 94% |  |
| 3 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 59 | 82 | 72% (14d) | Does not open (54%) | 83% | today | 84% |  |
| 4 | [ ] | Grand Theft Auto V Legacy (STEAM) | 38 | 48 | 79% (since fix) | Does not open (88%) | 76% | today | 70% |  |
| 5 | [ ] | Deskrawl: Idle ARPG (STEAM) | 55 | 66 | 83% (14d) | Does not open (60%) | 85% | 2d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 6 | [ ] | Valheim (STEAM) | 29 | 45 | 64% (since fix) | No graphics (53%) | 88% | today | 83% |  |
| 7 | [ ] | Road Rash™: 30th Anniversary Edition (STEAM) | 44 | 60 | 73% (14d) | Does not open (74%) | 60% | today | 64% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 8 | [ ] | Cyberpunk 2077 (STEAM) | 42 | 71 | 59% (14d) | Does not open (68%) | 73% | today | 65% |  |
| 9 | [ ] | MONSTER HUNTER RISE (STEAM) | 41 | 69 | 59% (14d) | Does not open (83%) | 62% | today | 61% |  |
| 10 | [ ] | No Man's Sky (STEAM) | 26 | 43 | 60% (since fix) | Controller issues (61%) | 80% | today | 76% |  |
| 11 | [ ] | Half-Life (STEAM) | 39 | 62 | 63% (14d) | Does not open (57%) | 71% | today | 63% |  |
| 12 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 39 | 52 | 75% (14d) | Does not open (75%) | 77% | today | 73% |  |
| 13 | [ ] | Buckshot Roulette (STEAM) | 32 | 61 | 52% (14d) | Does not open (62%) | 77% | today | 46% (drop) |  |
| 14 | [ ] | DREDGE (EPIC) | 32 | 37 | 86% (14d) | Does not open (76%) | 72% | today | 54% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 15 | [ ] | Palworld (STEAM) | 31 | 49 | 63% (14d) | Does not open (73%) | 87% | today | 85% |  |
| 16 | [ ] | Super Meat Boy (STEAM) | 28 | 55 | 51% (14d) | Does not open (55%) | 71% | today | 46% (drop) |  |
| 17 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 26 | 38 | 68% (14d) | Does not open (56%) | 74% | today | 62% |  |
| 18 | [ ] | Counter-Strike 2 (STEAM) | 39 | 53 | 74% (since fix) | Does not open (67%) | 61% | 1d ago | 65% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 19 | [ ] | Red Dead Redemption 2 (STEAM) | 15 | 15 | 100% (since fix) | Does not open (98%) | 81% | today | 78% |  |
| 20 | [ ] | ELDEN RING (STEAM) | 23 | 40 | 58% (14d) | Does not open (85%) | 74% | today | 70% |  |
| 21 | [ ] | Quake (STEAM) | 20 | 30 | 67% (14d) | Does not open (65%) | 84% | today | 58% (drop) |  |
| 22 | [ ] | Devil May Cry 5 (STEAM) | 18 | 29 | 62% (14d) | Does not open (83%) | 72% | today | 78% |  |
| 23 | [ ] | Deadlock (STEAM) | 18 | 21 | 86% (14d) | Does not open (54%) | 87% | 1d ago | 81% |  |
| 24 | [ ] | BeamNG.drive (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 81% | today | 55% (drop) | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 25 | [ ] | Batman™: Arkham Origins (STEAM) | 17 | 25 | 68% (14d) | Does not open (84%) | 75% | 1d ago | 63% |  |
| 26 | [ ] | DRAGON BALL FighterZ (STEAM) | 25 | 41 | 61% (since fix) | Does not open (89%) | 78% | 1d ago | 91% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 27 | [ ] | CHRONO TRIGGER (STEAM) | 16 | 27 | 59% (14d) | Does not open (60%) | 83% | 1d ago | 95% |  |
| 28 | [ ] | BioShock Remastered (EPIC) | 16 | 21 | 76% (14d) | Does not open (65%) | 72% | today | 55% |  |
| 29 | [ ] | Mortal Kombat X (STEAM) | 16 | 25 | 64% (14d) | Does not open (72%) | 89% | today | 91% |  |
| 30 | [ ] | Mass Effect™ Legendary Edition (STEAM) | 9 | 16 | 56% (since fix) | Does not open (87%) | 79% | today | 85% |  |
| 31 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (88%) | 94% | today | 93% |  |
| 32 | [ ] | METAL GEAR SOLID 4: Guns of the Patriots - Master Collection Version (STEAM) | 14 | 28 | 50% (14d) | Does not open (80%) | 90% | 1d ago | 92% |  |
| 33 | [ ] | Clair Obscur: Expedition 33 (STEAM) | 13 | 24 | 54% (14d) | Graphics glitches (42%) | 85% | 1d ago | 76% |  |
| 34 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 72% | 4d ago | 64% |  |
| 35 | [ ] | Fallout: New Vegas PCR (STEAM) | 17 | 20 | 85% (last 20) | Does not open (93%) | 60% | today | 58% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 36 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 18 | 33 | 55% (since fix) | Does not open (75%) | 64% | 1d ago | 50% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 37 | [ ] | Grand Theft Auto V (EPIC) | 19 | 20 | 95% (last 20) | Does not open (89%) | 74% | today | 65% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 38 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 65% | today | 43% (drop) |  |
| 39 | [ ] | The Forest (STEAM) | 11 | 22 | 50% (14d) | Does not open (77%) | 84% | today | 86% |  |
| 40 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (79%) | 98% | today | 94% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 41 | [ ] | Fallout: New Vegas (EPIC) | 15 | 20 | 75% (last 20) | Does not open (59%) | 85% | 2d ago | 71% |  |
| 42 | [ ] | Cyberpunk 2077 (GOG) | 14 | 20 | 70% (last 20) | Does not open (71%) | 70% | today | 53% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 43 | [ ] | Dead Island 2 (EPIC) | 15 | 20 | 75% (last 20) | Does not open (82%) | 81% | 2d ago | 60% |  |
| 44 | [ ] | DOOM 3: BFG Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (72%) | 70% | today | 61% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 45 | [ ] | eFootball™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 62% | today | 47% |  |
| 46 | [ ] | Marvel’s Spider-Man Remastered (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 66% | 1d ago | 80% |  |
| 47 | [ ] | Hogwarts Legacy (EPIC) | 15 | 20 | 75% (last 20) | Does not open (76%) | 66% | 1d ago | 47% |  |
| 48 | [ ] | Castlevania Advance Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (95%) | 89% | 4d ago | 82% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 49 | [ ] | Order of the Sinking Star (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | 66% | 1d ago | 77% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 50 | [ ] | Castlevania Dominus Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (92%) | 96% | today | 86% |  |
| 51 | [ ] | Divinity: Original Sin 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 89% | today | 81% |  |
| 52 | [ ] | Library Of Ruina (STEAM) | 10 | 20 | 50% (14d) | Does not open (69%) | 88% | 2d ago | 79% |  |
| 53 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (74%) | 100% | 2d ago | n/a | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 54 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 78% | today | 83% |  |
| 55 | [ ] | Don't Starve Together (STEAM) | 10 | 20 | 50% (last 20) | Does not open (58%) | 78% | today | 67% |  |
| 56 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (82%) | 72% | 4d ago | 50% (drop) |  |
| 57 | [ ] | Aniimo (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 84% | 1d ago | 73% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 58 | [ ] | Cry of Fear (STEAM) | 13 | 20 | 65% (last 20) | Does not open (48%) | 76% | today | 75% |  |
| 59 | [ ] | MIO: Memories in Orbit (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (52%) | 95% | 3d ago | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 60 | [ ] | Resident Evil 7 Biohazard (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 78% | today | 68% |  |
| 61 | [ ] | ZERO Sievert (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | 89% | 1d ago | 71% |  |
| 62 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (50%) | 93% | 1d ago | 90% |  |
| 63 | [ ] | American Truck Simulator (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 77% | 2d ago | 68% |  |
| 64 | [ ] | Sid Meier's Civilization VI (STEAM) | 15 | 20 | 75% (last 20) | Does not open (66%) | 85% | 1d ago | 70% |  |
| 65 | [ ] | Prey (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 78% | 2d ago | 82% |  |
| 66 | [ ] | Need for Speed: Hot Pursuit (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 80% | 2d ago | 87% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 67 | [ ] | Forza Horizon 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (45%) | 69% | today | 24% (drop) | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 68 | [ ] | Darkest Dungeon® (EPIC) | 11 | 20 | 55% (last 20) | Does not open (64%) | 77% | today | 100% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 69 | [ ] | Disgaea 5 Complete (STEAM) | 16 | 20 | 80% (last 20) | Does not open (75%) | 91% | 1d ago | 91% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 70 | [ ] | OMORI (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 75% | today | 54% (drop) | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 71 | [ ] | Dota 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (78%) | 76% | 1d ago | 93% |  |
| 72 | [ ] | Ratatan (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 97% | today | n/a |  |
| 73 | [ ] | Dead Space (STEAM) | 15 | 20 | 75% (last 20) | Does not open (55%) | 84% | today | 81% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 74 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (51%) | 81% | 2d ago | 45% (drop) | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 75 | [ ] | Welcome to Elderfield (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 71% | today | 68% |  |
| 76 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 15 | 20 | 75% (last 20) | Does not open (48%) | 69% | 8d ago | 58% |  |
| 77 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (46%) | 86% | today | 81% |  |
| 78 | [ ] | Call of Duty 4: Modern Warfare (2007) (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (54%) | 87% | today | 58% (drop) |  |
| 79 | [ ] | Happy Wheels (STEAM) | 19 | 20 | 95% (last 20) | No graphics (52%) | 73% | 6d ago | 52% (drop) | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 80 | [ ] | Need for Speed™ Rivals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (62%) | 76% | 2d ago | 100% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 81 | [ ] | Fable - The Lost Chapters (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (49%) | 84% | today | 86% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 82 | [ ] | Abiotic Factor (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 69% | 2d ago | 76% |  |
| 83 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 61% | today | 64% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 84 | [ ] | Cave Story+ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | 88% | 2d ago | 68% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 85 | [ ] | Disco Elysium - The Final Cut (EPIC) | 10 | 20 | 50% (last 20) | Does not open (68%) | 97% | today | 96% |  |
| 86 | [ ] | Poppy Playtime (STEAM) | 11 | 20 | 55% (last 20) | Does not open (59%) | 72% | 4d ago | 61% |  |
| 87 | [ ] | Resident Evil Village (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 89% | 1d ago | 81% |  |
| 88 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (62%) | 97% | today | 100% |  |
| 89 | [ ] | River City Girls (EPIC) | 14 | 20 | 70% (last 20) | Does not open (48%) | 79% | 1d ago | 45% (drop) |  |
| 90 | [ ] | Sifu (EPIC) | 10 | 20 | 50% (last 20) | Does not open (65%) | 62% | today | 32% (drop) |  |
| 91 | [ ] | Bejeweled 3 (STEAM) | 10 | 20 | 50% (last 20) | No graphics (59%) | 92% | today | 90% |  |
| 92 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (82%) | 71% | 1d ago | n/a | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 93 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (82%) | 92% | 1d ago | n/a | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 94 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (54%) | 80% | 1d ago | 58% (drop) |  |
| 95 | [ ] | Until Then (STEAM) | 14 | 20 | 70% (last 20) | Does not open (80%) | 81% | 2d ago | 61% |  |
| 96 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 12 | 20 | 60% (last 20) | Does not open (100%) | 96% | 2d ago | 82% |  |
| 97 | [ ] | Alabaster Dawn (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (49%) | 90% | 1d ago | 88% |  |
| 98 | [ ] | Red Dead Redemption (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | 66% | 24d ago | 30% (drop) | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 99 | [ ] | Sid Meier's Civilization V (STEAM) | 16 | 20 | 80% (last 20) | Does not open (75%) | 60% | 2d ago | 61% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 100 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 14 | 20 | 70% (last 20) | Does not open (43%) | 71% | today | 67% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 101 | [ ] | Mini Motorways (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 73% | 1d ago | 64% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 102 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 63% | 6d ago | 64% |  |
| 103 | [ ] | Lethal Company (STEAM) | 10 | 20 | 50% (last 20) | Does not open (42%) | 81% | 1d ago | 74% |  |
| 104 | [ ] | Palia (STEAM) | 15 | 20 | 75% (last 20) | Does not open (57%) | 74% | 6d ago | n/a | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 105 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 90% | 4d ago | 75% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 106 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 13 | 20 | 65% (last 20) | Does not open (82%) | 65% | 4d ago | n/a | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 107 | [ ] | Cat Quest (EPIC) | 10 | 20 | 50% (last 20) | No graphics (47%) | 65% | today | 36% (drop) |  |
| 108 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (57%) | 64% | 1d ago | n/a |  |
| 109 | [ ] | TBH: Task Bar Hero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (64%) | 83% | 1d ago | 80% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 110 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | Directx error (36%) | 67% | 5d ago | 30% (drop) |  |
| 111 | [ ] | Minecraft Dungeons II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (82%) | 67% | today | 68% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 112 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 67% | 1d ago | 78% |  |
| 113 | [ ] | Deliver At All Costs (EPIC) | 13 | 20 | 65% (last 20) | Does not open (58%) | 65% | today | 56% |  |
| 114 | [ ] | The Legend of Heroes: Trails in the Sky (STEAM) | 10 | 20 | 50% (last 20) | Does not open (55%) | 94% | today | 91% |  |
| 115 | [ ] | Yakuza: Like a Dragon (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 65% | 5d ago | n/a |  |
| 116 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 74% | today | 74% |  |
| 117 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | 82% | 12d ago | n/a | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 118 | [ ] | Overwatch® (STEAM) | 18 | 20 | 90% (last 20) | Does not open (57%) | 62% | 5d ago | n/a | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 119 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 60% | 4d ago | n/a | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 120 | [ ] | Call of Duty: World at War (STEAM) | 14 | 20 | 70% (last 20) | Does not open (44%) | 86% | 5d ago | 67% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 121 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 94% | 14d ago | n/a |  |
| 122 | [ ] | Fallout (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 73% | 2d ago | 76% |  |
| 123 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (50%) | 85% | 2d ago | 69% |  |
| 124 | [ ] | Heavy Rain (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (65%) | 89% | today | 90% |  |
| 125 | [ ] | Driving Rogue (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 92% | 6d ago | 84% |  |
| 126 | [ ] | Sonic Generations (STEAM) | 16 | 20 | 80% (last 20) | Does not open (69%) | 67% | 5d ago | 83% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 127 | [ ] | Moonstone Island (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (60%) | 83% | 2d ago | 73% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 128 | [ ] | Dishonored - Definitive Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (89%) | 81% | today | 74% |  |
| 129 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 89% | today | 83% |  |
| 130 | [ ] | Tails of Iron (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 88% | 4d ago | n/a |  |
| 131 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 64% | 11d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 132 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (73%) | 60% | 1d ago | n/a | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 133 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 73% | 2d ago | 70% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 134 | [ ] | ENA: Dream BBQ (STEAM) | 10 | 20 | 50% (last 20) | Does not open (43%) | 76% | 3d ago | 54% (drop) |  |
| 135 | [ ] | PowerWash Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (81%) | 79% | today | 100% |  |
| 136 | [ ] | A Plague Tale: Innocence (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | 82% | 14d ago | 80% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 137 | [ ] | Max Payne (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (46%) | 87% | 8d ago | 70% |  |
| 138 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (84%) | 92% | today | 92% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 139 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 64% | today | 70% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 140 | [ ] | Fallout 3 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (43%) | 90% | 3d ago | 90% |  |
| 141 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | 93% | 11d ago | n/a | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 142 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (86%) | 92% | today | 93% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 143 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (48%) | 92% | 3d ago | 83% |  |
| 144 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 83% | 1d ago | 79% |  |
| 145 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (82%) | 94% | 1d ago | n/a | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 146 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 88% | today | 86% |  |
| 147 | [ ] | Sonic Lost World (STEAM) | 11 | 20 | 55% (last 20) | No graphics (65%) | 80% | today | 78% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 148 | [ ] | Street Fighter™ 6 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (81%) | 81% | 1d ago | 79% |  |
| 149 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 73% | today | 46% (drop) |  |
| 150 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (81%) | 73% | 11d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 151 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | 82% | today | n/a | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 152 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (77%) | 91% | 1d ago | n/a | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 153 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 73% | 6d ago | n/a |  |
| 154 | [ ] | Gothic 1 Classic (STEAM) | 12 | 20 | 60% (last 20) | Does not open (61%) | 80% | 4d ago | 56% (drop) |  |
| 155 | [ ] | Oxygen Not Included (STEAM) | 12 | 20 | 60% (last 20) | Does not open (74%) | 61% | 4d ago | 78% |  |
| 156 | [ ] | ABZU (EPIC) | 10 | 20 | 50% (last 20) | Does not open (86%) | 90% | 4d ago | 85% |  |
| 157 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (62%) | 85% | 8d ago | n/a | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 158 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | 83% | 12d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 159 | [ ] | Rivals of Aether II (STEAM) | 15 | 20 | 75% (last 20) | Does not open (54%) | 62% | 1d ago | 9% (drop) | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 160 | [ ] | Stellar Blade™ (STEAM) | 14 | 20 | 70% (last 20) | No graphics (43%) | 80% | 3d ago | 82% |  |
| 161 | [ ] | Gambonanza (STEAM) | 13 | 20 | 65% (last 20) | Does not open (60%) | 95% | today | 100% |  |
| 162 | [ ] | FINAL FANTASY V (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 87% | today | 79% |  |
| 163 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 62% | 4d ago | n/a | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 164 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (64%) | 64% | 2d ago | 50% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 165 | [ ] | Tabletop Simulator (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 64% | 5d ago | 77% |  |
| 166 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (55%) | 65% | 1d ago | 56% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 167 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | Does not open (53%) | 85% | 4d ago | 100% |  |
| 168 | [ ] | Control Ultimate Edition (GOG) | 13 | 20 | 65% (last 20) | Does not open (76%) | 86% | 2d ago | 73% |  |
| 169 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 11 | 20 | 55% (last 20) | Does not open (59%) | 70% | 10d ago | 62% |  |
| 170 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 85% | 2d ago | 83% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 171 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (57%) | 68% | 11d ago | n/a | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 172 | [ ] | Chained Echoes (GOG) | 14 | 20 | 70% (last 20) | Does not open (60%) | 67% | 5d ago | n/a |  |
| 173 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (73%) | 73% | 5d ago | n/a | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 174 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (61%) | 92% | 8d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 175 | [ ] | One-armed robber (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (65%) | 71% | 5d ago | 50% (drop) |  |
| 176 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | 73% | 5d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 177 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (82%) | 91% | 13d ago | 70% |  |
| 178 | [ ] | Unturned (STEAM) | 12 | 20 | 60% (last 20) | Does not open (47%) | 72% | 2d ago | 80% |  |
| 179 | [ ] | Counter-Strike:Global Offensive (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 77% | 3d ago | 80% |  |
| 180 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 90% | 23d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 181 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 89% | 1d ago | 82% |  |
| 182 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 92% | 3d ago | n/a |  |
| 183 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 14 | 20 | 70% (last 20) | Does not open (69%) | 66% | 7d ago | n/a | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 184 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 60% | 9d ago | n/a |  |
| 185 | [ ] | Dishonored 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (89%) | 84% | 4d ago | 72% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 186 | [ ] | State of Decay: Year-One (STEAM) | 11 | 20 | 55% (last 20) | Does not open (69%) | 76% | 1d ago | 65% |  |
| 187 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | 95% | 2d ago | n/a | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 188 | [ ] | Capcom Arcade Stadium (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | 71% | today | n/a | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 189 | [ ] | Digimon Survive (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (77%) | 96% | 1d ago | 90% |  |
| 190 | [ ] | TurretGirls (STEAM) | 12 | 20 | 60% (last 20) | No graphics (75%) | 92% | today | 83% |  |
| 191 | [ ] | The Witcher: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (59%) | 69% | 6d ago | n/a | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 192 | [ ] | Escape from Duckov (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (69%) | 94% | today | 100% |  |
| 193 | [ ] | Stumble Guys (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 73% | 2d ago | 64% |  |
| 194 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (47%) | 61% | 3d ago | 53% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 195 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (56%) | 71% | 7d ago | n/a | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 196 | [ ] | Subnautica 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (58%) | 60% | 2d ago | n/a | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 197 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (62%) | 66% | 1d ago | 25% (drop) |  |
| 198 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (60%) | 67% | 3d ago | 55% |  |
| 199 | [ ] | My Summer Car (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | 82% | today | n/a |  |
| 200 | [ ] | Limbus Company (STEAM) | 11 | 20 | 55% (last 20) | Does not open (85%) | 82% | 1d ago | 93% |  |
| 201 | [ ] | Final Fantasy IV (3D Remake) (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 95% | 2d ago | n/a |  |
| 202 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 87% | 7d ago | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 203 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (69%) | 92% | 18d ago | n/a | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 204 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (72%) | 85% | 1d ago | n/a | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 205 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (61%) | 94% | 8d ago | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 206 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 74% | 16d ago | n/a | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 207 | [ ] | Supermarket Together (STEAM) | 15 | 20 | 75% (last 20) | Does not open (73%) | 68% | 8d ago | 79% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 208 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 71% | 2d ago | n/a | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 209 | [ ] | Mortal Kombat 11 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 72% | 5d ago | n/a |  |
| 210 | [ ] | Moonring (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 97% | today | 91% |  |
| 211 | [ ] | Battle Brothers (STEAM) | 10 | 20 | 50% (last 20) | Does not open (68%) | 72% | today | 82% |  |
| 212 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 100% | 2d ago | n/a | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 213 | [ ] | Darksiders (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 80% | 19d ago | 73% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 214 | [ ] | Lucid Blocks (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 63% | today | 57% |  |
| 215 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 77% | 1d ago | 73% |  |
| 216 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | 70% | 10d ago | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 217 | [ ] | Maneater (STEAM) | 15 | 20 | 75% (last 20) | Does not open (92%) | 62% | 7d ago | n/a |  |
| 218 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 73% | 16d ago | 60% |  |
| 219 | [ ] | GOD EATER RESURRECTION (STEAM) | 14 | 20 | 70% (last 20) | Does not open (56%) | 71% | 17d ago | n/a |  |
| 220 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (67%) | 71% | 1d ago | n/a | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 221 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (44%) | 83% | 6d ago | n/a |  |
| 222 | [ ] | Trailmakers (STEAM) | 12 | 20 | 60% (last 20) | Does not open (44%) | 92% | 1d ago | n/a |  |
| 223 | [ ] | Goat Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 74% | 5d ago | n/a |  |
| 224 | [ ] | Jade Empire: Special Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 74% | 4d ago | n/a | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 225 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | 91% | 1d ago | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 226 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 82% | 1d ago | n/a |  |
| 227 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (92%) | 86% | 26d ago | n/a |  |
| 228 | [ ] | Invisible, Inc. (STEAM) | 15 | 20 | 75% (last 20) | Does not open (63%) | 69% | 14d ago | n/a |  |
| 229 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 15 | 20 | 75% (last 20) | No graphics (53%) | 75% | 2d ago | n/a | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 230 | [ ] | Ultimate Custom Night (STEAM) | 14 | 20 | 70% (last 20) | No graphics (68%) | 67% | 15d ago | n/a | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 231 | [ ] | Return to Monkey Island (STEAM) | 14 | 20 | 70% (last 20) | No graphics (62%) | 75% | 6d ago | n/a |  |
| 232 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (42%) | 78% | 8d ago | n/a | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 233 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 85% | 3d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 234 | [ ] | SnowRunner (STEAM) | 13 | 20 | 65% (last 20) | Does not open (96%) | 78% | 4d ago | n/a | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 235 | [ ] | Zero Escape: The Nonary Games (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 63% | 3d ago | 70% |  |
| 236 | [ ] | MX Bikes (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 94% | today | n/a |  |
| 237 | [ ] | Resident Evil Revelations 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (45%) | 82% | today | 73% |  |
| 238 | [ ] | Secrets of Grindea (STEAM) | 11 | 20 | 55% (last 20) | Does not open (45%) | 73% | 19d ago | n/a | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 239 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 20 | 80% (last 20) | Does not open (82%) | 63% | 20d ago | n/a | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 240 | [ ] | Cat Mail Co. (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 85% | 1d ago | 80% |  |
| 241 | [ ] | Deus Ex™ GOTY Edition (GOG) | 12 | 20 | 60% (last 20) | No graphics (44%) | 87% | 13d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 242 | [ ] | CRUEL (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 67% | today | n/a | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 243 | [ ] | Revolution Idle (STEAM) | 12 | 20 | 60% (last 20) | Does not open (43%) | 73% | 6d ago | n/a |  |
| 244 | [ ] | Serious Sam 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (63%) | 90% | today | n/a |  |
| 245 | [ ] | Bongo Cat (STEAM) | 15 | 20 | 75% (last 20) | Does not open (70%) | 74% | 7d ago | n/a | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 246 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (83%) | 81% | 5d ago | n/a | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 247 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 65% | 4d ago | n/a |  |
| 248 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 89% | 5d ago | n/a |  |
| 249 | [ ] | Astral Party  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (85%) | 93% | today | n/a |  |
| 250 | [ ] | Hero Siege (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (50%) | 70% | 2d ago | 91% |  |
| 251 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 79% | 6d ago | n/a |  |
| 252 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (44%) | 92% | 13d ago | n/a |  |
| 253 | [ ] | Tales of Zestiria (STEAM) | 14 | 20 | 70% (last 20) | Does not open (79%) | 69% | 18d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 254 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (95%) | 95% | 4d ago | 89% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 255 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 13 | 20 | 65% (last 20) | No graphics (37%) | 87% | 2d ago | n/a | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 256 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (45%) | 65% | 8d ago | n/a |  |
| 257 | [ ] | PAYDAY: The Heist (STEAM) | 13 | 20 | 65% (last 20) | Does not open (75%) | 70% | 6d ago | n/a |  |
| 258 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (100%) | 76% | 8d ago | n/a |  |
| 259 | [ ] | 12 is Better Than 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 83% | 8d ago | n/a |  |
| 260 | [ ] | Big Walk (STEAM) | 11 | 20 | 55% (last 20) | Does not open (65%) | 71% | 10d ago | 42% (drop) |  |
| 261 | [ ] | Hitman: Absolution (GOG) | 11 | 20 | 55% (last 20) | Does not open (85%) | 73% | 7d ago | n/a |  |
| 262 | [ ] | Football Manager 2024 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (91%) | 65% | 5d ago | 40% (drop) |  |
| 263 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 94% | 1d ago | 86% |  |
| 264 | [ ] | Capcom Fighting Collection (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 73% | 4d ago | n/a | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 265 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 14 | 20 | 70% (last 20) | Does not open (85%) | 67% | 5d ago | n/a | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 266 | [ ] | Timberborn (STEAM) | 13 | 20 | 65% (last 20) | No graphics (62%) | 84% | 10d ago | n/a |  |
| 267 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (89%) | 80% | 5d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 268 | [ ] | AER Memories of Old (EPIC) | 13 | 20 | 65% (last 20) | Does not open (85%) | 93% | 1d ago | n/a |  |
| 269 | [ ] | Allumeria (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 75% | 3d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 270 | [ ] | Sons Of The Forest (STEAM) | 13 | 20 | 65% (last 20) | Does not open (57%) | 73% | 6d ago | n/a |  |
| 271 | [ ] | Disgaea 4 Complete+ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (43%) | 90% | 12d ago | n/a | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 272 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 12 | 20 | 60% (last 20) | Does not open (57%) | 71% | 8d ago | n/a | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 273 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 67% | 4d ago | 55% |  |
| 274 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 60% | today | 40% (drop) |  |
| 275 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 88% | 5d ago | n/a |  |
| 276 | [ ] | Hatred (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 88% | 5d ago | n/a |  |
| 277 | [ ] | Chef Knight (STEAM) | 14 | 20 | 70% (last 20) | Does not open (100%) | 60% | 17d ago | n/a |  |
| 278 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 77% | 3d ago | n/a |  |
| 279 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (77%) | 76% | 26d ago | n/a |  |
| 280 | [ ] | Mortal Shell (EPIC) | 12 | 20 | 60% (last 20) | No graphics (64%) | 72% | today | 31% (drop) |  |
| 281 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (45%) | 74% | 5d ago | n/a | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 282 | [ ] | BATTLETECH (STEAM) | 11 | 20 | 55% (last 20) | Does not open (43%) | 88% | today | n/a |  |
| 283 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (57%) | 90% | 3d ago | n/a |  |
| 284 | [ ] | Monster Boy And The Cursed Kingdom (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (84%) | 88% | 13d ago | n/a |  |
| 285 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 73% | 4d ago | 67% |  |
| 286 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 91% | 11d ago | 100% |  |
| 287 | [ ] | Katanaut (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | 64% | 7d ago | n/a | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 288 | [ ] | Spark the Electric Jester (STEAM) | 14 | 20 | 70% (last 20) | Does not open (62%) | 60% | 8d ago | n/a | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 289 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (58%) | 70% | 10d ago | n/a |  |
| 290 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 60% | 3d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 291 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | 90% | 7d ago | n/a |  |
| 292 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 60% | 1d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 293 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (92%) | 89% | 8d ago | n/a |  |
| 294 | [ ] | Antichamber (STEAM) | 11 | 20 | 55% (last 20) | Does not open (33%) | 73% | 2d ago | n/a |  |
| 295 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | No graphics (70%) | 75% | 2d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 296 | [ ] | Pinball FX Classic (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 95% | 8d ago | n/a |  |
| 297 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 64% | 29d ago | n/a |  |
| 298 | [ ] | Hylics (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (67%) | 97% | today | n/a |  |
| 299 | [ ] | Intravenous (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 78% | 4d ago | n/a |  |
| 300 | [ ] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 88% | 9d ago | 80% |  |
| 301 | [ ] | The Stanley Parable (STEAM) | 13 | 20 | 65% (last 20) | Does not open (89%) | 62% | 18d ago | n/a |  |
| 302 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 80% | 41d ago | n/a |  |
| 303 | [ ] | Legend of Grimrock 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 85% | 6d ago | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 304 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | 90% | 1d ago | n/a |  |
| 305 | [ ] | Assassin's Creed Odyssey (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 67% | 6d ago | 70% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 306 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 95% | 1d ago | 100% |  |
| 307 | [ ] | GRANDIA II HD Remaster (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 71% | 16d ago | n/a |  |
| 308 | [ ] | Subnautica: Below Zero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 70% | 4d ago | n/a |  |
| 309 | [ ] | Need for Speed™ Unbound (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 63% | 16d ago | n/a | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 310 | [ ] | Shift At Midnight (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | 82% | 7d ago | 80% |  |
| 311 | [ ] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | 71% | today | 83% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 312 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (56%) | 92% | 15d ago | n/a | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 313 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 73% | 6d ago | 70% |  |
| 314 | [ ] | Haydee (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 78% | 7d ago | n/a |  |
| 315 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 70% | 15d ago | n/a |  |
| 316 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 70% | 6d ago | n/a |  |
| 317 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 87% | 3d ago | 83% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 318 | [ ] | Killing Floor (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (100%) | 86% | 5d ago | n/a |  |
| 319 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 64% | today | n/a |  |
| 320 | [ ] | Castle in the Clouds (STEAM) | 10 | 20 | 50% (last 20) | No graphics (63%) | 76% | 13d ago | n/a |  |
| 321 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 67% | 4d ago | n/a | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 322 | [ ] | Forgive Me Father (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 62% | 5d ago | n/a |  |
| 323 | [ ] | WORLD OF FINAL FANTASY (STEAM) | 10 | 20 | 50% (last 20) | No graphics (55%) | 71% | 6d ago | n/a |  |
| 324 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 92% | 14d ago | n/a |  |
| 325 | [ ] | Sid Meier's Civilization VI (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 75% | 10d ago | 40% (drop) |  |

## Recently recovered (480)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Slay the Spire (STEAM) | 1326 | 2026-11-09 | 1651 | 60% | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [x] | Grim Dawn (STEAM) | 527 | 2026-11-08 | 587 | 63% |  |
| 3 | [x] | FINAL FANTASY RESONANCE (STEAM) | 409 | 2026-10-24 | 921 | 77% |  |
| 4 | [x] | Half-Life (STEAM) | 348 | 2026-11-09 | 617 | 71% |  |
| 5 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 231 | 2026-10-19 | 291 | 71% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 6 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 228 | 2026-11-09 | 320 | 90% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 7 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 224 | 2026-11-09 | 267 | 64% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 8 | [x] | MONSTER HUNTER RISE (STEAM) | 208 | 2026-11-09 | 506 | 62% |  |
| 9 | [x] | Counter-Strike 2 (STEAM) | 208 | 2026-11-13 | 291 | 61% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 10 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 203 | 2026-11-09 | 357 | 74% |  |
| 11 | [x] | BeamNG.drive (STEAM) | 201 | 2026-11-09 | 243 | 81% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 12 | [x] | Devil May Cry HD Collection (STEAM) | 199 | 2026-10-19 | 288 | 80% |  |
| 13 | [x] | Call of Duty: Black Ops (STEAM) | 197 | 2026-11-13 | 220 | 26% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 14 | [x] | OMORI (STEAM) | 192 | 2026-11-09 | 236 | 75% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 15 | [x] | DRAGON BALL FighterZ (STEAM) | 183 | 2026-11-01 | 219 | 78% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 16 | [x] | Spelunky 2 (STEAM) | 180 | 2026-11-01 | 214 | 70% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 17 | [x] | DREDGE (EPIC) | 169 | 2026-11-09 | 211 | 72% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 18 | [x] | Sid Meier's Civilization V (STEAM) | 166 | 2026-11-10 | 177 | 60% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 19 | [x] | BioShock (STEAM) | 152 | 2026-11-09 | 300 | 74% |  |
| 20 | [x] | Geometry Dash (STEAM) | 149 | 2026-11-11 | 444 | 48% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 21 | [x] | Prototype (STEAM) | 141 | 2026-11-11 | 206 | 57% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 22 | [x] | Burnout Paradise: The Ultimate Box (STEAM) | 138 | 2026-10-16 | 238 | 72% |  |
| 23 | [x] | Team Fortress 2 (STEAM) | 135 | 2026-11-09 | 231 | 75% |  |
| 24 | [x] | Castlevania Advance Collection (STEAM) | 133 | 2026-11-09 | 202 | 89% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 25 | [x] | Minecraft Dungeons II (STEAM) | 129 | 2026-11-09 | 148 | 67% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 26 | [x] | Counter-Strike (STEAM) | 128 | 2026-11-11 | 208 | 46% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 27 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 128 | 2026-11-09 | 169 | 64% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 28 | [x] | Mirror's Edge (STEAM) | 127 | 2026-11-09 | 179 | 72% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 29 | [x] | Call of Duty: Black Ops III (STEAM) | 122 | 2026-10-18 | 254 | 79% |  |
| 30 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 120 | 2026-10-18 | 175 | 77% |  |
| 31 | [x] | Assassin's Creed II (STEAM) | 118 | 2026-11-10 | 123 | 61% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 32 | [x] | Aniimo (STEAM) | 112 | 2026-11-09 | 151 | 84% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 33 | [x] | The Witcher: Enhanced Edition (STEAM) | 111 | 2026-11-09 | 130 | 69% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 34 | [x] | Cave Story+ (STEAM) | 109 | 2026-11-09 | 120 | 88% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 35 | [x] | Caravan SandWitch (EPIC) | 108 | 2026-11-09 | 175 | 65% |  |
| 36 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 107 | 2026-11-09 | 145 | 92% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 37 | [x] | Moonstone Island (STEAM) | 98 | 2026-11-09 | 131 | 83% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 38 | [x] | Happy Wheels (STEAM) | 97 | 2026-11-09 | 117 | 73% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 39 | [x] | Fallout: New Vegas PCR (STEAM) | 90 | 2026-11-13 | 120 | 60% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 40 | [x] | Catherine Classic (STEAM) | 89 | 2026-11-09 | 165 | 70% |  |
| 41 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 89 | 2026-11-09 | 115 | 92% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 42 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 88 | 2026-11-09 | 141 | 70% |  |
| 43 | [x] | Hi-Fi RUSH (STEAM) | 87 | 2026-11-11 | 121 | 46% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 44 | [x] | Quake (STEAM) | 85 | 2026-11-09 | 255 | 84% |  |
| 45 | [x] | DOOM 3: BFG Edition (STEAM) | 84 | 2026-11-09 | 124 | 70% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 46 | [x] | Ultra Street Fighter IV (STEAM) | 83 | 2026-10-17 | 181 | 69% |  |
| 47 | [x] | Cry of Fear (STEAM) | 83 | 2026-10-18 | 166 | 76% |  |
| 48 | [x] | Vital Shell (STEAM) | 83 | 2026-11-09 | 131 | 86% |  |
| 49 | [x] | FINAL FANTASY XIII-2 (STEAM) | 81 | 2026-11-09 | 84 | 62% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 50 | [x] | Age of Empires II: Definitive Edition (STEAM) | 80 | 2026-11-10 | 96 | 64% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 51 | [x] | Psychonauts (STEAM) | 79 | 2026-11-09 | 147 | 94% |  |
| 52 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 79 | 2026-10-18 | 134 | 97% |  |
| 53 | [x] | STEINS;GATE (STEAM) | 78 | 2026-11-09 | 111 | 91% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 54 | [x] | Ballionaire (STEAM) | 75 | 2026-11-09 | 122 | 88% |  |
| 55 | [x] | Don't Starve Together (STEAM) | 74 | 2026-10-16 | 157 | 78% |  |
| 56 | [x] | Brawlhalla (STEAM) | 74 | 2026-11-09 | 146 | 73% |  |
| 57 | [x] | Sovereign Tower (STEAM) | 73 | 2026-11-09 | 127 | 75% |  |
| 58 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 73 | 2026-11-09 | 112 | 87% |  |
| 59 | [x] | Spyro™ Reignited Trilogy (STEAM) | 70 | 2026-11-09 | 110 | 74% |  |
| 60 | [x] | Cyberpunk 2077 (GOG) | 70 | 2026-11-09 | 89 | 70% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 61 | [x] | Disgaea 5 Complete (STEAM) | 70 | 2026-11-09 | 82 | 91% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 62 | [x] | Need for Speed: Hot Pursuit (STEAM) | 69 | 2026-11-09 | 103 | 80% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 63 | [x] | Stardew Valley (GOG) | 68 | 2026-11-11 | 120 | 68% |  |
| 64 | [x] | Dota 2 (STEAM) | 68 | 2026-11-09 | 102 | 76% |  |
| 65 | [x] | The Sims™ 4 (STEAM) | 68 | 2026-11-09 | 90 | 76% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 66 | [x] | Bayonetta (STEAM) | 67 | 2026-10-18 | 205 | 84% |  |
| 67 | [x] | American Truck Simulator (STEAM) | 67 | 2026-11-09 | 111 | 77% |  |
| 68 | [x] | Fable - The Lost Chapters (STEAM) | 67 | 2026-11-09 | 105 | 84% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 69 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 67 | 2026-11-09 | 102 | 78% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 70 | [x] | Diablo® IV (STEAM) | 67 | 2026-11-11 | 79 | 60% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 71 | [x] | MIO: Memories in Orbit (STEAM) | 66 | 2026-11-09 | 122 | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 72 | [x] | Hogwarts Legacy (EPIC) | 65 | 2026-11-09 | 98 | 66% |  |
| 73 | [x] | Call of Juarez Gunslinger (STEAM) | 65 | 2026-11-09 | 80 | 73% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 74 | [x] | Don't Starve (STEAM) | 63 | 2026-10-16 | 157 | 79% |  |
| 75 | [x] | Fallout (STEAM) | 63 | 2026-11-09 | 98 | 73% |  |
| 76 | [x] | Order of the Sinking Star (STEAM) | 63 | 2026-11-09 | 91 | 66% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 77 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 63 | 2026-11-11 | 79 | 50% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 78 | [x] | Gunfire Reborn (STEAM) | 63 | 2026-11-09 | 69 | 93% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 79 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 62 | 2026-11-09 | 86 | 81% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 80 | [x] | Firewatch (STEAM) | 61 | 2026-11-10 | 117 | 67% |  |
| 81 | [x] | Sol Cesto (EPIC) | 61 | 2026-11-09 | 63 | 71% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 82 | [x] | Poppy Playtime (STEAM) | 60 | 2026-11-09 | 104 | 72% |  |
| 83 | [x] | eFootball™ (STEAM) | 60 | 2026-11-09 | 89 | 62% |  |
| 84 | [x] | Borderlands 3 (STEAM) | 60 | 2026-11-09 | 82 | 87% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 85 | [x] | Borderlands: The Pre-Sequel (STEAM) | 59 | 2026-11-09 | 93 | 64% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 86 | [x] | Darksiders (STEAM) | 59 | 2026-11-09 | 74 | 80% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 87 | [x] | Deskrawl: Idle ARPG (STEAM) | 58 | 2026-11-09 | 72 | 85% | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 88 | [x] | A Plague Tale: Innocence (STEAM) | 58 | 2026-11-09 | 61 | 82% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 89 | [x] | Mini Motorways (STEAM) | 57 | 2026-11-09 | 97 | 73% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 90 | [x] | TBH: Task Bar Hero (STEAM) | 57 | 2026-11-09 | 91 | 83% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 91 | [x] | Sonic Generations (STEAM) | 56 | 2026-11-09 | 64 | 67% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 92 | [x] | Until Then (STEAM) | 55 | 2026-10-17 | 92 | 81% |  |
| 93 | [x] | Starbound (STEAM) | 55 | 2026-11-09 | 87 | 76% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 94 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 55 | 2026-11-09 | 86 | 90% |  |
| 95 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 54 | 2026-10-25 | 101 | 63% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 96 | [x] | Call of Duty: World at War (STEAM) | 54 | 2026-11-09 | 77 | 86% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 97 | [x] | Grand Theft Auto V (EPIC) | 54 | 2026-11-09 | 60 | 74% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 98 | [x] | Deadlock (STEAM) | 53 | 2026-10-16 | 73 | 87% |  |
| 99 | [x] | Dead Space (STEAM) | 53 | 2026-10-18 | 67 | 84% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 100 | [x] | Alex Kidd in Miracle World DX (EPIC) | 53 | 2026-11-09 | 61 | 65% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 101 | [x] | Overwatch® (STEAM) | 53 | 2026-11-10 | 56 | 62% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 102 | [x] | Sonic Adventure DX (STEAM) | 50 | 2026-10-17 | 88 | 67% |  |
| 103 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 50 | 2026-11-09 | 85 | 56% |  |
| 104 | [x] | Oxygen Not Included (STEAM) | 50 | 2026-11-11 | 84 | 61% |  |
| 105 | [x] | Last Epoch (STEAM) | 50 | 2026-11-09 | 75 | 82% |  |
| 106 | [x] | Darkest Dungeon® (EPIC) | 49 | 2026-11-09 | 90 | 77% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 107 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 49 | 2026-11-09 | 82 | 48% |  |
| 108 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 49 | 2026-11-09 | 78 | 81% |  |
| 109 | [x] | Big Walk (STEAM) | 49 | 2026-11-09 | 76 | 71% |  |
| 110 | [x] | MudRunner (STEAM) | 48 | 2026-10-24 | 104 | 64% |  |
| 111 | [x] | Okami HD (STEAM) | 48 | 2026-11-09 | 93 | 91% |  |
| 112 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 48 | 2026-10-19 | 91 | 68% |  |
| 113 | [x] | Abiotic Factor (STEAM) | 48 | 2026-10-18 | 82 | 69% |  |
| 114 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 2026-11-09 | 74 | 92% |  |
| 115 | [x] | Rivals of Aether II (STEAM) | 46 | 2026-11-09 | 65 | 62% | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 116 | [x] | Sheepy: A Short Adventure (STEAM) | 46 | 2026-11-09 | 55 | 74% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 117 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 46 | 2026-11-09 | 53 | 91% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 118 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 45 | 2026-11-09 | 79 | 80% |  |
| 119 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 44 | 2026-11-13 | 60 | 60% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 120 | [x] | Moonlighter (EPIC) | 44 | 2026-11-09 | 48 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 121 | [x] | Mortal Kombat X (STEAM) | 43 | 2026-10-17 | 75 | 89% |  |
| 122 | [x] | Sonic Lost World (STEAM) | 43 | 2026-11-09 | 62 | 80% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 123 | [x] | Forza Horizon 4 (STEAM) | 43 | 2026-11-09 | 59 | 69% | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 124 | [x] | Tomb Raider GOTY (GOG) | 42 | 2026-10-17 | 102 | 94% |  |
| 125 | [x] | PROTOTYPE 2 (STEAM) | 42 | 2026-10-18 | 89 | 72% |  |
| 126 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 42 | 2026-11-09 | 63 | 73% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 127 | [x] | Guildrun Demo (STEAM) | 42 | 2026-11-09 | 59 | 75% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 128 | [x] | Aggelos (STEAM) | 42 | 2026-11-09 | 57 | 94% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 129 | [x] | Ace Attorney Investigations Collection (STEAM) | 41 | 2026-11-09 | 71 | 87% |  |
| 130 | [x] | The Bazaar (STEAM) | 41 | 2026-11-09 | 69 | 81% |  |
| 131 | [x] | Tomb Raider: Anniversary (STEAM) | 41 | 2026-11-09 | 64 | 66% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 132 | [x] | Rayman Origins (STEAM) | 40 | 2026-10-17 | 90 | 85% |  |
| 133 | [x] | Life is Strange™ (STEAM) | 39 | 2026-10-17 | 82 | 79% |  |
| 134 | [x] | Digimon World: Next Order (STEAM) | 39 | 2026-11-09 | 77 | 90% |  |
| 135 | [x] | Library Of Ruina (STEAM) | 39 | 2026-10-16 | 75 | 88% |  |
| 136 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 39 | 2026-11-09 | 71 | 89% |  |
| 137 | [x] | Frostpunk (STEAM) | 39 | 2026-11-09 | 64 | 69% |  |
| 138 | [x] | Dead by Daylight (STEAM) | 39 | 2026-11-09 | 43 | 85% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 139 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-11-09 | 40 | 82% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 140 | [x] | Amnesia: The Dark Descent (STEAM) | 38 | 2026-11-09 | 74 | 76% |  |
| 141 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 38 | 2026-11-09 | 71 | 91% |  |
| 142 | [x] | FINAL FANTASY VII (2013) (STEAM) | 38 | 2026-11-09 | 55 | 71% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 143 | [x] | Capcom Arcade Stadium (STEAM) | 38 | 2026-11-09 | 48 | 71% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 144 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 38 | 2026-11-09 | 39 | 82% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 145 | [x] | Sonic Origins (STEAM) | 37 | 2026-11-09 | 70 | 83% |  |
| 146 | [x] | Street Fighter™ 6 (STEAM) | 37 | 2026-11-09 | 63 | 81% |  |
| 147 | [x] | Russian Fishing 4 (STEAM) | 37 | 2026-11-09 | 43 | 85% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 148 | [x] | CrossCode (GOG) | 37 | 2026-11-09 | 40 | 73% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 149 | [x] | Death Road to Canada (STEAM) | 36 | 2026-10-17 | 97 | 78% |  |
| 150 | [x] | Little Nightmares (STEAM) | 36 | 2026-10-16 | 79 | 70% |  |
| 151 | [x] | Age of Empires II (2013) (STEAM) | 36 | 2026-11-09 | 62 | 67% |  |
| 152 | [x] | Rogue Legacy (STEAM) | 35 | 2026-10-17 | 83 | 81% |  |
| 153 | [x] | Teardown (STEAM) | 35 | 2026-10-17 | 78 | 85% |  |
| 154 | [x] | Tales of ARISE (STEAM) | 35 | 2026-10-16 | 75 | 90% |  |
| 155 | [x] | POSTAL 2 (GOG) | 35 | 2026-11-09 | 70 | 92% |  |
| 156 | [x] | SurrounDead (STEAM) | 35 | 2026-11-09 | 67 | 93% |  |
| 157 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 35 | 2026-11-09 | 61 | 70% |  |
| 158 | [x] | XCOM 2 (STEAM) | 35 | 2026-11-09 | 59 | 100% |  |
| 159 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 35 | 2026-11-09 | 46 | 92% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 160 | [x] | Elite Dangerous (STEAM) | 35 | 2026-11-09 | 38 | 64% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 161 | [x] | Cobalt Core (STEAM) | 34 | 2026-10-18 | 87 | 87% |  |
| 162 | [x] | Salt and Sanctuary (STEAM) | 34 | 2026-10-18 | 75 | 83% |  |
| 163 | [x] | Rocket League (STEAM) | 34 | 2026-10-17 | 59 | 71% |  |
| 164 | [x] | Hero Siege (STEAM) | 34 | 2026-11-09 | 57 | 70% |  |
| 165 | [x] | Need for Speed™ Rivals (STEAM) | 34 | 2026-11-10 | 47 | 76% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 166 | [x] | Super Animal Royale (STEAM) | 34 | 2026-11-09 | 45 | 60% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 167 | [x] | Romestead (STEAM) | 34 | 2026-11-09 | 44 | 64% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 168 | [x] | Journey (STEAM) | 33 | 2026-10-27 | 73 | 67% |  |
| 169 | [x] | Ultimate Chicken Horse (STEAM) | 33 | 2026-10-23 | 68 | 75% |  |
| 170 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 33 | 2026-11-09 | 66 | 86% |  |
| 171 | [x] | State of Decay: Year-One (STEAM) | 33 | 2026-10-18 | 66 | 76% |  |
| 172 | [x] | Hearts of Iron IV (STEAM) | 33 | 2026-11-09 | 62 | 71% |  |
| 173 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 2026-11-09 | 53 | 88% |  |
| 174 | [x] | Gauntlet™  (STEAM) | 33 | 2026-11-11 | 47 | 43% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 175 | [x] | Dishonored - Definitive Edition (EPIC) | 32 | 2026-10-17 | 80 | 81% |  |
| 176 | [x] | Torchlight II (STEAM) | 32 | 2026-10-20 | 72 | 88% |  |
| 177 | [x] | COCOON (STEAM) | 32 | 2026-11-09 | 62 | 85% |  |
| 178 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 32 | 2026-11-11 | 60 | 36% |  |
| 179 | [x] | Max Payne (STEAM) | 32 | 2026-11-09 | 56 | 87% |  |
| 180 | [x] | Counter-Strike:Global Offensive (STEAM) | 32 | 2026-11-09 | 52 | 77% |  |
| 181 | [x] | Earthion (STEAM) | 32 | 2026-11-09 | 52 | 100% |  |
| 182 | [x] | SnowRunner (STEAM) | 32 | 2026-11-09 | 46 | 78% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 183 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-11-09 | 41 | 85% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 184 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 31 | 2026-11-09 | 68 | 70% |  |
| 185 | [x] | BioShock™ (GOG) | 31 | 2026-10-18 | 67 | 79% |  |
| 186 | [x] | Stumble Guys (STEAM) | 31 | 2026-10-18 | 59 | 73% |  |
| 187 | [x] | Deponia (STEAM) | 31 | 2026-11-09 | 57 | 64% |  |
| 188 | [x] | Nioh: Complete Edition (STEAM) | 31 | 2026-11-09 | 42 | 92% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 189 | [x] | Bloodstained: Curse of the Moon (STEAM) | 30 | 2026-10-16 | 75 | 73% |  |
| 190 | [x] | Sable (EPIC) | 30 | 2026-10-18 | 69 | 67% |  |
| 191 | [x] | Resident Evil Village (STEAM) | 30 | 2026-11-09 | 53 | 89% |  |
| 192 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 30 | 2026-11-09 | 50 | 67% |  |
| 193 | [x] | Sol Cesto (STEAM) | 30 | 2026-11-11 | 48 | 60% |  |
| 194 | [x] | Supermarket Together (STEAM) | 30 | 2026-11-09 | 42 | 68% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 195 | [x] | Red Dead Redemption (STEAM) | 30 | 2026-11-09 | 33 | 66% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 196 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 29 | 2026-11-09 | 59 | 85% |  |
| 197 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 29 | 2026-11-09 | 56 | 88% |  |
| 198 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 2026-10-17 | 54 | 82% |  |
| 199 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 29 | 2026-11-09 | 53 | 69% |  |
| 200 | [x] | Prince of Persia: The Sands of Time (STEAM) | 29 | 2026-11-09 | 49 | 85% |  |
| 201 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 29 | 2026-11-09 | 47 | 88% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 202 | [x] | Secrets of Grindea (STEAM) | 29 | 2026-11-09 | 47 | 73% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 203 | [x] | Yakuza: Like a Dragon (STEAM) | 29 | 2026-11-09 | 46 | 65% |  |
| 204 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 68% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 205 | [x] | Subnautica 2 (STEAM) | 29 | 2026-11-10 | 34 | 60% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 206 | [x] | Grand Theft Auto III (STEAM) | 28 | 2026-10-17 | 74 | 81% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 207 | [x] | Owlboy (STEAM) | 28 | 2026-11-02 | 60 | 60% |  |
| 208 | [x] | Aethermancer (STEAM) | 28 | 2026-10-18 | 50 | 85% |  |
| 209 | [x] | Gambonanza (STEAM) | 28 | 2026-11-09 | 47 | 95% |  |
| 210 | [x] | Capcom Fighting Collection 2 (STEAM) | 28 | 2026-11-09 | 45 | 77% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 211 | [x] | Tower and Sword of Succubus (STEAM) | 28 | 2026-11-09 | 43 | 86% |  |
| 212 | [x] | Skullgirls 2nd Encore (STEAM) | 27 | 2026-11-10 | 63 | 64% |  |
| 213 | [x] | PlateUp! (STEAM) | 27 | 2026-10-16 | 58 | 88% |  |
| 214 | [x] | G.I. Joe Wrath of Cobra (EPIC) | 27 | 2026-11-09 | 48 | 64% |  |
| 215 | [x] | Heavy Rain (STEAM) | 27 | 2026-11-09 | 48 | 89% |  |
| 216 | [x] | Dead Rising 2 (STEAM) | 27 | 2026-11-09 | 43 | 63% |  |
| 217 | [x] | Digimon Survive (STEAM) | 27 | 2026-11-09 | 40 | 96% |  |
| 218 | [x] | Palia (STEAM) | 27 | 2026-11-09 | 39 | 74% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 219 | [x] | Gothic II: Gold Classic (STEAM) | 27 | 2026-11-09 | 37 | 71% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 220 | [x] | Ultimate Custom Night (STEAM) | 27 | 2026-11-09 | 37 | 67% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 221 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 26 | 2026-10-19 | 94 | 92% |  |
| 222 | [x] | Monster Hunter Stories (STEAM) | 26 | 2026-10-17 | 61 | 80% |  |
| 223 | [x] | Mirror's Edge™ (GOG) | 26 | 2026-11-13 | 46 | 54% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 224 | [x] | Battle Brothers (STEAM) | 26 | 2026-11-09 | 45 | 72% |  |
| 225 | [x] | Soul's Remnant (STEAM) | 26 | 2026-11-11 | 45 | n/a |  |
| 226 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 45 | 63% |  |
| 227 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 26 | 2026-11-09 | 37 | 71% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 228 | [x] | CRUEL (STEAM) | 26 | 2026-11-09 | 34 | 67% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 229 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 26 | 2026-11-09 | 30 | 100% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 230 | [x] | Dying Light (EPIC) | 25 | 2026-10-17 | 60 | 76% |  |
| 231 | [x] | Resident Evil Revelations 2 (STEAM) | 25 | 2026-11-09 | 49 | 82% |  |
| 232 | [x] | Being a DIK (STEAM) | 25 | 2026-11-09 | 46 | 64% |  |
| 233 | [x] | Counter-Strike: Condition Zero (STEAM) | 25 | 2026-11-11 | 43 | 36% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 234 | [x] | Limbus Company (STEAM) | 25 | 2026-11-09 | 39 | 82% |  |
| 235 | [x] | Ratatan (STEAM) | 25 | 2026-11-09 | 38 | 97% |  |
| 236 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 25 | 2026-11-09 | 33 | 92% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 237 | [x] | Bongo Cat (STEAM) | 25 | 2026-11-09 | 32 | 74% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 238 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-09 | 32 | 90% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 239 | [x] | Crab Game (STEAM) | 25 | 2026-11-09 | 31 | 95% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 240 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 25 | 2026-11-09 | 31 | 71% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 241 | [x] | Tales of Zestiria (STEAM) | 25 | 2026-11-09 | 31 | 69% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 242 | [x] | Northgard: Definitive Edition (STEAM) | 25 | 2026-11-09 | 28 | 83% | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 243 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 57 | 90% |  |
| 244 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 24 | 2026-11-09 | 46 | 97% |  |
| 245 | [x] | Unturned (STEAM) | 24 | 2026-11-09 | 43 | 72% |  |
| 246 | [x] | Prince of Persia (GOG) | 24 | 2026-11-09 | 42 | 89% |  |
| 247 | [x] | Opus Magnum (STEAM) | 24 | 2026-11-09 | 39 | 92% |  |
| 248 | [x] | Moonlight Peaks (STEAM) | 24 | 2026-11-09 | 35 | 81% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 249 | [x] | Jade Empire: Special Edition (GOG) | 24 | 2026-11-09 | 31 | 78% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 250 | [x] | Jade Empire: Special Edition (STEAM) | 24 | 2026-11-09 | 27 | 74% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 251 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 23 | 2026-10-20 | 52 | 89% |  |
| 252 | [x] | Chained Echoes (GOG) | 23 | 2026-11-08 | 48 | 67% |  |
| 253 | [x] | WEBFISHING (STEAM) | 23 | 2026-10-17 | 48 | 89% |  |
| 254 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 46 | 88% |  |
| 255 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-11-09 | 45 | 89% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 256 | [x] | Lucid Blocks (STEAM) | 23 | 2026-11-09 | 43 | 63% |  |
| 257 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 23 | 2026-11-09 | 41 | 78% |  |
| 258 | [x] | Football Manager 2024 (EPIC) | 23 | 2026-11-09 | 40 | 65% |  |
| 259 | [x] | Worms W.M.D (STEAM) | 23 | 2026-11-09 | 40 | 90% |  |
| 260 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 2026-11-09 | 36 | 76% |  |
| 261 | [x] | Return to Monkey Island (STEAM) | 23 | 2026-11-09 | 36 | 75% |  |
| 262 | [x] | Timberborn (STEAM) | 23 | 2026-11-09 | 34 | 84% |  |
| 263 | [x] | Borderlands: The Pre-Sequel (EPIC) | 23 | 2026-11-09 | 33 | 71% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 264 | [x] | Cities: Skylines (STEAM) | 23 | 2026-11-13 | 33 | 60% | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 265 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 95% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 266 | [x] | CarX Drift Racing Online (STEAM) | 22 | 2026-10-16 | 57 | 80% |  |
| 267 | [x] | Goat Simulator (STEAM) | 22 | 2026-11-09 | 45 | 74% |  |
| 268 | [x] | Crazy Taxi (STEAM) | 22 | 2026-11-10 | 42 | 68% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 269 | [x] | Wizard of Legend (EPIC) | 22 | 2026-11-09 | 40 | 83% |  |
| 270 | [x] | Cat Mail Co. (STEAM) | 22 | 2026-11-09 | 38 | 85% |  |
| 271 | [x] | Trailmakers (STEAM) | 22 | 2026-11-09 | 38 | 92% |  |
| 272 | [x] | My Summer Car (STEAM) | 22 | 2026-11-09 | 37 | 82% |  |
| 273 | [x] | Tabletop Simulator (STEAM) | 22 | 2026-11-09 | 36 | 64% |  |
| 274 | [x] | Deus Ex™ GOTY Edition (GOG) | 22 | 2026-11-09 | 35 | 87% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 275 | [x] | Dishonored 2 (STEAM) | 22 | 2026-11-09 | 32 | 84% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 276 | [x] | SOMA (STEAM) | 22 | 2026-11-09 | 32 | 60% | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 277 | [x] | Beyond: Two Souls (STEAM) | 22 | 2026-11-09 | 31 | 65% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 278 | [x] | CarX Street (STEAM) | 22 | 2026-11-09 | 28 | 87% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 279 | [x] | Tearscape (STEAM) | 22 | 2026-11-09 | 27 | 94% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 280 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 60 | 98% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 281 | [x] | Slow Roads (STEAM) | 21 | 2026-10-22 | 46 | 85% |  |
| 282 | [x] | Control Ultimate Edition (GOG) | 21 | 2026-11-09 | 39 | 86% |  |
| 283 | [x] | Pinball FX Classic (STEAM) | 21 | 2026-11-09 | 38 | 95% |  |
| 284 | [x] | Invisible, Inc. (STEAM) | 21 | 2026-11-09 | 37 | 69% |  |
| 285 | [x] | SWORN (STEAM) | 21 | 2026-11-09 | 36 | 95% |  |
| 286 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 89% |  |
| 287 | [x] | Sapphire Safari (GOG) | 21 | 2026-11-09 | 28 | 80% | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 288 | [x] | Titan Quest Anniversary Edition (STEAM) | 20 | 2026-10-16 | 62 | 95% |  |
| 289 | [x] | Saints Row IV (STEAM) | 20 | 2026-10-19 | 51 | 84% |  |
| 290 | [x] | MudRunner (EPIC) | 20 | 2026-10-18 | 44 | 75% |  |
| 291 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-11-09 | 38 | 100% |  |
| 292 | [x] | GOD EATER RESURRECTION (STEAM) | 20 | 2026-11-09 | 31 | 71% |  |
| 293 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 20 | 2026-11-09 | 30 | 87% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 294 | [x] | Party Animals (STEAM) | 20 | 2026-11-09 | 29 | 71% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 295 | [x] | Torchlight II (EPIC) | 20 | 2026-11-09 | 28 | 81% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 296 | [x] | Tyr (STEAM) | 20 | 2026-11-09 | 28 | 73% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 297 | [x] | Dead Island (STEAM) | 20 | 2026-11-09 | 25 | 92% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 298 | [x] | Cyberpunk 2077 (EPIC) | 20 | 2026-11-12 | 24 | 61% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 299 | [x] | BlazBlue Centralfiction (STEAM) | 19 | 2026-10-17 | 54 | 84% |  |
| 300 | [x] | No Rest for the Wicked (STEAM) | 19 | 2026-10-19 | 45 | 80% |  |
| 301 | [x] | Sorry We're Closed (EPIC) | 19 | 2026-11-09 | 34 | 72% |  |
| 302 | [x] | One-armed robber (STEAM) | 19 | 2026-11-09 | 34 | 71% |  |
| 303 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 19 | 2026-11-09 | 33 | 76% |  |
| 304 | [x] | Far Far West (STEAM) | 19 | 2026-11-09 | 33 | 64% |  |
| 305 | [x] | Stick It to the Stickman (STEAM) | 19 | 2026-11-09 | 33 | 73% |  |
| 306 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 32 | 62% |  |
| 307 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 19 | 2026-11-09 | 29 | 87% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 308 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 19 | 2026-11-09 | 25 | 75% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 309 | [x] | Cave Story+ (EPIC) | 18 | 2026-10-18 | 42 | 88% |  |
| 310 | [x] | Backpack Battles (STEAM) | 18 | 2026-11-09 | 42 | 100% |  |
| 311 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 18 | 2026-11-09 | 30 | 80% |  |
| 312 | [x] | Maneater (STEAM) | 18 | 2026-11-09 | 28 | 62% |  |
| 313 | [x] | Arcade Paradise (EPIC) | 18 | 2026-11-09 | 27 | 65% |  |
| 314 | [x] | Capcom Fighting Collection (STEAM) | 18 | 2026-11-09 | 26 | 73% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 315 | [x] | Need for Speed™ Unbound (STEAM) | 18 | 2026-11-09 | 26 | 63% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 316 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-09 | 23 | 70% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 317 | [x] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 2026-11-09 | 22 | 91% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 318 | [x] | ABZÛ (STEAM) | 17 | 2026-10-21 | 45 | 97% |  |
| 319 | [x] | Kingdom Come: Deliverance II (STEAM) | 17 | 2026-10-20 | 41 | 86% |  |
| 320 | [x] | Spin Rhythm XD (STEAM) | 17 | 2026-10-18 | 38 | 84% |  |
| 321 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 37 | 17% |  |
| 322 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 36 | 88% |  |
| 323 | [x] | Guacamelee! Gold Edition (STEAM) | 17 | 2026-11-11 | 32 | 75% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 324 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 17 | 2026-11-09 | 30 | 83% |  |
| 325 | [x] | Shank 2 (STEAM) | 17 | 2026-11-09 | 29 | 90% |  |
| 326 | [x] | DNF Duel (EPIC) | 17 | 2026-11-09 | 28 | 66% |  |
| 327 | [x] | Mortal Shell (EPIC) | 17 | 2026-11-09 | 28 | 72% |  |
| 328 | [x] | Sonic and SEGA All Stars Racing (STEAM) | 17 | 2026-11-09 | 26 | 66% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 329 | [x] | Katanaut (STEAM) | 17 | 2026-11-09 | 23 | 64% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 330 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 17 | 2026-11-09 | 22 | 92% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 331 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 332 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 333 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 51 | 94% |  |
| 334 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 16 | 2026-10-25 | 41 | 77% |  |
| 335 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 16 | 2026-10-20 | 36 | 79% |  |
| 336 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 16 | 2026-11-11 | 35 | 50% |  |
| 337 | [x] | Overlord (STEAM) | 16 | 2026-11-08 | 35 | 62% |  |
| 338 | [x] | GRIP: Combat Racing (STEAM) | 16 | 2026-11-09 | 34 | 80% |  |
| 339 | [x] | sobosuba (STEAM) | 16 | 2026-11-09 | 32 | 86% |  |
| 340 | [x] | Faster Than Light (EPIC) | 16 | 2026-11-09 | 31 | 92% |  |
| 341 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 342 | [x] | Tiny Glade (STEAM) | 16 | 2026-11-09 | 31 | 72% |  |
| 343 | [x] | GRANDIA HD Remaster (STEAM) | 16 | 2026-11-09 | 29 | 79% |  |
| 344 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 60% |  |
| 345 | [x] | Assassin's Creed Odyssey (STEAM) | 16 | 2026-11-09 | 25 | 67% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 346 | [x] | Legend of Grimrock 2 (STEAM) | 16 | 2026-11-09 | 24 | 85% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 347 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 16 | 2026-11-09 | 24 | 88% |  |
| 348 | [x] | Allumeria (STEAM) | 16 | 2026-11-09 | 23 | 75% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 349 | [x] | Spark the Electric Jester (STEAM) | 16 | 2026-11-13 | 22 | 60% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 350 | [x] | Darksiders Warmastered Edition (EPIC) | 16 | 2026-11-09 | 21 | 63% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 351 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 352 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 353 | [x] | Sacred Gold (STEAM) | 16 | 2026-11-09 | 20 | 70% | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 354 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 15 | 2026-10-19 | 55 | 84% |  |
| 355 | [x] | Blood: Fresh Supply (STEAM) | 15 | 2026-10-16 | 40 | 78% |  |
| 356 | [x] | Grim Fandango Remastered (STEAM) | 15 | 2026-10-19 | 39 | 72% |  |
| 357 | [x] | Mark of the Ninja (STEAM) | 15 | 2026-10-26 | 32 | 78% |  |
| 358 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 31 | 96% |  |
| 359 | [x] | Sonic Superstars (STEAM) | 15 | 2026-10-21 | 30 | 67% |  |
| 360 | [x] | Human Fall Flat (STEAM) | 15 | 2026-10-29 | 29 | 61% |  |
| 361 | [x] | Mortal Kombat 11 (STEAM) | 15 | 2026-11-09 | 29 | 72% |  |
| 362 | [x] | Hitman: Absolution (GOG) | 15 | 2026-11-09 | 28 | 73% |  |
| 363 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 15 | 2026-11-09 | 28 | 65% |  |
| 364 | [x] | Need for Speed: Undercover (STEAM) | 15 | 2026-11-11 | 28 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 365 | [x] | Titanfall® 2 (STEAM) | 15 | 2026-11-09 | 28 | 68% |  |
| 366 | [x] | Batman™: Arkham Origins (GOG) | 15 | 2026-11-09 | 26 | 100% |  |
| 367 | [x] | Gloomwood (STEAM) | 15 | 2026-11-09 | 26 | 64% |  |
| 368 | [x] | Wildermyth (STEAM) | 15 | 2026-11-09 | 26 | 80% |  |
| 369 | [x] | Nex Machina (STEAM) | 15 | 2026-11-09 | 24 | 74% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 370 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 85% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 371 | [x] | Chef Knight (STEAM) | 15 | 2026-11-09 | 22 | 60% |  |
| 372 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 373 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 15 | 2026-11-09 | 21 | 67% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 374 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 375 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 14 | 2026-10-21 | 43 | 81% |  |
| 376 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 92% |  |
| 377 | [x] | Killing Floor (STEAM) | 14 | 2026-10-19 | 29 | 86% |  |
| 378 | [x] | Evoland (STEAM) | 14 | 2026-11-11 | 28 | n/a |  |
| 379 | [x] | Antichamber (STEAM) | 14 | 2026-11-11 | 27 | 73% |  |
| 380 | [x] | MX Bikes (STEAM) | 14 | 2026-11-09 | 27 | 94% |  |
| 381 | [x] | Ultrapool (STEAM) | 14 | 2026-11-09 | 27 | 100% |  |
| 382 | [x] | AER Memories of Old (EPIC) | 14 | 2026-11-09 | 25 | 93% |  |
| 383 | [x] | WORLD OF FINAL FANTASY (STEAM) | 14 | 2026-11-09 | 24 | 71% |  |
| 384 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 23 | 77% |  |
| 385 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 386 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-11-09 | 21 | 90% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 387 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 388 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 389 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 13 | 2026-10-19 | 31 | 95% |  |
| 390 | [x] | Divinity: Original Sin (Classic) (STEAM) | 13 | 2026-10-16 | 30 | 70% |  |
| 391 | [x] | No Man's Sky (GOG) | 13 | 2026-10-19 | 29 | 91% |  |
| 392 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 29 | 50% |  |
| 393 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 29 | 73% |  |
| 394 | [x] | Dead Space™ 3 (STEAM) | 13 | 2026-10-20 | 28 | 75% |  |
| 395 | [x] | Intravenous 2 (STEAM) | 13 | 2026-11-09 | 27 | 97% |  |
| 396 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 27 | 73% |  |
| 397 | [x] | Blaster Master Zero (STEAM) | 13 | 2026-11-11 | 26 | 58% |  |
| 398 | [x] | Ready or Not (STEAM) | 13 | 2026-11-09 | 25 | 81% |  |
| 399 | [x] | Ghostwire Tokyo (EPIC) | 13 | 2026-11-09 | 23 | 79% |  |
| 400 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 13 | 2026-11-09 | 23 | 73% |  |
| 401 | [x] | Haydee (STEAM) | 13 | 2026-11-09 | 23 | 78% |  |
| 402 | [x] | 12 is Better Than 6 (STEAM) | 13 | 2026-11-09 | 22 | 83% |  |
| 403 | [x] | Horny Villa (STEAM) | 13 | 2026-11-09 | 22 | 90% |  |
| 404 | [x] | PAYDAY: The Heist (STEAM) | 13 | 2026-11-13 | 22 | 70% |  |
| 405 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 22 | 73% |  |
| 406 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 407 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 71% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 408 | [x] | The Stanley Parable (STEAM) | 13 | 2026-11-13 | 21 | 62% |  |
| 409 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 89% |  |
| 410 | [x] | Alabaster Dawn Demo (STEAM) | 13 | 2026-11-09 | 20 | 76% |  |
| 411 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 412 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 13 | 2026-10-23 | 20 | 61% |  |
| 413 | [x] | Super Monkey Ball Banana Mania (STEAM) | 13 | 2026-11-13 | 20 | 70% |  |
| 414 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 80% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 415 | [x] | Tom Clancy's Splinter Cell: Chaos Theory (STEAM) | 12 | 2026-10-16 | 31 | 84% |  |
| 416 | [x] | CULTIC (STEAM) | 12 | 2026-11-09 | 28 | 55% |  |
| 417 | [x] | Haiku, the Robot (STEAM) | 12 | 2026-10-21 | 28 | n/a |  |
| 418 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 12 | 2026-10-18 | 28 | 94% |  |
| 419 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 12 | 2026-11-01 | 27 | n/a |  |
| 420 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 26 | 71% |  |
| 421 | [x] | Alan Wake's American Nightmare (EPIC) | 12 | 2026-11-09 | 25 | 65% |  |
| 422 | [x] | Rayman Origins (GOG) | 12 | 2026-11-09 | 25 | 76% |  |
| 423 | [x] | Lust Goddess (STEAM) | 12 | 2026-11-09 | 25 | 88% |  |
| 424 | [x] | Injustice™ 2 (STEAM) | 12 | 2026-10-17 | 24 | 57% |  |
| 425 | [x] | Lost Castle 2 (STEAM) | 12 | 2026-11-09 | 24 | 94% |  |
| 426 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-11-09 | 23 | 95% |  |
| 427 | [x] | HITMAN World of Assassination (STEAM) | 12 | 2026-11-09 | 23 | 87% |  |
| 428 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 23 | 69% |  |
| 429 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-10 | 22 | 67% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 430 | [x] | DiRT 4 (STEAM) | 12 | 2026-11-09 | 22 | 92% |  |
| 431 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 12 | 2026-11-13 | 22 | 70% |  |
| 432 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 12 | 2026-11-09 | 21 | 70% |  |
| 433 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 434 | [x] | Shift At Midnight (STEAM) | 12 | 2026-11-09 | 21 | 82% |  |
| 435 | [x] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 2026-11-12 | 21 | 90% |  |
| 436 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 437 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 438 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 2026-11-10 | 20 | 60% |  |
| 439 | [x] | Turbo Overkill (STEAM) | 12 | 2026-11-09 | 20 | 95% |  |
| 440 | [x] | Middle-earth™: Shadow of War™ (STEAM) | 11 | 2026-10-16 | 34 | 83% |  |
| 441 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 2026-11-09 | 25 | 89% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 442 | [x] | Breath of Fire IV (GOG) | 11 | 2026-10-26 | 25 | 58% |  |
| 443 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 2026-10-27 | 25 | 80% |  |
| 444 | [x] | Aperture Desk Job (STEAM) | 11 | 2026-11-03 | 24 | n/a |  |
| 445 | [x] | Cruelty Squad (STEAM) | 11 | 2026-11-09 | 24 | 95% |  |
| 446 | [x] | Life is Strange Remastered (STEAM) | 11 | 2026-11-09 | 23 | 86% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 447 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 23 | 79% |  |
| 448 | [x] | Castle in the Clouds (STEAM) | 11 | 2026-11-09 | 22 | 76% |  |
| 449 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 21 | 71% |  |
| 450 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 451 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 452 | [x] | Distance (STEAM) | 10 | 2026-10-19 | 28 | 74% |  |
| 453 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 26 | n/a |  |
| 454 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 10 | 2026-10-23 | 24 | 88% |  |
| 455 | [x] | Coromon (GOG) | 10 | 2026-10-19 | 22 | 67% |  |
| 456 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 22 | 86% |  |
| 457 | [x] | Sid Meier's Civilization VI (EPIC) | 10 | 2026-10-19 | 21 | 75% |  |
| 458 | [x] | UNDEFEATED (STEAM) | 10 | 2026-11-09 | 21 | 73% |  |
| 459 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 460 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 461 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 462 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 20 | 78% |  |
| 463 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 464 | [x] | The WereCleaner (STEAM) | 9 | 2026-10-22 | 30 | 90% |  |
| 465 | [x] | TowerFall Ascension (STEAM) | 9 | 2026-10-16 | 30 | 70% |  |
| 466 | [x] | Possessor(s) (STEAM) | 9 | 2026-10-24 | 27 | 88% |  |
| 467 | [x] | SteamWorld Heist (GOG) | 9 | 2026-10-25 | 21 | n/a |  |
| 468 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 9 | 2026-10-21 | 21 | 92% |  |
| 469 | [x] | Football Manager 2024 (STEAM) | 9 | 2026-10-16 | 20 | n/a |  |
| 470 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 9 | 2026-11-09 | 20 | 84% |  |
| 471 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 29% |  |
| 472 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 9 | 2026-10-20 | 20 | n/a |  |
| 473 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 8 | 2026-10-20 | 25 | 81% |  |
| 474 | [x] | SCP – Containment Breach (STEAM) | 8 | 2026-10-27 | 22 | 92% |  |
| 475 | [x] | Gloomhaven (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 476 | [x] | Mina the Hollower (GOG) | 8 | 2026-10-28 | 20 | 71% |  |
| 477 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 20 | 53% |  |
| 478 | [x] | Mafia II: Definitive Edition (STEAM) | 7 | 2026-10-16 | 20 | 85% |  |
| 479 | [x] | What Remains of Edith Finch (STEAM) | 6 | 2026-10-19 | 26 | 73% |  |
| 480 | [x] | Alex Kidd in Miracle World DX (STEAM) | 2 | 2026-10-16 | 35 | 93% |  |
