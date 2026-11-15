# GameNative compatibility worklist

Generated: `2026-11-15T04:15:12.449Z` · Ratings since: `2026-08-17T04:15:12.449Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 122 |
| Probably does not work | 171 |
| Fix shipped, waiting for ratings | 15 |
| First launch fails | 325 |
| Mixed | 495 |
| Works | 1026 |
| Total | 2154 |

## Does not work (122)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 159 | 181 | 88% (14d) | Does not open (83%) | 55% | today | 10% (drop) | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 100 | 115 | 87% (since fix) | Does not open (92%) | 49% | today | 37% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 3 | [ ] | Rocket League® (EPIC) | 54 | 66 | 82% (14d) | Does not open (79%) | 52% | today | 28% (drop) | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 4 | [ ] | Hogwarts Legacy (STEAM) | 27 | 31 | 87% (14d) | Does not open (65%) | 41% | today | 16% (drop) | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 5 | [x] 2026-10-18 | Project Zomboid (STEAM) | 53 | 59 | 90% (since fix) | Does not open (65%) | 50% | 1d ago | 40% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 6 | [ ] | Saints Row 2 (STEAM) | 23 | 23 | 100% (14d) | Does not open (97%) | 33% | today | 37% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 7 | [ ] | Metro 2033 Redux (STEAM) | 22 | 29 | 76% (14d) | Does not open (70%) | 41% | 1d ago | 39% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 8 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 21 | 23 | 91% (14d) | Does not open (96%) | 51% | today | 16% (drop) | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 9 | [ ] | Saints Row 2 (GOG) | 20 | 26 | 77% (14d) | Does not open (92%) | 40% | 2d ago | 31% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 10 | [ ] | ROB RUN (STEAM) | 20 | 26 | 77% (14d) | Does not open (89%) | 55% | today | 58% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 11 | [ ] | Borderlands 2 (EPIC) | 19 | 22 | 86% (14d) | Does not open (80%) | 57% | today | 45% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 12 | [ ] | Bloons TD 6 (EPIC) | 19 | 23 | 83% (14d) | Does not open (78%) | 43% | today | 19% (drop) | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 13 | [ ] | Metro: Last Light Redux (STEAM) | 19 | 20 | 95% (last 20) | Does not open (88%) | 20% | today | 21% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 14 | [ ] | Sifu (EPIC) | 16 | 23 | 70% (14d) | Does not open (69%) | 55% | today | 38% |  |
| 15 | [ ] | Call of Duty: Black Ops II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 31% | today | 38% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 16 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 15 | 20 | 75% (last 20) | Does not open (75%) | 54% | today | 39% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 17 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (76%) | 0% | 6d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 18 | [ ] | Fallout: New Vegas PCR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | 58% | today | 60% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 19 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (92%) | 23% | 1d ago | 14% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 20 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 18 | 20 | 90% (last 20) | No graphics (46%) | 26% | 7d ago | n/a | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 21 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 41% | today | 27% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 22 | [ ] | Path of Exile (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 34% | today | 17% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 23 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (78%) | 7% | today | n/a | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 24 | [ ] | skate. (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | 10% | 1d ago | 18% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 25 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (70%) | 9% | 9d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 26 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | 6% | 1d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 27 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (78%) | 13% | 3d ago | 9% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 28 | [ ] | Mafia II (Classic) (STEAM) | 20 | 20 | 100% (last 20) | Does not open (74%) | 9% | 7d ago | 12% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 29 | [ ] | The Witcher: Enhanced Edition (GOG) | 19 | 20 | 95% (last 20) | Does not open (73%) | 12% | 6d ago | 8% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 30 | [ ] | Fall Guys (EPIC) | 19 | 20 | 95% (last 20) | Does not open (75%) | 13% | today | 8% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 31 | [ ] | Detroit: Become Human (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 53% | 1d ago | n/a | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 32 | [ ] | CPM 2 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 8% | 2d ago | 8% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 33 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | Does not open (54%) | 0% | 18d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 34 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | 0% | today | n/a | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 35 | [ ] | MECCHA CHAMELEON (STEAM) | 16 | 20 | 80% (last 20) | Does not open (65%) | 54% | today | 30% (drop) | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 36 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (70%) | 11% | 3d ago | n/a | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 37 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (91%) | 8% | 16d ago | n/a | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 38 | [ ] | Call of Duty® (STEAM) | 17 | 20 | 85% (last 20) | Does not open (67%) | 8% | today | n/a | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 39 | [ ] | Vampire Survivors (EPIC) | 14 | 20 | 70% (last 20) | Does not open (60%) | 52% | 1d ago | 37% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 40 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (68%) | 12% | 14d ago | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 41 | [ ] | Borderlands GOTY (STEAM) | 17 | 20 | 85% (last 20) | Does not open (94%) | 39% | 2d ago | 50% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 42 | [ ] | Trackmania (STEAM) | 16 | 20 | 80% (last 20) | Does not open (82%) | 18% | today | 25% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 43 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (60%) | 53% | 3d ago | n/a |  |
| 44 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (82%) | 12% | 6d ago | 17% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 45 | [ ] | Breath of Fire IV (STEAM) | 20 | 20 | 100% (last 20) | Does not open (60%) | 15% | 2d ago | 9% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 46 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (88%) | 20% | 6d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 47 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 58% | 5d ago | 32% (drop) | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 48 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (66%) | 17% | 1d ago | 30% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 49 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 53% | 8d ago | n/a | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 50 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (83%) | 40% | 29d ago | 40% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 51 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (88%) | 40% | 2d ago | 42% | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 52 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (71%) | 31% | 3d ago | n/a | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 53 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | 18% | 7d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 54 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 5% | today | 0% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 55 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | 0% | 1d ago | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 56 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (56%) | 29% | 10d ago | n/a | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 57 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (73%) | 57% | 3d ago | n/a | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 58 | [ ] | Plague Inc: Evolved (STEAM) | 14 | 20 | 70% (last 20) | Does not open (68%) | 57% | 5d ago | 60% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 59 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | 0% | today | n/a | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 60 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | 50% | 36d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 61 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 23% | 6d ago | 38% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 62 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (92%) | 31% | 1d ago | n/a | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 63 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (78%) | 37% | 3d ago | 20% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 64 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (47%) | 38% | 10d ago | 32% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 65 | [ ] | Black Mesa (STEAM) | 15 | 20 | 75% (last 20) | Does not open (82%) | 20% | 22d ago | 33% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 66 | [ ] | Watch_Dogs (STEAM) | 14 | 20 | 70% (last 20) | Does not open (90%) | 29% | 8d ago | 40% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 67 | [ ] | XCOM: Enemy Unknown (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | 12% | 1d ago | 20% | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 68 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (71%) | 35% | 8d ago | 25% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 69 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 21% | 27d ago | 36% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 70 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 20% | 24d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 71 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | 50% | 4d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 72 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (55%) | 58% | 3d ago | 56% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 73 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 14 | 20 | 70% (last 20) | Does not open (45%) | 53% | today | 55% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 74 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | 40% | 4d ago | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 75 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | No graphics (60%) | 36% | today | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 76 | [ ] | Half-Life: Blue Shift (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 36% | 6d ago | n/a | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 77 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | Does not open (63%) | 11% | 8d ago | n/a | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 78 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 15% | 13d ago | n/a | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 79 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | 36% | 2d ago | n/a | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 80 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 0% | 28d ago | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 81 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 3% | 3d ago | 1% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 82 | [ ] | Changed (STEAM) | 15 | 20 | 75% (last 20) | Does not open (69%) | 57% | 2d ago | 38% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 83 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 19% | 15d ago | n/a | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 84 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 50% | 3d ago | n/a | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 85 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (67%) | 0% | 21d ago | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 86 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 3% | 10d ago | 6% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 87 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 54% | 3d ago | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 88 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 19 | 20 | 95% (last 20) | No graphics (59%) | 40% | 1d ago | 52% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 89 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (76%) | 19% | 2d ago | n/a | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 90 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 36% | 12d ago | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 91 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (47%) | 59% | 5d ago | 52% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 92 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (91%) | 5% | 21d ago | 10% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 93 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (91%) | 23% | 7d ago | n/a | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 94 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | 36% | 5d ago | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 95 | [ ] | Umamusume: Pretty Derby (STEAM) | 18 | 20 | 90% (last 20) | Does not open (86%) | 50% | 11d ago | 60% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 96 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (68%) | 36% | 31d ago | n/a | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 97 | [ ] | OneShot (STEAM) | 16 | 20 | 80% (last 20) | Does not open (96%) | 17% | 30d ago | n/a | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 98 | [ ] | Hotline Miami (GOG) | 15 | 20 | 75% (last 20) | Does not open (90%) | 55% | 5d ago | n/a | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 99 | [ ] | Lost Planet: Extreme Condition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 43% | today | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 100 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 27% | 13d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 101 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (95%) | 26% | 26d ago | 31% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 102 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | 43% | today | 40% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 103 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (97%) | 27% | 13d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 104 | [ ] | Aliens vs. Predator (STEAM) | 16 | 20 | 80% (last 20) | No graphics (55%) | 22% | 3d ago | 23% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 105 | [ ] | Kenshi (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 4% | 14d ago | n/a | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 106 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | 20% | 4d ago | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 107 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 33% | 29d ago | 30% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 108 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (67%) | 50% | 4d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 109 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | 35% | 15d ago | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 110 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | 50% | 1d ago | 38% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 111 | [ ] | The Lantern of the Laughless Saint (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 46% | 12d ago | n/a | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 112 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | 40% | 32d ago | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 113 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | 0% | 4d ago | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 114 | [ ] | Maneater (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 52% | 1d ago | 45% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 115 | [ ] | Zuma Deluxe (STEAM) | 18 | 20 | 90% (last 20) | Does not open (94%) | 38% | 2d ago | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 116 | [ ] | skate.™ (EPIC) | 18 | 20 | 90% (last 20) | Does not open (87%) | 0% | 20d ago | n/a | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 117 | [ ] | Beyond Good & Evil™ (GOG) | 17 | 20 | 85% (last 20) | Does not open (100%) | 20% | 22d ago | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 118 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (67%) | 57% | 6d ago | n/a | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 119 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 38% | 15d ago | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 120 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 36% | 10d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 121 | [ ] | Maneater (EPIC) | 16 | 20 | 80% (last 20) | Does not open (75%) | 53% | 7d ago | n/a | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 122 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 58% | 7d ago | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |

## Probably does not work (171)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Counter-Strike 2 (STEAM) | 40 | 61 | 66% (since fix) | Does not open (67%) | 58% | today | 67% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 2 | [ ] | theHunter Classic (STEAM) | 22 | 22 | 100% (14d) | No graphics (92%) | n/a | 11d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 3 | [ ] | To The Moon (GOG) | 18 | 20 | 90% (last 20) | Does not open (86%) | n/a | 12d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 4 | [ ] | Euro Truck Simulator 2 (STEAM) | 13 | 25 | 52% (14d) | Does not open (66%) | 57% | today | 56% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 5 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 13 | 20 | 65% (last 20) | Does not open (62%) | 55% | today | 48% |  |
| 6 | [ ] | Bully: Scholarship Edition (STEAM) | 11 | 22 | 50% (14d) | Does not open (58%) | 59% | 1d ago | 10% (drop) |  |
| 7 | [ ] | VRChat (STEAM) | 13 | 20 | 65% (last 20) | Does not open (68%) | 38% | 1d ago | 30% |  |
| 8 | [ ] | Garry's Mod (STEAM) | 8 | 13 | 62% (since fix) | Does not open (79%) | 54% | today | 45% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 9 | [ ] | Driver: Parallel Lines (STEAM) | 19 | 20 | 95% (last 20) | Does not open (65%) | n/a | 6d ago | n/a | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 10 | [ ] | Gorilla Tag (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 17% | today | 8% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 11 | [ ] | Door Kickers 2 (STEAM) | 20 | 20 | 100% (last 20) | No graphics (86%) | n/a | 32d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 12 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 35d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 13 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (36%) | n/a | 12d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 14 | [ ] | Yume Nikki (STEAM) | 11 | 20 | 55% (last 20) | Does not open (87%) | 31% | today | 52% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 15 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 19d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 16 | [ ] | Metro 2033 Redux (EPIC) | 11 | 20 | 55% (last 20) | Does not open (62%) | 22% | today | 39% |  |
| 17 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 8d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 18 | [ ] | Sonic Adventure™ 2  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 48% | 3d ago | 37% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 19 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 9 | 16 | 56% (since fix) | Does not open (78%) | 27% | 1d ago | 41% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 20 | [ ] | Deliver At All Costs (EPIC) | 13 | 20 | 65% (last 20) | Does not open (58%) | 59% | 2d ago | 52% |  |
| 21 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 16d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 22 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 29% | today | 10% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 23 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 13 | 20 | 65% (last 20) | Does not open (84%) | 50% | 4d ago | 67% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 24 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (85%) | 54% | 5d ago | n/a |  |
| 25 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (93%) | n/a | 3d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 26 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (88%) | n/a | today | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 27 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (100%) | n/a | 4d ago | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 28 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 10d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 29 | [ ] | GRID (STEAM) | 10 | 20 | 50% (last 20) | Does not open (58%) | 47% | today | 53% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 30 | [ ] | CODE VEIN (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 47% | 4d ago | n/a | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 31 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | n/a | 2d ago | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 32 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 13d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 33 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | n/a | today | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 34 | [ ] | Hollow Knight: Silksong (GOG) | 12 | 20 | 60% (last 20) | Does not open (72%) | 54% | 2d ago | 57% |  |
| 35 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | 13d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 36 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (93%) | n/a | 3d ago | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 37 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 33d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 38 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (70%) | n/a | 12d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 39 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | n/a | 34d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 40 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 32d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 41 | [ ] | Dead Space 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 31% | 5d ago | 40% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 42 | [ ] | METAL SLUG 3 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 48% | 2d ago | n/a | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 43 | [ ] | Grim Dawn (GOG) | 12 | 20 | 60% (last 20) | Does not open (68%) | n/a | 3d ago | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 44 | [ ] | Alpha Protocol (STEAM) | 17 | 20 | 85% (last 20) | No graphics (53%) | n/a | 20d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 45 | [ ] | HELLDIVERS™ (STEAM) | 13 | 20 | 65% (last 20) | Does not open (58%) | 39% | today | 54% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 46 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | n/a | 1d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 47 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (57%) | n/a | 1d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 48 | [ ] | Borderlands 2 RU (STEAM) | 19 | 20 | 95% (last 20) | Does not open (61%) | n/a | today | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 49 | [ ] | DOOM Eternal (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | n/a | 23d ago | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 50 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | n/a | 16d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 51 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 18d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 52 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | n/a | 11d ago | n/a |  |
| 53 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 33% | 5d ago | n/a | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 54 | [ ] | Breathedge (STEAM) | 11 | 20 | 55% (last 20) | Does not open (56%) | 52% | 4d ago | 67% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 55 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | n/a | 35d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 56 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 10d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 57 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | n/a | 32d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 58 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 32d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 59 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | n/a | 7d ago | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 60 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 18d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 61 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 43d ago | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 62 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 14d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 63 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 1d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 64 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | n/a | 23d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 65 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 6d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 66 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (54%) | n/a | 20d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 67 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (93%) | n/a | 1d ago | n/a |  |
| 68 | [ ] | Euro Truck Simulator (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | 3d ago | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 69 | [ ] | Peggle Nights (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 18d ago | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 70 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (47%) | n/a | 14d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 71 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | n/a | 37d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 72 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | n/a | 41d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 73 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (86%) | n/a | 4d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 74 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (86%) | n/a | 15d ago | n/a | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 75 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | n/a | 3d ago | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 76 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | 4% | 10d ago | n/a |  |
| 77 | [ ] | Metro 2033 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (61%) | 18% | 11d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 78 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 30d ago | n/a | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 79 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 57d ago | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 80 | [ ] | The Survivalists (STEAM) | 18 | 20 | 90% (last 20) | Does not open (97%) | n/a | 2d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 81 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | n/a | 32d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 82 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 8d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 83 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 10d ago | n/a |  |
| 84 | [ ] | A Plague Tale: Innocence (EPIC) | 11 | 20 | 55% (last 20) | Does not open (70%) | 52% | 1d ago | 25% (drop) |  |
| 85 | [ ] | Marvel's Spider-Man 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (88%) | n/a | 34d ago | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 86 | [ ] | They Are Billions (STEAM) | 19 | 20 | 95% (last 20) | Does not open (75%) | n/a | 11d ago | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 87 | [ ] | Alien Breed: Impact (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 20d ago | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 88 | [ ] | Bionic Commando Rearmed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | n/a | 25d ago | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 89 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 18 | 20 | 90% (last 20) | Does not open (75%) | n/a | 19d ago | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 90 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | n/a | 8d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 91 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | n/a | 12d ago | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 92 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 5d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 93 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 3d ago | n/a |  |
| 94 | [ ] | Melatonin (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | n/a | 1d ago | n/a | [#272](https://github.com/GameNative/gamenative-compat/issues/272) |
| 95 | [ ] | No More Room in Hell (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 28d ago | n/a | [#365](https://github.com/GameNative/gamenative-compat/issues/365) |
| 96 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | n/a | 3d ago | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 97 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 6d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 98 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | n/a | 3d ago | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 99 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 16d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 100 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (47%) | n/a | 13d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 101 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 17d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 102 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 10d ago | n/a |  |
| 103 | [ ] | Drop Duchy (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | n/a | 1d ago | n/a |  |
| 104 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 10d ago | n/a |  |
| 105 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 55% | 3d ago | n/a | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 106 | [ ] | Deadly Premonition: The Director's Cut (STEAM) | 18 | 20 | 90% (last 20) | Does not open (53%) | n/a | 8d ago | n/a | [#520](https://github.com/GameNative/gamenative-compat/issues/520) |
| 107 | [ ] | Lay of the Land (STEAM) | 18 | 20 | 90% (last 20) | No graphics (61%) | n/a | 14d ago | n/a | [#477](https://github.com/GameNative/gamenative-compat/issues/477) |
| 108 | [ ] | Marvel's Midnight Suns (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | n/a | 32d ago | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 109 | [ ] | PICO PARK:Classic Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 37d ago | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 110 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 13d ago | n/a |  |
| 111 | [ ] | Beholder (EPIC) | 15 | 20 | 75% (last 20) | Does not open (69%) | n/a | 20d ago | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 112 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 3d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 113 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | Does not open (42%) | n/a | 5d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 114 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 57% | 3d ago | n/a |  |
| 115 | [ ] | King's Bounty: The Legend (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | n/a | 9d ago | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 116 | [ ] | ENDLESS Space™ 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | n/a | 30d ago | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 117 | [ ] | Fallout Classic (GOG) | 15 | 20 | 75% (last 20) | Does not open (88%) | n/a | 2d ago | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 118 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | n/a | 27d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 119 | [ ] | Goose Goose Duck (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 58% | today | n/a | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 120 | [ ] | Mafia II (Classic) (GOG) | 13 | 20 | 65% (last 20) | Does not open (95%) | n/a | today | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 121 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | 53% | 15d ago | 25% (drop) |  |
| 122 | [ ] | Mini Metro (STEAM) | 11 | 20 | 55% (last 20) | Does not open (44%) | 41% | 3d ago | n/a |  |
| 123 | [ ] | Re-Volt (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (71%) | n/a | 21d ago | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 124 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | n/a | 19d ago | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 125 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | 2d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 126 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | n/a | 5d ago | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 127 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (83%) | 28% | 13d ago | 17% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 128 | [ ] | Chasm (GOG) | 12 | 20 | 60% (last 20) | No graphics (50%) | n/a | today | n/a |  |
| 129 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (50%) | n/a | 6d ago | n/a |  |
| 130 | [ ] | Chef Knight (STEAM) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 19d ago | n/a |  |
| 131 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (89%) | n/a | 7d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 132 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 4d ago | n/a |  |
| 133 | [ ] | Hitman 2: Silent Assassin (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 33% | today | 42% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 134 | [ ] | FINAL FANTASY VII REMAKE INTERGRADE (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 44% | today | 41% |  |
| 135 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | n/a | 26d ago | n/a |  |
| 136 | [ ] | Sandustry (STEAM) | 12 | 20 | 60% (last 20) | Does not open (73%) | n/a | today | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 137 | [ ] | Styx: Master of Shadows (EPIC) | 12 | 20 | 60% (last 20) | Does not open (75%) | 37% | today | 40% |  |
| 138 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 58% | 6d ago | 58% |  |
| 139 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | No graphics (57%) | 21% | 8d ago | n/a | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 140 | [ ] | Dungeon Keeper™ 2 (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 21d ago | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 141 | [ ] | Beat Cop (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | n/a | 2d ago | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 142 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | n/a | 37d ago | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 143 | [ ] | Blood Omen: Legacy of Kain (GOG) | 13 | 20 | 65% (last 20) | No graphics (67%) | 43% | 4d ago | n/a |  |
| 144 | [ ] | Mortal Shell (EPIC) | 12 | 20 | 60% (last 20) | No graphics (58%) | 58% | 1d ago | 22% (drop) |  |
| 145 | [ ] | Songs of Conquest (EPIC) | 12 | 20 | 60% (last 20) | Does not open (75%) | n/a | 13d ago | n/a |  |
| 146 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 10d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 147 | [ ] | Mafia: Definitive Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 46% | 1d ago | 41% |  |
| 148 | [ ] | A Plague Tale: Innocence (GOG) | 11 | 20 | 55% (last 20) | Does not open (91%) | 58% | 22d ago | n/a |  |
| 149 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 45% | 3d ago | n/a | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 150 | [ ] | This War of Mine (STEAM) | 10 | 20 | 50% (last 20) | Does not open (54%) | 50% | 15d ago | 29% (drop) |  |
| 151 | [ ] | Knights of Pen and Paper 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (42%) | n/a | 6d ago | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 152 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 13 | 20 | 65% (last 20) | No graphics (56%) | n/a | 33d ago | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 153 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 9d ago | n/a |  |
| 154 | [ ] | Minit (EPIC) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 7d ago | n/a |  |
| 155 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 58% | 1d ago | 91% |  |
| 156 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 16d ago | n/a |  |
| 157 | [ ] | No More Heroes (STEAM) | 10 | 20 | 50% (last 20) | No graphics (71%) | 45% | 1d ago | 27% |  |
| 158 | [ ] | Fogpiercer (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 28d ago | n/a | [#303](https://github.com/GameNative/gamenative-compat/issues/303) |
| 159 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 30% | 5d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 160 | [ ] | Ys: Memories of Celceta (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 36% | 15d ago | n/a |  |
| 161 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (78%) | n/a | 9d ago | n/a |  |
| 162 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 54% | 7d ago | n/a |  |
| 163 | [ ] | Turnip Boy Robs a Bank (EPIC) | 11 | 20 | 55% (last 20) | Does not open (67%) | 40% | 1d ago | n/a | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 164 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 35% | 10d ago | n/a |  |
| 165 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | n/a | 9d ago | n/a |  |
| 166 | [ ] | Dex (GOG) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 4d ago | n/a |  |
| 167 | [ ] | Railway Chai Wala (STEAM) | 11 | 20 | 55% (last 20) | Does not open (91%) | n/a | today | n/a |  |
| 168 | [ ] | Crying Suns (EPIC) | 11 | 20 | 55% (last 20) | No graphics (57%) | n/a | 5d ago | n/a |  |
| 169 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 10 | 20 | 50% (last 20) | Does not open (86%) | n/a | 80d ago | n/a |  |
| 170 | [ ] | Delver (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 43% | 1d ago | 0% (drop) |  |
| 171 | [ ] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 17% | 10d ago | n/a |  |

## Fix shipped, waiting for ratings (15)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | Plants vs. Zombies: Game of the Year (STEAM) | 2026-11-04 | 7 | 5 | 3d ago | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 2 | L.A. Noire (STEAM) | 2026-11-04 | 4 | 4 | today | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 3 | Transistor (STEAM) | 2026-11-10 | 1 | 1 | 3d ago | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 4 | Max Payne 3 (STEAM) | 2026-11-04 | 1 | 1 | 8d ago | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 5 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 6 | 6 | 8d ago | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 6 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 3 | 3 | 4d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 7 | Peggle Deluxe (STEAM) | 2026-10-29 | 1 | 1 | 2d ago | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 8 | Necesse (STEAM) | 2026-10-29 | 5 | 0 | 6d ago | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 9 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 1 | 1 | 4d ago | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 10 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 1 | 1 | 11d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 11 | Need for Speed™ (STEAM) | 2026-11-04 | 0 | 0 | 24d ago | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 12 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 0 | 0 | 12d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 13 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 0 | 0 | 17d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 14 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 0 | 0 | 11d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 15 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 10d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |

## Works, but the first launch usually fails (325)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 76 | 99 | 77% (14d) | Does not open (63%) | 90% | today | 93% |  |
| 2 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 61 | 84 | 73% (14d) | Does not open (54%) | 83% | today | 84% |  |
| 3 | [ ] | Grand Theft Auto V Legacy (STEAM) | 45 | 55 | 82% (since fix) | Does not open (88%) | 76% | today | 71% |  |
| 4 | [ ] | MONSTER HUNTER RISE (STEAM) | 44 | 72 | 61% (14d) | Does not open (84%) | 60% | today | 61% |  |
| 5 | [ ] | Road Rash™: 30th Anniversary Edition (STEAM) | 44 | 61 | 72% (14d) | Does not open (74%) | 63% | today | 67% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 6 | [ ] | Half-Life (STEAM) | 43 | 71 | 61% (14d) | Does not open (57%) | 71% | today | 66% |  |
| 7 | [ ] | Cyberpunk 2077 (STEAM) | 43 | 74 | 58% (14d) | Does not open (68%) | 73% | today | 65% |  |
| 8 | [ ] | Valheim (STEAM) | 32 | 51 | 63% (since fix) | No graphics (53%) | 88% | today | 84% |  |
| 9 | [ ] | Buckshot Roulette (STEAM) | 39 | 64 | 61% (14d) | Does not open (64%) | 73% | today | 46% (drop) |  |
| 10 | [ ] | No Man's Sky (STEAM) | 31 | 52 | 60% (since fix) | Controller issues (61%) | 79% | today | 76% |  |
| 11 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 38 | 51 | 75% (14d) | Does not open (78%) | 77% | today | 74% |  |
| 12 | [ ] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 36 | 66 | 55% (14d) | Does not open (64%) | 61% | today | 67% |  |
| 13 | [ ] | DREDGE (EPIC) | 33 | 37 | 89% (14d) | Does not open (76%) | 64% | today | 49% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 14 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 26 | 38 | 68% (14d) | Does not open (56%) | 74% | today | 62% |  |
| 15 | [ ] | Red Dead Redemption 2 (STEAM) | 18 | 19 | 95% (since fix) | Does not open (98%) | 80% | 1d ago | 80% |  |
| 16 | [ ] | Quake (STEAM) | 21 | 31 | 68% (14d) | Does not open (66%) | 81% | 1d ago | 57% (drop) |  |
| 17 | [ ] | ELDEN RING (STEAM) | 20 | 35 | 57% (14d) | Does not open (85%) | 72% | today | 66% |  |
| 18 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 19 | 24 | 79% (14d) | Does not open (74%) | 60% | 2d ago | 56% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 19 | [ ] | BeamNG.drive (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 78% | today | 56% (drop) | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 20 | [ ] | Deadlock (STEAM) | 17 | 22 | 77% (14d) | Does not open (54%) | 87% | today | 84% |  |
| 21 | [ ] | Palworld (STEAM) | 16 | 31 | 52% (14d) | Does not open (75%) | 87% | today | 86% |  |
| 22 | [ ] | Horizon Chase Turbo (EPIC) | 16 | 29 | 55% (14d) | Does not open (82%) | 65% | today | 39% (drop) |  |
| 23 | [ ] | Devil May Cry 5 (STEAM) | 16 | 27 | 59% (14d) | Does not open (83%) | 77% | 1d ago | 83% |  |
| 24 | [ ] | BioShock Remastered (EPIC) | 16 | 20 | 80% (14d) | Does not open (65%) | 69% | 1d ago | 57% |  |
| 25 | [ ] | Mortal Kombat X (STEAM) | 16 | 24 | 67% (14d) | Does not open (72%) | 92% | 2d ago | 92% |  |
| 26 | [ ] | DRAGON BALL FighterZ (STEAM) | 26 | 44 | 59% (since fix) | Does not open (89%) | 78% | today | 89% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 27 | [ ] | Crypt of the NecroDancer (STEAM) | 15 | 29 | 52% (14d) | Does not open (49%) | 88% | today | 87% |  |
| 28 | [ ] | Resident Evil 4 (2005) (STEAM) | 15 | 28 | 54% (14d) | Does not open (78%) | 73% | today | 73% |  |
| 29 | [ ] | CHRONO TRIGGER (STEAM) | 14 | 25 | 56% (14d) | Does not open (58%) | 86% | today | 96% |  |
| 30 | [ ] | Clair Obscur: Expedition 33 (STEAM) | 14 | 26 | 54% (14d) | Graphics glitches (41%) | 83% | today | 74% |  |
| 31 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (88%) | 94% | 2d ago | 94% |  |
| 32 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (59%) | 78% | today | 62% |  |
| 33 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (71%) | 100% | today | n/a | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 34 | [ ] | Mass Effect™ Legendary Edition (STEAM) | 9 | 18 | 50% (since fix) | Does not open (87%) | 78% | today | 83% |  |
| 35 | [ ] | Divinity: Original Sin 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (74%) | 87% | 1d ago | 78% |  |
| 36 | [ ] | METAL GEAR SOLID 4: Guns of the Patriots - Master Collection Version (STEAM) | 12 | 21 | 57% (14d) | Does not open (80%) | 89% | 3d ago | 93% |  |
| 37 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 12 | 23 | 52% (14d) | Does not open (72%) | 60% | 1d ago | 94% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 38 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 69% | 6d ago | 65% |  |
| 39 | [ ] | Batman™: Arkham Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (84%) | 75% | 1d ago | 63% |  |
| 40 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 19 | 36 | 53% (since fix) | Does not open (74%) | 63% | today | 53% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 41 | [ ] | Noita (STEAM) | 11 | 22 | 50% (14d) | Does not open (55%) | 76% | today | 78% |  |
| 42 | [ ] | Library Of Ruina (STEAM) | 11 | 20 | 55% (14d) | Does not open (69%) | 87% | today | 80% |  |
| 43 | [ ] | Dead Island 2 (EPIC) | 17 | 20 | 85% (last 20) | Does not open (84%) | 72% | today | 50% (drop) |  |
| 44 | [ ] | Grand Theft Auto V (EPIC) | 19 | 20 | 95% (last 20) | Does not open (89%) | 78% | 2d ago | 74% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 45 | [ ] | Dead Space (STEAM) | 17 | 20 | 85% (last 20) | Does not open (59%) | 84% | today | 84% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 46 | [ ] | Cyberpunk 2077 (GOG) | 12 | 20 | 60% (last 20) | Does not open (71%) | 70% | today | 56% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 47 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (49%) | 91% | today | 88% |  |
| 48 | [ ] | eFootball™ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (63%) | 65% | today | 51% |  |
| 49 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 67% | 2d ago | 50% |  |
| 50 | [ ] | The Forest (STEAM) | 11 | 20 | 55% (last 20) | Does not open (76%) | 84% | today | 84% |  |
| 51 | [ ] | Fallout: New Vegas (EPIC) | 15 | 20 | 75% (last 20) | Does not open (59%) | 84% | 4d ago | 74% |  |
| 52 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (79%) | 98% | 2d ago | 94% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 53 | [ ] | DOOM 3: BFG Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (72%) | 72% | today | 65% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 54 | [ ] | Castlevania Dominus Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (92%) | 97% | today | 90% |  |
| 55 | [ ] | Order of the Sinking Star (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | 67% | today | 76% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 56 | [ ] | Don't Starve Together (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 77% | 1d ago | 65% |  |
| 57 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | 75% | today | 79% |  |
| 58 | [ ] | Dead Island Definitive Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 82% | today | 81% |  |
| 59 | [ ] | Deskrawl: Idle ARPG (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 83% | 4d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 60 | [ ] | Poppy Playtime (STEAM) | 13 | 20 | 65% (last 20) | Does not open (59%) | 71% | today | 63% |  |
| 61 | [ ] | Aniimo (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 83% | 3d ago | 74% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 62 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 16 | 20 | 80% (last 20) | Graphics glitches (44%) | 85% | today | 82% |  |
| 63 | [ ] | Hogwarts Legacy (EPIC) | 14 | 20 | 70% (last 20) | Does not open (76%) | 65% | 1d ago | 49% |  |
| 64 | [ ] | Cry of Fear (STEAM) | 12 | 20 | 60% (last 20) | Does not open (48%) | 75% | today | 72% |  |
| 65 | [ ] | Disgaea 5 Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 88% | 1d ago | 86% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 66 | [ ] | Sid Meier's Civilization VI (STEAM) | 15 | 20 | 75% (last 20) | Does not open (66%) | 84% | today | 68% |  |
| 67 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (82%) | 72% | 6d ago | 50% (drop) |  |
| 68 | [ ] | Castlevania Anniversary Collection (EPIC) | 12 | 20 | 60% (last 20) | Does not open (70%) | 73% | today | 36% (drop) |  |
| 69 | [ ] | Alabaster Dawn (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (48%) | 88% | 1d ago | 87% |  |
| 70 | [ ] | Fate/stay night REMASTERED (STEAM) | 12 | 20 | 60% (last 20) | No graphics (48%) | 91% | today | 76% |  |
| 71 | [ ] | MIO: Memories in Orbit (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (51%) | 95% | 5d ago | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 72 | [ ] | Resident Evil 7 Biohazard (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 79% | 2d ago | 69% |  |
| 73 | [ ] | Welcome to Elderfield (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 70% | 1d ago | 68% |  |
| 74 | [ ] | Need for Speed: Hot Pursuit (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 81% | 1d ago | 89% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 75 | [ ] | OMORI (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 73% | 1d ago | 53% (drop) | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 76 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (51%) | 75% | 1d ago | 39% (drop) | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 77 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 15 | 20 | 75% (last 20) | Does not open (44%) | 71% | 1d ago | 61% |  |
| 78 | [ ] | Call of Duty 4: Modern Warfare (2007) (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (52%) | 85% | 1d ago | 64% |  |
| 79 | [ ] | Prey (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 78% | 4d ago | 79% |  |
| 80 | [ ] | Forza Horizon 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (44%) | 62% | 2d ago | 22% (drop) | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 81 | [ ] | Fable - The Lost Chapters (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (47%) | 86% | 1d ago | 88% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 82 | [ ] | ZERO Sievert (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | 89% | 1d ago | 73% |  |
| 83 | [ ] | Ratatan (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 97% | 2d ago | n/a |  |
| 84 | [ ] | Dota 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (78%) | 72% | 3d ago | 93% |  |
| 85 | [ ] | Darkest Dungeon® (EPIC) | 11 | 20 | 55% (last 20) | Does not open (63%) | 79% | 2d ago | 100% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 86 | [ ] | Happy Wheels (STEAM) | 19 | 20 | 95% (last 20) | No graphics (52%) | 73% | 8d ago | 52% (drop) | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 87 | [ ] | American Truck Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (68%) | 78% | 1d ago | 71% |  |
| 88 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 64% | 1d ago | 70% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 89 | [ ] | Cave Story+ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | 83% | 4d ago | 70% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 90 | [ ] | Need for Speed™ Rivals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (62%) | 73% | 4d ago | 91% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 91 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 14 | 20 | 70% (last 20) | Does not open (60%) | 89% | today | 79% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 92 | [ ] | Abiotic Factor (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 74% | 4d ago | 83% |  |
| 93 | [ ] | Red Dead Redemption (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | 62% | today | 33% (drop) | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 94 | [ ] | Resident Evil Village (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 90% | 3d ago | 83% |  |
| 95 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (62%) | 97% | 2d ago | 100% |  |
| 96 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | No graphics (35%) | 60% | today | 34% (drop) |  |
| 97 | [ ] | Disco Elysium - The Final Cut (EPIC) | 10 | 20 | 50% (last 20) | Does not open (70%) | 97% | 2d ago | 97% |  |
| 98 | [ ] | River City Girls (EPIC) | 13 | 20 | 65% (last 20) | No graphics (52%) | 72% | 1d ago | 44% (drop) |  |
| 99 | [ ] | STAR WARS™ Knights of the Old Republic™ II: The Sith Lords™ (STEAM) | 10 | 20 | 50% (last 20) | No graphics (72%) | 75% | today | 40% (drop) |  |
| 100 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (80%) | 77% | 3d ago | n/a | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 101 | [ ] | Until Then (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | 81% | 1d ago | 63% |  |
| 102 | [ ] | Mini Motorways (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 70% | 1d ago | 67% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 103 | [ ] | Selaco (STEAM) | 13 | 20 | 65% (last 20) | Does not open (84%) | 71% | today | 58% |  |
| 104 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 96% | today | 86% |  |
| 105 | [ ] | Quake II (STEAM) | 10 | 20 | 50% (last 20) | No graphics (48%) | 88% | 1d ago | 80% |  |
| 106 | [ ] | Sid Meier's Civilization V (STEAM) | 16 | 20 | 80% (last 20) | Does not open (76%) | 62% | 1d ago | 61% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 107 | [ ] | Palia (STEAM) | 15 | 20 | 75% (last 20) | Does not open (57%) | 79% | 8d ago | 73% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 108 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 13 | 20 | 65% (last 20) | Does not open (84%) | 65% | 6d ago | n/a | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 109 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 62% | 8d ago | 64% |  |
| 110 | [ ] | Lethal Company (STEAM) | 10 | 20 | 50% (last 20) | Does not open (42%) | 81% | 3d ago | 77% |  |
| 111 | [ ] | TBH: Task Bar Hero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (64%) | 80% | 3d ago | 76% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 112 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (83%) | 85% | today | 75% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 113 | [ ] | Minecraft Dungeons II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (82%) | 68% | 2d ago | 75% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 114 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 13 | 20 | 65% (last 20) | Does not open (43%) | 67% | today | 67% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 115 | [ ] | Little Witch in the Woods (STEAM) | 10 | 20 | 50% (last 20) | Does not open (55%) | 85% | today | 85% |  |
| 116 | [ ] | Yakuza: Like a Dragon (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 63% | 7d ago | 79% |  |
| 117 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (52%) | 66% | today | 77% |  |
| 118 | [ ] | Tails of Iron (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 86% | today | 82% |  |
| 119 | [ ] | Overwatch® (STEAM) | 18 | 20 | 90% (last 20) | Does not open (57%) | 67% | 7d ago | n/a | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 120 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (77%) | 90% | today | n/a | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 121 | [ ] | Moonstone Island (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (60%) | 80% | today | 70% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 122 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 76% | 2d ago | 74% |  |
| 123 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 64% | 6d ago | 80% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 124 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 18 | 20 | 90% (last 20) | Does not open (59%) | 83% | 1d ago | n/a | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 125 | [ ] | Sonic Generations (STEAM) | 16 | 20 | 80% (last 20) | Does not open (68%) | 69% | 7d ago | 81% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 126 | [ ] | Astral Party  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 87% | today | n/a |  |
| 127 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (50%) | 80% | today | 71% |  |
| 128 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 60% | 13d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 129 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 95% | 16d ago | n/a |  |
| 130 | [ ] | Fallout (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 69% | 4d ago | 74% |  |
| 131 | [ ] | Heavy Rain (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 89% | today | 93% |  |
| 132 | [ ] | Driving Rogue (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 92% | 8d ago | 86% |  |
| 133 | [ ] | ENA: Dream BBQ (STEAM) | 10 | 20 | 50% (last 20) | Does not open (45%) | 83% | 1d ago | 62% |  |
| 134 | [ ] | Fallout 3 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (43%) | 89% | today | 85% |  |
| 135 | [ ] | A Plague Tale: Innocence (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | 75% | 16d ago | 73% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 136 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | 81% | 4d ago | 83% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 137 | [ ] | Chained Echoes (GOG) | 14 | 20 | 70% (last 20) | Does not open (60%) | 60% | 1d ago | n/a |  |
| 138 | [ ] | Call of Duty: World at War (STEAM) | 13 | 20 | 65% (last 20) | Does not open (45%) | 87% | today | 71% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 139 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 85% | 2d ago | 85% |  |
| 140 | [ ] | PowerWash Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (81%) | 78% | 2d ago | 100% |  |
| 141 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (86%) | 94% | today | 94% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 142 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (47%) | 91% | 5d ago | 85% |  |
| 143 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 62% | 2d ago | 67% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 144 | [ ] | Oxygen Not Included (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 62% | today | 80% |  |
| 145 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | 87% | 1d ago | n/a | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 146 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (82%) | 94% | 3d ago | n/a | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 147 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | 64% | today | 54% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 148 | [ ] | Max Payne (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (46%) | 82% | 1d ago | 71% |  |
| 149 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 82% | 3d ago | 80% |  |
| 150 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (81%) | 76% | 13d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 151 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | 77% | 2d ago | n/a | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 152 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 76% | 8d ago | 79% |  |
| 153 | [ ] | Rivals of Aether II (STEAM) | 15 | 20 | 75% (last 20) | Does not open (55%) | 61% | 1d ago | 8% (drop) | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 154 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 82% | 2d ago | 76% |  |
| 155 | [ ] | Sonic Lost World (STEAM) | 11 | 20 | 55% (last 20) | No graphics (65%) | 79% | today | 81% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 156 | [ ] | Street Fighter™ 6 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (81%) | 80% | 3d ago | 77% |  |
| 157 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 68% | 2d ago | 43% (drop) |  |
| 158 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (62%) | 83% | 10d ago | n/a | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 159 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | 90% | 14d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 160 | [ ] | Stellar Blade™ (STEAM) | 14 | 20 | 70% (last 20) | No graphics (43%) | 81% | 5d ago | 82% |  |
| 161 | [ ] | Gambonanza (STEAM) | 13 | 20 | 65% (last 20) | Does not open (60%) | 92% | 2d ago | 93% |  |
| 162 | [ ] | Gothic 1 Classic (STEAM) | 12 | 20 | 60% (last 20) | Does not open (61%) | 78% | 6d ago | 55% (drop) |  |
| 163 | [ ] | ABZU (EPIC) | 10 | 20 | 50% (last 20) | Does not open (86%) | 87% | 6d ago | 80% |  |
| 164 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 70% | 1d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 165 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 73% | 6d ago | n/a | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 166 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 88% | 1d ago | 86% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 167 | [ ] | Tabletop Simulator (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 69% | 1d ago | 79% |  |
| 168 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 81% | 6d ago | 94% |  |
| 169 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 11 | 20 | 55% (last 20) | Does not open (59%) | 73% | 12d ago | 71% |  |
| 170 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (57%) | 67% | 13d ago | n/a | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 171 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (64%) | 62% | 4d ago | n/a | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 172 | [ ] | Control Ultimate Edition (GOG) | 13 | 20 | 65% (last 20) | Does not open (76%) | 87% | 4d ago | 79% |  |
| 173 | [ ] | Limbus Company (STEAM) | 12 | 20 | 60% (last 20) | Does not open (86%) | 84% | 1d ago | 95% |  |
| 174 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (84%) | 95% | today | 93% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 175 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (70%) | 76% | 7d ago | n/a | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 176 | [ ] | State of Decay: Year-One (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 80% | 1d ago | 76% |  |
| 177 | [ ] | Stumble Guys (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 72% | today | 62% |  |
| 178 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (59%) | 92% | 10d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 179 | [ ] | One-armed robber (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (65%) | 70% | 7d ago | 55% |  |
| 180 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 65% | 1d ago | 33% (drop) | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 181 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | 73% | 7d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 182 | [ ] | Unturned (STEAM) | 12 | 20 | 60% (last 20) | Does not open (44%) | 71% | 4d ago | 80% |  |
| 183 | [ ] | Mortal Kombat 11 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 76% | 1d ago | 92% |  |
| 184 | [ ] | Counter-Strike:Global Offensive (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 79% | 5d ago | 81% |  |
| 185 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 91% | 25d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 186 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 88% | 3d ago | 85% |  |
| 187 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 92% | 5d ago | n/a |  |
| 188 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (85%) | 91% | 15d ago | 83% |  |
| 189 | [ ] | Subnautica 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (55%) | 62% | 4d ago | n/a | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 190 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 86% | 4d ago | n/a | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 191 | [ ] | Capcom Arcade Stadium (STEAM) | 15 | 20 | 75% (last 20) | Does not open (82%) | 76% | 2d ago | 85% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 192 | [ ] | Digimon Survive (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (77%) | 91% | 3d ago | 82% |  |
| 193 | [ ] | Dishonored 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 81% | today | 67% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 194 | [ ] | The Witcher: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 67% | 8d ago | 90% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 195 | [ ] | Escape from Duckov (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (71%) | 93% | 2d ago | 97% |  |
| 196 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (56%) | 67% | 9d ago | 75% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 197 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (72%) | 90% | 3d ago | n/a | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 198 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 20 | 80% (last 20) | Does not open (47%) | 69% | 1d ago | 40% (drop) | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 199 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (62%) | 64% | 3d ago | 24% (drop) |  |
| 200 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (59%) | 66% | 5d ago | 55% |  |
| 201 | [ ] | My Summer Car (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | 81% | 1d ago | 83% |  |
| 202 | [ ] | Final Fantasy IV (3D Remake) (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 95% | 4d ago | 100% |  |
| 203 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | 94% | 4d ago | n/a | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 204 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 87% | 9d ago | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 205 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (69%) | 92% | 20d ago | n/a | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 206 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (65%) | 100% | 10d ago | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 207 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (54%) | 78% | 18d ago | n/a | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 208 | [ ] | Supermarket Together (STEAM) | 15 | 20 | 75% (last 20) | Does not open (71%) | 63% | 10d ago | 71% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 209 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 73% | 4d ago | n/a | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 210 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 96% | today | 100% |  |
| 211 | [ ] | TurretGirls (STEAM) | 11 | 20 | 55% (last 20) | No graphics (75%) | 91% | today | 86% |  |
| 212 | [ ] | BioShock 2 Remastered (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 83% | today | 82% |  |
| 213 | [ ] | Moonring (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 93% | 2d ago | 88% |  |
| 214 | [ ] | Battle Brothers (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 86% | 2d ago | 88% |  |
| 215 | [ ] | Darksiders (STEAM) | 13 | 20 | 65% (last 20) | Does not open (68%) | 80% | 21d ago | 75% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 216 | [ ] | Lucid Blocks (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 61% | 2d ago | 53% |  |
| 217 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 79% | 3d ago | 77% |  |
| 218 | [ ] | Undisputed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 64% | 7d ago | n/a | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 219 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 80% | 3d ago | n/a |  |
| 220 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (92%) | 80% | 28d ago | n/a |  |
| 221 | [ ] | Invisible, Inc. (STEAM) | 15 | 20 | 75% (last 20) | Does not open (63%) | 75% | 16d ago | n/a |  |
| 222 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 71% | 18d ago | 60% |  |
| 223 | [ ] | Ultimate Custom Night (STEAM) | 14 | 20 | 70% (last 20) | No graphics (68%) | 65% | 17d ago | n/a | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 224 | [ ] | Return to Monkey Island (STEAM) | 14 | 20 | 70% (last 20) | No graphics (65%) | 71% | 8d ago | 64% |  |
| 225 | [ ] | GOD EATER RESURRECTION (STEAM) | 14 | 20 | 70% (last 20) | Does not open (59%) | 71% | 1d ago | n/a |  |
| 226 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 75% | 3d ago | n/a | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 227 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (53%) | 61% | today | 74% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 228 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (44%) | 85% | 8d ago | n/a |  |
| 229 | [ ] | MX Bikes (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 93% | 2d ago | 91% |  |
| 230 | [ ] | Resident Evil Revelations 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (42%) | 85% | 1d ago | 81% |  |
| 231 | [ ] | GUILTY GEAR Xrd REV 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (86%) | 83% | today | 60% |  |
| 232 | [ ] | Jade Empire: Special Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 74% | 6d ago | n/a | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 233 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (42%) | 74% | 10d ago | n/a | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 234 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 92% | 5d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 235 | [ ] | SnowRunner (STEAM) | 13 | 20 | 65% (last 20) | Does not open (96%) | 79% | 6d ago | 70% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 236 | [ ] | Zero Escape: The Nonary Games (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 65% | 5d ago | 67% |  |
| 237 | [ ] | Secrets of Grindea (STEAM) | 11 | 20 | 55% (last 20) | Does not open (48%) | 73% | 1d ago | 82% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 238 | [ ] | Mafia II: Definitive Edition (GOG) | 18 | 20 | 90% (last 20) | Does not open (53%) | 60% | today | 70% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 239 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 20 | 80% (last 20) | Does not open (82%) | 65% | 22d ago | n/a | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 240 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (54%) | 64% | today | n/a |  |
| 241 | [ ] | Cat Mail Co. (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 86% | 1d ago | 77% |  |
| 242 | [ ] | Deus Ex™ GOTY Edition (GOG) | 12 | 20 | 60% (last 20) | No graphics (44%) | 92% | 15d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 243 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 68% | 6d ago | n/a |  |
| 244 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 90% | today | 92% |  |
| 245 | [ ] | Dying Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (86%) | 74% | today | 57% |  |
| 246 | [ ] | Trailmakers (STEAM) | 10 | 20 | 50% (last 20) | Does not open (44%) | 93% | today | 92% |  |
| 247 | [ ] | Serious Sam 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (63%) | 89% | 2d ago | n/a |  |
| 248 | [ ] | Bongo Cat (STEAM) | 15 | 20 | 75% (last 20) | Does not open (92%) | 68% | 9d ago | 40% (drop) | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 249 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 13 | 20 | 65% (last 20) | No graphics (37%) | 86% | 4d ago | n/a | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 250 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (83%) | 75% | 7d ago | 69% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 251 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (71%) | 75% | today | n/a |  |
| 252 | [ ] | PAYDAY: The Heist (STEAM) | 13 | 20 | 65% (last 20) | Does not open (75%) | 73% | 8d ago | n/a |  |
| 253 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (100%) | 71% | today | n/a |  |
| 254 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 89% | 7d ago | n/a |  |
| 255 | [ ] | Revolution Idle (STEAM) | 11 | 20 | 55% (last 20) | Does not open (43%) | 83% | today | n/a |  |
| 256 | [ ] | Hero Siege (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (50%) | 77% | 4d ago | 93% |  |
| 257 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 80% | 1d ago | 70% |  |
| 258 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (41%) | 92% | 1d ago | n/a |  |
| 259 | [ ] | Tales of Zestiria (STEAM) | 14 | 20 | 70% (last 20) | Does not open (79%) | 67% | 20d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 260 | [ ] | Capcom Fighting Collection (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 78% | 6d ago | n/a | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 261 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (95%) | 94% | 6d ago | 89% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 262 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (45%) | 67% | 1d ago | n/a |  |
| 263 | [ ] | Disgaea 4 Complete+ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (43%) | 92% | today | n/a | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 264 | [ ] | Sacred Gold (STEAM) | 13 | 20 | 65% (last 20) | Does not open (91%) | 70% | 1d ago | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 265 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 12 | 20 | 60% (last 20) | Does not open (57%) | 64% | 10d ago | n/a | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 266 | [ ] | 12 is Better Than 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 85% | 10d ago | n/a |  |
| 267 | [ ] | Big Walk (STEAM) | 11 | 20 | 55% (last 20) | Does not open (66%) | 68% | 12d ago | 46% (drop) |  |
| 268 | [ ] | Hitman: Absolution (GOG) | 11 | 20 | 55% (last 20) | Does not open (85%) | 75% | today | n/a |  |
| 269 | [ ] | Hatred (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 88% | 7d ago | n/a |  |
| 270 | [ ] | Football Manager 2024 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (91%) | 65% | 7d ago | 44% (drop) |  |
| 271 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 93% | 3d ago | 86% |  |
| 272 | [ ] | Ghostwire Tokyo (EPIC) | 14 | 20 | 70% (last 20) | Does not open (91%) | 70% | today | 45% (drop) |  |
| 273 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 14 | 20 | 70% (last 20) | Does not open (85%) | 75% | 7d ago | n/a | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 274 | [ ] | Timberborn (STEAM) | 13 | 20 | 65% (last 20) | No graphics (62%) | 86% | 12d ago | n/a |  |
| 275 | [ ] | Allumeria (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 73% | 5d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 276 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 77% | 5d ago | n/a |  |
| 277 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 60% | 9d ago | 59% |  |
| 278 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 62% | 2d ago | 45% |  |
| 279 | [ ] | Sons Of The Forest (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 77% | today | 73% |  |
| 280 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 12 | 20 | 60% (last 20) | Does not open (92%) | 62% | 6d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 281 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (50%) | 76% | 7d ago | n/a | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 282 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 73% | 6d ago | 69% |  |
| 283 | [ ] | CRUEL (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 80% | today | n/a | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 284 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 90% | today | 100% |  |
| 285 | [ ] | Spark the Electric Jester (STEAM) | 14 | 20 | 70% (last 20) | Does not open (58%) | 67% | 10d ago | n/a | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 286 | [ ] | AER Memories of Old (EPIC) | 12 | 20 | 60% (last 20) | Does not open (85%) | 100% | today | n/a |  |
| 287 | [ ] | BATTLETECH (STEAM) | 11 | 20 | 55% (last 20) | Does not open (43%) | 94% | 2d ago | n/a |  |
| 288 | [ ] | Antichamber (STEAM) | 11 | 20 | 55% (last 20) | Does not open (33%) | 82% | 4d ago | n/a |  |
| 289 | [ ] | Forgive Me Father (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 62% | 1d ago | n/a |  |
| 290 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 73% | 1d ago | n/a |  |
| 291 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 85% | 5d ago | 70% |  |
| 292 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | No graphics (54%) | 69% | today | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 293 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 67% | 31d ago | n/a |  |
| 294 | [ ] | Hylics (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (64%) | 97% | 2d ago | n/a |  |
| 295 | [ ] | No Socks RPG (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (90%) | 93% | today | 90% |  |
| 296 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 60% | 5d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 297 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (44%) | 71% | 43d ago | n/a |  |
| 298 | [ ] | LET IT DIE (STEAM) | 11 | 20 | 55% (last 20) | Does not open (88%) | 64% | today | n/a |  |
| 299 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 60% | 3d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 300 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (92%) | 89% | 10d ago | n/a |  |
| 301 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (70%) | 62% | 3d ago | n/a |  |
| 302 | [ ] | Assassin's Creed Odyssey (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 61% | 8d ago | 62% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 303 | [ ] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (45%) | 71% | today | 56% |  |
| 304 | [ ] | Pinball FX Classic (STEAM) | 10 | 20 | 50% (last 20) | Does not open (79%) | 94% | 10d ago | n/a |  |
| 305 | [ ] | Subnautica: Below Zero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 77% | 6d ago | 60% |  |
| 306 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 62% | today | n/a | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 307 | [ ] | Intravenous (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 76% | 6d ago | 73% |  |
| 308 | [ ] | Need for Speed™ Unbound (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 62% | 18d ago | n/a | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 309 | [ ] | Legend of Grimrock 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 92% | 8d ago | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 310 | [ ] | The Stanley Parable (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 69% | 1d ago | n/a |  |
| 311 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | 90% | 1d ago | n/a |  |
| 312 | [ ] | SILENT HILL 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (58%) | 74% | today | 90% |  |
| 313 | [ ] | Shift At Midnight (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | 84% | 9d ago | 83% |  |
| 314 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (52%) | 90% | 17d ago | n/a | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 315 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 95% | 3d ago | 100% |  |
| 316 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 73% | 8d ago | 70% |  |
| 317 | [ ] | GRANDIA II HD Remaster (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 75% | 18d ago | n/a |  |
| 318 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 70% | 8d ago | n/a |  |
| 319 | [ ] | Killing Floor (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (100%) | 85% | 7d ago | n/a |  |
| 320 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 60% | 2d ago | n/a |  |
| 321 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 87% | 5d ago | 85% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 322 | [ ] | Decktamer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 85% | today | n/a |  |
| 323 | [ ] | Haydee (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 81% | today | n/a |  |
| 324 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 93% | today | 92% |  |
| 325 | [ ] | Sid Meier's Civilization VI (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 73% | 12d ago | 42% (drop) |  |

## Recently recovered (477)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Grim Dawn (STEAM) | 517 | 2026-11-08 | 580 | 66% |  |
| 2 | [x] | FINAL FANTASY RESONANCE (STEAM) | 424 | 2026-10-24 | 955 | 78% |  |
| 3 | [x] | Half-Life (STEAM) | 352 | 2026-11-09 | 624 | 71% |  |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 258 | 2026-11-14 | 407 | 61% |  |
| 5 | [x] | Alan Wake (STEAM) | 239 | 2026-11-14 | 263 | 38% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 6 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 230 | 2026-11-09 | 323 | 89% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 7 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 226 | 2026-10-19 | 286 | 68% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 8 | [x] | MONSTER HUNTER RISE (STEAM) | 215 | 2026-11-09 | 515 | 60% |  |
| 9 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 213 | 2026-11-09 | 256 | 63% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 10 | [x] | BeamNG.drive (STEAM) | 203 | 2026-11-09 | 245 | 78% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 11 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 202 | 2026-11-09 | 356 | 74% |  |
| 12 | [x] | Devil May Cry HD Collection (STEAM) | 201 | 2026-10-19 | 292 | 81% |  |
| 13 | [x] | Call of Duty: Black Ops (STEAM) | 196 | 2026-11-13 | 221 | 21% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 14 | [x] | OMORI (STEAM) | 190 | 2026-11-09 | 235 | 73% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 15 | [x] | DRAGON BALL FighterZ (STEAM) | 179 | 2026-11-01 | 217 | 78% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 16 | [x] | DREDGE (EPIC) | 170 | 2026-11-09 | 212 | 64% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 17 | [x] | Spelunky 2 (STEAM) | 168 | 2026-11-01 | 203 | 71% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 18 | [x] | Sid Meier's Civilization V (STEAM) | 163 | 2026-11-10 | 174 | 62% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 19 | [x] | BioShock (STEAM) | 151 | 2026-11-09 | 300 | 75% |  |
| 20 | [x] | Geometry Dash (STEAM) | 149 | 2026-11-11 | 441 | 52% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 21 | [x] | Prototype (STEAM) | 140 | 2026-11-11 | 205 | 54% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 22 | [x] | Team Fortress 2 (STEAM) | 136 | 2026-11-09 | 232 | 76% |  |
| 23 | [x] | Burnout Paradise: The Ultimate Box (STEAM) | 135 | 2026-10-16 | 239 | 70% |  |
| 24 | [x] | Castlevania Advance Collection (STEAM) | 130 | 2026-11-09 | 205 | 89% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 25 | [x] | Minecraft Dungeons II (STEAM) | 129 | 2026-11-09 | 148 | 68% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 26 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 127 | 2026-11-09 | 170 | 63% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 27 | [x] | Counter-Strike (STEAM) | 126 | 2026-11-11 | 208 | 44% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 28 | [x] | Mirror's Edge (STEAM) | 125 | 2026-11-09 | 178 | 73% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 29 | [x] | Call of Duty: Black Ops III (STEAM) | 122 | 2026-10-18 | 251 | 79% |  |
| 30 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 121 | 2026-10-18 | 178 | 77% |  |
| 31 | [x] | Assassin's Creed II (STEAM) | 117 | 2026-11-10 | 122 | 64% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 32 | [x] | Aniimo (STEAM) | 112 | 2026-11-09 | 151 | 83% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 33 | [x] | The Witcher: Enhanced Edition (STEAM) | 107 | 2026-11-09 | 125 | 67% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 34 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 104 | 2026-11-09 | 144 | 95% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 35 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 104 | 2026-11-15 | 142 | 60% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 36 | [x] | Cave Story+ (STEAM) | 104 | 2026-11-09 | 115 | 83% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 37 | [x] | Moonstone Island (STEAM) | 99 | 2026-11-09 | 131 | 80% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 38 | [x] | Happy Wheels (STEAM) | 97 | 2026-11-09 | 117 | 73% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 39 | [x] | Caravan SandWitch (EPIC) | 93 | 2026-11-09 | 157 | 70% |  |
| 40 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 90 | 2026-11-09 | 117 | 94% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 41 | [x] | Catherine Classic (STEAM) | 89 | 2026-11-09 | 167 | 66% |  |
| 42 | [x] | Quake (STEAM) | 86 | 2026-11-09 | 251 | 81% |  |
| 43 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 86 | 2026-11-09 | 139 | 68% |  |
| 44 | [x] | Hi-Fi RUSH (STEAM) | 86 | 2026-11-11 | 119 | 44% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 45 | [x] | DOOM 3: BFG Edition (STEAM) | 85 | 2026-11-09 | 125 | 72% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 46 | [x] | Ultra Street Fighter IV (STEAM) | 83 | 2026-10-17 | 181 | 71% |  |
| 47 | [x] | Cry of Fear (STEAM) | 83 | 2026-10-18 | 166 | 75% |  |
| 48 | [x] | Vital Shell (STEAM) | 81 | 2026-11-09 | 130 | 84% |  |
| 49 | [x] | Age of Empires II: Definitive Edition (STEAM) | 80 | 2026-11-10 | 96 | 62% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 50 | [x] | FINAL FANTASY XIII-2 (STEAM) | 80 | 2026-11-09 | 83 | 73% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 51 | [x] | Psychonauts (STEAM) | 78 | 2026-11-09 | 145 | 95% |  |
| 52 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 78 | 2026-10-18 | 132 | 97% |  |
| 53 | [x] | STEINS;GATE (STEAM) | 76 | 2026-11-09 | 109 | 94% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 54 | [x] | Don't Starve Together (STEAM) | 74 | 2026-10-16 | 156 | 77% |  |
| 55 | [x] | Ballionaire (STEAM) | 74 | 2026-11-09 | 123 | 84% |  |
| 56 | [x] | Brawlhalla (STEAM) | 73 | 2026-11-09 | 145 | 73% |  |
| 57 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 73 | 2026-11-09 | 113 | 87% |  |
| 58 | [x] | The Sims™ 4 (STEAM) | 71 | 2026-11-09 | 93 | 73% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 59 | [x] | Disgaea 5 Complete (STEAM) | 71 | 2026-11-09 | 83 | 88% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 60 | [x] | Sovereign Tower (STEAM) | 70 | 2026-11-09 | 124 | 74% |  |
| 61 | [x] | Cyberpunk 2077 (GOG) | 70 | 2026-11-09 | 92 | 70% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 62 | [x] | Stardew Valley (GOG) | 69 | 2026-11-11 | 121 | 73% |  |
| 63 | [x] | Spyro™ Reignited Trilogy (STEAM) | 69 | 2026-11-09 | 108 | 76% |  |
| 64 | [x] | Need for Speed: Hot Pursuit (STEAM) | 69 | 2026-11-09 | 104 | 81% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 65 | [x] | Bayonetta (STEAM) | 68 | 2026-10-18 | 208 | 84% |  |
| 66 | [x] | Dota 2 (STEAM) | 68 | 2026-11-09 | 102 | 72% |  |
| 67 | [x] | Fable - The Lost Chapters (STEAM) | 67 | 2026-11-09 | 105 | 86% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 68 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 67 | 2026-11-09 | 104 | 83% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 69 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 67 | 2026-11-15 | 92 | 60% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 70 | [x] | Diablo® IV (STEAM) | 67 | 2026-11-11 | 79 | 64% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 71 | [x] | American Truck Simulator (STEAM) | 66 | 2026-11-09 | 110 | 78% |  |
| 72 | [x] | MIO: Memories in Orbit (STEAM) | 65 | 2026-11-09 | 121 | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 73 | [x] | Hogwarts Legacy (EPIC) | 64 | 2026-11-09 | 97 | 65% |  |
| 74 | [x] | Fallout (STEAM) | 63 | 2026-11-09 | 98 | 69% |  |
| 75 | [x] | Order of the Sinking Star (STEAM) | 63 | 2026-11-09 | 92 | 67% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 76 | [x] | Gunfire Reborn (STEAM) | 63 | 2026-11-09 | 69 | 87% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 77 | [x] | Don't Starve (STEAM) | 62 | 2026-10-16 | 156 | 81% |  |
| 78 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 62 | 2026-11-09 | 87 | 75% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 79 | [x] | Poppy Playtime (STEAM) | 61 | 2026-11-09 | 104 | 71% |  |
| 80 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 61 | 2026-11-11 | 79 | 50% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 81 | [x] | Firewatch (STEAM) | 60 | 2026-11-10 | 117 | 69% |  |
| 82 | [x] | eFootball™ (STEAM) | 60 | 2026-11-09 | 88 | 65% |  |
| 83 | [x] | Borderlands 3 (STEAM) | 60 | 2026-11-09 | 86 | 90% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 84 | [x] | Borderlands: The Pre-Sequel (STEAM) | 59 | 2026-11-09 | 95 | 66% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 85 | [x] | Darksiders (STEAM) | 58 | 2026-11-09 | 73 | 80% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 86 | [x] | Deskrawl: Idle ARPG (STEAM) | 58 | 2026-11-09 | 72 | 83% | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 87 | [x] | Mini Motorways (STEAM) | 57 | 2026-11-09 | 97 | 70% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 88 | [x] | Call of Juarez Gunslinger (STEAM) | 57 | 2026-11-09 | 72 | 81% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 89 | [x] | A Plague Tale: Innocence (STEAM) | 57 | 2026-11-09 | 60 | 75% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 90 | [x] | Sol Cesto (EPIC) | 56 | 2026-11-09 | 57 | 77% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 91 | [x] | Until Then (STEAM) | 55 | 2026-10-17 | 90 | 81% |  |
| 92 | [x] | Starbound (STEAM) | 55 | 2026-11-09 | 88 | 78% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 93 | [x] | TBH: Task Bar Hero (STEAM) | 55 | 2026-11-09 | 88 | 80% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 94 | [x] | Call of Duty: World at War (STEAM) | 55 | 2026-11-09 | 79 | 87% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 95 | [x] | Sonic Generations (STEAM) | 55 | 2026-11-09 | 60 | 69% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 96 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 54 | 2026-10-25 | 101 | 66% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 97 | [x] | Grand Theft Auto V (EPIC) | 54 | 2026-11-09 | 60 | 78% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 98 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 53 | 2026-11-09 | 88 | 91% |  |
| 99 | [x] | Deadlock (STEAM) | 53 | 2026-10-16 | 75 | 87% |  |
| 100 | [x] | Dead Space (STEAM) | 53 | 2026-10-18 | 66 | 84% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 101 | [x] | Overwatch® (STEAM) | 53 | 2026-11-10 | 56 | 67% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 102 | [x] | Alex Kidd in Miracle World DX (EPIC) | 52 | 2026-11-09 | 60 | 65% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 103 | [x] | Sonic Adventure DX (STEAM) | 51 | 2026-10-17 | 89 | 68% |  |
| 104 | [x] | Okami HD (STEAM) | 50 | 2026-11-09 | 94 | 91% |  |
| 105 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 50 | 2026-11-09 | 86 | 78% |  |
| 106 | [x] | Last Epoch (STEAM) | 50 | 2026-11-09 | 75 | 79% |  |
| 107 | [x] | MudRunner (STEAM) | 48 | 2026-10-24 | 107 | 67% |  |
| 108 | [x] | Darkest Dungeon® (EPIC) | 48 | 2026-11-09 | 89 | 79% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 109 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 48 | 2026-11-09 | 83 | 57% |  |
| 110 | [x] | Oxygen Not Included (STEAM) | 48 | 2026-11-11 | 82 | 62% |  |
| 111 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 48 | 2026-11-09 | 55 | 90% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 112 | [x] | Abiotic Factor (STEAM) | 47 | 2026-10-18 | 81 | 74% |  |
| 113 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 47 | 2026-11-09 | 78 | 48% |  |
| 114 | [x] | Big Walk (STEAM) | 47 | 2026-11-09 | 72 | 68% |  |
| 115 | [x] | Heroes of Might & Magic III - HD Edition (STEAM) | 47 | 2026-11-14 | 62 | 64% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 116 | [x] | Moonlighter (EPIC) | 47 | 2026-11-09 | 51 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 117 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 46 | 2026-11-09 | 76 | 82% |  |
| 118 | [x] | Rivals of Aether II (STEAM) | 46 | 2026-11-09 | 65 | 61% | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 119 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 45 | 2026-10-19 | 90 | 71% |  |
| 120 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 45 | 2026-11-09 | 72 | 91% |  |
| 121 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 44 | 2026-11-13 | 61 | 63% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 122 | [x] | Sheepy: A Short Adventure (STEAM) | 44 | 2026-11-09 | 53 | 78% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 123 | [x] | Tomb Raider GOTY (GOG) | 43 | 2026-10-17 | 103 | 93% |  |
| 124 | [x] | Mortal Kombat X (STEAM) | 43 | 2026-10-17 | 75 | 92% |  |
| 125 | [x] | Sonic Lost World (STEAM) | 43 | 2026-11-09 | 62 | 79% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 126 | [x] | Forza Horizon 4 (STEAM) | 42 | 2026-11-09 | 58 | 62% | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 127 | [x] | Aggelos (STEAM) | 42 | 2026-11-09 | 57 | 94% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 128 | [x] | Rayman Origins (STEAM) | 40 | 2026-10-17 | 90 | 87% |  |
| 129 | [x] | Library Of Ruina (STEAM) | 40 | 2026-10-16 | 77 | 87% |  |
| 130 | [x] | Ace Attorney Investigations Collection (STEAM) | 40 | 2026-11-09 | 70 | 88% |  |
| 131 | [x] | Tomb Raider: Anniversary (STEAM) | 40 | 2026-11-09 | 64 | 63% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 132 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 39 | 2026-11-09 | 71 | 85% |  |
| 133 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 39 | 2026-11-09 | 60 | 76% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 134 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-11-09 | 40 | 77% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 135 | [x] | Digimon World: Next Order (STEAM) | 38 | 2026-11-09 | 75 | 82% |  |
| 136 | [x] | FINAL FANTASY VII (2013) (STEAM) | 38 | 2026-11-09 | 55 | 67% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 137 | [x] | Dead by Daylight (STEAM) | 38 | 2026-11-09 | 42 | 88% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 138 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 38 | 2026-11-09 | 40 | 83% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 139 | [x] | PROTOTYPE 2 (STEAM) | 37 | 2026-10-18 | 85 | 68% |  |
| 140 | [x] | Life is Strange™ (STEAM) | 37 | 2026-10-17 | 78 | 82% |  |
| 141 | [x] | Amnesia: The Dark Descent (STEAM) | 37 | 2026-11-09 | 73 | 79% |  |
| 142 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 37 | 2026-11-09 | 69 | 91% |  |
| 143 | [x] | Sonic Origins (STEAM) | 37 | 2026-11-09 | 69 | 82% |  |
| 144 | [x] | Age of Empires II (2013) (STEAM) | 37 | 2026-11-09 | 62 | 66% |  |
| 145 | [x] | Street Fighter™ 6 (STEAM) | 37 | 2026-11-09 | 61 | 80% |  |
| 146 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 37 | 2026-11-09 | 50 | 85% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 147 | [x] | Russian Fishing 4 (STEAM) | 37 | 2026-11-09 | 43 | 90% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 148 | [x] | CrossCode (GOG) | 37 | 2026-11-09 | 40 | 76% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 149 | [x] | Teardown (STEAM) | 36 | 2026-10-17 | 83 | 80% |  |
| 150 | [x] | Tales of ARISE (STEAM) | 36 | 2026-10-16 | 78 | 90% |  |
| 151 | [x] | Capcom Arcade Stadium (STEAM) | 36 | 2026-11-09 | 46 | 76% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 152 | [x] | Rogue Legacy (STEAM) | 35 | 2026-10-17 | 83 | 89% |  |
| 153 | [x] | Little Nightmares (STEAM) | 35 | 2026-10-16 | 79 | 75% |  |
| 154 | [x] | POSTAL 2 (GOG) | 35 | 2026-11-09 | 70 | 92% |  |
| 155 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 35 | 2026-11-09 | 65 | 85% |  |
| 156 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 35 | 2026-11-09 | 61 | 73% |  |
| 157 | [x] | XCOM 2 (STEAM) | 35 | 2026-11-09 | 59 | 87% |  |
| 158 | [x] | Elite Dangerous (STEAM) | 35 | 2026-11-09 | 38 | 60% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 159 | [x] | Death Road to Canada (STEAM) | 34 | 2026-10-17 | 95 | 81% |  |
| 160 | [x] | Cobalt Core (STEAM) | 34 | 2026-10-18 | 93 | 90% |  |
| 161 | [x] | SurrounDead (STEAM) | 34 | 2026-11-09 | 66 | 93% |  |
| 162 | [x] | The Bazaar (STEAM) | 34 | 2026-11-09 | 62 | 74% |  |
| 163 | [x] | Rocket League (STEAM) | 34 | 2026-10-17 | 59 | 68% |  |
| 164 | [x] | Hero Siege (STEAM) | 34 | 2026-11-09 | 57 | 77% |  |
| 165 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 34 | 2026-11-09 | 55 | 90% |  |
| 166 | [x] | Need for Speed™ Rivals (STEAM) | 34 | 2026-11-10 | 45 | 73% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 167 | [x] | Romestead (STEAM) | 34 | 2026-11-09 | 44 | 62% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 168 | [x] | Journey (STEAM) | 33 | 2026-10-27 | 72 | 68% |  |
| 169 | [x] | State of Decay: Year-One (STEAM) | 33 | 2026-10-18 | 68 | 80% |  |
| 170 | [x] | Ultimate Chicken Horse (STEAM) | 33 | 2026-10-23 | 68 | 78% |  |
| 171 | [x] | Hearts of Iron IV (STEAM) | 33 | 2026-11-09 | 63 | 75% |  |
| 172 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 33 | 2026-11-11 | 60 | 32% |  |
| 173 | [x] | Gauntlet™  (STEAM) | 33 | 2026-11-11 | 47 | 50% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 174 | [x] | Dishonored - Definitive Edition (EPIC) | 32 | 2026-10-17 | 81 | 80% |  |
| 175 | [x] | Salt and Sanctuary (STEAM) | 32 | 2026-10-18 | 74 | 84% |  |
| 176 | [x] | Torchlight II (STEAM) | 32 | 2026-10-20 | 74 | 88% |  |
| 177 | [x] | Being a DIK (STEAM) | 32 | 2026-11-09 | 59 | 60% |  |
| 178 | [x] | Stumble Guys (STEAM) | 32 | 2026-10-18 | 58 | 72% |  |
| 179 | [x] | Max Payne (STEAM) | 32 | 2026-11-09 | 57 | 82% |  |
| 180 | [x] | Earthion (STEAM) | 32 | 2026-11-09 | 53 | 100% |  |
| 181 | [x] | SnowRunner (STEAM) | 32 | 2026-11-09 | 46 | 79% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 182 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-11-09 | 41 | 83% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 183 | [x] | COCOON (STEAM) | 31 | 2026-11-09 | 66 | 86% |  |
| 184 | [x] | Owlboy (STEAM) | 31 | 2026-11-02 | 64 | 54% |  |
| 185 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 31 | 2026-11-09 | 55 | 71% |  |
| 186 | [x] | Counter-Strike:Global Offensive (STEAM) | 31 | 2026-11-09 | 51 | 79% |  |
| 187 | [x] | Red Dead Redemption (STEAM) | 31 | 2026-11-09 | 34 | 62% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 188 | [x] | Bloodstained: Curse of the Moon (STEAM) | 30 | 2026-10-16 | 76 | 76% |  |
| 189 | [x] | Sable (EPIC) | 30 | 2026-10-18 | 70 | 60% |  |
| 190 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 30 | 2026-11-09 | 67 | 73% |  |
| 191 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 30 | 2026-11-09 | 60 | 85% |  |
| 192 | [x] | Resident Evil Village (STEAM) | 30 | 2026-11-09 | 53 | 90% |  |
| 193 | [x] | Prince of Persia: The Sands of Time (STEAM) | 30 | 2026-11-09 | 50 | 80% |  |
| 194 | [x] | Secrets of Grindea (STEAM) | 30 | 2026-11-09 | 48 | 73% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 195 | [x] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 30 | 2026-11-14 | 35 | 70% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 196 | [x] | PlateUp! (STEAM) | 29 | 2026-10-16 | 64 | 81% |  |
| 197 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 2026-10-17 | 56 | 83% |  |
| 198 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 29 | 2026-11-09 | 55 | 82% |  |
| 199 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 29 | 2026-11-09 | 50 | 86% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 200 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 29 | 2026-11-09 | 49 | 66% |  |
| 201 | [x] | Guildrun Demo (STEAM) | 29 | 2026-11-09 | 46 | 69% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 202 | [x] | Yakuza: Like a Dragon (STEAM) | 29 | 2026-11-09 | 46 | 63% |  |
| 203 | [x] | Nioh: Complete Edition (STEAM) | 29 | 2026-11-09 | 39 | 90% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 204 | [x] | Deponia (STEAM) | 28 | 2026-11-09 | 53 | 69% |  |
| 205 | [x] | Aethermancer (STEAM) | 28 | 2026-10-18 | 50 | 85% |  |
| 206 | [x] | Heavy Rain (STEAM) | 28 | 2026-11-09 | 48 | 89% |  |
| 207 | [x] | Gambonanza (STEAM) | 28 | 2026-11-09 | 47 | 92% |  |
| 208 | [x] | Tower and Sword of Succubus (STEAM) | 28 | 2026-11-09 | 43 | 80% |  |
| 209 | [x] | Supermarket Together (STEAM) | 28 | 2026-11-09 | 40 | 63% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 210 | [x] | Metro: Last Light Complete Edition (STEAM) | 28 | 2026-11-10 | 34 | 67% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 211 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 27 | 2026-11-09 | 49 | 96% |  |
| 212 | [x] | Capcom Fighting Collection 2 (STEAM) | 27 | 2026-11-09 | 44 | 78% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 213 | [x] | Dead Rising 2 (STEAM) | 27 | 2026-11-09 | 43 | 62% |  |
| 214 | [x] | Digimon Survive (STEAM) | 27 | 2026-11-09 | 40 | 91% |  |
| 215 | [x] | Palia (STEAM) | 27 | 2026-11-09 | 39 | 79% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 216 | [x] | Ultimate Custom Night (STEAM) | 27 | 2026-11-09 | 37 | 65% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 217 | [x] | Gothic II: Gold Classic (STEAM) | 27 | 2026-11-09 | 36 | 67% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 218 | [x] | Subnautica 2 (STEAM) | 27 | 2026-11-15 | 32 | 62% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 219 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 26 | 2026-10-19 | 94 | 92% |  |
| 220 | [x] | Grand Theft Auto III (STEAM) | 26 | 2026-10-17 | 72 | 75% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 221 | [x] | Dying Light (EPIC) | 26 | 2026-10-17 | 61 | 74% |  |
| 222 | [x] | Monster Hunter Stories (STEAM) | 26 | 2026-10-17 | 61 | 80% |  |
| 223 | [x] | Frostpunk (STEAM) | 26 | 2026-11-09 | 52 | 73% |  |
| 224 | [x] | Resident Evil Revelations 2 (STEAM) | 26 | 2026-11-09 | 49 | 85% |  |
| 225 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 45 | 65% |  |
| 226 | [x] | Limbus Company (STEAM) | 26 | 2026-11-09 | 40 | 84% |  |
| 227 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 26 | 2026-11-09 | 38 | 67% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 228 | [x] | CRUEL (STEAM) | 26 | 2026-11-09 | 36 | 80% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 229 | [x] | Skullgirls 2nd Encore (STEAM) | 25 | 2026-11-10 | 60 | 64% |  |
| 230 | [x] | Prince of Persia (GOG) | 25 | 2026-11-09 | 44 | 83% |  |
| 231 | [x] | Battle Brothers (STEAM) | 25 | 2026-11-09 | 44 | 86% |  |
| 232 | [x] | Counter-Strike: Condition Zero (STEAM) | 25 | 2026-11-11 | 43 | 39% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 233 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-09 | 32 | 91% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 234 | [x] | Tales of Zestiria (STEAM) | 25 | 2026-11-09 | 31 | 67% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 235 | [x] | Northgard: Definitive Edition (STEAM) | 25 | 2026-11-09 | 28 | 90% | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 236 | [x] | BioShock™ (GOG) | 24 | 2026-10-18 | 61 | 82% |  |
| 237 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 58 | 92% |  |
| 238 | [x] | Mirror's Edge™ (GOG) | 24 | 2026-11-13 | 45 | 57% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 239 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 24 | 2026-11-09 | 43 | 71% |  |
| 240 | [x] | Opus Magnum (STEAM) | 24 | 2026-11-09 | 39 | 92% |  |
| 241 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 24 | 2026-11-09 | 37 | 71% |  |
| 242 | [x] | Ratatan (STEAM) | 24 | 2026-11-09 | 37 | 97% |  |
| 243 | [x] | Jade Empire: Special Edition (GOG) | 24 | 2026-11-09 | 31 | 74% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 244 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 24 | 2026-11-09 | 31 | 92% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 245 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 24 | 2026-11-09 | 30 | 75% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 246 | [x] | Crab Game (STEAM) | 24 | 2026-11-09 | 28 | 86% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 247 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 24 | 2026-11-09 | 28 | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 248 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 23 | 2026-10-20 | 52 | 88% |  |
| 249 | [x] | Chained Echoes (GOG) | 23 | 2026-11-08 | 49 | 60% |  |
| 250 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 46 | 88% |  |
| 251 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-11-09 | 45 | 89% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 252 | [x] | Lucid Blocks (STEAM) | 23 | 2026-11-09 | 43 | 61% |  |
| 253 | [x] | Football Manager 2024 (EPIC) | 23 | 2026-11-09 | 40 | 65% |  |
| 254 | [x] | Worms W.M.D (STEAM) | 23 | 2026-11-09 | 40 | 92% |  |
| 255 | [x] | Cat Mail Co. (STEAM) | 23 | 2026-11-09 | 39 | 86% |  |
| 256 | [x] | Moonlight Peaks (STEAM) | 23 | 2026-11-09 | 35 | 77% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 257 | [x] | Borderlands: The Pre-Sequel (EPIC) | 23 | 2026-11-09 | 33 | 64% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 258 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 94% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 259 | [x] | Jade Empire: Special Edition (STEAM) | 23 | 2026-11-09 | 26 | 74% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 260 | [x] | WEBFISHING (STEAM) | 22 | 2026-10-17 | 53 | 88% |  |
| 261 | [x] | Goat Simulator (STEAM) | 22 | 2026-11-09 | 47 | 71% |  |
| 262 | [x] | Crazy Taxi (STEAM) | 22 | 2026-11-10 | 44 | 70% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 263 | [x] | Wizard of Legend (EPIC) | 22 | 2026-11-09 | 41 | 82% |  |
| 264 | [x] | Trailmakers (STEAM) | 22 | 2026-11-09 | 40 | 93% |  |
| 265 | [x] | Unturned (STEAM) | 22 | 2026-11-09 | 40 | 71% |  |
| 266 | [x] | My Summer Car (STEAM) | 22 | 2026-11-09 | 38 | 81% |  |
| 267 | [x] | Tabletop Simulator (STEAM) | 22 | 2026-11-09 | 37 | 69% |  |
| 268 | [x] | Deus Ex™ GOTY Edition (GOG) | 22 | 2026-11-09 | 35 | 92% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 269 | [x] | Return to Monkey Island (STEAM) | 22 | 2026-11-09 | 35 | 71% |  |
| 270 | [x] | Timberborn (STEAM) | 22 | 2026-11-09 | 33 | 86% |  |
| 271 | [x] | Dishonored 2 (STEAM) | 22 | 2026-11-09 | 32 | 81% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 272 | [x] | LET IT DIE (STEAM) | 22 | 2026-11-14 | 32 | 64% |  |
| 273 | [x] | SOMA (STEAM) | 22 | 2026-11-09 | 32 | 60% | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 274 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 60 | 98% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 275 | [x] | No Rest for the Wicked (STEAM) | 21 | 2026-10-19 | 47 | 77% |  |
| 276 | [x] | Slow Roads (STEAM) | 21 | 2026-10-22 | 47 | 81% |  |
| 277 | [x] | Control Ultimate Edition (GOG) | 21 | 2026-11-09 | 39 | 87% |  |
| 278 | [x] | Invisible, Inc. (STEAM) | 21 | 2026-11-09 | 37 | 75% |  |
| 279 | [x] | Cities: Skylines (STEAM) | 21 | 2026-11-13 | 31 | 60% | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 280 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 88% |  |
| 281 | [x] | CarX Street (STEAM) | 21 | 2026-11-09 | 27 | 87% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 282 | [x] | Tearscape (STEAM) | 21 | 2026-11-09 | 25 | 100% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 283 | [x] | Titan Quest Anniversary Edition (STEAM) | 20 | 2026-10-16 | 61 | 91% |  |
| 284 | [x] | CarX Drift Racing Online (STEAM) | 20 | 2026-10-16 | 55 | 82% |  |
| 285 | [x] | BlazBlue Centralfiction (STEAM) | 20 | 2026-10-17 | 54 | 84% |  |
| 286 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-11-09 | 38 | 100% |  |
| 287 | [x] | Pinball FX Classic (STEAM) | 20 | 2026-11-09 | 37 | 94% |  |
| 288 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 20 | 2026-11-09 | 30 | 87% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 289 | [x] | Party Animals (STEAM) | 20 | 2026-11-09 | 29 | 73% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 290 | [x] | Torchlight II (EPIC) | 20 | 2026-11-09 | 28 | 75% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 291 | [x] | Tyr (STEAM) | 20 | 2026-11-09 | 28 | 73% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 292 | [x] | Dead Island (STEAM) | 20 | 2026-11-09 | 25 | 92% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 293 | [x] | Saints Row IV (STEAM) | 19 | 2026-10-19 | 50 | 83% |  |
| 294 | [x] | MudRunner (EPIC) | 19 | 2026-10-18 | 41 | 70% |  |
| 295 | [x] | Sorry We're Closed (EPIC) | 19 | 2026-11-09 | 34 | 72% |  |
| 296 | [x] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 2026-11-15 | 34 | 61% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 297 | [x] | One-armed robber (STEAM) | 19 | 2026-11-09 | 34 | 70% |  |
| 298 | [x] | SWORN (STEAM) | 19 | 2026-11-09 | 34 | 95% |  |
| 299 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 19 | 2026-11-09 | 33 | 76% |  |
| 300 | [x] | Far Far West (STEAM) | 19 | 2026-11-09 | 33 | 61% |  |
| 301 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 32 | 72% |  |
| 302 | [x] | GOD EATER RESURRECTION (STEAM) | 19 | 2026-11-09 | 31 | 71% |  |
| 303 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 19 | 2026-11-09 | 29 | 86% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 304 | [x] | Backpack Battles (STEAM) | 18 | 2026-11-09 | 42 | 100% |  |
| 305 | [x] | Soul's Remnant (STEAM) | 18 | 2026-11-11 | 36 | n/a |  |
| 306 | [x] | Arcade Paradise (EPIC) | 18 | 2026-11-09 | 28 | 67% |  |
| 307 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-11-09 | 27 | 76% |  |
| 308 | [x] | Capcom Fighting Collection (STEAM) | 18 | 2026-11-09 | 26 | 78% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 309 | [x] | Need for Speed™ Unbound (STEAM) | 18 | 2026-11-09 | 26 | 62% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 310 | [x] | Sonic and SEGA All Stars Racing (STEAM) | 18 | 2026-11-09 | 26 | 65% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 311 | [x] | Bongo Cat (STEAM) | 18 | 2026-11-09 | 25 | 68% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 312 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 18 | 2026-11-09 | 24 | 69% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 313 | [x] | Mafia II: Definitive Edition (GOG) | 18 | 2026-11-15 | 20 | 60% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 314 | [x] | Undisputed (STEAM) | 18 | 2026-11-14 | 20 | 64% | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 315 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 17 | 2026-10-19 | 57 | 80% |  |
| 316 | [x] | ABZÛ (STEAM) | 17 | 2026-10-21 | 45 | 97% |  |
| 317 | [x] | Kingdom Come: Deliverance II (STEAM) | 17 | 2026-10-20 | 41 | 88% |  |
| 318 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 37 | 15% |  |
| 319 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 36 | 88% |  |
| 320 | [x] | Faster Than Light (EPIC) | 17 | 2026-11-09 | 32 | 92% |  |
| 321 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 17 | 2026-11-09 | 30 | 85% |  |
| 322 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 17 | 2026-11-09 | 22 | 92% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 323 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 324 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 325 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 51 | 95% |  |
| 326 | [x] | Cave Story+ (EPIC) | 16 | 2026-10-18 | 40 | 85% |  |
| 327 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 16 | 2026-10-20 | 37 | 80% |  |
| 328 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 16 | 2026-11-11 | 35 | 55% |  |
| 329 | [x] | GRIP: Combat Racing (STEAM) | 16 | 2026-11-09 | 34 | 75% |  |
| 330 | [x] | sobosuba (STEAM) | 16 | 2026-11-09 | 33 | 86% |  |
| 331 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 332 | [x] | Tiny Glade (STEAM) | 16 | 2026-11-09 | 31 | 67% |  |
| 333 | [x] | Mortal Kombat 11 (STEAM) | 16 | 2026-11-09 | 30 | 76% |  |
| 334 | [x] | GRANDIA HD Remaster (STEAM) | 16 | 2026-11-09 | 29 | 82% |  |
| 335 | [x] | DNF Duel (EPIC) | 16 | 2026-11-09 | 27 | 64% |  |
| 336 | [x] | Another World: 20th Anniversary Edition (GOG) | 16 | 2026-11-14 | 27 | 62% |  |
| 337 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 62% |  |
| 338 | [x] | Legend of Grimrock 2 (STEAM) | 16 | 2026-11-09 | 24 | 92% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 339 | [x] | Allumeria (STEAM) | 16 | 2026-11-09 | 23 | 73% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 340 | [x] | Ghostwire Tokyo (EPIC) | 16 | 2026-11-09 | 22 | 70% |  |
| 341 | [x] | Darksiders Warmastered Edition (EPIC) | 16 | 2026-11-09 | 21 | 65% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 342 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 343 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 344 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 15 | 2026-10-21 | 44 | 81% |  |
| 345 | [x] | Blood: Fresh Supply (STEAM) | 15 | 2026-10-16 | 40 | 80% |  |
| 346 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 15 | 2026-10-25 | 40 | 76% |  |
| 347 | [x] | Grim Fandango Remastered (STEAM) | 15 | 2026-10-19 | 39 | 75% |  |
| 348 | [x] | Mark of the Ninja (STEAM) | 15 | 2026-10-26 | 31 | 78% |  |
| 349 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 31 | 96% |  |
| 350 | [x] | Intravenous 2 (STEAM) | 15 | 2026-11-09 | 30 | 97% |  |
| 351 | [x] | Hitman: Absolution (GOG) | 15 | 2026-11-09 | 29 | 75% |  |
| 352 | [x] | Human Fall Flat (STEAM) | 15 | 2026-10-29 | 29 | 59% |  |
| 353 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 15 | 2026-11-09 | 29 | 86% |  |
| 354 | [x] | Titanfall® 2 (STEAM) | 15 | 2026-11-09 | 28 | 71% |  |
| 355 | [x] | Batman™: Arkham Origins (GOG) | 15 | 2026-11-09 | 27 | 100% |  |
| 356 | [x] | Gloomwood (STEAM) | 15 | 2026-11-09 | 26 | 60% |  |
| 357 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 15 | 2026-11-15 | 26 | 60% |  |
| 358 | [x] | Assassin's Creed Odyssey (STEAM) | 15 | 2026-11-09 | 24 | 61% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 359 | [x] | STAR WARS™ Episode I: Racer (GOG) | 15 | 2026-11-15 | 23 | 62% | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 360 | [x] | Alabaster Dawn Demo (STEAM) | 15 | 2026-11-09 | 23 | 75% |  |
| 361 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 92% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 362 | [x] | Sacred Gold (STEAM) | 15 | 2026-11-09 | 22 | 70% | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 363 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 364 | [x] | Spark the Electric Jester (STEAM) | 15 | 2026-11-13 | 21 | 67% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 365 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 15 | 2026-11-09 | 21 | 75% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 366 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 367 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 93% |  |
| 368 | [x] | Evoland (STEAM) | 14 | 2026-11-11 | 28 | n/a |  |
| 369 | [x] | Antichamber (STEAM) | 14 | 2026-11-11 | 27 | 82% |  |
| 370 | [x] | Killing Floor (STEAM) | 14 | 2026-10-19 | 27 | 85% |  |
| 371 | [x] | Need for Speed: Undercover (STEAM) | 14 | 2026-11-11 | 27 | 80% | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 372 | [x] | Ultrapool (STEAM) | 14 | 2026-11-09 | 27 | 100% |  |
| 373 | [x] | AER Memories of Old (EPIC) | 14 | 2026-11-09 | 25 | 100% |  |
| 374 | [x] | WORLD OF FINAL FANTASY (STEAM) | 14 | 2026-11-09 | 25 | 80% |  |
| 375 | [x] | Wildermyth (STEAM) | 14 | 2026-11-09 | 25 | 71% |  |
| 376 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 23 | 77% |  |
| 377 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-11-09 | 22 | 92% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 378 | [x] | Nex Machina (STEAM) | 14 | 2026-11-09 | 22 | 76% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 379 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 380 | [x] | Super Monkey Ball Banana Mania (STEAM) | 14 | 2026-11-13 | 21 | 64% |  |
| 381 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 382 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 383 | [x] | Spin Rhythm XD (STEAM) | 13 | 2026-10-18 | 34 | 84% |  |
| 384 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 13 | 2026-10-19 | 31 | 93% |  |
| 385 | [x] | No Man's Sky (GOG) | 13 | 2026-10-19 | 30 | 90% |  |
| 386 | [x] | Divinity: Original Sin (Classic) (STEAM) | 13 | 2026-10-16 | 30 | 70% |  |
| 387 | [x] | Overlord (STEAM) | 13 | 2026-11-08 | 30 | 54% |  |
| 388 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 29 | 50% |  |
| 389 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 29 | 76% |  |
| 390 | [x] | Dead Space™ 3 (STEAM) | 13 | 2026-10-20 | 28 | 75% |  |
| 391 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 28 | 83% |  |
| 392 | [x] | Guacamelee! Gold Edition (STEAM) | 13 | 2026-11-11 | 27 | 83% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 393 | [x] | Blaster Master Zero (STEAM) | 13 | 2026-11-11 | 26 | 61% |  |
| 394 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 13 | 2026-11-09 | 26 | 68% |  |
| 395 | [x] | MX Bikes (STEAM) | 13 | 2026-11-09 | 25 | 93% |  |
| 396 | [x] | Asterigos: Curse of the Stars (STEAM) | 13 | 2026-11-15 | 24 | 90% |  |
| 397 | [x] | Haydee (STEAM) | 13 | 2026-11-09 | 24 | 81% |  |
| 398 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 24 | 77% |  |
| 399 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 13 | 2026-11-09 | 23 | 73% |  |
| 400 | [x] | The Stanley Parable (STEAM) | 13 | 2026-11-13 | 23 | 69% |  |
| 401 | [x] | 12 is Better Than 6 (STEAM) | 13 | 2026-11-09 | 22 | 85% |  |
| 402 | [x] | PAYDAY: The Heist (STEAM) | 13 | 2026-11-13 | 22 | 73% |  |
| 403 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 404 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 70% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 405 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 89% |  |
| 406 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 407 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 2026-11-09 | 20 | 85% |  |
| 408 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 80% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 409 | [x] | Tom Clancy's Splinter Cell: Chaos Theory (STEAM) | 12 | 2026-10-16 | 31 | 87% |  |
| 410 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 12 | 2026-10-18 | 27 | 91% |  |
| 411 | [x] | Castle in the Clouds (STEAM) | 12 | 2026-11-09 | 26 | 67% |  |
| 412 | [x] | Alan Wake's American Nightmare (EPIC) | 12 | 2026-11-09 | 25 | 67% |  |
| 413 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 25 | 68% |  |
| 414 | [x] | Injustice™ 2 (STEAM) | 12 | 2026-10-17 | 24 | 59% |  |
| 415 | [x] | Ready or Not (STEAM) | 12 | 2026-11-09 | 24 | 80% |  |
| 416 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-10 | 23 | 62% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 417 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-11-09 | 23 | 95% |  |
| 418 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 23 | 71% |  |
| 419 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 12 | 2026-11-13 | 22 | 73% |  |
| 420 | [x] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 2026-11-12 | 22 | 90% |  |
| 421 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 422 | [x] | Horny Villa (STEAM) | 12 | 2026-11-09 | 21 | 85% |  |
| 423 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 424 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 425 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 2026-11-10 | 20 | 60% |  |
| 426 | [x] | Shift At Midnight (STEAM) | 12 | 2026-11-09 | 20 | 84% |  |
| 427 | [x] | Turbo Overkill (STEAM) | 12 | 2026-11-09 | 20 | 95% |  |
| 428 | [x] | Haiku, the Robot (STEAM) | 11 | 2026-10-21 | 27 | n/a |  |
| 429 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 2026-11-09 | 25 | 88% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 430 | [x] | Breath of Fire IV (GOG) | 11 | 2026-10-26 | 25 | 67% |  |
| 431 | [x] | Lust Goddess (STEAM) | 11 | 2026-11-09 | 25 | 88% |  |
| 432 | [x] | Rayman Origins (GOG) | 11 | 2026-11-09 | 24 | 76% |  |
| 433 | [x] | Cruelty Squad (STEAM) | 11 | 2026-11-09 | 24 | 86% |  |
| 434 | [x] | DiRT 4 (STEAM) | 11 | 2026-11-09 | 23 | 93% |  |
| 435 | [x] | Life is Strange Remastered (STEAM) | 11 | 2026-11-09 | 23 | 86% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 436 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 23 | 80% |  |
| 437 | [x] | Forgive Me Father (STEAM) | 11 | 2026-11-15 | 22 | 62% |  |
| 438 | [x] | Lost Castle 2 (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 439 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 21 | 75% |  |
| 440 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 441 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-11-09 | 20 | 70% |  |
| 442 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 443 | [x] | Middle-earth™: Shadow of War™ (STEAM) | 10 | 2026-10-16 | 33 | 82% |  |
| 444 | [x] | The WereCleaner (STEAM) | 10 | 2026-10-22 | 31 | 90% |  |
| 445 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 28 | n/a |  |
| 446 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 10 | 2026-11-01 | 25 | n/a |  |
| 447 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 10 | 2026-10-27 | 25 | 76% |  |
| 448 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 10 | 2026-10-23 | 24 | 85% |  |
| 449 | [x] | Aperture Desk Job (STEAM) | 10 | 2026-11-03 | 23 | n/a |  |
| 450 | [x] | Coromon (GOG) | 10 | 2026-10-19 | 22 | 71% |  |
| 451 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 22 | 89% |  |
| 452 | [x] | UNDEFEATED (STEAM) | 10 | 2026-11-09 | 21 | 77% |  |
| 453 | [x] | Sid Meier's Civilization VI (EPIC) | 10 | 2026-10-19 | 20 | 73% |  |
| 454 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 455 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 456 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 457 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 20 | 76% |  |
| 458 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 459 | [x] | TowerFall Ascension (STEAM) | 9 | 2026-10-16 | 31 | 73% |  |
| 460 | [x] | Possessor(s) (STEAM) | 9 | 2026-10-24 | 27 | 88% |  |
| 461 | [x] | Distance (STEAM) | 9 | 2026-10-19 | 26 | 81% |  |
| 462 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 9 | 2026-10-20 | 26 | 83% |  |
| 463 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 9 | 2026-10-21 | 21 | 92% |  |
| 464 | [x] | Football Manager 2024 (STEAM) | 9 | 2026-10-16 | 20 | n/a |  |
| 465 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 9 | 2026-11-09 | 20 | 83% |  |
| 466 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 31% |  |
| 467 | [x] | CULTIC (STEAM) | 8 | 2026-11-09 | 23 | 56% |  |
| 468 | [x] | Gloomhaven (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 469 | [x] | SteamWorld Heist (GOG) | 8 | 2026-10-25 | 20 | n/a |  |
| 470 | [x] | HITMAN World of Assassination (STEAM) | 8 | 2026-11-09 | 20 | 85% |  |
| 471 | [x] | SCP – Containment Breach (STEAM) | 7 | 2026-10-27 | 21 | 92% |  |
| 472 | [x] | Mina the Hollower (GOG) | 7 | 2026-10-28 | 20 | 74% |  |
| 473 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 20 | 52% |  |
| 474 | [x] | Mafia II: Definitive Edition (STEAM) | 7 | 2026-10-16 | 20 | 85% |  |
| 475 | [x] | What Remains of Edith Finch (STEAM) | 6 | 2026-10-19 | 27 | 73% |  |
| 476 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 5 | 2026-10-20 | 20 | 71% |  |
| 477 | [x] | Alex Kidd in Miracle World DX (STEAM) | 1 | 2026-10-16 | 33 | 100% |  |
