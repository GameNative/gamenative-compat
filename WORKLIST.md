# GameNative compatibility worklist

Generated: `2026-10-26T04:15:05.353Z` · App release: `1.3.0` · Ratings since: `2026-07-28T04:15:05.353Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 308 |
| Probably does not work | 102 |
| First launch fails | 350 |
| Mixed | 453 |
| Works | 1007 |
| Total | 2220 |

## Does not work (308)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [x] 2026-10-18 | Project Zomboid (STEAM) | 667 | 710 | 93% (1.3.0) | Does not open (68%) | 45% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 2 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 269 | 287 | 94% (90d) | Does not open (75%) | 10% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 3 | [x] 2026-10-18 | Alan Wake (STEAM) | 253 | 262 | 92% (1.3.0) | Does not open (87%) | 10% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 4 | [ ] | Counter-Strike 2 (STEAM) | 227 | 313 | 85% (1.3.0) | Does not open (60%) | 42% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 5 | [x] 2026-10-18 | Call of Duty: Black Ops (STEAM) | 224 | 234 | 96% (90d) | Does not open (76%) | 15% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 6 | [ ] | DRAGON BALL FighterZ (STEAM) | 219 | 247 | 77% (1.3.0) | Does not open (87%) | 56% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 7 | [ ] | skate. (STEAM) | 218 | 233 | 90% (14d) | Does not open (81%) | 22% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 8 | [x] 2026-10-18 | Spelunky 2 (STEAM) | 212 | 224 | 71% (14d) | Does not open (71%) | 40% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 9 | [ ] | Garry's Mod (STEAM) | 199 | 326 | 70% (1.3.0) | Does not open (79%) | 55% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 10 | [x] 2026-10-18 | Sid Meier's Civilization V (STEAM) | 188 | 200 | 94% (90d) | Does not open (77%) | 46% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 11 | [ ] | Necesse (STEAM) | 187 | 196 | 95% (90d) | Does not open (81%) | 53% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 12 | [ ] | Prototype (STEAM) | 173 | 230 | 75% (90d) | Does not open (76%) | 45% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 13 | [ ] | Peggle Deluxe (STEAM) | 160 | 190 | 84% (90d) | Does not open (91%) | 44% | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 14 | [ ] | HELLDIVERS™ 2 (STEAM) | 147 | 155 | 95% (90d) | Does not open (92%) | 28% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 15 | [ ] | Sol Cesto (EPIC) | 146 | 154 | 95% (90d) | Does not open (75%) | 58% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 16 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 142 | 158 | 90% (90d) | Does not open (87%) | 43% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 17 | [ ] | Assassin's Creed II (STEAM) | 137 | 143 | 96% (90d) | Does not open (79%) | 51% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 18 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 116 | 142 | 71% (1.3.0) | Does not open (71%) | 53% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 19 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 114 | 147 | 77% (14d) | Does not open (75%) | 45% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 20 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 108 | 121 | 89% (90d) | No graphics (60%) | 50% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 21 | [ ] | Dust: An Elysian Tail (STEAM) | 108 | 112 | 96% (90d) | Does not open (71%) | 10% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 22 | [ ] | Transistor (STEAM) | 108 | 108 | 100% (90d) | Does not open (78%) | 0% | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 23 | [ ] | The Witcher: Enhanced Edition (GOG) | 104 | 114 | 91% (90d) | Does not open (75%) | 11% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 24 | [ ] | Mafia II (Classic) (STEAM) | 102 | 107 | 95% (90d) | Does not open (73%) | 4% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 25 | [ ] | Saints Row: The Third (STEAM) | 101 | 102 | 99% (90d) | Does not open (80%) | n/a | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 26 | [ ] | Fall Guys (EPIC) | 99 | 111 | 89% (90d) | Does not open (73%) | 4% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 27 | [ ] | Call of Duty: Black Ops II (STEAM) | 98 | 132 | 74% (90d) | Does not open (76%) | 25% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 28 | [ ] | Burnout™ Paradise Remastered (STEAM) | 97 | 101 | 96% (90d) | Does not open (85%) | 17% | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 29 | [ ] | Black Mesa (STEAM) | 94 | 130 | 72% (90d) | Does not open (83%) | 13% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 30 | [ ] | Dead Space 2 (STEAM) | 89 | 110 | 81% (90d) | Does not open (74%) | 39% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 31 | [ ] | Saints Row 2 (STEAM) | 87 | 100 | 92% (1.3.0) | Does not open (95%) | 46% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 32 | [ ] | Duskfade (STEAM) | 87 | 89 | 98% (90d) | Does not open (95%) | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 33 | [ ] | HELLDIVERS™ (STEAM) | 86 | 99 | 87% (90d) | Does not open (62%) | 45% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 34 | [ ] | Sniper Elite 4 (STEAM) | 86 | 88 | 98% (90d) | Does not open (95%) | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 35 | [ ] | MECCHA CHAMELEON (STEAM) | 82 | 117 | 70% (90d) | Does not open (67%) | 57% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 36 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 81 | 84 | 96% (90d) | Does not open (92%) | 45% | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 37 | [ ] | Call of Duty: Black Ops II - Zombies (STEAM) | 79 | 92 | 86% (90d) | Does not open (70%) | 54% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 38 | [ ] | GRID 2 (STEAM) | 79 | 83 | 95% (90d) | Does not open (67%) | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 39 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 78 | 84 | 93% (90d) | Does not open (70%) | 0% | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 40 | [ ] | Marvel Rivals (STEAM) | 76 | 86 | 88% (90d) | Does not open (80%) | 0% | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 41 | [ ] | The Wolf Among Us (STEAM) | 76 | 84 | 90% (90d) | Does not open (68%) | 14% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 42 | [ ] | Saints Row 2 (GOG) | 74 | 88 | 84% (90d) | Does not open (95%) | 46% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 43 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 74 | 79 | 94% (90d) | Does not open (75%) | 5% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 44 | [ ] | Need for Speed™ Heat  (STEAM) | 73 | 87 | 84% (90d) | Does not open (76%) | 29% | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 45 | [ ] | Borderlands GOTY (STEAM) | 73 | 79 | 92% (90d) | Does not open (91%) | 29% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 46 | [ ] | XCOM: Enemy Unknown (STEAM) | 71 | 74 | 96% (90d) | Does not open (75%) | 9% | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 47 | [x] 2026-10-18 | Diablo® IV (STEAM) | 69 | 81 | 85% (90d) | Does not open (63%) | n/a | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 48 | [ ] | Metro 2033 (STEAM) | 67 | 83 | 81% (90d) | Does not open (66%) | 54% | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 49 | [ ] | Door Kickers 2 (STEAM) | 67 | 72 | 93% (90d) | No graphics (85%) | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 50 | [ ] | GRID (STEAM) | 66 | 82 | 80% (90d) | Does not open (54%) | 52% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 51 | [ ] | Spec Ops: The Line (STEAM) | 66 | 67 | 99% (90d) | Does not open (61%) | n/a | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 52 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 63 | 63 | 100% (90d) | No graphics (56%) | 9% | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 53 | [ ] | DOOM (2016) (GOG) | 62 | 68 | 91% (90d) | Does not open (91%) | 44% | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 54 | [ ] | Call of Duty: World at War (STEAM) | 61 | 84 | 73% (90d) | Does not open (46%) | 53% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 55 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 61 | 70 | 87% (90d) | No graphics (49%) | 24% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 56 | [ ] | Three Kingdoms : Alias (STEAM) | 61 | 65 | 94% (90d) | No graphics (98%) | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 57 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 60 | 85 | 71% (90d) | Does not open (84%) | 57% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 58 | [ ] | Spore (STEAM) | 60 | 66 | 91% (90d) | Does not open (67%) | n/a | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 59 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 58 | 71 | 82% (90d) | Does not open (90%) | 59% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 60 | [ ] | DOOM 3 (STEAM) | 58 | 66 | 88% (90d) | Does not open (89%) | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 61 | [ ] | GrandChase (STEAM) | 58 | 61 | 95% (90d) | Does not open (85%) | 10% | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 62 | [ ] | Overwatch® (STEAM) | 58 | 60 | 97% (90d) | Does not open (60%) | 18% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 63 | [ ] | Vampire Survivors (EPIC) | 56 | 78 | 72% (90d) | Does not open (64%) | 54% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 64 | [ ] | Watch_Dogs (STEAM) | 56 | 67 | 84% (90d) | Does not open (91%) | 21% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 65 | [ ] | Fortune Mill (STEAM) | 56 | 57 | 98% (90d) | Does not open (89%) | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 66 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 55 | 70 | 79% (90d) | Does not open (82%) | 30% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 67 | [ ] | Asphalt Legends  (STEAM) | 55 | 63 | 87% (90d) | Does not open (80%) | 50% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 68 | [ ] | METAL SLUG 3 (STEAM) | 55 | 63 | 87% (90d) | Does not open (89%) | 18% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 69 | [ ] | Max Payne 3 (STEAM) | 55 | 60 | 92% (90d) | Does not open (93%) | 45% | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 70 | [ ] | RoboCop: Rogue City (STEAM) | 54 | 58 | 93% (90d) | Does not open (42%) | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 71 | [ ] | South Park The Fractured But Whole (STEAM) | 54 | 54 | 100% (90d) | Does not open (68%) | 20% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 72 | [ ] | Split/Second (STEAM) | 53 | 62 | 85% (90d) | Does not open (77%) | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 73 | [ ] | Hitman: Absolution (STEAM) | 53 | 58 | 91% (90d) | Does not open (85%) | 10% | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 74 | [ ] | STAR WARS Zero Company™ (STEAM) | 53 | 55 | 96% (90d) | Does not open (64%) | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 75 | [ ] | Enshrouded (STEAM) | 53 | 54 | 98% (90d) | Does not open (92%) | 14% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 76 | [ ] | Trackmania (STEAM) | 52 | 65 | 80% (90d) | Does not open (82%) | 52% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 77 | [ ] | tModLoader (STEAM) | 52 | 60 | 87% (90d) | Does not open (83%) | 5% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 78 | [ ] | Sleeping Dogs™ (STEAM) | 52 | 59 | 88% (90d) | Does not open (83%) | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 79 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 52 | 54 | 96% (90d) | No graphics (62%) | 8% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 80 | [ ] | Sandustry (STEAM) | 50 | 61 | 82% (90d) | Does not open (73%) | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 81 | [ ] | The Survivalists (STEAM) | 50 | 52 | 96% (90d) | Does not open (98%) | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 82 | [ ] | Scott Pilgrim vs The World (STEAM) | 50 | 50 | 100% (90d) | Does not open (81%) | n/a | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 83 | [ ] | ARC Raiders (STEAM) | 49 | 54 | 91% (90d) | Does not open (93%) | 0% | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 84 | [ ] | Prince of Persia The Lost Crown (STEAM) | 49 | 54 | 91% (90d) | Does not open (94%) | 36% | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 85 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 49 | 52 | 94% (90d) | Does not open (98%) | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 86 | [ ] | DOOM Eternal (STEAM) | 48 | 50 | 96% (90d) | Does not open (69%) | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 87 | [ ] | Aliens vs. Predator (STEAM) | 47 | 52 | 90% (90d) | No graphics (53%) | 20% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 88 | [ ] | Diablo + Hellfire (GOG) | 47 | 52 | 90% (90d) | Does not open (68%) | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 89 | [ ] | STAR WARS™ Republic Commando (STEAM) | 47 | 50 | 94% (90d) | Does not open (81%) | 47% | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 90 | [ ] | State of Decay 2 (STEAM) | 46 | 65 | 71% (90d) | Does not open (93%) | 0% | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 91 | [ ] | Tales of Berseria (STEAM) | 46 | 47 | 98% (90d) | Does not open (88%) | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 92 | [ ] | Mafia: Definitive Edition (GOG) | 45 | 62 | 73% (90d) | Does not open (86%) | 29% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 93 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 45 | 46 | 98% (90d) | Does not open (82%) | 42% | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 94 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 44 | 49 | 90% (90d) | Does not open (74%) | 7% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 95 | [ ] | GOALS (STEAM) | 43 | 50 | 86% (90d) | Does not open (78%) | 31% | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 96 | [ ] | ScourgeBringer (STEAM) | 43 | 48 | 90% (90d) | Does not open (69%) | 7% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 97 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 43 | 44 | 98% (90d) | Does not open (62%) | 0% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 98 | [ ] | Need for Speed™ Rivals (STEAM) | 42 | 49 | 86% (90d) | Does not open (59%) | 33% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 99 | [ ] | Alpha Protocol (STEAM) | 42 | 46 | 91% (90d) | Does not open (71%) | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 100 | [ ] | Sir, We Have an Orc Problem (STEAM) | 41 | 48 | 85% (90d) | Does not open (86%) | n/a | [#145](https://github.com/GameNative/gamenative-compat/issues/145) |
| 101 | [ ] | Mafia (STEAM) | 41 | 46 | 89% (90d) | Does not open (66%) | 38% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 102 | [ ] | Marvel's Spider-Man 2 (STEAM) | 41 | 43 | 95% (90d) | Does not open (82%) | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 103 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 41 | 42 | 98% (90d) | Does not open (61%) | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 104 | [ ] | DJMAX RESPECT V (STEAM) | 40 | 44 | 91% (90d) | Does not open (83%) | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 105 | [ ] | Elite Dangerous (STEAM) | 40 | 43 | 93% (90d) | Does not open (79%) | 55% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 106 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 40 | 42 | 95% (90d) | Does not open (91%) | 29% | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 107 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 39 | 41 | 95% (90d) | Does not open (61%) | n/a | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 108 | [ ] | Forza Horizon 6 (STEAM) | 39 | 40 | 98% (90d) | Does not open (62%) | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 109 | [ ] | GeoGuessr Steam Edition (STEAM) | 39 | 40 | 98% (90d) | No graphics (62%) | n/a | [#154](https://github.com/GameNative/gamenative-compat/issues/154) |
| 110 | [ ] | Utopia Must Fall (STEAM) | 39 | 39 | 100% (90d) | Does not open (84%) | n/a | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 111 | [ ] | BIT.TRIP RUNNER (STEAM) | 38 | 40 | 95% (90d) | No graphics (60%) | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 112 | [ ] | Barotrauma (STEAM) | 38 | 40 | 95% (90d) | Does not open (97%) | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 113 | [ ] | CODE VEIN (STEAM) | 37 | 49 | 76% (90d) | Does not open (70%) | 29% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 114 | [ ] | Call of Duty® (STEAM) | 37 | 47 | 79% (90d) | No graphics (60%) | n/a | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 115 | [ ] | FINAL FANTASY VIII (STEAM) | 37 | 45 | 82% (90d) | Does not open (64%) | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 116 | [ ] | L.A. Noire (STEAM) | 37 | 44 | 84% (90d) | Does not open (96%) | 55% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 117 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 37 | 43 | 86% (90d) | No graphics (68%) | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 118 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 37 | 40 | 93% (90d) | Does not open (64%) | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 119 | [ ] | Dragon's Dogma 2 (STEAM) | 37 | 38 | 97% (90d) | Does not open (91%) | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 120 | [ ] | Mafia II (Classic) (GOG) | 36 | 51 | 71% (90d) | Does not open (94%) | 20% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 121 | [ ] | Beat Saber (STEAM) | 36 | 40 | 90% (90d) | Does not open (45%) | 35% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 122 | [ ] | Beholder (EPIC) | 35 | 43 | 81% (90d) | Does not open (58%) | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 123 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 35 | 40 | 88% (90d) | Does not open (69%) | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 124 | [ ] | OneShot (STEAM) | 35 | 40 | 88% (90d) | Does not open (97%) | 27% | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 125 | [ ] | BattleBit Remastered (STEAM) | 35 | 39 | 90% (90d) | Does not open (63%) | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 126 | [ ] | Death Stranding (EPIC) | 35 | 38 | 92% (90d) | Does not open (72%) | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 127 | [ ] | PRAGMATA (STEAM) | 35 | 37 | 95% (90d) | Does not open (57%) | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 128 | [ ] | The Darkness II (STEAM) | 35 | 35 | 100% (90d) | Does not open (80%) | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 129 | [ ] | Forza Horizon 5 (STEAM) | 34 | 36 | 94% (90d) | Does not open (72%) | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 130 | [ ] | Breath of Fire IV (STEAM) | 34 | 34 | 100% (90d) | Does not open (66%) | 17% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 131 | [ ] | Dark Sector (STEAM) | 33 | 45 | 73% (90d) | Does not open (67%) | 37% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 132 | [ ] | Gauntlet™  (STEAM) | 33 | 44 | 75% (90d) | Does not open (68%) | n/a | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 133 | [ ] | Wolfenstein 3D (STEAM) | 33 | 36 | 92% (90d) | Does not open (52%) | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 134 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 33 | 35 | 94% (90d) | Does not open (74%) | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 135 | [ ] | DiRT Showdown (STEAM) | 33 | 34 | 97% (90d) | Does not open (61%) | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 136 | [ ] | Rayman Legends (STEAM) | 33 | 34 | 97% (90d) | Does not open (96%) | 55% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 137 | [ ] | Umamusume: Pretty Derby (STEAM) | 33 | 34 | 97% (90d) | Does not open (81%) | n/a | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 138 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 32 | 43 | 74% (90d) | Does not open (62%) | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 139 | [ ] | Tales of Zestiria (STEAM) | 32 | 38 | 84% (90d) | Does not open (81%) | 58% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 140 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 32 | 33 | 97% (90d) | Does not open (72%) | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 141 | [ ] | Hitman: Blood Money (STEAM) | 32 | 33 | 97% (90d) | Does not open (86%) | 15% | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 142 | [ ] | Muv-Luv (STEAM) | 32 | 33 | 97% (90d) | Does not open (86%) | 45% | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 143 | [ ] | Quantum Break (STEAM) | 32 | 32 | 100% (90d) | Does not open (91%) | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 144 | [ ] | CARRION (GOG) | 31 | 38 | 82% (90d) | Does not open (76%) | n/a | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 145 | [ ] | CPM 2 (STEAM) | 31 | 38 | 82% (90d) | Does not open (91%) | 9% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 146 | [ ] | Far Cry 4 (STEAM) | 31 | 35 | 89% (90d) | Does not open (100%) | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 147 | [ ] | The Lord of the Rings: War in the North (STEAM) | 31 | 33 | 94% (90d) | Does not open (86%) | n/a | [#195](https://github.com/GameNative/gamenative-compat/issues/195) |
| 148 | [ ] | King's Bounty: The Legend (STEAM) | 31 | 32 | 97% (90d) | Does not open (100%) | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 149 | [ ] | Grand Theft Auto III - The Definitive Edition (STEAM) | 31 | 31 | 100% (90d) | Does not open (92%) | 16% | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 150 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 30 | 39 | 77% (90d) | Does not open (63%) | 58% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 151 | [ ] | Insaniquarium! Deluxe (STEAM) | 30 | 38 | 79% (90d) | Does not open (85%) | 31% | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 152 | [ ] | Magicka (STEAM) | 30 | 33 | 91% (90d) | Does not open (64%) | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 153 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 30 | 31 | 97% (90d) | Does not open (95%) | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 154 | [ ] | EA SPORTS FC™ 26 (STEAM) | 29 | 37 | 78% (90d) | Does not open (77%) | n/a | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 155 | [ ] | Subnautica 2 (STEAM) | 29 | 36 | 81% (90d) | Does not open (68%) | 50% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 156 | [ ] | Zuma Deluxe (STEAM) | 29 | 32 | 91% (90d) | Does not open (96%) | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 157 | [ ] | Borderlands 2 RU (STEAM) | 29 | 31 | 94% (90d) | Does not open (60%) | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 158 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 29 | 29 | 100% (90d) | Does not open (91%) | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 159 | [ ] | Audiosurf (STEAM) | 28 | 40 | 70% (90d) | Does not open (46%) | 43% | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 160 | [ ] | CRUEL (STEAM) | 28 | 34 | 82% (90d) | Does not open (89%) | n/a | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 161 | [ ] | Persona 5 Strikers (STEAM) | 28 | 31 | 90% (90d) | Does not open (72%) | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 162 | [ ] | Wuthering Waves (STEAM) | 28 | 30 | 93% (90d) | Does not open (78%) | n/a | [#216](https://github.com/GameNative/gamenative-compat/issues/216) |
| 163 | [ ] | WRC 7 (STEAM) | 28 | 29 | 97% (90d) | Does not open (72%) | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 164 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 28 | 28 | 100% (90d) | Does not open (62%) | n/a | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 165 | [ ] | SOMA (STEAM) | 27 | 34 | 79% (90d) | Does not open (78%) | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 166 | [ ] | skate.™ (EPIC) | 27 | 31 | 87% (90d) | Does not open (90%) | 10% | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 167 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 27 | 30 | 90% (90d) | Does not open (81%) | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 168 | [ ] | PAYDAY 2 (STEAM) | 27 | 30 | 90% (90d) | Does not open (78%) | 33% | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 169 | [ ] | Bingle Bingle (STEAM) | 27 | 28 | 96% (90d) | Does not open (82%) | n/a | [#225](https://github.com/GameNative/gamenative-compat/issues/225) |
| 170 | [ ] | Northgard: Definitive Edition (STEAM) | 27 | 28 | 96% (90d) | Does not open (96%) | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 171 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 27 | 27 | 100% (90d) | Does not open (71%) | 0% | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 172 | [ ] | Kenshi (STEAM) | 26 | 34 | 76% (90d) | Does not open (80%) | 11% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 173 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 26 | 33 | 79% (90d) | Does not open (50%) | 8% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 174 | [ ] | Singularity™ (GOG) | 26 | 31 | 84% (90d) | Does not open (100%) | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 175 | [ ] | Turing Complete (STEAM) | 26 | 29 | 90% (90d) | Does not open (91%) | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 176 | [ ] | AION 2 (STEAM) | 26 | 28 | 93% (90d) | Does not open (65%) | 11% | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 177 | [ ] | Alien Breed: Impact (STEAM) | 26 | 28 | 93% (90d) | Does not open (80%) | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 178 | [ ] | Jade Empire: Special Edition (STEAM) | 26 | 28 | 93% (90d) | Does not open (92%) | 53% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 179 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 26 | 27 | 96% (90d) | Does not open (82%) | 41% | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 180 | [ ] | Isle of Reveries (STEAM) | 26 | 26 | 100% (90d) | Does not open (95%) | 20% | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 181 | [ ] | Resident Evil Requiem (STEAM) | 26 | 26 | 100% (90d) | Does not open (76%) | n/a | [#210](https://github.com/GameNative/gamenative-compat/issues/210) |
| 182 | [ ] | Content Warning (STEAM) | 25 | 33 | 76% (90d) | Does not open (55%) | n/a | [#241](https://github.com/GameNative/gamenative-compat/issues/241) |
| 183 | [ ] | Mirror's Edge™ (GOG) | 25 | 33 | 76% (90d) | No graphics (67%) | n/a | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 184 | [ ] | Knights of Pen and Paper 2 (STEAM) | 25 | 32 | 78% (90d) | Does not open (45%) | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 185 | [ ] | The Planet Crafter (STEAM) | 25 | 31 | 81% (90d) | Does not open (48%) | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 186 | [ ] | ENDLESS Space™ 2 (STEAM) | 25 | 30 | 83% (90d) | Does not open (94%) | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 187 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 25 | 28 | 89% (90d) | Does not open (91%) | 47% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 188 | [ ] | Bionic Commando Rearmed (STEAM) | 25 | 28 | 89% (90d) | Does not open (74%) | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 189 | [ ] | Peggle Nights (STEAM) | 25 | 27 | 93% (90d) | Does not open (95%) | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 190 | [ ] | Axiom Verge 2 (STEAM) | 25 | 26 | 96% (90d) | Does not open (76%) | 13% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 191 | [ ] | Euro Truck Simulator (STEAM) | 25 | 26 | 96% (90d) | Does not open (94%) | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 192 | [ ] | Gears 5 (STEAM) | 25 | 25 | 100% (90d) | Does not open (90%) | n/a | [#264](https://github.com/GameNative/gamenative-compat/issues/264) |
| 193 | [ ] | Spiral Knights (STEAM) | 25 | 25 | 100% (90d) | Does not open (74%) | n/a | [#263](https://github.com/GameNative/gamenative-compat/issues/263) |
| 194 | [ ] | Cities: Skylines (STEAM) | 24 | 34 | 71% (90d) | Does not open (59%) | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 195 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 24 | 34 | 71% (90d) | Does not open (95%) | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 196 | [ ] | CarX Street (STEAM) | 24 | 31 | 77% (90d) | Does not open (80%) | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 197 | [ ] | Transformers: Fall of Cybertron (STEAM) | 24 | 31 | 77% (90d) | Does not open (65%) | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 198 | [ ] | The Swapper (STEAM) | 24 | 28 | 86% (90d) | Does not open (54%) | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 199 | [ ] | Melatonin (STEAM) | 24 | 25 | 96% (90d) | Does not open (60%) | 50% | [#272](https://github.com/GameNative/gamenative-compat/issues/272) |
| 200 | [ ] | My Singing Monsters (STEAM) | 23 | 29 | 79% (90d) | Does not open (82%) | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 201 | [ ] | SimCity 4 Deluxe (STEAM) | 23 | 27 | 85% (90d) | Does not open (82%) | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 202 | [ ] | Tearscape (STEAM) | 23 | 27 | 85% (90d) | Controller issues (53%) | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 203 | [ ] | Marvel's Midnight Suns (STEAM) | 23 | 26 | 88% (90d) | Does not open (76%) | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 204 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 23 | 26 | 88% (90d) | Does not open (63%) | n/a | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 205 | [ ] | They Are Billions (STEAM) | 23 | 26 | 88% (90d) | Does not open (70%) | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 206 | [ ] | Rayman Legends (EPIC) | 23 | 24 | 96% (90d) | Does not open (92%) | n/a | [#286](https://github.com/GameNative/gamenative-compat/issues/286) |
| 207 | [ ] | Marie's Adventure (STEAM) | 23 | 23 | 100% (90d) | Does not open (100%) | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 208 | [ ] | Beat Cop (STEAM) | 22 | 30 | 73% (90d) | Does not open (76%) | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 209 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 22 | 28 | 79% (90d) | Does not open (64%) | n/a | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 210 | [ ] | Beyond Good & Evil™ (GOG) | 22 | 27 | 81% (90d) | Does not open (100%) | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 211 | [ ] | Half-Life: Blue Shift (STEAM) | 22 | 27 | 81% (90d) | Does not open (85%) | n/a | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 212 | [ ] | PICO PARK:Classic Edition (STEAM) | 22 | 26 | 85% (90d) | Does not open (90%) | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 213 | [ ] | Tom Clancy's Ghost Recon® Wildlands (STEAM) | 22 | 26 | 85% (90d) | Does not open (94%) | n/a | [#280](https://github.com/GameNative/gamenative-compat/issues/280) |
| 214 | [ ] | Halo: Spartan Assault (STEAM) | 22 | 25 | 88% (90d) | Does not open (80%) | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 215 | [ ] | Assassin's Creed Rogue (STEAM) | 22 | 24 | 92% (90d) | Does not open (63%) | n/a | [#271](https://github.com/GameNative/gamenative-compat/issues/271) |
| 216 | [ ] | The Lantern of the Laughless Saint (STEAM) | 22 | 23 | 96% (90d) | Does not open (79%) | n/a | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 217 | [ ] | Watch Dogs (EPIC) | 22 | 22 | 100% (90d) | Does not open (89%) | n/a | [#289](https://github.com/GameNative/gamenative-compat/issues/289) |
| 218 | [ ] | Aggelos 2 (STEAM) | 21 | 26 | 81% (90d) | No graphics (90%) | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 219 | [ ] | Command & Conquer™ Red Alert™ 3 (STEAM) | 21 | 26 | 81% (90d) | Does not open (50%) | n/a | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 220 | [ ] | Apex Legends (STEAM) | 21 | 24 | 88% (90d) | Does not open (79%) | n/a | [#261](https://github.com/GameNative/gamenative-compat/issues/261) |
| 221 | [ ] | Dragon Age™ Inquisition (STEAM) | 21 | 24 | 88% (90d) | Does not open (76%) | 40% | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 222 | [ ] | Sapphire Safari (GOG) | 21 | 24 | 88% (90d) | Does not open (89%) | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 223 | [ ] | Need for Speed: Undercover (STEAM) | 21 | 23 | 91% (90d) | Does not open (88%) | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 224 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 21 | 23 | 91% (90d) | Does not open (90%) | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 225 | [ ] | Chronicles of the Wolf (STEAM) | 21 | 22 | 95% (90d) | No graphics (85%) | n/a | [#314](https://github.com/GameNative/gamenative-compat/issues/314) |
| 226 | [ ] | Hell Yeah! (STEAM) | 21 | 22 | 95% (90d) | Does not open (81%) | n/a | [#297](https://github.com/GameNative/gamenative-compat/issues/297) |
| 227 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 21 | 22 | 95% (90d) | Does not open (69%) | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 228 | [ ] | No More Room in Hell (STEAM) | 21 | 22 | 95% (90d) | Does not open (95%) | n/a | [#365](https://github.com/GameNative/gamenative-compat/issues/365) |
| 229 | [ ] | Pathway (EPIC) | 21 | 22 | 95% (90d) | Does not open (58%) | n/a | [#298](https://github.com/GameNative/gamenative-compat/issues/298) |
| 230 | [ ] | The Last of Us™ Part I (STEAM) | 21 | 22 | 95% (90d) | Does not open (87%) | n/a | [#300](https://github.com/GameNative/gamenative-compat/issues/300) |
| 231 | [ ] | Resident Evil 3 Nemesis (1999) (STEAM) | 21 | 21 | 100% (90d) | Does not open (86%) | n/a | [#273](https://github.com/GameNative/gamenative-compat/issues/273) |
| 232 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 21 | 21 | 100% (90d) | Does not open (71%) | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 233 | [ ] | Fishing Planet (STEAM) | 20 | 28 | 71% (90d) | Does not open (93%) | 33% | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 234 | [ ] | Dungeon Keeper™ 2 (GOG) | 20 | 27 | 74% (90d) | Does not open (100%) | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 235 | [ ] | TEKKEN 8 (STEAM) | 20 | 27 | 74% (90d) | Does not open (88%) | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 236 | [ ] | Yuppie Psycho (STEAM) | 20 | 27 | 74% (90d) | Does not open (76%) | n/a | [#325](https://github.com/GameNative/gamenative-compat/issues/325) |
| 237 | [ ] | Surviving Mars (STEAM) | 20 | 26 | 77% (90d) | Does not open (92%) | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 238 | [ ] | BAJA: Edge of Control HD (STEAM) | 20 | 25 | 80% (90d) | Does not open (100%) | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 239 | [ ] | Assassin's Creed Brotherhood (STEAM) | 20 | 23 | 87% (90d) | Does not open (78%) | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 240 | [ ] | Mafia III: Definitive Edition (STEAM) | 20 | 23 | 87% (90d) | Does not open (95%) | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 241 | [ ] | The Elder Scrolls IV: Oblivion Remastered (STEAM) | 20 | 23 | 87% (90d) | Does not open (56%) | n/a | [#312](https://github.com/GameNative/gamenative-compat/issues/312) |
| 242 | [ ] | Fallen Aces (STEAM) | 20 | 22 | 91% (90d) | No graphics (80%) | n/a | [#250](https://github.com/GameNative/gamenative-compat/issues/250) |
| 243 | [ ] | Combat Master (STEAM) | 20 | 21 | 95% (90d) | Does not open (76%) | n/a | [#262](https://github.com/GameNative/gamenative-compat/issues/262) |
| 244 | [ ] | Grounded 2 (STEAM) | 20 | 21 | 95% (90d) | Does not open (56%) | n/a | [#317](https://github.com/GameNative/gamenative-compat/issues/317) |
| 245 | [ ] | Meowgic (STEAM) | 20 | 21 | 95% (90d) | Does not open (90%) | n/a | [#342](https://github.com/GameNative/gamenative-compat/issues/342) |
| 246 | [ ] | Mirror's Edge™ Catalyst (STEAM) | 20 | 21 | 95% (90d) | Does not open (67%) | 50% | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 247 | [ ] | Tom Clancy's Splinter Cell Blacklist (STEAM) | 20 | 21 | 95% (90d) | Does not open (87%) | n/a | [#367](https://github.com/GameNative/gamenative-compat/issues/367) |
| 248 | [ ] | Downfall - A Slay the Spire Fan Expansion (STEAM) | 20 | 20 | 100% (90d) | Does not open (68%) | n/a | [#320](https://github.com/GameNative/gamenative-compat/issues/320) |
| 249 | [ ] | Return to Castle Wolfenstein (STEAM) | 20 | 20 | 100% (90d) | Does not open (94%) | n/a | [#321](https://github.com/GameNative/gamenative-compat/issues/321) |
| 250 | [ ] | Fogpiercer (STEAM) | 19 | 26 | 73% (90d) | Does not open (79%) | n/a | [#303](https://github.com/GameNative/gamenative-compat/issues/303) |
| 251 | [ ] | Realm of the Mad God Exalt (STEAM) | 19 | 24 | 79% (90d) | Does not open (93%) | n/a | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 252 | [ ] | Rune Factory 5 (STEAM) | 19 | 24 | 79% (90d) | Does not open (84%) | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 253 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 19 | 22 | 86% (90d) | Does not open (69%) | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 254 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 19 | 22 | 86% (90d) | Does not open (79%) | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 255 | [ ] | Gothic 1 Remake (STEAM) | 19 | 21 | 90% (90d) | Directx error (44%) | n/a | [#336](https://github.com/GameNative/gamenative-compat/issues/336) |
| 256 | [ ] | Odallus: The Dark Call (STEAM) | 19 | 21 | 90% (90d) | No graphics (68%) | n/a | [#337](https://github.com/GameNative/gamenative-compat/issues/337) |
| 257 | [ ] | Call of Duty 2 (STEAM) | 19 | 20 | 95% (90d) | Does not open (80%) | n/a | [#340](https://github.com/GameNative/gamenative-compat/issues/340) |
| 258 | [ ] | Deus Ex: Invisible War (STEAM) | 19 | 20 | 95% (90d) | Does not open (80%) | n/a | [#341](https://github.com/GameNative/gamenative-compat/issues/341) |
| 259 | [ ] | FINAL FANTASY XVI (STEAM) | 19 | 20 | 95% (90d) | Does not open (94%) | n/a | [#363](https://github.com/GameNative/gamenative-compat/issues/363) |
| 260 | [ ] | GT Legends (STEAM) | 19 | 20 | 95% (90d) | Does not open (89%) | n/a | [#364](https://github.com/GameNative/gamenative-compat/issues/364) |
| 261 | [ ] | Tom Clancy's Rainbow Six Siege (STEAM) | 19 | 20 | 95% (90d) | Does not open (80%) | n/a | [#366](https://github.com/GameNative/gamenative-compat/issues/366) |
| 262 | [ ] | Devil May Cry 4 Special Edition (GOG) | 18 | 25 | 72% (90d) | Does not open (67%) | n/a | [#391](https://github.com/GameNative/gamenative-compat/issues/391) |
| 263 | [ ] | Grim Fandango Remastered (GOG) | 18 | 24 | 75% (90d) | No graphics (70%) | n/a | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 264 | [ ] | Sid Meier's Pirates! (STEAM) | 18 | 24 | 75% (90d) | Does not open (92%) | n/a | [#293](https://github.com/GameNative/gamenative-compat/issues/293) |
| 265 | [ ] | Spark the Electric Jester (STEAM) | 18 | 24 | 75% (90d) | Does not open (63%) | 57% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 266 | [ ] | We Were Here Together (EPIC) | 18 | 24 | 75% (90d) | Does not open (82%) | n/a | [#374](https://github.com/GameNative/gamenative-compat/issues/374) |
| 267 | [ ] | Portal: First Slice (STEAM) | 18 | 23 | 78% (90d) | Does not open (92%) | n/a | [#354](https://github.com/GameNative/gamenative-compat/issues/354) |
| 268 | [ ] | Tyr (STEAM) | 18 | 23 | 78% (90d) | Does not open (36%) | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 269 | [ ] | Yakuza 0 (GOG) | 18 | 23 | 78% (90d) | Does not open (67%) | n/a | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 270 | [ ] | Bejeweled 2 Deluxe (STEAM) | 18 | 22 | 82% (90d) | Does not open (93%) | n/a | [#329](https://github.com/GameNative/gamenative-compat/issues/329) |
| 271 | [ ] | Definitely Not Fried Chicken (EPIC) | 18 | 22 | 82% (90d) | Does not open (67%) | n/a | [#356](https://github.com/GameNative/gamenative-compat/issues/356) |
| 272 | [ ] | Dorfromantik (GOG) | 18 | 22 | 82% (90d) | Does not open (94%) | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 273 | [ ] | Genshin Impact (EPIC) | 18 | 22 | 82% (90d) | Does not open (85%) | n/a | [#326](https://github.com/GameNative/gamenative-compat/issues/326) |
| 274 | [ ] | The Last Stand: Aftermath (STEAM) | 18 | 22 | 82% (90d) | No graphics (50%) | n/a | [#324](https://github.com/GameNative/gamenative-compat/issues/324) |
| 275 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 18 | 22 | 82% (90d) | Does not open (100%) | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 276 | [ ] | Crusader Kings III (STEAM) | 18 | 21 | 86% (90d) | No graphics (64%) | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 277 | [ ] | Just Cause 4 (EPIC) | 18 | 21 | 86% (90d) | Does not open (78%) | n/a | [#383](https://github.com/GameNative/gamenative-compat/issues/383) |
| 278 | [ ] | NBA 2K26 (STEAM) | 18 | 21 | 86% (90d) | Does not open (83%) | n/a | [#384](https://github.com/GameNative/gamenative-compat/issues/384) |
| 279 | [ ] | Sacred Gold (STEAM) | 18 | 21 | 86% (90d) | Does not open (93%) | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 280 | [ ] | Battlefield™ 6 (STEAM) | 18 | 20 | 90% (90d) | Does not open (80%) | n/a | [#335](https://github.com/GameNative/gamenative-compat/issues/335) |
| 281 | [ ] | Clive Barker's Undying (GOG) | 18 | 20 | 90% (90d) | Does not open (67%) | n/a | [#388](https://github.com/GameNative/gamenative-compat/issues/388) |
| 282 | [ ] | F.E.A.R. 3 (STEAM) | 18 | 20 | 90% (90d) | No graphics (86%) | n/a | [#362](https://github.com/GameNative/gamenative-compat/issues/362) |
| 283 | [ ] | Mafia II: Definitive Edition (GOG) | 18 | 20 | 90% (90d) | No graphics (56%) | 38% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 284 | [ ] | STALZONE (STEAM) | 18 | 20 | 90% (90d) | Does not open (100%) | n/a | [#338](https://github.com/GameNative/gamenative-compat/issues/338) |
| 285 | [ ] | Assassin's Creed Odyssey (STEAM) | 17 | 24 | 71% (90d) | Does not open (75%) | n/a | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 286 | [ ] | Carnal Instinct (STEAM) | 17 | 24 | 71% (90d) | Does not open (57%) | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 287 | [ ] | Darksiders Warmastered Edition (EPIC) | 17 | 23 | 74% (90d) | Does not open (83%) | 33% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 288 | [ ] | SlashZero Demo (STEAM) | 17 | 22 | 77% (90d) | Does not open (75%) | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 289 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 17 | 22 | 77% (90d) | Does not open (87%) | n/a | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 290 | [ ] | EVE Online (STEAM) | 17 | 21 | 81% (90d) | No graphics (53%) | n/a | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 291 | [ ] | Grand Theft Auto: San Andreas - The Definitive Edition (STEAM) | 17 | 21 | 81% (90d) | Does not open (67%) | 25% | [#357](https://github.com/GameNative/gamenative-compat/issues/357) |
| 292 | [ ] | Resident Evil Requiem - Demo (STEAM) | 17 | 21 | 81% (90d) | No graphics (89%) | n/a | [#379](https://github.com/GameNative/gamenative-compat/issues/379) |
| 293 | [ ] | shapez (STEAM) | 17 | 21 | 81% (90d) | Does not open (62%) | n/a | [#332](https://github.com/GameNative/gamenative-compat/issues/332) |
| 294 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (90d) | No graphics (82%) | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 295 | [ ] | Tyrian 2000 (GOG) | 17 | 20 | 85% (90d) | Does not open (87%) | n/a | [#360](https://github.com/GameNative/gamenative-compat/issues/360) |
| 296 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 16 | 23 | 70% (90d) | No graphics (56%) | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 297 | [ ] | Hitman 3: Contracts (GOG) | 16 | 22 | 73% (90d) | Does not open (93%) | n/a | [#401](https://github.com/GameNative/gamenative-compat/issues/401) |
| 298 | [ ] | Re-Volt (STEAM) | 16 | 22 | 73% (90d) | Controller issues (71%) | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 299 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 16 | 21 | 76% (90d) | No graphics (67%) | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 300 | [ ] | Make Way (EPIC) | 16 | 21 | 76% (90d) | Does not open (73%) | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 301 | [ ] | Once Human (STEAM) | 16 | 20 | 80% (90d) | Does not open (63%) | n/a | [#395](https://github.com/GameNative/gamenative-compat/issues/395) |
| 302 | [ ] | Prey (GOG) | 16 | 20 | 80% (90d) | Does not open (38%) | n/a | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 303 | [ ] | Fallout Classic (GOG) | 15 | 21 | 71% (90d) | Does not open (71%) | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 304 | [ ] | Hob (STEAM) | 15 | 21 | 71% (90d) | Does not open (64%) | 53% | [#416](https://github.com/GameNative/gamenative-compat/issues/416) |
| 305 | [ ] | Jurassic World Evolution 2 (STEAM) | 15 | 21 | 71% (90d) | Does not open (45%) | n/a | [#448](https://github.com/GameNative/gamenative-compat/issues/448) |
| 306 | [ ] | Smushi Come Home (GOG) | 15 | 21 | 71% (90d) | Does not open (57%) | n/a | [#465](https://github.com/GameNative/gamenative-compat/issues/465) |
| 307 | [ ] | Maneater (EPIC) | 15 | 20 | 75% (90d) | Does not open (73%) | n/a | [#466](https://github.com/GameNative/gamenative-compat/issues/466) |
| 308 | [ ] | DayZ (STEAM) | 14 | 20 | 70% (90d) | Does not open (50%) | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |

## Probably does not work (102)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 170 | 284 | 60% (90d) | Does not open (77%) | n/a |  |
| 2 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 147 | 182 | 52% (1.3.0) | Does not open (95%) | 40% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 3 | [ ] | Metro 2033 Redux (STEAM) | 137 | 346 | 56% (1.3.0) | Does not open (68%) | 53% |  |
| 4 | [ ] | Euro Truck Simulator 2 (STEAM) | 123 | 216 | 58% (1.3.0) | Does not open (67%) | 59% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 5 | [ ] | Geometry Dash (STEAM) | 112 | 401 | 62% (1.3.0) | Does not open (67%) | 41% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 6 | [ ] | VRChat (STEAM) | 88 | 133 | 66% (90d) | Does not open (64%) | 40% |  |
| 7 | [ ] | Hollow Knight: Silksong (GOG) | 74 | 113 | 65% (90d) | Does not open (69%) | 48% |  |
| 8 | [ ] | Stardew Valley (GOG) | 65 | 112 | 58% (90d) | Controller issues (45%) | 58% |  |
| 9 | [ ] | Gorilla Tag (STEAM) | 64 | 107 | 60% (90d) | Does not open (78%) | 24% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 10 | [ ] | Mini Motorways (STEAM) | 54 | 96 | 56% (90d) | Does not open (75%) | 57% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 11 | [ ] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 54 | 93 | 58% (90d) | Does not open (63%) | 58% |  |
| 12 | [ ] | Oxygen Not Included (STEAM) | 52 | 86 | 60% (90d) | Does not open (69%) | 50% |  |
| 13 | [ ] | Breathedge (STEAM) | 50 | 74 | 68% (90d) | Does not open (63%) | 42% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 14 | [ ] | VALORANT (EPIC) | 49 | 76 | 64% (90d) | Does not open (82%) | 18% |  |
| 15 | [ ] | Frostpunk (STEAM) | 48 | 75 | 64% (90d) | No graphics (78%) | 53% |  |
| 16 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 43 | 76 | 57% (90d) | Does not open (73%) | 52% |  |
| 17 | [ ] | Fallout (GOG) | 43 | 62 | 69% (90d) | Does not open (71%) | 52% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 18 | [ ] | Age of Empires II (2013) (STEAM) | 40 | 66 | 61% (90d) | Does not open (50%) | 52% |  |
| 19 | [ ] | Grim Dawn (GOG) | 39 | 65 | 60% (90d) | Does not open (63%) | 50% | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 20 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 39 | 64 | 61% (90d) | Does not open (92%) | 44% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 21 | [ ] | XCOM 2 (STEAM) | 36 | 55 | 65% (90d) | Does not open (57%) | n/a |  |
| 22 | [ ] | Battle Brothers (STEAM) | 36 | 53 | 68% (90d) | Does not open (78%) | 57% |  |
| 23 | [ ] | Sol Cesto (STEAM) | 35 | 54 | 65% (90d) | Does not open (69%) | 50% |  |
| 24 | [ ] | Journey (STEAM) | 34 | 68 | 50% (90d) | Does not open (68%) | 51% |  |
| 25 | [ ] | Hero Siege (STEAM) | 33 | 57 | 58% (90d) | Graphics glitches (52%) | 59% |  |
| 26 | [ ] | Deponia (STEAM) | 32 | 61 | 52% (90d) | Does not open (48%) | 55% |  |
| 27 | [ ] | Crazy Taxi (STEAM) | 28 | 42 | 67% (90d) | Does not open (68%) | 40% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 28 | [ ] | Soul's Remnant (STEAM) | 27 | 49 | 55% (90d) | Does not open (55%) | n/a |  |
| 29 | [ ] | Lucid Blocks (STEAM) | 27 | 46 | 59% (90d) | Does not open (83%) | n/a |  |
| 30 | [ ] | Strider (STEAM) | 27 | 40 | 68% (90d) | Does not open (100%) | 36% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 31 | [ ] | Yume Nikki (STEAM) | 26 | 44 | 59% (90d) | Does not open (92%) | 0% |  |
| 32 | [ ] | Baldur's Gate: Enhanced Edition (STEAM) | 24 | 48 | 50% (90d) | Does not open (61%) | 26% |  |
| 33 | [ ] | Goat Simulator (STEAM) | 24 | 44 | 55% (90d) | Does not open (58%) | 52% |  |
| 34 | [ ] | Mafia: Definitive Edition (STEAM) | 23 | 42 | 55% (90d) | Does not open (81%) | n/a |  |
| 35 | [ ] | Opus Magnum (STEAM) | 23 | 37 | 62% (90d) | Does not open (81%) | n/a |  |
| 36 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 23 | 34 | 68% (90d) | Does not open (81%) | n/a |  |
| 37 | [ ] | Owlboy (STEAM) | 22 | 41 | 54% (90d) | Does not open (81%) | 50% |  |
| 38 | [ ] | Invisible, Inc. (STEAM) | 22 | 39 | 56% (90d) | Does not open (70%) | 50% |  |
| 39 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 21 | 39 | 54% (90d) | No graphics (60%) | 39% |  |
| 40 | [ ] | My Summer Car (STEAM) | 20 | 37 | 54% (90d) | Does not open (53%) | n/a |  |
| 41 | [ ] | Paper Lily - Chapter 1 (STEAM) | 20 | 36 | 56% (90d) | Does not open (72%) | n/a |  |
| 42 | [ ] | GOD EATER RESURRECTION (STEAM) | 20 | 31 | 65% (90d) | Does not open (50%) | 50% |  |
| 43 | [ ] | Another World: 20th Anniversary Edition (GOG) | 20 | 30 | 67% (90d) | Does not open (71%) | n/a |  |
| 44 | [ ] | Agatha Knife (AMAZON) | 20 | 29 | 69% (90d) | Graphics glitches (65%) | n/a | [#290](https://github.com/GameNative/gamenative-compat/issues/290) |
| 45 | [ ] | No More Heroes (STEAM) | 19 | 36 | 53% (90d) | No graphics (67%) | n/a |  |
| 46 | [ ] | Turnip Boy Robs a Bank (EPIC) | 19 | 28 | 68% (90d) | Does not open (65%) | 42% | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 47 | [ ] | SCP – Containment Breach (STEAM) | 18 | 35 | 51% (90d) | Does not open (83%) | n/a |  |
| 48 | [ ] | Lost Castle 2 (STEAM) | 18 | 34 | 53% (90d) | Does not open (64%) | n/a |  |
| 49 | [ ] | Legend of Grimrock 2 (STEAM) | 18 | 26 | 69% (90d) | Does not open (80%) | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 50 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 17 | 33 | 52% (90d) | Does not open (88%) | n/a |  |
| 51 | [ ] | Shank 2 (STEAM) | 17 | 30 | 57% (90d) | Does not open (82%) | n/a |  |
| 52 | [ ] | Guacamelee! Gold Edition (STEAM) | 17 | 28 | 61% (90d) | Does not open (93%) | n/a | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 53 | [ ] | Race The Sun (STEAM) | 17 | 28 | 61% (90d) | No graphics (92%) | n/a |  |
| 54 | [ ] | Alabaster Dawn Demo (STEAM) | 17 | 26 | 65% (90d) | Controller issues (71%) | n/a |  |
| 55 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 17 | 25 | 68% (90d) | Does not open (80%) | n/a |  |
| 56 | [ ] | Blaster Master Zero (STEAM) | 16 | 29 | 55% (90d) | Does not open (63%) | n/a |  |
| 57 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 16 | 27 | 59% (90d) | Does not open (80%) | n/a |  |
| 58 | [ ] | Foretales (EPIC) | 16 | 26 | 62% (90d) | Does not open (50%) | n/a | [#451](https://github.com/GameNative/gamenative-compat/issues/451) |
| 59 | [ ] | Aperture Desk Job (STEAM) | 15 | 30 | 50% (90d) | Does not open (62%) | n/a |  |
| 60 | [ ] | Evoland (STEAM) | 15 | 29 | 52% (90d) | Controller issues (71%) | n/a |  |
| 61 | [ ] | Spilled! (STEAM) | 15 | 25 | 60% (90d) | Graphics glitches (67%) | n/a |  |
| 62 | [ ] | War of Dots (STEAM) | 15 | 25 | 60% (90d) | Does not open (71%) | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 63 | [ ] | Blood Omen: Legacy of Kain (GOG) | 15 | 23 | 65% (90d) | Does not open (64%) | 43% |  |
| 64 | [ ] | Human Resource Machine (EPIC) | 15 | 23 | 65% (90d) | No graphics (67%) | n/a |  |
| 65 | [ ] | Chef Knight (STEAM) | 15 | 22 | 68% (90d) | Does not open (93%) | n/a |  |
| 66 | [ ] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 14 | 28 | 50% (90d) | Does not open (100%) | 50% |  |
| 67 | [ ] | NiGHTS into Dreams... (STEAM) | 14 | 27 | 52% (90d) | Does not open (45%) | n/a |  |
| 68 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 26 | 54% (90d) | Controller issues (54%) | n/a |  |
| 69 | [ ] | Alan Wake's American Nightmare (EPIC) | 14 | 25 | 56% (90d) | Does not open (92%) | 42% |  |
| 70 | [ ] | Katana ZERO (GOG) | 14 | 25 | 56% (90d) | Does not open (85%) | 27% |  |
| 71 | [ ] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 14 | 24 | 58% (90d) | Does not open (93%) | 23% |  |
| 72 | [ ] | Warhammer 40,000: Boltgun (GOG) | 14 | 24 | 58% (90d) | Does not open (92%) | 50% |  |
| 73 | [ ] | Space Rangers HD: A War Apart (STEAM) | 14 | 22 | 64% (90d) | Does not open (69%) | 50% |  |
| 74 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 21 | 67% (90d) | Does not open (67%) | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 75 | [ ] | Quake III Arena (STEAM) | 13 | 26 | 50% (90d) | Does not open (70%) | n/a |  |
| 76 | [ ] | Human Fall Flat (STEAM) | 13 | 25 | 52% (90d) | Does not open (58%) | 59% |  |
| 77 | [ ] | A Plague Tale: Innocence (GOG) | 13 | 24 | 54% (90d) | Does not open (92%) | n/a |  |
| 78 | [ ] | DYNASTY WARRIORS: ORIGINS (STEAM) | 13 | 23 | 57% (90d) | Does not open (62%) | n/a |  |
| 79 | [ ] | Secret of Mana (STEAM) | 13 | 23 | 57% (90d) | Graphics glitches (58%) | n/a |  |
| 80 | [ ] | The Stanley Parable (STEAM) | 13 | 23 | 57% (90d) | Does not open (89%) | 42% |  |
| 81 | [ ] | Lara Croft and the Temple of Osiris (STEAM) | 13 | 22 | 59% (90d) | Does not open (50%) | n/a |  |
| 82 | [ ] | Evenicle (STEAM) | 13 | 21 | 62% (90d) | Graphics glitches (77%) | n/a |  |
| 83 | [ ] | PAYDAY: The Heist (STEAM) | 13 | 21 | 62% (90d) | Does not open (67%) | n/a |  |
| 84 | [ ] | Trials Survivors (STEAM) | 13 | 21 | 62% (90d) | Does not open (67%) | n/a |  |
| 85 | [ ] | XIII (GOG) | 13 | 21 | 62% (90d) | Does not open (70%) | n/a |  |
| 86 | [ ] | Buck Up And Drive! (STEAM) | 13 | 20 | 65% (90d) | Does not open (67%) | n/a |  |
| 87 | [ ] | Look Outside (GOG) | 12 | 24 | 50% (90d) | Does not open (100%) | n/a |  |
| 88 | [ ] | Grounded (STEAM) | 12 | 23 | 52% (90d) | No graphics (44%) | n/a |  |
| 89 | [ ] | UNDEFEATED (STEAM) | 12 | 23 | 52% (90d) | Does not open (78%) | n/a |  |
| 90 | [ ] | Shift At Midnight (STEAM) | 12 | 22 | 55% (90d) | Does not open (80%) | n/a |  |
| 91 | [ ] | The Excavation of Hob's Barrow (STEAM) | 12 | 21 | 57% (90d) | Controller issues (82%) | n/a |  |
| 92 | [ ] | Ys: Memories of Celceta (STEAM) | 12 | 21 | 57% (90d) | No graphics (50%) | n/a |  |
| 93 | [ ] | Commander Keen Complete Pack (STEAM) | 12 | 20 | 60% (90d) | Does not open (73%) | n/a |  |
| 94 | [ ] | Dex (GOG) | 12 | 20 | 60% (90d) | Does not open (80%) | n/a |  |
| 95 | [ ] | Drop Duchy (EPIC) | 12 | 20 | 60% (90d) | Does not open (100%) | n/a |  |
| 96 | [ ] | Crying Suns (EPIC) | 11 | 22 | 50% (90d) | No graphics (57%) | n/a |  |
| 97 | [ ] | Ratchet & Clank: Rift Apart (STEAM) | 11 | 22 | 50% (90d) | Does not open (89%) | 48% |  |
| 98 | [ ] | FATE (STEAM) | 11 | 21 | 52% (90d) | No graphics (50%) | n/a |  |
| 99 | [ ] | Pathologic Classic HD (STEAM) | 11 | 21 | 52% (90d) | No graphics (78%) | n/a |  |
| 100 | [ ] | Far Cry® (GOG) | 10 | 20 | 50% (90d) | Graphics glitches (40%) | n/a |  |
| 101 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (90d) | Does not open (56%) | n/a |  |
| 102 | [ ] | Thief™ 3: Deadly Shadows (GOG) | 10 | 20 | 50% (90d) | Does not open (70%) | n/a |  |

## Works, but the first launch usually fails (350)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 1422 | 1794 | 74% (1.3.0) | Does not open (83%) | 78% |  |
| 2 | [ ] | Grim Dawn (STEAM) | 636 | 686 | 67% (1.3.0) | Does not open (76%) | 66% |  |
| 3 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 590 | 750 | 78% (1.3.0) | Does not open (65%) | 92% |  |
| 4 | [ ] | Terraria (STEAM) | 500 | 790 | 53% (1.3.0) | No graphics (51%) | 75% |  |
| 5 | [ ] | KINGDOM HEARTS -HD 1.5+2.5 ReMIX- (STEAM) | 447 | 908 | 56% (1.3.0) | Does not open (80%) | 93% |  |
| 6 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 367 | 550 | 67% (1.3.0) | Does not open (56%) | 88% |  |
| 7 | [ ] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 287 | 326 | 77% (14d) | Does not open (86%) | 62% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 8 | [ ] | Cyberpunk 2077 (STEAM) | 241 | 411 | 54% (1.3.0) | Does not open (68%) | 75% |  |
| 9 | [ ] | BeamNG.drive (STEAM) | 232 | 286 | 85% (1.3.0) | Does not open (84%) | 91% |  |
| 10 | [ ] | Welcome to Elderfield (STEAM) | 222 | 265 | 50% (14d) | Does not open (71%) | 81% |  |
| 11 | [ ] | Palworld (STEAM) | 221 | 453 | 50% (1.3.0) | Does not open (71%) | 89% |  |
| 12 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 219 | 310 | 71% (90d) | Does not open (61%) | 89% |  |
| 13 | [ ] | OMORI (STEAM) | 213 | 257 | 57% (14d) | Does not open (64%) | 74% |  |
| 14 | [ ] | Devil May Cry HD Collection (STEAM) | 197 | 276 | 84% (1.3.0) | Does not open (87%) | 71% |  |
| 15 | [ ] | ELDEN RING (STEAM) | 192 | 289 | 74% (1.3.0) | Does not open (86%) | 69% |  |
| 16 | [ ] | MONSTER HUNTER RISE (STEAM) | 190 | 479 | 52% (1.3.0) | Does not open (79%) | 75% |  |
| 17 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 187 | 351 | 63% (1.3.0) | Does not open (61%) | 81% |  |
| 18 | [ ] | DREDGE (EPIC) | 181 | 233 | 57% (1.3.0) | Does not open (68%) | 88% |  |
| 19 | [ ] | Mirror's Edge (STEAM) | 160 | 206 | 78% (90d) | Does not open (90%) | 77% |  |
| 20 | [ ] | Noita (STEAM) | 152 | 225 | 54% (1.3.0) | Does not open (55%) | 83% |  |
| 21 | [ ] | Far Cry® 3 (STEAM) | 147 | 166 | 89% (90d) | Does not open (83%) | 63% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 22 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 141 | 162 | 86% (14d) | Does not open (85%) | 81% |  |
| 23 | [ ] | Monster Hunter: World (STEAM) | 140 | 273 | 51% (90d) | No graphics (57%) | 85% |  |
| 24 | [ ] | Team Fortress 2 (STEAM) | 140 | 231 | 68% (1.3.0) | Does not open (70%) | 81% |  |
| 25 | [ ] | Borderlands 2 (EPIC) | 136 | 157 | 86% (1.3.0) | Does not open (83%) | 64% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 26 | [ ] | Fallout: New Vegas Ultimate Edition (GOG) | 134 | 277 | 50% (1.3.0) | Does not open (55%) | 75% |  |
| 27 | [ ] | Look Outside (STEAM) | 133 | 304 | 52% (1.3.0) | Controller issues (60%) | 92% |  |
| 28 | [ ] | Castlevania Advance Collection (STEAM) | 125 | 193 | 70% (1.3.0) | Controller issues (94%) | 97% |  |
| 29 | [ ] | Cave Story+ (STEAM) | 125 | 138 | 91% (90d) | Does not open (64%) | 93% |  |
| 30 | [ ] | Fallout: New Vegas (EPIC) | 123 | 147 | 84% (90d) | Does not open (59%) | 90% |  |
| 31 | [ ] | Minecraft Dungeons II (STEAM) | 122 | 139 | 88% (90d) | Does not open (83%) | 62% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 32 | [ ] | Devil May Cry 5 (STEAM) | 120 | 192 | 54% (1.3.0) | Does not open (81%) | 63% |  |
| 33 | [ ] | Castlevania Dominus Collection (STEAM) | 120 | 175 | 79% (1.3.0) | Controller issues (93%) | 98% |  |
| 34 | [ ] | The Witcher: Enhanced Edition (STEAM) | 119 | 135 | 88% (90d) | Does not open (59%) | 60% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 35 | [ ] | Touhou Koumakyou: New Classic - the Embodiment of Scarlet Devil (STEAM) | 115 | 174 | 66% (90d) | Does not open (78%) | 83% |  |
| 36 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 115 | 152 | 76% (90d) | Does not open (86%) | 82% |  |
| 37 | [ ] | Moonstone Island (STEAM) | 113 | 147 | 77% (90d) | Controller issues (55%) | 89% |  |
| 38 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 110 | 152 | 82% (1.3.0) | Does not open (73%) | 65% |  |
| 39 | [ ] | FINAL FANTASY VIII - REMASTERED (STEAM) | 102 | 162 | 63% (90d) | Does not open (88%) | 61% |  |
| 40 | [ ] | Rise of the Tomb Raider (STEAM) | 99 | 155 | 64% (90d) | Does not open (78%) | 95% |  |
| 41 | [ ] | Aniimo (STEAM) | 99 | 137 | 72% (90d) | Does not open (77%) | 92% |  |
| 42 | [ ] | Dying Light (STEAM) | 96 | 183 | 52% (90d) | Does not open (88%) | 91% |  |
| 43 | [ ] | Fallout: New Vegas PCR (STEAM) | 96 | 134 | 72% (90d) | Does not open (92%) | 82% |  |
| 44 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 95 | 129 | 74% (90d) | Controller issues (86%) | 100% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 45 | [ ] | Cry of Fear (STEAM) | 94 | 180 | 68% (14d) | Does not open (57%) | 89% |  |
| 46 | [ ] | Happy Wheels (STEAM) | 93 | 113 | 82% (90d) | No graphics (53%) | 78% |  |
| 47 | [ ] | Vital Shell (STEAM) | 92 | 135 | 64% (14d) | Does not open (55%) | 84% |  |
| 48 | [ ] | STEINS;GATE (STEAM) | 92 | 125 | 74% (90d) | Does not open (92%) | 86% |  |
| 49 | [ ] | BioShock Remastered (EPIC) | 91 | 166 | 55% (90d) | Does not open (51%) | 85% |  |
| 50 | [ ] | Sovereign Tower (STEAM) | 90 | 142 | 63% (90d) | Does not open (82%) | 92% |  |
| 51 | [ ] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 88 | 131 | 67% (90d) | Does not open (77%) | 66% |  |
| 52 | [ ] | The Sims™ 4 (STEAM) | 85 | 103 | 83% (90d) | Does not open (88%) | 67% |  |
| 53 | [ ] | Alabaster Dawn (STEAM) | 80 | 134 | 60% (90d) | Controller issues (51%) | 92% |  |
| 54 | [ ] | Detroit: Become Human (STEAM) | 79 | 82 | 96% (90d) | Does not open (72%) | 68% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 55 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 78 | 102 | 76% (90d) | Does not open (53%) | 70% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 56 | [ ] | Sid Meier's Civilization VI (STEAM) | 77 | 132 | 55% (1.3.0) | Does not open (68%) | 88% |  |
| 57 | [ ] | Mega Man Zero/ZX Legacy Collection (STEAM) | 77 | 104 | 74% (90d) | Does not open (87%) | 92% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 58 | [ ] | Firewatch (STEAM) | 75 | 121 | 62% (90d) | Does not open (90%) | 60% |  |
| 59 | [ ] | Call of Juarez Gunslinger (STEAM) | 75 | 89 | 84% (90d) | Does not open (88%) | 68% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 60 | [ ] | Gunfire Reborn (STEAM) | 75 | 83 | 90% (90d) | Does not open (83%) | 92% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 61 | [ ] | POSTAL 2 (STEAM) | 74 | 121 | 61% (90d) | Does not open (67%) | 66% |  |
| 62 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 73 | 122 | 60% (90d) | Controller issues (60%) | 93% |  |
| 63 | [ ] | Dota 2 (STEAM) | 73 | 106 | 69% (90d) | Does not open (78%) | 76% |  |
| 64 | [ ] | Darksiders (STEAM) | 73 | 89 | 82% (90d) | Does not open (68%) | 100% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 65 | [ ] | Need for Speed: Hot Pursuit (STEAM) | 72 | 100 | 72% (90d) | Does not open (72%) | 83% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 66 | [ ] | Fable - The Lost Chapters (STEAM) | 70 | 109 | 52% (1.3.0) | Graphics glitches (49%) | 74% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 67 | [ ] | Fallout (STEAM) | 70 | 109 | 64% (90d) | Does not open (69%) | 77% |  |
| 68 | [ ] | Antivirus Survivors 2003 Professional (STEAM) | 69 | 102 | 68% (90d) | Does not open (62%) | 91% |  |
| 69 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 69 | 84 | 95% (14d) | Does not open (92%) | 97% |  |
| 70 | [ ] | American Truck Simulator (STEAM) | 68 | 107 | 85% (1.3.0) | Does not open (74%) | 72% |  |
| 71 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 68 | 106 | 64% (90d) | Does not open (71%) | 71% |  |
| 72 | [ ] | Borderlands: The Pre-Sequel (STEAM) | 68 | 94 | 72% (90d) | Does not open (79%) | 65% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 73 | [ ] | TBH: Task Bar Hero (STEAM) | 67 | 98 | 68% (90d) | Does not open (66%) | 95% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 74 | [ ] | Dungeons & Degenerate Gamblers (STEAM) | 67 | 90 | 74% (90d) | Does not open (90%) | 98% |  |
| 75 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 66 | 117 | 56% (90d) | Does not open (62%) | 63% |  |
| 76 | [ ] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 66 | 89 | 74% (90d) | Does not open (89%) | 80% |  |
| 77 | [ ] | Disgaea 5 Complete (STEAM) | 66 | 80 | 86% (14d) | Does not open (79%) | 96% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 78 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 65 | 88 | 74% (90d) | Does not open (54%) | 89% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 79 | [ ] | The Binding of Isaac (STEAM) | 63 | 140 | 67% (1.3.0) | Controller issues (91%) | 94% |  |
| 80 | [ ] | Poppy Playtime (STEAM) | 63 | 112 | 56% (90d) | Does not open (67%) | 81% |  |
| 81 | [ ] | Sonic Lost World (STEAM) | 63 | 102 | 62% (90d) | No graphics (58%) | 93% |  |
| 82 | [ ] | Big Walk (STEAM) | 63 | 96 | 66% (90d) | Does not open (68%) | 86% |  |
| 83 | [ ] | Ace Attorney Investigations Collection (STEAM) | 63 | 95 | 66% (90d) | Does not open (97%) | 94% |  |
| 84 | [ ] | Sonic Generations (STEAM) | 63 | 73 | 86% (90d) | Does not open (71%) | 62% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 85 | [ ] | A Plague Tale: Innocence (STEAM) | 63 | 66 | 95% (90d) | Does not open (85%) | 70% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 86 | [ ] | Path of Exile (STEAM) | 62 | 71 | 87% (90d) | Does not open (91%) | 82% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 87 | [ ] | MIO: Memories in Orbit (STEAM) | 61 | 118 | 64% (1.3.0) | Graphics glitches (53%) | 98% |  |
| 88 | [ ] | Borderlands 3 (STEAM) | 61 | 74 | 82% (90d) | Does not open (91%) | 97% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 89 | [ ] | Cyberpunk 2077 (GOG) | 61 | 74 | 82% (90d) | Does not open (80%) | 70% |  |
| 90 | [ ] | Sonic Adventure DX (STEAM) | 60 | 96 | 63% (90d) | Does not open (85%) | 67% |  |
| 91 | [ ] | Red Dead Redemption 2 (STEAM) | 60 | 79 | 62% (1.3.0) | Does not open (98%) | 84% |  |
| 92 | [ ] | eFootball™ (STEAM) | 59 | 91 | 65% (90d) | Does not open (56%) | 74% |  |
| 93 | [ ] | Dead by Daylight (STEAM) | 59 | 64 | 92% (90d) | Does not open (80%) | 80% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 94 | [ ] | Starbound (STEAM) | 57 | 82 | 70% (90d) | Does not open (72%) | 71% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 95 | [ ] | Prey (STEAM) | 56 | 91 | 62% (90d) | Does not open (65%) | 88% |  |
| 96 | [ ] | The Secret of Monkey Island: Special Edition (STEAM) | 56 | 89 | 63% (90d) | Does not open (90%) | 74% |  |
| 97 | [ ] | Guildrun Demo (STEAM) | 56 | 80 | 70% (90d) | No graphics (66%) | 80% |  |
| 98 | [ ] | Until Then (STEAM) | 55 | 96 | 57% (90d) | Does not open (75%) | 96% |  |
| 99 | [ ] | Devil May Cry 4 Special Edition (STEAM) | 55 | 91 | 60% (90d) | Does not open (88%) | 81% |  |
| 100 | [ ] | The Bazaar (STEAM) | 55 | 89 | 62% (90d) | Does not open (74%) | 76% |  |
| 101 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 55 | 63 | 87% (90d) | Does not open (78%) | 83% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 102 | [ ] | MudRunner (STEAM) | 54 | 106 | 51% (90d) | Does not open (74%) | 60% |  |
| 103 | [ ] | A Plague Tale: Innocence (EPIC) | 54 | 92 | 59% (90d) | Does not open (71%) | 100% |  |
| 104 | [ ] | Teardown (STEAM) | 53 | 94 | 56% (90d) | Controller issues (50%) | 77% |  |
| 105 | [ ] | Street Fighter™ 6 (STEAM) | 53 | 77 | 69% (90d) | Does not open (89%) | 81% |  |
| 106 | [ ] | Sheepy: A Short Adventure (STEAM) | 52 | 61 | 85% (90d) | Does not open (53%) | 77% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 107 | [ ] | Okami HD (STEAM) | 51 | 93 | 55% (90d) | Controller issues (60%) | 87% |  |
| 108 | [ ] | Slay the Princess — The Pristine Cut (STEAM) | 51 | 85 | 60% (90d) | No graphics (60%) | 72% |  |
| 109 | [ ] | Order of the Sinking Star (STEAM) | 51 | 71 | 63% (14d) | Does not open (63%) | 69% |  |
| 110 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 51 | 55 | 93% (90d) | Does not open (85%) | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 111 | [ ] | 7 Days to Die (STEAM) | 50 | 106 | 70% (14d) | Does not open (73%) | 75% |  |
| 112 | [ ] | Rivals of Aether II (STEAM) | 50 | 76 | 66% (90d) | Does not open (57%) | 72% |  |
| 113 | [ ] | FINAL FANTASY VII (2013) (STEAM) | 50 | 71 | 70% (90d) | Does not open (86%) | 77% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 114 | [ ] | Dead Space (STEAM) | 50 | 63 | 79% (90d) | Does not open (53%) | 71% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 115 | [ ] | Watch_Dogs 2 (STEAM) | 50 | 57 | 88% (90d) | Does not open (97%) | 62% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 116 | [ ] | Resident Evil 6 (STEAM) | 49 | 125 | 78% (1.3.0) | Does not open (56%) | 91% |  |
| 117 | [ ] | Sable (EPIC) | 49 | 89 | 55% (90d) | No graphics (45%) | 80% |  |
| 118 | [ ] | Tomb Raider: Anniversary (STEAM) | 48 | 65 | 74% (90d) | Does not open (96%) | 63% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 119 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 75 | 63% (90d) | Controller issues (57%) | 97% |  |
| 120 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 47 | 68 | 69% (90d) | Does not open (82%) | 81% |  |
| 121 | [ ] | MapleStory (STEAM) | 47 | 48 | 96% (14d) | Does not open (77%) | 76% |  |
| 122 | [ ] | Digimon World: Next Order (STEAM) | 46 | 87 | 53% (90d) | Controller issues (80%) | 94% |  |
| 123 | [ ] | Resident Evil 7 Biohazard (STEAM) | 46 | 74 | 82% (14d) | Does not open (79%) | 82% |  |
| 124 | [ ] | Plague Inc: Evolved (STEAM) | 46 | 71 | 65% (90d) | Does not open (66%) | 61% |  |
| 125 | [ ] | Last Epoch (STEAM) | 46 | 61 | 86% (1.3.0) | Does not open (73%) | 100% |  |
| 126 | [ ] | Grand Theft Auto V (EPIC) | 45 | 51 | 88% (90d) | Does not open (89%) | 82% |  |
| 127 | [ ] | Moonlighter (EPIC) | 45 | 49 | 92% (90d) | No graphics (77%) | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 128 | [ ] | PROTOTYPE 2 (STEAM) | 44 | 84 | 52% (90d) | Does not open (74%) | 86% |  |
| 129 | [ ] | Darkest Dungeon® (EPIC) | 44 | 82 | 52% (1.3.0) | Does not open (60%) | 62% |  |
| 130 | [ ] | Skullgirls 2nd Encore (STEAM) | 44 | 76 | 58% (90d) | Does not open (93%) | 62% |  |
| 131 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 44 | 70 | 63% (90d) | Does not open (65%) | 81% |  |
| 132 | [ ] | Your Only Move Is HUSTLE (STEAM) | 43 | 86 | 50% (90d) | Does not open (59%) | 91% |  |
| 133 | [ ] | Life is Strange™ (STEAM) | 43 | 83 | 52% (90d) | Does not open (74%) | 82% |  |
| 134 | [ ] | Salt and Sanctuary (STEAM) | 43 | 80 | 54% (90d) | Does not open (76%) | 84% |  |
| 135 | [ ] | Capcom Fighting Collection (STEAM) | 43 | 50 | 86% (90d) | Does not open (86%) | 75% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 136 | [ ] | Amnesia: The Dark Descent (STEAM) | 42 | 77 | 55% (90d) | Does not open (85%) | 79% |  |
| 137 | [ ] | Sonic Origins (STEAM) | 42 | 70 | 60% (90d) | Does not open (71%) | 83% |  |
| 138 | [ ] | Deadlock (STEAM) | 42 | 68 | 71% (14d) | Does not open (52%) | 94% |  |
| 139 | [ ] | Tales of ARISE (STEAM) | 41 | 69 | 59% (90d) | Controller issues (76%) | 92% |  |
| 140 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 41 | 62 | 66% (90d) | Does not open (75%) | 68% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 141 | [ ] | Rayman Origins (STEAM) | 40 | 88 | 58% (14d) | Does not open (72%) | 78% |  |
| 142 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 40 | 74 | 54% (90d) | Controller issues (53%) | 85% |  |
| 143 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 40 | 66 | 61% (90d) | Does not open (42%) | 67% |  |
| 144 | [ ] | Forza Horizon 4 (STEAM) | 40 | 56 | 71% (90d) | Does not open (50%) | 86% |  |
| 145 | [ ] | Aggelos (STEAM) | 40 | 54 | 74% (90d) | No graphics (79%) | 93% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 146 | [ ] | Capcom Arcade Stadium (STEAM) | 40 | 50 | 80% (90d) | Does not open (84%) | 75% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 147 | [ ] | Monster Hunter Wilds (STEAM) | 40 | 41 | 98% (90d) | Does not open (64%) | 71% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 148 | [ ] | MOUSE: P.I. For Hire (STEAM) | 39 | 133 | 57% (1.3.0) | Does not open (59%) | 86% |  |
| 149 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 39 | 75 | 52% (90d) | Controller issues (47%) | 87% |  |
| 150 | [ ] | Abiotic Factor (STEAM) | 38 | 70 | 54% (90d) | Does not open (84%) | 68% |  |
| 151 | [ ] | SurrounDead (STEAM) | 38 | 70 | 54% (90d) | Controller issues (56%) | 95% |  |
| 152 | [ ] | Rocket League (STEAM) | 38 | 56 | 68% (90d) | Does not open (74%) | 71% |  |
| 153 | [ ] | CrossCode (GOG) | 38 | 42 | 90% (90d) | Does not open (76%) | 64% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 154 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 67 | 55% (90d) | Does not open (68%) | 88% |  |
| 155 | [ ] | Romestead (STEAM) | 37 | 48 | 77% (90d) | Does not open (67%) | 83% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 156 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 36 | 70 | 51% (90d) | No graphics (84%) | 96% |  |
| 157 | [ ] | Counter-Strike:Global Offensive (STEAM) | 36 | 53 | 68% (90d) | Does not open (80%) | 74% |  |
| 158 | [ ] | Capcom Fighting Collection 2 (STEAM) | 36 | 50 | 72% (90d) | Does not open (80%) | 84% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 159 | [ ] | SnowRunner (STEAM) | 36 | 45 | 80% (90d) | Does not open (96%) | 80% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 160 | [ ] | Lost Planet: Extreme Condition (STEAM) | 36 | 43 | 84% (90d) | Does not open (79%) | 60% | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 161 | [ ] | Street Fighter 30th Anniversary Collection (STEAM) | 35 | 69 | 51% (90d) | Does not open (100%) | 63% |  |
| 162 | [ ] | Monster Hunter Stories (STEAM) | 35 | 66 | 53% (90d) | Does not open (89%) | 83% |  |
| 163 | [ ] | Gothic II: Gold Classic (STEAM) | 35 | 62 | 56% (90d) | Does not open (50%) | 82% |  |
| 164 | [ ] | Hearts of Iron IV (STEAM) | 35 | 58 | 60% (90d) | Does not open (73%) | 70% |  |
| 165 | [ ] | Earthion (STEAM) | 35 | 55 | 64% (90d) | Controller issues (88%) | 100% |  |
| 166 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 35 | 41 | 85% (90d) | Does not open (65%) | 72% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 167 | [ ] | Fallout 3 (STEAM) | 34 | 67 | 51% (90d) | Does not open (54%) | 87% |  |
| 168 | [ ] | COCOON (STEAM) | 34 | 66 | 52% (90d) | Directx error (44%) | 87% |  |
| 169 | [ ] | Torchlight II (STEAM) | 34 | 63 | 54% (90d) | Does not open (50%) | 93% |  |
| 170 | [ ] | Resident Evil Village (STEAM) | 34 | 57 | 60% (90d) | Does not open (71%) | 86% |  |
| 171 | [ ] | Secrets of Grindea (STEAM) | 34 | 52 | 65% (90d) | Does not open (52%) | 81% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 172 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 34 | 49 | 69% (90d) | Controller issues (91%) | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 173 | [ ] | Ultimate Custom Night (STEAM) | 34 | 46 | 74% (90d) | No graphics (69%) | 80% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 174 | [ ] | Need for Speed™ (STEAM) | 34 | 38 | 89% (90d) | Does not open (71%) | 63% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 175 | [ ] | Hotline Miami (GOG) | 34 | 37 | 92% (90d) | Does not open (94%) | 74% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 176 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 33 | 54 | 61% (90d) | Controller issues (61%) | 60% |  |
| 177 | [ ] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 53 | 62% (90d) | Controller issues (84%) | 80% |  |
| 178 | [ ] | Deus Ex™ GOTY Edition (GOG) | 33 | 50 | 66% (90d) | Does not open (40%) | 84% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 179 | [ ] | Metro: Last Light Complete Edition (STEAM) | 33 | 45 | 73% (90d) | Does not open (56%) | 61% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 180 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 33 | 41 | 80% (90d) | Does not open (70%) | 93% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 181 | [ ] | Mass Effect (2007) (STEAM) | 33 | 41 | 80% (90d) | Does not open (81%) | 70% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 182 | [ ] | Russian Fishing 4 (STEAM) | 33 | 38 | 87% (90d) | Does not open (68%) | 67% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 183 | [ ] | Red Dead Redemption (STEAM) | 33 | 37 | 89% (90d) | Does not open (95%) | 85% |  |
| 184 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 32 | 62 | 52% (90d) | Does not open (69%) | 85% |  |
| 185 | [ ] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 32 | 51 | 63% (90d) | Does not open (43%) | 70% |  |
| 186 | [ ] | Supermarket Together (STEAM) | 32 | 47 | 68% (90d) | Does not open (71%) | 83% |  |
| 187 | [ ] | Moonlight Peaks (STEAM) | 32 | 46 | 70% (90d) | Does not open (63%) | 100% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 188 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 42 | 76% (90d) | Controller issues (63%) | 88% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 189 | [ ] | Nioh: Complete Edition (STEAM) | 32 | 41 | 78% (90d) | Does not open (56%) | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 190 | [ ] | Grand Theft Auto III (STEAM) | 32 | 40 | 80% (90d) | Does not open (50%) | 94% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 191 | [ ] | Path of Exile 2 (STEAM) | 32 | 37 | 86% (90d) | Does not open (96%) | 85% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 192 | [ ] | Library Of Ruina (STEAM) | 31 | 60 | 52% (90d) | Does not open (67%) | 81% |  |
| 193 | [ ] | Cave Story+ (EPIC) | 31 | 59 | 53% (90d) | Does not open (44%) | 82% |  |
| 194 | [ ] | LEGO® Harry Potter™ Collection (STEAM) | 31 | 57 | 54% (90d) | Does not open (85%) | 89% |  |
| 195 | [ ] | Max Payne (STEAM) | 31 | 57 | 54% (90d) | No graphics (42%) | 94% |  |
| 196 | [ ] | Tower and Sword of Succubus (STEAM) | 31 | 47 | 66% (90d) | No graphics (81%) | 100% |  |
| 197 | [ ] | Super Animal Royale (STEAM) | 31 | 39 | 79% (90d) | Does not open (70%) | 73% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 198 | [ ] | Aethermancer (STEAM) | 30 | 51 | 59% (90d) | Does not open (79%) | 73% |  |
| 199 | [ ] | Binary Domain (STEAM) | 30 | 48 | 63% (90d) | Does not open (92%) | 85% |  |
| 200 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 29 | 54 | 54% (90d) | Does not open (55%) | 65% |  |
| 201 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 29 | 50 | 58% (90d) | Controller issues (48%) | 94% |  |
| 202 | [ ] | Zero Escape: The Nonary Games (STEAM) | 29 | 49 | 59% (90d) | Does not open (88%) | 69% |  |
| 203 | [ ] | Yakuza: Like a Dragon (STEAM) | 29 | 44 | 66% (90d) | Does not open (68%) | 73% |  |
| 204 | [ ] | Stellar Blade™ (STEAM) | 29 | 39 | 74% (90d) | Does not open (50%) | 89% |  |
| 205 | [ ] | Mortal Kombat X (STEAM) | 28 | 52 | 54% (90d) | Does not open (52%) | 82% |  |
| 206 | [ ] | Heavy Rain (STEAM) | 28 | 48 | 58% (90d) | Controller issues (64%) | 86% |  |
| 207 | [ ] | Dead Rising 2 (STEAM) | 28 | 41 | 85% (14d) | Does not open (88%) | 69% |  |
| 208 | [ ] | Crab Game (STEAM) | 28 | 38 | 74% (90d) | Does not open (58%) | 65% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 209 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 27 | 50 | 54% (90d) | Does not open (57%) | 62% |  |
| 210 | [ ] | Akane (STEAM) | 27 | 46 | 59% (90d) | Controller issues (71%) | 100% |  |
| 211 | [ ] | Prince of Persia (GOG) | 27 | 44 | 61% (90d) | Does not open (95%) | 85% |  |
| 212 | [ ] | SWORN (STEAM) | 27 | 42 | 64% (90d) | Does not open (55%) | 100% |  |
| 213 | [ ] | Ratatan (STEAM) | 27 | 41 | 66% (90d) | Does not open (47%) | 98% |  |
| 214 | [ ] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 27 | 39 | 69% (90d) | Does not open (82%) | 87% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 215 | [ ] | Bongo Cat (STEAM) | 27 | 37 | 73% (90d) | Does not open (67%) | 78% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 216 | [ ] | Dead Island Riptide Definitive Edition (STEAM) | 26 | 49 | 53% (90d) | Does not open (55%) | 78% |  |
| 217 | [ ] | Goose Goose Duck (STEAM) | 26 | 33 | 79% (90d) | Does not open (70%) | 77% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 218 | [ ] | Wizard of Legend (EPIC) | 25 | 44 | 57% (90d) | Does not open (79%) | 74% |  |
| 219 | [ ] | Being a DIK (STEAM) | 25 | 43 | 58% (90d) | Does not open (78%) | 89% |  |
| 220 | [ ] | Cat Mail Co. (STEAM) | 25 | 40 | 63% (90d) | Does not open (90%) | 91% |  |
| 221 | [ ] | Limbus Company (STEAM) | 25 | 40 | 63% (90d) | Does not open (85%) | 82% |  |
| 222 | [ ] | Palia (STEAM) | 25 | 35 | 71% (90d) | Does not open (63%) | 67% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 223 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 32 | 78% (90d) | Does not open (87%) | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 224 | [ ] | Resident Evil (GOG) | 25 | 27 | 93% (90d) | Does not open (95%) | 76% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 225 | [ ] | Resident Evil Revelations 2 (STEAM) | 24 | 46 | 52% (90d) | Does not open (40%) | 92% |  |
| 226 | [ ] | Counter-Strike: Condition Zero (STEAM) | 24 | 42 | 57% (90d) | Does not open (53%) | 66% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 227 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 24 | 38 | 63% (90d) | Does not open (100%) | 86% |  |
| 228 | [ ] | Timberborn (STEAM) | 24 | 36 | 67% (90d) | No graphics (64%) | 77% |  |
| 229 | [ ] | Party Animals (STEAM) | 24 | 33 | 73% (90d) | Does not open (75%) | 79% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 230 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 23 | 44 | 52% (90d) | Controller issues (63%) | 92% |  |
| 231 | [ ] | Football Manager 2024 (EPIC) | 23 | 42 | 55% (90d) | Does not open (86%) | 88% |  |
| 232 | [ ] | Overlord (STEAM) | 23 | 42 | 55% (90d) | Does not open (72%) | 68% |  |
| 233 | [ ] | Unturned (STEAM) | 23 | 42 | 55% (90d) | Does not open (61%) | 86% |  |
| 234 | [ ] | Lobotomy Corporation (STEAM) | 23 | 38 | 80% (14d) | No graphics (60%) | 100% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 235 | [ ] | Return to Monkey Island (STEAM) | 23 | 37 | 62% (90d) | No graphics (59%) | 92% |  |
| 236 | [ ] | Digimon Survive (STEAM) | 23 | 36 | 64% (90d) | Controller issues (75%) | 94% |  |
| 237 | [ ] | Need for Speed™ Unbound (STEAM) | 23 | 31 | 74% (90d) | Does not open (79%) | 80% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 238 | [ ] | FINAL FANTASY XIV Online (STEAM) | 23 | 30 | 77% (90d) | Does not open (100%) | 92% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 239 | [ ] | Jade Empire: Special Edition (GOG) | 23 | 29 | 79% (90d) | Does not open (50%) | 74% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 240 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 23 | 28 | 82% (90d) | Does not open (40%) | 63% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 241 | [ ] | TCG Card Shop Simulator (STEAM) | 22 | 41 | 54% (90d) | Does not open (58%) | 85% |  |
| 242 | [ ] | This War of Mine (STEAM) | 22 | 39 | 56% (90d) | No graphics (56%) | 74% |  |
| 243 | [ ] | One-armed robber (STEAM) | 22 | 38 | 58% (90d) | Controller issues (65%) | 83% |  |
| 244 | [ ] | Life is Strange Remastered (STEAM) | 22 | 34 | 65% (90d) | Does not open (73%) | 93% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 245 | [ ] | Beyond: Two Souls (STEAM) | 22 | 30 | 73% (90d) | Does not open (48%) | 70% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 246 | [ ] | Nex Machina (STEAM) | 22 | 30 | 73% (90d) | Does not open (53%) | 86% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 247 | [ ] | Backpack Battles (STEAM) | 21 | 42 | 50% (90d) | Does not open (62%) | 94% |  |
| 248 | [ ] | Hatred (STEAM) | 21 | 42 | 50% (90d) | Does not open (71%) | 81% |  |
| 249 | [ ] | Gambonanza (STEAM) | 21 | 41 | 51% (90d) | Does not open (60%) | 96% |  |
| 250 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 21 | 39 | 54% (90d) | Does not open (53%) | 73% |  |
| 251 | [ ] | Pinball FX Classic (STEAM) | 21 | 39 | 54% (90d) | Does not open (75%) | 93% |  |
| 252 | [ ] | Tiny Glade (STEAM) | 21 | 38 | 55% (90d) | Does not open (42%) | 83% |  |
| 253 | [ ] | GRIP: Combat Racing (STEAM) | 21 | 36 | 58% (90d) | Does not open (100%) | 83% |  |
| 254 | [ ] | Trailmakers (STEAM) | 21 | 36 | 58% (90d) | Does not open (41%) | 89% |  |
| 255 | [ ] | Worms W.M.D (STEAM) | 21 | 36 | 58% (90d) | Does not open (56%) | 88% |  |
| 256 | [ ] | Changed (STEAM) | 21 | 35 | 60% (90d) | Does not open (60%) | 90% |  |
| 257 | [ ] | DNF Duel (EPIC) | 21 | 34 | 62% (90d) | Does not open (50%) | 88% |  |
| 258 | [ ] | Torchlight II (EPIC) | 21 | 28 | 75% (90d) | Does not open (86%) | 100% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 259 | [ ] | Hitman 2: Silent Assassin (STEAM) | 21 | 26 | 81% (90d) | Does not open (88%) | 67% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 260 | [ ] | Crimzon Clover World EXplosion (STEAM) | 20 | 39 | 51% (90d) | Does not open (47%) | 100% |  |
| 261 | [ ] | Control Ultimate Edition (GOG) | 20 | 37 | 54% (90d) | Does not open (81%) | 96% |  |
| 262 | [ ] | Breath of Fire IV (GOG) | 20 | 35 | 57% (90d) | Does not open (74%) | 62% |  |
| 263 | [ ] | Hitman: Absolution (GOG) | 20 | 31 | 65% (90d) | Does not open (84%) | 100% |  |
| 264 | [ ] | Dishonored 2 (STEAM) | 20 | 29 | 69% (90d) | Does not open (88%) | 92% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 265 | [ ] | DOOM 3: BFG Edition (GOG) | 20 | 28 | 71% (90d) | No graphics (65%) | 76% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 266 | [ ] | Dead Island (STEAM) | 20 | 26 | 77% (90d) | Does not open (69%) | 72% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 267 | [ ] | Killing Floor (STEAM) | 19 | 37 | 51% (90d) | Controller issues (100%) | 93% |  |
| 268 | [ ] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 19 | 34 | 56% (90d) | Does not open (60%) | 87% |  |
| 269 | [ ] | Tabletop Simulator (STEAM) | 19 | 32 | 59% (90d) | No graphics (50%) | 65% |  |
| 270 | [ ] | Metro Exodus (STEAM) | 19 | 30 | 63% (90d) | Does not open (82%) | 90% |  |
| 271 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 19 | 24 | 79% (90d) | Does not open (82%) | 100% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 272 | [ ] | SKALD: Against the Black Priory (STEAM) | 18 | 36 | 50% (90d) | No graphics (67%) | 100% |  |
| 273 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 18 | 35 | 51% (90d) | Does not open (67%) | 70% |  |
| 274 | [ ] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 18 | 35 | 51% (90d) | Controller issues (50%) | 100% |  |
| 275 | [ ] | Mini Metro (STEAM) | 18 | 35 | 51% (90d) | Does not open (35%) | 62% |  |
| 276 | [ ] | Faster Than Light (EPIC) | 18 | 34 | 53% (90d) | Does not open (41%) | 91% |  |
| 277 | [ ] | Stick It to the Stickman (STEAM) | 18 | 33 | 55% (90d) | Does not open (87%) | 81% |  |
| 278 | [ ] | Antichamber (STEAM) | 18 | 32 | 56% (90d) | Does not open (47%) | 85% |  |
| 279 | [ ] | Titanfall® 2 (STEAM) | 18 | 30 | 60% (90d) | Does not open (83%) | 92% |  |
| 280 | [ ] | Formula Legends (STEAM) | 18 | 29 | 62% (90d) | No graphics (60%) | 73% |  |
| 281 | [ ] | Maneater (STEAM) | 18 | 29 | 62% (90d) | Does not open (92%) | 82% |  |
| 282 | [ ] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 18 | 27 | 67% (90d) | Does not open (100%) | 94% |  |
| 283 | [ ] | Farming Simulator 25 (STEAM) | 18 | 26 | 69% (90d) | Does not open (82%) | 78% |  |
| 284 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 25 | 72% (90d) | No graphics (44%) | 73% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 285 | [ ] | Fall Guys (STEAM) | 18 | 24 | 75% (90d) | Does not open (92%) | 90% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 286 | [ ] | War Thunder (STEAM) | 18 | 24 | 75% (90d) | Does not open (53%) | 74% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 287 | [ ] | Spin Rhythm XD (STEAM) | 17 | 34 | 50% (90d) | Controller issues (88%) | 83% |  |
| 288 | [ ] | CULTIC (STEAM) | 17 | 33 | 52% (90d) | Does not open (92%) | 64% |  |
| 289 | [ ] | GRANDIA HD Remaster (STEAM) | 17 | 33 | 52% (90d) | Does not open (93%) | 67% |  |
| 290 | [ ] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 17 | 33 | 52% (90d) | Does not open (87%) | 60% |  |
| 291 | [ ] | Grim Fandango Remastered (STEAM) | 17 | 30 | 57% (90d) | Does not open (93%) | 76% |  |
| 292 | [ ] | Mortal Shell (EPIC) | 17 | 30 | 57% (90d) | No graphics (73%) | 80% |  |
| 293 | [ ] | Wildermyth (STEAM) | 17 | 29 | 59% (90d) | Does not open (50%) | 91% |  |
| 294 | [ ] | Arcade Paradise (EPIC) | 17 | 26 | 65% (90d) | Does not open (56%) | 80% |  |
| 295 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 17 | 25 | 68% (90d) | Does not open (69%) | 71% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 296 | [ ] | Katanaut (STEAM) | 17 | 24 | 71% (90d) | Does not open (75%) | 69% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 297 | [ ] | Cyberpunk 2077 (EPIC) | 17 | 22 | 77% (90d) | Does not open (50%) | 82% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 298 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 16 | 32 | 50% (90d) | Does not open (92%) | 68% |  |
| 299 | [ ] | Distance (STEAM) | 16 | 31 | 52% (90d) | Does not open (79%) | 84% |  |
| 300 | [ ] | Mortal Kombat 11 (STEAM) | 16 | 31 | 52% (90d) | Does not open (70%) | 61% |  |
| 301 | [ ] | Far Far West (STEAM) | 16 | 27 | 59% (90d) | Does not open (53%) | 94% |  |
| 302 | [ ] | WORLD OF FINAL FANTASY (STEAM) | 16 | 26 | 62% (90d) | No graphics (62%) | 71% |  |
| 303 | [ ] | Batman™: Arkham Origins (GOG) | 16 | 25 | 64% (90d) | Does not open (69%) | 92% |  |
| 304 | [ ] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 16 | 25 | 64% (90d) | Does not open (60%) | 71% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 305 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 23 | 70% (90d) | No graphics (60%) | 85% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 306 | [ ] | Ghosts 'n Goblins Resurrection (STEAM) | 15 | 30 | 50% (90d) | Does not open (100%) | 94% |  |
| 307 | [ ] | Mark of the Ninja (STEAM) | 15 | 29 | 52% (90d) | Does not open (75%) | 64% |  |
| 308 | [ ] | LET IT DIE (STEAM) | 15 | 25 | 60% (90d) | Does not open (91%) | 73% |  |
| 309 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 15 | 24 | 63% (90d) | Does not open (92%) | 67% |  |
| 310 | [ ] | Sons Of The Forest (STEAM) | 15 | 23 | 65% (90d) | Does not open (50%) | 74% |  |
| 311 | [ ] | Allumeria (STEAM) | 15 | 22 | 68% (90d) | Does not open (69%) | 71% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 312 | [ ] | Horny Villa (STEAM) | 15 | 22 | 68% (90d) | Does not open (67%) | 100% |  |
| 313 | [ ] | BioShock 2 Remastered (EPIC) | 14 | 28 | 50% (90d) | Does not open (60%) | 95% |  |
| 314 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 24 | 58% (90d) | Does not open (90%) | 65% |  |
| 315 | [ ] | Injustice™ 2 (STEAM) | 14 | 24 | 58% (90d) | Does not open (91%) | 75% |  |
| 316 | [ ] | Academy Love Saga: Tennis Angels EX (STEAM) | 14 | 23 | 61% (90d) | Does not open (77%) | 91% |  |
| 317 | [ ] | Disgaea 4 Complete+ (STEAM) | 14 | 22 | 64% (90d) | No graphics (43%) | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 318 | [ ] | Prince of Persia: The Two Thrones (STEAM) | 14 | 22 | 64% (90d) | Does not open (86%) | 67% |  |
| 319 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 22 | 64% (90d) | Does not open (86%) | 81% |  |
| 320 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 22 | 64% (90d) | Controller issues (57%) | 61% |  |
| 321 | [ ] | Escape the Backrooms (STEAM) | 14 | 21 | 67% (90d) | Does not open (100%) | 100% |  |
| 322 | [ ] | Fallout 2 (GOG) | 14 | 20 | 70% (90d) | Does not open (54%) | 73% |  |
| 323 | [ ] | Coromon (GOG) | 13 | 26 | 50% (90d) | No graphics (58%) | 65% |  |
| 324 | [ ] | Ys VIII: Lacrimosa of Dana (STEAM) | 13 | 26 | 50% (90d) | Does not open (73%) | 79% |  |
| 325 | [ ] | F.E.A.R. 2: Project Origin (STEAM) | 13 | 25 | 52% (90d) | Does not open (50%) | 79% |  |
| 326 | [ ] | Pillars of Eternity (STEAM) | 13 | 25 | 52% (90d) | Does not open (43%) | 90% |  |
| 327 | [ ] | Minit (EPIC) | 13 | 23 | 57% (90d) | Does not open (82%) | 82% |  |
| 328 | [ ] | DiRT 4 (STEAM) | 13 | 22 | 59% (90d) | Does not open (75%) | 100% |  |
| 329 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 22 | 59% (90d) | Does not open (80%) | 91% |  |
| 330 | [ ] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 13 | 20 | 65% (90d) | Does not open (33%) | 93% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 331 | [ ] | sobosuba (STEAM) | 12 | 24 | 50% (90d) | Does not open (58%) | 90% |  |
| 332 | [ ] | AER Memories of Old (EPIC) | 12 | 23 | 52% (90d) | Does not open (91%) | 91% |  |
| 333 | [ ] | Poly Bridge (STEAM) | 12 | 23 | 52% (90d) | Does not open (58%) | 100% |  |
| 334 | [ ] | SEGA Mega Drive & Genesis Classics (STEAM) | 12 | 23 | 52% (90d) | Graphics glitches (50%) | 67% |  |
| 335 | [ ] | Ultrapool (STEAM) | 12 | 23 | 52% (90d) | Does not open (64%) | 100% |  |
| 336 | [ ] | Lust Goddess (STEAM) | 12 | 22 | 55% (90d) | Does not open (100%) | 60% |  |
| 337 | [ ] | Mina the Hollower (GOG) | 12 | 22 | 55% (90d) | Does not open (42%) | 62% |  |
| 338 | [ ] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 21 | 57% (90d) | Controller issues (60%) | 90% |  |
| 339 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 12 | 20 | 60% (90d) | Does not open (86%) | 77% |  |
| 340 | [ ] | 12 is Better Than 6 (STEAM) | 11 | 22 | 50% (90d) | Does not open (56%) | 80% |  |
| 341 | [ ] | DRAGON BALL XENOVERSE (STEAM) | 11 | 22 | 50% (90d) | Does not open (100%) | 62% |  |
| 342 | [ ] | REMATCH (STEAM) | 11 | 22 | 50% (90d) | Graphics glitches (67%) | 76% |  |
| 343 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 11 | 21 | 52% (90d) | Does not open (67%) | 88% |  |
| 344 | [ ] | Pocket Mirror ~ GoldenerTraum (STEAM) | 11 | 21 | 52% (90d) | Does not open (70%) | 100% |  |
| 345 | [ ] | Sonic Superstars (STEAM) | 11 | 21 | 52% (90d) | Does not open (67%) | 67% |  |
| 346 | [ ] | Castle in the Clouds (STEAM) | 11 | 20 | 55% (90d) | No graphics (63%) | 93% |  |
| 347 | [ ] | Ready or Not (STEAM) | 11 | 20 | 55% (90d) | Does not open (60%) | 92% |  |
| 348 | [ ] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 20 | 55% (90d) | No graphics (60%) | 67% |  |
| 349 | [ ] | BioShock™ 2 Remastered (GOG) | 10 | 20 | 50% (90d) | Does not open (89%) | 82% |  |
| 350 | [ ] | HITMAN World of Assassination (STEAM) | 10 | 20 | 50% (90d) | Does not open (78%) | 89% |  |

## Recently recovered (332)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 287 | 2026-10-23 | 326 | 62% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 2 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 255 | 2026-10-19 | 304 | 65% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 3 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 217 | 2026-10-18 | 332 | 60% |  |
| 4 | [x] | OMORI (STEAM) | 213 | 2026-10-16 | 257 | 74% |  |
| 5 | [x] | Devil May Cry HD Collection (STEAM) | 197 | 2026-10-19 | 276 | 71% |  |
| 6 | [x] | Burnout Paradise: The Ultimate Box (STEAM) | 164 | 2026-10-16 | 247 | 72% |  |
| 7 | [x] | Counter-Strike (STEAM) | 156 | 2026-10-22 | 241 | 55% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 8 | [x] | FINAL FANTASY RESONANCE (STEAM) | 153 | 2026-10-24 | 350 | 69% |  |
| 9 | [x] | Far Cry® 3 (STEAM) | 147 | 2026-10-21 | 166 | 63% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 10 | [x] | Borderlands 2 (EPIC) | 136 | 2026-10-25 | 157 | 64% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 11 | [x] | Minecraft Dungeons II (STEAM) | 122 | 2026-10-21 | 139 | 62% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 12 | [x] | The Witcher: Enhanced Edition (STEAM) | 119 | 2026-10-25 | 135 | 60% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 13 | [x] | Call of Duty: Black Ops III (STEAM) | 117 | 2026-10-18 | 239 | 71% |  |
| 14 | [x] | Moonstone Island (STEAM) | 113 | 2026-10-16 | 147 | 89% |  |
| 15 | [x] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 110 | 2026-10-18 | 152 | 65% |  |
| 16 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 102 | 2026-10-25 | 162 | 61% |  |
| 17 | [x] | Don't Starve Together (STEAM) | 96 | 2026-10-16 | 176 | 75% |  |
| 18 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 95 | 2026-10-17 | 129 | 100% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 19 | [x] | Cry of Fear (STEAM) | 94 | 2026-10-18 | 180 | 89% |  |
| 20 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 88 | 2026-10-18 | 131 | 66% |  |
| 21 | [x] | Catherine Classic (STEAM) | 85 | 2026-10-19 | 175 | 76% |  |
| 22 | [x] | Ultra Street Fighter IV (STEAM) | 82 | 2026-10-17 | 178 | 70% |  |
| 23 | [x] | Hogwarts Legacy (STEAM) | 80 | 2026-10-17 | 139 | 68% |  |
| 24 | [x] | DOOM 3: BFG Edition (STEAM) | 80 | 2026-10-19 | 113 | 67% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 25 | [x] | Detroit: Become Human (STEAM) | 79 | 2026-10-17 | 82 | 68% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 26 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 78 | 2026-10-21 | 102 | 70% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 27 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 77 | 2026-10-17 | 104 | 92% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 28 | [x] | Call of Juarez Gunslinger (STEAM) | 75 | 2026-10-18 | 89 | 68% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 29 | [x] | Gunfire Reborn (STEAM) | 75 | 2026-10-22 | 83 | 92% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 30 | [x] | Bayonetta (STEAM) | 74 | 2026-10-18 | 199 | 74% |  |
| 31 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 73 | 2026-10-18 | 122 | 93% |  |
| 32 | [x] | Dota 2 (STEAM) | 73 | 2026-10-17 | 106 | 76% |  |
| 33 | [x] | Darksiders (STEAM) | 73 | 2026-10-26 | 89 | 100% | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 34 | [x] | Need for Speed: Hot Pursuit (STEAM) | 72 | 2026-10-25 | 100 | 83% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 35 | [x] | Fable - The Lost Chapters (STEAM) | 70 | 2026-10-17 | 109 | 74% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 36 | [x] | Fallout (STEAM) | 70 | 2026-10-18 | 109 | 77% |  |
| 37 | [x] | Don't Starve (STEAM) | 68 | 2026-10-16 | 144 | 82% |  |
| 38 | [x] | American Truck Simulator (STEAM) | 68 | 2026-10-18 | 107 | 72% |  |
| 39 | [x] | Spyro™ Reignited Trilogy (STEAM) | 68 | 2026-10-18 | 106 | 71% |  |
| 40 | [x] | Borderlands: The Pre-Sequel (STEAM) | 68 | 2026-10-17 | 94 | 65% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 41 | [x] | TBH: Task Bar Hero (STEAM) | 67 | 2026-10-19 | 98 | 95% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 42 | [x] | Bloodstained: Ritual of the Night (EPIC) | 66 | 2026-10-19 | 117 | 63% |  |
| 43 | [x] | Disgaea 5 Complete (STEAM) | 66 | 2026-10-18 | 80 | 96% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 44 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 65 | 2026-10-17 | 88 | 89% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 45 | [x] | Poppy Playtime (STEAM) | 63 | 2026-10-17 | 112 | 81% |  |
| 46 | [x] | Sonic Lost World (STEAM) | 63 | 2026-10-18 | 102 | 93% |  |
| 47 | [x] | Big Walk (STEAM) | 63 | 2026-10-17 | 96 | 86% |  |
| 48 | [x] | Sonic Generations (STEAM) | 63 | 2026-10-17 | 73 | 62% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 49 | [x] | A Plague Tale: Innocence (STEAM) | 63 | 2026-10-20 | 66 | 70% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 50 | [x] | Path of Exile (STEAM) | 62 | 2026-10-26 | 71 | 82% | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 51 | [x] | Borderlands 3 (STEAM) | 61 | 2026-10-19 | 74 | 97% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 52 | [x] | Sonic Adventure DX (STEAM) | 60 | 2026-10-17 | 96 | 67% |  |
| 53 | [x] | eFootball™ (STEAM) | 59 | 2026-10-18 | 91 | 74% |  |
| 54 | [x] | Dead by Daylight (STEAM) | 59 | 2026-10-23 | 64 | 80% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 55 | [x] | Starbound (STEAM) | 57 | 2026-10-18 | 82 | 71% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 56 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 56 | 2026-10-18 | 89 | 74% |  |
| 57 | [x] | Guildrun Demo (STEAM) | 56 | 2026-10-22 | 80 | 80% |  |
| 58 | [x] | Until Then (STEAM) | 55 | 2026-10-17 | 96 | 96% |  |
| 59 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 55 | 2026-10-21 | 63 | 83% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 60 | [x] | MudRunner (STEAM) | 54 | 2026-10-24 | 106 | 60% |  |
| 61 | [x] | A Plague Tale: Innocence (EPIC) | 54 | 2026-10-25 | 92 | 100% |  |
| 62 | [x] | Teardown (STEAM) | 53 | 2026-10-17 | 94 | 77% |  |
| 63 | [x] | Street Fighter™ 6 (STEAM) | 53 | 2026-10-16 | 77 | 81% |  |
| 64 | [x] | Sheepy: A Short Adventure (STEAM) | 52 | 2026-10-24 | 61 | 77% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 65 | [x] | Okami HD (STEAM) | 51 | 2026-10-17 | 93 | 87% |  |
| 66 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 51 | 2026-10-19 | 85 | 72% |  |
| 67 | [x] | Alex Kidd in Miracle World DX (EPIC) | 51 | 2026-10-22 | 55 | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 68 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 50 | 2026-10-25 | 94 | 57% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 69 | [x] | Rivals of Aether II (STEAM) | 50 | 2026-10-20 | 76 | 72% |  |
| 70 | [x] | FINAL FANTASY VII (2013) (STEAM) | 50 | 2026-10-18 | 71 | 77% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 71 | [x] | Dead Space (STEAM) | 50 | 2026-10-18 | 63 | 71% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 72 | [x] | Watch_Dogs 2 (STEAM) | 50 | 2026-10-17 | 57 | 62% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 73 | [x] | Sable (EPIC) | 49 | 2026-10-18 | 89 | 80% |  |
| 74 | [x] | Tomb Raider: Anniversary (STEAM) | 48 | 2026-10-25 | 65 | 63% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 75 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 2026-10-17 | 75 | 97% |  |
| 76 | [x] | STEINS;GATE RE:BOOT (STEAM) | 47 | 2026-10-21 | 68 | 81% |  |
| 77 | [x] | Cobalt Core (STEAM) | 46 | 2026-10-18 | 95 | 88% |  |
| 78 | [x] | Tomb Raider GOTY (GOG) | 46 | 2026-10-17 | 94 | 97% |  |
| 79 | [x] | Digimon World: Next Order (STEAM) | 46 | 2026-10-18 | 87 | 94% |  |
| 80 | [x] | Plague Inc: Evolved (STEAM) | 46 | 2026-10-21 | 71 | 61% |  |
| 81 | [x] | Dishonored - Definitive Edition (EPIC) | 45 | 2026-10-17 | 100 | 81% |  |
| 82 | [x] | Moonlighter (EPIC) | 45 | 2026-10-23 | 49 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 83 | [x] | Death Road to Canada (STEAM) | 44 | 2026-10-17 | 93 | 70% |  |
| 84 | [x] | PROTOTYPE 2 (STEAM) | 44 | 2026-10-18 | 84 | 86% |  |
| 85 | [x] | Darkest Dungeon® (EPIC) | 44 | 2026-10-22 | 82 | 62% |  |
| 86 | [x] | Skullgirls 2nd Encore (STEAM) | 44 | 2026-10-26 | 76 | 62% |  |
| 87 | [x] | Life is Strange™ (STEAM) | 43 | 2026-10-17 | 83 | 82% |  |
| 88 | [x] | Salt and Sanctuary (STEAM) | 43 | 2026-10-18 | 80 | 84% |  |
| 89 | [x] | Capcom Fighting Collection (STEAM) | 43 | 2026-10-23 | 50 | 75% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 90 | [x] | Rogue Legacy (STEAM) | 42 | 2026-10-17 | 93 | 54% |  |
| 91 | [x] | Amnesia: The Dark Descent (STEAM) | 42 | 2026-10-17 | 77 | 79% |  |
| 92 | [x] | Deadlock (STEAM) | 42 | 2026-10-16 | 68 | 94% |  |
| 93 | [x] | Tales of ARISE (STEAM) | 41 | 2026-10-16 | 69 | 92% |  |
| 94 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 41 | 2026-10-18 | 62 | 68% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 95 | [x] | Rayman Origins (STEAM) | 40 | 2026-10-17 | 88 | 78% |  |
| 96 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 40 | 2026-10-17 | 74 | 85% |  |
| 97 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 40 | 2026-10-18 | 66 | 67% |  |
| 98 | [x] | Aggelos (STEAM) | 40 | 2026-10-21 | 54 | 93% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 99 | [x] | Capcom Arcade Stadium (STEAM) | 40 | 2026-10-17 | 50 | 75% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 100 | [x] | Monster Hunter Wilds (STEAM) | 40 | 2026-10-23 | 41 | 71% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 101 | [x] | Abiotic Factor (STEAM) | 38 | 2026-10-18 | 70 | 68% |  |
| 102 | [x] | Rocket League (STEAM) | 38 | 2026-10-17 | 56 | 71% |  |
| 103 | [x] | CrossCode (GOG) | 38 | 2026-10-23 | 42 | 64% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 104 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 37 | 2026-10-17 | 67 | 88% |  |
| 105 | [x] | Romestead (STEAM) | 37 | 2026-10-18 | 48 | 83% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 106 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 36 | 2026-10-17 | 70 | 96% |  |
| 107 | [x] | Counter-Strike:Global Offensive (STEAM) | 36 | 2026-10-19 | 53 | 74% |  |
| 108 | [x] | Capcom Fighting Collection 2 (STEAM) | 36 | 2026-10-18 | 50 | 84% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 109 | [x] | SnowRunner (STEAM) | 36 | 2026-10-19 | 45 | 80% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 110 | [x] | Lost Planet: Extreme Condition (STEAM) | 36 | 2026-10-25 | 43 | 60% | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 111 | [x] | POSTAL 2 (GOG) | 35 | 2026-10-22 | 71 | 100% |  |
| 112 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 35 | 2026-10-16 | 69 | 63% |  |
| 113 | [x] | Monster Hunter Stories (STEAM) | 35 | 2026-10-17 | 66 | 83% |  |
| 114 | [x] | Gothic II: Gold Classic (STEAM) | 35 | 2026-10-20 | 62 | 82% |  |
| 115 | [x] | Hearts of Iron IV (STEAM) | 35 | 2026-10-19 | 58 | 70% |  |
| 116 | [x] | Earthion (STEAM) | 35 | 2026-10-22 | 55 | 100% |  |
| 117 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 35 | 2026-10-18 | 41 | 72% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 118 | [x] | Ultimate Chicken Horse (STEAM) | 34 | 2026-10-23 | 69 | 53% |  |
| 119 | [x] | COCOON (STEAM) | 34 | 2026-10-17 | 66 | 87% |  |
| 120 | [x] | Torchlight II (STEAM) | 34 | 2026-10-20 | 63 | 93% |  |
| 121 | [x] | Resident Evil Village (STEAM) | 34 | 2026-10-17 | 57 | 86% |  |
| 122 | [x] | Secrets of Grindea (STEAM) | 34 | 2026-10-20 | 52 | 81% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 123 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 34 | 2026-10-21 | 49 | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 124 | [x] | Ultimate Custom Night (STEAM) | 34 | 2026-10-19 | 46 | 80% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 125 | [x] | Need for Speed™ (STEAM) | 34 | 2026-10-18 | 38 | 63% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 126 | [x] | Hotline Miami (GOG) | 34 | 2026-10-20 | 37 | 74% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 127 | [x] | PlateUp! (STEAM) | 33 | 2026-10-16 | 68 | 81% |  |
| 128 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 33 | 2026-10-19 | 54 | 60% |  |
| 129 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 2026-10-19 | 53 | 80% |  |
| 130 | [x] | Deus Ex™ GOTY Edition (GOG) | 33 | 2026-10-19 | 50 | 84% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 131 | [x] | Metro: Last Light Complete Edition (STEAM) | 33 | 2026-10-24 | 45 | 61% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 132 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 33 | 2026-10-22 | 41 | 93% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 133 | [x] | Mass Effect (2007) (STEAM) | 33 | 2026-10-26 | 41 | 70% | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 134 | [x] | Russian Fishing 4 (STEAM) | 33 | 2026-10-23 | 38 | 67% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 135 | [x] | Little Nightmares (STEAM) | 32 | 2026-10-16 | 71 | 66% |  |
| 136 | [x] | BlazBlue Centralfiction (STEAM) | 32 | 2026-10-17 | 68 | 82% |  |
| 137 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 32 | 2026-10-22 | 51 | 70% |  |
| 138 | [x] | Supermarket Together (STEAM) | 32 | 2026-10-19 | 47 | 83% |  |
| 139 | [x] | Moonlight Peaks (STEAM) | 32 | 2026-10-20 | 46 | 100% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 140 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 32 | 2026-10-20 | 42 | 88% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 141 | [x] | Nioh: Complete Edition (STEAM) | 32 | 2026-10-20 | 41 | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 142 | [x] | Grand Theft Auto III (STEAM) | 32 | 2026-10-17 | 40 | 94% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 143 | [x] | Path of Exile 2 (STEAM) | 32 | 2026-10-18 | 37 | 85% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 144 | [x] | Stumble Guys (STEAM) | 31 | 2026-10-18 | 64 | 84% |  |
| 145 | [x] | Bloodstained: Curse of the Moon (STEAM) | 31 | 2026-10-16 | 63 | 70% |  |
| 146 | [x] | Library Of Ruina (STEAM) | 31 | 2026-10-16 | 60 | 81% |  |
| 147 | [x] | Cave Story+ (EPIC) | 31 | 2026-10-18 | 59 | 82% |  |
| 148 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 31 | 2026-10-17 | 57 | 89% |  |
| 149 | [x] | Max Payne (STEAM) | 31 | 2026-10-17 | 57 | 94% |  |
| 150 | [x] | Tower and Sword of Succubus (STEAM) | 31 | 2026-10-22 | 47 | 100% |  |
| 151 | [x] | Super Animal Royale (STEAM) | 31 | 2026-10-19 | 39 | 73% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 152 | [x] | Dying Light (EPIC) | 30 | 2026-10-17 | 67 | 96% |  |
| 153 | [x] | BioShock™ (GOG) | 30 | 2026-10-18 | 61 | 70% |  |
| 154 | [x] | Aethermancer (STEAM) | 30 | 2026-10-18 | 51 | 73% |  |
| 155 | [x] | Binary Domain (STEAM) | 30 | 2026-10-18 | 48 | 85% |  |
| 156 | [x] | Max Payne 2: The Fall of Max Payne (STEAM) | 29 | 2026-10-26 | 54 | 65% |  |
| 157 | [x] | Prince of Persia: The Sands of Time (STEAM) | 29 | 2026-10-20 | 50 | 94% |  |
| 158 | [x] | Zero Escape: The Nonary Games (STEAM) | 29 | 2026-10-17 | 49 | 69% |  |
| 159 | [x] | State of Decay: Year-One (STEAM) | 28 | 2026-10-18 | 61 | 83% |  |
| 160 | [x] | Mortal Kombat X (STEAM) | 28 | 2026-10-17 | 52 | 82% |  |
| 161 | [x] | Heavy Rain (STEAM) | 28 | 2026-10-18 | 48 | 86% |  |
| 162 | [x] | Crab Game (STEAM) | 28 | 2026-10-22 | 38 | 65% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 163 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 27 | 2026-10-19 | 91 | 91% |  |
| 164 | [x] | G.I. Joe Wrath of Cobra (EPIC) | 27 | 2026-10-19 | 50 | 62% |  |
| 165 | [x] | Akane (STEAM) | 27 | 2026-10-20 | 46 | 100% |  |
| 166 | [x] | Prince of Persia (GOG) | 27 | 2026-10-24 | 44 | 85% |  |
| 167 | [x] | SWORN (STEAM) | 27 | 2026-10-23 | 42 | 100% |  |
| 168 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 27 | 2026-10-18 | 39 | 87% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 169 | [x] | Bongo Cat (STEAM) | 27 | 2026-10-20 | 37 | 78% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 170 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 26 | 2026-10-19 | 60 | 81% |  |
| 171 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 26 | 2026-10-18 | 49 | 78% |  |
| 172 | [x] | Goose Goose Duck (STEAM) | 26 | 2026-10-25 | 33 | 77% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 173 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 25 | 2026-10-20 | 51 | 74% |  |
| 174 | [x] | Wizard of Legend (EPIC) | 25 | 2026-10-18 | 44 | 74% |  |
| 175 | [x] | Being a DIK (STEAM) | 25 | 2026-10-19 | 43 | 89% |  |
| 176 | [x] | Cat Mail Co. (STEAM) | 25 | 2026-10-24 | 40 | 91% |  |
| 177 | [x] | Limbus Company (STEAM) | 25 | 2026-10-18 | 40 | 82% |  |
| 178 | [x] | Palia (STEAM) | 25 | 2026-10-22 | 35 | 67% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 179 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-10-21 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 180 | [x] | Resident Evil (GOG) | 25 | 2026-10-20 | 27 | 76% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 181 | [x] | Titan Quest Anniversary Edition (STEAM) | 24 | 2026-10-16 | 55 | 81% |  |
| 182 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 54 | 84% |  |
| 183 | [x] | Counter-Strike: Condition Zero (STEAM) | 24 | 2026-10-17 | 42 | 66% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 184 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 24 | 2026-10-17 | 38 | 86% |  |
| 185 | [x] | Timberborn (STEAM) | 24 | 2026-10-25 | 36 | 77% |  |
| 186 | [x] | Party Animals (STEAM) | 24 | 2026-10-17 | 33 | 79% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 187 | [x] | ABZÛ (STEAM) | 23 | 2026-10-21 | 51 | 88% |  |
| 188 | [x] | CarX Drift Racing Online (STEAM) | 23 | 2026-10-16 | 47 | 79% |  |
| 189 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 23 | 2026-10-24 | 44 | 92% |  |
| 190 | [x] | Football Manager 2024 (EPIC) | 23 | 2026-10-20 | 42 | 88% |  |
| 191 | [x] | Overlord (STEAM) | 23 | 2026-10-21 | 42 | 68% |  |
| 192 | [x] | Unturned (STEAM) | 23 | 2026-10-17 | 42 | 86% |  |
| 193 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-10-19 | 38 | 100% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 194 | [x] | Return to Monkey Island (STEAM) | 23 | 2026-10-23 | 37 | 92% |  |
| 195 | [x] | Digimon Survive (STEAM) | 23 | 2026-10-23 | 36 | 94% |  |
| 196 | [x] | Need for Speed™ Unbound (STEAM) | 23 | 2026-10-26 | 31 | 80% | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 197 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 92% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 198 | [x] | Jade Empire: Special Edition (GOG) | 23 | 2026-10-23 | 29 | 74% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 199 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 23 | 2026-10-25 | 28 | 63% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 200 | [x] | Saints Row IV (STEAM) | 22 | 2026-10-19 | 49 | 73% |  |
| 201 | [x] | WEBFISHING (STEAM) | 22 | 2026-10-17 | 49 | 92% |  |
| 202 | [x] | No Rest for the Wicked (STEAM) | 22 | 2026-10-19 | 45 | 74% |  |
| 203 | [x] | This War of Mine (STEAM) | 22 | 2026-10-21 | 39 | 74% |  |
| 204 | [x] | One-armed robber (STEAM) | 22 | 2026-10-23 | 38 | 83% |  |
| 205 | [x] | Life is Strange Remastered (STEAM) | 22 | 2026-10-20 | 34 | 93% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 206 | [x] | Beyond: Two Souls (STEAM) | 22 | 2026-10-22 | 30 | 70% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 207 | [x] | Nex Machina (STEAM) | 22 | 2026-10-18 | 30 | 86% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 208 | [x] | MudRunner (EPIC) | 21 | 2026-10-18 | 43 | 87% |  |
| 209 | [x] | Backpack Battles (STEAM) | 21 | 2026-10-21 | 42 | 94% |  |
| 210 | [x] | Hatred (STEAM) | 21 | 2026-10-22 | 42 | 81% |  |
| 211 | [x] | Brothers - A Tale of Two Sons (EPIC) | 21 | 2026-10-23 | 39 | 73% |  |
| 212 | [x] | Pinball FX Classic (STEAM) | 21 | 2026-10-23 | 39 | 93% |  |
| 213 | [x] | Tiny Glade (STEAM) | 21 | 2026-10-24 | 38 | 83% |  |
| 214 | [x] | GRIP: Combat Racing (STEAM) | 21 | 2026-10-20 | 36 | 83% |  |
| 215 | [x] | Trailmakers (STEAM) | 21 | 2026-10-21 | 36 | 89% |  |
| 216 | [x] | Changed (STEAM) | 21 | 2026-10-24 | 35 | 90% |  |
| 217 | [x] | DNF Duel (EPIC) | 21 | 2026-10-21 | 34 | 88% |  |
| 218 | [x] | Torchlight II (EPIC) | 21 | 2026-10-22 | 28 | 100% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 219 | [x] | Hitman 2: Silent Assassin (STEAM) | 21 | 2026-10-22 | 26 | 67% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 220 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 20 | 2026-10-25 | 42 | 59% |  |
| 221 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-10-20 | 39 | 100% |  |
| 222 | [x] | Breath of Fire IV (GOG) | 20 | 2026-10-26 | 35 | 62% |  |
| 223 | [x] | Hitman: Absolution (GOG) | 20 | 2026-10-24 | 31 | 100% |  |
| 224 | [x] | Dishonored 2 (STEAM) | 20 | 2026-10-20 | 29 | 92% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 225 | [x] | DOOM 3: BFG Edition (GOG) | 20 | 2026-10-19 | 28 | 76% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 226 | [x] | Dead Island (STEAM) | 20 | 2026-10-20 | 26 | 72% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 227 | [x] | Slow Roads (STEAM) | 19 | 2026-10-22 | 40 | 95% |  |
| 228 | [x] | Graveyard Keeper (GOG) | 19 | 2026-10-25 | 39 | 23% |  |
| 229 | [x] | No Man's Sky (GOG) | 19 | 2026-10-19 | 39 | 75% |  |
| 230 | [x] | Killing Floor (STEAM) | 19 | 2026-10-19 | 37 | 93% |  |
| 231 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 19 | 2026-10-18 | 34 | 87% |  |
| 232 | [x] | Tabletop Simulator (STEAM) | 19 | 2026-10-19 | 32 | 65% |  |
| 233 | [x] | Metro Exodus (STEAM) | 19 | 2026-10-20 | 30 | 90% |  |
| 234 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 19 | 2026-10-23 | 24 | 100% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 235 | [x] | Kingdom Come: Deliverance II (STEAM) | 18 | 2026-10-20 | 37 | 93% |  |
| 236 | [x] | SKALD: Against the Black Priory (STEAM) | 18 | 2026-10-20 | 36 | 100% |  |
| 237 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 18 | 2026-10-20 | 35 | 70% |  |
| 238 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 18 | 2026-10-21 | 35 | 100% |  |
| 239 | [x] | Mini Metro (STEAM) | 18 | 2026-10-20 | 35 | 62% |  |
| 240 | [x] | Faster Than Light (EPIC) | 18 | 2026-10-24 | 34 | 91% |  |
| 241 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-10-17 | 33 | 81% |  |
| 242 | [x] | Antichamber (STEAM) | 18 | 2026-10-20 | 32 | 85% |  |
| 243 | [x] | Titanfall® 2 (STEAM) | 18 | 2026-10-16 | 30 | 92% |  |
| 244 | [x] | Formula Legends (STEAM) | 18 | 2026-10-21 | 29 | 73% |  |
| 245 | [x] | Maneater (STEAM) | 18 | 2026-10-20 | 29 | 82% |  |
| 246 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 18 | 2026-10-21 | 27 | 94% |  |
| 247 | [x] | Farming Simulator 25 (STEAM) | 18 | 2026-10-21 | 26 | 78% |  |
| 248 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 2026-10-20 | 25 | 73% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 249 | [x] | Fall Guys (STEAM) | 18 | 2026-10-26 | 24 | 90% | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 250 | [x] | War Thunder (STEAM) | 18 | 2026-10-21 | 24 | 74% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 251 | [x] | Spin Rhythm XD (STEAM) | 17 | 2026-10-18 | 34 | 83% |  |
| 252 | [x] | CULTIC (STEAM) | 17 | 2026-10-24 | 33 | 64% |  |
| 253 | [x] | GRANDIA HD Remaster (STEAM) | 17 | 2026-10-22 | 33 | 67% |  |
| 254 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 17 | 2026-10-21 | 33 | 60% |  |
| 255 | [x] | Mortal Shell (EPIC) | 17 | 2026-10-19 | 30 | 80% |  |
| 256 | [x] | Grim Fandango Remastered (STEAM) | 17 | 2026-10-19 | 30 | 76% |  |
| 257 | [x] | Wildermyth (STEAM) | 17 | 2026-10-26 | 29 | 91% |  |
| 258 | [x] | Arcade Paradise (EPIC) | 17 | 2026-10-25 | 26 | 80% |  |
| 259 | [x] | Sonic and SEGA All Stars Racing (STEAM) | 17 | 2026-10-19 | 25 | 71% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 260 | [x] | Katanaut (STEAM) | 17 | 2026-10-20 | 24 | 69% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 261 | [x] | Cyberpunk 2077 (EPIC) | 17 | 2026-10-19 | 22 | 82% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 262 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 49 | 100% |  |
| 263 | [x] | Distance (STEAM) | 16 | 2026-10-19 | 31 | 84% |  |
| 264 | [x] | Mortal Kombat 11 (STEAM) | 16 | 2026-10-21 | 31 | 61% |  |
| 265 | [x] | Far Far West (STEAM) | 16 | 2026-10-21 | 27 | 94% |  |
| 266 | [x] | WORLD OF FINAL FANTASY (STEAM) | 16 | 2026-10-19 | 26 | 71% |  |
| 267 | [x] | Batman™: Arkham Origins (GOG) | 16 | 2026-10-22 | 25 | 92% |  |
| 268 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 16 | 2026-10-20 | 25 | 71% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 269 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 2026-10-21 | 23 | 85% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 270 | [x] | Mark of the Ninja (STEAM) | 15 | 2026-10-26 | 29 | 64% |  |
| 271 | [x] | LET IT DIE (STEAM) | 15 | 2026-10-25 | 25 | 73% |  |
| 272 | [x] | Sons Of The Forest (STEAM) | 15 | 2026-10-19 | 23 | 74% |  |
| 273 | [x] | Allumeria (STEAM) | 15 | 2026-10-23 | 22 | 71% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 274 | [x] | Horny Villa (STEAM) | 15 | 2026-10-21 | 22 | 100% |  |
| 275 | [x] | Tom Clancy's Splinter Cell: Chaos Theory (STEAM) | 14 | 2026-10-16 | 31 | 84% |  |
| 276 | [x] | Rayman Origins (GOG) | 14 | 2026-10-25 | 29 | 56% |  |
| 277 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 2026-10-25 | 24 | 65% |  |
| 278 | [x] | Injustice™ 2 (STEAM) | 14 | 2026-10-17 | 24 | 75% |  |
| 279 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 14 | 2026-10-21 | 23 | 91% |  |
| 280 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-10-23 | 22 | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 281 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 67% |  |
| 282 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 2026-10-23 | 22 | 81% |  |
| 283 | [x] | Super Monkey Ball Banana Mania (STEAM) | 14 | 2026-10-18 | 22 | 61% |  |
| 284 | [x] | Escape the Backrooms (STEAM) | 14 | 2026-10-25 | 21 | 100% |  |
| 285 | [x] | Middle-earth™: Shadow of War™ (STEAM) | 13 | 2026-10-16 | 38 | 80% |  |
| 286 | [x] | Blood: Fresh Supply (STEAM) | 13 | 2026-10-16 | 35 | 85% |  |
| 287 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 30 | 61% |  |
| 288 | [x] | Battle Chasers: Nightwar (STEAM) | 13 | 2026-10-20 | 29 | 73% |  |
| 289 | [x] | The WereCleaner (STEAM) | 13 | 2026-10-22 | 29 | 92% |  |
| 290 | [x] | Haiku, the Robot (STEAM) | 13 | 2026-10-21 | 27 | 91% |  |
| 291 | [x] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 2026-10-26 | 27 | 53% |  |
| 292 | [x] | Coromon (GOG) | 13 | 2026-10-19 | 26 | 65% |  |
| 293 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 13 | 2026-10-21 | 25 | 79% |  |
| 294 | [x] | Pillars of Eternity (STEAM) | 13 | 2026-10-26 | 25 | 90% |  |
| 295 | [x] | DiRT 4 (STEAM) | 13 | 2026-10-20 | 22 | 100% |  |
| 296 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-10-21 | 22 | 91% |  |
| 297 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 13 | 2026-10-25 | 20 | 93% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 298 | [x] | TowerFall Ascension (STEAM) | 12 | 2026-10-16 | 31 | 52% |  |
| 299 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 12 | 2026-10-19 | 29 | 100% |  |
| 300 | [x] | Dead Space™ 3 (STEAM) | 12 | 2026-10-20 | 26 | 75% |  |
| 301 | [x] | Possessor(s) (STEAM) | 12 | 2026-10-24 | 25 | n/a |  |
| 302 | [x] | Revolution Idle (STEAM) | 12 | 2026-10-26 | 25 | n/a |  |
| 303 | [x] | Poly Bridge (STEAM) | 12 | 2026-10-26 | 23 | 100% |  |
| 304 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 12 | 2026-10-20 | 23 | 67% |  |
| 305 | [x] | Ultrapool (STEAM) | 12 | 2026-10-24 | 23 | 100% |  |
| 306 | [x] | Mina the Hollower (GOG) | 12 | 2026-10-26 | 22 | 62% |  |
| 307 | [x] | Lust Goddess (STEAM) | 12 | 2026-10-26 | 22 | 60% |  |
| 308 | [x] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 2026-10-26 | 21 | 90% |  |
| 309 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 12 | 2026-10-24 | 20 | 77% |  |
| 310 | [x] | SteamWorld Heist (GOG) | 11 | 2026-10-25 | 23 | n/a |  |
| 311 | [x] | Haydee (STEAM) | 11 | 2026-10-22 | 23 | 87% |  |
| 312 | [x] | 12 is Better Than 6 (STEAM) | 11 | 2026-10-21 | 22 | 80% |  |
| 313 | [x] | DRAGON BALL XENOVERSE (STEAM) | 11 | 2026-10-25 | 22 | 62% |  |
| 314 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 22 | 76% |  |
| 315 | [x] | Car Mechanic Simulator 2018 (STEAM) | 11 | 2026-10-22 | 21 | 88% |  |
| 316 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 11 | 2026-10-23 | 21 | 100% |  |
| 317 | [x] | Sonic Superstars (STEAM) | 11 | 2026-10-21 | 21 | 67% |  |
| 318 | [x] | Castle in the Clouds (STEAM) | 11 | 2026-10-21 | 20 | 93% |  |
| 319 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 11 | 2026-10-21 | 20 | 67% |  |
| 320 | [x] | What Remains of Edith Finch (STEAM) | 10 | 2026-10-19 | 27 | 43% |  |
| 321 | [x] | Divinity: Original Sin (Classic) (STEAM) | 10 | 2026-10-16 | 25 | n/a |  |
| 322 | [x] | Sid Meier's Civilization VI (EPIC) | 10 | 2026-10-19 | 23 | 80% |  |
| 323 | [x] | Delver (STEAM) | 10 | 2026-10-17 | 23 | 67% |  |
| 324 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 10 | 2026-10-23 | 22 | 80% |  |
| 325 | [x] | BioShock™ 2 Remastered (GOG) | 10 | 2026-10-23 | 20 | 82% |  |
| 326 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 327 | [x] | Football Manager 2024 (STEAM) | 9 | 2026-10-16 | 20 | n/a |  |
| 328 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 9 | 2026-10-20 | 20 | n/a |  |
| 329 | [x] | Gloomhaven (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 330 | [x] | Mafia II: Definitive Edition (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 331 | [x] | Intravenous (STEAM) | 8 | 2026-10-16 | 20 | 94% |  |
| 332 | [x] | Alex Kidd in Miracle World DX (STEAM) | 2 | 2026-10-16 | 36 | 82% |  |
