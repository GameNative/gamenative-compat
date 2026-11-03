# GameNative compatibility worklist

Generated: `2026-11-03T04:15:06.138Z` · App release: `1.3.0` · Ratings since: `2026-08-05T04:15:06.138Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 260 |
| Probably does not work | 70 |
| First launch fails | 370 |
| Mixed | 466 |
| Works | 1021 |
| Total | 2187 |

## Does not work (260)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [x] 2026-10-18 | Project Zomboid (STEAM) | 602 | 636 | 93% (1.3.0) | Does not open (66%) | 53% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 2 | [x] 2026-10-18 | Alan Wake (STEAM) | 255 | 266 | 90% (1.3.0) | Does not open (87%) | 9% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 3 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 247 | 266 | 93% (90d) | Does not open (76%) | 11% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 4 | [ ] | Counter-Strike 2 (STEAM) | 228 | 313 | 81% (1.3.0) | Does not open (61%) | 43% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 5 | [x] 2026-10-18 | Call of Duty: Black Ops (STEAM) | 214 | 225 | 95% (90d) | Does not open (75%) | 12% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 6 | [ ] | skate. (STEAM) | 197 | 212 | 93% (90d) | Does not open (80%) | 16% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 7 | [x] 2026-10-18 | Sid Meier's Civilization V (STEAM) | 179 | 191 | 94% (90d) | Does not open (76%) | 56% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 8 | [ ] | Necesse (STEAM) | 160 | 165 | 97% (90d) | Does not open (80%) | 51% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 9 | [ ] | Peggle Deluxe (STEAM) | 153 | 184 | 83% (90d) | Does not open (92%) | 37% | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 10 | [ ] | HELLDIVERS™ 2 (STEAM) | 139 | 145 | 96% (90d) | Does not open (92%) | 26% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 11 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 134 | 149 | 90% (90d) | Does not open (87%) | 44% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 12 | [ ] | Assassin's Creed II (STEAM) | 126 | 131 | 96% (90d) | Does not open (77%) | 50% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 13 | [ ] | Dust: An Elysian Tail (STEAM) | 108 | 112 | 96% (90d) | Does not open (72%) | 7% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 14 | [ ] | The Witcher: Enhanced Edition (GOG) | 104 | 114 | 91% (90d) | Does not open (73%) | 13% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 15 | [ ] | Call of Duty: Black Ops II (STEAM) | 101 | 134 | 85% (1.3.0) | Does not open (78%) | 25% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 16 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 101 | 114 | 89% (90d) | No graphics (59%) | 53% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 17 | [ ] | Mafia II (Classic) (STEAM) | 96 | 101 | 95% (90d) | Does not open (72%) | 6% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 18 | [ ] | Saints Row 2 (STEAM) | 94 | 106 | 92% (1.3.0) | Does not open (96%) | 42% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 19 | [ ] | Transistor (STEAM) | 93 | 93 | 100% (90d) | Does not open (75%) | 0% | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 20 | [ ] | Saints Row: The Third (STEAM) | 91 | 92 | 99% (90d) | Does not open (77%) | 27% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 21 | [ ] | Duskfade (STEAM) | 87 | 89 | 98% (90d) | Does not open (95%) | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 22 | [ ] | Black Mesa (STEAM) | 85 | 117 | 73% (90d) | Does not open (82%) | 12% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 23 | [ ] | Sniper Elite 4 (STEAM) | 83 | 83 | 100% (90d) | Does not open (97%) | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 24 | [ ] | Fall Guys (EPIC) | 82 | 94 | 87% (90d) | Does not open (75%) | 11% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 25 | [ ] | HELLDIVERS™ (STEAM) | 81 | 95 | 85% (90d) | Does not open (59%) | 43% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 26 | [ ] | Dead Space 2 (STEAM) | 79 | 100 | 79% (90d) | Does not open (74%) | 35% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 27 | [ ] | GRID 2 (STEAM) | 77 | 80 | 96% (90d) | Does not open (67%) | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 28 | [ ] | MECCHA CHAMELEON (STEAM) | 76 | 108 | 70% (90d) | Does not open (64%) | 59% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 29 | [ ] | The Wolf Among Us (STEAM) | 74 | 83 | 89% (90d) | Does not open (68%) | 13% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 30 | [ ] | Gorilla Tag (STEAM) | 72 | 120 | 71% (1.3.0) | Does not open (70%) | 21% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 31 | [ ] | Marvel Rivals (STEAM) | 71 | 79 | 90% (90d) | Does not open (81%) | 0% | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 32 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 71 | 77 | 92% (90d) | Does not open (70%) | 0% | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 33 | [ ] | Burnout™ Paradise Remastered (STEAM) | 71 | 74 | 96% (90d) | Does not open (88%) | 18% | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 34 | [ ] | Call of Duty: Black Ops II - Zombies (STEAM) | 70 | 86 | 81% (90d) | Does not open (70%) | 50% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 35 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 68 | 73 | 93% (90d) | Does not open (79%) | 8% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 36 | [x] 2026-10-18 | Diablo® IV (STEAM) | 67 | 79 | 85% (90d) | Does not open (61%) | 23% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 37 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 67 | 76 | 88% (90d) | Does not open (47%) | 26% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 38 | [ ] | Door Kickers 2 (STEAM) | 67 | 71 | 94% (90d) | No graphics (85%) | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 39 | [ ] | Borderlands GOTY (STEAM) | 66 | 71 | 93% (90d) | Does not open (95%) | 25% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 40 | [ ] | Saints Row 2 (GOG) | 65 | 78 | 83% (90d) | Does not open (96%) | 49% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 41 | [ ] | Metro 2033 (STEAM) | 64 | 80 | 80% (90d) | Does not open (64%) | 44% | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 42 | [ ] | GRID (STEAM) | 63 | 79 | 80% (90d) | Does not open (57%) | 51% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 43 | [ ] | Need for Speed™ Heat  (STEAM) | 63 | 77 | 82% (90d) | Does not open (78%) | 28% | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 44 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 63 | 63 | 100% (90d) | No graphics (54%) | 8% | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 45 | [ ] | Three Kingdoms : Alias (STEAM) | 62 | 66 | 94% (90d) | No graphics (97%) | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 46 | [ ] | XCOM: Enemy Unknown (STEAM) | 61 | 64 | 95% (90d) | Does not open (75%) | 7% | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 47 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 60 | 86 | 70% (90d) | Does not open (84%) | 52% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 48 | [ ] | Spore (STEAM) | 60 | 65 | 92% (90d) | Does not open (69%) | 36% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 49 | [ ] | DOOM (2016) (GOG) | 58 | 64 | 91% (90d) | Does not open (90%) | 43% | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 50 | [ ] | GrandChase (STEAM) | 57 | 60 | 95% (90d) | Does not open (85%) | 13% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 51 | [ ] | Enshrouded (STEAM) | 56 | 57 | 98% (90d) | Does not open (95%) | 19% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 52 | [ ] | Overwatch® (STEAM) | 55 | 57 | 96% (90d) | Does not open (58%) | 20% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 53 | [ ] | Fortune Mill (STEAM) | 54 | 55 | 98% (90d) | Does not open (89%) | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 54 | [ ] | STAR WARS Zero Company™ (STEAM) | 53 | 55 | 96% (90d) | Does not open (64%) | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 55 | [ ] | Spec Ops: The Line (STEAM) | 53 | 54 | 98% (90d) | No graphics (56%) | 0% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 56 | [ ] | Watch_Dogs (STEAM) | 52 | 67 | 78% (90d) | Does not open (90%) | 19% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 57 | [ ] | Max Payne 3 (STEAM) | 52 | 57 | 91% (90d) | Does not open (93%) | 43% | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 58 | [ ] | South Park The Fractured But Whole (STEAM) | 52 | 52 | 100% (90d) | Does not open (66%) | 15% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 59 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 51 | 67 | 76% (90d) | Does not open (80%) | 39% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 60 | [ ] | Split/Second (STEAM) | 51 | 60 | 85% (90d) | Does not open (76%) | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 61 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 50 | 64 | 78% (90d) | Does not open (90%) | 55% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 62 | [ ] | Sandustry (STEAM) | 50 | 62 | 81% (90d) | Does not open (73%) | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 63 | [ ] | METAL SLUG 3 (STEAM) | 50 | 58 | 86% (90d) | Does not open (80%) | 19% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 64 | [ ] | RoboCop: Rogue City (STEAM) | 50 | 54 | 93% (90d) | Does not open (37%) | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 65 | [ ] | Trackmania (STEAM) | 49 | 62 | 79% (90d) | Does not open (85%) | 39% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 66 | [ ] | Hitman: Absolution (STEAM) | 49 | 54 | 91% (90d) | Does not open (84%) | 7% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 67 | [ ] | Scott Pilgrim vs The World (STEAM) | 49 | 49 | 100% (90d) | Does not open (83%) | 47% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 68 | [ ] | Asphalt Legends  (STEAM) | 48 | 56 | 86% (90d) | Does not open (80%) | 47% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 69 | [ ] | DOOM Eternal (STEAM) | 48 | 50 | 96% (90d) | Does not open (69%) | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 70 | [ ] | Aliens vs. Predator (STEAM) | 47 | 52 | 90% (90d) | No graphics (53%) | 25% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 71 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 47 | 49 | 96% (90d) | No graphics (63%) | 18% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 72 | [ ] | tModLoader (STEAM) | 46 | 53 | 87% (90d) | Does not open (86%) | 4% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 73 | [ ] | STAR WARS™ Republic Commando (STEAM) | 46 | 48 | 96% (90d) | Does not open (80%) | 47% | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 74 | [ ] | State of Decay 2 (STEAM) | 45 | 63 | 71% (90d) | Does not open (93%) | 0% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 75 | [ ] | Prince of Persia The Lost Crown (STEAM) | 45 | 49 | 92% (90d) | Does not open (94%) | 38% | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 76 | [ ] | Mafia: Definitive Edition (GOG) | 44 | 58 | 76% (90d) | Does not open (86%) | 26% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 77 | [ ] | Diablo + Hellfire (GOG) | 44 | 50 | 88% (90d) | Does not open (65%) | 33% | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 78 | [ ] | ARC Raiders (STEAM) | 44 | 49 | 90% (90d) | Does not open (93%) | 0% | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 79 | [ ] | To The Moon (GOG) | 44 | 48 | 96% (1.3.0) | Does not open (86%) | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 80 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 44 | 47 | 94% (90d) | Does not open (95%) | 55% | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 81 | [ ] | The Survivalists (STEAM) | 44 | 46 | 96% (90d) | Does not open (98%) | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 82 | [ ] | Tales of Berseria (STEAM) | 44 | 45 | 98% (90d) | Does not open (88%) | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 83 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 43 | 44 | 98% (90d) | Does not open (84%) | 46% | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 84 | [ ] | Need for Speed™ Rivals (STEAM) | 42 | 50 | 84% (90d) | Does not open (61%) | 40% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 85 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 41 | 45 | 91% (90d) | Does not open (71%) | 26% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 86 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 41 | 42 | 98% (90d) | Does not open (63%) | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 87 | [ ] | Elite Dangerous (STEAM) | 39 | 42 | 93% (90d) | Does not open (77%) | 47% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 88 | [ ] | L.A. Noire (STEAM) | 38 | 45 | 84% (90d) | Does not open (96%) | 52% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 89 | [ ] | Mafia (STEAM) | 38 | 43 | 88% (90d) | Does not open (69%) | 42% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 90 | [ ] | DJMAX RESPECT V (STEAM) | 38 | 42 | 90% (90d) | Does not open (82%) | 30% | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 91 | [ ] | Marvel's Spider-Man 2 (STEAM) | 38 | 40 | 95% (90d) | Does not open (87%) | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 92 | [ ] | GeoGuessr Steam Edition (STEAM) | 38 | 39 | 97% (90d) | No graphics (62%) | n/a | [#154](https://github.com/GameNative/gamenative-compat/issues/154) |
| 93 | [ ] | ScourgeBringer (STEAM) | 37 | 42 | 88% (90d) | Does not open (69%) | 6% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 94 | [ ] | BIT.TRIP RUNNER (STEAM) | 37 | 39 | 95% (90d) | Does not open (59%) | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 95 | [ ] | Dragon's Dogma 2 (STEAM) | 37 | 38 | 97% (90d) | Does not open (91%) | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 96 | [ ] | Beat Saber (STEAM) | 36 | 42 | 86% (90d) | Does not open (45%) | 34% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 97 | [ ] | Barotrauma (STEAM) | 36 | 39 | 92% (90d) | Does not open (97%) | 36% | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 98 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 36 | 38 | 95% (90d) | Does not open (94%) | 27% | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 99 | [ ] | Forza Horizon 6 (STEAM) | 36 | 37 | 97% (90d) | Does not open (62%) | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 100 | [ ] | CODE VEIN (STEAM) | 35 | 49 | 71% (90d) | Does not open (68%) | 34% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 101 | [ ] | CARRION (GOG) | 35 | 43 | 81% (90d) | Does not open (73%) | 8% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 102 | [ ] | FINAL FANTASY VIII (STEAM) | 35 | 43 | 81% (90d) | Does not open (65%) | 45% | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 103 | [ ] | GOALS (STEAM) | 35 | 41 | 85% (90d) | Does not open (83%) | 24% | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 104 | [ ] | BattleBit Remastered (STEAM) | 35 | 39 | 90% (90d) | Does not open (61%) | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 105 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 35 | 36 | 97% (90d) | No graphics (62%) | 6% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 106 | [ ] | Utopia Must Fall (STEAM) | 35 | 35 | 100% (90d) | Does not open (83%) | n/a | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 107 | [ ] | Metro: Last Light Redux (STEAM) | 34 | 92 | 76% (1.3.0) | Does not open (91%) | 42% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 108 | [ ] | OneShot (STEAM) | 34 | 38 | 89% (90d) | Does not open (97%) | 20% | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 109 | [ ] | Muv-Luv (STEAM) | 34 | 35 | 97% (90d) | Does not open (86%) | 39% | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 110 | [ ] | Yume Nikki (STEAM) | 33 | 56 | 71% (14d) | Does not open (91%) | 0% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 111 | [ ] | Lost Planet: Extreme Condition (STEAM) | 33 | 41 | 80% (90d) | Does not open (77%) | 48% | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 112 | [ ] | Death Stranding (EPIC) | 33 | 36 | 92% (90d) | Does not open (75%) | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 113 | [ ] | The Darkness II (STEAM) | 33 | 33 | 100% (90d) | Does not open (83%) | 23% | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 114 | [ ] | Gauntlet™  (STEAM) | 32 | 46 | 70% (90d) | Does not open (67%) | 42% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 115 | [ ] | Mafia II (Classic) (GOG) | 32 | 46 | 70% (90d) | Does not open (96%) | 28% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 116 | [ ] | CPM 2 (STEAM) | 32 | 40 | 80% (90d) | Does not open (91%) | 10% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 117 | [ ] | Insaniquarium! Deluxe (STEAM) | 32 | 39 | 82% (90d) | Does not open (86%) | 35% | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 118 | [ ] | Mass Effect (2007) (STEAM) | 32 | 38 | 84% (90d) | Does not open (81%) | 50% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 119 | [ ] | Wolfenstein 3D (STEAM) | 32 | 35 | 91% (90d) | Does not open (50%) | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 120 | [ ] | Quantum Break (STEAM) | 32 | 32 | 100% (90d) | Does not open (91%) | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 121 | [ ] | Beholder (EPIC) | 31 | 36 | 86% (90d) | Does not open (65%) | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 122 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 31 | 34 | 91% (90d) | Does not open (81%) | 25% | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 123 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 31 | 34 | 91% (90d) | Does not open (67%) | 0% | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 124 | [ ] | Forza Horizon 5 (STEAM) | 31 | 33 | 94% (90d) | Does not open (67%) | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 125 | [ ] | Umamusume: Pretty Derby (STEAM) | 31 | 33 | 94% (90d) | Does not open (86%) | n/a | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 126 | [ ] | Rayman Legends (STEAM) | 31 | 32 | 97% (90d) | Does not open (96%) | 41% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 127 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 31 | 31 | 100% (90d) | Does not open (69%) | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 128 | [ ] | Metro: Last Light Complete Edition (STEAM) | 30 | 37 | 81% (90d) | Does not open (58%) | 57% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 129 | [ ] | Far Cry 4 (STEAM) | 30 | 34 | 88% (90d) | Does not open (100%) | 27% | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 130 | [ ] | King's Bounty: The Legend (STEAM) | 30 | 34 | 88% (90d) | Does not open (100%) | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 131 | [ ] | Magicka (STEAM) | 30 | 33 | 91% (90d) | Does not open (64%) | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 132 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 30 | 31 | 97% (90d) | Does not open (95%) | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 133 | [ ] | Grand Theft Auto III - The Definitive Edition (STEAM) | 30 | 30 | 100% (90d) | Does not open (92%) | 14% | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 134 | [ ] | Dark Sector (STEAM) | 29 | 38 | 76% (90d) | Does not open (68%) | 39% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 135 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 29 | 31 | 94% (90d) | Does not open (74%) | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 136 | [ ] | Audiosurf (STEAM) | 28 | 39 | 72% (90d) | Does not open (46%) | 50% | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 137 | [ ] | Borderlands 2 RU (STEAM) | 28 | 30 | 93% (90d) | Does not open (58%) | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 138 | [ ] | Breath of Fire IV (STEAM) | 28 | 28 | 100% (90d) | Does not open (56%) | 18% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 139 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 28 | 28 | 100% (90d) | Does not open (68%) | 0% | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 140 | [ ] | Mirror's Edge™ (GOG) | 27 | 38 | 71% (90d) | No graphics (62%) | 47% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 141 | [ ] | The Planet Crafter (STEAM) | 27 | 32 | 84% (90d) | Does not open (55%) | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 142 | [ ] | Alpha Protocol (STEAM) | 27 | 31 | 87% (90d) | Does not open (58%) | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 143 | [ ] | PAYDAY 2 (STEAM) | 27 | 30 | 90% (90d) | Does not open (78%) | 31% | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 144 | [ ] | Hitman: Blood Money (STEAM) | 27 | 28 | 96% (90d) | Does not open (83%) | 12% | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 145 | [ ] | WRC 7 (STEAM) | 27 | 28 | 96% (90d) | Does not open (72%) | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 146 | [ ] | Zuma Deluxe (STEAM) | 27 | 28 | 96% (90d) | Does not open (95%) | 30% | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 147 | [ ] | Kenshi (STEAM) | 26 | 33 | 79% (90d) | Does not open (80%) | 11% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 148 | [ ] | Subnautica 2 (STEAM) | 26 | 32 | 81% (90d) | Does not open (65%) | 54% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 149 | [ ] | Singularity™ (GOG) | 26 | 31 | 84% (90d) | Does not open (100%) | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 150 | [ ] | Dragon Age™ Inquisition (STEAM) | 26 | 30 | 87% (90d) | Does not open (77%) | 33% | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 151 | [ ] | Northgard: Definitive Edition (STEAM) | 26 | 29 | 90% (90d) | Does not open (96%) | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 152 | [ ] | Persona 5 Strikers (STEAM) | 26 | 29 | 90% (90d) | Does not open (78%) | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 153 | [ ] | Turing Complete (STEAM) | 26 | 29 | 90% (90d) | Does not open (91%) | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 154 | [ ] | AION 2 (STEAM) | 26 | 28 | 93% (90d) | Does not open (65%) | 8% | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 155 | [ ] | Axiom Verge 2 (STEAM) | 26 | 27 | 96% (90d) | Does not open (77%) | 12% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 156 | [ ] | DiRT Showdown (STEAM) | 26 | 27 | 96% (90d) | Does not open (54%) | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 157 | [ ] | Isle of Reveries (STEAM) | 26 | 27 | 96% (90d) | Does not open (95%) | 31% | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 158 | [ ] | EA SPORTS FC™ 26 (STEAM) | 25 | 33 | 76% (90d) | Does not open (75%) | n/a | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 159 | [ ] | Knights of Pen and Paper 2 (STEAM) | 25 | 32 | 78% (90d) | Does not open (45%) | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 160 | [ ] | Bionic Commando Rearmed (STEAM) | 25 | 28 | 89% (90d) | Does not open (74%) | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 161 | [ ] | Bingle Bingle (STEAM) | 25 | 26 | 96% (90d) | Does not open (80%) | n/a | [#225](https://github.com/GameNative/gamenative-compat/issues/225) |
| 162 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 25 | 26 | 96% (90d) | Does not open (81%) | 40% | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 163 | [ ] | Resident Evil Requiem (STEAM) | 25 | 25 | 100% (90d) | Does not open (75%) | n/a | [#210](https://github.com/GameNative/gamenative-compat/issues/210) |
| 164 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 25 | 25 | 100% (90d) | Does not open (56%) | 9% | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 165 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 24 | 34 | 71% (90d) | Does not open (95%) | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 166 | [ ] | Call of Duty® (STEAM) | 24 | 33 | 73% (90d) | Does not open (67%) | 5% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 167 | [ ] | My Singing Monsters (STEAM) | 24 | 30 | 80% (90d) | Does not open (83%) | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 168 | [ ] | ENDLESS Space™ 2 (STEAM) | 24 | 29 | 83% (90d) | Does not open (93%) | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 169 | [ ] | The Swapper (STEAM) | 24 | 28 | 86% (90d) | Does not open (52%) | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 170 | [ ] | Alien Breed: Impact (STEAM) | 24 | 26 | 92% (90d) | Does not open (87%) | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 171 | [ ] | Peggle Nights (STEAM) | 24 | 26 | 92% (90d) | Does not open (94%) | 30% | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 172 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 24 | 25 | 96% (90d) | No graphics (53%) | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 173 | [ ] | The Lantern of the Laughless Saint (STEAM) | 24 | 25 | 96% (90d) | Does not open (81%) | 50% | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 174 | [ ] | theHunter Classic (STEAM) | 24 | 24 | 100% (1.3.0) | No graphics (86%) | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 175 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 23 | 32 | 72% (90d) | No graphics (57%) | 11% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 176 | [ ] | CarX Street (STEAM) | 23 | 30 | 77% (90d) | Does not open (77%) | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 177 | [ ] | Transformers: Fall of Cybertron (STEAM) | 23 | 30 | 77% (90d) | Does not open (63%) | 30% | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 178 | [ ] | SimCity 4 Deluxe (STEAM) | 23 | 27 | 85% (90d) | Does not open (82%) | 45% | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 179 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 23 | 26 | 88% (90d) | Does not open (95%) | 52% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 180 | [ ] | They Are Billions (STEAM) | 23 | 26 | 88% (90d) | Does not open (70%) | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 181 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 23 | 25 | 92% (90d) | Does not open (63%) | 50% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 182 | [ ] | PRAGMATA (STEAM) | 23 | 24 | 96% (90d) | Does not open (79%) | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 183 | [ ] | Euro Truck Simulator (STEAM) | 23 | 23 | 100% (90d) | Does not open (93%) | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 184 | [ ] | Gears 5 (STEAM) | 23 | 23 | 100% (90d) | Does not open (88%) | n/a | [#264](https://github.com/GameNative/gamenative-compat/issues/264) |
| 185 | [ ] | Marie's Adventure (STEAM) | 23 | 23 | 100% (90d) | Does not open (100%) | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 186 | [ ] | Spiral Knights (STEAM) | 23 | 23 | 100% (90d) | Does not open (72%) | n/a | [#263](https://github.com/GameNative/gamenative-compat/issues/263) |
| 187 | [ ] | SOMA (STEAM) | 22 | 30 | 73% (90d) | Does not open (79%) | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 188 | [ ] | Half-Life: Blue Shift (STEAM) | 22 | 26 | 85% (90d) | Does not open (85%) | 20% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 189 | [ ] | Tom Clancy's Ghost Recon® Wildlands (STEAM) | 22 | 26 | 85% (90d) | Does not open (94%) | n/a | [#280](https://github.com/GameNative/gamenative-compat/issues/280) |
| 190 | [ ] | skate.™ (EPIC) | 22 | 25 | 88% (90d) | Does not open (88%) | 8% | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 191 | [ ] | Wallachia: Reign of Dracula (STEAM) | 22 | 23 | 96% (90d) | No graphics (95%) | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 192 | [ ] | TEKKEN 8 (STEAM) | 21 | 28 | 75% (90d) | Does not open (76%) | 50% | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 193 | [ ] | Aggelos 2 (STEAM) | 21 | 27 | 78% (90d) | No graphics (90%) | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 194 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 21 | 27 | 78% (90d) | Does not open (62%) | n/a | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 195 | [ ] | Beyond Good & Evil™ (GOG) | 21 | 26 | 81% (90d) | Does not open (100%) | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 196 | [ ] | Sapphire Safari (GOG) | 21 | 26 | 81% (90d) | Does not open (89%) | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 197 | [ ] | Marvel's Midnight Suns (STEAM) | 21 | 24 | 88% (90d) | Does not open (84%) | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 198 | [ ] | Apex Legends (STEAM) | 21 | 23 | 91% (90d) | Does not open (74%) | n/a | [#261](https://github.com/GameNative/gamenative-compat/issues/261) |
| 199 | [ ] | Wuthering Waves (STEAM) | 21 | 23 | 91% (90d) | Does not open (85%) | n/a | [#216](https://github.com/GameNative/gamenative-compat/issues/216) |
| 200 | [ ] | Melatonin (STEAM) | 21 | 22 | 95% (90d) | Does not open (56%) | 46% | [#272](https://github.com/GameNative/gamenative-compat/issues/272) |
| 201 | [ ] | Resident Evil 3 Nemesis (1999) (STEAM) | 21 | 21 | 100% (90d) | Does not open (86%) | n/a | [#273](https://github.com/GameNative/gamenative-compat/issues/273) |
| 202 | [ ] | Return to Castle Wolfenstein (STEAM) | 21 | 21 | 100% (90d) | Does not open (95%) | 18% | [#321](https://github.com/GameNative/gamenative-compat/issues/321) |
| 203 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 21 | 21 | 100% (90d) | Does not open (71%) | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 204 | [ ] | Beat Cop (STEAM) | 20 | 28 | 71% (90d) | Does not open (74%) | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 205 | [ ] | Fishing Planet (STEAM) | 20 | 28 | 71% (90d) | Does not open (93%) | 33% | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 206 | [ ] | Surviving Mars (STEAM) | 20 | 26 | 77% (90d) | Does not open (92%) | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 207 | [ ] | PICO PARK:Classic Edition (STEAM) | 20 | 24 | 83% (90d) | Does not open (89%) | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 208 | [ ] | Halo: Spartan Assault (STEAM) | 20 | 23 | 87% (90d) | Does not open (82%) | 38% | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 209 | [ ] | Mirror's Edge™ Catalyst (STEAM) | 20 | 21 | 95% (90d) | Does not open (67%) | 56% | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 210 | [ ] | No More Room in Hell (STEAM) | 20 | 21 | 95% (90d) | Does not open (94%) | n/a | [#365](https://github.com/GameNative/gamenative-compat/issues/365) |
| 211 | [ ] | Pathway (EPIC) | 20 | 21 | 95% (90d) | Does not open (61%) | n/a | [#298](https://github.com/GameNative/gamenative-compat/issues/298) |
| 212 | [ ] | Rayman Legends (EPIC) | 20 | 21 | 95% (90d) | Does not open (92%) | n/a | [#286](https://github.com/GameNative/gamenative-compat/issues/286) |
| 213 | [ ] | The Last of Us™ Part I (STEAM) | 20 | 21 | 95% (90d) | Does not open (93%) | n/a | [#300](https://github.com/GameNative/gamenative-compat/issues/300) |
| 214 | [ ] | DiRT 2 (STEAM) | 20 | 20 | 100% (90d) | Does not open (85%) | n/a | [#471](https://github.com/GameNative/gamenative-compat/issues/471) |
| 215 | [ ] | Grounded 2 (STEAM) | 20 | 20 | 100% (90d) | Does not open (56%) | n/a | [#317](https://github.com/GameNative/gamenative-compat/issues/317) |
| 216 | [ ] | Dungeon Keeper™ 2 (GOG) | 19 | 26 | 73% (90d) | Does not open (100%) | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 217 | [ ] | Fogpiercer (STEAM) | 19 | 26 | 73% (90d) | Does not open (79%) | n/a | [#303](https://github.com/GameNative/gamenative-compat/issues/303) |
| 218 | [ ] | Yuppie Psycho (STEAM) | 19 | 26 | 73% (90d) | Does not open (75%) | 18% | [#325](https://github.com/GameNative/gamenative-compat/issues/325) |
| 219 | [ ] | Mafia III: Definitive Edition (STEAM) | 19 | 22 | 86% (90d) | Does not open (95%) | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 220 | [ ] | The Elder Scrolls IV: Oblivion Remastered (STEAM) | 19 | 22 | 86% (90d) | Does not open (59%) | n/a | [#312](https://github.com/GameNative/gamenative-compat/issues/312) |
| 221 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 19 | 22 | 86% (90d) | Does not open (79%) | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 222 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 21 | 90% (90d) | Does not open (82%) | 0% | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 223 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 21 | 90% (90d) | Does not open (89%) | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 224 | [ ] | GT Legends (STEAM) | 19 | 20 | 95% (90d) | Does not open (89%) | n/a | [#364](https://github.com/GameNative/gamenative-compat/issues/364) |
| 225 | [ ] | Jurassic World Evolution (EPIC) | 19 | 20 | 95% (90d) | Does not open (80%) | n/a | [#469](https://github.com/GameNative/gamenative-compat/issues/469) |
| 226 | [ ] | Zenless Zone Zero (STEAM) | 19 | 20 | 95% (90d) | Does not open (76%) | n/a | [#369](https://github.com/GameNative/gamenative-compat/issues/369) |
| 227 | [ ] | We Were Here Together (EPIC) | 18 | 24 | 75% (90d) | Does not open (82%) | n/a | [#374](https://github.com/GameNative/gamenative-compat/issues/374) |
| 228 | [ ] | Hitman 2: Silent Assassin (STEAM) | 18 | 23 | 78% (90d) | Does not open (83%) | 50% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 229 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 18 | 23 | 78% (90d) | Does not open (100%) | 35% | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 230 | [ ] | Yakuza 0 (GOG) | 18 | 23 | 78% (90d) | Does not open (67%) | 50% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 231 | [ ] | EVE Online (STEAM) | 18 | 22 | 82% (90d) | Does not open (50%) | 55% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 232 | [ ] | Sid Meier's Pirates! (STEAM) | 18 | 22 | 82% (90d) | Does not open (92%) | n/a | [#293](https://github.com/GameNative/gamenative-compat/issues/293) |
| 233 | [ ] | Bright Memory (STEAM) | 18 | 21 | 86% (90d) | No graphics (83%) | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 234 | [ ] | Lay of the Land (STEAM) | 18 | 20 | 90% (90d) | No graphics (61%) | n/a | [#477](https://github.com/GameNative/gamenative-compat/issues/477) |
| 235 | [ ] | Carnal Instinct (STEAM) | 17 | 24 | 71% (90d) | Does not open (57%) | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 236 | [ ] | SlashZero Demo (STEAM) | 17 | 23 | 74% (90d) | Does not open (75%) | 30% | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 237 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 17 | 22 | 77% (90d) | Does not open (87%) | 50% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 238 | [ ] | Dorfromantik (GOG) | 17 | 21 | 81% (90d) | Does not open (100%) | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 239 | [ ] | Clive Barker's Undying (GOG) | 17 | 20 | 85% (90d) | Does not open (75%) | n/a | [#388](https://github.com/GameNative/gamenative-compat/issues/388) |
| 240 | [ ] | GRADIUS origin collection (STEAM) | 17 | 20 | 85% (90d) | Controller issues (71%) | n/a | [#479](https://github.com/GameNative/gamenative-compat/issues/479) |
| 241 | [ ] | NBA 2K26 (STEAM) | 17 | 20 | 85% (90d) | Does not open (82%) | n/a | [#384](https://github.com/GameNative/gamenative-compat/issues/384) |
| 242 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (90d) | Does not open (82%) | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 243 | [ ] | Tyrian 2000 (GOG) | 17 | 20 | 85% (90d) | Does not open (86%) | n/a | [#360](https://github.com/GameNative/gamenative-compat/issues/360) |
| 244 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 16 | 23 | 70% (90d) | No graphics (56%) | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 245 | [ ] | Legend of Grimrock 2 (STEAM) | 16 | 23 | 70% (90d) | Does not open (92%) | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 246 | [ ] | Content Warning (STEAM) | 16 | 22 | 73% (90d) | Does not open (53%) | n/a | [#241](https://github.com/GameNative/gamenative-compat/issues/241) |
| 247 | [ ] | Re-Volt (STEAM) | 16 | 22 | 73% (90d) | Controller issues (71%) | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 248 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 21 | 76% (90d) | Does not open (82%) | 44% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 249 | [ ] | Bejeweled 2 Deluxe (STEAM) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#329](https://github.com/GameNative/gamenative-compat/issues/329) |
| 250 | [ ] | F.E.A.R. 2: Project Origin + Reborn (GOG) | 16 | 20 | 80% (90d) | Does not open (100%) | n/a | [#478](https://github.com/GameNative/gamenative-compat/issues/478) |
| 251 | [ ] | Genshin Impact (EPIC) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#326](https://github.com/GameNative/gamenative-compat/issues/326) |
| 252 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 16 | 20 | 80% (90d) | No graphics (67%) | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 253 | [ ] | Sacred Gold (STEAM) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 254 | [ ] | shapez (STEAM) | 16 | 20 | 80% (90d) | No graphics (67%) | n/a | [#332](https://github.com/GameNative/gamenative-compat/issues/332) |
| 255 | [ ] | DayZ (STEAM) | 15 | 21 | 71% (90d) | Does not open (56%) | 58% | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 256 | [ ] | Fallout Classic (GOG) | 15 | 21 | 71% (90d) | Does not open (71%) | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 257 | [ ] | Make Way (EPIC) | 15 | 21 | 71% (90d) | Does not open (79%) | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 258 | [ ] | Smushi Come Home (GOG) | 15 | 21 | 71% (90d) | Does not open (57%) | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 259 | [ ] | Spark the Electric Jester (STEAM) | 15 | 20 | 75% (90d) | Does not open (62%) | 52% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 260 | [ ] | Sword Art Online: Hollow Realization Deluxe Edition (STEAM) | 14 | 20 | 70% (90d) | Controller issues (92%) | n/a | [#470](https://github.com/GameNative/gamenative-compat/issues/470) |

## Probably does not work (70)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | Garry's Mod (STEAM) | 199 | 319 | 68% (1.3.0) | Does not open (79%) | 58% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 2 | [ ] | Prototype (STEAM) | 152 | 216 | 52% (1.3.0) | Does not open (75%) | 45% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 3 | [ ] | Metro 2033 Redux (STEAM) | 150 | 344 | 65% (1.3.0) | Does not open (69%) | 51% |  |
| 4 | [ ] | Geometry Dash (STEAM) | 142 | 418 | 67% (1.3.0) | Does not open (70%) | 40% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 5 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 140 | 207 | 68% (90d) | Does not open (80%) | n/a |  |
| 6 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 136 | 170 | 52% (1.3.0) | Does not open (93%) | 40% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 7 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 101 | 135 | 67% (1.3.0) | Does not open (75%) | 39% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 8 | [ ] | VRChat (STEAM) | 92 | 139 | 55% (1.3.0) | Does not open (65%) | 40% |  |
| 9 | [ ] | Hollow Knight: Silksong (GOG) | 69 | 108 | 64% (90d) | Does not open (67%) | 49% |  |
| 10 | [ ] | Firewatch (STEAM) | 66 | 114 | 58% (90d) | Does not open (89%) | 57% |  |
| 11 | [ ] | Mini Motorways (STEAM) | 58 | 102 | 57% (90d) | Does not open (76%) | 59% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 12 | [ ] | Oxygen Not Included (STEAM) | 54 | 87 | 62% (90d) | Does not open (76%) | 50% |  |
| 13 | [ ] | Breathedge (STEAM) | 51 | 75 | 68% (90d) | Does not open (61%) | 36% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 14 | [ ] | VALORANT (EPIC) | 45 | 70 | 64% (90d) | Does not open (87%) | 17% |  |
| 15 | [ ] | Plague Inc: Evolved (STEAM) | 44 | 66 | 67% (90d) | Does not open (67%) | 54% |  |
| 16 | [ ] | Age of Empires II (2013) (STEAM) | 40 | 69 | 58% (90d) | Does not open (48%) | 52% |  |
| 17 | [ ] | Frostpunk (STEAM) | 40 | 65 | 62% (90d) | No graphics (79%) | 47% |  |
| 18 | [ ] | Fallout (GOG) | 40 | 61 | 66% (90d) | Does not open (72%) | 52% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 19 | [ ] | Grim Dawn (GOG) | 38 | 62 | 61% (90d) | Does not open (65%) | 46% | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 20 | [ ] | XCOM 2 (STEAM) | 35 | 54 | 65% (90d) | Does not open (57%) | n/a |  |
| 21 | [ ] | Deponia (STEAM) | 34 | 62 | 55% (90d) | Does not open (50%) | 57% |  |
| 22 | [ ] | Sol Cesto (STEAM) | 33 | 51 | 65% (90d) | Does not open (70%) | 56% |  |
| 23 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 32 | 57 | 56% (90d) | Does not open (95%) | 45% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 24 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 31 | 58 | 53% (90d) | Does not open (66%) | 47% |  |
| 25 | [ ] | Soul's Remnant (STEAM) | 27 | 49 | 55% (90d) | Does not open (55%) | n/a |  |
| 26 | [ ] | Lucid Blocks (STEAM) | 27 | 46 | 59% (90d) | Does not open (83%) | 56% |  |
| 27 | [ ] | Crazy Taxi (STEAM) | 25 | 42 | 60% (90d) | Does not open (63%) | 57% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 28 | [ ] | Chained Echoes (GOG) | 24 | 47 | 51% (90d) | Does not open (62%) | 50% |  |
| 29 | [ ] | Strider (STEAM) | 24 | 37 | 65% (90d) | Does not open (100%) | 35% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 30 | [ ] | Invisible, Inc. (STEAM) | 23 | 39 | 59% (90d) | Does not open (67%) | 55% |  |
| 31 | [ ] | Cities: Skylines (STEAM) | 22 | 33 | 67% (90d) | Does not open (67%) | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 32 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 21 | 36 | 58% (90d) | Does not open (58%) | 47% |  |
| 33 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 21 | 33 | 64% (90d) | Does not open (81%) | n/a |  |
| 34 | [ ] | Another World: 20th Anniversary Edition (GOG) | 19 | 29 | 66% (90d) | Does not open (69%) | n/a |  |
| 35 | [ ] | Warhammer 40,000: Boltgun (GOG) | 19 | 29 | 66% (90d) | Does not open (92%) | 53% |  |
| 36 | [ ] | Turnip Boy Robs a Bank (EPIC) | 19 | 28 | 68% (90d) | Does not open (65%) | 41% | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 37 | [ ] | Need for Speed: Undercover (STEAM) | 18 | 29 | 62% (90d) | Does not open (93%) | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 38 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 17 | 30 | 57% (90d) | Does not open (88%) | 27% |  |
| 39 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 17 | 27 | 63% (90d) | Does not open (80%) | n/a |  |
| 40 | [ ] | Assassin's Creed Odyssey (STEAM) | 17 | 26 | 65% (90d) | Does not open (77%) | n/a | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 41 | [ ] | War of Dots (STEAM) | 17 | 26 | 65% (90d) | Does not open (75%) | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 42 | [ ] | Race The Sun (STEAM) | 16 | 31 | 52% (90d) | No graphics (92%) | 57% |  |
| 43 | [ ] | Alan Wake's American Nightmare (EPIC) | 16 | 27 | 59% (90d) | Does not open (87%) | 50% |  |
| 44 | [ ] | Guacamelee! Gold Edition (STEAM) | 16 | 27 | 59% (90d) | Does not open (93%) | n/a | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 45 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 25 | 64% (90d) | Directx error (57%) | n/a |  |
| 46 | [ ] | Odallus: The Dark Call (STEAM) | 15 | 27 | 56% (90d) | No graphics (57%) | n/a | [#337](https://github.com/GameNative/gamenative-compat/issues/337) |
| 47 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 15 | 26 | 58% (90d) | Does not open (85%) | 49% |  |
| 48 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 15 | 26 | 58% (90d) | Does not open (64%) | 0% |  |
| 49 | [ ] | Ys: Memories of Celceta (STEAM) | 15 | 24 | 63% (90d) | No graphics (45%) | 31% |  |
| 50 | [ ] | Blood Omen: Legacy of Kain (GOG) | 15 | 23 | 65% (90d) | Does not open (64%) | 45% |  |
| 51 | [ ] | Space Rangers HD: A War Apart (STEAM) | 15 | 22 | 68% (90d) | Does not open (64%) | 47% | [#472](https://github.com/GameNative/gamenative-compat/issues/472) |
| 52 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 15 | 22 | 68% (90d) | Does not open (70%) | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 53 | [ ] | Evoland (STEAM) | 14 | 28 | 50% (90d) | Controller issues (69%) | n/a |  |
| 54 | [ ] | Blaster Master Zero (STEAM) | 14 | 25 | 56% (90d) | Does not open (64%) | 42% |  |
| 55 | [ ] | Katana ZERO (GOG) | 14 | 25 | 56% (90d) | Does not open (85%) | 33% |  |
| 56 | [ ] | Asterigos: Curse of the Stars (STEAM) | 13 | 23 | 57% (90d) | Graphics glitches (50%) | n/a |  |
| 57 | [ ] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 13 | 23 | 57% (90d) | Does not open (100%) | 12% |  |
| 58 | [ ] | Trials Survivors (STEAM) | 13 | 23 | 57% (90d) | Does not open (67%) | n/a |  |
| 59 | [ ] | Evenicle (STEAM) | 13 | 22 | 59% (90d) | Graphics glitches (77%) | n/a |  |
| 60 | [ ] | Drop Duchy (EPIC) | 13 | 21 | 62% (90d) | Does not open (100%) | 18% |  |
| 61 | [ ] | The Stanley Parable (STEAM) | 13 | 21 | 62% (90d) | Does not open (89%) | 50% |  |
| 62 | [ ] | Buck Up And Drive! (STEAM) | 13 | 20 | 65% (90d) | Does not open (67%) | n/a |  |
| 63 | [ ] | Revolution Idle (STEAM) | 12 | 24 | 50% (90d) | No graphics (50%) | n/a |  |
| 64 | [ ] | A Plague Tale: Innocence (GOG) | 12 | 23 | 52% (90d) | Does not open (91%) | 50% |  |
| 65 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 12 | 22 | 55% (90d) | Does not open (73%) | n/a |  |
| 66 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (90d) | Does not open (82%) | n/a |  |
| 67 | [ ] | Crying Suns (EPIC) | 11 | 22 | 50% (90d) | No graphics (57%) | n/a |  |
| 68 | [ ] | The Excavation of Hob's Barrow (STEAM) | 11 | 21 | 52% (90d) | Controller issues (90%) | n/a |  |
| 69 | [ ] | DYNASTY WARRIORS: ORIGINS (STEAM) | 10 | 20 | 50% (90d) | Does not open (60%) | n/a |  |
| 70 | [ ] | F1 2015 (STEAM) | 10 | 20 | 50% (90d) | Does not open (50%) | n/a |  |

## Works, but the first launch usually fails (370)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 1320 | 1668 | 76% (1.3.0) | Does not open (83%) | 77% |  |
| 2 | [ ] | Grim Dawn (STEAM) | 570 | 622 | 67% (1.3.0) | Does not open (75%) | 64% |  |
| 3 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 565 | 716 | 76% (1.3.0) | Does not open (63%) | 91% |  |
| 4 | [ ] | Terraria (STEAM) | 484 | 757 | 60% (1.3.0) | No graphics (51%) | 75% |  |
| 5 | [ ] | KINGDOM HEARTS -HD 1.5+2.5 ReMIX- (STEAM) | 477 | 952 | 56% (1.3.0) | Does not open (79%) | 94% |  |
| 6 | [ ] | No Man's Sky (STEAM) | 366 | 644 | 53% (1.3.0) | Controller issues (61%) | 85% |  |
| 7 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 366 | 550 | 68% (1.3.0) | Does not open (55%) | 84% |  |
| 8 | [ ] | Half-Life (STEAM) | 353 | 618 | 51% (1.3.0) | Does not open (57%) | 76% |  |
| 9 | [ ] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 256 | 298 | 86% (90d) | Does not open (87%) | 65% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 10 | [ ] | Cyberpunk 2077 (STEAM) | 246 | 425 | 53% (1.3.0) | Does not open (68%) | 77% |  |
| 11 | [ ] | Welcome to Elderfield (STEAM) | 236 | 282 | 61% (1.3.0) | Does not open (72%) | 73% |  |
| 12 | [ ] | Grand Theft Auto V Legacy (STEAM) | 228 | 289 | 69% (1.3.0) | Does not open (89%) | 79% |  |
| 13 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 225 | 317 | 71% (90d) | Does not open (61%) | 88% |  |
| 14 | [ ] | BeamNG.drive (STEAM) | 219 | 267 | 88% (1.3.0) | Does not open (83%) | 92% |  |
| 15 | [ ] | Palworld (STEAM) | 205 | 405 | 52% (1.3.0) | Does not open (71%) | 87% |  |
| 16 | [ ] | OMORI (STEAM) | 204 | 247 | 83% (90d) | Does not open (64%) | 79% |  |
| 17 | [ ] | DRAGON BALL FighterZ (STEAM) | 203 | 233 | 72% (1.3.0) | Does not open (89%) | 62% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 18 | [ ] | MONSTER HUNTER RISE (STEAM) | 200 | 505 | 50% (1.3.0) | Does not open (81%) | 71% |  |
| 19 | [ ] | Devil May Cry HD Collection (STEAM) | 200 | 282 | 75% (1.3.0) | Does not open (86%) | 76% |  |
| 20 | [ ] | ELDEN RING (STEAM) | 198 | 295 | 68% (1.3.0) | Does not open (86%) | 72% |  |
| 21 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 192 | 361 | 60% (1.3.0) | Does not open (57%) | 81% |  |
| 22 | [ ] | DREDGE (EPIC) | 174 | 222 | 62% (1.3.0) | Does not open (67%) | 88% |  |
| 23 | [ ] | Rocket League® (EPIC) | 156 | 260 | 51% (1.3.0) | Does not open (73%) | 76% |  |
| 24 | [ ] | Noita (STEAM) | 145 | 221 | 53% (1.3.0) | Does not open (54%) | 78% |  |
| 25 | [ ] | Team Fortress 2 (STEAM) | 144 | 233 | 71% (1.3.0) | Does not open (69%) | 79% |  |
| 26 | [ ] | Borderlands 2 (EPIC) | 140 | 167 | 79% (1.3.0) | Does not open (83%) | 62% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 27 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 137 | 156 | 90% (1.3.0) | Does not open (86%) | 77% |  |
| 28 | [ ] | Castlevania Advance Collection (STEAM) | 132 | 203 | 70% (1.3.0) | Controller issues (95%) | 97% |  |
| 29 | [ ] | Far Cry® 3 (STEAM) | 131 | 147 | 89% (90d) | Does not open (83%) | 66% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 30 | [ ] | Castlevania Dominus Collection (STEAM) | 124 | 182 | 76% (1.3.0) | Controller issues (92%) | 98% |  |
| 31 | [ ] | Minecraft Dungeons II (STEAM) | 124 | 142 | 87% (90d) | Does not open (83%) | 65% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 32 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 120 | 150 | 68% (1.3.0) | Does not open (71%) | 63% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 33 | [ ] | Cave Story+ (STEAM) | 119 | 131 | 91% (90d) | Does not open (64%) | 94% |  |
| 34 | [ ] | Devil May Cry 5 (STEAM) | 118 | 186 | 69% (1.3.0) | Does not open (80%) | 67% |  |
| 35 | [ ] | Fallout: New Vegas (EPIC) | 118 | 144 | 76% (1.3.0) | Does not open (58%) | 91% |  |
| 36 | [ ] | Touhou Koumakyou: New Classic - the Embodiment of Scarlet Devil (STEAM) | 117 | 180 | 65% (90d) | Does not open (78%) | 81% |  |
| 37 | [ ] | Caravan SandWitch (EPIC) | 116 | 179 | 65% (90d) | Does not open (92%) | 82% |  |
| 38 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 114 | 161 | 78% (1.3.0) | Does not open (75%) | 63% |  |
| 39 | [ ] | The Witcher: Enhanced Edition (STEAM) | 113 | 130 | 87% (90d) | Does not open (59%) | 61% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 40 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 109 | 145 | 75% (90d) | Does not open (85%) | 85% |  |
| 41 | [ ] | Aniimo (STEAM) | 105 | 143 | 73% (90d) | Does not open (77%) | 92% |  |
| 42 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 103 | 151 | 64% (1.3.0) | Does not open (73%) | 76% |  |
| 43 | [ ] | Moonstone Island (STEAM) | 103 | 136 | 76% (90d) | Controller issues (57%) | 87% |  |
| 44 | [ ] | Happy Wheels (STEAM) | 95 | 115 | 83% (90d) | No graphics (53%) | 80% |  |
| 45 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 94 | 125 | 75% (90d) | Controller issues (86%) | 98% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 46 | [ ] | Sovereign Tower (STEAM) | 92 | 150 | 61% (90d) | Does not open (83%) | 85% |  |
| 47 | [ ] | Fallout: New Vegas PCR (STEAM) | 91 | 122 | 75% (90d) | Does not open (89%) | 69% |  |
| 48 | [ ] | Sol Cesto (EPIC) | 88 | 93 | 95% (90d) | Does not open (76%) | 62% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 49 | [ ] | STEINS;GATE (STEAM) | 86 | 120 | 72% (90d) | Does not open (90%) | 90% |  |
| 50 | [ ] | Vital Shell (STEAM) | 85 | 129 | 66% (90d) | Does not open (52%) | 85% |  |
| 51 | [ ] | Cry of Fear (STEAM) | 84 | 165 | 72% (1.3.0) | Does not open (50%) | 87% |  |
| 52 | [ ] | Hogwarts Legacy (STEAM) | 83 | 145 | 51% (1.3.0) | Does not open (59%) | 66% |  |
| 53 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 82 | 84 | 98% (90d) | Does not open (91%) | 61% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 54 | [ ] | Detroit: Become Human (STEAM) | 77 | 80 | 96% (90d) | Does not open (71%) | 63% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 55 | [ ] | Mega Man Zero/ZX Legacy Collection (STEAM) | 76 | 105 | 72% (90d) | Does not open (86%) | 86% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 56 | [ ] | The Sims™ 4 (STEAM) | 76 | 98 | 78% (90d) | Does not open (89%) | 69% |  |
| 57 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 74 | 124 | 60% (90d) | Controller issues (59%) | 94% |  |
| 58 | [ ] | Sid Meier's Civilization VI (STEAM) | 72 | 127 | 54% (1.3.0) | Does not open (70%) | 92% |  |
| 59 | [ ] | Ballionaire (STEAM) | 71 | 109 | 50% (1.3.0) | Does not open (77%) | 96% |  |
| 60 | [ ] | Darksiders (STEAM) | 71 | 86 | 83% (90d) | Does not open (68%) | 88% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 61 | [ ] | Alabaster Dawn (STEAM) | 70 | 124 | 56% (90d) | Controller issues (52%) | 91% |  |
| 62 | [ ] | Dota 2 (STEAM) | 70 | 107 | 59% (1.3.0) | Does not open (76%) | 70% |  |
| 63 | [ ] | Antivirus Survivors 2003 Professional (STEAM) | 70 | 103 | 68% (90d) | Does not open (61%) | 92% |  |
| 64 | [ ] | Disgaea 5 Complete (STEAM) | 70 | 84 | 83% (90d) | Does not open (75%) | 100% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 65 | [ ] | Fallout (STEAM) | 69 | 107 | 64% (90d) | Does not open (70%) | 71% |  |
| 66 | [ ] | American Truck Simulator (STEAM) | 68 | 108 | 79% (1.3.0) | Does not open (74%) | 77% |  |
| 67 | [ ] | Fable - The Lost Chapters (STEAM) | 68 | 107 | 52% (1.3.0) | Graphics glitches (51%) | 79% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 68 | [ ] | Dungeons & Degenerate Gamblers (STEAM) | 68 | 93 | 54% (1.3.0) | Does not open (90%) | 99% |  |
| 69 | [ ] | Gunfire Reborn (STEAM) | 68 | 74 | 92% (90d) | Does not open (81%) | 94% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 70 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 67 | 105 | 64% (90d) | Does not open (72%) | 71% |  |
| 71 | [ ] | Call of Juarez Gunslinger (STEAM) | 67 | 82 | 82% (90d) | Does not open (90%) | 75% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 72 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 67 | 79 | 95% (1.3.0) | Does not open (89%) | 97% |  |
| 73 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 66 | 122 | 52% (1.3.0) | Does not open (67%) | 61% |  |
| 74 | [ ] | Cyberpunk 2077 (GOG) | 65 | 80 | 81% (90d) | Does not open (76%) | 77% |  |
| 75 | [ ] | Sonic Lost World (STEAM) | 64 | 108 | 59% (90d) | No graphics (61%) | 90% |  |
| 76 | [ ] | Borderlands: The Pre-Sequel (STEAM) | 64 | 90 | 71% (90d) | Does not open (77%) | 65% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 77 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 64 | 87 | 59% (1.3.0) | Does not open (50%) | 92% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 78 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 64 | 86 | 74% (90d) | Does not open (47%) | 61% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 79 | [ ] | MIO: Memories in Orbit (STEAM) | 62 | 117 | 66% (1.3.0) | Graphics glitches (53%) | 96% |  |
| 80 | [ ] | Poppy Playtime (STEAM) | 62 | 109 | 57% (90d) | Does not open (70%) | 78% |  |
| 81 | [ ] | Big Walk (STEAM) | 61 | 95 | 64% (90d) | Does not open (69%) | 85% |  |
| 82 | [ ] | A Plague Tale: Innocence (STEAM) | 60 | 63 | 95% (90d) | Does not open (88%) | 73% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 83 | [ ] | The Binding of Isaac (STEAM) | 59 | 135 | 63% (1.3.0) | Controller issues (91%) | 93% |  |
| 84 | [ ] | eFootball™ (STEAM) | 59 | 87 | 68% (90d) | Does not open (55%) | 75% |  |
| 85 | [ ] | Red Dead Redemption 2 (STEAM) | 59 | 79 | 59% (1.3.0) | Does not open (98%) | 82% |  |
| 86 | [ ] | Call of Duty: World at War (STEAM) | 58 | 83 | 70% (90d) | Does not open (42%) | 72% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 87 | [ ] | Borderlands 3 (STEAM) | 58 | 78 | 74% (90d) | Does not open (91%) | 96% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 88 | [ ] | Starbound (STEAM) | 57 | 87 | 54% (1.3.0) | Does not open (68%) | 71% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 89 | [ ] | Deskrawl: Idle ARPG (STEAM) | 57 | 68 | 86% (1.3.0) | Does not open (60%) | 80% |  |
| 90 | [ ] | Sonic Generations (STEAM) | 57 | 67 | 85% (90d) | Does not open (72%) | 62% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 91 | [ ] | Dead by Daylight (STEAM) | 57 | 62 | 92% (90d) | Does not open (83%) | 84% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 92 | [ ] | Sonic Adventure DX (STEAM) | 56 | 91 | 62% (90d) | Does not open (86%) | 65% |  |
| 93 | [ ] | TBH: Task Bar Hero (STEAM) | 55 | 85 | 65% (90d) | Does not open (74%) | 95% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 94 | [ ] | The Secret of Monkey Island: Special Edition (STEAM) | 55 | 85 | 65% (90d) | Does not open (92%) | 71% |  |
| 95 | [ ] | Okami HD (STEAM) | 54 | 99 | 55% (90d) | Controller issues (60%) | 85% |  |
| 96 | [ ] | Prey (STEAM) | 54 | 92 | 59% (90d) | Does not open (64%) | 84% |  |
| 97 | [ ] | Until Then (STEAM) | 53 | 92 | 58% (90d) | Does not open (73%) | 96% |  |
| 98 | [ ] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 53 | 90 | 59% (90d) | Does not open (62%) | 62% |  |
| 99 | [ ] | Ace Attorney Investigations Collection (STEAM) | 53 | 83 | 64% (90d) | Does not open (96%) | 91% |  |
| 100 | [ ] | Path of Exile (STEAM) | 53 | 62 | 85% (90d) | Does not open (91%) | 86% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 101 | [ ] | MapleStory (STEAM) | 53 | 55 | 91% (1.3.0) | Does not open (77%) | 75% |  |
| 102 | [ ] | A Plague Tale: Innocence (EPIC) | 52 | 88 | 59% (90d) | Does not open (69%) | 89% |  |
| 103 | [ ] | The Bazaar (STEAM) | 52 | 83 | 63% (90d) | Does not open (72%) | 86% |  |
| 104 | [ ] | Vampire Survivors (EPIC) | 52 | 74 | 70% (90d) | Does not open (63%) | 60% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 105 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 52 | 60 | 87% (90d) | Does not open (80%) | 82% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 106 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 52 | 56 | 93% (90d) | Does not open (83%) | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 107 | [ ] | Resident Evil 6 (STEAM) | 51 | 124 | 74% (1.3.0) | Does not open (56%) | 89% |  |
| 108 | [ ] | 7 Days to Die (STEAM) | 51 | 107 | 58% (1.3.0) | Does not open (74%) | 72% |  |
| 109 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 50 | 74 | 77% (1.3.0) | Does not open (59%) | 65% |  |
| 110 | [ ] | DOOM 3 (STEAM) | 50 | 55 | 91% (90d) | Does not open (92%) | 60% | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 111 | [ ] | Guildrun Demo (STEAM) | 49 | 71 | 69% (90d) | No graphics (65%) | 71% |  |
| 112 | [ ] | Dead Space (STEAM) | 49 | 62 | 79% (90d) | Does not open (54%) | 76% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 113 | [ ] | Sheepy: A Short Adventure (STEAM) | 49 | 59 | 83% (90d) | Does not open (52%) | 80% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 114 | [ ] | Sleeping Dogs™ (STEAM) | 49 | 56 | 88% (90d) | Does not open (87%) | 77% | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 115 | [ ] | Last Epoch (STEAM) | 48 | 71 | 71% (1.3.0) | Does not open (79%) | 100% |  |
| 116 | [ ] | Rivals of Aether II (STEAM) | 48 | 70 | 69% (90d) | Does not open (55%) | 74% |  |
| 117 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 48 | 69 | 70% (90d) | Does not open (83%) | 62% |  |
| 118 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 76 | 62% (90d) | Controller issues (55%) | 95% |  |
| 119 | [ ] | Watch_Dogs 2 (STEAM) | 47 | 52 | 90% (90d) | Does not open (97%) | 60% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 120 | [ ] | Moonlighter (EPIC) | 47 | 51 | 92% (90d) | No graphics (79%) | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 121 | [ ] | Digimon World: Next Order (STEAM) | 46 | 86 | 53% (90d) | Controller issues (80%) | 95% |  |
| 122 | [ ] | Tomb Raider: Anniversary (STEAM) | 46 | 65 | 71% (90d) | Does not open (95%) | 61% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 123 | [ ] | Grand Theft Auto V (EPIC) | 46 | 51 | 90% (90d) | Does not open (89%) | 83% |  |
| 124 | [ ] | Darkest Dungeon® (EPIC) | 45 | 85 | 52% (1.3.0) | Does not open (62%) | 62% |  |
| 125 | [ ] | Life is Strange™ (STEAM) | 44 | 86 | 51% (90d) | Does not open (74%) | 81% |  |
| 126 | [ ] | Street Fighter™ 6 (STEAM) | 44 | 70 | 63% (90d) | Does not open (86%) | 79% |  |
| 127 | [ ] | Resident Evil 7 Biohazard (STEAM) | 43 | 69 | 70% (1.3.0) | Does not open (77%) | 82% |  |
| 128 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 42 | 77 | 71% (1.3.0) | Controller issues (47%) | 89% |  |
| 129 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 42 | 76 | 55% (90d) | Controller issues (53%) | 86% |  |
| 130 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 42 | 70 | 60% (90d) | Does not open (67%) | 79% |  |
| 131 | [ ] | Deadlock (STEAM) | 42 | 63 | 67% (90d) | Does not open (45%) | 93% |  |
| 132 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 42 | 63 | 67% (90d) | Does not open (73%) | 69% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 133 | [ ] | FINAL FANTASY VII (2013) (STEAM) | 42 | 61 | 69% (90d) | Does not open (83%) | 79% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 134 | [ ] | Forza Horizon 4 (STEAM) | 42 | 58 | 72% (90d) | Does not open (53%) | 86% |  |
| 135 | [ ] | Amnesia: The Dark Descent (STEAM) | 41 | 75 | 55% (90d) | Does not open (85%) | 75% |  |
| 136 | [ ] | Aggelos (STEAM) | 41 | 55 | 75% (90d) | No graphics (79%) | 95% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 137 | [ ] | Your Only Move Is HUSTLE (STEAM) | 40 | 80 | 50% (90d) | Does not open (64%) | 88% |  |
| 138 | [ ] | Salt and Sanctuary (STEAM) | 40 | 79 | 51% (90d) | Does not open (74%) | 82% |  |
| 139 | [ ] | Sonic Origins (STEAM) | 40 | 71 | 56% (90d) | Does not open (69%) | 83% |  |
| 140 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 40 | 41 | 98% (90d) | Does not open (62%) | 85% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 141 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 39 | 74 | 53% (90d) | No graphics (83%) | 98% |  |
| 142 | [ ] | Tales of ARISE (STEAM) | 39 | 67 | 58% (90d) | Controller issues (74%) | 94% |  |
| 143 | [ ] | Capcom Arcade Stadium (STEAM) | 39 | 48 | 81% (90d) | Does not open (84%) | 76% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 144 | [ ] | CrossCode (GOG) | 39 | 43 | 91% (90d) | Does not open (76%) | 70% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 145 | [ ] | Monster Hunter Wilds (STEAM) | 39 | 40 | 98% (90d) | Does not open (63%) | 76% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 146 | [ ] | Fallout 3 (STEAM) | 37 | 73 | 50% (1.3.0) | Does not open (48%) | 91% |  |
| 147 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 68 | 54% (90d) | Does not open (68%) | 87% |  |
| 148 | [ ] | Hearts of Iron IV (STEAM) | 36 | 63 | 57% (90d) | Does not open (74%) | 67% |  |
| 149 | [ ] | Street Fighter 30th Anniversary Collection (STEAM) | 35 | 67 | 52% (90d) | Does not open (100%) | 65% |  |
| 150 | [ ] | SurrounDead (STEAM) | 35 | 66 | 53% (90d) | Controller issues (61%) | 94% |  |
| 151 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 35 | 41 | 85% (90d) | No graphics (69%) | 82% | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 152 | [ ] | Rocket League (STEAM) | 34 | 55 | 62% (90d) | Does not open (69%) | 69% |  |
| 153 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 34 | 48 | 71% (90d) | Controller issues (88%) | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 154 | [ ] | SnowRunner (STEAM) | 34 | 47 | 72% (90d) | Does not open (96%) | 85% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 155 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 34 | 40 | 85% (90d) | Does not open (64%) | 72% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 156 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 34 | 39 | 87% (90d) | Does not open (68%) | 64% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 157 | [ ] | Hero Siege (STEAM) | 33 | 57 | 58% (90d) | Graphics glitches (52%) | 60% |  |
| 158 | [ ] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 54 | 61% (90d) | Controller issues (84%) | 82% |  |
| 159 | [ ] | Earthion (STEAM) | 33 | 53 | 62% (90d) | Controller issues (88%) | 100% |  |
| 160 | [ ] | Capcom Fighting Collection 2 (STEAM) | 33 | 48 | 69% (90d) | Does not open (78%) | 83% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 161 | [ ] | Supermarket Together (STEAM) | 33 | 47 | 70% (90d) | Does not open (72%) | 72% |  |
| 162 | [ ] | Russian Fishing 4 (STEAM) | 33 | 39 | 85% (90d) | Does not open (68%) | 74% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 163 | [ ] | Hotline Miami (GOG) | 33 | 38 | 87% (90d) | Does not open (94%) | 68% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 164 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 32 | 61 | 52% (90d) | Does not open (75%) | 88% |  |
| 165 | [ ] | Max Payne (STEAM) | 32 | 58 | 55% (90d) | No graphics (43%) | 96% |  |
| 166 | [ ] | Counter-Strike:Global Offensive (STEAM) | 32 | 51 | 63% (90d) | Does not open (78%) | 76% |  |
| 167 | [ ] | Secrets of Grindea (STEAM) | 32 | 50 | 64% (90d) | Does not open (52%) | 80% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 168 | [ ] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 32 | 47 | 68% (90d) | Does not open (85%) | 86% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 169 | [ ] | Palia (STEAM) | 32 | 44 | 73% (90d) | Does not open (69%) | 82% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 170 | [ ] | Romestead (STEAM) | 32 | 43 | 74% (90d) | Does not open (65%) | 75% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 171 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 42 | 76% (90d) | Controller issues (62%) | 89% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 172 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 32 | 37 | 86% (90d) | Does not open (73%) | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 173 | [ ] | Red Dead Redemption (STEAM) | 32 | 36 | 89% (90d) | Does not open (95%) | 89% |  |
| 174 | [ ] | COCOON (STEAM) | 31 | 60 | 52% (90d) | Directx error (54%) | 89% |  |
| 175 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 31 | 55 | 56% (90d) | Does not open (46%) | 67% |  |
| 176 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 31 | 51 | 61% (90d) | Controller issues (61%) | 70% |  |
| 177 | [ ] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 31 | 50 | 62% (90d) | Does not open (45%) | 77% |  |
| 178 | [ ] | Tower and Sword of Succubus (STEAM) | 31 | 46 | 67% (90d) | No graphics (81%) | 100% |  |
| 179 | [ ] | Ultimate Custom Night (STEAM) | 31 | 43 | 72% (90d) | No graphics (69%) | 78% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 180 | [ ] | Nioh: Complete Edition (STEAM) | 31 | 42 | 74% (90d) | Does not open (56%) | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 181 | [ ] | Super Animal Royale (STEAM) | 31 | 41 | 76% (90d) | Does not open (68%) | 72% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 182 | [ ] | Grand Theft Auto III (STEAM) | 31 | 39 | 79% (90d) | Does not open (52%) | 85% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 183 | [ ] | CRUEL (STEAM) | 31 | 37 | 84% (90d) | Does not open (90%) | 75% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 184 | [ ] | Path of Exile 2 (STEAM) | 31 | 37 | 84% (90d) | Does not open (96%) | 86% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 185 | [ ] | Need for Speed™ (STEAM) | 31 | 33 | 94% (90d) | Does not open (69%) | 63% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 186 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 30 | 70 | 50% (1.3.0) | Does not open (74%) | 78% |  |
| 187 | [ ] | Yakuza: Like a Dragon (STEAM) | 30 | 45 | 67% (90d) | Does not open (61%) | 70% |  |
| 188 | [ ] | Dead Island Riptide Definitive Edition (STEAM) | 29 | 56 | 52% (90d) | Does not open (50%) | 81% |  |
| 189 | [ ] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 55 | 53% (90d) | Does not open (92%) | 83% |  |
| 190 | [ ] | Aethermancer (STEAM) | 29 | 51 | 57% (90d) | Does not open (78%) | 82% |  |
| 191 | [ ] | Heavy Rain (STEAM) | 29 | 50 | 58% (90d) | Controller issues (61%) | 86% |  |
| 192 | [ ] | Binary Domain (STEAM) | 29 | 45 | 64% (90d) | Does not open (92%) | 79% |  |
| 193 | [ ] | Cave Story+ (EPIC) | 28 | 53 | 53% (90d) | Does not open (50%) | 87% |  |
| 194 | [ ] | Mortal Kombat X (STEAM) | 28 | 52 | 54% (90d) | Does not open (52%) | 85% |  |
| 195 | [ ] | Resident Evil Village (STEAM) | 28 | 51 | 55% (90d) | Does not open (67%) | 90% |  |
| 196 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 28 | 49 | 57% (90d) | Controller issues (46%) | 93% |  |
| 197 | [ ] | Akane (STEAM) | 28 | 47 | 60% (90d) | Controller issues (67%) | 100% |  |
| 198 | [ ] | Zero Escape: The Nonary Games (STEAM) | 28 | 46 | 61% (90d) | Does not open (88%) | 67% |  |
| 199 | [ ] | Ratatan (STEAM) | 28 | 41 | 68% (90d) | Does not open (52%) | 99% |  |
| 200 | [ ] | Moonlight Peaks (STEAM) | 28 | 40 | 70% (90d) | Does not open (64%) | 93% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 201 | [ ] | Stellar Blade™ (STEAM) | 28 | 36 | 78% (90d) | Does not open (48%) | 87% |  |
| 202 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 28 | 28 | 100% (90d) | Does not open (91%) | 64% | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 203 | [ ] | Dead Rising 2 (STEAM) | 27 | 42 | 67% (1.3.0) | Does not open (88%) | 70% |  |
| 204 | [ ] | Deus Ex™ GOTY Edition (GOG) | 27 | 41 | 66% (90d) | Does not open (35%) | 83% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 205 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 27 | 37 | 73% (90d) | Does not open (67%) | 92% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 206 | [ ] | Tales of Zestiria (STEAM) | 27 | 33 | 82% (90d) | Does not open (81%) | 67% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 207 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 26 | 49 | 53% (90d) | Does not open (55%) | 71% |  |
| 208 | [ ] | Prince of Persia (GOG) | 26 | 42 | 62% (90d) | Does not open (95%) | 86% |  |
| 209 | [ ] | Gothic II: Gold Classic (STEAM) | 26 | 37 | 70% (90d) | Does not open (59%) | 71% |  |
| 210 | [ ] | Crab Game (STEAM) | 26 | 34 | 76% (90d) | Does not open (53%) | 76% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 211 | [ ] | Unturned (STEAM) | 25 | 46 | 54% (90d) | Does not open (59%) | 79% |  |
| 212 | [ ] | Being a DIK (STEAM) | 25 | 43 | 58% (90d) | Does not open (78%) | 83% |  |
| 213 | [ ] | Counter-Strike: Condition Zero (STEAM) | 25 | 43 | 58% (90d) | Does not open (53%) | 62% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 214 | [ ] | Digimon Survive (STEAM) | 25 | 42 | 60% (90d) | Controller issues (71%) | 96% |  |
| 215 | [ ] | Wizard of Legend (EPIC) | 25 | 42 | 60% (90d) | Does not open (79%) | 80% |  |
| 216 | [ ] | Battle Brothers (STEAM) | 25 | 40 | 63% (90d) | Does not open (67%) | 67% |  |
| 217 | [ ] | Changed (STEAM) | 25 | 39 | 64% (90d) | Does not open (65%) | 88% |  |
| 218 | [ ] | Limbus Company (STEAM) | 25 | 39 | 64% (90d) | Does not open (85%) | 82% |  |
| 219 | [ ] | Return to Monkey Island (STEAM) | 25 | 38 | 66% (90d) | No graphics (58%) | 86% |  |
| 220 | [ ] | Bongo Cat (STEAM) | 25 | 35 | 71% (90d) | Does not open (65%) | 79% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 221 | [ ] | Beyond: Two Souls (STEAM) | 25 | 33 | 76% (90d) | Does not open (50%) | 70% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 222 | [ ] | Goose Goose Duck (STEAM) | 25 | 33 | 76% (90d) | Does not open (71%) | 71% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 223 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 32 | 78% (90d) | Does not open (87%) | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 224 | [ ] | Tearscape (STEAM) | 25 | 29 | 86% (90d) | Controller issues (53%) | 93% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 225 | [ ] | Resident Evil (GOG) | 25 | 27 | 93% (90d) | Does not open (95%) | 67% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 226 | [ ] | Resident Evil Revelations 2 (STEAM) | 24 | 48 | 50% (90d) | Does not open (40%) | 92% |  |
| 227 | [ ] | Goat Simulator (STEAM) | 24 | 45 | 53% (90d) | Does not open (58%) | 64% |  |
| 228 | [ ] | Cat Mail Co. (STEAM) | 24 | 40 | 60% (90d) | Does not open (89%) | 89% |  |
| 229 | [ ] | Opus Magnum (STEAM) | 24 | 38 | 63% (90d) | Does not open (76%) | 82% |  |
| 230 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 24 | 34 | 71% (90d) | Does not open (57%) | 65% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 231 | [ ] | PowerWash Simulator (STEAM) | 23 | 67 | 76% (1.3.0) | Does not open (84%) | 78% |  |
| 232 | [ ] | Lobotomy Corporation (STEAM) | 23 | 40 | 58% (90d) | No graphics (60%) | 94% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 233 | [ ] | SWORN (STEAM) | 23 | 38 | 61% (90d) | Does not open (44%) | 100% |  |
| 234 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 36 | 64% (90d) | Does not open (100%) | 82% |  |
| 235 | [ ] | Timberborn (STEAM) | 23 | 35 | 66% (90d) | No graphics (62%) | 81% |  |
| 236 | [ ] | Party Animals (STEAM) | 23 | 32 | 72% (90d) | Does not open (75%) | 71% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 237 | [ ] | Jade Empire: Special Edition (GOG) | 23 | 31 | 74% (90d) | Does not open (50%) | 73% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 238 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 23 | 31 | 74% (90d) | Does not open (40%) | 73% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 239 | [ ] | FINAL FANTASY XIV Online (STEAM) | 23 | 30 | 77% (90d) | Does not open (100%) | 96% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 240 | [ ] | Jade Empire: Special Edition (STEAM) | 23 | 26 | 88% (90d) | Does not open (95%) | 67% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 241 | [ ] | Football Manager 2024 (EPIC) | 22 | 40 | 55% (90d) | Does not open (86%) | 92% |  |
| 242 | [ ] | Pinball FX Classic (STEAM) | 22 | 40 | 55% (90d) | Does not open (76%) | 91% |  |
| 243 | [ ] | This War of Mine (STEAM) | 22 | 40 | 55% (90d) | No graphics (56%) | 75% |  |
| 244 | [ ] | Life is Strange Remastered (STEAM) | 22 | 34 | 65% (90d) | Does not open (73%) | 89% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 245 | [ ] | Worms W.M.D (STEAM) | 22 | 34 | 65% (90d) | Does not open (61%) | 89% |  |
| 246 | [ ] | Need for Speed™ Unbound (STEAM) | 22 | 30 | 73% (90d) | Does not open (83%) | 79% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 247 | [ ] | Capcom Fighting Collection (STEAM) | 22 | 27 | 81% (90d) | Does not open (80%) | 75% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 248 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 59 | 82% (1.3.0) | Does not open (79%) | 100% |  |
| 249 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 21 | 41 | 51% (90d) | Controller issues (65%) | 90% |  |
| 250 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 21 | 40 | 53% (90d) | Does not open (53%) | 71% |  |
| 251 | [ ] | Gambonanza (STEAM) | 21 | 40 | 53% (90d) | Does not open (60%) | 93% |  |
| 252 | [ ] | Overlord (STEAM) | 21 | 40 | 53% (90d) | Does not open (71%) | 61% |  |
| 253 | [ ] | One-armed robber (STEAM) | 21 | 38 | 55% (90d) | Controller issues (58%) | 79% |  |
| 254 | [ ] | Trailmakers (STEAM) | 21 | 38 | 55% (90d) | Does not open (44%) | 93% |  |
| 255 | [ ] | Tiny Glade (STEAM) | 21 | 37 | 57% (90d) | Does not open (42%) | 72% |  |
| 256 | [ ] | GOD EATER RESURRECTION (STEAM) | 21 | 32 | 66% (90d) | Does not open (53%) | 62% |  |
| 257 | [ ] | Nex Machina (STEAM) | 21 | 28 | 75% (90d) | Does not open (57%) | 85% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 258 | [ ] | Paper Lily - Chapter 1 (STEAM) | 20 | 40 | 50% (90d) | Does not open (72%) | 94% |  |
| 259 | [ ] | Crimzon Clover World EXplosion (STEAM) | 20 | 39 | 51% (90d) | Does not open (47%) | 100% |  |
| 260 | [ ] | Control Ultimate Edition (GOG) | 20 | 37 | 54% (90d) | Does not open (81%) | 94% |  |
| 261 | [ ] | Mafia: Definitive Edition (STEAM) | 20 | 37 | 54% (90d) | Does not open (84%) | 82% |  |
| 262 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 20 | 29 | 69% (90d) | Does not open (74%) | 73% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 263 | [ ] | BAJA: Edge of Control HD (STEAM) | 20 | 26 | 77% (90d) | Does not open (100%) | 90% | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 264 | [ ] | Dead Island (STEAM) | 20 | 26 | 77% (90d) | Does not open (69%) | 74% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 265 | [ ] | Tyr (STEAM) | 20 | 26 | 77% (90d) | Does not open (33%) | 82% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 266 | [ ] | TCG Card Shop Simulator (STEAM) | 19 | 38 | 50% (90d) | Does not open (63%) | 85% |  |
| 267 | [ ] | No More Heroes (STEAM) | 19 | 36 | 53% (90d) | No graphics (67%) | 70% |  |
| 268 | [ ] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 19 | 35 | 54% (90d) | Controller issues (47%) | 100% |  |
| 269 | [ ] | My Summer Car (STEAM) | 19 | 34 | 56% (90d) | Does not open (59%) | 84% |  |
| 270 | [ ] | Stick It to the Stickman (STEAM) | 19 | 34 | 56% (90d) | Does not open (88%) | 76% |  |
| 271 | [ ] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 19 | 33 | 58% (90d) | Does not open (88%) | 68% |  |
| 272 | [ ] | Metro Exodus (STEAM) | 19 | 31 | 61% (90d) | Does not open (82%) | 89% |  |
| 273 | [ ] | Torchlight II (EPIC) | 19 | 27 | 70% (90d) | Does not open (82%) | 100% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 274 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 19 | 24 | 79% (90d) | Does not open (82%) | 93% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 275 | [ ] | Faster Than Light (EPIC) | 18 | 36 | 50% (90d) | Does not open (41%) | 94% |  |
| 276 | [ ] | SKALD: Against the Black Priory (STEAM) | 18 | 36 | 50% (90d) | No graphics (63%) | 97% |  |
| 277 | [ ] | Killing Floor (STEAM) | 18 | 34 | 53% (90d) | Controller issues (100%) | 87% |  |
| 278 | [ ] | Far Far West (STEAM) | 18 | 32 | 56% (90d) | Does not open (59%) | 81% |  |
| 279 | [ ] | Hitman: Absolution (GOG) | 18 | 30 | 60% (90d) | Does not open (81%) | 84% |  |
| 280 | [ ] | Formula Legends (STEAM) | 18 | 29 | 62% (90d) | No graphics (60%) | 65% |  |
| 281 | [ ] | Arcade Paradise (EPIC) | 18 | 26 | 69% (90d) | Does not open (45%) | 82% |  |
| 282 | [ ] | Crusader Kings III (STEAM) | 18 | 23 | 78% (90d) | No graphics (64%) | 77% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 283 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 18 | 22 | 82% (90d) | Controller issues (100%) | 100% |  |
| 284 | [ ] | Deadly Premonition: The Director's Cut (STEAM) | 18 | 21 | 86% (90d) | Does not open (47%) | 77% |  |
| 285 | [ ] | CULTIC (STEAM) | 17 | 34 | 50% (90d) | Does not open (92%) | 65% |  |
| 286 | [ ] | SCP – Containment Breach (STEAM) | 17 | 33 | 52% (90d) | Does not open (82%) | 83% |  |
| 287 | [ ] | GRIP: Combat Racing (STEAM) | 17 | 32 | 53% (90d) | Does not open (100%) | 83% |  |
| 288 | [ ] | Lost Castle 2 (STEAM) | 17 | 32 | 53% (90d) | Does not open (62%) | 100% |  |
| 289 | [ ] | GRANDIA HD Remaster (STEAM) | 17 | 31 | 55% (90d) | Does not open (93%) | 71% |  |
| 290 | [ ] | Shank 2 (STEAM) | 17 | 30 | 57% (90d) | Does not open (82%) | 100% |  |
| 291 | [ ] | Tabletop Simulator (STEAM) | 17 | 29 | 59% (90d) | Does not open (54%) | 61% |  |
| 292 | [ ] | Maneater (STEAM) | 17 | 28 | 61% (90d) | Does not open (92%) | 77% |  |
| 293 | [ ] | Dishonored 2 (STEAM) | 17 | 27 | 63% (90d) | Does not open (86%) | 92% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 294 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 17 | 27 | 63% (90d) | No graphics (47%) | 78% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 295 | [ ] | Grim Fandango Remastered (GOG) | 17 | 25 | 68% (90d) | No graphics (78%) | 60% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 296 | [ ] | DOOM 3: BFG Edition (GOG) | 17 | 24 | 71% (90d) | No graphics (71%) | 79% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 297 | [ ] | Katanaut (STEAM) | 17 | 24 | 71% (90d) | Does not open (75%) | 69% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 298 | [ ] | Fall Guys (STEAM) | 17 | 23 | 74% (90d) | Does not open (92%) | 92% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 299 | [ ] | Warframe (STEAM) | 16 | 32 | 50% (90d) | Does not open (78%) | 95% |  |
| 300 | [ ] | Mark of the Ninja (STEAM) | 16 | 31 | 52% (90d) | Does not open (67%) | 64% |  |
| 301 | [ ] | DNF Duel (EPIC) | 16 | 29 | 55% (90d) | Does not open (54%) | 90% |  |
| 302 | [ ] | Titanfall® 2 (STEAM) | 16 | 28 | 57% (90d) | Does not open (83%) | 81% |  |
| 303 | [ ] | WORLD OF FINAL FANTASY (STEAM) | 16 | 27 | 59% (90d) | No graphics (62%) | 77% |  |
| 304 | [ ] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 16 | 25 | 64% (90d) | Does not open (100%) | 96% |  |
| 305 | [ ] | Chef Knight (STEAM) | 16 | 23 | 70% (90d) | Does not open (93%) | 69% |  |
| 306 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 22 | 73% (90d) | No graphics (60%) | 88% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 307 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 16 | 20 | 80% (90d) | Does not open (60%) | 91% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 308 | [ ] | Antichamber (STEAM) | 15 | 30 | 50% (90d) | Does not open (38%) | 88% |  |
| 309 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 15 | 30 | 50% (90d) | Does not open (100%) | 67% |  |
| 310 | [ ] | Sorry We're Closed (EPIC) | 15 | 27 | 50% (14d) | Does not open (100%) | 86% |  |
| 311 | [ ] | Wildermyth (STEAM) | 15 | 26 | 58% (90d) | Does not open (50%) | 94% |  |
| 312 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 15 | 25 | 60% (90d) | Does not open (92%) | 74% |  |
| 313 | [ ] | LET IT DIE (STEAM) | 15 | 25 | 60% (90d) | Does not open (91%) | 73% |  |
| 314 | [ ] | Mortal Shell (EPIC) | 15 | 25 | 60% (90d) | No graphics (89%) | 87% |  |
| 315 | [ ] | Batman™: Arkham Origins (GOG) | 15 | 24 | 63% (90d) | Does not open (67%) | 93% |  |
| 316 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 15 | 24 | 63% (90d) | Controller issues (57%) | 65% |  |
| 317 | [ ] | Sons Of The Forest (STEAM) | 15 | 23 | 65% (90d) | Does not open (56%) | 77% |  |
| 318 | [ ] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 15 | 23 | 65% (90d) | Does not open (64%) | 69% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 319 | [ ] | Allumeria (STEAM) | 15 | 22 | 68% (90d) | Does not open (69%) | 69% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 320 | [ ] | Treasure of Nadia (GOG) | 15 | 21 | 71% (90d) | Does not open (79%) | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 321 | [ ] | Maneater (EPIC) | 15 | 20 | 75% (90d) | Does not open (73%) | 77% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 322 | [ ] | Prey (GOG) | 15 | 20 | 75% (90d) | Does not open (43%) | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 323 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 28 | 50% (90d) | Controller issues (54%) | 85% |  |
| 324 | [ ] | sobosuba (STEAM) | 14 | 26 | 54% (90d) | Does not open (57%) | 90% |  |
| 325 | [ ] | Ultrapool (STEAM) | 14 | 25 | 56% (90d) | Does not open (54%) | 100% |  |
| 326 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 24 | 58% (90d) | Does not open (90%) | 73% |  |
| 327 | [ ] | Gloomwood (STEAM) | 14 | 24 | 58% (90d) | Does not open (62%) | 75% |  |
| 328 | [ ] | Alabaster Dawn Demo (STEAM) | 14 | 23 | 61% (90d) | Controller issues (71%) | 94% |  |
| 329 | [ ] | Disgaea 4 Complete+ (STEAM) | 14 | 22 | 64% (90d) | No graphics (43%) | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 330 | [ ] | Songs of Conquest (EPIC) | 14 | 22 | 64% (90d) | Does not open (75%) | 90% |  |
| 331 | [ ] | Horny Villa (STEAM) | 14 | 20 | 70% (90d) | Does not open (63%) | 95% |  |
| 332 | [ ] | Realm of the Mad God Exalt (STEAM) | 14 | 20 | 70% (90d) | Does not open (88%) | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 333 | [ ] | Human Fall Flat (STEAM) | 13 | 26 | 50% (90d) | No graphics (58%) | 65% |  |
| 334 | [ ] | Lust Goddess (STEAM) | 13 | 25 | 52% (90d) | Does not open (100%) | 67% |  |
| 335 | [ ] | Scrap Mechanic (STEAM) | 13 | 25 | 52% (90d) | Does not open (45%) | 80% |  |
| 336 | [ ] | Haydee (STEAM) | 13 | 24 | 54% (90d) | Does not open (100%) | 85% |  |
| 337 | [ ] | Look Outside (GOG) | 13 | 24 | 54% (90d) | Does not open (100%) | 100% |  |
| 338 | [ ] | Pillars of Eternity (STEAM) | 13 | 24 | 54% (90d) | Does not open (43%) | 65% |  |
| 339 | [ ] | Sid Meier's Civilization VI (EPIC) | 13 | 24 | 54% (90d) | Does not open (50%) | 86% |  |
| 340 | [ ] | DiRT 4 (STEAM) | 13 | 23 | 57% (90d) | Does not open (75%) | 96% |  |
| 341 | [ ] | Minit (EPIC) | 13 | 23 | 57% (90d) | Does not open (82%) | 82% |  |
| 342 | [ ] | 12 is Better Than 6 (STEAM) | 13 | 22 | 59% (90d) | Does not open (50%) | 85% |  |
| 343 | [ ] | Ready or Not (STEAM) | 13 | 22 | 59% (90d) | Does not open (55%) | 89% |  |
| 344 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 22 | 59% (90d) | Does not open (80%) | 91% |  |
| 345 | [ ] | FINAL FANTASY TYPE-0 HD (STEAM) | 13 | 21 | 62% (90d) | Does not open (62%) | 64% |  |
| 346 | [ ] | Secret of Mana (STEAM) | 13 | 21 | 62% (90d) | Graphics glitches (58%) | 64% |  |
| 347 | [ ] | Escape the Backrooms (STEAM) | 13 | 20 | 65% (90d) | Does not open (100%) | 92% |  |
| 348 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 13 | 20 | 65% (90d) | Does not open (71%) | 63% |  |
| 349 | [ ] | War Thunder (STEAM) | 13 | 20 | 65% (90d) | Does not open (80%) | 83% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 350 | [ ] | Sonic Superstars (STEAM) | 12 | 24 | 50% (90d) | Does not open (70%) | 65% |  |
| 351 | [ ] | AER Memories of Old (EPIC) | 12 | 23 | 52% (90d) | Does not open (91%) | 94% |  |
| 352 | [ ] | Cruelty Squad (STEAM) | 12 | 23 | 52% (90d) | Does not open (67%) | 86% |  |
| 353 | [ ] | NiGHTS into Dreams... (STEAM) | 12 | 23 | 52% (90d) | Does not open (44%) | 92% |  |
| 354 | [ ] | UNDEFEATED (STEAM) | 12 | 23 | 52% (90d) | Does not open (89%) | 82% |  |
| 355 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 12 | 22 | 55% (90d) | Does not open (60%) | 88% |  |
| 356 | [ ] | HITMAN World of Assassination (STEAM) | 12 | 22 | 55% (90d) | Does not open (73%) | 86% |  |
| 357 | [ ] | FATE (STEAM) | 12 | 21 | 57% (90d) | No graphics (44%) | 92% |  |
| 358 | [ ] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 21 | 57% (90d) | Controller issues (60%) | 94% |  |
| 359 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (90d) | No graphics (67%) | 60% |  |
| 360 | [ ] | PAYDAY: The Heist (STEAM) | 12 | 20 | 60% (90d) | Does not open (73%) | 73% |  |
| 361 | [ ] | Shift At Midnight (STEAM) | 12 | 20 | 60% (90d) | Does not open (80%) | 90% |  |
| 362 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (90d) | Does not open (89%) | 96% |  |
| 363 | [ ] | Castle in the Clouds (STEAM) | 11 | 22 | 50% (90d) | No graphics (63%) | 85% |  |
| 364 | [ ] | Ghostwire Tokyo (EPIC) | 11 | 22 | 50% (90d) | Does not open (86%) | 88% |  |
| 365 | [ ] | Injustice™ 2 (STEAM) | 11 | 22 | 50% (90d) | Does not open (88%) | 73% |  |
| 366 | [ ] | Tom Clancy's Rainbow Six: Vegas 2 (STEAM) | 11 | 22 | 50% (90d) | Does not open (55%) | 88% |  |
| 367 | [ ] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 21 | 52% (90d) | Graphics glitches (40%) | 95% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 368 | [ ] | Shadow Tactics: Blades of the Shogun (EPIC) | 11 | 20 | 55% (90d) | Does not open (67%) | 100% |  |
| 369 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 10 | 20 | 50% (90d) | Does not open (83%) | 74% |  |
| 370 | [ ] | Coromon (GOG) | 10 | 20 | 50% (90d) | Does not open (56%) | 65% |  |

## Recently recovered (397)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | FINAL FANTASY RESONANCE (STEAM) | 295 | 2026-10-24 | 678 | 74% |  |
| 2 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 256 | 2026-10-23 | 298 | 65% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 3 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 245 | 2026-10-19 | 298 | 66% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 229 | 2026-10-18 | 353 | 59% |  |
| 5 | [x] | OMORI (STEAM) | 204 | 2026-10-16 | 247 | 79% |  |
| 6 | [x] | DRAGON BALL FighterZ (STEAM) | 203 | 2026-11-01 | 233 | 62% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 7 | [x] | Devil May Cry HD Collection (STEAM) | 200 | 2026-10-19 | 282 | 76% |  |
| 8 | [x] | Spelunky 2 (STEAM) | 191 | 2026-11-01 | 211 | 48% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 9 | [x] | Burnout Paradise: The Ultimate Box (STEAM) | 157 | 2026-10-16 | 243 | 71% |  |
| 10 | [x] | Counter-Strike (STEAM) | 143 | 2026-10-22 | 227 | 50% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 11 | [x] | Sonic Adventure™ 2  (STEAM) | 143 | 2026-11-01 | 203 | 54% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 12 | [x] | Borderlands 2 (EPIC) | 140 | 2026-10-25 | 167 | 62% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 13 | [x] | Far Cry® 3 (STEAM) | 131 | 2026-10-21 | 147 | 66% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 14 | [x] | Minecraft Dungeons II (STEAM) | 124 | 2026-10-21 | 142 | 65% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 15 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 120 | 2026-10-28 | 150 | 63% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 16 | [x] | Call of Duty: Black Ops III (STEAM) | 118 | 2026-10-18 | 246 | 72% |  |
| 17 | [x] | Euro Truck Simulator 2 (STEAM) | 116 | 2026-11-01 | 215 | 57% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 18 | [x] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 114 | 2026-10-18 | 161 | 63% |  |
| 19 | [x] | The Witcher: Enhanced Edition (STEAM) | 113 | 2026-10-25 | 130 | 61% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 20 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 103 | 2026-10-18 | 151 | 76% |  |
| 21 | [x] | Moonstone Island (STEAM) | 103 | 2026-10-16 | 136 | 87% |  |
| 22 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 98 | 2026-10-25 | 154 | 66% |  |
| 23 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 94 | 2026-10-17 | 125 | 98% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 24 | [x] | Don't Starve Together (STEAM) | 90 | 2026-10-16 | 178 | 79% |  |
| 25 | [x] | Sol Cesto (EPIC) | 88 | 2026-11-03 | 93 | 62% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 26 | [x] | Catherine Classic (STEAM) | 86 | 2026-10-19 | 172 | 80% |  |
| 27 | [x] | Ultra Street Fighter IV (STEAM) | 84 | 2026-10-17 | 181 | 69% |  |
| 28 | [x] | Cry of Fear (STEAM) | 84 | 2026-10-18 | 165 | 87% |  |
| 29 | [x] | Hogwarts Legacy (STEAM) | 83 | 2026-10-17 | 145 | 66% |  |
| 30 | [x] | DOOM 3: BFG Edition (STEAM) | 82 | 2026-10-19 | 118 | 70% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 31 | [x] | FINAL FANTASY XIII-2 (STEAM) | 82 | 2026-10-30 | 84 | 61% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 32 | [x] | Need for Speed: Hot Pursuit (STEAM) | 78 | 2026-10-25 | 108 | 77% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 33 | [x] | Detroit: Become Human (STEAM) | 77 | 2026-10-17 | 80 | 63% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 34 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 76 | 2026-10-17 | 105 | 86% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 35 | [x] | Bayonetta (STEAM) | 74 | 2026-10-18 | 210 | 77% |  |
| 36 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 74 | 2026-10-18 | 124 | 94% |  |
| 37 | [x] | Don't Starve (STEAM) | 73 | 2026-10-16 | 160 | 82% |  |
| 38 | [x] | Darksiders (STEAM) | 71 | 2026-10-26 | 86 | 88% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 39 | [x] | Dota 2 (STEAM) | 70 | 2026-10-17 | 107 | 70% |  |
| 40 | [x] | Disgaea 5 Complete (STEAM) | 70 | 2026-10-18 | 84 | 100% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 41 | [x] | Fallout (STEAM) | 69 | 2026-10-18 | 107 | 71% |  |
| 42 | [x] | American Truck Simulator (STEAM) | 68 | 2026-10-18 | 108 | 77% |  |
| 43 | [x] | Fable - The Lost Chapters (STEAM) | 68 | 2026-10-17 | 107 | 79% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 44 | [x] | Gunfire Reborn (STEAM) | 68 | 2026-10-22 | 74 | 94% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 45 | [x] | Spyro™ Reignited Trilogy (STEAM) | 67 | 2026-10-18 | 105 | 71% |  |
| 46 | [x] | Call of Juarez Gunslinger (STEAM) | 67 | 2026-10-18 | 82 | 75% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 47 | [x] | Bloodstained: Ritual of the Night (EPIC) | 66 | 2026-10-19 | 122 | 61% |  |
| 48 | [x] | Stardew Valley (GOG) | 66 | 2026-11-01 | 119 | 51% |  |
| 49 | [x] | Sonic Lost World (STEAM) | 64 | 2026-10-18 | 108 | 90% |  |
| 50 | [x] | Borderlands: The Pre-Sequel (STEAM) | 64 | 2026-10-17 | 90 | 65% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 51 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 64 | 2026-10-17 | 87 | 92% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 52 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 64 | 2026-10-21 | 86 | 61% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 53 | [x] | Poppy Playtime (STEAM) | 62 | 2026-10-17 | 109 | 78% |  |
| 54 | [x] | Big Walk (STEAM) | 61 | 2026-10-17 | 95 | 85% |  |
| 55 | [x] | A Plague Tale: Innocence (STEAM) | 60 | 2026-10-20 | 63 | 73% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 56 | [x] | eFootball™ (STEAM) | 59 | 2026-10-18 | 87 | 75% |  |
| 57 | [x] | Call of Duty: World at War (STEAM) | 58 | 2026-10-28 | 83 | 72% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 58 | [x] | Borderlands 3 (STEAM) | 58 | 2026-10-19 | 78 | 96% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 59 | [x] | Starbound (STEAM) | 57 | 2026-10-18 | 87 | 71% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 60 | [x] | Sonic Generations (STEAM) | 57 | 2026-10-17 | 67 | 62% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 61 | [x] | Dead by Daylight (STEAM) | 57 | 2026-10-23 | 62 | 84% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 62 | [x] | Sonic Adventure DX (STEAM) | 56 | 2026-10-17 | 91 | 65% |  |
| 63 | [x] | TBH: Task Bar Hero (STEAM) | 55 | 2026-10-19 | 85 | 95% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 64 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 55 | 2026-10-18 | 85 | 71% |  |
| 65 | [x] | Okami HD (STEAM) | 54 | 2026-10-17 | 99 | 85% |  |
| 66 | [x] | Until Then (STEAM) | 53 | 2026-10-17 | 92 | 96% |  |
| 67 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 53 | 2026-11-02 | 90 | 62% |  |
| 68 | [x] | Path of Exile (STEAM) | 53 | 2026-10-26 | 62 | 86% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 69 | [x] | A Plague Tale: Innocence (EPIC) | 52 | 2026-10-25 | 88 | 89% |  |
| 70 | [x] | Vampire Survivors (EPIC) | 52 | 2026-11-03 | 74 | 60% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 71 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 52 | 2026-10-21 | 60 | 82% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 72 | [x] | Alex Kidd in Miracle World DX (EPIC) | 52 | 2026-10-22 | 56 | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 73 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 50 | 2026-10-19 | 97 | 77% |  |
| 74 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 50 | 2026-10-25 | 97 | 57% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 75 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 50 | 2026-10-18 | 74 | 65% |  |
| 76 | [x] | DOOM 3 (STEAM) | 50 | 2026-11-01 | 55 | 60% | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 77 | [x] | Guildrun Demo (STEAM) | 49 | 2026-10-22 | 71 | 71% |  |
| 78 | [x] | Dead Space (STEAM) | 49 | 2026-10-18 | 62 | 76% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 79 | [x] | Sheepy: A Short Adventure (STEAM) | 49 | 2026-10-24 | 59 | 80% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 80 | [x] | Sleeping Dogs™ (STEAM) | 49 | 2026-10-27 | 56 | 77% | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 81 | [x] | Rivals of Aether II (STEAM) | 48 | 2026-10-20 | 70 | 74% |  |
| 82 | [x] | STEINS;GATE RE:BOOT (STEAM) | 48 | 2026-10-21 | 69 | 62% |  |
| 83 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 2026-10-17 | 76 | 95% |  |
| 84 | [x] | Watch_Dogs 2 (STEAM) | 47 | 2026-11-03 | 52 | 60% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 85 | [x] | Moonlighter (EPIC) | 47 | 2026-10-23 | 51 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 86 | [x] | MudRunner (STEAM) | 46 | 2026-10-24 | 98 | 67% |  |
| 87 | [x] | Digimon World: Next Order (STEAM) | 46 | 2026-10-18 | 86 | 95% |  |
| 88 | [x] | Tomb Raider: Anniversary (STEAM) | 46 | 2026-10-25 | 65 | 61% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 89 | [x] | Darkest Dungeon® (EPIC) | 45 | 2026-10-22 | 85 | 62% |  |
| 90 | [x] | Abiotic Factor (STEAM) | 45 | 2026-10-18 | 79 | 70% |  |
| 91 | [x] | PROTOTYPE 2 (STEAM) | 44 | 2026-10-18 | 91 | 77% |  |
| 92 | [x] | Life is Strange™ (STEAM) | 44 | 2026-10-17 | 86 | 81% |  |
| 93 | [x] | Street Fighter™ 6 (STEAM) | 44 | 2026-10-16 | 70 | 79% |  |
| 94 | [x] | Skullgirls 2nd Encore (STEAM) | 43 | 2026-11-01 | 78 | 59% |  |
| 95 | [x] | Death Road to Canada (STEAM) | 42 | 2026-10-17 | 99 | 69% |  |
| 96 | [x] | Tomb Raider GOTY (GOG) | 42 | 2026-10-17 | 88 | 96% |  |
| 97 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 42 | 2026-10-17 | 76 | 86% |  |
| 98 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 42 | 2026-10-18 | 63 | 69% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 99 | [x] | Deadlock (STEAM) | 42 | 2026-10-16 | 63 | 93% |  |
| 100 | [x] | FINAL FANTASY VII (2013) (STEAM) | 42 | 2026-10-18 | 61 | 79% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 101 | [x] | Rogue Legacy (STEAM) | 41 | 2026-10-17 | 91 | 55% |  |
| 102 | [x] | Amnesia: The Dark Descent (STEAM) | 41 | 2026-10-17 | 75 | 75% |  |
| 103 | [x] | Aggelos (STEAM) | 41 | 2026-10-21 | 55 | 95% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 104 | [x] | Cobalt Core (STEAM) | 40 | 2026-10-18 | 93 | 89% |  |
| 105 | [x] | Salt and Sanctuary (STEAM) | 40 | 2026-10-18 | 79 | 82% |  |
| 106 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 40 | 2026-10-27 | 41 | 85% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 107 | [x] | Rayman Origins (STEAM) | 39 | 2026-10-17 | 87 | 81% |  |
| 108 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 39 | 2026-10-17 | 74 | 98% |  |
| 109 | [x] | Tales of ARISE (STEAM) | 39 | 2026-10-16 | 67 | 94% |  |
| 110 | [x] | Capcom Arcade Stadium (STEAM) | 39 | 2026-10-17 | 48 | 76% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 111 | [x] | CrossCode (GOG) | 39 | 2026-10-23 | 43 | 70% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 112 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-10-23 | 40 | 76% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 113 | [x] | Dishonored - Definitive Edition (EPIC) | 38 | 2026-10-17 | 89 | 83% |  |
| 114 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 2026-10-17 | 68 | 87% |  |
| 115 | [x] | Hearts of Iron IV (STEAM) | 36 | 2026-10-19 | 63 | 67% |  |
| 116 | [x] | Sable (EPIC) | 35 | 2026-10-18 | 76 | 86% |  |
| 117 | [x] | Teardown (STEAM) | 35 | 2026-10-17 | 75 | 76% |  |
| 118 | [x] | POSTAL 2 (GOG) | 35 | 2026-10-22 | 71 | 92% |  |
| 119 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 35 | 2026-10-16 | 67 | 65% |  |
| 120 | [x] | STAR WARS™ Episode I: Racer (GOG) | 35 | 2026-11-02 | 41 | 82% | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 121 | [x] | Rocket League (STEAM) | 34 | 2026-10-17 | 55 | 69% |  |
| 122 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 34 | 2026-10-21 | 48 | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 123 | [x] | SnowRunner (STEAM) | 34 | 2026-10-19 | 47 | 85% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 124 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 34 | 2026-10-18 | 40 | 72% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 125 | [x] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 34 | 2026-11-01 | 39 | 64% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 126 | [x] | Journey (STEAM) | 33 | 2026-10-27 | 70 | 53% |  |
| 127 | [x] | Ultimate Chicken Horse (STEAM) | 33 | 2026-10-23 | 69 | 62% |  |
| 128 | [x] | Hero Siege (STEAM) | 33 | 2026-11-02 | 57 | 60% |  |
| 129 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 2026-10-19 | 54 | 82% |  |
| 130 | [x] | Earthion (STEAM) | 33 | 2026-10-22 | 53 | 100% |  |
| 131 | [x] | Capcom Fighting Collection 2 (STEAM) | 33 | 2026-10-18 | 48 | 83% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 132 | [x] | Supermarket Together (STEAM) | 33 | 2026-10-19 | 47 | 72% |  |
| 133 | [x] | Russian Fishing 4 (STEAM) | 33 | 2026-10-23 | 39 | 74% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 134 | [x] | Hotline Miami (GOG) | 33 | 2026-10-20 | 38 | 68% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 135 | [x] | Bloodstained: Curse of the Moon (STEAM) | 32 | 2026-10-16 | 73 | 67% |  |
| 136 | [x] | Little Nightmares (STEAM) | 32 | 2026-10-16 | 70 | 62% |  |
| 137 | [x] | Max Payne (STEAM) | 32 | 2026-10-17 | 58 | 96% |  |
| 138 | [x] | Counter-Strike:Global Offensive (STEAM) | 32 | 2026-10-19 | 51 | 76% |  |
| 139 | [x] | Secrets of Grindea (STEAM) | 32 | 2026-10-20 | 50 | 80% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 140 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 32 | 2026-10-18 | 47 | 86% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 141 | [x] | Palia (STEAM) | 32 | 2026-10-22 | 44 | 82% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 142 | [x] | Romestead (STEAM) | 32 | 2026-10-18 | 43 | 75% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 143 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-10-20 | 42 | 89% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 144 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 32 | 2026-10-22 | 37 | 95% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 145 | [x] | Torchlight II (STEAM) | 31 | 2026-10-20 | 64 | 91% |  |
| 146 | [x] | COCOON (STEAM) | 31 | 2026-10-17 | 60 | 89% |  |
| 147 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 31 | 2026-10-26 | 55 | 67% |  |
| 148 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 31 | 2026-10-19 | 51 | 70% |  |
| 149 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 31 | 2026-10-22 | 50 | 77% |  |
| 150 | [x] | Tower and Sword of Succubus (STEAM) | 31 | 2026-10-22 | 46 | 100% |  |
| 151 | [x] | Ultimate Custom Night (STEAM) | 31 | 2026-10-19 | 43 | 78% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 152 | [x] | Nioh: Complete Edition (STEAM) | 31 | 2026-10-20 | 42 | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 153 | [x] | Super Animal Royale (STEAM) | 31 | 2026-10-19 | 41 | 72% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 154 | [x] | Grand Theft Auto III (STEAM) | 31 | 2026-10-17 | 39 | 85% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 155 | [x] | CRUEL (STEAM) | 31 | 2026-10-28 | 37 | 75% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 156 | [x] | Path of Exile 2 (STEAM) | 31 | 2026-10-18 | 37 | 86% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 157 | [x] | Need for Speed™ (STEAM) | 31 | 2026-10-18 | 33 | 63% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 158 | [x] | Stumble Guys (STEAM) | 29 | 2026-10-18 | 61 | 82% |  |
| 159 | [x] | Library Of Ruina (STEAM) | 29 | 2026-10-16 | 59 | 87% |  |
| 160 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 29 | 2026-10-18 | 56 | 81% |  |
| 161 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 2026-10-17 | 55 | 83% |  |
| 162 | [x] | Aethermancer (STEAM) | 29 | 2026-10-18 | 51 | 82% |  |
| 163 | [x] | Heavy Rain (STEAM) | 29 | 2026-10-18 | 50 | 86% |  |
| 164 | [x] | Binary Domain (STEAM) | 29 | 2026-10-18 | 45 | 79% |  |
| 165 | [x] | Dying Light (EPIC) | 28 | 2026-10-17 | 65 | 91% |  |
| 166 | [x] | Monster Hunter Stories (STEAM) | 28 | 2026-10-17 | 61 | 85% |  |
| 167 | [x] | State of Decay: Year-One (STEAM) | 28 | 2026-10-18 | 60 | 81% |  |
| 168 | [x] | Cave Story+ (EPIC) | 28 | 2026-10-18 | 53 | 87% |  |
| 169 | [x] | Mortal Kombat X (STEAM) | 28 | 2026-10-17 | 52 | 85% |  |
| 170 | [x] | Resident Evil Village (STEAM) | 28 | 2026-10-17 | 51 | 90% |  |
| 171 | [x] | Prince of Persia: The Sands of Time (STEAM) | 28 | 2026-10-20 | 49 | 93% |  |
| 172 | [x] | Akane (STEAM) | 28 | 2026-10-20 | 47 | 100% |  |
| 173 | [x] | Zero Escape: The Nonary Games (STEAM) | 28 | 2026-10-17 | 46 | 67% |  |
| 174 | [x] | Moonlight Peaks (STEAM) | 28 | 2026-10-20 | 40 | 93% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 175 | [x] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 28 | 2026-10-28 | 28 | 64% | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 176 | [x] | BioShock™ (GOG) | 27 | 2026-10-18 | 63 | 71% |  |
| 177 | [x] | Deus Ex™ GOTY Edition (GOG) | 27 | 2026-10-19 | 41 | 83% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 178 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 27 | 2026-11-03 | 37 | 92% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 179 | [x] | Tales of Zestiria (STEAM) | 27 | 2026-10-27 | 33 | 67% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 180 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 26 | 2026-10-19 | 88 | 94% |  |
| 181 | [x] | PlateUp! (STEAM) | 26 | 2026-10-16 | 55 | 84% |  |
| 182 | [x] | G.I. Joe Wrath of Cobra (EPIC) | 26 | 2026-10-19 | 49 | 71% |  |
| 183 | [x] | Prince of Persia (GOG) | 26 | 2026-10-24 | 42 | 86% |  |
| 184 | [x] | Gothic II: Gold Classic (STEAM) | 26 | 2026-10-20 | 37 | 71% |  |
| 185 | [x] | Crab Game (STEAM) | 26 | 2026-10-22 | 34 | 76% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 186 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 25 | 2026-10-19 | 61 | 85% |  |
| 187 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 25 | 2026-10-20 | 53 | 83% |  |
| 188 | [x] | Unturned (STEAM) | 25 | 2026-10-17 | 46 | 79% |  |
| 189 | [x] | Being a DIK (STEAM) | 25 | 2026-10-19 | 43 | 83% |  |
| 190 | [x] | Counter-Strike: Condition Zero (STEAM) | 25 | 2026-10-17 | 43 | 62% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 191 | [x] | Wizard of Legend (EPIC) | 25 | 2026-10-18 | 42 | 80% |  |
| 192 | [x] | Digimon Survive (STEAM) | 25 | 2026-10-23 | 42 | 96% |  |
| 193 | [x] | Battle Brothers (STEAM) | 25 | 2026-10-27 | 40 | 67% |  |
| 194 | [x] | Changed (STEAM) | 25 | 2026-10-24 | 39 | 88% |  |
| 195 | [x] | Limbus Company (STEAM) | 25 | 2026-10-18 | 39 | 82% |  |
| 196 | [x] | Return to Monkey Island (STEAM) | 25 | 2026-10-23 | 38 | 86% |  |
| 197 | [x] | Bongo Cat (STEAM) | 25 | 2026-10-20 | 35 | 79% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 198 | [x] | Beyond: Two Souls (STEAM) | 25 | 2026-10-22 | 33 | 70% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 199 | [x] | Goose Goose Duck (STEAM) | 25 | 2026-10-25 | 33 | 71% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 200 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-10-21 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 201 | [x] | Tearscape (STEAM) | 25 | 2026-10-30 | 29 | 93% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 202 | [x] | Resident Evil (GOG) | 25 | 2026-10-20 | 27 | 67% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 203 | [x] | CarX Drift Racing Online (STEAM) | 24 | 2026-10-16 | 58 | 74% |  |
| 204 | [x] | Titan Quest Anniversary Edition (STEAM) | 24 | 2026-10-16 | 55 | 85% |  |
| 205 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 54 | 86% |  |
| 206 | [x] | WEBFISHING (STEAM) | 24 | 2026-10-17 | 51 | 90% |  |
| 207 | [x] | Goat Simulator (STEAM) | 24 | 2026-11-01 | 45 | 64% |  |
| 208 | [x] | Cat Mail Co. (STEAM) | 24 | 2026-10-24 | 40 | 89% |  |
| 209 | [x] | Opus Magnum (STEAM) | 24 | 2026-11-01 | 38 | 82% |  |
| 210 | [x] | Borderlands: The Pre-Sequel (EPIC) | 24 | 2026-10-30 | 34 | 65% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 211 | [x] | ABZÛ (STEAM) | 23 | 2026-10-21 | 53 | 89% |  |
| 212 | [x] | Owlboy (STEAM) | 23 | 2026-11-02 | 49 | 48% |  |
| 213 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 23 | 2026-10-27 | 47 | 25% |  |
| 214 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-10-19 | 40 | 94% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 215 | [x] | SWORN (STEAM) | 23 | 2026-10-23 | 38 | 100% |  |
| 216 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 2026-10-17 | 36 | 82% |  |
| 217 | [x] | Timberborn (STEAM) | 23 | 2026-10-25 | 35 | 81% |  |
| 218 | [x] | Party Animals (STEAM) | 23 | 2026-10-17 | 32 | 71% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 219 | [x] | Jade Empire: Special Edition (GOG) | 23 | 2026-10-23 | 31 | 73% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 220 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 23 | 2026-10-25 | 31 | 73% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 221 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 96% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 222 | [x] | Jade Empire: Special Edition (STEAM) | 23 | 2026-11-01 | 26 | 67% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 223 | [x] | Saints Row IV (STEAM) | 22 | 2026-10-19 | 51 | 71% |  |
| 224 | [x] | Football Manager 2024 (EPIC) | 22 | 2026-10-20 | 40 | 92% |  |
| 225 | [x] | Pinball FX Classic (STEAM) | 22 | 2026-10-23 | 40 | 91% |  |
| 226 | [x] | This War of Mine (STEAM) | 22 | 2026-10-21 | 40 | 75% |  |
| 227 | [x] | Life is Strange Remastered (STEAM) | 22 | 2026-10-20 | 34 | 89% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 228 | [x] | Need for Speed™ Unbound (STEAM) | 22 | 2026-10-26 | 30 | 79% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 229 | [x] | Capcom Fighting Collection (STEAM) | 22 | 2026-10-23 | 27 | 75% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 230 | [x] | BlazBlue Centralfiction (STEAM) | 21 | 2026-10-17 | 61 | 81% |  |
| 231 | [x] | Slow Roads (STEAM) | 21 | 2026-10-22 | 46 | 97% |  |
| 232 | [x] | Hatred (STEAM) | 21 | 2026-10-22 | 45 | 86% |  |
| 233 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 21 | 2026-10-24 | 41 | 90% |  |
| 234 | [x] | Brothers - A Tale of Two Sons (EPIC) | 21 | 2026-10-23 | 40 | 71% |  |
| 235 | [x] | Overlord (STEAM) | 21 | 2026-11-03 | 40 | 61% |  |
| 236 | [x] | One-armed robber (STEAM) | 21 | 2026-10-23 | 38 | 79% |  |
| 237 | [x] | Trailmakers (STEAM) | 21 | 2026-10-21 | 38 | 93% |  |
| 238 | [x] | Tiny Glade (STEAM) | 21 | 2026-10-24 | 37 | 72% |  |
| 239 | [x] | GOD EATER RESURRECTION (STEAM) | 21 | 2026-11-01 | 32 | 62% |  |
| 240 | [x] | Nex Machina (STEAM) | 21 | 2026-10-18 | 28 | 85% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 241 | [x] | No Rest for the Wicked (STEAM) | 20 | 2026-10-19 | 43 | 76% |  |
| 242 | [x] | Paper Lily - Chapter 1 (STEAM) | 20 | 2026-10-27 | 40 | 94% |  |
| 243 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-10-20 | 39 | 100% |  |
| 244 | [x] | Mafia: Definitive Edition (STEAM) | 20 | 2026-10-28 | 37 | 82% |  |
| 245 | [x] | Sonic and SEGA All Stars Racing (STEAM) | 20 | 2026-10-19 | 29 | 73% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 246 | [x] | BAJA: Edge of Control HD (STEAM) | 20 | 2026-10-28 | 26 | 90% | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 247 | [x] | Dead Island (STEAM) | 20 | 2026-10-20 | 26 | 74% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 248 | [x] | Tyr (STEAM) | 20 | 2026-11-02 | 26 | 82% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 249 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 19 | 2026-10-25 | 42 | 71% |  |
| 250 | [x] | MudRunner (EPIC) | 19 | 2026-10-18 | 40 | 91% |  |
| 251 | [x] | No More Heroes (STEAM) | 19 | 2026-11-03 | 36 | 70% |  |
| 252 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 19 | 2026-10-21 | 35 | 100% |  |
| 253 | [x] | My Summer Car (STEAM) | 19 | 2026-10-30 | 34 | 84% |  |
| 254 | [x] | Stick It to the Stickman (STEAM) | 19 | 2026-10-17 | 34 | 76% |  |
| 255 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 19 | 2026-10-21 | 33 | 68% |  |
| 256 | [x] | Metro Exodus (STEAM) | 19 | 2026-10-20 | 31 | 89% |  |
| 257 | [x] | Torchlight II (EPIC) | 19 | 2026-10-22 | 27 | 100% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 258 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 19 | 2026-10-23 | 24 | 93% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 259 | [x] | Styx: Master of Shadows (EPIC) | 18 | 2026-11-03 | 40 | 38% |  |
| 260 | [x] | Graveyard Keeper (GOG) | 18 | 2026-10-25 | 38 | 21% |  |
| 261 | [x] | Faster Than Light (EPIC) | 18 | 2026-10-24 | 36 | 94% |  |
| 262 | [x] | SKALD: Against the Black Priory (STEAM) | 18 | 2026-10-20 | 36 | 97% |  |
| 263 | [x] | Killing Floor (STEAM) | 18 | 2026-10-19 | 34 | 87% |  |
| 264 | [x] | Far Far West (STEAM) | 18 | 2026-10-21 | 32 | 81% |  |
| 265 | [x] | Hitman: Absolution (GOG) | 18 | 2026-10-24 | 30 | 84% |  |
| 266 | [x] | Formula Legends (STEAM) | 18 | 2026-10-21 | 29 | 65% |  |
| 267 | [x] | Arcade Paradise (EPIC) | 18 | 2026-10-25 | 26 | 82% |  |
| 268 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-01 | 23 | 77% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 269 | [x] | Grim Fandango Remastered (STEAM) | 17 | 2026-10-19 | 37 | 77% |  |
| 270 | [x] | Backpack Battles (STEAM) | 17 | 2026-10-21 | 35 | 96% |  |
| 271 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 17 | 2026-10-20 | 35 | 73% |  |
| 272 | [x] | Spin Rhythm XD (STEAM) | 17 | 2026-10-18 | 35 | 83% |  |
| 273 | [x] | CULTIC (STEAM) | 17 | 2026-10-24 | 34 | 65% |  |
| 274 | [x] | SCP – Containment Breach (STEAM) | 17 | 2026-10-27 | 33 | 83% |  |
| 275 | [x] | GRIP: Combat Racing (STEAM) | 17 | 2026-10-20 | 32 | 83% |  |
| 276 | [x] | Lost Castle 2 (STEAM) | 17 | 2026-11-02 | 32 | 100% |  |
| 277 | [x] | GRANDIA HD Remaster (STEAM) | 17 | 2026-10-22 | 31 | 71% |  |
| 278 | [x] | Shank 2 (STEAM) | 17 | 2026-10-27 | 30 | 100% |  |
| 279 | [x] | Tabletop Simulator (STEAM) | 17 | 2026-10-19 | 29 | 61% |  |
| 280 | [x] | Maneater (STEAM) | 17 | 2026-10-20 | 28 | 77% |  |
| 281 | [x] | Dishonored 2 (STEAM) | 17 | 2026-10-20 | 27 | 92% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 282 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 17 | 2026-10-20 | 27 | 78% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 283 | [x] | Grim Fandango Remastered (GOG) | 17 | 2026-11-03 | 25 | 60% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 284 | [x] | DOOM 3: BFG Edition (GOG) | 17 | 2026-10-19 | 24 | 79% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 285 | [x] | Katanaut (STEAM) | 17 | 2026-10-20 | 24 | 69% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 286 | [x] | Fall Guys (STEAM) | 17 | 2026-10-26 | 23 | 92% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 287 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 288 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 289 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 51 | 100% |  |
| 290 | [x] | No Man's Sky (GOG) | 16 | 2026-10-19 | 37 | 76% |  |
| 291 | [x] | Kingdom Come: Deliverance II (STEAM) | 16 | 2026-10-20 | 35 | 100% |  |
| 292 | [x] | Mini Metro (STEAM) | 16 | 2026-11-01 | 34 | 52% |  |
| 293 | [x] | Mark of the Ninja (STEAM) | 16 | 2026-10-26 | 31 | 64% |  |
| 294 | [x] | DNF Duel (EPIC) | 16 | 2026-10-21 | 29 | 90% |  |
| 295 | [x] | Titanfall® 2 (STEAM) | 16 | 2026-10-16 | 28 | 81% |  |
| 296 | [x] | WORLD OF FINAL FANTASY (STEAM) | 16 | 2026-10-19 | 27 | 77% |  |
| 297 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 16 | 2026-10-21 | 25 | 96% |  |
| 298 | [x] | Chef Knight (STEAM) | 16 | 2026-10-27 | 23 | 69% |  |
| 299 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 2026-10-21 | 22 | 88% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 300 | [x] | Jotunnslayer: Hordes of Hel (STEAM) | 16 | 2026-10-30 | 20 | 91% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 301 | [x] | Antichamber (STEAM) | 15 | 2026-10-20 | 30 | 88% |  |
| 302 | [x] | Wildermyth (STEAM) | 15 | 2026-10-26 | 26 | 94% |  |
| 303 | [x] | Mortal Shell (EPIC) | 15 | 2026-10-19 | 25 | 87% |  |
| 304 | [x] | LET IT DIE (STEAM) | 15 | 2026-10-25 | 25 | 73% |  |
| 305 | [x] | Batman™: Arkham Origins (GOG) | 15 | 2026-10-22 | 24 | 93% |  |
| 306 | [x] | Super Monkey Ball Banana Mania (STEAM) | 15 | 2026-10-18 | 24 | 65% |  |
| 307 | [x] | Sons Of The Forest (STEAM) | 15 | 2026-10-19 | 23 | 77% |  |
| 308 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 15 | 2026-10-20 | 23 | 69% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 309 | [x] | Allumeria (STEAM) | 15 | 2026-10-23 | 22 | 69% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 310 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 311 | [x] | Cyberpunk 2077 (EPIC) | 15 | 2026-10-19 | 20 | 81% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 312 | [x] | Maneater (EPIC) | 15 | 2026-10-28 | 20 | 77% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 313 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 314 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 29 | n/a |  |
| 315 | [x] | Rayman Origins (GOG) | 14 | 2026-11-02 | 29 | 56% |  |
| 316 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 2026-10-29 | 28 | 85% |  |
| 317 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 14 | 2026-10-21 | 25 | 93% |  |
| 318 | [x] | Ultrapool (STEAM) | 14 | 2026-10-24 | 25 | 100% |  |
| 319 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 2026-10-25 | 24 | 73% |  |
| 320 | [x] | Gloomwood (STEAM) | 14 | 2026-10-29 | 24 | 75% |  |
| 321 | [x] | Alabaster Dawn Demo (STEAM) | 14 | 2026-10-27 | 23 | 94% |  |
| 322 | [x] | Songs of Conquest (EPIC) | 14 | 2026-11-02 | 22 | 90% |  |
| 323 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-10-23 | 22 | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 324 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 325 | [x] | Horny Villa (STEAM) | 14 | 2026-10-21 | 20 | 95% |  |
| 326 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 327 | [x] | Middle-earth™: Shadow of War™ (STEAM) | 13 | 2026-10-16 | 39 | 75% |  |
| 328 | [x] | Blood: Fresh Supply (STEAM) | 13 | 2026-10-16 | 36 | 80% |  |
| 329 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 13 | 2026-10-21 | 32 | 83% |  |
| 330 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 32 | 63% |  |
| 331 | [x] | Distance (STEAM) | 13 | 2026-10-19 | 30 | 83% |  |
| 332 | [x] | Breath of Fire IV (GOG) | 13 | 2026-10-26 | 28 | 67% |  |
| 333 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 13 | 2026-11-01 | 28 | 55% |  |
| 334 | [x] | Dead Space™ 3 (STEAM) | 13 | 2026-10-20 | 28 | 74% |  |
| 335 | [x] | Haiku, the Robot (STEAM) | 13 | 2026-10-21 | 28 | 85% |  |
| 336 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 13 | 2026-10-18 | 28 | 92% |  |
| 337 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 28 | 50% |  |
| 338 | [x] | Aperture Desk Job (STEAM) | 13 | 2026-11-03 | 27 | n/a |  |
| 339 | [x] | Human Fall Flat (STEAM) | 13 | 2026-10-29 | 26 | 65% |  |
| 340 | [x] | Lust Goddess (STEAM) | 13 | 2026-10-26 | 25 | 67% |  |
| 341 | [x] | Sid Meier's Civilization VI (EPIC) | 13 | 2026-10-19 | 24 | 86% |  |
| 342 | [x] | Look Outside (GOG) | 13 | 2026-11-01 | 24 | 100% |  |
| 343 | [x] | Haydee (STEAM) | 13 | 2026-10-22 | 24 | 85% |  |
| 344 | [x] | Pillars of Eternity (STEAM) | 13 | 2026-10-26 | 24 | 65% |  |
| 345 | [x] | DiRT 4 (STEAM) | 13 | 2026-10-20 | 23 | 96% |  |
| 346 | [x] | 12 is Better Than 6 (STEAM) | 13 | 2026-10-21 | 22 | 85% |  |
| 347 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-10-21 | 22 | 91% |  |
| 348 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 13 | 2026-10-28 | 21 | 64% |  |
| 349 | [x] | Secret of Mana (STEAM) | 13 | 2026-10-28 | 21 | 64% |  |
| 350 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 92% |  |
| 351 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 13 | 2026-10-23 | 20 | 63% |  |
| 352 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 83% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 353 | [x] | The WereCleaner (STEAM) | 12 | 2026-10-22 | 31 | 95% |  |
| 354 | [x] | Tom Clancy's Splinter Cell: Chaos Theory (STEAM) | 12 | 2026-10-16 | 30 | 85% |  |
| 355 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 12 | 2026-10-19 | 29 | 98% |  |
| 356 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 26 | 70% |  |
| 357 | [x] | Sonic Superstars (STEAM) | 12 | 2026-10-21 | 24 | 65% |  |
| 358 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-10-28 | 23 | 92% |  |
| 359 | [x] | UNDEFEATED (STEAM) | 12 | 2026-11-01 | 23 | 82% |  |
| 360 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-10-22 | 22 | 88% |  |
| 361 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 92% |  |
| 362 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 2026-10-26 | 21 | 94% |  |
| 363 | [x] | Human Resource Machine (EPIC) | 12 | 2026-11-01 | 20 | 60% |  |
| 364 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 365 | [x] | PAYDAY: The Heist (STEAM) | 12 | 2026-11-02 | 20 | 73% |  |
| 366 | [x] | Shift At Midnight (STEAM) | 12 | 2026-11-01 | 20 | 90% |  |
| 367 | [x] | Mortal Kombat 11 (STEAM) | 11 | 2026-10-28 | 27 | 68% |  |
| 368 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 11 | 2026-10-20 | 26 | 72% |  |
| 369 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 2026-10-27 | 23 | 79% |  |
| 370 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 23 | 80% |  |
| 371 | [x] | Castle in the Clouds (STEAM) | 11 | 2026-10-21 | 22 | 85% |  |
| 372 | [x] | Injustice™ 2 (STEAM) | 11 | 2026-10-17 | 22 | 73% |  |
| 373 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 11 | 2026-10-23 | 22 | 94% |  |
| 374 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 2026-10-25 | 21 | 95% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 375 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 376 | [x] | TowerFall Ascension (STEAM) | 10 | 2026-10-16 | 30 | 53% |  |
| 377 | [x] | Possessor(s) (STEAM) | 10 | 2026-10-24 | 27 | 100% |  |
| 378 | [x] | Divinity: Original Sin (Classic) (STEAM) | 10 | 2026-10-16 | 23 | 82% |  |
| 379 | [x] | Mina the Hollower (GOG) | 10 | 2026-10-28 | 22 | 53% |  |
| 380 | [x] | SteamWorld Heist (GOG) | 10 | 2026-10-25 | 22 | 60% |  |
| 381 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 22 | 89% |  |
| 382 | [x] | DRAGON BALL XENOVERSE (STEAM) | 10 | 2026-10-28 | 21 | 61% |  |
| 383 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 384 | [x] | Coromon (GOG) | 10 | 2026-10-19 | 20 | 65% |  |
| 385 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 10 | 2026-10-24 | 20 | 74% |  |
| 386 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 387 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 388 | [x] | What Remains of Edith Finch (STEAM) | 9 | 2026-10-19 | 26 | 48% |  |
| 389 | [x] | Delver (STEAM) | 9 | 2026-10-17 | 22 | 76% |  |
| 390 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 9 | 2026-10-23 | 22 | 69% |  |
| 391 | [x] | Football Manager 2024 (STEAM) | 9 | 2026-10-16 | 20 | n/a |  |
| 392 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 8% |  |
| 393 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 9 | 2026-10-20 | 20 | n/a |  |
| 394 | [x] | Gloomhaven (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 395 | [x] | Intravenous (STEAM) | 8 | 2026-10-16 | 20 | 94% |  |
| 396 | [x] | Mafia II: Definitive Edition (STEAM) | 7 | 2026-10-16 | 20 | n/a |  |
| 397 | [x] | Alex Kidd in Miracle World DX (STEAM) | 2 | 2026-10-16 | 36 | 87% |  |
