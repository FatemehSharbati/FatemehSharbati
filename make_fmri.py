#!/usr/bin/env python3
"""Contribution fMRI — a radiology-themed animated SVG of the GitHub
contribution graph.

Renders the last ~12 months of contributions as an fMRI activation map:
dark scanner background, hot-colormap cells, a sweeping slice-acquisition
beam, pulsing peak-activation voxels. Data comes live from the GitHub
GraphQL API, so re-running this script refreshes the image.

Usage: python3 make_fmri.py   (writes assets/fmri.svg)
Requires: gh CLI authenticated.
"""
import json
import subprocess
import datetime

LOGIN = "FatemehSharbati"
OUT = "assets/fmri.svg"

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""

# fMRI "hot" colormap: 0 = no signal, 4 = peak activation
LEVELS = ["#16203a", "#7c2d12", "#c2410c", "#f59e0b", "#fef3c7"]

CELL, GAP = 12, 4
PITCH = CELL + GAP
ROWS = 7


def fetch_calendar():
    r = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={QUERY}", "-f", f"login={LOGIN}"],
        capture_output=True, text=True, check=True)
    return json.loads(r.stdout)["data"]["user"][
        "contributionsCollection"]["contributionCalendar"]


def level(count, mx):
    if count <= 0 or mx <= 0:
        return 0
    q = count / mx
    if q <= 0.25:
        return 1
    if q <= 0.50:
        return 2
    if q <= 0.75:
        return 3
    return 4


def build(cal):
    weeks = cal["weeks"]
    total = cal["totalContributions"]
    ncols = len(weeks)

    # grid: col -> {row: count}
    grid, mx, peak = {}, 0, None
    for c, w in enumerate(weeks):
        for d in w["contributionDays"]:
            dt = datetime.date.fromisoformat(d["date"])
            row = (dt.weekday() + 1) % 7  # GitHub rows run Sunday..Saturday
            cnt = d["contributionCount"]
            grid[(c, row)] = (cnt, dt)
            if cnt > mx:
                mx, peak = cnt, (c, row)

    grid_w, grid_h = ncols * PITCH - GAP, ROWS * PITCH - GAP
    pad_x, pad_y = 28, 64
    W = pad_x * 2 + grid_w
    H = pad_y + grid_h + 56

    s = []
    A = s.append
    A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
      f'width="{W}" height="{H}" role="img" aria-label="Contribution fMRI">')
    A('<defs>'
      '<linearGradient id="beam" x1="0" y1="0" x2="1" y2="0">'
      '<stop offset="0" stop-color="#22d3ee" stop-opacity="0"/>'
      '<stop offset="0.7" stop-color="#22d3ee" stop-opacity="0.35"/>'
      '<stop offset="1" stop-color="#a5f3fc" stop-opacity="0.9"/>'
      '</linearGradient>'
      '<linearGradient id="hotbar" x1="0" y1="0" x2="1" y2="0">'
      + "".join(f'<stop offset="{i/4}" stop-color="{c}"/>'
                for i, c in enumerate(LEVELS)) +
      '</linearGradient>'
      '<filter id="soft" x="-40%" y="-40%" width="180%" height="180%">'
      '<feGaussianBlur stdDeviation="1.6"/></filter>'
      '</defs>')

    # scanner-room background
    A(f'<rect width="{W}" height="{H}" rx="14" fill="#05070f"/>')
    A(f'<rect width="{W}" height="{H}" rx="14" fill="none" '
      f'stroke="#1e293b" stroke-width="1.5"/>')

    # console header
    A(f'<text x="{pad_x}" y="30" font-family="ui-monospace,Menlo,Consolas,monospace" '
      f'font-size="15" letter-spacing="3" fill="#7dd3fc">CONTRIBUTION fMRI</text>')
    A(f'<circle cx="{W - pad_x - 6}" cy="26" r="5" fill="#22d3ee">'
      f'<animate attributeName="opacity" values="1;0.25;1" dur="1.8s" '
      f'repeatCount="indefinite"/></circle>')
    A(f'<text x="{W - pad_x - 18}" y="30" text-anchor="end" '
      f'font-family="ui-monospace,Menlo,Consolas,monospace" font-size="11" '
      f'fill="#475569">SCANNING</text>')

    A(f'<g transform="translate({pad_x},{pad_y})">')

    # month labels
    prev_month = None
    for c, w in enumerate(weeks):
        days = w["contributionDays"]
        if not days:
            continue
        m = datetime.date.fromisoformat(days[0]["date"]).strftime("%b")
        if m != prev_month:
            A(f'<text x="{c * PITCH}" y="-10" font-family="ui-monospace,Menlo,Consolas,monospace" '
              f'font-size="10" fill="#475569">{m}</text>')
            prev_month = m

    # voxels
    pulse_i = 0
    for (c, r), (cnt, _dt) in sorted(grid.items()):
        lv = level(cnt, mx)
        x, y = c * PITCH, r * PITCH
        A(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3" '
          f'fill="{LEVELS[lv]}">')
        if lv == 4:  # peak-activation voxels pulse
            A(f'<animate attributeName="opacity" values="1;0.45;1" dur="2.4s" '
              f'begin="{(pulse_i * 0.3) % 2.4:.1f}s" repeatCount="indefinite"/>')
            pulse_i += 1
        elif lv == 3:
            A(f'<animate attributeName="opacity" values="1;0.7;1" dur="3.2s" '
              f'begin="{(pulse_i * 0.3) % 3.2:.1f}s" repeatCount="indefinite"/>')
            pulse_i += 1
        A('</rect>')

    # peak-activation crosshair
    if peak is not None:
        pcx, pcy = peak[0] * PITCH + CELL / 2, peak[1] * PITCH + CELL / 2
        A(f'<g stroke="#22d3ee" fill="none">'
          f'<circle cx="{pcx}" cy="{pcy}" r="9" stroke-width="1.5" opacity="0.9">'
          f'<animate attributeName="r" values="9;16" dur="2s" repeatCount="indefinite"/>'
          f'<animate attributeName="opacity" values="0.9;0" dur="2s" '
          f'repeatCount="indefinite"/></circle>'
          f'<line x1="{pcx - 13}" y1="{pcy}" x2="{pcx - 6}" y2="{pcy}" stroke-width="1.5"/>'
          f'<line x1="{pcx + 6}" y1="{pcy}" x2="{pcx + 13}" y2="{pcy}" stroke-width="1.5"/>'
          f'<line x1="{pcx}" y1="{pcy - 13}" x2="{pcx}" y2="{pcy - 6}" stroke-width="1.5"/>'
          f'<line x1="{pcx}" y1="{pcy + 6}" x2="{pcx}" y2="{pcy + 13}" stroke-width="1.5"/>'
          f'</g>')

    # slice-acquisition sweep beam
    A(f'<rect x="-46" y="-6" width="40" height="{grid_h + 12}" fill="url(#beam)" '
      f'filter="url(#soft)" opacity="0.8">'
      f'<animate attributeName="x" from="-46" to="{grid_w + 6}" dur="7s" '
      f'repeatCount="indefinite"/></rect>')
    A(f'<line x1="-6" y1="-6" x2="-6" y2="{grid_h + 6}" stroke="#a5f3fc" '
      f'stroke-width="1.5" opacity="0.85">'
      f'<animate attributeName="x1" from="-6" to="{grid_w + 46}" dur="7s" '
      f'repeatCount="indefinite"/>'
      f'<animate attributeName="x2" from="-6" to="{grid_w + 46}" dur="7s" '
      f'repeatCount="indefinite"/></line>')

    A('</g>')

    # legend
    ly = H - 26
    A(f'<text x="{pad_x}" y="{ly}" font-family="ui-monospace,Menlo,Consolas,monospace" '
      f'font-size="10" fill="#475569">less</text>')
    lx = pad_x + 36
    for i, c in enumerate(LEVELS):
        A(f'<rect x="{lx + i * 16}" y="{ly - 10}" width="12" height="12" rx="3" fill="{c}"/>')
    A(f'<text x="{lx + 5 * 16 + 6}" y="{ly}" font-family="ui-monospace,Menlo,Consolas,monospace" '
      f'font-size="10" fill="#475569">more &#183; BOLD signal &#183; {total} contributions</text>')

    A('</svg>')
    return "\n".join(s)


def main():
    cal = fetch_calendar()
    svg = build(cal)
    with open(OUT, "w") as f:
        f.write(svg)
    print(f"wrote {OUT} ({len(svg)} bytes, "
          f"{cal['totalContributions']} contributions)")


if __name__ == "__main__":
    main()
