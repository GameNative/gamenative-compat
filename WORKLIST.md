# GameNative compatibility worklist

Generated: `2026-11-23T04:15:12.383Z` · Ratings since: `2026-08-25T04:15:12.383Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Probably does not work | 186 |
| Fix shipped, waiting for ratings | 15 |
| First launch fails | 296 |
| Mixed | 466 |
| Works | 1024 |
| Total | 2116 |

## Does not work (129)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 138 | 166 | 83% (14d) | Does not open (83%) | 46% | today | 31% | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 188 | 220 | 85% (since fix) | Does not open (92%) | 41% | today | 35% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 3 | [ ] | Rocket League® (EPIC) | 89 | 101 | 88% (14d) | Does not open (81%) | 34% | today | 27% | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 4 | [ ] | Melvor Idle 2: A RuneScape Adventure (STEAM) | 37 | 38 | 97% (14d) | Does not open (97%) | 38% | today | 36% | [#543](https://github.com/GameNative/gamenative-compat/issues/543) |
| 5 | [ ] | DREDGE (EPIC) | 32 | 37 | 86% (14d) | Does not open (79%) | 53% | today | 47% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 6 | [ ] | Hogwarts Legacy (STEAM) | 29 | 31 | 94% (14d) | Does not open (71%) | 26% | 2d ago | 17% | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 7 | [x] 2026-10-18 | Project Zomboid (STEAM) | 62 | 68 | 91% (since fix) | Does not open (63%) | 38% | today | 36% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 8 | [ ] | Mark of the Deep (EPIC) | 22 | 28 | 79% (14d) | Does not open (90%) | 25% | 1d ago | 23% | [#549](https://github.com/GameNative/gamenative-compat/issues/549) |
| 9 | [ ] | Horizon Chase Turbo (EPIC) | 21 | 26 | 81% (14d) | Does not open (84%) | 54% | 2d ago | 45% | [#546](https://github.com/GameNative/gamenative-compat/issues/546) |
| 10 | [ ] | Absolute Drift (EPIC) | 21 | 30 | 70% (14d) | No graphics (60%) | 54% | today | 33% (drop) |  |
| 11 | [ ] | BioShock Remastered (EPIC) | 21 | 27 | 78% (14d) | Does not open (67%) | 56% | today | 51% | [#547](https://github.com/GameNative/gamenative-compat/issues/547) |
| 12 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 20 | 20 | 100% (last 20) | Does not open (96%) | 26% | today | 20% | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 13 | [ ] | Driver: Parallel Lines (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | 40% | 1d ago | 46% | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 14 | [ ] | Metro: Last Light Redux (STEAM) | 20 | 20 | 100% (last 20) | Does not open (93%) | 24% | today | 27% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 15 | [ ] | Bloons TD 6 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (77%) | 36% | today | 24% | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 16 | [ ] | Borderlands 2 (EPIC) | 18 | 20 | 90% (14d) | Does not open (80%) | 52% | 1d ago | 45% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 17 | [ ] | Saints Row 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | 28% | today | 28% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 18 | [ ] | Path of Exile (STEAM) | 18 | 20 | 90% (last 20) | Does not open (89%) | 28% | 3d ago | 25% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 19 | [ ] | Sifu (EPIC) | 16 | 21 | 76% (14d) | Does not open (72%) | 42% | today | 34% | [#535](https://github.com/GameNative/gamenative-compat/issues/535) |
| 20 | [ ] | River City Girls (EPIC) | 15 | 20 | 75% (last 20) | Does not open (50%) | 53% | 1d ago | 38% | [#550](https://github.com/GameNative/gamenative-compat/issues/550) |
| 21 | [ ] | Castlevania Anniversary Collection (EPIC) | 18 | 20 | 90% (last 20) | Does not open (79%) | 56% | 1d ago | 38% |  |
| 22 | [ ] | Saints Row 2 (GOG) | 15 | 20 | 75% (last 20) | Does not open (90%) | 35% | today | 33% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 23 | [ ] | Dead Island 2 (EPIC) | 20 | 20 | 100% (last 20) | Does not open (86%) | 53% | today | 40% | [#552](https://github.com/GameNative/gamenative-compat/issues/552) |
| 24 | [ ] | Vampire Survivors (EPIC) | 17 | 20 | 85% (last 20) | Does not open (63%) | 40% | today | 31% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 25 | [ ] | Mafia II (Classic) (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 8% | 5d ago | 11% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 26 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (78%) | 0% | 14d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 27 | [ ] | Hogwarts Legacy (EPIC) | 17 | 20 | 85% (last 20) | Does not open (77%) | 45% | today | 36% | [#537](https://github.com/GameNative/gamenative-compat/issues/537) |
| 28 | [ ] | skate. (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | 11% | 1d ago | 11% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 29 | [ ] | Call of Duty: Black Ops II (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 43% | 2d ago | 43% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 30 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 56% | 4d ago | 57% | [#553](https://github.com/GameNative/gamenative-compat/issues/553) |
| 31 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | 52% | 1d ago | 49% | [#548](https://github.com/GameNative/gamenative-compat/issues/548) |
| 32 | [ ] | Forza Horizon 4 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (43%) | 42% | today | 22% (drop) | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 33 | [ ] | Teenage Mutant Ninja Turtles: Shredder's Revenge (EPIC) | 15 | 20 | 75% (last 20) | Does not open (83%) | 46% | today | 43% | [#551](https://github.com/GameNative/gamenative-compat/issues/551) |
| 34 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (91%) | 21% | 9d ago | 14% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 35 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 10 | 14 | 71% (since fix) | Does not open (91%) | 42% | 3d ago | 45% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 36 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (78%) | 6% | 8d ago | 8% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 37 | [ ] | Trackmania (STEAM) | 17 | 20 | 85% (last 20) | Does not open (85%) | 27% | 1d ago | 28% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 38 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 35% | today | 27% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 39 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 52% | 1d ago | 58% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 40 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 16 | 20 | 80% (last 20) | Does not open (45%) | 56% | 4d ago | 75% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 41 | [ ] | Fall Guys (EPIC) | 20 | 20 | 100% (last 20) | Does not open (68%) | 8% | today | 5% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 42 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (71%) | 20% | 4d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 43 | [ ] | Kenshi (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 7% | 1d ago | 6% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 44 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 8% | 11d ago | 5% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 45 | [ ] | Detroit: Become Human (STEAM) | 18 | 20 | 90% (last 20) | Does not open (75%) | 50% | 5d ago | 54% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 46 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (70%) | 17% | 1d ago | 19% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 47 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 54% | 1d ago | 49% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 48 | [ ] | Breath of Fire IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (64%) | 15% | 3d ago | 10% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 49 | [ ] | The Witcher: Enhanced Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (76%) | 8% | 1d ago | 10% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 50 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (72%) | 0% | 8d ago | 0% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 51 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (94%) | 12% | 5d ago | 0% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 52 | [ ] | Call of Duty® (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | 0% | 2d ago | 0% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 53 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (68%) | 7% | 22d ago | 9% | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 54 | [ ] | MECCHA CHAMELEON (STEAM) | 15 | 20 | 75% (last 20) | Does not open (70%) | 40% | 5d ago | 35% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 55 | [ ] | Deliver At All Costs (EPIC) | 14 | 20 | 70% (last 20) | Does not open (62%) | 43% | 2d ago | 47% | [#538](https://github.com/GameNative/gamenative-compat/issues/538) |
| 56 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (82%) | 8% | 1d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 57 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (70%) | 23% | 9d ago | 25% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 58 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (80%) | 11% | 14d ago | 14% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 59 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (60%) | 18% | today | n/a | [#536](https://github.com/GameNative/gamenative-compat/issues/536) |
| 60 | [ ] | Borderlands GOTY (STEAM) | 16 | 20 | 80% (last 20) | Does not open (94%) | 35% | 3d ago | 47% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 61 | [ ] | Blood Omen: Legacy of Kain (GOG) | 16 | 20 | 80% (last 20) | No graphics (57%) | 55% | 4d ago | 55% | [#539](https://github.com/GameNative/gamenative-compat/issues/539) |
| 62 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (82%) | 43% | 5d ago | 45% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 63 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 40% | 2d ago | 48% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 64 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (88%) | 54% | 2d ago | 52% | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 65 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (74%) | 42% | today | 43% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 66 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (77%) | 5% | 1d ago | 6% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 67 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | 0% | 9d ago | 0% | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 68 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (54%) | 29% | 5d ago | 18% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 69 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (67%) | 22% | 11d ago | 23% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 70 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 33% | today | 38% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 71 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | 55% | today | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 72 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | 0% | 8d ago | 0% | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 73 | [ ] | Half-Life: Blue Shift (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | 36% | 6d ago | 42% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 74 | [ ] | Rivals of Aether II (STEAM) | 16 | 20 | 80% (last 20) | Does not open (51%) | 36% | 6d ago | 10% (drop) | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 75 | [ ] | Black Mesa (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 33% | 1d ago | 33% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 76 | [ ] | Rise of the Tomb Raider: 20 Year Celebration (EPIC) | 14 | 20 | 70% (last 20) | Does not open (73%) | 40% | today | 34% |  |
| 77 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | 10% | 10d ago | 10% | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 78 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 50% | 9d ago | 53% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 79 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (47%) | 48% | 2d ago | 45% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 80 | [ ] | A Plague Tale: Innocence (EPIC) | 14 | 20 | 70% (last 20) | Does not open (70%) | 48% | today | 43% |  |
| 81 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | 21% | 11d ago | 12% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 82 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 18% | 32d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 83 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 19 | 20 | 95% (last 20) | Does not open (85%) | 45% | 6d ago | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 84 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 18% | today | n/a | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 85 | [ ] | XCOM: Enemy Unknown (STEAM) | 18 | 20 | 90% (last 20) | Does not open (69%) | 15% | 9d ago | n/a | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 86 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (73%) | 28% | 16d ago | 21% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 87 | [ ] | Watch_Dogs (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | 34% | 3d ago | 40% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 88 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | Does not open (63%) | 26% | 2d ago | 27% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 89 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | 8% | 21d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 90 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | 27% | 1d ago | 23% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 91 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 59% | 12d ago | 36% (drop) | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 92 | [ ] | Umamusume: Pretty Derby (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 48% | 3d ago | 50% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 93 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (50%) | 53% | 4d ago | 59% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 94 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 3% | 1d ago | 1% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 95 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 15% | 23d ago | 0% | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 96 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | 33% | today | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 97 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 32% | 2d ago | 35% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 98 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (73%) | 0% | 36d ago | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 99 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (64%) | 46% | 3d ago | 46% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 100 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (62%) | 0% | 4d ago | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 101 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (89%) | 21% | today | 12% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 102 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (84%) | 3% | 1d ago | 3% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 103 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (61%) | 40% | 11d ago | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 104 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 21% | 3d ago | 17% | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 105 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 19 | 20 | 95% (last 20) | No graphics (59%) | 33% | today | 41% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 106 | [ ] | Aliens vs. Predator (STEAM) | 17 | 20 | 85% (last 20) | Does not open (67%) | 31% | 1d ago | 35% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 107 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 7% | 29d ago | 8% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 108 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 20 | 80% (last 20) | Does not open (53%) | 43% | 2d ago | 33% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 109 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | 20% | 21d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 110 | [ ] | Lost Planet: Extreme Condition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | 47% | 8d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 111 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (55%) | 44% | 11d ago | 20% (drop) | [#540](https://github.com/GameNative/gamenative-compat/issues/540) |
| 112 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | 30% | today | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 113 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (89%) | 28% | 7d ago | 33% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 114 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 27% | 1d ago | 36% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 115 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 58% | 26d ago | 43% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 116 | [ ] | OneShot (STEAM) | 15 | 20 | 75% (last 20) | Does not open (96%) | 20% | 2d ago | n/a | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 117 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (86%) | 31% | 23d ago | 25% | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 118 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 47% | 1d ago | 41% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 119 | [ ] | Maneater (EPIC) | 17 | 20 | 85% (last 20) | Does not open (73%) | 32% | today | 20% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 120 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | 31% | 12d ago | 30% | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 121 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 57% | 11d ago | 54% | [#554](https://github.com/GameNative/gamenative-compat/issues/554) |
| 122 | [ ] | Beyond Good & Evil™ (GOG) | 17 | 20 | 85% (last 20) | Does not open (100%) | 17% | 4d ago | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 123 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 20 | 80% (last 20) | Does not open (82%) | 50% | 7d ago | 33% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 124 | [ ] | Maneater (STEAM) | 14 | 20 | 70% (last 20) | Does not open (86%) | 59% | 2d ago | 62% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 125 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 14 | 20 | 70% (last 20) | Does not open (100%) | 40% | today | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 126 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (73%) | 57% | 14d ago | 67% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 127 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (54%) | 40% | 8d ago | 27% | [#541](https://github.com/GameNative/gamenative-compat/issues/541) |
| 128 | [ ] | Ghostwire Tokyo (EPIC) | 15 | 20 | 75% (last 20) | Does not open (91%) | 45% | today | 33% | [#544](https://github.com/GameNative/gamenative-compat/issues/544) |
| 129 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 20 | 70% (last 20) | Does not open (70%) | 42% | 15d ago | 42% | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |

## Probably does not work (186)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Buckshot Roulette (STEAM) | 42 | 61 | 69% (14d) | Does not open (69%) | 57% | today | 44% |  |
| 2 | [ ] | Counter-Strike 2 (STEAM) | 53 | 77 | 69% (since fix) | Does not open (68%) | 55% | today | 57% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 3 | [ ] | Owlboy (STEAM) | 19 | 28 | 68% (14d) | Does not open (81%) | 51% | today | 48% | [#545](https://github.com/GameNative/gamenative-compat/issues/545) |
| 4 | [ ] | Metro 2033 Redux (STEAM) | 15 | 25 | 60% (14d) | Does not open (72%) | 41% | today | 41% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 5 | [ ] | Bully: Scholarship Edition (STEAM) | 14 | 21 | 67% (14d) | Does not open (67%) | 35% | today | 14% (drop) |  |
| 6 | [ ] | theHunter Classic (STEAM) | 20 | 20 | 100% (last 20) | No graphics (92%) | n/a | 19d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 7 | [ ] | Garry's Mod (STEAM) | 16 | 25 | 64% (since fix) | Does not open (79%) | 51% | today | 44% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 8 | [ ] | To The Moon (GOG) | 18 | 20 | 90% (last 20) | Does not open (86%) | n/a | 20d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 9 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 13 | 20 | 65% (last 20) | Does not open (78%) | 52% | today | 48% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 10 | [ ] | Batman™ Arkham Asylum Game of the Year Edition (EPIC) | 11 | 20 | 55% (last 20) | Does not open (75%) | 50% | today | 40% |  |
| 11 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 13 | 20 | 65% (last 20) | Does not open (64%) | 47% | today | 42% |  |
| 12 | [ ] | VRChat (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 38% | today | 36% |  |
| 13 | [ ] | Cat Quest (EPIC) | 11 | 20 | 55% (last 20) | Does not open (50%) | 45% | today | 41% |  |
| 14 | [ ] | Asterigos: Curse of the Stars (STEAM) | 16 | 20 | 80% (last 20) | Graphics glitches (73%) | n/a | 1d ago | n/a |  |
| 15 | [ ] | Bad Cheese (EPIC) | 13 | 20 | 65% (last 20) | Does not open (92%) | 45% | today | 33% |  |
| 16 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 16 | 24 | 67% (since fix) | Does not open (78%) | 38% | today | 41% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 17 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 8 | 12 | 67% (since fix) | Does not open (82%) | 59% | 1d ago | 60% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 18 | [ ] | Catherine Classic (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (40%) | 47% | today | 40% |  |
| 19 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 43d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 20 | [ ] | STAR WARS™ Knights of the Old Republic™ II: The Sith Lords™ (STEAM) | 12 | 20 | 60% (last 20) | No graphics (64%) | 51% | 2d ago | 40% |  |
| 21 | [ ] | Darksiders Warmastered Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 50% | today | 38% |  |
| 22 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (38%) | n/a | 2d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 23 | [ ] | Sonic Adventure™ 2  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (77%) | 47% | today | 40% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 24 | [ ] | Gorilla Tag (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 15% | 8d ago | 8% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 25 | [ ] | Art of Rally (EPIC) | 12 | 20 | 60% (last 20) | Does not open (77%) | 39% | today | 37% |  |
| 26 | [ ] | MudRunner (EPIC) | 12 | 20 | 60% (last 20) | Does not open (65%) | 49% | today | 42% |  |
| 27 | [ ] | DOOM 64 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (60%) | 47% | 4d ago | 36% |  |
| 28 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 9d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 29 | [ ] | Door Kickers 2 (STEAM) | 18 | 20 | 90% (last 20) | No graphics (86%) | n/a | today | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 30 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 11 | 20 | 55% (last 20) | Does not open (73%) | 48% | 1d ago | 41% |  |
| 31 | [ ] | Metro 2033 Redux (EPIC) | 13 | 20 | 65% (last 20) | Does not open (64%) | 31% | today | 34% |  |
| 32 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (80%) | 56% | 2d ago | 50% |  |
| 33 | [ ] | Hi-Fi RUSH (STEAM) | 13 | 20 | 65% (last 20) | Does not open (77%) | 41% | today | 41% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 34 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (49%) | 56% | 9d ago | 39% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 35 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 27d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 36 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (100%) | n/a | today | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 37 | [ ] | Phasmophobia (STEAM) | 12 | 20 | 60% (last 20) | Does not open (56%) | 56% | 1d ago | 50% |  |
| 38 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 11 | 20 | 55% (last 20) | Does not open (72%) | 37% | 1d ago | 39% |  |
| 39 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | No graphics (58%) | n/a | 26d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 40 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | No graphics (38%) | 45% | 1d ago | 33% |  |
| 41 | [ ] | Counter-Strike (STEAM) | 11 | 20 | 55% (last 20) | Does not open (68%) | 33% | 2d ago | 30% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 42 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 16d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 43 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 12 | 20 | 60% (last 20) | Does not open (85%) | 47% | 3d ago | 23% (drop) | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 44 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 24d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 45 | [ ] | CPM 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (88%) | 3% | 1d ago | 3% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 46 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (92%) | n/a | 6d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 47 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | n/a | 15d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 48 | [ ] | Legacy of Kain: Defiance Remastered (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (69%) | n/a | 1d ago | n/a |  |
| 49 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (91%) | 57% | 4d ago | 48% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 50 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | n/a | 8d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 51 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 18d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 52 | [ ] | CODE VEIN (STEAM) | 13 | 20 | 65% (last 20) | Does not open (68%) | 26% | 7d ago | 13% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 53 | [ ] | No More Heroes (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 39% | today | 33% |  |
| 54 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (83%) | 55% | 13d ago | n/a |  |
| 55 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (66%) | n/a | 21d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 56 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | n/a | 8d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 57 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 27% | today | n/a |  |
| 58 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (93%) | n/a | 1d ago | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 59 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 12d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 60 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 20d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 61 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (73%) | n/a | 42d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 62 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | 9d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 63 | [ ] | Grim Dawn (GOG) | 13 | 20 | 65% (last 20) | Does not open (69%) | 50% | 7d ago | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 64 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 40d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 65 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 41d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 66 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 4d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 67 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | n/a | 9d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 68 | [ ] | Alpha Protocol (STEAM) | 17 | 20 | 85% (last 20) | No graphics (53%) | n/a | 28d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 69 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (58%) | n/a | 8d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 70 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | n/a | 12d ago | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 71 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 38% | 6d ago | 28% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 72 | [ ] | Dead Space 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 33% | 2d ago | 30% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 73 | [ ] | Metro 2033 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (62%) | 36% | 2d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 74 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 40d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 75 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (56%) | n/a | 9d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 76 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | 24d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 77 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (75%) | n/a | 40d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 78 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 26d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 79 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | 55% | 15d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 80 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 13 | 20 | 65% (last 20) | Does not open (85%) | 58% | 3d ago | 53% |  |
| 81 | [ ] | METAL SLUG 3 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (81%) | 57% | 10d ago | 63% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 82 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (91%) | n/a | 43d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 83 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 9d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 84 | [ ] | Borderlands 2 RU (STEAM) | 18 | 20 | 90% (last 20) | Does not open (57%) | n/a | 6d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 85 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | 5d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 86 | [ ] | DOOM Eternal (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | n/a | today | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 87 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 14d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 88 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 26d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 89 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 45% | 19d ago | n/a |  |
| 90 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (71%) | 26% | 13d ago | 19% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 91 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (92%) | 36% | 7d ago | 30% |  |
| 92 | [ ] | Euro Truck Simulator (STEAM) | 20 | 20 | 100% (last 20) | Does not open (86%) | n/a | 7d ago | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 93 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 51d ago | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 94 | [ ] | Peggle Nights (STEAM) | 20 | 20 | 100% (last 20) | Does not open (93%) | n/a | 1d ago | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 95 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 22d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 96 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (50%) | n/a | 22d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 97 | [ ] | Beholder (EPIC) | 18 | 20 | 90% (last 20) | No graphics (63%) | n/a | 2d ago | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 98 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | n/a | 45d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 99 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | n/a | 5d ago | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 100 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (96%) | n/a | 21d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 101 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (61%) | n/a | 49d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 102 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | n/a | 1d ago | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 103 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (80%) | n/a | 7d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 104 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (54%) | n/a | 28d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 105 | [ ] | Goat Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 54% | 4d ago | 50% |  |
| 106 | [ ] | Hollow Knight: Silksong (GOG) | 10 | 20 | 50% (last 20) | Does not open (69%) | 50% | 1d ago | 47% |  |
| 107 | [ ] | The Survivalists (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | n/a | 10d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 108 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | n/a | 2d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 109 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | n/a | 6d ago | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 110 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 18d ago | n/a |  |
| 111 | [ ] | Brutal Legend (GOG) | 16 | 20 | 80% (last 20) | Does not open (82%) | n/a | 1d ago | n/a |  |
| 112 | [ ] | Super Meat Boy Forever (EPIC) | 10 | 20 | 50% (last 20) | Does not open (83%) | 38% | 3d ago | 26% |  |
| 113 | [ ] | Bionic Commando Rearmed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (76%) | n/a | 33d ago | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 114 | [ ] | Undisputed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | n/a | 15d ago | n/a | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 115 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | n/a | 16d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 116 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (53%) | n/a | 16d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 117 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (80%) | n/a | 13d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 118 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 11d ago | n/a |  |
| 119 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 13 | 20 | 65% (last 20) | Does not open (89%) | n/a | today | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 120 | [ ] | CS2D (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | n/a | today | n/a |  |
| 121 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 14d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 122 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | n/a | 11d ago | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 123 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 24d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 124 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (36%) | n/a | 1d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 125 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 25d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 126 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (47%) | n/a | 7d ago | n/a |  |
| 127 | [ ] | Drop Duchy (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 10% | 4d ago | n/a |  |
| 128 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 18d ago | n/a |  |
| 129 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 18d ago | n/a |  |
| 130 | [ ] | Mafia: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 34% | today | 31% |  |
| 131 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 58% | 4d ago | 70% | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 132 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Controller issues (36%) | n/a | 4d ago | n/a |  |
| 133 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 11d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 134 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | Does not open (43%) | n/a | 13d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 135 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | n/a | 3d ago | n/a |  |
| 136 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | n/a | 5d ago | n/a | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 137 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 13 | 20 | 65% (last 20) | Does not open (55%) | 33% | 7d ago | 27% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 138 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 55% | 11d ago | n/a |  |
| 139 | [ ] | Mortal Shell (EPIC) | 13 | 20 | 65% (last 20) | Does not open (50%) | 28% | 4d ago | 21% |  |
| 140 | [ ] | Hitman 2: Silent Assassin (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 41% | today | 42% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 141 | [ ] | Dying Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (77%) | 50% | today | 39% |  |
| 142 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 10 | 20 | 50% (last 20) | Does not open (90%) | 46% | 1d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 143 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | n/a | 7d ago | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 144 | [ ] | Fallout Classic (GOG) | 15 | 20 | 75% (last 20) | Does not open (86%) | n/a | 10d ago | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 145 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | 10d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 146 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (69%) | n/a | 18d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 147 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | n/a | 35d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 148 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (84%) | n/a | 3d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 149 | [ ] | Romancing SaGa -Minstrel Song- Remastered (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (100%) | n/a | 1d ago | n/a |  |
| 150 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 46% | 23d ago | 29% |  |
| 151 | [ ] | Re-Volt (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (71%) | n/a | 1d ago | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 152 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | n/a | 13d ago | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 153 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (89%) | 20% | 4d ago | 25% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 154 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 46% | 9d ago | 30% |  |
| 155 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | 36% | 12d ago | 40% |  |
| 156 | [ ] | Mafia II (Classic) (GOG) | 12 | 20 | 60% (last 20) | Does not open (100%) | 55% | today | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 157 | [ ] | Crying Suns (EPIC) | 12 | 20 | 60% (last 20) | No graphics (56%) | n/a | today | n/a |  |
| 158 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (58%) | n/a | today | n/a |  |
| 159 | [ ] | Sacred Gold (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | n/a | 4d ago | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 160 | [ ] | Chasm (GOG) | 12 | 20 | 60% (last 20) | No graphics (50%) | n/a | 8d ago | n/a |  |
| 161 | [ ] | DAEMON X MACHINA (EPIC) | 10 | 20 | 50% (last 20) | Does not open (93%) | 43% | today | 24% |  |
| 162 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Does not open (40%) | n/a | 14d ago | n/a |  |
| 163 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 10 | 20 | 50% (last 20) | No graphics (57%) | 42% | 7d ago | 62% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 164 | [ ] | Beat Cop (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | n/a | 10d ago | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 165 | [ ] | Songs of Conquest (EPIC) | 13 | 20 | 65% (last 20) | Does not open (75%) | n/a | 7d ago | n/a |  |
| 166 | [ ] | FINAL FANTASY VII REMAKE INTERGRADE (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 41% | 8d ago | 41% |  |
| 167 | [ ] | Sandustry (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | n/a | 8d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 168 | [ ] | LET IT DIE (STEAM) | 12 | 20 | 60% (last 20) | Does not open (94%) | n/a | 1d ago | n/a |  |
| 169 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | n/a | 4d ago | n/a |  |
| 170 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 11 | 20 | 55% (last 20) | Does not open (100%) | 33% | 1d ago | 30% |  |
| 171 | [ ] | Hitman: Absolution (GOG) | 10 | 20 | 50% (last 20) | Does not open (83%) | n/a | 5d ago | n/a |  |
| 172 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 17d ago | n/a |  |
| 173 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | n/a | 13d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 174 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 31% | 4d ago | n/a |  |
| 175 | [ ] | Minit (EPIC) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 15d ago | n/a |  |
| 176 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 18d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 177 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 24d ago | n/a |  |
| 178 | [ ] | Allumeria (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | n/a | 1d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 179 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | n/a | 11d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 180 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 52% | 2d ago | 57% |  |
| 181 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 58% | 6d ago | 64% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 182 | [ ] | HOT WHEELS UNLEASHED™ (EPIC) | 10 | 20 | 50% (last 20) | No graphics (63%) | 40% | 6d ago | 30% |  |
| 183 | [ ] | Desperados III (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | n/a | today | n/a |  |
| 184 | [ ] | Turnip Boy Robs a Bank (EPIC) | 11 | 20 | 55% (last 20) | Does not open (64%) | 36% | 9d ago | n/a | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 185 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 50% | 10d ago | n/a |  |
| 186 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | n/a | 17d ago | n/a |  |

## Fix shipped, waiting for ratings (15)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | L.A. Noire (STEAM) | 2026-11-04 | 4 | 4 | 8d ago | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 2 | Max Payne 3 (STEAM) | 2026-11-04 | 4 | 4 | today | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 3 | Red Dead Redemption (STEAM) | 2026-11-04 | 2 | 2 | 6d ago | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 4 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 8 | 8 | 3d ago | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 5 | Transistor (STEAM) | 2026-11-10 | 8 | 4 | 3d ago | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 6 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 4 | 4 | 1d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 7 | Peggle Deluxe (STEAM) | 2026-10-29 | 5 | 3 | today | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 8 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 1 | 1 | 12d ago | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 9 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 2 | 2 | today | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 10 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 5 | 5 | 2d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 11 | Need for Speed™ (STEAM) | 2026-11-04 | 1 | 1 | today | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 12 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 2 | 2 | 1d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 13 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 18d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 14 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 2 | 2 | today | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 15 | Assassin's Creed Odyssey (STEAM) | n/a | 1 | 1 | 1d ago | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |

## Works, but the first launch usually fails (296)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Half-Life (STEAM) | 83 | 119 | 70% (14d) | Does not open (61%) | 71% | today | 68% |  |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 72 | 93 | 77% (14d) | Does not open (63%) | 93% | today | 95% |  |
| 3 | [ ] | Grand Theft Auto V Legacy (STEAM) | 81 | 97 | 84% (since fix) | Does not open (87%) | 74% | today | 72% |  |
| 4 | [ ] | Cyberpunk 2077 (STEAM) | 49 | 85 | 58% (14d) | Does not open (70%) | 72% | today | 70% |  |
| 5 | [ ] | Portal (STEAM) | 48 | 82 | 59% (14d) | Does not open (42%) | 89% | today | 88% |  |
| 6 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 45 | 58 | 78% (14d) | Does not open (55%) | 83% | today | 82% |  |
| 7 | [ ] | ROB RUN (STEAM) | 37 | 50 | 74% (14d) | Does not open (87%) | 67% | today | 68% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 8 | [ ] | MONSTER HUNTER RISE (STEAM) | 36 | 67 | 54% (14d) | Does not open (84%) | 60% | today | 62% |  |
| 9 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 35 | 50 | 70% (14d) | Does not open (60%) | 65% | today | 61% |  |
| 10 | [ ] | Valheim (STEAM) | 42 | 73 | 58% (since fix) | No graphics (54%) | 81% | today | 82% |  |
| 11 | [ ] | Probably Stolen (STEAM) | 30 | 51 | 59% (14d) | Does not open (64%) | 85% | 3d ago | 80% |  |
| 12 | [ ] | Selaco (STEAM) | 28 | 44 | 64% (14d) | Does not open (88%) | 64% | today | 61% |  |
| 13 | [ ] | No Man's Sky (STEAM) | 37 | 67 | 55% (since fix) | Controller issues (61%) | 81% | 1d ago | 78% |  |
| 14 | [ ] | Euro Truck Simulator 2 (STEAM) | 24 | 42 | 57% (14d) | Does not open (65%) | 61% | today | 60% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 15 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 24 | 39 | 62% (14d) | Does not open (76%) | 74% | today | 73% |  |
| 16 | [ ] | ELDEN RING (STEAM) | 20 | 33 | 61% (14d) | Does not open (86%) | 66% | today | 65% |  |
| 17 | [ ] | BeamNG.drive (STEAM) | 19 | 26 | 73% (14d) | Does not open (77%) | 68% | today | 59% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 18 | [ ] | Baldur's Gate 3 (STEAM) | 18 | 31 | 58% (14d) | Does not open (69%) | 84% | today | 83% |  |
| 19 | [ ] | Fallout: New Vegas PCR (STEAM) | 18 | 21 | 86% (14d) | Does not open (93%) | 67% | 1d ago | 61% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 20 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (40%) | 93% | 1d ago | 91% |  |
| 21 | [ ] | Red Dead Redemption 2 (STEAM) | 24 | 28 | 86% (since fix) | Does not open (97%) | 84% | today | 87% |  |
| 22 | [ ] | Overcooked! 2 (EPIC) | 17 | 21 | 81% (14d) | Does not open (92%) | 65% | 1d ago | 57% |  |
| 23 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 17 | 20 | 85% (last 20) | Does not open (75%) | 61% | 1d ago | 64% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 24 | [ ] | Look Outside (STEAM) | 16 | 27 | 59% (14d) | Controller issues (63%) | 91% | 1d ago | 91% |  |
| 25 | [ ] | Dead Space (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | 81% | 2d ago | 78% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 26 | [ ] | Team Fortress 2 (STEAM) | 15 | 28 | 54% (14d) | Does not open (67%) | 76% | today | 75% |  |
| 27 | [ ] | Library Of Ruina (STEAM) | 15 | 23 | 65% (14d) | Does not open (72%) | 87% | 2d ago | 87% |  |
| 28 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | 87% | today | 88% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 29 | [ ] | Noita (STEAM) | 14 | 23 | 61% (14d) | Does not open (62%) | 77% | 2d ago | 77% |  |
| 30 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 14 | 21 | 67% (14d) | Controller issues (53%) | 73% | today | 64% |  |
| 31 | [ ] | Grand Theft Auto V (EPIC) | 18 | 20 | 90% (last 20) | Does not open (88%) | 76% | today | 75% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 32 | [ ] | Resident Evil 4 (2005) (STEAM) | 14 | 20 | 70% (last 20) | Does not open (80%) | 72% | 1d ago | 70% |  |
| 33 | [ ] | Cry of Fear (STEAM) | 14 | 20 | 70% (last 20) | Does not open (44%) | 69% | today | 72% |  |
| 34 | [ ] | Alabaster Dawn (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (49%) | 91% | today | 91% |  |
| 35 | [ ] | Deadlock (STEAM) | 15 | 20 | 75% (last 20) | Does not open (51%) | 84% | 1d ago | 83% |  |
| 36 | [ ] | Loftia (STEAM) | 13 | 20 | 65% (last 20) | Does not open (94%) | 70% | 1d ago | 65% |  |
| 37 | [ ] | Clair Obscur: Expedition 33 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (39%) | 78% | today | 74% |  |
| 38 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (90%) | 91% | 2d ago | 90% |  |
| 39 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 26 | 47 | 55% (since fix) | Does not open (72%) | 60% | today | 59% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 40 | [ ] | Order of the Sinking Star (STEAM) | 11 | 20 | 55% (14d) | Does not open (65%) | 64% | 2d ago | 68% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 41 | [ ] | Mass Effect™ Legendary Edition (STEAM) | 14 | 27 | 52% (since fix) | Does not open (83%) | 80% | today | 82% |  |
| 42 | [ ] | Quake (STEAM) | 11 | 20 | 55% (last 20) | Does not open (65%) | 70% | 3d ago | 59% |  |
| 43 | [ ] | Dressmaker (STEAM) | 13 | 20 | 65% (last 20) | Does not open (56%) | 77% | today | 74% |  |
| 44 | [ ] | DOOM 3: BFG Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (74%) | 67% | 1d ago | 67% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 45 | [ ] | Mortal Kombat X (STEAM) | 13 | 20 | 65% (last 20) | Does not open (77%) | 92% | 5d ago | 92% |  |
| 46 | [ ] | Welcome to Elderfield (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 68% | today | 71% |  |
| 47 | [ ] | Pathogenic (STEAM) | 10 | 20 | 50% (14d) | Does not open (80%) | 68% | today | 64% |  |
| 48 | [ ] | Aniimo (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 79% | today | 74% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 49 | [ ] | Resident Evil 7 Biohazard (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 69% | today | 61% |  |
| 50 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (69%) | 100% | 2d ago | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 51 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 17 | 20 | 85% (last 20) | Does not open (85%) | 64% | today | 64% |  |
| 52 | [ ] | Don't Starve Together (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 72% | today | 68% |  |
| 53 | [ ] | Barony (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 82% | 1d ago | 77% |  |
| 54 | [ ] | Crypt of the NecroDancer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (45%) | 87% | 1d ago | 86% |  |
| 55 | [ ] | Disco Elysium - The Final Cut (EPIC) | 12 | 20 | 60% (last 20) | Does not open (76%) | 93% | 1d ago | 92% |  |
| 56 | [ ] | Batman™: Arkham Origins (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 67% | 2d ago | 64% |  |
| 57 | [ ] | Tales of ARISE (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (68%) | 81% | today | 79% |  |
| 58 | [ ] | Until Then (STEAM) | 17 | 20 | 85% (last 20) | Does not open (85%) | 61% | today | 47% |  |
| 59 | [ ] | Fallout: New Vegas (EPIC) | 16 | 20 | 80% (last 20) | Does not open (59%) | 77% | 2d ago | 72% |  |
| 60 | [ ] | Rune Factory 3 Special (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 100% | today | 100% |  |
| 61 | [ ] | Chained Echoes (GOG) | 15 | 20 | 75% (last 20) | Does not open (62%) | 68% | 1d ago | 60% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 62 | [ ] | Devil May Cry 5 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 81% | today | 83% |  |
| 63 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 10 | 19 | 53% (since fix) | Controller issues (83%) | 71% | today | 70% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 64 | [ ] | OMORI (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 67% | 2d ago | 60% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 65 | [ ] | FINAL FANTASY (STEAM) | 12 | 20 | 60% (last 20) | Does not open (78%) | 82% | today | 76% |  |
| 66 | [ ] | Stardew Valley (GOG) | 10 | 20 | 50% (last 20) | Controller issues (60%) | 86% | today | 83% |  |
| 67 | [ ] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 12 | 20 | 60% (last 20) | Does not open (59%) | 79% | today | 82% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 68 | [ ] | Disgaea 5 Complete (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | 94% | 6d ago | 96% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 69 | [ ] | Mini Motorways (STEAM) | 13 | 20 | 65% (last 20) | Does not open (72%) | 65% | today | 63% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 70 | [ ] | Cave Story+ (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | 75% | 1d ago | 74% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 71 | [ ] | Little Witch in the Woods (STEAM) | 11 | 20 | 55% (last 20) | Does not open (55%) | 84% | today | 84% |  |
| 72 | [ ] | LEGO® MARVEL Super Heroes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (65%) | 84% | today | 86% |  |
| 73 | [ ] | Castlevania Dominus Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (91%) | 98% | 1d ago | 96% |  |
| 74 | [ ] | Cyberpunk 2077 (GOG) | 11 | 20 | 55% (last 20) | Does not open (70%) | 68% | today | 64% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 75 | [ ] | Divinity: Original Sin 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 81% | 1d ago | 78% |  |
| 76 | [ ] | PAC-MAN Championship Edition DX+ (STEAM) | 10 | 20 | 50% (last 20) | No graphics (59%) | 67% | 2d ago | 56% |  |
| 77 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (61%) | 93% | 1d ago | 94% |  |
| 78 | [ ] | Grand Theft Auto: Vice City (STEAM) | 14 | 20 | 70% (last 20) | Does not open (43%) | 80% | today | 79% |  |
| 79 | [ ] | eFootball™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 62% | 5d ago | 57% |  |
| 80 | [ ] | Poppy Playtime (STEAM) | 13 | 20 | 65% (last 20) | Does not open (57%) | 69% | 1d ago | 64% |  |
| 81 | [ ] | Palia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (67%) | 69% | today | 67% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 82 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (52%) | 83% | 2d ago | 82% |  |
| 83 | [ ] | Titanfall® 2 (STEAM) | 9 | 12 | 75% (since fix) | Does not open (89%) | 67% | today | 65% |  |
| 84 | [ ] | Call of Duty 4: Modern Warfare (2007) (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (52%) | 71% | 2d ago | 64% |  |
| 85 | [ ] | TBH: Task Bar Hero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (68%) | 84% | today | 87% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 86 | [ ] | PAYDAY: The Heist (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 80% | 2d ago | n/a |  |
| 87 | [ ] | Dota 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 76% | today | 79% |  |
| 88 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (78%) | 66% | 6d ago | 71% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 89 | [ ] | Happy Wheels (STEAM) | 19 | 20 | 95% (last 20) | No graphics (52%) | 60% | 16d ago | 47% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 90 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (42%) | 72% | 6d ago | 71% |  |
| 91 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 97% | 4d ago | 96% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 92 | [ ] | Deskrawl: Idle ARPG (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 64% | 12d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 93 | [ ] | Leaf it Alone (STEAM) | 10 | 20 | 50% (last 20) | Does not open (54%) | 95% | 2d ago | 95% |  |
| 94 | [ ] | The Sims™ 4 (STEAM) | 7 | 13 | 54% (since fix) | Does not open (85%) | 68% | today | 68% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 95 | [ ] | Resident Evil Village (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 87% | today | 85% |  |
| 96 | [ ] | Assetto Corsa (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (48%) | 82% | today | 84% |  |
| 97 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (80%) | 88% | 5d ago | 82% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 98 | [ ] | Ratatan (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | 90% | 2d ago | 85% |  |
| 99 | [ ] | Mortal Kombat 11 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | 64% | 3d ago | 73% |  |
| 100 | [ ] | Tails of Iron (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 87% | 1d ago | 90% |  |
| 101 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 100% | today | 100% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 102 | [ ] | Minecraft Dungeons II (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 72% | 2d ago | 72% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 103 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (42%) | 87% | today | 87% |  |
| 104 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (57%) | 74% | 5d ago | 78% |  |
| 105 | [ ] | Fable - The Lost Chapters (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (48%) | 81% | today | 83% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 106 | [ ] | American Truck Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 73% | today | 71% |  |
| 107 | [ ] | ZERO Sievert (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 84% | 2d ago | 81% |  |
| 108 | [ ] | Fate/stay night REMASTERED (STEAM) | 11 | 20 | 55% (last 20) | No graphics (48%) | 91% | 1d ago | 92% |  |
| 109 | [ ] | Minecraft Dungeons (STEAM) | 11 | 20 | 55% (last 20) | Does not open (76%) | 77% | 2d ago | 76% |  |
| 110 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 89% | 4d ago | 83% |  |
| 111 | [ ] | Astral Party  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 89% | 3d ago | 86% |  |
| 112 | [ ] | Sid Meier's Civilization VI (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 79% | today | 77% |  |
| 113 | [ ] | MIO: Memories in Orbit (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (61%) | 94% | today | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 114 | [ ] | Abiotic Factor (STEAM) | 10 | 20 | 50% (last 20) | Does not open (74%) | 77% | 6d ago | 84% |  |
| 115 | [ ] | Sid Meier's Civilization V (STEAM) | 15 | 20 | 75% (last 20) | Does not open (77%) | 63% | 3d ago | 58% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 116 | [ ] | Call of Duty: World at War (STEAM) | 13 | 20 | 65% (last 20) | Does not open (40%) | 76% | 1d ago | 66% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 117 | [ ] | Need for Speed™ Rivals (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 73% | today | 75% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 118 | [ ] | A Plague Tale: Innocence (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | 68% | 7d ago | 68% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 119 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 61% | 7d ago | 56% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 120 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 17 | 20 | 85% (last 20) | Controller issues (88%) | 95% | today | 97% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 121 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 15 | 20 | 75% (last 20) | Does not open (71%) | 83% | 1d ago | 82% |  |
| 122 | [ ] | Moonstone Island (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (68%) | 79% | today | 78% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 123 | [ ] | Counter-Strike:Global Offensive (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 61% | today | 59% |  |
| 124 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 72% | 16d ago | 82% |  |
| 125 | [ ] | Caravan SandWitch (EPIC) | 10 | 20 | 50% (last 20) | Does not open (73%) | 65% | 1d ago | 65% |  |
| 126 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (84%) | 67% | 2d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 127 | [ ] | PlateUp! (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 80% | 3d ago | 73% |  |
| 128 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | 82% | 14d ago | 82% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 129 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | 94% | 9d ago | 93% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 130 | [ ] | Ultimate Custom Night (STEAM) | 15 | 20 | 75% (last 20) | No graphics (75%) | 67% | today | 55% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 131 | [ ] | Street Fighter™ 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | 82% | 1d ago | 79% |  |
| 132 | [ ] | No, I'm not a Human (STEAM) | 10 | 20 | 50% (last 20) | Does not open (52%) | 91% | 1d ago | 87% |  |
| 133 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (67%) | 86% | today | 87% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 134 | [ ] | Stumble Guys (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 67% | 1d ago | 62% |  |
| 135 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 11 | 20 | 55% (last 20) | Does not open (65%) | 89% | 1d ago | 88% |  |
| 136 | [ ] | OCTOPATH TRAVELER 0 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (77%) | 92% | 2d ago | 93% |  |
| 137 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (87%) | 88% | 5d ago | 93% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 138 | [ ] | Max Payne (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (45%) | 80% | 1d ago | 79% |  |
| 139 | [ ] | Stellar Blade™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | 82% | 2d ago | 82% |  |
| 140 | [ ] | Yakuza: Like a Dragon (STEAM) | 13 | 20 | 65% (last 20) | Does not open (60%) | 67% | today | 75% |  |
| 141 | [ ] | Oxygen Not Included (STEAM) | 12 | 20 | 60% (last 20) | Does not open (73%) | 72% | today | 78% |  |
| 142 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (79%) | 77% | today | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 143 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (82%) | 87% | 5d ago | 90% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 144 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 67% | 12d ago | 67% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 145 | [ ] | Sonic Generations (STEAM) | 14 | 20 | 70% (last 20) | Does not open (70%) | 67% | 5d ago | 64% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 146 | [ ] | Tabletop Simulator (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 81% | 4d ago | 82% |  |
| 147 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 77% | 1d ago | 69% |  |
| 148 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (48%) | 79% | 8d ago | 75% |  |
| 149 | [ ] | Pinball FX (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 67% | 6d ago | 65% |  |
| 150 | [ ] | Sovereign Tower (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 77% | today | 79% |  |
| 151 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | 85% | 10d ago | 83% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 152 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 84% | 16d ago | 83% |  |
| 153 | [ ] | Plague Inc: Evolved (STEAM) | 13 | 20 | 65% (last 20) | Does not open (58%) | 65% | 2d ago | 64% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 154 | [ ] | Trailmakers (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | 91% | 2d ago | 92% |  |
| 155 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | 70% | 4d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 156 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | No graphics (47%) | 87% | today | 86% |  |
| 157 | [ ] | Roguecraft DX (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 94% | today | 93% |  |
| 158 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (60%) | 92% | 1d ago | 90% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 159 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (92%) | 68% | 3d ago | 83% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 160 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (54%) | 72% | 7d ago | 73% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 161 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (59%) | 67% | 11d ago | 65% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 162 | [ ] | Necesse (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 64% | 1d ago | 65% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 163 | [ ] | Gambonanza (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 89% | 6d ago | 88% |  |
| 164 | [ ] | Gothic 1 Classic (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 71% | 14d ago | 67% |  |
| 165 | [ ] | Limbus Company (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 89% | 4d ago | 95% |  |
| 166 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 78% | 5d ago | 76% |  |
| 167 | [ ] | Unturned (STEAM) | 11 | 20 | 55% (last 20) | Does not open (41%) | 82% | today | 85% |  |
| 168 | [ ] | Fallout (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 68% | 4d ago | 65% |  |
| 169 | [ ] | Sonic Lost World (STEAM) | 10 | 20 | 50% (last 20) | No graphics (69%) | 80% | 2d ago | 81% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 170 | [ ] | Heavy Rain (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (64%) | 90% | today | 90% |  |
| 171 | [ ] | Raft (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | 91% | 1d ago | 88% |  |
| 172 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 67% | 11d ago | 67% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 173 | [ ] | Control Ultimate Edition (GOG) | 13 | 20 | 65% (last 20) | Does not open (76%) | 74% | 12d ago | 68% |  |
| 174 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (82%) | 89% | 4d ago | 89% |  |
| 175 | [ ] | Digimon Survive (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (77%) | 86% | 1d ago | 85% |  |
| 176 | [ ] | Dishonored 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 66% | 3d ago | 61% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 177 | [ ] | Overwatch® (STEAM) | 8 | 11 | 73% (since fix) | Does not open (62%) | 83% | today | 79% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 178 | [ ] | Subnautica 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (55%) | 79% | today | n/a | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 179 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (55%) | 91% | 18d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 180 | [ ] | Supermarket Together (STEAM) | 15 | 20 | 75% (last 20) | Does not open (68%) | 62% | today | 65% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 181 | [ ] | Changed (STEAM) | 15 | 20 | 75% (last 20) | Does not open (62%) | 62% | 10d ago | 54% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 182 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 100% | 33d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 183 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | 88% | today | 84% |  |
| 184 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (46%) | 64% | 2d ago | 65% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 185 | [ ] | HELLDIVERS™ (STEAM) | 12 | 20 | 60% (last 20) | Does not open (78%) | 61% | 4d ago | 58% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 186 | [ ] | One-armed robber (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (69%) | 60% | today | 52% |  |
| 187 | [ ] | TurretGirls (STEAM) | 12 | 20 | 60% (last 20) | No graphics (77%) | 95% | 3d ago | 100% |  |
| 188 | [ ] | Escape from Duckov (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (70%) | 95% | 4d ago | 98% |  |
| 189 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | 80% | 12d ago | 73% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 190 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (71%) | 83% | 5d ago | 82% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 191 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (75%) | 70% | 6d ago | 62% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 192 | [ ] | Capcom Arcade Stadium (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | 78% | 10d ago | 80% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 193 | [ ] | Hylics (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (74%) | 94% | today | 90% |  |
| 194 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (76%) | 100% | 13d ago | n/a |  |
| 195 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 76% | 1d ago | 76% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 196 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (59%) | 69% | 1d ago | 71% |  |
| 197 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (67%) | 96% | 1d ago | 100% |  |
| 198 | [ ] | BioShock 2 Remastered (STEAM) | 10 | 20 | 50% (last 20) | Does not open (83%) | 84% | today | 85% |  |
| 199 | [ ] | Watch Dogs 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (80%) | 65% | today | 59% | [#399](https://github.com/GameNative/gamenative-compat/issues/399) |
| 200 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | 69% | 4d ago | 72% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 201 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (83%) | 62% | 2d ago | 50% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 202 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 75% | 17d ago | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 203 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 14 | 20 | 70% (last 20) | Does not open (80%) | 61% | today | 60% |  |
| 204 | [ ] | Turbo Overkill (STEAM) | 13 | 20 | 65% (last 20) | No graphics (91%) | 100% | 1d ago | 100% |  |
| 205 | [ ] | Warframe (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 80% | today | 79% |  |
| 206 | [ ] | Moonring (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 80% | 3d ago | 76% |  |
| 207 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 95% | 12d ago | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 208 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (65%) | 79% | today | 73% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 209 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (61%) | 73% | 12d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 210 | [ ] | Resident Evil Revelations 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 82% | today | 82% |  |
| 211 | [ ] | Jade Empire: Special Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (93%) | 71% | 7d ago | 64% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 212 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | 75% | 20d ago | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 213 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (91%) | 81% | 36d ago | 73% |  |
| 214 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 75% | 26d ago | 75% |  |
| 215 | [ ] | Hotline Miami (GOG) | 14 | 20 | 70% (last 20) | Does not open (89%) | 75% | 5d ago | 78% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 216 | [ ] | GOD EATER RESURRECTION (STEAM) | 14 | 20 | 70% (last 20) | Does not open (56%) | 86% | today | n/a |  |
| 217 | [ ] | Lucid Blocks (STEAM) | 11 | 20 | 55% (last 20) | Does not open (80%) | 62% | 3d ago | 50% |  |
| 218 | [ ] | MX Bikes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 96% | 5d ago | 95% |  |
| 219 | [ ] | Bongo Cat (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 64% | 2d ago | 47% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 220 | [ ] | Return to Monkey Island (STEAM) | 14 | 20 | 70% (last 20) | No graphics (72%) | 68% | 16d ago | 67% |  |
| 221 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (47%) | 81% | 18d ago | n/a | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 222 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 93% | 13d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 223 | [ ] | My Summer Car (STEAM) | 11 | 20 | 55% (last 20) | Does not open (63%) | 76% | 5d ago | 74% |  |
| 224 | [ ] | GUILTY GEAR Xrd REV 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (83%) | 67% | 8d ago | 62% |  |
| 225 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (64%) | 78% | 11d ago | 79% |  |
| 226 | [ ] | No Socks RPG (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (91%) | 94% | 1d ago | 93% |  |
| 227 | [ ] | Invisible, Inc. (STEAM) | 14 | 20 | 70% (last 20) | Does not open (63%) | 85% | today | n/a |  |
| 228 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (82%) | 80% | 6d ago | 80% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 229 | [ ] | Big Walk (STEAM) | 12 | 20 | 60% (last 20) | Does not open (52%) | 65% | 3d ago | 58% |  |
| 230 | [ ] | SnowRunner (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 72% | today | 73% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 231 | [ ] | Darksiders (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 84% | today | 84% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 232 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 95% | 8d ago | 100% |  |
| 233 | [ ] | Spark the Electric Jester (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 77% | 2d ago | n/a | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 234 | [ ] | AER Memories of Old (EPIC) | 13 | 20 | 65% (last 20) | Does not open (86%) | 93% | 7d ago | 92% |  |
| 235 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (71%) | 69% | 8d ago | 67% |  |
| 236 | [ ] | Capcom Fighting Collection (STEAM) | 13 | 20 | 65% (last 20) | Does not open (86%) | 90% | 3d ago | 87% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 237 | [ ] | BATTLETECH (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 96% | 7d ago | 94% |  |
| 238 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (50%) | 76% | 2d ago | 86% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 239 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 93% | 15d ago | n/a |  |
| 240 | [ ] | Super Battle Golf (STEAM) | 11 | 20 | 55% (last 20) | Does not open (78%) | 89% | today | 87% |  |
| 241 | [ ] | Hero Siege (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (46%) | 84% | 7d ago | 88% |  |
| 242 | [ ] | Secrets of Grindea (STEAM) | 10 | 20 | 50% (last 20) | Does not open (48%) | 79% | 5d ago | 80% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 243 | [ ] | Zero Escape: The Nonary Games (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 72% | 2d ago | 73% |  |
| 244 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 77% | today | 78% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 245 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 83% | 9d ago | 78% |  |
| 246 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 78% | today | 75% |  |
| 247 | [ ] | HITMAN World of Assassination (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 74% | 2d ago | 73% |  |
| 248 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (94%) | 94% | 14d ago | 93% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 249 | [ ] | Decktamer (STEAM) | 13 | 20 | 65% (last 20) | Does not open (100%) | 75% | today | n/a |  |
| 250 | [ ] | Tales of Zestiria (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 67% | today | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 251 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 92% | 34d ago | 92% |  |
| 252 | [ ] | Timberborn (STEAM) | 12 | 20 | 60% (last 20) | No graphics (71%) | 94% | 4d ago | 100% |  |
| 253 | [ ] | Goose Goose Duck (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 82% | 3d ago | 80% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 254 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 12 | 20 | 60% (last 20) | No graphics (39%) | 86% | 6d ago | 90% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 255 | [ ] | 12 is Better Than 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 75% | 18d ago | n/a |  |
| 256 | [ ] | Deus Ex™ GOTY Edition (GOG) | 11 | 20 | 55% (last 20) | No graphics (47%) | 100% | 1d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 257 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 93% | 11d ago | 90% |  |
| 258 | [ ] | Rollout Inline (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 67% | 3d ago | 82% |  |
| 259 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 71% | 7d ago | 83% |  |
| 260 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 13 | 20 | 65% (last 20) | Does not open (86%) | 76% | 1d ago | 90% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 261 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 60% | 13d ago | 64% |  |
| 262 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 71% | 10d ago | 69% |  |
| 263 | [ ] | Disgaea 4 Complete+ (STEAM) | 12 | 20 | 60% (last 20) | No graphics (40%) | 93% | today | 92% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 264 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 64% | 14d ago | 64% |  |
| 265 | [ ] | Sons Of The Forest (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 74% | 8d ago | 71% |  |
| 266 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | 60% | today | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 267 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 77% | 5d ago | 79% |  |
| 268 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 78% | today | 75% |  |
| 269 | [ ] | Cat Mail Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 91% | 1d ago | 90% |  |
| 270 | [ ] | CRUEL (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 83% | 8d ago | 82% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 271 | [ ] | Subnautica: Below Zero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 79% | today | 68% |  |
| 272 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 94% | 8d ago | 100% |  |
| 273 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 92% | 1d ago | 89% |  |
| 274 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 93% | 5d ago | 93% |  |
| 275 | [ ] | Hitman: Contracts (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (82%) | 69% | today | 64% |  |
| 276 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (92%) | 87% | 18d ago | 92% |  |
| 277 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (63%) | 62% | 11d ago | n/a |  |
| 278 | [ ] | Forgive Me Father (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 70% | 9d ago | 58% |  |
| 279 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 77% | 7d ago | 75% |  |
| 280 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 85% | 8d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 281 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 67% | 4d ago | 71% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 282 | [ ] | Assetto Corsa Competizione (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 88% | today | 86% |  |
| 283 | [ ] | BioShock 2 Remastered (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 81% | 3d ago | 76% |  |
| 284 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | No graphics (50%) | 90% | 25d ago | n/a | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 285 | [ ] | Sort Them Ducks (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (58%) | 100% | today | 100% |  |
| 286 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 69% | 16d ago | 67% |  |
| 287 | [ ] | Cruelty Squad (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 87% | 6d ago | 83% |  |
| 288 | [ ] | A Plague Tale: Innocence (GOG) | 10 | 20 | 50% (last 20) | Does not open (91%) | 64% | 5d ago | n/a |  |
| 289 | [ ] | Dungeon Siege (STEAM) | 10 | 20 | 50% (last 20) | No graphics (50%) | 100% | 2d ago | 100% |  |
| 290 | [ ] | The Stanley Parable (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 75% | 3d ago | 77% |  |
| 291 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (65%) | 88% | 2d ago | 90% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 292 | [ ] | Command & Conquer™ Red Alert™ 3 (STEAM) | 10 | 20 | 50% (last 20) | No graphics (38%) | 86% | 1d ago | 90% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 293 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 100% | 1d ago | 100% |  |
| 294 | [ ] | Pillars of Eternity (STEAM) | 10 | 20 | 50% (last 20) | Does not open (40%) | 100% | 2d ago | 100% |  |
| 295 | [ ] | Haydee (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 79% | 8d ago | 90% |  |
| 296 | [ ] | Spirit City: Lofi Sessions (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 67% | today | 67% |  |

## Recently recovered (368)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Grim Dawn (STEAM) | 465 | 2026-11-08 | 546 | 69% |  |
| 2 | [x] | FINAL FANTASY RESONANCE (STEAM) | 462 | 2026-10-24 | 1055 | 81% |  |
| 3 | [x] | Half-Life (STEAM) | 368 | 2026-11-09 | 635 | 71% |  |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 265 | 2026-11-14 | 421 | 70% |  |
| 5 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 243 | 2026-11-09 | 337 | 87% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 6 | [x] | MONSTER HUNTER RISE (STEAM) | 227 | 2026-11-17 | 535 | 60% |  |
| 7 | [x] | Alan Wake (STEAM) | 224 | 2026-11-14 | 250 | 76% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 8 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 219 | 2026-11-09 | 374 | 65% |  |
| 9 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 189 | 2026-11-09 | 230 | 54% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 10 | [x] | BeamNG.drive (STEAM) | 185 | 2026-11-09 | 229 | 68% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 11 | [x] | Call of Duty: Black Ops (STEAM) | 181 | 2026-11-13 | 207 | 21% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 12 | [x] | OMORI (STEAM) | 168 | 2026-11-09 | 214 | 67% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 13 | [x] | DRAGON BALL FighterZ (STEAM) | 164 | 2026-11-01 | 213 | 87% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 14 | [x] | Geometry Dash (STEAM) | 159 | 2026-11-11 | 451 | 63% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 15 | [x] | Spelunky 2 (STEAM) | 153 | 2026-11-01 | 198 | 82% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 16 | [x] | BioShock (STEAM) | 147 | 2026-11-09 | 299 | 71% |  |
| 17 | [x] | Sid Meier's Civilization V (STEAM) | 143 | 2026-11-10 | 155 | 63% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 18 | [x] | Team Fortress 2 (STEAM) | 137 | 2026-11-09 | 239 | 76% |  |
| 19 | [x] | Prototype (STEAM) | 134 | 2026-11-11 | 200 | 59% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 20 | [x] | Minecraft Dungeons II (STEAM) | 132 | 2026-11-09 | 151 | 72% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 21 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 128 | 2026-11-23 | 175 | 60% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 22 | [x] | Castlevania Advance Collection (STEAM) | 127 | 2026-11-09 | 203 | 87% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 23 | [x] | Euro Truck Simulator 2 (STEAM) | 122 | 2026-11-23 | 223 | 61% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 24 | [x] | Aniimo (STEAM) | 116 | 2026-11-09 | 157 | 79% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 25 | [x] | Mirror's Edge (STEAM) | 110 | 2026-11-09 | 166 | 67% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 26 | [x] | Assassin's Creed II (STEAM) | 109 | 2026-11-10 | 114 | 66% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 27 | [x] | Cave Story+ (STEAM) | 103 | 2026-11-09 | 113 | 75% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 28 | [x] | Necesse (STEAM) | 103 | 2026-11-22 | 113 | 64% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 29 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 101 | 2026-11-09 | 142 | 90% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 30 | [x] | The Witcher: Enhanced Edition (STEAM) | 99 | 2026-11-09 | 118 | 75% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 31 | [x] | Happy Wheels (STEAM) | 97 | 2026-11-09 | 117 | 60% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 32 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 91 | 2026-11-15 | 136 | 81% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 33 | [x] | Moonstone Island (STEAM) | 91 | 2026-11-09 | 121 | 79% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 34 | [x] | Fallout: New Vegas PCR (STEAM) | 86 | 2026-11-20 | 114 | 67% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 35 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 80 | 2026-11-09 | 105 | 95% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 36 | [x] | FINAL FANTASY XIII-2 (STEAM) | 80 | 2026-11-09 | 83 | 68% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 37 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 79 | 2026-11-09 | 129 | 74% |  |
| 38 | [x] | DOOM 3: BFG Edition (STEAM) | 79 | 2026-11-09 | 122 | 67% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 39 | [x] | Vital Shell (STEAM) | 76 | 2026-11-09 | 125 | 85% |  |
| 40 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 76 | 2026-11-23 | 98 | 61% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 41 | [x] | Psychonauts (STEAM) | 75 | 2026-11-09 | 142 | 92% |  |
| 42 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 75 | 2026-11-09 | 116 | 77% |  |
| 43 | [x] | Brawlhalla (STEAM) | 73 | 2026-11-09 | 143 | 72% |  |
| 44 | [x] | Quake (STEAM) | 72 | 2026-11-09 | 219 | 70% |  |
| 45 | [x] | Cyberpunk 2077 (GOG) | 72 | 2026-11-09 | 96 | 68% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 46 | [x] | The Sims™ 4 (STEAM) | 70 | 2026-11-09 | 94 | 68% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 47 | [x] | Age of Empires II: Definitive Edition (STEAM) | 70 | 2026-11-10 | 90 | 68% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 48 | [x] | Ballionaire (STEAM) | 69 | 2026-11-09 | 118 | 82% |  |
| 49 | [x] | Order of the Sinking Star (STEAM) | 69 | 2026-11-09 | 104 | 64% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 50 | [x] | Dota 2 (STEAM) | 66 | 2026-11-09 | 100 | 76% |  |
| 51 | [x] | Stardew Valley (GOG) | 65 | 2026-11-11 | 117 | 86% |  |
| 52 | [x] | Fable - The Lost Chapters (STEAM) | 65 | 2026-11-09 | 108 | 81% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 53 | [x] | American Truck Simulator (STEAM) | 65 | 2026-11-09 | 106 | 73% |  |
| 54 | [x] | Disgaea 5 Complete (STEAM) | 65 | 2026-11-09 | 76 | 94% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 55 | [x] | Need for Speed: Hot Pursuit (STEAM) | 64 | 2026-11-09 | 98 | 76% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 56 | [x] | GRID (STEAM) | 64 | 2026-11-21 | 85 | 48% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 57 | [x] | Diablo® IV (STEAM) | 63 | 2026-11-11 | 75 | 82% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 58 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 62 | 2026-11-11 | 82 | 60% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 59 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 61 | 2026-11-09 | 99 | 85% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 60 | [x] | Mini Motorways (STEAM) | 61 | 2026-11-09 | 96 | 65% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 61 | [x] | Spyro™ Reignited Trilogy (STEAM) | 60 | 2026-11-09 | 107 | 79% |  |
| 62 | [x] | Grand Theft Auto V (EPIC) | 60 | 2026-11-09 | 65 | 76% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 63 | [x] | Poppy Playtime (STEAM) | 59 | 2026-11-09 | 101 | 69% |  |
| 64 | [x] | STEINS;GATE (STEAM) | 59 | 2026-11-09 | 89 | 83% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 65 | [x] | Sovereign Tower (STEAM) | 58 | 2026-11-09 | 114 | 77% |  |
| 66 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 58 | 2026-10-25 | 99 | 79% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 67 | [x] | Deskrawl: Idle ARPG (STEAM) | 58 | 2026-11-09 | 72 | 64% | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 68 | [x] | Borderlands 3 (STEAM) | 57 | 2026-11-09 | 87 | 91% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 69 | [x] | Gunfire Reborn (STEAM) | 57 | 2026-11-09 | 63 | 88% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 70 | [x] | FINAL FANTASY XIII (STEAM) | 56 | 2026-11-22 | 513 | 62% |  |
| 71 | [x] | Firewatch (STEAM) | 56 | 2026-11-10 | 110 | 87% |  |
| 72 | [x] | Fallout (STEAM) | 56 | 2026-11-09 | 89 | 68% |  |
| 73 | [x] | Call of Duty: World at War (STEAM) | 56 | 2026-11-09 | 80 | 76% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 74 | [x] | Caravan SandWitch (EPIC) | 55 | 2026-11-09 | 117 | 65% |  |
| 75 | [x] | Call of Juarez Gunslinger (STEAM) | 55 | 2026-11-09 | 68 | 67% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 76 | [x] | A Plague Tale: Innocence (STEAM) | 55 | 2026-11-09 | 58 | 68% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 77 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 54 | 2026-11-09 | 90 | 73% |  |
| 78 | [x] | Sonic Generations (STEAM) | 54 | 2026-11-09 | 61 | 67% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 79 | [x] | eFootball™ (STEAM) | 52 | 2026-11-09 | 78 | 62% |  |
| 80 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 52 | 2026-11-17 | 77 | 64% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 81 | [x] | MIO: Memories in Orbit (STEAM) | 50 | 2026-11-09 | 104 | 94% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 82 | [x] | Starbound (STEAM) | 50 | 2026-11-09 | 84 | 85% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 83 | [x] | Sol Cesto (EPIC) | 50 | 2026-11-09 | 51 | 88% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 84 | [x] | Last Epoch (STEAM) | 49 | 2026-11-09 | 74 | 62% |  |
| 85 | [x] | Darksiders (STEAM) | 49 | 2026-11-09 | 65 | 84% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 86 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 49 | 2026-11-09 | 55 | 100% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 87 | [x] | Okami HD (STEAM) | 48 | 2026-11-09 | 90 | 95% |  |
| 88 | [x] | HELLDIVERS™ (STEAM) | 48 | 2026-11-23 | 60 | 61% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 89 | [x] | Overwatch® (STEAM) | 48 | 2026-11-10 | 53 | 83% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 90 | [x] | Moonlighter (EPIC) | 48 | 2026-11-09 | 52 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 91 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 47 | 2026-11-09 | 82 | 85% |  |
| 92 | [x] | Oxygen Not Included (STEAM) | 47 | 2026-11-11 | 80 | 72% |  |
| 93 | [x] | TBH: Task Bar Hero (STEAM) | 47 | 2026-11-09 | 74 | 84% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 94 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 46 | 2026-11-09 | 80 | 53% |  |
| 95 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 45 | 2026-11-13 | 74 | 65% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 96 | [x] | Watch_Dogs 2 (STEAM) | 45 | 2026-11-22 | 50 | 61% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 97 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 44 | 2026-11-09 | 68 | 87% |  |
| 98 | [x] | Darkest Dungeon® (EPIC) | 41 | 2026-11-09 | 81 | 88% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 99 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 41 | 2026-11-09 | 70 | 85% |  |
| 100 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 41 | 2026-11-09 | 69 | 58% |  |
| 101 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 41 | 2026-11-09 | 59 | 71% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 102 | [x] | Borderlands: The Pre-Sequel (STEAM) | 39 | 2026-11-09 | 77 | 58% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 103 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 39 | 2026-11-09 | 62 | 63% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 104 | [x] | Digimon World: Next Order (STEAM) | 38 | 2026-11-09 | 74 | 86% |  |
| 105 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 38 | 2026-11-09 | 69 | 89% |  |
| 106 | [x] | Sonic Lost World (STEAM) | 38 | 2026-11-09 | 58 | 80% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 107 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 2026-11-09 | 70 | 89% |  |
| 108 | [x] | Tomb Raider: Anniversary (STEAM) | 37 | 2026-11-09 | 64 | 62% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 109 | [x] | Aggelos (STEAM) | 37 | 2026-11-09 | 53 | 87% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 110 | [x] | ROB RUN (STEAM) | 37 | 2026-11-17 | 53 | 67% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 111 | [x] | MudRunner (STEAM) | 36 | 2026-10-24 | 92 | 62% |  |
| 112 | [x] | Sonic Origins (STEAM) | 36 | 2026-11-09 | 65 | 77% |  |
| 113 | [x] | Age of Empires II (2013) (STEAM) | 36 | 2026-11-09 | 61 | 74% |  |
| 114 | [x] | CrossCode (GOG) | 36 | 2026-11-09 | 39 | 77% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 115 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 36 | 2026-11-19 | 38 | 94% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 116 | [x] | POSTAL 2 (GOG) | 35 | 2026-11-09 | 66 | 94% |  |
| 117 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 35 | 2026-11-09 | 66 | 83% |  |
| 118 | [x] | XCOM 2 (STEAM) | 35 | 2026-11-09 | 61 | 68% |  |
| 119 | [x] | Street Fighter™ 6 (STEAM) | 35 | 2026-11-09 | 56 | 82% |  |
| 120 | [x] | Russian Fishing 4 (STEAM) | 35 | 2026-11-09 | 41 | 70% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 121 | [x] | Dead by Daylight (STEAM) | 35 | 2026-11-09 | 39 | 86% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 122 | [x] | Monster Hunter Wilds (STEAM) | 35 | 2026-11-09 | 36 | 85% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 123 | [x] | Amnesia: The Dark Descent (STEAM) | 34 | 2026-11-09 | 73 | 85% |  |
| 124 | [x] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 34 | 2026-11-20 | 64 | 15% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 125 | [x] | Ace Attorney Investigations Collection (STEAM) | 34 | 2026-11-09 | 62 | 88% |  |
| 126 | [x] | Breathedge (STEAM) | 34 | 2026-11-23 | 52 | 61% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 127 | [x] | Being a DIK (STEAM) | 33 | 2026-11-09 | 73 | 71% |  |
| 128 | [x] | Max Payne (STEAM) | 33 | 2026-11-09 | 55 | 80% |  |
| 129 | [x] | Plague Inc: Evolved (STEAM) | 33 | 2026-11-16 | 53 | 65% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 130 | [x] | FINAL FANTASY VII (2013) (STEAM) | 33 | 2026-11-09 | 50 | 57% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 131 | [x] | Counter-Strike:Global Offensive (STEAM) | 33 | 2026-11-09 | 49 | 61% |  |
| 132 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 33 | 2026-11-09 | 41 | 92% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 133 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 32 | 2026-11-09 | 59 | 78% |  |
| 134 | [x] | Gauntlet™  (STEAM) | 32 | 2026-11-11 | 47 | n/a | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 135 | [x] | SnowRunner (STEAM) | 32 | 2026-11-09 | 43 | 72% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 136 | [x] | Capcom Arcade Stadium (STEAM) | 32 | 2026-11-09 | 42 | 78% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 137 | [x] | Journey (STEAM) | 31 | 2026-10-27 | 72 | 73% |  |
| 138 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 31 | 2026-11-09 | 70 | 75% |  |
| 139 | [x] | Hearts of Iron IV (STEAM) | 31 | 2026-11-09 | 65 | 80% |  |
| 140 | [x] | COCOON (STEAM) | 31 | 2026-11-09 | 64 | 79% |  |
| 141 | [x] | The Bazaar (STEAM) | 31 | 2026-11-09 | 61 | 79% |  |
| 142 | [x] | Yume Nikki (STEAM) | 31 | 2026-11-20 | 56 | 45% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 143 | [x] | Earthion (STEAM) | 31 | 2026-11-09 | 53 | 100% |  |
| 144 | [x] | Asphalt Legends  (STEAM) | 31 | 2026-11-21 | 35 | 62% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 145 | [x] | Red Dead Redemption (STEAM) | 31 | 2026-11-09 | 34 | 41% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 146 | [x] | Elite Dangerous (STEAM) | 31 | 2026-11-20 | 31 | 67% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 147 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 30 | 2026-11-09 | 54 | 72% |  |
| 148 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 30 | 2026-11-09 | 52 | 69% |  |
| 149 | [x] | Resident Evil Village (STEAM) | 30 | 2026-11-09 | 50 | 87% |  |
| 150 | [x] | Need for Speed™ Rivals (STEAM) | 30 | 2026-11-10 | 44 | 73% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 151 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 29 | 2026-11-09 | 52 | 85% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 152 | [x] | Big Walk (STEAM) | 29 | 2026-11-09 | 50 | 65% |  |
| 153 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 29 | 2026-11-09 | 50 | 94% |  |
| 154 | [x] | Prince of Persia: The Sands of Time (STEAM) | 29 | 2026-11-09 | 49 | 79% |  |
| 155 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 29 | 2026-11-09 | 43 | 83% |  |
| 156 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 72% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 157 | [x] | SurrounDead (STEAM) | 28 | 2026-11-09 | 59 | 90% |  |
| 158 | [x] | Resident Evil Revelations 2 (STEAM) | 28 | 2026-11-09 | 54 | 82% |  |
| 159 | [x] | Hero Siege (STEAM) | 28 | 2026-11-09 | 48 | 84% |  |
| 160 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 28 | 2026-11-09 | 48 | 96% |  |
| 161 | [x] | Secrets of Grindea (STEAM) | 28 | 2026-11-09 | 48 | 79% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 162 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 28 | 2026-11-09 | 45 | 71% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 163 | [x] | Supermarket Together (STEAM) | 28 | 2026-11-18 | 41 | 62% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 164 | [x] | Palia (STEAM) | 28 | 2026-11-09 | 40 | 69% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 165 | [x] | Gothic II: Gold Classic (STEAM) | 28 | 2026-11-09 | 36 | 69% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 166 | [x] | Hotline Miami (GOG) | 28 | 2026-11-18 | 35 | 75% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 167 | [x] | Yakuza: Like a Dragon (STEAM) | 27 | 2026-11-09 | 43 | 67% |  |
| 168 | [x] | Tower and Sword of Succubus (STEAM) | 27 | 2026-11-09 | 42 | 81% |  |
| 169 | [x] | Digimon Survive (STEAM) | 27 | 2026-11-09 | 40 | 86% |  |
| 170 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 26 | 2026-11-09 | 59 | 86% |  |
| 171 | [x] | Heavy Rain (STEAM) | 26 | 2026-11-09 | 47 | 90% |  |
| 172 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 44 | 72% |  |
| 173 | [x] | Dead Rising 2 (STEAM) | 26 | 2026-11-09 | 42 | 72% |  |
| 174 | [x] | Ultimate Custom Night (STEAM) | 26 | 2026-11-19 | 36 | 67% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 175 | [x] | Skullgirls 2nd Encore (STEAM) | 25 | 2026-11-10 | 61 | 69% |  |
| 176 | [x] | Frostpunk (STEAM) | 25 | 2026-11-09 | 52 | 81% |  |
| 177 | [x] | Deponia (STEAM) | 25 | 2026-11-09 | 49 | 84% |  |
| 178 | [x] | Cat Mail Co. (STEAM) | 25 | 2026-11-09 | 43 | 91% |  |
| 179 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-19 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 180 | [x] | Chained Echoes (GOG) | 24 | 2026-11-19 | 52 | 68% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 181 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 24 | 2026-11-09 | 47 | 64% |  |
| 182 | [x] | Lobotomy Corporation (STEAM) | 24 | 2026-11-09 | 47 | 92% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 183 | [x] | Mirror's Edge™ (GOG) | 24 | 2026-11-13 | 46 | 83% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 184 | [x] | Lucid Blocks (STEAM) | 24 | 2026-11-09 | 45 | 62% |  |
| 185 | [x] | Battle Brothers (STEAM) | 24 | 2026-11-09 | 44 | 78% |  |
| 186 | [x] | Trailmakers (STEAM) | 24 | 2026-11-09 | 41 | 91% |  |
| 187 | [x] | Gambonanza (STEAM) | 24 | 2026-11-09 | 40 | 89% |  |
| 188 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 24 | 2026-11-09 | 38 | 77% |  |
| 189 | [x] | Ratatan (STEAM) | 24 | 2026-11-09 | 37 | 90% |  |
| 190 | [x] | Subnautica 2 (STEAM) | 24 | 2026-11-15 | 29 | 79% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 191 | [x] | Northgard: Definitive Edition (STEAM) | 24 | 2026-11-22 | 27 | 70% | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 192 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 46 | 92% |  |
| 193 | [x] | Unturned (STEAM) | 23 | 2026-11-09 | 41 | 82% |  |
| 194 | [x] | Opus Magnum (STEAM) | 23 | 2026-11-09 | 36 | 100% |  |
| 195 | [x] | Dishonored 2 (STEAM) | 23 | 2026-11-09 | 34 | 66% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 196 | [x] | Timberborn (STEAM) | 23 | 2026-11-09 | 34 | 94% |  |
| 197 | [x] | Crab Game (STEAM) | 23 | 2026-11-09 | 27 | 80% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 198 | [x] | Football Manager 2024 (EPIC) | 22 | 2026-11-09 | 40 | 63% |  |
| 199 | [x] | Guildrun Demo (STEAM) | 22 | 2026-11-09 | 38 | 85% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 200 | [x] | Strider (STEAM) | 22 | 2026-11-20 | 38 | 67% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 201 | [x] | My Summer Car (STEAM) | 22 | 2026-11-09 | 37 | 76% |  |
| 202 | [x] | Titanfall® 2 (STEAM) | 22 | 2026-11-09 | 37 | 67% |  |
| 203 | [x] | Limbus Company (STEAM) | 22 | 2026-11-09 | 35 | 89% |  |
| 204 | [x] | Mortal Kombat 11 (STEAM) | 22 | 2026-11-09 | 33 | 64% |  |
| 205 | [x] | Changed (STEAM) | 22 | 2026-11-23 | 32 | 62% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 206 | [x] | Jade Empire: Special Edition (GOG) | 22 | 2026-11-09 | 29 | 81% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 207 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 22 | 2026-11-09 | 26 | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 208 | [x] | Tearscape (STEAM) | 22 | 2026-11-09 | 26 | 79% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 209 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 59 | 97% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 210 | [x] | Prince of Persia (GOG) | 21 | 2026-11-09 | 42 | 73% |  |
| 211 | [x] | Invisible, Inc. (STEAM) | 21 | 2026-11-09 | 38 | 85% |  |
| 212 | [x] | Control Ultimate Edition (GOG) | 21 | 2026-11-09 | 37 | 74% |  |
| 213 | [x] | Tabletop Simulator (STEAM) | 21 | 2026-11-09 | 35 | 81% |  |
| 214 | [x] | Goose Goose Duck (STEAM) | 21 | 2026-11-18 | 30 | 82% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 215 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 88% |  |
| 216 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 21 | 2026-11-09 | 27 | 91% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 217 | [x] | CarX Street (STEAM) | 21 | 2026-11-09 | 26 | 75% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 218 | [x] | Dead Island (STEAM) | 21 | 2026-11-09 | 25 | 83% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 219 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-11-09 | 37 | 86% |  |
| 220 | [x] | Capcom Fighting Collection 2 (STEAM) | 20 | 2026-11-09 | 36 | 85% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 221 | [x] | Deus Ex™ GOTY Edition (GOG) | 20 | 2026-11-09 | 33 | 100% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 222 | [x] | Return to Monkey Island (STEAM) | 20 | 2026-11-09 | 32 | 68% |  |
| 223 | [x] | GOD EATER RESURRECTION (STEAM) | 20 | 2026-11-09 | 31 | 86% |  |
| 224 | [x] | CRUEL (STEAM) | 20 | 2026-11-09 | 30 | 83% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 225 | [x] | Nioh: Complete Edition (STEAM) | 20 | 2026-11-23 | 30 | 90% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 226 | [x] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 20 | 2026-11-22 | 21 | 67% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 227 | [x] | Crazy Taxi (STEAM) | 19 | 2026-11-10 | 41 | 64% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 228 | [x] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 2026-11-15 | 38 | 77% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 229 | [x] | Pinball FX Classic (STEAM) | 19 | 2026-11-09 | 37 | 87% |  |
| 230 | [x] | One-armed robber (STEAM) | 19 | 2026-11-09 | 35 | 60% |  |
| 231 | [x] | Worms W.M.D (STEAM) | 19 | 2026-11-09 | 35 | 96% |  |
| 232 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 32 | 85% |  |
| 233 | [x] | Moonlight Peaks (STEAM) | 19 | 2026-11-09 | 32 | 70% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 234 | [x] | Torchlight II (EPIC) | 19 | 2026-11-09 | 27 | 80% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 235 | [x] | Dark Sector (STEAM) | 19 | 2026-11-21 | 25 | 73% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 236 | [x] | Watch Dogs 2 (EPIC) | 19 | 2026-11-23 | 20 | 65% | [#399](https://github.com/GameNative/gamenative-compat/issues/399) |
| 237 | [x] | Wizard of Legend (EPIC) | 18 | 2026-11-09 | 37 | 78% |  |
| 238 | [x] | Counter-Strike: Condition Zero (STEAM) | 18 | 2026-11-11 | 37 | 29% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 239 | [x] | Mini Metro (STEAM) | 18 | 2026-11-16 | 37 | 61% |  |
| 240 | [x] | This War of Mine (STEAM) | 18 | 2026-11-17 | 33 | 48% |  |
| 241 | [x] | Far Far West (STEAM) | 18 | 2026-11-09 | 32 | 55% |  |
| 242 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 2026-11-09 | 29 | 86% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 243 | [x] | Beyond: Two Souls (STEAM) | 18 | 2026-11-22 | 27 | 67% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 244 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-11-09 | 27 | 84% |  |
| 245 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-18 | 23 | 75% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 246 | [x] | Mafia II: Definitive Edition (GOG) | 18 | 2026-11-15 | 20 | 60% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 247 | [x] | Jade Empire: Special Edition (STEAM) | 18 | 2026-11-09 | 20 | 71% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 248 | [x] | Backpack Battles (STEAM) | 17 | 2026-11-09 | 39 | 94% |  |
| 249 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 36 | 40% |  |
| 250 | [x] | Intravenous 2 (STEAM) | 17 | 2026-11-09 | 33 | 100% |  |
| 251 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 33 | 77% |  |
| 252 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 17 | 2026-11-09 | 27 | 88% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 253 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 17 | 2026-11-15 | 26 | 61% |  |
| 254 | [x] | Bongo Cat (STEAM) | 17 | 2026-11-20 | 24 | 64% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 255 | [x] | Tales of Zestiria (STEAM) | 17 | 2026-11-09 | 24 | 67% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 256 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 16 | 2026-11-11 | 36 | 78% |  |
| 257 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 258 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 16 | 2026-11-09 | 30 | 67% |  |
| 259 | [x] | PAYDAY: The Heist (STEAM) | 16 | 2026-11-13 | 28 | 80% |  |
| 260 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 71% |  |
| 261 | [x] | Party Animals (STEAM) | 16 | 2026-11-09 | 24 | 76% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 262 | [x] | Capcom Fighting Collection (STEAM) | 16 | 2026-11-09 | 23 | 90% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 263 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 16 | 2026-11-09 | 23 | 76% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 264 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 265 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 266 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 15 | 2026-10-25 | 42 | 73% |  |
| 267 | [x] | Styx: Master of Shadows (EPIC) | 15 | 2026-11-23 | 40 | 50% |  |
| 268 | [x] | Flotsam (EPIC) | 15 | 2026-11-20 | 34 | 41% |  |
| 269 | [x] | sobosuba (STEAM) | 15 | 2026-11-09 | 34 | 84% |  |
| 270 | [x] | Mark of the Ninja (STEAM) | 15 | 2026-10-26 | 31 | 88% |  |
| 271 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 29 | 100% |  |
| 272 | [x] | AER Memories of Old (EPIC) | 15 | 2026-11-09 | 24 | 93% |  |
| 273 | [x] | Disgaea 4 Complete+ (STEAM) | 15 | 2026-11-09 | 24 | 93% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 274 | [x] | Alabaster Dawn Demo (STEAM) | 15 | 2026-11-09 | 23 | 69% |  |
| 275 | [x] | Need for Speed™ Unbound (STEAM) | 15 | 2026-11-09 | 23 | 58% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 276 | [x] | Nex Machina (STEAM) | 15 | 2026-11-09 | 23 | 76% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 277 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 93% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 278 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 279 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 280 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 88% |  |
| 281 | [x] | Castle in the Clouds (STEAM) | 14 | 2026-11-09 | 28 | 64% |  |
| 282 | [x] | SWORN (STEAM) | 14 | 2026-11-09 | 28 | 94% |  |
| 283 | [x] | Another World: 20th Anniversary Edition (GOG) | 14 | 2026-11-21 | 24 | 62% |  |
| 284 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 2026-11-16 | 22 | 93% |  |
| 285 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 21 | 60% |  |
| 286 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 287 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 288 | [x] | Spark the Electric Jester (STEAM) | 14 | 2026-11-13 | 20 | 77% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 289 | [x] | Overlord (STEAM) | 13 | 2026-11-08 | 30 | 59% |  |
| 290 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 30 | 86% |  |
| 291 | [x] | Blaster Master Zero (STEAM) | 13 | 2026-11-11 | 28 | 79% |  |
| 292 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 13 | 2026-11-09 | 28 | 90% |  |
| 293 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 13 | 2026-11-13 | 28 | 64% |  |
| 294 | [x] | Human Fall Flat (STEAM) | 13 | 2026-10-29 | 27 | 61% |  |
| 295 | [x] | Batman™: Arkham Origins (GOG) | 13 | 2026-11-09 | 26 | 94% |  |
| 296 | [x] | Evoland (STEAM) | 13 | 2026-11-11 | 26 | n/a |  |
| 297 | [x] | MX Bikes (STEAM) | 13 | 2026-11-09 | 26 | 96% |  |
| 298 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 26 | 95% |  |
| 299 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 24 | 74% |  |
| 300 | [x] | Horny Villa (STEAM) | 13 | 2026-11-09 | 22 | 78% |  |
| 301 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 302 | [x] | Shift At Midnight (STEAM) | 13 | 2026-11-09 | 21 | 90% |  |
| 303 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 70% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 304 | [x] | War of Dots (STEAM) | 13 | 2026-11-22 | 21 | 60% | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 305 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 93% |  |
| 306 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 307 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 2026-11-09 | 20 | 85% |  |
| 308 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-11-16 | 20 | 92% |  |
| 309 | [x] | Turbo Overkill (STEAM) | 13 | 2026-11-09 | 20 | 100% |  |
| 310 | [x] | GRIP: Combat Racing (STEAM) | 12 | 2026-11-09 | 33 | 79% |  |
| 311 | [x] | Antichamber (STEAM) | 12 | 2026-11-18 | 27 | 80% |  |
| 312 | [x] | Tiny Glade (STEAM) | 12 | 2026-11-09 | 27 | 69% |  |
| 313 | [x] | Cruelty Squad (STEAM) | 12 | 2026-11-09 | 24 | 87% |  |
| 314 | [x] | Legend of Grimrock 2 (STEAM) | 12 | 2026-11-09 | 24 | 93% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 315 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 24 | 64% |  |
| 316 | [x] | Sonic Superstars (STEAM) | 12 | 2026-11-21 | 24 | 64% |  |
| 317 | [x] | A Plague Tale: Innocence (GOG) | 12 | 2026-11-18 | 23 | 64% |  |
| 318 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-11-09 | 23 | 92% |  |
| 319 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 320 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 321 | [x] | 12 is Better Than 6 (STEAM) | 12 | 2026-11-09 | 20 | 75% |  |
| 322 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 323 | [x] | Hitman: Contracts (STEAM) | 12 | 2026-11-23 | 20 | 69% |  |
| 324 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 28 | 100% |  |
| 325 | [x] | Alan Wake's American Nightmare (EPIC) | 11 | 2026-11-09 | 24 | 73% |  |
| 326 | [x] | Ultrapool (STEAM) | 11 | 2026-11-09 | 24 | n/a |  |
| 327 | [x] | HITMAN World of Assassination (STEAM) | 11 | 2026-11-09 | 23 | 74% |  |
| 328 | [x] | Life is Strange Remastered (STEAM) | 11 | 2026-11-09 | 23 | 86% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 329 | [x] | Ready or Not (STEAM) | 11 | 2026-11-09 | 23 | 82% |  |
| 330 | [x] | Lost Castle 2 (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 331 | [x] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 2026-11-18 | 21 | 71% |  |
| 332 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 11 | 2026-10-27 | 21 | 86% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 333 | [x] | Forgive Me Father (STEAM) | 11 | 2026-11-15 | 21 | 70% |  |
| 334 | [x] | Haydee (STEAM) | 11 | 2026-11-09 | 21 | 79% |  |
| 335 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 336 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-11-09 | 20 | 69% |  |
| 337 | [x] | The Stanley Parable (STEAM) | 11 | 2026-11-13 | 20 | 75% |  |
| 338 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 28 | 91% |  |
| 339 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 10 | 2026-10-27 | 27 | 82% |  |
| 340 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 25 | 92% |  |
| 341 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 10 | 2026-11-09 | 24 | 89% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 342 | [x] | GRANDIA HD Remaster (STEAM) | 10 | 2026-11-09 | 23 | 93% |  |
| 343 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 22 | 84% |  |
| 344 | [x] | UNDEFEATED (STEAM) | 10 | 2026-11-09 | 22 | 75% |  |
| 345 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 10 | 2026-11-10 | 21 | 69% |  |
| 346 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 347 | [x] | DiRT 4 (STEAM) | 10 | 2026-11-09 | 20 | 100% |  |
| 348 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 349 | [x] | Pillars of Eternity (STEAM) | 10 | 2026-11-21 | 20 | 100% |  |
| 350 | [x] | Secret of Mana (STEAM) | 10 | 2026-11-18 | 20 | 70% |  |
| 351 | [x] | Rayman Origins (GOG) | 9 | 2026-11-09 | 24 | 62% |  |
| 352 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 9 | 2026-11-01 | 24 | n/a |  |
| 353 | [x] | Breath of Fire IV (GOG) | 9 | 2026-10-26 | 23 | 53% |  |
| 354 | [x] | Guacamelee! Gold Edition (STEAM) | 9 | 2026-11-11 | 22 | 75% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 355 | [x] | Need for Speed: Undercover (STEAM) | 9 | 2026-11-11 | 22 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 356 | [x] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 9 | 2026-11-17 | 20 | 33% |  |
| 357 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 27% |  |
| 358 | [x] | WORLD OF FINAL FANTASY (STEAM) | 8 | 2026-11-09 | 23 | 89% |  |
| 359 | [x] | Lust Goddess (STEAM) | 8 | 2026-11-09 | 22 | 79% |  |
| 360 | [x] | Aperture Desk Job (STEAM) | 8 | 2026-11-03 | 21 | n/a |  |
| 361 | [x] | SteamWorld Heist (GOG) | 8 | 2026-10-25 | 20 | n/a |  |
| 362 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 8 | 2026-11-09 | 20 | 73% |  |
| 363 | [x] | Soul's Remnant (STEAM) | 8 | 2026-11-11 | 20 | n/a |  |
| 364 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 23 | 53% |  |
| 365 | [x] | SCP – Containment Breach (STEAM) | 7 | 2026-10-27 | 21 | 91% |  |
| 366 | [x] | Mina the Hollower (GOG) | 7 | 2026-10-28 | 20 | 74% |  |
| 367 | [x] | CULTIC (STEAM) | 7 | 2026-11-09 | 20 | 53% |  |
| 368 | [x] | Possessor(s) (STEAM) | 6 | 2026-10-24 | 22 | 73% |  |
