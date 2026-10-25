# GameNative compatibility worklist

Generated: `2026-10-25T04:30:07.347Z` · App release: `1.3.0` · Ratings since: `2026-07-27T04:30:07.347Z` · Telemetry window: `21` days on `Adreno + Turnip`

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
| Does not work | 314 |
| Probably does not work | 109 |
| First launch fails | 341 |
| Mixed | 456 |
| Works | 994 |
| Total | 2214 |

## Does not work (314)

Open issues track these. Pick one and fix it. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/430).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [x] 2026-10-18 | Project Zomboid (STEAM) | 670 | 715 | 93% (1.3.0) | Does not open (68%) | 45% | [#1](https://github.com/GameNative/gamenative-compat/issues/1) |
| 2 | [x] 2026-10-18 | Just Cause 2 (STEAM) | 266 | 283 | 94% (90d) | Does not open (75%) | 10% | [#3](https://github.com/GameNative/gamenative-compat/issues/3) |
| 3 | [x] 2026-10-18 | Alan Wake (STEAM) | 254 | 262 | 100% (1.3.0) | Does not open (87%) | 9% | [#5](https://github.com/GameNative/gamenative-compat/issues/5) |
| 4 | [ ] | Counter-Strike 2 (STEAM) | 226 | 317 | 85% (1.3.0) | Does not open (60%) | 42% | [#10](https://github.com/GameNative/gamenative-compat/issues/10) |
| 5 | [x] 2026-10-18 | Call of Duty: Black Ops (STEAM) | 225 | 235 | 96% (90d) | Does not open (76%) | 17% | [#6](https://github.com/GameNative/gamenative-compat/issues/6) |
| 6 | [ ] | DRAGON BALL FighterZ (STEAM) | 221 | 249 | 76% (1.3.0) | Does not open (87%) | 57% | [#9](https://github.com/GameNative/gamenative-compat/issues/9) |
| 7 | [ ] | skate. (STEAM) | 220 | 235 | 90% (14d) | Does not open (81%) | 23% | [#7](https://github.com/GameNative/gamenative-compat/issues/7) |
| 8 | [x] 2026-10-18 | Spelunky 2 (STEAM) | 215 | 226 | 79% (14d) | Does not open (71%) | 40% | [#8](https://github.com/GameNative/gamenative-compat/issues/8) |
| 9 | [ ] | Garry's Mod (STEAM) | 200 | 331 | 70% (1.3.0) | Does not open (79%) | 56% | [#450](https://github.com/GameNative/gamenative-compat/issues/450) |
| 10 | [x] 2026-10-18 | Sid Meier's Civilization V (STEAM) | 189 | 201 | 94% (90d) | Does not open (76%) | 50% | [#11](https://github.com/GameNative/gamenative-compat/issues/11) |
| 11 | [ ] | Necesse (STEAM) | 186 | 195 | 95% (90d) | Does not open (81%) | 54% | [#12](https://github.com/GameNative/gamenative-compat/issues/12) |
| 12 | [ ] | Prototype (STEAM) | 175 | 231 | 76% (90d) | Does not open (76%) | 47% | [#13](https://github.com/GameNative/gamenative-compat/issues/13) |
| 13 | [ ] | Peggle Deluxe (STEAM) | 161 | 191 | 84% (90d) | Does not open (91%) | 44% | [#433](https://github.com/GameNative/gamenative-compat/issues/433) |
| 14 | [ ] | HELLDIVERS™ 2 (STEAM) | 147 | 155 | 95% (90d) | Does not open (92%) | 32% | [#17](https://github.com/GameNative/gamenative-compat/issues/17) |
| 15 | [ ] | Sol Cesto (EPIC) | 146 | 154 | 95% (90d) | Does not open (75%) | 55% | [#18](https://github.com/GameNative/gamenative-compat/issues/18) |
| 16 | [ ] | The Elder Scrolls III: Morrowind (STEAM) | 140 | 156 | 90% (90d) | Does not open (87%) | 44% | [#19](https://github.com/GameNative/gamenative-compat/issues/19) |
| 17 | [ ] | Assassin's Creed II (STEAM) | 138 | 144 | 96% (90d) | Does not open (79%) | 51% | [#20](https://github.com/GameNative/gamenative-compat/issues/20) |
| 18 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (EPIC) | 116 | 148 | 82% (14d) | Does not open (76%) | 43% | [#22](https://github.com/GameNative/gamenative-compat/issues/22) |
| 19 | [ ] | Diablo II: Resurrected – Infernal Edition (STEAM) | 116 | 142 | 71% (1.3.0) | Does not open (71%) | 50% | [#456](https://github.com/GameNative/gamenative-compat/issues/456) |
| 20 | [ ] | Transistor (STEAM) | 109 | 109 | 100% (90d) | Does not open (78%) | 0% | [#30](https://github.com/GameNative/gamenative-compat/issues/30) |
| 21 | [x] 2026-10-18 | Age of Empires II: Definitive Edition (STEAM) | 108 | 121 | 89% (90d) | No graphics (60%) | 48% | [#26](https://github.com/GameNative/gamenative-compat/issues/26) |
| 22 | [ ] | Dust: An Elysian Tail (STEAM) | 108 | 112 | 96% (90d) | Does not open (71%) | 10% | [#28](https://github.com/GameNative/gamenative-compat/issues/28) |
| 23 | [ ] | The Witcher: Enhanced Edition (GOG) | 105 | 115 | 91% (90d) | Does not open (75%) | 12% | [#23](https://github.com/GameNative/gamenative-compat/issues/23) |
| 24 | [ ] | Call of Duty: Black Ops II (STEAM) | 103 | 137 | 75% (90d) | Does not open (76%) | 26% | [#24](https://github.com/GameNative/gamenative-compat/issues/24) |
| 25 | [ ] | Mafia II (Classic) (STEAM) | 102 | 107 | 95% (90d) | Does not open (73%) | 4% | [#29](https://github.com/GameNative/gamenative-compat/issues/29) |
| 26 | [ ] | Saints Row: The Third (STEAM) | 101 | 102 | 99% (90d) | Does not open (80%) | n/a | [#27](https://github.com/GameNative/gamenative-compat/issues/27) |
| 27 | [ ] | Fall Guys (EPIC) | 99 | 111 | 89% (90d) | Does not open (73%) | 5% | [#32](https://github.com/GameNative/gamenative-compat/issues/32) |
| 28 | [ ] | Burnout™ Paradise Remastered (STEAM) | 96 | 100 | 96% (90d) | Does not open (85%) | 12% | [#35](https://github.com/GameNative/gamenative-compat/issues/35) |
| 29 | [ ] | Black Mesa (STEAM) | 94 | 130 | 72% (90d) | Does not open (83%) | 11% | [#38](https://github.com/GameNative/gamenative-compat/issues/38) |
| 30 | [ ] | Dead Space 2 (STEAM) | 89 | 110 | 81% (90d) | Does not open (74%) | 41% | [#34](https://github.com/GameNative/gamenative-compat/issues/34) |
| 31 | [ ] | HELLDIVERS™ (STEAM) | 87 | 100 | 87% (90d) | Does not open (62%) | 45% | [#39](https://github.com/GameNative/gamenative-compat/issues/39) |
| 32 | [ ] | Duskfade (STEAM) | 87 | 89 | 98% (90d) | Does not open (95%) | n/a | [#43](https://github.com/GameNative/gamenative-compat/issues/43) |
| 33 | [ ] | Saints Row 2 (STEAM) | 86 | 100 | 91% (1.3.0) | Does not open (95%) | 48% | [#419](https://github.com/GameNative/gamenative-compat/issues/419) |
| 34 | [ ] | Sniper Elite 4 (STEAM) | 86 | 88 | 98% (90d) | Does not open (95%) | n/a | [#44](https://github.com/GameNative/gamenative-compat/issues/44) |
| 35 | [ ] | MECCHA CHAMELEON (STEAM) | 84 | 119 | 71% (90d) | Does not open (66%) | 52% | [#31](https://github.com/GameNative/gamenative-compat/issues/31) |
| 36 | [ ] | Call of Duty: Black Ops II - Zombies (STEAM) | 83 | 96 | 86% (90d) | Does not open (72%) | 58% | [#36](https://github.com/GameNative/gamenative-compat/issues/36) |
| 37 | [ ] | FINAL FANTASY XIII-2 (STEAM) | 82 | 85 | 96% (90d) | Does not open (92%) | n/a | [#41](https://github.com/GameNative/gamenative-compat/issues/41) |
| 38 | [ ] | GRID 2 (STEAM) | 80 | 84 | 95% (90d) | Does not open (67%) | n/a | [#25](https://github.com/GameNative/gamenative-compat/issues/25) |
| 39 | [ ] | Warhammer 40,000: Space Marine - Anniversary Edition (STEAM) | 79 | 85 | 93% (90d) | Does not open (70%) | n/a | [#37](https://github.com/GameNative/gamenative-compat/issues/37) |
| 40 | [ ] | Marvel Rivals (STEAM) | 78 | 88 | 89% (90d) | Does not open (81%) | 0% | [#47](https://github.com/GameNative/gamenative-compat/issues/47) |
| 41 | [ ] | The Wolf Among Us (STEAM) | 76 | 84 | 90% (90d) | Does not open (68%) | 14% | [#60](https://github.com/GameNative/gamenative-compat/issues/60) |
| 42 | [ ] | Darksiders (STEAM) | 75 | 91 | 82% (90d) | Does not open (67%) | n/a | [#56](https://github.com/GameNative/gamenative-compat/issues/56) |
| 43 | [ ] | Need for Speed™ Heat  (STEAM) | 74 | 88 | 84% (90d) | Does not open (75%) | 31% | [#49](https://github.com/GameNative/gamenative-compat/issues/49) |
| 44 | [ ] | Saints Row 2 (GOG) | 74 | 88 | 84% (90d) | Does not open (95%) | 44% | [#58](https://github.com/GameNative/gamenative-compat/issues/58) |
| 45 | [ ] | Borderlands GOTY (STEAM) | 74 | 80 | 93% (90d) | Does not open (91%) | 31% | [#48](https://github.com/GameNative/gamenative-compat/issues/48) |
| 46 | [ ] | Heroes of Might and Magic® 3: Complete (GOG) | 74 | 79 | 94% (90d) | Does not open (75%) | 6% | [#51](https://github.com/GameNative/gamenative-compat/issues/51) |
| 47 | [ ] | Door Kickers 2 (STEAM) | 72 | 77 | 100% (14d) | No graphics (87%) | n/a | [#57](https://github.com/GameNative/gamenative-compat/issues/57) |
| 48 | [ ] | XCOM: Enemy Unknown (STEAM) | 71 | 74 | 96% (90d) | Does not open (75%) | 11% | [#62](https://github.com/GameNative/gamenative-compat/issues/62) |
| 49 | [x] 2026-10-18 | Diablo® IV (STEAM) | 69 | 81 | 85% (90d) | Does not open (63%) | n/a | [#65](https://github.com/GameNative/gamenative-compat/issues/65) |
| 50 | [ ] | Spec Ops: The Line (STEAM) | 66 | 67 | 99% (90d) | Does not open (61%) | n/a | [#61](https://github.com/GameNative/gamenative-compat/issues/61) |
| 51 | [ ] | Metro 2033 (STEAM) | 65 | 81 | 80% (90d) | Does not open (64%) | 50% | [#63](https://github.com/GameNative/gamenative-compat/issues/63) |
| 52 | [ ] | GRID (STEAM) | 65 | 78 | 83% (90d) | Does not open (55%) | 48% | [#67](https://github.com/GameNative/gamenative-compat/issues/67) |
| 53 | [ ] | Path of Exile (STEAM) | 64 | 73 | 88% (90d) | Does not open (91%) | n/a | [#59](https://github.com/GameNative/gamenative-compat/issues/59) |
| 54 | [ ] | Ghost Trick: Phantom Detective (STEAM) | 64 | 64 | 100% (90d) | No graphics (55%) | 10% | [#72](https://github.com/GameNative/gamenative-compat/issues/72) |
| 55 | [ ] | DOOM (2016) (GOG) | 62 | 68 | 91% (90d) | Does not open (91%) | 41% | [#80](https://github.com/GameNative/gamenative-compat/issues/80) |
| 56 | [ ] | Three Kingdoms : Alias (STEAM) | 62 | 66 | 94% (90d) | No graphics (97%) | n/a | [#81](https://github.com/GameNative/gamenative-compat/issues/81) |
| 57 | [ ] | Apollo Justice: Ace Attorney Trilogy (STEAM) | 61 | 86 | 71% (90d) | Does not open (83%) | 57% | [#457](https://github.com/GameNative/gamenative-compat/issues/457) |
| 58 | [ ] | Horizon Zero Dawn™ Complete Edition (STEAM) | 61 | 70 | 87% (90d) | No graphics (49%) | 25% | [#90](https://github.com/GameNative/gamenative-compat/issues/90) |
| 59 | [ ] | Spore (STEAM) | 61 | 67 | 91% (90d) | Does not open (67%) | n/a | [#75](https://github.com/GameNative/gamenative-compat/issues/75) |
| 60 | [ ] | Call of Duty: World at War (STEAM) | 60 | 83 | 72% (90d) | Does not open (44%) | 54% | [#66](https://github.com/GameNative/gamenative-compat/issues/66) |
| 61 | [ ] | DOOM 3 (STEAM) | 60 | 68 | 88% (90d) | Does not open (89%) | n/a | [#78](https://github.com/GameNative/gamenative-compat/issues/78) |
| 62 | [ ] | GrandChase (STEAM) | 58 | 61 | 95% (90d) | Does not open (85%) | n/a | [#84](https://github.com/GameNative/gamenative-compat/issues/84) |
| 63 | [ ] | Overwatch® (STEAM) | 58 | 61 | 95% (90d) | Does not open (60%) | 20% | [#74](https://github.com/GameNative/gamenative-compat/issues/74) |
| 64 | [ ] | Heroes of Might & Magic III - HD Edition (STEAM) | 57 | 70 | 81% (90d) | Does not open (90%) | 56% | [#86](https://github.com/GameNative/gamenative-compat/issues/86) |
| 65 | [ ] | Watch_Dogs (STEAM) | 56 | 67 | 84% (90d) | Does not open (91%) | 19% | [#82](https://github.com/GameNative/gamenative-compat/issues/82) |
| 66 | [ ] | Fortune Mill (STEAM) | 56 | 57 | 98% (90d) | Does not open (89%) | n/a | [#68](https://github.com/GameNative/gamenative-compat/issues/68) |
| 67 | [ ] | Vampire Survivors (EPIC) | 55 | 77 | 71% (90d) | Does not open (64%) | 55% | [#434](https://github.com/GameNative/gamenative-compat/issues/434) |
| 68 | [ ] | Deus Ex: Game of the Year Edition (STEAM) | 55 | 70 | 79% (90d) | Does not open (82%) | 27% | [#76](https://github.com/GameNative/gamenative-compat/issues/76) |
| 69 | [ ] | Asphalt Legends  (STEAM) | 55 | 63 | 87% (90d) | Does not open (80%) | 50% | [#83](https://github.com/GameNative/gamenative-compat/issues/83) |
| 70 | [ ] | METAL SLUG 3 (STEAM) | 55 | 62 | 89% (90d) | Does not open (89%) | 14% | [#95](https://github.com/GameNative/gamenative-compat/issues/95) |
| 71 | [ ] | Max Payne 3 (STEAM) | 55 | 60 | 92% (90d) | Does not open (93%) | 41% | [#98](https://github.com/GameNative/gamenative-compat/issues/98) |
| 72 | [ ] | South Park The Fractured But Whole (STEAM) | 55 | 55 | 100% (90d) | Does not open (66%) | 21% | [#101](https://github.com/GameNative/gamenative-compat/issues/101) |
| 73 | [ ] | Split/Second (STEAM) | 54 | 63 | 86% (90d) | Does not open (78%) | n/a | [#89](https://github.com/GameNative/gamenative-compat/issues/89) |
| 74 | [ ] | Sleeping Dogs™ (STEAM) | 54 | 61 | 89% (90d) | Does not open (82%) | n/a | [#94](https://github.com/GameNative/gamenative-compat/issues/94) |
| 75 | [ ] | RoboCop: Rogue City (STEAM) | 54 | 58 | 93% (90d) | Does not open (42%) | n/a | [#100](https://github.com/GameNative/gamenative-compat/issues/100) |
| 76 | [ ] | Hitman: Absolution (STEAM) | 53 | 58 | 91% (90d) | Does not open (85%) | n/a | [#105](https://github.com/GameNative/gamenative-compat/issues/105) |
| 77 | [ ] | Command & Conquer: Red Alert™ 2 and Yuri’s Revenge™ (STEAM) | 53 | 55 | 96% (90d) | No graphics (60%) | 8% | [#93](https://github.com/GameNative/gamenative-compat/issues/93) |
| 78 | [ ] | STAR WARS Zero Company™ (STEAM) | 53 | 55 | 96% (90d) | Does not open (64%) | n/a | [#107](https://github.com/GameNative/gamenative-compat/issues/107) |
| 79 | [ ] | Enshrouded (STEAM) | 53 | 54 | 98% (90d) | Does not open (92%) | 15% | [#129](https://github.com/GameNative/gamenative-compat/issues/129) |
| 80 | [ ] | tModLoader (STEAM) | 52 | 60 | 87% (90d) | Does not open (83%) | 5% | [#73](https://github.com/GameNative/gamenative-compat/issues/73) |
| 81 | [ ] | Trackmania (STEAM) | 51 | 64 | 80% (90d) | Does not open (82%) | 53% | [#117](https://github.com/GameNative/gamenative-compat/issues/117) |
| 82 | [ ] | The Survivalists (STEAM) | 51 | 53 | 96% (90d) | Does not open (98%) | n/a | [#85](https://github.com/GameNative/gamenative-compat/issues/85) |
| 83 | [ ] | Sandustry (STEAM) | 50 | 61 | 82% (90d) | Does not open (73%) | n/a | [#113](https://github.com/GameNative/gamenative-compat/issues/113) |
| 84 | [ ] | Scott Pilgrim vs The World (STEAM) | 50 | 50 | 100% (90d) | Does not open (81%) | n/a | [#109](https://github.com/GameNative/gamenative-compat/issues/109) |
| 85 | [ ] | ARC Raiders (STEAM) | 49 | 54 | 91% (90d) | Does not open (93%) | 0% | [#104](https://github.com/GameNative/gamenative-compat/issues/104) |
| 86 | [ ] | Diablo + Hellfire (GOG) | 49 | 54 | 91% (90d) | Does not open (69%) | n/a | [#111](https://github.com/GameNative/gamenative-compat/issues/111) |
| 87 | [ ] | Prince of Persia The Lost Crown (STEAM) | 49 | 54 | 91% (90d) | Does not open (94%) | 34% | [#114](https://github.com/GameNative/gamenative-compat/issues/114) |
| 88 | [ ] | Dungeons & Dragons: Chronicles of Mystara (STEAM) | 49 | 51 | 96% (90d) | Does not open (98%) | n/a | [#71](https://github.com/GameNative/gamenative-compat/issues/71) |
| 89 | [ ] | DOOM Eternal (STEAM) | 48 | 50 | 96% (90d) | Does not open (69%) | n/a | [#115](https://github.com/GameNative/gamenative-compat/issues/115) |
| 90 | [ ] | Mafia: Definitive Edition (GOG) | 47 | 64 | 73% (90d) | Does not open (87%) | 29% | [#125](https://github.com/GameNative/gamenative-compat/issues/125) |
| 91 | [ ] | Aliens vs. Predator (STEAM) | 47 | 52 | 90% (90d) | No graphics (53%) | 21% | [#96](https://github.com/GameNative/gamenative-compat/issues/96) |
| 92 | [ ] | STAR WARS™ Republic Commando (STEAM) | 47 | 50 | 94% (90d) | Does not open (81%) | 44% | [#106](https://github.com/GameNative/gamenative-compat/issues/106) |
| 93 | [ ] | State of Decay 2 (STEAM) | 46 | 65 | 71% (90d) | Does not open (93%) | n/a | [#116](https://github.com/GameNative/gamenative-compat/issues/116) |
| 94 | [ ] | Tales of Berseria (STEAM) | 46 | 47 | 98% (90d) | Does not open (88%) | n/a | [#123](https://github.com/GameNative/gamenative-compat/issues/123) |
| 95 | [ ] | STAR WARS™ Episode I Racer (STEAM) | 45 | 46 | 98% (90d) | Does not open (82%) | 45% | [#122](https://github.com/GameNative/gamenative-compat/issues/122) |
| 96 | [ ] | Fallout (GOG) | 44 | 63 | 70% (90d) | Does not open (72%) | 53% | [#133](https://github.com/GameNative/gamenative-compat/issues/133) |
| 97 | [ ] | Blossom Tales: The Sleeping King (STEAM) | 44 | 49 | 90% (90d) | Does not open (74%) | 7% | [#119](https://github.com/GameNative/gamenative-compat/issues/119) |
| 98 | [ ] | Axiom Verge 2 (STEAM) | 44 | 45 | 98% (90d) | Does not open (66%) | 7% | [#134](https://github.com/GameNative/gamenative-compat/issues/134) |
| 99 | [ ] | GOALS (STEAM) | 43 | 50 | 86% (90d) | Does not open (78%) | 33% | [#118](https://github.com/GameNative/gamenative-compat/issues/118) |
| 100 | [ ] | Shin Megami Tensei III Nocturne HD Remaster (STEAM) | 43 | 44 | 98% (90d) | Does not open (62%) | 0% | [#108](https://github.com/GameNative/gamenative-compat/issues/108) |
| 101 | [ ] | DJMAX RESPECT V (STEAM) | 42 | 46 | 91% (90d) | Does not open (84%) | n/a | [#137](https://github.com/GameNative/gamenative-compat/issues/137) |
| 102 | [ ] | Sir, We Have an Orc Problem (STEAM) | 41 | 48 | 85% (90d) | Does not open (86%) | n/a | [#145](https://github.com/GameNative/gamenative-compat/issues/145) |
| 103 | [ ] | Mafia (STEAM) | 41 | 46 | 89% (90d) | Does not open (66%) | 36% | [#120](https://github.com/GameNative/gamenative-compat/issues/120) |
| 104 | [ ] | ScourgeBringer (STEAM) | 41 | 46 | 89% (90d) | Does not open (68%) | 7% | [#141](https://github.com/GameNative/gamenative-compat/issues/141) |
| 105 | [ ] | Elite Dangerous (STEAM) | 41 | 45 | 91% (90d) | Does not open (76%) | 55% | [#132](https://github.com/GameNative/gamenative-compat/issues/132) |
| 106 | [ ] | Marvel's Spider-Man 2 (STEAM) | 41 | 43 | 95% (90d) | Does not open (82%) | n/a | [#143](https://github.com/GameNative/gamenative-compat/issues/143) |
| 107 | [ ] | Dark Messiah of Might & Magic Single Player (STEAM) | 41 | 42 | 98% (90d) | Does not open (61%) | n/a | [#121](https://github.com/GameNative/gamenative-compat/issues/121) |
| 108 | [ ] | Monster Hunter Stories 3: Twisted Reflection (STEAM) | 40 | 42 | 95% (90d) | Does not open (91%) | 31% | [#153](https://github.com/GameNative/gamenative-compat/issues/153) |
| 109 | [ ] | The Darkness II (STEAM) | 40 | 40 | 100% (90d) | Does not open (81%) | n/a | [#144](https://github.com/GameNative/gamenative-compat/issues/144) |
| 110 | [ ] | STAR WARS™ Episode I: Racer (GOG) | 39 | 45 | 87% (90d) | No graphics (64%) | n/a | [#162](https://github.com/GameNative/gamenative-compat/issues/162) |
| 111 | [ ] | Alpha Protocol (STEAM) | 39 | 43 | 91% (90d) | Does not open (69%) | n/a | [#135](https://github.com/GameNative/gamenative-compat/issues/135) |
| 112 | [ ] | Death Stranding (EPIC) | 39 | 42 | 93% (90d) | Does not open (76%) | n/a | [#151](https://github.com/GameNative/gamenative-compat/issues/151) |
| 113 | [ ] | FINAL FANTASY VII REBIRTH (STEAM) | 39 | 41 | 95% (90d) | Does not open (61%) | n/a | [#158](https://github.com/GameNative/gamenative-compat/issues/158) |
| 114 | [ ] | Forza Horizon 6 (STEAM) | 39 | 40 | 98% (90d) | Does not open (62%) | n/a | [#138](https://github.com/GameNative/gamenative-compat/issues/138) |
| 115 | [ ] | GeoGuessr Steam Edition (STEAM) | 39 | 40 | 98% (90d) | No graphics (62%) | n/a | [#154](https://github.com/GameNative/gamenative-compat/issues/154) |
| 116 | [ ] | Utopia Must Fall (STEAM) | 39 | 39 | 100% (90d) | Does not open (84%) | n/a | [#155](https://github.com/GameNative/gamenative-compat/issues/155) |
| 117 | [ ] | Call of Duty® (STEAM) | 38 | 48 | 79% (90d) | No graphics (58%) | n/a | [#124](https://github.com/GameNative/gamenative-compat/issues/124) |
| 118 | [ ] | BIT.TRIP RUNNER (STEAM) | 38 | 40 | 95% (90d) | No graphics (60%) | n/a | [#160](https://github.com/GameNative/gamenative-compat/issues/160) |
| 119 | [ ] | Barotrauma (STEAM) | 38 | 40 | 95% (90d) | Does not open (97%) | n/a | [#146](https://github.com/GameNative/gamenative-compat/issues/146) |
| 120 | [ ] | FINAL FANTASY VIII (STEAM) | 37 | 45 | 82% (90d) | Does not open (64%) | n/a | [#150](https://github.com/GameNative/gamenative-compat/issues/150) |
| 121 | [ ] | L.A. Noire (STEAM) | 37 | 44 | 84% (90d) | Does not open (96%) | 54% | [#446](https://github.com/GameNative/gamenative-compat/issues/446) |
| 122 | [ ] | Wonder Boy The Dragons Trap (EPIC) | 37 | 40 | 93% (90d) | Does not open (64%) | n/a | [#142](https://github.com/GameNative/gamenative-compat/issues/142) |
| 123 | [ ] | Dragon's Dogma 2 (STEAM) | 37 | 38 | 97% (90d) | Does not open (91%) | n/a | [#177](https://github.com/GameNative/gamenative-compat/issues/177) |
| 124 | [ ] | Hitman: Blood Money (STEAM) | 37 | 38 | 97% (90d) | Does not open (88%) | 17% | [#128](https://github.com/GameNative/gamenative-compat/issues/128) |
| 125 | [ ] | Mafia II (Classic) (GOG) | 36 | 51 | 71% (90d) | Does not open (94%) | 20% | [#435](https://github.com/GameNative/gamenative-compat/issues/435) |
| 126 | [ ] | CODE VEIN (STEAM) | 36 | 48 | 75% (90d) | Does not open (72%) | 26% | [#181](https://github.com/GameNative/gamenative-compat/issues/181) |
| 127 | [ ] | Gauntlet™  (STEAM) | 36 | 47 | 77% (90d) | Does not open (72%) | n/a | [#157](https://github.com/GameNative/gamenative-compat/issues/157) |
| 128 | [ ] | Beat Saber (STEAM) | 36 | 40 | 90% (90d) | Does not open (45%) | 36% | [#136](https://github.com/GameNative/gamenative-compat/issues/136) |
| 129 | [ ] | Beholder (EPIC) | 35 | 42 | 83% (90d) | Does not open (58%) | n/a | [#184](https://github.com/GameNative/gamenative-compat/issues/184) |
| 130 | [ ] | Fahrenheit: Indigo Prophecy Remastered (STEAM) | 35 | 40 | 88% (90d) | Does not open (69%) | n/a | [#190](https://github.com/GameNative/gamenative-compat/issues/190) |
| 131 | [ ] | OneShot (STEAM) | 35 | 40 | 88% (90d) | Does not open (97%) | 30% | [#174](https://github.com/GameNative/gamenative-compat/issues/174) |
| 132 | [ ] | PRAGMATA (STEAM) | 35 | 37 | 95% (90d) | Does not open (57%) | n/a | [#176](https://github.com/GameNative/gamenative-compat/issues/176) |
| 133 | [ ] | BattleBit Remastered (STEAM) | 34 | 38 | 89% (90d) | Does not open (61%) | n/a | [#159](https://github.com/GameNative/gamenative-compat/issues/159) |
| 134 | [ ] | Forza Horizon 5 (STEAM) | 34 | 36 | 94% (90d) | Does not open (72%) | n/a | [#187](https://github.com/GameNative/gamenative-compat/issues/187) |
| 135 | [ ] | DiRT Showdown (STEAM) | 34 | 35 | 97% (90d) | Does not open (63%) | n/a | [#168](https://github.com/GameNative/gamenative-compat/issues/168) |
| 136 | [ ] | Dark Sector (STEAM) | 33 | 45 | 73% (90d) | Does not open (67%) | 31% | [#163](https://github.com/GameNative/gamenative-compat/issues/163) |
| 137 | [ ] | ELDEN RING NIGHTREIGN (STEAM) | 33 | 44 | 75% (90d) | Does not open (60%) | n/a | [#180](https://github.com/GameNative/gamenative-compat/issues/180) |
| 138 | [ ] | Mass Effect (2007) (STEAM) | 33 | 41 | 80% (90d) | Does not open (81%) | n/a | [#165](https://github.com/GameNative/gamenative-compat/issues/165) |
| 139 | [ ] | Wolfenstein 3D (STEAM) | 33 | 36 | 92% (90d) | Does not open (52%) | n/a | [#200](https://github.com/GameNative/gamenative-compat/issues/200) |
| 140 | [ ] | Lara Croft and the Guardian of Light (STEAM) | 33 | 35 | 94% (90d) | Does not open (74%) | n/a | [#167](https://github.com/GameNative/gamenative-compat/issues/167) |
| 141 | [ ] | Rayman Legends (STEAM) | 33 | 34 | 97% (90d) | Does not open (96%) | 55% | [#201](https://github.com/GameNative/gamenative-compat/issues/201) |
| 142 | [ ] | Umamusume: Pretty Derby (STEAM) | 33 | 34 | 97% (90d) | Does not open (81%) | n/a | [#178](https://github.com/GameNative/gamenative-compat/issues/178) |
| 143 | [ ] | Need for Speed™ Rivals (STEAM) | 32 | 39 | 82% (90d) | Does not open (62%) | 37% | [#185](https://github.com/GameNative/gamenative-compat/issues/185) |
| 144 | [ ] | Tales of Zestiria (STEAM) | 32 | 37 | 86% (90d) | Does not open (81%) | 50% | [#194](https://github.com/GameNative/gamenative-compat/issues/194) |
| 145 | [ ] | Wuthering Waves (STEAM) | 32 | 34 | 94% (90d) | Does not open (81%) | n/a | [#216](https://github.com/GameNative/gamenative-compat/issues/216) |
| 146 | [ ] | Far Cry® 3 Blood Dragon (STEAM) | 32 | 33 | 97% (90d) | Does not open (72%) | n/a | [#208](https://github.com/GameNative/gamenative-compat/issues/208) |
| 147 | [ ] | Muv-Luv (STEAM) | 32 | 33 | 97% (90d) | Does not open (86%) | 40% | [#196](https://github.com/GameNative/gamenative-compat/issues/196) |
| 148 | [ ] | WRC 7 (STEAM) | 32 | 33 | 97% (90d) | Does not open (68%) | n/a | [#202](https://github.com/GameNative/gamenative-compat/issues/202) |
| 149 | [ ] | Quantum Break (STEAM) | 32 | 32 | 100% (90d) | Does not open (91%) | n/a | [#211](https://github.com/GameNative/gamenative-compat/issues/211) |
| 150 | [ ] | CARRION (GOG) | 31 | 38 | 82% (90d) | Does not open (76%) | n/a | [#213](https://github.com/GameNative/gamenative-compat/issues/213) |
| 151 | [ ] | Far Cry 4 (STEAM) | 31 | 35 | 89% (90d) | Does not open (100%) | n/a | [#215](https://github.com/GameNative/gamenative-compat/issues/215) |
| 152 | [ ] | The Lord of the Rings: War in the North (STEAM) | 31 | 33 | 94% (90d) | Does not open (86%) | n/a | [#195](https://github.com/GameNative/gamenative-compat/issues/195) |
| 153 | [ ] | King's Bounty: The Legend (STEAM) | 31 | 32 | 97% (90d) | Does not open (100%) | n/a | [#218](https://github.com/GameNative/gamenative-compat/issues/218) |
| 154 | [ ] | Grand Theft Auto III - The Definitive Edition (STEAM) | 31 | 31 | 100% (90d) | Does not open (92%) | 11% | [#219](https://github.com/GameNative/gamenative-compat/issues/219) |
| 155 | [ ] | Borderlands: The Pre-Sequel (EPIC) | 30 | 39 | 77% (90d) | Does not open (63%) | 58% | [#221](https://github.com/GameNative/gamenative-compat/issues/221) |
| 156 | [ ] | Insaniquarium! Deluxe (STEAM) | 30 | 38 | 79% (90d) | Does not open (85%) | 27% | [#189](https://github.com/GameNative/gamenative-compat/issues/189) |
| 157 | [ ] | CPM 2 (STEAM) | 30 | 37 | 80% (14d) | Does not open (90%) | 10% | [#243](https://github.com/GameNative/gamenative-compat/issues/243) |
| 158 | [ ] | Magicka (STEAM) | 30 | 33 | 91% (90d) | Does not open (64%) | n/a | [#191](https://github.com/GameNative/gamenative-compat/issues/191) |
| 159 | [ ] | Sonic Racing: CrossWorlds (EPIC) | 30 | 31 | 97% (90d) | Does not open (95%) | n/a | [#226](https://github.com/GameNative/gamenative-compat/issues/226) |
| 160 | [ ] | Breath of Fire IV (STEAM) | 30 | 30 | 100% (90d) | Does not open (60%) | 19% | [#203](https://github.com/GameNative/gamenative-compat/issues/203) |
| 161 | [ ] | EA SPORTS FC™ 26 (STEAM) | 29 | 37 | 78% (90d) | Does not open (77%) | n/a | [#172](https://github.com/GameNative/gamenative-compat/issues/172) |
| 162 | [ ] | Subnautica 2 (STEAM) | 29 | 36 | 81% (90d) | Does not open (68%) | 55% | [#205](https://github.com/GameNative/gamenative-compat/issues/205) |
| 163 | [ ] | Zuma Deluxe (STEAM) | 29 | 33 | 88% (90d) | Does not open (96%) | n/a | [#206](https://github.com/GameNative/gamenative-compat/issues/206) |
| 164 | [ ] | Persona 5 Strikers (STEAM) | 29 | 32 | 91% (90d) | Does not open (73%) | n/a | [#207](https://github.com/GameNative/gamenative-compat/issues/207) |
| 165 | [ ] | Borderlands 2 RU (STEAM) | 29 | 31 | 94% (90d) | Does not open (60%) | n/a | [#217](https://github.com/GameNative/gamenative-compat/issues/217) |
| 166 | [ ] | Tom Clancy's Splinter Cell: Conviction (STEAM) | 29 | 29 | 100% (90d) | Does not open (91%) | n/a | [#227](https://github.com/GameNative/gamenative-compat/issues/227) |
| 167 | [ ] | Audiosurf (STEAM) | 28 | 40 | 70% (90d) | Does not open (46%) | 43% | [#463](https://github.com/GameNative/gamenative-compat/issues/463) |
| 168 | [ ] | CRUEL (STEAM) | 28 | 35 | 80% (90d) | Does not open (89%) | n/a | [#242](https://github.com/GameNative/gamenative-compat/issues/242) |
| 169 | [ ] | Blossom Tales 2: The Minotaur Prince (STEAM) | 28 | 31 | 90% (90d) | Does not open (81%) | n/a | [#231](https://github.com/GameNative/gamenative-compat/issues/231) |
| 170 | [ ] | Resident Evil Requiem (STEAM) | 28 | 29 | 97% (90d) | Does not open (77%) | n/a | [#210](https://github.com/GameNative/gamenative-compat/issues/210) |
| 171 | [ ] | Solo Leveling: ARISE OVERDRIVE (STEAM) | 28 | 28 | 100% (90d) | Does not open (62%) | n/a | [#239](https://github.com/GameNative/gamenative-compat/issues/239) |
| 172 | [ ] | Baldur's Gate: Enhanced Edition (GOG) | 27 | 34 | 79% (90d) | No graphics (52%) | 8% | [#183](https://github.com/GameNative/gamenative-compat/issues/183) |
| 173 | [ ] | The Planet Crafter (STEAM) | 27 | 33 | 82% (90d) | Does not open (48%) | n/a | [#229](https://github.com/GameNative/gamenative-compat/issues/229) |
| 174 | [ ] | skate.™ (EPIC) | 27 | 31 | 87% (90d) | Does not open (90%) | n/a | [#230](https://github.com/GameNative/gamenative-compat/issues/230) |
| 175 | [ ] | Turing Complete (STEAM) | 27 | 30 | 90% (90d) | Does not open (92%) | n/a | [#238](https://github.com/GameNative/gamenative-compat/issues/238) |
| 176 | [ ] | Bingle Bingle (STEAM) | 27 | 28 | 96% (90d) | Does not open (82%) | n/a | [#225](https://github.com/GameNative/gamenative-compat/issues/225) |
| 177 | [ ] | Northgard: Definitive Edition (STEAM) | 27 | 28 | 96% (90d) | Does not open (96%) | n/a | [#232](https://github.com/GameNative/gamenative-compat/issues/232) |
| 178 | [ ] | STAR WARS: Galactic Racer™ (STEAM) | 27 | 27 | 100% (90d) | Does not open (71%) | 0% | [#288](https://github.com/GameNative/gamenative-compat/issues/288) |
| 179 | [ ] | Kenshi (STEAM) | 26 | 34 | 76% (90d) | Does not open (80%) | 12% | [#452](https://github.com/GameNative/gamenative-compat/issues/452) |
| 180 | [ ] | ENDLESS Space™ 2 (STEAM) | 26 | 31 | 84% (90d) | Does not open (94%) | n/a | [#246](https://github.com/GameNative/gamenative-compat/issues/246) |
| 181 | [ ] | Singularity™ (GOG) | 26 | 31 | 84% (90d) | Does not open (100%) | n/a | [#247](https://github.com/GameNative/gamenative-compat/issues/247) |
| 182 | [ ] | Assassin's Creed IV Black Flag (STEAM) | 26 | 29 | 90% (90d) | Does not open (91%) | 50% | [#244](https://github.com/GameNative/gamenative-compat/issues/244) |
| 183 | [ ] | Marvel's Midnight Suns (STEAM) | 26 | 29 | 90% (90d) | Does not open (79%) | n/a | [#224](https://github.com/GameNative/gamenative-compat/issues/224) |
| 184 | [ ] | PAYDAY 2 (STEAM) | 26 | 29 | 90% (90d) | Does not open (77%) | 33% | [#260](https://github.com/GameNative/gamenative-compat/issues/260) |
| 185 | [ ] | AION 2 (STEAM) | 26 | 28 | 93% (90d) | Does not open (65%) | 14% | [#282](https://github.com/GameNative/gamenative-compat/issues/282) |
| 186 | [ ] | Jade Empire: Special Edition (STEAM) | 26 | 28 | 93% (90d) | Does not open (92%) | 53% | [#251](https://github.com/GameNative/gamenative-compat/issues/251) |
| 187 | [ ] | Peggle Nights (STEAM) | 26 | 28 | 93% (90d) | Does not open (95%) | n/a | [#252](https://github.com/GameNative/gamenative-compat/issues/252) |
| 188 | [ ] | Tony Hawk's™ Pro Skater™ 1 + 2 (EPIC) | 26 | 27 | 96% (90d) | Does not open (82%) | 44% | [#319](https://github.com/GameNative/gamenative-compat/issues/319) |
| 189 | [ ] | Isle of Reveries (STEAM) | 26 | 26 | 100% (90d) | Does not open (95%) | n/a | [#254](https://github.com/GameNative/gamenative-compat/issues/254) |
| 190 | [ ] | Content Warning (STEAM) | 25 | 33 | 76% (90d) | Does not open (55%) | n/a | [#241](https://github.com/GameNative/gamenative-compat/issues/241) |
| 191 | [ ] | Mirror's Edge™ (GOG) | 25 | 33 | 76% (90d) | No graphics (67%) | n/a | [#235](https://github.com/GameNative/gamenative-compat/issues/235) |
| 192 | [ ] | Knights of Pen and Paper 2 (STEAM) | 25 | 31 | 81% (90d) | Does not open (45%) | n/a | [#259](https://github.com/GameNative/gamenative-compat/issues/259) |
| 193 | [ ] | Bionic Commando Rearmed (STEAM) | 25 | 28 | 89% (90d) | Does not open (74%) | n/a | [#245](https://github.com/GameNative/gamenative-compat/issues/245) |
| 194 | [ ] | The Swapper (STEAM) | 25 | 28 | 89% (90d) | Does not open (56%) | n/a | [#283](https://github.com/GameNative/gamenative-compat/issues/283) |
| 195 | [ ] | Alien Breed: Impact (STEAM) | 25 | 27 | 93% (90d) | Does not open (80%) | n/a | [#249](https://github.com/GameNative/gamenative-compat/issues/249) |
| 196 | [ ] | Euro Truck Simulator (STEAM) | 25 | 26 | 96% (90d) | Does not open (94%) | n/a | [#253](https://github.com/GameNative/gamenative-compat/issues/253) |
| 197 | [ ] | Gears 5 (STEAM) | 25 | 25 | 100% (90d) | Does not open (90%) | n/a | [#264](https://github.com/GameNative/gamenative-compat/issues/264) |
| 198 | [ ] | Spiral Knights (STEAM) | 25 | 25 | 100% (90d) | Does not open (74%) | n/a | [#263](https://github.com/GameNative/gamenative-compat/issues/263) |
| 199 | [ ] | Cities: Skylines (STEAM) | 24 | 34 | 71% (90d) | Does not open (59%) | n/a | [#233](https://github.com/GameNative/gamenative-compat/issues/233) |
| 200 | [ ] | MARVEL Tōkon: Fighting Souls (STEAM) | 24 | 34 | 71% (90d) | Does not open (95%) | n/a | [#266](https://github.com/GameNative/gamenative-compat/issues/266) |
| 201 | [ ] | CarX Street (STEAM) | 24 | 31 | 77% (90d) | Does not open (80%) | n/a | [#255](https://github.com/GameNative/gamenative-compat/issues/255) |
| 202 | [ ] | SOMA (STEAM) | 24 | 31 | 77% (90d) | Does not open (77%) | n/a | [#256](https://github.com/GameNative/gamenative-compat/issues/256) |
| 203 | [ ] | Melatonin (STEAM) | 24 | 25 | 96% (90d) | Does not open (60%) | 50% | [#272](https://github.com/GameNative/gamenative-compat/issues/272) |
| 204 | [ ] | Beyond Good & Evil™ (GOG) | 23 | 28 | 82% (90d) | Does not open (100%) | n/a | [#330](https://github.com/GameNative/gamenative-compat/issues/330) |
| 205 | [ ] | SimCity 4 Deluxe (STEAM) | 23 | 27 | 85% (90d) | Does not open (82%) | n/a | [#186](https://github.com/GameNative/gamenative-compat/issues/186) |
| 206 | [ ] | Tearscape (STEAM) | 23 | 27 | 85% (90d) | Controller issues (53%) | n/a | [#248](https://github.com/GameNative/gamenative-compat/issues/248) |
| 207 | [ ] | Resident Evil Village Gold Edition Gameplay Demo (STEAM) | 23 | 26 | 88% (90d) | Does not open (63%) | n/a | [#331](https://github.com/GameNative/gamenative-compat/issues/331) |
| 208 | [ ] | They Are Billions (STEAM) | 23 | 26 | 88% (90d) | Does not open (70%) | n/a | [#281](https://github.com/GameNative/gamenative-compat/issues/281) |
| 209 | [ ] | Fallen Aces (STEAM) | 23 | 25 | 92% (90d) | No graphics (67%) | n/a | [#250](https://github.com/GameNative/gamenative-compat/issues/250) |
| 210 | [ ] | Need for Speed™ Unbound (STEAM) | 23 | 24 | 96% (90d) | Does not open (79%) | n/a | [#285](https://github.com/GameNative/gamenative-compat/issues/285) |
| 211 | [ ] | Rayman Legends (EPIC) | 23 | 24 | 96% (90d) | Does not open (92%) | n/a | [#286](https://github.com/GameNative/gamenative-compat/issues/286) |
| 212 | [ ] | Marie's Adventure (STEAM) | 23 | 23 | 100% (90d) | Does not open (100%) | n/a | [#287](https://github.com/GameNative/gamenative-compat/issues/287) |
| 213 | [ ] | Foretales (EPIC) | 22 | 31 | 71% (90d) | Does not open (65%) | n/a | [#451](https://github.com/GameNative/gamenative-compat/issues/451) |
| 214 | [ ] | Beat Cop (STEAM) | 22 | 30 | 73% (90d) | Does not open (76%) | n/a | [#291](https://github.com/GameNative/gamenative-compat/issues/291) |
| 215 | [ ] | Half-Life: Blue Shift (STEAM) | 22 | 28 | 79% (90d) | Does not open (85%) | n/a | [#305](https://github.com/GameNative/gamenative-compat/issues/305) |
| 216 | [ ] | My Singing Monsters (STEAM) | 22 | 28 | 79% (90d) | Does not open (82%) | n/a | [#278](https://github.com/GameNative/gamenative-compat/issues/278) |
| 217 | [ ] | ONE PIECE: PIRATE WARRIORS 4 (STEAM) | 22 | 28 | 79% (90d) | Does not open (64%) | n/a | [#277](https://github.com/GameNative/gamenative-compat/issues/277) |
| 218 | [ ] | PICO PARK:Classic Edition (STEAM) | 22 | 26 | 85% (90d) | Does not open (90%) | n/a | [#279](https://github.com/GameNative/gamenative-compat/issues/279) |
| 219 | [ ] | Tom Clancy's Ghost Recon® Wildlands (STEAM) | 22 | 26 | 85% (90d) | Does not open (94%) | n/a | [#280](https://github.com/GameNative/gamenative-compat/issues/280) |
| 220 | [ ] | Halo: Spartan Assault (STEAM) | 22 | 25 | 88% (90d) | Does not open (80%) | n/a | [#284](https://github.com/GameNative/gamenative-compat/issues/284) |
| 221 | [ ] | Assassin's Creed Rogue (STEAM) | 22 | 24 | 92% (90d) | Does not open (63%) | n/a | [#271](https://github.com/GameNative/gamenative-compat/issues/271) |
| 222 | [ ] | Hell Yeah! (STEAM) | 22 | 23 | 96% (90d) | Does not open (82%) | n/a | [#297](https://github.com/GameNative/gamenative-compat/issues/297) |
| 223 | [ ] | No More Room in Hell (STEAM) | 22 | 23 | 96% (90d) | Does not open (95%) | n/a | [#365](https://github.com/GameNative/gamenative-compat/issues/365) |
| 224 | [ ] | The Lantern of the Laughless Saint (STEAM) | 22 | 23 | 96% (90d) | Does not open (79%) | n/a | [#299](https://github.com/GameNative/gamenative-compat/issues/299) |
| 225 | [ ] | Watch Dogs (EPIC) | 22 | 22 | 100% (90d) | Does not open (89%) | n/a | [#289](https://github.com/GameNative/gamenative-compat/issues/289) |
| 226 | [ ] | Aggelos 2 (STEAM) | 21 | 26 | 81% (90d) | No graphics (90%) | n/a | [#307](https://github.com/GameNative/gamenative-compat/issues/307) |
| 227 | [ ] | Command & Conquer™ Red Alert™ 3 (STEAM) | 21 | 26 | 81% (90d) | Does not open (50%) | n/a | [#327](https://github.com/GameNative/gamenative-compat/issues/327) |
| 228 | [ ] | Apex Legends (STEAM) | 21 | 24 | 88% (90d) | Does not open (79%) | n/a | [#261](https://github.com/GameNative/gamenative-compat/issues/261) |
| 229 | [ ] | Dragon Age™ Inquisition (STEAM) | 21 | 24 | 88% (90d) | Does not open (76%) | n/a | [#296](https://github.com/GameNative/gamenative-compat/issues/296) |
| 230 | [ ] | Sapphire Safari (GOG) | 21 | 24 | 88% (90d) | Does not open (89%) | n/a | [#385](https://github.com/GameNative/gamenative-compat/issues/385) |
| 231 | [ ] | The Elder Scrolls IV: Oblivion Remastered (STEAM) | 21 | 24 | 88% (90d) | Does not open (53%) | n/a | [#312](https://github.com/GameNative/gamenative-compat/issues/312) |
| 232 | [ ] | Need for Speed: Undercover (STEAM) | 21 | 23 | 91% (90d) | Does not open (88%) | n/a | [#292](https://github.com/GameNative/gamenative-compat/issues/292) |
| 233 | [ ] | SONIC THE HEDGEHOG 4 Episode I (STEAM) | 21 | 23 | 91% (90d) | Does not open (90%) | n/a | [#294](https://github.com/GameNative/gamenative-compat/issues/294) |
| 234 | [ ] | Chronicles of the Wolf (STEAM) | 21 | 22 | 95% (90d) | No graphics (85%) | n/a | [#314](https://github.com/GameNative/gamenative-compat/issues/314) |
| 235 | [ ] | Combat Master (STEAM) | 21 | 22 | 95% (90d) | Does not open (72%) | n/a | [#262](https://github.com/GameNative/gamenative-compat/issues/262) |
| 236 | [ ] | Monster Hunter Rise: Sunbreak Demo (STEAM) | 21 | 22 | 95% (90d) | Does not open (69%) | n/a | [#318](https://github.com/GameNative/gamenative-compat/issues/318) |
| 237 | [ ] | Pathway (EPIC) | 21 | 22 | 95% (90d) | Does not open (58%) | n/a | [#298](https://github.com/GameNative/gamenative-compat/issues/298) |
| 238 | [ ] | The Last of Us™ Part I (STEAM) | 21 | 22 | 95% (90d) | Does not open (87%) | n/a | [#300](https://github.com/GameNative/gamenative-compat/issues/300) |
| 239 | [ ] | Age of Mythology: Retold (STEAM) | 21 | 21 | 100% (90d) | Does not open (81%) | n/a | [#295](https://github.com/GameNative/gamenative-compat/issues/295) |
| 240 | [ ] | Resident Evil 3 Nemesis (1999) (STEAM) | 21 | 21 | 100% (90d) | Does not open (86%) | n/a | [#273](https://github.com/GameNative/gamenative-compat/issues/273) |
| 241 | [ ] | Sid Meier's Alpha Centauri™ Planetary Pack (GOG) | 21 | 21 | 100% (90d) | Does not open (71%) | n/a | [#302](https://github.com/GameNative/gamenative-compat/issues/302) |
| 242 | [ ] | Fishing Planet (STEAM) | 20 | 28 | 71% (90d) | Does not open (93%) | 33% | [#458](https://github.com/GameNative/gamenative-compat/issues/458) |
| 243 | [ ] | Dungeon Keeper™ 2 (GOG) | 20 | 27 | 74% (90d) | Does not open (100%) | n/a | [#328](https://github.com/GameNative/gamenative-compat/issues/328) |
| 244 | [ ] | TEKKEN 8 (STEAM) | 20 | 27 | 74% (90d) | Does not open (88%) | n/a | [#306](https://github.com/GameNative/gamenative-compat/issues/306) |
| 245 | [ ] | Yuppie Psycho (STEAM) | 20 | 27 | 74% (90d) | Does not open (76%) | n/a | [#325](https://github.com/GameNative/gamenative-compat/issues/325) |
| 246 | [ ] | Fall Guys (STEAM) | 20 | 26 | 77% (90d) | Does not open (92%) | n/a | [#370](https://github.com/GameNative/gamenative-compat/issues/370) |
| 247 | [ ] | Sid Meier's Pirates! (STEAM) | 20 | 26 | 77% (90d) | Does not open (92%) | n/a | [#293](https://github.com/GameNative/gamenative-compat/issues/293) |
| 248 | [ ] | BAJA: Edge of Control HD (STEAM) | 20 | 25 | 80% (90d) | Does not open (100%) | n/a | [#333](https://github.com/GameNative/gamenative-compat/issues/333) |
| 249 | [ ] | Assassin's Creed Brotherhood (STEAM) | 20 | 23 | 87% (90d) | Does not open (78%) | n/a | [#310](https://github.com/GameNative/gamenative-compat/issues/310) |
| 250 | [ ] | Mafia III: Definitive Edition (STEAM) | 20 | 23 | 87% (90d) | Does not open (95%) | n/a | [#311](https://github.com/GameNative/gamenative-compat/issues/311) |
| 251 | [ ] | Grounded 2 (STEAM) | 20 | 21 | 95% (90d) | Does not open (56%) | n/a | [#317](https://github.com/GameNative/gamenative-compat/issues/317) |
| 252 | [ ] | Meowgic (STEAM) | 20 | 21 | 95% (90d) | Does not open (90%) | n/a | [#342](https://github.com/GameNative/gamenative-compat/issues/342) |
| 253 | [ ] | Mirror's Edge™ Catalyst (STEAM) | 20 | 21 | 95% (90d) | Does not open (67%) | 50% | [#454](https://github.com/GameNative/gamenative-compat/issues/454) |
| 254 | [ ] | Downfall - A Slay the Spire Fan Expansion (STEAM) | 20 | 20 | 100% (90d) | Does not open (68%) | n/a | [#320](https://github.com/GameNative/gamenative-compat/issues/320) |
| 255 | [ ] | Return to Castle Wolfenstein (STEAM) | 20 | 20 | 100% (90d) | Does not open (94%) | n/a | [#321](https://github.com/GameNative/gamenative-compat/issues/321) |
| 256 | [ ] | Fogpiercer (STEAM) | 19 | 26 | 73% (90d) | Does not open (79%) | n/a | [#303](https://github.com/GameNative/gamenative-compat/issues/303) |
| 257 | [ ] | Transformers: Fall of Cybertron (STEAM) | 19 | 26 | 73% (90d) | Does not open (76%) | n/a | [#304](https://github.com/GameNative/gamenative-compat/issues/304) |
| 258 | [ ] | Surviving Mars (STEAM) | 19 | 25 | 76% (90d) | Does not open (92%) | n/a | [#372](https://github.com/GameNative/gamenative-compat/issues/372) |
| 259 | [ ] | Realm of the Mad God Exalt (STEAM) | 19 | 24 | 79% (90d) | Does not open (93%) | n/a | [#359](https://github.com/GameNative/gamenative-compat/issues/359) |
| 260 | [ ] | Rune Factory 5 (STEAM) | 19 | 24 | 79% (90d) | Does not open (84%) | n/a | [#358](https://github.com/GameNative/gamenative-compat/issues/358) |
| 261 | [ ] | Definitely Not Fried Chicken (EPIC) | 19 | 23 | 83% (90d) | Does not open (68%) | n/a | [#356](https://github.com/GameNative/gamenative-compat/issues/356) |
| 262 | [ ] | Genshin Impact (EPIC) | 19 | 23 | 83% (90d) | Does not open (86%) | n/a | [#326](https://github.com/GameNative/gamenative-compat/issues/326) |
| 263 | [ ] | Jotunnslayer: Hordes of Hel (STEAM) | 19 | 22 | 86% (90d) | Does not open (67%) | n/a | [#382](https://github.com/GameNative/gamenative-compat/issues/382) |
| 264 | [ ] | ZONE OF THE ENDERS THE 2nd RUNNER : MARS / ANUBIS ZONE OF THE ENDERS : MARS (STEAM) | 19 | 22 | 86% (90d) | Does not open (79%) | n/a | [#386](https://github.com/GameNative/gamenative-compat/issues/386) |
| 265 | [ ] | Gothic 1 Remake (STEAM) | 19 | 21 | 90% (90d) | Directx error (44%) | n/a | [#336](https://github.com/GameNative/gamenative-compat/issues/336) |
| 266 | [ ] | Odallus: The Dark Call (STEAM) | 19 | 21 | 90% (90d) | No graphics (68%) | n/a | [#337](https://github.com/GameNative/gamenative-compat/issues/337) |
| 267 | [ ] | STALZONE (STEAM) | 19 | 21 | 90% (90d) | Does not open (100%) | n/a | [#338](https://github.com/GameNative/gamenative-compat/issues/338) |
| 268 | [ ] | Call of Duty 2 (STEAM) | 19 | 20 | 95% (90d) | Does not open (80%) | n/a | [#340](https://github.com/GameNative/gamenative-compat/issues/340) |
| 269 | [ ] | Deus Ex: Invisible War (STEAM) | 19 | 20 | 95% (90d) | Does not open (80%) | n/a | [#341](https://github.com/GameNative/gamenative-compat/issues/341) |
| 270 | [ ] | FINAL FANTASY XVI (STEAM) | 19 | 20 | 95% (90d) | Does not open (94%) | n/a | [#363](https://github.com/GameNative/gamenative-compat/issues/363) |
| 271 | [ ] | GT Legends (STEAM) | 19 | 20 | 95% (90d) | Does not open (89%) | n/a | [#364](https://github.com/GameNative/gamenative-compat/issues/364) |
| 272 | [ ] | Tom Clancy's Splinter Cell Blacklist (STEAM) | 19 | 20 | 95% (90d) | Does not open (87%) | n/a | [#367](https://github.com/GameNative/gamenative-compat/issues/367) |
| 273 | [ ] | Carnal Instinct (STEAM) | 18 | 25 | 72% (90d) | Does not open (63%) | n/a | [#440](https://github.com/GameNative/gamenative-compat/issues/440) |
| 274 | [ ] | Devil May Cry 4 Special Edition (GOG) | 18 | 25 | 72% (90d) | Does not open (67%) | n/a | [#391](https://github.com/GameNative/gamenative-compat/issues/391) |
| 275 | [ ] | Grim Fandango Remastered (GOG) | 18 | 24 | 75% (90d) | No graphics (70%) | n/a | [#375](https://github.com/GameNative/gamenative-compat/issues/375) |
| 276 | [ ] | Spark the Electric Jester (STEAM) | 18 | 24 | 75% (90d) | Does not open (63%) | 57% | [#377](https://github.com/GameNative/gamenative-compat/issues/377) |
| 277 | [ ] | We Were Here Together (EPIC) | 18 | 24 | 75% (90d) | Does not open (82%) | n/a | [#374](https://github.com/GameNative/gamenative-compat/issues/374) |
| 278 | [ ] | Portal: First Slice (STEAM) | 18 | 23 | 78% (90d) | Does not open (92%) | n/a | [#354](https://github.com/GameNative/gamenative-compat/issues/354) |
| 279 | [ ] | Tyr (STEAM) | 18 | 23 | 78% (90d) | Does not open (36%) | n/a | [#396](https://github.com/GameNative/gamenative-compat/issues/396) |
| 280 | [ ] | Yakuza 0 (GOG) | 18 | 23 | 78% (90d) | Does not open (67%) | n/a | [#378](https://github.com/GameNative/gamenative-compat/issues/378) |
| 281 | [ ] | Bejeweled 2 Deluxe (STEAM) | 18 | 22 | 82% (90d) | Does not open (93%) | n/a | [#329](https://github.com/GameNative/gamenative-compat/issues/329) |
| 282 | [ ] | The Last Stand: Aftermath (STEAM) | 18 | 22 | 82% (90d) | No graphics (50%) | n/a | [#324](https://github.com/GameNative/gamenative-compat/issues/324) |
| 283 | [ ] | Touhou Koumakyou: Classic - the Embodiment of Scarlet Devil (STEAM) | 18 | 22 | 82% (90d) | Does not open (100%) | n/a | [#464](https://github.com/GameNative/gamenative-compat/issues/464) |
| 284 | [ ] | Apotheon (STEAM) | 18 | 21 | 86% (90d) | Does not open (73%) | 42% | [#309](https://github.com/GameNative/gamenative-compat/issues/309) |
| 285 | [ ] | Crusader Kings III (STEAM) | 18 | 21 | 86% (90d) | No graphics (64%) | n/a | [#397](https://github.com/GameNative/gamenative-compat/issues/397) |
| 286 | [ ] | Dorfromantik (GOG) | 18 | 21 | 86% (90d) | Does not open (94%) | n/a | [#381](https://github.com/GameNative/gamenative-compat/issues/381) |
| 287 | [ ] | Just Cause 4 (EPIC) | 18 | 21 | 86% (90d) | Does not open (78%) | n/a | [#383](https://github.com/GameNative/gamenative-compat/issues/383) |
| 288 | [ ] | Mafia II: Definitive Edition (GOG) | 18 | 21 | 86% (90d) | No graphics (56%) | 27% | [#455](https://github.com/GameNative/gamenative-compat/issues/455) |
| 289 | [ ] | NBA 2K26 (STEAM) | 18 | 21 | 86% (90d) | Does not open (83%) | n/a | [#384](https://github.com/GameNative/gamenative-compat/issues/384) |
| 290 | [ ] | Sacred Gold (STEAM) | 18 | 21 | 86% (90d) | Does not open (93%) | n/a | [#334](https://github.com/GameNative/gamenative-compat/issues/334) |
| 291 | [ ] | Clive Barker's Undying (GOG) | 18 | 20 | 90% (90d) | Does not open (67%) | n/a | [#388](https://github.com/GameNative/gamenative-compat/issues/388) |
| 292 | [ ] | Assassin's Creed Odyssey (STEAM) | 17 | 24 | 71% (90d) | Does not open (75%) | n/a | [#390](https://github.com/GameNative/gamenative-compat/issues/390) |
| 293 | [ ] | Darksiders Warmastered Edition (EPIC) | 17 | 23 | 74% (90d) | Does not open (83%) | 36% | [#415](https://github.com/GameNative/gamenative-compat/issues/415) |
| 294 | [ ] | SlashZero Demo (STEAM) | 17 | 22 | 77% (90d) | Does not open (75%) | n/a | [#408](https://github.com/GameNative/gamenative-compat/issues/408) |
| 295 | [ ] | Grand Theft Auto: San Andreas - The Definitive Edition (STEAM) | 17 | 21 | 81% (90d) | Does not open (67%) | 27% | [#357](https://github.com/GameNative/gamenative-compat/issues/357) |
| 296 | [ ] | Resident Evil Requiem - Demo (STEAM) | 17 | 21 | 81% (90d) | No graphics (89%) | n/a | [#379](https://github.com/GameNative/gamenative-compat/issues/379) |
| 297 | [ ] | shapez (STEAM) | 17 | 21 | 81% (90d) | Does not open (62%) | n/a | [#332](https://github.com/GameNative/gamenative-compat/issues/332) |
| 298 | [ ] | Bright Memory (STEAM) | 17 | 20 | 85% (90d) | No graphics (82%) | n/a | [#380](https://github.com/GameNative/gamenative-compat/issues/380) |
| 299 | [ ] | The Escapists (EPIC) | 17 | 20 | 85% (90d) | Does not open (46%) | n/a | [#398](https://github.com/GameNative/gamenative-compat/issues/398) |
| 300 | [ ] | Tyrian 2000 (GOG) | 17 | 20 | 85% (90d) | Does not open (87%) | n/a | [#360](https://github.com/GameNative/gamenative-compat/issues/360) |
| 301 | [ ] | G-MODEアーカイブス+ ペルソナ3 アイギス THE FIRST MISSION (STEAM) | 16 | 23 | 70% (90d) | No graphics (56%) | n/a | [#400](https://github.com/GameNative/gamenative-compat/issues/400) |
| 302 | [ ] | Fallout Classic (GOG) | 16 | 22 | 73% (90d) | Does not open (63%) | n/a | [#392](https://github.com/GameNative/gamenative-compat/issues/392) |
| 303 | [ ] | Hitman 3: Contracts (GOG) | 16 | 22 | 73% (90d) | Does not open (93%) | n/a | [#401](https://github.com/GameNative/gamenative-compat/issues/401) |
| 304 | [ ] | Re-Volt (STEAM) | 16 | 22 | 73% (90d) | Controller issues (71%) | n/a | [#447](https://github.com/GameNative/gamenative-compat/issues/447) |
| 305 | [ ] | Life is Strange: Before the Storm Remastered (STEAM) | 16 | 21 | 76% (90d) | No graphics (67%) | n/a | [#402](https://github.com/GameNative/gamenative-compat/issues/402) |
| 306 | [ ] | The Elder Scrolls II: Daggerfall (STEAM) | 16 | 21 | 76% (90d) | Does not open (86%) | n/a | [#355](https://github.com/GameNative/gamenative-compat/issues/355) |
| 307 | [ ] | EVE Online (STEAM) | 16 | 20 | 80% (90d) | No graphics (57%) | n/a | [#407](https://github.com/GameNative/gamenative-compat/issues/407) |
| 308 | [ ] | Make Way (EPIC) | 16 | 20 | 80% (90d) | Does not open (73%) | n/a | [#441](https://github.com/GameNative/gamenative-compat/issues/441) |
| 309 | [ ] | Once Human (STEAM) | 16 | 20 | 80% (90d) | Does not open (63%) | n/a | [#395](https://github.com/GameNative/gamenative-compat/issues/395) |
| 310 | [ ] | Prey (GOG) | 16 | 20 | 80% (90d) | Does not open (38%) | n/a | [#461](https://github.com/GameNative/gamenative-compat/issues/461) |
| 311 | [ ] | Hob (STEAM) | 15 | 21 | 71% (90d) | Does not open (64%) | 50% | [#416](https://github.com/GameNative/gamenative-compat/issues/416) |
| 312 | [ ] | DayZ (STEAM) | 14 | 20 | 70% (90d) | Does not open (50%) | n/a | [#462](https://github.com/GameNative/gamenative-compat/issues/462) |
| 313 | [ ] | Jurassic World Evolution 2 (STEAM) | 14 | 20 | 70% (90d) | Directx error (50%) | n/a | [#448](https://github.com/GameNative/gamenative-compat/issues/448) |
| 314 | [ ] | The Long Drive (STEAM) | 14 | 20 | 70% (90d) | Does not open (58%) | n/a | [#404](https://github.com/GameNative/gamenative-compat/issues/404) |

## Probably does not work (109)

Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/431).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | The Witcher 3: Wild Hunt (STEAM) | 175 | 290 | 60% (90d) | Does not open (77%) | n/a |  |
| 2 | [ ] | Plants vs. Zombies: Game of the Year (STEAM) | 148 | 184 | 50% (14d) | Does not open (95%) | 42% | [#15](https://github.com/GameNative/gamenative-compat/issues/15) |
| 3 | [ ] | Metro 2033 Redux (STEAM) | 132 | 340 | 52% (1.3.0) | Does not open (66%) | 54% |  |
| 4 | [ ] | Euro Truck Simulator 2 (STEAM) | 123 | 215 | 63% (1.3.0) | Does not open (67%) | 57% | [#445](https://github.com/GameNative/gamenative-compat/issues/445) |
| 5 | [ ] | Geometry Dash (STEAM) | 105 | 395 | 62% (1.3.0) | Does not open (67%) | 41% | [#425](https://github.com/GameNative/gamenative-compat/issues/425) |
| 6 | [ ] | VRChat (STEAM) | 88 | 134 | 66% (90d) | Does not open (66%) | 41% |  |
| 7 | [ ] | Hollow Knight: Silksong (GOG) | 73 | 113 | 65% (90d) | Does not open (69%) | 50% |  |
| 8 | [ ] | Stardew Valley (GOG) | 65 | 113 | 58% (90d) | Controller issues (44%) | 50% |  |
| 9 | [ ] | Gorilla Tag (STEAM) | 63 | 105 | 60% (90d) | Does not open (77%) | 25% | [#442](https://github.com/GameNative/gamenative-compat/issues/442) |
| 10 | [ ] | Mini Motorways (STEAM) | 55 | 97 | 57% (90d) | Does not open (76%) | 57% | [#99](https://github.com/GameNative/gamenative-compat/issues/99) |
| 11 | [ ] | The Witcher 3: Wild Hunt - Complete Edition (GOG) | 53 | 92 | 58% (90d) | Does not open (62%) | 59% |  |
| 12 | [ ] | Oxygen Not Included (STEAM) | 52 | 86 | 60% (90d) | Does not open (69%) | 48% |  |
| 13 | [ ] | Breathedge (STEAM) | 50 | 74 | 68% (90d) | Does not open (63%) | 39% | [#112](https://github.com/GameNative/gamenative-compat/issues/112) |
| 14 | [ ] | Frostpunk (STEAM) | 48 | 75 | 64% (90d) | No graphics (78%) | 47% |  |
| 15 | [ ] | VALORANT (EPIC) | 46 | 73 | 63% (90d) | Does not open (77%) | 12% |  |
| 16 | [ ] | Skullgirls 2nd Encore (STEAM) | 45 | 78 | 58% (90d) | Does not open (93%) | 56% |  |
| 17 | [ ] | Tomb Raider I-III Remastered Starring Lara Croft (GOG) | 42 | 73 | 58% (90d) | Does not open (75%) | 49% |  |
| 18 | [ ] | Age of Empires II (2013) (STEAM) | 40 | 65 | 62% (90d) | Does not open (50%) | 58% |  |
| 19 | [ ] | Grim Dawn (GOG) | 39 | 65 | 60% (90d) | Does not open (63%) | 45% | [#147](https://github.com/GameNative/gamenative-compat/issues/147) |
| 20 | [ ] | DEATH STRANDING DIRECTOR'S CUT (STEAM) | 39 | 64 | 61% (90d) | Does not open (92%) | 44% | [#139](https://github.com/GameNative/gamenative-compat/issues/139) |
| 21 | [ ] | Sol Cesto (STEAM) | 36 | 55 | 65% (90d) | Does not open (70%) | 54% |  |
| 22 | [ ] | Battle Brothers (STEAM) | 36 | 54 | 67% (90d) | Does not open (78%) | 57% |  |
| 23 | [ ] | Journey (STEAM) | 34 | 68 | 50% (90d) | Does not open (68%) | 51% |  |
| 24 | [ ] | XCOM 2 (STEAM) | 34 | 52 | 65% (90d) | Does not open (61%) | n/a |  |
| 25 | [ ] | Deponia (STEAM) | 32 | 62 | 52% (90d) | Does not open (48%) | 59% |  |
| 26 | [ ] | Max Payne 2: The Fall of Max Payne (STEAM) | 29 | 52 | 56% (90d) | Does not open (55%) | 59% |  |
| 27 | [ ] | Crazy Taxi (STEAM) | 28 | 42 | 67% (90d) | Does not open (68%) | 40% | [#234](https://github.com/GameNative/gamenative-compat/issues/234) |
| 28 | [ ] | Strider (STEAM) | 28 | 42 | 67% (90d) | Does not open (100%) | 36% | [#126](https://github.com/GameNative/gamenative-compat/issues/126) |
| 29 | [ ] | Soul's Remnant (STEAM) | 27 | 49 | 55% (90d) | Does not open (55%) | n/a |  |
| 30 | [ ] | Lucid Blocks (STEAM) | 27 | 46 | 59% (90d) | Does not open (83%) | n/a |  |
| 31 | [ ] | Yume Nikki (STEAM) | 26 | 44 | 59% (90d) | Does not open (92%) | 0% |  |
| 32 | [ ] | Goat Simulator (STEAM) | 24 | 42 | 57% (90d) | Does not open (58%) | 53% |  |
| 33 | [ ] | Mafia: Definitive Edition (STEAM) | 23 | 42 | 55% (90d) | Does not open (81%) | n/a |  |
| 34 | [ ] | Opus Magnum (STEAM) | 23 | 37 | 62% (90d) | Does not open (81%) | n/a |  |
| 35 | [ ] | PUBG: BATTLEGROUNDS (STEAM) | 23 | 34 | 68% (90d) | Does not open (81%) | n/a |  |
| 36 | [ ] | Owlboy (STEAM) | 22 | 41 | 54% (90d) | Does not open (81%) | 50% |  |
| 37 | [ ] | Ghost of Tsushima DIRECTOR'S CUT (STEAM) | 22 | 40 | 55% (90d) | No graphics (62%) | 40% |  |
| 38 | [ ] | Invisible, Inc. (STEAM) | 22 | 39 | 56% (90d) | Does not open (70%) | 54% |  |
| 39 | [ ] | My Summer Car (STEAM) | 20 | 37 | 54% (90d) | Does not open (53%) | n/a |  |
| 40 | [ ] | Paper Lily - Chapter 1 (STEAM) | 20 | 36 | 56% (90d) | Does not open (72%) | n/a |  |
| 41 | [ ] | Breath of Fire IV (GOG) | 20 | 35 | 57% (90d) | Does not open (74%) | 58% |  |
| 42 | [ ] | GOD EATER RESURRECTION (STEAM) | 20 | 31 | 65% (90d) | Does not open (50%) | 58% |  |
| 43 | [ ] | Another World: 20th Anniversary Edition (GOG) | 20 | 30 | 67% (90d) | Does not open (71%) | n/a |  |
| 44 | [ ] | Agatha Knife (AMAZON) | 20 | 29 | 69% (90d) | Graphics glitches (65%) | n/a | [#290](https://github.com/GameNative/gamenative-compat/issues/290) |
| 45 | [ ] | No More Heroes (STEAM) | 19 | 36 | 53% (90d) | No graphics (67%) | n/a |  |
| 46 | [ ] | SCP – Containment Breach (STEAM) | 18 | 35 | 51% (90d) | Does not open (83%) | n/a |  |
| 47 | [ ] | Lost Castle 2 (STEAM) | 18 | 34 | 53% (90d) | Does not open (64%) | n/a |  |
| 48 | [ ] | Alabaster Dawn Demo (STEAM) | 18 | 27 | 67% (90d) | Controller issues (72%) | n/a |  |
| 49 | [ ] | Turnip Boy Robs a Bank (EPIC) | 18 | 27 | 67% (90d) | Does not open (69%) | 27% | [#222](https://github.com/GameNative/gamenative-compat/issues/222) |
| 50 | [ ] | Legend of Grimrock 2 (STEAM) | 18 | 26 | 69% (90d) | Does not open (80%) | n/a | [#352](https://github.com/GameNative/gamenative-compat/issues/352) |
| 51 | [ ] | Resident Evil 3: Raccoon City Demo  (STEAM) | 17 | 34 | 50% (90d) | Does not open (88%) | n/a |  |
| 52 | [ ] | Shank 2 (STEAM) | 17 | 30 | 57% (90d) | Does not open (82%) | n/a |  |
| 53 | [ ] | Wildermyth (STEAM) | 17 | 29 | 59% (90d) | Does not open (50%) | n/a |  |
| 54 | [ ] | Guacamelee! Gold Edition (STEAM) | 17 | 28 | 61% (90d) | Does not open (93%) | n/a | [#322](https://github.com/GameNative/gamenative-compat/issues/322) |
| 55 | [ ] | Race The Sun (STEAM) | 17 | 28 | 61% (90d) | No graphics (92%) | n/a |  |
| 56 | [ ] | War of Dots (STEAM) | 17 | 27 | 63% (90d) | Does not open (69%) | n/a | [#274](https://github.com/GameNative/gamenative-compat/issues/274) |
| 57 | [ ] | Shiren the Wanderer: The Tower of Fortune and the Dice of Fate (STEAM) | 17 | 25 | 68% (90d) | Does not open (80%) | n/a |  |
| 58 | [ ] | Blaster Master Zero (STEAM) | 16 | 29 | 55% (90d) | Does not open (63%) | n/a |  |
| 59 | [ ] | Baldur's Gate II: Enhanced Edition (STEAM) | 16 | 27 | 59% (90d) | Does not open (80%) | n/a |  |
| 60 | [ ] | Aperture Desk Job (STEAM) | 15 | 30 | 50% (90d) | Does not open (62%) | n/a |  |
| 61 | [ ] | Evoland (STEAM) | 15 | 29 | 52% (90d) | Controller issues (71%) | n/a |  |
| 62 | [ ] | Mark of the Ninja (STEAM) | 15 | 29 | 52% (90d) | Does not open (75%) | n/a |  |
| 63 | [ ] | Spilled! (STEAM) | 15 | 25 | 60% (90d) | Graphics glitches (67%) | n/a |  |
| 64 | [ ] | Human Resource Machine (EPIC) | 15 | 23 | 65% (90d) | No graphics (67%) | n/a |  |
| 65 | [ ] | Chef Knight (STEAM) | 15 | 22 | 68% (90d) | Does not open (93%) | n/a |  |
| 66 | [ ] | BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien (STEAM) | 14 | 28 | 50% (90d) | Does not open (100%) | n/a |  |
| 67 | [ ] | NiGHTS into Dreams... (STEAM) | 14 | 27 | 52% (90d) | Does not open (45%) | n/a |  |
| 68 | [ ] | Ys VI: The Ark of Napishtim (STEAM) | 14 | 26 | 54% (90d) | Controller issues (54%) | n/a |  |
| 69 | [ ] | Alan Wake's American Nightmare (EPIC) | 14 | 25 | 56% (90d) | Does not open (92%) | 40% |  |
| 70 | [ ] | Call of Duty: Black Ops II - Multiplayer (STEAM) | 14 | 24 | 58% (90d) | Does not open (93%) | 23% |  |
| 71 | [ ] | Katana ZERO (GOG) | 14 | 24 | 58% (90d) | Does not open (85%) | 30% |  |
| 72 | [ ] | Warhammer 40,000: Boltgun (GOG) | 14 | 23 | 61% (90d) | Does not open (92%) | 50% |  |
| 73 | [ ] | Space Rangers HD: A War Apart (STEAM) | 14 | 22 | 64% (90d) | Does not open (69%) | 50% |  |
| 74 | [ ] | Tom Clancy's Splinter Cell (STEAM) | 14 | 21 | 67% (90d) | Does not open (67%) | n/a | [#417](https://github.com/GameNative/gamenative-compat/issues/417) |
| 75 | [ ] | Quake III Arena (STEAM) | 13 | 26 | 50% (90d) | Does not open (70%) | n/a |  |
| 76 | [ ] | Shantae: Half-Genie Hero Ultimate Edition (STEAM) | 13 | 26 | 50% (90d) | Does not open (54%) | 57% |  |
| 77 | [ ] | Pillars of Eternity (STEAM) | 13 | 25 | 52% (90d) | Does not open (43%) | n/a |  |
| 78 | [ ] | UNDEFEATED (STEAM) | 13 | 25 | 52% (90d) | Does not open (80%) | n/a |  |
| 79 | [ ] | A Plague Tale: Innocence (GOG) | 13 | 24 | 54% (90d) | Does not open (92%) | n/a |  |
| 80 | [ ] | Secret of Mana (STEAM) | 13 | 24 | 54% (90d) | Graphics glitches (58%) | n/a |  |
| 81 | [ ] | DYNASTY WARRIORS: ORIGINS (STEAM) | 13 | 23 | 57% (90d) | Does not open (62%) | n/a |  |
| 82 | [ ] | Poly Bridge (STEAM) | 13 | 23 | 57% (90d) | Does not open (54%) | n/a |  |
| 83 | [ ] | Lara Croft and the Temple of Osiris (STEAM) | 13 | 22 | 59% (90d) | Does not open (50%) | n/a |  |
| 84 | [ ] | Strikers Club (STEAM) | 13 | 22 | 59% (90d) | Does not open (83%) | n/a |  |
| 85 | [ ] | Blood Omen: Legacy of Kain (GOG) | 13 | 21 | 62% (90d) | Does not open (75%) | 46% |  |
| 86 | [ ] | Evenicle (STEAM) | 13 | 21 | 62% (90d) | Graphics glitches (77%) | n/a |  |
| 87 | [ ] | PAYDAY: The Heist (STEAM) | 13 | 21 | 62% (90d) | Does not open (67%) | n/a |  |
| 88 | [ ] | Trials Survivors (STEAM) | 13 | 21 | 62% (90d) | Does not open (67%) | n/a |  |
| 89 | [ ] | XIII (GOG) | 13 | 21 | 62% (90d) | Does not open (70%) | n/a |  |
| 90 | [ ] | (the) Gnorp Apologue (STEAM) | 13 | 20 | 65% (90d) | Does not open (67%) | n/a |  |
| 91 | [ ] | Look Outside (GOG) | 12 | 24 | 50% (90d) | Does not open (100%) | n/a |  |
| 92 | [ ] | Grounded (STEAM) | 12 | 23 | 52% (90d) | No graphics (44%) | n/a |  |
| 93 | [ ] | Lust Goddess (STEAM) | 12 | 22 | 55% (90d) | Does not open (100%) | n/a |  |
| 94 | [ ] | Mina the Hollower (GOG) | 12 | 22 | 55% (90d) | Does not open (42%) | 58% |  |
| 95 | [ ] | Revolution Idle (STEAM) | 12 | 22 | 55% (90d) | No graphics (50%) | n/a |  |
| 96 | [ ] | Shift At Midnight (STEAM) | 12 | 22 | 55% (90d) | Does not open (80%) | n/a |  |
| 97 | [ ] | The Stanley Parable (STEAM) | 12 | 22 | 55% (90d) | Does not open (88%) | 50% |  |
| 98 | [ ] | The Excavation of Hob's Barrow (STEAM) | 12 | 21 | 57% (90d) | Controller issues (82%) | n/a |  |
| 99 | [ ] | The Lord of the Rings: War in the North™ - Legacy Edition (STEAM) | 12 | 21 | 57% (90d) | Controller issues (60%) | n/a |  |
| 100 | [ ] | Ys: Memories of Celceta (STEAM) | 12 | 21 | 57% (90d) | No graphics (50%) | n/a |  |
| 101 | [ ] | Commander Keen Complete Pack (STEAM) | 12 | 20 | 60% (90d) | Does not open (73%) | n/a |  |
| 102 | [ ] | Dex (GOG) | 12 | 20 | 60% (90d) | Does not open (80%) | n/a |  |
| 103 | [ ] | Drop Duchy (EPIC) | 12 | 20 | 60% (90d) | Does not open (100%) | n/a |  |
| 104 | [ ] | Crying Suns (EPIC) | 11 | 22 | 50% (90d) | No graphics (57%) | n/a |  |
| 105 | [ ] | Pathologic Classic HD (STEAM) | 11 | 21 | 52% (90d) | No graphics (78%) | n/a |  |
| 106 | [ ] | FATE (STEAM) | 10 | 20 | 50% (90d) | No graphics (43%) | n/a |  |
| 107 | [ ] | Far Cry® (GOG) | 10 | 20 | 50% (90d) | Graphics glitches (40%) | n/a |  |
| 108 | [ ] | Gloomwood (STEAM) | 10 | 20 | 50% (90d) | Does not open (56%) | n/a |  |
| 109 | [ ] | Thief™ 3: Deadly Shadows (GOG) | 10 | 20 | 50% (90d) | Does not open (70%) | n/a |  |

## Works, but the first launch usually fails (341)

Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change. Tick games off in the [checklist](https://github.com/GameNative/gamenative-compat/issues/432).

| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |
|---:|---|---|---:|---:|---:|---|---:|---|
| 1 | [ ] | Slay the Spire (STEAM) | 1434 | 1820 | 74% (1.3.0) | Does not open (83%) | 78% |  |
| 2 | [ ] | Grim Dawn (STEAM) | 640 | 690 | 67% (1.3.0) | Does not open (77%) | 66% |  |
| 3 | [ ] | Sleeping Dogs: Definitive Edition (STEAM) | 583 | 743 | 76% (1.3.0) | Does not open (66%) | 93% |  |
| 4 | [ ] | Terraria (STEAM) | 502 | 793 | 55% (1.3.0) | No graphics (51%) | 76% |  |
| 5 | [ ] | KINGDOM HEARTS -HD 1.5+2.5 ReMIX- (STEAM) | 444 | 907 | 55% (1.3.0) | Does not open (80%) | 93% |  |
| 6 | [ ] | The Elder Scrolls V: Skyrim (STEAM) | 360 | 540 | 67% (1.3.0) | Does not open (56%) | 89% |  |
| 7 | [ ] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 282 | 321 | 88% (90d) | Does not open (88%) | 60% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 8 | [ ] | Cyberpunk 2077 (STEAM) | 238 | 392 | 63% (1.3.0) | Does not open (68%) | 74% |  |
| 9 | [ ] | BeamNG.drive (STEAM) | 232 | 285 | 86% (1.3.0) | Does not open (84%) | 92% |  |
| 10 | [ ] | Palworld (STEAM) | 231 | 469 | 56% (14d) | Does not open (71%) | 88% |  |
| 11 | [ ] | Welcome to Elderfield (STEAM) | 221 | 263 | 54% (14d) | Does not open (72%) | 81% |  |
| 12 | [ ] | METAL GEAR SOLID: Peace Walker - Master Collection Version (STEAM) | 219 | 310 | 71% (90d) | Does not open (61%) | 89% |  |
| 13 | [ ] | OMORI (STEAM) | 213 | 258 | 62% (14d) | Does not open (64%) | 74% |  |
| 14 | [ ] | Devil May Cry HD Collection (STEAM) | 197 | 274 | 88% (1.3.0) | Does not open (88%) | 70% |  |
| 15 | [ ] | ELDEN RING (STEAM) | 191 | 288 | 73% (1.3.0) | Does not open (87%) | 67% |  |
| 16 | [ ] | MONSTER HUNTER RISE (STEAM) | 188 | 476 | 52% (1.3.0) | Does not open (78%) | 76% |  |
| 17 | [ ] | Fallout 3 - Game of the Year Edition (STEAM) | 187 | 350 | 64% (1.3.0) | Does not open (60%) | 81% |  |
| 18 | [ ] | DREDGE (EPIC) | 182 | 234 | 57% (1.3.0) | Does not open (68%) | 88% |  |
| 19 | [ ] | Mirror's Edge (STEAM) | 158 | 205 | 77% (90d) | Does not open (90%) | 76% |  |
| 20 | [ ] | Noita (STEAM) | 150 | 222 | 53% (1.3.0) | Does not open (54%) | 84% |  |
| 21 | [ ] | Far Cry® 3 (STEAM) | 146 | 165 | 88% (90d) | Does not open (83%) | 64% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 22 | [ ] | Grand Theft Auto V Enhanced (STEAM) | 143 | 164 | 85% (14d) | Does not open (85%) | 79% |  |
| 23 | [ ] | Team Fortress 2 (STEAM) | 137 | 227 | 68% (1.3.0) | Does not open (71%) | 79% |  |
| 24 | [ ] | Fallout: New Vegas Ultimate Edition (GOG) | 135 | 279 | 50% (1.3.0) | Does not open (54%) | 76% |  |
| 25 | [ ] | Cave Story+ (STEAM) | 131 | 144 | 91% (90d) | Does not open (65%) | 93% |  |
| 26 | [ ] | Borderlands 2 (EPIC) | 127 | 148 | 82% (1.3.0) | Does not open (89%) | 63% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 27 | [ ] | Schedule I (STEAM) | 123 | 203 | 50% (14d) | Does not open (71%) | 90% |  |
| 28 | [ ] | Fallout: New Vegas (EPIC) | 122 | 146 | 84% (90d) | Does not open (58%) | 88% |  |
| 29 | [ ] | Minecraft Dungeons II (STEAM) | 122 | 139 | 88% (90d) | Does not open (83%) | 65% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 30 | [ ] | Castlevania Advance Collection (STEAM) | 121 | 189 | 65% (1.3.0) | Controller issues (94%) | 97% |  |
| 31 | [ ] | The Witcher: Enhanced Edition (STEAM) | 121 | 138 | 88% (90d) | Does not open (58%) | 60% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 32 | [ ] | Castlevania Dominus Collection (STEAM) | 120 | 176 | 77% (1.3.0) | Controller issues (94%) | 97% |  |
| 33 | [ ] | Devil May Cry 5 (STEAM) | 119 | 191 | 52% (1.3.0) | Does not open (81%) | 64% |  |
| 34 | [ ] | Mega Man Battle Network Legacy Collection Vol. 1 (STEAM) | 118 | 155 | 76% (90d) | Does not open (86%) | 81% |  |
| 35 | [ ] | Touhou Koumakyou: New Classic - the Embodiment of Scarlet Devil (STEAM) | 115 | 173 | 66% (90d) | Does not open (78%) | 83% |  |
| 36 | [ ] | Moonstone Island (STEAM) | 113 | 147 | 77% (90d) | Controller issues (55%) | 89% |  |
| 37 | [ ] | FINAL FANTASY VIII - REMASTERED (STEAM) | 101 | 158 | 64% (90d) | Does not open (87%) | 60% |  |
| 38 | [ ] | Rise of the Tomb Raider (STEAM) | 99 | 154 | 64% (90d) | Does not open (78%) | 96% |  |
| 39 | [ ] | Aniimo (STEAM) | 99 | 136 | 73% (90d) | Does not open (77%) | 94% |  |
| 40 | [ ] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 97 | 139 | 77% (1.3.0) | Does not open (70%) | 68% |  |
| 41 | [ ] | DOOM (STEAM) | 95 | 163 | 58% (90d) | Does not open (71%) | 90% |  |
| 42 | [ ] | Vital Shell (STEAM) | 95 | 138 | 64% (14d) | Does not open (54%) | 85% |  |
| 43 | [ ] | METAL GEAR SOLID - Master Collection Version (STEAM) | 95 | 129 | 74% (90d) | Controller issues (86%) | 100% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 44 | [ ] | Cry of Fear (STEAM) | 94 | 180 | 65% (14d) | Does not open (57%) | 90% |  |
| 45 | [ ] | Dying Light (STEAM) | 94 | 180 | 52% (90d) | Does not open (88%) | 91% |  |
| 46 | [ ] | STEINS;GATE (STEAM) | 93 | 126 | 74% (90d) | Does not open (92%) | 85% |  |
| 47 | [ ] | Fallout: New Vegas PCR (STEAM) | 92 | 131 | 70% (90d) | Does not open (92%) | 83% |  |
| 48 | [ ] | Happy Wheels (STEAM) | 92 | 112 | 82% (90d) | No graphics (54%) | 78% |  |
| 49 | [ ] | BioShock Remastered (EPIC) | 90 | 165 | 55% (90d) | Does not open (51%) | 85% |  |
| 50 | [ ] | Sovereign Tower (STEAM) | 90 | 142 | 63% (90d) | Does not open (82%) | 92% |  |
| 51 | [ ] | The Sims™ 4 (STEAM) | 85 | 106 | 80% (90d) | Does not open (88%) | 67% |  |
| 52 | [ ] | Resident Evil 4 (2005) (STEAM) | 82 | 162 | 51% (90d) | Does not open (75%) | 74% |  |
| 53 | [ ] | Alabaster Dawn (STEAM) | 80 | 135 | 59% (90d) | Controller issues (51%) | 93% |  |
| 54 | [ ] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 79 | 103 | 77% (90d) | Does not open (52%) | 70% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 55 | [ ] | Call of Juarez Gunslinger (STEAM) | 78 | 92 | 85% (90d) | Does not open (89%) | 62% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 56 | [ ] | Detroit: Become Human (STEAM) | 78 | 80 | 98% (90d) | Does not open (72%) | 68% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 57 | [ ] | Mega Man Zero/ZX Legacy Collection (STEAM) | 77 | 103 | 75% (90d) | Does not open (87%) | 91% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 58 | [ ] | Sid Meier's Civilization VI (STEAM) | 76 | 132 | 52% (1.3.0) | Does not open (68%) | 91% |  |
| 59 | [ ] | Gunfire Reborn (STEAM) | 76 | 84 | 90% (90d) | Does not open (84%) | 91% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 60 | [ ] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 74 | 123 | 60% (90d) | Controller issues (60%) | 93% |  |
| 61 | [ ] | Firewatch (STEAM) | 74 | 121 | 61% (90d) | Does not open (92%) | 62% |  |
| 62 | [ ] | POSTAL 2 (STEAM) | 74 | 120 | 62% (90d) | Does not open (67%) | 67% |  |
| 63 | [ ] | Need for Speed: Hot Pursuit (STEAM) | 73 | 100 | 73% (90d) | Does not open (73%) | 75% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 64 | [ ] | Fable - The Lost Chapters (STEAM) | 72 | 111 | 52% (1.3.0) | Graphics glitches (47%) | 74% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 65 | [ ] | Fallout (STEAM) | 72 | 110 | 65% (90d) | Does not open (70%) | 76% |  |
| 66 | [ ] | Dota 2 (STEAM) | 71 | 104 | 77% (14d) | Does not open (76%) | 78% |  |
| 67 | [ ] | Hatsune Miku: Project DIVA Mega Mix+ (STEAM) | 70 | 175 | 54% (1.3.0) | Does not open (81%) | 79% |  |
| 68 | [ ] | Antivirus Survivors 2003 Professional (STEAM) | 69 | 99 | 70% (90d) | Does not open (62%) | 89% |  |
| 69 | [ ] | Disgaea 5 Complete (STEAM) | 69 | 83 | 86% (14d) | Does not open (80%) | 96% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 70 | [ ] | Fallout 3: Game of the Year Edition (GOG) | 68 | 166 | 50% (14d) | Does not open (60%) | 74% |  |
| 71 | [ ] | Spyro™ Reignited Trilogy (STEAM) | 68 | 107 | 64% (90d) | Does not open (71%) | 68% |  |
| 72 | [ ] | TBH: Task Bar Hero (STEAM) | 68 | 100 | 68% (90d) | Does not open (67%) | 100% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 73 | [ ] | Borderlands: The Pre-Sequel (STEAM) | 68 | 94 | 72% (90d) | Does not open (79%) | 62% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 74 | [ ] | Five Nights at Freddy's: Into the Pit (EPIC) | 67 | 92 | 73% (90d) | Does not open (55%) | 88% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 75 | [ ] | Dungeons & Degenerate Gamblers (STEAM) | 67 | 90 | 74% (90d) | Does not open (90%) | 98% |  |
| 76 | [ ] | Grand Theft Auto V Enhanced (EPIC) | 67 | 82 | 82% (90d) | Does not open (91%) | 98% |  |
| 77 | [ ] | MARVEL vs. CAPCOM Fighting Collection: Arcade Classics (STEAM) | 66 | 89 | 74% (90d) | Does not open (89%) | 80% |  |
| 78 | [ ] | The Binding of Isaac (STEAM) | 63 | 144 | 67% (1.3.0) | Controller issues (91%) | 94% |  |
| 79 | [ ] | Bloodstained: Ritual of the Night (EPIC) | 63 | 117 | 54% (90d) | Does not open (61%) | 64% |  |
| 80 | [ ] | Sonic Lost World (STEAM) | 63 | 102 | 62% (90d) | No graphics (58%) | 93% |  |
| 81 | [ ] | Sonic Adventure DX (STEAM) | 63 | 99 | 64% (90d) | Does not open (85%) | 70% |  |
| 82 | [ ] | Big Walk (STEAM) | 63 | 96 | 66% (90d) | Does not open (68%) | 86% |  |
| 83 | [ ] | Ace Attorney Investigations Collection (STEAM) | 63 | 95 | 66% (90d) | Does not open (97%) | 93% |  |
| 84 | [ ] | Sonic Generations (STEAM) | 63 | 73 | 86% (90d) | Does not open (71%) | 62% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 85 | [ ] | A Plague Tale: Innocence (STEAM) | 63 | 66 | 95% (90d) | Does not open (85%) | 68% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 86 | [ ] | Poppy Playtime (STEAM) | 62 | 111 | 56% (90d) | Does not open (69%) | 83% |  |
| 87 | [ ] | Red Dead Redemption 2 (STEAM) | 61 | 80 | 62% (1.3.0) | Does not open (98%) | 84% |  |
| 88 | [ ] | Borderlands 3 (STEAM) | 61 | 73 | 84% (90d) | Does not open (91%) | 100% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 89 | [ ] | American Truck Simulator (STEAM) | 60 | 99 | 73% (14d) | Does not open (76%) | 71% |  |
| 90 | [ ] | Cyberpunk 2077 (GOG) | 60 | 73 | 82% (90d) | Does not open (80%) | 71% |  |
| 91 | [ ] | eFootball™ (STEAM) | 59 | 93 | 63% (90d) | Does not open (56%) | 74% |  |
| 92 | [ ] | Dead by Daylight (STEAM) | 59 | 65 | 91% (90d) | Does not open (80%) | 77% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 93 | [ ] | The Secret of Monkey Island: Special Edition (STEAM) | 58 | 93 | 62% (90d) | Does not open (90%) | 77% |  |
| 94 | [ ] | The Bazaar (STEAM) | 58 | 92 | 63% (90d) | Does not open (74%) | 78% |  |
| 95 | [ ] | Starbound (STEAM) | 57 | 83 | 69% (90d) | Does not open (72%) | 73% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 96 | [ ] | Guildrun Demo (STEAM) | 57 | 81 | 70% (90d) | No graphics (65%) | 80% |  |
| 97 | [ ] | MIO: Memories in Orbit (STEAM) | 56 | 113 | 52% (14d) | Graphics glitches (48%) | 98% |  |
| 98 | [ ] | Prey (STEAM) | 56 | 91 | 62% (90d) | Does not open (67%) | 88% |  |
| 99 | [ ] | Until Then (STEAM) | 55 | 96 | 57% (90d) | Does not open (75%) | 96% |  |
| 100 | [ ] | Devil May Cry 4 Special Edition (STEAM) | 55 | 91 | 60% (90d) | Does not open (88%) | 81% |  |
| 101 | [ ] | Sheepy: A Short Adventure (STEAM) | 55 | 64 | 86% (90d) | Does not open (52%) | 73% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 102 | [ ] | MudRunner (STEAM) | 54 | 106 | 51% (90d) | Does not open (74%) | 60% |  |
| 103 | [ ] | A Plague Tale: Innocence (EPIC) | 54 | 92 | 59% (90d) | Does not open (71%) | 100% |  |
| 104 | [ ] | MY HERO ULTRA RUMBLE (STEAM) | 54 | 62 | 87% (90d) | Does not open (79%) | 83% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 105 | [ ] | Teardown (STEAM) | 53 | 94 | 56% (90d) | Controller issues (50%) | 76% |  |
| 106 | [ ] | Street Fighter™ 6 (STEAM) | 53 | 76 | 70% (90d) | Does not open (91%) | 80% |  |
| 107 | [ ] | Sable (EPIC) | 52 | 91 | 57% (90d) | No graphics (49%) | 74% |  |
| 108 | [ ] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 51 | 94 | 55% (14d) | Does not open (56%) | 60% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 109 | [ ] | Okami HD (STEAM) | 51 | 93 | 55% (90d) | Controller issues (60%) | 88% |  |
| 110 | [ ] | Slay the Princess — The Pristine Cut (STEAM) | 51 | 85 | 60% (90d) | No graphics (60%) | 71% |  |
| 111 | [ ] | Alex Kidd in Miracle World DX (EPIC) | 51 | 55 | 93% (90d) | Does not open (85%) | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 112 | [ ] | 7 Days to Die (STEAM) | 50 | 108 | 73% (14d) | Does not open (73%) | 76% |  |
| 113 | [ ] | Rivals of Aether II (STEAM) | 50 | 76 | 66% (90d) | Does not open (57%) | 68% |  |
| 114 | [ ] | FINAL FANTASY VII (2013) (STEAM) | 50 | 71 | 70% (90d) | Does not open (86%) | 80% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 115 | [ ] | Watch_Dogs 2 (STEAM) | 50 | 57 | 88% (90d) | Does not open (97%) | 65% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 116 | [ ] | Order of the Sinking Star (STEAM) | 49 | 69 | 66% (14d) | Does not open (67%) | 69% |  |
| 117 | [ ] | Tomb Raider: Anniversary (STEAM) | 48 | 64 | 75% (90d) | Does not open (96%) | 60% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 118 | [ ] | Dead Space (STEAM) | 48 | 61 | 79% (90d) | Does not open (51%) | 75% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 119 | [ ] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 77 | 61% (90d) | Controller issues (57%) | 97% |  |
| 120 | [ ] | STEINS;GATE RE:BOOT (STEAM) | 47 | 68 | 69% (90d) | Does not open (82%) | 81% |  |
| 121 | [ ] | Moonlighter (EPIC) | 47 | 51 | 92% (90d) | No graphics (76%) | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 122 | [ ] | Digimon World: Next Order (STEAM) | 46 | 87 | 53% (90d) | Controller issues (80%) | 97% |  |
| 123 | [ ] | Resident Evil 7 Biohazard (STEAM) | 46 | 74 | 81% (14d) | Does not open (82%) | 82% |  |
| 124 | [ ] | Plague Inc: Evolved (STEAM) | 46 | 73 | 63% (90d) | Does not open (63%) | 63% |  |
| 125 | [ ] | Grand Theft Auto V (EPIC) | 45 | 52 | 87% (90d) | Does not open (89%) | 83% |  |
| 126 | [ ] | MapleStory (STEAM) | 45 | 46 | 96% (14d) | Does not open (76%) | 77% |  |
| 127 | [ ] | Life is Strange™ (STEAM) | 44 | 84 | 52% (90d) | Does not open (75%) | 80% |  |
| 128 | [ ] | PROTOTYPE 2 (STEAM) | 44 | 84 | 52% (90d) | Does not open (74%) | 83% |  |
| 129 | [ ] | Salt and Sanctuary (STEAM) | 44 | 79 | 56% (90d) | Does not open (76%) | 83% |  |
| 130 | [ ] | Capcom Fighting Collection (STEAM) | 43 | 50 | 86% (90d) | Does not open (86%) | 79% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 131 | [ ] | LEGO® Batman™: Legacy of the Dark Knight (STEAM) | 42 | 68 | 62% (90d) | Does not open (65%) | 80% |  |
| 132 | [ ] | Forza Horizon 4 (STEAM) | 42 | 58 | 72% (90d) | Does not open (53%) | 88% |  |
| 133 | [ ] | MOUSE: P.I. For Hire (STEAM) | 41 | 136 | 57% (1.3.0) | Does not open (62%) | 88% |  |
| 134 | [ ] | Sonic Origins (STEAM) | 41 | 68 | 60% (90d) | Does not open (70%) | 82% |  |
| 135 | [ ] | Deadlock (STEAM) | 41 | 67 | 71% (14d) | Does not open (50%) | 96% |  |
| 136 | [ ] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 41 | 62 | 66% (90d) | Does not open (75%) | 66% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 137 | [ ] | Capcom Arcade Stadium (STEAM) | 41 | 51 | 80% (90d) | Does not open (81%) | 68% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 138 | [ ] | Amnesia: The Dark Descent (STEAM) | 40 | 74 | 54% (90d) | Does not open (84%) | 82% |  |
| 139 | [ ] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 40 | 73 | 55% (90d) | Controller issues (53%) | 84% |  |
| 140 | [ ] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 40 | 66 | 61% (90d) | Does not open (42%) | 67% |  |
| 141 | [ ] | Aggelos (STEAM) | 40 | 54 | 74% (90d) | No graphics (79%) | 92% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 142 | [ ] | Monster Hunter Wilds (STEAM) | 40 | 41 | 98% (90d) | Does not open (64%) | 71% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 143 | [ ] | Resident Evil 6 (STEAM) | 39 | 114 | 73% (1.3.0) | Does not open (56%) | 93% |  |
| 144 | [ ] | Rayman Origins (STEAM) | 39 | 85 | 60% (14d) | Does not open (72%) | 78% |  |
| 145 | [ ] | STAR WARS™: The Force Unleashed™ Ultimate Sith Edition (STEAM) | 39 | 75 | 52% (90d) | Controller issues (47%) | 87% |  |
| 146 | [ ] | Tales of ARISE (STEAM) | 39 | 66 | 59% (90d) | Controller issues (77%) | 93% |  |
| 147 | [ ] | DRAGON BALL XENOVERSE 2 (STEAM) | 38 | 74 | 51% (90d) | Does not open (100%) | 69% |  |
| 148 | [ ] | Abiotic Factor (STEAM) | 38 | 71 | 54% (90d) | Does not open (84%) | 70% |  |
| 149 | [ ] | Rocket League (STEAM) | 38 | 55 | 69% (90d) | Does not open (74%) | 72% |  |
| 150 | [ ] | SurrounDead (STEAM) | 37 | 67 | 55% (90d) | Controller issues (54%) | 94% |  |
| 151 | [ ] | CrossCode (GOG) | 37 | 41 | 90% (90d) | Does not open (76%) | 67% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 152 | [ ] | ASTLIBRA ～生きた証～ Revision (STEAM) | 36 | 70 | 51% (90d) | No graphics (84%) | 96% |  |
| 153 | [ ] | Combolands: Roguelike Citybuilder (STEAM) | 36 | 66 | 55% (90d) | Does not open (70%) | 88% |  |
| 154 | [ ] | Counter-Strike:Global Offensive (STEAM) | 36 | 53 | 68% (90d) | Does not open (80%) | 74% |  |
| 155 | [ ] | Last Epoch (STEAM) | 36 | 51 | 71% (90d) | Does not open (71%) | 100% |  |
| 156 | [ ] | Capcom Fighting Collection 2 (STEAM) | 36 | 50 | 72% (90d) | Does not open (80%) | 87% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 157 | [ ] | Romestead (STEAM) | 36 | 47 | 77% (90d) | Does not open (67%) | 83% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 158 | [ ] | SnowRunner (STEAM) | 36 | 45 | 80% (90d) | Does not open (96%) | 82% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 159 | [ ] | Lost Planet: Extreme Condition (STEAM) | 36 | 43 | 84% (90d) | Does not open (79%) | 62% | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 160 | [ ] | POSTAL 2 (GOG) | 35 | 70 | 50% (90d) | Graphics glitches (43%) | 100% |  |
| 161 | [ ] | Street Fighter 30th Anniversary Collection (STEAM) | 35 | 68 | 51% (90d) | Does not open (100%) | 65% |  |
| 162 | [ ] | Monster Hunter Stories (STEAM) | 35 | 66 | 53% (90d) | Does not open (89%) | 82% |  |
| 163 | [ ] | Gothic II: Gold Classic (STEAM) | 35 | 62 | 56% (90d) | Does not open (50%) | 80% |  |
| 164 | [ ] | Hearts of Iron IV (STEAM) | 35 | 57 | 61% (90d) | Does not open (73%) | 68% |  |
| 165 | [ ] | Earthion (STEAM) | 35 | 55 | 64% (90d) | Controller issues (88%) | 100% |  |
| 166 | [ ] | STORY OF SEASONS: Grand Bazaar (STEAM) | 35 | 50 | 70% (90d) | Controller issues (91%) | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 167 | [ ] | Ultimate Custom Night (STEAM) | 35 | 47 | 74% (90d) | No graphics (67%) | 81% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 168 | [ ] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 35 | 41 | 85% (90d) | Does not open (65%) | 72% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 169 | [ ] | COCOON (STEAM) | 34 | 66 | 52% (90d) | Directx error (44%) | 87% |  |
| 170 | [ ] | Torchlight II (STEAM) | 34 | 64 | 53% (90d) | Does not open (50%) | 91% |  |
| 171 | [ ] | Resident Evil Village (STEAM) | 34 | 57 | 60% (90d) | Does not open (71%) | 85% |  |
| 172 | [ ] | Secrets of Grindea (STEAM) | 34 | 52 | 65% (90d) | Does not open (52%) | 80% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 173 | [ ] | Deus Ex™ GOTY Edition (GOG) | 34 | 51 | 67% (90d) | Does not open (42%) | 84% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 174 | [ ] | Metro: Last Light Complete Edition (STEAM) | 34 | 46 | 74% (90d) | Does not open (56%) | 64% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 175 | [ ] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 34 | 43 | 79% (90d) | Does not open (68%) | 92% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 176 | [ ] | Need for Speed™ (STEAM) | 34 | 38 | 89% (90d) | Does not open (71%) | 63% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 177 | [ ] | Hotline Miami (GOG) | 34 | 37 | 92% (90d) | Does not open (94%) | 75% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 178 | [ ] | Hero Siege (STEAM) | 33 | 58 | 57% (90d) | Graphics glitches (52%) | 61% |  |
| 179 | [ ] | Mega Man Star Force Legacy Collection (STEAM) | 33 | 54 | 61% (90d) | Controller issues (61%) | 64% |  |
| 180 | [ ] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 54 | 61% (90d) | Controller issues (84%) | 79% |  |
| 181 | [ ] | Russian Fishing 4 (STEAM) | 33 | 38 | 87% (90d) | Does not open (68%) | 62% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 182 | [ ] | Red Dead Redemption (STEAM) | 33 | 37 | 89% (90d) | Does not open (95%) | 84% |  |
| 183 | [ ] | Bloodstained: Curse of the Moon (STEAM) | 32 | 64 | 50% (90d) | Does not open (78%) | 67% |  |
| 184 | [ ] | Fallout 3 (STEAM) | 32 | 64 | 50% (90d) | Does not open (54%) | 85% |  |
| 185 | [ ] | Heroes of Might and Magic: Olden Era (STEAM) | 32 | 62 | 52% (90d) | Does not open (69%) | 89% |  |
| 186 | [ ] | Aethermancer (STEAM) | 32 | 53 | 60% (90d) | Does not open (77%) | 73% |  |
| 187 | [ ] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 32 | 51 | 63% (90d) | Does not open (47%) | 70% |  |
| 188 | [ ] | Supermarket Together (STEAM) | 32 | 47 | 68% (90d) | Does not open (71%) | 78% |  |
| 189 | [ ] | Moonlight Peaks (STEAM) | 32 | 46 | 70% (90d) | Does not open (63%) | 100% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 190 | [ ] | Nioh: Complete Edition (STEAM) | 32 | 41 | 78% (90d) | Does not open (56%) | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 191 | [ ] | Grand Theft Auto III (STEAM) | 32 | 40 | 80% (90d) | Does not open (50%) | 94% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 192 | [ ] | Path of Exile 2 (STEAM) | 32 | 37 | 86% (90d) | Does not open (96%) | 89% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 193 | [ ] | Library Of Ruina (STEAM) | 31 | 60 | 52% (90d) | Does not open (67%) | 82% |  |
| 194 | [ ] | Max Payne (STEAM) | 31 | 58 | 53% (90d) | No graphics (42%) | 96% |  |
| 195 | [ ] | LEGO® Harry Potter™ Collection (STEAM) | 31 | 57 | 54% (90d) | Does not open (85%) | 88% |  |
| 196 | [ ] | Binary Domain (STEAM) | 31 | 49 | 63% (90d) | Does not open (92%) | 85% |  |
| 197 | [ ] | Tower and Sword of Succubus (STEAM) | 31 | 48 | 65% (90d) | No graphics (81%) | 100% |  |
| 198 | [ ] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 31 | 41 | 76% (90d) | Controller issues (66%) | 93% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 199 | [ ] | Super Animal Royale (STEAM) | 31 | 39 | 79% (90d) | Does not open (70%) | 80% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 200 | [ ] | Cave Story+ (EPIC) | 30 | 58 | 52% (90d) | Does not open (42%) | 85% |  |
| 201 | [ ] | XCOM: Enemy Unknown Complete Pack (GOG) | 29 | 55 | 53% (90d) | Does not open (68%) | 73% |  |
| 202 | [ ] | Prince of Persia: The Sands of Time (STEAM) | 29 | 50 | 58% (90d) | Controller issues (48%) | 93% |  |
| 203 | [ ] | Zero Escape: The Nonary Games (STEAM) | 29 | 49 | 59% (90d) | Does not open (88%) | 69% |  |
| 204 | [ ] | Unturned (STEAM) | 29 | 48 | 60% (90d) | Does not open (60%) | 88% |  |
| 205 | [ ] | SWORN (STEAM) | 29 | 45 | 64% (90d) | Does not open (59%) | 100% |  |
| 206 | [ ] | Yakuza: Like a Dragon (STEAM) | 29 | 44 | 66% (90d) | Does not open (68%) | 73% |  |
| 207 | [ ] | Stellar Blade™ (STEAM) | 29 | 38 | 76% (90d) | Does not open (45%) | 88% |  |
| 208 | [ ] | Mortal Kombat X (STEAM) | 28 | 52 | 54% (90d) | Graphics glitches (55%) | 82% |  |
| 209 | [ ] | Heavy Rain (STEAM) | 28 | 49 | 57% (90d) | Controller issues (64%) | 86% |  |
| 210 | [ ] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 28 | 41 | 68% (90d) | Does not open (78%) | 88% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 211 | [ ] | Crab Game (STEAM) | 28 | 38 | 74% (90d) | Does not open (58%) | 67% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 212 | [ ] | Dead Island Riptide Definitive Edition (STEAM) | 27 | 50 | 54% (90d) | Does not open (52%) | 79% |  |
| 213 | [ ] | Akane (STEAM) | 27 | 46 | 59% (90d) | Controller issues (71%) | 100% |  |
| 214 | [ ] | Prince of Persia (GOG) | 27 | 44 | 61% (90d) | Does not open (95%) | 83% |  |
| 215 | [ ] | Ratatan (STEAM) | 27 | 41 | 66% (90d) | Does not open (47%) | 98% |  |
| 216 | [ ] | G.I. Joe Wrath of Cobra (EPIC) | 26 | 48 | 54% (90d) | Does not open (60%) | 71% |  |
| 217 | [ ] | Resident Evil Revelations 2 (STEAM) | 26 | 48 | 54% (90d) | Does not open (33%) | 91% |  |
| 218 | [ ] | Bongo Cat (STEAM) | 26 | 36 | 72% (90d) | Does not open (65%) | 77% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 219 | [ ] | Goose Goose Duck (STEAM) | 26 | 33 | 79% (90d) | Does not open (70%) | 77% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 220 | [ ] | Wizard of Legend (EPIC) | 25 | 44 | 57% (90d) | Does not open (79%) | 78% |  |
| 221 | [ ] | Being a DIK (STEAM) | 25 | 43 | 58% (90d) | Does not open (78%) | 88% |  |
| 222 | [ ] | Limbus Company (STEAM) | 25 | 40 | 63% (90d) | Does not open (85%) | 82% |  |
| 223 | [ ] | Cat Mail Co. (STEAM) | 25 | 39 | 64% (90d) | Does not open (90%) | 90% |  |
| 224 | [ ] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 25 | 39 | 64% (90d) | Does not open (100%) | 86% |  |
| 225 | [ ] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 32 | 78% (90d) | Does not open (87%) | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 226 | [ ] | Resident Evil (GOG) | 25 | 27 | 93% (90d) | Does not open (95%) | 76% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 227 | [ ] | DOOM + DOOM II (GOG) | 24 | 121 | 50% (1.3.0) | Graphics glitches (57%) | 64% |  |
| 228 | [ ] | Counter-Strike: Condition Zero (STEAM) | 24 | 42 | 57% (90d) | Does not open (53%) | 68% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 229 | [ ] | Timberborn (STEAM) | 24 | 36 | 67% (90d) | No graphics (64%) | 80% |  |
| 230 | [ ] | Palia (STEAM) | 24 | 34 | 71% (90d) | Does not open (63%) | 64% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 231 | [ ] | No Rest for the Wicked (STEAM) | 23 | 46 | 50% (90d) | Does not open (70%) | 73% |  |
| 232 | [ ] | PAC-MAN WORLD Re-PAC (STEAM) | 23 | 45 | 51% (90d) | Controller issues (63%) | 92% |  |
| 233 | [ ] | Football Manager 2024 (EPIC) | 23 | 42 | 55% (90d) | Does not open (86%) | 87% |  |
| 234 | [ ] | Overlord (STEAM) | 23 | 42 | 55% (90d) | Does not open (72%) | 75% |  |
| 235 | [ ] | One-armed robber (STEAM) | 23 | 39 | 59% (90d) | Controller issues (67%) | 80% |  |
| 236 | [ ] | Lobotomy Corporation (STEAM) | 23 | 38 | 76% (14d) | No graphics (60%) | 100% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 237 | [ ] | Worms W.M.D (STEAM) | 23 | 38 | 61% (90d) | Does not open (60%) | 91% |  |
| 238 | [ ] | Return to Monkey Island (STEAM) | 23 | 36 | 64% (90d) | No graphics (59%) | 91% |  |
| 239 | [ ] | Party Animals (STEAM) | 23 | 32 | 72% (90d) | Does not open (75%) | 76% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 240 | [ ] | FINAL FANTASY XIV Online (STEAM) | 23 | 30 | 77% (90d) | Does not open (100%) | 92% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 241 | [ ] | Hitman 2: Silent Assassin (STEAM) | 23 | 29 | 79% (90d) | Does not open (82%) | 73% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 242 | [ ] | Jade Empire: Special Edition (GOG) | 23 | 29 | 79% (90d) | Does not open (50%) | 74% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 243 | [ ] | The Witcher 3: Wild Hunt — Remastered (GOG) | 23 | 28 | 82% (90d) | Does not open (40%) | 63% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 244 | [ ] | TCG Card Shop Simulator (STEAM) | 22 | 41 | 54% (90d) | Does not open (58%) | 86% |  |
| 245 | [ ] | This War of Mine (STEAM) | 22 | 38 | 58% (90d) | No graphics (63%) | 69% |  |
| 246 | [ ] | GRIP: Combat Racing (STEAM) | 22 | 36 | 61% (90d) | Does not open (94%) | 84% |  |
| 247 | [ ] | Digimon Survive (STEAM) | 22 | 35 | 63% (90d) | Controller issues (74%) | 93% |  |
| 248 | [ ] | Life is Strange Remastered (STEAM) | 22 | 34 | 65% (90d) | Does not open (73%) | 92% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 249 | [ ] | Nex Machina (STEAM) | 22 | 30 | 73% (90d) | Does not open (53%) | 85% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 250 | [ ] | ENA: Dream BBQ (STEAM) | 21 | 76 | 50% (14d) | Graphics glitches (44%) | 79% |  |
| 251 | [ ] | Backpack Battles (STEAM) | 21 | 42 | 50% (90d) | Does not open (62%) | 93% |  |
| 252 | [ ] | Gambonanza (STEAM) | 21 | 42 | 50% (90d) | Does not open (60%) | 96% |  |
| 253 | [ ] | Hatred (STEAM) | 21 | 41 | 51% (90d) | Does not open (71%) | 80% |  |
| 254 | [ ] | Pinball FX Classic (STEAM) | 21 | 39 | 54% (90d) | Does not open (75%) | 85% |  |
| 255 | [ ] | Control Ultimate Edition (GOG) | 21 | 38 | 55% (90d) | Does not open (82%) | 96% |  |
| 256 | [ ] | Trailmakers (STEAM) | 21 | 38 | 55% (90d) | Does not open (41%) | 89% |  |
| 257 | [ ] | Changed (STEAM) | 21 | 35 | 60% (90d) | Does not open (60%) | 90% |  |
| 258 | [ ] | DNF Duel (EPIC) | 21 | 34 | 62% (90d) | Does not open (50%) | 85% |  |
| 259 | [ ] | Hitman: Absolution (GOG) | 21 | 32 | 66% (90d) | Does not open (85%) | 100% |  |
| 260 | [ ] | Beyond: Two Souls (STEAM) | 21 | 29 | 72% (90d) | Does not open (50%) | 71% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 261 | [ ] | Torchlight II (EPIC) | 21 | 29 | 72% (90d) | Does not open (86%) | 100% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 262 | [ ] | Tiny Glade (STEAM) | 20 | 36 | 56% (90d) | No graphics (44%) | 80% |  |
| 263 | [ ] | Dead Rising 2 (STEAM) | 20 | 33 | 61% (90d) | Does not open (78%) | 72% |  |
| 264 | [ ] | DOOM 3: BFG Edition (GOG) | 20 | 28 | 71% (90d) | No graphics (65%) | 81% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 265 | [ ] | Dishonored 2 (STEAM) | 20 | 28 | 71% (90d) | Does not open (88%) | 91% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 266 | [ ] | Farming Simulator 25 (STEAM) | 20 | 28 | 71% (90d) | Does not open (75%) | 76% |  |
| 267 | [ ] | Dead Island (STEAM) | 20 | 25 | 80% (90d) | Does not open (69%) | 71% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 268 | [ ] | Killing Floor (STEAM) | 19 | 37 | 51% (90d) | Controller issues (100%) | 92% |  |
| 269 | [ ] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 19 | 36 | 53% (90d) | Does not open (63%) | 67% |  |
| 270 | [ ] | Mini Metro (STEAM) | 19 | 36 | 53% (90d) | Does not open (39%) | 62% |  |
| 271 | [ ] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 19 | 33 | 58% (90d) | Does not open (60%) | 93% |  |
| 272 | [ ] | Tabletop Simulator (STEAM) | 19 | 32 | 59% (90d) | No graphics (50%) | 71% |  |
| 273 | [ ] | Maneater (STEAM) | 19 | 30 | 63% (90d) | Does not open (93%) | 82% |  |
| 274 | [ ] | Metro Exodus (STEAM) | 19 | 30 | 63% (90d) | Does not open (82%) | 89% |  |
| 275 | [ ] | 3on3 FreeStyle: Rebound (STEAM) | 19 | 24 | 79% (90d) | Does not open (82%) | 100% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 276 | [ ] | Brothers - A Tale of Two Sons (EPIC) | 18 | 36 | 50% (90d) | Does not open (50%) | 80% |  |
| 277 | [ ] | SKALD: Against the Black Priory (STEAM) | 18 | 36 | 50% (90d) | No graphics (67%) | 100% |  |
| 278 | [ ] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 18 | 35 | 51% (90d) | Controller issues (50%) | 100% |  |
| 279 | [ ] | Faster Than Light (EPIC) | 18 | 34 | 53% (90d) | Does not open (41%) | 91% |  |
| 280 | [ ] | Stick It to the Stickman (STEAM) | 18 | 34 | 53% (90d) | Does not open (87%) | 79% |  |
| 281 | [ ] | Antichamber (STEAM) | 18 | 32 | 56% (90d) | Does not open (47%) | 83% |  |
| 282 | [ ] | Grim Fandango Remastered (STEAM) | 18 | 31 | 58% (90d) | Does not open (94%) | 75% |  |
| 283 | [ ] | Titanfall® 2 (STEAM) | 18 | 30 | 60% (90d) | Does not open (83%) | 92% |  |
| 284 | [ ] | Formula Legends (STEAM) | 18 | 29 | 62% (90d) | No graphics (60%) | 73% |  |
| 285 | [ ] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 18 | 27 | 67% (90d) | Does not open (100%) | 94% |  |
| 286 | [ ] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 25 | 72% (90d) | No graphics (44%) | 67% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 287 | [ ] | War Thunder (STEAM) | 18 | 24 | 75% (90d) | Does not open (53%) | 81% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 288 | [ ] | Spin Rhythm XD (STEAM) | 17 | 34 | 50% (90d) | Controller issues (88%) | 83% |  |
| 289 | [ ] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 17 | 33 | 52% (90d) | Does not open (87%) | 63% |  |
| 290 | [ ] | Arcade Paradise (EPIC) | 17 | 26 | 65% (90d) | Does not open (56%) | 80% |  |
| 291 | [ ] | Sonic and SEGA All Stars Racing (STEAM) | 17 | 25 | 68% (90d) | Does not open (69%) | 67% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 292 | [ ] | Katanaut (STEAM) | 17 | 24 | 71% (90d) | Does not open (75%) | 69% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 293 | [ ] | Cyberpunk 2077 (EPIC) | 17 | 22 | 77% (90d) | Does not open (50%) | 71% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 294 | [ ] | BioShock Infinite: Complete Edition (EPIC) | 16 | 32 | 50% (90d) | Does not open (92%) | 72% |  |
| 295 | [ ] | CULTIC (STEAM) | 16 | 32 | 50% (90d) | Does not open (92%) | 69% |  |
| 296 | [ ] | GRANDIA HD Remaster (STEAM) | 16 | 32 | 50% (90d) | Does not open (93%) | 67% |  |
| 297 | [ ] | Mortal Kombat 11 (STEAM) | 16 | 32 | 50% (90d) | Does not open (70%) | 62% |  |
| 298 | [ ] | Distance (STEAM) | 16 | 31 | 52% (90d) | Does not open (79%) | 84% |  |
| 299 | [ ] | Far Far West (STEAM) | 16 | 27 | 59% (90d) | Does not open (53%) | 93% |  |
| 300 | [ ] | WORLD OF FINAL FANTASY (STEAM) | 16 | 26 | 62% (90d) | No graphics (62%) | 69% |  |
| 301 | [ ] | Batman™: Arkham Origins (GOG) | 16 | 25 | 64% (90d) | Does not open (69%) | 92% |  |
| 302 | [ ] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 16 | 24 | 67% (90d) | Does not open (60%) | 72% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 303 | [ ] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 23 | 70% (90d) | No graphics (60%) | 83% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 304 | [ ] | Mortal Shell (EPIC) | 15 | 28 | 54% (90d) | No graphics (70%) | 80% |  |
| 305 | [ ] | LET IT DIE (STEAM) | 15 | 24 | 63% (90d) | Does not open (91%) | 70% |  |
| 306 | [ ] | Command & Conquer™ Generals Zero Hour (STEAM) | 15 | 23 | 65% (90d) | Does not open (92%) | 69% |  |
| 307 | [ ] | Horny Villa (STEAM) | 15 | 22 | 68% (90d) | Does not open (67%) | 100% |  |
| 308 | [ ] | Allumeria (STEAM) | 15 | 21 | 71% (90d) | Does not open (69%) | 67% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 309 | [ ] | BioShock 2 Remastered (EPIC) | 14 | 27 | 52% (90d) | Does not open (60%) | 94% |  |
| 310 | [ ] | Academy Love Saga: Tennis Angels EX (STEAM) | 14 | 23 | 61% (90d) | Does not open (77%) | 91% |  |
| 311 | [ ] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 23 | 61% (90d) | Does not open (90%) | 60% |  |
| 312 | [ ] | Injustice™ 2 (STEAM) | 14 | 23 | 61% (90d) | Does not open (91%) | 79% |  |
| 313 | [ ] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 14 | 23 | 61% (90d) | No graphics (62%) | 67% |  |
| 314 | [ ] | Disgaea 4 Complete+ (STEAM) | 14 | 22 | 64% (90d) | No graphics (43%) | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 315 | [ ] | Prince of Persia: The Two Thrones (STEAM) | 14 | 22 | 64% (90d) | Does not open (86%) | 62% |  |
| 316 | [ ] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 22 | 64% (90d) | Does not open (86%) | 87% |  |
| 317 | [ ] | Sons Of The Forest (STEAM) | 14 | 22 | 64% (90d) | Does not open (44%) | 77% |  |
| 318 | [ ] | Super Monkey Ball Banana Mania (STEAM) | 14 | 22 | 64% (90d) | Controller issues (57%) | 65% |  |
| 319 | [ ] | Escape the Backrooms (STEAM) | 14 | 21 | 67% (90d) | Does not open (100%) | 100% |  |
| 320 | [ ] | Fallout 2 (GOG) | 14 | 20 | 70% (90d) | Does not open (54%) | 80% |  |
| 321 | [ ] | Haiku, the Robot (STEAM) | 13 | 26 | 50% (90d) | Does not open (50%) | 90% |  |
| 322 | [ ] | Ys VIII: Lacrimosa of Dana (STEAM) | 13 | 26 | 50% (90d) | Does not open (73%) | 81% |  |
| 323 | [ ] | F.E.A.R. 2: Project Origin (STEAM) | 13 | 25 | 52% (90d) | Does not open (50%) | 81% |  |
| 324 | [ ] | Human Fall Flat (STEAM) | 13 | 25 | 52% (90d) | Does not open (58%) | 60% |  |
| 325 | [ ] | Minit (EPIC) | 13 | 23 | 57% (90d) | Does not open (82%) | 79% |  |
| 326 | [ ] | DiRT 4 (STEAM) | 13 | 22 | 59% (90d) | Does not open (75%) | 100% |  |
| 327 | [ ] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 22 | 59% (90d) | Does not open (80%) | 100% |  |
| 328 | [ ] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 13 | 20 | 65% (90d) | Does not open (33%) | 92% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 329 | [ ] | AER Memories of Old (EPIC) | 12 | 23 | 52% (90d) | Does not open (91%) | 90% |  |
| 330 | [ ] | SEGA Mega Drive & Genesis Classics (STEAM) | 12 | 23 | 52% (90d) | Graphics glitches (50%) | 65% |  |
| 331 | [ ] | Ultrapool (STEAM) | 12 | 23 | 52% (90d) | Does not open (64%) | 100% |  |
| 332 | [ ] | Capcom Arcade 2nd Stadium (STEAM) | 12 | 20 | 60% (90d) | Does not open (86%) | 83% |  |
| 333 | [ ] | 12 is Better Than 6 (STEAM) | 11 | 22 | 50% (90d) | Does not open (56%) | 79% |  |
| 334 | [ ] | REMATCH (STEAM) | 11 | 22 | 50% (90d) | Graphics glitches (67%) | 80% |  |
| 335 | [ ] | BioShock™ 2 Remastered (GOG) | 11 | 21 | 52% (90d) | Does not open (90%) | 80% |  |
| 336 | [ ] | Pocket Mirror ~ GoldenerTraum (STEAM) | 11 | 21 | 52% (90d) | Does not open (70%) | 100% |  |
| 337 | [ ] | Sonic Superstars (STEAM) | 11 | 21 | 52% (90d) | Does not open (67%) | 65% |  |
| 338 | [ ] | Castle in the Clouds (STEAM) | 11 | 20 | 55% (90d) | No graphics (63%) | 92% |  |
| 339 | [ ] | Ready or Not (STEAM) | 11 | 20 | 55% (90d) | Does not open (60%) | 91% |  |
| 340 | [ ] | Car Mechanic Simulator 2018 (STEAM) | 10 | 20 | 50% (90d) | Does not open (67%) | 92% |  |
| 341 | [ ] | HITMAN World of Assassination (STEAM) | 10 | 20 | 50% (90d) | Does not open (78%) | 88% |  |

## Recently recovered (318)

Games that left the two broken lists in the last 30 days. Their issues close after 3 nights in a row of staying out.

| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |
|---:|---|---|---:|---|---:|---:|---|
| 1 | [x] | The Elder Scrolls IV: Oblivion Game of the Year Edition (2009) (STEAM) | 282 | 2026-10-23 | 321 | 60% | [#2](https://github.com/GameNative/gamenative-compat/issues/2) |
| 2 | [x] | METAL GEAR SOLID V: THE PHANTOM PAIN (STEAM) | 255 | 2026-10-19 | 302 | 65% | [#4](https://github.com/GameNative/gamenative-compat/issues/4) |
| 3 | [x] | The Witcher 3: Wild Hunt — Remastered (STEAM) | 217 | 2026-10-18 | 332 | 61% |  |
| 4 | [x] | OMORI (STEAM) | 213 | 2026-10-16 | 258 | 74% |  |
| 5 | [x] | Devil May Cry HD Collection (STEAM) | 197 | 2026-10-19 | 274 | 70% |  |
| 6 | [x] | Burnout Paradise: The Ultimate Box (STEAM) | 165 | 2026-10-16 | 245 | 69% |  |
| 7 | [x] | Counter-Strike (STEAM) | 160 | 2026-10-22 | 247 | 53% | [#14](https://github.com/GameNative/gamenative-compat/issues/14) |
| 8 | [x] | Far Cry® 3 (STEAM) | 146 | 2026-10-21 | 165 | 64% | [#16](https://github.com/GameNative/gamenative-compat/issues/16) |
| 9 | [x] | FINAL FANTASY RESONANCE (STEAM) | 134 | 2026-10-24 | 302 | 69% |  |
| 10 | [x] | Borderlands 2 (EPIC) | 127 | 2026-10-25 | 148 | 63% | [#460](https://github.com/GameNative/gamenative-compat/issues/460) |
| 11 | [x] | Minecraft Dungeons II (STEAM) | 122 | 2026-10-21 | 139 | 65% | [#418](https://github.com/GameNative/gamenative-compat/issues/418) |
| 12 | [x] | The Witcher: Enhanced Edition (STEAM) | 121 | 2026-10-25 | 138 | 60% | [#21](https://github.com/GameNative/gamenative-compat/issues/21) |
| 13 | [x] | Call of Duty: Black Ops III (STEAM) | 114 | 2026-10-18 | 238 | 70% |  |
| 14 | [x] | Moonstone Island (STEAM) | 113 | 2026-10-16 | 147 | 89% |  |
| 15 | [x] | FINAL FANTASY VIII - REMASTERED (STEAM) | 101 | 2026-10-25 | 158 | 60% |  |
| 16 | [x] | The Elder Scrolls IV: Oblivion - Game of the Year Edition Deluxe (GOG) | 97 | 2026-10-18 | 139 | 68% |  |
| 17 | [x] | Don't Starve Together (STEAM) | 95 | 2026-10-16 | 172 | 76% |  |
| 18 | [x] | METAL GEAR SOLID - Master Collection Version (STEAM) | 95 | 2026-10-17 | 129 | 100% | [#33](https://github.com/GameNative/gamenative-compat/issues/33) |
| 19 | [x] | Cry of Fear (STEAM) | 94 | 2026-10-18 | 180 | 90% |  |
| 20 | [x] | The Elder Scrolls V: Skyrim Special Edition (GOG) | 88 | 2026-10-18 | 131 | 71% |  |
| 21 | [x] | Ultra Street Fighter IV (STEAM) | 84 | 2026-10-17 | 180 | 70% |  |
| 22 | [x] | Catherine Classic (STEAM) | 82 | 2026-10-19 | 172 | 74% |  |
| 23 | [x] | DOOM 3: BFG Edition (STEAM) | 79 | 2026-10-19 | 111 | 67% | [#55](https://github.com/GameNative/gamenative-compat/issues/55) |
| 24 | [x] | Call of Duty: Modern Warfare 2 (2009) (STEAM) | 79 | 2026-10-21 | 103 | 70% | [#45](https://github.com/GameNative/gamenative-compat/issues/45) |
| 25 | [x] | Call of Juarez Gunslinger (STEAM) | 78 | 2026-10-18 | 92 | 62% | [#42](https://github.com/GameNative/gamenative-compat/issues/42) |
| 26 | [x] | Detroit: Become Human (STEAM) | 78 | 2026-10-17 | 80 | 68% | [#50](https://github.com/GameNative/gamenative-compat/issues/50) |
| 27 | [x] | Mega Man Zero/ZX Legacy Collection (STEAM) | 77 | 2026-10-17 | 103 | 91% | [#52](https://github.com/GameNative/gamenative-compat/issues/52) |
| 28 | [x] | Bayonetta (STEAM) | 76 | 2026-10-18 | 200 | 74% |  |
| 29 | [x] | Gunfire Reborn (STEAM) | 76 | 2026-10-22 | 84 | 91% | [#46](https://github.com/GameNative/gamenative-compat/issues/46) |
| 30 | [x] | Hogwarts Legacy (STEAM) | 74 | 2026-10-17 | 132 | 67% |  |
| 31 | [x] | Ni no Kuni Wrath of the White Witch™ Remastered (STEAM) | 74 | 2026-10-18 | 123 | 93% |  |
| 32 | [x] | Need for Speed: Hot Pursuit (STEAM) | 73 | 2026-10-25 | 100 | 75% | [#54](https://github.com/GameNative/gamenative-compat/issues/54) |
| 33 | [x] | Fable - The Lost Chapters (STEAM) | 72 | 2026-10-17 | 111 | 74% | [#79](https://github.com/GameNative/gamenative-compat/issues/79) |
| 34 | [x] | Fallout (STEAM) | 72 | 2026-10-18 | 110 | 76% |  |
| 35 | [x] | Dota 2 (STEAM) | 71 | 2026-10-17 | 104 | 78% |  |
| 36 | [x] | Disgaea 5 Complete (STEAM) | 69 | 2026-10-18 | 83 | 96% | [#77](https://github.com/GameNative/gamenative-compat/issues/77) |
| 37 | [x] | Don't Starve (STEAM) | 68 | 2026-10-16 | 140 | 84% |  |
| 38 | [x] | Spyro™ Reignited Trilogy (STEAM) | 68 | 2026-10-18 | 107 | 68% |  |
| 39 | [x] | TBH: Task Bar Hero (STEAM) | 68 | 2026-10-19 | 100 | 100% | [#40](https://github.com/GameNative/gamenative-compat/issues/40) |
| 40 | [x] | Borderlands: The Pre-Sequel (STEAM) | 68 | 2026-10-17 | 94 | 62% | [#69](https://github.com/GameNative/gamenative-compat/issues/69) |
| 41 | [x] | Five Nights at Freddy's: Into the Pit (EPIC) | 67 | 2026-10-17 | 92 | 88% | [#53](https://github.com/GameNative/gamenative-compat/issues/53) |
| 42 | [x] | Bloodstained: Ritual of the Night (EPIC) | 63 | 2026-10-19 | 117 | 64% |  |
| 43 | [x] | Sonic Lost World (STEAM) | 63 | 2026-10-18 | 102 | 93% |  |
| 44 | [x] | Sonic Adventure DX (STEAM) | 63 | 2026-10-17 | 99 | 70% |  |
| 45 | [x] | Big Walk (STEAM) | 63 | 2026-10-17 | 96 | 86% |  |
| 46 | [x] | Sonic Generations (STEAM) | 63 | 2026-10-17 | 73 | 62% | [#70](https://github.com/GameNative/gamenative-compat/issues/70) |
| 47 | [x] | A Plague Tale: Innocence (STEAM) | 63 | 2026-10-20 | 66 | 68% | [#64](https://github.com/GameNative/gamenative-compat/issues/64) |
| 48 | [x] | Poppy Playtime (STEAM) | 62 | 2026-10-17 | 111 | 83% |  |
| 49 | [x] | Borderlands 3 (STEAM) | 61 | 2026-10-19 | 73 | 100% | [#88](https://github.com/GameNative/gamenative-compat/issues/88) |
| 50 | [x] | American Truck Simulator (STEAM) | 60 | 2026-10-18 | 99 | 71% |  |
| 51 | [x] | eFootball™ (STEAM) | 59 | 2026-10-18 | 93 | 74% |  |
| 52 | [x] | Dead by Daylight (STEAM) | 59 | 2026-10-23 | 65 | 77% | [#92](https://github.com/GameNative/gamenative-compat/issues/92) |
| 53 | [x] | The Secret of Monkey Island: Special Edition (STEAM) | 58 | 2026-10-18 | 93 | 77% |  |
| 54 | [x] | Starbound (STEAM) | 57 | 2026-10-18 | 83 | 73% | [#420](https://github.com/GameNative/gamenative-compat/issues/420) |
| 55 | [x] | Guildrun Demo (STEAM) | 57 | 2026-10-22 | 81 | 80% |  |
| 56 | [x] | Until Then (STEAM) | 55 | 2026-10-17 | 96 | 96% |  |
| 57 | [x] | Sheepy: A Short Adventure (STEAM) | 55 | 2026-10-24 | 64 | 73% | [#87](https://github.com/GameNative/gamenative-compat/issues/87) |
| 58 | [x] | MudRunner (STEAM) | 54 | 2026-10-24 | 106 | 60% |  |
| 59 | [x] | A Plague Tale: Innocence (EPIC) | 54 | 2026-10-25 | 92 | 100% |  |
| 60 | [x] | MY HERO ULTRA RUMBLE (STEAM) | 54 | 2026-10-21 | 62 | 83% | [#91](https://github.com/GameNative/gamenative-compat/issues/91) |
| 61 | [x] | Teardown (STEAM) | 53 | 2026-10-17 | 94 | 76% |  |
| 62 | [x] | Street Fighter™ 6 (STEAM) | 53 | 2026-10-16 | 76 | 80% |  |
| 63 | [x] | Sable (EPIC) | 52 | 2026-10-18 | 91 | 74% |  |
| 64 | [x] | Star Wars: Battlefront 2 (Classic, 2005) (STEAM) | 51 | 2026-10-25 | 94 | 60% | [#443](https://github.com/GameNative/gamenative-compat/issues/443) |
| 65 | [x] | Okami HD (STEAM) | 51 | 2026-10-17 | 93 | 88% |  |
| 66 | [x] | Slay the Princess — The Pristine Cut (STEAM) | 51 | 2026-10-19 | 85 | 71% |  |
| 67 | [x] | Alex Kidd in Miracle World DX (EPIC) | 51 | 2026-10-22 | 55 | 100% | [#127](https://github.com/GameNative/gamenative-compat/issues/127) |
| 68 | [x] | Rivals of Aether II (STEAM) | 50 | 2026-10-20 | 76 | 68% |  |
| 69 | [x] | FINAL FANTASY VII (2013) (STEAM) | 50 | 2026-10-18 | 71 | 80% | [#102](https://github.com/GameNative/gamenative-compat/issues/102) |
| 70 | [x] | Watch_Dogs 2 (STEAM) | 50 | 2026-10-17 | 57 | 65% | [#103](https://github.com/GameNative/gamenative-compat/issues/103) |
| 71 | [x] | Tomb Raider: Anniversary (STEAM) | 48 | 2026-10-25 | 64 | 60% | [#110](https://github.com/GameNative/gamenative-compat/issues/110) |
| 72 | [x] | Dead Space (STEAM) | 48 | 2026-10-18 | 61 | 75% | [#131](https://github.com/GameNative/gamenative-compat/issues/131) |
| 73 | [x] | METAL GEAR SOLID 2: Sons of Liberty - Master Collection Version (STEAM) | 47 | 2026-10-17 | 77 | 97% |  |
| 74 | [x] | STEINS;GATE RE:BOOT (STEAM) | 47 | 2026-10-21 | 68 | 81% |  |
| 75 | [x] | Moonlighter (EPIC) | 47 | 2026-10-23 | 51 | 100% | [#152](https://github.com/GameNative/gamenative-compat/issues/152) |
| 76 | [x] | Dishonored - Definitive Edition (EPIC) | 46 | 2026-10-17 | 101 | 79% |  |
| 77 | [x] | Cobalt Core (STEAM) | 46 | 2026-10-18 | 95 | 87% |  |
| 78 | [x] | Digimon World: Next Order (STEAM) | 46 | 2026-10-18 | 87 | 97% |  |
| 79 | [x] | Plague Inc: Evolved (STEAM) | 46 | 2026-10-21 | 73 | 63% |  |
| 80 | [x] | Tomb Raider GOTY (GOG) | 45 | 2026-10-17 | 92 | 97% |  |
| 81 | [x] | Death Road to Canada (STEAM) | 44 | 2026-10-17 | 92 | 70% |  |
| 82 | [x] | Life is Strange™ (STEAM) | 44 | 2026-10-17 | 84 | 80% |  |
| 83 | [x] | PROTOTYPE 2 (STEAM) | 44 | 2026-10-18 | 84 | 83% |  |
| 84 | [x] | Salt and Sanctuary (STEAM) | 44 | 2026-10-18 | 79 | 83% |  |
| 85 | [x] | Capcom Fighting Collection (STEAM) | 43 | 2026-10-23 | 50 | 79% | [#97](https://github.com/GameNative/gamenative-compat/issues/97) |
| 86 | [x] | Rogue Legacy (STEAM) | 42 | 2026-10-17 | 92 | 53% |  |
| 87 | [x] | Deadlock (STEAM) | 41 | 2026-10-16 | 67 | 96% |  |
| 88 | [x] | The Witcher 2: Assassins of Kings Enhanced Edition (GOG) | 41 | 2026-10-18 | 62 | 66% | [#156](https://github.com/GameNative/gamenative-compat/issues/156) |
| 89 | [x] | Capcom Arcade Stadium (STEAM) | 41 | 2026-10-17 | 51 | 68% | [#140](https://github.com/GameNative/gamenative-compat/issues/140) |
| 90 | [x] | Amnesia: The Dark Descent (STEAM) | 40 | 2026-10-17 | 74 | 82% |  |
| 91 | [x] | ARMORED CORE™ VI FIRES OF RUBICON™ (STEAM) | 40 | 2026-10-17 | 73 | 84% |  |
| 92 | [x] | LEGO® Star Wars™: The Skywalker Saga (EPIC) | 40 | 2026-10-18 | 66 | 67% |  |
| 93 | [x] | Aggelos (STEAM) | 40 | 2026-10-21 | 54 | 92% | [#148](https://github.com/GameNative/gamenative-compat/issues/148) |
| 94 | [x] | Monster Hunter Wilds (STEAM) | 40 | 2026-10-23 | 41 | 71% | [#161](https://github.com/GameNative/gamenative-compat/issues/161) |
| 95 | [x] | Rayman Origins (STEAM) | 39 | 2026-10-17 | 85 | 78% |  |
| 96 | [x] | Tales of ARISE (STEAM) | 39 | 2026-10-16 | 66 | 93% |  |
| 97 | [x] | Abiotic Factor (STEAM) | 38 | 2026-10-18 | 71 | 70% |  |
| 98 | [x] | Rocket League (STEAM) | 38 | 2026-10-17 | 55 | 72% |  |
| 99 | [x] | CrossCode (GOG) | 37 | 2026-10-23 | 41 | 67% | [#175](https://github.com/GameNative/gamenative-compat/issues/175) |
| 100 | [x] | ASTLIBRA ～生きた証～ Revision (STEAM) | 36 | 2026-10-17 | 70 | 96% |  |
| 101 | [x] | Combolands: Roguelike Citybuilder (STEAM) | 36 | 2026-10-17 | 66 | 88% |  |
| 102 | [x] | Counter-Strike:Global Offensive (STEAM) | 36 | 2026-10-19 | 53 | 74% |  |
| 103 | [x] | Capcom Fighting Collection 2 (STEAM) | 36 | 2026-10-18 | 50 | 87% | [#149](https://github.com/GameNative/gamenative-compat/issues/149) |
| 104 | [x] | Romestead (STEAM) | 36 | 2026-10-18 | 47 | 83% | [#164](https://github.com/GameNative/gamenative-compat/issues/164) |
| 105 | [x] | SnowRunner (STEAM) | 36 | 2026-10-19 | 45 | 82% | [#130](https://github.com/GameNative/gamenative-compat/issues/130) |
| 106 | [x] | Lost Planet: Extreme Condition (STEAM) | 36 | 2026-10-25 | 43 | 62% | [#173](https://github.com/GameNative/gamenative-compat/issues/173) |
| 107 | [x] | POSTAL 2 (GOG) | 35 | 2026-10-22 | 70 | 100% |  |
| 108 | [x] | Street Fighter 30th Anniversary Collection (STEAM) | 35 | 2026-10-16 | 68 | 65% |  |
| 109 | [x] | Monster Hunter Stories (STEAM) | 35 | 2026-10-17 | 66 | 82% |  |
| 110 | [x] | Gothic II: Gold Classic (STEAM) | 35 | 2026-10-20 | 62 | 80% |  |
| 111 | [x] | Hearts of Iron IV (STEAM) | 35 | 2026-10-19 | 57 | 68% |  |
| 112 | [x] | Earthion (STEAM) | 35 | 2026-10-22 | 55 | 100% |  |
| 113 | [x] | STORY OF SEASONS: Grand Bazaar (STEAM) | 35 | 2026-10-21 | 50 | 100% | [#427](https://github.com/GameNative/gamenative-compat/issues/427) |
| 114 | [x] | Ultimate Custom Night (STEAM) | 35 | 2026-10-19 | 47 | 81% | [#182](https://github.com/GameNative/gamenative-compat/issues/182) |
| 115 | [x] | Need for Speed™ Hot Pursuit Remastered (STEAM) | 35 | 2026-10-18 | 41 | 72% | [#193](https://github.com/GameNative/gamenative-compat/issues/193) |
| 116 | [x] | Ultimate Chicken Horse (STEAM) | 34 | 2026-10-23 | 69 | 56% |  |
| 117 | [x] | COCOON (STEAM) | 34 | 2026-10-17 | 66 | 87% |  |
| 118 | [x] | Torchlight II (STEAM) | 34 | 2026-10-20 | 64 | 91% |  |
| 119 | [x] | Resident Evil Village (STEAM) | 34 | 2026-10-17 | 57 | 85% |  |
| 120 | [x] | Secrets of Grindea (STEAM) | 34 | 2026-10-20 | 52 | 80% | [#169](https://github.com/GameNative/gamenative-compat/issues/169) |
| 121 | [x] | Deus Ex™ GOTY Edition (GOG) | 34 | 2026-10-19 | 51 | 84% | [#170](https://github.com/GameNative/gamenative-compat/issues/170) |
| 122 | [x] | Metro: Last Light Complete Edition (STEAM) | 34 | 2026-10-24 | 46 | 64% | [#188](https://github.com/GameNative/gamenative-compat/issues/188) |
| 123 | [x] | METAL GEAR & METAL GEAR 2: Solid Snake (STEAM) | 34 | 2026-10-22 | 43 | 92% | [#179](https://github.com/GameNative/gamenative-compat/issues/179) |
| 124 | [x] | Need for Speed™ (STEAM) | 34 | 2026-10-18 | 38 | 63% | [#192](https://github.com/GameNative/gamenative-compat/issues/192) |
| 125 | [x] | Hotline Miami (GOG) | 34 | 2026-10-20 | 37 | 75% | [#166](https://github.com/GameNative/gamenative-compat/issues/166) |
| 126 | [x] | Darkest Dungeon® (EPIC) | 33 | 2026-10-22 | 71 | 62% |  |
| 127 | [x] | Little Nightmares (STEAM) | 33 | 2026-10-16 | 71 | 62% |  |
| 128 | [x] | Dying Light (EPIC) | 33 | 2026-10-17 | 69 | 95% |  |
| 129 | [x] | PlateUp! (STEAM) | 33 | 2026-10-16 | 68 | 80% |  |
| 130 | [x] | Hero Siege (STEAM) | 33 | 2026-10-21 | 58 | 61% |  |
| 131 | [x] | Mega Man Star Force Legacy Collection (STEAM) | 33 | 2026-10-19 | 54 | 64% |  |
| 132 | [x] | Monster Boy And The Cursed Kingdom (STEAM) | 33 | 2026-10-19 | 54 | 79% |  |
| 133 | [x] | Russian Fishing 4 (STEAM) | 33 | 2026-10-23 | 38 | 62% | [#214](https://github.com/GameNative/gamenative-compat/issues/214) |
| 134 | [x] | BlazBlue Centralfiction (STEAM) | 32 | 2026-10-17 | 68 | 79% |  |
| 135 | [x] | Bloodstained: Curse of the Moon (STEAM) | 32 | 2026-10-16 | 64 | 67% |  |
| 136 | [x] | Aethermancer (STEAM) | 32 | 2026-10-18 | 53 | 73% |  |
| 137 | [x] | The Elder Scrolls III: Morrowind GOTY Edition (GOG) | 32 | 2026-10-22 | 51 | 70% |  |
| 138 | [x] | Supermarket Together (STEAM) | 32 | 2026-10-19 | 47 | 78% |  |
| 139 | [x] | Moonlight Peaks (STEAM) | 32 | 2026-10-20 | 46 | 100% | [#426](https://github.com/GameNative/gamenative-compat/issues/426) |
| 140 | [x] | Nioh: Complete Edition (STEAM) | 32 | 2026-10-20 | 41 | 100% | [#204](https://github.com/GameNative/gamenative-compat/issues/204) |
| 141 | [x] | Grand Theft Auto III (STEAM) | 32 | 2026-10-17 | 40 | 94% | [#171](https://github.com/GameNative/gamenative-compat/issues/171) |
| 142 | [x] | Path of Exile 2 (STEAM) | 32 | 2026-10-18 | 37 | 89% | [#199](https://github.com/GameNative/gamenative-compat/issues/199) |
| 143 | [x] | Library Of Ruina (STEAM) | 31 | 2026-10-16 | 60 | 82% |  |
| 144 | [x] | Max Payne (STEAM) | 31 | 2026-10-17 | 58 | 96% |  |
| 145 | [x] | LEGO® Harry Potter™ Collection (STEAM) | 31 | 2026-10-17 | 57 | 88% |  |
| 146 | [x] | Binary Domain (STEAM) | 31 | 2026-10-18 | 49 | 85% |  |
| 147 | [x] | Tower and Sword of Succubus (STEAM) | 31 | 2026-10-22 | 48 | 100% |  |
| 148 | [x] | METAL GEAR SOLID 3: Snake Eater - Master Collection Version (STEAM) | 31 | 2026-10-20 | 41 | 93% | [#220](https://github.com/GameNative/gamenative-compat/issues/220) |
| 149 | [x] | Super Animal Royale (STEAM) | 31 | 2026-10-19 | 39 | 80% | [#237](https://github.com/GameNative/gamenative-compat/issues/237) |
| 150 | [x] | BioShock™ (GOG) | 30 | 2026-10-18 | 61 | 67% |  |
| 151 | [x] | Stumble Guys (STEAM) | 30 | 2026-10-18 | 61 | 87% |  |
| 152 | [x] | Cave Story+ (EPIC) | 30 | 2026-10-18 | 58 | 85% |  |
| 153 | [x] | XCOM: Enemy Unknown Complete Pack (GOG) | 29 | 2026-10-20 | 55 | 73% |  |
| 154 | [x] | Prince of Persia: The Sands of Time (STEAM) | 29 | 2026-10-20 | 50 | 93% |  |
| 155 | [x] | Zero Escape: The Nonary Games (STEAM) | 29 | 2026-10-17 | 49 | 69% |  |
| 156 | [x] | Unturned (STEAM) | 29 | 2026-10-17 | 48 | 88% |  |
| 157 | [x] | SWORN (STEAM) | 29 | 2026-10-23 | 45 | 100% |  |
| 158 | [x] | State of Decay: Year-One (STEAM) | 28 | 2026-10-18 | 61 | 84% |  |
| 159 | [x] | Mortal Kombat X (STEAM) | 28 | 2026-10-17 | 52 | 82% |  |
| 160 | [x] | Heavy Rain (STEAM) | 28 | 2026-10-18 | 49 | 86% |  |
| 161 | [x] | FINAL FANTASY XV WINDOWS EDITION (STEAM) | 28 | 2026-10-18 | 41 | 88% | [#240](https://github.com/GameNative/gamenative-compat/issues/240) |
| 162 | [x] | Crab Game (STEAM) | 28 | 2026-10-22 | 38 | 67% | [#197](https://github.com/GameNative/gamenative-compat/issues/197) |
| 163 | [x] | FlipWitch - Forbidden Sex Hex (STEAM) | 27 | 2026-10-19 | 92 | 91% |  |
| 164 | [x] | Dead Island Riptide Definitive Edition (STEAM) | 27 | 2026-10-18 | 50 | 79% |  |
| 165 | [x] | Akane (STEAM) | 27 | 2026-10-20 | 46 | 100% |  |
| 166 | [x] | Prince of Persia (GOG) | 27 | 2026-10-24 | 44 | 83% |  |
| 167 | [x] | Batman™ Arkham City - Game of the Year Edition (EPIC) | 26 | 2026-10-19 | 62 | 87% |  |
| 168 | [x] | G.I. Joe Wrath of Cobra (EPIC) | 26 | 2026-10-19 | 48 | 71% |  |
| 169 | [x] | Bongo Cat (STEAM) | 26 | 2026-10-20 | 36 | 77% | [#228](https://github.com/GameNative/gamenative-compat/issues/228) |
| 170 | [x] | Goose Goose Duck (STEAM) | 26 | 2026-10-25 | 33 | 77% | [#236](https://github.com/GameNative/gamenative-compat/issues/236) |
| 171 | [x] | Wizard of Legend (EPIC) | 25 | 2026-10-18 | 44 | 78% |  |
| 172 | [x] | Being a DIK (STEAM) | 25 | 2026-10-19 | 43 | 88% |  |
| 173 | [x] | Limbus Company (STEAM) | 25 | 2026-10-18 | 40 | 82% |  |
| 174 | [x] | Cat Mail Co. (STEAM) | 25 | 2026-10-24 | 39 | 90% |  |
| 175 | [x] | Mega Man Battle Network Legacy Collection Vol. 2 (STEAM) | 25 | 2026-10-17 | 39 | 86% |  |
| 176 | [x] | 창세기전 외전: 서풍의 광시곡 리마스터 (STEAM) | 25 | 2026-10-21 | 32 | 100% | [#257](https://github.com/GameNative/gamenative-compat/issues/257) |
| 177 | [x] | Resident Evil (GOG) | 25 | 2026-10-20 | 27 | 76% | [#265](https://github.com/GameNative/gamenative-compat/issues/265) |
| 178 | [x] | Poker Night at the Inventory (STEAM) | 24 | 2026-10-18 | 54 | 84% |  |
| 179 | [x] | Titan Quest Anniversary Edition (STEAM) | 24 | 2026-10-16 | 54 | 83% |  |
| 180 | [x] | ABZÛ (STEAM) | 24 | 2026-10-21 | 51 | 85% |  |
| 181 | [x] | Baldur's Gate: Enhanced Edition (STEAM) | 24 | 2026-10-16 | 50 | 25% |  |
| 182 | [x] | Counter-Strike: Condition Zero (STEAM) | 24 | 2026-10-17 | 42 | 68% | [#223](https://github.com/GameNative/gamenative-compat/issues/223) |
| 183 | [x] | Timberborn (STEAM) | 24 | 2026-10-25 | 36 | 80% |  |
| 184 | [x] | Palia (STEAM) | 24 | 2026-10-22 | 34 | 64% | [#267](https://github.com/GameNative/gamenative-compat/issues/267) |
| 185 | [x] | CarX Drift Racing Online (STEAM) | 23 | 2026-10-16 | 47 | 82% |  |
| 186 | [x] | No Rest for the Wicked (STEAM) | 23 | 2026-10-19 | 46 | 73% |  |
| 187 | [x] | PAC-MAN WORLD Re-PAC (STEAM) | 23 | 2026-10-24 | 45 | 92% |  |
| 188 | [x] | Football Manager 2024 (EPIC) | 23 | 2026-10-20 | 42 | 87% |  |
| 189 | [x] | Overlord (STEAM) | 23 | 2026-10-21 | 42 | 75% |  |
| 190 | [x] | One-armed robber (STEAM) | 23 | 2026-10-23 | 39 | 80% |  |
| 191 | [x] | Lobotomy Corporation (STEAM) | 23 | 2026-10-19 | 38 | 100% | [#351](https://github.com/GameNative/gamenative-compat/issues/351) |
| 192 | [x] | Return to Monkey Island (STEAM) | 23 | 2026-10-23 | 36 | 91% |  |
| 193 | [x] | Party Animals (STEAM) | 23 | 2026-10-17 | 32 | 76% | [#268](https://github.com/GameNative/gamenative-compat/issues/268) |
| 194 | [x] | FINAL FANTASY XIV Online (STEAM) | 23 | 2026-10-22 | 30 | 92% | [#270](https://github.com/GameNative/gamenative-compat/issues/270) |
| 195 | [x] | Jade Empire: Special Edition (GOG) | 23 | 2026-10-23 | 29 | 74% | [#276](https://github.com/GameNative/gamenative-compat/issues/276) |
| 196 | [x] | Hitman 2: Silent Assassin (STEAM) | 23 | 2026-10-22 | 29 | 73% | [#275](https://github.com/GameNative/gamenative-compat/issues/275) |
| 197 | [x] | The Witcher 3: Wild Hunt — Remastered (GOG) | 23 | 2026-10-25 | 28 | 63% | [#412](https://github.com/GameNative/gamenative-compat/issues/412) |
| 198 | [x] | WEBFISHING (STEAM) | 22 | 2026-10-17 | 49 | 91% |  |
| 199 | [x] | This War of Mine (STEAM) | 22 | 2026-10-21 | 38 | 69% |  |
| 200 | [x] | GRIP: Combat Racing (STEAM) | 22 | 2026-10-20 | 36 | 84% |  |
| 201 | [x] | Digimon Survive (STEAM) | 22 | 2026-10-23 | 35 | 93% |  |
| 202 | [x] | Life is Strange Remastered (STEAM) | 22 | 2026-10-20 | 34 | 92% | [#436](https://github.com/GameNative/gamenative-compat/issues/436) |
| 203 | [x] | Nex Machina (STEAM) | 22 | 2026-10-18 | 30 | 85% | [#323](https://github.com/GameNative/gamenative-compat/issues/323) |
| 204 | [x] | Saints Row IV (STEAM) | 21 | 2026-10-19 | 48 | 74% |  |
| 205 | [x] | MudRunner (EPIC) | 21 | 2026-10-18 | 43 | 86% |  |
| 206 | [x] | Backpack Battles (STEAM) | 21 | 2026-10-21 | 42 | 93% |  |
| 207 | [x] | Hatred (STEAM) | 21 | 2026-10-22 | 41 | 80% |  |
| 208 | [x] | Pinball FX Classic (STEAM) | 21 | 2026-10-23 | 39 | 85% |  |
| 209 | [x] | Trailmakers (STEAM) | 21 | 2026-10-21 | 38 | 89% |  |
| 210 | [x] | Changed (STEAM) | 21 | 2026-10-24 | 35 | 90% |  |
| 211 | [x] | DNF Duel (EPIC) | 21 | 2026-10-21 | 34 | 85% |  |
| 212 | [x] | Hitman: Absolution (GOG) | 21 | 2026-10-24 | 32 | 100% |  |
| 213 | [x] | Torchlight II (EPIC) | 21 | 2026-10-22 | 29 | 100% | [#444](https://github.com/GameNative/gamenative-compat/issues/444) |
| 214 | [x] | Beyond: Two Souls (STEAM) | 21 | 2026-10-22 | 29 | 71% | [#438](https://github.com/GameNative/gamenative-compat/issues/438) |
| 215 | [x] | Crimzon Clover World EXplosion (STEAM) | 20 | 2026-10-20 | 41 | 100% |  |
| 216 | [x] | Resident Evil 2 "R.P.D. Demo" (STEAM) | 20 | 2026-10-25 | 41 | 55% |  |
| 217 | [x] | Tiny Glade (STEAM) | 20 | 2026-10-24 | 36 | 80% |  |
| 218 | [x] | DOOM 3: BFG Edition (GOG) | 20 | 2026-10-19 | 28 | 81% | [#269](https://github.com/GameNative/gamenative-compat/issues/269) |
| 219 | [x] | Dishonored 2 (STEAM) | 20 | 2026-10-20 | 28 | 91% | [#353](https://github.com/GameNative/gamenative-compat/issues/353) |
| 220 | [x] | Farming Simulator 25 (STEAM) | 20 | 2026-10-21 | 28 | 76% |  |
| 221 | [x] | Dead Island (STEAM) | 20 | 2026-10-20 | 25 | 71% | [#437](https://github.com/GameNative/gamenative-compat/issues/437) |
| 222 | [x] | No Man's Sky (GOG) | 19 | 2026-10-19 | 40 | 73% |  |
| 223 | [x] | Slow Roads (STEAM) | 19 | 2026-10-22 | 40 | 94% |  |
| 224 | [x] | Graveyard Keeper (GOG) | 19 | 2026-10-25 | 39 | 23% |  |
| 225 | [x] | Killing Floor (STEAM) | 19 | 2026-10-19 | 37 | 92% |  |
| 226 | [x] | Batman™: Arkham Origins Blackgate - Deluxe Edition (STEAM) | 19 | 2026-10-20 | 36 | 67% |  |
| 227 | [x] | Mini Metro (STEAM) | 19 | 2026-10-20 | 36 | 62% |  |
| 228 | [x] | S.T.A.L.K.E.R.: Shadow of Chornobyl - Enhanced Edition (STEAM) | 19 | 2026-10-18 | 33 | 93% |  |
| 229 | [x] | Tabletop Simulator (STEAM) | 19 | 2026-10-19 | 32 | 71% |  |
| 230 | [x] | Maneater (STEAM) | 19 | 2026-10-20 | 30 | 82% |  |
| 231 | [x] | Metro Exodus (STEAM) | 19 | 2026-10-20 | 30 | 89% |  |
| 232 | [x] | 3on3 FreeStyle: Rebound (STEAM) | 19 | 2026-10-23 | 24 | 100% | [#410](https://github.com/GameNative/gamenative-compat/issues/410) |
| 233 | [x] | Kingdom Come: Deliverance II (STEAM) | 18 | 2026-10-20 | 39 | 92% |  |
| 234 | [x] | Brothers - A Tale of Two Sons (EPIC) | 18 | 2026-10-23 | 36 | 80% |  |
| 235 | [x] | SKALD: Against the Black Priory (STEAM) | 18 | 2026-10-20 | 36 | 100% |  |
| 236 | [x] | EARTH DEFENSE FORCE 4.1  The Shadow of New Despair (STEAM) | 18 | 2026-10-21 | 35 | 100% |  |
| 237 | [x] | Faster Than Light (EPIC) | 18 | 2026-10-24 | 34 | 91% |  |
| 238 | [x] | Stick It to the Stickman (STEAM) | 18 | 2026-10-17 | 34 | 79% |  |
| 239 | [x] | Antichamber (STEAM) | 18 | 2026-10-20 | 32 | 83% |  |
| 240 | [x] | Grim Fandango Remastered (STEAM) | 18 | 2026-10-19 | 31 | 75% |  |
| 241 | [x] | Titanfall® 2 (STEAM) | 18 | 2026-10-16 | 30 | 92% |  |
| 242 | [x] | Formula Legends (STEAM) | 18 | 2026-10-21 | 29 | 73% |  |
| 243 | [x] | Monster Hunter Stories 2: Wings of Ruin (STEAM) | 18 | 2026-10-21 | 27 | 94% |  |
| 244 | [x] | S.T.A.L.K.E.R.: Shadow of Chernobyl (STEAM) | 18 | 2026-10-20 | 25 | 67% | [#371](https://github.com/GameNative/gamenative-compat/issues/371) |
| 245 | [x] | War Thunder (STEAM) | 18 | 2026-10-21 | 24 | 81% | [#198](https://github.com/GameNative/gamenative-compat/issues/198) |
| 246 | [x] | Spin Rhythm XD (STEAM) | 17 | 2026-10-18 | 34 | 83% |  |
| 247 | [x] | Resident Evil 7 Teaser: Beginning Hour (STEAM) | 17 | 2026-10-21 | 33 | 63% |  |
| 248 | [x] | Arcade Paradise (EPIC) | 17 | 2026-10-25 | 26 | 80% |  |
| 249 | [x] | Sonic and SEGA All Stars Racing (STEAM) | 17 | 2026-10-19 | 25 | 67% | [#394](https://github.com/GameNative/gamenative-compat/issues/394) |
| 250 | [x] | Katanaut (STEAM) | 17 | 2026-10-20 | 24 | 69% | [#393](https://github.com/GameNative/gamenative-compat/issues/393) |
| 251 | [x] | Cyberpunk 2077 (EPIC) | 17 | 2026-10-19 | 22 | 71% | [#422](https://github.com/GameNative/gamenative-compat/issues/422) |
| 252 | [x] | Roguecraft DX (STEAM) | 16 | 2026-10-19 | 49 | 100% |  |
| 253 | [x] | CULTIC (STEAM) | 16 | 2026-10-24 | 32 | 69% |  |
| 254 | [x] | GRANDIA HD Remaster (STEAM) | 16 | 2026-10-22 | 32 | 67% |  |
| 255 | [x] | Mortal Kombat 11 (STEAM) | 16 | 2026-10-21 | 32 | 62% |  |
| 256 | [x] | Distance (STEAM) | 16 | 2026-10-19 | 31 | 84% |  |
| 257 | [x] | Far Far West (STEAM) | 16 | 2026-10-21 | 27 | 93% |  |
| 258 | [x] | WORLD OF FINAL FANTASY (STEAM) | 16 | 2026-10-19 | 26 | 69% |  |
| 259 | [x] | Batman™: Arkham Origins (GOG) | 16 | 2026-10-22 | 25 | 92% |  |
| 260 | [x] | The Legend of Heroes: Trails of Cold Steel (STEAM) | 16 | 2026-10-20 | 24 | 72% | [#373](https://github.com/GameNative/gamenative-compat/issues/373) |
| 261 | [x] | Freddy Fazbear's Pizzeria Simulator (STEAM) | 16 | 2026-10-21 | 23 | 83% | [#411](https://github.com/GameNative/gamenative-compat/issues/411) |
| 262 | [x] | Mortal Shell (EPIC) | 15 | 2026-10-19 | 28 | 80% |  |
| 263 | [x] | LET IT DIE (STEAM) | 15 | 2026-10-25 | 24 | 70% |  |
| 264 | [x] | Horny Villa (STEAM) | 15 | 2026-10-21 | 22 | 100% |  |
| 265 | [x] | Allumeria (STEAM) | 15 | 2026-10-23 | 21 | 67% | [#414](https://github.com/GameNative/gamenative-compat/issues/414) |
| 266 | [x] | Tom Clancy's Splinter Cell: Chaos Theory (STEAM) | 14 | 2026-10-16 | 31 | 86% |  |
| 267 | [x] | Rayman Origins (GOG) | 14 | 2026-10-25 | 29 | 57% |  |
| 268 | [x] | Academy Love Saga: Tennis Angels EX (STEAM) | 14 | 2026-10-21 | 23 | 91% |  |
| 269 | [x] | DYNASTY WARRIORS 8: Xtreme Legends Complete Edition (STEAM) | 14 | 2026-10-25 | 23 | 60% |  |
| 270 | [x] | Injustice™ 2 (STEAM) | 14 | 2026-10-17 | 23 | 79% |  |
| 271 | [x] | SD GUNDAM G GENERATION CROSS RAYS (STEAM) | 14 | 2026-10-21 | 23 | 67% |  |
| 272 | [x] | Disgaea 4 Complete+ (STEAM) | 14 | 2026-10-23 | 22 | 100% | [#421](https://github.com/GameNative/gamenative-compat/issues/421) |
| 273 | [x] | Prince of Persia: The Two Thrones (STEAM) | 14 | 2026-10-23 | 22 | 62% |  |
| 274 | [x] | Shadow Tactics: Blades of the Shogun (STEAM) | 14 | 2026-10-23 | 22 | 87% |  |
| 275 | [x] | Sons Of The Forest (STEAM) | 14 | 2026-10-19 | 22 | 77% |  |
| 276 | [x] | Super Monkey Ball Banana Mania (STEAM) | 14 | 2026-10-18 | 22 | 65% |  |
| 277 | [x] | Escape the Backrooms (STEAM) | 14 | 2026-10-25 | 21 | 100% |  |
| 278 | [x] | Middle-earth™: Shadow of War™ (STEAM) | 13 | 2026-10-16 | 37 | 81% |  |
| 279 | [x] | Blood: Fresh Supply (STEAM) | 13 | 2026-10-16 | 34 | 83% |  |
| 280 | [x] | One Finger Death Punch (STEAM) | 13 | 2026-10-18 | 30 | 65% |  |
| 281 | [x] | The WereCleaner (STEAM) | 13 | 2026-10-22 | 29 | 92% |  |
| 282 | [x] | Coromon (GOG) | 13 | 2026-10-19 | 27 | 59% |  |
| 283 | [x] | Haiku, the Robot (STEAM) | 13 | 2026-10-21 | 26 | 90% |  |
| 284 | [x] | F.E.A.R. 2: Project Origin (STEAM) | 13 | 2026-10-21 | 25 | 81% |  |
| 285 | [x] | DiRT 4 (STEAM) | 13 | 2026-10-20 | 22 | 100% |  |
| 286 | [x] | The Legend of Heroes: Trails of Cold Steel II (STEAM) | 13 | 2026-10-21 | 22 | 100% |  |
| 287 | [x] | RollerCoaster Tycoon® 3: Complete Edition (EPIC) | 13 | 2026-10-25 | 20 | 92% | [#409](https://github.com/GameNative/gamenative-compat/issues/409) |
| 288 | [x] | TowerFall Ascension (STEAM) | 12 | 2026-10-16 | 30 | 54% |  |
| 289 | [x] | STAR WARS™ Jedi Knight: Jedi Academy™ (STEAM) | 12 | 2026-10-19 | 28 | 100% |  |
| 290 | [x] | Battle Chasers: Nightwar (STEAM) | 12 | 2026-10-20 | 27 | 74% |  |
| 291 | [x] | Dead Space™ 3 (STEAM) | 12 | 2026-10-20 | 25 | 73% |  |
| 292 | [x] | Possessor(s) (STEAM) | 12 | 2026-10-24 | 25 | n/a |  |
| 293 | [x] | SEGA Mega Drive & Genesis Classics (STEAM) | 12 | 2026-10-20 | 23 | 65% |  |
| 294 | [x] | Ultrapool (STEAM) | 12 | 2026-10-24 | 23 | 100% |  |
| 295 | [x] | Capcom Arcade 2nd Stadium (STEAM) | 12 | 2026-10-24 | 20 | 83% |  |
| 296 | [x] | SteamWorld Heist (GOG) | 11 | 2026-10-25 | 23 | n/a |  |
| 297 | [x] | Haydee (STEAM) | 11 | 2026-10-22 | 23 | 92% |  |
| 298 | [x] | 12 is Better Than 6 (STEAM) | 11 | 2026-10-21 | 22 | 79% |  |
| 299 | [x] | REMATCH (STEAM) | 11 | 2026-10-19 | 22 | 80% |  |
| 300 | [x] | BioShock™ 2 Remastered (GOG) | 11 | 2026-10-23 | 21 | 80% |  |
| 301 | [x] | Pocket Mirror ~ GoldenerTraum (STEAM) | 11 | 2026-10-23 | 21 | 100% |  |
| 302 | [x] | Sonic Superstars (STEAM) | 11 | 2026-10-21 | 21 | 65% |  |
| 303 | [x] | Castle in the Clouds (STEAM) | 11 | 2026-10-21 | 20 | 92% |  |
| 304 | [x] | What Remains of Edith Finch (STEAM) | 10 | 2026-10-19 | 26 | 43% |  |
| 305 | [x] | Divinity: Original Sin (Classic) (STEAM) | 10 | 2026-10-16 | 24 | n/a |  |
| 306 | [x] | Sid Meier's Civilization VI (EPIC) | 10 | 2026-10-19 | 23 | 80% |  |
| 307 | [x] | Delver (STEAM) | 10 | 2026-10-17 | 22 | n/a |  |
| 308 | [x] | Hellblade: Senua's Sacrifice (STEAM) | 10 | 2026-10-23 | 22 | 80% |  |
| 309 | [x] | DRAGON BALL XENOVERSE (STEAM) | 10 | 2026-10-25 | 21 | 67% |  |
| 310 | [x] | Ratchet & Clank: Rift Apart (STEAM) | 10 | 2026-10-21 | 21 | 46% |  |
| 311 | [x] | Car Mechanic Simulator 2018 (STEAM) | 10 | 2026-10-22 | 20 | 92% |  |
| 312 | [x] | Drift86 (STEAM) | 10 | 2026-10-19 | 20 | 69% |  |
| 313 | [x] | Football Manager 2024 (STEAM) | 9 | 2026-10-16 | 20 | n/a |  |
| 314 | [x] | STAR WARS™ Battlefront (Classic, 2004) (STEAM) | 9 | 2026-10-20 | 20 | n/a |  |
| 315 | [x] | Gloomhaven (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 316 | [x] | Mafia II: Definitive Edition (STEAM) | 8 | 2026-10-16 | 21 | n/a |  |
| 317 | [x] | Intravenous (STEAM) | 8 | 2026-10-16 | 20 | 94% |  |
| 318 | [x] | Alex Kidd in Miracle World DX (STEAM) | 2 | 2026-10-16 | 36 | 80% |  |
