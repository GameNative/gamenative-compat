# GameNative compatibility worklist

Generated: `2026-11-22T04:15:12.270Z` · Ratings since: `2026-08-24T04:15:12.270Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Probably does not work | 187 |
| Fix shipped, waiting for ratings | 15 |
| First launch fails | 299 |
| Mixed | 473 |
| Works | 1023 |
| Total | 2123 |

## Does not work (126)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 179 | 210 | 85% (since fix) | Does not open (92%) | 42% | today | 35% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 2 | [ ] | Slay the Spire (STEAM) | 138 | 165 | 84% (14d) | Does not open (83%) | 47% | today | 29% | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 3 | [ ] | Rocket League® (EPIC) | 85 | 98 | 87% (14d) | Does not open (80%) | 37% | today | 29% | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 4 | [ ] | Buckshot Roulette (STEAM) | 45 | 63 | 71% (14d) | Does not open (65%) | 58% | today | 43% |  |
| 5 | [ ] | Hogwarts Legacy (STEAM) | 39 | 41 | 95% (14d) | Does not open (71%) | 28% | 1d ago | 17% | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 6 | [ ] | DREDGE (EPIC) | 37 | 41 | 90% (14d) | Does not open (79%) | 53% | today | 46% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 7 | [ ] | Melvor Idle 2: A RuneScape Adventure (STEAM) | 36 | 37 | 97% (14d) | Does not open (97%) | 36% | today | 35% | [#543](https://github.com/GameNative/gamenative-compat/issues/543) |
| 8 | [ ] | Horizon Chase Turbo (EPIC) | 24 | 31 | 77% (14d) | Does not open (84%) | 56% | 1d ago | 47% | [#546](https://github.com/GameNative/gamenative-compat/issues/546) |
| 9 | [x] 2026-10-18 | Project Zomboid (STEAM) | 61 | 67 | 91% (since fix) | Does not open (63%) | 40% | 1d ago | 36% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 10 | [ ] | Counter-Strike 2 (STEAM) | 53 | 76 | 70% (since fix) | Does not open (68%) | 56% | today | 58% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 11 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 23 | 26 | 88% (14d) | Does not open (75%) | 58% | today | 61% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 12 | [ ] | Mark of the Deep (EPIC) | 22 | 28 | 79% (14d) | Does not open (90%) | 24% | today | 21% | [#549](https://github.com/GameNative/gamenative-compat/issues/549) |
| 13 | [ ] | Path of Exile (STEAM) | 20 | 22 | 91% (14d) | Does not open (89%) | 29% | 2d ago | 26% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 14 | [ ] | Driver: Parallel Lines (STEAM) | 20 | 20 | 100% (14d) | Does not open (67%) | 43% | today | 50% | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 15 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 20 | 20 | 100% (last 20) | Does not open (96%) | 29% | today | 20% | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 16 | [ ] | Saints Row 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | 31% | today | 29% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 17 | [ ] | Bloons TD 6 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (79%) | 37% | 2d ago | 24% | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 18 | [ ] | Borderlands 2 (EPIC) | 18 | 20 | 90% (14d) | Does not open (80%) | 51% | today | 45% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 19 | [ ] | BioShock Remastered (EPIC) | 18 | 25 | 72% (14d) | Does not open (67%) | 59% | today | 53% | [#547](https://github.com/GameNative/gamenative-compat/issues/547) |
| 20 | [ ] | Sifu (EPIC) | 18 | 23 | 78% (14d) | Does not open (72%) | 44% | today | 34% | [#535](https://github.com/GameNative/gamenative-compat/issues/535) |
| 21 | [ ] | Metro: Last Light Redux (STEAM) | 20 | 20 | 100% (last 20) | Does not open (93%) | 25% | 3d ago | 28% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 22 | [ ] | River City Girls (EPIC) | 15 | 20 | 75% (14d) | Does not open (50%) | 56% | today | 39% | [#550](https://github.com/GameNative/gamenative-compat/issues/550) |
| 23 | [ ] | Saints Row 2 (GOG) | 15 | 20 | 75% (last 20) | Does not open (90%) | 35% | today | 35% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 24 | [ ] | Mafia II (Classic) (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 8% | 4d ago | 11% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 25 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (76%) | 0% | 13d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 26 | [ ] | skate. (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | 11% | today | 11% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 27 | [ ] | Dead Island 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (86%) | 56% | 1d ago | 39% |  |
| 28 | [ ] | Call of Duty: Black Ops II (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | 43% | 1d ago | 43% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 29 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 59% | 3d ago | 60% |  |
| 30 | [ ] | Vampire Survivors (EPIC) | 17 | 20 | 85% (last 20) | Does not open (60%) | 43% | 1d ago | 32% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 31 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | 54% | today | 47% | [#548](https://github.com/GameNative/gamenative-compat/issues/548) |
| 32 | [ ] | Hogwarts Legacy (EPIC) | 17 | 20 | 85% (last 20) | Does not open (76%) | 45% | today | 36% | [#537](https://github.com/GameNative/gamenative-compat/issues/537) |
| 33 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (91%) | 25% | 8d ago | 15% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 34 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 10 | 14 | 71% (since fix) | Does not open (91%) | 43% | 2d ago | 48% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 35 | [ ] | Teenage Mutant Ninja Turtles: Shredder's Revenge (EPIC) | 14 | 20 | 70% (last 20) | Does not open (84%) | 52% | 1d ago | 45% | [#551](https://github.com/GameNative/gamenative-compat/issues/551) |
| 36 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (78%) | 6% | 7d ago | 8% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 37 | [ ] | Trackmania (STEAM) | 17 | 20 | 85% (last 20) | Does not open (83%) | 24% | today | 31% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 38 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 33% | 4d ago | 27% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 39 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 16 | 20 | 80% (last 20) | Does not open (45%) | 47% | 3d ago | 70% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 40 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 55% | today | 62% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 41 | [ ] | Forza Horizon 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (47%) | 42% | 4d ago | 22% (drop) | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 42 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (71%) | 20% | 3d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 43 | [ ] | Kenshi (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 4% | today | 0% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 44 | [ ] | Fall Guys (EPIC) | 20 | 20 | 100% (last 20) | Does not open (68%) | 9% | 2d ago | 5% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 45 | [ ] | Detroit: Become Human (STEAM) | 18 | 20 | 90% (last 20) | Does not open (75%) | 59% | 4d ago | 64% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 46 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 8% | 10d ago | 5% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 47 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (70%) | 17% | today | 19% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 48 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 55% | today | 49% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 49 | [ ] | Breath of Fire IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (64%) | 15% | 2d ago | 11% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 50 | [ ] | The Witcher: Enhanced Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (76%) | 8% | today | 10% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 51 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | 0% | 7d ago | 0% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 52 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (94%) | 11% | 4d ago | 0% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 53 | [ ] | Call of Duty® (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | 0% | 1d ago | 0% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 54 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (68%) | 7% | 21d ago | 10% | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 55 | [ ] | MECCHA CHAMELEON (STEAM) | 15 | 20 | 75% (last 20) | Does not open (70%) | 40% | 4d ago | 34% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 56 | [ ] | Deliver At All Costs (EPIC) | 14 | 20 | 70% (last 20) | Does not open (62%) | 46% | 1d ago | 48% | [#538](https://github.com/GameNative/gamenative-compat/issues/538) |
| 57 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (82%) | 8% | today | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 58 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (71%) | 25% | 8d ago | 30% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 59 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (80%) | 12% | 13d ago | 14% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 60 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (83%) | 45% | 4d ago | 47% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 61 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 34% | 1d ago | 45% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 62 | [ ] | Borderlands GOTY (STEAM) | 16 | 20 | 80% (last 20) | Does not open (94%) | 38% | 2d ago | 47% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 63 | [ ] | Blood Omen: Legacy of Kain (GOG) | 16 | 20 | 80% (last 20) | No graphics (57%) | 58% | 3d ago | 55% | [#539](https://github.com/GameNative/gamenative-compat/issues/539) |
| 64 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (77%) | 5% | today | 6% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 65 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | 0% | 8d ago | 0% | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 66 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (88%) | 52% | 1d ago | 55% | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 67 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (67%) | 21% | 10d ago | 23% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 68 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (73%) | 45% | today | 38% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 69 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (54%) | 29% | 4d ago | 18% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 70 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | 0% | 7d ago | 0% | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 71 | [ ] | Half-Life: Blue Shift (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 36% | 5d ago | 45% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 72 | [ ] | Rivals of Aether II (STEAM) | 16 | 20 | 80% (last 20) | Does not open (53%) | 39% | 5d ago | 10% (drop) | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 73 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (77%) | 45% | 43d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 74 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (46%) | 46% | 1d ago | 45% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 75 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 31% | 13d ago | 37% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 76 | [ ] | Black Mesa (STEAM) | 15 | 20 | 75% (last 20) | Does not open (86%) | 33% | today | 34% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 77 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | 10% | 9d ago | 10% | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 78 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 45% | 8d ago | 53% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 79 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | 27% | 10d ago | 14% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 80 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 19 | 20 | 95% (last 20) | Does not open (85%) | 45% | 5d ago | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 81 | [ ] | XCOM: Enemy Unknown (STEAM) | 18 | 20 | 90% (last 20) | Does not open (71%) | 15% | 8d ago | n/a | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 82 | [ ] | Watch_Dogs (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | 37% | 2d ago | 41% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 83 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | 8% | 20d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 84 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 18% | 31d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 85 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 18% | today | n/a | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 86 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 17 | 20 | 85% (last 20) | Does not open (63%) | 29% | today | 25% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 87 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (73%) | 33% | 15d ago | 23% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 88 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | Does not open (63%) | 26% | 1d ago | 29% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 89 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 58% | 11d ago | 36% (drop) | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 90 | [ ] | Umamusume: Pretty Derby (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 50% | 2d ago | 53% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 91 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 15% | 22d ago | n/a | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 92 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (50%) | 52% | 3d ago | 59% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 93 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (73%) | 0% | 35d ago | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 94 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 3% | today | 4% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 95 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 3% | today | 1% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 96 | [ ] | Changed (STEAM) | 15 | 20 | 75% (last 20) | Does not open (62%) | 59% | 9d ago | 50% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 97 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 19 | 20 | 95% (last 20) | Does not open (57%) | 36% | today | 42% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 98 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 33% | 1d ago | 38% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 99 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (63%) | 46% | 2d ago | 50% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 100 | [ ] | Aliens vs. Predator (STEAM) | 17 | 20 | 85% (last 20) | Does not open (67%) | 33% | today | 38% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 101 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (89%) | 16% | 14d ago | 7% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 102 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (61%) | 46% | 10d ago | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 103 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 23% | 2d ago | 18% | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 104 | [ ] | Assassin's Creed Brotherhood (STEAM) | 18 | 20 | 90% (last 20) | Does not open (94%) | 33% | 1d ago | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 105 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 7% | 28d ago | 8% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 106 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 20 | 80% (last 20) | Does not open (53%) | 48% | 1d ago | 33% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 107 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | 17% | 20d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 108 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (89%) | 28% | 6d ago | 35% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 109 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (96%) | 30% | 20d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 110 | [ ] | Brutal Legend (GOG) | 16 | 20 | 80% (last 20) | Does not open (82%) | 20% | today | n/a |  |
| 111 | [ ] | Lost Planet: Extreme Condition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | 46% | 7d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 112 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 47% | today | 41% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 113 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (55%) | 46% | 10d ago | 21% (drop) | [#540](https://github.com/GameNative/gamenative-compat/issues/540) |
| 114 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 25% | today | 36% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 115 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (54%) | 55% | 25d ago | 43% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 116 | [ ] | OneShot (STEAM) | 15 | 20 | 75% (last 20) | Does not open (96%) | 20% | 1d ago | n/a | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 117 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 33% | 22d ago | 30% | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 118 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | 45% | 22d ago | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 119 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | 27% | 11d ago | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 120 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 58% | 10d ago | 55% |  |
| 121 | [ ] | Beyond Good & Evil™ (GOG) | 17 | 20 | 85% (last 20) | Does not open (100%) | 9% | 3d ago | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 122 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (73%) | 57% | 13d ago | 67% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 123 | [ ] | Hitman 2: Silent Assassin (STEAM) | 14 | 20 | 70% (last 20) | Does not open (67%) | 43% | 1d ago | 44% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 124 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (54%) | 42% | 7d ago | n/a | [#541](https://github.com/GameNative/gamenative-compat/issues/541) |
| 125 | [ ] | Ghostwire Tokyo (EPIC) | 14 | 20 | 70% (last 20) | Does not open (90%) | 48% | 7d ago | 35% | [#544](https://github.com/GameNative/gamenative-compat/issues/544) |
| 126 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 20 | 70% (last 20) | Does not open (70%) | 42% | 14d ago | 45% | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |

## Probably does not work (187)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Euro Truck Simulator 2 (STEAM) | 19 | 34 | 56% (14d) | Does not open (64%) | 59% | today | 57% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 2 | [ ] | Owlboy (STEAM) | 18 | 28 | 64% (14d) | Does not open (81%) | 52% | today | 48% | [#545](https://github.com/GameNative/gamenative-compat/issues/545) |
| 3 | [ ] | Metro 2033 Redux (STEAM) | 17 | 30 | 57% (14d) | Does not open (70%) | 40% | today | 41% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 4 | [ ] | Absolute Drift (EPIC) | 16 | 25 | 64% (14d) | No graphics (58%) | 59% | today | 36% (drop) |  |
| 5 | [ ] | theHunter Classic (STEAM) | 20 | 20 | 100% (last 20) | No graphics (92%) | n/a | 18d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 6 | [ ] | Bully: Scholarship Edition (STEAM) | 14 | 22 | 64% (14d) | Does not open (65%) | 39% | today | 13% (drop) |  |
| 7 | [ ] | To The Moon (GOG) | 18 | 20 | 90% (last 20) | Does not open (86%) | n/a | 19d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 8 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 26 | 46 | 57% (since fix) | Does not open (72%) | 59% | 2d ago | 57% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 9 | [ ] | Garry's Mod (STEAM) | 14 | 23 | 61% (since fix) | Does not open (78%) | 54% | today | 45% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 10 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 13 | 20 | 65% (last 20) | Does not open (78%) | 55% | today | 48% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 11 | [ ] | Batman™ Arkham Asylum Game of the Year Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (75%) | 54% | today | 42% |  |
| 12 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 13 | 20 | 65% (last 20) | Does not open (63%) | 47% | 7d ago | 43% |  |
| 13 | [ ] | Asterigos: Curse of the Stars (STEAM) | 16 | 20 | 80% (last 20) | Graphics glitches (73%) | n/a | today | n/a |  |
| 14 | [ ] | VRChat (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 38% | 1d ago | 35% |  |
| 15 | [ ] | Darksiders Warmastered Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 53% | 3d ago | 39% |  |
| 16 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 15 | 23 | 65% (since fix) | Does not open (78%) | 38% | today | 42% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 17 | [ ] | STAR WARS™ Knights of the Old Republic™ II: The Sith Lords™ (STEAM) | 12 | 20 | 60% (last 20) | No graphics (64%) | 53% | 1d ago | 39% |  |
| 18 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 42d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 19 | [ ] | Cat Quest (EPIC) | 10 | 20 | 50% (last 20) | Does not open (47%) | 42% | today | 37% |  |
| 20 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (38%) | n/a | 1d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 21 | [ ] | Gorilla Tag (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 14% | 7d ago | 8% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 22 | [ ] | Catherine Classic (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (41%) | 51% | today | 44% |  |
| 23 | [ ] | DOOM 64 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (60%) | 49% | 3d ago | 35% |  |
| 24 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 11 | 20 | 55% (last 20) | Does not open (73%) | 48% | today | 41% |  |
| 25 | [ ] | Bad Cheese (EPIC) | 11 | 20 | 55% (last 20) | Does not open (100%) | 45% | today | 30% |  |
| 26 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 8d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 27 | [ ] | Door Kickers 2 (STEAM) | 18 | 20 | 90% (last 20) | No graphics (85%) | n/a | today | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 28 | [ ] | Art of Rally (EPIC) | 12 | 20 | 60% (last 20) | Does not open (76%) | 39% | today | 36% |  |
| 29 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (49%) | 56% | 8d ago | 39% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 30 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 20 | 20 | 100% (last 20) | Controller issues (100%) | n/a | 3d ago | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 31 | [ ] | Phasmophobia (STEAM) | 12 | 20 | 60% (last 20) | Does not open (56%) | 56% | today | 50% |  |
| 32 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 11 | 20 | 55% (last 20) | Does not open (72%) | 38% | today | 39% |  |
| 33 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 26d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 34 | [ ] | Metro 2033 Redux (EPIC) | 12 | 20 | 60% (last 20) | Does not open (62%) | 30% | today | 33% |  |
| 35 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | No graphics (41%) | 46% | today | 34% |  |
| 36 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | No graphics (56%) | n/a | 25d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 37 | [ ] | Counter-Strike (STEAM) | 11 | 20 | 55% (last 20) | Does not open (69%) | 38% | 1d ago | 31% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 38 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 15d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 39 | [ ] | MudRunner (EPIC) | 11 | 20 | 55% (last 20) | Does not open (63%) | 49% | 1d ago | 41% |  |
| 40 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (58%) | n/a | 6d ago | n/a | [#536](https://github.com/GameNative/gamenative-compat/issues/536) |
| 41 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 12 | 20 | 60% (last 20) | Does not open (85%) | 47% | 2d ago | 23% (drop) | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 42 | [ ] | Sonic Adventure™ 2  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 46% | 2d ago | 40% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 43 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 23d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 44 | [ ] | CPM 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (88%) | 3% | today | 3% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 45 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (93%) | n/a | 5d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 46 | [ ] | Legacy of Kain: Defiance Remastered (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (69%) | n/a | today | n/a |  |
| 47 | [ ] | Hi-Fi RUSH (STEAM) | 11 | 20 | 55% (last 20) | Does not open (76%) | 42% | 2d ago | 42% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 48 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 11 | 20 | 55% (last 20) | Does not open (62%) | 17% | 5d ago | n/a |  |
| 49 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | n/a | 14d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 50 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | n/a | 7d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 51 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | 59% | 3d ago | 50% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 52 | [ ] | CODE VEIN (STEAM) | 13 | 20 | 65% (last 20) | Does not open (68%) | 35% | 6d ago | 20% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 53 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (85%) | 50% | 12d ago | n/a |  |
| 54 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 17d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 55 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (66%) | n/a | 20d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 56 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | n/a | 7d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 57 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 40d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 58 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (93%) | n/a | today | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 59 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 3d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 60 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 11d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 61 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 19d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 62 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | n/a | 41d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 63 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | 8d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 64 | [ ] | Grim Dawn (GOG) | 13 | 20 | 65% (last 20) | Does not open (69%) | n/a | 6d ago | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 65 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 39d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 66 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (58%) | n/a | 7d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 67 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | n/a | 11d ago | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 68 | [ ] | Dead Space 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (66%) | 33% | 1d ago | 32% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 69 | [ ] | No More Heroes (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 41% | 1d ago | 35% |  |
| 70 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | n/a | 8d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 71 | [ ] | DOOM Eternal (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | 2d ago | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 72 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (62%) | n/a | 3d ago | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 73 | [ ] | Alpha Protocol (STEAM) | 17 | 20 | 85% (last 20) | No graphics (53%) | n/a | 27d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 74 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 42% | 5d ago | 28% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 75 | [ ] | METAL SLUG 3 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (81%) | 53% | 9d ago | 61% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 76 | [ ] | Metro 2033 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (62%) | 36% | 1d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 77 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | n/a | 42d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 78 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 39d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 79 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (56%) | n/a | 8d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 80 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | 23d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 81 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (77%) | n/a | 39d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 82 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 25d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 83 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | 58% | 14d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 84 | [ ] | HELLDIVERS™ (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 56% | 3d ago | 57% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 85 | [ ] | Peggle Nights (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | today | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 86 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 50d ago | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 87 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 21d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 88 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 8d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 89 | [ ] | Borderlands 2 RU (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | n/a | 5d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 90 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | 4d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 91 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 13d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 92 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 25d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 93 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 55% | 18d ago | n/a |  |
| 94 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 30% | 12d ago | 23% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 95 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (92%) | 36% | 6d ago | 30% |  |
| 96 | [ ] | Hollow Knight: Silksong (GOG) | 10 | 20 | 50% (last 20) | Does not open (70%) | 49% | today | 47% |  |
| 97 | [ ] | Euro Truck Simulator (STEAM) | 20 | 20 | 100% (last 20) | Does not open (86%) | n/a | 6d ago | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 98 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (50%) | n/a | 21d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 99 | [ ] | Beholder (EPIC) | 18 | 20 | 90% (last 20) | No graphics (63%) | n/a | 1d ago | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 100 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | n/a | 44d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 101 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | n/a | 4d ago | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 102 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | n/a | 1d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 103 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (61%) | n/a | 48d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 104 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | n/a | today | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 105 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 6d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 106 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 14 | 20 | 70% (last 20) | Does not open (90%) | n/a | today | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 107 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (54%) | n/a | 27d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 108 | [ ] | A Plague Tale: Innocence (EPIC) | 12 | 20 | 60% (last 20) | Does not open (70%) | 39% | 2d ago | 32% |  |
| 109 | [ ] | Super Meat Boy Forever (EPIC) | 10 | 20 | 50% (last 20) | Does not open (83%) | 40% | 2d ago | 26% |  |
| 110 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | n/a | today | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 111 | [ ] | The Survivalists (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | n/a | 9d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 112 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | n/a | 5d ago | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 113 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 15d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 114 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 17d ago | n/a |  |
| 115 | [ ] | Rise of the Tomb Raider: 20 Year Celebration (EPIC) | 11 | 20 | 55% (last 20) | Does not open (67%) | 44% | 3d ago | 36% |  |
| 116 | [ ] | Breathedge (STEAM) | 10 | 20 | 50% (last 20) | Does not open (54%) | 57% | 2d ago | 65% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 117 | [ ] | Bionic Commando Rearmed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (75%) | n/a | 32d ago | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 118 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 18 | 20 | 90% (last 20) | Does not open (72%) | n/a | 26d ago | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 119 | [ ] | Undisputed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | n/a | 14d ago | n/a | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 120 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 13d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 121 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | n/a | 15d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 122 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (80%) | n/a | 12d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 123 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 10d ago | n/a |  |
| 124 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | n/a | 10d ago | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 125 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 23d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 126 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (36%) | n/a | today | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 127 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 24d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 128 | [ ] | Drop Duchy (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 10% | 3d ago | n/a |  |
| 129 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 17d ago | n/a |  |
| 130 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 17d ago | n/a |  |
| 131 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 55% | 3d ago | n/a | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 132 | [ ] | CS2D (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | n/a | 3d ago | n/a |  |
| 133 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 10 | 20 | 50% (last 20) | Does not open (90%) | 50% | today | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 134 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 10d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 135 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | No graphics (45%) | n/a | 12d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 136 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | n/a | 2d ago | n/a |  |
| 137 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | n/a | 4d ago | n/a | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 138 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 13 | 20 | 65% (last 20) | Does not open (55%) | 42% | 6d ago | 30% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 139 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | n/a | 10d ago | n/a |  |
| 140 | [ ] | Mortal Shell (EPIC) | 13 | 20 | 65% (last 20) | Does not open (50%) | 32% | 3d ago | 21% |  |
| 141 | [ ] | Mafia II (Classic) (GOG) | 13 | 20 | 65% (last 20) | Does not open (100%) | n/a | 7d ago | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 142 | [ ] | Dying Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (86%) | 52% | today | 42% |  |
| 143 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | n/a | 6d ago | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 144 | [ ] | Fallout Classic (GOG) | 15 | 20 | 75% (last 20) | Does not open (86%) | n/a | 9d ago | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 145 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | 9d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 146 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (69%) | n/a | 17d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 147 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | n/a | 34d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 148 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (86%) | 15% | 3d ago | 21% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 149 | [ ] | Romancing SaGa -Minstrel Song- Remastered (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (100%) | n/a | today | n/a |  |
| 150 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 46% | 22d ago | 29% |  |
| 151 | [ ] | Mafia: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (87%) | 35% | 3d ago | 32% |  |
| 152 | [ ] | Sacred Gold (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | n/a | 3d ago | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 153 | [ ] | Re-Volt (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (71%) | n/a | today | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 154 | [ ] | Chef Knight (STEAM) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 26d ago | n/a |  |
| 155 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | n/a | 12d ago | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 156 | [ ] | shapez (STEAM) | 14 | 20 | 70% (last 20) | No graphics (73%) | n/a | 2d ago | n/a | [#332](https://github.com/GameNative/gamenative-compat/issues/332) |
| 157 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 47% | 8d ago | 30% |  |
| 158 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | 42% | 11d ago | 40% |  |
| 159 | [ ] | Songs of Conquest (EPIC) | 13 | 20 | 65% (last 20) | Does not open (75%) | n/a | 6d ago | n/a |  |
| 160 | [ ] | LET IT DIE (STEAM) | 12 | 20 | 60% (last 20) | Does not open (94%) | 20% | today | n/a |  |
| 161 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | n/a | 3d ago | n/a |  |
| 162 | [ ] | Chasm (GOG) | 12 | 20 | 60% (last 20) | No graphics (50%) | n/a | 7d ago | n/a |  |
| 163 | [ ] | Crying Suns (EPIC) | 12 | 20 | 60% (last 20) | No graphics (63%) | n/a | 4d ago | n/a |  |
| 164 | [ ] | DAEMON X MACHINA (EPIC) | 10 | 20 | 50% (last 20) | Does not open (92%) | 44% | 3d ago | 21% (drop) |  |
| 165 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Does not open (40%) | n/a | 13d ago | n/a |  |
| 166 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 10 | 20 | 50% (last 20) | No graphics (57%) | 42% | 6d ago | 62% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 167 | [ ] | Beat Cop (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | n/a | 9d ago | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 168 | [ ] | FINAL FANTASY VII REMAKE INTERGRADE (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 41% | 7d ago | 41% |  |
| 169 | [ ] | Sandustry (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | n/a | 7d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 170 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 17d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 171 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 11 | 20 | 55% (last 20) | Does not open (100%) | 33% | today | 30% |  |
| 172 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 56% | 1d ago | 59% |  |
| 173 | [ ] | Hitman: Absolution (GOG) | 10 | 20 | 50% (last 20) | Does not open (83%) | n/a | 4d ago | n/a |  |
| 174 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | n/a | 12d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 175 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 16d ago | n/a |  |
| 176 | [ ] | Minit (EPIC) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 14d ago | n/a |  |
| 177 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 43% | 3d ago | n/a |  |
| 178 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 23d ago | n/a |  |
| 179 | [ ] | Allumeria (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | n/a | today | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 180 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | n/a | 10d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 181 | [ ] | HOT WHEELS UNLEASHED™ (EPIC) | 10 | 20 | 50% (last 20) | No graphics (63%) | 43% | 5d ago | 35% |  |
| 182 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | No graphics (50%) | n/a | 24d ago | n/a | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 183 | [ ] | Turnip Boy Robs a Bank (EPIC) | 11 | 20 | 55% (last 20) | Does not open (64%) | 38% | 8d ago | n/a | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 184 | [ ] | Styx: Master of Shadows (EPIC) | 10 | 20 | 50% (last 20) | Does not open (73%) | 50% | 1d ago | 53% |  |
| 185 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 55% | 9d ago | n/a |  |
| 186 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | n/a | 16d ago | n/a |  |
| 187 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 10 | 20 | 50% (last 20) | Does not open (77%) | n/a | 87d ago | n/a |  |

## Fix shipped, waiting for ratings (15)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | L.A. Noire (STEAM) | 2026-11-04 | 4 | 4 | 7d ago | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 2 | Max Payne 3 (STEAM) | 2026-11-04 | 3 | 3 | 5d ago | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 3 | Red Dead Redemption (STEAM) | 2026-11-04 | 2 | 2 | 5d ago | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 4 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 8 | 8 | 2d ago | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 5 | Transistor (STEAM) | 2026-11-10 | 8 | 4 | 2d ago | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 6 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 4 | 4 | today | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 7 | Peggle Deluxe (STEAM) | 2026-10-29 | 4 | 2 | today | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 8 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 1 | 1 | 11d ago | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 9 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 1 | 1 | 18d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 10 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 5 | 5 | 1d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 11 | Need for Speed™ (STEAM) | 2026-11-04 | 0 | 0 | 31d ago | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 12 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 2 | 2 | today | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 13 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 17d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 14 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 0 | 0 | 18d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 15 | Assassin's Creed Odyssey (STEAM) | n/a | 1 | 1 | today | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |

## Works, but the first launch usually fails (299)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Half-Life (STEAM) | 80 | 114 | 70% (14d) | Does not open (60%) | 70% | today | 67% |  |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 61 | 83 | 73% (14d) | Does not open (63%) | 93% | today | 95% |  |
| 3 | [ ] | Grand Theft Auto V Legacy (STEAM) | 78 | 90 | 87% (since fix) | Does not open (87%) | 74% | today | 73% |  |
| 4 | [ ] | Cyberpunk 2077 (STEAM) | 48 | 81 | 59% (14d) | Does not open (70%) | 72% | today | 70% |  |
| 5 | [ ] | Portal (STEAM) | 47 | 82 | 57% (14d) | Does not open (42%) | 88% | today | 87% |  |
| 6 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 46 | 61 | 75% (14d) | Does not open (55%) | 83% | today | 82% |  |
| 7 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 39 | 53 | 74% (14d) | Does not open (60%) | 66% | today | 61% |  |
| 8 | [ ] | MONSTER HUNTER RISE (STEAM) | 38 | 67 | 57% (14d) | Does not open (84%) | 60% | today | 62% |  |
| 9 | [ ] | ROB RUN (STEAM) | 36 | 47 | 77% (14d) | Does not open (86%) | 66% | today | 68% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 10 | [ ] | Valheim (STEAM) | 41 | 69 | 59% (since fix) | No graphics (54%) | 82% | today | 82% |  |
| 11 | [ ] | Probably Stolen (STEAM) | 31 | 53 | 58% (14d) | Does not open (64%) | 85% | 2d ago | 80% |  |
| 12 | [ ] | No Man's Sky (STEAM) | 37 | 67 | 55% (since fix) | Controller issues (61%) | 81% | today | 77% |  |
| 13 | [ ] | Selaco (STEAM) | 27 | 42 | 64% (14d) | Does not open (88%) | 67% | today | 64% |  |
| 14 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 24 | 38 | 63% (14d) | Does not open (76%) | 73% | today | 69% |  |
| 15 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 19 | 20 | 95% (14d) | Controller issues (40%) | 93% | today | 91% |  |
| 16 | [ ] | ELDEN RING (STEAM) | 18 | 34 | 53% (14d) | Does not open (86%) | 66% | today | 64% |  |
| 17 | [ ] | BeamNG.drive (STEAM) | 18 | 25 | 72% (14d) | Does not open (77%) | 70% | today | 60% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 18 | [ ] | Fallout: New Vegas PCR (STEAM) | 18 | 21 | 86% (14d) | Does not open (93%) | 66% | today | 61% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 19 | [ ] | Red Dead Redemption 2 (STEAM) | 23 | 26 | 88% (since fix) | Does not open (97%) | 85% | today | 87% |  |
| 20 | [ ] | Look Outside (STEAM) | 17 | 29 | 59% (14d) | Controller issues (63%) | 92% | today | 91% |  |
| 21 | [ ] | Library Of Ruina (STEAM) | 17 | 25 | 68% (14d) | Does not open (72%) | 87% | 1d ago | 86% |  |
| 22 | [ ] | Overcooked! 2 (EPIC) | 17 | 21 | 81% (14d) | Does not open (92%) | 73% | today | 65% |  |
| 23 | [ ] | Dead Space (STEAM) | 18 | 20 | 90% (last 20) | Does not open (54%) | 81% | 1d ago | 76% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 24 | [ ] | Castlevania Anniversary Collection (EPIC) | 18 | 20 | 90% (last 20) | Does not open (80%) | 60% | today | 38% (drop) |  |
| 25 | [ ] | Alice: Madness Returns (STEAM) | 14 | 27 | 52% (14d) | Does not open (66%) | 89% | today | 89% |  |
| 26 | [ ] | Team Fortress 2 (STEAM) | 14 | 28 | 50% (14d) | Does not open (68%) | 77% | today | 76% |  |
| 27 | [ ] | Noita (STEAM) | 14 | 23 | 61% (14d) | Does not open (58%) | 77% | 1d ago | 77% |  |
| 28 | [ ] | Order of the Sinking Star (STEAM) | 14 | 25 | 56% (14d) | Does not open (65%) | 66% | 1d ago | 70% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 29 | [ ] | Resident Evil 4 (2005) (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 72% | today | 70% |  |
| 30 | [ ] | Deadlock (STEAM) | 15 | 20 | 75% (last 20) | Does not open (51%) | 86% | today | 82% |  |
| 31 | [ ] | DRAGON BALL FighterZ (STEAM) | 28 | 55 | 51% (since fix) | Does not open (88%) | 86% | today | 89% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 32 | [ ] | Cry of Fear (STEAM) | 14 | 20 | 70% (last 20) | Does not open (44%) | 68% | today | 70% |  |
| 33 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 13 | 20 | 65% (14d) | Controller issues (54%) | 74% | today | 66% |  |
| 34 | [ ] | Loftia (STEAM) | 13 | 20 | 65% (14d) | Does not open (94%) | 70% | today | 64% |  |
| 35 | [ ] | Grand Theft Auto V (EPIC) | 18 | 20 | 90% (last 20) | Does not open (87%) | 75% | today | 73% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 36 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (90%) | 90% | 1d ago | 89% |  |
| 37 | [ ] | Left 4 Dead (STEAM) | 12 | 24 | 50% (14d) | Does not open (43%) | 86% | today | 84% |  |
| 38 | [ ] | Quake (STEAM) | 12 | 21 | 57% (14d) | Does not open (62%) | 71% | 2d ago | 59% |  |
| 39 | [ ] | Mass Effect™ Legendary Edition (STEAM) | 14 | 26 | 54% (since fix) | Does not open (83%) | 80% | 1d ago | 83% |  |
| 40 | [ ] | DOOM 3: BFG Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (74%) | 71% | today | 69% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 41 | [ ] | Mortal Kombat X (STEAM) | 13 | 20 | 65% (last 20) | Does not open (72%) | 91% | 4d ago | 92% |  |
| 42 | [ ] | Alabaster Dawn (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (50%) | 89% | 2d ago | 89% |  |
| 43 | [ ] | Resident Evil 7 Biohazard (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 70% | 2d ago | 62% |  |
| 44 | [ ] | DmC Devil May Cry (STEAM) | 10 | 20 | 50% (14d) | No graphics (52%) | 84% | today | 83% |  |
| 45 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 17 | 20 | 85% (last 20) | Does not open (59%) | 87% | today | 86% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 46 | [ ] | Barony (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 84% | today | 79% |  |
| 47 | [ ] | Clair Obscur: Expedition 33 (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (41%) | 77% | today | 73% |  |
| 48 | [ ] | Crypt of the NecroDancer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (45%) | 88% | today | 86% |  |
| 49 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (69%) | 100% | 1d ago | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 50 | [ ] | DOOM (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 87% | 4d ago | 86% |  |
| 51 | [ ] | Disco Elysium - The Final Cut (EPIC) | 12 | 20 | 60% (last 20) | Does not open (76%) | 92% | today | 91% |  |
| 52 | [ ] | Welcome to Elderfield (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 70% | today | 72% |  |
| 53 | [ ] | Batman™: Arkham Origins (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 67% | 1d ago | 61% |  |
| 54 | [ ] | Dressmaker (STEAM) | 12 | 20 | 60% (last 20) | Does not open (55%) | 78% | today | 73% |  |
| 55 | [ ] | Fallout: New Vegas (EPIC) | 16 | 20 | 80% (last 20) | Does not open (59%) | 78% | 1d ago | 73% |  |
| 56 | [ ] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (59%) | 77% | today | 84% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 57 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 10 | 18 | 56% (since fix) | Controller issues (83%) | 73% | today | 72% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 58 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 66% | today | 68% |  |
| 59 | [ ] | Chained Echoes (GOG) | 15 | 20 | 75% (last 20) | Does not open (62%) | 65% | today | 57% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 60 | [ ] | OMORI (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 68% | 1d ago | 59% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 61 | [ ] | Aniimo (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 79% | today | 74% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 62 | [ ] | Don't Starve Together (STEAM) | 11 | 20 | 55% (last 20) | Does not open (61%) | 73% | today | 67% |  |
| 63 | [ ] | Mini Motorways (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 64% | 2d ago | 62% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 64 | [ ] | Rune Factory 3 Special (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 100% | today | 100% |  |
| 65 | [ ] | Devil May Cry 5 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 82% | today | 83% |  |
| 66 | [ ] | Disgaea 5 Complete (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | 91% | 5d ago | 95% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 67 | [ ] | FINAL FANTASY (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 82% | 1d ago | 76% |  |
| 68 | [ ] | Until Then (STEAM) | 17 | 20 | 85% (last 20) | Does not open (85%) | 66% | today | 51% |  |
| 69 | [ ] | Cave Story+ (STEAM) | 19 | 20 | 95% (last 20) | Does not open (62%) | 76% | today | 74% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 70 | [ ] | Stardew Valley (GOG) | 10 | 20 | 50% (last 20) | Controller issues (59%) | 80% | today | 82% |  |
| 71 | [ ] | Castlevania Dominus Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (91%) | 98% | today | 96% |  |
| 72 | [ ] | Divinity: Original Sin 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 81% | today | 77% |  |
| 73 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 8 | 12 | 67% (since fix) | Does not open (82%) | 62% | today | 64% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 74 | [ ] | LEGO® MARVEL Super Heroes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (65%) | 85% | 2d ago | 87% |  |
| 75 | [ ] | PAC-MAN Championship Edition DX+ (STEAM) | 10 | 20 | 50% (last 20) | No graphics (59%) | 69% | 1d ago | 57% |  |
| 76 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (61%) | 95% | today | 96% |  |
| 77 | [ ] | TBH: Task Bar Hero (STEAM) | 11 | 20 | 55% (last 20) | Does not open (68%) | 84% | 1d ago | 87% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 78 | [ ] | eFootball™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | 63% | 4d ago | 57% |  |
| 79 | [ ] | Poppy Playtime (STEAM) | 13 | 20 | 65% (last 20) | Does not open (57%) | 70% | today | 63% |  |
| 80 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (52%) | 83% | 1d ago | 81% |  |
| 81 | [ ] | Call of Duty 4: Modern Warfare (2007) (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (54%) | 74% | 1d ago | 64% |  |
| 82 | [ ] | PAYDAY: The Heist (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 75% | 1d ago | n/a |  |
| 83 | [ ] | Cyberpunk 2077 (GOG) | 10 | 20 | 50% (last 20) | Does not open (71%) | 69% | today | 65% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 84 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 97% | 3d ago | 96% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 85 | [ ] | Deskrawl: Idle ARPG (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 64% | 11d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 86 | [ ] | Leaf it Alone (STEAM) | 10 | 20 | 50% (last 20) | Does not open (54%) | 95% | 1d ago | 94% |  |
| 87 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 67% | 5d ago | 74% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 88 | [ ] | Happy Wheels (STEAM) | 19 | 20 | 95% (last 20) | No graphics (52%) | 63% | 15d ago | 50% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 89 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 15 | 20 | 75% (last 20) | Does not open (40%) | 72% | 5d ago | 71% |  |
| 90 | [ ] | Fable - The Lost Chapters (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (48%) | 80% | today | 83% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 91 | [ ] | Dota 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (77%) | 75% | today | 78% |  |
| 92 | [ ] | Need for Speed™ Rivals (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 72% | 5d ago | 74% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 93 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (80%) | 62% | 1d ago | 47% |  |
| 94 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (80%) | 88% | 4d ago | 82% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 95 | [ ] | Palia (STEAM) | 16 | 20 | 80% (last 20) | Does not open (65%) | 71% | 3d ago | 67% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 96 | [ ] | Ratatan (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | 87% | 1d ago | 83% |  |
| 97 | [ ] | Mortal Kombat 11 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | 67% | 2d ago | 76% |  |
| 98 | [ ] | Minecraft Dungeons II (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 72% | 1d ago | 71% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 99 | [ ] | Tails of Iron (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 86% | today | 87% |  |
| 100 | [ ] | Sid Meier's Civilization VI (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | 78% | 1d ago | 76% |  |
| 101 | [ ] | MIO: Memories in Orbit (STEAM) | 11 | 20 | 55% (last 20) | Graphics glitches (61%) | 93% | 6d ago | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 102 | [ ] | Grand Theft Auto: Vice City (STEAM) | 13 | 20 | 65% (last 20) | Does not open (45%) | 76% | today | 77% |  |
| 103 | [ ] | ZERO Sievert (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 85% | 1d ago | 80% |  |
| 104 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (57%) | 69% | 4d ago | 74% |  |
| 105 | [ ] | American Truck Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 73% | today | 71% |  |
| 106 | [ ] | Fate/stay night REMASTERED (STEAM) | 11 | 20 | 55% (last 20) | No graphics (48%) | 92% | today | 91% |  |
| 107 | [ ] | Resident Evil Village (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 88% | 1d ago | 86% |  |
| 108 | [ ] | Minecraft Dungeons (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 80% | 1d ago | 79% |  |
| 109 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 89% | 3d ago | 83% |  |
| 110 | [ ] | The Sims™ 4 (STEAM) | 6 | 12 | 50% (since fix) | Does not open (84%) | 70% | 4d ago | 70% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 111 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (42%) | 90% | 1d ago | 90% |  |
| 112 | [ ] | Astral Party  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 89% | 2d ago | 86% |  |
| 113 | [ ] | Abiotic Factor (STEAM) | 10 | 20 | 50% (last 20) | Does not open (74%) | 76% | 5d ago | 83% |  |
| 114 | [ ] | Moonstone Island (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (63%) | 71% | today | 72% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 115 | [ ] | Call of Duty: World at War (STEAM) | 13 | 20 | 65% (last 20) | Does not open (39%) | 76% | today | 66% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 116 | [ ] | Caravan SandWitch (EPIC) | 10 | 20 | 50% (last 20) | Does not open (75%) | 67% | today | 67% |  |
| 117 | [ ] | A Plague Tale: Innocence (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | 70% | 6d ago | 71% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 118 | [ ] | Sid Meier's Civilization V (STEAM) | 15 | 20 | 75% (last 20) | Does not open (77%) | 62% | 2d ago | 57% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 119 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 15 | 20 | 75% (last 20) | Does not open (71%) | 83% | today | 81% |  |
| 120 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 70% | 15d ago | 73% |  |
| 121 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (84%) | 62% | 1d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 122 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 62% | 6d ago | 59% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 123 | [ ] | PlateUp! (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 81% | 2d ago | 72% |  |
| 124 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | 82% | 13d ago | 82% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 125 | [ ] | Street Fighter™ 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | 79% | today | 77% |  |
| 126 | [ ] | No, I'm not a Human (STEAM) | 10 | 20 | 50% (last 20) | Does not open (52%) | 91% | today | 86% |  |
| 127 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | 93% | 8d ago | 92% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 128 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (76%) | 100% | 7d ago | 100% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 129 | [ ] | Oxygen Not Included (STEAM) | 13 | 20 | 65% (last 20) | Does not open (74%) | 70% | today | 76% |  |
| 130 | [ ] | Sovereign Tower (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 81% | 2d ago | 81% |  |
| 131 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 11 | 20 | 55% (last 20) | Does not open (68%) | 91% | today | 91% |  |
| 132 | [ ] | OCTOPATH TRAVELER 0 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (77%) | 92% | 1d ago | 95% |  |
| 133 | [ ] | Max Payne (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (45%) | 81% | today | 79% |  |
| 134 | [ ] | Stellar Blade™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | 80% | 1d ago | 81% |  |
| 135 | [ ] | Yakuza: Like a Dragon (STEAM) | 13 | 20 | 65% (last 20) | Does not open (58%) | 69% | 3d ago | 77% |  |
| 136 | [ ] | Stumble Guys (STEAM) | 12 | 20 | 60% (last 20) | Does not open (72%) | 67% | today | 61% |  |
| 137 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 88% | 4d ago | 92% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 138 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 86% | 2d ago | 86% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 139 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 75% | 11d ago | 75% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 140 | [ ] | Tabletop Simulator (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 82% | 3d ago | 84% |  |
| 141 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 93% | 23d ago | 92% |  |
| 142 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (48%) | 78% | 7d ago | 71% |  |
| 143 | [ ] | Pinball FX (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 70% | 5d ago | 69% |  |
| 144 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (79%) | 80% | 20d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 145 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (82%) | 86% | 4d ago | n/a | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 146 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (88%) | 95% | 5d ago | 96% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 147 | [ ] | Sonic Generations (STEAM) | 14 | 20 | 70% (last 20) | Does not open (70%) | 67% | 4d ago | 66% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 148 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 85% | today | 79% |  |
| 149 | [ ] | Heavy Rain (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (65%) | 94% | 7d ago | 89% |  |
| 150 | [ ] | Trailmakers (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | 90% | 1d ago | 92% |  |
| 151 | [ ] | Dishonored - Definitive Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (88%) | 80% | today | 79% |  |
| 152 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | 77% | 9d ago | 75% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 153 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | 70% | 3d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 154 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 85% | 15d ago | 83% |  |
| 155 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | Does not open (43%) | 86% | 1d ago | 86% |  |
| 156 | [ ] | Plague Inc: Evolved (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 66% | 1d ago | 66% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 157 | [ ] | Gambonanza (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 89% | 5d ago | 87% |  |
| 158 | [ ] | Limbus Company (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 86% | 3d ago | 92% |  |
| 159 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 77% | 4d ago | 76% |  |
| 160 | [ ] | Fallout (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 70% | 3d ago | 65% |  |
| 161 | [ ] | Sonic Lost World (STEAM) | 10 | 20 | 50% (last 20) | No graphics (69%) | 81% | 1d ago | 81% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 162 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (60%) | 92% | today | 90% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 163 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (92%) | 63% | 2d ago | 82% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 164 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (54%) | 67% | 6d ago | 72% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 165 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (59%) | 67% | 10d ago | 65% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 166 | [ ] | Necesse (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 62% | today | 65% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 167 | [ ] | Gothic 1 Classic (STEAM) | 12 | 20 | 60% (last 20) | Does not open (59%) | 74% | 13d ago | 65% |  |
| 168 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (82%) | 89% | 3d ago | 89% |  |
| 169 | [ ] | Digimon Survive (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (77%) | 88% | today | 85% |  |
| 170 | [ ] | Raft (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | 91% | today | 88% |  |
| 171 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 60% | 10d ago | 69% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 172 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (55%) | 92% | 17d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 173 | [ ] | Control Ultimate Edition (GOG) | 13 | 20 | 65% (last 20) | Does not open (76%) | 78% | 11d ago | 72% |  |
| 174 | [ ] | Dishonored 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 66% | 2d ago | 59% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 175 | [ ] | Counter-Strike:Global Offensive (STEAM) | 10 | 20 | 50% (last 20) | Does not open (77%) | 65% | today | 62% |  |
| 176 | [ ] | Capcom Arcade Stadium (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | 74% | 9d ago | 79% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 177 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 100% | 32d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 178 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 87% | 10d ago | 83% |  |
| 179 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (76%) | 100% | 12d ago | n/a |  |
| 180 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (46%) | 62% | 1d ago | 67% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 181 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 13 | 20 | 65% (last 20) | Does not open (85%) | 61% | 2d ago | 57% |  |
| 182 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (67%) | 96% | today | 100% |  |
| 183 | [ ] | TurretGirls (STEAM) | 12 | 20 | 60% (last 20) | No graphics (77%) | 91% | 2d ago | 94% |  |
| 184 | [ ] | Escape from Duckov (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (70%) | 95% | 3d ago | 98% |  |
| 185 | [ ] | BioShock 2 Remastered (STEAM) | 10 | 20 | 50% (last 20) | Does not open (84%) | 84% | today | 84% |  |
| 186 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 65% | 3d ago | 72% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 187 | [ ] | Subnautica 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (55%) | 80% | 4d ago | n/a | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 188 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | 88% | 11d ago | 80% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 189 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (71%) | 83% | 4d ago | 80% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 190 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (75%) | 68% | 5d ago | 60% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 191 | [ ] | Supermarket Together (STEAM) | 14 | 20 | 70% (last 20) | Does not open (68%) | 62% | 1d ago | 67% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 192 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (55%) | 76% | today | 76% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 193 | [ ] | One-armed robber (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (69%) | 65% | 1d ago | 54% |  |
| 194 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (59%) | 72% | today | 73% |  |
| 195 | [ ] | Unturned (STEAM) | 11 | 20 | 55% (last 20) | Does not open (44%) | 80% | today | 82% |  |
| 196 | [ ] | Moonring (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 81% | 2d ago | 76% |  |
| 197 | [ ] | Overwatch® (STEAM) | 7 | 10 | 70% (since fix) | Does not open (61%) | 82% | 1d ago | 77% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 198 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 95% | 11d ago | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 199 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (83%) | 61% | 1d ago | 50% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 200 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 76% | 16d ago | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 201 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (65%) | 79% | 17d ago | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 202 | [ ] | Turbo Overkill (STEAM) | 13 | 20 | 65% (last 20) | No graphics (91%) | 100% | today | 100% |  |
| 203 | [ ] | Goat Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 60% | 3d ago | 53% |  |
| 204 | [ ] | The Witcher: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (59%) | 77% | 15d ago | 85% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 205 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (61%) | 67% | 11d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 206 | [ ] | Hotline Miami (GOG) | 14 | 20 | 70% (last 20) | Does not open (89%) | 76% | 4d ago | 82% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 207 | [ ] | Ultimate Custom Night (STEAM) | 14 | 20 | 70% (last 20) | No graphics (72%) | 67% | 2d ago | 50% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 208 | [ ] | Jade Empire: Special Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (93%) | 74% | 6d ago | 62% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 209 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | 75% | 19d ago | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 210 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (91%) | 81% | 35d ago | 73% |  |
| 211 | [ ] | Invisible, Inc. (STEAM) | 15 | 20 | 75% (last 20) | Does not open (63%) | 83% | 23d ago | n/a |  |
| 212 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 75% | 25d ago | 75% |  |
| 213 | [ ] | Return to Monkey Island (STEAM) | 14 | 20 | 70% (last 20) | No graphics (72%) | 74% | 15d ago | 71% |  |
| 214 | [ ] | GOD EATER RESURRECTION (STEAM) | 14 | 20 | 70% (last 20) | Does not open (59%) | 73% | 8d ago | n/a |  |
| 215 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (47%) | 90% | 6d ago | n/a |  |
| 216 | [ ] | Lucid Blocks (STEAM) | 11 | 20 | 55% (last 20) | Does not open (80%) | 60% | 2d ago | 50% |  |
| 217 | [ ] | My Summer Car (STEAM) | 11 | 20 | 55% (last 20) | Does not open (63%) | 78% | 4d ago | 74% |  |
| 218 | [ ] | Warframe (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 81% | 5d ago | 78% |  |
| 219 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 80% | 10d ago | 79% |  |
| 220 | [ ] | MX Bikes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 93% | 4d ago | 95% |  |
| 221 | [ ] | Bongo Cat (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 61% | 1d ago | 47% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 222 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 20 | 80% (last 20) | Does not open (82%) | 60% | 6d ago | 40% (drop) | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 223 | [ ] | Maneater (STEAM) | 14 | 20 | 70% (last 20) | Does not open (86%) | 60% | 1d ago | 63% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 224 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (44%) | 76% | 17d ago | n/a | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 225 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 93% | 12d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 226 | [ ] | Darksiders (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 88% | today | 84% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 227 | [ ] | GUILTY GEAR Xrd REV 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (83%) | 69% | 7d ago | 62% |  |
| 228 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Controller issues (36%) | 90% | 3d ago | n/a |  |
| 229 | [ ] | No Socks RPG (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (91%) | 94% | today | 93% |  |
| 230 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (83%) | 81% | 5d ago | 80% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 231 | [ ] | Capcom Fighting Collection (STEAM) | 13 | 20 | 65% (last 20) | Does not open (86%) | 89% | 2d ago | 86% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 232 | [ ] | Big Walk (STEAM) | 12 | 20 | 60% (last 20) | Does not open (56%) | 67% | 2d ago | 57% |  |
| 233 | [ ] | SnowRunner (STEAM) | 12 | 20 | 60% (last 20) | Does not open (96%) | 71% | 1d ago | 71% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 234 | [ ] | Hylics (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (69%) | 97% | 3d ago | 94% |  |
| 235 | [ ] | BATTLETECH (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 95% | 6d ago | 94% |  |
| 236 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (50%) | 76% | 1d ago | 85% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 237 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 11 | 20 | 55% (last 20) | Does not open (53%) | 75% | 5d ago | 78% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 238 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 95% | 7d ago | 100% |  |
| 239 | [ ] | Tales of Zestiria (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 70% | 27d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 240 | [ ] | Spark the Electric Jester (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 69% | 1d ago | n/a | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 241 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (84%) | 70% | 2d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 242 | [ ] | AER Memories of Old (EPIC) | 13 | 20 | 65% (last 20) | Does not open (86%) | 93% | 6d ago | 92% |  |
| 243 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (71%) | 75% | 7d ago | 73% |  |
| 244 | [ ] | Timberborn (STEAM) | 12 | 20 | 60% (last 20) | No graphics (68%) | 94% | 3d ago | 100% |  |
| 245 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 93% | 14d ago | n/a |  |
| 246 | [ ] | 12 is Better Than 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 77% | 17d ago | n/a |  |
| 247 | [ ] | Hero Siege (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (46%) | 86% | 6d ago | 92% |  |
| 248 | [ ] | Secrets of Grindea (STEAM) | 10 | 20 | 50% (last 20) | Does not open (48%) | 84% | 4d ago | 84% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 249 | [ ] | Zero Escape: The Nonary Games (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 72% | 1d ago | 72% |  |
| 250 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 83% | 8d ago | 78% |  |
| 251 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 84% | 1d ago | 78% |  |
| 252 | [ ] | HITMAN World of Assassination (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 74% | 1d ago | 75% |  |
| 253 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (94%) | 97% | 13d ago | 96% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 254 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 92% | 33d ago | 92% |  |
| 255 | [ ] | Goose Goose Duck (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 79% | 2d ago | 80% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 256 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 12 | 20 | 60% (last 20) | No graphics (39%) | 87% | 5d ago | 90% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 257 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 71% | 9d ago | 67% |  |
| 258 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 62% | 13d ago | 62% |  |
| 259 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 63% | 16d ago | 61% |  |
| 260 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 81% | 4d ago | 85% |  |
| 261 | [ ] | Deus Ex™ GOTY Edition (GOG) | 11 | 20 | 55% (last 20) | No graphics (47%) | 100% | today | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 262 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 93% | 10d ago | 90% |  |
| 263 | [ ] | Rollout Inline (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 67% | 2d ago | 82% |  |
| 264 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 92% | today | 89% |  |
| 265 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 71% | 6d ago | 83% |  |
| 266 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 13 | 20 | 65% (last 20) | Does not open (86%) | 76% | today | 90% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 267 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 65% | 12d ago | 64% |  |
| 268 | [ ] | Sons Of The Forest (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 76% | 7d ago | 72% |  |
| 269 | [ ] | Disgaea 4 Complete+ (STEAM) | 12 | 20 | 60% (last 20) | No graphics (43%) | 93% | today | 92% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 270 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 60% | 6d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 271 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 86% | 12d ago | 86% |  |
| 272 | [ ] | Cat Mail Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 91% | today | 89% |  |
| 273 | [ ] | Super Battle Golf (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 88% | 3d ago | 85% |  |
| 274 | [ ] | CRUEL (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 81% | 7d ago | 80% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 275 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 95% | 7d ago | 100% |  |
| 276 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 100% | 4d ago | 100% |  |
| 277 | [ ] | Sort Them Ducks (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (58%) | 100% | 1d ago | 100% |  |
| 278 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (92%) | 86% | 17d ago | 91% |  |
| 279 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (63%) | 64% | 10d ago | n/a |  |
| 280 | [ ] | Forgive Me Father (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 74% | 8d ago | 64% |  |
| 281 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 85% | 7d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 282 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 75% | 6d ago | 73% |  |
| 283 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 67% | 3d ago | 71% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 284 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 62% | 5d ago | 64% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 285 | [ ] | BioShock 2 Remastered (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 89% | 2d ago | 87% |  |
| 286 | [ ] | Intravenous (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 84% | 13d ago | 87% |  |
| 287 | [ ] | Decktamer (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 75% | 2d ago | n/a |  |
| 288 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 73% | 15d ago | 70% |  |
| 289 | [ ] | Subnautica: Below Zero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 82% | 2d ago | 70% |  |
| 290 | [ ] | Cruelty Squad (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 87% | 5d ago | 82% |  |
| 291 | [ ] | A Plague Tale: Innocence (GOG) | 10 | 20 | 50% (last 20) | Does not open (91%) | 64% | 4d ago | n/a |  |
| 292 | [ ] | Dungeon Siege (STEAM) | 10 | 20 | 50% (last 20) | Does not open (44%) | 100% | 1d ago | 100% |  |
| 293 | [ ] | The Stanley Parable (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 75% | 2d ago | 77% |  |
| 294 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 92% | 1d ago | 95% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 295 | [ ] | Command & Conquer™ Red Alert™ 3 (STEAM) | 10 | 20 | 50% (last 20) | No graphics (38%) | 86% | today | 90% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 296 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 100% | today | 100% |  |
| 297 | [ ] | Pillars of Eternity (STEAM) | 10 | 20 | 50% (last 20) | Does not open (40%) | 100% | 1d ago | 100% |  |
| 298 | [ ] | Haydee (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 79% | 7d ago | n/a |  |
| 299 | [ ] | Helping the Hotties (GOG) | 10 | 20 | 50% (last 20) | Does not open (75%) | 73% | 3d ago | n/a |  |

## Recently recovered (373)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Grim Dawn (STEAM) | 469 | 2026-11-08 | 549 | 67% |  |
| 2 | [x] | FINAL FANTASY RESONANCE (STEAM) | 459 | 2026-10-24 | 1046 | 80% |  |
| 3 | [x] | Half-Life (STEAM) | 371 | 2026-11-09 | 637 | 70% |  |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 265 | 2026-11-14 | 421 | 69% |  |
| 5 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 239 | 2026-11-09 | 333 | 87% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 6 | [x] | MONSTER HUNTER RISE (STEAM) | 228 | 2026-11-17 | 533 | 60% |  |
| 7 | [x] | Alan Wake (STEAM) | 225 | 2026-11-14 | 250 | 71% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 8 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 219 | 2026-11-09 | 375 | 66% |  |
| 9 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 189 | 2026-11-09 | 230 | 55% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 10 | [x] | BeamNG.drive (STEAM) | 187 | 2026-11-09 | 231 | 70% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 11 | [x] | Call of Duty: Black Ops (STEAM) | 187 | 2026-11-13 | 213 | 21% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 12 | [x] | OMORI (STEAM) | 174 | 2026-11-09 | 220 | 68% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 13 | [x] | DRAGON BALL FighterZ (STEAM) | 165 | 2026-11-01 | 212 | 86% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 14 | [x] | Geometry Dash (STEAM) | 161 | 2026-11-11 | 452 | 60% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 15 | [x] | Spelunky 2 (STEAM) | 155 | 2026-11-01 | 198 | 81% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 16 | [x] | BioShock (STEAM) | 151 | 2026-11-09 | 301 | 70% |  |
| 17 | [x] | Sid Meier's Civilization V (STEAM) | 144 | 2026-11-10 | 156 | 62% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 18 | [x] | Team Fortress 2 (STEAM) | 136 | 2026-11-09 | 237 | 77% |  |
| 19 | [x] | Prototype (STEAM) | 134 | 2026-11-11 | 200 | 62% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 20 | [x] | Minecraft Dungeons II (STEAM) | 132 | 2026-11-09 | 151 | 72% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 21 | [x] | Castlevania Advance Collection (STEAM) | 128 | 2026-11-09 | 204 | 89% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 22 | [x] | Aniimo (STEAM) | 116 | 2026-11-09 | 156 | 79% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 23 | [x] | Mirror's Edge (STEAM) | 113 | 2026-11-09 | 168 | 67% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 24 | [x] | Assassin's Creed II (STEAM) | 113 | 2026-11-10 | 118 | 67% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 25 | [x] | Necesse (STEAM) | 106 | 2026-11-22 | 116 | 62% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 26 | [x] | Cave Story+ (STEAM) | 105 | 2026-11-09 | 115 | 76% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 27 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 101 | 2026-11-09 | 142 | 93% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 28 | [x] | The Witcher: Enhanced Edition (STEAM) | 100 | 2026-11-09 | 118 | 77% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 29 | [x] | Happy Wheels (STEAM) | 97 | 2026-11-09 | 117 | 63% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 30 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 95 | 2026-11-15 | 139 | 75% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 31 | [x] | Moonstone Island (STEAM) | 95 | 2026-11-09 | 124 | 71% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 32 | [x] | Fallout: New Vegas PCR (STEAM) | 86 | 2026-11-20 | 114 | 66% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 33 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 81 | 2026-11-09 | 132 | 72% |  |
| 34 | [x] | FINAL FANTASY XIII-2 (STEAM) | 80 | 2026-11-09 | 83 | 63% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 35 | [x] | DOOM 3: BFG Edition (STEAM) | 79 | 2026-11-09 | 122 | 71% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 36 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 78 | 2026-11-09 | 102 | 95% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 37 | [x] | Vital Shell (STEAM) | 77 | 2026-11-09 | 126 | 84% |  |
| 38 | [x] | Psychonauts (STEAM) | 76 | 2026-11-09 | 142 | 94% |  |
| 39 | [x] | Quake (STEAM) | 75 | 2026-11-09 | 230 | 71% |  |
| 40 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 74 | 2026-11-09 | 115 | 78% |  |
| 41 | [x] | Age of Empires II: Definitive Edition (STEAM) | 74 | 2026-11-10 | 94 | 69% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 42 | [x] | Brawlhalla (STEAM) | 73 | 2026-11-09 | 142 | 73% |  |
| 43 | [x] | Cyberpunk 2077 (GOG) | 71 | 2026-11-09 | 95 | 69% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 44 | [x] | Ballionaire (STEAM) | 69 | 2026-11-09 | 118 | 82% |  |
| 45 | [x] | Order of the Sinking Star (STEAM) | 69 | 2026-11-09 | 104 | 66% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 46 | [x] | The Sims™ 4 (STEAM) | 69 | 2026-11-09 | 94 | 70% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 47 | [x] | Stardew Valley (GOG) | 66 | 2026-11-11 | 117 | 80% |  |
| 48 | [x] | Fable - The Lost Chapters (STEAM) | 66 | 2026-11-09 | 108 | 80% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 49 | [x] | Dota 2 (STEAM) | 65 | 2026-11-09 | 100 | 75% |  |
| 50 | [x] | Disgaea 5 Complete (STEAM) | 65 | 2026-11-09 | 76 | 91% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 51 | [x] | Need for Speed: Hot Pursuit (STEAM) | 64 | 2026-11-09 | 98 | 76% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 52 | [x] | STEINS;GATE (STEAM) | 64 | 2026-11-09 | 95 | 82% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 53 | [x] | GRID (STEAM) | 64 | 2026-11-21 | 85 | 49% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 54 | [x] | American Truck Simulator (STEAM) | 63 | 2026-11-09 | 105 | 73% |  |
| 55 | [x] | Diablo® IV (STEAM) | 63 | 2026-11-11 | 75 | 82% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 56 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 62 | 2026-11-11 | 82 | 60% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 57 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 61 | 2026-11-09 | 99 | 83% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 58 | [x] | Caravan SandWitch (EPIC) | 60 | 2026-11-09 | 122 | 67% |  |
| 59 | [x] | Spyro™ Reignited Trilogy (STEAM) | 60 | 2026-11-09 | 106 | 78% |  |
| 60 | [x] | Mini Motorways (STEAM) | 60 | 2026-11-09 | 95 | 64% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 61 | [x] | Poppy Playtime (STEAM) | 59 | 2026-11-09 | 101 | 70% |  |
| 62 | [x] | Call of Duty: World at War (STEAM) | 59 | 2026-11-09 | 83 | 76% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 63 | [x] | Grand Theft Auto V (EPIC) | 59 | 2026-11-09 | 66 | 75% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 64 | [x] | Gunfire Reborn (STEAM) | 59 | 2026-11-09 | 65 | 88% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 65 | [x] | Sovereign Tower (STEAM) | 58 | 2026-11-09 | 112 | 81% |  |
| 66 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 58 | 2026-10-25 | 98 | 77% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 67 | [x] | Deskrawl: Idle ARPG (STEAM) | 58 | 2026-11-09 | 72 | 64% | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 68 | [x] | FINAL FANTASY XIII (STEAM) | 57 | 2026-11-22 | 514 | 59% |  |
| 69 | [x] | Fallout (STEAM) | 57 | 2026-11-09 | 91 | 70% |  |
| 70 | [x] | Borderlands 3 (STEAM) | 57 | 2026-11-09 | 87 | 91% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 71 | [x] | Firewatch (STEAM) | 56 | 2026-11-10 | 110 | 86% |  |
| 72 | [x] | eFootball™ (STEAM) | 56 | 2026-11-09 | 82 | 63% |  |
| 73 | [x] | Call of Juarez Gunslinger (STEAM) | 55 | 2026-11-09 | 68 | 75% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 74 | [x] | A Plague Tale: Innocence (STEAM) | 55 | 2026-11-09 | 58 | 70% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 75 | [x] | Darksiders (STEAM) | 54 | 2026-11-09 | 70 | 88% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 76 | [x] | Sonic Generations (STEAM) | 54 | 2026-11-09 | 61 | 67% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 77 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 53 | 2026-11-09 | 89 | 74% |  |
| 78 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 52 | 2026-11-17 | 77 | 62% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 79 | [x] | MIO: Memories in Orbit (STEAM) | 50 | 2026-11-09 | 103 | 93% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 80 | [x] | Starbound (STEAM) | 50 | 2026-11-09 | 84 | 83% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 81 | [x] | Sol Cesto (EPIC) | 50 | 2026-11-09 | 51 | 88% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 82 | [x] | Last Epoch (STEAM) | 49 | 2026-11-09 | 74 | 62% |  |
| 83 | [x] | Castlevania Anniversary Collection (EPIC) | 48 | 2026-11-21 | 110 | 60% |  |
| 84 | [x] | Okami HD (STEAM) | 48 | 2026-11-09 | 90 | 95% |  |
| 85 | [x] | Oxygen Not Included (STEAM) | 48 | 2026-11-11 | 82 | 70% |  |
| 86 | [x] | TBH: Task Bar Hero (STEAM) | 48 | 2026-11-09 | 74 | 84% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 87 | [x] | Moonlighter (EPIC) | 48 | 2026-11-09 | 52 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 88 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 47 | 2026-11-09 | 81 | 56% |  |
| 89 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 47 | 2026-11-09 | 54 | 100% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 90 | [x] | Overwatch® (STEAM) | 47 | 2026-11-10 | 52 | 82% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 91 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 46 | 2026-11-09 | 80 | 85% |  |
| 92 | [x] | Watch_Dogs 2 (STEAM) | 46 | 2026-11-22 | 51 | 62% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 93 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 45 | 2026-11-13 | 74 | 65% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 94 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 44 | 2026-11-09 | 74 | 82% |  |
| 95 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 44 | 2026-11-09 | 73 | 62% |  |
| 96 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 44 | 2026-11-09 | 68 | 90% |  |
| 97 | [x] | Darkest Dungeon® (EPIC) | 41 | 2026-11-09 | 82 | 89% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 98 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 41 | 2026-11-09 | 58 | 73% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 99 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 40 | 2026-11-09 | 74 | 91% |  |
| 100 | [x] | Borderlands: The Pre-Sequel (STEAM) | 39 | 2026-11-09 | 77 | 62% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 101 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 39 | 2026-11-09 | 62 | 63% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 102 | [x] | Plague Inc: Evolved (STEAM) | 39 | 2026-11-16 | 60 | 66% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 103 | [x] | Dead by Daylight (STEAM) | 39 | 2026-11-09 | 43 | 86% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 104 | [x] | MudRunner (STEAM) | 38 | 2026-10-24 | 93 | 59% |  |
| 105 | [x] | Digimon World: Next Order (STEAM) | 38 | 2026-11-09 | 74 | 86% |  |
| 106 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 38 | 2026-11-09 | 70 | 89% |  |
| 107 | [x] | Tomb Raider: Anniversary (STEAM) | 38 | 2026-11-09 | 63 | 59% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 108 | [x] | Sonic Lost World (STEAM) | 38 | 2026-11-09 | 58 | 81% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 109 | [x] | XCOM 2 (STEAM) | 37 | 2026-11-09 | 63 | 68% |  |
| 110 | [x] | Aggelos (STEAM) | 37 | 2026-11-09 | 53 | 86% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 111 | [x] | Sonic Origins (STEAM) | 36 | 2026-11-09 | 66 | 85% |  |
| 112 | [x] | Age of Empires II (2013) (STEAM) | 36 | 2026-11-09 | 61 | 69% |  |
| 113 | [x] | ROB RUN (STEAM) | 36 | 2026-11-17 | 48 | 66% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 114 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 36 | 2026-11-19 | 38 | 93% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 115 | [x] | Amnesia: The Dark Descent (STEAM) | 35 | 2026-11-09 | 74 | 84% |  |
| 116 | [x] | POSTAL 2 (GOG) | 35 | 2026-11-09 | 66 | 94% |  |
| 117 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 35 | 2026-11-09 | 66 | 83% |  |
| 118 | [x] | Street Fighter™ 6 (STEAM) | 35 | 2026-11-09 | 56 | 79% |  |
| 119 | [x] | Russian Fishing 4 (STEAM) | 35 | 2026-11-09 | 41 | 68% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 120 | [x] | CrossCode (GOG) | 35 | 2026-11-09 | 38 | 80% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 121 | [x] | Monster Hunter Wilds (STEAM) | 35 | 2026-11-09 | 36 | 77% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 122 | [x] | Ace Attorney Investigations Collection (STEAM) | 34 | 2026-11-09 | 62 | 86% |  |
| 123 | [x] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 34 | 2026-11-20 | 62 | 14% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 124 | [x] | FINAL FANTASY VII (2013) (STEAM) | 34 | 2026-11-09 | 51 | 57% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 125 | [x] | Asphalt Legends  (STEAM) | 34 | 2026-11-21 | 38 | 61% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 126 | [x] | Being a DIK (STEAM) | 33 | 2026-11-09 | 73 | 67% |  |
| 127 | [x] | Max Payne (STEAM) | 33 | 2026-11-09 | 55 | 81% |  |
| 128 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 33 | 2026-11-09 | 41 | 92% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 129 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 32 | 2026-11-09 | 59 | 77% |  |
| 130 | [x] | Gauntlet™  (STEAM) | 32 | 2026-11-11 | 47 | 80% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 131 | [x] | SnowRunner (STEAM) | 32 | 2026-11-09 | 45 | 71% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 132 | [x] | Capcom Arcade Stadium (STEAM) | 32 | 2026-11-09 | 42 | 74% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 133 | [x] | Journey (STEAM) | 31 | 2026-10-27 | 70 | 69% |  |
| 134 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 31 | 2026-11-09 | 70 | 73% |  |
| 135 | [x] | COCOON (STEAM) | 31 | 2026-11-09 | 65 | 81% |  |
| 136 | [x] | Hearts of Iron IV (STEAM) | 31 | 2026-11-09 | 64 | 79% |  |
| 137 | [x] | The Bazaar (STEAM) | 31 | 2026-11-09 | 61 | 79% |  |
| 138 | [x] | Yume Nikki (STEAM) | 31 | 2026-11-20 | 56 | 42% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 139 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 31 | 2026-11-09 | 55 | 72% |  |
| 140 | [x] | Earthion (STEAM) | 31 | 2026-11-09 | 53 | 100% |  |
| 141 | [x] | Big Walk (STEAM) | 31 | 2026-11-09 | 52 | 67% |  |
| 142 | [x] | Counter-Strike:Global Offensive (STEAM) | 31 | 2026-11-09 | 47 | 65% |  |
| 143 | [x] | Red Dead Redemption (STEAM) | 31 | 2026-11-09 | 34 | 45% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 144 | [x] | Elite Dangerous (STEAM) | 31 | 2026-11-20 | 33 | 62% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 145 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 30 | 2026-11-09 | 53 | 72% |  |
| 146 | [x] | Hero Siege (STEAM) | 30 | 2026-11-09 | 51 | 86% |  |
| 147 | [x] | Need for Speed™ Rivals (STEAM) | 30 | 2026-11-10 | 42 | 72% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 148 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 29 | 2026-11-09 | 52 | 89% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 149 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 29 | 2026-11-09 | 50 | 94% |  |
| 150 | [x] | Prince of Persia: The Sands of Time (STEAM) | 29 | 2026-11-09 | 49 | 78% |  |
| 151 | [x] | Resident Evil Village (STEAM) | 29 | 2026-11-09 | 49 | 88% |  |
| 152 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 29 | 2026-11-09 | 45 | 83% |  |
| 153 | [x] | Gothic II: Gold Classic (STEAM) | 29 | 2026-11-09 | 37 | 65% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 154 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 67% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 155 | [x] | SurrounDead (STEAM) | 28 | 2026-11-09 | 59 | 91% |  |
| 156 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 28 | 2026-11-09 | 50 | 96% |  |
| 157 | [x] | Secrets of Grindea (STEAM) | 28 | 2026-11-09 | 48 | 84% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 158 | [x] | Supermarket Together (STEAM) | 28 | 2026-11-18 | 41 | 62% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 159 | [x] | Hotline Miami (GOG) | 28 | 2026-11-18 | 35 | 76% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 160 | [x] | Resident Evil Revelations 2 (STEAM) | 27 | 2026-11-09 | 53 | 84% |  |
| 161 | [x] | Heavy Rain (STEAM) | 27 | 2026-11-09 | 46 | 94% |  |
| 162 | [x] | Tower and Sword of Succubus (STEAM) | 27 | 2026-11-09 | 42 | 81% |  |
| 163 | [x] | Digimon Survive (STEAM) | 27 | 2026-11-09 | 40 | 88% |  |
| 164 | [x] | Palia (STEAM) | 27 | 2026-11-09 | 39 | 71% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 165 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 27 | 2026-11-09 | 35 | 62% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 166 | [x] | Skullgirls 2nd Encore (STEAM) | 26 | 2026-11-10 | 63 | 68% |  |
| 167 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 26 | 2026-11-09 | 59 | 87% |  |
| 168 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 45 | 72% |  |
| 169 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 26 | 2026-11-09 | 43 | 68% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 170 | [x] | Dead Rising 2 (STEAM) | 26 | 2026-11-09 | 42 | 70% |  |
| 171 | [x] | Yakuza: Like a Dragon (STEAM) | 26 | 2026-11-09 | 42 | 69% |  |
| 172 | [x] | Frostpunk (STEAM) | 25 | 2026-11-09 | 52 | 77% |  |
| 173 | [x] | Deponia (STEAM) | 25 | 2026-11-09 | 50 | 79% |  |
| 174 | [x] | Cat Mail Co. (STEAM) | 25 | 2026-11-09 | 43 | 91% |  |
| 175 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-19 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 176 | [x] | Chained Echoes (GOG) | 24 | 2026-11-19 | 52 | 65% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 177 | [x] | Lobotomy Corporation (STEAM) | 24 | 2026-11-09 | 47 | 90% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 178 | [x] | Mirror's Edge™ (GOG) | 24 | 2026-11-13 | 46 | 77% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 179 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 24 | 2026-11-09 | 46 | 62% |  |
| 180 | [x] | Lucid Blocks (STEAM) | 24 | 2026-11-09 | 46 | 60% |  |
| 181 | [x] | Battle Brothers (STEAM) | 24 | 2026-11-09 | 44 | 78% |  |
| 182 | [x] | Trailmakers (STEAM) | 24 | 2026-11-09 | 43 | 90% |  |
| 183 | [x] | Guildrun Demo (STEAM) | 24 | 2026-11-09 | 41 | 85% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 184 | [x] | Gambonanza (STEAM) | 24 | 2026-11-09 | 40 | 89% |  |
| 185 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 24 | 2026-11-09 | 38 | 81% |  |
| 186 | [x] | Ratatan (STEAM) | 24 | 2026-11-09 | 37 | 87% |  |
| 187 | [x] | Timberborn (STEAM) | 24 | 2026-11-09 | 35 | 94% |  |
| 188 | [x] | Subnautica 2 (STEAM) | 24 | 2026-11-15 | 28 | 80% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 189 | [x] | Northgard: Definitive Edition (STEAM) | 24 | 2026-11-22 | 27 | 70% | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 190 | [x] | Goat Simulator (STEAM) | 23 | 2026-11-09 | 48 | 60% |  |
| 191 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 46 | 92% |  |
| 192 | [x] | Opus Magnum (STEAM) | 23 | 2026-11-09 | 36 | 100% |  |
| 193 | [x] | Dishonored 2 (STEAM) | 23 | 2026-11-09 | 34 | 66% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 194 | [x] | Jade Empire: Special Edition (GOG) | 23 | 2026-11-09 | 30 | 76% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 195 | [x] | Crab Game (STEAM) | 23 | 2026-11-09 | 27 | 88% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 196 | [x] | Football Manager 2024 (EPIC) | 22 | 2026-11-09 | 40 | 65% |  |
| 197 | [x] | Unturned (STEAM) | 22 | 2026-11-09 | 40 | 80% |  |
| 198 | [x] | Strider (STEAM) | 22 | 2026-11-20 | 38 | 67% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 199 | [x] | My Summer Car (STEAM) | 22 | 2026-11-09 | 37 | 78% |  |
| 200 | [x] | Sorry We're Closed (EPIC) | 22 | 2026-11-09 | 36 | 62% |  |
| 201 | [x] | Limbus Company (STEAM) | 22 | 2026-11-09 | 35 | 86% |  |
| 202 | [x] | Mortal Kombat 11 (STEAM) | 22 | 2026-11-09 | 33 | 67% |  |
| 203 | [x] | Ultimate Custom Night (STEAM) | 22 | 2026-11-19 | 31 | 67% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 204 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 22 | 2026-11-09 | 26 | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 205 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 59 | 97% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 206 | [x] | Prince of Persia (GOG) | 21 | 2026-11-09 | 42 | 74% |  |
| 207 | [x] | Crazy Taxi (STEAM) | 21 | 2026-11-10 | 42 | 66% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 208 | [x] | Control Ultimate Edition (GOG) | 21 | 2026-11-09 | 38 | 78% |  |
| 209 | [x] | Invisible, Inc. (STEAM) | 21 | 2026-11-09 | 37 | 83% |  |
| 210 | [x] | Tabletop Simulator (STEAM) | 21 | 2026-11-09 | 35 | 82% |  |
| 211 | [x] | Deus Ex™ GOTY Edition (GOG) | 21 | 2026-11-09 | 34 | 100% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 212 | [x] | Goose Goose Duck (STEAM) | 21 | 2026-11-18 | 30 | 79% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 213 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 87% |  |
| 214 | [x] | Sapphire Safari (GOG) | 21 | 2026-11-20 | 28 | 70% | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 215 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 21 | 2026-11-09 | 27 | 92% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 216 | [x] | CarX Street (STEAM) | 21 | 2026-11-09 | 26 | 76% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 217 | [x] | Dead Island (STEAM) | 21 | 2026-11-09 | 25 | 83% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 218 | [x] | Tearscape (STEAM) | 21 | 2026-11-09 | 25 | 79% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 219 | [x] | Worms W.M.D (STEAM) | 20 | 2026-11-09 | 38 | 97% |  |
| 220 | [x] | Capcom Fighting Collection 2 (STEAM) | 20 | 2026-11-09 | 37 | 82% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 221 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-11-09 | 37 | 87% |  |
| 222 | [x] | Return to Monkey Island (STEAM) | 20 | 2026-11-09 | 33 | 74% |  |
| 223 | [x] | Maneater (STEAM) | 20 | 2026-11-22 | 31 | 60% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 224 | [x] | CRUEL (STEAM) | 20 | 2026-11-09 | 30 | 81% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 225 | [x] | Torchlight II (EPIC) | 20 | 2026-11-09 | 28 | 81% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 226 | [x] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 20 | 2026-11-22 | 21 | 60% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 227 | [x] | Pinball FX Classic (STEAM) | 19 | 2026-11-09 | 37 | 93% |  |
| 228 | [x] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 2026-11-15 | 36 | 75% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 229 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 32 | 71% |  |
| 230 | [x] | Moonlight Peaks (STEAM) | 19 | 2026-11-09 | 32 | 70% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 231 | [x] | GOD EATER RESURRECTION (STEAM) | 19 | 2026-11-09 | 30 | 73% |  |
| 232 | [x] | Dark Sector (STEAM) | 19 | 2026-11-21 | 25 | 67% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 233 | [x] | Wizard of Legend (EPIC) | 18 | 2026-11-09 | 37 | 78% |  |
| 234 | [x] | Counter-Strike: Condition Zero (STEAM) | 18 | 2026-11-11 | 37 | 29% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 235 | [x] | Mini Metro (STEAM) | 18 | 2026-11-16 | 37 | 61% |  |
| 236 | [x] | One-armed robber (STEAM) | 18 | 2026-11-09 | 33 | 65% |  |
| 237 | [x] | This War of Mine (STEAM) | 18 | 2026-11-17 | 33 | 46% |  |
| 238 | [x] | Far Far West (STEAM) | 18 | 2026-11-09 | 32 | 52% |  |
| 239 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 2026-11-09 | 29 | 87% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 240 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 18 | 2026-11-09 | 28 | 92% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 241 | [x] | Beyond: Two Souls (STEAM) | 18 | 2026-11-22 | 27 | 67% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 242 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-11-09 | 27 | 85% |  |
| 243 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-18 | 23 | 75% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 244 | [x] | Mafia II: Definitive Edition (GOG) | 18 | 2026-11-15 | 20 | 60% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 245 | [x] | Jade Empire: Special Edition (STEAM) | 18 | 2026-11-09 | 20 | 74% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 246 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 17 | 2026-10-25 | 44 | 74% |  |
| 247 | [x] | Backpack Battles (STEAM) | 17 | 2026-11-09 | 40 | 93% |  |
| 248 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 36 | 36% |  |
| 249 | [x] | Intravenous 2 (STEAM) | 17 | 2026-11-09 | 33 | 100% |  |
| 250 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 33 | 86% |  |
| 251 | [x] | Titanfall® 2 (STEAM) | 17 | 2026-11-09 | 32 | 69% |  |
| 252 | [x] | Party Animals (STEAM) | 17 | 2026-11-09 | 25 | 76% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 253 | [x] | Bongo Cat (STEAM) | 17 | 2026-11-20 | 24 | 61% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 254 | [x] | Tales of Zestiria (STEAM) | 17 | 2026-11-09 | 23 | 70% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 255 | [x] | Darksiders Warmastered Edition (EPIC) | 17 | 2026-11-22 | 22 | 60% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 256 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 16 | 2026-11-11 | 35 | 74% |  |
| 257 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 258 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 16 | 2026-11-09 | 30 | 71% |  |
| 259 | [x] | PAYDAY: The Heist (STEAM) | 16 | 2026-11-13 | 28 | 75% |  |
| 260 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 71% |  |
| 261 | [x] | Capcom Fighting Collection (STEAM) | 16 | 2026-11-09 | 23 | 89% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 262 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 16 | 2026-11-09 | 23 | 76% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 263 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 264 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 265 | [x] | Flotsam (EPIC) | 15 | 2026-11-20 | 34 | 42% |  |
| 266 | [x] | sobosuba (STEAM) | 15 | 2026-11-09 | 34 | 85% |  |
| 267 | [x] | Mark of the Ninja (STEAM) | 15 | 2026-10-26 | 31 | 83% |  |
| 268 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 30 | 96% |  |
| 269 | [x] | Tiny Glade (STEAM) | 15 | 2026-11-09 | 30 | 71% |  |
| 270 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 15 | 2026-11-20 | 29 | 90% |  |
| 271 | [x] | AER Memories of Old (EPIC) | 15 | 2026-11-09 | 24 | 93% |  |
| 272 | [x] | Alabaster Dawn Demo (STEAM) | 15 | 2026-11-09 | 23 | 75% |  |
| 273 | [x] | Need for Speed™ Unbound (STEAM) | 15 | 2026-11-09 | 23 | 58% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 274 | [x] | Nex Machina (STEAM) | 15 | 2026-11-09 | 23 | 76% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 275 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 93% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 276 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 277 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 278 | [x] | Faster Than Light (EPIC) | 14 | 2026-11-09 | 31 | 90% |  |
| 279 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 94% |  |
| 280 | [x] | SWORN (STEAM) | 14 | 2026-11-09 | 29 | 94% |  |
| 281 | [x] | Castle in the Clouds (STEAM) | 14 | 2026-11-09 | 28 | 64% |  |
| 282 | [x] | Human Fall Flat (STEAM) | 14 | 2026-10-29 | 28 | 63% |  |
| 283 | [x] | WORLD OF FINAL FANTASY (STEAM) | 14 | 2026-11-09 | 28 | 88% |  |
| 284 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 14 | 2026-11-09 | 27 | 61% |  |
| 285 | [x] | Ultrapool (STEAM) | 14 | 2026-11-09 | 27 | n/a |  |
| 286 | [x] | Another World: 20th Anniversary Edition (GOG) | 14 | 2026-11-21 | 24 | 64% |  |
| 287 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-11-09 | 23 | 93% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 288 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 14 | 2026-11-15 | 23 | 63% |  |
| 289 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 290 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 2026-11-16 | 22 | 100% |  |
| 291 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 21 | 65% |  |
| 292 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 293 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 294 | [x] | Spark the Electric Jester (STEAM) | 14 | 2026-11-13 | 20 | 69% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 295 | [x] | Overlord (STEAM) | 13 | 2026-11-08 | 30 | 56% |  |
| 296 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 29 | 83% |  |
| 297 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 13 | 2026-11-09 | 28 | 91% |  |
| 298 | [x] | Blaster Master Zero (STEAM) | 13 | 2026-11-11 | 27 | 79% |  |
| 299 | [x] | Evoland (STEAM) | 13 | 2026-11-11 | 26 | n/a |  |
| 300 | [x] | MX Bikes (STEAM) | 13 | 2026-11-09 | 26 | 93% |  |
| 301 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 26 | 95% |  |
| 302 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 13 | 2026-11-13 | 26 | 60% |  |
| 303 | [x] | Batman™: Arkham Origins (GOG) | 13 | 2026-11-09 | 25 | 93% |  |
| 304 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 24 | 76% |  |
| 305 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 306 | [x] | Shift At Midnight (STEAM) | 13 | 2026-11-09 | 21 | 90% |  |
| 307 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 70% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 308 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 93% |  |
| 309 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 310 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 2026-11-09 | 20 | 85% |  |
| 311 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-11-16 | 20 | 92% |  |
| 312 | [x] | Turbo Overkill (STEAM) | 13 | 2026-11-09 | 20 | 100% |  |
| 313 | [x] | GRIP: Combat Racing (STEAM) | 12 | 2026-11-09 | 31 | 77% |  |
| 314 | [x] | Antichamber (STEAM) | 12 | 2026-11-18 | 27 | 80% |  |
| 315 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-10 | 24 | 62% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 316 | [x] | Cruelty Squad (STEAM) | 12 | 2026-11-09 | 24 | 87% |  |
| 317 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 24 | 64% |  |
| 318 | [x] | Sonic Superstars (STEAM) | 12 | 2026-11-21 | 24 | 62% |  |
| 319 | [x] | A Plague Tale: Innocence (GOG) | 12 | 2026-11-18 | 23 | 64% |  |
| 320 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-11-09 | 23 | 92% |  |
| 321 | [x] | Legend of Grimrock 2 (STEAM) | 12 | 2026-11-09 | 23 | 93% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 322 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 323 | [x] | Horny Villa (STEAM) | 12 | 2026-11-09 | 21 | 86% |  |
| 324 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 325 | [x] | 12 is Better Than 6 (STEAM) | 12 | 2026-11-09 | 20 | 77% |  |
| 326 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 327 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 2026-11-10 | 20 | 60% |  |
| 328 | [x] | War of Dots (STEAM) | 12 | 2026-11-22 | 20 | 60% | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 329 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 29 | 92% |  |
| 330 | [x] | Alan Wake's American Nightmare (EPIC) | 11 | 2026-11-09 | 24 | 70% |  |
| 331 | [x] | GRANDIA HD Remaster (STEAM) | 11 | 2026-11-09 | 24 | 88% |  |
| 332 | [x] | HITMAN World of Assassination (STEAM) | 11 | 2026-11-09 | 23 | 74% |  |
| 333 | [x] | Life is Strange Remastered (STEAM) | 11 | 2026-11-09 | 23 | 86% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 334 | [x] | Ready or Not (STEAM) | 11 | 2026-11-09 | 23 | 82% |  |
| 335 | [x] | Lost Castle 2 (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 336 | [x] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 2026-11-18 | 21 | 71% |  |
| 337 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 11 | 2026-10-27 | 21 | 86% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 338 | [x] | Forgive Me Father (STEAM) | 11 | 2026-11-15 | 21 | 74% |  |
| 339 | [x] | Haydee (STEAM) | 11 | 2026-11-09 | 21 | 79% |  |
| 340 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 341 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-11-09 | 20 | 73% |  |
| 342 | [x] | The Stanley Parable (STEAM) | 11 | 2026-11-13 | 20 | 75% |  |
| 343 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 28 | 90% |  |
| 344 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 10 | 2026-10-27 | 25 | 81% |  |
| 345 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 25 | 91% |  |
| 346 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 10 | 2026-11-09 | 24 | 88% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 347 | [x] | Breath of Fire IV (GOG) | 10 | 2026-10-26 | 24 | 61% |  |
| 348 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 10 | 2026-10-23 | 23 | 88% |  |
| 349 | [x] | Soul's Remnant (STEAM) | 10 | 2026-11-11 | 22 | n/a |  |
| 350 | [x] | DiRT 4 (STEAM) | 10 | 2026-11-09 | 21 | 100% |  |
| 351 | [x] | UNDEFEATED (STEAM) | 10 | 2026-11-09 | 21 | 70% |  |
| 352 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 353 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 354 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 20 | 84% |  |
| 355 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 356 | [x] | Pillars of Eternity (STEAM) | 10 | 2026-11-21 | 20 | 100% |  |
| 357 | [x] | Secret of Mana (STEAM) | 10 | 2026-11-18 | 20 | 70% |  |
| 358 | [x] | Rayman Origins (GOG) | 9 | 2026-11-09 | 24 | 64% |  |
| 359 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 9 | 2026-11-01 | 24 | n/a |  |
| 360 | [x] | Guacamelee! Gold Edition (STEAM) | 9 | 2026-11-11 | 22 | 75% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 361 | [x] | Need for Speed: Undercover (STEAM) | 9 | 2026-11-11 | 22 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 362 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 9 | 2026-11-09 | 21 | 68% |  |
| 363 | [x] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 9 | 2026-11-17 | 20 | 33% |  |
| 364 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 27% |  |
| 365 | [x] | Lust Goddess (STEAM) | 8 | 2026-11-09 | 22 | 75% |  |
| 366 | [x] | Aperture Desk Job (STEAM) | 8 | 2026-11-03 | 21 | n/a |  |
| 367 | [x] | SteamWorld Heist (GOG) | 8 | 2026-10-25 | 20 | n/a |  |
| 368 | [x] | Ultimate Chicken Horse (STEAM) | 7 | 2026-10-23 | 26 | 91% |  |
| 369 | [x] | Possessor(s) (STEAM) | 7 | 2026-10-24 | 24 | 70% |  |
| 370 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 22 | 51% |  |
| 371 | [x] | SCP – Containment Breach (STEAM) | 7 | 2026-10-27 | 21 | 91% |  |
| 372 | [x] | Mina the Hollower (GOG) | 7 | 2026-10-28 | 20 | 74% |  |
| 373 | [x] | CULTIC (STEAM) | 7 | 2026-11-09 | 20 | 53% |  |
