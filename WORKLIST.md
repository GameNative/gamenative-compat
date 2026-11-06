# GameNative compatibility worklist

Generated: `2026-11-06T04:15:05.810Z` · App release: `1.3.0` · Ratings since: `2026-08-08T04:15:05.810Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 242 |
| Probably does not work | 84 |
| First launch fails | 352 |
| Mixed | 468 |
| Works | 1021 |
| Total | 2167 |

## Does not work (242)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [x] 2026-10-18 | Project Zomboid (STEAM) | 589 | 622 | 93% (1.3.0) | Does not open (66%) | 56% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 2 | [x] 2026-10-18 | Alan Wake (STEAM) | 251 | 263 | 88% (1.3.0) | Does not open (87%) | 10% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 3 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 238 | 258 | 92% (90d) | Does not open (77%) | 11% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 4 | [ ] | Counter-Strike 2 (STEAM) | 235 | 318 | 83% (1.3.0) | Does not open (62%) | 45% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 5 | [x] 2026-10-18 | Call of Duty: Black Ops (STEAM) | 209 | 221 | 95% (90d) | Does not open (76%) | 12% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 6 | [ ] | skate. (STEAM) | 189 | 202 | 94% (90d) | Does not open (80%) | 16% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 7 | [ ] | Peggle Deluxe (STEAM) | 152 | 184 | 83% (90d) | Does not open (92%) | 34% | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 8 | [ ] | Necesse (STEAM) | 152 | 157 | 97% (90d) | Does not open (80%) | 44% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 9 | [ ] | HELLDIVERS™ 2 (STEAM) | 138 | 144 | 96% (90d) | Does not open (92%) | 17% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 10 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 131 | 146 | 90% (90d) | Does not open (86%) | 46% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 11 | [ ] | Assassin's Creed II (STEAM) | 124 | 129 | 96% (90d) | Does not open (78%) | 52% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 12 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 104 | 138 | 76% (1.3.0) | Does not open (74%) | 37% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 13 | [ ] | The Witcher: Enhanced Edition (GOG) | 103 | 112 | 92% (90d) | Does not open (74%) | 15% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 14 | [ ] | Dust: An Elysian Tail (STEAM) | 103 | 108 | 95% (90d) | Does not open (74%) | 8% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 15 | [ ] | Call of Duty: Black Ops II (STEAM) | 101 | 132 | 86% (1.3.0) | Does not open (78%) | 28% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 16 | [ ] | Saints Row 2 (STEAM) | 97 | 108 | 93% (1.3.0) | Does not open (96%) | 40% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 17 | [ ] | Mafia II (Classic) (STEAM) | 92 | 97 | 95% (90d) | Does not open (73%) | 6% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 18 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 87 | 91 | 100% (1.3.0) | Does not open (77%) | 0% | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 19 | [ ] | Duskfade (STEAM) | 87 | 89 | 98% (90d) | Does not open (95%) | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 20 | [ ] | Transistor (STEAM) | 87 | 87 | 100% (90d) | Does not open (74%) | 0% | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 21 | [ ] | Saints Row: The Third (STEAM) | 86 | 87 | 99% (90d) | Does not open (77%) | 31% | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 22 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 84 | 97 | 87% (90d) | Does not open (69%) | 53% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 23 | [ ] | Sniper Elite 4 (STEAM) | 83 | 83 | 100% (90d) | Does not open (97%) | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 24 | [ ] | Black Mesa (STEAM) | 82 | 113 | 73% (90d) | Does not open (81%) | 14% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 25 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 81 | 83 | 98% (90d) | Does not open (90%) | 57% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 26 | [ ] | Fall Guys (EPIC) | 79 | 91 | 87% (90d) | Does not open (75%) | 15% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 27 | [ ] | HELLDIVERS™ (STEAM) | 78 | 87 | 90% (90d) | Does not open (59%) | 43% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 28 | [ ] | MECCHA CHAMELEON (STEAM) | 76 | 108 | 70% (90d) | Does not open (65%) | 59% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 29 | [ ] | Detroit: Become Human (STEAM) | 76 | 79 | 96% (90d) | Does not open (71%) | 54% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 30 | [ ] | Dead Space 2 (STEAM) | 75 | 96 | 78% (90d) | Does not open (72%) | 33% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 31 | [ ] | GRID 2 (STEAM) | 75 | 78 | 96% (90d) | Does not open (68%) | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 32 | [ ] | The Wolf Among Us (STEAM) | 72 | 78 | 92% (90d) | Does not open (67%) | 16% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 33 | [ ] | Saints Row 2 (GOG) | 68 | 81 | 84% (90d) | Does not open (96%) | 46% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 34 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 68 | 73 | 93% (90d) | Does not open (79%) | 10% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 35 | [ ] | Call of Duty: Black Ops II - Zombies (STEAM) | 67 | 83 | 81% (90d) | Does not open (69%) | 49% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 36 | [x] 2026-10-18 | Diablo® IV (STEAM) | 67 | 79 | 85% (90d) | Does not open (61%) | 23% | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 37 | [ ] | Marvel Rivals (STEAM) | 66 | 74 | 89% (90d) | Does not open (81%) | 0% | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 38 | [ ] | Door Kickers 2 (STEAM) | 66 | 70 | 94% (90d) | No graphics (85%) | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 39 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 65 | 74 | 95% (1.3.0) | No graphics (47%) | 18% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 40 | [ ] | Borderlands GOTY (STEAM) | 64 | 69 | 93% (90d) | Does not open (95%) | 18% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 41 | [ ] | Burnout™ Paradise Remastered (STEAM) | 64 | 67 | 96% (90d) | Does not open (88%) | 19% | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 42 | [ ] | GRID (STEAM) | 63 | 80 | 79% (90d) | Does not open (57%) | 44% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 43 | [ ] | Metro 2033 (STEAM) | 63 | 79 | 80% (90d) | Does not open (61%) | 40% | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 44 | [ ] | Three Kingdoms : Alias (STEAM) | 62 | 66 | 94% (90d) | No graphics (97%) | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 45 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 62 | 62 | 100% (90d) | Does not open (53%) | 10% | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 46 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 60 | 85 | 71% (90d) | Does not open (84%) | 48% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 47 | [ ] | Need for Speed™ Heat  (STEAM) | 57 | 71 | 80% (90d) | Does not open (78%) | 27% | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 48 | [ ] | DOOM (2016) (GOG) | 57 | 63 | 90% (90d) | Does not open (90%) | 39% | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 49 | [ ] | Enshrouded (STEAM) | 57 | 58 | 98% (90d) | Does not open (95%) | 22% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 50 | [ ] | Spore (STEAM) | 56 | 60 | 93% (90d) | Does not open (68%) | 36% | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 51 | [ ] | XCOM: Enemy Unknown (STEAM) | 56 | 59 | 95% (90d) | Does not open (77%) | 4% | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 52 | [ ] | Overwatch® (STEAM) | 55 | 57 | 96% (90d) | Does not open (58%) | 31% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 53 | [ ] | GrandChase (STEAM) | 54 | 57 | 95% (90d) | Does not open (84%) | 12% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 54 | [ ] | STAR WARS Zero Company™ (STEAM) | 53 | 55 | 96% (90d) | Does not open (64%) | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 55 | [ ] | Spec Ops: The Line (STEAM) | 53 | 54 | 98% (90d) | No graphics (56%) | 0% | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 56 | [ ] | Watch_Dogs (STEAM) | 52 | 67 | 78% (90d) | Does not open (90%) | 17% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 57 | [ ] | Max Payne 3 (STEAM) | 51 | 56 | 91% (90d) | Does not open (93%) | 41% | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 58 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 50 | 64 | 78% (90d) | Does not open (90%) | 58% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 59 | [ ] | Trackmania (STEAM) | 50 | 63 | 79% (90d) | Does not open (86%) | 37% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 60 | [ ] | Sandustry (STEAM) | 50 | 62 | 81% (90d) | Does not open (73%) | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 61 | [ ] | METAL SLUG 3 (STEAM) | 50 | 60 | 83% (90d) | Does not open (80%) | 23% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 62 | [ ] | Prince of Persia The Lost Crown (STEAM) | 50 | 54 | 93% (90d) | Does not open (95%) | 33% | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 63 | [ ] | RoboCop: Rogue City (STEAM) | 50 | 54 | 93% (90d) | Does not open (37%) | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 64 | [ ] | South Park The Fractured But Whole (STEAM) | 50 | 50 | 100% (90d) | Does not open (67%) | 16% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 65 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 49 | 64 | 77% (90d) | Does not open (80%) | 41% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 66 | [ ] | Fortune Mill (STEAM) | 49 | 49 | 100% (90d) | Does not open (90%) | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 67 | [ ] | Scott Pilgrim vs The World (STEAM) | 49 | 49 | 100% (90d) | Does not open (83%) | 50% | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 68 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 48 | 69 | 70% (90d) | Does not open (83%) | 52% | [#481](https://github.com/GameNative/gamenative-compat/issues/481) |
| 69 | [ ] | DOOM Eternal (STEAM) | 48 | 50 | 96% (90d) | Does not open (69%) | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 70 | [ ] | Asphalt Legends  (STEAM) | 47 | 55 | 85% (90d) | Does not open (79%) | 47% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 71 | [ ] | tModLoader (STEAM) | 47 | 54 | 87% (90d) | Does not open (86%) | 4% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 72 | [ ] | DOOM 3 (STEAM) | 47 | 52 | 90% (90d) | Does not open (92%) | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 73 | [ ] | Hitman: Absolution (STEAM) | 47 | 52 | 90% (90d) | Does not open (84%) | 7% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 74 | [ ] | Aliens vs. Predator (STEAM) | 45 | 50 | 90% (90d) | No graphics (56%) | 28% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 75 | [ ] | STAR WARS™ Republic Commando (STEAM) | 45 | 47 | 96% (90d) | Does not open (80%) | 50% | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 76 | [ ] | To The Moon (GOG) | 44 | 48 | 96% (1.3.0) | Does not open (86%) | n/a | [#474](https://github.com/GameNative/gamenative-compat/issues/474) |
| 77 | [ ] | The Survivalists (STEAM) | 44 | 46 | 96% (90d) | Does not open (98%) | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 78 | [ ] | Mafia: Definitive Edition (GOG) | 43 | 56 | 77% (90d) | Does not open (85%) | 32% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 79 | [ ] | Diablo + Hellfire (GOG) | 43 | 49 | 88% (90d) | Does not open (64%) | 25% | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 80 | [ ] | Split/Second (STEAM) | 43 | 47 | 91% (90d) | Does not open (79%) | 9% | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 81 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 43 | 44 | 98% (90d) | Does not open (84%) | 45% | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 82 | [ ] | Metro: Last Light Redux (STEAM) | 41 | 98 | 82% (1.3.0) | Does not open (93%) | 36% | [#473](https://github.com/GameNative/gamenative-compat/issues/473) |
| 83 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 41 | 45 | 91% (90d) | Does not open (71%) | 29% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 84 | [ ] | Tales of Berseria (STEAM) | 40 | 41 | 98% (90d) | Does not open (89%) | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 85 | [ ] | Need for Speed™ Rivals (STEAM) | 39 | 49 | 80% (90d) | Does not open (60%) | 42% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 86 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 39 | 40 | 98% (90d) | Does not open (67%) | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 87 | [ ] | Mafia (STEAM) | 38 | 43 | 88% (90d) | Does not open (69%) | 40% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 88 | [ ] | DJMAX RESPECT V (STEAM) | 38 | 42 | 90% (90d) | Does not open (82%) | 30% | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 89 | [ ] | GeoGuessr Steam Edition (STEAM) | 38 | 39 | 97% (90d) | No graphics (62%) | n/a | [#154](https://github.com/GameNative/gamenative-compat/issues/154) |
| 90 | [ ] | L.A. Noire (STEAM) | 37 | 44 | 84% (90d) | Does not open (100%) | 46% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 91 | [ ] | Beat Saber (STEAM) | 37 | 43 | 86% (90d) | Does not open (47%) | 31% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 92 | [ ] | ARC Raiders (STEAM) | 37 | 42 | 88% (90d) | Does not open (91%) | 0% | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 93 | [ ] | Marvel's Spider-Man 2 (STEAM) | 37 | 39 | 95% (90d) | Does not open (86%) | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 94 | [ ] | Dragon's Dogma 2 (STEAM) | 37 | 38 | 97% (90d) | Does not open (91%) | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 95 | [ ] | Utopia Must Fall (STEAM) | 37 | 38 | 97% (90d) | Does not open (84%) | n/a | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 96 | [ ] | ScourgeBringer (STEAM) | 36 | 41 | 88% (90d) | Does not open (71%) | 6% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 97 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 36 | 38 | 95% (90d) | Does not open (94%) | 30% | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 98 | [ ] | CODE VEIN (STEAM) | 35 | 50 | 70% (90d) | Does not open (68%) | 39% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 99 | [ ] | CARRION (GOG) | 35 | 43 | 81% (90d) | Does not open (73%) | 8% | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 100 | [ ] | FINAL FANTASY VIII (STEAM) | 35 | 43 | 81% (90d) | Does not open (65%) | 55% | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 101 | [ ] | GOALS (STEAM) | 35 | 42 | 83% (90d) | Does not open (83%) | 24% | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 102 | [ ] | Barotrauma (STEAM) | 35 | 38 | 92% (90d) | Does not open (97%) | 36% | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 103 | [ ] | BIT.TRIP RUNNER (STEAM) | 35 | 37 | 95% (90d) | Does not open (63%) | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 104 | [ ] | Axiom Verge 2 (STEAM) | 35 | 36 | 97% (90d) | Does not open (57%) | 18% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 105 | [ ] | CPM 2 (STEAM) | 34 | 42 | 81% (90d) | Does not open (88%) | 10% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 106 | [ ] | BattleBit Remastered (STEAM) | 34 | 38 | 89% (90d) | Does not open (64%) | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 107 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 34 | 38 | 89% (90d) | Does not open (62%) | 29% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 108 | [ ] | Muv-Luv (STEAM) | 34 | 35 | 97% (90d) | Does not open (86%) | 31% | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 109 | [ ] | Gauntlet™  (STEAM) | 33 | 47 | 70% (90d) | Does not open (64%) | 38% | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 110 | [ ] | Lost Planet: Extreme Condition (STEAM) | 33 | 41 | 80% (90d) | Does not open (77%) | 39% | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 111 | [ ] | OneShot (STEAM) | 33 | 37 | 89% (90d) | Does not open (96%) | 17% | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 112 | [ ] | Forza Horizon 6 (STEAM) | 33 | 34 | 97% (90d) | Does not open (58%) | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 113 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 33 | 34 | 97% (90d) | No graphics (59%) | 12% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 114 | [ ] | Death Stranding (EPIC) | 32 | 35 | 91% (90d) | Does not open (78%) | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 115 | [ ] | Wolfenstein 3D (STEAM) | 32 | 35 | 91% (90d) | Does not open (50%) | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 116 | [ ] | Insaniquarium! Deluxe (STEAM) | 31 | 38 | 82% (90d) | Does not open (86%) | 39% | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 117 | [ ] | King's Bounty: The Legend (STEAM) | 31 | 35 | 89% (90d) | Does not open (100%) | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 118 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 31 | 34 | 91% (90d) | Does not open (67%) | 0% | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 119 | [ ] | Umamusume: Pretty Derby (STEAM) | 31 | 33 | 94% (90d) | Does not open (86%) | 55% | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 120 | [ ] | Rayman Legends (STEAM) | 31 | 32 | 97% (90d) | Does not open (96%) | 39% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 121 | [ ] | Quantum Break (STEAM) | 31 | 31 | 100% (90d) | Does not open (90%) | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 122 | [ ] | Beholder (EPIC) | 30 | 35 | 86% (90d) | Does not open (69%) | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 123 | [ ] | Far Cry 4 (STEAM) | 30 | 34 | 88% (90d) | Does not open (100%) | 27% | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 124 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 30 | 33 | 91% (90d) | Does not open (85%) | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 125 | [ ] | Need for Speed™ (STEAM) | 30 | 32 | 94% (90d) | Does not open (69%) | 56% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 126 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 30 | 30 | 100% (90d) | Does not open (72%) | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 127 | [ ] | The Darkness II (STEAM) | 30 | 30 | 100% (90d) | Does not open (81%) | 25% | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 128 | [ ] | Magicka (STEAM) | 29 | 32 | 91% (90d) | Does not open (63%) | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 129 | [ ] | Forza Horizon 5 (STEAM) | 29 | 31 | 94% (90d) | Does not open (71%) | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 130 | [ ] | Grand Theft Auto III - The Definitive Edition (STEAM) | 29 | 29 | 100% (90d) | Does not open (92%) | 17% | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 131 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 29 | 29 | 100% (90d) | Does not open (70%) | 0% | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 132 | [ ] | Dark Sector (STEAM) | 28 | 37 | 76% (90d) | Does not open (68%) | 45% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 133 | [ ] | PAYDAY 2 (STEAM) | 28 | 31 | 90% (90d) | Does not open (79%) | 29% | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 134 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 28 | 30 | 93% (90d) | Does not open (77%) | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 135 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 28 | 29 | 97% (90d) | Does not open (82%) | 38% | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 136 | [ ] | Breath of Fire IV (STEAM) | 28 | 28 | 100% (90d) | Does not open (56%) | 20% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 137 | [ ] | Audiosurf (STEAM) | 27 | 38 | 71% (90d) | Does not open (44%) | 45% | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 138 | [ ] | Mirror's Edge™ (GOG) | 27 | 38 | 71% (90d) | No graphics (62%) | 40% | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 139 | [ ] | Mass Effect (2007) (STEAM) | 27 | 32 | 84% (90d) | Does not open (76%) | 39% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 140 | [ ] | The Planet Crafter (STEAM) | 27 | 32 | 84% (90d) | Does not open (55%) | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 141 | [ ] | Borderlands 2 RU (STEAM) | 27 | 29 | 93% (90d) | Does not open (58%) | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 142 | [ ] | DiRT Showdown (STEAM) | 27 | 28 | 96% (90d) | Does not open (56%) | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 143 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 27 | 27 | 100% (90d) | Does not open (90%) | 50% | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 144 | [ ] | Alpha Protocol (STEAM) | 26 | 30 | 87% (90d) | Does not open (57%) | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 145 | [ ] | Northgard: Definitive Edition (STEAM) | 26 | 29 | 90% (90d) | Does not open (96%) | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 146 | [ ] | Persona 5 Strikers (STEAM) | 26 | 29 | 90% (90d) | Does not open (78%) | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 147 | [ ] | AION 2 (STEAM) | 26 | 28 | 93% (90d) | Does not open (65%) | 5% | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 148 | [ ] | Isle of Reveries (STEAM) | 26 | 27 | 96% (90d) | Does not open (95%) | 25% | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 149 | [ ] | theHunter Classic (STEAM) | 26 | 26 | 100% (1.3.0) | No graphics (92%) | n/a | [#480](https://github.com/GameNative/gamenative-compat/issues/480) |
| 150 | [ ] | EA SPORTS FC™ 26 (STEAM) | 25 | 33 | 76% (90d) | Does not open (75%) | n/a | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 151 | [ ] | Knights of Pen and Paper 2 (STEAM) | 25 | 33 | 76% (90d) | Does not open (45%) | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 152 | [ ] | Kenshi (STEAM) | 25 | 32 | 78% (90d) | Does not open (84%) | 9% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 153 | [ ] | Subnautica 2 (STEAM) | 25 | 31 | 81% (90d) | Does not open (65%) | 58% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 154 | [ ] | Singularity™ (GOG) | 25 | 30 | 83% (90d) | Does not open (100%) | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 155 | [ ] | Bionic Commando Rearmed (STEAM) | 25 | 28 | 89% (90d) | Does not open (74%) | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 156 | [ ] | Turing Complete (STEAM) | 25 | 28 | 89% (90d) | Does not open (91%) | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 157 | [ ] | Hitman: Blood Money (STEAM) | 25 | 26 | 96% (90d) | Does not open (82%) | 14% | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 158 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 25 | 26 | 96% (90d) | Does not open (95%) | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 159 | [ ] | Zuma Deluxe (STEAM) | 25 | 26 | 96% (90d) | Does not open (95%) | 33% | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 160 | [ ] | Resident Evil Requiem (STEAM) | 25 | 25 | 100% (90d) | Does not open (75%) | n/a | [#210](https://github.com/GameNative/gamenative-compat/issues/210) |
| 161 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 24 | 34 | 71% (90d) | No graphics (59%) | 11% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 162 | [ ] | ENDLESS Space™ 2 (STEAM) | 24 | 29 | 83% (90d) | Does not open (93%) | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 163 | [ ] | They Are Billions (STEAM) | 24 | 27 | 89% (90d) | Does not open (71%) | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 164 | [ ] | Call of Duty® (STEAM) | 23 | 32 | 72% (90d) | Does not open (67%) | 5% | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 165 | [ ] | Transformers: Fall of Cybertron (STEAM) | 23 | 30 | 77% (90d) | Does not open (63%) | 20% | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 166 | [ ] | Dragon Age™ Inquisition (STEAM) | 23 | 27 | 85% (90d) | Does not open (75%) | n/a | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 167 | [ ] | Half-Life: Blue Shift (STEAM) | 23 | 27 | 85% (90d) | Does not open (85%) | 25% | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 168 | [ ] | SimCity 4 Deluxe (STEAM) | 23 | 27 | 85% (90d) | Does not open (82%) | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 169 | [ ] | The Swapper (STEAM) | 23 | 27 | 85% (90d) | Does not open (50%) | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 170 | [ ] | Alien Breed: Impact (STEAM) | 23 | 24 | 96% (90d) | Does not open (91%) | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 171 | [ ] | PRAGMATA (STEAM) | 23 | 24 | 96% (90d) | Does not open (79%) | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 172 | [ ] | Euro Truck Simulator (STEAM) | 23 | 23 | 100% (90d) | Does not open (93%) | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 173 | [ ] | Gears 5 (STEAM) | 23 | 23 | 100% (90d) | Does not open (88%) | n/a | [#264](https://github.com/GameNative/gamenative-compat/issues/264) |
| 174 | [ ] | Marie's Adventure (STEAM) | 23 | 23 | 100% (90d) | Does not open (100%) | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 175 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 23 | 23 | 100% (90d) | Does not open (53%) | n/a | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 176 | [ ] | Spiral Knights (STEAM) | 23 | 23 | 100% (90d) | Does not open (72%) | n/a | [#263](https://github.com/GameNative/gamenative-compat/issues/263) |
| 177 | [ ] | SOMA (STEAM) | 22 | 30 | 73% (90d) | Does not open (79%) | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 178 | [ ] | TEKKEN 8 (STEAM) | 22 | 29 | 76% (90d) | Does not open (76%) | 50% | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 179 | [ ] | My Singing Monsters (STEAM) | 22 | 28 | 79% (90d) | Does not open (82%) | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 180 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 22 | 25 | 88% (90d) | Does not open (100%) | 43% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 181 | [ ] | skate.™ (EPIC) | 22 | 25 | 88% (90d) | Does not open (88%) | 7% | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 182 | [ ] | Peggle Nights (STEAM) | 22 | 24 | 92% (90d) | Does not open (94%) | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 183 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 22 | 23 | 96% (90d) | Does not open (50%) | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 184 | [ ] | WRC 7 (STEAM) | 22 | 23 | 96% (90d) | Does not open (67%) | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 185 | [ ] | Wallachia: Reign of Dracula (STEAM) | 22 | 23 | 96% (90d) | No graphics (95%) | n/a | [#475](https://github.com/GameNative/gamenative-compat/issues/475) |
| 186 | [ ] | Aggelos 2 (STEAM) | 21 | 27 | 78% (90d) | No graphics (90%) | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 187 | [ ] | Beyond Good & Evil™ (GOG) | 21 | 26 | 81% (90d) | Does not open (100%) | 20% | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 188 | [ ] | Sapphire Safari (GOG) | 21 | 26 | 81% (90d) | Does not open (89%) | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 189 | [ ] | Marvel's Midnight Suns (STEAM) | 21 | 24 | 88% (90d) | Does not open (84%) | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 190 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 21 | 23 | 91% (90d) | Does not open (65%) | 54% | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 191 | [ ] | Wuthering Waves (STEAM) | 21 | 23 | 91% (90d) | Does not open (85%) | n/a | [#216](https://github.com/GameNative/gamenative-compat/issues/216) |
| 192 | [ ] | Mirror's Edge™ Catalyst (STEAM) | 21 | 22 | 95% (90d) | Does not open (68%) | 36% | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 193 | [ ] | Resident Evil 3 Nemesis (1999) (STEAM) | 21 | 21 | 100% (90d) | Does not open (86%) | n/a | [#273](https://github.com/GameNative/gamenative-compat/issues/273) |
| 194 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 21 | 21 | 100% (90d) | Does not open (71%) | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 195 | [ ] | Fishing Planet (STEAM) | 20 | 28 | 71% (90d) | Does not open (93%) | 36% | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 196 | [ ] | Surviving Mars (STEAM) | 20 | 26 | 77% (90d) | Does not open (92%) | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 197 | [ ] | Halo: Spartan Assault (STEAM) | 20 | 23 | 87% (90d) | Does not open (82%) | 31% | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 198 | [ ] | Apex Legends (STEAM) | 20 | 22 | 91% (90d) | Does not open (72%) | n/a | [#261](https://github.com/GameNative/gamenative-compat/issues/261) |
| 199 | [ ] | Pathway (EPIC) | 20 | 21 | 95% (90d) | Does not open (61%) | n/a | [#298](https://github.com/GameNative/gamenative-compat/issues/298) |
| 200 | [ ] | Grounded 2 (STEAM) | 20 | 20 | 100% (90d) | Does not open (56%) | n/a | [#317](https://github.com/GameNative/gamenative-compat/issues/317) |
| 201 | [ ] | Beat Cop (STEAM) | 19 | 27 | 70% (90d) | Does not open (72%) | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 202 | [ ] | Dungeon Keeper™ 2 (GOG) | 19 | 26 | 73% (90d) | Does not open (100%) | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 203 | [ ] | Mafia III: Definitive Edition (STEAM) | 19 | 22 | 86% (90d) | Does not open (95%) | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 204 | [ ] | PICO PARK:Classic Edition (STEAM) | 19 | 22 | 86% (90d) | Does not open (89%) | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 205 | [ ] | The Elder Scrolls IV: Oblivion Remastered (STEAM) | 19 | 22 | 86% (90d) | Does not open (59%) | n/a | [#312](https://github.com/GameNative/gamenative-compat/issues/312) |
| 206 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 19 | 22 | 86% (90d) | Does not open (79%) | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 207 | [ ] | Assassin's Creed Brotherhood (STEAM) | 19 | 21 | 90% (90d) | Does not open (82%) | 0% | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 208 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 19 | 21 | 90% (90d) | Does not open (89%) | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 209 | [ ] | Bingle Bingle (STEAM) | 19 | 20 | 95% (90d) | Does not open (80%) | n/a | [#225](https://github.com/GameNative/gamenative-compat/issues/225) |
| 210 | [ ] | GT Legends (STEAM) | 19 | 20 | 95% (90d) | Does not open (89%) | n/a | [#364](https://github.com/GameNative/gamenative-compat/issues/364) |
| 211 | [ ] | Melatonin (STEAM) | 19 | 20 | 95% (90d) | Does not open (59%) | 30% | [#272](https://github.com/GameNative/gamenative-compat/issues/272) |
| 212 | [ ] | No More Room in Hell (STEAM) | 19 | 20 | 95% (90d) | Does not open (94%) | n/a | [#365](https://github.com/GameNative/gamenative-compat/issues/365) |
| 213 | [ ] | Zenless Zone Zero (STEAM) | 19 | 20 | 95% (90d) | Does not open (76%) | n/a | [#369](https://github.com/GameNative/gamenative-compat/issues/369) |
| 214 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 18 | 23 | 78% (90d) | Does not open (100%) | 37% | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 215 | [ ] | Yakuza 0 (GOG) | 18 | 23 | 78% (90d) | Does not open (67%) | 46% | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 216 | [ ] | SaGa Frontier 2 Remastered (STEAM) | 18 | 22 | 82% (90d) | Controller issues (100%) | n/a | [#482](https://github.com/GameNative/gamenative-compat/issues/482) |
| 217 | [ ] | Lay of the Land (STEAM) | 18 | 20 | 90% (90d) | No graphics (61%) | n/a | [#477](https://github.com/GameNative/gamenative-compat/issues/477) |
| 218 | [ ] | Carnal Instinct (STEAM) | 17 | 24 | 71% (90d) | Does not open (57%) | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 219 | [ ] | SlashZero Demo (STEAM) | 17 | 23 | 74% (90d) | Does not open (75%) | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 220 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 17 | 22 | 77% (90d) | Does not open (87%) | 54% | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 221 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (90d) | No graphics (88%) | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 222 | [ ] | Clive Barker's Undying (GOG) | 17 | 20 | 85% (90d) | Does not open (75%) | n/a | [#388](https://github.com/GameNative/gamenative-compat/issues/388) |
| 223 | [ ] | GRADIUS origin collection (STEAM) | 17 | 20 | 85% (90d) | Controller issues (71%) | n/a | [#479](https://github.com/GameNative/gamenative-compat/issues/479) |
| 224 | [ ] | NBA 2K26 (STEAM) | 17 | 20 | 85% (90d) | Does not open (82%) | n/a | [#384](https://github.com/GameNative/gamenative-compat/issues/384) |
| 225 | [ ] | We Were Here Together (EPIC) | 17 | 20 | 85% (90d) | Does not open (81%) | n/a | [#374](https://github.com/GameNative/gamenative-compat/issues/374) |
| 226 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 16 | 23 | 70% (90d) | No graphics (56%) | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 227 | [ ] | Re-Volt (STEAM) | 16 | 22 | 73% (90d) | Controller issues (71%) | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 228 | [ ] | Spark the Electric Jester (STEAM) | 16 | 22 | 73% (90d) | Does not open (62%) | 52% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 229 | [ ] | Darksiders Warmastered Edition (EPIC) | 16 | 21 | 76% (90d) | Does not open (82%) | 52% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 230 | [ ] | Hitman 2: Silent Assassin (STEAM) | 16 | 21 | 76% (90d) | Does not open (82%) | 44% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 231 | [ ] | Bejeweled 2 Deluxe (STEAM) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#329](https://github.com/GameNative/gamenative-compat/issues/329) |
| 232 | [ ] | Blood Bowl 2 (STEAM) | 16 | 20 | 80% (90d) | Does not open (64%) | n/a | [#258](https://github.com/GameNative/gamenative-compat/issues/258) |
| 233 | [ ] | F.E.A.R. 2: Project Origin + Reborn (GOG) | 16 | 20 | 80% (90d) | Does not open (100%) | n/a | [#478](https://github.com/GameNative/gamenative-compat/issues/478) |
| 234 | [ ] | Genshin Impact (EPIC) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#326](https://github.com/GameNative/gamenative-compat/issues/326) |
| 235 | [ ] | Sacred Gold (STEAM) | 16 | 20 | 80% (90d) | Does not open (92%) | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 236 | [ ] | DayZ (STEAM) | 15 | 21 | 71% (90d) | Does not open (56%) | 54% | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 237 | [ ] | Fallout Classic (GOG) | 15 | 21 | 71% (90d) | Does not open (71%) | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 238 | [ ] | Smushi Come Home (GOG) | 15 | 21 | 71% (90d) | Does not open (57%) | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 239 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 15 | 21 | 71% (90d) | Does not open (70%) | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 240 | [ ] | Content Warning (STEAM) | 15 | 20 | 75% (90d) | Does not open (50%) | n/a | [#241](https://github.com/GameNative/gamenative-compat/issues/241) |
| 241 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 15 | 20 | 75% (90d) | No graphics (71%) | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 242 | [ ] | Make Way (EPIC) | 15 | 20 | 75% (90d) | Does not open (79%) | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |

## Probably does not work (84)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | Grim Dawn (STEAM) | 555 | 612 | 63% (1.3.0) | Does not open (74%) | 59% |  |
| 2 | [ ] | Garry's Mod (STEAM) | 196 | 310 | 68% (1.3.0) | Does not open (79%) | 58% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 3 | [ ] | Metro 2033 Redux (STEAM) | 158 | 342 | 69% (1.3.0) | Does not open (70%) | 49% |  |
| 4 | [ ] | Prototype (STEAM) | 149 | 211 | 52% (1.3.0) | Does not open (76%) | 46% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 5 | [ ] | Geometry Dash (STEAM) | 141 | 423 | 64% (1.3.0) | Does not open (71%) | 38% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 6 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 132 | 167 | 56% (1.3.0) | Does not open (92%) | 39% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 7 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 97 | 144 | 67% (90d) | Does not open (78%) | n/a |  |
| 8 | [ ] | VRChat (STEAM) | 92 | 141 | 52% (1.3.0) | Does not open (66%) | 40% |  |
| 9 | [ ] | Gorilla Tag (STEAM) | 72 | 121 | 68% (1.3.0) | Does not open (70%) | 22% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 10 | [ ] | Firewatch (STEAM) | 64 | 113 | 57% (90d) | Does not open (90%) | 51% |  |
| 11 | [ ] | Hollow Knight: Silksong (GOG) | 61 | 99 | 62% (90d) | Does not open (75%) | 51% |  |
| 12 | [ ] | Oxygen Not Included (STEAM) | 53 | 86 | 62% (90d) | Does not open (76%) | 51% |  |
| 13 | [ ] | Breathedge (STEAM) | 50 | 74 | 68% (90d) | Does not open (60%) | 42% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 14 | [ ] | VALORANT (EPIC) | 44 | 67 | 66% (90d) | Does not open (86%) | 21% |  |
| 15 | [ ] | Frostpunk (STEAM) | 41 | 65 | 63% (90d) | No graphics (77%) | 49% |  |
| 16 | [ ] | Fallout (GOG) | 40 | 61 | 66% (90d) | Does not open (72%) | 48% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 17 | [ ] | State of Decay 2 (STEAM) | 39 | 57 | 68% (90d) | Does not open (91%) | 0% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 18 | [ ] | Grim Dawn (GOG) | 38 | 62 | 61% (90d) | Does not open (65%) | 50% | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 19 | [ ] | Age of Empires II (2013) (STEAM) | 37 | 64 | 58% (90d) | Does not open (48%) | 58% |  |
| 20 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 37 | 62 | 60% (90d) | Does not open (96%) | 45% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 21 | [ ] | XCOM 2 (STEAM) | 35 | 54 | 65% (90d) | Does not open (57%) | n/a |  |
| 22 | [ ] | Deponia (STEAM) | 34 | 62 | 55% (90d) | Does not open (46%) | 59% |  |
| 23 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 31 | 56 | 55% (90d) | Does not open (66%) | 47% |  |
| 24 | [ ] | Yume Nikki (STEAM) | 31 | 54 | 67% (14d) | Does not open (90%) | 0% | [#468](https://github.com/GameNative/gamenative-compat/issues/468) |
| 25 | [ ] | Sol Cesto (STEAM) | 31 | 49 | 63% (90d) | Does not open (68%) | 53% |  |
| 26 | [ ] | Mafia II (Classic) (GOG) | 31 | 45 | 69% (90d) | Does not open (96%) | 19% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 27 | [ ] | Soul's Remnant (STEAM) | 27 | 49 | 55% (90d) | Does not open (55%) | n/a |  |
| 28 | [ ] | Counter-Strike: Condition Zero (STEAM) | 25 | 43 | 58% (90d) | Does not open (53%) | 59% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 29 | [ ] | Crazy Taxi (STEAM) | 25 | 43 | 58% (90d) | Does not open (63%) | 57% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 30 | [ ] | Chained Echoes (GOG) | 24 | 48 | 50% (90d) | Does not open (62%) | 55% |  |
| 31 | [ ] | Baldur's Gate: Enhanced Edition (STEAM) | 24 | 46 | 52% (90d) | Does not open (61%) | 22% |  |
| 32 | [ ] | Strider (STEAM) | 23 | 36 | 64% (90d) | Does not open (100%) | 38% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 33 | [ ] | Invisible, Inc. (STEAM) | 22 | 38 | 58% (90d) | Does not open (65%) | 58% |  |
| 34 | [ ] | Cities: Skylines (STEAM) | 22 | 33 | 67% (90d) | Does not open (67%) | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 35 | [ ] | Overlord (STEAM) | 21 | 41 | 51% (90d) | Does not open (71%) | 59% |  |
| 36 | [ ] | GOD EATER RESURRECTION (STEAM) | 21 | 32 | 66% (90d) | Does not open (53%) | 59% |  |
| 37 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 20 | 33 | 61% (90d) | Does not open (56%) | 48% |  |
| 38 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 20 | 32 | 63% (90d) | Does not open (81%) | n/a |  |
| 39 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 19 | 29 | 66% (90d) | Does not open (94%) | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 40 | [ ] | Warhammer 40,000: Boltgun (GOG) | 19 | 29 | 66% (90d) | Does not open (92%) | 53% |  |
| 41 | [ ] | Turnip Boy Robs a Bank (EPIC) | 19 | 28 | 68% (90d) | Does not open (65%) | 47% | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 42 | [ ] | Need for Speed: Undercover (STEAM) | 18 | 29 | 62% (90d) | Does not open (93%) | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 43 | [ ] | Another World: 20th Anniversary Edition (GOG) | 18 | 28 | 64% (90d) | Does not open (67%) | 45% |  |
| 44 | [ ] | Formula Legends (STEAM) | 18 | 28 | 64% (90d) | No graphics (60%) | 53% |  |
| 45 | [ ] | CULTIC (STEAM) | 17 | 33 | 52% (90d) | Does not open (92%) | 55% |  |
| 46 | [ ] | No More Heroes (STEAM) | 17 | 33 | 52% (90d) | No graphics (71%) | 50% |  |
| 47 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 17 | 27 | 63% (90d) | Does not open (80%) | n/a |  |
| 48 | [ ] | Assassin's Creed Odyssey (STEAM) | 17 | 26 | 65% (90d) | Does not open (77%) | n/a | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 49 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 16 | 29 | 55% (90d) | Does not open (87%) | 31% |  |
| 50 | [ ] | Guacamelee! Gold Edition (STEAM) | 16 | 27 | 59% (90d) | Does not open (93%) | n/a | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 51 | [ ] | Gargoyles Remastered (AMAZON) | 16 | 26 | 62% (90d) | Directx error (57%) | n/a |  |
| 52 | [ ] | War of Dots (STEAM) | 16 | 25 | 64% (90d) | Does not open (75%) | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 53 | [ ] | Race The Sun (STEAM) | 15 | 30 | 50% (90d) | No graphics (92%) | 50% |  |
| 54 | [ ] | Spooky's Jump Scare Mansion (STEAM) | 15 | 29 | 52% (90d) | Does not open (64%) | 0% |  |
| 55 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 15 | 27 | 56% (90d) | Does not open (85%) | 51% |  |
| 56 | [ ] | Ys: Memories of Celceta (STEAM) | 15 | 24 | 63% (90d) | No graphics (45%) | 31% |  |
| 57 | [ ] | Fogpiercer (STEAM) | 15 | 22 | 68% (90d) | Does not open (73%) | n/a | [#303](https://github.com/GameNative/gamenative-compat/issues/303) |
| 58 | [ ] | Evoland (STEAM) | 14 | 28 | 50% (90d) | Controller issues (69%) | n/a |  |
| 59 | [ ] | Odallus: The Dark Call (STEAM) | 14 | 26 | 54% (90d) | No graphics (54%) | n/a | [#337](https://github.com/GameNative/gamenative-compat/issues/337) |
| 60 | [ ] | Blaster Master Zero (STEAM) | 14 | 25 | 56% (90d) | Does not open (64%) | 33% |  |
| 61 | [ ] | Katana ZERO (GOG) | 14 | 25 | 56% (90d) | Does not open (85%) | 36% |  |
| 62 | [ ] | Evenicle (STEAM) | 14 | 23 | 61% (90d) | Graphics glitches (71%) | n/a |  |
| 63 | [ ] | Dex (GOG) | 14 | 22 | 64% (90d) | Does not open (83%) | n/a |  |
| 64 | [ ] | Songs of Conquest (EPIC) | 14 | 22 | 64% (90d) | Does not open (75%) | n/a |  |
| 65 | [ ] | Blood Omen: Legacy of Kain (GOG) | 14 | 21 | 67% (90d) | Does not open (62%) | 41% |  |
| 66 | [ ] | Revolution Idle (STEAM) | 13 | 26 | 50% (90d) | Does not open (43%) | n/a |  |
| 67 | [ ] | Alan Wake's American Nightmare (EPIC) | 13 | 25 | 52% (90d) | Does not open (92%) | 59% |  |
| 68 | [ ] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 13 | 24 | 54% (90d) | Does not open (100%) | 16% |  |
| 69 | [ ] | Trials Survivors (STEAM) | 13 | 24 | 54% (90d) | Does not open (67%) | n/a |  |
| 70 | [ ] | Asterigos: Curse of the Stars (STEAM) | 13 | 23 | 57% (90d) | Graphics glitches (50%) | n/a |  |
| 71 | [ ] | Look Outside (GOG) | 13 | 23 | 57% (90d) | Does not open (100%) | n/a |  |
| 72 | [ ] | Human Resource Machine (EPIC) | 13 | 22 | 59% (90d) | No graphics (70%) | 50% |  |
| 73 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 22 | 59% (90d) | Does not open (80%) | n/a |  |
| 74 | [ ] | Drop Duchy (EPIC) | 13 | 21 | 62% (90d) | Does not open (100%) | 8% |  |
| 75 | [ ] | Secret of Mana (STEAM) | 13 | 21 | 62% (90d) | Graphics glitches (58%) | n/a |  |
| 76 | [ ] | The Stanley Parable (STEAM) | 13 | 21 | 62% (90d) | Does not open (89%) | 50% |  |
| 77 | [ ] | Buck Up And Drive! (STEAM) | 13 | 20 | 65% (90d) | Does not open (67%) | n/a |  |
| 78 | [ ] | Five Nights at Freddy's 3 (STEAM) | 13 | 20 | 65% (90d) | No graphics (50%) | n/a |  |
| 79 | [ ] | A Plague Tale: Innocence (GOG) | 12 | 23 | 52% (90d) | Does not open (91%) | 43% |  |
| 80 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 12 | 21 | 57% (90d) | Does not open (73%) | n/a |  |
| 81 | [ ] | Audiosurf 2 (STEAM) | 12 | 20 | 60% (90d) | Does not open (80%) | n/a | [#405](https://github.com/GameNative/gamenative-compat/issues/405) |
| 82 | [ ] | Click the Button (STEAM) | 12 | 20 | 60% (90d) | Does not open (82%) | n/a |  |
| 83 | [ ] | Crying Suns (EPIC) | 11 | 22 | 50% (90d) | No graphics (57%) | n/a |  |
| 84 | [ ] | DYNASTY WARRIORS: ORIGINS (STEAM) | 10 | 20 | 50% (90d) | Does not open (60%) | n/a |  |

## Works, but the first launch usually fails (352)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 1298 | 1643 | 75% (1.3.0) | Does not open (83%) | 77% |  |
| 2 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 560 | 711 | 78% (1.3.0) | Does not open (64%) | 90% |  |
| 3 | [ ] | Terraria (STEAM) | 486 | 761 | 58% (1.3.0) | No graphics (51%) | 75% |  |
| 4 | [ ] | KINGDOM HEARTS -HD 1.5+2.5 ReMIX- (STEAM) | 476 | 956 | 53% (1.3.0) | Does not open (79%) | 95% |  |
| 5 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 369 | 549 | 68% (1.3.0) | Does not open (55%) | 83% |  |
| 6 | [ ] | No Man's Sky (STEAM) | 364 | 637 | 54% (1.3.0) | Controller issues (62%) | 84% |  |
| 7 | [ ] | Half-Life (STEAM) | 350 | 615 | 51% (1.3.0) | Does not open (57%) | 77% |  |
| 8 | [ ] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 249 | 291 | 86% (90d) | Does not open (87%) | 69% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 9 | [ ] | Cyberpunk 2077 (STEAM) | 239 | 423 | 51% (1.3.0) | Does not open (66%) | 77% |  |
| 10 | [ ] | Welcome to Elderfield (STEAM) | 236 | 283 | 59% (1.3.0) | Does not open (72%) | 74% |  |
| 11 | [ ] | Grand Theft Auto V Legacy (STEAM) | 231 | 294 | 69% (1.3.0) | Does not open (88%) | 80% |  |
| 12 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 226 | 318 | 71% (90d) | Does not open (61%) | 89% |  |
| 13 | [ ] | BeamNG.drive (STEAM) | 214 | 260 | 88% (1.3.0) | Does not open (82%) | 92% |  |
| 14 | [ ] | Palworld (STEAM) | 205 | 399 | 53% (1.3.0) | Does not open (71%) | 87% |  |
| 15 | [ ] | ELDEN RING (STEAM) | 203 | 300 | 70% (1.3.0) | Does not open (86%) | 71% |  |
| 16 | [ ] | OMORI (STEAM) | 202 | 244 | 83% (90d) | Does not open (65%) | 83% |  |
| 17 | [ ] | DRAGON BALL FighterZ (STEAM) | 202 | 235 | 69% (1.3.0) | Does not open (89%) | 65% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 18 | [ ] | Devil May Cry HD Collection (STEAM) | 201 | 280 | 76% (1.3.0) | Does not open (86%) | 77% |  |
| 19 | [ ] | MONSTER HUNTER RISE (STEAM) | 197 | 495 | 51% (1.3.0) | Does not open (81%) | 68% |  |
| 20 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 193 | 359 | 59% (1.3.0) | Does not open (57%) | 82% |  |
| 21 | [ ] | DREDGE (EPIC) | 172 | 219 | 63% (1.3.0) | Does not open (66%) | 86% |  |
| 22 | [x] 2026-10-18 | Sid Meier's Civilization V (STEAM) | 172 | 184 | 93% (90d) | Does not open (75%) | 60% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 23 | [ ] | Rocket League® (EPIC) | 159 | 263 | 54% (1.3.0) | Does not open (75%) | 74% |  |
| 24 | [ ] | Resident Evil 2 (STEAM) | 158 | 324 | 50% (1.3.0) | Does not open (72%) | 81% |  |
| 25 | [ ] | Noita (STEAM) | 147 | 223 | 55% (1.3.0) | Does not open (54%) | 75% |  |
| 26 | [ ] | Monster Hunter: World (STEAM) | 144 | 273 | 55% (1.3.0) | No graphics (55%) | 82% |  |
| 27 | [ ] | Borderlands 2 (EPIC) | 142 | 168 | 81% (1.3.0) | Does not open (82%) | 61% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 28 | [ ] | Team Fortress 2 (STEAM) | 134 | 228 | 63% (1.3.0) | Does not open (68%) | 80% |  |
| 29 | [ ] | Castlevania Advance Collection (STEAM) | 133 | 205 | 69% (1.3.0) | Controller issues (95%) | 96% |  |
| 30 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 130 | 149 | 90% (1.3.0) | Does not open (85%) | 77% |  |
| 31 | [ ] | Minecraft Dungeons II (STEAM) | 126 | 144 | 88% (90d) | Does not open (82%) | 67% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 32 | [ ] | Far Cry® 3 (STEAM) | 126 | 140 | 90% (90d) | Does not open (83%) | 68% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 33 | [ ] | Castlevania Dominus Collection (STEAM) | 122 | 179 | 77% (1.3.0) | Controller issues (92%) | 98% |  |
| 34 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 122 | 170 | 79% (1.3.0) | Does not open (76%) | 65% |  |
| 35 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 120 | 153 | 66% (1.3.0) | Does not open (71%) | 65% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 36 | [ ] | Devil May Cry 5 (STEAM) | 118 | 182 | 68% (1.3.0) | Does not open (82%) | 68% |  |
| 37 | [ ] | Touhou Koumakyou: New Classic - the Embodiment of Scarlet Devil (STEAM) | 117 | 181 | 65% (90d) | Does not open (78%) | 81% |  |
| 38 | [ ] | Fallout: New Vegas (EPIC) | 117 | 143 | 75% (1.3.0) | Does not open (57%) | 91% |  |
| 39 | [ ] | Cave Story+ (STEAM) | 117 | 129 | 91% (90d) | Does not open (64%) | 95% |  |
| 40 | [ ] | The Witcher: Enhanced Edition (STEAM) | 112 | 129 | 87% (90d) | Does not open (60%) | 63% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 41 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 107 | 159 | 62% (1.3.0) | Does not open (74%) | 76% |  |
| 42 | [ ] | Aniimo (STEAM) | 106 | 144 | 75% (1.3.0) | Does not open (76%) | 92% |  |
| 43 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 106 | 141 | 75% (90d) | Does not open (85%) | 86% |  |
| 44 | [ ] | Moonstone Island (STEAM) | 102 | 135 | 76% (90d) | Controller issues (58%) | 87% |  |
| 45 | [ ] | Happy Wheels (STEAM) | 96 | 116 | 83% (90d) | No graphics (53%) | 79% |  |
| 46 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 92 | 119 | 77% (90d) | Controller issues (85%) | 97% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 47 | [ ] | Fallout: New Vegas PCR (STEAM) | 88 | 117 | 75% (90d) | Does not open (93%) | 69% |  |
| 48 | [ ] | Vital Shell (STEAM) | 86 | 130 | 66% (90d) | Does not open (51%) | 83% |  |
| 49 | [ ] | STEINS;GATE (STEAM) | 85 | 118 | 72% (90d) | Does not open (91%) | 91% |  |
| 50 | [ ] | Hogwarts Legacy (STEAM) | 84 | 145 | 52% (1.3.0) | Does not open (59%) | 65% |  |
| 51 | [ ] | Sovereign Tower (STEAM) | 83 | 136 | 61% (90d) | Does not open (83%) | 84% |  |
| 52 | [ ] | Cry of Fear (STEAM) | 82 | 162 | 72% (1.3.0) | Does not open (51%) | 81% |  |
| 53 | [ ] | The Sims™ 4 (STEAM) | 75 | 94 | 80% (90d) | Does not open (88%) | 67% |  |
| 54 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 73 | 123 | 59% (90d) | Controller issues (59%) | 93% |  |
| 55 | [ ] | Sol Cesto (EPIC) | 73 | 77 | 95% (90d) | Does not open (78%) | 73% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 56 | [ ] | Sid Meier's Civilization VI (STEAM) | 72 | 122 | 56% (1.3.0) | Does not open (70%) | 91% |  |
| 57 | [ ] | Ballionaire (STEAM) | 72 | 111 | 50% (1.3.0) | Does not open (77%) | 93% |  |
| 58 | [ ] | Antivirus Survivors 2003 Professional (STEAM) | 72 | 106 | 68% (90d) | Does not open (60%) | 95% |  |
| 59 | [ ] | Darksiders (STEAM) | 71 | 86 | 83% (90d) | Does not open (68%) | 88% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 60 | [ ] | Disgaea 5 Complete (STEAM) | 70 | 84 | 83% (90d) | Does not open (75%) | 98% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 61 | [ ] | Alabaster Dawn (STEAM) | 69 | 125 | 55% (90d) | Controller issues (51%) | 90% |  |
| 62 | [ ] | American Truck Simulator (STEAM) | 68 | 111 | 72% (1.3.0) | Does not open (74%) | 81% |  |
| 63 | [ ] | Dota 2 (STEAM) | 68 | 104 | 59% (1.3.0) | Does not open (80%) | 69% |  |
| 64 | [ ] | Dungeons & Degenerate Gamblers (STEAM) | 68 | 95 | 50% (1.3.0) | Does not open (90%) | 100% |  |
| 65 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 67 | 123 | 54% (1.3.0) | Does not open (67%) | 63% |  |
| 66 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 67 | 105 | 64% (90d) | Does not open (72%) | 74% |  |
| 67 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 67 | 78 | 95% (1.3.0) | Does not open (88%) | 96% |  |
| 68 | [ ] | Fallout (STEAM) | 66 | 103 | 64% (90d) | Does not open (72%) | 73% |  |
| 69 | [ ] | Mega Man Zero/ZX Legacy Collection (STEAM) | 66 | 95 | 69% (90d) | Does not open (83%) | 80% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 70 | [ ] | Call of Juarez Gunslinger (STEAM) | 66 | 81 | 81% (90d) | Does not open (90%) | 75% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 71 | [ ] | Cyberpunk 2077 (GOG) | 65 | 81 | 80% (90d) | Does not open (76%) | 77% |  |
| 72 | [ ] | Gunfire Reborn (STEAM) | 65 | 71 | 92% (90d) | Does not open (80%) | 93% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 73 | [ ] | MIO: Memories in Orbit (STEAM) | 64 | 119 | 66% (1.3.0) | Graphics glitches (53%) | 95% |  |
| 74 | [ ] | Fable - The Lost Chapters (STEAM) | 64 | 102 | 52% (1.3.0) | Graphics glitches (54%) | 79% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 75 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 63 | 85 | 74% (90d) | Does not open (46%) | 63% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 76 | [ ] | Borderlands: The Pre-Sequel (STEAM) | 62 | 89 | 70% (90d) | Does not open (78%) | 68% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 77 | [ ] | Red Dead Redemption 2 (STEAM) | 62 | 82 | 63% (1.3.0) | Does not open (98%) | 82% |  |
| 78 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 61 | 85 | 58% (1.3.0) | Does not open (48%) | 88% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 79 | [ ] | A Plague Tale: Innocence (STEAM) | 60 | 63 | 95% (90d) | Does not open (88%) | 78% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 80 | [ ] | The Binding of Isaac (STEAM) | 59 | 133 | 65% (1.3.0) | Controller issues (91%) | 93% |  |
| 81 | [ ] | Poppy Playtime (STEAM) | 59 | 107 | 50% (1.3.0) | Does not open (65%) | 80% |  |
| 82 | [ ] | Borderlands 3 (STEAM) | 58 | 78 | 74% (90d) | Does not open (91%) | 93% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 83 | [ ] | Mini Motorways (STEAM) | 57 | 99 | 58% (90d) | Does not open (76%) | 63% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 84 | [ ] | Starbound (STEAM) | 57 | 88 | 52% (1.3.0) | Does not open (68%) | 73% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 85 | [ ] | Call of Duty: World at War (STEAM) | 57 | 81 | 70% (90d) | Does not open (43%) | 75% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 86 | [ ] | Deskrawl: Idle ARPG (STEAM) | 57 | 68 | 86% (1.3.0) | Does not open (60%) | 78% |  |
| 87 | [ ] | Sonic Generations (STEAM) | 57 | 66 | 86% (90d) | Does not open (67%) | 64% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 88 | [ ] | eFootball™ (STEAM) | 56 | 84 | 67% (90d) | Does not open (54%) | 79% |  |
| 89 | [ ] | Prey (STEAM) | 55 | 91 | 60% (90d) | Does not open (63%) | 82% |  |
| 90 | [ ] | The Secret of Monkey Island: Special Edition (STEAM) | 55 | 86 | 64% (90d) | Does not open (92%) | 74% |  |
| 91 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 55 | 59 | 93% (90d) | Does not open (83%) | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 92 | [ ] | Resident Evil 6 (STEAM) | 54 | 128 | 71% (1.3.0) | Does not open (57%) | 90% |  |
| 93 | [ ] | TBH: Task Bar Hero (STEAM) | 54 | 87 | 62% (90d) | Does not open (74%) | 92% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 94 | [ ] | Big Walk (STEAM) | 54 | 86 | 63% (90d) | Does not open (67%) | 84% |  |
| 95 | [ ] | Vampire Survivors (EPIC) | 54 | 76 | 71% (90d) | Does not open (60%) | 64% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 96 | [ ] | Grand Theft Auto V (EPIC) | 54 | 60 | 95% (1.3.0) | Does not open (91%) | 83% |  |
| 97 | [ ] | MapleStory (STEAM) | 54 | 56 | 92% (1.3.0) | Does not open (76%) | 74% |  |
| 98 | [ ] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 53 | 89 | 60% (90d) | Does not open (62%) | 65% |  |
| 99 | [ ] | Sonic Adventure DX (STEAM) | 53 | 88 | 60% (90d) | Does not open (87%) | 61% |  |
| 100 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 53 | 77 | 77% (1.3.0) | Does not open (61%) | 66% |  |
| 101 | [ ] | Path of Exile (STEAM) | 52 | 61 | 85% (90d) | Does not open (91%) | 80% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 102 | [ ] | 7 Days to Die (STEAM) | 51 | 109 | 57% (1.3.0) | Does not open (74%) | 68% |  |
| 103 | [ ] | Until Then (STEAM) | 51 | 90 | 57% (90d) | Does not open (77%) | 96% |  |
| 104 | [ ] | A Plague Tale: Innocence (EPIC) | 51 | 87 | 59% (90d) | Does not open (71%) | 89% |  |
| 105 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 51 | 59 | 86% (90d) | Does not open (80%) | 86% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 106 | [ ] | Marvel’s Spider-Man Remastered (STEAM) | 50 | 121 | 56% (1.3.0) | Does not open (48%) | 62% |  |
| 107 | [ ] | Darkest Dungeon® (EPIC) | 49 | 88 | 57% (1.3.0) | Does not open (64%) | 61% |  |
| 108 | [ ] | Ace Attorney Investigations Collection (STEAM) | 49 | 79 | 62% (90d) | Does not open (96%) | 93% |  |
| 109 | [ ] | Last Epoch (STEAM) | 49 | 72 | 72% (1.3.0) | Does not open (80%) | 100% |  |
| 110 | [ ] | Guildrun Demo (STEAM) | 49 | 69 | 71% (90d) | No graphics (66%) | 75% |  |
| 111 | [ ] | Dead Space (STEAM) | 49 | 62 | 79% (90d) | Does not open (54%) | 78% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 112 | [ ] | Sheepy: A Short Adventure (STEAM) | 49 | 59 | 83% (90d) | Does not open (52%) | 82% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 113 | [ ] | The Bazaar (STEAM) | 48 | 80 | 60% (90d) | Does not open (74%) | 79% |  |
| 114 | [ ] | Sleeping Dogs™ (STEAM) | 48 | 55 | 87% (90d) | Does not open (87%) | 77% | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 115 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 75 | 63% (90d) | Controller issues (51%) | 96% |  |
| 116 | [ ] | Resident Evil 7 Biohazard (STEAM) | 47 | 75 | 69% (1.3.0) | Does not open (74%) | 83% |  |
| 117 | [ ] | Watch_Dogs 2 (STEAM) | 47 | 52 | 90% (90d) | Does not open (97%) | 60% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 118 | [ ] | Deadlock (STEAM) | 46 | 67 | 70% (1.3.0) | Does not open (44%) | 93% |  |
| 119 | [ ] | Rivals of Aether II (STEAM) | 46 | 65 | 71% (90d) | Does not open (54%) | 82% |  |
| 120 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 45 | 77 | 58% (90d) | Controller issues (54%) | 89% |  |
| 121 | [ ] | Plague Inc: Evolved (STEAM) | 44 | 66 | 67% (90d) | Does not open (67%) | 60% |  |
| 122 | [ ] | Tomb Raider: Anniversary (STEAM) | 44 | 65 | 68% (90d) | Does not open (95%) | 64% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 123 | [ ] | Sonic Lost World (STEAM) | 44 | 61 | 72% (90d) | No graphics (63%) | 84% |  |
| 124 | [ ] | Aggelos (STEAM) | 44 | 58 | 76% (90d) | No graphics (78%) | 94% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 125 | [ ] | Moonlighter (EPIC) | 44 | 48 | 100% (1.3.0) | No graphics (77%) | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 126 | [ ] | Digimon World: Next Order (STEAM) | 43 | 83 | 52% (90d) | Controller issues (85%) | 95% |  |
| 127 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 43 | 46 | 93% (90d) | Does not open (95%) | 64% | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 128 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 42 | 77 | 71% (1.3.0) | Controller issues (47%) | 88% |  |
| 129 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 42 | 63 | 67% (90d) | Does not open (73%) | 70% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 130 | [ ] | FINAL FANTASY VII (2013) (STEAM) | 42 | 60 | 70% (90d) | Does not open (83%) | 81% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 131 | [ ] | Dead by Daylight (STEAM) | 42 | 46 | 91% (90d) | Does not open (81%) | 81% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 132 | [ ] | Street Fighter™ 6 (STEAM) | 41 | 67 | 61% (90d) | Does not open (86%) | 86% |  |
| 133 | [ ] | Amnesia: The Dark Descent (STEAM) | 40 | 75 | 53% (90d) | Does not open (84%) | 76% |  |
| 134 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 40 | 41 | 98% (90d) | Does not open (62%) | 83% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 135 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 39 | 74 | 53% (90d) | No graphics (83%) | 98% |  |
| 136 | [ ] | Sonic Origins (STEAM) | 39 | 70 | 56% (90d) | Does not open (71%) | 87% |  |
| 137 | [ ] | Capcom Arcade Stadium (STEAM) | 39 | 48 | 81% (90d) | Does not open (84%) | 83% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 138 | [ ] | CrossCode (GOG) | 38 | 42 | 90% (90d) | Does not open (78%) | 73% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 139 | [ ] | Monster Hunter Wilds (STEAM) | 38 | 39 | 97% (90d) | Does not open (61%) | 83% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 140 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 69 | 54% (90d) | Does not open (68%) | 89% |  |
| 141 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 37 | 64 | 58% (90d) | Does not open (61%) | 78% |  |
| 142 | [ ] | Forza Horizon 4 (STEAM) | 37 | 53 | 70% (90d) | Does not open (45%) | 85% |  |
| 143 | [ ] | Elite Dangerous (STEAM) | 37 | 40 | 93% (90d) | Does not open (76%) | 69% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 144 | [ ] | Fallout 3 (STEAM) | 36 | 72 | 50% (1.3.0) | Does not open (47%) | 96% |  |
| 145 | [ ] | Supermarket Together (STEAM) | 36 | 50 | 72% (90d) | Does not open (75%) | 70% |  |
| 146 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 35 | 42 | 83% (90d) | No graphics (69%) | 82% | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 147 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 35 | 40 | 88% (90d) | Does not open (69%) | 60% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 148 | [ ] | Street Fighter 30th Anniversary Collection (STEAM) | 34 | 67 | 51% (90d) | Does not open (97%) | 66% |  |
| 149 | [ ] | SurrounDead (STEAM) | 34 | 66 | 52% (90d) | Controller issues (63%) | 96% |  |
| 150 | [ ] | Hearts of Iron IV (STEAM) | 34 | 61 | 56% (90d) | Does not open (72%) | 66% |  |
| 151 | [ ] | SnowRunner (STEAM) | 34 | 48 | 71% (90d) | Does not open (96%) | 92% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 152 | [ ] | Hero Siege (STEAM) | 33 | 56 | 59% (90d) | Graphics glitches (52%) | 62% |  |
| 153 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 33 | 53 | 62% (90d) | Controller issues (64%) | 74% |  |
| 154 | [ ] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 53 | 62% (90d) | Controller issues (84%) | 80% |  |
| 155 | [ ] | Palia (STEAM) | 33 | 45 | 73% (90d) | Does not open (65%) | 77% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 156 | [ ] | Romestead (STEAM) | 33 | 44 | 75% (90d) | Does not open (67%) | 77% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 157 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 33 | 43 | 77% (90d) | Controller issues (63%) | 88% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 158 | [ ] | Russian Fishing 4 (STEAM) | 33 | 39 | 85% (90d) | Does not open (68%) | 72% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 159 | [ ] | Hotline Miami (GOG) | 33 | 38 | 87% (90d) | Does not open (94%) | 65% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 160 | [ ] | COCOON (STEAM) | 32 | 62 | 52% (90d) | Directx error (50%) | 89% |  |
| 161 | [ ] | Max Payne (STEAM) | 32 | 58 | 55% (90d) | Controller issues (46%) | 93% |  |
| 162 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 32 | 57 | 75% (1.3.0) | Does not open (48%) | 67% |  |
| 163 | [ ] | Earthion (STEAM) | 32 | 53 | 60% (90d) | Controller issues (90%) | 100% |  |
| 164 | [ ] | Rocket League (STEAM) | 32 | 53 | 60% (90d) | Does not open (74%) | 71% |  |
| 165 | [ ] | Counter-Strike:Global Offensive (STEAM) | 32 | 50 | 64% (90d) | Does not open (78%) | 75% |  |
| 166 | [ ] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 32 | 50 | 64% (90d) | Does not open (85%) | 85% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 167 | [ ] | Capcom Fighting Collection 2 (STEAM) | 32 | 49 | 65% (90d) | Does not open (81%) | 85% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 168 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 32 | 45 | 71% (90d) | Controller issues (87%) | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 169 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 32 | 37 | 86% (90d) | Does not open (73%) | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 170 | [ ] | Red Dead Redemption (STEAM) | 32 | 36 | 89% (90d) | Does not open (95%) | 84% |  |
| 171 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 31 | 60 | 52% (90d) | Does not open (73%) | 87% |  |
| 172 | [ ] | Mortal Kombat X (STEAM) | 31 | 59 | 53% (90d) | Does not open (55%) | 83% |  |
| 173 | [ ] | Resident Evil Village (STEAM) | 31 | 53 | 58% (90d) | Does not open (67%) | 90% |  |
| 174 | [ ] | Tower and Sword of Succubus (STEAM) | 31 | 46 | 67% (90d) | No graphics (81%) | 100% |  |
| 175 | [ ] | Nioh: Complete Edition (STEAM) | 31 | 42 | 74% (90d) | Does not open (56%) | 94% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 176 | [ ] | Super Animal Royale (STEAM) | 31 | 42 | 74% (90d) | Does not open (68%) | 72% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 177 | [ ] | Path of Exile 2 (STEAM) | 31 | 37 | 84% (90d) | Does not open (96%) | 89% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 178 | [ ] | Yakuza: Like a Dragon (STEAM) | 30 | 44 | 68% (90d) | Does not open (61%) | 67% |  |
| 179 | [ ] | Ultimate Custom Night (STEAM) | 30 | 42 | 71% (90d) | No graphics (72%) | 79% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 180 | [ ] | Dead Island Riptide Definitive Edition (STEAM) | 29 | 57 | 51% (90d) | Does not open (50%) | 80% |  |
| 181 | [ ] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 54 | 54% (90d) | Does not open (92%) | 83% |  |
| 182 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 29 | 52 | 56% (90d) | Does not open (44%) | 91% |  |
| 183 | [ ] | Aethermancer (STEAM) | 29 | 51 | 57% (90d) | Does not open (78%) | 88% |  |
| 184 | [ ] | Heavy Rain (STEAM) | 29 | 51 | 57% (90d) | Controller issues (61%) | 92% |  |
| 185 | [ ] | Secrets of Grindea (STEAM) | 29 | 47 | 62% (90d) | Does not open (45%) | 78% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 186 | [ ] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 29 | 47 | 62% (90d) | Does not open (44%) | 80% |  |
| 187 | [ ] | Metro: Last Light Complete Edition (STEAM) | 29 | 35 | 83% (90d) | Does not open (57%) | 60% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 188 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 29 | 35 | 83% (90d) | Does not open (65%) | 79% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 189 | [ ] | Binary Domain (STEAM) | 28 | 44 | 64% (90d) | Does not open (91%) | 75% |  |
| 190 | [ ] | Moonlight Peaks (STEAM) | 28 | 40 | 70% (90d) | Does not open (64%) | 87% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 191 | [ ] | Zero Escape: The Nonary Games (STEAM) | 27 | 45 | 60% (90d) | Does not open (92%) | 67% |  |
| 192 | [ ] | Battle Brothers (STEAM) | 27 | 42 | 64% (90d) | Does not open (67%) | 66% |  |
| 193 | [ ] | Dead Rising 2 (STEAM) | 27 | 42 | 67% (1.3.0) | Does not open (88%) | 70% |  |
| 194 | [ ] | Deus Ex™ GOTY Edition (GOG) | 27 | 41 | 66% (90d) | Does not open (35%) | 91% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 195 | [ ] | Ratatan (STEAM) | 27 | 41 | 66% (90d) | Does not open (50%) | 98% |  |
| 196 | [ ] | Gothic II: Gold Classic (STEAM) | 27 | 38 | 71% (90d) | Does not open (56%) | 73% |  |
| 197 | [ ] | Bongo Cat (STEAM) | 27 | 37 | 73% (90d) | Does not open (68%) | 83% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 198 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 27 | 37 | 73% (90d) | Does not open (64%) | 90% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 199 | [ ] | Stellar Blade™ (STEAM) | 27 | 37 | 73% (90d) | Does not open (45%) | 87% |  |
| 200 | [ ] | CRUEL (STEAM) | 27 | 33 | 82% (90d) | Does not open (88%) | 80% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 201 | [ ] | ENA: Dream BBQ (STEAM) | 26 | 76 | 50% (1.3.0) | Does not open (43%) | 85% |  |
| 202 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 26 | 48 | 54% (90d) | Does not open (55%) | 78% |  |
| 203 | [ ] | Akane (STEAM) | 26 | 45 | 58% (90d) | Controller issues (63%) | 100% |  |
| 204 | [ ] | Digimon Survive (STEAM) | 26 | 42 | 62% (90d) | Controller issues (73%) | 96% |  |
| 205 | [ ] | Opus Magnum (STEAM) | 26 | 40 | 65% (90d) | Does not open (78%) | 88% |  |
| 206 | [ ] | Limbus Company (STEAM) | 26 | 39 | 67% (90d) | Does not open (86%) | 76% |  |
| 207 | [ ] | Tales of Zestiria (STEAM) | 26 | 32 | 81% (90d) | Does not open (80%) | 71% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 208 | [ ] | Tearscape (STEAM) | 26 | 31 | 84% (90d) | Controller issues (55%) | 94% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 209 | [ ] | No, I'm not a Human (STEAM) | 25 | 56 | 57% (1.3.0) | Does not open (48%) | 93% |  |
| 210 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 25 | 45 | 56% (90d) | Controller issues (71%) | 96% |  |
| 211 | [ ] | Lucid Blocks (STEAM) | 25 | 44 | 57% (90d) | Does not open (81%) | 61% |  |
| 212 | [ ] | Being a DIK (STEAM) | 25 | 43 | 58% (90d) | Does not open (78%) | 71% |  |
| 213 | [ ] | Prince of Persia (GOG) | 25 | 42 | 60% (90d) | Does not open (94%) | 96% |  |
| 214 | [ ] | Changed (STEAM) | 25 | 38 | 66% (90d) | Does not open (65%) | 88% |  |
| 215 | [ ] | Return to Monkey Island (STEAM) | 25 | 38 | 66% (90d) | No graphics (58%) | 85% |  |
| 216 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 25 | 34 | 74% (90d) | Does not open (41%) | 64% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 217 | [ ] | Crab Game (STEAM) | 25 | 33 | 76% (90d) | Does not open (53%) | 77% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 218 | [ ] | Goose Goose Duck (STEAM) | 25 | 33 | 76% (90d) | Does not open (71%) | 71% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 219 | [ ] | Jade Empire: Special Edition (GOG) | 25 | 33 | 76% (90d) | Does not open (45%) | 75% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 220 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 32 | 78% (90d) | Does not open (87%) | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 221 | [ ] | Resident Evil (GOG) | 25 | 27 | 93% (90d) | Does not open (95%) | 62% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 222 | [ ] | Resident Evil Revelations 2 (STEAM) | 24 | 47 | 51% (90d) | Does not open (40%) | 92% |  |
| 223 | [ ] | Unturned (STEAM) | 24 | 45 | 53% (90d) | Does not open (59%) | 77% |  |
| 224 | [ ] | Wizard of Legend (EPIC) | 24 | 41 | 59% (90d) | Does not open (78%) | 85% |  |
| 225 | [ ] | Cat Mail Co. (STEAM) | 24 | 39 | 62% (90d) | Does not open (89%) | 83% |  |
| 226 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 24 | 35 | 69% (90d) | Does not open (57%) | 71% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 227 | [ ] | CarX Street (STEAM) | 24 | 30 | 80% (90d) | Does not open (79%) | 92% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 228 | [ ] | The Lantern of the Laughless Saint (STEAM) | 24 | 25 | 96% (90d) | Does not open (81%) | 64% | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 229 | [ ] | Goat Simulator (STEAM) | 23 | 45 | 51% (90d) | Does not open (56%) | 61% |  |
| 230 | [ ] | Football Manager 2024 (EPIC) | 23 | 42 | 55% (90d) | Does not open (86%) | 93% |  |
| 231 | [ ] | Lobotomy Corporation (STEAM) | 23 | 42 | 55% (90d) | No graphics (60%) | 93% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 232 | [ ] | Pinball FX Classic (STEAM) | 23 | 41 | 56% (90d) | Does not open (76%) | 92% |  |
| 233 | [ ] | SWORN (STEAM) | 23 | 39 | 59% (90d) | Does not open (44%) | 95% |  |
| 234 | [ ] | Worms W.M.D (STEAM) | 23 | 38 | 61% (90d) | Does not open (58%) | 89% |  |
| 235 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 37 | 62% (90d) | Does not open (100%) | 75% |  |
| 236 | [ ] | Timberborn (STEAM) | 23 | 34 | 68% (90d) | No graphics (62%) | 83% |  |
| 237 | [ ] | Party Animals (STEAM) | 23 | 32 | 72% (90d) | Does not open (75%) | 73% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 238 | [ ] | FINAL FANTASY XIV Online (STEAM) | 23 | 30 | 77% (90d) | Does not open (100%) | 96% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 239 | [ ] | Jade Empire: Special Edition (STEAM) | 23 | 26 | 88% (90d) | Does not open (95%) | 69% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 240 | [ ] | PowerWash Simulator (STEAM) | 22 | 64 | 76% (1.3.0) | Does not open (84%) | 74% |  |
| 241 | [ ] | Gambonanza (STEAM) | 22 | 41 | 54% (90d) | Does not open (65%) | 92% |  |
| 242 | [ ] | Life is Strange Remastered (STEAM) | 22 | 34 | 65% (90d) | Does not open (73%) | 94% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 243 | [ ] | Beyond: Two Souls (STEAM) | 22 | 30 | 73% (90d) | Does not open (48%) | 71% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 244 | [ ] | Legacy of Kain™ Soul Reaver 1&2 Remastered (STEAM) | 21 | 60 | 75% (1.3.0) | Does not open (79%) | 100% |  |
| 245 | [ ] | This War of Mine (STEAM) | 21 | 38 | 55% (90d) | No graphics (53%) | 73% |  |
| 246 | [ ] | Trailmakers (STEAM) | 21 | 38 | 55% (90d) | Does not open (44%) | 93% |  |
| 247 | [ ] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 21 | 36 | 58% (90d) | Controller issues (50%) | 100% |  |
| 248 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 21 | 30 | 70% (90d) | Does not open (67%) | 87% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 249 | [ ] | Need for Speed™ Unbound (STEAM) | 21 | 29 | 72% (90d) | Does not open (82%) | 80% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 250 | [ ] | Nex Machina (STEAM) | 21 | 28 | 75% (90d) | Does not open (57%) | 77% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 251 | [ ] | Capcom Fighting Collection (STEAM) | 21 | 26 | 81% (90d) | Does not open (79%) | 79% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 252 | [ ] | Deadly Premonition: The Director's Cut (STEAM) | 21 | 24 | 88% (90d) | Does not open (53%) | 75% |  |
| 253 | [ ] | Crimzon Clover World EXplosion (STEAM) | 20 | 40 | 50% (90d) | Does not open (47%) | 100% |  |
| 254 | [ ] | Control Ultimate Edition (GOG) | 20 | 38 | 53% (90d) | Does not open (81%) | 97% |  |
| 255 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 20 | 37 | 54% (90d) | Does not open (56%) | 71% |  |
| 256 | [ ] | One-armed robber (STEAM) | 20 | 37 | 54% (90d) | Controller issues (56%) | 81% |  |
| 257 | [ ] | Tiny Glade (STEAM) | 20 | 34 | 59% (90d) | Does not open (44%) | 78% |  |
| 258 | [ ] | BAJA: Edge of Control HD (STEAM) | 20 | 27 | 74% (90d) | Does not open (100%) | 90% | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 259 | [ ] | Dead Island (STEAM) | 20 | 26 | 77% (90d) | Does not open (69%) | 71% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 260 | [ ] | Tyr (STEAM) | 20 | 26 | 77% (90d) | Does not open (33%) | 82% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 261 | [ ] | Mafia: Definitive Edition (STEAM) | 19 | 36 | 53% (90d) | Does not open (83%) | 75% |  |
| 262 | [ ] | Killing Floor (STEAM) | 19 | 34 | 56% (90d) | Controller issues (100%) | 82% |  |
| 263 | [ ] | My Summer Car (STEAM) | 19 | 34 | 56% (90d) | Does not open (59%) | 86% |  |
| 264 | [ ] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 19 | 33 | 58% (90d) | Does not open (88%) | 71% |  |
| 265 | [ ] | Stick It to the Stickman (STEAM) | 19 | 33 | 58% (90d) | Does not open (88%) | 74% |  |
| 266 | [ ] | Metro Exodus (STEAM) | 19 | 31 | 61% (90d) | Does not open (82%) | 90% |  |
| 267 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 19 | 28 | 68% (90d) | Does not open (71%) | 70% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 268 | [ ] | Torchlight II (EPIC) | 19 | 27 | 70% (90d) | Does not open (82%) | 94% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 269 | [ ] | Katanaut (STEAM) | 19 | 25 | 76% (90d) | Does not open (78%) | 62% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 270 | [ ] | Faster Than Light (EPIC) | 18 | 35 | 51% (90d) | Does not open (41%) | 100% |  |
| 271 | [ ] | Far Far West (STEAM) | 18 | 32 | 56% (90d) | Does not open (59%) | 78% |  |
| 272 | [ ] | Tabletop Simulator (STEAM) | 18 | 30 | 60% (90d) | Does not open (50%) | 64% |  |
| 273 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 29 | 62% (90d) | No graphics (39%) | 81% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 274 | [ ] | Maneater (STEAM) | 18 | 28 | 64% (90d) | Does not open (92%) | 72% |  |
| 275 | [ ] | Arcade Paradise (EPIC) | 18 | 27 | 67% (90d) | Does not open (45%) | 83% |  |
| 276 | [ ] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 18 | 27 | 67% (90d) | Does not open (83%) | 96% |  |
| 277 | [ ] | DOOM 3: BFG Edition (GOG) | 18 | 25 | 72% (90d) | No graphics (67%) | 79% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 278 | [ ] | Crusader Kings III (STEAM) | 18 | 23 | 78% (90d) | No graphics (64%) | 69% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 279 | [ ] | Dorfromantik (GOG) | 18 | 23 | 78% (90d) | Does not open (94%) | 70% | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 280 | [ ] | SKALD: Against the Black Priory (STEAM) | 17 | 34 | 50% (90d) | No graphics (57%) | 97% |  |
| 281 | [ ] | SCP – Containment Breach (STEAM) | 17 | 32 | 53% (90d) | Does not open (82%) | 85% |  |
| 282 | [ ] | GRANDIA HD Remaster (STEAM) | 17 | 31 | 55% (90d) | Does not open (93%) | 76% |  |
| 283 | [ ] | GRIP: Combat Racing (STEAM) | 17 | 31 | 55% (90d) | Does not open (100%) | 82% |  |
| 284 | [ ] | Shank 2 (STEAM) | 17 | 31 | 55% (90d) | Does not open (82%) | 100% |  |
| 285 | [ ] | Sorry We're Closed (EPIC) | 17 | 30 | 55% (14d) | Does not open (88%) | 83% |  |
| 286 | [ ] | Grim Fandango Remastered (GOG) | 17 | 25 | 68% (90d) | No graphics (78%) | 60% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 287 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 17 | 23 | 74% (90d) | No graphics (60%) | 82% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 288 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 17 | 22 | 77% (90d) | Does not open (80%) | 93% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 289 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 16 | 31 | 52% (90d) | Does not open (100%) | 65% |  |
| 290 | [ ] | DNF Duel (EPIC) | 16 | 29 | 55% (90d) | Does not open (54%) | 91% |  |
| 291 | [ ] | Titanfall® 2 (STEAM) | 16 | 29 | 55% (90d) | Does not open (83%) | 77% |  |
| 292 | [ ] | Dishonored 2 (STEAM) | 16 | 26 | 62% (90d) | Does not open (85%) | 92% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 293 | [ ] | LET IT DIE (STEAM) | 16 | 26 | 62% (90d) | Does not open (83%) | 73% |  |
| 294 | [ ] | Legend of Grimrock 2 (STEAM) | 16 | 23 | 70% (90d) | Does not open (92%) | 70% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 295 | [ ] | Fall Guys (STEAM) | 16 | 22 | 73% (90d) | Does not open (92%) | 92% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 296 | [ ] | EVE Online (STEAM) | 16 | 20 | 80% (90d) | No graphics (57%) | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 297 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 16 | 20 | 80% (90d) | Does not open (60%) | 92% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 298 | [ ] | Mark of the Ninja (STEAM) | 15 | 30 | 50% (90d) | Does not open (75%) | 64% |  |
| 299 | [ ] | Lost Castle 2 (STEAM) | 15 | 29 | 52% (90d) | Does not open (64%) | 100% |  |
| 300 | [ ] | Hitman: Absolution (GOG) | 15 | 28 | 54% (90d) | Does not open (85%) | 71% |  |
| 301 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 15 | 26 | 58% (90d) | Does not open (92%) | 60% |  |
| 302 | [ ] | WORLD OF FINAL FANTASY (STEAM) | 15 | 26 | 58% (90d) | No graphics (58%) | 80% |  |
| 303 | [ ] | Wildermyth (STEAM) | 15 | 26 | 58% (90d) | Does not open (50%) | 94% |  |
| 304 | [ ] | Mortal Shell (EPIC) | 15 | 25 | 60% (90d) | No graphics (89%) | 91% |  |
| 305 | [ ] | Batman™: Arkham Origins (GOG) | 15 | 24 | 63% (90d) | Does not open (67%) | 93% |  |
| 306 | [ ] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 15 | 23 | 65% (90d) | Does not open (64%) | 65% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 307 | [ ] | Allumeria (STEAM) | 15 | 22 | 68% (90d) | Does not open (69%) | 80% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 308 | [ ] | Chef Knight (STEAM) | 15 | 22 | 68% (90d) | Does not open (100%) | 67% |  |
| 309 | [ ] | Maneater (EPIC) | 15 | 20 | 75% (90d) | Does not open (73%) | 83% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 310 | [ ] | Human Fall Flat (STEAM) | 14 | 28 | 50% (90d) | Does not open (46%) | 64% |  |
| 311 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 28 | 50% (90d) | Controller issues (54%) | 83% |  |
| 312 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 25 | 56% (90d) | Does not open (90%) | 72% |  |
| 313 | [ ] | Ultrapool (STEAM) | 14 | 25 | 56% (90d) | Does not open (54%) | 100% |  |
| 314 | [ ] | Gloomwood (STEAM) | 14 | 24 | 58% (90d) | Does not open (62%) | 75% |  |
| 315 | [ ] | 12 is Better Than 6 (STEAM) | 14 | 23 | 61% (90d) | Does not open (45%) | 83% |  |
| 316 | [ ] | Shift At Midnight (STEAM) | 14 | 23 | 61% (90d) | Does not open (83%) | 92% |  |
| 317 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 23 | 61% (90d) | Controller issues (62%) | 64% |  |
| 318 | [ ] | Disgaea 4 Complete+ (STEAM) | 14 | 22 | 64% (90d) | No graphics (43%) | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 319 | [ ] | Sons Of The Forest (STEAM) | 14 | 22 | 64% (90d) | Does not open (50%) | 74% |  |
| 320 | [ ] | Intravenous 2 (STEAM) | 13 | 26 | 50% (90d) | No graphics (63%) | 87% |  |
| 321 | [ ] | Lust Goddess (STEAM) | 13 | 25 | 52% (90d) | Does not open (100%) | 69% |  |
| 322 | [ ] | Haydee (STEAM) | 13 | 24 | 54% (90d) | Does not open (100%) | 82% |  |
| 323 | [ ] | Ready or Not (STEAM) | 13 | 24 | 54% (90d) | Does not open (55%) | 93% |  |
| 324 | [ ] | DiRT 4 (STEAM) | 13 | 23 | 57% (90d) | Does not open (75%) | 96% |  |
| 325 | [ ] | Minit (EPIC) | 13 | 23 | 57% (90d) | Does not open (82%) | 82% |  |
| 326 | [ ] | Scrap Mechanic (STEAM) | 13 | 23 | 57% (90d) | Does not open (45%) | 72% |  |
| 327 | [ ] | Alabaster Dawn Demo (STEAM) | 13 | 22 | 59% (90d) | Controller issues (77%) | 89% |  |
| 328 | [ ] | PAYDAY: The Heist (STEAM) | 13 | 21 | 62% (90d) | Does not open (75%) | 69% |  |
| 329 | [ ] | Horny Villa (STEAM) | 13 | 20 | 65% (90d) | Does not open (57%) | 95% |  |
| 330 | [ ] | War Thunder (STEAM) | 13 | 20 | 65% (90d) | Does not open (80%) | 80% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 331 | [ ] | Sonic Superstars (STEAM) | 12 | 24 | 50% (90d) | Does not open (70%) | 67% |  |
| 332 | [ ] | AER Memories of Old (EPIC) | 12 | 23 | 52% (90d) | Does not open (91%) | 93% |  |
| 333 | [ ] | Cruelty Squad (STEAM) | 12 | 23 | 52% (90d) | Does not open (67%) | 89% |  |
| 334 | [ ] | HITMAN World of Assassination (STEAM) | 12 | 23 | 52% (90d) | Does not open (73%) | 85% |  |
| 335 | [ ] | NiGHTS into Dreams... (STEAM) | 12 | 23 | 52% (90d) | Does not open (44%) | 92% |  |
| 336 | [ ] | Pillars of Eternity (STEAM) | 12 | 23 | 52% (90d) | Does not open (33%) | 62% |  |
| 337 | [ ] | UNDEFEATED (STEAM) | 12 | 23 | 52% (90d) | Does not open (89%) | 79% |  |
| 338 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 12 | 22 | 55% (90d) | Does not open (60%) | 91% |  |
| 339 | [ ] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 22 | 55% (90d) | Controller issues (60%) | 88% |  |
| 340 | [ ] | FATE (STEAM) | 12 | 21 | 57% (90d) | No graphics (44%) | 91% |  |
| 341 | [ ] | [WoG] War of Genesis: Idle Loot (STEAM) | 12 | 20 | 60% (90d) | Does not open (89%) | 96% |  |
| 342 | [ ] | Castle in the Clouds (STEAM) | 11 | 22 | 50% (90d) | No graphics (63%) | 83% |  |
| 343 | [ ] | Injustice™ 2 (STEAM) | 11 | 22 | 50% (90d) | Does not open (88%) | 73% |  |
| 344 | [ ] | MX Bikes (STEAM) | 11 | 22 | 50% (90d) | Does not open (73%) | 94% |  |
| 345 | [ ] | Tom Clancy's Rainbow Six: Vegas 2 (STEAM) | 11 | 22 | 50% (90d) | Does not open (55%) | 88% |  |
| 346 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 21 | 52% (90d) | Does not open (86%) | 72% |  |
| 347 | [ ] | GRANDIA II HD Remaster (STEAM) | 11 | 21 | 52% (90d) | Does not open (70%) | 69% |  |
| 348 | [ ] | Ghostwire Tokyo (EPIC) | 11 | 21 | 52% (90d) | Does not open (86%) | 94% |  |
| 349 | [ ] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 21 | 52% (90d) | Graphics glitches (40%) | 94% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 350 | [ ] | Hitman: Contracts (STEAM) | 11 | 20 | 55% (90d) | Controller issues (90%) | 80% |  |
| 351 | [ ] | Coromon (GOG) | 10 | 20 | 50% (90d) | Does not open (56%) | 63% |  |
| 352 | [ ] | Pocket Mirror ~ GoldenerTraum (STEAM) | 10 | 20 | 50% (90d) | Does not open (78%) | 93% |  |

## Recently recovered (395)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | FINAL FANTASY RESONANCE (STEAM) | 333 | 2026-10-24 | 760 | 75% |  |
| 2 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 249 | 2026-10-23 | 291 | 69% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 3 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 242 | 2026-10-19 | 297 | 67% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 4 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 241 | 2026-10-18 | 367 | 58% |  |
| 5 | [x] | OMORI (STEAM) | 202 | 2026-10-16 | 244 | 83% |  |
| 6 | [x] | DRAGON BALL FighterZ (STEAM) | 202 | 2026-11-01 | 235 | 65% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 7 | [x] | Devil May Cry HD Collection (STEAM) | 201 | 2026-10-19 | 280 | 77% |  |
| 8 | [x] | Spelunky 2 (STEAM) | 188 | 2026-11-01 | 209 | 55% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 9 | [x] | Sid Meier's Civilization V (STEAM) | 172 | 2026-11-06 | 184 | 60% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 10 | [x] | Burnout Paradise: The Ultimate Box (STEAM) | 148 | 2026-10-16 | 240 | 72% |  |
| 11 | [x] | Borderlands 2 (EPIC) | 142 | 2026-10-25 | 168 | 61% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 12 | [x] | Sonic Adventure™ 2  (STEAM) | 140 | 2026-11-01 | 197 | 52% | [#467](https://github.com/GameNative/gamenative-compat/issues/467) |
| 13 | [x] | Counter-Strike (STEAM) | 138 | 2026-10-22 | 223 | 51% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 14 | [x] | Minecraft Dungeons II (STEAM) | 126 | 2026-10-21 | 144 | 67% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 15 | [x] | Far Cry® 3 (STEAM) | 126 | 2026-10-21 | 140 | 68% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 16 | [x] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 122 | 2026-10-18 | 170 | 65% |  |
| 17 | [x] | Diablo II: Resurrected – Infernal Edition (STEAM) | 120 | 2026-10-28 | 153 | 65% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 18 | [x] | Call of Duty: Black Ops III (STEAM) | 117 | 2026-10-18 | 246 | 73% |  |
| 19 | [x] | Euro Truck Simulator 2 (STEAM) | 115 | 2026-11-01 | 213 | 57% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 20 | [x] | The Witcher: Enhanced Edition (STEAM) | 112 | 2026-10-25 | 129 | 63% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 21 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 107 | 2026-10-18 | 159 | 76% |  |
| 22 | [x] | Moonstone Island (STEAM) | 102 | 2026-10-16 | 135 | 87% |  |
| 23 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 94 | 2026-10-25 | 150 | 69% |  |
| 24 | [x] | Don't Starve Together (STEAM) | 92 | 2026-10-16 | 180 | 81% |  |
| 25 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 92 | 2026-10-17 | 119 | 97% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 26 | [x] | Catherine Classic (STEAM) | 89 | 2026-10-19 | 178 | 79% |  |
| 27 | [x] | Ultra Street Fighter IV (STEAM) | 84 | 2026-10-17 | 180 | 69% |  |
| 28 | [x] | Hogwarts Legacy (STEAM) | 84 | 2026-10-17 | 145 | 65% |  |
| 29 | [x] | Cry of Fear (STEAM) | 82 | 2026-10-18 | 162 | 81% |  |
| 30 | [x] | DOOM 3: BFG Edition (STEAM) | 78 | 2026-10-19 | 114 | 70% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 31 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 73 | 2026-10-18 | 123 | 93% |  |
| 32 | [x] | Sol Cesto (EPIC) | 73 | 2026-11-03 | 77 | 73% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 33 | [x] | Bayonetta (STEAM) | 71 | 2026-10-18 | 207 | 80% |  |
| 34 | [x] | Need for Speed: Hot Pursuit (STEAM) | 71 | 2026-10-25 | 105 | 81% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 35 | [x] | Darksiders (STEAM) | 71 | 2026-10-26 | 86 | 88% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 36 | [x] | Disgaea 5 Complete (STEAM) | 70 | 2026-10-18 | 84 | 98% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 37 | [x] | American Truck Simulator (STEAM) | 68 | 2026-10-18 | 111 | 81% |  |
| 38 | [x] | Dota 2 (STEAM) | 68 | 2026-10-17 | 104 | 69% |  |
| 39 | [x] | Don't Starve (STEAM) | 67 | 2026-10-16 | 157 | 81% |  |
| 40 | [x] | Bloodstained: Ritual of the Night (EPIC) | 67 | 2026-10-19 | 123 | 63% |  |
| 41 | [x] | Spyro™ Reignited Trilogy (STEAM) | 67 | 2026-10-18 | 105 | 74% |  |
| 42 | [x] | Stardew Valley (GOG) | 66 | 2026-11-01 | 120 | 53% |  |
| 43 | [x] | Fallout (STEAM) | 66 | 2026-10-18 | 103 | 73% |  |
| 44 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 66 | 2026-10-17 | 95 | 80% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 45 | [x] | Call of Juarez Gunslinger (STEAM) | 66 | 2026-10-18 | 81 | 75% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 46 | [x] | Gunfire Reborn (STEAM) | 65 | 2026-10-22 | 71 | 93% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 47 | [x] | Fable - The Lost Chapters (STEAM) | 64 | 2026-10-17 | 102 | 79% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 48 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 63 | 2026-11-06 | 85 | 63% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 49 | [x] | Borderlands: The Pre-Sequel (STEAM) | 62 | 2026-10-17 | 89 | 68% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 50 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 61 | 2026-10-17 | 85 | 88% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 51 | [x] | A Plague Tale: Innocence (STEAM) | 60 | 2026-10-20 | 63 | 78% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 52 | [x] | Poppy Playtime (STEAM) | 59 | 2026-10-17 | 107 | 80% |  |
| 53 | [x] | Borderlands 3 (STEAM) | 58 | 2026-10-19 | 78 | 93% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 54 | [x] | Mini Motorways (STEAM) | 57 | 2026-11-04 | 99 | 63% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 55 | [x] | Starbound (STEAM) | 57 | 2026-10-18 | 88 | 73% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 56 | [x] | Call of Duty: World at War (STEAM) | 57 | 2026-10-28 | 81 | 75% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 57 | [x] | Sonic Generations (STEAM) | 57 | 2026-10-17 | 66 | 64% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 58 | [x] | eFootball™ (STEAM) | 56 | 2026-10-18 | 84 | 79% |  |
| 59 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 55 | 2026-10-18 | 86 | 74% |  |
| 60 | [x] | Alex Kidd in Miracle World DX (EPIC) | 55 | 2026-10-22 | 59 | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 61 | [x] | TBH: Task Bar Hero (STEAM) | 54 | 2026-10-19 | 87 | 92% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 62 | [x] | Big Walk (STEAM) | 54 | 2026-10-17 | 86 | 84% |  |
| 63 | [x] | Vampire Survivors (EPIC) | 54 | 2026-11-03 | 76 | 64% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 64 | [x] | Okami HD (STEAM) | 53 | 2026-10-17 | 98 | 86% |  |
| 65 | [x] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 53 | 2026-11-06 | 89 | 65% |  |
| 66 | [x] | Sonic Adventure DX (STEAM) | 53 | 2026-10-17 | 88 | 61% |  |
| 67 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 53 | 2026-10-18 | 77 | 66% |  |
| 68 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 52 | 2026-10-19 | 98 | 75% |  |
| 69 | [x] | Path of Exile (STEAM) | 52 | 2026-10-26 | 61 | 80% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 70 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 51 | 2026-10-25 | 98 | 56% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 71 | [x] | Until Then (STEAM) | 51 | 2026-10-17 | 90 | 96% |  |
| 72 | [x] | A Plague Tale: Innocence (EPIC) | 51 | 2026-10-25 | 87 | 89% |  |
| 73 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 51 | 2026-10-21 | 59 | 86% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 74 | [x] | Darkest Dungeon® (EPIC) | 49 | 2026-10-22 | 88 | 61% |  |
| 75 | [x] | Guildrun Demo (STEAM) | 49 | 2026-10-22 | 69 | 75% |  |
| 76 | [x] | Dead Space (STEAM) | 49 | 2026-10-18 | 62 | 78% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 77 | [x] | Sheepy: A Short Adventure (STEAM) | 49 | 2026-10-24 | 59 | 82% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 78 | [x] | Sleeping Dogs™ (STEAM) | 48 | 2026-10-27 | 55 | 77% | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 79 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 2026-10-17 | 75 | 96% |  |
| 80 | [x] | Watch_Dogs 2 (STEAM) | 47 | 2026-11-03 | 52 | 60% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 81 | [x] | Deadlock (STEAM) | 46 | 2026-10-16 | 67 | 93% |  |
| 82 | [x] | Rivals of Aether II (STEAM) | 46 | 2026-10-20 | 65 | 82% |  |
| 83 | [x] | Abiotic Factor (STEAM) | 45 | 2026-10-18 | 78 | 65% |  |
| 84 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 45 | 2026-10-17 | 77 | 89% |  |
| 85 | [x] | Plague Inc: Evolved (STEAM) | 44 | 2026-11-06 | 66 | 60% |  |
| 86 | [x] | Tomb Raider: Anniversary (STEAM) | 44 | 2026-10-25 | 65 | 64% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 87 | [x] | Sonic Lost World (STEAM) | 44 | 2026-10-18 | 61 | 84% |  |
| 88 | [x] | Aggelos (STEAM) | 44 | 2026-10-21 | 58 | 94% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 89 | [x] | Moonlighter (EPIC) | 44 | 2026-10-23 | 48 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 90 | [x] | MudRunner (STEAM) | 43 | 2026-10-24 | 97 | 71% |  |
| 91 | [x] | Tomb Raider GOTY (GOG) | 43 | 2026-10-17 | 91 | 97% |  |
| 92 | [x] | Digimon World: Next Order (STEAM) | 43 | 2026-10-18 | 83 | 95% |  |
| 93 | [x] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 43 | 2026-11-05 | 46 | 64% | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 94 | [x] | Death Road to Canada (STEAM) | 42 | 2026-10-17 | 100 | 71% |  |
| 95 | [x] | PROTOTYPE 2 (STEAM) | 42 | 2026-10-18 | 88 | 76% |  |
| 96 | [x] | Skullgirls 2nd Encore (STEAM) | 42 | 2026-11-01 | 77 | 57% |  |
| 97 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 42 | 2026-10-18 | 63 | 70% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 98 | [x] | FINAL FANTASY VII (2013) (STEAM) | 42 | 2026-10-18 | 60 | 81% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 99 | [x] | Dead by Daylight (STEAM) | 42 | 2026-10-23 | 46 | 81% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 100 | [x] | Street Fighter™ 6 (STEAM) | 41 | 2026-10-16 | 67 | 86% |  |
| 101 | [x] | Rogue Legacy (STEAM) | 40 | 2026-10-17 | 91 | 64% |  |
| 102 | [x] | Life is Strange™ (STEAM) | 40 | 2026-10-17 | 83 | 82% |  |
| 103 | [x] | Amnesia: The Dark Descent (STEAM) | 40 | 2026-10-17 | 75 | 76% |  |
| 104 | [x] | FINAL FANTASY VII REBIRTH (STEAM) | 40 | 2026-10-27 | 41 | 83% | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 105 | [x] | Cobalt Core (STEAM) | 39 | 2026-10-18 | 90 | 88% |  |
| 106 | [x] | Rayman Origins (STEAM) | 39 | 2026-10-17 | 87 | 82% |  |
| 107 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 39 | 2026-10-17 | 74 | 98% |  |
| 108 | [x] | Capcom Arcade Stadium (STEAM) | 39 | 2026-10-17 | 48 | 83% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 109 | [x] | CrossCode (GOG) | 38 | 2026-10-23 | 42 | 73% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 110 | [x] | Monster Hunter Wilds (STEAM) | 38 | 2026-10-23 | 39 | 83% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 111 | [x] | Sable (EPIC) | 37 | 2026-10-18 | 79 | 84% |  |
| 112 | [x] | Tales of ARISE (STEAM) | 37 | 2026-10-16 | 75 | 92% |  |
| 113 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 2026-10-17 | 69 | 89% |  |
| 114 | [x] | Elite Dangerous (STEAM) | 37 | 2026-11-05 | 40 | 69% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 115 | [x] | Salt and Sanctuary (STEAM) | 36 | 2026-10-18 | 76 | 83% |  |
| 116 | [x] | Supermarket Together (STEAM) | 36 | 2026-10-19 | 50 | 70% |  |
| 117 | [x] | POSTAL 2 (GOG) | 35 | 2026-10-22 | 71 | 93% |  |
| 118 | [x] | STAR WARS™ Episode I: Racer (GOG) | 35 | 2026-11-02 | 42 | 82% | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 119 | [x] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 35 | 2026-11-01 | 40 | 60% | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 120 | [x] | Teardown (STEAM) | 34 | 2026-10-17 | 76 | 76% |  |
| 121 | [x] | Journey (STEAM) | 34 | 2026-10-27 | 71 | 55% |  |
| 122 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 34 | 2026-10-16 | 67 | 66% |  |
| 123 | [x] | Hearts of Iron IV (STEAM) | 34 | 2026-10-19 | 61 | 66% |  |
| 124 | [x] | SnowRunner (STEAM) | 34 | 2026-10-19 | 48 | 92% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 125 | [x] | Ultimate Chicken Horse (STEAM) | 33 | 2026-10-23 | 68 | 63% |  |
| 126 | [x] | Hero Siege (STEAM) | 33 | 2026-11-02 | 56 | 62% |  |
| 127 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 33 | 2026-10-19 | 53 | 74% |  |
| 128 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 2026-10-19 | 53 | 80% |  |
| 129 | [x] | Palia (STEAM) | 33 | 2026-10-22 | 45 | 77% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 130 | [x] | Romestead (STEAM) | 33 | 2026-10-18 | 44 | 77% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 131 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 33 | 2026-10-20 | 43 | 88% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 132 | [x] | Russian Fishing 4 (STEAM) | 33 | 2026-10-23 | 39 | 72% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 133 | [x] | Hotline Miami (GOG) | 33 | 2026-10-20 | 38 | 65% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 134 | [x] | Bloodstained: Curse of the Moon (STEAM) | 32 | 2026-10-16 | 72 | 73% |  |
| 135 | [x] | COCOON (STEAM) | 32 | 2026-10-17 | 62 | 89% |  |
| 136 | [x] | Max Payne (STEAM) | 32 | 2026-10-17 | 58 | 93% |  |
| 137 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 32 | 2026-10-26 | 57 | 67% |  |
| 138 | [x] | Earthion (STEAM) | 32 | 2026-10-22 | 53 | 100% |  |
| 139 | [x] | Rocket League (STEAM) | 32 | 2026-10-17 | 53 | 71% |  |
| 140 | [x] | Counter-Strike:Global Offensive (STEAM) | 32 | 2026-10-19 | 50 | 75% |  |
| 141 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 32 | 2026-10-18 | 50 | 85% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 142 | [x] | Capcom Fighting Collection 2 (STEAM) | 32 | 2026-10-18 | 49 | 85% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 143 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 32 | 2026-10-21 | 45 | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 144 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 32 | 2026-10-22 | 37 | 94% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 145 | [x] | Little Nightmares (STEAM) | 31 | 2026-10-16 | 71 | 59% |  |
| 146 | [x] | Torchlight II (STEAM) | 31 | 2026-10-20 | 64 | 91% |  |
| 147 | [x] | Mortal Kombat X (STEAM) | 31 | 2026-10-17 | 59 | 83% |  |
| 148 | [x] | Resident Evil Village (STEAM) | 31 | 2026-10-17 | 53 | 90% |  |
| 149 | [x] | Tower and Sword of Succubus (STEAM) | 31 | 2026-10-22 | 46 | 100% |  |
| 150 | [x] | Nioh: Complete Edition (STEAM) | 31 | 2026-10-20 | 42 | 94% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 151 | [x] | Super Animal Royale (STEAM) | 31 | 2026-10-19 | 42 | 72% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 152 | [x] | Path of Exile 2 (STEAM) | 31 | 2026-10-18 | 37 | 89% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 153 | [x] | Dishonored - Definitive Edition (EPIC) | 30 | 2026-10-17 | 78 | 83% |  |
| 154 | [x] | Ultimate Custom Night (STEAM) | 30 | 2026-10-19 | 42 | 79% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 155 | [x] | Grand Theft Auto III (STEAM) | 29 | 2026-10-17 | 75 | 78% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 156 | [x] | Library Of Ruina (STEAM) | 29 | 2026-10-16 | 62 | 89% |  |
| 157 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 29 | 2026-10-18 | 57 | 80% |  |
| 158 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 29 | 2026-10-17 | 54 | 83% |  |
| 159 | [x] | Prince of Persia: The Sands of Time (STEAM) | 29 | 2026-10-20 | 52 | 91% |  |
| 160 | [x] | Aethermancer (STEAM) | 29 | 2026-10-18 | 51 | 88% |  |
| 161 | [x] | Heavy Rain (STEAM) | 29 | 2026-10-18 | 51 | 92% |  |
| 162 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 29 | 2026-10-22 | 47 | 80% |  |
| 163 | [x] | Secrets of Grindea (STEAM) | 29 | 2026-10-20 | 47 | 78% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 164 | [x] | Metro: Last Light Complete Edition (STEAM) | 29 | 2026-11-06 | 35 | 60% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 165 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 29 | 2026-10-18 | 35 | 79% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 166 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 28 | 2026-10-19 | 93 | 94% |  |
| 167 | [x] | Dying Light (EPIC) | 28 | 2026-10-17 | 65 | 89% |  |
| 168 | [x] | BioShock™ (GOG) | 28 | 2026-10-18 | 63 | 71% |  |
| 169 | [x] | Monster Hunter Stories (STEAM) | 28 | 2026-10-17 | 63 | 86% |  |
| 170 | [x] | State of Decay: Year-One (STEAM) | 28 | 2026-10-18 | 60 | 83% |  |
| 171 | [x] | Stumble Guys (STEAM) | 28 | 2026-10-18 | 59 | 81% |  |
| 172 | [x] | Binary Domain (STEAM) | 28 | 2026-10-18 | 44 | 75% |  |
| 173 | [x] | Moonlight Peaks (STEAM) | 28 | 2026-10-20 | 40 | 87% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 174 | [x] | Zero Escape: The Nonary Games (STEAM) | 27 | 2026-10-17 | 45 | 67% |  |
| 175 | [x] | Battle Brothers (STEAM) | 27 | 2026-10-27 | 42 | 66% |  |
| 176 | [x] | Deus Ex™ GOTY Edition (GOG) | 27 | 2026-10-19 | 41 | 91% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 177 | [x] | Gothic II: Gold Classic (STEAM) | 27 | 2026-10-20 | 38 | 73% |  |
| 178 | [x] | Bongo Cat (STEAM) | 27 | 2026-10-20 | 37 | 83% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 179 | [x] | ELDEN RING NIGHTREIGN (STEAM) | 27 | 2026-11-03 | 37 | 90% | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 180 | [x] | CRUEL (STEAM) | 27 | 2026-10-28 | 33 | 80% | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 181 | [x] | PlateUp! (STEAM) | 26 | 2026-10-16 | 55 | 87% |  |
| 182 | [x] | G.I. Joe Wrath of Cobra (EPIC) | 26 | 2026-10-19 | 48 | 78% |  |
| 183 | [x] | Akane (STEAM) | 26 | 2026-10-20 | 45 | 100% |  |
| 184 | [x] | Digimon Survive (STEAM) | 26 | 2026-10-23 | 42 | 96% |  |
| 185 | [x] | Opus Magnum (STEAM) | 26 | 2026-11-01 | 40 | 88% |  |
| 186 | [x] | Limbus Company (STEAM) | 26 | 2026-10-18 | 39 | 76% |  |
| 187 | [x] | Tales of Zestiria (STEAM) | 26 | 2026-10-27 | 32 | 71% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 188 | [x] | Tearscape (STEAM) | 26 | 2026-10-30 | 31 | 94% | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 189 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 25 | 2026-10-19 | 63 | 83% |  |
| 190 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 25 | 2026-10-24 | 45 | 96% |  |
| 191 | [x] | Lucid Blocks (STEAM) | 25 | 2026-11-06 | 44 | 61% |  |
| 192 | [x] | Being a DIK (STEAM) | 25 | 2026-10-19 | 43 | 71% |  |
| 193 | [x] | Prince of Persia (GOG) | 25 | 2026-10-24 | 42 | 96% |  |
| 194 | [x] | Changed (STEAM) | 25 | 2026-10-24 | 38 | 88% |  |
| 195 | [x] | Return to Monkey Island (STEAM) | 25 | 2026-10-23 | 38 | 85% |  |
| 196 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 25 | 2026-10-25 | 34 | 64% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 197 | [x] | Jade Empire: Special Edition (GOG) | 25 | 2026-10-23 | 33 | 75% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 198 | [x] | Crab Game (STEAM) | 25 | 2026-10-22 | 33 | 77% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 199 | [x] | Goose Goose Duck (STEAM) | 25 | 2026-10-25 | 33 | 71% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 200 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-10-21 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 201 | [x] | Resident Evil (GOG) | 25 | 2026-10-20 | 27 | 62% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 202 | [x] | CarX Drift Racing Online (STEAM) | 24 | 2026-10-16 | 57 | 74% |  |
| 203 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 57 | 88% |  |
| 204 | [x] | WEBFISHING (STEAM) | 24 | 2026-10-17 | 49 | 87% |  |
| 205 | [x] | Unturned (STEAM) | 24 | 2026-10-17 | 45 | 77% |  |
| 206 | [x] | Wizard of Legend (EPIC) | 24 | 2026-10-18 | 41 | 85% |  |
| 207 | [x] | Cat Mail Co. (STEAM) | 24 | 2026-10-24 | 39 | 83% |  |
| 208 | [x] | Borderlands: The Pre-Sequel (EPIC) | 24 | 2026-10-30 | 35 | 71% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 209 | [x] | CarX Street (STEAM) | 24 | 2026-11-04 | 30 | 92% | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 210 | [x] | The Lantern of the Laughless Saint (STEAM) | 24 | 2026-11-05 | 25 | 64% | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 211 | [x] | Owlboy (STEAM) | 23 | 2026-11-02 | 53 | 50% |  |
| 212 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 23 | 2026-10-20 | 50 | 81% |  |
| 213 | [x] | Cave Story+ (EPIC) | 23 | 2026-10-18 | 48 | 85% |  |
| 214 | [x] | Goat Simulator (STEAM) | 23 | 2026-11-01 | 45 | 61% |  |
| 215 | [x] | Football Manager 2024 (EPIC) | 23 | 2026-10-20 | 42 | 93% |  |
| 216 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-10-19 | 42 | 93% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 217 | [x] | Pinball FX Classic (STEAM) | 23 | 2026-10-23 | 41 | 92% |  |
| 218 | [x] | SWORN (STEAM) | 23 | 2026-10-23 | 39 | 95% |  |
| 219 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 23 | 2026-10-17 | 37 | 75% |  |
| 220 | [x] | Timberborn (STEAM) | 23 | 2026-10-25 | 34 | 83% |  |
| 221 | [x] | Party Animals (STEAM) | 23 | 2026-10-17 | 32 | 73% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 222 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 96% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 223 | [x] | Jade Empire: Special Edition (STEAM) | 23 | 2026-11-01 | 26 | 69% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 224 | [x] | ABZÛ (STEAM) | 22 | 2026-10-21 | 52 | 97% |  |
| 225 | [x] | Hatred (STEAM) | 22 | 2026-10-22 | 45 | 88% |  |
| 226 | [x] | Life is Strange Remastered (STEAM) | 22 | 2026-10-20 | 34 | 94% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 227 | [x] | Beyond: Two Souls (STEAM) | 22 | 2026-10-22 | 30 | 71% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 228 | [x] | BlazBlue Centralfiction (STEAM) | 21 | 2026-10-17 | 60 | 81% |  |
| 229 | [x] | Titan Quest Anniversary Edition (STEAM) | 21 | 2026-10-16 | 54 | 86% |  |
| 230 | [x] | Slow Roads (STEAM) | 21 | 2026-10-22 | 46 | 94% |  |
| 231 | [x] | This War of Mine (STEAM) | 21 | 2026-10-21 | 38 | 73% |  |
| 232 | [x] | Trailmakers (STEAM) | 21 | 2026-10-21 | 38 | 93% |  |
| 233 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 21 | 2026-10-21 | 36 | 100% |  |
| 234 | [x] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 21 | 2026-11-04 | 30 | 87% | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 235 | [x] | Need for Speed™ Unbound (STEAM) | 21 | 2026-10-26 | 29 | 80% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 236 | [x] | Nex Machina (STEAM) | 21 | 2026-10-18 | 28 | 77% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 237 | [x] | Capcom Fighting Collection (STEAM) | 21 | 2026-10-23 | 26 | 79% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 238 | [x] | Saints Row IV (STEAM) | 20 | 2026-10-19 | 47 | 73% |  |
| 239 | [x] | No Rest for the Wicked (STEAM) | 20 | 2026-10-19 | 43 | 74% |  |
| 240 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-10-20 | 40 | 100% |  |
| 241 | [x] | Brothers - A Tale of Two Sons (EPIC) | 20 | 2026-10-23 | 37 | 71% |  |
| 242 | [x] | One-armed robber (STEAM) | 20 | 2026-10-23 | 37 | 81% |  |
| 243 | [x] | Tiny Glade (STEAM) | 20 | 2026-10-24 | 34 | 78% |  |
| 244 | [x] | BAJA: Edge of Control HD (STEAM) | 20 | 2026-10-28 | 27 | 90% | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 245 | [x] | Dead Island (STEAM) | 20 | 2026-10-20 | 26 | 71% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 246 | [x] | Tyr (STEAM) | 20 | 2026-11-02 | 26 | 82% | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 247 | [x] | MudRunner (EPIC) | 19 | 2026-10-18 | 41 | 94% |  |
| 248 | [x] | Mafia: Definitive Edition (STEAM) | 19 | 2026-10-28 | 36 | 75% |  |
| 249 | [x] | Killing Floor (STEAM) | 19 | 2026-10-19 | 34 | 82% |  |
| 250 | [x] | My Summer Car (STEAM) | 19 | 2026-10-30 | 34 | 86% |  |
| 251 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 19 | 2026-10-21 | 33 | 71% |  |
| 252 | [x] | Stick It to the Stickman (STEAM) | 19 | 2026-10-17 | 33 | 74% |  |
| 253 | [x] | Metro Exodus (STEAM) | 19 | 2026-10-20 | 31 | 90% |  |
| 254 | [x] | Sonic and SEGA All Stars Racing (STEAM) | 19 | 2026-10-19 | 28 | 70% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 255 | [x] | Torchlight II (EPIC) | 19 | 2026-10-22 | 27 | 94% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 256 | [x] | Katanaut (STEAM) | 19 | 2026-10-20 | 25 | 62% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 257 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 18 | 2026-10-25 | 41 | 71% |  |
| 258 | [x] | Styx: Master of Shadows (EPIC) | 18 | 2026-11-03 | 39 | 40% |  |
| 259 | [x] | Backpack Battles (STEAM) | 18 | 2026-10-21 | 37 | 100% |  |
| 260 | [x] | Faster Than Light (EPIC) | 18 | 2026-10-24 | 35 | 100% |  |
| 261 | [x] | Far Far West (STEAM) | 18 | 2026-10-21 | 32 | 78% |  |
| 262 | [x] | Tabletop Simulator (STEAM) | 18 | 2026-10-19 | 30 | 64% |  |
| 263 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 2026-10-20 | 29 | 81% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 264 | [x] | Maneater (STEAM) | 18 | 2026-10-20 | 28 | 72% |  |
| 265 | [x] | Arcade Paradise (EPIC) | 18 | 2026-10-25 | 27 | 83% |  |
| 266 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 18 | 2026-10-21 | 27 | 96% |  |
| 267 | [x] | DOOM 3: BFG Edition (GOG) | 18 | 2026-10-19 | 25 | 79% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 268 | [x] | Dorfromantik (GOG) | 18 | 2026-11-04 | 23 | 70% | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 269 | [x] | Crusader Kings III (STEAM) | 18 | 2026-11-01 | 23 | 69% | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 270 | [x] | Graveyard Keeper (GOG) | 17 | 2026-10-25 | 37 | 18% |  |
| 271 | [x] | Kingdom Come: Deliverance II (STEAM) | 17 | 2026-10-20 | 36 | 100% |  |
| 272 | [x] | Mini Metro (STEAM) | 17 | 2026-11-01 | 36 | 48% |  |
| 273 | [x] | Paper Lily - Chapter 1 (STEAM) | 17 | 2026-10-27 | 35 | 94% |  |
| 274 | [x] | Spin Rhythm XD (STEAM) | 17 | 2026-10-18 | 35 | 85% |  |
| 275 | [x] | SKALD: Against the Black Priory (STEAM) | 17 | 2026-10-20 | 34 | 97% |  |
| 276 | [x] | SCP – Containment Breach (STEAM) | 17 | 2026-10-27 | 32 | 85% |  |
| 277 | [x] | GRANDIA HD Remaster (STEAM) | 17 | 2026-10-22 | 31 | 76% |  |
| 278 | [x] | GRIP: Combat Racing (STEAM) | 17 | 2026-10-20 | 31 | 82% |  |
| 279 | [x] | Shank 2 (STEAM) | 17 | 2026-11-06 | 31 | 100% |  |
| 280 | [x] | Grim Fandango Remastered (GOG) | 17 | 2026-11-03 | 25 | 60% | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 281 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 17 | 2026-10-21 | 23 | 82% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 282 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 17 | 2026-10-23 | 22 | 93% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 283 | [x] | Command & Conquer™ Red Alert™ 3 (STEAM) | 17 | 2026-10-27 | 22 | 69% | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 284 | [x] | Farming Simulator 25 (STEAM) | 17 | 2026-10-21 | 21 | 79% |  |
| 285 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 51 | 100% |  |
| 286 | [x] | No Man's Sky (GOG) | 16 | 2026-10-19 | 37 | 76% |  |
| 287 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 16 | 2026-10-20 | 34 | 76% |  |
| 288 | [x] | DNF Duel (EPIC) | 16 | 2026-10-21 | 29 | 91% |  |
| 289 | [x] | Titanfall® 2 (STEAM) | 16 | 2026-10-16 | 29 | 77% |  |
| 290 | [x] | Dishonored 2 (STEAM) | 16 | 2026-10-20 | 26 | 92% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 291 | [x] | LET IT DIE (STEAM) | 16 | 2026-10-25 | 26 | 73% |  |
| 292 | [x] | Legend of Grimrock 2 (STEAM) | 16 | 2026-11-06 | 23 | 70% | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 293 | [x] | Fall Guys (STEAM) | 16 | 2026-10-26 | 22 | 92% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 294 | [x] | EVE Online (STEAM) | 16 | 2026-11-06 | 20 | 60% | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 295 | [x] | Jotunnslayer: Hordes of Hel (STEAM) | 16 | 2026-10-30 | 20 | 92% | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 296 | [x] | Grim Fandango Remastered (STEAM) | 15 | 2026-10-19 | 36 | 76% |  |
| 297 | [x] | Railway Chai Wala (STEAM) | 15 | 2026-11-06 | 31 | n/a |  |
| 298 | [x] | Mark of the Ninja (STEAM) | 15 | 2026-10-26 | 30 | 64% |  |
| 299 | [x] | Lost Castle 2 (STEAM) | 15 | 2026-11-02 | 29 | 100% |  |
| 300 | [x] | Hitman: Absolution (GOG) | 15 | 2026-10-24 | 28 | 71% |  |
| 301 | [x] | WORLD OF FINAL FANTASY (STEAM) | 15 | 2026-10-19 | 26 | 80% |  |
| 302 | [x] | Wildermyth (STEAM) | 15 | 2026-10-26 | 26 | 94% |  |
| 303 | [x] | Mortal Shell (EPIC) | 15 | 2026-10-19 | 25 | 91% |  |
| 304 | [x] | Batman™: Arkham Origins (GOG) | 15 | 2026-10-22 | 24 | 93% |  |
| 305 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 15 | 2026-10-20 | 23 | 65% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 306 | [x] | Allumeria (STEAM) | 15 | 2026-10-23 | 22 | 80% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 307 | [x] | Chef Knight (STEAM) | 15 | 2026-10-27 | 22 | 67% |  |
| 308 | [x] | Treasure of Nadia (GOG) | 15 | 2026-11-02 | 21 | 100% | [#413](https://github.com/GameNative/gamenative-compat/issues/413) |
| 309 | [x] | Cyberpunk 2077 (EPIC) | 15 | 2026-10-19 | 20 | 81% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 310 | [x] | Maneater (EPIC) | 15 | 2026-10-28 | 20 | 83% | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 311 | [x] | Prey (GOG) | 15 | 2026-10-27 | 20 | 60% | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 312 | [x] | Far Cry® (GOG) | 14 | 2026-11-03 | 30 | 92% |  |
| 313 | [x] | Antichamber (STEAM) | 14 | 2026-10-20 | 30 | 83% |  |
| 314 | [x] | Rayman Origins (GOG) | 14 | 2026-11-02 | 29 | 56% |  |
| 315 | [x] | Human Fall Flat (STEAM) | 14 | 2026-10-29 | 28 | 64% |  |
| 316 | [x] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 2026-10-29 | 28 | 83% |  |
| 317 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 2026-10-25 | 25 | 72% |  |
| 318 | [x] | Ultrapool (STEAM) | 14 | 2026-10-24 | 25 | 100% |  |
| 319 | [x] | Gloomwood (STEAM) | 14 | 2026-10-29 | 24 | 75% |  |
| 320 | [x] | 12 is Better Than 6 (STEAM) | 14 | 2026-10-21 | 23 | 83% |  |
| 321 | [x] | Shift At Midnight (STEAM) | 14 | 2026-11-01 | 23 | 92% |  |
| 322 | [x] | Super Monkey Ball Banana Mania (STEAM) | 14 | 2026-10-18 | 23 | 64% |  |
| 323 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-10-23 | 22 | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 324 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 63% |  |
| 325 | [x] | Sons Of The Forest (STEAM) | 14 | 2026-10-19 | 22 | 74% |  |
| 326 | [x] | Realm of the Mad God Exalt (STEAM) | 14 | 2026-10-29 | 20 | 100% | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 327 | [x] | Middle-earth™: Shadow of War™ (STEAM) | 13 | 2026-10-16 | 39 | 73% |  |
| 328 | [x] | Blood: Fresh Supply (STEAM) | 13 | 2026-10-16 | 37 | 75% |  |
| 329 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 13 | 2026-10-21 | 35 | 86% |  |
| 330 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 32 | 65% |  |
| 331 | [x] | Distance (STEAM) | 13 | 2026-10-19 | 30 | 77% |  |
| 332 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 13 | 2026-10-19 | 30 | 98% |  |
| 333 | [x] | Haiku, the Robot (STEAM) | 13 | 2026-10-21 | 29 | 91% |  |
| 334 | [x] | Breath of Fire IV (GOG) | 13 | 2026-10-26 | 28 | 76% |  |
| 335 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 28 | 56% |  |
| 336 | [x] | Aperture Desk Job (STEAM) | 13 | 2026-11-03 | 27 | n/a |  |
| 337 | [x] | Lust Goddess (STEAM) | 13 | 2026-10-26 | 25 | 69% |  |
| 338 | [x] | Haydee (STEAM) | 13 | 2026-10-22 | 24 | 82% |  |
| 339 | [x] | DiRT 4 (STEAM) | 13 | 2026-10-20 | 23 | 96% |  |
| 340 | [x] | Alabaster Dawn Demo (STEAM) | 13 | 2026-10-27 | 22 | 89% |  |
| 341 | [x] | FINAL FANTASY TYPE-0 HD (STEAM) | 13 | 2026-10-28 | 21 | 64% |  |
| 342 | [x] | PAYDAY: The Heist (STEAM) | 13 | 2026-11-02 | 21 | 69% |  |
| 343 | [x] | Escape the Backrooms (STEAM) | 13 | 2026-10-25 | 20 | 93% |  |
| 344 | [x] | Horny Villa (STEAM) | 13 | 2026-10-21 | 20 | 95% |  |
| 345 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 13 | 2026-10-23 | 20 | 61% |  |
| 346 | [x] | War Thunder (STEAM) | 13 | 2026-10-21 | 20 | 80% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 347 | [x] | The WereCleaner (STEAM) | 12 | 2026-10-22 | 32 | 92% |  |
| 348 | [x] | Tom Clancy's Splinter Cell: Chaos Theory (STEAM) | 12 | 2026-10-16 | 30 | 84% |  |
| 349 | [x] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 12 | 2026-11-01 | 27 | n/a |  |
| 350 | [x] | Dead Space™ 3 (STEAM) | 12 | 2026-10-20 | 27 | 76% |  |
| 351 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 12 | 2026-10-18 | 27 | 92% |  |
| 352 | [x] | Mortal Kombat 11 (STEAM) | 12 | 2026-10-28 | 26 | 61% |  |
| 353 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 25 | 64% |  |
| 354 | [x] | Sonic Superstars (STEAM) | 12 | 2026-10-21 | 24 | 67% |  |
| 355 | [x] | NiGHTS into Dreams... (STEAM) | 12 | 2026-10-28 | 23 | 92% |  |
| 356 | [x] | Pillars of Eternity (STEAM) | 12 | 2026-10-26 | 23 | 62% |  |
| 357 | [x] | UNDEFEATED (STEAM) | 12 | 2026-11-01 | 23 | 79% |  |
| 358 | [x] | Car Mechanic Simulator 2018 (STEAM) | 12 | 2026-10-22 | 22 | 91% |  |
| 359 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 2026-10-26 | 22 | 88% |  |
| 360 | [x] | FATE (STEAM) | 12 | 2026-11-01 | 21 | 91% |  |
| 361 | [x] | Jazz Jackrabbit 2: The Secret Files (GOG) | 12 | 2026-11-05 | 20 | 100% |  |
| 362 | [x] | Commander Keen Complete Pack (STEAM) | 12 | 2026-10-28 | 20 | 100% |  |
| 363 | [x] | Divinity: Original Sin (Classic) (STEAM) | 11 | 2026-10-16 | 26 | 77% |  |
| 364 | [x] | Lara Croft and the Temple of Osiris (STEAM) | 11 | 2026-10-27 | 24 | 83% |  |
| 365 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 23 | 76% |  |
| 366 | [x] | Castle in the Clouds (STEAM) | 11 | 2026-10-21 | 22 | 83% |  |
| 367 | [x] | Injustice™ 2 (STEAM) | 11 | 2026-10-17 | 22 | 73% |  |
| 368 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 11 | 2026-10-25 | 21 | 94% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 369 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 11 | 2026-10-24 | 21 | 72% |  |
| 370 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 371 | [x] | TowerFall Ascension (STEAM) | 10 | 2026-10-16 | 31 | 59% |  |
| 372 | [x] | Possessor(s) (STEAM) | 10 | 2026-10-24 | 27 | 100% |  |
| 373 | [x] | F1 2015 (STEAM) | 10 | 2026-11-05 | 25 | 80% |  |
| 374 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 10 | 2026-10-20 | 25 | 79% |  |
| 375 | [x] | Mina the Hollower (GOG) | 10 | 2026-10-28 | 22 | 53% |  |
| 376 | [x] | SteamWorld Heist (GOG) | 10 | 2026-10-25 | 22 | n/a |  |
| 377 | [x] | Poly Bridge (STEAM) | 10 | 2026-10-26 | 22 | 95% |  |
| 378 | [x] | Sid Meier's Civilization VI (EPIC) | 10 | 2026-10-19 | 21 | 90% |  |
| 379 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 83% |  |
| 380 | [x] | Coromon (GOG) | 10 | 2026-10-19 | 20 | 63% |  |
| 381 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 382 | [x] | Pathologic Classic HD (STEAM) | 10 | 2026-10-28 | 20 | 86% |  |
| 383 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 10 | 2026-10-23 | 20 | 93% |  |
| 384 | [x] | Delver (STEAM) | 9 | 2026-10-17 | 22 | 81% |  |
| 385 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 9 | 2026-10-23 | 21 | 71% |  |
| 386 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 9 | 2026-10-21 | 20 | 92% |  |
| 387 | [x] | Football Manager 2024 (STEAM) | 9 | 2026-10-16 | 20 | n/a |  |
| 388 | [x] | Intravenous (STEAM) | 9 | 2026-10-16 | 20 | 95% |  |
| 389 | [x] | Quake III Arena (STEAM) | 9 | 2026-11-03 | 20 | 14% |  |
| 390 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 9 | 2026-10-20 | 20 | n/a |  |
| 391 | [x] | Gloomhaven (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 392 | [x] | What Remains of Edith Finch (STEAM) | 7 | 2026-10-19 | 24 | 50% |  |
| 393 | [x] | DRAGON BALL XENOVERSE (STEAM) | 7 | 2026-10-28 | 20 | 58% |  |
| 394 | [x] | Mafia II: Definitive Edition (STEAM) | 7 | 2026-10-16 | 20 | n/a |  |
| 395 | [x] | Alex Kidd in Miracle World DX (STEAM) | 2 | 2026-10-16 | 36 | 88% |  |
