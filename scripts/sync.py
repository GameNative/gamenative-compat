#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
import time
import traceback
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKLIST_PATH = ROOT / "data" / "worklist.json"
STATE_PATH = ROOT / "data" / "state.json"
MARKDOWN_PATH = ROOT / "WORKLIST.md"

DEFAULT_URL = "https://api.gamenative.app/api/compat-worklist"
LABEL = "does-not-work"
LABEL_COLOR = "d73a4a"
LABEL_DESCRIPTION = "Game does not run in GameNative (auto-managed from the compat worklist)"
CLOSE_AFTER_SYNCS = 7
RECENT_DAYS = 30
MARKER_RE = re.compile(r"<!-- compat-worklist: (.+?) -->")

REASONS = {
    "does_not_open": "Does not open",
    "no_graphics": "No graphics",
    "graphics_glitches": "Graphics glitches",
    "controller": "Controller problems",
    "performance": "Poor performance",
    "audio": "Audio problems",
    "crashes": "Crashes",
}

SECTIONS = [
    ("BROKEN", "Does not work", "Open issues track these. Pick one and fix it."),
    ("LIKELY_BROKEN", "Probably does not work", "Fewer one-star ratings than the list above, or a thin sample. Needs confirmation on a device before it gets an issue."),
    ("FIRST_RUN_FRICTION", "Works, but the first launch usually fails", "Most users get a frame on screen eventually. The first run is the problem: a redistributable, a launcher, a login or a config change."),
]


def log(msg):
    print(msg, flush=True)


def today():
    return date.today().isoformat()


def game_key(game):
    return f"{game['store']}:{game['name']}"


def humanise_reason(reason):
    if not reason:
        return ""
    return REASONS.get(reason, reason.replace("_", " ").capitalize())


def md_escape(text):
    return str(text).replace("|", "\\|")


def pct(value):
    return "n/a" if value is None else f"{value}%"


def one_star_count(game):
    value = game.get("one_star")
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    return round(game["ratings"] * (game.get("one_star_pct") or 0) / 100)


def sort_key(game):
    return (-one_star_count(game), -game["ratings"], game["name"])


def fetch_worklist(url):
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "gamenative-compat-sync"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            if resp.status != 200:
                log(f"fetch: {url} returned HTTP {resp.status}; falling back to committed data/worklist.json")
                return None
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        log(f"fetch: {url} returned HTTP {e.code}; falling back to committed data/worklist.json")
        return None
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
        log(f"fetch: {url} failed ({e}); falling back to committed data/worklist.json")
        return None
    if not isinstance(data, dict) or not isinstance(data.get("games"), list):
        keys = ", ".join(sorted(data)[:6]) if isinstance(data, dict) else type(data).__name__
        log(f"fetch: {url} returned JSON without a games list (got: {keys}); falling back to committed data/worklist.json")
        return None
    log(f"fetch: got {len(data['games'])} games from {url}")
    return data


def load_json(path, default):
    if not path.exists():
        return default
    with path.open() as f:
        return json.load(f)


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, sort_keys=False)
        f.write("\n")


def is_broken_ish(verdict):
    return verdict in ("BROKEN", "LIKELY_BROKEN")


def update_state(worklist, state):
    games = state.setdefault("games", {})
    for game in worklist["games"]:
        key = game_key(game)
        verdict = game["verdict"]
        entry = games.get(key)
        if entry is None:
            if not is_broken_ish(verdict):
                continue
            entry = games[key] = {
                "name": game["name"],
                "store": game["store"],
                "issue_number": None,
                "non_broken_streak": 0,
                "recovered_since": None,
                "last_verdict": None,
            }
        previous = entry.get("last_verdict")
        if is_broken_ish(verdict):
            entry["non_broken_streak"] = 0
            entry["recovered_since"] = None
        else:
            entry["non_broken_streak"] = entry.get("non_broken_streak", 0) + 1
            if entry.get("recovered_since") is None and (is_broken_ish(previous) or game.get("recovered")):
                entry["recovered_since"] = today()
        entry["last_verdict"] = verdict
        entry["last_seen"] = today()
        entry["ratings"] = game["ratings"]
        entry["one_star"] = one_star_count(game)
        entry["users_rendered_pct"] = game.get("users_rendered_pct")
    state["last_sync"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    state["release"] = worklist.get("release")
    return state


def issue_url(repo, number):
    if repo:
        return f"https://github.com/{repo}/issues/{number}"
    return f"../../issues/{number}"


def render_table(games, state_games, repo):
    lines = [
        "| # | | Game | One-star ratings | Ratings | One-star | Top reason | Users rendered | Issue |",
        "|---:|---|---|---:|---:|---:|---|---:|---|",
    ]
    for rank, g in enumerate(sorted(games, key=sort_key), 1):
        box = "[x]" if g.get("recovered") else "[ ]"
        reason = humanise_reason(g.get("top_reason"))
        if reason and g.get("reason_pct") is not None:
            reason = f"{reason} ({g['reason_pct']}%)"
        entry = state_games.get(game_key(g)) or {}
        number = entry.get("issue_number")
        issue = f"[#{number}]({issue_url(repo, number)})" if number else ""
        lines.append(
            f"| {rank} | {box} | {md_escape(g['name'])} ({g['store']}) | {one_star_count(g)} | {g['ratings']} | {g['one_star_pct']}% | "
            f"{reason or 'n/a'} | {pct(g.get('users_rendered_pct'))} | {issue} |"
        )
    return lines


def render_markdown(worklist, state, repo):
    games = worklist["games"]
    counts = {}
    for g in games:
        counts[g["verdict"]] = counts.get(g["verdict"], 0) + 1
    window = worklist.get("window", {})
    rules = worklist.get("rules", {})
    state_games = state.get("games", {})

    out = []
    out.append("# GameNative compatibility worklist")
    out.append("")
    out.append(f"Generated: `{worklist.get('generated_at')}` · App release: `{worklist.get('release')}` · "
               f"Ratings since: `{window.get('ratings_since')}` · Telemetry window: `{window.get('telemetry_days')}` days on `{window.get('gpu')}`")
    out.append("")
    out.append("This file is rewritten every night. Do not edit it by hand. See the [README](README.md) for how to read it and how to help.")
    out.append("")
    out.append("## How a game lands here")
    out.append("")
    out.append(f"- **Does not work**: {rules.get('broken', 'n/a')}.")
    out.append(f"- **Probably does not work**: {rules.get('likely_broken', 'n/a')}.")
    out.append(f"- **Works, but the first launch usually fails**: {rules.get('first_run_friction', 'n/a')}.")
    out.append(f"- **Recovered**: {rules.get('recovered', 'n/a')}.")
    out.append("")
    out.append("\"Users rendered\" is the share of users on Adreno GPUs with the Turnip driver who got the game to put a frame on screen at least once on the current release. Other GPUs are not counted. \"n/a\" means no telemetry for that game yet.")
    out.append("")
    out.append("## Counts")
    out.append("")
    out.append("| Verdict | Games |")
    out.append("|---|---:|")
    for verdict, label in [("BROKEN", "Does not work"), ("LIKELY_BROKEN", "Probably does not work"),
                           ("FIRST_RUN_FRICTION", "First launch fails"), ("MIXED", "Mixed"), ("WORKS", "Works")]:
        out.append(f"| {label} | {counts.get(verdict, 0)} |")
    out.append(f"| Total | {len(games)} |")
    out.append("")

    for verdict, heading, blurb in SECTIONS:
        subset = [g for g in games if g["verdict"] == verdict]
        out.append(f"## {heading} ({len(subset)})")
        out.append("")
        out.append(blurb)
        out.append("")
        if subset:
            out.extend(render_table(subset, state_games, repo))
        else:
            out.append("Nothing here right now.")
        out.append("")

    cutoff = date.today() - timedelta(days=RECENT_DAYS)
    by_key = {game_key(g): g for g in games}
    recent = []
    for key, entry in state_games.items():
        since = entry.get("recovered_since")
        if not since:
            continue
        try:
            if date.fromisoformat(since) < cutoff:
                continue
        except ValueError:
            continue
        recent.append((since, key, entry))
    out.append(f"## Recently recovered ({len(recent)})")
    out.append("")
    out.append(f"Games that left the two broken lists in the last {RECENT_DAYS} days. Their issues close after {CLOSE_AFTER_SYNCS} nights in a row of staying out.")
    out.append("")
    if recent:
        out.append("| # | | Game | One-star ratings | Recovered since | Ratings | Users rendered | Issue |")
        out.append("|---:|---|---|---:|---|---:|---:|---|")

        def recent_key(item):
            since, key, entry = item
            g = by_key.get(key)
            one_star = one_star_count(g) if g else entry.get("one_star") or 0
            ratings = g["ratings"] if g else entry.get("ratings") or 0
            return (-one_star, -ratings, key)

        for rank, (since, key, entry) in enumerate(sorted(recent, key=recent_key), 1):
            g = by_key.get(key)
            one_star = one_star_count(g) if g else entry.get("one_star", "")
            ratings = g["ratings"] if g else entry.get("ratings", "")
            rendered = pct(g.get("users_rendered_pct")) if g else pct(entry.get("users_rendered_pct"))
            number = entry.get("issue_number")
            issue = f"[#{number}]({issue_url(repo, number)})" if number else ""
            out.append(f"| {rank} | [x] | {md_escape(entry.get('name', key))} ({entry.get('store', '')}) | {one_star} | {since} | {ratings} | {rendered} | {issue} |")
    else:
        out.append("Nothing yet.")
    out.append("")
    return "\n".join(out)


def issue_title(game):
    return f"{game['name']} ({game['store']}) does not work"


def marker_for(game):
    return f"<!-- compat-worklist: {game_key(game).replace('--', '-')} -->"


def issue_body(game, worklist, repo):
    window = worklist.get("window", {})
    reason = humanise_reason(game.get("top_reason")) or "n/a"
    if game.get("reason_pct") is not None and game.get("top_reason"):
        reason = f"{reason} ({game['reason_pct']}% of tagged one-star ratings)"
    rows = [
        ("Store", game["store"]),
        ("Store app id", game.get("app_id") or "n/a"),
        ("Verdict", game["verdict"]),
        ("Ratings", str(game["ratings"])),
        ("Devices that rated", str(game.get("devices", "n/a"))),
        ("One-star ratings", f"{one_star_count(game)} ({game['one_star_pct']}%)"),
        ("One-star devices", pct(game.get("one_star_devices_pct"))),
        ("Top reason", reason),
        (f"Ratings on release {worklist.get('release')}", f"{game.get('ratings_recent', 'n/a')} ({game.get('one_star_recent', 'n/a')} one-star)"),
        (f"Telemetry users ({window.get('gpu', 'n/a')}, {window.get('telemetry_days', 'n/a')} days)", str(game.get("telemetry_users") if game.get("telemetry_users") is not None else "n/a")),
        ("Users who ever rendered a frame", pct(game.get("users_rendered_pct"))),
        ("Sessions per user", str(game.get("sessions_per_user") if game.get("sessions_per_user") is not None else "n/a")),
        ("Typical failed windows", game.get("typical_failed_windows") or "n/a"),
    ]
    worklist_link = f"https://github.com/{repo}/blob/main/WORKLIST.md" if repo else "WORKLIST.md"
    lines = [
        f"**{game['name']}** ({game['store']}) {'does not run' if is_broken_ish(game['verdict']) else 'is no longer on the broken lists'} in GameNative on app release {worklist.get('release')}.",
        "",
        "| Metric | Value |",
        "|---|---|",
    ]
    lines += [f"| {k} | {md_escape(v)} |" for k, v in rows]
    lines += [
        "",
        f"Data as of `{worklist.get('generated_at')}`. See the [worklist]({worklist_link}) for how these numbers are produced.",
        "",
        f"This issue is managed by the nightly sync. The metrics above refresh automatically; comments are left alone. It closes on its own once the game stays out of the broken lists for {CLOSE_AFTER_SYNCS} nights in a row and reopens if the game breaks again. To stop that for a game we will not fix, close the issue as \"not planned\" and the sync leaves it alone.",
        "",
        marker_for(game),
    ]
    return "\n".join(lines)


class GitHub:
    def __init__(self, token, repo, dry_run):
        self.token = token
        self.repo = repo
        self.dry_run = dry_run
        self.base = "https://api.github.com"
        self.writes = 0

    def _request(self, method, path, body=None, params=None):
        url = f"{self.base}{path}"
        if params:
            url += "?" + urllib.parse.urlencode(params)
        data = json.dumps(body).encode("utf-8") if body is not None else None
        for attempt in range(6):
            req = urllib.request.Request(url, data=data, method=method, headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "gamenative-compat-sync",
                "Content-Type": "application/json",
            })
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    payload = resp.read().decode("utf-8")
                    return resp.status, (json.loads(payload) if payload else None)
            except urllib.error.HTTPError as e:
                remaining = e.headers.get("X-RateLimit-Remaining")
                retry_after = e.headers.get("Retry-After")
                if e.code in (403, 429) and (remaining == "0" or retry_after):
                    if retry_after:
                        wait = int(retry_after)
                    else:
                        reset = int(e.headers.get("X-RateLimit-Reset", "0"))
                        wait = max(5, reset - int(time.time()) + 2)
                    wait = min(wait, 3600)
                    log(f"github: rate limited on {method} {path}; sleeping {wait}s")
                    time.sleep(wait)
                    continue
                if e.code >= 500 and attempt < 5:
                    time.sleep(5 * (attempt + 1))
                    continue
                detail = e.read().decode("utf-8", "replace")[:300]
                raise RuntimeError(f"GitHub {method} {path} failed: HTTP {e.code} {detail}")
        raise RuntimeError(f"GitHub {method} {path} failed after retries")

    def get(self, path, params=None):
        return self._request("GET", path, params=params)[1]

    def write(self, method, path, body):
        self.writes += 1
        status, data = self._request(method, path, body=body)
        time.sleep(1)
        return data

    def ensure_label(self):
        try:
            self.get(f"/repos/{self.repo}/labels/{urllib.parse.quote(LABEL)}")
            return
        except RuntimeError as e:
            if "HTTP 404" not in str(e):
                raise
        if self.dry_run:
            log(f"[dry-run] would create label '{LABEL}'")
            return
        self.write("POST", f"/repos/{self.repo}/labels", {"name": LABEL, "color": LABEL_COLOR, "description": LABEL_DESCRIPTION})
        log(f"github: created label '{LABEL}'")

    def list_labelled_issues(self):
        issues = {}
        page = 1
        while True:
            batch = self.get(f"/repos/{self.repo}/issues", {"labels": LABEL, "state": "all", "per_page": 100, "page": page})
            if not batch:
                break
            for issue in batch:
                if "pull_request" in issue:
                    continue
                m = MARKER_RE.search(issue.get("body") or "")
                if not m:
                    continue
                key = m.group(1)
                if key not in issues or issue["number"] > issues[key]["number"]:
                    issues[key] = issue
            if len(batch) < 100:
                break
            page += 1
        return issues

    def create_issue(self, title, body):
        return self.write("POST", f"/repos/{self.repo}/issues", {"title": title, "body": body, "labels": [LABEL]})

    def update_issue(self, number, **fields):
        return self.write("PATCH", f"/repos/{self.repo}/issues/{number}", fields)

    def comment(self, number, text):
        return self.write("POST", f"/repos/{self.repo}/issues/{number}/comments", {"body": text})


def manage_issues(worklist, state, args):
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    dry = args.dry_run
    if not dry and (not token or not repo):
        log("issues: GITHUB_TOKEN or GITHUB_REPOSITORY missing; skipping issue management")
        return
    gh = GitHub(token, repo, dry) if token and repo else None
    if dry and gh is None:
        log("[dry-run] no GITHUB_TOKEN/GITHUB_REPOSITORY; assuming no existing issues")

    state_games = state.setdefault("games", {})
    release = worklist.get("release")
    existing = {}
    if gh:
        gh.ensure_label()
        existing = gh.list_labelled_issues()
        log(f"issues: found {len(existing)} existing '{LABEL}' issues with a marker")

    by_key = {game_key(g): g for g in sorted(worklist["games"], key=sort_key)}
    planned = {"create": 0, "update": 0, "reopen": 0, "close": 0, "unchanged": 0}

    for key, issue in existing.items():
        entry = state_games.get(key)
        if entry is None:
            g = by_key.get(key)
            entry = state_games[key] = {
                "name": g["name"] if g else key.split(":", 1)[-1],
                "store": g["store"] if g else key.split(":", 1)[0],
                "issue_number": None,
                "non_broken_streak": 0,
                "recovered_since": None,
                "last_verdict": g["verdict"] if g else None,
            }
        entry["issue_number"] = issue["number"]

    for key, game in by_key.items():
        entry = state_games.get(key)
        issue = existing.get(key)
        number = entry.get("issue_number") if entry else None
        qualifies = game["verdict"] == "BROKEN"
        title = issue_title(game)
        body = issue_body(game, worklist, repo)

        if issue is None and number is None:
            if not qualifies:
                continue
            planned["create"] += 1
            if dry:
                log(f"[dry-run] create: {title}")
                continue
            created = gh.create_issue(title, body)
            entry["issue_number"] = created["number"]
            log(f"issues: created #{created['number']} {title}")
            continue

        if issue is None:
            if dry:
                log(f"[dry-run] #{number} is in state but was not found via the label; skipping")
            else:
                log(f"issues: #{number} for {key} is in state but was not found via the label; skipping")
            continue

        number = issue["number"]
        is_open = issue["state"] == "open"
        current_body = (issue.get("body") or "").replace("\r\n", "\n").rstrip()
        body_changed = current_body != body.rstrip() or issue.get("title") != title

        if game["verdict"] == "BROKEN":
            if not is_open and issue.get("state_reason") == "not_planned":
                log(f"issues: #{number} {title} was closed as not planned by a human; leaving it closed")
                planned["unchanged"] += 1
                continue
            if not is_open:
                planned["reopen"] += 1
                if dry:
                    log(f"[dry-run] reopen #{number}: {title}")
                else:
                    gh.update_issue(number, state="open", title=title, body=body)
                    gh.comment(number, f"Back on the \"does not work\" list on release {release}: {game['one_star_pct']}% one-star across {game['ratings']} ratings, {pct(game.get('users_rendered_pct'))} of telemetry users rendered a frame. Reopening.")
                    log(f"issues: reopened #{number} {title}")
                continue
            if body_changed:
                planned["update"] += 1
                if dry:
                    log(f"[dry-run] update #{number}: {title}")
                else:
                    gh.update_issue(number, title=title, body=body)
                    log(f"issues: updated #{number} {title}")
            else:
                planned["unchanged"] += 1
            continue

        streak = entry.get("non_broken_streak", 0)
        if is_open and streak >= CLOSE_AFTER_SYNCS:
            planned["close"] += 1
            if dry:
                log(f"[dry-run] close #{number}: {title} (non-broken for {streak} syncs, verdict {game['verdict']})")
            else:
                gh.update_issue(number, body=body)
                gh.comment(number, f"Out of the broken lists for {streak} nightly syncs in a row on release {release}. Verdict is now {game['verdict']}: {game['one_star_pct']}% one-star across {game['ratings']} ratings, {pct(game.get('users_rendered_pct'))} of telemetry users rendered a frame. Closing. The sync reopens this if the game breaks again.")
                gh.update_issue(number, state="closed", state_reason="completed")
                log(f"issues: closed #{number} {title}")
        elif is_open and body_changed:
            planned["update"] += 1
            if dry:
                log(f"[dry-run] update #{number}: {title} (verdict {game['verdict']}, streak {streak}/{CLOSE_AFTER_SYNCS})")
            else:
                gh.update_issue(number, title=title, body=body)
                log(f"issues: updated #{number} {title}")
        else:
            planned["unchanged"] += 1

    prefix = "[dry-run] plan" if dry else "issues: done"
    log(f"{prefix}: create {planned['create']}, update {planned['update']}, reopen {planned['reopen']}, close {planned['close']}, unchanged {planned['unchanged']}")


def main():
    parser = argparse.ArgumentParser(description="Sync the GameNative compat worklist, render WORKLIST.md and manage GitHub issues.")
    parser.add_argument("--dry-run", action="store_true", help="print planned issue actions instead of calling GitHub")
    parser.add_argument("--no-issues", action="store_true", help="skip issue management entirely")
    parser.add_argument("--url", default=os.environ.get("WORKLIST_URL", DEFAULT_URL))
    args = parser.parse_args()

    fetched = fetch_worklist(args.url)
    if fetched is not None:
        save_json(WORKLIST_PATH, fetched)
        worklist = fetched
    else:
        worklist = load_json(WORKLIST_PATH, None)
        if worklist is None:
            raise RuntimeError(f"no worklist available: fetch failed and {WORKLIST_PATH} does not exist")
        log(f"using committed {WORKLIST_PATH.relative_to(ROOT)} ({len(worklist['games'])} games, generated {worklist.get('generated_at')})")

    state = load_json(STATE_PATH, {"games": {}})
    update_state(worklist, state)

    if not args.no_issues:
        manage_issues(worklist, state, args)
    else:
        log("issues: skipped (--no-issues)")

    repo = os.environ.get("GITHUB_REPOSITORY")
    MARKDOWN_PATH.write_text(render_markdown(worklist, state, repo), encoding="utf-8")
    if not args.dry_run:
        save_json(STATE_PATH, state)
    counts = {}
    for g in worklist["games"]:
        counts[g["verdict"]] = counts.get(g["verdict"], 0) + 1
    log(f"rendered {MARKDOWN_PATH.relative_to(ROOT)}: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    if args.dry_run:
        log("[dry-run] state.json not written")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
