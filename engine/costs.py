"""Calculator de costuri LIMITLESS, citește config/costs.json.

Folosire: python3 engine/costs.py [produse] [videouri_pe_zi_pe_produs] [reteta]
Exemplu: python3 engine/costs.py 10 5 slab_reutilizare
"""
import json, os, sys

cfg = json.load(open(os.path.join(os.path.dirname(__file__), "..", "config", "costs.json")))

def video_credits(reteta, which):
    r = cfg["retete_video"][reteta]
    return sum(n * cfg["credits"][k][which] for k, n in r.items() if not k.startswith("_"))

def main():
    produse = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    pe_zi = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    retete = [sys.argv[3]] if len(sys.argv) > 3 else list(cfg["retete_video"])
    usd, retry = cfg["usd_per_credit"], cfg["factor_reincercari"]
    print(f"{produse} produse × {pe_zi} videouri/zi = {produse * pe_zi} videouri/zi\n")
    for r in retete:
        lo = video_credits(r, "min") * retry["min"]
        hi = video_credits(r, "max") * retry["max"]
        n = produse * pe_zi
        print(f"[{r}] {cfg['retete_video'][r]['_desc']}")
        print(f"  pe video: {lo:.0f}–{hi:.0f} credite ≈ ${lo*usd['min']:.1f}–{hi*usd['max']:.1f}")
        print(f"  pe zi:    {lo*n:,.0f}–{hi*n:,.0f} credite ≈ ${lo*n*usd['min']:,.0f}–{hi*n*usd['max']:,.0f}")
        print(f"  pe lună:  ≈ ${lo*n*30*usd['min']:,.0f}–{hi*n*30*usd['max']:,.0f}\n")
    f = cfg["fix_lunar_usd"]
    fix = produse * (f["shopify_per_magazin"]["val"] + f["domeniu_per_magazin"]["val"]) + f["server_hetzner"]["val"] + f["apify_plan"]["val"]
    print(f"Fix lunar (fără ManyChat, telefoane, Claude, furnizori): ≈ ${fix:,.0f}")

if __name__ == "__main__":
    main()
