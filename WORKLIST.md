# GameNative compatibility worklist

Generated: `2026-11-24T04:15:12.406Z` · Ratings since: `2026-08-26T04:15:12.406Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 132 |
| Probably does not work | 179 |
| Fix shipped, waiting for ratings | 16 |
| First launch fails | 292 |
| Mixed | 470 |
| Works | 1018 |
| Total | 2107 |

## Does not work (132)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 201 | 236 | 85% (since fix) | Does not open (91%) | 40% | today | 34% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 2 | [ ] | Slay the Spire (STEAM) | 138 | 167 | 83% (14d) | Does not open (83%) | 44% | today | 31% | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 3 | [ ] | Rocket League® (EPIC) | 82 | 94 | 87% (14d) | Does not open (81%) | 32% | today | 27% | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 4 | [ ] | Buckshot Roulette (STEAM) | 40 | 56 | 71% (14d) | Does not open (68%) | 55% | today | 44% |  |
| 5 | [ ] | Melvor Idle 2: A RuneScape Adventure (STEAM) | 40 | 41 | 98% (14d) | Does not open (97%) | 41% | today | 40% | [#543](https://github.com/GameNative/gamenative-compat/issues/543) |
| 6 | [ ] | DREDGE (EPIC) | 31 | 36 | 86% (14d) | Does not open (79%) | 52% | 1d ago | 46% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 7 | [ ] | Hogwarts Legacy (STEAM) | 30 | 32 | 94% (14d) | Does not open (72%) | 25% | today | 16% | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 8 | [ ] | Horizon Chase Turbo (EPIC) | 27 | 33 | 82% (14d) | Does not open (83%) | 52% | today | 44% | [#546](https://github.com/GameNative/gamenative-compat/issues/546) |
| 9 | [ ] | Mark of the Deep (EPIC) | 25 | 33 | 76% (14d) | Does not open (87%) | 22% | today | 20% | [#549](https://github.com/GameNative/gamenative-compat/issues/549) |
| 10 | [ ] | Borderlands 2 (EPIC) | 24 | 27 | 89% (14d) | Does not open (81%) | 51% | today | 46% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 11 | [x] 2026-10-18 | Project Zomboid (STEAM) | 64 | 71 | 90% (since fix) | Does not open (64%) | 38% | today | 37% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 12 | [ ] | Absolute Drift (EPIC) | 22 | 31 | 71% (14d) | No graphics (59%) | 48% | today | 32% | [#555](https://github.com/GameNative/gamenative-compat/issues/555) |
| 13 | [ ] | BioShock Remastered (EPIC) | 21 | 27 | 78% (14d) | Does not open (67%) | 55% | 1d ago | 50% | [#547](https://github.com/GameNative/gamenative-compat/issues/547) |
| 14 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 20 | 20 | 100% (last 20) | Does not open (96%) | 26% | 1d ago | 20% | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 15 | [ ] | Bloons TD 6 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (77%) | 34% | today | 24% | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 16 | [ ] | Saints Row 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | 27% | today | 28% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 17 | [ ] | Driver: Parallel Lines (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | 43% | 2d ago | 46% | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 18 | [ ] | Metro: Last Light Redux (STEAM) | 20 | 20 | 100% (last 20) | Does not open (93%) | 26% | today | 28% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 19 | [ ] | Path of Exile (STEAM) | 17 | 21 | 81% (14d) | Does not open (89%) | 27% | today | 25% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 20 | [ ] | Castlevania Anniversary Collection (EPIC) | 19 | 20 | 95% (last 20) | Does not open (79%) | 51% | today | 37% | [#556](https://github.com/GameNative/gamenative-compat/issues/556) |
| 21 | [ ] | Saints Row 2 (GOG) | 18 | 20 | 90% (last 20) | Does not open (91%) | 33% | today | 32% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 22 | [ ] | Sifu (EPIC) | 15 | 20 | 75% (14d) | Does not open (72%) | 40% | today | 35% | [#535](https://github.com/GameNative/gamenative-compat/issues/535) |
| 23 | [ ] | River City Girls (EPIC) | 15 | 20 | 75% (last 20) | Does not open (50%) | 50% | 2d ago | 38% | [#550](https://github.com/GameNative/gamenative-compat/issues/550) |
| 24 | [ ] | Bad Cheese (EPIC) | 16 | 20 | 80% (last 20) | Does not open (94%) | 45% | today | 34% |  |
| 25 | [ ] | Dead Island 2 (EPIC) | 20 | 20 | 100% (last 20) | Does not open (86%) | 52% | 1d ago | 40% | [#552](https://github.com/GameNative/gamenative-compat/issues/552) |
| 26 | [ ] | Until Then (STEAM) | 18 | 20 | 90% (last 20) | Does not open (86%) | 58% | today | 46% |  |
| 27 | [ ] | Mafia II (Classic) (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 8% | 6d ago | 10% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 28 | [ ] | Vampire Survivors (EPIC) | 17 | 20 | 85% (last 20) | Does not open (63%) | 38% | 1d ago | 32% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 29 | [ ] | Hogwarts Legacy (EPIC) | 17 | 20 | 85% (last 20) | Does not open (76%) | 43% | 1d ago | 35% | [#537](https://github.com/GameNative/gamenative-compat/issues/537) |
| 30 | [ ] | skate. (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | 11% | 2d ago | 10% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 31 | [ ] | Call of Duty: Black Ops II (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 44% | 3d ago | 44% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 32 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 59% | 5d ago | 57% | [#553](https://github.com/GameNative/gamenative-compat/issues/553) |
| 33 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 51% | today | 46% | [#548](https://github.com/GameNative/gamenative-compat/issues/548) |
| 34 | [ ] | Forza Horizon 4 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (43%) | 40% | 1d ago | 24% | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 35 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (91%) | 19% | 10d ago | 14% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 36 | [ ] | Teenage Mutant Ninja Turtles: Shredder's Revenge (EPIC) | 15 | 20 | 75% (last 20) | Does not open (83%) | 46% | 1d ago | 42% | [#551](https://github.com/GameNative/gamenative-compat/issues/551) |
| 37 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 10 | 14 | 71% (since fix) | Does not open (91%) | 47% | 4d ago | 50% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 38 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (76%) | 6% | 9d ago | 7% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 39 | [ ] | Trackmania (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 28% | 2d ago | 29% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 40 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 36% | 1d ago | 29% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 41 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 16 | 20 | 80% (last 20) | Does not open (45%) | 56% | 5d ago | 75% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 42 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 52% | 2d ago | 57% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 43 | [ ] | Fall Guys (EPIC) | 20 | 20 | 100% (last 20) | Does not open (68%) | 4% | 1d ago | 4% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 44 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (71%) | 20% | 5d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 45 | [ ] | Kenshi (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 8% | 2d ago | 6% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 46 | [ ] | Metro 2033 Redux (EPIC) | 14 | 20 | 70% (last 20) | Does not open (67%) | 32% | today | 33% |  |
| 47 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 8% | today | 5% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 48 | [ ] | Happy Wheels (STEAM) | 18 | 20 | 90% (last 20) | No graphics (52%) | 54% | today | 45% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 49 | [ ] | Detroit: Become Human (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | 56% | 6d ago | 53% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 50 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (70%) | 17% | 2d ago | 18% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 51 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 54% | 2d ago | 50% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 52 | [ ] | Breath of Fire IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (64%) | 16% | 4d ago | 10% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 53 | [ ] | The Witcher: Enhanced Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (76%) | 8% | 2d ago | 10% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 54 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (72%) | 0% | 9d ago | 0% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 55 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | 7% | 23d ago | 9% | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 56 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (94%) | 6% | 6d ago | 0% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 57 | [ ] | Call of Duty® (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | 0% | 3d ago | 0% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 58 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (82%) | 9% | 2d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 59 | [ ] | MECCHA CHAMELEON (STEAM) | 15 | 20 | 75% (last 20) | Does not open (70%) | 40% | 6d ago | 37% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 60 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 58% | 8d ago | 53% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 61 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (70%) | 17% | 10d ago | 23% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 62 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (82%) | 12% | 15d ago | 14% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 63 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (88%) | 56% | today | 52% | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 64 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (60%) | 10% | 1d ago | n/a | [#536](https://github.com/GameNative/gamenative-compat/issues/536) |
| 65 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (82%) | 42% | 6d ago | 45% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 66 | [ ] | Blood Omen: Legacy of Kain (GOG) | 16 | 20 | 80% (last 20) | No graphics (57%) | 55% | 5d ago | 55% | [#539](https://github.com/GameNative/gamenative-compat/issues/539) |
| 67 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (78%) | 5% | today | 6% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 68 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (91%) | 0% | 10d ago | 0% | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 69 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 41% | 3d ago | 48% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 70 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (67%) | 24% | 12d ago | 21% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 71 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (74%) | 45% | 1d ago | 44% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 72 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 55% | 1d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 73 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (53%) | 29% | 6d ago | 18% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 74 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | 0% | 9d ago | 0% | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 75 | [ ] | Half-Life: Blue Shift (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | 40% | 7d ago | 46% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 76 | [ ] | Rivals of Aether II (STEAM) | 16 | 20 | 80% (last 20) | Does not open (51%) | 35% | 7d ago | 10% (drop) | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 77 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 34% | 1d ago | 38% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 78 | [ ] | Borderlands GOTY (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | 33% | today | 47% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 79 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (47%) | 49% | 3d ago | 45% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 80 | [ ] | Black Mesa (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 33% | 2d ago | 33% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 81 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | 10% | 11d ago | 10% | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 82 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 53% | 10d ago | 53% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 83 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | 15% | 12d ago | 11% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 84 | [ ] | A Plague Tale: Innocence (EPIC) | 14 | 20 | 70% (last 20) | Does not open (70%) | 46% | 1d ago | 41% | [#557](https://github.com/GameNative/gamenative-compat/issues/557) |
| 85 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 19 | 20 | 95% (last 20) | Does not open (85%) | 45% | 7d ago | 50% | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 86 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (73%) | 25% | 17d ago | 21% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 87 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 3% | today | 1% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 88 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | 10% | 22d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 89 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 17% | 1d ago | 20% | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 90 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 17 | 20 | 85% (last 20) | Does not open (63%) | 27% | 2d ago | 23% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 91 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | Does not open (63%) | 28% | 3d ago | 27% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 92 | [ ] | Umamusume: Pretty Derby (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 48% | 4d ago | 52% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 93 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 56% | 13d ago | 36% (drop) | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 94 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | 45% | 13d ago | 45% | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 95 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 0% | 24d ago | 0% | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 96 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 32% | 3d ago | 38% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 97 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (50%) | 56% | 5d ago | 62% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 98 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (73%) | 0% | 37d ago | 0% | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 99 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (63%) | 0% | today | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 100 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (89%) | 21% | 1d ago | 12% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 101 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (84%) | 3% | 2d ago | 3% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 102 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 21% | 4d ago | 17% | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 103 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 19 | 20 | 95% (last 20) | Does not open (58%) | 32% | 1d ago | 39% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 104 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | 33% | 1d ago | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 105 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 8% | 30d ago | 8% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 106 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (64%) | 43% | 4d ago | 43% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 107 | [ ] | Aliens vs. Predator (STEAM) | 17 | 20 | 85% (last 20) | Does not open (73%) | 33% | 2d ago | 36% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 108 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (61%) | 35% | today | 18% | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 109 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 20 | 80% (last 20) | Does not open (53%) | 41% | today | 33% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 110 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | 27% | 22d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 111 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 57% | 3d ago | 50% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 112 | [ ] | Lost Planet: Extreme Condition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | 54% | 9d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 113 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | 30% | 1d ago | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 114 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (89%) | 30% | 8d ago | 33% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 115 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 38% | 2d ago | 46% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 116 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 50% | 27d ago | 38% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 117 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | 25% | 24d ago | 25% | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 118 | [ ] | OneShot (STEAM) | 15 | 20 | 75% (last 20) | Does not open (94%) | 18% | 3d ago | 20% | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 119 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 43% | 2d ago | 37% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 120 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (55%) | 44% | 12d ago | 23% (drop) | [#540](https://github.com/GameNative/gamenative-compat/issues/540) |
| 121 | [ ] | Maneater (EPIC) | 17 | 20 | 85% (last 20) | Does not open (73%) | 30% | 1d ago | 18% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 122 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | 31% | 13d ago | 27% | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 123 | [ ] | Beyond Good & Evil™ (GOG) | 17 | 20 | 85% (last 20) | Does not open (100%) | 17% | 5d ago | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 124 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (58%) | 54% | 12d ago | 54% | [#554](https://github.com/GameNative/gamenative-compat/issues/554) |
| 125 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 14 | 20 | 70% (last 20) | Does not open (100%) | 50% | 1d ago | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 126 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (73%) | 57% | 15d ago | 67% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 127 | [ ] | Ghostwire Tokyo (EPIC) | 14 | 20 | 70% (last 20) | Does not open (90%) | 43% | today | 35% | [#544](https://github.com/GameNative/gamenative-compat/issues/544) |
| 128 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 20 | 80% (last 20) | Does not open (82%) | 50% | 8d ago | 33% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 129 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 20% | today | 24% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 130 | [ ] | Maneater (STEAM) | 14 | 20 | 70% (last 20) | Does not open (85%) | 59% | 3d ago | 62% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 131 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (54%) | 40% | 9d ago | 38% | [#541](https://github.com/GameNative/gamenative-compat/issues/541) |
| 132 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 20 | 70% (last 20) | Does not open (70%) | 42% | 16d ago | 42% | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |

## Probably does not work (179)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Counter-Strike 2 (STEAM) | 53 | 78 | 68% (since fix) | Does not open (68%) | 56% | today | 56% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 2 | [ ] | Owlboy (STEAM) | 18 | 27 | 67% (14d) | Does not open (80%) | 53% | 1d ago | 49% | [#545](https://github.com/GameNative/gamenative-compat/issues/545) |
| 3 | [ ] | theHunter Classic (STEAM) | 20 | 20 | 100% (last 20) | No graphics (92%) | n/a | 20d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 4 | [ ] | Metro 2033 Redux (STEAM) | 13 | 23 | 57% (14d) | Does not open (72%) | 42% | 1d ago | 41% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 5 | [ ] | Bully: Scholarship Edition (STEAM) | 13 | 20 | 65% (14d) | Does not open (67%) | 32% | 1d ago | 13% |  |
| 6 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 13 | 20 | 65% (14d) | Does not open (79%) | 50% | today | 46% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 7 | [ ] | Garry's Mod (STEAM) | 16 | 26 | 62% (since fix) | Does not open (80%) | 49% | today | 43% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 8 | [ ] | To The Moon (GOG) | 18 | 20 | 90% (last 20) | Does not open (86%) | n/a | 21d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 9 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (78%) | n/a | 15d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 10 | [ ] | Batman™ Arkham Asylum Game of the Year Edition (EPIC) | 11 | 20 | 55% (last 20) | Does not open (75%) | 51% | 1d ago | 41% |  |
| 11 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 13 | 20 | 65% (last 20) | Does not open (64%) | 46% | 1d ago | 41% |  |
| 12 | [ ] | VRChat (STEAM) | 13 | 20 | 65% (last 20) | Does not open (74%) | 38% | 1d ago | 36% |  |
| 13 | [ ] | Asterigos: Curse of the Stars (STEAM) | 16 | 20 | 80% (last 20) | Graphics glitches (73%) | n/a | 2d ago | n/a |  |
| 14 | [ ] | Cat Quest (EPIC) | 11 | 20 | 55% (last 20) | Does not open (52%) | 43% | 1d ago | 39% |  |
| 15 | [ ] | Catherine Classic (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (40%) | 46% | today | 42% |  |
| 16 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 16 | 24 | 67% (since fix) | Does not open (78%) | 39% | 1d ago | 42% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 17 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 8 | 12 | 67% (since fix) | Does not open (82%) | 59% | 2d ago | 60% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 18 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 11 | 20 | 55% (last 20) | Does not open (72%) | 34% | today | 35% |  |
| 19 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 44d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 20 | [ ] | PAYDAY: The Heist (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | n/a | 3d ago | n/a |  |
| 21 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (38%) | n/a | 3d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 22 | [ ] | Sonic Adventure™ 2  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (77%) | 46% | 1d ago | 40% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 23 | [ ] | STAR WARS™ Knights of the Old Republic™ II: The Sith Lords™ (STEAM) | 12 | 20 | 60% (last 20) | No graphics (64%) | 51% | 3d ago | 41% |  |
| 24 | [ ] | Darksiders Warmastered Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 47% | 1d ago | 36% |  |
| 25 | [ ] | MudRunner (EPIC) | 12 | 20 | 60% (last 20) | Does not open (65%) | 48% | 1d ago | 41% |  |
| 26 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 10d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 27 | [ ] | Door Kickers 2 (STEAM) | 18 | 20 | 90% (last 20) | No graphics (86%) | n/a | 1d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 28 | [ ] | Art of Rally (EPIC) | 12 | 20 | 60% (last 20) | Does not open (77%) | 39% | 1d ago | 36% |  |
| 29 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 11 | 20 | 55% (last 20) | Does not open (73%) | 50% | 2d ago | 43% |  |
| 30 | [ ] | Deskrawl: Idle ARPG (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | n/a | 13d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 31 | [ ] | Hi-Fi RUSH (STEAM) | 13 | 20 | 65% (last 20) | Does not open (77%) | 44% | today | 46% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 32 | [ ] | Gorilla Tag (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 13% | today | 8% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 33 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (49%) | 52% | 10d ago | 39% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 34 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (79%) | 53% | 3d ago | 48% |  |
| 35 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 28d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 36 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (100%) | n/a | 1d ago | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 37 | [ ] | Phasmophobia (STEAM) | 12 | 20 | 60% (last 20) | Does not open (56%) | 55% | 2d ago | 48% |  |
| 38 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | No graphics (59%) | n/a | 27d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 39 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | No graphics (38%) | 44% | 2d ago | 35% |  |
| 40 | [ ] | Counter-Strike (STEAM) | 11 | 20 | 55% (last 20) | Does not open (68%) | 34% | today | 31% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 41 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (87%) | n/a | 17d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 42 | [ ] | Deliver At All Costs (EPIC) | 13 | 20 | 65% (last 20) | Does not open (65%) | 44% | today | 45% | [#538](https://github.com/GameNative/gamenative-compat/issues/538) |
| 43 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 12 | 20 | 60% (last 20) | Does not open (88%) | 44% | 4d ago | 23% (drop) | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 44 | [ ] | Counter-Strike:Global Offensive (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 59% | 1d ago | 59% |  |
| 45 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 25d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 46 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | n/a | 7d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 47 | [ ] | CPM 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (88%) | 3% | 2d ago | 3% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 48 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | n/a | 16d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 49 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | n/a | 9d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 50 | [ ] | CODE VEIN (STEAM) | 13 | 20 | 65% (last 20) | Does not open (68%) | 24% | 8d ago | 13% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 51 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | 59% | today | 50% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 52 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 19d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 53 | [ ] | Rise of the Tomb Raider: 20 Year Celebration (EPIC) | 13 | 20 | 65% (last 20) | Does not open (73%) | 41% | today | 38% |  |
| 54 | [ ] | No More Heroes (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 38% | 1d ago | 33% |  |
| 55 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | n/a | 22d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 56 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | n/a | 2d ago | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 57 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 13d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 58 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | n/a | 43d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 59 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | n/a | 9d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 60 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | n/a | 5d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 61 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 40% | 1d ago | n/a |  |
| 62 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 42d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 63 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | n/a | 33d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 64 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 5d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 65 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (74%) | n/a | 21d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 66 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | 10d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 67 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 41d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 68 | [ ] | Alpha Protocol (STEAM) | 17 | 20 | 85% (last 20) | No graphics (53%) | n/a | 29d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 69 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (57%) | n/a | 9d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 70 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 36% | today | 30% |  |
| 71 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | n/a | 10d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 72 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (56%) | n/a | 10d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 73 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | n/a | 25d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 74 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 19d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 75 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 40% | 7d ago | 31% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 76 | [ ] | Dead Space 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 32% | 3d ago | 28% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 77 | [ ] | Metro 2033 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (65%) | 40% | 3d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 78 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | n/a | 44d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 79 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 41d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 80 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (53%) | n/a | today | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 81 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 10d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 82 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 41d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 83 | [ ] | Borderlands 2 RU (STEAM) | 18 | 20 | 90% (last 20) | Does not open (55%) | n/a | 7d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 84 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | 6d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 85 | [ ] | DOOM Eternal (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | n/a | 1d ago | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 86 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 27d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 87 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 27d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 88 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 50% | 20d ago | 50% |  |
| 89 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | n/a | 16d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 90 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 23d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 91 | [ ] | Pathway (EPIC) | 19 | 20 | 95% (last 20) | Does not open (59%) | n/a | today | n/a | [#298](https://github.com/GameNative/gamenative-compat/issues/298) |
| 92 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | n/a | 6d ago | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 93 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (96%) | n/a | 22d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 94 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (76%) | n/a | today | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 95 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 15d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 96 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (80%) | n/a | 8d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 97 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (54%) | n/a | 29d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 98 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (71%) | 23% | 14d ago | 19% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 99 | [ ] | Hollow Knight: Silksong (GOG) | 10 | 20 | 50% (last 20) | Does not open (65%) | 49% | 2d ago | 47% |  |
| 100 | [ ] | Beholder (EPIC) | 18 | 20 | 90% (last 20) | Does not open (61%) | n/a | 3d ago | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 101 | [ ] | The Survivalists (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | n/a | 11d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 102 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | n/a | 46d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 103 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | n/a | 3d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 104 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | n/a | 7d ago | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 105 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (61%) | n/a | 50d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 106 | [ ] | Brutal Legend (GOG) | 16 | 20 | 80% (last 20) | Does not open (82%) | n/a | 2d ago | n/a |  |
| 107 | [ ] | Super Meat Boy Forever (EPIC) | 10 | 20 | 50% (last 20) | Does not open (83%) | 37% | 4d ago | 27% |  |
| 108 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | n/a | 17d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 109 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (53%) | n/a | 17d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 110 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 19d ago | n/a |  |
| 111 | [ ] | Halo: Spartan Assault (STEAM) | 16 | 20 | 80% (last 20) | Does not open (79%) | n/a | today | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 112 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 12d ago | n/a |  |
| 113 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 13 | 20 | 65% (last 20) | Does not open (88%) | n/a | 1d ago | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 114 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 15d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 115 | [ ] | Utopia Must Fall (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | n/a | today | n/a | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 116 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 25d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 117 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | n/a | 14d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 118 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (36%) | n/a | 2d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 119 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (47%) | n/a | 8d ago | n/a |  |
| 120 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 19d ago | n/a |  |
| 121 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 58% | 5d ago | 70% | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 122 | [ ] | Lucid Blocks (STEAM) | 11 | 20 | 55% (last 20) | Does not open (94%) | 58% | 4d ago | 50% |  |
| 123 | [ ] | Goat Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (58%) | 55% | today | 55% |  |
| 124 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 12d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 125 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 26d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 126 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | n/a | 6d ago | n/a | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 127 | [ ] | Mortal Shell (EPIC) | 13 | 20 | 65% (last 20) | Does not open (50%) | 28% | 5d ago | 21% |  |
| 128 | [ ] | Drop Duchy (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 10% | 5d ago | n/a |  |
| 129 | [ ] | Hitman 2: Silent Assassin (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 43% | 1d ago | 42% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 130 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 19d ago | n/a |  |
| 131 | [ ] | Mafia: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (87%) | 33% | 1d ago | 31% |  |
| 132 | [ ] | Dying Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (77%) | 46% | 1d ago | 39% |  |
| 133 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Controller issues (36%) | n/a | 5d ago | n/a |  |
| 134 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 10 | 20 | 50% (last 20) | Does not open (90%) | 42% | 2d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 135 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | n/a | 8d ago | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 136 | [ ] | Fallout Classic (GOG) | 15 | 20 | 75% (last 20) | Does not open (86%) | n/a | 11d ago | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 137 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | Does not open (43%) | n/a | 14d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 138 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | n/a | 4d ago | n/a |  |
| 139 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | n/a | 36d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 140 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (67%) | n/a | 19d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 141 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 13 | 20 | 65% (last 20) | Does not open (55%) | 33% | 8d ago | 27% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 142 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 55% | 12d ago | n/a |  |
| 143 | [ ] | Romancing SaGa -Minstrel Song- Remastered (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (100%) | n/a | 2d ago | n/a |  |
| 144 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 39% | 24d ago | 29% |  |
| 145 | [ ] | HOT WHEELS UNLEASHED™ (EPIC) | 12 | 20 | 60% (last 20) | No graphics (50%) | 41% | today | 32% |  |
| 146 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | 11d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 147 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | n/a | 14d ago | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 148 | [ ] | Re-Volt (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (69%) | n/a | 2d ago | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 149 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (63%) | 50% | 10d ago | n/a |  |
| 150 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (58%) | n/a | 1d ago | n/a |  |
| 151 | [ ] | Sacred Gold (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | n/a | 5d ago | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 152 | [ ] | Chasm (GOG) | 12 | 20 | 60% (last 20) | No graphics (50%) | n/a | 9d ago | n/a |  |
| 153 | [ ] | Crying Suns (EPIC) | 12 | 20 | 60% (last 20) | No graphics (56%) | n/a | 1d ago | n/a |  |
| 154 | [ ] | DAEMON X MACHINA (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 44% | 1d ago | 29% |  |
| 155 | [ ] | Decktamer (STEAM) | 13 | 20 | 65% (last 20) | Does not open (100%) | n/a | 1d ago | n/a |  |
| 156 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | 36% | 13d ago | 40% |  |
| 157 | [ ] | Songs of Conquest (EPIC) | 13 | 20 | 65% (last 20) | Does not open (75%) | n/a | 8d ago | n/a |  |
| 158 | [ ] | FINAL FANTASY VII REMAKE INTERGRADE (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 41% | 9d ago | 41% |  |
| 159 | [ ] | Sandustry (STEAM) | 12 | 20 | 60% (last 20) | Does not open (73%) | n/a | 9d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 160 | [ ] | LET IT DIE (STEAM) | 12 | 20 | 60% (last 20) | Does not open (94%) | n/a | 2d ago | n/a |  |
| 161 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | n/a | 1d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 162 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | n/a | 5d ago | n/a |  |
| 163 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 11 | 20 | 55% (last 20) | Does not open (100%) | 33% | 2d ago | 30% |  |
| 164 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Does not open (40%) | n/a | 15d ago | n/a |  |
| 165 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 10 | 20 | 50% (last 20) | No graphics (60%) | 56% | 8d ago | 64% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 166 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | today | n/a |  |
| 167 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | n/a | 14d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 168 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 25% | 5d ago | n/a |  |
| 169 | [ ] | Minit (EPIC) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 16d ago | n/a |  |
| 170 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 19d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 171 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 25d ago | n/a |  |
| 172 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | n/a | 12d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 173 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 52% | 3d ago | 57% |  |
| 174 | [ ] | Hitman: Absolution (GOG) | 10 | 20 | 50% (last 20) | Does not open (82%) | n/a | 6d ago | n/a |  |
| 175 | [ ] | Allumeria (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | n/a | 2d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 176 | [ ] | A Plague Tale: Innocence (GOG) | 10 | 20 | 50% (last 20) | Does not open (91%) | n/a | 6d ago | n/a |  |
| 177 | [ ] | Turnip Boy Robs a Bank (EPIC) | 11 | 20 | 55% (last 20) | Does not open (64%) | 33% | 10d ago | 30% | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 178 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 50% | 11d ago | n/a |  |
| 179 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | n/a | 18d ago | n/a |  |

## Fix shipped, waiting for ratings (16)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | Max Payne 3 (STEAM) | 2026-11-04 | 5 | 5 | today | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 2 | Peggle Deluxe (STEAM) | 2026-10-29 | 7 | 3 | today | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 3 | Red Dead Redemption (STEAM) | 2026-11-04 | 2 | 2 | 7d ago | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 4 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 8 | 8 | 4d ago | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 5 | Transistor (STEAM) | 2026-11-10 | 8 | 4 | 4d ago | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 6 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 4 | 4 | 2d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 7 | Watch_Dogs (STEAM) | n/a | 4 | 4 | today | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 8 | XCOM: Enemy Unknown (STEAM) | n/a | 1 | 1 | today | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 9 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 2 | 2 | today | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 10 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 5 | 5 | 3d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 11 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 2 | 2 | 1d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 12 | Need for Speed™ (STEAM) | 2026-11-04 | 2 | 2 | today | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 13 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 2 | 2 | 2d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 14 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 19d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 15 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 2 | 2 | 1d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 16 | Assassin's Creed Odyssey (STEAM) | n/a | 1 | 1 | 2d ago | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |

## Works, but the first launch usually fails (292)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Half-Life (STEAM) | 83 | 117 | 71% (14d) | Does not open (61%) | 71% | today | 68% |  |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 78 | 98 | 80% (14d) | Does not open (62%) | 94% | today | 95% |  |
| 3 | [ ] | Grand Theft Auto V Legacy (STEAM) | 88 | 104 | 85% (since fix) | Does not open (87%) | 74% | today | 73% |  |
| 4 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 59 | 74 | 80% (14d) | Does not open (55%) | 83% | today | 83% |  |
| 5 | [ ] | Portal (STEAM) | 46 | 79 | 58% (14d) | Does not open (41%) | 89% | today | 88% |  |
| 6 | [ ] | Cyberpunk 2077 (STEAM) | 43 | 77 | 56% (14d) | Does not open (69%) | 72% | today | 71% |  |
| 7 | [ ] | ROB RUN (STEAM) | 40 | 54 | 74% (14d) | Does not open (88%) | 67% | today | 68% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 8 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 35 | 50 | 70% (14d) | Does not open (60%) | 64% | today | 61% |  |
| 9 | [ ] | MONSTER HUNTER RISE (STEAM) | 32 | 61 | 52% (14d) | Does not open (83%) | 61% | today | 63% |  |
| 10 | [ ] | Selaco (STEAM) | 31 | 47 | 66% (14d) | Does not open (88%) | 62% | today | 60% |  |
| 11 | [ ] | Valheim (STEAM) | 43 | 74 | 58% (since fix) | No graphics (54%) | 81% | today | 82% |  |
| 12 | [ ] | Probably Stolen (STEAM) | 27 | 43 | 63% (14d) | Does not open (65%) | 85% | today | 80% |  |
| 13 | [ ] | No Man's Sky (STEAM) | 37 | 71 | 52% (since fix) | Controller issues (61%) | 81% | today | 78% |  |
| 14 | [ ] | Euro Truck Simulator 2 (STEAM) | 21 | 38 | 55% (14d) | Does not open (64%) | 62% | 1d ago | 60% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 15 | [ ] | ELDEN RING (STEAM) | 20 | 32 | 63% (14d) | Does not open (86%) | 65% | today | 65% |  |
| 16 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 18 | 33 | 55% (14d) | Does not open (74%) | 71% | today | 73% |  |
| 17 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (39%) | 92% | today | 90% |  |
| 18 | [ ] | BeamNG.drive (STEAM) | 17 | 24 | 71% (14d) | Does not open (77%) | 65% | 1d ago | 59% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 19 | [ ] | Overcooked! 2 (EPIC) | 17 | 21 | 81% (14d) | Does not open (92%) | 63% | 2d ago | 57% |  |
| 20 | [ ] | Red Dead Redemption 2 (STEAM) | 24 | 28 | 86% (since fix) | Does not open (97%) | 85% | 1d ago | 87% |  |
| 21 | [ ] | Fallout: New Vegas PCR (STEAM) | 17 | 20 | 85% (last 20) | Does not open (93%) | 67% | 2d ago | 62% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 22 | [ ] | Baldur's Gate 3 (STEAM) | 16 | 27 | 59% (14d) | Does not open (68%) | 84% | 1d ago | 83% |  |
| 23 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 17 | 20 | 85% (last 20) | Does not open (77%) | 61% | today | 64% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 24 | [ ] | Team Fortress 2 (STEAM) | 15 | 27 | 56% (14d) | Does not open (67%) | 77% | today | 75% |  |
| 25 | [ ] | Resident Evil 4 (2005) (STEAM) | 15 | 21 | 71% (14d) | Does not open (79%) | 71% | today | 69% |  |
| 26 | [ ] | Dead Space (STEAM) | 17 | 20 | 85% (last 20) | Does not open (62%) | 80% | today | 79% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 27 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 14 | 21 | 67% (14d) | Controller issues (53%) | 70% | today | 63% |  |
| 28 | [ ] | Library Of Ruina (STEAM) | 14 | 24 | 58% (14d) | Does not open (73%) | 88% | today | 87% |  |
| 29 | [ ] | Grand Theft Auto V (EPIC) | 19 | 20 | 95% (last 20) | Does not open (88%) | 77% | today | 76% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 30 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | 87% | 1d ago | 88% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 31 | [ ] | Noita (STEAM) | 13 | 21 | 62% (14d) | Does not open (59%) | 78% | today | 78% |  |
| 32 | [ ] | Clair Obscur: Expedition 33 (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (41%) | 76% | today | 73% |  |
| 33 | [ ] | Cry of Fear (STEAM) | 14 | 20 | 70% (last 20) | Does not open (46%) | 68% | today | 71% |  |
| 34 | [ ] | Pathogenic (STEAM) | 12 | 20 | 60% (14d) | Does not open (81%) | 66% | today | 64% |  |
| 35 | [ ] | Fallout 3: Game of the Year Edition (GOG) | 12 | 24 | 50% (14d) | Does not open (48%) | 72% | today | 75% |  |
| 36 | [ ] | Alabaster Dawn (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (48%) | 87% | 1d ago | 89% |  |
| 37 | [ ] | Deadlock (STEAM) | 15 | 20 | 75% (last 20) | Does not open (51%) | 84% | 2d ago | 84% |  |
| 38 | [ ] | Loftia (STEAM) | 13 | 20 | 65% (last 20) | Does not open (94%) | 70% | 2d ago | 65% |  |
| 39 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (90%) | 89% | 3d ago | 88% |  |
| 40 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 26 | 47 | 55% (since fix) | Does not open (73%) | 60% | 1d ago | 58% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 41 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 14 | 25 | 56% (since fix) | Controller issues (79%) | 74% | today | 75% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 42 | [ ] | Quake (STEAM) | 12 | 20 | 60% (last 20) | Does not open (54%) | 68% | today | 60% |  |
| 43 | [ ] | Look Outside (STEAM) | 11 | 20 | 55% (14d) | Controller issues (64%) | 88% | today | 89% |  |
| 44 | [ ] | Tales of ARISE (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (68%) | 84% | today | 82% |  |
| 45 | [ ] | Mass Effect™ Legendary Edition (STEAM) | 14 | 27 | 52% (since fix) | Does not open (83%) | 82% | 1d ago | 83% |  |
| 46 | [ ] | Dressmaker (STEAM) | 13 | 20 | 65% (last 20) | Does not open (56%) | 75% | 1d ago | 73% |  |
| 47 | [ ] | DOOM 3: BFG Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (74%) | 68% | 2d ago | 68% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 48 | [ ] | Welcome to Elderfield (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 70% | today | 72% |  |
| 49 | [ ] | OMORI (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 65% | today | 60% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 50 | [ ] | Mortal Kombat X (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 92% | 6d ago | 92% |  |
| 51 | [ ] | Aniimo (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 75% | today | 73% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 52 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (70%) | 100% | today | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 53 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 17 | 20 | 85% (last 20) | Does not open (85%) | 69% | 1d ago | 69% |  |
| 54 | [ ] | Barony (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 81% | today | 78% |  |
| 55 | [ ] | Resident Evil 7 Biohazard (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 67% | today | 61% |  |
| 56 | [ ] | Don't Starve Together (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 73% | 1d ago | 69% |  |
| 57 | [ ] | Disco Elysium - The Final Cut (EPIC) | 12 | 20 | 60% (last 20) | Does not open (75%) | 93% | today | 93% |  |
| 58 | [ ] | Batman™: Arkham Origins (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 68% | 3d ago | 64% |  |
| 59 | [ ] | Crypt of the NecroDancer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (45%) | 88% | 2d ago | 87% |  |
| 60 | [ ] | Fallout: New Vegas (EPIC) | 16 | 20 | 80% (last 20) | Does not open (59%) | 74% | 3d ago | 71% |  |
| 61 | [ ] | Rune Factory 3 Special (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 100% | 1d ago | 100% |  |
| 62 | [ ] | Chained Echoes (GOG) | 15 | 20 | 75% (last 20) | Does not open (62%) | 73% | 2d ago | 65% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 63 | [ ] | Devil May Cry 5 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 83% | today | 83% |  |
| 64 | [ ] | FINAL FANTASY (STEAM) | 12 | 20 | 60% (last 20) | Does not open (78%) | 83% | 1d ago | 76% |  |
| 65 | [ ] | Stardew Valley (GOG) | 10 | 20 | 50% (last 20) | Controller issues (60%) | 86% | 1d ago | 83% |  |
| 66 | [ ] | Disgaea 5 Complete (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | 93% | 7d ago | 96% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 67 | [ ] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 12 | 20 | 60% (last 20) | Does not open (59%) | 81% | 1d ago | 84% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 68 | [ ] | LEGO® MARVEL Super Heroes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (65%) | 83% | today | 85% |  |
| 69 | [ ] | Cave Story+ (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | 77% | 2d ago | 76% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 70 | [ ] | Mini Motorways (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 70% | 1d ago | 63% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 71 | [ ] | Little Witch in the Woods (STEAM) | 11 | 20 | 55% (last 20) | Does not open (55%) | 84% | 1d ago | 84% |  |
| 72 | [ ] | POSTAL 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 64% | today | 62% |  |
| 73 | [ ] | Cyberpunk 2077 (GOG) | 11 | 20 | 55% (last 20) | Does not open (70%) | 68% | 1d ago | 67% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 74 | [ ] | Castlevania Dominus Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (91%) | 97% | 2d ago | 96% |  |
| 75 | [ ] | Divinity: Original Sin 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 81% | 2d ago | 78% |  |
| 76 | [ ] | eFootball™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 61% | 6d ago | 57% |  |
| 77 | [ ] | Poppy Playtime (STEAM) | 13 | 20 | 65% (last 20) | Does not open (53%) | 66% | today | 62% |  |
| 78 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (61%) | 92% | 2d ago | 92% |  |
| 79 | [ ] | PAC-MAN Championship Edition DX+ (STEAM) | 10 | 20 | 50% (last 20) | No graphics (59%) | 66% | 3d ago | 57% |  |
| 80 | [ ] | Palia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | 69% | 1d ago | 69% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 81 | [ ] | Minecraft Dungeons II (STEAM) | 15 | 20 | 75% (last 20) | Does not open (80%) | 72% | today | 71% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 82 | [ ] | Grand Theft Auto: Vice City (STEAM) | 14 | 20 | 70% (last 20) | Does not open (43%) | 82% | 1d ago | 82% |  |
| 83 | [ ] | L.A. Noire (STEAM) | 18 | 20 | 90% (last 20) | Does not open (96%) | 62% | 9d ago | 59% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 84 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (52%) | 82% | 3d ago | 82% |  |
| 85 | [ ] | Age of Empires II (2013) (STEAM) | 14 | 20 | 70% (last 20) | Does not open (59%) | 71% | today | 73% |  |
| 86 | [ ] | Doki Doki Literature Club (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 84% | today | 82% |  |
| 87 | [ ] | Titanfall® 2 (STEAM) | 9 | 12 | 75% (since fix) | Does not open (89%) | 71% | 1d ago | 71% |  |
| 88 | [ ] | Call of Duty 4: Modern Warfare (2007) (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (50%) | 65% | 3d ago | 61% |  |
| 89 | [ ] | TBH: Task Bar Hero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 83% | 1d ago | 85% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 90 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 70% | 7d ago | 73% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 91 | [ ] | Dota 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 78% | 1d ago | 80% |  |
| 92 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 97% | 5d ago | 96% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 93 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (78%) | 87% | 6d ago | 82% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 94 | [ ] | The Sims™ 4 (STEAM) | 7 | 14 | 50% (since fix) | Does not open (85%) | 69% | today | 70% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 95 | [ ] | Ratatan (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | 90% | 3d ago | 86% |  |
| 96 | [ ] | Mortal Kombat 11 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | 63% | 4d ago | 73% |  |
| 97 | [ ] | Resident Evil Village (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 83% | 1d ago | 83% |  |
| 98 | [ ] | Tails of Iron (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 87% | 2d ago | 90% |  |
| 99 | [ ] | SONIC X SHADOW GENERATIONS (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 77% | today | 78% |  |
| 100 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 100% | 1d ago | 100% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 101 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (42%) | 73% | today | 73% |  |
| 102 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 17 | 20 | 85% (last 20) | Controller issues (88%) | 96% | today | 97% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 103 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (41%) | 87% | 1d ago | 87% |  |
| 104 | [ ] | Fable - The Lost Chapters (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (48%) | 79% | 1d ago | 83% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 105 | [ ] | American Truck Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 71% | 1d ago | 70% |  |
| 106 | [ ] | Fate/stay night REMASTERED (STEAM) | 11 | 20 | 55% (last 20) | No graphics (48%) | 91% | 2d ago | 92% |  |
| 107 | [ ] | Moonstone Island (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (69%) | 80% | today | 77% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 108 | [ ] | Unturned (STEAM) | 13 | 20 | 65% (last 20) | Does not open (47%) | 82% | today | 84% |  |
| 109 | [ ] | Astral Party  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 89% | 4d ago | 86% |  |
| 110 | [ ] | Minecraft Dungeons (STEAM) | 11 | 20 | 55% (last 20) | Does not open (76%) | 77% | 3d ago | 76% |  |
| 111 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 89% | 5d ago | 83% |  |
| 112 | [ ] | MIO: Memories in Orbit (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (61%) | 94% | 1d ago | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 113 | [ ] | Abiotic Factor (STEAM) | 10 | 20 | 50% (last 20) | Does not open (74%) | 79% | 7d ago | 84% |  |
| 114 | [ ] | Last Epoch (STEAM) | 10 | 20 | 50% (last 20) | Does not open (81%) | 62% | today | 61% |  |
| 115 | [ ] | ZERO Sievert (STEAM) | 10 | 20 | 50% (last 20) | Does not open (86%) | 84% | today | 82% |  |
| 116 | [ ] | A Plague Tale: Innocence (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | 68% | 8d ago | 68% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 117 | [ ] | Sid Meier's Civilization V (STEAM) | 15 | 20 | 75% (last 20) | Does not open (80%) | 63% | 4d ago | 56% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 118 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 15 | 20 | 75% (last 20) | Does not open (71%) | 82% | 2d ago | 79% |  |
| 119 | [ ] | Call of Duty: World at War (STEAM) | 13 | 20 | 65% (last 20) | Does not open (40%) | 74% | 2d ago | 66% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 120 | [ ] | Need for Speed™ Rivals (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 75% | 1d ago | 75% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 121 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (84%) | 67% | 3d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 122 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 69% | 17d ago | 82% |  |
| 123 | [ ] | Caravan SandWitch (EPIC) | 10 | 20 | 50% (last 20) | Does not open (71%) | 63% | 2d ago | 65% |  |
| 124 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | 83% | 15d ago | 83% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 125 | [ ] | PlateUp! (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 78% | 4d ago | 73% |  |
| 126 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | 94% | 10d ago | 93% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 127 | [ ] | Ultimate Custom Night (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | 64% | 1d ago | 58% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 128 | [ ] | Legacy of Kain: Defiance Remastered (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (69%) | 80% | 2d ago | n/a |  |
| 129 | [ ] | Street Fighter™ 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | 82% | 2d ago | 80% |  |
| 130 | [ ] | Watch Dogs 2 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (80%) | 67% | today | 63% | [#399](https://github.com/GameNative/gamenative-compat/issues/399) |
| 131 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (70%) | 82% | 1d ago | 83% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 132 | [ ] | Sonic Generations (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 66% | today | 63% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 133 | [ ] | Stellar Blade™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | 82% | 3d ago | 83% |  |
| 134 | [ ] | Gothic 1 Classic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (58%) | 64% | today | 62% |  |
| 135 | [ ] | Yakuza: Like a Dragon (STEAM) | 13 | 20 | 65% (last 20) | Does not open (60%) | 70% | 1d ago | 76% |  |
| 136 | [ ] | Oxygen Not Included (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 69% | today | 74% |  |
| 137 | [ ] | Stumble Guys (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 62% | 2d ago | 61% |  |
| 138 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 11 | 20 | 55% (last 20) | Does not open (59%) | 89% | 2d ago | 89% |  |
| 139 | [ ] | OCTOPATH TRAVELER 0 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (77%) | 90% | 3d ago | 92% |  |
| 140 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (79%) | 75% | 1d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 141 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (87%) | 89% | 6d ago | 94% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 142 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 66% | 13d ago | 67% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 143 | [ ] | Tabletop Simulator (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 79% | 5d ago | 81% |  |
| 144 | [ ] | Max Payne (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (45%) | 81% | today | 80% |  |
| 145 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 94% | today | 93% |  |
| 146 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (83%) | 60% | 14d ago | n/a |  |
| 147 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 75% | today | 76% |  |
| 148 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (48%) | 78% | today | 75% |  |
| 149 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | 85% | 11d ago | 83% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 150 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (80%) | 81% | today | 82% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 151 | [ ] | Gambonanza (STEAM) | 14 | 20 | 70% (last 20) | Does not open (60%) | 87% | today | 86% |  |
| 152 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (66%) | 78% | today | 73% |  |
| 153 | [ ] | Pinball FX (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 70% | 7d ago | 65% |  |
| 154 | [ ] | Sovereign Tower (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 75% | 1d ago | 78% |  |
| 155 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 83% | 17d ago | 83% |  |
| 156 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | No graphics (47%) | 86% | 1d ago | 86% |  |
| 157 | [ ] | Plague Inc: Evolved (STEAM) | 13 | 20 | 65% (last 20) | Does not open (58%) | 67% | 3d ago | 64% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 158 | [ ] | Trailmakers (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | 94% | 3d ago | 92% |  |
| 159 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (60%) | 92% | 2d ago | 90% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 160 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (92%) | 65% | 4d ago | 77% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 161 | [ ] | Sonic Lost World (STEAM) | 10 | 20 | 50% (last 20) | No graphics (69%) | 79% | 3d ago | 82% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 162 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (54%) | 73% | 8d ago | 74% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 163 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (59%) | 67% | 12d ago | 65% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 164 | [ ] | Necesse (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 62% | 2d ago | 63% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 165 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (82%) | 87% | 5d ago | 89% |  |
| 166 | [ ] | Digimon Survive (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (77%) | 86% | 2d ago | 85% |  |
| 167 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 60% | today | 59% |  |
| 168 | [ ] | Fallout (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 65% | 5d ago | 66% |  |
| 169 | [ ] | Heavy Rain (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (65%) | 90% | today | 91% |  |
| 170 | [ ] | Raft (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | 93% | 2d ago | 90% |  |
| 171 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 67% | 12d ago | 67% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 172 | [ ] | Supermarket Together (STEAM) | 15 | 20 | 75% (last 20) | Does not open (67%) | 60% | 1d ago | 62% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 173 | [ ] | Changed (STEAM) | 15 | 20 | 75% (last 20) | Does not open (62%) | 65% | 11d ago | 60% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 174 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (43%) | 66% | 3d ago | 65% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 175 | [ ] | Control Ultimate Edition (GOG) | 13 | 20 | 65% (last 20) | Does not open (76%) | 71% | 13d ago | 67% |  |
| 176 | [ ] | Grim Dawn (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 60% | today | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 177 | [ ] | My Summer Car (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 73% | today | 67% |  |
| 178 | [ ] | One-armed robber (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (69%) | 65% | today | 59% |  |
| 179 | [ ] | Dishonored 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 66% | 4d ago | 61% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 180 | [ ] | METAL SLUG 3 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (81%) | 63% | today | 65% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 181 | [ ] | Overwatch® (STEAM) | 8 | 11 | 73% (since fix) | Does not open (61%) | 82% | 1d ago | 79% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 182 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | 73% | 13d ago | 67% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 183 | [ ] | Capcom Arcade Stadium (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | 77% | 11d ago | 80% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 184 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 100% | 34d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 185 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | 88% | 1d ago | 84% |  |
| 186 | [ ] | Hylics (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (74%) | 90% | 1d ago | 86% |  |
| 187 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (76%) | 100% | 14d ago | n/a |  |
| 188 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 73% | 2d ago | 68% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 189 | [ ] | HELLDIVERS™ (STEAM) | 12 | 20 | 60% (last 20) | Does not open (78%) | 62% | 5d ago | 62% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 190 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (67%) | 93% | 2d ago | 94% |  |
| 191 | [ ] | Warframe (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 79% | today | 78% |  |
| 192 | [ ] | TurretGirls (STEAM) | 12 | 20 | 60% (last 20) | No graphics (77%) | 100% | 4d ago | 100% |  |
| 193 | [ ] | Escape from Duckov (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (70%) | 97% | 5d ago | 98% |  |
| 194 | [ ] | Limbus Company (STEAM) | 11 | 20 | 55% (last 20) | Does not open (82%) | 88% | today | 93% |  |
| 195 | [ ] | BioShock 2 Remastered (STEAM) | 10 | 20 | 50% (last 20) | Does not open (83%) | 85% | today | 85% |  |
| 196 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | 75% | 5d ago | 72% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 197 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (71%) | 85% | 6d ago | 83% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 198 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (75%) | 71% | 7d ago | 65% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 199 | [ ] | Subnautica 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (55%) | 73% | today | 80% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 200 | [ ] | Return to Monkey Island (STEAM) | 15 | 20 | 75% (last 20) | No graphics (74%) | 72% | today | 72% |  |
| 201 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 14 | 20 | 70% (last 20) | Does not open (80%) | 64% | 1d ago | 62% |  |
| 202 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (59%) | 72% | 2d ago | 75% |  |
| 203 | [ ] | Moonring (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 81% | 4d ago | 77% |  |
| 204 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 95% | 13d ago | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 205 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 75% | 18d ago | 60% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 206 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (65%) | 79% | 1d ago | 73% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 207 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | 75% | today | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 208 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (61%) | 73% | 13d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 209 | [ ] | Turbo Overkill (STEAM) | 13 | 20 | 65% (last 20) | No graphics (91%) | 100% | 2d ago | 100% |  |
| 210 | [ ] | Resident Evil Revelations 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (55%) | 82% | 1d ago | 83% |  |
| 211 | [ ] | POSTAL: Brain Damaged (STEAM) | 16 | 20 | 80% (last 20) | Does not open (91%) | 80% | today | n/a |  |
| 212 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (91%) | 81% | 37d ago | 73% |  |
| 213 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 75% | 27d ago | 75% |  |
| 214 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Graphics glitches (50%) | 73% | today | 70% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 215 | [ ] | Hotline Miami (GOG) | 13 | 20 | 65% (last 20) | Does not open (89%) | 73% | today | 75% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 216 | [ ] | GOD EATER RESURRECTION (STEAM) | 13 | 20 | 65% (last 20) | Does not open (56%) | 86% | today | n/a |  |
| 217 | [ ] | GUILTY GEAR Xrd REV 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (83%) | 65% | 9d ago | 59% |  |
| 218 | [ ] | CS2D (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 60% | 1d ago | n/a |  |
| 219 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (64%) | 77% | 12d ago | 77% |  |
| 220 | [ ] | MX Bikes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 96% | 6d ago | 95% |  |
| 221 | [ ] | No Socks RPG (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (91%) | 93% | 2d ago | 93% |  |
| 222 | [ ] | Bongo Cat (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 64% | 3d ago | 53% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 223 | [ ] | Invisible, Inc. (STEAM) | 14 | 20 | 70% (last 20) | Does not open (63%) | 92% | 1d ago | n/a |  |
| 224 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 93% | 14d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 225 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (82%) | 81% | 7d ago | 82% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 226 | [ ] | Big Walk (STEAM) | 12 | 20 | 60% (last 20) | Does not open (52%) | 60% | 4d ago | 58% |  |
| 227 | [ ] | SnowRunner (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 72% | 1d ago | 73% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 228 | [ ] | Darksiders (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 85% | 1d ago | 85% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 229 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 95% | today | 100% |  |
| 230 | [ ] | AER Memories of Old (EPIC) | 13 | 20 | 65% (last 20) | Does not open (86%) | 93% | 8d ago | 92% |  |
| 231 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (71%) | 67% | 9d ago | 67% |  |
| 232 | [ ] | Capcom Fighting Collection (STEAM) | 13 | 20 | 65% (last 20) | Does not open (86%) | 90% | 4d ago | 88% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 233 | [ ] | BATTLETECH (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 96% | 8d ago | 94% |  |
| 234 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (50%) | 83% | 3d ago | 93% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 235 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 93% | 16d ago | n/a |  |
| 236 | [ ] | Secrets of Grindea (STEAM) | 10 | 20 | 50% (last 20) | Does not open (48%) | 80% | 6d ago | 81% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 237 | [ ] | Zero Escape: The Nonary Games (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 67% | 3d ago | 68% |  |
| 238 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 76% | 1d ago | 77% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 239 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 79% | 1d ago | 77% |  |
| 240 | [ ] | Spark the Electric Jester (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 75% | 3d ago | n/a | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 241 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (84%) | 60% | 4d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 242 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (94%) | 94% | 15d ago | 93% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 243 | [ ] | Tales of Zestiria (STEAM) | 13 | 20 | 65% (last 20) | Does not open (77%) | 73% | 1d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 244 | [ ] | SILENT HILL 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 100% | today | 100% |  |
| 245 | [ ] | Sid Meier's Civilization VI (EPIC) | 13 | 20 | 65% (last 20) | Does not open (58%) | 60% | today | 52% |  |
| 246 | [ ] | Timberborn (STEAM) | 12 | 20 | 60% (last 20) | No graphics (70%) | 100% | 5d ago | 100% |  |
| 247 | [ ] | Goose Goose Duck (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 82% | 4d ago | 81% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 248 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 12 | 20 | 60% (last 20) | No graphics (39%) | 86% | 7d ago | 90% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 249 | [ ] | Mafia II (Classic) (GOG) | 12 | 20 | 60% (last 20) | Does not open (100%) | 60% | 1d ago | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 250 | [ ] | 12 is Better Than 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 73% | 19d ago | n/a |  |
| 251 | [ ] | Deus Ex™ GOTY Edition (GOG) | 11 | 20 | 55% (last 20) | No graphics (47%) | 100% | 2d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 252 | [ ] | Super Battle Golf (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 89% | 1d ago | 87% |  |
| 253 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 82% | 10d ago | 78% |  |
| 254 | [ ] | Rollout Inline (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 71% | 4d ago | 75% |  |
| 255 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 93% | today | 90% |  |
| 256 | [ ] | HITMAN World of Assassination (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 74% | 3d ago | 75% |  |
| 257 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 67% | today | 71% |  |
| 258 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 13 | 20 | 65% (last 20) | Does not open (85%) | 78% | 2d ago | 91% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 259 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 92% | 35d ago | 92% |  |
| 260 | [ ] | Portal: Revolution (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (100%) | 93% | today | 92% |  |
| 261 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 68% | 11d ago | 69% |  |
| 262 | [ ] | Disgaea 4 Complete+ (STEAM) | 12 | 20 | 60% (last 20) | No graphics (40%) | 93% | 1d ago | 92% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 263 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 68% | 15d ago | 67% |  |
| 264 | [ ] | Sons Of The Forest (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 74% | 9d ago | 72% |  |
| 265 | [ ] | Forgive Me Father (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 72% | today | 58% |  |
| 266 | [ ] | Cat Mail Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (91%) | 91% | today | 90% |  |
| 267 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 93% | 12d ago | 90% |  |
| 268 | [ ] | CRUEL (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 83% | 9d ago | 82% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 269 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 94% | 9d ago | 100% |  |
| 270 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 71% | 8d ago | 83% |  |
| 271 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 93% | 6d ago | 93% |  |
| 272 | [ ] | Hitman: Contracts (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (82%) | 67% | 1d ago | 64% |  |
| 273 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 86% | 1d ago | 82% |  |
| 274 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (40%) | 60% | 12d ago | 82% |  |
| 275 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 82% | today | 81% |  |
| 276 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 83% | 9d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 277 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 67% | 5d ago | 71% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 278 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 75% | 8d ago | 75% |  |
| 279 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 64% | 7d ago | 64% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 280 | [ ] | Assetto Corsa Competizione (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 88% | 1d ago | 86% |  |
| 281 | [ ] | BioShock 2 Remastered (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 81% | 4d ago | 76% |  |
| 282 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | No graphics (58%) | 90% | 26d ago | n/a | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 283 | [ ] | Sort Them Ducks (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (64%) | 100% | 1d ago | 100% |  |
| 284 | [ ] | Cruelty Squad (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 86% | today | 83% |  |
| 285 | [ ] | Dungeon Siege (STEAM) | 10 | 20 | 50% (last 20) | No graphics (50%) | 100% | 3d ago | 100% |  |
| 286 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 71% | 17d ago | 67% |  |
| 287 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (65%) | 90% | 3d ago | 91% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 288 | [ ] | Command & Conquer™ Red Alert™ 3 (STEAM) | 10 | 20 | 50% (last 20) | No graphics (38%) | 92% | 2d ago | 90% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 289 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 100% | 2d ago | 100% |  |
| 290 | [ ] | Haydee (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 83% | 9d ago | 90% |  |
| 291 | [ ] | Pillars of Eternity (STEAM) | 10 | 20 | 50% (last 20) | Does not open (40%) | 100% | 3d ago | 100% |  |
| 292 | [ ] | Spirit City: Lofi Sessions (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 69% | 1d ago | 69% |  |

## Recently recovered (365)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Grim Dawn (STEAM) | 458 | 2026-11-08 | 540 | 68% |  |
| 2 | [x] | Half-Life (STEAM) | 372 | 2026-11-09 | 639 | 71% |  |
| 3 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 265 | 2026-11-14 | 422 | 71% |  |
| 4 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 243 | 2026-11-09 | 337 | 87% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 5 | [x] | MONSTER HUNTER RISE (STEAM) | 228 | 2026-11-17 | 532 | 61% |  |
| 6 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 219 | 2026-11-09 | 372 | 64% |  |
| 7 | [x] | Alan Wake (STEAM) | 217 | 2026-11-14 | 244 | 78% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 8 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 183 | 2026-11-09 | 224 | 54% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 9 | [x] | BeamNG.drive (STEAM) | 179 | 2026-11-09 | 223 | 65% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 10 | [x] | OMORI (STEAM) | 168 | 2026-11-09 | 214 | 65% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 11 | [x] | DRAGON BALL FighterZ (STEAM) | 163 | 2026-11-01 | 213 | 87% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 12 | [x] | Geometry Dash (STEAM) | 161 | 2026-11-11 | 451 | 64% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 13 | [x] | Call of Duty: Black Ops (STEAM) | 156 | 2026-11-13 | 182 | 23% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 14 | [x] | BioShock (STEAM) | 145 | 2026-11-09 | 295 | 71% |  |
| 15 | [x] | Spelunky 2 (STEAM) | 143 | 2026-11-01 | 191 | 85% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 16 | [x] | Sid Meier's Civilization V (STEAM) | 140 | 2026-11-10 | 152 | 63% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 17 | [x] | Team Fortress 2 (STEAM) | 138 | 2026-11-09 | 239 | 77% |  |
| 18 | [x] | Minecraft Dungeons II (STEAM) | 133 | 2026-11-09 | 152 | 72% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 19 | [x] | Prototype (STEAM) | 132 | 2026-11-11 | 199 | 61% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 20 | [x] | Castlevania Advance Collection (STEAM) | 127 | 2026-11-09 | 203 | 86% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 21 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 127 | 2026-11-23 | 174 | 60% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 22 | [x] | Euro Truck Simulator 2 (STEAM) | 120 | 2026-11-23 | 216 | 62% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 23 | [x] | Aniimo (STEAM) | 117 | 2026-11-09 | 158 | 75% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 24 | [x] | Mirror's Edge (STEAM) | 110 | 2026-11-09 | 166 | 68% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 25 | [x] | Assassin's Creed II (STEAM) | 107 | 2026-11-10 | 112 | 70% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 26 | [x] | Cave Story+ (STEAM) | 103 | 2026-11-09 | 113 | 77% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 27 | [x] | Necesse (STEAM) | 102 | 2026-11-22 | 112 | 62% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 28 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 99 | 2026-11-09 | 140 | 90% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 29 | [x] | The Witcher: Enhanced Edition (STEAM) | 99 | 2026-11-09 | 118 | 79% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 30 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 91 | 2026-11-15 | 136 | 84% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 31 | [x] | Moonstone Island (STEAM) | 91 | 2026-11-09 | 119 | 80% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 32 | [x] | Fallout: New Vegas PCR (STEAM) | 85 | 2026-11-20 | 113 | 67% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 33 | [x] | FINAL FANTASY XIII-2 (STEAM) | 80 | 2026-11-09 | 83 | 65% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 34 | [x] | DOOM 3: BFG Edition (STEAM) | 79 | 2026-11-09 | 122 | 68% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 35 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 78 | 2026-11-09 | 128 | 75% |  |
| 36 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 77 | 2026-11-23 | 99 | 61% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 37 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 76 | 2026-11-09 | 100 | 96% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 38 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 75 | 2026-11-09 | 116 | 76% |  |
| 39 | [x] | Psychonauts (STEAM) | 74 | 2026-11-09 | 141 | 92% |  |
| 40 | [x] | Vital Shell (STEAM) | 74 | 2026-11-09 | 123 | 85% |  |
| 41 | [x] | Cyberpunk 2077 (GOG) | 72 | 2026-11-09 | 96 | 68% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 42 | [x] | Brawlhalla (STEAM) | 70 | 2026-11-09 | 137 | 72% |  |
| 43 | [x] | The Sims™ 4 (STEAM) | 70 | 2026-11-09 | 95 | 69% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 44 | [x] | Age of Empires II: Definitive Edition (STEAM) | 70 | 2026-11-10 | 89 | 62% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 45 | [x] | Ballionaire (STEAM) | 69 | 2026-11-09 | 119 | 82% |  |
| 46 | [x] | Order of the Sinking Star (STEAM) | 69 | 2026-11-09 | 107 | 66% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 47 | [x] | Dota 2 (STEAM) | 66 | 2026-11-09 | 100 | 78% |  |
| 48 | [x] | Stardew Valley (GOG) | 65 | 2026-11-11 | 117 | 86% |  |
| 49 | [x] | Fable - The Lost Chapters (STEAM) | 65 | 2026-11-09 | 108 | 79% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 50 | [x] | American Truck Simulator (STEAM) | 65 | 2026-11-09 | 105 | 71% |  |
| 51 | [x] | Disgaea 5 Complete (STEAM) | 65 | 2026-11-09 | 76 | 93% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 52 | [x] | Need for Speed: Hot Pursuit (STEAM) | 64 | 2026-11-09 | 98 | 76% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 53 | [x] | Diablo® IV (STEAM) | 63 | 2026-11-11 | 75 | 83% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 54 | [x] | Grand Theft Auto V (EPIC) | 63 | 2026-11-09 | 67 | 77% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 55 | [x] | GRID (STEAM) | 62 | 2026-11-21 | 83 | 47% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 56 | [x] | Mini Motorways (STEAM) | 60 | 2026-11-09 | 94 | 70% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 57 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 60 | 2026-11-11 | 80 | 61% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 58 | [x] | Spyro™ Reignited Trilogy (STEAM) | 59 | 2026-11-09 | 106 | 80% |  |
| 59 | [x] | Poppy Playtime (STEAM) | 58 | 2026-11-09 | 99 | 66% |  |
| 60 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 58 | 2026-10-25 | 99 | 81% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 61 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 58 | 2026-11-09 | 96 | 85% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 62 | [x] | Sovereign Tower (STEAM) | 57 | 2026-11-09 | 113 | 75% |  |
| 63 | [x] | Borderlands 3 (STEAM) | 57 | 2026-11-09 | 87 | 91% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 64 | [x] | Gunfire Reborn (STEAM) | 57 | 2026-11-09 | 63 | 89% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 65 | [x] | FINAL FANTASY XIII (STEAM) | 56 | 2026-11-22 | 514 | 65% |  |
| 66 | [x] | Quake (STEAM) | 56 | 2026-11-09 | 185 | 68% |  |
| 67 | [x] | Call of Duty: World at War (STEAM) | 55 | 2026-11-09 | 78 | 74% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 68 | [x] | Call of Juarez Gunslinger (STEAM) | 55 | 2026-11-09 | 68 | 66% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 69 | [x] | A Plague Tale: Innocence (STEAM) | 55 | 2026-11-09 | 58 | 68% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 70 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 54 | 2026-11-09 | 90 | 70% |  |
| 71 | [x] | Fallout (STEAM) | 54 | 2026-11-09 | 87 | 65% |  |
| 72 | [x] | Firewatch (STEAM) | 53 | 2026-11-10 | 107 | 89% |  |
| 73 | [x] | Sonic Generations (STEAM) | 53 | 2026-11-09 | 61 | 66% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 74 | [x] | Caravan SandWitch (EPIC) | 52 | 2026-11-09 | 112 | 63% |  |
| 75 | [x] | STEINS;GATE (STEAM) | 52 | 2026-11-09 | 81 | 81% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 76 | [x] | Last Epoch (STEAM) | 52 | 2026-11-09 | 77 | 62% |  |
| 77 | [x] | MIO: Memories in Orbit (STEAM) | 50 | 2026-11-09 | 103 | 94% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 78 | [x] | eFootball™ (STEAM) | 50 | 2026-11-09 | 75 | 61% |  |
| 79 | [x] | Starbound (STEAM) | 49 | 2026-11-09 | 82 | 87% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 80 | [x] | Darksiders (STEAM) | 49 | 2026-11-09 | 65 | 85% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 81 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 49 | 2026-11-09 | 55 | 100% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 82 | [x] | Moonlighter (EPIC) | 49 | 2026-11-09 | 53 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 83 | [x] | Okami HD (STEAM) | 48 | 2026-11-09 | 90 | 95% |  |
| 84 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 48 | 2026-11-17 | 73 | 66% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 85 | [x] | HELLDIVERS™ (STEAM) | 48 | 2026-11-23 | 60 | 62% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 86 | [x] | METAL SLUG 3 (STEAM) | 47 | 2026-11-24 | 61 | 63% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 87 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 46 | 2026-11-09 | 80 | 53% |  |
| 88 | [x] | TBH: Task Bar Hero (STEAM) | 46 | 2026-11-09 | 72 | 83% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 89 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 45 | 2026-11-09 | 80 | 85% |  |
| 90 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 45 | 2026-11-13 | 75 | 65% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 91 | [x] | Sol Cesto (EPIC) | 45 | 2026-11-09 | 45 | 87% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 92 | [x] | Oxygen Not Included (STEAM) | 44 | 2026-11-11 | 77 | 69% |  |
| 93 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 44 | 2026-11-09 | 64 | 74% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 94 | [x] | Overwatch® (STEAM) | 44 | 2026-11-10 | 49 | 82% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 95 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 43 | 2026-11-09 | 66 | 87% |  |
| 96 | [x] | ROB RUN (STEAM) | 41 | 2026-11-17 | 58 | 67% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 97 | [x] | Darkest Dungeon® (EPIC) | 40 | 2026-11-09 | 80 | 88% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 98 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 40 | 2026-11-09 | 68 | 56% |  |
| 99 | [x] | Borderlands: The Pre-Sequel (STEAM) | 39 | 2026-11-09 | 77 | 61% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 100 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 39 | 2026-11-09 | 68 | 83% |  |
| 101 | [x] | Digimon World: Next Order (STEAM) | 38 | 2026-11-09 | 74 | 86% |  |
| 102 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 38 | 2026-11-09 | 69 | 87% |  |
| 103 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 38 | 2026-11-09 | 61 | 68% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 104 | [x] | Sonic Lost World (STEAM) | 38 | 2026-11-09 | 58 | 79% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 105 | [x] | Age of Empires II (2013) (STEAM) | 37 | 2026-11-09 | 62 | 71% |  |
| 106 | [x] | Grim Dawn (GOG) | 37 | 2026-11-24 | 61 | 60% | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 107 | [x] | Aggelos (STEAM) | 37 | 2026-11-09 | 53 | 81% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 108 | [x] | CrossCode (GOG) | 36 | 2026-11-09 | 39 | 75% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 109 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 36 | 2026-11-19 | 38 | 94% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 110 | [x] | Amnesia: The Dark Descent (STEAM) | 35 | 2026-11-09 | 74 | 84% |  |
| 111 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 35 | 2026-11-09 | 66 | 82% |  |
| 112 | [x] | Street Fighter™ 6 (STEAM) | 35 | 2026-11-09 | 56 | 82% |  |
| 113 | [x] | L.A. Noire (STEAM) | 35 | 2026-11-24 | 42 | 62% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 114 | [x] | Russian Fishing 4 (STEAM) | 35 | 2026-11-09 | 41 | 71% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 115 | [x] | Monster Hunter Wilds (STEAM) | 35 | 2026-11-09 | 36 | 85% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 116 | [x] | POSTAL 2 (GOG) | 34 | 2026-11-09 | 66 | 95% |  |
| 117 | [x] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 34 | 2026-11-20 | 64 | 15% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 118 | [x] | Tomb Raider: Anniversary (STEAM) | 34 | 2026-11-09 | 62 | 64% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 119 | [x] | Dead by Daylight (STEAM) | 34 | 2026-11-09 | 38 | 82% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 120 | [x] | Being a DIK (STEAM) | 33 | 2026-11-09 | 73 | 71% |  |
| 121 | [x] | Sonic Origins (STEAM) | 33 | 2026-11-09 | 61 | 78% |  |
| 122 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 33 | 2026-11-09 | 60 | 75% |  |
| 123 | [x] | XCOM 2 (STEAM) | 33 | 2026-11-09 | 59 | 68% |  |
| 124 | [x] | Max Payne (STEAM) | 33 | 2026-11-09 | 56 | 81% |  |
| 125 | [x] | Plague Inc: Evolved (STEAM) | 33 | 2026-11-16 | 53 | 67% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 126 | [x] | Breathedge (STEAM) | 33 | 2026-11-23 | 51 | 63% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 127 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 33 | 2026-11-09 | 41 | 92% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 128 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 32 | 2026-11-09 | 71 | 70% |  |
| 129 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 32 | 2026-11-09 | 64 | 89% |  |
| 130 | [x] | Ace Attorney Investigations Collection (STEAM) | 32 | 2026-11-09 | 60 | 88% |  |
| 131 | [x] | FINAL FANTASY VII (2013) (STEAM) | 32 | 2026-11-09 | 49 | 55% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 132 | [x] | SnowRunner (STEAM) | 32 | 2026-11-09 | 43 | 72% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 133 | [x] | Capcom Arcade Stadium (STEAM) | 32 | 2026-11-09 | 42 | 77% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 134 | [x] | Journey (STEAM) | 31 | 2026-10-27 | 72 | 79% |  |
| 135 | [x] | Hearts of Iron IV (STEAM) | 31 | 2026-11-09 | 66 | 80% |  |
| 136 | [x] | COCOON (STEAM) | 31 | 2026-11-09 | 64 | 81% |  |
| 137 | [x] | Yume Nikki (STEAM) | 31 | 2026-11-20 | 57 | 48% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 138 | [x] | Earthion (STEAM) | 31 | 2026-11-09 | 53 | 100% |  |
| 139 | [x] | Gauntlet™  (STEAM) | 31 | 2026-11-11 | 46 | n/a | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 140 | [x] | Red Dead Redemption (STEAM) | 31 | 2026-11-09 | 34 | 34% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 141 | [x] | DOOM 64 (EPIC) | 30 | 2026-11-24 | 116 | 43% |  |
| 142 | [x] | The Bazaar (STEAM) | 30 | 2026-11-09 | 60 | 79% |  |
| 143 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 30 | 2026-11-09 | 55 | 73% |  |
| 144 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 30 | 2026-11-09 | 50 | 72% |  |
| 145 | [x] | Resident Evil Village (STEAM) | 30 | 2026-11-09 | 50 | 83% |  |
| 146 | [x] | Need for Speed™ Rivals (STEAM) | 30 | 2026-11-10 | 44 | 75% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 147 | [x] | Elite Dangerous (STEAM) | 30 | 2026-11-20 | 30 | 67% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 148 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 29 | 2026-11-09 | 52 | 87% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 149 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 29 | 2026-11-09 | 50 | 94% |  |
| 150 | [x] | Big Walk (STEAM) | 29 | 2026-11-09 | 49 | 60% |  |
| 151 | [x] | Prince of Persia: The Sands of Time (STEAM) | 29 | 2026-11-09 | 49 | 78% |  |
| 152 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 29 | 2026-11-09 | 43 | 82% |  |
| 153 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 73% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 154 | [x] | SurrounDead (STEAM) | 28 | 2026-11-09 | 59 | 90% |  |
| 155 | [x] | Hero Siege (STEAM) | 28 | 2026-11-09 | 49 | 85% |  |
| 156 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 28 | 2026-11-09 | 48 | 93% |  |
| 157 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 28 | 2026-11-09 | 45 | 68% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 158 | [x] | Hotline Miami (GOG) | 28 | 2026-11-18 | 36 | 73% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 159 | [x] | Gothic II: Gold Classic (STEAM) | 28 | 2026-11-09 | 36 | 75% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 160 | [x] | Resident Evil Revelations 2 (STEAM) | 27 | 2026-11-09 | 53 | 82% |  |
| 161 | [x] | Heavy Rain (STEAM) | 27 | 2026-11-09 | 48 | 90% |  |
| 162 | [x] | Secrets of Grindea (STEAM) | 27 | 2026-11-09 | 46 | 80% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 163 | [x] | Tower and Sword of Succubus (STEAM) | 27 | 2026-11-09 | 41 | 81% |  |
| 164 | [x] | Digimon Survive (STEAM) | 27 | 2026-11-09 | 40 | 86% |  |
| 165 | [x] | Supermarket Together (STEAM) | 27 | 2026-11-18 | 40 | 60% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 166 | [x] | Palia (STEAM) | 27 | 2026-11-09 | 38 | 69% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 167 | [x] | Cat Mail Co. (STEAM) | 26 | 2026-11-09 | 44 | 91% |  |
| 168 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 44 | 67% |  |
| 169 | [x] | Dead Rising 2 (STEAM) | 26 | 2026-11-09 | 42 | 69% |  |
| 170 | [x] | Yakuza: Like a Dragon (STEAM) | 26 | 2026-11-09 | 42 | 70% |  |
| 171 | [x] | Frostpunk (STEAM) | 25 | 2026-11-09 | 52 | 82% |  |
| 172 | [x] | Deponia (STEAM) | 25 | 2026-11-09 | 49 | 86% |  |
| 173 | [x] | My Summer Car (STEAM) | 25 | 2026-11-09 | 39 | 73% |  |
| 174 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-19 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 175 | [x] | Skullgirls 2nd Encore (STEAM) | 24 | 2026-11-10 | 61 | 70% |  |
| 176 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 24 | 2026-11-09 | 58 | 83% |  |
| 177 | [x] | Chained Echoes (GOG) | 24 | 2026-11-19 | 52 | 73% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 178 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 24 | 2026-11-09 | 48 | 59% |  |
| 179 | [x] | Lobotomy Corporation (STEAM) | 24 | 2026-11-09 | 47 | 92% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 180 | [x] | Mirror's Edge™ (GOG) | 24 | 2026-11-13 | 46 | 82% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 181 | [x] | Unturned (STEAM) | 24 | 2026-11-09 | 42 | 82% |  |
| 182 | [x] | Trailmakers (STEAM) | 24 | 2026-11-09 | 41 | 94% |  |
| 183 | [x] | Gambonanza (STEAM) | 24 | 2026-11-09 | 40 | 87% |  |
| 184 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 24 | 2026-11-09 | 39 | 82% |  |
| 185 | [x] | Ratatan (STEAM) | 24 | 2026-11-09 | 37 | 90% |  |
| 186 | [x] | Subnautica 2 (STEAM) | 24 | 2026-11-15 | 30 | 73% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 187 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 44 | 94% |  |
| 188 | [x] | Opus Magnum (STEAM) | 23 | 2026-11-09 | 36 | 100% |  |
| 189 | [x] | Dishonored 2 (STEAM) | 23 | 2026-11-09 | 34 | 66% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 190 | [x] | Ultimate Custom Night (STEAM) | 23 | 2026-11-19 | 33 | 64% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 191 | [x] | Jade Empire: Special Edition (GOG) | 23 | 2026-11-09 | 30 | 73% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 192 | [x] | Crab Game (STEAM) | 23 | 2026-11-09 | 27 | 73% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 193 | [x] | Football Manager 2024 (EPIC) | 22 | 2026-11-09 | 40 | 62% |  |
| 194 | [x] | Guildrun Demo (STEAM) | 22 | 2026-11-09 | 38 | 83% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 195 | [x] | Strider (STEAM) | 22 | 2026-11-20 | 38 | 67% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 196 | [x] | Titanfall® 2 (STEAM) | 22 | 2026-11-09 | 37 | 71% |  |
| 197 | [x] | Mortal Kombat 11 (STEAM) | 22 | 2026-11-09 | 33 | 63% |  |
| 198 | [x] | Timberborn (STEAM) | 22 | 2026-11-09 | 33 | 100% |  |
| 199 | [x] | Changed (STEAM) | 22 | 2026-11-23 | 32 | 65% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 200 | [x] | Tearscape (STEAM) | 22 | 2026-11-09 | 26 | 79% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 201 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 22 | 2026-11-09 | 25 | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 202 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 58 | 97% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 203 | [x] | Prince of Persia (GOG) | 21 | 2026-11-09 | 42 | 73% |  |
| 204 | [x] | Battle Brothers (STEAM) | 21 | 2026-11-09 | 41 | 80% |  |
| 205 | [x] | Invisible, Inc. (STEAM) | 21 | 2026-11-09 | 38 | 92% |  |
| 206 | [x] | Control Ultimate Edition (GOG) | 21 | 2026-11-09 | 37 | 71% |  |
| 207 | [x] | Limbus Company (STEAM) | 21 | 2026-11-09 | 35 | 88% |  |
| 208 | [x] | Return to Monkey Island (STEAM) | 21 | 2026-11-09 | 33 | 72% |  |
| 209 | [x] | Goose Goose Duck (STEAM) | 21 | 2026-11-18 | 30 | 82% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 210 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 88% |  |
| 211 | [x] | Sapphire Safari (GOG) | 21 | 2026-11-24 | 28 | 60% | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 212 | [x] | CarX Street (STEAM) | 21 | 2026-11-09 | 26 | 75% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 213 | [x] | Dead Island (STEAM) | 21 | 2026-11-09 | 24 | 85% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 214 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-11-09 | 37 | 86% |  |
| 215 | [x] | Capcom Fighting Collection 2 (STEAM) | 20 | 2026-11-09 | 36 | 87% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 216 | [x] | Tabletop Simulator (STEAM) | 20 | 2026-11-09 | 33 | 79% |  |
| 217 | [x] | GOD EATER RESURRECTION (STEAM) | 20 | 2026-11-09 | 32 | 86% |  |
| 218 | [x] | Deus Ex™ GOTY Edition (GOG) | 20 | 2026-11-09 | 31 | 100% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 219 | [x] | CRUEL (STEAM) | 20 | 2026-11-09 | 30 | 83% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 220 | [x] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 20 | 2026-11-22 | 21 | 67% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 221 | [x] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 2026-11-15 | 38 | 76% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 222 | [x] | Pinball FX Classic (STEAM) | 19 | 2026-11-09 | 37 | 87% |  |
| 223 | [x] | One-armed robber (STEAM) | 19 | 2026-11-09 | 36 | 65% |  |
| 224 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 32 | 92% |  |
| 225 | [x] | Torchlight II (EPIC) | 19 | 2026-11-09 | 27 | 81% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 226 | [x] | Dark Sector (STEAM) | 19 | 2026-11-21 | 25 | 73% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 227 | [x] | Crusader Kings III (STEAM) | 19 | 2026-11-18 | 23 | 75% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 228 | [x] | Watch Dogs 2 (EPIC) | 19 | 2026-11-23 | 21 | 67% | [#399](https://github.com/GameNative/gamenative-compat/issues/399) |
| 229 | [x] | Wizard of Legend (EPIC) | 18 | 2026-11-09 | 37 | 77% |  |
| 230 | [x] | Counter-Strike: Condition Zero (STEAM) | 18 | 2026-11-11 | 37 | 26% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 231 | [x] | Mini Metro (STEAM) | 18 | 2026-11-16 | 35 | 58% |  |
| 232 | [x] | Worms W.M.D (STEAM) | 18 | 2026-11-09 | 34 | 96% |  |
| 233 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 2026-11-09 | 29 | 86% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 234 | [x] | Nioh: Complete Edition (STEAM) | 18 | 2026-11-23 | 28 | 90% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 235 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-11-09 | 27 | 83% |  |
| 236 | [x] | Beyond: Two Souls (STEAM) | 18 | 2026-11-22 | 26 | 67% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 237 | [x] | Mafia II: Definitive Edition (GOG) | 18 | 2026-11-15 | 20 | 60% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 238 | [x] | Jade Empire: Special Edition (STEAM) | 18 | 2026-11-09 | 20 | 71% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 239 | [x] | Crazy Taxi (STEAM) | 17 | 2026-11-10 | 39 | 63% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 240 | [x] | Backpack Battles (STEAM) | 17 | 2026-11-09 | 38 | 90% |  |
| 241 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 17 | 2026-11-11 | 37 | 79% |  |
| 242 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 36 | 30% |  |
| 243 | [x] | Intravenous 2 (STEAM) | 17 | 2026-11-09 | 33 | 96% |  |
| 244 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 33 | 75% |  |
| 245 | [x] | This War of Mine (STEAM) | 17 | 2026-11-17 | 32 | 50% |  |
| 246 | [x] | Mafia II (Classic) (GOG) | 17 | 2026-11-24 | 28 | 60% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 247 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 17 | 2026-11-09 | 27 | 90% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 248 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 17 | 2026-11-15 | 26 | 64% |  |
| 249 | [x] | Bongo Cat (STEAM) | 17 | 2026-11-20 | 23 | 64% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 250 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 16 | 2026-10-25 | 43 | 71% |  |
| 251 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 252 | [x] | Far Far West (STEAM) | 16 | 2026-11-09 | 30 | 60% |  |
| 253 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 16 | 2026-11-09 | 29 | 61% |  |
| 254 | [x] | Moonlight Peaks (STEAM) | 16 | 2026-11-09 | 29 | 74% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 255 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 68% |  |
| 256 | [x] | Party Animals (STEAM) | 16 | 2026-11-09 | 24 | 73% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 257 | [x] | Capcom Fighting Collection (STEAM) | 16 | 2026-11-09 | 23 | 90% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 258 | [x] | Tales of Zestiria (STEAM) | 16 | 2026-11-09 | 23 | 73% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 259 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 260 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 261 | [x] | Styx: Master of Shadows (EPIC) | 15 | 2026-11-23 | 41 | 52% |  |
| 262 | [x] | Flotsam (EPIC) | 15 | 2026-11-20 | 34 | 41% |  |
| 263 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 29 | 100% |  |
| 264 | [x] | SWORN (STEAM) | 15 | 2026-11-09 | 29 | 95% |  |
| 265 | [x] | Disgaea 4 Complete+ (STEAM) | 15 | 2026-11-09 | 24 | 93% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 266 | [x] | AER Memories of Old (EPIC) | 15 | 2026-11-09 | 23 | 93% |  |
| 267 | [x] | Alabaster Dawn Demo (STEAM) | 15 | 2026-11-09 | 23 | 67% |  |
| 268 | [x] | Need for Speed™ Unbound (STEAM) | 15 | 2026-11-09 | 23 | 58% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 269 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 93% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 270 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 15 | 2026-11-09 | 22 | 78% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 271 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 272 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 273 | [x] | sobosuba (STEAM) | 14 | 2026-11-09 | 34 | 82% |  |
| 274 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 88% |  |
| 275 | [x] | Castle in the Clouds (STEAM) | 14 | 2026-11-09 | 28 | 68% |  |
| 276 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 14 | 2026-11-24 | 28 | 60% |  |
| 277 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 23 | 67% |  |
| 278 | [x] | Nex Machina (STEAM) | 14 | 2026-11-09 | 22 | 83% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 279 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 2026-11-16 | 22 | 93% |  |
| 280 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 281 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 282 | [x] | Spark the Electric Jester (STEAM) | 14 | 2026-11-13 | 20 | 75% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 283 | [x] | Blaster Master Zero (STEAM) | 13 | 2026-11-11 | 29 | 81% |  |
| 284 | [x] | Overlord (STEAM) | 13 | 2026-11-08 | 29 | 53% |  |
| 285 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 13 | 2026-11-09 | 28 | 94% |  |
| 286 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 28 | 100% |  |
| 287 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 13 | 2026-11-13 | 28 | 62% |  |
| 288 | [x] | Evoland (STEAM) | 13 | 2026-11-11 | 27 | n/a |  |
| 289 | [x] | Human Fall Flat (STEAM) | 13 | 2026-10-29 | 27 | 58% |  |
| 290 | [x] | Legacy of Kain: Defiance Remastered (STEAM) | 13 | 2026-11-24 | 27 | 80% |  |
| 291 | [x] | Batman™: Arkham Origins (GOG) | 13 | 2026-11-09 | 26 | 89% |  |
| 292 | [x] | MX Bikes (STEAM) | 13 | 2026-11-09 | 26 | 96% |  |
| 293 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 26 | 95% |  |
| 294 | [x] | Katana ZERO (GOG) | 13 | 2026-11-24 | 25 | 60% |  |
| 295 | [x] | Car Mechanic Simulator 2018 (STEAM) | 13 | 2026-11-09 | 24 | 93% |  |
| 296 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 24 | 74% |  |
| 297 | [x] | Horny Villa (STEAM) | 13 | 2026-11-09 | 22 | 86% |  |
| 298 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 299 | [x] | Shift At Midnight (STEAM) | 13 | 2026-11-09 | 21 | 90% |  |
| 300 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 70% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 301 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 93% |  |
| 302 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 303 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 2026-11-09 | 20 | 85% |  |
| 304 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-11-16 | 20 | 92% |  |
| 305 | [x] | Turbo Overkill (STEAM) | 13 | 2026-11-09 | 20 | 100% |  |
| 306 | [x] | CS2D (STEAM) | 12 | 2026-11-24 | 33 | 60% |  |
| 307 | [x] | GRIP: Combat Racing (STEAM) | 12 | 2026-11-09 | 33 | 80% |  |
| 308 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-24 | 24 | 64% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 309 | [x] | Legend of Grimrock 2 (STEAM) | 12 | 2026-11-09 | 24 | 93% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 310 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 24 | 64% |  |
| 311 | [x] | Sonic Superstars (STEAM) | 12 | 2026-11-21 | 24 | 68% |  |
| 312 | [x] | Forgive Me Father (STEAM) | 12 | 2026-11-15 | 22 | 72% |  |
| 313 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 314 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 315 | [x] | 12 is Better Than 6 (STEAM) | 12 | 2026-11-09 | 20 | 73% |  |
| 316 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 317 | [x] | Hitman: Contracts (STEAM) | 12 | 2026-11-23 | 20 | 67% |  |
| 318 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 28 | 100% |  |
| 319 | [x] | Antichamber (STEAM) | 11 | 2026-11-18 | 26 | 80% |  |
| 320 | [x] | Alan Wake's American Nightmare (EPIC) | 11 | 2026-11-09 | 24 | 73% |  |
| 321 | [x] | Cruelty Squad (STEAM) | 11 | 2026-11-09 | 23 | 86% |  |
| 322 | [x] | HITMAN World of Assassination (STEAM) | 11 | 2026-11-09 | 23 | 74% |  |
| 323 | [x] | Life is Strange Remastered (STEAM) | 11 | 2026-11-09 | 23 | 86% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 324 | [x] | Ready or Not (STEAM) | 11 | 2026-11-09 | 23 | 79% |  |
| 325 | [x] | Ultrapool (STEAM) | 11 | 2026-11-09 | 23 | n/a |  |
| 326 | [x] | Lost Castle 2 (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 327 | [x] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 2026-11-18 | 21 | 71% |  |
| 328 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 11 | 2026-10-27 | 21 | 92% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 329 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 330 | [x] | Another World: 20th Anniversary Edition (GOG) | 11 | 2026-11-21 | 20 | 60% |  |
| 331 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-11-09 | 20 | 71% |  |
| 332 | [x] | The Stanley Parable (STEAM) | 11 | 2026-11-13 | 20 | 75% |  |
| 333 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 28 | 92% |  |
| 334 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 10 | 2026-10-27 | 27 | 82% |  |
| 335 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 25 | 92% |  |
| 336 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 10 | 2026-11-09 | 24 | 88% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 337 | [x] | Tiny Glade (STEAM) | 10 | 2026-11-09 | 24 | 69% |  |
| 338 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 22 | 84% |  |
| 339 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 10 | 2026-11-10 | 21 | 69% |  |
| 340 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 341 | [x] | DiRT 4 (STEAM) | 10 | 2026-11-09 | 20 | 100% |  |
| 342 | [x] | Haydee (STEAM) | 10 | 2026-11-09 | 20 | 83% |  |
| 343 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 344 | [x] | Pillars of Eternity (STEAM) | 10 | 2026-11-21 | 20 | 100% |  |
| 345 | [x] | Secret of Mana (STEAM) | 10 | 2026-11-18 | 20 | 70% |  |
| 346 | [x] | Rayman Origins (GOG) | 9 | 2026-11-09 | 24 | 50% |  |
| 347 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 9 | 2026-11-01 | 24 | n/a |  |
| 348 | [x] | Mark of the Ninja (STEAM) | 9 | 2026-10-26 | 24 | 87% |  |
| 349 | [x] | Breath of Fire IV (GOG) | 9 | 2026-10-26 | 23 | 50% |  |
| 350 | [x] | Guacamelee! Gold Edition (STEAM) | 9 | 2026-11-11 | 22 | 75% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 351 | [x] | Need for Speed: Undercover (STEAM) | 9 | 2026-11-11 | 22 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 352 | [x] | UNDEFEATED (STEAM) | 9 | 2026-11-09 | 21 | 75% |  |
| 353 | [x] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 9 | 2026-11-17 | 20 | 33% |  |
| 354 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 27% |  |
| 355 | [x] | WORLD OF FINAL FANTASY (STEAM) | 8 | 2026-11-09 | 23 | 82% |  |
| 356 | [x] | Lust Goddess (STEAM) | 8 | 2026-11-09 | 22 | 69% |  |
| 357 | [x] | Aperture Desk Job (STEAM) | 8 | 2026-11-03 | 21 | n/a |  |
| 358 | [x] | GRANDIA HD Remaster (STEAM) | 8 | 2026-11-09 | 21 | 93% |  |
| 359 | [x] | SteamWorld Heist (GOG) | 8 | 2026-10-25 | 20 | n/a |  |
| 360 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 8 | 2026-11-09 | 20 | 73% |  |
| 361 | [x] | Soul's Remnant (STEAM) | 8 | 2026-11-11 | 20 | n/a |  |
| 362 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 23 | 50% |  |
| 363 | [x] | SCP – Containment Breach (STEAM) | 7 | 2026-10-27 | 21 | 91% |  |
| 364 | [x] | Mina the Hollower (GOG) | 7 | 2026-10-28 | 20 | 74% |  |
| 365 | [x] | CULTIC (STEAM) | 7 | 2026-11-09 | 20 | 53% |  |
