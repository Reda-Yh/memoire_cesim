#!/usr/bin/env python3
"""
Analyseur Stratégique de la Concurrence & Prédicteur des Mouvements du Tour Suivant (Tour N+1)
Session : ESYBIA2AS (Univers 1) — Bordeaux INP Cesim Global Challenge

Ce script lit le rapport HTML du dernier tour terminé (ex: "manuels/Results for Univers 1, Tour 2.html")
et extrait pour les 12 équipes :
1. Leurs usines disponibles pour le PROCHAIN tour (Tour N+1) aux USA et en Chine.
2. Leurs stocks invendus à écouler au prochain tour (Thermique, Hybride, Électrique).
3. Leurs équipements maximums débloqués en R&D pour le prochain tour (Thermique, Hybride, Électrique, Hydrogène).
4. Leur trésorerie, dette long terme et découvert bancaire à rembourser.
5.Leur prix moyen et positionnement commercial -> Prédiction de ce qu'ils seront FORCÉS de faire au prochain tour !

Usage :
    python memoire_agent_cesim/analyseur_concurrence_et_decisions.py "manuels/Results for Univers 1, Tour 2.html"
"""
import sys
import os
from calculateur_classement_astien import CesimTableParser, to_float


def main():
    target = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "manuels/Results for Univers 1, Tour 2.html"
    )
    if not os.path.exists(target):
        print(f"Fichier introuvable : {target}")
        sys.exit(1)

    with open(target, "r", encoding="utf-8", errors="ignore") as f:
        p = CesimTableParser()
        p.feed(f.read())
        lines = p.lines

    def parse_row(line: str) -> list[float]:
        parts = [p.strip() for p in line.split("|")]
        vals = [to_float(x) for x in parts[1:13]]
        while len(vals) < 12:
            vals.append(0.0)
        return vals[:12]

    teams = [
        "Ren'Auto",
        "AURA",
        "IronHorse (NOUS)",
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

    # 1. Usines au prochain tour ("Tour suivant" sous "Nombre d'usines")
    usines_us_next, usines_cn_next = [0.0] * 12, [0.0] * 12
    for idx, line in enumerate(lines):
        if "Nombre d'usines" in line:
            for j in range(idx, min(idx + 12, len(lines))):
                if lines[j].split("|")[0].strip() in ("Tour suivant", "Prochain tour"):
                    usines_us_next = parse_row(lines[j + 1])
                    usines_cn_next = parse_row(lines[j + 2])
                    break
            break

    # 2. Stocks à écouler au début du prochain tour
    stocks_therm_us, stocks_hyb_us, stocks_therm_cn, stocks_hyb_cn = (
        [0.0] * 12,
        [0.0] * 12,
        [0.0] * 12,
        [0.0] * 12,
    )
    for idx, line in enumerate(lines):
        if "Stocks, k unités" in line or "Stocks, milliers d'unités" in line:
            t_rows = []
            h_rows = []
            for sub in lines[idx + 1 : idx + 11]:
                lbl = sub.split("|")[0].strip()
                if lbl == "Thermique":
                    t_rows.append(parse_row(sub))
                elif lbl == "Hybride":
                    h_rows.append(parse_row(sub))
            if len(t_rows) >= 2:
                stocks_therm_us, stocks_therm_cn = t_rows[0], t_rows[1]
            if len(h_rows) >= 2:
                stocks_hyb_us, stocks_hyb_cn = h_rows[0], h_rows[1]
            break

    # 3. Équipements proposés au dernier tour (USA Thermique & Hybride)
    eq_rows = [parse_row(l) for l in lines if "|" in l and l.split("|")[0].strip() == "Nombre d'équipements proposés"]
    eq_therm = eq_rows[0] if len(eq_rows) > 0 else [0.0] * 12
    eq_hyb = eq_rows[1] if len(eq_rows) > 1 else [0.0] * 12
    eq_elec = eq_rows[2] if len(eq_rows) > 2 else [0.0] * 12

    # 4. Trésorerie, Découvert, Dette LT
    cash = [0.0] * 12
    dette_lt = [0.0] * 12
    decouvert = [0.0] * 12
    for line in lines:
        if "|" in line:
            lbl = line.split("|")[0].strip()
            if lbl == "Trésorerie et équivalents" and not any(cash):
                cash = parse_row(line)
            elif lbl == "Dettes à long terme" and not any(dette_lt):
                dette_lt = parse_row(line)
            elif lbl == "Dettes à court terme (imprévues)" and not any(decouvert):
                decouvert = parse_row(line)

    print("=== RADAR CONCURRENCE & CAPACITÉS POUR LE PROCHAIN TOUR ===")
    print(
        f"{'Équipe':18s} | {'Usines US/CN':12s} | {'Cap.Brute':9s} | {'Stock T/H (k)':13s} | "
        f"{'Max Éq T/H/E':12s} | {'Cash/Découv.(M$)':17s} | Diagnostic Tactique"
    )
    print("-" * 135)
    for i in range(12):
        cap_brute = int(usines_us_next[i] * 200 + usines_cn_next[i] * 250)
        st_t = int(stocks_therm_us[i] + stocks_therm_cn[i])
        st_h = int(stocks_hyb_us[i] + stocks_hyb_cn[i])
        u_str = f"{int(usines_us_next[i])} US / {int(usines_cn_next[i])} CN"
        st_str = f"{st_t:4d}T / {st_h:3d}H"
        eq_str = f"{int(eq_therm[i]):2d}T/{int(eq_hyb[i]):1d}H/{int(eq_elec[i]):1d}E"
        fin_str = f"{int(cash[i]):5d} / {int(decouvert[i]):5d}"

        diag = []
        if st_t + st_h > 500:
            diag.append("SURSTOCK MASSIF (forcé de baisser prix/prod)")
        elif st_t + st_h == 0:
            diag.append("0 Stock (usines à 90%+)")
        if decouvert[i] > 3000:
            diag.append("CRISE CASH")
        if eq_elec[i] >= 1:
            diag.append(f"ÉLEC PRÊT ({int(eq_elec[i])} éq!)")
        print(
            f"{teams[i]:18s} | {u_str:12s} | {cap_brute:7d} k | {st_str:13s} | "
            f"{eq_str:12s} | {fin_str:17s} | {', '.join(diag)}"
        )


if __name__ == "__main__":
    main()
