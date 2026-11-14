# GameNative compatibility worklist

Generated: `2026-11-14T04:15:12.680Z` · Ratings since: `2026-08-16T04:15:12.680Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Probably does not work | 164 |
| Fix shipped, waiting for ratings | 17 |
| First launch fails | 326 |
| Mixed | 502 |
| Works | 1021 |
| Total | 2153 |

## Does not work (123)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 148 | 167 | 89% (14d) | Does not open (83%) | 57% | today | 9% (drop) | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 90 | 105 | 86% (since fix) | Does not open (92%) | 50% | today | 39% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 3 | [ ] | Rocket League® (EPIC) | 48 | 58 | 83% (14d) | Does not open (79%) | 56% | today | 32% (drop) | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 4 | [ ] | Hogwarts Legacy (STEAM) | 28 | 33 | 85% (14d) | Does not open (66%) | 46% | today | 18% (drop) | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 5 | [x] 2026-10-18 | Project Zomboid (STEAM) | 53 | 59 | 90% (since fix) | Does not open (65%) | 51% | today | 42% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 6 | [ ] | Metro 2033 Redux (STEAM) | 24 | 32 | 75% (14d) | Does not open (70%) | 40% | today | 38% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 7 | [ ] | Saints Row 2 (GOG) | 20 | 26 | 77% (14d) | Does not open (92%) | 41% | 1d ago | 32% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 8 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 20 | 25 | 80% (14d) | Does not open (74%) | 59% | 1d ago | 55% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 9 | [ ] | Borderlands 2 (EPIC) | 19 | 22 | 86% (14d) | Does not open (81%) | 59% | today | 48% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 10 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 19 | 22 | 86% (14d) | Does not open (95%) | 54% | today | 14% (drop) | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 11 | [ ] | Bloons TD 6 (EPIC) | 18 | 22 | 82% (14d) | Does not open (78%) | 45% | today | 20% (drop) | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 12 | [ ] | Saints Row 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | 34% | today | 41% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 13 | [ ] | Metro: Last Light Redux (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 18% | today | 18% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 14 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 17 | 21 | 81% (14d) | Does not open (75%) | 53% | 1d ago | 37% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 15 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (75%) | 0% | 5d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 16 | [ ] | ROB RUN (STEAM) | 15 | 21 | 71% (14d) | Does not open (93%) | 49% | today | 53% |  |
| 17 | [ ] | Call of Duty: Black Ops II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (76%) | 31% | 2d ago | 39% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 18 | [ ] | Fallout: New Vegas PCR (STEAM) | 17 | 20 | 85% (last 20) | Does not open (93%) | 57% | today | 56% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 19 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (92%) | 24% | today | 14% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 20 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 18 | 20 | 90% (last 20) | No graphics (46%) | 27% | 6d ago | n/a | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 21 | [ ] | Yume Nikki (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | 28% | 7d ago | 48% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 22 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (78%) | 7% | 2d ago | n/a | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 23 | [ ] | skate. (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | 10% | today | 18% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 24 | [ ] | Path of Exile (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 33% | today | 12% (drop) | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 25 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 17 | 20 | 85% (last 20) | Does not open (87%) | 42% | today | 28% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 26 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (70%) | 8% | 8d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 27 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | 5% | today | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 28 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 13% | 2d ago | 9% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 29 | [ ] | The Witcher: Enhanced Edition (GOG) | 19 | 20 | 95% (last 20) | Does not open (73%) | 11% | 5d ago | 0% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 30 | [ ] | Mafia II (Classic) (STEAM) | 20 | 20 | 100% (last 20) | Does not open (74%) | 7% | 6d ago | 9% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 31 | [ ] | CPM 2 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 6% | 1d ago | n/a | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 32 | [ ] | Fall Guys (EPIC) | 19 | 20 | 95% (last 20) | Does not open (75%) | 16% | 4d ago | 9% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 33 | [ ] | Detroit: Become Human (STEAM) | 19 | 20 | 95% (last 20) | Does not open (75%) | 42% | today | n/a | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 34 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | No graphics (57%) | 0% | 17d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 35 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | 0% | 3d ago | n/a | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 36 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (75%) | 11% | 2d ago | n/a | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 37 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (92%) | 7% | 15d ago | n/a | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 38 | [ ] | Vampire Survivors (EPIC) | 14 | 20 | 70% (last 20) | Does not open (60%) | 53% | today | 37% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 39 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (67%) | 12% | 13d ago | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 40 | [ ] | Borderlands GOTY (STEAM) | 17 | 20 | 85% (last 20) | Does not open (94%) | 35% | 1d ago | 45% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 41 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (80%) | 15% | 5d ago | 18% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 42 | [ ] | Breath of Fire IV (STEAM) | 20 | 20 | 100% (last 20) | Does not open (60%) | 16% | 1d ago | n/a | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 43 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (88%) | 19% | 5d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 44 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 57% | 4d ago | 26% (drop) | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 45 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (67%) | 16% | today | n/a | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 46 | [ ] | MECCHA CHAMELEON (STEAM) | 15 | 20 | 75% (last 20) | Does not open (64%) | 49% | today | 26% (drop) | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 47 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 59% | 7d ago | n/a | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 48 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (83%) | 45% | 28d ago | n/a | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 49 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (73%) | 25% | 2d ago | n/a | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 50 | [ ] | Trackmania (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | 22% | today | 28% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 51 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | 18% | 6d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 52 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (89%) | 43% | 1d ago | 42% | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 53 | [ ] | Plague Inc: Evolved (STEAM) | 14 | 20 | 70% (last 20) | Does not open (68%) | 56% | 4d ago | 62% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 54 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 6% | 1d ago | n/a | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 55 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | 0% | today | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 56 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (56%) | 25% | 9d ago | n/a | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 57 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | 0% | 6d ago | n/a | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 58 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 16 | 20 | 80% (last 20) | Does not open (44%) | 47% | today | 47% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 59 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 19% | 5d ago | 36% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 60 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | 42% | 35d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 61 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (47%) | 37% | 9d ago | 31% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 62 | [ ] | Black Mesa (STEAM) | 15 | 20 | 75% (last 20) | Does not open (82%) | 20% | 21d ago | 36% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 63 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (92%) | 35% | today | n/a | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 64 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (78%) | 39% | 2d ago | 20% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 65 | [ ] | Watch_Dogs (STEAM) | 14 | 20 | 70% (last 20) | Does not open (90%) | 30% | 7d ago | n/a | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 66 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | 0% | 12d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 67 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (71%) | 39% | 7d ago | 30% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 68 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 20% | 26d ago | 40% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 69 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | 45% | 3d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 70 | [ ] | XCOM: Enemy Unknown (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | 11% | today | 20% | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 71 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | 9% | 12d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 72 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 20% | 23d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 73 | [ ] | Half-Life: Blue Shift (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 36% | 5d ago | n/a | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 74 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | Does not open (63%) | 11% | 7d ago | n/a | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 75 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 15% | 12d ago | n/a | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 76 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (60%) | 40% | 14d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 77 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 4% | 2d ago | 2% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 78 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 46% | 2d ago | n/a | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 79 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | 36% | 1d ago | n/a | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 80 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 0% | 27d ago | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 81 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (67%) | 0% | 20d ago | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 82 | [ ] | Changed (STEAM) | 15 | 20 | 75% (last 20) | Does not open (69%) | 55% | 1d ago | 33% (drop) | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 83 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 18% | 14d ago | n/a | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 84 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 36% | 11d ago | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 85 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (81%) | 31% | 6d ago | n/a | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 86 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 6% | 9d ago | 7% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 87 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 19 | 20 | 95% (last 20) | No graphics (59%) | 39% | today | 58% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 88 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (77%) | 23% | 1d ago | n/a | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 89 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (91%) | 5% | 20d ago | 9% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 90 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (68%) | 33% | 30d ago | n/a | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 91 | [ ] | Subnautica 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (57%) | 57% | 3d ago | n/a | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 92 | [ ] | OneShot (STEAM) | 16 | 20 | 80% (last 20) | Does not open (96%) | 17% | 29d ago | n/a | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 93 | [ ] | Call of Duty® (STEAM) | 15 | 20 | 75% (last 20) | Does not open (71%) | 7% | today | n/a | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 94 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | 33% | 4d ago | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 95 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 33% | 12d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 96 | [ ] | Umamusume: Pretty Derby (STEAM) | 18 | 20 | 90% (last 20) | Does not open (86%) | 53% | 10d ago | n/a | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 97 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (97%) | 25% | 12d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 98 | [ ] | Lost Planet: Extreme Condition (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | 47% | 4d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 99 | [ ] | Hotline Miami (GOG) | 15 | 20 | 75% (last 20) | Does not open (90%) | 57% | 4d ago | n/a | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 100 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (95%) | 25% | 25d ago | 27% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 101 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 42% | 11d ago | n/a | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 102 | [ ] | Aliens vs. Predator (STEAM) | 16 | 20 | 80% (last 20) | No graphics (55%) | 17% | 2d ago | 17% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 103 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (86%) | 36% | 14d ago | n/a | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 104 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (67%) | 45% | 3d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 105 | [ ] | Kenshi (STEAM) | 15 | 20 | 75% (last 20) | Does not open (89%) | 4% | 13d ago | n/a | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 106 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | 40% | 31d ago | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 107 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | 20% | 3d ago | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 108 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 38% | 28d ago | n/a | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 109 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | 38% | 14d ago | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 110 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 14 | 20 | 70% (last 20) | Does not open (56%) | 54% | 4d ago | 68% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 111 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | 53% | today | 38% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 112 | [ ] | The Lantern of the Laughless Saint (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 57% | 11d ago | n/a | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 113 | [ ] | Zuma Deluxe (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 38% | 1d ago | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 114 | [ ] | Maneater (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 57% | today | 45% |  |
| 115 | [ ] | skate.™ (EPIC) | 18 | 20 | 90% (last 20) | Does not open (87%) | 0% | 19d ago | n/a | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 116 | [ ] | Beyond Good & Evil™ (GOG) | 17 | 20 | 85% (last 20) | Does not open (100%) | 17% | 21d ago | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 117 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (67%) | 54% | 5d ago | n/a | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 118 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 40% | 14d ago | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 119 | [ ] | Goose Goose Duck (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 56% | 4d ago | n/a | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 120 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 36% | 9d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 121 | [ ] | Maneater (EPIC) | 16 | 20 | 80% (last 20) | Does not open (75%) | 47% | 6d ago | n/a | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 122 | [ ] | Hitman 2: Silent Assassin (STEAM) | 14 | 20 | 70% (last 20) | Does not open (80%) | 39% | today | 42% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 123 | [ ] | Katanaut (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | 56% | 8d ago | 50% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |

## Probably does not work (164)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | To The Moon (GOG) | 44 | 46 | 96% (14d) | Does not open (86%) | n/a | 11d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 2 | [ ] | theHunter Classic (STEAM) | 23 | 23 | 100% (14d) | No graphics (92%) | n/a | 10d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 3 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 14 | 25 | 56% (14d) | Does not open (72%) | 57% | today | 93% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 4 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 13 | 20 | 65% (last 20) | Does not open (63%) | 53% | 1d ago | 47% |  |
| 5 | [ ] | VRChat (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 37% | today | 28% |  |
| 6 | [ ] | Driver: Parallel Lines (STEAM) | 19 | 20 | 95% (last 20) | Does not open (65%) | n/a | 5d ago | n/a | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 7 | [ ] | Garry's Mod (STEAM) | 7 | 12 | 58% (since fix) | Does not open (79%) | 54% | today | 43% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 8 | [ ] | Gorilla Tag (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 17% | today | 8% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 9 | [ ] | Door Kickers 2 (STEAM) | 20 | 20 | 100% (last 20) | No graphics (86%) | n/a | 31d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 10 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 34d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 11 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (35%) | n/a | 11d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 12 | [ ] | Sifu (EPIC) | 11 | 20 | 55% (last 20) | Does not open (66%) | 58% | today | 35% (drop) |  |
| 13 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 18d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 14 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 7d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 15 | [ ] | Sonic Adventure™ 2  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (76%) | 48% | 2d ago | 39% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 16 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 9 | 16 | 56% (since fix) | Does not open (78%) | 24% | today | 37% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 17 | [ ] | Metro 2033 Redux (EPIC) | 10 | 20 | 50% (last 20) | Does not open (62%) | 24% | 5d ago | 39% |  |
| 18 | [ ] | GRID (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 44% | 5d ago | 50% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 19 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 15d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 20 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 13 | 20 | 65% (last 20) | Does not open (84%) | 51% | 3d ago | 67% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 21 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (85%) | 43% | 4d ago | n/a |  |
| 22 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (93%) | n/a | 2d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 23 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (100%) | n/a | 3d ago | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 24 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 9d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 25 | [ ] | CODE VEIN (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 50% | 3d ago | n/a | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 26 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 30% | 6d ago | n/a | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 27 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | n/a | 1d ago | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 28 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (87%) | n/a | 12d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 29 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | n/a | 33d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 30 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | n/a | 16d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 31 | [ ] | Hollow Knight: Silksong (GOG) | 12 | 20 | 60% (last 20) | Does not open (72%) | 54% | 1d ago | 60% |  |
| 32 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | 2d ago | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 33 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 32d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 34 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 11d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 35 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | n/a | 3d ago | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 36 | [ ] | Dead Space 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 30% | 4d ago | 40% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 37 | [ ] | Grim Dawn (GOG) | 12 | 20 | 60% (last 20) | Does not open (65%) | n/a | 2d ago | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 38 | [ ] | METAL SLUG 3 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 44% | 1d ago | n/a | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 39 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 31d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 40 | [ ] | Alpha Protocol (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | n/a | 19d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 41 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | n/a | today | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 42 | [ ] | DOOM Eternal (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | n/a | 22d ago | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 43 | [ ] | Breathedge (STEAM) | 11 | 20 | 55% (last 20) | Does not open (56%) | 49% | 3d ago | 64% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 44 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (57%) | n/a | today | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 45 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | n/a | 15d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 46 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 31d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 47 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 17d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 48 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 32% | 4d ago | n/a | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 49 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | n/a | 34d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 50 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 9d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 51 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | n/a | 31d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 52 | [ ] | Borderlands 2 RU (STEAM) | 19 | 20 | 95% (last 20) | Does not open (64%) | n/a | 31d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 53 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | today | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 54 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 5d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 55 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | n/a | 6d ago | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 56 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 17d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 57 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (54%) | n/a | 19d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 58 | [ ] | HELLDIVERS™ (STEAM) | 13 | 20 | 65% (last 20) | Does not open (59%) | 42% | 3d ago | 55% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 59 | [ ] | Euro Truck Simulator (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | 2d ago | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 60 | [ ] | Peggle Nights (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 17d ago | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 61 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 42d ago | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 62 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 13d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 63 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | n/a | 22d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 64 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | n/a | 2d ago | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 65 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (93%) | 40% | today | n/a |  |
| 66 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | 0% | 9d ago | n/a |  |
| 67 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (47%) | n/a | 13d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 68 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | n/a | 36d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 69 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | n/a | 31d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 70 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (63%) | n/a | 40d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 71 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (86%) | n/a | 3d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 72 | [ ] | A Plague Tale: Innocence (EPIC) | 11 | 20 | 55% (last 20) | Does not open (68%) | 52% | today | 20% (drop) |  |
| 73 | [ ] | Metro 2033 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (61%) | 23% | 10d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 74 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 29d ago | n/a | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 75 | [ ] | They Are Billions (STEAM) | 19 | 20 | 95% (last 20) | Does not open (75%) | n/a | 10d ago | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 76 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 56d ago | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 77 | [ ] | The Survivalists (STEAM) | 18 | 20 | 90% (last 20) | Does not open (97%) | n/a | 1d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 78 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 7d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 79 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 9d ago | n/a |  |
| 80 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 2d ago | n/a |  |
| 81 | [ ] | Resident Evil Requiem (STEAM) | 20 | 20 | 100% (last 20) | Does not open (69%) | n/a | 33d ago | n/a | [#210](https://github.com/GameNative/gamenative-compat/issues/210) |
| 82 | [ ] | Marvel's Spider-Man 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (88%) | n/a | 33d ago | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 83 | [ ] | Alien Breed: Impact (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 19d ago | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 84 | [ ] | Melatonin (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | n/a | today | n/a | [#272](https://github.com/GameNative/gamenative-compat/issues/272) |
| 85 | [ ] | Bionic Commando Rearmed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | n/a | 24d ago | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 86 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 18 | 20 | 90% (last 20) | Does not open (75%) | n/a | 18d ago | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 87 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | n/a | 2d ago | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 88 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (83%) | n/a | 7d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 89 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 5d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 90 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 3d ago | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 91 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 4d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 92 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 9d ago | n/a |  |
| 93 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 9d ago | n/a |  |
| 94 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 50% | 2d ago | n/a | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 95 | [ ] | No More Room in Hell (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 27d ago | n/a | [#365](https://github.com/GameNative/gamenative-compat/issues/365) |
| 96 | [ ] | Lay of the Land (STEAM) | 18 | 20 | 90% (last 20) | No graphics (61%) | n/a | 13d ago | n/a | [#477](https://github.com/GameNative/gamenative-compat/issues/477) |
| 97 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | n/a | 2d ago | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 98 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 15d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 99 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (47%) | n/a | 12d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 100 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 16d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 101 | [ ] | Drop Duchy (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | n/a | today | n/a |  |
| 102 | [ ] | Deadly Premonition: The Director's Cut (STEAM) | 18 | 20 | 90% (last 20) | Does not open (53%) | n/a | 7d ago | n/a | [#520](https://github.com/GameNative/gamenative-compat/issues/520) |
| 103 | [ ] | King's Bounty: The Legend (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | n/a | 8d ago | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 104 | [ ] | Marvel's Midnight Suns (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | n/a | 31d ago | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 105 | [ ] | PICO PARK:Classic Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 36d ago | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 106 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 12d ago | n/a |  |
| 107 | [ ] | Beholder (EPIC) | 15 | 20 | 75% (last 20) | Does not open (69%) | n/a | 19d ago | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 108 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 2d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 109 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | Does not open (42%) | n/a | 4d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 110 | [ ] | Mafia II (Classic) (GOG) | 13 | 20 | 65% (last 20) | Does not open (95%) | n/a | 21d ago | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 111 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | 53% | 14d ago | 25% (drop) |  |
| 112 | [ ] | ENDLESS Space™ 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | n/a | 29d ago | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 113 | [ ] | Re-Volt (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (71%) | n/a | 20d ago | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 114 | [ ] | Fallout Classic (GOG) | 15 | 20 | 75% (last 20) | Does not open (88%) | n/a | 1d ago | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 115 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | 1d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 116 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | n/a | 26d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 117 | [ ] | Mini Metro (STEAM) | 11 | 20 | 55% (last 20) | Does not open (44%) | 39% | 2d ago | n/a |  |
| 118 | [ ] | Lunarium (STEAM) | 16 | 20 | 80% (last 20) | Does not open (54%) | n/a | 1d ago | n/a |  |
| 119 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | n/a | 18d ago | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 120 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | n/a | 6d ago | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 121 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | n/a | 4d ago | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 122 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (83%) | 32% | 12d ago | 18% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 123 | [ ] | Sandustry (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 4d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 124 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | n/a | 25d ago | n/a |  |
| 125 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | No graphics (57%) | 21% | 7d ago | n/a | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 126 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (50%) | n/a | 5d ago | n/a |  |
| 127 | [ ] | Chef Knight (STEAM) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 18d ago | n/a |  |
| 128 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 3d ago | n/a |  |
| 129 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 56% | 8d ago | 60% |  |
| 130 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 12 | 20 | 60% (last 20) | Does not open (92%) | 58% | 5d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 131 | [ ] | A Plague Tale: Innocence (GOG) | 11 | 20 | 55% (last 20) | Does not open (91%) | 50% | 21d ago | n/a |  |
| 132 | [ ] | Dungeon Keeper™ 2 (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 20d ago | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 133 | [ ] | Beat Cop (STEAM) | 13 | 20 | 65% (last 20) | Does not open (72%) | n/a | 1d ago | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 134 | [ ] | Blood Omen: Legacy of Kain (GOG) | 13 | 20 | 65% (last 20) | Does not open (62%) | 44% | 3d ago | n/a |  |
| 135 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | n/a | 36d ago | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 136 | [ ] | Songs of Conquest (EPIC) | 12 | 20 | 60% (last 20) | Does not open (75%) | n/a | 12d ago | n/a |  |
| 137 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 50% | today | n/a |  |
| 138 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 9d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 139 | [ ] | Mafia: Definitive Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 48% | today | 43% |  |
| 140 | [ ] | Styx: Master of Shadows (EPIC) | 11 | 20 | 55% (last 20) | Does not open (65%) | 31% | 5d ago | n/a |  |
| 141 | [ ] | Forgive Me Father (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 57% | today | n/a |  |
| 142 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 50% | 2d ago | n/a | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 143 | [ ] | This War of Mine (STEAM) | 10 | 20 | 50% (last 20) | Does not open (54%) | 51% | 14d ago | 31% (drop) |  |
| 144 | [ ] | Knights of Pen and Paper 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (42%) | n/a | 5d ago | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 145 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 13 | 20 | 65% (last 20) | No graphics (56%) | n/a | 32d ago | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 146 | [ ] | Fogpiercer (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 27d ago | n/a | [#303](https://github.com/GameNative/gamenative-compat/issues/303) |
| 147 | [ ] | Minit (EPIC) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 6d ago | n/a |  |
| 148 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 15d ago | n/a |  |
| 149 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (78%) | n/a | 8d ago | n/a |  |
| 150 | [ ] | No More Heroes (STEAM) | 10 | 20 | 50% (last 20) | No graphics (71%) | 50% | today | n/a |  |
| 151 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 35% | 9d ago | n/a |  |
| 152 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | n/a | 4d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 153 | [ ] | Ys: Memories of Celceta (STEAM) | 12 | 20 | 60% (last 20) | No graphics (45%) | 36% | 14d ago | n/a |  |
| 154 | [ ] | Dex (GOG) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 3d ago | n/a |  |
| 155 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 54% | 6d ago | n/a |  |
| 156 | [ ] | Turnip Boy Robs a Bank (EPIC) | 11 | 20 | 55% (last 20) | Does not open (62%) | 40% | today | n/a | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 157 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | n/a | 8d ago | n/a |  |
| 158 | [ ] | Secret of Mana (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (55%) | 55% | 27d ago | n/a |  |
| 159 | [ ] | Crying Suns (EPIC) | 11 | 20 | 55% (last 20) | No graphics (57%) | n/a | 4d ago | n/a |  |
| 160 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 10 | 20 | 50% (last 20) | Does not open (86%) | n/a | 79d ago | n/a |  |
| 161 | [ ] | Railway Chai Wala (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | n/a | 7d ago | n/a |  |
| 162 | [ ] | Delver (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 43% | today | 0% (drop) |  |
| 163 | [ ] | Asterigos: Curse of the Stars (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (50%) | n/a | 14d ago | n/a |  |
| 164 | [ ] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 15% | 9d ago | n/a |  |

## Fix shipped, waiting for ratings (17)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | Plants vs. Zombies: Game of the Year (STEAM) | 2026-11-04 | 7 | 5 | 2d ago | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 2 | Transistor (STEAM) | 2026-11-10 | 1 | 1 | 2d ago | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 3 | Max Payne 3 (STEAM) | 2026-11-04 | 1 | 1 | 7d ago | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 4 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 6 | 6 | 7d ago | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 5 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 3 | 3 | 3d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 6 | L.A. Noire (STEAM) | 2026-11-04 | 1 | 1 | today | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 7 | Diablo® IV (STEAM) | 2026-10-20 | 3 | 2 | 5d ago | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 8 | Peggle Deluxe (STEAM) | 2026-10-29 | 1 | 1 | 1d ago | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 9 | Necesse (STEAM) | 2026-10-29 | 5 | 0 | 5d ago | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 10 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 1 | 1 | 3d ago | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 11 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 1 | 1 | 10d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 12 | Need for Speed™ (STEAM) | 2026-11-04 | 0 | 0 | 23d ago | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 13 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 0 | 0 | 11d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 14 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 0 | 0 | 10d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 15 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 9d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 16 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 0 | 0 | 16d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 17 | Need for Speed™ Unbound (STEAM) | 2026-11-04 | 0 | 0 | 17d ago | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |

## Works, but the first launch usually fails (326)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 71 | 87 | 82% (14d) | Does not open (63%) | 91% | today | 94% |  |
| 2 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 60 | 82 | 73% (14d) | Does not open (54%) | 83% | today | 84% |  |
| 3 | [ ] | Grand Theft Auto V Legacy (STEAM) | 40 | 50 | 80% (since fix) | Does not open (88%) | 76% | today | 71% |  |
| 4 | [ ] | Cyberpunk 2077 (STEAM) | 44 | 73 | 60% (14d) | Does not open (68%) | 73% | today | 66% |  |
| 5 | [ ] | Road Rash™: 30th Anniversary Edition (STEAM) | 44 | 60 | 73% (14d) | Does not open (74%) | 61% | 1d ago | 66% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 6 | [ ] | Valheim (STEAM) | 29 | 45 | 64% (since fix) | No graphics (53%) | 88% | 1d ago | 83% |  |
| 7 | [ ] | Half-Life (STEAM) | 40 | 63 | 63% (14d) | Does not open (56%) | 71% | today | 64% |  |
| 8 | [ ] | MONSTER HUNTER RISE (STEAM) | 40 | 67 | 60% (14d) | Does not open (83%) | 61% | today | 61% |  |
| 9 | [ ] | No Man's Sky (STEAM) | 28 | 47 | 60% (since fix) | Controller issues (61%) | 80% | today | 77% |  |
| 10 | [ ] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 37 | 65 | 57% (14d) | Does not open (64%) | 60% | today | 66% |  |
| 11 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 36 | 47 | 77% (14d) | Does not open (77%) | 77% | 1d ago | 74% |  |
| 12 | [ ] | Buckshot Roulette (STEAM) | 32 | 58 | 55% (14d) | Does not open (62%) | 75% | 1d ago | 44% (drop) |  |
| 13 | [ ] | DREDGE (EPIC) | 32 | 38 | 84% (14d) | Does not open (76%) | 67% | today | 50% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 14 | [ ] | Palworld (STEAM) | 27 | 43 | 63% (14d) | Does not open (73%) | 87% | 1d ago | 85% |  |
| 15 | [ ] | Super Meat Boy (STEAM) | 26 | 50 | 52% (14d) | Does not open (56%) | 71% | today | 50% (drop) |  |
| 16 | [ ] | Red Dead Redemption 2 (STEAM) | 18 | 19 | 95% (since fix) | Does not open (98%) | 80% | today | 78% |  |
| 17 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 24 | 36 | 67% (14d) | Does not open (56%) | 74% | today | 63% |  |
| 18 | [ ] | Counter-Strike 2 (STEAM) | 39 | 54 | 72% (since fix) | Does not open (67%) | 60% | today | 68% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 19 | [ ] | ELDEN RING (STEAM) | 22 | 39 | 56% (14d) | Does not open (85%) | 72% | today | 66% |  |
| 20 | [ ] | Quake (STEAM) | 21 | 32 | 66% (14d) | Does not open (66%) | 83% | today | 58% (drop) |  |
| 21 | [ ] | Deadlock (STEAM) | 18 | 22 | 82% (14d) | Does not open (54%) | 86% | today | 81% |  |
| 22 | [ ] | Devil May Cry 5 (STEAM) | 17 | 28 | 61% (14d) | Does not open (83%) | 74% | today | 81% |  |
| 23 | [ ] | DRAGON BALL FighterZ (STEAM) | 26 | 43 | 60% (since fix) | Does not open (90%) | 79% | today | 88% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 24 | [ ] | BioShock Remastered (EPIC) | 16 | 22 | 73% (14d) | Does not open (65%) | 71% | today | 59% |  |
| 25 | [ ] | Mortal Kombat X (STEAM) | 16 | 25 | 64% (14d) | Does not open (72%) | 88% | 1d ago | 91% |  |
| 26 | [ ] | BeamNG.drive (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 80% | today | 57% (drop) | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 27 | [ ] | CHRONO TRIGGER (STEAM) | 15 | 25 | 60% (14d) | Does not open (59%) | 84% | 2d ago | 97% |  |
| 28 | [ ] | Crypt of the NecroDancer (STEAM) | 15 | 30 | 50% (14d) | Does not open (50%) | 90% | 2d ago | 89% |  |
| 29 | [ ] | Clair Obscur: Expedition 33 (STEAM) | 14 | 26 | 54% (14d) | Graphics glitches (41%) | 84% | today | 76% |  |
| 30 | [ ] | Divinity: Original Sin 2 (STEAM) | 14 | 22 | 64% (14d) | Does not open (74%) | 88% | today | 79% |  |
| 31 | [ ] | Mass Effect™ Legendary Edition (STEAM) | 9 | 17 | 53% (since fix) | Does not open (87%) | 79% | today | 84% |  |
| 32 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (88%) | 94% | 1d ago | 93% |  |
| 33 | [ ] | Resident Evil 4 (2005) (STEAM) | 13 | 25 | 52% (14d) | Does not open (69%) | 72% | today | 70% |  |
| 34 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 71% | 5d ago | 65% |  |
| 35 | [ ] | Batman™: Arkham Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (84%) | 75% | today | 63% |  |
| 36 | [ ] | METAL GEAR SOLID 4: Guns of the Patriots - Master Collection Version (STEAM) | 12 | 21 | 57% (14d) | Does not open (80%) | 89% | 2d ago | 92% |  |
| 37 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (58%) | 82% | today | 59% (drop) |  |
| 38 | [ ] | Grand Theft Auto V (EPIC) | 19 | 20 | 95% (last 20) | Does not open (89%) | 77% | 1d ago | 74% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 39 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 18 | 35 | 51% (since fix) | Does not open (74%) | 64% | today | 51% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 40 | [ ] | Cyberpunk 2077 (GOG) | 13 | 20 | 65% (last 20) | Does not open (71%) | 71% | today | 54% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 41 | [ ] | The Forest (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 85% | 1d ago | 86% |  |
| 42 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 66% | 1d ago | 45% (drop) |  |
| 43 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (79%) | 98% | 1d ago | 94% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 44 | [ ] | Fallout: New Vegas (EPIC) | 15 | 20 | 75% (last 20) | Does not open (60%) | 85% | 3d ago | 73% |  |
| 45 | [ ] | Dead Island 2 (EPIC) | 15 | 20 | 75% (last 20) | Does not open (82%) | 78% | 3d ago | 58% (drop) |  |
| 46 | [ ] | DOOM 3: BFG Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (72%) | 71% | today | 63% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 47 | [ ] | Don't Starve Together (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 78% | today | 65% |  |
| 48 | [ ] | eFootball™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (63%) | 66% | 1d ago | 55% |  |
| 49 | [ ] | Library Of Ruina (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 88% | today | 79% |  |
| 50 | [ ] | Deskrawl: Idle ARPG (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 83% | 3d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 51 | [ ] | Order of the Sinking Star (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | 66% | 2d ago | 71% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 52 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (73%) | 100% | today | n/a | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 53 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 78% | 1d ago | 81% |  |
| 54 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (49%) | 91% | today | 87% |  |
| 55 | [ ] | Castlevania Dominus Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (92%) | 97% | 1d ago | 89% |  |
| 56 | [ ] | Aniimo (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 81% | 2d ago | 72% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 57 | [ ] | Hogwarts Legacy (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | 66% | today | 44% (drop) |  |
| 58 | [ ] | Cry of Fear (STEAM) | 13 | 20 | 65% (last 20) | Does not open (48%) | 73% | today | 70% |  |
| 59 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (82%) | 72% | 5d ago | 50% (drop) |  |
| 60 | [ ] | Disgaea 5 Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (74%) | 89% | today | 86% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 61 | [ ] | Dead Space (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | 84% | today | 85% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 62 | [ ] | Alabaster Dawn (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (48%) | 89% | today | 86% |  |
| 63 | [ ] | Sid Meier's Civilization VI (STEAM) | 15 | 20 | 75% (last 20) | Does not open (66%) | 85% | 2d ago | 71% |  |
| 64 | [ ] | MIO: Memories in Orbit (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (51%) | 95% | 4d ago | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 65 | [ ] | Resident Evil 7 Biohazard (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 79% | 1d ago | 69% |  |
| 66 | [ ] | Welcome to Elderfield (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 70% | today | 67% |  |
| 67 | [ ] | Need for Speed: Hot Pursuit (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 82% | today | 89% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 68 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (51%) | 77% | today | 41% (drop) | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 69 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 15 | 20 | 75% (last 20) | Graphics glitches (44%) | 86% | today | 80% |  |
| 70 | [ ] | OMORI (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 74% | today | 54% (drop) | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 71 | [ ] | Call of Duty 4: Modern Warfare (2007) (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (52%) | 87% | today | 62% |  |
| 72 | [ ] | Prey (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 79% | 3d ago | 81% |  |
| 73 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 15 | 20 | 75% (last 20) | Does not open (44%) | 74% | today | 67% |  |
| 74 | [ ] | Fable - The Lost Chapters (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (48%) | 85% | today | 87% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 75 | [ ] | ZERO Sievert (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | 89% | today | 73% |  |
| 76 | [ ] | Forza Horizon 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (45%) | 65% | 1d ago | 21% (drop) | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 77 | [ ] | Dota 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (78%) | 75% | 2d ago | 93% |  |
| 78 | [ ] | Poppy Playtime (STEAM) | 12 | 20 | 60% (last 20) | Does not open (60%) | 72% | today | 61% |  |
| 79 | [ ] | Darkest Dungeon® (EPIC) | 11 | 20 | 55% (last 20) | Does not open (63%) | 77% | 1d ago | 100% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 80 | [ ] | Ratatan (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 97% | 1d ago | n/a |  |
| 81 | [ ] | American Truck Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (68%) | 78% | today | 71% |  |
| 82 | [ ] | STAR WARS™ Knights of the Old Republic™ II: The Sith Lords™ (STEAM) | 11 | 20 | 55% (last 20) | No graphics (72%) | 77% | today | 39% (drop) |  |
| 83 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 66% | today | 71% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 84 | [ ] | Happy Wheels (STEAM) | 19 | 20 | 95% (last 20) | No graphics (52%) | 73% | 7d ago | 48% (drop) | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 85 | [ ] | Cave Story+ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | 84% | 3d ago | 68% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 86 | [ ] | Need for Speed™ Rivals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (62%) | 73% | 3d ago | 91% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 87 | [ ] | Abiotic Factor (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 69% | 3d ago | 81% |  |
| 88 | [ ] | Fate/stay night REMASTERED (STEAM) | 12 | 20 | 60% (last 20) | Does not open (44%) | 91% | today | 72% |  |
| 89 | [ ] | Disco Elysium - The Final Cut (EPIC) | 10 | 20 | 50% (last 20) | Does not open (70%) | 98% | 1d ago | 97% |  |
| 90 | [ ] | Resident Evil Village (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 89% | 2d ago | 81% |  |
| 91 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (62%) | 97% | 1d ago | 100% |  |
| 92 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 89% | today | 77% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 93 | [ ] | River City Girls (EPIC) | 13 | 20 | 65% (last 20) | No graphics (52%) | 77% | today | 46% (drop) |  |
| 94 | [ ] | Until Then (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | 80% | today | 60% |  |
| 95 | [ ] | Mini Motorways (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 70% | today | 61% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 96 | [ ] | Quake II (STEAM) | 10 | 20 | 50% (last 20) | No graphics (48%) | 88% | today | 80% |  |
| 97 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (81%) | 79% | 2d ago | n/a | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 98 | [ ] | Bejeweled 3 (STEAM) | 10 | 20 | 50% (last 20) | No graphics (59%) | 92% | 1d ago | 90% |  |
| 99 | [ ] | Sid Meier's Civilization V (STEAM) | 16 | 20 | 80% (last 20) | Does not open (75%) | 64% | today | 61% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 100 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 12 | 20 | 60% (last 20) | Does not open (100%) | 96% | 3d ago | 82% |  |
| 101 | [ ] | Red Dead Redemption (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | 67% | 25d ago | 42% (drop) | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 102 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 17 | 20 | 85% (last 20) | Controller issues (82%) | 89% | today | 80% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 103 | [ ] | Palia (STEAM) | 15 | 20 | 75% (last 20) | Does not open (57%) | 75% | 7d ago | 70% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 104 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 14 | 20 | 70% (last 20) | Does not open (43%) | 67% | 1d ago | 62% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 105 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 13 | 20 | 65% (last 20) | Does not open (82%) | 67% | 5d ago | n/a | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 106 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 63% | 7d ago | 64% |  |
| 107 | [ ] | Castlevania Anniversary Collection (EPIC) | 10 | 20 | 50% (last 20) | Does not open (68%) | 74% | today | 37% (drop) |  |
| 108 | [ ] | Lethal Company (STEAM) | 10 | 20 | 50% (last 20) | Does not open (42%) | 81% | 2d ago | 76% |  |
| 109 | [ ] | Cat Quest (EPIC) | 10 | 20 | 50% (last 20) | No graphics (45%) | 66% | today | 41% (drop) |  |
| 110 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (57%) | 64% | 2d ago | n/a |  |
| 111 | [ ] | TBH: Task Bar Hero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (64%) | 83% | 2d ago | 80% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 112 | [ ] | Minecraft Dungeons II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (82%) | 68% | 1d ago | 73% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 113 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | Directx error (36%) | 65% | 6d ago | 32% (drop) |  |
| 114 | [ ] | The Legend of Heroes: Trails in the Sky (STEAM) | 10 | 20 | 50% (last 20) | Does not open (55%) | 94% | 1d ago | 92% |  |
| 115 | [ ] | Yakuza: Like a Dragon (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 65% | 6d ago | 77% |  |
| 116 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 66% | 2d ago | 76% |  |
| 117 | [ ] | Deliver At All Costs (EPIC) | 13 | 20 | 65% (last 20) | Does not open (58%) | 63% | 1d ago | 56% |  |
| 118 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 74% | 1d ago | 71% |  |
| 119 | [ ] | Overwatch® (STEAM) | 18 | 20 | 90% (last 20) | Does not open (57%) | 62% | 6d ago | n/a | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 120 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 18 | 20 | 90% (last 20) | Does not open (59%) | 83% | today | n/a | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 121 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (77%) | 91% | today | n/a | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 122 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (50%) | 83% | 3d ago | 69% |  |
| 123 | [ ] | Driving Rogue (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 95% | 7d ago | 85% |  |
| 124 | [ ] | ENA: Dream BBQ (STEAM) | 10 | 20 | 50% (last 20) | Does not open (43%) | 78% | today | 62% |  |
| 125 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 64% | 12d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 126 | [ ] | Sonic Generations (STEAM) | 16 | 20 | 80% (last 20) | Does not open (69%) | 68% | 6d ago | 85% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 127 | [ ] | Moonstone Island (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (60%) | 78% | 3d ago | 71% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 128 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 94% | 15d ago | n/a |  |
| 129 | [ ] | Fallout (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 70% | 3d ago | 76% |  |
| 130 | [ ] | Heavy Rain (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (65%) | 88% | 1d ago | 90% |  |
| 131 | [ ] | Dishonored - Definitive Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (89%) | 79% | 1d ago | 70% |  |
| 132 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 86% | 1d ago | 83% |  |
| 133 | [ ] | Tails of Iron (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 86% | 5d ago | n/a |  |
| 134 | [ ] | A Plague Tale: Innocence (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | 80% | 15d ago | 80% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 135 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (73%) | 61% | 2d ago | n/a | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 136 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (88%) | 75% | 3d ago | 73% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 137 | [ ] | Chained Echoes (GOG) | 14 | 20 | 70% (last 20) | Does not open (60%) | 63% | today | n/a |  |
| 138 | [ ] | Call of Duty: World at War (STEAM) | 13 | 20 | 65% (last 20) | Does not open (44%) | 86% | today | 69% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 139 | [ ] | PowerWash Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (81%) | 79% | 1d ago | 100% |  |
| 140 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (86%) | 92% | 1d ago | 93% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 141 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (48%) | 91% | 4d ago | 83% |  |
| 142 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (84%) | 93% | 1d ago | 92% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 143 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 63% | 1d ago | 67% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 144 | [ ] | Astral Party  (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 93% | today | n/a |  |
| 145 | [ ] | Fallout 3 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (43%) | 89% | 4d ago | 88% |  |
| 146 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | 86% | today | n/a | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 147 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (82%) | 94% | 2d ago | n/a | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 148 | [ ] | Max Payne (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (46%) | 88% | today | 79% |  |
| 149 | [ ] | Selaco (STEAM) | 13 | 20 | 65% (last 20) | Does not open (86%) | 72% | today | 52% (drop) |  |
| 150 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 84% | 2d ago | 80% |  |
| 151 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (81%) | 76% | 12d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 152 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 76% | 7d ago | 83% |  |
| 153 | [ ] | Rivals of Aether II (STEAM) | 15 | 20 | 75% (last 20) | Does not open (55%) | 64% | today | 9% (drop) | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 154 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (92%) | 63% | 15d ago | n/a | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 155 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 82% | 1d ago | 75% |  |
| 156 | [ ] | Sonic Lost World (STEAM) | 11 | 20 | 55% (last 20) | No graphics (65%) | 79% | 1d ago | 79% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 157 | [ ] | Street Fighter™ 6 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (81%) | 81% | 2d ago | 77% |  |
| 158 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 72% | 1d ago | 46% (drop) |  |
| 159 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (62%) | 83% | 9d ago | n/a | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 160 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | 81% | 1d ago | n/a | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 161 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | 91% | 13d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 162 | [ ] | Stellar Blade™ (STEAM) | 14 | 20 | 70% (last 20) | No graphics (43%) | 80% | 4d ago | 83% |  |
| 163 | [ ] | Gambonanza (STEAM) | 13 | 20 | 65% (last 20) | Does not open (60%) | 92% | 1d ago | 93% |  |
| 164 | [ ] | Gothic 1 Classic (STEAM) | 12 | 20 | 60% (last 20) | Does not open (61%) | 78% | 5d ago | 53% (drop) |  |
| 165 | [ ] | Oxygen Not Included (STEAM) | 12 | 20 | 60% (last 20) | Does not open (78%) | 61% | 5d ago | 78% |  |
| 166 | [ ] | ABZU (EPIC) | 10 | 20 | 50% (last 20) | Does not open (86%) | 88% | 5d ago | 80% |  |
| 167 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 70% | today | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 168 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 84% | today | 83% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 169 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (55%) | 65% | 2d ago | 56% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 170 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 11 | 20 | 55% (last 20) | Does not open (59%) | 70% | 11d ago | 70% |  |
| 171 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 65% | 5d ago | n/a | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 172 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (57%) | 67% | 12d ago | n/a | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 173 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (64%) | 62% | 3d ago | n/a | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 174 | [ ] | Tabletop Simulator (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 66% | today | 79% |  |
| 175 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 84% | 5d ago | 100% |  |
| 176 | [ ] | Control Ultimate Edition (GOG) | 13 | 20 | 65% (last 20) | Does not open (76%) | 86% | 3d ago | 77% |  |
| 177 | [ ] | State of Decay: Year-One (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 77% | today | 73% |  |
| 178 | [ ] | Unturned (STEAM) | 12 | 20 | 60% (last 20) | Does not open (47%) | 71% | 3d ago | 76% |  |
| 179 | [ ] | Limbus Company (STEAM) | 12 | 20 | 60% (last 20) | Does not open (86%) | 86% | today | 94% |  |
| 180 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (72%) | 74% | 6d ago | n/a | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 181 | [ ] | Assetto Corsa (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (50%) | 78% | today | 84% |  |
| 182 | [ ] | Counter-Strike:Global Offensive (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 80% | 4d ago | 80% |  |
| 183 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (61%) | 92% | 9d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 184 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 90% | 24d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 185 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 90% | 2d ago | 85% |  |
| 186 | [ ] | One-armed robber (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (65%) | 74% | 6d ago | 55% |  |
| 187 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 67% | today | 40% (drop) | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 188 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | 73% | 6d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 189 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (82%) | 91% | 14d ago | 75% |  |
| 190 | [ ] | Mortal Kombat 11 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 71% | today | n/a |  |
| 191 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 62% | 2d ago | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 192 | [ ] | Capcom Arcade Stadium (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | 74% | 1d ago | 80% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 193 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 92% | 4d ago | n/a |  |
| 194 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 60% | 10d ago | n/a |  |
| 195 | [ ] | Dishonored 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (89%) | 82% | 5d ago | 68% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 196 | [ ] | Escape from Duckov (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (69%) | 93% | 1d ago | 96% |  |
| 197 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (47%) | 61% | 4d ago | 50% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 198 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | 95% | 3d ago | n/a | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 199 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 20 | 80% (last 20) | No graphics (53%) | 73% | today | 40% (drop) | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 200 | [ ] | Digimon Survive (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (77%) | 93% | 2d ago | 82% |  |
| 201 | [ ] | TurretGirls (STEAM) | 12 | 20 | 60% (last 20) | No graphics (75%) | 92% | 1d ago | 83% |  |
| 202 | [ ] | Final Fantasy IV (3D Remake) (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 95% | 3d ago | 100% |  |
| 203 | [ ] | The Witcher: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (59%) | 68% | 7d ago | n/a | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 204 | [ ] | Stumble Guys (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 69% | today | 59% |  |
| 205 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (56%) | 73% | 8d ago | n/a | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 206 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (69%) | 93% | 19d ago | n/a | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 207 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (72%) | 84% | 2d ago | n/a | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 208 | [ ] | Supermarket Together (STEAM) | 15 | 20 | 75% (last 20) | Does not open (73%) | 66% | 9d ago | 73% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 209 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (62%) | 64% | 2d ago | 25% (drop) |  |
| 210 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (60%) | 66% | 4d ago | 55% |  |
| 211 | [ ] | My Summer Car (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | 79% | today | 80% |  |
| 212 | [ ] | Moonring (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 93% | 1d ago | 86% |  |
| 213 | [ ] | Battle Brothers (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 79% | 1d ago | 85% |  |
| 214 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 100% | 3d ago | n/a | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 215 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 87% | 8d ago | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 216 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (65%) | 94% | 9d ago | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 217 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 74% | 17d ago | n/a | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 218 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 70% | 3d ago | n/a | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 219 | [ ] | Darksiders (STEAM) | 13 | 20 | 65% (last 20) | Does not open (68%) | 80% | 20d ago | 75% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 220 | [ ] | Lucid Blocks (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 63% | 1d ago | 57% |  |
| 221 | [ ] | GOD EATER RESURRECTION (STEAM) | 14 | 20 | 70% (last 20) | Does not open (59%) | 72% | today | n/a |  |
| 222 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (67%) | 69% | 2d ago | n/a | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 223 | [ ] | Resident Evil Revelations 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (42%) | 83% | today | 76% |  |
| 224 | [ ] | Goat Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 74% | today | n/a |  |
| 225 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 78% | 2d ago | 75% |  |
| 226 | [ ] | Jade Empire: Special Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 75% | 5d ago | n/a | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 227 | [ ] | Undisputed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 67% | 6d ago | n/a | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 228 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 80% | 2d ago | n/a |  |
| 229 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | 70% | 11d ago | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 230 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (92%) | 86% | 27d ago | n/a |  |
| 231 | [ ] | Invisible, Inc. (STEAM) | 15 | 20 | 75% (last 20) | Does not open (63%) | 73% | 15d ago | n/a |  |
| 232 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 73% | 17d ago | 60% |  |
| 233 | [ ] | Ultimate Custom Night (STEAM) | 14 | 20 | 70% (last 20) | No graphics (68%) | 64% | 16d ago | n/a | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 234 | [ ] | Return to Monkey Island (STEAM) | 14 | 20 | 70% (last 20) | No graphics (62%) | 76% | 7d ago | n/a |  |
| 235 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (42%) | 77% | 9d ago | n/a | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 236 | [ ] | SnowRunner (STEAM) | 13 | 20 | 65% (last 20) | Does not open (96%) | 78% | 5d ago | n/a | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 237 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (44%) | 83% | 7d ago | n/a |  |
| 238 | [ ] | Zero Escape: The Nonary Games (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 63% | 4d ago | 68% |  |
| 239 | [ ] | MX Bikes (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 93% | 1d ago | n/a |  |
| 240 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 85% | 4d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 241 | [ ] | Revolution Idle (STEAM) | 12 | 20 | 60% (last 20) | Does not open (43%) | 73% | 7d ago | n/a |  |
| 242 | [ ] | Secrets of Grindea (STEAM) | 11 | 20 | 55% (last 20) | Does not open (48%) | 74% | today | 82% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 243 | [ ] | Trailmakers (STEAM) | 11 | 20 | 55% (last 20) | Does not open (44%) | 92% | today | 90% |  |
| 244 | [ ] | Serious Sam 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (63%) | 90% | 1d ago | n/a |  |
| 245 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 20 | 80% (last 20) | Does not open (82%) | 63% | 21d ago | n/a | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 246 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 60% | 2d ago | n/a |  |
| 247 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (83%) | 82% | 6d ago | n/a | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 248 | [ ] | Cat Mail Co. (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 85% | today | 82% |  |
| 249 | [ ] | Deus Ex™ GOTY Edition (GOG) | 12 | 20 | 60% (last 20) | No graphics (44%) | 87% | 14d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 250 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 67% | 5d ago | n/a |  |
| 251 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (41%) | 92% | today | n/a |  |
| 252 | [ ] | Bongo Cat (STEAM) | 15 | 20 | 75% (last 20) | Does not open (70%) | 74% | 8d ago | n/a | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 253 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 13 | 20 | 65% (last 20) | No graphics (37%) | 87% | 3d ago | n/a | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 254 | [ ] | PAYDAY: The Heist (STEAM) | 13 | 20 | 65% (last 20) | Does not open (75%) | 70% | 7d ago | n/a |  |
| 255 | [ ] | Sacred Gold (STEAM) | 13 | 20 | 65% (last 20) | Does not open (91%) | 70% | today | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 256 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (100%) | 76% | 9d ago | n/a |  |
| 257 | [ ] | 12 is Better Than 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 91% | 9d ago | n/a |  |
| 258 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 89% | 6d ago | n/a |  |
| 259 | [ ] | Big Walk (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 70% | 11d ago | 42% (drop) |  |
| 260 | [ ] | CRUEL (STEAM) | 11 | 20 | 55% (last 20) | Does not open (92%) | 69% | today | n/a | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 261 | [ ] | Hitman: Absolution (GOG) | 11 | 20 | 55% (last 20) | Does not open (85%) | 73% | 8d ago | n/a |  |
| 262 | [ ] | Hero Siege (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (50%) | 72% | 3d ago | 92% |  |
| 263 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 80% | today | 70% |  |
| 264 | [ ] | Tales of Zestiria (STEAM) | 14 | 20 | 70% (last 20) | Does not open (79%) | 67% | 19d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 265 | [ ] | Capcom Fighting Collection (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 78% | 5d ago | n/a | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 266 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 14 | 20 | 70% (last 20) | Does not open (85%) | 67% | 6d ago | n/a | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 267 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (95%) | 95% | 5d ago | 89% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 268 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (45%) | 69% | today | n/a |  |
| 269 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (89%) | 80% | 6d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 270 | [ ] | Allumeria (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 75% | 4d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 271 | [ ] | Sons Of The Forest (STEAM) | 13 | 20 | 65% (last 20) | Does not open (57%) | 79% | 7d ago | n/a |  |
| 272 | [ ] | Disgaea 4 Complete+ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (43%) | 91% | 13d ago | n/a | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 273 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 12 | 20 | 60% (last 20) | Does not open (57%) | 69% | 9d ago | n/a | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 274 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 88% | 6d ago | n/a |  |
| 275 | [ ] | Hatred (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 88% | 6d ago | n/a |  |
| 276 | [ ] | Football Manager 2024 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (91%) | 67% | 6d ago | 47% (drop) |  |
| 277 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 94% | 2d ago | 88% |  |
| 278 | [ ] | Timberborn (STEAM) | 13 | 20 | 65% (last 20) | No graphics (62%) | 85% | 11d ago | n/a |  |
| 279 | [ ] | AER Memories of Old (EPIC) | 13 | 20 | 65% (last 20) | Does not open (85%) | 93% | 2d ago | n/a |  |
| 280 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 77% | 4d ago | n/a |  |
| 281 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (77%) | 72% | 27d ago | n/a |  |
| 282 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 65% | 5d ago | 55% |  |
| 283 | [ ] | Mortal Shell (EPIC) | 12 | 20 | 60% (last 20) | No graphics (58%) | 64% | today | 25% (drop) |  |
| 284 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 60% | 1d ago | 40% (drop) |  |
| 285 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (45%) | 79% | 6d ago | n/a | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 286 | [ ] | BATTLETECH (STEAM) | 11 | 20 | 55% (last 20) | Does not open (43%) | 89% | 1d ago | n/a |  |
| 287 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 85% | 4d ago | 70% |  |
| 288 | [ ] | Monster Boy And The Cursed Kingdom (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (84%) | 90% | today | n/a |  |
| 289 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 71% | 5d ago | 67% |  |
| 290 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 95% | 12d ago | 100% |  |
| 291 | [ ] | Spark the Electric Jester (STEAM) | 14 | 20 | 70% (last 20) | Does not open (58%) | 64% | 9d ago | n/a | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 292 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (58%) | 70% | 11d ago | n/a |  |
| 293 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 60% | 4d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 294 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | 90% | 8d ago | n/a |  |
| 295 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 60% | 2d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 296 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (92%) | 88% | 9d ago | n/a |  |
| 297 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (70%) | 62% | 2d ago | n/a |  |
| 298 | [ ] | Antichamber (STEAM) | 11 | 20 | 55% (last 20) | Does not open (33%) | 73% | 3d ago | n/a |  |
| 299 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 73% | today | n/a |  |
| 300 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 69% | 3d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 301 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 64% | 30d ago | n/a |  |
| 302 | [ ] | Pinball FX Classic (STEAM) | 10 | 20 | 50% (last 20) | Does not open (79%) | 94% | 9d ago | n/a |  |
| 303 | [ ] | Hylics (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (67%) | 97% | 1d ago | n/a |  |
| 304 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (44%) | 73% | 42d ago | n/a |  |
| 305 | [ ] | Legend of Grimrock 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 86% | 7d ago | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 306 | [ ] | The Stanley Parable (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 69% | today | n/a |  |
| 307 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | 90% | today | n/a |  |
| 308 | [ ] | LET IT DIE (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 60% | 8d ago | n/a |  |
| 309 | [ ] | Assassin's Creed Odyssey (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 67% | 7d ago | 70% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 310 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 95% | 2d ago | 100% |  |
| 311 | [ ] | GRANDIA II HD Remaster (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 73% | 17d ago | n/a |  |
| 312 | [ ] | Subnautica: Below Zero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 76% | 5d ago | 55% (drop) |  |
| 313 | [ ] | Intravenous (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 75% | 5d ago | n/a |  |
| 314 | [ ] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 20 | 65% (last 20) | Does not open (78%) | 85% | 10d ago | 80% |  |
| 315 | [ ] | Shift At Midnight (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | 84% | 8d ago | 83% |  |
| 316 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (56%) | 92% | 16d ago | n/a | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 317 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 75% | 7d ago | 70% |  |
| 318 | [ ] | Haydee (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 82% | 8d ago | n/a |  |
| 319 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 70% | 7d ago | n/a |  |
| 320 | [ ] | Killing Floor (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (100%) | 86% | 6d ago | n/a |  |
| 321 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 64% | 1d ago | n/a |  |
| 322 | [ ] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | 70% | 1d ago | 85% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 323 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 86% | 4d ago | 82% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 324 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 67% | 5d ago | n/a | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 325 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 92% | today | 90% |  |
| 326 | [ ] | Sid Meier's Civilization VI (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 76% | 11d ago | 40% (drop) |  |

## Recently recovered (482)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Grim Dawn (STEAM) | 520 | 2026-11-08 | 582 | 64% |  |
| 2 | [x] | FINAL FANTASY RESONANCE (STEAM) | 415 | 2026-10-24 | 936 | 78% |  |
| 3 | [x] | Half-Life (STEAM) | 351 | 2026-11-09 | 619 | 71% |  |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 258 | 2026-11-14 | 405 | 60% |  |
| 5 | [x] | Alan Wake (STEAM) | 240 | 2026-11-14 | 263 | 31% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 6 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 229 | 2026-11-09 | 322 | 89% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 7 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 226 | 2026-10-19 | 286 | 70% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 8 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 219 | 2026-11-09 | 262 | 65% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 9 | [x] | MONSTER HUNTER RISE (STEAM) | 210 | 2026-11-09 | 507 | 61% |  |
| 10 | [x] | Counter-Strike 2 (STEAM) | 207 | 2026-11-13 | 291 | 60% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 11 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 202 | 2026-11-09 | 357 | 74% |  |
| 12 | [x] | Devil May Cry HD Collection (STEAM) | 200 | 2026-10-19 | 290 | 81% |  |
| 13 | [x] | BeamNG.drive (STEAM) | 199 | 2026-11-09 | 241 | 80% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 14 | [x] | Call of Duty: Black Ops (STEAM) | 197 | 2026-11-13 | 222 | 23% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 15 | [x] | OMORI (STEAM) | 191 | 2026-11-09 | 236 | 74% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 16 | [x] | DRAGON BALL FighterZ (STEAM) | 181 | 2026-11-01 | 218 | 79% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 17 | [x] | Spelunky 2 (STEAM) | 180 | 2026-11-01 | 214 | 70% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 18 | [x] | DREDGE (EPIC) | 169 | 2026-11-09 | 211 | 67% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 19 | [x] | Sid Meier's Civilization V (STEAM) | 166 | 2026-11-10 | 177 | 64% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 20 | [x] | BioShock (STEAM) | 152 | 2026-11-09 | 301 | 74% |  |
| 21 | [x] | Geometry Dash (STEAM) | 148 | 2026-11-11 | 442 | 50% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 22 | [x] | Prototype (STEAM) | 141 | 2026-11-11 | 206 | 54% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 23 | [x] | Team Fortress 2 (STEAM) | 136 | 2026-11-09 | 232 | 76% |  |
| 24 | [x] | Castlevania Advance Collection (STEAM) | 134 | 2026-11-09 | 208 | 89% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 25 | [x] | Burnout Paradise: The Ultimate Box (STEAM) | 133 | 2026-10-16 | 235 | 73% |  |
| 26 | [x] | Minecraft Dungeons II (STEAM) | 129 | 2026-11-09 | 148 | 68% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 27 | [x] | Counter-Strike (STEAM) | 127 | 2026-11-11 | 207 | 46% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 28 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 127 | 2026-11-09 | 170 | 64% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 29 | [x] | Mirror's Edge (STEAM) | 125 | 2026-11-09 | 177 | 72% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 30 | [x] | Call of Duty: Black Ops III (STEAM) | 122 | 2026-10-18 | 251 | 79% |  |
| 31 | [x] | Assassin's Creed II (STEAM) | 118 | 2026-11-10 | 123 | 66% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 32 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 117 | 2026-10-18 | 171 | 77% |  |
| 33 | [x] | Aniimo (STEAM) | 112 | 2026-11-09 | 151 | 81% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 34 | [x] | Euro Truck Simulator 2 (STEAM) | 111 | 2026-11-14 | 209 | 57% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 35 | [x] | The Witcher: Enhanced Edition (STEAM) | 111 | 2026-11-09 | 129 | 68% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 36 | [x] | Cave Story+ (STEAM) | 105 | 2026-11-09 | 116 | 84% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 37 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 104 | 2026-11-09 | 142 | 93% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 38 | [x] | Caravan SandWitch (EPIC) | 99 | 2026-11-09 | 164 | 69% |  |
| 39 | [x] | Moonstone Island (STEAM) | 98 | 2026-11-09 | 130 | 78% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 40 | [x] | Happy Wheels (STEAM) | 97 | 2026-11-09 | 117 | 73% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 41 | [x] | Catherine Classic (STEAM) | 89 | 2026-11-09 | 167 | 70% |  |
| 42 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 89 | 2026-11-09 | 115 | 92% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 43 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 87 | 2026-11-09 | 140 | 71% |  |
| 44 | [x] | Hi-Fi RUSH (STEAM) | 87 | 2026-11-11 | 121 | 45% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 45 | [x] | Quake (STEAM) | 86 | 2026-11-09 | 257 | 83% |  |
| 46 | [x] | DOOM 3: BFG Edition (STEAM) | 84 | 2026-11-09 | 124 | 71% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 47 | [x] | Ultra Street Fighter IV (STEAM) | 83 | 2026-10-17 | 181 | 69% |  |
| 48 | [x] | Cry of Fear (STEAM) | 83 | 2026-10-18 | 166 | 73% |  |
| 49 | [x] | Vital Shell (STEAM) | 83 | 2026-11-09 | 131 | 85% |  |
| 50 | [x] | FINAL FANTASY XIII-2 (STEAM) | 81 | 2026-11-09 | 84 | 65% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 51 | [x] | Age of Empires II: Definitive Edition (STEAM) | 80 | 2026-11-10 | 96 | 63% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 52 | [x] | Psychonauts (STEAM) | 79 | 2026-11-09 | 147 | 94% |  |
| 53 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 79 | 2026-10-18 | 134 | 97% |  |
| 54 | [x] | STEINS;GATE (STEAM) | 78 | 2026-11-09 | 112 | 92% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 55 | [x] | Ballionaire (STEAM) | 75 | 2026-11-09 | 123 | 87% |  |
| 56 | [x] | Don't Starve Together (STEAM) | 74 | 2026-10-16 | 156 | 78% |  |
| 57 | [x] | Brawlhalla (STEAM) | 73 | 2026-11-09 | 145 | 73% |  |
| 58 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 73 | 2026-11-09 | 113 | 87% |  |
| 59 | [x] | Disgaea 5 Complete (STEAM) | 72 | 2026-11-09 | 84 | 89% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 60 | [x] | Sovereign Tower (STEAM) | 71 | 2026-11-09 | 125 | 75% |  |
| 61 | [x] | Spyro™ Reignited Trilogy (STEAM) | 70 | 2026-11-09 | 110 | 74% |  |
| 62 | [x] | The Sims™ 4 (STEAM) | 70 | 2026-11-09 | 92 | 76% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 63 | [x] | Cyberpunk 2077 (GOG) | 70 | 2026-11-09 | 90 | 71% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 64 | [x] | Need for Speed: Hot Pursuit (STEAM) | 69 | 2026-11-09 | 104 | 82% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 65 | [x] | Stardew Valley (GOG) | 68 | 2026-11-11 | 120 | 69% |  |
| 66 | [x] | Fable - The Lost Chapters (STEAM) | 68 | 2026-11-09 | 106 | 85% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 67 | [x] | Dota 2 (STEAM) | 68 | 2026-11-09 | 102 | 75% |  |
| 68 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 67 | 2026-11-09 | 103 | 81% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 69 | [x] | Diablo® IV (STEAM) | 67 | 2026-11-11 | 79 | 58% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 70 | [x] | Bayonetta (STEAM) | 66 | 2026-10-18 | 205 | 83% |  |
| 71 | [x] | American Truck Simulator (STEAM) | 66 | 2026-11-09 | 111 | 78% |  |
| 72 | [x] | Hogwarts Legacy (EPIC) | 66 | 2026-11-09 | 99 | 66% |  |
| 73 | [x] | MIO: Memories in Orbit (STEAM) | 65 | 2026-11-09 | 121 | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 74 | [x] | Gunfire Reborn (STEAM) | 64 | 2026-11-09 | 70 | 86% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 75 | [x] | Don't Starve (STEAM) | 63 | 2026-10-16 | 157 | 81% |  |
| 76 | [x] | Fallout (STEAM) | 63 | 2026-11-09 | 98 | 70% |  |
| 77 | [x] | Order of the Sinking Star (STEAM) | 63 | 2026-11-09 | 91 | 66% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 78 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 62 | 2026-11-09 | 87 | 77% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 79 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 62 | 2026-11-11 | 78 | 50% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 80 | [x] | Call of Juarez Gunslinger (STEAM) | 62 | 2026-11-09 | 77 | 75% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 81 | [x] | Firewatch (STEAM) | 61 | 2026-11-10 | 118 | 69% |  |
| 82 | [x] | Poppy Playtime (STEAM) | 61 | 2026-11-09 | 104 | 72% |  |
| 83 | [x] | Borderlands 3 (STEAM) | 60 | 2026-11-09 | 83 | 88% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 84 | [x] | Sol Cesto (EPIC) | 60 | 2026-11-09 | 61 | 79% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 85 | [x] | Borderlands: The Pre-Sequel (STEAM) | 59 | 2026-11-09 | 93 | 63% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 86 | [x] | eFootball™ (STEAM) | 59 | 2026-11-09 | 87 | 66% |  |
| 87 | [x] | Mini Motorways (STEAM) | 58 | 2026-11-09 | 98 | 70% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 88 | [x] | Darksiders (STEAM) | 58 | 2026-11-09 | 73 | 80% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 89 | [x] | Deskrawl: Idle ARPG (STEAM) | 58 | 2026-11-09 | 72 | 83% | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 90 | [x] | A Plague Tale: Innocence (STEAM) | 57 | 2026-11-09 | 60 | 80% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 91 | [x] | Sonic Generations (STEAM) | 56 | 2026-11-09 | 62 | 68% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 92 | [x] | Until Then (STEAM) | 55 | 2026-10-17 | 90 | 80% |  |
| 93 | [x] | TBH: Task Bar Hero (STEAM) | 55 | 2026-11-09 | 88 | 83% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 94 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 55 | 2026-11-09 | 87 | 90% |  |
| 95 | [x] | Starbound (STEAM) | 55 | 2026-11-09 | 87 | 76% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 96 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 54 | 2026-10-25 | 101 | 65% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 97 | [x] | Call of Duty: World at War (STEAM) | 54 | 2026-11-09 | 78 | 86% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 98 | [x] | Grand Theft Auto V (EPIC) | 54 | 2026-11-09 | 60 | 77% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 99 | [x] | Deadlock (STEAM) | 53 | 2026-10-16 | 74 | 86% |  |
| 100 | [x] | Alex Kidd in Miracle World DX (EPIC) | 53 | 2026-11-09 | 61 | 67% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 101 | [x] | Overwatch® (STEAM) | 53 | 2026-11-10 | 56 | 62% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 102 | [x] | Dead Space (STEAM) | 52 | 2026-10-18 | 65 | 84% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 103 | [x] | Okami HD (STEAM) | 50 | 2026-11-09 | 96 | 91% |  |
| 104 | [x] | Sonic Adventure DX (STEAM) | 50 | 2026-10-17 | 89 | 68% |  |
| 105 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 50 | 2026-11-09 | 85 | 52% |  |
| 106 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 50 | 2026-11-09 | 83 | 46% |  |
| 107 | [x] | Last Epoch (STEAM) | 50 | 2026-11-09 | 75 | 80% |  |
| 108 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 49 | 2026-11-09 | 83 | 82% |  |
| 109 | [x] | MudRunner (STEAM) | 48 | 2026-10-24 | 104 | 62% |  |
| 110 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 48 | 2026-10-19 | 93 | 69% |  |
| 111 | [x] | Darkest Dungeon® (EPIC) | 48 | 2026-11-09 | 89 | 77% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 112 | [x] | Abiotic Factor (STEAM) | 48 | 2026-10-18 | 82 | 69% |  |
| 113 | [x] | Oxygen Not Included (STEAM) | 48 | 2026-11-11 | 82 | 61% |  |
| 114 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 48 | 2026-11-09 | 78 | 82% |  |
| 115 | [x] | Big Walk (STEAM) | 48 | 2026-11-09 | 73 | 70% |  |
| 116 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 2026-11-09 | 74 | 91% |  |
| 117 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 47 | 2026-11-09 | 54 | 91% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 118 | [x] | Rivals of Aether II (STEAM) | 46 | 2026-11-09 | 65 | 64% | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 119 | [x] | Sheepy: A Short Adventure (STEAM) | 46 | 2026-11-09 | 55 | 74% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 120 | [x] | Heroes of Might & Magic III - HD Edition (STEAM) | 45 | 2026-11-14 | 59 | 63% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 121 | [x] | Moonlighter (EPIC) | 45 | 2026-11-09 | 49 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 122 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 44 | 2026-11-13 | 60 | 61% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 123 | [x] | Tomb Raider GOTY (GOG) | 43 | 2026-10-17 | 103 | 92% |  |
| 124 | [x] | Mortal Kombat X (STEAM) | 43 | 2026-10-17 | 75 | 88% |  |
| 125 | [x] | Sonic Lost World (STEAM) | 43 | 2026-11-09 | 62 | 79% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 126 | [x] | Forza Horizon 4 (STEAM) | 43 | 2026-11-09 | 59 | 65% | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 127 | [x] | Aggelos (STEAM) | 42 | 2026-11-09 | 57 | 94% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 128 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 41 | 2026-11-09 | 62 | 74% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 129 | [x] | Rayman Origins (STEAM) | 40 | 2026-10-17 | 90 | 85% |  |
| 130 | [x] | Ace Attorney Investigations Collection (STEAM) | 40 | 2026-11-09 | 70 | 87% |  |
| 131 | [x] | Tomb Raider: Anniversary (STEAM) | 40 | 2026-11-09 | 63 | 62% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 132 | [x] | PROTOTYPE 2 (STEAM) | 39 | 2026-10-18 | 87 | 72% |  |
| 133 | [x] | Digimon World: Next Order (STEAM) | 39 | 2026-11-09 | 76 | 86% |  |
| 134 | [x] | Library Of Ruina (STEAM) | 39 | 2026-10-16 | 76 | 88% |  |
| 135 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 39 | 2026-11-09 | 71 | 86% |  |
| 136 | [x] | FINAL FANTASY VII (2013) (STEAM) | 39 | 2026-11-09 | 56 | 71% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 137 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-11-09 | 40 | 81% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 138 | [x] | Amnesia: The Dark Descent (STEAM) | 38 | 2026-11-09 | 74 | 79% |  |
| 139 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 38 | 2026-11-09 | 71 | 91% |  |
| 140 | [x] | Dead by Daylight (STEAM) | 38 | 2026-11-09 | 42 | 84% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 141 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 38 | 2026-11-09 | 40 | 83% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 142 | [x] | Life is Strange™ (STEAM) | 37 | 2026-10-17 | 79 | 81% |  |
| 143 | [x] | Sonic Origins (STEAM) | 37 | 2026-11-09 | 70 | 84% |  |
| 144 | [x] | The Bazaar (STEAM) | 37 | 2026-11-09 | 65 | 73% |  |
| 145 | [x] | Street Fighter™ 6 (STEAM) | 37 | 2026-11-09 | 61 | 81% |  |
| 146 | [x] | Capcom Arcade Stadium (STEAM) | 37 | 2026-11-09 | 47 | 74% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 147 | [x] | Russian Fishing 4 (STEAM) | 37 | 2026-11-09 | 43 | 84% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 148 | [x] | CrossCode (GOG) | 37 | 2026-11-09 | 40 | 76% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 149 | [x] | Teardown (STEAM) | 36 | 2026-10-17 | 81 | 82% |  |
| 150 | [x] | Age of Empires II (2013) (STEAM) | 36 | 2026-11-09 | 61 | 66% |  |
| 151 | [x] | Rogue Legacy (STEAM) | 35 | 2026-10-17 | 83 | 85% |  |
| 152 | [x] | Little Nightmares (STEAM) | 35 | 2026-10-16 | 79 | 71% |  |
| 153 | [x] | Tales of ARISE (STEAM) | 35 | 2026-10-16 | 76 | 90% |  |
| 154 | [x] | POSTAL 2 (GOG) | 35 | 2026-11-09 | 70 | 92% |  |
| 155 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 35 | 2026-11-09 | 61 | 70% |  |
| 156 | [x] | XCOM 2 (STEAM) | 35 | 2026-11-09 | 59 | 87% |  |
| 157 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 35 | 2026-11-09 | 47 | 89% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 158 | [x] | Elite Dangerous (STEAM) | 35 | 2026-11-09 | 38 | 64% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 159 | [x] | Death Road to Canada (STEAM) | 34 | 2026-10-17 | 95 | 80% |  |
| 160 | [x] | Cobalt Core (STEAM) | 34 | 2026-10-18 | 87 | 89% |  |
| 161 | [x] | SurrounDead (STEAM) | 34 | 2026-11-09 | 66 | 93% |  |
| 162 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 34 | 2026-11-09 | 65 | 86% |  |
| 163 | [x] | Rocket League (STEAM) | 34 | 2026-10-17 | 60 | 71% |  |
| 164 | [x] | Hero Siege (STEAM) | 34 | 2026-11-09 | 57 | 72% |  |
| 165 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 34 | 2026-11-09 | 54 | 90% |  |
| 166 | [x] | Need for Speed™ Rivals (STEAM) | 34 | 2026-11-10 | 45 | 73% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 167 | [x] | Super Animal Royale (STEAM) | 34 | 2026-11-09 | 45 | 61% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 168 | [x] | Romestead (STEAM) | 34 | 2026-11-09 | 44 | 62% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 169 | [x] | Journey (STEAM) | 33 | 2026-10-27 | 73 | 67% |  |
| 170 | [x] | State of Decay: Year-One (STEAM) | 33 | 2026-10-18 | 68 | 77% |  |
| 171 | [x] | Ultimate Chicken Horse (STEAM) | 33 | 2026-10-23 | 68 | 76% |  |
| 172 | [x] | Hearts of Iron IV (STEAM) | 33 | 2026-11-09 | 62 | 74% |  |
| 173 | [x] | Gauntlet™  (STEAM) | 33 | 2026-11-11 | 47 | 43% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 174 | [x] | FINAL FANTASY VIII (STEAM) | 33 | 2026-11-14 | 42 | 62% | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 175 | [x] | Dishonored - Definitive Edition (EPIC) | 32 | 2026-10-17 | 80 | 79% |  |
| 176 | [x] | Salt and Sanctuary (STEAM) | 32 | 2026-10-18 | 73 | 84% |  |
| 177 | [x] | Torchlight II (STEAM) | 32 | 2026-10-20 | 72 | 89% |  |
| 178 | [x] | COCOON (STEAM) | 32 | 2026-11-09 | 66 | 82% |  |
| 179 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 32 | 2026-11-11 | 59 | 33% |  |
| 180 | [x] | Stumble Guys (STEAM) | 32 | 2026-10-18 | 59 | 69% |  |
| 181 | [x] | Being a DIK (STEAM) | 32 | 2026-11-09 | 57 | 60% |  |
| 182 | [x] | Max Payne (STEAM) | 32 | 2026-11-09 | 57 | 88% |  |
| 183 | [x] | Earthion (STEAM) | 32 | 2026-11-09 | 52 | 100% |  |
| 184 | [x] | SnowRunner (STEAM) | 32 | 2026-11-09 | 46 | 78% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 185 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-11-09 | 41 | 83% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 186 | [x] | Owlboy (STEAM) | 31 | 2026-11-02 | 63 | 56% |  |
| 187 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 31 | 2026-11-09 | 55 | 74% |  |
| 188 | [x] | Counter-Strike:Global Offensive (STEAM) | 31 | 2026-11-09 | 51 | 80% |  |
| 189 | [x] | Nioh: Complete Edition (STEAM) | 31 | 2026-11-09 | 42 | 92% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 190 | [x] | Bloodstained: Curse of the Moon (STEAM) | 30 | 2026-10-16 | 75 | 77% |  |
| 191 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 30 | 2026-11-09 | 67 | 76% |  |
| 192 | [x] | Resident Evil Village (STEAM) | 30 | 2026-11-09 | 53 | 89% |  |
| 193 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 30 | 2026-11-09 | 50 | 66% |  |
| 194 | [x] | Secrets of Grindea (STEAM) | 30 | 2026-11-09 | 48 | 74% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 195 | [x] | Sol Cesto (STEAM) | 30 | 2026-11-11 | 48 | 60% |  |
| 196 | [x] | Supermarket Together (STEAM) | 30 | 2026-11-09 | 42 | 66% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 197 | [x] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 30 | 2026-11-14 | 35 | 70% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 198 | [x] | Red Dead Redemption (STEAM) | 30 | 2026-11-09 | 33 | 67% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 199 | [x] | Sable (EPIC) | 29 | 2026-10-18 | 68 | 65% |  |
| 200 | [x] | PlateUp! (STEAM) | 29 | 2026-10-16 | 64 | 86% |  |
| 201 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 29 | 2026-11-09 | 59 | 84% |  |
| 202 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 29 | 2026-11-09 | 56 | 82% |  |
| 203 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 2026-10-17 | 55 | 83% |  |
| 204 | [x] | Deponia (STEAM) | 29 | 2026-11-09 | 53 | 67% |  |
| 205 | [x] | Prince of Persia: The Sands of Time (STEAM) | 29 | 2026-11-09 | 49 | 83% |  |
| 206 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 29 | 2026-11-09 | 47 | 85% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 207 | [x] | Yakuza: Like a Dragon (STEAM) | 29 | 2026-11-09 | 46 | 65% |  |
| 208 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 67% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 209 | [x] | Aethermancer (STEAM) | 28 | 2026-10-18 | 50 | 84% |  |
| 210 | [x] | Gambonanza (STEAM) | 28 | 2026-11-09 | 47 | 92% |  |
| 211 | [x] | Guildrun Demo (STEAM) | 28 | 2026-11-09 | 45 | 69% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 212 | [x] | Tower and Sword of Succubus (STEAM) | 28 | 2026-11-09 | 43 | 86% |  |
| 213 | [x] | G.I. Joe Wrath of Cobra (EPIC) | 27 | 2026-11-09 | 48 | 64% |  |
| 214 | [x] | Heavy Rain (STEAM) | 27 | 2026-11-09 | 48 | 88% |  |
| 215 | [x] | Capcom Fighting Collection 2 (STEAM) | 27 | 2026-11-09 | 44 | 76% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 216 | [x] | Dead Rising 2 (STEAM) | 27 | 2026-11-09 | 43 | 63% |  |
| 217 | [x] | Digimon Survive (STEAM) | 27 | 2026-11-09 | 40 | 93% |  |
| 218 | [x] | Palia (STEAM) | 27 | 2026-11-09 | 39 | 75% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 219 | [x] | Gothic II: Gold Classic (STEAM) | 27 | 2026-11-09 | 37 | 73% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 220 | [x] | Ultimate Custom Night (STEAM) | 27 | 2026-11-09 | 37 | 64% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 221 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 26 | 2026-10-19 | 94 | 92% |  |
| 222 | [x] | Grand Theft Auto III (STEAM) | 26 | 2026-10-17 | 72 | 78% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 223 | [x] | Skullgirls 2nd Encore (STEAM) | 26 | 2026-11-10 | 62 | 63% |  |
| 224 | [x] | BioShock™ (GOG) | 26 | 2026-10-18 | 61 | 82% |  |
| 225 | [x] | Monster Hunter Stories (STEAM) | 26 | 2026-10-17 | 61 | 78% |  |
| 226 | [x] | Frostpunk (STEAM) | 26 | 2026-11-09 | 51 | 72% |  |
| 227 | [x] | Resident Evil Revelations 2 (STEAM) | 26 | 2026-11-09 | 49 | 83% |  |
| 228 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 45 | 63% |  |
| 229 | [x] | Limbus Company (STEAM) | 26 | 2026-11-09 | 40 | 86% |  |
| 230 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 26 | 2026-11-09 | 37 | 67% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 231 | [x] | CRUEL (STEAM) | 26 | 2026-11-09 | 35 | 69% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 232 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 26 | 2026-11-09 | 30 | 100% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 233 | [x] | Dying Light (EPIC) | 25 | 2026-10-17 | 60 | 77% |  |
| 234 | [x] | Battle Brothers (STEAM) | 25 | 2026-11-09 | 44 | 79% |  |
| 235 | [x] | Counter-Strike: Condition Zero (STEAM) | 25 | 2026-11-11 | 42 | 38% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 236 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 25 | 2026-11-09 | 33 | 92% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 237 | [x] | Bongo Cat (STEAM) | 25 | 2026-11-09 | 32 | 74% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 238 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-09 | 32 | 90% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 239 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 25 | 2026-11-09 | 31 | 69% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 240 | [x] | Tales of Zestiria (STEAM) | 25 | 2026-11-09 | 31 | 67% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 241 | [x] | Crab Game (STEAM) | 25 | 2026-11-09 | 30 | 95% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 242 | [x] | Northgard: Definitive Edition (STEAM) | 25 | 2026-11-09 | 28 | 91% | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 243 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 57 | 92% |  |
| 244 | [x] | Mirror's Edge™ (GOG) | 24 | 2026-11-13 | 45 | 53% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 245 | [x] | Prince of Persia (GOG) | 24 | 2026-11-09 | 42 | 85% |  |
| 246 | [x] | Unturned (STEAM) | 24 | 2026-11-09 | 42 | 71% |  |
| 247 | [x] | Opus Magnum (STEAM) | 24 | 2026-11-09 | 39 | 92% |  |
| 248 | [x] | Ratatan (STEAM) | 24 | 2026-11-09 | 37 | 97% |  |
| 249 | [x] | Jade Empire: Special Edition (GOG) | 24 | 2026-11-09 | 31 | 77% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 250 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 23 | 2026-10-20 | 52 | 89% |  |
| 251 | [x] | Chained Echoes (GOG) | 23 | 2026-11-08 | 49 | 63% |  |
| 252 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 46 | 88% |  |
| 253 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-11-09 | 45 | 89% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 254 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 23 | 2026-11-09 | 45 | 96% |  |
| 255 | [x] | Lucid Blocks (STEAM) | 23 | 2026-11-09 | 43 | 63% |  |
| 256 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 23 | 2026-11-09 | 42 | 75% |  |
| 257 | [x] | Football Manager 2024 (EPIC) | 23 | 2026-11-09 | 40 | 67% |  |
| 258 | [x] | Worms W.M.D (STEAM) | 23 | 2026-11-09 | 40 | 93% |  |
| 259 | [x] | Cat Mail Co. (STEAM) | 23 | 2026-11-09 | 39 | 85% |  |
| 260 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 2026-11-09 | 36 | 76% |  |
| 261 | [x] | Return to Monkey Island (STEAM) | 23 | 2026-11-09 | 36 | 76% |  |
| 262 | [x] | Moonlight Peaks (STEAM) | 23 | 2026-11-09 | 34 | 81% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 263 | [x] | Borderlands: The Pre-Sequel (EPIC) | 23 | 2026-11-09 | 33 | 69% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 264 | [x] | Cities: Skylines (STEAM) | 23 | 2026-11-13 | 33 | 60% | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 265 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 95% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 266 | [x] | Jade Empire: Special Edition (STEAM) | 23 | 2026-11-09 | 26 | 75% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 267 | [x] | CarX Drift Racing Online (STEAM) | 22 | 2026-10-16 | 57 | 81% |  |
| 268 | [x] | WEBFISHING (STEAM) | 22 | 2026-10-17 | 53 | 88% |  |
| 269 | [x] | Goat Simulator (STEAM) | 22 | 2026-11-09 | 46 | 74% |  |
| 270 | [x] | Crazy Taxi (STEAM) | 22 | 2026-11-10 | 42 | 71% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 271 | [x] | Wizard of Legend (EPIC) | 22 | 2026-11-09 | 41 | 83% |  |
| 272 | [x] | Soul's Remnant (STEAM) | 22 | 2026-11-11 | 40 | n/a |  |
| 273 | [x] | Trailmakers (STEAM) | 22 | 2026-11-09 | 39 | 92% |  |
| 274 | [x] | My Summer Car (STEAM) | 22 | 2026-11-09 | 38 | 79% |  |
| 275 | [x] | Tabletop Simulator (STEAM) | 22 | 2026-11-09 | 37 | 66% |  |
| 276 | [x] | Deus Ex™ GOTY Edition (GOG) | 22 | 2026-11-09 | 35 | 87% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 277 | [x] | Timberborn (STEAM) | 22 | 2026-11-09 | 33 | 85% |  |
| 278 | [x] | SOMA (STEAM) | 22 | 2026-11-09 | 32 | 60% | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 279 | [x] | Dishonored 2 (STEAM) | 22 | 2026-11-09 | 31 | 82% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 280 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 60 | 98% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 281 | [x] | No Rest for the Wicked (STEAM) | 21 | 2026-10-19 | 47 | 80% |  |
| 282 | [x] | Slow Roads (STEAM) | 21 | 2026-10-22 | 46 | 82% |  |
| 283 | [x] | MudRunner (EPIC) | 21 | 2026-10-18 | 43 | 73% |  |
| 284 | [x] | Control Ultimate Edition (GOG) | 21 | 2026-11-09 | 39 | 86% |  |
| 285 | [x] | Invisible, Inc. (STEAM) | 21 | 2026-11-09 | 37 | 73% |  |
| 286 | [x] | Beyond: Two Souls (STEAM) | 21 | 2026-11-09 | 30 | 65% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 287 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 90% |  |
| 288 | [x] | CarX Street (STEAM) | 21 | 2026-11-09 | 27 | 87% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 289 | [x] | Tearscape (STEAM) | 21 | 2026-11-09 | 25 | 94% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 290 | [x] | Titan Quest Anniversary Edition (STEAM) | 20 | 2026-10-16 | 61 | 92% |  |
| 291 | [x] | BlazBlue Centralfiction (STEAM) | 20 | 2026-10-17 | 54 | 82% |  |
| 292 | [x] | Saints Row IV (STEAM) | 20 | 2026-10-19 | 51 | 85% |  |
| 293 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-11-09 | 38 | 100% |  |
| 294 | [x] | Pinball FX Classic (STEAM) | 20 | 2026-11-09 | 37 | 94% |  |
| 295 | [x] | SWORN (STEAM) | 20 | 2026-11-09 | 35 | 95% |  |
| 296 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 20 | 2026-11-09 | 30 | 86% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 297 | [x] | Party Animals (STEAM) | 20 | 2026-11-09 | 29 | 70% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 298 | [x] | Torchlight II (EPIC) | 20 | 2026-11-09 | 28 | 82% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 299 | [x] | Tyr (STEAM) | 20 | 2026-11-09 | 28 | 73% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 300 | [x] | Sapphire Safari (GOG) | 20 | 2026-11-09 | 27 | 80% | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 301 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 20 | 2026-11-09 | 26 | 73% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 302 | [x] | Dead Island (STEAM) | 20 | 2026-11-09 | 25 | 93% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 303 | [x] | Cyberpunk 2077 (EPIC) | 20 | 2026-11-12 | 24 | 61% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 304 | [x] | Sorry We're Closed (EPIC) | 19 | 2026-11-09 | 34 | 72% |  |
| 305 | [x] | One-armed robber (STEAM) | 19 | 2026-11-09 | 34 | 74% |  |
| 306 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 19 | 2026-11-09 | 33 | 76% |  |
| 307 | [x] | Far Far West (STEAM) | 19 | 2026-11-09 | 33 | 64% |  |
| 308 | [x] | Stick It to the Stickman (STEAM) | 19 | 2026-11-09 | 33 | 76% |  |
| 309 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 32 | 62% |  |
| 310 | [x] | GOD EATER RESURRECTION (STEAM) | 19 | 2026-11-09 | 31 | 72% |  |
| 311 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 19 | 2026-11-09 | 29 | 87% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 312 | [x] | Backpack Battles (STEAM) | 18 | 2026-11-09 | 42 | 100% |  |
| 313 | [x] | Brothers - A Tale of Two Sons (EPIC) | 18 | 2026-11-14 | 34 | 60% |  |
| 314 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 18 | 2026-11-09 | 31 | 83% |  |
| 315 | [x] | Mortal Shell (EPIC) | 18 | 2026-11-09 | 29 | 64% |  |
| 316 | [x] | Arcade Paradise (EPIC) | 18 | 2026-11-09 | 28 | 69% |  |
| 317 | [x] | Sonic and SEGA All Stars Racing (STEAM) | 18 | 2026-11-09 | 27 | 67% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 318 | [x] | Capcom Fighting Collection (STEAM) | 18 | 2026-11-09 | 26 | 78% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 319 | [x] | Need for Speed™ Unbound (STEAM) | 18 | 2026-11-09 | 26 | 56% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 320 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-09 | 23 | 70% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 321 | [x] | Undisputed (STEAM) | 18 | 2026-11-14 | 20 | 67% | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 322 | [x] | ABZÛ (STEAM) | 17 | 2026-10-21 | 45 | 97% |  |
| 323 | [x] | Cave Story+ (EPIC) | 17 | 2026-10-18 | 41 | 89% |  |
| 324 | [x] | Kingdom Come: Deliverance II (STEAM) | 17 | 2026-10-20 | 41 | 87% |  |
| 325 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 37 | 18% |  |
| 326 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 36 | 88% |  |
| 327 | [x] | Faster Than Light (EPIC) | 17 | 2026-11-09 | 32 | 92% |  |
| 328 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 17 | 2026-11-09 | 30 | 83% |  |
| 329 | [x] | Shank 2 (STEAM) | 17 | 2026-11-09 | 29 | 90% |  |
| 330 | [x] | DNF Duel (EPIC) | 17 | 2026-11-09 | 28 | 64% |  |
| 331 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 17 | 2026-11-09 | 22 | 92% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 332 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 333 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 334 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 16 | 2026-10-19 | 56 | 82% |  |
| 335 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 51 | 94% |  |
| 336 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 16 | 2026-10-20 | 37 | 80% |  |
| 337 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 16 | 2026-11-11 | 35 | 52% |  |
| 338 | [x] | GRIP: Combat Racing (STEAM) | 16 | 2026-11-09 | 34 | 76% |  |
| 339 | [x] | sobosuba (STEAM) | 16 | 2026-11-09 | 33 | 86% |  |
| 340 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 341 | [x] | Tiny Glade (STEAM) | 16 | 2026-11-09 | 31 | 69% |  |
| 342 | [x] | Mortal Kombat 11 (STEAM) | 16 | 2026-11-09 | 30 | 71% |  |
| 343 | [x] | GRANDIA HD Remaster (STEAM) | 16 | 2026-11-09 | 29 | 83% |  |
| 344 | [x] | Another World: 20th Anniversary Edition (GOG) | 16 | 2026-11-14 | 27 | 62% |  |
| 345 | [x] | LET IT DIE (STEAM) | 16 | 2026-11-14 | 26 | 60% |  |
| 346 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 60% |  |
| 347 | [x] | Assassin's Creed Odyssey (STEAM) | 16 | 2026-11-09 | 25 | 67% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 348 | [x] | Legend of Grimrock 2 (STEAM) | 16 | 2026-11-09 | 24 | 86% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 349 | [x] | Allumeria (STEAM) | 16 | 2026-11-09 | 23 | 75% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 350 | [x] | Darksiders Warmastered Edition (EPIC) | 16 | 2026-11-09 | 21 | 63% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 351 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 352 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 353 | [x] | Blood: Fresh Supply (STEAM) | 15 | 2026-10-16 | 40 | 81% |  |
| 354 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 15 | 2026-10-25 | 40 | 77% |  |
| 355 | [x] | Grim Fandango Remastered (STEAM) | 15 | 2026-10-19 | 39 | 72% |  |
| 356 | [x] | Mark of the Ninja (STEAM) | 15 | 2026-10-26 | 31 | 78% |  |
| 357 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 31 | 96% |  |
| 358 | [x] | Sonic Superstars (STEAM) | 15 | 2026-10-21 | 30 | 65% |  |
| 359 | [x] | Human Fall Flat (STEAM) | 15 | 2026-10-29 | 29 | 60% |  |
| 360 | [x] | Hitman: Absolution (GOG) | 15 | 2026-11-09 | 28 | 73% |  |
| 361 | [x] | Need for Speed: Undercover (STEAM) | 15 | 2026-11-11 | 28 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 362 | [x] | Titanfall® 2 (STEAM) | 15 | 2026-11-09 | 28 | 69% |  |
| 363 | [x] | Batman™: Arkham Origins (GOG) | 15 | 2026-11-09 | 27 | 100% |  |
| 364 | [x] | Gloomwood (STEAM) | 15 | 2026-11-09 | 26 | 64% |  |
| 365 | [x] | Nex Machina (STEAM) | 15 | 2026-11-09 | 24 | 79% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 366 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 85% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 367 | [x] | Sacred Gold (STEAM) | 15 | 2026-11-09 | 22 | 70% | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 368 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 369 | [x] | Spark the Electric Jester (STEAM) | 15 | 2026-11-13 | 21 | 64% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 370 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 15 | 2026-11-09 | 21 | 67% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 371 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 372 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 14 | 2026-10-21 | 43 | 80% |  |
| 373 | [x] | Overlord (STEAM) | 14 | 2026-11-08 | 33 | 59% |  |
| 374 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 93% |  |
| 375 | [x] | Killing Floor (STEAM) | 14 | 2026-10-19 | 29 | 86% |  |
| 376 | [x] | Evoland (STEAM) | 14 | 2026-11-11 | 28 | n/a |  |
| 377 | [x] | Antichamber (STEAM) | 14 | 2026-11-11 | 27 | 73% |  |
| 378 | [x] | Ultrapool (STEAM) | 14 | 2026-11-09 | 27 | 100% |  |
| 379 | [x] | AER Memories of Old (EPIC) | 14 | 2026-11-09 | 25 | 93% |  |
| 380 | [x] | WORLD OF FINAL FANTASY (STEAM) | 14 | 2026-11-09 | 25 | 71% |  |
| 381 | [x] | Wildermyth (STEAM) | 14 | 2026-11-09 | 25 | 73% |  |
| 382 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 23 | 77% |  |
| 383 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 384 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-11-09 | 21 | 91% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 385 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 386 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 387 | [x] | Spin Rhythm XD (STEAM) | 13 | 2026-10-18 | 34 | 85% |  |
| 388 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 13 | 2026-10-19 | 31 | 95% |  |
| 389 | [x] | Divinity: Original Sin (Classic) (STEAM) | 13 | 2026-10-16 | 30 | n/a |  |
| 390 | [x] | No Man's Sky (GOG) | 13 | 2026-10-19 | 29 | 95% |  |
| 391 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 29 | 46% |  |
| 392 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 29 | 75% |  |
| 393 | [x] | Dead Space™ 3 (STEAM) | 13 | 2026-10-20 | 28 | 81% |  |
| 394 | [x] | Guacamelee! Gold Edition (STEAM) | 13 | 2026-11-11 | 27 | 83% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 395 | [x] | Intravenous 2 (STEAM) | 13 | 2026-11-09 | 27 | 97% |  |
| 396 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 27 | 73% |  |
| 397 | [x] | Blaster Master Zero (STEAM) | 13 | 2026-11-11 | 26 | 60% |  |
| 398 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 13 | 2026-11-09 | 26 | 67% |  |
| 399 | [x] | MX Bikes (STEAM) | 13 | 2026-11-09 | 25 | 93% |  |
| 400 | [x] | Ghostwire Tokyo (EPIC) | 13 | 2026-11-09 | 23 | 79% |  |
| 401 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 13 | 2026-11-09 | 23 | 75% |  |
| 402 | [x] | Haydee (STEAM) | 13 | 2026-11-09 | 23 | 82% |  |
| 403 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 13 | 2026-11-13 | 23 | 73% |  |
| 404 | [x] | The Stanley Parable (STEAM) | 13 | 2026-11-13 | 23 | 69% |  |
| 405 | [x] | 12 is Better Than 6 (STEAM) | 13 | 2026-11-09 | 22 | 91% |  |
| 406 | [x] | PAYDAY: The Heist (STEAM) | 13 | 2026-11-13 | 22 | 70% |  |
| 407 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 22 | 79% |  |
| 408 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 409 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 70% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 410 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 89% |  |
| 411 | [x] | Alabaster Dawn Demo (STEAM) | 13 | 2026-11-09 | 20 | 72% |  |
| 412 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 413 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 2026-11-09 | 20 | 85% |  |
| 414 | [x] | Super Monkey Ball Banana Mania (STEAM) | 13 | 2026-11-13 | 20 | 70% |  |
| 415 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 80% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 416 | [x] | Tom Clancy's Splinter Cell: Chaos Theory (STEAM) | 12 | 2026-10-16 | 31 | 88% |  |
| 417 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 12 | 2026-10-18 | 28 | 94% |  |
| 418 | [x] | Alan Wake's American Nightmare (EPIC) | 12 | 2026-11-09 | 25 | 68% |  |
| 419 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 25 | 71% |  |
| 420 | [x] | Lust Goddess (STEAM) | 12 | 2026-11-09 | 25 | 88% |  |
| 421 | [x] | Injustice™ 2 (STEAM) | 12 | 2026-10-17 | 24 | 58% |  |
| 422 | [x] | Lost Castle 2 (STEAM) | 12 | 2026-11-09 | 24 | 94% |  |
| 423 | [x] | Ready or Not (STEAM) | 12 | 2026-11-09 | 24 | 80% |  |
| 424 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-11-09 | 23 | 95% |  |
| 425 | [x] | HITMAN World of Assassination (STEAM) | 12 | 2026-11-09 | 23 | 87% |  |
| 426 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 23 | 69% |  |
| 427 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-10 | 22 | 67% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 428 | [x] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 2026-11-12 | 22 | 90% |  |
| 429 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 12 | 2026-11-09 | 21 | 70% |  |
| 430 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 431 | [x] | Horny Villa (STEAM) | 12 | 2026-11-09 | 21 | 85% |  |
| 432 | [x] | Shift At Midnight (STEAM) | 12 | 2026-11-09 | 21 | 84% |  |
| 433 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 434 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 435 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 2026-11-10 | 20 | 60% |  |
| 436 | [x] | Turbo Overkill (STEAM) | 12 | 2026-11-09 | 20 | 95% |  |
| 437 | [x] | Middle-earth™: Shadow of War™ (STEAM) | 11 | 2026-10-16 | 34 | 82% |  |
| 438 | [x] | Haiku, the Robot (STEAM) | 11 | 2026-10-21 | 27 | n/a |  |
| 439 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 2026-10-27 | 26 | 81% |  |
| 440 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 2026-11-09 | 25 | 89% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 441 | [x] | Breath of Fire IV (GOG) | 11 | 2026-10-26 | 25 | 65% |  |
| 442 | [x] | Rayman Origins (GOG) | 11 | 2026-11-09 | 24 | 76% |  |
| 443 | [x] | Aperture Desk Job (STEAM) | 11 | 2026-11-03 | 24 | n/a |  |
| 444 | [x] | Castle in the Clouds (STEAM) | 11 | 2026-11-09 | 24 | 78% |  |
| 445 | [x] | Cruelty Squad (STEAM) | 11 | 2026-11-09 | 24 | 86% |  |
| 446 | [x] | Life is Strange Remastered (STEAM) | 11 | 2026-11-09 | 23 | 86% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 447 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 23 | 78% |  |
| 448 | [x] | DiRT 4 (STEAM) | 11 | 2026-11-09 | 22 | 92% |  |
| 449 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 21 | 73% |  |
| 450 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 451 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 452 | [x] | The WereCleaner (STEAM) | 10 | 2026-10-22 | 31 | 90% |  |
| 453 | [x] | Distance (STEAM) | 10 | 2026-10-19 | 28 | 76% |  |
| 454 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 26 | n/a |  |
| 455 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 10 | 2026-11-01 | 25 | n/a |  |
| 456 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 10 | 2026-10-23 | 24 | 88% |  |
| 457 | [x] | Coromon (GOG) | 10 | 2026-10-19 | 22 | 67% |  |
| 458 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 22 | 83% |  |
| 459 | [x] | UNDEFEATED (STEAM) | 10 | 2026-11-09 | 21 | 73% |  |
| 460 | [x] | Sid Meier's Civilization VI (EPIC) | 10 | 2026-10-19 | 20 | 76% |  |
| 461 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 462 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 463 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 464 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 20 | 75% |  |
| 465 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 466 | [x] | TowerFall Ascension (STEAM) | 9 | 2026-10-16 | 31 | 71% |  |
| 467 | [x] | Possessor(s) (STEAM) | 9 | 2026-10-24 | 27 | 88% |  |
| 468 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 9 | 2026-10-21 | 21 | 92% |  |
| 469 | [x] | Football Manager 2024 (STEAM) | 9 | 2026-10-16 | 20 | n/a |  |
| 470 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 9 | 2026-11-09 | 20 | 83% |  |
| 471 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 31% |  |
| 472 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 8 | 2026-10-20 | 25 | 83% |  |
| 473 | [x] | CULTIC (STEAM) | 8 | 2026-11-09 | 24 | 57% |  |
| 474 | [x] | SCP – Containment Breach (STEAM) | 8 | 2026-10-27 | 22 | 92% |  |
| 475 | [x] | Gloomhaven (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 476 | [x] | SteamWorld Heist (GOG) | 8 | 2026-10-25 | 20 | n/a |  |
| 477 | [x] | Mina the Hollower (GOG) | 7 | 2026-10-28 | 20 | 74% |  |
| 478 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 20 | 54% |  |
| 479 | [x] | Mafia II: Definitive Edition (STEAM) | 7 | 2026-10-16 | 20 | 85% |  |
| 480 | [x] | What Remains of Edith Finch (STEAM) | 6 | 2026-10-19 | 27 | 74% |  |
| 481 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 5 | 2026-10-20 | 20 | 73% |  |
| 482 | [x] | Alex Kidd in Miracle World DX (STEAM) | 2 | 2026-10-16 | 35 | 92% |  |
