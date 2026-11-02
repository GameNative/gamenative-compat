# GameNative compatibility worklist

Generated: `2026-11-02T04:15:05.877Z` · App release: `1.3.0` · Ratings since: `2026-08-04T04:15:05.877Z` · Telemetry window: `21` days on `Adreno + Turnip`

This file is rewritten every night. To mark a game as fixed, tick its box in the checklist issue linked under each section (or change `[ ]` to `[x]` on its row here). The sync remembers the tick with its date until the data agrees and the game leaves the list. Untick to undo. See the [README](README.md) for how to read it and how to help.

## How a game lands here

- **Does not work**: 20+ ratings, 70%+ one-star, and under 60% of users ever rendered a game window on Adreno + Turnip in the current release (or no telemetry).
- **Probably does not work**: 20+ ratings, 50%+ one-star, under 60% rendered or no telemetry.
- **Works, but the first launch usually fails**: 50%+ one-star but 60%+ of users render the game eventually.
- **Recovered**: the current release shows the game rendering for most users and the last 14 days of ratings are no longer mostly one-star.

"Users rendered" is the share of users on Adreno GPUs with the Turnip driver who got the game to put a frame on screen at least once on the current release. Other GPUs are not counted. "n/a" means no telemetry for that game yet.

## Counts

| Verdict | Games |
|---|---:|
| Does not work | 266 |
| Probably does not work | 78 |
| First launch fails | 367 |
| Mixed | 466 |
| Works | 1023 |
| Total | 2200 |

## Does not work (266)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [x] 2026-10-18 | Project Zomboid (STEAM) | 604 | 638 | 92% (1.3.0) | Does not open (66%) | 52% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 2 | [x] 2026-10-18 | Alan Wake (STEAM) | 259 | 270 | 90% (1.3.0) | Does not open (86%) | 8% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 3 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 253 | 272 | 93% (90d) | Does not open (74%) | 10% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 4 | [ ] | Counter-Strike 2 (STEAM) | 229 | 316 | 81% (1.3.0) | Does not open (61%) | 45% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 5 | [x] 2026-10-18 | Call of Duty: Black Ops (STEAM) | 215 | 226 | 95% (90d) | Does not open (75%) | 12% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 6 | [ ] | skate. (STEAM) | 200 | 216 | 93% (90d) | Does not open (80%) | 16% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 7 | [x] 2026-10-18 | Sid Meier's Civilization V (STEAM) | 178 | 190 | 94% (90d) | Does not open (76%) | 50% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 8 | [ ] | Necesse (STEAM) | 165 | 171 | 96% (90d) | Does not open (80%) | 51% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 9 | [ ] | Peggle Deluxe (STEAM) | 161 | 192 | 84% (90d) | Does not open (92%) | 37% | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 10 | [ ] | HELLDIVERS™ 2 (STEAM) | 140 | 146 | 96% (90d) | Does not open (92%) | 23% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 11 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 136 | 152 | 89% (90d) | Does not open (87%) | 43% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 12 | [ ] | Assassin's Creed II (STEAM) | 126 | 131 | 96% (90d) | Does not open (77%) | 52% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 13 | [ ] | Dust: An Elysian Tail (STEAM) | 108 | 112 | 96% (90d) | Does not open (72%) | 7% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 14 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 105 | 118 | 89% (90d) | No graphics (59%) | 52% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 15 | [ ] | The Witcher: Enhanced Edition (GOG) | 105 | 115 | 91% (90d) | Does not open (73%) | 13% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 16 | [ ] | Transistor (STEAM) | 102 | 102 | 100% (90d) | Does not open (76%) | 0% | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 17 | [ ] | Call of Duty: Black Ops II (STEAM) | 101 | 134 | 85% (1.3.0) | Does not open (78%) | 25% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 18 | [ ] | Mafia II (Classic) (STEAM) | 97 | 102 | 95% (90d) | Does not open (71%) | 6% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 19 | [ ] | Sol Cesto (EPIC) | 95 | 100 | 95% (90d) | Does not open (78%) | 58% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 20 | [ ] | Saints Row 2 (STEAM) | 93 | 105 | 92% (1.3.0) | Does not open (96%) | 41% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 21 | [ ] | Saints Row: The Third (STEAM) | 91 | 92 | 99% (90d) | Does not open (77%) | 29% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 22 | [ ] | Duskfade (STEAM) | 87 | 89 | 98% (90d) | Does not open (95%) | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 23 | [ ] | Black Mesa (STEAM) | 86 | 119 | 72% (90d) | Does not open (82%) | 12% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 24 | [ ] | Sniper Elite 4 (STEAM) | 83 | 83 | 100% (90d) | Does not open (97%) | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 25 | [ ] | Dead Space 2 (STEAM) | 81 | 102 | 79% (90d) | Does not open (74%) | 36% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 26 | [ ] | HELLDIVERS™ (STEAM) | 81 | 95 | 85% (90d) | Does not open (59%) | 38% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 27 | [ ] | Fall Guys (EPIC) | 81 | 93 | 87% (90d) | Does not open (75%) | 9% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 28 | [ ] | GRID 2 (STEAM) | 78 | 81 | 96% (90d) | Does not open (66%) | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 29 | [ ] | The Wolf Among Us (STEAM) | 74 | 83 | 89% (90d) | Does not open (68%) | 10% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 30 | [ ] | Marvel Rivals (STEAM) | 72 | 80 | 90% (90d) | Does not open (81%) | 0% | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 31 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 71 | 77 | 92% (90d) | Does not open (70%) | 0% | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 32 | [ ] | Burnout™ Paradise Remastered (STEAM) | 71 | 74 | 96% (90d) | Does not open (88%) | 18% | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 33 | [ ] | Call of Duty: Black Ops II - Zombies (STEAM) | 70 | 84 | 83% (90d) | Does not open (70%) | 50% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 34 | [ ] | Saints Row 2 (GOG) | 69 | 82 | 84% (90d) | Does not open (96%) | 52% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 35 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 69 | 74 | 93% (90d) | Does not open (80%) | 8% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 36 | [x] 2026-10-18 | Diablo® IV (STEAM) | 67 | 79 | 85% (90d) | Does not open (61%) | 23% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 37 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 67 | 76 | 88% (90d) | Does not open (47%) | 26% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 38 | [ ] | Door Kickers 2 (STEAM) | 67 | 71 | 94% (90d) | No graphics (85%) | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 39 | [ ] | GRID (STEAM) | 65 | 81 | 80% (90d) | Does not open (55%) | 49% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 40 | [ ] | Borderlands GOTY (STEAM) | 65 | 70 | 93% (90d) | Does not open (95%) | 27% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 41 | [ ] | Metro 2033 (STEAM) | 64 | 80 | 80% (90d) | Does not open (64%) | 47% | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 42 | [ ] | XCOM: Enemy Unknown (STEAM) | 64 | 67 | 96% (90d) | Does not open (75%) | 8% | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 43 | [ ] | Need for Speed™ Heat  (STEAM) | 63 | 77 | 82% (90d) | Does not open (78%) | 30% | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 44 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 63 | 63 | 100% (90d) | No graphics (54%) | 8% | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 45 | [ ] | Three Kingdoms : Alias (STEAM) | 62 | 66 | 94% (90d) | No graphics (97%) | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 46 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 61 | 87 | 70% (90d) | Does not open (85%) | 51% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 47 | [ ] | Spore (STEAM) | 59 | 64 | 92% (90d) | Does not open (68%) | n/a | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 48 | [ ] | DOOM (2016) (GOG) | 58 | 64 | 91% (90d) | Does not open (90%) | 45% | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 49 | [ ] | GrandChase (STEAM) | 57 | 60 | 95% (90d) | Does not open (85%) | 13% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 50 | [ ] | Enshrouded (STEAM) | 57 | 58 | 98% (90d) | Does not open (93%) | 18% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 51 | [ ] | Overwatch® (STEAM) | 55 | 57 | 96% (90d) | Does not open (58%) | 14% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 52 | [ ] | Fortune Mill (STEAM) | 55 | 56 | 98% (90d) | Does not open (89%) | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 53 | [ ] | Spec Ops: The Line (STEAM) | 55 | 56 | 98% (90d) | Does not open (55%) | 0% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 54 | [ ] | METAL SLUG 3 (STEAM) | 53 | 61 | 87% (90d) | Does not open (81%) | 18% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 55 | [ ] | STAR WARS Zero Company™ (STEAM) | 53 | 55 | 96% (90d) | Does not open (64%) | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 56 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 52 | 68 | 76% (90d) | Does not open (81%) | 39% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 57 | [ ] | Watch_Dogs (STEAM) | 52 | 67 | 78% (90d) | Does not open (90%) | 20% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 58 | [ ] | Max Payne 3 (STEAM) | 52 | 57 | 91% (90d) | Does not open (93%) | 44% | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 59 | [ ] | South Park The Fractured But Whole (STEAM) | 52 | 52 | 100% (90d) | Does not open (66%) | 15% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 60 | [ ] | Vampire Survivors (EPIC) | 51 | 73 | 70% (90d) | Does not open (63%) | 59% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 61 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 51 | 65 | 78% (90d) | Does not open (90%) | 55% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 62 | [ ] | Split/Second (STEAM) | 51 | 60 | 85% (90d) | Does not open (76%) | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 63 | [ ] | RoboCop: Rogue City (STEAM) | 51 | 55 | 93% (90d) | Does not open (38%) | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 64 | [ ] | Sandustry (STEAM) | 50 | 62 | 81% (90d) | Does not open (73%) | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 65 | [ ] | Hitman: Absolution (STEAM) | 50 | 55 | 91% (90d) | Does not open (84%) | 7% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 66 | [ ] | Trackmania (STEAM) | 49 | 63 | 78% (90d) | Does not open (85%) | 39% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 67 | [ ] | Scott Pilgrim vs The World (STEAM) | 49 | 49 | 100% (90d) | Does not open (83%) | 47% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 68 | [ ] | Asphalt Legends  (STEAM) | 48 | 56 | 86% (90d) | Does not open (80%) | 41% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 69 | [ ] | Watch_Dogs 2 (STEAM) | 48 | 53 | 91% (90d) | Does not open (97%) | 58% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 70 | [ ] | DOOM Eternal (STEAM) | 48 | 50 | 96% (90d) | Does not open (69%) | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 71 | [ ] | tModLoader (STEAM) | 47 | 54 | 87% (90d) | Does not open (86%) | 4% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 72 | [ ] | Aliens vs. Predator (STEAM) | 47 | 52 | 90% (90d) | No graphics (53%) | 25% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 73 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 47 | 49 | 96% (90d) | No graphics (63%) | 19% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 74 | [ ] | Mafia: Definitive Edition (GOG) | 46 | 61 | 75% (90d) | Does not open (86%) | 22% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 75 | [ ] | ARC Raiders (STEAM) | 46 | 51 | 90% (90d) | Does not open (93%) | 0% | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 76 | [ ] | STAR WARS™ Republic Commando (STEAM) | 46 | 48 | 96% (90d) | Does not open (80%) | 47% | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 77 | [ ] | The Survivalists (STEAM) | 46 | 48 | 96% (90d) | Does not open (98%) | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 78 | [ ] | State of Decay 2 (STEAM) | 45 | 63 | 71% (90d) | Does not open (93%) | 0% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 79 | [ ] | Prince of Persia The Lost Crown (STEAM) | 45 | 49 | 92% (90d) | Does not open (94%) | 38% | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 80 | [ ] | Diablo + Hellfire (GOG) | 44 | 50 | 88% (90d) | Does not open (65%) | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 81 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 44 | 47 | 94% (90d) | Does not open (95%) | 50% | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 82 | [ ] | Tales of Berseria (STEAM) | 44 | 45 | 98% (90d) | Does not open (88%) | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 83 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 43 | 44 | 98% (90d) | Does not open (84%) | 46% | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 84 | [ ] | Need for Speed™ Rivals (STEAM) | 42 | 50 | 84% (90d) | Does not open (59%) | 39% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 85 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 42 | 46 | 91% (90d) | Does not open (72%) | 22% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 86 | [ ] | Elite Dangerous (STEAM) | 42 | 45 | 93% (90d) | Does not open (79%) | 50% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 87 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 41 | 42 | 98% (90d) | Does not open (63%) | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 88 | [ ] | Mafia (STEAM) | 38 | 43 | 88% (90d) | Does not open (69%) | 42% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 89 | [ ] | DJMAX RESPECT V (STEAM) | 38 | 42 | 90% (90d) | Does not open (82%) | 30% | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 90 | [ ] | Barotrauma (STEAM) | 38 | 41 | 93% (90d) | Does not open (97%) | 36% | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 91 | [ ] | Marvel's Spider-Man 2 (STEAM) | 38 | 40 | 95% (90d) | Does not open (87%) | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 92 | [ ] | GeoGuessr Steam Edition (STEAM) | 38 | 39 | 97% (90d) | No graphics (62%) | n/a | [#154](https://github.com/GameNative/gamenative-compat/issues/154) |
| 93 | [ ] | L.A. Noire (STEAM) | 37 | 44 | 84% (90d) | Does not open (96%) | 53% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 94 | [ ] | GOALS (STEAM) | 37 | 43 | 86% (90d) | Does not open (84%) | 24% | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 95 | [ ] | ScourgeBringer (STEAM) | 37 | 42 | 88% (90d) | Does not open (69%) | 6% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 96 | [ ] | BIT.TRIP RUNNER (STEAM) | 37 | 39 | 95% (90d) | Does not open (59%) | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 97 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 37 | 39 | 95% (90d) | Does not open (94%) | 27% | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 98 | [ ] | Dragon's Dogma 2 (STEAM) | 37 | 38 | 97% (90d) | Does not open (91%) | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 99 | [ ] | Beat Saber (STEAM) | 36 | 42 | 86% (90d) | Does not open (45%) | 35% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 100 | [ ] | Forza Horizon 6 (STEAM) | 36 | 37 | 97% (90d) | Does not open (62%) | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 101 | [ ] | Utopia Must Fall (STEAM) | 36 | 36 | 100% (90d) | Does not open (83%) | n/a | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 102 | [ ] | CODE VEIN (STEAM) | 35 | 47 | 74% (90d) | Does not open (68%) | 33% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 103 | [ ] | CARRION (GOG) | 35 | 43 | 81% (90d) | Does not open (73%) | 8% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 104 | [ ] | FINAL FANTASY VIII (STEAM) | 35 | 42 | 83% (90d) | Does not open (65%) | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 105 | [ ] | BattleBit Remastered (STEAM) | 35 | 39 | 90% (90d) | Does not open (61%) | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 106 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 35 | 36 | 97% (90d) | No graphics (62%) | 6% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 107 | [ ] | Mafia II (Classic) (GOG) | 34 | 48 | 71% (90d) | Does not open (93%) | 29% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 108 | [ ] | OneShot (STEAM) | 34 | 38 | 89% (90d) | Does not open (97%) | 20% | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 109 | [ ] | Muv-Luv (STEAM) | 34 | 35 | 97% (90d) | Does not open (86%) | 35% | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 110 | [ ] | Metro: Last Light Redux (STEAM) | 33 | 91 | 75% (1.3.0) | Does not open (91%) | 44% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 111 | [ ] | Beholder (EPIC) | 33 | 40 | 83% (90d) | Does not open (65%) | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 112 | [ ] | Mass Effect (2007) (STEAM) | 33 | 39 | 85% (90d) | Does not open (81%) | 50% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 113 | [ ] | Death Stranding (EPIC) | 33 | 36 | 92% (90d) | Does not open (75%) | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 114 | [ ] | To The Moon (GOG) | 33 | 35 | 100% (1.3.0) | Does not open (88%) | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 115 | [ ] | The Darkness II (STEAM) | 33 | 33 | 100% (90d) | Does not open (83%) | 30% | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 116 | [ ] | Yume Nikki (STEAM) | 32 | 54 | 73% (14d) | Does not open (94%) | 0% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 117 | [ ] | Gauntlet™  (STEAM) | 32 | 46 | 70% (90d) | Does not open (67%) | 42% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 118 | [ ] | CPM 2 (STEAM) | 32 | 40 | 80% (90d) | Does not open (91%) | 10% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 119 | [ ] | Lost Planet: Extreme Condition (STEAM) | 32 | 40 | 80% (90d) | Does not open (80%) | 56% | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 120 | [ ] | Insaniquarium! Deluxe (STEAM) | 32 | 39 | 82% (90d) | Does not open (86%) | 32% | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 121 | [ ] | Wolfenstein 3D (STEAM) | 32 | 35 | 91% (90d) | Does not open (50%) | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 122 | [ ] | Quantum Break (STEAM) | 32 | 32 | 100% (90d) | Does not open (91%) | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 123 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 31 | 34 | 91% (90d) | Does not open (67%) | 0% | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 124 | [ ] | Forza Horizon 5 (STEAM) | 31 | 33 | 94% (90d) | Does not open (67%) | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 125 | [ ] | Umamusume: Pretty Derby (STEAM) | 31 | 33 | 94% (90d) | Does not open (86%) | n/a | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 126 | [ ] | Rayman Legends (STEAM) | 31 | 32 | 97% (90d) | Does not open (96%) | 44% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 127 | [ ] | Metro: Last Light Complete Edition (STEAM) | 30 | 37 | 81% (90d) | Does not open (58%) | 57% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 128 | [ ] | Far Cry 4 (STEAM) | 30 | 34 | 88% (90d) | Does not open (100%) | 30% | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 129 | [ ] | King's Bounty: The Legend (STEAM) | 30 | 34 | 88% (90d) | Does not open (100%) | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 130 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 30 | 33 | 91% (90d) | Does not open (81%) | 27% | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 131 | [ ] | Magicka (STEAM) | 30 | 33 | 91% (90d) | Does not open (64%) | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 132 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 30 | 32 | 94% (90d) | Does not open (75%) | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 133 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 30 | 31 | 97% (90d) | Does not open (95%) | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 134 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 30 | 30 | 100% (90d) | Does not open (72%) | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 135 | [ ] | Grand Theft Auto III - The Definitive Edition (STEAM) | 30 | 30 | 100% (90d) | Does not open (92%) | 16% | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 136 | [ ] | Dark Sector (STEAM) | 29 | 38 | 76% (90d) | Does not open (68%) | 39% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 137 | [ ] | Borderlands 2 RU (STEAM) | 29 | 31 | 94% (90d) | Does not open (60%) | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 138 | [ ] | Audiosurf (STEAM) | 28 | 39 | 72% (90d) | Does not open (46%) | 50% | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 139 | [ ] | Hitman: Blood Money (STEAM) | 28 | 29 | 97% (90d) | Does not open (84%) | 12% | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 140 | [ ] | Breath of Fire IV (STEAM) | 28 | 28 | 100% (90d) | Does not open (56%) | 15% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 141 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 28 | 28 | 100% (90d) | Does not open (68%) | 0% | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 142 | [ ] | Mirror's Edge™ (GOG) | 27 | 38 | 71% (90d) | No graphics (62%) | 43% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 143 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 27 | 37 | 73% (90d) | Does not open (67%) | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 144 | [ ] | The Planet Crafter (STEAM) | 27 | 32 | 84% (90d) | Does not open (55%) | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 145 | [ ] | Alpha Protocol (STEAM) | 27 | 31 | 87% (90d) | Does not open (58%) | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 146 | [ ] | PAYDAY 2 (STEAM) | 27 | 30 | 90% (90d) | Does not open (78%) | 31% | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 147 | [ ] | WRC 7 (STEAM) | 27 | 28 | 96% (90d) | Does not open (72%) | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 148 | [ ] | Zuma Deluxe (STEAM) | 27 | 28 | 96% (90d) | Does not open (95%) | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 149 | [ ] | Kenshi (STEAM) | 26 | 33 | 79% (90d) | Does not open (80%) | 11% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 150 | [ ] | Subnautica 2 (STEAM) | 26 | 32 | 81% (90d) | Does not open (65%) | 50% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 151 | [ ] | Singularity™ (GOG) | 26 | 31 | 84% (90d) | Does not open (100%) | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 152 | [ ] | Northgard: Definitive Edition (STEAM) | 26 | 29 | 90% (90d) | Does not open (96%) | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 153 | [ ] | Persona 5 Strikers (STEAM) | 26 | 29 | 90% (90d) | Does not open (78%) | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 154 | [ ] | Turing Complete (STEAM) | 26 | 29 | 90% (90d) | Does not open (91%) | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 155 | [ ] | AION 2 (STEAM) | 26 | 28 | 93% (90d) | Does not open (65%) | 8% | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 156 | [ ] | Axiom Verge 2 (STEAM) | 26 | 27 | 96% (90d) | Does not open (77%) | 12% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 157 | [ ] | DiRT Showdown (STEAM) | 26 | 27 | 96% (90d) | Does not open (54%) | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 158 | [ ] | Isle of Reveries (STEAM) | 26 | 27 | 96% (90d) | Does not open (95%) | 21% | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 159 | [ ] | EA SPORTS FC™ 26 (STEAM) | 25 | 33 | 76% (90d) | Does not open (75%) | n/a | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 160 | [ ] | Knights of Pen and Paper 2 (STEAM) | 25 | 32 | 78% (90d) | Does not open (45%) | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 161 | [ ] | Dragon Age™ Inquisition (STEAM) | 25 | 29 | 86% (90d) | Does not open (76%) | 33% | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 162 | [ ] | Bionic Commando Rearmed (STEAM) | 25 | 28 | 89% (90d) | Does not open (74%) | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 163 | [ ] | Alien Breed: Impact (STEAM) | 25 | 27 | 93% (90d) | Does not open (83%) | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 164 | [ ] | Bingle Bingle (STEAM) | 25 | 26 | 96% (90d) | Does not open (80%) | n/a | [#225](https://github.com/GameNative/gamenative-compat/issues/225) |
| 165 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 25 | 26 | 96% (90d) | Does not open (81%) | 42% | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 166 | [ ] | Resident Evil Requiem (STEAM) | 25 | 25 | 100% (90d) | Does not open (75%) | n/a | [#210](https://github.com/GameNative/gamenative-compat/issues/210) |
| 167 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 25 | 25 | 100% (90d) | Does not open (56%) | 10% | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 168 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 24 | 34 | 71% (90d) | Does not open (95%) | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 169 | [ ] | Call of Duty® (STEAM) | 24 | 33 | 73% (90d) | Does not open (67%) | 5% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 170 | [ ] | Content Warning (STEAM) | 24 | 31 | 77% (90d) | Does not open (57%) | n/a | [#241](https://github.com/GameNative/gamenative-compat/issues/241) |
| 171 | [ ] | My Singing Monsters (STEAM) | 24 | 30 | 80% (90d) | Does not open (83%) | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 172 | [ ] | ENDLESS Space™ 2 (STEAM) | 24 | 29 | 83% (90d) | Does not open (93%) | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 173 | [ ] | The Swapper (STEAM) | 24 | 28 | 86% (90d) | Does not open (52%) | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 174 | [ ] | Peggle Nights (STEAM) | 24 | 26 | 92% (90d) | Does not open (94%) | 30% | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 175 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 24 | 25 | 96% (90d) | No graphics (53%) | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 176 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 23 | 32 | 72% (90d) | No graphics (57%) | 13% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 177 | [ ] | Transformers: Fall of Cybertron (STEAM) | 23 | 30 | 77% (90d) | Does not open (63%) | 30% | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 178 | [ ] | SimCity 4 Deluxe (STEAM) | 23 | 27 | 85% (90d) | Does not open (82%) | 45% | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 179 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 23 | 26 | 88% (90d) | Does not open (95%) | 55% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 180 | [ ] | They Are Billions (STEAM) | 23 | 26 | 88% (90d) | Does not open (70%) | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 181 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 23 | 25 | 92% (90d) | Does not open (63%) | 50% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 182 | [ ] | PRAGMATA (STEAM) | 23 | 24 | 96% (90d) | Does not open (79%) | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 183 | [ ] | The Lantern of the Laughless Saint (STEAM) | 23 | 24 | 96% (90d) | Does not open (80%) | n/a | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 184 | [ ] | Euro Truck Simulator (STEAM) | 23 | 23 | 100% (90d) | Does not open (93%) | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 185 | [ ] | Gears 5 (STEAM) | 23 | 23 | 100% (90d) | Does not open (88%) | n/a | [#264](https://github.com/GameNative/gamenative-compat/issues/264) |
| 186 | [ ] | Marie's Adventure (STEAM) | 23 | 23 | 100% (90d) | Does not open (100%) | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 187 | [ ] | Spiral Knights (STEAM) | 23 | 23 | 100% (90d) | Does not open (72%) | n/a | [#263](https://github.com/GameNative/gamenative-compat/issues/263) |
| 188 | [ ] | CarX Street (STEAM) | 22 | 29 | 76% (90d) | Does not open (77%) | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 189 | [ ] | Half-Life: Blue Shift (STEAM) | 22 | 26 | 85% (90d) | Does not open (85%) | 20% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 190 | [ ] | Tom Clancy's Ghost Recon® Wildlands (STEAM) | 22 | 26 | 85% (90d) | Does not open (94%) | n/a | [#280](https://github.com/GameNative/gamenative-compat/issues/280) |
| 191 | [ ] | skate.™ (EPIC) | 22 | 25 | 88% (90d) | Does not open (88%) | 8% | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 192 | [ ] | Melatonin (STEAM) | 22 | 23 | 96% (90d) | Does not open (58%) | 46% | [#272](https://github.com/GameNative/gamenative-compat/issues/272) |
| 193 | [ ] | Wallachia: Reign of Dracula (STEAM) | 22 | 23 | 96% (90d) | No graphics (95%) | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 194 | [ ] | Beat Cop (STEAM) | 21 | 29 | 72% (90d) | Does not open (75%) | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 195 | [ ] | SOMA (STEAM) | 21 | 28 | 75% (90d) | Does not open (78%) | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 196 | [ ] | TEKKEN 8 (STEAM) | 21 | 28 | 75% (90d) | Does not open (76%) | 50% | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 197 | [ ] | Aggelos 2 (STEAM) | 21 | 27 | 78% (90d) | No graphics (90%) | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 198 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 21 | 27 | 78% (90d) | Does not open (62%) | n/a | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 199 | [ ] | Beyond Good & Evil™ (GOG) | 21 | 26 | 81% (90d) | Does not open (100%) | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 200 | [ ] | Sapphire Safari (GOG) | 21 | 26 | 81% (90d) | Does not open (89%) | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 201 | [ ] | PICO PARK:Classic Edition (STEAM) | 21 | 25 | 84% (90d) | Does not open (90%) | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 202 | [ ] | Marvel's Midnight Suns (STEAM) | 21 | 24 | 88% (90d) | Does not open (84%) | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 203 | [ ] | Apex Legends (STEAM) | 21 | 23 | 91% (90d) | Does not open (74%) | n/a | [#261](https://github.com/GameNative/gamenative-compat/issues/261) |
| 204 | [ ] | Wuthering Waves (STEAM) | 21 | 23 | 91% (90d) | Does not open (85%) | n/a | [#216](https://github.com/GameNative/gamenative-compat/issues/216) |
| 205 | [ ] | Pathway (EPIC) | 21 | 22 | 95% (90d) | Does not open (63%) | n/a | [#298](https://github.com/GameNative/gamenative-compat/issues/298) |
| 206 | [ ] | Resident Evil 3 Nemesis (1999) (STEAM) | 21 | 21 | 100% (90d) | Does not open (86%) | n/a | [#273](https://github.com/GameNative/gamenative-compat/issues/273) |
| 207 | [ ] | Return to Castle Wolfenstein (STEAM) | 21 | 21 | 100% (90d) | Does not open (95%) | 18% | [#321](https://github.com/GameNative/gamenative-compat/issues/321) |
| 208 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 21 | 21 | 100% (90d) | Does not open (71%) | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 209 | [ ] | Fishing Planet (STEAM) | 20 | 28 | 71% (90d) | Does not open (93%) | 33% | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 210 | [ ] | Surviving Mars (STEAM) | 20 | 26 | 77% (90d) | Does not open (92%) | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 211 | [ ] | Halo: Spartan Assault (STEAM) | 20 | 23 | 87% (90d) | Does not open (82%) | 38% | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 212 | [ ] | Mirror's Edge™ Catalyst (STEAM) | 20 | 21 | 95% (90d) | Does not open (67%) | 56% | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 213 | [ ] | No More Room in Hell (STEAM) | 20 | 21 | 95% (90d) | Does not open (94%) | n/a | [#365](https://github.com/GameNative/gamenative-compat/issues/365) |
| 214 | [ ] | Rayman Legends (EPIC) | 20 | 21 | 95% (90d) | Does not open (92%) | n/a | [#286](https://github.com/GameNative/gamenative-compat/issues/286) |
| 215 | [ ] | The Last of Us™ Part I (STEAM) | 20 | 21 | 95% (90d) | Does not open (93%) | n/a | [#300](https://github.com/GameNative/gamenative-compat/issues/300) |
| 216 | [ ] | DiRT 2 (STEAM) | 20 | 20 | 100% (90d) | Does not open (85%) | n/a | [#471](https://github.com/GameNative/gamenative-compat/issues/471) |
| 217 | [ ] | Grounded 2 (STEAM) | 20 | 20 | 100% (90d) | Does not open (56%) | n/a | [#317](https://github.com/GameNative/gamenative-compat/issues/317) |
| 218 | [ ] | Dungeon Keeper™ 2 (GOG) | 19 | 26 | 73% (90d) | Does not open (100%) | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 219 | [ ] | Fogpiercer (STEAM) | 19 | 26 | 73% (90d) | Does not open (79%) | n/a | [#303](https://github.com/GameNative/gamenative-compat/issues/303) |
| 220 | [ ] | Yuppie Psycho (STEAM) | 19 | 26 | 73% (90d) | Does not open (75%) | n/a | [#325](https://github.com/GameNative/gamenative-compat/issues/325) |
| 221 | [ ] | Mafia III: Definitive Edition (STEAM) | 19 | 22 | 86% (90d) | Does not open (95%) | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 222 | [ ] | The Elder Scrolls IV: Oblivion Remastered (STEAM) | 19 | 22 | 86% (90d) | Does not open (59%) | n/a | [#312](https://github.com/GameNative/gamenative-compat/issues/312) |
| 223 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 19 | 22 | 86% (90d) | Does not open (79%) | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 224 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 21 | 90% (90d) | Does not open (82%) | 0% | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 225 | [ ] | Gothic 1 Remake (STEAM) | 19 | 21 | 90% (90d) | Directx error (44%) | n/a | [#336](https://github.com/GameNative/gamenative-compat/issues/336) |
| 226 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 21 | 90% (90d) | Does not open (89%) | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 227 | [ ] | GT Legends (STEAM) | 19 | 20 | 95% (90d) | Does not open (89%) | n/a | [#364](https://github.com/GameNative/gamenative-compat/issues/364) |
| 228 | [ ] | Jurassic World Evolution (EPIC) | 19 | 20 | 95% (90d) | Does not open (80%) | n/a | [#469](https://github.com/GameNative/gamenative-compat/issues/469) |
| 229 | [ ] | Zenless Zone Zero (STEAM) | 19 | 20 | 95% (90d) | Does not open (76%) | n/a | [#369](https://github.com/GameNative/gamenative-compat/issues/369) |
| 230 | [ ] | We Were Here Together (EPIC) | 18 | 24 | 75% (90d) | Does not open (82%) | n/a | [#374](https://github.com/GameNative/gamenative-compat/issues/374) |
| 231 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 18 | 23 | 78% (90d) | Does not open (100%) | 35% | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 232 | [ ] | Yakuza 0 (GOG) | 18 | 23 | 78% (90d) | Does not open (67%) | 50% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 233 | [ ] | EVE Online (STEAM) | 18 | 22 | 82% (90d) | Does not open (50%) | 55% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 234 | [ ] | Sid Meier's Pirates! (STEAM) | 18 | 22 | 82% (90d) | Does not open (92%) | n/a | [#293](https://github.com/GameNative/gamenative-compat/issues/293) |
| 235 | [ ] | Sir, We Have an Orc Problem (STEAM) | 18 | 22 | 82% (90d) | Does not open (58%) | n/a | [#145](https://github.com/GameNative/gamenative-compat/issues/145) |
| 236 | [ ] | Bright Memory (STEAM) | 18 | 21 | 86% (90d) | No graphics (83%) | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 237 | [ ] | Tyrian 2000 (GOG) | 18 | 21 | 86% (90d) | Does not open (87%) | n/a | [#360](https://github.com/GameNative/gamenative-compat/issues/360) |
| 238 | [ ] | Assassin's Creed Rogue (STEAM) | 18 | 20 | 90% (90d) | Does not open (60%) | 40% | [#271](https://github.com/GameNative/gamenative-compat/issues/271) |
| 239 | [ ] | Duke Nukem 3D: Megaton Edition (STEAM) | 18 | 20 | 90% (90d) | Does not open (83%) | n/a | [#476](https://github.com/GameNative/gamenative-compat/issues/476) |
| 240 | [ ] | Lay of the Land (STEAM) | 18 | 20 | 90% (90d) | No graphics (61%) | n/a | [#477](https://github.com/GameNative/gamenative-compat/issues/477) |
| 241 | [ ] | Carnal Instinct (STEAM) | 17 | 24 | 71% (90d) | Does not open (57%) | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 242 | [ ] | SlashZero Demo (STEAM) | 17 | 23 | 74% (90d) | Does not open (75%) | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 243 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 17 | 22 | 77% (90d) | Does not open (87%) | 50% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 244 | [ ] | Dorfromantik (GOG) | 17 | 21 | 81% (90d) | Does not open (100%) | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 245 | [ ] | Clive Barker's Undying (GOG) | 17 | 20 | 85% (90d) | Does not open (75%) | n/a | [#388](https://github.com/GameNative/gamenative-compat/issues/388) |
| 246 | [ ] | GRADIUS origin collection (STEAM) | 17 | 20 | 85% (90d) | Controller issues (71%) | n/a | [#479](https://github.com/GameNative/gamenative-compat/issues/479) |
| 247 | [ ] | NBA 2K26 (STEAM) | 17 | 20 | 85% (90d) | Does not open (82%) | n/a | [#384](https://github.com/GameNative/gamenative-compat/issues/384) |
| 248 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (90d) | Does not open (82%) | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 249 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 16 | 23 | 70% (90d) | No graphics (56%) | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 250 | [ ] | Legend of Grimrock 2 (STEAM) | 16 | 23 | 70% (90d) | Does not open (92%) | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 251 | [ ] | Hitman 3: Contracts (GOG) | 16 | 22 | 73% (90d) | Does not open (93%) | n/a | [#401](https://github.com/GameNative/gamenative-compat/issues/401) |
| 252 | [ ] | Re-Volt (STEAM) | 16 | 22 | 73% (90d) | Controller issues (71%) | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 253 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 21 | 76% (90d) | Does not open (82%) | 41% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 254 | [ ] | Hitman 2: Silent Assassin (STEAM) | 16 | 21 | 76% (90d) | Does not open (82%) | 53% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 255 | [ ] | Bejeweled 2 Deluxe (STEAM) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#329](https://github.com/GameNative/gamenative-compat/issues/329) |
| 256 | [ ] | F.E.A.R. 2: Project Origin + Reborn (GOG) | 16 | 20 | 80% (90d) | Does not open (100%) | n/a | [#478](https://github.com/GameNative/gamenative-compat/issues/478) |
| 257 | [ ] | Genshin Impact (EPIC) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#326](https://github.com/GameNative/gamenative-compat/issues/326) |
| 258 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 16 | 20 | 80% (90d) | No graphics (67%) | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 259 | [ ] | Sacred Gold (STEAM) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 260 | [ ] | shapez (STEAM) | 16 | 20 | 80% (90d) | No graphics (67%) | n/a | [#332](https://github.com/GameNative/gamenative-compat/issues/332) |
| 261 | [ ] | DayZ (STEAM) | 15 | 21 | 71% (90d) | Does not open (56%) | 58% | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 262 | [ ] | Fallout Classic (GOG) | 15 | 21 | 71% (90d) | Does not open (71%) | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 263 | [ ] | Smushi Come Home (GOG) | 15 | 21 | 71% (90d) | Does not open (57%) | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 264 | [ ] | Space Rangers HD: A War Apart (STEAM) | 15 | 21 | 71% (90d) | Does not open (64%) | 46% | [#472](https://github.com/GameNative/gamenative-compat/issues/472) |
| 265 | [ ] | Spark the Electric Jester (STEAM) | 15 | 20 | 75% (90d) | Does not open (62%) | 50% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 266 | [ ] | Sword Art Online: Hollow Realization Deluxe Edition (STEAM) | 14 | 20 | 70% (90d) | Controller issues (92%) | n/a | [#470](https://github.com/GameNative/gamenative-compat/issues/470) |

## Probably does not work (78)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | Garry's Mod (STEAM) | 198 | 322 | 65% (1.3.0) | Does not open (79%) | 57% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 2 | [ ] | Metro 2033 Redux (STEAM) | 153 | 352 | 65% (1.3.0) | Does not open (69%) | 52% |  |
| 3 | [ ] | Prototype (STEAM) | 151 | 215 | 50% (1.3.0) | Does not open (75%) | 46% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 4 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 143 | 217 | 66% (90d) | Does not open (80%) | n/a |  |
| 5 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 139 | 173 | 52% (1.3.0) | Does not open (93%) | 41% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 6 | [ ] | Geometry Dash (STEAM) | 137 | 414 | 66% (1.3.0) | Does not open (68%) | 40% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 7 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 101 | 134 | 67% (1.3.0) | Does not open (75%) | 39% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 8 | [ ] | VRChat (STEAM) | 92 | 138 | 55% (1.3.0) | Does not open (65%) | 41% |  |
| 9 | [ ] | MECCHA CHAMELEON (STEAM) | 74 | 107 | 69% (90d) | Does not open (63%) | 59% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 10 | [ ] | Hollow Knight: Silksong (GOG) | 70 | 109 | 64% (90d) | Does not open (66%) | 49% |  |
| 11 | [ ] | Gorilla Tag (STEAM) | 67 | 115 | 58% (90d) | Does not open (75%) | 21% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 12 | [ ] | Firewatch (STEAM) | 66 | 113 | 58% (90d) | Does not open (89%) | 56% |  |
| 13 | [ ] | Oxygen Not Included (STEAM) | 54 | 87 | 62% (90d) | Does not open (76%) | 50% |  |
| 14 | [ ] | Breathedge (STEAM) | 51 | 75 | 68% (90d) | Does not open (61%) | 36% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 15 | [ ] | Frostpunk (STEAM) | 46 | 74 | 62% (90d) | No graphics (79%) | 48% |  |
| 16 | [ ] | VALORANT (EPIC) | 46 | 72 | 64% (90d) | Does not open (87%) | 18% |  |
| 17 | [ ] | Plague Inc: Evolved (STEAM) | 45 | 67 | 67% (90d) | Does not open (65%) | 56% |  |
| 18 | [ ] | Age of Empires II (2013) (STEAM) | 40 | 69 | 58% (90d) | Does not open (48%) | 52% |  |
| 19 | [ ] | Fallout (GOG) | 40 | 61 | 66% (90d) | Does not open (72%) | 48% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 20 | [ ] | Grim Dawn (GOG) | 38 | 63 | 60% (90d) | Does not open (65%) | 46% | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 21 | [ ] | XCOM 2 (STEAM) | 35 | 54 | 65% (90d) | Does not open (57%) | n/a |  |
| 22 | [ ] | Deponia (STEAM) | 34 | 63 | 54% (90d) | Does not open (50%) | 57% |  |
| 23 | [ ] | Sol Cesto (STEAM) | 33 | 51 | 65% (90d) | Does not open (70%) | 56% |  |
| 24 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 32 | 57 | 56% (90d) | Does not open (95%) | 45% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 25 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 31 | 59 | 53% (90d) | Does not open (66%) | 46% |  |
| 26 | [ ] | Soul's Remnant (STEAM) | 27 | 49 | 55% (90d) | Does not open (55%) | n/a |  |
| 27 | [ ] | Lucid Blocks (STEAM) | 27 | 46 | 59% (90d) | Does not open (83%) | 50% |  |
| 28 | [ ] | Crazy Taxi (STEAM) | 25 | 42 | 60% (90d) | Does not open (63%) | 55% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 29 | [ ] | Strider (STEAM) | 24 | 37 | 65% (90d) | Does not open (100%) | 35% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 30 | [ ] | Invisible, Inc. (STEAM) | 23 | 40 | 58% (90d) | Does not open (67%) | 58% |  |
| 31 | [ ] | Styx: Master of Shadows (EPIC) | 22 | 43 | 51% (90d) | Does not open (55%) | 33% |  |
| 32 | [ ] | Cities: Skylines (STEAM) | 22 | 32 | 69% (90d) | Does not open (67%) | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 33 | [ ] | Overlord (STEAM) | 21 | 40 | 53% (90d) | Does not open (71%) | 59% |  |
| 34 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 21 | 33 | 64% (90d) | Does not open (81%) | n/a |  |
| 35 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 20 | 36 | 56% (90d) | Does not open (58%) | 44% |  |
| 36 | [ ] | Need for Speed: Undercover (STEAM) | 20 | 31 | 65% (90d) | Does not open (94%) | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 37 | [ ] | Warhammer 40,000: Boltgun (GOG) | 20 | 31 | 65% (90d) | Does not open (93%) | 44% |  |
| 38 | [ ] | No More Heroes (STEAM) | 19 | 36 | 53% (90d) | No graphics (67%) | n/a |  |
| 39 | [ ] | Another World: 20th Anniversary Edition (GOG) | 19 | 29 | 66% (90d) | Does not open (69%) | n/a |  |
| 40 | [ ] | Turnip Boy Robs a Bank (EPIC) | 19 | 28 | 68% (90d) | Does not open (65%) | 41% | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 41 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 17 | 30 | 57% (90d) | Does not open (88%) | 27% |  |
| 42 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 17 | 27 | 63% (90d) | Does not open (80%) | n/a |  |
| 43 | [ ] | War of Dots (STEAM) | 17 | 27 | 63% (90d) | Does not open (75%) | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 44 | [ ] | Grim Fandango Remastered (GOG) | 17 | 25 | 68% (90d) | No graphics (78%) | n/a | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 45 | [ ] | Race The Sun (STEAM) | 16 | 31 | 52% (90d) | No graphics (92%) | 57% |  |
| 46 | [ ] | Alan Wake's American Nightmare (EPIC) | 16 | 27 | 59% (90d) | Does not open (87%) | 47% |  |
| 47 | [ ] | Guacamelee! Gold Edition (STEAM) | 16 | 27 | 59% (90d) | Does not open (93%) | n/a | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 48 | [ ] | Assassin's Creed Odyssey (STEAM) | 16 | 25 | 64% (90d) | Does not open (75%) | n/a | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 49 | [ ] | Odallus: The Dark Call (STEAM) | 15 | 27 | 56% (90d) | No graphics (57%) | n/a | [#337](https://github.com/GameNative/gamenative-compat/issues/337) |
| 50 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 15 | 26 | 58% (90d) | Does not open (85%) | 50% |  |
| 51 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 15 | 26 | 58% (90d) | Does not open (64%) | 0% |  |
| 52 | [ ] | Ys: Memories of Celceta (STEAM) | 15 | 24 | 63% (90d) | No graphics (45%) | 33% |  |
| 53 | [ ] | Blood Omen: Legacy of Kain (GOG) | 15 | 23 | 65% (90d) | Does not open (64%) | 45% |  |
| 54 | [ ] | Make Way (EPIC) | 15 | 22 | 68% (90d) | Does not open (79%) | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 55 | [ ] | Aperture Desk Job (STEAM) | 14 | 28 | 50% (90d) | Does not open (67%) | n/a |  |
| 56 | [ ] | Evoland (STEAM) | 14 | 28 | 50% (90d) | Controller issues (69%) | n/a |  |
| 57 | [ ] | Far Cry® (GOG) | 14 | 27 | 52% (90d) | Does not open (31%) | n/a |  |
| 58 | [ ] | Blaster Master Zero (STEAM) | 14 | 25 | 56% (90d) | Does not open (64%) | 42% |  |
| 59 | [ ] | Katana ZERO (GOG) | 14 | 25 | 56% (90d) | Does not open (85%) | 33% |  |
| 60 | [ ] | Gargoyles Remastered (AMAZON) | 14 | 23 | 61% (90d) | Directx error (67%) | n/a |  |
| 61 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 21 | 67% (90d) | Does not open (67%) | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 62 | [ ] | A Plague Tale: Innocence (GOG) | 13 | 24 | 54% (90d) | Does not open (92%) | 50% |  |
| 63 | [ ] | Asterigos: Curse of the Stars (STEAM) | 13 | 23 | 57% (90d) | Graphics glitches (50%) | n/a |  |
| 64 | [ ] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 13 | 23 | 57% (90d) | Does not open (100%) | 12% |  |
| 65 | [ ] | The Stanley Parable (STEAM) | 13 | 23 | 57% (90d) | Does not open (89%) | 50% |  |
| 66 | [ ] | Trials Survivors (STEAM) | 13 | 23 | 57% (90d) | Does not open (67%) | n/a |  |
| 67 | [ ] | Evenicle (STEAM) | 13 | 22 | 59% (90d) | Graphics glitches (77%) | n/a |  |
| 68 | [ ] | Drop Duchy (EPIC) | 13 | 21 | 62% (90d) | Does not open (100%) | 18% |  |
| 69 | [ ] | Buck Up And Drive! (STEAM) | 13 | 20 | 65% (90d) | Does not open (67%) | n/a |  |
| 70 | [ ] | Revolution Idle (STEAM) | 12 | 24 | 50% (90d) | No graphics (50%) | n/a |  |
| 71 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 12 | 22 | 55% (90d) | Does not open (73%) | n/a |  |
| 72 | [ ] | The Excavation of Hob's Barrow (STEAM) | 12 | 22 | 55% (90d) | Controller issues (82%) | n/a |  |
| 73 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (90d) | Does not open (82%) | n/a |  |
| 74 | [ ] | Crying Suns (EPIC) | 11 | 22 | 50% (90d) | No graphics (57%) | n/a |  |
| 75 | [ ] | Quake III Arena (STEAM) | 11 | 22 | 50% (90d) | Does not open (78%) | 8% |  |
| 76 | [ ] | Deathsmiles (STEAM) | 11 | 20 | 55% (90d) | Does not open (67%) | 38% |  |
| 77 | [ ] | DYNASTY WARRIORS: ORIGINS (STEAM) | 10 | 20 | 50% (90d) | Does not open (60%) | n/a |  |
| 78 | [ ] | F1 2015 (STEAM) | 10 | 20 | 50% (90d) | Does not open (50%) | n/a |  |

## Works, but the first launch usually fails (367)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 1324 | 1676 | 76% (1.3.0) | Does not open (83%) | 77% |  |
| 2 | [ ] | Grim Dawn (STEAM) | 570 | 618 | 68% (1.3.0) | Does not open (74%) | 63% |  |
| 3 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 567 | 723 | 76% (1.3.0) | Does not open (63%) | 92% |  |
| 4 | [ ] | Terraria (STEAM) | 488 | 763 | 62% (1.3.0) | No graphics (51%) | 75% |  |
| 5 | [ ] | KINGDOM HEARTS -HD 1.5+2.5 ReMIX- (STEAM) | 474 | 946 | 56% (1.3.0) | Does not open (79%) | 94% |  |
| 6 | [ ] | No Man's Sky (STEAM) | 369 | 649 | 53% (1.3.0) | Controller issues (61%) | 85% |  |
| 7 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 365 | 550 | 67% (1.3.0) | Does not open (55%) | 84% |  |
| 8 | [ ] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 259 | 300 | 86% (90d) | Does not open (87%) | 66% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 9 | [ ] | Cyberpunk 2077 (STEAM) | 245 | 424 | 54% (1.3.0) | Does not open (68%) | 77% |  |
| 10 | [ ] | Welcome to Elderfield (STEAM) | 235 | 280 | 62% (1.3.0) | Does not open (72%) | 75% |  |
| 11 | [ ] | Grand Theft Auto V Legacy (STEAM) | 226 | 286 | 69% (1.3.0) | Does not open (89%) | 80% |  |
| 12 | [ ] | BeamNG.drive (STEAM) | 226 | 276 | 88% (1.3.0) | Does not open (84%) | 92% |  |
| 13 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 225 | 317 | 71% (90d) | Does not open (61%) | 88% |  |
| 14 | [ ] | Palworld (STEAM) | 214 | 414 | 55% (1.3.0) | Does not open (72%) | 87% |  |
| 15 | [ ] | DRAGON BALL FighterZ (STEAM) | 208 | 238 | 71% (1.3.0) | Does not open (89%) | 60% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 16 | [ ] | OMORI (STEAM) | 207 | 250 | 83% (90d) | Does not open (64%) | 78% |  |
| 17 | [ ] | Devil May Cry HD Collection (STEAM) | 200 | 282 | 75% (1.3.0) | Does not open (86%) | 76% |  |
| 18 | [ ] | ELDEN RING (STEAM) | 198 | 294 | 69% (1.3.0) | Does not open (86%) | 71% |  |
| 19 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 192 | 361 | 61% (1.3.0) | Does not open (57%) | 81% |  |
| 20 | [ ] | DREDGE (EPIC) | 172 | 219 | 61% (1.3.0) | Does not open (68%) | 89% |  |
| 21 | [ ] | Noita (STEAM) | 146 | 222 | 53% (1.3.0) | Does not open (55%) | 78% |  |
| 22 | [ ] | Team Fortress 2 (STEAM) | 145 | 234 | 71% (1.3.0) | Does not open (68%) | 79% |  |
| 23 | [ ] | Resident Evil 3 (STEAM) | 143 | 239 | 50% (1.3.0) | Does not open (78%) | 83% |  |
| 24 | [ ] | Borderlands 2 (EPIC) | 139 | 166 | 79% (1.3.0) | Does not open (82%) | 64% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 25 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 139 | 158 | 90% (1.3.0) | Does not open (86%) | 78% |  |
| 26 | [ ] | Far Cry® 3 (STEAM) | 132 | 148 | 89% (90d) | Does not open (82%) | 65% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 27 | [ ] | Castlevania Advance Collection (STEAM) | 130 | 200 | 70% (1.3.0) | Controller issues (94%) | 97% |  |
| 28 | [ ] | Minecraft Dungeons II (STEAM) | 123 | 141 | 87% (90d) | Does not open (83%) | 66% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 29 | [ ] | Castlevania Dominus Collection (STEAM) | 122 | 179 | 76% (1.3.0) | Controller issues (92%) | 98% |  |
| 30 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 120 | 149 | 70% (1.3.0) | Does not open (71%) | 63% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 31 | [ ] | Cave Story+ (STEAM) | 120 | 132 | 91% (90d) | Does not open (65%) | 96% |  |
| 32 | [ ] | Touhou Koumakyou: New Classic - the Embodiment of Scarlet Devil (STEAM) | 117 | 180 | 65% (90d) | Does not open (78%) | 81% |  |
| 33 | [ ] | Fallout: New Vegas (EPIC) | 117 | 143 | 75% (1.3.0) | Does not open (59%) | 90% |  |
| 34 | [ ] | Caravan SandWitch (EPIC) | 116 | 179 | 65% (90d) | Does not open (92%) | 81% |  |
| 35 | [ ] | Devil May Cry 5 (STEAM) | 115 | 183 | 65% (1.3.0) | Does not open (80%) | 67% |  |
| 36 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 114 | 159 | 81% (1.3.0) | Does not open (75%) | 63% |  |
| 37 | [ ] | The Witcher: Enhanced Edition (STEAM) | 114 | 130 | 88% (90d) | Does not open (60%) | 63% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 38 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 111 | 147 | 76% (90d) | Does not open (86%) | 84% |  |
| 39 | [ ] | Aniimo (STEAM) | 104 | 142 | 73% (90d) | Does not open (77%) | 92% |  |
| 40 | [ ] | Moonstone Island (STEAM) | 103 | 136 | 76% (90d) | Controller issues (57%) | 89% |  |
| 41 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 97 | 144 | 60% (1.3.0) | Does not open (77%) | 76% |  |
| 42 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 97 | 128 | 76% (90d) | Controller issues (86%) | 98% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 43 | [ ] | Happy Wheels (STEAM) | 94 | 114 | 82% (90d) | No graphics (54%) | 79% |  |
| 44 | [ ] | Fallout: New Vegas PCR (STEAM) | 92 | 123 | 75% (90d) | Does not open (89%) | 69% |  |
| 45 | [ ] | Sovereign Tower (STEAM) | 91 | 149 | 61% (90d) | Does not open (82%) | 85% |  |
| 46 | [ ] | Cry of Fear (STEAM) | 88 | 170 | 72% (1.3.0) | Does not open (52%) | 88% |  |
| 47 | [ ] | STEINS;GATE (STEAM) | 87 | 122 | 71% (90d) | Does not open (90%) | 90% |  |
| 48 | [ ] | Vital Shell (STEAM) | 85 | 129 | 66% (90d) | Does not open (52%) | 85% |  |
| 49 | [ ] | Hogwarts Legacy (STEAM) | 83 | 145 | 51% (1.3.0) | Does not open (59%) | 66% |  |
| 50 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 81 | 83 | 98% (90d) | Does not open (92%) | 62% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 51 | [ ] | The Sims™ 4 (STEAM) | 78 | 100 | 78% (90d) | Does not open (89%) | 68% |  |
| 52 | [ ] | Detroit: Become Human (STEAM) | 78 | 81 | 96% (90d) | Does not open (72%) | 66% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 53 | [ ] | Resident Evil 4 (2005) (STEAM) | 77 | 149 | 52% (90d) | Does not open (74%) | 73% |  |
| 54 | [ ] | Mega Man Zero/ZX Legacy Collection (STEAM) | 76 | 105 | 72% (90d) | Does not open (86%) | 86% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 55 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 74 | 125 | 59% (90d) | Controller issues (59%) | 94% |  |
| 56 | [ ] | Sid Meier's Civilization VI (STEAM) | 72 | 127 | 54% (1.3.0) | Does not open (70%) | 92% |  |
| 57 | [ ] | Ballionaire (STEAM) | 72 | 110 | 50% (1.3.0) | Does not open (77%) | 96% |  |
| 58 | [ ] | Alabaster Dawn (STEAM) | 71 | 126 | 56% (90d) | Controller issues (51%) | 91% |  |
| 59 | [ ] | Darksiders (STEAM) | 71 | 86 | 83% (90d) | Does not open (68%) | 88% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 60 | [ ] | Fallout (STEAM) | 70 | 108 | 65% (90d) | Does not open (69%) | 72% |  |
| 61 | [ ] | Antivirus Survivors 2003 Professional (STEAM) | 70 | 103 | 68% (90d) | Does not open (61%) | 92% |  |
| 62 | [ ] | Disgaea 5 Complete (STEAM) | 70 | 84 | 83% (90d) | Does not open (75%) | 100% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 63 | [ ] | Dota 2 (STEAM) | 69 | 106 | 57% (1.3.0) | Does not open (78%) | 71% |  |
| 64 | [ ] | Gunfire Reborn (STEAM) | 69 | 75 | 92% (90d) | Does not open (82%) | 94% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 65 | [ ] | American Truck Simulator (STEAM) | 68 | 108 | 79% (1.3.0) | Does not open (74%) | 76% |  |
| 66 | [ ] | Fable - The Lost Chapters (STEAM) | 68 | 107 | 52% (1.3.0) | Graphics glitches (51%) | 78% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 67 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 68 | 106 | 64% (90d) | Does not open (73%) | 71% |  |
| 68 | [ ] | Dungeons & Degenerate Gamblers (STEAM) | 68 | 92 | 55% (1.3.0) | Does not open (90%) | 99% |  |
| 69 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 68 | 81 | 95% (1.3.0) | Does not open (89%) | 97% |  |
| 70 | [ ] | Call of Juarez Gunslinger (STEAM) | 67 | 82 | 82% (90d) | Does not open (90%) | 74% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 71 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 66 | 123 | 55% (1.3.0) | Does not open (65%) | 63% |  |
| 72 | [ ] | Cyberpunk 2077 (GOG) | 65 | 80 | 81% (90d) | Does not open (78%) | 75% |  |
| 73 | [ ] | Borderlands: The Pre-Sequel (STEAM) | 64 | 90 | 71% (90d) | Does not open (77%) | 69% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 74 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 64 | 87 | 62% (1.3.0) | Does not open (50%) | 92% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 75 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 64 | 86 | 74% (90d) | Does not open (47%) | 62% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 76 | [ ] | MIO: Memories in Orbit (STEAM) | 63 | 120 | 66% (1.3.0) | Graphics glitches (54%) | 95% |  |
| 77 | [ ] | Big Walk (STEAM) | 63 | 96 | 66% (90d) | Does not open (68%) | 84% |  |
| 78 | [ ] | Poppy Playtime (STEAM) | 62 | 109 | 57% (90d) | Does not open (71%) | 77% |  |
| 79 | [ ] | Sonic Lost World (STEAM) | 62 | 104 | 60% (90d) | No graphics (59%) | 86% |  |
| 80 | [ ] | eFootball™ (STEAM) | 60 | 90 | 67% (90d) | Does not open (55%) | 75% |  |
| 81 | [ ] | A Plague Tale: Innocence (STEAM) | 60 | 63 | 95% (90d) | Does not open (88%) | 73% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 82 | [ ] | Red Dead Redemption 2 (STEAM) | 59 | 79 | 59% (1.3.0) | Does not open (98%) | 83% |  |
| 83 | [ ] | The Binding of Isaac (STEAM) | 58 | 134 | 62% (1.3.0) | Controller issues (92%) | 92% |  |
| 84 | [ ] | Mini Motorways (STEAM) | 58 | 101 | 57% (90d) | Does not open (76%) | 65% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 85 | [ ] | Starbound (STEAM) | 58 | 86 | 59% (1.3.0) | Does not open (68%) | 71% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 86 | [ ] | Borderlands 3 (STEAM) | 58 | 75 | 77% (90d) | Does not open (91%) | 95% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 87 | [ ] | Call of Duty: World at War (STEAM) | 57 | 80 | 71% (90d) | Does not open (42%) | 70% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 88 | [ ] | Deskrawl: Idle ARPG (STEAM) | 57 | 67 | 88% (1.3.0) | Does not open (60%) | 78% |  |
| 89 | [ ] | Sonic Generations (STEAM) | 57 | 67 | 85% (90d) | Does not open (72%) | 62% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 90 | [ ] | Dead by Daylight (STEAM) | 57 | 62 | 92% (90d) | Does not open (83%) | 83% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 91 | [ ] | Sonic Adventure DX (STEAM) | 56 | 92 | 61% (90d) | Does not open (86%) | 63% |  |
| 92 | [ ] | Ace Attorney Investigations Collection (STEAM) | 56 | 87 | 64% (90d) | Does not open (96%) | 92% |  |
| 93 | [ ] | The Secret of Monkey Island: Special Edition (STEAM) | 56 | 87 | 64% (90d) | Does not open (90%) | 71% |  |
| 94 | [ ] | TBH: Task Bar Hero (STEAM) | 55 | 85 | 65% (90d) | Does not open (74%) | 95% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 95 | [ ] | Okami HD (STEAM) | 54 | 99 | 55% (90d) | Controller issues (60%) | 83% |  |
| 96 | [ ] | Prey (STEAM) | 54 | 92 | 59% (90d) | Does not open (64%) | 83% |  |
| 97 | [ ] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 54 | 91 | 59% (90d) | Does not open (63%) | 62% |  |
| 98 | [ ] | Until Then (STEAM) | 53 | 92 | 58% (90d) | Does not open (73%) | 96% |  |
| 99 | [ ] | The Bazaar (STEAM) | 53 | 85 | 62% (90d) | Does not open (72%) | 85% |  |
| 100 | [ ] | Path of Exile (STEAM) | 53 | 62 | 85% (90d) | Does not open (91%) | 85% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 101 | [ ] | A Plague Tale: Innocence (EPIC) | 52 | 88 | 59% (90d) | Does not open (69%) | 94% |  |
| 102 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 52 | 60 | 87% (90d) | Does not open (80%) | 81% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 103 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 52 | 56 | 93% (90d) | Does not open (83%) | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 104 | [ ] | MapleStory (STEAM) | 52 | 54 | 90% (1.3.0) | Does not open (77%) | 76% |  |
| 105 | [ ] | MudRunner (STEAM) | 51 | 101 | 50% (90d) | Does not open (75%) | 66% |  |
| 106 | [ ] | DOOM 3 (STEAM) | 51 | 58 | 88% (90d) | Does not open (90%) | 60% | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 107 | [ ] | Sleeping Dogs™ (STEAM) | 51 | 58 | 88% (90d) | Does not open (85%) | 77% | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 108 | [ ] | Resident Evil 6 (STEAM) | 50 | 125 | 75% (1.3.0) | Does not open (55%) | 89% |  |
| 109 | [ ] | 7 Days to Die (STEAM) | 50 | 106 | 56% (1.3.0) | Does not open (74%) | 73% |  |
| 110 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 50 | 74 | 77% (1.3.0) | Does not open (59%) | 66% |  |
| 111 | [ ] | Guildrun Demo (STEAM) | 49 | 71 | 69% (90d) | No graphics (65%) | 70% |  |
| 112 | [ ] | Dead Space (STEAM) | 49 | 62 | 79% (90d) | Does not open (54%) | 74% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 113 | [ ] | Sheepy: A Short Adventure (STEAM) | 49 | 59 | 83% (90d) | Does not open (52%) | 79% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 114 | [ ] | Rivals of Aether II (STEAM) | 48 | 70 | 69% (90d) | Does not open (55%) | 75% |  |
| 115 | [ ] | Last Epoch (STEAM) | 48 | 69 | 74% (1.3.0) | Does not open (79%) | 100% |  |
| 116 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 48 | 69 | 70% (90d) | Does not open (83%) | 65% |  |
| 117 | [ ] | Digimon World: Next Order (STEAM) | 47 | 87 | 54% (90d) | Controller issues (80%) | 95% |  |
| 118 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 76 | 62% (90d) | Controller issues (55%) | 95% |  |
| 119 | [ ] | Street Fighter™ 6 (STEAM) | 47 | 73 | 64% (90d) | Does not open (88%) | 78% |  |
| 120 | [ ] | Moonlighter (EPIC) | 47 | 51 | 92% (90d) | No graphics (79%) | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 121 | [ ] | Tomb Raider: Anniversary (STEAM) | 46 | 65 | 71% (90d) | Does not open (95%) | 62% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 122 | [ ] | Darkest Dungeon® (EPIC) | 45 | 85 | 52% (1.3.0) | Does not open (62%) | 62% |  |
| 123 | [ ] | Grand Theft Auto V (EPIC) | 45 | 51 | 88% (90d) | Does not open (89%) | 84% |  |
| 124 | [ ] | FINAL FANTASY VII (2013) (STEAM) | 44 | 65 | 68% (90d) | Does not open (84%) | 78% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 125 | [ ] | Life is Strange™ (STEAM) | 43 | 85 | 51% (90d) | Does not open (74%) | 80% |  |
| 126 | [ ] | Resident Evil 7 Biohazard (STEAM) | 43 | 70 | 73% (1.3.0) | Does not open (77%) | 82% |  |
| 127 | [ ] | Salt and Sanctuary (STEAM) | 42 | 81 | 52% (90d) | Does not open (75%) | 81% |  |
| 128 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 42 | 77 | 71% (1.3.0) | Controller issues (47%) | 89% |  |
| 129 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 42 | 69 | 61% (90d) | Does not open (67%) | 79% |  |
| 130 | [ ] | Deadlock (STEAM) | 42 | 63 | 67% (90d) | Does not open (45%) | 93% |  |
| 131 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 42 | 63 | 67% (90d) | Does not open (73%) | 67% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 132 | [ ] | Your Only Move Is HUSTLE (STEAM) | 41 | 82 | 50% (90d) | Does not open (62%) | 88% |  |
| 133 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 41 | 75 | 55% (90d) | Controller issues (54%) | 85% |  |
| 134 | [ ] | Amnesia: The Dark Descent (STEAM) | 41 | 75 | 55% (90d) | Does not open (85%) | 76% |  |
| 135 | [ ] | Sonic Origins (STEAM) | 41 | 72 | 57% (90d) | Does not open (70%) | 83% |  |
| 136 | [ ] | Aggelos (STEAM) | 41 | 55 | 75% (90d) | No graphics (79%) | 95% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 137 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 40 | 41 | 98% (90d) | Does not open (62%) | 85% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 138 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 39 | 74 | 53% (90d) | No graphics (83%) | 97% |  |
| 139 | [ ] | Tales of ARISE (STEAM) | 39 | 68 | 57% (90d) | Controller issues (74%) | 94% |  |
| 140 | [ ] | Forza Horizon 4 (STEAM) | 39 | 55 | 71% (90d) | Does not open (48%) | 86% |  |
| 141 | [ ] | Capcom Arcade Stadium (STEAM) | 39 | 48 | 81% (90d) | Does not open (84%) | 75% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 142 | [ ] | CrossCode (GOG) | 39 | 43 | 91% (90d) | Does not open (76%) | 69% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 143 | [ ] | Monster Hunter Wilds (STEAM) | 39 | 40 | 98% (90d) | Does not open (63%) | 76% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 144 | [ ] | Fallout 3 (STEAM) | 37 | 72 | 51% (90d) | Does not open (48%) | 91% |  |
| 145 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 68 | 54% (90d) | Does not open (68%) | 87% |  |
| 146 | [ ] | Hearts of Iron IV (STEAM) | 36 | 62 | 58% (90d) | Does not open (74%) | 68% |  |
| 147 | [ ] | Street Fighter 30th Anniversary Collection (STEAM) | 35 | 67 | 52% (90d) | Does not open (100%) | 66% |  |
| 148 | [ ] | SurrounDead (STEAM) | 35 | 66 | 53% (90d) | Controller issues (61%) | 94% |  |
| 149 | [ ] | Capcom Fighting Collection 2 (STEAM) | 35 | 50 | 70% (90d) | Does not open (79%) | 84% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 150 | [ ] | SnowRunner (STEAM) | 35 | 48 | 73% (90d) | Does not open (96%) | 84% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 151 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 35 | 41 | 85% (90d) | No graphics (69%) | 80% | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 152 | [ ] | Rocket League (STEAM) | 34 | 55 | 62% (90d) | Does not open (69%) | 70% |  |
| 153 | [ ] | Earthion (STEAM) | 34 | 54 | 63% (90d) | Controller issues (88%) | 100% |  |
| 154 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 34 | 48 | 71% (90d) | Controller issues (88%) | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 155 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 34 | 40 | 85% (90d) | Does not open (64%) | 74% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 156 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 34 | 39 | 87% (90d) | Does not open (68%) | 60% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 157 | [ ] | Hotline Miami (GOG) | 34 | 39 | 87% (90d) | Does not open (94%) | 68% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 158 | [ ] | Torchlight II (STEAM) | 33 | 66 | 50% (90d) | Does not open (52%) | 91% |  |
| 159 | [ ] | Hero Siege (STEAM) | 33 | 57 | 58% (90d) | Graphics glitches (52%) | 62% |  |
| 160 | [ ] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 54 | 61% (90d) | Controller issues (84%) | 82% |  |
| 161 | [ ] | Supermarket Together (STEAM) | 33 | 48 | 69% (90d) | Does not open (72%) | 74% |  |
| 162 | [ ] | Russian Fishing 4 (STEAM) | 33 | 39 | 85% (90d) | Does not open (68%) | 73% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 163 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 33 | 38 | 87% (90d) | Does not open (73%) | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 164 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 32 | 62 | 52% (90d) | Does not open (75%) | 90% |  |
| 165 | [ ] | COCOON (STEAM) | 32 | 61 | 52% (90d) | Directx error (50%) | 89% |  |
| 166 | [ ] | Max Payne (STEAM) | 32 | 58 | 55% (90d) | No graphics (43%) | 96% |  |
| 167 | [ ] | Counter-Strike:Global Offensive (STEAM) | 32 | 51 | 63% (90d) | Does not open (78%) | 74% |  |
| 168 | [ ] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 32 | 51 | 63% (90d) | Does not open (43%) | 76% |  |
| 169 | [ ] | Secrets of Grindea (STEAM) | 32 | 50 | 64% (90d) | Does not open (52%) | 80% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 170 | [ ] | Romestead (STEAM) | 32 | 43 | 74% (90d) | Does not open (65%) | 74% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 171 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 42 | 76% (90d) | Controller issues (62%) | 89% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 172 | [ ] | Red Dead Redemption (STEAM) | 32 | 36 | 89% (90d) | Does not open (95%) | 89% |  |
| 173 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 31 | 55 | 56% (90d) | Does not open (46%) | 67% |  |
| 174 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 31 | 52 | 60% (90d) | Controller issues (61%) | 70% |  |
| 175 | [ ] | Tower and Sword of Succubus (STEAM) | 31 | 46 | 67% (90d) | No graphics (81%) | 100% |  |
| 176 | [ ] | Yakuza: Like a Dragon (STEAM) | 31 | 46 | 67% (90d) | Does not open (63%) | 70% |  |
| 177 | [ ] | Ultimate Custom Night (STEAM) | 31 | 43 | 72% (90d) | No graphics (69%) | 78% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 178 | [ ] | Nioh: Complete Edition (STEAM) | 31 | 42 | 74% (90d) | Does not open (56%) | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 179 | [ ] | Grand Theft Auto III (STEAM) | 31 | 39 | 79% (90d) | Does not open (52%) | 85% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 180 | [ ] | Path of Exile 2 (STEAM) | 31 | 37 | 84% (90d) | Does not open (96%) | 86% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 181 | [ ] | Need for Speed™ (STEAM) | 31 | 33 | 94% (90d) | Does not open (69%) | 63% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 182 | [ ] | Library Of Ruina (STEAM) | 30 | 60 | 50% (90d) | Does not open (70%) | 87% |  |
| 183 | [ ] | Palia (STEAM) | 30 | 41 | 73% (90d) | Does not open (67%) | 78% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 184 | [ ] | Super Animal Royale (STEAM) | 30 | 40 | 75% (90d) | Does not open (67%) | 74% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 185 | [ ] | CRUEL (STEAM) | 30 | 36 | 83% (90d) | Does not open (90%) | 75% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 186 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 29 | 68 | 50% (1.3.0) | Does not open (72%) | 80% |  |
| 187 | [ ] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 54 | 54% (90d) | Does not open (92%) | 83% |  |
| 188 | [ ] | Aethermancer (STEAM) | 29 | 52 | 56% (90d) | Does not open (78%) | 83% |  |
| 189 | [ ] | Heavy Rain (STEAM) | 29 | 50 | 58% (90d) | Controller issues (61%) | 85% |  |
| 190 | [ ] | Binary Domain (STEAM) | 29 | 45 | 64% (90d) | Does not open (92%) | 78% |  |
| 191 | [ ] | Dead Island Riptide Definitive Edition (STEAM) | 28 | 54 | 52% (90d) | Does not open (50%) | 81% |  |
| 192 | [ ] | Cave Story+ (EPIC) | 28 | 53 | 53% (90d) | Does not open (50%) | 86% |  |
| 193 | [ ] | Mortal Kombat X (STEAM) | 28 | 53 | 53% (90d) | Does not open (52%) | 83% |  |
| 194 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 28 | 49 | 57% (90d) | Controller issues (46%) | 93% |  |
| 195 | [ ] | Akane (STEAM) | 28 | 47 | 60% (90d) | Controller issues (67%) | 100% |  |
| 196 | [ ] | Zero Escape: The Nonary Games (STEAM) | 28 | 46 | 61% (90d) | Does not open (88%) | 67% |  |
| 197 | [ ] | Ratatan (STEAM) | 28 | 41 | 68% (90d) | Does not open (52%) | 99% |  |
| 198 | [ ] | Moonlight Peaks (STEAM) | 28 | 40 | 70% (90d) | Does not open (64%) | 100% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 199 | [ ] | Stellar Blade™ (STEAM) | 28 | 36 | 78% (90d) | Does not open (48%) | 86% |  |
| 200 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 28 | 28 | 100% (90d) | Does not open (91%) | 62% | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 201 | [ ] | Resident Evil Village (STEAM) | 27 | 50 | 54% (90d) | Does not open (65%) | 89% |  |
| 202 | [ ] | Dead Rising 2 (STEAM) | 27 | 42 | 67% (1.3.0) | Does not open (88%) | 70% |  |
| 203 | [ ] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 27 | 42 | 64% (90d) | Does not open (82%) | 88% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 204 | [ ] | Deus Ex™ GOTY Edition (GOG) | 27 | 41 | 66% (90d) | Does not open (35%) | 81% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 205 | [ ] | Crab Game (STEAM) | 27 | 36 | 75% (90d) | Does not open (56%) | 75% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 206 | [ ] | Tales of Zestiria (STEAM) | 27 | 33 | 82% (90d) | Does not open (81%) | 71% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 207 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 26 | 49 | 53% (90d) | Does not open (55%) | 70% |  |
| 208 | [ ] | Prince of Persia (GOG) | 26 | 42 | 62% (90d) | Does not open (95%) | 86% |  |
| 209 | [ ] | Battle Brothers (STEAM) | 26 | 41 | 63% (90d) | Does not open (68%) | 69% |  |
| 210 | [ ] | Limbus Company (STEAM) | 26 | 40 | 65% (90d) | Does not open (86%) | 82% |  |
| 211 | [ ] | Gothic II: Gold Classic (STEAM) | 26 | 37 | 70% (90d) | Does not open (59%) | 77% |  |
| 212 | [ ] | Beyond: Two Souls (STEAM) | 26 | 34 | 76% (90d) | Does not open (48%) | 70% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 213 | [ ] | Being a DIK (STEAM) | 25 | 43 | 58% (90d) | Does not open (78%) | 82% |  |
| 214 | [ ] | Counter-Strike: Condition Zero (STEAM) | 25 | 43 | 58% (90d) | Does not open (53%) | 62% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 215 | [ ] | Digimon Survive (STEAM) | 25 | 42 | 60% (90d) | Controller issues (71%) | 96% |  |
| 216 | [ ] | Wizard of Legend (EPIC) | 25 | 42 | 60% (90d) | Does not open (79%) | 77% |  |
| 217 | [ ] | Return to Monkey Island (STEAM) | 25 | 39 | 64% (90d) | No graphics (58%) | 86% |  |
| 218 | [ ] | Bongo Cat (STEAM) | 25 | 35 | 71% (90d) | Does not open (65%) | 78% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 219 | [ ] | Goose Goose Duck (STEAM) | 25 | 33 | 76% (90d) | Does not open (71%) | 69% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 220 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 32 | 78% (90d) | Does not open (87%) | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 221 | [ ] | Resident Evil (GOG) | 25 | 27 | 93% (90d) | Does not open (95%) | 70% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 222 | [ ] | Resident Evil Revelations 2 (STEAM) | 24 | 48 | 50% (90d) | Does not open (40%) | 91% |  |
| 223 | [ ] | Unturned (STEAM) | 24 | 44 | 55% (90d) | Does not open (59%) | 80% |  |
| 224 | [ ] | Goat Simulator (STEAM) | 24 | 43 | 56% (90d) | Does not open (58%) | 61% |  |
| 225 | [ ] | Cat Mail Co. (STEAM) | 24 | 39 | 62% (90d) | Does not open (89%) | 88% |  |
| 226 | [ ] | Changed (STEAM) | 24 | 38 | 63% (90d) | Does not open (65%) | 88% |  |
| 227 | [ ] | Opus Magnum (STEAM) | 24 | 38 | 63% (90d) | Does not open (76%) | 80% |  |
| 228 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 24 | 34 | 71% (90d) | Does not open (57%) | 65% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 229 | [ ] | Tearscape (STEAM) | 24 | 28 | 86% (90d) | Controller issues (53%) | 93% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 230 | [ ] | PowerWash Simulator (STEAM) | 23 | 67 | 76% (1.3.0) | Does not open (84%) | 77% |  |
| 231 | [ ] | Lobotomy Corporation (STEAM) | 23 | 40 | 58% (90d) | No graphics (60%) | 94% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 232 | [ ] | SWORN (STEAM) | 23 | 38 | 61% (90d) | Does not open (44%) | 100% |  |
| 233 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 36 | 64% (90d) | Does not open (100%) | 82% |  |
| 234 | [ ] | Timberborn (STEAM) | 23 | 34 | 68% (90d) | No graphics (62%) | 85% |  |
| 235 | [ ] | Party Animals (STEAM) | 23 | 32 | 72% (90d) | Does not open (75%) | 74% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 236 | [ ] | Jade Empire: Special Edition (GOG) | 23 | 31 | 74% (90d) | Does not open (50%) | 71% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 237 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 23 | 31 | 74% (90d) | Does not open (40%) | 73% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 238 | [ ] | FINAL FANTASY XIV Online (STEAM) | 23 | 30 | 77% (90d) | Does not open (100%) | 96% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 239 | [ ] | Jade Empire: Special Edition (STEAM) | 23 | 25 | 92% (90d) | Does not open (95%) | 64% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 240 | [ ] | Football Manager 2024 (EPIC) | 22 | 40 | 55% (90d) | Does not open (86%) | 91% |  |
| 241 | [ ] | Pinball FX Classic (STEAM) | 22 | 40 | 55% (90d) | Does not open (76%) | 91% |  |
| 242 | [ ] | This War of Mine (STEAM) | 22 | 40 | 55% (90d) | No graphics (56%) | 76% |  |
| 243 | [ ] | Worms W.M.D (STEAM) | 22 | 36 | 61% (90d) | Does not open (61%) | 89% |  |
| 244 | [ ] | Life is Strange Remastered (STEAM) | 22 | 34 | 65% (90d) | Does not open (73%) | 94% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 245 | [ ] | Need for Speed™ Unbound (STEAM) | 22 | 30 | 73% (90d) | Does not open (83%) | 77% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 246 | [ ] | Capcom Fighting Collection (STEAM) | 22 | 27 | 81% (90d) | Does not open (80%) | 74% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 247 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 59 | 82% (1.3.0) | Does not open (79%) | 100% |  |
| 248 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 21 | 42 | 50% (90d) | Controller issues (65%) | 90% |  |
| 249 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 21 | 40 | 53% (90d) | Does not open (53%) | 71% |  |
| 250 | [ ] | Gambonanza (STEAM) | 21 | 40 | 53% (90d) | Does not open (60%) | 92% |  |
| 251 | [ ] | One-armed robber (STEAM) | 21 | 38 | 55% (90d) | Controller issues (58%) | 79% |  |
| 252 | [ ] | Trailmakers (STEAM) | 21 | 38 | 55% (90d) | Does not open (44%) | 93% |  |
| 253 | [ ] | Tiny Glade (STEAM) | 21 | 37 | 57% (90d) | Does not open (42%) | 72% |  |
| 254 | [ ] | GOD EATER RESURRECTION (STEAM) | 21 | 32 | 66% (90d) | Does not open (53%) | 61% |  |
| 255 | [ ] | Nex Machina (STEAM) | 21 | 28 | 75% (90d) | Does not open (57%) | 85% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 256 | [ ] | Paper Lily - Chapter 1 (STEAM) | 20 | 40 | 50% (90d) | Does not open (72%) | 93% |  |
| 257 | [ ] | Crimzon Clover World EXplosion (STEAM) | 20 | 39 | 51% (90d) | Does not open (47%) | 100% |  |
| 258 | [ ] | Control Ultimate Edition (GOG) | 20 | 37 | 54% (90d) | Does not open (81%) | 94% |  |
| 259 | [ ] | Mafia: Definitive Edition (STEAM) | 20 | 37 | 54% (90d) | Does not open (84%) | 82% |  |
| 260 | [ ] | Killing Floor (STEAM) | 20 | 36 | 56% (90d) | Controller issues (100%) | 87% |  |
| 261 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 20 | 29 | 69% (90d) | Does not open (74%) | 73% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 262 | [ ] | BAJA: Edge of Control HD (STEAM) | 20 | 26 | 77% (90d) | Does not open (100%) | 90% | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 263 | [ ] | Dead Island (STEAM) | 20 | 26 | 77% (90d) | Does not open (69%) | 74% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 264 | [ ] | Tyr (STEAM) | 20 | 26 | 77% (90d) | Does not open (33%) | 90% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 265 | [ ] | TCG Card Shop Simulator (STEAM) | 19 | 38 | 50% (90d) | Does not open (63%) | 86% |  |
| 266 | [ ] | GRIP: Combat Racing (STEAM) | 19 | 34 | 56% (90d) | Does not open (100%) | 85% |  |
| 267 | [ ] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 19 | 34 | 56% (90d) | Does not open (88%) | 69% |  |
| 268 | [ ] | Stick It to the Stickman (STEAM) | 19 | 34 | 56% (90d) | Does not open (88%) | 74% |  |
| 269 | [ ] | Hitman: Absolution (GOG) | 19 | 31 | 61% (90d) | Does not open (82%) | 84% |  |
| 270 | [ ] | Metro Exodus (STEAM) | 19 | 31 | 61% (90d) | Does not open (82%) | 89% |  |
| 271 | [ ] | Tabletop Simulator (STEAM) | 19 | 31 | 61% (90d) | Does not open (53%) | 60% |  |
| 272 | [ ] | Arcade Paradise (EPIC) | 19 | 27 | 70% (90d) | Does not open (45%) | 82% |  |
| 273 | [ ] | Torchlight II (EPIC) | 19 | 27 | 70% (90d) | Does not open (82%) | 100% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 274 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 19 | 24 | 79% (90d) | Does not open (82%) | 93% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 275 | [ ] | Faster Than Light (EPIC) | 18 | 36 | 50% (90d) | Does not open (41%) | 94% |  |
| 276 | [ ] | SCP – Containment Breach (STEAM) | 18 | 36 | 50% (90d) | Does not open (83%) | 83% |  |
| 277 | [ ] | SKALD: Against the Black Priory (STEAM) | 18 | 36 | 50% (90d) | No graphics (63%) | 97% |  |
| 278 | [ ] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 18 | 34 | 53% (90d) | Controller issues (50%) | 100% |  |
| 279 | [ ] | My Summer Car (STEAM) | 18 | 33 | 55% (90d) | Does not open (56%) | 89% |  |
| 280 | [ ] | Far Far West (STEAM) | 18 | 32 | 56% (90d) | Does not open (59%) | 83% |  |
| 281 | [ ] | DNF Duel (EPIC) | 18 | 31 | 58% (90d) | Does not open (47%) | 90% |  |
| 282 | [ ] | Formula Legends (STEAM) | 18 | 29 | 62% (90d) | No graphics (60%) | 68% |  |
| 283 | [ ] | Crusader Kings III (STEAM) | 18 | 22 | 82% (90d) | No graphics (64%) | 73% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 284 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 18 | 22 | 82% (90d) | Controller issues (100%) | 100% |  |
| 285 | [ ] | Deadly Premonition: The Director's Cut (STEAM) | 18 | 21 | 86% (90d) | Does not open (47%) | 75% |  |
| 286 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 17 | 34 | 50% (90d) | Does not open (64%) | 71% |  |
| 287 | [ ] | CULTIC (STEAM) | 17 | 34 | 50% (90d) | Does not open (92%) | 65% |  |
| 288 | [ ] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 17 | 34 | 50% (90d) | Does not open (54%) | 92% |  |
| 289 | [ ] | Lost Castle 2 (STEAM) | 17 | 32 | 53% (90d) | Does not open (62%) | 100% |  |
| 290 | [ ] | GRANDIA HD Remaster (STEAM) | 17 | 31 | 55% (90d) | Does not open (93%) | 71% |  |
| 291 | [ ] | Shank 2 (STEAM) | 17 | 30 | 57% (90d) | Does not open (82%) | 100% |  |
| 292 | [ ] | Maneater (STEAM) | 17 | 28 | 61% (90d) | Does not open (92%) | 77% |  |
| 293 | [ ] | Dishonored 2 (STEAM) | 17 | 27 | 63% (90d) | Does not open (86%) | 94% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 294 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 17 | 27 | 63% (90d) | No graphics (47%) | 78% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 295 | [ ] | DOOM 3: BFG Edition (GOG) | 17 | 24 | 71% (90d) | No graphics (71%) | 79% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 296 | [ ] | Katanaut (STEAM) | 17 | 24 | 71% (90d) | Does not open (75%) | 64% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 297 | [ ] | Fall Guys (STEAM) | 17 | 23 | 74% (90d) | Does not open (92%) | 92% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 298 | [ ] | Prey (GOG) | 17 | 22 | 77% (90d) | Does not open (47%) | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 299 | [ ] | Realm of the Mad God Exalt (STEAM) | 17 | 22 | 77% (90d) | Does not open (91%) | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 300 | [ ] | Warframe (STEAM) | 16 | 32 | 50% (90d) | Does not open (78%) | 95% |  |
| 301 | [ ] | Mark of the Ninja (STEAM) | 16 | 31 | 52% (90d) | Does not open (67%) | 62% |  |
| 302 | [ ] | Titanfall® 2 (STEAM) | 16 | 27 | 59% (90d) | Does not open (83%) | 83% |  |
| 303 | [ ] | WORLD OF FINAL FANTASY (STEAM) | 16 | 26 | 62% (90d) | No graphics (62%) | 75% |  |
| 304 | [ ] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 16 | 25 | 64% (90d) | Does not open (100%) | 96% |  |
| 305 | [ ] | Chef Knight (STEAM) | 16 | 23 | 70% (90d) | Does not open (93%) | 69% |  |
| 306 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 22 | 73% (90d) | No graphics (60%) | 88% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 307 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 16 | 20 | 80% (90d) | Does not open (60%) | 90% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 308 | [ ] | Antichamber (STEAM) | 15 | 30 | 50% (90d) | Does not open (38%) | 88% |  |
| 309 | [ ] | Mortal Shell (EPIC) | 15 | 26 | 58% (90d) | No graphics (89%) | 86% |  |
| 310 | [ ] | Wildermyth (STEAM) | 15 | 26 | 58% (90d) | Does not open (50%) | 94% |  |
| 311 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 15 | 25 | 60% (90d) | Does not open (92%) | 74% |  |
| 312 | [ ] | LET IT DIE (STEAM) | 15 | 25 | 60% (90d) | Does not open (91%) | 79% |  |
| 313 | [ ] | Alabaster Dawn Demo (STEAM) | 15 | 24 | 63% (90d) | Controller issues (73%) | 94% |  |
| 314 | [ ] | Batman™: Arkham Origins (GOG) | 15 | 24 | 63% (90d) | Does not open (67%) | 93% |  |
| 315 | [ ] | Sorry We're Closed (EPIC) | 15 | 24 | 63% (90d) | Does not open (100%) | 91% |  |
| 316 | [ ] | Sons Of The Forest (STEAM) | 15 | 23 | 65% (90d) | Does not open (56%) | 76% |  |
| 317 | [ ] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 15 | 23 | 65% (90d) | Does not open (64%) | 71% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 318 | [ ] | Allumeria (STEAM) | 15 | 22 | 68% (90d) | Does not open (69%) | 69% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 319 | [ ] | Treasure of Nadia (GOG) | 15 | 21 | 71% (90d) | Does not open (79%) | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 320 | [ ] | Cyberpunk 2077 (EPIC) | 15 | 20 | 75% (90d) | Does not open (42%) | 81% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 321 | [ ] | Maneater (EPIC) | 15 | 20 | 75% (90d) | Does not open (73%) | 83% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 322 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 28 | 50% (90d) | Controller issues (54%) | 85% |  |
| 323 | [ ] | sobosuba (STEAM) | 14 | 26 | 54% (90d) | Does not open (57%) | 89% |  |
| 324 | [ ] | Ultrapool (STEAM) | 14 | 25 | 56% (90d) | Does not open (54%) | 100% |  |
| 325 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 24 | 58% (90d) | Does not open (90%) | 73% |  |
| 326 | [ ] | Gloomwood (STEAM) | 14 | 24 | 58% (90d) | Does not open (62%) | 75% |  |
| 327 | [ ] | Disgaea 4 Complete+ (STEAM) | 14 | 22 | 64% (90d) | No graphics (43%) | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 328 | [ ] | Prince of Persia: The Two Thrones (STEAM) | 14 | 22 | 64% (90d) | Does not open (86%) | 63% |  |
| 329 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 22 | 64% (90d) | Does not open (71%) | 63% |  |
| 330 | [ ] | Songs of Conquest (EPIC) | 14 | 22 | 64% (90d) | Does not open (75%) | 90% |  |
| 331 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 22 | 64% (90d) | Controller issues (57%) | 62% |  |
| 332 | [ ] | Horny Villa (STEAM) | 14 | 20 | 70% (90d) | Does not open (63%) | 100% |  |
| 333 | [ ] | Haydee (STEAM) | 13 | 24 | 54% (90d) | Does not open (100%) | 89% |  |
| 334 | [ ] | Look Outside (GOG) | 13 | 24 | 54% (90d) | Does not open (100%) | 100% |  |
| 335 | [ ] | Pillars of Eternity (STEAM) | 13 | 24 | 54% (90d) | Does not open (43%) | 62% |  |
| 336 | [ ] | UNDEFEATED (STEAM) | 13 | 24 | 54% (90d) | Does not open (80%) | 82% |  |
| 337 | [ ] | DiRT 4 (STEAM) | 13 | 23 | 57% (90d) | Does not open (75%) | 96% |  |
| 338 | [ ] | Lust Goddess (STEAM) | 13 | 23 | 57% (90d) | Does not open (100%) | 64% |  |
| 339 | [ ] | Minit (EPIC) | 13 | 23 | 57% (90d) | Does not open (82%) | 82% |  |
| 340 | [ ] | 12 is Better Than 6 (STEAM) | 13 | 22 | 59% (90d) | Does not open (50%) | 83% |  |
| 341 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 22 | 59% (90d) | Does not open (80%) | 91% |  |
| 342 | [ ] | FINAL FANTASY TYPE-0 HD (STEAM) | 13 | 21 | 62% (90d) | Does not open (62%) | 64% |  |
| 343 | [ ] | Secret of Mana (STEAM) | 13 | 21 | 62% (90d) | Graphics glitches (58%) | 64% |  |
| 344 | [ ] | Escape the Backrooms (STEAM) | 13 | 20 | 65% (90d) | Does not open (100%) | 92% |  |
| 345 | [ ] | War Thunder (STEAM) | 13 | 20 | 65% (90d) | Does not open (80%) | 83% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 346 | [ ] | Sonic Superstars (STEAM) | 12 | 24 | 50% (90d) | Does not open (70%) | 66% |  |
| 347 | [ ] | AER Memories of Old (EPIC) | 12 | 23 | 52% (90d) | Does not open (91%) | 93% |  |
| 348 | [ ] | F.E.A.R. 2: Project Origin (STEAM) | 12 | 23 | 52% (90d) | Does not open (50%) | 82% |  |
| 349 | [ ] | Injustice™ 2 (STEAM) | 12 | 23 | 52% (90d) | Does not open (89%) | 70% |  |
| 350 | [ ] | NiGHTS into Dreams... (STEAM) | 12 | 23 | 52% (90d) | Does not open (44%) | 92% |  |
| 351 | [ ] | Sid Meier's Civilization VI (EPIC) | 12 | 23 | 52% (90d) | Does not open (45%) | 85% |  |
| 352 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 12 | 22 | 55% (90d) | Does not open (60%) | 88% |  |
| 353 | [ ] | FATE (STEAM) | 12 | 21 | 57% (90d) | No graphics (44%) | 91% |  |
| 354 | [ ] | Ready or Not (STEAM) | 12 | 21 | 57% (90d) | Does not open (60%) | 88% |  |
| 355 | [ ] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 21 | 57% (90d) | Controller issues (60%) | 93% |  |
| 356 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (90d) | No graphics (67%) | 60% |  |
| 357 | [ ] | PAYDAY: The Heist (STEAM) | 12 | 20 | 60% (90d) | Does not open (73%) | 70% |  |
| 358 | [ ] | Shift At Midnight (STEAM) | 12 | 20 | 60% (90d) | Does not open (80%) | 90% |  |
| 359 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (90d) | Does not open (89%) | 96% |  |
| 360 | [ ] | Castle in the Clouds (STEAM) | 11 | 22 | 50% (90d) | No graphics (63%) | 84% |  |
| 361 | [ ] | Cruelty Squad (STEAM) | 11 | 22 | 50% (90d) | Does not open (67%) | 85% |  |
| 362 | [ ] | Pocket Mirror ~ GoldenerTraum (STEAM) | 11 | 22 | 50% (90d) | Does not open (70%) | 94% |  |
| 363 | [ ] | Tom Clancy's Rainbow Six: Vegas 2 (STEAM) | 11 | 22 | 50% (90d) | Does not open (55%) | 88% |  |
| 364 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 21 | 52% (90d) | Does not open (86%) | 76% |  |
| 365 | [ ] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 20 | 55% (90d) | Graphics glitches (40%) | 95% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 366 | [ ] | Coromon (GOG) | 10 | 20 | 50% (90d) | Does not open (56%) | 65% |  |
| 367 | [ ] | HITMAN World of Assassination (STEAM) | 10 | 20 | 50% (90d) | Does not open (67%) | 85% |  |

## Recently recovered (387)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | FINAL FANTASY RESONANCE (STEAM) | 286 | 2026-10-24 | 654 | 73% |  |
| 2 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 259 | 2026-10-23 | 300 | 66% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 3 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 248 | 2026-10-19 | 299 | 66% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 225 | 2026-10-18 | 347 | 59% |  |
| 5 | [x] | DRAGON BALL FighterZ (STEAM) | 208 | 2026-11-01 | 238 | 60% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 6 | [x] | OMORI (STEAM) | 207 | 2026-10-16 | 250 | 78% |  |
| 7 | [x] | Devil May Cry HD Collection (STEAM) | 200 | 2026-10-19 | 282 | 76% |  |
| 8 | [x] | Spelunky 2 (STEAM) | 193 | 2026-11-01 | 211 | 48% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 9 | [x] | Burnout Paradise: The Ultimate Box (STEAM) | 158 | 2026-10-16 | 244 | 71% |  |
| 10 | [x] | Counter-Strike (STEAM) | 148 | 2026-10-22 | 232 | 52% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 11 | [x] | Sonic Adventure™ 2  (STEAM) | 145 | 2026-11-01 | 206 | 55% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 12 | [x] | Borderlands 2 (EPIC) | 139 | 2026-10-25 | 166 | 64% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 13 | [x] | Far Cry® 3 (STEAM) | 132 | 2026-10-21 | 148 | 65% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 14 | [x] | Minecraft Dungeons II (STEAM) | 123 | 2026-10-21 | 141 | 66% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 15 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 120 | 2026-10-28 | 149 | 63% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 16 | [x] | Call of Duty: Black Ops III (STEAM) | 117 | 2026-10-18 | 244 | 72% |  |
| 17 | [x] | Euro Truck Simulator 2 (STEAM) | 117 | 2026-11-01 | 215 | 57% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 18 | [x] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 114 | 2026-10-18 | 159 | 63% |  |
| 19 | [x] | The Witcher: Enhanced Edition (STEAM) | 114 | 2026-10-25 | 130 | 63% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 20 | [x] | Moonstone Island (STEAM) | 103 | 2026-10-16 | 136 | 89% |  |
| 21 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 98 | 2026-10-25 | 154 | 65% |  |
| 22 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 97 | 2026-10-18 | 144 | 76% |  |
| 23 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 97 | 2026-10-17 | 128 | 98% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 24 | [x] | Don't Starve Together (STEAM) | 90 | 2026-10-16 | 178 | 80% |  |
| 25 | [x] | Cry of Fear (STEAM) | 88 | 2026-10-18 | 170 | 88% |  |
| 26 | [x] | Ultra Street Fighter IV (STEAM) | 86 | 2026-10-17 | 183 | 68% |  |
| 27 | [x] | Catherine Classic (STEAM) | 85 | 2026-10-19 | 176 | 81% |  |
| 28 | [x] | Hogwarts Legacy (STEAM) | 83 | 2026-10-17 | 145 | 66% |  |
| 29 | [x] | DOOM 3: BFG Edition (STEAM) | 82 | 2026-10-19 | 118 | 70% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 30 | [x] | FINAL FANTASY XIII-2 (STEAM) | 81 | 2026-10-30 | 83 | 62% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 31 | [x] | Need for Speed: Hot Pursuit (STEAM) | 78 | 2026-10-25 | 108 | 77% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 32 | [x] | Detroit: Become Human (STEAM) | 78 | 2026-10-17 | 81 | 66% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 33 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 76 | 2026-10-17 | 105 | 86% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 34 | [x] | Bayonetta (STEAM) | 74 | 2026-10-18 | 207 | 78% |  |
| 35 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 74 | 2026-10-18 | 125 | 94% |  |
| 36 | [x] | Don't Starve (STEAM) | 73 | 2026-10-16 | 160 | 82% |  |
| 37 | [x] | Darksiders (STEAM) | 71 | 2026-10-26 | 86 | 88% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 38 | [x] | Fallout (STEAM) | 70 | 2026-10-18 | 108 | 72% |  |
| 39 | [x] | Disgaea 5 Complete (STEAM) | 70 | 2026-10-18 | 84 | 100% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 40 | [x] | Dota 2 (STEAM) | 69 | 2026-10-17 | 106 | 71% |  |
| 41 | [x] | Gunfire Reborn (STEAM) | 69 | 2026-10-22 | 75 | 94% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 42 | [x] | American Truck Simulator (STEAM) | 68 | 2026-10-18 | 108 | 76% |  |
| 43 | [x] | Fable - The Lost Chapters (STEAM) | 68 | 2026-10-17 | 107 | 78% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 44 | [x] | Spyro™ Reignited Trilogy (STEAM) | 68 | 2026-10-18 | 106 | 71% |  |
| 45 | [x] | Call of Juarez Gunslinger (STEAM) | 67 | 2026-10-18 | 82 | 74% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 46 | [x] | Bloodstained: Ritual of the Night (EPIC) | 66 | 2026-10-19 | 123 | 63% |  |
| 47 | [x] | Stardew Valley (GOG) | 66 | 2026-11-01 | 119 | 51% |  |
| 48 | [x] | Borderlands: The Pre-Sequel (STEAM) | 64 | 2026-10-17 | 90 | 69% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 49 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 64 | 2026-10-17 | 87 | 92% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 50 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 64 | 2026-10-21 | 86 | 62% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 51 | [x] | Big Walk (STEAM) | 63 | 2026-10-17 | 96 | 84% |  |
| 52 | [x] | Poppy Playtime (STEAM) | 62 | 2026-10-17 | 109 | 77% |  |
| 53 | [x] | Sonic Lost World (STEAM) | 62 | 2026-10-18 | 104 | 86% |  |
| 54 | [x] | eFootball™ (STEAM) | 60 | 2026-10-18 | 90 | 75% |  |
| 55 | [x] | A Plague Tale: Innocence (STEAM) | 60 | 2026-10-20 | 63 | 73% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 56 | [x] | Mini Motorways (STEAM) | 58 | 2026-10-29 | 101 | 65% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 57 | [x] | Starbound (STEAM) | 58 | 2026-10-18 | 86 | 71% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 58 | [x] | Borderlands 3 (STEAM) | 58 | 2026-10-19 | 75 | 95% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 59 | [x] | Call of Duty: World at War (STEAM) | 57 | 2026-10-28 | 80 | 70% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 60 | [x] | Sonic Generations (STEAM) | 57 | 2026-10-17 | 67 | 62% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 61 | [x] | Dead by Daylight (STEAM) | 57 | 2026-10-23 | 62 | 83% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 62 | [x] | Sonic Adventure DX (STEAM) | 56 | 2026-10-17 | 92 | 63% |  |
| 63 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 56 | 2026-10-18 | 87 | 71% |  |
| 64 | [x] | TBH: Task Bar Hero (STEAM) | 55 | 2026-10-19 | 85 | 95% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 65 | [x] | Okami HD (STEAM) | 54 | 2026-10-17 | 99 | 83% |  |
| 66 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 54 | 2026-11-02 | 91 | 62% |  |
| 67 | [x] | Until Then (STEAM) | 53 | 2026-10-17 | 92 | 96% |  |
| 68 | [x] | Path of Exile (STEAM) | 53 | 2026-10-26 | 62 | 85% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 69 | [x] | A Plague Tale: Innocence (EPIC) | 52 | 2026-10-25 | 88 | 94% |  |
| 70 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 52 | 2026-10-21 | 60 | 81% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 71 | [x] | Alex Kidd in Miracle World DX (EPIC) | 52 | 2026-10-22 | 56 | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 72 | [x] | MudRunner (STEAM) | 51 | 2026-10-24 | 101 | 66% |  |
| 73 | [x] | DOOM 3 (STEAM) | 51 | 2026-11-01 | 58 | 60% | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 74 | [x] | Sleeping Dogs™ (STEAM) | 51 | 2026-10-27 | 58 | 77% | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 75 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 50 | 2026-10-25 | 96 | 57% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 76 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 50 | 2026-10-19 | 95 | 75% |  |
| 77 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 50 | 2026-10-18 | 74 | 66% |  |
| 78 | [x] | Guildrun Demo (STEAM) | 49 | 2026-10-22 | 71 | 70% |  |
| 79 | [x] | Dead Space (STEAM) | 49 | 2026-10-18 | 62 | 74% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 80 | [x] | Sheepy: A Short Adventure (STEAM) | 49 | 2026-10-24 | 59 | 79% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 81 | [x] | Rivals of Aether II (STEAM) | 48 | 2026-10-20 | 70 | 75% |  |
| 82 | [x] | STEINS;GATE RE:BOOT (STEAM) | 48 | 2026-10-21 | 69 | 65% |  |
| 83 | [x] | Digimon World: Next Order (STEAM) | 47 | 2026-10-18 | 87 | 95% |  |
| 84 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 2026-10-17 | 76 | 95% |  |
| 85 | [x] | Street Fighter™ 6 (STEAM) | 47 | 2026-10-16 | 73 | 78% |  |
| 86 | [x] | Moonlighter (EPIC) | 47 | 2026-10-23 | 51 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 87 | [x] | Tomb Raider: Anniversary (STEAM) | 46 | 2026-10-25 | 65 | 62% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 88 | [x] | Dishonored - Definitive Edition (EPIC) | 45 | 2026-10-17 | 95 | 82% |  |
| 89 | [x] | Darkest Dungeon® (EPIC) | 45 | 2026-10-22 | 85 | 62% |  |
| 90 | [x] | Abiotic Factor (STEAM) | 44 | 2026-10-18 | 79 | 70% |  |
| 91 | [x] | FINAL FANTASY VII (2013) (STEAM) | 44 | 2026-10-18 | 65 | 78% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 92 | [x] | PROTOTYPE 2 (STEAM) | 43 | 2026-10-18 | 89 | 77% |  |
| 93 | [x] | Life is Strange™ (STEAM) | 43 | 2026-10-17 | 85 | 80% |  |
| 94 | [x] | Skullgirls 2nd Encore (STEAM) | 43 | 2026-11-01 | 78 | 58% |  |
| 95 | [x] | Death Road to Canada (STEAM) | 42 | 2026-10-17 | 99 | 70% |  |
| 96 | [x] | Tomb Raider GOTY (GOG) | 42 | 2026-10-17 | 88 | 97% |  |
| 97 | [x] | Salt and Sanctuary (STEAM) | 42 | 2026-10-18 | 81 | 81% |  |
| 98 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 42 | 2026-10-18 | 63 | 67% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 99 | [x] | Deadlock (STEAM) | 42 | 2026-10-16 | 63 | 93% |  |
| 100 | [x] | Cobalt Core (STEAM) | 41 | 2026-10-18 | 94 | 88% |  |
| 101 | [x] | Rogue Legacy (STEAM) | 41 | 2026-10-17 | 90 | 55% |  |
| 102 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 41 | 2026-10-17 | 75 | 85% |  |
| 103 | [x] | Amnesia: The Dark Descent (STEAM) | 41 | 2026-10-17 | 75 | 76% |  |
| 104 | [x] | Aggelos (STEAM) | 41 | 2026-10-21 | 55 | 95% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 105 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 40 | 2026-10-27 | 41 | 85% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 106 | [x] | Rayman Origins (STEAM) | 39 | 2026-10-17 | 87 | 79% |  |
| 107 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 39 | 2026-10-17 | 74 | 97% |  |
| 108 | [x] | Tales of ARISE (STEAM) | 39 | 2026-10-16 | 68 | 94% |  |
| 109 | [x] | Capcom Arcade Stadium (STEAM) | 39 | 2026-10-17 | 48 | 75% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 110 | [x] | CrossCode (GOG) | 39 | 2026-10-23 | 43 | 69% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 111 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-10-23 | 40 | 76% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 112 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 2026-10-17 | 68 | 87% |  |
| 113 | [x] | Sable (EPIC) | 36 | 2026-10-18 | 78 | 85% |  |
| 114 | [x] | Hearts of Iron IV (STEAM) | 36 | 2026-10-19 | 62 | 68% |  |
| 115 | [x] | Teardown (STEAM) | 35 | 2026-10-17 | 75 | 77% |  |
| 116 | [x] | POSTAL 2 (GOG) | 35 | 2026-10-22 | 71 | 92% |  |
| 117 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 35 | 2026-10-16 | 67 | 66% |  |
| 118 | [x] | Capcom Fighting Collection 2 (STEAM) | 35 | 2026-10-18 | 50 | 84% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 119 | [x] | SnowRunner (STEAM) | 35 | 2026-10-19 | 48 | 84% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 120 | [x] | STAR WARS™ Episode I: Racer (GOG) | 35 | 2026-11-02 | 41 | 80% | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 121 | [x] | Journey (STEAM) | 34 | 2026-10-27 | 71 | 54% |  |
| 122 | [x] | Ultimate Chicken Horse (STEAM) | 34 | 2026-10-23 | 70 | 62% |  |
| 123 | [x] | Rocket League (STEAM) | 34 | 2026-10-17 | 55 | 70% |  |
| 124 | [x] | Earthion (STEAM) | 34 | 2026-10-22 | 54 | 100% |  |
| 125 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 34 | 2026-10-21 | 48 | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 126 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 34 | 2026-10-18 | 40 | 74% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 127 | [x] | Hotline Miami (GOG) | 34 | 2026-10-20 | 39 | 68% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 128 | [x] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 34 | 2026-11-01 | 39 | 60% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 129 | [x] | Torchlight II (STEAM) | 33 | 2026-10-20 | 66 | 91% |  |
| 130 | [x] | Hero Siege (STEAM) | 33 | 2026-11-02 | 57 | 62% |  |
| 131 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 2026-10-19 | 54 | 82% |  |
| 132 | [x] | Supermarket Together (STEAM) | 33 | 2026-10-19 | 48 | 74% |  |
| 133 | [x] | Russian Fishing 4 (STEAM) | 33 | 2026-10-23 | 39 | 73% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 134 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 33 | 2026-10-22 | 38 | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 135 | [x] | Bloodstained: Curse of the Moon (STEAM) | 32 | 2026-10-16 | 73 | 65% |  |
| 136 | [x] | Little Nightmares (STEAM) | 32 | 2026-10-16 | 71 | 61% |  |
| 137 | [x] | COCOON (STEAM) | 32 | 2026-10-17 | 61 | 89% |  |
| 138 | [x] | Max Payne (STEAM) | 32 | 2026-10-17 | 58 | 96% |  |
| 139 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 32 | 2026-10-22 | 51 | 76% |  |
| 140 | [x] | Counter-Strike:Global Offensive (STEAM) | 32 | 2026-10-19 | 51 | 74% |  |
| 141 | [x] | Secrets of Grindea (STEAM) | 32 | 2026-10-20 | 50 | 80% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 142 | [x] | Romestead (STEAM) | 32 | 2026-10-18 | 43 | 74% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 143 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-10-20 | 42 | 89% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 144 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 31 | 2026-10-26 | 55 | 67% |  |
| 145 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 31 | 2026-10-19 | 52 | 70% |  |
| 146 | [x] | Tower and Sword of Succubus (STEAM) | 31 | 2026-10-22 | 46 | 100% |  |
| 147 | [x] | Ultimate Custom Night (STEAM) | 31 | 2026-10-19 | 43 | 78% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 148 | [x] | Nioh: Complete Edition (STEAM) | 31 | 2026-10-20 | 42 | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 149 | [x] | Grand Theft Auto III (STEAM) | 31 | 2026-10-17 | 39 | 85% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 150 | [x] | Path of Exile 2 (STEAM) | 31 | 2026-10-18 | 37 | 86% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 151 | [x] | Need for Speed™ (STEAM) | 31 | 2026-10-18 | 33 | 63% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 152 | [x] | Monster Hunter Stories (STEAM) | 30 | 2026-10-17 | 63 | 85% |  |
| 153 | [x] | Library Of Ruina (STEAM) | 30 | 2026-10-16 | 60 | 87% |  |
| 154 | [x] | Palia (STEAM) | 30 | 2026-10-22 | 41 | 78% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 155 | [x] | Super Animal Royale (STEAM) | 30 | 2026-10-19 | 40 | 74% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 156 | [x] | CRUEL (STEAM) | 30 | 2026-10-28 | 36 | 75% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 157 | [x] | Stumble Guys (STEAM) | 29 | 2026-10-18 | 61 | 80% |  |
| 158 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 2026-10-17 | 54 | 83% |  |
| 159 | [x] | Aethermancer (STEAM) | 29 | 2026-10-18 | 52 | 83% |  |
| 160 | [x] | Heavy Rain (STEAM) | 29 | 2026-10-18 | 50 | 85% |  |
| 161 | [x] | Binary Domain (STEAM) | 29 | 2026-10-18 | 45 | 78% |  |
| 162 | [x] | Dying Light (EPIC) | 28 | 2026-10-17 | 65 | 90% |  |
| 163 | [x] | BioShock™ (GOG) | 28 | 2026-10-18 | 64 | 70% |  |
| 164 | [x] | State of Decay: Year-One (STEAM) | 28 | 2026-10-18 | 60 | 80% |  |
| 165 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 28 | 2026-10-18 | 54 | 81% |  |
| 166 | [x] | Cave Story+ (EPIC) | 28 | 2026-10-18 | 53 | 86% |  |
| 167 | [x] | Mortal Kombat X (STEAM) | 28 | 2026-10-17 | 53 | 83% |  |
| 168 | [x] | Prince of Persia: The Sands of Time (STEAM) | 28 | 2026-10-20 | 49 | 93% |  |
| 169 | [x] | Akane (STEAM) | 28 | 2026-10-20 | 47 | 100% |  |
| 170 | [x] | Zero Escape: The Nonary Games (STEAM) | 28 | 2026-10-17 | 46 | 67% |  |
| 171 | [x] | Moonlight Peaks (STEAM) | 28 | 2026-10-20 | 40 | 100% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 172 | [x] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 28 | 2026-10-28 | 28 | 62% | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 173 | [x] | Resident Evil Village (STEAM) | 27 | 2026-10-17 | 50 | 89% |  |
| 174 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 27 | 2026-10-18 | 42 | 88% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 175 | [x] | Deus Ex™ GOTY Edition (GOG) | 27 | 2026-10-19 | 41 | 81% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 176 | [x] | Crab Game (STEAM) | 27 | 2026-10-22 | 36 | 75% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 177 | [x] | Tales of Zestiria (STEAM) | 27 | 2026-10-27 | 33 | 71% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 178 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 26 | 2026-10-19 | 89 | 94% |  |
| 179 | [x] | PlateUp! (STEAM) | 26 | 2026-10-16 | 56 | 84% |  |
| 180 | [x] | G.I. Joe Wrath of Cobra (EPIC) | 26 | 2026-10-19 | 49 | 70% |  |
| 181 | [x] | Prince of Persia (GOG) | 26 | 2026-10-24 | 42 | 86% |  |
| 182 | [x] | Battle Brothers (STEAM) | 26 | 2026-10-27 | 41 | 69% |  |
| 183 | [x] | Limbus Company (STEAM) | 26 | 2026-10-18 | 40 | 82% |  |
| 184 | [x] | Gothic II: Gold Classic (STEAM) | 26 | 2026-10-20 | 37 | 77% |  |
| 185 | [x] | Beyond: Two Souls (STEAM) | 26 | 2026-10-22 | 34 | 70% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 186 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 25 | 2026-10-19 | 61 | 85% |  |
| 187 | [x] | CarX Drift Racing Online (STEAM) | 25 | 2026-10-16 | 58 | 74% |  |
| 188 | [x] | Titan Quest Anniversary Edition (STEAM) | 25 | 2026-10-16 | 56 | 83% |  |
| 189 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 25 | 2026-10-20 | 53 | 83% |  |
| 190 | [x] | Being a DIK (STEAM) | 25 | 2026-10-19 | 43 | 82% |  |
| 191 | [x] | Counter-Strike: Condition Zero (STEAM) | 25 | 2026-10-17 | 43 | 62% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 192 | [x] | Wizard of Legend (EPIC) | 25 | 2026-10-18 | 42 | 77% |  |
| 193 | [x] | Digimon Survive (STEAM) | 25 | 2026-10-23 | 42 | 96% |  |
| 194 | [x] | Return to Monkey Island (STEAM) | 25 | 2026-10-23 | 39 | 86% |  |
| 195 | [x] | Bongo Cat (STEAM) | 25 | 2026-10-20 | 35 | 78% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 196 | [x] | Goose Goose Duck (STEAM) | 25 | 2026-10-25 | 33 | 69% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 197 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-10-21 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 198 | [x] | Resident Evil (GOG) | 25 | 2026-10-20 | 27 | 70% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 199 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 54 | 86% |  |
| 200 | [x] | WEBFISHING (STEAM) | 24 | 2026-10-17 | 51 | 90% |  |
| 201 | [x] | Unturned (STEAM) | 24 | 2026-10-17 | 44 | 80% |  |
| 202 | [x] | Goat Simulator (STEAM) | 24 | 2026-11-01 | 43 | 61% |  |
| 203 | [x] | Cat Mail Co. (STEAM) | 24 | 2026-10-24 | 39 | 88% |  |
| 204 | [x] | Changed (STEAM) | 24 | 2026-10-24 | 38 | 88% |  |
| 205 | [x] | Opus Magnum (STEAM) | 24 | 2026-11-01 | 38 | 80% |  |
| 206 | [x] | Borderlands: The Pre-Sequel (EPIC) | 24 | 2026-10-30 | 34 | 65% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 207 | [x] | Tearscape (STEAM) | 24 | 2026-10-30 | 28 | 93% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 208 | [x] | ABZÛ (STEAM) | 23 | 2026-10-21 | 53 | 89% |  |
| 209 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 23 | 2026-10-27 | 47 | 25% |  |
| 210 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-10-19 | 40 | 94% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 211 | [x] | SWORN (STEAM) | 23 | 2026-10-23 | 38 | 100% |  |
| 212 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 2026-10-17 | 36 | 82% |  |
| 213 | [x] | Timberborn (STEAM) | 23 | 2026-10-25 | 34 | 85% |  |
| 214 | [x] | Party Animals (STEAM) | 23 | 2026-10-17 | 32 | 74% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 215 | [x] | Jade Empire: Special Edition (GOG) | 23 | 2026-10-23 | 31 | 71% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 216 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 23 | 2026-10-25 | 31 | 73% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 217 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 96% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 218 | [x] | Jade Empire: Special Edition (STEAM) | 23 | 2026-11-01 | 25 | 64% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 219 | [x] | Saints Row IV (STEAM) | 22 | 2026-10-19 | 51 | 74% |  |
| 220 | [x] | Football Manager 2024 (EPIC) | 22 | 2026-10-20 | 40 | 91% |  |
| 221 | [x] | Pinball FX Classic (STEAM) | 22 | 2026-10-23 | 40 | 91% |  |
| 222 | [x] | This War of Mine (STEAM) | 22 | 2026-10-21 | 40 | 76% |  |
| 223 | [x] | Life is Strange Remastered (STEAM) | 22 | 2026-10-20 | 34 | 94% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 224 | [x] | Need for Speed™ Unbound (STEAM) | 22 | 2026-10-26 | 30 | 77% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 225 | [x] | Capcom Fighting Collection (STEAM) | 22 | 2026-10-23 | 27 | 74% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 226 | [x] | BlazBlue Centralfiction (STEAM) | 21 | 2026-10-17 | 61 | 81% |  |
| 227 | [x] | Slow Roads (STEAM) | 21 | 2026-10-22 | 46 | 97% |  |
| 228 | [x] | Hatred (STEAM) | 21 | 2026-10-22 | 44 | 85% |  |
| 229 | [x] | Owlboy (STEAM) | 21 | 2026-11-02 | 44 | 49% |  |
| 230 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 21 | 2026-10-24 | 42 | 90% |  |
| 231 | [x] | Brothers - A Tale of Two Sons (EPIC) | 21 | 2026-10-23 | 40 | 71% |  |
| 232 | [x] | One-armed robber (STEAM) | 21 | 2026-10-23 | 38 | 79% |  |
| 233 | [x] | Trailmakers (STEAM) | 21 | 2026-10-21 | 38 | 93% |  |
| 234 | [x] | Tiny Glade (STEAM) | 21 | 2026-10-24 | 37 | 72% |  |
| 235 | [x] | GOD EATER RESURRECTION (STEAM) | 21 | 2026-11-01 | 32 | 61% |  |
| 236 | [x] | Nex Machina (STEAM) | 21 | 2026-10-18 | 28 | 85% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 237 | [x] | No Rest for the Wicked (STEAM) | 20 | 2026-10-19 | 43 | 76% |  |
| 238 | [x] | MudRunner (EPIC) | 20 | 2026-10-18 | 42 | 91% |  |
| 239 | [x] | Paper Lily - Chapter 1 (STEAM) | 20 | 2026-10-27 | 40 | 93% |  |
| 240 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-10-20 | 39 | 100% |  |
| 241 | [x] | Mafia: Definitive Edition (STEAM) | 20 | 2026-10-28 | 37 | 82% |  |
| 242 | [x] | Killing Floor (STEAM) | 20 | 2026-10-19 | 36 | 87% |  |
| 243 | [x] | Sonic and SEGA All Stars Racing (STEAM) | 20 | 2026-10-19 | 29 | 73% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 244 | [x] | BAJA: Edge of Control HD (STEAM) | 20 | 2026-10-28 | 26 | 90% | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 245 | [x] | Dead Island (STEAM) | 20 | 2026-10-20 | 26 | 74% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 246 | [x] | Tyr (STEAM) | 20 | 2026-11-02 | 26 | 90% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 247 | [x] | GRIP: Combat Racing (STEAM) | 19 | 2026-10-20 | 34 | 85% |  |
| 248 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 19 | 2026-10-21 | 34 | 69% |  |
| 249 | [x] | Stick It to the Stickman (STEAM) | 19 | 2026-10-17 | 34 | 74% |  |
| 250 | [x] | Hitman: Absolution (GOG) | 19 | 2026-10-24 | 31 | 84% |  |
| 251 | [x] | Metro Exodus (STEAM) | 19 | 2026-10-20 | 31 | 89% |  |
| 252 | [x] | Tabletop Simulator (STEAM) | 19 | 2026-10-19 | 31 | 60% |  |
| 253 | [x] | Arcade Paradise (EPIC) | 19 | 2026-10-25 | 27 | 82% |  |
| 254 | [x] | Torchlight II (EPIC) | 19 | 2026-10-22 | 27 | 100% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 255 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 19 | 2026-10-23 | 24 | 93% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 256 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 18 | 2026-10-25 | 41 | 69% |  |
| 257 | [x] | Graveyard Keeper (GOG) | 18 | 2026-10-25 | 38 | 16% |  |
| 258 | [x] | Faster Than Light (EPIC) | 18 | 2026-10-24 | 36 | 94% |  |
| 259 | [x] | SCP – Containment Breach (STEAM) | 18 | 2026-10-27 | 36 | 83% |  |
| 260 | [x] | SKALD: Against the Black Priory (STEAM) | 18 | 2026-10-20 | 36 | 97% |  |
| 261 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 18 | 2026-10-21 | 34 | 100% |  |
| 262 | [x] | My Summer Car (STEAM) | 18 | 2026-10-30 | 33 | 89% |  |
| 263 | [x] | Far Far West (STEAM) | 18 | 2026-10-21 | 32 | 83% |  |
| 264 | [x] | DNF Duel (EPIC) | 18 | 2026-10-21 | 31 | 90% |  |
| 265 | [x] | Formula Legends (STEAM) | 18 | 2026-10-21 | 29 | 68% |  |
| 266 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-01 | 22 | 73% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 267 | [x] | Grim Fandango Remastered (STEAM) | 17 | 2026-10-19 | 37 | 76% |  |
| 268 | [x] | Backpack Battles (STEAM) | 17 | 2026-10-21 | 35 | 96% |  |
| 269 | [x] | Spin Rhythm XD (STEAM) | 17 | 2026-10-18 | 35 | 82% |  |
| 270 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 17 | 2026-10-20 | 34 | 71% |  |
| 271 | [x] | CULTIC (STEAM) | 17 | 2026-10-24 | 34 | 65% |  |
| 272 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 17 | 2026-10-18 | 34 | 92% |  |
| 273 | [x] | Lost Castle 2 (STEAM) | 17 | 2026-11-02 | 32 | 100% |  |
| 274 | [x] | GRANDIA HD Remaster (STEAM) | 17 | 2026-10-22 | 31 | 71% |  |
| 275 | [x] | Shank 2 (STEAM) | 17 | 2026-10-27 | 30 | 100% |  |
| 276 | [x] | Maneater (STEAM) | 17 | 2026-10-20 | 28 | 77% |  |
| 277 | [x] | Dishonored 2 (STEAM) | 17 | 2026-10-20 | 27 | 94% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 278 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 17 | 2026-10-20 | 27 | 78% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 279 | [x] | DOOM 3: BFG Edition (GOG) | 17 | 2026-10-19 | 24 | 79% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 280 | [x] | Katanaut (STEAM) | 17 | 2026-10-20 | 24 | 64% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 281 | [x] | Fall Guys (STEAM) | 17 | 2026-10-26 | 23 | 92% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 282 | [x] | Prey (GOG) | 17 | 2026-10-27 | 22 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 283 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 284 | [x] | Realm of the Mad God Exalt (STEAM) | 17 | 2026-10-29 | 22 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 285 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 286 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 51 | 100% |  |
| 287 | [x] | No Man's Sky (GOG) | 16 | 2026-10-19 | 37 | 76% |  |
| 288 | [x] | Kingdom Come: Deliverance II (STEAM) | 16 | 2026-10-20 | 35 | 100% |  |
| 289 | [x] | Mini Metro (STEAM) | 16 | 2026-11-01 | 34 | 52% |  |
| 290 | [x] | Mark of the Ninja (STEAM) | 16 | 2026-10-26 | 31 | 62% |  |
| 291 | [x] | Titanfall® 2 (STEAM) | 16 | 2026-10-16 | 27 | 83% |  |
| 292 | [x] | WORLD OF FINAL FANTASY (STEAM) | 16 | 2026-10-19 | 26 | 75% |  |
| 293 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 16 | 2026-10-21 | 25 | 96% |  |
| 294 | [x] | Chef Knight (STEAM) | 16 | 2026-10-27 | 23 | 69% |  |
| 295 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 2026-10-21 | 22 | 88% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 296 | [x] | Jotunnslayer: Hordes of Hel (STEAM) | 16 | 2026-10-30 | 20 | 90% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 297 | [x] | Antichamber (STEAM) | 15 | 2026-10-20 | 30 | 88% |  |
| 298 | [x] | Mortal Shell (EPIC) | 15 | 2026-10-19 | 26 | 86% |  |
| 299 | [x] | Wildermyth (STEAM) | 15 | 2026-10-26 | 26 | 94% |  |
| 300 | [x] | LET IT DIE (STEAM) | 15 | 2026-10-25 | 25 | 79% |  |
| 301 | [x] | Batman™: Arkham Origins (GOG) | 15 | 2026-10-22 | 24 | 93% |  |
| 302 | [x] | Alabaster Dawn Demo (STEAM) | 15 | 2026-10-27 | 24 | 94% |  |
| 303 | [x] | Sons Of The Forest (STEAM) | 15 | 2026-10-19 | 23 | 76% |  |
| 304 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 15 | 2026-10-20 | 23 | 71% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 305 | [x] | Allumeria (STEAM) | 15 | 2026-10-23 | 22 | 69% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 306 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 307 | [x] | Cyberpunk 2077 (EPIC) | 15 | 2026-10-19 | 20 | 81% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 308 | [x] | Maneater (EPIC) | 15 | 2026-10-28 | 20 | 83% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 309 | [x] | Rayman Origins (GOG) | 14 | 2026-11-02 | 29 | 56% |  |
| 310 | [x] | Distance (STEAM) | 14 | 2026-10-19 | 29 | 83% |  |
| 311 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 2026-10-29 | 28 | 85% |  |
| 312 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 14 | 2026-10-21 | 25 | 93% |  |
| 313 | [x] | Ultrapool (STEAM) | 14 | 2026-10-24 | 25 | 100% |  |
| 314 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 2026-10-25 | 24 | 73% |  |
| 315 | [x] | Gloomwood (STEAM) | 14 | 2026-10-29 | 24 | 75% |  |
| 316 | [x] | Songs of Conquest (EPIC) | 14 | 2026-11-02 | 22 | 90% |  |
| 317 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-10-23 | 22 | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 318 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 319 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 320 | [x] | Super Monkey Ball Banana Mania (STEAM) | 14 | 2026-10-18 | 22 | 62% |  |
| 321 | [x] | Horny Villa (STEAM) | 14 | 2026-10-21 | 20 | 100% |  |
| 322 | [x] | Middle-earth™: Shadow of War™ (STEAM) | 13 | 2026-10-16 | 39 | 76% |  |
| 323 | [x] | Blood: Fresh Supply (STEAM) | 13 | 2026-10-16 | 36 | 83% |  |
| 324 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 32 | 63% |  |
| 325 | [x] | Breath of Fire IV (GOG) | 13 | 2026-10-26 | 28 | 67% |  |
| 326 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 13 | 2026-11-01 | 28 | 55% |  |
| 327 | [x] | Dead Space™ 3 (STEAM) | 13 | 2026-10-20 | 28 | 72% |  |
| 328 | [x] | Haiku, the Robot (STEAM) | 13 | 2026-10-21 | 28 | 85% |  |
| 329 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 28 | 50% |  |
| 330 | [x] | Human Fall Flat (STEAM) | 13 | 2026-10-29 | 27 | 64% |  |
| 331 | [x] | Look Outside (GOG) | 13 | 2026-11-01 | 24 | 100% |  |
| 332 | [x] | Haydee (STEAM) | 13 | 2026-10-22 | 24 | 89% |  |
| 333 | [x] | Pillars of Eternity (STEAM) | 13 | 2026-10-26 | 24 | 62% |  |
| 334 | [x] | UNDEFEATED (STEAM) | 13 | 2026-11-01 | 24 | 82% |  |
| 335 | [x] | DiRT 4 (STEAM) | 13 | 2026-10-20 | 23 | 96% |  |
| 336 | [x] | Lust Goddess (STEAM) | 13 | 2026-10-26 | 23 | 64% |  |
| 337 | [x] | 12 is Better Than 6 (STEAM) | 13 | 2026-10-21 | 22 | 83% |  |
| 338 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-10-21 | 22 | 91% |  |
| 339 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 13 | 2026-10-28 | 21 | 64% |  |
| 340 | [x] | Secret of Mana (STEAM) | 13 | 2026-10-28 | 21 | 64% |  |
| 341 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 92% |  |
| 342 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 83% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 343 | [x] | The WereCleaner (STEAM) | 12 | 2026-10-22 | 31 | 95% |  |
| 344 | [x] | Tom Clancy's Splinter Cell: Chaos Theory (STEAM) | 12 | 2026-10-16 | 30 | 84% |  |
| 345 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 26 | 70% |  |
| 346 | [x] | Sonic Superstars (STEAM) | 12 | 2026-10-21 | 24 | 66% |  |
| 347 | [x] | Sid Meier's Civilization VI (EPIC) | 12 | 2026-10-19 | 23 | 85% |  |
| 348 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 12 | 2026-10-21 | 23 | 82% |  |
| 349 | [x] | Injustice™ 2 (STEAM) | 12 | 2026-10-17 | 23 | 70% |  |
| 350 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-10-28 | 23 | 92% |  |
| 351 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-10-22 | 22 | 88% |  |
| 352 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 353 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 2026-10-26 | 21 | 93% |  |
| 354 | [x] | Human Resource Machine (EPIC) | 12 | 2026-11-01 | 20 | 60% |  |
| 355 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 356 | [x] | PAYDAY: The Heist (STEAM) | 12 | 2026-11-02 | 20 | 70% |  |
| 357 | [x] | Shift At Midnight (STEAM) | 12 | 2026-11-01 | 20 | 90% |  |
| 358 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 11 | 2026-10-19 | 29 | 98% |  |
| 359 | [x] | Mortal Kombat 11 (STEAM) | 11 | 2026-10-28 | 27 | 67% |  |
| 360 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 11 | 2026-10-20 | 25 | 71% |  |
| 361 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 2026-10-27 | 23 | 79% |  |
| 362 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 23 | 80% |  |
| 363 | [x] | Castle in the Clouds (STEAM) | 11 | 2026-10-21 | 22 | 84% |  |
| 364 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 11 | 2026-10-23 | 22 | 94% |  |
| 365 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-10-24 | 21 | 76% |  |
| 366 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 2026-10-25 | 20 | 95% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 367 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 368 | [x] | TowerFall Ascension (STEAM) | 10 | 2026-10-16 | 30 | 53% |  |
| 369 | [x] | Possessor(s) (STEAM) | 10 | 2026-10-24 | 26 | 100% |  |
| 370 | [x] | Divinity: Original Sin (Classic) (STEAM) | 10 | 2026-10-16 | 23 | 82% |  |
| 371 | [x] | Mina the Hollower (GOG) | 10 | 2026-10-28 | 22 | 56% |  |
| 372 | [x] | SteamWorld Heist (GOG) | 10 | 2026-10-25 | 22 | 60% |  |
| 373 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 22 | 94% |  |
| 374 | [x] | DRAGON BALL XENOVERSE (STEAM) | 10 | 2026-10-28 | 21 | 55% |  |
| 375 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 376 | [x] | Coromon (GOG) | 10 | 2026-10-19 | 20 | 65% |  |
| 377 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 378 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 379 | [x] | What Remains of Edith Finch (STEAM) | 9 | 2026-10-19 | 25 | 44% |  |
| 380 | [x] | Delver (STEAM) | 9 | 2026-10-17 | 22 | 75% |  |
| 381 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 9 | 2026-10-23 | 22 | 69% |  |
| 382 | [x] | Football Manager 2024 (STEAM) | 9 | 2026-10-16 | 20 | n/a |  |
| 383 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 9 | 2026-10-20 | 20 | n/a |  |
| 384 | [x] | Gloomhaven (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 385 | [x] | Intravenous (STEAM) | 8 | 2026-10-16 | 20 | 94% |  |
| 386 | [x] | Mafia II: Definitive Edition (STEAM) | 7 | 2026-10-16 | 20 | n/a |  |
| 387 | [x] | Alex Kidd in Miracle World DX (STEAM) | 2 | 2026-10-16 | 37 | 86% |  |
