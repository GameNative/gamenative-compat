# GameNative compatibility worklist

Generated: `2026-11-27T04:15:11.905Z` · Ratings since: `2026-08-29T04:15:11.905Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Probably does not work | 183 |
| Fix shipped, waiting for ratings | 19 |
| First launch fails | 280 |
| Mixed | 439 |
| Works | 1037 |
| Total | 2084 |

## Does not work (126)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 220 | 267 | 82% (since fix) | Does not open (91%) | 41% | today | 59% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 2 | [ ] | Slay the Spire (STEAM) | 111 | 152 | 73% (14d) | Does not open (83%) | 43% | today | 82% | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 3 | [ ] | Rocket League® (EPIC) | 75 | 87 | 86% (14d) | Does not open (81%) | 30% | today | 69% | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 4 | [ ] | Buckshot Roulette (STEAM) | 49 | 70 | 70% (14d) | Does not open (69%) | 50% | today | 92% | [#558](https://github.com/GameNative/gamenative-compat/issues/558) |
| 5 | [ ] | Melvor Idle 2: A RuneScape Adventure (STEAM) | 46 | 52 | 88% (14d) | Does not open (86%) | 45% | today | 90% | [#543](https://github.com/GameNative/gamenative-compat/issues/543) |
| 6 | [ ] | Mark of the Deep (EPIC) | 32 | 41 | 78% (14d) | Does not open (90%) | 29% | today | n/a | [#549](https://github.com/GameNative/gamenative-compat/issues/549) |
| 7 | [ ] | Horizon Chase Turbo (EPIC) | 31 | 37 | 84% (14d) | Does not open (82%) | 50% | 1d ago | n/a | [#546](https://github.com/GameNative/gamenative-compat/issues/546) |
| 8 | [ ] | DREDGE (EPIC) | 29 | 35 | 83% (14d) | Does not open (79%) | 47% | today | n/a | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 9 | [ ] | Borderlands 2 (EPIC) | 28 | 31 | 90% (14d) | Does not open (81%) | 44% | today | n/a | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 10 | [x] 2026-10-18 | Project Zomboid (STEAM) | 67 | 76 | 88% (since fix) | Does not open (66%) | 34% | today | 20% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 11 | [ ] | Hogwarts Legacy (EPIC) | 20 | 22 | 91% (14d) | Does not open (75%) | 41% | 1d ago | n/a | [#537](https://github.com/GameNative/gamenative-compat/issues/537) |
| 12 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 19 | 26 | 73% (14d) | Does not open (97%) | 36% | 1d ago | n/a | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 13 | [ ] | Metro: Last Light Redux (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | 30% | today | n/a | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 14 | [ ] | Mafia II (Classic) (STEAM) | 17 | 20 | 85% (14d) | Does not open (78%) | 12% | today | n/a | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 15 | [ ] | Castlevania Anniversary Collection (EPIC) | 17 | 20 | 85% (last 20) | Does not open (75%) | 41% | today | n/a | [#556](https://github.com/GameNative/gamenative-compat/issues/556) |
| 16 | [ ] | Saints Row 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 31% | today | n/a | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 17 | [ ] | Bloons TD 6 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (80%) | 32% | 1d ago | n/a | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 18 | [ ] | Path of Exile (STEAM) | 16 | 20 | 80% (last 20) | Does not open (88%) | 26% | 2d ago | n/a | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 19 | [ ] | Batman™ Arkham Asylum Game of the Year Edition (EPIC) | 15 | 21 | 71% (14d) | Does not open (77%) | 44% | today | n/a | [#563](https://github.com/GameNative/gamenative-compat/issues/563) |
| 20 | [ ] | Driver: Parallel Lines (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | 39% | 1d ago | n/a | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 21 | [ ] | Dead Island 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (87%) | 42% | today | n/a | [#552](https://github.com/GameNative/gamenative-compat/issues/552) |
| 22 | [ ] | Until Then (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 53% | today | n/a | [#559](https://github.com/GameNative/gamenative-compat/issues/559) |
| 23 | [ ] | Sifu (EPIC) | 15 | 20 | 75% (last 20) | Does not open (70%) | 39% | 3d ago | n/a | [#535](https://github.com/GameNative/gamenative-compat/issues/535) |
| 24 | [ ] | BioShock Remastered (EPIC) | 14 | 20 | 70% (last 20) | Does not open (67%) | 50% | 1d ago | n/a | [#547](https://github.com/GameNative/gamenative-compat/issues/547) |
| 25 | [ ] | Saints Row 2 (GOG) | 17 | 20 | 85% (last 20) | Does not open (91%) | 34% | today | n/a | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 26 | [ ] | Bad Cheese (EPIC) | 16 | 20 | 80% (last 20) | Does not open (94%) | 39% | 1d ago | n/a | [#560](https://github.com/GameNative/gamenative-compat/issues/560) |
| 27 | [ ] | Vampire Survivors (EPIC) | 16 | 20 | 80% (last 20) | Does not open (65%) | 34% | today | n/a | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 28 | [ ] | River City Girls (EPIC) | 14 | 20 | 70% (last 20) | Does not open (50%) | 46% | 1d ago | n/a | [#550](https://github.com/GameNative/gamenative-compat/issues/550) |
| 29 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 15 | 20 | 75% (last 20) | Does not open (62%) | 43% | today | n/a | [#564](https://github.com/GameNative/gamenative-compat/issues/564) |
| 30 | [ ] | VRChat (STEAM) | 15 | 20 | 75% (last 20) | Does not open (74%) | 37% | 1d ago | n/a | [#562](https://github.com/GameNative/gamenative-compat/issues/562) |
| 31 | [ ] | ScourgeBringer (STEAM) | 20 | 20 | 100% (last 20) | Does not open (76%) | 6% | today | n/a | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 32 | [ ] | skate. (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 7% | 2d ago | n/a | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 33 | [ ] | STAR WARS™ Knights of the Old Republic™ II: The Sith Lords™ (STEAM) | 16 | 20 | 80% (last 20) | No graphics (60%) | 47% | 1d ago | n/a | [#565](https://github.com/GameNative/gamenative-compat/issues/565) |
| 34 | [ ] | Call of Duty: Black Ops II (STEAM) | 18 | 20 | 90% (last 20) | Does not open (83%) | 43% | 2d ago | n/a | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 35 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 58% | 8d ago | n/a | [#553](https://github.com/GameNative/gamenative-compat/issues/553) |
| 36 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 18 | 20 | 90% (last 20) | Does not open (87%) | 50% | 2d ago | n/a | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 37 | [ ] | Forza Horizon 4 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (43%) | 28% | 4d ago | n/a | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 38 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 16 | 20 | 80% (last 20) | Does not open (88%) | 33% | 1d ago | n/a | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 39 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (91%) | 12% | 13d ago | n/a | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 40 | [ ] | Teenage Mutant Ninja Turtles: Shredder's Revenge (EPIC) | 15 | 20 | 75% (last 20) | Does not open (83%) | 46% | 4d ago | n/a | [#551](https://github.com/GameNative/gamenative-compat/issues/551) |
| 41 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (76%) | 6% | 12d ago | n/a | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 42 | [ ] | Kenshi (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | 7% | 1d ago | n/a | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 43 | [ ] | Fall Guys (EPIC) | 20 | 20 | 100% (last 20) | Does not open (66%) | 3% | 4d ago | n/a | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 44 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (71%) | 31% | 8d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 45 | [ ] | Prince of Persia The Lost Crown (STEAM) | 9 | 10 | 90% (since fix) | Does not open (94%) | 18% | today | n/a | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 46 | [ ] | Happy Wheels (STEAM) | 18 | 20 | 90% (last 20) | No graphics (52%) | 44% | 1d ago | n/a | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 47 | [ ] | Detroit: Become Human (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | 50% | 2d ago | n/a | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 48 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 10% | 3d ago | n/a | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 49 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (72%) | 11% | 1d ago | n/a | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 50 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 15 | 20 | 75% (last 20) | Does not open (62%) | 45% | 1d ago | n/a | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 51 | [ ] | Breath of Fire IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | 9% | 7d ago | n/a | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 52 | [ ] | The Witcher: Enhanced Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (74%) | 9% | 5d ago | n/a | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 53 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | 7% | 26d ago | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 54 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (93%) | 0% | 9d ago | n/a | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 55 | [ ] | Call of Duty® (STEAM) | 17 | 20 | 85% (last 20) | Does not open (63%) | 0% | 6d ago | n/a | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 56 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (78%) | 9% | today | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 57 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (83%) | 11% | 18d ago | n/a | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 58 | [ ] | Blood Omen: Legacy of Kain (GOG) | 17 | 20 | 85% (last 20) | No graphics (57%) | 57% | today | n/a | [#539](https://github.com/GameNative/gamenative-compat/issues/539) |
| 59 | [ ] | MECCHA CHAMELEON (STEAM) | 15 | 20 | 75% (last 20) | Does not open (69%) | 42% | 9d ago | n/a | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 60 | [ ] | CPM 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (88%) | 3% | 1d ago | n/a | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 61 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (84%) | 58% | 6d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 62 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (88%) | 54% | 3d ago | n/a | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 63 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (77%) | 40% | 2d ago | n/a | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 64 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (71%) | 20% | 4d ago | n/a | [#536](https://github.com/GameNative/gamenative-compat/issues/536) |
| 65 | [ ] | The Wolf Among Us (STEAM) | 16 | 20 | 80% (last 20) | Does not open (67%) | 12% | 1d ago | n/a | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 66 | [ ] | CODE VEIN (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 11% | today | n/a | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 67 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (75%) | 5% | today | n/a | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 68 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (91%) | 0% | 1d ago | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 69 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (55%) | 18% | 9d ago | n/a | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 70 | [ ] | Watch Dogs 2 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (80%) | 59% | 3d ago | n/a | [#399](https://github.com/GameNative/gamenative-compat/issues/399) |
| 71 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (91%) | 26% | 2d ago | n/a | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 72 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 38% | 4d ago | n/a | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 73 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | 36% | 4d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 74 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (85%) | 0% | 12d ago | n/a | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 75 | [ ] | Half-Life: Blue Shift (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | 47% | 10d ago | n/a | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 76 | [ ] | Rivals of Aether II (STEAM) | 16 | 20 | 80% (last 20) | Does not open (53%) | 17% | 2d ago | n/a | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 77 | [ ] | Black Mesa (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 30% | 5d ago | n/a | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 78 | [ ] | Ultimate Custom Night (STEAM) | 14 | 20 | 70% (last 20) | No graphics (71%) | 58% | 1d ago | n/a | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 79 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | 0% | 19d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 80 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | 10% | 14d ago | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 81 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | 55% | 13d ago | n/a | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 82 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (88%) | 10% | 12d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 83 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (87%) | 10% | 15d ago | n/a | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 84 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (55%) | 45% | 6d ago | n/a | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 85 | [ ] | A Plague Tale: Innocence (EPIC) | 14 | 20 | 70% (last 20) | Does not open (70%) | 43% | 4d ago | n/a | [#557](https://github.com/GameNative/gamenative-compat/issues/557) |
| 86 | [ ] | Spore (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | 26% | today | n/a | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 87 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 19 | 20 | 95% (last 20) | Does not open (85%) | 42% | 10d ago | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 88 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 3% | today | n/a | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 89 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 18% | 4d ago | n/a | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 90 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 17 | 20 | 85% (last 20) | Does not open (61%) | 29% | 5d ago | n/a | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 91 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (70%) | 28% | 20d ago | n/a | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 92 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | No graphics (59%) | 29% | 6d ago | n/a | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 93 | [ ] | Umamusume: Pretty Derby (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 54% | 7d ago | n/a | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 94 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 43% | 16d ago | n/a | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 95 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | 42% | 16d ago | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 96 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 0% | 27d ago | n/a | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 97 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | 35% | 4d ago | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 98 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 36% | 6d ago | n/a | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 99 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (50%) | 56% | 8d ago | n/a | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 100 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (69%) | 8% | 40d ago | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 101 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 55% | 2d ago | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 102 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 3% | 5d ago | n/a | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 103 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 20% | 7d ago | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 104 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (89%) | 36% | 1d ago | n/a | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 105 | [ ] | Aliens vs. Predator (STEAM) | 17 | 20 | 85% (last 20) | Does not open (74%) | 28% | today | n/a | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 106 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 17 | 20 | 85% (last 20) | Does not open (62%) | 34% | today | n/a | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 107 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (59%) | 44% | 7d ago | n/a | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 108 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (63%) | 31% | 3d ago | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 109 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (96%) | 40% | 25d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 110 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 57% | 6d ago | n/a | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 111 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (52%) | 42% | today | n/a | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 112 | [ ] | Lost Planet: Extreme Condition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (80%) | 50% | 12d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 113 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (55%) | 38% | 15d ago | n/a | [#540](https://github.com/GameNative/gamenative-compat/issues/540) |
| 114 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 53% | 5d ago | n/a | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 115 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | 24% | today | n/a | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 116 | [ ] | OneShot (STEAM) | 15 | 20 | 75% (last 20) | Does not open (94%) | 15% | 6d ago | n/a | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 117 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (88%) | 40% | 5d ago | n/a | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 118 | [ ] | Maneater (EPIC) | 17 | 20 | 85% (last 20) | Does not open (73%) | 25% | 4d ago | n/a | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 119 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | 40% | 16d ago | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 120 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (58%) | 54% | 15d ago | n/a | [#554](https://github.com/GameNative/gamenative-compat/issues/554) |
| 121 | [ ] | Maneater (STEAM) | 15 | 20 | 75% (last 20) | Does not open (86%) | 59% | 2d ago | n/a | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 122 | [ ] | Ghostwire Tokyo (EPIC) | 14 | 20 | 70% (last 20) | Does not open (100%) | 42% | 3d ago | n/a | [#544](https://github.com/GameNative/gamenative-compat/issues/544) |
| 123 | [ ] | TEKKEN 8 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (67%) | 38% | today | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 124 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 14 | 20 | 70% (last 20) | Does not open (95%) | 29% | 3d ago | n/a | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 125 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | Does not open (45%) | 10% | 17d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 126 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (54%) | 39% | 12d ago | n/a | [#541](https://github.com/GameNative/gamenative-compat/issues/541) |

## Probably does not work (183)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Counter-Strike 2 (STEAM) | 57 | 89 | 64% (since fix) | Does not open (68%) | 56% | today | n/a | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 2 | [ ] | Absolute Drift (EPIC) | 21 | 31 | 68% (14d) | No graphics (60%) | 40% | today | n/a | [#555](https://github.com/GameNative/gamenative-compat/issues/555) |
| 3 | [ ] | Metro 2033 Redux (STEAM) | 17 | 25 | 68% (14d) | Does not open (72%) | 42% | today | 31% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 4 | [ ] | Owlboy (STEAM) | 15 | 27 | 56% (14d) | Does not open (77%) | 53% | today | n/a | [#545](https://github.com/GameNative/gamenative-compat/issues/545) |
| 5 | [ ] | Bully: Scholarship Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | 22% | today | 30% |  |
| 6 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 12 | 20 | 60% (last 20) | Does not open (78%) | 48% | today | n/a | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 7 | [ ] | theHunter Classic (STEAM) | 20 | 20 | 100% (last 20) | No graphics (92%) | n/a | 23d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 8 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 27 | 49 | 55% (since fix) | Does not open (72%) | 58% | today | n/a | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 9 | [ ] | Garry's Mod (STEAM) | 17 | 29 | 59% (since fix) | Does not open (80%) | 48% | today | 33% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 10 | [ ] | To The Moon (GOG) | 18 | 20 | 90% (last 20) | Does not open (86%) | n/a | 24d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 11 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | n/a | 18d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 12 | [ ] | Catherine Classic (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (39%) | 45% | today | n/a |  |
| 13 | [ ] | MudRunner (EPIC) | 13 | 20 | 65% (last 20) | Does not open (65%) | 46% | 1d ago | n/a |  |
| 14 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 11 | 17 | 65% (since fix) | Does not open (84%) | 56% | today | n/a | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 15 | [ ] | Phasmophobia (STEAM) | 11 | 20 | 55% (last 20) | Does not open (61%) | 47% | today | n/a |  |
| 16 | [ ] | DOOM 64 (EPIC) | 11 | 20 | 55% (last 20) | Does not open (62%) | 42% | today | n/a |  |
| 17 | [ ] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 16 | 31 | 52% (since fix) | Does not open (83%) | 49% | today | 67% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 18 | [ ] | Cat Quest (EPIC) | 11 | 20 | 55% (last 20) | Does not open (44%) | 39% | 1d ago | n/a |  |
| 19 | [ ] | Sonic Adventure™ 2  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (77%) | 42% | 1d ago | n/a | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 20 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (83%) | 46% | today | n/a | [#548](https://github.com/GameNative/gamenative-compat/issues/548) |
| 21 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 11 | 18 | 61% (since fix) | Does not open (90%) | 52% | today | n/a | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 22 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 16 | 24 | 67% (since fix) | Does not open (78%) | 43% | 4d ago | n/a | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 23 | [ ] | Art of Rally (EPIC) | 13 | 20 | 65% (last 20) | Does not open (79%) | 33% | today | n/a |  |
| 24 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 47d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 25 | [ ] | PAYDAY: The Heist (STEAM) | 16 | 20 | 80% (last 20) | Does not open (81%) | n/a | 2d ago | n/a |  |
| 26 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (39%) | n/a | 6d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 27 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 13d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 28 | [ ] | Door Kickers 2 (STEAM) | 18 | 20 | 90% (last 20) | No graphics (85%) | n/a | 4d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 29 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 11 | 20 | 55% (last 20) | Does not open (69%) | 44% | 1d ago | n/a |  |
| 30 | [ ] | Darksiders Warmastered Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 46% | today | n/a |  |
| 31 | [ ] | Hi-Fi RUSH (STEAM) | 13 | 20 | 65% (last 20) | Does not open (75%) | 45% | 1d ago | n/a | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 32 | [ ] | Metro 2033 Redux (EPIC) | 13 | 20 | 65% (last 20) | Does not open (67%) | 37% | today | n/a | [#561](https://github.com/GameNative/gamenative-compat/issues/561) |
| 33 | [ ] | Transistor (STEAM) | 6 | 11 | 55% (since fix) | Does not open (73%) | 30% | today | n/a | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 34 | [ ] | Deskrawl: Idle ARPG (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | n/a | 16d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 35 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 31d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 36 | [ ] | Gorilla Tag (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 14% | 2d ago | n/a | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 37 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | No graphics (59%) | n/a | 30d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 38 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (100%) | n/a | today | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 39 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (50%) | 50% | 1d ago | n/a | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 40 | [ ] | Last Epoch (STEAM) | 11 | 20 | 55% (last 20) | Does not open (82%) | 53% | 1d ago | n/a |  |
| 41 | [ ] | Prototype (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 56% | today | 80% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 42 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (79%) | 56% | 6d ago | n/a |  |
| 43 | [ ] | Counter-Strike (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 35% | 2d ago | n/a | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 44 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | No graphics (38%) | 48% | 5d ago | n/a |  |
| 45 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (87%) | n/a | 20d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 46 | [ ] | Call of Duty: Black Ops II - Zombies (STEAM) | 5 | 10 | 50% (since fix) | Does not open (72%) | 59% | 2d ago | n/a | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 47 | [ ] | Deliver At All Costs (EPIC) | 13 | 20 | 65% (last 20) | Does not open (61%) | 41% | 3d ago | n/a | [#538](https://github.com/GameNative/gamenative-compat/issues/538) |
| 48 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 12 | 20 | 60% (last 20) | Does not open (87%) | 35% | 7d ago | n/a | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 49 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 28d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 50 | [ ] | Counter-Strike:Global Offensive (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 55% | 4d ago | n/a |  |
| 51 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | n/a | 10d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 52 | [ ] | Stumble Guys (STEAM) | 12 | 20 | 60% (last 20) | Does not open (72%) | 57% | 1d ago | n/a |  |
| 53 | [ ] | System Shock 2: 25th Anniversary Remaster (EPIC) | 10 | 20 | 50% (last 20) | Does not open (83%) | 43% | 1d ago | n/a |  |
| 54 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 17% | today | n/a | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 55 | [ ] | Saints Row IV Re-Elected (EPIC) | 10 | 20 | 50% (last 20) | No graphics (50%) | 40% | 2d ago | n/a |  |
| 56 | [ ] | Brutal Legend (GOG) | 16 | 20 | 80% (last 20) | Does not open (75%) | n/a | 1d ago | n/a |  |
| 57 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 22d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 58 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | 45% | 1d ago | n/a | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 59 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (69%) | n/a | 25d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 60 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | n/a | 5d ago | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 61 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 16d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 62 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | n/a | 1d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 63 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | n/a | 12d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 64 | [ ] | Rise of the Tomb Raider: 20 Year Celebration (EPIC) | 13 | 20 | 65% (last 20) | Does not open (73%) | 44% | today | n/a |  |
| 65 | [ ] | No More Heroes (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 38% | 1d ago | n/a |  |
| 66 | [ ] | Borderlands GOTY (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 53% | 1d ago | n/a | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 67 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (71%) | 21% | 2d ago | n/a | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 68 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 45d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 69 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | n/a | 25d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 70 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (83%) | n/a | 36d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 71 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 8d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 72 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (74%) | n/a | 24d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 73 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | 13d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 74 | [ ] | Dead Space 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (63%) | 32% | 2d ago | n/a | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 75 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (65%) | n/a | 44d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 76 | [ ] | Northgard: Definitive Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | n/a | 1d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 77 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (57%) | n/a | 12d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 78 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | n/a | 13d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 79 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | n/a | 13d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 80 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 2d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 81 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | n/a | 28d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 82 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (64%) | n/a | 1d ago | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 83 | [ ] | Alpha Protocol (STEAM) | 16 | 20 | 80% (last 20) | No graphics (56%) | n/a | 2d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 84 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 22d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 85 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 36% | 10d ago | n/a | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 86 | [ ] | Grim Dawn (GOG) | 12 | 20 | 60% (last 20) | Does not open (68%) | n/a | today | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 87 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 33% | 2d ago | n/a |  |
| 88 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | n/a | 47d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 89 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 44d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 90 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (50%) | n/a | 3d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 91 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 13d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 92 | [ ] | Borderlands 2 RU (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | n/a | 10d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 93 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | 9d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 94 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 30d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 95 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | No graphics (50%) | n/a | 30d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 96 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | n/a | 19d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 97 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 26d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 98 | [ ] | Beholder (EPIC) | 18 | 20 | 90% (last 20) | Does not open (56%) | n/a | 6d ago | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 99 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | n/a | 49d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 100 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (82%) | n/a | 1d ago | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 101 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (58%) | n/a | 2d ago | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 102 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (62%) | n/a | 53d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 103 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (76%) | n/a | 3d ago | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 104 | [ ] | DOOM Eternal (STEAM) | 16 | 20 | 80% (last 20) | Does not open (63%) | n/a | 2d ago | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 105 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 18d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 106 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | n/a | 11d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 107 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (54%) | n/a | 32d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 108 | [ ] | Blood West (EPIC) | 11 | 20 | 55% (last 20) | Does not open (100%) | 30% | today | n/a |  |
| 109 | [ ] | Metro 2033 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (65%) | 42% | today | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 110 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | n/a | 6d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 111 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 22d ago | n/a |  |
| 112 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | today | n/a |  |
| 113 | [ ] | Big Walk (STEAM) | 13 | 20 | 65% (last 20) | Does not open (61%) | 59% | today | n/a |  |
| 114 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 13 | 20 | 65% (last 20) | Does not open (88%) | n/a | 2d ago | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 115 | [ ] | Hollow Knight: Silksong (GOG) | 10 | 20 | 50% (last 20) | Does not open (67%) | 45% | 5d ago | n/a |  |
| 116 | [ ] | The Survivalists (STEAM) | 17 | 20 | 85% (last 20) | Does not open (95%) | n/a | 1d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 117 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (56%) | n/a | 20d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 118 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | n/a | 17d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 119 | [ ] | Super Meat Boy Forever (EPIC) | 10 | 20 | 50% (last 20) | Does not open (83%) | 25% | 7d ago | n/a |  |
| 120 | [ ] | LEGO® Builder's Journey (EPIC) | 10 | 20 | 50% (last 20) | No graphics (63%) | 42% | today | n/a |  |
| 121 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (89%) | n/a | 28d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 122 | [ ] | Turing Complete (STEAM) | 16 | 20 | 80% (last 20) | Does not open (79%) | n/a | 1d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 123 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 29d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 124 | [ ] | State of Decay 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (90%) | 7% | today | n/a | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 125 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 22d ago | n/a |  |
| 126 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 22d ago | n/a |  |
| 127 | [ ] | Mafia: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 37% | today | n/a |  |
| 128 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 41% | 2d ago | n/a | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 129 | [ ] | Sol Cesto (STEAM) | 11 | 20 | 55% (last 20) | Does not open (63%) | 50% | today | n/a |  |
| 130 | [ ] | Lucid Blocks (STEAM) | 11 | 20 | 55% (last 20) | Does not open (94%) | 58% | 7d ago | n/a |  |
| 131 | [ ] | Goat Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 52% | 1d ago | n/a |  |
| 132 | [ ] | CS2D (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | n/a | 4d ago | n/a |  |
| 133 | [ ] | POSTAL: Brain Damaged (STEAM) | 15 | 20 | 75% (last 20) | Does not open (91%) | n/a | 1d ago | n/a |  |
| 134 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 15d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 135 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | n/a | 7d ago | n/a |  |
| 136 | [ ] | The Planet Crafter (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (38%) | n/a | today | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 137 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | n/a | 9d ago | n/a | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 138 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 13 | 20 | 65% (last 20) | Does not open (55%) | 29% | 11d ago | n/a | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 139 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 13 | 20 | 65% (last 20) | Does not open (94%) | n/a | 1d ago | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 140 | [ ] | Mortal Shell (EPIC) | 13 | 20 | 65% (last 20) | Does not open (46%) | 22% | 8d ago | n/a |  |
| 141 | [ ] | Hitman 2: Silent Assassin (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 39% | 4d ago | n/a | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 142 | [ ] | Drop Duchy (EPIC) | 12 | 20 | 60% (last 20) | Does not open (100%) | n/a | 1d ago | n/a |  |
| 143 | [ ] | Dying Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (77%) | 44% | 4d ago | n/a |  |
| 144 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Controller issues (36%) | n/a | 8d ago | n/a |  |
| 145 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 10 | 20 | 50% (last 20) | Does not open (90%) | 36% | 5d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 146 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | 14d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 147 | [ ] | Songs of Conquest (EPIC) | 14 | 20 | 70% (last 20) | Does not open (67%) | n/a | 1d ago | n/a |  |
| 148 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | n/a | 39d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 149 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (82%) | n/a | 7d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 150 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (63%) | 45% | 13d ago | n/a |  |
| 151 | [ ] | FINAL FANTASY VII REMAKE INTERGRADE (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 42% | 2d ago | n/a |  |
| 152 | [ ] | Romancing SaGa -Minstrel Song- Remastered (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (100%) | n/a | 5d ago | n/a |  |
| 153 | [ ] | Sid Meier's Civilization VI (EPIC) | 13 | 20 | 65% (last 20) | Does not open (58%) | 54% | 3d ago | n/a |  |
| 154 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 26% | 27d ago | n/a |  |
| 155 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 12 | 20 | 60% (last 20) | Does not open (53%) | 50% | today | n/a |  |
| 156 | [ ] | HOT WHEELS UNLEASHED™ (EPIC) | 12 | 20 | 60% (last 20) | No graphics (50%) | 32% | 3d ago | n/a |  |
| 157 | [ ] | Sacred Gold (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | n/a | 8d ago | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 158 | [ ] | Football Manager 2024 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (91%) | 59% | 2d ago | n/a |  |
| 159 | [ ] | Minit (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | n/a | 2d ago | n/a |  |
| 160 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 54% | 16d ago | n/a |  |
| 161 | [ ] | LET IT DIE (STEAM) | 12 | 20 | 60% (last 20) | Does not open (94%) | n/a | 5d ago | n/a |  |
| 162 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (81%) | n/a | 1d ago | n/a |  |
| 163 | [ ] | Chasm (GOG) | 12 | 20 | 60% (last 20) | No graphics (50%) | n/a | 12d ago | n/a |  |
| 164 | [ ] | Crying Suns (EPIC) | 12 | 20 | 60% (last 20) | No graphics (56%) | n/a | 4d ago | n/a |  |
| 165 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (50%) | n/a | 4d ago | n/a |  |
| 166 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | n/a | 8d ago | n/a |  |
| 167 | [ ] | DAEMON X MACHINA (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 28% | 1d ago | n/a |  |
| 168 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Does not open (44%) | n/a | 18d ago | n/a |  |
| 169 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 22d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 170 | [ ] | Turnip Boy Robs a Bank (EPIC) | 12 | 20 | 60% (last 20) | Does not open (80%) | 31% | 2d ago | n/a | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 171 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 11 | 20 | 55% (last 20) | Does not open (100%) | 36% | 5d ago | n/a |  |
| 172 | [ ] | Gloomwood (STEAM) | 11 | 20 | 55% (last 20) | No graphics (57%) | 55% | today | n/a |  |
| 173 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 57% | 6d ago | n/a |  |
| 174 | [ ] | Eastern Exorcist (EPIC) | 10 | 20 | 50% (last 20) | No graphics (50%) | 58% | today | n/a |  |
| 175 | [ ] | Hitman: Absolution (GOG) | 10 | 20 | 50% (last 20) | Does not open (80%) | n/a | 9d ago | n/a |  |
| 176 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 50% | 17d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 177 | [ ] | Sandustry (STEAM) | 11 | 20 | 55% (last 20) | Does not open (74%) | n/a | 1d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 178 | [ ] | Allumeria (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | n/a | 5d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 179 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | n/a | 15d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 180 | [ ] | LEGO® MARVEL's Avengers (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 33% | 2d ago | n/a |  |
| 181 | [ ] | A Plague Tale: Innocence (GOG) | 10 | 20 | 50% (last 20) | Does not open (92%) | n/a | 2d ago | n/a |  |
| 182 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | n/a | 21d ago | n/a |  |
| 183 | [ ] | Delver (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 11% | today | n/a |  |

## Fix shipped, waiting for ratings (19)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | Hogwarts Legacy (STEAM) | n/a | 5 | 2 | today | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 2 | Trackmania (STEAM) | n/a | 2 | 0 | today | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 3 | Far Cry® 3 (STEAM) | n/a | 1 | 1 | today | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 4 | Max Payne 3 (STEAM) | 2026-11-04 | 6 | 6 | 1d ago | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 5 | Peggle Deluxe (STEAM) | 2026-10-29 | 7 | 3 | 3d ago | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 6 | Red Dead Redemption (STEAM) | 2026-11-04 | 2 | 2 | 10d ago | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 7 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 4 | 4 | 5d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 8 | South Park The Fractured But Whole (STEAM) | n/a | 3 | 3 | today | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 9 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 6 | 6 | today | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 10 | Scott Pilgrim vs The World (STEAM) | n/a | 1 | 0 | 1d ago | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 11 | Watch_Dogs 2 (STEAM) | n/a | 2 | 0 | today | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 12 | Watch_Dogs (STEAM) | n/a | 6 | 5 | 1d ago | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 13 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 3 | 3 | today | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 14 | Need for Speed™ (STEAM) | 2026-11-04 | 3 | 3 | today | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 15 | XCOM: Enemy Unknown (STEAM) | n/a | 2 | 1 | 1d ago | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 16 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 2 | 2 | 4d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 17 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 2 | 2 | 5d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 18 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 3 | 3 | 1d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 19 | Assassin's Creed Odyssey (STEAM) | n/a | 1 | 1 | 5d ago | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |

## Works, but the first launch usually fails (280)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Half-Life (STEAM) | 84 | 118 | 71% (14d) | Does not open (59%) | 69% | today | 65% |  |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 73 | 90 | 81% (14d) | Does not open (61%) | 95% | today | 91% |  |
| 3 | [ ] | Grand Theft Auto V Legacy (STEAM) | 111 | 137 | 81% (since fix) | Does not open (87%) | 78% | today | 93% |  |
| 4 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 55 | 69 | 80% (14d) | Does not open (55%) | 84% | today | 86% |  |
| 5 | [ ] | Portal (STEAM) | 51 | 77 | 66% (14d) | Does not open (38%) | 88% | today | 86% |  |
| 6 | [ ] | ROB RUN (STEAM) | 45 | 56 | 80% (14d) | Does not open (88%) | 67% | today | 79% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 7 | [ ] | Selaco (STEAM) | 34 | 54 | 63% (14d) | Does not open (89%) | 68% | today | 93% |  |
| 8 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 33 | 51 | 65% (14d) | Does not open (60%) | 64% | today | 77% |  |
| 9 | [ ] | Valheim (STEAM) | 53 | 92 | 58% (since fix) | No graphics (55%) | 82% | today | 96% |  |
| 10 | [ ] | MONSTER HUNTER RISE (STEAM) | 30 | 54 | 56% (14d) | Does not open (83%) | 62% | today | 70% |  |
| 11 | [ ] | No Man's Sky (STEAM) | 42 | 81 | 52% (since fix) | Controller issues (60%) | 78% | today | 76% |  |
| 12 | [ ] | PEAK (STEAM) | 23 | 39 | 59% (14d) | Does not open (65%) | 82% | today | 86% |  |
| 13 | [ ] | ELDEN RING (STEAM) | 21 | 27 | 78% (14d) | Does not open (87%) | 65% | today | 77% |  |
| 14 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 20 | 21 | 95% (14d) | Does not open (40%) | 91% | today | n/a |  |
| 15 | [ ] | Euro Truck Simulator 2 (STEAM) | 19 | 38 | 50% (14d) | Does not open (65%) | 61% | today | 69% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 16 | [ ] | Noita (STEAM) | 19 | 28 | 68% (14d) | Does not open (58%) | 79% | today | 90% |  |
| 17 | [ ] | Baldur's Gate 3 (STEAM) | 18 | 30 | 60% (14d) | Does not open (68%) | 81% | today | 68% |  |
| 18 | [ ] | Probably Stolen (STEAM) | 18 | 33 | 55% (14d) | Does not open (61%) | 84% | today | 83% |  |
| 19 | [ ] | Red Dead Redemption 2 (STEAM) | 29 | 36 | 81% (since fix) | Does not open (95%) | 88% | today | 80% |  |
| 20 | [ ] | Grand Theft Auto V (EPIC) | 19 | 20 | 95% (last 20) | Does not open (89%) | 78% | today | 90% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 21 | [ ] | BeamNG.drive (STEAM) | 17 | 23 | 74% (14d) | Does not open (76%) | 63% | 2d ago | 77% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 22 | [ ] | Fallout 3: Game of the Year Edition (GOG) | 15 | 30 | 50% (14d) | Does not open (48%) | 74% | 1d ago | n/a |  |
| 23 | [ ] | Grand Theft Auto: Vice City (STEAM) | 15 | 20 | 75% (14d) | Does not open (36%) | 82% | 1d ago | 100% |  |
| 24 | [ ] | Overcooked! 2 (EPIC) | 15 | 20 | 75% (14d) | Does not open (92%) | 62% | 1d ago | n/a |  |
| 25 | [ ] | Pathogenic (STEAM) | 14 | 20 | 70% (14d) | Does not open (85%) | 68% | 1d ago | n/a |  |
| 26 | [ ] | Resident Evil 4 (2005) (STEAM) | 14 | 21 | 67% (14d) | Does not open (80%) | 73% | today | n/a |  |
| 27 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 14 | 23 | 61% (14d) | Controller issues (50%) | 66% | today | n/a |  |
| 28 | [ ] | Tales of ARISE (STEAM) | 14 | 20 | 70% (14d) | Controller issues (73%) | 86% | today | n/a |  |
| 29 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (90%) | 90% | today | n/a |  |
| 30 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 16 | 20 | 80% (last 20) | Does not open (77%) | 65% | today | n/a | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 31 | [ ] | Dead Space (STEAM) | 16 | 20 | 80% (last 20) | Does not open (67%) | 77% | 1d ago | n/a | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 32 | [ ] | Fallout: New Vegas PCR (STEAM) | 15 | 20 | 75% (last 20) | Does not open (93%) | 68% | today | n/a | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 33 | [ ] | Look Outside (STEAM) | 12 | 22 | 55% (14d) | Controller issues (65%) | 91% | 1d ago | n/a |  |
| 34 | [ ] | Team Fortress 2 (STEAM) | 12 | 22 | 55% (14d) | Does not open (67%) | 77% | 1d ago | 83% |  |
| 35 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 17 | 20 | 85% (last 20) | Does not open (61%) | 89% | 1d ago | n/a | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 36 | [ ] | Cry of Fear (STEAM) | 14 | 20 | 70% (last 20) | Does not open (48%) | 68% | today | n/a |  |
| 37 | [ ] | RimWorld (STEAM) | 11 | 22 | 50% (14d) | Does not open (49%) | 80% | 1d ago | 73% |  |
| 38 | [ ] | Alabaster Dawn (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (48%) | 88% | 2d ago | n/a |  |
| 39 | [ ] | Clair Obscur: Expedition 33 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (39%) | 74% | 3d ago | n/a |  |
| 40 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (57%) | 92% | today | n/a |  |
| 41 | [ ] | Deadlock (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 80% | 5d ago | n/a |  |
| 42 | [ ] | Welcome to Elderfield (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 69% | today | n/a |  |
| 43 | [ ] | DOOM (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 87% | 1d ago | n/a |  |
| 44 | [ ] | Rune Factory 3 Special (STEAM) | 14 | 20 | 70% (last 20) | Does not open (90%) | 100% | today | n/a |  |
| 45 | [ ] | Loftia (STEAM) | 13 | 20 | 65% (last 20) | Does not open (95%) | 67% | today | n/a |  |
| 46 | [ ] | Quake (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 64% | 1d ago | n/a |  |
| 47 | [ ] | Shakedown: Hawaii (STEAM) | 11 | 20 | 55% (last 20) | Does not open (81%) | 76% | today | n/a |  |
| 48 | [ ] | Monster Hunter: World (STEAM) | 10 | 20 | 50% (14d) | Does not open (53%) | 79% | 1d ago | 100% |  |
| 49 | [ ] | The Forest (STEAM) | 10 | 20 | 50% (14d) | Does not open (68%) | 79% | today | n/a |  |
| 50 | [ ] | Mass Effect™ Legendary Edition (STEAM) | 15 | 28 | 54% (since fix) | Does not open (83%) | 84% | 2d ago | n/a |  |
| 51 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 14 | 26 | 54% (since fix) | Controller issues (79%) | 71% | 2d ago | n/a | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 52 | [ ] | Library Of Ruina (STEAM) | 11 | 20 | 55% (last 20) | Does not open (74%) | 87% | 1d ago | n/a |  |
| 53 | [ ] | Barony (STEAM) | 11 | 20 | 55% (last 20) | Does not open (78%) | 80% | today | n/a |  |
| 54 | [ ] | Coromon (STEAM) | 10 | 20 | 50% (last 20) | Does not open (52%) | 83% | today | n/a |  |
| 55 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 70% | 2d ago | n/a |  |
| 56 | [ ] | Stardew Valley (GOG) | 12 | 20 | 60% (last 20) | Controller issues (61%) | 85% | today | n/a |  |
| 57 | [ ] | Palworld (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 85% | today | 88% |  |
| 58 | [ ] | Crypt of the NecroDancer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (47%) | 88% | 1d ago | n/a |  |
| 59 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (70%) | 95% | 2d ago | n/a | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 60 | [ ] | Cyberpunk 2077 (GOG) | 11 | 20 | 55% (last 20) | Does not open (73%) | 66% | 1d ago | 50% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 61 | [ ] | 80's OVERDRIVE (STEAM) | 10 | 20 | 50% (last 20) | No graphics (72%) | 84% | today | n/a |  |
| 62 | [ ] | Aniimo (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 75% | 3d ago | n/a | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 63 | [ ] | Mortal Kombat X (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 94% | 9d ago | n/a |  |
| 64 | [ ] | Batman™: Arkham Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 67% | today | 54% |  |
| 65 | [ ] | OMORI (STEAM) | 11 | 20 | 55% (last 20) | Does not open (65%) | 60% | today | n/a | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 66 | [ ] | Dressmaker (STEAM) | 11 | 20 | 55% (last 20) | Does not open (56%) | 74% | today | 77% |  |
| 67 | [ ] | TrackMania Nations Forever (STEAM) | 10 | 20 | 50% (last 20) | Does not open (48%) | 70% | today | n/a |  |
| 68 | [ ] | Fallout: New Vegas (EPIC) | 17 | 20 | 85% (last 20) | Does not open (59%) | 75% | today | n/a |  |
| 69 | [ ] | Fate/stay night REMASTERED (STEAM) | 13 | 20 | 65% (last 20) | No graphics (54%) | 94% | 1d ago | n/a |  |
| 70 | [ ] | Assetto Corsa (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (47%) | 85% | today | 92% |  |
| 71 | [ ] | Devil May Cry 5 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (81%) | 82% | today | 71% |  |
| 72 | [ ] | Chained Echoes (GOG) | 15 | 20 | 75% (last 20) | Does not open (62%) | 60% | 2d ago | n/a | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 73 | [ ] | Don't Starve Together (STEAM) | 10 | 20 | 50% (last 20) | Does not open (61%) | 74% | 1d ago | 100% |  |
| 74 | [ ] | Disco Elysium - The Final Cut (EPIC) | 12 | 20 | 60% (last 20) | Does not open (78%) | 91% | 3d ago | n/a |  |
| 75 | [ ] | Resident Evil 7 Biohazard (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 63% | 3d ago | n/a |  |
| 76 | [ ] | Disgaea 5 Complete (STEAM) | 18 | 20 | 90% (last 20) | Does not open (75%) | 94% | 10d ago | n/a | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 77 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (48%) | 84% | today | n/a |  |
| 78 | [ ] | Cave Story+ (STEAM) | 19 | 20 | 95% (last 20) | Does not open (64%) | 75% | 5d ago | n/a | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 79 | [ ] | Asterigos: Curse of the Stars (STEAM) | 16 | 20 | 80% (last 20) | Graphics glitches (73%) | 90% | 5d ago | n/a |  |
| 80 | [ ] | Moonstone Island (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (64%) | 80% | today | n/a | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 81 | [ ] | Mortal Kombat 11 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (71%) | 64% | 2d ago | n/a |  |
| 82 | [ ] | Mini Motorways (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 65% | today | n/a | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 83 | [ ] | FINAL FANTASY (STEAM) | 12 | 20 | 60% (last 20) | Does not open (78%) | 78% | 4d ago | n/a |  |
| 84 | [ ] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 12 | 20 | 60% (last 20) | Does not open (60%) | 82% | 4d ago | n/a | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 85 | [ ] | Doki Doki Literature Club (STEAM) | 11 | 20 | 55% (last 20) | Does not open (52%) | 83% | today | n/a |  |
| 86 | [ ] | Poppy Playtime (STEAM) | 13 | 20 | 65% (last 20) | Does not open (53%) | 66% | today | n/a |  |
| 87 | [ ] | POSTAL 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | 60% | 1d ago | n/a |  |
| 88 | [ ] | Castlevania Dominus Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (91%) | 96% | 5d ago | n/a |  |
| 89 | [ ] | Little Witch in the Woods (STEAM) | 11 | 20 | 55% (last 20) | Does not open (55%) | 84% | 4d ago | n/a |  |
| 90 | [ ] | Palia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | 71% | 4d ago | n/a | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 91 | [ ] | Minecraft Dungeons II (STEAM) | 15 | 20 | 75% (last 20) | Does not open (80%) | 69% | 3d ago | n/a | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 92 | [ ] | eFootball™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (67%) | 61% | 9d ago | n/a |  |
| 93 | [ ] | No, I'm not a Human (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 91% | today | n/a |  |
| 94 | [ ] | PAC-MAN Championship Edition DX+ (STEAM) | 10 | 20 | 50% (last 20) | No graphics (59%) | 61% | today | n/a |  |
| 95 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 15 | 20 | 75% (last 20) | Does not open (45%) | 88% | 2d ago | n/a | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 96 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 71% | 10d ago | 70% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 97 | [ ] | Dota 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (79%) | 76% | 2d ago | n/a |  |
| 98 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (62%) | 75% | 1d ago | n/a |  |
| 99 | [ ] | TBH: Task Bar Hero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (66%) | 83% | 4d ago | n/a | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 100 | [ ] | Titanfall® 2 (STEAM) | 9 | 13 | 69% (since fix) | Does not open (89%) | 69% | 2d ago | n/a |  |
| 101 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 17 | 20 | 85% (last 20) | Controller issues (87%) | 93% | 1d ago | n/a | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 102 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (76%) | 75% | 9d ago | n/a | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 103 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (47%) | 86% | today | n/a |  |
| 104 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 97% | 8d ago | n/a | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 105 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 16 | 20 | 80% (last 20) | Does not open (67%) | 79% | 1d ago | n/a |  |
| 106 | [ ] | Ratatan (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | 87% | 6d ago | n/a |  |
| 107 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 100% | 4d ago | n/a | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 108 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (43%) | 75% | 3d ago | n/a |  |
| 109 | [ ] | L.A. Noire (STEAM) | 14 | 20 | 70% (last 20) | Does not open (96%) | 65% | today | n/a | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 110 | [ ] | Tails of Iron (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 90% | 5d ago | n/a |  |
| 111 | [ ] | Devil May Cry 4 Special Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (84%) | 66% | today | n/a |  |
| 112 | [ ] | SONIC X SHADOW GENERATIONS (STEAM) | 10 | 20 | 50% (last 20) | Does not open (79%) | 80% | 3d ago | 90% |  |
| 113 | [ ] | Oxygen Not Included (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 76% | today | n/a |  |
| 114 | [ ] | PlateUp! (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 75% | 1d ago | n/a |  |
| 115 | [ ] | The Sims™ 4 (STEAM) | 7 | 14 | 50% (since fix) | Does not open (86%) | 67% | 3d ago | n/a | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 116 | [ ] | Resident Evil Village (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 84% | 1d ago | n/a |  |
| 117 | [ ] | Unturned (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 82% | 3d ago | n/a |  |
| 118 | [ ] | Astral Party  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 82% | 7d ago | n/a |  |
| 119 | [ ] | A Plague Tale: Innocence (STEAM) | 18 | 20 | 90% (last 20) | Does not open (85%) | 68% | today | n/a | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 120 | [ ] | Dishonored 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 63% | today | n/a | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 121 | [ ] | Caravan SandWitch (EPIC) | 10 | 20 | 50% (last 20) | Does not open (69%) | 66% | today | n/a |  |
| 122 | [ ] | Abiotic Factor (STEAM) | 10 | 20 | 50% (last 20) | Does not open (74%) | 84% | 10d ago | n/a |  |
| 123 | [ ] | FINAL FANTASY VIII - REMASTERED (STEAM) | 10 | 20 | 50% (last 20) | Does not open (94%) | 75% | today | n/a |  |
| 124 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | 83% | 13d ago | n/a | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 125 | [ ] | Call of Duty: World at War (STEAM) | 12 | 20 | 60% (last 20) | Does not open (38%) | 72% | today | n/a | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 126 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (87%) | 87% | 20d ago | n/a |  |
| 127 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 90% | 1d ago | n/a |  |
| 128 | [ ] | Digimon Survive (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (83%) | 88% | 2d ago | n/a |  |
| 129 | [ ] | Gambonanza (STEAM) | 13 | 20 | 65% (last 20) | Does not open (61%) | 88% | today | n/a |  |
| 130 | [ ] | Legacy of Kain: Defiance Remastered (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (69%) | 75% | 5d ago | n/a |  |
| 131 | [ ] | Hood Warfare 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (62%) | 65% | today | n/a |  |
| 132 | [ ] | Street Fighter™ 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | 74% | 5d ago | n/a |  |
| 133 | [ ] | Fable - The Lost Chapters (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (43%) | 85% | 1d ago | n/a | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 134 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (86%) | 88% | 9d ago | n/a | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 135 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (70%) | 83% | 4d ago | n/a | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 136 | [ ] | Sonic Generations (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 68% | today | n/a | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 137 | [ ] | Stellar Blade™ (STEAM) | 14 | 20 | 70% (last 20) | No graphics (42%) | 84% | 6d ago | n/a |  |
| 138 | [ ] | Gothic 1 Classic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (57%) | 70% | 3d ago | n/a |  |
| 139 | [ ] | Yakuza: Like a Dragon (STEAM) | 13 | 20 | 65% (last 20) | Does not open (62%) | 72% | 1d ago | n/a |  |
| 140 | [ ] | OCTOPATH TRAVELER 0 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (77%) | 91% | 2d ago | n/a |  |
| 141 | [ ] | CrossCode (GOG) | 17 | 20 | 85% (last 20) | Does not open (79%) | 62% | 1d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 142 | [x] 2026-10-18 | Diablo® IV (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 86% | today | n/a | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 143 | [ ] | Supermarket Together (STEAM) | 16 | 20 | 80% (last 20) | Does not open (64%) | 63% | 2d ago | n/a | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 144 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (88%) | 62% | 16d ago | n/a | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 145 | [ ] | Tabletop Simulator (STEAM) | 14 | 20 | 70% (last 20) | Does not open (42%) | 79% | 8d ago | n/a |  |
| 146 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 94% | 3d ago | n/a |  |
| 147 | [ ] | Max Payne (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (46%) | 81% | 3d ago | n/a |  |
| 148 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (83%) | 60% | 17d ago | n/a |  |
| 149 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 78% | 3d ago | n/a |  |
| 150 | [ ] | One-armed robber (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (72%) | 68% | today | n/a |  |
| 151 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | 86% | 14d ago | n/a | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 152 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (48%) | 75% | 1d ago | n/a | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 153 | [ ] | Aggelos (STEAM) | 16 | 20 | 80% (last 20) | No graphics (79%) | 81% | today | n/a | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 154 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 90% | 20d ago | n/a |  |
| 155 | [ ] | DRAPLINE (STEAM) | 13 | 20 | 65% (last 20) | Does not open (100%) | 100% | 1d ago | n/a |  |
| 156 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (66%) | 76% | 3d ago | n/a |  |
| 157 | [ ] | Trailmakers (STEAM) | 11 | 20 | 55% (last 20) | Does not open (46%) | 100% | 1d ago | n/a |  |
| 158 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (57%) | 92% | 5d ago | n/a | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 159 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (92%) | 73% | 7d ago | n/a | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 160 | [ ] | Control Ultimate Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (72%) | 68% | 2d ago | n/a |  |
| 161 | [ ] | Plague Inc: Evolved (STEAM) | 13 | 20 | 65% (last 20) | Does not open (59%) | 68% | 6d ago | n/a | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 162 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 10 | 20 | 50% (last 20) | Does not open (59%) | 89% | 2d ago | n/a |  |
| 163 | [ ] | SurrounDead (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (71%) | 89% | 1d ago | n/a |  |
| 164 | [ ] | Changed (STEAM) | 16 | 20 | 80% (last 20) | Does not open (64%) | 61% | 1d ago | n/a | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 165 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (59%) | 62% | 15d ago | n/a | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 166 | [ ] | Necesse (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 67% | 5d ago | n/a | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 167 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 61% | 3d ago | n/a |  |
| 168 | [ ] | Yu-Gi-Oh!  Master Duel (STEAM) | 10 | 20 | 50% (last 20) | Does not open (79%) | 68% | 1d ago | n/a |  |
| 169 | [ ] | Sonic Lost World (STEAM) | 10 | 20 | 50% (last 20) | No graphics (69%) | 82% | 6d ago | n/a | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 170 | [ ] | Heavy Rain (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (65%) | 90% | 3d ago | n/a |  |
| 171 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (48%) | 77% | 2d ago | n/a |  |
| 172 | [ ] | Pinball FX (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 71% | today | n/a |  |
| 173 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 69% | 15d ago | n/a | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 174 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (43%) | 70% | today | n/a | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 175 | [ ] | CLANNAD (STEAM) | 13 | 20 | 65% (last 20) | No graphics (47%) | 88% | 1d ago | n/a |  |
| 176 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (82%) | 92% | 8d ago | n/a |  |
| 177 | [ ] | My Summer Car (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 68% | 3d ago | n/a |  |
| 178 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | 64% | 16d ago | n/a | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 179 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 90% | 37d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 180 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | 82% | 4d ago | n/a |  |
| 181 | [ ] | Gothic II: Gold Classic (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 73% | today | n/a | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 182 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (76%) | 100% | 17d ago | n/a |  |
| 183 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 72% | 5d ago | n/a | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 184 | [ ] | HELLDIVERS™ (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 63% | 2d ago | n/a | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 185 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (78%) | 93% | 2d ago | n/a |  |
| 186 | [ ] | Warframe (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 79% | 3d ago | n/a |  |
| 187 | [ ] | TurretGirls (STEAM) | 12 | 20 | 60% (last 20) | No graphics (77%) | 100% | 7d ago | n/a |  |
| 188 | [ ] | METAL SLUG 3 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (79%) | 67% | 3d ago | n/a | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 189 | [ ] | Limbus Company (STEAM) | 11 | 20 | 55% (last 20) | Does not open (88%) | 96% | today | n/a |  |
| 190 | [ ] | Overwatch® (STEAM) | 8 | 11 | 73% (since fix) | Does not open (61%) | 83% | 4d ago | n/a | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 191 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (76%) | 62% | 1d ago | n/a | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 192 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 86% | today | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 193 | [ ] | Return to Monkey Island (STEAM) | 15 | 20 | 75% (last 20) | No graphics (74%) | 72% | 3d ago | n/a |  |
| 194 | [ ] | Hylics (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (72%) | 90% | 4d ago | n/a |  |
| 195 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (61%) | 70% | 5d ago | n/a |  |
| 196 | [ ] | Tower and Sword of Succubus (STEAM) | 12 | 20 | 60% (last 20) | No graphics (89%) | 77% | 1d ago | n/a |  |
| 197 | [ ] | Escape from Duckov (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (65%) | 96% | 1d ago | n/a |  |
| 198 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | 95% | 16d ago | n/a | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 199 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (73%) | 67% | 21d ago | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 200 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (69%) | 73% | 4d ago | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 201 | [ ] | Subnautica 2 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (44%) | 87% | 2d ago | n/a | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 202 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (61%) | 83% | 16d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 203 | [ ] | Capcom Arcade Stadium (STEAM) | 14 | 20 | 70% (last 20) | Does not open (74%) | 71% | 1d ago | n/a | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 204 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 13 | 20 | 65% (last 20) | Does not open (81%) | 62% | 2d ago | n/a |  |
| 205 | [ ] | Turbo Overkill (STEAM) | 13 | 20 | 65% (last 20) | No graphics (91%) | 100% | 5d ago | n/a |  |
| 206 | [ ] | Jade Empire: Special Edition (GOG) | 15 | 20 | 75% (last 20) | Graphics glitches (56%) | 75% | 1d ago | n/a | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 207 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (59%) | 75% | 30d ago | n/a |  |
| 208 | [ ] | Dead Island (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 86% | 1d ago | n/a | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 209 | [ ] | AER Memories of Old (EPIC) | 14 | 20 | 70% (last 20) | Does not open (86%) | 94% | 1d ago | n/a |  |
| 210 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (47%) | 91% | 1d ago | n/a |  |
| 211 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 100% | 17d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 212 | [ ] | Hotline Miami (GOG) | 13 | 20 | 65% (last 20) | Does not open (87%) | 71% | 3d ago | n/a | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 213 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (50%) | 94% | today | n/a | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 214 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 94% | 3d ago | n/a |  |
| 215 | [ ] | GUILTY GEAR Xrd REV 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | 63% | 1d ago | n/a |  |
| 216 | [ ] | No Socks RPG (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (91%) | 93% | 1d ago | n/a |  |
| 217 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (64%) | 72% | 15d ago | n/a |  |
| 218 | [ ] | MX Bikes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 96% | 9d ago | n/a |  |
| 219 | [ ] | Invisible, Inc. (STEAM) | 14 | 20 | 70% (last 20) | Does not open (79%) | 92% | 4d ago | n/a |  |
| 220 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (82%) | 84% | 10d ago | n/a | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 221 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 92% | today | n/a | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 222 | [ ] | Yakuza 0 (GOG) | 13 | 20 | 65% (last 20) | Does not open (70%) | 67% | 1d ago | n/a | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 223 | [ ] | Capcom Fighting Collection (STEAM) | 13 | 20 | 65% (last 20) | Does not open (83%) | 81% | today | n/a | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 224 | [ ] | SnowRunner (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | 74% | 4d ago | n/a | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 225 | [ ] | Donut Dodo (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 95% | 1d ago | n/a |  |
| 226 | [ ] | Darksiders (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 77% | 4d ago | n/a | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 227 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 92% | 1d ago | n/a |  |
| 228 | [ ] | Spark the Electric Jester (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 77% | 6d ago | n/a | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 229 | [ ] | Ys: Memories of Celceta (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 67% | today | n/a |  |
| 230 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (45%) | 78% | 2d ago | n/a |  |
| 231 | [ ] | Tales of Zestiria (STEAM) | 13 | 20 | 65% (last 20) | Does not open (75%) | 83% | 4d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 232 | [ ] | SILENT HILL 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 100% | 3d ago | n/a |  |
| 233 | [ ] | Timberborn (STEAM) | 12 | 20 | 60% (last 20) | No graphics (57%) | 100% | 8d ago | n/a |  |
| 234 | [ ] | BATTLETECH (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 92% | 11d ago | n/a |  |
| 235 | [ ] | Alabaster Dawn Demo (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (71%) | 64% | today | n/a |  |
| 236 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 94% | 19d ago | n/a |  |
| 237 | [ ] | GOD EATER RESURRECTION (STEAM) | 11 | 20 | 55% (last 20) | Does not open (56%) | 93% | today | n/a |  |
| 238 | [ ] | Super Battle Golf (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 91% | 4d ago | n/a |  |
| 239 | [ ] | Secrets of Grindea (STEAM) | 10 | 20 | 50% (last 20) | Does not open (48%) | 81% | 9d ago | n/a | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 240 | [ ] | Zero Escape: The Nonary Games (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 68% | 6d ago | n/a |  |
| 241 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 77% | 4d ago | n/a | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 242 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 79% | 2d ago | n/a |  |
| 243 | [ ] | Serious Sam 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 82% | today | n/a |  |
| 244 | [ ] | HITMAN World of Assassination (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 76% | 1d ago | n/a |  |
| 245 | [ ] | Decktamer (STEAM) | 13 | 20 | 65% (last 20) | Does not open (100%) | 70% | 4d ago | n/a |  |
| 246 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 93% | 38d ago | n/a |  |
| 247 | [ ] | Goose Goose Duck (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 72% | 7d ago | n/a | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 248 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (42%) | 81% | today | n/a | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 249 | [ ] | Mafia II (Classic) (GOG) | 12 | 20 | 60% (last 20) | Does not open (100%) | 70% | 4d ago | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 250 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 69% | 14d ago | n/a |  |
| 251 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 75% | 18d ago | n/a |  |
| 252 | [ ] | Sons Of The Forest (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 73% | 12d ago | n/a |  |
| 253 | [ ] | Forgive Me Father (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 67% | 3d ago | n/a |  |
| 254 | [ ] | Deus Ex™ GOTY Edition (GOG) | 11 | 20 | 55% (last 20) | No graphics (46%) | 92% | 5d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 255 | [ ] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (61%) | 73% | today | n/a |  |
| 256 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 77% | today | n/a |  |
| 257 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 92% | 1d ago | n/a |  |
| 258 | [ ] | Rollout Inline (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 69% | 7d ago | n/a |  |
| 259 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 75% | 11d ago | n/a |  |
| 260 | [ ] | Disgaea 4 Complete+ (STEAM) | 12 | 20 | 60% (last 20) | No graphics (40%) | 93% | 4d ago | n/a | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 261 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 83% | today | n/a |  |
| 262 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | 70% | 4d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 263 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 67% | today | n/a |  |
| 264 | [ ] | Hitman: Contracts (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (82%) | 67% | 4d ago | n/a |  |
| 265 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 84% | 4d ago | n/a |  |
| 266 | [ ] | CRUEL (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 85% | 12d ago | n/a | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 267 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 93% | 12d ago | n/a |  |
| 268 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (100%) | 93% | 2d ago | n/a |  |
| 269 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (40%) | 69% | 15d ago | n/a |  |
| 270 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 75% | 11d ago | n/a |  |
| 271 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 82% | 12d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 272 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 64% | 10d ago | n/a | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 273 | [ ] | 12 is Better Than 6 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (40%) | 73% | 1d ago | n/a |  |
| 274 | [ ] | Assetto Corsa Competizione (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 80% | 4d ago | n/a |  |
| 275 | [ ] | BioShock 2 Remastered (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 82% | 7d ago | n/a |  |
| 276 | [ ] | Sort Them Ducks (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (64%) | 100% | 4d ago | n/a |  |
| 277 | [ ] | Cruelty Squad (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 82% | 3d ago | n/a |  |
| 278 | [ ] | Dungeon Siege (STEAM) | 10 | 20 | 50% (last 20) | No graphics (50%) | 100% | 6d ago | n/a |  |
| 279 | [ ] | Command & Conquer™ Red Alert™ 3 (STEAM) | 10 | 20 | 50% (last 20) | No graphics (38%) | 93% | 5d ago | n/a | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 280 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 89% | 6d ago | n/a | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |

## Recently recovered (344)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Grim Dawn (STEAM) | 428 | 2026-11-08 | 517 | 73% |  |
| 2 | [x] | Half-Life (STEAM) | 368 | 2026-11-09 | 626 | 69% |  |
| 3 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 267 | 2026-11-14 | 428 | 74% |  |
| 4 | [x] | MONSTER HUNTER RISE (STEAM) | 223 | 2026-11-17 | 517 | 62% |  |
| 5 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 217 | 2026-11-09 | 373 | 64% |  |
| 6 | [x] | Alan Wake (STEAM) | 209 | 2026-11-14 | 241 | 83% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 7 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 206 | 2026-11-09 | 272 | 89% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 8 | [x] | BeamNG.drive (STEAM) | 171 | 2026-11-09 | 215 | 63% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 9 | [x] | Geometry Dash (STEAM) | 162 | 2026-11-11 | 454 | 67% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 10 | [x] | DRAGON BALL FighterZ (STEAM) | 155 | 2026-11-01 | 204 | 87% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 11 | [x] | OMORI (STEAM) | 144 | 2026-11-09 | 186 | 60% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 12 | [x] | Call of Duty: Black Ops (STEAM) | 139 | 2026-11-13 | 166 | 27% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 13 | [x] | BioShock (STEAM) | 135 | 2026-11-09 | 282 | 71% |  |
| 14 | [x] | Team Fortress 2 (STEAM) | 135 | 2026-11-09 | 235 | 77% |  |
| 15 | [x] | Spelunky 2 (STEAM) | 135 | 2026-11-01 | 192 | 88% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 16 | [x] | Sid Meier's Civilization V (STEAM) | 134 | 2026-11-10 | 149 | 59% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 17 | [x] | Minecraft Dungeons II (STEAM) | 133 | 2026-11-09 | 152 | 69% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 18 | [x] | Castlevania Advance Collection (STEAM) | 129 | 2026-11-09 | 207 | 88% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 19 | [x] | Euro Truck Simulator 2 (STEAM) | 121 | 2026-11-23 | 214 | 61% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 20 | [x] | Aniimo (STEAM) | 117 | 2026-11-09 | 158 | 75% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 21 | [x] | Mirror's Edge (STEAM) | 104 | 2026-11-09 | 164 | 69% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 22 | [x] | Cave Story+ (STEAM) | 100 | 2026-11-09 | 108 | 75% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 23 | [x] | Assassin's Creed II (STEAM) | 99 | 2026-11-10 | 104 | 71% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 24 | [x] | The Witcher: Enhanced Edition (STEAM) | 93 | 2026-11-09 | 115 | 73% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 25 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 91 | 2026-11-09 | 130 | 89% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 26 | [x] | Necesse (STEAM) | 91 | 2026-11-22 | 101 | 67% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 27 | [x] | Moonstone Island (STEAM) | 87 | 2026-11-09 | 114 | 80% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 28 | [x] | Fallout: New Vegas PCR (STEAM) | 83 | 2026-11-20 | 113 | 68% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 29 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 82 | 2026-11-15 | 128 | 91% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 30 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 79 | 2026-11-09 | 127 | 75% |  |
| 31 | [x] | FINAL FANTASY XIII-2 (STEAM) | 79 | 2026-11-09 | 82 | 73% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 32 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 78 | 2026-11-23 | 99 | 65% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 33 | [x] | DOOM 3: BFG Edition (STEAM) | 77 | 2026-11-09 | 121 | 72% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 34 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 75 | 2026-11-09 | 118 | 75% |  |
| 35 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 75 | 2026-11-09 | 97 | 93% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 36 | [x] | Vital Shell (STEAM) | 72 | 2026-11-09 | 122 | 88% |  |
| 37 | [x] | Brawlhalla (STEAM) | 70 | 2026-11-09 | 136 | 70% |  |
| 38 | [x] | Order of the Sinking Star (STEAM) | 69 | 2026-11-09 | 107 | 66% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 39 | [x] | Cyberpunk 2077 (GOG) | 68 | 2026-11-09 | 93 | 66% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 40 | [x] | Stardew Valley (GOG) | 67 | 2026-11-11 | 118 | 85% |  |
| 41 | [x] | The Sims™ 4 (STEAM) | 67 | 2026-11-09 | 92 | 67% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 42 | [x] | Grand Theft Auto V (EPIC) | 67 | 2026-11-09 | 71 | 78% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 43 | [x] | Psychonauts (STEAM) | 66 | 2026-11-09 | 133 | 89% |  |
| 44 | [x] | Ballionaire (STEAM) | 66 | 2026-11-09 | 117 | 83% |  |
| 45 | [x] | Diablo® IV (STEAM) | 65 | 2026-11-11 | 80 | 86% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 46 | [x] | Dota 2 (STEAM) | 63 | 2026-11-09 | 98 | 76% |  |
| 47 | [x] | Horizon Zero Dawn™ Complete Edition (STEAM) | 63 | 2026-11-25 | 76 | 88% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 48 | [x] | American Truck Simulator (STEAM) | 62 | 2026-11-09 | 101 | 66% |  |
| 49 | [x] | Age of Empires II: Definitive Edition (STEAM) | 62 | 2026-11-10 | 81 | 65% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 50 | [x] | Disgaea 5 Complete (STEAM) | 62 | 2026-11-09 | 70 | 94% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 51 | [x] | Mini Motorways (STEAM) | 61 | 2026-11-09 | 94 | 65% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 52 | [x] | GRID (STEAM) | 61 | 2026-11-21 | 82 | 54% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 53 | [x] | Spyro™ Reignited Trilogy (STEAM) | 60 | 2026-11-09 | 106 | 79% |  |
| 54 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 58 | 2026-11-09 | 98 | 92% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 55 | [x] | Need for Speed: Hot Pursuit (STEAM) | 58 | 2026-11-09 | 90 | 69% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 56 | [x] | Fable - The Lost Chapters (STEAM) | 57 | 2026-11-09 | 98 | 85% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 57 | [x] | Quake (STEAM) | 56 | 2026-11-09 | 181 | 64% |  |
| 58 | [x] | Gunfire Reborn (STEAM) | 56 | 2026-11-09 | 62 | 88% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 59 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 55 | 2026-11-09 | 94 | 66% |  |
| 60 | [x] | Borderlands 3 (STEAM) | 55 | 2026-11-09 | 86 | 94% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 61 | [x] | FINAL FANTASY XIII (STEAM) | 53 | 2026-11-22 | 515 | 63% |  |
| 62 | [x] | Fallout (STEAM) | 53 | 2026-11-09 | 87 | 61% |  |
| 63 | [x] | Call of Duty: World at War (STEAM) | 53 | 2026-11-09 | 75 | 72% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 64 | [x] | Sonic Generations (STEAM) | 53 | 2026-11-09 | 61 | 68% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 65 | [x] | Sovereign Tower (STEAM) | 52 | 2026-11-09 | 110 | 76% |  |
| 66 | [x] | Firewatch (STEAM) | 52 | 2026-11-10 | 107 | 95% |  |
| 67 | [x] | Poppy Playtime (STEAM) | 52 | 2026-11-09 | 93 | 66% |  |
| 68 | [x] | A Plague Tale: Innocence (STEAM) | 51 | 2026-11-09 | 55 | 68% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 69 | [x] | Caravan SandWitch (EPIC) | 50 | 2026-11-09 | 103 | 66% |  |
| 70 | [x] | ROB RUN (STEAM) | 50 | 2026-11-17 | 67 | 67% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 71 | [x] | Call of Juarez Gunslinger (STEAM) | 50 | 2026-11-09 | 63 | 62% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 72 | [x] | MIO: Memories in Orbit (STEAM) | 49 | 2026-11-09 | 104 | 94% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 73 | [x] | eFootball™ (STEAM) | 49 | 2026-11-09 | 74 | 61% |  |
| 74 | [x] | Moonlighter (EPIC) | 49 | 2026-11-09 | 53 | 95% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 75 | [x] | Darksiders (STEAM) | 48 | 2026-11-09 | 64 | 77% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 76 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 48 | 2026-11-09 | 54 | 100% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 77 | [x] | STEINS;GATE (STEAM) | 47 | 2026-11-09 | 76 | 81% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 78 | [x] | HELLDIVERS™ (STEAM) | 47 | 2026-11-23 | 59 | 63% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 79 | [x] | Okami HD (STEAM) | 46 | 2026-11-09 | 88 | 96% |  |
| 80 | [x] | Starbound (STEAM) | 46 | 2026-11-09 | 74 | 91% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 81 | [x] | Oxygen Not Included (STEAM) | 45 | 2026-11-11 | 81 | 76% |  |
| 82 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 45 | 2026-11-13 | 75 | 69% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 83 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 45 | 2026-11-17 | 71 | 70% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 84 | [x] | TBH: Task Bar Hero (STEAM) | 45 | 2026-11-09 | 71 | 83% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 85 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 44 | 2026-11-09 | 64 | 71% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 86 | [x] | Overwatch® (STEAM) | 44 | 2026-11-10 | 49 | 83% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 87 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 43 | 2026-11-09 | 73 | 73% |  |
| 88 | [x] | METAL SLUG 3 (STEAM) | 43 | 2026-11-24 | 56 | 67% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 89 | [x] | Sol Cesto (EPIC) | 42 | 2026-11-09 | 42 | 75% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 90 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 41 | 2026-11-09 | 78 | 85% |  |
| 91 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 40 | 2026-11-27 | 73 | 43% |  |
| 92 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 39 | 2026-11-09 | 61 | 86% |  |
| 93 | [x] | Borderlands: The Pre-Sequel (STEAM) | 38 | 2026-11-09 | 78 | 66% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 94 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 38 | 2026-11-09 | 69 | 84% |  |
| 95 | [x] | Digimon World: Next Order (STEAM) | 37 | 2026-11-09 | 70 | 90% |  |
| 96 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 37 | 2026-11-09 | 67 | 92% |  |
| 97 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 37 | 2026-11-09 | 67 | 84% |  |
| 98 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 37 | 2026-11-09 | 65 | 52% |  |
| 99 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 37 | 2026-11-09 | 62 | 71% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 100 | [x] | Age of Empires II (2013) (STEAM) | 36 | 2026-11-09 | 61 | 75% |  |
| 101 | [x] | Russian Fishing 4 (STEAM) | 36 | 2026-11-09 | 42 | 62% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 102 | [x] | Amnesia: The Dark Descent (STEAM) | 35 | 2026-11-09 | 74 | 88% |  |
| 103 | [x] | Darkest Dungeon® (EPIC) | 35 | 2026-11-09 | 73 | 88% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 104 | [x] | Sonic Lost World (STEAM) | 35 | 2026-11-09 | 55 | 82% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 105 | [x] | Street Fighter™ 6 (STEAM) | 35 | 2026-11-09 | 55 | 74% |  |
| 106 | [x] | Aggelos (STEAM) | 35 | 2026-11-09 | 52 | 81% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 107 | [x] | L.A. Noire (STEAM) | 35 | 2026-11-24 | 46 | 65% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 108 | [x] | CrossCode (GOG) | 35 | 2026-11-09 | 40 | 62% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 109 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 35 | 2026-11-19 | 37 | 83% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 110 | [x] | Monster Hunter Wilds (STEAM) | 35 | 2026-11-09 | 36 | 86% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 111 | [x] | Dead by Daylight (STEAM) | 34 | 2026-11-09 | 38 | 83% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 112 | [x] | Being a DIK (STEAM) | 33 | 2026-11-09 | 75 | 71% |  |
| 113 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 33 | 2026-11-09 | 59 | 78% |  |
| 114 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 32 | 2026-11-09 | 72 | 75% |  |
| 115 | [x] | Hearts of Iron IV (STEAM) | 32 | 2026-11-09 | 69 | 80% |  |
| 116 | [x] | COCOON (STEAM) | 32 | 2026-11-09 | 63 | 82% |  |
| 117 | [x] | POSTAL 2 (GOG) | 32 | 2026-11-09 | 61 | 88% |  |
| 118 | [x] | XCOM 2 (STEAM) | 32 | 2026-11-09 | 59 | 75% |  |
| 119 | [x] | Sonic Origins (STEAM) | 32 | 2026-11-09 | 58 | 76% |  |
| 120 | [x] | Yume Nikki (STEAM) | 31 | 2026-11-20 | 58 | 57% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 121 | [x] | Gauntlet™  (STEAM) | 31 | 2026-11-11 | 49 | n/a | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 122 | [x] | FINAL FANTASY VII (2013) (STEAM) | 31 | 2026-11-09 | 47 | 50% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 123 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 31 | 2026-11-09 | 39 | 92% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 124 | [x] | Red Dead Redemption (STEAM) | 31 | 2026-11-09 | 34 | 53% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 125 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 30 | 2026-11-09 | 61 | 89% |  |
| 126 | [x] | SurrounDead (STEAM) | 30 | 2026-11-09 | 61 | 89% |  |
| 127 | [x] | Ace Attorney Investigations Collection (STEAM) | 30 | 2026-11-09 | 58 | 89% |  |
| 128 | [x] | Max Payne (STEAM) | 30 | 2026-11-09 | 52 | 81% |  |
| 129 | [x] | Resident Evil Village (STEAM) | 30 | 2026-11-09 | 51 | 84% |  |
| 130 | [x] | Plague Inc: Evolved (STEAM) | 30 | 2026-11-16 | 48 | 68% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 131 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 30 | 2026-11-09 | 45 | 79% |  |
| 132 | [x] | Tomb Raider: Anniversary (STEAM) | 29 | 2026-11-09 | 57 | 62% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 133 | [x] | Earthion (STEAM) | 29 | 2026-11-09 | 53 | 100% |  |
| 134 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 29 | 2026-11-09 | 52 | 75% |  |
| 135 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 29 | 2026-11-09 | 49 | 70% |  |
| 136 | [x] | Breathedge (STEAM) | 29 | 2026-11-23 | 45 | 63% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 137 | [x] | Need for Speed™ Rivals (STEAM) | 29 | 2026-11-10 | 45 | 76% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 138 | [x] | SnowRunner (STEAM) | 29 | 2026-11-09 | 40 | 74% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 139 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 34 | 75% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 140 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 28 | 2026-11-09 | 52 | 85% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 141 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 28 | 2026-11-09 | 45 | 70% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 142 | [x] | Digimon Survive (STEAM) | 28 | 2026-11-09 | 41 | 88% |  |
| 143 | [x] | Resident Evil Revelations 2 (STEAM) | 27 | 2026-11-09 | 55 | 85% |  |
| 144 | [x] | Heavy Rain (STEAM) | 27 | 2026-11-09 | 48 | 90% |  |
| 145 | [x] | Prince of Persia: The Sands of Time (STEAM) | 27 | 2026-11-09 | 48 | 77% |  |
| 146 | [x] | Hero Siege (STEAM) | 27 | 2026-11-09 | 47 | 86% |  |
| 147 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 27 | 2026-11-09 | 47 | 92% |  |
| 148 | [x] | Secrets of Grindea (STEAM) | 27 | 2026-11-09 | 46 | 81% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 149 | [x] | Yakuza: Like a Dragon (STEAM) | 27 | 2026-11-09 | 43 | 72% |  |
| 150 | [x] | Palia (STEAM) | 27 | 2026-11-09 | 38 | 71% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 151 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 43 | 68% |  |
| 152 | [x] | Supermarket Together (STEAM) | 26 | 2026-11-18 | 34 | 63% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 153 | [x] | Lobotomy Corporation (STEAM) | 25 | 2026-11-09 | 49 | 94% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 154 | [x] | Dead Rising 2 (STEAM) | 25 | 2026-11-09 | 41 | 87% |  |
| 155 | [x] | Gothic II: Gold Classic (STEAM) | 25 | 2026-11-09 | 37 | 73% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 156 | [x] | Capcom Arcade Stadium (STEAM) | 25 | 2026-11-09 | 35 | 71% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 157 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-19 | 32 | 90% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 158 | [x] | Skullgirls 2nd Encore (STEAM) | 24 | 2026-11-10 | 62 | 76% |  |
| 159 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 24 | 2026-11-09 | 47 | 54% |  |
| 160 | [x] | Cat Mail Co. (STEAM) | 24 | 2026-11-09 | 44 | 92% |  |
| 161 | [x] | My Summer Car (STEAM) | 24 | 2026-11-09 | 38 | 68% |  |
| 162 | [x] | Ratatan (STEAM) | 24 | 2026-11-09 | 37 | 87% |  |
| 163 | [x] | Mortal Kombat 11 (STEAM) | 24 | 2026-11-27 | 35 | 64% |  |
| 164 | [x] | Chained Echoes (GOG) | 23 | 2026-11-19 | 48 | 60% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 165 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 43 | 97% |  |
| 166 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 2026-11-09 | 40 | 87% |  |
| 167 | [x] | Unturned (STEAM) | 23 | 2026-11-09 | 40 | 82% |  |
| 168 | [x] | Dishonored 2 (STEAM) | 23 | 2026-11-09 | 35 | 63% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 169 | [x] | Hotline Miami (GOG) | 23 | 2026-11-18 | 31 | 71% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 170 | [x] | Jade Empire: Special Edition (GOG) | 23 | 2026-11-09 | 30 | 75% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 171 | [x] | Crab Game (STEAM) | 23 | 2026-11-09 | 27 | 64% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 172 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 22 | 2026-11-09 | 56 | 86% |  |
| 173 | [x] | Frostpunk (STEAM) | 22 | 2026-11-09 | 49 | 89% |  |
| 174 | [x] | The Bazaar (STEAM) | 22 | 2026-11-09 | 48 | 82% |  |
| 175 | [x] | Deponia (STEAM) | 22 | 2026-11-09 | 45 | 84% |  |
| 176 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 22 | 2026-11-09 | 42 | 93% |  |
| 177 | [x] | Gambonanza (STEAM) | 22 | 2026-11-09 | 41 | 88% |  |
| 178 | [x] | Tower and Sword of Succubus (STEAM) | 22 | 2026-11-09 | 39 | 77% |  |
| 179 | [x] | Control Ultimate Edition (GOG) | 22 | 2026-11-09 | 38 | 68% |  |
| 180 | [x] | One-armed robber (STEAM) | 22 | 2026-11-09 | 38 | 68% |  |
| 181 | [x] | Titanfall® 2 (STEAM) | 22 | 2026-11-09 | 38 | 69% |  |
| 182 | [x] | Opus Magnum (STEAM) | 22 | 2026-11-09 | 35 | 100% |  |
| 183 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 58 | 97% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 184 | [x] | Prince of Persia (GOG) | 21 | 2026-11-09 | 43 | 70% |  |
| 185 | [x] | Trailmakers (STEAM) | 21 | 2026-11-09 | 39 | 100% |  |
| 186 | [x] | Worms W.M.D (STEAM) | 21 | 2026-11-09 | 37 | 96% |  |
| 187 | [x] | Return to Monkey Island (STEAM) | 21 | 2026-11-09 | 32 | 72% |  |
| 188 | [x] | Changed (STEAM) | 21 | 2026-11-23 | 31 | 61% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 189 | [x] | Goose Goose Duck (STEAM) | 21 | 2026-11-18 | 30 | 72% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 190 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 82% |  |
| 191 | [x] | Limbus Company (STEAM) | 20 | 2026-11-09 | 33 | 96% |  |
| 192 | [x] | CRUEL (STEAM) | 20 | 2026-11-09 | 30 | 85% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 193 | [x] | Dead Island (STEAM) | 20 | 2026-11-09 | 27 | 86% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 194 | [x] | Subnautica 2 (STEAM) | 20 | 2026-11-15 | 26 | 87% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 195 | [x] | Crusader Kings III (STEAM) | 20 | 2026-11-18 | 24 | 86% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 196 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 20 | 2026-11-09 | 22 | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 197 | [x] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 20 | 2026-11-22 | 21 | 69% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 198 | [x] | Battle Brothers (STEAM) | 19 | 2026-11-09 | 40 | 79% |  |
| 199 | [x] | Wizard of Legend (EPIC) | 19 | 2026-11-09 | 38 | 79% |  |
| 200 | [x] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 2026-11-15 | 37 | 77% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 201 | [x] | Pinball FX Classic (STEAM) | 19 | 2026-11-09 | 36 | 83% |  |
| 202 | [x] | Baldur's Gate: Enhanced Edition (GOG) | 19 | 2026-11-26 | 32 | 65% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 203 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 32 | 100% |  |
| 204 | [x] | GOD EATER RESURRECTION (STEAM) | 19 | 2026-11-09 | 32 | 93% |  |
| 205 | [x] | Asterigos: Curse of the Stars (STEAM) | 19 | 2026-11-26 | 31 | 90% |  |
| 206 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 19 | 2026-11-09 | 30 | 81% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 207 | [x] | Torchlight II (EPIC) | 19 | 2026-11-09 | 27 | 84% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 208 | [x] | Dark Sector (STEAM) | 19 | 2026-11-21 | 25 | 83% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 209 | [x] | Mirror's Edge™ (GOG) | 18 | 2026-11-13 | 36 | 83% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 210 | [x] | Capcom Fighting Collection 2 (STEAM) | 18 | 2026-11-09 | 34 | 90% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 211 | [x] | Mini Metro (STEAM) | 18 | 2026-11-16 | 34 | 61% |  |
| 212 | [x] | Guildrun Demo (STEAM) | 18 | 2026-11-09 | 33 | 82% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 213 | [x] | Tabletop Simulator (STEAM) | 18 | 2026-11-09 | 31 | 79% |  |
| 214 | [x] | Deus Ex™ GOTY Edition (GOG) | 18 | 2026-11-09 | 29 | 92% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 215 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 18 | 2026-11-15 | 29 | 62% |  |
| 216 | [x] | Beyond: Two Souls (STEAM) | 18 | 2026-11-26 | 26 | 62% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 217 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-11-09 | 26 | 90% |  |
| 218 | [x] | CarX Street (STEAM) | 18 | 2026-11-09 | 22 | 67% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 219 | [x] | Tearscape (STEAM) | 18 | 2026-11-09 | 22 | 73% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 220 | [x] | Mafia II: Definitive Edition (GOG) | 18 | 2026-11-15 | 20 | 60% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 221 | [x] | Jade Empire: Special Edition (STEAM) | 18 | 2026-11-09 | 20 | 71% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 222 | [x] | Crazy Taxi (STEAM) | 17 | 2026-11-10 | 42 | 69% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 223 | [x] | Counter-Strike: Condition Zero (STEAM) | 17 | 2026-11-11 | 37 | 33% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 224 | [x] | Strider (STEAM) | 17 | 2026-11-20 | 33 | 73% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 225 | [x] | Mafia II (Classic) (GOG) | 17 | 2026-11-24 | 28 | 70% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 226 | [x] | Nioh: Complete Edition (STEAM) | 17 | 2026-11-23 | 28 | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 227 | [x] | Flotsam (EPIC) | 16 | 2026-11-20 | 37 | 39% |  |
| 228 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 229 | [x] | Moonlight Peaks (STEAM) | 16 | 2026-11-09 | 29 | 70% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 230 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 16 | 2026-11-09 | 28 | 53% |  |
| 231 | [x] | Timberborn (STEAM) | 16 | 2026-11-09 | 26 | 100% |  |
| 232 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 69% |  |
| 233 | [x] | Invisible, Inc. (STEAM) | 16 | 2026-11-09 | 25 | 92% |  |
| 234 | [x] | AER Memories of Old (EPIC) | 16 | 2026-11-09 | 24 | 94% |  |
| 235 | [x] | Party Animals (STEAM) | 16 | 2026-11-09 | 24 | 72% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 236 | [x] | Yakuza 0 (GOG) | 16 | 2026-11-25 | 23 | 67% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 237 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 238 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 239 | [x] | Backpack Battles (STEAM) | 15 | 2026-11-09 | 37 | 89% |  |
| 240 | [x] | sobosuba (STEAM) | 15 | 2026-11-09 | 37 | 80% |  |
| 241 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 15 | 2026-11-11 | 35 | 83% |  |
| 242 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 15 | 2026-11-26 | 30 | 91% |  |
| 243 | [x] | Far Far West (STEAM) | 15 | 2026-11-09 | 27 | 47% |  |
| 244 | [x] | Alabaster Dawn Demo (STEAM) | 15 | 2026-11-27 | 24 | 64% |  |
| 245 | [x] | Disgaea 4 Complete+ (STEAM) | 15 | 2026-11-09 | 24 | 93% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 246 | [x] | Need for Speed™ Unbound (STEAM) | 15 | 2026-11-09 | 23 | 58% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 247 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 15 | 2026-11-16 | 23 | 83% |  |
| 248 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 100% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 249 | [x] | Tales of Zestiria (STEAM) | 15 | 2026-11-09 | 22 | 83% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 250 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 15 | 2026-11-09 | 22 | 78% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 251 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 252 | [x] | Styx: Master of Shadows (EPIC) | 14 | 2026-11-23 | 40 | 50% |  |
| 253 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 29 | 83% |  |
| 254 | [x] | Human Fall Flat (STEAM) | 14 | 2026-10-29 | 29 | 53% |  |
| 255 | [x] | This War of Mine (STEAM) | 14 | 2026-11-17 | 29 | 50% |  |
| 256 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 14 | 2026-11-27 | 28 | 61% |  |
| 257 | [x] | SWORN (STEAM) | 14 | 2026-11-09 | 28 | 100% |  |
| 258 | [x] | Car Mechanic Simulator 2018 (STEAM) | 14 | 2026-11-09 | 25 | 92% |  |
| 259 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 14 | 2026-11-09 | 24 | 89% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 260 | [x] | Nex Machina (STEAM) | 14 | 2026-11-09 | 23 | 94% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 261 | [x] | Capcom Fighting Collection (STEAM) | 14 | 2026-11-09 | 21 | 81% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 262 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 263 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 264 | [x] | Spark the Electric Jester (STEAM) | 14 | 2026-11-13 | 20 | 77% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 265 | [x] | Ys: Memories of Celceta (STEAM) | 14 | 2026-11-27 | 20 | 67% |  |
| 266 | [x] | Spooky's Jump Scare Mansion (STEAM) | 13 | 2026-11-25 | 29 | 55% |  |
| 267 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 13 | 2026-11-09 | 28 | 94% |  |
| 268 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 28 | 100% |  |
| 269 | [x] | Legacy of Kain: Defiance Remastered (STEAM) | 13 | 2026-11-24 | 27 | 75% |  |
| 270 | [x] | Castle in the Clouds (STEAM) | 13 | 2026-11-09 | 26 | 68% |  |
| 271 | [x] | MX Bikes (STEAM) | 13 | 2026-11-09 | 26 | 96% |  |
| 272 | [x] | Katana ZERO (GOG) | 13 | 2026-11-24 | 25 | 60% |  |
| 273 | [x] | Scrap Mechanic (STEAM) | 13 | 2026-11-09 | 23 | 78% |  |
| 274 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 23 | 73% |  |
| 275 | [x] | Decktamer (STEAM) | 13 | 2026-11-26 | 22 | 70% |  |
| 276 | [x] | Horny Villa (STEAM) | 13 | 2026-11-09 | 22 | 84% |  |
| 277 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 278 | [x] | Shift At Midnight (STEAM) | 13 | 2026-11-09 | 21 | 90% |  |
| 279 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 70% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 280 | [x] | War of Dots (STEAM) | 13 | 2026-11-27 | 21 | 70% | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 281 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 94% |  |
| 282 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 2026-11-09 | 20 | 85% |  |
| 283 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-11-16 | 20 | 93% |  |
| 284 | [x] | Turbo Overkill (STEAM) | 13 | 2026-11-09 | 20 | 100% |  |
| 285 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 12 | 2026-11-13 | 28 | 67% |  |
| 286 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-24 | 24 | 64% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 287 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 24 | 64% |  |
| 288 | [x] | Sonic Superstars (STEAM) | 12 | 2026-11-21 | 23 | 75% |  |
| 289 | [x] | 12 is Better Than 6 (STEAM) | 12 | 2026-11-09 | 22 | 73% |  |
| 290 | [x] | Forgive Me Father (STEAM) | 12 | 2026-11-15 | 22 | 67% |  |
| 291 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 292 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 293 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 12 | 2026-11-09 | 20 | 67% |  |
| 294 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 295 | [x] | Hitman: Contracts (STEAM) | 12 | 2026-11-23 | 20 | 67% |  |
| 296 | [x] | GRIP: Combat Racing (STEAM) | 11 | 2026-11-09 | 32 | 81% |  |
| 297 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 29 | 92% |  |
| 298 | [x] | Blaster Master Zero (STEAM) | 11 | 2026-11-11 | 27 | 89% |  |
| 299 | [x] | Overlord (STEAM) | 11 | 2026-11-08 | 26 | 39% |  |
| 300 | [x] | Antichamber (STEAM) | 11 | 2026-11-18 | 25 | 75% |  |
| 301 | [x] | SKALD: Against the Black Priory (STEAM) | 11 | 2026-11-09 | 25 | 96% |  |
| 302 | [x] | Alan Wake's American Nightmare (EPIC) | 11 | 2026-11-09 | 24 | n/a |  |
| 303 | [x] | HITMAN World of Assassination (STEAM) | 11 | 2026-11-09 | 24 | 76% |  |
| 304 | [x] | Ready or Not (STEAM) | 11 | 2026-11-09 | 23 | 73% |  |
| 305 | [x] | Lost Castle 2 (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 306 | [x] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 2026-11-18 | 21 | 75% |  |
| 307 | [x] | Cruelty Squad (STEAM) | 11 | 2026-11-09 | 21 | 82% |  |
| 308 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 309 | [x] | Another World: 20th Anniversary Edition (GOG) | 11 | 2026-11-21 | 20 | 69% |  |
| 310 | [x] | The Stanley Parable (STEAM) | 11 | 2026-11-13 | 20 | 75% |  |
| 311 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 29 | 91% |  |
| 312 | [x] | Intravenous 2 (STEAM) | 10 | 2026-11-09 | 26 | 95% |  |
| 313 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 10 | 2026-11-09 | 24 | 89% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 314 | [x] | Tiny Glade (STEAM) | 10 | 2026-11-09 | 23 | 53% |  |
| 315 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 10 | 2026-11-10 | 22 | 75% |  |
| 316 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 22 | 87% |  |
| 317 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 318 | [x] | DiRT 4 (STEAM) | 10 | 2026-11-09 | 20 | 100% |  |
| 319 | [x] | Haydee (STEAM) | 10 | 2026-11-09 | 20 | 83% |  |
| 320 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 321 | [x] | Pillars of Eternity (STEAM) | 10 | 2026-11-21 | 20 | 100% |  |
| 322 | [x] | Secret of Mana (STEAM) | 10 | 2026-11-18 | 20 | 70% |  |
| 323 | [x] | Batman™: Arkham Origins (GOG) | 9 | 2026-11-09 | 22 | 88% |  |
| 324 | [x] | Evoland (STEAM) | 9 | 2026-11-11 | 22 | n/a |  |
| 325 | [x] | Guacamelee! Gold Edition (STEAM) | 9 | 2026-11-11 | 22 | 69% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 326 | [x] | Need for Speed: Undercover (STEAM) | 9 | 2026-11-11 | 22 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 327 | [x] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 9 | 2026-11-17 | 20 | 33% |  |
| 328 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 27% |  |
| 329 | [x] | UNDEFEATED (STEAM) | 9 | 2026-11-09 | 20 | 70% |  |
| 330 | [x] | Ultrapool (STEAM) | 9 | 2026-11-09 | 20 | n/a |  |
| 331 | [x] | Rayman Origins (GOG) | 8 | 2026-11-09 | 22 | 50% |  |
| 332 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 8 | 2026-11-01 | 22 | n/a |  |
| 333 | [x] | GRANDIA HD Remaster (STEAM) | 8 | 2026-11-09 | 22 | 93% |  |
| 334 | [x] | Aperture Desk Job (STEAM) | 8 | 2026-11-03 | 21 | n/a |  |
| 335 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 8 | 2026-11-09 | 20 | 71% |  |
| 336 | [x] | Soul's Remnant (STEAM) | 8 | 2026-11-11 | 20 | n/a |  |
| 337 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 23 | 52% |  |
| 338 | [x] | Lust Goddess (STEAM) | 7 | 2026-11-09 | 21 | 64% |  |
| 339 | [x] | WORLD OF FINAL FANTASY (STEAM) | 7 | 2026-11-09 | 21 | 82% |  |
| 340 | [x] | Mina the Hollower (GOG) | 7 | 2026-10-28 | 20 | 74% |  |
| 341 | [x] | CULTIC (STEAM) | 7 | 2026-11-09 | 20 | 53% |  |
| 342 | [x] | Legend of Grimrock 2 (STEAM) | 7 | 2026-11-09 | 20 | 92% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 343 | [x] | Crimzon Clover World EXplosion (STEAM) | 6 | 2026-11-09 | 23 | 86% |  |
| 344 | [x] | Life is Strange Remastered (STEAM) | 5 | 2026-11-09 | 20 | 88% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
