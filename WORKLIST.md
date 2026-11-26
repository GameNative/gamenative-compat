# GameNative compatibility worklist

Generated: `2026-11-26T04:15:13.976Z` · Ratings since: `2026-08-28T04:15:13.976Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Probably does not work | 180 |
| Fix shipped, waiting for ratings | 17 |
| First launch fails | 278 |
| Mixed | 451 |
| Works | 1032 |
| Total | 2090 |

## Does not work (132)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 208 | 246 | 85% (since fix) | Does not open (91%) | 39% | today | 34% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 2 | [ ] | Slay the Spire (STEAM) | 111 | 146 | 76% (14d) | Does not open (83%) | 43% | today | 33% | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 3 | [ ] | Rocket League® (EPIC) | 82 | 94 | 87% (14d) | Does not open (81%) | 29% | today | 27% | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 4 | [ ] | Buckshot Roulette (STEAM) | 47 | 67 | 70% (14d) | Does not open (69%) | 50% | today | 43% | [#558](https://github.com/GameNative/gamenative-compat/issues/558) |
| 5 | [ ] | Melvor Idle 2: A RuneScape Adventure (STEAM) | 41 | 45 | 91% (14d) | Does not open (94%) | 43% | today | 41% | [#543](https://github.com/GameNative/gamenative-compat/issues/543) |
| 6 | [ ] | Horizon Chase Turbo (EPIC) | 33 | 40 | 83% (14d) | Does not open (82%) | 51% | today | 43% | [#546](https://github.com/GameNative/gamenative-compat/issues/546) |
| 7 | [ ] | Mark of the Deep (EPIC) | 31 | 40 | 78% (14d) | Does not open (90%) | 27% | today | 23% | [#549](https://github.com/GameNative/gamenative-compat/issues/549) |
| 8 | [ ] | DREDGE (EPIC) | 30 | 36 | 83% (14d) | Does not open (79%) | 50% | today | 44% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 9 | [ ] | Borderlands 2 (EPIC) | 27 | 29 | 93% (14d) | Does not open (81%) | 46% | today | 44% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 10 | [x] 2026-10-18 | Project Zomboid (STEAM) | 64 | 73 | 88% (since fix) | Does not open (66%) | 35% | today | 35% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 11 | [ ] | Path of Exile (STEAM) | 21 | 25 | 84% (14d) | Does not open (88%) | 26% | 1d ago | 24% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 12 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 21 | 28 | 75% (14d) | Does not open (97%) | 36% | today | 19% | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 13 | [ ] | Hogwarts Legacy (EPIC) | 20 | 22 | 91% (14d) | Does not open (75%) | 40% | today | 35% | [#537](https://github.com/GameNative/gamenative-compat/issues/537) |
| 14 | [ ] | Bloons TD 6 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (80%) | 33% | today | 28% | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 15 | [ ] | Dead Island 2 (EPIC) | 20 | 20 | 100% (last 20) | Does not open (87%) | 43% | 1d ago | 31% | [#552](https://github.com/GameNative/gamenative-compat/issues/552) |
| 16 | [ ] | Saints Row 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | 29% | today | 30% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 17 | [ ] | Driver: Parallel Lines (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | 35% | today | 38% | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 18 | [ ] | Metro: Last Light Redux (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | 29% | 1d ago | 29% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 19 | [ ] | Castlevania Anniversary Collection (EPIC) | 18 | 20 | 90% (last 20) | Does not open (75%) | 42% | today | 34% | [#556](https://github.com/GameNative/gamenative-compat/issues/556) |
| 20 | [ ] | Mafia II (Classic) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | 10% | today | 12% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 21 | [ ] | Batman™ Arkham Asylum Game of the Year Edition (EPIC) | 14 | 20 | 70% (last 20) | Does not open (78%) | 46% | today | 39% |  |
| 22 | [ ] | Saints Row 2 (GOG) | 18 | 20 | 90% (last 20) | Does not open (91%) | 33% | 2d ago | 32% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 23 | [ ] | Sifu (EPIC) | 15 | 20 | 75% (last 20) | Does not open (70%) | 39% | 2d ago | 35% | [#535](https://github.com/GameNative/gamenative-compat/issues/535) |
| 24 | [ ] | BioShock Remastered (EPIC) | 14 | 20 | 70% (last 20) | Does not open (67%) | 48% | today | 49% | [#547](https://github.com/GameNative/gamenative-compat/issues/547) |
| 25 | [ ] | Until Then (STEAM) | 18 | 20 | 90% (last 20) | Does not open (88%) | 55% | 1d ago | 44% | [#559](https://github.com/GameNative/gamenative-compat/issues/559) |
| 26 | [ ] | Bad Cheese (EPIC) | 16 | 20 | 80% (last 20) | Does not open (94%) | 43% | today | 32% | [#560](https://github.com/GameNative/gamenative-compat/issues/560) |
| 27 | [ ] | Vampire Survivors (EPIC) | 17 | 20 | 85% (last 20) | Does not open (65%) | 33% | 1d ago | 33% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 28 | [ ] | River City Girls (EPIC) | 14 | 20 | 70% (last 20) | Does not open (50%) | 46% | today | 37% | [#550](https://github.com/GameNative/gamenative-compat/issues/550) |
| 29 | [ ] | VRChat (STEAM) | 15 | 20 | 75% (last 20) | Does not open (74%) | 37% | today | 35% | [#562](https://github.com/GameNative/gamenative-compat/issues/562) |
| 30 | [ ] | skate. (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 10% | 1d ago | 10% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 31 | [ ] | STAR WARS™ Knights of the Old Republic™ II: The Sith Lords™ (STEAM) | 16 | 20 | 80% (last 20) | No graphics (60%) | 44% | today | 39% |  |
| 32 | [ ] | Call of Duty: Black Ops II (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 43% | 1d ago | 42% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 33 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 14 | 20 | 70% (last 20) | Does not open (61%) | 43% | today | 38% |  |
| 34 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 59% | 7d ago | 57% | [#553](https://github.com/GameNative/gamenative-compat/issues/553) |
| 35 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 18 | 20 | 90% (last 20) | Does not open (86%) | 50% | 1d ago | 52% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 36 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 47% | 2d ago | 43% | [#548](https://github.com/GameNative/gamenative-compat/issues/548) |
| 37 | [ ] | Forza Horizon 4 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (43%) | 33% | 3d ago | 24% | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 38 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 16 | 20 | 80% (last 20) | Does not open (88%) | 34% | today | 30% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 39 | [ ] | Teenage Mutant Ninja Turtles: Shredder's Revenge (EPIC) | 15 | 20 | 75% (last 20) | Does not open (83%) | 48% | 3d ago | 42% | [#551](https://github.com/GameNative/gamenative-compat/issues/551) |
| 40 | [ ] | Art of Rally (EPIC) | 14 | 20 | 70% (last 20) | Does not open (79%) | 30% | today | 31% |  |
| 41 | [ ] | Mortal Kombat 11 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (68%) | 58% | 1d ago | 64% |  |
| 42 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (91%) | 16% | 12d ago | 14% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 43 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (76%) | 6% | 11d ago | 7% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 44 | [ ] | Kenshi (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | 7% | today | 5% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 45 | [ ] | Fall Guys (EPIC) | 20 | 20 | 100% (last 20) | Does not open (67%) | 3% | 3d ago | 4% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 46 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (71%) | 36% | 7d ago | 27% | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 47 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | 54% | today | 52% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 48 | [ ] | Metro 2033 Redux (EPIC) | 14 | 20 | 70% (last 20) | Does not open (67%) | 31% | 2d ago | 32% | [#561](https://github.com/GameNative/gamenative-compat/issues/561) |
| 49 | [ ] | Happy Wheels (STEAM) | 18 | 20 | 90% (last 20) | No graphics (52%) | 48% | today | 46% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 50 | [ ] | Detroit: Become Human (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | 50% | 1d ago | 50% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 51 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 7% | 2d ago | 8% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 52 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (73%) | 17% | today | 17% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 53 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 15 | 20 | 75% (last 20) | Does not open (62%) | 45% | today | 40% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 54 | [ ] | Breath of Fire IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | 8% | 6d ago | 9% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 55 | [ ] | The Witcher: Enhanced Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (75%) | 8% | 4d ago | 9% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 56 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (71%) | 8% | 11d ago | 10% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 57 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | 7% | 25d ago | 8% | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 58 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (93%) | 6% | 8d ago | 0% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 59 | [ ] | Call of Duty® (STEAM) | 17 | 20 | 85% (last 20) | Does not open (63%) | 0% | 5d ago | 0% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 60 | [ ] | MECCHA CHAMELEON (STEAM) | 15 | 20 | 75% (last 20) | Does not open (69%) | 40% | 8d ago | 39% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 61 | [ ] | CPM 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (88%) | 3% | today | 3% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 62 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 52% | 10d ago | 50% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 63 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (82%) | 10% | 4d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 64 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (83%) | 12% | 17d ago | 13% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 65 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (88%) | 56% | 2d ago | 50% | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 66 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (74%) | 40% | 1d ago | 41% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 67 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (67%) | 10% | 3d ago | n/a | [#536](https://github.com/GameNative/gamenative-compat/issues/536) |
| 68 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | 46% | 5d ago | 44% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 69 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (84%) | 55% | 5d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 70 | [ ] | Blood Omen: Legacy of Kain (GOG) | 16 | 20 | 80% (last 20) | No graphics (57%) | 58% | 7d ago | 58% | [#539](https://github.com/GameNative/gamenative-compat/issues/539) |
| 71 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (77%) | 5% | 2d ago | 5% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 72 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 0% | today | 0% | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 73 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (55%) | 18% | 8d ago | 18% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 74 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (91%) | 22% | 1d ago | 22% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 75 | [ ] | The Wolf Among Us (STEAM) | 16 | 20 | 80% (last 20) | Does not open (68%) | 16% | today | 17% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 76 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (64%) | 22% | 14d ago | 19% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 77 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | 50% | 3d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 78 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (85%) | 0% | 11d ago | 0% | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 79 | [ ] | Half-Life: Blue Shift (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | 47% | 9d ago | 50% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 80 | [ ] | Rivals of Aether II (STEAM) | 16 | 20 | 80% (last 20) | Does not open (53%) | 20% | 1d ago | 9% | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 81 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 38% | 3d ago | 40% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 82 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | 0% | 18d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 83 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | 10% | 13d ago | 10% | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 84 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | 59% | 12d ago | 56% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 85 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (88%) | 10% | 11d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 86 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (48%) | 48% | 5d ago | 45% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 87 | [ ] | Black Mesa (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 28% | 4d ago | 29% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 88 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 10% | 14d ago | 11% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 89 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 3% | 2d ago | 2% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 90 | [ ] | A Plague Tale: Innocence (EPIC) | 14 | 20 | 70% (last 20) | Does not open (70%) | 46% | 3d ago | 41% | [#557](https://github.com/GameNative/gamenative-compat/issues/557) |
| 91 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 19 | 20 | 95% (last 20) | Does not open (85%) | 45% | 9d ago | 50% | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 92 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (81%) | 18% | 3d ago | 20% | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 93 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (70%) | 24% | 19d ago | 20% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 94 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | Does not open (60%) | 29% | 5d ago | 28% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 95 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 17 | 20 | 85% (last 20) | Does not open (61%) | 29% | 4d ago | 25% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 96 | [ ] | Umamusume: Pretty Derby (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 50% | 6d ago | 55% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 97 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (50%) | 59% | 7d ago | 66% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 98 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 55% | 1d ago | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 99 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (60%) | 50% | 15d ago | 42% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 100 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | 45% | 15d ago | 45% | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 101 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 0% | 26d ago | 0% | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 102 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | 31% | 3d ago | 30% | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 103 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 33% | 5d ago | 35% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 104 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (71%) | 8% | 39d ago | 9% | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 105 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (64%) | 0% | today | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 106 | [ ] | Aliens vs. Predator (STEAM) | 17 | 20 | 85% (last 20) | Does not open (73%) | 29% | 4d ago | 30% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 107 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (63%) | 40% | 6d ago | 40% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 108 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (61%) | 31% | 2d ago | 25% | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 109 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 3% | 4d ago | 3% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 110 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 21% | 6d ago | 15% | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 111 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | 31% | today | 39% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 112 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (89%) | 39% | today | 36% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 113 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 7% | 32d ago | 8% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 114 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (96%) | 40% | 24d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 115 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 55% | 5d ago | 50% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 116 | [ ] | Lost Planet: Extreme Condition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (80%) | 50% | 11d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 117 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (55%) | 38% | 14d ago | 23% | [#540](https://github.com/GameNative/gamenative-compat/issues/540) |
| 118 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 18% | 3d ago | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 119 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 50% | 4d ago | 50% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 120 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (52%) | 54% | 29d ago | 47% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 121 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | 24% | 26d ago | 21% | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 122 | [ ] | OneShot (STEAM) | 15 | 20 | 75% (last 20) | Does not open (94%) | 15% | 5d ago | 20% | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 123 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (88%) | 43% | 4d ago | 40% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 124 | [ ] | Darksiders Warmastered Edition (EPIC) | 17 | 20 | 85% (last 20) | Does not open (82%) | 35% | 1d ago | 31% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 125 | [ ] | Maneater (EPIC) | 17 | 20 | 85% (last 20) | Does not open (73%) | 25% | 3d ago | 21% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 126 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | 40% | 15d ago | 27% | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 127 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (58%) | 54% | 14d ago | 54% | [#554](https://github.com/GameNative/gamenative-compat/issues/554) |
| 128 | [ ] | Ghostwire Tokyo (EPIC) | 14 | 20 | 70% (last 20) | Does not open (90%) | 38% | 2d ago | 38% | [#544](https://github.com/GameNative/gamenative-compat/issues/544) |
| 129 | [ ] | Bongo Cat (STEAM) | 16 | 20 | 80% (last 20) | Does not open (91%) | 56% | 5d ago | 48% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 130 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (54%) | 31% | 11d ago | 33% | [#541](https://github.com/GameNative/gamenative-compat/issues/541) |
| 131 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 14 | 20 | 70% (last 20) | Does not open (96%) | 29% | 2d ago | 26% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 132 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (67%) | 33% | 21d ago | 20% | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |

## Probably does not work (180)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Counter-Strike 2 (STEAM) | 56 | 86 | 65% (since fix) | Does not open (68%) | 55% | today | 55% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 2 | [ ] | Absolute Drift (EPIC) | 21 | 31 | 68% (14d) | No graphics (60%) | 40% | today | 32% | [#555](https://github.com/GameNative/gamenative-compat/issues/555) |
| 3 | [ ] | Metro 2033 Redux (STEAM) | 14 | 22 | 64% (14d) | Does not open (71%) | 43% | today | 43% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 4 | [ ] | Owlboy (STEAM) | 13 | 24 | 54% (14d) | Does not open (80%) | 54% | today | 51% | [#545](https://github.com/GameNative/gamenative-compat/issues/545) |
| 5 | [ ] | Bully: Scholarship Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 26% | today | 13% |  |
| 6 | [ ] | theHunter Classic (STEAM) | 20 | 20 | 100% (last 20) | No graphics (92%) | n/a | 22d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 7 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 12 | 20 | 60% (last 20) | Does not open (78%) | 50% | 1d ago | 48% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 8 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 27 | 48 | 56% (since fix) | Does not open (72%) | 57% | today | 56% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 9 | [ ] | To The Moon (GOG) | 18 | 20 | 90% (last 20) | Does not open (86%) | n/a | 23d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 10 | [ ] | Garry's Mod (STEAM) | 16 | 28 | 57% (since fix) | Does not open (80%) | 47% | today | 45% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 11 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | n/a | 17d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 12 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 10 | 20 | 50% (last 20) | Does not open (71%) | 39% | today | 40% |  |
| 13 | [ ] | MudRunner (EPIC) | 13 | 20 | 65% (last 20) | Does not open (65%) | 48% | today | 39% |  |
| 14 | [ ] | Catherine Classic (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (40%) | 47% | 1d ago | 42% |  |
| 15 | [ ] | DOOM 64 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (62%) | 41% | today | 34% |  |
| 16 | [ ] | Cat Quest (EPIC) | 11 | 20 | 55% (last 20) | Does not open (47%) | 40% | today | 38% |  |
| 17 | [ ] | Sonic Adventure™ 2  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 45% | today | 38% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 18 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 11 | 17 | 65% (since fix) | Does not open (91%) | 51% | today | 49% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 19 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 16 | 24 | 67% (since fix) | Does not open (79%) | 42% | 3d ago | 43% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 20 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 46d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 21 | [ ] | PAYDAY: The Heist (STEAM) | 16 | 20 | 80% (last 20) | Does not open (81%) | n/a | 1d ago | n/a |  |
| 22 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 8 | 14 | 57% (since fix) | Does not open (82%) | 59% | today | 60% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 23 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (39%) | n/a | 5d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 24 | [ ] | Darksiders Warmastered Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 43% | 3d ago | 35% |  |
| 25 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 12d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 26 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 11 | 20 | 55% (last 20) | Does not open (69%) | 46% | today | 42% |  |
| 27 | [ ] | Door Kickers 2 (STEAM) | 18 | 20 | 90% (last 20) | No graphics (85%) | n/a | 3d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 28 | [ ] | Hi-Fi RUSH (STEAM) | 13 | 20 | 65% (last 20) | Does not open (77%) | 45% | today | 46% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 29 | [ ] | Gorilla Tag (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 13% | 1d ago | 8% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 30 | [ ] | Deskrawl: Idle ARPG (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | n/a | 15d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 31 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 30d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 32 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (49%) | 48% | today | 37% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 33 | [ ] | Last Epoch (STEAM) | 11 | 20 | 55% (last 20) | Does not open (82%) | 57% | today | 64% |  |
| 34 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (100%) | n/a | 3d ago | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 35 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (79%) | 54% | 5d ago | 52% |  |
| 36 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | No graphics (59%) | n/a | 29d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 37 | [ ] | Counter-Strike (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 35% | 1d ago | 33% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 38 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | No graphics (38%) | 44% | 4d ago | 38% |  |
| 39 | [ ] | Phasmophobia (STEAM) | 11 | 20 | 55% (last 20) | Does not open (56%) | 50% | today | 44% |  |
| 40 | [ ] | Transistor (STEAM) | 5 | 10 | 50% (since fix) | Does not open (72%) | 35% | today | 20% | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 41 | [ ] | Call of Duty: Black Ops II - Zombies (STEAM) | 5 | 10 | 50% (since fix) | Does not open (72%) | 58% | 1d ago | 63% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 42 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (87%) | n/a | 19d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 43 | [ ] | Deliver At All Costs (EPIC) | 13 | 20 | 65% (last 20) | Does not open (61%) | 39% | 2d ago | 43% | [#538](https://github.com/GameNative/gamenative-compat/issues/538) |
| 44 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 27d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 45 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 12 | 20 | 60% (last 20) | Does not open (87%) | 35% | 6d ago | 21% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 46 | [ ] | Counter-Strike:Global Offensive (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 56% | 3d ago | 56% |  |
| 47 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | n/a | 9d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 48 | [ ] | System Shock 2: 25th Anniversary Remaster (EPIC) | 10 | 20 | 50% (last 20) | Does not open (83%) | 45% | today | 40% |  |
| 49 | [ ] | Stumble Guys (STEAM) | 12 | 20 | 60% (last 20) | Does not open (72%) | 57% | today | 56% |  |
| 50 | [ ] | Saints Row IV Re-Elected (EPIC) | 10 | 20 | 50% (last 20) | No graphics (50%) | 38% | 1d ago | 35% |  |
| 51 | [ ] | Brutal Legend (GOG) | 16 | 20 | 80% (last 20) | Does not open (75%) | n/a | today | n/a |  |
| 52 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (70%) | n/a | 24d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 53 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 21d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 54 | [ ] | Rise of the Tomb Raider: 20 Year Celebration (EPIC) | 13 | 20 | 65% (last 20) | Does not open (73%) | 41% | 2d ago | 37% |  |
| 55 | [ ] | CODE VEIN (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | 20% | 10d ago | 13% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 56 | [ ] | No More Heroes (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 38% | today | 30% |  |
| 57 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 48% | today | 46% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 58 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (71%) | 21% | 1d ago | 18% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 59 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | n/a | 35d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 60 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | n/a | 4d ago | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 61 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 15d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 62 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (74%) | n/a | 23d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 63 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | n/a | today | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 64 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | n/a | 11d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 65 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | 12d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 66 | [ ] | Dead Space 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (63%) | 32% | 1d ago | 28% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 67 | [ ] | Borderlands GOTY (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 45% | today | 50% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 68 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (63%) | n/a | 43d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 69 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 44d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 70 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (96%) | n/a | 24d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 71 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 7d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 72 | [ ] | Northgard: Definitive Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | n/a | today | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 73 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | n/a | 12d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 74 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (57%) | n/a | 11d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 75 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 35% | 9d ago | 32% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 76 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 36% | 1d ago | 33% |  |
| 77 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 57% | 2d ago | 61% |  |
| 78 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | n/a | 46d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 79 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 43d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 80 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | n/a | 12d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 81 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (50%) | n/a | 2d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 82 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (75%) | n/a | 1d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 83 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | n/a | 27d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 84 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 29d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 85 | [ ] | Alpha Protocol (STEAM) | 16 | 20 | 80% (last 20) | No graphics (56%) | n/a | 1d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 86 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 21d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 87 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | n/a | 18d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 88 | [ ] | Grim Dawn (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | n/a | 2d ago | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 89 | [ ] | Metro 2033 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (65%) | 40% | 5d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 90 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 12d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 91 | [ ] | Borderlands 2 RU (STEAM) | 18 | 20 | 90% (last 20) | Does not open (58%) | n/a | 9d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 92 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | 8d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 93 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 17d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 94 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 29d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 95 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (63%) | 55% | 22d ago | 50% |  |
| 96 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 25d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 97 | [ ] | Pathway (EPIC) | 19 | 20 | 95% (last 20) | Does not open (59%) | n/a | 2d ago | n/a | [#298](https://github.com/GameNative/gamenative-compat/issues/298) |
| 98 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 24d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 99 | [ ] | Beholder (EPIC) | 18 | 20 | 90% (last 20) | Does not open (61%) | n/a | 5d ago | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 100 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | n/a | 48d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 101 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | n/a | 5d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 102 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | n/a | today | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 103 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (58%) | n/a | 1d ago | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 104 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (64%) | n/a | 52d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 105 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (76%) | n/a | 2d ago | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 106 | [ ] | DOOM Eternal (STEAM) | 16 | 20 | 80% (last 20) | Does not open (66%) | n/a | 1d ago | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 107 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | n/a | 10d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 108 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (54%) | n/a | 31d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 109 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 13 | 20 | 65% (last 20) | Does not open (88%) | n/a | 1d ago | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 110 | [ ] | Hollow Knight: Silksong (GOG) | 10 | 20 | 50% (last 20) | Does not open (68%) | 45% | 4d ago | 44% |  |
| 111 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (56%) | n/a | 19d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 112 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 21d ago | n/a |  |
| 113 | [ ] | Super Meat Boy Forever (EPIC) | 10 | 20 | 50% (last 20) | Does not open (83%) | 31% | 6d ago | 26% |  |
| 114 | [ ] | The Survivalists (STEAM) | 17 | 20 | 85% (last 20) | Does not open (95%) | n/a | today | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 115 | [ ] | Utopia Must Fall (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | n/a | 2d ago | n/a | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 116 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | n/a | 16d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 117 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 14d ago | n/a |  |
| 118 | [ ] | Lucid Blocks (STEAM) | 11 | 20 | 55% (last 20) | Does not open (94%) | 58% | 6d ago | 52% |  |
| 119 | [ ] | Blood West (EPIC) | 11 | 20 | 55% (last 20) | Does not open (100%) | 31% | today | 29% |  |
| 120 | [ ] | Goat Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 50% | today | 52% |  |
| 121 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 27d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 122 | [ ] | Turing Complete (STEAM) | 16 | 20 | 80% (last 20) | Does not open (79%) | n/a | today | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 123 | [ ] | POSTAL: Brain Damaged (STEAM) | 15 | 20 | 75% (last 20) | Does not open (91%) | n/a | today | n/a |  |
| 124 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Graphics glitches (38%) | n/a | 4d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 125 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 14d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 126 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 28d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 127 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 21d ago | n/a |  |
| 128 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 21d ago | n/a |  |
| 129 | [ ] | Mafia: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 33% | 1d ago | 32% |  |
| 130 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 50% | 1d ago | 58% | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 131 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Controller issues (36%) | n/a | 7d ago | n/a |  |
| 132 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | Does not open (43%) | n/a | 16d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 133 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | n/a | 6d ago | n/a |  |
| 134 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | n/a | 8d ago | n/a | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 135 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 13 | 20 | 65% (last 20) | Does not open (55%) | 25% | 10d ago | 25% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 136 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 45% | 14d ago | n/a |  |
| 137 | [ ] | Mortal Shell (EPIC) | 13 | 20 | 65% (last 20) | Does not open (50%) | 24% | 7d ago | 20% |  |
| 138 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 13 | 20 | 65% (last 20) | Does not open (94%) | n/a | today | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 139 | [ ] | Hitman 2: Silent Assassin (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 39% | 3d ago | 38% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 140 | [ ] | Drop Duchy (EPIC) | 12 | 20 | 60% (last 20) | Does not open (100%) | 9% | today | n/a |  |
| 141 | [ ] | HOT WHEELS UNLEASHED™ (EPIC) | 12 | 20 | 60% (last 20) | No graphics (50%) | 36% | 2d ago | 32% |  |
| 142 | [ ] | Dying Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (77%) | 44% | 3d ago | 35% |  |
| 143 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 10 | 20 | 50% (last 20) | Does not open (90%) | 42% | 4d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 144 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | 13d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 145 | [ ] | Songs of Conquest (EPIC) | 14 | 20 | 70% (last 20) | Does not open (67%) | n/a | today | n/a |  |
| 146 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | n/a | 38d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 147 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (82%) | n/a | 6d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 148 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (71%) | 57% | 11d ago | 67% |  |
| 149 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (63%) | 45% | 12d ago | n/a |  |
| 150 | [ ] | FINAL FANTASY VII REMAKE INTERGRADE (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 42% | 1d ago | 42% |  |
| 151 | [ ] | Romancing SaGa -Minstrel Song- Remastered (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (100%) | n/a | 4d ago | n/a |  |
| 152 | [ ] | Sid Meier's Civilization VI (EPIC) | 13 | 20 | 65% (last 20) | Does not open (58%) | 54% | 2d ago | 48% |  |
| 153 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 26% | 26d ago | 26% |  |
| 154 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (58%) | n/a | 3d ago | n/a |  |
| 155 | [ ] | Crying Suns (EPIC) | 12 | 20 | 60% (last 20) | No graphics (56%) | n/a | 3d ago | n/a |  |
| 156 | [ ] | Sacred Gold (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | n/a | 7d ago | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 157 | [ ] | DAEMON X MACHINA (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 33% | today | 25% |  |
| 158 | [ ] | Football Manager 2024 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (91%) | 58% | 1d ago | 50% |  |
| 159 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | 42% | 15d ago | 40% |  |
| 160 | [ ] | Minit (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | n/a | 1d ago | n/a |  |
| 161 | [ ] | LET IT DIE (STEAM) | 12 | 20 | 60% (last 20) | Does not open (94%) | n/a | 4d ago | n/a |  |
| 162 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (81%) | n/a | today | n/a |  |
| 163 | [ ] | Chasm (GOG) | 12 | 20 | 60% (last 20) | No graphics (50%) | n/a | 11d ago | n/a |  |
| 164 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | n/a | 3d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 165 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | n/a | 7d ago | n/a |  |
| 166 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Does not open (44%) | n/a | 17d ago | n/a |  |
| 167 | [ ] | Turnip Boy Robs a Bank (EPIC) | 12 | 20 | 60% (last 20) | Does not open (73%) | 33% | 1d ago | 36% | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 168 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 21d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 169 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 11 | 20 | 55% (last 20) | Does not open (100%) | 36% | 4d ago | 30% |  |
| 170 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 54% | 5d ago | 59% |  |
| 171 | [ ] | Hitman: Absolution (GOG) | 10 | 20 | 50% (last 20) | Does not open (82%) | n/a | 8d ago | n/a |  |
| 172 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 50% | 16d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 173 | [ ] | Sandustry (STEAM) | 11 | 20 | 55% (last 20) | Does not open (76%) | n/a | today | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 174 | [ ] | Allumeria (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | n/a | 4d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 175 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | n/a | 14d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 176 | [ ] | LEGO® MARVEL's Avengers (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 32% | 1d ago | 29% |  |
| 177 | [ ] | A Plague Tale: Innocence (GOG) | 10 | 20 | 50% (last 20) | Does not open (92%) | n/a | 1d ago | n/a |  |
| 178 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (last 20) | No graphics (54%) | 50% | 13d ago | n/a |  |
| 179 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | n/a | 20d ago | n/a |  |
| 180 | [ ] | Delver (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 11% | 1d ago | 6% |  |

## Fix shipped, waiting for ratings (17)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | Hogwarts Legacy (STEAM) | n/a | 1 | 0 | today | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 2 | Trackmania (STEAM) | n/a | 1 | 0 | today | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 3 | Max Payne 3 (STEAM) | 2026-11-04 | 6 | 6 | today | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 4 | Peggle Deluxe (STEAM) | 2026-10-29 | 7 | 3 | 2d ago | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 5 | Red Dead Redemption (STEAM) | 2026-11-04 | 2 | 2 | 9d ago | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 6 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 8 | 8 | 6d ago | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 7 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 4 | 4 | 4d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 8 | Scott Pilgrim vs The World (STEAM) | n/a | 1 | 0 | today | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 9 | Watch_Dogs (STEAM) | n/a | 6 | 5 | today | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 10 | XCOM: Enemy Unknown (STEAM) | n/a | 2 | 1 | today | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 11 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 2 | 2 | 2d ago | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 12 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 2 | 2 | 3d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 13 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 5 | 5 | 5d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 14 | Need for Speed™ (STEAM) | 2026-11-04 | 2 | 2 | 2d ago | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 15 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 2 | 2 | 4d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 16 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 3 | 3 | today | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 17 | Assassin's Creed Odyssey (STEAM) | n/a | 1 | 1 | 4d ago | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |

## Works, but the first launch usually fails (278)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Half-Life (STEAM) | 83 | 117 | 71% (14d) | Does not open (60%) | 70% | today | 68% |  |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 80 | 99 | 81% (14d) | Does not open (60%) | 95% | today | 96% |  |
| 3 | [ ] | Grand Theft Auto V Legacy (STEAM) | 106 | 127 | 83% (since fix) | Does not open (87%) | 77% | today | 75% |  |
| 4 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 50 | 65 | 77% (14d) | Does not open (56%) | 83% | today | 83% |  |
| 5 | [ ] | Portal (STEAM) | 49 | 78 | 63% (14d) | Does not open (38%) | 88% | today | 87% |  |
| 6 | [ ] | ROB RUN (STEAM) | 42 | 56 | 75% (14d) | Does not open (86%) | 66% | today | 66% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 7 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 34 | 50 | 68% (14d) | Does not open (60%) | 64% | today | 61% |  |
| 8 | [ ] | Valheim (STEAM) | 50 | 88 | 57% (since fix) | No graphics (55%) | 81% | today | 82% |  |
| 9 | [ ] | Selaco (STEAM) | 32 | 51 | 63% (14d) | Does not open (88%) | 64% | today | 61% |  |
| 10 | [ ] | MONSTER HUNTER RISE (STEAM) | 30 | 55 | 55% (14d) | Does not open (84%) | 61% | today | 62% |  |
| 11 | [ ] | No Man's Sky (STEAM) | 41 | 79 | 52% (since fix) | Controller issues (60%) | 79% | today | 78% |  |
| 12 | [ ] | Probably Stolen (STEAM) | 25 | 42 | 60% (14d) | Does not open (61%) | 84% | today | 81% |  |
| 13 | [ ] | ELDEN RING (STEAM) | 19 | 25 | 76% (14d) | Does not open (87%) | 64% | today | 64% |  |
| 14 | [ ] | Euro Truck Simulator 2 (STEAM) | 19 | 37 | 51% (14d) | Does not open (65%) | 61% | 1d ago | 60% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 15 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 19 | 20 | 95% (last 20) | Does not open (38%) | 91% | 1d ago | 90% |  |
| 16 | [ ] | BeamNG.drive (STEAM) | 18 | 25 | 72% (14d) | Does not open (76%) | 63% | 1d ago | 59% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 17 | [ ] | Baldur's Gate 3 (STEAM) | 18 | 30 | 60% (14d) | Does not open (67%) | 80% | today | 81% |  |
| 18 | [ ] | Red Dead Redemption 2 (STEAM) | 28 | 33 | 85% (since fix) | Does not open (95%) | 86% | today | 87% |  |
| 19 | [ ] | Overcooked! 2 (EPIC) | 17 | 22 | 77% (14d) | Does not open (92%) | 62% | today | 58% |  |
| 20 | [ ] | Fallout 3: Game of the Year Edition (GOG) | 16 | 32 | 50% (14d) | Does not open (49%) | 74% | today | 75% |  |
| 21 | [ ] | Team Fortress 2 (STEAM) | 15 | 26 | 58% (14d) | Does not open (67%) | 76% | today | 75% |  |
| 22 | [ ] | Grand Theft Auto: Vice City (STEAM) | 15 | 21 | 71% (14d) | Does not open (36%) | 81% | today | 80% |  |
| 23 | [ ] | Pathogenic (STEAM) | 14 | 20 | 70% (14d) | Does not open (85%) | 64% | today | 62% |  |
| 24 | [ ] | RimWorld (STEAM) | 14 | 28 | 50% (14d) | Does not open (49%) | 80% | today | 77% |  |
| 25 | [ ] | Resident Evil 4 (2005) (STEAM) | 14 | 20 | 70% (14d) | Does not open (78%) | 73% | 1d ago | 71% |  |
| 26 | [ ] | Fallout: New Vegas PCR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | 67% | today | 62% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 27 | [ ] | Dead Space (STEAM) | 16 | 20 | 80% (last 20) | Does not open (64%) | 77% | today | 76% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 28 | [ ] | Noita (STEAM) | 13 | 22 | 59% (14d) | Does not open (59%) | 78% | today | 77% |  |
| 29 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 16 | 20 | 80% (last 20) | Does not open (77%) | 64% | today | 67% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 30 | [ ] | Grand Theft Auto V (EPIC) | 19 | 20 | 95% (last 20) | Does not open (88%) | 77% | today | 76% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 31 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 17 | 20 | 85% (last 20) | Does not open (60%) | 89% | today | 88% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 32 | [ ] | Tales of ARISE (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (73%) | 85% | 1d ago | 83% |  |
| 33 | [ ] | Look Outside (STEAM) | 12 | 23 | 52% (14d) | Controller issues (65%) | 89% | today | 90% |  |
| 34 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 12 | 21 | 57% (14d) | Controller issues (53%) | 67% | 1d ago | 62% |  |
| 35 | [ ] | Alabaster Dawn (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (48%) | 87% | 1d ago | 89% |  |
| 36 | [ ] | Clair Obscur: Expedition 33 (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (40%) | 76% | 2d ago | 76% |  |
| 37 | [ ] | Cry of Fear (STEAM) | 14 | 20 | 70% (last 20) | Does not open (47%) | 68% | 2d ago | 70% |  |
| 38 | [ ] | Barony (STEAM) | 13 | 20 | 65% (last 20) | Does not open (78%) | 79% | today | 78% |  |
| 39 | [ ] | DOOM (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 86% | today | 86% |  |
| 40 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (90%) | 89% | 5d ago | 88% |  |
| 41 | [ ] | Deadlock (STEAM) | 15 | 20 | 75% (last 20) | Does not open (51%) | 80% | 4d ago | 83% |  |
| 42 | [ ] | Rune Factory 3 Special (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | 100% | today | 100% |  |
| 43 | [ ] | Loftia (STEAM) | 13 | 20 | 65% (last 20) | Does not open (94%) | 62% | 1d ago | 65% |  |
| 44 | [ ] | Quake (STEAM) | 12 | 20 | 60% (last 20) | Does not open (54%) | 67% | today | 61% |  |
| 45 | [ ] | Mass Effect™ Legendary Edition (STEAM) | 15 | 28 | 54% (since fix) | Does not open (83%) | 83% | 1d ago | 84% |  |
| 46 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 14 | 26 | 54% (since fix) | Controller issues (79%) | 70% | 1d ago | 72% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 47 | [ ] | Monster Hunter: World (STEAM) | 10 | 20 | 50% (14d) | Does not open (53%) | 78% | today | 76% |  |
| 48 | [ ] | Library Of Ruina (STEAM) | 11 | 20 | 55% (last 20) | Does not open (74%) | 87% | today | 87% |  |
| 49 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (60%) | 92% | 1d ago | 93% |  |
| 50 | [ ] | Welcome to Elderfield (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 70% | today | 70% |  |
| 51 | [ ] | Palworld (STEAM) | 11 | 20 | 55% (last 20) | Does not open (72%) | 85% | today | 84% |  |
| 52 | [ ] | 80's OVERDRIVE (STEAM) | 11 | 20 | 55% (last 20) | No graphics (72%) | 85% | today | 82% |  |
| 53 | [ ] | Batman™: Arkham Origins (STEAM) | 13 | 20 | 65% (last 20) | Does not open (85%) | 67% | today | 64% |  |
| 54 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 17 | 20 | 85% (last 20) | Does not open (85%) | 70% | 1d ago | 71% |  |
| 55 | [ ] | Crypt of the NecroDancer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (47%) | 89% | today | 89% |  |
| 56 | [ ] | OMORI (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | 61% | 1d ago | 58% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 57 | [ ] | Cyberpunk 2077 (GOG) | 11 | 20 | 55% (last 20) | Does not open (73%) | 69% | today | 67% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 58 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (70%) | 95% | 1d ago | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 59 | [ ] | Mortal Kombat X (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 91% | 8d ago | 93% |  |
| 60 | [ ] | Shakedown: Hawaii (STEAM) | 10 | 20 | 50% (last 20) | Does not open (79%) | 78% | today | 77% |  |
| 61 | [ ] | Aniimo (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 74% | 2d ago | 73% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 62 | [ ] | Dressmaker (STEAM) | 12 | 20 | 60% (last 20) | Does not open (56%) | 77% | today | 74% |  |
| 63 | [ ] | Fate/stay night REMASTERED (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | 96% | today | 95% |  |
| 64 | [ ] | Devil May Cry 5 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (81%) | 83% | today | 82% |  |
| 65 | [ ] | DOOM 3: BFG Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 68% | today | 68% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 66 | [ ] | Chained Echoes (GOG) | 15 | 20 | 75% (last 20) | Does not open (62%) | 65% | 1d ago | 59% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 67 | [ ] | Don't Starve Together (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 72% | today | 69% |  |
| 68 | [ ] | Disco Elysium - The Final Cut (EPIC) | 12 | 20 | 60% (last 20) | Does not open (78%) | 91% | 2d ago | 91% |  |
| 69 | [ ] | Resident Evil 7 Biohazard (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 65% | 2d ago | 60% |  |
| 70 | [ ] | Fallout: New Vegas (EPIC) | 16 | 20 | 80% (last 20) | Does not open (59%) | 73% | 5d ago | 71% |  |
| 71 | [ ] | Disgaea 5 Complete (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | 94% | 9d ago | 96% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 72 | [ ] | Asterigos: Curse of the Stars (STEAM) | 16 | 20 | 80% (last 20) | Graphics glitches (73%) | 90% | 4d ago | n/a |  |
| 73 | [ ] | Cave Story+ (STEAM) | 19 | 20 | 95% (last 20) | Does not open (64%) | 76% | 4d ago | 76% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 74 | [ ] | FINAL FANTASY (STEAM) | 12 | 20 | 60% (last 20) | Does not open (78%) | 77% | 3d ago | 75% |  |
| 75 | [ ] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 12 | 20 | 60% (last 20) | Does not open (60%) | 83% | 3d ago | 83% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 76 | [ ] | Mini Motorways (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 65% | 3d ago | 61% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 77 | [ ] | Stardew Valley (GOG) | 10 | 20 | 50% (last 20) | Controller issues (60%) | 88% | 3d ago | 83% |  |
| 78 | [ ] | POSTAL 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | 63% | today | 60% |  |
| 79 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (50%) | 82% | today | 82% |  |
| 80 | [ ] | Little Witch in the Woods (STEAM) | 11 | 20 | 55% (last 20) | Does not open (55%) | 85% | 3d ago | 84% |  |
| 81 | [ ] | Moonstone Island (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (64%) | 81% | today | 79% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 82 | [ ] | Castlevania Dominus Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (91%) | 96% | 4d ago | 95% |  |
| 83 | [ ] | eFootball™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 60% | 8d ago | 59% |  |
| 84 | [ ] | Poppy Playtime (STEAM) | 13 | 20 | 65% (last 20) | Does not open (53%) | 64% | 2d ago | 64% |  |
| 85 | [ ] | Palia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | 72% | 3d ago | 68% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 86 | [ ] | Minecraft Dungeons II (STEAM) | 15 | 20 | 75% (last 20) | Does not open (80%) | 70% | 2d ago | 69% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 87 | [ ] | No, I'm not a Human (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 92% | today | 88% |  |
| 88 | [ ] | PAC-MAN Championship Edition DX+ (STEAM) | 10 | 20 | 50% (last 20) | No graphics (59%) | 65% | 5d ago | 60% |  |
| 89 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 15 | 20 | 75% (last 20) | Does not open (45%) | 86% | 1d ago | 91% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 90 | [ ] | Dota 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 74% | 1d ago | 78% |  |
| 91 | [ ] | Doki Doki Literature Club (STEAM) | 10 | 20 | 50% (last 20) | Does not open (51%) | 83% | 2d ago | 80% |  |
| 92 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (81%) | 72% | 9d ago | 73% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 93 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (62%) | 71% | today | 73% |  |
| 94 | [ ] | TBH: Task Bar Hero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (66%) | 83% | 3d ago | 86% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 95 | [ ] | Titanfall® 2 (STEAM) | 9 | 13 | 69% (since fix) | Does not open (89%) | 68% | 1d ago | 69% |  |
| 96 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 17 | 20 | 85% (last 20) | Controller issues (88%) | 98% | today | 97% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 97 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (76%) | 75% | 8d ago | 67% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 98 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 97% | 7d ago | 96% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 99 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 16 | 20 | 80% (last 20) | Does not open (67%) | 81% | today | 80% |  |
| 100 | [ ] | Ratatan (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | 88% | 5d ago | 86% |  |
| 101 | [ ] | L.A. Noire (STEAM) | 15 | 20 | 75% (last 20) | Does not open (96%) | 65% | today | 59% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 102 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 100% | 3d ago | 100% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 103 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (42%) | 74% | 2d ago | 74% |  |
| 104 | [ ] | Tails of Iron (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 88% | 4d ago | 92% |  |
| 105 | [ ] | Oxygen Not Included (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 73% | 1d ago | 76% |  |
| 106 | [ ] | SONIC X SHADOW GENERATIONS (STEAM) | 10 | 20 | 50% (last 20) | Does not open (79%) | 80% | 2d ago | 79% |  |
| 107 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (44%) | 89% | 3d ago | 91% |  |
| 108 | [ ] | PlateUp! (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 75% | today | 74% |  |
| 109 | [ ] | The Sims™ 4 (STEAM) | 7 | 14 | 50% (since fix) | Does not open (84%) | 67% | 2d ago | 67% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 110 | [ ] | Resident Evil Village (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 83% | today | 84% |  |
| 111 | [ ] | Unturned (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 84% | 2d ago | 84% |  |
| 112 | [ ] | Astral Party  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 83% | 6d ago | 80% |  |
| 113 | [ ] | Minecraft Dungeons (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 74% | 5d ago | 75% |  |
| 114 | [ ] | A Plague Tale: Innocence (STEAM) | 19 | 20 | 95% (last 20) | Does not open (85%) | 70% | 10d ago | 70% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 115 | [ ] | Call of Duty: World at War (STEAM) | 13 | 20 | 65% (last 20) | Does not open (38%) | 72% | 4d ago | 67% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 116 | [ ] | Abiotic Factor (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 84% | 9d ago | 87% |  |
| 117 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | 83% | 17d ago | 83% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 118 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (87%) | 71% | 19d ago | 81% |  |
| 119 | [ ] | Caravan SandWitch (EPIC) | 10 | 20 | 50% (last 20) | Does not open (70%) | 62% | 4d ago | 64% |  |
| 120 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 87% | today | 81% |  |
| 121 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | 82% | 12d ago | 82% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 122 | [ ] | Street Fighter™ 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | 81% | 4d ago | 77% |  |
| 123 | [ ] | Fable - The Lost Chapters (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (46%) | 83% | today | 86% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 124 | [ ] | Watch Dogs 2 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (80%) | 60% | 2d ago | 59% | [#399](https://github.com/GameNative/gamenative-compat/issues/399) |
| 125 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (70%) | 83% | 3d ago | 85% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 126 | [ ] | Sonic Generations (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 67% | 2d ago | 66% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 127 | [ ] | Ultimate Custom Night (STEAM) | 14 | 20 | 70% (last 20) | No graphics (71%) | 62% | today | 58% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 128 | [ ] | Gothic 1 Classic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (58%) | 65% | 2d ago | 66% |  |
| 129 | [ ] | Yakuza: Like a Dragon (STEAM) | 13 | 20 | 65% (last 20) | Does not open (62%) | 71% | today | 76% |  |
| 130 | [ ] | Digimon Survive (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (83%) | 88% | 1d ago | 87% |  |
| 131 | [ ] | Legacy of Kain: Defiance Remastered (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (69%) | 80% | 4d ago | 80% |  |
| 132 | [ ] | OCTOPATH TRAVELER 0 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (77%) | 89% | 1d ago | 93% |  |
| 133 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (86%) | 86% | 8d ago | 89% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 134 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (79%) | 81% | 2d ago | 83% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 135 | [ ] | Supermarket Together (STEAM) | 16 | 20 | 80% (last 20) | Does not open (65%) | 64% | 1d ago | 64% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 136 | [ ] | Stellar Blade™ (STEAM) | 14 | 20 | 70% (last 20) | No graphics (42%) | 83% | 5d ago | 84% |  |
| 137 | [ ] | Max Payne (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (48%) | 82% | 2d ago | 80% |  |
| 138 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 94% | 2d ago | 94% |  |
| 139 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (69%) | 86% | 13d ago | 83% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 140 | [ ] | CrossCode (GOG) | 17 | 20 | 85% (last 20) | Does not open (79%) | 67% | today | 80% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 141 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (88%) | 63% | 15d ago | 67% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 142 | [ ] | Tabletop Simulator (STEAM) | 14 | 20 | 70% (last 20) | Does not open (42%) | 83% | 7d ago | 83% |  |
| 143 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (83%) | 60% | 16d ago | n/a |  |
| 144 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 76% | 2d ago | 77% |  |
| 145 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (66%) | 77% | 2d ago | 73% |  |
| 146 | [ ] | Trailmakers (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | 100% | today | 97% |  |
| 147 | [ ] | Pinball FX (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 68% | 9d ago | 67% |  |
| 148 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (48%) | 77% | today | 76% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 149 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 90% | 19d ago | 88% |  |
| 150 | [ ] | Control Ultimate Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (72%) | 68% | 1d ago | 63% |  |
| 151 | [ ] | Plague Inc: Evolved (STEAM) | 13 | 20 | 65% (last 20) | Does not open (57%) | 67% | 5d ago | 65% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 152 | [ ] | DRAPLINE (STEAM) | 13 | 20 | 65% (last 20) | Does not open (100%) | 94% | today | 93% |  |
| 153 | [ ] | Dishonored 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 66% | today | 61% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 154 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 89% | 1d ago | 89% |  |
| 155 | [ ] | SurrounDead (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (71%) | 90% | today | 92% |  |
| 156 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (57%) | 92% | 4d ago | 90% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 157 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (92%) | 73% | 6d ago | 71% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 158 | [ ] | Changed (STEAM) | 16 | 20 | 80% (last 20) | Does not open (64%) | 61% | today | 58% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 159 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (59%) | 61% | 14d ago | 62% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 160 | [ ] | Gambonanza (STEAM) | 12 | 20 | 60% (last 20) | Does not open (61%) | 90% | today | 88% |  |
| 161 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (46%) | 78% | 1d ago | 76% |  |
| 162 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 69% | 14d ago | 67% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 163 | [ ] | Necesse (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 62% | 4d ago | 62% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 164 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (43%) | 68% | 1d ago | 66% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 165 | [ ] | CLANNAD (STEAM) | 13 | 20 | 65% (last 20) | No graphics (47%) | 86% | today | 90% |  |
| 166 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (82%) | 86% | 7d ago | 89% |  |
| 167 | [ ] | Sonic Lost World (STEAM) | 10 | 20 | 50% (last 20) | No graphics (68%) | 82% | 5d ago | 82% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 168 | [ ] | Yu-Gi-Oh!  Master Duel (STEAM) | 10 | 20 | 50% (last 20) | Does not open (79%) | 68% | today | 68% |  |
| 169 | [ ] | Heavy Rain (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (65%) | 89% | 2d ago | 92% |  |
| 170 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 90% | 36d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 171 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | 88% | 3d ago | 85% |  |
| 172 | [ ] | HELLDIVERS™ (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 63% | 1d ago | 61% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 173 | [ ] | My Summer Car (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 70% | 2d ago | 67% |  |
| 174 | [ ] | One-armed robber (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (71%) | 68% | 1d ago | 62% |  |
| 175 | [ ] | METAL SLUG 3 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (81%) | 67% | 2d ago | 67% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 176 | [ ] | Limbus Company (STEAM) | 11 | 20 | 55% (last 20) | Does not open (82%) | 96% | 1d ago | 95% |  |
| 177 | [ ] | Overwatch® (STEAM) | 8 | 11 | 73% (since fix) | Does not open (61%) | 83% | 3d ago | 81% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 178 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 77% | 7d ago | 75% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 179 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (53%) | 64% | 15d ago | 64% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 180 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (76%) | 68% | today | 67% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 181 | [ ] | Hylics (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (74%) | 90% | 3d ago | 88% |  |
| 182 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (76%) | 100% | 16d ago | n/a |  |
| 183 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 74% | 4d ago | 73% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 184 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (74%) | 93% | 1d ago | 95% |  |
| 185 | [ ] | Tower and Sword of Succubus (STEAM) | 12 | 20 | 60% (last 20) | No graphics (90%) | 79% | today | 73% |  |
| 186 | [ ] | Warframe (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 76% | 2d ago | 77% |  |
| 187 | [ ] | TurretGirls (STEAM) | 12 | 20 | 60% (last 20) | No graphics (77%) | 100% | 6d ago | 100% |  |
| 188 | [ ] | Escape from Duckov (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (68%) | 96% | today | 96% |  |
| 189 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 95% | 15d ago | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 190 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (73%) | 67% | 20d ago | 64% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 191 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (63%) | 79% | 3d ago | 73% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 192 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | 86% | 2d ago | 91% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 193 | [ ] | Return to Monkey Island (STEAM) | 15 | 20 | 75% (last 20) | No graphics (74%) | 72% | 2d ago | 72% |  |
| 194 | [ ] | Capcom Arcade Stadium (STEAM) | 14 | 20 | 70% (last 20) | Does not open (76%) | 71% | today | 80% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 195 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 13 | 20 | 65% (last 20) | Does not open (81%) | 64% | 1d ago | 61% |  |
| 196 | [ ] | Turbo Overkill (STEAM) | 13 | 20 | 65% (last 20) | No graphics (91%) | 100% | 4d ago | 100% |  |
| 197 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (61%) | 73% | 4d ago | 75% |  |
| 198 | [ ] | Maneater (STEAM) | 15 | 20 | 75% (last 20) | Does not open (86%) | 61% | 1d ago | 64% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 199 | [ ] | Jade Empire: Special Edition (GOG) | 15 | 20 | 75% (last 20) | Graphics glitches (56%) | 75% | today | 70% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 200 | [ ] | Subnautica 2 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (44%) | 86% | 1d ago | 83% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 201 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (61%) | 83% | 15d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 202 | [ ] | Dead Island (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 86% | today | 83% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 203 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 75% | 29d ago | 75% |  |
| 204 | [ ] | AER Memories of Old (EPIC) | 14 | 20 | 70% (last 20) | Does not open (86%) | 94% | today | 93% |  |
| 205 | [ ] | Hotline Miami (GOG) | 13 | 20 | 65% (last 20) | Does not open (88%) | 71% | 2d ago | 74% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 206 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (47%) | 91% | today | 90% |  |
| 207 | [ ] | CS2D (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 73% | 3d ago | n/a |  |
| 208 | [ ] | MX Bikes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 96% | 8d ago | 95% |  |
| 209 | [ ] | Invisible, Inc. (STEAM) | 14 | 20 | 70% (last 20) | Does not open (79%) | 92% | 3d ago | n/a |  |
| 210 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 92% | 16d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 211 | [ ] | GOD EATER RESURRECTION (STEAM) | 13 | 20 | 65% (last 20) | Does not open (56%) | 93% | 2d ago | 91% |  |
| 212 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 94% | 2d ago | 100% |  |
| 213 | [ ] | GUILTY GEAR Xrd REV 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | 64% | today | 62% |  |
| 214 | [ ] | No Socks RPG (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (91%) | 93% | today | 93% |  |
| 215 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (64%) | 74% | 14d ago | 78% |  |
| 216 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (82%) | 84% | 9d ago | 83% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 217 | [ ] | Yakuza 0 (GOG) | 13 | 20 | 65% (last 20) | Does not open (73%) | 67% | today | 69% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 218 | [ ] | Capcom Fighting Collection (STEAM) | 13 | 20 | 65% (last 20) | Does not open (83%) | 88% | 6d ago | 88% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 219 | [ ] | SnowRunner (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 72% | 3d ago | 75% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 220 | [ ] | Big Walk (STEAM) | 12 | 20 | 60% (last 20) | Does not open (58%) | 62% | 6d ago | 59% |  |
| 221 | [ ] | BATTLETECH (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 96% | 10d ago | 95% |  |
| 222 | [ ] | Donut Dodo (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 94% | today | 100% |  |
| 223 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (50%) | 88% | 5d ago | 93% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 224 | [ ] | Darksiders (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 77% | 3d ago | 77% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 225 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 92% | today | 91% |  |
| 226 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 78% | 1d ago | 77% |  |
| 227 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 77% | 3d ago | 76% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 228 | [ ] | Spark the Electric Jester (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 77% | 5d ago | 73% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 229 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 94% | 17d ago | 94% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 230 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (45%) | 78% | 1d ago | 75% |  |
| 231 | [ ] | Tales of Zestiria (STEAM) | 13 | 20 | 65% (last 20) | Does not open (75%) | 83% | 3d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 232 | [ ] | SILENT HILL 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 100% | 2d ago | 100% |  |
| 233 | [ ] | Timberborn (STEAM) | 12 | 20 | 60% (last 20) | No graphics (67%) | 100% | 7d ago | 100% |  |
| 234 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 94% | 18d ago | 92% |  |
| 235 | [ ] | Super Battle Golf (STEAM) | 11 | 20 | 55% (last 20) | Does not open (75%) | 89% | 3d ago | 88% |  |
| 236 | [ ] | Secrets of Grindea (STEAM) | 10 | 20 | 50% (last 20) | Does not open (48%) | 84% | 8d ago | 83% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 237 | [ ] | Zero Escape: The Nonary Games (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 68% | 5d ago | 70% |  |
| 238 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 78% | 12d ago | 75% |  |
| 239 | [ ] | Vampyr (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 100% | 1d ago | 100% |  |
| 240 | [ ] | HITMAN World of Assassination (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 76% | today | 74% |  |
| 241 | [ ] | Decktamer (STEAM) | 13 | 20 | 65% (last 20) | Does not open (100%) | 70% | 3d ago | 70% |  |
| 242 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 92% | 37d ago | 92% |  |
| 243 | [ ] | Goose Goose Duck (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 72% | 6d ago | 81% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 244 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 12 | 20 | 60% (last 20) | No graphics (39%) | 80% | 9d ago | 82% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 245 | [ ] | Mafia II (Classic) (GOG) | 12 | 20 | 60% (last 20) | Does not open (100%) | 70% | 3d ago | 70% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 246 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 71% | 13d ago | 69% |  |
| 247 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 74% | 17d ago | 69% |  |
| 248 | [ ] | Sons Of The Forest (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 76% | 11d ago | 73% |  |
| 249 | [ ] | Forgive Me Father (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 71% | 2d ago | 62% |  |
| 250 | [ ] | Deus Ex™ GOTY Edition (GOG) | 11 | 20 | 55% (last 20) | No graphics (47%) | 92% | 4d ago | 90% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 251 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 92% | today | 91% |  |
| 252 | [ ] | Rollout Inline (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 75% | 6d ago | 75% |  |
| 253 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 71% | 10d ago | 83% |  |
| 254 | [ ] | Disgaea 4 Complete+ (STEAM) | 12 | 20 | 60% (last 20) | No graphics (40%) | 93% | 3d ago | 92% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 255 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 82% | 8d ago | 82% |  |
| 256 | [ ] | Hitman: Contracts (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (82%) | 69% | 3d ago | 67% |  |
| 257 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (100%) | 93% | 1d ago | 92% |  |
| 258 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 87% | 3d ago | 85% |  |
| 259 | [ ] | Cat Mail Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 91% | 2d ago | 90% |  |
| 260 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 67% | today | 77% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 261 | [ ] | CRUEL (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 85% | 11d ago | 84% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 262 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 93% | 11d ago | 100% |  |
| 263 | [ ] | Eastern Exorcist (EPIC) | 10 | 20 | 50% (last 20) | No graphics (50%) | 65% | 1d ago | 56% |  |
| 264 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (40%) | 69% | 14d ago | 82% |  |
| 265 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 75% | 10d ago | 75% |  |
| 266 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | Does not open (53%) | 82% | 11d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 267 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 64% | 9d ago | 64% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 268 | [ ] | 12 is Better Than 6 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (40%) | 75% | today | 80% |  |
| 269 | [ ] | Assetto Corsa Competizione (STEAM) | 10 | 20 | 50% (last 20) | Does not open (89%) | 83% | 3d ago | 82% |  |
| 270 | [ ] | BioShock 2 Remastered (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 77% | 6d ago | 74% |  |
| 271 | [ ] | Cruelty Squad (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 83% | 2d ago | 82% |  |
| 272 | [ ] | Sort Them Ducks (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (64%) | 100% | 3d ago | 100% |  |
| 273 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 90% | 5d ago | 88% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 274 | [ ] | Command & Conquer™ Red Alert™ 3 (STEAM) | 10 | 20 | 50% (last 20) | No graphics (38%) | 93% | 4d ago | 92% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 275 | [ ] | Dungeon Siege (STEAM) | 10 | 20 | 50% (last 20) | No graphics (50%) | 100% | 5d ago | 100% |  |
| 276 | [ ] | Nioh: Complete Edition (STEAM) | 10 | 20 | 50% (last 20) | No graphics (64%) | 100% | today | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 277 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 100% | 4d ago | 100% |  |
| 278 | [ ] | Pillars of Eternity (STEAM) | 10 | 20 | 50% (last 20) | Does not open (40%) | 100% | 5d ago | 100% |  |

## Recently recovered (352)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Grim Dawn (STEAM) | 436 | 2026-11-08 | 519 | 73% |  |
| 2 | [x] | Half-Life (STEAM) | 373 | 2026-11-09 | 634 | 70% |  |
| 3 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 266 | 2026-11-14 | 426 | 73% |  |
| 4 | [x] | MONSTER HUNTER RISE (STEAM) | 228 | 2026-11-17 | 524 | 61% |  |
| 5 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 219 | 2026-11-09 | 373 | 64% |  |
| 6 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 216 | 2026-11-09 | 290 | 89% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 7 | [x] | Alan Wake (STEAM) | 211 | 2026-11-14 | 240 | 82% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 8 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 182 | 2026-11-09 | 225 | 51% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 9 | [x] | BeamNG.drive (STEAM) | 174 | 2026-11-09 | 218 | 63% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 10 | [x] | Geometry Dash (STEAM) | 161 | 2026-11-11 | 451 | 67% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 11 | [x] | DRAGON BALL FighterZ (STEAM) | 159 | 2026-11-01 | 207 | 87% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 12 | [x] | OMORI (STEAM) | 156 | 2026-11-09 | 198 | 61% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 13 | [x] | Call of Duty: Black Ops (STEAM) | 143 | 2026-11-13 | 170 | 24% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 14 | [x] | BioShock (STEAM) | 139 | 2026-11-09 | 284 | 69% |  |
| 15 | [x] | Team Fortress 2 (STEAM) | 137 | 2026-11-09 | 239 | 76% |  |
| 16 | [x] | Spelunky 2 (STEAM) | 137 | 2026-11-01 | 192 | 88% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 17 | [x] | Sid Meier's Civilization V (STEAM) | 135 | 2026-11-10 | 150 | 64% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 18 | [x] | Minecraft Dungeons II (STEAM) | 133 | 2026-11-09 | 152 | 70% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 19 | [x] | Castlevania Advance Collection (STEAM) | 126 | 2026-11-09 | 202 | 86% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 20 | [x] | Prototype (STEAM) | 126 | 2026-11-11 | 193 | 56% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 21 | [x] | Euro Truck Simulator 2 (STEAM) | 121 | 2026-11-23 | 214 | 61% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 22 | [x] | Aniimo (STEAM) | 117 | 2026-11-09 | 158 | 74% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 23 | [x] | Mirror's Edge (STEAM) | 105 | 2026-11-09 | 163 | 68% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 24 | [x] | Cave Story+ (STEAM) | 101 | 2026-11-09 | 110 | 76% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 25 | [x] | Assassin's Creed II (STEAM) | 100 | 2026-11-10 | 105 | 72% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 26 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 96 | 2026-11-09 | 135 | 90% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 27 | [x] | The Witcher: Enhanced Edition (STEAM) | 94 | 2026-11-09 | 116 | 76% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 28 | [x] | Necesse (STEAM) | 94 | 2026-11-22 | 104 | 62% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 29 | [x] | Moonstone Island (STEAM) | 87 | 2026-11-09 | 113 | 81% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 30 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 83 | 2026-11-15 | 128 | 91% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 31 | [x] | Fallout: New Vegas PCR (STEAM) | 83 | 2026-11-20 | 112 | 67% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 32 | [x] | FINAL FANTASY XIII-2 (STEAM) | 80 | 2026-11-09 | 83 | 73% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 33 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 77 | 2026-11-09 | 125 | 75% |  |
| 34 | [x] | DOOM 3: BFG Edition (STEAM) | 77 | 2026-11-09 | 119 | 68% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 35 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 77 | 2026-11-23 | 99 | 64% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 36 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 76 | 2026-11-09 | 100 | 98% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 37 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 75 | 2026-11-09 | 118 | 76% |  |
| 38 | [x] | Vital Shell (STEAM) | 73 | 2026-11-09 | 123 | 87% |  |
| 39 | [x] | Brawlhalla (STEAM) | 70 | 2026-11-09 | 136 | 71% |  |
| 40 | [x] | Order of the Sinking Star (STEAM) | 69 | 2026-11-09 | 107 | 68% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 41 | [x] | The Sims™ 4 (STEAM) | 69 | 2026-11-09 | 94 | 67% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 42 | [x] | Psychonauts (STEAM) | 68 | 2026-11-09 | 139 | 92% |  |
| 43 | [x] | Cyberpunk 2077 (GOG) | 68 | 2026-11-09 | 93 | 69% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 44 | [x] | Ballionaire (STEAM) | 67 | 2026-11-09 | 118 | 84% |  |
| 45 | [x] | Grand Theft Auto V (EPIC) | 66 | 2026-11-09 | 70 | 77% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 46 | [x] | Stardew Valley (GOG) | 65 | 2026-11-11 | 117 | 88% |  |
| 47 | [x] | Dota 2 (STEAM) | 64 | 2026-11-09 | 99 | 74% |  |
| 48 | [x] | Age of Empires II: Definitive Edition (STEAM) | 64 | 2026-11-10 | 83 | 65% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 49 | [x] | American Truck Simulator (STEAM) | 63 | 2026-11-09 | 104 | 66% |  |
| 50 | [x] | Horizon Zero Dawn™ Complete Edition (STEAM) | 63 | 2026-11-25 | 76 | 86% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 51 | [x] | Diablo® IV (STEAM) | 63 | 2026-11-11 | 75 | 83% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 52 | [x] | Disgaea 5 Complete (STEAM) | 63 | 2026-11-09 | 72 | 94% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 53 | [x] | Fable - The Lost Chapters (STEAM) | 62 | 2026-11-09 | 104 | 83% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 54 | [x] | GRID (STEAM) | 62 | 2026-11-21 | 83 | 54% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 55 | [x] | Spyro™ Reignited Trilogy (STEAM) | 60 | 2026-11-09 | 107 | 77% |  |
| 56 | [x] | Need for Speed: Hot Pursuit (STEAM) | 60 | 2026-11-09 | 92 | 76% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 57 | [x] | Quake (STEAM) | 59 | 2026-11-09 | 186 | 67% |  |
| 58 | [x] | Mini Motorways (STEAM) | 59 | 2026-11-09 | 93 | 65% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 59 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 58 | 2026-11-09 | 98 | 92% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 60 | [x] | Poppy Playtime (STEAM) | 58 | 2026-11-09 | 98 | 64% |  |
| 61 | [x] | Gunfire Reborn (STEAM) | 56 | 2026-11-09 | 62 | 86% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 62 | [x] | Borderlands 3 (STEAM) | 55 | 2026-11-09 | 85 | 93% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 63 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 54 | 2026-11-09 | 93 | 67% |  |
| 64 | [x] | FINAL FANTASY XIII (STEAM) | 53 | 2026-11-22 | 513 | 64% |  |
| 65 | [x] | Sovereign Tower (STEAM) | 53 | 2026-11-09 | 111 | 76% |  |
| 66 | [x] | Firewatch (STEAM) | 53 | 2026-11-10 | 105 | 95% |  |
| 67 | [x] | Fallout (STEAM) | 53 | 2026-11-09 | 87 | 60% |  |
| 68 | [x] | Call of Duty: World at War (STEAM) | 53 | 2026-11-09 | 75 | 72% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 69 | [x] | Sonic Generations (STEAM) | 53 | 2026-11-09 | 61 | 67% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 70 | [x] | Caravan SandWitch (EPIC) | 51 | 2026-11-09 | 107 | 62% |  |
| 71 | [x] | A Plague Tale: Innocence (STEAM) | 51 | 2026-11-09 | 54 | 70% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 72 | [x] | eFootball™ (STEAM) | 50 | 2026-11-09 | 75 | 60% |  |
| 73 | [x] | Call of Juarez Gunslinger (STEAM) | 50 | 2026-11-09 | 63 | 63% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 74 | [x] | MIO: Memories in Orbit (STEAM) | 49 | 2026-11-09 | 103 | 94% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 75 | [x] | Moonlighter (EPIC) | 49 | 2026-11-09 | 53 | 95% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 76 | [x] | Darksiders (STEAM) | 48 | 2026-11-09 | 64 | 77% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 77 | [x] | HELLDIVERS™ (STEAM) | 48 | 2026-11-23 | 60 | 63% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 78 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 48 | 2026-11-09 | 54 | 100% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 79 | [x] | Okami HD (STEAM) | 47 | 2026-11-09 | 89 | 96% |  |
| 80 | [x] | Starbound (STEAM) | 47 | 2026-11-09 | 80 | 90% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 81 | [x] | STEINS;GATE (STEAM) | 47 | 2026-11-09 | 76 | 81% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 82 | [x] | METAL SLUG 3 (STEAM) | 47 | 2026-11-24 | 61 | 67% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 83 | [x] | Oxygen Not Included (STEAM) | 45 | 2026-11-11 | 78 | 73% |  |
| 84 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 45 | 2026-11-13 | 75 | 65% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 85 | [x] | TBH: Task Bar Hero (STEAM) | 45 | 2026-11-09 | 71 | 83% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 86 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 45 | 2026-11-17 | 70 | 68% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 87 | [x] | ROB RUN (STEAM) | 45 | 2026-11-17 | 62 | 66% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 88 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 44 | 2026-11-09 | 64 | 70% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 89 | [x] | Overwatch® (STEAM) | 44 | 2026-11-10 | 49 | 83% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 90 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 43 | 2026-11-09 | 73 | 71% |  |
| 91 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 42 | 2026-11-09 | 78 | 85% |  |
| 92 | [x] | Sol Cesto (EPIC) | 42 | 2026-11-09 | 42 | 75% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 93 | [x] | Borderlands: The Pre-Sequel (STEAM) | 39 | 2026-11-09 | 78 | 63% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 94 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 39 | 2026-11-09 | 69 | 83% |  |
| 95 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 39 | 2026-11-09 | 61 | 89% |  |
| 96 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 38 | 2026-11-09 | 63 | 71% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 97 | [x] | Darkest Dungeon® (EPIC) | 37 | 2026-11-09 | 77 | 88% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 98 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 37 | 2026-11-09 | 68 | 86% |  |
| 99 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 37 | 2026-11-09 | 65 | 52% |  |
| 100 | [x] | Sonic Lost World (STEAM) | 37 | 2026-11-09 | 57 | 82% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 101 | [x] | Digimon World: Next Order (STEAM) | 36 | 2026-11-09 | 69 | 87% |  |
| 102 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 36 | 2026-11-09 | 67 | 82% |  |
| 103 | [x] | Age of Empires II (2013) (STEAM) | 36 | 2026-11-09 | 62 | 71% |  |
| 104 | [x] | Aggelos (STEAM) | 36 | 2026-11-09 | 52 | 81% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 105 | [x] | Russian Fishing 4 (STEAM) | 36 | 2026-11-09 | 42 | 68% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 106 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 36 | 2026-11-19 | 38 | 82% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 107 | [x] | Amnesia: The Dark Descent (STEAM) | 35 | 2026-11-09 | 74 | 88% |  |
| 108 | [x] | Street Fighter™ 6 (STEAM) | 35 | 2026-11-09 | 55 | 81% |  |
| 109 | [x] | L.A. Noire (STEAM) | 35 | 2026-11-24 | 45 | 65% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 110 | [x] | CrossCode (GOG) | 35 | 2026-11-09 | 40 | 67% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 111 | [x] | Monster Hunter Wilds (STEAM) | 35 | 2026-11-09 | 36 | 86% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 112 | [x] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 34 | 2026-11-20 | 68 | 17% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 113 | [x] | POSTAL 2 (GOG) | 34 | 2026-11-09 | 66 | 89% |  |
| 114 | [x] | Dead by Daylight (STEAM) | 34 | 2026-11-09 | 38 | 83% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 115 | [x] | Being a DIK (STEAM) | 33 | 2026-11-09 | 75 | 62% |  |
| 116 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 33 | 2026-11-09 | 60 | 76% |  |
| 117 | [x] | COCOON (STEAM) | 32 | 2026-11-09 | 63 | 80% |  |
| 118 | [x] | Ace Attorney Investigations Collection (STEAM) | 32 | 2026-11-09 | 60 | 87% |  |
| 119 | [x] | Sonic Origins (STEAM) | 32 | 2026-11-09 | 59 | 77% |  |
| 120 | [x] | XCOM 2 (STEAM) | 32 | 2026-11-09 | 59 | 70% |  |
| 121 | [x] | SnowRunner (STEAM) | 32 | 2026-11-09 | 43 | 72% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 122 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 31 | 2026-11-09 | 71 | 74% |  |
| 123 | [x] | Hearts of Iron IV (STEAM) | 31 | 2026-11-09 | 67 | 82% |  |
| 124 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 31 | 2026-11-09 | 62 | 89% |  |
| 125 | [x] | Yume Nikki (STEAM) | 31 | 2026-11-20 | 58 | 56% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 126 | [x] | Max Payne (STEAM) | 31 | 2026-11-09 | 53 | 82% |  |
| 127 | [x] | Plague Inc: Evolved (STEAM) | 31 | 2026-11-16 | 49 | 67% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 128 | [x] | Gauntlet™  (STEAM) | 31 | 2026-11-11 | 48 | n/a | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 129 | [x] | FINAL FANTASY VII (2013) (STEAM) | 31 | 2026-11-09 | 47 | 50% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 130 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 31 | 2026-11-09 | 39 | 92% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 131 | [x] | Red Dead Redemption (STEAM) | 31 | 2026-11-09 | 34 | 41% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 132 | [x] | SurrounDead (STEAM) | 30 | 2026-11-09 | 61 | 90% |  |
| 133 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 30 | 2026-11-09 | 54 | 74% |  |
| 134 | [x] | Resident Evil Village (STEAM) | 30 | 2026-11-09 | 51 | 83% |  |
| 135 | [x] | Breathedge (STEAM) | 30 | 2026-11-23 | 47 | 59% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 136 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 30 | 2026-11-09 | 45 | 81% |  |
| 137 | [x] | Journey (STEAM) | 29 | 2026-10-27 | 71 | 83% |  |
| 138 | [x] | Tomb Raider: Anniversary (STEAM) | 29 | 2026-11-09 | 57 | 65% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 139 | [x] | Earthion (STEAM) | 29 | 2026-11-09 | 53 | 100% |  |
| 140 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 29 | 2026-11-09 | 52 | 85% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 141 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 29 | 2026-11-09 | 49 | 73% |  |
| 142 | [x] | Need for Speed™ Rivals (STEAM) | 29 | 2026-11-10 | 44 | 74% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 143 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 77% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 144 | [x] | Prince of Persia: The Sands of Time (STEAM) | 28 | 2026-11-09 | 49 | 78% |  |
| 145 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 28 | 2026-11-09 | 45 | 70% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 146 | [x] | Digimon Survive (STEAM) | 28 | 2026-11-09 | 41 | 88% |  |
| 147 | [x] | Resident Evil Revelations 2 (STEAM) | 27 | 2026-11-09 | 55 | 85% |  |
| 148 | [x] | The Bazaar (STEAM) | 27 | 2026-11-09 | 54 | 78% |  |
| 149 | [x] | Heavy Rain (STEAM) | 27 | 2026-11-09 | 48 | 89% |  |
| 150 | [x] | Hero Siege (STEAM) | 27 | 2026-11-09 | 47 | 83% |  |
| 151 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 27 | 2026-11-09 | 47 | 100% |  |
| 152 | [x] | Secrets of Grindea (STEAM) | 27 | 2026-11-09 | 46 | 84% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 153 | [x] | Yakuza: Like a Dragon (STEAM) | 27 | 2026-11-09 | 43 | 71% |  |
| 154 | [x] | Palia (STEAM) | 27 | 2026-11-09 | 38 | 72% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 155 | [x] | Capcom Arcade Stadium (STEAM) | 27 | 2026-11-09 | 37 | 71% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 156 | [x] | Supermarket Together (STEAM) | 27 | 2026-11-18 | 37 | 64% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 157 | [x] | Hotline Miami (GOG) | 27 | 2026-11-18 | 35 | 71% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 158 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 43 | 68% |  |
| 159 | [x] | Dead Rising 2 (STEAM) | 25 | 2026-11-09 | 41 | 71% |  |
| 160 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-19 | 32 | 90% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 161 | [x] | Skullgirls 2nd Encore (STEAM) | 24 | 2026-11-10 | 62 | 75% |  |
| 162 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 24 | 2026-11-09 | 58 | 79% |  |
| 163 | [x] | Lobotomy Corporation (STEAM) | 24 | 2026-11-09 | 48 | 92% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 164 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 24 | 2026-11-09 | 47 | 55% |  |
| 165 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 24 | 2026-11-09 | 44 | 93% |  |
| 166 | [x] | Cat Mail Co. (STEAM) | 24 | 2026-11-09 | 42 | 91% |  |
| 167 | [x] | Trailmakers (STEAM) | 24 | 2026-11-09 | 42 | 100% |  |
| 168 | [x] | My Summer Car (STEAM) | 24 | 2026-11-09 | 38 | 70% |  |
| 169 | [x] | Ratatan (STEAM) | 24 | 2026-11-09 | 37 | 88% |  |
| 170 | [x] | Chained Echoes (GOG) | 23 | 2026-11-19 | 48 | 65% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 171 | [x] | Deponia (STEAM) | 23 | 2026-11-09 | 45 | 84% |  |
| 172 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 43 | 97% |  |
| 173 | [x] | Big Walk (STEAM) | 23 | 2026-11-09 | 42 | 62% |  |
| 174 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 2026-11-09 | 40 | 81% |  |
| 175 | [x] | Tower and Sword of Succubus (STEAM) | 23 | 2026-11-09 | 40 | 79% |  |
| 176 | [x] | Unturned (STEAM) | 23 | 2026-11-09 | 40 | 84% |  |
| 177 | [x] | Opus Magnum (STEAM) | 23 | 2026-11-09 | 36 | 100% |  |
| 178 | [x] | Gothic II: Gold Classic (STEAM) | 23 | 2026-11-09 | 31 | 77% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 179 | [x] | Jade Empire: Special Edition (GOG) | 23 | 2026-11-09 | 30 | 75% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 180 | [x] | Crab Game (STEAM) | 23 | 2026-11-09 | 27 | 64% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 181 | [x] | Frostpunk (STEAM) | 22 | 2026-11-09 | 49 | 87% |  |
| 182 | [x] | Gambonanza (STEAM) | 22 | 2026-11-09 | 40 | 90% |  |
| 183 | [x] | Control Ultimate Edition (GOG) | 22 | 2026-11-09 | 38 | 68% |  |
| 184 | [x] | Strider (STEAM) | 22 | 2026-11-20 | 38 | 67% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 185 | [x] | Titanfall® 2 (STEAM) | 22 | 2026-11-09 | 38 | 68% |  |
| 186 | [x] | Dishonored 2 (STEAM) | 22 | 2026-11-09 | 34 | 66% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 187 | [x] | Ultimate Custom Night (STEAM) | 22 | 2026-11-19 | 33 | 62% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 188 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 22 | 2026-11-09 | 25 | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 189 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 58 | 97% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 190 | [x] | Prince of Persia (GOG) | 21 | 2026-11-09 | 43 | 73% |  |
| 191 | [x] | Worms W.M.D (STEAM) | 21 | 2026-11-09 | 37 | 100% |  |
| 192 | [x] | Limbus Company (STEAM) | 21 | 2026-11-09 | 34 | 96% |  |
| 193 | [x] | Return to Monkey Island (STEAM) | 21 | 2026-11-09 | 33 | 72% |  |
| 194 | [x] | Changed (STEAM) | 21 | 2026-11-23 | 31 | 61% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 195 | [x] | Goose Goose Duck (STEAM) | 21 | 2026-11-18 | 30 | 72% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 196 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 88% |  |
| 197 | [x] | Tearscape (STEAM) | 21 | 2026-11-09 | 25 | 79% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 198 | [x] | Battle Brothers (STEAM) | 20 | 2026-11-09 | 41 | 80% |  |
| 199 | [x] | One-armed robber (STEAM) | 20 | 2026-11-09 | 36 | 68% |  |
| 200 | [x] | GOD EATER RESURRECTION (STEAM) | 20 | 2026-11-09 | 32 | 93% |  |
| 201 | [x] | Deus Ex™ GOTY Edition (GOG) | 20 | 2026-11-09 | 31 | 92% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 202 | [x] | Maneater (STEAM) | 20 | 2026-11-25 | 31 | 61% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 203 | [x] | Timberborn (STEAM) | 20 | 2026-11-09 | 31 | 100% |  |
| 204 | [x] | CRUEL (STEAM) | 20 | 2026-11-09 | 30 | 85% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 205 | [x] | Dead Island (STEAM) | 20 | 2026-11-09 | 27 | 86% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 206 | [x] | Subnautica 2 (STEAM) | 20 | 2026-11-15 | 26 | 86% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 207 | [x] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 20 | 2026-11-22 | 21 | 69% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 208 | [x] | Mirror's Edge™ (GOG) | 19 | 2026-11-13 | 40 | 83% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 209 | [x] | Wizard of Legend (EPIC) | 19 | 2026-11-09 | 38 | 76% |  |
| 210 | [x] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 2026-11-15 | 38 | 77% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 211 | [x] | Pinball FX Classic (STEAM) | 19 | 2026-11-09 | 36 | 83% |  |
| 212 | [x] | Capcom Fighting Collection 2 (STEAM) | 19 | 2026-11-09 | 35 | 86% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 213 | [x] | Baldur's Gate: Enhanced Edition (GOG) | 19 | 2026-11-26 | 31 | 65% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 214 | [x] | Asterigos: Curse of the Stars (STEAM) | 19 | 2026-11-26 | 31 | 90% |  |
| 215 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 31 | 100% |  |
| 216 | [x] | Torchlight II (EPIC) | 19 | 2026-11-09 | 27 | 84% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 217 | [x] | Dark Sector (STEAM) | 19 | 2026-11-21 | 25 | 83% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 218 | [x] | Crusader Kings III (STEAM) | 19 | 2026-11-18 | 23 | 86% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 219 | [x] | Watch Dogs 2 (EPIC) | 19 | 2026-11-23 | 21 | 60% | [#399](https://github.com/GameNative/gamenative-compat/issues/399) |
| 220 | [x] | Mini Metro (STEAM) | 18 | 2026-11-16 | 34 | 53% |  |
| 221 | [x] | Guildrun Demo (STEAM) | 18 | 2026-11-09 | 33 | 82% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 222 | [x] | Tabletop Simulator (STEAM) | 18 | 2026-11-09 | 31 | 83% |  |
| 223 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 18 | 2026-11-15 | 29 | 64% |  |
| 224 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 2026-11-09 | 29 | 80% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 225 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-11-09 | 27 | 90% |  |
| 226 | [x] | Beyond: Two Souls (STEAM) | 18 | 2026-11-26 | 26 | 61% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 227 | [x] | CarX Street (STEAM) | 18 | 2026-11-09 | 22 | 67% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 228 | [x] | Mafia II: Definitive Edition (GOG) | 18 | 2026-11-15 | 20 | 60% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 229 | [x] | Jade Empire: Special Edition (STEAM) | 18 | 2026-11-09 | 20 | 71% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 230 | [x] | Backpack Battles (STEAM) | 17 | 2026-11-09 | 40 | 89% |  |
| 231 | [x] | Crazy Taxi (STEAM) | 17 | 2026-11-10 | 40 | 69% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 232 | [x] | Counter-Strike: Condition Zero (STEAM) | 17 | 2026-11-11 | 37 | 32% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 233 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 32 | 75% |  |
| 234 | [x] | Mafia II (Classic) (GOG) | 17 | 2026-11-24 | 28 | 70% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 235 | [x] | Nioh: Complete Edition (STEAM) | 17 | 2026-11-23 | 28 | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 236 | [x] | Yakuza 0 (GOG) | 17 | 2026-11-25 | 24 | 67% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 237 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 238 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 16 | 2026-11-09 | 29 | 55% |  |
| 239 | [x] | Moonlight Peaks (STEAM) | 16 | 2026-11-09 | 29 | 76% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 240 | [x] | Invisible, Inc. (STEAM) | 16 | 2026-11-09 | 27 | 92% |  |
| 241 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 16 | 2026-11-09 | 26 | 90% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 242 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 71% |  |
| 243 | [x] | AER Memories of Old (EPIC) | 16 | 2026-11-09 | 24 | 94% |  |
| 244 | [x] | Party Animals (STEAM) | 16 | 2026-11-09 | 24 | 74% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 245 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 246 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 247 | [x] | Flotsam (EPIC) | 15 | 2026-11-20 | 36 | 41% |  |
| 248 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 15 | 2026-11-11 | 35 | 80% |  |
| 249 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 15 | 2026-11-26 | 30 | 91% |  |
| 250 | [x] | Far Far West (STEAM) | 15 | 2026-11-09 | 27 | 50% |  |
| 251 | [x] | Disgaea 4 Complete+ (STEAM) | 15 | 2026-11-09 | 24 | 93% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 252 | [x] | Need for Speed™ Unbound (STEAM) | 15 | 2026-11-09 | 23 | 58% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 253 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 92% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 254 | [x] | Tales of Zestiria (STEAM) | 15 | 2026-11-09 | 22 | 83% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 255 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 15 | 2026-11-09 | 22 | 78% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 256 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 257 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 258 | [x] | Styx: Master of Shadows (EPIC) | 14 | 2026-11-23 | 40 | 52% |  |
| 259 | [x] | sobosuba (STEAM) | 14 | 2026-11-09 | 36 | 80% |  |
| 260 | [x] | Spooky's Jump Scare Mansion (STEAM) | 14 | 2026-11-25 | 30 | 55% |  |
| 261 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 29 | 85% |  |
| 262 | [x] | Human Fall Flat (STEAM) | 14 | 2026-10-29 | 29 | 56% |  |
| 263 | [x] | This War of Mine (STEAM) | 14 | 2026-11-17 | 29 | 49% |  |
| 264 | [x] | SKALD: Against the Black Priory (STEAM) | 14 | 2026-11-09 | 28 | 100% |  |
| 265 | [x] | SWORN (STEAM) | 14 | 2026-11-09 | 28 | 95% |  |
| 266 | [x] | Car Mechanic Simulator 2018 (STEAM) | 14 | 2026-11-09 | 25 | 92% |  |
| 267 | [x] | Nex Machina (STEAM) | 14 | 2026-11-09 | 22 | 88% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 268 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 2026-11-16 | 22 | 82% |  |
| 269 | [x] | Capcom Fighting Collection (STEAM) | 14 | 2026-11-09 | 21 | 88% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 270 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 271 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 272 | [x] | Spark the Electric Jester (STEAM) | 14 | 2026-11-13 | 20 | 77% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 273 | [x] | Overlord (STEAM) | 13 | 2026-11-08 | 29 | 42% |  |
| 274 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 13 | 2026-11-09 | 28 | 94% |  |
| 275 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 28 | 100% |  |
| 276 | [x] | Legacy of Kain: Defiance Remastered (STEAM) | 13 | 2026-11-24 | 27 | 80% |  |
| 277 | [x] | Castle in the Clouds (STEAM) | 13 | 2026-11-09 | 26 | 68% |  |
| 278 | [x] | MX Bikes (STEAM) | 13 | 2026-11-09 | 26 | 96% |  |
| 279 | [x] | Katana ZERO (GOG) | 13 | 2026-11-24 | 25 | 60% |  |
| 280 | [x] | Decktamer (STEAM) | 13 | 2026-11-26 | 23 | 70% |  |
| 281 | [x] | Scrap Mechanic (STEAM) | 13 | 2026-11-09 | 23 | 78% |  |
| 282 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 23 | 76% |  |
| 283 | [x] | Horny Villa (STEAM) | 13 | 2026-11-09 | 22 | 87% |  |
| 284 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 285 | [x] | Shift At Midnight (STEAM) | 13 | 2026-11-09 | 21 | 90% |  |
| 286 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 70% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 287 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 94% |  |
| 288 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 2026-11-09 | 20 | 85% |  |
| 289 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-11-16 | 20 | 92% |  |
| 290 | [x] | Turbo Overkill (STEAM) | 13 | 2026-11-09 | 20 | 100% |  |
| 291 | [x] | CS2D (STEAM) | 12 | 2026-11-24 | 33 | 73% |  |
| 292 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 12 | 2026-11-13 | 28 | 67% |  |
| 293 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-24 | 24 | 64% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 294 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 24 | 64% |  |
| 295 | [x] | Sonic Superstars (STEAM) | 12 | 2026-11-21 | 24 | 74% |  |
| 296 | [x] | 12 is Better Than 6 (STEAM) | 12 | 2026-11-09 | 22 | 75% |  |
| 297 | [x] | Forgive Me Father (STEAM) | 12 | 2026-11-15 | 22 | 71% |  |
| 298 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 299 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 300 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 301 | [x] | Hitman: Contracts (STEAM) | 12 | 2026-11-23 | 20 | 69% |  |
| 302 | [x] | GRIP: Combat Racing (STEAM) | 11 | 2026-11-09 | 32 | 80% |  |
| 303 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 29 | 92% |  |
| 304 | [x] | Blaster Master Zero (STEAM) | 11 | 2026-11-11 | 27 | 90% |  |
| 305 | [x] | Antichamber (STEAM) | 11 | 2026-11-18 | 26 | 75% |  |
| 306 | [x] | Alan Wake's American Nightmare (EPIC) | 11 | 2026-11-09 | 24 | 80% |  |
| 307 | [x] | HITMAN World of Assassination (STEAM) | 11 | 2026-11-09 | 24 | 76% |  |
| 308 | [x] | Ready or Not (STEAM) | 11 | 2026-11-09 | 23 | 76% |  |
| 309 | [x] | Lost Castle 2 (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 310 | [x] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 2026-11-18 | 21 | 71% |  |
| 311 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 11 | 2026-10-27 | 21 | 93% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 312 | [x] | Cruelty Squad (STEAM) | 11 | 2026-11-09 | 21 | 83% |  |
| 313 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 314 | [x] | Another World: 20th Anniversary Edition (GOG) | 11 | 2026-11-21 | 20 | 69% |  |
| 315 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-11-09 | 20 | 62% |  |
| 316 | [x] | The Stanley Parable (STEAM) | 11 | 2026-11-13 | 20 | 75% |  |
| 317 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 28 | 92% |  |
| 318 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 10 | 2026-10-27 | 27 | 83% |  |
| 319 | [x] | Intravenous 2 (STEAM) | 10 | 2026-11-09 | 26 | 95% |  |
| 320 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 10 | 2026-11-09 | 24 | 90% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 321 | [x] | Tiny Glade (STEAM) | 10 | 2026-11-09 | 24 | 62% |  |
| 322 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 22 | 86% |  |
| 323 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 10 | 2026-11-10 | 21 | 75% |  |
| 324 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 325 | [x] | DiRT 4 (STEAM) | 10 | 2026-11-09 | 20 | 100% |  |
| 326 | [x] | Haydee (STEAM) | 10 | 2026-11-09 | 20 | 83% |  |
| 327 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 328 | [x] | Pillars of Eternity (STEAM) | 10 | 2026-11-21 | 20 | 100% |  |
| 329 | [x] | Secret of Mana (STEAM) | 10 | 2026-11-18 | 20 | 70% |  |
| 330 | [x] | Rayman Origins (GOG) | 9 | 2026-11-09 | 24 | 54% |  |
| 331 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 9 | 2026-11-01 | 24 | n/a |  |
| 332 | [x] | Evoland (STEAM) | 9 | 2026-11-11 | 23 | n/a |  |
| 333 | [x] | Batman™: Arkham Origins (GOG) | 9 | 2026-11-09 | 22 | 89% |  |
| 334 | [x] | Guacamelee! Gold Edition (STEAM) | 9 | 2026-11-11 | 22 | 69% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 335 | [x] | Need for Speed: Undercover (STEAM) | 9 | 2026-11-11 | 22 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 336 | [x] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 9 | 2026-11-17 | 20 | 33% |  |
| 337 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 27% |  |
| 338 | [x] | UNDEFEATED (STEAM) | 9 | 2026-11-09 | 20 | 73% |  |
| 339 | [x] | Ultrapool (STEAM) | 9 | 2026-11-09 | 20 | n/a |  |
| 340 | [x] | WORLD OF FINAL FANTASY (STEAM) | 8 | 2026-11-09 | 23 | 82% |  |
| 341 | [x] | Aperture Desk Job (STEAM) | 8 | 2026-11-03 | 21 | n/a |  |
| 342 | [x] | GRANDIA HD Remaster (STEAM) | 8 | 2026-11-09 | 21 | 92% |  |
| 343 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 8 | 2026-11-09 | 20 | 71% |  |
| 344 | [x] | Soul's Remnant (STEAM) | 8 | 2026-11-11 | 20 | n/a |  |
| 345 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 23 | 53% |  |
| 346 | [x] | Lust Goddess (STEAM) | 7 | 2026-11-09 | 21 | 71% |  |
| 347 | [x] | SCP – Containment Breach (STEAM) | 7 | 2026-10-27 | 21 | 91% |  |
| 348 | [x] | Mina the Hollower (GOG) | 7 | 2026-10-28 | 20 | 74% |  |
| 349 | [x] | CULTIC (STEAM) | 7 | 2026-11-09 | 20 | 53% |  |
| 350 | [x] | Legend of Grimrock 2 (STEAM) | 7 | 2026-11-09 | 20 | 92% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 351 | [x] | Crimzon Clover World EXplosion (STEAM) | 6 | 2026-11-09 | 22 | 86% |  |
| 352 | [x] | Life is Strange Remastered (STEAM) | 5 | 2026-11-09 | 20 | 88% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
