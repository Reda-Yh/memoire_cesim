#!/usr/bin/env python3
"""
Calculateur Officiel du Barème 15 Critères d'Eric Astien (180 points max)
Session : ESYBIA2AS (Univers 1) — Bordeaux INP Cesim Global Challenge
Usage :
    python memoire_agent_cesim/calculateur_classement_astien.py "manuels/Results for Univers 1, Tour 2.html"
"""
import sys
import os
import re
from html.parser import HTMLParser


class CesimTableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_td = False
        self.in_tr = False
        self.in_h = False
        self.cur_cell = []
        self.cur_row = []
        self.lines = []

    def handle_starttag(self, tag, attrs):
        if tag in ("h1", "h2", "h3", "h4", "caption"):
            self.in_h = True
            self.cur_cell = []
        elif tag == "tr":
            self.in_tr = True
            self.cur_row = []
        elif tag in ("td", "th"):
            self.in_td = True
            self.cur_cell = []

    def handle_endtag(self, tag):
        if tag in ("h1", "h2", "h3", "h4", "caption") and self.in_h:
            self.in_h = False
            txt = " ".join("".join(self.cur_cell).split())
            if txt:
                self.lines.append(txt)
        elif tag in ("td", "th") and self.in_td:
            self.in_td = False
            txt = " ".join("".join(self.cur_cell).split())
            self.cur_row.append(txt)
        elif tag == "tr" and self.in_tr:
            self.in_tr = False
            if any(self.cur_row):
                self.lines.append(" | ".join(self.cur_row))

    def handle_data(self, data):
        if self.in_td or self.in_h:
            self.cur_cell.append(data)


def to_float(s: str) -> float:
    if not s:
        return 0.0
    s = (
        s.replace(" ", "")
        .replace("\xa0", "")
        .replace("\u202f", "")
        .replace(",", ".")
        .replace("%", "")
    )
    try:
        return float(s)
    except ValueError:
        return 0.0


def score_higher_better(vals: list[float]) -> list[int]:
    return [1 + sum(1 for j in range(12) if vals[j] < vals[i] - 1e-9) for i in range(12)]


def score_lower_better(vals: list[float]) -> list[int]:
    return [1 + sum(1 for j in range(12) if vals[j] > vals[i] + 1e-9) for i in range(12)]


def main():
    target = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "manuels/Results for Univers 1, Tour 2.html"
    )
    if not os.path.exists(target):
        print(f"Fichier introuvable : {target}")
        sys.exit(1)

    if target.endswith(".html") or target.endswith(".htm"):
        with open(target, "r", encoding="utf-8", errors="ignore") as f:
            p = CesimTableParser()
            p.feed(f.read())
            lines = p.lines
    else:
        with open(target, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()

    def parse_row(line: str) -> list[float]:
        parts = [p.strip() for p in line.split("|")]
        vals = [to_float(x) for x in parts[1:13]]
        while len(vals) < 12:
            vals.append(0.0)
        return vals[:12]

    def find_nth_row(prefix: str, n: int = 1) -> list[float]:
        count = 0
        for line in lines:
            if "|" in line:
                label = line.split("|")[0].strip()
                if label == prefix or label.startswith(prefix):
                    count += 1
                    if count == n:
                        return parse_row(line)
        return [0.0] * 12

    def find_all_rows(prefix: str) -> list[list[float]]:
        res = []
        for line in lines:
            if "|" in line:
                label = line.split("|")[0].strip()
                if label == prefix or label.startswith(prefix):
                    res.append(parse_row(line))
        return res

    teams = [
        "Ren'Auto",
        "AURA",
        "IronHorse (Bleu)",
        "YANAUTO",
        "tomobil",
        "GT-Auto VI",
        "Vrooom (Rose)",
        "POLRAMOS",
        "Ça Roule",
        "BM2P",
        "TABCHOUR (Marron)",
        "MO'THOR",
    ]

    roe = find_nth_row("Rentabilité des fonds propres (ROE)", 1)
    val_crea = find_nth_row("Création de valeur totale", 1)
    indep = find_nth_row("Ratio des fonds propres", 1)
    net_income = find_nth_row("Résultat net annuel", 1)
    decouvert = find_nth_row("Dettes à court terme (imprévues)", 1)

    # EBIT: 1=Global, 2=USA, 3=Chine, 4=Europe
    ebit_us = find_nth_row("RÉSULTAT OPÉRATIONNEL (EBIT)", 2)
    ebit_cn = find_nth_row("RÉSULTAT OPÉRATIONNEL (EBIT)", 3)
    ebit_eu = find_nth_row("RÉSULTAT OPÉRATIONNEL (EBIT)", 4)

    # CA total: 1=USA, 2=Chine; Europe is the 2nd non-empty "Chiffre d'affaires" row (1st is Global, 2nd is Europe)
    ca_us = find_nth_row("Chiffre d'affaires total", 1)
    ca_cn = find_nth_row("Chiffre d'affaires total", 2)
    non_empty_ca = [
        parse_row(l)
        for l in lines
        if "|" in l and l.split("|")[0].strip() == "Chiffre d'affaires" and any(parse_row(l))
    ]
    ca_eu = non_empty_ca[1] if len(non_empty_ca) > 1 else [0.0] * 12

    marge_us = [ebit_us[i] / ca_us[i] * 100.0 if ca_us[i] else 0.0 for i in range(12)]
    marge_cn = [ebit_cn[i] / ca_cn[i] * 100.0 if ca_cn[i] else 0.0 for i in range(12)]
    marge_eu = [ebit_eu[i] / ca_eu[i] * 100.0 if ca_eu[i] else 0.0 for i in range(12)]

    # Parts de marché
    pdm_glob, pdm_us, pdm_cn, pdm_eu = [0.0] * 12, [0.0] * 12, [0.0] * 12, [0.0] * 12
    for idx, line in enumerate(lines):
        if "Parts de marché global, %" in line:
            for sub in lines[idx : idx + 8]:
                if sub.split("|")[0].strip() == "Total":
                    pdm_glob = parse_row(sub)
                    break
        elif "USA parts de marché, %" in line:
            for sub in lines[idx : idx + 8]:
                if sub.split("|")[0].strip() == "Total":
                    pdm_us = parse_row(sub)
                    break
        elif "Chine parts de marché, %" in line:
            for sub in lines[idx : idx + 8]:
                if sub.split("|")[0].strip() == "Total":
                    pdm_cn = parse_row(sub)
                    break
        elif "Europe parts de marché, %" in line:
            for sub in lines[idx : idx + 8]:
                if sub.split("|")[0].strip() == "Total":
                    pdm_eu = parse_row(sub)
                    break

    # Demande insatisfaite
    dem_insat = [0.0] * 12
    for r in find_all_rows("Demande insatisfaite"):
        for i in range(12):
            dem_insat[i] += r[i]

    # Stocks en volume (uniquement les 6 lignes USA + Chine sous "Stocks, k unités")
    stocks_vol = [0.0] * 12
    for idx, line in enumerate(lines):
        if "Stocks, k unités" in line or "Stocks, milliers d'unités" in line:
            for sub in lines[idx + 1 : idx + 11]:
                lbl = sub.split("|")[0].strip()
                if lbl in ("Thermique", "Hybride", "Électrique", "Hydrogène"):
                    r = parse_row(sub)
                    for i in range(12):
                        stocks_vol[i] += r[i]
            break

    # Coûts moyens unitaires pondérés (1=USA, 2=Chine, 3=Europe)
    moy_pond = find_all_rows("Moyenne pondérée")
    cost_us = moy_pond[0] if len(moy_pond) > 0 else [0.0] * 12
    cost_cn = moy_pond[1] if len(moy_pond) > 1 else [0.0] * 12
    cost_eu = moy_pond[2] if len(moy_pond) > 2 else [0.0] * 12

    prod_eng = find_nth_row("Coefficient de productivité", 1)

    criteria = [
        ("1. ROE (%)", roe, score_higher_better(roe)),
        ("2. Création de valeur", val_crea, score_higher_better(val_crea)),
        ("3. Indépendance financière (%)", indep, score_higher_better(indep)),
        ("4. Marge op. US (%)", marge_us, score_higher_better(marge_us)),
        ("5. Marge op. Asie (%)", marge_cn, score_higher_better(marge_cn)),
        ("6. Marge op. Europe (%)", marge_eu, score_higher_better(marge_eu)),
        ("7. Part de marché US/Glob (%)", pdm_glob, score_higher_better(pdm_glob)),
        ("8. Part de marché Asie (%)", pdm_cn, score_higher_better(pdm_cn)),
        ("9. Part de marché Europe (%)", pdm_eu, score_higher_better(pdm_eu)),
        ("10. Demande insatisfaite (k)", dem_insat, score_lower_better(dem_insat)),
        ("11. Stocks en volume (k)", stocks_vol, score_lower_better(stocks_vol)),
        ("12. Coût moyen unit. US ($)", cost_us, score_lower_better(cost_us)),
        ("13. Coût moyen unit. Asie ($)", cost_cn, score_lower_better(cost_cn)),
        ("14. Coût moyen unit. Europe ($)", cost_eu, score_lower_better(cost_eu)),
        ("15. Productivité Ingénieurs", prod_eng, score_higher_better(prod_eng)),
    ]

    totals = [sum(c[2][i] for c in criteria) for i in range(12)]
    pts_pdm_us = score_higher_better(pdm_us)
    totals_us_var = [totals[i] - criteria[6][2][i] + pts_pdm_us[i] for i in range(12)]

    print(f"=== CLASSEMENT OFFICIEL ESTIMÉ (BARÈME ERIC ASTIEN) — {os.path.basename(target)} ===")
    ranking = sorted(range(12), key=lambda i: (-totals[i], decouvert[i]))
    for rank, idx in enumerate(ranking, 1):
        print(
            f"#{rank:2d} | {teams[idx]:18s} | {totals[idx]:3d} pts (var US={totals_us_var[idx]:3d}) "
            f"| Net={net_income[idx]:6.0f} M$ | Stocks={stocks_vol[idx]:5.0f} k | Découvert={decouvert[idx]:6.0f} M$"
        )


if __name__ == "__main__":
    main()
