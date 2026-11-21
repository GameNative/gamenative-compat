# GameNative compatibility worklist

Generated: `2026-11-21T04:15:12.294Z` · Ratings since: `2026-08-23T04:15:12.294Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Probably does not work | 189 |
| Fix shipped, waiting for ratings | 15 |
| First launch fails | 302 |
| Mixed | 477 |
| Works | 1028 |
| Total | 2137 |

## Does not work (126)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 152 | 180 | 84% (14d) | Does not open (83%) | 48% | today | 27% (drop) | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 164 | 188 | 87% (since fix) | Does not open (92%) | 42% | today | 35% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 3 | [ ] | Rocket League® (EPIC) | 83 | 93 | 89% (14d) | Does not open (80%) | 39% | today | 28% | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 4 | [ ] | Hogwarts Legacy (STEAM) | 40 | 42 | 95% (14d) | Does not open (71%) | 28% | today | 16% | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 5 | [ ] | DREDGE (EPIC) | 38 | 40 | 95% (14d) | Does not open (78%) | 56% | today | 46% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 6 | [ ] | Melvor Idle 2: A RuneScape Adventure (STEAM) | 34 | 35 | 97% (14d) | Does not open (96%) | 34% | today | 33% | [#543](https://github.com/GameNative/gamenative-compat/issues/543) |
| 7 | [ ] | Horizon Chase Turbo (EPIC) | 30 | 37 | 81% (14d) | Does not open (84%) | 57% | today | 47% | [#546](https://github.com/GameNative/gamenative-compat/issues/546) |
| 8 | [x] 2026-10-18 | Project Zomboid (STEAM) | 61 | 67 | 91% (since fix) | Does not open (63%) | 40% | today | 35% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 9 | [ ] | Bloons TD 6 (EPIC) | 21 | 22 | 95% (14d) | Does not open (79%) | 39% | 1d ago | 24% | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 10 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 21 | 21 | 100% (14d) | Does not open (96%) | 30% | 6d ago | 21% | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 11 | [ ] | Path of Exile (STEAM) | 20 | 22 | 91% (14d) | Does not open (89%) | 29% | 1d ago | 26% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 12 | [ ] | Metro: Last Light Redux (STEAM) | 20 | 20 | 100% (last 20) | Does not open (91%) | 24% | 2d ago | 27% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 13 | [ ] | BioShock Remastered (EPIC) | 18 | 24 | 75% (14d) | Does not open (67%) | 58% | today | 52% | [#547](https://github.com/GameNative/gamenative-compat/issues/547) |
| 14 | [ ] | Sifu (EPIC) | 18 | 22 | 82% (14d) | Does not open (73%) | 46% | today | 36% | [#535](https://github.com/GameNative/gamenative-compat/issues/535) |
| 15 | [ ] | Saints Row 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | 33% | today | 30% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 16 | [ ] | Borderlands 2 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (80%) | 50% | 2d ago | 46% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 17 | [ ] | Saints Row 2 (GOG) | 15 | 20 | 75% (14d) | Does not open (90%) | 38% | 3d ago | 39% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 18 | [ ] | Mark of the Deep (EPIC) | 15 | 21 | 71% (14d) | Does not open (92%) | 23% | today | 18% |  |
| 19 | [ ] | Mafia II (Classic) (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 8% | 3d ago | 12% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 20 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 14 | 20 | 70% (last 20) | Does not open (78%) | 54% | today | 46% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 21 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (76%) | 0% | 12d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 22 | [ ] | River City Girls (EPIC) | 14 | 20 | 70% (last 20) | Does not open (48%) | 59% | today | 42% |  |
| 23 | [ ] | Call of Duty: Black Ops II (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 40% | today | 40% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 24 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | 56% | 1d ago | 46% | [#548](https://github.com/GameNative/gamenative-compat/issues/548) |
| 25 | [ ] | Vampire Survivors (EPIC) | 17 | 20 | 85% (last 20) | Does not open (61%) | 42% | today | 30% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 26 | [ ] | skate. (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | 12% | 2d ago | 14% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 27 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (92%) | 24% | 7d ago | 15% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 28 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 10 | 14 | 71% (since fix) | Does not open (90%) | 39% | 1d ago | 46% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 29 | [ ] | Driver: Parallel Lines (STEAM) | 19 | 20 | 95% (last 20) | Does not open (65%) | 54% | 12d ago | 60% | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 30 | [ ] | Teenage Mutant Ninja Turtles: Shredder's Revenge (EPIC) | 14 | 20 | 70% (last 20) | Does not open (84%) | 52% | today | 45% |  |
| 31 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (78%) | 6% | 6d ago | 8% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 32 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 37% | 3d ago | 29% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 33 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 16 | 20 | 80% (last 20) | Does not open (45%) | 41% | 2d ago | 60% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 34 | [ ] | Forza Horizon 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (47%) | 47% | 3d ago | 23% (drop) | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 35 | [ ] | Hogwarts Legacy (EPIC) | 14 | 20 | 70% (last 20) | Does not open (75%) | 50% | today | 38% | [#537](https://github.com/GameNative/gamenative-compat/issues/537) |
| 36 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 52% | 1d ago | 62% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 37 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (71%) | 20% | 2d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 38 | [ ] | Fall Guys (EPIC) | 20 | 20 | 100% (last 20) | Does not open (70%) | 9% | 1d ago | 6% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 39 | [ ] | Trackmania (STEAM) | 17 | 20 | 85% (last 20) | Does not open (83%) | 22% | today | 29% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 40 | [ ] | Kenshi (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 4% | 2d ago | 0% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 41 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 8% | 9d ago | 5% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 42 | [ ] | The Witcher: Enhanced Edition (GOG) | 18 | 20 | 90% (last 20) | Does not open (75%) | 8% | 1d ago | 12% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 43 | [ ] | Breath of Fire IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (64%) | 15% | 1d ago | 11% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 44 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (70%) | 15% | 2d ago | 20% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 45 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | 0% | 6d ago | 0% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 46 | [ ] | Call of Duty® (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | 0% | today | 0% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 47 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (70%) | 7% | 20d ago | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 48 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (93%) | 11% | 3d ago | n/a | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 49 | [ ] | Deliver At All Costs (EPIC) | 14 | 20 | 70% (last 20) | Does not open (62%) | 49% | today | 46% | [#538](https://github.com/GameNative/gamenative-compat/issues/538) |
| 50 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (80%) | 12% | 12d ago | 17% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 51 | [ ] | MECCHA CHAMELEON (STEAM) | 15 | 20 | 75% (last 20) | Does not open (68%) | 38% | 3d ago | 32% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 52 | [ ] | CPM 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (88%) | 6% | today | 4% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 53 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 55% | 5d ago | 44% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 54 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (88%) | 17% | 12d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 55 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | 27% | 7d ago | n/a | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 56 | [ ] | Borderlands GOTY (STEAM) | 16 | 20 | 80% (last 20) | Does not open (94%) | 38% | 1d ago | 47% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 57 | [ ] | Blood Omen: Legacy of Kain (GOG) | 16 | 20 | 80% (last 20) | No graphics (57%) | 57% | 2d ago | 55% | [#539](https://github.com/GameNative/gamenative-compat/issues/539) |
| 58 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (83%) | 46% | 3d ago | 47% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 59 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 26% | today | 38% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 60 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (89%) | 54% | today | 58% | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 61 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (68%) | 24% | 9d ago | 27% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 62 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (77%) | 6% | 6d ago | 8% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 63 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | 0% | 7d ago | 0% | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 64 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (54%) | 29% | 3d ago | 18% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 65 | [ ] | Half-Life: Blue Shift (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 36% | 4d ago | 45% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 66 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | 45% | 42d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 67 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (82%) | 0% | 6d ago | n/a | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 68 | [ ] | Rivals of Aether II (STEAM) | 16 | 20 | 80% (last 20) | Does not open (53%) | 41% | 4d ago | 10% (drop) | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 69 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (71%) | 48% | 9d ago | 33% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 70 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | 10% | 8d ago | 10% | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 71 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 41% | 7d ago | 53% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 72 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (47%) | 44% | today | 43% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 73 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 32% | 12d ago | 38% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 74 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | 27% | 4d ago | 25% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 75 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 30% | 9d ago | 14% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 76 | [ ] | Black Mesa (STEAM) | 14 | 20 | 70% (last 20) | Does not open (86%) | 29% | 3d ago | 33% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 77 | [ ] | Watch_Dogs (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | 31% | 1d ago | 38% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 78 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 18% | 30d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 79 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 19 | 20 | 95% (last 20) | Does not open (85%) | 45% | 4d ago | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 80 | [ ] | XCOM: Enemy Unknown (STEAM) | 18 | 20 | 90% (last 20) | Does not open (71%) | 17% | 7d ago | n/a | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 81 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (73%) | 33% | 14d ago | 23% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 82 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 8% | 19d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 83 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (59%) | 58% | 9d ago | 61% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 84 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | Does not open (63%) | 25% | today | 29% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 85 | [ ] | Umamusume: Pretty Derby (STEAM) | 19 | 20 | 95% (last 20) | Does not open (82%) | 52% | 1d ago | 53% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 86 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 20% | 19d ago | n/a | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 87 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 58% | 10d ago | 40% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 88 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 2% | 9d ago | 1% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 89 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | 30% | 10d ago | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 90 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 13% | 21d ago | n/a | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 91 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 56% | 9d ago | 69% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 92 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 27% | today | 31% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 93 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (53%) | 58% | 2d ago | 63% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 94 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (73%) | 0% | 34d ago | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 95 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (62%) | 0% | 2d ago | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 96 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 25% | 1d ago | 20% | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 97 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 19 | 20 | 95% (last 20) | No graphics (59%) | 37% | 7d ago | 44% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 98 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 6% | 27d ago | 7% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 99 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (64%) | 46% | 1d ago | 50% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 100 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (89%) | 20% | 13d ago | 9% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 101 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 3% | 16d ago | 4% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 102 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (61%) | 46% | 9d ago | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 103 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | 21% | 19d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 104 | [ ] | Assassin's Creed Brotherhood (STEAM) | 18 | 20 | 90% (last 20) | Does not open (94%) | 36% | today | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 105 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 20 | 80% (last 20) | Does not open (53%) | 48% | today | 33% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 106 | [ ] | Lost Planet: Extreme Condition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | 42% | 6d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 107 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (89%) | 32% | 5d ago | 37% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 108 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (97%) | 27% | 19d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 109 | [ ] | Aliens vs. Predator (STEAM) | 16 | 20 | 80% (last 20) | Does not open (65%) | 33% | today | 36% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 110 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (50%) | 58% | 24d ago | 42% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 111 | [ ] | OneShot (STEAM) | 15 | 20 | 75% (last 20) | Does not open (96%) | 18% | today | n/a | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 112 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 36% | 21d ago | n/a | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 113 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (55%) | 50% | 9d ago | 22% (drop) | [#540](https://github.com/GameNative/gamenative-compat/issues/540) |
| 114 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 20% | 35d ago | 30% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 115 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | 42% | 21d ago | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 116 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | 47% | 7d ago | 40% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 117 | [ ] | Beyond Good & Evil™ (GOG) | 17 | 20 | 85% (last 20) | Does not open (100%) | 9% | 2d ago | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 118 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | 27% | 10d ago | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 119 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 20 | 80% (last 20) | Does not open (82%) | 59% | 5d ago | 40% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 120 | [ ] | Maneater (STEAM) | 14 | 20 | 70% (last 20) | Does not open (86%) | 59% | today | 63% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 121 | [ ] | Hitman 2: Silent Assassin (STEAM) | 14 | 20 | 70% (last 20) | Does not open (67%) | 42% | today | 44% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 122 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (73%) | 54% | 12d ago | 70% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 123 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (54%) | 42% | 6d ago | n/a | [#541](https://github.com/GameNative/gamenative-compat/issues/541) |
| 124 | [ ] | Maneater (EPIC) | 16 | 20 | 80% (last 20) | Does not open (73%) | 33% | 5d ago | 15% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 125 | [ ] | Ghostwire Tokyo (EPIC) | 14 | 20 | 70% (last 20) | Does not open (90%) | 52% | 6d ago | 38% | [#544](https://github.com/GameNative/gamenative-compat/issues/544) |
| 126 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 20 | 70% (last 20) | Does not open (70%) | 45% | 13d ago | 50% | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |

## Probably does not work (189)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Counter-Strike 2 (STEAM) | 49 | 72 | 68% (since fix) | Does not open (68%) | 56% | 1d ago | 59% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 2 | [ ] | Euro Truck Simulator 2 (STEAM) | 19 | 34 | 56% (14d) | Does not open (65%) | 58% | today | 57% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 3 | [ ] | theHunter Classic (STEAM) | 20 | 20 | 100% (last 20) | No graphics (92%) | n/a | 17d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 4 | [ ] | Metro 2033 Redux (STEAM) | 15 | 27 | 56% (14d) | Does not open (70%) | 40% | today | 39% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 5 | [ ] | Bully: Scholarship Edition (STEAM) | 15 | 23 | 65% (14d) | Does not open (65%) | 41% | 1d ago | 12% (drop) |  |
| 6 | [ ] | Owlboy (STEAM) | 15 | 24 | 63% (14d) | Does not open (80%) | 50% | today | 47% | [#545](https://github.com/GameNative/gamenative-compat/issues/545) |
| 7 | [ ] | To The Moon (GOG) | 18 | 20 | 90% (last 20) | Does not open (86%) | n/a | 18d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 8 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 26 | 46 | 57% (since fix) | Does not open (73%) | 59% | 1d ago | 57% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 9 | [ ] | FINAL FANTASY XIII (STEAM) | 11 | 22 | 50% (14d) | Does not open (71%) | 57% | 1d ago | 59% |  |
| 10 | [ ] | Garry's Mod (STEAM) | 12 | 20 | 60% (since fix) | Does not open (80%) | 54% | today | 43% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 11 | [ ] | Asterigos: Curse of the Stars (STEAM) | 17 | 20 | 85% (last 20) | Graphics glitches (73%) | n/a | 1d ago | n/a |  |
| 12 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 13 | 20 | 65% (last 20) | Does not open (62%) | 45% | 6d ago | 39% |  |
| 13 | [ ] | VRChat (STEAM) | 13 | 20 | 65% (last 20) | Does not open (72%) | 39% | today | 34% |  |
| 14 | [ ] | Darksiders Warmastered Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 58% | 2d ago | 43% |  |
| 15 | [ ] | STAR WARS™ Knights of the Old Republic™ II: The Sith Lords™ (STEAM) | 12 | 20 | 60% (last 20) | No graphics (64%) | 55% | today | 38% |  |
| 16 | [ ] | Door Kickers 2 (STEAM) | 20 | 20 | 100% (last 20) | No graphics (86%) | n/a | 38d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 17 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 41d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 18 | [ ] | Gorilla Tag (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 13% | 6d ago | 8% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 19 | [ ] | Cat Quest (EPIC) | 11 | 20 | 55% (last 20) | Does not open (47%) | 45% | today | 38% |  |
| 20 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (38%) | n/a | today | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 21 | [ ] | DOOM 64 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (60%) | 51% | 2d ago | 35% |  |
| 22 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 13 | 21 | 62% (since fix) | Does not open (78%) | 39% | today | 41% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 23 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 7d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 24 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (51%) | 59% | 7d ago | 38% (drop) | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 25 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 20 | 20 | 100% (last 20) | Controller issues (100%) | n/a | 2d ago | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 26 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 12 | 20 | 60% (last 20) | Does not open (72%) | 36% | today | 39% |  |
| 27 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 25d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 28 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | No graphics (55%) | n/a | 24d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 29 | [ ] | Phasmophobia (STEAM) | 12 | 20 | 60% (last 20) | Does not open (56%) | 56% | today | 47% |  |
| 30 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | No graphics (39%) | 49% | 6d ago | 34% |  |
| 31 | [ ] | Counter-Strike (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 37% | today | 29% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 32 | [ ] | Bad Cheese (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 52% | today | 33% |  |
| 33 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 48% | 5d ago | 38% |  |
| 34 | [ ] | Sonic Adventure™ 2  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (76%) | 47% | 1d ago | 39% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 35 | [ ] | MudRunner (EPIC) | 11 | 20 | 55% (last 20) | Does not open (63%) | 51% | today | 42% |  |
| 36 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 14d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 37 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (58%) | n/a | 5d ago | n/a | [#536](https://github.com/GameNative/gamenative-compat/issues/536) |
| 38 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 12 | 20 | 60% (last 20) | Does not open (86%) | 53% | 1d ago | 25% (drop) | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 39 | [ ] | Metro 2033 Redux (EPIC) | 11 | 20 | 55% (last 20) | Does not open (58%) | 28% | 2d ago | 35% |  |
| 40 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 22d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 41 | [ ] | Hi-Fi RUSH (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 42% | 1d ago | 43% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 42 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (93%) | n/a | 4d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 43 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | n/a | 13d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 44 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | 15% | 4d ago | n/a |  |
| 45 | [ ] | CODE VEIN (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | 35% | 5d ago | 20% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 46 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (85%) | 50% | 11d ago | n/a |  |
| 47 | [ ] | Art of Rally (EPIC) | 10 | 20 | 50% (last 20) | Does not open (72%) | 42% | 1d ago | 39% |  |
| 48 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | n/a | 6d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 49 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 16d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 50 | [ ] | Legacy of Kain: Defiance Remastered (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (69%) | n/a | 1d ago | n/a |  |
| 51 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (66%) | n/a | 19d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 52 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 10d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 53 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | n/a | 40d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 54 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (70%) | n/a | 6d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 55 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | n/a | 2d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 56 | [ ] | Grim Dawn (GOG) | 13 | 20 | 65% (last 20) | Does not open (69%) | n/a | 5d ago | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 57 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 39d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 58 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (93%) | n/a | 3d ago | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 59 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 2d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 60 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | n/a | 18d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 61 | [ ] | Hollow Knight: Silksong (GOG) | 12 | 20 | 60% (last 20) | Does not open (70%) | 50% | 4d ago | 47% |  |
| 62 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 38d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 63 | [ ] | Alpha Protocol (STEAM) | 17 | 20 | 85% (last 20) | No graphics (53%) | n/a | 26d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 64 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (56%) | n/a | 6d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 65 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 44% | 4d ago | 29% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 66 | [ ] | Dead Space 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (66%) | 31% | today | 31% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 67 | [ ] | No More Heroes (STEAM) | 12 | 20 | 60% (last 20) | Does not open (59%) | 44% | today | 36% |  |
| 68 | [ ] | Metro 2033 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (62%) | 33% | today | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 69 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | n/a | 7d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 70 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (56%) | n/a | 7d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 71 | [ ] | DOOM Eternal (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | 1d ago | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 72 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | 22d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 73 | [ ] | HELLDIVERS™ (STEAM) | 12 | 20 | 60% (last 20) | Does not open (58%) | 45% | 2d ago | 52% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 74 | [ ] | METAL SLUG 3 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (78%) | 54% | 8d ago | 67% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 75 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (93%) | n/a | 41d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 76 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 38d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 77 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 38d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 78 | [ ] | Borderlands 2 RU (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | n/a | 4d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 79 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | 3d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 80 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 24d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 81 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 24d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 82 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 55% | 17d ago | n/a |  |
| 83 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 30% | 11d ago | 27% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 84 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (92%) | 38% | 5d ago | n/a |  |
| 85 | [ ] | Euro Truck Simulator (STEAM) | 20 | 20 | 100% (last 20) | Does not open (87%) | n/a | 5d ago | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 86 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 49d ago | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 87 | [ ] | Peggle Nights (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 24d ago | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 88 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 20d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 89 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 7d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 90 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | 3d ago | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 91 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 12d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 92 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 5d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 93 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (54%) | n/a | 26d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 94 | [ ] | A Plague Tale: Innocence (EPIC) | 12 | 20 | 60% (last 20) | Does not open (70%) | 38% | 1d ago | 29% |  |
| 95 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (50%) | n/a | 20d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 96 | [ ] | Beholder (EPIC) | 18 | 20 | 90% (last 20) | No graphics (63%) | n/a | today | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 97 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | n/a | 43d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 98 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | n/a | today | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 99 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (61%) | n/a | 47d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 100 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | n/a | 9d ago | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 101 | [ ] | Breathedge (STEAM) | 10 | 20 | 50% (last 20) | Does not open (54%) | 58% | 1d ago | 67% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 102 | [ ] | Super Meat Boy Forever (EPIC) | 10 | 20 | 50% (last 20) | Does not open (83%) | 42% | 1d ago | 28% |  |
| 103 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 63d ago | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 104 | [ ] | The Survivalists (STEAM) | 18 | 20 | 90% (last 20) | Does not open (96%) | n/a | 8d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 105 | [ ] | Bionic Commando Rearmed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | n/a | 31d ago | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 106 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | n/a | 1d ago | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 107 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | n/a | 4d ago | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 108 | [ ] | Undisputed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | n/a | 13d ago | n/a | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 109 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | n/a | 4d ago | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 110 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 14d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 111 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 16d ago | n/a |  |
| 112 | [ ] | Rise of the Tomb Raider: 20 Year Celebration (EPIC) | 11 | 20 | 55% (last 20) | Does not open (67%) | 44% | 2d ago | 36% |  |
| 113 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 25d ago | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 114 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 12d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 115 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | n/a | 9d ago | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 116 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | n/a | 14d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 117 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (80%) | n/a | 11d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 118 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 9d ago | n/a |  |
| 119 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (94%) | 50% | 2d ago | n/a | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 120 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 11 | 20 | 55% (last 20) | Does not open (90%) | 54% | 2d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 121 | [ ] | CS2D (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | n/a | 2d ago | n/a |  |
| 122 | [ ] | Crysis® (GOG) | 17 | 20 | 85% (last 20) | Does not open (86%) | n/a | 4d ago | n/a |  |
| 123 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 22d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 124 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (36%) | n/a | 19d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 125 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 9d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 126 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 23d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 127 | [ ] | Drop Duchy (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 9% | 2d ago | n/a |  |
| 128 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 16d ago | n/a |  |
| 129 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 16d ago | n/a |  |
| 130 | [ ] | Dying Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (86%) | 56% | 5d ago | 45% |  |
| 131 | [ ] | ENDLESS Space™ 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 36d ago | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 132 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | n/a | 5d ago | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 133 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | No graphics (45%) | n/a | 11d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 134 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | n/a | 1d ago | n/a |  |
| 135 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | n/a | 3d ago | n/a | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 136 | [ ] | Romancing SaGa -Minstrel Song- Remastered (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (100%) | n/a | 5d ago | n/a |  |
| 137 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 13 | 20 | 65% (last 20) | Does not open (55%) | 50% | 5d ago | 30% (drop) | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 138 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | n/a | 9d ago | n/a |  |
| 139 | [ ] | Mortal Shell (EPIC) | 13 | 20 | 65% (last 20) | Does not open (50%) | 31% | 2d ago | 20% |  |
| 140 | [ ] | Mafia II (Classic) (GOG) | 13 | 20 | 65% (last 20) | Does not open (100%) | n/a | 6d ago | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 141 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 48% | 21d ago | 29% |  |
| 142 | [ ] | Fallout Classic (GOG) | 15 | 20 | 75% (last 20) | Does not open (86%) | n/a | 8d ago | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 143 | [ ] | Re-Volt (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (71%) | n/a | 27d ago | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 144 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | 8d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 145 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (69%) | n/a | 16d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 146 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | n/a | 33d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 147 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (86%) | 19% | 2d ago | 21% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 148 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 47% | 7d ago | 30% |  |
| 149 | [ ] | Mafia: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (87%) | 37% | 2d ago | 35% |  |
| 150 | [ ] | Sacred Gold (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | n/a | 2d ago | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 151 | [ ] | Chef Knight (STEAM) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 25d ago | n/a |  |
| 152 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | n/a | 11d ago | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 153 | [ ] | shapez (STEAM) | 14 | 20 | 70% (last 20) | No graphics (73%) | n/a | 1d ago | n/a | [#332](https://github.com/GameNative/gamenative-compat/issues/332) |
| 154 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 42% | 10d ago | 40% |  |
| 155 | [ ] | Songs of Conquest (EPIC) | 13 | 20 | 65% (last 20) | Does not open (75%) | n/a | 5d ago | n/a |  |
| 156 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | n/a | 2d ago | n/a |  |
| 157 | [ ] | Chasm (GOG) | 12 | 20 | 60% (last 20) | No graphics (50%) | n/a | 6d ago | n/a |  |
| 158 | [ ] | Crying Suns (EPIC) | 12 | 20 | 60% (last 20) | No graphics (63%) | n/a | 3d ago | n/a |  |
| 159 | [ ] | DAEMON X MACHINA (EPIC) | 10 | 20 | 50% (last 20) | Does not open (92%) | 47% | 2d ago | 25% (drop) |  |
| 160 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Does not open (40%) | n/a | 12d ago | n/a |  |
| 161 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 10 | 20 | 50% (last 20) | No graphics (57%) | 42% | 5d ago | 62% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 162 | [ ] | Beat Cop (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | n/a | 8d ago | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 163 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | n/a | 43d ago | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 164 | [ ] | FINAL FANTASY VII REMAKE INTERGRADE (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 43% | 6d ago | 43% |  |
| 165 | [ ] | Sandustry (STEAM) | 12 | 20 | 60% (last 20) | Does not open (74%) | n/a | 6d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 166 | [ ] | Allumeria (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | n/a | 2d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 167 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 16d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 168 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 55% | 5d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 169 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 52% | today | 57% |  |
| 170 | [ ] | Assassin's Creed Odyssey (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 50% | 4d ago | 45% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 171 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | n/a | 11d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 172 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 15d ago | n/a |  |
| 173 | [ ] | Minit (EPIC) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 13d ago | n/a |  |
| 174 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 46% | 2d ago | n/a |  |
| 175 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 22d ago | n/a |  |
| 176 | [ ] | LET IT DIE (STEAM) | 11 | 20 | 55% (last 20) | Does not open (94%) | n/a | 3d ago | n/a |  |
| 177 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | n/a | 9d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 178 | [ ] | Styx: Master of Shadows (EPIC) | 10 | 20 | 50% (last 20) | Does not open (73%) | 50% | today | 53% |  |
| 179 | [ ] | HOT WHEELS UNLEASHED™ (EPIC) | 10 | 20 | 50% (last 20) | No graphics (63%) | 47% | 4d ago | 35% |  |
| 180 | [ ] | Veritas Tales: Witch of the Dark Castle (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | n/a | 1d ago | n/a |  |
| 181 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (47%) | n/a | 23d ago | n/a | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 182 | [ ] | Turnip Boy Robs a Bank (EPIC) | 11 | 20 | 55% (last 20) | Does not open (64%) | 38% | 7d ago | n/a | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 183 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 36% | 16d ago | n/a |  |
| 184 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 58% | 8d ago | n/a |  |
| 185 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | n/a | 15d ago | n/a |  |
| 186 | [ ] | Human Resource Machine (EPIC) | 11 | 20 | 55% (last 20) | No graphics (78%) | n/a | today | n/a |  |
| 187 | [ ] | Railway Chai Wala (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | n/a | 6d ago | n/a |  |
| 188 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | n/a | 86d ago | n/a |  |
| 189 | [ ] | Delver (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 21% | today | 0% (drop) |  |

## Fix shipped, waiting for ratings (15)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | L.A. Noire (STEAM) | 2026-11-04 | 4 | 4 | 6d ago | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 2 | Max Payne 3 (STEAM) | 2026-11-04 | 3 | 3 | 4d ago | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 3 | Red Dead Redemption (STEAM) | 2026-11-04 | 2 | 2 | 4d ago | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 4 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 8 | 8 | 1d ago | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 5 | Transistor (STEAM) | 2026-11-10 | 8 | 4 | 1d ago | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 6 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 3 | 3 | 10d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 7 | Peggle Deluxe (STEAM) | 2026-10-29 | 3 | 2 | today | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 8 | Necesse (STEAM) | 2026-10-29 | 6 | 0 | 5d ago | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 9 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 1 | 1 | 10d ago | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 10 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 5 | 5 | today | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 11 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 1 | 1 | 17d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 12 | Need for Speed™ (STEAM) | 2026-11-04 | 0 | 0 | 30d ago | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 13 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 16d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 14 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 0 | 0 | 23d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 15 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 0 | 0 | 17d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |

## Works, but the first launch usually fails (302)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Half-Life (STEAM) | 83 | 114 | 73% (14d) | Does not open (60%) | 69% | today | 67% |  |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 68 | 91 | 75% (14d) | Does not open (63%) | 93% | today | 95% |  |
| 3 | [ ] | Grand Theft Auto V Legacy (STEAM) | 70 | 81 | 86% (since fix) | Does not open (86%) | 74% | today | 71% |  |
| 4 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 52 | 70 | 74% (14d) | Does not open (54%) | 82% | today | 83% |  |
| 5 | [ ] | Portal (STEAM) | 47 | 88 | 53% (14d) | Does not open (41%) | 89% | today | 88% |  |
| 6 | [ ] | Buckshot Roulette (STEAM) | 46 | 63 | 73% (14d) | Does not open (64%) | 60% | today | 43% |  |
| 7 | [ ] | Cyberpunk 2077 (STEAM) | 44 | 75 | 59% (14d) | Does not open (70%) | 71% | 1d ago | 69% |  |
| 8 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 41 | 55 | 75% (14d) | Does not open (60%) | 66% | today | 60% |  |
| 9 | [ ] | MONSTER HUNTER RISE (STEAM) | 40 | 67 | 60% (14d) | Does not open (83%) | 61% | today | 62% |  |
| 10 | [ ] | Terraria (STEAM) | 33 | 66 | 50% (14d) | No graphics (50%) | 73% | today | 72% |  |
| 11 | [ ] | ROB RUN (STEAM) | 33 | 44 | 75% (14d) | Does not open (85%) | 66% | today | 68% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 12 | [ ] | Valheim (STEAM) | 39 | 67 | 58% (since fix) | No graphics (54%) | 83% | today | 84% |  |
| 13 | [ ] | Probably Stolen (STEAM) | 32 | 57 | 56% (14d) | Does not open (64%) | 85% | 1d ago | 80% |  |
| 14 | [ ] | No Man's Sky (STEAM) | 36 | 66 | 55% (since fix) | Controller issues (61%) | 81% | today | 78% |  |
| 15 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 27 | 39 | 69% (14d) | Does not open (76%) | 75% | today | 71% |  |
| 16 | [ ] | Selaco (STEAM) | 26 | 42 | 62% (14d) | Does not open (87%) | 67% | 1d ago | 62% |  |
| 17 | [ ] | Road Rash™: 30th Anniversary Edition (STEAM) | 25 | 49 | 51% (14d) | Does not open (74%) | 65% | today | 69% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 18 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 21 | 22 | 95% (14d) | Controller issues (41%) | 91% | today | 90% |  |
| 19 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 21 | 26 | 81% (14d) | Does not open (77%) | 60% | today | 62% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 20 | [ ] | Red Dead Redemption 2 (STEAM) | 22 | 23 | 96% (since fix) | Does not open (98%) | 83% | today | 86% |  |
| 21 | [ ] | Look Outside (STEAM) | 18 | 31 | 58% (14d) | Controller issues (64%) | 91% | today | 90% |  |
| 22 | [ ] | Dead Space (STEAM) | 18 | 20 | 90% (last 20) | Does not open (54%) | 83% | today | 78% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 23 | [ ] | BeamNG.drive (STEAM) | 17 | 23 | 74% (14d) | Does not open (78%) | 73% | today | 60% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 24 | [ ] | Fallout: New Vegas PCR (STEAM) | 17 | 20 | 85% (14d) | Does not open (93%) | 64% | today | 60% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 25 | [ ] | Library Of Ruina (STEAM) | 17 | 25 | 68% (14d) | Does not open (69%) | 85% | today | 81% |  |
| 26 | [ ] | Noita (STEAM) | 15 | 25 | 60% (14d) | Does not open (56%) | 77% | today | 79% |  |
| 27 | [ ] | Shakedown: Hawaii (STEAM) | 15 | 26 | 58% (14d) | Does not open (79%) | 87% | today | 79% |  |
| 28 | [ ] | Order of the Sinking Star (STEAM) | 15 | 26 | 58% (14d) | Does not open (65%) | 68% | today | 71% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 29 | [ ] | Resident Evil 4 (2005) (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 71% | today | 70% |  |
| 30 | [ ] | Castlevania Anniversary Collection (EPIC) | 19 | 20 | 95% (last 20) | Does not open (80%) | 61% | today | 38% (drop) |  |
| 31 | [ ] | DRAGON BALL FighterZ (STEAM) | 28 | 54 | 52% (since fix) | Does not open (88%) | 86% | today | 89% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 32 | [ ] | Loftia (STEAM) | 15 | 20 | 75% (last 20) | Does not open (94%) | 72% | today | 65% |  |
| 33 | [ ] | Quake (STEAM) | 13 | 23 | 57% (14d) | Does not open (62%) | 71% | 1d ago | 59% |  |
| 34 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (90%) | 90% | today | 90% |  |
| 35 | [ ] | Deadlock (STEAM) | 15 | 20 | 75% (last 20) | Does not open (54%) | 87% | today | 83% |  |
| 36 | [ ] | DOOM 3: BFG Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 71% | 1d ago | 68% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 37 | [ ] | Grand Theft Auto V (EPIC) | 18 | 20 | 90% (last 20) | Does not open (87%) | 76% | today | 73% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 38 | [ ] | Mass Effect™ Legendary Edition (STEAM) | 14 | 26 | 54% (since fix) | Does not open (83%) | 79% | today | 83% |  |
| 39 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (57%) | 74% | today | 65% |  |
| 40 | [ ] | Absolute Drift (EPIC) | 12 | 21 | 57% (14d) | No graphics (54%) | 62% | today | 36% (drop) |  |
| 41 | [ ] | Mortal Kombat X (STEAM) | 13 | 20 | 65% (last 20) | Does not open (72%) | 91% | 3d ago | 92% |  |
| 42 | [ ] | Alabaster Dawn (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (50%) | 88% | 1d ago | 89% |  |
| 43 | [ ] | DOOM (STEAM) | 11 | 22 | 50% (14d) | Does not open (68%) | 86% | 3d ago | 86% |  |
| 44 | [ ] | Resident Evil 7 Biohazard (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 72% | 1d ago | 65% |  |
| 45 | [ ] | Cry of Fear (STEAM) | 14 | 20 | 70% (last 20) | Does not open (47%) | 68% | 1d ago | 71% |  |
| 46 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (70%) | 100% | today | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 47 | [ ] | Dead Island 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (86%) | 62% | today | 45% |  |
| 48 | [ ] | Crypt of the NecroDancer (STEAM) | 10 | 20 | 50% (14d) | Does not open (44%) | 89% | 1d ago | 88% |  |
| 49 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 17 | 20 | 85% (last 20) | Does not open (59%) | 88% | 1d ago | 87% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 50 | [ ] | Batman™: Arkham Origins (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 68% | today | 60% |  |
| 51 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 10 | 16 | 63% (since fix) | Controller issues (83%) | 77% | today | 74% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 52 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 61% | 2d ago | 62% |  |
| 53 | [ ] | Fallout: New Vegas (EPIC) | 16 | 20 | 80% (last 20) | Does not open (59%) | 79% | today | 70% |  |
| 54 | [ ] | Barony (STEAM) | 10 | 20 | 50% (last 20) | Does not open (77%) | 83% | 5d ago | 76% |  |
| 55 | [ ] | OMORI (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 68% | today | 58% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 56 | [ ] | Aniimo (STEAM) | 18 | 20 | 90% (last 20) | Does not open (75%) | 77% | today | 72% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 57 | [ ] | Dressmaker (STEAM) | 11 | 20 | 55% (last 20) | Does not open (57%) | 80% | today | 73% |  |
| 58 | [ ] | Mini Motorways (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 65% | 1d ago | 62% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 59 | [ ] | FINAL FANTASY (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 83% | today | 76% |  |
| 60 | [ ] | Divinity: Original Sin 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (73%) | 82% | 2d ago | 76% |  |
| 61 | [ ] | Disco Elysium - The Final Cut (EPIC) | 11 | 20 | 55% (last 20) | Does not open (75%) | 95% | 1d ago | 94% |  |
| 62 | [ ] | Disgaea 5 Complete (STEAM) | 18 | 20 | 90% (last 20) | Does not open (72%) | 90% | 4d ago | 95% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 63 | [ ] | Castlevania Dominus Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (91%) | 98% | 5d ago | 96% |  |
| 64 | [ ] | Welcome to Elderfield (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 67% | today | 72% |  |
| 65 | [ ] | Cyberpunk 2077 (GOG) | 12 | 20 | 60% (last 20) | Does not open (71%) | 69% | 3d ago | 63% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 66 | [ ] | LEGO® MARVEL Super Heroes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (66%) | 83% | 1d ago | 86% |  |
| 67 | [ ] | PAC-MAN Championship Edition DX+ (STEAM) | 10 | 20 | 50% (last 20) | No graphics (59%) | 70% | today | 57% |  |
| 68 | [ ] | Don't Starve Together (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 73% | today | 66% |  |
| 69 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (61%) | 97% | today | 98% |  |
| 70 | [ ] | TBH: Task Bar Hero (STEAM) | 11 | 20 | 55% (last 20) | Does not open (68%) | 84% | today | 85% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 71 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 64% | today | 66% |  |
| 72 | [ ] | eFootball™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | 64% | 3d ago | 58% |  |
| 73 | [ ] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 76% | 4d ago | 85% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 74 | [ ] | METAL GEAR SOLID 4: Guns of the Patriots - Master Collection Version (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 88% | 1d ago | 92% |  |
| 75 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (52%) | 85% | today | 82% |  |
| 76 | [ ] | Call of Duty 4: Modern Warfare (2007) (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (54%) | 75% | today | 65% |  |
| 77 | [ ] | Poppy Playtime (STEAM) | 13 | 20 | 65% (last 20) | Does not open (59%) | 68% | 6d ago | 61% |  |
| 78 | [ ] | PAYDAY: The Heist (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 73% | today | n/a |  |
| 79 | [ ] | Fable - The Lost Chapters (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (47%) | 80% | 1d ago | 84% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 80 | [ ] | Chained Echoes (GOG) | 14 | 20 | 70% (last 20) | Does not open (60%) | 65% | 2d ago | 57% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 81 | [ ] | Rune Factory 3 Special (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 100% | 1d ago | 100% |  |
| 82 | [ ] | Deskrawl: Idle ARPG (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 64% | 10d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 83 | [ ] | Leaf it Alone (STEAM) | 10 | 20 | 50% (last 20) | Does not open (54%) | 95% | today | 94% |  |
| 84 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 15 | 20 | 75% (last 20) | Does not open (42%) | 71% | 4d ago | 68% |  |
| 85 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 97% | 2d ago | 96% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 86 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 69% | 4d ago | 73% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 87 | [ ] | Happy Wheels (STEAM) | 19 | 20 | 95% (last 20) | No graphics (52%) | 66% | 14d ago | 50% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 88 | [ ] | Fate/stay night REMASTERED (STEAM) | 12 | 20 | 60% (last 20) | No graphics (48%) | 92% | 6d ago | 91% |  |
| 89 | [ ] | Need for Speed™ Rivals (STEAM) | 12 | 20 | 60% (last 20) | Does not open (58%) | 75% | 4d ago | 78% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 90 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (80%) | 65% | today | 47% |  |
| 91 | [ ] | Cave Story+ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | 77% | 3d ago | 73% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 92 | [ ] | Detroit: Become Human (STEAM) | 18 | 20 | 90% (last 20) | Does not open (75%) | 61% | 3d ago | 64% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 93 | [ ] | Dota 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 76% | today | 82% |  |
| 94 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (80%) | 87% | 3d ago | 80% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 95 | [ ] | Palia (STEAM) | 16 | 20 | 80% (last 20) | Does not open (65%) | 74% | 2d ago | 68% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 96 | [ ] | Ratatan (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | 87% | today | 82% |  |
| 97 | [ ] | Mortal Kombat 11 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | 63% | 1d ago | 70% |  |
| 98 | [ ] | Minecraft Dungeons II (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 73% | today | 73% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 99 | [ ] | Sid Meier's Civilization VI (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | 79% | today | 75% |  |
| 100 | [ ] | MIO: Memories in Orbit (STEAM) | 11 | 20 | 55% (last 20) | Graphics glitches (62%) | 93% | 5d ago | 94% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 101 | [ ] | Until Then (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 72% | 2d ago | 57% |  |
| 102 | [ ] | ZERO Sievert (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 84% | today | 81% |  |
| 103 | [ ] | The Sims™ 4 (STEAM) | 6 | 12 | 50% (since fix) | Does not open (85%) | 69% | 3d ago | 70% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 104 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (55%) | 70% | 3d ago | 74% |  |
| 105 | [ ] | Resident Evil Village (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 88% | today | 85% |  |
| 106 | [ ] | Overcooked! 2 (EPIC) | 12 | 20 | 60% (last 20) | Does not open (92%) | 67% | today | 56% |  |
| 107 | [ ] | American Truck Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 76% | 1d ago | 73% |  |
| 108 | [ ] | Minecraft Dungeons (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 77% | today | 79% |  |
| 109 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 89% | 2d ago | 82% |  |
| 110 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 60% | today | 49% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 111 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (42%) | 91% | today | 90% |  |
| 112 | [ ] | Astral Party  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 89% | 1d ago | 86% |  |
| 113 | [ ] | Grand Theft Auto: Vice City (STEAM) | 12 | 20 | 60% (last 20) | Does not open (45%) | 79% | today | 79% |  |
| 114 | [ ] | Abiotic Factor (STEAM) | 10 | 20 | 50% (last 20) | Does not open (74%) | 75% | 4d ago | 81% |  |
| 115 | [ ] | Caravan SandWitch (EPIC) | 10 | 20 | 50% (last 20) | Does not open (75%) | 69% | 1d ago | 68% |  |
| 116 | [ ] | A Plague Tale: Innocence (STEAM) | 19 | 20 | 95% (last 20) | Does not open (87%) | 67% | 5d ago | 68% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 117 | [ ] | Sid Meier's Civilization V (STEAM) | 15 | 20 | 75% (last 20) | Does not open (77%) | 62% | 1d ago | 58% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 118 | [ ] | Tails of Iron (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 89% | 1d ago | 85% |  |
| 119 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 74% | 14d ago | 73% |  |
| 120 | [ ] | Moonstone Island (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (63%) | 74% | 5d ago | 76% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 121 | [ ] | PlateUp! (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 82% | 1d ago | 72% |  |
| 122 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 64% | today | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 123 | [ ] | No, I'm not a Human (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 94% | 3d ago | 88% |  |
| 124 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | 82% | 12d ago | 90% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 125 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | 93% | 7d ago | 91% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 126 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (76%) | 100% | 6d ago | n/a | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 127 | [ ] | Sovereign Tower (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 80% | 1d ago | 79% |  |
| 128 | [ ] | OCTOPATH TRAVELER 0 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (77%) | 93% | today | 95% |  |
| 129 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 81% | 1d ago | 78% |  |
| 130 | [ ] | Stellar Blade™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | 80% | today | 81% |  |
| 131 | [ ] | Oxygen Not Included (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 69% | today | 74% |  |
| 132 | [ ] | Yakuza: Like a Dragon (STEAM) | 13 | 20 | 65% (last 20) | Does not open (58%) | 67% | 2d ago | 79% |  |
| 133 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 11 | 20 | 55% (last 20) | Does not open (68%) | 92% | 1d ago | 91% |  |
| 134 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 88% | 3d ago | 90% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 135 | [ ] | Max Payne (STEAM) | 14 | 20 | 70% (last 20) | No graphics (43%) | 79% | 3d ago | 75% |  |
| 136 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | 60% | 2d ago | 50% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 137 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 94% | 22d ago | 92% |  |
| 138 | [ ] | Call of Duty: World at War (STEAM) | 12 | 20 | 60% (last 20) | Does not open (43%) | 81% | today | 67% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 139 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (50%) | 79% | 6d ago | 75% |  |
| 140 | [ ] | Pinball FX (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 75% | 4d ago | 73% |  |
| 141 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (83%) | 88% | 3d ago | n/a | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 142 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 84% | 1d ago | 86% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 143 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (88%) | 93% | 4d ago | 96% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 144 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 76% | 10d ago | 78% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 145 | [ ] | Sonic Generations (STEAM) | 14 | 20 | 70% (last 20) | Does not open (70%) | 69% | 3d ago | 69% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 146 | [ ] | Tabletop Simulator (STEAM) | 14 | 20 | 70% (last 20) | Does not open (53%) | 82% | 2d ago | 87% |  |
| 147 | [ ] | Street Fighter™ 6 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (81%) | 80% | 2d ago | 79% |  |
| 148 | [ ] | Heavy Rain (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 94% | 6d ago | 94% |  |
| 149 | [ ] | Trailmakers (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | 91% | today | 91% |  |
| 150 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (79%) | 82% | 19d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 151 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (64%) | 77% | 8d ago | 73% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 152 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 85% | 14d ago | 82% |  |
| 153 | [ ] | Plague Inc: Evolved (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 65% | today | 65% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 154 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 82% | 9d ago | 78% |  |
| 155 | [ ] | Stumble Guys (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 69% | today | 62% |  |
| 156 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 80% | 7d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 157 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 86% | today | 85% |  |
| 158 | [ ] | Sonic Lost World (STEAM) | 10 | 20 | 50% (last 20) | No graphics (69%) | 82% | today | 81% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 159 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (62%) | 100% | 1d ago | n/a | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 160 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 63% | 1d ago | 82% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 161 | [ ] | Gambonanza (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 91% | 4d ago | 89% |  |
| 162 | [ ] | Gothic 1 Classic (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 75% | 12d ago | 67% |  |
| 163 | [ ] | Limbus Company (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 86% | 2d ago | 91% |  |
| 164 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 11 | 20 | 55% (last 20) | Does not open (62%) | 78% | 3d ago | 76% |  |
| 165 | [ ] | Fallout (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 71% | 2d ago | 66% |  |
| 166 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (54%) | 72% | 5d ago | 76% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 167 | [ ] | Control Ultimate Edition (GOG) | 13 | 20 | 65% (last 20) | Does not open (76%) | 78% | 10d ago | 72% |  |
| 168 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (82%) | 89% | 2d ago | 88% |  |
| 169 | [ ] | Dishonored 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 69% | 1d ago | 59% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 170 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (55%) | 91% | 16d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 171 | [ ] | Changed (STEAM) | 15 | 20 | 75% (last 20) | Does not open (62%) | 62% | 8d ago | 52% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 172 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 100% | 31d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 173 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 91% | 9d ago | 88% |  |
| 174 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (45%) | 65% | today | 68% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 175 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | 64% | 13d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 176 | [ ] | Digimon Survive (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (77%) | 87% | 2d ago | 84% |  |
| 177 | [ ] | TurretGirls (STEAM) | 12 | 20 | 60% (last 20) | No graphics (77%) | 91% | 1d ago | 94% |  |
| 178 | [ ] | Escape from Duckov (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (72%) | 95% | 2d ago | 98% |  |
| 179 | [ ] | BioShock 2 Remastered (STEAM) | 11 | 20 | 55% (last 20) | Does not open (80%) | 84% | today | 85% |  |
| 180 | [ ] | Counter-Strike:Global Offensive (STEAM) | 10 | 20 | 50% (last 20) | Does not open (76%) | 68% | 5d ago | 62% |  |
| 181 | [ ] | Raft (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | 90% | 5d ago | 87% |  |
| 182 | [ ] | Subnautica 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (52%) | 79% | 3d ago | n/a | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 183 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | 88% | 10d ago | 80% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 184 | [ ] | Capcom Arcade Stadium (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | 74% | 8d ago | 79% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 185 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 92% | 11d ago | n/a |  |
| 186 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (59%) | 73% | today | 68% |  |
| 187 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 13 | 20 | 65% (last 20) | Does not open (85%) | 61% | 1d ago | 57% |  |
| 188 | [ ] | Moonring (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 84% | 1d ago | 79% |  |
| 189 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 67% | 2d ago | 72% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 190 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (71%) | 83% | 3d ago | 80% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 191 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (75%) | 82% | 4d ago | 67% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 192 | [ ] | Supermarket Together (STEAM) | 14 | 20 | 70% (last 20) | Does not open (68%) | 60% | today | 67% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 193 | [ ] | One-armed robber (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (69%) | 66% | today | 52% |  |
| 194 | [ ] | Goat Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 65% | 2d ago | 62% |  |
| 195 | [ ] | Unturned (STEAM) | 11 | 20 | 55% (last 20) | Does not open (40%) | 75% | 3d ago | 78% |  |
| 196 | [ ] | Overwatch® (STEAM) | 7 | 10 | 70% (since fix) | Does not open (61%) | 83% | today | 79% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 197 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 95% | 10d ago | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 198 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (83%) | 62% | today | 53% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 199 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 76% | 15d ago | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 200 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (65%) | 87% | 16d ago | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 201 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 77% | 2d ago | 81% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 202 | [ ] | The Witcher: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (59%) | 70% | 14d ago | 83% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 203 | [ ] | Jade Empire: Special Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 78% | 5d ago | 64% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 204 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (61%) | 62% | 10d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 205 | [ ] | Hotline Miami (GOG) | 14 | 20 | 70% (last 20) | Does not open (89%) | 74% | 3d ago | 81% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 206 | [ ] | Ultimate Custom Night (STEAM) | 14 | 20 | 70% (last 20) | No graphics (72%) | 62% | 1d ago | n/a | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 207 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 13 | 20 | 65% (last 20) | Does not open (77%) | 62% | today | 60% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 208 | [ ] | Darksiders (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 86% | 5d ago | 82% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 209 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (70%) | 96% | today | 100% |  |
| 210 | [ ] | Warframe (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 83% | 4d ago | 80% |  |
| 211 | [ ] | MX Bikes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 93% | 3d ago | 95% |  |
| 212 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 62% | 9d ago | 55% |  |
| 213 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | 75% | 18d ago | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 214 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (91%) | 82% | 34d ago | 73% |  |
| 215 | [ ] | Invisible, Inc. (STEAM) | 15 | 20 | 75% (last 20) | Does not open (63%) | 83% | 22d ago | n/a |  |
| 216 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 77% | 24d ago | 75% |  |
| 217 | [ ] | Return to Monkey Island (STEAM) | 14 | 20 | 70% (last 20) | No graphics (72%) | 70% | 14d ago | 69% |  |
| 218 | [ ] | GOD EATER RESURRECTION (STEAM) | 14 | 20 | 70% (last 20) | Does not open (59%) | 76% | 7d ago | n/a |  |
| 219 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (44%) | 68% | 16d ago | n/a | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 220 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (47%) | 80% | 5d ago | n/a |  |
| 221 | [ ] | Lucid Blocks (STEAM) | 11 | 20 | 55% (last 20) | Does not open (80%) | 65% | 1d ago | 53% |  |
| 222 | [ ] | My Summer Car (STEAM) | 11 | 20 | 55% (last 20) | Does not open (63%) | 83% | 3d ago | 81% |  |
| 223 | [ ] | Resident Evil Revelations 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 83% | today | 80% |  |
| 224 | [ ] | GUILTY GEAR Xrd REV 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (83%) | 71% | 6d ago | 62% |  |
| 225 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 80% | 9d ago | 78% |  |
| 226 | [ ] | Bongo Cat (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 62% | today | 47% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 227 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 93% | 11d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 228 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (83%) | 77% | 4d ago | 75% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 229 | [ ] | Big Walk (STEAM) | 12 | 20 | 60% (last 20) | Does not open (56%) | 67% | 1d ago | 59% |  |
| 230 | [ ] | STORY OF SEASONS: Friends of Mineral Town (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 97% | today | 100% |  |
| 231 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Controller issues (36%) | 91% | 2d ago | n/a |  |
| 232 | [ ] | No Socks RPG (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (91%) | 93% | 1d ago | 92% |  |
| 233 | [ ] | Capcom Fighting Collection (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 91% | 1d ago | 86% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 234 | [ ] | SnowRunner (STEAM) | 12 | 20 | 60% (last 20) | Does not open (96%) | 76% | today | 71% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 235 | [ ] | Deus Ex™ GOTY Edition (GOG) | 12 | 20 | 60% (last 20) | No graphics (47%) | 100% | 21d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 236 | [ ] | Hylics (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (69%) | 97% | 2d ago | 94% |  |
| 237 | [ ] | BATTLETECH (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 95% | 5d ago | 94% |  |
| 238 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (50%) | 76% | today | 85% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 239 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 11 | 20 | 55% (last 20) | Does not open (53%) | 71% | 4d ago | 75% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 240 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 94% | 6d ago | 100% |  |
| 241 | [ ] | Secrets of Grindea (STEAM) | 10 | 20 | 50% (last 20) | Does not open (48%) | 75% | 3d ago | 80% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 242 | [ ] | Zero Escape: The Nonary Games (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 70% | today | 68% |  |
| 243 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 83% | today | 76% |  |
| 244 | [ ] | Revolution Idle (STEAM) | 10 | 20 | 50% (last 20) | Does not open (43%) | 83% | 4d ago | n/a |  |
| 245 | [ ] | Tales of Zestiria (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 67% | 26d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 246 | [ ] | Spark the Electric Jester (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 69% | today | n/a | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 247 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (95%) | 91% | 12d ago | 90% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 248 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (84%) | 70% | 1d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 249 | [ ] | AER Memories of Old (EPIC) | 13 | 20 | 65% (last 20) | Does not open (86%) | 94% | 5d ago | 92% |  |
| 250 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (71%) | 76% | 6d ago | 73% |  |
| 251 | [ ] | Timberborn (STEAM) | 12 | 20 | 60% (last 20) | No graphics (68%) | 94% | 2d ago | 100% |  |
| 252 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 100% | 13d ago | n/a |  |
| 253 | [ ] | 12 is Better Than 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 75% | 16d ago | n/a |  |
| 254 | [ ] | Cat Mail Co. (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 87% | today | 87% |  |
| 255 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (78%) | 95% | 4d ago | 92% |  |
| 256 | [ ] | Hero Siege (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (46%) | 86% | 5d ago | 91% |  |
| 257 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 87% | 7d ago | 82% |  |
| 258 | [ ] | Rollout Inline (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 62% | 1d ago | 82% |  |
| 259 | [ ] | HITMAN World of Assassination (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 76% | today | 75% |  |
| 260 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 14 | 20 | 70% (last 20) | Does not open (86%) | 75% | today | 90% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 261 | [ ] | Disgaea 4 Complete+ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (43%) | 93% | 6d ago | 92% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 262 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 69% | 11d ago | 70% |  |
| 263 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 92% | 32d ago | 92% |  |
| 264 | [ ] | Goose Goose Duck (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 74% | 1d ago | 79% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 265 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 12 | 20 | 60% (last 20) | No graphics (39%) | 88% | 4d ago | 90% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 266 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 67% | 8d ago | 60% |  |
| 267 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 62% | 12d ago | 62% |  |
| 268 | [ ] | Sons Of The Forest (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 74% | 6d ago | 71% |  |
| 269 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 62% | 15d ago | 62% |  |
| 270 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 77% | 3d ago | 83% |  |
| 271 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 93% | 9d ago | 90% |  |
| 272 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 69% | 5d ago | 82% |  |
| 273 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 86% | 11d ago | 86% |  |
| 274 | [ ] | Super Battle Golf (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 88% | 2d ago | 83% |  |
| 275 | [ ] | CRUEL (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 82% | 6d ago | 80% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 276 | [ ] | Hitman: Absolution (GOG) | 10 | 20 | 50% (last 20) | Does not open (83%) | 80% | 3d ago | n/a |  |
| 277 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 95% | 6d ago | 100% |  |
| 278 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 93% | 3d ago | 93% |  |
| 279 | [ ] | Sort Them Ducks (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (58%) | 100% | today | 100% |  |
| 280 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (92%) | 86% | 16d ago | 91% |  |
| 281 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (63%) | 64% | 9d ago | n/a |  |
| 282 | [ ] | Forgive Me Father (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 75% | 7d ago | 64% |  |
| 283 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 85% | 6d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 284 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 69% | 2d ago | 71% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 285 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 77% | 5d ago | 73% |  |
| 286 | [ ] | Subnautica: Below Zero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 84% | 1d ago | 72% |  |
| 287 | [ ] | A Plague Tale: Innocence (GOG) | 10 | 20 | 50% (last 20) | Does not open (91%) | 60% | 3d ago | n/a |  |
| 288 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 62% | 4d ago | 70% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 289 | [ ] | BioShock 2 Remastered (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 90% | 1d ago | 87% |  |
| 290 | [ ] | Intravenous (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 81% | 12d ago | 81% |  |
| 291 | [ ] | Decktamer (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 75% | 1d ago | n/a |  |
| 292 | [ ] | The Stanley Parable (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 78% | 1d ago | 77% |  |
| 293 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 71% | 14d ago | 70% |  |
| 294 | [ ] | Command & Conquer™ Red Alert™ 3 (STEAM) | 11 | 20 | 55% (last 20) | No graphics (38%) | 87% | today | 90% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 295 | [ ] | Dungeon Siege (STEAM) | 10 | 20 | 50% (last 20) | Does not open (44%) | 93% | today | 100% |  |
| 296 | [ ] | Cruelty Squad (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 86% | 4d ago | 81% |  |
| 297 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 93% | today | 95% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 298 | [ ] | Haydee (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 79% | 6d ago | n/a |  |
| 299 | [ ] | Pillars of Eternity (STEAM) | 10 | 20 | 50% (last 20) | Does not open (40%) | 100% | today | 100% |  |
| 300 | [ ] | Legend of Grimrock 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 92% | 4d ago | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 301 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 100% | 6d ago | 100% |  |
| 302 | [ ] | Helping the Hotties (GOG) | 10 | 20 | 50% (last 20) | Does not open (75%) | 73% | 2d ago | n/a |  |

## Recently recovered (376)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Grim Dawn (STEAM) | 481 | 2026-11-08 | 561 | 67% |  |
| 2 | [x] | FINAL FANTASY RESONANCE (STEAM) | 453 | 2026-10-24 | 1034 | 81% |  |
| 3 | [x] | Half-Life (STEAM) | 375 | 2026-11-09 | 642 | 69% |  |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 265 | 2026-11-14 | 420 | 68% |  |
| 5 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 238 | 2026-11-09 | 332 | 88% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 6 | [x] | Alan Wake (STEAM) | 235 | 2026-11-14 | 260 | 65% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 7 | [x] | MONSTER HUNTER RISE (STEAM) | 227 | 2026-11-17 | 532 | 61% |  |
| 8 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 220 | 2026-11-09 | 376 | 66% |  |
| 9 | [x] | BeamNG.drive (STEAM) | 194 | 2026-11-09 | 239 | 73% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 10 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 191 | 2026-11-09 | 232 | 56% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 11 | [x] | Call of Duty: Black Ops (STEAM) | 184 | 2026-11-13 | 210 | 21% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 12 | [x] | OMORI (STEAM) | 179 | 2026-11-09 | 225 | 68% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 13 | [x] | DRAGON BALL FighterZ (STEAM) | 170 | 2026-11-01 | 216 | 86% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 14 | [x] | Spelunky 2 (STEAM) | 160 | 2026-11-01 | 202 | 79% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 15 | [x] | Geometry Dash (STEAM) | 157 | 2026-11-11 | 447 | 58% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 16 | [x] | BioShock (STEAM) | 151 | 2026-11-09 | 300 | 70% |  |
| 17 | [x] | Sid Meier's Civilization V (STEAM) | 148 | 2026-11-10 | 160 | 62% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 18 | [x] | Prototype (STEAM) | 140 | 2026-11-11 | 206 | 63% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 19 | [x] | Team Fortress 2 (STEAM) | 134 | 2026-11-09 | 237 | 77% |  |
| 20 | [x] | Minecraft Dungeons II (STEAM) | 132 | 2026-11-09 | 151 | 73% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 21 | [x] | Castlevania Advance Collection (STEAM) | 129 | 2026-11-09 | 202 | 87% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 22 | [x] | Far Cry® 3 (STEAM) | 119 | 2026-11-20 | 133 | 60% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 23 | [x] | Mirror's Edge (STEAM) | 117 | 2026-11-09 | 171 | 68% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 24 | [x] | Aniimo (STEAM) | 116 | 2026-11-09 | 155 | 77% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 25 | [x] | Assassin's Creed II (STEAM) | 113 | 2026-11-10 | 118 | 69% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 26 | [x] | Cave Story+ (STEAM) | 102 | 2026-11-09 | 112 | 77% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 27 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 101 | 2026-11-09 | 142 | 96% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 28 | [x] | The Witcher: Enhanced Edition (STEAM) | 101 | 2026-11-09 | 119 | 70% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 29 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 98 | 2026-11-15 | 141 | 72% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 30 | [x] | Happy Wheels (STEAM) | 97 | 2026-11-09 | 117 | 66% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 31 | [x] | Moonstone Island (STEAM) | 94 | 2026-11-09 | 123 | 74% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 32 | [x] | Catherine Classic (STEAM) | 88 | 2026-11-09 | 167 | 51% |  |
| 33 | [x] | Fallout: New Vegas PCR (STEAM) | 85 | 2026-11-20 | 113 | 64% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 34 | [x] | FINAL FANTASY XIII-2 (STEAM) | 81 | 2026-11-09 | 84 | 63% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 35 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 80 | 2026-11-09 | 131 | 72% |  |
| 36 | [x] | DOOM 3: BFG Edition (STEAM) | 80 | 2026-11-09 | 122 | 71% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 37 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 78 | 2026-11-09 | 103 | 93% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 38 | [x] | Vital Shell (STEAM) | 77 | 2026-11-09 | 126 | 83% |  |
| 39 | [x] | Psychonauts (STEAM) | 76 | 2026-11-09 | 141 | 94% |  |
| 40 | [x] | Quake (STEAM) | 75 | 2026-11-09 | 234 | 71% |  |
| 41 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 75 | 2026-11-19 | 96 | 60% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 42 | [x] | Ballionaire (STEAM) | 74 | 2026-11-09 | 126 | 82% |  |
| 43 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 74 | 2026-11-09 | 115 | 79% |  |
| 44 | [x] | Brawlhalla (STEAM) | 73 | 2026-11-09 | 143 | 73% |  |
| 45 | [x] | Age of Empires II: Definitive Edition (STEAM) | 73 | 2026-11-10 | 92 | 64% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 46 | [x] | The Sims™ 4 (STEAM) | 70 | 2026-11-09 | 95 | 69% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 47 | [x] | Cyberpunk 2077 (GOG) | 70 | 2026-11-09 | 92 | 69% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 48 | [x] | Order of the Sinking Star (STEAM) | 69 | 2026-11-09 | 104 | 68% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 49 | [x] | STEINS;GATE (STEAM) | 69 | 2026-11-09 | 101 | 85% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 50 | [x] | Fable - The Lost Chapters (STEAM) | 67 | 2026-11-09 | 108 | 80% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 51 | [x] | Dota 2 (STEAM) | 66 | 2026-11-09 | 101 | 76% |  |
| 52 | [x] | Disgaea 5 Complete (STEAM) | 66 | 2026-11-09 | 78 | 90% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 53 | [x] | Detroit: Become Human (STEAM) | 66 | 2026-11-20 | 70 | 61% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 54 | [x] | Stardew Valley (GOG) | 65 | 2026-11-11 | 114 | 78% |  |
| 55 | [x] | Need for Speed: Hot Pursuit (STEAM) | 64 | 2026-11-09 | 99 | 76% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 56 | [x] | GRID (STEAM) | 64 | 2026-11-21 | 83 | 45% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 57 | [x] | Sovereign Tower (STEAM) | 63 | 2026-11-09 | 117 | 80% |  |
| 58 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 63 | 2026-11-09 | 102 | 84% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 59 | [x] | Diablo® IV (STEAM) | 63 | 2026-11-11 | 75 | 82% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 60 | [x] | American Truck Simulator (STEAM) | 62 | 2026-11-09 | 104 | 76% |  |
| 61 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 62 | 2026-11-11 | 82 | 57% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 62 | [x] | Spyro™ Reignited Trilogy (STEAM) | 61 | 2026-11-09 | 105 | 79% |  |
| 63 | [x] | Poppy Playtime (STEAM) | 61 | 2026-11-09 | 103 | 68% |  |
| 64 | [x] | Caravan SandWitch (EPIC) | 60 | 2026-11-09 | 122 | 69% |  |
| 65 | [x] | Mini Motorways (STEAM) | 60 | 2026-11-09 | 95 | 65% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 66 | [x] | Gunfire Reborn (STEAM) | 60 | 2026-11-09 | 66 | 88% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 67 | [x] | Borderlands 3 (STEAM) | 59 | 2026-11-09 | 87 | 90% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 68 | [x] | Fallout (STEAM) | 58 | 2026-11-09 | 93 | 71% |  |
| 69 | [x] | Deskrawl: Idle ARPG (STEAM) | 58 | 2026-11-09 | 72 | 64% | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 70 | [x] | Grand Theft Auto V (EPIC) | 58 | 2026-11-09 | 65 | 76% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 71 | [x] | Firewatch (STEAM) | 57 | 2026-11-10 | 111 | 83% |  |
| 72 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 56 | 2026-10-25 | 97 | 76% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 73 | [x] | eFootball™ (STEAM) | 56 | 2026-11-09 | 82 | 64% |  |
| 74 | [x] | Call of Juarez Gunslinger (STEAM) | 56 | 2026-11-09 | 71 | 76% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 75 | [x] | A Plague Tale: Innocence (STEAM) | 56 | 2026-11-09 | 59 | 67% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 76 | [x] | Call of Duty: World at War (STEAM) | 55 | 2026-11-09 | 80 | 81% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 77 | [x] | Darksiders (STEAM) | 54 | 2026-11-09 | 69 | 86% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 78 | [x] | Sonic Generations (STEAM) | 54 | 2026-11-09 | 61 | 69% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 79 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 53 | 2026-11-17 | 78 | 65% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 80 | [x] | Starbound (STEAM) | 52 | 2026-11-09 | 86 | 83% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 81 | [x] | MIO: Memories in Orbit (STEAM) | 51 | 2026-11-09 | 104 | 93% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 82 | [x] | Borderlands: The Pre-Sequel (STEAM) | 51 | 2026-11-09 | 89 | 63% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 83 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 50 | 2026-11-09 | 86 | 74% |  |
| 84 | [x] | Sol Cesto (EPIC) | 50 | 2026-11-09 | 51 | 87% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 85 | [x] | Okami HD (STEAM) | 49 | 2026-11-09 | 91 | 92% |  |
| 86 | [x] | Last Epoch (STEAM) | 49 | 2026-11-09 | 74 | 63% |  |
| 87 | [x] | Moonlighter (EPIC) | 49 | 2026-11-09 | 53 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 88 | [x] | Castlevania Anniversary Collection (EPIC) | 48 | 2026-11-21 | 110 | 61% |  |
| 89 | [x] | TBH: Task Bar Hero (STEAM) | 48 | 2026-11-09 | 78 | 84% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 90 | [x] | Heroes of Might & Magic III - HD Edition (STEAM) | 48 | 2026-11-14 | 63 | 60% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 91 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 47 | 2026-11-09 | 81 | 63% |  |
| 92 | [x] | Oxygen Not Included (STEAM) | 47 | 2026-11-11 | 81 | 69% |  |
| 93 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 47 | 2026-11-09 | 54 | 100% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 94 | [x] | Overwatch® (STEAM) | 47 | 2026-11-10 | 52 | 83% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 95 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 46 | 2026-11-09 | 78 | 85% |  |
| 96 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 45 | 2026-11-09 | 75 | 82% |  |
| 97 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 45 | 2026-11-13 | 74 | 65% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 98 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 45 | 2026-11-09 | 69 | 91% |  |
| 99 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 43 | 2026-11-09 | 73 | 58% |  |
| 100 | [x] | Plague Inc: Evolved (STEAM) | 42 | 2026-11-16 | 64 | 65% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 101 | [x] | MudRunner (STEAM) | 41 | 2026-10-24 | 95 | 59% |  |
| 102 | [x] | Darkest Dungeon® (EPIC) | 41 | 2026-11-09 | 82 | 84% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 103 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 41 | 2026-11-09 | 57 | 77% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 104 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 40 | 2026-11-09 | 73 | 92% |  |
| 105 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 39 | 2026-11-09 | 62 | 66% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 106 | [x] | Dead by Daylight (STEAM) | 39 | 2026-11-09 | 43 | 84% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 107 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 38 | 2026-11-09 | 71 | 89% |  |
| 108 | [x] | Tomb Raider: Anniversary (STEAM) | 38 | 2026-11-09 | 63 | 56% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 109 | [x] | Sonic Lost World (STEAM) | 38 | 2026-11-09 | 59 | 82% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 110 | [x] | Aggelos (STEAM) | 38 | 2026-11-09 | 54 | 88% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 111 | [x] | Age of Empires II (2013) (STEAM) | 37 | 2026-11-09 | 62 | 70% |  |
| 112 | [x] | Street Fighter™ 6 (STEAM) | 37 | 2026-11-09 | 58 | 80% |  |
| 113 | [x] | FINAL FANTASY VII (2013) (STEAM) | 37 | 2026-11-09 | 54 | 59% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 114 | [x] | Monster Hunter Wilds (STEAM) | 37 | 2026-11-09 | 38 | 77% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 115 | [x] | Amnesia: The Dark Descent (STEAM) | 36 | 2026-11-09 | 75 | 85% |  |
| 116 | [x] | Digimon World: Next Order (STEAM) | 36 | 2026-11-09 | 73 | 84% |  |
| 117 | [x] | Sonic Origins (STEAM) | 36 | 2026-11-09 | 66 | 82% |  |
| 118 | [x] | XCOM 2 (STEAM) | 36 | 2026-11-09 | 62 | 72% |  |
| 119 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 36 | 2026-11-19 | 38 | 93% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 120 | [x] | POSTAL 2 (GOG) | 35 | 2026-11-09 | 66 | 95% |  |
| 121 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 35 | 2026-11-09 | 66 | 85% |  |
| 122 | [x] | Ace Attorney Investigations Collection (STEAM) | 35 | 2026-11-09 | 63 | 87% |  |
| 123 | [x] | Capcom Arcade Stadium (STEAM) | 35 | 2026-11-09 | 45 | 74% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 124 | [x] | Russian Fishing 4 (STEAM) | 35 | 2026-11-09 | 41 | 82% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 125 | [x] | CrossCode (GOG) | 35 | 2026-11-09 | 38 | 82% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 126 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 34 | 2026-11-09 | 61 | 78% |  |
| 127 | [x] | Gauntlet™  (STEAM) | 34 | 2026-11-11 | 50 | 73% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 128 | [x] | Asphalt Legends  (STEAM) | 34 | 2026-11-21 | 38 | 62% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 129 | [x] | Being a DIK (STEAM) | 33 | 2026-11-09 | 73 | 65% |  |
| 130 | [x] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 33 | 2026-11-20 | 60 | 15% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 131 | [x] | SnowRunner (STEAM) | 33 | 2026-11-09 | 46 | 76% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 132 | [x] | ROB RUN (STEAM) | 33 | 2026-11-17 | 45 | 66% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 133 | [x] | Elite Dangerous (STEAM) | 33 | 2026-11-20 | 36 | 64% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 134 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 32 | 2026-11-09 | 69 | 73% |  |
| 135 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 32 | 2026-11-09 | 56 | 71% |  |
| 136 | [x] | Max Payne (STEAM) | 32 | 2026-11-09 | 54 | 79% |  |
| 137 | [x] | Need for Speed™ Rivals (STEAM) | 32 | 2026-11-10 | 44 | 75% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 138 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-11-09 | 40 | 100% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 139 | [x] | Journey (STEAM) | 31 | 2026-10-27 | 71 | 67% |  |
| 140 | [x] | COCOON (STEAM) | 31 | 2026-11-09 | 66 | 81% |  |
| 141 | [x] | Hearts of Iron IV (STEAM) | 31 | 2026-11-09 | 64 | 82% |  |
| 142 | [x] | The Bazaar (STEAM) | 31 | 2026-11-09 | 61 | 78% |  |
| 143 | [x] | Yume Nikki (STEAM) | 31 | 2026-11-20 | 54 | 42% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 144 | [x] | Earthion (STEAM) | 31 | 2026-11-09 | 53 | 100% |  |
| 145 | [x] | Big Walk (STEAM) | 31 | 2026-11-09 | 52 | 67% |  |
| 146 | [x] | Red Dead Redemption (STEAM) | 31 | 2026-11-09 | 34 | 50% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 147 | [x] | Hero Siege (STEAM) | 30 | 2026-11-09 | 52 | 86% |  |
| 148 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 30 | 2026-11-09 | 51 | 95% |  |
| 149 | [x] | Prince of Persia: The Sands of Time (STEAM) | 30 | 2026-11-09 | 50 | 79% |  |
| 150 | [x] | Counter-Strike:Global Offensive (STEAM) | 30 | 2026-11-09 | 46 | 68% |  |
| 151 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 29 | 2026-11-09 | 52 | 89% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 152 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 29 | 2026-11-09 | 50 | 73% |  |
| 153 | [x] | Resident Evil Village (STEAM) | 29 | 2026-11-09 | 49 | 88% |  |
| 154 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 29 | 2026-11-09 | 45 | 81% |  |
| 155 | [x] | Gothic II: Gold Classic (STEAM) | 29 | 2026-11-09 | 37 | 67% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 156 | [x] | Hotline Miami (GOG) | 29 | 2026-11-18 | 36 | 74% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 157 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 72% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 158 | [x] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 29 | 2026-11-14 | 34 | 80% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 159 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 28 | 2026-11-09 | 61 | 86% |  |
| 160 | [x] | SurrounDead (STEAM) | 28 | 2026-11-09 | 59 | 90% |  |
| 161 | [x] | Resident Evil Revelations 2 (STEAM) | 28 | 2026-11-09 | 54 | 83% |  |
| 162 | [x] | Secrets of Grindea (STEAM) | 28 | 2026-11-09 | 48 | 75% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 163 | [x] | Heavy Rain (STEAM) | 28 | 2026-11-09 | 47 | 94% |  |
| 164 | [x] | Supermarket Together (STEAM) | 28 | 2026-11-18 | 41 | 60% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 165 | [x] | Gambonanza (STEAM) | 27 | 2026-11-09 | 45 | 91% |  |
| 166 | [x] | Tower and Sword of Succubus (STEAM) | 27 | 2026-11-09 | 42 | 82% |  |
| 167 | [x] | Digimon Survive (STEAM) | 27 | 2026-11-09 | 39 | 87% |  |
| 168 | [x] | Palia (STEAM) | 27 | 2026-11-09 | 39 | 74% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 169 | [x] | Skullgirls 2nd Encore (STEAM) | 26 | 2026-11-10 | 63 | 68% |  |
| 170 | [x] | Deponia (STEAM) | 26 | 2026-11-09 | 50 | 76% |  |
| 171 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 26 | 2026-11-09 | 48 | 96% |  |
| 172 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 45 | 70% |  |
| 173 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 26 | 2026-11-09 | 43 | 68% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 174 | [x] | Dead Rising 2 (STEAM) | 26 | 2026-11-09 | 42 | 74% |  |
| 175 | [x] | Yakuza: Like a Dragon (STEAM) | 26 | 2026-11-09 | 42 | 67% |  |
| 176 | [x] | Cat Mail Co. (STEAM) | 25 | 2026-11-09 | 42 | 87% |  |
| 177 | [x] | Guildrun Demo (STEAM) | 25 | 2026-11-09 | 42 | 85% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 178 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-19 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 179 | [x] | Subnautica 2 (STEAM) | 25 | 2026-11-15 | 30 | 79% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 180 | [x] | Slow Roads (STEAM) | 24 | 2026-10-22 | 51 | 59% |  |
| 181 | [x] | Frostpunk (STEAM) | 24 | 2026-11-09 | 50 | 74% |  |
| 182 | [x] | Mirror's Edge™ (GOG) | 24 | 2026-11-13 | 46 | 77% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 183 | [x] | Lucid Blocks (STEAM) | 24 | 2026-11-09 | 46 | 65% |  |
| 184 | [x] | Battle Brothers (STEAM) | 24 | 2026-11-09 | 44 | 78% |  |
| 185 | [x] | Trailmakers (STEAM) | 24 | 2026-11-09 | 43 | 91% |  |
| 186 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 24 | 2026-11-09 | 38 | 77% |  |
| 187 | [x] | Opus Magnum (STEAM) | 24 | 2026-11-09 | 38 | 92% |  |
| 188 | [x] | Ratatan (STEAM) | 24 | 2026-11-09 | 38 | 87% |  |
| 189 | [x] | Limbus Company (STEAM) | 24 | 2026-11-09 | 37 | 86% |  |
| 190 | [x] | Timberborn (STEAM) | 24 | 2026-11-09 | 35 | 94% |  |
| 191 | [x] | Chained Echoes (GOG) | 23 | 2026-11-19 | 51 | 65% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 192 | [x] | Goat Simulator (STEAM) | 23 | 2026-11-09 | 48 | 65% |  |
| 193 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-11-09 | 46 | 90% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 194 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 23 | 2026-11-09 | 45 | 62% |  |
| 195 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 45 | 91% |  |
| 196 | [x] | Dishonored 2 (STEAM) | 23 | 2026-11-09 | 34 | 69% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 197 | [x] | Jade Empire: Special Edition (GOG) | 23 | 2026-11-09 | 30 | 68% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 198 | [x] | Crab Game (STEAM) | 23 | 2026-11-09 | 27 | 88% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 199 | [x] | Football Manager 2024 (EPIC) | 22 | 2026-11-09 | 40 | 65% |  |
| 200 | [x] | Capcom Fighting Collection 2 (STEAM) | 22 | 2026-11-09 | 39 | 84% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 201 | [x] | Strider (STEAM) | 22 | 2026-11-20 | 39 | 69% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 202 | [x] | My Summer Car (STEAM) | 22 | 2026-11-09 | 37 | 83% |  |
| 203 | [x] | Sorry We're Closed (EPIC) | 22 | 2026-11-09 | 36 | 65% |  |
| 204 | [x] | Tabletop Simulator (STEAM) | 22 | 2026-11-09 | 36 | 82% |  |
| 205 | [x] | Mortal Kombat 11 (STEAM) | 22 | 2026-11-09 | 33 | 63% |  |
| 206 | [x] | Changed (STEAM) | 22 | 2026-11-18 | 32 | 62% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 207 | [x] | Ultimate Custom Night (STEAM) | 22 | 2026-11-19 | 32 | 62% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 208 | [x] | FINAL FANTASY XIV Online (STEAM) | 22 | 2026-10-22 | 29 | 91% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 209 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 22 | 2026-11-09 | 29 | 62% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 210 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 22 | 2026-11-09 | 26 | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 211 | [x] | Jade Empire: Special Edition (STEAM) | 22 | 2026-11-09 | 25 | 78% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 212 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 61 | 97% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 213 | [x] | Prince of Persia (GOG) | 21 | 2026-11-09 | 42 | 76% |  |
| 214 | [x] | Crazy Taxi (STEAM) | 21 | 2026-11-10 | 42 | 64% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 215 | [x] | Control Ultimate Edition (GOG) | 21 | 2026-11-09 | 39 | 78% |  |
| 216 | [x] | Unturned (STEAM) | 21 | 2026-11-09 | 39 | 75% |  |
| 217 | [x] | Invisible, Inc. (STEAM) | 21 | 2026-11-09 | 37 | 83% |  |
| 218 | [x] | Deus Ex™ GOTY Edition (GOG) | 21 | 2026-11-09 | 34 | 100% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 219 | [x] | Goose Goose Duck (STEAM) | 21 | 2026-11-18 | 32 | 74% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 220 | [x] | CRUEL (STEAM) | 21 | 2026-11-09 | 31 | 82% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 221 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 91% |  |
| 222 | [x] | Sapphire Safari (GOG) | 21 | 2026-11-20 | 28 | 70% | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 223 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 21 | 2026-11-09 | 27 | 91% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 224 | [x] | CarX Street (STEAM) | 21 | 2026-11-09 | 26 | 76% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 225 | [x] | Dead Island (STEAM) | 21 | 2026-11-09 | 26 | 83% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 226 | [x] | Tearscape (STEAM) | 21 | 2026-11-09 | 25 | 87% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 227 | [x] | Wizard of Legend (EPIC) | 20 | 2026-11-09 | 39 | 77% |  |
| 228 | [x] | Worms W.M.D (STEAM) | 20 | 2026-11-09 | 38 | 97% |  |
| 229 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-11-09 | 36 | 86% |  |
| 230 | [x] | Return to Monkey Island (STEAM) | 20 | 2026-11-09 | 33 | 70% |  |
| 231 | [x] | Torchlight II (EPIC) | 20 | 2026-11-09 | 28 | 77% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 232 | [x] | Tyr (STEAM) | 20 | 2026-11-09 | 28 | 64% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 233 | [x] | Counter-Strike: Condition Zero (STEAM) | 19 | 2026-11-11 | 38 | 29% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 234 | [x] | Pinball FX Classic (STEAM) | 19 | 2026-11-09 | 37 | 87% |  |
| 235 | [x] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 2026-11-15 | 36 | 71% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 236 | [x] | SWORN (STEAM) | 19 | 2026-11-09 | 34 | 94% |  |
| 237 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 32 | 73% |  |
| 238 | [x] | Moonlight Peaks (STEAM) | 19 | 2026-11-09 | 32 | 72% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 239 | [x] | GOD EATER RESURRECTION (STEAM) | 19 | 2026-11-09 | 30 | 76% |  |
| 240 | [x] | Dark Sector (STEAM) | 19 | 2026-11-21 | 25 | 62% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 241 | [x] | Backpack Battles (STEAM) | 18 | 2026-11-09 | 42 | 93% |  |
| 242 | [x] | Mini Metro (STEAM) | 18 | 2026-11-16 | 37 | 62% |  |
| 243 | [x] | One-armed robber (STEAM) | 18 | 2026-11-09 | 33 | 66% |  |
| 244 | [x] | This War of Mine (STEAM) | 18 | 2026-11-17 | 33 | 44% |  |
| 245 | [x] | Far Far West (STEAM) | 18 | 2026-11-09 | 32 | 54% |  |
| 246 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 2026-11-09 | 29 | 88% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 247 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 18 | 2026-11-09 | 28 | 93% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 248 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-11-09 | 27 | 85% |  |
| 249 | [x] | Bongo Cat (STEAM) | 18 | 2026-11-20 | 25 | 62% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 250 | [x] | Tales of Zestiria (STEAM) | 18 | 2026-11-09 | 24 | 67% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 251 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-18 | 23 | 75% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 252 | [x] | Mafia II: Definitive Edition (GOG) | 18 | 2026-11-15 | 20 | 60% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 253 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 17 | 2026-10-25 | 43 | 72% |  |
| 254 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 37 | 33% |  |
| 255 | [x] | Intravenous 2 (STEAM) | 17 | 2026-11-09 | 33 | 96% |  |
| 256 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 33 | 86% |  |
| 257 | [x] | Capcom Fighting Collection (STEAM) | 17 | 2026-11-09 | 25 | 91% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 258 | [x] | Party Animals (STEAM) | 17 | 2026-11-09 | 25 | 77% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 259 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 16 | 2026-11-11 | 35 | 74% |  |
| 260 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 261 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 16 | 2026-11-09 | 30 | 72% |  |
| 262 | [x] | PAYDAY: The Heist (STEAM) | 16 | 2026-11-13 | 28 | 73% |  |
| 263 | [x] | Legend of Grimrock 2 (STEAM) | 16 | 2026-11-09 | 26 | 92% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 264 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 67% |  |
| 265 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 16 | 2026-11-09 | 22 | 75% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 266 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 267 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 268 | [x] | sobosuba (STEAM) | 15 | 2026-11-09 | 34 | 85% |  |
| 269 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 30 | 96% |  |
| 270 | [x] | Tiny Glade (STEAM) | 15 | 2026-11-09 | 30 | 71% |  |
| 271 | [x] | Titanfall® 2 (STEAM) | 15 | 2026-11-09 | 29 | 70% |  |
| 272 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 15 | 2026-11-20 | 29 | 80% |  |
| 273 | [x] | AER Memories of Old (EPIC) | 15 | 2026-11-09 | 25 | 94% |  |
| 274 | [x] | Alabaster Dawn Demo (STEAM) | 15 | 2026-11-09 | 23 | 76% |  |
| 275 | [x] | Need for Speed™ Unbound (STEAM) | 15 | 2026-11-09 | 23 | 58% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 276 | [x] | Nex Machina (STEAM) | 15 | 2026-11-09 | 23 | 76% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 277 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 93% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 278 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 279 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 280 | [x] | Mark of the Ninja (STEAM) | 14 | 2026-10-26 | 32 | 94% |  |
| 281 | [x] | Faster Than Light (EPIC) | 14 | 2026-11-09 | 31 | 91% |  |
| 282 | [x] | Flotsam (EPIC) | 14 | 2026-11-20 | 30 | 42% |  |
| 283 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 94% |  |
| 284 | [x] | Hitman: Absolution (GOG) | 14 | 2026-11-09 | 29 | 80% |  |
| 285 | [x] | Castle in the Clouds (STEAM) | 14 | 2026-11-09 | 28 | 61% |  |
| 286 | [x] | Human Fall Flat (STEAM) | 14 | 2026-10-29 | 28 | 64% |  |
| 287 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 14 | 2026-11-09 | 27 | 61% |  |
| 288 | [x] | Ultrapool (STEAM) | 14 | 2026-11-09 | 27 | n/a |  |
| 289 | [x] | Another World: 20th Anniversary Edition (GOG) | 14 | 2026-11-21 | 25 | 64% |  |
| 290 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 14 | 2026-11-15 | 23 | 62% |  |
| 291 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-11-09 | 22 | 93% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 292 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 293 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 2026-11-16 | 22 | 93% |  |
| 294 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 21 | 69% |  |
| 295 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 296 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 297 | [x] | Spark the Electric Jester (STEAM) | 14 | 2026-11-13 | 20 | 69% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 298 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 13 | 2026-11-09 | 28 | 91% |  |
| 299 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 28 | 83% |  |
| 300 | [x] | Evoland (STEAM) | 13 | 2026-11-11 | 27 | n/a |  |
| 301 | [x] | MX Bikes (STEAM) | 13 | 2026-11-09 | 27 | 93% |  |
| 302 | [x] | WORLD OF FINAL FANTASY (STEAM) | 13 | 2026-11-09 | 27 | 88% |  |
| 303 | [x] | Blaster Master Zero (STEAM) | 13 | 2026-11-11 | 26 | 79% |  |
| 304 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 26 | 82% |  |
| 305 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 13 | 2026-11-13 | 26 | 55% |  |
| 306 | [x] | Batman™: Arkham Origins (GOG) | 13 | 2026-11-09 | 25 | 100% |  |
| 307 | [x] | Cruelty Squad (STEAM) | 13 | 2026-11-09 | 25 | 86% |  |
| 308 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 24 | 74% |  |
| 309 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 310 | [x] | Shift At Midnight (STEAM) | 13 | 2026-11-09 | 21 | 90% |  |
| 311 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 70% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 312 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 100% |  |
| 313 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 314 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 2026-11-09 | 20 | 85% |  |
| 315 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-11-16 | 20 | 92% |  |
| 316 | [x] | GRIP: Combat Racing (STEAM) | 12 | 2026-11-09 | 31 | 77% |  |
| 317 | [x] | Overlord (STEAM) | 12 | 2026-11-08 | 29 | 56% |  |
| 318 | [x] | Antichamber (STEAM) | 12 | 2026-11-18 | 27 | 80% |  |
| 319 | [x] | A Plague Tale: Innocence (GOG) | 12 | 2026-11-18 | 24 | 60% |  |
| 320 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-10 | 24 | 62% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 321 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 24 | 64% |  |
| 322 | [x] | Sonic Superstars (STEAM) | 12 | 2026-11-21 | 24 | 62% |  |
| 323 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-11-09 | 22 | 95% |  |
| 324 | [x] | Haydee (STEAM) | 12 | 2026-11-09 | 22 | 79% |  |
| 325 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 326 | [x] | Horny Villa (STEAM) | 12 | 2026-11-09 | 21 | 86% |  |
| 327 | [x] | The Stanley Parable (STEAM) | 12 | 2026-11-13 | 21 | 78% |  |
| 328 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 329 | [x] | 12 is Better Than 6 (STEAM) | 12 | 2026-11-09 | 20 | 75% |  |
| 330 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 331 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 2026-11-10 | 20 | 60% |  |
| 332 | [x] | Turbo Overkill (STEAM) | 12 | 2026-11-09 | 20 | 95% |  |
| 333 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 25 | 83% |  |
| 334 | [x] | Alan Wake's American Nightmare (EPIC) | 11 | 2026-11-09 | 24 | 64% |  |
| 335 | [x] | GRANDIA HD Remaster (STEAM) | 11 | 2026-11-09 | 24 | 89% |  |
| 336 | [x] | HITMAN World of Assassination (STEAM) | 11 | 2026-11-09 | 23 | 76% |  |
| 337 | [x] | Life is Strange Remastered (STEAM) | 11 | 2026-11-09 | 23 | 86% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 338 | [x] | Ready or Not (STEAM) | 11 | 2026-11-09 | 23 | 83% |  |
| 339 | [x] | Lost Castle 2 (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 340 | [x] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 2026-11-18 | 21 | 69% |  |
| 341 | [x] | Forgive Me Father (STEAM) | 11 | 2026-11-15 | 21 | 75% |  |
| 342 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 343 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-11-09 | 20 | 71% |  |
| 344 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 11 | 2026-10-27 | 20 | 87% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 345 | [x] | The WereCleaner (STEAM) | 10 | 2026-10-22 | 31 | 89% |  |
| 346 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 28 | 90% |  |
| 347 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 10 | 2026-10-27 | 25 | 80% |  |
| 348 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 25 | 92% |  |
| 349 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 10 | 2026-11-09 | 24 | 83% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 350 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 10 | 2026-10-23 | 24 | 89% |  |
| 351 | [x] | Soul's Remnant (STEAM) | 10 | 2026-11-11 | 24 | n/a |  |
| 352 | [x] | Breath of Fire IV (GOG) | 10 | 2026-10-26 | 23 | 65% |  |
| 353 | [x] | DiRT 4 (STEAM) | 10 | 2026-11-09 | 21 | 100% |  |
| 354 | [x] | UNDEFEATED (STEAM) | 10 | 2026-11-09 | 21 | 73% |  |
| 355 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 356 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 357 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 20 | 81% |  |
| 358 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 359 | [x] | Pillars of Eternity (STEAM) | 10 | 2026-11-21 | 20 | 100% |  |
| 360 | [x] | Secret of Mana (STEAM) | 10 | 2026-11-18 | 20 | 70% |  |
| 361 | [x] | Rayman Origins (GOG) | 9 | 2026-11-09 | 23 | 69% |  |
| 362 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 9 | 2026-11-01 | 23 | n/a |  |
| 363 | [x] | Guacamelee! Gold Edition (STEAM) | 9 | 2026-11-11 | 22 | 75% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 364 | [x] | Need for Speed: Undercover (STEAM) | 9 | 2026-11-11 | 22 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 365 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 9 | 2026-11-09 | 21 | 70% |  |
| 366 | [x] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 9 | 2026-11-17 | 20 | 33% |  |
| 367 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 27% |  |
| 368 | [x] | Possessor(s) (STEAM) | 8 | 2026-10-24 | 25 | 73% |  |
| 369 | [x] | Lust Goddess (STEAM) | 8 | 2026-11-09 | 22 | 76% |  |
| 370 | [x] | Aperture Desk Job (STEAM) | 8 | 2026-11-03 | 21 | n/a |  |
| 371 | [x] | SteamWorld Heist (GOG) | 8 | 2026-10-25 | 20 | n/a |  |
| 372 | [x] | Ultimate Chicken Horse (STEAM) | 7 | 2026-10-23 | 27 | 93% |  |
| 373 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 21 | 51% |  |
| 374 | [x] | SCP – Containment Breach (STEAM) | 7 | 2026-10-27 | 21 | 91% |  |
| 375 | [x] | Mina the Hollower (GOG) | 7 | 2026-10-28 | 20 | 74% |  |
| 376 | [x] | CULTIC (STEAM) | 7 | 2026-11-09 | 20 | 53% |  |
