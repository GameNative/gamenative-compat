# GameNative compatibility worklist

Generated: `2026-10-29T04:15:06.915Z` · App release: `1.3.0` · Ratings since: `2026-07-31T04:15:06.915Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 290 |
| Probably does not work | 90 |
| First launch fails | 365 |
| Mixed | 460 |
| Works | 1004 |
| Total | 2209 |

## Does not work (290)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [x] 2026-10-18 | Project Zomboid (STEAM) | 637 | 677 | 91% (1.3.0) | Does not open (66%) | 49% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 2 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 262 | 281 | 93% (90d) | Does not open (75%) | 9% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 3 | [x] 2026-10-18 | Alan Wake (STEAM) | 255 | 265 | 91% (1.3.0) | Does not open (86%) | 9% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 4 | [ ] | Counter-Strike 2 (STEAM) | 232 | 319 | 84% (1.3.0) | Does not open (61%) | 44% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 5 | [ ] | DRAGON BALL FighterZ (STEAM) | 217 | 245 | 76% (1.3.0) | Does not open (87%) | 55% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 6 | [x] 2026-10-18 | Call of Duty: Black Ops (STEAM) | 216 | 226 | 96% (90d) | Does not open (75%) | 15% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 7 | [ ] | skate. (STEAM) | 206 | 221 | 93% (90d) | Does not open (81%) | 19% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 8 | [x] 2026-10-18 | Sid Meier's Civilization V (STEAM) | 182 | 194 | 94% (90d) | Does not open (77%) | 47% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 9 | [ ] | Necesse (STEAM) | 180 | 187 | 96% (90d) | Does not open (80%) | 54% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 10 | [ ] | Peggle Deluxe (STEAM) | 161 | 191 | 84% (90d) | Does not open (92%) | 41% | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 11 | [ ] | Sonic Adventure™ 2  (STEAM) | 153 | 212 | 72% (90d) | Does not open (74%) | 55% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 12 | [ ] | HELLDIVERS™ 2 (STEAM) | 143 | 150 | 95% (90d) | Does not open (92%) | 25% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 13 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 138 | 154 | 90% (90d) | Does not open (88%) | 42% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 14 | [ ] | Sol Cesto (EPIC) | 137 | 145 | 94% (90d) | Does not open (74%) | 58% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 15 | [ ] | Assassin's Creed II (STEAM) | 134 | 139 | 96% (90d) | Does not open (79%) | 51% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 16 | [ ] | Call of Duty: Black Ops II (STEAM) | 109 | 142 | 77% (90d) | Does not open (77%) | 23% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 17 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 108 | 121 | 89% (90d) | No graphics (59%) | 52% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 18 | [ ] | Dust: An Elysian Tail (STEAM) | 108 | 112 | 96% (90d) | Does not open (71%) | 8% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 19 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 106 | 141 | 75% (90d) | Does not open (73%) | 44% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 20 | [ ] | Transistor (STEAM) | 106 | 106 | 100% (90d) | Does not open (77%) | 0% | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 21 | [ ] | The Witcher: Enhanced Edition (GOG) | 103 | 113 | 91% (90d) | Does not open (75%) | 15% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 22 | [ ] | Mafia II (Classic) (STEAM) | 97 | 102 | 95% (90d) | Does not open (72%) | 7% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 23 | [ ] | Saints Row: The Third (STEAM) | 97 | 98 | 99% (90d) | Does not open (79%) | n/a | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 24 | [ ] | Saints Row 2 (STEAM) | 93 | 107 | 90% (1.3.0) | Does not open (95%) | 43% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 25 | [ ] | Fall Guys (EPIC) | 93 | 105 | 89% (90d) | Does not open (74%) | 7% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 26 | [ ] | Black Mesa (STEAM) | 92 | 126 | 73% (90d) | Does not open (82%) | 15% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 27 | [ ] | Dead Space 2 (STEAM) | 89 | 111 | 80% (90d) | Does not open (77%) | 37% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 28 | [ ] | Duskfade (STEAM) | 87 | 89 | 98% (90d) | Does not open (95%) | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 29 | [ ] | Sniper Elite 4 (STEAM) | 84 | 85 | 99% (90d) | Does not open (96%) | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 30 | [ ] | HELLDIVERS™ (STEAM) | 83 | 96 | 86% (90d) | Does not open (60%) | 45% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 31 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 81 | 84 | 96% (90d) | Does not open (92%) | 57% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 32 | [ ] | MECCHA CHAMELEON (STEAM) | 80 | 115 | 70% (90d) | Does not open (67%) | 58% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 33 | [ ] | GRID 2 (STEAM) | 79 | 83 | 95% (90d) | Does not open (67%) | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 34 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 78 | 84 | 93% (90d) | Does not open (71%) | 0% | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 35 | [ ] | Burnout™ Paradise Remastered (STEAM) | 76 | 80 | 95% (90d) | Does not open (89%) | 16% | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 36 | [ ] | Call of Duty: Black Ops II - Zombies (STEAM) | 75 | 88 | 85% (90d) | Does not open (72%) | 48% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 37 | [ ] | The Wolf Among Us (STEAM) | 75 | 84 | 89% (90d) | Does not open (68%) | 10% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 38 | [ ] | Saints Row 2 (GOG) | 73 | 86 | 85% (90d) | Does not open (97%) | 49% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 39 | [ ] | Marvel Rivals (STEAM) | 73 | 82 | 89% (90d) | Does not open (80%) | 0% | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 40 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 72 | 77 | 94% (90d) | Does not open (77%) | 10% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 41 | [ ] | Borderlands GOTY (STEAM) | 71 | 77 | 92% (90d) | Does not open (94%) | 29% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 42 | [ ] | XCOM: Enemy Unknown (STEAM) | 71 | 74 | 96% (90d) | Does not open (75%) | 9% | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 43 | [ ] | Need for Speed™ Heat  (STEAM) | 69 | 83 | 83% (90d) | Does not open (80%) | 32% | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 44 | [x] 2026-10-18 | Diablo® IV (STEAM) | 69 | 81 | 85% (90d) | Does not open (63%) | 20% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 45 | [ ] | GRID (STEAM) | 67 | 84 | 80% (90d) | Does not open (55%) | 52% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 46 | [ ] | Metro 2033 (STEAM) | 67 | 83 | 81% (90d) | Does not open (66%) | 54% | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 47 | [ ] | Door Kickers 2 (STEAM) | 67 | 72 | 93% (90d) | No graphics (85%) | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 48 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 65 | 65 | 100% (90d) | No graphics (54%) | 8% | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 49 | [ ] | Three Kingdoms : Alias (STEAM) | 62 | 66 | 94% (90d) | No graphics (97%) | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 50 | [ ] | DOOM (2016) (GOG) | 61 | 67 | 91% (90d) | Does not open (91%) | 44% | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 51 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 60 | 86 | 70% (90d) | Does not open (84%) | 55% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 52 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 60 | 69 | 87% (90d) | No graphics (49%) | 24% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 53 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 59 | 72 | 82% (90d) | Does not open (90%) | 53% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 54 | [ ] | Spore (STEAM) | 59 | 64 | 92% (90d) | Does not open (68%) | n/a | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 55 | [ ] | Spec Ops: The Line (STEAM) | 59 | 60 | 98% (90d) | Does not open (60%) | n/a | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 56 | [ ] | METAL SLUG 3 (STEAM) | 57 | 65 | 88% (90d) | Does not open (85%) | 17% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 57 | [ ] | GrandChase (STEAM) | 57 | 60 | 95% (90d) | Does not open (85%) | 10% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 58 | [ ] | Watch_Dogs (STEAM) | 56 | 67 | 84% (90d) | Does not open (91%) | 19% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 59 | [ ] | Overwatch® (STEAM) | 56 | 58 | 97% (90d) | Does not open (59%) | 17% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 60 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 55 | 70 | 79% (90d) | Does not open (82%) | 30% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 61 | [ ] | DOOM 3 (STEAM) | 55 | 63 | 87% (90d) | Does not open (88%) | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 62 | [ ] | Max Payne 3 (STEAM) | 55 | 60 | 92% (90d) | Does not open (93%) | 44% | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 63 | [ ] | Fortune Mill (STEAM) | 55 | 56 | 98% (90d) | Does not open (89%) | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 64 | [ ] | Vampire Survivors (EPIC) | 54 | 76 | 71% (90d) | Does not open (65%) | 56% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 65 | [ ] | RoboCop: Rogue City (STEAM) | 54 | 58 | 93% (90d) | Does not open (42%) | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 66 | [ ] | STAR WARS Zero Company™ (STEAM) | 53 | 55 | 96% (90d) | Does not open (64%) | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 67 | [ ] | Asphalt Legends  (STEAM) | 52 | 60 | 87% (90d) | Does not open (79%) | 42% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 68 | [ ] | Enshrouded (STEAM) | 52 | 53 | 98% (90d) | Does not open (92%) | 17% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 69 | [ ] | South Park The Fractured But Whole (STEAM) | 52 | 52 | 100% (90d) | Does not open (66%) | 19% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 70 | [ ] | Trackmania (STEAM) | 51 | 65 | 78% (90d) | Does not open (86%) | 47% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 71 | [ ] | Split/Second (STEAM) | 51 | 60 | 85% (90d) | Does not open (76%) | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 72 | [ ] | Hitman: Absolution (STEAM) | 51 | 56 | 91% (90d) | Does not open (84%) | 8% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 73 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 51 | 53 | 96% (90d) | No graphics (62%) | 20% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 74 | [ ] | Sandustry (STEAM) | 50 | 62 | 81% (90d) | Does not open (73%) | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 75 | [ ] | Watch_Dogs 2 (STEAM) | 50 | 57 | 88% (90d) | Does not open (97%) | 59% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 76 | [ ] | tModLoader (STEAM) | 50 | 57 | 88% (90d) | Does not open (85%) | 4% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 77 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 50 | 53 | 94% (90d) | Does not open (95%) | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 78 | [ ] | Scott Pilgrim vs The World (STEAM) | 49 | 49 | 100% (90d) | Does not open (83%) | 54% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 79 | [ ] | Prince of Persia The Lost Crown (STEAM) | 48 | 53 | 91% (90d) | Does not open (94%) | 40% | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 80 | [ ] | DOOM Eternal (STEAM) | 48 | 50 | 96% (90d) | Does not open (69%) | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 81 | [ ] | Aliens vs. Predator (STEAM) | 47 | 53 | 89% (90d) | No graphics (53%) | 24% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 82 | [ ] | ARC Raiders (STEAM) | 47 | 52 | 90% (90d) | Does not open (93%) | 0% | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 83 | [ ] | STAR WARS™ Republic Commando (STEAM) | 47 | 50 | 94% (90d) | Does not open (81%) | 47% | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 84 | [ ] | The Survivalists (STEAM) | 47 | 49 | 96% (90d) | Does not open (98%) | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 85 | [ ] | State of Decay 2 (STEAM) | 45 | 64 | 70% (90d) | Does not open (93%) | 0% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 86 | [ ] | Mafia: Definitive Edition (GOG) | 45 | 60 | 75% (90d) | Does not open (86%) | 27% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 87 | [ ] | Diablo + Hellfire (GOG) | 45 | 50 | 90% (90d) | Does not open (66%) | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 88 | [ ] | Tales of Berseria (STEAM) | 45 | 46 | 98% (90d) | Does not open (88%) | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 89 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 44 | 45 | 98% (90d) | Does not open (82%) | 42% | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 90 | [ ] | Need for Speed™ Rivals (STEAM) | 43 | 51 | 84% (90d) | Does not open (57%) | 39% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 91 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 43 | 48 | 90% (90d) | Does not open (76%) | 13% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 92 | [ ] | GOALS (STEAM) | 42 | 49 | 86% (90d) | Does not open (77%) | 25% | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 93 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 41 | 42 | 98% (90d) | Does not open (61%) | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 94 | [ ] | DJMAX RESPECT V (STEAM) | 40 | 44 | 91% (90d) | Does not open (83%) | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 95 | [ ] | Elite Dangerous (STEAM) | 40 | 43 | 93% (90d) | Does not open (79%) | 58% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 96 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 40 | 41 | 98% (90d) | Does not open (59%) | 0% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 97 | [ ] | Mafia (STEAM) | 39 | 44 | 89% (90d) | Does not open (70%) | 41% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 98 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 39 | 41 | 95% (90d) | Does not open (94%) | 27% | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 99 | [ ] | GeoGuessr Steam Edition (STEAM) | 39 | 40 | 98% (90d) | No graphics (62%) | n/a | [#154](https://github.com/GameNative/gamenative-compat/issues/154) |
| 100 | [ ] | Utopia Must Fall (STEAM) | 39 | 39 | 100% (90d) | Does not open (84%) | n/a | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 101 | [ ] | Marvel's Spider-Man 2 (STEAM) | 38 | 40 | 95% (90d) | Does not open (87%) | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 102 | [ ] | Forza Horizon 6 (STEAM) | 38 | 39 | 97% (90d) | Does not open (64%) | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 103 | [ ] | FINAL FANTASY VIII (STEAM) | 37 | 45 | 82% (90d) | Does not open (64%) | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 104 | [ ] | L.A. Noire (STEAM) | 37 | 44 | 84% (90d) | Does not open (96%) | 53% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 105 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 37 | 43 | 86% (90d) | No graphics (68%) | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 106 | [ ] | ScourgeBringer (STEAM) | 37 | 42 | 88% (90d) | Does not open (66%) | 6% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 107 | [ ] | Barotrauma (STEAM) | 37 | 40 | 93% (90d) | Does not open (97%) | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 108 | [ ] | BIT.TRIP RUNNER (STEAM) | 37 | 39 | 95% (90d) | Does not open (59%) | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 109 | [ ] | Forza Horizon 5 (STEAM) | 37 | 39 | 95% (90d) | Does not open (66%) | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 110 | [ ] | Dragon's Dogma 2 (STEAM) | 37 | 38 | 97% (90d) | Does not open (91%) | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 111 | [ ] | Mafia II (Classic) (GOG) | 36 | 51 | 71% (90d) | Does not open (94%) | 20% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 112 | [ ] | CODE VEIN (STEAM) | 36 | 48 | 75% (90d) | Does not open (69%) | 29% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 113 | [ ] | Beat Saber (STEAM) | 36 | 42 | 86% (90d) | Does not open (45%) | 36% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 114 | [ ] | Beholder (EPIC) | 35 | 42 | 83% (90d) | Does not open (58%) | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 115 | [ ] | OneShot (STEAM) | 35 | 40 | 88% (90d) | Does not open (97%) | 25% | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 116 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 35 | 38 | 92% (90d) | Does not open (68%) | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 117 | [ ] | The Darkness II (STEAM) | 35 | 35 | 100% (90d) | Does not open (80%) | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 118 | [ ] | Call of Duty® (STEAM) | 34 | 43 | 79% (90d) | No graphics (64%) | 7% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 119 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 34 | 39 | 87% (90d) | Does not open (68%) | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 120 | [ ] | BattleBit Remastered (STEAM) | 34 | 38 | 89% (90d) | Does not open (61%) | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 121 | [ ] | Death Stranding (EPIC) | 34 | 37 | 92% (90d) | Does not open (75%) | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 122 | [ ] | Dark Sector (STEAM) | 33 | 44 | 75% (90d) | Does not open (67%) | 43% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 123 | [ ] | CARRION (GOG) | 33 | 41 | 80% (90d) | Does not open (74%) | 8% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 124 | [ ] | Mass Effect (2007) (STEAM) | 33 | 40 | 83% (90d) | Does not open (81%) | 58% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 125 | [ ] | Wolfenstein 3D (STEAM) | 33 | 36 | 92% (90d) | Does not open (52%) | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 126 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 33 | 35 | 94% (90d) | Does not open (74%) | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 127 | [ ] | PRAGMATA (STEAM) | 33 | 35 | 94% (90d) | Does not open (59%) | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 128 | [ ] | Umamusume: Pretty Derby (STEAM) | 33 | 34 | 97% (90d) | Does not open (81%) | n/a | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 129 | [ ] | Gauntlet™  (STEAM) | 32 | 45 | 71% (90d) | Does not open (67%) | 40% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 130 | [ ] | Far Cry 4 (STEAM) | 32 | 36 | 89% (90d) | Does not open (100%) | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 131 | [ ] | DiRT Showdown (STEAM) | 32 | 33 | 97% (90d) | Does not open (60%) | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 132 | [ ] | Hitman: Blood Money (STEAM) | 32 | 33 | 97% (90d) | Does not open (86%) | 12% | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 133 | [ ] | Rayman Legends (STEAM) | 32 | 33 | 97% (90d) | Does not open (96%) | 54% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 134 | [ ] | Quantum Break (STEAM) | 32 | 32 | 100% (90d) | Does not open (91%) | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 135 | [ ] | Yume Nikki (STEAM) | 31 | 49 | 90% (14d) | Does not open (94%) | 0% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 136 | [ ] | Metro: Last Light Complete Edition (STEAM) | 31 | 40 | 78% (90d) | Does not open (56%) | 59% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 137 | [ ] | Insaniquarium! Deluxe (STEAM) | 31 | 39 | 79% (90d) | Does not open (86%) | 35% | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 138 | [ ] | CPM 2 (STEAM) | 31 | 38 | 82% (90d) | Does not open (91%) | 7% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 139 | [ ] | Sir, We Have an Orc Problem (STEAM) | 31 | 38 | 82% (90d) | Does not open (80%) | n/a | [#145](https://github.com/GameNative/gamenative-compat/issues/145) |
| 140 | [ ] | King's Bounty: The Legend (STEAM) | 31 | 34 | 91% (90d) | Does not open (100%) | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 141 | [ ] | The Lord of the Rings: War in the North (STEAM) | 31 | 33 | 94% (90d) | Does not open (86%) | n/a | [#195](https://github.com/GameNative/gamenative-compat/issues/195) |
| 142 | [ ] | Muv-Luv (STEAM) | 31 | 32 | 97% (90d) | Does not open (86%) | 45% | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 143 | [ ] | Breath of Fire IV (STEAM) | 31 | 31 | 100% (90d) | Does not open (62%) | 19% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 144 | [ ] | Grand Theft Auto III - The Definitive Edition (STEAM) | 31 | 31 | 100% (90d) | Does not open (92%) | 16% | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 145 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 30 | 40 | 75% (90d) | Does not open (63%) | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 146 | [ ] | Magicka (STEAM) | 30 | 33 | 91% (90d) | Does not open (64%) | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 147 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 30 | 31 | 97% (90d) | Does not open (95%) | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 148 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 30 | 30 | 100% (90d) | Does not open (72%) | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 149 | [ ] | EA SPORTS FC™ 26 (STEAM) | 29 | 37 | 78% (90d) | Does not open (77%) | n/a | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 150 | [ ] | Subnautica 2 (STEAM) | 29 | 35 | 83% (90d) | Does not open (68%) | 50% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 151 | [ ] | Alpha Protocol (STEAM) | 29 | 33 | 88% (90d) | Does not open (60%) | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 152 | [ ] | Zuma Deluxe (STEAM) | 29 | 32 | 91% (90d) | Does not open (96%) | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 153 | [ ] | Borderlands 2 RU (STEAM) | 29 | 31 | 94% (90d) | Does not open (60%) | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 154 | [ ] | Audiosurf (STEAM) | 28 | 40 | 70% (90d) | Does not open (46%) | 43% | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 155 | [ ] | Persona 5 Strikers (STEAM) | 28 | 31 | 90% (90d) | Does not open (72%) | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 156 | [ ] | Wuthering Waves (STEAM) | 28 | 30 | 93% (90d) | Does not open (78%) | n/a | [#216](https://github.com/GameNative/gamenative-compat/issues/216) |
| 157 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 28 | 28 | 100% (90d) | Does not open (68%) | 0% | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 158 | [ ] | The Planet Crafter (STEAM) | 27 | 33 | 82% (90d) | Does not open (52%) | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 159 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 27 | 30 | 90% (90d) | Does not open (81%) | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 160 | [ ] | PAYDAY 2 (STEAM) | 27 | 30 | 90% (90d) | Does not open (78%) | 38% | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 161 | [ ] | WRC 7 (STEAM) | 27 | 28 | 96% (90d) | Does not open (72%) | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 162 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 27 | 27 | 100% (90d) | Does not open (60%) | n/a | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 163 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 26 | 33 | 79% (90d) | Does not open (50%) | 13% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 164 | [ ] | SOMA (STEAM) | 26 | 33 | 79% (90d) | Does not open (77%) | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 165 | [ ] | Singularity™ (GOG) | 26 | 31 | 84% (90d) | Does not open (100%) | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 166 | [ ] | Turing Complete (STEAM) | 26 | 29 | 90% (90d) | Does not open (91%) | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 167 | [ ] | AION 2 (STEAM) | 26 | 28 | 93% (90d) | Does not open (65%) | 10% | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 168 | [ ] | Alien Breed: Impact (STEAM) | 26 | 28 | 93% (90d) | Does not open (80%) | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 169 | [ ] | Northgard: Definitive Edition (STEAM) | 26 | 27 | 96% (90d) | Does not open (96%) | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 170 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 26 | 27 | 96% (90d) | Does not open (82%) | 38% | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 171 | [ ] | Isle of Reveries (STEAM) | 26 | 26 | 100% (90d) | Does not open (95%) | 27% | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 172 | [ ] | Resident Evil Requiem (STEAM) | 26 | 26 | 100% (90d) | Does not open (76%) | n/a | [#210](https://github.com/GameNative/gamenative-compat/issues/210) |
| 173 | [ ] | Mirror's Edge™ (GOG) | 25 | 34 | 74% (90d) | No graphics (67%) | 42% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 174 | [ ] | Content Warning (STEAM) | 25 | 33 | 76% (90d) | Does not open (55%) | n/a | [#241](https://github.com/GameNative/gamenative-compat/issues/241) |
| 175 | [ ] | Kenshi (STEAM) | 25 | 32 | 78% (90d) | Does not open (79%) | 12% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 176 | [ ] | Knights of Pen and Paper 2 (STEAM) | 25 | 32 | 78% (90d) | Does not open (45%) | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 177 | [ ] | ENDLESS Space™ 2 (STEAM) | 25 | 30 | 83% (90d) | Does not open (94%) | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 178 | [ ] | Bionic Commando Rearmed (STEAM) | 25 | 28 | 89% (90d) | Does not open (74%) | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 179 | [ ] | Axiom Verge 2 (STEAM) | 25 | 26 | 96% (90d) | Does not open (76%) | 13% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 180 | [ ] | Bingle Bingle (STEAM) | 25 | 26 | 96% (90d) | Does not open (80%) | n/a | [#225](https://github.com/GameNative/gamenative-compat/issues/225) |
| 181 | [ ] | Euro Truck Simulator (STEAM) | 25 | 26 | 96% (90d) | Does not open (94%) | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 182 | [ ] | Gears 5 (STEAM) | 25 | 25 | 100% (90d) | Does not open (90%) | n/a | [#264](https://github.com/GameNative/gamenative-compat/issues/264) |
| 183 | [ ] | Spiral Knights (STEAM) | 25 | 25 | 100% (90d) | Does not open (74%) | n/a | [#263](https://github.com/GameNative/gamenative-compat/issues/263) |
| 184 | [ ] | Cities: Skylines (STEAM) | 24 | 34 | 71% (90d) | Does not open (59%) | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 185 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 24 | 34 | 71% (90d) | Does not open (95%) | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 186 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 24 | 33 | 73% (90d) | Does not open (57%) | 58% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 187 | [ ] | CarX Street (STEAM) | 24 | 31 | 77% (90d) | Does not open (80%) | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 188 | [ ] | Transformers: Fall of Cybertron (STEAM) | 24 | 31 | 77% (90d) | Does not open (65%) | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 189 | [ ] | My Singing Monsters (STEAM) | 24 | 30 | 80% (90d) | Does not open (83%) | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 190 | [ ] | The Swapper (STEAM) | 24 | 28 | 86% (90d) | Does not open (52%) | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 191 | [ ] | Jade Empire: Special Edition (STEAM) | 24 | 26 | 92% (90d) | Does not open (95%) | 55% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 192 | [ ] | Peggle Nights (STEAM) | 24 | 26 | 92% (90d) | Does not open (94%) | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 193 | [ ] | Tearscape (STEAM) | 23 | 27 | 85% (90d) | Controller issues (53%) | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 194 | [ ] | skate.™ (EPIC) | 23 | 27 | 85% (90d) | Does not open (88%) | 10% | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 195 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 23 | 26 | 88% (90d) | Does not open (95%) | 56% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 196 | [ ] | SimCity 4 Deluxe (STEAM) | 23 | 26 | 88% (90d) | Does not open (82%) | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 197 | [ ] | They Are Billions (STEAM) | 23 | 26 | 88% (90d) | Does not open (70%) | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 198 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 23 | 25 | 92% (90d) | Does not open (63%) | n/a | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 199 | [ ] | Marie's Adventure (STEAM) | 23 | 23 | 100% (90d) | Does not open (100%) | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 200 | [ ] | Beat Cop (STEAM) | 22 | 30 | 73% (90d) | Does not open (76%) | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 201 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 22 | 28 | 79% (90d) | Does not open (64%) | n/a | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 202 | [ ] | Half-Life: Blue Shift (STEAM) | 22 | 26 | 85% (90d) | Does not open (85%) | n/a | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 203 | [ ] | Tom Clancy's Ghost Recon® Wildlands (STEAM) | 22 | 26 | 85% (90d) | Does not open (94%) | n/a | [#280](https://github.com/GameNative/gamenative-compat/issues/280) |
| 204 | [ ] | Halo: Spartan Assault (STEAM) | 22 | 25 | 88% (90d) | Does not open (79%) | 31% | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 205 | [ ] | Melatonin (STEAM) | 22 | 23 | 96% (90d) | Does not open (58%) | 50% | [#272](https://github.com/GameNative/gamenative-compat/issues/272) |
| 206 | [ ] | Rayman Legends (EPIC) | 22 | 23 | 96% (90d) | Does not open (92%) | n/a | [#286](https://github.com/GameNative/gamenative-compat/issues/286) |
| 207 | [ ] | The Lantern of the Laughless Saint (STEAM) | 22 | 23 | 96% (90d) | Does not open (79%) | n/a | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 208 | [ ] | Aggelos 2 (STEAM) | 21 | 26 | 81% (90d) | No graphics (90%) | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 209 | [ ] | Beyond Good & Evil™ (GOG) | 21 | 26 | 81% (90d) | Does not open (100%) | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 210 | [ ] | PICO PARK:Classic Edition (STEAM) | 21 | 25 | 84% (90d) | Does not open (90%) | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 211 | [ ] | Clive Barker's Undying (GOG) | 21 | 24 | 88% (90d) | Does not open (67%) | n/a | [#388](https://github.com/GameNative/gamenative-compat/issues/388) |
| 212 | [ ] | Dragon Age™ Inquisition (STEAM) | 21 | 24 | 88% (90d) | Does not open (76%) | 33% | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 213 | [ ] | Marvel's Midnight Suns (STEAM) | 21 | 24 | 88% (90d) | Does not open (84%) | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 214 | [ ] | Sapphire Safari (GOG) | 21 | 24 | 88% (90d) | Does not open (89%) | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 215 | [ ] | Need for Speed: Undercover (STEAM) | 21 | 23 | 91% (90d) | Does not open (88%) | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 216 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 21 | 23 | 91% (90d) | Does not open (90%) | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 217 | [ ] | No More Room in Hell (STEAM) | 21 | 22 | 95% (90d) | Does not open (95%) | n/a | [#365](https://github.com/GameNative/gamenative-compat/issues/365) |
| 218 | [ ] | Chronicles of the Wolf (STEAM) | 21 | 21 | 100% (90d) | No graphics (85%) | n/a | [#314](https://github.com/GameNative/gamenative-compat/issues/314) |
| 219 | [ ] | Resident Evil 3 Nemesis (1999) (STEAM) | 21 | 21 | 100% (90d) | Does not open (86%) | n/a | [#273](https://github.com/GameNative/gamenative-compat/issues/273) |
| 220 | [ ] | Return to Castle Wolfenstein (STEAM) | 21 | 21 | 100% (90d) | Does not open (95%) | n/a | [#321](https://github.com/GameNative/gamenative-compat/issues/321) |
| 221 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 21 | 21 | 100% (90d) | Does not open (71%) | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 222 | [ ] | Watch Dogs (EPIC) | 21 | 21 | 100% (90d) | Does not open (89%) | n/a | [#289](https://github.com/GameNative/gamenative-compat/issues/289) |
| 223 | [ ] | Fishing Planet (STEAM) | 20 | 28 | 71% (90d) | Does not open (93%) | 31% | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 224 | [ ] | Dungeon Keeper™ 2 (GOG) | 20 | 27 | 74% (90d) | Does not open (100%) | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 225 | [ ] | TEKKEN 8 (STEAM) | 20 | 27 | 74% (90d) | Does not open (88%) | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 226 | [ ] | Surviving Mars (STEAM) | 20 | 26 | 77% (90d) | Does not open (92%) | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 227 | [ ] | Assassin's Creed Brotherhood (STEAM) | 20 | 23 | 87% (90d) | Does not open (78%) | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 228 | [ ] | Apex Legends (STEAM) | 20 | 22 | 91% (90d) | Does not open (78%) | n/a | [#261](https://github.com/GameNative/gamenative-compat/issues/261) |
| 229 | [ ] | Assassin's Creed Rogue (STEAM) | 20 | 22 | 91% (90d) | Does not open (63%) | n/a | [#271](https://github.com/GameNative/gamenative-compat/issues/271) |
| 230 | [ ] | Grounded 2 (STEAM) | 20 | 21 | 95% (90d) | Does not open (56%) | n/a | [#317](https://github.com/GameNative/gamenative-compat/issues/317) |
| 231 | [ ] | Meowgic (STEAM) | 20 | 21 | 95% (90d) | Does not open (90%) | n/a | [#342](https://github.com/GameNative/gamenative-compat/issues/342) |
| 232 | [ ] | Mirror's Edge™ Catalyst (STEAM) | 20 | 21 | 95% (90d) | Does not open (67%) | 47% | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 233 | [ ] | Pathway (EPIC) | 20 | 21 | 95% (90d) | Does not open (61%) | n/a | [#298](https://github.com/GameNative/gamenative-compat/issues/298) |
| 234 | [ ] | The Last of Us™ Part I (STEAM) | 20 | 21 | 95% (90d) | Does not open (93%) | n/a | [#300](https://github.com/GameNative/gamenative-compat/issues/300) |
| 235 | [ ] | DiRT 2 (STEAM) | 20 | 20 | 100% (90d) | Does not open (85%) | n/a | [#471](https://github.com/GameNative/gamenative-compat/issues/471) |
| 236 | [ ] | Downfall - A Slay the Spire Fan Expansion (STEAM) | 20 | 20 | 100% (90d) | Does not open (68%) | n/a | [#320](https://github.com/GameNative/gamenative-compat/issues/320) |
| 237 | [ ] | Fogpiercer (STEAM) | 19 | 26 | 73% (90d) | Does not open (79%) | n/a | [#303](https://github.com/GameNative/gamenative-compat/issues/303) |
| 238 | [ ] | Yuppie Psycho (STEAM) | 19 | 26 | 73% (90d) | Does not open (75%) | n/a | [#325](https://github.com/GameNative/gamenative-compat/issues/325) |
| 239 | [ ] | Rune Factory 5 (STEAM) | 19 | 24 | 79% (90d) | Does not open (84%) | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 240 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 19 | 22 | 86% (90d) | Does not open (69%) | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 241 | [ ] | Mafia III: Definitive Edition (STEAM) | 19 | 22 | 86% (90d) | Does not open (95%) | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 242 | [ ] | The Elder Scrolls IV: Oblivion Remastered (STEAM) | 19 | 22 | 86% (90d) | Does not open (59%) | n/a | [#312](https://github.com/GameNative/gamenative-compat/issues/312) |
| 243 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 19 | 22 | 86% (90d) | Does not open (79%) | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 244 | [ ] | Gothic 1 Remake (STEAM) | 19 | 21 | 90% (90d) | Directx error (44%) | n/a | [#336](https://github.com/GameNative/gamenative-compat/issues/336) |
| 245 | [ ] | Call of Duty 2 (STEAM) | 19 | 20 | 95% (90d) | Does not open (80%) | n/a | [#340](https://github.com/GameNative/gamenative-compat/issues/340) |
| 246 | [ ] | GT Legends (STEAM) | 19 | 20 | 95% (90d) | Does not open (89%) | n/a | [#364](https://github.com/GameNative/gamenative-compat/issues/364) |
| 247 | [ ] | Jurassic World Evolution (EPIC) | 19 | 20 | 95% (90d) | Does not open (80%) | n/a | [#469](https://github.com/GameNative/gamenative-compat/issues/469) |
| 248 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (90d) | Does not open (64%) | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 249 | [ ] | Zenless Zone Zero (STEAM) | 19 | 20 | 95% (90d) | Does not open (76%) | n/a | [#369](https://github.com/GameNative/gamenative-compat/issues/369) |
| 250 | [ ] | We Were Here Together (EPIC) | 18 | 24 | 75% (90d) | Does not open (82%) | n/a | [#374](https://github.com/GameNative/gamenative-compat/issues/374) |
| 251 | [ ] | Hitman 2: Silent Assassin (STEAM) | 18 | 23 | 78% (90d) | Does not open (85%) | 56% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 252 | [ ] | Portal: First Slice (STEAM) | 18 | 23 | 78% (90d) | Does not open (92%) | n/a | [#354](https://github.com/GameNative/gamenative-compat/issues/354) |
| 253 | [ ] | Sid Meier's Pirates! (STEAM) | 18 | 23 | 78% (90d) | Does not open (92%) | n/a | [#293](https://github.com/GameNative/gamenative-compat/issues/293) |
| 254 | [ ] | Tyr (STEAM) | 18 | 23 | 78% (90d) | Does not open (36%) | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 255 | [ ] | Yakuza 0 (GOG) | 18 | 23 | 78% (90d) | Does not open (67%) | n/a | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 256 | [ ] | EVE Online (STEAM) | 18 | 22 | 82% (90d) | No graphics (50%) | 50% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 257 | [ ] | Genshin Impact (EPIC) | 18 | 22 | 82% (90d) | Does not open (85%) | n/a | [#326](https://github.com/GameNative/gamenative-compat/issues/326) |
| 258 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 18 | 22 | 82% (90d) | Does not open (100%) | 27% | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 259 | [ ] | Bright Memory (STEAM) | 18 | 21 | 86% (90d) | No graphics (83%) | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 260 | [ ] | Crusader Kings III (STEAM) | 18 | 21 | 86% (90d) | No graphics (64%) | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 261 | [ ] | NBA 2K26 (STEAM) | 18 | 21 | 86% (90d) | Does not open (83%) | n/a | [#384](https://github.com/GameNative/gamenative-compat/issues/384) |
| 262 | [ ] | Sacred Gold (STEAM) | 18 | 21 | 86% (90d) | Does not open (93%) | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 263 | [ ] | Battlefield™ 6 (STEAM) | 18 | 20 | 90% (90d) | Does not open (80%) | n/a | [#335](https://github.com/GameNative/gamenative-compat/issues/335) |
| 264 | [ ] | Fallen Aces (STEAM) | 18 | 20 | 90% (90d) | No graphics (77%) | n/a | [#250](https://github.com/GameNative/gamenative-compat/issues/250) |
| 265 | [ ] | Mafia II: Definitive Edition (GOG) | 18 | 20 | 90% (90d) | No graphics (60%) | 31% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 266 | [ ] | STALZONE (STEAM) | 18 | 20 | 90% (90d) | Does not open (100%) | n/a | [#338](https://github.com/GameNative/gamenative-compat/issues/338) |
| 267 | [ ] | Carnal Instinct (STEAM) | 17 | 24 | 71% (90d) | Does not open (57%) | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 268 | [ ] | Darksiders Warmastered Edition (EPIC) | 17 | 23 | 74% (90d) | Does not open (83%) | 38% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 269 | [ ] | Grim Fandango Remastered (GOG) | 17 | 23 | 74% (90d) | No graphics (78%) | n/a | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 270 | [ ] | SlashZero Demo (STEAM) | 17 | 23 | 74% (90d) | Does not open (75%) | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 271 | [ ] | Spark the Electric Jester (STEAM) | 17 | 23 | 74% (90d) | Does not open (60%) | 53% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 272 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 17 | 22 | 77% (90d) | Does not open (87%) | 42% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 273 | [ ] | Bejeweled 2 Deluxe (STEAM) | 17 | 21 | 81% (90d) | Does not open (93%) | n/a | [#329](https://github.com/GameNative/gamenative-compat/issues/329) |
| 274 | [ ] | Definitely Not Fried Chicken (EPIC) | 17 | 21 | 81% (90d) | Does not open (65%) | n/a | [#356](https://github.com/GameNative/gamenative-compat/issues/356) |
| 275 | [ ] | Dorfromantik (GOG) | 17 | 21 | 81% (90d) | Does not open (100%) | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 276 | [ ] | Tyrian 2000 (GOG) | 17 | 20 | 85% (90d) | Does not open (87%) | n/a | [#360](https://github.com/GameNative/gamenative-compat/issues/360) |
| 277 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 16 | 23 | 70% (90d) | No graphics (56%) | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 278 | [ ] | Make Way (EPIC) | 16 | 23 | 70% (90d) | Does not open (73%) | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 279 | [ ] | Hitman 3: Contracts (GOG) | 16 | 22 | 73% (90d) | Does not open (93%) | n/a | [#401](https://github.com/GameNative/gamenative-compat/issues/401) |
| 280 | [ ] | Re-Volt (STEAM) | 16 | 22 | 73% (90d) | Controller issues (71%) | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 281 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 16 | 21 | 76% (90d) | No graphics (67%) | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 282 | [ ] | Once Human (STEAM) | 16 | 20 | 80% (90d) | Does not open (63%) | n/a | [#395](https://github.com/GameNative/gamenative-compat/issues/395) |
| 283 | [ ] | The Last Stand: Aftermath (STEAM) | 16 | 20 | 80% (90d) | No graphics (50%) | n/a | [#324](https://github.com/GameNative/gamenative-compat/issues/324) |
| 284 | [ ] | shapez (STEAM) | 16 | 20 | 80% (90d) | No graphics (67%) | n/a | [#332](https://github.com/GameNative/gamenative-compat/issues/332) |
| 285 | [ ] | Fallout Classic (GOG) | 15 | 21 | 71% (90d) | Does not open (71%) | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 286 | [ ] | Jurassic World Evolution 2 (STEAM) | 15 | 21 | 71% (90d) | Does not open (45%) | n/a | [#448](https://github.com/GameNative/gamenative-compat/issues/448) |
| 287 | [ ] | Smushi Come Home (GOG) | 15 | 21 | 71% (90d) | Does not open (57%) | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 288 | [ ] | Space Rangers HD: A War Apart (STEAM) | 15 | 21 | 71% (90d) | Does not open (64%) | 50% | [#472](https://github.com/GameNative/gamenative-compat/issues/472) |
| 289 | [ ] | Hob (STEAM) | 14 | 20 | 70% (90d) | Does not open (60%) | 59% | [#416](https://github.com/GameNative/gamenative-compat/issues/416) |
| 290 | [ ] | Sword Art Online: Hollow Realization Deluxe Edition (STEAM) | 14 | 20 | 70% (90d) | Controller issues (92%) | n/a | [#470](https://github.com/GameNative/gamenative-compat/issues/470) |

## Probably does not work (90)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [x] 2026-10-18 | Spelunky 2 (STEAM) | 203 | 216 | 57% (14d) | Does not open (73%) | 41% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 2 | [ ] | Garry's Mod (STEAM) | 200 | 327 | 69% (1.3.0) | Does not open (79%) | 55% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 3 | [ ] | Prototype (STEAM) | 164 | 225 | 55% (1.3.0) | Does not open (75%) | 42% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 4 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 160 | 249 | 64% (90d) | Does not open (77%) | n/a |  |
| 5 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 144 | 181 | 52% (1.3.0) | Does not open (93%) | 39% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 6 | [ ] | Metro 2033 Redux (STEAM) | 141 | 346 | 59% (1.3.0) | Does not open (68%) | 51% |  |
| 7 | [ ] | Geometry Dash (STEAM) | 128 | 413 | 65% (1.3.0) | Does not open (67%) | 41% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 8 | [ ] | Euro Truck Simulator 2 (STEAM) | 120 | 211 | 58% (1.3.0) | Does not open (67%) | 59% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 9 | [ ] | VRChat (STEAM) | 91 | 137 | 66% (90d) | Does not open (64%) | 40% |  |
| 10 | [ ] | Hollow Knight: Silksong (GOG) | 74 | 113 | 65% (90d) | Does not open (69%) | 50% |  |
| 11 | [ ] | Firewatch (STEAM) | 71 | 118 | 60% (90d) | Does not open (89%) | 58% |  |
| 12 | [ ] | Stardew Valley (GOG) | 65 | 115 | 57% (90d) | Controller issues (45%) | 55% |  |
| 13 | [ ] | Gorilla Tag (STEAM) | 65 | 110 | 59% (90d) | Does not open (76%) | 23% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 14 | [ ] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 54 | 91 | 59% (90d) | Does not open (63%) | 58% |  |
| 15 | [ ] | Oxygen Not Included (STEAM) | 54 | 87 | 62% (90d) | Does not open (71%) | 50% |  |
| 16 | [ ] | Breathedge (STEAM) | 50 | 74 | 68% (90d) | Does not open (63%) | 39% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 17 | [ ] | Frostpunk (STEAM) | 48 | 76 | 63% (90d) | No graphics (78%) | 55% |  |
| 18 | [ ] | VALORANT (EPIC) | 47 | 74 | 64% (90d) | Does not open (84%) | 16% |  |
| 19 | [ ] | Skullgirls 2nd Encore (STEAM) | 45 | 75 | 60% (90d) | Does not open (93%) | 57% |  |
| 20 | [ ] | Plague Inc: Evolved (STEAM) | 45 | 69 | 65% (90d) | Does not open (65%) | 56% |  |
| 21 | [ ] | Fallout (GOG) | 43 | 63 | 68% (90d) | Does not open (71%) | 54% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 22 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 42 | 72 | 58% (90d) | Does not open (73%) | 52% |  |
| 23 | [ ] | Age of Empires II (2013) (STEAM) | 40 | 69 | 58% (90d) | Does not open (48%) | 54% |  |
| 24 | [ ] | Grim Dawn (GOG) | 38 | 63 | 60% (90d) | Does not open (65%) | 50% | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 25 | [ ] | XCOM 2 (STEAM) | 36 | 55 | 65% (90d) | Does not open (57%) | n/a |  |
| 26 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 35 | 60 | 58% (90d) | Does not open (92%) | 44% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 27 | [ ] | Sol Cesto (STEAM) | 34 | 53 | 64% (90d) | Does not open (71%) | 53% |  |
| 28 | [ ] | Hero Siege (STEAM) | 33 | 56 | 59% (90d) | Graphics glitches (52%) | 58% |  |
| 29 | [ ] | Soul's Remnant (STEAM) | 27 | 49 | 55% (90d) | Does not open (55%) | n/a |  |
| 30 | [ ] | Lucid Blocks (STEAM) | 27 | 46 | 59% (90d) | Does not open (83%) | n/a |  |
| 31 | [ ] | Opus Magnum (STEAM) | 25 | 39 | 64% (90d) | Does not open (72%) | n/a |  |
| 32 | [ ] | Strider (STEAM) | 25 | 38 | 66% (90d) | Does not open (100%) | 33% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 33 | [ ] | Goat Simulator (STEAM) | 24 | 43 | 56% (90d) | Does not open (58%) | 58% |  |
| 34 | [ ] | Crazy Taxi (STEAM) | 24 | 39 | 62% (90d) | Does not open (61%) | 44% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 35 | [ ] | Styx: Master of Shadows (EPIC) | 22 | 42 | 52% (90d) | Does not open (55%) | 27% |  |
| 36 | [ ] | Owlboy (STEAM) | 22 | 41 | 54% (90d) | Does not open (81%) | 50% |  |
| 37 | [ ] | Invisible, Inc. (STEAM) | 22 | 39 | 56% (90d) | Does not open (70%) | 56% |  |
| 38 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 22 | 33 | 67% (90d) | Does not open (80%) | n/a |  |
| 39 | [ ] | GOD EATER RESURRECTION (STEAM) | 21 | 32 | 66% (90d) | Does not open (53%) | 56% |  |
| 40 | [ ] | My Summer Car (STEAM) | 20 | 35 | 57% (90d) | Does not open (53%) | n/a |  |
| 41 | [ ] | Odallus: The Dark Call (STEAM) | 20 | 33 | 61% (90d) | No graphics (68%) | n/a | [#337](https://github.com/GameNative/gamenative-compat/issues/337) |
| 42 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 36 | 53% (90d) | Does not open (56%) | 44% |  |
| 43 | [ ] | No More Heroes (STEAM) | 19 | 36 | 53% (90d) | No graphics (67%) | n/a |  |
| 44 | [ ] | Another World: 20th Anniversary Edition (GOG) | 19 | 28 | 68% (90d) | Does not open (69%) | n/a |  |
| 45 | [ ] | Turnip Boy Robs a Bank (EPIC) | 19 | 28 | 68% (90d) | Does not open (65%) | 46% | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 46 | [ ] | Lost Castle 2 (STEAM) | 18 | 33 | 55% (90d) | Does not open (64%) | n/a |  |
| 47 | [ ] | Legend of Grimrock 2 (STEAM) | 18 | 26 | 69% (90d) | Does not open (80%) | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 48 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 17 | 33 | 52% (90d) | Does not open (88%) | 30% |  |
| 49 | [ ] | Guacamelee! Gold Edition (STEAM) | 17 | 28 | 61% (90d) | Does not open (93%) | n/a | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 50 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 17 | 27 | 63% (90d) | Does not open (80%) | n/a |  |
| 51 | [ ] | Assassin's Creed Odyssey (STEAM) | 16 | 24 | 67% (90d) | Does not open (75%) | n/a | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 52 | [ ] | Evoland (STEAM) | 15 | 29 | 52% (90d) | Controller issues (71%) | n/a |  |
| 53 | [ ] | Blaster Master Zero (STEAM) | 15 | 28 | 54% (90d) | Does not open (67%) | 36% |  |
| 54 | [ ] | Spilled! (STEAM) | 15 | 27 | 56% (90d) | Graphics glitches (67%) | n/a |  |
| 55 | [ ] | War of Dots (STEAM) | 15 | 25 | 60% (90d) | Does not open (71%) | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 56 | [ ] | Human Resource Machine (EPIC) | 15 | 23 | 65% (90d) | No graphics (67%) | n/a |  |
| 57 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 15 | 22 | 68% (90d) | Does not open (70%) | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 58 | [ ] | Aperture Desk Job (STEAM) | 14 | 28 | 50% (90d) | Does not open (67%) | n/a |  |
| 59 | [ ] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 14 | 28 | 50% (90d) | Does not open (100%) | 50% |  |
| 60 | [ ] | Far Cry® (GOG) | 14 | 27 | 52% (90d) | Does not open (31%) | n/a |  |
| 61 | [ ] | Alan Wake's American Nightmare (EPIC) | 14 | 26 | 54% (90d) | Does not open (92%) | 44% |  |
| 62 | [ ] | Katana ZERO (GOG) | 14 | 25 | 56% (90d) | Does not open (85%) | 29% |  |
| 63 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 14 | 25 | 56% (90d) | Does not open (92%) | 53% |  |
| 64 | [ ] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 14 | 24 | 58% (90d) | Does not open (93%) | 15% |  |
| 65 | [ ] | Warhammer 40,000: Boltgun (GOG) | 14 | 24 | 58% (90d) | Does not open (92%) | 36% |  |
| 66 | [ ] | Ys: Memories of Celceta (STEAM) | 14 | 23 | 61% (90d) | Does not open (40%) | 30% |  |
| 67 | [ ] | Blood Omen: Legacy of Kain (GOG) | 14 | 22 | 64% (90d) | Does not open (69%) | 39% |  |
| 68 | [ ] | Quake III Arena (STEAM) | 13 | 26 | 50% (90d) | Does not open (70%) | 9% |  |
| 69 | [ ] | A Plague Tale: Innocence (GOG) | 13 | 24 | 54% (90d) | Does not open (92%) | n/a |  |
| 70 | [ ] | UNDEFEATED (STEAM) | 13 | 24 | 54% (90d) | Does not open (80%) | n/a |  |
| 71 | [ ] | The Stanley Parable (STEAM) | 13 | 23 | 57% (90d) | Does not open (89%) | 38% |  |
| 72 | [ ] | Evenicle (STEAM) | 13 | 22 | 59% (90d) | Graphics glitches (77%) | n/a |  |
| 73 | [ ] | Foretales (EPIC) | 13 | 21 | 62% (90d) | Does not open (55%) | n/a | [#451](https://github.com/GameNative/gamenative-compat/issues/451) |
| 74 | [ ] | PAYDAY: The Heist (STEAM) | 13 | 21 | 62% (90d) | Does not open (67%) | n/a |  |
| 75 | [ ] | Trials Survivors (STEAM) | 13 | 21 | 62% (90d) | Does not open (67%) | n/a |  |
| 76 | [ ] | XIII (GOG) | 13 | 21 | 62% (90d) | Does not open (70%) | n/a |  |
| 77 | [ ] | Buck Up And Drive! (STEAM) | 13 | 20 | 65% (90d) | Does not open (67%) | n/a |  |
| 78 | [ ] | Look Outside (GOG) | 12 | 24 | 50% (90d) | Does not open (100%) | n/a |  |
| 79 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 12 | 23 | 52% (90d) | Does not open (73%) | n/a |  |
| 80 | [ ] | Crying Suns (EPIC) | 12 | 23 | 52% (90d) | No graphics (63%) | n/a |  |
| 81 | [ ] | Shift At Midnight (STEAM) | 12 | 21 | 57% (90d) | Does not open (80%) | n/a |  |
| 82 | [ ] | The Excavation of Hob's Barrow (STEAM) | 12 | 21 | 57% (90d) | Controller issues (82%) | n/a |  |
| 83 | [ ] | Breathedge (EPIC) | 12 | 20 | 60% (90d) | Does not open (100%) | 50% |  |
| 84 | [ ] | Dex (GOG) | 12 | 20 | 60% (90d) | Does not open (80%) | n/a |  |
| 85 | [ ] | Drop Duchy (EPIC) | 12 | 20 | 60% (90d) | Does not open (100%) | n/a |  |
| 86 | [ ] | DYNASTY WARRIORS: ORIGINS (STEAM) | 11 | 21 | 52% (90d) | Does not open (55%) | n/a |  |
| 87 | [ ] | FATE (STEAM) | 11 | 21 | 52% (90d) | No graphics (50%) | n/a |  |
| 88 | [ ] | Grounded (STEAM) | 11 | 20 | 55% (90d) | No graphics (50%) | n/a |  |
| 89 | [ ] | Asterigos: Curse of the Stars (STEAM) | 10 | 20 | 50% (90d) | Does not open (43%) | n/a |  |
| 90 | [ ] | Thief™ 3: Deadly Shadows (GOG) | 10 | 20 | 50% (90d) | Does not open (70%) | n/a |  |

## Works, but the first launch usually fails (365)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 1375 | 1739 | 73% (1.3.0) | Does not open (83%) | 77% |  |
| 2 | [ ] | Grim Dawn (STEAM) | 603 | 652 | 67% (1.3.0) | Does not open (76%) | 66% |  |
| 3 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 583 | 740 | 78% (1.3.0) | Does not open (65%) | 91% |  |
| 4 | [ ] | Terraria (STEAM) | 490 | 767 | 57% (1.3.0) | No graphics (50%) | 76% |  |
| 5 | [ ] | KINGDOM HEARTS -HD 1.5+2.5 ReMIX- (STEAM) | 458 | 926 | 56% (1.3.0) | Does not open (80%) | 94% |  |
| 6 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 377 | 561 | 69% (1.3.0) | Does not open (55%) | 87% |  |
| 7 | [ ] | No Man's Sky (STEAM) | 360 | 637 | 50% (1.3.0) | Controller issues (63%) | 88% |  |
| 8 | [ ] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 276 | 317 | 87% (90d) | Does not open (85%) | 64% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 9 | [ ] | Cyberpunk 2077 (STEAM) | 248 | 428 | 53% (1.3.0) | Does not open (66%) | 77% |  |
| 10 | [ ] | Welcome to Elderfield (STEAM) | 231 | 276 | 57% (1.3.0) | Does not open (72%) | 80% |  |
| 11 | [ ] | BeamNG.drive (STEAM) | 229 | 283 | 87% (1.3.0) | Does not open (84%) | 92% |  |
| 12 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 224 | 315 | 71% (90d) | Does not open (61%) | 86% |  |
| 13 | [ ] | Grand Theft Auto V Legacy (STEAM) | 212 | 267 | 69% (1.3.0) | Does not open (87%) | 79% |  |
| 14 | [ ] | OMORI (STEAM) | 212 | 255 | 83% (90d) | Does not open (64%) | 77% |  |
| 15 | [ ] | Devil May Cry HD Collection (STEAM) | 200 | 281 | 80% (1.3.0) | Does not open (87%) | 73% |  |
| 16 | [ ] | ELDEN RING (STEAM) | 199 | 293 | 71% (1.3.0) | Does not open (85%) | 70% |  |
| 17 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 192 | 357 | 64% (1.3.0) | Does not open (58%) | 81% |  |
| 18 | [ ] | DREDGE (EPIC) | 182 | 232 | 63% (1.3.0) | Does not open (67%) | 88% |  |
| 19 | [ ] | Resident Evil 2 (STEAM) | 165 | 325 | 53% (1.3.0) | Does not open (77%) | 80% |  |
| 20 | [ ] | Mirror's Edge (STEAM) | 150 | 203 | 74% (90d) | Does not open (91%) | 79% |  |
| 21 | [ ] | Noita (STEAM) | 148 | 222 | 56% (1.3.0) | Does not open (54%) | 78% |  |
| 22 | [ ] | Far Cry® 3 (STEAM) | 142 | 161 | 88% (90d) | Does not open (84%) | 64% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 23 | [ ] | Team Fortress 2 (STEAM) | 141 | 231 | 68% (1.3.0) | Does not open (68%) | 80% |  |
| 24 | [ ] | Borderlands 2 (EPIC) | 140 | 162 | 85% (1.3.0) | Does not open (83%) | 63% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 25 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 138 | 159 | 87% (90d) | Does not open (85%) | 80% |  |
| 26 | [ ] | Look Outside (STEAM) | 132 | 302 | 52% (1.3.0) | Controller issues (62%) | 90% |  |
| 27 | [ ] | Castlevania Advance Collection (STEAM) | 132 | 203 | 71% (1.3.0) | Controller issues (94%) | 97% |  |
| 28 | [ ] | Devil May Cry 5 (STEAM) | 124 | 194 | 65% (1.3.0) | Does not open (80%) | 67% |  |
| 29 | [ ] | Fallout: New Vegas (EPIC) | 122 | 148 | 82% (90d) | Does not open (58%) | 92% |  |
| 30 | [ ] | Minecraft Dungeons II (STEAM) | 122 | 139 | 88% (90d) | Does not open (83%) | 66% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 31 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 120 | 148 | 70% (1.3.0) | Does not open (71%) | 61% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 32 | [ ] | Cave Story+ (STEAM) | 120 | 132 | 91% (90d) | Does not open (65%) | 94% |  |
| 33 | [ ] | Castlevania Dominus Collection (STEAM) | 119 | 175 | 74% (1.3.0) | Controller issues (92%) | 98% |  |
| 34 | [ ] | The Witcher: Enhanced Edition (STEAM) | 118 | 136 | 87% (90d) | Does not open (59%) | 62% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 35 | [ ] | Touhou Koumakyou: New Classic - the Embodiment of Scarlet Devil (STEAM) | 116 | 177 | 66% (90d) | Does not open (78%) | 80% |  |
| 36 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 115 | 151 | 76% (90d) | Does not open (86%) | 81% |  |
| 37 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 110 | 154 | 80% (1.3.0) | Does not open (74%) | 64% |  |
| 38 | [ ] | Moonstone Island (STEAM) | 105 | 138 | 76% (90d) | Controller issues (57%) | 91% |  |
| 39 | [ ] | Aniimo (STEAM) | 101 | 139 | 73% (90d) | Does not open (76%) | 92% |  |
| 40 | [ ] | FINAL FANTASY VIII - REMASTERED (STEAM) | 99 | 155 | 64% (90d) | Does not open (89%) | 63% |  |
| 41 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 96 | 129 | 74% (90d) | Controller issues (86%) | 100% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 42 | [ ] | Cry of Fear (STEAM) | 93 | 178 | 73% (1.3.0) | Does not open (54%) | 92% |  |
| 43 | [ ] | Happy Wheels (STEAM) | 93 | 113 | 82% (90d) | No graphics (53%) | 79% |  |
| 44 | [ ] | STEINS;GATE (STEAM) | 92 | 124 | 74% (90d) | Does not open (90%) | 86% |  |
| 45 | [ ] | BioShock Remastered (EPIC) | 91 | 164 | 55% (90d) | Does not open (56%) | 85% |  |
| 46 | [ ] | Sovereign Tower (STEAM) | 90 | 143 | 63% (90d) | Does not open (82%) | 88% |  |
| 47 | [ ] | Fallout: New Vegas PCR (STEAM) | 90 | 124 | 73% (90d) | Does not open (90%) | 75% |  |
| 48 | [ ] | Vital Shell (STEAM) | 88 | 131 | 67% (90d) | Does not open (53%) | 85% |  |
| 49 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 86 | 128 | 67% (90d) | Does not open (79%) | 74% |  |
| 50 | [ ] | Hogwarts Legacy (STEAM) | 83 | 140 | 54% (1.3.0) | Does not open (61%) | 67% |  |
| 51 | [ ] | The Sims™ 4 (STEAM) | 80 | 97 | 82% (90d) | Does not open (89%) | 69% |  |
| 52 | [ ] | Detroit: Become Human (STEAM) | 79 | 82 | 96% (90d) | Does not open (72%) | 68% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 53 | [ ] | Need for Speed: Hot Pursuit (STEAM) | 78 | 107 | 73% (90d) | Does not open (75%) | 76% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 54 | [ ] | Resident Evil 4 (2005) (STEAM) | 77 | 150 | 51% (90d) | Does not open (75%) | 73% |  |
| 55 | [ ] | Mega Man Zero/ZX Legacy Collection (STEAM) | 76 | 103 | 74% (90d) | Does not open (87%) | 84% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 56 | [ ] | Alabaster Dawn (STEAM) | 75 | 130 | 58% (90d) | Controller issues (49%) | 93% |  |
| 57 | [ ] | Sid Meier's Civilization VI (STEAM) | 75 | 129 | 57% (1.3.0) | Does not open (70%) | 92% |  |
| 58 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 73 | 122 | 60% (90d) | Controller issues (60%) | 93% |  |
| 59 | [ ] | Call of Juarez Gunslinger (STEAM) | 73 | 88 | 83% (90d) | Does not open (91%) | 71% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 60 | [ ] | Darksiders (STEAM) | 72 | 87 | 83% (90d) | Does not open (69%) | 92% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 61 | [ ] | Fallout 3: Game of the Year Edition (GOG) | 71 | 163 | 52% (1.3.0) | Does not open (60%) | 70% |  |
| 62 | [ ] | Ballionaire (STEAM) | 71 | 108 | 66% (90d) | Does not open (77%) | 97% |  |
| 63 | [ ] | Fable - The Lost Chapters (STEAM) | 70 | 109 | 52% (1.3.0) | Graphics glitches (49%) | 79% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 64 | [ ] | Dota 2 (STEAM) | 70 | 107 | 57% (1.3.0) | Does not open (78%) | 74% |  |
| 65 | [ ] | Antivirus Survivors 2003 Professional (STEAM) | 70 | 103 | 68% (90d) | Does not open (61%) | 92% |  |
| 66 | [ ] | Dungeons & Degenerate Gamblers (STEAM) | 70 | 94 | 74% (90d) | Does not open (90%) | 98% |  |
| 67 | [ ] | Gunfire Reborn (STEAM) | 70 | 77 | 91% (90d) | Does not open (82%) | 92% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 68 | [ ] | POSTAL 2 (STEAM) | 69 | 120 | 58% (90d) | Does not open (66%) | 66% |  |
| 69 | [ ] | Fallout (STEAM) | 69 | 108 | 64% (90d) | Does not open (69%) | 72% |  |
| 70 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 69 | 84 | 95% (1.3.0) | Does not open (91%) | 97% |  |
| 71 | [ ] | American Truck Simulator (STEAM) | 68 | 107 | 83% (1.3.0) | Does not open (76%) | 75% |  |
| 72 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 68 | 90 | 76% (90d) | Does not open (48%) | 70% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 73 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 67 | 122 | 55% (90d) | Does not open (64%) | 64% |  |
| 74 | [ ] | Castlevania Anniversary Collection (EPIC) | 66 | 131 | 50% (90d) | Does not open (68%) | 96% |  |
| 75 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 66 | 104 | 63% (90d) | Does not open (75%) | 69% |  |
| 76 | [ ] | Borderlands: The Pre-Sequel (STEAM) | 66 | 92 | 72% (90d) | Does not open (78%) | 68% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 77 | [ ] | Disgaea 5 Complete (STEAM) | 66 | 80 | 83% (90d) | Does not open (79%) | 97% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 78 | [ ] | Poppy Playtime (STEAM) | 65 | 111 | 59% (90d) | Does not open (67%) | 79% |  |
| 79 | [ ] | MIO: Memories in Orbit (STEAM) | 64 | 122 | 67% (1.3.0) | Graphics glitches (52%) | 96% |  |
| 80 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 64 | 86 | 74% (90d) | Does not open (51%) | 91% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 81 | [ ] | A Plague Tale: Innocence (STEAM) | 64 | 67 | 96% (90d) | Does not open (85%) | 75% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 82 | [ ] | Sonic Lost World (STEAM) | 63 | 102 | 62% (90d) | No graphics (58%) | 90% |  |
| 83 | [ ] | Big Walk (STEAM) | 63 | 96 | 66% (90d) | Does not open (68%) | 84% |  |
| 84 | [ ] | Ace Attorney Investigations Collection (STEAM) | 62 | 94 | 66% (90d) | Does not open (97%) | 91% |  |
| 85 | [ ] | The Binding of Isaac (STEAM) | 61 | 141 | 61% (1.3.0) | Controller issues (91%) | 94% |  |
| 86 | [ ] | eFootball™ (STEAM) | 60 | 91 | 66% (90d) | Does not open (57%) | 75% |  |
| 87 | [ ] | TBH: Task Bar Hero (STEAM) | 60 | 90 | 67% (90d) | Does not open (70%) | 96% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 88 | [ ] | Borderlands 3 (STEAM) | 60 | 77 | 78% (90d) | Does not open (91%) | 95% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 89 | [ ] | Cyberpunk 2077 (GOG) | 60 | 74 | 81% (90d) | Does not open (80%) | 73% |  |
| 90 | [ ] | Sonic Generations (STEAM) | 60 | 70 | 86% (90d) | Does not open (73%) | 66% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 91 | [ ] | Sonic Adventure DX (STEAM) | 59 | 96 | 61% (90d) | Does not open (85%) | 71% |  |
| 92 | [ ] | Call of Duty: World at War (STEAM) | 59 | 82 | 72% (90d) | Does not open (43%) | 62% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 93 | [ ] | Red Dead Redemption 2 (STEAM) | 59 | 78 | 63% (1.3.0) | Does not open (98%) | 84% |  |
| 94 | [ ] | Starbound (STEAM) | 58 | 85 | 68% (90d) | Does not open (69%) | 71% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 95 | [ ] | Dead by Daylight (STEAM) | 58 | 63 | 92% (90d) | Does not open (83%) | 80% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 96 | [ ] | Prey (STEAM) | 56 | 94 | 60% (90d) | Does not open (63%) | 88% |  |
| 97 | [ ] | Devil May Cry 4 Special Edition (STEAM) | 55 | 94 | 59% (90d) | Does not open (86%) | 77% |  |
| 98 | [ ] | The Secret of Monkey Island: Special Edition (STEAM) | 55 | 87 | 63% (90d) | Does not open (90%) | 69% |  |
| 99 | [ ] | Path of Exile (STEAM) | 55 | 64 | 86% (90d) | Does not open (89%) | 83% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 100 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 55 | 63 | 87% (90d) | Does not open (78%) | 79% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 101 | [ ] | A Plague Tale: Innocence (EPIC) | 54 | 91 | 59% (90d) | Does not open (71%) | 87% |  |
| 102 | [ ] | The Bazaar (STEAM) | 54 | 87 | 62% (90d) | Does not open (73%) | 81% |  |
| 103 | [ ] | MudRunner (STEAM) | 53 | 104 | 51% (90d) | Does not open (73%) | 65% |  |
| 104 | [ ] | Mini Motorways (STEAM) | 53 | 95 | 56% (90d) | Does not open (74%) | 62% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 105 | [ ] | Teardown (STEAM) | 52 | 93 | 56% (90d) | Controller issues (51%) | 76% |  |
| 106 | [ ] | Until Then (STEAM) | 52 | 93 | 56% (90d) | Does not open (73%) | 97% |  |
| 107 | [ ] | Resident Evil 6 (STEAM) | 51 | 127 | 76% (1.3.0) | Does not open (55%) | 90% |  |
| 108 | [ ] | 7 Days to Die (STEAM) | 51 | 108 | 61% (1.3.0) | Does not open (74%) | 73% |  |
| 109 | [ ] | Street Fighter™ 6 (STEAM) | 51 | 75 | 68% (90d) | Does not open (89%) | 80% |  |
| 110 | [ ] | Guildrun Demo (STEAM) | 51 | 74 | 69% (90d) | No graphics (65%) | 72% |  |
| 111 | [ ] | Sheepy: A Short Adventure (STEAM) | 51 | 61 | 84% (90d) | Does not open (54%) | 81% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 112 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 51 | 55 | 93% (90d) | Does not open (85%) | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 113 | [ ] | Slay the Princess — The Pristine Cut (STEAM) | 50 | 87 | 57% (90d) | No graphics (61%) | 70% |  |
| 114 | [ ] | Dead Space (STEAM) | 50 | 63 | 79% (90d) | Does not open (54%) | 71% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 115 | [ ] | Sleeping Dogs™ (STEAM) | 50 | 57 | 88% (90d) | Does not open (83%) | 80% | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 116 | [ ] | Okami HD (STEAM) | 49 | 90 | 54% (90d) | Controller issues (60%) | 87% |  |
| 117 | [ ] | Rivals of Aether II (STEAM) | 49 | 74 | 66% (90d) | Does not open (56%) | 72% |  |
| 118 | [ ] | MapleStory (STEAM) | 49 | 51 | 90% (14d) | Does not open (78%) | 75% |  |
| 119 | [ ] | FINAL FANTASY VII (2013) (STEAM) | 48 | 69 | 70% (90d) | Does not open (85%) | 81% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 120 | [ ] | Last Epoch (STEAM) | 48 | 67 | 78% (1.3.0) | Does not open (77%) | 100% |  |
| 121 | [ ] | Digimon World: Next Order (STEAM) | 47 | 87 | 54% (90d) | Controller issues (80%) | 94% |  |
| 122 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 75 | 63% (90d) | Controller issues (57%) | 94% |  |
| 123 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 47 | 68 | 69% (90d) | Does not open (82%) | 82% |  |
| 124 | [ ] | Tomb Raider: Anniversary (STEAM) | 46 | 66 | 70% (90d) | Does not open (95%) | 70% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 125 | [ ] | Crypt of the NecroDancer (STEAM) | 45 | 151 | 50% (1.3.0) | Does not open (53%) | 85% |  |
| 126 | [ ] | Darkest Dungeon® (EPIC) | 45 | 83 | 54% (1.3.0) | Does not open (62%) | 62% |  |
| 127 | [ ] | Abiotic Factor (STEAM) | 45 | 80 | 56% (90d) | Does not open (74%) | 68% |  |
| 128 | [ ] | PROTOTYPE 2 (STEAM) | 44 | 88 | 50% (90d) | Does not open (74%) | 79% |  |
| 129 | [ ] | Life is Strange™ (STEAM) | 44 | 85 | 52% (90d) | Does not open (74%) | 83% |  |
| 130 | [ ] | Grand Theft Auto V (EPIC) | 44 | 50 | 88% (90d) | Does not open (88%) | 82% |  |
| 131 | [ ] | Salt and Sanctuary (STEAM) | 43 | 81 | 53% (90d) | Does not open (76%) | 82% |  |
| 132 | [ ] | Moonlighter (EPIC) | 43 | 47 | 91% (90d) | No graphics (79%) | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 133 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 42 | 77 | 55% (90d) | Controller issues (55%) | 87% |  |
| 134 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 42 | 69 | 61% (90d) | Does not open (64%) | 80% |  |
| 135 | [ ] | Resident Evil 7 Biohazard (STEAM) | 42 | 67 | 63% (90d) | Does not open (76%) | 85% |  |
| 136 | [ ] | Deadlock (STEAM) | 42 | 66 | 64% (90d) | Does not open (52%) | 94% |  |
| 137 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 42 | 66 | 64% (90d) | Does not open (50%) | 67% |  |
| 138 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 41 | 76 | 54% (90d) | No graphics (81%) | 94% |  |
| 139 | [ ] | Amnesia: The Dark Descent (STEAM) | 41 | 76 | 54% (90d) | Does not open (85%) | 76% |  |
| 140 | [ ] | Sonic Origins (STEAM) | 41 | 70 | 59% (90d) | Does not open (70%) | 84% |  |
| 141 | [ ] | Tales of ARISE (STEAM) | 41 | 69 | 59% (90d) | Controller issues (76%) | 92% |  |
| 142 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 41 | 62 | 66% (90d) | Does not open (75%) | 74% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 143 | [ ] | Capcom Arcade Stadium (STEAM) | 41 | 51 | 80% (90d) | Does not open (84%) | 75% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 144 | [ ] | Forza Horizon 4 (STEAM) | 40 | 56 | 71% (90d) | Does not open (50%) | 86% |  |
| 145 | [ ] | Aggelos (STEAM) | 40 | 54 | 74% (90d) | No graphics (79%) | 94% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 146 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 39 | 74 | 53% (90d) | Controller issues (44%) | 90% |  |
| 147 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 39 | 41 | 95% (90d) | Does not open (61%) | 82% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 148 | [ ] | Monster Hunter Wilds (STEAM) | 39 | 40 | 98% (90d) | Does not open (63%) | 72% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 149 | [ ] | CrossCode (GOG) | 38 | 42 | 90% (90d) | Does not open (76%) | 72% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 150 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 67 | 55% (90d) | Does not open (68%) | 86% |  |
| 151 | [ ] | Romestead (STEAM) | 37 | 48 | 77% (90d) | Does not open (67%) | 81% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 152 | [ ] | SurrounDead (STEAM) | 36 | 68 | 53% (90d) | Controller issues (59%) | 94% |  |
| 153 | [ ] | Rocket League (STEAM) | 36 | 55 | 65% (90d) | Does not open (72%) | 68% |  |
| 154 | [ ] | Capcom Fighting Collection 2 (STEAM) | 36 | 52 | 69% (90d) | Does not open (80%) | 87% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 155 | [ ] | Street Fighter 30th Anniversary Collection (STEAM) | 35 | 67 | 52% (90d) | Does not open (100%) | 65% |  |
| 156 | [ ] | Hearts of Iron IV (STEAM) | 35 | 59 | 59% (90d) | Does not open (73%) | 60% |  |
| 157 | [ ] | Earthion (STEAM) | 35 | 56 | 63% (90d) | Controller issues (88%) | 100% |  |
| 158 | [ ] | Battle Brothers (STEAM) | 35 | 52 | 67% (90d) | Does not open (77%) | 62% |  |
| 159 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 35 | 49 | 71% (90d) | Controller issues (88%) | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 160 | [ ] | SnowRunner (STEAM) | 35 | 47 | 74% (90d) | Does not open (96%) | 82% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 161 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 35 | 41 | 85% (90d) | Does not open (65%) | 74% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 162 | [ ] | Deponia (STEAM) | 34 | 63 | 54% (90d) | Does not open (50%) | 60% |  |
| 163 | [ ] | Ultimate Custom Night (STEAM) | 34 | 46 | 74% (90d) | No graphics (66%) | 76% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 164 | [ ] | Lost Planet: Extreme Condition (STEAM) | 34 | 41 | 83% (90d) | Does not open (77%) | 60% | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 165 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 34 | 41 | 83% (90d) | Does not open (70%) | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 166 | [ ] | Fallout 3 (STEAM) | 33 | 66 | 50% (90d) | Does not open (56%) | 88% |  |
| 167 | [ ] | Resident Evil Village (STEAM) | 33 | 55 | 60% (90d) | Does not open (70%) | 87% |  |
| 168 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 33 | 54 | 61% (90d) | Controller issues (61%) | 65% |  |
| 169 | [ ] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 53 | 62% (90d) | Controller issues (84%) | 83% |  |
| 170 | [ ] | Secrets of Grindea (STEAM) | 33 | 51 | 65% (90d) | Does not open (54%) | 81% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 171 | [ ] | Counter-Strike:Global Offensive (STEAM) | 33 | 50 | 66% (90d) | Does not open (79%) | 72% |  |
| 172 | [ ] | Supermarket Together (STEAM) | 33 | 48 | 69% (90d) | Does not open (72%) | 82% |  |
| 173 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 33 | 43 | 77% (90d) | Controller issues (63%) | 89% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 174 | [ ] | Russian Fishing 4 (STEAM) | 33 | 38 | 87% (90d) | Does not open (68%) | 67% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 175 | [ ] | Need for Speed™ (STEAM) | 33 | 37 | 89% (90d) | Does not open (70%) | 63% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 176 | [ ] | Hotline Miami (GOG) | 33 | 36 | 92% (90d) | Does not open (94%) | 64% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 177 | [ ] | COCOON (STEAM) | 32 | 62 | 52% (90d) | Directx error (50%) | 88% |  |
| 178 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 32 | 62 | 52% (90d) | Does not open (69%) | 88% |  |
| 179 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 32 | 56 | 57% (90d) | Does not open (48%) | 63% |  |
| 180 | [ ] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 32 | 51 | 63% (90d) | Does not open (43%) | 71% |  |
| 181 | [ ] | Nioh: Complete Edition (STEAM) | 32 | 43 | 74% (90d) | Does not open (56%) | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 182 | [ ] | Super Animal Royale (STEAM) | 32 | 41 | 78% (90d) | Does not open (65%) | 72% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 183 | [ ] | Path of Exile 2 (STEAM) | 32 | 37 | 86% (90d) | Does not open (96%) | 85% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 184 | [ ] | Red Dead Redemption (STEAM) | 32 | 36 | 89% (90d) | Does not open (95%) | 87% |  |
| 185 | [ ] | Torchlight II (STEAM) | 31 | 62 | 50% (90d) | Does not open (54%) | 94% |  |
| 186 | [ ] | Library Of Ruina (STEAM) | 31 | 60 | 52% (90d) | Does not open (67%) | 84% |  |
| 187 | [ ] | Max Payne (STEAM) | 31 | 57 | 54% (90d) | No graphics (42%) | 95% |  |
| 188 | [ ] | LEGO® Harry Potter™ Collection (STEAM) | 31 | 56 | 55% (90d) | Does not open (85%) | 85% |  |
| 189 | [ ] | Deus Ex™ GOTY Edition (GOG) | 31 | 47 | 66% (90d) | No graphics (39%) | 84% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 190 | [ ] | Tower and Sword of Succubus (STEAM) | 31 | 46 | 67% (90d) | No graphics (81%) | 100% |  |
| 191 | [ ] | Moonlight Peaks (STEAM) | 31 | 45 | 69% (90d) | Does not open (65%) | 100% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 192 | [ ] | Grand Theft Auto III (STEAM) | 31 | 39 | 79% (90d) | Does not open (52%) | 88% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 193 | [ ] | Capcom Fighting Collection (STEAM) | 31 | 35 | 89% (90d) | Does not open (84%) | 71% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 194 | [ ] | Cave Story+ (EPIC) | 29 | 55 | 53% (90d) | Does not open (48%) | 85% |  |
| 195 | [ ] | Aethermancer (STEAM) | 29 | 49 | 59% (90d) | Does not open (78%) | 76% |  |
| 196 | [ ] | Binary Domain (STEAM) | 29 | 45 | 64% (90d) | Does not open (91%) | 79% |  |
| 197 | [ ] | Yakuza: Like a Dragon (STEAM) | 29 | 44 | 66% (90d) | Does not open (68%) | 76% |  |
| 198 | [ ] | Dead Rising 2 (STEAM) | 29 | 41 | 85% (14d) | Does not open (88%) | 66% |  |
| 199 | [ ] | Stellar Blade™ (STEAM) | 29 | 37 | 78% (90d) | Does not open (50%) | 87% |  |
| 200 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 29 | 29 | 100% (90d) | Does not open (91%) | 62% | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 201 | [ ] | Tails of Iron (STEAM) | 28 | 56 | 50% (90d) | Does not open (47%) | 96% |  |
| 202 | [ ] | Mortal Kombat X (STEAM) | 28 | 53 | 53% (90d) | Does not open (52%) | 85% |  |
| 203 | [ ] | Heavy Rain (STEAM) | 28 | 49 | 57% (90d) | Controller issues (64%) | 85% |  |
| 204 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 28 | 48 | 58% (90d) | Controller issues (48%) | 94% |  |
| 205 | [ ] | Zero Escape: The Nonary Games (STEAM) | 28 | 46 | 61% (90d) | Does not open (88%) | 62% |  |
| 206 | [ ] | Crab Game (STEAM) | 28 | 37 | 76% (90d) | Does not open (58%) | 74% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 207 | [ ] | CRUEL (STEAM) | 28 | 34 | 82% (90d) | Does not open (89%) | 70% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 208 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 27 | 51 | 53% (90d) | Does not open (57%) | 67% |  |
| 209 | [ ] | Akane (STEAM) | 27 | 46 | 59% (90d) | Controller issues (71%) | 100% |  |
| 210 | [ ] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 27 | 39 | 69% (90d) | Does not open (82%) | 88% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 211 | [ ] | Goose Goose Duck (STEAM) | 27 | 34 | 79% (90d) | Does not open (70%) | 77% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 212 | [ ] | Tales of Zestiria (STEAM) | 27 | 33 | 82% (90d) | Does not open (81%) | 69% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 213 | [ ] | Dead Island Riptide Definitive Edition (STEAM) | 26 | 51 | 51% (90d) | Does not open (55%) | 79% |  |
| 214 | [ ] | Wizard of Legend (EPIC) | 26 | 44 | 59% (90d) | Does not open (80%) | 76% |  |
| 215 | [ ] | Prince of Persia (GOG) | 26 | 42 | 62% (90d) | Does not open (95%) | 80% |  |
| 216 | [ ] | Limbus Company (STEAM) | 26 | 40 | 65% (90d) | Does not open (86%) | 79% |  |
| 217 | [ ] | SWORN (STEAM) | 26 | 40 | 65% (90d) | Does not open (53%) | 100% |  |
| 218 | [ ] | Gothic II: Gold Classic (STEAM) | 26 | 39 | 67% (90d) | Does not open (59%) | 79% |  |
| 219 | [ ] | Ratatan (STEAM) | 26 | 39 | 67% (90d) | Does not open (47%) | 100% |  |
| 220 | [ ] | Palia (STEAM) | 26 | 36 | 72% (90d) | Does not open (65%) | 71% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 221 | [ ] | CarX Drift Racing Online (STEAM) | 25 | 50 | 50% (90d) | Does not open (50%) | 70% |  |
| 222 | [ ] | Being a DIK (STEAM) | 25 | 43 | 58% (90d) | Does not open (78%) | 90% |  |
| 223 | [ ] | Counter-Strike: Condition Zero (STEAM) | 25 | 43 | 58% (90d) | Does not open (53%) | 64% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 224 | [ ] | Digimon Survive (STEAM) | 25 | 42 | 60% (90d) | Controller issues (71%) | 96% |  |
| 225 | [ ] | Cat Mail Co. (STEAM) | 25 | 40 | 63% (90d) | Does not open (90%) | 87% |  |
| 226 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 32 | 78% (90d) | Does not open (87%) | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 227 | [ ] | Resident Evil (GOG) | 25 | 27 | 93% (90d) | Does not open (95%) | 72% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 228 | [ ] | Resident Evil Revelations 2 (STEAM) | 24 | 46 | 52% (90d) | Does not open (40%) | 89% |  |
| 229 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 24 | 38 | 63% (90d) | Does not open (100%) | 89% |  |
| 230 | [ ] | Timberborn (STEAM) | 24 | 36 | 67% (90d) | No graphics (64%) | 83% |  |
| 231 | [ ] | Bongo Cat (STEAM) | 24 | 34 | 71% (90d) | Does not open (63%) | 79% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 232 | [ ] | Beyond: Two Souls (STEAM) | 24 | 32 | 75% (90d) | Does not open (48%) | 73% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 233 | [ ] | Need for Speed™ Unbound (STEAM) | 24 | 32 | 75% (90d) | Does not open (80%) | 75% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 234 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 23 | 44 | 52% (90d) | Controller issues (63%) | 94% |  |
| 235 | [ ] | Changed (STEAM) | 23 | 37 | 62% (90d) | Does not open (63%) | 83% |  |
| 236 | [ ] | Return to Monkey Island (STEAM) | 23 | 37 | 62% (90d) | No graphics (59%) | 93% |  |
| 237 | [ ] | Party Animals (STEAM) | 23 | 32 | 72% (90d) | Does not open (75%) | 83% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 238 | [ ] | FINAL FANTASY XIV Online (STEAM) | 23 | 30 | 77% (90d) | Does not open (100%) | 95% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 239 | [ ] | Jade Empire: Special Edition (GOG) | 23 | 29 | 79% (90d) | Does not open (50%) | 78% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 240 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 23 | 29 | 79% (90d) | Does not open (40%) | 62% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 241 | [ ] | Mafia: Definitive Edition (STEAM) | 22 | 41 | 54% (90d) | Does not open (81%) | 90% |  |
| 242 | [ ] | Football Manager 2024 (EPIC) | 22 | 40 | 55% (90d) | Does not open (86%) | 89% |  |
| 243 | [ ] | Overlord (STEAM) | 22 | 40 | 55% (90d) | Does not open (71%) | 62% |  |
| 244 | [ ] | This War of Mine (STEAM) | 22 | 39 | 56% (90d) | No graphics (56%) | 74% |  |
| 245 | [ ] | Lobotomy Corporation (STEAM) | 22 | 38 | 58% (90d) | No graphics (63%) | 100% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 246 | [ ] | Life is Strange Remastered (STEAM) | 22 | 34 | 65% (90d) | Does not open (73%) | 94% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 247 | [ ] | Nex Machina (STEAM) | 22 | 30 | 73% (90d) | Does not open (53%) | 88% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 248 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 59 | 82% (1.3.0) | Does not open (79%) | 100% |  |
| 249 | [ ] | Gambonanza (STEAM) | 21 | 40 | 53% (90d) | Does not open (60%) | 91% |  |
| 250 | [ ] | Unturned (STEAM) | 21 | 40 | 53% (90d) | Does not open (63%) | 83% |  |
| 251 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 21 | 39 | 54% (90d) | Does not open (53%) | 67% |  |
| 252 | [ ] | Pinball FX Classic (STEAM) | 21 | 39 | 54% (90d) | Does not open (75%) | 94% |  |
| 253 | [ ] | One-armed robber (STEAM) | 21 | 38 | 55% (90d) | Controller issues (61%) | 76% |  |
| 254 | [ ] | Tiny Glade (STEAM) | 21 | 36 | 58% (90d) | Does not open (42%) | 77% |  |
| 255 | [ ] | Command & Conquer™ Red Alert™ 3 (STEAM) | 21 | 26 | 81% (90d) | Does not open (50%) | 60% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 256 | [ ] | Crimzon Clover World EXplosion (STEAM) | 20 | 39 | 51% (90d) | Does not open (47%) | 100% |  |
| 257 | [ ] | TCG Card Shop Simulator (STEAM) | 20 | 39 | 51% (90d) | Does not open (59%) | 84% |  |
| 258 | [ ] | Paper Lily - Chapter 1 (STEAM) | 20 | 38 | 53% (90d) | Does not open (72%) | 91% |  |
| 259 | [ ] | Control Ultimate Edition (GOG) | 20 | 37 | 54% (90d) | Does not open (81%) | 97% |  |
| 260 | [ ] | Killing Floor (STEAM) | 20 | 36 | 56% (90d) | Controller issues (100%) | 86% |  |
| 261 | [ ] | Trailmakers (STEAM) | 20 | 36 | 56% (90d) | Does not open (44%) | 91% |  |
| 262 | [ ] | Tabletop Simulator (STEAM) | 20 | 33 | 61% (90d) | Does not open (50%) | 66% |  |
| 263 | [ ] | Worms W.M.D (STEAM) | 20 | 33 | 61% (90d) | Does not open (59%) | 86% |  |
| 264 | [ ] | Hitman: Absolution (GOG) | 20 | 31 | 65% (90d) | Does not open (83%) | 93% |  |
| 265 | [ ] | DOOM 3: BFG Edition (GOG) | 20 | 28 | 71% (90d) | No graphics (65%) | 76% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 266 | [ ] | Torchlight II (EPIC) | 20 | 27 | 74% (90d) | Does not open (83%) | 100% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 267 | [ ] | BAJA: Edge of Control HD (STEAM) | 20 | 26 | 77% (90d) | Does not open (100%) | 90% | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 268 | [ ] | Dead Island (STEAM) | 20 | 26 | 77% (90d) | Does not open (69%) | 71% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 269 | [ ] | War Thunder (STEAM) | 20 | 26 | 77% (90d) | Does not open (53%) | 80% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 270 | [ ] | Backpack Battles (STEAM) | 19 | 36 | 53% (90d) | Does not open (63%) | 96% |  |
| 271 | [ ] | Breath of Fire IV (GOG) | 19 | 34 | 56% (90d) | Does not open (72%) | 62% |  |
| 272 | [ ] | Stick It to the Stickman (STEAM) | 19 | 34 | 56% (90d) | Does not open (88%) | 76% |  |
| 273 | [ ] | GRIP: Combat Racing (STEAM) | 19 | 33 | 58% (90d) | Does not open (100%) | 83% |  |
| 274 | [ ] | DNF Duel (EPIC) | 19 | 32 | 59% (90d) | Does not open (44%) | 88% |  |
| 275 | [ ] | Metro Exodus (STEAM) | 19 | 30 | 63% (90d) | Does not open (82%) | 91% |  |
| 276 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 19 | 28 | 68% (90d) | Does not open (72%) | 70% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 277 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 19 | 24 | 79% (90d) | Does not open (82%) | 100% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 278 | [ ] | SKALD: Against the Black Priory (STEAM) | 18 | 36 | 50% (90d) | No graphics (75%) | 100% |  |
| 279 | [ ] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 18 | 35 | 51% (90d) | Controller issues (50%) | 100% |  |
| 280 | [ ] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 18 | 35 | 51% (90d) | Does not open (57%) | 90% |  |
| 281 | [ ] | SCP – Containment Breach (STEAM) | 18 | 35 | 51% (90d) | Does not open (83%) | 82% |  |
| 282 | [ ] | Faster Than Light (EPIC) | 18 | 34 | 53% (90d) | Does not open (41%) | 92% |  |
| 283 | [ ] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 18 | 34 | 53% (90d) | Does not open (88%) | 64% |  |
| 284 | [ ] | Antichamber (STEAM) | 18 | 33 | 55% (90d) | Does not open (47%) | 88% |  |
| 285 | [ ] | Formula Legends (STEAM) | 18 | 29 | 62% (90d) | No graphics (60%) | 75% |  |
| 286 | [ ] | Titanfall® 2 (STEAM) | 18 | 29 | 62% (90d) | Does not open (83%) | 87% |  |
| 287 | [ ] | Moon Sweepers (STEAM) | 18 | 28 | 67% (1.3.0) | Controller issues (80%) | 81% |  |
| 288 | [ ] | Dishonored 2 (STEAM) | 18 | 27 | 67% (90d) | Does not open (87%) | 94% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 289 | [ ] | Fall Guys (STEAM) | 18 | 24 | 75% (90d) | Does not open (92%) | 92% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 290 | [ ] | CULTIC (STEAM) | 17 | 33 | 52% (90d) | Does not open (92%) | 69% |  |
| 291 | [ ] | Grim Fandango Remastered (STEAM) | 17 | 33 | 52% (90d) | Does not open (93%) | 81% |  |
| 292 | [ ] | GRANDIA HD Remaster (STEAM) | 17 | 32 | 53% (90d) | Does not open (93%) | 67% |  |
| 293 | [ ] | Shank 2 (STEAM) | 17 | 30 | 57% (90d) | Does not open (82%) | 100% |  |
| 294 | [ ] | Maneater (STEAM) | 17 | 28 | 61% (90d) | Does not open (92%) | 77% |  |
| 295 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 17 | 28 | 61% (90d) | No graphics (47%) | 80% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 296 | [ ] | Wildermyth (STEAM) | 17 | 28 | 61% (90d) | Does not open (50%) | 91% |  |
| 297 | [ ] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 17 | 27 | 63% (90d) | Does not open (100%) | 95% |  |
| 298 | [ ] | Alabaster Dawn Demo (STEAM) | 17 | 26 | 65% (90d) | Controller issues (71%) | 92% |  |
| 299 | [ ] | Arcade Paradise (EPIC) | 17 | 26 | 65% (90d) | Does not open (56%) | 83% |  |
| 300 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 17 | 24 | 71% (90d) | No graphics (60%) | 88% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 301 | [ ] | Katanaut (STEAM) | 17 | 24 | 71% (90d) | Does not open (75%) | 64% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 302 | [ ] | Realm of the Mad God Exalt (STEAM) | 17 | 22 | 77% (90d) | Does not open (92%) | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 303 | [ ] | Prey (GOG) | 17 | 21 | 81% (90d) | Does not open (47%) | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 304 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 16 | 32 | 50% (90d) | Does not open (92%) | 65% |  |
| 305 | [ ] | Distance (STEAM) | 16 | 32 | 50% (90d) | Does not open (79%) | 82% |  |
| 306 | [ ] | Mortal Kombat 11 (STEAM) | 16 | 32 | 50% (90d) | Does not open (70%) | 61% |  |
| 307 | [ ] | Mark of the Ninja (STEAM) | 16 | 31 | 52% (90d) | Does not open (67%) | 65% |  |
| 308 | [ ] | Far Far West (STEAM) | 16 | 29 | 55% (90d) | Does not open (53%) | 91% |  |
| 309 | [ ] | Race The Sun (STEAM) | 16 | 27 | 59% (90d) | No graphics (92%) | 70% |  |
| 310 | [ ] | WORLD OF FINAL FANTASY (STEAM) | 16 | 26 | 62% (90d) | No graphics (62%) | 74% |  |
| 311 | [ ] | Batman™: Arkham Origins (GOG) | 16 | 25 | 64% (90d) | Does not open (69%) | 92% |  |
| 312 | [ ] | Chef Knight (STEAM) | 16 | 23 | 70% (90d) | Does not open (93%) | 75% |  |
| 313 | [ ] | Cyberpunk 2077 (EPIC) | 16 | 21 | 76% (90d) | Does not open (46%) | 83% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 314 | [ ] | Mortal Shell (EPIC) | 15 | 28 | 54% (90d) | No graphics (89%) | 80% |  |
| 315 | [ ] | LET IT DIE (STEAM) | 15 | 25 | 60% (90d) | Does not open (91%) | 77% |  |
| 316 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 15 | 24 | 63% (90d) | Does not open (92%) | 69% |  |
| 317 | [ ] | Gloomwood (STEAM) | 15 | 24 | 63% (90d) | Does not open (64%) | 60% |  |
| 318 | [ ] | Sons Of The Forest (STEAM) | 15 | 23 | 65% (90d) | Does not open (56%) | 76% |  |
| 319 | [ ] | Allumeria (STEAM) | 15 | 22 | 68% (90d) | Does not open (69%) | 71% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 320 | [ ] | Disgaea 4 Complete+ (STEAM) | 15 | 22 | 68% (90d) | No graphics (47%) | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 321 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 15 | 22 | 68% (90d) | Does not open (75%) | 62% |  |
| 322 | [ ] | DayZ (STEAM) | 15 | 21 | 71% (90d) | Does not open (56%) | 70% | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 323 | [ ] | Maneater (EPIC) | 15 | 20 | 75% (90d) | Does not open (73%) | 82% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 324 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 26 | 54% (90d) | Controller issues (54%) | 90% |  |
| 325 | [ ] | Academy Love Saga: Tennis Angels EX (STEAM) | 14 | 25 | 56% (90d) | Does not open (77%) | 93% |  |
| 326 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 25 | 56% (90d) | Does not open (90%) | 76% |  |
| 327 | [ ] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 14 | 23 | 61% (90d) | Does not open (69%) | 74% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 328 | [ ] | Prince of Persia: The Two Thrones (STEAM) | 14 | 22 | 64% (90d) | Does not open (86%) | 61% |  |
| 329 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 22 | 64% (90d) | Controller issues (57%) | 63% |  |
| 330 | [ ] | Escape the Backrooms (STEAM) | 14 | 21 | 67% (90d) | Does not open (100%) | 91% |  |
| 331 | [ ] | Horny Villa (STEAM) | 14 | 21 | 67% (90d) | Does not open (63%) | 100% |  |
| 332 | [ ] | Fallout 2 (GOG) | 14 | 20 | 70% (90d) | Does not open (54%) | 67% |  |
| 333 | [ ] | BioShock 2 Remastered (EPIC) | 13 | 26 | 50% (90d) | Does not open (56%) | 91% |  |
| 334 | [ ] | Coromon (GOG) | 13 | 25 | 52% (90d) | No graphics (58%) | 65% |  |
| 335 | [ ] | Human Fall Flat (STEAM) | 13 | 24 | 54% (90d) | Does not open (58%) | 61% |  |
| 336 | [ ] | Injustice™ 2 (STEAM) | 13 | 24 | 54% (90d) | Does not open (90%) | 74% |  |
| 337 | [ ] | Pillars of Eternity (STEAM) | 13 | 24 | 54% (90d) | Does not open (43%) | 69% |  |
| 338 | [ ] | Ultrapool (STEAM) | 13 | 24 | 54% (90d) | Does not open (58%) | 100% |  |
| 339 | [ ] | Minit (EPIC) | 13 | 23 | 57% (90d) | Does not open (82%) | 82% |  |
| 340 | [ ] | DiRT 4 (STEAM) | 13 | 22 | 59% (90d) | Does not open (75%) | 94% |  |
| 341 | [ ] | Lust Goddess (STEAM) | 13 | 22 | 59% (90d) | Does not open (100%) | 64% |  |
| 342 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 22 | 59% (90d) | Does not open (80%) | 91% |  |
| 343 | [ ] | Secret of Mana (STEAM) | 13 | 21 | 62% (90d) | Graphics glitches (58%) | 60% |  |
| 344 | [ ] | F.E.A.R. 2: Project Origin (STEAM) | 12 | 24 | 50% (90d) | Does not open (50%) | 81% |  |
| 345 | [ ] | Haydee (STEAM) | 12 | 24 | 50% (90d) | Does not open (100%) | 88% |  |
| 346 | [ ] | Mina the Hollower (GOG) | 12 | 24 | 50% (90d) | Does not open (42%) | 67% |  |
| 347 | [ ] | Ys VIII: Lacrimosa of Dana (STEAM) | 12 | 24 | 50% (90d) | Does not open (70%) | 77% |  |
| 348 | [ ] | sobosuba (STEAM) | 12 | 24 | 50% (90d) | Does not open (58%) | 92% |  |
| 349 | [ ] | AER Memories of Old (EPIC) | 12 | 23 | 52% (90d) | Does not open (91%) | 92% |  |
| 350 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 12 | 23 | 52% (90d) | Does not open (60%) | 86% |  |
| 351 | [ ] | NiGHTS into Dreams... (STEAM) | 12 | 23 | 52% (90d) | Does not open (44%) | 91% |  |
| 352 | [ ] | Sonic Superstars (STEAM) | 12 | 22 | 55% (90d) | Does not open (70%) | 69% |  |
| 353 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 12 | 21 | 57% (90d) | Does not open (86%) | 75% |  |
| 354 | [ ] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 21 | 57% (90d) | Controller issues (60%) | 93% |  |
| 355 | [ ] | Commander Keen Complete Pack (STEAM) | 12 | 20 | 60% (90d) | Does not open (73%) | 100% |  |
| 356 | [ ] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 20 | 60% (90d) | Does not open (67%) | 64% |  |
| 357 | [ ] | Dungeon Siege (STEAM) | 11 | 22 | 50% (90d) | Does not open (38%) | 93% |  |
| 358 | [ ] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 22 | 50% (90d) | Does not open (50%) | 67% |  |
| 359 | [ ] | Sid Meier's Civilization VI (EPIC) | 11 | 22 | 50% (90d) | Does not open (40%) | 88% |  |
| 360 | [ ] | Castle in the Clouds (STEAM) | 11 | 21 | 52% (90d) | No graphics (63%) | 94% |  |
| 361 | [ ] | HITMAN World of Assassination (STEAM) | 11 | 21 | 52% (90d) | Does not open (70%) | 91% |  |
| 362 | [ ] | Pocket Mirror ~ GoldenerTraum (STEAM) | 11 | 21 | 52% (90d) | Does not open (70%) | 100% |  |
| 363 | [ ] | Ready or Not (STEAM) | 11 | 20 | 55% (90d) | Does not open (60%) | 87% |  |
| 364 | [ ] | Pathologic Classic HD (STEAM) | 10 | 20 | 50% (90d) | No graphics (78%) | 83% |  |
| 365 | [ ] | Tom Clancy's Rainbow Six: Vegas 2 (STEAM) | 10 | 20 | 50% (90d) | Does not open (60%) | 84% |  |

## Recently recovered (360)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 276 | 2026-10-23 | 317 | 64% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 2 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 255 | 2026-10-19 | 305 | 65% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 3 | [x] | FINAL FANTASY RESONANCE (STEAM) | 221 | 2026-10-24 | 499 | 71% |  |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 219 | 2026-10-18 | 336 | 58% |  |
| 5 | [x] | OMORI (STEAM) | 212 | 2026-10-16 | 255 | 77% |  |
| 6 | [x] | Devil May Cry HD Collection (STEAM) | 200 | 2026-10-19 | 281 | 73% |  |
| 7 | [x] | Burnout Paradise: The Ultimate Box (STEAM) | 162 | 2026-10-16 | 246 | 72% |  |
| 8 | [x] | Counter-Strike (STEAM) | 155 | 2026-10-22 | 240 | 52% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 9 | [x] | Far Cry® 3 (STEAM) | 142 | 2026-10-21 | 161 | 64% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 10 | [x] | Borderlands 2 (EPIC) | 140 | 2026-10-25 | 162 | 63% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 11 | [x] | Minecraft Dungeons II (STEAM) | 122 | 2026-10-21 | 139 | 66% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 12 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 120 | 2026-10-28 | 148 | 61% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 13 | [x] | Call of Duty: Black Ops III (STEAM) | 118 | 2026-10-18 | 244 | 72% |  |
| 14 | [x] | The Witcher: Enhanced Edition (STEAM) | 118 | 2026-10-25 | 136 | 62% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 15 | [x] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 110 | 2026-10-18 | 154 | 64% |  |
| 16 | [x] | Moonstone Island (STEAM) | 105 | 2026-10-16 | 138 | 91% |  |
| 17 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 99 | 2026-10-25 | 155 | 63% |  |
| 18 | [x] | Don't Starve Together (STEAM) | 96 | 2026-10-16 | 182 | 79% |  |
| 19 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 96 | 2026-10-17 | 129 | 100% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 20 | [x] | Cry of Fear (STEAM) | 93 | 2026-10-18 | 178 | 92% |  |
| 21 | [x] | Catherine Classic (STEAM) | 87 | 2026-10-19 | 178 | 78% |  |
| 22 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 86 | 2026-10-18 | 128 | 74% |  |
| 23 | [x] | Hogwarts Legacy (STEAM) | 83 | 2026-10-17 | 140 | 67% |  |
| 24 | [x] | DOOM 3: BFG Edition (STEAM) | 83 | 2026-10-19 | 119 | 70% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 25 | [x] | Ultra Street Fighter IV (STEAM) | 82 | 2026-10-17 | 178 | 68% |  |
| 26 | [x] | Detroit: Become Human (STEAM) | 79 | 2026-10-17 | 82 | 68% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 27 | [x] | Need for Speed: Hot Pursuit (STEAM) | 78 | 2026-10-25 | 107 | 76% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 28 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 76 | 2026-10-17 | 103 | 84% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 29 | [x] | Bayonetta (STEAM) | 73 | 2026-10-18 | 200 | 76% |  |
| 30 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 73 | 2026-10-18 | 122 | 93% |  |
| 31 | [x] | Call of Juarez Gunslinger (STEAM) | 73 | 2026-10-18 | 88 | 71% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 32 | [x] | Don't Starve (STEAM) | 72 | 2026-10-16 | 153 | 83% |  |
| 33 | [x] | Darksiders (STEAM) | 72 | 2026-10-26 | 87 | 92% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 34 | [x] | Fable - The Lost Chapters (STEAM) | 70 | 2026-10-17 | 109 | 79% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 35 | [x] | Dota 2 (STEAM) | 70 | 2026-10-17 | 107 | 74% |  |
| 36 | [x] | Gunfire Reborn (STEAM) | 70 | 2026-10-22 | 77 | 92% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 37 | [x] | Fallout (STEAM) | 69 | 2026-10-18 | 108 | 72% |  |
| 38 | [x] | American Truck Simulator (STEAM) | 68 | 2026-10-18 | 107 | 75% |  |
| 39 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 68 | 2026-10-21 | 90 | 70% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 40 | [x] | Bloodstained: Ritual of the Night (EPIC) | 67 | 2026-10-19 | 122 | 64% |  |
| 41 | [x] | Spyro™ Reignited Trilogy (STEAM) | 66 | 2026-10-18 | 104 | 69% |  |
| 42 | [x] | Borderlands: The Pre-Sequel (STEAM) | 66 | 2026-10-17 | 92 | 68% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 43 | [x] | Disgaea 5 Complete (STEAM) | 66 | 2026-10-18 | 80 | 97% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 44 | [x] | Poppy Playtime (STEAM) | 65 | 2026-10-17 | 111 | 79% |  |
| 45 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 64 | 2026-10-17 | 86 | 91% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 46 | [x] | A Plague Tale: Innocence (STEAM) | 64 | 2026-10-20 | 67 | 75% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 47 | [x] | Sonic Lost World (STEAM) | 63 | 2026-10-18 | 102 | 90% |  |
| 48 | [x] | Big Walk (STEAM) | 63 | 2026-10-17 | 96 | 84% |  |
| 49 | [x] | eFootball™ (STEAM) | 60 | 2026-10-18 | 91 | 75% |  |
| 50 | [x] | TBH: Task Bar Hero (STEAM) | 60 | 2026-10-19 | 90 | 96% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 51 | [x] | Borderlands 3 (STEAM) | 60 | 2026-10-19 | 77 | 95% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 52 | [x] | Sonic Generations (STEAM) | 60 | 2026-10-17 | 70 | 66% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 53 | [x] | Sonic Adventure DX (STEAM) | 59 | 2026-10-17 | 96 | 71% |  |
| 54 | [x] | Call of Duty: World at War (STEAM) | 59 | 2026-10-28 | 82 | 62% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 55 | [x] | Starbound (STEAM) | 58 | 2026-10-18 | 85 | 71% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 56 | [x] | Dead by Daylight (STEAM) | 58 | 2026-10-23 | 63 | 80% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 57 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 55 | 2026-10-18 | 87 | 69% |  |
| 58 | [x] | Path of Exile (STEAM) | 55 | 2026-10-26 | 64 | 83% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 59 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 55 | 2026-10-21 | 63 | 79% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 60 | [x] | A Plague Tale: Innocence (EPIC) | 54 | 2026-10-25 | 91 | 87% |  |
| 61 | [x] | MudRunner (STEAM) | 53 | 2026-10-24 | 104 | 65% |  |
| 62 | [x] | Mini Motorways (STEAM) | 53 | 2026-10-29 | 95 | 62% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 63 | [x] | Teardown (STEAM) | 52 | 2026-10-17 | 93 | 76% |  |
| 64 | [x] | Until Then (STEAM) | 52 | 2026-10-17 | 93 | 97% |  |
| 65 | [x] | Street Fighter™ 6 (STEAM) | 51 | 2026-10-16 | 75 | 80% |  |
| 66 | [x] | Guildrun Demo (STEAM) | 51 | 2026-10-22 | 74 | 72% |  |
| 67 | [x] | Sheepy: A Short Adventure (STEAM) | 51 | 2026-10-24 | 61 | 81% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 68 | [x] | Alex Kidd in Miracle World DX (EPIC) | 51 | 2026-10-22 | 55 | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 69 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 50 | 2026-10-19 | 87 | 70% |  |
| 70 | [x] | Dead Space (STEAM) | 50 | 2026-10-18 | 63 | 71% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 71 | [x] | Sleeping Dogs™ (STEAM) | 50 | 2026-10-27 | 57 | 80% | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 72 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 49 | 2026-10-25 | 91 | 57% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 73 | [x] | Okami HD (STEAM) | 49 | 2026-10-17 | 90 | 87% |  |
| 74 | [x] | Rivals of Aether II (STEAM) | 49 | 2026-10-20 | 74 | 72% |  |
| 75 | [x] | FINAL FANTASY VII (2013) (STEAM) | 48 | 2026-10-18 | 69 | 81% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 76 | [x] | Digimon World: Next Order (STEAM) | 47 | 2026-10-18 | 87 | 94% |  |
| 77 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 2026-10-17 | 75 | 94% |  |
| 78 | [x] | STEINS;GATE RE:BOOT (STEAM) | 47 | 2026-10-21 | 68 | 82% |  |
| 79 | [x] | Tomb Raider GOTY (GOG) | 46 | 2026-10-17 | 94 | 98% |  |
| 80 | [x] | Tomb Raider: Anniversary (STEAM) | 46 | 2026-10-25 | 66 | 70% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 81 | [x] | Darkest Dungeon® (EPIC) | 45 | 2026-10-22 | 83 | 62% |  |
| 82 | [x] | Abiotic Factor (STEAM) | 45 | 2026-10-18 | 80 | 68% |  |
| 83 | [x] | Dishonored - Definitive Edition (EPIC) | 44 | 2026-10-17 | 95 | 80% |  |
| 84 | [x] | PROTOTYPE 2 (STEAM) | 44 | 2026-10-18 | 88 | 79% |  |
| 85 | [x] | Life is Strange™ (STEAM) | 44 | 2026-10-17 | 85 | 83% |  |
| 86 | [x] | Death Road to Canada (STEAM) | 43 | 2026-10-17 | 97 | 74% |  |
| 87 | [x] | Cobalt Core (STEAM) | 43 | 2026-10-18 | 93 | 86% |  |
| 88 | [x] | Salt and Sanctuary (STEAM) | 43 | 2026-10-18 | 81 | 82% |  |
| 89 | [x] | Moonlighter (EPIC) | 43 | 2026-10-23 | 47 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 90 | [x] | Rogue Legacy (STEAM) | 42 | 2026-10-17 | 92 | 55% |  |
| 91 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 42 | 2026-10-17 | 77 | 87% |  |
| 92 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 42 | 2026-10-18 | 66 | 67% |  |
| 93 | [x] | Deadlock (STEAM) | 42 | 2026-10-16 | 66 | 94% |  |
| 94 | [x] | Rayman Origins (STEAM) | 41 | 2026-10-17 | 90 | 83% |  |
| 95 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 41 | 2026-10-17 | 76 | 94% |  |
| 96 | [x] | Amnesia: The Dark Descent (STEAM) | 41 | 2026-10-17 | 76 | 76% |  |
| 97 | [x] | Tales of ARISE (STEAM) | 41 | 2026-10-16 | 69 | 92% |  |
| 98 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 41 | 2026-10-18 | 62 | 74% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 99 | [x] | Capcom Arcade Stadium (STEAM) | 41 | 2026-10-17 | 51 | 75% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 100 | [x] | Aggelos (STEAM) | 40 | 2026-10-21 | 54 | 94% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 101 | [x] | Sable (EPIC) | 39 | 2026-10-18 | 81 | 82% |  |
| 102 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 39 | 2026-10-27 | 41 | 82% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 103 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-10-23 | 40 | 72% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 104 | [x] | CrossCode (GOG) | 38 | 2026-10-23 | 42 | 72% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 105 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 2026-10-17 | 67 | 86% |  |
| 106 | [x] | Romestead (STEAM) | 37 | 2026-10-18 | 48 | 81% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 107 | [x] | Rocket League (STEAM) | 36 | 2026-10-17 | 55 | 68% |  |
| 108 | [x] | Capcom Fighting Collection 2 (STEAM) | 36 | 2026-10-18 | 52 | 87% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 109 | [x] | POSTAL 2 (GOG) | 35 | 2026-10-22 | 72 | 96% |  |
| 110 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 35 | 2026-10-16 | 67 | 65% |  |
| 111 | [x] | Hearts of Iron IV (STEAM) | 35 | 2026-10-19 | 59 | 60% |  |
| 112 | [x] | Earthion (STEAM) | 35 | 2026-10-22 | 56 | 100% |  |
| 113 | [x] | Battle Brothers (STEAM) | 35 | 2026-10-27 | 52 | 62% |  |
| 114 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 35 | 2026-10-21 | 49 | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 115 | [x] | SnowRunner (STEAM) | 35 | 2026-10-19 | 47 | 82% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 116 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 35 | 2026-10-18 | 41 | 74% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 117 | [x] | Journey (STEAM) | 34 | 2026-10-27 | 70 | 52% |  |
| 118 | [x] | Ultimate Chicken Horse (STEAM) | 34 | 2026-10-23 | 70 | 55% |  |
| 119 | [x] | Monster Hunter Stories (STEAM) | 34 | 2026-10-17 | 69 | 83% |  |
| 120 | [x] | Deponia (STEAM) | 34 | 2026-10-29 | 63 | 60% |  |
| 121 | [x] | Ultimate Custom Night (STEAM) | 34 | 2026-10-19 | 46 | 76% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 122 | [x] | Lost Planet: Extreme Condition (STEAM) | 34 | 2026-10-25 | 41 | 60% | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 123 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 34 | 2026-10-22 | 41 | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 124 | [x] | Resident Evil Village (STEAM) | 33 | 2026-10-17 | 55 | 87% |  |
| 125 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 33 | 2026-10-19 | 54 | 65% |  |
| 126 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 2026-10-19 | 53 | 83% |  |
| 127 | [x] | Secrets of Grindea (STEAM) | 33 | 2026-10-20 | 51 | 81% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 128 | [x] | Counter-Strike:Global Offensive (STEAM) | 33 | 2026-10-19 | 50 | 72% |  |
| 129 | [x] | Supermarket Together (STEAM) | 33 | 2026-10-19 | 48 | 82% |  |
| 130 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 33 | 2026-10-20 | 43 | 89% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 131 | [x] | Russian Fishing 4 (STEAM) | 33 | 2026-10-23 | 38 | 67% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 132 | [x] | Need for Speed™ (STEAM) | 33 | 2026-10-18 | 37 | 63% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 133 | [x] | Hotline Miami (GOG) | 33 | 2026-10-20 | 36 | 64% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 134 | [x] | Little Nightmares (STEAM) | 32 | 2026-10-16 | 72 | 60% |  |
| 135 | [x] | Bloodstained: Curse of the Moon (STEAM) | 32 | 2026-10-16 | 67 | 66% |  |
| 136 | [x] | Stumble Guys (STEAM) | 32 | 2026-10-18 | 65 | 83% |  |
| 137 | [x] | COCOON (STEAM) | 32 | 2026-10-17 | 62 | 88% |  |
| 138 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 32 | 2026-10-26 | 56 | 63% |  |
| 139 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 32 | 2026-10-22 | 51 | 71% |  |
| 140 | [x] | Nioh: Complete Edition (STEAM) | 32 | 2026-10-20 | 43 | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 141 | [x] | Super Animal Royale (STEAM) | 32 | 2026-10-19 | 41 | 72% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 142 | [x] | Path of Exile 2 (STEAM) | 32 | 2026-10-18 | 37 | 85% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 143 | [x] | Torchlight II (STEAM) | 31 | 2026-10-20 | 62 | 94% |  |
| 144 | [x] | Library Of Ruina (STEAM) | 31 | 2026-10-16 | 60 | 84% |  |
| 145 | [x] | Max Payne (STEAM) | 31 | 2026-10-17 | 57 | 95% |  |
| 146 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 31 | 2026-10-17 | 56 | 85% |  |
| 147 | [x] | Deus Ex™ GOTY Edition (GOG) | 31 | 2026-10-19 | 47 | 84% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 148 | [x] | Tower and Sword of Succubus (STEAM) | 31 | 2026-10-22 | 46 | 100% |  |
| 149 | [x] | Moonlight Peaks (STEAM) | 31 | 2026-10-20 | 45 | 100% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 150 | [x] | Grand Theft Auto III (STEAM) | 31 | 2026-10-17 | 39 | 88% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 151 | [x] | Capcom Fighting Collection (STEAM) | 31 | 2026-10-23 | 35 | 71% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 152 | [x] | Dying Light (EPIC) | 30 | 2026-10-17 | 68 | 94% |  |
| 153 | [x] | BioShock™ (GOG) | 30 | 2026-10-18 | 62 | 69% |  |
| 154 | [x] | Cave Story+ (EPIC) | 29 | 2026-10-18 | 55 | 85% |  |
| 155 | [x] | Aethermancer (STEAM) | 29 | 2026-10-18 | 49 | 76% |  |
| 156 | [x] | Binary Domain (STEAM) | 29 | 2026-10-18 | 45 | 79% |  |
| 157 | [x] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 29 | 2026-10-28 | 29 | 62% | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 158 | [x] | Mortal Kombat X (STEAM) | 28 | 2026-10-17 | 53 | 85% |  |
| 159 | [x] | Heavy Rain (STEAM) | 28 | 2026-10-18 | 49 | 85% |  |
| 160 | [x] | Prince of Persia: The Sands of Time (STEAM) | 28 | 2026-10-20 | 48 | 94% |  |
| 161 | [x] | Zero Escape: The Nonary Games (STEAM) | 28 | 2026-10-17 | 46 | 62% |  |
| 162 | [x] | Crab Game (STEAM) | 28 | 2026-10-22 | 37 | 74% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 163 | [x] | CRUEL (STEAM) | 28 | 2026-10-28 | 34 | 70% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 164 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 27 | 2026-10-19 | 90 | 91% |  |
| 165 | [x] | G.I. Joe Wrath of Cobra (EPIC) | 27 | 2026-10-19 | 51 | 67% |  |
| 166 | [x] | Akane (STEAM) | 27 | 2026-10-20 | 46 | 100% |  |
| 167 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 27 | 2026-10-18 | 39 | 88% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 168 | [x] | Goose Goose Duck (STEAM) | 27 | 2026-10-25 | 34 | 77% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 169 | [x] | Tales of Zestiria (STEAM) | 27 | 2026-10-27 | 33 | 69% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 170 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 26 | 2026-10-19 | 62 | 83% |  |
| 171 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 26 | 2026-10-18 | 51 | 79% |  |
| 172 | [x] | Wizard of Legend (EPIC) | 26 | 2026-10-18 | 44 | 76% |  |
| 173 | [x] | Prince of Persia (GOG) | 26 | 2026-10-24 | 42 | 80% |  |
| 174 | [x] | Limbus Company (STEAM) | 26 | 2026-10-18 | 40 | 79% |  |
| 175 | [x] | SWORN (STEAM) | 26 | 2026-10-23 | 40 | 100% |  |
| 176 | [x] | Gothic II: Gold Classic (STEAM) | 26 | 2026-10-20 | 39 | 79% |  |
| 177 | [x] | Palia (STEAM) | 26 | 2026-10-22 | 36 | 71% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 178 | [x] | PlateUp! (STEAM) | 25 | 2026-10-16 | 59 | 82% |  |
| 179 | [x] | State of Decay: Year-One (STEAM) | 25 | 2026-10-18 | 57 | 85% |  |
| 180 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 25 | 2026-10-20 | 52 | 82% |  |
| 181 | [x] | CarX Drift Racing Online (STEAM) | 25 | 2026-10-16 | 50 | 70% |  |
| 182 | [x] | Being a DIK (STEAM) | 25 | 2026-10-19 | 43 | 90% |  |
| 183 | [x] | Counter-Strike: Condition Zero (STEAM) | 25 | 2026-10-17 | 43 | 64% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 184 | [x] | Digimon Survive (STEAM) | 25 | 2026-10-23 | 42 | 96% |  |
| 185 | [x] | Cat Mail Co. (STEAM) | 25 | 2026-10-24 | 40 | 87% |  |
| 186 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-10-21 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 187 | [x] | Resident Evil (GOG) | 25 | 2026-10-20 | 27 | 72% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 188 | [x] | Titan Quest Anniversary Edition (STEAM) | 24 | 2026-10-16 | 55 | 83% |  |
| 189 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 54 | 87% |  |
| 190 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 24 | 2026-10-17 | 38 | 89% |  |
| 191 | [x] | Timberborn (STEAM) | 24 | 2026-10-25 | 36 | 83% |  |
| 192 | [x] | Bongo Cat (STEAM) | 24 | 2026-10-20 | 34 | 79% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 193 | [x] | Beyond: Two Souls (STEAM) | 24 | 2026-10-22 | 32 | 73% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 194 | [x] | Need for Speed™ Unbound (STEAM) | 24 | 2026-10-26 | 32 | 75% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 195 | [x] | BlazBlue Centralfiction (STEAM) | 23 | 2026-10-17 | 62 | 81% |  |
| 196 | [x] | ABZÛ (STEAM) | 23 | 2026-10-21 | 51 | 91% |  |
| 197 | [x] | WEBFISHING (STEAM) | 23 | 2026-10-17 | 50 | 91% |  |
| 198 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 23 | 2026-10-27 | 48 | 30% |  |
| 199 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 23 | 2026-10-24 | 44 | 94% |  |
| 200 | [x] | Changed (STEAM) | 23 | 2026-10-24 | 37 | 83% |  |
| 201 | [x] | Return to Monkey Island (STEAM) | 23 | 2026-10-23 | 37 | 93% |  |
| 202 | [x] | Party Animals (STEAM) | 23 | 2026-10-17 | 32 | 83% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 203 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 95% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 204 | [x] | Jade Empire: Special Edition (GOG) | 23 | 2026-10-23 | 29 | 78% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 205 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 23 | 2026-10-25 | 29 | 62% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 206 | [x] | Saints Row IV (STEAM) | 22 | 2026-10-19 | 50 | 75% |  |
| 207 | [x] | Mafia: Definitive Edition (STEAM) | 22 | 2026-10-28 | 41 | 90% |  |
| 208 | [x] | Football Manager 2024 (EPIC) | 22 | 2026-10-20 | 40 | 89% |  |
| 209 | [x] | Overlord (STEAM) | 22 | 2026-10-21 | 40 | 62% |  |
| 210 | [x] | This War of Mine (STEAM) | 22 | 2026-10-21 | 39 | 74% |  |
| 211 | [x] | Lobotomy Corporation (STEAM) | 22 | 2026-10-19 | 38 | 100% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 212 | [x] | Life is Strange Remastered (STEAM) | 22 | 2026-10-20 | 34 | 94% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 213 | [x] | Nex Machina (STEAM) | 22 | 2026-10-18 | 30 | 88% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 214 | [x] | No Rest for the Wicked (STEAM) | 21 | 2026-10-19 | 44 | 75% |  |
| 215 | [x] | Unturned (STEAM) | 21 | 2026-10-17 | 40 | 83% |  |
| 216 | [x] | Brothers - A Tale of Two Sons (EPIC) | 21 | 2026-10-23 | 39 | 67% |  |
| 217 | [x] | Pinball FX Classic (STEAM) | 21 | 2026-10-23 | 39 | 94% |  |
| 218 | [x] | One-armed robber (STEAM) | 21 | 2026-10-23 | 38 | 76% |  |
| 219 | [x] | Tiny Glade (STEAM) | 21 | 2026-10-24 | 36 | 77% |  |
| 220 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 21 | 2026-10-27 | 26 | 60% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 221 | [x] | MudRunner (EPIC) | 20 | 2026-10-18 | 42 | 90% |  |
| 222 | [x] | Hatred (STEAM) | 20 | 2026-10-22 | 41 | 85% |  |
| 223 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-10-20 | 39 | 100% |  |
| 224 | [x] | Paper Lily - Chapter 1 (STEAM) | 20 | 2026-10-27 | 38 | 91% |  |
| 225 | [x] | Killing Floor (STEAM) | 20 | 2026-10-19 | 36 | 86% |  |
| 226 | [x] | Trailmakers (STEAM) | 20 | 2026-10-21 | 36 | 91% |  |
| 227 | [x] | Tabletop Simulator (STEAM) | 20 | 2026-10-19 | 33 | 66% |  |
| 228 | [x] | Hitman: Absolution (GOG) | 20 | 2026-10-24 | 31 | 93% |  |
| 229 | [x] | DOOM 3: BFG Edition (GOG) | 20 | 2026-10-19 | 28 | 76% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 230 | [x] | Torchlight II (EPIC) | 20 | 2026-10-22 | 27 | 100% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 231 | [x] | BAJA: Edge of Control HD (STEAM) | 20 | 2026-10-28 | 26 | 90% | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 232 | [x] | Dead Island (STEAM) | 20 | 2026-10-20 | 26 | 71% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 233 | [x] | War Thunder (STEAM) | 20 | 2026-10-21 | 26 | 80% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 234 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 19 | 2026-10-25 | 44 | 71% |  |
| 235 | [x] | Slow Roads (STEAM) | 19 | 2026-10-22 | 41 | 96% |  |
| 236 | [x] | Graveyard Keeper (GOG) | 19 | 2026-10-25 | 39 | 23% |  |
| 237 | [x] | Backpack Battles (STEAM) | 19 | 2026-10-21 | 36 | 96% |  |
| 238 | [x] | Breath of Fire IV (GOG) | 19 | 2026-10-26 | 34 | 62% |  |
| 239 | [x] | Stick It to the Stickman (STEAM) | 19 | 2026-10-17 | 34 | 76% |  |
| 240 | [x] | GRIP: Combat Racing (STEAM) | 19 | 2026-10-20 | 33 | 83% |  |
| 241 | [x] | DNF Duel (EPIC) | 19 | 2026-10-21 | 32 | 88% |  |
| 242 | [x] | Metro Exodus (STEAM) | 19 | 2026-10-20 | 30 | 91% |  |
| 243 | [x] | Sonic and SEGA All Stars Racing (STEAM) | 19 | 2026-10-19 | 28 | 70% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 244 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 19 | 2026-10-23 | 24 | 100% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 245 | [x] | SKALD: Against the Black Priory (STEAM) | 18 | 2026-10-20 | 36 | 100% |  |
| 246 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 18 | 2026-10-21 | 35 | 100% |  |
| 247 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 18 | 2026-10-18 | 35 | 90% |  |
| 248 | [x] | SCP – Containment Breach (STEAM) | 18 | 2026-10-27 | 35 | 82% |  |
| 249 | [x] | Faster Than Light (EPIC) | 18 | 2026-10-24 | 34 | 92% |  |
| 250 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 18 | 2026-10-21 | 34 | 64% |  |
| 251 | [x] | Antichamber (STEAM) | 18 | 2026-10-20 | 33 | 88% |  |
| 252 | [x] | Formula Legends (STEAM) | 18 | 2026-10-21 | 29 | 75% |  |
| 253 | [x] | Titanfall® 2 (STEAM) | 18 | 2026-10-16 | 29 | 87% |  |
| 254 | [x] | Dishonored 2 (STEAM) | 18 | 2026-10-20 | 27 | 94% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 255 | [x] | Fall Guys (STEAM) | 18 | 2026-10-26 | 24 | 92% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 256 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 17 | 2026-10-20 | 35 | 73% |  |
| 257 | [x] | Spin Rhythm XD (STEAM) | 17 | 2026-10-18 | 35 | 87% |  |
| 258 | [x] | CULTIC (STEAM) | 17 | 2026-10-24 | 33 | 69% |  |
| 259 | [x] | Grim Fandango Remastered (STEAM) | 17 | 2026-10-19 | 33 | 81% |  |
| 260 | [x] | GRANDIA HD Remaster (STEAM) | 17 | 2026-10-22 | 32 | 67% |  |
| 261 | [x] | Shank 2 (STEAM) | 17 | 2026-10-27 | 30 | 100% |  |
| 262 | [x] | Maneater (STEAM) | 17 | 2026-10-20 | 28 | 77% |  |
| 263 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 17 | 2026-10-20 | 28 | 80% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 264 | [x] | Wildermyth (STEAM) | 17 | 2026-10-26 | 28 | 91% |  |
| 265 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 17 | 2026-10-21 | 27 | 95% |  |
| 266 | [x] | Arcade Paradise (EPIC) | 17 | 2026-10-25 | 26 | 83% |  |
| 267 | [x] | Alabaster Dawn Demo (STEAM) | 17 | 2026-10-27 | 26 | 92% |  |
| 268 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 17 | 2026-10-21 | 24 | 88% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 269 | [x] | Katanaut (STEAM) | 17 | 2026-10-20 | 24 | 64% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 270 | [x] | Realm of the Mad God Exalt (STEAM) | 17 | 2026-10-29 | 22 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 271 | [x] | Prey (GOG) | 17 | 2026-10-27 | 21 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 272 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 273 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 50 | 100% |  |
| 274 | [x] | No Man's Sky (GOG) | 16 | 2026-10-19 | 37 | 75% |  |
| 275 | [x] | Kingdom Come: Deliverance II (STEAM) | 16 | 2026-10-20 | 35 | 100% |  |
| 276 | [x] | Mini Metro (STEAM) | 16 | 2026-10-20 | 34 | 50% |  |
| 277 | [x] | Distance (STEAM) | 16 | 2026-10-19 | 32 | 82% |  |
| 278 | [x] | Mortal Kombat 11 (STEAM) | 16 | 2026-10-28 | 32 | 61% |  |
| 279 | [x] | Mark of the Ninja (STEAM) | 16 | 2026-10-26 | 31 | 65% |  |
| 280 | [x] | Far Far West (STEAM) | 16 | 2026-10-21 | 29 | 91% |  |
| 281 | [x] | Race The Sun (STEAM) | 16 | 2026-10-28 | 27 | 70% |  |
| 282 | [x] | WORLD OF FINAL FANTASY (STEAM) | 16 | 2026-10-19 | 26 | 74% |  |
| 283 | [x] | Batman™: Arkham Origins (GOG) | 16 | 2026-10-22 | 25 | 92% |  |
| 284 | [x] | Chef Knight (STEAM) | 16 | 2026-10-27 | 23 | 75% |  |
| 285 | [x] | Cyberpunk 2077 (EPIC) | 16 | 2026-10-19 | 21 | 83% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 286 | [x] | Mortal Shell (EPIC) | 15 | 2026-10-19 | 28 | 80% |  |
| 287 | [x] | LET IT DIE (STEAM) | 15 | 2026-10-25 | 25 | 77% |  |
| 288 | [x] | Gloomwood (STEAM) | 15 | 2026-10-29 | 24 | 60% |  |
| 289 | [x] | Sons Of The Forest (STEAM) | 15 | 2026-10-19 | 23 | 76% |  |
| 290 | [x] | Allumeria (STEAM) | 15 | 2026-10-23 | 22 | 71% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 291 | [x] | Disgaea 4 Complete+ (STEAM) | 15 | 2026-10-23 | 22 | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 292 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 15 | 2026-10-23 | 22 | 62% |  |
| 293 | [x] | DayZ (STEAM) | 15 | 2026-10-29 | 21 | 70% | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 294 | [x] | Maneater (EPIC) | 15 | 2026-10-28 | 20 | 82% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 295 | [x] | Tom Clancy's Splinter Cell: Chaos Theory (STEAM) | 14 | 2026-10-16 | 31 | 83% |  |
| 296 | [x] | Rayman Origins (GOG) | 14 | 2026-10-25 | 29 | 59% |  |
| 297 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 2026-10-29 | 26 | 90% |  |
| 298 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 14 | 2026-10-21 | 25 | 93% |  |
| 299 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 2026-10-25 | 25 | 76% |  |
| 300 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 14 | 2026-10-20 | 23 | 74% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 301 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 61% |  |
| 302 | [x] | Super Monkey Ball Banana Mania (STEAM) | 14 | 2026-10-18 | 22 | 63% |  |
| 303 | [x] | Escape the Backrooms (STEAM) | 14 | 2026-10-25 | 21 | 91% |  |
| 304 | [x] | Horny Villa (STEAM) | 14 | 2026-10-21 | 21 | 100% |  |
| 305 | [x] | Middle-earth™: Shadow of War™ (STEAM) | 13 | 2026-10-16 | 38 | 82% |  |
| 306 | [x] | Blood: Fresh Supply (STEAM) | 13 | 2026-10-16 | 35 | 79% |  |
| 307 | [x] | The WereCleaner (STEAM) | 13 | 2026-10-22 | 32 | 95% |  |
| 308 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 30 | 58% |  |
| 309 | [x] | Battle Chasers: Nightwar (STEAM) | 13 | 2026-10-20 | 28 | 67% |  |
| 310 | [x] | Haiku, the Robot (STEAM) | 13 | 2026-10-21 | 27 | 92% |  |
| 311 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 27 | 56% |  |
| 312 | [x] | Coromon (GOG) | 13 | 2026-10-19 | 25 | 65% |  |
| 313 | [x] | Human Fall Flat (STEAM) | 13 | 2026-10-29 | 24 | 61% |  |
| 314 | [x] | Injustice™ 2 (STEAM) | 13 | 2026-10-17 | 24 | 74% |  |
| 315 | [x] | Pillars of Eternity (STEAM) | 13 | 2026-10-26 | 24 | 69% |  |
| 316 | [x] | Ultrapool (STEAM) | 13 | 2026-10-24 | 24 | 100% |  |
| 317 | [x] | DiRT 4 (STEAM) | 13 | 2026-10-20 | 22 | 94% |  |
| 318 | [x] | Lust Goddess (STEAM) | 13 | 2026-10-26 | 22 | 64% |  |
| 319 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-10-21 | 22 | 91% |  |
| 320 | [x] | Secret of Mana (STEAM) | 13 | 2026-10-28 | 21 | 60% |  |
| 321 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 13 | 2026-10-25 | 20 | 94% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 322 | [x] | Possessor(s) (STEAM) | 12 | 2026-10-24 | 29 | n/a |  |
| 323 | [x] | Dead Space™ 3 (STEAM) | 12 | 2026-10-20 | 26 | 71% |  |
| 324 | [x] | Revolution Idle (STEAM) | 12 | 2026-10-26 | 25 | n/a |  |
| 325 | [x] | Mina the Hollower (GOG) | 12 | 2026-10-28 | 24 | 67% |  |
| 326 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 12 | 2026-10-21 | 24 | 81% |  |
| 327 | [x] | Haydee (STEAM) | 12 | 2026-10-22 | 24 | 88% |  |
| 328 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-10-22 | 23 | 86% |  |
| 329 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-10-28 | 23 | 91% |  |
| 330 | [x] | Sonic Superstars (STEAM) | 12 | 2026-10-21 | 22 | 69% |  |
| 331 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 12 | 2026-10-24 | 21 | 75% |  |
| 332 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 2026-10-26 | 21 | 93% |  |
| 333 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 334 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 2026-10-28 | 20 | 64% |  |
| 335 | [x] | TowerFall Ascension (STEAM) | 11 | 2026-10-16 | 31 | 55% |  |
| 336 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 11 | 2026-10-19 | 28 | 100% |  |
| 337 | [x] | SteamWorld Heist (GOG) | 11 | 2026-10-25 | 23 | n/a |  |
| 338 | [x] | DRAGON BALL XENOVERSE (STEAM) | 11 | 2026-10-28 | 23 | 55% |  |
| 339 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 23 | 78% |  |
| 340 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 11 | 2026-10-20 | 23 | 71% |  |
| 341 | [x] | Sid Meier's Civilization VI (EPIC) | 11 | 2026-10-19 | 22 | 88% |  |
| 342 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 2026-10-27 | 22 | 67% |  |
| 343 | [x] | Castle in the Clouds (STEAM) | 11 | 2026-10-21 | 21 | 94% |  |
| 344 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 11 | 2026-10-23 | 21 | 100% |  |
| 345 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 346 | [x] | What Remains of Edith Finch (STEAM) | 10 | 2026-10-19 | 26 | 46% |  |
| 347 | [x] | Divinity: Original Sin (Classic) (STEAM) | 10 | 2026-10-16 | 25 | n/a |  |
| 348 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 23 | 93% |  |
| 349 | [x] | 12 is Better Than 6 (STEAM) | 10 | 2026-10-21 | 21 | 80% |  |
| 350 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 351 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 352 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 83% |  |
| 353 | [x] | Delver (STEAM) | 9 | 2026-10-17 | 22 | 71% |  |
| 354 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 9 | 2026-10-23 | 21 | 75% |  |
| 355 | [x] | Football Manager 2024 (STEAM) | 9 | 2026-10-16 | 20 | n/a |  |
| 356 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 9 | 2026-10-20 | 20 | n/a |  |
| 357 | [x] | Gloomhaven (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 358 | [x] | Mafia II: Definitive Edition (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 359 | [x] | Intravenous (STEAM) | 8 | 2026-10-16 | 20 | 94% |  |
| 360 | [x] | Alex Kidd in Miracle World DX (STEAM) | 2 | 2026-10-16 | 36 | 82% |  |
