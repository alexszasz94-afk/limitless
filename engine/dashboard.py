"""Construiește panoul LIMITLESS (dashboard/index.html) din starea motorului. Pagina e statică, fără scripturi."""
import html

E = html.escape

CSS = """
/* Layout: o coloană de lucru, rezumatul sus, apoi fluxul, produsele, coada și prețurile. */
:root{
  --bg:#eef1f3; --panel:#ffffff; --ink:#15212b; --muted:#5b6873; --line:#d6dde2;
  --accent:#0b6e88; --accent-soft:#d8ecf1;
  --ok:#1f7a4a; --ok-soft:#dcefe4; --warn:#9a6200; --warn-soft:#f6ead2; --bad:#a3322a; --bad-soft:#f5dfdc;
  --f-display:"Archivo",system-ui,sans-serif; --f-body:"IBM Plex Sans",system-ui,sans-serif; --f-data:"IBM Plex Mono",ui-monospace,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#0f1519; --panel:#172027; --ink:#e3eaee; --muted:#93a2ad; --line:#26333c;
  --accent:#4fb7d1; --accent-soft:#143440;
  --ok:#5cc38a; --ok-soft:#173326; --warn:#e0a640; --warn-soft:#3a2c12; --bad:#ec7a70; --bad-soft:#3c1d1a; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#0f1519; --panel:#172027; --ink:#e3eaee; --muted:#93a2ad; --line:#26333c;
  --accent:#4fb7d1; --accent-soft:#143440;
  --ok:#5cc38a; --ok-soft:#173326; --warn:#e0a640; --warn-soft:#3a2c12; --bad:#ec7a70; --bad-soft:#3c1d1a; color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--f-body);font-size:15px;line-height:1.5;padding-inline:16px;padding-block:20px 48px}
.wrap{max-width:1080px;margin:0 auto;display:flex;flex-direction:column;gap:28px}
header{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:8px 20px}
.mark{font-family:var(--f-display);font-weight:800;font-size:clamp(28px,5vw,40px);letter-spacing:.14em;margin:0}
.mark span{color:var(--accent)}
.sub{color:var(--muted);font-family:var(--f-data);font-size:12.5px}
.demo{background:var(--warn-soft);color:var(--warn);border:1px solid var(--warn);border-radius:6px;padding:10px 14px;font-size:14px}
h2{font-family:var(--f-display);font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 10px;font-weight:700}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}
.kpi{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:14px 16px;display:flex;flex-direction:column;gap:4px}
.kpi b{font-family:var(--f-data);font-size:26px;font-weight:600;font-variant-numeric:tabular-nums}
.kpi small{color:var(--muted);font-size:13px}
.meter{height:8px;border-radius:4px;background:var(--line);overflow:hidden;margin-top:6px}
.meter i{display:block;height:100%;background:var(--accent)}
.flow{display:grid;grid-template-columns:repeat(8,minmax(0,1fr));gap:6px}
.stage{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:10px 8px;text-align:center;min-width:0}
.stage b{display:block;font-family:var(--f-data);font-size:22px;font-variant-numeric:tabular-nums}
.stage span{font-size:12px;color:var(--muted);overflow-wrap:anywhere}
.stage.on{border-color:var(--accent);background:var(--accent-soft)}
@media (max-width:640px){.flow{grid-template-columns:repeat(4,minmax(0,1fr))}}
.prods{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px}
.prod{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:16px;display:flex;flex-direction:column;gap:10px;min-width:0}
.prod h3{margin:0;font-family:var(--f-display);font-size:18px;text-wrap:balance}
.row{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;font-size:13px;color:var(--muted)}
.row b{color:var(--ink);font-family:var(--f-data);font-weight:500}
.score{display:flex;align-items:center;gap:10px}
.score .meter{flex:1;margin:0}
.score b{font-family:var(--f-data);font-size:20px;min-width:2.5ch;text-align:right}
.chip{display:inline-block;font-size:12px;font-weight:600;padding:2px 9px;border-radius:999px;white-space:nowrap}
.c-ok{background:var(--ok-soft);color:var(--ok)} .c-warn{background:var(--warn-soft);color:var(--warn)}
.c-bad{background:var(--bad-soft);color:var(--bad)} .c-acc{background:var(--accent-soft);color:var(--accent)}
.crit{display:grid;grid-template-columns:repeat(10,1fr);gap:4px}
.crit i{height:22px;border-radius:4px;display:flex;align-items:center;justify-content:center;font-style:normal;font-family:var(--f-data);font-size:11px;border:1px solid var(--line);color:var(--muted)}
.crit i.y{background:var(--ok-soft);color:var(--ok);border-color:transparent}
.crit i.n{background:var(--bad-soft);color:var(--bad);border-color:transparent}
.tbl{overflow-x:auto;background:var(--panel);border:1px solid var(--line);border-radius:8px}
table{width:100%;border-collapse:collapse;font-size:14px}
th,td{padding:10px 12px;text-align:left;border-bottom:1px solid var(--line);white-space:nowrap}
th{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:600}
td.n{font-family:var(--f-data);font-variant-numeric:tabular-nums;text-align:right}
tr:last-child td{border-bottom:0}
a{color:var(--accent)}
.legend{font-size:12.5px;color:var(--muted);margin-top:8px}
.cmds{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:10px}
.cmd{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:12px 14px;min-width:0}
.cmd code{font-family:var(--f-data);font-size:13.5px;color:var(--accent);font-weight:600}
.cmd p{margin:4px 0 0;font-size:13.5px;color:var(--muted)}
"""

def chip(text, kind):
    return f'<span class="chip c-{kind}">{E(text)}</span>'

def build(out, products, virals, meta, costs, budget, criterii, stadii, cost_reteta):
    pmap = {p["id"]: p for p in products}
    azi_plan = sum(v.get("credite_est", 0) for v in virals if v.get("stadiu") == "planificat")
    lim = budget["credits_per_day"]
    pct = min(100, round(100 * azi_plan / lim)) if lim else 0
    dovedite = [v for v in virals if v.get("dovedit")]
    in_lucru = [v for v in virals if v["stadiu"] in ("planificat", "produs", "verificat", "montat")]
    est = cost_reteta("full_genjutsu")
    usd = costs["usd_per_credit"]

    kpis = f"""
<section class="kpis" aria-label="Rezumat">
  <div class="kpi"><small>Produse urmărite</small><b>{len(products)}</b><small>{len([p for p in products if p.get('verdict')=='trece'])} trec toate cele 10 condiții</small></div>
  <div class="kpi"><small>Virale dovedite (≥100k/24 h)</small><b>{len(dovedite)}</b><small>din {len(virals)} găsite</small></div>
  <div class="kpi"><small>Videouri în lucru</small><b>{len(in_lucru)}</b><small>planificate → montate</small></div>
  <div class="kpi"><small>Credite planificate azi</small><b>{azi_plan:,} / {lim:,}</b><div class="meter" role="img" aria-label="{pct}% din bugetul zilnic"><i style="width:{pct}%"></i></div></div>
  <div class="kpi"><small>Cost estimat pe video (full Genjutsu)</small><b>~{est}</b><small>credite ≈ ${est*usd['min']:.0f}–{est*usd['max']:.0f}</small></div>
</section>"""

    flow = "".join(
        f'<div class="stage{" on" if any(v["stadiu"]==s for v in virals) else ""}"><b>{len([v for v in virals if v["stadiu"]==s])}</b><span>{E(s)}</span></div>'
        for s in stadii)

    cards = []
    for p in sorted(products, key=lambda p: -(p.get("scor") or 0)):
        m, c = p.get("metrici", {}), p.get("criterii", {})
        verdict = p.get("verdict", "în evaluare")
        kind = {"trece": "ok", "picat": "bad"}.get(verdict, "warn")
        dots = "".join(
            f'<i class="{"y" if c.get(str(i)) is True else "n" if c.get(str(i)) is False else ""}" title="{i}. {E(criterii[i])}">{i}</i>'
            for i in criterii)
        s = p.get("scor") or 0
        cards.append(f"""
<article class="prod">
  <div class="row" style="justify-content:space-between"><span>{E(p.get('categorie') or 'fără categorie')}</span>{chip(verdict, kind)}</div>
  <h3>{E(p['nume'])}</h3>
  <div class="score"><div class="meter" role="img" aria-label="scor {s} din 100"><i style="width:{s}%"></i></div><b>{s}</b></div>
  <div class="crit" aria-label="Cele 10 condiții">{dots}</div>
  <div class="row"><span>Preț <b>{'$'+format(m['pret'],'.2f') if m.get('pret') else '–'}</b></span><span>$/1M <b>{format(int(m['usd1m']),',') if m.get('usd1m') else '–'}</b></span><span>Concurenți <b>{m.get('concurenti','–')}</b></span><span>Viral max <b>{format(p.get('viteza_max',0),',')}/24h</b></span></div>
</article>""")

    rows = []
    for v in sorted(virals, key=lambda v: (stadii.index(v["stadiu"]), -v["viteza24h"])):
        p = pmap.get(v.get("produs"), {})
        rows.append(f"""<tr><td><a href="{E(v['url'])}">{E(v.get('cont') or v['url'])}</a></td><td>{E(p.get('nume','–'))}</td>
<td class="n">{v['viteza24h']:,}</td><td>{chip('dovedit','ok') if v['dovedit'] else chip('sub prag','warn')}</td>
<td>{chip(v['stadiu'],'acc')}</td><td>{E(v.get('reteta') or '–')}</td><td class="n">{v.get('credite_est') or '–'}</td></tr>""")

    cr = costs["credits"]
    price_rows = "".join(
        f'<tr><td>{E(k.replace("_"," "))}</td><td class="n">{v["min"]:g}–{v["max"]:g}</td><td style="white-space:normal;min-width:240px">{E(v["sursa"])}</td></tr>'
        for k, v in cr.items())

    cmds = [
        ("produs nou <link>", "Fac fișa produsului și îl trec prin cele 10 condiții."),
        ("evaluează P1", "Completez prețul, concurenții, $/1M (test order) și recalculez scorul."),
        ("viral <link> <views> <ore>", "Calculez viteza; peste 100k/24 h intră direct în coadă."),
        ("planifică", "Aleg viralele dovedite, rețeta cea mai ieftină și le programez în bugetul zilei."),
        ("status", "Îți spun unde e fiecare produs și fiecare video."),
        ("regula: …", "O trec datată în reguli și se aplică la tot ce urmează."),
    ]
    cmd_html = "".join(f'<div class="cmd"><code>{E(a)}</code><p>{E(b)}</p></div>' for a, b in cmds)

    demo = '<div class="demo" role="note"><b>Date de exemplu.</b> Produsele și viralele de mai jos sunt inventate ca să vezi cum arată panoul. Dispar la primul produs real.</div>' if meta.get("demo") else ""

    page = f"""<title>LIMITLESS Control</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800&family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;600&display=swap">
<style>{CSS}</style>
<div class="wrap">
<header><h1 class="mark">LIMIT<span>LESS</span></h1><span class="sub">actualizat {E(meta.get('actualizat',''))} UTC · țintă 5.000.000 $ · unelte: Genjutsu motion control, Seedance 2.5, GPT Image 2.5</span></header>
{demo}
{kpis}
<section><h2>Fluxul fiecărui video</h2><div class="flow">{flow}</div></section>
<section><h2>Produse</h2><div class="prods">{''.join(cards) or '<p>Niciun produs încă. Spune „produs nou” cu linkul lui.</p>'}</div>
<p class="legend">Pătratele 1–10 sunt condițiile din docs/09: verde = trece, roșu = pică, gol = de verificat. Un singur roșu oprește produsul.</p></section>
<section><h2>Coada de virale</h2><div class="tbl"><table><thead><tr><th>Cont</th><th>Produs</th><th style="text-align:right">Vizualizări / 24 h</th><th>Semnal</th><th>Stadiu</th><th>Rețetă</th><th style="text-align:right">Credite</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div></section>
<section><h2>Prețuri Higgsfield (măsurate)</h2><div class="tbl"><table><thead><tr><th>Unealtă</th><th style="text-align:right">Credite</th><th>Detalii</th></tr></thead><tbody>{price_rows}</tbody></table></div>
<p class="legend">1 credit ≈ ${usd['min']}–{usd['max']} (de confirmat cu prețul planului tău).</p></section>
<section><h2>Ce îmi spui ca să lucrez</h2><div class="cmds">{cmd_html}</div></section>
</div>"""
    with open(out, "w") as f:
        f.write(page)
