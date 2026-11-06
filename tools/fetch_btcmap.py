#!/usr/bin/env python3
"""Fetch a fresh OpenStreetMap export of the places BTC Map shows for Lago Bitcoin.

WHAT IT DOES
  1. Reads the Lago Bitcoin community area from the BTC Map API (its outline around the lake).
  2. Asks BTC Map for every place near the lake and keeps the ones inside that outline,
     which is the same list https://btcmap.org/community/lago-bitcoin/merchants shows.
  3. Reads each place's full tags from the OpenStreetMap API (a few batched requests).
  4. Writes source-archive/data/merchants-osm-<today>.json in the same shape as the
     2026-10-19 export, so tools/build_data.py turns it into data/merchants.json unchanged.

WHERE THE DATA COMES FROM
  OpenStreetMap contributors, licence ODbL, as shown on BTC Map. Nothing is invented:
  every value is an OSM tag, except lat/lon, which is BTC Map's point for the place
  (for a building outline, its centre).

SAFETY
  If the fetch returns far fewer places than data/merchants.json already has (under 80%),
  it stops without writing anything. A half-failed API call should never shrink the map.

Run:  python tools/fetch_btcmap.py        then  python tools/build_data.py --latest
No API keys. Standard library only, so it runs the same on a laptop and in GitHub Actions.
"""
import datetime
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "source-archive" / "data"
CURRENT = ROOT / "data" / "merchants.json"

AREA_URL = "https://api.btcmap.org/v3/areas/lago-bitcoin"
# The search radius only has to cover the whole area outline; the outline does the real filtering.
SEARCH_URL = "https://api.btcmap.org/v4/places/search/?lat=14.71&lon=-91.19&radius_km=25"
OSM_URL = "https://api.openstreetmap.org/api/0.6/{kind}.json?{kind}={ids}"
UA = "bitcoin-lago-site/1.0 (+https://github.com/itstomekk/bitcoin-lago)"
MIN_SHARE = 0.8
# Same order the 2026-10-19 export used to pick a place's category.
CAT_KEYS = ("amenity", "shop", "tourism", "craft", "office", "leisure", "healthcare")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def inside(lon, lat, ring):
    """Ray casting point-in-polygon on the area's outer ring."""
    hit = False
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i]
        xj, yj = ring[j]
        if (yi > lat) != (yj > lat) and lon < (xj - xi) * (lat - yi) / (yj - yi) + xi:
            hit = not hit
        j = i
    return hit


def osm_tags(ids):
    """{'node/123': {...tags}} for every id, in batches the OSM API accepts."""
    tags = {}
    for kind in ("node", "way"):
        nums = [i.split("/")[1] for i in ids if i.startswith(kind + "/")]
        for k in range(0, len(nums), 100):
            batch = ",".join(nums[k:k + 100])
            for el in get(OSM_URL.format(kind=kind + "s", ids=batch))["elements"]:
                tags[f"{kind}/{el['id']}"] = el.get("tags", {})
    return tags


def first(tags, *keys):
    for k in keys:
        if tags.get(k):
            return tags[k]
    return None


def main():
    geo = get(AREA_URL)["tags"]["geo_json"]
    ring = geo["coordinates"][0] if geo["type"] == "Polygon" else geo["coordinates"][0][0]
    places = [p for p in get(SEARCH_URL) if p.get("osm_id") and inside(p["lon"], p["lat"], ring)]

    if CURRENT.exists():
        before = json.loads(CURRENT.read_text(encoding="utf-8"))["count"]
        if len(places) < before * MIN_SHARE:
            sys.exit(f"stopped: BTC Map returned {len(places)} places, data/merchants.json has {before}. Nothing written.")

    ids = [p["osm_id"].replace(":", "/") for p in places]
    tags = osm_tags(ids)
    missing = [i for i in ids if i not in tags]
    if missing:
        sys.exit(f"stopped: OpenStreetMap did not return {len(missing)} places ({', '.join(missing[:5])}). Nothing written.")

    raw = []
    # Nodes, then ways, each by OSM number: the order of the 2026-10-19 export, so diffs stay small.
    for p, osm in sorted(zip(places, ids), key=lambda x: (x[1].split("/")[0], int(x[1].split("/")[1]))):
        t = tags[osm]
        raw.append({
            "osm": osm,
            "name": t.get("name"),
            "lat": p["lat"],
            "lon": p["lon"],
            "cat": first(t, *CAT_KEYS),
            "phone": first(t, "phone", "contact:phone"),
            "website": first(t, "website", "contact:website"),
            "facebook": first(t, "contact:facebook", "facebook"),
            "instagram": first(t, "contact:instagram", "instagram"),
            "hours": t.get("opening_hours"),
            # Bitcoin-specific check first, then the survey date. A plain check_date only says the
            # place still exists, not that it still takes bitcoin, so the 2026-10-19 export skipped it.
            "check": first(t, "check_date:currency:XBT", "survey:date"),
            "ln": t.get("payment:lightning"),
            "onchain": t.get("payment:onchain"),
            "tags": t,
        })

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"merchants-osm-{datetime.date.today().isoformat()}.json"
    out.write_text(json.dumps(raw, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", out, len(raw), "places")


if __name__ == "__main__":
    main()
