# GameNative compatibility worklist

A public list of PC games that do not run in [GameNative](https://gamenative.app), the Android app that runs Windows games. It is rebuilt every night from real usage data, and one GitHub issue is kept open per broken game until users can play it again.

- **[WORKLIST.md](WORKLIST.md)**: the rendered list. Start here.
- **[Issues labelled `does-not-work`](../../issues?q=label%3Adoes-not-work)**: one per broken game. These are the things to fix.
- **[data/worklist.json](data/worklist.json)**: the raw data, free to reuse.

## How to read the verdicts

Every game that has enough data gets one verdict:

| Verdict | Meaning |
|---|---|
| **Does not work** (`BROKEN`) | Most ratings are one star and most users never get a game window to draw a frame. Every game with this verdict gets an issue. |
| **Probably does not work** (`LIKELY_BROKEN`) | Half or more of the ratings are one star and rendering looks bad, but the signal is weaker. Needs someone to confirm on a device before it becomes an issue. |
| **Works, but the first launch usually fails** (`FIRST_RUN_FRICTION`) | Users complain, but most of them do get the game to render eventually. Usually a redistributable, launcher, login or setting that the first run trips over. |
| `MIXED` | Some users play, some do not. Not shown in the list. |
| `WORKS` | Fine. Not shown in the list. |

The tables are ordered by the number of one-star ratings, which is the count of players who hit the problem, so the top rows are where a fix helps the most people; the `#` column is just the row rank. The exact thresholds are in the header of WORKLIST.md; they come from the data file so they are always the ones used for the current render.

A game is **recovered** when it is no longer `BROKEN` or `LIKELY_BROKEN` on the current app release. Its row shows `[x]`, it moves to the "Recently recovered" section for 30 days, and its issue closes after it stays out of the broken lists for 3 nightly syncs in a row. If it breaks again, the issue reopens. Closing an issue by hand as "not planned" tells the sync to leave it closed for good; closing it as "completed" while the data still says broken gets it reopened the next night with a comment.

## How a game leaves the list

The verdict is judged on ratings from the **current app release** once a game has 20 of them, so a fix shipped in a release shows up as soon as players on that release rate it. With fewer, the last 14 days are used when they hold 20 ratings, which covers fixes shipped without an app release. Only then does the 90-day history decide. The one-star column says which window judged the row: the release number, `(14d)`, or `(90d)` for history.

## Where the data comes from

**Ratings.** GameNative shows a "How did the game run?" dialog on a game's first run and again after the user changes the game's config. The one-star answers carry a reason tag: does not open, no graphics, graphics glitches, controller problems. The "Top reason" column is the most common tag and the share of tagged one-star ratings that carry it.

**Telemetry.** Anonymous session reports from the app record whether the game's window ever rendered frames. "Users rendered" is the share of users who got at least one frame on screen, on the current release, in the telemetry window. A game with 10% rendered is broken for almost everyone. A game with 90% rendered and lots of one-star ratings has a first-run problem, not a runtime one.

The two signals are combined into the verdict by the API that produces `data/worklist.json`. This repo only renders and tracks it.

## Limits

- The telemetry column covers **Adreno GPUs with the Turnip driver only**. Mali, PowerVR, Xclipse and Adreno-with-stock-driver users are not represented in "Users rendered". A game can be fine on Adreno and dead on Mali, or the other way round; this list will not tell you.
- A game needs **20 ratings** to appear at all. Niche games are missing even if they are broken.
- Everything refers to the **current app release**. Ratings are counted from the date in the header; older ratings are not used.
- A game that rendered a frame is not necessarily playable. Crashes after the menu, missing audio, broken saves and bad performance all count as "rendered".
- The rating comes from the user's device and setup. A bad rating for a game can mean the game, the device, the GPU driver, a missing login or a slow download. The reason tag helps, but it is a guess by the user.

## How to help

1. Pick an issue from the [`does-not-work`](../../issues?q=is%3Aopen+label%3Adoes-not-work) list. The metrics table in the issue tells you how many users it affects and what they report.
2. Work out why it fails. Most fixes land in the app, in the Proton/Wine fork, in the GPU driver wrappers or in the per-game config that ships with the app.
3. Open a pull request in the relevant repository and link it from the issue.
4. Once the fix ships, tick the box: edit WORKLIST.md and change `[ ]` to `[x]` on the game's row. The nightly sync keeps the tick and the date it was set, so the row reads as "fixed, waiting for the data" until users start rendering the game. Then the game moves to "Recently recovered" and the issue closes a week later with a comment. You do not need to close anything by hand. Change the box back to `[ ]` if the fix did not take; the sync also clears it if the game recovers and then breaks again.

Comments on the issues are kept. The bot only rewrites the metrics table in the issue body.

## Reusing the data

`data/worklist.json` is public and updated nightly. Each game object has the store, name, store app id where known, rating counts and percentages, the top one-star reason, the telemetry numbers, the verdict and the recovered flag. The top-level object carries `generated_at`, `release`, the `window` used and the `rules` in plain words. Use it for whatever you like; a link back is appreciated.

## Running the sync yourself

```
python3 scripts/sync.py --no-issues     # fetch (or fall back to data/worklist.json) and render WORKLIST.md
python3 scripts/sync.py --dry-run       # also print the issue actions a real run would take
GITHUB_TOKEN=... GITHUB_REPOSITORY=owner/repo python3 scripts/sync.py
```

Python 3.11 or newer, standard library only. `WORKLIST_URL` overrides the API endpoint.
