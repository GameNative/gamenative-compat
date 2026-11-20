# GameNative compatibility worklist

Generated: `2026-11-20T04:15:12.430Z` · Ratings since: `2026-08-22T04:15:12.430Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 125 |
| Probably does not work | 183 |
| Fix shipped, waiting for ratings | 15 |
| First launch fails | 305 |
| Mixed | 477 |
| Works | 1034 |
| Total | 2139 |

## Does not work (125)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 159 | 181 | 88% (14d) | Does not open (83%) | 49% | today | 24% (drop) | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 152 | 175 | 87% (since fix) | Does not open (91%) | 43% | today | 36% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 3 | [ ] | Rocket League® (EPIC) | 81 | 93 | 87% (14d) | Does not open (81%) | 41% | today | 28% | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 4 | [ ] | Hogwarts Legacy (STEAM) | 39 | 41 | 95% (14d) | Does not open (71%) | 31% | today | 16% | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 5 | [ ] | DREDGE (EPIC) | 37 | 40 | 93% (14d) | Does not open (76%) | 57% | 2d ago | 46% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 6 | [ ] | Melvor Idle 2: A RuneScape Adventure (STEAM) | 33 | 34 | 97% (14d) | Does not open (96%) | 34% | today | 33% | [#543](https://github.com/GameNative/gamenative-compat/issues/543) |
| 7 | [ ] | Horizon Chase Turbo (EPIC) | 29 | 35 | 83% (14d) | Does not open (84%) | 59% | today | 47% |  |
| 8 | [x] 2026-10-18 | Project Zomboid (STEAM) | 59 | 65 | 91% (since fix) | Does not open (65%) | 42% | today | 37% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 9 | [ ] | Path of Exile (STEAM) | 22 | 24 | 92% (14d) | Does not open (89%) | 24% | today | 20% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 10 | [ ] | Bloons TD 6 (EPIC) | 21 | 22 | 95% (14d) | Does not open (77%) | 38% | today | 22% | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 11 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 21 | 21 | 100% (14d) | Does not open (96%) | 34% | 5d ago | 20% | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 12 | [ ] | Metro: Last Light Redux (STEAM) | 20 | 20 | 100% (last 20) | Does not open (91%) | 24% | 1d ago | 28% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 13 | [ ] | Saints Row 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | 34% | 4d ago | 30% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 14 | [ ] | Borderlands 2 (EPIC) | 18 | 20 | 90% (14d) | Does not open (80%) | 52% | 1d ago | 47% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 15 | [ ] | Sifu (EPIC) | 18 | 22 | 82% (14d) | Does not open (72%) | 47% | today | 36% | [#535](https://github.com/GameNative/gamenative-compat/issues/535) |
| 16 | [ ] | BioShock Remastered (EPIC) | 16 | 22 | 73% (14d) | Does not open (67%) | 59% | 1d ago | 53% |  |
| 17 | [ ] | Saints Row 2 (GOG) | 16 | 21 | 76% (14d) | Does not open (90%) | 40% | 2d ago | 40% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 18 | [ ] | Owlboy (STEAM) | 15 | 20 | 75% (14d) | Does not open (81%) | 48% | today | 43% | [#545](https://github.com/GameNative/gamenative-compat/issues/545) |
| 19 | [ ] | Mafia II (Classic) (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 8% | 2d ago | 12% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 20 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 14 | 20 | 70% (last 20) | Does not open (78%) | 53% | today | 43% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 21 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (76%) | 0% | 11d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 22 | [ ] | Call of Duty: Black Ops II (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 35% | 1d ago | 37% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 23 | [ ] | Castlevania Anniversary Collection (EPIC) | 16 | 20 | 80% (last 20) | Does not open (79%) | 59% | today | 33% (drop) |  |
| 24 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (77%) | 57% | today | 45% |  |
| 25 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 10 | 14 | 71% (since fix) | Does not open (90%) | 42% | today | 48% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 26 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (92%) | 23% | 6d ago | 15% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 27 | [ ] | skate. (STEAM) | 18 | 20 | 90% (last 20) | Does not open (78%) | 12% | 1d ago | 14% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 28 | [ ] | Vampire Survivors (EPIC) | 17 | 20 | 85% (last 20) | Does not open (62%) | 43% | today | 30% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 29 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (78%) | 0% | 5d ago | 0% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 30 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 37% | 2d ago | 30% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 31 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 16 | 20 | 80% (last 20) | No graphics (46%) | 33% | 1d ago | 40% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 32 | [ ] | Forza Horizon 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (47%) | 48% | 2d ago | 21% (drop) | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 33 | [ ] | Hogwarts Legacy (EPIC) | 14 | 20 | 70% (last 20) | Does not open (76%) | 51% | 1d ago | 40% | [#537](https://github.com/GameNative/gamenative-compat/issues/537) |
| 34 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 52% | today | 67% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 35 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (71%) | 20% | 1d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 36 | [ ] | Fall Guys (EPIC) | 20 | 20 | 100% (last 20) | Does not open (70%) | 12% | today | 6% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 37 | [ ] | Kenshi (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 4% | 1d ago | 0% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 38 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 12% | 8d ago | 6% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 39 | [ ] | The Witcher: Enhanced Edition (GOG) | 18 | 20 | 90% (last 20) | Does not open (75%) | 9% | today | 12% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 40 | [ ] | Breath of Fire IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (64%) | 14% | today | 11% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 41 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (70%) | 15% | 1d ago | 20% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 42 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | 0% | 5d ago | 0% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 43 | [ ] | Trackmania (STEAM) | 16 | 20 | 80% (last 20) | Does not open (82%) | 21% | 4d ago | 31% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 44 | [ ] | CPM 2 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 8% | 4d ago | 5% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 45 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (93%) | 10% | 2d ago | n/a | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 46 | [ ] | Call of Duty® (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | 0% | 3d ago | 0% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 47 | [ ] | Deliver At All Costs (EPIC) | 14 | 20 | 70% (last 20) | Does not open (60%) | 48% | 4d ago | 42% | [#538](https://github.com/GameNative/gamenative-compat/issues/538) |
| 48 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | 7% | 19d ago | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 49 | [ ] | MECCHA CHAMELEON (STEAM) | 15 | 20 | 75% (last 20) | Does not open (68%) | 40% | 2d ago | 29% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 50 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (58%) | 42% | 4d ago | n/a | [#536](https://github.com/GameNative/gamenative-compat/issues/536) |
| 51 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (88%) | 20% | 11d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 52 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | 23% | 6d ago | 30% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 53 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (79%) | 13% | 11d ago | 18% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 54 | [ ] | Borderlands GOTY (STEAM) | 16 | 20 | 80% (last 20) | Does not open (94%) | 38% | today | 47% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 55 | [ ] | Blood Omen: Legacy of Kain (GOG) | 16 | 20 | 80% (last 20) | No graphics (57%) | 54% | 1d ago | 50% | [#539](https://github.com/GameNative/gamenative-compat/issues/539) |
| 56 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (83%) | 46% | 2d ago | 47% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 57 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (77%) | 11% | 5d ago | 8% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 58 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | 0% | 6d ago | 0% | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 59 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (54%) | 27% | 2d ago | 18% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 60 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (88%) | 50% | 7d ago | 56% | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 61 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (68%) | 24% | 8d ago | 27% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 62 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 26% | 1d ago | 35% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 63 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (82%) | 0% | 5d ago | n/a | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 64 | [ ] | Half-Life: Blue Shift (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 36% | 3d ago | 45% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 65 | [ ] | Rivals of Aether II (STEAM) | 16 | 20 | 80% (last 20) | Does not open (56%) | 42% | 3d ago | 6% (drop) | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 66 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (73%) | 41% | 8d ago | 27% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 67 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | 50% | 41d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 68 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 30% | 11d ago | 38% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 69 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | 10% | 7d ago | 10% | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 70 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 38% | 6d ago | 50% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 71 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 37% | 8d ago | 15% (drop) | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 72 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (45%) | 45% | 15d ago | 42% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 73 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 19 | 20 | 95% (last 20) | Does not open (85%) | 45% | 3d ago | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 74 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | 29% | 3d ago | 27% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 75 | [ ] | Black Mesa (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 24% | 2d ago | 31% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 76 | [ ] | Watch_Dogs (STEAM) | 14 | 20 | 70% (last 20) | Does not open (87%) | 36% | today | 47% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 77 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 8% | 18d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 78 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 18% | 29d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 79 | [ ] | XCOM: Enemy Unknown (STEAM) | 18 | 20 | 90% (last 20) | Does not open (71%) | 18% | 6d ago | n/a | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 80 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (73%) | 33% | 13d ago | 23% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 81 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | Does not open (63%) | 25% | 13d ago | 31% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 82 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 55% | 9d ago | 40% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 83 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (80%) | 36% | 9d ago | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 84 | [ ] | Umamusume: Pretty Derby (STEAM) | 19 | 20 | 95% (last 20) | Does not open (82%) | 50% | today | 50% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 85 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 20% | 18d ago | n/a | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 86 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 53% | 8d ago | 69% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 87 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (53%) | 53% | 1d ago | 58% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 88 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 2% | 8d ago | 1% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 89 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 13% | 20d ago | n/a | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 90 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (64%) | 36% | today | 40% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 91 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (73%) | 0% | 33d ago | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 92 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (62%) | 0% | 1d ago | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 93 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (89%) | 21% | 12d ago | 10% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 94 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 3% | 15d ago | 4% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 95 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (61%) | 50% | 8d ago | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 96 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (80%) | 25% | today | 20% | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 97 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 19 | 20 | 95% (last 20) | No graphics (59%) | 37% | 6d ago | 47% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 98 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 24% | today | 25% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 99 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 5% | 26d ago | 7% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 100 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | 36% | 10d ago | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 101 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (94%) | 25% | 18d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 102 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (97%) | 27% | 18d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 103 | [ ] | OneShot (STEAM) | 16 | 20 | 80% (last 20) | Does not open (96%) | 15% | 35d ago | n/a | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 104 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | 50% | 6d ago | 29% (drop) | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 105 | [ ] | Lost Planet: Extreme Condition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | 42% | 5d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 106 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (55%) | 53% | 8d ago | 22% (drop) | [#540](https://github.com/GameNative/gamenative-compat/issues/540) |
| 107 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (89%) | 27% | 4d ago | 31% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 108 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (83%) | 58% | 5d ago | 50% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 109 | [ ] | Aliens vs. Predator (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 29% | 8d ago | 33% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 110 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (67%) | 54% | 9d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 111 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 19% | 34d ago | 30% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 112 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 40% | 3d ago | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 113 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | 18% | 9d ago | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 114 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | 46% | 20d ago | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 115 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | 47% | 6d ago | 36% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 116 | [ ] | Zuma Deluxe (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | 25% | 7d ago | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 117 | [ ] | Beyond Good & Evil™ (GOG) | 17 | 20 | 85% (last 20) | Does not open (100%) | 20% | 1d ago | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 118 | [ ] | Maneater (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 50% | 6d ago | 50% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 119 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (73%) | 50% | 11d ago | 60% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 120 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 20 | 80% (last 20) | Does not open (82%) | 56% | 4d ago | 40% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 121 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (54%) | 50% | 5d ago | n/a | [#541](https://github.com/GameNative/gamenative-compat/issues/541) |
| 122 | [ ] | Maneater (EPIC) | 16 | 20 | 80% (last 20) | Does not open (73%) | 35% | 4d ago | 17% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 123 | [ ] | Hitman 2: Silent Assassin (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 40% | 3d ago | 44% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 124 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 45% | 12d ago | 50% | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 125 | [ ] | Ghostwire Tokyo (EPIC) | 14 | 20 | 70% (last 20) | Does not open (90%) | 52% | 5d ago | 38% | [#544](https://github.com/GameNative/gamenative-compat/issues/544) |

## Probably does not work (183)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Counter-Strike 2 (STEAM) | 49 | 72 | 68% (since fix) | Does not open (67%) | 55% | today | 57% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 2 | [ ] | Euro Truck Simulator 2 (STEAM) | 17 | 29 | 59% (14d) | Does not open (65%) | 56% | today | 56% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 3 | [ ] | theHunter Classic (STEAM) | 20 | 20 | 100% (last 20) | No graphics (92%) | n/a | 16d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 4 | [ ] | Bully: Scholarship Edition (STEAM) | 16 | 24 | 67% (14d) | Does not open (61%) | 45% | today | 12% (drop) |  |
| 5 | [ ] | To The Moon (GOG) | 18 | 20 | 90% (last 20) | Does not open (86%) | n/a | 17d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 6 | [ ] | FINAL FANTASY XIII (STEAM) | 12 | 23 | 52% (14d) | Does not open (72%) | 55% | today | 57% |  |
| 7 | [ ] | Metro 2033 Redux (STEAM) | 11 | 21 | 52% (14d) | Does not open (70%) | 40% | 1d ago | 39% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 8 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 13 | 20 | 65% (last 20) | Does not open (62%) | 46% | 5d ago | 37% |  |
| 9 | [ ] | Garry's Mod (STEAM) | 10 | 18 | 56% (since fix) | Does not open (80%) | 53% | today | 44% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 10 | [ ] | Driver: Parallel Lines (STEAM) | 19 | 20 | 95% (last 20) | Does not open (65%) | n/a | 11d ago | n/a | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 11 | [ ] | VRChat (STEAM) | 13 | 20 | 65% (last 20) | Does not open (70%) | 39% | 2d ago | 33% |  |
| 12 | [ ] | Door Kickers 2 (STEAM) | 20 | 20 | 100% (last 20) | No graphics (86%) | n/a | 37d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 13 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 40d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 14 | [ ] | Gorilla Tag (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 11% | 5d ago | 7% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 15 | [ ] | Teenage Mutant Ninja Turtles: Shredder's Revenge (EPIC) | 13 | 20 | 65% (last 20) | Does not open (82%) | 54% | 4d ago | 47% |  |
| 16 | [ ] | DOOM 64 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (60%) | 51% | 1d ago | 35% |  |
| 17 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (36%) | n/a | 17d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 18 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | n/a | 6d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 19 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 12 | 20 | 60% (last 20) | Does not open (72%) | 35% | 2d ago | 40% |  |
| 20 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 20 | 20 | 100% (last 20) | Controller issues (100%) | n/a | 1d ago | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 21 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 24d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 22 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | No graphics (55%) | n/a | 23d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 23 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 11 | 19 | 58% (since fix) | Does not open (77%) | 34% | 4d ago | 37% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 24 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | No graphics (38%) | 49% | 5d ago | 34% |  |
| 25 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 54% | 4d ago | 38% |  |
| 26 | [ ] | Sonic Adventure™ 2  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (76%) | 46% | today | 40% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 27 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 13d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 28 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 12 | 20 | 60% (last 20) | Does not open (86%) | 56% | today | 27% (drop) | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 29 | [ ] | Metro 2033 Redux (EPIC) | 11 | 20 | 55% (last 20) | Does not open (58%) | 28% | 1d ago | 36% |  |
| 30 | [ ] | Counter-Strike (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 36% | today | 29% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 31 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 21d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 32 | [ ] | Hi-Fi RUSH (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 45% | today | 45% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 33 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (93%) | n/a | 3d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 34 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | n/a | 12d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 35 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | 12% | 3d ago | n/a |  |
| 36 | [ ] | MudRunner (EPIC) | 10 | 20 | 50% (last 20) | Does not open (58%) | 52% | today | 41% |  |
| 37 | [ ] | Art of Rally (EPIC) | 10 | 20 | 50% (last 20) | Does not open (72%) | 49% | today | 40% |  |
| 38 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | n/a | 5d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 39 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 15d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 40 | [ ] | CODE VEIN (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | 36% | 4d ago | 20% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 41 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (85%) | 50% | 10d ago | n/a |  |
| 42 | [ ] | Legacy of Kain: Defiance Remastered (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (69%) | n/a | today | n/a |  |
| 43 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (66%) | n/a | 18d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 44 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (70%) | n/a | 5d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 45 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | n/a | 1d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 46 | [ ] | GRID (STEAM) | 10 | 20 | 50% (last 20) | Does not open (58%) | 42% | 5d ago | 53% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 47 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | 2d ago | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 48 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 38d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 49 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | n/a | 17d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 50 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 9d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 51 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | n/a | 39d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 52 | [ ] | Grim Dawn (GOG) | 13 | 20 | 65% (last 20) | Does not open (69%) | 40% | 4d ago | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 53 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 37d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 54 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (59%) | n/a | 1d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 55 | [ ] | Hollow Knight: Silksong (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 51% | 3d ago | 48% |  |
| 56 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | n/a | 6d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 57 | [ ] | Alpha Protocol (STEAM) | 17 | 20 | 85% (last 20) | No graphics (53%) | n/a | 25d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 58 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (56%) | n/a | 5d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 59 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 47% | 3d ago | 29% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 60 | [ ] | Dead Space 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 31% | 10d ago | 30% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 61 | [ ] | METAL SLUG 3 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (78%) | 54% | 7d ago | 67% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 62 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (56%) | n/a | 6d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 63 | [ ] | DOOM Eternal (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | today | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 64 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (65%) | n/a | 21d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 65 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 37d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 66 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 23d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 67 | [ ] | HELLDIVERS™ (STEAM) | 12 | 20 | 60% (last 20) | Does not open (58%) | 47% | 1d ago | 55% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 68 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (93%) | n/a | 40d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 69 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 37d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 70 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 6d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 71 | [ ] | Borderlands 2 RU (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | n/a | 3d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 72 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | 2d ago | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 73 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 11d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 74 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 23d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 75 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 55% | 16d ago | n/a |  |
| 76 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 29% | 10d ago | 27% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 77 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (92%) | 38% | 4d ago | n/a |  |
| 78 | [ ] | Euro Truck Simulator (STEAM) | 20 | 20 | 100% (last 20) | Does not open (88%) | n/a | 4d ago | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 79 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 48d ago | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 80 | [ ] | Peggle Nights (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 23d ago | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 81 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 19d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 82 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | 2d ago | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 83 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 4d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 84 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (54%) | n/a | 25d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 85 | [ ] | A Plague Tale: Innocence (EPIC) | 12 | 20 | 60% (last 20) | Does not open (70%) | 41% | today | 29% |  |
| 86 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (50%) | n/a | 19d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 87 | [ ] | Beholder (EPIC) | 18 | 20 | 90% (last 20) | Does not open (61%) | n/a | 2d ago | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 88 | [ ] | The Survivalists (STEAM) | 18 | 20 | 90% (last 20) | Does not open (96%) | n/a | 7d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 89 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (60%) | n/a | 42d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 90 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | n/a | 3d ago | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 91 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | n/a | 37d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 92 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (61%) | n/a | 46d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 93 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 15d ago | n/a |  |
| 94 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | n/a | 20d ago | n/a | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 95 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | n/a | 8d ago | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 96 | [ ] | Breathedge (STEAM) | 10 | 20 | 50% (last 20) | Does not open (55%) | 59% | today | 73% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 97 | [ ] | Super Meat Boy Forever (EPIC) | 10 | 20 | 50% (last 20) | Does not open (83%) | 46% | today | 28% |  |
| 98 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 62d ago | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 99 | [ ] | Bionic Commando Rearmed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | n/a | 30d ago | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 100 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | n/a | today | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 101 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 24d ago | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 102 | [ ] | Undisputed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | n/a | 12d ago | n/a | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 103 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (80%) | n/a | 13d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 104 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 13d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 105 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 8d ago | n/a |  |
| 106 | [ ] | Rise of the Tomb Raider: 20 Year Celebration (EPIC) | 11 | 20 | 55% (last 20) | Does not open (69%) | 48% | 1d ago | 36% |  |
| 107 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 11 | 20 | 55% (last 20) | Does not open (90%) | 54% | 1d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 108 | [ ] | Metro 2033 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 25% | 16d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 109 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 11d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 110 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | n/a | 8d ago | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 111 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 21d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 112 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 10d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 113 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 15d ago | n/a |  |
| 114 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 15d ago | n/a |  |
| 115 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (94%) | 50% | 1d ago | n/a | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 116 | [ ] | Crysis® (GOG) | 17 | 20 | 85% (last 20) | Does not open (86%) | n/a | 3d ago | n/a |  |
| 117 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (36%) | n/a | 18d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 118 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 8d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 119 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 22d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 120 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | n/a | 2d ago | n/a | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 121 | [ ] | Romancing SaGa -Minstrel Song- Remastered (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (100%) | n/a | 4d ago | n/a |  |
| 122 | [ ] | Mortal Shell (EPIC) | 13 | 20 | 65% (last 20) | Does not open (50%) | 44% | 1d ago | 21% (drop) |  |
| 123 | [ ] | Drop Duchy (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 9% | 1d ago | n/a |  |
| 124 | [ ] | Dying Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (86%) | 57% | 4d ago | 44% |  |
| 125 | [ ] | ENDLESS Space™ 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 35d ago | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 126 | [ ] | Fallout Classic (GOG) | 15 | 20 | 75% (last 20) | Does not open (88%) | n/a | 7d ago | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 127 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | n/a | 4d ago | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 128 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | No graphics (45%) | n/a | 10d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 129 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | n/a | today | n/a |  |
| 130 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 55% | 8d ago | n/a |  |
| 131 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 13 | 20 | 65% (last 20) | Does not open (55%) | 50% | 4d ago | 30% (drop) | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 132 | [ ] | Mafia II (Classic) (GOG) | 13 | 20 | 65% (last 20) | Does not open (94%) | 50% | 5d ago | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 133 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 54% | 20d ago | 33% (drop) |  |
| 134 | [ ] | Re-Volt (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (71%) | n/a | 26d ago | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 135 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | 7d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 136 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (69%) | n/a | 15d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 137 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | n/a | 32d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 138 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | n/a | 10d ago | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 139 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (87%) | 19% | 1d ago | 24% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 140 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 53% | 6d ago | 36% |  |
| 141 | [ ] | Mafia: Definitive Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (87%) | 39% | 1d ago | 38% |  |
| 142 | [ ] | Sacred Gold (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | n/a | 1d ago | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 143 | [ ] | DAEMON X MACHINA (EPIC) | 10 | 20 | 50% (last 20) | Does not open (92%) | 48% | 1d ago | 25% (drop) |  |
| 144 | [ ] | Chef Knight (STEAM) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 24d ago | n/a |  |
| 145 | [ ] | shapez (STEAM) | 14 | 20 | 70% (last 20) | No graphics (73%) | n/a | today | n/a | [#332](https://github.com/GameNative/gamenative-compat/issues/332) |
| 146 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 42% | 9d ago | n/a |  |
| 147 | [ ] | Songs of Conquest (EPIC) | 13 | 20 | 65% (last 20) | Does not open (75%) | n/a | 4d ago | n/a |  |
| 148 | [ ] | FINAL FANTASY VII REMAKE INTERGRADE (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 43% | 5d ago | 43% |  |
| 149 | [ ] | Sandustry (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | n/a | 5d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 150 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 52% | today | 60% |  |
| 151 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 57% | 11d ago | 58% |  |
| 152 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | n/a | 1d ago | n/a |  |
| 153 | [ ] | Chasm (GOG) | 12 | 20 | 60% (last 20) | No graphics (50%) | n/a | 5d ago | n/a |  |
| 154 | [ ] | Crying Suns (EPIC) | 12 | 20 | 60% (last 20) | No graphics (63%) | n/a | 2d ago | n/a |  |
| 155 | [ ] | Assassin's Creed Odyssey (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 57% | 3d ago | 50% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 156 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (45%) | n/a | 11d ago | n/a |  |
| 157 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 10 | 20 | 50% (last 20) | No graphics (57%) | 37% | 4d ago | 54% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 158 | [ ] | Beat Cop (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | n/a | 7d ago | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 159 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | n/a | 42d ago | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 160 | [ ] | Allumeria (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | n/a | 1d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 161 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 55% | 4d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 162 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 15d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 163 | [ ] | Styx: Master of Shadows (EPIC) | 11 | 20 | 55% (last 20) | Does not open (73%) | 48% | 2d ago | 47% |  |
| 164 | [ ] | No More Heroes (STEAM) | 10 | 20 | 50% (last 20) | No graphics (59%) | 41% | today | 35% |  |
| 165 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 13 | 20 | 65% (last 20) | No graphics (56%) | n/a | 38d ago | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 166 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | n/a | 10d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 167 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 14d ago | n/a |  |
| 168 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (58%) | 53% | 1d ago | n/a |  |
| 169 | [ ] | Minit (EPIC) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 12d ago | n/a |  |
| 170 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 21d ago | n/a |  |
| 171 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (78%) | n/a | 14d ago | n/a |  |
| 172 | [ ] | Veritas Tales: Witch of the Dark Castle (STEAM) | 12 | 20 | 60% (last 20) | Does not open (63%) | n/a | today | n/a |  |
| 173 | [ ] | LET IT DIE (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | n/a | 2d ago | n/a |  |
| 174 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (63%) | 58% | 8d ago | n/a |  |
| 175 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | n/a | 8d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 176 | [ ] | HOT WHEELS UNLEASHED™ (EPIC) | 10 | 20 | 50% (last 20) | No graphics (63%) | 48% | 3d ago | 35% |  |
| 177 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | n/a | 22d ago | n/a | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 178 | [ ] | Turnip Boy Robs a Bank (EPIC) | 11 | 20 | 55% (last 20) | Does not open (64%) | 38% | 6d ago | n/a | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 179 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 42% | 15d ago | n/a |  |
| 180 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | n/a | 14d ago | n/a |  |
| 181 | [ ] | Railway Chai Wala (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | n/a | 5d ago | n/a |  |
| 182 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 10 | 20 | 50% (last 20) | Does not open (79%) | n/a | 85d ago | n/a |  |
| 183 | [ ] | Delver (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 26% | 4d ago | 0% (drop) |  |

## Fix shipped, waiting for ratings (15)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | L.A. Noire (STEAM) | 2026-11-04 | 4 | 4 | 5d ago | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 2 | Max Payne 3 (STEAM) | 2026-11-04 | 3 | 3 | 3d ago | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 3 | Red Dead Redemption (STEAM) | 2026-11-04 | 2 | 2 | 3d ago | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 4 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 8 | 8 | today | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 5 | Transistor (STEAM) | 2026-11-10 | 8 | 4 | today | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 6 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 3 | 3 | 9d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 7 | Peggle Deluxe (STEAM) | 2026-10-29 | 2 | 2 | today | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 8 | Necesse (STEAM) | 2026-10-29 | 6 | 0 | 4d ago | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 9 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 1 | 1 | 9d ago | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 10 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 1 | 1 | 16d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 11 | Need for Speed™ (STEAM) | 2026-11-04 | 0 | 0 | 29d ago | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 12 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 0 | 0 | 17d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 13 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 15d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 14 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 0 | 0 | 22d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 15 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 0 | 0 | 16d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |

## Works, but the first launch usually fails (305)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Half-Life (STEAM) | 82 | 116 | 71% (14d) | Does not open (60%) | 69% | today | 67% |  |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 70 | 91 | 77% (14d) | Does not open (63%) | 93% | today | 95% |  |
| 3 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 57 | 78 | 73% (14d) | Does not open (54%) | 82% | today | 83% |  |
| 4 | [ ] | Grand Theft Auto V Legacy (STEAM) | 64 | 75 | 85% (since fix) | Does not open (87%) | 73% | today | 69% |  |
| 5 | [ ] | Buckshot Roulette (STEAM) | 47 | 63 | 75% (14d) | Does not open (64%) | 63% | today | 43% (drop) |  |
| 6 | [ ] | Fallout: New Vegas (STEAM) | 45 | 90 | 50% (14d) | Does not open (67%) | 73% | today | 68% |  |
| 7 | [ ] | Cyberpunk 2077 (STEAM) | 45 | 77 | 58% (14d) | Does not open (71%) | 71% | today | 67% |  |
| 8 | [ ] | MONSTER HUNTER RISE (STEAM) | 38 | 61 | 62% (14d) | Does not open (84%) | 62% | today | 63% |  |
| 9 | [ ] | Road Rash™: 30th Anniversary Edition (STEAM) | 38 | 65 | 58% (14d) | Does not open (74%) | 64% | today | 68% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 10 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 34 | 45 | 76% (14d) | Does not open (59%) | 68% | today | 61% |  |
| 11 | [ ] | Valheim (STEAM) | 38 | 63 | 60% (since fix) | No graphics (54%) | 83% | today | 83% |  |
| 12 | [ ] | Probably Stolen (STEAM) | 33 | 64 | 52% (14d) | Does not open (64%) | 85% | today | 81% |  |
| 13 | [ ] | ROB RUN (STEAM) | 31 | 42 | 74% (14d) | Does not open (88%) | 66% | today | 68% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 14 | [ ] | No Man's Sky (STEAM) | 34 | 64 | 53% (since fix) | Controller issues (61%) | 80% | today | 76% |  |
| 15 | [ ] | Super Meat Boy (STEAM) | 29 | 55 | 53% (14d) | Does not open (57%) | 65% | today | 59% |  |
| 16 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 26 | 36 | 72% (14d) | Does not open (77%) | 77% | today | 73% |  |
| 17 | [ ] | Selaco (STEAM) | 26 | 42 | 62% (14d) | Does not open (87%) | 68% | today | 62% |  |
| 18 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 23 | 28 | 82% (14d) | Does not open (77%) | 62% | today | 62% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 19 | [ ] | Look Outside (STEAM) | 19 | 32 | 59% (14d) | Controller issues (64%) | 91% | today | 91% |  |
| 20 | [ ] | Red Dead Redemption 2 (STEAM) | 21 | 22 | 95% (since fix) | Does not open (98%) | 83% | 1d ago | 85% |  |
| 21 | [ ] | Library Of Ruina (STEAM) | 18 | 25 | 72% (14d) | Does not open (69%) | 85% | today | 81% |  |
| 22 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (43%) | 93% | 1d ago | 91% |  |
| 23 | [ ] | ELDEN RING (STEAM) | 16 | 31 | 52% (14d) | Does not open (85%) | 68% | today | 65% |  |
| 24 | [ ] | BeamNG.drive (STEAM) | 16 | 21 | 76% (14d) | Does not open (78%) | 74% | today | 59% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 25 | [ ] | Team Fortress 2 (STEAM) | 16 | 31 | 52% (14d) | Does not open (68%) | 76% | 1d ago | 74% |  |
| 26 | [ ] | Resident Evil 4 (2005) (STEAM) | 16 | 23 | 70% (14d) | Does not open (78%) | 72% | 2d ago | 70% |  |
| 27 | [ ] | Order of the Sinking Star (STEAM) | 15 | 24 | 63% (14d) | Does not open (65%) | 65% | today | 69% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 28 | [ ] | Loftia (STEAM) | 16 | 20 | 80% (last 20) | Does not open (94%) | 72% | 1d ago | 67% |  |
| 29 | [ ] | Shakedown: Hawaii (STEAM) | 14 | 27 | 52% (14d) | Does not open (77%) | 90% | today | 82% |  |
| 30 | [ ] | DOOM 3: BFG Edition (STEAM) | 14 | 21 | 67% (14d) | Does not open (73%) | 70% | today | 66% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 31 | [ ] | DRAGON BALL FighterZ (STEAM) | 28 | 53 | 53% (since fix) | Does not open (88%) | 85% | today | 89% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 32 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (57%) | 75% | 1d ago | 67% |  |
| 33 | [ ] | Deadlock (STEAM) | 15 | 20 | 75% (last 20) | Does not open (54%) | 88% | 5d ago | 84% |  |
| 34 | [ ] | Quake (STEAM) | 13 | 23 | 57% (14d) | Does not open (63%) | 71% | today | 60% |  |
| 35 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 26 | 46 | 57% (since fix) | Does not open (73%) | 60% | today | 57% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 36 | [ ] | Mortal Kombat X (STEAM) | 13 | 20 | 65% (last 20) | Does not open (72%) | 90% | 2d ago | 91% |  |
| 37 | [ ] | Noita (STEAM) | 12 | 24 | 50% (14d) | Does not open (56%) | 78% | 1d ago | 80% |  |
| 38 | [ ] | Alabaster Dawn (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (50%) | 88% | today | 89% |  |
| 39 | [ ] | Geometry Wars: Retro Evolved (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 63% | today | 56% |  |
| 40 | [ ] | Fallout: New Vegas PCR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | 62% | today | 60% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 41 | [ ] | Grand Theft Auto V (EPIC) | 18 | 20 | 90% (last 20) | Does not open (89%) | 78% | 2d ago | 78% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 42 | [ ] | Resident Evil 7 Biohazard (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 73% | today | 66% |  |
| 43 | [ ] | DOOM (STEAM) | 11 | 22 | 50% (14d) | Does not open (69%) | 86% | 2d ago | 86% |  |
| 44 | [ ] | Batman™: Arkham Origins (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | 72% | 2d ago | 61% |  |
| 45 | [ ] | Cry of Fear (STEAM) | 14 | 20 | 70% (last 20) | Does not open (47%) | 71% | today | 73% |  |
| 46 | [ ] | River City Girls (EPIC) | 14 | 20 | 70% (last 20) | Does not open (45%) | 63% | today | 44% |  |
| 47 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (90%) | 93% | 2d ago | 94% |  |
| 48 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (71%) | 100% | 5d ago | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 49 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 17 | 20 | 85% (last 20) | Does not open (59%) | 88% | today | 87% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 50 | [ ] | Absolute Drift (EPIC) | 11 | 20 | 55% (last 20) | No graphics (53%) | 62% | today | 35% (drop) |  |
| 51 | [ ] | Mass Effect™ Legendary Edition (STEAM) | 11 | 22 | 50% (since fix) | Does not open (85%) | 80% | today | 83% |  |
| 52 | [ ] | OMORI (STEAM) | 13 | 20 | 65% (last 20) | Does not open (62%) | 68% | today | 57% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 53 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 62% | 1d ago | 62% |  |
| 54 | [ ] | Dead Space (STEAM) | 18 | 20 | 90% (last 20) | Does not open (57%) | 83% | today | 78% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 55 | [ ] | Dead Island 2 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (85%) | 67% | today | 53% |  |
| 56 | [ ] | Asterigos: Curse of the Stars (STEAM) | 17 | 20 | 85% (last 20) | Graphics glitches (73%) | 80% | today | n/a |  |
| 57 | [ ] | Aniimo (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | 80% | today | 74% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 58 | [ ] | Mini Motorways (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 67% | today | 63% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 59 | [ ] | Divinity: Original Sin 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (73%) | 80% | 1d ago | 73% |  |
| 60 | [ ] | Don't Starve Together (STEAM) | 11 | 20 | 55% (last 20) | Does not open (62%) | 72% | today | 65% |  |
| 61 | [ ] | Disco Elysium - The Final Cut (EPIC) | 11 | 20 | 55% (last 20) | Does not open (75%) | 97% | today | 98% |  |
| 62 | [ ] | Disgaea 5 Complete (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | 90% | 3d ago | 94% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 63 | [ ] | Castlevania Dominus Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (92%) | 98% | 4d ago | 96% |  |
| 64 | [ ] | Fallout: New Vegas (EPIC) | 15 | 20 | 75% (last 20) | Does not open (60%) | 79% | today | 74% |  |
| 65 | [ ] | LEGO® MARVEL Super Heroes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (66%) | 83% | today | 85% |  |
| 66 | [ ] | Cyberpunk 2077 (GOG) | 12 | 20 | 60% (last 20) | Does not open (72%) | 70% | 2d ago | 63% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 67 | [ ] | Dressmaker (STEAM) | 10 | 20 | 50% (last 20) | Does not open (55%) | 81% | today | 73% |  |
| 68 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 65% | 3d ago | 68% |  |
| 69 | [ ] | Darksiders Warmastered Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 60% | 1d ago | 44% |  |
| 70 | [ ] | eFootball™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | 66% | 2d ago | 59% |  |
| 71 | [ ] | Welcome to Elderfield (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 69% | 1d ago | 72% |  |
| 72 | [ ] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 74% | 3d ago | 84% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 73 | [ ] | TBH: Task Bar Hero (STEAM) | 11 | 20 | 55% (last 20) | Does not open (68%) | 86% | today | 88% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 74 | [ ] | METAL GEAR SOLID 4: Guns of the Patriots - Master Collection Version (STEAM) | 10 | 20 | 50% (last 20) | Does not open (80%) | 88% | today | 92% |  |
| 75 | [ ] | Prey (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 78% | 1d ago | 81% |  |
| 76 | [ ] | Pathogenic (STEAM) | 10 | 20 | 50% (last 20) | Does not open (81%) | 70% | today | 62% |  |
| 77 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (50%) | 86% | today | 83% |  |
| 78 | [ ] | Poppy Playtime (STEAM) | 13 | 20 | 65% (last 20) | Does not open (59%) | 68% | 5d ago | 58% |  |
| 79 | [ ] | Fable - The Lost Chapters (STEAM) | 14 | 20 | 70% (last 20) | Graphics glitches (47%) | 81% | today | 84% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 80 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 7 | 13 | 54% (since fix) | Controller issues (84%) | 76% | 1d ago | 73% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 81 | [ ] | Chained Echoes (GOG) | 14 | 20 | 70% (last 20) | Does not open (60%) | 60% | 1d ago | 54% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 82 | [ ] | Deskrawl: Idle ARPG (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 64% | 9d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 83 | [ ] | Dota 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (76%) | 82% | 3d ago | 88% |  |
| 84 | [ ] | Rune Factory 3 Special (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 93% | today | n/a |  |
| 85 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 12 | 20 | 60% (last 20) | Does not open (79%) | 97% | 1d ago | 96% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 86 | [ ] | Call of Duty 4: Modern Warfare (2007) (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (54%) | 75% | 1d ago | 64% |  |
| 87 | [ ] | Ratatan (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 90% | 7d ago | 87% |  |
| 88 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 15 | 20 | 75% (last 20) | Does not open (42%) | 72% | 3d ago | 67% |  |
| 89 | [ ] | Fate/stay night REMASTERED (STEAM) | 12 | 20 | 60% (last 20) | No graphics (48%) | 93% | 5d ago | 90% |  |
| 90 | [ ] | STAR WARS™ Knights of the Old Republic™ II: The Sith Lords™ (STEAM) | 11 | 20 | 55% (last 20) | No graphics (67%) | 60% | today | 38% (drop) |  |
| 91 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (84%) | 70% | 2d ago | 47% (drop) |  |
| 92 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 67% | 3d ago | 71% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 93 | [ ] | Happy Wheels (STEAM) | 19 | 20 | 95% (last 20) | No graphics (52%) | 67% | 13d ago | 52% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 94 | [ ] | Cave Story+ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | 80% | 2d ago | 75% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 95 | [ ] | Minecraft Dungeons (STEAM) | 12 | 20 | 60% (last 20) | Does not open (77%) | 76% | today | 75% |  |
| 96 | [ ] | Need for Speed™ Rivals (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 74% | 3d ago | 81% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 97 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (61%) | 97% | 2d ago | 98% |  |
| 98 | [ ] | Detroit: Become Human (STEAM) | 18 | 20 | 90% (last 20) | Does not open (75%) | 61% | 2d ago | 64% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 99 | [ ] | MIO: Memories in Orbit (STEAM) | 11 | 20 | 55% (last 20) | Graphics glitches (62%) | 94% | 4d ago | 97% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 100 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (51%) | 60% | 6d ago | 34% (drop) | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 101 | [ ] | The Sims™ 4 (STEAM) | 6 | 12 | 50% (since fix) | Does not open (85%) | 71% | 2d ago | 73% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 102 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (80%) | 81% | 2d ago | 73% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 103 | [ ] | Palia (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 74% | 1d ago | 67% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 104 | [ ] | Mortal Kombat 11 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | 69% | today | 74% |  |
| 105 | [ ] | Until Then (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 74% | 1d ago | 57% |  |
| 106 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (52%) | 70% | 2d ago | 74% |  |
| 107 | [ ] | Sid Meier's Civilization VI (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | 82% | 1d ago | 75% |  |
| 108 | [ ] | American Truck Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 77% | today | 72% |  |
| 109 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (42%) | 91% | today | 89% |  |
| 110 | [ ] | ZERO Sievert (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 86% | 2d ago | 79% |  |
| 111 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 92% | 1d ago | 85% |  |
| 112 | [ ] | Minecraft Dungeons II (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | 70% | 1d ago | 72% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 113 | [ ] | Resident Evil Village (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 90% | 8d ago | 86% |  |
| 114 | [ ] | Abiotic Factor (STEAM) | 10 | 20 | 50% (last 20) | Does not open (74%) | 75% | 3d ago | 81% |  |
| 115 | [ ] | Astral Party  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 84% | today | 79% |  |
| 116 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 60% | 1d ago | 47% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 117 | [ ] | PAYDAY: The Heist (STEAM) | 15 | 20 | 75% (last 20) | Does not open (79%) | 69% | 1d ago | n/a |  |
| 118 | [ ] | Caravan SandWitch (EPIC) | 10 | 20 | 50% (last 20) | Does not open (76%) | 70% | today | 69% |  |
| 119 | [ ] | Sid Meier's Civilization V (STEAM) | 15 | 20 | 75% (last 20) | Does not open (77%) | 62% | today | 58% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 120 | [ ] | Tails of Iron (STEAM) | 12 | 20 | 60% (last 20) | Does not open (75%) | 86% | today | 83% |  |
| 121 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 77% | 13d ago | 73% |  |
| 122 | [ ] | Grand Theft Auto: Vice City (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | 82% | today | 81% |  |
| 123 | [ ] | A Plague Tale: Innocence (STEAM) | 19 | 20 | 95% (last 20) | Does not open (88%) | 60% | 4d ago | 65% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 124 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 60% | 4d ago | 50% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 125 | [ ] | Moonstone Island (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (63%) | 74% | 4d ago | 74% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 126 | [ ] | PlateUp! (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 82% | today | 70% |  |
| 127 | [ ] | Overwatch® (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | 76% | 3d ago | 83% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 128 | [ ] | No, I'm not a Human (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 94% | 2d ago | 88% |  |
| 129 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | 75% | 11d ago | 90% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 130 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 18 | 20 | 90% (last 20) | Does not open (58%) | 93% | 6d ago | 90% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 131 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (76%) | 100% | 5d ago | n/a | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 132 | [ ] | Call of Duty: World at War (STEAM) | 13 | 20 | 65% (last 20) | Does not open (43%) | 80% | today | 64% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 133 | [ ] | Sovereign Tower (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 78% | today | 73% |  |
| 134 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (78%) | 62% | 18d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 135 | [ ] | Yakuza: Like a Dragon (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | 65% | 1d ago | 78% |  |
| 136 | [ ] | Trailmakers (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 91% | today | 90% |  |
| 137 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 11 | 20 | 55% (last 20) | Does not open (68%) | 90% | today | 90% |  |
| 138 | [ ] | Max Payne (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (45%) | 81% | 2d ago | 78% |  |
| 139 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 82% | today | 79% |  |
| 140 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | 60% | 1d ago | 50% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 141 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 94% | 21d ago | 92% |  |
| 142 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (50%) | 81% | 5d ago | 75% |  |
| 143 | [ ] | Pinball FX (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 75% | 3d ago | 73% |  |
| 144 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 88% | 2d ago | 90% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 145 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 84% | today | 86% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 146 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 73% | 9d ago | 75% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 147 | [ ] | Sonic Generations (STEAM) | 14 | 20 | 70% (last 20) | Does not open (70%) | 67% | 2d ago | 68% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 148 | [ ] | Tabletop Simulator (STEAM) | 14 | 20 | 70% (last 20) | Does not open (53%) | 81% | 1d ago | 86% |  |
| 149 | [ ] | Street Fighter™ 6 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (81%) | 81% | 1d ago | 81% |  |
| 150 | [ ] | Heavy Rain (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 94% | 5d ago | 94% |  |
| 151 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (79%) | 82% | 18d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 152 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (83%) | 88% | 2d ago | n/a | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 153 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (87%) | 92% | 3d ago | 95% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 154 | [ ] | Plague Inc: Evolved (STEAM) | 13 | 20 | 65% (last 20) | Does not open (68%) | 64% | 2d ago | 65% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 155 | [ ] | Oxygen Not Included (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 64% | 5d ago | 70% |  |
| 156 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | 77% | 7d ago | n/a | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 157 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 80% | 13d ago | 81% |  |
| 158 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 83% | 8d ago | 81% |  |
| 159 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 80% | 6d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 160 | [ ] | Gambonanza (STEAM) | 13 | 20 | 65% (last 20) | Does not open (60%) | 91% | 3d ago | 89% |  |
| 161 | [ ] | Gothic 1 Classic (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 77% | 11d ago | 67% |  |
| 162 | [ ] | Limbus Company (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 85% | 1d ago | 91% |  |
| 163 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 11 | 20 | 55% (last 20) | Does not open (62%) | 76% | 2d ago | 74% |  |
| 164 | [ ] | Fallout (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 71% | 1d ago | 67% |  |
| 165 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (62%) | 100% | today | n/a | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 166 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 63% | today | 82% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 167 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (54%) | 69% | 4d ago | 74% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 168 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (59%) | 62% | 8d ago | 61% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 169 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 14 | 20 | 70% (last 20) | Does not open (45%) | 64% | 5d ago | 68% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 170 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 88% | 11d ago | 91% |  |
| 171 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (82%) | 90% | 1d ago | 88% |  |
| 172 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (55%) | 91% | 15d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 173 | [ ] | Stellar Blade™ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (41%) | 79% | today | 80% |  |
| 174 | [ ] | Control Ultimate Edition (GOG) | 13 | 20 | 65% (last 20) | Does not open (76%) | 78% | 9d ago | 72% |  |
| 175 | [ ] | Digimon Survive (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (77%) | 86% | 1d ago | 82% |  |
| 176 | [ ] | Dishonored 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 69% | today | 59% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 177 | [ ] | Escape from Duckov (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (72%) | 95% | 1d ago | 98% |  |
| 178 | [ ] | Sonic Lost World (STEAM) | 10 | 20 | 50% (last 20) | No graphics (69%) | 81% | 3d ago | 79% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 179 | [ ] | Supermarket Together (STEAM) | 15 | 20 | 75% (last 20) | Does not open (68%) | 60% | 2d ago | 67% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 180 | [ ] | Changed (STEAM) | 15 | 20 | 75% (last 20) | Does not open (64%) | 62% | 7d ago | 53% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 181 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | 100% | 30d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 182 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 91% | 8d ago | 88% |  |
| 183 | [ ] | One-armed robber (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (65%) | 76% | 12d ago | 62% |  |
| 184 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | 64% | 12d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 185 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 13 | 20 | 65% (last 20) | Does not open (85%) | 61% | today | 58% |  |
| 186 | [ ] | TurretGirls (STEAM) | 12 | 20 | 60% (last 20) | No graphics (77%) | 91% | today | 94% |  |
| 187 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (70%) | 69% | 12d ago | 71% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 188 | [ ] | BioShock 2 Remastered (STEAM) | 11 | 20 | 55% (last 20) | Does not open (79%) | 85% | 4d ago | 85% |  |
| 189 | [ ] | Stumble Guys (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 68% | 5d ago | 61% |  |
| 190 | [ ] | Counter-Strike:Global Offensive (STEAM) | 10 | 20 | 50% (last 20) | Does not open (76%) | 68% | 4d ago | 65% |  |
| 191 | [ ] | Raft (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | 90% | 4d ago | 86% |  |
| 192 | [ ] | Subnautica 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (52%) | 79% | 2d ago | n/a | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 193 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 88% | 9d ago | n/a | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 194 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (71%) | 91% | 2d ago | n/a | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 195 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (75%) | 83% | 3d ago | 67% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 196 | [ ] | Capcom Arcade Stadium (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | 77% | 7d ago | 82% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 197 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 92% | 10d ago | n/a |  |
| 198 | [ ] | Moonring (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 85% | today | 79% |  |
| 199 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 67% | 1d ago | 72% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 200 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 77% | 1d ago | 81% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 201 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (61%) | 71% | 10d ago | 65% |  |
| 202 | [ ] | Goat Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 67% | 1d ago | 62% |  |
| 203 | [ ] | Unturned (STEAM) | 11 | 20 | 55% (last 20) | Does not open (40%) | 71% | 2d ago | 75% |  |
| 204 | [ ] | The Witcher: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 71% | 13d ago | 82% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 205 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 94% | 9d ago | 93% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 206 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 76% | 14d ago | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 207 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (65%) | 88% | 15d ago | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 208 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (51%) | 63% | 23d ago | 45% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 209 | [ ] | Ultimate Custom Night (STEAM) | 14 | 20 | 70% (last 20) | No graphics (72%) | 62% | today | n/a | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 210 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | 64% | 1d ago | n/a | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 211 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (70%) | 96% | 5d ago | 100% |  |
| 212 | [ ] | Jade Empire: Special Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 79% | 4d ago | n/a | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 213 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | 73% | 17d ago | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 214 | [ ] | Hotline Miami (GOG) | 14 | 20 | 70% (last 20) | Does not open (89%) | 73% | 2d ago | 80% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 215 | [ ] | GOD EATER RESURRECTION (STEAM) | 14 | 20 | 70% (last 20) | Does not open (59%) | 76% | 6d ago | n/a |  |
| 216 | [ ] | Darksiders (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 87% | 4d ago | 82% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 217 | [ ] | Lucid Blocks (STEAM) | 11 | 20 | 55% (last 20) | Does not open (80%) | 65% | today | 53% |  |
| 218 | [ ] | My Summer Car (STEAM) | 11 | 20 | 55% (last 20) | Does not open (63%) | 77% | 2d ago | 81% |  |
| 219 | [ ] | Warframe (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 82% | 3d ago | 78% |  |
| 220 | [ ] | MX Bikes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 92% | 2d ago | 94% |  |
| 221 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 64% | 8d ago | 55% |  |
| 222 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (91%) | 81% | 33d ago | 73% |  |
| 223 | [ ] | Invisible, Inc. (STEAM) | 15 | 20 | 75% (last 20) | Does not open (63%) | 77% | 21d ago | n/a |  |
| 224 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 75% | 23d ago | 73% |  |
| 225 | [ ] | Return to Monkey Island (STEAM) | 14 | 20 | 70% (last 20) | No graphics (72%) | 68% | 13d ago | 69% |  |
| 226 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (44%) | 68% | 15d ago | n/a | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 227 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (47%) | 80% | 4d ago | n/a |  |
| 228 | [ ] | Resident Evil Revelations 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (45%) | 84% | 2d ago | 82% |  |
| 229 | [ ] | STORY OF SEASONS: Friends of Mineral Town (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 93% | today | 100% |  |
| 230 | [ ] | GUILTY GEAR Xrd REV 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (83%) | 74% | 5d ago | 60% |  |
| 231 | [ ] | CS2D (STEAM) | 10 | 20 | 50% (last 20) | Does not open (57%) | 80% | 1d ago | n/a |  |
| 232 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Controller issues (36%) | 92% | 1d ago | n/a |  |
| 233 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 77% | 8d ago | 78% |  |
| 234 | [ ] | No Socks RPG (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (91%) | 93% | today | 92% |  |
| 235 | [ ] | Bongo Cat (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 61% | 2d ago | 44% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 236 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 93% | 10d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 237 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (83%) | 77% | 3d ago | 76% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 238 | [ ] | Big Walk (STEAM) | 12 | 20 | 60% (last 20) | Does not open (55%) | 68% | today | 53% |  |
| 239 | [ ] | Cat Mail Co. (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 85% | 1d ago | 84% |  |
| 240 | [ ] | Hylics (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (69%) | 97% | 1d ago | 94% |  |
| 241 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 11 | 20 | 55% (last 20) | Does not open (53%) | 70% | 3d ago | 74% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 242 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 95% | 5d ago | 100% |  |
| 243 | [ ] | Revolution Idle (STEAM) | 10 | 20 | 50% (last 20) | Does not open (43%) | 83% | 3d ago | n/a |  |
| 244 | [ ] | AER Memories of Old (EPIC) | 13 | 20 | 65% (last 20) | Does not open (86%) | 93% | 4d ago | 91% |  |
| 245 | [ ] | Capcom Fighting Collection (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 88% | today | 86% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 246 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (71%) | 76% | 5d ago | 73% |  |
| 247 | [ ] | SnowRunner (STEAM) | 12 | 20 | 60% (last 20) | Does not open (96%) | 71% | 2d ago | 69% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 248 | [ ] | BATTLETECH (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 96% | 4d ago | 94% |  |
| 249 | [ ] | Deus Ex™ GOTY Edition (GOG) | 12 | 20 | 60% (last 20) | No graphics (44%) | 100% | 20d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 250 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 100% | 12d ago | n/a |  |
| 251 | [ ] | Zero Escape: The Nonary Games (STEAM) | 11 | 20 | 55% (last 20) | Does not open (92%) | 72% | today | 68% |  |
| 252 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (78%) | 97% | 3d ago | 96% |  |
| 253 | [ ] | Hero Siege (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (46%) | 83% | 4d ago | 86% |  |
| 254 | [ ] | Secrets of Grindea (STEAM) | 10 | 20 | 50% (last 20) | Does not open (45%) | 76% | 2d ago | 80% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 255 | [ ] | Tales of Zestiria (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 67% | 25d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 256 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (95%) | 91% | 11d ago | 89% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 257 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (84%) | 70% | today | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 258 | [ ] | Disgaea 4 Complete+ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (43%) | 91% | 5d ago | n/a | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 259 | [ ] | Timberborn (STEAM) | 12 | 20 | 60% (last 20) | No graphics (68%) | 94% | 1d ago | 100% |  |
| 260 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 12 | 20 | 60% (last 20) | No graphics (39%) | 76% | 3d ago | n/a | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 261 | [ ] | 12 is Better Than 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 77% | 15d ago | n/a |  |
| 262 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 88% | 6d ago | 82% |  |
| 263 | [ ] | Rollout Inline (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 62% | today | 82% |  |
| 264 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 14 | 20 | 70% (last 20) | Does not open (85%) | 82% | 12d ago | n/a | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 265 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 67% | 10d ago | n/a |  |
| 266 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 92% | 31d ago | 92% |  |
| 267 | [ ] | Goose Goose Duck (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 71% | today | 75% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 268 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 65% | 7d ago | 57% |  |
| 269 | [ ] | Sons Of The Forest (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 78% | 5d ago | 75% |  |
| 270 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 61% | 14d ago | 60% |  |
| 271 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (50%) | 72% | 12d ago | 85% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 272 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 76% | 2d ago | 82% |  |
| 273 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 93% | 8d ago | 89% |  |
| 274 | [ ] | CRUEL (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 76% | 5d ago | 73% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 275 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 64% | 4d ago | 82% |  |
| 276 | [ ] | Shift At Midnight (STEAM) | 13 | 20 | 65% (last 20) | Does not open (67%) | 90% | 1d ago | 86% |  |
| 277 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 88% | 2d ago | 93% |  |
| 278 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 85% | 10d ago | 83% |  |
| 279 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 85% | 5d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 280 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 67% | 1d ago | 69% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 281 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 81% | 11d ago | 74% |  |
| 282 | [ ] | Super Battle Golf (STEAM) | 10 | 20 | 50% (last 20) | Does not open (88%) | 90% | 1d ago | 83% |  |
| 283 | [ ] | Hitman: Absolution (GOG) | 10 | 20 | 50% (last 20) | Does not open (83%) | 82% | 2d ago | n/a |  |
| 284 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 90% | 5d ago | 100% |  |
| 285 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (92%) | 85% | 15d ago | n/a |  |
| 286 | [ ] | Forgive Me Father (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 74% | 6d ago | 60% |  |
| 287 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 77% | 4d ago | 70% |  |
| 288 | [ ] | Subnautica: Below Zero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 82% | today | 72% |  |
| 289 | [ ] | Cruelty Squad (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 86% | 3d ago | 81% |  |
| 290 | [ ] | A Plague Tale: Innocence (GOG) | 10 | 20 | 50% (last 20) | Does not open (91%) | 60% | 2d ago | n/a |  |
| 291 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 60% | 3d ago | 73% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 292 | [ ] | BioShock 2 Remastered (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 90% | today | 87% |  |
| 293 | [ ] | Intravenous (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 76% | 11d ago | 80% |  |
| 294 | [ ] | SILENT HILL 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (58%) | 88% | 5d ago | 100% |  |
| 295 | [ ] | Decktamer (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 75% | today | n/a |  |
| 296 | [ ] | The Stanley Parable (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 82% | today | 83% |  |
| 297 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 74% | 13d ago | 70% |  |
| 298 | [ ] | Dungeon Siege (STEAM) | 10 | 20 | 50% (last 20) | Does not open (44%) | 93% | today | 100% |  |
| 299 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 62% | 7d ago | n/a |  |
| 300 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (65%) | 92% | 10d ago | 94% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 301 | [ ] | Legend of Grimrock 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 92% | 3d ago | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 302 | [ ] | Haydee (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 79% | 5d ago | n/a |  |
| 303 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (78%) | 100% | 5d ago | 100% |  |
| 304 | [ ] | Helping the Hotties (GOG) | 10 | 20 | 50% (last 20) | Does not open (75%) | 75% | 1d ago | n/a |  |
| 305 | [ ] | Secret of Mana (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (56%) | 70% | 2d ago | n/a |  |

## Recently recovered (384)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Grim Dawn (STEAM) | 494 | 2026-11-08 | 573 | 65% |  |
| 2 | [x] | FINAL FANTASY RESONANCE (STEAM) | 450 | 2026-10-24 | 1029 | 80% |  |
| 3 | [x] | Half-Life (STEAM) | 378 | 2026-11-09 | 644 | 69% |  |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 265 | 2026-11-14 | 416 | 67% |  |
| 5 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 238 | 2026-11-09 | 332 | 88% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 6 | [x] | Alan Wake (STEAM) | 233 | 2026-11-14 | 257 | 61% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 7 | [x] | MONSTER HUNTER RISE (STEAM) | 222 | 2026-11-17 | 524 | 62% |  |
| 8 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 207 | 2026-11-09 | 362 | 68% |  |
| 9 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 200 | 2026-11-09 | 241 | 58% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 10 | [x] | BeamNG.drive (STEAM) | 192 | 2026-11-09 | 237 | 74% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 11 | [x] | Call of Duty: Black Ops (STEAM) | 189 | 2026-11-13 | 214 | 19% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 12 | [x] | OMORI (STEAM) | 180 | 2026-11-09 | 226 | 68% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 13 | [x] | DRAGON BALL FighterZ (STEAM) | 170 | 2026-11-01 | 215 | 85% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 14 | [x] | Spelunky 2 (STEAM) | 165 | 2026-11-01 | 207 | 79% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 15 | [x] | Geometry Dash (STEAM) | 154 | 2026-11-11 | 447 | 56% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 16 | [x] | BioShock (STEAM) | 151 | 2026-11-09 | 300 | 71% |  |
| 17 | [x] | Sid Meier's Civilization V (STEAM) | 148 | 2026-11-10 | 160 | 62% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 18 | [x] | Prototype (STEAM) | 141 | 2026-11-11 | 207 | 64% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 19 | [x] | Team Fortress 2 (STEAM) | 135 | 2026-11-09 | 235 | 76% |  |
| 20 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 132 | 2026-11-20 | 178 | 60% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 21 | [x] | Minecraft Dungeons II (STEAM) | 131 | 2026-11-09 | 150 | 70% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 22 | [x] | Castlevania Advance Collection (STEAM) | 127 | 2026-11-09 | 199 | 88% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 23 | [x] | Far Cry® 3 (STEAM) | 119 | 2026-11-20 | 134 | 60% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 24 | [x] | Mirror's Edge (STEAM) | 117 | 2026-11-09 | 171 | 68% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 25 | [x] | Assassin's Creed II (STEAM) | 116 | 2026-11-10 | 121 | 67% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 26 | [x] | Aniimo (STEAM) | 115 | 2026-11-09 | 154 | 80% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 27 | [x] | The Witcher: Enhanced Edition (STEAM) | 102 | 2026-11-09 | 120 | 71% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 28 | [x] | Cave Story+ (STEAM) | 102 | 2026-11-09 | 112 | 80% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 29 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 101 | 2026-11-09 | 142 | 96% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 30 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 99 | 2026-11-15 | 140 | 71% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 31 | [x] | Happy Wheels (STEAM) | 97 | 2026-11-09 | 117 | 67% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 32 | [x] | Moonstone Island (STEAM) | 94 | 2026-11-09 | 123 | 74% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 33 | [x] | Fallout: New Vegas PCR (STEAM) | 91 | 2026-11-20 | 119 | 62% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 34 | [x] | Catherine Classic (STEAM) | 89 | 2026-11-09 | 167 | 54% |  |
| 35 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 81 | 2026-11-09 | 134 | 71% |  |
| 36 | [x] | DOOM 3: BFG Edition (STEAM) | 81 | 2026-11-09 | 123 | 70% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 37 | [x] | FINAL FANTASY XIII-2 (STEAM) | 81 | 2026-11-09 | 84 | 63% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 38 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 80 | 2026-11-09 | 105 | 92% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 39 | [x] | Vital Shell (STEAM) | 79 | 2026-11-09 | 128 | 82% |  |
| 40 | [x] | Quake (STEAM) | 76 | 2026-11-09 | 236 | 71% |  |
| 41 | [x] | Psychonauts (STEAM) | 76 | 2026-11-09 | 141 | 95% |  |
| 42 | [x] | Ballionaire (STEAM) | 74 | 2026-11-09 | 126 | 83% |  |
| 43 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 74 | 2026-11-19 | 96 | 62% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 44 | [x] | Brawlhalla (STEAM) | 73 | 2026-11-09 | 142 | 71% |  |
| 45 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 73 | 2026-11-09 | 113 | 81% |  |
| 46 | [x] | Age of Empires II: Definitive Edition (STEAM) | 73 | 2026-11-10 | 92 | 64% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 47 | [x] | The Sims™ 4 (STEAM) | 72 | 2026-11-09 | 97 | 71% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 48 | [x] | Cyberpunk 2077 (GOG) | 71 | 2026-11-09 | 93 | 70% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 49 | [x] | Detroit: Become Human (STEAM) | 70 | 2026-11-20 | 74 | 61% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 50 | [x] | Order of the Sinking Star (STEAM) | 69 | 2026-11-09 | 102 | 65% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 51 | [x] | STEINS;GATE (STEAM) | 69 | 2026-11-09 | 101 | 87% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 52 | [x] | Dota 2 (STEAM) | 68 | 2026-11-09 | 102 | 82% |  |
| 53 | [x] | Fable - The Lost Chapters (STEAM) | 67 | 2026-11-09 | 108 | 81% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 54 | [x] | Disgaea 5 Complete (STEAM) | 67 | 2026-11-09 | 79 | 90% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 55 | [x] | Stardew Valley (GOG) | 65 | 2026-11-11 | 113 | 76% |  |
| 56 | [x] | Need for Speed: Hot Pursuit (STEAM) | 65 | 2026-11-09 | 101 | 76% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 57 | [x] | Sovereign Tower (STEAM) | 63 | 2026-11-09 | 117 | 78% |  |
| 58 | [x] | Spyro™ Reignited Trilogy (STEAM) | 63 | 2026-11-09 | 107 | 78% |  |
| 59 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 63 | 2026-11-09 | 102 | 84% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 60 | [x] | Diablo® IV (STEAM) | 63 | 2026-11-11 | 75 | 75% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 61 | [x] | Caravan SandWitch (EPIC) | 62 | 2026-11-09 | 124 | 70% |  |
| 62 | [x] | American Truck Simulator (STEAM) | 62 | 2026-11-09 | 104 | 77% |  |
| 63 | [x] | Poppy Playtime (STEAM) | 61 | 2026-11-09 | 103 | 68% |  |
| 64 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 61 | 2026-11-11 | 81 | 57% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 65 | [x] | Mini Motorways (STEAM) | 60 | 2026-11-09 | 96 | 67% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 66 | [x] | Gunfire Reborn (STEAM) | 60 | 2026-11-09 | 66 | 88% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 67 | [x] | Fallout (STEAM) | 59 | 2026-11-09 | 94 | 71% |  |
| 68 | [x] | Borderlands 3 (STEAM) | 59 | 2026-11-09 | 87 | 90% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 69 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 58 | 2026-11-09 | 83 | 60% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 70 | [x] | Deskrawl: Idle ARPG (STEAM) | 58 | 2026-11-09 | 72 | 64% | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 71 | [x] | A Plague Tale: Innocence (STEAM) | 58 | 2026-11-09 | 61 | 60% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 72 | [x] | Firewatch (STEAM) | 57 | 2026-11-10 | 111 | 81% |  |
| 73 | [x] | Grand Theft Auto V (EPIC) | 57 | 2026-11-09 | 64 | 78% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 74 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 56 | 2026-10-25 | 97 | 74% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 75 | [x] | eFootball™ (STEAM) | 56 | 2026-11-09 | 84 | 66% |  |
| 76 | [x] | Call of Juarez Gunslinger (STEAM) | 56 | 2026-11-09 | 71 | 73% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 77 | [x] | Call of Duty: World at War (STEAM) | 55 | 2026-11-09 | 79 | 80% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 78 | [x] | Darksiders (STEAM) | 54 | 2026-11-09 | 69 | 87% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 79 | [x] | Sonic Generations (STEAM) | 54 | 2026-11-09 | 61 | 67% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 80 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 53 | 2026-11-17 | 77 | 64% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 81 | [x] | Starbound (STEAM) | 52 | 2026-11-09 | 84 | 81% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 82 | [x] | Sol Cesto (EPIC) | 52 | 2026-11-09 | 53 | 81% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 83 | [x] | MIO: Memories in Orbit (STEAM) | 51 | 2026-11-09 | 104 | 94% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 84 | [x] | Borderlands: The Pre-Sequel (STEAM) | 51 | 2026-11-09 | 88 | 66% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 85 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 51 | 2026-11-09 | 86 | 75% |  |
| 86 | [x] | Last Epoch (STEAM) | 50 | 2026-11-09 | 75 | 71% |  |
| 87 | [x] | Okami HD (STEAM) | 49 | 2026-11-09 | 91 | 92% |  |
| 88 | [x] | TBH: Task Bar Hero (STEAM) | 48 | 2026-11-09 | 78 | 86% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 89 | [x] | Heroes of Might & Magic III - HD Edition (STEAM) | 48 | 2026-11-14 | 63 | 60% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 90 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 47 | 2026-11-09 | 81 | 60% |  |
| 91 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 47 | 2026-11-09 | 79 | 85% |  |
| 92 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 47 | 2026-11-09 | 54 | 100% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 93 | [x] | Moonlighter (EPIC) | 47 | 2026-11-09 | 51 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 94 | [x] | Overwatch® (STEAM) | 47 | 2026-11-10 | 51 | 76% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 95 | [x] | Oxygen Not Included (STEAM) | 46 | 2026-11-11 | 79 | 64% |  |
| 96 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 46 | 2026-11-09 | 76 | 82% |  |
| 97 | [x] | Watch_Dogs 2 (STEAM) | 46 | 2026-11-20 | 51 | 60% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 98 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 45 | 2026-11-13 | 72 | 64% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 99 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 45 | 2026-11-09 | 68 | 91% |  |
| 100 | [x] | Darkest Dungeon® (EPIC) | 43 | 2026-11-09 | 84 | 86% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 101 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 43 | 2026-11-09 | 73 | 58% |  |
| 102 | [x] | Plague Inc: Evolved (STEAM) | 43 | 2026-11-16 | 64 | 64% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 103 | [x] | Cat Quest (EPIC) | 42 | 2026-11-19 | 101 | 48% |  |
| 104 | [x] | MudRunner (STEAM) | 42 | 2026-10-24 | 97 | 59% |  |
| 105 | [x] | Sheepy: A Short Adventure (STEAM) | 42 | 2026-11-09 | 50 | 63% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 106 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 40 | 2026-11-09 | 73 | 90% |  |
| 107 | [x] | Tomb Raider: Anniversary (STEAM) | 39 | 2026-11-09 | 64 | 56% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 108 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 39 | 2026-11-09 | 60 | 69% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 109 | [x] | Dead by Daylight (STEAM) | 39 | 2026-11-09 | 43 | 84% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 110 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-11-09 | 40 | 77% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 111 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 38 | 2026-11-09 | 71 | 90% |  |
| 112 | [x] | Age of Empires II (2013) (STEAM) | 38 | 2026-11-09 | 63 | 70% |  |
| 113 | [x] | Sonic Lost World (STEAM) | 38 | 2026-11-09 | 58 | 81% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 114 | [x] | Aggelos (STEAM) | 38 | 2026-11-09 | 54 | 88% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 115 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 38 | 2026-11-09 | 54 | 76% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 116 | [x] | Street Fighter™ 6 (STEAM) | 37 | 2026-11-09 | 59 | 81% |  |
| 117 | [x] | FINAL FANTASY VII (2013) (STEAM) | 37 | 2026-11-09 | 54 | 64% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 118 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 37 | 2026-11-19 | 39 | 93% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 119 | [x] | Amnesia: The Dark Descent (STEAM) | 36 | 2026-11-09 | 74 | 87% |  |
| 120 | [x] | Digimon World: Next Order (STEAM) | 36 | 2026-11-09 | 74 | 84% |  |
| 121 | [x] | Sonic Origins (STEAM) | 36 | 2026-11-09 | 67 | 83% |  |
| 122 | [x] | POSTAL 2 (GOG) | 35 | 2026-11-09 | 67 | 90% |  |
| 123 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 35 | 2026-11-09 | 66 | 86% |  |
| 124 | [x] | Ace Attorney Investigations Collection (STEAM) | 35 | 2026-11-09 | 63 | 89% |  |
| 125 | [x] | XCOM 2 (STEAM) | 35 | 2026-11-09 | 61 | 80% |  |
| 126 | [x] | Capcom Arcade Stadium (STEAM) | 35 | 2026-11-09 | 45 | 77% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 127 | [x] | Russian Fishing 4 (STEAM) | 35 | 2026-11-09 | 41 | 83% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 128 | [x] | CrossCode (GOG) | 35 | 2026-11-09 | 38 | 82% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 129 | [x] | SurrounDead (STEAM) | 34 | 2026-11-09 | 65 | 92% |  |
| 130 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 34 | 2026-11-09 | 61 | 76% |  |
| 131 | [x] | Big Walk (STEAM) | 34 | 2026-11-09 | 56 | 68% |  |
| 132 | [x] | Need for Speed™ Rivals (STEAM) | 34 | 2026-11-10 | 46 | 74% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 133 | [x] | Being a DIK (STEAM) | 33 | 2026-11-09 | 73 | 65% |  |
| 134 | [x] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 33 | 2026-11-20 | 60 | 21% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 135 | [x] | Max Payne (STEAM) | 33 | 2026-11-09 | 56 | 81% |  |
| 136 | [x] | Gauntlet™  (STEAM) | 33 | 2026-11-11 | 48 | 70% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 137 | [x] | Elite Dangerous (STEAM) | 33 | 2026-11-20 | 36 | 62% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 138 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 32 | 2026-11-09 | 69 | 71% |  |
| 139 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 32 | 2026-11-09 | 56 | 72% |  |
| 140 | [x] | SnowRunner (STEAM) | 32 | 2026-11-09 | 47 | 71% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 141 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-11-09 | 40 | 100% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 142 | [x] | Journey (STEAM) | 31 | 2026-10-27 | 71 | 66% |  |
| 143 | [x] | COCOON (STEAM) | 31 | 2026-11-09 | 66 | 81% |  |
| 144 | [x] | Hearts of Iron IV (STEAM) | 31 | 2026-11-09 | 63 | 82% |  |
| 145 | [x] | The Bazaar (STEAM) | 31 | 2026-11-09 | 61 | 78% |  |
| 146 | [x] | Yume Nikki (STEAM) | 31 | 2026-11-20 | 55 | 39% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 147 | [x] | Earthion (STEAM) | 31 | 2026-11-09 | 53 | 100% |  |
| 148 | [x] | ROB RUN (STEAM) | 31 | 2026-11-17 | 43 | 66% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 149 | [x] | Red Dead Redemption (STEAM) | 31 | 2026-11-09 | 34 | 52% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 150 | [x] | Ultimate Chicken Horse (STEAM) | 30 | 2026-10-23 | 64 | 93% |  |
| 151 | [x] | Hero Siege (STEAM) | 30 | 2026-11-09 | 52 | 83% |  |
| 152 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 30 | 2026-11-09 | 51 | 95% |  |
| 153 | [x] | Resident Evil Village (STEAM) | 30 | 2026-11-09 | 51 | 90% |  |
| 154 | [x] | Prince of Persia: The Sands of Time (STEAM) | 30 | 2026-11-09 | 50 | 81% |  |
| 155 | [x] | Counter-Strike:Global Offensive (STEAM) | 30 | 2026-11-09 | 46 | 68% |  |
| 156 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 29 | 2026-11-09 | 61 | 86% |  |
| 157 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 29 | 2026-11-09 | 52 | 90% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 158 | [x] | Secrets of Grindea (STEAM) | 29 | 2026-11-09 | 49 | 76% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 159 | [x] | Gambonanza (STEAM) | 29 | 2026-11-09 | 47 | 91% |  |
| 160 | [x] | Yakuza: Like a Dragon (STEAM) | 29 | 2026-11-09 | 47 | 65% |  |
| 161 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 29 | 2026-11-09 | 45 | 82% |  |
| 162 | [x] | Supermarket Together (STEAM) | 29 | 2026-11-18 | 41 | 60% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 163 | [x] | Gothic II: Gold Classic (STEAM) | 29 | 2026-11-09 | 37 | 67% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 164 | [x] | Hotline Miami (GOG) | 29 | 2026-11-18 | 36 | 73% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 165 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 69% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 166 | [x] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 29 | 2026-11-14 | 34 | 80% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 167 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 28 | 2026-11-09 | 48 | 71% |  |
| 168 | [x] | Heavy Rain (STEAM) | 28 | 2026-11-09 | 47 | 94% |  |
| 169 | [x] | Palia (STEAM) | 28 | 2026-11-09 | 40 | 74% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 170 | [x] | Resident Evil Revelations 2 (STEAM) | 27 | 2026-11-09 | 53 | 84% |  |
| 171 | [x] | Tower and Sword of Succubus (STEAM) | 27 | 2026-11-09 | 42 | 81% |  |
| 172 | [x] | Digimon Survive (STEAM) | 27 | 2026-11-09 | 40 | 86% |  |
| 173 | [x] | Skullgirls 2nd Encore (STEAM) | 26 | 2026-11-10 | 62 | 69% |  |
| 174 | [x] | Deponia (STEAM) | 26 | 2026-11-09 | 50 | 74% |  |
| 175 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 26 | 2026-11-09 | 48 | 96% |  |
| 176 | [x] | Zero Escape: The Nonary Games (STEAM) | 26 | 2026-11-09 | 46 | 72% |  |
| 177 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 26 | 2026-11-09 | 43 | 68% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 178 | [x] | Dead Rising 2 (STEAM) | 26 | 2026-11-09 | 42 | 77% |  |
| 179 | [x] | CRUEL (STEAM) | 26 | 2026-11-09 | 36 | 76% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 180 | [x] | Guildrun Demo (STEAM) | 25 | 2026-11-09 | 42 | 85% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 181 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-11-19 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 182 | [x] | Subnautica 2 (STEAM) | 25 | 2026-11-15 | 30 | 79% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 183 | [x] | Slow Roads (STEAM) | 24 | 2026-10-22 | 51 | 63% |  |
| 184 | [x] | Frostpunk (STEAM) | 24 | 2026-11-09 | 50 | 74% |  |
| 185 | [x] | Mirror's Edge™ (GOG) | 24 | 2026-11-13 | 46 | 77% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 186 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 24 | 2026-11-09 | 46 | 62% |  |
| 187 | [x] | Lucid Blocks (STEAM) | 24 | 2026-11-09 | 46 | 65% |  |
| 188 | [x] | Capcom Fighting Collection 2 (STEAM) | 24 | 2026-11-09 | 41 | 85% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 189 | [x] | Cat Mail Co. (STEAM) | 24 | 2026-11-09 | 40 | 85% |  |
| 190 | [x] | Opus Magnum (STEAM) | 24 | 2026-11-09 | 39 | 92% |  |
| 191 | [x] | Limbus Company (STEAM) | 24 | 2026-11-09 | 38 | 85% |  |
| 192 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 24 | 2026-11-09 | 38 | 76% |  |
| 193 | [x] | Ratatan (STEAM) | 24 | 2026-11-09 | 37 | 90% |  |
| 194 | [x] | Dishonored 2 (STEAM) | 24 | 2026-11-09 | 35 | 69% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 195 | [x] | Timberborn (STEAM) | 24 | 2026-11-09 | 35 | 94% |  |
| 196 | [x] | Crab Game (STEAM) | 24 | 2026-11-09 | 28 | 88% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 197 | [x] | Chained Echoes (GOG) | 23 | 2026-11-19 | 51 | 60% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 198 | [x] | Goat Simulator (STEAM) | 23 | 2026-11-09 | 48 | 67% |  |
| 199 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 45 | 91% |  |
| 200 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-11-09 | 45 | 89% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 201 | [x] | Battle Brothers (STEAM) | 23 | 2026-11-09 | 43 | 79% |  |
| 202 | [x] | Trailmakers (STEAM) | 23 | 2026-11-09 | 41 | 91% |  |
| 203 | [x] | Ultimate Custom Night (STEAM) | 23 | 2026-11-19 | 34 | 62% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 204 | [x] | Changed (STEAM) | 23 | 2026-11-18 | 33 | 62% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 205 | [x] | Jade Empire: Special Edition (GOG) | 23 | 2026-11-09 | 30 | 68% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 206 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 23 | 2026-11-09 | 29 | 64% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 207 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 23 | 2026-11-09 | 27 | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 208 | [x] | Prince of Persia (GOG) | 22 | 2026-11-09 | 43 | 77% |  |
| 209 | [x] | Football Manager 2024 (EPIC) | 22 | 2026-11-09 | 40 | 65% |  |
| 210 | [x] | Strider (STEAM) | 22 | 2026-11-20 | 39 | 67% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 211 | [x] | My Summer Car (STEAM) | 22 | 2026-11-09 | 37 | 77% |  |
| 212 | [x] | Tabletop Simulator (STEAM) | 22 | 2026-11-09 | 37 | 81% |  |
| 213 | [x] | Deus Ex™ GOTY Edition (GOG) | 22 | 2026-11-09 | 35 | 100% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 214 | [x] | Mortal Kombat 11 (STEAM) | 22 | 2026-11-09 | 33 | 69% |  |
| 215 | [x] | FINAL FANTASY XIV Online (STEAM) | 22 | 2026-10-22 | 29 | 91% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 216 | [x] | Jade Empire: Special Edition (STEAM) | 22 | 2026-11-09 | 25 | 79% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 217 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 61 | 97% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 218 | [x] | Crazy Taxi (STEAM) | 21 | 2026-11-10 | 43 | 67% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 219 | [x] | Wizard of Legend (EPIC) | 21 | 2026-11-09 | 40 | 78% |  |
| 220 | [x] | Counter-Strike: Condition Zero (STEAM) | 21 | 2026-11-11 | 40 | 25% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 221 | [x] | Control Ultimate Edition (GOG) | 21 | 2026-11-09 | 39 | 78% |  |
| 222 | [x] | Unturned (STEAM) | 21 | 2026-11-09 | 39 | 71% |  |
| 223 | [x] | Invisible, Inc. (STEAM) | 21 | 2026-11-09 | 37 | 77% |  |
| 224 | [x] | Sorry We're Closed (EPIC) | 21 | 2026-11-09 | 35 | 70% |  |
| 225 | [x] | Goose Goose Duck (STEAM) | 21 | 2026-11-18 | 32 | 71% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 226 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 91% |  |
| 227 | [x] | Sapphire Safari (GOG) | 21 | 2026-11-20 | 28 | 70% | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 228 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 21 | 2026-11-09 | 27 | 91% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 229 | [x] | CarX Street (STEAM) | 21 | 2026-11-09 | 26 | 76% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 230 | [x] | Dead Island (STEAM) | 21 | 2026-11-09 | 26 | 91% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 231 | [x] | Tearscape (STEAM) | 21 | 2026-11-09 | 25 | 88% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 232 | [x] | Worms W.M.D (STEAM) | 20 | 2026-11-09 | 37 | 97% |  |
| 233 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-11-09 | 36 | 93% |  |
| 234 | [x] | Return to Monkey Island (STEAM) | 20 | 2026-11-09 | 33 | 68% |  |
| 235 | [x] | Torchlight II (EPIC) | 20 | 2026-11-09 | 28 | 77% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 236 | [x] | Tyr (STEAM) | 20 | 2026-11-09 | 28 | 64% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 237 | [x] | Tales of Zestiria (STEAM) | 20 | 2026-11-09 | 26 | 67% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 238 | [x] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 2026-11-15 | 36 | 70% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 239 | [x] | Pinball FX Classic (STEAM) | 19 | 2026-11-09 | 36 | 86% |  |
| 240 | [x] | SWORN (STEAM) | 19 | 2026-11-09 | 34 | 93% |  |
| 241 | [x] | One-armed robber (STEAM) | 19 | 2026-11-09 | 33 | 76% |  |
| 242 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 32 | 69% |  |
| 243 | [x] | Moonlight Peaks (STEAM) | 19 | 2026-11-09 | 32 | 71% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 244 | [x] | Asterigos: Curse of the Stars (STEAM) | 19 | 2026-11-20 | 31 | 80% |  |
| 245 | [x] | GOD EATER RESURRECTION (STEAM) | 19 | 2026-11-09 | 30 | 76% |  |
| 246 | [x] | Backpack Battles (STEAM) | 18 | 2026-11-09 | 42 | 93% |  |
| 247 | [x] | Mini Metro (STEAM) | 18 | 2026-11-16 | 37 | 62% |  |
| 248 | [x] | This War of Mine (STEAM) | 18 | 2026-11-17 | 34 | 46% |  |
| 249 | [x] | Far Far West (STEAM) | 18 | 2026-11-09 | 32 | 52% |  |
| 250 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 2026-11-09 | 29 | 76% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 251 | [x] | Beyond: Two Souls (STEAM) | 18 | 2026-11-19 | 27 | 62% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 252 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-11-09 | 27 | 80% |  |
| 253 | [x] | Bongo Cat (STEAM) | 18 | 2026-11-20 | 24 | 61% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 254 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-18 | 23 | 73% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 255 | [x] | Mafia II: Definitive Edition (GOG) | 18 | 2026-11-15 | 20 | 60% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 256 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 37 | 23% |  |
| 257 | [x] | Intravenous 2 (STEAM) | 17 | 2026-11-09 | 33 | 96% |  |
| 258 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 33 | 86% |  |
| 259 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 17 | 2026-11-09 | 27 | 92% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 260 | [x] | Capcom Fighting Collection (STEAM) | 17 | 2026-11-09 | 25 | 88% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 261 | [x] | Party Animals (STEAM) | 17 | 2026-11-09 | 25 | 77% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 262 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 263 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 264 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 16 | 2026-10-25 | 42 | 72% |  |
| 265 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 16 | 2026-11-11 | 35 | 71% |  |
| 266 | [x] | GRIP: Combat Racing (STEAM) | 16 | 2026-11-09 | 35 | 76% |  |
| 267 | [x] | sobosuba (STEAM) | 16 | 2026-11-09 | 35 | 84% |  |
| 268 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 269 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 16 | 2026-11-09 | 30 | 76% |  |
| 270 | [x] | Legend of Grimrock 2 (STEAM) | 16 | 2026-11-09 | 26 | 92% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 271 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 65% |  |
| 272 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 273 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 274 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 15 | 2026-10-21 | 42 | 79% |  |
| 275 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 31 | 96% |  |
| 276 | [x] | Tiny Glade (STEAM) | 15 | 2026-11-09 | 30 | 73% |  |
| 277 | [x] | Titanfall® 2 (STEAM) | 15 | 2026-11-09 | 29 | 73% |  |
| 278 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 15 | 2026-11-20 | 29 | 80% |  |
| 279 | [x] | GRANDIA HD Remaster (STEAM) | 15 | 2026-11-09 | 28 | 89% |  |
| 280 | [x] | PAYDAY: The Heist (STEAM) | 15 | 2026-11-13 | 27 | 69% |  |
| 281 | [x] | Gloomwood (STEAM) | 15 | 2026-11-19 | 26 | 62% |  |
| 282 | [x] | AER Memories of Old (EPIC) | 15 | 2026-11-09 | 25 | 93% |  |
| 283 | [x] | Alabaster Dawn Demo (STEAM) | 15 | 2026-11-09 | 23 | 76% |  |
| 284 | [x] | Need for Speed™ Unbound (STEAM) | 15 | 2026-11-09 | 23 | 58% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 285 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 93% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 286 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 287 | [x] | Spark the Electric Jester (STEAM) | 15 | 2026-11-13 | 21 | 69% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 288 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 15 | 2026-11-09 | 21 | 82% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 289 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 290 | [x] | ABZÛ (STEAM) | 14 | 2026-10-21 | 44 | 91% |  |
| 291 | [x] | Faster Than Light (EPIC) | 14 | 2026-11-09 | 31 | 92% |  |
| 292 | [x] | Mark of the Ninja (STEAM) | 14 | 2026-10-26 | 31 | 93% |  |
| 293 | [x] | Flotsam (EPIC) | 14 | 2026-11-20 | 30 | 42% |  |
| 294 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 94% |  |
| 295 | [x] | Hitman: Absolution (GOG) | 14 | 2026-11-09 | 29 | 82% |  |
| 296 | [x] | Castle in the Clouds (STEAM) | 14 | 2026-11-09 | 28 | 59% |  |
| 297 | [x] | Evoland (STEAM) | 14 | 2026-11-11 | 28 | n/a |  |
| 298 | [x] | Human Fall Flat (STEAM) | 14 | 2026-10-29 | 28 | 61% |  |
| 299 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 14 | 2026-11-09 | 27 | 61% |  |
| 300 | [x] | Ultrapool (STEAM) | 14 | 2026-11-09 | 27 | n/a |  |
| 301 | [x] | WORLD OF FINAL FANTASY (STEAM) | 14 | 2026-11-09 | 27 | 87% |  |
| 302 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 14 | 2026-11-15 | 23 | 61% |  |
| 303 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-11-09 | 22 | 91% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 304 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 305 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 2026-11-16 | 22 | 88% |  |
| 306 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 21 | 67% |  |
| 307 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 308 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 309 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 13 | 2026-11-09 | 28 | 88% |  |
| 310 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 28 | 83% |  |
| 311 | [x] | MX Bikes (STEAM) | 13 | 2026-11-09 | 27 | 92% |  |
| 312 | [x] | Blaster Master Zero (STEAM) | 13 | 2026-11-11 | 26 | 79% |  |
| 313 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 26 | 81% |  |
| 314 | [x] | Batman™: Arkham Origins (GOG) | 13 | 2026-11-09 | 25 | 100% |  |
| 315 | [x] | Cruelty Squad (STEAM) | 13 | 2026-11-09 | 25 | 86% |  |
| 316 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 13 | 2026-11-13 | 25 | 70% |  |
| 317 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 24 | 78% |  |
| 318 | [x] | Haydee (STEAM) | 13 | 2026-11-09 | 23 | 79% |  |
| 319 | [x] | The Stanley Parable (STEAM) | 13 | 2026-11-13 | 22 | 82% |  |
| 320 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 321 | [x] | Nex Machina (STEAM) | 13 | 2026-11-09 | 21 | 72% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 322 | [x] | Shift At Midnight (STEAM) | 13 | 2026-11-09 | 21 | 90% |  |
| 323 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 70% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 324 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 100% |  |
| 325 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 326 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 2026-11-09 | 20 | 85% |  |
| 327 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-11-16 | 20 | 92% |  |
| 328 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 80% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 329 | [x] | Overlord (STEAM) | 12 | 2026-11-08 | 29 | 58% |  |
| 330 | [x] | Antichamber (STEAM) | 12 | 2026-11-18 | 27 | 80% |  |
| 331 | [x] | A Plague Tale: Innocence (GOG) | 12 | 2026-11-18 | 24 | 60% |  |
| 332 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-10 | 24 | 60% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 333 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 24 | 67% |  |
| 334 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-11-09 | 22 | 97% |  |
| 335 | [x] | 12 is Better Than 6 (STEAM) | 12 | 2026-11-09 | 21 | 77% |  |
| 336 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 337 | [x] | Horny Villa (STEAM) | 12 | 2026-11-09 | 21 | 85% |  |
| 338 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 339 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 340 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 2026-11-10 | 20 | 60% |  |
| 341 | [x] | Turbo Overkill (STEAM) | 12 | 2026-11-09 | 20 | 95% |  |
| 342 | [x] | Haiku, the Robot (STEAM) | 11 | 2026-10-21 | 27 | n/a |  |
| 343 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 2026-11-09 | 26 | 88% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 344 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 25 | 85% |  |
| 345 | [x] | Alan Wake's American Nightmare (EPIC) | 11 | 2026-11-09 | 24 | 67% |  |
| 346 | [x] | Need for Speed: Undercover (STEAM) | 11 | 2026-11-11 | 24 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 347 | [x] | Life is Strange Remastered (STEAM) | 11 | 2026-11-09 | 23 | 86% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 348 | [x] | Ready or Not (STEAM) | 11 | 2026-11-09 | 23 | 84% |  |
| 349 | [x] | Lost Castle 2 (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 350 | [x] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 2026-11-18 | 21 | 64% |  |
| 351 | [x] | Forgive Me Father (STEAM) | 11 | 2026-11-15 | 21 | 74% |  |
| 352 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 353 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-11-09 | 20 | 74% |  |
| 354 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 355 | [x] | The WereCleaner (STEAM) | 10 | 2026-10-22 | 31 | 89% |  |
| 356 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 28 | 90% |  |
| 357 | [x] | Possessor(s) (STEAM) | 10 | 2026-10-24 | 27 | 75% |  |
| 358 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 10 | 2026-10-27 | 25 | 82% |  |
| 359 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 25 | 83% |  |
| 360 | [x] | Soul's Remnant (STEAM) | 10 | 2026-11-11 | 25 | n/a |  |
| 361 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 10 | 2026-11-01 | 24 | n/a |  |
| 362 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 10 | 2026-10-23 | 24 | 88% |  |
| 363 | [x] | Breath of Fire IV (GOG) | 10 | 2026-10-26 | 23 | 72% |  |
| 364 | [x] | Guacamelee! Gold Edition (STEAM) | 10 | 2026-11-11 | 23 | 75% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 365 | [x] | DiRT 4 (STEAM) | 10 | 2026-11-09 | 22 | 100% |  |
| 366 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 10 | 2026-11-09 | 22 | 75% |  |
| 367 | [x] | UNDEFEATED (STEAM) | 10 | 2026-11-09 | 21 | 70% |  |
| 368 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 369 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 370 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 20 | 76% |  |
| 371 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 372 | [x] | Secret of Mana (STEAM) | 10 | 2026-11-18 | 20 | 70% |  |
| 373 | [x] | Rayman Origins (GOG) | 9 | 2026-11-09 | 23 | 69% |  |
| 374 | [x] | Aperture Desk Job (STEAM) | 9 | 2026-11-03 | 22 | n/a |  |
| 375 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 9 | 2026-10-21 | 21 | 92% |  |
| 376 | [x] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 9 | 2026-11-17 | 20 | 30% |  |
| 377 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 27% |  |
| 378 | [x] | Lust Goddess (STEAM) | 8 | 2026-11-09 | 22 | 81% |  |
| 379 | [x] | SteamWorld Heist (GOG) | 8 | 2026-10-25 | 20 | n/a |  |
| 380 | [x] | HITMAN World of Assassination (STEAM) | 8 | 2026-11-09 | 20 | 81% |  |
| 381 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 21 | 51% |  |
| 382 | [x] | SCP – Containment Breach (STEAM) | 7 | 2026-10-27 | 21 | 91% |  |
| 383 | [x] | Mina the Hollower (GOG) | 7 | 2026-10-28 | 20 | 74% |  |
| 384 | [x] | CULTIC (STEAM) | 7 | 2026-11-09 | 20 | 56% |  |
