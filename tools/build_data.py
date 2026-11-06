#!/usr/bin/env python3
"""Build data/merchants.json (the trimmed, public copy of the OSM export).

WHAT IT DOES
  Reads the raw OpenStreetMap export  source-archive/data/merchants-osm-2026-10-19.json
  (117 places tagged as accepting Bitcoin, pulled on 2026-10-19; the same places BTC Map shows)
  and writes data/merchants.json with only the fields the website needs.

WHERE THE DATA COMES FROM
  OpenStreetMap contributors, licence ODbL. Credit is shown in the page footer.
  Nothing is invented here: every value is copied from the OSM tags, with three
  mechanical derivations that are documented below.

DERIVATIONS (the only things not copied 1:1)
  1. group  : the raw OSM category (restaurant, cafe, hotel ...) is folded into six
              browsing groups so the filter chips stay readable.
  2. town   : OSM has no town tag for most places, so the town is the nearest
              village centre to the place's coordinates. Approximate by design;
              the page says so.
  4. website: four dead website links are dropped (see DEAD_WEBSITES).
  3. phone  : three tuk tuk entries carry their number inside the OSM *name*
              ("Niul - Tuk Tuk 4120 0757"). The number is moved into `phone`
              and removed from the display name. Value is unchanged.

The raw export lives in source-archive/ which is NOT published (see .gitignore).
Run:  python tools/build_data.py            (the 2026-10-19 export)
      python tools/build_data.py --latest   (the newest export from tools/fetch_btcmap.py)
"""
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "source-archive" / "data" / "merchants-osm-2026-10-19.json"
if "--latest" in sys.argv:
    RAW = sorted(RAW.parent.glob("merchants-osm-*.json"))[-1]
OUT = ROOT / "data" / "merchants.json"

# Village centres (approximate lat, lon) used only to label each place with a town.
TOWNS = {
    "Panajachel": (14.7425, -91.1578),
    "Santa Catarina Palopó": (14.7230, -91.1370),
    "San Antonio Palopó": (14.6930, -91.1180),
    "San Andrés Semetabaj": (14.7430, -91.1330),
    "Santa Cruz La Laguna": (14.7390, -91.2050),
    "Jaibalito": (14.7380, -91.2190),
    "Tzununá": (14.7390, -91.2480),
    "San Marcos La Laguna": (14.7230, -91.2600),
    "San Pablo La Laguna": (14.7140, -91.2870),
    "San Juan La Laguna": (14.6960, -91.2840),
    "San Pedro La Laguna": (14.6910, -91.2720),
    "Santiago Atitlán": (14.6380, -91.2310),
}

# Website links from OSM that did not resolve when checked on 2026-10-19 (DNS failure, TLS
# hostname mismatch, or HTTP 404 on the home page). They are left out so the site never links
# to a dead page. The place itself stays in the list. Re-check with qa/check_links.py.
DEAD_WEBSITES = {
    "http://www.imagenchocolate.com/",
    "https://eaglesretreats.com/",
    "https://lax-travel-panajachel.business.site/",
    "https://www.tekoaspaces.com/",
}

# raw OSM category -> browsing group
GROUPS = {
    "eat": ["restaurant", "cafe", "fast_food", "ice_cream", "pastry", "bar"],
    "stay": ["hotel", "hostel"],
    "tours": ["travel_agency", "guide", "boat_rental", "canoe_hire", "taxi", "attraction", "parking"],
    "shops": ["gift", "clothes", "convenience", "supermarket", "shoes", "second_hand", "florist",
              "pottery", "craft", "art", "gallery", "artwork", "hardware", "electronics", "pharmacy"],
    "services": ["beauty", "hairdresser", "wellness_centre", "massage", "fitness_centre", "computer",
                 "internet_cafe", "mobile_phone", "repair", "laundry", "copyshop", "electrician",
                 "motorcycle", "school"],
}
CAT2GROUP = {c: g for g, cats in GROUPS.items() for c in cats}


def nearest_town(lat, lon):
    def dist(c):
        return math.hypot(lat - c[0], (lon - c[1]) * math.cos(math.radians(lat)))
    return min(TOWNS, key=lambda t: dist(TOWNS[t]))


def clean(v):
    return v if v not in ("", None) else None


def main():
    raw = json.loads(RAW.read_text(encoding="utf-8"))
    out = []
    for r in raw:
        tags = r.get("tags", {})
        name = r.get("name")
        phone = clean(r.get("phone"))
        # derivation 3: number embedded in the name of tuk tuk entries
        m = re.match(r"^(.*?)\s+((?:\+?\d[\d\- ]{6,}))$", name or "")
        if m:
            name = m.group(1).strip()
            phone = phone or m.group(2).strip()
        cat = r.get("cat")
        out.append({
            "id": r["osm"],
            "name": name,
            "category": cat,
            "group": CAT2GROUP.get(cat, "other"),
            "town": nearest_town(r["lat"], r["lon"]),
            "lat": round(r["lat"], 6),
            "lon": round(r["lon"], 6),
            "phone": phone,
            "website": None if r.get("website") in DEAD_WEBSITES else clean(r.get("website")),
            "facebook": clean(r.get("facebook")),
            "instagram": clean(r.get("instagram")),
            "hours": clean(r.get("hours")),
            "survey": clean(tags.get("survey:date")),
            "checked": clean(r.get("check")),
            "lightning": r.get("ln"),
            "onchain": r.get("onchain"),
            "operator": clean(tags.get("operator")),
        })
    payload = {
        "source": "OpenStreetMap contributors (ODbL), as shown on BTC Map",
        "licence": "https://www.openstreetmap.org/copyright",
        "data_date": RAW.stem.removeprefix("merchants-osm-"),
        "count": len(out),
        "places": out,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", OUT, len(out), "places")


if __name__ == "__main__":
    main()
