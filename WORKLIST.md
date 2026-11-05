# GameNative compatibility worklist

Generated: `2026-11-05T04:15:05.408Z` · App release: `1.3.0` · Ratings since: `2026-08-07T04:15:05.408Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 252 |
| Probably does not work | 75 |
| First launch fails | 356 |
| Mixed | 478 |
| Works | 1019 |
| Total | 2180 |

## Does not work (252)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [x] 2026-10-18 | Project Zomboid (STEAM) | 594 | 628 | 93% (1.3.0) | Does not open (66%) | 55% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 2 | [x] 2026-10-18 | Alan Wake (STEAM) | 252 | 263 | 90% (1.3.0) | Does not open (87%) | 9% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 3 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 241 | 260 | 93% (90d) | Does not open (76%) | 11% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 4 | [ ] | Counter-Strike 2 (STEAM) | 231 | 316 | 82% (1.3.0) | Does not open (61%) | 43% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 5 | [x] 2026-10-18 | Call of Duty: Black Ops (STEAM) | 212 | 223 | 95% (90d) | Does not open (75%) | 10% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 6 | [ ] | skate. (STEAM) | 192 | 206 | 93% (90d) | Does not open (79%) | 14% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 7 | [x] 2026-10-18 | Sid Meier's Civilization V (STEAM) | 175 | 187 | 94% (90d) | Does not open (75%) | 58% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 8 | [ ] | Peggle Deluxe (STEAM) | 154 | 186 | 83% (90d) | Does not open (92%) | 35% | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 9 | [ ] | Necesse (STEAM) | 154 | 159 | 97% (90d) | Does not open (80%) | 50% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 10 | [ ] | HELLDIVERS™ 2 (STEAM) | 138 | 144 | 96% (90d) | Does not open (92%) | 17% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 11 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 134 | 149 | 90% (90d) | Does not open (87%) | 48% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 12 | [ ] | Assassin's Creed II (STEAM) | 125 | 130 | 96% (90d) | Does not open (78%) | 54% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 13 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 105 | 139 | 75% (1.3.0) | Does not open (74%) | 36% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 14 | [ ] | Dust: An Elysian Tail (STEAM) | 105 | 109 | 96% (90d) | Does not open (73%) | 4% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 15 | [ ] | The Witcher: Enhanced Edition (GOG) | 103 | 113 | 91% (90d) | Does not open (74%) | 14% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 16 | [ ] | Call of Duty: Black Ops II (STEAM) | 102 | 134 | 86% (1.3.0) | Does not open (78%) | 26% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 17 | [ ] | Saints Row 2 (STEAM) | 96 | 108 | 93% (1.3.0) | Does not open (96%) | 41% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 18 | [ ] | Mafia II (Classic) (STEAM) | 94 | 99 | 95% (90d) | Does not open (71%) | 5% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 19 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 93 | 106 | 88% (90d) | Does not open (61%) | 54% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 20 | [ ] | Saints Row: The Third (STEAM) | 89 | 90 | 99% (90d) | Does not open (78%) | 33% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 21 | [ ] | Duskfade (STEAM) | 87 | 89 | 98% (90d) | Does not open (95%) | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 22 | [ ] | Transistor (STEAM) | 87 | 87 | 100% (90d) | Does not open (74%) | 0% | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 23 | [ ] | Black Mesa (STEAM) | 84 | 115 | 73% (90d) | Does not open (81%) | 14% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 24 | [ ] | Sniper Elite 4 (STEAM) | 83 | 83 | 100% (90d) | Does not open (97%) | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 25 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 82 | 84 | 98% (90d) | Does not open (91%) | 57% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 26 | [ ] | Fall Guys (EPIC) | 79 | 91 | 87% (90d) | Does not open (75%) | 11% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 27 | [ ] | HELLDIVERS™ (STEAM) | 78 | 87 | 90% (90d) | Does not open (59%) | 42% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 28 | [ ] | MECCHA CHAMELEON (STEAM) | 77 | 109 | 71% (90d) | Does not open (65%) | 59% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 29 | [ ] | Dead Space 2 (STEAM) | 77 | 98 | 79% (90d) | Does not open (73%) | 36% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 30 | [ ] | GRID 2 (STEAM) | 76 | 79 | 96% (90d) | Does not open (67%) | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 31 | [ ] | The Wolf Among Us (STEAM) | 72 | 78 | 92% (90d) | Does not open (67%) | 13% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 32 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 69 | 73 | 95% (90d) | Does not open (69%) | 0% | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 33 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 68 | 73 | 93% (90d) | Does not open (79%) | 8% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 34 | [ ] | Call of Duty: Black Ops II - Zombies (STEAM) | 67 | 83 | 81% (90d) | Does not open (69%) | 49% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 35 | [ ] | Saints Row 2 (GOG) | 67 | 80 | 84% (90d) | Does not open (96%) | 45% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 36 | [x] 2026-10-18 | Diablo® IV (STEAM) | 67 | 79 | 85% (90d) | Does not open (61%) | 23% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 37 | [ ] | Burnout™ Paradise Remastered (STEAM) | 67 | 70 | 96% (90d) | Does not open (87%) | 18% | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 38 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 66 | 75 | 95% (1.3.0) | No graphics (48%) | 23% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 39 | [ ] | Marvel Rivals (STEAM) | 66 | 74 | 89% (90d) | Does not open (81%) | 0% | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 40 | [ ] | Door Kickers 2 (STEAM) | 66 | 70 | 94% (90d) | No graphics (85%) | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 41 | [ ] | Metro 2033 (STEAM) | 65 | 81 | 80% (90d) | Does not open (63%) | 44% | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 42 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 64 | 86 | 74% (90d) | Does not open (47%) | 59% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 43 | [ ] | Borderlands GOTY (STEAM) | 64 | 69 | 93% (90d) | Does not open (95%) | 19% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 44 | [ ] | GRID (STEAM) | 63 | 78 | 81% (90d) | Does not open (57%) | 48% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 45 | [ ] | Three Kingdoms : Alias (STEAM) | 62 | 66 | 94% (90d) | No graphics (97%) | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 46 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 62 | 62 | 100% (90d) | Does not open (53%) | 10% | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 47 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 60 | 85 | 71% (90d) | Does not open (84%) | 50% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 48 | [ ] | Need for Speed™ Heat  (STEAM) | 60 | 74 | 81% (90d) | Does not open (76%) | 27% | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 49 | [ ] | Spore (STEAM) | 60 | 65 | 92% (90d) | Does not open (69%) | 31% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 50 | [ ] | DOOM (2016) (GOG) | 57 | 63 | 90% (90d) | Does not open (90%) | 35% | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 51 | [ ] | XCOM: Enemy Unknown (STEAM) | 56 | 59 | 95% (90d) | Does not open (77%) | 8% | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 52 | [ ] | Enshrouded (STEAM) | 56 | 57 | 98% (90d) | Does not open (95%) | 19% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 53 | [ ] | GrandChase (STEAM) | 55 | 58 | 95% (90d) | Does not open (84%) | 12% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 54 | [ ] | Overwatch® (STEAM) | 55 | 57 | 96% (90d) | Does not open (58%) | 29% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 55 | [ ] | STAR WARS Zero Company™ (STEAM) | 53 | 55 | 96% (90d) | Does not open (64%) | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 56 | [ ] | Spec Ops: The Line (STEAM) | 53 | 54 | 98% (90d) | No graphics (56%) | 0% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 57 | [ ] | Watch_Dogs (STEAM) | 52 | 67 | 78% (90d) | Does not open (90%) | 19% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 58 | [ ] | South Park The Fractured But Whole (STEAM) | 52 | 52 | 100% (90d) | Does not open (66%) | 15% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 59 | [ ] | Max Payne 3 (STEAM) | 51 | 56 | 91% (90d) | Does not open (93%) | 38% | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 60 | [ ] | Sandustry (STEAM) | 50 | 62 | 81% (90d) | Does not open (73%) | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 61 | [ ] | METAL SLUG 3 (STEAM) | 50 | 59 | 85% (90d) | Does not open (80%) | 19% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 62 | [ ] | Prince of Persia The Lost Crown (STEAM) | 50 | 54 | 93% (90d) | Does not open (95%) | 32% | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 63 | [ ] | RoboCop: Rogue City (STEAM) | 50 | 54 | 93% (90d) | Does not open (37%) | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 64 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 49 | 64 | 77% (90d) | Does not open (80%) | 41% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 65 | [ ] | Trackmania (STEAM) | 49 | 62 | 79% (90d) | Does not open (85%) | 41% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 66 | [ ] | Fortune Mill (STEAM) | 49 | 49 | 100% (90d) | Does not open (90%) | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 67 | [ ] | Scott Pilgrim vs The World (STEAM) | 49 | 49 | 100% (90d) | Does not open (83%) | 50% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 68 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 48 | 69 | 70% (90d) | Does not open (83%) | 58% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 69 | [ ] | Asphalt Legends  (STEAM) | 48 | 56 | 86% (90d) | Does not open (80%) | 47% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 70 | [ ] | DOOM 3 (STEAM) | 48 | 53 | 91% (90d) | Does not open (92%) | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 71 | [ ] | DOOM Eternal (STEAM) | 48 | 50 | 96% (90d) | Does not open (69%) | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 72 | [ ] | tModLoader (STEAM) | 47 | 54 | 87% (90d) | Does not open (86%) | 3% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 73 | [ ] | Hitman: Absolution (STEAM) | 47 | 52 | 90% (90d) | Does not open (84%) | 7% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 74 | [ ] | Aliens vs. Predator (STEAM) | 46 | 51 | 90% (90d) | No graphics (54%) | 28% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 75 | [ ] | STAR WARS™ Republic Commando (STEAM) | 46 | 48 | 96% (90d) | Does not open (80%) | 53% | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 76 | [ ] | State of Decay 2 (STEAM) | 45 | 63 | 71% (90d) | Does not open (93%) | 0% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 77 | [ ] | Split/Second (STEAM) | 45 | 49 | 92% (90d) | Does not open (80%) | 10% | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 78 | [ ] | To The Moon (GOG) | 44 | 48 | 96% (1.3.0) | Does not open (86%) | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 79 | [ ] | The Survivalists (STEAM) | 44 | 46 | 96% (90d) | Does not open (98%) | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 80 | [ ] | Mafia: Definitive Edition (GOG) | 43 | 56 | 77% (90d) | Does not open (85%) | 30% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 81 | [ ] | Diablo + Hellfire (GOG) | 43 | 49 | 88% (90d) | Does not open (64%) | 31% | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 82 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 43 | 44 | 98% (90d) | Does not open (84%) | 46% | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 83 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 41 | 45 | 91% (90d) | Does not open (71%) | 28% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 84 | [ ] | Tales of Berseria (STEAM) | 40 | 41 | 98% (90d) | Does not open (89%) | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 85 | [ ] | Need for Speed™ Rivals (STEAM) | 39 | 48 | 81% (90d) | Does not open (60%) | 44% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 86 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 39 | 40 | 98% (90d) | Does not open (67%) | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 87 | [ ] | Mafia (STEAM) | 38 | 43 | 88% (90d) | Does not open (69%) | 41% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 88 | [ ] | DJMAX RESPECT V (STEAM) | 38 | 42 | 90% (90d) | Does not open (82%) | 30% | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 89 | [ ] | Marvel's Spider-Man 2 (STEAM) | 38 | 40 | 95% (90d) | Does not open (87%) | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 90 | [ ] | GeoGuessr Steam Edition (STEAM) | 38 | 39 | 97% (90d) | No graphics (62%) | n/a | [#154](https://github.com/GameNative/gamenative-compat/issues/154) |
| 91 | [ ] | L.A. Noire (STEAM) | 37 | 44 | 84% (90d) | Does not open (100%) | 48% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 92 | [ ] | Beat Saber (STEAM) | 37 | 43 | 86% (90d) | Does not open (47%) | 32% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 93 | [ ] | ARC Raiders (STEAM) | 37 | 42 | 88% (90d) | Does not open (91%) | 0% | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 94 | [ ] | ScourgeBringer (STEAM) | 37 | 42 | 88% (90d) | Does not open (69%) | 6% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 95 | [ ] | Dragon's Dogma 2 (STEAM) | 37 | 38 | 97% (90d) | Does not open (91%) | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 96 | [ ] | Utopia Must Fall (STEAM) | 37 | 38 | 97% (90d) | Does not open (84%) | 0% | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 97 | [ ] | Barotrauma (STEAM) | 36 | 39 | 92% (90d) | Does not open (97%) | 36% | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 98 | [ ] | BIT.TRIP RUNNER (STEAM) | 36 | 38 | 95% (90d) | Does not open (61%) | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 99 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 36 | 38 | 95% (90d) | Does not open (94%) | 27% | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 100 | [ ] | Metro: Last Light Redux (STEAM) | 35 | 93 | 77% (1.3.0) | Does not open (92%) | 38% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 101 | [ ] | CARRION (GOG) | 35 | 43 | 81% (90d) | Does not open (73%) | 8% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 102 | [ ] | FINAL FANTASY VIII (STEAM) | 35 | 43 | 81% (90d) | Does not open (65%) | 55% | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 103 | [ ] | GOALS (STEAM) | 35 | 42 | 83% (90d) | Does not open (83%) | 22% | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 104 | [ ] | BattleBit Remastered (STEAM) | 35 | 39 | 90% (90d) | Does not open (61%) | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 105 | [ ] | Axiom Verge 2 (STEAM) | 35 | 36 | 97% (90d) | Does not open (57%) | 17% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 106 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 35 | 36 | 97% (90d) | No graphics (62%) | 12% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 107 | [ ] | CPM 2 (STEAM) | 34 | 42 | 81% (90d) | Does not open (88%) | 10% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 108 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 34 | 38 | 89% (90d) | Does not open (62%) | 27% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 109 | [ ] | OneShot (STEAM) | 34 | 38 | 89% (90d) | Does not open (97%) | 23% | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 110 | [ ] | Muv-Luv (STEAM) | 34 | 35 | 97% (90d) | Does not open (86%) | 37% | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 111 | [ ] | Gauntlet™  (STEAM) | 33 | 47 | 70% (90d) | Does not open (64%) | 46% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 112 | [ ] | CODE VEIN (STEAM) | 33 | 46 | 72% (90d) | Does not open (65%) | 36% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 113 | [ ] | Lost Planet: Extreme Condition (STEAM) | 33 | 41 | 80% (90d) | Does not open (77%) | 45% | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 114 | [ ] | Forza Horizon 6 (STEAM) | 33 | 34 | 97% (90d) | Does not open (58%) | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 115 | [ ] | Mass Effect (2007) (STEAM) | 32 | 38 | 84% (90d) | Does not open (81%) | 44% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 116 | [ ] | Death Stranding (EPIC) | 32 | 35 | 91% (90d) | Does not open (78%) | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 117 | [ ] | Wolfenstein 3D (STEAM) | 32 | 35 | 91% (90d) | Does not open (50%) | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 118 | [ ] | Yume Nikki (STEAM) | 31 | 54 | 70% (14d) | Does not open (90%) | 0% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 119 | [ ] | Insaniquarium! Deluxe (STEAM) | 31 | 38 | 82% (90d) | Does not open (86%) | 35% | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 120 | [ ] | Beholder (EPIC) | 31 | 36 | 86% (90d) | Does not open (65%) | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 121 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 31 | 34 | 91% (90d) | Does not open (67%) | 0% | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 122 | [ ] | Umamusume: Pretty Derby (STEAM) | 31 | 33 | 94% (90d) | Does not open (86%) | 55% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 123 | [ ] | Rayman Legends (STEAM) | 31 | 32 | 97% (90d) | Does not open (96%) | 39% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 124 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 31 | 31 | 100% (90d) | Does not open (69%) | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 125 | [ ] | Quantum Break (STEAM) | 31 | 31 | 100% (90d) | Does not open (90%) | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 126 | [ ] | Metro: Last Light Complete Edition (STEAM) | 30 | 36 | 83% (90d) | Does not open (58%) | 58% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 127 | [ ] | Far Cry 4 (STEAM) | 30 | 34 | 88% (90d) | Does not open (100%) | 27% | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 128 | [ ] | King's Bounty: The Legend (STEAM) | 30 | 34 | 88% (90d) | Does not open (100%) | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 129 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 30 | 33 | 91% (90d) | Does not open (85%) | 30% | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 130 | [ ] | Need for Speed™ (STEAM) | 30 | 32 | 94% (90d) | Does not open (69%) | 53% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 131 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 30 | 31 | 97% (90d) | Does not open (95%) | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 132 | [ ] | The Darkness II (STEAM) | 30 | 30 | 100% (90d) | Does not open (81%) | 23% | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 133 | [ ] | Magicka (STEAM) | 29 | 32 | 91% (90d) | Does not open (63%) | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 134 | [ ] | Forza Horizon 5 (STEAM) | 29 | 31 | 94% (90d) | Does not open (71%) | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 135 | [ ] | Grand Theft Auto III - The Definitive Edition (STEAM) | 29 | 29 | 100% (90d) | Does not open (92%) | 18% | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 136 | [ ] | Audiosurf (STEAM) | 28 | 39 | 72% (90d) | Does not open (46%) | 38% | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 137 | [ ] | Dark Sector (STEAM) | 28 | 37 | 76% (90d) | Does not open (68%) | 43% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 138 | [ ] | PAYDAY 2 (STEAM) | 28 | 31 | 90% (90d) | Does not open (79%) | 31% | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 139 | [ ] | Borderlands 2 RU (STEAM) | 28 | 30 | 93% (90d) | Does not open (58%) | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 140 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 28 | 30 | 93% (90d) | Does not open (77%) | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 141 | [ ] | Breath of Fire IV (STEAM) | 28 | 28 | 100% (90d) | Does not open (56%) | 19% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 142 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 28 | 28 | 100% (90d) | Does not open (68%) | 0% | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 143 | [ ] | Mirror's Edge™ (GOG) | 27 | 38 | 71% (90d) | No graphics (62%) | 44% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 144 | [ ] | The Planet Crafter (STEAM) | 27 | 32 | 84% (90d) | Does not open (55%) | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 145 | [ ] | DiRT Showdown (STEAM) | 27 | 28 | 96% (90d) | Does not open (56%) | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 146 | [ ] | Hitman: Blood Money (STEAM) | 27 | 28 | 96% (90d) | Does not open (83%) | 12% | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 147 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 27 | 28 | 96% (90d) | Does not open (81%) | 40% | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 148 | [ ] | Zuma Deluxe (STEAM) | 27 | 28 | 96% (90d) | Does not open (95%) | 36% | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 149 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 27 | 27 | 100% (90d) | Does not open (90%) | 53% | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 150 | [ ] | Subnautica 2 (STEAM) | 26 | 32 | 81% (90d) | Does not open (65%) | 54% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 151 | [ ] | Alpha Protocol (STEAM) | 26 | 30 | 87% (90d) | Does not open (57%) | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 152 | [ ] | Northgard: Definitive Edition (STEAM) | 26 | 29 | 90% (90d) | Does not open (96%) | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 153 | [ ] | Persona 5 Strikers (STEAM) | 26 | 29 | 90% (90d) | Does not open (78%) | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 154 | [ ] | AION 2 (STEAM) | 26 | 28 | 93% (90d) | Does not open (65%) | 9% | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 155 | [ ] | Isle of Reveries (STEAM) | 26 | 27 | 96% (90d) | Does not open (95%) | 33% | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 156 | [ ] | theHunter Classic (STEAM) | 26 | 26 | 100% (1.3.0) | No graphics (92%) | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 157 | [ ] | EA SPORTS FC™ 26 (STEAM) | 25 | 33 | 76% (90d) | Does not open (75%) | n/a | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 158 | [ ] | Kenshi (STEAM) | 25 | 32 | 78% (90d) | Does not open (84%) | 9% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 159 | [ ] | Knights of Pen and Paper 2 (STEAM) | 25 | 32 | 78% (90d) | Does not open (45%) | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 160 | [ ] | Singularity™ (GOG) | 25 | 30 | 83% (90d) | Does not open (100%) | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 161 | [ ] | Bionic Commando Rearmed (STEAM) | 25 | 28 | 89% (90d) | Does not open (74%) | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 162 | [ ] | Turing Complete (STEAM) | 25 | 28 | 89% (90d) | Does not open (91%) | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 163 | [ ] | Resident Evil Requiem (STEAM) | 25 | 25 | 100% (90d) | Does not open (75%) | n/a | [#210](https://github.com/GameNative/gamenative-compat/issues/210) |
| 164 | [ ] | Call of Duty® (STEAM) | 24 | 33 | 73% (90d) | Does not open (68%) | 5% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 165 | [ ] | ENDLESS Space™ 2 (STEAM) | 24 | 29 | 83% (90d) | Does not open (93%) | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 166 | [ ] | The Swapper (STEAM) | 24 | 28 | 86% (90d) | Does not open (52%) | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 167 | [ ] | They Are Billions (STEAM) | 24 | 27 | 89% (90d) | Does not open (71%) | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 168 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 23 | 31 | 74% (90d) | No graphics (57%) | 11% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 169 | [ ] | Transformers: Fall of Cybertron (STEAM) | 23 | 30 | 77% (90d) | Does not open (63%) | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 170 | [ ] | Dragon Age™ Inquisition (STEAM) | 23 | 27 | 85% (90d) | Does not open (75%) | 40% | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 171 | [ ] | SimCity 4 Deluxe (STEAM) | 23 | 27 | 85% (90d) | Does not open (82%) | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 172 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 23 | 26 | 88% (90d) | Does not open (95%) | 48% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 173 | [ ] | Peggle Nights (STEAM) | 23 | 25 | 92% (90d) | Does not open (94%) | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 174 | [ ] | Alien Breed: Impact (STEAM) | 23 | 24 | 96% (90d) | Does not open (91%) | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 175 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 23 | 24 | 96% (90d) | No graphics (53%) | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 176 | [ ] | PRAGMATA (STEAM) | 23 | 24 | 96% (90d) | Does not open (79%) | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 177 | [ ] | Euro Truck Simulator (STEAM) | 23 | 23 | 100% (90d) | Does not open (93%) | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 178 | [ ] | Gears 5 (STEAM) | 23 | 23 | 100% (90d) | Does not open (88%) | n/a | [#264](https://github.com/GameNative/gamenative-compat/issues/264) |
| 179 | [ ] | Marie's Adventure (STEAM) | 23 | 23 | 100% (90d) | Does not open (100%) | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 180 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 23 | 23 | 100% (90d) | Does not open (53%) | 10% | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 181 | [ ] | Spiral Knights (STEAM) | 23 | 23 | 100% (90d) | Does not open (72%) | n/a | [#263](https://github.com/GameNative/gamenative-compat/issues/263) |
| 182 | [ ] | SOMA (STEAM) | 22 | 30 | 73% (90d) | Does not open (79%) | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 183 | [ ] | TEKKEN 8 (STEAM) | 22 | 29 | 76% (90d) | Does not open (76%) | 50% | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 184 | [ ] | My Singing Monsters (STEAM) | 22 | 28 | 79% (90d) | Does not open (82%) | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 185 | [ ] | Half-Life: Blue Shift (STEAM) | 22 | 26 | 85% (90d) | Does not open (85%) | 18% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 186 | [ ] | Tom Clancy's Ghost Recon® Wildlands (STEAM) | 22 | 26 | 85% (90d) | Does not open (94%) | n/a | [#280](https://github.com/GameNative/gamenative-compat/issues/280) |
| 187 | [ ] | skate.™ (EPIC) | 22 | 25 | 88% (90d) | Does not open (88%) | 7% | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 188 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 22 | 24 | 92% (90d) | Does not open (61%) | 54% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 189 | [ ] | WRC 7 (STEAM) | 22 | 23 | 96% (90d) | Does not open (67%) | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 190 | [ ] | Wallachia: Reign of Dracula (STEAM) | 22 | 23 | 96% (90d) | No graphics (95%) | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 191 | [ ] | Aggelos 2 (STEAM) | 21 | 27 | 78% (90d) | No graphics (90%) | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 192 | [ ] | Beyond Good & Evil™ (GOG) | 21 | 26 | 81% (90d) | Does not open (100%) | 20% | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 193 | [ ] | Sapphire Safari (GOG) | 21 | 26 | 81% (90d) | Does not open (89%) | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 194 | [ ] | Marvel's Midnight Suns (STEAM) | 21 | 24 | 88% (90d) | Does not open (84%) | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 195 | [ ] | Wuthering Waves (STEAM) | 21 | 23 | 91% (90d) | Does not open (85%) | n/a | [#216](https://github.com/GameNative/gamenative-compat/issues/216) |
| 196 | [ ] | Mirror's Edge™ Catalyst (STEAM) | 21 | 22 | 95% (90d) | Does not open (68%) | 46% | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 197 | [ ] | Resident Evil 3 Nemesis (1999) (STEAM) | 21 | 21 | 100% (90d) | Does not open (86%) | n/a | [#273](https://github.com/GameNative/gamenative-compat/issues/273) |
| 198 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 21 | 21 | 100% (90d) | Does not open (71%) | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 199 | [ ] | Fishing Planet (STEAM) | 20 | 28 | 71% (90d) | Does not open (93%) | 33% | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 200 | [ ] | Surviving Mars (STEAM) | 20 | 26 | 77% (90d) | Does not open (92%) | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 201 | [ ] | PICO PARK:Classic Edition (STEAM) | 20 | 24 | 83% (90d) | Does not open (89%) | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 202 | [ ] | Halo: Spartan Assault (STEAM) | 20 | 23 | 87% (90d) | Does not open (82%) | 31% | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 203 | [ ] | Apex Legends (STEAM) | 20 | 22 | 91% (90d) | Does not open (72%) | n/a | [#261](https://github.com/GameNative/gamenative-compat/issues/261) |
| 204 | [ ] | Pathway (EPIC) | 20 | 21 | 95% (90d) | Does not open (61%) | n/a | [#298](https://github.com/GameNative/gamenative-compat/issues/298) |
| 205 | [ ] | The Last of Us™ Part I (STEAM) | 20 | 21 | 95% (90d) | Does not open (93%) | n/a | [#300](https://github.com/GameNative/gamenative-compat/issues/300) |
| 206 | [ ] | Grounded 2 (STEAM) | 20 | 20 | 100% (90d) | Does not open (56%) | n/a | [#317](https://github.com/GameNative/gamenative-compat/issues/317) |
| 207 | [ ] | Return to Castle Wolfenstein (STEAM) | 20 | 20 | 100% (90d) | Does not open (95%) | 25% | [#321](https://github.com/GameNative/gamenative-compat/issues/321) |
| 208 | [ ] | Beat Cop (STEAM) | 19 | 27 | 70% (90d) | Does not open (72%) | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 209 | [ ] | Dungeon Keeper™ 2 (GOG) | 19 | 26 | 73% (90d) | Does not open (100%) | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 210 | [ ] | Mafia III: Definitive Edition (STEAM) | 19 | 22 | 86% (90d) | Does not open (95%) | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 211 | [ ] | The Elder Scrolls IV: Oblivion Remastered (STEAM) | 19 | 22 | 86% (90d) | Does not open (59%) | n/a | [#312](https://github.com/GameNative/gamenative-compat/issues/312) |
| 212 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 19 | 22 | 86% (90d) | Does not open (79%) | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 213 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 21 | 90% (90d) | Does not open (82%) | 0% | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 214 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 21 | 90% (90d) | Does not open (89%) | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 215 | [ ] | Bingle Bingle (STEAM) | 19 | 20 | 95% (90d) | Does not open (80%) | n/a | [#225](https://github.com/GameNative/gamenative-compat/issues/225) |
| 216 | [ ] | GT Legends (STEAM) | 19 | 20 | 95% (90d) | Does not open (89%) | n/a | [#364](https://github.com/GameNative/gamenative-compat/issues/364) |
| 217 | [ ] | Melatonin (STEAM) | 19 | 20 | 95% (90d) | Does not open (59%) | 36% | [#272](https://github.com/GameNative/gamenative-compat/issues/272) |
| 218 | [ ] | No More Room in Hell (STEAM) | 19 | 20 | 95% (90d) | Does not open (94%) | n/a | [#365](https://github.com/GameNative/gamenative-compat/issues/365) |
| 219 | [ ] | Rayman Legends (EPIC) | 19 | 20 | 95% (90d) | Does not open (92%) | n/a | [#286](https://github.com/GameNative/gamenative-compat/issues/286) |
| 220 | [ ] | Zenless Zone Zero (STEAM) | 19 | 20 | 95% (90d) | Does not open (76%) | n/a | [#369](https://github.com/GameNative/gamenative-compat/issues/369) |
| 221 | [ ] | Fogpiercer (STEAM) | 18 | 25 | 72% (90d) | Does not open (78%) | n/a | [#303](https://github.com/GameNative/gamenative-compat/issues/303) |
| 222 | [ ] | Hitman 2: Silent Assassin (STEAM) | 18 | 23 | 78% (90d) | Does not open (83%) | 47% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 223 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 18 | 23 | 78% (90d) | Does not open (100%) | 37% | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 224 | [ ] | Yakuza 0 (GOG) | 18 | 23 | 78% (90d) | Does not open (67%) | 46% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 225 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 18 | 22 | 82% (90d) | Controller issues (100%) | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 226 | [ ] | We Were Here Together (EPIC) | 18 | 22 | 82% (90d) | Does not open (82%) | n/a | [#374](https://github.com/GameNative/gamenative-compat/issues/374) |
| 227 | [ ] | Bright Memory (STEAM) | 18 | 21 | 86% (90d) | No graphics (83%) | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 228 | [ ] | Lay of the Land (STEAM) | 18 | 20 | 90% (90d) | No graphics (61%) | n/a | [#477](https://github.com/GameNative/gamenative-compat/issues/477) |
| 229 | [ ] | Carnal Instinct (STEAM) | 17 | 24 | 71% (90d) | Does not open (57%) | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 230 | [ ] | SlashZero Demo (STEAM) | 17 | 23 | 74% (90d) | Does not open (75%) | 40% | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 231 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 17 | 22 | 77% (90d) | Does not open (87%) | 43% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 232 | [ ] | Clive Barker's Undying (GOG) | 17 | 20 | 85% (90d) | Does not open (75%) | n/a | [#388](https://github.com/GameNative/gamenative-compat/issues/388) |
| 233 | [ ] | GRADIUS origin collection (STEAM) | 17 | 20 | 85% (90d) | Controller issues (71%) | n/a | [#479](https://github.com/GameNative/gamenative-compat/issues/479) |
| 234 | [ ] | NBA 2K26 (STEAM) | 17 | 20 | 85% (90d) | Does not open (82%) | n/a | [#384](https://github.com/GameNative/gamenative-compat/issues/384) |
| 235 | [ ] | Rune Factory 5 (STEAM) | 17 | 20 | 85% (90d) | Does not open (82%) | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 236 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 16 | 23 | 70% (90d) | No graphics (56%) | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 237 | [ ] | Legend of Grimrock 2 (STEAM) | 16 | 23 | 70% (90d) | Does not open (92%) | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 238 | [ ] | Re-Volt (STEAM) | 16 | 22 | 73% (90d) | Controller issues (71%) | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 239 | [ ] | Spark the Electric Jester (STEAM) | 16 | 22 | 73% (90d) | Does not open (62%) | 52% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 240 | [ ] | Content Warning (STEAM) | 16 | 21 | 76% (90d) | Does not open (53%) | n/a | [#241](https://github.com/GameNative/gamenative-compat/issues/241) |
| 241 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 21 | 76% (90d) | Does not open (82%) | 50% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 242 | [ ] | Bejeweled 2 Deluxe (STEAM) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#329](https://github.com/GameNative/gamenative-compat/issues/329) |
| 243 | [ ] | EVE Online (STEAM) | 16 | 20 | 80% (90d) | No graphics (57%) | 55% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 244 | [ ] | F.E.A.R. 2: Project Origin + Reborn (GOG) | 16 | 20 | 80% (90d) | Does not open (100%) | n/a | [#478](https://github.com/GameNative/gamenative-compat/issues/478) |
| 245 | [ ] | Genshin Impact (EPIC) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#326](https://github.com/GameNative/gamenative-compat/issues/326) |
| 246 | [ ] | Sacred Gold (STEAM) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 247 | [ ] | DayZ (STEAM) | 15 | 21 | 71% (90d) | Does not open (56%) | 54% | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 248 | [ ] | Fallout Classic (GOG) | 15 | 21 | 71% (90d) | Does not open (71%) | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 249 | [ ] | Smushi Come Home (GOG) | 15 | 21 | 71% (90d) | Does not open (57%) | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 250 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 15 | 21 | 71% (90d) | Does not open (70%) | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 251 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (90d) | No graphics (71%) | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 252 | [ ] | Make Way (EPIC) | 15 | 20 | 75% (90d) | Does not open (79%) | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |

## Probably does not work (75)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | Garry's Mod (STEAM) | 197 | 312 | 68% (1.3.0) | Does not open (79%) | 59% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 2 | [ ] | Metro 2033 Redux (STEAM) | 157 | 345 | 69% (1.3.0) | Does not open (70%) | 49% |  |
| 3 | [ ] | Prototype (STEAM) | 150 | 214 | 52% (1.3.0) | Does not open (76%) | 46% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 4 | [ ] | Geometry Dash (STEAM) | 141 | 422 | 64% (1.3.0) | Does not open (71%) | 39% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 5 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 135 | 170 | 54% (1.3.0) | Does not open (92%) | 39% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 6 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 120 | 183 | 66% (90d) | Does not open (82%) | n/a |  |
| 7 | [ ] | VRChat (STEAM) | 91 | 139 | 52% (1.3.0) | Does not open (65%) | 40% |  |
| 8 | [ ] | Gorilla Tag (STEAM) | 72 | 121 | 68% (1.3.0) | Does not open (70%) | 23% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 9 | [ ] | Firewatch (STEAM) | 65 | 114 | 57% (90d) | Does not open (90%) | 52% |  |
| 10 | [ ] | Hollow Knight: Silksong (GOG) | 65 | 104 | 63% (90d) | Does not open (71%) | 48% |  |
| 11 | [ ] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 53 | 89 | 60% (90d) | Does not open (62%) | 59% |  |
| 12 | [ ] | Oxygen Not Included (STEAM) | 53 | 86 | 62% (90d) | Does not open (76%) | 52% |  |
| 13 | [ ] | Breathedge (STEAM) | 51 | 75 | 68% (90d) | Does not open (61%) | 43% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 14 | [ ] | VALORANT (EPIC) | 44 | 67 | 66% (90d) | Does not open (86%) | 17% |  |
| 15 | [ ] | Plague Inc: Evolved (STEAM) | 44 | 66 | 67% (90d) | Does not open (67%) | 57% |  |
| 16 | [ ] | Frostpunk (STEAM) | 41 | 66 | 62% (90d) | No graphics (77%) | 44% |  |
| 17 | [ ] | Fallout (GOG) | 40 | 61 | 66% (90d) | Does not open (72%) | 49% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 18 | [ ] | Age of Empires II (2013) (STEAM) | 39 | 67 | 58% (90d) | Does not open (46%) | 53% |  |
| 19 | [ ] | Grim Dawn (GOG) | 38 | 62 | 61% (90d) | Does not open (65%) | 50% | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 20 | [ ] | XCOM 2 (STEAM) | 35 | 54 | 65% (90d) | Does not open (57%) | n/a |  |
| 21 | [ ] | Deponia (STEAM) | 33 | 61 | 54% (90d) | Does not open (48%) | 57% |  |
| 22 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 32 | 57 | 56% (90d) | Does not open (95%) | 43% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 23 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 31 | 56 | 55% (90d) | Does not open (66%) | 46% |  |
| 24 | [ ] | Sol Cesto (STEAM) | 31 | 49 | 63% (90d) | Does not open (68%) | 50% |  |
| 25 | [ ] | Mafia II (Classic) (GOG) | 31 | 45 | 69% (90d) | Does not open (96%) | 25% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 26 | [ ] | Soul's Remnant (STEAM) | 27 | 49 | 55% (90d) | Does not open (55%) | n/a |  |
| 27 | [ ] | Lucid Blocks (STEAM) | 26 | 45 | 58% (90d) | Does not open (82%) | 59% |  |
| 28 | [ ] | Crazy Taxi (STEAM) | 25 | 43 | 58% (90d) | Does not open (63%) | 55% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 29 | [ ] | Chained Echoes (GOG) | 24 | 48 | 50% (90d) | Does not open (62%) | 48% |  |
| 30 | [ ] | Strider (STEAM) | 24 | 37 | 65% (90d) | Does not open (100%) | 38% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 31 | [ ] | Baldur's Gate: Enhanced Edition (STEAM) | 23 | 46 | 50% (90d) | Does not open (61%) | 21% |  |
| 32 | [ ] | Invisible, Inc. (STEAM) | 22 | 38 | 58% (90d) | Does not open (65%) | 55% |  |
| 33 | [ ] | Cities: Skylines (STEAM) | 22 | 33 | 67% (90d) | Does not open (67%) | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 34 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 21 | 31 | 68% (90d) | Does not open (95%) | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 35 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 20 | 34 | 59% (90d) | Does not open (56%) | 47% |  |
| 36 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 20 | 32 | 63% (90d) | Does not open (81%) | 10% |  |
| 37 | [ ] | Warhammer 40,000: Boltgun (GOG) | 19 | 29 | 66% (90d) | Does not open (92%) | 50% |  |
| 38 | [ ] | Turnip Boy Robs a Bank (EPIC) | 19 | 28 | 68% (90d) | Does not open (65%) | 47% | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 39 | [ ] | Need for Speed: Undercover (STEAM) | 18 | 29 | 62% (90d) | Does not open (93%) | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 40 | [ ] | Another World: 20th Anniversary Edition (GOG) | 18 | 28 | 64% (90d) | Does not open (67%) | 50% |  |
| 41 | [ ] | No More Heroes (STEAM) | 17 | 33 | 52% (90d) | No graphics (71%) | 57% |  |
| 42 | [ ] | Shank 2 (STEAM) | 17 | 30 | 57% (90d) | Does not open (82%) | n/a |  |
| 43 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 17 | 27 | 63% (90d) | Does not open (80%) | n/a |  |
| 44 | [ ] | Assassin's Creed Odyssey (STEAM) | 17 | 26 | 65% (90d) | Does not open (77%) | n/a | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 45 | [ ] | Railway Chai Wala (STEAM) | 16 | 32 | 50% (90d) | Does not open (64%) | n/a |  |
| 46 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 16 | 29 | 55% (90d) | Does not open (87%) | 31% |  |
| 47 | [ ] | Guacamelee! Gold Edition (STEAM) | 16 | 27 | 59% (90d) | Does not open (93%) | n/a | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 48 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 26 | 62% (90d) | Directx error (57%) | n/a |  |
| 49 | [ ] | War of Dots (STEAM) | 16 | 25 | 64% (90d) | Does not open (75%) | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 50 | [ ] | Race The Sun (STEAM) | 15 | 30 | 50% (90d) | No graphics (92%) | 54% |  |
| 51 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 15 | 29 | 52% (90d) | Does not open (64%) | 0% |  |
| 52 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 15 | 26 | 58% (90d) | Does not open (85%) | 51% |  |
| 53 | [ ] | Ys: Memories of Celceta (STEAM) | 15 | 24 | 63% (90d) | No graphics (45%) | 33% |  |
| 54 | [ ] | Blood Omen: Legacy of Kain (GOG) | 15 | 22 | 68% (90d) | Does not open (64%) | 47% |  |
| 55 | [ ] | Alan Wake's American Nightmare (EPIC) | 14 | 26 | 54% (90d) | Does not open (85%) | 50% |  |
| 56 | [ ] | Odallus: The Dark Call (STEAM) | 14 | 26 | 54% (90d) | No graphics (54%) | n/a | [#337](https://github.com/GameNative/gamenative-compat/issues/337) |
| 57 | [ ] | Blaster Master Zero (STEAM) | 14 | 25 | 56% (90d) | Does not open (64%) | 29% |  |
| 58 | [ ] | Katana ZERO (GOG) | 14 | 25 | 56% (90d) | Does not open (85%) | 36% |  |
| 59 | [ ] | Evenicle (STEAM) | 14 | 23 | 61% (90d) | Graphics glitches (71%) | n/a |  |
| 60 | [ ] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 13 | 24 | 54% (90d) | Does not open (100%) | 17% |  |
| 61 | [ ] | Look Outside (GOG) | 13 | 24 | 54% (90d) | Does not open (100%) | n/a |  |
| 62 | [ ] | Asterigos: Curse of the Stars (STEAM) | 13 | 23 | 57% (90d) | Graphics glitches (50%) | n/a |  |
| 63 | [ ] | Trials Survivors (STEAM) | 13 | 23 | 57% (90d) | Does not open (67%) | n/a |  |
| 64 | [ ] | Drop Duchy (EPIC) | 13 | 21 | 62% (90d) | Does not open (100%) | 25% |  |
| 65 | [ ] | Human Resource Machine (EPIC) | 13 | 21 | 62% (90d) | No graphics (70%) | 55% |  |
| 66 | [ ] | Secret of Mana (STEAM) | 13 | 21 | 62% (90d) | Graphics glitches (58%) | 50% |  |
| 67 | [ ] | The Stanley Parable (STEAM) | 13 | 21 | 62% (90d) | Does not open (89%) | 53% |  |
| 68 | [ ] | Buck Up And Drive! (STEAM) | 13 | 20 | 65% (90d) | Does not open (67%) | n/a |  |
| 69 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (90d) | No graphics (50%) | n/a |  |
| 70 | [ ] | A Plague Tale: Innocence (GOG) | 12 | 23 | 52% (90d) | Does not open (91%) | 53% |  |
| 71 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 12 | 22 | 55% (90d) | Does not open (73%) | n/a |  |
| 72 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (90d) | Does not open (80%) | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 73 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (90d) | Does not open (82%) | n/a |  |
| 74 | [ ] | Crying Suns (EPIC) | 11 | 22 | 50% (90d) | No graphics (57%) | n/a |  |
| 75 | [ ] | DYNASTY WARRIORS: ORIGINS (STEAM) | 10 | 20 | 50% (90d) | Does not open (60%) | n/a |  |

## Works, but the first launch usually fails (356)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 1305 | 1655 | 75% (1.3.0) | Does not open (83%) | 77% |  |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 563 | 714 | 78% (1.3.0) | Does not open (64%) | 91% |  |
| 3 | [ ] | Grim Dawn (STEAM) | 557 | 613 | 63% (1.3.0) | Does not open (74%) | 61% |  |
| 4 | [ ] | Terraria (STEAM) | 486 | 761 | 58% (1.3.0) | No graphics (51%) | 75% |  |
| 5 | [ ] | KINGDOM HEARTS -HD 1.5+2.5 ReMIX- (STEAM) | 476 | 950 | 55% (1.3.0) | Does not open (79%) | 94% |  |
| 6 | [ ] | No Man's Sky (STEAM) | 367 | 641 | 54% (1.3.0) | Controller issues (61%) | 85% |  |
| 7 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 366 | 548 | 68% (1.3.0) | Does not open (55%) | 83% |  |
| 8 | [ ] | Half-Life (STEAM) | 353 | 620 | 51% (1.3.0) | Does not open (58%) | 76% |  |
| 9 | [ ] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 253 | 295 | 86% (90d) | Does not open (87%) | 67% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 10 | [ ] | Cyberpunk 2077 (STEAM) | 247 | 432 | 52% (1.3.0) | Does not open (67%) | 77% |  |
| 11 | [ ] | Welcome to Elderfield (STEAM) | 236 | 282 | 61% (1.3.0) | Does not open (72%) | 73% |  |
| 12 | [ ] | Grand Theft Auto V Legacy (STEAM) | 229 | 290 | 69% (1.3.0) | Does not open (89%) | 78% |  |
| 13 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 225 | 317 | 71% (90d) | Does not open (61%) | 88% |  |
| 14 | [ ] | BeamNG.drive (STEAM) | 213 | 260 | 88% (1.3.0) | Does not open (83%) | 93% |  |
| 15 | [ ] | Palworld (STEAM) | 205 | 402 | 53% (1.3.0) | Does not open (71%) | 87% |  |
| 16 | [ ] | OMORI (STEAM) | 203 | 245 | 83% (90d) | Does not open (64%) | 82% |  |
| 17 | [ ] | Devil May Cry HD Collection (STEAM) | 202 | 283 | 76% (1.3.0) | Does not open (86%) | 76% |  |
| 18 | [ ] | DRAGON BALL FighterZ (STEAM) | 202 | 233 | 71% (1.3.0) | Does not open (89%) | 62% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 19 | [ ] | ELDEN RING (STEAM) | 199 | 296 | 69% (1.3.0) | Does not open (86%) | 72% |  |
| 20 | [ ] | MONSTER HUNTER RISE (STEAM) | 198 | 499 | 51% (1.3.0) | Does not open (82%) | 69% |  |
| 21 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 192 | 361 | 60% (1.3.0) | Does not open (57%) | 82% |  |
| 22 | [ ] | DREDGE (EPIC) | 172 | 219 | 62% (1.3.0) | Does not open (66%) | 85% |  |
| 23 | [ ] | Rocket League® (EPIC) | 155 | 258 | 53% (1.3.0) | Does not open (74%) | 74% |  |
| 24 | [ ] | Noita (STEAM) | 147 | 222 | 57% (1.3.0) | Does not open (54%) | 76% |  |
| 25 | [ ] | Monster Hunter: World (STEAM) | 144 | 273 | 55% (1.3.0) | No graphics (55%) | 83% |  |
| 26 | [ ] | Team Fortress 2 (STEAM) | 143 | 236 | 65% (1.3.0) | Does not open (68%) | 80% |  |
| 27 | [ ] | Borderlands 2 (EPIC) | 143 | 169 | 81% (1.3.0) | Does not open (82%) | 61% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 28 | [ ] | Castlevania Advance Collection (STEAM) | 133 | 204 | 71% (1.3.0) | Controller issues (95%) | 97% |  |
| 29 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 132 | 151 | 90% (1.3.0) | Does not open (86%) | 77% |  |
| 30 | [ ] | Far Cry® 3 (STEAM) | 128 | 143 | 90% (90d) | Does not open (82%) | 67% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 31 | [ ] | Minecraft Dungeons II (STEAM) | 125 | 143 | 87% (90d) | Does not open (82%) | 64% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 32 | [ ] | Castlevania Dominus Collection (STEAM) | 122 | 179 | 77% (1.3.0) | Controller issues (92%) | 98% |  |
| 33 | [ ] | Devil May Cry 5 (STEAM) | 120 | 187 | 68% (1.3.0) | Does not open (82%) | 67% |  |
| 34 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 120 | 168 | 79% (1.3.0) | Does not open (76%) | 64% |  |
| 35 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 120 | 152 | 68% (1.3.0) | Does not open (71%) | 60% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 36 | [ ] | Fallout: New Vegas (EPIC) | 118 | 144 | 73% (1.3.0) | Does not open (58%) | 92% |  |
| 37 | [ ] | Touhou Koumakyou: New Classic - the Embodiment of Scarlet Devil (STEAM) | 117 | 181 | 65% (90d) | Does not open (78%) | 81% |  |
| 38 | [ ] | Cave Story+ (STEAM) | 117 | 129 | 91% (90d) | Does not open (64%) | 94% |  |
| 39 | [ ] | The Witcher: Enhanced Edition (STEAM) | 112 | 129 | 87% (90d) | Does not open (60%) | 63% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 40 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 107 | 143 | 75% (90d) | Does not open (85%) | 86% |  |
| 41 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 106 | 155 | 65% (1.3.0) | Does not open (74%) | 76% |  |
| 42 | [ ] | Aniimo (STEAM) | 106 | 144 | 75% (1.3.0) | Does not open (76%) | 91% |  |
| 43 | [ ] | Moonstone Island (STEAM) | 104 | 137 | 76% (90d) | Controller issues (57%) | 87% |  |
| 44 | [ ] | Happy Wheels (STEAM) | 96 | 116 | 83% (90d) | No graphics (53%) | 80% |  |
| 45 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 92 | 120 | 77% (90d) | Controller issues (85%) | 97% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 46 | [ ] | Fallout: New Vegas PCR (STEAM) | 91 | 121 | 75% (90d) | Does not open (89%) | 69% |  |
| 47 | [ ] | Sovereign Tower (STEAM) | 86 | 139 | 62% (90d) | Does not open (84%) | 84% |  |
| 48 | [ ] | Vital Shell (STEAM) | 86 | 130 | 66% (90d) | Does not open (51%) | 85% |  |
| 49 | [ ] | STEINS;GATE (STEAM) | 86 | 119 | 72% (90d) | Does not open (90%) | 91% |  |
| 50 | [ ] | Hogwarts Legacy (STEAM) | 84 | 145 | 52% (1.3.0) | Does not open (59%) | 66% |  |
| 51 | [ ] | Cry of Fear (STEAM) | 81 | 161 | 72% (1.3.0) | Does not open (51%) | 85% |  |
| 52 | [ ] | Detroit: Become Human (STEAM) | 77 | 80 | 96% (90d) | Does not open (71%) | 61% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 53 | [ ] | The Sims™ 4 (STEAM) | 75 | 95 | 79% (90d) | Does not open (88%) | 68% |  |
| 54 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 74 | 124 | 60% (90d) | Controller issues (59%) | 94% |  |
| 55 | [ ] | Sid Meier's Civilization VI (STEAM) | 73 | 125 | 56% (1.3.0) | Does not open (70%) | 90% |  |
| 56 | [ ] | Sol Cesto (EPIC) | 73 | 77 | 95% (90d) | Does not open (78%) | 73% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 57 | [ ] | Antivirus Survivors 2003 Professional (STEAM) | 72 | 106 | 68% (90d) | Does not open (60%) | 92% |  |
| 58 | [ ] | Ballionaire (STEAM) | 71 | 109 | 50% (1.3.0) | Does not open (77%) | 96% |  |
| 59 | [ ] | Darksiders (STEAM) | 71 | 86 | 83% (90d) | Does not open (68%) | 88% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 60 | [ ] | Alabaster Dawn (STEAM) | 70 | 126 | 56% (90d) | Controller issues (52%) | 91% |  |
| 61 | [ ] | Disgaea 5 Complete (STEAM) | 70 | 84 | 83% (90d) | Does not open (75%) | 98% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 62 | [ ] | American Truck Simulator (STEAM) | 68 | 111 | 72% (1.3.0) | Does not open (74%) | 79% |  |
| 63 | [ ] | Fallout (STEAM) | 68 | 106 | 64% (90d) | Does not open (70%) | 73% |  |
| 64 | [ ] | Dota 2 (STEAM) | 68 | 104 | 59% (1.3.0) | Does not open (80%) | 72% |  |
| 65 | [ ] | Dungeons & Degenerate Gamblers (STEAM) | 68 | 93 | 54% (1.3.0) | Does not open (90%) | 99% |  |
| 66 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 67 | 105 | 64% (90d) | Does not open (72%) | 72% |  |
| 67 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 67 | 78 | 95% (1.3.0) | Does not open (88%) | 96% |  |
| 68 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 66 | 122 | 52% (1.3.0) | Does not open (67%) | 63% |  |
| 69 | [ ] | Mega Man Zero/ZX Legacy Collection (STEAM) | 66 | 95 | 69% (90d) | Does not open (83%) | 80% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 70 | [ ] | Gunfire Reborn (STEAM) | 66 | 72 | 92% (90d) | Does not open (81%) | 94% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 71 | [ ] | Cyberpunk 2077 (GOG) | 65 | 81 | 80% (90d) | Does not open (76%) | 77% |  |
| 72 | [ ] | Call of Juarez Gunslinger (STEAM) | 65 | 80 | 81% (90d) | Does not open (90%) | 75% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 73 | [ ] | MIO: Memories in Orbit (STEAM) | 64 | 119 | 66% (1.3.0) | Graphics glitches (53%) | 96% |  |
| 74 | [ ] | Sonic Lost World (STEAM) | 64 | 108 | 59% (90d) | No graphics (61%) | 86% |  |
| 75 | [ ] | Fable - The Lost Chapters (STEAM) | 64 | 102 | 52% (1.3.0) | Graphics glitches (54%) | 79% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 76 | [ ] | Poppy Playtime (STEAM) | 63 | 111 | 50% (1.3.0) | Does not open (68%) | 80% |  |
| 77 | [ ] | Borderlands: The Pre-Sequel (STEAM) | 63 | 89 | 71% (90d) | Does not open (77%) | 64% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 78 | [ ] | Red Dead Redemption 2 (STEAM) | 62 | 82 | 63% (1.3.0) | Does not open (98%) | 82% |  |
| 79 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 61 | 84 | 58% (1.3.0) | Does not open (48%) | 90% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 80 | [ ] | A Plague Tale: Innocence (STEAM) | 60 | 63 | 95% (90d) | Does not open (88%) | 76% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 81 | [ ] | The Binding of Isaac (STEAM) | 59 | 134 | 65% (1.3.0) | Controller issues (91%) | 94% |  |
| 82 | [ ] | Big Walk (STEAM) | 58 | 90 | 64% (90d) | Does not open (67%) | 82% |  |
| 83 | [ ] | Call of Duty: World at War (STEAM) | 58 | 83 | 70% (90d) | Does not open (42%) | 74% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 84 | [ ] | Borderlands 3 (STEAM) | 58 | 78 | 74% (90d) | Does not open (91%) | 94% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 85 | [ ] | Mini Motorways (STEAM) | 57 | 99 | 58% (90d) | Does not open (76%) | 63% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 86 | [ ] | Starbound (STEAM) | 57 | 87 | 54% (1.3.0) | Does not open (68%) | 72% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 87 | [ ] | Deskrawl: Idle ARPG (STEAM) | 57 | 68 | 86% (1.3.0) | Does not open (60%) | 79% |  |
| 88 | [ ] | Dead by Daylight (STEAM) | 57 | 62 | 92% (90d) | Does not open (83%) | 81% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 89 | [ ] | eFootball™ (STEAM) | 56 | 84 | 67% (90d) | Does not open (54%) | 76% |  |
| 90 | [ ] | Sonic Generations (STEAM) | 56 | 65 | 86% (90d) | Does not open (69%) | 63% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 91 | [ ] | Prey (STEAM) | 55 | 93 | 59% (90d) | Does not open (63%) | 85% |  |
| 92 | [ ] | The Secret of Monkey Island: Special Edition (STEAM) | 55 | 86 | 64% (90d) | Does not open (92%) | 74% |  |
| 93 | [ ] | Grand Theft Auto V (EPIC) | 55 | 61 | 95% (1.3.0) | Does not open (91%) | 83% |  |
| 94 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 55 | 59 | 93% (90d) | Does not open (83%) | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 95 | [ ] | Resident Evil 6 (STEAM) | 54 | 129 | 73% (1.3.0) | Does not open (57%) | 89% |  |
| 96 | [ ] | Sonic Adventure DX (STEAM) | 54 | 89 | 61% (90d) | Does not open (88%) | 63% |  |
| 97 | [ ] | TBH: Task Bar Hero (STEAM) | 54 | 84 | 64% (90d) | Does not open (74%) | 94% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 98 | [ ] | MapleStory (STEAM) | 54 | 56 | 92% (1.3.0) | Does not open (76%) | 74% |  |
| 99 | [ ] | Path of Exile (STEAM) | 53 | 62 | 85% (90d) | Does not open (91%) | 86% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 100 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 52 | 76 | 76% (1.3.0) | Does not open (60%) | 64% |  |
| 101 | [ ] | Vampire Survivors (EPIC) | 52 | 74 | 70% (90d) | Does not open (63%) | 64% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 102 | [ ] | Until Then (STEAM) | 51 | 90 | 57% (90d) | Does not open (77%) | 96% |  |
| 103 | [ ] | A Plague Tale: Innocence (EPIC) | 51 | 87 | 59% (90d) | Does not open (71%) | 89% |  |
| 104 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 51 | 59 | 86% (90d) | Does not open (80%) | 82% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 105 | [ ] | 7 Days to Die (STEAM) | 50 | 108 | 56% (1.3.0) | Does not open (74%) | 71% |  |
| 106 | [ ] | Ace Attorney Investigations Collection (STEAM) | 50 | 80 | 63% (90d) | Does not open (96%) | 93% |  |
| 107 | [ ] | The Bazaar (STEAM) | 50 | 80 | 63% (90d) | Does not open (71%) | 87% |  |
| 108 | [ ] | Last Epoch (STEAM) | 50 | 73 | 72% (1.3.0) | Does not open (80%) | 100% |  |
| 109 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 50 | 64 | 78% (90d) | Does not open (90%) | 62% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 110 | [ ] | Marvel’s Spider-Man Remastered (STEAM) | 49 | 120 | 55% (1.3.0) | Does not open (46%) | 62% |  |
| 111 | [ ] | Guildrun Demo (STEAM) | 49 | 69 | 71% (90d) | No graphics (66%) | 70% |  |
| 112 | [ ] | Dead Space (STEAM) | 49 | 62 | 79% (90d) | Does not open (54%) | 78% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 113 | [ ] | Sheepy: A Short Adventure (STEAM) | 49 | 59 | 83% (90d) | Does not open (52%) | 80% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 114 | [ ] | Darkest Dungeon® (EPIC) | 48 | 87 | 56% (1.3.0) | Does not open (64%) | 61% |  |
| 115 | [ ] | Sleeping Dogs™ (STEAM) | 48 | 55 | 87% (90d) | Does not open (87%) | 77% | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 116 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 75 | 63% (90d) | Controller issues (54%) | 95% |  |
| 117 | [ ] | Watch_Dogs 2 (STEAM) | 47 | 52 | 90% (90d) | Does not open (97%) | 60% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 118 | [ ] | Moonlighter (EPIC) | 47 | 51 | 100% (1.3.0) | No graphics (79%) | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 119 | [ ] | Deadlock (STEAM) | 46 | 67 | 70% (1.3.0) | Does not open (44%) | 94% |  |
| 120 | [ ] | Rivals of Aether II (STEAM) | 46 | 67 | 69% (90d) | Does not open (54%) | 74% |  |
| 121 | [ ] | Tomb Raider: Anniversary (STEAM) | 45 | 66 | 68% (90d) | Does not open (95%) | 64% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 122 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 44 | 78 | 56% (90d) | Controller issues (53%) | 89% |  |
| 123 | [ ] | Resident Evil 7 Biohazard (STEAM) | 44 | 71 | 69% (1.3.0) | Does not open (77%) | 83% |  |
| 124 | [ ] | Aggelos (STEAM) | 44 | 58 | 76% (90d) | No graphics (78%) | 95% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 125 | [ ] | Digimon World: Next Order (STEAM) | 43 | 83 | 52% (90d) | Controller issues (85%) | 95% |  |
| 126 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 43 | 46 | 93% (90d) | Does not open (95%) | 64% | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 127 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 42 | 77 | 71% (1.3.0) | Controller issues (47%) | 89% |  |
| 128 | [ ] | Street Fighter™ 6 (STEAM) | 42 | 68 | 62% (90d) | Does not open (86%) | 84% |  |
| 129 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 42 | 63 | 67% (90d) | Does not open (73%) | 69% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 130 | [ ] | FINAL FANTASY VII (2013) (STEAM) | 42 | 60 | 70% (90d) | Does not open (83%) | 81% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 131 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 41 | 68 | 60% (90d) | Does not open (66%) | 78% |  |
| 132 | [ ] | Amnesia: The Dark Descent (STEAM) | 40 | 75 | 53% (90d) | Does not open (84%) | 75% |  |
| 133 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 40 | 41 | 98% (90d) | Does not open (62%) | 86% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 134 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 39 | 74 | 53% (90d) | No graphics (83%) | 100% |  |
| 135 | [ ] | Sonic Origins (STEAM) | 39 | 70 | 56% (90d) | Does not open (71%) | 88% |  |
| 136 | [ ] | Capcom Arcade Stadium (STEAM) | 39 | 48 | 81% (90d) | Does not open (84%) | 76% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 137 | [ ] | CrossCode (GOG) | 38 | 42 | 90% (90d) | Does not open (78%) | 73% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 138 | [ ] | Monster Hunter Wilds (STEAM) | 38 | 39 | 97% (90d) | Does not open (61%) | 79% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 139 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 69 | 54% (90d) | Does not open (68%) | 89% |  |
| 140 | [ ] | Forza Horizon 4 (STEAM) | 37 | 53 | 70% (90d) | Does not open (45%) | 87% |  |
| 141 | [ ] | Elite Dangerous (STEAM) | 37 | 40 | 93% (90d) | Does not open (76%) | 69% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 142 | [ ] | Fallout 3 (STEAM) | 36 | 72 | 50% (1.3.0) | Does not open (47%) | 93% |  |
| 143 | [ ] | Hearts of Iron IV (STEAM) | 36 | 63 | 57% (90d) | Does not open (74%) | 67% |  |
| 144 | [ ] | Supermarket Together (STEAM) | 36 | 50 | 72% (90d) | Does not open (75%) | 69% |  |
| 145 | [ ] | Street Fighter 30th Anniversary Collection (STEAM) | 35 | 68 | 51% (90d) | Does not open (97%) | 65% |  |
| 146 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 35 | 41 | 85% (90d) | No graphics (69%) | 80% | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 147 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 35 | 40 | 88% (90d) | Does not open (69%) | 60% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 148 | [ ] | SurrounDead (STEAM) | 34 | 66 | 52% (90d) | Controller issues (63%) | 94% |  |
| 149 | [ ] | SnowRunner (STEAM) | 34 | 48 | 71% (90d) | Does not open (96%) | 89% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 150 | [ ] | Max Payne (STEAM) | 33 | 59 | 56% (90d) | No graphics (45%) | 93% |  |
| 151 | [ ] | Hero Siege (STEAM) | 33 | 57 | 58% (90d) | Graphics glitches (52%) | 64% |  |
| 152 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 33 | 54 | 61% (90d) | Controller issues (64%) | 74% |  |
| 153 | [ ] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 53 | 62% (90d) | Controller issues (84%) | 80% |  |
| 154 | [ ] | Capcom Fighting Collection 2 (STEAM) | 33 | 49 | 67% (90d) | Does not open (78%) | 87% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 155 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 33 | 46 | 72% (90d) | Controller issues (88%) | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 156 | [ ] | Romestead (STEAM) | 33 | 44 | 75% (90d) | Does not open (67%) | 77% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 157 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 33 | 43 | 77% (90d) | Controller issues (63%) | 89% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 158 | [ ] | Russian Fishing 4 (STEAM) | 33 | 39 | 85% (90d) | Does not open (68%) | 75% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 159 | [ ] | Hotline Miami (GOG) | 33 | 38 | 87% (90d) | Does not open (94%) | 67% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 160 | [ ] | COCOON (STEAM) | 32 | 62 | 52% (90d) | Directx error (50%) | 90% |  |
| 161 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 32 | 57 | 75% (1.3.0) | Does not open (48%) | 67% |  |
| 162 | [ ] | Rocket League (STEAM) | 32 | 53 | 60% (90d) | Does not open (74%) | 70% |  |
| 163 | [ ] | Earthion (STEAM) | 32 | 52 | 62% (90d) | Controller issues (90%) | 100% |  |
| 164 | [ ] | Counter-Strike:Global Offensive (STEAM) | 32 | 50 | 64% (90d) | Does not open (78%) | 78% |  |
| 165 | [ ] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 32 | 48 | 67% (90d) | Does not open (85%) | 87% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 166 | [ ] | Palia (STEAM) | 32 | 44 | 73% (90d) | Does not open (68%) | 76% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 167 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 32 | 37 | 86% (90d) | Does not open (73%) | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 168 | [ ] | Red Dead Redemption (STEAM) | 32 | 36 | 89% (90d) | Does not open (95%) | 90% |  |
| 169 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 31 | 60 | 52% (90d) | Does not open (73%) | 88% |  |
| 170 | [ ] | Mortal Kombat X (STEAM) | 31 | 57 | 54% (90d) | Does not open (55%) | 85% |  |
| 171 | [ ] | Resident Evil Village (STEAM) | 31 | 53 | 58% (90d) | Does not open (67%) | 90% |  |
| 172 | [ ] | Grand Theft Auto III (STEAM) | 31 | 47 | 66% (90d) | Does not open (52%) | 79% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 173 | [ ] | Tower and Sword of Succubus (STEAM) | 31 | 46 | 67% (90d) | No graphics (81%) | 100% |  |
| 174 | [ ] | Nioh: Complete Edition (STEAM) | 31 | 42 | 74% (90d) | Does not open (56%) | 95% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 175 | [ ] | Super Animal Royale (STEAM) | 31 | 41 | 76% (90d) | Does not open (68%) | 72% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 176 | [ ] | Path of Exile 2 (STEAM) | 31 | 37 | 84% (90d) | Does not open (96%) | 86% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 177 | [ ] | Mortal Kombat Komplete Edition (STEAM) | 30 | 70 | 50% (1.3.0) | Does not open (74%) | 78% |  |
| 178 | [ ] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 30 | 49 | 61% (90d) | Does not open (46%) | 80% |  |
| 179 | [ ] | Secrets of Grindea (STEAM) | 30 | 48 | 63% (90d) | Does not open (48%) | 78% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 180 | [ ] | Yakuza: Like a Dragon (STEAM) | 30 | 44 | 68% (90d) | Does not open (61%) | 68% |  |
| 181 | [ ] | Ultimate Custom Night (STEAM) | 30 | 42 | 71% (90d) | No graphics (72%) | 79% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 182 | [ ] | CRUEL (STEAM) | 30 | 36 | 83% (90d) | Does not open (90%) | 75% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 183 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 30 | 36 | 83% (90d) | Does not open (61%) | 75% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 184 | [ ] | Dead Island Riptide Definitive Edition (STEAM) | 29 | 56 | 52% (90d) | Does not open (50%) | 82% |  |
| 185 | [ ] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 54 | 54% (90d) | Does not open (92%) | 83% |  |
| 186 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 29 | 52 | 56% (90d) | Does not open (44%) | 91% |  |
| 187 | [ ] | Aethermancer (STEAM) | 29 | 51 | 57% (90d) | Does not open (78%) | 85% |  |
| 188 | [ ] | Heavy Rain (STEAM) | 29 | 51 | 57% (90d) | Controller issues (61%) | 92% |  |
| 189 | [ ] | Zero Escape: The Nonary Games (STEAM) | 28 | 47 | 60% (90d) | Does not open (88%) | 67% |  |
| 190 | [ ] | Binary Domain (STEAM) | 28 | 44 | 64% (90d) | Does not open (91%) | 75% |  |
| 191 | [ ] | Moonlight Peaks (STEAM) | 28 | 40 | 70% (90d) | Does not open (64%) | 90% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 192 | [ ] | Dead Rising 2 (STEAM) | 27 | 42 | 67% (1.3.0) | Does not open (88%) | 73% |  |
| 193 | [ ] | Deus Ex™ GOTY Edition (GOG) | 27 | 41 | 66% (90d) | Does not open (35%) | 88% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 194 | [ ] | Ratatan (STEAM) | 27 | 40 | 68% (90d) | Does not open (50%) | 98% |  |
| 195 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 27 | 37 | 73% (90d) | Does not open (64%) | 92% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 196 | [ ] | Stellar Blade™ (STEAM) | 27 | 37 | 73% (90d) | Does not open (45%) | 88% |  |
| 197 | [ ] | Tales of Zestiria (STEAM) | 27 | 33 | 82% (90d) | Does not open (81%) | 62% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 198 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 26 | 48 | 54% (90d) | Does not open (55%) | 79% |  |
| 199 | [ ] | Unturned (STEAM) | 26 | 47 | 55% (90d) | Does not open (61%) | 77% |  |
| 200 | [ ] | Akane (STEAM) | 26 | 45 | 58% (90d) | Controller issues (63%) | 100% |  |
| 201 | [ ] | Prince of Persia (GOG) | 26 | 43 | 60% (90d) | Does not open (95%) | 92% |  |
| 202 | [ ] | Digimon Survive (STEAM) | 26 | 42 | 62% (90d) | Controller issues (73%) | 96% |  |
| 203 | [ ] | Battle Brothers (STEAM) | 26 | 41 | 63% (90d) | Does not open (67%) | 68% |  |
| 204 | [ ] | Limbus Company (STEAM) | 26 | 39 | 67% (90d) | Does not open (86%) | 77% |  |
| 205 | [ ] | Gothic II: Gold Classic (STEAM) | 26 | 37 | 70% (90d) | Does not open (59%) | 75% |  |
| 206 | [ ] | Crab Game (STEAM) | 26 | 34 | 76% (90d) | Does not open (53%) | 79% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 207 | [ ] | Tearscape (STEAM) | 26 | 31 | 84% (90d) | Controller issues (55%) | 94% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 208 | [ ] | No, I'm not a Human (STEAM) | 25 | 56 | 57% (1.3.0) | Does not open (48%) | 92% |  |
| 209 | [ ] | Being a DIK (STEAM) | 25 | 43 | 58% (90d) | Does not open (78%) | 83% |  |
| 210 | [ ] | Changed (STEAM) | 25 | 38 | 66% (90d) | Does not open (65%) | 88% |  |
| 211 | [ ] | Return to Monkey Island (STEAM) | 25 | 38 | 66% (90d) | No graphics (58%) | 86% |  |
| 212 | [ ] | Bongo Cat (STEAM) | 25 | 35 | 71% (90d) | Does not open (65%) | 85% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 213 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 25 | 34 | 74% (90d) | Does not open (41%) | 69% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 214 | [ ] | Goose Goose Duck (STEAM) | 25 | 33 | 76% (90d) | Does not open (71%) | 72% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 215 | [ ] | Jade Empire: Special Edition (GOG) | 25 | 33 | 76% (90d) | Does not open (45%) | 73% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 216 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 32 | 78% (90d) | Does not open (87%) | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 217 | [ ] | Resident Evil (GOG) | 25 | 27 | 93% (90d) | Does not open (95%) | 65% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 218 | [ ] | Resident Evil Revelations 2 (STEAM) | 24 | 47 | 51% (90d) | Does not open (40%) | 92% |  |
| 219 | [ ] | Goat Simulator (STEAM) | 24 | 46 | 52% (90d) | Does not open (58%) | 62% |  |
| 220 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 24 | 44 | 55% (90d) | Controller issues (70%) | 96% |  |
| 221 | [ ] | Counter-Strike: Condition Zero (STEAM) | 24 | 42 | 57% (90d) | Does not open (50%) | 60% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 222 | [ ] | Wizard of Legend (EPIC) | 24 | 41 | 59% (90d) | Does not open (78%) | 85% |  |
| 223 | [ ] | Cat Mail Co. (STEAM) | 24 | 39 | 62% (90d) | Does not open (89%) | 89% |  |
| 224 | [ ] | Opus Magnum (STEAM) | 24 | 38 | 63% (90d) | Does not open (76%) | 87% |  |
| 225 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 24 | 35 | 69% (90d) | Does not open (57%) | 68% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 226 | [ ] | The Lantern of the Laughless Saint (STEAM) | 24 | 25 | 96% (90d) | Does not open (81%) | 64% | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 227 | [ ] | Football Manager 2024 (EPIC) | 23 | 42 | 55% (90d) | Does not open (86%) | 90% |  |
| 228 | [ ] | Lobotomy Corporation (STEAM) | 23 | 41 | 56% (90d) | No graphics (60%) | 95% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 229 | [ ] | Pinball FX Classic (STEAM) | 23 | 41 | 56% (90d) | Does not open (76%) | 92% |  |
| 230 | [ ] | SWORN (STEAM) | 23 | 39 | 59% (90d) | Does not open (44%) | 100% |  |
| 231 | [ ] | Worms W.M.D (STEAM) | 23 | 38 | 61% (90d) | Does not open (58%) | 89% |  |
| 232 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 37 | 62% (90d) | Does not open (100%) | 77% |  |
| 233 | [ ] | Timberborn (STEAM) | 23 | 35 | 66% (90d) | No graphics (62%) | 83% |  |
| 234 | [ ] | Party Animals (STEAM) | 23 | 32 | 72% (90d) | Does not open (75%) | 74% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 235 | [ ] | Beyond: Two Souls (STEAM) | 23 | 31 | 74% (90d) | Does not open (50%) | 71% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 236 | [ ] | CarX Street (STEAM) | 23 | 30 | 77% (90d) | Does not open (77%) | 92% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 237 | [ ] | FINAL FANTASY XIV Online (STEAM) | 23 | 30 | 77% (90d) | Does not open (100%) | 96% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 238 | [ ] | Jade Empire: Special Edition (STEAM) | 23 | 26 | 88% (90d) | Does not open (95%) | 67% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 239 | [ ] | PowerWash Simulator (STEAM) | 22 | 64 | 76% (1.3.0) | Does not open (84%) | 77% |  |
| 240 | [ ] | Gambonanza (STEAM) | 22 | 41 | 54% (90d) | Does not open (62%) | 93% |  |
| 241 | [ ] | Life is Strange Remastered (STEAM) | 22 | 34 | 65% (90d) | Does not open (73%) | 94% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 242 | [ ] | Need for Speed™ Unbound (STEAM) | 22 | 30 | 73% (90d) | Does not open (83%) | 79% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 243 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 59 | 82% (1.3.0) | Does not open (79%) | 100% |  |
| 244 | [ ] | Overlord (STEAM) | 21 | 40 | 53% (90d) | Does not open (71%) | 60% |  |
| 245 | [ ] | This War of Mine (STEAM) | 21 | 39 | 54% (90d) | No graphics (53%) | 71% |  |
| 246 | [ ] | Trailmakers (STEAM) | 21 | 39 | 54% (90d) | Does not open (44%) | 90% |  |
| 247 | [ ] | One-armed robber (STEAM) | 21 | 38 | 55% (90d) | Controller issues (58%) | 79% |  |
| 248 | [ ] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 21 | 36 | 58% (90d) | Controller issues (50%) | 100% |  |
| 249 | [ ] | Tiny Glade (STEAM) | 21 | 36 | 58% (90d) | Does not open (42%) | 78% |  |
| 250 | [ ] | GOD EATER RESURRECTION (STEAM) | 21 | 32 | 66% (90d) | Does not open (53%) | 63% |  |
| 251 | [ ] | Nex Machina (STEAM) | 21 | 28 | 75% (90d) | Does not open (57%) | 83% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 252 | [ ] | Capcom Fighting Collection (STEAM) | 21 | 26 | 81% (90d) | Does not open (79%) | 77% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 253 | [ ] | Crimzon Clover World EXplosion (STEAM) | 20 | 40 | 50% (90d) | Does not open (47%) | 100% |  |
| 254 | [ ] | Paper Lily - Chapter 1 (STEAM) | 20 | 40 | 50% (90d) | Does not open (72%) | 94% |  |
| 255 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 20 | 37 | 54% (90d) | Does not open (56%) | 69% |  |
| 256 | [ ] | Control Ultimate Edition (GOG) | 20 | 37 | 54% (90d) | Does not open (81%) | 94% |  |
| 257 | [ ] | Mafia: Definitive Edition (STEAM) | 20 | 37 | 54% (90d) | Does not open (84%) | 75% |  |
| 258 | [ ] | BAJA: Edge of Control HD (STEAM) | 20 | 27 | 74% (90d) | Does not open (100%) | 91% | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 259 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 20 | 27 | 74% (90d) | Does not open (65%) | 83% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 260 | [ ] | Dead Island (STEAM) | 20 | 26 | 77% (90d) | Does not open (69%) | 71% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 261 | [ ] | Tyr (STEAM) | 20 | 26 | 77% (90d) | Does not open (33%) | 82% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 262 | [ ] | Killing Floor (STEAM) | 19 | 34 | 56% (90d) | Controller issues (100%) | 85% |  |
| 263 | [ ] | My Summer Car (STEAM) | 19 | 34 | 56% (90d) | Does not open (59%) | 86% |  |
| 264 | [ ] | Stick It to the Stickman (STEAM) | 19 | 34 | 56% (90d) | Does not open (88%) | 74% |  |
| 265 | [ ] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 19 | 33 | 58% (90d) | Does not open (88%) | 67% |  |
| 266 | [ ] | Metro Exodus (STEAM) | 19 | 31 | 61% (90d) | Does not open (82%) | 90% |  |
| 267 | [ ] | Torchlight II (EPIC) | 19 | 27 | 70% (90d) | Does not open (82%) | 94% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 268 | [ ] | Faster Than Light (EPIC) | 18 | 36 | 50% (90d) | Does not open (41%) | 100% |  |
| 269 | [ ] | Far Far West (STEAM) | 18 | 32 | 56% (90d) | Does not open (59%) | 78% |  |
| 270 | [ ] | Hitman: Absolution (GOG) | 18 | 30 | 60% (90d) | Does not open (81%) | 75% |  |
| 271 | [ ] | Tabletop Simulator (STEAM) | 18 | 30 | 60% (90d) | Does not open (50%) | 62% |  |
| 272 | [ ] | Formula Legends (STEAM) | 18 | 28 | 64% (90d) | No graphics (60%) | 62% |  |
| 273 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 28 | 64% (90d) | No graphics (39%) | 81% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 274 | [ ] | Arcade Paradise (EPIC) | 18 | 27 | 67% (90d) | Does not open (45%) | 83% |  |
| 275 | [ ] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 18 | 27 | 67% (90d) | Does not open (83%) | 96% |  |
| 276 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 18 | 27 | 67% (90d) | Does not open (71%) | 73% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 277 | [ ] | DOOM 3: BFG Edition (GOG) | 18 | 25 | 72% (90d) | No graphics (67%) | 80% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 278 | [ ] | Katanaut (STEAM) | 18 | 24 | 75% (90d) | Does not open (76%) | 62% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 279 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 18 | 23 | 78% (90d) | Does not open (81%) | 93% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 280 | [ ] | Crusader Kings III (STEAM) | 18 | 23 | 78% (90d) | No graphics (64%) | 69% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 281 | [ ] | Dorfromantik (GOG) | 18 | 23 | 78% (90d) | Does not open (94%) | 64% | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 282 | [ ] | Deadly Premonition: The Director's Cut (STEAM) | 18 | 21 | 86% (90d) | Does not open (47%) | 77% |  |
| 283 | [ ] | SKALD: Against the Black Priory (STEAM) | 17 | 34 | 50% (90d) | No graphics (57%) | 97% |  |
| 284 | [ ] | CULTIC (STEAM) | 17 | 33 | 52% (90d) | Does not open (92%) | 61% |  |
| 285 | [ ] | SCP – Containment Breach (STEAM) | 17 | 32 | 53% (90d) | Does not open (82%) | 85% |  |
| 286 | [ ] | GRANDIA HD Remaster (STEAM) | 17 | 31 | 55% (90d) | Does not open (93%) | 72% |  |
| 287 | [ ] | GRIP: Combat Racing (STEAM) | 17 | 31 | 55% (90d) | Does not open (100%) | 83% |  |
| 288 | [ ] | Sorry We're Closed (EPIC) | 17 | 30 | 55% (14d) | Does not open (88%) | 87% |  |
| 289 | [ ] | Maneater (STEAM) | 17 | 27 | 63% (90d) | Does not open (92%) | 77% |  |
| 290 | [ ] | Grim Fandango Remastered (GOG) | 17 | 25 | 68% (90d) | No graphics (78%) | 60% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 291 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 16 | 31 | 52% (90d) | Does not open (100%) | 65% |  |
| 292 | [ ] | Lost Castle 2 (STEAM) | 16 | 30 | 53% (90d) | Does not open (58%) | 100% |  |
| 293 | [ ] | DNF Duel (EPIC) | 16 | 29 | 55% (90d) | Does not open (54%) | 91% |  |
| 294 | [ ] | Titanfall® 2 (STEAM) | 16 | 29 | 55% (90d) | Does not open (83%) | 78% |  |
| 295 | [ ] | Dishonored 2 (STEAM) | 16 | 26 | 62% (90d) | Does not open (85%) | 90% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 296 | [ ] | Fall Guys (STEAM) | 16 | 22 | 73% (90d) | Does not open (92%) | 93% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 297 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 22 | 73% (90d) | No graphics (60%) | 85% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 298 | [ ] | Blood Bowl 2 (STEAM) | 16 | 20 | 80% (90d) | Does not open (64%) | 90% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 299 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 16 | 20 | 80% (90d) | Does not open (60%) | 91% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 300 | [ ] | Mark of the Ninja (STEAM) | 15 | 30 | 50% (90d) | Does not open (75%) | 62% |  |
| 301 | [ ] | WORLD OF FINAL FANTASY (STEAM) | 15 | 26 | 58% (90d) | No graphics (58%) | 81% |  |
| 302 | [ ] | Wildermyth (STEAM) | 15 | 26 | 58% (90d) | Does not open (50%) | 94% |  |
| 303 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 15 | 25 | 60% (90d) | Does not open (92%) | 74% |  |
| 304 | [ ] | LET IT DIE (STEAM) | 15 | 25 | 60% (90d) | Does not open (91%) | 73% |  |
| 305 | [ ] | Batman™: Arkham Origins (GOG) | 15 | 24 | 63% (90d) | Does not open (67%) | 93% |  |
| 306 | [ ] | Mortal Shell (EPIC) | 15 | 24 | 63% (90d) | No graphics (89%) | 88% |  |
| 307 | [ ] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 15 | 23 | 65% (90d) | Does not open (64%) | 69% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 308 | [ ] | Allumeria (STEAM) | 15 | 22 | 68% (90d) | Does not open (69%) | 73% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 309 | [ ] | Chef Knight (STEAM) | 15 | 22 | 68% (90d) | Does not open (100%) | 69% |  |
| 310 | [ ] | Maneater (EPIC) | 15 | 20 | 75% (90d) | Does not open (73%) | 80% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 311 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 28 | 50% (90d) | Controller issues (54%) | 85% |  |
| 312 | [ ] | Ultrapool (STEAM) | 14 | 25 | 56% (90d) | Does not open (54%) | 100% |  |
| 313 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 24 | 58% (90d) | Does not open (90%) | 72% |  |
| 314 | [ ] | Gloomwood (STEAM) | 14 | 24 | 58% (90d) | Does not open (62%) | 75% |  |
| 315 | [ ] | 12 is Better Than 6 (STEAM) | 14 | 23 | 61% (90d) | Does not open (45%) | 83% |  |
| 316 | [ ] | Alabaster Dawn Demo (STEAM) | 14 | 23 | 61% (90d) | Controller issues (71%) | 89% |  |
| 317 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 23 | 61% (90d) | Controller issues (62%) | 65% |  |
| 318 | [ ] | Disgaea 4 Complete+ (STEAM) | 14 | 22 | 64% (90d) | No graphics (43%) | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 319 | [ ] | Songs of Conquest (EPIC) | 14 | 22 | 64% (90d) | Does not open (75%) | 90% |  |
| 320 | [ ] | Sons Of The Forest (STEAM) | 14 | 22 | 64% (90d) | Does not open (50%) | 74% |  |
| 321 | [ ] | Horny Villa (STEAM) | 14 | 20 | 70% (90d) | Does not open (63%) | 95% |  |
| 322 | [ ] | Intravenous 2 (STEAM) | 13 | 26 | 50% (90d) | No graphics (63%) | 88% |  |
| 323 | [ ] | Lust Goddess (STEAM) | 13 | 25 | 52% (90d) | Does not open (100%) | 64% |  |
| 324 | [ ] | Ready or Not (STEAM) | 13 | 24 | 54% (90d) | Does not open (55%) | 93% |  |
| 325 | [ ] | DiRT 4 (STEAM) | 13 | 23 | 57% (90d) | Does not open (75%) | 96% |  |
| 326 | [ ] | Minit (EPIC) | 13 | 23 | 57% (90d) | Does not open (82%) | 81% |  |
| 327 | [ ] | Scrap Mechanic (STEAM) | 13 | 23 | 57% (90d) | Does not open (45%) | 71% |  |
| 328 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 22 | 59% (90d) | Does not open (80%) | 90% |  |
| 329 | [ ] | PAYDAY: The Heist (STEAM) | 13 | 21 | 62% (90d) | Does not open (75%) | 69% |  |
| 330 | [ ] | Shift At Midnight (STEAM) | 13 | 21 | 62% (90d) | Does not open (83%) | 92% |  |
| 331 | [ ] | Hitman: Contracts (STEAM) | 13 | 20 | 65% (90d) | Controller issues (75%) | 80% |  |
| 332 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 13 | 20 | 65% (90d) | Does not open (71%) | 61% |  |
| 333 | [ ] | War Thunder (STEAM) | 13 | 20 | 65% (90d) | Does not open (80%) | 81% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 334 | [ ] | NiGHTS into Dreams... (STEAM) | 12 | 24 | 50% (90d) | Does not open (44%) | 93% |  |
| 335 | [ ] | Sonic Superstars (STEAM) | 12 | 24 | 50% (90d) | Does not open (70%) | 65% |  |
| 336 | [ ] | AER Memories of Old (EPIC) | 12 | 23 | 52% (90d) | Does not open (91%) | 93% |  |
| 337 | [ ] | Cruelty Squad (STEAM) | 12 | 23 | 52% (90d) | Does not open (67%) | 86% |  |
| 338 | [ ] | Haydee (STEAM) | 12 | 23 | 52% (90d) | Does not open (100%) | 82% |  |
| 339 | [ ] | Pillars of Eternity (STEAM) | 12 | 23 | 52% (90d) | Does not open (33%) | 62% |  |
| 340 | [ ] | UNDEFEATED (STEAM) | 12 | 23 | 52% (90d) | Does not open (89%) | 77% |  |
| 341 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 12 | 22 | 55% (90d) | Does not open (60%) | 90% |  |
| 342 | [ ] | HITMAN World of Assassination (STEAM) | 12 | 22 | 55% (90d) | Does not open (73%) | 87% |  |
| 343 | [ ] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 22 | 55% (90d) | Controller issues (60%) | 88% |  |
| 344 | [ ] | FATE (STEAM) | 12 | 21 | 57% (90d) | No graphics (44%) | 91% |  |
| 345 | [ ] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 20 | 60% (90d) | No graphics (40%) | 100% |  |
| 346 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (90d) | Does not open (89%) | 96% |  |
| 347 | [ ] | Castle in the Clouds (STEAM) | 11 | 22 | 50% (90d) | No graphics (63%) | 86% |  |
| 348 | [ ] | Injustice™ 2 (STEAM) | 11 | 22 | 50% (90d) | Does not open (88%) | 75% |  |
| 349 | [ ] | MX Bikes (STEAM) | 11 | 22 | 50% (90d) | Does not open (73%) | 94% |  |
| 350 | [ ] | Tom Clancy's Rainbow Six: Vegas 2 (STEAM) | 11 | 22 | 50% (90d) | Does not open (55%) | 88% |  |
| 351 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 21 | 52% (90d) | Does not open (86%) | 75% |  |
| 352 | [ ] | Ghostwire Tokyo (EPIC) | 11 | 21 | 52% (90d) | Does not open (86%) | 94% |  |
| 353 | [ ] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 21 | 52% (90d) | Graphics glitches (40%) | 95% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 354 | [ ] | Shadow Tactics: Blades of the Shogun (EPIC) | 11 | 20 | 55% (90d) | Does not open (67%) | 100% |  |
| 355 | [ ] | Coromon (GOG) | 10 | 20 | 50% (90d) | Does not open (56%) | 64% |  |
| 356 | [ ] | F1 2015 (STEAM) | 10 | 20 | 50% (90d) | Does not open (50%) | 70% |  |

## Recently recovered (397)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | FINAL FANTASY RESONANCE (STEAM) | 319 | 2026-10-24 | 736 | 75% |  |
| 2 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 253 | 2026-10-23 | 295 | 67% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 3 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 243 | 2026-10-19 | 297 | 68% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 236 | 2026-10-18 | 362 | 59% |  |
| 5 | [x] | OMORI (STEAM) | 203 | 2026-10-16 | 245 | 82% |  |
| 6 | [x] | Devil May Cry HD Collection (STEAM) | 202 | 2026-10-19 | 283 | 76% |  |
| 7 | [x] | DRAGON BALL FighterZ (STEAM) | 202 | 2026-11-01 | 233 | 62% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 8 | [x] | Spelunky 2 (STEAM) | 190 | 2026-11-01 | 211 | 51% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 9 | [x] | Burnout Paradise: The Ultimate Box (STEAM) | 149 | 2026-10-16 | 240 | 72% |  |
| 10 | [x] | Borderlands 2 (EPIC) | 143 | 2026-10-25 | 169 | 61% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 11 | [x] | Sonic Adventure™ 2  (STEAM) | 141 | 2026-11-01 | 198 | 49% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 12 | [x] | Counter-Strike (STEAM) | 138 | 2026-10-22 | 222 | 50% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 13 | [x] | Far Cry® 3 (STEAM) | 128 | 2026-10-21 | 143 | 67% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 14 | [x] | Minecraft Dungeons II (STEAM) | 125 | 2026-10-21 | 143 | 64% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 15 | [x] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 120 | 2026-10-18 | 168 | 64% |  |
| 16 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 120 | 2026-10-28 | 152 | 60% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 17 | [x] | Call of Duty: Black Ops III (STEAM) | 117 | 2026-10-18 | 245 | 72% |  |
| 18 | [x] | Euro Truck Simulator 2 (STEAM) | 115 | 2026-11-01 | 213 | 58% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 19 | [x] | The Witcher: Enhanced Edition (STEAM) | 112 | 2026-10-25 | 129 | 63% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 20 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 106 | 2026-10-18 | 155 | 76% |  |
| 21 | [x] | Moonstone Island (STEAM) | 104 | 2026-10-16 | 137 | 87% |  |
| 22 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 97 | 2026-10-25 | 154 | 67% |  |
| 23 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 92 | 2026-10-17 | 120 | 97% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 24 | [x] | Don't Starve Together (STEAM) | 91 | 2026-10-16 | 180 | 81% |  |
| 25 | [x] | Catherine Classic (STEAM) | 87 | 2026-10-19 | 172 | 78% |  |
| 26 | [x] | Ultra Street Fighter IV (STEAM) | 84 | 2026-10-17 | 180 | 68% |  |
| 27 | [x] | Hogwarts Legacy (STEAM) | 84 | 2026-10-17 | 145 | 66% |  |
| 28 | [x] | Cry of Fear (STEAM) | 81 | 2026-10-18 | 161 | 85% |  |
| 29 | [x] | DOOM 3: BFG Edition (STEAM) | 78 | 2026-10-19 | 114 | 70% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 30 | [x] | Detroit: Become Human (STEAM) | 77 | 2026-10-17 | 80 | 61% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 31 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 74 | 2026-10-18 | 124 | 94% |  |
| 32 | [x] | Need for Speed: Hot Pursuit (STEAM) | 74 | 2026-10-25 | 108 | 79% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 33 | [x] | Sol Cesto (EPIC) | 73 | 2026-11-03 | 77 | 73% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 34 | [x] | Bayonetta (STEAM) | 71 | 2026-10-18 | 205 | 78% |  |
| 35 | [x] | Darksiders (STEAM) | 71 | 2026-10-26 | 86 | 88% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 36 | [x] | Disgaea 5 Complete (STEAM) | 70 | 2026-10-18 | 84 | 98% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 37 | [x] | American Truck Simulator (STEAM) | 68 | 2026-10-18 | 111 | 79% |  |
| 38 | [x] | Fallout (STEAM) | 68 | 2026-10-18 | 106 | 73% |  |
| 39 | [x] | Dota 2 (STEAM) | 68 | 2026-10-17 | 104 | 72% |  |
| 40 | [x] | Don't Starve (STEAM) | 67 | 2026-10-16 | 157 | 81% |  |
| 41 | [x] | Stardew Valley (GOG) | 67 | 2026-11-01 | 122 | 50% |  |
| 42 | [x] | Spyro™ Reignited Trilogy (STEAM) | 67 | 2026-10-18 | 105 | 72% |  |
| 43 | [x] | Bloodstained: Ritual of the Night (EPIC) | 66 | 2026-10-19 | 122 | 63% |  |
| 44 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 66 | 2026-10-17 | 95 | 80% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 45 | [x] | Gunfire Reborn (STEAM) | 66 | 2026-10-22 | 72 | 94% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 46 | [x] | Call of Juarez Gunslinger (STEAM) | 65 | 2026-10-18 | 80 | 75% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 47 | [x] | Sonic Lost World (STEAM) | 64 | 2026-10-18 | 108 | 86% |  |
| 48 | [x] | Fable - The Lost Chapters (STEAM) | 64 | 2026-10-17 | 102 | 79% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 49 | [x] | Poppy Playtime (STEAM) | 63 | 2026-10-17 | 111 | 80% |  |
| 50 | [x] | Borderlands: The Pre-Sequel (STEAM) | 63 | 2026-10-17 | 89 | 64% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 51 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 61 | 2026-10-17 | 84 | 90% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 52 | [x] | A Plague Tale: Innocence (STEAM) | 60 | 2026-10-20 | 63 | 76% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 53 | [x] | Big Walk (STEAM) | 58 | 2026-10-17 | 90 | 82% |  |
| 54 | [x] | Call of Duty: World at War (STEAM) | 58 | 2026-10-28 | 83 | 74% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 55 | [x] | Borderlands 3 (STEAM) | 58 | 2026-10-19 | 78 | 94% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 56 | [x] | Mini Motorways (STEAM) | 57 | 2026-11-04 | 99 | 63% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 57 | [x] | Starbound (STEAM) | 57 | 2026-10-18 | 87 | 72% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 58 | [x] | Dead by Daylight (STEAM) | 57 | 2026-10-23 | 62 | 81% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 59 | [x] | eFootball™ (STEAM) | 56 | 2026-10-18 | 84 | 76% |  |
| 60 | [x] | Sonic Generations (STEAM) | 56 | 2026-10-17 | 65 | 63% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 61 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 55 | 2026-10-18 | 86 | 74% |  |
| 62 | [x] | Alex Kidd in Miracle World DX (EPIC) | 55 | 2026-10-22 | 59 | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 63 | [x] | Sonic Adventure DX (STEAM) | 54 | 2026-10-17 | 89 | 63% |  |
| 64 | [x] | TBH: Task Bar Hero (STEAM) | 54 | 2026-10-19 | 84 | 94% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 65 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 53 | 2026-10-19 | 100 | 76% |  |
| 66 | [x] | Okami HD (STEAM) | 53 | 2026-10-17 | 98 | 85% |  |
| 67 | [x] | Path of Exile (STEAM) | 53 | 2026-10-26 | 62 | 86% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 68 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 52 | 2026-10-18 | 76 | 64% |  |
| 69 | [x] | Vampire Survivors (EPIC) | 52 | 2026-11-03 | 74 | 64% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 70 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 51 | 2026-10-25 | 97 | 57% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 71 | [x] | Until Then (STEAM) | 51 | 2026-10-17 | 90 | 96% |  |
| 72 | [x] | A Plague Tale: Innocence (EPIC) | 51 | 2026-10-25 | 87 | 89% |  |
| 73 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 51 | 2026-10-21 | 59 | 82% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 74 | [x] | Heroes of Might & Magic III - HD Edition (STEAM) | 50 | 2026-11-04 | 64 | 62% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 75 | [x] | Guildrun Demo (STEAM) | 49 | 2026-10-22 | 69 | 70% |  |
| 76 | [x] | Dead Space (STEAM) | 49 | 2026-10-18 | 62 | 78% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 77 | [x] | Sheepy: A Short Adventure (STEAM) | 49 | 2026-10-24 | 59 | 80% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 78 | [x] | Darkest Dungeon® (EPIC) | 48 | 2026-10-22 | 87 | 61% |  |
| 79 | [x] | Sleeping Dogs™ (STEAM) | 48 | 2026-10-27 | 55 | 77% | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 80 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 2026-10-17 | 75 | 95% |  |
| 81 | [x] | Watch_Dogs 2 (STEAM) | 47 | 2026-11-03 | 52 | 60% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 82 | [x] | Moonlighter (EPIC) | 47 | 2026-10-23 | 51 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 83 | [x] | Deadlock (STEAM) | 46 | 2026-10-16 | 67 | 94% |  |
| 84 | [x] | Rivals of Aether II (STEAM) | 46 | 2026-10-20 | 67 | 74% |  |
| 85 | [x] | MudRunner (STEAM) | 45 | 2026-10-24 | 99 | 71% |  |
| 86 | [x] | Abiotic Factor (STEAM) | 45 | 2026-10-18 | 78 | 67% |  |
| 87 | [x] | Tomb Raider: Anniversary (STEAM) | 45 | 2026-10-25 | 66 | 64% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 88 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 44 | 2026-10-17 | 78 | 89% |  |
| 89 | [x] | Aggelos (STEAM) | 44 | 2026-10-21 | 58 | 95% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 90 | [x] | Tomb Raider GOTY (GOG) | 43 | 2026-10-17 | 90 | 97% |  |
| 91 | [x] | Digimon World: Next Order (STEAM) | 43 | 2026-10-18 | 83 | 95% |  |
| 92 | [x] | Skullgirls 2nd Encore (STEAM) | 43 | 2026-11-01 | 78 | 54% |  |
| 93 | [x] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 43 | 2026-11-05 | 46 | 64% | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 94 | [x] | Death Road to Canada (STEAM) | 42 | 2026-10-17 | 100 | 71% |  |
| 95 | [x] | PROTOTYPE 2 (STEAM) | 42 | 2026-10-18 | 89 | 79% |  |
| 96 | [x] | Street Fighter™ 6 (STEAM) | 42 | 2026-10-16 | 68 | 84% |  |
| 97 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 42 | 2026-10-18 | 63 | 69% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 98 | [x] | FINAL FANTASY VII (2013) (STEAM) | 42 | 2026-10-18 | 60 | 81% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 99 | [x] | Life is Strange™ (STEAM) | 41 | 2026-10-17 | 84 | 81% |  |
| 100 | [x] | Rogue Legacy (STEAM) | 40 | 2026-10-17 | 90 | 62% |  |
| 101 | [x] | Rayman Origins (STEAM) | 40 | 2026-10-17 | 88 | 83% |  |
| 102 | [x] | Amnesia: The Dark Descent (STEAM) | 40 | 2026-10-17 | 75 | 75% |  |
| 103 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 40 | 2026-10-27 | 41 | 86% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 104 | [x] | Cobalt Core (STEAM) | 39 | 2026-10-18 | 90 | 88% |  |
| 105 | [x] | Salt and Sanctuary (STEAM) | 39 | 2026-10-18 | 79 | 81% |  |
| 106 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 39 | 2026-10-17 | 74 | 100% |  |
| 107 | [x] | Capcom Arcade Stadium (STEAM) | 39 | 2026-10-17 | 48 | 76% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 108 | [x] | CrossCode (GOG) | 38 | 2026-10-23 | 42 | 73% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 109 | [x] | Monster Hunter Wilds (STEAM) | 38 | 2026-10-23 | 39 | 79% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 110 | [x] | Tales of ARISE (STEAM) | 37 | 2026-10-16 | 71 | 93% |  |
| 111 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 2026-10-17 | 69 | 89% |  |
| 112 | [x] | Elite Dangerous (STEAM) | 37 | 2026-11-05 | 40 | 69% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 113 | [x] | Hearts of Iron IV (STEAM) | 36 | 2026-10-19 | 63 | 67% |  |
| 114 | [x] | Supermarket Together (STEAM) | 36 | 2026-10-19 | 50 | 69% |  |
| 115 | [x] | Sable (EPIC) | 35 | 2026-10-18 | 77 | 84% |  |
| 116 | [x] | POSTAL 2 (GOG) | 35 | 2026-10-22 | 71 | 93% |  |
| 117 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 35 | 2026-10-16 | 68 | 65% |  |
| 118 | [x] | STAR WARS™ Episode I: Racer (GOG) | 35 | 2026-11-02 | 41 | 80% | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 119 | [x] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 35 | 2026-11-01 | 40 | 60% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 120 | [x] | Teardown (STEAM) | 34 | 2026-10-17 | 76 | 76% |  |
| 121 | [x] | SnowRunner (STEAM) | 34 | 2026-10-19 | 48 | 89% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 122 | [x] | Journey (STEAM) | 33 | 2026-10-27 | 70 | 57% |  |
| 123 | [x] | Ultimate Chicken Horse (STEAM) | 33 | 2026-10-23 | 69 | 66% |  |
| 124 | [x] | Max Payne (STEAM) | 33 | 2026-10-17 | 59 | 93% |  |
| 125 | [x] | Hero Siege (STEAM) | 33 | 2026-11-02 | 57 | 64% |  |
| 126 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 33 | 2026-10-19 | 54 | 74% |  |
| 127 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 2026-10-19 | 53 | 80% |  |
| 128 | [x] | Capcom Fighting Collection 2 (STEAM) | 33 | 2026-10-18 | 49 | 87% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 129 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 33 | 2026-10-21 | 46 | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 130 | [x] | Romestead (STEAM) | 33 | 2026-10-18 | 44 | 77% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 131 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 33 | 2026-10-20 | 43 | 89% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 132 | [x] | Russian Fishing 4 (STEAM) | 33 | 2026-10-23 | 39 | 75% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 133 | [x] | Hotline Miami (GOG) | 33 | 2026-10-20 | 38 | 67% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 134 | [x] | Bloodstained: Curse of the Moon (STEAM) | 32 | 2026-10-16 | 73 | 70% |  |
| 135 | [x] | COCOON (STEAM) | 32 | 2026-10-17 | 62 | 90% |  |
| 136 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 32 | 2026-10-26 | 57 | 67% |  |
| 137 | [x] | Rocket League (STEAM) | 32 | 2026-10-17 | 53 | 70% |  |
| 138 | [x] | Earthion (STEAM) | 32 | 2026-10-22 | 52 | 100% |  |
| 139 | [x] | Counter-Strike:Global Offensive (STEAM) | 32 | 2026-10-19 | 50 | 78% |  |
| 140 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 32 | 2026-10-18 | 48 | 87% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 141 | [x] | Palia (STEAM) | 32 | 2026-10-22 | 44 | 76% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 142 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 32 | 2026-10-22 | 37 | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 143 | [x] | Dishonored - Definitive Edition (EPIC) | 31 | 2026-10-17 | 79 | 84% |  |
| 144 | [x] | Little Nightmares (STEAM) | 31 | 2026-10-16 | 70 | 60% |  |
| 145 | [x] | Mortal Kombat X (STEAM) | 31 | 2026-10-17 | 57 | 85% |  |
| 146 | [x] | Resident Evil Village (STEAM) | 31 | 2026-10-17 | 53 | 90% |  |
| 147 | [x] | Grand Theft Auto III (STEAM) | 31 | 2026-10-17 | 47 | 79% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 148 | [x] | Tower and Sword of Succubus (STEAM) | 31 | 2026-10-22 | 46 | 100% |  |
| 149 | [x] | Nioh: Complete Edition (STEAM) | 31 | 2026-10-20 | 42 | 95% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 150 | [x] | Super Animal Royale (STEAM) | 31 | 2026-10-19 | 41 | 72% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 151 | [x] | Path of Exile 2 (STEAM) | 31 | 2026-10-18 | 37 | 86% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 152 | [x] | Torchlight II (STEAM) | 30 | 2026-10-20 | 63 | 91% |  |
| 153 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 30 | 2026-10-22 | 49 | 80% |  |
| 154 | [x] | Secrets of Grindea (STEAM) | 30 | 2026-10-20 | 48 | 78% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 155 | [x] | Ultimate Custom Night (STEAM) | 30 | 2026-10-19 | 42 | 79% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 156 | [x] | CRUEL (STEAM) | 30 | 2026-10-28 | 36 | 75% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 157 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 30 | 2026-10-18 | 36 | 75% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 158 | [x] | Monster Hunter Stories (STEAM) | 29 | 2026-10-17 | 64 | 86% |  |
| 159 | [x] | Stumble Guys (STEAM) | 29 | 2026-10-18 | 61 | 83% |  |
| 160 | [x] | Library Of Ruina (STEAM) | 29 | 2026-10-16 | 60 | 86% |  |
| 161 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 29 | 2026-10-18 | 56 | 82% |  |
| 162 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 2026-10-17 | 54 | 83% |  |
| 163 | [x] | Prince of Persia: The Sands of Time (STEAM) | 29 | 2026-10-20 | 52 | 91% |  |
| 164 | [x] | Aethermancer (STEAM) | 29 | 2026-10-18 | 51 | 85% |  |
| 165 | [x] | Heavy Rain (STEAM) | 29 | 2026-10-18 | 51 | 92% |  |
| 166 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 28 | 2026-10-19 | 93 | 93% |  |
| 167 | [x] | Dying Light (EPIC) | 28 | 2026-10-17 | 65 | 89% |  |
| 168 | [x] | State of Decay: Year-One (STEAM) | 28 | 2026-10-18 | 60 | 83% |  |
| 169 | [x] | Zero Escape: The Nonary Games (STEAM) | 28 | 2026-10-17 | 47 | 67% |  |
| 170 | [x] | Binary Domain (STEAM) | 28 | 2026-10-18 | 44 | 75% |  |
| 171 | [x] | Moonlight Peaks (STEAM) | 28 | 2026-10-20 | 40 | 90% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 172 | [x] | BioShock™ (GOG) | 27 | 2026-10-18 | 62 | 71% |  |
| 173 | [x] | Deus Ex™ GOTY Edition (GOG) | 27 | 2026-10-19 | 41 | 88% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 174 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 27 | 2026-11-03 | 37 | 92% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 175 | [x] | Tales of Zestiria (STEAM) | 27 | 2026-10-27 | 33 | 62% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 176 | [x] | PlateUp! (STEAM) | 26 | 2026-10-16 | 56 | 88% |  |
| 177 | [x] | G.I. Joe Wrath of Cobra (EPIC) | 26 | 2026-10-19 | 48 | 79% |  |
| 178 | [x] | Unturned (STEAM) | 26 | 2026-10-17 | 47 | 77% |  |
| 179 | [x] | Akane (STEAM) | 26 | 2026-10-20 | 45 | 100% |  |
| 180 | [x] | Prince of Persia (GOG) | 26 | 2026-10-24 | 43 | 92% |  |
| 181 | [x] | Digimon Survive (STEAM) | 26 | 2026-10-23 | 42 | 96% |  |
| 182 | [x] | Battle Brothers (STEAM) | 26 | 2026-10-27 | 41 | 68% |  |
| 183 | [x] | Limbus Company (STEAM) | 26 | 2026-10-18 | 39 | 77% |  |
| 184 | [x] | Gothic II: Gold Classic (STEAM) | 26 | 2026-10-20 | 37 | 75% |  |
| 185 | [x] | Crab Game (STEAM) | 26 | 2026-10-22 | 34 | 79% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 186 | [x] | Tearscape (STEAM) | 26 | 2026-10-30 | 31 | 94% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 187 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 25 | 2026-10-19 | 63 | 83% |  |
| 188 | [x] | Being a DIK (STEAM) | 25 | 2026-10-19 | 43 | 83% |  |
| 189 | [x] | Changed (STEAM) | 25 | 2026-10-24 | 38 | 88% |  |
| 190 | [x] | Return to Monkey Island (STEAM) | 25 | 2026-10-23 | 38 | 86% |  |
| 191 | [x] | Bongo Cat (STEAM) | 25 | 2026-10-20 | 35 | 85% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 192 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 25 | 2026-10-25 | 34 | 69% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 193 | [x] | Jade Empire: Special Edition (GOG) | 25 | 2026-10-23 | 33 | 73% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 194 | [x] | Goose Goose Duck (STEAM) | 25 | 2026-10-25 | 33 | 72% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 195 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-10-21 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 196 | [x] | Resident Evil (GOG) | 25 | 2026-10-20 | 27 | 65% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 197 | [x] | CarX Drift Racing Online (STEAM) | 24 | 2026-10-16 | 58 | 74% |  |
| 198 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 57 | 88% |  |
| 199 | [x] | WEBFISHING (STEAM) | 24 | 2026-10-17 | 49 | 88% |  |
| 200 | [x] | Goat Simulator (STEAM) | 24 | 2026-11-01 | 46 | 62% |  |
| 201 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 24 | 2026-10-24 | 44 | 96% |  |
| 202 | [x] | Counter-Strike: Condition Zero (STEAM) | 24 | 2026-10-17 | 42 | 60% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 203 | [x] | Wizard of Legend (EPIC) | 24 | 2026-10-18 | 41 | 85% |  |
| 204 | [x] | Cat Mail Co. (STEAM) | 24 | 2026-10-24 | 39 | 89% |  |
| 205 | [x] | Opus Magnum (STEAM) | 24 | 2026-11-01 | 38 | 87% |  |
| 206 | [x] | Borderlands: The Pre-Sequel (EPIC) | 24 | 2026-10-30 | 35 | 68% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 207 | [x] | The Lantern of the Laughless Saint (STEAM) | 24 | 2026-11-05 | 25 | 64% | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 208 | [x] | Owlboy (STEAM) | 23 | 2026-11-02 | 51 | 51% |  |
| 209 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 23 | 2026-10-20 | 50 | 83% |  |
| 210 | [x] | Cave Story+ (EPIC) | 23 | 2026-10-18 | 48 | 86% |  |
| 211 | [x] | Football Manager 2024 (EPIC) | 23 | 2026-10-20 | 42 | 90% |  |
| 212 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-10-19 | 41 | 95% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 213 | [x] | Pinball FX Classic (STEAM) | 23 | 2026-10-23 | 41 | 92% |  |
| 214 | [x] | SWORN (STEAM) | 23 | 2026-10-23 | 39 | 100% |  |
| 215 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 2026-10-17 | 37 | 77% |  |
| 216 | [x] | Timberborn (STEAM) | 23 | 2026-10-25 | 35 | 83% |  |
| 217 | [x] | Party Animals (STEAM) | 23 | 2026-10-17 | 32 | 74% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 218 | [x] | Beyond: Two Souls (STEAM) | 23 | 2026-10-22 | 31 | 71% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 219 | [x] | CarX Street (STEAM) | 23 | 2026-11-04 | 30 | 92% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 220 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 96% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 221 | [x] | Jade Empire: Special Edition (STEAM) | 23 | 2026-11-01 | 26 | 67% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 222 | [x] | ABZÛ (STEAM) | 22 | 2026-10-21 | 52 | 93% |  |
| 223 | [x] | Hatred (STEAM) | 22 | 2026-10-22 | 45 | 82% |  |
| 224 | [x] | Life is Strange Remastered (STEAM) | 22 | 2026-10-20 | 34 | 94% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 225 | [x] | Need for Speed™ Unbound (STEAM) | 22 | 2026-10-26 | 30 | 79% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 226 | [x] | BlazBlue Centralfiction (STEAM) | 21 | 2026-10-17 | 61 | 80% |  |
| 227 | [x] | Titan Quest Anniversary Edition (STEAM) | 21 | 2026-10-16 | 54 | 88% |  |
| 228 | [x] | Slow Roads (STEAM) | 21 | 2026-10-22 | 46 | 94% |  |
| 229 | [x] | Overlord (STEAM) | 21 | 2026-11-03 | 40 | 60% |  |
| 230 | [x] | This War of Mine (STEAM) | 21 | 2026-10-21 | 39 | 71% |  |
| 231 | [x] | Trailmakers (STEAM) | 21 | 2026-10-21 | 39 | 90% |  |
| 232 | [x] | One-armed robber (STEAM) | 21 | 2026-10-23 | 38 | 79% |  |
| 233 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 21 | 2026-10-21 | 36 | 100% |  |
| 234 | [x] | Tiny Glade (STEAM) | 21 | 2026-10-24 | 36 | 78% |  |
| 235 | [x] | GOD EATER RESURRECTION (STEAM) | 21 | 2026-11-01 | 32 | 63% |  |
| 236 | [x] | Nex Machina (STEAM) | 21 | 2026-10-18 | 28 | 83% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 237 | [x] | Capcom Fighting Collection (STEAM) | 21 | 2026-10-23 | 26 | 77% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 238 | [x] | Saints Row IV (STEAM) | 20 | 2026-10-19 | 48 | 72% |  |
| 239 | [x] | No Rest for the Wicked (STEAM) | 20 | 2026-10-19 | 43 | 75% |  |
| 240 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-10-20 | 40 | 100% |  |
| 241 | [x] | Paper Lily - Chapter 1 (STEAM) | 20 | 2026-10-27 | 40 | 94% |  |
| 242 | [x] | Brothers - A Tale of Two Sons (EPIC) | 20 | 2026-10-23 | 37 | 69% |  |
| 243 | [x] | Mafia: Definitive Edition (STEAM) | 20 | 2026-10-28 | 37 | 75% |  |
| 244 | [x] | BAJA: Edge of Control HD (STEAM) | 20 | 2026-10-28 | 27 | 91% | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 245 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 20 | 2026-11-04 | 27 | 83% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 246 | [x] | Dead Island (STEAM) | 20 | 2026-10-20 | 26 | 71% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 247 | [x] | Tyr (STEAM) | 20 | 2026-11-02 | 26 | 82% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 248 | [x] | MudRunner (EPIC) | 19 | 2026-10-18 | 40 | 91% |  |
| 249 | [x] | Killing Floor (STEAM) | 19 | 2026-10-19 | 34 | 85% |  |
| 250 | [x] | My Summer Car (STEAM) | 19 | 2026-10-30 | 34 | 86% |  |
| 251 | [x] | Stick It to the Stickman (STEAM) | 19 | 2026-10-17 | 34 | 74% |  |
| 252 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 19 | 2026-10-21 | 33 | 67% |  |
| 253 | [x] | Metro Exodus (STEAM) | 19 | 2026-10-20 | 31 | 90% |  |
| 254 | [x] | Torchlight II (EPIC) | 19 | 2026-10-22 | 27 | 94% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 255 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 18 | 2026-10-25 | 41 | 71% |  |
| 256 | [x] | Styx: Master of Shadows (EPIC) | 18 | 2026-11-03 | 39 | 36% |  |
| 257 | [x] | Backpack Battles (STEAM) | 18 | 2026-10-21 | 37 | 97% |  |
| 258 | [x] | Faster Than Light (EPIC) | 18 | 2026-10-24 | 36 | 100% |  |
| 259 | [x] | Far Far West (STEAM) | 18 | 2026-10-21 | 32 | 78% |  |
| 260 | [x] | Hitman: Absolution (GOG) | 18 | 2026-10-24 | 30 | 75% |  |
| 261 | [x] | Tabletop Simulator (STEAM) | 18 | 2026-10-19 | 30 | 62% |  |
| 262 | [x] | Formula Legends (STEAM) | 18 | 2026-10-21 | 28 | 62% |  |
| 263 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 2026-10-20 | 28 | 81% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 264 | [x] | Arcade Paradise (EPIC) | 18 | 2026-10-25 | 27 | 83% |  |
| 265 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 18 | 2026-10-21 | 27 | 96% |  |
| 266 | [x] | Sonic and SEGA All Stars Racing (STEAM) | 18 | 2026-10-19 | 27 | 73% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 267 | [x] | DOOM 3: BFG Edition (GOG) | 18 | 2026-10-19 | 25 | 80% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 268 | [x] | Katanaut (STEAM) | 18 | 2026-10-20 | 24 | 62% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 269 | [x] | Dorfromantik (GOG) | 18 | 2026-11-04 | 23 | 64% | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 270 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 18 | 2026-10-23 | 23 | 93% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 271 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-01 | 23 | 69% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 272 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 37 | 21% |  |
| 273 | [x] | Mini Metro (STEAM) | 17 | 2026-11-01 | 36 | 50% |  |
| 274 | [x] | Spin Rhythm XD (STEAM) | 17 | 2026-10-18 | 35 | 83% |  |
| 275 | [x] | SKALD: Against the Black Priory (STEAM) | 17 | 2026-10-20 | 34 | 97% |  |
| 276 | [x] | CULTIC (STEAM) | 17 | 2026-10-24 | 33 | 61% |  |
| 277 | [x] | SCP – Containment Breach (STEAM) | 17 | 2026-10-27 | 32 | 85% |  |
| 278 | [x] | GRANDIA HD Remaster (STEAM) | 17 | 2026-10-22 | 31 | 72% |  |
| 279 | [x] | GRIP: Combat Racing (STEAM) | 17 | 2026-10-20 | 31 | 83% |  |
| 280 | [x] | Maneater (STEAM) | 17 | 2026-10-20 | 27 | 77% |  |
| 281 | [x] | Grim Fandango Remastered (GOG) | 17 | 2026-11-03 | 25 | 60% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 282 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 283 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 284 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 51 | 100% |  |
| 285 | [x] | No Man's Sky (GOG) | 16 | 2026-10-19 | 37 | 81% |  |
| 286 | [x] | Grim Fandango Remastered (STEAM) | 16 | 2026-10-19 | 36 | 75% |  |
| 287 | [x] | Kingdom Come: Deliverance II (STEAM) | 16 | 2026-10-20 | 35 | 100% |  |
| 288 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 16 | 2026-10-20 | 34 | 75% |  |
| 289 | [x] | Lost Castle 2 (STEAM) | 16 | 2026-11-02 | 30 | 100% |  |
| 290 | [x] | DNF Duel (EPIC) | 16 | 2026-10-21 | 29 | 91% |  |
| 291 | [x] | Titanfall® 2 (STEAM) | 16 | 2026-10-16 | 29 | 78% |  |
| 292 | [x] | Dishonored 2 (STEAM) | 16 | 2026-10-20 | 26 | 90% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 293 | [x] | Fall Guys (STEAM) | 16 | 2026-10-26 | 22 | 93% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 294 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 2026-10-21 | 22 | 85% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 295 | [x] | Blood Bowl 2 (STEAM) | 16 | 2026-11-04 | 20 | 90% | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 296 | [x] | Jotunnslayer: Hordes of Hel (STEAM) | 16 | 2026-10-30 | 20 | 91% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 297 | [x] | Mark of the Ninja (STEAM) | 15 | 2026-10-26 | 30 | 62% |  |
| 298 | [x] | WORLD OF FINAL FANTASY (STEAM) | 15 | 2026-10-19 | 26 | 81% |  |
| 299 | [x] | Wildermyth (STEAM) | 15 | 2026-10-26 | 26 | 94% |  |
| 300 | [x] | LET IT DIE (STEAM) | 15 | 2026-10-25 | 25 | 73% |  |
| 301 | [x] | Mortal Shell (EPIC) | 15 | 2026-10-19 | 24 | 88% |  |
| 302 | [x] | Batman™: Arkham Origins (GOG) | 15 | 2026-10-22 | 24 | 93% |  |
| 303 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 15 | 2026-10-20 | 23 | 69% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 304 | [x] | Allumeria (STEAM) | 15 | 2026-10-23 | 22 | 73% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 305 | [x] | Chef Knight (STEAM) | 15 | 2026-10-27 | 22 | 69% |  |
| 306 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 307 | [x] | Cyberpunk 2077 (EPIC) | 15 | 2026-10-19 | 20 | 81% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 308 | [x] | Maneater (EPIC) | 15 | 2026-10-28 | 20 | 80% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 309 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 310 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 91% |  |
| 311 | [x] | Antichamber (STEAM) | 14 | 2026-10-20 | 30 | 87% |  |
| 312 | [x] | Rayman Origins (GOG) | 14 | 2026-11-02 | 29 | 59% |  |
| 313 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 2026-10-29 | 28 | 85% |  |
| 314 | [x] | Ultrapool (STEAM) | 14 | 2026-10-24 | 25 | 100% |  |
| 315 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 2026-10-25 | 24 | 72% |  |
| 316 | [x] | Gloomwood (STEAM) | 14 | 2026-10-29 | 24 | 75% |  |
| 317 | [x] | 12 is Better Than 6 (STEAM) | 14 | 2026-10-21 | 23 | 83% |  |
| 318 | [x] | Alabaster Dawn Demo (STEAM) | 14 | 2026-10-27 | 23 | 89% |  |
| 319 | [x] | Super Monkey Ball Banana Mania (STEAM) | 14 | 2026-10-18 | 23 | 65% |  |
| 320 | [x] | Songs of Conquest (EPIC) | 14 | 2026-11-02 | 22 | 90% |  |
| 321 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-10-23 | 22 | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 322 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 323 | [x] | Sons Of The Forest (STEAM) | 14 | 2026-10-19 | 22 | 74% |  |
| 324 | [x] | Horny Villa (STEAM) | 14 | 2026-10-21 | 20 | 95% |  |
| 325 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 326 | [x] | Middle-earth™: Shadow of War™ (STEAM) | 13 | 2026-10-16 | 39 | 73% |  |
| 327 | [x] | Blood: Fresh Supply (STEAM) | 13 | 2026-10-16 | 36 | 76% |  |
| 328 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 13 | 2026-10-21 | 35 | 84% |  |
| 329 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 32 | 60% |  |
| 330 | [x] | Distance (STEAM) | 13 | 2026-10-19 | 30 | 80% |  |
| 331 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 13 | 2026-10-19 | 30 | 98% |  |
| 332 | [x] | Haiku, the Robot (STEAM) | 13 | 2026-10-21 | 29 | 85% |  |
| 333 | [x] | Breath of Fire IV (GOG) | 13 | 2026-10-26 | 28 | 68% |  |
| 334 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 28 | 53% |  |
| 335 | [x] | Aperture Desk Job (STEAM) | 13 | 2026-11-03 | 27 | n/a |  |
| 336 | [x] | Evoland (STEAM) | 13 | 2026-11-05 | 27 | n/a |  |
| 337 | [x] | Human Fall Flat (STEAM) | 13 | 2026-10-29 | 27 | 62% |  |
| 338 | [x] | Lust Goddess (STEAM) | 13 | 2026-10-26 | 25 | 64% |  |
| 339 | [x] | DiRT 4 (STEAM) | 13 | 2026-10-20 | 23 | 96% |  |
| 340 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-10-21 | 22 | 90% |  |
| 341 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 13 | 2026-10-28 | 21 | 64% |  |
| 342 | [x] | PAYDAY: The Heist (STEAM) | 13 | 2026-11-02 | 21 | 69% |  |
| 343 | [x] | Shift At Midnight (STEAM) | 13 | 2026-11-01 | 21 | 92% |  |
| 344 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 345 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 13 | 2026-10-23 | 20 | 61% |  |
| 346 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 81% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 347 | [x] | The WereCleaner (STEAM) | 12 | 2026-10-22 | 31 | 88% |  |
| 348 | [x] | Tom Clancy's Splinter Cell: Chaos Theory (STEAM) | 12 | 2026-10-16 | 30 | 84% |  |
| 349 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 12 | 2026-11-01 | 27 | 60% |  |
| 350 | [x] | Dead Space™ 3 (STEAM) | 12 | 2026-10-20 | 27 | 74% |  |
| 351 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 12 | 2026-10-18 | 27 | 92% |  |
| 352 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 26 | 68% |  |
| 353 | [x] | Revolution Idle (STEAM) | 12 | 2026-11-05 | 26 | n/a |  |
| 354 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-10-28 | 24 | 93% |  |
| 355 | [x] | Sonic Superstars (STEAM) | 12 | 2026-10-21 | 24 | 65% |  |
| 356 | [x] | Haydee (STEAM) | 12 | 2026-10-22 | 23 | 82% |  |
| 357 | [x] | Pillars of Eternity (STEAM) | 12 | 2026-10-26 | 23 | 62% |  |
| 358 | [x] | UNDEFEATED (STEAM) | 12 | 2026-11-01 | 23 | 77% |  |
| 359 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-10-22 | 22 | 90% |  |
| 360 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 2026-10-26 | 22 | 88% |  |
| 361 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 362 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 363 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 364 | [x] | Mortal Kombat 11 (STEAM) | 11 | 2026-10-28 | 25 | 68% |  |
| 365 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 2026-10-27 | 23 | 84% |  |
| 366 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 23 | 76% |  |
| 367 | [x] | Castle in the Clouds (STEAM) | 11 | 2026-10-21 | 22 | 86% |  |
| 368 | [x] | Injustice™ 2 (STEAM) | 11 | 2026-10-17 | 22 | 75% |  |
| 369 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 11 | 2026-10-23 | 22 | 94% |  |
| 370 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 2026-10-25 | 21 | 95% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 371 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-10-24 | 21 | 75% |  |
| 372 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 373 | [x] | TowerFall Ascension (STEAM) | 10 | 2026-10-16 | 31 | 56% |  |
| 374 | [x] | Possessor(s) (STEAM) | 10 | 2026-10-24 | 27 | 100% |  |
| 375 | [x] | Divinity: Original Sin (Classic) (STEAM) | 10 | 2026-10-16 | 25 | 83% |  |
| 376 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 10 | 2026-10-20 | 25 | 73% |  |
| 377 | [x] | DRAGON BALL XENOVERSE (STEAM) | 10 | 2026-10-28 | 23 | 50% |  |
| 378 | [x] | Mina the Hollower (GOG) | 10 | 2026-10-28 | 22 | 59% |  |
| 379 | [x] | SteamWorld Heist (GOG) | 10 | 2026-10-25 | 22 | n/a |  |
| 380 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 22 | 90% |  |
| 381 | [x] | Sid Meier's Civilization VI (EPIC) | 10 | 2026-10-19 | 21 | 91% |  |
| 382 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 383 | [x] | Coromon (GOG) | 10 | 2026-10-19 | 20 | 64% |  |
| 384 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 385 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 20 | 70% |  |
| 386 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 387 | [x] | Delver (STEAM) | 9 | 2026-10-17 | 22 | 76% |  |
| 388 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 9 | 2026-10-23 | 21 | 71% |  |
| 389 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 9 | 2026-10-21 | 20 | 93% |  |
| 390 | [x] | Football Manager 2024 (STEAM) | 9 | 2026-10-16 | 20 | n/a |  |
| 391 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 14% |  |
| 392 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 9 | 2026-10-20 | 20 | n/a |  |
| 393 | [x] | Gloomhaven (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 394 | [x] | Intravenous (STEAM) | 8 | 2026-10-16 | 20 | 94% |  |
| 395 | [x] | What Remains of Edith Finch (STEAM) | 7 | 2026-10-19 | 24 | 50% |  |
| 396 | [x] | Mafia II: Definitive Edition (STEAM) | 7 | 2026-10-16 | 20 | n/a |  |
| 397 | [x] | Alex Kidd in Miracle World DX (STEAM) | 2 | 2026-10-16 | 36 | 88% |  |
