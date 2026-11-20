#!/usr/bin/env python3
"""
P1 — Calibrateur des Élasticités du Modèle Logit de Marché Cesim
Session : ESYBIA2AS (Univers 1) — Bordeaux INP Cesim Global Challenge

Exploite les 5 rapports XLS tours 1 à 5 pour estimer empiriquement les élasticités
du modèle d'attractivité Logit théorique de Cesim :

    A(i,j,k) = (1 / Prix)^α × (1 + β × Équip) × (Pub)^γ × (1 + δ × ESG)

où :
  - i = équipe, j = région (USA/Chine/Europe), k = technologie (Thermique/Hybride/EV/H2)
  - α = élasticité-prix (> 0, coûts)
  - β = impact équipements (linéaire)
  - γ = élasticité-publicité (> 0)
  - δ = impact ESG (linéaire)

Méthode : Régression log-linéaire en Python stdlib pur (sans numpy/sklearn).
    ln(PDM) = α × ln(1/Prix) + γ × ln(Pub) + ε
Résout le système par méthode des moindres carrés (élimination de Gauss manuelle).

Usage :
    python 03_outils_et_scripts/calibrateur_elasticites_marche.py
    python 03_outils_et_scripts/calibrateur_elasticites_marche.py --verbose
"""
import argparse
import glob
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "03_outils_et_scripts"))
from calculateur_classement_astien import load_report_lines, to_float


# ---------------------------------------------------------------------------
# Utilitaires d'extraction
# ---------------------------------------------------------------------------

def find_nth_row(lines: list, prefix: str, n: int = 1) -> list:
    """Retourne la n-ième ligne commençant par prefix, avec 12 valeurs float."""
    count = 0
    for line in lines:
        if "|" in line:
            label = line.split("|")[0].strip()
            if label == prefix or label.startswith(prefix):
                count += 1
                if count == n:
                    parts = [p.strip() for p in line.split("|")]
                    vals = parts[1:13]
                    while len(vals) < 12:
                        vals.append("")
                    return [to_float(v) for v in vals[:12]]
    return [0.0] * 12


def extract_pdm_region(lines: list, region_label: str) -> list:
    """Extrait le Total PDM (%) pour une région donnée."""
    for idx, line in enumerate(lines):
        if region_label in line:
            for sub in lines[idx: idx + 10]:
                if sub.split("|")[0].strip() == "Total":
                    parts = [p.strip() for p in sub.split("|")]
                    vals = parts[1:13]
                    return [to_float(v) for v in vals[:12]]
    return [0.0] * 12


def extract_prix_region(lines: list, region_label: str, techno: str) -> list:
    """Extrait le prix de vente moyen par région et technologie (Moyenne pondérée)."""
    # Le prix est dans la section "Prix de vente" par technologie et marché.
    # On cherche le prix moyen pondéré le plus proche de la section région.
    # Fallback : utiliser le coût moyen unitaire comme proxy du prix.
    region_map = {"USA": 1, "Chine": 2, "Europe": 3}
    n = region_map.get(region_label, 1)
    return find_nth_row(lines, "Moyenne pondérée", n)


def extract_pub_total(lines: list) -> list:
    """Extrait la dépense publicitaire totale (toutes régions)."""
    result = [0.0] * 12
    # La pub est souvent sous forme de lignes "Publicité" par région.
    for line in lines:
        if "|" in line:
            lbl = line.split("|")[0].strip()
            if "Publicité" in lbl or "publicité" in lbl:
                parts = [p.strip() for p in line.split("|")]
                vals = [to_float(v) for v in parts[1:13]]
                for i in range(12):
                    result[i] += vals[i] if i < len(vals) else 0.0
    return result


def extract_esg_total(lines: list) -> list:
    """Extrait le score ESG (environnement + social + gouvernance) si disponible."""
    env = find_nth_row(lines, "Environnement", 1)
    soc = find_nth_row(lines, "Social", 1)
    gov = find_nth_row(lines, "Gouvernance", 1)
    combined = [env[i] + soc[i] + gov[i] for i in range(12)]
    return combined if any(combined) else [1.0] * 12  # 1.0 = neutre si absent


# ---------------------------------------------------------------------------
# Moindres carrés en stdlib pur (Gauss-Jordan 2 variables)
# ---------------------------------------------------------------------------

def ols_2var(xy_pairs: list) -> tuple:
    """
    Régression OLS y = a0 + a1*x1 + a2*x2 sur une liste de (x1, x2, y).
    Retourne (a0, a1, a2, R²).
    Utilise la méthode matricielle 3×3 par élimination de Gauss.
    """
    n = len(xy_pairs)
    if n < 4:
        return 0.0, 0.0, 0.0, float("nan")

    # Matrice normale X'X (3×3) et vecteur X'y (3×1)
    S = [[0.0] * 3 for _ in range(3)]
    T = [0.0, 0.0, 0.0]

    for x1, x2, y in xy_pairs:
        row = [1.0, x1, x2]
        for r in range(3):
            for c in range(3):
                S[r][c] += row[r] * row[c]
            T[r] += row[r] * y

    # Gauss-Jordan augmenté [S|T]
    M = [S[r][:] + [T[r]] for r in range(3)]
    for col in range(3):
        pivot = max(range(col, 3), key=lambda r: abs(M[r][col]))
        M[col], M[pivot] = M[pivot], M[col]
        if abs(M[col][col]) < 1e-12:
            return 0.0, 0.0, 0.0, float("nan")
        for row in range(3):
            if row != col:
                factor = M[row][col] / M[col][col]
                for k in range(4):
                    M[row][k] -= factor * M[col][k]

    coeffs = [M[r][3] / M[r][r] for r in range(3)]

    # R²
    y_vals = [pt[2] for pt in xy_pairs]
    y_mean = sum(y_vals) / n
    ss_tot = sum((y - y_mean) ** 2 for y in y_vals)
    if ss_tot < 1e-12:
        return coeffs[0], coeffs[1], coeffs[2], 1.0
    y_pred = [coeffs[0] + coeffs[1] * pt[0] + coeffs[2] * pt[1] for pt in xy_pairs]
    ss_res = sum((y_vals[i] - y_pred[i]) ** 2 for i in range(n))
    r2 = 1.0 - ss_res / ss_tot
    return coeffs[0], coeffs[1], coeffs[2], r2


# ---------------------------------------------------------------------------
# Collecte des données sur T1-T5
# ---------------------------------------------------------------------------

TEAMS = [
    "Ren'Auto", "AURA", "IronHorse", "YANAUTO", "tomobil", "GT-Auto VI",
    "Vrooom", "POLRAMOS", "Ça Roule", "BM2P", "TABCHOUR", "MO'THOR",
]

REGIONS = ["USA", "Chine", "Europe"]
REGION_PDM_LABELS = {
    "USA": "USA parts de marché, %",
    "Chine": "Chine parts de marché, %",
    "Europe": "Europe parts de marché, %",
}
REGION_COUT_N = {"USA": 1, "Chine": 2, "Europe": 3}


def collect_tour_data(report_path: str, tour_num: int, verbose: bool) -> list:
    """
    Retourne une liste de dict {tour, equipe, region, pdm, prix, pub, esg}
    pour toutes les équipes et régions d'un tour.
    """
    lines = load_report_lines(report_path)
    pub_total = extract_pub_total(lines)
    esg_total = extract_esg_total(lines)
    records = []

    for region in REGIONS:
        pdm_label = REGION_PDM_LABELS[region]
        pdm = extract_pdm_region(lines, pdm_label)
        cout_n = REGION_COUT_N[region]
        prix = find_nth_row(lines, "Moyenne pondérée", cout_n)

        for i, team in enumerate(TEAMS):
            # Exclure les observations aberrantes (PDM nulle ou prix nul)
            if pdm[i] <= 0.0 or prix[i] <= 0.0:
                continue
            records.append({
                "tour": tour_num,
                "equipe": team,
                "region": region,
                "pdm": pdm[i],
                "prix": prix[i],
                "pub": pub_total[i],
                "esg": esg_total[i],
            })
            if verbose:
                print(
                    f"  T{tour_num} | {team:12s} | {region:6s} | PDM={pdm[i]:5.2f}% "
                    f"| Prix={prix[i]:7.0f} | Pub={pub_total[i]:8.0f} | ESG={esg_total[i]:.2f}"
                )
    return records


# ---------------------------------------------------------------------------
# Estimation des élasticités
# ---------------------------------------------------------------------------

def estimate_elasticities(records: list) -> dict:
    """
    Modèle log-linéaire :
        ln(PDM) = const + α × ln(1/Prix) + γ × ln(Pub+1)
    Estimation globale + par région.
    Retourne dict des résultats.
    """
    results = {}

    def build_pairs(subset: list) -> list:
        pairs = []
        for r in subset:
            if r["prix"] > 0 and r["pdm"] > 0:
                x1 = math.log(1.0 / r["prix"])     # ln(1/Prix) → coefficient = α
                x2 = math.log(r["pub"] + 1.0)      # ln(Pub+1)  → coefficient = γ
                y  = math.log(r["pdm"])
                pairs.append((x1, x2, y))
        return pairs

    # Global
    pairs_glob = build_pairs(records)
    a0, alpha, gamma, r2 = ols_2var(pairs_glob)
    results["global"] = {
        "n_obs": len(pairs_glob),
        "alpha_prix": alpha,
        "gamma_pub": gamma,
        "intercept": a0,
        "R2": r2,
    }

    # Par région
    for region in REGIONS:
        subset = [r for r in records if r["region"] == region]
        pairs = build_pairs(subset)
        a0r, alpha_r, gamma_r, r2r = ols_2var(pairs)
        results[region] = {
            "n_obs": len(pairs),
            "alpha_prix": alpha_r,
            "gamma_pub": gamma_r,
            "intercept": a0r,
            "R2": r2r,
        }

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Calibre les élasticités Logit du marché Cesim sur T1-T5."
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Afficher chaque observation")
    args = parser.parse_args()

    reports_dir = os.path.join(ROOT, "04_rapports_tours")
    if not os.path.isdir(reports_dir):
        print(f"Dossier introuvable : {reports_dir}")
        sys.exit(1)

    all_records = []
    for tour_num in range(1, 6):
        pattern = os.path.join(reports_dir, f"tour_{tour_num:02d}_resultats_univers1.*")
        candidates = glob.glob(pattern)
        if not candidates:
            print(f"[AVERT] Tour {tour_num} absent — ignoré")
            continue
        report_path = sorted(candidates, key=lambda p: (0 if p.endswith(".xls") else 1))[0]
        print(f"\n--- Tour {tour_num} : {os.path.basename(report_path)} ---")
        records = collect_tour_data(report_path, tour_num, args.verbose)
        all_records.extend(records)
        print(f"  → {len(records)} observations collectées")

    if len(all_records) < 10:
        print("\n[ERREUR] Données insuffisantes pour calibrer les élasticités.")
        sys.exit(1)

    print(f"\n{'='*70}")
    print(f"CALIBRATION LOGIT — {len(all_records)} observations totales (T1-T5, 12 équipes × 3 régions)")
    print(f"Modèle : ln(PDM) = const + α × ln(1/Prix) + γ × ln(Pub+1)")
    print(f"{'='*70}")

    results = estimate_elasticities(all_records)

    print(f"\n{'Périmètre':<12} | {'N obs':>5} | {'α (Prix)':>10} | {'γ (Pub)':>10} | {'R²':>7} | Interprétation")
    print("-" * 70)
    for label, res in results.items():
        alpha = res["alpha_prix"]
        gamma = res["gamma_pub"]
        r2    = res["R2"]
        n     = res["n_obs"]
        interp = ""
        if abs(alpha) > 0.5:
            interp += f"Prix très élastique (α={alpha:.2f}). "
        elif abs(alpha) > 0.1:
            interp += f"Prix modérément élastique. "
        if abs(gamma) > 0.3:
            interp += f"Pub efficace (γ={gamma:.2f}). "
        print(f"{label:<12} | {n:>5} | {alpha:>10.4f} | {gamma:>10.4f} | {r2:>7.4f} | {interp}")

    print(f"\n{'='*70}")
    print("FOURCHETTES OBSERVÉES DES VARIABLES CLÉS (T1-T5)")
    print(f"{'='*70}")
    for region in REGIONS:
        subset = [r for r in all_records if r["region"] == region]
        if not subset:
            continue
        pdms  = [r["pdm"]  for r in subset]
        prix  = [r["prix"] for r in subset if r["prix"] > 0]
        pubs  = [r["pub"]  for r in subset if r["pub"]  > 0]
        print(f"\n{region}:")
        print(f"  PDM   : min={min(pdms):5.2f}%  max={max(pdms):5.2f}%  moy={sum(pdms)/len(pdms):5.2f}%")
        if prix:
            print(f"  Prix  : min={min(prix):8.0f}  max={max(prix):8.0f}  moy={sum(prix)/len(prix):8.0f} USD")
        if pubs:
            print(f"  Pub   : min={min(pubs):8.0f}  max={max(pubs):8.0f}  moy={sum(pubs)/len(pubs):8.0f} k USD")

    print(f"\n{'='*70}")
    print("MISE EN GARDE STATISTIQUE")
    print(f"{'='*70}")
    print("""
  - 5 tours × 12 équipes × 3 régions = 180 observations max (moins les zéros).
  - Le modèle OLS log-linéaire simplifie Logit multinomial → élasticités approchées.
  - α et γ sont estimés en supposant l'indépendance entre observations
    (non respectée : même équipe sur plusieurs tours = autocorrélation temporelle).
  - Ces fourchettes servent à borner les simulations de l'optimiseur, pas à prédire
    une PDM exacte.
  - Pour T6+ : réestimer après chaque tour avec les nouveaux rapports.
""")


if __name__ == "__main__":
    main()
