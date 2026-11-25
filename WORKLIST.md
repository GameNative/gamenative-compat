# GameNative compatibility worklist

Generated: `2026-11-25T04:15:12.681Z` · Ratings since: `2026-08-27T04:15:12.681Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 127 |
| Probably does not work | 182 |
| Fix shipped, waiting for ratings | 16 |
| First launch fails | 296 |
| Mixed | 459 |
| Works | 1021 |
| Total | 2101 |

## Does not work (127)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 205 | 241 | 85% (since fix) | Does not open (91%) | 39% | today | 34% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 2 | [ ] | Slay the Spire (STEAM) | 125 | 154 | 81% (14d) | Does not open (83%) | 42% | today | 32% | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 3 | [ ] | Rocket League® (EPIC) | 84 | 96 | 88% (14d) | Does not open (81%) | 31% | today | 26% | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 4 | [ ] | Buckshot Roulette (STEAM) | 44 | 62 | 71% (14d) | Does not open (69%) | 54% | today | 45% | [#558](https://github.com/GameNative/gamenative-compat/issues/558) |
| 5 | [ ] | Melvor Idle 2: A RuneScape Adventure (STEAM) | 41 | 44 | 93% (14d) | Does not open (94%) | 42% | today | 41% | [#543](https://github.com/GameNative/gamenative-compat/issues/543) |
| 6 | [ ] | Horizon Chase Turbo (EPIC) | 33 | 39 | 85% (14d) | Does not open (82%) | 50% | today | 43% | [#546](https://github.com/GameNative/gamenative-compat/issues/546) |
| 7 | [ ] | Hogwarts Legacy (STEAM) | 29 | 31 | 94% (14d) | Does not open (72%) | 22% | today | 15% | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 8 | [ ] | Mark of the Deep (EPIC) | 27 | 36 | 75% (14d) | Does not open (88%) | 24% | today | 22% | [#549](https://github.com/GameNative/gamenative-compat/issues/549) |
| 9 | [ ] | Borderlands 2 (EPIC) | 26 | 27 | 96% (14d) | Does not open (81%) | 48% | today | 45% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 10 | [ ] | DREDGE (EPIC) | 23 | 28 | 82% (14d) | Does not open (79%) | 51% | 2d ago | 46% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 11 | [x] 2026-10-18 | Project Zomboid (STEAM) | 64 | 72 | 89% (since fix) | Does not open (65%) | 36% | today | 36% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 12 | [ ] | Absolute Drift (EPIC) | 21 | 30 | 70% (14d) | No graphics (60%) | 45% | today | 32% | [#555](https://github.com/GameNative/gamenative-compat/issues/555) |
| 13 | [ ] | Path of Exile (STEAM) | 21 | 25 | 84% (14d) | Does not open (88%) | 26% | today | 25% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 14 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 20 | 20 | 100% (last 20) | Does not open (96%) | 26% | 2d ago | 20% | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 15 | [ ] | Dead Island 2 (EPIC) | 20 | 20 | 100% (last 20) | Does not open (87%) | 46% | today | 34% | [#552](https://github.com/GameNative/gamenative-compat/issues/552) |
| 16 | [ ] | Bloons TD 6 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (77%) | 34% | today | 25% | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 17 | [ ] | Saints Row 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | 29% | 1d ago | 29% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 18 | [ ] | Driver: Parallel Lines (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | 43% | 3d ago | 46% | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 19 | [ ] | Metro: Last Light Redux (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | 28% | today | 29% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 20 | [ ] | Castlevania Anniversary Collection (EPIC) | 19 | 20 | 95% (last 20) | Does not open (79%) | 45% | 1d ago | 35% | [#556](https://github.com/GameNative/gamenative-compat/issues/556) |
| 21 | [ ] | Saints Row 2 (GOG) | 18 | 20 | 90% (last 20) | Does not open (91%) | 33% | 1d ago | 32% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 22 | [ ] | Hogwarts Legacy (EPIC) | 18 | 20 | 90% (last 20) | Does not open (75%) | 42% | today | 34% | [#537](https://github.com/GameNative/gamenative-compat/issues/537) |
| 23 | [ ] | Sifu (EPIC) | 15 | 20 | 75% (last 20) | Does not open (70%) | 39% | 1d ago | 35% | [#535](https://github.com/GameNative/gamenative-compat/issues/535) |
| 24 | [ ] | BioShock Remastered (EPIC) | 14 | 20 | 70% (14d) | Does not open (68%) | 51% | 2d ago | 49% | [#547](https://github.com/GameNative/gamenative-compat/issues/547) |
| 25 | [ ] | Until Then (STEAM) | 18 | 20 | 90% (last 20) | Does not open (88%) | 58% | today | 45% | [#559](https://github.com/GameNative/gamenative-compat/issues/559) |
| 26 | [ ] | River City Girls (EPIC) | 15 | 20 | 75% (last 20) | Does not open (50%) | 48% | 3d ago | 37% | [#550](https://github.com/GameNative/gamenative-compat/issues/550) |
| 27 | [ ] | Bad Cheese (EPIC) | 16 | 20 | 80% (last 20) | Does not open (94%) | 42% | 1d ago | 33% | [#560](https://github.com/GameNative/gamenative-compat/issues/560) |
| 28 | [ ] | Vampire Survivors (EPIC) | 17 | 20 | 85% (last 20) | Does not open (65%) | 36% | today | 31% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 29 | [ ] | Mafia II (Classic) (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | 8% | today | 10% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 30 | [ ] | skate. (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 9% | today | 10% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 31 | [ ] | Call of Duty: Black Ops II (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 44% | today | 42% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 32 | [ ] | VRChat (STEAM) | 14 | 20 | 70% (last 20) | Does not open (74%) | 38% | today | 35% |  |
| 33 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 56% | 6d ago | 55% | [#553](https://github.com/GameNative/gamenative-compat/issues/553) |
| 34 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 18 | 20 | 90% (last 20) | Does not open (86%) | 50% | today | 52% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 35 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 50% | 1d ago | 45% | [#548](https://github.com/GameNative/gamenative-compat/issues/548) |
| 36 | [ ] | Forza Horizon 4 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (43%) | 37% | 2d ago | 23% | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 37 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (91%) | 19% | 11d ago | 14% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 38 | [ ] | Teenage Mutant Ninja Turtles: Shredder's Revenge (EPIC) | 15 | 20 | 75% (last 20) | Does not open (83%) | 44% | 2d ago | 42% | [#551](https://github.com/GameNative/gamenative-compat/issues/551) |
| 39 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 36% | today | 32% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 40 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (76%) | 6% | 10d ago | 7% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 41 | [ ] | Trackmania (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 29% | 3d ago | 29% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 42 | [ ] | Fall Guys (EPIC) | 20 | 20 | 100% (last 20) | Does not open (68%) | 4% | 2d ago | 4% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 43 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (71%) | 30% | 6d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 44 | [ ] | Kenshi (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 7% | 3d ago | 6% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 45 | [ ] | Metro 2033 Redux (EPIC) | 14 | 20 | 70% (last 20) | Does not open (67%) | 33% | 1d ago | 33% | [#561](https://github.com/GameNative/gamenative-compat/issues/561) |
| 46 | [ ] | Detroit: Become Human (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | 56% | today | 56% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 47 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (82%) | 4% | 1d ago | 4% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 48 | [ ] | Happy Wheels (STEAM) | 18 | 20 | 90% (last 20) | No graphics (52%) | 52% | 1d ago | 47% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 49 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (73%) | 17% | 3d ago | 18% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 50 | [ ] | Breath of Fire IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | 12% | 5d ago | 9% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 51 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (83%) | 56% | 3d ago | 52% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 52 | [ ] | The Witcher: Enhanced Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (75%) | 8% | 3d ago | 9% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 53 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (94%) | 7% | 7d ago | 0% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 54 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (72%) | 0% | 10d ago | 0% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 55 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | 7% | 24d ago | 8% | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 56 | [ ] | Call of Duty® (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | 0% | 4d ago | 0% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 57 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (82%) | 10% | 3d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 58 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (68%) | 18% | 11d ago | 23% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 59 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (81%) | 12% | 16d ago | 13% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 60 | [ ] | MECCHA CHAMELEON (STEAM) | 15 | 20 | 75% (last 20) | Does not open (69%) | 38% | 7d ago | 36% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 61 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (74%) | 45% | today | 44% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 62 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 52% | 9d ago | 53% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 63 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (88%) | 56% | 1d ago | 50% | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 64 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (67%) | 10% | 2d ago | n/a | [#536](https://github.com/GameNative/gamenative-compat/issues/536) |
| 65 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (82%) | 44% | 7d ago | 45% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 66 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | 42% | 4d ago | 46% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 67 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (77%) | 5% | 1d ago | 6% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 68 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (91%) | 0% | 11d ago | 0% | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 69 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (53%) | 31% | 7d ago | 18% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 70 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (91%) | 21% | today | 18% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 71 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (67%) | 21% | 13d ago | 19% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 72 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 33% | 2d ago | 37% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 73 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 50% | 2d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 74 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | 0% | 10d ago | 0% | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 75 | [ ] | Half-Life: Blue Shift (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | 47% | 8d ago | 50% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 76 | [ ] | Rivals of Aether II (STEAM) | 16 | 20 | 80% (last 20) | Does not open (53%) | 31% | today | 9% (drop) | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 77 | [ ] | Black Mesa (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 31% | 3d ago | 31% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 78 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | 10% | 12d ago | 10% | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 79 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 53% | 11d ago | 53% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 80 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (48%) | 47% | 4d ago | 45% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 81 | [ ] | A Plague Tale: Innocence (EPIC) | 14 | 20 | 70% (last 20) | Does not open (70%) | 46% | 2d ago | 41% | [#557](https://github.com/GameNative/gamenative-compat/issues/557) |
| 82 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 19 | 20 | 95% (last 20) | Does not open (85%) | 45% | 8d ago | 50% | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 83 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | 13% | 13d ago | 11% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 84 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 3% | 1d ago | 2% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 85 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 17% | 2d ago | 20% | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 86 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (73%) | 25% | 18d ago | 20% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 87 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | Does not open (63%) | 29% | 4d ago | 28% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 88 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 17 | 20 | 85% (last 20) | Does not open (62%) | 21% | 3d ago | 23% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 89 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 56% | 14d ago | 42% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 90 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (59%) | 58% | 13d ago | 62% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 91 | [ ] | Umamusume: Pretty Derby (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 50% | 5d ago | 55% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 92 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 0% | 25d ago | 0% | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 93 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 32% | 4d ago | 38% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 94 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (50%) | 58% | 6d ago | 66% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 95 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (71%) | 7% | 38d ago | 9% | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 96 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (63%) | 0% | 1d ago | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 97 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 50% | today | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 98 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 3% | 3d ago | 3% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 99 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | 45% | 14d ago | 45% | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 100 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 19 | 20 | 95% (last 20) | Does not open (58%) | 32% | 2d ago | 39% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 101 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | 33% | 2d ago | 30% | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 102 | [ ] | Aliens vs. Predator (STEAM) | 17 | 20 | 85% (last 20) | Does not open (73%) | 29% | 3d ago | 30% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 103 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (64%) | 43% | 5d ago | 43% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 104 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (61%) | 35% | 1d ago | 25% | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 105 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 20% | 5d ago | 15% | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 106 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 20 | 80% (last 20) | Does not open (53%) | 43% | 1d ago | 33% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 107 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 7% | 31d ago | 8% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 108 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (89%) | 33% | 9d ago | 33% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 109 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (96%) | 30% | 23d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 110 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 57% | 4d ago | 50% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 111 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (52%) | 55% | 28d ago | 44% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 112 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | 21% | 25d ago | 21% | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 113 | [ ] | OneShot (STEAM) | 15 | 20 | 75% (last 20) | Does not open (94%) | 17% | 4d ago | 20% | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 114 | [ ] | Lost Planet: Extreme Condition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 50% | 10d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 115 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 43% | 3d ago | 37% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 116 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (55%) | 39% | 13d ago | 23% | [#540](https://github.com/GameNative/gamenative-compat/issues/540) |
| 117 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 20% | 2d ago | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 118 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 40% | 3d ago | 46% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 119 | [ ] | Darksiders Warmastered Edition (EPIC) | 17 | 20 | 85% (last 20) | Does not open (83%) | 50% | today | 33% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 120 | [ ] | Maneater (EPIC) | 17 | 20 | 85% (last 20) | Does not open (73%) | 25% | 2d ago | 17% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 121 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | 36% | 14d ago | 27% | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 122 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (58%) | 54% | 13d ago | 54% | [#554](https://github.com/GameNative/gamenative-compat/issues/554) |
| 123 | [ ] | Ghostwire Tokyo (EPIC) | 14 | 20 | 70% (last 20) | Does not open (90%) | 38% | 1d ago | 35% | [#544](https://github.com/GameNative/gamenative-compat/issues/544) |
| 124 | [ ] | Bongo Cat (STEAM) | 16 | 20 | 80% (last 20) | Does not open (91%) | 59% | 4d ago | 50% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 125 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (54%) | 36% | 10d ago | 38% | [#541](https://github.com/GameNative/gamenative-compat/issues/541) |
| 126 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 14 | 20 | 70% (last 20) | Does not open (88%) | 20% | 1d ago | 23% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 127 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (67%) | 27% | 20d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |

## Probably does not work (182)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Counter-Strike 2 (STEAM) | 55 | 83 | 66% (since fix) | Does not open (68%) | 58% | today | 56% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 2 | [ ] | Owlboy (STEAM) | 18 | 28 | 64% (14d) | Does not open (80%) | 54% | today | 50% | [#545](https://github.com/GameNative/gamenative-compat/issues/545) |
| 3 | [ ] | Metro 2033 Redux (STEAM) | 14 | 23 | 61% (14d) | Does not open (71%) | 43% | today | 42% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 4 | [ ] | Bully: Scholarship Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 31% | 2d ago | 13% |  |
| 5 | [ ] | theHunter Classic (STEAM) | 20 | 20 | 100% (last 20) | No graphics (92%) | n/a | 21d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 6 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 12 | 20 | 60% (last 20) | Does not open (79%) | 52% | today | 48% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 7 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 26 | 47 | 55% (since fix) | Does not open (73%) | 58% | 2d ago | 57% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 8 | [ ] | Garry's Mod (STEAM) | 16 | 26 | 62% (since fix) | Does not open (80%) | 48% | 1d ago | 44% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 9 | [ ] | To The Moon (GOG) | 18 | 20 | 90% (last 20) | Does not open (86%) | n/a | 22d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 10 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 11 | 20 | 55% (last 20) | Does not open (71%) | 34% | today | 37% |  |
| 11 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (78%) | n/a | 16d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 12 | [ ] | Batman™ Arkham Asylum Game of the Year Edition (EPIC) | 12 | 20 | 60% (last 20) | Does not open (75%) | 48% | today | 41% |  |
| 13 | [ ] | Catherine Classic (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (40%) | 44% | today | 42% |  |
| 14 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 13 | 20 | 65% (last 20) | Does not open (63%) | 42% | today | 40% |  |
| 15 | [ ] | Asterigos: Curse of the Stars (STEAM) | 16 | 20 | 80% (last 20) | Graphics glitches (73%) | n/a | 3d ago | n/a |  |
| 16 | [ ] | Cat Quest (EPIC) | 11 | 20 | 55% (last 20) | Does not open (48%) | 42% | 2d ago | 39% |  |
| 17 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 16 | 24 | 67% (since fix) | Does not open (77%) | 40% | 2d ago | 42% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 18 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 10 | 16 | 63% (since fix) | Does not open (91%) | 48% | today | 49% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 19 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 8 | 12 | 67% (since fix) | Does not open (82%) | 59% | 3d ago | 60% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 20 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 45d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 21 | [ ] | PAYDAY: The Heist (STEAM) | 16 | 20 | 80% (last 20) | Does not open (81%) | n/a | today | n/a |  |
| 22 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (39%) | n/a | 4d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 23 | [ ] | Sonic Adventure™ 2  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (77%) | 45% | today | 38% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 24 | [ ] | STAR WARS™ Knights of the Old Republic™ II: The Sith Lords™ (STEAM) | 12 | 20 | 60% (last 20) | No graphics (64%) | 47% | 4d ago | 39% |  |
| 25 | [ ] | Darksiders Warmastered Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 44% | 2d ago | 36% |  |
| 26 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 11d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 27 | [ ] | Door Kickers 2 (STEAM) | 18 | 20 | 90% (last 20) | No graphics (86%) | n/a | 2d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 28 | [ ] | Art of Rally (EPIC) | 12 | 20 | 60% (last 20) | Does not open (77%) | 34% | 2d ago | 34% |  |
| 29 | [ ] | MudRunner (EPIC) | 12 | 20 | 60% (last 20) | Does not open (68%) | 48% | 2d ago | 41% |  |
| 30 | [ ] | Deskrawl: Idle ARPG (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | n/a | 14d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 31 | [ ] | Hi-Fi RUSH (STEAM) | 13 | 20 | 65% (last 20) | Does not open (77%) | 46% | 1d ago | 46% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 32 | [ ] | Gorilla Tag (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 13% | today | 8% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 33 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 11 | 20 | 55% (last 20) | Does not open (75%) | 48% | today | 44% |  |
| 34 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (79%) | 55% | 4d ago | 52% |  |
| 35 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 29d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 36 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (100%) | n/a | 2d ago | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 37 | [ ] | Counter-Strike (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 34% | today | 32% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 38 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (49%) | 50% | 11d ago | 38% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 39 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | No graphics (59%) | n/a | 28d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 40 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | No graphics (38%) | 45% | 3d ago | 38% |  |
| 41 | [ ] | Phasmophobia (STEAM) | 11 | 20 | 55% (last 20) | Does not open (56%) | 52% | today | 45% |  |
| 42 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (87%) | n/a | 18d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 43 | [ ] | Deliver At All Costs (EPIC) | 13 | 20 | 65% (last 20) | Does not open (61%) | 41% | 1d ago | 43% | [#538](https://github.com/GameNative/gamenative-compat/issues/538) |
| 44 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 12 | 20 | 60% (last 20) | Does not open (88%) | 44% | 5d ago | 23% (drop) | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 45 | [ ] | Counter-Strike:Global Offensive (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 58% | 2d ago | 57% |  |
| 46 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 26d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 47 | [ ] | CPM 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (88%) | 3% | 3d ago | 3% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 48 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | n/a | 8d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 49 | [ ] | Saints Row IV Re-Elected (EPIC) | 10 | 20 | 50% (last 20) | No graphics (50%) | 36% | today | 33% |  |
| 50 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | n/a | 17d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 51 | [ ] | Borderlands GOTY (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 38% | today | 50% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 52 | [ ] | Stumble Guys (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 58% | 3d ago | 57% |  |
| 53 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (89%) | n/a | 10d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 54 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 20d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 55 | [ ] | CODE VEIN (STEAM) | 13 | 20 | 65% (last 20) | Does not open (68%) | 24% | 9d ago | 13% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 56 | [ ] | No More Heroes (STEAM) | 13 | 20 | 65% (last 20) | Does not open (68%) | 35% | today | 32% |  |
| 57 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | 50% | 1d ago | 46% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 58 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | n/a | 23d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 59 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | n/a | 10d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 60 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | n/a | 6d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 61 | [ ] | Rise of the Tomb Raider: 20 Year Celebration (EPIC) | 13 | 20 | 65% (last 20) | Does not open (73%) | 38% | 1d ago | 36% |  |
| 62 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (72%) | 24% | today | 18% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 63 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 43d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 64 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | n/a | 23d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 65 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | n/a | 34d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 66 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (56%) | n/a | 6d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 67 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | n/a | 3d ago | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 68 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 14d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 69 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (74%) | n/a | 22d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 70 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (70%) | n/a | 44d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 71 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | 11d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 72 | [ ] | Dead Space 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (63%) | 31% | today | 28% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 73 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 42d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 74 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | n/a | 11d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 75 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | n/a | 26d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 76 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (57%) | n/a | 10d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 77 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 20d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 78 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 33% | 8d ago | 30% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 79 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 38% | today | 33% |  |
| 80 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | n/a | 45d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 81 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 42d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 82 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (58%) | n/a | 11d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 83 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (53%) | n/a | 1d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 84 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (75%) | n/a | today | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 85 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 28d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 86 | [ ] | Alpha Protocol (STEAM) | 16 | 20 | 80% (last 20) | No graphics (56%) | n/a | today | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 87 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | n/a | 17d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 88 | [ ] | Metro 2033 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (65%) | 40% | 4d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 89 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 24d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 90 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 23d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 91 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 11d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 92 | [ ] | Borderlands 2 RU (STEAM) | 18 | 20 | 90% (last 20) | Does not open (58%) | n/a | 8d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 93 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | 7d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 94 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 16d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 95 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 28d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 96 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 55% | 21d ago | 50% |  |
| 97 | [ ] | Pathway (EPIC) | 19 | 20 | 95% (last 20) | Does not open (59%) | n/a | 1d ago | n/a | [#298](https://github.com/GameNative/gamenative-compat/issues/298) |
| 98 | [ ] | Beholder (EPIC) | 18 | 20 | 90% (last 20) | Does not open (61%) | n/a | 4d ago | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 99 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | n/a | 47d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 100 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | n/a | 4d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 101 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | n/a | 7d ago | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 102 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (58%) | n/a | today | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 103 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (64%) | n/a | 51d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 104 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (76%) | n/a | 1d ago | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 105 | [ ] | DOOM Eternal (STEAM) | 16 | 20 | 80% (last 20) | Does not open (66%) | n/a | today | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 106 | [ ] | Brutal Legend (GOG) | 16 | 20 | 80% (last 20) | Does not open (82%) | n/a | 3d ago | n/a |  |
| 107 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | n/a | 9d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 108 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (54%) | n/a | 30d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 109 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 13 | 20 | 65% (last 20) | Does not open (88%) | n/a | today | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 110 | [ ] | Hollow Knight: Silksong (GOG) | 10 | 20 | 50% (last 20) | Does not open (64%) | 49% | 3d ago | 47% |  |
| 111 | [ ] | The Survivalists (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | n/a | 12d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 112 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (53%) | n/a | 18d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 113 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 20d ago | n/a |  |
| 114 | [ ] | Super Meat Boy Forever (EPIC) | 10 | 20 | 50% (last 20) | Does not open (83%) | 33% | 5d ago | 26% |  |
| 115 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 16d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 116 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | n/a | 18d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 117 | [ ] | Utopia Must Fall (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | n/a | 1d ago | n/a | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 118 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | n/a | 15d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 119 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 13d ago | n/a |  |
| 120 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (47%) | n/a | 9d ago | n/a |  |
| 121 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 50% | today | 58% | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 122 | [ ] | Lucid Blocks (STEAM) | 11 | 20 | 55% (last 20) | Does not open (94%) | 58% | 5d ago | 52% |  |
| 123 | [ ] | Goat Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 56% | 1d ago | 55% |  |
| 124 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 26d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 125 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (36%) | n/a | 3d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 126 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 13d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 127 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 27d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 128 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | n/a | 7d ago | n/a | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 129 | [ ] | Drop Duchy (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 10% | 6d ago | n/a |  |
| 130 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 20d ago | n/a |  |
| 131 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 20d ago | n/a |  |
| 132 | [ ] | Mafia: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 34% | today | 32% |  |
| 133 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Controller issues (36%) | n/a | 6d ago | n/a |  |
| 134 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 10 | 20 | 50% (last 20) | Does not open (90%) | 42% | 3d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 135 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | n/a | 9d ago | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 136 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | Does not open (43%) | n/a | 15d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 137 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | n/a | 5d ago | n/a |  |
| 138 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 13 | 20 | 65% (last 20) | Does not open (55%) | 27% | 9d ago | 27% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 139 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 45% | 13d ago | n/a |  |
| 140 | [ ] | Mortal Shell (EPIC) | 13 | 20 | 65% (last 20) | Does not open (50%) | 24% | 6d ago | 19% |  |
| 141 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 13 | 20 | 65% (last 20) | Does not open (100%) | n/a | today | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 142 | [ ] | Hitman 2: Silent Assassin (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 39% | 2d ago | 38% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 143 | [ ] | FINAL FANTASY VII REMAKE INTERGRADE (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 43% | today | 43% |  |
| 144 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 30% | 25d ago | 29% |  |
| 145 | [ ] | HOT WHEELS UNLEASHED™ (EPIC) | 12 | 20 | 60% (last 20) | No graphics (50%) | 38% | 1d ago | 32% |  |
| 146 | [ ] | Dying Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (77%) | 43% | 2d ago | 36% |  |
| 147 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | 12d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 148 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (80%) | n/a | today | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 149 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | n/a | 37d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 150 | [ ] | Shank 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (81%) | n/a | today | n/a |  |
| 151 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (63%) | 50% | 11d ago | n/a |  |
| 152 | [ ] | Romancing SaGa -Minstrel Song- Remastered (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (100%) | n/a | 3d ago | n/a |  |
| 153 | [ ] | Sid Meier's Civilization VI (EPIC) | 13 | 20 | 65% (last 20) | Does not open (58%) | 56% | 1d ago | 50% |  |
| 154 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (58%) | n/a | 2d ago | n/a |  |
| 155 | [ ] | Crying Suns (EPIC) | 12 | 20 | 60% (last 20) | No graphics (56%) | n/a | 2d ago | n/a |  |
| 156 | [ ] | DAEMON X MACHINA (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 38% | 2d ago | 26% |  |
| 157 | [ ] | Decktamer (STEAM) | 13 | 20 | 65% (last 20) | Does not open (100%) | n/a | 2d ago | n/a |  |
| 158 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | 36% | 14d ago | 40% |  |
| 159 | [ ] | Minit (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | n/a | today | n/a |  |
| 160 | [ ] | Songs of Conquest (EPIC) | 13 | 20 | 65% (last 20) | Does not open (75%) | n/a | 9d ago | n/a |  |
| 161 | [ ] | Sandustry (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | n/a | 10d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 162 | [ ] | LET IT DIE (STEAM) | 12 | 20 | 60% (last 20) | Does not open (94%) | n/a | 3d ago | n/a |  |
| 163 | [ ] | Chasm (GOG) | 12 | 20 | 60% (last 20) | No graphics (50%) | n/a | 10d ago | n/a |  |
| 164 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | n/a | 2d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 165 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | n/a | 6d ago | n/a |  |
| 166 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 11 | 20 | 55% (last 20) | Does not open (100%) | 33% | 3d ago | 30% |  |
| 167 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Does not open (44%) | n/a | 16d ago | n/a |  |
| 168 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 10 | 20 | 50% (last 20) | No graphics (60%) | 56% | 9d ago | 64% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 169 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | n/a | 15d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 170 | [ ] | Turnip Boy Robs a Bank (EPIC) | 12 | 20 | 60% (last 20) | Does not open (73%) | 38% | today | 36% | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 171 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 20d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 172 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 54% | 4d ago | 59% |  |
| 173 | [ ] | LEGO® MARVEL's Avengers (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 31% | today | 27% |  |
| 174 | [ ] | Hitman: Absolution (GOG) | 10 | 20 | 50% (last 20) | Does not open (82%) | n/a | 7d ago | n/a |  |
| 175 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (60%) | 17% | 6d ago | 0% |  |
| 176 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 26d ago | n/a |  |
| 177 | [ ] | Allumeria (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | n/a | 3d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 178 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | n/a | 13d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 179 | [ ] | Rustler - Grand Theft Horse (EPIC) | 11 | 20 | 55% (last 20) | Does not open (50%) | 25% | today | 18% |  |
| 180 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 50% | 12d ago | n/a |  |
| 181 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | n/a | 19d ago | n/a |  |
| 182 | [ ] | Delver (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 11% | today | 6% |  |

## Fix shipped, waiting for ratings (16)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | Max Payne 3 (STEAM) | 2026-11-04 | 5 | 5 | 1d ago | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 2 | Peggle Deluxe (STEAM) | 2026-10-29 | 7 | 3 | 1d ago | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 3 | Red Dead Redemption (STEAM) | 2026-11-04 | 2 | 2 | 8d ago | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 4 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 8 | 8 | 5d ago | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 5 | Transistor (STEAM) | 2026-11-10 | 8 | 4 | 5d ago | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 6 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 4 | 4 | 3d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 7 | Watch_Dogs (STEAM) | n/a | 4 | 4 | 1d ago | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 8 | XCOM: Enemy Unknown (STEAM) | n/a | 1 | 1 | today | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 9 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 2 | 2 | 1d ago | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 10 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 2 | 2 | 2d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 11 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 5 | 5 | 4d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 12 | Need for Speed™ (STEAM) | 2026-11-04 | 2 | 2 | 1d ago | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 13 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 2 | 2 | 3d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 14 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 20d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 15 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 2 | 2 | 2d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 16 | Assassin's Creed Odyssey (STEAM) | n/a | 1 | 1 | 3d ago | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |

## Works, but the first launch usually fails (296)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Half-Life (STEAM) | 82 | 118 | 69% (14d) | Does not open (61%) | 71% | today | 69% |  |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 79 | 99 | 80% (14d) | Does not open (61%) | 94% | today | 96% |  |
| 3 | [ ] | Grand Theft Auto V Legacy (STEAM) | 101 | 118 | 86% (since fix) | Does not open (87%) | 76% | today | 75% |  |
| 4 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 53 | 67 | 79% (14d) | Does not open (55%) | 83% | today | 83% |  |
| 5 | [ ] | Portal (STEAM) | 47 | 78 | 60% (14d) | Does not open (39%) | 88% | today | 88% |  |
| 6 | [ ] | Cyberpunk 2077 (STEAM) | 40 | 73 | 55% (14d) | Does not open (69%) | 72% | today | 71% |  |
| 7 | [ ] | ROB RUN (STEAM) | 40 | 54 | 74% (14d) | Does not open (88%) | 66% | today | 67% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 8 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 35 | 50 | 70% (14d) | Does not open (60%) | 63% | today | 61% |  |
| 9 | [ ] | Valheim (STEAM) | 49 | 84 | 58% (since fix) | No graphics (54%) | 81% | today | 83% |  |
| 10 | [ ] | Selaco (STEAM) | 32 | 48 | 67% (14d) | Does not open (88%) | 62% | today | 61% |  |
| 11 | [ ] | MONSTER HUNTER RISE (STEAM) | 28 | 53 | 53% (14d) | Does not open (83%) | 61% | today | 62% |  |
| 12 | [ ] | No Man's Sky (STEAM) | 39 | 75 | 52% (since fix) | Controller issues (60%) | 79% | today | 77% |  |
| 13 | [ ] | Probably Stolen (STEAM) | 25 | 42 | 60% (14d) | Does not open (63%) | 85% | today | 81% |  |
| 14 | [ ] | Euro Truck Simulator 2 (STEAM) | 21 | 39 | 54% (14d) | Does not open (65%) | 60% | today | 59% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 15 | [ ] | ELDEN RING (STEAM) | 19 | 31 | 61% (14d) | Does not open (85%) | 65% | 1d ago | 65% |  |
| 16 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 19 | 20 | 95% (14d) | Does not open (37%) | 91% | today | 89% |  |
| 17 | [ ] | BeamNG.drive (STEAM) | 18 | 25 | 72% (14d) | Does not open (76%) | 64% | today | 59% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 18 | [ ] | Baldur's Gate 3 (STEAM) | 17 | 27 | 63% (14d) | Does not open (68%) | 83% | today | 83% |  |
| 19 | [ ] | Overcooked! 2 (EPIC) | 17 | 21 | 81% (14d) | Does not open (92%) | 60% | 3d ago | 57% |  |
| 20 | [ ] | Red Dead Redemption 2 (STEAM) | 25 | 29 | 86% (since fix) | Does not open (97%) | 87% | today | 88% |  |
| 21 | [ ] | Resident Evil 4 (2005) (STEAM) | 16 | 23 | 70% (14d) | Does not open (79%) | 73% | today | 72% |  |
| 22 | [ ] | Fallout: New Vegas PCR (STEAM) | 17 | 20 | 85% (last 20) | Does not open (93%) | 67% | 3d ago | 63% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 23 | [ ] | Team Fortress 2 (STEAM) | 15 | 26 | 58% (14d) | Does not open (67%) | 76% | 1d ago | 75% |  |
| 24 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 15 | 28 | 54% (14d) | Does not open (74%) | 71% | 1d ago | 71% |  |
| 25 | [ ] | Dead Space (STEAM) | 17 | 20 | 85% (last 20) | Does not open (64%) | 77% | today | 76% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 26 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 17 | 20 | 85% (last 20) | Does not open (77%) | 61% | 1d ago | 63% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 27 | [ ] | Grand Theft Auto: Vice City (STEAM) | 16 | 20 | 80% (last 20) | Does not open (36%) | 81% | today | 81% |  |
| 28 | [ ] | Dying Light (STEAM) | 13 | 26 | 50% (14d) | Does not open (81%) | 82% | today | 80% |  |
| 29 | [ ] | Fallout 3: Game of the Year Edition (GOG) | 13 | 26 | 50% (14d) | Does not open (49%) | 74% | today | 75% |  |
| 30 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 13 | 23 | 57% (14d) | Controller issues (53%) | 68% | today | 63% |  |
| 31 | [ ] | Grand Theft Auto V (EPIC) | 19 | 20 | 95% (last 20) | Does not open (88%) | 76% | today | 76% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 32 | [ ] | Tales of ARISE (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (73%) | 84% | today | 83% |  |
| 33 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | 89% | 2d ago | 88% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 34 | [ ] | Library Of Ruina (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 87% | 1d ago | 87% |  |
| 35 | [ ] | Alabaster Dawn (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (47%) | 89% | today | 89% |  |
| 36 | [ ] | Clair Obscur: Expedition 33 (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (41%) | 77% | 1d ago | 74% |  |
| 37 | [ ] | RimWorld (STEAM) | 12 | 23 | 52% (14d) | Does not open (49%) | 78% | today | 76% |  |
| 38 | [ ] | Quake (STEAM) | 13 | 20 | 65% (last 20) | Does not open (56%) | 67% | today | 59% |  |
| 39 | [ ] | Cry of Fear (STEAM) | 14 | 20 | 70% (last 20) | Does not open (47%) | 69% | 1d ago | 70% |  |
| 40 | [ ] | Pathogenic (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 66% | 1d ago | 63% |  |
| 41 | [ ] | Loftia (STEAM) | 13 | 20 | 65% (last 20) | Does not open (94%) | 64% | today | 65% |  |
| 42 | [ ] | Deadlock (STEAM) | 15 | 20 | 75% (last 20) | Does not open (51%) | 83% | 3d ago | 83% |  |
| 43 | [ ] | Core Keeper (STEAM) | 11 | 22 | 50% (14d) | Does not open (60%) | 82% | today | 80% |  |
| 44 | [ ] | Noita (STEAM) | 11 | 21 | 52% (14d) | Does not open (59%) | 77% | today | 77% |  |
| 45 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (90%) | 88% | 4d ago | 88% |  |
| 46 | [ ] | Monster Hunter: World (STEAM) | 11 | 20 | 55% (last 20) | Does not open (54%) | 78% | today | 76% |  |
| 47 | [ ] | Look Outside (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (65%) | 89% | 1d ago | 90% |  |
| 48 | [ ] | Mass Effect™ Legendary Edition (STEAM) | 15 | 28 | 54% (since fix) | Does not open (84%) | 82% | today | 82% |  |
| 49 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 14 | 26 | 54% (since fix) | Controller issues (79%) | 73% | today | 75% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 50 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (59%) | 92% | today | 92% |  |
| 51 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 17 | 20 | 85% (last 20) | Does not open (85%) | 70% | today | 70% |  |
| 52 | [ ] | Dressmaker (STEAM) | 13 | 20 | 65% (last 20) | Does not open (56%) | 76% | 2d ago | 73% |  |
| 53 | [ ] | Welcome to Elderfield (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 68% | 1d ago | 72% |  |
| 54 | [ ] | OMORI (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 64% | today | 60% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 55 | [ ] | DOOM 3: BFG Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (73%) | 68% | 3d ago | 68% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 56 | [ ] | Mortal Kombat X (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 90% | 7d ago | 93% |  |
| 57 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (68%) | 100% | today | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 58 | [ ] | Aniimo (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 75% | 1d ago | 72% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 59 | [ ] | Shakedown: Hawaii (STEAM) | 10 | 20 | 50% (last 20) | Does not open (79%) | 80% | today | 77% |  |
| 60 | [ ] | Batman™: Arkham Origins (STEAM) | 14 | 20 | 70% (last 20) | Does not open (85%) | 69% | today | 65% |  |
| 61 | [ ] | Barony (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 80% | 1d ago | 78% |  |
| 62 | [ ] | Resident Evil 7 Biohazard (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 65% | 1d ago | 60% |  |
| 63 | [ ] | Chained Echoes (GOG) | 15 | 20 | 75% (last 20) | Does not open (62%) | 67% | today | 62% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 64 | [ ] | Disco Elysium - The Final Cut (EPIC) | 12 | 20 | 60% (last 20) | Does not open (75%) | 92% | 1d ago | 91% |  |
| 65 | [ ] | Crypt of the NecroDancer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (45%) | 90% | 3d ago | 90% |  |
| 66 | [ ] | Fallout: New Vegas (EPIC) | 16 | 20 | 80% (last 20) | Does not open (60%) | 73% | 4d ago | 71% |  |
| 67 | [ ] | Rune Factory 3 Special (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 100% | 2d ago | 100% |  |
| 68 | [ ] | Don't Starve Together (STEAM) | 10 | 20 | 50% (last 20) | Does not open (63%) | 73% | today | 69% |  |
| 69 | [ ] | Divinity: Original Sin 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 79% | today | 77% |  |
| 70 | [ ] | Devil May Cry 5 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (81%) | 84% | today | 82% |  |
| 71 | [ ] | Fate/stay night REMASTERED (STEAM) | 13 | 20 | 65% (last 20) | No graphics (48%) | 94% | today | 95% |  |
| 72 | [ ] | Disgaea 5 Complete (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | 93% | 8d ago | 96% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 73 | [ ] | FINAL FANTASY (STEAM) | 12 | 20 | 60% (last 20) | Does not open (78%) | 77% | 2d ago | 74% |  |
| 74 | [ ] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 12 | 20 | 60% (last 20) | Does not open (59%) | 83% | 2d ago | 84% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 75 | [ ] | LEGO® MARVEL Super Heroes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (65%) | 84% | 1d ago | 85% |  |
| 76 | [ ] | Stardew Valley (GOG) | 10 | 20 | 50% (last 20) | Controller issues (60%) | 86% | 2d ago | 83% |  |
| 77 | [ ] | Cave Story+ (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | 76% | 3d ago | 77% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 78 | [ ] | Mortal Kombat 11 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (68%) | 60% | today | 68% |  |
| 79 | [ ] | Mini Motorways (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 70% | 2d ago | 64% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 80 | [ ] | POSTAL 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | 64% | today | 60% |  |
| 81 | [ ] | Little Witch in the Woods (STEAM) | 11 | 20 | 55% (last 20) | Does not open (55%) | 85% | 2d ago | 84% |  |
| 82 | [ ] | Castlevania Dominus Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (91%) | 96% | 3d ago | 95% |  |
| 83 | [ ] | Cyberpunk 2077 (GOG) | 10 | 20 | 50% (last 20) | Does not open (69%) | 70% | today | 69% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 84 | [ ] | Palia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | 73% | 2d ago | 70% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 85 | [ ] | eFootball™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 61% | 7d ago | 58% |  |
| 86 | [ ] | Poppy Playtime (STEAM) | 13 | 20 | 65% (last 20) | Does not open (53%) | 66% | 1d ago | 63% |  |
| 87 | [ ] | PAC-MAN Championship Edition DX+ (STEAM) | 10 | 20 | 50% (last 20) | No graphics (59%) | 64% | 4d ago | 58% |  |
| 88 | [ ] | Minecraft Dungeons II (STEAM) | 15 | 20 | 75% (last 20) | Does not open (80%) | 71% | 1d ago | 69% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 89 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (52%) | 84% | 4d ago | 82% |  |
| 90 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 15 | 20 | 75% (last 20) | Does not open (45%) | 67% | today | 83% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 91 | [ ] | Age of Empires II (2013) (STEAM) | 14 | 20 | 70% (last 20) | Does not open (59%) | 70% | 1d ago | 73% |  |
| 92 | [ ] | Doki Doki Literature Club (STEAM) | 10 | 20 | 50% (last 20) | Does not open (52%) | 83% | 1d ago | 81% |  |
| 93 | [ ] | L.A. Noire (STEAM) | 17 | 20 | 85% (last 20) | Does not open (96%) | 60% | today | 59% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 94 | [ ] | Dota 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 76% | today | 78% |  |
| 95 | [ ] | Call of Duty 4: Modern Warfare (2007) (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (50%) | 65% | 4d ago | 62% |  |
| 96 | [ ] | TBH: Task Bar Hero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 83% | 2d ago | 86% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 97 | [ ] | Titanfall® 2 (STEAM) | 9 | 13 | 69% (since fix) | Does not open (89%) | 69% | today | 69% |  |
| 98 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (82%) | 73% | 8d ago | 73% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 99 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (76%) | 80% | 7d ago | 75% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 100 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 97% | 6d ago | 96% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 101 | [ ] | Ratatan (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | 89% | 4d ago | 86% |  |
| 102 | [ ] | Resident Evil Village (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 83% | 2d ago | 83% |  |
| 103 | [ ] | SONIC X SHADOW GENERATIONS (STEAM) | 10 | 20 | 50% (last 20) | Does not open (79%) | 79% | 1d ago | 79% |  |
| 104 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 100% | 2d ago | 100% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 105 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 16 | 20 | 80% (last 20) | Does not open (67%) | 82% | today | 80% |  |
| 106 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (42%) | 71% | 1d ago | 73% |  |
| 107 | [ ] | Tails of Iron (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 87% | 3d ago | 91% |  |
| 108 | [ ] | Oxygen Not Included (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 70% | today | 75% |  |
| 109 | [ ] | The Sims™ 4 (STEAM) | 7 | 14 | 50% (since fix) | Does not open (85%) | 69% | 1d ago | 68% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 110 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 17 | 20 | 85% (last 20) | Controller issues (88%) | 98% | 1d ago | 97% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 111 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (44%) | 89% | 2d ago | 91% |  |
| 112 | [ ] | Call of Duty: Black Ops II - Zombies (STEAM) | 5 | 10 | 50% (since fix) | Does not open (72%) | 60% | today | 62% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 113 | [ ] | Moonstone Island (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (70%) | 80% | today | 78% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 114 | [ ] | Unturned (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 81% | 1d ago | 82% |  |
| 115 | [ ] | Astral Party  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 83% | 5d ago | 80% |  |
| 116 | [ ] | Minecraft Dungeons (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 76% | 4d ago | 76% |  |
| 117 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 89% | 6d ago | 83% |  |
| 118 | [ ] | Call of Duty: World at War (STEAM) | 13 | 20 | 65% (last 20) | Does not open (38%) | 74% | 3d ago | 67% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 119 | [ ] | Fable - The Lost Chapters (STEAM) | 11 | 20 | 55% (last 20) | Graphics glitches (48%) | 82% | today | 86% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 120 | [ ] | MIO: Memories in Orbit (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (61%) | 94% | 2d ago | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 121 | [ ] | Abiotic Factor (STEAM) | 10 | 20 | 50% (last 20) | Does not open (76%) | 82% | 8d ago | 85% |  |
| 122 | [ ] | Last Epoch (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | 62% | today | 64% |  |
| 123 | [ ] | A Plague Tale: Innocence (STEAM) | 19 | 20 | 95% (last 20) | Does not open (85%) | 70% | 9d ago | 70% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 124 | [ ] | Sid Meier's Civilization V (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | 65% | 5d ago | 59% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 125 | [ ] | Need for Speed™ Rivals (STEAM) | 10 | 20 | 50% (last 20) | Does not open (55%) | 74% | 2d ago | 75% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 126 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (84%) | 60% | 4d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 127 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (87%) | 76% | 18d ago | 86% |  |
| 128 | [ ] | Caravan SandWitch (EPIC) | 10 | 20 | 50% (last 20) | Does not open (70%) | 63% | 3d ago | 65% |  |
| 129 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | 83% | 16d ago | 83% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 130 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | 88% | 11d ago | 88% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 131 | [ ] | Blood Omen: Legacy of Kain (GOG) | 16 | 20 | 80% (last 20) | No graphics (57%) | 64% | 6d ago | 64% | [#539](https://github.com/GameNative/gamenative-compat/issues/539) |
| 132 | [ ] | Ultimate Custom Night (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | 64% | 2d ago | 58% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 133 | [ ] | PlateUp! (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 76% | 5d ago | 74% |  |
| 134 | [ ] | Watch Dogs 2 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (80%) | 65% | 1d ago | 62% | [#399](https://github.com/GameNative/gamenative-compat/issues/399) |
| 135 | [ ] | Sonic Generations (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 68% | 1d ago | 65% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 136 | [ ] | Gothic 1 Classic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (58%) | 64% | 1d ago | 65% |  |
| 137 | [ ] | Digimon Survive (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (79%) | 88% | today | 87% |  |
| 138 | [ ] | Legacy of Kain: Defiance Remastered (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (69%) | 80% | 3d ago | n/a |  |
| 139 | [ ] | Street Fighter™ 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | 80% | 3d ago | 78% |  |
| 140 | [ ] | OCTOPATH TRAVELER 0 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (77%) | 90% | today | 92% |  |
| 141 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (87%) | 85% | 7d ago | 89% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 142 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (70%) | 86% | 2d ago | 85% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 143 | [ ] | Stellar Blade™ (STEAM) | 14 | 20 | 70% (last 20) | No graphics (42%) | 83% | 4d ago | 83% |  |
| 144 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 94% | 1d ago | 93% |  |
| 145 | [ ] | Yakuza: Like a Dragon (STEAM) | 13 | 20 | 65% (last 20) | Does not open (60%) | 70% | 2d ago | 74% |  |
| 146 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (79%) | 73% | 2d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 147 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (80%) | 81% | 1d ago | 82% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 148 | [ ] | Supermarket Together (STEAM) | 16 | 20 | 80% (last 20) | Does not open (67%) | 62% | today | 63% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 149 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 66% | 14d ago | 69% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 150 | [ ] | Tabletop Simulator (STEAM) | 14 | 20 | 70% (last 20) | Does not open (42%) | 76% | 6d ago | 79% |  |
| 151 | [ ] | Max Payne (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (48%) | 82% | 1d ago | 80% |  |
| 152 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (83%) | 60% | 15d ago | n/a |  |
| 153 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 77% | 1d ago | 76% |  |
| 154 | [ ] | Pinball FX (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 67% | 8d ago | 61% |  |
| 155 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | 86% | 12d ago | 83% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 156 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 86% | 18d ago | 88% |  |
| 157 | [ ] | Plague Inc: Evolved (STEAM) | 13 | 20 | 65% (last 20) | Does not open (57%) | 67% | 4d ago | 65% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 158 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (66%) | 77% | 1d ago | 73% |  |
| 159 | [ ] | Trailmakers (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | 93% | 4d ago | 93% |  |
| 160 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 88% | today | 89% |  |
| 161 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (52%) | 74% | today | 76% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 162 | [ ] | Control Ultimate Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (72%) | 67% | today | 63% |  |
| 163 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | No graphics (47%) | 86% | 2d ago | 87% |  |
| 164 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (59%) | 92% | 3d ago | 90% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 165 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (92%) | 67% | 5d ago | 77% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 166 | [ ] | Necesse (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 62% | 3d ago | 63% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 167 | [ ] | Gambonanza (STEAM) | 13 | 20 | 65% (last 20) | Does not open (61%) | 87% | today | 87% |  |
| 168 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 62% | 1d ago | 61% |  |
| 169 | [ ] | SurrounDead (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (70%) | 90% | today | 92% |  |
| 170 | [ ] | Sonic Lost World (STEAM) | 10 | 20 | 50% (last 20) | No graphics (69%) | 82% | 4d ago | 82% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 171 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (46%) | 78% | today | 75% |  |
| 172 | [ ] | Heavy Rain (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (65%) | 90% | 1d ago | 92% |  |
| 173 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 67% | 13d ago | 67% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 174 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (42%) | 67% | today | 66% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 175 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (82%) | 87% | 6d ago | 89% |  |
| 176 | [ ] | Grim Dawn (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 60% | 1d ago | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 177 | [ ] | My Summer Car (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 71% | 1d ago | 67% |  |
| 178 | [ ] | One-armed robber (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (71%) | 68% | today | 62% |  |
| 179 | [ ] | Dishonored 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 64% | 5d ago | 61% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 180 | [ ] | Raft (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | 93% | 3d ago | 91% |  |
| 181 | [ ] | Overwatch® (STEAM) | 8 | 11 | 73% (since fix) | Does not open (61%) | 83% | 2d ago | 81% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 182 | [ ] | Changed (STEAM) | 15 | 20 | 75% (last 20) | Does not open (62%) | 62% | 12d ago | 60% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 183 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 90% | 35d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 184 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | 83% | 2d ago | 80% |  |
| 185 | [ ] | HELLDIVERS™ (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 64% | today | 62% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 186 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (67%) | 93% | today | 95% |  |
| 187 | [ ] | Warframe (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 80% | 1d ago | 79% |  |
| 188 | [ ] | TurretGirls (STEAM) | 12 | 20 | 60% (last 20) | No graphics (77%) | 100% | 5d ago | 100% |  |
| 189 | [ ] | METAL SLUG 3 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (81%) | 63% | 1d ago | 65% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 190 | [ ] | Limbus Company (STEAM) | 11 | 20 | 55% (last 20) | Does not open (82%) | 94% | today | 95% |  |
| 191 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (44%) | 75% | 6d ago | 74% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 192 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | 64% | 14d ago | 62% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 193 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (71%) | 85% | 7d ago | 83% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 194 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (75%) | 68% | 8d ago | 65% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 195 | [ ] | Capcom Arcade Stadium (STEAM) | 15 | 20 | 75% (last 20) | Does not open (78%) | 77% | 12d ago | 80% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 196 | [ ] | Hylics (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (74%) | 90% | 2d ago | 87% |  |
| 197 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (76%) | 100% | 15d ago | n/a |  |
| 198 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 75% | 3d ago | 71% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 199 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (59%) | 71% | 3d ago | 75% |  |
| 200 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 95% | 14d ago | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 201 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 76% | 19d ago | 64% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 202 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (65%) | 80% | 2d ago | 73% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 203 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | 79% | 1d ago | 90% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 204 | [ ] | Return to Monkey Island (STEAM) | 15 | 20 | 75% (last 20) | No graphics (74%) | 72% | 1d ago | 72% |  |
| 205 | [ ] | Subnautica 2 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (44%) | 73% | today | 82% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 206 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 13 | 20 | 65% (last 20) | Does not open (81%) | 63% | today | 61% |  |
| 207 | [ ] | Turbo Overkill (STEAM) | 13 | 20 | 65% (last 20) | No graphics (91%) | 100% | 3d ago | 100% |  |
| 208 | [ ] | Escape from Duckov (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (68%) | 96% | today | 96% |  |
| 209 | [ ] | Moonring (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | 81% | 5d ago | 77% |  |
| 210 | [ ] | Maneater (STEAM) | 15 | 20 | 75% (last 20) | Does not open (86%) | 61% | today | 64% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 211 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (61%) | 79% | 14d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 212 | [ ] | Resident Evil Revelations 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (55%) | 82% | 2d ago | 84% |  |
| 213 | [ ] | POSTAL: Brain Damaged (STEAM) | 16 | 20 | 80% (last 20) | Does not open (91%) | 80% | 1d ago | n/a |  |
| 214 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (91%) | 80% | 38d ago | 73% |  |
| 215 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 75% | 28d ago | 75% |  |
| 216 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Graphics glitches (53%) | 71% | 1d ago | 70% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 217 | [ ] | Hotline Miami (GOG) | 13 | 20 | 65% (last 20) | Does not open (88%) | 68% | 1d ago | 71% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 218 | [ ] | GOD EATER RESURRECTION (STEAM) | 13 | 20 | 65% (last 20) | Does not open (56%) | 87% | 1d ago | 90% |  |
| 219 | [ ] | CS2D (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 64% | 2d ago | n/a |  |
| 220 | [ ] | MX Bikes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 96% | 7d ago | 95% |  |
| 221 | [ ] | Invisible, Inc. (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 92% | 2d ago | n/a |  |
| 222 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (73%) | 64% | 16d ago | 69% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 223 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 92% | 15d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 224 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (82%) | 81% | 8d ago | 82% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 225 | [ ] | Big Walk (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 62% | 5d ago | 58% |  |
| 226 | [ ] | Darksiders (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 81% | 2d ago | 81% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 227 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 94% | 1d ago | 100% |  |
| 228 | [ ] | GUILTY GEAR Xrd REV 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (83%) | 66% | 10d ago | 61% |  |
| 229 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (64%) | 78% | 13d ago | 78% |  |
| 230 | [ ] | No Socks RPG (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (91%) | 93% | 3d ago | 93% |  |
| 231 | [ ] | Capcom Fighting Collection (STEAM) | 13 | 20 | 65% (last 20) | Does not open (85%) | 89% | 5d ago | 88% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 232 | [ ] | SnowRunner (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 71% | 2d ago | 73% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 233 | [ ] | BATTLETECH (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 96% | 9d ago | 95% |  |
| 234 | [ ] | Donut Dodo (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 94% | today | 100% |  |
| 235 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (50%) | 88% | 4d ago | 93% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 236 | [ ] | Secrets of Grindea (STEAM) | 10 | 20 | 50% (last 20) | Does not open (48%) | 80% | 7d ago | 82% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 237 | [ ] | Zero Escape: The Nonary Games (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 69% | 4d ago | 70% |  |
| 238 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 77% | today | 76% |  |
| 239 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 77% | 2d ago | 77% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 240 | [ ] | HITMAN World of Assassination (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 71% | today | 70% |  |
| 241 | [ ] | Spark the Electric Jester (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 73% | 4d ago | n/a | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 242 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (82%) | 60% | 5d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 243 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 94% | 16d ago | 94% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 244 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 76% | today | 73% |  |
| 245 | [ ] | AER Memories of Old (EPIC) | 13 | 20 | 65% (last 20) | Does not open (86%) | 93% | 9d ago | 93% |  |
| 246 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (71%) | 62% | 10d ago | 67% |  |
| 247 | [ ] | Tales of Zestiria (STEAM) | 13 | 20 | 65% (last 20) | Does not open (77%) | 73% | 2d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 248 | [ ] | SILENT HILL 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 100% | 1d ago | 100% |  |
| 249 | [ ] | Timberborn (STEAM) | 12 | 20 | 60% (last 20) | No graphics (68%) | 100% | 6d ago | 100% |  |
| 250 | [ ] | Mafia II (Classic) (GOG) | 12 | 20 | 60% (last 20) | Does not open (100%) | 70% | 2d ago | 70% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 251 | [ ] | Sacred Gold (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | 70% | 6d ago | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 252 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 94% | 17d ago | 92% |  |
| 253 | [ ] | Deus Ex™ GOTY Edition (GOG) | 11 | 20 | 55% (last 20) | No graphics (47%) | 100% | 3d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 254 | [ ] | Super Battle Golf (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 88% | 2d ago | 87% |  |
| 255 | [ ] | Football Manager 2024 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (91%) | 61% | today | 50% |  |
| 256 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 83% | 11d ago | 79% |  |
| 257 | [ ] | Rollout Inline (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 77% | 5d ago | 75% |  |
| 258 | [ ] | Vampyr (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 100% | today | 100% |  |
| 259 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 90% | 1d ago | 88% |  |
| 260 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 92% | 36d ago | 92% |  |
| 261 | [ ] | Goose Goose Duck (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 76% | 5d ago | 81% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 262 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 12 | 20 | 60% (last 20) | No graphics (39%) | 86% | 8d ago | 90% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 263 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 67% | 12d ago | 69% |  |
| 264 | [ ] | Disgaea 4 Complete+ (STEAM) | 12 | 20 | 60% (last 20) | No graphics (40%) | 93% | 2d ago | 92% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 265 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 70% | 16d ago | 73% |  |
| 266 | [ ] | Sons Of The Forest (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 76% | 10d ago | 73% |  |
| 267 | [ ] | Forgive Me Father (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 69% | 1d ago | 58% |  |
| 268 | [ ] | 12 is Better Than 6 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (40%) | 77% | today | 80% |  |
| 269 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 92% | 13d ago | 91% |  |
| 270 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 71% | 9d ago | 83% |  |
| 271 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 88% | 7d ago | 88% |  |
| 272 | [ ] | Hitman: Contracts (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (82%) | 69% | 2d ago | 67% |  |
| 273 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (100%) | 93% | today | 92% |  |
| 274 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 87% | 2d ago | 85% |  |
| 275 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (40%) | 60% | 13d ago | 82% |  |
| 276 | [ ] | Cat Mail Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 91% | 1d ago | 90% |  |
| 277 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 84% | 1d ago | 81% |  |
| 278 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 71% | 6d ago | 77% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 279 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 75% | 10d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 280 | [ ] | CRUEL (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 85% | 10d ago | 84% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 281 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 94% | 10d ago | 100% |  |
| 282 | [ ] | Eastern Exorcist (EPIC) | 10 | 20 | 50% (last 20) | No graphics (50%) | 71% | today | 60% |  |
| 283 | [ ] | Assetto Corsa Competizione (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 87% | 2d ago | 86% |  |
| 284 | [ ] | Sort Them Ducks (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (64%) | 100% | 2d ago | 100% |  |
| 285 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 75% | 9d ago | 75% |  |
| 286 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 64% | 8d ago | 64% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 287 | [ ] | A Plague Tale: Innocence (GOG) | 10 | 20 | 50% (last 20) | Does not open (92%) | 70% | today | n/a |  |
| 288 | [ ] | Cruelty Squad (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 83% | 1d ago | 81% |  |
| 289 | [ ] | BioShock 2 Remastered (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 79% | 5d ago | 76% |  |
| 290 | [ ] | Dungeon Siege (STEAM) | 10 | 20 | 50% (last 20) | No graphics (50%) | 100% | 4d ago | 100% |  |
| 291 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | No graphics (64%) | 100% | 27d ago | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 292 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 62% | 18d ago | 60% |  |
| 293 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 93% | 4d ago | 92% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 294 | [ ] | Command & Conquer™ Red Alert™ 3 (STEAM) | 10 | 20 | 50% (last 20) | No graphics (38%) | 93% | 3d ago | 92% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 295 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 100% | 3d ago | 100% |  |
| 296 | [ ] | Pillars of Eternity (STEAM) | 10 | 20 | 50% (last 20) | Does not open (40%) | 100% | 4d ago | 100% |  |

## Recently recovered (364)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Grim Dawn (STEAM) | 451 | 2026-11-08 | 534 | 72% |  |
| 2 | [x] | Half-Life (STEAM) | 375 | 2026-11-09 | 638 | 71% |  |
| 3 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 266 | 2026-11-14 | 425 | 72% |  |
| 4 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 243 | 2026-11-09 | 337 | 89% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 5 | [x] | MONSTER HUNTER RISE (STEAM) | 227 | 2026-11-17 | 527 | 61% |  |
| 6 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 218 | 2026-11-09 | 371 | 63% |  |
| 7 | [x] | Alan Wake (STEAM) | 211 | 2026-11-14 | 240 | 80% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 8 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 184 | 2026-11-09 | 226 | 52% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 9 | [x] | BeamNG.drive (STEAM) | 176 | 2026-11-09 | 220 | 64% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 10 | [x] | OMORI (STEAM) | 166 | 2026-11-09 | 211 | 64% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 11 | [x] | Geometry Dash (STEAM) | 161 | 2026-11-11 | 452 | 66% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 12 | [x] | DRAGON BALL FighterZ (STEAM) | 161 | 2026-11-01 | 210 | 86% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 13 | [x] | Call of Duty: Black Ops (STEAM) | 150 | 2026-11-13 | 177 | 24% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 14 | [x] | BioShock (STEAM) | 139 | 2026-11-09 | 288 | 72% |  |
| 15 | [x] | Spelunky 2 (STEAM) | 139 | 2026-11-01 | 189 | 87% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 16 | [x] | Team Fortress 2 (STEAM) | 137 | 2026-11-09 | 238 | 76% |  |
| 17 | [x] | Sid Meier's Civilization V (STEAM) | 135 | 2026-11-10 | 147 | 65% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 18 | [x] | Minecraft Dungeons II (STEAM) | 133 | 2026-11-09 | 152 | 71% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 19 | [x] | Prototype (STEAM) | 131 | 2026-11-11 | 198 | 56% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 20 | [x] | Castlevania Advance Collection (STEAM) | 126 | 2026-11-09 | 202 | 86% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 21 | [x] | Euro Truck Simulator 2 (STEAM) | 122 | 2026-11-23 | 218 | 60% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 22 | [x] | Aniimo (STEAM) | 117 | 2026-11-09 | 158 | 75% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 23 | [x] | Mirror's Edge (STEAM) | 106 | 2026-11-09 | 163 | 67% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 24 | [x] | Cave Story+ (STEAM) | 103 | 2026-11-09 | 113 | 76% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 25 | [x] | Assassin's Creed II (STEAM) | 103 | 2026-11-10 | 108 | 73% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 26 | [x] | Necesse (STEAM) | 100 | 2026-11-22 | 110 | 62% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 27 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 97 | 2026-11-09 | 137 | 90% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 28 | [x] | The Witcher: Enhanced Edition (STEAM) | 96 | 2026-11-09 | 115 | 79% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 29 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 88 | 2026-11-15 | 133 | 84% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 30 | [x] | Fallout: New Vegas PCR (STEAM) | 85 | 2026-11-20 | 113 | 67% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 31 | [x] | Moonstone Island (STEAM) | 82 | 2026-11-09 | 108 | 80% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 32 | [x] | FINAL FANTASY XIII-2 (STEAM) | 80 | 2026-11-09 | 83 | 67% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 33 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 77 | 2026-11-09 | 127 | 74% |  |
| 34 | [x] | DOOM 3: BFG Edition (STEAM) | 77 | 2026-11-09 | 120 | 68% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 35 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 77 | 2026-11-23 | 99 | 61% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 36 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 75 | 2026-11-09 | 117 | 78% |  |
| 37 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 75 | 2026-11-09 | 99 | 98% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 38 | [x] | Vital Shell (STEAM) | 73 | 2026-11-09 | 122 | 85% |  |
| 39 | [x] | Psychonauts (STEAM) | 70 | 2026-11-09 | 137 | 91% |  |
| 40 | [x] | Brawlhalla (STEAM) | 70 | 2026-11-09 | 136 | 71% |  |
| 41 | [x] | Cyberpunk 2077 (GOG) | 70 | 2026-11-09 | 95 | 70% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 42 | [x] | The Sims™ 4 (STEAM) | 70 | 2026-11-09 | 95 | 69% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 43 | [x] | Order of the Sinking Star (STEAM) | 69 | 2026-11-09 | 107 | 66% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 44 | [x] | Ballionaire (STEAM) | 67 | 2026-11-09 | 117 | 84% |  |
| 45 | [x] | Stardew Valley (GOG) | 65 | 2026-11-11 | 117 | 86% |  |
| 46 | [x] | Fable - The Lost Chapters (STEAM) | 65 | 2026-11-09 | 108 | 82% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 47 | [x] | Age of Empires II: Definitive Edition (STEAM) | 65 | 2026-11-10 | 84 | 62% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 48 | [x] | Dota 2 (STEAM) | 64 | 2026-11-09 | 99 | 76% |  |
| 49 | [x] | Grand Theft Auto V (EPIC) | 64 | 2026-11-09 | 68 | 76% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 50 | [x] | American Truck Simulator (STEAM) | 63 | 2026-11-09 | 104 | 68% |  |
| 51 | [x] | Need for Speed: Hot Pursuit (STEAM) | 63 | 2026-11-09 | 96 | 76% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 52 | [x] | Horizon Zero Dawn™ Complete Edition (STEAM) | 63 | 2026-11-25 | 76 | 67% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 53 | [x] | Diablo® IV (STEAM) | 63 | 2026-11-11 | 75 | 83% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 54 | [x] | Disgaea 5 Complete (STEAM) | 63 | 2026-11-09 | 73 | 93% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 55 | [x] | GRID (STEAM) | 62 | 2026-11-21 | 83 | 52% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 56 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 60 | 2026-11-11 | 80 | 60% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 57 | [x] | Quake (STEAM) | 59 | 2026-11-09 | 185 | 67% |  |
| 58 | [x] | Spyro™ Reignited Trilogy (STEAM) | 59 | 2026-11-09 | 107 | 78% |  |
| 59 | [x] | Mini Motorways (STEAM) | 59 | 2026-11-09 | 93 | 70% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 60 | [x] | Poppy Playtime (STEAM) | 58 | 2026-11-09 | 99 | 66% |  |
| 61 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 58 | 2026-11-09 | 96 | 89% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 62 | [x] | Borderlands 3 (STEAM) | 57 | 2026-11-09 | 87 | 93% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 63 | [x] | Gunfire Reborn (STEAM) | 57 | 2026-11-09 | 63 | 85% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 64 | [x] | FINAL FANTASY XIII (STEAM) | 54 | 2026-11-22 | 514 | 66% |  |
| 65 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 54 | 2026-11-09 | 93 | 68% |  |
| 66 | [x] | Fallout (STEAM) | 54 | 2026-11-09 | 88 | 67% |  |
| 67 | [x] | Sovereign Tower (STEAM) | 53 | 2026-11-09 | 110 | 75% |  |
| 68 | [x] | Firewatch (STEAM) | 53 | 2026-11-10 | 105 | 90% |  |
| 69 | [x] | Last Epoch (STEAM) | 53 | 2026-11-09 | 78 | 62% |  |
| 70 | [x] | Call of Duty: World at War (STEAM) | 53 | 2026-11-09 | 76 | 74% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 71 | [x] | Sonic Generations (STEAM) | 53 | 2026-11-09 | 61 | 68% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 72 | [x] | Caravan SandWitch (EPIC) | 51 | 2026-11-09 | 111 | 63% |  |
| 73 | [x] | Call of Juarez Gunslinger (STEAM) | 51 | 2026-11-09 | 64 | 66% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 74 | [x] | A Plague Tale: Innocence (STEAM) | 51 | 2026-11-09 | 54 | 70% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 75 | [x] | eFootball™ (STEAM) | 50 | 2026-11-09 | 75 | 61% |  |
| 76 | [x] | Moonlighter (EPIC) | 50 | 2026-11-09 | 54 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 77 | [x] | MIO: Memories in Orbit (STEAM) | 49 | 2026-11-09 | 102 | 94% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 78 | [x] | Starbound (STEAM) | 49 | 2026-11-09 | 82 | 90% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 79 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 49 | 2026-11-17 | 74 | 67% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 80 | [x] | Darksiders (STEAM) | 49 | 2026-11-09 | 65 | 81% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 81 | [x] | HELLDIVERS™ (STEAM) | 49 | 2026-11-23 | 61 | 64% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 82 | [x] | STEINS;GATE (STEAM) | 48 | 2026-11-09 | 77 | 82% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 83 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 48 | 2026-11-09 | 54 | 100% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 84 | [x] | Okami HD (STEAM) | 47 | 2026-11-09 | 89 | 96% |  |
| 85 | [x] | METAL SLUG 3 (STEAM) | 47 | 2026-11-24 | 61 | 63% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 86 | [x] | TBH: Task Bar Hero (STEAM) | 46 | 2026-11-09 | 72 | 83% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 87 | [x] | Oxygen Not Included (STEAM) | 45 | 2026-11-11 | 78 | 70% |  |
| 88 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 45 | 2026-11-13 | 75 | 65% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 89 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 44 | 2026-11-09 | 64 | 73% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 90 | [x] | Overwatch® (STEAM) | 44 | 2026-11-10 | 49 | 83% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 91 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 43 | 2026-11-09 | 76 | 57% |  |
| 92 | [x] | ROB RUN (STEAM) | 43 | 2026-11-17 | 60 | 66% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 93 | [x] | Sol Cesto (EPIC) | 43 | 2026-11-09 | 43 | 80% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 94 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 42 | 2026-11-09 | 77 | 85% |  |
| 95 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 40 | 2026-11-09 | 68 | 56% |  |
| 96 | [x] | Borderlands: The Pre-Sequel (STEAM) | 39 | 2026-11-09 | 78 | 63% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 97 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 39 | 2026-11-09 | 69 | 83% |  |
| 98 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 39 | 2026-11-09 | 61 | 89% |  |
| 99 | [x] | Darkest Dungeon® (EPIC) | 38 | 2026-11-09 | 78 | 90% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 100 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 38 | 2026-11-09 | 62 | 68% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 101 | [x] | Sonic Lost World (STEAM) | 38 | 2026-11-09 | 58 | 82% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 102 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 37 | 2026-11-09 | 68 | 87% |  |
| 103 | [x] | Age of Empires II (2013) (STEAM) | 37 | 2026-11-09 | 62 | 70% |  |
| 104 | [x] | Grim Dawn (GOG) | 37 | 2026-11-24 | 61 | 60% | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 105 | [x] | Aggelos (STEAM) | 37 | 2026-11-09 | 53 | 81% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 106 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 36 | 2026-11-19 | 38 | 88% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 107 | [x] | Amnesia: The Dark Descent (STEAM) | 35 | 2026-11-09 | 75 | 86% |  |
| 108 | [x] | Digimon World: Next Order (STEAM) | 35 | 2026-11-09 | 70 | 86% |  |
| 109 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 35 | 2026-11-09 | 66 | 84% |  |
| 110 | [x] | Street Fighter™ 6 (STEAM) | 35 | 2026-11-09 | 56 | 80% |  |
| 111 | [x] | L.A. Noire (STEAM) | 35 | 2026-11-24 | 43 | 60% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 112 | [x] | Russian Fishing 4 (STEAM) | 35 | 2026-11-09 | 41 | 68% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 113 | [x] | CrossCode (GOG) | 35 | 2026-11-09 | 38 | 73% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 114 | [x] | Monster Hunter Wilds (STEAM) | 35 | 2026-11-09 | 36 | 86% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 115 | [x] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 34 | 2026-11-20 | 68 | 17% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 116 | [x] | POSTAL 2 (GOG) | 34 | 2026-11-09 | 66 | 95% |  |
| 117 | [x] | Dead by Daylight (STEAM) | 34 | 2026-11-09 | 38 | 86% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 118 | [x] | Being a DIK (STEAM) | 33 | 2026-11-09 | 73 | 69% |  |
| 119 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 33 | 2026-11-09 | 60 | 77% |  |
| 120 | [x] | Sonic Origins (STEAM) | 33 | 2026-11-09 | 60 | 77% |  |
| 121 | [x] | COCOON (STEAM) | 32 | 2026-11-09 | 63 | 81% |  |
| 122 | [x] | XCOM 2 (STEAM) | 32 | 2026-11-09 | 58 | 68% |  |
| 123 | [x] | FINAL FANTASY VII (2013) (STEAM) | 32 | 2026-11-09 | 49 | 50% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 124 | [x] | SnowRunner (STEAM) | 32 | 2026-11-09 | 43 | 71% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 125 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-11-09 | 40 | 92% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 126 | [x] | Journey (STEAM) | 31 | 2026-10-27 | 71 | 80% |  |
| 127 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 31 | 2026-11-09 | 70 | 69% |  |
| 128 | [x] | Hearts of Iron IV (STEAM) | 31 | 2026-11-09 | 67 | 81% |  |
| 129 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 31 | 2026-11-09 | 63 | 88% |  |
| 130 | [x] | Ace Attorney Investigations Collection (STEAM) | 31 | 2026-11-09 | 59 | 86% |  |
| 131 | [x] | Yume Nikki (STEAM) | 31 | 2026-11-20 | 57 | 51% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 132 | [x] | Max Payne (STEAM) | 31 | 2026-11-09 | 54 | 82% |  |
| 133 | [x] | Plague Inc: Evolved (STEAM) | 31 | 2026-11-16 | 50 | 67% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 134 | [x] | Breathedge (STEAM) | 31 | 2026-11-23 | 49 | 60% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 135 | [x] | Gauntlet™  (STEAM) | 31 | 2026-11-11 | 46 | 70% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 136 | [x] | Red Dead Redemption (STEAM) | 31 | 2026-11-09 | 34 | 37% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 137 | [x] | DOOM 64 (EPIC) | 30 | 2026-11-24 | 115 | 42% |  |
| 138 | [x] | Tomb Raider: Anniversary (STEAM) | 30 | 2026-11-09 | 58 | 67% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 139 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 30 | 2026-11-09 | 54 | 71% |  |
| 140 | [x] | Earthion (STEAM) | 30 | 2026-11-09 | 53 | 100% |  |
| 141 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 30 | 2026-11-09 | 50 | 71% |  |
| 142 | [x] | Resident Evil Village (STEAM) | 30 | 2026-11-09 | 50 | 83% |  |
| 143 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 30 | 2026-11-09 | 44 | 82% |  |
| 144 | [x] | Capcom Arcade Stadium (STEAM) | 30 | 2026-11-09 | 40 | 77% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 145 | [x] | Elite Dangerous (STEAM) | 30 | 2026-11-20 | 30 | 60% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 146 | [x] | SurrounDead (STEAM) | 29 | 2026-11-09 | 60 | 90% |  |
| 147 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 29 | 2026-11-09 | 52 | 83% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 148 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 29 | 2026-11-09 | 50 | 100% |  |
| 149 | [x] | Need for Speed™ Rivals (STEAM) | 29 | 2026-11-10 | 43 | 74% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 150 | [x] | Digimon Survive (STEAM) | 29 | 2026-11-09 | 42 | 88% |  |
| 151 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 74% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 152 | [x] | Hero Siege (STEAM) | 28 | 2026-11-09 | 49 | 84% |  |
| 153 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 28 | 2026-11-09 | 49 | 93% |  |
| 154 | [x] | Prince of Persia: The Sands of Time (STEAM) | 28 | 2026-11-09 | 49 | 78% |  |
| 155 | [x] | Big Walk (STEAM) | 28 | 2026-11-09 | 47 | 62% |  |
| 156 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 28 | 2026-11-09 | 45 | 69% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 157 | [x] | Supermarket Together (STEAM) | 28 | 2026-11-18 | 39 | 62% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 158 | [x] | The Bazaar (STEAM) | 27 | 2026-11-09 | 54 | 81% |  |
| 159 | [x] | Resident Evil Revelations 2 (STEAM) | 27 | 2026-11-09 | 53 | 82% |  |
| 160 | [x] | Heavy Rain (STEAM) | 27 | 2026-11-09 | 48 | 90% |  |
| 161 | [x] | Secrets of Grindea (STEAM) | 27 | 2026-11-09 | 46 | 80% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 162 | [x] | Tower and Sword of Succubus (STEAM) | 27 | 2026-11-09 | 41 | 80% |  |
| 163 | [x] | Palia (STEAM) | 27 | 2026-11-09 | 38 | 73% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 164 | [x] | Hotline Miami (GOG) | 27 | 2026-11-18 | 35 | 68% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 165 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 43 | 69% |  |
| 166 | [x] | Yakuza: Like a Dragon (STEAM) | 26 | 2026-11-09 | 42 | 70% |  |
| 167 | [x] | Dead Rising 2 (STEAM) | 25 | 2026-11-09 | 41 | 76% |  |
| 168 | [x] | Mortal Kombat 11 (STEAM) | 25 | 2026-11-09 | 36 | 60% |  |
| 169 | [x] | Gothic II: Gold Classic (STEAM) | 25 | 2026-11-09 | 33 | 75% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 170 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-19 | 32 | 90% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 171 | [x] | Skullgirls 2nd Encore (STEAM) | 24 | 2026-11-10 | 61 | 71% |  |
| 172 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 24 | 2026-11-09 | 58 | 83% |  |
| 173 | [x] | Frostpunk (STEAM) | 24 | 2026-11-09 | 51 | 83% |  |
| 174 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 24 | 2026-11-09 | 48 | 56% |  |
| 175 | [x] | Deponia (STEAM) | 24 | 2026-11-09 | 47 | 84% |  |
| 176 | [x] | Lobotomy Corporation (STEAM) | 24 | 2026-11-09 | 47 | 92% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 177 | [x] | Mirror's Edge™ (GOG) | 24 | 2026-11-13 | 46 | 75% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 178 | [x] | Cat Mail Co. (STEAM) | 24 | 2026-11-09 | 42 | 91% |  |
| 179 | [x] | Trailmakers (STEAM) | 24 | 2026-11-09 | 41 | 93% |  |
| 180 | [x] | My Summer Car (STEAM) | 24 | 2026-11-09 | 38 | 71% |  |
| 181 | [x] | Ratatan (STEAM) | 24 | 2026-11-09 | 37 | 89% |  |
| 182 | [x] | Chained Echoes (GOG) | 23 | 2026-11-19 | 48 | 67% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 183 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 43 | 92% |  |
| 184 | [x] | Unturned (STEAM) | 23 | 2026-11-09 | 41 | 81% |  |
| 185 | [x] | Football Manager 2024 (EPIC) | 23 | 2026-11-09 | 40 | 61% |  |
| 186 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 2026-11-09 | 38 | 84% |  |
| 187 | [x] | Opus Magnum (STEAM) | 23 | 2026-11-09 | 36 | 100% |  |
| 188 | [x] | Ultimate Custom Night (STEAM) | 23 | 2026-11-19 | 33 | 64% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 189 | [x] | Crab Game (STEAM) | 23 | 2026-11-09 | 27 | 64% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 190 | [x] | Gambonanza (STEAM) | 22 | 2026-11-09 | 39 | 87% |  |
| 191 | [x] | Control Ultimate Edition (GOG) | 22 | 2026-11-09 | 38 | 67% |  |
| 192 | [x] | Titanfall® 2 (STEAM) | 22 | 2026-11-09 | 38 | 69% |  |
| 193 | [x] | Dishonored 2 (STEAM) | 22 | 2026-11-09 | 33 | 64% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 194 | [x] | Changed (STEAM) | 22 | 2026-11-23 | 32 | 62% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 195 | [x] | Jade Empire: Special Edition (GOG) | 22 | 2026-11-09 | 29 | 71% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 196 | [x] | Tearscape (STEAM) | 22 | 2026-11-09 | 26 | 80% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 197 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 22 | 2026-11-09 | 25 | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 198 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 58 | 97% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 199 | [x] | Battle Brothers (STEAM) | 21 | 2026-11-09 | 41 | 79% |  |
| 200 | [x] | Strider (STEAM) | 21 | 2026-11-20 | 37 | 71% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 201 | [x] | Limbus Company (STEAM) | 21 | 2026-11-09 | 35 | 94% |  |
| 202 | [x] | Return to Monkey Island (STEAM) | 21 | 2026-11-09 | 33 | 72% |  |
| 203 | [x] | Timberborn (STEAM) | 21 | 2026-11-09 | 32 | 100% |  |
| 204 | [x] | Goose Goose Duck (STEAM) | 21 | 2026-11-18 | 30 | 76% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 205 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 83% |  |
| 206 | [x] | Prince of Persia (GOG) | 20 | 2026-11-09 | 41 | 74% |  |
| 207 | [x] | Capcom Fighting Collection 2 (STEAM) | 20 | 2026-11-09 | 36 | 86% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 208 | [x] | One-armed robber (STEAM) | 20 | 2026-11-09 | 36 | 68% |  |
| 209 | [x] | GOD EATER RESURRECTION (STEAM) | 20 | 2026-11-09 | 32 | 87% |  |
| 210 | [x] | Deus Ex™ GOTY Edition (GOG) | 20 | 2026-11-09 | 31 | 100% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 211 | [x] | Maneater (STEAM) | 20 | 2026-11-25 | 31 | 61% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 212 | [x] | CRUEL (STEAM) | 20 | 2026-11-09 | 30 | 85% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 213 | [x] | Subnautica 2 (STEAM) | 20 | 2026-11-15 | 27 | 73% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 214 | [x] | Blood Omen: Legacy of Kain (GOG) | 20 | 2026-11-25 | 26 | 64% | [#539](https://github.com/GameNative/gamenative-compat/issues/539) |
| 215 | [x] | Dead Island (STEAM) | 20 | 2026-11-09 | 23 | 85% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 216 | [x] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 20 | 2026-11-22 | 21 | 67% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 217 | [x] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 2026-11-15 | 38 | 77% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 218 | [x] | Pinball FX Classic (STEAM) | 19 | 2026-11-09 | 37 | 88% |  |
| 219 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 32 | 100% |  |
| 220 | [x] | Invisible, Inc. (STEAM) | 19 | 2026-11-09 | 31 | 92% |  |
| 221 | [x] | Torchlight II (EPIC) | 19 | 2026-11-09 | 27 | 81% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 222 | [x] | Sapphire Safari (GOG) | 19 | 2026-11-24 | 26 | 60% | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 223 | [x] | Dark Sector (STEAM) | 19 | 2026-11-21 | 25 | 79% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 224 | [x] | CarX Street (STEAM) | 19 | 2026-11-09 | 23 | 76% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 225 | [x] | Crusader Kings III (STEAM) | 19 | 2026-11-18 | 23 | 79% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 226 | [x] | Watch Dogs 2 (EPIC) | 19 | 2026-11-23 | 21 | 65% | [#399](https://github.com/GameNative/gamenative-compat/issues/399) |
| 227 | [x] | Wizard of Legend (EPIC) | 18 | 2026-11-09 | 37 | 74% |  |
| 228 | [x] | Mini Metro (STEAM) | 18 | 2026-11-16 | 35 | 56% |  |
| 229 | [x] | Worms W.M.D (STEAM) | 18 | 2026-11-09 | 34 | 96% |  |
| 230 | [x] | Guildrun Demo (STEAM) | 18 | 2026-11-09 | 33 | 75% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 231 | [x] | Tabletop Simulator (STEAM) | 18 | 2026-11-09 | 31 | 76% |  |
| 232 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 18 | 2026-11-15 | 29 | 63% |  |
| 233 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 2026-11-09 | 29 | 86% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 234 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-11-09 | 27 | 86% |  |
| 235 | [x] | Mafia II: Definitive Edition (GOG) | 18 | 2026-11-15 | 20 | 60% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 236 | [x] | Jade Empire: Special Edition (STEAM) | 18 | 2026-11-09 | 20 | 71% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 237 | [x] | Backpack Battles (STEAM) | 17 | 2026-11-09 | 39 | 89% |  |
| 238 | [x] | Crazy Taxi (STEAM) | 17 | 2026-11-10 | 39 | 68% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 239 | [x] | Counter-Strike: Condition Zero (STEAM) | 17 | 2026-11-11 | 36 | 27% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 240 | [x] | Intravenous 2 (STEAM) | 17 | 2026-11-09 | 33 | 96% |  |
| 241 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 32 | 75% |  |
| 242 | [x] | Mafia II (Classic) (GOG) | 17 | 2026-11-24 | 28 | 70% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 243 | [x] | Nioh: Complete Edition (STEAM) | 17 | 2026-11-23 | 27 | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 244 | [x] | Yakuza 0 (GOG) | 17 | 2026-11-25 | 23 | 64% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 245 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 16 | 2026-11-11 | 37 | 79% |  |
| 246 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 247 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 16 | 2026-11-09 | 29 | 53% |  |
| 248 | [x] | Far Far West (STEAM) | 16 | 2026-11-09 | 29 | 59% |  |
| 249 | [x] | Moonlight Peaks (STEAM) | 16 | 2026-11-09 | 29 | 76% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 250 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 16 | 2026-11-09 | 26 | 93% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 251 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 67% |  |
| 252 | [x] | Party Animals (STEAM) | 16 | 2026-11-09 | 24 | 75% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 253 | [x] | Tales of Zestiria (STEAM) | 16 | 2026-11-09 | 23 | 73% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 254 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 255 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 256 | [x] | Styx: Master of Shadows (EPIC) | 15 | 2026-11-23 | 41 | 50% |  |
| 257 | [x] | Flotsam (EPIC) | 15 | 2026-11-20 | 34 | 41% |  |
| 258 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 29 | 100% |  |
| 259 | [x] | SWORN (STEAM) | 15 | 2026-11-09 | 29 | 95% |  |
| 260 | [x] | Disgaea 4 Complete+ (STEAM) | 15 | 2026-11-09 | 24 | 93% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 261 | [x] | AER Memories of Old (EPIC) | 15 | 2026-11-09 | 23 | 93% |  |
| 262 | [x] | Alabaster Dawn Demo (STEAM) | 15 | 2026-11-09 | 23 | 62% |  |
| 263 | [x] | Need for Speed™ Unbound (STEAM) | 15 | 2026-11-09 | 23 | 58% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 264 | [x] | Sacred Gold (STEAM) | 15 | 2026-11-25 | 23 | 70% | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 265 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 92% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 266 | [x] | Capcom Fighting Collection (STEAM) | 15 | 2026-11-09 | 22 | 89% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 267 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 15 | 2026-11-09 | 22 | 78% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 268 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 269 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 270 | [x] | sobosuba (STEAM) | 14 | 2026-11-09 | 34 | 81% |  |
| 271 | [x] | Spooky's Jump Scare Mansion (STEAM) | 14 | 2026-11-25 | 30 | 50% |  |
| 272 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 29 | 86% |  |
| 273 | [x] | This War of Mine (STEAM) | 14 | 2026-11-17 | 29 | 49% |  |
| 274 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 14 | 2026-11-24 | 28 | 62% |  |
| 275 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 24 | 76% |  |
| 276 | [x] | Nex Machina (STEAM) | 14 | 2026-11-09 | 22 | 88% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 277 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 2026-11-16 | 22 | 88% |  |
| 278 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 279 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 280 | [x] | Spark the Electric Jester (STEAM) | 14 | 2026-11-13 | 20 | 73% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 281 | [x] | Blaster Master Zero (STEAM) | 13 | 2026-11-11 | 29 | 86% |  |
| 282 | [x] | Overlord (STEAM) | 13 | 2026-11-08 | 29 | 44% |  |
| 283 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 13 | 2026-11-13 | 29 | 67% |  |
| 284 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 13 | 2026-11-09 | 28 | 94% |  |
| 285 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 28 | 100% |  |
| 286 | [x] | Evoland (STEAM) | 13 | 2026-11-11 | 27 | n/a |  |
| 287 | [x] | Human Fall Flat (STEAM) | 13 | 2026-10-29 | 27 | 56% |  |
| 288 | [x] | Legacy of Kain: Defiance Remastered (STEAM) | 13 | 2026-11-24 | 27 | 80% |  |
| 289 | [x] | Castle in the Clouds (STEAM) | 13 | 2026-11-09 | 26 | 68% |  |
| 290 | [x] | MX Bikes (STEAM) | 13 | 2026-11-09 | 26 | 96% |  |
| 291 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 26 | 95% |  |
| 292 | [x] | Katana ZERO (GOG) | 13 | 2026-11-24 | 25 | 60% |  |
| 293 | [x] | Car Mechanic Simulator 2018 (STEAM) | 13 | 2026-11-09 | 24 | 90% |  |
| 294 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 24 | 76% |  |
| 295 | [x] | A Plague Tale: Innocence (GOG) | 13 | 2026-11-25 | 23 | 70% |  |
| 296 | [x] | Horny Villa (STEAM) | 13 | 2026-11-09 | 22 | 87% |  |
| 297 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 298 | [x] | Shift At Midnight (STEAM) | 13 | 2026-11-09 | 21 | 90% |  |
| 299 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 70% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 300 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 94% |  |
| 301 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 2026-11-09 | 20 | 85% |  |
| 302 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-11-16 | 20 | 92% |  |
| 303 | [x] | Turbo Overkill (STEAM) | 13 | 2026-11-09 | 20 | 100% |  |
| 304 | [x] | CS2D (STEAM) | 12 | 2026-11-24 | 33 | 64% |  |
| 305 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-24 | 24 | 64% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 306 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 24 | 64% |  |
| 307 | [x] | Sonic Superstars (STEAM) | 12 | 2026-11-21 | 24 | 70% |  |
| 308 | [x] | Forgive Me Father (STEAM) | 12 | 2026-11-15 | 22 | 69% |  |
| 309 | [x] | 12 is Better Than 6 (STEAM) | 12 | 2026-11-09 | 21 | 77% |  |
| 310 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 311 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 312 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 313 | [x] | Hitman: Contracts (STEAM) | 12 | 2026-11-23 | 20 | 69% |  |
| 314 | [x] | GRIP: Combat Racing (STEAM) | 11 | 2026-11-09 | 32 | 81% |  |
| 315 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 28 | 91% |  |
| 316 | [x] | Antichamber (STEAM) | 11 | 2026-11-18 | 26 | 80% |  |
| 317 | [x] | Alan Wake's American Nightmare (EPIC) | 11 | 2026-11-09 | 24 | 73% |  |
| 318 | [x] | HITMAN World of Assassination (STEAM) | 11 | 2026-11-09 | 24 | 71% |  |
| 319 | [x] | Cruelty Squad (STEAM) | 11 | 2026-11-09 | 23 | 83% |  |
| 320 | [x] | Ready or Not (STEAM) | 11 | 2026-11-09 | 23 | 80% |  |
| 321 | [x] | Lost Castle 2 (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 322 | [x] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 2026-11-18 | 21 | 71% |  |
| 323 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 11 | 2026-10-27 | 21 | 93% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 324 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 325 | [x] | Another World: 20th Anniversary Edition (GOG) | 11 | 2026-11-21 | 20 | 60% |  |
| 326 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-11-09 | 20 | 62% |  |
| 327 | [x] | The Stanley Parable (STEAM) | 11 | 2026-11-13 | 20 | 75% |  |
| 328 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 28 | 92% |  |
| 329 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 10 | 2026-10-27 | 27 | 81% |  |
| 330 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 25 | 91% |  |
| 331 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 10 | 2026-11-09 | 24 | 88% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 332 | [x] | Tiny Glade (STEAM) | 10 | 2026-11-09 | 24 | 62% |  |
| 333 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 22 | 85% |  |
| 334 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 10 | 2026-11-10 | 21 | 69% |  |
| 335 | [x] | Ultrapool (STEAM) | 10 | 2026-11-09 | 21 | n/a |  |
| 336 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 337 | [x] | DiRT 4 (STEAM) | 10 | 2026-11-09 | 20 | 100% |  |
| 338 | [x] | Haydee (STEAM) | 10 | 2026-11-09 | 20 | 83% |  |
| 339 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 340 | [x] | Pillars of Eternity (STEAM) | 10 | 2026-11-21 | 20 | 100% |  |
| 341 | [x] | Secret of Mana (STEAM) | 10 | 2026-11-18 | 20 | 70% |  |
| 342 | [x] | Mark of the Ninja (STEAM) | 9 | 2026-10-26 | 25 | 82% |  |
| 343 | [x] | Rayman Origins (GOG) | 9 | 2026-11-09 | 24 | 54% |  |
| 344 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 9 | 2026-11-01 | 24 | n/a |  |
| 345 | [x] | Breath of Fire IV (GOG) | 9 | 2026-10-26 | 23 | 53% |  |
| 346 | [x] | Batman™: Arkham Origins (GOG) | 9 | 2026-11-09 | 22 | 89% |  |
| 347 | [x] | Guacamelee! Gold Edition (STEAM) | 9 | 2026-11-11 | 22 | 69% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 348 | [x] | Need for Speed: Undercover (STEAM) | 9 | 2026-11-11 | 22 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 349 | [x] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 9 | 2026-11-17 | 20 | 33% |  |
| 350 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 27% |  |
| 351 | [x] | UNDEFEATED (STEAM) | 9 | 2026-11-09 | 20 | 75% |  |
| 352 | [x] | WORLD OF FINAL FANTASY (STEAM) | 8 | 2026-11-09 | 23 | 81% |  |
| 353 | [x] | GRANDIA HD Remaster (STEAM) | 8 | 2026-11-09 | 22 | 93% |  |
| 354 | [x] | Lust Goddess (STEAM) | 8 | 2026-11-09 | 22 | 69% |  |
| 355 | [x] | Aperture Desk Job (STEAM) | 8 | 2026-11-03 | 21 | n/a |  |
| 356 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 8 | 2026-11-09 | 20 | 70% |  |
| 357 | [x] | Soul's Remnant (STEAM) | 8 | 2026-11-11 | 20 | n/a |  |
| 358 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 23 | 51% |  |
| 359 | [x] | SCP – Containment Breach (STEAM) | 7 | 2026-10-27 | 21 | 91% |  |
| 360 | [x] | Mina the Hollower (GOG) | 7 | 2026-10-28 | 20 | 74% |  |
| 361 | [x] | CULTIC (STEAM) | 7 | 2026-11-09 | 20 | 53% |  |
| 362 | [x] | Legend of Grimrock 2 (STEAM) | 7 | 2026-11-09 | 20 | 93% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 363 | [x] | Crimzon Clover World EXplosion (STEAM) | 6 | 2026-11-09 | 22 | 86% |  |
| 364 | [x] | Life is Strange Remastered (STEAM) | 5 | 2026-11-09 | 20 | 87% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
