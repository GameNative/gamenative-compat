# GameNative compatibility worklist

Generated: `2026-11-04T04:15:05.872Z` · App release: `1.3.0` · Ratings since: `2026-08-06T04:15:05.872Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 250 |
| Probably does not work | 68 |
| First launch fails | 375 |
| Mixed | 467 |
| Works | 1024 |
| Total | 2184 |

## Does not work (250)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [x] 2026-10-18 | Project Zomboid (STEAM) | 598 | 632 | 93% (1.3.0) | Does not open (66%) | 53% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 2 | [x] 2026-10-18 | Alan Wake (STEAM) | 254 | 265 | 90% (1.3.0) | Does not open (87%) | 9% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 3 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 244 | 263 | 93% (90d) | Does not open (76%) | 11% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 4 | [ ] | Counter-Strike 2 (STEAM) | 228 | 313 | 81% (1.3.0) | Does not open (61%) | 43% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 5 | [x] 2026-10-18 | Call of Duty: Black Ops (STEAM) | 214 | 225 | 95% (90d) | Does not open (75%) | 11% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 6 | [ ] | skate. (STEAM) | 193 | 208 | 93% (90d) | Does not open (79%) | 16% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 7 | [x] 2026-10-18 | Sid Meier's Civilization V (STEAM) | 175 | 187 | 94% (90d) | Does not open (75%) | 56% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 8 | [ ] | Necesse (STEAM) | 157 | 162 | 97% (90d) | Does not open (81%) | 51% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 9 | [ ] | Peggle Deluxe (STEAM) | 153 | 184 | 83% (90d) | Does not open (92%) | 35% | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 10 | [ ] | HELLDIVERS™ 2 (STEAM) | 139 | 145 | 96% (90d) | Does not open (92%) | 22% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 11 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 134 | 149 | 90% (90d) | Does not open (87%) | 45% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 12 | [ ] | Assassin's Creed II (STEAM) | 124 | 129 | 96% (90d) | Does not open (78%) | 50% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 13 | [ ] | Dust: An Elysian Tail (STEAM) | 106 | 110 | 96% (90d) | Does not open (73%) | 7% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 14 | [ ] | The Witcher: Enhanced Edition (GOG) | 104 | 114 | 91% (90d) | Does not open (73%) | 13% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 15 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 103 | 137 | 72% (1.3.0) | Does not open (75%) | 38% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 16 | [ ] | Call of Duty: Black Ops II (STEAM) | 101 | 134 | 85% (1.3.0) | Does not open (78%) | 24% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 17 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 100 | 113 | 88% (90d) | No graphics (59%) | 52% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 18 | [ ] | Mafia II (Classic) (STEAM) | 96 | 101 | 95% (90d) | Does not open (72%) | 5% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 19 | [ ] | Saints Row 2 (STEAM) | 94 | 106 | 92% (1.3.0) | Does not open (96%) | 41% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 20 | [ ] | Saints Row: The Third (STEAM) | 89 | 90 | 99% (90d) | Does not open (78%) | 31% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 21 | [ ] | Transistor (STEAM) | 89 | 89 | 100% (90d) | Does not open (73%) | 0% | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 22 | [ ] | Duskfade (STEAM) | 87 | 89 | 98% (90d) | Does not open (95%) | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 23 | [ ] | Black Mesa (STEAM) | 84 | 115 | 73% (90d) | Does not open (81%) | 12% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 24 | [ ] | Sniper Elite 4 (STEAM) | 83 | 83 | 100% (90d) | Does not open (97%) | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 25 | [ ] | Fall Guys (EPIC) | 81 | 93 | 87% (90d) | Does not open (76%) | 11% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 26 | [ ] | HELLDIVERS™ (STEAM) | 79 | 92 | 86% (90d) | Does not open (59%) | 42% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 27 | [ ] | MECCHA CHAMELEON (STEAM) | 78 | 110 | 71% (90d) | Does not open (65%) | 59% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 28 | [ ] | Dead Space 2 (STEAM) | 78 | 99 | 79% (90d) | Does not open (73%) | 36% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 29 | [ ] | GRID 2 (STEAM) | 76 | 79 | 96% (90d) | Does not open (67%) | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 30 | [ ] | The Wolf Among Us (STEAM) | 74 | 83 | 89% (90d) | Does not open (68%) | 13% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 31 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 70 | 74 | 95% (90d) | Does not open (70%) | 0% | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 32 | [ ] | Call of Duty: Black Ops II - Zombies (STEAM) | 69 | 85 | 81% (90d) | Does not open (70%) | 51% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 33 | [ ] | Burnout™ Paradise Remastered (STEAM) | 69 | 72 | 96% (90d) | Does not open (88%) | 18% | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 34 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 68 | 73 | 93% (90d) | Does not open (79%) | 8% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 35 | [ ] | Saints Row 2 (GOG) | 67 | 80 | 84% (90d) | Does not open (96%) | 48% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 36 | [x] 2026-10-18 | Diablo® IV (STEAM) | 67 | 79 | 85% (90d) | Does not open (61%) | 23% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 37 | [ ] | Borderlands GOTY (STEAM) | 67 | 72 | 93% (90d) | Does not open (95%) | 22% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 38 | [ ] | Marvel Rivals (STEAM) | 66 | 74 | 89% (90d) | Does not open (81%) | 0% | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 39 | [ ] | Door Kickers 2 (STEAM) | 66 | 70 | 94% (90d) | No graphics (85%) | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 40 | [ ] | Metro 2033 (STEAM) | 65 | 81 | 80% (90d) | Does not open (63%) | 44% | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 41 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 65 | 74 | 88% (90d) | No graphics (47%) | 25% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 42 | [ ] | GRID (STEAM) | 63 | 79 | 80% (90d) | Does not open (57%) | 49% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 43 | [ ] | Need for Speed™ Heat  (STEAM) | 62 | 77 | 81% (90d) | Does not open (77%) | 27% | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 44 | [ ] | Three Kingdoms : Alias (STEAM) | 62 | 66 | 94% (90d) | No graphics (97%) | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 45 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 62 | 62 | 100% (90d) | Does not open (53%) | 8% | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 46 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 61 | 87 | 70% (90d) | Does not open (83%) | 51% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 47 | [ ] | Spore (STEAM) | 60 | 65 | 92% (90d) | Does not open (69%) | 36% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 48 | [ ] | DOOM (2016) (GOG) | 58 | 64 | 91% (90d) | Does not open (90%) | 43% | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 49 | [ ] | XCOM: Enemy Unknown (STEAM) | 58 | 61 | 95% (90d) | Does not open (75%) | 7% | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 50 | [ ] | Enshrouded (STEAM) | 56 | 57 | 98% (90d) | Does not open (95%) | 19% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 51 | [ ] | GrandChase (STEAM) | 55 | 58 | 95% (90d) | Does not open (84%) | 13% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 52 | [ ] | Overwatch® (STEAM) | 55 | 57 | 96% (90d) | Does not open (58%) | 25% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 53 | [ ] | Fortune Mill (STEAM) | 54 | 55 | 98% (90d) | Does not open (89%) | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 54 | [ ] | STAR WARS Zero Company™ (STEAM) | 53 | 55 | 96% (90d) | Does not open (64%) | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 55 | [ ] | Spec Ops: The Line (STEAM) | 53 | 54 | 98% (90d) | No graphics (56%) | 0% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 56 | [ ] | Watch_Dogs (STEAM) | 52 | 67 | 78% (90d) | Does not open (90%) | 19% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 57 | [ ] | South Park The Fractured But Whole (STEAM) | 52 | 52 | 100% (90d) | Does not open (66%) | 16% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 58 | [ ] | Split/Second (STEAM) | 51 | 60 | 85% (90d) | Does not open (76%) | 10% | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 59 | [ ] | Max Payne 3 (STEAM) | 51 | 56 | 91% (90d) | Does not open (93%) | 41% | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 60 | [ ] | Sandustry (STEAM) | 50 | 62 | 81% (90d) | Does not open (73%) | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 61 | [ ] | METAL SLUG 3 (STEAM) | 50 | 58 | 86% (90d) | Does not open (80%) | 19% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 62 | [ ] | RoboCop: Rogue City (STEAM) | 50 | 54 | 93% (90d) | Does not open (37%) | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 63 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 49 | 64 | 77% (90d) | Does not open (80%) | 40% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 64 | [ ] | Trackmania (STEAM) | 49 | 62 | 79% (90d) | Does not open (85%) | 39% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 65 | [ ] | Scott Pilgrim vs The World (STEAM) | 49 | 49 | 100% (90d) | Does not open (83%) | 47% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 66 | [ ] | Asphalt Legends  (STEAM) | 48 | 56 | 86% (90d) | Does not open (80%) | 47% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 67 | [ ] | DOOM Eternal (STEAM) | 48 | 50 | 96% (90d) | Does not open (69%) | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 68 | [ ] | Hitman: Absolution (STEAM) | 47 | 52 | 90% (90d) | Does not open (84%) | 7% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 69 | [ ] | tModLoader (STEAM) | 46 | 53 | 87% (90d) | Does not open (86%) | 3% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 70 | [ ] | Aliens vs. Predator (STEAM) | 46 | 51 | 90% (90d) | No graphics (54%) | 25% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 71 | [ ] | STAR WARS™ Republic Commando (STEAM) | 46 | 48 | 96% (90d) | Does not open (80%) | 50% | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 72 | [ ] | State of Decay 2 (STEAM) | 45 | 63 | 71% (90d) | Does not open (93%) | 0% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 73 | [ ] | Prince of Persia The Lost Crown (STEAM) | 45 | 49 | 92% (90d) | Does not open (94%) | 36% | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 74 | [ ] | To The Moon (GOG) | 44 | 48 | 96% (1.3.0) | Does not open (86%) | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 75 | [ ] | The Survivalists (STEAM) | 44 | 46 | 96% (90d) | Does not open (98%) | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 76 | [ ] | Mafia: Definitive Edition (GOG) | 43 | 56 | 77% (90d) | Does not open (85%) | 26% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 77 | [ ] | Diablo + Hellfire (GOG) | 43 | 49 | 88% (90d) | Does not open (64%) | 33% | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 78 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 43 | 46 | 93% (90d) | Does not open (95%) | 58% | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 79 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 43 | 44 | 98% (90d) | Does not open (84%) | 43% | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 80 | [ ] | Tales of Berseria (STEAM) | 42 | 43 | 98% (90d) | Does not open (87%) | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 81 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 41 | 45 | 91% (90d) | Does not open (71%) | 25% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 82 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 41 | 42 | 98% (90d) | Does not open (63%) | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 83 | [ ] | Need for Speed™ Rivals (STEAM) | 39 | 47 | 83% (90d) | Does not open (60%) | 42% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 84 | [ ] | L.A. Noire (STEAM) | 38 | 45 | 84% (90d) | Does not open (96%) | 52% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 85 | [ ] | Mafia (STEAM) | 38 | 43 | 88% (90d) | Does not open (69%) | 42% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 86 | [ ] | DJMAX RESPECT V (STEAM) | 38 | 42 | 90% (90d) | Does not open (82%) | 36% | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 87 | [ ] | Marvel's Spider-Man 2 (STEAM) | 38 | 40 | 95% (90d) | Does not open (87%) | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 88 | [ ] | GeoGuessr Steam Edition (STEAM) | 38 | 39 | 97% (90d) | No graphics (62%) | n/a | [#154](https://github.com/GameNative/gamenative-compat/issues/154) |
| 89 | [ ] | ARC Raiders (STEAM) | 37 | 42 | 88% (90d) | Does not open (91%) | 0% | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 90 | [ ] | ScourgeBringer (STEAM) | 37 | 42 | 88% (90d) | Does not open (69%) | 6% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 91 | [ ] | Elite Dangerous (STEAM) | 37 | 40 | 93% (90d) | Does not open (76%) | 56% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 92 | [ ] | BIT.TRIP RUNNER (STEAM) | 37 | 39 | 95% (90d) | Does not open (59%) | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 93 | [ ] | Dragon's Dogma 2 (STEAM) | 37 | 38 | 97% (90d) | Does not open (91%) | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 94 | [ ] | Beat Saber (STEAM) | 36 | 42 | 86% (90d) | Does not open (45%) | 35% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 95 | [ ] | Barotrauma (STEAM) | 36 | 39 | 92% (90d) | Does not open (97%) | 36% | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 96 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 36 | 38 | 95% (90d) | Does not open (94%) | 29% | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 97 | [ ] | Metro: Last Light Redux (STEAM) | 35 | 93 | 77% (1.3.0) | Does not open (92%) | 41% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 98 | [ ] | CODE VEIN (STEAM) | 35 | 49 | 71% (90d) | Does not open (68%) | 34% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 99 | [ ] | CARRION (GOG) | 35 | 43 | 81% (90d) | Does not open (73%) | 8% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 100 | [ ] | FINAL FANTASY VIII (STEAM) | 35 | 43 | 81% (90d) | Does not open (65%) | 45% | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 101 | [ ] | GOALS (STEAM) | 35 | 42 | 83% (90d) | Does not open (83%) | 28% | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 102 | [ ] | BattleBit Remastered (STEAM) | 35 | 39 | 90% (90d) | Does not open (61%) | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 103 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 35 | 38 | 92% (90d) | Does not open (60%) | 24% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 104 | [ ] | Forza Horizon 6 (STEAM) | 35 | 36 | 97% (90d) | Does not open (61%) | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 105 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 35 | 36 | 97% (90d) | No graphics (62%) | 6% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 106 | [ ] | Utopia Must Fall (STEAM) | 35 | 35 | 100% (90d) | Does not open (83%) | 0% | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 107 | [ ] | CPM 2 (STEAM) | 34 | 42 | 81% (90d) | Does not open (88%) | 10% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 108 | [ ] | OneShot (STEAM) | 34 | 38 | 89% (90d) | Does not open (97%) | 20% | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 109 | [ ] | Muv-Luv (STEAM) | 34 | 35 | 97% (90d) | Does not open (86%) | 35% | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 110 | [ ] | Lost Planet: Extreme Condition (STEAM) | 33 | 41 | 80% (90d) | Does not open (77%) | 48% | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 111 | [ ] | Death Stranding (EPIC) | 33 | 36 | 92% (90d) | Does not open (75%) | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 112 | [ ] | The Darkness II (STEAM) | 33 | 33 | 100% (90d) | Does not open (83%) | 23% | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 113 | [ ] | Gauntlet™  (STEAM) | 32 | 46 | 70% (90d) | Does not open (67%) | 42% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 114 | [ ] | Mass Effect (2007) (STEAM) | 32 | 38 | 84% (90d) | Does not open (81%) | 50% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 115 | [ ] | Wolfenstein 3D (STEAM) | 32 | 35 | 91% (90d) | Does not open (50%) | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 116 | [ ] | Yume Nikki (STEAM) | 31 | 53 | 73% (14d) | Does not open (90%) | 0% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 117 | [ ] | Insaniquarium! Deluxe (STEAM) | 31 | 38 | 82% (90d) | Does not open (86%) | 35% | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 118 | [ ] | Beholder (EPIC) | 31 | 36 | 86% (90d) | Does not open (65%) | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 119 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 31 | 34 | 91% (90d) | Does not open (81%) | 25% | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 120 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 31 | 34 | 91% (90d) | Does not open (67%) | 0% | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 121 | [ ] | Umamusume: Pretty Derby (STEAM) | 31 | 33 | 94% (90d) | Does not open (86%) | 55% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 122 | [ ] | Axiom Verge 2 (STEAM) | 31 | 32 | 97% (90d) | Does not open (65%) | 16% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 123 | [ ] | Rayman Legends (STEAM) | 31 | 32 | 97% (90d) | Does not open (96%) | 41% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 124 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 31 | 31 | 100% (90d) | Does not open (69%) | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 125 | [ ] | Quantum Break (STEAM) | 31 | 31 | 100% (90d) | Does not open (90%) | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 126 | [ ] | Metro: Last Light Complete Edition (STEAM) | 30 | 36 | 83% (90d) | Does not open (58%) | 59% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 127 | [ ] | Far Cry 4 (STEAM) | 30 | 34 | 88% (90d) | Does not open (100%) | 27% | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 128 | [ ] | King's Bounty: The Legend (STEAM) | 30 | 34 | 88% (90d) | Does not open (100%) | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 129 | [ ] | Magicka (STEAM) | 30 | 33 | 91% (90d) | Does not open (64%) | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 130 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 30 | 31 | 97% (90d) | Does not open (95%) | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 131 | [ ] | Grand Theft Auto III - The Definitive Edition (STEAM) | 30 | 30 | 100% (90d) | Does not open (92%) | 14% | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 132 | [ ] | Forza Horizon 5 (STEAM) | 29 | 31 | 94% (90d) | Does not open (71%) | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 133 | [ ] | Audiosurf (STEAM) | 28 | 39 | 72% (90d) | Does not open (46%) | 50% | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 134 | [ ] | Dark Sector (STEAM) | 28 | 37 | 76% (90d) | Does not open (68%) | 38% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 135 | [ ] | Borderlands 2 RU (STEAM) | 28 | 30 | 93% (90d) | Does not open (58%) | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 136 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 28 | 30 | 93% (90d) | Does not open (77%) | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 137 | [ ] | Breath of Fire IV (STEAM) | 28 | 28 | 100% (90d) | Does not open (56%) | 17% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 138 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 28 | 28 | 100% (90d) | Does not open (68%) | 0% | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 139 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 28 | 28 | 100% (90d) | Does not open (91%) | 57% | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 140 | [ ] | Mirror's Edge™ (GOG) | 27 | 38 | 71% (90d) | No graphics (62%) | 50% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 141 | [ ] | The Planet Crafter (STEAM) | 27 | 32 | 84% (90d) | Does not open (55%) | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 142 | [ ] | PAYDAY 2 (STEAM) | 27 | 30 | 90% (90d) | Does not open (78%) | 31% | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 143 | [ ] | DiRT Showdown (STEAM) | 27 | 28 | 96% (90d) | Does not open (56%) | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 144 | [ ] | Hitman: Blood Money (STEAM) | 27 | 28 | 96% (90d) | Does not open (83%) | 12% | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 145 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 27 | 28 | 96% (90d) | Does not open (81%) | 38% | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 146 | [ ] | Zuma Deluxe (STEAM) | 27 | 28 | 96% (90d) | Does not open (95%) | 27% | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 147 | [ ] | theHunter Classic (STEAM) | 27 | 27 | 100% (1.3.0) | No graphics (92%) | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 148 | [ ] | Subnautica 2 (STEAM) | 26 | 32 | 81% (90d) | Does not open (65%) | 57% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 149 | [ ] | Alpha Protocol (STEAM) | 26 | 30 | 87% (90d) | Does not open (57%) | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 150 | [ ] | Dragon Age™ Inquisition (STEAM) | 26 | 30 | 87% (90d) | Does not open (77%) | 42% | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 151 | [ ] | Northgard: Definitive Edition (STEAM) | 26 | 29 | 90% (90d) | Does not open (96%) | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 152 | [ ] | AION 2 (STEAM) | 26 | 28 | 93% (90d) | Does not open (65%) | 8% | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 153 | [ ] | Isle of Reveries (STEAM) | 26 | 27 | 96% (90d) | Does not open (95%) | 31% | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 154 | [ ] | WRC 7 (STEAM) | 26 | 27 | 96% (90d) | Does not open (71%) | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 155 | [ ] | Call of Duty® (STEAM) | 25 | 34 | 74% (90d) | Does not open (68%) | 5% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 156 | [ ] | EA SPORTS FC™ 26 (STEAM) | 25 | 33 | 76% (90d) | Does not open (75%) | n/a | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 157 | [ ] | Kenshi (STEAM) | 25 | 32 | 78% (90d) | Does not open (84%) | 11% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 158 | [ ] | Knights of Pen and Paper 2 (STEAM) | 25 | 32 | 78% (90d) | Does not open (45%) | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 159 | [ ] | Singularity™ (GOG) | 25 | 30 | 83% (90d) | Does not open (100%) | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 160 | [ ] | Bionic Commando Rearmed (STEAM) | 25 | 28 | 89% (90d) | Does not open (74%) | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 161 | [ ] | Turing Complete (STEAM) | 25 | 28 | 89% (90d) | Does not open (91%) | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 162 | [ ] | Resident Evil Requiem (STEAM) | 25 | 25 | 100% (90d) | Does not open (75%) | n/a | [#210](https://github.com/GameNative/gamenative-compat/issues/210) |
| 163 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 24 | 34 | 71% (90d) | Does not open (95%) | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 164 | [ ] | My Singing Monsters (STEAM) | 24 | 30 | 80% (90d) | Does not open (83%) | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 165 | [ ] | ENDLESS Space™ 2 (STEAM) | 24 | 29 | 83% (90d) | Does not open (93%) | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 166 | [ ] | The Swapper (STEAM) | 24 | 28 | 86% (90d) | Does not open (52%) | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 167 | [ ] | They Are Billions (STEAM) | 24 | 27 | 89% (90d) | Does not open (71%) | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 168 | [ ] | Peggle Nights (STEAM) | 24 | 26 | 92% (90d) | Does not open (94%) | 30% | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 169 | [ ] | Alien Breed: Impact (STEAM) | 24 | 25 | 96% (90d) | Does not open (87%) | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 170 | [ ] | Bingle Bingle (STEAM) | 24 | 25 | 96% (90d) | Does not open (79%) | n/a | [#225](https://github.com/GameNative/gamenative-compat/issues/225) |
| 171 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 24 | 25 | 96% (90d) | No graphics (53%) | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 172 | [ ] | The Lantern of the Laughless Saint (STEAM) | 24 | 25 | 96% (90d) | Does not open (81%) | 50% | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 173 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 24 | 24 | 100% (90d) | Does not open (56%) | 9% | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 174 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 23 | 32 | 72% (90d) | No graphics (57%) | 11% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 175 | [ ] | Transformers: Fall of Cybertron (STEAM) | 23 | 30 | 77% (90d) | Does not open (63%) | 30% | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 176 | [ ] | SimCity 4 Deluxe (STEAM) | 23 | 27 | 85% (90d) | Does not open (82%) | 45% | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 177 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 23 | 26 | 88% (90d) | Does not open (95%) | 50% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 178 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 23 | 25 | 92% (90d) | Does not open (63%) | 50% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 179 | [ ] | PRAGMATA (STEAM) | 23 | 24 | 96% (90d) | Does not open (79%) | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 180 | [ ] | Euro Truck Simulator (STEAM) | 23 | 23 | 100% (90d) | Does not open (93%) | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 181 | [ ] | Gears 5 (STEAM) | 23 | 23 | 100% (90d) | Does not open (88%) | n/a | [#264](https://github.com/GameNative/gamenative-compat/issues/264) |
| 182 | [ ] | Marie's Adventure (STEAM) | 23 | 23 | 100% (90d) | Does not open (100%) | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 183 | [ ] | Spiral Knights (STEAM) | 23 | 23 | 100% (90d) | Does not open (72%) | n/a | [#263](https://github.com/GameNative/gamenative-compat/issues/263) |
| 184 | [ ] | SOMA (STEAM) | 22 | 30 | 73% (90d) | Does not open (79%) | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 185 | [ ] | Half-Life: Blue Shift (STEAM) | 22 | 26 | 85% (90d) | Does not open (85%) | 18% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 186 | [ ] | Tom Clancy's Ghost Recon® Wildlands (STEAM) | 22 | 26 | 85% (90d) | Does not open (94%) | n/a | [#280](https://github.com/GameNative/gamenative-compat/issues/280) |
| 187 | [ ] | skate.™ (EPIC) | 22 | 25 | 88% (90d) | Does not open (88%) | 8% | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 188 | [ ] | Wallachia: Reign of Dracula (STEAM) | 22 | 23 | 96% (90d) | No graphics (95%) | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 189 | [ ] | TEKKEN 8 (STEAM) | 21 | 28 | 75% (90d) | Does not open (76%) | 54% | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 190 | [ ] | Aggelos 2 (STEAM) | 21 | 27 | 78% (90d) | No graphics (90%) | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 191 | [ ] | Beyond Good & Evil™ (GOG) | 21 | 26 | 81% (90d) | Does not open (100%) | 20% | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 192 | [ ] | Sapphire Safari (GOG) | 21 | 26 | 81% (90d) | Does not open (89%) | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 193 | [ ] | Marvel's Midnight Suns (STEAM) | 21 | 24 | 88% (90d) | Does not open (84%) | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 194 | [ ] | Wuthering Waves (STEAM) | 21 | 23 | 91% (90d) | Does not open (85%) | n/a | [#216](https://github.com/GameNative/gamenative-compat/issues/216) |
| 195 | [ ] | Mirror's Edge™ Catalyst (STEAM) | 21 | 22 | 95% (90d) | Does not open (68%) | 59% | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 196 | [ ] | Resident Evil 3 Nemesis (1999) (STEAM) | 21 | 21 | 100% (90d) | Does not open (86%) | n/a | [#273](https://github.com/GameNative/gamenative-compat/issues/273) |
| 197 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 21 | 21 | 100% (90d) | Does not open (71%) | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 198 | [ ] | Beat Cop (STEAM) | 20 | 28 | 71% (90d) | Does not open (74%) | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 199 | [ ] | Fishing Planet (STEAM) | 20 | 28 | 71% (90d) | Does not open (93%) | 33% | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 200 | [ ] | Surviving Mars (STEAM) | 20 | 26 | 77% (90d) | Does not open (92%) | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 201 | [ ] | PICO PARK:Classic Edition (STEAM) | 20 | 24 | 83% (90d) | Does not open (89%) | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 202 | [ ] | Halo: Spartan Assault (STEAM) | 20 | 23 | 87% (90d) | Does not open (82%) | 38% | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 203 | [ ] | Apex Legends (STEAM) | 20 | 22 | 91% (90d) | Does not open (72%) | n/a | [#261](https://github.com/GameNative/gamenative-compat/issues/261) |
| 204 | [ ] | No More Room in Hell (STEAM) | 20 | 21 | 95% (90d) | Does not open (94%) | n/a | [#365](https://github.com/GameNative/gamenative-compat/issues/365) |
| 205 | [ ] | Pathway (EPIC) | 20 | 21 | 95% (90d) | Does not open (61%) | n/a | [#298](https://github.com/GameNative/gamenative-compat/issues/298) |
| 206 | [ ] | The Last of Us™ Part I (STEAM) | 20 | 21 | 95% (90d) | Does not open (93%) | n/a | [#300](https://github.com/GameNative/gamenative-compat/issues/300) |
| 207 | [ ] | Grounded 2 (STEAM) | 20 | 20 | 100% (90d) | Does not open (56%) | n/a | [#317](https://github.com/GameNative/gamenative-compat/issues/317) |
| 208 | [ ] | Return to Castle Wolfenstein (STEAM) | 20 | 20 | 100% (90d) | Does not open (95%) | 25% | [#321](https://github.com/GameNative/gamenative-compat/issues/321) |
| 209 | [ ] | Dungeon Keeper™ 2 (GOG) | 19 | 26 | 73% (90d) | Does not open (100%) | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 210 | [ ] | Mafia III: Definitive Edition (STEAM) | 19 | 22 | 86% (90d) | Does not open (95%) | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 211 | [ ] | The Elder Scrolls IV: Oblivion Remastered (STEAM) | 19 | 22 | 86% (90d) | Does not open (59%) | n/a | [#312](https://github.com/GameNative/gamenative-compat/issues/312) |
| 212 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 19 | 22 | 86% (90d) | Does not open (79%) | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 213 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 21 | 90% (90d) | Does not open (82%) | 0% | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 214 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 21 | 90% (90d) | Does not open (89%) | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 215 | [ ] | GT Legends (STEAM) | 19 | 20 | 95% (90d) | Does not open (89%) | n/a | [#364](https://github.com/GameNative/gamenative-compat/issues/364) |
| 216 | [ ] | Jurassic World Evolution (EPIC) | 19 | 20 | 95% (90d) | Does not open (80%) | n/a | [#469](https://github.com/GameNative/gamenative-compat/issues/469) |
| 217 | [ ] | Melatonin (STEAM) | 19 | 20 | 95% (90d) | Does not open (59%) | 46% | [#272](https://github.com/GameNative/gamenative-compat/issues/272) |
| 218 | [ ] | Rayman Legends (EPIC) | 19 | 20 | 95% (90d) | Does not open (92%) | n/a | [#286](https://github.com/GameNative/gamenative-compat/issues/286) |
| 219 | [ ] | Zenless Zone Zero (STEAM) | 19 | 20 | 95% (90d) | Does not open (76%) | n/a | [#369](https://github.com/GameNative/gamenative-compat/issues/369) |
| 220 | [ ] | Fogpiercer (STEAM) | 18 | 25 | 72% (90d) | Does not open (78%) | n/a | [#303](https://github.com/GameNative/gamenative-compat/issues/303) |
| 221 | [ ] | We Were Here Together (EPIC) | 18 | 24 | 75% (90d) | Does not open (82%) | n/a | [#374](https://github.com/GameNative/gamenative-compat/issues/374) |
| 222 | [ ] | Hitman 2: Silent Assassin (STEAM) | 18 | 23 | 78% (90d) | Does not open (83%) | 50% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 223 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 18 | 23 | 78% (90d) | Does not open (100%) | 42% | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 224 | [ ] | Yakuza 0 (GOG) | 18 | 23 | 78% (90d) | Does not open (67%) | 45% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 225 | [ ] | Bright Memory (STEAM) | 18 | 21 | 86% (90d) | No graphics (83%) | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 226 | [ ] | Lay of the Land (STEAM) | 18 | 20 | 90% (90d) | No graphics (61%) | n/a | [#477](https://github.com/GameNative/gamenative-compat/issues/477) |
| 227 | [ ] | Carnal Instinct (STEAM) | 17 | 24 | 71% (90d) | Does not open (57%) | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 228 | [ ] | SlashZero Demo (STEAM) | 17 | 23 | 74% (90d) | Does not open (75%) | 40% | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 229 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 17 | 22 | 77% (90d) | Does not open (87%) | 44% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 230 | [ ] | Clive Barker's Undying (GOG) | 17 | 20 | 85% (90d) | Does not open (75%) | n/a | [#388](https://github.com/GameNative/gamenative-compat/issues/388) |
| 231 | [ ] | GRADIUS origin collection (STEAM) | 17 | 20 | 85% (90d) | Controller issues (71%) | n/a | [#479](https://github.com/GameNative/gamenative-compat/issues/479) |
| 232 | [ ] | NBA 2K26 (STEAM) | 17 | 20 | 85% (90d) | Does not open (82%) | n/a | [#384](https://github.com/GameNative/gamenative-compat/issues/384) |
| 233 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (90d) | Does not open (82%) | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 234 | [ ] | Tyrian 2000 (GOG) | 17 | 20 | 85% (90d) | Does not open (86%) | n/a | [#360](https://github.com/GameNative/gamenative-compat/issues/360) |
| 235 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 16 | 23 | 70% (90d) | No graphics (56%) | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 236 | [ ] | Legend of Grimrock 2 (STEAM) | 16 | 23 | 70% (90d) | Does not open (92%) | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 237 | [ ] | Re-Volt (STEAM) | 16 | 22 | 73% (90d) | Controller issues (71%) | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 238 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 21 | 76% (90d) | Does not open (82%) | 44% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 239 | [ ] | Bejeweled 2 Deluxe (STEAM) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#329](https://github.com/GameNative/gamenative-compat/issues/329) |
| 240 | [ ] | EVE Online (STEAM) | 16 | 20 | 80% (90d) | No graphics (57%) | 55% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 241 | [ ] | F.E.A.R. 2: Project Origin + Reborn (GOG) | 16 | 20 | 80% (90d) | Does not open (100%) | n/a | [#478](https://github.com/GameNative/gamenative-compat/issues/478) |
| 242 | [ ] | Genshin Impact (EPIC) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#326](https://github.com/GameNative/gamenative-compat/issues/326) |
| 243 | [ ] | Sacred Gold (STEAM) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 244 | [ ] | shapez (STEAM) | 16 | 20 | 80% (90d) | No graphics (67%) | n/a | [#332](https://github.com/GameNative/gamenative-compat/issues/332) |
| 245 | [ ] | DayZ (STEAM) | 15 | 21 | 71% (90d) | Does not open (56%) | 57% | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 246 | [ ] | Fallout Classic (GOG) | 15 | 21 | 71% (90d) | Does not open (71%) | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 247 | [ ] | Smushi Come Home (GOG) | 15 | 21 | 71% (90d) | Does not open (57%) | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 248 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 15 | 21 | 71% (90d) | Does not open (70%) | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 249 | [ ] | Make Way (EPIC) | 15 | 20 | 75% (90d) | Does not open (79%) | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 250 | [ ] | Spark the Electric Jester (STEAM) | 15 | 20 | 75% (90d) | Does not open (62%) | 55% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |

## Probably does not work (68)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | Garry's Mod (STEAM) | 198 | 316 | 67% (1.3.0) | Does not open (79%) | 59% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 2 | [ ] | Metro 2033 Redux (STEAM) | 151 | 341 | 66% (1.3.0) | Does not open (70%) | 50% |  |
| 3 | [ ] | Prototype (STEAM) | 151 | 215 | 52% (1.3.0) | Does not open (76%) | 45% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 4 | [ ] | Geometry Dash (STEAM) | 141 | 419 | 66% (1.3.0) | Does not open (71%) | 40% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 5 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 137 | 200 | 69% (90d) | Does not open (80%) | n/a |  |
| 6 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 136 | 170 | 52% (1.3.0) | Does not open (93%) | 40% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 7 | [ ] | VRChat (STEAM) | 91 | 138 | 55% (1.3.0) | Does not open (65%) | 40% |  |
| 8 | [ ] | Gorilla Tag (STEAM) | 72 | 121 | 68% (1.3.0) | Does not open (70%) | 22% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 9 | [ ] | Hollow Knight: Silksong (GOG) | 69 | 108 | 64% (90d) | Does not open (67%) | 48% |  |
| 10 | [ ] | Firewatch (STEAM) | 65 | 113 | 58% (90d) | Does not open (90%) | 55% |  |
| 11 | [ ] | Oxygen Not Included (STEAM) | 54 | 87 | 62% (90d) | Does not open (76%) | 50% |  |
| 12 | [ ] | Breathedge (STEAM) | 51 | 75 | 68% (90d) | Does not open (61%) | 40% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 13 | [ ] | VALORANT (EPIC) | 45 | 69 | 65% (90d) | Does not open (87%) | 17% |  |
| 14 | [ ] | Plague Inc: Evolved (STEAM) | 44 | 66 | 67% (90d) | Does not open (67%) | 55% |  |
| 15 | [ ] | Frostpunk (STEAM) | 41 | 66 | 62% (90d) | No graphics (77%) | 47% |  |
| 16 | [ ] | Fallout (GOG) | 40 | 61 | 66% (90d) | Does not open (72%) | 48% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 17 | [ ] | Age of Empires II (2013) (STEAM) | 39 | 68 | 57% (90d) | Does not open (46%) | 53% |  |
| 18 | [ ] | Grim Dawn (GOG) | 38 | 62 | 61% (90d) | Does not open (65%) | 46% | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 19 | [ ] | XCOM 2 (STEAM) | 35 | 54 | 65% (90d) | Does not open (57%) | n/a |  |
| 20 | [ ] | Sol Cesto (STEAM) | 34 | 52 | 65% (90d) | Does not open (71%) | 53% |  |
| 21 | [ ] | Deponia (STEAM) | 33 | 61 | 54% (90d) | Does not open (48%) | 57% |  |
| 22 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 32 | 57 | 56% (90d) | Does not open (95%) | 43% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 23 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 31 | 57 | 54% (90d) | Does not open (66%) | 47% |  |
| 24 | [ ] | Mafia II (Classic) (GOG) | 31 | 45 | 69% (90d) | Does not open (96%) | 26% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 25 | [ ] | Soul's Remnant (STEAM) | 27 | 49 | 55% (90d) | Does not open (55%) | n/a |  |
| 26 | [ ] | Lucid Blocks (STEAM) | 27 | 46 | 59% (90d) | Does not open (83%) | 59% |  |
| 27 | [ ] | Crazy Taxi (STEAM) | 25 | 43 | 58% (90d) | Does not open (63%) | 55% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 28 | [ ] | Chained Echoes (GOG) | 24 | 48 | 50% (90d) | Does not open (62%) | 50% |  |
| 29 | [ ] | Strider (STEAM) | 24 | 37 | 65% (90d) | Does not open (100%) | 35% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 30 | [ ] | Invisible, Inc. (STEAM) | 22 | 38 | 58% (90d) | Does not open (65%) | 55% |  |
| 31 | [ ] | Cities: Skylines (STEAM) | 22 | 33 | 67% (90d) | Does not open (67%) | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 32 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 21 | 36 | 58% (90d) | Does not open (58%) | 47% |  |
| 33 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 20 | 32 | 63% (90d) | Does not open (81%) | n/a |  |
| 34 | [ ] | Warhammer 40,000: Boltgun (GOG) | 19 | 29 | 66% (90d) | Does not open (92%) | 56% |  |
| 35 | [ ] | Turnip Boy Robs a Bank (EPIC) | 19 | 28 | 68% (90d) | Does not open (65%) | 41% | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 36 | [ ] | Need for Speed: Undercover (STEAM) | 18 | 29 | 62% (90d) | Does not open (93%) | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 37 | [ ] | Another World: 20th Anniversary Edition (GOG) | 18 | 28 | 64% (90d) | Does not open (67%) | n/a |  |
| 38 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 17 | 27 | 63% (90d) | Does not open (80%) | n/a |  |
| 39 | [ ] | Assassin's Creed Odyssey (STEAM) | 17 | 26 | 65% (90d) | Does not open (77%) | n/a | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 40 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 16 | 29 | 55% (90d) | Does not open (87%) | 27% |  |
| 41 | [ ] | Guacamelee! Gold Edition (STEAM) | 16 | 27 | 59% (90d) | Does not open (93%) | n/a | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 42 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 25 | 64% (90d) | Directx error (57%) | n/a |  |
| 43 | [ ] | War of Dots (STEAM) | 16 | 25 | 64% (90d) | Does not open (75%) | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 44 | [ ] | Race The Sun (STEAM) | 15 | 30 | 50% (90d) | No graphics (92%) | 57% |  |
| 45 | [ ] | Odallus: The Dark Call (STEAM) | 15 | 27 | 56% (90d) | No graphics (57%) | n/a | [#337](https://github.com/GameNative/gamenative-compat/issues/337) |
| 46 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 15 | 27 | 56% (90d) | Does not open (64%) | 0% |  |
| 47 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 15 | 26 | 58% (90d) | Does not open (85%) | 52% |  |
| 48 | [ ] | Ys: Memories of Celceta (STEAM) | 15 | 24 | 63% (90d) | No graphics (45%) | 31% |  |
| 49 | [ ] | Blood Omen: Legacy of Kain (GOG) | 15 | 23 | 65% (90d) | Does not open (64%) | 45% |  |
| 50 | [ ] | Yuppie Psycho (STEAM) | 15 | 22 | 68% (90d) | Does not open (71%) | 18% | [#325](https://github.com/GameNative/gamenative-compat/issues/325) |
| 51 | [ ] | Evoland (STEAM) | 14 | 28 | 50% (90d) | Controller issues (69%) | n/a |  |
| 52 | [ ] | Blaster Master Zero (STEAM) | 14 | 25 | 56% (90d) | Does not open (64%) | 38% |  |
| 53 | [ ] | Katana ZERO (GOG) | 14 | 25 | 56% (90d) | Does not open (85%) | 33% |  |
| 54 | [ ] | Alan Wake's American Nightmare (EPIC) | 13 | 24 | 54% (90d) | Does not open (83%) | 50% |  |
| 55 | [ ] | Asterigos: Curse of the Stars (STEAM) | 13 | 23 | 57% (90d) | Graphics glitches (50%) | n/a |  |
| 56 | [ ] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 13 | 23 | 57% (90d) | Does not open (100%) | 12% |  |
| 57 | [ ] | Trials Survivors (STEAM) | 13 | 23 | 57% (90d) | Does not open (67%) | n/a |  |
| 58 | [ ] | Evenicle (STEAM) | 13 | 22 | 59% (90d) | Graphics glitches (77%) | n/a |  |
| 59 | [ ] | Drop Duchy (EPIC) | 13 | 21 | 62% (90d) | Does not open (100%) | 18% |  |
| 60 | [ ] | The Stanley Parable (STEAM) | 13 | 21 | 62% (90d) | Does not open (89%) | 50% |  |
| 61 | [ ] | Buck Up And Drive! (STEAM) | 13 | 20 | 65% (90d) | Does not open (67%) | n/a |  |
| 62 | [ ] | Revolution Idle (STEAM) | 12 | 24 | 50% (90d) | No graphics (50%) | n/a |  |
| 63 | [ ] | A Plague Tale: Innocence (GOG) | 12 | 23 | 52% (90d) | Does not open (91%) | 57% |  |
| 64 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 12 | 22 | 55% (90d) | Does not open (73%) | n/a |  |
| 65 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (90d) | Does not open (82%) | n/a |  |
| 66 | [ ] | Crying Suns (EPIC) | 11 | 22 | 50% (90d) | No graphics (57%) | n/a |  |
| 67 | [ ] | DYNASTY WARRIORS: ORIGINS (STEAM) | 10 | 20 | 50% (90d) | Does not open (60%) | n/a |  |
| 68 | [ ] | F1 2015 (STEAM) | 10 | 20 | 50% (90d) | Does not open (50%) | n/a |  |

## Works, but the first launch usually fails (375)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 1315 | 1663 | 75% (1.3.0) | Does not open (83%) | 77% |  |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 568 | 719 | 78% (1.3.0) | Does not open (64%) | 91% |  |
| 3 | [ ] | Grim Dawn (STEAM) | 563 | 618 | 64% (1.3.0) | Does not open (74%) | 62% |  |
| 4 | [ ] | Terraria (STEAM) | 484 | 755 | 60% (1.3.0) | No graphics (51%) | 75% |  |
| 5 | [ ] | KINGDOM HEARTS -HD 1.5+2.5 ReMIX- (STEAM) | 472 | 948 | 55% (1.3.0) | Does not open (80%) | 94% |  |
| 6 | [ ] | No Man's Sky (STEAM) | 368 | 645 | 54% (1.3.0) | Controller issues (61%) | 86% |  |
| 7 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 367 | 552 | 67% (1.3.0) | Does not open (55%) | 84% |  |
| 8 | [ ] | Half-Life (STEAM) | 352 | 618 | 51% (1.3.0) | Does not open (58%) | 76% |  |
| 9 | [ ] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 253 | 295 | 86% (90d) | Does not open (87%) | 65% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 10 | [ ] | Cyberpunk 2077 (STEAM) | 245 | 430 | 51% (1.3.0) | Does not open (68%) | 77% |  |
| 11 | [ ] | Welcome to Elderfield (STEAM) | 236 | 282 | 61% (1.3.0) | Does not open (72%) | 73% |  |
| 12 | [ ] | Grand Theft Auto V Legacy (STEAM) | 229 | 290 | 69% (1.3.0) | Does not open (89%) | 79% |  |
| 13 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 225 | 317 | 71% (90d) | Does not open (61%) | 88% |  |
| 14 | [ ] | BeamNG.drive (STEAM) | 214 | 262 | 88% (1.3.0) | Does not open (83%) | 93% |  |
| 15 | [ ] | Palworld (STEAM) | 205 | 405 | 52% (1.3.0) | Does not open (72%) | 87% |  |
| 16 | [ ] | OMORI (STEAM) | 203 | 246 | 83% (90d) | Does not open (64%) | 78% |  |
| 17 | [ ] | MONSTER HUNTER RISE (STEAM) | 201 | 504 | 50% (1.3.0) | Does not open (81%) | 70% |  |
| 18 | [ ] | DRAGON BALL FighterZ (STEAM) | 201 | 231 | 72% (1.3.0) | Does not open (89%) | 62% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 19 | [ ] | Devil May Cry HD Collection (STEAM) | 200 | 282 | 75% (1.3.0) | Does not open (86%) | 76% |  |
| 20 | [ ] | ELDEN RING (STEAM) | 198 | 295 | 69% (1.3.0) | Does not open (86%) | 72% |  |
| 21 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 193 | 362 | 60% (1.3.0) | Does not open (57%) | 82% |  |
| 22 | [ ] | DREDGE (EPIC) | 173 | 221 | 62% (1.3.0) | Does not open (67%) | 87% |  |
| 23 | [ ] | Rocket League® (EPIC) | 156 | 259 | 52% (1.3.0) | Does not open (73%) | 75% |  |
| 24 | [ ] | Monster Hunter: World (STEAM) | 146 | 274 | 55% (1.3.0) | No graphics (55%) | 83% |  |
| 25 | [ ] | Noita (STEAM) | 144 | 219 | 53% (1.3.0) | Does not open (54%) | 79% |  |
| 26 | [ ] | Team Fortress 2 (STEAM) | 142 | 230 | 71% (1.3.0) | Does not open (68%) | 79% |  |
| 27 | [ ] | Borderlands 2 (EPIC) | 142 | 169 | 80% (1.3.0) | Does not open (83%) | 63% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 28 | [ ] | Castlevania Advance Collection (STEAM) | 133 | 204 | 71% (1.3.0) | Controller issues (95%) | 97% |  |
| 29 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 133 | 152 | 90% (1.3.0) | Does not open (86%) | 77% |  |
| 30 | [ ] | Far Cry® 3 (STEAM) | 129 | 144 | 90% (90d) | Does not open (82%) | 66% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 31 | [ ] | Minecraft Dungeons II (STEAM) | 124 | 142 | 87% (90d) | Does not open (83%) | 64% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 32 | [ ] | Castlevania Dominus Collection (STEAM) | 122 | 180 | 76% (1.3.0) | Controller issues (92%) | 98% |  |
| 33 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 120 | 152 | 68% (1.3.0) | Does not open (71%) | 64% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 34 | [ ] | Devil May Cry 5 (STEAM) | 118 | 186 | 70% (1.3.0) | Does not open (81%) | 67% |  |
| 35 | [ ] | Fallout: New Vegas (EPIC) | 118 | 144 | 73% (1.3.0) | Does not open (58%) | 92% |  |
| 36 | [ ] | Cave Story+ (STEAM) | 118 | 130 | 91% (90d) | Does not open (64%) | 94% |  |
| 37 | [ ] | Touhou Koumakyou: New Classic - the Embodiment of Scarlet Devil (STEAM) | 117 | 181 | 65% (90d) | Does not open (78%) | 81% |  |
| 38 | [ ] | Caravan SandWitch (EPIC) | 116 | 180 | 50% (1.3.0) | Does not open (92%) | 81% |  |
| 39 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 116 | 163 | 79% (1.3.0) | Does not open (76%) | 62% |  |
| 40 | [ ] | The Witcher: Enhanced Edition (STEAM) | 113 | 130 | 87% (90d) | Does not open (59%) | 61% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 41 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 109 | 145 | 75% (90d) | Does not open (85%) | 85% |  |
| 42 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 105 | 154 | 64% (1.3.0) | Does not open (73%) | 75% |  |
| 43 | [ ] | Aniimo (STEAM) | 105 | 143 | 73% (90d) | Does not open (77%) | 91% |  |
| 44 | [ ] | Moonstone Island (STEAM) | 103 | 136 | 76% (90d) | Controller issues (57%) | 88% |  |
| 45 | [ ] | Happy Wheels (STEAM) | 95 | 115 | 83% (90d) | No graphics (53%) | 80% |  |
| 46 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 94 | 122 | 77% (90d) | Controller issues (86%) | 97% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 47 | [ ] | Sovereign Tower (STEAM) | 92 | 150 | 61% (90d) | Does not open (83%) | 84% |  |
| 48 | [ ] | Fallout: New Vegas PCR (STEAM) | 91 | 121 | 75% (90d) | Does not open (89%) | 70% |  |
| 49 | [ ] | STEINS;GATE (STEAM) | 86 | 120 | 72% (90d) | Does not open (90%) | 90% |  |
| 50 | [ ] | Vital Shell (STEAM) | 85 | 129 | 66% (90d) | Does not open (52%) | 85% |  |
| 51 | [ ] | Hogwarts Legacy (STEAM) | 83 | 145 | 51% (1.3.0) | Does not open (59%) | 67% |  |
| 52 | [ ] | Cry of Fear (STEAM) | 82 | 163 | 72% (1.3.0) | Does not open (50%) | 85% |  |
| 53 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 82 | 84 | 98% (90d) | Does not open (91%) | 60% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 54 | [ ] | Sol Cesto (EPIC) | 79 | 84 | 94% (90d) | Does not open (77%) | 64% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 55 | [ ] | Detroit: Become Human (STEAM) | 77 | 80 | 96% (90d) | Does not open (71%) | 65% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 56 | [ ] | The Sims™ 4 (STEAM) | 76 | 98 | 78% (90d) | Does not open (89%) | 69% |  |
| 57 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 74 | 124 | 60% (90d) | Controller issues (59%) | 94% |  |
| 58 | [ ] | Mega Man Zero/ZX Legacy Collection (STEAM) | 73 | 102 | 72% (90d) | Does not open (85%) | 82% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 59 | [ ] | Sid Meier's Civilization VI (STEAM) | 72 | 127 | 54% (1.3.0) | Does not open (70%) | 90% |  |
| 60 | [ ] | Ballionaire (STEAM) | 71 | 109 | 50% (1.3.0) | Does not open (77%) | 96% |  |
| 61 | [ ] | Antivirus Survivors 2003 Professional (STEAM) | 71 | 104 | 68% (90d) | Does not open (61%) | 93% |  |
| 62 | [ ] | Darksiders (STEAM) | 71 | 86 | 83% (90d) | Does not open (68%) | 88% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 63 | [ ] | Dota 2 (STEAM) | 70 | 106 | 59% (1.3.0) | Does not open (76%) | 70% |  |
| 64 | [ ] | Disgaea 5 Complete (STEAM) | 70 | 84 | 83% (90d) | Does not open (75%) | 98% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 65 | [ ] | Alabaster Dawn (STEAM) | 69 | 123 | 56% (90d) | Controller issues (51%) | 91% |  |
| 66 | [ ] | American Truck Simulator (STEAM) | 68 | 109 | 76% (1.3.0) | Does not open (74%) | 79% |  |
| 67 | [ ] | Fallout (STEAM) | 68 | 106 | 64% (90d) | Does not open (70%) | 71% |  |
| 68 | [ ] | Dungeons & Degenerate Gamblers (STEAM) | 68 | 93 | 54% (1.3.0) | Does not open (90%) | 99% |  |
| 69 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 68 | 79 | 95% (1.3.0) | Does not open (88%) | 97% |  |
| 70 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 67 | 105 | 64% (90d) | Does not open (72%) | 72% |  |
| 71 | [ ] | Gunfire Reborn (STEAM) | 67 | 73 | 92% (90d) | Does not open (81%) | 94% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 72 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 66 | 121 | 52% (1.3.0) | Does not open (67%) | 62% |  |
| 73 | [ ] | Fable - The Lost Chapters (STEAM) | 66 | 105 | 52% (1.3.0) | Graphics glitches (52%) | 79% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 74 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 65 | 87 | 61% (1.3.0) | Does not open (50%) | 92% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 75 | [ ] | Cyberpunk 2077 (GOG) | 65 | 81 | 80% (90d) | Does not open (76%) | 77% |  |
| 76 | [ ] | Call of Juarez Gunslinger (STEAM) | 65 | 80 | 81% (90d) | Does not open (90%) | 76% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 77 | [ ] | Sonic Lost World (STEAM) | 64 | 108 | 59% (90d) | No graphics (61%) | 88% |  |
| 78 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 64 | 86 | 74% (90d) | Does not open (47%) | 61% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 79 | [ ] | Poppy Playtime (STEAM) | 63 | 110 | 57% (90d) | Does not open (68%) | 78% |  |
| 80 | [ ] | Borderlands: The Pre-Sequel (STEAM) | 63 | 89 | 71% (90d) | Does not open (77%) | 63% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 81 | [ ] | MIO: Memories in Orbit (STEAM) | 62 | 117 | 66% (1.3.0) | Graphics glitches (53%) | 96% |  |
| 82 | [ ] | Red Dead Redemption 2 (STEAM) | 60 | 80 | 60% (1.3.0) | Does not open (98%) | 81% |  |
| 83 | [ ] | A Plague Tale: Innocence (STEAM) | 60 | 63 | 95% (90d) | Does not open (88%) | 73% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 84 | [ ] | The Binding of Isaac (STEAM) | 59 | 134 | 63% (1.3.0) | Controller issues (91%) | 93% |  |
| 85 | [ ] | Mini Motorways (STEAM) | 59 | 102 | 58% (90d) | Does not open (76%) | 61% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 86 | [ ] | Big Walk (STEAM) | 59 | 91 | 65% (90d) | Does not open (68%) | 82% |  |
| 87 | [ ] | eFootball™ (STEAM) | 59 | 87 | 68% (90d) | Does not open (55%) | 75% |  |
| 88 | [ ] | Call of Duty: World at War (STEAM) | 58 | 83 | 70% (90d) | Does not open (42%) | 73% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 89 | [ ] | Borderlands 3 (STEAM) | 58 | 78 | 74% (90d) | Does not open (91%) | 94% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 90 | [ ] | Sonic Generations (STEAM) | 58 | 68 | 85% (90d) | Does not open (70%) | 62% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 91 | [ ] | Starbound (STEAM) | 57 | 87 | 54% (1.3.0) | Does not open (68%) | 69% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 92 | [ ] | Deskrawl: Idle ARPG (STEAM) | 57 | 68 | 86% (1.3.0) | Does not open (60%) | 80% |  |
| 93 | [ ] | Dead by Daylight (STEAM) | 57 | 62 | 92% (90d) | Does not open (83%) | 81% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 94 | [ ] | The Secret of Monkey Island: Special Edition (STEAM) | 56 | 86 | 65% (90d) | Does not open (92%) | 71% |  |
| 95 | [ ] | Prey (STEAM) | 55 | 93 | 59% (90d) | Does not open (63%) | 84% |  |
| 96 | [ ] | Sonic Adventure DX (STEAM) | 55 | 89 | 62% (90d) | Does not open (86%) | 64% |  |
| 97 | [ ] | TBH: Task Bar Hero (STEAM) | 55 | 85 | 65% (90d) | Does not open (74%) | 94% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 98 | [ ] | Resident Evil 6 (STEAM) | 54 | 129 | 73% (1.3.0) | Does not open (57%) | 89% |  |
| 99 | [ ] | MapleStory (STEAM) | 54 | 56 | 91% (1.3.0) | Does not open (76%) | 75% |  |
| 100 | [ ] | Until Then (STEAM) | 53 | 92 | 58% (90d) | Does not open (73%) | 96% |  |
| 101 | [ ] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 53 | 90 | 59% (90d) | Does not open (62%) | 61% |  |
| 102 | [ ] | Path of Exile (STEAM) | 53 | 62 | 85% (90d) | Does not open (91%) | 86% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 103 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 53 | 57 | 93% (90d) | Does not open (83%) | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 104 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 52 | 77 | 76% (1.3.0) | Does not open (60%) | 65% |  |
| 105 | [ ] | Vampire Survivors (EPIC) | 52 | 74 | 70% (90d) | Does not open (63%) | 60% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 106 | [ ] | Guildrun Demo (STEAM) | 52 | 73 | 71% (90d) | No graphics (65%) | 73% |  |
| 107 | [ ] | A Plague Tale: Innocence (EPIC) | 51 | 87 | 59% (90d) | Does not open (71%) | 89% |  |
| 108 | [ ] | The Bazaar (STEAM) | 51 | 82 | 62% (90d) | Does not open (72%) | 86% |  |
| 109 | [ ] | Ace Attorney Investigations Collection (STEAM) | 51 | 81 | 63% (90d) | Does not open (96%) | 92% |  |
| 110 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 51 | 59 | 86% (90d) | Does not open (80%) | 82% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 111 | [ ] | Marvel’s Spider-Man Remastered (STEAM) | 50 | 120 | 57% (1.3.0) | Does not open (48%) | 63% |  |
| 112 | [ ] | 7 Days to Die (STEAM) | 50 | 107 | 58% (1.3.0) | Does not open (74%) | 72% |  |
| 113 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 50 | 64 | 78% (90d) | Does not open (90%) | 61% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 114 | [ ] | DOOM 3 (STEAM) | 50 | 55 | 91% (90d) | Does not open (92%) | 60% | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 115 | [ ] | Dead Space (STEAM) | 49 | 62 | 79% (90d) | Does not open (54%) | 78% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 116 | [ ] | Sheepy: A Short Adventure (STEAM) | 49 | 59 | 83% (90d) | Does not open (52%) | 80% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 117 | [ ] | Sleeping Dogs™ (STEAM) | 49 | 56 | 88% (90d) | Does not open (87%) | 77% | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 118 | [ ] | Darkest Dungeon® (EPIC) | 48 | 88 | 56% (1.3.0) | Does not open (64%) | 61% |  |
| 119 | [ ] | Last Epoch (STEAM) | 48 | 71 | 71% (1.3.0) | Does not open (79%) | 100% |  |
| 120 | [ ] | Rivals of Aether II (STEAM) | 48 | 70 | 69% (90d) | Does not open (55%) | 73% |  |
| 121 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 48 | 69 | 70% (90d) | Does not open (83%) | 60% |  |
| 122 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 78 | 60% (90d) | Controller issues (54%) | 95% |  |
| 123 | [ ] | Watch_Dogs 2 (STEAM) | 47 | 52 | 90% (90d) | Does not open (97%) | 61% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 124 | [ ] | Moonlighter (EPIC) | 47 | 51 | 92% (90d) | No graphics (79%) | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 125 | [ ] | Digimon World: Next Order (STEAM) | 46 | 86 | 53% (90d) | Controller issues (80%) | 95% |  |
| 126 | [ ] | Tomb Raider: Anniversary (STEAM) | 46 | 65 | 71% (90d) | Does not open (95%) | 60% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 127 | [ ] | Grand Theft Auto V (EPIC) | 46 | 51 | 90% (90d) | Does not open (89%) | 84% |  |
| 128 | [ ] | Resident Evil 7 Biohazard (STEAM) | 44 | 70 | 71% (1.3.0) | Does not open (78%) | 83% |  |
| 129 | [ ] | Street Fighter™ 6 (STEAM) | 44 | 70 | 63% (90d) | Does not open (84%) | 79% |  |
| 130 | [ ] | Aggelos (STEAM) | 44 | 58 | 76% (90d) | No graphics (78%) | 95% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 131 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 43 | 77 | 56% (90d) | Controller issues (51%) | 87% |  |
| 132 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 42 | 77 | 71% (1.3.0) | Controller issues (47%) | 89% |  |
| 133 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 42 | 69 | 61% (90d) | Does not open (67%) | 78% |  |
| 134 | [ ] | Deadlock (STEAM) | 42 | 63 | 67% (90d) | Does not open (45%) | 94% |  |
| 135 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 42 | 63 | 67% (90d) | Does not open (73%) | 69% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 136 | [ ] | FINAL FANTASY VII (2013) (STEAM) | 42 | 61 | 69% (90d) | Does not open (83%) | 79% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 137 | [ ] | Forza Horizon 4 (STEAM) | 42 | 58 | 72% (90d) | Does not open (53%) | 87% |  |
| 138 | [ ] | Amnesia: The Dark Descent (STEAM) | 41 | 76 | 54% (90d) | Does not open (85%) | 75% |  |
| 139 | [ ] | Sonic Origins (STEAM) | 41 | 72 | 57% (90d) | Does not open (69%) | 83% |  |
| 140 | [ ] | Your Only Move Is HUSTLE (STEAM) | 40 | 80 | 50% (90d) | Does not open (64%) | 89% |  |
| 141 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 40 | 41 | 98% (90d) | Does not open (62%) | 85% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 142 | [ ] | Salt and Sanctuary (STEAM) | 39 | 78 | 50% (90d) | Does not open (74%) | 81% |  |
| 143 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 39 | 74 | 53% (90d) | No graphics (83%) | 98% |  |
| 144 | [ ] | Capcom Arcade Stadium (STEAM) | 39 | 48 | 81% (90d) | Does not open (84%) | 76% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 145 | [ ] | Monster Hunter Wilds (STEAM) | 39 | 40 | 98% (90d) | Does not open (63%) | 76% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 146 | [ ] | CrossCode (GOG) | 38 | 42 | 90% (90d) | Does not open (78%) | 71% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 147 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 69 | 54% (90d) | Does not open (68%) | 88% |  |
| 148 | [ ] | Tales of ARISE (STEAM) | 37 | 66 | 56% (90d) | Controller issues (73%) | 94% |  |
| 149 | [ ] | Fallout 3 (STEAM) | 36 | 72 | 50% (1.3.0) | Does not open (47%) | 91% |  |
| 150 | [ ] | Hearts of Iron IV (STEAM) | 36 | 63 | 57% (90d) | Does not open (74%) | 67% |  |
| 151 | [ ] | SurrounDead (STEAM) | 35 | 66 | 53% (90d) | Controller issues (61%) | 94% |  |
| 152 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 35 | 41 | 85% (90d) | No graphics (69%) | 82% | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 153 | [ ] | Street Fighter 30th Anniversary Collection (STEAM) | 34 | 66 | 52% (90d) | Does not open (100%) | 65% |  |
| 154 | [ ] | Rocket League (STEAM) | 34 | 55 | 62% (90d) | Does not open (69%) | 69% |  |
| 155 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 34 | 47 | 72% (90d) | Controller issues (88%) | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 156 | [ ] | SnowRunner (STEAM) | 34 | 47 | 72% (90d) | Does not open (96%) | 85% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 157 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 34 | 39 | 87% (90d) | Does not open (68%) | 64% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 158 | [ ] | Hero Siege (STEAM) | 33 | 58 | 57% (90d) | Graphics glitches (52%) | 63% |  |
| 159 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 33 | 54 | 61% (90d) | Controller issues (64%) | 71% |  |
| 160 | [ ] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 54 | 61% (90d) | Controller issues (84%) | 81% |  |
| 161 | [ ] | Capcom Fighting Collection 2 (STEAM) | 33 | 49 | 67% (90d) | Does not open (78%) | 86% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 162 | [ ] | Supermarket Together (STEAM) | 33 | 47 | 70% (90d) | Does not open (72%) | 72% |  |
| 163 | [ ] | Romestead (STEAM) | 33 | 44 | 75% (90d) | Does not open (67%) | 77% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 164 | [ ] | Russian Fishing 4 (STEAM) | 33 | 39 | 85% (90d) | Does not open (68%) | 75% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 165 | [ ] | Hotline Miami (GOG) | 33 | 38 | 87% (90d) | Does not open (94%) | 69% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 166 | [ ] | COCOON (STEAM) | 32 | 61 | 52% (90d) | Directx error (50%) | 90% |  |
| 167 | [ ] | Max Payne (STEAM) | 32 | 58 | 55% (90d) | No graphics (43%) | 94% |  |
| 168 | [ ] | Earthion (STEAM) | 32 | 52 | 62% (90d) | Controller issues (90%) | 100% |  |
| 169 | [ ] | Counter-Strike:Global Offensive (STEAM) | 32 | 50 | 64% (90d) | Does not open (78%) | 78% |  |
| 170 | [ ] | Secrets of Grindea (STEAM) | 32 | 50 | 64% (90d) | Does not open (52%) | 81% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 171 | [ ] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 32 | 48 | 67% (90d) | Does not open (85%) | 87% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 172 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 42 | 76% (90d) | Controller issues (62%) | 89% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 173 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 32 | 38 | 84% (90d) | Does not open (60%) | 72% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 174 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 32 | 37 | 86% (90d) | Does not open (73%) | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 175 | [ ] | Red Dead Redemption (STEAM) | 32 | 36 | 89% (90d) | Does not open (95%) | 89% |  |
| 176 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 31 | 60 | 52% (90d) | Does not open (73%) | 88% |  |
| 177 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 31 | 55 | 56% (90d) | Does not open (46%) | 67% |  |
| 178 | [ ] | Resident Evil Village (STEAM) | 31 | 53 | 58% (90d) | Does not open (67%) | 90% |  |
| 179 | [ ] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 31 | 50 | 62% (90d) | Does not open (45%) | 78% |  |
| 180 | [ ] | Tower and Sword of Succubus (STEAM) | 31 | 46 | 67% (90d) | No graphics (81%) | 100% |  |
| 181 | [ ] | Palia (STEAM) | 31 | 43 | 72% (90d) | Does not open (68%) | 79% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 182 | [ ] | Nioh: Complete Edition (STEAM) | 31 | 42 | 74% (90d) | Does not open (56%) | 95% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 183 | [ ] | Super Animal Royale (STEAM) | 31 | 41 | 76% (90d) | Does not open (68%) | 72% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 184 | [ ] | Grand Theft Auto III (STEAM) | 31 | 39 | 79% (90d) | Does not open (52%) | 81% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 185 | [ ] | CRUEL (STEAM) | 31 | 37 | 84% (90d) | Does not open (90%) | 75% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 186 | [ ] | Path of Exile 2 (STEAM) | 31 | 37 | 84% (90d) | Does not open (96%) | 86% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 187 | [ ] | Need for Speed™ (STEAM) | 31 | 33 | 94% (90d) | Does not open (69%) | 60% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 188 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 30 | 70 | 50% (1.3.0) | Does not open (74%) | 78% |  |
| 189 | [ ] | Yakuza: Like a Dragon (STEAM) | 30 | 44 | 68% (90d) | Does not open (61%) | 68% |  |
| 190 | [ ] | Ultimate Custom Night (STEAM) | 30 | 42 | 71% (90d) | No graphics (72%) | 78% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 191 | [ ] | Dead Island Riptide Definitive Edition (STEAM) | 29 | 54 | 54% (90d) | Does not open (50%) | 82% |  |
| 192 | [ ] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 54 | 54% (90d) | Does not open (92%) | 83% |  |
| 193 | [ ] | Aethermancer (STEAM) | 29 | 51 | 57% (90d) | Does not open (78%) | 83% |  |
| 194 | [ ] | Heavy Rain (STEAM) | 29 | 50 | 58% (90d) | Controller issues (61%) | 86% |  |
| 195 | [ ] | Binary Domain (STEAM) | 29 | 45 | 64% (90d) | Does not open (92%) | 80% |  |
| 196 | [ ] | Mortal Kombat X (STEAM) | 28 | 54 | 52% (90d) | Does not open (52%) | 85% |  |
| 197 | [ ] | Tails of Iron (STEAM) | 28 | 54 | 52% (90d) | Does not open (47%) | 95% |  |
| 198 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 28 | 49 | 57% (90d) | Controller issues (46%) | 91% |  |
| 199 | [ ] | Akane (STEAM) | 28 | 47 | 60% (90d) | Controller issues (67%) | 100% |  |
| 200 | [ ] | Zero Escape: The Nonary Games (STEAM) | 28 | 46 | 61% (90d) | Does not open (88%) | 67% |  |
| 201 | [ ] | Moonlight Peaks (STEAM) | 28 | 40 | 70% (90d) | Does not open (64%) | 91% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 202 | [ ] | Stellar Blade™ (STEAM) | 28 | 38 | 74% (90d) | Does not open (48%) | 86% |  |
| 203 | [ ] | Dead Rising 2 (STEAM) | 27 | 42 | 67% (1.3.0) | Does not open (88%) | 71% |  |
| 204 | [ ] | Deus Ex™ GOTY Edition (GOG) | 27 | 41 | 66% (90d) | Does not open (35%) | 83% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 205 | [ ] | Ratatan (STEAM) | 27 | 40 | 68% (90d) | Does not open (50%) | 99% |  |
| 206 | [ ] | Tales of Zestiria (STEAM) | 27 | 33 | 82% (90d) | Does not open (81%) | 67% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 207 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 26 | 48 | 54% (90d) | Does not open (55%) | 71% |  |
| 208 | [ ] | Digimon Survive (STEAM) | 26 | 43 | 60% (90d) | Controller issues (73%) | 96% |  |
| 209 | [ ] | Prince of Persia (GOG) | 26 | 43 | 60% (90d) | Does not open (95%) | 91% |  |
| 210 | [ ] | Gothic II: Gold Classic (STEAM) | 26 | 37 | 70% (90d) | Does not open (59%) | 72% |  |
| 211 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 26 | 36 | 72% (90d) | Does not open (67%) | 92% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 212 | [ ] | Crab Game (STEAM) | 26 | 34 | 76% (90d) | Does not open (53%) | 78% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 213 | [ ] | Persona 5 Strikers (STEAM) | 26 | 29 | 90% (90d) | Does not open (78%) | 60% | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 214 | [ ] | No, I'm not a Human (STEAM) | 25 | 56 | 57% (1.3.0) | Does not open (48%) | 92% |  |
| 215 | [ ] | Cave Story+ (EPIC) | 25 | 50 | 50% (90d) | Does not open (47%) | 87% |  |
| 216 | [ ] | Unturned (STEAM) | 25 | 46 | 54% (90d) | Does not open (59%) | 78% |  |
| 217 | [ ] | Being a DIK (STEAM) | 25 | 43 | 58% (90d) | Does not open (78%) | 83% |  |
| 218 | [ ] | Battle Brothers (STEAM) | 25 | 40 | 63% (90d) | Does not open (67%) | 67% |  |
| 219 | [ ] | Limbus Company (STEAM) | 25 | 39 | 64% (90d) | Does not open (85%) | 75% |  |
| 220 | [ ] | Changed (STEAM) | 25 | 38 | 66% (90d) | Does not open (65%) | 88% |  |
| 221 | [ ] | Return to Monkey Island (STEAM) | 25 | 38 | 66% (90d) | No graphics (58%) | 86% |  |
| 222 | [ ] | Bongo Cat (STEAM) | 25 | 35 | 71% (90d) | Does not open (65%) | 81% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 223 | [ ] | Beyond: Two Souls (STEAM) | 25 | 33 | 76% (90d) | Does not open (50%) | 70% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 224 | [ ] | Goose Goose Duck (STEAM) | 25 | 33 | 76% (90d) | Does not open (71%) | 72% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 225 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 32 | 78% (90d) | Does not open (87%) | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 226 | [ ] | Tearscape (STEAM) | 25 | 29 | 86% (90d) | Controller issues (53%) | 93% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 227 | [ ] | Resident Evil (GOG) | 25 | 27 | 93% (90d) | Does not open (95%) | 61% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 228 | [ ] | Resident Evil Revelations 2 (STEAM) | 24 | 48 | 50% (90d) | Does not open (40%) | 92% |  |
| 229 | [ ] | Goat Simulator (STEAM) | 24 | 45 | 53% (90d) | Does not open (58%) | 62% |  |
| 230 | [ ] | Counter-Strike: Condition Zero (STEAM) | 24 | 42 | 57% (90d) | Does not open (50%) | 60% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 231 | [ ] | Wizard of Legend (EPIC) | 24 | 41 | 59% (90d) | Does not open (78%) | 80% |  |
| 232 | [ ] | Cat Mail Co. (STEAM) | 24 | 40 | 60% (90d) | Does not open (89%) | 89% |  |
| 233 | [ ] | Opus Magnum (STEAM) | 24 | 38 | 63% (90d) | Does not open (76%) | 83% |  |
| 234 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 24 | 34 | 71% (90d) | Does not open (57%) | 65% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 235 | [ ] | PowerWash Simulator (STEAM) | 23 | 67 | 76% (1.3.0) | Does not open (84%) | 77% |  |
| 236 | [ ] | Football Manager 2024 (EPIC) | 23 | 41 | 56% (90d) | Does not open (86%) | 89% |  |
| 237 | [ ] | Lobotomy Corporation (STEAM) | 23 | 41 | 56% (90d) | No graphics (60%) | 95% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 238 | [ ] | SWORN (STEAM) | 23 | 38 | 61% (90d) | Does not open (44%) | 100% |  |
| 239 | [ ] | Worms W.M.D (STEAM) | 23 | 38 | 61% (90d) | Does not open (58%) | 90% |  |
| 240 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 36 | 64% (90d) | Does not open (100%) | 79% |  |
| 241 | [ ] | Timberborn (STEAM) | 23 | 35 | 66% (90d) | No graphics (62%) | 83% |  |
| 242 | [ ] | Party Animals (STEAM) | 23 | 32 | 72% (90d) | Does not open (75%) | 71% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 243 | [ ] | Jade Empire: Special Edition (GOG) | 23 | 31 | 74% (90d) | Does not open (50%) | 72% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 244 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 23 | 31 | 74% (90d) | Does not open (40%) | 73% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 245 | [ ] | CarX Street (STEAM) | 23 | 30 | 77% (90d) | Does not open (77%) | 82% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 246 | [ ] | FINAL FANTASY XIV Online (STEAM) | 23 | 30 | 77% (90d) | Does not open (100%) | 96% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 247 | [ ] | Jade Empire: Special Edition (STEAM) | 23 | 26 | 88% (90d) | Does not open (95%) | 67% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 248 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 22 | 42 | 52% (90d) | Controller issues (67%) | 91% |  |
| 249 | [ ] | Pinball FX Classic (STEAM) | 22 | 40 | 55% (90d) | Does not open (76%) | 91% |  |
| 250 | [ ] | This War of Mine (STEAM) | 22 | 40 | 55% (90d) | No graphics (56%) | 76% |  |
| 251 | [ ] | Life is Strange Remastered (STEAM) | 22 | 34 | 65% (90d) | Does not open (73%) | 89% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 252 | [ ] | Need for Speed™ Unbound (STEAM) | 22 | 30 | 73% (90d) | Does not open (83%) | 79% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 253 | [ ] | Capcom Fighting Collection (STEAM) | 22 | 27 | 81% (90d) | Does not open (80%) | 76% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 254 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 59 | 82% (1.3.0) | Does not open (79%) | 100% |  |
| 255 | [ ] | Gambonanza (STEAM) | 21 | 40 | 53% (90d) | Does not open (60%) | 93% |  |
| 256 | [ ] | Overlord (STEAM) | 21 | 40 | 53% (90d) | Does not open (71%) | 62% |  |
| 257 | [ ] | Trailmakers (STEAM) | 21 | 39 | 54% (90d) | Does not open (44%) | 94% |  |
| 258 | [ ] | One-armed robber (STEAM) | 21 | 38 | 55% (90d) | Controller issues (58%) | 79% |  |
| 259 | [ ] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 21 | 37 | 57% (90d) | Controller issues (50%) | 100% |  |
| 260 | [ ] | Tiny Glade (STEAM) | 21 | 36 | 58% (90d) | Does not open (42%) | 68% |  |
| 261 | [ ] | GOD EATER RESURRECTION (STEAM) | 21 | 32 | 66% (90d) | Does not open (53%) | 60% |  |
| 262 | [ ] | Nex Machina (STEAM) | 21 | 28 | 75% (90d) | Does not open (57%) | 79% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 263 | [ ] | Paper Lily - Chapter 1 (STEAM) | 20 | 40 | 50% (90d) | Does not open (72%) | 94% |  |
| 264 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 20 | 39 | 51% (90d) | Does not open (56%) | 73% |  |
| 265 | [ ] | Crimzon Clover World EXplosion (STEAM) | 20 | 39 | 51% (90d) | Does not open (47%) | 100% |  |
| 266 | [ ] | Control Ultimate Edition (GOG) | 20 | 37 | 54% (90d) | Does not open (81%) | 94% |  |
| 267 | [ ] | Mafia: Definitive Edition (STEAM) | 20 | 37 | 54% (90d) | Does not open (84%) | 82% |  |
| 268 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 20 | 27 | 74% (90d) | Does not open (65%) | 83% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 269 | [ ] | BAJA: Edge of Control HD (STEAM) | 20 | 26 | 77% (90d) | Does not open (100%) | 90% | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 270 | [ ] | Dead Island (STEAM) | 20 | 26 | 77% (90d) | Does not open (69%) | 75% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 271 | [ ] | Tyr (STEAM) | 20 | 26 | 77% (90d) | Does not open (33%) | 82% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 272 | [ ] | Killing Floor (STEAM) | 19 | 34 | 56% (90d) | Controller issues (100%) | 88% |  |
| 273 | [ ] | My Summer Car (STEAM) | 19 | 34 | 56% (90d) | Does not open (59%) | 86% |  |
| 274 | [ ] | Stick It to the Stickman (STEAM) | 19 | 34 | 56% (90d) | Does not open (88%) | 76% |  |
| 275 | [ ] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 19 | 33 | 58% (90d) | Does not open (88%) | 68% |  |
| 276 | [ ] | Metro Exodus (STEAM) | 19 | 31 | 61% (90d) | Does not open (82%) | 90% |  |
| 277 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 19 | 28 | 68% (90d) | Does not open (72%) | 75% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 278 | [ ] | Torchlight II (EPIC) | 19 | 27 | 70% (90d) | Does not open (82%) | 100% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 279 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 19 | 24 | 79% (90d) | Does not open (82%) | 94% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 280 | [ ] | Backpack Battles (STEAM) | 18 | 36 | 50% (90d) | Does not open (61%) | 97% |  |
| 281 | [ ] | Faster Than Light (EPIC) | 18 | 36 | 50% (90d) | Does not open (41%) | 94% |  |
| 282 | [ ] | SKALD: Against the Black Priory (STEAM) | 18 | 36 | 50% (90d) | No graphics (63%) | 97% |  |
| 283 | [ ] | Far Far West (STEAM) | 18 | 32 | 56% (90d) | Does not open (59%) | 77% |  |
| 284 | [ ] | Hitman: Absolution (GOG) | 18 | 30 | 60% (90d) | Does not open (81%) | 84% |  |
| 285 | [ ] | Tabletop Simulator (STEAM) | 18 | 30 | 60% (90d) | Does not open (50%) | 65% |  |
| 286 | [ ] | Formula Legends (STEAM) | 18 | 28 | 64% (90d) | No graphics (60%) | 65% |  |
| 287 | [ ] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 18 | 27 | 67% (90d) | Does not open (83%) | 93% |  |
| 288 | [ ] | Arcade Paradise (EPIC) | 18 | 26 | 69% (90d) | Does not open (45%) | 82% |  |
| 289 | [ ] | DOOM 3: BFG Edition (GOG) | 18 | 25 | 72% (90d) | No graphics (67%) | 80% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 290 | [ ] | Katanaut (STEAM) | 18 | 25 | 72% (90d) | Does not open (76%) | 69% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 291 | [ ] | Crusader Kings III (STEAM) | 18 | 23 | 78% (90d) | No graphics (64%) | 77% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 292 | [ ] | Dorfromantik (GOG) | 18 | 23 | 78% (90d) | Does not open (94%) | 64% | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 293 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 18 | 22 | 82% (90d) | Controller issues (100%) | 100% |  |
| 294 | [ ] | Deadly Premonition: The Director's Cut (STEAM) | 18 | 21 | 86% (90d) | Does not open (47%) | 77% |  |
| 295 | [ ] | CULTIC (STEAM) | 17 | 33 | 52% (90d) | Does not open (92%) | 61% |  |
| 296 | [ ] | No More Heroes (STEAM) | 17 | 33 | 52% (90d) | No graphics (71%) | 62% |  |
| 297 | [ ] | Lost Castle 2 (STEAM) | 17 | 32 | 53% (90d) | Does not open (62%) | 100% |  |
| 298 | [ ] | SCP – Containment Breach (STEAM) | 17 | 32 | 53% (90d) | Does not open (82%) | 83% |  |
| 299 | [ ] | GRANDIA HD Remaster (STEAM) | 17 | 31 | 55% (90d) | Does not open (93%) | 68% |  |
| 300 | [ ] | GRIP: Combat Racing (STEAM) | 17 | 31 | 55% (90d) | Does not open (100%) | 83% |  |
| 301 | [ ] | Shank 2 (STEAM) | 17 | 30 | 57% (90d) | Does not open (82%) | 100% |  |
| 302 | [ ] | Maneater (STEAM) | 17 | 27 | 63% (90d) | Does not open (92%) | 77% |  |
| 303 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 17 | 27 | 63% (90d) | No graphics (47%) | 78% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 304 | [ ] | Grim Fandango Remastered (GOG) | 17 | 25 | 68% (90d) | No graphics (78%) | 60% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 305 | [ ] | Fall Guys (STEAM) | 17 | 23 | 74% (90d) | Does not open (92%) | 93% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 306 | [ ] | DNF Duel (EPIC) | 16 | 29 | 55% (90d) | Does not open (54%) | 90% |  |
| 307 | [ ] | Titanfall® 2 (STEAM) | 16 | 28 | 57% (90d) | Does not open (83%) | 82% |  |
| 308 | [ ] | WORLD OF FINAL FANTASY (STEAM) | 16 | 27 | 59% (90d) | No graphics (62%) | 78% |  |
| 309 | [ ] | Dishonored 2 (STEAM) | 16 | 26 | 62% (90d) | Does not open (85%) | 92% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 310 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 22 | 73% (90d) | No graphics (60%) | 85% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 311 | [ ] | Content Warning (STEAM) | 16 | 21 | 76% (90d) | Does not open (53%) | 90% | [#241](https://github.com/GameNative/gamenative-compat/issues/241) |
| 312 | [ ] | Blood Bowl 2 (STEAM) | 16 | 20 | 80% (90d) | Does not open (64%) | 90% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 313 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 16 | 20 | 80% (90d) | Does not open (60%) | 91% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 314 | [ ] | Antichamber (STEAM) | 15 | 30 | 50% (90d) | Does not open (38%) | 88% |  |
| 315 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 15 | 30 | 50% (90d) | Does not open (100%) | 68% |  |
| 316 | [ ] | Mark of the Ninja (STEAM) | 15 | 30 | 50% (90d) | Does not open (75%) | 64% |  |
| 317 | [ ] | Sorry We're Closed (EPIC) | 15 | 28 | 50% (14d) | Does not open (100%) | 86% |  |
| 318 | [ ] | Wildermyth (STEAM) | 15 | 26 | 58% (90d) | Does not open (50%) | 94% |  |
| 319 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 15 | 25 | 60% (90d) | Does not open (92%) | 74% |  |
| 320 | [ ] | LET IT DIE (STEAM) | 15 | 25 | 60% (90d) | Does not open (91%) | 73% |  |
| 321 | [ ] | Batman™: Arkham Origins (GOG) | 15 | 24 | 63% (90d) | Does not open (67%) | 93% |  |
| 322 | [ ] | Mortal Shell (EPIC) | 15 | 24 | 63% (90d) | No graphics (89%) | 88% |  |
| 323 | [ ] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 15 | 23 | 65% (90d) | Does not open (64%) | 67% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 324 | [ ] | Allumeria (STEAM) | 15 | 22 | 68% (90d) | Does not open (69%) | 69% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 325 | [ ] | Chef Knight (STEAM) | 15 | 22 | 68% (90d) | Does not open (100%) | 69% |  |
| 326 | [ ] | Maneater (EPIC) | 15 | 20 | 75% (90d) | Does not open (73%) | 79% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 327 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 28 | 50% (90d) | Controller issues (54%) | 85% |  |
| 328 | [ ] | sobosuba (STEAM) | 14 | 28 | 50% (90d) | Does not open (57%) | 90% |  |
| 329 | [ ] | Ultrapool (STEAM) | 14 | 25 | 56% (90d) | Does not open (54%) | 100% |  |
| 330 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 24 | 58% (90d) | Does not open (90%) | 73% |  |
| 331 | [ ] | Gloomwood (STEAM) | 14 | 24 | 58% (90d) | Does not open (62%) | 75% |  |
| 332 | [ ] | Alabaster Dawn Demo (STEAM) | 14 | 23 | 61% (90d) | Controller issues (71%) | 89% |  |
| 333 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 23 | 61% (90d) | Controller issues (62%) | 65% |  |
| 334 | [ ] | Disgaea 4 Complete+ (STEAM) | 14 | 22 | 64% (90d) | No graphics (43%) | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 335 | [ ] | Songs of Conquest (EPIC) | 14 | 22 | 64% (90d) | Does not open (75%) | 90% |  |
| 336 | [ ] | Sons Of The Forest (STEAM) | 14 | 22 | 64% (90d) | Does not open (50%) | 77% |  |
| 337 | [ ] | Horny Villa (STEAM) | 14 | 20 | 70% (90d) | Does not open (63%) | 95% |  |
| 338 | [ ] | Human Fall Flat (STEAM) | 13 | 26 | 50% (90d) | Does not open (50%) | 66% |  |
| 339 | [ ] | Lust Goddess (STEAM) | 13 | 25 | 52% (90d) | Does not open (100%) | 67% |  |
| 340 | [ ] | Haydee (STEAM) | 13 | 24 | 54% (90d) | Does not open (100%) | 82% |  |
| 341 | [ ] | Look Outside (GOG) | 13 | 24 | 54% (90d) | Does not open (100%) | 100% |  |
| 342 | [ ] | Pillars of Eternity (STEAM) | 13 | 24 | 54% (90d) | Does not open (43%) | 65% |  |
| 343 | [ ] | Scrap Mechanic (STEAM) | 13 | 24 | 54% (90d) | Does not open (45%) | 71% |  |
| 344 | [ ] | DiRT 4 (STEAM) | 13 | 23 | 57% (90d) | Does not open (75%) | 96% |  |
| 345 | [ ] | Minit (EPIC) | 13 | 23 | 57% (90d) | Does not open (82%) | 82% |  |
| 346 | [ ] | Ready or Not (STEAM) | 13 | 23 | 57% (90d) | Does not open (55%) | 90% |  |
| 347 | [ ] | 12 is Better Than 6 (STEAM) | 13 | 22 | 59% (90d) | Does not open (50%) | 85% |  |
| 348 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 22 | 59% (90d) | Does not open (80%) | 92% |  |
| 349 | [ ] | Secret of Mana (STEAM) | 13 | 21 | 62% (90d) | Graphics glitches (58%) | 64% |  |
| 350 | [ ] | Shift At Midnight (STEAM) | 13 | 21 | 62% (90d) | Does not open (83%) | 91% |  |
| 351 | [ ] | Escape the Backrooms (STEAM) | 13 | 20 | 65% (90d) | Does not open (100%) | 93% |  |
| 352 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 13 | 20 | 65% (90d) | Does not open (71%) | 61% |  |
| 353 | [ ] | War Thunder (STEAM) | 13 | 20 | 65% (90d) | Does not open (80%) | 81% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 354 | [ ] | NiGHTS into Dreams... (STEAM) | 12 | 24 | 50% (90d) | Does not open (44%) | 93% |  |
| 355 | [ ] | Sonic Superstars (STEAM) | 12 | 24 | 50% (90d) | Does not open (70%) | 66% |  |
| 356 | [ ] | AER Memories of Old (EPIC) | 12 | 23 | 52% (90d) | Does not open (91%) | 94% |  |
| 357 | [ ] | Cruelty Squad (STEAM) | 12 | 23 | 52% (90d) | Does not open (67%) | 86% |  |
| 358 | [ ] | Sid Meier's Civilization VI (EPIC) | 12 | 23 | 52% (90d) | Does not open (55%) | 90% |  |
| 359 | [ ] | UNDEFEATED (STEAM) | 12 | 23 | 52% (90d) | Does not open (89%) | 82% |  |
| 360 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 12 | 22 | 55% (90d) | Does not open (60%) | 89% |  |
| 361 | [ ] | HITMAN World of Assassination (STEAM) | 12 | 22 | 55% (90d) | Does not open (73%) | 87% |  |
| 362 | [ ] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 22 | 55% (90d) | Controller issues (60%) | 89% |  |
| 363 | [ ] | FATE (STEAM) | 12 | 21 | 57% (90d) | No graphics (44%) | 92% |  |
| 364 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (90d) | No graphics (67%) | 64% |  |
| 365 | [ ] | PAYDAY: The Heist (STEAM) | 12 | 20 | 60% (90d) | Does not open (73%) | 75% |  |
| 366 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (90d) | Does not open (89%) | 96% |  |
| 367 | [ ] | Castle in the Clouds (STEAM) | 11 | 22 | 50% (90d) | No graphics (63%) | 85% |  |
| 368 | [ ] | Ghostwire Tokyo (EPIC) | 11 | 22 | 50% (90d) | Does not open (86%) | 94% |  |
| 369 | [ ] | Injustice™ 2 (STEAM) | 11 | 22 | 50% (90d) | Does not open (88%) | 73% |  |
| 370 | [ ] | Tom Clancy's Rainbow Six: Vegas 2 (STEAM) | 11 | 22 | 50% (90d) | Does not open (55%) | 88% |  |
| 371 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 21 | 52% (90d) | Does not open (86%) | 74% |  |
| 372 | [ ] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 21 | 52% (90d) | Graphics glitches (40%) | 95% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 373 | [ ] | Shadow Tactics: Blades of the Shogun (EPIC) | 11 | 20 | 55% (90d) | Does not open (67%) | 100% |  |
| 374 | [ ] | Command & Conquer™ Remastered Collection (STEAM) | 10 | 20 | 50% (90d) | Does not open (75%) | 70% |  |
| 375 | [ ] | Coromon (GOG) | 10 | 20 | 50% (90d) | Does not open (56%) | 61% |  |

## Recently recovered (404)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | FINAL FANTASY RESONANCE (STEAM) | 309 | 2026-10-24 | 716 | 75% |  |
| 2 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 253 | 2026-10-23 | 295 | 65% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 3 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 244 | 2026-10-19 | 297 | 66% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 232 | 2026-10-18 | 356 | 59% |  |
| 5 | [x] | OMORI (STEAM) | 203 | 2026-10-16 | 246 | 78% |  |
| 6 | [x] | DRAGON BALL FighterZ (STEAM) | 201 | 2026-11-01 | 231 | 62% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 7 | [x] | Devil May Cry HD Collection (STEAM) | 200 | 2026-10-19 | 282 | 76% |  |
| 8 | [x] | Spelunky 2 (STEAM) | 191 | 2026-11-01 | 212 | 49% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 9 | [x] | Burnout Paradise: The Ultimate Box (STEAM) | 156 | 2026-10-16 | 244 | 71% |  |
| 10 | [x] | Counter-Strike (STEAM) | 142 | 2026-10-22 | 226 | 50% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 11 | [x] | Borderlands 2 (EPIC) | 142 | 2026-10-25 | 169 | 63% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 12 | [x] | Sonic Adventure™ 2  (STEAM) | 141 | 2026-11-01 | 198 | 52% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 13 | [x] | Far Cry® 3 (STEAM) | 129 | 2026-10-21 | 144 | 66% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 14 | [x] | Minecraft Dungeons II (STEAM) | 124 | 2026-10-21 | 142 | 64% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 15 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 120 | 2026-10-28 | 152 | 64% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 16 | [x] | Call of Duty: Black Ops III (STEAM) | 117 | 2026-10-18 | 245 | 71% |  |
| 17 | [x] | Euro Truck Simulator 2 (STEAM) | 116 | 2026-11-01 | 214 | 58% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 18 | [x] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 116 | 2026-10-18 | 163 | 62% |  |
| 19 | [x] | The Witcher: Enhanced Edition (STEAM) | 113 | 2026-10-25 | 130 | 61% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 20 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 105 | 2026-10-18 | 154 | 75% |  |
| 21 | [x] | Moonstone Island (STEAM) | 103 | 2026-10-16 | 136 | 88% |  |
| 22 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 98 | 2026-10-25 | 154 | 66% |  |
| 23 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 94 | 2026-10-17 | 122 | 97% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 24 | [x] | Don't Starve Together (STEAM) | 91 | 2026-10-16 | 181 | 79% |  |
| 25 | [x] | Catherine Classic (STEAM) | 86 | 2026-10-19 | 172 | 80% |  |
| 26 | [x] | Ultra Street Fighter IV (STEAM) | 84 | 2026-10-17 | 181 | 69% |  |
| 27 | [x] | Hogwarts Legacy (STEAM) | 83 | 2026-10-17 | 145 | 67% |  |
| 28 | [x] | Cry of Fear (STEAM) | 82 | 2026-10-18 | 163 | 85% |  |
| 29 | [x] | FINAL FANTASY XIII-2 (STEAM) | 82 | 2026-10-30 | 84 | 60% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 30 | [x] | DOOM 3: BFG Edition (STEAM) | 80 | 2026-10-19 | 116 | 70% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 31 | [x] | Sol Cesto (EPIC) | 79 | 2026-11-03 | 84 | 64% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 32 | [x] | Detroit: Become Human (STEAM) | 77 | 2026-10-17 | 80 | 65% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 33 | [x] | Need for Speed: Hot Pursuit (STEAM) | 75 | 2026-10-25 | 107 | 79% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 34 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 74 | 2026-10-18 | 124 | 94% |  |
| 35 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 73 | 2026-10-17 | 102 | 82% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 36 | [x] | Bayonetta (STEAM) | 71 | 2026-10-18 | 208 | 77% |  |
| 37 | [x] | Darksiders (STEAM) | 71 | 2026-10-26 | 86 | 88% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 38 | [x] | Dota 2 (STEAM) | 70 | 2026-10-17 | 106 | 70% |  |
| 39 | [x] | Disgaea 5 Complete (STEAM) | 70 | 2026-10-18 | 84 | 98% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 40 | [x] | American Truck Simulator (STEAM) | 68 | 2026-10-18 | 109 | 79% |  |
| 41 | [x] | Fallout (STEAM) | 68 | 2026-10-18 | 106 | 71% |  |
| 42 | [x] | Spyro™ Reignited Trilogy (STEAM) | 67 | 2026-10-18 | 105 | 72% |  |
| 43 | [x] | Gunfire Reborn (STEAM) | 67 | 2026-10-22 | 73 | 94% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 44 | [x] | Bloodstained: Ritual of the Night (EPIC) | 66 | 2026-10-19 | 121 | 62% |  |
| 45 | [x] | Stardew Valley (GOG) | 66 | 2026-11-01 | 119 | 51% |  |
| 46 | [x] | Fable - The Lost Chapters (STEAM) | 66 | 2026-10-17 | 105 | 79% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 47 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 65 | 2026-10-17 | 87 | 92% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 48 | [x] | Call of Juarez Gunslinger (STEAM) | 65 | 2026-10-18 | 80 | 76% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 49 | [x] | Don't Starve (STEAM) | 64 | 2026-10-16 | 152 | 82% |  |
| 50 | [x] | Sonic Lost World (STEAM) | 64 | 2026-10-18 | 108 | 88% |  |
| 51 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 64 | 2026-10-21 | 86 | 61% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 52 | [x] | Poppy Playtime (STEAM) | 63 | 2026-10-17 | 110 | 78% |  |
| 53 | [x] | Borderlands: The Pre-Sequel (STEAM) | 63 | 2026-10-17 | 89 | 63% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 54 | [x] | A Plague Tale: Innocence (STEAM) | 60 | 2026-10-20 | 63 | 73% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 55 | [x] | Mini Motorways (STEAM) | 59 | 2026-11-04 | 102 | 61% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 56 | [x] | Big Walk (STEAM) | 59 | 2026-10-17 | 91 | 82% |  |
| 57 | [x] | eFootball™ (STEAM) | 59 | 2026-10-18 | 87 | 75% |  |
| 58 | [x] | Call of Duty: World at War (STEAM) | 58 | 2026-10-28 | 83 | 73% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 59 | [x] | Borderlands 3 (STEAM) | 58 | 2026-10-19 | 78 | 94% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 60 | [x] | Sonic Generations (STEAM) | 58 | 2026-10-17 | 68 | 62% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 61 | [x] | Starbound (STEAM) | 57 | 2026-10-18 | 87 | 69% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 62 | [x] | Dead by Daylight (STEAM) | 57 | 2026-10-23 | 62 | 81% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 63 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 56 | 2026-10-18 | 86 | 71% |  |
| 64 | [x] | Okami HD (STEAM) | 55 | 2026-10-17 | 100 | 86% |  |
| 65 | [x] | Sonic Adventure DX (STEAM) | 55 | 2026-10-17 | 89 | 64% |  |
| 66 | [x] | TBH: Task Bar Hero (STEAM) | 55 | 2026-10-19 | 85 | 94% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 67 | [x] | Until Then (STEAM) | 53 | 2026-10-17 | 92 | 96% |  |
| 68 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 53 | 2026-11-02 | 90 | 61% |  |
| 69 | [x] | Path of Exile (STEAM) | 53 | 2026-10-26 | 62 | 86% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 70 | [x] | Alex Kidd in Miracle World DX (EPIC) | 53 | 2026-10-22 | 57 | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 71 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 52 | 2026-10-18 | 77 | 65% |  |
| 72 | [x] | Vampire Survivors (EPIC) | 52 | 2026-11-03 | 74 | 60% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 73 | [x] | Guildrun Demo (STEAM) | 52 | 2026-10-22 | 73 | 73% |  |
| 74 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 51 | 2026-10-25 | 97 | 57% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 75 | [x] | A Plague Tale: Innocence (EPIC) | 51 | 2026-10-25 | 87 | 89% |  |
| 76 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 51 | 2026-10-21 | 59 | 82% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 77 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 50 | 2026-10-19 | 97 | 76% |  |
| 78 | [x] | Heroes of Might & Magic III - HD Edition (STEAM) | 50 | 2026-11-04 | 64 | 61% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 79 | [x] | DOOM 3 (STEAM) | 50 | 2026-11-01 | 55 | 60% | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 80 | [x] | Dead Space (STEAM) | 49 | 2026-10-18 | 62 | 78% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 81 | [x] | Sheepy: A Short Adventure (STEAM) | 49 | 2026-10-24 | 59 | 80% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 82 | [x] | Sleeping Dogs™ (STEAM) | 49 | 2026-10-27 | 56 | 77% | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 83 | [x] | Darkest Dungeon® (EPIC) | 48 | 2026-10-22 | 88 | 61% |  |
| 84 | [x] | Rivals of Aether II (STEAM) | 48 | 2026-10-20 | 70 | 73% |  |
| 85 | [x] | STEINS;GATE RE:BOOT (STEAM) | 48 | 2026-10-21 | 69 | 60% |  |
| 86 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 2026-10-17 | 78 | 95% |  |
| 87 | [x] | Watch_Dogs 2 (STEAM) | 47 | 2026-11-03 | 52 | 61% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 88 | [x] | Moonlighter (EPIC) | 47 | 2026-10-23 | 51 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 89 | [x] | Digimon World: Next Order (STEAM) | 46 | 2026-10-18 | 86 | 95% |  |
| 90 | [x] | Tomb Raider: Anniversary (STEAM) | 46 | 2026-10-25 | 65 | 60% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 91 | [x] | MudRunner (STEAM) | 45 | 2026-10-24 | 97 | 70% |  |
| 92 | [x] | Abiotic Factor (STEAM) | 45 | 2026-10-18 | 78 | 68% |  |
| 93 | [x] | Street Fighter™ 6 (STEAM) | 44 | 2026-10-16 | 70 | 79% |  |
| 94 | [x] | Aggelos (STEAM) | 44 | 2026-10-21 | 58 | 95% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 95 | [x] | PROTOTYPE 2 (STEAM) | 43 | 2026-10-18 | 90 | 78% |  |
| 96 | [x] | Skullgirls 2nd Encore (STEAM) | 43 | 2026-11-01 | 78 | 57% |  |
| 97 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 43 | 2026-10-17 | 77 | 87% |  |
| 98 | [x] | Death Road to Canada (STEAM) | 42 | 2026-10-17 | 100 | 70% |  |
| 99 | [x] | Tomb Raider GOTY (GOG) | 42 | 2026-10-17 | 87 | 97% |  |
| 100 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 42 | 2026-10-18 | 63 | 69% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 101 | [x] | Deadlock (STEAM) | 42 | 2026-10-16 | 63 | 94% |  |
| 102 | [x] | FINAL FANTASY VII (2013) (STEAM) | 42 | 2026-10-18 | 61 | 79% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 103 | [x] | Life is Strange™ (STEAM) | 41 | 2026-10-17 | 83 | 81% |  |
| 104 | [x] | Amnesia: The Dark Descent (STEAM) | 41 | 2026-10-17 | 76 | 75% |  |
| 105 | [x] | Cobalt Core (STEAM) | 40 | 2026-10-18 | 92 | 89% |  |
| 106 | [x] | Rogue Legacy (STEAM) | 40 | 2026-10-17 | 90 | 56% |  |
| 107 | [x] | Rayman Origins (STEAM) | 40 | 2026-10-17 | 88 | 83% |  |
| 108 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 40 | 2026-10-27 | 41 | 85% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 109 | [x] | Salt and Sanctuary (STEAM) | 39 | 2026-10-18 | 78 | 81% |  |
| 110 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 39 | 2026-10-17 | 74 | 98% |  |
| 111 | [x] | Capcom Arcade Stadium (STEAM) | 39 | 2026-10-17 | 48 | 76% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 112 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-10-23 | 40 | 76% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 113 | [x] | CrossCode (GOG) | 38 | 2026-10-23 | 42 | 71% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 114 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 2026-10-17 | 69 | 88% |  |
| 115 | [x] | Tales of ARISE (STEAM) | 37 | 2026-10-16 | 66 | 94% |  |
| 116 | [x] | Hearts of Iron IV (STEAM) | 36 | 2026-10-19 | 63 | 67% |  |
| 117 | [x] | Teardown (STEAM) | 35 | 2026-10-17 | 77 | 79% |  |
| 118 | [x] | Sable (EPIC) | 35 | 2026-10-18 | 76 | 86% |  |
| 119 | [x] | POSTAL 2 (GOG) | 35 | 2026-10-22 | 71 | 92% |  |
| 120 | [x] | STAR WARS™ Episode I: Racer (GOG) | 35 | 2026-11-02 | 41 | 82% | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 121 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 34 | 2026-10-16 | 66 | 65% |  |
| 122 | [x] | Rocket League (STEAM) | 34 | 2026-10-17 | 55 | 69% |  |
| 123 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 34 | 2026-10-21 | 47 | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 124 | [x] | SnowRunner (STEAM) | 34 | 2026-10-19 | 47 | 85% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 125 | [x] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 34 | 2026-11-01 | 39 | 64% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 126 | [x] | Journey (STEAM) | 33 | 2026-10-27 | 70 | 53% |  |
| 127 | [x] | Ultimate Chicken Horse (STEAM) | 33 | 2026-10-23 | 69 | 62% |  |
| 128 | [x] | Hero Siege (STEAM) | 33 | 2026-11-02 | 58 | 63% |  |
| 129 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 33 | 2026-10-19 | 54 | 71% |  |
| 130 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 2026-10-19 | 54 | 81% |  |
| 131 | [x] | Capcom Fighting Collection 2 (STEAM) | 33 | 2026-10-18 | 49 | 86% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 132 | [x] | Supermarket Together (STEAM) | 33 | 2026-10-19 | 47 | 72% |  |
| 133 | [x] | Romestead (STEAM) | 33 | 2026-10-18 | 44 | 77% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 134 | [x] | Russian Fishing 4 (STEAM) | 33 | 2026-10-23 | 39 | 75% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 135 | [x] | Hotline Miami (GOG) | 33 | 2026-10-20 | 38 | 69% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 136 | [x] | Bloodstained: Curse of the Moon (STEAM) | 32 | 2026-10-16 | 73 | 69% |  |
| 137 | [x] | Little Nightmares (STEAM) | 32 | 2026-10-16 | 70 | 61% |  |
| 138 | [x] | COCOON (STEAM) | 32 | 2026-10-17 | 61 | 90% |  |
| 139 | [x] | Max Payne (STEAM) | 32 | 2026-10-17 | 58 | 94% |  |
| 140 | [x] | Earthion (STEAM) | 32 | 2026-10-22 | 52 | 100% |  |
| 141 | [x] | Counter-Strike:Global Offensive (STEAM) | 32 | 2026-10-19 | 50 | 78% |  |
| 142 | [x] | Secrets of Grindea (STEAM) | 32 | 2026-10-20 | 50 | 81% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 143 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 32 | 2026-10-18 | 48 | 87% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 144 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-10-20 | 42 | 89% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 145 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 32 | 2026-10-18 | 38 | 72% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 146 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 32 | 2026-10-22 | 37 | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 147 | [x] | Dishonored - Definitive Edition (EPIC) | 31 | 2026-10-17 | 79 | 84% |  |
| 148 | [x] | Torchlight II (STEAM) | 31 | 2026-10-20 | 64 | 90% |  |
| 149 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 31 | 2026-10-26 | 55 | 67% |  |
| 150 | [x] | Resident Evil Village (STEAM) | 31 | 2026-10-17 | 53 | 90% |  |
| 151 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 31 | 2026-10-22 | 50 | 78% |  |
| 152 | [x] | Tower and Sword of Succubus (STEAM) | 31 | 2026-10-22 | 46 | 100% |  |
| 153 | [x] | Palia (STEAM) | 31 | 2026-10-22 | 43 | 79% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 154 | [x] | Nioh: Complete Edition (STEAM) | 31 | 2026-10-20 | 42 | 95% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 155 | [x] | Super Animal Royale (STEAM) | 31 | 2026-10-19 | 41 | 72% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 156 | [x] | Grand Theft Auto III (STEAM) | 31 | 2026-10-17 | 39 | 81% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 157 | [x] | CRUEL (STEAM) | 31 | 2026-10-28 | 37 | 75% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 158 | [x] | Path of Exile 2 (STEAM) | 31 | 2026-10-18 | 37 | 86% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 159 | [x] | Need for Speed™ (STEAM) | 31 | 2026-10-18 | 33 | 60% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 160 | [x] | Ultimate Custom Night (STEAM) | 30 | 2026-10-19 | 42 | 78% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 161 | [x] | Monster Hunter Stories (STEAM) | 29 | 2026-10-17 | 64 | 86% |  |
| 162 | [x] | Stumble Guys (STEAM) | 29 | 2026-10-18 | 61 | 82% |  |
| 163 | [x] | Library Of Ruina (STEAM) | 29 | 2026-10-16 | 60 | 87% |  |
| 164 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 29 | 2026-10-18 | 54 | 82% |  |
| 165 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 2026-10-17 | 54 | 83% |  |
| 166 | [x] | Aethermancer (STEAM) | 29 | 2026-10-18 | 51 | 83% |  |
| 167 | [x] | Heavy Rain (STEAM) | 29 | 2026-10-18 | 50 | 86% |  |
| 168 | [x] | Binary Domain (STEAM) | 29 | 2026-10-18 | 45 | 80% |  |
| 169 | [x] | Dying Light (EPIC) | 28 | 2026-10-17 | 65 | 91% |  |
| 170 | [x] | BioShock™ (GOG) | 28 | 2026-10-18 | 64 | 71% |  |
| 171 | [x] | State of Decay: Year-One (STEAM) | 28 | 2026-10-18 | 60 | 81% |  |
| 172 | [x] | Mortal Kombat X (STEAM) | 28 | 2026-10-17 | 54 | 85% |  |
| 173 | [x] | Prince of Persia: The Sands of Time (STEAM) | 28 | 2026-10-20 | 49 | 91% |  |
| 174 | [x] | Akane (STEAM) | 28 | 2026-10-20 | 47 | 100% |  |
| 175 | [x] | Zero Escape: The Nonary Games (STEAM) | 28 | 2026-10-17 | 46 | 67% |  |
| 176 | [x] | Moonlight Peaks (STEAM) | 28 | 2026-10-20 | 40 | 91% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 177 | [x] | Deus Ex™ GOTY Edition (GOG) | 27 | 2026-10-19 | 41 | 83% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 178 | [x] | Tales of Zestiria (STEAM) | 27 | 2026-10-27 | 33 | 67% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 179 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 26 | 2026-10-19 | 88 | 93% |  |
| 180 | [x] | PlateUp! (STEAM) | 26 | 2026-10-16 | 55 | 85% |  |
| 181 | [x] | G.I. Joe Wrath of Cobra (EPIC) | 26 | 2026-10-19 | 48 | 71% |  |
| 182 | [x] | Prince of Persia (GOG) | 26 | 2026-10-24 | 43 | 91% |  |
| 183 | [x] | Digimon Survive (STEAM) | 26 | 2026-10-23 | 43 | 96% |  |
| 184 | [x] | Gothic II: Gold Classic (STEAM) | 26 | 2026-10-20 | 37 | 72% |  |
| 185 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 26 | 2026-11-03 | 36 | 92% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 186 | [x] | Crab Game (STEAM) | 26 | 2026-10-22 | 34 | 78% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 187 | [x] | Persona 5 Strikers (STEAM) | 26 | 2026-11-04 | 29 | 60% | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 188 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 25 | 2026-10-19 | 62 | 84% |  |
| 189 | [x] | Cave Story+ (EPIC) | 25 | 2026-10-18 | 50 | 87% |  |
| 190 | [x] | Unturned (STEAM) | 25 | 2026-10-17 | 46 | 78% |  |
| 191 | [x] | Being a DIK (STEAM) | 25 | 2026-10-19 | 43 | 83% |  |
| 192 | [x] | Battle Brothers (STEAM) | 25 | 2026-10-27 | 40 | 67% |  |
| 193 | [x] | Limbus Company (STEAM) | 25 | 2026-10-18 | 39 | 75% |  |
| 194 | [x] | Changed (STEAM) | 25 | 2026-10-24 | 38 | 88% |  |
| 195 | [x] | Return to Monkey Island (STEAM) | 25 | 2026-10-23 | 38 | 86% |  |
| 196 | [x] | Bongo Cat (STEAM) | 25 | 2026-10-20 | 35 | 81% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 197 | [x] | Beyond: Two Souls (STEAM) | 25 | 2026-10-22 | 33 | 70% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 198 | [x] | Goose Goose Duck (STEAM) | 25 | 2026-10-25 | 33 | 72% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 199 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-10-21 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 200 | [x] | Tearscape (STEAM) | 25 | 2026-10-30 | 29 | 93% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 201 | [x] | Resident Evil (GOG) | 25 | 2026-10-20 | 27 | 61% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 202 | [x] | CarX Drift Racing Online (STEAM) | 24 | 2026-10-16 | 58 | 73% |  |
| 203 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 54 | 86% |  |
| 204 | [x] | WEBFISHING (STEAM) | 24 | 2026-10-17 | 51 | 89% |  |
| 205 | [x] | Goat Simulator (STEAM) | 24 | 2026-11-01 | 45 | 62% |  |
| 206 | [x] | Counter-Strike: Condition Zero (STEAM) | 24 | 2026-10-17 | 42 | 60% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 207 | [x] | Wizard of Legend (EPIC) | 24 | 2026-10-18 | 41 | 80% |  |
| 208 | [x] | Cat Mail Co. (STEAM) | 24 | 2026-10-24 | 40 | 89% |  |
| 209 | [x] | Opus Magnum (STEAM) | 24 | 2026-11-01 | 38 | 83% |  |
| 210 | [x] | Borderlands: The Pre-Sequel (EPIC) | 24 | 2026-10-30 | 34 | 65% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 211 | [x] | Owlboy (STEAM) | 23 | 2026-11-02 | 51 | 46% |  |
| 212 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 23 | 2026-10-20 | 50 | 83% |  |
| 213 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 23 | 2026-10-27 | 47 | 24% |  |
| 214 | [x] | Football Manager 2024 (EPIC) | 23 | 2026-10-20 | 41 | 89% |  |
| 215 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-10-19 | 41 | 95% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 216 | [x] | SWORN (STEAM) | 23 | 2026-10-23 | 38 | 100% |  |
| 217 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 2026-10-17 | 36 | 79% |  |
| 218 | [x] | Timberborn (STEAM) | 23 | 2026-10-25 | 35 | 83% |  |
| 219 | [x] | Party Animals (STEAM) | 23 | 2026-10-17 | 32 | 71% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 220 | [x] | Jade Empire: Special Edition (GOG) | 23 | 2026-10-23 | 31 | 72% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 221 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 23 | 2026-10-25 | 31 | 73% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 222 | [x] | CarX Street (STEAM) | 23 | 2026-11-04 | 30 | 82% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 223 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 96% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 224 | [x] | Jade Empire: Special Edition (STEAM) | 23 | 2026-11-01 | 26 | 67% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 225 | [x] | ABZÛ (STEAM) | 22 | 2026-10-21 | 53 | 90% |  |
| 226 | [x] | Titan Quest Anniversary Edition (STEAM) | 22 | 2026-10-16 | 53 | 85% |  |
| 227 | [x] | Saints Row IV (STEAM) | 22 | 2026-10-19 | 51 | 72% |  |
| 228 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 22 | 2026-10-24 | 42 | 91% |  |
| 229 | [x] | Pinball FX Classic (STEAM) | 22 | 2026-10-23 | 40 | 91% |  |
| 230 | [x] | This War of Mine (STEAM) | 22 | 2026-10-21 | 40 | 76% |  |
| 231 | [x] | Life is Strange Remastered (STEAM) | 22 | 2026-10-20 | 34 | 89% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 232 | [x] | Need for Speed™ Unbound (STEAM) | 22 | 2026-10-26 | 30 | 79% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 233 | [x] | Capcom Fighting Collection (STEAM) | 22 | 2026-10-23 | 27 | 76% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 234 | [x] | BlazBlue Centralfiction (STEAM) | 21 | 2026-10-17 | 61 | 82% |  |
| 235 | [x] | Slow Roads (STEAM) | 21 | 2026-10-22 | 46 | 97% |  |
| 236 | [x] | Hatred (STEAM) | 21 | 2026-10-22 | 45 | 86% |  |
| 237 | [x] | Overlord (STEAM) | 21 | 2026-11-03 | 40 | 62% |  |
| 238 | [x] | Trailmakers (STEAM) | 21 | 2026-10-21 | 39 | 94% |  |
| 239 | [x] | One-armed robber (STEAM) | 21 | 2026-10-23 | 38 | 79% |  |
| 240 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 21 | 2026-10-21 | 37 | 100% |  |
| 241 | [x] | Tiny Glade (STEAM) | 21 | 2026-10-24 | 36 | 68% |  |
| 242 | [x] | GOD EATER RESURRECTION (STEAM) | 21 | 2026-11-01 | 32 | 60% |  |
| 243 | [x] | Nex Machina (STEAM) | 21 | 2026-10-18 | 28 | 79% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 244 | [x] | No Rest for the Wicked (STEAM) | 20 | 2026-10-19 | 43 | 76% |  |
| 245 | [x] | Paper Lily - Chapter 1 (STEAM) | 20 | 2026-10-27 | 40 | 94% |  |
| 246 | [x] | Brothers - A Tale of Two Sons (EPIC) | 20 | 2026-10-23 | 39 | 73% |  |
| 247 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-10-20 | 39 | 100% |  |
| 248 | [x] | Mafia: Definitive Edition (STEAM) | 20 | 2026-10-28 | 37 | 82% |  |
| 249 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 20 | 2026-11-04 | 27 | 83% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 250 | [x] | BAJA: Edge of Control HD (STEAM) | 20 | 2026-10-28 | 26 | 90% | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 251 | [x] | Dead Island (STEAM) | 20 | 2026-10-20 | 26 | 75% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 252 | [x] | Tyr (STEAM) | 20 | 2026-11-02 | 26 | 82% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 253 | [x] | MudRunner (EPIC) | 19 | 2026-10-18 | 40 | 88% |  |
| 254 | [x] | Killing Floor (STEAM) | 19 | 2026-10-19 | 34 | 88% |  |
| 255 | [x] | My Summer Car (STEAM) | 19 | 2026-10-30 | 34 | 86% |  |
| 256 | [x] | Stick It to the Stickman (STEAM) | 19 | 2026-10-17 | 34 | 76% |  |
| 257 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 19 | 2026-10-21 | 33 | 68% |  |
| 258 | [x] | Metro Exodus (STEAM) | 19 | 2026-10-20 | 31 | 90% |  |
| 259 | [x] | Sonic and SEGA All Stars Racing (STEAM) | 19 | 2026-10-19 | 28 | 75% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 260 | [x] | Torchlight II (EPIC) | 19 | 2026-10-22 | 27 | 100% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 261 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 19 | 2026-10-23 | 24 | 94% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 262 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 18 | 2026-10-25 | 41 | 67% |  |
| 263 | [x] | Styx: Master of Shadows (EPIC) | 18 | 2026-11-03 | 39 | 38% |  |
| 264 | [x] | Graveyard Keeper (GOG) | 18 | 2026-10-25 | 38 | 21% |  |
| 265 | [x] | Faster Than Light (EPIC) | 18 | 2026-10-24 | 36 | 94% |  |
| 266 | [x] | Backpack Battles (STEAM) | 18 | 2026-10-21 | 36 | 97% |  |
| 267 | [x] | SKALD: Against the Black Priory (STEAM) | 18 | 2026-10-20 | 36 | 97% |  |
| 268 | [x] | Far Far West (STEAM) | 18 | 2026-10-21 | 32 | 77% |  |
| 269 | [x] | Hitman: Absolution (GOG) | 18 | 2026-10-24 | 30 | 84% |  |
| 270 | [x] | Tabletop Simulator (STEAM) | 18 | 2026-10-19 | 30 | 65% |  |
| 271 | [x] | Formula Legends (STEAM) | 18 | 2026-10-21 | 28 | 65% |  |
| 272 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 18 | 2026-10-21 | 27 | 93% |  |
| 273 | [x] | Arcade Paradise (EPIC) | 18 | 2026-10-25 | 26 | 82% |  |
| 274 | [x] | DOOM 3: BFG Edition (GOG) | 18 | 2026-10-19 | 25 | 80% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 275 | [x] | Katanaut (STEAM) | 18 | 2026-10-20 | 25 | 69% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 276 | [x] | Dorfromantik (GOG) | 18 | 2026-11-04 | 23 | 64% | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 277 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-01 | 23 | 77% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 278 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 17 | 2026-10-20 | 35 | 73% |  |
| 279 | [x] | Mini Metro (STEAM) | 17 | 2026-11-01 | 35 | 54% |  |
| 280 | [x] | Spin Rhythm XD (STEAM) | 17 | 2026-10-18 | 35 | 84% |  |
| 281 | [x] | CULTIC (STEAM) | 17 | 2026-10-24 | 33 | 61% |  |
| 282 | [x] | No More Heroes (STEAM) | 17 | 2026-11-03 | 33 | 62% |  |
| 283 | [x] | Lost Castle 2 (STEAM) | 17 | 2026-11-02 | 32 | 100% |  |
| 284 | [x] | SCP – Containment Breach (STEAM) | 17 | 2026-10-27 | 32 | 83% |  |
| 285 | [x] | GRANDIA HD Remaster (STEAM) | 17 | 2026-10-22 | 31 | 68% |  |
| 286 | [x] | GRIP: Combat Racing (STEAM) | 17 | 2026-10-20 | 31 | 83% |  |
| 287 | [x] | Shank 2 (STEAM) | 17 | 2026-10-27 | 30 | 100% |  |
| 288 | [x] | Maneater (STEAM) | 17 | 2026-10-20 | 27 | 77% |  |
| 289 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 17 | 2026-10-20 | 27 | 78% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 290 | [x] | Grim Fandango Remastered (GOG) | 17 | 2026-11-03 | 25 | 60% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 291 | [x] | Fall Guys (STEAM) | 17 | 2026-10-26 | 23 | 93% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 292 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 293 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 294 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 51 | 96% |  |
| 295 | [x] | No Man's Sky (GOG) | 16 | 2026-10-19 | 37 | 76% |  |
| 296 | [x] | Grim Fandango Remastered (STEAM) | 16 | 2026-10-19 | 36 | 77% |  |
| 297 | [x] | Kingdom Come: Deliverance II (STEAM) | 16 | 2026-10-20 | 35 | 100% |  |
| 298 | [x] | DNF Duel (EPIC) | 16 | 2026-10-21 | 29 | 90% |  |
| 299 | [x] | Titanfall® 2 (STEAM) | 16 | 2026-10-16 | 28 | 82% |  |
| 300 | [x] | WORLD OF FINAL FANTASY (STEAM) | 16 | 2026-10-19 | 27 | 78% |  |
| 301 | [x] | Dishonored 2 (STEAM) | 16 | 2026-10-20 | 26 | 92% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 302 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 2026-10-21 | 22 | 85% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 303 | [x] | Content Warning (STEAM) | 16 | 2026-11-04 | 21 | 90% | [#241](https://github.com/GameNative/gamenative-compat/issues/241) |
| 304 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-04 | 20 | 90% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 305 | [x] | Jotunnslayer: Hordes of Hel (STEAM) | 16 | 2026-10-30 | 20 | 91% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 306 | [x] | Antichamber (STEAM) | 15 | 2026-10-20 | 30 | 88% |  |
| 307 | [x] | Mark of the Ninja (STEAM) | 15 | 2026-10-26 | 30 | 64% |  |
| 308 | [x] | Wildermyth (STEAM) | 15 | 2026-10-26 | 26 | 94% |  |
| 309 | [x] | LET IT DIE (STEAM) | 15 | 2026-10-25 | 25 | 73% |  |
| 310 | [x] | Mortal Shell (EPIC) | 15 | 2026-10-19 | 24 | 88% |  |
| 311 | [x] | Batman™: Arkham Origins (GOG) | 15 | 2026-10-22 | 24 | 93% |  |
| 312 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 15 | 2026-10-20 | 23 | 67% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 313 | [x] | Allumeria (STEAM) | 15 | 2026-10-23 | 22 | 69% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 314 | [x] | Chef Knight (STEAM) | 15 | 2026-10-27 | 22 | 69% |  |
| 315 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 316 | [x] | Cyberpunk 2077 (EPIC) | 15 | 2026-10-19 | 20 | 81% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 317 | [x] | Maneater (EPIC) | 15 | 2026-10-28 | 20 | 79% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 318 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 319 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 91% |  |
| 320 | [x] | Rayman Origins (GOG) | 14 | 2026-11-02 | 29 | 53% |  |
| 321 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 2026-10-29 | 28 | 85% |  |
| 322 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 14 | 2026-10-21 | 25 | 93% |  |
| 323 | [x] | Ultrapool (STEAM) | 14 | 2026-10-24 | 25 | 100% |  |
| 324 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 2026-10-25 | 24 | 73% |  |
| 325 | [x] | Gloomwood (STEAM) | 14 | 2026-10-29 | 24 | 75% |  |
| 326 | [x] | Alabaster Dawn Demo (STEAM) | 14 | 2026-10-27 | 23 | 89% |  |
| 327 | [x] | Super Monkey Ball Banana Mania (STEAM) | 14 | 2026-10-18 | 23 | 65% |  |
| 328 | [x] | Songs of Conquest (EPIC) | 14 | 2026-11-02 | 22 | 90% |  |
| 329 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-10-23 | 22 | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 330 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 331 | [x] | Sons Of The Forest (STEAM) | 14 | 2026-10-19 | 22 | 77% |  |
| 332 | [x] | Horny Villa (STEAM) | 14 | 2026-10-21 | 20 | 95% |  |
| 333 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 334 | [x] | Middle-earth™: Shadow of War™ (STEAM) | 13 | 2026-10-16 | 39 | 74% |  |
| 335 | [x] | Blood: Fresh Supply (STEAM) | 13 | 2026-10-16 | 36 | 80% |  |
| 336 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 13 | 2026-10-21 | 34 | 83% |  |
| 337 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 32 | 63% |  |
| 338 | [x] | Distance (STEAM) | 13 | 2026-10-19 | 31 | 83% |  |
| 339 | [x] | Breath of Fire IV (GOG) | 13 | 2026-10-26 | 28 | 67% |  |
| 340 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 13 | 2026-11-01 | 28 | 55% |  |
| 341 | [x] | Dead Space™ 3 (STEAM) | 13 | 2026-10-20 | 28 | 74% |  |
| 342 | [x] | Haiku, the Robot (STEAM) | 13 | 2026-10-21 | 28 | 85% |  |
| 343 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 13 | 2026-10-18 | 28 | 92% |  |
| 344 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 28 | 48% |  |
| 345 | [x] | Aperture Desk Job (STEAM) | 13 | 2026-11-03 | 27 | n/a |  |
| 346 | [x] | Human Fall Flat (STEAM) | 13 | 2026-10-29 | 26 | 66% |  |
| 347 | [x] | Lust Goddess (STEAM) | 13 | 2026-10-26 | 25 | 67% |  |
| 348 | [x] | Look Outside (GOG) | 13 | 2026-11-01 | 24 | 100% |  |
| 349 | [x] | Haydee (STEAM) | 13 | 2026-10-22 | 24 | 82% |  |
| 350 | [x] | Pillars of Eternity (STEAM) | 13 | 2026-10-26 | 24 | 65% |  |
| 351 | [x] | DiRT 4 (STEAM) | 13 | 2026-10-20 | 23 | 96% |  |
| 352 | [x] | 12 is Better Than 6 (STEAM) | 13 | 2026-10-21 | 22 | 85% |  |
| 353 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-10-21 | 22 | 92% |  |
| 354 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 13 | 2026-10-28 | 21 | 64% |  |
| 355 | [x] | Secret of Mana (STEAM) | 13 | 2026-10-28 | 21 | 64% |  |
| 356 | [x] | Shift At Midnight (STEAM) | 13 | 2026-11-01 | 21 | 91% |  |
| 357 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 358 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 13 | 2026-10-23 | 20 | 61% |  |
| 359 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 81% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 360 | [x] | The WereCleaner (STEAM) | 12 | 2026-10-22 | 31 | 91% |  |
| 361 | [x] | Tom Clancy's Splinter Cell: Chaos Theory (STEAM) | 12 | 2026-10-16 | 30 | 85% |  |
| 362 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 12 | 2026-10-19 | 29 | 98% |  |
| 363 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 26 | 70% |  |
| 364 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-10-28 | 24 | 93% |  |
| 365 | [x] | Sonic Superstars (STEAM) | 12 | 2026-10-21 | 24 | 66% |  |
| 366 | [x] | Sid Meier's Civilization VI (EPIC) | 12 | 2026-10-19 | 23 | 90% |  |
| 367 | [x] | UNDEFEATED (STEAM) | 12 | 2026-11-01 | 23 | 82% |  |
| 368 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-10-22 | 22 | 89% |  |
| 369 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 2026-10-26 | 22 | 89% |  |
| 370 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 92% |  |
| 371 | [x] | Human Resource Machine (EPIC) | 12 | 2026-11-01 | 20 | 64% |  |
| 372 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 373 | [x] | PAYDAY: The Heist (STEAM) | 12 | 2026-11-02 | 20 | 75% |  |
| 374 | [x] | Mortal Kombat 11 (STEAM) | 11 | 2026-10-28 | 27 | 68% |  |
| 375 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 2026-10-27 | 23 | 80% |  |
| 376 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 23 | 80% |  |
| 377 | [x] | Castle in the Clouds (STEAM) | 11 | 2026-10-21 | 22 | 85% |  |
| 378 | [x] | Injustice™ 2 (STEAM) | 11 | 2026-10-17 | 22 | 73% |  |
| 379 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 11 | 2026-10-23 | 22 | 94% |  |
| 380 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 2026-10-25 | 21 | 95% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 381 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-10-24 | 21 | 74% |  |
| 382 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 383 | [x] | TowerFall Ascension (STEAM) | 10 | 2026-10-16 | 30 | 53% |  |
| 384 | [x] | Possessor(s) (STEAM) | 10 | 2026-10-24 | 27 | 100% |  |
| 385 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 10 | 2026-10-20 | 25 | 72% |  |
| 386 | [x] | Divinity: Original Sin (Classic) (STEAM) | 10 | 2026-10-16 | 23 | 83% |  |
| 387 | [x] | Mina the Hollower (GOG) | 10 | 2026-10-28 | 22 | 53% |  |
| 388 | [x] | SteamWorld Heist (GOG) | 10 | 2026-10-25 | 22 | 60% |  |
| 389 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 22 | 89% |  |
| 390 | [x] | DRAGON BALL XENOVERSE (STEAM) | 10 | 2026-10-28 | 21 | 58% |  |
| 391 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 392 | [x] | Coromon (GOG) | 10 | 2026-10-19 | 20 | 61% |  |
| 393 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 394 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 395 | [x] | What Remains of Edith Finch (STEAM) | 9 | 2026-10-19 | 26 | 50% |  |
| 396 | [x] | Delver (STEAM) | 9 | 2026-10-17 | 22 | 76% |  |
| 397 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 9 | 2026-10-23 | 22 | 69% |  |
| 398 | [x] | Football Manager 2024 (STEAM) | 9 | 2026-10-16 | 20 | n/a |  |
| 399 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 8% |  |
| 400 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 9 | 2026-10-20 | 20 | n/a |  |
| 401 | [x] | Gloomhaven (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 402 | [x] | Intravenous (STEAM) | 8 | 2026-10-16 | 20 | 94% |  |
| 403 | [x] | Mafia II: Definitive Edition (STEAM) | 7 | 2026-10-16 | 20 | n/a |  |
| 404 | [x] | Alex Kidd in Miracle World DX (STEAM) | 2 | 2026-10-16 | 36 | 87% |  |
