# GameNative compatibility worklist

Generated: `2026-11-16T04:15:12.574Z` · Ratings since: `2026-08-18T04:15:12.574Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Probably does not work | 178 |
| Fix shipped, waiting for ratings | 17 |
| First launch fails | 317 |
| Mixed | 489 |
| Works | 1027 |
| Total | 2150 |

## Does not work (122)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 160 | 183 | 87% (14d) | Does not open (83%) | 54% | today | 15% (drop) | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 109 | 124 | 88% (since fix) | Does not open (92%) | 48% | today | 37% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 3 | [ ] | Rocket League® (EPIC) | 59 | 71 | 83% (14d) | Does not open (79%) | 48% | today | 27% (drop) | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 4 | [ ] | Hogwarts Legacy (STEAM) | 26 | 26 | 100% (14d) | Does not open (65%) | 36% | 1d ago | 16% (drop) | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 5 | [x] 2026-10-18 | Project Zomboid (STEAM) | 55 | 61 | 90% (since fix) | Does not open (64%) | 48% | today | 39% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 6 | [ ] | Saints Row 2 (STEAM) | 23 | 23 | 100% (14d) | Does not open (97%) | 33% | today | 34% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 7 | [ ] | ROB RUN (STEAM) | 23 | 30 | 77% (14d) | Does not open (89%) | 57% | today | 60% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 8 | [ ] | Bloons TD 6 (EPIC) | 21 | 25 | 84% (14d) | Does not open (79%) | 41% | today | 20% (drop) | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 9 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 21 | 23 | 91% (14d) | Does not open (96%) | 44% | 1d ago | 15% (drop) | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 10 | [ ] | Saints Row 2 (GOG) | 20 | 25 | 80% (14d) | Does not open (92%) | 39% | 3d ago | 31% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 11 | [ ] | Borderlands 2 (EPIC) | 19 | 21 | 90% (14d) | Does not open (80%) | 55% | 1d ago | 47% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 12 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 19 | 24 | 79% (14d) | Does not open (74%) | 59% | 3d ago | 56% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 13 | [ ] | Metro 2033 Redux (STEAM) | 18 | 25 | 72% (14d) | Does not open (70%) | 42% | today | 39% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 14 | [ ] | Sifu (EPIC) | 16 | 23 | 70% (14d) | Does not open (69%) | 52% | today | 38% | [#535](https://github.com/GameNative/gamenative-compat/issues/535) |
| 15 | [ ] | Metro: Last Light Redux (STEAM) | 19 | 20 | 95% (last 20) | Does not open (88%) | 22% | 1d ago | 24% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 16 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 15 | 20 | 75% (last 20) | Does not open (75%) | 55% | today | 40% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 17 | [ ] | Call of Duty: Black Ops II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 32% | 1d ago | 38% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 18 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (76%) | 0% | 7d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 19 | [ ] | Fallout: New Vegas PCR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | 57% | 1d ago | 61% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 20 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (92%) | 26% | 2d ago | 19% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 21 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | No graphics (46%) | 30% | today | 40% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 22 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 41% | 1d ago | 31% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 23 | [ ] | Path of Exile (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 28% | 1d ago | 16% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 24 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (78%) | 6% | 1d ago | n/a | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 25 | [ ] | skate. (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | 11% | 2d ago | 17% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 26 | [ ] | Hogwarts Legacy (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | 58% | today | 45% |  |
| 27 | [ ] | Mafia II (Classic) (STEAM) | 20 | 20 | 100% (last 20) | Does not open (77%) | 9% | today | 11% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 28 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (70%) | 10% | 10d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 29 | [ ] | Detroit: Become Human (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 55% | today | n/a | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 30 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | 7% | 2d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 31 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 13% | 4d ago | 8% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 32 | [ ] | The Witcher: Enhanced Edition (GOG) | 19 | 20 | 95% (last 20) | Does not open (73%) | 13% | 7d ago | 8% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 33 | [ ] | Fall Guys (EPIC) | 19 | 20 | 95% (last 20) | Does not open (75%) | 15% | 1d ago | 8% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 34 | [ ] | CPM 2 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 8% | today | 7% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 35 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | Does not open (54%) | 0% | 19d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 36 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | 15% | today | 27% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 37 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | 0% | 1d ago | n/a | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 38 | [ ] | MECCHA CHAMELEON (STEAM) | 16 | 20 | 80% (last 20) | Does not open (65%) | 50% | 1d ago | 30% (drop) | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 39 | [ ] | Trackmania (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 19% | today | 29% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 40 | [ ] | Deliver At All Costs (EPIC) | 14 | 20 | 70% (last 20) | Does not open (60%) | 56% | today | 50% |  |
| 41 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (92%) | 8% | 17d ago | 0% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 42 | [ ] | Call of Duty® (STEAM) | 17 | 20 | 85% (last 20) | Does not open (68%) | 4% | today | n/a | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 43 | [ ] | Vampire Survivors (EPIC) | 14 | 20 | 70% (last 20) | Does not open (60%) | 50% | 2d ago | 33% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 44 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | 12% | 15d ago | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 45 | [ ] | Borderlands GOTY (STEAM) | 17 | 20 | 85% (last 20) | Does not open (94%) | 41% | 3d ago | 50% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 46 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (62%) | 54% | today | n/a | [#536](https://github.com/GameNative/gamenative-compat/issues/536) |
| 47 | [ ] | Breath of Fire IV (STEAM) | 20 | 20 | 100% (last 20) | Does not open (60%) | 17% | 3d ago | 9% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 48 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (66%) | 17% | 2d ago | 30% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 49 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (80%) | 15% | 7d ago | 20% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 50 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (88%) | 21% | 7d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 51 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 58% | 6d ago | 37% (drop) | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 52 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 53% | today | 50% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 53 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (83%) | 41% | today | 42% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 54 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (88%) | 44% | 3d ago | 50% | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 55 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (69%) | 33% | 4d ago | 30% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 56 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 12% | 1d ago | 10% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 57 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | 0% | 2d ago | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 58 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (56%) | 27% | 11d ago | 20% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 59 | [ ] | Blood Omen: Legacy of Kain (GOG) | 16 | 20 | 80% (last 20) | No graphics (57%) | 50% | today | n/a |  |
| 60 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 0% | 1d ago | n/a | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 61 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | 50% | 37d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 62 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 26% | 7d ago | 37% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 63 | [ ] | Black Mesa (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | 21% | 23d ago | 33% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 64 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (92%) | 33% | 2d ago | n/a | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 65 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (78%) | 37% | 4d ago | 20% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 66 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (47%) | 42% | 11d ago | 38% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 67 | [ ] | Watch_Dogs (STEAM) | 14 | 20 | 70% (last 20) | Does not open (90%) | 29% | 9d ago | 42% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 68 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (71%) | 35% | 9d ago | 25% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 69 | [ ] | Rivals of Aether II (STEAM) | 15 | 20 | 75% (last 20) | Does not open (55%) | 55% | 2d ago | 8% (drop) | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 70 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 23% | 28d ago | 42% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 71 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 18% | 25d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 72 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | 50% | 5d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 73 | [ ] | XCOM: Enemy Unknown (STEAM) | 18 | 20 | 90% (last 20) | Does not open (72%) | 14% | 2d ago | 20% | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 74 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 14 | 20 | 70% (last 20) | Does not open (44%) | 54% | 1d ago | 57% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 75 | [ ] | Half-Life: Blue Shift (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 36% | 7d ago | n/a | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 76 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | Does not open (63%) | 11% | 9d ago | n/a | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 77 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 17% | 14d ago | n/a | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 78 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (59%) | 30% | 1d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 79 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 3% | 4d ago | 1% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 80 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 19% | 16d ago | n/a | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 81 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 50% | 4d ago | n/a | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 82 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | 43% | today | n/a | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 83 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 0% | 29d ago | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 84 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (67%) | 0% | 22d ago | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 85 | [ ] | Changed (STEAM) | 15 | 20 | 75% (last 20) | Does not open (69%) | 58% | 3d ago | 44% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 86 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 40% | 13d ago | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 87 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (75%) | 20% | 3d ago | n/a | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 88 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (90%) | 21% | 8d ago | n/a | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 89 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 3% | 11d ago | 6% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 90 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 46% | 4d ago | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 91 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 19 | 20 | 95% (last 20) | No graphics (59%) | 41% | 2d ago | 52% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 92 | [ ] | Umamusume: Pretty Derby (STEAM) | 18 | 20 | 90% (last 20) | Does not open (86%) | 50% | 12d ago | 60% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 93 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (47%) | 56% | 6d ago | 52% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 94 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (91%) | 5% | 22d ago | 9% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 95 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (69%) | 36% | 32d ago | n/a | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 96 | [ ] | OneShot (STEAM) | 16 | 20 | 80% (last 20) | Does not open (96%) | 17% | 31d ago | n/a | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 97 | [ ] | Lost Planet: Extreme Condition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 42% | 1d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 98 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | 36% | 6d ago | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 99 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 27% | 14d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 100 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | 43% | 1d ago | 45% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 101 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (97%) | 33% | 14d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 102 | [ ] | Hotline Miami (GOG) | 15 | 20 | 75% (last 20) | Does not open (90%) | 57% | 6d ago | 70% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 103 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (62%) | 57% | 4d ago | 21% (drop) |  |
| 104 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (90%) | 26% | today | 31% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 105 | [ ] | Aliens vs. Predator (STEAM) | 16 | 20 | 80% (last 20) | No graphics (55%) | 22% | 4d ago | 21% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 106 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 40% | 16d ago | n/a | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 107 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (67%) | 50% | 5d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 108 | [ ] | Kenshi (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 4% | 15d ago | 0% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 109 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | 38% | 16d ago | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 110 | [ ] | The Lantern of the Laughless Saint (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 42% | 13d ago | n/a | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 111 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 36% | today | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 112 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 35% | 30d ago | 30% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 113 | [ ] | Maneater (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 56% | 2d ago | 50% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 114 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | 53% | 2d ago | 38% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 115 | [ ] | Zuma Deluxe (STEAM) | 18 | 20 | 90% (last 20) | Does not open (94%) | 31% | 3d ago | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 116 | [ ] | skate.™ (EPIC) | 18 | 20 | 90% (last 20) | Does not open (87%) | 0% | 21d ago | n/a | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 117 | [ ] | Beyond Good & Evil™ (GOG) | 17 | 20 | 85% (last 20) | Does not open (100%) | 20% | 23d ago | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 118 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (67%) | 54% | 7d ago | n/a | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 119 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 33% | 16d ago | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 120 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (54%) | 58% | 1d ago | n/a |  |
| 121 | [ ] | Maneater (EPIC) | 16 | 20 | 80% (last 20) | Does not open (77%) | 47% | today | n/a | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 122 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 36% | 11d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |

## Probably does not work (178)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | MONSTER HUNTER RISE (STEAM) | 37 | 58 | 64% (14d) | Does not open (84%) | 59% | today | 61% |  |
| 2 | [ ] | theHunter Classic (STEAM) | 22 | 22 | 100% (14d) | No graphics (92%) | n/a | 12d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 3 | [ ] | To The Moon (GOG) | 18 | 20 | 90% (last 20) | Does not open (86%) | n/a | 13d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 4 | [ ] | Euro Truck Simulator 2 (STEAM) | 14 | 26 | 54% (14d) | Does not open (65%) | 56% | today | 56% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 5 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 13 | 20 | 65% (last 20) | Does not open (63%) | 52% | 1d ago | 42% |  |
| 6 | [ ] | FINAL FANTASY XIII (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 55% | today | 57% |  |
| 7 | [ ] | Bully: Scholarship Edition (STEAM) | 10 | 20 | 50% (14d) | Does not open (58%) | 56% | today | 11% (drop) |  |
| 8 | [ ] | VRChat (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 39% | 2d ago | 34% |  |
| 9 | [ ] | Driver: Parallel Lines (STEAM) | 19 | 20 | 95% (last 20) | Does not open (65%) | n/a | 7d ago | n/a | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 10 | [ ] | Garry's Mod (STEAM) | 8 | 16 | 50% (since fix) | Does not open (79%) | 54% | today | 44% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 11 | [ ] | Gorilla Tag (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 17% | 1d ago | 7% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 12 | [ ] | Door Kickers 2 (STEAM) | 20 | 20 | 100% (last 20) | No graphics (86%) | n/a | 33d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 13 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 36d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 14 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (36%) | n/a | 13d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 15 | [ ] | Yume Nikki (STEAM) | 11 | 20 | 55% (last 20) | Does not open (87%) | 33% | 1d ago | 51% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 16 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | No graphics (35%) | 54% | 1d ago | 31% (drop) |  |
| 17 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 11 | 19 | 58% (since fix) | Does not open (78%) | 31% | today | 41% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 18 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 20d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 19 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 13 | 20 | 65% (last 20) | Does not open (84%) | 59% | 7d ago | n/a | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 20 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 9d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 21 | [ ] | Metro 2033 Redux (EPIC) | 11 | 20 | 55% (last 20) | Does not open (62%) | 24% | 1d ago | 38% |  |
| 22 | [ ] | Sonic Adventure™ 2  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 49% | 4d ago | 38% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 23 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 17d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 24 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | n/a | 8d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 25 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 27% | 1d ago | 8% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 26 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (93%) | n/a | 4d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 27 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 13 | 20 | 65% (last 20) | Does not open (84%) | 50% | 5d ago | 65% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 28 | [ ] | CODE VEIN (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | 36% | today | 18% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 29 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (85%) | 54% | 6d ago | n/a |  |
| 30 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (100%) | n/a | 5d ago | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 31 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (88%) | n/a | 1d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 32 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 11d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 33 | [ ] | Hollow Knight: Silksong (GOG) | 13 | 20 | 65% (last 20) | Does not open (70%) | 53% | today | 55% |  |
| 34 | [ ] | GRID (STEAM) | 10 | 20 | 50% (last 20) | Does not open (58%) | 41% | 1d ago | 50% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 35 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | n/a | 3d ago | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 36 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 14d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 37 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | n/a | 1d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 38 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | n/a | 15d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 39 | [ ] | Grim Dawn (GOG) | 13 | 20 | 65% (last 20) | Does not open (69%) | n/a | today | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 40 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (70%) | n/a | 13d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 41 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | n/a | 35d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 42 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | 14d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 43 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | today | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 44 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 34d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 45 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | n/a | 5d ago | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 46 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 59% | today | 31% (drop) | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 47 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 33d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 48 | [ ] | Alpha Protocol (STEAM) | 17 | 20 | 85% (last 20) | No graphics (53%) | n/a | 21d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 49 | [ ] | HELLDIVERS™ (STEAM) | 13 | 20 | 65% (last 20) | Does not open (58%) | 37% | 1d ago | 47% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 50 | [ ] | Dead Space 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 32% | 6d ago | 40% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 51 | [ ] | METAL SLUG 3 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 50% | 3d ago | 73% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 52 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | n/a | 2d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 53 | [ ] | Borderlands 2 RU (STEAM) | 19 | 20 | 95% (last 20) | Does not open (61%) | n/a | 1d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 54 | [ ] | DOOM Eternal (STEAM) | 18 | 20 | 90% (last 20) | Does not open (66%) | n/a | 24d ago | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 55 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | n/a | 17d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 56 | [ ] | Breathedge (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 53% | 5d ago | 69% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 57 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | n/a | 36d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 58 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 11d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 59 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 33d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 60 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (57%) | n/a | 2d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 61 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 33d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 62 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 19d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 63 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | n/a | 8d ago | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 64 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | n/a | 12d ago | n/a |  |
| 65 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 32% | 6d ago | n/a | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 66 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (92%) | 33% | today | n/a |  |
| 67 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 2d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 68 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 7d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 69 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 19d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 70 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (54%) | n/a | 21d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 71 | [ ] | Euro Truck Simulator (STEAM) | 20 | 20 | 100% (last 20) | Does not open (88%) | n/a | today | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 72 | [ ] | Peggle Nights (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 19d ago | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 73 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 44d ago | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 74 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 15d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 75 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | n/a | 38d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 76 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | n/a | 24d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 77 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | n/a | 42d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 78 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | n/a | today | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 79 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | n/a | 4d ago | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 80 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | 5% | 11d ago | n/a |  |
| 81 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (47%) | n/a | 15d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 82 | [ ] | The Survivalists (STEAM) | 18 | 20 | 90% (last 20) | Does not open (97%) | n/a | 3d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 83 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | n/a | 5d ago | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 84 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | n/a | 33d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 85 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 11d ago | n/a |  |
| 86 | [ ] | A Plague Tale: Innocence (EPIC) | 11 | 20 | 55% (last 20) | Does not open (70%) | 45% | 2d ago | 23% (drop) |  |
| 87 | [ ] | Metro 2033 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 10% | 12d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 88 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 31d ago | n/a | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 89 | [ ] | Marvel's Spider-Man 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (88%) | n/a | 35d ago | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 90 | [ ] | They Are Billions (STEAM) | 19 | 20 | 95% (last 20) | Does not open (75%) | n/a | 12d ago | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 91 | [ ] | Alien Breed: Impact (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 21d ago | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 92 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 58d ago | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 93 | [ ] | Bionic Commando Rearmed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | n/a | 26d ago | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 94 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 18 | 20 | 90% (last 20) | Does not open (75%) | n/a | 20d ago | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 95 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | n/a | 9d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 96 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 9d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 97 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 5d ago | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 98 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | n/a | 13d ago | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 99 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 6d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 100 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 4d ago | n/a |  |
| 101 | [ ] | Melatonin (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | n/a | 2d ago | n/a | [#272](https://github.com/GameNative/gamenative-compat/issues/272) |
| 102 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | n/a | 4d ago | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 103 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 7d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 104 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | n/a | 4d ago | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 105 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 17d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 106 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 11d ago | n/a |  |
| 107 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 11d ago | n/a |  |
| 108 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 50% | 4d ago | n/a | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 109 | [ ] | Lay of the Land (STEAM) | 18 | 20 | 90% (last 20) | No graphics (61%) | n/a | 15d ago | n/a | [#477](https://github.com/GameNative/gamenative-compat/issues/477) |
| 110 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 14d ago | n/a |  |
| 111 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (47%) | n/a | 14d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 112 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 4d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 113 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 18d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 114 | [ ] | Romancing SaGa -Minstrel Song- Remastered (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (100%) | n/a | today | n/a |  |
| 115 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 13 | 20 | 65% (last 20) | Does not open (52%) | 53% | today | n/a | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 116 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 54% | 4d ago | n/a |  |
| 117 | [ ] | Drop Duchy (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 10% | 2d ago | n/a |  |
| 118 | [ ] | Rise of the Tomb Raider: 20 Year Celebration (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 57% | today | 30% (drop) |  |
| 119 | [ ] | Marvel's Midnight Suns (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | n/a | 33d ago | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 120 | [ ] | GRADIUS origin collection (STEAM) | 17 | 20 | 85% (last 20) | Controller issues (71%) | n/a | today | n/a | [#479](https://github.com/GameNative/gamenative-compat/issues/479) |
| 121 | [ ] | King's Bounty: The Legend (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | n/a | 10d ago | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 122 | [ ] | PICO PARK:Classic Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 38d ago | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 123 | [ ] | ENDLESS Space™ 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | n/a | 31d ago | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 124 | [ ] | Beholder (EPIC) | 15 | 20 | 75% (last 20) | Does not open (65%) | n/a | today | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 125 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | n/a | today | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 126 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | Does not open (42%) | n/a | 6d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 127 | [ ] | Mafia II (Classic) (GOG) | 13 | 20 | 65% (last 20) | Does not open (95%) | n/a | 1d ago | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 128 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 52% | 16d ago | 23% (drop) |  |
| 129 | [ ] | Re-Volt (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (71%) | n/a | 22d ago | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 130 | [ ] | Fallout Classic (GOG) | 15 | 20 | 75% (last 20) | Does not open (88%) | n/a | 3d ago | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 131 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | 3d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 132 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | n/a | 28d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 133 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (83%) | 25% | 14d ago | 17% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 134 | [ ] | Goose Goose Duck (STEAM) | 13 | 20 | 65% (last 20) | Does not open (70%) | 58% | 1d ago | n/a | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 135 | [ ] | Chef Knight (STEAM) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 20d ago | n/a |  |
| 136 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | n/a | 6d ago | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 137 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (89%) | n/a | 8d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 138 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 40% | 5d ago | n/a |  |
| 139 | [ ] | Allumeria (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | n/a | 6d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 140 | [ ] | Songs of Conquest (EPIC) | 13 | 20 | 65% (last 20) | Does not open (75%) | n/a | today | n/a |  |
| 141 | [ ] | Styx: Master of Shadows (EPIC) | 12 | 20 | 60% (last 20) | Does not open (75%) | 37% | 1d ago | 36% |  |
| 142 | [ ] | Chasm (GOG) | 12 | 20 | 60% (last 20) | No graphics (50%) | n/a | 1d ago | n/a |  |
| 143 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (50%) | n/a | 7d ago | n/a |  |
| 144 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 10 | 20 | 50% (last 20) | No graphics (57%) | 38% | today | n/a | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 145 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 57% | today | n/a |  |
| 146 | [ ] | Dungeon Keeper™ 2 (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 22d ago | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 147 | [ ] | Beat Cop (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 3d ago | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 148 | [ ] | Hitman 2: Silent Assassin (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 35% | 1d ago | 42% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 149 | [ ] | FINAL FANTASY VII REMAKE INTERGRADE (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 39% | 1d ago | 39% |  |
| 150 | [ ] | Sandustry (STEAM) | 12 | 20 | 60% (last 20) | Does not open (73%) | n/a | 1d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 151 | [ ] | Mortal Shell (EPIC) | 12 | 20 | 60% (last 20) | No graphics (58%) | 52% | 2d ago | 20% (drop) |  |
| 152 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 45% | today | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 153 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 11d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 154 | [ ] | Mafia: Definitive Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 46% | 2d ago | 41% |  |
| 155 | [ ] | Crying Suns (EPIC) | 11 | 20 | 55% (last 20) | No graphics (63%) | n/a | today | n/a |  |
| 156 | [ ] | A Plague Tale: Innocence (GOG) | 11 | 20 | 55% (last 20) | Does not open (91%) | 58% | 23d ago | n/a |  |
| 157 | [ ] | Knights of Pen and Paper 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (42%) | n/a | 7d ago | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 158 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 13 | 20 | 65% (last 20) | No graphics (56%) | n/a | 34d ago | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 159 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | n/a | 38d ago | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 160 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | n/a | 6d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 161 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 10d ago | n/a |  |
| 162 | [ ] | Minit (EPIC) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 8d ago | n/a |  |
| 163 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 17d ago | n/a |  |
| 164 | [ ] | LET IT DIE (STEAM) | 11 | 20 | 55% (last 20) | Does not open (88%) | n/a | 1d ago | n/a |  |
| 165 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 50% | 4d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 166 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (70%) | 57% | 4d ago | n/a |  |
| 167 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 46% | 4d ago | n/a | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 168 | [ ] | This War of Mine (STEAM) | 10 | 20 | 50% (last 20) | Does not open (54%) | 49% | 16d ago | 31% |  |
| 169 | [ ] | No More Heroes (STEAM) | 10 | 20 | 50% (last 20) | No graphics (67%) | 41% | 2d ago | 23% |  |
| 170 | [ ] | Ys: Memories of Celceta (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 42% | 16d ago | n/a |  |
| 171 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (78%) | n/a | 10d ago | n/a |  |
| 172 | [ ] | Turnip Boy Robs a Bank (EPIC) | 11 | 20 | 55% (last 20) | Does not open (67%) | 29% | 2d ago | n/a | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 173 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 36% | 11d ago | n/a |  |
| 174 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | n/a | 10d ago | n/a |  |
| 175 | [ ] | Railway Chai Wala (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | n/a | 1d ago | n/a |  |
| 176 | [ ] | Dex (GOG) | 11 | 20 | 55% (last 20) | Does not open (89%) | n/a | today | n/a |  |
| 177 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 10 | 20 | 50% (last 20) | Does not open (85%) | n/a | 81d ago | n/a |  |
| 178 | [ ] | Delver (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 40% | today | 0% (drop) |  |

## Fix shipped, waiting for ratings (17)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | Plants vs. Zombies: Game of the Year (STEAM) | 2026-11-04 | 9 | 6 | today | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 2 | L.A. Noire (STEAM) | 2026-11-04 | 4 | 4 | 1d ago | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 3 | Transistor (STEAM) | 2026-11-10 | 1 | 1 | 4d ago | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 4 | Red Dead Redemption (STEAM) | 2026-11-04 | 1 | 1 | 1d ago | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 5 | Max Payne 3 (STEAM) | 2026-11-04 | 2 | 2 | today | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 6 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 6 | 6 | 9d ago | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 7 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 3 | 3 | 5d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 8 | Peggle Deluxe (STEAM) | 2026-10-29 | 1 | 1 | 3d ago | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 9 | Necesse (STEAM) | 2026-10-29 | 6 | 0 | today | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 10 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 1 | 1 | 5d ago | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 11 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 1 | 1 | 12d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 12 | Need for Speed™ (STEAM) | 2026-11-04 | 0 | 0 | 25d ago | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 13 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 0 | 0 | 13d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 14 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 0 | 0 | 18d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 15 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 0 | 0 | 12d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 16 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 11d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 17 | Need for Speed™ Unbound (STEAM) | 2026-11-04 | 0 | 0 | 19d ago | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |

## Works, but the first launch usually fails (317)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 78 | 98 | 80% (14d) | Does not open (63%) | 91% | today | 93% |  |
| 2 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 61 | 82 | 74% (14d) | Does not open (54%) | 83% | today | 84% |  |
| 3 | [ ] | Grand Theft Auto V Legacy (STEAM) | 46 | 56 | 82% (since fix) | Does not open (88%) | 75% | today | 70% |  |
| 4 | [ ] | Cyberpunk 2077 (STEAM) | 45 | 76 | 59% (14d) | Does not open (70%) | 72% | today | 65% |  |
| 5 | [ ] | Half-Life (STEAM) | 44 | 76 | 58% (14d) | Does not open (56%) | 71% | today | 65% |  |
| 6 | [ ] | Road Rash™: 30th Anniversary Edition (STEAM) | 44 | 65 | 68% (14d) | Does not open (74%) | 62% | today | 67% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 7 | [ ] | Valheim (STEAM) | 34 | 54 | 63% (since fix) | No graphics (53%) | 87% | today | 83% |  |
| 8 | [ ] | Buckshot Roulette (STEAM) | 40 | 60 | 67% (14d) | Does not open (63%) | 73% | today | 48% (drop) |  |
| 9 | [ ] | No Man's Sky (STEAM) | 32 | 53 | 60% (since fix) | Controller issues (62%) | 78% | today | 74% |  |
| 10 | [ ] | DREDGE (EPIC) | 35 | 39 | 90% (14d) | Does not open (76%) | 63% | today | 49% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 11 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 35 | 48 | 73% (14d) | Does not open (77%) | 78% | today | 74% |  |
| 12 | [ ] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 34 | 61 | 56% (14d) | Does not open (64%) | 63% | today | 67% |  |
| 13 | [ ] | Super Meat Boy (STEAM) | 28 | 52 | 54% (14d) | Does not open (57%) | 70% | today | 56% |  |
| 14 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 27 | 37 | 73% (14d) | Does not open (57%) | 73% | today | 62% |  |
| 15 | [ ] | Counter-Strike 2 (STEAM) | 42 | 63 | 67% (since fix) | Does not open (67%) | 60% | today | 66% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 16 | [ ] | Red Dead Redemption 2 (STEAM) | 18 | 19 | 95% (since fix) | Does not open (98%) | 79% | 2d ago | 81% |  |
| 17 | [ ] | Quake (STEAM) | 20 | 31 | 65% (14d) | Does not open (65%) | 79% | today | 58% (drop) |  |
| 18 | [ ] | ELDEN RING (STEAM) | 19 | 32 | 59% (14d) | Does not open (85%) | 71% | 1d ago | 64% |  |
| 19 | [ ] | BioShock Remastered (EPIC) | 18 | 22 | 82% (14d) | Does not open (66%) | 66% | today | 54% |  |
| 20 | [ ] | BeamNG.drive (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | 75% | today | 55% (drop) | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 21 | [ ] | Horizon Chase Turbo (EPIC) | 16 | 28 | 57% (14d) | Does not open (82%) | 66% | 1d ago | 40% (drop) |  |
| 22 | [ ] | Devil May Cry 5 (STEAM) | 16 | 27 | 59% (14d) | Does not open (82%) | 79% | 2d ago | 84% |  |
| 23 | [ ] | Resident Evil 4 (2005) (STEAM) | 16 | 30 | 53% (14d) | Does not open (79%) | 72% | today | 69% |  |
| 24 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 16 | 20 | 80% (14d) | Controller issues (60%) | 78% | today | 62% |  |
| 25 | [ ] | Deadlock (STEAM) | 16 | 21 | 76% (14d) | Does not open (54%) | 88% | 1d ago | 85% |  |
| 26 | [ ] | Mortal Kombat X (STEAM) | 16 | 24 | 67% (14d) | Does not open (72%) | 90% | 3d ago | 88% |  |
| 27 | [ ] | DRAGON BALL FighterZ (STEAM) | 27 | 49 | 55% (since fix) | Does not open (89%) | 80% | today | 88% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 28 | [ ] | Crypt of the NecroDancer (STEAM) | 14 | 28 | 50% (14d) | Does not open (47%) | 87% | today | 86% |  |
| 29 | [ ] | Selaco (STEAM) | 14 | 28 | 50% (14d) | Does not open (79%) | 69% | today | 59% |  |
| 30 | [ ] | Clair Obscur: Expedition 33 (STEAM) | 13 | 25 | 52% (14d) | Graphics glitches (41%) | 82% | 1d ago | 74% |  |
| 31 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (88%) | 94% | today | 92% |  |
| 32 | [ ] | Noita (STEAM) | 12 | 21 | 57% (14d) | Does not open (56%) | 75% | today | 77% |  |
| 33 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 12 | 22 | 55% (14d) | Does not open (71%) | 62% | today | 92% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 34 | [ ] | Library Of Ruina (STEAM) | 12 | 21 | 57% (14d) | Does not open (69%) | 86% | today | 78% |  |
| 35 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (71%) | 100% | 1d ago | n/a | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 36 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 69% | 7d ago | 62% |  |
| 37 | [ ] | Absolute Drift (EPIC) | 11 | 21 | 52% (14d) | No graphics (50%) | 75% | today | 37% (drop) |  |
| 38 | [ ] | Dead Island Definitive Edition (STEAM) | 11 | 20 | 55% (14d) | Does not open (66%) | 84% | today | 83% |  |
| 39 | [ ] | Castlevania Dominus Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (92%) | 97% | today | 91% |  |
| 40 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 19 | 37 | 51% (since fix) | Does not open (74%) | 60% | today | 52% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 41 | [ ] | Divinity: Original Sin 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (74%) | 87% | today | 79% |  |
| 42 | [ ] | METAL GEAR SOLID 4: Guns of the Patriots - Master Collection Version (STEAM) | 11 | 20 | 55% (last 20) | Does not open (80%) | 89% | 4d ago | 94% |  |
| 43 | [ ] | Dead Island 2 (EPIC) | 17 | 20 | 85% (last 20) | Does not open (84%) | 68% | 1d ago | 50% |  |
| 44 | [ ] | Batman™: Arkham Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (84%) | 74% | 2d ago | 64% |  |
| 45 | [ ] | Resident Evil 7 Biohazard (STEAM) | 11 | 20 | 55% (last 20) | Does not open (68%) | 78% | today | 69% |  |
| 46 | [ ] | Grand Theft Auto V (EPIC) | 19 | 20 | 95% (last 20) | Does not open (89%) | 79% | 3d ago | 76% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 47 | [ ] | Dead Space (STEAM) | 17 | 20 | 85% (last 20) | Does not open (59%) | 82% | 1d ago | 80% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 48 | [ ] | Alabaster Dawn (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (48%) | 88% | today | 88% |  |
| 49 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (48%) | 92% | 1d ago | 89% |  |
| 50 | [ ] | eFootball™ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (66%) | 63% | 1d ago | 51% |  |
| 51 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 65% | today | 50% |  |
| 52 | [ ] | Cyberpunk 2077 (GOG) | 12 | 20 | 60% (last 20) | Does not open (71%) | 72% | 1d ago | 60% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 53 | [ ] | Fallout: New Vegas (EPIC) | 15 | 20 | 75% (last 20) | Does not open (59%) | 84% | 5d ago | 75% |  |
| 54 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (79%) | 97% | 3d ago | 94% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 55 | [ ] | DOOM 3: BFG Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (72%) | 71% | 1d ago | 65% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 56 | [ ] | The Forest (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 84% | 1d ago | 83% |  |
| 57 | [ ] | Disgaea 5 Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (74%) | 91% | today | 93% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 58 | [ ] | Cry of Fear (STEAM) | 13 | 20 | 65% (last 20) | Does not open (48%) | 73% | today | 74% |  |
| 59 | [ ] | Aniimo (STEAM) | 17 | 20 | 85% (last 20) | Does not open (74%) | 85% | today | 75% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 60 | [ ] | Order of the Sinking Star (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | 69% | 1d ago | 81% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 61 | [ ] | Don't Starve Together (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 76% | 2d ago | 65% |  |
| 62 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | 71% | 1d ago | 74% |  |
| 63 | [ ] | OMORI (STEAM) | 14 | 20 | 70% (last 20) | Does not open (63%) | 69% | today | 51% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 64 | [ ] | Poppy Playtime (STEAM) | 13 | 20 | 65% (last 20) | Does not open (59%) | 73% | 1d ago | 67% |  |
| 65 | [ ] | Deskrawl: Idle ARPG (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 83% | 5d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 66 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 16 | 20 | 80% (last 20) | Graphics glitches (42%) | 84% | today | 81% |  |
| 67 | [ ] | Digimon Story Cyber Sleuth: Complete Edition (STEAM) | 10 | 20 | 50% (last 20) | No graphics (49%) | 80% | today | 89% |  |
| 68 | [ ] | Teenage Mutant Ninja Turtles: Shredder's Revenge (EPIC) | 13 | 20 | 65% (last 20) | Does not open (82%) | 62% | today | 47% |  |
| 69 | [ ] | Abiotic Factor (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 74% | today | 81% |  |
| 70 | [ ] | River City Girls (EPIC) | 14 | 20 | 70% (last 20) | No graphics (50%) | 69% | today | 43% (drop) |  |
| 71 | [ ] | Mini Motorways (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 69% | today | 70% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 72 | [ ] | Castlevania Anniversary Collection (EPIC) | 12 | 20 | 60% (last 20) | Does not open (72%) | 72% | 1d ago | 37% (drop) |  |
| 73 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (82%) | 71% | 7d ago | 50% (drop) |  |
| 74 | [ ] | Fate/stay night REMASTERED (STEAM) | 12 | 20 | 60% (last 20) | No graphics (48%) | 91% | 1d ago | 77% |  |
| 75 | [ ] | Call of Duty 4: Modern Warfare (2007) (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (52%) | 82% | today | 62% |  |
| 76 | [ ] | Welcome to Elderfield (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 71% | today | 70% |  |
| 77 | [ ] | Forza Horizon 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (44%) | 62% | 3d ago | 24% (drop) | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 78 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 15 | 20 | 75% (last 20) | Does not open (44%) | 73% | 2d ago | 67% |  |
| 79 | [ ] | MIO: Memories in Orbit (STEAM) | 11 | 20 | 55% (last 20) | Graphics glitches (50%) | 95% | today | 96% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 80 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (52%) | 72% | 2d ago | 39% (drop) | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 81 | [ ] | Need for Speed: Hot Pursuit (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 78% | 2d ago | 84% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 82 | [ ] | Ratatan (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 97% | 3d ago | n/a |  |
| 83 | [ ] | ZERO Sievert (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | 89% | 2d ago | 73% |  |
| 84 | [ ] | Prey (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 77% | 5d ago | 78% |  |
| 85 | [ ] | Sid Meier's Civilization VI (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 84% | today | 72% |  |
| 86 | [ ] | Fable - The Lost Chapters (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (48%) | 85% | today | 86% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 87 | [ ] | Dota 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (78%) | 74% | 4d ago | 94% |  |
| 88 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 64% | 2d ago | 69% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 89 | [ ] | Happy Wheels (STEAM) | 19 | 20 | 95% (last 20) | No graphics (52%) | 74% | 9d ago | 52% (drop) | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 90 | [ ] | Cave Story+ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | 81% | today | 72% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 91 | [ ] | Rune Factory 3 Special (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 92% | today | n/a |  |
| 92 | [ ] | American Truck Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (68%) | 78% | 2d ago | 72% |  |
| 93 | [ ] | Coromon (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 89% | today | 81% |  |
| 94 | [ ] | Need for Speed™ Rivals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (62%) | 81% | 5d ago | 91% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 95 | [ ] | STAR WARS™ Knights of the Old Republic™ II: The Sith Lords™ (STEAM) | 11 | 20 | 55% (last 20) | No graphics (65%) | 70% | today | 38% (drop) |  |
| 96 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 14 | 20 | 70% (last 20) | Does not open (60%) | 90% | 1d ago | 80% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 97 | [ ] | Quake II (STEAM) | 10 | 20 | 50% (last 20) | No graphics (48%) | 89% | today | 83% |  |
| 98 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (79%) | 79% | today | n/a | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 99 | [ ] | Resident Evil Village (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 88% | 4d ago | 78% |  |
| 100 | [ ] | Disco Elysium - The Final Cut (EPIC) | 10 | 20 | 50% (last 20) | Does not open (71%) | 97% | 3d ago | 97% |  |
| 101 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 70% | today | 50% (drop) |  |
| 102 | [ ] | Until Then (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 79% | 2d ago | 61% |  |
| 103 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 96% | 1d ago | 87% |  |
| 104 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (61%) | 95% | today | 97% |  |
| 105 | [ ] | Palia (STEAM) | 15 | 20 | 75% (last 20) | Does not open (57%) | 76% | 9d ago | 67% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 106 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 65% | 9d ago | 70% |  |
| 107 | [ ] | Sid Meier's Civilization V (STEAM) | 15 | 20 | 75% (last 20) | Does not open (76%) | 64% | today | 61% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 108 | [ ] | Moonstone Island (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (60%) | 78% | today | 70% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 109 | [ ] | Minecraft Dungeons (STEAM) | 10 | 20 | 50% (last 20) | Does not open (79%) | 82% | today | 80% |  |
| 110 | [ ] | Lethal Company (STEAM) | 10 | 20 | 50% (last 20) | Does not open (42%) | 81% | 4d ago | 80% |  |
| 111 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (83%) | 85% | 1d ago | 75% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 112 | [ ] | TBH: Task Bar Hero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 82% | 4d ago | 80% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 113 | [ ] | A Plague Tale: Innocence (STEAM) | 19 | 20 | 95% (last 20) | Does not open (88%) | 75% | today | 75% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 114 | [ ] | Minecraft Dungeons II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (82%) | 72% | 3d ago | 77% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 115 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (52%) | 69% | today | 79% |  |
| 116 | [ ] | PlateUp! (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 81% | today | 66% |  |
| 117 | [ ] | Yakuza: Like a Dragon (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 63% | 8d ago | 75% |  |
| 118 | [ ] | Tails of Iron (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 85% | 1d ago | 82% |  |
| 119 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 64% | 7d ago | 80% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 120 | [ ] | Overwatch® (STEAM) | 18 | 20 | 90% (last 20) | Does not open (57%) | 64% | 8d ago | n/a | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 121 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (77%) | 90% | 1d ago | n/a | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 122 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 12 | 20 | 60% (last 20) | Does not open (43%) | 69% | today | 71% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 123 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 77% | today | 78% |  |
| 124 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 18 | 20 | 90% (last 20) | Does not open (58%) | 82% | 2d ago | n/a | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 125 | [ ] | Sonic Generations (STEAM) | 16 | 20 | 80% (last 20) | Does not open (68%) | 67% | 8d ago | 70% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 126 | [ ] | Astral Party  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 87% | 1d ago | n/a |  |
| 127 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (50%) | 78% | 1d ago | 71% |  |
| 128 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 60% | 14d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 129 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (73%) | 62% | 4d ago | n/a | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 130 | [ ] | Plague Inc: Evolved (STEAM) | 14 | 20 | 70% (last 20) | Does not open (68%) | 60% | 6d ago | 62% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 131 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 95% | 17d ago | n/a |  |
| 132 | [ ] | Fallout (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 65% | 5d ago | 71% |  |
| 133 | [ ] | Heavy Rain (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 92% | 1d ago | 93% |  |
| 134 | [ ] | Driving Rogue (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 92% | 9d ago | 88% |  |
| 135 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 77% | 5d ago | 77% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 136 | [ ] | Chained Echoes (GOG) | 14 | 20 | 70% (last 20) | Does not open (60%) | 62% | 2d ago | n/a |  |
| 137 | [ ] | Call of Duty: World at War (STEAM) | 13 | 20 | 65% (last 20) | Does not open (45%) | 88% | today | 70% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 138 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 86% | 3d ago | 87% |  |
| 139 | [ ] | PowerWash Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (81%) | 79% | today | 100% |  |
| 140 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | 87% | today | n/a | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 141 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (86%) | 94% | 1d ago | 95% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 142 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (47%) | 91% | 6d ago | 86% |  |
| 143 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | 61% | today | 50% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 144 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 60% | 3d ago | 67% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 145 | [ ] | Oxygen Not Included (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 60% | 1d ago | 77% |  |
| 146 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 83% | 4d ago | 78% |  |
| 147 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (80%) | 79% | 14d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 148 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (82%) | 94% | 4d ago | n/a | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 149 | [ ] | Max Payne (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (46%) | 84% | 2d ago | 71% |  |
| 150 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 85% | 3d ago | 79% |  |
| 151 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (62%) | 92% | 11d ago | n/a | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 152 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | 79% | 3d ago | n/a | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 153 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 76% | 9d ago | 79% |  |
| 154 | [ ] | Sonic Lost World (STEAM) | 11 | 20 | 55% (last 20) | No graphics (64%) | 81% | 1d ago | 83% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 155 | [ ] | Street Fighter™ 6 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (81%) | 84% | 4d ago | 82% |  |
| 156 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 64% | 2d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 157 | [ ] | Stellar Blade™ (STEAM) | 14 | 20 | 70% (last 20) | No graphics (43%) | 80% | 6d ago | 82% |  |
| 158 | [ ] | Gambonanza (STEAM) | 13 | 20 | 65% (last 20) | Does not open (60%) | 92% | 3d ago | 94% |  |
| 159 | [ ] | Gothic 1 Classic (STEAM) | 12 | 20 | 60% (last 20) | Does not open (61%) | 78% | 7d ago | 57% (drop) |  |
| 160 | [ ] | ABZU (EPIC) | 10 | 20 | 50% (last 20) | Does not open (86%) | 88% | 7d ago | 81% |  |
| 161 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 68% | 7d ago | n/a | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 162 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 87% | 2d ago | 86% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 163 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (54%) | 71% | today | 85% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 164 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (64%) | 61% | 5d ago | n/a | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 165 | [ ] | Tabletop Simulator (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 73% | 2d ago | 79% |  |
| 166 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (55%) | 62% | 4d ago | 60% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 167 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 79% | 7d ago | 89% |  |
| 168 | [ ] | Control Ultimate Edition (GOG) | 13 | 20 | 65% (last 20) | Does not open (76%) | 83% | 5d ago | 75% |  |
| 169 | [ ] | Limbus Company (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | 83% | today | 90% |  |
| 170 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 94% | 1d ago | 94% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 171 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 11 | 20 | 55% (last 20) | Does not open (62%) | 73% | 13d ago | 75% |  |
| 172 | [ ] | Trailmakers (STEAM) | 11 | 20 | 55% (last 20) | Does not open (44%) | 97% | today | 100% |  |
| 173 | [ ] | BioShock 2 Remastered (STEAM) | 11 | 20 | 55% (last 20) | Does not open (79%) | 83% | today | 83% |  |
| 174 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (70%) | 73% | 8d ago | 80% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 175 | [ ] | State of Decay: Year-One (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 80% | 2d ago | 77% |  |
| 176 | [ ] | Stumble Guys (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 72% | 1d ago | 64% |  |
| 177 | [ ] | Counter-Strike:Global Offensive (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 78% | today | 78% |  |
| 178 | [ ] | Raft (STEAM) | 10 | 20 | 50% (last 20) | Does not open (83%) | 91% | today | 83% |  |
| 179 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (59%) | 92% | 11d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 180 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 92% | 26d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 181 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 88% | 4d ago | 85% |  |
| 182 | [ ] | One-armed robber (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (65%) | 67% | 8d ago | 50% |  |
| 183 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | 64% | 8d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 184 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (85%) | 90% | 16d ago | 83% |  |
| 185 | [ ] | Unturned (STEAM) | 12 | 20 | 60% (last 20) | Does not open (44%) | 70% | 5d ago | 76% |  |
| 186 | [ ] | Mortal Kombat 11 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 80% | 2d ago | 93% |  |
| 187 | [ ] | Capcom Arcade Stadium (STEAM) | 15 | 20 | 75% (last 20) | Does not open (82%) | 75% | 3d ago | 86% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 188 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 93% | 6d ago | n/a |  |
| 189 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (56%) | 65% | 10d ago | 73% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 190 | [ ] | Subnautica 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (55%) | 67% | 5d ago | n/a | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 191 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 85% | 5d ago | n/a | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 192 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 20 | 80% (last 20) | Does not open (47%) | 62% | 2d ago | 33% (drop) | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 193 | [ ] | Digimon Survive (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (77%) | 87% | 4d ago | 77% |  |
| 194 | [ ] | Dishonored 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 82% | 1d ago | 68% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 195 | [ ] | The Witcher: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 64% | 9d ago | 77% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 196 | [ ] | Escape from Duckov (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (71%) | 93% | 3d ago | 97% |  |
| 197 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 87% | 10d ago | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 198 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (69%) | 85% | 21d ago | n/a | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 199 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (75%) | 84% | 4d ago | 70% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 200 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (65%) | 100% | 11d ago | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 201 | [ ] | Supermarket Together (STEAM) | 15 | 20 | 75% (last 20) | Does not open (68%) | 63% | today | 72% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 202 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 68% | 5d ago | 73% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 203 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (59%) | 70% | 6d ago | 58% |  |
| 204 | [ ] | My Summer Car (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | 81% | 2d ago | 83% |  |
| 205 | [ ] | Resident Evil Revelations 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (42%) | 83% | today | 80% |  |
| 206 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 96% | 1d ago | 100% |  |
| 207 | [ ] | TurretGirls (STEAM) | 11 | 20 | 55% (last 20) | No graphics (75%) | 88% | 1d ago | 87% |  |
| 208 | [ ] | Moonring (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 90% | 3d ago | 83% |  |
| 209 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 94% | 5d ago | n/a | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 210 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 75% | 19d ago | n/a | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 211 | [ ] | Darksiders (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 80% | today | 77% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 212 | [ ] | Lucid Blocks (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 62% | today | 56% |  |
| 213 | [ ] | Goat Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 71% | today | 70% |  |
| 214 | [ ] | Battle Brothers (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 84% | 3d ago | 84% |  |
| 215 | [ ] | Jade Empire: Special Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 72% | today | n/a | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 216 | [ ] | Undisputed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 64% | 8d ago | n/a | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 217 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 75% | 4d ago | n/a |  |
| 218 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (92%) | 81% | 29d ago | n/a |  |
| 219 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 71% | 19d ago | 60% |  |
| 220 | [ ] | GOD EATER RESURRECTION (STEAM) | 14 | 20 | 70% (last 20) | Does not open (59%) | 75% | 2d ago | n/a |  |
| 221 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 77% | 4d ago | n/a | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 222 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (44%) | 85% | today | n/a |  |
| 223 | [ ] | GUILTY GEAR Xrd REV 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (86%) | 83% | 1d ago | 62% |  |
| 224 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 81% | 4d ago | 79% |  |
| 225 | [ ] | Invisible, Inc. (STEAM) | 15 | 20 | 75% (last 20) | Does not open (63%) | 80% | 17d ago | n/a |  |
| 226 | [ ] | Ultimate Custom Night (STEAM) | 14 | 20 | 70% (last 20) | No graphics (68%) | 61% | 18d ago | n/a | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 227 | [ ] | Return to Monkey Island (STEAM) | 14 | 20 | 70% (last 20) | No graphics (65%) | 68% | 9d ago | 58% |  |
| 228 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (42%) | 73% | 11d ago | n/a | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 229 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 92% | 6d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 230 | [ ] | SnowRunner (STEAM) | 13 | 20 | 65% (last 20) | Does not open (96%) | 82% | 7d ago | 67% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 231 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (53%) | 64% | 1d ago | 72% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 232 | [ ] | Zero Escape: The Nonary Games (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 62% | 6d ago | 62% |  |
| 233 | [ ] | MX Bikes (STEAM) | 11 | 20 | 55% (last 20) | Does not open (62%) | 93% | today | 92% |  |
| 234 | [ ] | STORY OF SEASONS: Friends of Mineral Town (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 90% | today | 100% |  |
| 235 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 20 | 80% (last 20) | Does not open (82%) | 61% | today | n/a | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 236 | [ ] | Cat Mail Co. (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 86% | 2d ago | 81% |  |
| 237 | [ ] | Deus Ex™ GOTY Edition (GOG) | 12 | 20 | 60% (last 20) | No graphics (44%) | 92% | 16d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 238 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 90% | 1d ago | 92% |  |
| 239 | [ ] | Dying Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (87%) | 70% | today | 53% |  |
| 240 | [ ] | Warframe (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | 83% | today | 75% |  |
| 241 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (40%) | 93% | today | n/a |  |
| 242 | [ ] | Bongo Cat (STEAM) | 15 | 20 | 75% (last 20) | Does not open (92%) | 67% | 10d ago | 40% (drop) | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 243 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 13 | 20 | 65% (last 20) | No graphics (37%) | 86% | 5d ago | n/a | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 244 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (83%) | 77% | 8d ago | 73% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 245 | [ ] | AER Memories of Old (EPIC) | 13 | 20 | 65% (last 20) | Does not open (86%) | 100% | today | n/a |  |
| 246 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (71%) | 78% | 1d ago | n/a |  |
| 247 | [ ] | BATTLETECH (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 90% | today | 82% |  |
| 248 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 72% | 7d ago | 70% |  |
| 249 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 95% | 8d ago | n/a |  |
| 250 | [ ] | Revolution Idle (STEAM) | 11 | 20 | 55% (last 20) | Does not open (43%) | 77% | 1d ago | n/a |  |
| 251 | [ ] | Hero Siege (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (50%) | 82% | today | 94% |  |
| 252 | [ ] | Secrets of Grindea (STEAM) | 10 | 20 | 50% (last 20) | Does not open (48%) | 71% | today | 79% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 253 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 79% | 2d ago | 73% |  |
| 254 | [ ] | Tales of Zestiria (STEAM) | 14 | 20 | 70% (last 20) | Does not open (79%) | 67% | 21d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 255 | [ ] | Capcom Fighting Collection (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 80% | 7d ago | n/a | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 256 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (95%) | 95% | 7d ago | 90% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 257 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (45%) | 62% | 2d ago | n/a |  |
| 258 | [ ] | PAYDAY: The Heist (STEAM) | 13 | 20 | 65% (last 20) | Does not open (75%) | 73% | 9d ago | n/a |  |
| 259 | [ ] | Sacred Gold (STEAM) | 13 | 20 | 65% (last 20) | Does not open (91%) | 70% | 2d ago | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 260 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (100%) | 71% | 1d ago | n/a |  |
| 261 | [ ] | 12 is Better Than 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 83% | 11d ago | n/a |  |
| 262 | [ ] | Big Walk (STEAM) | 11 | 20 | 55% (last 20) | Does not open (65%) | 68% | 13d ago | 46% (drop) |  |
| 263 | [ ] | Hitman: Absolution (GOG) | 11 | 20 | 55% (last 20) | Does not open (85%) | 77% | 1d ago | n/a |  |
| 264 | [ ] | Football Manager 2024 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (91%) | 62% | 8d ago | 41% (drop) |  |
| 265 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 93% | 4d ago | 87% |  |
| 266 | [ ] | Ghostwire Tokyo (EPIC) | 14 | 20 | 70% (last 20) | Does not open (91%) | 68% | 1d ago | 45% (drop) |  |
| 267 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 62% | 8d ago | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 268 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 14 | 20 | 70% (last 20) | Does not open (85%) | 76% | 8d ago | n/a | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 269 | [ ] | Disgaea 4 Complete+ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (43%) | 92% | 1d ago | n/a | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 270 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 90% | 27d ago | 90% |  |
| 271 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 60% | 7d ago | 58% |  |
| 272 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 61% | 10d ago | 61% |  |
| 273 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 60% | 3d ago | 50% |  |
| 274 | [ ] | Sons Of The Forest (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 81% | 1d ago | 79% |  |
| 275 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (50%) | 75% | 8d ago | n/a | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 276 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 12 | 20 | 60% (last 20) | Does not open (90%) | 67% | 7d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 277 | [ ] | Hylics (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 94% | today | 92% |  |
| 278 | [ ] | Hatred (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 89% | 8d ago | 92% |  |
| 279 | [ ] | CRUEL (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 79% | 1d ago | n/a | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 280 | [ ] | Spark the Electric Jester (STEAM) | 14 | 20 | 70% (last 20) | Does not open (58%) | 71% | 11d ago | n/a | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 281 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 77% | 6d ago | n/a |  |
| 282 | [ ] | Timberborn (STEAM) | 12 | 20 | 60% (last 20) | No graphics (62%) | 95% | today | n/a |  |
| 283 | [ ] | Antichamber (STEAM) | 11 | 20 | 55% (last 20) | Does not open (33%) | 80% | 5d ago | n/a |  |
| 284 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 97% | today | 100% |  |
| 285 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 73% | 2d ago | n/a |  |
| 286 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 85% | 6d ago | 70% |  |
| 287 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 71% | 7d ago | 69% |  |
| 288 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 90% | 1d ago | 100% |  |
| 289 | [ ] | No Socks RPG (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (90%) | 93% | 1d ago | 90% |  |
| 290 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (44%) | 67% | 44d ago | n/a |  |
| 291 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 64% | 2d ago | 91% |  |
| 292 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (92%) | 88% | 11d ago | n/a |  |
| 293 | [ ] | Assassin's Creed Odyssey (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 63% | 9d ago | 60% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 294 | [ ] | Forgive Me Father (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 67% | 2d ago | n/a |  |
| 295 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | No graphics (54%) | 69% | 1d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 296 | [ ] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (45%) | 68% | 1d ago | 50% |  |
| 297 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 67% | today | n/a |  |
| 298 | [ ] | Pinball FX Classic (STEAM) | 10 | 20 | 50% (last 20) | Does not open (79%) | 94% | 11d ago | n/a |  |
| 299 | [ ] | GRANDIA II HD Remaster (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 81% | today | n/a |  |
| 300 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 62% | 1d ago | n/a | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 301 | [ ] | Intravenous (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 78% | 7d ago | 77% |  |
| 302 | [ ] | Legend of Grimrock 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 92% | 9d ago | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 303 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | 90% | 2d ago | n/a |  |
| 304 | [ ] | The Outer Worlds (EPIC) | 12 | 20 | 60% (last 20) | Does not open (100%) | 92% | today | n/a |  |
| 305 | [ ] | The Stanley Parable (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 80% | 2d ago | n/a |  |
| 306 | [ ] | SILENT HILL 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (58%) | 78% | 1d ago | 91% |  |
| 307 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (52%) | 90% | 18d ago | n/a | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 308 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 73% | 9d ago | n/a |  |
| 309 | [ ] | Killing Floor (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (100%) | 82% | 8d ago | n/a |  |
| 310 | [ ] | Subnautica: Below Zero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 76% | 7d ago | 64% |  |
| 311 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 60% | 3d ago | n/a |  |
| 312 | [ ] | Shift At Midnight (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | 89% | 10d ago | 83% |  |
| 313 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 72% | 9d ago | 73% |  |
| 314 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 91% | 6d ago | 93% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 315 | [ ] | Decktamer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 83% | 1d ago | n/a |  |
| 316 | [ ] | Haydee (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 87% | 1d ago | n/a |  |
| 317 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 92% | 1d ago | 93% |  |

## Recently recovered (450)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Grim Dawn (STEAM) | 509 | 2026-11-08 | 576 | 68% |  |
| 2 | [x] | FINAL FANTASY RESONANCE (STEAM) | 428 | 2026-10-24 | 971 | 79% |  |
| 3 | [x] | Half-Life (STEAM) | 350 | 2026-11-09 | 623 | 71% |  |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 259 | 2026-11-14 | 408 | 63% |  |
| 5 | [x] | Alan Wake (STEAM) | 239 | 2026-11-14 | 263 | 43% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 6 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 230 | 2026-11-09 | 323 | 90% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 7 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 222 | 2026-10-19 | 284 | 69% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 8 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 211 | 2026-11-09 | 254 | 60% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 9 | [x] | Counter-Strike 2 (STEAM) | 207 | 2026-11-16 | 297 | 60% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 10 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 203 | 2026-11-09 | 356 | 73% |  |
| 11 | [x] | BeamNG.drive (STEAM) | 202 | 2026-11-09 | 243 | 75% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 12 | [x] | Call of Duty: Black Ops (STEAM) | 196 | 2026-11-13 | 221 | 22% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 13 | [x] | Devil May Cry HD Collection (STEAM) | 194 | 2026-10-19 | 284 | 81% |  |
| 14 | [x] | OMORI (STEAM) | 190 | 2026-11-09 | 234 | 69% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 15 | [x] | DRAGON BALL FighterZ (STEAM) | 178 | 2026-11-01 | 220 | 80% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 16 | [x] | DREDGE (EPIC) | 173 | 2026-11-09 | 215 | 63% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 17 | [x] | Spelunky 2 (STEAM) | 165 | 2026-11-01 | 200 | 73% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 18 | [x] | Sid Meier's Civilization V (STEAM) | 160 | 2026-11-10 | 172 | 64% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 19 | [x] | BioShock (STEAM) | 152 | 2026-11-09 | 301 | 74% |  |
| 20 | [x] | Geometry Dash (STEAM) | 150 | 2026-11-11 | 443 | 53% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 21 | [x] | Prototype (STEAM) | 139 | 2026-11-11 | 204 | 56% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 22 | [x] | Team Fortress 2 (STEAM) | 136 | 2026-11-09 | 235 | 74% |  |
| 23 | [x] | Castlevania Advance Collection (STEAM) | 130 | 2026-11-09 | 204 | 89% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 24 | [x] | Minecraft Dungeons II (STEAM) | 129 | 2026-11-09 | 148 | 72% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 25 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 126 | 2026-11-09 | 170 | 60% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 26 | [x] | Counter-Strike (STEAM) | 124 | 2026-11-11 | 205 | 42% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 27 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 124 | 2026-10-18 | 182 | 78% |  |
| 28 | [x] | Mirror's Edge (STEAM) | 123 | 2026-11-09 | 178 | 70% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 29 | [x] | Call of Duty: Black Ops III (STEAM) | 122 | 2026-10-18 | 251 | 80% |  |
| 30 | [x] | Assassin's Creed II (STEAM) | 115 | 2026-11-10 | 120 | 64% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 31 | [x] | Aniimo (STEAM) | 113 | 2026-11-09 | 152 | 85% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 32 | [x] | The Witcher: Enhanced Edition (STEAM) | 107 | 2026-11-09 | 125 | 64% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 33 | [x] | Cave Story+ (STEAM) | 105 | 2026-11-09 | 116 | 81% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 34 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 103 | 2026-11-09 | 143 | 94% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 35 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 101 | 2026-11-15 | 140 | 62% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 36 | [x] | Moonstone Island (STEAM) | 100 | 2026-11-09 | 131 | 78% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 37 | [x] | Happy Wheels (STEAM) | 97 | 2026-11-09 | 117 | 74% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 38 | [x] | Caravan SandWitch (EPIC) | 89 | 2026-11-09 | 153 | 71% |  |
| 39 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 89 | 2026-11-09 | 116 | 94% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 40 | [x] | Catherine Classic (STEAM) | 88 | 2026-11-09 | 166 | 65% |  |
| 41 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 86 | 2026-11-09 | 139 | 67% |  |
| 42 | [x] | Cry of Fear (STEAM) | 85 | 2026-10-18 | 167 | 73% |  |
| 43 | [x] | DOOM 3: BFG Edition (STEAM) | 85 | 2026-11-09 | 125 | 71% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 44 | [x] | Hi-Fi RUSH (STEAM) | 85 | 2026-11-11 | 118 | 43% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 45 | [x] | Quake (STEAM) | 84 | 2026-11-09 | 248 | 79% |  |
| 46 | [x] | Ultra Street Fighter IV (STEAM) | 83 | 2026-10-17 | 181 | 71% |  |
| 47 | [x] | Vital Shell (STEAM) | 80 | 2026-11-09 | 129 | 84% |  |
| 48 | [x] | Age of Empires II: Definitive Edition (STEAM) | 80 | 2026-11-10 | 96 | 60% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 49 | [x] | FINAL FANTASY XIII-2 (STEAM) | 80 | 2026-11-09 | 83 | 68% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 50 | [x] | Psychonauts (STEAM) | 77 | 2026-11-09 | 144 | 94% |  |
| 51 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 77 | 2026-10-18 | 129 | 95% |  |
| 52 | [x] | STEINS;GATE (STEAM) | 76 | 2026-11-09 | 109 | 90% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 53 | [x] | Brawlhalla (STEAM) | 75 | 2026-11-09 | 147 | 72% |  |
| 54 | [x] | Ballionaire (STEAM) | 75 | 2026-11-09 | 124 | 82% |  |
| 55 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 73 | 2026-11-09 | 113 | 84% |  |
| 56 | [x] | The Sims™ 4 (STEAM) | 71 | 2026-11-09 | 93 | 73% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 57 | [x] | Cyberpunk 2077 (GOG) | 70 | 2026-11-09 | 92 | 72% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 58 | [x] | Spyro™ Reignited Trilogy (STEAM) | 69 | 2026-11-09 | 109 | 77% |  |
| 59 | [x] | Need for Speed: Hot Pursuit (STEAM) | 69 | 2026-11-09 | 104 | 78% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 60 | [x] | Disgaea 5 Complete (STEAM) | 69 | 2026-11-09 | 81 | 91% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 61 | [x] | Bayonetta (STEAM) | 68 | 2026-10-18 | 209 | 84% |  |
| 62 | [x] | Dota 2 (STEAM) | 68 | 2026-11-09 | 102 | 74% |  |
| 63 | [x] | Diablo® IV (STEAM) | 67 | 2026-11-11 | 79 | 64% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 64 | [x] | MIO: Memories in Orbit (STEAM) | 66 | 2026-11-09 | 123 | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 65 | [x] | Fable - The Lost Chapters (STEAM) | 66 | 2026-11-09 | 106 | 85% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 66 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 66 | 2026-11-09 | 103 | 83% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 67 | [x] | Stardew Valley (GOG) | 65 | 2026-11-11 | 115 | 71% |  |
| 68 | [x] | American Truck Simulator (STEAM) | 65 | 2026-11-09 | 108 | 78% |  |
| 69 | [x] | Fallout (STEAM) | 63 | 2026-11-09 | 97 | 65% |  |
| 70 | [x] | Order of the Sinking Star (STEAM) | 63 | 2026-11-09 | 92 | 69% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 71 | [x] | Sovereign Tower (STEAM) | 62 | 2026-11-09 | 115 | 71% |  |
| 72 | [x] | Gunfire Reborn (STEAM) | 62 | 2026-11-09 | 68 | 87% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 73 | [x] | Firewatch (STEAM) | 61 | 2026-11-10 | 118 | 72% |  |
| 74 | [x] | Poppy Playtime (STEAM) | 61 | 2026-11-09 | 104 | 73% |  |
| 75 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 61 | 2026-11-09 | 86 | 72% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 76 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 61 | 2026-11-11 | 79 | 51% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 77 | [x] | Borderlands 3 (STEAM) | 60 | 2026-11-09 | 87 | 90% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 78 | [x] | Borderlands: The Pre-Sequel (STEAM) | 59 | 2026-11-09 | 96 | 63% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 79 | [x] | eFootball™ (STEAM) | 59 | 2026-11-09 | 86 | 63% |  |
| 80 | [x] | A Plague Tale: Innocence (STEAM) | 59 | 2026-11-09 | 62 | 75% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 81 | [x] | Mini Motorways (STEAM) | 58 | 2026-11-09 | 98 | 69% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 82 | [x] | Darksiders (STEAM) | 58 | 2026-11-09 | 74 | 80% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 83 | [x] | Deskrawl: Idle ARPG (STEAM) | 58 | 2026-11-09 | 72 | 83% | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 84 | [x] | Call of Juarez Gunslinger (STEAM) | 56 | 2026-11-09 | 71 | 77% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 85 | [x] | Starbound (STEAM) | 55 | 2026-11-09 | 88 | 79% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 86 | [x] | Call of Duty: World at War (STEAM) | 55 | 2026-11-09 | 79 | 88% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 87 | [x] | Sonic Generations (STEAM) | 55 | 2026-11-09 | 60 | 67% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 88 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 54 | 2026-10-25 | 102 | 70% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 89 | [x] | Until Then (STEAM) | 54 | 2026-10-17 | 89 | 79% |  |
| 90 | [x] | Grand Theft Auto V (EPIC) | 54 | 2026-11-09 | 60 | 79% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 91 | [x] | Dead Space (STEAM) | 53 | 2026-10-18 | 66 | 82% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 92 | [x] | Overwatch® (STEAM) | 53 | 2026-11-10 | 56 | 64% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 93 | [x] | Sol Cesto (EPIC) | 53 | 2026-11-09 | 54 | 79% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 94 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 52 | 2026-11-09 | 86 | 89% |  |
| 95 | [x] | TBH: Task Bar Hero (STEAM) | 52 | 2026-11-09 | 85 | 82% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 96 | [x] | Sonic Adventure DX (STEAM) | 51 | 2026-10-17 | 89 | 70% |  |
| 97 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 51 | 2026-11-09 | 85 | 78% |  |
| 98 | [x] | Darkest Dungeon® (EPIC) | 50 | 2026-11-09 | 93 | 80% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 99 | [x] | Okami HD (STEAM) | 50 | 2026-11-09 | 92 | 91% |  |
| 100 | [x] | Last Epoch (STEAM) | 50 | 2026-11-09 | 75 | 77% |  |
| 101 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 48 | 2026-11-09 | 83 | 61% |  |
| 102 | [x] | Heroes of Might & Magic III - HD Edition (STEAM) | 48 | 2026-11-14 | 63 | 61% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 103 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 48 | 2026-11-09 | 55 | 90% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 104 | [x] | Abiotic Factor (STEAM) | 47 | 2026-10-18 | 82 | 74% |  |
| 105 | [x] | Oxygen Not Included (STEAM) | 47 | 2026-11-11 | 80 | 60% |  |
| 106 | [x] | Moonlighter (EPIC) | 47 | 2026-11-09 | 51 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 107 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 46 | 2026-11-09 | 77 | 50% |  |
| 108 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 46 | 2026-11-09 | 76 | 85% |  |
| 109 | [x] | MudRunner (STEAM) | 45 | 2026-10-24 | 100 | 66% |  |
| 110 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 45 | 2026-11-09 | 72 | 91% |  |
| 111 | [x] | Tomb Raider GOTY (GOG) | 44 | 2026-10-17 | 105 | 95% |  |
| 112 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 44 | 2026-10-19 | 88 | 71% |  |
| 113 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 44 | 2026-11-13 | 65 | 62% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 114 | [x] | Mortal Kombat X (STEAM) | 43 | 2026-10-17 | 75 | 90% |  |
| 115 | [x] | Big Walk (STEAM) | 43 | 2026-11-09 | 68 | 68% |  |
| 116 | [x] | Plague Inc: Evolved (STEAM) | 43 | 2026-11-16 | 63 | 60% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 117 | [x] | Sheepy: A Short Adventure (STEAM) | 43 | 2026-11-09 | 51 | 75% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 118 | [x] | Sonic Lost World (STEAM) | 42 | 2026-11-09 | 61 | 81% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 119 | [x] | Forza Horizon 4 (STEAM) | 42 | 2026-11-09 | 58 | 62% | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 120 | [x] | Aggelos (STEAM) | 42 | 2026-11-09 | 57 | 94% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 121 | [x] | Tomb Raider: Anniversary (STEAM) | 41 | 2026-11-09 | 65 | 61% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 122 | [x] | Rayman Origins (STEAM) | 40 | 2026-10-17 | 89 | 84% |  |
| 123 | [x] | Ace Attorney Investigations Collection (STEAM) | 40 | 2026-11-09 | 70 | 87% |  |
| 124 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 39 | 2026-11-09 | 71 | 86% |  |
| 125 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 39 | 2026-11-09 | 60 | 73% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 126 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-11-09 | 40 | 79% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 127 | [x] | Digimon World: Next Order (STEAM) | 38 | 2026-11-09 | 75 | 86% |  |
| 128 | [x] | Age of Empires II (2013) (STEAM) | 38 | 2026-11-09 | 63 | 69% |  |
| 129 | [x] | FINAL FANTASY VII (2013) (STEAM) | 38 | 2026-11-09 | 55 | 64% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 130 | [x] | Dead by Daylight (STEAM) | 38 | 2026-11-09 | 42 | 87% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 131 | [x] | PROTOTYPE 2 (STEAM) | 37 | 2026-10-18 | 82 | 67% |  |
| 132 | [x] | Life is Strange™ (STEAM) | 37 | 2026-10-17 | 79 | 83% |  |
| 133 | [x] | Amnesia: The Dark Descent (STEAM) | 37 | 2026-11-09 | 73 | 82% |  |
| 134 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 37 | 2026-11-09 | 69 | 90% |  |
| 135 | [x] | Street Fighter™ 6 (STEAM) | 37 | 2026-11-09 | 61 | 84% |  |
| 136 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 37 | 2026-11-09 | 50 | 85% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 137 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 37 | 2026-11-09 | 39 | 82% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 138 | [x] | Teardown (STEAM) | 36 | 2026-10-17 | 84 | 79% |  |
| 139 | [x] | Sonic Origins (STEAM) | 36 | 2026-11-09 | 67 | 83% |  |
| 140 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 36 | 2026-11-09 | 66 | 84% |  |
| 141 | [x] | Capcom Arcade Stadium (STEAM) | 36 | 2026-11-09 | 46 | 75% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 142 | [x] | CrossCode (GOG) | 36 | 2026-11-09 | 39 | 79% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 143 | [x] | POSTAL 2 (GOG) | 35 | 2026-11-09 | 70 | 88% |  |
| 144 | [x] | XCOM 2 (STEAM) | 35 | 2026-11-09 | 59 | 85% |  |
| 145 | [x] | Russian Fishing 4 (STEAM) | 35 | 2026-11-09 | 41 | 84% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 146 | [x] | Elite Dangerous (STEAM) | 35 | 2026-11-09 | 38 | 60% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 147 | [x] | Cobalt Core (STEAM) | 34 | 2026-10-18 | 93 | 88% |  |
| 148 | [x] | Rogue Legacy (STEAM) | 34 | 2026-10-17 | 81 | 88% |  |
| 149 | [x] | SurrounDead (STEAM) | 34 | 2026-11-09 | 67 | 91% |  |
| 150 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 34 | 2026-11-11 | 62 | 26% |  |
| 151 | [x] | The Bazaar (STEAM) | 34 | 2026-11-09 | 62 | 77% |  |
| 152 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 34 | 2026-11-09 | 60 | 73% |  |
| 153 | [x] | Rocket League (STEAM) | 34 | 2026-10-17 | 59 | 68% |  |
| 154 | [x] | Hero Siege (STEAM) | 34 | 2026-11-09 | 58 | 82% |  |
| 155 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 34 | 2026-11-09 | 55 | 90% |  |
| 156 | [x] | Super Animal Royale (STEAM) | 34 | 2026-11-16 | 45 | 62% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 157 | [x] | Need for Speed™ Rivals (STEAM) | 34 | 2026-11-10 | 44 | 81% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 158 | [x] | Romestead (STEAM) | 34 | 2026-11-09 | 44 | 61% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 159 | [x] | Death Road to Canada (STEAM) | 33 | 2026-10-17 | 95 | 83% |  |
| 160 | [x] | State of Decay: Year-One (STEAM) | 33 | 2026-10-18 | 68 | 80% |  |
| 161 | [x] | Hearts of Iron IV (STEAM) | 33 | 2026-11-09 | 65 | 75% |  |
| 162 | [x] | Gauntlet™  (STEAM) | 33 | 2026-11-11 | 47 | 53% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 163 | [x] | Journey (STEAM) | 32 | 2026-10-27 | 72 | 69% |  |
| 164 | [x] | Being a DIK (STEAM) | 32 | 2026-11-09 | 59 | 62% |  |
| 165 | [x] | Stumble Guys (STEAM) | 32 | 2026-10-18 | 58 | 72% |  |
| 166 | [x] | Max Payne (STEAM) | 32 | 2026-11-09 | 57 | 84% |  |
| 167 | [x] | Earthion (STEAM) | 32 | 2026-11-09 | 53 | 100% |  |
| 168 | [x] | Counter-Strike:Global Offensive (STEAM) | 32 | 2026-11-09 | 52 | 78% |  |
| 169 | [x] | SnowRunner (STEAM) | 32 | 2026-11-09 | 46 | 82% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 170 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-11-09 | 41 | 92% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 171 | [x] | Dishonored - Definitive Edition (EPIC) | 31 | 2026-10-17 | 80 | 79% |  |
| 172 | [x] | Salt and Sanctuary (STEAM) | 31 | 2026-10-18 | 73 | 83% |  |
| 173 | [x] | COCOON (STEAM) | 31 | 2026-11-09 | 66 | 85% |  |
| 174 | [x] | Owlboy (STEAM) | 31 | 2026-11-02 | 64 | 52% |  |
| 175 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 31 | 2026-11-09 | 55 | 73% |  |
| 176 | [x] | Red Dead Redemption (STEAM) | 31 | 2026-11-09 | 34 | 58% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 177 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 30 | 2026-11-09 | 67 | 75% |  |
| 178 | [x] | Ultimate Chicken Horse (STEAM) | 30 | 2026-10-23 | 64 | 85% |  |
| 179 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 30 | 2026-11-09 | 61 | 84% |  |
| 180 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 30 | 2026-10-17 | 57 | 83% |  |
| 181 | [x] | Resident Evil Village (STEAM) | 30 | 2026-11-09 | 53 | 88% |  |
| 182 | [x] | Prince of Persia: The Sands of Time (STEAM) | 30 | 2026-11-09 | 50 | 78% |  |
| 183 | [x] | Secrets of Grindea (STEAM) | 30 | 2026-11-09 | 49 | 71% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 184 | [x] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 30 | 2026-11-14 | 35 | 64% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 185 | [x] | Torchlight II (STEAM) | 29 | 2026-10-20 | 72 | 87% |  |
| 186 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 29 | 2026-11-09 | 51 | 85% |  |
| 187 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 29 | 2026-11-09 | 50 | 86% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 188 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 29 | 2026-11-09 | 49 | 70% |  |
| 189 | [x] | Guildrun Demo (STEAM) | 29 | 2026-11-09 | 46 | 69% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 190 | [x] | Yakuza: Like a Dragon (STEAM) | 29 | 2026-11-09 | 46 | 63% |  |
| 191 | [x] | Supermarket Together (STEAM) | 29 | 2026-11-09 | 41 | 63% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 192 | [x] | Nioh: Complete Edition (STEAM) | 29 | 2026-11-09 | 39 | 90% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 193 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 71% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 194 | [x] | Heavy Rain (STEAM) | 28 | 2026-11-09 | 48 | 92% |  |
| 195 | [x] | Gambonanza (STEAM) | 28 | 2026-11-09 | 46 | 92% |  |
| 196 | [x] | Tower and Sword of Succubus (STEAM) | 28 | 2026-11-09 | 43 | 81% |  |
| 197 | [x] | Dying Light (EPIC) | 27 | 2026-10-17 | 62 | 70% |  |
| 198 | [x] | Resident Evil Revelations 2 (STEAM) | 27 | 2026-11-09 | 52 | 83% |  |
| 199 | [x] | Deponia (STEAM) | 27 | 2026-11-09 | 51 | 73% |  |
| 200 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 27 | 2026-11-09 | 49 | 96% |  |
| 201 | [x] | Dead Rising 2 (STEAM) | 27 | 2026-11-09 | 43 | 65% |  |
| 202 | [x] | Limbus Company (STEAM) | 27 | 2026-11-09 | 41 | 83% |  |
| 203 | [x] | Digimon Survive (STEAM) | 27 | 2026-11-09 | 40 | 87% |  |
| 204 | [x] | Palia (STEAM) | 27 | 2026-11-09 | 39 | 76% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 205 | [x] | Ultimate Custom Night (STEAM) | 27 | 2026-11-09 | 37 | 61% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 206 | [x] | Gothic II: Gold Classic (STEAM) | 27 | 2026-11-09 | 36 | 65% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 207 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 26 | 2026-10-19 | 94 | 92% |  |
| 208 | [x] | Grand Theft Auto III (STEAM) | 26 | 2026-10-17 | 72 | 73% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 209 | [x] | Monster Hunter Stories (STEAM) | 26 | 2026-10-17 | 63 | 80% |  |
| 210 | [x] | Skullgirls 2nd Encore (STEAM) | 26 | 2026-11-10 | 61 | 66% |  |
| 211 | [x] | Frostpunk (STEAM) | 26 | 2026-11-09 | 53 | 69% |  |
| 212 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 45 | 62% |  |
| 213 | [x] | Capcom Fighting Collection 2 (STEAM) | 26 | 2026-11-09 | 43 | 82% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 214 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 26 | 2026-11-09 | 39 | 69% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 215 | [x] | CRUEL (STEAM) | 26 | 2026-11-09 | 36 | 79% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 216 | [x] | Subnautica 2 (STEAM) | 26 | 2026-11-15 | 31 | 67% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 217 | [x] | Aethermancer (STEAM) | 25 | 2026-10-18 | 49 | 87% |  |
| 218 | [x] | Prince of Persia (GOG) | 25 | 2026-11-09 | 44 | 81% |  |
| 219 | [x] | Battle Brothers (STEAM) | 25 | 2026-11-09 | 44 | 84% |  |
| 220 | [x] | Counter-Strike: Condition Zero (STEAM) | 25 | 2026-11-11 | 44 | 38% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 221 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-09 | 32 | 92% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 222 | [x] | Tales of Zestiria (STEAM) | 25 | 2026-11-09 | 31 | 67% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 223 | [x] | BioShock™ (GOG) | 24 | 2026-10-18 | 63 | 84% |  |
| 224 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 57 | 92% |  |
| 225 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 24 | 2026-10-20 | 53 | 87% |  |
| 226 | [x] | Mirror's Edge™ (GOG) | 24 | 2026-11-13 | 45 | 62% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 227 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 24 | 2026-11-09 | 43 | 68% |  |
| 228 | [x] | Opus Magnum (STEAM) | 24 | 2026-11-09 | 39 | 93% |  |
| 229 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 24 | 2026-11-09 | 37 | 71% |  |
| 230 | [x] | Ratatan (STEAM) | 24 | 2026-11-09 | 37 | 97% |  |
| 231 | [x] | Jade Empire: Special Edition (GOG) | 24 | 2026-11-09 | 31 | 73% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 232 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 24 | 2026-11-09 | 31 | 92% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 233 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 24 | 2026-11-09 | 30 | 77% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 234 | [x] | Crab Game (STEAM) | 24 | 2026-11-09 | 28 | 85% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 235 | [x] | Jade Empire: Special Edition (STEAM) | 24 | 2026-11-09 | 27 | 72% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 236 | [x] | WEBFISHING (STEAM) | 23 | 2026-10-17 | 54 | 90% |  |
| 237 | [x] | Chained Echoes (GOG) | 23 | 2026-11-08 | 49 | 62% |  |
| 238 | [x] | Goat Simulator (STEAM) | 23 | 2026-11-09 | 48 | 71% |  |
| 239 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 46 | 89% |  |
| 240 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-11-09 | 45 | 89% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 241 | [x] | Lucid Blocks (STEAM) | 23 | 2026-11-09 | 44 | 62% |  |
| 242 | [x] | Trailmakers (STEAM) | 23 | 2026-11-09 | 41 | 97% |  |
| 243 | [x] | Football Manager 2024 (EPIC) | 23 | 2026-11-09 | 39 | 62% |  |
| 244 | [x] | Cat Mail Co. (STEAM) | 23 | 2026-11-09 | 39 | 86% |  |
| 245 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 95% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 246 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 23 | 2026-11-09 | 27 | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 247 | [x] | Crazy Taxi (STEAM) | 22 | 2026-11-10 | 44 | 68% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 248 | [x] | Wizard of Legend (EPIC) | 22 | 2026-11-09 | 41 | 86% |  |
| 249 | [x] | Unturned (STEAM) | 22 | 2026-11-09 | 40 | 70% |  |
| 250 | [x] | My Summer Car (STEAM) | 22 | 2026-11-09 | 38 | 81% |  |
| 251 | [x] | Deus Ex™ GOTY Edition (GOG) | 22 | 2026-11-09 | 35 | 92% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 252 | [x] | Return to Monkey Island (STEAM) | 22 | 2026-11-09 | 35 | 68% |  |
| 253 | [x] | Tabletop Simulator (STEAM) | 22 | 2026-11-09 | 35 | 73% |  |
| 254 | [x] | Timberborn (STEAM) | 22 | 2026-11-09 | 34 | 95% |  |
| 255 | [x] | Dishonored 2 (STEAM) | 22 | 2026-11-09 | 32 | 82% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 256 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 60 | 97% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 257 | [x] | No Rest for the Wicked (STEAM) | 21 | 2026-10-19 | 47 | 75% |  |
| 258 | [x] | Slow Roads (STEAM) | 21 | 2026-10-22 | 47 | 76% |  |
| 259 | [x] | Control Ultimate Edition (GOG) | 21 | 2026-11-09 | 39 | 83% |  |
| 260 | [x] | Invisible, Inc. (STEAM) | 21 | 2026-11-09 | 37 | 80% |  |
| 261 | [x] | Beyond: Two Souls (STEAM) | 21 | 2026-11-16 | 30 | 62% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 262 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 88% |  |
| 263 | [x] | CarX Street (STEAM) | 21 | 2026-11-09 | 26 | 87% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 264 | [x] | Tearscape (STEAM) | 21 | 2026-11-09 | 25 | 100% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 265 | [x] | BlazBlue Centralfiction (STEAM) | 20 | 2026-10-17 | 54 | 81% |  |
| 266 | [x] | MudRunner (EPIC) | 20 | 2026-10-18 | 43 | 71% |  |
| 267 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-11-09 | 38 | 100% |  |
| 268 | [x] | Pinball FX Classic (STEAM) | 20 | 2026-11-09 | 37 | 94% |  |
| 269 | [x] | Worms W.M.D (STEAM) | 20 | 2026-11-09 | 37 | 95% |  |
| 270 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 20 | 2026-11-09 | 30 | 91% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 271 | [x] | Party Animals (STEAM) | 20 | 2026-11-09 | 29 | 68% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 272 | [x] | Torchlight II (EPIC) | 20 | 2026-11-09 | 28 | 77% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 273 | [x] | Tyr (STEAM) | 20 | 2026-11-09 | 28 | 64% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 274 | [x] | Dead Island (STEAM) | 20 | 2026-11-09 | 25 | 85% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 275 | [x] | Saints Row IV (STEAM) | 19 | 2026-10-19 | 50 | 84% |  |
| 276 | [x] | Mini Metro (STEAM) | 19 | 2026-11-16 | 38 | 43% |  |
| 277 | [x] | Sorry We're Closed (EPIC) | 19 | 2026-11-09 | 34 | 71% |  |
| 278 | [x] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 2026-11-15 | 34 | 64% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 279 | [x] | One-armed robber (STEAM) | 19 | 2026-11-09 | 34 | 67% |  |
| 280 | [x] | SWORN (STEAM) | 19 | 2026-11-09 | 34 | 94% |  |
| 281 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 19 | 2026-11-09 | 33 | 74% |  |
| 282 | [x] | Far Far West (STEAM) | 19 | 2026-11-09 | 33 | 59% |  |
| 283 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 32 | 69% |  |
| 284 | [x] | GOD EATER RESURRECTION (STEAM) | 19 | 2026-11-09 | 31 | 75% |  |
| 285 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 19 | 2026-11-09 | 29 | 86% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 286 | [x] | Backpack Battles (STEAM) | 18 | 2026-11-09 | 42 | 100% |  |
| 287 | [x] | Moonlight Peaks (STEAM) | 18 | 2026-11-09 | 30 | 77% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 288 | [x] | Arcade Paradise (EPIC) | 18 | 2026-11-09 | 28 | 62% |  |
| 289 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-11-09 | 27 | 76% |  |
| 290 | [x] | Capcom Fighting Collection (STEAM) | 18 | 2026-11-09 | 26 | 80% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 291 | [x] | Need for Speed™ Unbound (STEAM) | 18 | 2026-11-09 | 26 | 53% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 292 | [x] | Bongo Cat (STEAM) | 18 | 2026-11-09 | 24 | 67% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 293 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 18 | 2026-11-09 | 24 | 62% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 294 | [x] | Mafia II: Definitive Edition (GOG) | 18 | 2026-11-15 | 20 | 60% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 295 | [x] | Undisputed (STEAM) | 18 | 2026-11-14 | 20 | 64% | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 296 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 17 | 2026-10-19 | 57 | 80% |  |
| 297 | [x] | Kingdom Come: Deliverance II (STEAM) | 17 | 2026-10-20 | 41 | 87% |  |
| 298 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 37 | 23% |  |
| 299 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 36 | 88% |  |
| 300 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 17 | 2026-11-09 | 31 | 85% |  |
| 301 | [x] | Darksiders Warmastered Edition (EPIC) | 17 | 2026-11-09 | 22 | 61% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 302 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 17 | 2026-11-09 | 22 | 92% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 303 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 304 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 305 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 51 | 95% |  |
| 306 | [x] | ABZÛ (STEAM) | 16 | 2026-10-21 | 45 | 97% |  |
| 307 | [x] | Cave Story+ (EPIC) | 16 | 2026-10-18 | 40 | 88% |  |
| 308 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 16 | 2026-10-20 | 37 | 79% |  |
| 309 | [x] | GRIP: Combat Racing (STEAM) | 16 | 2026-11-09 | 34 | 79% |  |
| 310 | [x] | sobosuba (STEAM) | 16 | 2026-11-09 | 33 | 86% |  |
| 311 | [x] | Soul's Remnant (STEAM) | 16 | 2026-11-11 | 32 | n/a |  |
| 312 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 313 | [x] | Tiny Glade (STEAM) | 16 | 2026-11-09 | 31 | 60% |  |
| 314 | [x] | Mortal Kombat 11 (STEAM) | 16 | 2026-11-09 | 30 | 80% |  |
| 315 | [x] | GRANDIA HD Remaster (STEAM) | 16 | 2026-11-09 | 29 | 88% |  |
| 316 | [x] | Batman™: Arkham Origins (GOG) | 16 | 2026-11-09 | 28 | 100% |  |
| 317 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 60% |  |
| 318 | [x] | Legend of Grimrock 2 (STEAM) | 16 | 2026-11-09 | 24 | 92% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 319 | [x] | Ghostwire Tokyo (EPIC) | 16 | 2026-11-09 | 22 | 68% |  |
| 320 | [x] | Tom Clancy's Splinter Cell (STEAM) | 16 | 2026-11-16 | 22 | 62% | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 321 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 322 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 323 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 15 | 2026-10-21 | 44 | 80% |  |
| 324 | [x] | Grim Fandango Remastered (STEAM) | 15 | 2026-10-19 | 40 | 74% |  |
| 325 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 15 | 2026-10-25 | 40 | 77% |  |
| 326 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 15 | 2026-11-11 | 35 | 62% |  |
| 327 | [x] | Faster Than Light (EPIC) | 15 | 2026-11-09 | 31 | 93% |  |
| 328 | [x] | Mark of the Ninja (STEAM) | 15 | 2026-10-26 | 31 | 82% |  |
| 329 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 31 | 96% |  |
| 330 | [x] | Intravenous 2 (STEAM) | 15 | 2026-11-09 | 30 | 97% |  |
| 331 | [x] | Sonic Superstars (STEAM) | 15 | 2026-11-16 | 30 | 60% |  |
| 332 | [x] | Hitman: Absolution (GOG) | 15 | 2026-11-09 | 29 | 77% |  |
| 333 | [x] | Human Fall Flat (STEAM) | 15 | 2026-10-29 | 29 | 62% |  |
| 334 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 15 | 2026-11-09 | 29 | 89% |  |
| 335 | [x] | Titanfall® 2 (STEAM) | 15 | 2026-11-09 | 28 | 72% |  |
| 336 | [x] | AER Memories of Old (EPIC) | 15 | 2026-11-09 | 26 | 100% |  |
| 337 | [x] | Gloomwood (STEAM) | 15 | 2026-11-09 | 26 | 60% |  |
| 338 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 15 | 2026-11-15 | 26 | 61% |  |
| 339 | [x] | Assassin's Creed Odyssey (STEAM) | 15 | 2026-11-09 | 24 | 63% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 340 | [x] | Alabaster Dawn Demo (STEAM) | 15 | 2026-11-09 | 23 | 78% |  |
| 341 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 92% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 342 | [x] | Sacred Gold (STEAM) | 15 | 2026-11-09 | 22 | 70% | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 343 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 344 | [x] | Spark the Electric Jester (STEAM) | 15 | 2026-11-13 | 21 | 71% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 345 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 15 | 2026-11-09 | 21 | 76% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 346 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 347 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 93% |  |
| 348 | [x] | Evoland (STEAM) | 14 | 2026-11-11 | 28 | n/a |  |
| 349 | [x] | Antichamber (STEAM) | 14 | 2026-11-11 | 27 | 80% |  |
| 350 | [x] | Killing Floor (STEAM) | 14 | 2026-10-19 | 27 | 82% |  |
| 351 | [x] | Need for Speed: Undercover (STEAM) | 14 | 2026-11-11 | 27 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 352 | [x] | Ultrapool (STEAM) | 14 | 2026-11-09 | 27 | 100% |  |
| 353 | [x] | WORLD OF FINAL FANTASY (STEAM) | 14 | 2026-11-09 | 25 | 80% |  |
| 354 | [x] | Wildermyth (STEAM) | 14 | 2026-11-09 | 25 | 67% |  |
| 355 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-11-09 | 22 | 92% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 356 | [x] | Nex Machina (STEAM) | 14 | 2026-11-09 | 22 | 75% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 357 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 358 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 22 | 77% |  |
| 359 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 360 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 361 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 13 | 2026-10-19 | 31 | 93% |  |
| 362 | [x] | No Man's Sky (GOG) | 13 | 2026-10-19 | 29 | 90% |  |
| 363 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 29 | 50% |  |
| 364 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 29 | 81% |  |
| 365 | [x] | Dead Space™ 3 (STEAM) | 13 | 2026-10-20 | 28 | 73% |  |
| 366 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 28 | 77% |  |
| 367 | [x] | Castle in the Clouds (STEAM) | 13 | 2026-11-09 | 27 | 65% |  |
| 368 | [x] | Blaster Master Zero (STEAM) | 13 | 2026-11-11 | 26 | 61% |  |
| 369 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 13 | 2026-11-09 | 26 | 72% |  |
| 370 | [x] | MX Bikes (STEAM) | 13 | 2026-11-09 | 26 | 93% |  |
| 371 | [x] | Asterigos: Curse of the Stars (STEAM) | 13 | 2026-11-15 | 24 | 90% |  |
| 372 | [x] | Haydee (STEAM) | 13 | 2026-11-09 | 24 | 87% |  |
| 373 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 24 | 81% |  |
| 374 | [x] | Car Mechanic Simulator 2018 (STEAM) | 13 | 2026-11-09 | 23 | 97% |  |
| 375 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 13 | 2026-11-09 | 23 | 72% |  |
| 376 | [x] | 12 is Better Than 6 (STEAM) | 13 | 2026-11-09 | 22 | 83% |  |
| 377 | [x] | PAYDAY: The Heist (STEAM) | 13 | 2026-11-13 | 22 | 73% |  |
| 378 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 379 | [x] | STAR WARS™ Episode I: Racer (GOG) | 13 | 2026-11-15 | 21 | 67% | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 380 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 70% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 381 | [x] | The Stanley Parable (STEAM) | 13 | 2026-11-13 | 21 | 80% |  |
| 382 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 95% |  |
| 383 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 384 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 2026-11-09 | 20 | 85% |  |
| 385 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-11-16 | 20 | 90% |  |
| 386 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 80% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 387 | [x] | Overlord (STEAM) | 12 | 2026-11-08 | 29 | 57% |  |
| 388 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 12 | 2026-10-18 | 27 | 100% |  |
| 389 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 12 | 2026-11-09 | 26 | 88% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 390 | [x] | Alan Wake's American Nightmare (EPIC) | 12 | 2026-11-09 | 25 | 69% |  |
| 391 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 25 | 70% |  |
| 392 | [x] | Injustice™ 2 (STEAM) | 12 | 2026-10-17 | 24 | 59% |  |
| 393 | [x] | Ready or Not (STEAM) | 12 | 2026-11-09 | 24 | 82% |  |
| 394 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-10 | 23 | 62% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 395 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 23 | 71% |  |
| 396 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 12 | 2026-11-13 | 22 | 73% |  |
| 397 | [x] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 2026-11-12 | 22 | 90% |  |
| 398 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 399 | [x] | Horny Villa (STEAM) | 12 | 2026-11-09 | 21 | 85% |  |
| 400 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 2026-11-16 | 21 | 64% |  |
| 401 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 402 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 403 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 2026-11-10 | 20 | 60% |  |
| 404 | [x] | Shift At Midnight (STEAM) | 12 | 2026-11-09 | 20 | 89% |  |
| 405 | [x] | Turbo Overkill (STEAM) | 12 | 2026-11-09 | 20 | 95% |  |
| 406 | [x] | Spin Rhythm XD (STEAM) | 11 | 2026-10-18 | 32 | 84% |  |
| 407 | [x] | Haiku, the Robot (STEAM) | 11 | 2026-10-21 | 27 | n/a |  |
| 408 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 2026-10-27 | 26 | 77% |  |
| 409 | [x] | Coromon (GOG) | 11 | 2026-10-19 | 25 | 67% |  |
| 410 | [x] | Guacamelee! Gold Edition (STEAM) | 11 | 2026-11-11 | 25 | 75% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 411 | [x] | Lust Goddess (STEAM) | 11 | 2026-11-09 | 25 | 88% |  |
| 412 | [x] | Rayman Origins (GOG) | 11 | 2026-11-09 | 24 | 80% |  |
| 413 | [x] | Cruelty Squad (STEAM) | 11 | 2026-11-09 | 24 | 86% |  |
| 414 | [x] | DiRT 4 (STEAM) | 11 | 2026-11-09 | 23 | 92% |  |
| 415 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 23 | 81% |  |
| 416 | [x] | Life is Strange Remastered (STEAM) | 11 | 2026-11-09 | 23 | 86% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 417 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 23 | 86% |  |
| 418 | [x] | Forgive Me Father (STEAM) | 11 | 2026-11-15 | 22 | 67% |  |
| 419 | [x] | Lost Castle 2 (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 420 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 421 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-11-09 | 20 | 73% |  |
| 422 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 423 | [x] | The WereCleaner (STEAM) | 10 | 2026-10-22 | 31 | 90% |  |
| 424 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 28 | n/a |  |
| 425 | [x] | Distance (STEAM) | 10 | 2026-10-19 | 27 | 81% |  |
| 426 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 10 | 2026-10-23 | 25 | 90% |  |
| 427 | [x] | Breath of Fire IV (GOG) | 10 | 2026-10-26 | 24 | 64% |  |
| 428 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 10 | 2026-11-01 | 24 | n/a |  |
| 429 | [x] | Aperture Desk Job (STEAM) | 10 | 2026-11-03 | 23 | n/a |  |
| 430 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 23 | 88% |  |
| 431 | [x] | Sid Meier's Civilization VI (EPIC) | 10 | 2026-10-19 | 21 | 71% |  |
| 432 | [x] | UNDEFEATED (STEAM) | 10 | 2026-11-09 | 21 | 75% |  |
| 433 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 434 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 435 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 436 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 20 | 78% |  |
| 437 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 438 | [x] | Possessor(s) (STEAM) | 9 | 2026-10-24 | 27 | 88% |  |
| 439 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 9 | 2026-10-20 | 26 | 86% |  |
| 440 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 9 | 2026-10-21 | 21 | 92% |  |
| 441 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 9 | 2026-11-09 | 20 | 82% |  |
| 442 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 31% |  |
| 443 | [x] | SteamWorld Heist (GOG) | 8 | 2026-10-25 | 21 | n/a |  |
| 444 | [x] | HITMAN World of Assassination (STEAM) | 8 | 2026-11-09 | 20 | 81% |  |
| 445 | [x] | CULTIC (STEAM) | 7 | 2026-11-09 | 22 | 56% |  |
| 446 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 21 | 55% |  |
| 447 | [x] | SCP – Containment Breach (STEAM) | 7 | 2026-10-27 | 21 | 91% |  |
| 448 | [x] | Mina the Hollower (GOG) | 7 | 2026-10-28 | 20 | 74% |  |
| 449 | [x] | What Remains of Edith Finch (STEAM) | 6 | 2026-10-19 | 28 | 76% |  |
| 450 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 5 | 2026-10-20 | 20 | 69% |  |
