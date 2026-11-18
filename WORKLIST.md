# GameNative compatibility worklist

Generated: `2026-11-18T04:15:12.699Z` · Ratings since: `2026-08-20T04:15:12.699Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Probably does not work | 189 |
| Fix shipped, waiting for ratings | 16 |
| First launch fails | 301 |
| Mixed | 486 |
| Works | 1026 |
| Total | 2143 |

## Does not work (125)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 155 | 179 | 87% (14d) | Does not open (83%) | 51% | today | 21% (drop) | [#484](https://github.com/GameNative/gamenative-compat/issues/484) |
| 2 | [ ] | Grand Theft Auto IV: The Complete Edition (STEAM) | 127 | 148 | 86% (since fix) | Does not open (92%) | 45% | today | 37% | [#524](https://github.com/GameNative/gamenative-compat/issues/524) |
| 3 | [ ] | Rocket League® (EPIC) | 76 | 89 | 85% (14d) | Does not open (79%) | 46% | today | 29% | [#488](https://github.com/GameNative/gamenative-compat/issues/488) |
| 4 | [ ] | Hogwarts Legacy (STEAM) | 32 | 32 | 100% (14d) | Does not open (67%) | 34% | today | 17% | [#500](https://github.com/GameNative/gamenative-compat/issues/500) |
| 5 | [x] 2026-10-18 | Project Zomboid (STEAM) | 57 | 63 | 90% (since fix) | Does not open (64%) | 44% | today | 39% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 6 | [ ] | Bloons TD 6 (EPIC) | 23 | 27 | 85% (14d) | Does not open (77%) | 40% | 1d ago | 23% | [#525](https://github.com/GameNative/gamenative-compat/issues/525) |
| 7 | [ ] | Melvor Idle 2: A RuneScape Adventure (STEAM) | 22 | 23 | 96% (14d) | Does not open (100%) | 21% | today | 19% |  |
| 8 | [ ] | Saints Row 2 (STEAM) | 21 | 21 | 100% (14d) | Does not open (97%) | 32% | 2d ago | 31% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 9 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 21 | 25 | 84% (14d) | Does not open (75%) | 59% | today | 58% | [#507](https://github.com/GameNative/gamenative-compat/issues/507) |
| 10 | [ ] | KINGDOM HEARTS HD 1.5+2.5 ReMIX (EPIC) | 21 | 23 | 91% (14d) | Does not open (96%) | 40% | 3d ago | 20% (drop) | [#531](https://github.com/GameNative/gamenative-compat/issues/531) |
| 11 | [ ] | Borderlands 2 (EPIC) | 19 | 21 | 90% (14d) | Does not open (80%) | 52% | today | 48% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 12 | [ ] | Saints Row 2 (GOG) | 18 | 23 | 78% (14d) | Does not open (90%) | 39% | today | 34% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 13 | [ ] | Sifu (EPIC) | 17 | 22 | 77% (14d) | Does not open (71%) | 48% | today | 36% | [#535](https://github.com/GameNative/gamenative-compat/issues/535) |
| 14 | [ ] | Mafia II (Classic) (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 10% | today | 12% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 15 | [ ] | Metro: Last Light Redux (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | 22% | 1d ago | 25% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 16 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 15 | 20 | 75% (last 20) | Does not open (75%) | 54% | today | 45% | [#493](https://github.com/GameNative/gamenative-compat/issues/493) |
| 17 | [ ] | Call of Duty: Black Ops II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 38% | 3d ago | 39% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 18 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 20 | 20 | 100% (last 20) | Does not open (76%) | 0% | 9d ago | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 19 | [ ] | Fallout: New Vegas PCR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (93%) | 58% | today | 59% | [#501](https://github.com/GameNative/gamenative-compat/issues/501) |
| 20 | [ ] | Enshrouded (STEAM) | 16 | 20 | 80% (last 20) | Does not open (92%) | 25% | 4d ago | 19% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 21 | [ ] | skate. (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | 11% | today | 15% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 22 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | No graphics (46%) | 30% | 2d ago | 40% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 23 | [ ] | Path of Exile (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 26% | 1d ago | 19% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 24 | [ ] | CARRION (GOG) | 19 | 20 | 95% (last 20) | Does not open (78%) | 0% | 3d ago | 0% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 25 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | 40% | today | 30% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 26 | [ ] | Forza Horizon 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (45%) | 56% | today | 23% (drop) | [#514](https://github.com/GameNative/gamenative-compat/issues/514) |
| 27 | [ ] | Hogwarts Legacy (EPIC) | 14 | 20 | 70% (last 20) | Does not open (75%) | 53% | 1d ago | 43% | [#537](https://github.com/GameNative/gamenative-compat/issues/537) |
| 28 | [ ] | Vampire Survivors (EPIC) | 16 | 20 | 80% (last 20) | Does not open (58%) | 47% | today | 29% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 29 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (70%) | 20% | 12d ago | n/a | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 30 | [ ] | Detroit: Become Human (STEAM) | 18 | 20 | 90% (last 20) | Does not open (76%) | 59% | today | 64% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 31 | [ ] | AION 2 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (67%) | 8% | 4d ago | n/a | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 32 | [ ] | Kenshi (STEAM) | 18 | 20 | 90% (last 20) | Does not open (90%) | 4% | today | 0% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 33 | [ ] | Saints Row: The Third (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 13% | 6d ago | 8% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 34 | [ ] | The Witcher: Enhanced Edition (GOG) | 19 | 20 | 95% (last 20) | Does not open (74%) | 7% | 9d ago | 7% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 35 | [ ] | Fall Guys (EPIC) | 19 | 20 | 95% (last 20) | Does not open (74%) | 16% | 3d ago | 7% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 36 | [ ] | CPM 2 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 8% | 2d ago | 6% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 37 | [ ] | Dust: An Elysian Tail (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | 15% | 2d ago | 25% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 38 | [ ] | ScourgeBringer (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | 0% | 3d ago | n/a | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 39 | [ ] | Trackmania (STEAM) | 16 | 20 | 80% (last 20) | Does not open (82%) | 21% | 2d ago | 31% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 40 | [ ] | Deliver At All Costs (EPIC) | 14 | 20 | 70% (last 20) | Does not open (60%) | 50% | 2d ago | 45% | [#538](https://github.com/GameNative/gamenative-compat/issues/538) |
| 41 | [ ] | HELLDIVERS™ 2 (STEAM) | 18 | 20 | 90% (last 20) | Does not open (93%) | 9% | today | n/a | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 42 | [ ] | Call of Duty® (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | 0% | 1d ago | 0% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 43 | [ ] | Breath of Fire IV (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | 15% | 1d ago | 7% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 44 | [ ] | GRID 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (70%) | 12% | 17d ago | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 45 | [ ] | Borderlands GOTY (STEAM) | 17 | 20 | 85% (last 20) | Does not open (94%) | 39% | 5d ago | 46% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 46 | [ ] | MECCHA CHAMELEON (STEAM) | 15 | 20 | 75% (last 20) | Does not open (67%) | 47% | today | 33% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 47 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 14 | 20 | 70% (last 20) | Does not open (60%) | 50% | 2d ago | n/a | [#536](https://github.com/GameNative/gamenative-compat/issues/536) |
| 48 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 19 | 20 | 95% (last 20) | Does not open (88%) | 23% | 9d ago | n/a | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 49 | [ ] | Far Cry® 3 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (84%) | 56% | 8d ago | 35% (drop) | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 50 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 17 | 20 | 85% (last 20) | Does not open (80%) | 15% | 9d ago | 18% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 51 | [ ] | The Wolf Among Us (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | 19% | 4d ago | 30% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 52 | [ ] | Watch_Dogs 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (97%) | 56% | 2d ago | 55% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 53 | [ ] | Scott Pilgrim vs The World (STEAM) | 20 | 20 | 100% (last 20) | Does not open (83%) | 41% | today | 44% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 54 | [ ] | Spore (STEAM) | 16 | 20 | 80% (last 20) | Does not open (68%) | 28% | 6d ago | 27% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 55 | [ ] | GrandChase (STEAM) | 20 | 20 | 100% (last 20) | Does not open (77%) | 11% | 3d ago | 9% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 56 | [ ] | Tales of Berseria (STEAM) | 20 | 20 | 100% (last 20) | Does not open (89%) | 0% | 4d ago | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 57 | [ ] | Axiom Verge 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (54%) | 25% | today | 18% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 58 | [ ] | VALORANT (EPIC) | 16 | 20 | 80% (last 20) | Does not open (88%) | 50% | 5d ago | 53% | [#527](https://github.com/GameNative/gamenative-compat/issues/527) |
| 59 | [ ] | Blood Omen: Legacy of Kain (GOG) | 16 | 20 | 80% (last 20) | No graphics (57%) | 58% | 2d ago | n/a | [#539](https://github.com/GameNative/gamenative-compat/issues/539) |
| 60 | [ ] | Chained Echoes (GOG) | 14 | 20 | 70% (last 20) | Does not open (60%) | 58% | today | 50% | [#542](https://github.com/GameNative/gamenative-compat/issues/542) |
| 61 | [ ] | Marvel Rivals (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 0% | 3d ago | n/a | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 62 | [ ] | Half-Life: Blue Shift (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | 38% | 1d ago | 45% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 63 | [ ] | Rivals of Aether II (STEAM) | 16 | 20 | 80% (last 20) | Does not open (56%) | 45% | 1d ago | 6% (drop) | [#512](https://github.com/GameNative/gamenative-compat/issues/512) |
| 64 | [ ] | Super Animal Royale (STEAM) | 15 | 20 | 75% (last 20) | Does not open (73%) | 50% | 6d ago | n/a | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 65 | [ ] | South Park The Fractured But Whole (STEAM) | 20 | 20 | 100% (last 20) | Does not open (92%) | 29% | 1d ago | 41% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 66 | [ ] | STAR WARS™ Republic Commando (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | 50% | 39d ago | n/a | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 67 | [ ] | Hitman: Absolution (STEAM) | 16 | 20 | 80% (last 20) | Does not open (84%) | 30% | 9d ago | 38% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 68 | [ ] | WRC 7 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | 10% | 5d ago | 10% | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 69 | [ ] | Rayman Legends (STEAM) | 19 | 20 | 95% (last 20) | Does not open (91%) | 35% | 4d ago | 42% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 70 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (75%) | 36% | 6d ago | 18% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 71 | [ ] | Beat Saber (STEAM) | 17 | 20 | 85% (last 20) | Does not open (45%) | 43% | 13d ago | 41% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 72 | [ ] | Black Mesa (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | 20% | today | 27% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 73 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | 42% | 1d ago | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 74 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | 36% | 1d ago | 30% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 75 | [ ] | Watch_Dogs (STEAM) | 14 | 20 | 70% (last 20) | Does not open (90%) | 39% | 11d ago | 46% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 76 | [ ] | The Darkness II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 25% | 27d ago | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 77 | [ ] | DJMAX RESPECT V (STEAM) | 19 | 20 | 95% (last 20) | Does not open (78%) | 30% | 37d ago | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 78 | [ ] | XCOM: Enemy Unknown (STEAM) | 18 | 20 | 90% (last 20) | Does not open (71%) | 18% | 4d ago | n/a | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 79 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 16 | 20 | 80% (last 20) | Does not open (71%) | 30% | 11d ago | 23% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 80 | [ ] | Fortune Mill (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | 10% | 16d ago | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 81 | [ ] | Beyond: Two Souls (STEAM) | 15 | 20 | 75% (last 20) | Does not open (61%) | 58% | 6d ago | 56% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 82 | [ ] | Spec Ops: The Line (STEAM) | 20 | 20 | 100% (last 20) | Does not open (63%) | 19% | 11d ago | 33% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 83 | [ ] | Hitman: Blood Money (STEAM) | 19 | 20 | 95% (last 20) | Does not open (80%) | 18% | 16d ago | n/a | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 84 | [ ] | Diablo + Hellfire (GOG) | 16 | 20 | 80% (last 20) | Does not open (59%) | 30% | 3d ago | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 85 | [ ] | SteamVR (STEAM) | 16 | 20 | 80% (last 20) | Does not open (83%) | 3% | 6d ago | 1% | [#528](https://github.com/GameNative/gamenative-compat/issues/528) |
| 86 | [ ] | Isle of Reveries (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 12% | 18d ago | n/a | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 87 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (60%) | 47% | 6d ago | 60% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 88 | [ ] | Cyberpunk 2077 (EPIC) | 18 | 20 | 90% (last 20) | Does not open (50%) | 56% | 1d ago | 54% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 89 | [ ] | Split/Second (STEAM) | 17 | 20 | 85% (last 20) | Does not open (76%) | 0% | 31d ago | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 90 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 17 | 20 | 85% (last 20) | Does not open (67%) | 0% | 24d ago | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 91 | [ ] | Umamusume: Pretty Derby (STEAM) | 19 | 20 | 95% (last 20) | Does not open (83%) | 50% | 1d ago | 57% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 92 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 19 | 20 | 95% (last 20) | No graphics (57%) | 39% | 4d ago | 50% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 93 | [ ] | Mass Effect (2007) (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | 23% | 1d ago | 27% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 94 | [ ] | State of Decay 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 0% | 24d ago | 0% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 95 | [ ] | Mafia: Definitive Edition (GOG) | 17 | 20 | 85% (last 20) | Does not open (90%) | 21% | 10d ago | n/a | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 96 | [ ] | Mafia (STEAM) | 17 | 20 | 85% (last 20) | Does not open (67%) | 36% | today | n/a | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 97 | [ ] | tModLoader (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 3% | 13d ago | 5% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 98 | [ ] | FINAL FANTASY VIII (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 46% | 6d ago | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 99 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 20 | 95% (last 20) | Does not open (86%) | 36% | 8d ago | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 100 | [ ] | OneShot (STEAM) | 16 | 20 | 80% (last 20) | Does not open (96%) | 15% | 33d ago | n/a | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 101 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 20 | 80% (last 20) | Does not open (47%) | 59% | 4d ago | 29% (drop) | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 102 | [ ] | Lost Planet: Extreme Condition (STEAM) | 14 | 20 | 70% (last 20) | Does not open (80%) | 38% | 3d ago | n/a | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 103 | [ ] | DNF Duel (EPIC) | 14 | 20 | 70% (last 20) | Does not open (62%) | 53% | 6d ago | 22% (drop) | [#540](https://github.com/GameNative/gamenative-compat/issues/540) |
| 104 | [ ] | Muv-Luv (STEAM) | 19 | 20 | 95% (last 20) | Does not open (95%) | 25% | 16d ago | n/a | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 105 | [ ] | Resident Evil (GOG) | 18 | 20 | 90% (last 20) | Does not open (90%) | 27% | 2d ago | 31% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 106 | [ ] | Asphalt Legends  (STEAM) | 17 | 20 | 85% (last 20) | Does not open (83%) | 50% | 3d ago | 46% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 107 | [ ] | Barotrauma (STEAM) | 17 | 20 | 85% (last 20) | Does not open (97%) | 30% | 16d ago | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 108 | [ ] | Aliens vs. Predator (STEAM) | 16 | 20 | 80% (last 20) | No graphics (58%) | 27% | 6d ago | 27% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 109 | [ ] | Insaniquarium! Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (88%) | 30% | 18d ago | n/a | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 110 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 17 | 20 | 85% (last 20) | Does not open (100%) | 30% | 32d ago | 30% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 111 | [ ] | Dark Sector (STEAM) | 15 | 20 | 75% (last 20) | Does not open (67%) | 50% | 7d ago | n/a | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 112 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | 43% | 18d ago | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 113 | [ ] | Path of Exile 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | 53% | 4d ago | 38% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 114 | [ ] | Zuma Deluxe (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | 31% | 5d ago | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 115 | [ ] | Maneater (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 54% | 4d ago | 50% | [#534](https://github.com/GameNative/gamenative-compat/issues/534) |
| 116 | [ ] | Ultimate Custom Night (STEAM) | 14 | 20 | 70% (last 20) | No graphics (71%) | 57% | 20d ago | n/a | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 117 | [ ] | skate.™ (EPIC) | 18 | 20 | 90% (last 20) | Does not open (87%) | 0% | 23d ago | n/a | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 118 | [ ] | Bongo Cat (STEAM) | 16 | 20 | 80% (last 20) | Does not open (85%) | 57% | today | 33% (drop) | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 119 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 20 | 80% (last 20) | Does not open (82%) | 59% | 2d ago | n/a | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 120 | [ ] | Yakuza 0 (GOG) | 14 | 20 | 70% (last 20) | Does not open (67%) | 57% | 9d ago | n/a | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 121 | [ ] | Maneater (EPIC) | 16 | 20 | 80% (last 20) | Does not open (73%) | 40% | 2d ago | 20% (drop) | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 122 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (54%) | 54% | 3d ago | n/a | [#541](https://github.com/GameNative/gamenative-compat/issues/541) |
| 123 | [ ] | Hitman 2: Silent Assassin (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 33% | 1d ago | 36% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 124 | [ ] | Ghostwire Tokyo (EPIC) | 14 | 20 | 70% (last 20) | Does not open (91%) | 58% | 3d ago | 38% (drop) |  |
| 125 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 50% | 10d ago | 50% | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |

## Probably does not work (189)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Counter-Strike 2 (STEAM) | 44 | 67 | 66% (since fix) | Does not open (68%) | 59% | today | 62% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 2 | [ ] | theHunter Classic (STEAM) | 20 | 20 | 100% (last 20) | No graphics (92%) | n/a | 14d ago | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 3 | [ ] | Metro 2033 Redux (STEAM) | 17 | 26 | 65% (14d) | Does not open (70%) | 43% | today | 41% | [#490](https://github.com/GameNative/gamenative-compat/issues/490) |
| 4 | [ ] | Euro Truck Simulator 2 (STEAM) | 16 | 26 | 62% (14d) | Does not open (65%) | 56% | 1d ago | 55% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 5 | [ ] | To The Moon (GOG) | 18 | 20 | 90% (last 20) | Does not open (86%) | n/a | 15d ago | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 6 | [ ] | Owlboy (STEAM) | 14 | 21 | 67% (14d) | Does not open (81%) | 50% | today | 45% |  |
| 7 | [ ] | FINAL FANTASY XIII (STEAM) | 13 | 21 | 62% (14d) | Does not open (75%) | 54% | today | 57% |  |
| 8 | [ ] | Bully: Scholarship Edition (STEAM) | 12 | 22 | 55% (14d) | Does not open (62%) | 49% | today | 11% (drop) |  |
| 9 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 13 | 20 | 65% (last 20) | Does not open (61%) | 46% | 3d ago | 36% |  |
| 10 | [ ] | VRChat (STEAM) | 13 | 20 | 65% (last 20) | Does not open (70%) | 39% | today | 34% |  |
| 11 | [ ] | Garry's Mod (STEAM) | 9 | 17 | 53% (since fix) | Does not open (80%) | 55% | 1d ago | 44% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 12 | [ ] | Driver: Parallel Lines (STEAM) | 19 | 20 | 95% (last 20) | Does not open (65%) | n/a | 9d ago | n/a | [#522](https://github.com/GameNative/gamenative-compat/issues/522) |
| 13 | [ ] | Asterigos: Curse of the Stars (STEAM) | 17 | 20 | 85% (last 20) | Graphics glitches (73%) | n/a | 1d ago | n/a |  |
| 14 | [ ] | Gorilla Tag (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 14% | 3d ago | 9% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 15 | [ ] | Door Kickers 2 (STEAM) | 20 | 20 | 100% (last 20) | No graphics (86%) | n/a | 35d ago | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 16 | [ ] | Teenage Mutant Ninja Turtles: Shredder's Revenge (EPIC) | 13 | 20 | 65% (last 20) | Does not open (82%) | 57% | 2d ago | 44% |  |
| 17 | [ ] | Marie's Adventure (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 38d ago | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 18 | [ ] | RoboCop: Rogue City (STEAM) | 20 | 20 | 100% (last 20) | Directx error (36%) | n/a | 15d ago | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 19 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 7 | 11 | 64% (since fix) | Does not open (91%) | 44% | today | 50% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 20 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 12 | 20 | 60% (last 20) | Does not open (72%) | 35% | today | 42% |  |
| 21 | [ ] | DOOM 64 (EPIC) | 10 | 20 | 50% (last 20) | Does not open (58%) | 54% | today | 34% (drop) |  |
| 22 | [ ] | Yume Nikki (STEAM) | 10 | 20 | 50% (last 20) | Does not open (87%) | 35% | today | 53% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 23 | [ ] | Three Kingdoms : Alias (STEAM) | 20 | 20 | 100% (last 20) | No graphics (97%) | n/a | 22d ago | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 24 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 11 | 19 | 58% (since fix) | Does not open (78%) | 30% | 2d ago | 37% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 25 | [ ] | Sable (EPIC) | 11 | 20 | 55% (last 20) | No graphics (38%) | 52% | 3d ago | 32% (drop) |  |
| 26 | [ ] | Cat Quest (EPIC) | 10 | 20 | 50% (last 20) | Does not open (45%) | 49% | 1d ago | 34% |  |
| 27 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 20 | 20 | 100% (last 20) | Does not open (54%) | n/a | 21d ago | n/a | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 28 | [ ] | DOOM (2016) (GOG) | 17 | 20 | 85% (last 20) | Does not open (88%) | n/a | 11d ago | n/a | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 29 | [ ] | Metro 2033 Redux (EPIC) | 11 | 20 | 55% (last 20) | Does not open (55%) | 25% | 3d ago | 36% |  |
| 30 | [ ] | Sonic Adventure™ 2  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (76%) | 47% | 6d ago | 38% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 31 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 12 | 20 | 60% (last 20) | Does not open (86%) | 59% | today | 30% (drop) | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 32 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 11 | 20 | 55% (last 20) | Does not open (64%) | 5% | 1d ago | n/a |  |
| 33 | [ ] | Sniper Elite 4 (STEAM) | 20 | 20 | 100% (last 20) | Does not open (97%) | n/a | 19d ago | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 34 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 18 | 20 | 90% (last 20) | Does not open (58%) | n/a | 4d ago | n/a | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 35 | [ ] | ARC Raiders (STEAM) | 19 | 20 | 95% (last 20) | Does not open (93%) | n/a | 1d ago | n/a | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 36 | [ ] | Transformers: Fall of Cybertron (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | n/a | 10d ago | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 37 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 13 | 20 | 65% (last 20) | Does not open (83%) | 55% | 7d ago | 68% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 38 | [ ] | CODE VEIN (STEAM) | 13 | 20 | 65% (last 20) | Does not open (69%) | 39% | 2d ago | 23% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 39 | [ ] | Katana ZERO (GOG) | 13 | 20 | 65% (last 20) | Does not open (85%) | 45% | 8d ago | n/a |  |
| 40 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 20% | 3d ago | 8% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 41 | [ ] | Sleeping Dogs™ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (88%) | n/a | 3d ago | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 42 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 18 | 20 | 90% (last 20) | Controller issues (100%) | n/a | 7d ago | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 43 | [ ] | BAJA: Edge of Control HD (STEAM) | 15 | 20 | 75% (last 20) | Does not open (100%) | n/a | 13d ago | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 44 | [ ] | GRID (STEAM) | 10 | 20 | 50% (last 20) | Does not open (58%) | 40% | 3d ago | 50% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 45 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 20 | 20 | 100% (last 20) | Does not open (66%) | n/a | 16d ago | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 46 | [ ] | Forza Horizon 5 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (71%) | n/a | 3d ago | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 47 | [ ] | Northgard: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (100%) | n/a | 17d ago | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 48 | [ ] | Grim Dawn (GOG) | 13 | 20 | 65% (last 20) | Does not open (69%) | 40% | 2d ago | n/a | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 49 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 20 | 20 | 100% (last 20) | Does not open (94%) | n/a | today | n/a | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 50 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 20 | 20 | 100% (last 20) | Does not open (68%) | n/a | 15d ago | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 51 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 7d ago | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 52 | [ ] | Hollow Knight: Silksong (GOG) | 12 | 20 | 60% (last 20) | Does not open (70%) | 53% | 1d ago | 50% |  |
| 53 | [ ] | Quantum Break (STEAM) | 20 | 20 | 100% (last 20) | Does not open (90%) | n/a | 36d ago | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 54 | [ ] | DOOM 3 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | n/a | 7d ago | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 55 | [ ] | HELLDIVERS™ (STEAM) | 13 | 20 | 65% (last 20) | Does not open (58%) | 41% | 1d ago | 53% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 56 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 55% | 1d ago | 32% (drop) | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 57 | [ ] | STAR WARS Zero Company™ (STEAM) | 20 | 20 | 100% (last 20) | Does not open (64%) | n/a | 35d ago | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 58 | [ ] | Alpha Protocol (STEAM) | 17 | 20 | 85% (last 20) | No graphics (53%) | n/a | 23d ago | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 59 | [ ] | Dead Space 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 25% | 8d ago | 34% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 60 | [ ] | METAL SLUG 3 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (78%) | 54% | 5d ago | 71% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 61 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 19 | 20 | 95% (last 20) | Does not open (79%) | n/a | 4d ago | n/a | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 62 | [ ] | Forza Horizon 6 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (57%) | n/a | 4d ago | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 63 | [ ] | DOOM Eternal (STEAM) | 18 | 20 | 90% (last 20) | Does not open (66%) | n/a | 26d ago | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 64 | [ ] | BattleBit Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (63%) | n/a | 19d ago | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 65 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (last 20) | No graphics (88%) | n/a | 21d ago | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 66 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 15 | 20 | 75% (last 20) | Does not open (87%) | n/a | 28d ago | n/a | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 67 | [ ] | Duskfade (STEAM) | 20 | 20 | 100% (last 20) | Does not open (95%) | n/a | 38d ago | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 68 | [ ] | DiRT Showdown (STEAM) | 20 | 20 | 100% (last 20) | Does not open (54%) | n/a | 13d ago | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 69 | [ ] | Dragon's Dogma 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (90%) | n/a | 35d ago | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 70 | [ ] | Death Stranding (EPIC) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 35d ago | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 71 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | today | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 72 | [ ] | My Singing Monsters (STEAM) | 16 | 20 | 80% (last 20) | Does not open (87%) | n/a | 10d ago | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 73 | [ ] | The Swapper (STEAM) | 16 | 20 | 80% (last 20) | Does not open (48%) | n/a | 21d ago | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 74 | [ ] | Sol Cesto (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | n/a | 14d ago | n/a |  |
| 75 | [ ] | Fallout (GOG) | 12 | 20 | 60% (last 20) | Does not open (69%) | 29% | 8d ago | 20% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 76 | [ ] | Breathedge (STEAM) | 11 | 20 | 55% (last 20) | Does not open (55%) | 55% | 7d ago | 69% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 77 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 11 | 20 | 55% (last 20) | Does not open (92%) | 38% | 2d ago | n/a |  |
| 78 | [ ] | Euro Truck Simulator (STEAM) | 20 | 20 | 100% (last 20) | Does not open (88%) | n/a | 2d ago | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 79 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 20 | 20 | 100% (last 20) | Does not open (71%) | n/a | 46d ago | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 80 | [ ] | Wallachia: Reign of Dracula (STEAM) | 19 | 20 | 95% (last 20) | No graphics (95%) | n/a | 17d ago | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 81 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 4d ago | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 82 | [ ] | Borderlands 2 RU (STEAM) | 18 | 20 | 90% (last 20) | Does not open (61%) | n/a | 1d ago | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 83 | [ ] | Singularity™ (GOG) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 9d ago | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 84 | [ ] | GOALS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (83%) | n/a | 2d ago | n/a | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 85 | [ ] | Smushi Come Home (GOG) | 14 | 20 | 70% (last 20) | Does not open (54%) | n/a | 23d ago | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 86 | [ ] | Peggle Nights (STEAM) | 20 | 20 | 100% (last 20) | Does not open (100%) | n/a | 21d ago | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 87 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (last 20) | Does not open (47%) | n/a | 17d ago | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 88 | [ ] | Beholder (EPIC) | 18 | 20 | 90% (last 20) | Does not open (61%) | n/a | today | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 89 | [ ] | BIT.TRIP RUNNER (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | n/a | 40d ago | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 90 | [ ] | PRAGMATA (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | n/a | today | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 91 | [ ] | Mafia III: Definitive Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | n/a | 35d ago | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 92 | [ ] | Magicka (STEAM) | 17 | 20 | 85% (last 20) | Does not open (65%) | n/a | 44d ago | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 93 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 14 | 20 | 70% (last 20) | Does not open (94%) | n/a | 6d ago | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 94 | [ ] | They Are Billions (STEAM) | 19 | 20 | 95% (last 20) | Does not open (74%) | n/a | 14d ago | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 95 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 19 | 20 | 95% (last 20) | Does not open (94%) | n/a | 60d ago | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 96 | [ ] | The Survivalists (STEAM) | 18 | 20 | 90% (last 20) | Does not open (96%) | n/a | 5d ago | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 97 | [ ] | Persona 5 Strikers (STEAM) | 18 | 20 | 90% (last 20) | Does not open (80%) | n/a | 2d ago | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 98 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 20 | 90% (last 20) | Does not open (64%) | n/a | 1d ago | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 99 | [ ] | Wolfenstein 3D (STEAM) | 16 | 20 | 80% (last 20) | Does not open (50%) | n/a | 11d ago | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 100 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 20 | 80% (last 20) | Directx error (57%) | n/a | 13d ago | n/a |  |
| 101 | [ ] | A Plague Tale: Innocence (EPIC) | 11 | 20 | 55% (last 20) | Does not open (70%) | 36% | 4d ago | 20% |  |
| 102 | [ ] | Metro 2033 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 18% | 14d ago | n/a | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 103 | [ ] | Marvel's Spider-Man 2 (STEAM) | 19 | 20 | 95% (last 20) | Does not open (88%) | n/a | 37d ago | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 104 | [ ] | Alien Breed: Impact (STEAM) | 19 | 20 | 95% (last 20) | Does not open (89%) | n/a | 23d ago | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 105 | [ ] | Bionic Commando Rearmed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | n/a | 28d ago | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 106 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 18 | 20 | 90% (last 20) | Does not open (74%) | n/a | 22d ago | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 107 | [ ] | Dorfromantik (GOG) | 17 | 20 | 85% (last 20) | Does not open (94%) | n/a | 9d ago | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 108 | [ ] | Halo: Spartan Assault (STEAM) | 17 | 20 | 85% (last 20) | Does not open (76%) | n/a | 1d ago | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 109 | [ ] | Turing Complete (STEAM) | 17 | 20 | 85% (last 20) | Does not open (82%) | n/a | 11d ago | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 110 | [ ] | Far Cry 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 7d ago | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 111 | [ ] | SimCity 4 Deluxe (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 8d ago | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 112 | [ ] | Look Outside (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 6d ago | n/a |  |
| 113 | [ ] | Rise of the Tomb Raider: 20 Year Celebration (EPIC) | 11 | 20 | 55% (last 20) | Does not open (69%) | 49% | today | 36% |  |
| 114 | [ ] | Beyond Good & Evil™ (GOG) | 17 | 20 | 85% (last 20) | Does not open (100%) | n/a | 25d ago | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 115 | [ ] | Crysis® (GOG) | 17 | 20 | 85% (last 20) | Does not open (87%) | n/a | 1d ago | n/a |  |
| 116 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (72%) | n/a | 6d ago | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 117 | [ ] | Aggelos 2 (STEAM) | 16 | 20 | 80% (last 20) | No graphics (90%) | n/a | 19d ago | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 118 | [ ] | The Planet Crafter (STEAM) | 15 | 20 | 75% (last 20) | Does not open (44%) | n/a | 16d ago | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 119 | [ ] | SlashZero Demo (STEAM) | 14 | 20 | 70% (last 20) | Does not open (75%) | n/a | 20d ago | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 120 | [ ] | Drop Duchy (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 8% | 1d ago | n/a |  |
| 121 | [ ] | Evenicle (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (71%) | n/a | 13d ago | n/a |  |
| 122 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (last 20) | No graphics (50%) | n/a | 13d ago | n/a |  |
| 123 | [ ] | Fishing Planet (STEAM) | 12 | 20 | 60% (last 20) | Does not open (93%) | 55% | 6d ago | n/a | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 124 | [ ] | Marvel's Midnight Suns (STEAM) | 17 | 20 | 85% (last 20) | Does not open (81%) | n/a | 35d ago | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 125 | [ ] | ENDLESS Space™ 2 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | 33d ago | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 126 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 15 | 20 | 75% (last 20) | Does not open (81%) | n/a | 16d ago | n/a |  |
| 127 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (last 20) | No graphics (71%) | n/a | 6d ago | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 128 | [ ] | Audiosurf (STEAM) | 14 | 20 | 70% (last 20) | No graphics (43%) | n/a | 8d ago | n/a | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 129 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 14 | 20 | 70% (last 20) | Does not open (83%) | n/a | today | n/a | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 130 | [ ] | Romancing SaGa -Minstrel Song- Remastered (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (100%) | n/a | 2d ago | n/a |  |
| 131 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 13 | 20 | 65% (last 20) | Does not open (56%) | 50% | 6d ago | n/a |  |
| 132 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 13 | 20 | 65% (last 20) | Does not open (55%) | 50% | 2d ago | n/a | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 133 | [ ] | Mafia II (Classic) (GOG) | 13 | 20 | 65% (last 20) | Does not open (95%) | n/a | 3d ago | n/a | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 134 | [ ] | King's Bounty: The Legend (STEAM) | 16 | 20 | 80% (last 20) | Does not open (100%) | n/a | today | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 135 | [ ] | Re-Volt (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (71%) | n/a | 24d ago | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 136 | [ ] | DayZ (STEAM) | 15 | 20 | 75% (last 20) | Does not open (56%) | n/a | 2d ago | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 137 | [ ] | Fallout Classic (GOG) | 15 | 20 | 75% (last 20) | Does not open (88%) | n/a | 5d ago | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 138 | [ ] | Surviving Mars (STEAM) | 14 | 20 | 70% (last 20) | Does not open (93%) | n/a | 5d ago | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 139 | [ ] | TEKKEN 8 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (71%) | n/a | 13d ago | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 140 | [ ] | Carnal Instinct (STEAM) | 14 | 20 | 70% (last 20) | Does not open (40%) | n/a | 30d ago | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 141 | [ ] | Mortal Shell (EPIC) | 13 | 20 | 65% (last 20) | Does not open (54%) | 49% | 1d ago | 21% (drop) |  |
| 142 | [ ] | Sacred Gold (STEAM) | 13 | 20 | 65% (last 20) | Does not open (91%) | n/a | 4d ago | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 143 | [ ] | Binary Domain (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 46% | 18d ago | 23% (drop) |  |
| 144 | [ ] | Make Way (EPIC) | 14 | 20 | 70% (last 20) | Does not open (77%) | n/a | 8d ago | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 145 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 13 | 20 | 65% (last 20) | Does not open (84%) | 23% | 16d ago | 27% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 146 | [ ] | Arcade Paradise (EPIC) | 13 | 20 | 65% (last 20) | Does not open (45%) | 59% | 4d ago | 40% |  |
| 147 | [ ] | Sapphire Safari (GOG) | 13 | 20 | 65% (last 20) | Does not open (89%) | n/a | 10d ago | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 148 | [ ] | Prince of Persia: The Forgotten Sands (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 36% | 7d ago | n/a |  |
| 149 | [ ] | Allumeria (STEAM) | 13 | 20 | 65% (last 20) | Does not open (64%) | n/a | 8d ago | n/a | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 150 | [ ] | Crying Suns (EPIC) | 12 | 20 | 60% (last 20) | No graphics (67%) | n/a | today | n/a |  |
| 151 | [ ] | Chasm (GOG) | 12 | 20 | 60% (last 20) | No graphics (50%) | n/a | 3d ago | n/a |  |
| 152 | [ ] | Akane (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (50%) | n/a | 9d ago | n/a |  |
| 153 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 10 | 20 | 50% (last 20) | No graphics (57%) | 42% | 2d ago | 58% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 154 | [ ] | Chef Knight (STEAM) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 22d ago | n/a |  |
| 155 | [ ] | Dungeon Keeper™ 2 (GOG) | 14 | 20 | 70% (last 20) | Does not open (100%) | n/a | 24d ago | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 156 | [ ] | Songs of Conquest (EPIC) | 13 | 20 | 65% (last 20) | Does not open (75%) | n/a | 2d ago | n/a |  |
| 157 | [ ] | FINAL FANTASY VII REMAKE INTERGRADE (EPIC) | 13 | 20 | 65% (last 20) | Does not open (100%) | 43% | 3d ago | 43% |  |
| 158 | [ ] | Sandustry (STEAM) | 12 | 20 | 60% (last 20) | Does not open (72%) | n/a | 3d ago | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 159 | [ ] | Sonic Superstars (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 59% | 9d ago | 58% |  |
| 160 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 12 | 20 | 60% (last 20) | Does not open (90%) | 58% | 9d ago | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 161 | [ ] | Styx: Master of Shadows (EPIC) | 11 | 20 | 55% (last 20) | Does not open (75%) | 42% | today | 44% |  |
| 162 | [ ] | Assassin's Creed Odyssey (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 55% | 1d ago | 50% | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 163 | [ ] | Beat Cop (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | n/a | 5d ago | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 164 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 13 | 20 | 65% (last 20) | No graphics (56%) | n/a | 36d ago | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 165 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | n/a | 40d ago | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 166 | [ ] | SOMA (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | n/a | 8d ago | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 167 | [ ] | Shank 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 12d ago | n/a |  |
| 168 | [ ] | Wildermyth (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 57% | today | n/a |  |
| 169 | [ ] | Minit (EPIC) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 10d ago | n/a |  |
| 170 | [ ] | War of Dots (STEAM) | 12 | 20 | 60% (last 20) | Does not open (64%) | 55% | 2d ago | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 171 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | n/a | 13d ago | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 172 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (last 20) | Does not open (82%) | n/a | 19d ago | n/a |  |
| 173 | [ ] | Mafia: Definitive Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 41% | 4d ago | 40% |  |
| 174 | [ ] | Another World: 20th Anniversary Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (70%) | 58% | 6d ago | n/a |  |
| 175 | [ ] | Cities: Skylines (STEAM) | 11 | 20 | 55% (last 20) | Does not open (56%) | n/a | 6d ago | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 176 | [ ] | Strider (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 50% | 6d ago | 60% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 177 | [ ] | HOT WHEELS UNLEASHED™ (EPIC) | 10 | 20 | 50% (last 20) | No graphics (63%) | 57% | 1d ago | 41% |  |
| 178 | [ ] | Knights of Pen and Paper 2 (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (46%) | n/a | 9d ago | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 179 | [ ] | Wizardry: Proving Grounds of the Mad Overlord (STEAM) | 12 | 20 | 60% (last 20) | Graphics glitches (64%) | n/a | 4d ago | n/a |  |
| 180 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (last 20) | No graphics (78%) | n/a | 12d ago | n/a |  |
| 181 | [ ] | LET IT DIE (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 50% | today | n/a |  |
| 182 | [ ] | No More Heroes (STEAM) | 10 | 20 | 50% (last 20) | No graphics (67%) | 39% | 4d ago | 29% |  |
| 183 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 10 | 20 | 50% (last 20) | Does not open (100%) | 36% | 13d ago | n/a |  |
| 184 | [ ] | Railway Chai Wala (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | n/a | 3d ago | n/a |  |
| 185 | [ ] | Turnip Boy Robs a Bank (EPIC) | 11 | 20 | 55% (last 20) | Does not open (67%) | 29% | 4d ago | n/a | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 186 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (last 20) | No graphics (57%) | 57% | 5d ago | n/a |  |
| 187 | [ ] | Trials Survivors (STEAM) | 10 | 20 | 50% (last 20) | Does not open (75%) | n/a | 12d ago | n/a |  |
| 188 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 10 | 20 | 50% (last 20) | Does not open (86%) | n/a | 83d ago | n/a |  |
| 189 | [ ] | Delver (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 35% | 2d ago | 0% (drop) |  |

## Fix shipped, waiting for ratings (16)

A fix reached these games. They stay off the broken lists while ratings from players who have the fix come in, then the data decides again.

| # | Game | Fix shipped | Ratings since the fix | One-star since the fix | Newest rating | Issue |
|---:|---|---|---:|---:|---|---|
| 1 | L.A. Noire (STEAM) | 2026-11-04 | 4 | 4 | 3d ago | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 2 | Transistor (STEAM) | 2026-11-10 | 2 | 2 | 1d ago | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 3 | Max Payne 3 (STEAM) | 2026-11-04 | 3 | 3 | 1d ago | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 4 | Red Dead Redemption (STEAM) | 2026-11-04 | 2 | 2 | 1d ago | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 5 | Prince of Persia The Lost Crown (STEAM) | 2026-11-04 | 7 | 7 | 1d ago | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 6 | Burnout™ Paradise Remastered (STEAM) | 2026-11-04 | 3 | 3 | 7d ago | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 7 | Peggle Deluxe (STEAM) | 2026-10-29 | 1 | 1 | 5d ago | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 8 | Necesse (STEAM) | 2026-10-29 | 6 | 0 | 2d ago | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 9 | Grand Theft Auto III - The Definitive Edition (STEAM) | 2026-11-04 | 1 | 1 | 7d ago | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 10 | Mirror's Edge™ Catalyst (STEAM) | 2026-11-04 | 1 | 1 | 14d ago | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 11 | Need for Speed™ (STEAM) | 2026-11-04 | 0 | 0 | 27d ago | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 12 | Dragon Age™ Inquisition (STEAM) | 2026-11-04 | 0 | 0 | 15d ago | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 13 | PAYDAY 2 (STEAM) | 2026-11-04 | 1 | 1 | 13d ago | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 14 | EA SPORTS FC™ 26 (STEAM) | 2026-11-04 | 0 | 0 | 20d ago | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 15 | Need for Speed™ Heat  (STEAM) | 2026-11-04 | 0 | 0 | 14d ago | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 16 | Need for Speed™ Unbound (STEAM) | 2026-11-04 | 0 | 0 | 21d ago | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |

## Works, but the first launch usually fails (301)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Newest rating | Newest release rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|---:|---|
| 1 | [ ] | Half-Life (STEAM) | 85 | 120 | 71% (14d) | Does not open (61%) | 71% | today | 66% |  |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 70 | 92 | 76% (14d) | Does not open (63%) | 92% | today | 95% |  |
| 3 | [ ] | Grand Theft Auto V Legacy (STEAM) | 55 | 65 | 85% (since fix) | Does not open (87%) | 75% | today | 69% |  |
| 4 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 54 | 73 | 74% (14d) | Does not open (54%) | 81% | today | 82% |  |
| 5 | [ ] | Cyberpunk 2077 (STEAM) | 48 | 78 | 62% (14d) | Does not open (71%) | 71% | today | 66% |  |
| 6 | [ ] | Buckshot Roulette (STEAM) | 45 | 63 | 71% (14d) | Does not open (63%) | 70% | today | 47% (drop) |  |
| 7 | [ ] | Road Rash™: 30th Anniversary Edition (STEAM) | 45 | 69 | 65% (14d) | Does not open (74%) | 62% | today | 67% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 8 | [ ] | DREDGE (EPIC) | 38 | 42 | 90% (14d) | Does not open (76%) | 60% | today | 47% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 9 | [ ] | Probably Stolen (STEAM) | 38 | 75 | 51% (14d) | Does not open (64%) | 86% | 1d ago | 81% |  |
| 10 | [ ] | Valheim (STEAM) | 37 | 59 | 63% (since fix) | No graphics (54%) | 84% | today | 81% |  |
| 11 | [ ] | MONSTER HUNTER RISE (STEAM) | 36 | 58 | 62% (14d) | Does not open (83%) | 60% | today | 62% |  |
| 12 | [ ] | No Man's Sky (STEAM) | 33 | 60 | 55% (since fix) | Controller issues (61%) | 79% | today | 76% |  |
| 13 | [ ] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 32 | 58 | 55% (14d) | Does not open (65%) | 64% | today | 67% |  |
| 14 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 31 | 42 | 74% (14d) | Does not open (58%) | 70% | today | 60% |  |
| 15 | [ ] | Super Meat Boy (STEAM) | 30 | 57 | 53% (14d) | Does not open (60%) | 67% | today | 58% |  |
| 16 | [ ] | ROB RUN (STEAM) | 30 | 38 | 79% (14d) | Does not open (88%) | 63% | today | 66% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 17 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 28 | 39 | 72% (14d) | Does not open (77%) | 76% | today | 72% |  |
| 18 | [ ] | Selaco (STEAM) | 27 | 42 | 64% (14d) | Does not open (86%) | 68% | today | 61% |  |
| 19 | [ ] | Horizon Chase Turbo (EPIC) | 26 | 38 | 68% (14d) | Does not open (85%) | 63% | today | 46% |  |
| 20 | [ ] | Quake (STEAM) | 20 | 33 | 61% (14d) | Does not open (65%) | 74% | today | 59% |  |
| 21 | [ ] | ELDEN RING (STEAM) | 19 | 34 | 56% (14d) | Does not open (85%) | 69% | today | 65% |  |
| 22 | [ ] | Red Dead Redemption 2 (STEAM) | 19 | 20 | 95% (since fix) | Does not open (98%) | 83% | 1d ago | 85% |  |
| 23 | [ ] | BeamNG.drive (STEAM) | 18 | 20 | 90% (last 20) | Does not open (79%) | 73% | today | 56% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 24 | [ ] | Resident Evil 4 (2005) (STEAM) | 17 | 25 | 68% (14d) | Does not open (79%) | 71% | today | 71% |  |
| 25 | [ ] | Loftia (STEAM) | 17 | 20 | 85% (14d) | Does not open (94%) | 74% | today | 68% |  |
| 26 | [ ] | Look Outside (STEAM) | 16 | 31 | 52% (14d) | Controller issues (61%) | 90% | 1d ago | 90% |  |
| 27 | [ ] | BioShock Remastered (EPIC) | 16 | 22 | 73% (14d) | Does not open (67%) | 61% | today | 54% |  |
| 28 | [ ] | Deadlock (STEAM) | 16 | 21 | 76% (14d) | Does not open (54%) | 88% | 3d ago | 87% |  |
| 29 | [ ] | Mortal Kombat X (STEAM) | 16 | 23 | 70% (14d) | Does not open (72%) | 91% | today | 90% |  |
| 30 | [ ] | Clair Obscur: Expedition 33 (STEAM) | 15 | 27 | 56% (14d) | Graphics glitches (41%) | 81% | today | 72% |  |
| 31 | [ ] | Library Of Ruina (STEAM) | 15 | 23 | 65% (14d) | Does not open (69%) | 86% | today | 79% |  |
| 32 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (59%) | 75% | 2d ago | 61% |  |
| 33 | [ ] | DRAGON BALL FighterZ (STEAM) | 27 | 50 | 54% (since fix) | Does not open (89%) | 83% | 1d ago | 89% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 34 | [ ] | Noita (STEAM) | 14 | 26 | 54% (14d) | Does not open (56%) | 78% | today | 79% |  |
| 35 | [ ] | Shakedown: Hawaii (STEAM) | 14 | 27 | 52% (14d) | Does not open (77%) | 93% | 1d ago | 85% |  |
| 36 | [ ] | STAR WARS™ Knights of the Old Republic™ (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (44%) | 91% | today | 90% |  |
| 37 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 25 | 45 | 56% (since fix) | Does not open (74%) | 60% | today | 54% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 38 | [ ] | DOOM 3: BFG Edition (STEAM) | 15 | 20 | 75% (last 20) | Does not open (72%) | 71% | today | 66% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 39 | [ ] | Grand Theft Auto V (EPIC) | 18 | 20 | 90% (last 20) | Does not open (89%) | 77% | today | 74% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 40 | [ ] | Batman™: Arkham Origins (STEAM) | 15 | 20 | 75% (last 20) | Does not open (84%) | 73% | today | 62% |  |
| 41 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 12 | 20 | 60% (last 20) | Does not open (70%) | 64% | 2d ago | 92% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 42 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 20 | 20 | 100% (last 20) | Does not open (89%) | 95% | today | 95% |  |
| 43 | [ ] | Absolute Drift (EPIC) | 12 | 20 | 60% (last 20) | No graphics (51%) | 68% | today | 35% (drop) |  |
| 44 | [ ] | Order of the Sinking Star (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 68% | today | 77% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 45 | [ ] | Moonlighter (EPIC) | 20 | 20 | 100% (last 20) | No graphics (71%) | 100% | 3d ago | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 46 | [ ] | Resident Evil 7 Biohazard (STEAM) | 11 | 20 | 55% (last 20) | Does not open (69%) | 75% | today | 70% |  |
| 47 | [ ] | Mini Motorways (STEAM) | 15 | 20 | 75% (last 20) | Does not open (71%) | 71% | today | 68% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 48 | [ ] | Alabaster Dawn (STEAM) | 12 | 20 | 60% (last 20) | Controller issues (48%) | 88% | 1d ago | 89% |  |
| 49 | [ ] | MapleStory (STEAM) | 19 | 20 | 95% (last 20) | Does not open (76%) | 68% | 9d ago | 63% |  |
| 50 | [ ] | Cry of Fear (STEAM) | 13 | 20 | 65% (last 20) | Does not open (48%) | 73% | today | 75% |  |
| 51 | [ ] | Dead Island Definitive Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (66%) | 86% | today | 85% |  |
| 52 | [ ] | Palworld (STEAM) | 10 | 20 | 50% (14d) | Does not open (76%) | 87% | 1d ago | 86% |  |
| 53 | [ ] | Dead Island 2 (EPIC) | 17 | 20 | 85% (last 20) | Does not open (84%) | 65% | 3d ago | 50% |  |
| 54 | [ ] | Castlevania Dominus Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (92%) | 98% | 2d ago | 96% |  |
| 55 | [ ] | Don't Starve Together (STEAM) | 11 | 20 | 55% (last 20) | Does not open (58%) | 73% | today | 64% |  |
| 56 | [ ] | Dead Space (STEAM) | 17 | 20 | 85% (last 20) | Does not open (57%) | 84% | today | 81% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 57 | [ ] | Divinity: Original Sin 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (74%) | 84% | 2d ago | 76% |  |
| 58 | [ ] | METAL GEAR SOLID 4: Guns of the Patriots - Master Collection Version (STEAM) | 11 | 20 | 55% (last 20) | Does not open (80%) | 89% | 6d ago | 91% |  |
| 59 | [ ] | LEGO® MARVEL Super Heroes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (66%) | 81% | today | 86% |  |
| 60 | [ ] | Disgaea 5 Complete (STEAM) | 18 | 20 | 90% (last 20) | Does not open (73%) | 90% | 1d ago | 94% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 61 | [ ] | Cyberpunk 2077 (GOG) | 12 | 20 | 60% (last 20) | Does not open (72%) | 70% | today | 58% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 62 | [ ] | Fallout: New Vegas (EPIC) | 15 | 20 | 75% (last 20) | Does not open (59%) | 82% | today | 74% |  |
| 63 | [ ] | Geometry Wars: Retro Evolved (STEAM) | 11 | 20 | 55% (last 20) | Does not open (94%) | 65% | 1d ago | 52% |  |
| 64 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (76%) | 62% | 2d ago | 52% |  |
| 65 | [ ] | Aniimo (STEAM) | 17 | 20 | 85% (last 20) | Does not open (74%) | 85% | today | 77% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 66 | [ ] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 74% | 1d ago | 83% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 67 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (79%) | 97% | 5d ago | 95% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 68 | [ ] | Prey (STEAM) | 10 | 20 | 50% (last 20) | Does not open (58%) | 79% | today | 82% |  |
| 69 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 18 | 20 | 90% (last 20) | Does not open (84%) | 69% | 1d ago | 71% |  |
| 70 | [ ] | OMORI (STEAM) | 14 | 20 | 70% (last 20) | Does not open (62%) | 69% | 1d ago | 52% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 71 | [ ] | eFootball™ (STEAM) | 14 | 20 | 70% (last 20) | Does not open (65%) | 66% | today | 56% |  |
| 72 | [ ] | Welcome to Elderfield (STEAM) | 12 | 20 | 60% (last 20) | Does not open (71%) | 70% | today | 71% |  |
| 73 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 16 | 20 | 80% (last 20) | Graphics glitches (48%) | 84% | today | 82% |  |
| 74 | [ ] | Poppy Playtime (STEAM) | 13 | 20 | 65% (last 20) | Does not open (59%) | 68% | 3d ago | 60% |  |
| 75 | [ ] | Deskrawl: Idle ARPG (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 82% | 7d ago | n/a | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 76 | [ ] | Digimon Story Cyber Sleuth: Complete Edition (STEAM) | 10 | 20 | 50% (last 20) | No graphics (49%) | 84% | 1d ago | 90% |  |
| 77 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Does not open (61%) | 90% | today | 83% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 78 | [ ] | Dota 2 (STEAM) | 14 | 20 | 70% (last 20) | Does not open (76%) | 74% | 1d ago | 86% |  |
| 79 | [ ] | River City Girls (EPIC) | 14 | 20 | 70% (last 20) | No graphics (48%) | 67% | 2d ago | 43% (drop) |  |
| 80 | [ ] | Darksiders Warmastered Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (90%) | 68% | 1d ago | 52% |  |
| 81 | [ ] | The Sims™ 4 (STEAM) | 6 | 12 | 50% (since fix) | Does not open (85%) | 72% | today | 74% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 82 | [ ] | Castlevania Anniversary Collection (EPIC) | 12 | 20 | 60% (last 20) | Does not open (70%) | 65% | 3d ago | 33% (drop) |  |
| 83 | [ ] | Call of Duty 4: Modern Warfare (2007) (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (52%) | 76% | 1d ago | 62% |  |
| 84 | [ ] | Fate/stay night REMASTERED (STEAM) | 12 | 20 | 60% (last 20) | No graphics (48%) | 89% | 3d ago | 81% |  |
| 85 | [ ] | Disco Elysium - The Final Cut (EPIC) | 11 | 20 | 55% (last 20) | Does not open (74%) | 97% | 1d ago | 98% |  |
| 86 | [ ] | Sorry We're Closed (EPIC) | 10 | 20 | 50% (last 20) | Does not open (84%) | 71% | today | 44% (drop) |  |
| 87 | [ ] | Ratatan (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 90% | 5d ago | 85% |  |
| 88 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 15 | 20 | 75% (last 20) | Does not open (42%) | 73% | 1d ago | 65% |  |
| 89 | [ ] | Need for Speed™ Rivals (STEAM) | 12 | 20 | 60% (last 20) | Does not open (62%) | 81% | 1d ago | 92% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 90 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (62%) | 95% | today | 97% |  |
| 91 | [ ] | STAR WARS™ Knights of the Old Republic™ II: The Sith Lords™ (STEAM) | 11 | 20 | 55% (last 20) | No graphics (65%) | 66% | today | 37% (drop) |  |
| 92 | [ ] | Assassin's Creed II (STEAM) | 20 | 20 | 100% (last 20) | Does not open (80%) | 65% | 1d ago | 69% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 93 | [ ] | Happy Wheels (STEAM) | 19 | 20 | 95% (last 20) | No graphics (52%) | 69% | 11d ago | 50% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 94 | [ ] | MIO: Memories in Orbit (STEAM) | 11 | 20 | 55% (last 20) | Graphics glitches (50%) | 95% | 2d ago | 97% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 95 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 11 | 20 | 55% (last 20) | Does not open (51%) | 66% | 4d ago | 35% (drop) | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 96 | [ ] | Cave Story+ (STEAM) | 18 | 20 | 90% (last 20) | Does not open (62%) | 82% | today | 74% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 97 | [ ] | Fable - The Lost Chapters (STEAM) | 13 | 20 | 65% (last 20) | Graphics glitches (48%) | 82% | 2d ago | 83% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 98 | [ ] | Rune Factory 3 Special (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 92% | 2d ago | n/a |  |
| 99 | [ ] | Sol Cesto (EPIC) | 20 | 20 | 100% (last 20) | Does not open (81%) | 80% | today | 70% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 100 | [ ] | Age of Empires II (2013) (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 73% | today | 77% |  |
| 101 | [ ] | American Truck Simulator (STEAM) | 11 | 20 | 55% (last 20) | Does not open (70%) | 76% | 4d ago | 70% |  |
| 102 | [ ] | Sid Meier's Civilization VI (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 82% | today | 72% |  |
| 103 | [ ] | ZERO Sievert (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 88% | today | 77% |  |
| 104 | [ ] | The Binding of Isaac (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (93%) | 94% | today | 95% |  |
| 105 | [ ] | Resident Evil Village (STEAM) | 13 | 20 | 65% (last 20) | Does not open (73%) | 88% | 6d ago | 82% |  |
| 106 | [ ] | Minecraft Dungeons (STEAM) | 11 | 20 | 55% (last 20) | Does not open (77%) | 81% | today | 80% |  |
| 107 | [ ] | Abiotic Factor (STEAM) | 10 | 20 | 50% (last 20) | Does not open (74%) | 73% | 1d ago | 81% |  |
| 108 | [ ] | Palia (STEAM) | 15 | 20 | 75% (last 20) | Does not open (59%) | 76% | 1d ago | 69% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 109 | [ ] | Minecraft Dungeons II (STEAM) | 14 | 20 | 70% (last 20) | Does not open (82%) | 69% | today | 74% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 110 | [ ] | Until Then (STEAM) | 14 | 20 | 70% (last 20) | Does not open (84%) | 78% | 4d ago | 59% |  |
| 111 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 96% | 1d ago | 89% |  |
| 112 | [ ] | ENDER LILIES: Quietus of the Knights (EPIC) | 10 | 20 | 50% (last 20) | Does not open (67%) | 60% | 2d ago | 44% |  |
| 113 | [ ] | Grand Theft Auto: Vice City (STEAM) | 11 | 20 | 55% (last 20) | Does not open (50%) | 85% | today | 81% |  |
| 114 | [ ] | Sid Meier's Civilization V (STEAM) | 15 | 20 | 75% (last 20) | Does not open (75%) | 63% | 2d ago | 59% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 115 | [ ] | Dead Rising 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (88%) | 80% | 11d ago | 80% |  |
| 116 | [ ] | PlateUp! (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 80% | 1d ago | 68% |  |
| 117 | [ ] | A Plague Tale: Innocence (STEAM) | 19 | 20 | 95% (last 20) | Does not open (88%) | 71% | 2d ago | 73% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 118 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (83%) | 77% | 3d ago | 67% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 119 | [ ] | Moonstone Island (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (63%) | 74% | 2d ago | 71% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 120 | [ ] | No, I'm not a Human (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 94% | today | 86% |  |
| 121 | [ ] | TBH: Task Bar Hero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 85% | 6d ago | 82% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 122 | [ ] | Overwatch® (STEAM) | 18 | 20 | 90% (last 20) | Does not open (58%) | 69% | 1d ago | 80% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 123 | [ ] | Yakuza: Like a Dragon (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 64% | 10d ago | 77% |  |
| 124 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 78% | today | 79% |  |
| 125 | [x] 2026-10-18 | Diablo® IV (STEAM) | 19 | 20 | 95% (last 20) | Does not open (59%) | 69% | 9d ago | 80% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 126 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 16 | 20 | 80% (last 20) | Does not open (76%) | 90% | 3d ago | n/a | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 127 | [ ] | Tails of Iron (STEAM) | 11 | 20 | 55% (last 20) | Does not open (73%) | 87% | 3d ago | 82% |  |
| 128 | [ ] | Elite Dangerous (STEAM) | 20 | 20 | 100% (last 20) | Does not open (79%) | 60% | 16d ago | n/a | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 129 | [ ] | Roguecraft DX (STEAM) | 13 | 20 | 65% (last 20) | Does not open (79%) | 95% | 19d ago | 92% |  |
| 130 | [ ] | Astral Party  (STEAM) | 13 | 20 | 65% (last 20) | Does not open (93%) | 81% | 3d ago | 70% |  |
| 131 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 11 | 20 | 55% (last 20) | Does not open (43%) | 70% | today | 71% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 132 | [ ] | Pinball FX (STEAM) | 11 | 20 | 55% (last 20) | Does not open (60%) | 71% | 1d ago | 69% |  |
| 133 | [ ] | Call of Juarez Gunslinger (STEAM) | 14 | 20 | 70% (last 20) | Does not open (89%) | 77% | 7d ago | 79% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 134 | [ ] | Max Payne (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (45%) | 85% | today | 77% |  |
| 135 | [ ] | Fallout (STEAM) | 11 | 20 | 55% (last 20) | Does not open (71%) | 71% | 7d ago | 65% |  |
| 136 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (50%) | 77% | 3d ago | 72% |  |
| 137 | [ ] | Heavy Rain (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 94% | 3d ago | 94% |  |
| 138 | [ ] | Driving Rogue (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 91% | 11d ago | 88% |  |
| 139 | [ ] | Gunfire Reborn (STEAM) | 18 | 20 | 90% (last 20) | Does not open (81%) | 88% | today | n/a | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 140 | [ ] | Aggelos (STEAM) | 17 | 20 | 85% (last 20) | No graphics (83%) | 88% | today | n/a | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 141 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (87%) | 93% | 1d ago | 95% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 142 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 15 | 20 | 75% (last 20) | Controller issues (46%) | 91% | 8d ago | 87% |  |
| 143 | [ ] | Sonic Generations (STEAM) | 14 | 20 | 70% (last 20) | Does not open (70%) | 70% | today | 71% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 144 | [ ] | Call of Duty: World at War (STEAM) | 13 | 20 | 65% (last 20) | Does not open (44%) | 84% | today | 66% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 145 | [ ] | Street Fighter™ 6 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (81%) | 83% | today | 83% |  |
| 146 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 91% | 5d ago | 89% |  |
| 147 | [ ] | CrossCode (GOG) | 19 | 20 | 95% (last 20) | Does not open (80%) | 78% | 16d ago | n/a | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 148 | [ ] | Plague Inc: Evolved (STEAM) | 13 | 20 | 65% (last 20) | Does not open (68%) | 63% | today | 62% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 149 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 13 | 20 | 65% (last 20) | Does not open (92%) | 62% | 2d ago | 53% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 150 | [ ] | Oxygen Not Included (STEAM) | 12 | 20 | 60% (last 20) | Does not open (76%) | 61% | 3d ago | 75% |  |
| 151 | [ ] | Sonic Origins (STEAM) | 12 | 20 | 60% (last 20) | Does not open (68%) | 83% | 6d ago | 79% |  |
| 152 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 19 | 20 | 95% (last 20) | Controller issues (62%) | 92% | 13d ago | n/a | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 153 | [ ] | Monster Hunter Wilds (STEAM) | 19 | 20 | 95% (last 20) | Does not open (63%) | 79% | 5d ago | n/a | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 154 | [ ] | Dead by Daylight (STEAM) | 17 | 20 | 85% (last 20) | Does not open (79%) | 83% | 1d ago | 82% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 155 | [ ] | Stick It to the Stickman (STEAM) | 16 | 20 | 80% (last 20) | Does not open (86%) | 78% | 11d ago | 81% |  |
| 156 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 13 | 20 | 65% (last 20) | Does not open (71%) | 82% | 5d ago | 77% |  |
| 157 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 11 | 20 | 55% (last 20) | Does not open (62%) | 72% | today | 72% |  |
| 158 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 73% | 4d ago | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 159 | [ ] | Tabletop Simulator (STEAM) | 15 | 20 | 75% (last 20) | Does not open (53%) | 79% | today | 84% |  |
| 160 | [ ] | Gambonanza (STEAM) | 13 | 20 | 65% (last 20) | Does not open (60%) | 92% | 1d ago | 89% |  |
| 161 | [ ] | Dishonored 2 (STEAM) | 13 | 20 | 65% (last 20) | Does not open (90%) | 75% | 1d ago | 62% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 162 | [ ] | Gothic 1 Classic (STEAM) | 12 | 20 | 60% (last 20) | Does not open (65%) | 76% | 9d ago | 61% |  |
| 163 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (90%) | 67% | 9d ago | n/a | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 164 | [ ] | Metro: Last Light Complete Edition (STEAM) | 17 | 20 | 85% (last 20) | Does not open (54%) | 72% | 2d ago | 80% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 165 | [ ] | Romestead (STEAM) | 16 | 20 | 80% (last 20) | Does not open (64%) | 61% | 7d ago | n/a | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 166 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 14 | 20 | 70% (last 20) | Does not open (46%) | 61% | 3d ago | 65% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 167 | [ ] | CLANNAD (STEAM) | 14 | 20 | 70% (last 20) | Does not open (50%) | 82% | 9d ago | 91% |  |
| 168 | [ ] | Limbus Company (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 83% | 2d ago | 91% |  |
| 169 | [ ] | Stellar Blade™ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (43%) | 78% | 1d ago | 79% |  |
| 170 | [ ] | Control Ultimate Edition (GOG) | 13 | 20 | 65% (last 20) | Does not open (76%) | 79% | 7d ago | 71% |  |
| 171 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 12 | 20 | 60% (last 20) | No graphics (85%) | 89% | today | 85% |  |
| 172 | [ ] | BioShock 2 Remastered (STEAM) | 11 | 20 | 55% (last 20) | Does not open (79%) | 85% | 2d ago | 84% |  |
| 173 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 11 | 20 | 55% (last 20) | Does not open (70%) | 67% | 10d ago | 73% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 174 | [ ] | Trailmakers (STEAM) | 11 | 20 | 55% (last 20) | Does not open (44%) | 93% | 2d ago | 94% |  |
| 175 | [ ] | Sonic Lost World (STEAM) | 10 | 20 | 50% (last 20) | No graphics (69%) | 79% | 1d ago | 81% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 176 | [ ] | Stumble Guys (STEAM) | 10 | 20 | 50% (last 20) | Does not open (72%) | 71% | 3d ago | 63% |  |
| 177 | [ ] | Counter-Strike:Global Offensive (STEAM) | 10 | 20 | 50% (last 20) | Does not open (76%) | 72% | 2d ago | 71% |  |
| 178 | [ ] | Raft (STEAM) | 10 | 20 | 50% (last 20) | Does not open (82%) | 90% | 2d ago | 84% |  |
| 179 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 16 | 20 | 80% (last 20) | Does not open (59%) | 91% | 13d ago | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 180 | [ ] | Supermarket Together (STEAM) | 15 | 20 | 75% (last 20) | Does not open (65%) | 62% | today | 75% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 181 | [ ] | Changed (STEAM) | 15 | 20 | 75% (last 20) | Does not open (69%) | 61% | 5d ago | 47% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 182 | [ ] | Metro Exodus (STEAM) | 15 | 20 | 75% (last 20) | Does not open (85%) | 88% | 6d ago | 88% |  |
| 183 | [ ] | One-armed robber (STEAM) | 14 | 20 | 70% (last 20) | Controller issues (65%) | 70% | 10d ago | 57% |  |
| 184 | [ ] | Tyr (STEAM) | 13 | 20 | 65% (last 20) | Does not open (33%) | 73% | 10d ago | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 185 | [ ] | Mortal Kombat 11 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (69%) | 75% | 4d ago | 81% |  |
| 186 | [ ] | Subnautica 2 (STEAM) | 17 | 20 | 85% (last 20) | Does not open (52%) | 79% | today | n/a | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 187 | [ ] | Crab Game (STEAM) | 17 | 20 | 85% (last 20) | Does not open (50%) | 84% | 7d ago | n/a | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 188 | [ ] | Capcom Arcade Stadium (STEAM) | 15 | 20 | 75% (last 20) | Does not open (82%) | 72% | 5d ago | 82% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 189 | [ ] | Opus Magnum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (78%) | 92% | 8d ago | n/a |  |
| 190 | [ ] | Gothic II: Gold Classic (STEAM) | 17 | 20 | 85% (last 20) | Does not open (56%) | 65% | 12d ago | 71% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 191 | [ ] | Dead Island (STEAM) | 17 | 20 | 85% (last 20) | Does not open (71%) | 90% | today | n/a | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 192 | [ ] | Russian Fishing 4 (STEAM) | 16 | 20 | 80% (last 20) | Does not open (75%) | 80% | 1d ago | 67% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 193 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (61%) | 68% | 8d ago | 60% |  |
| 194 | [ ] | Digimon Survive (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (77%) | 83% | 6d ago | 77% |  |
| 195 | [ ] | Unturned (STEAM) | 11 | 20 | 55% (last 20) | Does not open (44%) | 71% | today | 75% |  |
| 196 | [ ] | The Witcher: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 63% | 11d ago | 79% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 197 | [ ] | Escape from Duckov (STEAM) | 10 | 20 | 50% (last 20) | Controller issues (71%) | 95% | 5d ago | 97% |  |
| 198 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 95% | 7d ago | 93% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 199 | [ ] | CarX Street (STEAM) | 17 | 20 | 85% (last 20) | Does not open (77%) | 82% | 12d ago | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 200 | [ ] | Tearscape (STEAM) | 16 | 20 | 80% (last 20) | Controller issues (65%) | 100% | 13d ago | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 201 | [ ] | Sheepy: A Short Adventure (STEAM) | 15 | 20 | 75% (last 20) | Does not open (51%) | 67% | 21d ago | n/a | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 202 | [ ] | Party Animals (STEAM) | 14 | 20 | 70% (last 20) | Does not open (67%) | 67% | 7d ago | 79% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 203 | [ ] | Lucid Blocks (STEAM) | 12 | 20 | 60% (last 20) | Does not open (80%) | 66% | today | 59% |  |
| 204 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 96% | 3d ago | 100% |  |
| 205 | [ ] | TurretGirls (STEAM) | 11 | 20 | 55% (last 20) | No graphics (75%) | 88% | 3d ago | 88% |  |
| 206 | [ ] | Hotline Miami (GOG) | 14 | 20 | 70% (last 20) | Does not open (90%) | 67% | today | 75% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 207 | [ ] | Darksiders (STEAM) | 12 | 20 | 60% (last 20) | Does not open (70%) | 86% | 2d ago | 83% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 208 | [ ] | Warframe (STEAM) | 11 | 20 | 55% (last 20) | Does not open (83%) | 84% | 1d ago | 78% |  |
| 209 | [ ] | Moonring (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 87% | 5d ago | 81% |  |
| 210 | [ ] | Goat Simulator (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 69% | 2d ago | 67% |  |
| 211 | [ ] | MX Bikes (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 92% | today | 94% |  |
| 212 | [ ] | Jade Empire: Special Edition (STEAM) | 18 | 20 | 90% (last 20) | Does not open (95%) | 75% | 2d ago | n/a | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 213 | [ ] | Undisputed (STEAM) | 18 | 20 | 90% (last 20) | Does not open (67%) | 67% | 10d ago | n/a | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 214 | [ ] | Bodycam (STEAM) | 16 | 20 | 80% (last 20) | Does not open (62%) | 64% | 6d ago | 50% |  |
| 215 | [ ] | Crusader Kings III (STEAM) | 16 | 20 | 80% (last 20) | No graphics (64%) | 70% | 15d ago | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 216 | [ ] | Tower and Sword of Succubus (STEAM) | 15 | 20 | 75% (last 20) | No graphics (91%) | 82% | 31d ago | 70% |  |
| 217 | [ ] | Invisible, Inc. (STEAM) | 15 | 20 | 75% (last 20) | Does not open (63%) | 77% | 19d ago | n/a |  |
| 218 | [ ] | Divinum (STEAM) | 14 | 20 | 70% (last 20) | Does not open (61%) | 73% | 21d ago | 67% |  |
| 219 | [ ] | Return to Monkey Island (STEAM) | 14 | 20 | 70% (last 20) | No graphics (72%) | 70% | 11d ago | 64% |  |
| 220 | [ ] | GOD EATER RESURRECTION (STEAM) | 14 | 20 | 70% (last 20) | Does not open (59%) | 78% | 4d ago | n/a |  |
| 221 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 14 | 20 | 70% (last 20) | Does not open (64%) | 73% | 6d ago | n/a | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 222 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (47%) | 83% | 2d ago | n/a |  |
| 223 | [ ] | My Summer Car (STEAM) | 11 | 20 | 55% (last 20) | Does not open (63%) | 82% | today | 86% |  |
| 224 | [ ] | Resident Evil Revelations 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (45%) | 82% | today | 80% |  |
| 225 | [ ] | GUILTY GEAR Xrd REV 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (86%) | 81% | 3d ago | 58% (drop) |  |
| 226 | [ ] | Lost and Found Co. (STEAM) | 10 | 20 | 50% (last 20) | Does not open (67%) | 78% | 6d ago | 75% |  |
| 227 | [ ] | Jade Empire: Special Edition (GOG) | 14 | 20 | 70% (last 20) | Does not open (42%) | 70% | 13d ago | n/a | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 228 | [ ] | DOOM 3: BFG Edition (GOG) | 14 | 20 | 70% (last 20) | No graphics (53%) | 93% | 8d ago | n/a | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 229 | [ ] | Zero Escape: The Nonary Games (STEAM) | 12 | 20 | 60% (last 20) | Does not open (91%) | 67% | 8d ago | 68% |  |
| 230 | [ ] | Dying Light (EPIC) | 10 | 20 | 50% (last 20) | Does not open (87%) | 65% | 2d ago | 50% |  |
| 231 | [ ] | STORY OF SEASONS: Friends of Mineral Town (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 90% | 2d ago | 100% |  |
| 232 | [ ] | Torchlight II (EPIC) | 13 | 20 | 65% (last 20) | Does not open (83%) | 73% | 1d ago | 71% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 233 | [ ] | SnowRunner (STEAM) | 12 | 20 | 60% (last 20) | Does not open (96%) | 81% | today | 69% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 234 | [ ] | Cat Mail Co. (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 83% | 4d ago | 83% |  |
| 235 | [ ] | BATTLETECH (STEAM) | 12 | 20 | 60% (last 20) | Does not open (50%) | 95% | 2d ago | 92% |  |
| 236 | [ ] | Deus Ex™ GOTY Edition (GOG) | 12 | 20 | 60% (last 20) | No graphics (44%) | 92% | 18d ago | n/a | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 237 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 12 | 20 | 60% (last 20) | Does not open (92%) | 67% | 9d ago | 64% |  |
| 238 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 11 | 20 | 55% (last 20) | Does not open (53%) | 65% | 1d ago | 73% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 239 | [ ] | Absolum Demo (STEAM) | 11 | 20 | 55% (last 20) | Does not open (90%) | 90% | 3d ago | 93% |  |
| 240 | [ ] | XCOM 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (58%) | 80% | today | 75% |  |
| 241 | [ ] | Secrets of Grindea (STEAM) | 10 | 20 | 50% (last 20) | Does not open (45%) | 75% | today | 79% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 242 | [ ] | Faster Than Light (EPIC) | 10 | 20 | 50% (last 20) | Controller issues (38%) | 92% | 1d ago | n/a |  |
| 243 | [ ] | Revolution Idle (STEAM) | 10 | 20 | 50% (last 20) | Does not open (43%) | 77% | 1d ago | n/a |  |
| 244 | [ ] | Goose Goose Duck (STEAM) | 13 | 20 | 65% (last 20) | Does not open (65%) | 64% | 3d ago | n/a | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 245 | [ ] | AER Memories of Old (EPIC) | 13 | 20 | 65% (last 20) | Does not open (86%) | 100% | 2d ago | n/a |  |
| 246 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 20 | 65% (last 20) | Controller issues (71%) | 76% | 3d ago | 70% |  |
| 247 | [ ] | PAYDAY: The Heist (STEAM) | 13 | 20 | 65% (last 20) | Does not open (75%) | 67% | 11d ago | n/a |  |
| 248 | [ ] | 12 is Better Than 6 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (40%) | 85% | 13d ago | n/a |  |
| 249 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 100% | 10d ago | n/a |  |
| 250 | [ ] | No Socks RPG (STEAM) | 11 | 20 | 55% (last 20) | Graphics glitches (91%) | 93% | 1d ago | 91% |  |
| 251 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (78%) | 95% | 1d ago | 95% |  |
| 252 | [ ] | Hero Siege (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (52%) | 82% | 2d ago | 86% |  |
| 253 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (62%) | 81% | 4d ago | 80% |  |
| 254 | [ ] | Capcom Fighting Collection (STEAM) | 14 | 20 | 70% (last 20) | Does not open (81%) | 87% | 9d ago | 80% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 255 | [ ] | Tales of Zestiria (STEAM) | 14 | 20 | 70% (last 20) | Does not open (73%) | 73% | 23d ago | n/a | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 256 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 14 | 20 | 70% (last 20) | Does not open (85%) | 82% | 10d ago | n/a | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 257 | [ ] | FINAL FANTASY XIV Online (STEAM) | 13 | 20 | 65% (last 20) | Does not open (95%) | 92% | 9d ago | 88% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 258 | [ ] | Disgaea 4 Complete+ (STEAM) | 13 | 20 | 65% (last 20) | No graphics (43%) | 92% | 3d ago | n/a | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 259 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 20 | 65% (last 20) | Does not open (80%) | 90% | 29d ago | 90% |  |
| 260 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 12 | 20 | 60% (last 20) | No graphics (39%) | 82% | 1d ago | n/a | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 261 | [ ] | Warhammer 40,000: Boltgun (GOG) | 12 | 20 | 60% (last 20) | Does not open (75%) | 62% | 5d ago | 54% |  |
| 262 | [ ] | Big Walk (STEAM) | 11 | 20 | 55% (last 20) | Does not open (63%) | 68% | 15d ago | 43% (drop) |  |
| 263 | [ ] | Hylics (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (67%) | 97% | 2d ago | 93% |  |
| 264 | [ ] | Hatred (STEAM) | 10 | 20 | 50% (last 20) | Does not open (69%) | 89% | 10d ago | 94% |  |
| 265 | [ ] | UNBEATABLE (STEAM) | 10 | 20 | 50% (last 20) | Does not open (73%) | 93% | 6d ago | 89% |  |
| 266 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 62% | 2d ago | n/a |  |
| 267 | [ ] | Scrap Mechanic (STEAM) | 13 | 20 | 65% (last 20) | Does not open (50%) | 73% | 8d ago | n/a |  |
| 268 | [ ] | Timberborn (STEAM) | 12 | 20 | 60% (last 20) | No graphics (62%) | 95% | 2d ago | n/a |  |
| 269 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 12 | 20 | 60% (last 20) | Does not open (85%) | 64% | 12d ago | 67% |  |
| 270 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 12 | 20 | 60% (last 20) | Does not open (90%) | 69% | today | 73% |  |
| 271 | [ ] | Sons Of The Forest (STEAM) | 12 | 20 | 60% (last 20) | Does not open (57%) | 78% | 3d ago | 71% |  |
| 272 | [ ] | Nex Machina (STEAM) | 12 | 20 | 60% (last 20) | No graphics (50%) | 75% | 10d ago | 91% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 273 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 11 | 20 | 55% (last 20) | Does not open (100%) | 73% | today | n/a |  |
| 274 | [ ] | Horny Villa (STEAM) | 11 | 20 | 55% (last 20) | Does not open (67%) | 85% | 8d ago | 70% |  |
| 275 | [ ] | Drift Legends 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (71%) | 82% | 9d ago | 72% |  |
| 276 | [ ] | CRUEL (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 76% | 3d ago | 71% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 277 | [ ] | Hitman: Absolution (GOG) | 10 | 20 | 50% (last 20) | Does not open (83%) | 82% | today | n/a |  |
| 278 | [ ] | No Man's Sky (GOG) | 10 | 20 | 50% (last 20) | Does not open (36%) | 90% | 3d ago | 100% |  |
| 279 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 12 | 20 | 60% (last 20) | Does not open (83%) | 81% | today | 91% |  |
| 280 | [ ] | Portal: Revolution (STEAM) | 11 | 20 | 55% (last 20) | Controller issues (92%) | 88% | 13d ago | n/a |  |
| 281 | [ ] | Forgive Me Father (STEAM) | 11 | 20 | 55% (last 20) | Does not open (89%) | 72% | 4d ago | n/a |  |
| 282 | [ ] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (45%) | 65% | 3d ago | 48% |  |
| 283 | [ ] | Guildrun Demo (STEAM) | 10 | 20 | 50% (last 20) | Does not open (50%) | 69% | 3d ago | n/a | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 284 | [ ] | Dragon Age™: Origins - Ultimate Edition (GOG) | 10 | 20 | 50% (last 20) | Does not open (77%) | 69% | 2d ago | n/a |  |
| 285 | [ ] | Grim Fandango Remastered (GOG) | 10 | 20 | 50% (last 20) | No graphics (86%) | 60% | 1d ago | 73% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 286 | [ ] | Intravenous (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 78% | 9d ago | 79% |  |
| 287 | [ ] | The Stanley Parable (STEAM) | 12 | 20 | 60% (last 20) | Does not open (89%) | 86% | 4d ago | n/a |  |
| 288 | [ ] | SILENT HILL 2 (STEAM) | 12 | 20 | 60% (last 20) | Does not open (58%) | 78% | 3d ago | 92% |  |
| 289 | [ ] | Shift At Midnight (STEAM) | 12 | 20 | 60% (last 20) | Does not open (67%) | 90% | today | 86% |  |
| 290 | [ ] | Nioh: Complete Edition (STEAM) | 11 | 20 | 55% (last 20) | Does not open (52%) | 90% | 20d ago | n/a | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 291 | [ ] | Subnautica: Below Zero (STEAM) | 10 | 20 | 50% (last 20) | Does not open (56%) | 75% | 9d ago | 69% |  |
| 292 | [ ] | Cruelty Squad (STEAM) | 10 | 20 | 50% (last 20) | Does not open (60%) | 85% | 1d ago | 79% |  |
| 293 | [ ] | A Plague Tale: Innocence (GOG) | 10 | 20 | 50% (last 20) | Does not open (91%) | 62% | today | n/a |  |
| 294 | [ ] | The Outer Worlds (EPIC) | 12 | 20 | 60% (last 20) | Does not open (100%) | 92% | 2d ago | n/a |  |
| 295 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 20 | 55% (last 20) | Does not open (86%) | 73% | 11d ago | n/a |  |
| 296 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 92% | 8d ago | 93% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 297 | [ ] | Legend of Grimrock 2 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (92%) | 93% | 1d ago | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 298 | [ ] | Decktamer (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 75% | 3d ago | n/a |  |
| 299 | [ ] | Haydee (STEAM) | 10 | 20 | 50% (last 20) | Does not open (100%) | 87% | 3d ago | n/a |  |
| 300 | [ ] | DiRT 4 (STEAM) | 10 | 20 | 50% (last 20) | Does not open (70%) | 96% | 3d ago | 93% |  |
| 301 | [ ] | Secret of Mana (STEAM) | 10 | 20 | 50% (last 20) | Graphics glitches (60%) | 70% | today | n/a |  |

## Recently recovered (398)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | Grim Dawn (STEAM) | 498 | 2026-11-08 | 569 | 65% |  |
| 2 | [x] | FINAL FANTASY RESONANCE (STEAM) | 437 | 2026-10-24 | 1002 | 79% |  |
| 3 | [x] | Half-Life (STEAM) | 384 | 2026-11-09 | 655 | 71% |  |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 264 | 2026-11-14 | 414 | 64% |  |
| 5 | [x] | Alan Wake (STEAM) | 239 | 2026-11-14 | 262 | 52% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 6 | [x] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 233 | 2026-11-09 | 326 | 90% | [#485](https://github.com/GameNative/gamenative-compat/issues/485) |
| 7 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 220 | 2026-10-19 | 281 | 68% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 8 | [x] | MONSTER HUNTER RISE (STEAM) | 219 | 2026-11-17 | 522 | 60% |  |
| 9 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 208 | 2026-11-09 | 249 | 59% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 10 | [x] | Fallout 3 - Game of the Year Edition (STEAM) | 205 | 2026-11-09 | 359 | 70% |  |
| 11 | [x] | BeamNG.drive (STEAM) | 198 | 2026-11-09 | 240 | 73% | [#486](https://github.com/GameNative/gamenative-compat/issues/486) |
| 12 | [x] | Call of Duty: Black Ops (STEAM) | 194 | 2026-11-13 | 219 | 22% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 13 | [x] | Devil May Cry HD Collection (STEAM) | 189 | 2026-10-19 | 281 | 78% |  |
| 14 | [x] | OMORI (STEAM) | 184 | 2026-11-09 | 227 | 69% | [#487](https://github.com/GameNative/gamenative-compat/issues/487) |
| 15 | [x] | DREDGE (EPIC) | 177 | 2026-11-09 | 218 | 60% | [#489](https://github.com/GameNative/gamenative-compat/issues/489) |
| 16 | [x] | DRAGON BALL FighterZ (STEAM) | 173 | 2026-11-01 | 216 | 83% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 17 | [x] | Spelunky 2 (STEAM) | 165 | 2026-11-01 | 201 | 77% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 18 | [x] | Sid Meier's Civilization V (STEAM) | 151 | 2026-11-10 | 163 | 63% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 19 | [x] | Geometry Dash (STEAM) | 150 | 2026-11-11 | 441 | 54% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 20 | [x] | BioShock (STEAM) | 150 | 2026-11-09 | 298 | 73% |  |
| 21 | [x] | Prototype (STEAM) | 140 | 2026-11-11 | 206 | 60% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 22 | [x] | Team Fortress 2 (STEAM) | 136 | 2026-11-09 | 236 | 75% |  |
| 23 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 131 | 2026-11-18 | 177 | 60% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 24 | [x] | Minecraft Dungeons II (STEAM) | 130 | 2026-11-09 | 149 | 69% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 25 | [x] | Castlevania Advance Collection (STEAM) | 128 | 2026-11-09 | 199 | 88% | [#492](https://github.com/GameNative/gamenative-compat/issues/492) |
| 26 | [x] | Mirror's Edge (STEAM) | 118 | 2026-11-09 | 171 | 66% | [#491](https://github.com/GameNative/gamenative-compat/issues/491) |
| 27 | [x] | Counter-Strike (STEAM) | 117 | 2026-11-11 | 197 | 38% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 28 | [x] | Assassin's Creed II (STEAM) | 116 | 2026-11-10 | 121 | 65% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 29 | [x] | Aniimo (STEAM) | 114 | 2026-11-09 | 153 | 85% | [#495](https://github.com/GameNative/gamenative-compat/issues/495) |
| 30 | [x] | Cave Story+ (STEAM) | 105 | 2026-11-09 | 116 | 82% | [#494](https://github.com/GameNative/gamenative-compat/issues/494) |
| 31 | [x] | The Witcher: Enhanced Edition (STEAM) | 104 | 2026-11-09 | 122 | 63% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 32 | [x] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 101 | 2026-11-09 | 142 | 94% | [#496](https://github.com/GameNative/gamenative-compat/issues/496) |
| 33 | [x] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 98 | 2026-11-15 | 136 | 64% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 34 | [x] | Happy Wheels (STEAM) | 97 | 2026-11-09 | 117 | 69% | [#498](https://github.com/GameNative/gamenative-compat/issues/498) |
| 35 | [x] | Moonstone Island (STEAM) | 95 | 2026-11-09 | 124 | 74% | [#497](https://github.com/GameNative/gamenative-compat/issues/497) |
| 36 | [x] | Catherine Classic (STEAM) | 89 | 2026-11-09 | 167 | 58% |  |
| 37 | [x] | Quake (STEAM) | 85 | 2026-11-09 | 247 | 74% |  |
| 38 | [x] | DOOM 3: BFG Edition (STEAM) | 85 | 2026-11-09 | 126 | 71% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 39 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 83 | 2026-11-09 | 137 | 67% |  |
| 40 | [x] | Hi-Fi RUSH (STEAM) | 82 | 2026-11-11 | 114 | 44% | [#499](https://github.com/GameNative/gamenative-compat/issues/499) |
| 41 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 82 | 2026-11-09 | 109 | 93% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 42 | [x] | Vital Shell (STEAM) | 80 | 2026-11-09 | 129 | 85% |  |
| 43 | [x] | FINAL FANTASY XIII-2 (STEAM) | 80 | 2026-11-09 | 83 | 67% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 44 | [x] | Age of Empires II: Definitive Edition (STEAM) | 78 | 2026-11-10 | 97 | 59% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 45 | [x] | Psychonauts (STEAM) | 76 | 2026-11-09 | 140 | 94% |  |
| 46 | [x] | Brawlhalla (STEAM) | 73 | 2026-11-09 | 145 | 75% |  |
| 47 | [x] | Ballionaire (STEAM) | 73 | 2026-11-09 | 123 | 81% |  |
| 48 | [x] | Antivirus Survivors 2003 Professional (STEAM) | 73 | 2026-11-09 | 113 | 81% |  |
| 49 | [x] | The Sims™ 4 (STEAM) | 72 | 2026-11-09 | 97 | 72% | [#503](https://github.com/GameNative/gamenative-compat/issues/503) |
| 50 | [x] | STEINS;GATE (STEAM) | 71 | 2026-11-09 | 103 | 90% | [#502](https://github.com/GameNative/gamenative-compat/issues/502) |
| 51 | [x] | Cyberpunk 2077 (GOG) | 71 | 2026-11-09 | 93 | 70% | [#505](https://github.com/GameNative/gamenative-compat/issues/505) |
| 52 | [x] | Caravan SandWitch (EPIC) | 68 | 2026-11-09 | 130 | 69% |  |
| 53 | [x] | Dota 2 (STEAM) | 68 | 2026-11-09 | 102 | 74% |  |
| 54 | [x] | Disgaea 5 Complete (STEAM) | 68 | 2026-11-09 | 80 | 90% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 55 | [x] | Spyro™ Reignited Trilogy (STEAM) | 67 | 2026-11-09 | 109 | 78% |  |
| 56 | [x] | MIO: Memories in Orbit (STEAM) | 66 | 2026-11-09 | 122 | 95% | [#504](https://github.com/GameNative/gamenative-compat/issues/504) |
| 57 | [x] | Fable - The Lost Chapters (STEAM) | 66 | 2026-11-09 | 106 | 82% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 58 | [x] | Stardew Valley (GOG) | 65 | 2026-11-11 | 114 | 74% |  |
| 59 | [x] | Need for Speed: Hot Pursuit (STEAM) | 65 | 2026-11-09 | 101 | 78% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 60 | [x] | Order of the Sinking Star (STEAM) | 65 | 2026-11-09 | 97 | 68% | [#508](https://github.com/GameNative/gamenative-compat/issues/508) |
| 61 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 64 | 2026-11-09 | 101 | 86% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 62 | [x] | Diablo® IV (STEAM) | 63 | 2026-11-11 | 75 | 69% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 63 | [x] | Fallout (STEAM) | 62 | 2026-11-09 | 96 | 71% |  |
| 64 | [x] | Sovereign Tower (STEAM) | 61 | 2026-11-09 | 115 | 73% |  |
| 65 | [x] | American Truck Simulator (STEAM) | 61 | 2026-11-09 | 103 | 76% |  |
| 66 | [x] | Poppy Playtime (STEAM) | 61 | 2026-11-09 | 103 | 68% |  |
| 67 | [x] | Call of Duty: Black Ops II - Zombies (STEAM) | 61 | 2026-11-11 | 81 | 56% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 68 | [x] | Mini Motorways (STEAM) | 60 | 2026-11-09 | 98 | 71% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 69 | [x] | Borderlands 3 (STEAM) | 60 | 2026-11-09 | 87 | 90% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 70 | [x] | Gunfire Reborn (STEAM) | 60 | 2026-11-09 | 66 | 88% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 71 | [x] | A Plague Tale: Innocence (STEAM) | 59 | 2026-11-09 | 62 | 71% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 72 | [x] | Firewatch (STEAM) | 58 | 2026-11-10 | 112 | 78% |  |
| 73 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 58 | 2026-11-09 | 83 | 66% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 74 | [x] | Deskrawl: Idle ARPG (STEAM) | 58 | 2026-11-09 | 72 | 82% | [#506](https://github.com/GameNative/gamenative-compat/issues/506) |
| 75 | [x] | Grand Theft Auto V (EPIC) | 57 | 2026-11-09 | 64 | 77% | [#509](https://github.com/GameNative/gamenative-compat/issues/509) |
| 76 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 56 | 2026-10-25 | 97 | 74% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 77 | [x] | eFootball™ (STEAM) | 56 | 2026-11-09 | 84 | 66% |  |
| 78 | [x] | Call of Duty: World at War (STEAM) | 56 | 2026-11-09 | 80 | 84% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 79 | [x] | Call of Juarez Gunslinger (STEAM) | 56 | 2026-11-09 | 71 | 77% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 80 | [x] | Darksiders (STEAM) | 55 | 2026-11-09 | 70 | 86% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 81 | [x] | Starbound (STEAM) | 54 | 2026-11-09 | 87 | 80% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 82 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 54 | 2026-11-17 | 78 | 61% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 83 | [x] | Sonic Generations (STEAM) | 54 | 2026-11-09 | 61 | 70% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 84 | [x] | Sol Cesto (EPIC) | 53 | 2026-11-09 | 54 | 80% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 85 | [x] | TBH: Task Bar Hero (STEAM) | 52 | 2026-11-09 | 84 | 85% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 86 | [x] | Borderlands: The Pre-Sequel (STEAM) | 51 | 2026-11-09 | 88 | 61% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 87 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 50 | 2026-11-09 | 84 | 75% |  |
| 88 | [x] | Last Epoch (STEAM) | 50 | 2026-11-09 | 75 | 72% |  |
| 89 | [x] | Okami HD (STEAM) | 49 | 2026-11-09 | 91 | 93% |  |
| 90 | [x] | Dungeons & Degenerate Gamblers (STEAM) | 49 | 2026-11-09 | 83 | 86% |  |
| 91 | [x] | Overwatch® (STEAM) | 49 | 2026-11-10 | 53 | 69% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 92 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 48 | 2026-11-09 | 82 | 59% |  |
| 93 | [x] | Heroes of Might & Magic III - HD Edition (STEAM) | 48 | 2026-11-14 | 63 | 62% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 94 | [x] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 47 | 2026-11-09 | 77 | 81% |  |
| 95 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 47 | 2026-11-09 | 54 | 90% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 96 | [x] | Moonlighter (EPIC) | 47 | 2026-11-09 | 51 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 97 | [x] | Oxygen Not Included (STEAM) | 46 | 2026-11-11 | 79 | 61% |  |
| 98 | [x] | Road Rash™: 30th Anniversary Edition (STEAM) | 45 | 2026-11-13 | 69 | 62% | [#517](https://github.com/GameNative/gamenative-compat/issues/517) |
| 99 | [x] | MudRunner (STEAM) | 44 | 2026-10-24 | 99 | 61% |  |
| 100 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 44 | 2026-10-19 | 89 | 73% |  |
| 101 | [x] | Darkest Dungeon® (EPIC) | 44 | 2026-11-09 | 85 | 82% | [#510](https://github.com/GameNative/gamenative-compat/issues/510) |
| 102 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 44 | 2026-11-09 | 69 | 91% |  |
| 103 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 43 | 2026-11-09 | 74 | 50% |  |
| 104 | [x] | Plague Inc: Evolved (STEAM) | 43 | 2026-11-16 | 64 | 63% | [#526](https://github.com/GameNative/gamenative-compat/issues/526) |
| 105 | [x] | Sheepy: A Short Adventure (STEAM) | 42 | 2026-11-09 | 50 | 67% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 106 | [x] | Big Walk (STEAM) | 40 | 2026-11-09 | 64 | 68% |  |
| 107 | [x] | Tomb Raider: Anniversary (STEAM) | 40 | 2026-11-09 | 64 | 59% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 108 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 39 | 2026-11-09 | 71 | 91% |  |
| 109 | [x] | Age of Empires II (2013) (STEAM) | 39 | 2026-11-09 | 64 | 73% |  |
| 110 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 39 | 2026-11-09 | 60 | 67% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 111 | [x] | Dead by Daylight (STEAM) | 39 | 2026-11-09 | 43 | 83% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 112 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-11-09 | 40 | 79% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 113 | [x] | Ace Attorney Investigations Collection (STEAM) | 38 | 2026-11-09 | 67 | 86% |  |
| 114 | [x] | Sonic Lost World (STEAM) | 38 | 2026-11-09 | 58 | 79% | [#513](https://github.com/GameNative/gamenative-compat/issues/513) |
| 115 | [x] | Aggelos (STEAM) | 38 | 2026-11-09 | 54 | 88% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 116 | [x] | Digimon World: Next Order (STEAM) | 37 | 2026-11-09 | 75 | 85% |  |
| 117 | [x] | Amnesia: The Dark Descent (STEAM) | 37 | 2026-11-09 | 73 | 84% |  |
| 118 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 37 | 2026-11-09 | 70 | 89% |  |
| 119 | [x] | FINAL FANTASY VII (2013) (STEAM) | 37 | 2026-11-09 | 54 | 57% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 120 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 37 | 2026-11-09 | 50 | 77% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 121 | [x] | Sonic Origins (STEAM) | 36 | 2026-11-09 | 67 | 83% |  |
| 122 | [x] | XCOM 2 (STEAM) | 36 | 2026-11-09 | 61 | 80% |  |
| 123 | [x] | Street Fighter™ 6 (STEAM) | 36 | 2026-11-09 | 58 | 83% |  |
| 124 | [x] | Capcom Arcade Stadium (STEAM) | 36 | 2026-11-09 | 46 | 72% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 125 | [x] | CrossCode (GOG) | 36 | 2026-11-09 | 39 | 78% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 126 | [x] | POSTAL 2 (GOG) | 35 | 2026-11-09 | 69 | 89% |  |
| 127 | [x] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 35 | 2026-11-09 | 65 | 84% |  |
| 128 | [x] | Russian Fishing 4 (STEAM) | 35 | 2026-11-09 | 41 | 80% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 129 | [x] | Elite Dangerous (STEAM) | 35 | 2026-11-09 | 38 | 60% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 130 | [x] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 34 | 2026-11-09 | 61 | 72% |  |
| 131 | [x] | Need for Speed™ Rivals (STEAM) | 34 | 2026-11-10 | 46 | 81% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 132 | [x] | Romestead (STEAM) | 34 | 2026-11-09 | 44 | 61% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 133 | [x] | Being a DIK (STEAM) | 33 | 2026-11-09 | 72 | 60% |  |
| 134 | [x] | SurrounDead (STEAM) | 33 | 2026-11-09 | 65 | 90% |  |
| 135 | [x] | The Bazaar (STEAM) | 33 | 2026-11-09 | 63 | 73% |  |
| 136 | [x] | Hero Siege (STEAM) | 33 | 2026-11-09 | 57 | 82% |  |
| 137 | [x] | Max Payne (STEAM) | 33 | 2026-11-09 | 57 | 85% |  |
| 138 | [x] | Gauntlet™  (STEAM) | 33 | 2026-11-11 | 48 | 69% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 139 | [x] | Journey (STEAM) | 32 | 2026-10-27 | 73 | 70% |  |
| 140 | [x] | Hearts of Iron IV (STEAM) | 32 | 2026-11-09 | 62 | 83% |  |
| 141 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 32 | 2026-11-09 | 56 | 73% |  |
| 142 | [x] | Earthion (STEAM) | 32 | 2026-11-09 | 54 | 100% |  |
| 143 | [x] | SnowRunner (STEAM) | 32 | 2026-11-09 | 47 | 81% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 144 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-11-09 | 41 | 92% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 145 | [x] | Red Dead Redemption (STEAM) | 32 | 2026-11-09 | 35 | 58% | [#516](https://github.com/GameNative/gamenative-compat/issues/516) |
| 146 | [x] | COCOON (STEAM) | 31 | 2026-11-09 | 66 | 83% |  |
| 147 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 30 | 2026-11-09 | 67 | 72% |  |
| 148 | [x] | Ultimate Chicken Horse (STEAM) | 30 | 2026-10-23 | 64 | 83% |  |
| 149 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 30 | 2026-11-09 | 62 | 83% |  |
| 150 | [x] | Resident Evil Village (STEAM) | 30 | 2026-11-09 | 52 | 88% |  |
| 151 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 30 | 2026-11-09 | 51 | 88% |  |
| 152 | [x] | Prince of Persia: The Sands of Time (STEAM) | 30 | 2026-11-09 | 50 | 77% |  |
| 153 | [x] | Counter-Strike:Global Offensive (STEAM) | 30 | 2026-11-09 | 46 | 72% |  |
| 154 | [x] | Supermarket Together (STEAM) | 30 | 2026-11-18 | 42 | 62% | [#515](https://github.com/GameNative/gamenative-compat/issues/515) |
| 155 | [x] | ROB RUN (STEAM) | 30 | 2026-11-17 | 38 | 63% | [#533](https://github.com/GameNative/gamenative-compat/issues/533) |
| 156 | [x] | Hotline Miami (GOG) | 30 | 2026-11-18 | 37 | 67% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 157 | [x] | Torchlight II (STEAM) | 29 | 2026-10-20 | 72 | 86% |  |
| 158 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 29 | 2026-11-09 | 50 | 89% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 159 | [x] | Secrets of Grindea (STEAM) | 29 | 2026-11-09 | 49 | 75% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 160 | [x] | Gambonanza (STEAM) | 29 | 2026-11-09 | 47 | 92% |  |
| 161 | [x] | Heroes of Might and Magic: Olden Era (STEAM) | 29 | 2026-11-09 | 47 | 82% |  |
| 162 | [x] | Yakuza: Like a Dragon (STEAM) | 29 | 2026-11-09 | 46 | 64% |  |
| 163 | [x] | Nioh: Complete Edition (STEAM) | 29 | 2026-11-18 | 39 | 90% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 164 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-10 | 35 | 72% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 165 | [x] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 29 | 2026-11-14 | 34 | 73% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 166 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 28 | 2026-11-09 | 48 | 68% |  |
| 167 | [x] | Heavy Rain (STEAM) | 28 | 2026-11-09 | 47 | 94% |  |
| 168 | [x] | Palia (STEAM) | 28 | 2026-11-09 | 40 | 76% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 169 | [x] | Resident Evil Revelations 2 (STEAM) | 27 | 2026-11-09 | 53 | 82% |  |
| 170 | [x] | Deponia (STEAM) | 27 | 2026-11-09 | 52 | 73% |  |
| 171 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 27 | 2026-11-09 | 49 | 96% |  |
| 172 | [x] | Dead Rising 2 (STEAM) | 27 | 2026-11-09 | 43 | 80% |  |
| 173 | [x] | Tower and Sword of Succubus (STEAM) | 27 | 2026-11-09 | 42 | 82% |  |
| 174 | [x] | Digimon Survive (STEAM) | 27 | 2026-11-09 | 40 | 83% |  |
| 175 | [x] | Gothic II: Gold Classic (STEAM) | 27 | 2026-11-09 | 35 | 65% | [#518](https://github.com/GameNative/gamenative-compat/issues/518) |
| 176 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 26 | 2026-10-19 | 91 | 92% |  |
| 177 | [x] | Skullgirls 2nd Encore (STEAM) | 26 | 2026-11-10 | 61 | 67% |  |
| 178 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 26 | 2026-11-09 | 40 | 70% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 179 | [x] | CRUEL (STEAM) | 26 | 2026-11-09 | 36 | 76% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 180 | [x] | Frostpunk (STEAM) | 25 | 2026-11-09 | 51 | 74% |  |
| 181 | [x] | Zero Escape: The Nonary Games (STEAM) | 25 | 2026-11-09 | 44 | 67% |  |
| 182 | [x] | Guildrun Demo (STEAM) | 25 | 2026-11-09 | 42 | 69% | [#511](https://github.com/GameNative/gamenative-compat/issues/511) |
| 183 | [x] | Changed (STEAM) | 25 | 2026-11-18 | 36 | 61% | [#529](https://github.com/GameNative/gamenative-compat/issues/529) |
| 184 | [x] | Subnautica 2 (STEAM) | 25 | 2026-11-15 | 30 | 79% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 185 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 24 | 2026-10-20 | 53 | 85% |  |
| 186 | [x] | Slow Roads (STEAM) | 24 | 2026-10-22 | 50 | 73% |  |
| 187 | [x] | Mirror's Edge™ (GOG) | 24 | 2026-11-13 | 45 | 71% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 188 | [x] | Lucid Blocks (STEAM) | 24 | 2026-11-09 | 45 | 66% |  |
| 189 | [x] | Battle Brothers (STEAM) | 24 | 2026-11-09 | 44 | 82% |  |
| 190 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 24 | 2026-11-09 | 43 | 65% |  |
| 191 | [x] | Counter-Strike: Condition Zero (STEAM) | 24 | 2026-11-11 | 43 | 31% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 192 | [x] | Capcom Fighting Collection 2 (STEAM) | 24 | 2026-11-09 | 41 | 82% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 193 | [x] | Opus Magnum (STEAM) | 24 | 2026-11-09 | 39 | 92% |  |
| 194 | [x] | Limbus Company (STEAM) | 24 | 2026-11-09 | 38 | 83% |  |
| 195 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 24 | 2026-11-09 | 38 | 73% |  |
| 196 | [x] | Ratatan (STEAM) | 24 | 2026-11-09 | 37 | 90% |  |
| 197 | [x] | Jade Empire: Special Edition (GOG) | 24 | 2026-11-09 | 31 | 70% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 198 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 24 | 2026-11-09 | 31 | 91% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 199 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 24 | 2026-11-09 | 30 | 73% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 200 | [x] | Crab Game (STEAM) | 24 | 2026-11-09 | 28 | 84% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 201 | [x] | Jade Empire: Special Edition (STEAM) | 24 | 2026-11-09 | 27 | 75% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 202 | [x] | Hatred (STEAM) | 23 | 2026-11-09 | 45 | 89% |  |
| 203 | [x] | Prince of Persia (GOG) | 23 | 2026-11-09 | 44 | 83% |  |
| 204 | [x] | Trailmakers (STEAM) | 23 | 2026-11-09 | 41 | 93% |  |
| 205 | [x] | Cat Mail Co. (STEAM) | 23 | 2026-11-09 | 39 | 83% |  |
| 206 | [x] | Dishonored 2 (STEAM) | 23 | 2026-11-09 | 33 | 75% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 207 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 92% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 208 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 23 | 2026-11-09 | 27 | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 209 | [x] | Goat Simulator (STEAM) | 22 | 2026-11-09 | 47 | 69% |  |
| 210 | [x] | Crazy Taxi (STEAM) | 22 | 2026-11-10 | 44 | 67% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 211 | [x] | Lobotomy Corporation (STEAM) | 22 | 2026-11-09 | 43 | 92% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 212 | [x] | Wizard of Legend (EPIC) | 22 | 2026-11-09 | 41 | 82% |  |
| 213 | [x] | Football Manager 2024 (EPIC) | 22 | 2026-11-09 | 40 | 65% |  |
| 214 | [x] | Unturned (STEAM) | 22 | 2026-11-09 | 40 | 71% |  |
| 215 | [x] | My Summer Car (STEAM) | 22 | 2026-11-09 | 37 | 82% |  |
| 216 | [x] | Tabletop Simulator (STEAM) | 22 | 2026-11-09 | 36 | 79% |  |
| 217 | [x] | Deus Ex™ GOTY Edition (GOG) | 22 | 2026-11-09 | 35 | 92% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 218 | [x] | Timberborn (STEAM) | 22 | 2026-11-09 | 34 | 95% |  |
| 219 | [x] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 2026-11-09 | 59 | 97% | [#519](https://github.com/GameNative/gamenative-compat/issues/519) |
| 220 | [x] | No Rest for the Wicked (STEAM) | 21 | 2026-10-19 | 46 | 71% |  |
| 221 | [x] | Control Ultimate Edition (GOG) | 21 | 2026-11-09 | 39 | 79% |  |
| 222 | [x] | Invisible, Inc. (STEAM) | 21 | 2026-11-09 | 37 | 77% |  |
| 223 | [x] | Sorry We're Closed (EPIC) | 21 | 2026-11-09 | 36 | 71% |  |
| 224 | [x] | Goose Goose Duck (STEAM) | 21 | 2026-11-18 | 31 | 64% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 225 | [x] | Metro Exodus (STEAM) | 21 | 2026-11-09 | 30 | 88% |  |
| 226 | [x] | CarX Street (STEAM) | 21 | 2026-11-09 | 26 | 82% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 227 | [x] | Dead Island (STEAM) | 21 | 2026-11-09 | 26 | 90% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 228 | [x] | Tearscape (STEAM) | 21 | 2026-11-09 | 25 | 100% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 229 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-11-09 | 38 | 100% |  |
| 230 | [x] | Worms W.M.D (STEAM) | 20 | 2026-11-09 | 37 | 97% |  |
| 231 | [x] | Pinball FX Classic (STEAM) | 20 | 2026-11-09 | 36 | 87% |  |
| 232 | [x] | Return to Monkey Island (STEAM) | 20 | 2026-11-09 | 33 | 70% |  |
| 233 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 20 | 2026-11-09 | 30 | 92% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 234 | [x] | Torchlight II (EPIC) | 20 | 2026-11-09 | 28 | 73% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 235 | [x] | Tyr (STEAM) | 20 | 2026-11-09 | 28 | 73% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 236 | [x] | Tales of Zestiria (STEAM) | 20 | 2026-11-09 | 26 | 73% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 237 | [x] | Saints Row IV (STEAM) | 19 | 2026-10-19 | 50 | 86% |  |
| 238 | [x] | Mini Metro (STEAM) | 19 | 2026-11-16 | 38 | 46% |  |
| 239 | [x] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 2026-11-15 | 36 | 65% | [#530](https://github.com/GameNative/gamenative-compat/issues/530) |
| 240 | [x] | SWORN (STEAM) | 19 | 2026-11-09 | 34 | 93% |  |
| 241 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 19 | 2026-11-09 | 33 | 78% |  |
| 242 | [x] | Far Far West (STEAM) | 19 | 2026-11-09 | 33 | 54% |  |
| 243 | [x] | One-armed robber (STEAM) | 19 | 2026-11-09 | 33 | 70% |  |
| 244 | [x] | Formula Legends (STEAM) | 19 | 2026-11-11 | 32 | 76% |  |
| 245 | [x] | Moonlight Peaks (STEAM) | 19 | 2026-11-09 | 31 | 75% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 246 | [x] | GOD EATER RESURRECTION (STEAM) | 19 | 2026-11-09 | 30 | 78% |  |
| 247 | [x] | Backpack Battles (STEAM) | 18 | 2026-11-09 | 42 | 97% |  |
| 248 | [x] | This War of Mine (STEAM) | 18 | 2026-11-17 | 35 | 46% |  |
| 249 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 2026-11-09 | 29 | 82% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 250 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-11-09 | 27 | 78% |  |
| 251 | [x] | Capcom Fighting Collection (STEAM) | 18 | 2026-11-09 | 26 | 87% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 252 | [x] | Need for Speed™ Unbound (STEAM) | 18 | 2026-11-09 | 26 | 54% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 253 | [x] | Party Animals (STEAM) | 18 | 2026-11-09 | 26 | 67% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 254 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-18 | 23 | 70% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 255 | [x] | Mafia II: Definitive Edition (GOG) | 18 | 2026-11-15 | 20 | 60% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 256 | [x] | Undisputed (STEAM) | 18 | 2026-11-14 | 20 | 67% | [#521](https://github.com/GameNative/gamenative-compat/issues/521) |
| 257 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 17 | 2026-10-19 | 58 | 78% |  |
| 258 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 37 | 27% |  |
| 259 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 33 | 92% |  |
| 260 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 261 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 262 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 51 | 95% |  |
| 263 | [x] | Kingdom Come: Deliverance II (STEAM) | 16 | 2026-10-20 | 39 | 84% |  |
| 264 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 16 | 2026-10-20 | 37 | 81% |  |
| 265 | [x] | GRIP: Combat Racing (STEAM) | 16 | 2026-11-09 | 35 | 79% |  |
| 266 | [x] | sobosuba (STEAM) | 16 | 2026-11-09 | 34 | 84% |  |
| 267 | [x] | Intravenous 2 (STEAM) | 16 | 2026-11-09 | 31 | 96% |  |
| 268 | [x] | Race The Sun (STEAM) | 16 | 2026-11-11 | 31 | 36% |  |
| 269 | [x] | Tiny Glade (STEAM) | 16 | 2026-11-09 | 31 | 67% |  |
| 270 | [x] | Mortal Kombat 11 (STEAM) | 16 | 2026-11-09 | 29 | 75% |  |
| 271 | [x] | Legend of Grimrock 2 (STEAM) | 16 | 2026-11-09 | 26 | 93% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 272 | [x] | Warhammer 40,000: Boltgun (GOG) | 16 | 2026-11-13 | 25 | 62% |  |
| 273 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-09 | 20 | 100% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 274 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 275 | [x] | ABZÛ (STEAM) | 15 | 2026-10-21 | 44 | 92% |  |
| 276 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 15 | 2026-10-21 | 42 | 77% |  |
| 277 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 15 | 2026-10-25 | 41 | 73% |  |
| 278 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 15 | 2026-11-11 | 33 | 71% |  |
| 279 | [x] | Mark of the Ninja (STEAM) | 15 | 2026-10-26 | 32 | 85% |  |
| 280 | [x] | SKALD: Against the Black Priory (STEAM) | 15 | 2026-11-09 | 31 | 96% |  |
| 281 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 15 | 2026-11-09 | 29 | 83% |  |
| 282 | [x] | GRANDIA HD Remaster (STEAM) | 15 | 2026-11-09 | 28 | 88% |  |
| 283 | [x] | AER Memories of Old (EPIC) | 15 | 2026-11-09 | 25 | 100% |  |
| 284 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 15 | 2026-11-15 | 25 | 64% |  |
| 285 | [x] | Alabaster Dawn Demo (STEAM) | 15 | 2026-11-09 | 23 | 76% |  |
| 286 | [x] | DOOM 3: BFG Edition (GOG) | 15 | 2026-11-09 | 22 | 93% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 287 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 288 | [x] | Spark the Electric Jester (STEAM) | 15 | 2026-11-13 | 21 | 69% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 289 | [x] | The Elder Scrolls II: Daggerfall (STEAM) | 15 | 2026-11-09 | 21 | 82% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 290 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 291 | [x] | Grim Fandango Remastered (STEAM) | 14 | 2026-10-19 | 40 | 74% |  |
| 292 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 93% |  |
| 293 | [x] | Hitman: Absolution (GOG) | 14 | 2026-11-09 | 29 | 82% |  |
| 294 | [x] | Killing Floor (STEAM) | 14 | 2026-10-19 | 29 | 85% |  |
| 295 | [x] | Castle in the Clouds (STEAM) | 14 | 2026-11-09 | 28 | 60% |  |
| 296 | [x] | Evoland (STEAM) | 14 | 2026-11-11 | 28 | n/a |  |
| 297 | [x] | Human Fall Flat (STEAM) | 14 | 2026-10-29 | 28 | 64% |  |
| 298 | [x] | Titanfall® 2 (STEAM) | 14 | 2026-11-09 | 28 | 76% |  |
| 299 | [x] | Need for Speed: Undercover (STEAM) | 14 | 2026-11-11 | 27 | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 300 | [x] | Ultrapool (STEAM) | 14 | 2026-11-09 | 27 | 100% |  |
| 301 | [x] | Batman™: Arkham Origins (GOG) | 14 | 2026-11-09 | 26 | 100% |  |
| 302 | [x] | WORLD OF FINAL FANTASY (STEAM) | 14 | 2026-11-09 | 25 | 77% |  |
| 303 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 2026-11-09 | 24 | 69% |  |
| 304 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 2026-11-16 | 23 | 81% |  |
| 305 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-11-09 | 22 | 92% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 306 | [x] | Nex Machina (STEAM) | 14 | 2026-11-09 | 22 | 75% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 307 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 308 | [x] | Scrap Mechanic (STEAM) | 14 | 2026-11-09 | 21 | 73% |  |
| 309 | [x] | Fall Guys (STEAM) | 14 | 2026-11-09 | 20 | 100% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 310 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 311 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 13 | 2026-10-19 | 31 | 93% |  |
| 312 | [x] | Faster Than Light (EPIC) | 13 | 2026-11-09 | 29 | 92% |  |
| 313 | [x] | No Man's Sky (GOG) | 13 | 2026-10-19 | 29 | 90% |  |
| 314 | [x] | Dead Space™ 3 (STEAM) | 13 | 2026-10-20 | 29 | 67% |  |
| 315 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 29 | 81% |  |
| 316 | [x] | Antichamber (STEAM) | 13 | 2026-11-18 | 28 | 82% |  |
| 317 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 13 | 2026-11-09 | 28 | 90% |  |
| 318 | [x] | Revolution Idle (STEAM) | 13 | 2026-11-08 | 28 | 77% |  |
| 319 | [x] | MX Bikes (STEAM) | 13 | 2026-11-09 | 27 | 92% |  |
| 320 | [x] | Blaster Master Zero (STEAM) | 13 | 2026-11-11 | 26 | 75% |  |
| 321 | [x] | Command & Conquer™ Generals Zero Hour (STEAM) | 13 | 2026-11-09 | 26 | 67% |  |
| 322 | [x] | Cruelty Squad (STEAM) | 13 | 2026-11-09 | 26 | 85% |  |
| 323 | [x] | Haydee (STEAM) | 13 | 2026-11-09 | 24 | 87% |  |
| 324 | [x] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 13 | 2026-11-13 | 24 | 64% |  |
| 325 | [x] | Sons Of The Forest (STEAM) | 13 | 2026-11-09 | 24 | 78% |  |
| 326 | [x] | 12 is Better Than 6 (STEAM) | 13 | 2026-11-09 | 22 | 85% |  |
| 327 | [x] | PAYDAY: The Heist (STEAM) | 13 | 2026-11-13 | 22 | 67% |  |
| 328 | [x] | GRIP (GOG) | 13 | 2026-11-09 | 21 | 100% |  |
| 329 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 13 | 2026-11-09 | 21 | 70% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 330 | [x] | The Stanley Parable (STEAM) | 13 | 2026-11-13 | 21 | 86% |  |
| 331 | [x] | [WoG] War of Genesis: Idle Loot (STEAM) | 13 | 2026-11-09 | 21 | 100% |  |
| 332 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 333 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 13 | 2026-11-09 | 20 | 85% |  |
| 334 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-11-16 | 20 | 90% |  |
| 335 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 80% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 336 | [x] | Overlord (STEAM) | 12 | 2026-11-08 | 29 | 55% |  |
| 337 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 12 | 2026-11-09 | 27 | 88% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 338 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 26 | 81% |  |
| 339 | [x] | A Plague Tale: Innocence (GOG) | 12 | 2026-11-18 | 24 | 62% |  |
| 340 | [x] | Grim Fandango Remastered (GOG) | 12 | 2026-11-10 | 24 | 60% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 341 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-11-09 | 24 | 69% |  |
| 342 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-11-09 | 23 | 95% |  |
| 343 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 344 | [x] | Horny Villa (STEAM) | 12 | 2026-11-09 | 21 | 85% |  |
| 345 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 346 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 347 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 2026-11-10 | 20 | 60% |  |
| 348 | [x] | Shift At Midnight (STEAM) | 12 | 2026-11-09 | 20 | 90% |  |
| 349 | [x] | Turbo Overkill (STEAM) | 12 | 2026-11-09 | 20 | 95% |  |
| 350 | [x] | Haiku, the Robot (STEAM) | 11 | 2026-10-21 | 27 | n/a |  |
| 351 | [x] | Soul's Remnant (STEAM) | 11 | 2026-11-11 | 26 | n/a |  |
| 352 | [x] | GRANDIA II HD Remaster (STEAM) | 11 | 2026-11-09 | 25 | 85% |  |
| 353 | [x] | Guacamelee! Gold Edition (STEAM) | 11 | 2026-11-11 | 25 | 75% | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 354 | [x] | Alan Wake's American Nightmare (EPIC) | 11 | 2026-11-09 | 24 | 64% |  |
| 355 | [x] | Coromon (GOG) | 11 | 2026-10-19 | 24 | 65% |  |
| 356 | [x] | Rayman Origins (GOG) | 11 | 2026-11-09 | 24 | 77% |  |
| 357 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 24 | 86% |  |
| 358 | [x] | DiRT 4 (STEAM) | 11 | 2026-11-09 | 23 | 96% |  |
| 359 | [x] | Life is Strange Remastered (STEAM) | 11 | 2026-11-09 | 23 | 86% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 360 | [x] | Ready or Not (STEAM) | 11 | 2026-11-09 | 23 | 85% |  |
| 361 | [x] | Lost Castle 2 (STEAM) | 11 | 2026-11-09 | 22 | 94% |  |
| 362 | [x] | Baldur's Gate II: Enhanced Edition (STEAM) | 11 | 2026-11-18 | 21 | 62% |  |
| 363 | [x] | Forgive Me Father (STEAM) | 11 | 2026-11-15 | 21 | 72% |  |
| 364 | [x] | Secret of Mana (STEAM) | 11 | 2026-11-18 | 21 | 70% |  |
| 365 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 11 | 2026-11-09 | 21 | 94% |  |
| 366 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-11-09 | 20 | 73% |  |
| 367 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 368 | [x] | The WereCleaner (STEAM) | 10 | 2026-10-22 | 31 | 89% |  |
| 369 | [x] | Distance (STEAM) | 10 | 2026-10-19 | 28 | 83% |  |
| 370 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 28 | n/a |  |
| 371 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 10 | 2026-10-27 | 25 | 78% |  |
| 372 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 10 | 2026-11-01 | 24 | n/a |  |
| 373 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 10 | 2026-10-23 | 24 | 87% |  |
| 374 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 24 | 91% |  |
| 375 | [x] | Breath of Fire IV (GOG) | 10 | 2026-10-26 | 23 | 70% |  |
| 376 | [x] | UNDEFEATED (STEAM) | 10 | 2026-11-09 | 21 | 70% |  |
| 377 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 378 | [x] | Beatblock (STEAM) | 10 | 2026-11-09 | 20 | 91% |  |
| 379 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 380 | [x] | Intravenous (STEAM) | 10 | 2026-11-09 | 20 | 78% |  |
| 381 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 382 | [x] | Possessor(s) (STEAM) | 9 | 2026-10-24 | 27 | 86% |  |
| 383 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 9 | 2026-10-20 | 26 | 89% |  |
| 384 | [x] | Aperture Desk Job (STEAM) | 9 | 2026-11-03 | 22 | n/a |  |
| 385 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 9 | 2026-10-21 | 21 | 92% |  |
| 386 | [x] | Sid Meier's Civilization VI (EPIC) | 9 | 2026-10-19 | 20 | 67% |  |
| 387 | [x] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 9 | 2026-11-17 | 20 | 31% |  |
| 388 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 9 | 2026-11-09 | 20 | 74% |  |
| 389 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 33% |  |
| 390 | [x] | Lust Goddess (STEAM) | 8 | 2026-11-09 | 22 | 81% |  |
| 391 | [x] | SteamWorld Heist (GOG) | 8 | 2026-10-25 | 20 | n/a |  |
| 392 | [x] | HITMAN World of Assassination (STEAM) | 8 | 2026-11-09 | 20 | 80% |  |
| 393 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 21 | 55% |  |
| 394 | [x] | SCP – Containment Breach (STEAM) | 7 | 2026-10-27 | 21 | 91% |  |
| 395 | [x] | Mina the Hollower (GOG) | 7 | 2026-10-28 | 20 | 74% |  |
| 396 | [x] | CULTIC (STEAM) | 7 | 2026-11-09 | 20 | 53% |  |
| 397 | [x] | What Remains of Edith Finch (STEAM) | 6 | 2026-10-19 | 28 | 78% |  |
| 398 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 5 | 2026-10-20 | 20 | 69% |  |
