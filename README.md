# GameNative compatibility worklist

A public list of PC games that do not run in [GameNative](https://gamenative.app), the Android app that runs Windows games. It is rebuilt every night from real usage data, and one GitHub issue is kept open per broken game until users can play it again.

- **[WORKLIST.md](WORKLIST.md)**: the rendered list. Start here.
- **[Issues labelled `does-not-work`](../../issues?q=label%3Adoes-not-work)**: one per broken game. These are the things to fix.
- **[data/worklist.json](data/worklist.json)**: the raw data, free to reuse.

## Popular games that do not work

The first list in WORKLIST.md is the most popular games that most players cannot play, most popular first. It is judged on play telemetry, not ratings:

- **Played 10 min**: of the players who launched the game at least twice on the newest app releases, the share who got 10 minutes of play with the game window rendering. A game is on the list when that share is far below the typical game on the same releases. When a release has few players for a game, the newest releases are counted together; "(few players)" means even that was not enough for a firm call.
- **Popularity** decides the order: everyone who ever launched the game, everyone who started an install, the phone models that rated it, and its Steam review count where known. It does not depend on how many people tried the game this week, so the order only moves when a game joins or leaves.
- A game joins after two nights in a row of failing and leaves after three nights in a row of working, so one noisy night does not move it.
- **Ever rendered**: the share of players whose game window rendered at least once. **By release**: "Played 10 min" per app release. **Failure**: what most failing players see, either no game window at all or a window followed by an exit. **Anti-cheat**: the anti-cheat the app detected, if most sessions report one. **Fix**: the date a config fix for the game shipped.
- Stores are merged by game name; the "Stores" column shows the split of players.
- Tools, VR-only titles and custom imports are left out.

"Works after a failed first run" lists games most players get running eventually even though their first session usually fails.

The lists further down are judged on ratings and work as described below. Issues and checklists still come from them.

## How to read the verdicts

Every game that has enough data gets one verdict:

| Verdict | Meaning |
|---|---|
| **Does not work** (`BROKEN`) | Most ratings are one star and most users never get a game window to draw a frame. Every game with this verdict gets an issue. |
| **Probably does not work** (`LIKELY_BROKEN`) | Half or more of the ratings are one star and rendering looks bad, but the signal is weaker. Needs someone to confirm on a device before it becomes an issue. |
| **Fix shipped, waiting for ratings** (`FIX_PENDING`) | A fix reached the game, and the list is waiting for ratings from players who have it. Kept off the broken lists until those ratings decide. |
| **Works, but the first launch usually fails** (`FIRST_RUN_FRICTION`) | Users complain, but most of them do get the game to render eventually. Usually a redistributable, launcher, login or setting that the first run trips over. |
| `MIXED` | Some users play, some do not. Not shown in the list. |
| `WORKS` | Fine. Not shown in the list. |

The tables are ordered by how many one-star ratings a game collects per day in the ratings that decided its verdict, so the top rows are where players hit the problem right now; the `#` column is just the row rank. The one-star columns show those same ratings, so the number next to a game is the one that put it there. The exact thresholds are in the header of WORKLIST.md; they come from the data file so they are always the ones used for the current render.

A game is **recovered** when it is no longer `BROKEN` or `LIKELY_BROKEN` (a game waiting for ratings after a fix is not counted as recovered yet). Its row shows `[x]`, it moves to the "Recently recovered" section for 30 days, and its issue closes after it stays out of the broken lists for 3 nightly syncs in a row. An issue also closes, with a comment, when its game has been missing from the list for 3 days (too few recent ratings to say anything).

An issue opens, or reopens, only after the game has been on the "does not work" list for 2 nightly syncs in a row, judged on current ratings. One bad night does not reopen anything. Closing an issue by hand as "not planned" tells the sync to leave it closed for good; closing it as "completed" while the data still says broken gets it reopened with a comment.

## How a game leaves the list

The verdict is judged on recent ratings, not on months of history, so a fix shows up as soon as players rate the game again. The one-star column says which ratings judged the row: `(14d)` for the last 14 days, `(last 20)` for the newest ratings of a game that is rated less often, or `(since fix)` for ratings given after a fix shipped. "Newest rating" says how old the newest of them is. When a fix ships for a game, it moves to "Fix shipped, waiting for ratings" until players who have the fix have rated it.

## Where the data comes from

**Ratings.** GameNative shows a "How did the game run?" dialog on a game's first run and again after the user changes the game's config. The one-star answers carry a reason tag: does not open, no graphics, graphics glitches, controller problems. The "Top reason" column is the most common tag and the share of tagged one-star ratings that carry it.

**Telemetry.** Anonymous session reports from the app record whether the game's window ever rendered frames. "Users rendered" is the share of users who got at least one frame on screen in the telemetry window, on any app version. A game with 10% rendered is broken for almost everyone. A game with 90% rendered and lots of one-star ratings has a first-run problem, not a runtime one.

The two signals are combined into the verdict by the API that produces `data/worklist.json`. This repo only renders and tracks it.

## Limits

- The telemetry column covers **Adreno GPUs with the Turnip driver only**. Mali, PowerVR, Xclipse and Adreno-with-stock-driver users are not represented in "Users rendered". A game can be fine on Adreno and dead on Mali, or the other way round; this list will not tell you.
- A game needs **20 ratings** to appear at all. Niche games are missing even if they are broken.
- Ratings are counted from the date in the header; older ratings are not used. Telemetry covers the number of days in the header. "Newest release rendered" covers the newest app release only.
- A game that rendered a frame is not necessarily playable. Crashes after the menu, missing audio, broken saves and bad performance all count as "rendered".
- The rating comes from the user's device and setup. A bad rating for a game can mean the game, the device, the GPU driver, a missing login or a slow download. The reason tag helps, but it is a guess by the user.

## How to help

1. Pick an issue from the [`does-not-work`](../../issues?q=is%3Aopen+label%3Adoes-not-work) list. The metrics table in the issue tells you how many users it affects and what they report.
2. Work out why it fails. Most fixes land in the app, in the Proton/Wine fork, in the GPU driver wrappers or in the per-game config that ships with the app.
3. Open a pull request in the relevant repository and link it from the issue.
4. Once the fix ships, tick the game off in the [checklist issues](../../issues?q=label%3Achecklist): one per section, with a clickable box per game. (Changing `[ ]` to `[x]` on the row in WORKLIST.md does the same.) The nightly sync keeps the tick and the date it was set, so the row reads as "fixed, waiting for the data" until users start rendering the game. Then the game moves to "Recently recovered" and the issue closes a week later with a comment. You do not need to close anything by hand. Change the box back to `[ ]` if the fix did not take; the sync also clears it if the game recovers and then breaks again.

Comments on the issues are kept. The bot only rewrites the metrics table in the issue body.

## Reusing the data

`data/worklist.json` is public and updated nightly. `not_working` holds the popular list (`games`) and the first-run list (`recovers_after_first_run`) with the numbers shown in WORKLIST.md. Each object in the top-level `games` list has the store, name, store app id where known, rating counts and percentages (over the full window and over the ratings that decided the verdict), the top one-star reason, the telemetry numbers, the verdict and the recovered flag. The top-level object carries `generated_at`, the `window` used and the `rules` in plain words. Use it for whatever you like; a link back is appreciated.

## Running the sync yourself

```
python3 scripts/sync.py --no-issues     # fetch (or fall back to data/worklist.json) and render WORKLIST.md
python3 scripts/sync.py --dry-run       # also print the issue actions a real run would take
GITHUB_TOKEN=... GITHUB_REPOSITORY=owner/repo python3 scripts/sync.py
```

Python 3.11 or newer, standard library only. `WORKLIST_URL` overrides the API endpoint.
