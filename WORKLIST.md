# GameNative compatibility worklist

Generated: `2026-11-17T04:15:12.282Z` · Ratings since: `2026-08-19T04:15:12.282Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 129 |
| Probably does not work | 187 |
| Fix shipped, waiting for ratings | 18 |
| First launch fails | 310 |
| Mixed | 474 |
| Works | 1030 |
| Total | 2148 |

## Does not work (129)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 160 | 183 | 87% (14d) | Does not open (83%) | 53% | today | 19% (drop) | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 117 | 137 | 85% (since fix) | Does not open (92%) | 47% | today | 37% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 3 | [ ] | Rocket League® (EPIC) | 75 | 87 | 86% (14d) | Does not open (79%) | 46% | today | 29% | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 4 | [ ] | Hogwarts Legacy (STEAM) | 28 | 28 | 100% (14d) | Does not open (66%) | 34% | today | 15% | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 5 | [x] 2026-10-18 | Project Zomboid (STEAM) | 55 | 61 | 90% (since fix) | Does not open (64%) | 46% | 1d ago | 38% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 6 | [ ] | Bloons TD 6 (EPIC) | 23 | 27 | 85% (14d) | Does not open (78%) | 41% | today | 21% (drop) | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 7 | [ ] | Saints Row 2 (STEAM) | 22 | 22 | 100% (14d) | Does not open (97%) | 32% | 1d ago | 33% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 8 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 21 | 26 | 81% (14d) | Does not open (75%) | 56% | today | 54% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 9 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 21 | 23 | 91% (14d) | Does not open (96%) | 44% | 2d ago | 21% (drop) | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 10 | [ ] | Metro 2033 Redux (STEAM) | 19 | 26 | 73% (14d) | Does not open (70%) | 41% | today | 39% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 11 | [ ] | Borderlands 2 (EPIC) | 19 | 21 | 90% (14d) | Does not open (80%) | 52% | today | 44% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 12 | [ ] | Saints Row 2 (GOG) | 19 | 24 | 79% (14d) | Does not open (92%) | 39% | 4d ago | 37% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 13 | [ ] | Sifu (EPIC) | 16 | 22 | 73% (14d) | Does not open (69%) | 50% | 1d ago | 39% | [#535](https://github.com/GameNative/gamenative-compat/issues/535) |
| 14 | [ ] | Mafia II (Classic) (STEAM) | 20 | 20 | 100% (last 20) | Does not open (78%) | 8% | today | 9% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 15 | [ ] | Metro: Last Light Redux (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | 22% | today | 24% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 16 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 15 | 20 | 75% (last 20) | Does not open (75%) | 55% | 1d ago | 43% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 17 | [ ] | Call of Duty: Black Ops II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 35% | 2d ago | 41% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 18 | [ ] | Fallout: New Vegas PCR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | 57% | 2d ago | 59% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 19 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (92%) | 24% | 3d ago | 19% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 20 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | No graphics (46%) | 30% | 1d ago | 40% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 21 | [ ] | Path of Exile (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 27% | today | 18% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 22 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (78%) | 0% | 2d ago | 0% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 23 | [ ] | skate. (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | 11% | today | 15% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 24 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 41% | 2d ago | 30% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 25 | [ ] | Hogwarts Legacy (EPIC) | 14 | 20 | 70% (last 20) | Does not open (75%) | 54% | today | 42% | [#537](https://github.com/GameNative/gamenative-compat/issues/537) |
| 26 | [ ] | Detroit: Become Human (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 55% | 1d ago | 60% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 27 | [ ] | Forza Horizon 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (44%) | 58% | 4d ago | 22% (drop) | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 28 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (70%) | 20% | 11d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 29 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | 8% | 3d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 30 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 13% | 5d ago | 8% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 31 | [ ] | The Witcher: Enhanced Edition (GOG) | 19 | 20 | 95% (last 20) | Does not open (73%) | 7% | 8d ago | 8% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 32 | [ ] | Fall Guys (EPIC) | 19 | 20 | 95% (last 20) | Does not open (74%) | 15% | 2d ago | 8% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 33 | [ ] | CPM 2 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 8% | 1d ago | 7% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 34 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | Does not open (54%) | 0% | 20d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 35 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (67%) | 14% | 1d ago | 25% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 36 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | 0% | 2d ago | n/a | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 37 | [ ] | MECCHA CHAMELEON (STEAM) | 16 | 20 | 80% (last 20) | Does not open (65%) | 48% | 2d ago | 33% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 38 | [ ] | Trackmania (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 17% | 1d ago | 27% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 39 | [ ] | Deliver At All Costs (EPIC) | 14 | 20 | 70% (last 20) | Does not open (60%) | 55% | 1d ago | 50% | [#538](https://github.com/GameNative/gamenative-compat/issues/538) |
| 40 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (92%) | 9% | 18d ago | n/a | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 41 | [ ] | Call of Duty® (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | 5% | today | n/a | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 42 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (70%) | 12% | 16d ago | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 43 | [ ] | Borderlands GOTY (STEAM) | 17 | 20 | 85% (last 20) | Does not open (94%) | 41% | 4d ago | 50% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 44 | [ ] | Vampire Survivors (EPIC) | 14 | 20 | 70% (last 20) | Does not open (60%) | 49% | 3d ago | 30% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 45 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (62%) | 50% | 1d ago | n/a | [#536](https://github.com/GameNative/gamenative-compat/issues/536) |
| 46 | [ ] | Breath of Fire IV (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | 15% | today | 8% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 47 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (67%) | 18% | 3d ago | 30% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 48 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (80%) | 15% | 8d ago | 19% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 49 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 56% | 1d ago | 55% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 50 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (88%) | 23% | 8d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 51 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 59% | 7d ago | 36% (drop) | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 52 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (83%) | 35% | 1d ago | 38% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 53 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 12% | 2d ago | 10% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 54 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (88%) | 46% | 4d ago | 50% | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 55 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (69%) | 28% | 5d ago | 27% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 56 | [ ] | Blood Omen: Legacy of Kain (GOG) | 16 | 20 | 80% (last 20) | No graphics (57%) | 54% | 1d ago | n/a | [#539](https://github.com/GameNative/gamenative-compat/issues/539) |
| 57 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | 0% | 3d ago | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 58 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (56%) | 25% | 12d ago | 18% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 59 | [ ] | Half-Life: Blue Shift (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 38% | today | 45% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 60 | [ ] | Rivals of Aether II (STEAM) | 16 | 20 | 80% (last 20) | Does not open (54%) | 50% | today | 7% (drop) | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 61 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (73%) | 57% | 5d ago | n/a | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 62 | [ ] | Kenshi (STEAM) | 15 | 20 | 75% (last 20) | Does not open (89%) | 3% | today | 0% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 63 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | 50% | 38d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 64 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 0% | 2d ago | n/a | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 65 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 29% | 8d ago | 38% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 66 | [ ] | Chained Echoes (GOG) | 14 | 20 | 70% (last 20) | Does not open (60%) | 59% | 3d ago | 50% |  |
| 67 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 25% | today | 40% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 68 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 33% | 3d ago | 40% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 69 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (76%) | 38% | 5d ago | 20% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 70 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (45%) | 42% | 12d ago | 38% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 71 | [ ] | Black Mesa (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | 21% | 24d ago | 31% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 72 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | 10% | 4d ago | 10% | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 73 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | 38% | today | n/a | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 74 | [ ] | Watch_Dogs (STEAM) | 14 | 20 | 70% (last 20) | Does not open (90%) | 33% | 10d ago | 46% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 75 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | 50% | 6d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 76 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | 40% | today | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 77 | [ ] | XCOM: Enemy Unknown (STEAM) | 18 | 20 | 90% (last 20) | Does not open (71%) | 14% | 3d ago | 20% | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 78 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (71%) | 32% | 10d ago | 25% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 79 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | 10% | 15d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 80 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 18% | 26d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 81 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (58%) | 59% | 5d ago | 56% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 82 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | Does not open (63%) | 16% | 10d ago | 30% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 83 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 18% | 15d ago | n/a | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 84 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 43% | 5d ago | n/a | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 85 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (50%) | 59% | today | 56% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 86 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (76%) | 0% | 30d ago | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 87 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (67%) | 0% | 23d ago | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 88 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 2% | 5d ago | 0% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 89 | [ ] | Changed (STEAM) | 15 | 20 | 75% (last 20) | Does not open (69%) | 57% | 4d ago | 44% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 90 | [ ] | Umamusume: Pretty Derby (STEAM) | 19 | 20 | 95% (last 20) | Does not open (83%) | 48% | today | 54% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 91 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 12% | 17d ago | n/a | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 92 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (90%) | 20% | 9d ago | n/a | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 93 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 3% | 12d ago | 5% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 94 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 46% | 5d ago | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 95 | [ ] | Supermarket Together (STEAM) | 15 | 20 | 75% (last 20) | Does not open (65%) | 59% | today | 72% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 96 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 19 | 20 | 95% (last 20) | No graphics (57%) | 39% | 3d ago | 50% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 97 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (76%) | 19% | today | 20% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 98 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (91%) | 0% | 23d ago | 0% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 99 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (69%) | 36% | 33d ago | n/a | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 100 | [ ] | OneShot (STEAM) | 16 | 20 | 80% (last 20) | Does not open (96%) | 15% | 32d ago | n/a | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 101 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | 36% | 7d ago | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 102 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 25% | 15d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 103 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (97%) | 36% | 15d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 104 | [ ] | Hotline Miami (GOG) | 15 | 20 | 75% (last 20) | Does not open (90%) | 59% | 7d ago | 73% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 105 | [ ] | Lost Planet: Extreme Condition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 42% | 2d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 106 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (62%) | 56% | 5d ago | 24% (drop) | [#540](https://github.com/GameNative/gamenative-compat/issues/540) |
| 107 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (90%) | 27% | 1d ago | 31% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 108 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (83%) | 46% | 2d ago | 50% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 109 | [ ] | Aliens vs. Predator (STEAM) | 16 | 20 | 80% (last 20) | No graphics (55%) | 26% | 5d ago | 27% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 110 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 36% | 17d ago | n/a | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 111 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (67%) | 50% | 6d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 112 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 36% | 1d ago | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 113 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 35% | 31d ago | 30% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 114 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (76%) | 30% | today | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 115 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | 35% | 17d ago | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 116 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | 53% | 3d ago | 38% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 117 | [ ] | The Lantern of the Laughless Saint (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | 46% | 14d ago | n/a | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 118 | [ ] | Zuma Deluxe (STEAM) | 18 | 20 | 90% (last 20) | Does not open (94%) | 31% | 4d ago | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 119 | [ ] | Beyond Good & Evil™ (GOG) | 17 | 20 | 85% (last 20) | Does not open (100%) | 20% | 24d ago | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 120 | [ ] | Maneater (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 54% | 3d ago | 50% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 121 | [ ] | Ultimate Custom Night (STEAM) | 14 | 20 | 70% (last 20) | No graphics (71%) | 57% | 19d ago | n/a | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 122 | [ ] | skate.™ (EPIC) | 18 | 20 | 90% (last 20) | Does not open (87%) | 0% | 22d ago | n/a | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 123 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 20 | 80% (last 20) | Does not open (82%) | 59% | 1d ago | n/a | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 124 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (67%) | 53% | 8d ago | n/a | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 125 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (54%) | 58% | 2d ago | n/a | [#541](https://github.com/GameNative/gamenative-compat/issues/541) |
| 126 | [ ] | Maneater (EPIC) | 16 | 20 | 80% (last 20) | Does not open (75%) | 44% | 1d ago | n/a | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 127 | [ ] | Hitman 2: Silent Assassin (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 35% | today | 42% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 128 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 30% | 12d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 129 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 50% | 9d ago | 50% | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |

## Probably does not work (187)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Counter-Strike 2 (STEAM) | 43 | 66 | 65% (since fix) | Does not open (68%) | 59% | today | 63% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 2 | [ ] | theHunter Classic (STEAM) | 20 | 20 | 100% (last 20) | No graphics (92%) | n/a | 13d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 3 | [ ] | Euro Truck Simulator 2 (STEAM) | 16 | 26 | 62% (14d) | Does not open (65%) | 56% | today | 57% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 4 | [ ] | To The Moon (GOG) | 18 | 20 | 90% (last 20) | Does not open (86%) | n/a | 14d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 5 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 24 | 43 | 56% (since fix) | Does not open (74%) | 59% | today | 52% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 6 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (76%) | n/a | 8d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 7 | [ ] | FINAL FANTASY XIII (STEAM) | 12 | 20 | 60% (14d) | Does not open (76%) | 54% | today | 57% |  |
| 8 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 13 | 20 | 65% (last 20) | Does not open (61%) | 50% | 2d ago | 38% |  |
| 9 | [ ] | Bully: Scholarship Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 51% | 1d ago | 11% (drop) |  |
| 10 | [ ] | Owlboy (STEAM) | 10 | 20 | 50% (last 20) | Does not open (86%) | 51% | 2d ago | 45% |  |
| 11 | [ ] | Garry's Mod (STEAM) | 9 | 17 | 53% (since fix) | Does not open (79%) | 56% | today | 44% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 12 | [ ] | VRChat (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 40% | 3d ago | 35% |  |
| 13 | [ ] | Driver: Parallel Lines (STEAM) | 19 | 20 | 95% (last 20) | Does not open (65%) | n/a | 8d ago | n/a | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 14 | [ ] | Asterigos: Curse of the Stars (STEAM) | 17 | 20 | 85% (last 20) | Graphics glitches (73%) | n/a | today | n/a |  |
| 15 | [ ] | Gorilla Tag (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 15% | 2d ago | 8% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 16 | [ ] | Door Kickers 2 (STEAM) | 20 | 20 | 100% (last 20) | No graphics (86%) | n/a | 34d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 17 | [ ] | Teenage Mutant Ninja Turtles: Shredder's Revenge (EPIC) | 13 | 20 | 65% (last 20) | Does not open (82%) | 59% | 1d ago | 44% |  |
| 18 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 37d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 19 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (36%) | n/a | 14d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 20 | [ ] | Yume Nikki (STEAM) | 11 | 20 | 55% (last 20) | Does not open (87%) | 33% | 2d ago | 51% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 21 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | No graphics (38%) | 53% | 2d ago | 33% (drop) |  |
| 22 | [ ] | Cat Quest (EPIC) | 10 | 20 | 50% (last 20) | Does not open (45%) | 53% | today | 36% |  |
| 23 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 21d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 24 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 11 | 19 | 58% (since fix) | Does not open (78%) | 31% | 1d ago | 41% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 25 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 10d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 26 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 13 | 20 | 65% (last 20) | Does not open (84%) | 59% | 8d ago | n/a | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 27 | [ ] | Metro 2033 Redux (EPIC) | 11 | 20 | 55% (last 20) | Does not open (58%) | 25% | 2d ago | 38% |  |
| 28 | [ ] | Sonic Adventure™ 2  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 48% | 5d ago | 38% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 29 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | 5% | today | n/a |  |
| 30 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 18d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 31 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | n/a | 9d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 32 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (93%) | n/a | today | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 33 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 13 | 20 | 65% (last 20) | Does not open (84%) | 52% | 6d ago | 67% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 34 | [ ] | CODE VEIN (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | 35% | 1d ago | 15% (drop) | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 35 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (85%) | 54% | 7d ago | n/a |  |
| 36 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 19% | 2d ago | 7% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 37 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (100%) | n/a | 6d ago | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 38 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 12d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 39 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (88%) | n/a | 2d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 40 | [ ] | GRID (STEAM) | 10 | 20 | 50% (last 20) | Does not open (58%) | 42% | 2d ago | 50% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 41 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 15d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 42 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | n/a | 2d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 43 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | n/a | 16d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 44 | [ ] | Grim Dawn (GOG) | 13 | 20 | 65% (last 20) | Does not open (69%) | 40% | 1d ago | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 45 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | 1d ago | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 46 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 35d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 47 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (70%) | n/a | 14d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 48 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | n/a | 36d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 49 | [ ] | HELLDIVERS™ (STEAM) | 13 | 20 | 65% (last 20) | Does not open (58%) | 40% | today | 53% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 50 | [ ] | Hollow Knight: Silksong (GOG) | 12 | 20 | 60% (last 20) | Does not open (70%) | 50% | today | 46% |  |
| 51 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 34d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 52 | [ ] | Alpha Protocol (STEAM) | 17 | 20 | 85% (last 20) | No graphics (53%) | n/a | 22d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 53 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (59%) | n/a | 2d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 54 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | n/a | 6d ago | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 55 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 58% | today | 35% (drop) | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 56 | [ ] | Dead Space 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 28% | 7d ago | 40% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 57 | [ ] | METAL SLUG 3 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 54% | 4d ago | 71% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 58 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | n/a | 3d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 59 | [ ] | DOOM Eternal (STEAM) | 18 | 20 | 90% (last 20) | Does not open (66%) | n/a | 25d ago | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 60 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (57%) | n/a | 3d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 61 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | n/a | 18d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 62 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 34d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 63 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 20d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 64 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | n/a | 13d ago | n/a |  |
| 65 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 27% | 7d ago | n/a | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 66 | [ ] | Breathedge (STEAM) | 11 | 20 | 55% (last 20) | Does not open (57%) | 55% | 6d ago | 69% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 67 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (92%) | 36% | 1d ago | n/a |  |
| 68 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | n/a | 37d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 69 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 12d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 70 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 34d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 71 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 3d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 72 | [ ] | Borderlands 2 RU (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | n/a | today | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 73 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 8d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 74 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | n/a | 9d ago | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 75 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 20d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 76 | [ ] | Euro Truck Simulator (STEAM) | 20 | 20 | 100% (last 20) | Does not open (88%) | n/a | 1d ago | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 77 | [ ] | Peggle Nights (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 20d ago | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 78 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 45d ago | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 79 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 16d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 80 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | n/a | 25d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 81 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | n/a | 1d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 82 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (54%) | n/a | 22d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 83 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (47%) | n/a | 16d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 84 | [ ] | The Survivalists (STEAM) | 18 | 20 | 90% (last 20) | Does not open (96%) | n/a | 4d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 85 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | n/a | 39d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 86 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | n/a | 34d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 87 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | n/a | 43d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 88 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | n/a | 5d ago | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 89 | [ ] | Metro 2033 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 17% | 13d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 90 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 32d ago | n/a | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 91 | [ ] | Marvel's Spider-Man 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (88%) | n/a | 36d ago | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 92 | [ ] | They Are Billions (STEAM) | 19 | 20 | 95% (last 20) | Does not open (74%) | n/a | 13d ago | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 93 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 59d ago | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 94 | [ ] | Bionic Commando Rearmed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | n/a | 27d ago | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 95 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | n/a | 6d ago | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 96 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | n/a | today | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 97 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 10d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 98 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 6d ago | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 99 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 12d ago | n/a |  |
| 100 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | n/a | 14d ago | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 101 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 5d ago | n/a |  |
| 102 | [ ] | A Plague Tale: Innocence (EPIC) | 11 | 20 | 55% (last 20) | Does not open (70%) | 41% | 3d ago | 21% (drop) |  |
| 103 | [ ] | Alien Breed: Impact (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 22d ago | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 104 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 21d ago | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 105 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 8d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 106 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | n/a | 10d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 107 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 7d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 108 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 12d ago | n/a |  |
| 109 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 55% | 5d ago | n/a | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 110 | [ ] | Crysis® (GOG) | 17 | 20 | 85% (last 20) | Does not open (87%) | n/a | today | n/a |  |
| 111 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | n/a | 5d ago | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 112 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 18d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 113 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 15d ago | n/a |  |
| 114 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (47%) | n/a | 15d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 115 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 5d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 116 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 19d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 117 | [ ] | Drop Duchy (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 8% | today | n/a |  |
| 118 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 12d ago | n/a |  |
| 119 | [ ] | GRADIUS origin collection (STEAM) | 17 | 20 | 85% (last 20) | Controller issues (71%) | n/a | 1d ago | n/a | [#479](https://github.com/GameNative/gamenative-compat/issues/479) |
| 120 | [ ] | King's Bounty: The Legend (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | n/a | 11d ago | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 121 | [ ] | Marvel's Midnight Suns (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | n/a | 34d ago | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 122 | [ ] | PICO PARK:Classic Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 39d ago | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 123 | [ ] | ENDLESS Space™ 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | n/a | 32d ago | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 124 | [ ] | Beholder (EPIC) | 15 | 20 | 75% (last 20) | Does not open (65%) | n/a | 1d ago | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 125 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | n/a | 1d ago | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 126 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | Does not open (42%) | n/a | 7d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 127 | [ ] | Romancing SaGa -Minstrel Song- Remastered (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (100%) | n/a | 1d ago | n/a |  |
| 128 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 13 | 20 | 65% (last 20) | Does not open (52%) | 50% | 1d ago | n/a | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 129 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 54% | 5d ago | n/a |  |
| 130 | [ ] | Mafia II (Classic) (GOG) | 13 | 20 | 65% (last 20) | Does not open (95%) | n/a | 2d ago | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 131 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 50% | 17d ago | 23% (drop) |  |
| 132 | [ ] | Rise of the Tomb Raider: 20 Year Celebration (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 52% | today | 37% |  |
| 133 | [ ] | Re-Volt (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (71%) | n/a | 23d ago | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 134 | [ ] | Fallout Classic (GOG) | 15 | 20 | 75% (last 20) | Does not open (88%) | n/a | 4d ago | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 135 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | 4d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 136 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | n/a | 29d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 137 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (83%) | 24% | 15d ago | 29% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 138 | [ ] | Goose Goose Duck (STEAM) | 13 | 20 | 65% (last 20) | Does not open (70%) | 54% | 2d ago | n/a | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 139 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (45%) | 59% | 3d ago | 40% |  |
| 140 | [ ] | Mortal Shell (EPIC) | 13 | 20 | 65% (last 20) | Does not open (54%) | 49% | today | 21% (drop) |  |
| 141 | [ ] | Sacred Gold (STEAM) | 13 | 20 | 65% (last 20) | Does not open (91%) | n/a | 3d ago | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 142 | [ ] | Chef Knight (STEAM) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 21d ago | n/a |  |
| 143 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | n/a | 7d ago | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 144 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (89%) | n/a | 9d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 145 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 36% | 6d ago | n/a |  |
| 146 | [ ] | Allumeria (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | n/a | 7d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 147 | [ ] | Songs of Conquest (EPIC) | 13 | 20 | 65% (last 20) | Does not open (75%) | n/a | 1d ago | n/a |  |
| 148 | [ ] | Styx: Master of Shadows (EPIC) | 12 | 20 | 60% (last 20) | Does not open (75%) | 35% | 2d ago | 33% |  |
| 149 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 59% | 8d ago | 58% |  |
| 150 | [ ] | Chasm (GOG) | 12 | 20 | 60% (last 20) | No graphics (50%) | n/a | 2d ago | n/a |  |
| 151 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (50%) | n/a | 8d ago | n/a |  |
| 152 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 10 | 20 | 50% (last 20) | No graphics (57%) | 35% | 1d ago | 50% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 153 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 57% | 1d ago | n/a |  |
| 154 | [ ] | Dungeon Keeper™ 2 (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 23d ago | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 155 | [ ] | Beat Cop (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 4d ago | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 156 | [ ] | FINAL FANTASY VII REMAKE INTERGRADE (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 40% | 2d ago | 40% |  |
| 157 | [ ] | Sandustry (STEAM) | 12 | 20 | 60% (last 20) | Does not open (72%) | n/a | 2d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 158 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 12d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 159 | [ ] | Antichamber (STEAM) | 11 | 20 | 55% (last 20) | No graphics (36%) | n/a | 6d ago | n/a |  |
| 160 | [ ] | A Plague Tale: Innocence (GOG) | 11 | 20 | 55% (last 20) | Does not open (91%) | 58% | 24d ago | n/a |  |
| 161 | [ ] | Knights of Pen and Paper 2 (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (44%) | n/a | 8d ago | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 162 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 13 | 20 | 65% (last 20) | No graphics (56%) | n/a | 35d ago | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 163 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | n/a | 39d ago | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 164 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | n/a | 7d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 165 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 11d ago | n/a |  |
| 166 | [ ] | Minit (EPIC) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 9d ago | n/a |  |
| 167 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | 55% | 1d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 168 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 18d ago | n/a |  |
| 169 | [ ] | Mafia: Definitive Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 47% | 3d ago | 42% |  |
| 170 | [ ] | LET IT DIE (STEAM) | 11 | 20 | 55% (last 20) | Does not open (88%) | n/a | 2d ago | n/a |  |
| 171 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | n/a | 5d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 172 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (70%) | 57% | 5d ago | n/a |  |
| 173 | [ ] | Crying Suns (EPIC) | 11 | 20 | 55% (last 20) | No graphics (63%) | n/a | 1d ago | n/a |  |
| 174 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 46% | 5d ago | n/a | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 175 | [ ] | HOT WHEELS UNLEASHED™ (EPIC) | 10 | 20 | 50% (last 20) | No graphics (63%) | 58% | today | 41% |  |
| 176 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (78%) | n/a | 11d ago | n/a |  |
| 177 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (52%) | n/a | 19d ago | n/a | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 178 | [ ] | No More Heroes (STEAM) | 10 | 20 | 50% (last 20) | No graphics (67%) | 41% | 3d ago | 23% |  |
| 179 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 38% | 12d ago | n/a |  |
| 180 | [ ] | Ys: Memories of Celceta (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 45% | 17d ago | n/a |  |
| 181 | [ ] | Railway Chai Wala (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | n/a | 2d ago | n/a |  |
| 182 | [ ] | Turnip Boy Robs a Bank (EPIC) | 11 | 20 | 55% (last 20) | Does not open (67%) | 27% | 3d ago | n/a | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 183 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 57% | 4d ago | n/a |  |
| 184 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | n/a | 11d ago | n/a |  |
| 185 | [ ] | Secret of Mana (STEAM) | 11 | 20 | 55% (last 20) | Graphics glitches (60%) | 55% | today | n/a |  |
| 186 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 10 | 20 | 50% (last 20) | Does not open (84%) | n/a | 82d ago | n/a |  |
| 187 | [ ] | Delver (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 40% | 1d ago | 0% (drop) |  |

## Fix shipped, waiting for ratings (18)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | Plants vs. Zombies: Game of the Year (STEAM) | 2026-11-04 | 9 | 6 | 1d ago | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 2 | L.A. Noire (STEAM) | 2026-11-04 | 4 | 4 | 2d ago | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 3 | Transistor (STEAM) | 2026-11-10 | 2 | 2 | today | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 4 | Max Payne 3 (STEAM) | 2026-11-04 | 3 | 3 | today | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 5 | Red Dead Redemption (STEAM) | 2026-11-04 | 2 | 2 | today | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 6 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 7 | 7 | today | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 7 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 3 | 3 | 6d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 8 | Peggle Deluxe (STEAM) | 2026-10-29 | 1 | 1 | 4d ago | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 9 | Necesse (STEAM) | 2026-10-29 | 6 | 0 | 1d ago | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 10 | Age of Empires II: Definitive Edition (STEAM) | 2026-10-20 | 7 | 3 | 4d ago | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 11 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 1 | 1 | 6d ago | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 12 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 1 | 1 | 13d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 13 | Need for Speed™ (STEAM) | 2026-11-04 | 0 | 0 | 26d ago | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 14 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 0 | 0 | 14d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 15 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 12d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 16 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 0 | 0 | 19d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 17 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 0 | 0 | 13d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 18 | Need for Speed™ Unbound (STEAM) | 2026-11-04 | 0 | 0 | 20d ago | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |

## Works, but the first launch usually fails (310)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 80 | 100 | 80% (14d) | Does not open (63%) | 92% | today | 94% |  |
| 2 | [ ] | Half-Life (STEAM) | 68 | 101 | 67% (14d) | Does not open (59%) | 72% | today | 66% |  |
| 3 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 58 | 79 | 73% (14d) | Does not open (54%) | 80% | today | 81% |  |
| 4 | [ ] | Grand Theft Auto V Legacy (STEAM) | 48 | 58 | 83% (since fix) | Does not open (88%) | 75% | today | 70% |  |
| 5 | [ ] | Cyberpunk 2077 (STEAM) | 47 | 76 | 62% (14d) | Does not open (70%) | 71% | today | 66% |  |
| 6 | [ ] | Road Rash™: 30th Anniversary Edition (STEAM) | 44 | 66 | 67% (14d) | Does not open (74%) | 62% | today | 66% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 7 | [ ] | Buckshot Roulette (STEAM) | 43 | 63 | 68% (14d) | Does not open (63%) | 72% | today | 48% (drop) |  |
| 8 | [ ] | Valheim (STEAM) | 37 | 58 | 64% (since fix) | No graphics (54%) | 85% | today | 82% |  |
| 9 | [ ] | MONSTER HUNTER RISE (STEAM) | 37 | 58 | 64% (14d) | Does not open (84%) | 60% | today | 62% |  |
| 10 | [ ] | No Man's Sky (STEAM) | 33 | 56 | 59% (since fix) | Controller issues (61%) | 79% | today | 75% |  |
| 11 | [ ] | DREDGE (EPIC) | 33 | 37 | 89% (14d) | Does not open (76%) | 62% | today | 48% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 12 | [ ] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 31 | 57 | 54% (14d) | Does not open (64%) | 64% | today | 68% |  |
| 13 | [ ] | Super Meat Boy (STEAM) | 30 | 54 | 56% (14d) | Does not open (59%) | 68% | today | 56% |  |
| 14 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 29 | 38 | 76% (14d) | Does not open (58%) | 71% | today | 59% |  |
| 15 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 29 | 41 | 71% (14d) | Does not open (77%) | 78% | 1d ago | 73% |  |
| 16 | [ ] | ROB RUN (STEAM) | 27 | 34 | 79% (14d) | Does not open (86%) | 61% | today | 63% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 17 | [ ] | Selaco (STEAM) | 25 | 40 | 63% (14d) | Does not open (86%) | 69% | today | 60% |  |
| 18 | [ ] | Red Dead Redemption 2 (STEAM) | 19 | 20 | 95% (since fix) | Does not open (98%) | 81% | today | 83% |  |
| 19 | [ ] | Quake (STEAM) | 20 | 31 | 65% (14d) | Does not open (65%) | 77% | today | 57% (drop) |  |
| 20 | [ ] | ELDEN RING (STEAM) | 19 | 33 | 58% (14d) | Does not open (85%) | 70% | today | 65% |  |
| 21 | [ ] | Baldur's Gate 3 (STEAM) | 19 | 38 | 50% (14d) | Does not open (66%) | 87% | 1d ago | 85% |  |
| 22 | [ ] | BioShock Remastered (EPIC) | 19 | 23 | 83% (14d) | Does not open (67%) | 65% | today | 53% |  |
| 23 | [ ] | Loftia (STEAM) | 17 | 20 | 85% (14d) | Does not open (93%) | 72% | today | 64% |  |
| 24 | [ ] | BeamNG.drive (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | 74% | 1d ago | 55% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 25 | [ ] | Look Outside (STEAM) | 16 | 32 | 50% (14d) | Controller issues (62%) | 90% | today | 89% |  |
| 26 | [ ] | Horizon Chase Turbo (EPIC) | 16 | 28 | 57% (14d) | Does not open (82%) | 66% | 2d ago | 46% (drop) |  |
| 27 | [ ] | Deadlock (STEAM) | 16 | 21 | 76% (14d) | Does not open (54%) | 88% | 2d ago | 86% |  |
| 28 | [ ] | Mortal Kombat X (STEAM) | 16 | 24 | 67% (14d) | Does not open (72%) | 91% | 4d ago | 89% |  |
| 29 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (59%) | 76% | 1d ago | 61% |  |
| 30 | [ ] | DRAGON BALL FighterZ (STEAM) | 27 | 50 | 54% (since fix) | Does not open (89%) | 82% | today | 88% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 31 | [ ] | Resident Evil 4 (2005) (STEAM) | 14 | 25 | 56% (14d) | Does not open (78%) | 71% | 1d ago | 70% |  |
| 32 | [ ] | Clair Obscur: Expedition 33 (STEAM) | 14 | 26 | 54% (14d) | Graphics glitches (40%) | 82% | today | 72% |  |
| 33 | [ ] | Library Of Ruina (STEAM) | 14 | 23 | 61% (14d) | Does not open (68%) | 86% | today | 78% |  |
| 34 | [ ] | Palworld (STEAM) | 13 | 26 | 50% (14d) | Does not open (75%) | 87% | today | 86% |  |
| 35 | [ ] | Noita (STEAM) | 13 | 23 | 57% (14d) | Does not open (56%) | 76% | today | 78% |  |
| 36 | [ ] | TrackMania Nations Forever (STEAM) | 13 | 26 | 50% (14d) | Does not open (54%) | 79% | today | 72% |  |
| 37 | [ ] | Absolute Drift (EPIC) | 12 | 20 | 60% (14d) | No graphics (51%) | 71% | today | 36% (drop) |  |
| 38 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 12 | 21 | 57% (14d) | Does not open (71%) | 64% | 1d ago | 92% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 39 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (88%) | 96% | today | 97% |  |
| 40 | [ ] | Order of the Sinking Star (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 70% | today | 82% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 41 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (71%) | 100% | 2d ago | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 42 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (47%) | 92% | today | 90% |  |
| 43 | [ ] | Alabaster Dawn (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (48%) | 88% | today | 88% |  |
| 44 | [ ] | Devil May Cry 5 (STEAM) | 11 | 22 | 50% (14d) | Does not open (82%) | 79% | 3d ago | 84% |  |
| 45 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 67% | 8d ago | 61% |  |
| 46 | [ ] | Resident Evil 7 Biohazard (STEAM) | 11 | 20 | 55% (last 20) | Does not open (69%) | 77% | today | 72% |  |
| 47 | [ ] | Dead Island Definitive Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (66%) | 84% | 1d ago | 83% |  |
| 48 | [ ] | Dead Island 2 (EPIC) | 17 | 20 | 85% (last 20) | Does not open (84%) | 65% | 2d ago | 46% |  |
| 49 | [ ] | Castlevania Dominus Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (92%) | 97% | 1d ago | 93% |  |
| 50 | [ ] | Batman™: Arkham Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (84%) | 74% | 3d ago | 62% |  |
| 51 | [ ] | Divinity: Original Sin 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (74%) | 86% | 1d ago | 77% |  |
| 52 | [ ] | METAL GEAR SOLID 4: Guns of the Patriots - Master Collection Version (STEAM) | 11 | 20 | 55% (last 20) | Does not open (80%) | 89% | 5d ago | 91% |  |
| 53 | [ ] | Sekiro™: Shadows Die Twice (STEAM) | 10 | 20 | 50% (14d) | Graphics glitches (48%) | 75% | 1d ago | 85% |  |
| 54 | [ ] | DOOM 3: BFG Edition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (72%) | 70% | today | 63% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 55 | [ ] | Disgaea 5 Complete (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | 91% | today | 94% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 56 | [ ] | Grand Theft Auto V (EPIC) | 18 | 20 | 90% (last 20) | Does not open (89%) | 81% | today | 76% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 57 | [ ] | Dead Space (STEAM) | 17 | 20 | 85% (last 20) | Does not open (58%) | 84% | 2d ago | 81% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 58 | [ ] | Geometry Wars: Retro Evolved (STEAM) | 11 | 20 | 55% (last 20) | Does not open (94%) | 66% | today | 53% |  |
| 59 | [ ] | eFootball™ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (65%) | 65% | 2d ago | 51% |  |
| 60 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 65% | 1d ago | 52% |  |
| 61 | [ ] | LEGO® MARVEL Super Heroes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (66%) | 80% | today | 85% |  |
| 62 | [ ] | Cyberpunk 2077 (GOG) | 12 | 20 | 60% (last 20) | Does not open (71%) | 72% | 2d ago | 60% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 63 | [ ] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 11 | 20 | 55% (last 20) | Does not open (61%) | 74% | today | 84% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 64 | [ ] | Prey (STEAM) | 10 | 20 | 50% (last 20) | Does not open (58%) | 76% | today | 79% |  |
| 65 | [ ] | Fallout: New Vegas (EPIC) | 15 | 20 | 75% (last 20) | Does not open (59%) | 84% | 6d ago | 76% |  |
| 66 | [ ] | Mini Motorways (STEAM) | 14 | 20 | 70% (last 20) | Does not open (74%) | 70% | today | 67% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 67 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (79%) | 95% | 4d ago | 95% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 68 | [ ] | Aniimo (STEAM) | 17 | 20 | 85% (last 20) | Does not open (74%) | 84% | 1d ago | 76% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 69 | [ ] | OMORI (STEAM) | 14 | 20 | 70% (last 20) | Does not open (62%) | 70% | today | 52% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 70 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | 71% | today | 71% |  |
| 71 | [ ] | Cry of Fear (STEAM) | 12 | 20 | 60% (last 20) | Does not open (48%) | 73% | today | 74% |  |
| 72 | [ ] | Poppy Playtime (STEAM) | 13 | 20 | 65% (last 20) | Does not open (59%) | 70% | 2d ago | 63% |  |
| 73 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 16 | 20 | 80% (last 20) | Graphics glitches (46%) | 85% | 1d ago | 82% |  |
| 74 | [ ] | Deskrawl: Idle ARPG (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 91% | 6d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 75 | [ ] | Digimon Story Cyber Sleuth: Complete Edition (STEAM) | 10 | 20 | 50% (last 20) | No graphics (49%) | 82% | today | 89% |  |
| 76 | [ ] | The Forest (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | 84% | today | 82% |  |
| 77 | [ ] | Don't Starve Together (STEAM) | 10 | 20 | 50% (last 20) | Does not open (58%) | 74% | today | 65% |  |
| 78 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Does not open (61%) | 90% | today | 81% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 79 | [ ] | Dota 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (76%) | 76% | today | 89% |  |
| 80 | [ ] | River City Girls (EPIC) | 14 | 20 | 70% (last 20) | No graphics (48%) | 68% | 1d ago | 43% (drop) |  |
| 81 | [ ] | Castlevania Anniversary Collection (EPIC) | 12 | 20 | 60% (last 20) | Does not open (71%) | 68% | 2d ago | 34% (drop) |  |
| 82 | [ ] | Call of Duty 4: Modern Warfare (2007) (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (52%) | 79% | today | 63% |  |
| 83 | [ ] | Darksiders Warmastered Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 70% | today | 53% |  |
| 84 | [ ] | Fate/stay night REMASTERED (STEAM) | 12 | 20 | 60% (last 20) | No graphics (48%) | 91% | 2d ago | 79% |  |
| 85 | [ ] | Disco Elysium - The Final Cut (EPIC) | 11 | 20 | 55% (last 20) | Does not open (71%) | 97% | today | 97% |  |
| 86 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (82%) | 71% | 8d ago | 47% (drop) |  |
| 87 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 15 | 20 | 75% (last 20) | Does not open (42%) | 71% | today | 65% |  |
| 88 | [ ] | ZERO Sievert (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 89% | today | 76% |  |
| 89 | [ ] | Need for Speed™ Rivals (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 83% | today | 92% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 90 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (52%) | 69% | 3d ago | 38% (drop) | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 91 | [ ] | Welcome to Elderfield (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 71% | 1d ago | 70% |  |
| 92 | [ ] | Need for Speed: Hot Pursuit (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 76% | 3d ago | 80% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 93 | [ ] | Ratatan (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 94% | 4d ago | 92% |  |
| 94 | [ ] | MIO: Memories in Orbit (STEAM) | 11 | 20 | 55% (last 20) | Graphics glitches (50%) | 95% | 1d ago | 96% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 95 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 66% | today | 70% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 96 | [ ] | Happy Wheels (STEAM) | 19 | 20 | 95% (last 20) | No graphics (52%) | 70% | 10d ago | 50% (drop) | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 97 | [ ] | Sid Meier's Civilization VI (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 82% | 1d ago | 70% |  |
| 98 | [ ] | Fable - The Lost Chapters (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (48%) | 83% | 1d ago | 85% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 99 | [ ] | Coromon (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 89% | today | 83% |  |
| 100 | [ ] | Cave Story+ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | 81% | 1d ago | 71% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 101 | [ ] | Rune Factory 3 Special (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 93% | 1d ago | n/a |  |
| 102 | [ ] | American Truck Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (69%) | 76% | 3d ago | 70% |  |
| 103 | [ ] | STAR WARS™ Knights of the Old Republic™ II: The Sith Lords™ (STEAM) | 11 | 20 | 55% (last 20) | No graphics (65%) | 69% | 1d ago | 39% (drop) |  |
| 104 | [ ] | Quake II (STEAM) | 10 | 20 | 50% (last 20) | No graphics (48%) | 89% | 1d ago | 83% |  |
| 105 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (80%) | 79% | 1d ago | n/a | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 106 | [ ] | Resident Evil Village (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 90% | 5d ago | 83% |  |
| 107 | [ ] | The Binding of Isaac (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (92%) | 93% | today | 93% |  |
| 108 | [ ] | Abiotic Factor (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | 74% | today | 80% |  |
| 109 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 96% | today | 88% |  |
| 110 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 68% | 1d ago | 50% |  |
| 111 | [ ] | Palia (STEAM) | 15 | 20 | 75% (last 20) | Does not open (59%) | 76% | today | 67% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 112 | [ ] | Until Then (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 78% | 3d ago | 59% |  |
| 113 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (61%) | 95% | 1d ago | 97% |  |
| 114 | [ ] | PlateUp! (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 80% | today | 68% |  |
| 115 | [ ] | Sid Meier's Civilization V (STEAM) | 15 | 20 | 75% (last 20) | Does not open (75%) | 64% | 1d ago | 61% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 116 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 68% | 10d ago | 70% |  |
| 117 | [ ] | Minecraft Dungeons (STEAM) | 10 | 20 | 50% (last 20) | Does not open (79%) | 81% | 1d ago | 80% |  |
| 118 | [ ] | A Plague Tale: Innocence (STEAM) | 19 | 20 | 95% (last 20) | Does not open (88%) | 76% | 1d ago | 79% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 119 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (83%) | 79% | 2d ago | 67% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 120 | [ ] | Moonstone Island (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (60%) | 74% | 1d ago | 68% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 121 | [ ] | Minecraft Dungeons II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (82%) | 69% | 4d ago | 73% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 122 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (52%) | 70% | 1d ago | 79% |  |
| 123 | [ ] | TBH: Task Bar Hero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 82% | 5d ago | 80% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 124 | [ ] | Overwatch® (STEAM) | 18 | 20 | 90% (last 20) | Does not open (57%) | 71% | today | n/a | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 125 | [ ] | Yakuza: Like a Dragon (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 62% | 9d ago | 71% |  |
| 126 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | 69% | 8d ago | 80% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 127 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 18 | 20 | 90% (last 20) | Does not open (58%) | 80% | 3d ago | n/a | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 128 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (76%) | 90% | 2d ago | n/a | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 129 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 12 | 20 | 60% (last 20) | Does not open (43%) | 68% | 1d ago | 68% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 130 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 78% | today | 78% |  |
| 131 | [ ] | Tails of Iron (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 86% | 2d ago | 82% |  |
| 132 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 60% | 15d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 133 | [ ] | Sonic Generations (STEAM) | 16 | 20 | 80% (last 20) | Does not open (70%) | 69% | 9d ago | 70% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 134 | [ ] | Astral Party  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 80% | 2d ago | n/a |  |
| 135 | [ ] | Pinball FX (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 70% | today | 67% |  |
| 136 | [ ] | Grand Theft Auto: Vice City (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 84% | today | 81% |  |
| 137 | [ ] | Plague Inc: Evolved (STEAM) | 14 | 20 | 70% (last 20) | Does not open (68%) | 61% | 7d ago | 65% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 138 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 95% | 18d ago | n/a |  |
| 139 | [ ] | Fallout (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 67% | 6d ago | 64% |  |
| 140 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (50%) | 78% | 2d ago | 72% |  |
| 141 | [ ] | Heavy Rain (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 94% | 2d ago | 94% |  |
| 142 | [ ] | Driving Rogue (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 89% | 10d ago | 84% |  |
| 143 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 77% | 6d ago | 79% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 144 | [ ] | Call of Duty: World at War (STEAM) | 13 | 20 | 65% (last 20) | Does not open (45%) | 88% | 1d ago | 71% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 145 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 88% | 4d ago | 88% |  |
| 146 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 88% | 1d ago | n/a | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 147 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (84%) | 88% | 5d ago | n/a | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 148 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (88%) | 94% | today | 95% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 149 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (46%) | 91% | 7d ago | 86% |  |
| 150 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | 64% | 1d ago | 56% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 151 | [ ] | Oxygen Not Included (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 62% | 2d ago | 77% |  |
| 152 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 82% | 5d ago | 79% |  |
| 153 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | 73% | 4d ago | n/a | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 154 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (80%) | 80% | 15d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 155 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | 84% | today | 82% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 156 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 76% | 10d ago | 80% |  |
| 157 | [ ] | Max Payne (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (46%) | 85% | 3d ago | 75% |  |
| 158 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 83% | 4d ago | 76% |  |
| 159 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (62%) | 92% | 12d ago | n/a | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 160 | [ ] | Gambonanza (STEAM) | 13 | 20 | 65% (last 20) | Does not open (60%) | 95% | today | 94% |  |
| 161 | [ ] | Gothic 1 Classic (STEAM) | 12 | 20 | 60% (last 20) | Does not open (61%) | 77% | 8d ago | 59% |  |
| 162 | [ ] | Street Fighter™ 6 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (81%) | 84% | 5d ago | 83% |  |
| 163 | [ ] | ABZU (EPIC) | 10 | 20 | 50% (last 20) | Does not open (86%) | 88% | today | 82% |  |
| 164 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 64% | 3d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 165 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 63% | 8d ago | n/a | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 166 | [ ] | Tabletop Simulator (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 76% | 3d ago | 82% |  |
| 167 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 14 | 20 | 70% (last 20) | Does not open (44%) | 60% | 2d ago | 64% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 168 | [ ] | Dishonored 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (90%) | 79% | today | 65% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 169 | [ ] | Limbus Company (STEAM) | 12 | 20 | 60% (last 20) | Does not open (86%) | 83% | 1d ago | 90% |  |
| 170 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (54%) | 73% | 1d ago | 80% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 171 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (64%) | 61% | 6d ago | n/a | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 172 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 79% | 8d ago | 89% |  |
| 173 | [ ] | Stellar Blade™ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (43%) | 79% | today | 80% |  |
| 174 | [ ] | Control Ultimate Edition (GOG) | 13 | 20 | 65% (last 20) | Does not open (76%) | 83% | 6d ago | 75% |  |
| 175 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 11 | 20 | 55% (last 20) | Does not open (62%) | 73% | 14d ago | 76% |  |
| 176 | [ ] | Trailmakers (STEAM) | 11 | 20 | 55% (last 20) | Does not open (44%) | 93% | 1d ago | 93% |  |
| 177 | [ ] | Sonic Lost World (STEAM) | 10 | 20 | 50% (last 20) | No graphics (67%) | 82% | today | 84% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 178 | [ ] | Stumble Guys (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 71% | 2d ago | 62% |  |
| 179 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (59%) | 91% | 12d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 180 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | 67% | 9d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 181 | [ ] | Unturned (STEAM) | 12 | 20 | 60% (last 20) | Does not open (44%) | 71% | 6d ago | 81% |  |
| 182 | [ ] | Mortal Kombat 11 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 80% | 3d ago | 87% |  |
| 183 | [ ] | BioShock 2 Remastered (STEAM) | 11 | 20 | 55% (last 20) | Does not open (79%) | 86% | 1d ago | 86% |  |
| 184 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (70%) | 71% | 9d ago | 73% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 185 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (83%) | 93% | today | 92% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 186 | [ ] | State of Decay: Year-One (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 78% | 3d ago | 77% |  |
| 187 | [ ] | Counter-Strike:Global Offensive (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 74% | 1d ago | 73% |  |
| 188 | [ ] | Raft (STEAM) | 10 | 20 | 50% (last 20) | Does not open (83%) | 90% | 1d ago | 83% |  |
| 189 | [ ] | Capcom Arcade Stadium (STEAM) | 15 | 20 | 75% (last 20) | Does not open (82%) | 73% | 4d ago | 82% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 190 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 90% | 27d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 191 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 87% | 5d ago | 87% |  |
| 192 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 92% | 7d ago | n/a |  |
| 193 | [ ] | One-armed robber (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (65%) | 65% | 9d ago | 50% |  |
| 194 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (85%) | 89% | 17d ago | 83% |  |
| 195 | [ ] | Subnautica 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (55%) | 71% | 6d ago | n/a | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 196 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 85% | 6d ago | n/a | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 197 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (75%) | 84% | today | 70% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 198 | [ ] | Digimon Survive (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (77%) | 86% | 5d ago | 77% |  |
| 199 | [ ] | Escape from Duckov (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (71%) | 94% | 4d ago | 97% |  |
| 200 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (56%) | 64% | 11d ago | 69% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 201 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (69%) | 83% | 22d ago | n/a | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 202 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 20 | 80% (last 20) | Does not open (47%) | 62% | 3d ago | 31% (drop) | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 203 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (59%) | 68% | 7d ago | 57% |  |
| 204 | [ ] | My Summer Car (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | 81% | 3d ago | 85% |  |
| 205 | [ ] | Resident Evil Revelations 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (45%) | 83% | today | 81% |  |
| 206 | [ ] | The Witcher: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 65% | 10d ago | 79% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 207 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 95% | 6d ago | 92% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 208 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 81% | 11d ago | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 209 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (65%) | 100% | 12d ago | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 210 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (51%) | 67% | 20d ago | n/a | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 211 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 65% | 6d ago | 75% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 212 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 96% | 2d ago | 100% |  |
| 213 | [ ] | TurretGirls (STEAM) | 11 | 20 | 55% (last 20) | No graphics (75%) | 88% | 2d ago | 87% |  |
| 214 | [ ] | Moonring (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 87% | 4d ago | 80% |  |
| 215 | [ ] | Battle Brothers (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 82% | 4d ago | 78% |  |
| 216 | [ ] | Jade Empire: Special Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 71% | 1d ago | n/a | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 217 | [ ] | Undisputed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 69% | 9d ago | n/a | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 218 | [ ] | GOD EATER RESURRECTION (STEAM) | 14 | 20 | 70% (last 20) | Does not open (59%) | 78% | 3d ago | n/a |  |
| 219 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 82% | 5d ago | n/a | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 220 | [ ] | Darksiders (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 83% | 1d ago | 83% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 221 | [ ] | Lucid Blocks (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 63% | 1d ago | 59% |  |
| 222 | [ ] | Warframe (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 83% | today | 77% |  |
| 223 | [ ] | Goat Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 72% | 1d ago | 73% |  |
| 224 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 81% | 5d ago | 80% |  |
| 225 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 64% | 5d ago | 50% |  |
| 226 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (91%) | 81% | 30d ago | n/a |  |
| 227 | [ ] | Invisible, Inc. (STEAM) | 15 | 20 | 75% (last 20) | Does not open (63%) | 80% | 18d ago | n/a |  |
| 228 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 71% | 20d ago | 60% |  |
| 229 | [ ] | Return to Monkey Island (STEAM) | 14 | 20 | 70% (last 20) | No graphics (65%) | 70% | 10d ago | 64% |  |
| 230 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (42%) | 71% | 12d ago | n/a | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 231 | [ ] | SnowRunner (STEAM) | 13 | 20 | 65% (last 20) | Does not open (96%) | 81% | 8d ago | 67% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 232 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (44%) | 83% | 1d ago | n/a |  |
| 233 | [ ] | Zero Escape: The Nonary Games (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 63% | 7d ago | 66% |  |
| 234 | [ ] | MX Bikes (STEAM) | 11 | 20 | 55% (last 20) | Does not open (62%) | 93% | 1d ago | 93% |  |
| 235 | [ ] | GUILTY GEAR Xrd REV 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (86%) | 83% | 2d ago | 65% |  |
| 236 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 93% | 7d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 237 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (83%) | 76% | today | 75% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 238 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 11 | 20 | 55% (last 20) | Does not open (53%) | 65% | today | 74% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 239 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 90% | 2d ago | 93% |  |
| 240 | [ ] | Dying Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (87%) | 69% | 1d ago | 53% |  |
| 241 | [ ] | STORY OF SEASONS: Friends of Mineral Town (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 90% | 1d ago | 100% |  |
| 242 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Controller issues (38%) | 93% | today | n/a |  |
| 243 | [ ] | Revolution Idle (STEAM) | 10 | 20 | 50% (last 20) | Does not open (43%) | 77% | today | n/a |  |
| 244 | [ ] | Bongo Cat (STEAM) | 15 | 20 | 75% (last 20) | Does not open (92%) | 62% | 11d ago | 36% (drop) | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 245 | [ ] | Cat Mail Co. (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 83% | 3d ago | 82% |  |
| 246 | [ ] | BATTLETECH (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 95% | 1d ago | 92% |  |
| 247 | [ ] | Deus Ex™ GOTY Edition (GOG) | 12 | 20 | 60% (last 20) | No graphics (44%) | 92% | 17d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 248 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 67% | 8d ago | 64% |  |
| 249 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 100% | 9d ago | n/a |  |
| 250 | [ ] | Hero Siege (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (52%) | 84% | 1d ago | 94% |  |
| 251 | [ ] | Tales of Zestiria (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 69% | 22d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 252 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (95%) | 95% | 8d ago | 91% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 253 | [ ] | AER Memories of Old (EPIC) | 13 | 20 | 65% (last 20) | Does not open (86%) | 100% | 1d ago | n/a |  |
| 254 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (71%) | 74% | 2d ago | 70% |  |
| 255 | [ ] | PAYDAY: The Heist (STEAM) | 13 | 20 | 65% (last 20) | Does not open (75%) | 73% | 10d ago | n/a |  |
| 256 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (100%) | 75% | 2d ago | n/a |  |
| 257 | [ ] | 12 is Better Than 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 83% | 12d ago | n/a |  |
| 258 | [ ] | Big Walk (STEAM) | 11 | 20 | 55% (last 20) | Does not open (65%) | 66% | 14d ago | 43% (drop) |  |
| 259 | [ ] | Hitman: Absolution (GOG) | 11 | 20 | 55% (last 20) | Does not open (85%) | 75% | 2d ago | n/a |  |
| 260 | [ ] | No Socks RPG (STEAM) | 11 | 20 | 55% (last 20) | Graphics glitches (91%) | 93% | today | 91% |  |
| 261 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (78%) | 97% | today | 100% |  |
| 262 | [ ] | Secrets of Grindea (STEAM) | 10 | 20 | 50% (last 20) | Does not open (45%) | 74% | 1d ago | 79% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 263 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 80% | 3d ago | 77% |  |
| 264 | [ ] | Capcom Fighting Collection (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 87% | 8d ago | n/a | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 265 | [ ] | Ghostwire Tokyo (EPIC) | 14 | 20 | 70% (last 20) | Does not open (91%) | 61% | 2d ago | 42% |  |
| 266 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 14 | 20 | 70% (last 20) | Does not open (85%) | 82% | 9d ago | n/a | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 267 | [ ] | Disgaea 4 Complete+ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (43%) | 92% | 2d ago | n/a | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 268 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 90% | 28d ago | 90% |  |
| 269 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 12 | 20 | 60% (last 20) | No graphics (37%) | 82% | today | n/a | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 270 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 63% | 11d ago | 67% |  |
| 271 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 62% | 4d ago | 54% |  |
| 272 | [ ] | Sons Of The Forest (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 76% | 2d ago | 71% |  |
| 273 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 12 | 20 | 60% (last 20) | Does not open (90%) | 62% | 8d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 274 | [ ] | Hylics (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 94% | 1d ago | 92% |  |
| 275 | [ ] | Hatred (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 88% | 9d ago | 93% |  |
| 276 | [ ] | Football Manager 2024 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (91%) | 62% | 9d ago | 39% (drop) |  |
| 277 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 93% | 5d ago | 88% |  |
| 278 | [ ] | Spark the Electric Jester (STEAM) | 14 | 20 | 70% (last 20) | Does not open (58%) | 69% | 12d ago | n/a | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 279 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 79% | 7d ago | n/a |  |
| 280 | [ ] | Timberborn (STEAM) | 12 | 20 | 60% (last 20) | No graphics (62%) | 95% | 1d ago | n/a |  |
| 281 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (50%) | 75% | 9d ago | 90% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 282 | [ ] | Assassin's Creed Odyssey (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 60% | today | 56% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 283 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 73% | today | n/a |  |
| 284 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 85% | 7d ago | 70% |  |
| 285 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 74% | 8d ago | 69% |  |
| 286 | [ ] | CRUEL (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 82% | 2d ago | 77% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 287 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 90% | 2d ago | 100% |  |
| 288 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (44%) | 67% | 45d ago | n/a |  |
| 289 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 78% | 3d ago | 91% |  |
| 290 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (92%) | 89% | 12d ago | n/a |  |
| 291 | [ ] | Forgive Me Father (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 67% | 3d ago | n/a |  |
| 292 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | Does not open (52%) | 71% | 2d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 293 | [ ] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (45%) | 66% | 2d ago | 50% |  |
| 294 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 69% | 1d ago | n/a |  |
| 295 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 62% | today | n/a | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 296 | [ ] | Intravenous (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 78% | 8d ago | 77% |  |
| 297 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | 90% | 3d ago | n/a |  |
| 298 | [ ] | The Stanley Parable (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 86% | 3d ago | n/a |  |
| 299 | [ ] | SILENT HILL 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (58%) | 78% | 2d ago | 91% |  |
| 300 | [ ] | The Outer Worlds (EPIC) | 12 | 20 | 60% (last 20) | Does not open (100%) | 92% | 1d ago | n/a |  |
| 301 | [ ] | Subnautica: Below Zero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 75% | 8d ago | 67% |  |
| 302 | [ ] | Cruelty Squad (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 84% | today | 77% |  |
| 303 | [ ] | Chroma Squad (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (75%) | 100% | today | n/a |  |
| 304 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 69% | 10d ago | 69% |  |
| 305 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 73% | 10d ago | n/a |  |
| 306 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 91% | 7d ago | 93% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 307 | [ ] | Legend of Grimrock 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 92% | today | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 308 | [ ] | Decktamer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 82% | 2d ago | n/a |  |
| 309 | [ ] | Haydee (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 87% | 2d ago | n/a |  |
| 310 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 92% | 2d ago | 93% |  |

## Recently recovered (418)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Grim Dawn (STEAM) | 503 | 2026-11-08 | 570 | 66% |  |
| 2 | [x] | FINAL FANTASY RESONANCE (STEAM) | 433 | 2026-10-24 | 991 | 80% |  |
| 3 | [x] | Half-Life (STEAM) | 371 | 2026-11-09 | 643 | 72% |  |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 260 | 2026-11-14 | 410 | 64% |  |
| 5 | [x] | Alan Wake (STEAM) | 239 | 2026-11-14 | 262 | 46% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 6 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 232 | 2026-11-09 | 325 | 90% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 7 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 221 | 2026-10-19 | 283 | 67% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 8 | [x] | MONSTER HUNTER RISE (STEAM) | 219 | 2026-11-17 | 521 | 60% |  |
| 9 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 210 | 2026-11-09 | 253 | 61% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 10 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 204 | 2026-11-09 | 357 | 71% |  |
| 11 | [x] | BeamNG.drive (STEAM) | 201 | 2026-11-09 | 242 | 74% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 12 | [x] | Call of Duty: Black Ops (STEAM) | 196 | 2026-11-13 | 221 | 23% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 13 | [x] | Devil May Cry HD Collection (STEAM) | 192 | 2026-10-19 | 282 | 80% |  |
| 14 | [x] | OMORI (STEAM) | 186 | 2026-11-09 | 229 | 70% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 15 | [x] | DRAGON BALL FighterZ (STEAM) | 175 | 2026-11-01 | 218 | 82% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 16 | [x] | DREDGE (EPIC) | 174 | 2026-11-09 | 216 | 62% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 17 | [x] | Spelunky 2 (STEAM) | 165 | 2026-11-01 | 200 | 76% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 18 | [x] | Sid Meier's Civilization V (STEAM) | 151 | 2026-11-10 | 163 | 64% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 19 | [x] | BioShock (STEAM) | 150 | 2026-11-09 | 300 | 72% |  |
| 20 | [x] | Geometry Dash (STEAM) | 149 | 2026-11-11 | 441 | 55% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 21 | [x] | Prototype (STEAM) | 140 | 2026-11-11 | 205 | 58% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 22 | [x] | Team Fortress 2 (STEAM) | 136 | 2026-11-09 | 235 | 74% |  |
| 23 | [x] | Castlevania Advance Collection (STEAM) | 129 | 2026-11-09 | 203 | 87% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 24 | [x] | Minecraft Dungeons II (STEAM) | 129 | 2026-11-09 | 148 | 69% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 25 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 124 | 2026-10-18 | 182 | 78% |  |
| 26 | [x] | Counter-Strike (STEAM) | 123 | 2026-11-11 | 204 | 40% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 27 | [x] | Call of Duty: Black Ops III (STEAM) | 122 | 2026-10-18 | 250 | 80% |  |
| 28 | [x] | Mirror's Edge (STEAM) | 118 | 2026-11-09 | 171 | 69% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 29 | [x] | Assassin's Creed II (STEAM) | 116 | 2026-11-10 | 121 | 66% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 30 | [x] | Aniimo (STEAM) | 113 | 2026-11-09 | 152 | 84% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 31 | [x] | The Witcher: Enhanced Edition (STEAM) | 106 | 2026-11-09 | 124 | 65% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 32 | [x] | Cave Story+ (STEAM) | 104 | 2026-11-09 | 115 | 81% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 33 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 103 | 2026-11-09 | 143 | 93% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 34 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 101 | 2026-11-15 | 140 | 64% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 35 | [x] | Moonstone Island (STEAM) | 100 | 2026-11-09 | 129 | 74% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 36 | [x] | Happy Wheels (STEAM) | 97 | 2026-11-09 | 117 | 70% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 37 | [x] | Catherine Classic (STEAM) | 87 | 2026-11-09 | 165 | 62% |  |
| 38 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 87 | 2026-11-09 | 141 | 65% |  |
| 39 | [x] | Caravan SandWitch (EPIC) | 86 | 2026-11-09 | 149 | 71% |  |
| 40 | [x] | Quake (STEAM) | 85 | 2026-11-09 | 246 | 77% |  |
| 41 | [x] | Cry of Fear (STEAM) | 85 | 2026-10-18 | 167 | 73% |  |
| 42 | [x] | DOOM 3: BFG Edition (STEAM) | 85 | 2026-11-09 | 125 | 70% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 43 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 84 | 2026-11-09 | 111 | 94% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 44 | [x] | Hi-Fi RUSH (STEAM) | 82 | 2026-11-11 | 114 | 42% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 45 | [x] | Vital Shell (STEAM) | 80 | 2026-11-09 | 129 | 84% |  |
| 46 | [x] | FINAL FANTASY XIII-2 (STEAM) | 80 | 2026-11-09 | 83 | 63% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 47 | [x] | Age of Empires II: Definitive Edition (STEAM) | 79 | 2026-11-10 | 95 | 56% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 48 | [x] | Psychonauts (STEAM) | 77 | 2026-11-09 | 143 | 94% |  |
| 49 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 77 | 2026-10-18 | 129 | 95% |  |
| 50 | [x] | STEINS;GATE (STEAM) | 76 | 2026-11-09 | 110 | 88% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 51 | [x] | Brawlhalla (STEAM) | 73 | 2026-11-09 | 145 | 73% |  |
| 52 | [x] | Ballionaire (STEAM) | 73 | 2026-11-09 | 122 | 80% |  |
| 53 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 73 | 2026-11-09 | 113 | 84% |  |
| 54 | [x] | The Sims™ 4 (STEAM) | 71 | 2026-11-09 | 93 | 74% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 55 | [x] | Cyberpunk 2077 (GOG) | 70 | 2026-11-09 | 92 | 72% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 56 | [x] | Dota 2 (STEAM) | 69 | 2026-11-09 | 103 | 76% |  |
| 57 | [x] | Disgaea 5 Complete (STEAM) | 69 | 2026-11-09 | 81 | 91% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 58 | [x] | Spyro™ Reignited Trilogy (STEAM) | 68 | 2026-11-09 | 109 | 78% |  |
| 59 | [x] | Bayonetta (STEAM) | 67 | 2026-10-18 | 208 | 85% |  |
| 60 | [x] | MIO: Memories in Orbit (STEAM) | 66 | 2026-11-09 | 123 | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 61 | [x] | Fable - The Lost Chapters (STEAM) | 66 | 2026-11-09 | 106 | 83% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 62 | [x] | Stardew Valley (GOG) | 65 | 2026-11-11 | 115 | 70% |  |
| 63 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 65 | 2026-11-09 | 102 | 84% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 64 | [x] | Need for Speed: Hot Pursuit (STEAM) | 65 | 2026-11-09 | 100 | 76% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 65 | [x] | Order of the Sinking Star (STEAM) | 65 | 2026-11-09 | 96 | 70% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 66 | [x] | American Truck Simulator (STEAM) | 64 | 2026-11-09 | 107 | 76% |  |
| 67 | [x] | Diablo® IV (STEAM) | 63 | 2026-11-11 | 75 | 69% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 68 | [x] | Sovereign Tower (STEAM) | 62 | 2026-11-09 | 116 | 72% |  |
| 69 | [x] | Fallout (STEAM) | 62 | 2026-11-09 | 96 | 67% |  |
| 70 | [x] | Poppy Playtime (STEAM) | 61 | 2026-11-09 | 104 | 70% |  |
| 71 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 61 | 2026-11-11 | 79 | 55% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 72 | [x] | Firewatch (STEAM) | 60 | 2026-11-10 | 117 | 75% |  |
| 73 | [x] | Borderlands 3 (STEAM) | 60 | 2026-11-09 | 87 | 90% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 74 | [x] | Borderlands: The Pre-Sequel (STEAM) | 59 | 2026-11-09 | 96 | 63% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 75 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 59 | 2026-11-09 | 84 | 69% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 76 | [x] | Gunfire Reborn (STEAM) | 59 | 2026-11-09 | 65 | 88% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 77 | [x] | A Plague Tale: Innocence (STEAM) | 59 | 2026-11-09 | 62 | 76% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 78 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 58 | 2026-10-25 | 108 | 74% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 79 | [x] | Mini Motorways (STEAM) | 58 | 2026-11-09 | 97 | 70% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 80 | [x] | Deskrawl: Idle ARPG (STEAM) | 58 | 2026-11-09 | 72 | 91% | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 81 | [x] | eFootball™ (STEAM) | 56 | 2026-11-09 | 83 | 65% |  |
| 82 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 56 | 2026-11-17 | 80 | 60% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 83 | [x] | Call of Juarez Gunslinger (STEAM) | 56 | 2026-11-09 | 71 | 77% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 84 | [x] | Starbound (STEAM) | 55 | 2026-11-09 | 88 | 80% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 85 | [x] | Call of Duty: World at War (STEAM) | 55 | 2026-11-09 | 79 | 88% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 86 | [x] | Darksiders (STEAM) | 55 | 2026-11-09 | 70 | 83% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 87 | [x] | Grand Theft Auto V (EPIC) | 54 | 2026-11-09 | 61 | 81% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 88 | [x] | Sonic Generations (STEAM) | 54 | 2026-11-09 | 59 | 69% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 89 | [x] | Overwatch® (STEAM) | 53 | 2026-11-10 | 57 | 71% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 90 | [x] | TBH: Task Bar Hero (STEAM) | 52 | 2026-11-09 | 85 | 82% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 91 | [x] | Dead Space (STEAM) | 52 | 2026-10-18 | 65 | 84% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 92 | [x] | Sol Cesto (EPIC) | 52 | 2026-11-09 | 53 | 79% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 93 | [x] | Okami HD (STEAM) | 50 | 2026-11-09 | 92 | 91% |  |
| 94 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 50 | 2026-11-09 | 84 | 76% |  |
| 95 | [x] | Last Epoch (STEAM) | 50 | 2026-11-09 | 75 | 75% |  |
| 96 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 49 | 2026-11-09 | 83 | 88% |  |
| 97 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 48 | 2026-11-09 | 83 | 61% |  |
| 98 | [x] | Heroes of Might & Magic III - HD Edition (STEAM) | 48 | 2026-11-14 | 63 | 64% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 99 | [x] | Abiotic Factor (STEAM) | 47 | 2026-10-18 | 85 | 74% |  |
| 100 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 47 | 2026-11-09 | 77 | 83% |  |
| 101 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 47 | 2026-11-09 | 54 | 90% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 102 | [x] | Moonlighter (EPIC) | 47 | 2026-11-09 | 51 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 103 | [x] | Oxygen Not Included (STEAM) | 46 | 2026-11-11 | 79 | 62% |  |
| 104 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 46 | 2026-11-09 | 77 | 50% |  |
| 105 | [x] | MudRunner (STEAM) | 45 | 2026-10-24 | 99 | 63% |  |
| 106 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 45 | 2026-10-19 | 89 | 71% |  |
| 107 | [x] | Darkest Dungeon® (EPIC) | 45 | 2026-11-09 | 86 | 80% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 108 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 44 | 2026-11-09 | 69 | 91% |  |
| 109 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 44 | 2026-11-13 | 66 | 62% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 110 | [x] | Big Walk (STEAM) | 43 | 2026-11-09 | 67 | 66% |  |
| 111 | [x] | Plague Inc: Evolved (STEAM) | 43 | 2026-11-16 | 63 | 61% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 112 | [x] | Sheepy: A Short Adventure (STEAM) | 42 | 2026-11-09 | 50 | 67% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 113 | [x] | Tomb Raider: Anniversary (STEAM) | 40 | 2026-11-09 | 63 | 59% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 114 | [x] | Aggelos (STEAM) | 40 | 2026-11-09 | 55 | 88% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 115 | [x] | Dead by Daylight (STEAM) | 40 | 2026-11-09 | 44 | 84% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 116 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 39 | 2026-11-09 | 71 | 88% |  |
| 117 | [x] | Ace Attorney Investigations Collection (STEAM) | 39 | 2026-11-09 | 69 | 86% |  |
| 118 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 39 | 2026-11-09 | 60 | 71% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 119 | [x] | Sonic Lost World (STEAM) | 39 | 2026-11-09 | 59 | 82% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 120 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-11-09 | 40 | 73% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 121 | [x] | Digimon World: Next Order (STEAM) | 38 | 2026-11-09 | 75 | 85% |  |
| 122 | [x] | Age of Empires II (2013) (STEAM) | 38 | 2026-11-09 | 63 | 70% |  |
| 123 | [x] | FINAL FANTASY VII (2013) (STEAM) | 38 | 2026-11-09 | 55 | 57% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 124 | [x] | PROTOTYPE 2 (STEAM) | 37 | 2026-10-18 | 82 | 68% |  |
| 125 | [x] | Amnesia: The Dark Descent (STEAM) | 37 | 2026-11-09 | 73 | 81% |  |
| 126 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 37 | 2026-11-09 | 69 | 89% |  |
| 127 | [x] | Street Fighter™ 6 (STEAM) | 37 | 2026-11-09 | 61 | 84% |  |
| 128 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 37 | 2026-11-09 | 50 | 79% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 129 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 37 | 2026-11-09 | 39 | 80% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 130 | [x] | Sonic Origins (STEAM) | 36 | 2026-11-09 | 67 | 82% |  |
| 131 | [x] | Capcom Arcade Stadium (STEAM) | 36 | 2026-11-09 | 46 | 73% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 132 | [x] | Russian Fishing 4 (STEAM) | 36 | 2026-11-09 | 42 | 84% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 133 | [x] | CrossCode (GOG) | 36 | 2026-11-09 | 39 | 80% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 134 | [x] | POSTAL 2 (GOG) | 35 | 2026-11-09 | 69 | 88% |  |
| 135 | [x] | XCOM 2 (STEAM) | 35 | 2026-11-09 | 59 | 85% |  |
| 136 | [x] | Elite Dangerous (STEAM) | 35 | 2026-11-09 | 38 | 60% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 137 | [x] | Cobalt Core (STEAM) | 34 | 2026-10-18 | 93 | 86% |  |
| 138 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 34 | 2026-11-11 | 64 | 36% |  |
| 139 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 34 | 2026-11-09 | 64 | 85% |  |
| 140 | [x] | The Bazaar (STEAM) | 34 | 2026-11-09 | 63 | 75% |  |
| 141 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 34 | 2026-11-09 | 60 | 73% |  |
| 142 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 34 | 2026-11-09 | 55 | 88% |  |
| 143 | [x] | Need for Speed™ Rivals (STEAM) | 34 | 2026-11-10 | 46 | 83% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 144 | [x] | Romestead (STEAM) | 34 | 2026-11-09 | 44 | 61% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 145 | [x] | State of Decay: Year-One (STEAM) | 33 | 2026-10-18 | 68 | 78% |  |
| 146 | [x] | Hearts of Iron IV (STEAM) | 33 | 2026-11-09 | 66 | 79% |  |
| 147 | [x] | Hero Siege (STEAM) | 33 | 2026-11-09 | 57 | 84% |  |
| 148 | [x] | Gauntlet™  (STEAM) | 33 | 2026-11-11 | 48 | 64% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 149 | [x] | Salt and Sanctuary (STEAM) | 32 | 2026-10-18 | 74 | 83% |  |
| 150 | [x] | Journey (STEAM) | 32 | 2026-10-27 | 73 | 68% |  |
| 151 | [x] | SurrounDead (STEAM) | 32 | 2026-11-09 | 64 | 90% |  |
| 152 | [x] | Being a DIK (STEAM) | 32 | 2026-11-09 | 59 | 56% |  |
| 153 | [x] | Stumble Guys (STEAM) | 32 | 2026-10-18 | 58 | 71% |  |
| 154 | [x] | Max Payne (STEAM) | 32 | 2026-11-09 | 57 | 85% |  |
| 155 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 32 | 2026-11-09 | 56 | 71% |  |
| 156 | [x] | Earthion (STEAM) | 32 | 2026-11-09 | 54 | 100% |  |
| 157 | [x] | Counter-Strike:Global Offensive (STEAM) | 32 | 2026-11-09 | 51 | 74% |  |
| 158 | [x] | SnowRunner (STEAM) | 32 | 2026-11-09 | 46 | 81% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 159 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-11-09 | 41 | 92% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 160 | [x] | Red Dead Redemption (STEAM) | 32 | 2026-11-09 | 35 | 55% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 161 | [x] | COCOON (STEAM) | 31 | 2026-11-09 | 66 | 86% |  |
| 162 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 31 | 2026-11-09 | 62 | 85% |  |
| 163 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 30 | 2026-11-09 | 67 | 72% |  |
| 164 | [x] | Ultimate Chicken Horse (STEAM) | 30 | 2026-10-23 | 64 | 84% |  |
| 165 | [x] | Resident Evil Village (STEAM) | 30 | 2026-11-09 | 53 | 90% |  |
| 166 | [x] | Prince of Persia: The Sands of Time (STEAM) | 30 | 2026-11-09 | 50 | 78% |  |
| 167 | [x] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 30 | 2026-11-14 | 35 | 64% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 168 | [x] | Torchlight II (STEAM) | 29 | 2026-10-20 | 72 | 86% |  |
| 169 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 29 | 2026-11-09 | 50 | 86% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 170 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 29 | 2026-11-09 | 49 | 83% |  |
| 171 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 29 | 2026-11-09 | 49 | 68% |  |
| 172 | [x] | Secrets of Grindea (STEAM) | 29 | 2026-11-09 | 48 | 74% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 173 | [x] | Gambonanza (STEAM) | 29 | 2026-11-09 | 47 | 95% |  |
| 174 | [x] | Yakuza: Like a Dragon (STEAM) | 29 | 2026-11-09 | 46 | 62% |  |
| 175 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 73% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 176 | [x] | Heavy Rain (STEAM) | 28 | 2026-11-09 | 48 | 94% |  |
| 177 | [x] | Palia (STEAM) | 28 | 2026-11-09 | 40 | 76% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 178 | [x] | Frostpunk (STEAM) | 27 | 2026-11-09 | 53 | 74% |  |
| 179 | [x] | Deponia (STEAM) | 27 | 2026-11-09 | 52 | 74% |  |
| 180 | [x] | Resident Evil Revelations 2 (STEAM) | 27 | 2026-11-09 | 52 | 83% |  |
| 181 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 27 | 2026-11-09 | 49 | 96% |  |
| 182 | [x] | Dead Rising 2 (STEAM) | 27 | 2026-11-09 | 43 | 68% |  |
| 183 | [x] | Tower and Sword of Succubus (STEAM) | 27 | 2026-11-09 | 42 | 81% |  |
| 184 | [x] | Digimon Survive (STEAM) | 27 | 2026-11-09 | 40 | 86% |  |
| 185 | [x] | Gothic II: Gold Classic (STEAM) | 27 | 2026-11-09 | 35 | 64% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 186 | [x] | ROB RUN (STEAM) | 27 | 2026-11-17 | 34 | 61% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 187 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 26 | 2026-10-19 | 92 | 92% |  |
| 188 | [x] | Skullgirls 2nd Encore (STEAM) | 26 | 2026-11-10 | 62 | 67% |  |
| 189 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 45 | 63% |  |
| 190 | [x] | Capcom Fighting Collection 2 (STEAM) | 26 | 2026-11-09 | 43 | 81% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 191 | [x] | Guildrun Demo (STEAM) | 26 | 2026-11-09 | 43 | 71% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 192 | [x] | Limbus Company (STEAM) | 26 | 2026-11-09 | 40 | 83% |  |
| 193 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 26 | 2026-11-09 | 39 | 68% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 194 | [x] | CRUEL (STEAM) | 26 | 2026-11-09 | 36 | 82% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 195 | [x] | Aethermancer (STEAM) | 25 | 2026-10-18 | 52 | 87% |  |
| 196 | [x] | Battle Brothers (STEAM) | 25 | 2026-11-09 | 44 | 82% |  |
| 197 | [x] | Counter-Strike: Condition Zero (STEAM) | 25 | 2026-11-11 | 44 | 31% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 198 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-09 | 32 | 90% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 199 | [x] | BioShock™ (GOG) | 24 | 2026-10-18 | 64 | 83% |  |
| 200 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 57 | 91% |  |
| 201 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 24 | 2026-10-20 | 53 | 86% |  |
| 202 | [x] | Mirror's Edge™ (GOG) | 24 | 2026-11-13 | 45 | 64% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 203 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 24 | 2026-11-09 | 43 | 66% |  |
| 204 | [x] | Opus Magnum (STEAM) | 24 | 2026-11-09 | 39 | 92% |  |
| 205 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 24 | 2026-11-09 | 37 | 75% |  |
| 206 | [x] | Ratatan (STEAM) | 24 | 2026-11-09 | 37 | 94% |  |
| 207 | [x] | Jade Empire: Special Edition (GOG) | 24 | 2026-11-09 | 31 | 71% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 208 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 24 | 2026-11-09 | 31 | 91% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 209 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 24 | 2026-11-09 | 30 | 82% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 210 | [x] | Tales of Zestiria (STEAM) | 24 | 2026-11-09 | 30 | 69% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 211 | [x] | Subnautica 2 (STEAM) | 24 | 2026-11-15 | 29 | 71% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 212 | [x] | Crab Game (STEAM) | 24 | 2026-11-09 | 28 | 85% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 213 | [x] | Jade Empire: Special Edition (STEAM) | 24 | 2026-11-09 | 27 | 71% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 214 | [x] | Goat Simulator (STEAM) | 23 | 2026-11-09 | 48 | 72% |  |
| 215 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 46 | 88% |  |
| 216 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-11-09 | 45 | 90% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 217 | [x] | Prince of Persia (GOG) | 23 | 2026-11-09 | 44 | 82% |  |
| 218 | [x] | Lucid Blocks (STEAM) | 23 | 2026-11-09 | 44 | 63% |  |
| 219 | [x] | Trailmakers (STEAM) | 23 | 2026-11-09 | 41 | 93% |  |
| 220 | [x] | Football Manager 2024 (EPIC) | 23 | 2026-11-09 | 39 | 62% |  |
| 221 | [x] | Cat Mail Co. (STEAM) | 23 | 2026-11-09 | 39 | 83% |  |
| 222 | [x] | Dishonored 2 (STEAM) | 23 | 2026-11-09 | 33 | 79% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 223 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 95% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 224 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 23 | 2026-11-09 | 27 | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 225 | [x] | Crazy Taxi (STEAM) | 22 | 2026-11-10 | 44 | 66% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 226 | [x] | Wizard of Legend (EPIC) | 22 | 2026-11-09 | 41 | 81% |  |
| 227 | [x] | Unturned (STEAM) | 22 | 2026-11-09 | 40 | 71% |  |
| 228 | [x] | My Summer Car (STEAM) | 22 | 2026-11-09 | 36 | 81% |  |
| 229 | [x] | Deus Ex™ GOTY Edition (GOG) | 22 | 2026-11-09 | 35 | 92% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 230 | [x] | Return to Monkey Island (STEAM) | 22 | 2026-11-09 | 35 | 70% |  |
| 231 | [x] | Tabletop Simulator (STEAM) | 22 | 2026-11-09 | 35 | 76% |  |
| 232 | [x] | Timberborn (STEAM) | 22 | 2026-11-09 | 34 | 95% |  |
| 233 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 59 | 95% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 234 | [x] | No Rest for the Wicked (STEAM) | 21 | 2026-10-19 | 47 | 72% |  |
| 235 | [x] | Slow Roads (STEAM) | 21 | 2026-10-22 | 47 | 76% |  |
| 236 | [x] | Control Ultimate Edition (GOG) | 21 | 2026-11-09 | 39 | 83% |  |
| 237 | [x] | Invisible, Inc. (STEAM) | 21 | 2026-11-09 | 37 | 80% |  |
| 238 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 87% |  |
| 239 | [x] | CarX Street (STEAM) | 21 | 2026-11-09 | 26 | 81% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 240 | [x] | Tearscape (STEAM) | 21 | 2026-11-09 | 25 | 100% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 241 | [x] | MudRunner (EPIC) | 20 | 2026-10-18 | 43 | 67% |  |
| 242 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-11-09 | 38 | 100% |  |
| 243 | [x] | Pinball FX Classic (STEAM) | 20 | 2026-11-09 | 38 | 88% |  |
| 244 | [x] | Worms W.M.D (STEAM) | 20 | 2026-11-09 | 37 | 95% |  |
| 245 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 20 | 2026-11-09 | 30 | 91% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 246 | [x] | Party Animals (STEAM) | 20 | 2026-11-09 | 29 | 65% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 247 | [x] | Torchlight II (EPIC) | 20 | 2026-11-09 | 28 | 76% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 248 | [x] | Tyr (STEAM) | 20 | 2026-11-09 | 28 | 67% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 249 | [x] | Dead Island (STEAM) | 20 | 2026-11-09 | 25 | 83% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 250 | [x] | Saints Row IV (STEAM) | 19 | 2026-10-19 | 50 | 83% |  |
| 251 | [x] | Mini Metro (STEAM) | 19 | 2026-11-16 | 38 | 42% |  |
| 252 | [x] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 2026-11-15 | 36 | 65% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 253 | [x] | Sorry We're Closed (EPIC) | 19 | 2026-11-09 | 34 | 71% |  |
| 254 | [x] | One-armed robber (STEAM) | 19 | 2026-11-09 | 34 | 65% |  |
| 255 | [x] | SWORN (STEAM) | 19 | 2026-11-09 | 34 | 94% |  |
| 256 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 19 | 2026-11-09 | 33 | 75% |  |
| 257 | [x] | Far Far West (STEAM) | 19 | 2026-11-09 | 33 | 54% |  |
| 258 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 32 | 71% |  |
| 259 | [x] | Moonlight Peaks (STEAM) | 19 | 2026-11-09 | 31 | 75% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 260 | [x] | GOD EATER RESURRECTION (STEAM) | 19 | 2026-11-09 | 30 | 78% |  |
| 261 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 19 | 2026-11-09 | 30 | 82% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 262 | [x] | Backpack Battles (STEAM) | 18 | 2026-11-09 | 42 | 97% |  |
| 263 | [x] | This War of Mine (STEAM) | 18 | 2026-11-17 | 35 | 47% |  |
| 264 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-11-09 | 27 | 76% |  |
| 265 | [x] | Capcom Fighting Collection (STEAM) | 18 | 2026-11-09 | 26 | 87% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 266 | [x] | Need for Speed™ Unbound (STEAM) | 18 | 2026-11-09 | 26 | 53% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 267 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 18 | 2026-11-09 | 24 | 62% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 268 | [x] | Mafia II: Definitive Edition (GOG) | 18 | 2026-11-15 | 20 | 60% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 269 | [x] | Undisputed (STEAM) | 18 | 2026-11-14 | 20 | 69% | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 270 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 17 | 2026-10-19 | 57 | 78% |  |
| 271 | [x] | Kingdom Come: Deliverance II (STEAM) | 17 | 2026-10-20 | 40 | 83% |  |
| 272 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 37 | 21% |  |
| 273 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 35 | 93% |  |
| 274 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 17 | 2026-11-09 | 31 | 83% |  |
| 275 | [x] | Bongo Cat (STEAM) | 17 | 2026-11-09 | 23 | 62% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 276 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 17 | 2026-11-09 | 22 | 92% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 277 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 278 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 279 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 51 | 95% |  |
| 280 | [x] | Cave Story+ (EPIC) | 16 | 2026-10-18 | 41 | 88% |  |
| 281 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 16 | 2026-10-20 | 37 | 80% |  |
| 282 | [x] | GRIP: Combat Racing (STEAM) | 16 | 2026-11-09 | 34 | 79% |  |
| 283 | [x] | sobosuba (STEAM) | 16 | 2026-11-09 | 34 | 84% |  |
| 284 | [x] | Intravenous 2 (STEAM) | 16 | 2026-11-09 | 31 | 97% |  |
| 285 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 286 | [x] | Tiny Glade (STEAM) | 16 | 2026-11-09 | 31 | 60% |  |
| 287 | [x] | Mortal Kombat 11 (STEAM) | 16 | 2026-11-09 | 30 | 80% |  |
| 288 | [x] | Batman™: Arkham Origins (GOG) | 16 | 2026-11-09 | 28 | 100% |  |
| 289 | [x] | Legend of Grimrock 2 (STEAM) | 16 | 2026-11-09 | 26 | 92% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 290 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 62% |  |
| 291 | [x] | Assassin's Creed Odyssey (STEAM) | 16 | 2026-11-09 | 25 | 60% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 292 | [x] | Ghostwire Tokyo (EPIC) | 16 | 2026-11-09 | 22 | 61% |  |
| 293 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 294 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 295 | [x] | ABZÛ (STEAM) | 15 | 2026-10-21 | 44 | 94% |  |
| 296 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 15 | 2026-10-21 | 42 | 77% |  |
| 297 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 15 | 2026-10-25 | 41 | 73% |  |
| 298 | [x] | Grim Fandango Remastered (STEAM) | 15 | 2026-10-19 | 40 | 76% |  |
| 299 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 15 | 2026-11-11 | 35 | 70% |  |
| 300 | [x] | Mark of the Ninja (STEAM) | 15 | 2026-10-26 | 32 | 83% |  |
| 301 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 31 | 96% |  |
| 302 | [x] | Hitman: Absolution (GOG) | 15 | 2026-11-09 | 29 | 75% |  |
| 303 | [x] | Human Fall Flat (STEAM) | 15 | 2026-10-29 | 29 | 62% |  |
| 304 | [x] | Titanfall® 2 (STEAM) | 15 | 2026-11-09 | 29 | 71% |  |
| 305 | [x] | GRANDIA HD Remaster (STEAM) | 15 | 2026-11-09 | 28 | 88% |  |
| 306 | [x] | AER Memories of Old (EPIC) | 15 | 2026-11-09 | 26 | 100% |  |
| 307 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 15 | 2026-11-15 | 25 | 63% |  |
| 308 | [x] | Alabaster Dawn Demo (STEAM) | 15 | 2026-11-09 | 23 | 74% |  |
| 309 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 93% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 310 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 311 | [x] | Spark the Electric Jester (STEAM) | 15 | 2026-11-13 | 21 | 69% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 312 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 15 | 2026-11-09 | 21 | 82% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 313 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 314 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 100% |  |
| 315 | [x] | Killing Floor (STEAM) | 14 | 2026-10-19 | 29 | 86% |  |
| 316 | [x] | Evoland (STEAM) | 14 | 2026-11-11 | 28 | n/a |  |
| 317 | [x] | Need for Speed: Undercover (STEAM) | 14 | 2026-11-11 | 27 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 318 | [x] | Ultrapool (STEAM) | 14 | 2026-11-09 | 27 | 100% |  |
| 319 | [x] | WORLD OF FINAL FANTASY (STEAM) | 14 | 2026-11-09 | 25 | 79% |  |
| 320 | [x] | Wildermyth (STEAM) | 14 | 2026-11-09 | 25 | 67% |  |
| 321 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-11-09 | 22 | 92% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 322 | [x] | Nex Machina (STEAM) | 14 | 2026-11-09 | 22 | 75% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 323 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 324 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 22 | 79% |  |
| 325 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 326 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 327 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 13 | 2026-10-19 | 31 | 93% |  |
| 328 | [x] | Faster Than Light (EPIC) | 13 | 2026-11-09 | 29 | 93% |  |
| 329 | [x] | No Man's Sky (GOG) | 13 | 2026-10-19 | 29 | 90% |  |
| 330 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 29 | 54% |  |
| 331 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 29 | 77% |  |
| 332 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 29 | 81% |  |
| 333 | [x] | Dead Space™ 3 (STEAM) | 13 | 2026-10-20 | 28 | 69% |  |
| 334 | [x] | Soul's Remnant (STEAM) | 13 | 2026-11-11 | 28 | n/a |  |
| 335 | [x] | Castle in the Clouds (STEAM) | 13 | 2026-11-09 | 27 | 62% |  |
| 336 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 13 | 2026-11-09 | 27 | 90% |  |
| 337 | [x] | Blaster Master Zero (STEAM) | 13 | 2026-11-11 | 26 | 71% |  |
| 338 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 13 | 2026-11-09 | 26 | 67% |  |
| 339 | [x] | Cruelty Squad (STEAM) | 13 | 2026-11-09 | 26 | 84% |  |
| 340 | [x] | MX Bikes (STEAM) | 13 | 2026-11-09 | 26 | 93% |  |
| 341 | [x] | Haydee (STEAM) | 13 | 2026-11-09 | 24 | 87% |  |
| 342 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 24 | 76% |  |
| 343 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 13 | 2026-11-09 | 23 | 69% |  |
| 344 | [x] | 12 is Better Than 6 (STEAM) | 13 | 2026-11-09 | 22 | 83% |  |
| 345 | [x] | PAYDAY: The Heist (STEAM) | 13 | 2026-11-13 | 22 | 73% |  |
| 346 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 13 | 2026-11-13 | 22 | 73% |  |
| 347 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 348 | [x] | STAR WARS™ Episode I: Racer (GOG) | 13 | 2026-11-15 | 21 | 62% | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 349 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 70% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 350 | [x] | The Stanley Parable (STEAM) | 13 | 2026-11-13 | 21 | 86% |  |
| 351 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 100% |  |
| 352 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 353 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 2026-11-09 | 20 | 85% |  |
| 354 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-11-16 | 20 | 90% |  |
| 355 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 80% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 356 | [x] | Overlord (STEAM) | 12 | 2026-11-08 | 29 | 55% |  |
| 357 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 12 | 2026-11-09 | 27 | 88% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 358 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 12 | 2026-10-18 | 27 | 100% |  |
| 359 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 26 | 74% |  |
| 360 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-10 | 24 | 62% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 361 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 24 | 64% |  |
| 362 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-11-09 | 23 | 97% |  |
| 363 | [x] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 2026-11-12 | 22 | 90% |  |
| 364 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 365 | [x] | Horny Villa (STEAM) | 12 | 2026-11-09 | 21 | 85% |  |
| 366 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 2026-11-16 | 21 | 78% |  |
| 367 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 368 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 369 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 2026-11-10 | 20 | 60% |  |
| 370 | [x] | Shift At Midnight (STEAM) | 12 | 2026-11-09 | 20 | 89% |  |
| 371 | [x] | Turbo Overkill (STEAM) | 12 | 2026-11-09 | 20 | 95% |  |
| 372 | [x] | Spin Rhythm XD (STEAM) | 11 | 2026-10-18 | 32 | 82% |  |
| 373 | [x] | Haiku, the Robot (STEAM) | 11 | 2026-10-21 | 27 | n/a |  |
| 374 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 2026-10-27 | 26 | 74% |  |
| 375 | [x] | Coromon (GOG) | 11 | 2026-10-19 | 25 | 68% |  |
| 376 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 25 | 80% |  |
| 377 | [x] | Guacamelee! Gold Edition (STEAM) | 11 | 2026-11-11 | 25 | 75% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 378 | [x] | Lust Goddess (STEAM) | 11 | 2026-11-09 | 25 | 88% |  |
| 379 | [x] | Alan Wake's American Nightmare (EPIC) | 11 | 2026-11-09 | 24 | 64% |  |
| 380 | [x] | Rayman Origins (GOG) | 11 | 2026-11-09 | 24 | 77% |  |
| 381 | [x] | DiRT 4 (STEAM) | 11 | 2026-11-09 | 23 | 92% |  |
| 382 | [x] | Life is Strange Remastered (STEAM) | 11 | 2026-11-09 | 23 | 86% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 383 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 23 | 85% |  |
| 384 | [x] | Ready or Not (STEAM) | 11 | 2026-11-09 | 23 | 83% |  |
| 385 | [x] | Lost Castle 2 (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 386 | [x] | Forgive Me Father (STEAM) | 11 | 2026-11-15 | 21 | 67% |  |
| 387 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 388 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-11-09 | 20 | 73% |  |
| 389 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 390 | [x] | The WereCleaner (STEAM) | 10 | 2026-10-22 | 31 | 89% |  |
| 391 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 28 | n/a |  |
| 392 | [x] | Distance (STEAM) | 10 | 2026-10-19 | 27 | 82% |  |
| 393 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 10 | 2026-10-23 | 25 | 90% |  |
| 394 | [x] | Breath of Fire IV (GOG) | 10 | 2026-10-26 | 24 | 62% |  |
| 395 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 10 | 2026-11-01 | 24 | n/a |  |
| 396 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 24 | 93% |  |
| 397 | [x] | Aperture Desk Job (STEAM) | 10 | 2026-11-03 | 23 | n/a |  |
| 398 | [x] | Sid Meier's Civilization VI (EPIC) | 10 | 2026-10-19 | 21 | 67% |  |
| 399 | [x] | UNDEFEATED (STEAM) | 10 | 2026-11-09 | 21 | 73% |  |
| 400 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 401 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 402 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 403 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 20 | 78% |  |
| 404 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 405 | [x] | Possessor(s) (STEAM) | 9 | 2026-10-24 | 27 | 88% |  |
| 406 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 9 | 2026-10-20 | 26 | 90% |  |
| 407 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 9 | 2026-10-21 | 21 | 92% |  |
| 408 | [x] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 9 | 2026-11-17 | 20 | 27% |  |
| 409 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 9 | 2026-11-09 | 20 | 82% |  |
| 410 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 31% |  |
| 411 | [x] | SteamWorld Heist (GOG) | 8 | 2026-10-25 | 21 | n/a |  |
| 412 | [x] | HITMAN World of Assassination (STEAM) | 8 | 2026-11-09 | 20 | 80% |  |
| 413 | [x] | CULTIC (STEAM) | 7 | 2026-11-09 | 21 | 53% |  |
| 414 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 21 | 52% |  |
| 415 | [x] | SCP – Containment Breach (STEAM) | 7 | 2026-10-27 | 21 | 91% |  |
| 416 | [x] | Mina the Hollower (GOG) | 7 | 2026-10-28 | 20 | 74% |  |
| 417 | [x] | What Remains of Edith Finch (STEAM) | 6 | 2026-10-19 | 28 | 79% |  |
| 418 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 5 | 2026-10-20 | 20 | 69% |  |
