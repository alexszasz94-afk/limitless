"""LIMITLESS — motorul: produse, virale, producție, buget, panou de control.

Starea stă în state/*.json (în repo, ca să o vadă orice sesiune). Comenzi:
  produs-nou   --nume N [--link L] [--categorie C]
  evalueaza    ID [--pret P] [--concurenti N] [--usd1m U] [--marja 0.6] [--usor 0-10] [--ok 1,2,...] [--nu 3,...]
  viral-nou    --url U --views V --ore H [--produs ID] [--cont C] [--platforma P]
  planifica    [--reteta full_genjutsu]
  stadiu       VIRAL_ID STADIU
  status
  dashboard    (scrie dashboard/index.html)
  demo         (încarcă date de EXEMPLU, marcate ca atare)
"""
import argparse, datetime as dt, html, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
STATE = os.path.join(ROOT, "state")
sys.path.insert(0, os.path.dirname(__file__))

CRITERII = {  # docs/09-reguli-produs.md §1
    1: "Dovadă de cerere (≥100k/24 h sau reclame care rulează)",
    2: "≤ 4 concurenți organici activi",
    3: "Preț ≥ 38,99 $",
    4: "≥ 2.000 $ la 1M vizualizări (test order)",
    5: "Public american cu bani (25+)",
    6: "Se înțelege în 1–3 s cum funcționează",
    7: "Îl putem face mai bine decât concurenții",
    8: "Iese fidel cu uneltele noastre",
    9: "Livrare sigură în SUA, risc mic de chargeback",
    10: "Se potrivește sezonului / evergreen",
}
STADII = ["găsit", "analizat", "planificat", "produs", "verificat", "montat", "postat", "măsurat"]
PRAG_DOVEDIT = 100_000  # vizualizări în ~24 h (docs/08)


def load(name, default):
    p = os.path.join(STATE, name + ".json")
    return json.load(open(p)) if os.path.exists(p) else default


def save(name, data):
    os.makedirs(STATE, exist_ok=True)
    with open(os.path.join(STATE, name + ".json"), "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def cfg(name):
    return json.load(open(os.path.join(ROOT, "config", name + ".json")))


def now():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M")


def next_id(items, prefix):
    return f"{prefix}{max([int(i['id'][len(prefix):]) for i in items] + [0]) + 1}"


# ---------- scor produs (docs/09 §3) ----------
def scor(p):
    m = p.get("metrici", {})
    c = p.get("criterii", {})
    if any(v is False for v in c.values()):
        return 0, "picat"
    usd = min((m.get("usd1m") or 0) / 10000, 1)
    viteza = min((p.get("viteza_max") or 0) / 300000, 1)
    conc = m.get("concurenti")
    conc_s = 0 if conc is None else max(0, 1 - conc / 5)
    marja = min((m.get("marja") or 0) / 0.7, 1)
    usor = (m.get("usor") or 0) / 10
    s = round(100 * (0.40 * usd + 0.20 * viteza + 0.15 * conc_s + 0.15 * marja + 0.10 * usor))
    complet = len([v for v in c.values() if v is True]) == len(CRITERII)
    return s, ("trece" if complet else "în evaluare")


def viteza(v):
    return round(v["views"] / max(v["ore"], 1) * 24)


# ---------- cost (config/costs.json) ----------
def cost_reteta(reteta):
    c = cfg("costs")
    r = c["retete_video"][reteta]
    typ = sum(n * c["credits"][k]["typ"] for k, n in r.items() if not k.startswith("_"))
    return round(typ * c["factor_reincercari"]["min"])


# ---------- comenzi ----------
def cmd_produs_nou(a):
    ps = load("products", [])
    p = {"id": next_id(ps, "P"), "nume": a.nume, "link": a.link, "categorie": a.categorie,
         "status": "candidat", "criterii": {}, "metrici": {}, "viteza_max": 0, "adaugat": now()}
    ps.append(p); save("products", ps); print("adăugat", p["id"], p["nume"])


def cmd_evalueaza(a):
    ps = load("products", [])
    p = next(x for x in ps if x["id"] == a.id)
    m = p["metrici"]
    for k in ("pret", "concurenti", "usd1m", "marja", "usor"):
        v = getattr(a, k)
        if v is not None:
            m[k] = v
    for lst, val in ((a.ok, True), (a.nu, False)):
        for n in filter(None, (lst or "").split(",")):
            p["criterii"][n.strip()] = val
    if m.get("pret") is not None:
        p["criterii"]["3"] = m["pret"] >= 38.99
    if m.get("concurenti") is not None:
        p["criterii"]["2"] = m["concurenti"] <= 4
    if m.get("usd1m") is not None:
        p["criterii"]["4"] = m["usd1m"] >= 2000
    s, verdict = scor(p)
    p["scor"], p["verdict"] = s, verdict
    if verdict == "picat":
        p["status"] = "respins"
    save("products", ps); print(p["id"], "scor", s, verdict)


def cmd_viral_nou(a):
    vs = load("virals", [])
    v = {"id": next_id(vs, "V"), "url": a.url, "platforma": a.platforma, "cont": a.cont,
         "produs": a.produs, "views": a.views, "ore": a.ore, "stadiu": "găsit", "adaugat": now()}
    v["viteza24h"] = viteza(v)
    v["dovedit"] = v["viteza24h"] >= PRAG_DOVEDIT
    vs.append(v); save("virals", vs)
    if a.produs:
        ps = load("products", [])
        for p in ps:
            if p["id"] == a.produs:
                p["viteza_max"] = max(p.get("viteza_max", 0), v["viteza24h"])
                p["scor"], p["verdict"] = scor(p)
        save("products", ps)
    print(v["id"], f"{v['viteza24h']:,}/24h", "DOVEDIT" if v["dovedit"] else "sub prag")


def cmd_planifica(a):
    vs, b = load("virals", []), cfg("budget")
    azi = dt.date.today().isoformat()
    folosit = sum(v.get("credite_est", 0) for v in vs if v.get("planificat_la", "")[:10] == azi)
    cand = sorted([v for v in vs if v["dovedit"] and v["stadiu"] in ("găsit", "analizat")],
                  key=lambda v: -v["viteza24h"])
    est = cost_reteta(a.reteta)
    for v in cand:
        if est > b["max_credits_per_video"]:
            print("rețeta depășește plafonul per video"); break
        if folosit + est > b["credits_per_day"]:
            print("buget zilnic atins, restul rămân în coadă"); break
        v.update(stadiu="planificat", reteta=a.reteta, credite_est=est, planificat_la=now())
        folosit += est
        print("planificat", v["id"], a.reteta, est, "credite")
    save("virals", vs)


def cmd_stadiu(a):
    vs = load("virals", [])
    assert a.stadiu in STADII, f"stadiu necunoscut; folosește: {', '.join(STADII)}"
    for v in vs:
        if v["id"] == a.id:
            v["stadiu"] = a.stadiu
    save("virals", vs)


def cmd_status(a):
    ps, vs = load("products", []), load("virals", [])
    print("PRODUSE")
    for p in sorted(ps, key=lambda p: -(p.get("scor") or 0)):
        print(f"  {p['id']:4} {p['nume'][:40]:40} scor {p.get('scor', '-'):>3}  {p.get('verdict', p['status'])}")
    print("VIRALE")
    for s in STADII:
        n = len([v for v in vs if v["stadiu"] == s])
        if n:
            print(f"  {s:11} {n}")


def cmd_demo(a):
    ps = [
        {"id": "P1", "nume": "Halat încălzit cu glugă", "categorie": "îmbrăcăminte cozy", "status": "test",
         "metrici": {"pret": 59.99, "concurenti": 3, "usd1m": 5500, "marja": 0.62, "usor": 8},
         "criterii": {str(i): True for i in range(1, 11)}, "viteza_max": 240000},
        {"id": "P2", "nume": "Lampă LED cu proiecție de zăpadă", "categorie": "decor sărbători", "status": "candidat",
         "metrici": {"pret": 44.99, "concurenti": 2, "usd1m": 3100, "marja": 0.58, "usor": 7},
         "criterii": {**{str(i): True for i in range(1, 8)}}, "viteza_max": 130000},
        {"id": "P3", "nume": "Pernă de masaj pentru gât", "categorie": "wellness", "status": "respins",
         "metrici": {"pret": 29.99, "concurenti": 9, "usd1m": 1400, "marja": 0.55, "usor": 6},
         "criterii": {"2": False, "3": False, "4": False}, "viteza_max": 60000},
    ]
    for p in ps:
        p["scor"], p["verdict"] = scor(p); p["adaugat"] = now(); p["link"] = None
    vs = []
    for i, (cont, views, ore, prod, st) in enumerate([
        ("@cozy.example", 310000, 20, "P1", "planificat"), ("@snug.example", 180000, 22, "P1", "produs"),
        ("@warm.example", 95000, 30, "P1", "găsit"), ("@glow.example", 140000, 18, "P2", "analizat"),
        ("@home.example", 260000, 26, "P1", "montat"), ("@decor.example", 70000, 24, "P2", "găsit")], 1):
        v = {"id": f"V{i}", "url": f"https://www.instagram.com/reel/EXEMPLU{i}/", "platforma": "instagram",
             "cont": cont, "produs": prod, "views": views, "ore": ore, "stadiu": st, "adaugat": now()}
        v["viteza24h"] = viteza(v); v["dovedit"] = v["viteza24h"] >= PRAG_DOVEDIT
        if st != "găsit" and v["dovedit"]:
            v.update(reteta="full_genjutsu", credite_est=cost_reteta("full_genjutsu"), planificat_la=now())
        vs.append(v)
    save("products", ps); save("virals", vs); save("meta", {"demo": True, "actualizat": now()})
    print("date de EXEMPLU încărcate")


def cmd_dashboard(a):
    print("Panoul e acum platforma live (dashboard/index.html + baza de date a artifactului); vezi CLAUDE.md.")


def main():
    ap = argparse.ArgumentParser(description="LIMITLESS")
    sp = ap.add_subparsers(dest="cmd", required=True)
    x = sp.add_parser("produs-nou"); x.add_argument("--nume", required=True); x.add_argument("--link"); x.add_argument("--categorie")
    x = sp.add_parser("evalueaza"); x.add_argument("id")
    for k, t in (("pret", float), ("concurenti", int), ("usd1m", float), ("marja", float), ("usor", float)):
        x.add_argument("--" + k, type=t)
    x.add_argument("--ok"); x.add_argument("--nu")
    x = sp.add_parser("viral-nou"); x.add_argument("--url", required=True); x.add_argument("--views", type=int, required=True)
    x.add_argument("--ore", type=float, required=True); x.add_argument("--produs"); x.add_argument("--cont"); x.add_argument("--platforma", default="instagram")
    x = sp.add_parser("planifica"); x.add_argument("--reteta", default="full_genjutsu")
    x = sp.add_parser("stadiu"); x.add_argument("id"); x.add_argument("stadiu")
    for n in ("status", "dashboard", "demo"):
        sp.add_parser(n)
    a = ap.parse_args()
    globals()["cmd_" + a.cmd.replace("-", "_")](a)


if __name__ == "__main__":
    main()
