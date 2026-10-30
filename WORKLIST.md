# GameNative compatibility worklist

Generated: `2026-10-30T04:15:05.689Z` · App release: `1.3.0` · Ratings since: `2026-08-01T04:15:05.689Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 280 |
| Probably does not work | 95 |
| First launch fails | 363 |
| Mixed | 461 |
| Works | 1008 |
| Total | 2207 |

## Does not work (280)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [x] 2026-10-18 | Project Zomboid (STEAM) | 626 | 665 | 92% (1.3.0) | Does not open (66%) | 49% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 2 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 264 | 283 | 93% (90d) | Does not open (75%) | 9% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 3 | [x] 2026-10-18 | Alan Wake (STEAM) | 256 | 267 | 89% (1.3.0) | Does not open (86%) | 8% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 4 | [ ] | Counter-Strike 2 (STEAM) | 229 | 317 | 84% (1.3.0) | Does not open (61%) | 43% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 5 | [x] 2026-10-18 | Call of Duty: Black Ops (STEAM) | 216 | 226 | 96% (90d) | Does not open (75%) | 14% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 6 | [ ] | DRAGON BALL FighterZ (STEAM) | 215 | 243 | 76% (1.3.0) | Does not open (87%) | 58% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 7 | [ ] | skate. (STEAM) | 204 | 220 | 93% (90d) | Does not open (80%) | 18% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 8 | [x] 2026-10-18 | Sid Meier's Civilization V (STEAM) | 180 | 192 | 94% (90d) | Does not open (77%) | 50% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 9 | [ ] | Necesse (STEAM) | 178 | 184 | 97% (90d) | Does not open (80%) | 54% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 10 | [ ] | Peggle Deluxe (STEAM) | 161 | 192 | 84% (90d) | Does not open (92%) | 40% | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 11 | [ ] | Sonic Adventure™ 2  (STEAM) | 150 | 209 | 72% (90d) | Does not open (75%) | 55% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 12 | [ ] | HELLDIVERS™ 2 (STEAM) | 142 | 149 | 95% (90d) | Does not open (92%) | 24% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 13 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 137 | 153 | 90% (90d) | Does not open (87%) | 48% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 14 | [ ] | Assassin's Creed II (STEAM) | 132 | 137 | 96% (90d) | Does not open (78%) | 50% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 15 | [ ] | Sol Cesto (EPIC) | 120 | 126 | 95% (90d) | Does not open (75%) | 58% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 16 | [ ] | Dust: An Elysian Tail (STEAM) | 109 | 113 | 96% (90d) | Does not open (71%) | 8% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 17 | [ ] | Call of Duty: Black Ops II (STEAM) | 108 | 141 | 77% (90d) | Does not open (77%) | 23% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 18 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 108 | 121 | 89% (90d) | No graphics (59%) | 55% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 19 | [ ] | Transistor (STEAM) | 105 | 105 | 100% (90d) | Does not open (77%) | 0% | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 20 | [ ] | The Witcher: Enhanced Edition (GOG) | 103 | 113 | 91% (90d) | Does not open (75%) | 14% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 21 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 102 | 136 | 75% (90d) | Does not open (75%) | 41% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 22 | [ ] | Mafia II (Classic) (STEAM) | 98 | 103 | 95% (90d) | Does not open (71%) | 7% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 23 | [ ] | Saints Row: The Third (STEAM) | 94 | 95 | 99% (90d) | Does not open (78%) | 30% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 24 | [ ] | Saints Row 2 (STEAM) | 92 | 105 | 91% (1.3.0) | Does not open (96%) | 40% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 25 | [ ] | Fall Guys (EPIC) | 92 | 104 | 88% (90d) | Does not open (73%) | 6% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 26 | [ ] | Black Mesa (STEAM) | 87 | 121 | 72% (90d) | Does not open (82%) | 14% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 27 | [ ] | Dead Space 2 (STEAM) | 87 | 109 | 80% (90d) | Does not open (76%) | 36% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 28 | [ ] | Duskfade (STEAM) | 87 | 89 | 98% (90d) | Does not open (95%) | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 29 | [ ] | HELLDIVERS™ (STEAM) | 83 | 97 | 86% (90d) | Does not open (60%) | 44% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 30 | [ ] | Sniper Elite 4 (STEAM) | 83 | 83 | 100% (90d) | Does not open (97%) | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 31 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 78 | 84 | 93% (90d) | Does not open (71%) | 0% | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 32 | [ ] | GRID 2 (STEAM) | 78 | 82 | 95% (90d) | Does not open (66%) | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 33 | [ ] | The Wolf Among Us (STEAM) | 76 | 85 | 89% (90d) | Does not open (68%) | 8% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 34 | [ ] | Burnout™ Paradise Remastered (STEAM) | 75 | 79 | 95% (90d) | Does not open (88%) | 18% | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 35 | [ ] | Call of Duty: Black Ops II - Zombies (STEAM) | 74 | 87 | 85% (90d) | Does not open (71%) | 48% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 36 | [ ] | Saints Row 2 (GOG) | 73 | 86 | 85% (90d) | Does not open (97%) | 49% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 37 | [ ] | Marvel Rivals (STEAM) | 72 | 80 | 90% (90d) | Does not open (81%) | 0% | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 38 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 71 | 76 | 93% (90d) | Does not open (78%) | 9% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 39 | [ ] | Borderlands GOTY (STEAM) | 70 | 75 | 93% (90d) | Does not open (95%) | 27% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 40 | [ ] | Need for Speed™ Heat  (STEAM) | 68 | 82 | 83% (90d) | Does not open (79%) | 30% | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 41 | [x] 2026-10-18 | Diablo® IV (STEAM) | 68 | 80 | 85% (90d) | Does not open (62%) | 20% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 42 | [ ] | Metro 2033 (STEAM) | 67 | 83 | 81% (90d) | Does not open (66%) | 54% | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 43 | [ ] | Door Kickers 2 (STEAM) | 67 | 71 | 94% (90d) | No graphics (85%) | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 44 | [ ] | XCOM: Enemy Unknown (STEAM) | 67 | 70 | 96% (90d) | Does not open (75%) | 8% | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 45 | [ ] | GRID (STEAM) | 66 | 83 | 80% (90d) | Does not open (54%) | 50% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 46 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 65 | 65 | 100% (90d) | No graphics (54%) | 8% | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 47 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 64 | 73 | 88% (90d) | Does not open (48%) | 21% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 48 | [ ] | Three Kingdoms : Alias (STEAM) | 62 | 66 | 94% (90d) | No graphics (97%) | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 49 | [ ] | DOOM (2016) (GOG) | 61 | 67 | 91% (90d) | Does not open (91%) | 44% | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 50 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 60 | 86 | 70% (90d) | Does not open (84%) | 56% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 51 | [ ] | Spore (STEAM) | 59 | 64 | 92% (90d) | Does not open (68%) | n/a | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 52 | [ ] | GrandChase (STEAM) | 57 | 60 | 95% (90d) | Does not open (85%) | 10% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 53 | [ ] | Overwatch® (STEAM) | 57 | 59 | 97% (90d) | Does not open (59%) | 17% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 54 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 56 | 70 | 80% (90d) | Does not open (89%) | 55% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 55 | [ ] | Spec Ops: The Line (STEAM) | 56 | 57 | 98% (90d) | Does not open (56%) | 0% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 56 | [ ] | METAL SLUG 3 (STEAM) | 55 | 63 | 87% (90d) | Does not open (84%) | 17% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 57 | [ ] | Max Payne 3 (STEAM) | 55 | 60 | 92% (90d) | Does not open (93%) | 44% | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 58 | [ ] | Fortune Mill (STEAM) | 55 | 56 | 98% (90d) | Does not open (89%) | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 59 | [ ] | Vampire Survivors (EPIC) | 54 | 76 | 71% (90d) | Does not open (65%) | 56% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 60 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 54 | 69 | 78% (90d) | Does not open (82%) | 31% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 61 | [ ] | Watch_Dogs (STEAM) | 54 | 69 | 78% (90d) | Does not open (91%) | 19% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 62 | [ ] | DOOM 3 (STEAM) | 54 | 61 | 89% (90d) | Does not open (90%) | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 63 | [ ] | RoboCop: Rogue City (STEAM) | 53 | 57 | 93% (90d) | Does not open (40%) | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 64 | [ ] | STAR WARS Zero Company™ (STEAM) | 53 | 55 | 96% (90d) | Does not open (64%) | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 65 | [ ] | Trackmania (STEAM) | 52 | 66 | 79% (90d) | Does not open (86%) | 47% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 66 | [ ] | Asphalt Legends  (STEAM) | 52 | 60 | 87% (90d) | Does not open (79%) | 42% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 67 | [ ] | Enshrouded (STEAM) | 52 | 53 | 98% (90d) | Does not open (92%) | 17% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 68 | [ ] | South Park The Fractured But Whole (STEAM) | 52 | 52 | 100% (90d) | Does not open (66%) | 17% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 69 | [ ] | Split/Second (STEAM) | 51 | 60 | 85% (90d) | Does not open (76%) | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 70 | [ ] | Hitman: Absolution (STEAM) | 51 | 56 | 91% (90d) | Does not open (84%) | 8% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 71 | [ ] | Sandustry (STEAM) | 50 | 62 | 81% (90d) | Does not open (73%) | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 72 | [ ] | Watch_Dogs 2 (STEAM) | 50 | 56 | 89% (90d) | Does not open (97%) | 59% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 73 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 49 | 51 | 96% (90d) | No graphics (60%) | 20% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 74 | [ ] | Scott Pilgrim vs The World (STEAM) | 49 | 49 | 100% (90d) | Does not open (83%) | 50% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 75 | [ ] | tModLoader (STEAM) | 48 | 55 | 87% (90d) | Does not open (84%) | 4% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 76 | [ ] | DOOM Eternal (STEAM) | 48 | 50 | 96% (90d) | Does not open (69%) | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 77 | [ ] | ARC Raiders (STEAM) | 47 | 52 | 90% (90d) | Does not open (93%) | 0% | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 78 | [ ] | Aliens vs. Predator (STEAM) | 47 | 52 | 90% (90d) | No graphics (53%) | 22% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 79 | [ ] | Prince of Persia The Lost Crown (STEAM) | 46 | 51 | 90% (90d) | Does not open (94%) | 41% | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 80 | [ ] | STAR WARS™ Republic Commando (STEAM) | 46 | 49 | 94% (90d) | Does not open (80%) | 50% | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 81 | [ ] | The Survivalists (STEAM) | 46 | 48 | 96% (90d) | Does not open (98%) | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 82 | [ ] | State of Decay 2 (STEAM) | 45 | 64 | 70% (90d) | Does not open (93%) | 0% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 83 | [ ] | Mafia: Definitive Edition (GOG) | 45 | 60 | 75% (90d) | Does not open (86%) | 25% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 84 | [ ] | Diablo + Hellfire (GOG) | 45 | 50 | 90% (90d) | Does not open (66%) | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 85 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 45 | 48 | 94% (90d) | Does not open (95%) | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 86 | [ ] | Tales of Berseria (STEAM) | 45 | 46 | 98% (90d) | Does not open (88%) | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 87 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 44 | 45 | 98% (90d) | Does not open (82%) | 42% | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 88 | [ ] | Need for Speed™ Rivals (STEAM) | 42 | 50 | 84% (90d) | Does not open (56%) | 39% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 89 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 42 | 47 | 89% (90d) | Does not open (75%) | 12% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 90 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 41 | 42 | 98% (90d) | Does not open (61%) | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 91 | [ ] | GOALS (STEAM) | 40 | 47 | 85% (90d) | Does not open (79%) | 24% | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 92 | [ ] | DJMAX RESPECT V (STEAM) | 40 | 44 | 91% (90d) | Does not open (83%) | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 93 | [ ] | Elite Dangerous (STEAM) | 40 | 43 | 93% (90d) | Does not open (79%) | 54% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 94 | [ ] | Mafia (STEAM) | 39 | 44 | 89% (90d) | Does not open (70%) | 41% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 95 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 39 | 41 | 95% (90d) | Does not open (94%) | 27% | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 96 | [ ] | GeoGuessr Steam Edition (STEAM) | 39 | 40 | 98% (90d) | No graphics (62%) | n/a | [#154](https://github.com/GameNative/gamenative-compat/issues/154) |
| 97 | [ ] | Utopia Must Fall (STEAM) | 39 | 39 | 100% (90d) | Does not open (84%) | n/a | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 98 | [ ] | Marvel's Spider-Man 2 (STEAM) | 38 | 40 | 95% (90d) | Does not open (87%) | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 99 | [ ] | Forza Horizon 6 (STEAM) | 38 | 39 | 97% (90d) | Does not open (64%) | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 100 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 38 | 39 | 97% (90d) | Does not open (57%) | 0% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 101 | [ ] | FINAL FANTASY VIII (STEAM) | 37 | 44 | 84% (90d) | Does not open (64%) | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 102 | [ ] | L.A. Noire (STEAM) | 37 | 44 | 84% (90d) | Does not open (96%) | 53% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 103 | [ ] | ScourgeBringer (STEAM) | 37 | 42 | 88% (90d) | Does not open (66%) | 6% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 104 | [ ] | Barotrauma (STEAM) | 37 | 40 | 93% (90d) | Does not open (97%) | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 105 | [ ] | BIT.TRIP RUNNER (STEAM) | 37 | 39 | 95% (90d) | Does not open (59%) | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 106 | [ ] | Dragon's Dogma 2 (STEAM) | 37 | 38 | 97% (90d) | Does not open (91%) | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 107 | [ ] | Mafia II (Classic) (GOG) | 36 | 51 | 71% (90d) | Does not open (94%) | 27% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 108 | [ ] | CODE VEIN (STEAM) | 36 | 48 | 75% (90d) | Does not open (69%) | 29% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 109 | [ ] | Beat Saber (STEAM) | 36 | 42 | 86% (90d) | Does not open (45%) | 35% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 110 | [ ] | Beholder (EPIC) | 35 | 42 | 83% (90d) | Does not open (58%) | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 111 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 35 | 41 | 85% (90d) | No graphics (69%) | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 112 | [ ] | OneShot (STEAM) | 35 | 40 | 88% (90d) | Does not open (97%) | 25% | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 113 | [ ] | BattleBit Remastered (STEAM) | 35 | 39 | 90% (90d) | Does not open (61%) | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 114 | [ ] | Forza Horizon 5 (STEAM) | 35 | 37 | 95% (90d) | Does not open (64%) | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 115 | [ ] | CARRION (GOG) | 34 | 42 | 81% (90d) | Does not open (75%) | 8% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 116 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 34 | 39 | 87% (90d) | Does not open (68%) | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 117 | [ ] | Death Stranding (EPIC) | 34 | 37 | 92% (90d) | Does not open (75%) | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 118 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 34 | 37 | 92% (90d) | Does not open (67%) | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 119 | [ ] | Yume Nikki (STEAM) | 33 | 52 | 87% (14d) | Does not open (94%) | 0% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 120 | [ ] | Lost Planet: Extreme Condition (STEAM) | 33 | 40 | 83% (90d) | Does not open (80%) | 56% | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 121 | [ ] | Mass Effect (2007) (STEAM) | 33 | 39 | 85% (90d) | Does not open (81%) | 54% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 122 | [ ] | Wolfenstein 3D (STEAM) | 33 | 36 | 92% (90d) | Does not open (52%) | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 123 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 33 | 35 | 94% (90d) | Does not open (74%) | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 124 | [ ] | The Darkness II (STEAM) | 33 | 33 | 100% (90d) | Does not open (83%) | 30% | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 125 | [ ] | Gauntlet™  (STEAM) | 32 | 45 | 71% (90d) | Does not open (67%) | 40% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 126 | [ ] | Far Cry 4 (STEAM) | 32 | 36 | 89% (90d) | Does not open (100%) | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 127 | [ ] | PRAGMATA (STEAM) | 32 | 34 | 94% (90d) | Does not open (57%) | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 128 | [ ] | DiRT Showdown (STEAM) | 32 | 33 | 97% (90d) | Does not open (60%) | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 129 | [ ] | Rayman Legends (STEAM) | 32 | 33 | 97% (90d) | Does not open (96%) | 54% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 130 | [ ] | Umamusume: Pretty Derby (STEAM) | 32 | 33 | 97% (90d) | Does not open (83%) | n/a | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 131 | [ ] | Quantum Break (STEAM) | 32 | 32 | 100% (90d) | Does not open (91%) | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 132 | [ ] | Metro: Last Light Redux (STEAM) | 31 | 88 | 82% (14d) | Does not open (90%) | 45% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 133 | [ ] | Dark Sector (STEAM) | 31 | 41 | 76% (90d) | Does not open (68%) | 43% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 134 | [ ] | Insaniquarium! Deluxe (STEAM) | 31 | 39 | 79% (90d) | Does not open (86%) | 33% | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 135 | [ ] | CPM 2 (STEAM) | 31 | 38 | 82% (90d) | Does not open (91%) | 7% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 136 | [ ] | Metro: Last Light Complete Edition (STEAM) | 31 | 38 | 82% (90d) | Does not open (56%) | 57% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 137 | [ ] | King's Bounty: The Legend (STEAM) | 31 | 34 | 91% (90d) | Does not open (100%) | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 138 | [ ] | Muv-Luv (STEAM) | 31 | 32 | 97% (90d) | Does not open (86%) | 42% | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 139 | [ ] | Magicka (STEAM) | 30 | 33 | 91% (90d) | Does not open (64%) | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 140 | [ ] | The Lord of the Rings: War in the North (STEAM) | 30 | 32 | 94% (90d) | Does not open (85%) | n/a | [#195](https://github.com/GameNative/gamenative-compat/issues/195) |
| 141 | [ ] | Hitman: Blood Money (STEAM) | 30 | 31 | 97% (90d) | Does not open (89%) | 12% | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 142 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 30 | 31 | 97% (90d) | Does not open (95%) | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 143 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 30 | 30 | 100% (90d) | Does not open (72%) | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 144 | [ ] | Grand Theft Auto III - The Definitive Edition (STEAM) | 30 | 30 | 100% (90d) | Does not open (92%) | 16% | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 145 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 29 | 39 | 74% (90d) | Does not open (65%) | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 146 | [ ] | EA SPORTS FC™ 26 (STEAM) | 29 | 37 | 78% (90d) | Does not open (77%) | n/a | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 147 | [ ] | Subnautica 2 (STEAM) | 29 | 35 | 83% (90d) | Does not open (68%) | 50% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 148 | [ ] | Alpha Protocol (STEAM) | 29 | 33 | 88% (90d) | Does not open (60%) | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 149 | [ ] | Zuma Deluxe (STEAM) | 29 | 32 | 91% (90d) | Does not open (96%) | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 150 | [ ] | Borderlands 2 RU (STEAM) | 29 | 31 | 94% (90d) | Does not open (60%) | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 151 | [ ] | Breath of Fire IV (STEAM) | 29 | 29 | 100% (90d) | Does not open (58%) | 19% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 152 | [ ] | Audiosurf (STEAM) | 28 | 39 | 72% (90d) | Does not open (46%) | 50% | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 153 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 28 | 28 | 100% (90d) | Does not open (68%) | 0% | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 154 | [ ] | Mirror's Edge™ (GOG) | 27 | 38 | 71% (90d) | No graphics (62%) | 46% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 155 | [ ] | The Planet Crafter (STEAM) | 27 | 33 | 82% (90d) | Does not open (52%) | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 156 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 27 | 30 | 90% (90d) | Does not open (81%) | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 157 | [ ] | PAYDAY 2 (STEAM) | 27 | 30 | 90% (90d) | Does not open (78%) | 38% | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 158 | [ ] | Persona 5 Strikers (STEAM) | 27 | 30 | 90% (90d) | Does not open (75%) | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 159 | [ ] | WRC 7 (STEAM) | 27 | 28 | 96% (90d) | Does not open (72%) | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 160 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 27 | 27 | 100% (90d) | Does not open (60%) | 10% | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 161 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 26 | 33 | 79% (90d) | Does not open (50%) | 13% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 162 | [ ] | Singularity™ (GOG) | 26 | 31 | 84% (90d) | Does not open (100%) | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 163 | [ ] | Sir, We Have an Orc Problem (STEAM) | 26 | 30 | 87% (90d) | Does not open (75%) | n/a | [#145](https://github.com/GameNative/gamenative-compat/issues/145) |
| 164 | [ ] | AION 2 (STEAM) | 26 | 28 | 93% (90d) | Does not open (65%) | 10% | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 165 | [ ] | Alien Breed: Impact (STEAM) | 26 | 28 | 93% (90d) | Does not open (80%) | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 166 | [ ] | Axiom Verge 2 (STEAM) | 26 | 27 | 96% (90d) | Does not open (77%) | 12% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 167 | [ ] | Northgard: Definitive Edition (STEAM) | 26 | 27 | 96% (90d) | Does not open (96%) | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 168 | [ ] | Isle of Reveries (STEAM) | 26 | 26 | 100% (90d) | Does not open (95%) | 27% | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 169 | [ ] | Resident Evil Requiem (STEAM) | 26 | 26 | 100% (90d) | Does not open (76%) | n/a | [#210](https://github.com/GameNative/gamenative-compat/issues/210) |
| 170 | [ ] | Content Warning (STEAM) | 25 | 33 | 76% (90d) | Does not open (55%) | n/a | [#241](https://github.com/GameNative/gamenative-compat/issues/241) |
| 171 | [ ] | Kenshi (STEAM) | 25 | 32 | 78% (90d) | Does not open (79%) | 12% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 172 | [ ] | Knights of Pen and Paper 2 (STEAM) | 25 | 32 | 78% (90d) | Does not open (45%) | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 173 | [ ] | ENDLESS Space™ 2 (STEAM) | 25 | 30 | 83% (90d) | Does not open (94%) | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 174 | [ ] | Bionic Commando Rearmed (STEAM) | 25 | 28 | 89% (90d) | Does not open (74%) | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 175 | [ ] | Turing Complete (STEAM) | 25 | 28 | 89% (90d) | Does not open (91%) | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 176 | [ ] | Bingle Bingle (STEAM) | 25 | 26 | 96% (90d) | Does not open (80%) | n/a | [#225](https://github.com/GameNative/gamenative-compat/issues/225) |
| 177 | [ ] | Euro Truck Simulator (STEAM) | 25 | 26 | 96% (90d) | Does not open (94%) | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 178 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 25 | 26 | 96% (90d) | Does not open (81%) | 36% | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 179 | [ ] | Spiral Knights (STEAM) | 25 | 25 | 100% (90d) | Does not open (74%) | n/a | [#263](https://github.com/GameNative/gamenative-compat/issues/263) |
| 180 | [ ] | Cities: Skylines (STEAM) | 24 | 34 | 71% (90d) | Does not open (59%) | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 181 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 24 | 34 | 71% (90d) | Does not open (95%) | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 182 | [ ] | CarX Street (STEAM) | 24 | 31 | 77% (90d) | Does not open (80%) | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 183 | [ ] | SOMA (STEAM) | 24 | 31 | 77% (90d) | Does not open (75%) | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 184 | [ ] | Transformers: Fall of Cybertron (STEAM) | 24 | 31 | 77% (90d) | Does not open (65%) | 30% | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 185 | [ ] | My Singing Monsters (STEAM) | 24 | 30 | 80% (90d) | Does not open (83%) | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 186 | [ ] | The Swapper (STEAM) | 24 | 28 | 86% (90d) | Does not open (52%) | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 187 | [ ] | Jade Empire: Special Edition (STEAM) | 24 | 26 | 92% (90d) | Does not open (95%) | 59% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 188 | [ ] | Peggle Nights (STEAM) | 24 | 26 | 92% (90d) | Does not open (94%) | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 189 | [ ] | Call of Duty® (STEAM) | 23 | 32 | 72% (90d) | Does not open (65%) | 7% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 190 | [ ] | SimCity 4 Deluxe (STEAM) | 23 | 27 | 85% (90d) | Does not open (82%) | 50% | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 191 | [ ] | skate.™ (EPIC) | 23 | 27 | 85% (90d) | Does not open (88%) | 9% | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 192 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 23 | 26 | 88% (90d) | Does not open (95%) | 58% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 193 | [ ] | They Are Billions (STEAM) | 23 | 26 | 88% (90d) | Does not open (70%) | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 194 | [ ] | Wuthering Waves (STEAM) | 23 | 25 | 92% (90d) | Does not open (86%) | n/a | [#216](https://github.com/GameNative/gamenative-compat/issues/216) |
| 195 | [ ] | Gears 5 (STEAM) | 23 | 23 | 100% (90d) | Does not open (88%) | n/a | [#264](https://github.com/GameNative/gamenative-compat/issues/264) |
| 196 | [ ] | Marie's Adventure (STEAM) | 23 | 23 | 100% (90d) | Does not open (100%) | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 197 | [ ] | Beat Cop (STEAM) | 22 | 30 | 73% (90d) | Does not open (76%) | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 198 | [ ] | Half-Life: Blue Shift (STEAM) | 22 | 26 | 85% (90d) | Does not open (85%) | n/a | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 199 | [ ] | Tom Clancy's Ghost Recon® Wildlands (STEAM) | 22 | 26 | 85% (90d) | Does not open (94%) | n/a | [#280](https://github.com/GameNative/gamenative-compat/issues/280) |
| 200 | [ ] | Melatonin (STEAM) | 22 | 23 | 96% (90d) | Does not open (58%) | 45% | [#272](https://github.com/GameNative/gamenative-compat/issues/272) |
| 201 | [ ] | The Lantern of the Laughless Saint (STEAM) | 22 | 23 | 96% (90d) | Does not open (79%) | n/a | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 202 | [ ] | Need for Speed: Undercover (STEAM) | 21 | 30 | 70% (90d) | Does not open (88%) | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 203 | [ ] | TEKKEN 8 (STEAM) | 21 | 28 | 75% (90d) | Does not open (76%) | 50% | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 204 | [ ] | Aggelos 2 (STEAM) | 21 | 27 | 78% (90d) | No graphics (90%) | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 205 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 21 | 27 | 78% (90d) | Does not open (62%) | n/a | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 206 | [ ] | Beyond Good & Evil™ (GOG) | 21 | 26 | 81% (90d) | Does not open (100%) | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 207 | [ ] | PICO PARK:Classic Edition (STEAM) | 21 | 25 | 84% (90d) | Does not open (90%) | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 208 | [ ] | Clive Barker's Undying (GOG) | 21 | 24 | 88% (90d) | Does not open (67%) | n/a | [#388](https://github.com/GameNative/gamenative-compat/issues/388) |
| 209 | [ ] | Dragon Age™ Inquisition (STEAM) | 21 | 24 | 88% (90d) | Does not open (76%) | 33% | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 210 | [ ] | Halo: Spartan Assault (STEAM) | 21 | 24 | 88% (90d) | Does not open (83%) | 31% | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 211 | [ ] | Marvel's Midnight Suns (STEAM) | 21 | 24 | 88% (90d) | Does not open (84%) | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 212 | [ ] | Sapphire Safari (GOG) | 21 | 24 | 88% (90d) | Does not open (89%) | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 213 | [ ] | Apex Legends (STEAM) | 21 | 23 | 91% (90d) | Does not open (74%) | n/a | [#261](https://github.com/GameNative/gamenative-compat/issues/261) |
| 214 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 21 | 23 | 91% (90d) | Does not open (90%) | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 215 | [ ] | Pathway (EPIC) | 21 | 22 | 95% (90d) | Does not open (63%) | n/a | [#298](https://github.com/GameNative/gamenative-compat/issues/298) |
| 216 | [ ] | Rayman Legends (EPIC) | 21 | 22 | 95% (90d) | Does not open (92%) | n/a | [#286](https://github.com/GameNative/gamenative-compat/issues/286) |
| 217 | [ ] | Chronicles of the Wolf (STEAM) | 21 | 21 | 100% (90d) | No graphics (85%) | n/a | [#314](https://github.com/GameNative/gamenative-compat/issues/314) |
| 218 | [ ] | Resident Evil 3 Nemesis (1999) (STEAM) | 21 | 21 | 100% (90d) | Does not open (86%) | n/a | [#273](https://github.com/GameNative/gamenative-compat/issues/273) |
| 219 | [ ] | Return to Castle Wolfenstein (STEAM) | 21 | 21 | 100% (90d) | Does not open (95%) | 20% | [#321](https://github.com/GameNative/gamenative-compat/issues/321) |
| 220 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 21 | 21 | 100% (90d) | Does not open (71%) | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 221 | [ ] | Fishing Planet (STEAM) | 20 | 28 | 71% (90d) | Does not open (93%) | 31% | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 222 | [ ] | Dungeon Keeper™ 2 (GOG) | 20 | 27 | 74% (90d) | Does not open (100%) | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 223 | [ ] | Surviving Mars (STEAM) | 20 | 26 | 77% (90d) | Does not open (92%) | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 224 | [ ] | Assassin's Creed Brotherhood (STEAM) | 20 | 23 | 87% (90d) | Does not open (78%) | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 225 | [ ] | Grounded 2 (STEAM) | 20 | 21 | 95% (90d) | Does not open (56%) | n/a | [#317](https://github.com/GameNative/gamenative-compat/issues/317) |
| 226 | [ ] | Mirror's Edge™ Catalyst (STEAM) | 20 | 21 | 95% (90d) | Does not open (67%) | 50% | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 227 | [ ] | No More Room in Hell (STEAM) | 20 | 21 | 95% (90d) | Does not open (94%) | n/a | [#365](https://github.com/GameNative/gamenative-compat/issues/365) |
| 228 | [ ] | The Last of Us™ Part I (STEAM) | 20 | 21 | 95% (90d) | Does not open (93%) | n/a | [#300](https://github.com/GameNative/gamenative-compat/issues/300) |
| 229 | [ ] | DiRT 2 (STEAM) | 20 | 20 | 100% (90d) | Does not open (85%) | n/a | [#471](https://github.com/GameNative/gamenative-compat/issues/471) |
| 230 | [ ] | Downfall - A Slay the Spire Fan Expansion (STEAM) | 20 | 20 | 100% (90d) | Does not open (68%) | n/a | [#320](https://github.com/GameNative/gamenative-compat/issues/320) |
| 231 | [ ] | Fogpiercer (STEAM) | 19 | 26 | 73% (90d) | Does not open (79%) | n/a | [#303](https://github.com/GameNative/gamenative-compat/issues/303) |
| 232 | [ ] | Yuppie Psycho (STEAM) | 19 | 26 | 73% (90d) | Does not open (75%) | n/a | [#325](https://github.com/GameNative/gamenative-compat/issues/325) |
| 233 | [ ] | Tyr (STEAM) | 19 | 25 | 76% (90d) | Does not open (33%) | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 234 | [ ] | Mafia III: Definitive Edition (STEAM) | 19 | 22 | 86% (90d) | Does not open (95%) | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 235 | [ ] | Rune Factory 5 (STEAM) | 19 | 22 | 86% (90d) | Does not open (84%) | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 236 | [ ] | The Elder Scrolls IV: Oblivion Remastered (STEAM) | 19 | 22 | 86% (90d) | Does not open (59%) | n/a | [#312](https://github.com/GameNative/gamenative-compat/issues/312) |
| 237 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 19 | 22 | 86% (90d) | Does not open (79%) | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 238 | [ ] | Gothic 1 Remake (STEAM) | 19 | 21 | 90% (90d) | Directx error (44%) | n/a | [#336](https://github.com/GameNative/gamenative-compat/issues/336) |
| 239 | [ ] | GT Legends (STEAM) | 19 | 20 | 95% (90d) | Does not open (89%) | n/a | [#364](https://github.com/GameNative/gamenative-compat/issues/364) |
| 240 | [ ] | Jurassic World Evolution (EPIC) | 19 | 20 | 95% (90d) | Does not open (80%) | n/a | [#469](https://github.com/GameNative/gamenative-compat/issues/469) |
| 241 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 19 | 20 | 95% (90d) | Does not open (64%) | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 242 | [ ] | Zenless Zone Zero (STEAM) | 19 | 20 | 95% (90d) | Does not open (76%) | n/a | [#369](https://github.com/GameNative/gamenative-compat/issues/369) |
| 243 | [ ] | We Were Here Together (EPIC) | 18 | 24 | 75% (90d) | Does not open (82%) | n/a | [#374](https://github.com/GameNative/gamenative-compat/issues/374) |
| 244 | [ ] | Portal: First Slice (STEAM) | 18 | 23 | 78% (90d) | Does not open (92%) | n/a | [#354](https://github.com/GameNative/gamenative-compat/issues/354) |
| 245 | [ ] | Sid Meier's Pirates! (STEAM) | 18 | 23 | 78% (90d) | Does not open (92%) | n/a | [#293](https://github.com/GameNative/gamenative-compat/issues/293) |
| 246 | [ ] | Yakuza 0 (GOG) | 18 | 23 | 78% (90d) | Does not open (67%) | n/a | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 247 | [ ] | EVE Online (STEAM) | 18 | 22 | 82% (90d) | No graphics (50%) | 45% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 248 | [ ] | Genshin Impact (EPIC) | 18 | 22 | 82% (90d) | Does not open (85%) | n/a | [#326](https://github.com/GameNative/gamenative-compat/issues/326) |
| 249 | [ ] | Hitman 2: Silent Assassin (STEAM) | 18 | 22 | 82% (90d) | Does not open (85%) | 56% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 250 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 18 | 22 | 82% (90d) | Does not open (100%) | 21% | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 251 | [ ] | Bright Memory (STEAM) | 18 | 21 | 86% (90d) | No graphics (83%) | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 252 | [ ] | Crusader Kings III (STEAM) | 18 | 21 | 86% (90d) | No graphics (64%) | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 253 | [ ] | NBA 2K26 (STEAM) | 18 | 21 | 86% (90d) | Does not open (83%) | n/a | [#384](https://github.com/GameNative/gamenative-compat/issues/384) |
| 254 | [ ] | Assassin's Creed Rogue (STEAM) | 18 | 20 | 90% (90d) | Does not open (60%) | n/a | [#271](https://github.com/GameNative/gamenative-compat/issues/271) |
| 255 | [ ] | Battlefield™ 6 (STEAM) | 18 | 20 | 90% (90d) | Does not open (80%) | n/a | [#335](https://github.com/GameNative/gamenative-compat/issues/335) |
| 256 | [ ] | Mafia II: Definitive Edition (GOG) | 18 | 20 | 90% (90d) | No graphics (60%) | 31% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 257 | [ ] | STALZONE (STEAM) | 18 | 20 | 90% (90d) | Does not open (100%) | n/a | [#338](https://github.com/GameNative/gamenative-compat/issues/338) |
| 258 | [ ] | Carnal Instinct (STEAM) | 17 | 24 | 71% (90d) | Does not open (57%) | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 259 | [ ] | Darksiders Warmastered Edition (EPIC) | 17 | 23 | 74% (90d) | Does not open (83%) | 43% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 260 | [ ] | Grim Fandango Remastered (GOG) | 17 | 23 | 74% (90d) | No graphics (78%) | n/a | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 261 | [ ] | SlashZero Demo (STEAM) | 17 | 23 | 74% (90d) | Does not open (75%) | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 262 | [ ] | Spark the Electric Jester (STEAM) | 17 | 22 | 77% (90d) | Does not open (60%) | 56% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 263 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 17 | 22 | 77% (90d) | Does not open (87%) | 42% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 264 | [ ] | Bejeweled 2 Deluxe (STEAM) | 17 | 21 | 81% (90d) | Does not open (93%) | n/a | [#329](https://github.com/GameNative/gamenative-compat/issues/329) |
| 265 | [ ] | Dorfromantik (GOG) | 17 | 21 | 81% (90d) | Does not open (100%) | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 266 | [ ] | Tyrian 2000 (GOG) | 17 | 20 | 85% (90d) | Does not open (87%) | n/a | [#360](https://github.com/GameNative/gamenative-compat/issues/360) |
| 267 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 16 | 23 | 70% (90d) | No graphics (56%) | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 268 | [ ] | Make Way (EPIC) | 16 | 23 | 70% (90d) | Does not open (73%) | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 269 | [ ] | Hitman 3: Contracts (GOG) | 16 | 22 | 73% (90d) | Does not open (93%) | n/a | [#401](https://github.com/GameNative/gamenative-compat/issues/401) |
| 270 | [ ] | Re-Volt (STEAM) | 16 | 22 | 73% (90d) | Controller issues (71%) | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 271 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 16 | 21 | 76% (90d) | No graphics (67%) | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 272 | [ ] | Definitely Not Fried Chicken (EPIC) | 16 | 20 | 80% (90d) | Does not open (63%) | n/a | [#356](https://github.com/GameNative/gamenative-compat/issues/356) |
| 273 | [ ] | Once Human (STEAM) | 16 | 20 | 80% (90d) | Does not open (63%) | n/a | [#395](https://github.com/GameNative/gamenative-compat/issues/395) |
| 274 | [ ] | The Last Stand: Aftermath (STEAM) | 16 | 20 | 80% (90d) | No graphics (50%) | n/a | [#324](https://github.com/GameNative/gamenative-compat/issues/324) |
| 275 | [ ] | shapez (STEAM) | 16 | 20 | 80% (90d) | No graphics (67%) | n/a | [#332](https://github.com/GameNative/gamenative-compat/issues/332) |
| 276 | [ ] | Fallout Classic (GOG) | 15 | 21 | 71% (90d) | Does not open (71%) | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 277 | [ ] | Jurassic World Evolution 2 (STEAM) | 15 | 21 | 71% (90d) | Does not open (45%) | n/a | [#448](https://github.com/GameNative/gamenative-compat/issues/448) |
| 278 | [ ] | Smushi Come Home (GOG) | 15 | 21 | 71% (90d) | Does not open (57%) | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 279 | [ ] | Space Rangers HD: A War Apart (STEAM) | 15 | 21 | 71% (90d) | Does not open (64%) | 50% | [#472](https://github.com/GameNative/gamenative-compat/issues/472) |
| 280 | [ ] | Sword Art Online: Hollow Realization Deluxe Edition (STEAM) | 14 | 20 | 70% (90d) | Controller issues (92%) | n/a | [#470](https://github.com/GameNative/gamenative-compat/issues/470) |

## Probably does not work (95)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [x] 2026-10-18 | Spelunky 2 (STEAM) | 203 | 219 | 50% (14d) | Does not open (73%) | 44% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 2 | [ ] | Garry's Mod (STEAM) | 200 | 328 | 65% (1.3.0) | Does not open (79%) | 56% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 3 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 159 | 246 | 65% (90d) | Does not open (77%) | n/a |  |
| 4 | [ ] | Prototype (STEAM) | 155 | 218 | 50% (1.3.0) | Does not open (75%) | 42% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 5 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 143 | 180 | 52% (1.3.0) | Does not open (93%) | 41% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 6 | [ ] | Metro 2033 Redux (STEAM) | 142 | 347 | 61% (1.3.0) | Does not open (69%) | 52% |  |
| 7 | [ ] | Geometry Dash (STEAM) | 129 | 411 | 66% (1.3.0) | Does not open (68%) | 41% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 8 | [ ] | Euro Truck Simulator 2 (STEAM) | 119 | 213 | 52% (1.3.0) | Does not open (66%) | 58% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 9 | [ ] | VRChat (STEAM) | 92 | 138 | 65% (14d) | Does not open (64%) | 39% |  |
| 10 | [ ] | MECCHA CHAMELEON (STEAM) | 77 | 111 | 69% (90d) | Does not open (65%) | 58% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 11 | [ ] | Hollow Knight: Silksong (GOG) | 74 | 113 | 65% (90d) | Does not open (69%) | 50% |  |
| 12 | [ ] | Firewatch (STEAM) | 68 | 116 | 59% (90d) | Does not open (89%) | 58% |  |
| 13 | [ ] | Gorilla Tag (STEAM) | 66 | 111 | 59% (90d) | Does not open (76%) | 24% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 14 | [ ] | Stardew Valley (GOG) | 65 | 115 | 57% (90d) | Controller issues (45%) | 53% |  |
| 15 | [ ] | Oxygen Not Included (STEAM) | 56 | 90 | 62% (90d) | Does not open (70%) | 46% |  |
| 16 | [ ] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 54 | 91 | 59% (90d) | Does not open (63%) | 59% |  |
| 17 | [ ] | Breathedge (STEAM) | 50 | 74 | 68% (90d) | Does not open (63%) | 40% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 18 | [ ] | Frostpunk (STEAM) | 48 | 76 | 63% (90d) | No graphics (78%) | 55% |  |
| 19 | [ ] | VALORANT (EPIC) | 47 | 74 | 64% (90d) | Does not open (84%) | 20% |  |
| 20 | [ ] | Skullgirls 2nd Encore (STEAM) | 45 | 77 | 58% (90d) | Does not open (93%) | 58% |  |
| 21 | [ ] | Plague Inc: Evolved (STEAM) | 45 | 69 | 65% (90d) | Does not open (65%) | 55% |  |
| 22 | [ ] | Fallout (GOG) | 43 | 64 | 67% (90d) | Does not open (71%) | 56% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 23 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 41 | 71 | 58% (90d) | Does not open (74%) | 49% |  |
| 24 | [ ] | Age of Empires II (2013) (STEAM) | 40 | 69 | 58% (90d) | Does not open (48%) | 54% |  |
| 25 | [ ] | Grim Dawn (GOG) | 38 | 63 | 60% (90d) | Does not open (65%) | 50% | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 26 | [ ] | XCOM 2 (STEAM) | 36 | 55 | 65% (90d) | Does not open (57%) | n/a |  |
| 27 | [ ] | Deponia (STEAM) | 34 | 63 | 54% (90d) | Does not open (50%) | 57% |  |
| 28 | [ ] | Hero Siege (STEAM) | 33 | 56 | 59% (90d) | Graphics glitches (52%) | 57% |  |
| 29 | [ ] | Sol Cesto (STEAM) | 33 | 52 | 63% (90d) | Does not open (70%) | 53% |  |
| 30 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 32 | 57 | 56% (90d) | Does not open (95%) | 44% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 31 | [ ] | Soul's Remnant (STEAM) | 27 | 49 | 55% (90d) | Does not open (55%) | n/a |  |
| 32 | [ ] | Lucid Blocks (STEAM) | 27 | 45 | 60% (90d) | Does not open (83%) | n/a |  |
| 33 | [ ] | Opus Magnum (STEAM) | 25 | 39 | 64% (90d) | Does not open (72%) | n/a |  |
| 34 | [ ] | Strider (STEAM) | 25 | 38 | 66% (90d) | Does not open (100%) | 31% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 35 | [ ] | Goat Simulator (STEAM) | 24 | 43 | 56% (90d) | Does not open (58%) | 54% |  |
| 36 | [ ] | Crazy Taxi (STEAM) | 24 | 40 | 60% (90d) | Does not open (61%) | 44% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 37 | [ ] | Invisible, Inc. (STEAM) | 23 | 40 | 58% (90d) | Does not open (67%) | 59% |  |
| 38 | [ ] | Styx: Master of Shadows (EPIC) | 22 | 42 | 52% (90d) | Does not open (55%) | 27% |  |
| 39 | [ ] | Owlboy (STEAM) | 22 | 41 | 54% (90d) | Does not open (81%) | 50% |  |
| 40 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 22 | 33 | 67% (90d) | Does not open (80%) | n/a |  |
| 41 | [ ] | GOD EATER RESURRECTION (STEAM) | 21 | 32 | 66% (90d) | Does not open (53%) | 55% |  |
| 42 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 19 | 36 | 53% (90d) | Does not open (56%) | 44% |  |
| 43 | [ ] | No More Heroes (STEAM) | 19 | 36 | 53% (90d) | No graphics (67%) | n/a |  |
| 44 | [ ] | Another World: 20th Anniversary Edition (GOG) | 19 | 28 | 68% (90d) | Does not open (69%) | n/a |  |
| 45 | [ ] | Turnip Boy Robs a Bank (EPIC) | 19 | 28 | 68% (90d) | Does not open (65%) | 43% | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 46 | [ ] | Lost Castle 2 (STEAM) | 18 | 33 | 55% (90d) | Does not open (64%) | n/a |  |
| 47 | [ ] | Legend of Grimrock 2 (STEAM) | 18 | 26 | 69% (90d) | Does not open (80%) | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 48 | [ ] | Mini Metro (STEAM) | 17 | 34 | 50% (90d) | Does not open (38%) | 48% |  |
| 49 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 17 | 33 | 52% (90d) | Does not open (88%) | 30% |  |
| 50 | [ ] | Guacamelee! Gold Edition (STEAM) | 17 | 28 | 61% (90d) | Does not open (93%) | n/a | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 51 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 17 | 27 | 63% (90d) | Does not open (80%) | n/a |  |
| 52 | [ ] | Assassin's Creed Odyssey (STEAM) | 16 | 24 | 67% (90d) | Does not open (75%) | n/a | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 53 | [ ] | Evoland (STEAM) | 15 | 29 | 52% (90d) | Controller issues (71%) | n/a |  |
| 54 | [ ] | Blaster Master Zero (STEAM) | 15 | 27 | 56% (90d) | Does not open (67%) | 36% |  |
| 55 | [ ] | Odallus: The Dark Call (STEAM) | 15 | 27 | 56% (90d) | No graphics (57%) | n/a | [#337](https://github.com/GameNative/gamenative-compat/issues/337) |
| 56 | [ ] | Spilled! (STEAM) | 15 | 27 | 56% (90d) | Graphics glitches (67%) | n/a |  |
| 57 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 15 | 26 | 58% (90d) | Does not open (85%) | 49% |  |
| 58 | [ ] | War of Dots (STEAM) | 15 | 25 | 60% (90d) | Does not open (71%) | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 59 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 15 | 22 | 68% (90d) | Does not open (70%) | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 60 | [ ] | Aperture Desk Job (STEAM) | 14 | 28 | 50% (90d) | Does not open (67%) | n/a |  |
| 61 | [ ] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 14 | 28 | 50% (90d) | Does not open (100%) | 50% |  |
| 62 | [ ] | Far Cry® (GOG) | 14 | 27 | 52% (90d) | Does not open (31%) | n/a |  |
| 63 | [ ] | Alan Wake's American Nightmare (EPIC) | 14 | 26 | 54% (90d) | Does not open (92%) | 47% |  |
| 64 | [ ] | Katana ZERO (GOG) | 14 | 25 | 56% (90d) | Does not open (85%) | 29% |  |
| 65 | [ ] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 14 | 24 | 58% (90d) | Does not open (93%) | 15% |  |
| 66 | [ ] | Warhammer 40,000: Boltgun (GOG) | 14 | 24 | 58% (90d) | Does not open (92%) | 33% |  |
| 67 | [ ] | Ys: Memories of Celceta (STEAM) | 14 | 23 | 61% (90d) | Does not open (40%) | 27% |  |
| 68 | [ ] | Blood Omen: Legacy of Kain (GOG) | 14 | 22 | 64% (90d) | Does not open (69%) | 39% |  |
| 69 | [ ] | Quake III Arena (STEAM) | 13 | 26 | 50% (90d) | Does not open (70%) | 9% |  |
| 70 | [ ] | A Plague Tale: Innocence (GOG) | 13 | 24 | 54% (90d) | Does not open (92%) | 50% |  |
| 71 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 13 | 24 | 54% (90d) | Does not open (75%) | 0% |  |
| 72 | [ ] | UNDEFEATED (STEAM) | 13 | 24 | 54% (90d) | Does not open (80%) | n/a |  |
| 73 | [ ] | The Stanley Parable (STEAM) | 13 | 23 | 57% (90d) | Does not open (89%) | 43% |  |
| 74 | [ ] | Evenicle (STEAM) | 13 | 22 | 59% (90d) | Graphics glitches (77%) | n/a |  |
| 75 | [ ] | Foretales (EPIC) | 13 | 21 | 62% (90d) | Does not open (55%) | n/a | [#451](https://github.com/GameNative/gamenative-compat/issues/451) |
| 76 | [ ] | PAYDAY: The Heist (STEAM) | 13 | 21 | 62% (90d) | Does not open (67%) | n/a |  |
| 77 | [ ] | Trials Survivors (STEAM) | 13 | 21 | 62% (90d) | Does not open (67%) | n/a |  |
| 78 | [ ] | Buck Up And Drive! (STEAM) | 13 | 20 | 65% (90d) | Does not open (67%) | n/a |  |
| 79 | [ ] | Look Outside (GOG) | 12 | 24 | 50% (90d) | Does not open (100%) | n/a |  |
| 80 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 12 | 23 | 52% (90d) | Does not open (73%) | n/a |  |
| 81 | [ ] | Shift At Midnight (STEAM) | 12 | 21 | 57% (90d) | Does not open (80%) | n/a |  |
| 82 | [ ] | The Excavation of Hob's Barrow (STEAM) | 12 | 21 | 57% (90d) | Controller issues (82%) | n/a |  |
| 83 | [ ] | Breathedge (EPIC) | 12 | 20 | 60% (90d) | Does not open (100%) | 47% |  |
| 84 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (90d) | Does not open (82%) | n/a |  |
| 85 | [ ] | Dex (GOG) | 12 | 20 | 60% (90d) | Does not open (80%) | n/a |  |
| 86 | [ ] | Drop Duchy (EPIC) | 12 | 20 | 60% (90d) | Does not open (100%) | n/a |  |
| 87 | [ ] | Human Resource Machine (EPIC) | 12 | 20 | 60% (90d) | No graphics (67%) | n/a |  |
| 88 | [ ] | Songs of Conquest (EPIC) | 12 | 20 | 60% (90d) | Does not open (83%) | n/a |  |
| 89 | [ ] | XIII (GOG) | 12 | 20 | 60% (90d) | Does not open (70%) | n/a |  |
| 90 | [ ] | Crying Suns (EPIC) | 11 | 22 | 50% (90d) | No graphics (57%) | n/a |  |
| 91 | [ ] | FATE (STEAM) | 11 | 20 | 55% (90d) | No graphics (50%) | n/a |  |
| 92 | [ ] | Grounded (STEAM) | 11 | 20 | 55% (90d) | No graphics (50%) | n/a |  |
| 93 | [ ] | Asterigos: Curse of the Stars (STEAM) | 10 | 20 | 50% (90d) | Does not open (43%) | n/a |  |
| 94 | [ ] | DYNASTY WARRIORS: ORIGINS (STEAM) | 10 | 20 | 50% (90d) | Does not open (60%) | n/a |  |
| 95 | [ ] | Thief™ 3: Deadly Shadows (GOG) | 10 | 20 | 50% (90d) | Does not open (70%) | n/a |  |

## Works, but the first launch usually fails (363)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 1367 | 1726 | 75% (1.3.0) | Does not open (83%) | 77% |  |
| 2 | [ ] | Grim Dawn (STEAM) | 595 | 644 | 68% (1.3.0) | Does not open (75%) | 65% |  |
| 3 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 579 | 737 | 77% (1.3.0) | Does not open (64%) | 91% |  |
| 4 | [ ] | Terraria (STEAM) | 491 | 769 | 59% (1.3.0) | No graphics (51%) | 75% |  |
| 5 | [ ] | KINGDOM HEARTS -HD 1.5+2.5 ReMIX- (STEAM) | 465 | 937 | 55% (1.3.0) | Does not open (79%) | 94% |  |
| 6 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 377 | 560 | 69% (1.3.0) | Does not open (55%) | 86% |  |
| 7 | [ ] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 269 | 310 | 87% (90d) | Does not open (85%) | 65% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 8 | [ ] | Cyberpunk 2077 (STEAM) | 247 | 425 | 54% (1.3.0) | Does not open (67%) | 76% |  |
| 9 | [ ] | Welcome to Elderfield (STEAM) | 231 | 276 | 57% (1.3.0) | Does not open (72%) | 80% |  |
| 10 | [ ] | BeamNG.drive (STEAM) | 228 | 279 | 86% (1.3.0) | Does not open (84%) | 92% |  |
| 11 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 224 | 315 | 71% (90d) | Does not open (61%) | 87% |  |
| 12 | [ ] | Grand Theft Auto V Legacy (STEAM) | 215 | 270 | 70% (1.3.0) | Does not open (87%) | 79% |  |
| 13 | [ ] | OMORI (STEAM) | 210 | 253 | 83% (90d) | Does not open (64%) | 77% |  |
| 14 | [ ] | Devil May Cry HD Collection (STEAM) | 200 | 280 | 80% (1.3.0) | Does not open (87%) | 74% |  |
| 15 | [ ] | ELDEN RING (STEAM) | 198 | 294 | 69% (1.3.0) | Does not open (85%) | 69% |  |
| 16 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 192 | 361 | 61% (1.3.0) | Does not open (58%) | 82% |  |
| 17 | [ ] | DREDGE (EPIC) | 176 | 225 | 64% (1.3.0) | Does not open (69%) | 88% |  |
| 18 | [ ] | Resident Evil 2 (STEAM) | 155 | 313 | 54% (1.3.0) | Does not open (75%) | 81% |  |
| 19 | [ ] | Rocket League® (EPIC) | 151 | 252 | 50% (1.3.0) | Does not open (74%) | 76% |  |
| 20 | [ ] | Noita (STEAM) | 148 | 223 | 55% (1.3.0) | Does not open (54%) | 78% |  |
| 21 | [ ] | Team Fortress 2 (STEAM) | 141 | 231 | 68% (1.3.0) | Does not open (68%) | 80% |  |
| 22 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 140 | 161 | 87% (90d) | Does not open (85%) | 80% |  |
| 23 | [ ] | Far Cry® 3 (STEAM) | 140 | 159 | 88% (90d) | Does not open (83%) | 64% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 24 | [ ] | Borderlands 2 (EPIC) | 139 | 163 | 81% (1.3.0) | Does not open (83%) | 64% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 25 | [ ] | Look Outside (STEAM) | 133 | 301 | 53% (1.3.0) | Controller issues (61%) | 91% |  |
| 26 | [ ] | Castlevania Advance Collection (STEAM) | 132 | 202 | 70% (1.3.0) | Controller issues (94%) | 97% |  |
| 27 | [ ] | Minecraft Dungeons II (STEAM) | 122 | 139 | 88% (90d) | Does not open (83%) | 65% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 28 | [ ] | Cave Story+ (STEAM) | 121 | 133 | 91% (90d) | Does not open (65%) | 95% |  |
| 29 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 120 | 148 | 70% (1.3.0) | Does not open (71%) | 63% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 30 | [ ] | Castlevania Dominus Collection (STEAM) | 119 | 176 | 72% (1.3.0) | Controller issues (92%) | 98% |  |
| 31 | [ ] | Devil May Cry 5 (STEAM) | 118 | 189 | 65% (1.3.0) | Does not open (80%) | 67% |  |
| 32 | [ ] | Fallout: New Vegas (EPIC) | 118 | 144 | 82% (90d) | Does not open (59%) | 91% |  |
| 33 | [ ] | Touhou Koumakyou: New Classic - the Embodiment of Scarlet Devil (STEAM) | 117 | 178 | 66% (90d) | Does not open (78%) | 79% |  |
| 34 | [ ] | Caravan SandWitch (EPIC) | 116 | 179 | 50% (14d) | Does not open (92%) | 82% |  |
| 35 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 114 | 150 | 76% (90d) | Does not open (86%) | 81% |  |
| 36 | [ ] | The Witcher: Enhanced Edition (STEAM) | 114 | 132 | 86% (90d) | Does not open (60%) | 65% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 37 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 110 | 154 | 80% (1.3.0) | Does not open (74%) | 65% |  |
| 38 | [ ] | Moonstone Island (STEAM) | 105 | 138 | 76% (90d) | Controller issues (57%) | 91% |  |
| 39 | [ ] | Aniimo (STEAM) | 103 | 141 | 73% (90d) | Does not open (77%) | 92% |  |
| 40 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 96 | 129 | 74% (90d) | Controller issues (86%) | 100% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 41 | [ ] | Happy Wheels (STEAM) | 93 | 113 | 82% (90d) | No graphics (53%) | 79% |  |
| 42 | [ ] | BioShock Remastered (EPIC) | 92 | 165 | 56% (90d) | Does not open (56%) | 85% |  |
| 43 | [ ] | Fallout: New Vegas PCR (STEAM) | 92 | 125 | 74% (90d) | Does not open (89%) | 74% |  |
| 44 | [ ] | Cry of Fear (STEAM) | 91 | 176 | 73% (1.3.0) | Does not open (53%) | 91% |  |
| 45 | [ ] | Sovereign Tower (STEAM) | 90 | 143 | 63% (90d) | Does not open (82%) | 87% |  |
| 46 | [ ] | Vital Shell (STEAM) | 88 | 130 | 68% (90d) | Does not open (53%) | 84% |  |
| 47 | [ ] | STEINS;GATE (STEAM) | 88 | 120 | 73% (90d) | Does not open (90%) | 87% |  |
| 48 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 87 | 130 | 50% (1.3.0) | Does not open (79%) | 74% |  |
| 49 | [ ] | Hogwarts Legacy (STEAM) | 81 | 138 | 54% (1.3.0) | Does not open (60%) | 66% |  |
| 50 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 81 | 84 | 96% (90d) | Does not open (92%) | 60% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 51 | [ ] | Need for Speed: Hot Pursuit (STEAM) | 78 | 107 | 73% (90d) | Does not open (75%) | 74% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 52 | [ ] | The Sims™ 4 (STEAM) | 78 | 96 | 81% (90d) | Does not open (89%) | 70% |  |
| 53 | [ ] | Detroit: Become Human (STEAM) | 78 | 81 | 96% (90d) | Does not open (72%) | 64% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 54 | [ ] | Resident Evil 4 (2005) (STEAM) | 77 | 150 | 51% (90d) | Does not open (75%) | 73% |  |
| 55 | [ ] | Mega Man Zero/ZX Legacy Collection (STEAM) | 76 | 103 | 74% (90d) | Does not open (87%) | 84% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 56 | [ ] | Alabaster Dawn (STEAM) | 75 | 130 | 58% (90d) | Controller issues (49%) | 93% |  |
| 57 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 74 | 123 | 60% (90d) | Controller issues (59%) | 93% |  |
| 58 | [ ] | Fallout 3: Game of the Year Edition (GOG) | 72 | 165 | 52% (1.3.0) | Does not open (59%) | 71% |  |
| 59 | [ ] | Sid Meier's Civilization VI (STEAM) | 72 | 127 | 54% (1.3.0) | Does not open (70%) | 92% |  |
| 60 | [ ] | Darksiders (STEAM) | 72 | 87 | 83% (90d) | Does not open (69%) | 87% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 61 | [ ] | Ballionaire (STEAM) | 71 | 108 | 66% (90d) | Does not open (77%) | 97% |  |
| 62 | [ ] | A Plague Tale: Innocence (STEAM) | 71 | 74 | 96% (90d) | Does not open (85%) | 75% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 63 | [ ] | Fable - The Lost Chapters (STEAM) | 70 | 109 | 52% (1.3.0) | Graphics glitches (49%) | 77% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 64 | [ ] | Dota 2 (STEAM) | 70 | 107 | 57% (1.3.0) | Does not open (78%) | 71% |  |
| 65 | [ ] | Antivirus Survivors 2003 Professional (STEAM) | 70 | 103 | 68% (90d) | Does not open (61%) | 92% |  |
| 66 | [ ] | Gunfire Reborn (STEAM) | 70 | 77 | 91% (90d) | Does not open (82%) | 93% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 67 | [ ] | Fallout (STEAM) | 69 | 107 | 64% (90d) | Does not open (69%) | 71% |  |
| 68 | [ ] | Call of Juarez Gunslinger (STEAM) | 69 | 84 | 82% (90d) | Does not open (91%) | 72% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 69 | [ ] | POSTAL 2 (STEAM) | 68 | 119 | 57% (90d) | Does not open (65%) | 67% |  |
| 70 | [ ] | American Truck Simulator (STEAM) | 68 | 108 | 81% (1.3.0) | Does not open (74%) | 74% |  |
| 71 | [ ] | Dungeons & Degenerate Gamblers (STEAM) | 68 | 92 | 74% (90d) | Does not open (90%) | 99% |  |
| 72 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 68 | 90 | 76% (90d) | Does not open (48%) | 65% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 73 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 68 | 81 | 95% (1.3.0) | Does not open (91%) | 97% |  |
| 74 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 67 | 123 | 54% (90d) | Does not open (64%) | 65% |  |
| 75 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 66 | 104 | 63% (90d) | Does not open (75%) | 69% |  |
| 76 | [ ] | Borderlands: The Pre-Sequel (STEAM) | 66 | 92 | 72% (90d) | Does not open (78%) | 67% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 77 | [ ] | Disgaea 5 Complete (STEAM) | 66 | 80 | 83% (90d) | Does not open (79%) | 97% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 78 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 65 | 87 | 75% (90d) | Does not open (51%) | 92% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 79 | [ ] | MIO: Memories in Orbit (STEAM) | 64 | 123 | 64% (1.3.0) | Graphics glitches (52%) | 97% |  |
| 80 | [ ] | Poppy Playtime (STEAM) | 64 | 109 | 59% (90d) | Does not open (69%) | 78% |  |
| 81 | [ ] | Big Walk (STEAM) | 63 | 96 | 66% (90d) | Does not open (68%) | 82% |  |
| 82 | [ ] | The Binding of Isaac (STEAM) | 62 | 142 | 62% (1.3.0) | Controller issues (91%) | 93% |  |
| 83 | [ ] | Sonic Lost World (STEAM) | 62 | 103 | 60% (90d) | No graphics (59%) | 88% |  |
| 84 | [ ] | Cyberpunk 2077 (GOG) | 62 | 76 | 82% (90d) | Does not open (80%) | 75% |  |
| 85 | [ ] | Ace Attorney Investigations Collection (STEAM) | 61 | 92 | 66% (90d) | Does not open (97%) | 90% |  |
| 86 | [ ] | eFootball™ (STEAM) | 60 | 91 | 66% (90d) | Does not open (57%) | 75% |  |
| 87 | [ ] | Sonic Generations (STEAM) | 60 | 70 | 86% (90d) | Does not open (73%) | 66% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 88 | [ ] | Starbound (STEAM) | 59 | 85 | 65% (1.3.0) | Does not open (69%) | 72% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 89 | [ ] | Red Dead Redemption 2 (STEAM) | 59 | 78 | 63% (1.3.0) | Does not open (98%) | 84% |  |
| 90 | [ ] | Borderlands 3 (STEAM) | 59 | 76 | 78% (90d) | Does not open (91%) | 95% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 91 | [ ] | Sonic Adventure DX (STEAM) | 58 | 94 | 62% (90d) | Does not open (86%) | 70% |  |
| 92 | [ ] | Call of Duty: World at War (STEAM) | 58 | 81 | 72% (90d) | Does not open (43%) | 62% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 93 | [ ] | Dead by Daylight (STEAM) | 58 | 63 | 92% (90d) | Does not open (83%) | 81% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 94 | [ ] | TBH: Task Bar Hero (STEAM) | 57 | 86 | 66% (90d) | Does not open (70%) | 94% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 95 | [ ] | Prey (STEAM) | 56 | 94 | 60% (90d) | Does not open (63%) | 88% |  |
| 96 | [ ] | Devil May Cry 4 Special Edition (STEAM) | 55 | 94 | 59% (90d) | Does not open (86%) | 79% |  |
| 97 | [ ] | The Secret of Monkey Island: Special Edition (STEAM) | 55 | 88 | 63% (90d) | Does not open (90%) | 68% |  |
| 98 | [ ] | Mini Motorways (STEAM) | 54 | 96 | 56% (90d) | Does not open (75%) | 62% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 99 | [ ] | A Plague Tale: Innocence (EPIC) | 54 | 91 | 59% (90d) | Does not open (71%) | 88% |  |
| 100 | [ ] | The Bazaar (STEAM) | 54 | 86 | 63% (90d) | Does not open (73%) | 85% |  |
| 101 | [ ] | Path of Exile (STEAM) | 54 | 63 | 86% (90d) | Does not open (91%) | 85% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 102 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 54 | 62 | 87% (90d) | Does not open (77%) | 73% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 103 | [ ] | MudRunner (STEAM) | 52 | 102 | 51% (90d) | Does not open (75%) | 64% |  |
| 104 | [ ] | Until Then (STEAM) | 52 | 93 | 56% (90d) | Does not open (73%) | 97% |  |
| 105 | [ ] | Resident Evil 6 (STEAM) | 51 | 127 | 76% (1.3.0) | Does not open (55%) | 91% |  |
| 106 | [ ] | 7 Days to Die (STEAM) | 51 | 108 | 61% (1.3.0) | Does not open (74%) | 73% |  |
| 107 | [ ] | Slay the Princess — The Pristine Cut (STEAM) | 51 | 92 | 55% (90d) | No graphics (60%) | 73% |  |
| 108 | [ ] | Sheepy: A Short Adventure (STEAM) | 51 | 61 | 84% (90d) | Does not open (54%) | 82% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 109 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 51 | 55 | 93% (90d) | Does not open (85%) | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 110 | [ ] | Street Fighter™ 6 (STEAM) | 50 | 75 | 67% (90d) | Does not open (88%) | 80% |  |
| 111 | [ ] | Guildrun Demo (STEAM) | 50 | 72 | 69% (90d) | No graphics (65%) | 72% |  |
| 112 | [ ] | Dead Space (STEAM) | 50 | 63 | 79% (90d) | Does not open (54%) | 72% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 113 | [ ] | Sleeping Dogs™ (STEAM) | 50 | 57 | 88% (90d) | Does not open (83%) | 80% | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 114 | [ ] | MapleStory (STEAM) | 50 | 52 | 91% (14d) | Does not open (78%) | 76% |  |
| 115 | [ ] | Okami HD (STEAM) | 49 | 93 | 53% (90d) | Controller issues (60%) | 85% |  |
| 116 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 49 | 75 | 76% (1.3.0) | Does not open (59%) | 65% |  |
| 117 | [ ] | Rivals of Aether II (STEAM) | 49 | 74 | 66% (90d) | Does not open (56%) | 73% |  |
| 118 | [ ] | FINAL FANTASY VII (2013) (STEAM) | 48 | 69 | 70% (90d) | Does not open (85%) | 79% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 119 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 48 | 69 | 70% (90d) | Does not open (83%) | 79% |  |
| 120 | [ ] | Last Epoch (STEAM) | 48 | 67 | 78% (1.3.0) | Does not open (77%) | 100% |  |
| 121 | [ ] | Digimon World: Next Order (STEAM) | 47 | 87 | 54% (90d) | Controller issues (80%) | 94% |  |
| 122 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 75 | 63% (90d) | Controller issues (57%) | 95% |  |
| 123 | [ ] | Crypt of the NecroDancer (STEAM) | 46 | 152 | 50% (1.3.0) | Does not open (53%) | 86% |  |
| 124 | [ ] | Darkest Dungeon® (EPIC) | 46 | 83 | 56% (1.3.0) | Does not open (63%) | 63% |  |
| 125 | [ ] | Tomb Raider: Anniversary (STEAM) | 46 | 66 | 70% (90d) | Does not open (95%) | 71% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 126 | [ ] | Abiotic Factor (STEAM) | 45 | 79 | 57% (90d) | Does not open (74%) | 69% |  |
| 127 | [ ] | Life is Strange™ (STEAM) | 44 | 86 | 51% (90d) | Does not open (74%) | 81% |  |
| 128 | [ ] | Teardown (STEAM) | 44 | 84 | 52% (90d) | Does not open (56%) | 77% |  |
| 129 | [ ] | Grand Theft Auto V (EPIC) | 44 | 50 | 88% (90d) | Does not open (88%) | 83% |  |
| 130 | [ ] | Salt and Sanctuary (STEAM) | 43 | 81 | 53% (90d) | Does not open (76%) | 81% |  |
| 131 | [ ] | Moonlighter (EPIC) | 43 | 47 | 91% (90d) | No graphics (79%) | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 132 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 42 | 77 | 55% (90d) | Controller issues (55%) | 87% |  |
| 133 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 42 | 69 | 61% (90d) | Does not open (64%) | 79% |  |
| 134 | [ ] | Resident Evil 7 Biohazard (STEAM) | 42 | 67 | 63% (90d) | Does not open (76%) | 83% |  |
| 135 | [ ] | Amnesia: The Dark Descent (STEAM) | 41 | 76 | 54% (90d) | Does not open (85%) | 77% |  |
| 136 | [ ] | Sonic Origins (STEAM) | 41 | 71 | 58% (90d) | Does not open (70%) | 85% |  |
| 137 | [ ] | Deadlock (STEAM) | 41 | 65 | 63% (90d) | Does not open (50%) | 93% |  |
| 138 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 41 | 62 | 66% (90d) | Does not open (75%) | 70% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 139 | [ ] | Capcom Arcade Stadium (STEAM) | 41 | 51 | 80% (90d) | Does not open (84%) | 76% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 140 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 40 | 75 | 53% (90d) | No graphics (81%) | 94% |  |
| 141 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 40 | 75 | 53% (90d) | Controller issues (44%) | 90% |  |
| 142 | [ ] | Forza Horizon 4 (STEAM) | 40 | 56 | 71% (90d) | Does not open (50%) | 87% |  |
| 143 | [ ] | Aggelos (STEAM) | 40 | 54 | 74% (90d) | No graphics (79%) | 94% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 144 | [ ] | Tales of ARISE (STEAM) | 39 | 67 | 58% (90d) | Controller issues (74%) | 93% |  |
| 145 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 39 | 41 | 95% (90d) | Does not open (61%) | 82% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 146 | [ ] | Monster Hunter Wilds (STEAM) | 39 | 40 | 98% (90d) | Does not open (63%) | 74% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 147 | [ ] | CrossCode (GOG) | 38 | 42 | 90% (90d) | Does not open (76%) | 71% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 148 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 67 | 55% (90d) | Does not open (68%) | 86% |  |
| 149 | [ ] | Romestead (STEAM) | 37 | 48 | 77% (90d) | Does not open (67%) | 77% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 150 | [ ] | SurrounDead (STEAM) | 36 | 68 | 53% (90d) | Controller issues (59%) | 95% |  |
| 151 | [ ] | Hearts of Iron IV (STEAM) | 36 | 62 | 58% (90d) | Does not open (74%) | 62% |  |
| 152 | [ ] | Rocket League (STEAM) | 36 | 55 | 65% (90d) | Does not open (72%) | 69% |  |
| 153 | [ ] | Capcom Fighting Collection 2 (STEAM) | 36 | 51 | 71% (90d) | Does not open (80%) | 87% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 154 | [ ] | Street Fighter 30th Anniversary Collection (STEAM) | 35 | 67 | 52% (90d) | Does not open (100%) | 66% |  |
| 155 | [ ] | Earthion (STEAM) | 35 | 56 | 63% (90d) | Controller issues (88%) | 100% |  |
| 156 | [ ] | Battle Brothers (STEAM) | 35 | 50 | 70% (90d) | Does not open (77%) | 64% |  |
| 157 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 35 | 49 | 71% (90d) | Controller issues (88%) | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 158 | [ ] | SnowRunner (STEAM) | 35 | 48 | 73% (90d) | Does not open (96%) | 83% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 159 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 35 | 41 | 85% (90d) | Does not open (65%) | 74% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 160 | [ ] | Fallout 3 (STEAM) | 34 | 67 | 51% (90d) | Does not open (54%) | 89% |  |
| 161 | [ ] | Ultimate Custom Night (STEAM) | 34 | 46 | 74% (90d) | No graphics (66%) | 77% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 162 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 34 | 41 | 83% (90d) | Does not open (70%) | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 163 | [ ] | Max Payne (STEAM) | 33 | 59 | 56% (90d) | No graphics (45%) | 95% |  |
| 164 | [ ] | Resident Evil Village (STEAM) | 33 | 55 | 60% (90d) | Does not open (70%) | 87% |  |
| 165 | [ ] | Secrets of Grindea (STEAM) | 33 | 51 | 65% (90d) | Does not open (54%) | 82% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 166 | [ ] | Counter-Strike:Global Offensive (STEAM) | 33 | 50 | 66% (90d) | Does not open (79%) | 74% |  |
| 167 | [ ] | Supermarket Together (STEAM) | 33 | 48 | 69% (90d) | Does not open (72%) | 79% |  |
| 168 | [ ] | Russian Fishing 4 (STEAM) | 33 | 38 | 87% (90d) | Does not open (68%) | 67% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 169 | [ ] | Hotline Miami (GOG) | 33 | 36 | 92% (90d) | Does not open (94%) | 64% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 170 | [ ] | COCOON (STEAM) | 32 | 62 | 52% (90d) | Directx error (50%) | 89% |  |
| 171 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 32 | 61 | 52% (90d) | Does not open (69%) | 88% |  |
| 172 | [ ] | Library Of Ruina (STEAM) | 32 | 61 | 52% (90d) | Does not open (68%) | 85% |  |
| 173 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 32 | 53 | 60% (90d) | Controller issues (63%) | 65% |  |
| 174 | [ ] | Monster Boy And The Cursed Kingdom (STEAM) | 32 | 52 | 62% (90d) | Controller issues (83%) | 77% |  |
| 175 | [ ] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 32 | 50 | 64% (90d) | Does not open (43%) | 76% |  |
| 176 | [ ] | Nioh: Complete Edition (STEAM) | 32 | 43 | 74% (90d) | Does not open (56%) | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 177 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 42 | 76% (90d) | Controller issues (62%) | 89% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 178 | [ ] | Path of Exile 2 (STEAM) | 32 | 37 | 86% (90d) | Does not open (96%) | 86% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 179 | [ ] | Need for Speed™ (STEAM) | 32 | 36 | 89% (90d) | Does not open (70%) | 63% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 180 | [ ] | Red Dead Redemption (STEAM) | 32 | 36 | 89% (90d) | Does not open (95%) | 89% |  |
| 181 | [ ] | Stumble Guys (STEAM) | 31 | 62 | 50% (90d) | Does not open (68%) | 82% |  |
| 182 | [ ] | LEGO® Harry Potter™ Collection (STEAM) | 31 | 57 | 54% (90d) | Does not open (85%) | 85% |  |
| 183 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 31 | 55 | 56% (90d) | Does not open (46%) | 65% |  |
| 184 | [ ] | Tower and Sword of Succubus (STEAM) | 31 | 46 | 67% (90d) | No graphics (81%) | 100% |  |
| 185 | [ ] | Super Animal Royale (STEAM) | 31 | 40 | 78% (90d) | Does not open (63%) | 77% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 186 | [ ] | Grand Theft Auto III (STEAM) | 31 | 39 | 79% (90d) | Does not open (52%) | 89% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 187 | [ ] | Cave Story+ (EPIC) | 29 | 55 | 53% (90d) | Does not open (48%) | 85% |  |
| 188 | [ ] | Aethermancer (STEAM) | 29 | 50 | 58% (90d) | Does not open (78%) | 78% |  |
| 189 | [ ] | Yakuza: Like a Dragon (STEAM) | 29 | 44 | 66% (90d) | Does not open (68%) | 75% |  |
| 190 | [ ] | Dead Rising 2 (STEAM) | 29 | 41 | 85% (14d) | Does not open (88%) | 68% |  |
| 191 | [ ] | Moonlight Peaks (STEAM) | 29 | 41 | 71% (90d) | Does not open (62%) | 100% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 192 | [ ] | Stellar Blade™ (STEAM) | 29 | 37 | 78% (90d) | Does not open (50%) | 87% |  |
| 193 | [ ] | Capcom Fighting Collection (STEAM) | 29 | 33 | 88% (90d) | Does not open (87%) | 70% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 194 | [ ] | Dead Island Riptide Definitive Edition (STEAM) | 28 | 54 | 52% (90d) | Does not open (50%) | 80% |  |
| 195 | [ ] | Mortal Kombat X (STEAM) | 28 | 53 | 53% (90d) | Does not open (52%) | 84% |  |
| 196 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 28 | 48 | 58% (90d) | Controller issues (46%) | 94% |  |
| 197 | [ ] | Zero Escape: The Nonary Games (STEAM) | 28 | 46 | 61% (90d) | Does not open (88%) | 61% |  |
| 198 | [ ] | Binary Domain (STEAM) | 28 | 44 | 64% (90d) | Does not open (91%) | 79% |  |
| 199 | [ ] | Deus Ex™ GOTY Edition (GOG) | 28 | 44 | 64% (90d) | Does not open (38%) | 81% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 200 | [ ] | Crab Game (STEAM) | 28 | 37 | 76% (90d) | Does not open (58%) | 70% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 201 | [ ] | CRUEL (STEAM) | 28 | 34 | 82% (90d) | Does not open (89%) | 70% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 202 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 28 | 28 | 100% (90d) | Does not open (91%) | 62% | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 203 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 27 | 51 | 53% (90d) | Does not open (57%) | 67% |  |
| 204 | [ ] | Heavy Rain (STEAM) | 27 | 48 | 56% (90d) | Controller issues (62%) | 86% |  |
| 205 | [ ] | Akane (STEAM) | 27 | 46 | 59% (90d) | Controller issues (71%) | 100% |  |
| 206 | [ ] | Wizard of Legend (EPIC) | 27 | 45 | 60% (90d) | Does not open (77%) | 76% |  |
| 207 | [ ] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 27 | 39 | 69% (90d) | Does not open (82%) | 86% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 208 | [ ] | Palia (STEAM) | 27 | 37 | 73% (90d) | Does not open (62%) | 71% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 209 | [ ] | Tales of Zestiria (STEAM) | 27 | 33 | 82% (90d) | Does not open (81%) | 71% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 210 | [ ] | Prince of Persia (GOG) | 26 | 42 | 62% (90d) | Does not open (95%) | 83% |  |
| 211 | [ ] | Cat Mail Co. (STEAM) | 26 | 41 | 63% (90d) | Does not open (90%) | 88% |  |
| 212 | [ ] | Limbus Company (STEAM) | 26 | 40 | 65% (90d) | Does not open (86%) | 81% |  |
| 213 | [ ] | SWORN (STEAM) | 26 | 40 | 65% (90d) | Does not open (53%) | 100% |  |
| 214 | [ ] | Gothic II: Gold Classic (STEAM) | 26 | 39 | 67% (90d) | Does not open (59%) | 79% |  |
| 215 | [ ] | Ratatan (STEAM) | 26 | 39 | 67% (90d) | Does not open (47%) | 100% |  |
| 216 | [ ] | Goose Goose Duck (STEAM) | 26 | 33 | 79% (90d) | Does not open (73%) | 77% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 217 | [ ] | CarX Drift Racing Online (STEAM) | 25 | 50 | 50% (90d) | Does not open (50%) | 71% |  |
| 218 | [ ] | Being a DIK (STEAM) | 25 | 43 | 58% (90d) | Does not open (78%) | 86% |  |
| 219 | [ ] | Counter-Strike: Condition Zero (STEAM) | 25 | 43 | 58% (90d) | Does not open (53%) | 65% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 220 | [ ] | Digimon Survive (STEAM) | 25 | 42 | 60% (90d) | Controller issues (71%) | 96% |  |
| 221 | [ ] | Return to Monkey Island (STEAM) | 25 | 39 | 64% (90d) | No graphics (58%) | 94% |  |
| 222 | [ ] | Beyond: Two Souls (STEAM) | 25 | 33 | 76% (90d) | Does not open (46%) | 73% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 223 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 32 | 78% (90d) | Does not open (87%) | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 224 | [ ] | Resident Evil (GOG) | 25 | 27 | 93% (90d) | Does not open (95%) | 72% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 225 | [ ] | Resident Evil Revelations 2 (STEAM) | 24 | 47 | 51% (90d) | Does not open (40%) | 90% |  |
| 226 | [ ] | Moon Sweepers (STEAM) | 24 | 41 | 60% (1.3.0) | Controller issues (76%) | 83% |  |
| 227 | [ ] | Bongo Cat (STEAM) | 24 | 34 | 71% (90d) | Does not open (63%) | 79% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 228 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 24 | 33 | 73% (90d) | Does not open (57%) | 62% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 229 | [ ] | Need for Speed™ Unbound (STEAM) | 24 | 32 | 75% (90d) | Does not open (80%) | 75% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 230 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 23 | 44 | 52% (90d) | Controller issues (63%) | 94% |  |
| 231 | [ ] | Changed (STEAM) | 23 | 37 | 62% (90d) | Does not open (63%) | 87% |  |
| 232 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 36 | 64% (90d) | Does not open (100%) | 87% |  |
| 233 | [ ] | Timberborn (STEAM) | 23 | 35 | 66% (90d) | No graphics (62%) | 83% |  |
| 234 | [ ] | Party Animals (STEAM) | 23 | 32 | 72% (90d) | Does not open (75%) | 75% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 235 | [ ] | FINAL FANTASY XIV Online (STEAM) | 23 | 30 | 77% (90d) | Does not open (100%) | 95% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 236 | [ ] | Jade Empire: Special Edition (GOG) | 23 | 29 | 79% (90d) | Does not open (50%) | 79% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 237 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 23 | 29 | 79% (90d) | Does not open (40%) | 61% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 238 | [ ] | Tearscape (STEAM) | 23 | 27 | 85% (90d) | Controller issues (53%) | 90% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 239 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 23 | 25 | 92% (90d) | Does not open (63%) | 70% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 240 | [ ] | Football Manager 2024 (EPIC) | 22 | 40 | 55% (90d) | Does not open (86%) | 90% |  |
| 241 | [ ] | Mafia: Definitive Edition (STEAM) | 22 | 39 | 56% (90d) | Does not open (81%) | 90% |  |
| 242 | [ ] | This War of Mine (STEAM) | 22 | 39 | 56% (90d) | No graphics (56%) | 75% |  |
| 243 | [ ] | Lobotomy Corporation (STEAM) | 22 | 38 | 58% (90d) | No graphics (63%) | 100% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 244 | [ ] | Life is Strange Remastered (STEAM) | 22 | 34 | 65% (90d) | Does not open (73%) | 94% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 245 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 59 | 82% (1.3.0) | Does not open (79%) | 100% |  |
| 246 | [ ] | Unturned (STEAM) | 21 | 41 | 51% (90d) | Does not open (63%) | 81% |  |
| 247 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 21 | 40 | 53% (90d) | Does not open (53%) | 69% |  |
| 248 | [ ] | Gambonanza (STEAM) | 21 | 40 | 53% (90d) | Does not open (60%) | 92% |  |
| 249 | [ ] | Overlord (STEAM) | 21 | 39 | 54% (90d) | Does not open (71%) | 62% |  |
| 250 | [ ] | Pinball FX Classic (STEAM) | 21 | 39 | 54% (90d) | Does not open (75%) | 95% |  |
| 251 | [ ] | One-armed robber (STEAM) | 21 | 38 | 55% (90d) | Controller issues (61%) | 76% |  |
| 252 | [ ] | Trailmakers (STEAM) | 21 | 37 | 57% (90d) | Does not open (44%) | 92% |  |
| 253 | [ ] | Tiny Glade (STEAM) | 21 | 36 | 58% (90d) | Does not open (42%) | 71% |  |
| 254 | [ ] | Worms W.M.D (STEAM) | 21 | 35 | 60% (90d) | Does not open (61%) | 87% |  |
| 255 | [ ] | Nex Machina (STEAM) | 21 | 29 | 72% (90d) | Does not open (57%) | 88% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 256 | [ ] | Command & Conquer™ Red Alert™ 3 (STEAM) | 21 | 26 | 81% (90d) | Does not open (50%) | 60% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 257 | [ ] | Crimzon Clover World EXplosion (STEAM) | 20 | 39 | 51% (90d) | Does not open (47%) | 100% |  |
| 258 | [ ] | TCG Card Shop Simulator (STEAM) | 20 | 39 | 51% (90d) | Does not open (59%) | 85% |  |
| 259 | [ ] | Paper Lily - Chapter 1 (STEAM) | 20 | 38 | 53% (90d) | Does not open (72%) | 92% |  |
| 260 | [ ] | Control Ultimate Edition (GOG) | 20 | 37 | 54% (90d) | Does not open (81%) | 97% |  |
| 261 | [ ] | Killing Floor (STEAM) | 20 | 36 | 56% (90d) | Controller issues (100%) | 87% |  |
| 262 | [ ] | Tabletop Simulator (STEAM) | 20 | 33 | 61% (90d) | Does not open (50%) | 63% |  |
| 263 | [ ] | Hitman: Absolution (GOG) | 20 | 31 | 65% (90d) | Does not open (83%) | 93% |  |
| 264 | [ ] | DOOM 3: BFG Edition (GOG) | 20 | 27 | 74% (90d) | No graphics (65%) | 78% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 265 | [ ] | Torchlight II (EPIC) | 20 | 27 | 74% (90d) | Does not open (83%) | 100% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 266 | [ ] | BAJA: Edge of Control HD (STEAM) | 20 | 26 | 77% (90d) | Does not open (100%) | 90% | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 267 | [ ] | Dead Island (STEAM) | 20 | 26 | 77% (90d) | Does not open (69%) | 71% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 268 | [ ] | Backpack Battles (STEAM) | 19 | 36 | 53% (90d) | Does not open (63%) | 96% |  |
| 269 | [ ] | Breath of Fire IV (GOG) | 19 | 34 | 56% (90d) | Does not open (72%) | 61% |  |
| 270 | [ ] | Stick It to the Stickman (STEAM) | 19 | 34 | 56% (90d) | Does not open (88%) | 76% |  |
| 271 | [ ] | GRIP: Combat Racing (STEAM) | 19 | 33 | 58% (90d) | Does not open (100%) | 83% |  |
| 272 | [ ] | DNF Duel (EPIC) | 19 | 32 | 59% (90d) | Does not open (44%) | 88% |  |
| 273 | [ ] | Metro Exodus (STEAM) | 19 | 30 | 63% (90d) | Does not open (82%) | 88% |  |
| 274 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 19 | 28 | 68% (90d) | Does not open (72%) | 70% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 275 | [ ] | War Thunder (STEAM) | 19 | 25 | 76% (90d) | Does not open (53%) | 79% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 276 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 19 | 24 | 79% (90d) | Does not open (82%) | 100% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 277 | [ ] | SKALD: Against the Black Priory (STEAM) | 18 | 36 | 50% (90d) | No graphics (75%) | 100% |  |
| 278 | [ ] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 18 | 35 | 51% (90d) | Does not open (57%) | 91% |  |
| 279 | [ ] | SCP – Containment Breach (STEAM) | 18 | 35 | 51% (90d) | Does not open (83%) | 82% |  |
| 280 | [ ] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 18 | 34 | 53% (90d) | Controller issues (50%) | 100% |  |
| 281 | [ ] | Faster Than Light (EPIC) | 18 | 34 | 53% (90d) | Does not open (41%) | 92% |  |
| 282 | [ ] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 18 | 34 | 53% (90d) | Does not open (88%) | 65% |  |
| 283 | [ ] | My Summer Car (STEAM) | 18 | 33 | 55% (90d) | Does not open (56%) | 100% |  |
| 284 | [ ] | Formula Legends (STEAM) | 18 | 29 | 62% (90d) | No graphics (60%) | 75% |  |
| 285 | [ ] | Titanfall® 2 (STEAM) | 18 | 29 | 62% (90d) | Does not open (83%) | 88% |  |
| 286 | [ ] | Fall Guys (STEAM) | 18 | 24 | 75% (90d) | Does not open (92%) | 92% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 287 | [ ] | Deadly Premonition: The Director's Cut (STEAM) | 18 | 21 | 86% (90d) | Does not open (47%) | 75% |  |
| 288 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 21 | 86% (90d) | Does not open (67%) | 90% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 289 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 17 | 34 | 50% (90d) | Does not open (64%) | 69% |  |
| 290 | [ ] | Grim Fandango Remastered (STEAM) | 17 | 34 | 50% (90d) | Does not open (93%) | 81% |  |
| 291 | [ ] | CULTIC (STEAM) | 17 | 33 | 52% (90d) | Does not open (92%) | 69% |  |
| 292 | [ ] | Antichamber (STEAM) | 17 | 32 | 53% (90d) | Does not open (43%) | 88% |  |
| 293 | [ ] | GRANDIA HD Remaster (STEAM) | 17 | 31 | 55% (90d) | Does not open (93%) | 67% |  |
| 294 | [ ] | Shank 2 (STEAM) | 17 | 30 | 57% (90d) | Does not open (82%) | 100% |  |
| 295 | [ ] | Maneater (STEAM) | 17 | 28 | 61% (90d) | Does not open (92%) | 79% |  |
| 296 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 17 | 28 | 61% (90d) | No graphics (47%) | 83% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 297 | [ ] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 17 | 27 | 63% (90d) | Does not open (100%) | 95% |  |
| 298 | [ ] | Alabaster Dawn Demo (STEAM) | 17 | 26 | 65% (90d) | Controller issues (71%) | 92% |  |
| 299 | [ ] | Dishonored 2 (STEAM) | 17 | 26 | 65% (90d) | Does not open (86%) | 94% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 300 | [ ] | Arcade Paradise (EPIC) | 17 | 25 | 68% (90d) | Does not open (56%) | 86% |  |
| 301 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 17 | 24 | 71% (90d) | No graphics (60%) | 88% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 302 | [ ] | Katanaut (STEAM) | 17 | 24 | 71% (90d) | Does not open (75%) | 64% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 303 | [ ] | Prey (GOG) | 17 | 21 | 81% (90d) | Does not open (47%) | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 304 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 16 | 32 | 50% (90d) | Does not open (92%) | 65% |  |
| 305 | [ ] | Mortal Kombat 11 (STEAM) | 16 | 32 | 50% (90d) | Does not open (70%) | 65% |  |
| 306 | [ ] | Distance (STEAM) | 16 | 31 | 52% (90d) | Does not open (79%) | 82% |  |
| 307 | [ ] | Mark of the Ninja (STEAM) | 16 | 31 | 52% (90d) | Does not open (67%) | 63% |  |
| 308 | [ ] | Far Far West (STEAM) | 16 | 29 | 55% (90d) | Does not open (53%) | 91% |  |
| 309 | [ ] | Race The Sun (STEAM) | 16 | 29 | 55% (90d) | No graphics (92%) | 64% |  |
| 310 | [ ] | Wildermyth (STEAM) | 16 | 27 | 59% (90d) | Does not open (50%) | 91% |  |
| 311 | [ ] | WORLD OF FINAL FANTASY (STEAM) | 16 | 26 | 62% (90d) | No graphics (62%) | 74% |  |
| 312 | [ ] | Chef Knight (STEAM) | 16 | 23 | 70% (90d) | Does not open (93%) | 69% |  |
| 313 | [ ] | Realm of the Mad God Exalt (STEAM) | 16 | 21 | 76% (90d) | Does not open (91%) | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 314 | [ ] | Mortal Shell (EPIC) | 15 | 27 | 56% (90d) | No graphics (89%) | 81% |  |
| 315 | [ ] | LET IT DIE (STEAM) | 15 | 25 | 60% (90d) | Does not open (91%) | 77% |  |
| 316 | [ ] | Batman™: Arkham Origins (GOG) | 15 | 24 | 63% (90d) | Does not open (67%) | 92% |  |
| 317 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 15 | 24 | 63% (90d) | Does not open (92%) | 71% |  |
| 318 | [ ] | Gloomwood (STEAM) | 15 | 24 | 63% (90d) | Does not open (64%) | 60% |  |
| 319 | [ ] | Sorry We're Closed (EPIC) | 15 | 24 | 63% (90d) | Does not open (100%) | 77% |  |
| 320 | [ ] | Sons Of The Forest (STEAM) | 15 | 23 | 65% (90d) | Does not open (56%) | 76% |  |
| 321 | [ ] | Allumeria (STEAM) | 15 | 22 | 68% (90d) | Does not open (69%) | 64% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 322 | [ ] | Disgaea 4 Complete+ (STEAM) | 15 | 22 | 68% (90d) | No graphics (47%) | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 323 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 15 | 22 | 68% (90d) | Does not open (75%) | 64% |  |
| 324 | [ ] | DayZ (STEAM) | 15 | 21 | 71% (90d) | Does not open (56%) | 70% | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 325 | [ ] | Cyberpunk 2077 (EPIC) | 15 | 20 | 75% (90d) | Does not open (42%) | 83% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 326 | [ ] | Maneater (EPIC) | 15 | 20 | 75% (90d) | Does not open (73%) | 82% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 327 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 26 | 54% (90d) | Controller issues (54%) | 90% |  |
| 328 | [ ] | Academy Love Saga: Tennis Angels EX (STEAM) | 14 | 25 | 56% (90d) | Does not open (77%) | 93% |  |
| 329 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 25 | 56% (90d) | Does not open (90%) | 77% |  |
| 330 | [ ] | Ultrapool (STEAM) | 14 | 25 | 56% (90d) | Does not open (54%) | 100% |  |
| 331 | [ ] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 14 | 23 | 61% (90d) | Does not open (69%) | 75% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 332 | [ ] | Prince of Persia: The Two Thrones (STEAM) | 14 | 22 | 64% (90d) | Does not open (86%) | 61% |  |
| 333 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 22 | 64% (90d) | Controller issues (57%) | 62% |  |
| 334 | [ ] | Horny Villa (STEAM) | 14 | 20 | 70% (90d) | Does not open (63%) | 100% |  |
| 335 | [ ] | BioShock 2 Remastered (EPIC) | 13 | 26 | 50% (90d) | Does not open (56%) | 91% |  |
| 336 | [ ] | Haydee (STEAM) | 13 | 25 | 52% (90d) | Does not open (100%) | 88% |  |
| 337 | [ ] | sobosuba (STEAM) | 13 | 25 | 52% (90d) | Does not open (54%) | 92% |  |
| 338 | [ ] | Human Fall Flat (STEAM) | 13 | 24 | 54% (90d) | Does not open (58%) | 62% |  |
| 339 | [ ] | Injustice™ 2 (STEAM) | 13 | 24 | 54% (90d) | Does not open (90%) | 71% |  |
| 340 | [ ] | Pillars of Eternity (STEAM) | 13 | 24 | 54% (90d) | Does not open (43%) | 64% |  |
| 341 | [ ] | DiRT 4 (STEAM) | 13 | 23 | 57% (90d) | Does not open (75%) | 95% |  |
| 342 | [ ] | Minit (EPIC) | 13 | 23 | 57% (90d) | Does not open (82%) | 82% |  |
| 343 | [ ] | Lust Goddess (STEAM) | 13 | 22 | 59% (90d) | Does not open (100%) | 64% |  |
| 344 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 22 | 59% (90d) | Does not open (80%) | 91% |  |
| 345 | [ ] | Secret of Mana (STEAM) | 13 | 21 | 62% (90d) | Graphics glitches (58%) | 60% |  |
| 346 | [ ] | Escape the Backrooms (STEAM) | 13 | 20 | 65% (90d) | Does not open (100%) | 91% |  |
| 347 | [ ] | F.E.A.R. 2: Project Origin (STEAM) | 12 | 24 | 50% (90d) | Does not open (50%) | 81% |  |
| 348 | [ ] | Mina the Hollower (GOG) | 12 | 24 | 50% (90d) | Does not open (42%) | 67% |  |
| 349 | [ ] | AER Memories of Old (EPIC) | 12 | 23 | 52% (90d) | Does not open (91%) | 92% |  |
| 350 | [ ] | NiGHTS into Dreams... (STEAM) | 12 | 23 | 52% (90d) | Does not open (44%) | 91% |  |
| 351 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 12 | 22 | 55% (90d) | Does not open (60%) | 86% |  |
| 352 | [ ] | Sonic Superstars (STEAM) | 12 | 22 | 55% (90d) | Does not open (70%) | 69% |  |
| 353 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 12 | 21 | 57% (90d) | Does not open (86%) | 76% |  |
| 354 | [ ] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 21 | 57% (90d) | Controller issues (60%) | 93% |  |
| 355 | [ ] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 20 | 60% (90d) | Does not open (67%) | 64% |  |
| 356 | [ ] | Coromon (GOG) | 11 | 22 | 50% (90d) | No graphics (50%) | 67% |  |
| 357 | [ ] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 22 | 50% (90d) | Does not open (50%) | 67% |  |
| 358 | [ ] | Sid Meier's Civilization VI (EPIC) | 11 | 22 | 50% (90d) | Does not open (40%) | 88% |  |
| 359 | [ ] | Castle in the Clouds (STEAM) | 11 | 21 | 52% (90d) | No graphics (63%) | 88% |  |
| 360 | [ ] | Pocket Mirror ~ GoldenerTraum (STEAM) | 11 | 21 | 52% (90d) | Does not open (70%) | 100% |  |
| 361 | [ ] | Tom Clancy's Rainbow Six: Vegas 2 (STEAM) | 11 | 21 | 52% (90d) | Does not open (55%) | 85% |  |
| 362 | [ ] | Ready or Not (STEAM) | 11 | 20 | 55% (90d) | Does not open (60%) | 87% |  |
| 363 | [ ] | HITMAN World of Assassination (STEAM) | 10 | 20 | 50% (90d) | Does not open (67%) | 86% |  |

## Recently recovered (363)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 269 | 2026-10-23 | 310 | 65% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 2 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 250 | 2026-10-19 | 300 | 66% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 3 | [x] | FINAL FANTASY RESONANCE (STEAM) | 245 | 2026-10-24 | 547 | 71% |  |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 220 | 2026-10-18 | 337 | 58% |  |
| 5 | [x] | OMORI (STEAM) | 210 | 2026-10-16 | 253 | 77% |  |
| 6 | [x] | Devil May Cry HD Collection (STEAM) | 200 | 2026-10-19 | 280 | 74% |  |
| 7 | [x] | Burnout Paradise: The Ultimate Box (STEAM) | 162 | 2026-10-16 | 246 | 70% |  |
| 8 | [x] | Counter-Strike (STEAM) | 154 | 2026-10-22 | 239 | 51% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 9 | [x] | Far Cry® 3 (STEAM) | 140 | 2026-10-21 | 159 | 64% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 10 | [x] | Borderlands 2 (EPIC) | 139 | 2026-10-25 | 163 | 64% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 11 | [x] | Minecraft Dungeons II (STEAM) | 122 | 2026-10-21 | 139 | 65% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 12 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 120 | 2026-10-28 | 148 | 63% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 13 | [x] | Call of Duty: Black Ops III (STEAM) | 117 | 2026-10-18 | 240 | 72% |  |
| 14 | [x] | The Witcher: Enhanced Edition (STEAM) | 114 | 2026-10-25 | 132 | 65% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 15 | [x] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 110 | 2026-10-18 | 154 | 65% |  |
| 16 | [x] | Moonstone Island (STEAM) | 105 | 2026-10-16 | 138 | 91% |  |
| 17 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 101 | 2026-10-25 | 157 | 63% |  |
| 18 | [x] | Don't Starve Together (STEAM) | 96 | 2026-10-16 | 183 | 79% |  |
| 19 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 96 | 2026-10-17 | 129 | 100% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 20 | [x] | Cry of Fear (STEAM) | 91 | 2026-10-18 | 176 | 91% |  |
| 21 | [x] | Catherine Classic (STEAM) | 88 | 2026-10-19 | 180 | 79% |  |
| 22 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 87 | 2026-10-18 | 130 | 74% |  |
| 23 | [x] | DOOM 3: BFG Edition (STEAM) | 83 | 2026-10-19 | 119 | 71% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 24 | [x] | Ultra Street Fighter IV (STEAM) | 82 | 2026-10-17 | 179 | 68% |  |
| 25 | [x] | Hogwarts Legacy (STEAM) | 81 | 2026-10-17 | 138 | 66% |  |
| 26 | [x] | FINAL FANTASY XIII-2 (STEAM) | 81 | 2026-10-30 | 84 | 60% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 27 | [x] | Need for Speed: Hot Pursuit (STEAM) | 78 | 2026-10-25 | 107 | 74% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 28 | [x] | Detroit: Become Human (STEAM) | 78 | 2026-10-17 | 81 | 64% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 29 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 76 | 2026-10-17 | 103 | 84% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 30 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 74 | 2026-10-18 | 123 | 93% |  |
| 31 | [x] | Bayonetta (STEAM) | 73 | 2026-10-18 | 202 | 78% |  |
| 32 | [x] | Don't Starve (STEAM) | 72 | 2026-10-16 | 154 | 82% |  |
| 33 | [x] | Darksiders (STEAM) | 72 | 2026-10-26 | 87 | 87% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 34 | [x] | A Plague Tale: Innocence (STEAM) | 71 | 2026-10-20 | 74 | 75% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 35 | [x] | Fable - The Lost Chapters (STEAM) | 70 | 2026-10-17 | 109 | 77% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 36 | [x] | Dota 2 (STEAM) | 70 | 2026-10-17 | 107 | 71% |  |
| 37 | [x] | Gunfire Reborn (STEAM) | 70 | 2026-10-22 | 77 | 93% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 38 | [x] | Fallout (STEAM) | 69 | 2026-10-18 | 107 | 71% |  |
| 39 | [x] | Call of Juarez Gunslinger (STEAM) | 69 | 2026-10-18 | 84 | 72% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 40 | [x] | American Truck Simulator (STEAM) | 68 | 2026-10-18 | 108 | 74% |  |
| 41 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 68 | 2026-10-21 | 90 | 65% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 42 | [x] | Bloodstained: Ritual of the Night (EPIC) | 67 | 2026-10-19 | 123 | 65% |  |
| 43 | [x] | Spyro™ Reignited Trilogy (STEAM) | 66 | 2026-10-18 | 104 | 69% |  |
| 44 | [x] | Borderlands: The Pre-Sequel (STEAM) | 66 | 2026-10-17 | 92 | 67% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 45 | [x] | Disgaea 5 Complete (STEAM) | 66 | 2026-10-18 | 80 | 97% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 46 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 65 | 2026-10-17 | 87 | 92% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 47 | [x] | Poppy Playtime (STEAM) | 64 | 2026-10-17 | 109 | 78% |  |
| 48 | [x] | Big Walk (STEAM) | 63 | 2026-10-17 | 96 | 82% |  |
| 49 | [x] | Sonic Lost World (STEAM) | 62 | 2026-10-18 | 103 | 88% |  |
| 50 | [x] | eFootball™ (STEAM) | 60 | 2026-10-18 | 91 | 75% |  |
| 51 | [x] | Sonic Generations (STEAM) | 60 | 2026-10-17 | 70 | 66% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 52 | [x] | Starbound (STEAM) | 59 | 2026-10-18 | 85 | 72% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 53 | [x] | Borderlands 3 (STEAM) | 59 | 2026-10-19 | 76 | 95% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 54 | [x] | Sonic Adventure DX (STEAM) | 58 | 2026-10-17 | 94 | 70% |  |
| 55 | [x] | Call of Duty: World at War (STEAM) | 58 | 2026-10-28 | 81 | 62% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 56 | [x] | Dead by Daylight (STEAM) | 58 | 2026-10-23 | 63 | 81% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 57 | [x] | TBH: Task Bar Hero (STEAM) | 57 | 2026-10-19 | 86 | 94% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 58 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 55 | 2026-10-18 | 88 | 68% |  |
| 59 | [x] | Mini Motorways (STEAM) | 54 | 2026-10-29 | 96 | 62% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 60 | [x] | A Plague Tale: Innocence (EPIC) | 54 | 2026-10-25 | 91 | 88% |  |
| 61 | [x] | Path of Exile (STEAM) | 54 | 2026-10-26 | 63 | 85% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 62 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 54 | 2026-10-21 | 62 | 73% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 63 | [x] | MudRunner (STEAM) | 52 | 2026-10-24 | 102 | 64% |  |
| 64 | [x] | Until Then (STEAM) | 52 | 2026-10-17 | 93 | 97% |  |
| 65 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 51 | 2026-10-19 | 92 | 73% |  |
| 66 | [x] | Sheepy: A Short Adventure (STEAM) | 51 | 2026-10-24 | 61 | 82% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 67 | [x] | Alex Kidd in Miracle World DX (EPIC) | 51 | 2026-10-22 | 55 | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 68 | [x] | Street Fighter™ 6 (STEAM) | 50 | 2026-10-16 | 75 | 80% |  |
| 69 | [x] | Guildrun Demo (STEAM) | 50 | 2026-10-22 | 72 | 72% |  |
| 70 | [x] | Dead Space (STEAM) | 50 | 2026-10-18 | 63 | 72% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 71 | [x] | Sleeping Dogs™ (STEAM) | 50 | 2026-10-27 | 57 | 80% | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 72 | [x] | Okami HD (STEAM) | 49 | 2026-10-17 | 93 | 85% |  |
| 73 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 49 | 2026-10-18 | 75 | 65% |  |
| 74 | [x] | Rivals of Aether II (STEAM) | 49 | 2026-10-20 | 74 | 73% |  |
| 75 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 48 | 2026-10-25 | 90 | 58% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 76 | [x] | FINAL FANTASY VII (2013) (STEAM) | 48 | 2026-10-18 | 69 | 79% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 77 | [x] | STEINS;GATE RE:BOOT (STEAM) | 48 | 2026-10-21 | 69 | 79% |  |
| 78 | [x] | Digimon World: Next Order (STEAM) | 47 | 2026-10-18 | 87 | 94% |  |
| 79 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 2026-10-17 | 75 | 95% |  |
| 80 | [x] | Dishonored - Definitive Edition (EPIC) | 46 | 2026-10-17 | 97 | 81% |  |
| 81 | [x] | Darkest Dungeon® (EPIC) | 46 | 2026-10-22 | 83 | 63% |  |
| 82 | [x] | Tomb Raider: Anniversary (STEAM) | 46 | 2026-10-25 | 66 | 71% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 83 | [x] | Cobalt Core (STEAM) | 45 | 2026-10-18 | 96 | 87% |  |
| 84 | [x] | Abiotic Factor (STEAM) | 45 | 2026-10-18 | 79 | 69% |  |
| 85 | [x] | PROTOTYPE 2 (STEAM) | 44 | 2026-10-18 | 89 | 81% |  |
| 86 | [x] | Life is Strange™ (STEAM) | 44 | 2026-10-17 | 86 | 81% |  |
| 87 | [x] | Teardown (STEAM) | 44 | 2026-10-17 | 84 | 77% |  |
| 88 | [x] | Death Road to Canada (STEAM) | 43 | 2026-10-17 | 98 | 73% |  |
| 89 | [x] | Salt and Sanctuary (STEAM) | 43 | 2026-10-18 | 81 | 81% |  |
| 90 | [x] | Moonlighter (EPIC) | 43 | 2026-10-23 | 47 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 91 | [x] | Tomb Raider GOTY (GOG) | 42 | 2026-10-17 | 90 | 98% |  |
| 92 | [x] | Rogue Legacy (STEAM) | 42 | 2026-10-17 | 90 | 55% |  |
| 93 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 42 | 2026-10-17 | 77 | 87% |  |
| 94 | [x] | Rayman Origins (STEAM) | 41 | 2026-10-17 | 90 | 81% |  |
| 95 | [x] | Amnesia: The Dark Descent (STEAM) | 41 | 2026-10-17 | 76 | 77% |  |
| 96 | [x] | Deadlock (STEAM) | 41 | 2026-10-16 | 65 | 93% |  |
| 97 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 41 | 2026-10-18 | 62 | 70% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 98 | [x] | Capcom Arcade Stadium (STEAM) | 41 | 2026-10-17 | 51 | 76% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 99 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 40 | 2026-10-17 | 75 | 94% |  |
| 100 | [x] | Aggelos (STEAM) | 40 | 2026-10-21 | 54 | 94% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 101 | [x] | Sable (EPIC) | 39 | 2026-10-18 | 83 | 84% |  |
| 102 | [x] | Tales of ARISE (STEAM) | 39 | 2026-10-16 | 67 | 93% |  |
| 103 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 39 | 2026-10-27 | 41 | 82% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 104 | [x] | Monster Hunter Wilds (STEAM) | 39 | 2026-10-23 | 40 | 74% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 105 | [x] | CrossCode (GOG) | 38 | 2026-10-23 | 42 | 71% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 106 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 2026-10-17 | 67 | 86% |  |
| 107 | [x] | Romestead (STEAM) | 37 | 2026-10-18 | 48 | 77% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 108 | [x] | Hearts of Iron IV (STEAM) | 36 | 2026-10-19 | 62 | 62% |  |
| 109 | [x] | Rocket League (STEAM) | 36 | 2026-10-17 | 55 | 69% |  |
| 110 | [x] | Capcom Fighting Collection 2 (STEAM) | 36 | 2026-10-18 | 51 | 87% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 111 | [x] | POSTAL 2 (GOG) | 35 | 2026-10-22 | 72 | 96% |  |
| 112 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 35 | 2026-10-16 | 67 | 66% |  |
| 113 | [x] | Earthion (STEAM) | 35 | 2026-10-22 | 56 | 100% |  |
| 114 | [x] | Battle Brothers (STEAM) | 35 | 2026-10-27 | 50 | 64% |  |
| 115 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 35 | 2026-10-21 | 49 | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 116 | [x] | SnowRunner (STEAM) | 35 | 2026-10-19 | 48 | 83% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 117 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 35 | 2026-10-18 | 41 | 74% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 118 | [x] | Journey (STEAM) | 34 | 2026-10-27 | 70 | 55% |  |
| 119 | [x] | Ultimate Chicken Horse (STEAM) | 34 | 2026-10-23 | 70 | 54% |  |
| 120 | [x] | Ultimate Custom Night (STEAM) | 34 | 2026-10-19 | 46 | 77% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 121 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 34 | 2026-10-22 | 41 | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 122 | [x] | Monster Hunter Stories (STEAM) | 33 | 2026-10-17 | 68 | 84% |  |
| 123 | [x] | Max Payne (STEAM) | 33 | 2026-10-17 | 59 | 95% |  |
| 124 | [x] | Resident Evil Village (STEAM) | 33 | 2026-10-17 | 55 | 87% |  |
| 125 | [x] | Secrets of Grindea (STEAM) | 33 | 2026-10-20 | 51 | 82% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 126 | [x] | Counter-Strike:Global Offensive (STEAM) | 33 | 2026-10-19 | 50 | 74% |  |
| 127 | [x] | Supermarket Together (STEAM) | 33 | 2026-10-19 | 48 | 79% |  |
| 128 | [x] | Russian Fishing 4 (STEAM) | 33 | 2026-10-23 | 38 | 67% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 129 | [x] | Hotline Miami (GOG) | 33 | 2026-10-20 | 36 | 64% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 130 | [x] | Little Nightmares (STEAM) | 32 | 2026-10-16 | 71 | 61% |  |
| 131 | [x] | Bloodstained: Curse of the Moon (STEAM) | 32 | 2026-10-16 | 68 | 66% |  |
| 132 | [x] | COCOON (STEAM) | 32 | 2026-10-17 | 62 | 89% |  |
| 133 | [x] | Library Of Ruina (STEAM) | 32 | 2026-10-16 | 61 | 85% |  |
| 134 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 32 | 2026-10-19 | 53 | 65% |  |
| 135 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 32 | 2026-10-19 | 52 | 77% |  |
| 136 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 32 | 2026-10-22 | 50 | 76% |  |
| 137 | [x] | Nioh: Complete Edition (STEAM) | 32 | 2026-10-20 | 43 | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 138 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-10-20 | 42 | 89% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 139 | [x] | Path of Exile 2 (STEAM) | 32 | 2026-10-18 | 37 | 86% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 140 | [x] | Need for Speed™ (STEAM) | 32 | 2026-10-18 | 36 | 63% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 141 | [x] | Torchlight II (STEAM) | 31 | 2026-10-20 | 63 | 92% |  |
| 142 | [x] | Stumble Guys (STEAM) | 31 | 2026-10-18 | 62 | 82% |  |
| 143 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 31 | 2026-10-17 | 57 | 85% |  |
| 144 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 31 | 2026-10-26 | 55 | 65% |  |
| 145 | [x] | Tower and Sword of Succubus (STEAM) | 31 | 2026-10-22 | 46 | 100% |  |
| 146 | [x] | Super Animal Royale (STEAM) | 31 | 2026-10-19 | 40 | 77% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 147 | [x] | Grand Theft Auto III (STEAM) | 31 | 2026-10-17 | 39 | 89% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 148 | [x] | Dying Light (EPIC) | 30 | 2026-10-17 | 69 | 94% |  |
| 149 | [x] | BioShock™ (GOG) | 29 | 2026-10-18 | 62 | 69% |  |
| 150 | [x] | Cave Story+ (EPIC) | 29 | 2026-10-18 | 55 | 85% |  |
| 151 | [x] | Aethermancer (STEAM) | 29 | 2026-10-18 | 50 | 78% |  |
| 152 | [x] | Moonlight Peaks (STEAM) | 29 | 2026-10-20 | 41 | 100% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 153 | [x] | Capcom Fighting Collection (STEAM) | 29 | 2026-10-23 | 33 | 70% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 154 | [x] | State of Decay: Year-One (STEAM) | 28 | 2026-10-18 | 60 | 84% |  |
| 155 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 28 | 2026-10-18 | 54 | 80% |  |
| 156 | [x] | Mortal Kombat X (STEAM) | 28 | 2026-10-17 | 53 | 84% |  |
| 157 | [x] | Prince of Persia: The Sands of Time (STEAM) | 28 | 2026-10-20 | 48 | 94% |  |
| 158 | [x] | Zero Escape: The Nonary Games (STEAM) | 28 | 2026-10-17 | 46 | 61% |  |
| 159 | [x] | Deus Ex™ GOTY Edition (GOG) | 28 | 2026-10-19 | 44 | 81% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 160 | [x] | Binary Domain (STEAM) | 28 | 2026-10-18 | 44 | 79% |  |
| 161 | [x] | Crab Game (STEAM) | 28 | 2026-10-22 | 37 | 70% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 162 | [x] | CRUEL (STEAM) | 28 | 2026-10-28 | 34 | 70% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 163 | [x] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 28 | 2026-10-28 | 28 | 62% | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 164 | [x] | G.I. Joe Wrath of Cobra (EPIC) | 27 | 2026-10-19 | 51 | 67% |  |
| 165 | [x] | Heavy Rain (STEAM) | 27 | 2026-10-18 | 48 | 86% |  |
| 166 | [x] | Akane (STEAM) | 27 | 2026-10-20 | 46 | 100% |  |
| 167 | [x] | Wizard of Legend (EPIC) | 27 | 2026-10-18 | 45 | 76% |  |
| 168 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 27 | 2026-10-18 | 39 | 86% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 169 | [x] | Palia (STEAM) | 27 | 2026-10-22 | 37 | 71% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 170 | [x] | Tales of Zestiria (STEAM) | 27 | 2026-10-27 | 33 | 71% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 171 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 26 | 2026-10-19 | 89 | 93% |  |
| 172 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 26 | 2026-10-19 | 62 | 85% |  |
| 173 | [x] | PlateUp! (STEAM) | 26 | 2026-10-16 | 58 | 82% |  |
| 174 | [x] | Prince of Persia (GOG) | 26 | 2026-10-24 | 42 | 83% |  |
| 175 | [x] | Cat Mail Co. (STEAM) | 26 | 2026-10-24 | 41 | 88% |  |
| 176 | [x] | Limbus Company (STEAM) | 26 | 2026-10-18 | 40 | 81% |  |
| 177 | [x] | SWORN (STEAM) | 26 | 2026-10-23 | 40 | 100% |  |
| 178 | [x] | Gothic II: Gold Classic (STEAM) | 26 | 2026-10-20 | 39 | 79% |  |
| 179 | [x] | Goose Goose Duck (STEAM) | 26 | 2026-10-25 | 33 | 77% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 180 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 25 | 2026-10-20 | 52 | 82% |  |
| 181 | [x] | CarX Drift Racing Online (STEAM) | 25 | 2026-10-16 | 50 | 71% |  |
| 182 | [x] | Being a DIK (STEAM) | 25 | 2026-10-19 | 43 | 86% |  |
| 183 | [x] | Counter-Strike: Condition Zero (STEAM) | 25 | 2026-10-17 | 43 | 65% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 184 | [x] | Digimon Survive (STEAM) | 25 | 2026-10-23 | 42 | 96% |  |
| 185 | [x] | Return to Monkey Island (STEAM) | 25 | 2026-10-23 | 39 | 94% |  |
| 186 | [x] | Beyond: Two Souls (STEAM) | 25 | 2026-10-22 | 33 | 73% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 187 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-10-21 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 188 | [x] | Resident Evil (GOG) | 25 | 2026-10-20 | 27 | 72% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 189 | [x] | Titan Quest Anniversary Edition (STEAM) | 24 | 2026-10-16 | 55 | 83% |  |
| 190 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 54 | 87% |  |
| 191 | [x] | Bongo Cat (STEAM) | 24 | 2026-10-20 | 34 | 79% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 192 | [x] | Borderlands: The Pre-Sequel (EPIC) | 24 | 2026-10-30 | 33 | 62% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 193 | [x] | Need for Speed™ Unbound (STEAM) | 24 | 2026-10-26 | 32 | 75% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 194 | [x] | BlazBlue Centralfiction (STEAM) | 23 | 2026-10-17 | 62 | 82% |  |
| 195 | [x] | ABZÛ (STEAM) | 23 | 2026-10-21 | 51 | 91% |  |
| 196 | [x] | WEBFISHING (STEAM) | 23 | 2026-10-17 | 50 | 90% |  |
| 197 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 23 | 2026-10-27 | 47 | 28% |  |
| 198 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 23 | 2026-10-24 | 44 | 94% |  |
| 199 | [x] | Changed (STEAM) | 23 | 2026-10-24 | 37 | 87% |  |
| 200 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 2026-10-17 | 36 | 87% |  |
| 201 | [x] | Timberborn (STEAM) | 23 | 2026-10-25 | 35 | 83% |  |
| 202 | [x] | Party Animals (STEAM) | 23 | 2026-10-17 | 32 | 75% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 203 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 95% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 204 | [x] | Jade Empire: Special Edition (GOG) | 23 | 2026-10-23 | 29 | 79% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 205 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 23 | 2026-10-25 | 29 | 61% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 206 | [x] | Tearscape (STEAM) | 23 | 2026-10-30 | 27 | 90% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 207 | [x] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 23 | 2026-10-30 | 25 | 70% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 208 | [x] | Saints Row IV (STEAM) | 22 | 2026-10-19 | 51 | 75% |  |
| 209 | [x] | Football Manager 2024 (EPIC) | 22 | 2026-10-20 | 40 | 90% |  |
| 210 | [x] | Mafia: Definitive Edition (STEAM) | 22 | 2026-10-28 | 39 | 90% |  |
| 211 | [x] | This War of Mine (STEAM) | 22 | 2026-10-21 | 39 | 75% |  |
| 212 | [x] | Lobotomy Corporation (STEAM) | 22 | 2026-10-19 | 38 | 100% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 213 | [x] | Life is Strange Remastered (STEAM) | 22 | 2026-10-20 | 34 | 94% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 214 | [x] | No Rest for the Wicked (STEAM) | 21 | 2026-10-19 | 44 | 76% |  |
| 215 | [x] | Unturned (STEAM) | 21 | 2026-10-17 | 41 | 81% |  |
| 216 | [x] | Brothers - A Tale of Two Sons (EPIC) | 21 | 2026-10-23 | 40 | 69% |  |
| 217 | [x] | Overlord (STEAM) | 21 | 2026-10-21 | 39 | 62% |  |
| 218 | [x] | Pinball FX Classic (STEAM) | 21 | 2026-10-23 | 39 | 95% |  |
| 219 | [x] | One-armed robber (STEAM) | 21 | 2026-10-23 | 38 | 76% |  |
| 220 | [x] | Trailmakers (STEAM) | 21 | 2026-10-21 | 37 | 92% |  |
| 221 | [x] | Tiny Glade (STEAM) | 21 | 2026-10-24 | 36 | 71% |  |
| 222 | [x] | Nex Machina (STEAM) | 21 | 2026-10-18 | 29 | 88% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 223 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 21 | 2026-10-27 | 26 | 60% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 224 | [x] | Hatred (STEAM) | 20 | 2026-10-22 | 42 | 83% |  |
| 225 | [x] | MudRunner (EPIC) | 20 | 2026-10-18 | 41 | 90% |  |
| 226 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-10-20 | 39 | 100% |  |
| 227 | [x] | Paper Lily - Chapter 1 (STEAM) | 20 | 2026-10-27 | 38 | 92% |  |
| 228 | [x] | Killing Floor (STEAM) | 20 | 2026-10-19 | 36 | 87% |  |
| 229 | [x] | Tabletop Simulator (STEAM) | 20 | 2026-10-19 | 33 | 63% |  |
| 230 | [x] | Hitman: Absolution (GOG) | 20 | 2026-10-24 | 31 | 93% |  |
| 231 | [x] | Torchlight II (EPIC) | 20 | 2026-10-22 | 27 | 100% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 232 | [x] | DOOM 3: BFG Edition (GOG) | 20 | 2026-10-19 | 27 | 78% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 233 | [x] | BAJA: Edge of Control HD (STEAM) | 20 | 2026-10-28 | 26 | 90% | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 234 | [x] | Dead Island (STEAM) | 20 | 2026-10-20 | 26 | 71% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 235 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 19 | 2026-10-25 | 44 | 69% |  |
| 236 | [x] | Slow Roads (STEAM) | 19 | 2026-10-22 | 41 | 96% |  |
| 237 | [x] | Graveyard Keeper (GOG) | 19 | 2026-10-25 | 39 | 21% |  |
| 238 | [x] | Backpack Battles (STEAM) | 19 | 2026-10-21 | 36 | 96% |  |
| 239 | [x] | Breath of Fire IV (GOG) | 19 | 2026-10-26 | 34 | 61% |  |
| 240 | [x] | Stick It to the Stickman (STEAM) | 19 | 2026-10-17 | 34 | 76% |  |
| 241 | [x] | GRIP: Combat Racing (STEAM) | 19 | 2026-10-20 | 33 | 83% |  |
| 242 | [x] | DNF Duel (EPIC) | 19 | 2026-10-21 | 32 | 88% |  |
| 243 | [x] | Metro Exodus (STEAM) | 19 | 2026-10-20 | 30 | 88% |  |
| 244 | [x] | Sonic and SEGA All Stars Racing (STEAM) | 19 | 2026-10-19 | 28 | 70% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 245 | [x] | War Thunder (STEAM) | 19 | 2026-10-21 | 25 | 79% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 246 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 19 | 2026-10-23 | 24 | 100% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 247 | [x] | SKALD: Against the Black Priory (STEAM) | 18 | 2026-10-20 | 36 | 100% |  |
| 248 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 18 | 2026-10-18 | 35 | 91% |  |
| 249 | [x] | SCP – Containment Breach (STEAM) | 18 | 2026-10-27 | 35 | 82% |  |
| 250 | [x] | Faster Than Light (EPIC) | 18 | 2026-10-24 | 34 | 92% |  |
| 251 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 18 | 2026-10-21 | 34 | 100% |  |
| 252 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 18 | 2026-10-21 | 34 | 65% |  |
| 253 | [x] | My Summer Car (STEAM) | 18 | 2026-10-30 | 33 | 100% |  |
| 254 | [x] | Formula Legends (STEAM) | 18 | 2026-10-21 | 29 | 75% |  |
| 255 | [x] | Titanfall® 2 (STEAM) | 18 | 2026-10-16 | 29 | 88% |  |
| 256 | [x] | Fall Guys (STEAM) | 18 | 2026-10-26 | 24 | 92% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 257 | [x] | Jotunnslayer: Hordes of Hel (STEAM) | 18 | 2026-10-30 | 21 | 90% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 258 | [x] | Spin Rhythm XD (STEAM) | 17 | 2026-10-18 | 35 | 87% |  |
| 259 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 17 | 2026-10-20 | 34 | 69% |  |
| 260 | [x] | Grim Fandango Remastered (STEAM) | 17 | 2026-10-19 | 34 | 81% |  |
| 261 | [x] | CULTIC (STEAM) | 17 | 2026-10-24 | 33 | 69% |  |
| 262 | [x] | Antichamber (STEAM) | 17 | 2026-10-20 | 32 | 88% |  |
| 263 | [x] | GRANDIA HD Remaster (STEAM) | 17 | 2026-10-22 | 31 | 67% |  |
| 264 | [x] | Shank 2 (STEAM) | 17 | 2026-10-27 | 30 | 100% |  |
| 265 | [x] | Maneater (STEAM) | 17 | 2026-10-20 | 28 | 79% |  |
| 266 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 17 | 2026-10-20 | 28 | 83% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 267 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 17 | 2026-10-21 | 27 | 95% |  |
| 268 | [x] | Alabaster Dawn Demo (STEAM) | 17 | 2026-10-27 | 26 | 92% |  |
| 269 | [x] | Dishonored 2 (STEAM) | 17 | 2026-10-20 | 26 | 94% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 270 | [x] | Arcade Paradise (EPIC) | 17 | 2026-10-25 | 25 | 86% |  |
| 271 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 17 | 2026-10-21 | 24 | 88% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 272 | [x] | Katanaut (STEAM) | 17 | 2026-10-20 | 24 | 64% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 273 | [x] | Prey (GOG) | 17 | 2026-10-27 | 21 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 274 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 275 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 51 | 100% |  |
| 276 | [x] | No Man's Sky (GOG) | 16 | 2026-10-19 | 37 | 75% |  |
| 277 | [x] | Kingdom Come: Deliverance II (STEAM) | 16 | 2026-10-20 | 35 | 100% |  |
| 278 | [x] | Mortal Kombat 11 (STEAM) | 16 | 2026-10-28 | 32 | 65% |  |
| 279 | [x] | Distance (STEAM) | 16 | 2026-10-19 | 31 | 82% |  |
| 280 | [x] | Mark of the Ninja (STEAM) | 16 | 2026-10-26 | 31 | 63% |  |
| 281 | [x] | Far Far West (STEAM) | 16 | 2026-10-21 | 29 | 91% |  |
| 282 | [x] | Race The Sun (STEAM) | 16 | 2026-10-28 | 29 | 64% |  |
| 283 | [x] | Wildermyth (STEAM) | 16 | 2026-10-26 | 27 | 91% |  |
| 284 | [x] | WORLD OF FINAL FANTASY (STEAM) | 16 | 2026-10-19 | 26 | 74% |  |
| 285 | [x] | Chef Knight (STEAM) | 16 | 2026-10-27 | 23 | 69% |  |
| 286 | [x] | Realm of the Mad God Exalt (STEAM) | 16 | 2026-10-29 | 21 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 287 | [x] | Mortal Shell (EPIC) | 15 | 2026-10-19 | 27 | 81% |  |
| 288 | [x] | LET IT DIE (STEAM) | 15 | 2026-10-25 | 25 | 77% |  |
| 289 | [x] | Batman™: Arkham Origins (GOG) | 15 | 2026-10-22 | 24 | 92% |  |
| 290 | [x] | Gloomwood (STEAM) | 15 | 2026-10-29 | 24 | 60% |  |
| 291 | [x] | Sons Of The Forest (STEAM) | 15 | 2026-10-19 | 23 | 76% |  |
| 292 | [x] | Allumeria (STEAM) | 15 | 2026-10-23 | 22 | 64% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 293 | [x] | Disgaea 4 Complete+ (STEAM) | 15 | 2026-10-23 | 22 | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 294 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 15 | 2026-10-23 | 22 | 64% |  |
| 295 | [x] | DayZ (STEAM) | 15 | 2026-10-29 | 21 | 70% | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 296 | [x] | Cyberpunk 2077 (EPIC) | 15 | 2026-10-19 | 20 | 83% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 297 | [x] | Maneater (EPIC) | 15 | 2026-10-28 | 20 | 82% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 298 | [x] | Tom Clancy's Splinter Cell: Chaos Theory (STEAM) | 14 | 2026-10-16 | 30 | 84% |  |
| 299 | [x] | Rayman Origins (GOG) | 14 | 2026-10-25 | 29 | 59% |  |
| 300 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 2026-10-29 | 26 | 90% |  |
| 301 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 14 | 2026-10-21 | 25 | 93% |  |
| 302 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 2026-10-25 | 25 | 77% |  |
| 303 | [x] | Ultrapool (STEAM) | 14 | 2026-10-24 | 25 | 100% |  |
| 304 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 14 | 2026-10-20 | 23 | 75% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 305 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 61% |  |
| 306 | [x] | Super Monkey Ball Banana Mania (STEAM) | 14 | 2026-10-18 | 22 | 62% |  |
| 307 | [x] | Horny Villa (STEAM) | 14 | 2026-10-21 | 20 | 100% |  |
| 308 | [x] | Middle-earth™: Shadow of War™ (STEAM) | 13 | 2026-10-16 | 38 | 82% |  |
| 309 | [x] | Blood: Fresh Supply (STEAM) | 13 | 2026-10-16 | 35 | 79% |  |
| 310 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 32 | 63% |  |
| 311 | [x] | The WereCleaner (STEAM) | 13 | 2026-10-22 | 32 | 95% |  |
| 312 | [x] | Battle Chasers: Nightwar (STEAM) | 13 | 2026-10-20 | 28 | 67% |  |
| 313 | [x] | Haiku, the Robot (STEAM) | 13 | 2026-10-21 | 27 | 85% |  |
| 314 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 27 | 59% |  |
| 315 | [x] | Haydee (STEAM) | 13 | 2026-10-22 | 25 | 88% |  |
| 316 | [x] | Human Fall Flat (STEAM) | 13 | 2026-10-29 | 24 | 62% |  |
| 317 | [x] | Injustice™ 2 (STEAM) | 13 | 2026-10-17 | 24 | 71% |  |
| 318 | [x] | Pillars of Eternity (STEAM) | 13 | 2026-10-26 | 24 | 64% |  |
| 319 | [x] | DiRT 4 (STEAM) | 13 | 2026-10-20 | 23 | 95% |  |
| 320 | [x] | Lust Goddess (STEAM) | 13 | 2026-10-26 | 22 | 64% |  |
| 321 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-10-21 | 22 | 91% |  |
| 322 | [x] | Secret of Mana (STEAM) | 13 | 2026-10-28 | 21 | 60% |  |
| 323 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 13 | 2026-10-25 | 20 | 94% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 324 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 91% |  |
| 325 | [x] | Possessor(s) (STEAM) | 12 | 2026-10-24 | 28 | 100% |  |
| 326 | [x] | Dead Space™ 3 (STEAM) | 12 | 2026-10-20 | 26 | 71% |  |
| 327 | [x] | Revolution Idle (STEAM) | 12 | 2026-10-26 | 25 | n/a |  |
| 328 | [x] | Mina the Hollower (GOG) | 12 | 2026-10-28 | 24 | 67% |  |
| 329 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 12 | 2026-10-21 | 24 | 81% |  |
| 330 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-10-28 | 23 | 91% |  |
| 331 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-10-22 | 22 | 86% |  |
| 332 | [x] | Sonic Superstars (STEAM) | 12 | 2026-10-21 | 22 | 69% |  |
| 333 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 12 | 2026-10-24 | 21 | 76% |  |
| 334 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 2026-10-26 | 21 | 93% |  |
| 335 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 336 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 12 | 2026-10-28 | 20 | 64% |  |
| 337 | [x] | TowerFall Ascension (STEAM) | 11 | 2026-10-16 | 31 | 53% |  |
| 338 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 11 | 2026-10-19 | 28 | 100% |  |
| 339 | [x] | SteamWorld Heist (GOG) | 11 | 2026-10-25 | 23 | n/a |  |
| 340 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 23 | 78% |  |
| 341 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 11 | 2026-10-20 | 23 | 71% |  |
| 342 | [x] | Sid Meier's Civilization VI (EPIC) | 11 | 2026-10-19 | 22 | 88% |  |
| 343 | [x] | Coromon (GOG) | 11 | 2026-10-19 | 22 | 67% |  |
| 344 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 2026-10-27 | 22 | 67% |  |
| 345 | [x] | Castle in the Clouds (STEAM) | 11 | 2026-10-21 | 21 | 88% |  |
| 346 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 11 | 2026-10-23 | 21 | 100% |  |
| 347 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 348 | [x] | What Remains of Edith Finch (STEAM) | 10 | 2026-10-19 | 26 | 44% |  |
| 349 | [x] | Divinity: Original Sin (Classic) (STEAM) | 10 | 2026-10-16 | 25 | 80% |  |
| 350 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 23 | 93% |  |
| 351 | [x] | 12 is Better Than 6 (STEAM) | 10 | 2026-10-21 | 21 | 81% |  |
| 352 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 21 | 85% |  |
| 353 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 354 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 355 | [x] | Delver (STEAM) | 9 | 2026-10-17 | 22 | 73% |  |
| 356 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 9 | 2026-10-23 | 21 | 75% |  |
| 357 | [x] | DRAGON BALL XENOVERSE (STEAM) | 9 | 2026-10-28 | 20 | 55% |  |
| 358 | [x] | Football Manager 2024 (STEAM) | 9 | 2026-10-16 | 20 | n/a |  |
| 359 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 9 | 2026-10-20 | 20 | n/a |  |
| 360 | [x] | Gloomhaven (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 361 | [x] | Intravenous (STEAM) | 8 | 2026-10-16 | 20 | 94% |  |
| 362 | [x] | Mafia II: Definitive Edition (STEAM) | 7 | 2026-10-16 | 20 | n/a |  |
| 363 | [x] | Alex Kidd in Miracle World DX (STEAM) | 2 | 2026-10-16 | 36 | 82% |  |
