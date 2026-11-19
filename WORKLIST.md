# GameNative compatibility worklist

Generated: `2026-11-19T04:15:13.349Z` · Ratings since: `2026-08-21T04:15:13.349Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 126 |
| Probably does not work | 184 |
| Fix shipped, waiting for ratings | 16 |
| First launch fails | 300 |
| Mixed | 485 |
| Works | 1026 |
| Total | 2137 |

## Does not work (126)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 161 | 181 | 89% (14d) | Does not open (83%) | 50% | today | 24% (drop) | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 142 | 163 | 87% (since fix) | Does not open (91%) | 44% | today | 36% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 3 | [ ] | Rocket League® (EPIC) | 78 | 92 | 85% (14d) | Does not open (79%) | 43% | today | 27% | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 4 | [ ] | DREDGE (EPIC) | 38 | 42 | 90% (14d) | Does not open (76%) | 58% | 1d ago | 46% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 5 | [ ] | Hogwarts Legacy (STEAM) | 34 | 34 | 100% (14d) | Does not open (70%) | 33% | today | 16% | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 6 | [ ] | Melvor Idle 2: A RuneScape Adventure (STEAM) | 31 | 32 | 97% (14d) | Does not open (100%) | 24% | today | 22% | [#543](https://github.com/GameNative/gamenative-compat/issues/543) |
| 7 | [x] 2026-10-18 | Project Zomboid (STEAM) | 58 | 64 | 91% (since fix) | Does not open (65%) | 43% | today | 38% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 8 | [ ] | Metro: Last Light Redux (STEAM) | 24 | 24 | 100% (14d) | Does not open (91%) | 23% | today | 28% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 9 | [ ] | Bloons TD 6 (EPIC) | 23 | 24 | 96% (14d) | Does not open (77%) | 39% | today | 22% | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 10 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 21 | 22 | 95% (14d) | Does not open (96%) | 40% | 4d ago | 20% (drop) | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 11 | [ ] | Borderlands 2 (EPIC) | 20 | 22 | 91% (14d) | Does not open (80%) | 54% | today | 47% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 12 | [ ] | Saints Row 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | 32% | 3d ago | 31% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 13 | [ ] | Path of Exile (STEAM) | 19 | 21 | 90% (14d) | Does not open (91%) | 25% | today | 18% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 14 | [ ] | Sifu (EPIC) | 17 | 21 | 81% (14d) | Does not open (71%) | 48% | 1d ago | 37% | [#535](https://github.com/GameNative/gamenative-compat/issues/535) |
| 15 | [ ] | Saints Row 2 (GOG) | 17 | 22 | 77% (14d) | Does not open (90%) | 40% | 1d ago | 38% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 16 | [ ] | Owlboy (STEAM) | 14 | 20 | 70% (14d) | Does not open (81%) | 49% | 1d ago | 46% |  |
| 17 | [ ] | Mafia II (Classic) (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 8% | 1d ago | 12% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 18 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 14 | 20 | 70% (last 20) | Does not open (77%) | 55% | today | 45% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 19 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (76%) | 0% | 10d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 20 | [ ] | Call of Duty: Black Ops II (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 37% | today | 38% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 21 | [ ] | Fallout: New Vegas PCR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | 59% | 1d ago | 57% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 22 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (92%) | 25% | 5d ago | 18% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 23 | [ ] | skate. (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | 12% | today | 15% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 24 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (78%) | 0% | 4d ago | 0% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 25 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 38% | 1d ago | 30% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 26 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 16 | 20 | 80% (last 20) | No graphics (46%) | 30% | today | 40% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 27 | [ ] | Forza Horizon 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (47%) | 53% | 1d ago | 23% (drop) | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 28 | [ ] | Hogwarts Legacy (EPIC) | 14 | 20 | 70% (last 20) | Does not open (75%) | 51% | today | 42% | [#537](https://github.com/GameNative/gamenative-compat/issues/537) |
| 29 | [ ] | Vampire Survivors (EPIC) | 17 | 20 | 85% (last 20) | Does not open (59%) | 44% | today | 28% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 30 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 16 | 20 | 80% (last 20) | Does not open (84%) | 52% | today | 69% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 31 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (71%) | 20% | today | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 32 | [ ] | Detroit: Become Human (STEAM) | 18 | 20 | 90% (last 20) | Does not open (76%) | 57% | 1d ago | 64% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 33 | [ ] | Kenshi (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 3% | today | 0% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 34 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | 9% | 5d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 35 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 12% | 7d ago | 7% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 36 | [ ] | The Witcher: Enhanced Edition (GOG) | 19 | 20 | 95% (last 20) | Does not open (74%) | 7% | 10d ago | 13% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 37 | [ ] | Breath of Fire IV (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | 15% | today | 12% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 38 | [ ] | Fall Guys (EPIC) | 19 | 20 | 95% (last 20) | Does not open (74%) | 12% | 4d ago | 7% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 39 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (70%) | 16% | today | 23% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 40 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | 0% | 4d ago | n/a | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 41 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 57% | today | 39% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 42 | [ ] | Trackmania (STEAM) | 16 | 20 | 80% (last 20) | Does not open (82%) | 21% | 3d ago | 31% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 43 | [ ] | CPM 2 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 8% | 3d ago | 5% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 44 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (93%) | 10% | 1d ago | n/a | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 45 | [ ] | Call of Duty® (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | 0% | 2d ago | 0% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 46 | [ ] | Deliver At All Costs (EPIC) | 14 | 20 | 70% (last 20) | Does not open (60%) | 47% | 3d ago | 42% | [#538](https://github.com/GameNative/gamenative-compat/issues/538) |
| 47 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | 13% | 18d ago | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 48 | [ ] | MECCHA CHAMELEON (STEAM) | 15 | 20 | 75% (last 20) | Does not open (67%) | 44% | 1d ago | 32% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 49 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (60%) | 45% | 3d ago | n/a | [#536](https://github.com/GameNative/gamenative-compat/issues/536) |
| 50 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (88%) | 25% | 10d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 51 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (80%) | 12% | 10d ago | 18% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 52 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | 20% | 5d ago | 30% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 53 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 59% | 3d ago | 54% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 54 | [ ] | Borderlands GOTY (STEAM) | 16 | 20 | 80% (last 20) | Does not open (94%) | 38% | today | 47% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 55 | [ ] | Blood Omen: Legacy of Kain (GOG) | 16 | 20 | 80% (last 20) | No graphics (57%) | 58% | today | n/a | [#539](https://github.com/GameNative/gamenative-compat/issues/539) |
| 56 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (83%) | 43% | 1d ago | 47% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 57 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 57% | 17d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 58 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (88%) | 50% | 6d ago | 53% | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 59 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (68%) | 24% | 7d ago | 27% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 60 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (77%) | 11% | 4d ago | 8% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 61 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | 0% | 5d ago | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 62 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (54%) | 25% | 1d ago | 18% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 63 | [ ] | Half-Life: Blue Shift (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 33% | 2d ago | 45% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 64 | [ ] | Rivals of Aether II (STEAM) | 16 | 20 | 80% (last 20) | Does not open (56%) | 44% | 2d ago | 6% (drop) | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 65 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (73%) | 50% | 7d ago | n/a | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 66 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 30% | today | 41% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 67 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | 50% | 40d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 68 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (82%) | 0% | 4d ago | n/a | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 69 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | 10% | 6d ago | 10% | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 70 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 38% | 5d ago | 50% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 71 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (45%) | 43% | 14d ago | 41% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 72 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 32% | 10d ago | 41% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 73 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | 31% | 2d ago | 30% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 74 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 38% | 7d ago | 17% (drop) | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 75 | [ ] | Black Mesa (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | 22% | 1d ago | 33% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 76 | [ ] | Watch_Dogs (STEAM) | 14 | 20 | 70% (last 20) | Does not open (90%) | 33% | 12d ago | 38% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 77 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 19 | 20 | 95% (last 20) | Does not open (85%) | 42% | 2d ago | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 78 | [ ] | XCOM: Enemy Unknown (STEAM) | 18 | 20 | 90% (last 20) | Does not open (71%) | 18% | 5d ago | n/a | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 79 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (73%) | 30% | 12d ago | 23% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 80 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (93%) | 9% | 17d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 81 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 17% | 28d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 82 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | Does not open (63%) | 25% | 12d ago | 33% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 83 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 20% | 17d ago | n/a | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 84 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (63%) | 55% | 8d ago | 40% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 85 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 3% | 7d ago | 1% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 86 | [ ] | Umamusume: Pretty Derby (STEAM) | 19 | 20 | 95% (last 20) | Does not open (82%) | 50% | today | 53% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 87 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 13% | 19d ago | n/a | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 88 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 53% | 7d ago | 67% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 89 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (53%) | 52% | today | 54% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 90 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (76%) | 0% | 32d ago | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 91 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (62%) | 0% | today | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 92 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | 23% | 2d ago | 25% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 93 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (90%) | 21% | 11d ago | n/a | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 94 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 3% | 14d ago | 4% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 95 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (61%) | 46% | 7d ago | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 96 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 17% | today | 20% | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 97 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 19 | 20 | 95% (last 20) | No graphics (57%) | 37% | 5d ago | 47% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 98 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 0% | 25d ago | 0% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 99 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (67%) | 40% | 1d ago | n/a | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 100 | [ ] | OneShot (STEAM) | 16 | 20 | 80% (last 20) | Does not open (96%) | 15% | 34d ago | n/a | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 101 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 20 | 80% (last 20) | Does not open (47%) | 54% | 5d ago | 29% (drop) | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 102 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | 33% | 9d ago | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 103 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | 25% | 17d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 104 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (83%) | 52% | 4d ago | 46% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 105 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (97%) | 30% | 17d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 106 | [ ] | Lost Planet: Extreme Condition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (80%) | 38% | 4d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 107 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (62%) | 53% | 7d ago | 22% (drop) | [#540](https://github.com/GameNative/gamenative-compat/issues/540) |
| 108 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (90%) | 27% | 3d ago | 31% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 109 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 22% | 33d ago | 30% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 110 | [ ] | Aliens vs. Predator (STEAM) | 16 | 20 | 80% (last 20) | No graphics (58%) | 23% | 7d ago | 25% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 111 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 30% | 19d ago | n/a | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 112 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (67%) | 54% | 8d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 113 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | 46% | 19d ago | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 114 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 40% | 2d ago | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 115 | [ ] | Maneater (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 54% | 5d ago | 50% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 116 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | 50% | 5d ago | 36% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 117 | [ ] | Zuma Deluxe (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | 25% | 6d ago | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 118 | [ ] | Beyond Good & Evil™ (GOG) | 17 | 20 | 85% (last 20) | Does not open (100%) | 20% | today | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 119 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (73%) | 54% | 10d ago | n/a | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 120 | [ ] | Bongo Cat (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 59% | 1d ago | 38% (drop) | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 121 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 20 | 80% (last 20) | Does not open (82%) | 56% | 3d ago | 40% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 122 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (54%) | 50% | 4d ago | n/a | [#541](https://github.com/GameNative/gamenative-compat/issues/541) |
| 123 | [ ] | Maneater (EPIC) | 16 | 20 | 80% (last 20) | Does not open (73%) | 40% | 3d ago | 20% (drop) | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 124 | [ ] | Hitman 2: Silent Assassin (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 33% | 2d ago | 36% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 125 | [ ] | Ghostwire Tokyo (EPIC) | 14 | 20 | 70% (last 20) | Does not open (91%) | 58% | 4d ago | 43% | [#544](https://github.com/GameNative/gamenative-compat/issues/544) |
| 126 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 45% | 11d ago | 50% | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |

## Probably does not work (184)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Counter-Strike 2 (STEAM) | 46 | 69 | 67% (since fix) | Does not open (68%) | 56% | today | 59% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 2 | [ ] | theHunter Classic (STEAM) | 20 | 20 | 100% (last 20) | No graphics (92%) | n/a | 15d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 3 | [ ] | Euro Truck Simulator 2 (STEAM) | 15 | 26 | 58% (14d) | Does not open (65%) | 57% | today | 57% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 4 | [ ] | Bully: Scholarship Edition (STEAM) | 14 | 21 | 67% (14d) | Does not open (63%) | 46% | today | 11% (drop) |  |
| 5 | [ ] | To The Moon (GOG) | 18 | 20 | 90% (last 20) | Does not open (86%) | n/a | 16d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 6 | [ ] | Flotsam (EPIC) | 13 | 26 | 50% (14d) | Does not open (80%) | 42% | today | 33% |  |
| 7 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 25 | 45 | 56% (since fix) | Does not open (74%) | 58% | 1d ago | 53% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 8 | [ ] | FINAL FANTASY XIII (STEAM) | 12 | 22 | 55% (14d) | Does not open (73%) | 55% | today | 57% |  |
| 9 | [ ] | Metro 2033 Redux (STEAM) | 12 | 22 | 55% (14d) | Does not open (70%) | 43% | today | 40% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 10 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 13 | 20 | 65% (last 20) | Does not open (61%) | 46% | 4d ago | 37% |  |
| 11 | [ ] | VRChat (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 39% | 1d ago | 34% |  |
| 12 | [ ] | Driver: Parallel Lines (STEAM) | 19 | 20 | 95% (last 20) | Does not open (65%) | n/a | 10d ago | n/a | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 13 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 59% | 3d ago | 47% |  |
| 14 | [ ] | Garry's Mod (STEAM) | 9 | 17 | 53% (since fix) | Does not open (80%) | 54% | 2d ago | 44% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 15 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 9 | 13 | 69% (since fix) | Does not open (91%) | 42% | today | 48% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 16 | [ ] | Asterigos: Curse of the Stars (STEAM) | 17 | 20 | 85% (last 20) | Graphics glitches (73%) | n/a | 2d ago | n/a |  |
| 17 | [ ] | Door Kickers 2 (STEAM) | 20 | 20 | 100% (last 20) | No graphics (86%) | n/a | 36d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 18 | [ ] | Gorilla Tag (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 14% | 4d ago | 10% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 19 | [ ] | DOOM 64 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (60%) | 54% | today | 35% |  |
| 20 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 39d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 21 | [ ] | Teenage Mutant Ninja Turtles: Shredder's Revenge (EPIC) | 13 | 20 | 65% (last 20) | Does not open (82%) | 52% | 3d ago | 44% |  |
| 22 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (36%) | n/a | 16d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 23 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 12 | 20 | 60% (last 20) | Does not open (72%) | 30% | 1d ago | 38% |  |
| 24 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 20 | 20 | 100% (last 20) | Controller issues (100%) | n/a | today | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 25 | [ ] | Sonic Adventure™ 2  (STEAM) | 12 | 20 | 60% (last 20) | Does not open (77%) | 46% | today | 39% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 26 | [ ] | Yume Nikki (STEAM) | 10 | 20 | 50% (last 20) | Does not open (87%) | 35% | 1d ago | 53% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 27 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 23d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 28 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | No graphics (38%) | 52% | 4d ago | 34% |  |
| 29 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 11 | 19 | 58% (since fix) | Does not open (77%) | 32% | 3d ago | 36% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 30 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 58% | 3d ago | 42% |  |
| 31 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | No graphics (55%) | n/a | 22d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 32 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 12d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 33 | [ ] | Metro 2033 Redux (EPIC) | 11 | 20 | 55% (last 20) | Does not open (58%) | 27% | today | 38% |  |
| 34 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 12 | 20 | 60% (last 20) | Does not open (86%) | 59% | 1d ago | 30% (drop) | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 35 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | 5% | 2d ago | n/a |  |
| 36 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 20d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 37 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (93%) | n/a | 2d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 38 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | n/a | 11d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 39 | [ ] | CODE VEIN (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | 38% | 3d ago | 21% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 40 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (85%) | 50% | 9d ago | n/a |  |
| 41 | [ ] | Hi-Fi RUSH (STEAM) | 10 | 20 | 50% (last 20) | Does not open (76%) | 45% | today | 44% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 42 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 19% | 4d ago | 7% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 43 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | n/a | 4d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 44 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 14d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 45 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (66%) | n/a | 17d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 46 | [ ] | GRID (STEAM) | 10 | 20 | 50% (last 20) | Does not open (58%) | 40% | 4d ago | 50% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 47 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 8d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 48 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (70%) | n/a | 4d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 49 | [ ] | Grim Dawn (GOG) | 13 | 20 | 65% (last 20) | Does not open (69%) | 40% | 3d ago | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 50 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | 1d ago | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 51 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 37d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 52 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (59%) | n/a | today | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 53 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | n/a | 16d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 54 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | n/a | 38d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 55 | [ ] | Hollow Knight: Silksong (GOG) | 12 | 20 | 60% (last 20) | Does not open (70%) | 51% | 2d ago | 48% |  |
| 56 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 36d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 57 | [ ] | Alpha Protocol (STEAM) | 17 | 20 | 85% (last 20) | No graphics (53%) | n/a | 24d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 58 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (56%) | n/a | 4d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 59 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | n/a | 8d ago | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 60 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 52% | 2d ago | 30% (drop) | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 61 | [ ] | Dead Space 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 28% | 9d ago | 33% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 62 | [ ] | METAL SLUG 3 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (78%) | 54% | 6d ago | 67% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 63 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | n/a | 5d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 64 | [ ] | DOOM Eternal (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | 27d ago | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 65 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | n/a | 20d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 66 | [ ] | HELLDIVERS™ (STEAM) | 12 | 20 | 60% (last 20) | Does not open (58%) | 44% | today | 56% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 67 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | 39d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 68 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 36d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 69 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (57%) | n/a | 5d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 70 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 36d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 71 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 22d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 72 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | n/a | 15d ago | n/a |  |
| 73 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 30% | 9d ago | 27% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 74 | [ ] | Breathedge (STEAM) | 11 | 20 | 55% (last 20) | Does not open (55%) | 56% | 8d ago | 69% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 75 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (92%) | 38% | 3d ago | n/a |  |
| 76 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 5d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 77 | [ ] | Borderlands 2 RU (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | n/a | 2d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 78 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | 1d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 79 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 10d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 80 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 22d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 81 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (54%) | n/a | 24d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 82 | [ ] | Euro Truck Simulator (STEAM) | 20 | 20 | 100% (last 20) | Does not open (88%) | n/a | 3d ago | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 83 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 47d ago | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 84 | [ ] | Peggle Nights (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 22d ago | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 85 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 18d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 86 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (50%) | n/a | 18d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 87 | [ ] | Beholder (EPIC) | 18 | 20 | 90% (last 20) | Does not open (61%) | n/a | 1d ago | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 88 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | n/a | 41d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 89 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | 1d ago | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 90 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | n/a | 45d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 91 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (82%) | n/a | 3d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 92 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | n/a | 7d ago | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 93 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 61d ago | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 94 | [ ] | The Survivalists (STEAM) | 18 | 20 | 90% (last 20) | Does not open (96%) | n/a | 6d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 95 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | n/a | 2d ago | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 96 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | n/a | 36d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 97 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 14d ago | n/a |  |
| 98 | [ ] | A Plague Tale: Innocence (EPIC) | 11 | 20 | 55% (last 20) | Does not open (70%) | 38% | 5d ago | 20% |  |
| 99 | [ ] | Rise of the Tomb Raider: 20 Year Celebration (EPIC) | 11 | 20 | 55% (last 20) | Does not open (69%) | 49% | today | 37% |  |
| 100 | [ ] | Metro 2033 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 18% | 15d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 101 | [ ] | They Are Billions (STEAM) | 19 | 20 | 95% (last 20) | Does not open (74%) | n/a | 15d ago | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 102 | [ ] | Bionic Commando Rearmed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | n/a | 29d ago | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 103 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | n/a | 3d ago | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 104 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 23d ago | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 105 | [ ] | Undisputed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | n/a | 11d ago | n/a | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 106 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | n/a | 12d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 107 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 12d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 108 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 8d ago | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 109 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 9d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 110 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 7d ago | n/a |  |
| 111 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (47%) | n/a | 3d ago | n/a |  |
| 112 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 11 | 20 | 55% (last 20) | Does not open (90%) | 54% | today | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 113 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 10d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 114 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | n/a | 7d ago | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 115 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 20d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 116 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (40%) | n/a | 17d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 117 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 21d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 118 | [ ] | Drop Duchy (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 8% | today | n/a |  |
| 119 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 14d ago | n/a |  |
| 120 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 14d ago | n/a |  |
| 121 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (94%) | 50% | today | n/a | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 122 | [ ] | Crysis® (GOG) | 17 | 20 | 85% (last 20) | Does not open (87%) | n/a | 2d ago | n/a |  |
| 123 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 17d ago | n/a |  |
| 124 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 7d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 125 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | No graphics (45%) | n/a | 9d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 126 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | n/a | 1d ago | n/a | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 127 | [ ] | Romancing SaGa -Minstrel Song- Remastered (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (100%) | n/a | 3d ago | n/a |  |
| 128 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 55% | 7d ago | n/a |  |
| 129 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 13 | 20 | 65% (last 20) | Does not open (55%) | 47% | 3d ago | n/a | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 130 | [ ] | Mortal Shell (EPIC) | 13 | 20 | 65% (last 20) | Does not open (50%) | 46% | today | 22% (drop) |  |
| 131 | [ ] | ENDLESS Space™ 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 34d ago | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 132 | [ ] | King's Bounty: The Legend (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 1d ago | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 133 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | n/a | 3d ago | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 134 | [ ] | Fallout Classic (GOG) | 15 | 20 | 75% (last 20) | Does not open (88%) | n/a | 6d ago | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 135 | [ ] | Re-Volt (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (71%) | n/a | 25d ago | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 136 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (69%) | n/a | 14d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 137 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | n/a | 31d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 138 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 54% | 19d ago | 33% (drop) |  |
| 139 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | 6d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 140 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | n/a | 9d ago | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 141 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (83%) | 21% | today | 24% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 142 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (50%) | 59% | 5d ago | 40% |  |
| 143 | [ ] | Mafia: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (87%) | 41% | today | 39% |  |
| 144 | [ ] | Sacred Gold (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | n/a | today | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 145 | [ ] | Chasm (GOG) | 12 | 20 | 60% (last 20) | No graphics (50%) | n/a | 4d ago | n/a |  |
| 146 | [ ] | DAEMON X MACHINA (EPIC) | 10 | 20 | 50% (last 20) | Does not open (92%) | 50% | today | 25% (drop) |  |
| 147 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (50%) | n/a | 10d ago | n/a |  |
| 148 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 10 | 20 | 50% (last 20) | No graphics (57%) | 37% | 3d ago | 54% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 149 | [ ] | Chef Knight (STEAM) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 23d ago | n/a |  |
| 150 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (89%) | n/a | 11d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 151 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 36% | 8d ago | n/a |  |
| 152 | [ ] | Songs of Conquest (EPIC) | 13 | 20 | 65% (last 20) | Does not open (75%) | n/a | 3d ago | n/a |  |
| 153 | [ ] | FINAL FANTASY VII REMAKE INTERGRADE (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 43% | 4d ago | 43% |  |
| 154 | [ ] | Sandustry (STEAM) | 12 | 20 | 60% (last 20) | Does not open (74%) | n/a | 4d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 155 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (78%) | 57% | 10d ago | 58% |  |
| 156 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | n/a | today | n/a |  |
| 157 | [ ] | Crying Suns (EPIC) | 12 | 20 | 60% (last 20) | No graphics (63%) | n/a | 1d ago | n/a |  |
| 158 | [ ] | Assassin's Creed Odyssey (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 57% | 2d ago | 50% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 159 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 13 | 20 | 65% (last 20) | No graphics (56%) | n/a | 37d ago | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 160 | [ ] | Beat Cop (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | n/a | 6d ago | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 161 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | n/a | 41d ago | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 162 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | n/a | 9d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 163 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 13d ago | n/a |  |
| 164 | [ ] | Allumeria (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | n/a | today | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 165 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 55% | 3d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 166 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 14d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 167 | [ ] | Styx: Master of Shadows (EPIC) | 11 | 20 | 55% (last 20) | Does not open (73%) | 48% | 1d ago | 47% |  |
| 168 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (67%) | 58% | 7d ago | n/a |  |
| 169 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | n/a | 7d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 170 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 53% | today | 64% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 171 | [ ] | No More Heroes (STEAM) | 10 | 20 | 50% (last 20) | No graphics (63%) | 40% | today | 33% |  |
| 172 | [ ] | HOT WHEELS UNLEASHED™ (EPIC) | 10 | 20 | 50% (last 20) | No graphics (63%) | 50% | 2d ago | 37% |  |
| 173 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (58%) | 53% | today | n/a |  |
| 174 | [ ] | Minit (EPIC) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 11d ago | n/a |  |
| 175 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 20d ago | n/a |  |
| 176 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (78%) | n/a | 13d ago | n/a |  |
| 177 | [ ] | LET IT DIE (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | n/a | 1d ago | n/a |  |
| 178 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 38% | 14d ago | n/a |  |
| 179 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (52%) | n/a | 21d ago | n/a | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 180 | [ ] | Railway Chai Wala (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | n/a | 4d ago | n/a |  |
| 181 | [ ] | Turnip Boy Robs a Bank (EPIC) | 11 | 20 | 55% (last 20) | Does not open (67%) | 31% | 5d ago | n/a | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 182 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | n/a | 13d ago | n/a |  |
| 183 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 10 | 20 | 50% (last 20) | Does not open (79%) | n/a | 84d ago | n/a |  |
| 184 | [ ] | Delver (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 28% | 3d ago | 0% (drop) |  |

## Fix shipped, waiting for ratings (16)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | L.A. Noire (STEAM) | 2026-11-04 | 4 | 4 | 4d ago | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 2 | Transistor (STEAM) | 2026-11-10 | 3 | 3 | today | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 3 | Max Payne 3 (STEAM) | 2026-11-04 | 3 | 3 | 2d ago | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 4 | Red Dead Redemption (STEAM) | 2026-11-04 | 2 | 2 | 2d ago | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 5 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 7 | 7 | 2d ago | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 6 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 3 | 3 | 8d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 7 | Peggle Deluxe (STEAM) | 2026-10-29 | 1 | 1 | 6d ago | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 8 | Necesse (STEAM) | 2026-10-29 | 6 | 0 | 3d ago | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 9 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 1 | 1 | 8d ago | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 10 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 1 | 1 | 15d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 11 | Need for Speed™ (STEAM) | 2026-11-04 | 0 | 0 | 28d ago | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 12 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 0 | 0 | 16d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 13 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 0 | 0 | 21d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 14 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 0 | 0 | 15d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 15 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 14d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 16 | Need for Speed™ Unbound (STEAM) | 2026-11-04 | 0 | 0 | 22d ago | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |

## Works, but the first launch usually fails (300)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Half-Life (STEAM) | 82 | 115 | 71% (14d) | Does not open (60%) | 71% | today | 67% |  |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 72 | 95 | 76% (14d) | Does not open (63%) | 93% | today | 95% |  |
| 3 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 56 | 76 | 74% (14d) | Does not open (54%) | 82% | today | 83% |  |
| 4 | [ ] | Grand Theft Auto V Legacy (STEAM) | 57 | 67 | 85% (since fix) | Does not open (88%) | 74% | today | 69% |  |
| 5 | [ ] | Buckshot Roulette (STEAM) | 46 | 62 | 74% (14d) | Does not open (63%) | 67% | today | 45% (drop) |  |
| 6 | [ ] | Cyberpunk 2077 (STEAM) | 45 | 77 | 58% (14d) | Does not open (71%) | 71% | today | 67% |  |
| 7 | [ ] | Road Rash™: 30th Anniversary Edition (STEAM) | 45 | 71 | 63% (14d) | Does not open (74%) | 63% | today | 67% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 8 | [ ] | MONSTER HUNTER RISE (STEAM) | 37 | 59 | 63% (14d) | Does not open (83%) | 62% | today | 63% |  |
| 9 | [ ] | Probably Stolen (STEAM) | 36 | 70 | 51% (14d) | Does not open (64%) | 85% | 2d ago | 80% |  |
| 10 | [ ] | Valheim (STEAM) | 38 | 61 | 62% (since fix) | No graphics (54%) | 84% | today | 82% |  |
| 11 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 32 | 44 | 73% (14d) | Does not open (59%) | 69% | today | 60% |  |
| 12 | [ ] | No Man's Sky (STEAM) | 34 | 61 | 56% (since fix) | Controller issues (61%) | 79% | today | 76% |  |
| 13 | [ ] | ROB RUN (STEAM) | 31 | 41 | 76% (14d) | Does not open (88%) | 65% | today | 67% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 14 | [ ] | Super Meat Boy (STEAM) | 29 | 55 | 53% (14d) | Does not open (57%) | 67% | today | 58% |  |
| 15 | [ ] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 28 | 52 | 54% (14d) | Does not open (65%) | 66% | 1d ago | 69% |  |
| 16 | [ ] | Horizon Chase Turbo (EPIC) | 28 | 37 | 76% (14d) | Does not open (85%) | 62% | today | 47% |  |
| 17 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 27 | 38 | 71% (14d) | Does not open (77%) | 77% | 1d ago | 73% |  |
| 18 | [ ] | Selaco (STEAM) | 27 | 43 | 63% (14d) | Does not open (86%) | 71% | today | 64% |  |
| 19 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 24 | 28 | 86% (14d) | Does not open (77%) | 61% | today | 61% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 20 | [ ] | Red Dead Redemption 2 (STEAM) | 21 | 22 | 95% (since fix) | Does not open (98%) | 82% | today | 84% |  |
| 21 | [ ] | ELDEN RING (STEAM) | 18 | 33 | 55% (14d) | Does not open (85%) | 68% | 1d ago | 64% |  |
| 22 | [ ] | Quake (STEAM) | 18 | 30 | 60% (14d) | Does not open (62%) | 72% | 1d ago | 59% |  |
| 23 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (43%) | 92% | today | 90% |  |
| 24 | [ ] | Resident Evil 4 (2005) (STEAM) | 17 | 25 | 68% (14d) | Does not open (78%) | 71% | 1d ago | 71% |  |
| 25 | [ ] | Library Of Ruina (STEAM) | 17 | 26 | 65% (14d) | Does not open (68%) | 86% | today | 81% |  |
| 26 | [ ] | BeamNG.drive (STEAM) | 16 | 21 | 76% (14d) | Does not open (79%) | 73% | today | 57% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 27 | [ ] | BioShock Remastered (EPIC) | 16 | 22 | 73% (14d) | Does not open (67%) | 61% | today | 55% |  |
| 28 | [ ] | Loftia (STEAM) | 16 | 20 | 80% (last 20) | Does not open (94%) | 72% | today | 65% |  |
| 29 | [ ] | Order of the Sinking Star (STEAM) | 15 | 23 | 65% (14d) | Does not open (65%) | 67% | today | 72% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 30 | [ ] | Deadlock (STEAM) | 15 | 20 | 75% (last 20) | Does not open (54%) | 86% | 4d ago | 83% |  |
| 31 | [ ] | Look Outside (STEAM) | 14 | 28 | 50% (14d) | Controller issues (61%) | 91% | 2d ago | 90% |  |
| 32 | [ ] | Shakedown: Hawaii (STEAM) | 14 | 27 | 52% (14d) | Does not open (77%) | 90% | 2d ago | 81% |  |
| 33 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 14 | 20 | 70% (14d) | Controller issues (57%) | 75% | today | 65% |  |
| 34 | [ ] | DRAGON BALL FighterZ (STEAM) | 27 | 50 | 54% (since fix) | Does not open (89%) | 85% | 2d ago | 90% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 35 | [ ] | Mortal Kombat X (STEAM) | 13 | 20 | 65% (14d) | Does not open (72%) | 91% | 1d ago | 91% |  |
| 36 | [ ] | DOOM 3: BFG Edition (STEAM) | 15 | 20 | 75% (last 20) | Does not open (72%) | 69% | 1d ago | 64% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 37 | [ ] | Resident Evil 7 Biohazard (STEAM) | 12 | 20 | 60% (14d) | Does not open (71%) | 72% | today | 66% |  |
| 38 | [ ] | Grand Theft Auto V (EPIC) | 18 | 20 | 90% (last 20) | Does not open (89%) | 79% | 1d ago | 77% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 39 | [ ] | Geometry Wars: Retro Evolved (STEAM) | 12 | 20 | 60% (last 20) | Does not open (94%) | 63% | today | 55% |  |
| 40 | [ ] | Batman™: Arkham Origins (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | 73% | 1d ago | 61% |  |
| 41 | [ ] | Alabaster Dawn (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (48%) | 87% | today | 88% |  |
| 42 | [ ] | Crypt of the NecroDancer (STEAM) | 11 | 22 | 50% (14d) | Does not open (46%) | 91% | 1d ago | 88% |  |
| 43 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (89%) | 95% | 1d ago | 95% |  |
| 44 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (71%) | 100% | 4d ago | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 45 | [ ] | Dead Space (STEAM) | 18 | 20 | 90% (last 20) | Does not open (57%) | 85% | today | 80% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 46 | [ ] | Mini Motorways (STEAM) | 15 | 20 | 75% (last 20) | Does not open (71%) | 67% | 1d ago | 62% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 47 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 66% | today | 62% |  |
| 48 | [ ] | Absolute Drift (EPIC) | 11 | 20 | 55% (last 20) | No graphics (53%) | 64% | today | 33% (drop) |  |
| 49 | [ ] | Cry of Fear (STEAM) | 13 | 20 | 65% (last 20) | Does not open (48%) | 72% | 1d ago | 73% |  |
| 50 | [ ] | Divinity: Original Sin 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (74%) | 83% | today | 76% |  |
| 51 | [ ] | Palworld (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | 87% | 2d ago | 86% |  |
| 52 | [ ] | Dead Island Definitive Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (61%) | 86% | today | 85% |  |
| 53 | [ ] | River City Girls (EPIC) | 13 | 20 | 65% (last 20) | No graphics (48%) | 65% | today | 46% |  |
| 54 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 10 | 20 | 50% (last 20) | Does not open (70%) | 69% | today | 93% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 55 | [ ] | Dead Island 2 (EPIC) | 17 | 20 | 85% (last 20) | Does not open (84%) | 67% | 4d ago | 53% |  |
| 56 | [ ] | Castlevania Dominus Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (92%) | 98% | 3d ago | 98% |  |
| 57 | [ ] | Don't Starve Together (STEAM) | 11 | 20 | 55% (last 20) | Does not open (61%) | 72% | 1d ago | 64% |  |
| 58 | [ ] | Disgaea 5 Complete (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | 90% | 2d ago | 94% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 59 | [ ] | METAL GEAR SOLID 4: Guns of the Patriots - Master Collection Version (STEAM) | 11 | 20 | 55% (last 20) | Does not open (80%) | 89% | 7d ago | 92% |  |
| 60 | [ ] | LEGO® MARVEL Super Heroes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (66%) | 83% | 1d ago | 86% |  |
| 61 | [ ] | Cyberpunk 2077 (GOG) | 12 | 20 | 60% (last 20) | Does not open (72%) | 71% | 1d ago | 61% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 62 | [ ] | Fallout: New Vegas (EPIC) | 15 | 20 | 75% (last 20) | Does not open (60%) | 81% | 1d ago | 75% |  |
| 63 | [ ] | Aniimo (STEAM) | 17 | 20 | 85% (last 20) | Does not open (74%) | 84% | 1d ago | 78% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 64 | [ ] | OMORI (STEAM) | 14 | 20 | 70% (last 20) | Does not open (62%) | 66% | today | 52% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 65 | [ ] | Darksiders Warmastered Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 63% | today | 45% |  |
| 66 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 69% | 2d ago | 71% |  |
| 67 | [ ] | Welcome to Elderfield (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 70% | today | 72% |  |
| 68 | [ ] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 74% | 2d ago | 84% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 69 | [ ] | Prey (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 79% | today | 83% |  |
| 70 | [ ] | eFootball™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | 66% | 1d ago | 57% |  |
| 71 | [ ] | Disco Elysium - The Final Cut (EPIC) | 11 | 20 | 55% (last 20) | Does not open (75%) | 97% | today | 98% |  |
| 72 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 7 | 13 | 54% (since fix) | Controller issues (84%) | 75% | today | 68% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 73 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Does not open (61%) | 88% | today | 84% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 74 | [ ] | Poppy Playtime (STEAM) | 13 | 20 | 65% (last 20) | Does not open (59%) | 67% | 4d ago | 58% |  |
| 75 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (48%) | 83% | today | 82% |  |
| 76 | [ ] | Fable - The Lost Chapters (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (47%) | 81% | today | 83% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 77 | [ ] | Chained Echoes (GOG) | 14 | 20 | 70% (last 20) | Does not open (60%) | 60% | today | 54% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 78 | [ ] | Castlevania Anniversary Collection (EPIC) | 12 | 20 | 60% (last 20) | Does not open (75%) | 62% | today | 33% (drop) |  |
| 79 | [ ] | Deskrawl: Idle ARPG (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 67% | 8d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 80 | [ ] | Dota 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (76%) | 77% | 2d ago | 87% |  |
| 81 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 97% | today | 96% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 82 | [ ] | Call of Duty 4: Modern Warfare (2007) (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (54%) | 76% | today | 63% |  |
| 83 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 15 | 20 | 75% (last 20) | Does not open (42%) | 74% | 2d ago | 67% |  |
| 84 | [ ] | Fate/stay night REMASTERED (STEAM) | 12 | 20 | 60% (last 20) | No graphics (48%) | 91% | 4d ago | 86% |  |
| 85 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (84%) | 71% | 1d ago | 44% (drop) |  |
| 86 | [ ] | The Sims™ 4 (STEAM) | 6 | 12 | 50% (since fix) | Does not open (85%) | 72% | 1d ago | 73% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 87 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 67% | 2d ago | 71% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 88 | [ ] | Happy Wheels (STEAM) | 19 | 20 | 95% (last 20) | No graphics (52%) | 70% | 12d ago | 54% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 89 | [ ] | Ratatan (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 90% | 6d ago | 86% |  |
| 90 | [ ] | Need for Speed™ Rivals (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 80% | 2d ago | 92% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 91 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (62%) | 97% | 1d ago | 98% |  |
| 92 | [ ] | STAR WARS™ Knights of the Old Republic™ II: The Sith Lords™ (STEAM) | 11 | 20 | 55% (last 20) | No graphics (65%) | 63% | 1d ago | 40% (drop) |  |
| 93 | [ ] | Cave Story+ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | 82% | 1d ago | 74% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 94 | [ ] | MIO: Memories in Orbit (STEAM) | 11 | 20 | 55% (last 20) | Graphics glitches (62%) | 95% | 3d ago | 97% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 95 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (51%) | 63% | 5d ago | 36% (drop) | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 96 | [ ] | Rune Factory 3 Special (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 93% | today | n/a |  |
| 97 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (80%) | 81% | 1d ago | 73% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 98 | [ ] | Palia (STEAM) | 16 | 20 | 80% (last 20) | Does not open (59%) | 74% | today | 65% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 99 | [ ] | Until Then (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 75% | today | 59% |  |
| 100 | [ ] | Sid Meier's Civilization VI (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | 79% | today | 70% |  |
| 101 | [ ] | American Truck Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 77% | 5d ago | 72% |  |
| 102 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (52%) | 71% | 1d ago | 77% |  |
| 103 | [ ] | ZERO Sievert (STEAM) | 11 | 20 | 55% (last 20) | Does not open (87%) | 86% | 1d ago | 79% |  |
| 104 | [ ] | Resident Evil Village (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 89% | 7d ago | 85% |  |
| 105 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 92% | today | 84% |  |
| 106 | [ ] | The Binding of Isaac (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (93%) | 92% | 1d ago | 93% |  |
| 107 | [ ] | Minecraft Dungeons II (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | 70% | today | 75% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 108 | [ ] | Minecraft Dungeons (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 79% | 1d ago | 78% |  |
| 109 | [ ] | Abiotic Factor (STEAM) | 10 | 20 | 50% (last 20) | Does not open (74%) | 73% | 2d ago | 79% |  |
| 110 | [ ] | PAYDAY: The Heist (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | 67% | today | n/a |  |
| 111 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 78% | today | 80% |  |
| 112 | [ ] | Sid Meier's Civilization V (STEAM) | 15 | 20 | 75% (last 20) | Does not open (77%) | 64% | 3d ago | 59% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 113 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 79% | 12d ago | 73% |  |
| 114 | [ ] | Grand Theft Auto: Vice City (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | 85% | 1d ago | 84% |  |
| 115 | [ ] | PlateUp! (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 82% | 2d ago | 69% |  |
| 116 | [ ] | A Plague Tale: Innocence (STEAM) | 19 | 20 | 95% (last 20) | Does not open (88%) | 68% | 3d ago | 69% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 117 | [ ] | Moonstone Island (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (63%) | 74% | 3d ago | 72% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 118 | [ ] | TBH: Task Bar Hero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (68%) | 84% | 7d ago | 83% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 119 | [ ] | No, I'm not a Human (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 94% | 1d ago | 87% |  |
| 120 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | 69% | 10d ago | 82% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 121 | [ ] | Overwatch® (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | 69% | 2d ago | 80% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 122 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 18 | 20 | 90% (last 20) | Does not open (58%) | 91% | 5d ago | n/a | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 123 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (76%) | 95% | 4d ago | n/a | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 124 | [ ] | Tails of Iron (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 87% | 4d ago | 83% |  |
| 125 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | 62% | today | 50% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 126 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 95% | 20d ago | 92% |  |
| 127 | [ ] | Yakuza: Like a Dragon (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 67% | today | 81% |  |
| 128 | [ ] | Astral Party  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 83% | 4d ago | 77% |  |
| 129 | [ ] | Pinball FX (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 71% | 2d ago | 69% |  |
| 130 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 88% | 1d ago | n/a | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 131 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 76% | 8d ago | 79% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 132 | [ ] | Max Payne (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (45%) | 82% | 1d ago | 78% |  |
| 133 | [ ] | Tabletop Simulator (STEAM) | 14 | 20 | 70% (last 20) | Does not open (53%) | 79% | today | 86% |  |
| 134 | [ ] | Call of Duty: World at War (STEAM) | 13 | 20 | 65% (last 20) | Does not open (44%) | 83% | 1d ago | 65% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 135 | [ ] | Street Fighter™ 6 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (81%) | 82% | today | 81% |  |
| 136 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (50%) | 78% | 4d ago | 72% |  |
| 137 | [ ] | Heavy Rain (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 94% | 4d ago | 94% |  |
| 138 | [ ] | Driving Rogue (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 89% | 12d ago | 85% |  |
| 139 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (83%) | 88% | 1d ago | n/a | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 140 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (87%) | 93% | 2d ago | 95% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 141 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (46%) | 91% | 9d ago | 88% |  |
| 142 | [ ] | Sonic Generations (STEAM) | 14 | 20 | 70% (last 20) | Does not open (70%) | 69% | 1d ago | 70% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 143 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 90% | 6d ago | 89% |  |
| 144 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | 79% | 6d ago | n/a | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 145 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (79%) | 78% | 17d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 146 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (78%) | 83% | 2d ago | 84% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 147 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 80% | 12d ago | 81% |  |
| 148 | [ ] | Plague Inc: Evolved (STEAM) | 13 | 20 | 65% (last 20) | Does not open (68%) | 62% | 1d ago | 61% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 149 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 82% | 6d ago | 79% |  |
| 150 | [ ] | Oxygen Not Included (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 61% | 4d ago | 72% |  |
| 151 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 83% | 7d ago | 80% |  |
| 152 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (62%) | 100% | 14d ago | n/a | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 153 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 73% | 5d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 154 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | 90% | today | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 155 | [ ] | Gambonanza (STEAM) | 13 | 20 | 65% (last 20) | Does not open (60%) | 92% | 2d ago | 89% |  |
| 156 | [ ] | Dishonored 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (90%) | 71% | today | 60% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 157 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 11 | 20 | 55% (last 20) | Does not open (62%) | 74% | 1d ago | 73% |  |
| 158 | [ ] | Fallout (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 70% | today | 67% |  |
| 159 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 61% | 10d ago | n/a | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 160 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (59%) | 63% | 7d ago | 61% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 161 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 14 | 20 | 70% (last 20) | Does not open (46%) | 62% | 4d ago | 70% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 162 | [ ] | Gothic 1 Classic (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 77% | 10d ago | 64% |  |
| 163 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (82%) | 89% | today | 87% |  |
| 164 | [ ] | Limbus Company (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 85% | today | 90% |  |
| 165 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (54%) | 72% | 3d ago | 78% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 166 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 84% | 10d ago | 91% |  |
| 167 | [ ] | Control Ultimate Edition (GOG) | 13 | 20 | 65% (last 20) | Does not open (76%) | 78% | 8d ago | 72% |  |
| 168 | [ ] | Trailmakers (STEAM) | 11 | 20 | 55% (last 20) | Does not open (44%) | 94% | 3d ago | 95% |  |
| 169 | [ ] | Sonic Lost World (STEAM) | 10 | 20 | 50% (last 20) | No graphics (69%) | 82% | 2d ago | 81% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 170 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (55%) | 91% | 14d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 171 | [ ] | Changed (STEAM) | 15 | 20 | 75% (last 20) | Does not open (64%) | 64% | 6d ago | 50% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 172 | [ ] | Stellar Blade™ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (43%) | 80% | 2d ago | 82% |  |
| 173 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | 67% | 11d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 174 | [ ] | Digimon Survive (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (77%) | 85% | today | 80% |  |
| 175 | [ ] | Escape from Duckov (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (72%) | 95% | today | 98% |  |
| 176 | [ ] | BioShock 2 Remastered (STEAM) | 11 | 20 | 55% (last 20) | Does not open (79%) | 84% | 3d ago | 84% |  |
| 177 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (70%) | 66% | 11d ago | 80% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 178 | [ ] | Stumble Guys (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 67% | 4d ago | 59% |  |
| 179 | [ ] | Counter-Strike:Global Offensive (STEAM) | 10 | 20 | 50% (last 20) | Does not open (76%) | 68% | 3d ago | 63% |  |
| 180 | [ ] | Raft (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | 90% | 3d ago | 85% |  |
| 181 | [ ] | Capcom Arcade Stadium (STEAM) | 15 | 20 | 75% (last 20) | Does not open (82%) | 74% | 6d ago | 82% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 182 | [ ] | Supermarket Together (STEAM) | 15 | 20 | 75% (last 20) | Does not open (65%) | 61% | 1d ago | 68% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 183 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 100% | 29d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 184 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 88% | 7d ago | 88% |  |
| 185 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 92% | 9d ago | n/a |  |
| 186 | [ ] | One-armed robber (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (65%) | 71% | 11d ago | 60% |  |
| 187 | [ ] | Mortal Kombat 11 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 69% | 5d ago | 72% |  |
| 188 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 65% | today | 71% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 189 | [ ] | Subnautica 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (52%) | 79% | 1d ago | n/a | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 190 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 82% | 8d ago | n/a | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 191 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (71%) | 91% | 1d ago | n/a | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 192 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (75%) | 83% | 2d ago | 67% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 193 | [ ] | Goat Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 64% | today | 62% |  |
| 194 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 81% | 13d ago | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 195 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (65%) | 89% | 14d ago | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 196 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (67%) | 64% | today | n/a | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 197 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 68% | today | 81% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 198 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (61%) | 70% | 9d ago | 62% |  |
| 199 | [ ] | Unturned (STEAM) | 11 | 20 | 55% (last 20) | Does not open (40%) | 71% | 1d ago | 74% |  |
| 200 | [ ] | The Witcher: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 71% | 12d ago | 80% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 201 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 95% | 8d ago | 93% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 202 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (51%) | 62% | 22d ago | 45% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 203 | [ ] | Hotline Miami (GOG) | 14 | 20 | 70% (last 20) | Does not open (89%) | 71% | 1d ago | 77% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 204 | [ ] | Lucid Blocks (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | 66% | 1d ago | 56% |  |
| 205 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 96% | 4d ago | 100% |  |
| 206 | [ ] | TurretGirls (STEAM) | 11 | 20 | 55% (last 20) | No graphics (75%) | 87% | 4d ago | 88% |  |
| 207 | [ ] | Moonring (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 87% | 6d ago | 82% |  |
| 208 | [ ] | MX Bikes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 92% | 1d ago | 94% |  |
| 209 | [ ] | Jade Empire: Special Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 75% | 3d ago | n/a | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 210 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 64% | 7d ago | 55% |  |
| 211 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | 73% | 16d ago | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 212 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (91%) | 82% | 32d ago | 73% |  |
| 213 | [ ] | Invisible, Inc. (STEAM) | 15 | 20 | 75% (last 20) | Does not open (63%) | 77% | 20d ago | n/a |  |
| 214 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 71% | 22d ago | 67% |  |
| 215 | [ ] | Return to Monkey Island (STEAM) | 14 | 20 | 70% (last 20) | No graphics (72%) | 68% | 12d ago | 67% |  |
| 216 | [ ] | GOD EATER RESURRECTION (STEAM) | 14 | 20 | 70% (last 20) | Does not open (59%) | 75% | 5d ago | n/a |  |
| 217 | [ ] | Big Walk (STEAM) | 13 | 20 | 65% (last 20) | Does not open (62%) | 62% | today | 47% |  |
| 218 | [ ] | Darksiders (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 88% | 3d ago | 87% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 219 | [ ] | My Summer Car (STEAM) | 11 | 20 | 55% (last 20) | Does not open (63%) | 79% | 1d ago | 80% |  |
| 220 | [ ] | Warframe (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 82% | 2d ago | 77% |  |
| 221 | [ ] | Resident Evil Revelations 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (45%) | 83% | 1d ago | 81% |  |
| 222 | [ ] | GUILTY GEAR Xrd REV 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (86%) | 76% | 4d ago | 60% |  |
| 223 | [ ] | CS2D (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 82% | today | n/a |  |
| 224 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 77% | 7d ago | 76% |  |
| 225 | [ ] | Ultimate Custom Night (STEAM) | 14 | 20 | 70% (last 20) | No graphics (75%) | 62% | 21d ago | n/a | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 226 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (42%) | 70% | 14d ago | n/a | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 227 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 93% | 9d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 228 | [ ] | Zero Escape: The Nonary Games (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 71% | today | 68% |  |
| 229 | [ ] | STORY OF SEASONS: Friends of Mineral Town (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 93% | 3d ago | 100% |  |
| 230 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Controller issues (36%) | 93% | today | n/a |  |
| 231 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (83%) | 77% | 2d ago | 76% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 232 | [ ] | Cat Mail Co. (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 85% | today | 83% |  |
| 233 | [ ] | Deus Ex™ GOTY Edition (GOG) | 12 | 20 | 60% (last 20) | No graphics (44%) | 93% | 19d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 234 | [ ] | Hylics (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (69%) | 97% | today | 93% |  |
| 235 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 11 | 20 | 55% (last 20) | Does not open (53%) | 69% | 2d ago | 75% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 236 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 95% | 4d ago | 100% |  |
| 237 | [ ] | XCOM 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (58%) | 80% | 1d ago | 75% |  |
| 238 | [ ] | Dying Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (86%) | 62% | 3d ago | 48% |  |
| 239 | [ ] | Revolution Idle (STEAM) | 10 | 20 | 50% (last 20) | Does not open (43%) | 83% | 2d ago | n/a |  |
| 240 | [ ] | Mafia II (Classic) (GOG) | 13 | 20 | 65% (last 20) | Does not open (95%) | 60% | 4d ago | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 241 | [ ] | Goose Goose Duck (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 67% | 4d ago | 70% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 242 | [ ] | AER Memories of Old (EPIC) | 13 | 20 | 65% (last 20) | Does not open (86%) | 100% | 3d ago | n/a |  |
| 243 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (71%) | 78% | 4d ago | 73% |  |
| 244 | [ ] | SnowRunner (STEAM) | 12 | 20 | 60% (last 20) | Does not open (96%) | 79% | 1d ago | 69% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 245 | [ ] | BATTLETECH (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 96% | 3d ago | 93% |  |
| 246 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 63% | 10d ago | 58% |  |
| 247 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 100% | 11d ago | n/a |  |
| 248 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (78%) | 97% | 2d ago | 96% |  |
| 249 | [ ] | Hero Siege (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (52%) | 82% | 3d ago | 86% |  |
| 250 | [ ] | Secrets of Grindea (STEAM) | 10 | 20 | 50% (last 20) | Does not open (45%) | 75% | 1d ago | 79% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 251 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 85% | 5d ago | 82% |  |
| 252 | [ ] | Tales of Zestiria (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 71% | 24d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 253 | [ ] | Capcom Fighting Collection (STEAM) | 14 | 20 | 70% (last 20) | Does not open (80%) | 83% | 10d ago | 82% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 254 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 14 | 20 | 70% (last 20) | Does not open (85%) | 82% | 11d ago | n/a | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 255 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (95%) | 91% | 10d ago | 88% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 256 | [ ] | Disgaea 4 Complete+ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (43%) | 92% | 4d ago | n/a | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 257 | [ ] | Timberborn (STEAM) | 12 | 20 | 60% (last 20) | No graphics (65%) | 89% | today | 90% |  |
| 258 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 12 | 20 | 60% (last 20) | No graphics (39%) | 79% | 2d ago | n/a | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 259 | [ ] | 12 is Better Than 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 85% | 14d ago | n/a |  |
| 260 | [ ] | No Socks RPG (STEAM) | 11 | 20 | 55% (last 20) | Graphics glitches (91%) | 93% | 2d ago | 91% |  |
| 261 | [ ] | Hatred (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 89% | 11d ago | 94% |  |
| 262 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 93% | 7d ago | 89% |  |
| 263 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 62% | 3d ago | n/a |  |
| 264 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 69% | 9d ago | n/a |  |
| 265 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 90% | 30d ago | 90% |  |
| 266 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 62% | 13d ago | 63% |  |
| 267 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 60% | 6d ago | 54% |  |
| 268 | [ ] | Sons Of The Forest (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 78% | 4d ago | 72% |  |
| 269 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 64% | 1d ago | 71% |  |
| 270 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (50%) | 75% | 11d ago | 91% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 271 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 73% | 1d ago | 80% |  |
| 272 | [ ] | CRUEL (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 78% | 4d ago | 73% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 273 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 81% | 10d ago | 72% |  |
| 274 | [ ] | Super Battle Golf (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 90% | today | 82% |  |
| 275 | [ ] | Hitman: Absolution (GOG) | 10 | 20 | 50% (last 20) | Does not open (83%) | 83% | 1d ago | n/a |  |
| 276 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 90% | 4d ago | 100% |  |
| 277 | [ ] | Shift At Midnight (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 90% | today | 86% |  |
| 278 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 81% | 1d ago | 85% |  |
| 279 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (92%) | 85% | 14d ago | n/a |  |
| 280 | [ ] | Forgive Me Father (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 72% | 5d ago | n/a |  |
| 281 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 85% | 9d ago | 73% |  |
| 282 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 83% | 4d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 283 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 69% | 3d ago | n/a |  |
| 284 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 60% | 2d ago | 73% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 285 | [ ] | The Stanley Parable (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 87% | 5d ago | n/a |  |
| 286 | [ ] | Subnautica: Below Zero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 77% | 10d ago | 69% |  |
| 287 | [ ] | Cruelty Squad (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 85% | 2d ago | 79% |  |
| 288 | [ ] | A Plague Tale: Innocence (GOG) | 10 | 20 | 50% (last 20) | Does not open (91%) | 60% | 1d ago | n/a |  |
| 289 | [ ] | BioShock 2 Remastered (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 89% | today | 85% |  |
| 290 | [ ] | Intravenous (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 77% | 10d ago | 79% |  |
| 291 | [ ] | SILENT HILL 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (58%) | 80% | 4d ago | 92% |  |
| 292 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 75% | 12d ago | 70% |  |
| 293 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 92% | 9d ago | 94% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 294 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 62% | 6d ago | n/a |  |
| 295 | [ ] | Legend of Grimrock 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 93% | 2d ago | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 296 | [ ] | Decktamer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 75% | 4d ago | n/a |  |
| 297 | [ ] | Haydee (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 86% | 4d ago | n/a |  |
| 298 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 95% | 4d ago | 93% |  |
| 299 | [ ] | Helping the Hotties (GOG) | 10 | 20 | 50% (last 20) | Does not open (75%) | 75% | today | n/a |  |
| 300 | [ ] | Secret of Mana (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (56%) | 70% | 1d ago | n/a |  |

## Recently recovered (382)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Grim Dawn (STEAM) | 497 | 2026-11-08 | 571 | 65% |  |
| 2 | [x] | FINAL FANTASY RESONANCE (STEAM) | 448 | 2026-10-24 | 1020 | 79% |  |
| 3 | [x] | Half-Life (STEAM) | 378 | 2026-11-09 | 645 | 71% |  |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 264 | 2026-11-14 | 414 | 66% |  |
| 5 | [x] | Alan Wake (STEAM) | 237 | 2026-11-14 | 261 | 56% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 6 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 233 | 2026-11-09 | 327 | 88% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 7 | [x] | MONSTER HUNTER RISE (STEAM) | 221 | 2026-11-17 | 523 | 62% |  |
| 8 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 205 | 2026-11-09 | 359 | 69% |  |
| 9 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 203 | 2026-11-09 | 244 | 58% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 10 | [x] | BeamNG.drive (STEAM) | 195 | 2026-11-09 | 240 | 73% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 11 | [x] | Call of Duty: Black Ops (STEAM) | 192 | 2026-11-13 | 217 | 21% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 12 | [x] | OMORI (STEAM) | 181 | 2026-11-09 | 225 | 66% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 13 | [x] | DRAGON BALL FighterZ (STEAM) | 171 | 2026-11-01 | 214 | 85% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 14 | [x] | Spelunky 2 (STEAM) | 165 | 2026-11-01 | 205 | 76% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 15 | [x] | Geometry Dash (STEAM) | 151 | 2026-11-11 | 445 | 56% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 16 | [x] | BioShock (STEAM) | 150 | 2026-11-09 | 298 | 72% |  |
| 17 | [x] | Sid Meier's Civilization V (STEAM) | 147 | 2026-11-10 | 159 | 64% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 18 | [x] | Prototype (STEAM) | 141 | 2026-11-11 | 207 | 66% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 19 | [x] | Team Fortress 2 (STEAM) | 139 | 2026-11-09 | 239 | 76% |  |
| 20 | [x] | Minecraft Dungeons II (STEAM) | 131 | 2026-11-09 | 150 | 70% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 21 | [x] | Castlevania Advance Collection (STEAM) | 128 | 2026-11-09 | 200 | 88% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 22 | [x] | Mirror's Edge (STEAM) | 117 | 2026-11-09 | 170 | 66% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 23 | [x] | Assassin's Creed II (STEAM) | 116 | 2026-11-10 | 121 | 67% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 24 | [x] | Aniimo (STEAM) | 114 | 2026-11-09 | 153 | 84% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 25 | [x] | Counter-Strike (STEAM) | 112 | 2026-11-11 | 192 | 38% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 26 | [x] | Cave Story+ (STEAM) | 103 | 2026-11-09 | 113 | 82% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 27 | [x] | The Witcher: Enhanced Edition (STEAM) | 102 | 2026-11-09 | 120 | 71% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 28 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 101 | 2026-11-09 | 142 | 96% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 29 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 98 | 2026-11-15 | 138 | 69% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 30 | [x] | Happy Wheels (STEAM) | 97 | 2026-11-09 | 117 | 70% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 31 | [x] | Moonstone Island (STEAM) | 94 | 2026-11-09 | 123 | 74% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 32 | [x] | Catherine Classic (STEAM) | 89 | 2026-11-09 | 167 | 56% |  |
| 33 | [x] | DOOM 3: BFG Edition (STEAM) | 85 | 2026-11-09 | 126 | 69% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 34 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 82 | 2026-11-09 | 136 | 71% |  |
| 35 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 81 | 2026-11-09 | 108 | 93% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 36 | [x] | Vital Shell (STEAM) | 80 | 2026-11-09 | 129 | 85% |  |
| 37 | [x] | FINAL FANTASY XIII-2 (STEAM) | 80 | 2026-11-09 | 83 | 61% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 38 | [x] | Quake (STEAM) | 78 | 2026-11-09 | 238 | 72% |  |
| 39 | [x] | Psychonauts (STEAM) | 77 | 2026-11-09 | 143 | 95% |  |
| 40 | [x] | Age of Empires II: Definitive Edition (STEAM) | 76 | 2026-11-10 | 95 | 64% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 41 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 74 | 2026-11-19 | 97 | 61% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 42 | [x] | Brawlhalla (STEAM) | 73 | 2026-11-09 | 144 | 73% |  |
| 43 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 73 | 2026-11-09 | 113 | 80% |  |
| 44 | [x] | Ballionaire (STEAM) | 72 | 2026-11-09 | 122 | 81% |  |
| 45 | [x] | The Sims™ 4 (STEAM) | 72 | 2026-11-09 | 97 | 72% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 46 | [x] | STEINS;GATE (STEAM) | 71 | 2026-11-09 | 103 | 89% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 47 | [x] | Cyberpunk 2077 (GOG) | 71 | 2026-11-09 | 93 | 71% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 48 | [x] | Order of the Sinking Star (STEAM) | 69 | 2026-11-09 | 101 | 67% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 49 | [x] | Dota 2 (STEAM) | 68 | 2026-11-09 | 102 | 77% |  |
| 50 | [x] | Disgaea 5 Complete (STEAM) | 68 | 2026-11-09 | 80 | 90% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 51 | [x] | Fable - The Lost Chapters (STEAM) | 67 | 2026-11-09 | 107 | 81% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 52 | [x] | Stardew Valley (GOG) | 66 | 2026-11-11 | 115 | 74% |  |
| 53 | [x] | Need for Speed: Hot Pursuit (STEAM) | 65 | 2026-11-09 | 101 | 77% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 54 | [x] | Spyro™ Reignited Trilogy (STEAM) | 64 | 2026-11-09 | 107 | 78% |  |
| 55 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 64 | 2026-11-09 | 103 | 84% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 56 | [x] | Diablo® IV (STEAM) | 63 | 2026-11-11 | 75 | 69% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 57 | [x] | Sovereign Tower (STEAM) | 62 | 2026-11-09 | 116 | 77% |  |
| 58 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 62 | 2026-11-11 | 82 | 57% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 59 | [x] | Caravan SandWitch (EPIC) | 61 | 2026-11-09 | 123 | 71% |  |
| 60 | [x] | American Truck Simulator (STEAM) | 61 | 2026-11-09 | 103 | 77% |  |
| 61 | [x] | Poppy Playtime (STEAM) | 61 | 2026-11-09 | 103 | 67% |  |
| 62 | [x] | Mini Motorways (STEAM) | 60 | 2026-11-09 | 96 | 67% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 63 | [x] | Borderlands 3 (STEAM) | 60 | 2026-11-09 | 88 | 90% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 64 | [x] | Gunfire Reborn (STEAM) | 60 | 2026-11-09 | 66 | 88% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 65 | [x] | Fallout (STEAM) | 59 | 2026-11-09 | 94 | 70% |  |
| 66 | [x] | Firewatch (STEAM) | 58 | 2026-11-10 | 112 | 79% |  |
| 67 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 58 | 2026-11-09 | 83 | 63% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 68 | [x] | Deskrawl: Idle ARPG (STEAM) | 58 | 2026-11-09 | 72 | 67% | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 69 | [x] | A Plague Tale: Innocence (STEAM) | 58 | 2026-11-09 | 61 | 68% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 70 | [x] | Grand Theft Auto V (EPIC) | 57 | 2026-11-09 | 64 | 79% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 71 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 56 | 2026-10-25 | 97 | 74% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 72 | [x] | eFootball™ (STEAM) | 56 | 2026-11-09 | 84 | 66% |  |
| 73 | [x] | Call of Duty: World at War (STEAM) | 56 | 2026-11-09 | 80 | 83% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 74 | [x] | Call of Juarez Gunslinger (STEAM) | 56 | 2026-11-09 | 71 | 76% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 75 | [x] | Darksiders (STEAM) | 55 | 2026-11-09 | 70 | 88% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 76 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 54 | 2026-11-17 | 78 | 62% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 77 | [x] | Sonic Generations (STEAM) | 54 | 2026-11-09 | 61 | 69% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 78 | [x] | Starbound (STEAM) | 52 | 2026-11-09 | 85 | 82% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 79 | [x] | Sol Cesto (EPIC) | 52 | 2026-11-09 | 53 | 81% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 80 | [x] | MIO: Memories in Orbit (STEAM) | 51 | 2026-11-09 | 104 | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 81 | [x] | Borderlands: The Pre-Sequel (STEAM) | 51 | 2026-11-09 | 88 | 65% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 82 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 51 | 2026-11-09 | 86 | 75% |  |
| 83 | [x] | Last Epoch (STEAM) | 50 | 2026-11-09 | 75 | 70% |  |
| 84 | [x] | Okami HD (STEAM) | 49 | 2026-11-09 | 91 | 93% |  |
| 85 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 48 | 2026-11-09 | 82 | 64% |  |
| 86 | [x] | Heroes of Might & Magic III - HD Edition (STEAM) | 48 | 2026-11-14 | 63 | 62% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 87 | [x] | Overwatch® (STEAM) | 48 | 2026-11-10 | 52 | 69% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 88 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 47 | 2026-11-09 | 79 | 85% |  |
| 89 | [x] | TBH: Task Bar Hero (STEAM) | 47 | 2026-11-09 | 77 | 84% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 90 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 47 | 2026-11-09 | 54 | 95% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 91 | [x] | Moonlighter (EPIC) | 47 | 2026-11-09 | 51 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 92 | [x] | Oxygen Not Included (STEAM) | 46 | 2026-11-11 | 79 | 61% |  |
| 93 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 46 | 2026-11-09 | 76 | 80% |  |
| 94 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 45 | 2026-11-13 | 71 | 63% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 95 | [x] | Cat Quest (EPIC) | 44 | 2026-11-19 | 104 | 47% |  |
| 96 | [x] | Darkest Dungeon® (EPIC) | 44 | 2026-11-09 | 86 | 84% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 97 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 44 | 2026-11-09 | 68 | 91% |  |
| 98 | [x] | MudRunner (STEAM) | 43 | 2026-10-24 | 98 | 60% |  |
| 99 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 43 | 2026-11-09 | 73 | 54% |  |
| 100 | [x] | Plague Inc: Evolved (STEAM) | 43 | 2026-11-16 | 64 | 62% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 101 | [x] | Big Walk (STEAM) | 42 | 2026-11-09 | 66 | 62% |  |
| 102 | [x] | Sheepy: A Short Adventure (STEAM) | 42 | 2026-11-09 | 50 | 62% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 103 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 39 | 2026-11-09 | 71 | 90% |  |
| 104 | [x] | Tomb Raider: Anniversary (STEAM) | 39 | 2026-11-09 | 64 | 56% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 105 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 39 | 2026-11-09 | 60 | 66% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 106 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-11-09 | 40 | 79% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 107 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 38 | 2026-11-09 | 72 | 89% |  |
| 108 | [x] | Ace Attorney Investigations Collection (STEAM) | 38 | 2026-11-09 | 66 | 88% |  |
| 109 | [x] | Age of Empires II (2013) (STEAM) | 38 | 2026-11-09 | 63 | 71% |  |
| 110 | [x] | Sonic Lost World (STEAM) | 38 | 2026-11-09 | 58 | 82% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 111 | [x] | Aggelos (STEAM) | 38 | 2026-11-09 | 54 | 88% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 112 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 38 | 2026-11-09 | 54 | 75% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 113 | [x] | Digimon World: Next Order (STEAM) | 37 | 2026-11-09 | 75 | 85% |  |
| 114 | [x] | Street Fighter™ 6 (STEAM) | 37 | 2026-11-09 | 59 | 82% |  |
| 115 | [x] | FINAL FANTASY VII (2013) (STEAM) | 37 | 2026-11-09 | 54 | 57% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 116 | [x] | Dead by Daylight (STEAM) | 37 | 2026-11-09 | 41 | 83% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 117 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 37 | 2026-11-19 | 39 | 91% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 118 | [x] | Amnesia: The Dark Descent (STEAM) | 36 | 2026-11-09 | 73 | 86% |  |
| 119 | [x] | Sonic Origins (STEAM) | 36 | 2026-11-09 | 67 | 83% |  |
| 120 | [x] | XCOM 2 (STEAM) | 36 | 2026-11-09 | 61 | 80% |  |
| 121 | [x] | Capcom Arcade Stadium (STEAM) | 36 | 2026-11-09 | 46 | 74% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 122 | [x] | POSTAL 2 (GOG) | 35 | 2026-11-09 | 68 | 95% |  |
| 123 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 35 | 2026-11-09 | 67 | 83% |  |
| 124 | [x] | Russian Fishing 4 (STEAM) | 35 | 2026-11-09 | 41 | 83% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 125 | [x] | CrossCode (GOG) | 35 | 2026-11-09 | 38 | 78% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 126 | [x] | SurrounDead (STEAM) | 34 | 2026-11-09 | 65 | 90% |  |
| 127 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 34 | 2026-11-09 | 61 | 74% |  |
| 128 | [x] | Need for Speed™ Rivals (STEAM) | 34 | 2026-11-10 | 46 | 80% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 129 | [x] | Being a DIK (STEAM) | 33 | 2026-11-09 | 72 | 63% |  |
| 130 | [x] | The Bazaar (STEAM) | 33 | 2026-11-09 | 63 | 77% |  |
| 131 | [x] | Hero Siege (STEAM) | 33 | 2026-11-09 | 57 | 82% |  |
| 132 | [x] | Max Payne (STEAM) | 33 | 2026-11-09 | 56 | 82% |  |
| 133 | [x] | Gauntlet™  (STEAM) | 33 | 2026-11-11 | 48 | 67% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 134 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 32 | 2026-11-09 | 69 | 70% |  |
| 135 | [x] | Hearts of Iron IV (STEAM) | 32 | 2026-11-09 | 64 | 81% |  |
| 136 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 32 | 2026-11-09 | 56 | 74% |  |
| 137 | [x] | Earthion (STEAM) | 32 | 2026-11-09 | 54 | 100% |  |
| 138 | [x] | SnowRunner (STEAM) | 32 | 2026-11-09 | 47 | 79% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 139 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-11-09 | 40 | 100% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 140 | [x] | Journey (STEAM) | 31 | 2026-10-27 | 71 | 68% |  |
| 141 | [x] | COCOON (STEAM) | 31 | 2026-11-09 | 66 | 82% |  |
| 142 | [x] | ROB RUN (STEAM) | 31 | 2026-11-17 | 42 | 65% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 143 | [x] | Red Dead Redemption (STEAM) | 31 | 2026-11-09 | 34 | 56% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 144 | [x] | Ultimate Chicken Horse (STEAM) | 30 | 2026-10-23 | 64 | 88% |  |
| 145 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 30 | 2026-11-09 | 51 | 88% |  |
| 146 | [x] | Resident Evil Village (STEAM) | 30 | 2026-11-09 | 51 | 89% |  |
| 147 | [x] | Prince of Persia: The Sands of Time (STEAM) | 30 | 2026-11-09 | 50 | 78% |  |
| 148 | [x] | Counter-Strike:Global Offensive (STEAM) | 30 | 2026-11-09 | 46 | 68% |  |
| 149 | [x] | Supermarket Together (STEAM) | 30 | 2026-11-18 | 42 | 61% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 150 | [x] | Torchlight II (STEAM) | 29 | 2026-10-20 | 71 | 86% |  |
| 151 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 29 | 2026-11-09 | 61 | 87% |  |
| 152 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 29 | 2026-11-09 | 50 | 89% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 153 | [x] | Secrets of Grindea (STEAM) | 29 | 2026-11-09 | 49 | 75% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 154 | [x] | Gambonanza (STEAM) | 29 | 2026-11-09 | 47 | 92% |  |
| 155 | [x] | Yakuza: Like a Dragon (STEAM) | 29 | 2026-11-09 | 47 | 67% |  |
| 156 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 29 | 2026-11-09 | 45 | 82% |  |
| 157 | [x] | Palia (STEAM) | 29 | 2026-11-09 | 41 | 74% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 158 | [x] | Gothic II: Gold Classic (STEAM) | 29 | 2026-11-09 | 37 | 65% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 159 | [x] | Hotline Miami (GOG) | 29 | 2026-11-18 | 36 | 71% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 160 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 72% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 161 | [x] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 29 | 2026-11-14 | 34 | 73% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 162 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 28 | 2026-11-09 | 48 | 70% |  |
| 163 | [x] | Heavy Rain (STEAM) | 28 | 2026-11-09 | 47 | 94% |  |
| 164 | [x] | Resident Evil Revelations 2 (STEAM) | 27 | 2026-11-09 | 53 | 83% |  |
| 165 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 27 | 2026-11-09 | 49 | 96% |  |
| 166 | [x] | Tower and Sword of Succubus (STEAM) | 27 | 2026-11-09 | 42 | 82% |  |
| 167 | [x] | Digimon Survive (STEAM) | 27 | 2026-11-09 | 40 | 85% |  |
| 168 | [x] | Skullgirls 2nd Encore (STEAM) | 26 | 2026-11-10 | 61 | 68% |  |
| 169 | [x] | Deponia (STEAM) | 26 | 2026-11-09 | 51 | 73% |  |
| 170 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 45 | 71% |  |
| 171 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 26 | 2026-11-09 | 42 | 69% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 172 | [x] | Dead Rising 2 (STEAM) | 26 | 2026-11-09 | 42 | 79% |  |
| 173 | [x] | CRUEL (STEAM) | 26 | 2026-11-09 | 36 | 78% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 174 | [x] | Guildrun Demo (STEAM) | 25 | 2026-11-09 | 42 | 83% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 175 | [x] | Timberborn (STEAM) | 25 | 2026-11-09 | 37 | 89% |  |
| 176 | [x] | Ultimate Custom Night (STEAM) | 25 | 2026-11-19 | 35 | 62% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 177 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-19 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 178 | [x] | Subnautica 2 (STEAM) | 25 | 2026-11-15 | 30 | 79% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 179 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 24 | 2026-10-20 | 53 | 83% |  |
| 180 | [x] | Slow Roads (STEAM) | 24 | 2026-10-22 | 51 | 67% |  |
| 181 | [x] | Frostpunk (STEAM) | 24 | 2026-11-09 | 50 | 74% |  |
| 182 | [x] | Mirror's Edge™ (GOG) | 24 | 2026-11-13 | 46 | 73% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 183 | [x] | Lucid Blocks (STEAM) | 24 | 2026-11-09 | 45 | 66% |  |
| 184 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 24 | 2026-11-09 | 44 | 62% |  |
| 185 | [x] | Capcom Fighting Collection 2 (STEAM) | 24 | 2026-11-09 | 41 | 82% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 186 | [x] | Cat Mail Co. (STEAM) | 24 | 2026-11-09 | 40 | 85% |  |
| 187 | [x] | Opus Magnum (STEAM) | 24 | 2026-11-09 | 39 | 92% |  |
| 188 | [x] | Limbus Company (STEAM) | 24 | 2026-11-09 | 38 | 85% |  |
| 189 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 24 | 2026-11-09 | 38 | 73% |  |
| 190 | [x] | Ratatan (STEAM) | 24 | 2026-11-09 | 37 | 90% |  |
| 191 | [x] | Dishonored 2 (STEAM) | 24 | 2026-11-09 | 34 | 71% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 192 | [x] | Jade Empire: Special Edition (GOG) | 24 | 2026-11-09 | 31 | 70% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 193 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 24 | 2026-11-09 | 30 | 64% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 194 | [x] | Crab Game (STEAM) | 24 | 2026-11-09 | 28 | 82% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 195 | [x] | Northgard: Definitive Edition (STEAM) | 24 | 2026-11-19 | 27 | 90% | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 196 | [x] | Chained Echoes (GOG) | 23 | 2026-11-19 | 51 | 60% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 197 | [x] | Goat Simulator (STEAM) | 23 | 2026-11-09 | 48 | 64% |  |
| 198 | [x] | Battle Brothers (STEAM) | 23 | 2026-11-09 | 44 | 80% |  |
| 199 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 44 | 89% |  |
| 200 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-11-09 | 44 | 92% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 201 | [x] | Trailmakers (STEAM) | 23 | 2026-11-09 | 41 | 94% |  |
| 202 | [x] | Changed (STEAM) | 23 | 2026-11-18 | 34 | 64% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 203 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 91% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 204 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 23 | 2026-11-09 | 27 | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 205 | [x] | Jade Empire: Special Edition (STEAM) | 23 | 2026-11-09 | 26 | 75% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 206 | [x] | Prince of Persia (GOG) | 22 | 2026-11-09 | 43 | 80% |  |
| 207 | [x] | Wizard of Legend (EPIC) | 22 | 2026-11-09 | 41 | 83% |  |
| 208 | [x] | Counter-Strike: Condition Zero (STEAM) | 22 | 2026-11-11 | 41 | 25% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 209 | [x] | Football Manager 2024 (EPIC) | 22 | 2026-11-09 | 40 | 66% |  |
| 210 | [x] | My Summer Car (STEAM) | 22 | 2026-11-09 | 37 | 79% |  |
| 211 | [x] | Tabletop Simulator (STEAM) | 22 | 2026-11-09 | 37 | 79% |  |
| 212 | [x] | Deus Ex™ GOTY Edition (GOG) | 22 | 2026-11-09 | 35 | 93% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 213 | [x] | Mafia II (Classic) (GOG) | 22 | 2026-11-19 | 32 | 60% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 214 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 61 | 97% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 215 | [x] | Crazy Taxi (STEAM) | 21 | 2026-11-10 | 43 | 67% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 216 | [x] | Control Ultimate Edition (GOG) | 21 | 2026-11-09 | 39 | 78% |  |
| 217 | [x] | Unturned (STEAM) | 21 | 2026-11-09 | 39 | 71% |  |
| 218 | [x] | Invisible, Inc. (STEAM) | 21 | 2026-11-09 | 37 | 77% |  |
| 219 | [x] | Sorry We're Closed (EPIC) | 21 | 2026-11-09 | 35 | 71% |  |
| 220 | [x] | Goose Goose Duck (STEAM) | 21 | 2026-11-18 | 31 | 67% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 221 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 88% |  |
| 222 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 21 | 2026-11-09 | 27 | 91% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 223 | [x] | CarX Street (STEAM) | 21 | 2026-11-09 | 26 | 81% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 224 | [x] | Dead Island (STEAM) | 21 | 2026-11-09 | 26 | 91% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 225 | [x] | Tearscape (STEAM) | 21 | 2026-11-09 | 25 | 89% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 226 | [x] | Worms W.M.D (STEAM) | 20 | 2026-11-09 | 37 | 97% |  |
| 227 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-11-09 | 36 | 100% |  |
| 228 | [x] | Return to Monkey Island (STEAM) | 20 | 2026-11-09 | 33 | 68% |  |
| 229 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 20 | 2026-11-09 | 30 | 92% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 230 | [x] | Torchlight II (EPIC) | 20 | 2026-11-09 | 28 | 77% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 231 | [x] | Tyr (STEAM) | 20 | 2026-11-09 | 28 | 67% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 232 | [x] | Tales of Zestiria (STEAM) | 20 | 2026-11-09 | 26 | 71% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 233 | [x] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 2026-11-15 | 36 | 69% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 234 | [x] | Pinball FX Classic (STEAM) | 19 | 2026-11-09 | 35 | 87% |  |
| 235 | [x] | SWORN (STEAM) | 19 | 2026-11-09 | 34 | 93% |  |
| 236 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 19 | 2026-11-09 | 33 | 75% |  |
| 237 | [x] | Far Far West (STEAM) | 19 | 2026-11-09 | 33 | 52% |  |
| 238 | [x] | One-armed robber (STEAM) | 19 | 2026-11-09 | 33 | 71% |  |
| 239 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 32 | 69% |  |
| 240 | [x] | Moonlight Peaks (STEAM) | 19 | 2026-11-09 | 31 | 74% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 241 | [x] | GOD EATER RESURRECTION (STEAM) | 19 | 2026-11-09 | 30 | 75% |  |
| 242 | [x] | Backpack Battles (STEAM) | 18 | 2026-11-09 | 42 | 93% |  |
| 243 | [x] | Mini Metro (STEAM) | 18 | 2026-11-16 | 37 | 59% |  |
| 244 | [x] | This War of Mine (STEAM) | 18 | 2026-11-17 | 34 | 46% |  |
| 245 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 2026-11-09 | 29 | 79% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 246 | [x] | Beyond: Two Souls (STEAM) | 18 | 2026-11-19 | 27 | 63% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 247 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-11-09 | 27 | 80% |  |
| 248 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-18 | 23 | 73% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 249 | [x] | Mafia II: Definitive Edition (GOG) | 18 | 2026-11-15 | 20 | 60% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 250 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 37 | 21% |  |
| 251 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 33 | 93% |  |
| 252 | [x] | Party Animals (STEAM) | 17 | 2026-11-09 | 25 | 68% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 253 | [x] | Capcom Fighting Collection (STEAM) | 17 | 2026-11-09 | 24 | 83% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 254 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 255 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 256 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 16 | 2026-10-25 | 42 | 70% |  |
| 257 | [x] | Kingdom Come: Deliverance II (STEAM) | 16 | 2026-10-20 | 39 | 83% |  |
| 258 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 16 | 2026-10-20 | 37 | 85% |  |
| 259 | [x] | GRIP: Combat Racing (STEAM) | 16 | 2026-11-09 | 35 | 78% |  |
| 260 | [x] | sobosuba (STEAM) | 16 | 2026-11-09 | 34 | 84% |  |
| 261 | [x] | Intravenous 2 (STEAM) | 16 | 2026-11-09 | 31 | 96% |  |
| 262 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 263 | [x] | Mortal Kombat 11 (STEAM) | 16 | 2026-11-09 | 27 | 69% |  |
| 264 | [x] | Legend of Grimrock 2 (STEAM) | 16 | 2026-11-09 | 26 | 93% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 265 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 60% |  |
| 266 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 267 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 268 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 15 | 2026-10-21 | 42 | 79% |  |
| 269 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 15 | 2026-11-11 | 34 | 70% |  |
| 270 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 31 | 96% |  |
| 271 | [x] | Tiny Glade (STEAM) | 15 | 2026-11-09 | 30 | 69% |  |
| 272 | [x] | GRANDIA HD Remaster (STEAM) | 15 | 2026-11-09 | 28 | 89% |  |
| 273 | [x] | PAYDAY: The Heist (STEAM) | 15 | 2026-11-13 | 27 | 67% |  |
| 274 | [x] | Gloomwood (STEAM) | 15 | 2026-11-19 | 26 | 62% |  |
| 275 | [x] | AER Memories of Old (EPIC) | 15 | 2026-11-09 | 25 | 100% |  |
| 276 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 15 | 2026-11-15 | 25 | 62% |  |
| 277 | [x] | Alabaster Dawn Demo (STEAM) | 15 | 2026-11-09 | 23 | 78% |  |
| 278 | [x] | Need for Speed™ Unbound (STEAM) | 15 | 2026-11-09 | 23 | 58% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 279 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 93% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 280 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 281 | [x] | Spark the Electric Jester (STEAM) | 15 | 2026-11-13 | 21 | 69% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 282 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 15 | 2026-11-09 | 21 | 82% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 283 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 284 | [x] | ABZÛ (STEAM) | 14 | 2026-10-21 | 44 | 91% |  |
| 285 | [x] | Faster Than Light (EPIC) | 14 | 2026-11-09 | 31 | 93% |  |
| 286 | [x] | Mark of the Ninja (STEAM) | 14 | 2026-10-26 | 31 | 83% |  |
| 287 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 94% |  |
| 288 | [x] | Hitman: Absolution (GOG) | 14 | 2026-11-09 | 29 | 83% |  |
| 289 | [x] | Castle in the Clouds (STEAM) | 14 | 2026-11-09 | 28 | 57% |  |
| 290 | [x] | Evoland (STEAM) | 14 | 2026-11-11 | 28 | n/a |  |
| 291 | [x] | Human Fall Flat (STEAM) | 14 | 2026-10-29 | 28 | 62% |  |
| 292 | [x] | Titanfall® 2 (STEAM) | 14 | 2026-11-09 | 28 | 77% |  |
| 293 | [x] | Ultrapool (STEAM) | 14 | 2026-11-09 | 27 | 100% |  |
| 294 | [x] | Batman™: Arkham Origins (GOG) | 14 | 2026-11-09 | 26 | 100% |  |
| 295 | [x] | WORLD OF FINAL FANTASY (STEAM) | 14 | 2026-11-09 | 25 | 85% |  |
| 296 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-11-09 | 22 | 92% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 297 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 298 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 2026-11-16 | 22 | 81% |  |
| 299 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 21 | 69% |  |
| 300 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 301 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 302 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 29 | 81% |  |
| 303 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 13 | 2026-11-09 | 28 | 90% |  |
| 304 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 28 | 83% |  |
| 305 | [x] | MX Bikes (STEAM) | 13 | 2026-11-09 | 27 | 92% |  |
| 306 | [x] | Blaster Master Zero (STEAM) | 13 | 2026-11-11 | 26 | 76% |  |
| 307 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 13 | 2026-11-09 | 26 | 63% |  |
| 308 | [x] | Cruelty Squad (STEAM) | 13 | 2026-11-09 | 25 | 85% |  |
| 309 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 13 | 2026-11-13 | 25 | 70% |  |
| 310 | [x] | Haydee (STEAM) | 13 | 2026-11-09 | 24 | 86% |  |
| 311 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 24 | 78% |  |
| 312 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 13 | 2026-11-09 | 23 | 64% |  |
| 313 | [x] | 12 is Better Than 6 (STEAM) | 13 | 2026-11-09 | 22 | 85% |  |
| 314 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 315 | [x] | Nex Machina (STEAM) | 13 | 2026-11-09 | 21 | 75% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 316 | [x] | Shift At Midnight (STEAM) | 13 | 2026-11-09 | 21 | 90% |  |
| 317 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 70% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 318 | [x] | The Stanley Parable (STEAM) | 13 | 2026-11-13 | 21 | 87% |  |
| 319 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 100% |  |
| 320 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 321 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 2026-11-09 | 20 | 85% |  |
| 322 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-11-16 | 20 | 90% |  |
| 323 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 80% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 324 | [x] | Dead Space™ 3 (STEAM) | 12 | 2026-10-20 | 29 | 71% |  |
| 325 | [x] | Overlord (STEAM) | 12 | 2026-11-08 | 29 | 58% |  |
| 326 | [x] | Antichamber (STEAM) | 12 | 2026-11-18 | 27 | 80% |  |
| 327 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 26 | 78% |  |
| 328 | [x] | Need for Speed: Undercover (STEAM) | 12 | 2026-11-11 | 25 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 329 | [x] | A Plague Tale: Innocence (GOG) | 12 | 2026-11-18 | 24 | 60% |  |
| 330 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-10 | 24 | 60% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 331 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 24 | 67% |  |
| 332 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-11-09 | 22 | 97% |  |
| 333 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 334 | [x] | Horny Villa (STEAM) | 12 | 2026-11-09 | 21 | 85% |  |
| 335 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 336 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 337 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 2026-11-10 | 20 | 60% |  |
| 338 | [x] | Turbo Overkill (STEAM) | 12 | 2026-11-09 | 20 | 95% |  |
| 339 | [x] | Haiku, the Robot (STEAM) | 11 | 2026-10-21 | 27 | n/a |  |
| 340 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 2026-11-09 | 26 | 88% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 341 | [x] | Soul's Remnant (STEAM) | 11 | 2026-11-11 | 26 | n/a |  |
| 342 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 25 | 85% |  |
| 343 | [x] | Guacamelee! Gold Edition (STEAM) | 11 | 2026-11-11 | 25 | 75% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 344 | [x] | Alan Wake's American Nightmare (EPIC) | 11 | 2026-11-09 | 24 | 69% |  |
| 345 | [x] | Life is Strange Remastered (STEAM) | 11 | 2026-11-09 | 23 | 86% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 346 | [x] | Ready or Not (STEAM) | 11 | 2026-11-09 | 23 | 84% |  |
| 347 | [x] | Lost Castle 2 (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 348 | [x] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 2026-11-18 | 21 | 62% |  |
| 349 | [x] | Forgive Me Father (STEAM) | 11 | 2026-11-15 | 21 | 72% |  |
| 350 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 351 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-11-09 | 20 | 75% |  |
| 352 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 353 | [x] | The WereCleaner (STEAM) | 10 | 2026-10-22 | 31 | 89% |  |
| 354 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 28 | 90% |  |
| 355 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 10 | 2026-10-27 | 25 | 79% |  |
| 356 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 25 | 91% |  |
| 357 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 10 | 2026-11-01 | 24 | n/a |  |
| 358 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 10 | 2026-10-23 | 24 | 87% |  |
| 359 | [x] | Breath of Fire IV (GOG) | 10 | 2026-10-26 | 23 | 70% |  |
| 360 | [x] | DiRT 4 (STEAM) | 10 | 2026-11-09 | 22 | 95% |  |
| 361 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 10 | 2026-11-09 | 22 | 75% |  |
| 362 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 363 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 364 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 20 | 77% |  |
| 365 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 366 | [x] | Secret of Mana (STEAM) | 10 | 2026-11-18 | 20 | 70% |  |
| 367 | [x] | Possessor(s) (STEAM) | 9 | 2026-10-24 | 27 | 85% |  |
| 368 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 9 | 2026-10-20 | 26 | 88% |  |
| 369 | [x] | Rayman Origins (GOG) | 9 | 2026-11-09 | 22 | 67% |  |
| 370 | [x] | Aperture Desk Job (STEAM) | 9 | 2026-11-03 | 22 | n/a |  |
| 371 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 9 | 2026-10-21 | 21 | 92% |  |
| 372 | [x] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 9 | 2026-11-17 | 20 | 30% |  |
| 373 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 27% |  |
| 374 | [x] | UNDEFEATED (STEAM) | 9 | 2026-11-09 | 20 | 70% |  |
| 375 | [x] | Lust Goddess (STEAM) | 8 | 2026-11-09 | 22 | 81% |  |
| 376 | [x] | SteamWorld Heist (GOG) | 8 | 2026-10-25 | 20 | n/a |  |
| 377 | [x] | HITMAN World of Assassination (STEAM) | 8 | 2026-11-09 | 20 | 80% |  |
| 378 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 21 | 56% |  |
| 379 | [x] | SCP – Containment Breach (STEAM) | 7 | 2026-10-27 | 21 | 91% |  |
| 380 | [x] | Mina the Hollower (GOG) | 7 | 2026-10-28 | 20 | 74% |  |
| 381 | [x] | CULTIC (STEAM) | 7 | 2026-11-09 | 20 | 53% |  |
| 382 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 5 | 2026-10-20 | 20 | 62% |  |
