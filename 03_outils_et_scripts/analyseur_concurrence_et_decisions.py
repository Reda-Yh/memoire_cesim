#!/usr/bin/env python3
"""
Analyseur Stratégique de la Concurrence & Prédicteur des Mouvements du Tour Suivant (Tour N+1 & N+2)
Session : ESYBIA2AS (Univers 1) — Bordeaux INP Cesim Global Challenge

Ce script lit le rapport Excel (.xls) ou HTML du dernier tour terminé (détecté automatiquement ou via argument, ex: "04_rapports_tours/tour_04_resultats_univers1.xls")
et extrait pour les 12 équipes :
1. Leurs usines disponibles pour le PROCHAIN tour (t+1) et APRES LE PROCHAIN TOUR (t+2) aux USA et en Chine.
2. Leurs stocks invendus sur TOUTES les technologies (Thermique, Hybride, Électrique, Hydrogène).
3. Leurs équipements proposés en Thermique, Hybride, Électrique, Hydrogène.
4. Leur trésorerie, dette long terme et découvert bancaire à rembourser.
5. Leurs scores ESG (Environnement, Social, Gouvernance), Score DDRS Fournisseurs et Certification ESG.

Usage :
    python memoire_agent_cesim/03_outils_et_scripts/analyseur_concurrence_et_decisions.py
    python memoire_agent_cesim/03_outils_et_scripts/analyseur_concurrence_et_decisions.py "04_rapports_tours/tour_04_resultats_univers1.xls"
"""
import os
import sys
from calculateur_classement_astien import load_report_lines, resolve_report_path, to_float


def main():
    target = resolve_report_path(sys.argv[1] if len(sys.argv) > 1 else None)
    lines = load_report_lines(target)

    def parse_str_row(line: str) -> list[str]:
        parts = [cell.strip() for cell in line.split("|")]
        vals = parts[1:13]
        while len(vals) < 12:
            vals.append("")
        return vals[:12]

    def parse_row(line: str) -> list[float]:
        return [to_float(x) for x in parse_str_row(line)]

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

    # 1. Usines à t+1 ("Tour suivant") et t+2 ("Après le prochain tour")
    usines_us_t1, usines_cn_t1 = [0.0] * 12, [0.0] * 12
    usines_us_t2, usines_cn_t2 = [0.0] * 12, [0.0] * 12
    for idx, line in enumerate(lines):
        if "Nombre d'usines" in line:
            for j in range(idx + 1, min(idx + 14, len(lines))):
                lbl = lines[j].split("|")[0].strip()
                if lbl in ("Tour suivant", "Prochain tour") and j + 2 < len(lines):
                    usines_us_t1 = parse_row(lines[j + 1])
                    usines_cn_t1 = parse_row(lines[j + 2])
                elif lbl.startswith("Après le prochain tour") and j + 2 < len(lines):
                    usines_us_t2 = parse_row(lines[j + 1])
                    usines_cn_t2 = parse_row(lines[j + 2])
            break

    # 2. Stocks totaux (USA + Chine) sur TOUTES les technologies
    stocks_by_tech = {
        "Thermique": [0.0] * 12,
        "Hybride": [0.0] * 12,
        "Électrique": [0.0] * 12,
        "Hydrogène": [0.0] * 12,
    }
    for idx, line in enumerate(lines):
        if "Stocks, k unités" in line or "Stocks, milliers d'unités" in line:
            for sub in lines[idx + 1 : idx + 16]:
                if "Nombre d'usines" in sub:
                    break
                lbl = sub.split("|")[0].strip()
                if lbl in stocks_by_tech:
                    row = parse_row(sub)
                    for i in range(12):
                        stocks_by_tech[lbl][i] += row[i]
            break

    # 3. Équipements proposés : conserver les valeurs par région (ne pas masquer
    # les différences avec un maximum USA/Chine/Europe).
    technologies = ("Thermique", "Hybride", "Électrique", "Hydrogène")
    regions = ("USA", "Chine", "Europe")
    equipment_by_region = {
        region: {tech: [None] * 12 for tech in technologies} for region in regions
    }
    current_region = None
    current_tech = None
    in_zone_results = False
    for line in lines:
        if line.startswith("Résultats par zone, "):
            region_name = line.split(",", 1)[1].strip()
            current_region = region_name if region_name in equipment_by_region else None
            current_tech = None
            in_zone_results = True
            continue
        if in_zone_results:
            if line.startswith("Rapport RH"):
                break
            label = line.split("|")[0].strip() if "|" in line else line.strip()
            if label in technologies:
                current_tech = label
            elif label == "Nombre d'équipements proposés" and current_region and current_tech:
                raw_values = parse_str_row(line)
                equipment_by_region[current_region][current_tech] = [
                    to_float(value) if value else None for value in raw_values
                ]

    # Valeur de synthèse = maximum régional, conservée uniquement pour compatibilité
    # avec l'ancien radar ; les valeurs régionales détaillées sont imprimées ensuite.
    eq_by_tech = {
        tech: [max((equipment_by_region[r][tech][i] or 0) for r in regions) for i in range(12)]
        for tech in technologies
    }
    eq_therm = eq_by_tech["Thermique"]
    eq_hyb = eq_by_tech["Hybride"]
    eq_elec = eq_by_tech["Électrique"]
    eq_hydro = eq_by_tech["Hydrogène"]

    # 4. Trésorerie, Dette LT, Découvert
    cash, dette_lt, decouvert = [0.0] * 12, [0.0] * 12, [0.0] * 12
    for line in lines:
        if "|" in line:
            lbl = line.split("|")[0].strip()
            if lbl == "Trésorerie et équivalents" and not any(cash):
                cash = parse_row(line)
            elif lbl == "Dettes à long terme" and not any(dette_lt):
                dette_lt = parse_row(line)
            elif lbl == "Dettes à court terme (imprévues)" and not any(decouvert):
                decouvert = parse_row(line)

    # 5. ESG (E / S / G), DDRS Fournisseurs, Certification ESG
    env_score, soc_score, gov_score = [0.0] * 12, [0.0] * 12, [0.0] * 12
    for idx, line in enumerate(lines):
        if "Score final" in line and idx + 3 < len(lines):
            env_score = parse_row(lines[idx + 1])
            soc_score = parse_row(lines[idx + 2])
            gov_score = parse_row(lines[idx + 3])
            break

    ddrs_qual, ddrs_dd = [0.0] * 12, [0.0] * 12
    certs = ["Aucune"] * 12
    for line in lines:
        if "|" not in line:
            continue
        lbl = line.split("|")[0].strip()
        if lbl == "Qualité" and not any(ddrs_qual):
            ddrs_qual = parse_row(line)
        elif lbl == "Développement durable" and not any(ddrs_dd):
            ddrs_dd = parse_row(line)
        elif lbl.startswith("Cert") and "développement" in lbl:
            certs = [c or "Aucune" for c in parse_str_row(line)]

    print(f"=== RADAR CONCURRENCE & CAPACITÉS ({os.path.basename(target)}) ===")
    print(
        f"{'Équipe':18s} | {'Usines t+1 (Cap)':18s} | {'Usines t+2 (Cap)':18s} | "
        f"{'Stock T/H/E+Hy (k)':18s} | {'Éq T/H/E/Hy':11s} | {'Cash/Découv(M$)':15s} | Diagnostic"
    )
    print("-" * 145)
    for i in range(12):
        cap_t1 = int(usines_us_t1[i] * 200 + usines_cn_t1[i] * 250)
        cap_t2 = int(usines_us_t2[i] * 200 + usines_cn_t2[i] * 250)
        u_t1 = f"{int(usines_us_t1[i]):2d}U/{int(usines_cn_t1[i]):2d}C ({cap_t1:4d}k)"
        u_t2 = f"{int(usines_us_t2[i]):2d}U/{int(usines_cn_t2[i]):2d}C ({cap_t2:4d}k)"

        st_t = int(stocks_by_tech["Thermique"][i])
        st_h = int(stocks_by_tech["Hybride"][i])
        st_eh = int(stocks_by_tech["Électrique"][i] + stocks_by_tech["Hydrogène"][i])
        st_tot = st_t + st_h + st_eh
        st_str = f"{st_t:4d}T/{st_h:3d}H/{st_eh:3d}E"

        eq_str = f"{int(eq_therm[i]):2d}/{int(eq_hyb[i]):1d}/{int(eq_elec[i]):1d}/{int(eq_hydro[i]):1d}"
        fin_str = f"{int(cash[i]):5d} / {int(decouvert[i]):5d}"

        diag = []
        if st_tot > 500:
            diag.append("SURSTOCK MASSIF")
        elif st_tot == 0:
            diag.append("0 Stock")
        if decouvert[i] > 1000:
            diag.append("DÉCOUVERT!")
        if cap_t2 > cap_t1:
            diag.append(f"+{cap_t2 - cap_t1}k cap à t+2")
        if eq_elec[i] >= 1 or st_eh > 0:
            diag.append("ÉLEC ACTIF")
        if eq_hydro[i] >= 1:
            diag.append("HYDRO ACTIF")

        print(
            f"{teams[i]:18s} | {u_t1:18s} | {u_t2:18s} | {st_str:18s} | "
            f"{eq_str:11s} | {fin_str:15s} | {', '.join(diag)}"
        )

    print("\n=== ÉQUIPEMENTS PAR RÉGION (T/H/E/H2) ===")
    print(f"{'Équipe':18s} | {'USA':15s} | {'Chine':15s} | {'Europe':15s}")
    print("-" * 72)
    for i in range(12):
        def fmt_region(region):
            vals = [equipment_by_region[region][tech][i] for tech in technologies]
            return "/".join("—" if value is None else str(int(value)) for value in vals)
        print(f"{teams[i]:18s} | {fmt_region('USA'):15s} | {fmt_region('Chine'):15s} | {fmt_region('Europe'):15s}")

    if any(env_score) or any(ddrs_qual):
        print("\n=== RADAR ESG, FOURNISSEURS (DDRS) & DETTE LT ===")
        print(
            f"{'Équipe':18s} | {'DDRS (Q+DD)':11s} | {'Env (E)':7s} | {'Soc (S)':7s} | "
            f"{'Gouv (G)':8s} | {'Dette LT':8s} | Certification"
        )
        print("-" * 92)
        for i in range(12):
            ddrs = ddrs_qual[i] + ddrs_dd[i]
            print(
                f"{teams[i]:18s} | {ddrs:11.2f} | {env_score[i]:7.2f} | {soc_score[i]:7.2f} | "
                f"{gov_score[i]:8.2f} | {int(dette_lt[i]):8d} | {certs[i]}"
            )


if __name__ == "__main__":
    main()
