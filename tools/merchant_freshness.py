#!/usr/bin/env python3
"""Print how recently each listed place was confirmed to take bitcoin, as Markdown.

WHAT IT DOES
  Reads data/merchants.json and groups the places by their `checked` date (the OSM
  check_date:currency:XBT tag, else survey:date: the last time someone confirmed on the
  ground that the place takes bitcoin). Prints a short report and the places most
  overdue for a visit, so whoever walks the lake next knows where to go first.

  The weekly GitHub Action writes this report to the run's summary page. It changes nothing.

WHY
  "117 listed" and "about 50 active" are different numbers. Listed places stay on the map
  for years; only a fresh check says a place still takes bitcoin. A confirmed visit, added
  on BTC Map with its "Verify" button, moves a place into the fresh group here.

Run:  python tools/merchant_freshness.py
"""
import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "merchants.json"
BANDS = ((365, "in the last 12 months"), (730, "12 to 24 months ago"), (None, "more than 24 months ago"))
LIST_OLDEST = 25


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    places = data["places"]
    today = datetime.date.fromisoformat(data["data_date"])

    def age(p):
        return (today - datetime.date.fromisoformat(p["checked"])).days if p["checked"] else None

    lines = [f"## Bitcoin Lago places, data of {data['data_date']}", "",
             f"{len(places)} places listed on BTC Map. Last confirmed to take bitcoin:", ""]
    low = 0
    for limit, label in BANDS:
        n = sum(1 for p in places if age(p) is not None and age(p) >= low and (limit is None or age(p) < limit))
        lines.append(f"- {label}: {n}")
        low = limit or low
    lines.append(f"- never: {sum(1 for p in places if age(p) is None)}")

    overdue = sorted((p for p in places if age(p) is None or age(p) >= 365),
                     key=lambda p: p["checked"] or "")[:LIST_OLDEST]
    lines += ["", f"### Visit first ({len(overdue)} oldest checks)", "",
              "| Place | Town | Last check | BTC Map |", "|---|---|---|---|"]
    for p in overdue:
        kind, num = p["id"].split("/")
        lines.append(f"| {p['name'] or '(no name)'} | {p['town']} | {p['checked'] or 'never'} "
                     f"| [open](https://btcmap.org/merchant/{kind}:{num}) |")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
