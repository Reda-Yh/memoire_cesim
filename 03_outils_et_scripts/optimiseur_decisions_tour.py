#!/usr/bin/env python3
"""
P2 — Simulateur d'Optimisation Décisionnelle IronHorse (Tours 6-10)
Session : ESYBIA2AS (Univers 1) — Bordeaux INP Cesim Global Challenge

Modules :
  1. optimise_dividende_tsr()      → Dividende optimal sous contrainte de liquidité
  2. planifier_basculement_cop32() → Reconversion COP32 : éliminer Thermique avant T7
  3. simuler_points_tsr()          → Rang TSR simulé parmi 12 équipes

Usage :
    python 03_outils_et_scripts/optimiseur_decisions_tour.py --help
    python 03_outils_et_scripts/optimiseur_decisions_tour.py \\
        --cash-usa 20000 --cash-chine 15000 --cash-europe 9000 \\
        --actions 1621.9 --cours-precedent 163.57 \\
        --usines-usa 9 --usines-chine 6 \\
        --demande-hybride-usa 350 --demande-ev-usa 100 --demande-h2-usa 50 \\
        --sous-traitance-max 525

Python standard uniquement — aucune dépendance externe.
"""
import argparse
import math
import sys

# ---------------------------------------------------------------------------
# 1. Optimiseur Dividende & TSR
# ---------------------------------------------------------------------------

def simuler_cours_estime(
    cap_propres: float,
    net_income: float,
    actions: float,
    dividende_mds: float,
    per_sectoriel: float = 12.0,
) -> float:
    """
    Estimation simplifiée du cours de l'action après dividende.

    Modèle calibré sur les données Cesim T1-T5 IronHorse :
      - Cours observé T5 = 163.57 USD avec cap_propres ≈ 52 000 M$,
        actions ≈ 1 621.9 M, net_income ≈ 16 630 M$.
      - EPS = 16 630 / 1 621.9 ≈ 10.25 USD/action
      - PER implicite = 163.57 / 10.25 ≈ 15.96 → on retient PER ≈ 16

    Le dividende est DÉJÀ dans le DPS du TSR (il ne réduit pas le cours
    directement, sauf via la réduction des capitaux propres ensuite).
    On applique donc :
      BV = (Cap_propres - Dividende) / Actions   [ex-dividende]
      PER × EPS                                   [basé sur net_income futur]
      Cours = max(BV, PER × EPS)

    PER sectoriel Cesim observé : ~16 (non 12) d'après données T5.
    """
    if actions <= 0:
        raise ValueError(f"Nombre d'actions invalide : {actions}")
    cap_propres_post = max(0.0, cap_propres - dividende_mds)
    bv_par_action = cap_propres_post / actions
    eps = net_income / actions
    cours_per = per_sectoriel * eps
    return max(bv_par_action, cours_per, 0.01)


def calculer_tsr(
    cours_actuel: float,
    cours_precedent: float,
    dividende_mds: float,
    actions: float,
) -> float:
    """
    TSR (%) = (Cours_t - Cours_t-1 + DPS) / Cours_t-1 × 100
    DPS = Dividende (M USD, positif) / Actions (millions)
    """
    if cours_precedent <= 0:
        raise ValueError(f"Cours précédent invalide : {cours_precedent}")
    if actions <= 0:
        raise ValueError(f"Nombre d'actions invalide : {actions}")
    dps = dividende_mds / actions
    return (cours_actuel - cours_precedent + dps) / cours_precedent * 100.0


def optimise_dividende_tsr(
    cash_usa: float,
    cash_chine: float,
    cash_europe: float,
    actions: float,
    cours_precedent: float,
    cap_propres: float,
    net_income: float,
    tsr_concurrents: list = None,
    min_cash_reserve: float = 2000.0,
    pas_mds: float = 1000.0,
    transfert_usa_europe_max: float = 10000.0,
    per_sectoriel: float = 16.0,
) -> dict:
    """
    Résout DPS* = argmax(Points_TSR) s.c. Découvert bancaire = 0 dans les 3 zones.

    Paramètres :
        cash_usa, cash_chine, cash_europe : Trésoreries disponibles (M USD)
        actions                : Actions sur le marché (millions)
        cours_precedent        : Cours de l'action fin du tour précédent (USD)
        cap_propres            : Capitaux propres actuels (M USD)
        net_income             : Résultat net annuel projeté (M USD)
        tsr_concurrents        : Liste des TSR estimés des 11 concurrents (%)
                                 Si None → simuler un rang moyen conservateur.
        min_cash_reserve       : Cash minimum à conserver par zone (M USD)
        pas_mds                : Pas d'exploration des dividendes (M USD)
        transfert_usa_europe_max : Transfert max autorisé USA→Europe (M USD)

    Retourne un dict avec le dividende optimal, TSR résultant, rang simulé, transfert recommandé.
    """
    if cours_precedent <= 0:
        raise ValueError(f"Cours précédent invalide : {cours_precedent}")
    if actions <= 0:
        raise ValueError(f"Nombre d'actions invalide : {actions}")

    # Cash total disponible pour distribution
    cash_total = cash_usa + cash_chine + cash_europe
    # On ne distribue que depuis USA (pratique IronHorse observée aux T4-T5)
    # Le transfert USA→Europe finance si Europe est trop juste.
    max_dividende = max(0.0, cash_usa - min_cash_reserve)

    best = {
        "dividende_mds": 0.0,
        "tsr_pct": 0.0,
        "cours_estime": cours_precedent,
        "rang_tsr": 7,  # conservateur
        "pts_tsr": 6,
        "transfert_usa_europe": 0.0,
        "cash_usa_post": cash_usa,
        "cash_europe_post": cash_europe,
        "viable": True,
    }
    best_pts = 1  # Minimum absolu

    div = 0.0
    while div <= max_dividende + pas_mds / 2:
        # Cours estimé après versement du dividende
        try:
            cours_est = simuler_cours_estime(cap_propres, net_income, actions, div, per_sectoriel=per_sectoriel)
        except ValueError:
            div += pas_mds
            continue

        # TSR résultant
        tsr = calculer_tsr(cours_est, cours_precedent, div, actions)

        # Rang TSR parmi 12 équipes (1 = meilleur)
        if tsr_concurrents and len(tsr_concurrents) == 11:
            rang = 1 + sum(1 for t in tsr_concurrents if t > tsr)
        else:
            # Heuristique : TSR > 25% → top 5, etc.
            if tsr >= 40:
                rang = 2
            elif tsr >= 25:
                rang = 5
            elif tsr >= 15:
                rang = 7
            else:
                rang = 10
        pts_tsr = max(1, min(12, 13 - rang))

        # Contrainte liquidité USA
        cash_usa_post = cash_usa - div
        if cash_usa_post < min_cash_reserve:
            # Essayer transfert Europe → USA ou skip
            div += pas_mds
            continue

        if pts_tsr > best_pts or (pts_tsr == best_pts and div > best["dividende_mds"]):
            best_pts = pts_tsr
            # Transfert USA→Europe recommandé si Europe en dessous du seuil
            transfert = max(0.0, min_cash_reserve - cash_europe)
            transfert = min(transfert, transfert_usa_europe_max, cash_usa_post - min_cash_reserve)
            best = {
                "dividende_mds": div,
                "tsr_pct": tsr,
                "cours_estime": cours_est,
                "rang_tsr": rang,
                "pts_tsr": pts_tsr,
                "transfert_usa_europe": transfert,
                "cash_usa_post": cash_usa_post - transfert,
                "cash_europe_post": cash_europe + transfert,
                "viable": True,
            }
        div += pas_mds

    return best


# ---------------------------------------------------------------------------
# 2. Planificateur COP32 — Basculement Industriel Tour 7
# ---------------------------------------------------------------------------

CAPACITE_PAR_USINE_USA = 200   # k unités / usine / tour (USA)
CAPACITE_PAR_USINE_CHINE = 250  # k unités / usine / tour (Chine)

def planifier_basculement_cop32(
    usines_usa: int,
    usines_chine: int,
    stock_thermique_usa: float,
    stock_thermique_chine: float,
    demande_hybride_usa: float,
    demande_ev_usa: float,
    demande_h2_usa: float,
    demande_hybride_chine: float,
    demande_ev_chine: float,
    demande_h2_chine: float,
    h2_debloque: bool = True,
    sous_traitance_max_usa: float = 525.0,
    sous_traitance_max_chine: float = 525.0,
) -> dict:
    """
    Planifie la reconversion COP32 pour T7 : élimination TOTALE du Thermique.
    
    Règle COP32 (Eric Astien) :
      - À partir de T7, interdiction de commercialiser du 100% Thermique.
      - Stock thermique DOIT être = 0 k unités à la fin de T6.
      - Capacités libérées → allouées à Hybride / Électrique / Hydrogène.

    Paramètres :
        usines_usa, usines_chine : Nombre d'usines actives au tour T (après construction T6)
        stock_thermique_*        : Stocks thermiques résiduels à écouler (k unités)
        demande_hybride/ev/h2_*  : Demande estimée T7 (k unités) par région et techno
        h2_debloque              : True si le cumul R&D Hydrogène dépasse 2 115 480 j-h
        sous_traitance_max_*     : Capacité max de sous-traitance disponible (k unités)

    Retourne un plan d'allocation détaillé + alertes.
    """
    alertes = []
    if stock_thermique_usa > 0:
        alertes.append(
            f"[CRITIQUE] Stock thermique USA = {stock_thermique_usa:.0f} k unités. "
            "Doit être écoulé ou détruit avant fin T6."
        )
    if stock_thermique_chine > 0:
        alertes.append(
            f"[CRITIQUE] Stock thermique Chine = {stock_thermique_chine:.0f} k unités. "
            "Doit être écoulé ou détruit avant fin T6."
        )
    if not h2_debloque:
        alertes.append(
            "[AVERT] Hydrogène non encore débloqué (< 2 115 480 j-h R&D cumulés). "
            "Allocation H2 T7 sera nulle."
        )

    # Capacité productive interne T7
    cap_usa_total = usines_usa * CAPACITE_PAR_USINE_USA    # k unités
    cap_chine_total = usines_chine * CAPACITE_PAR_USINE_CHINE  # k unités

    # Demande totale non-thermique à satisfaire
    demande_usa = demande_hybride_usa + demande_ev_usa + (demande_h2_usa if h2_debloque else 0)
    demande_chine = demande_hybride_chine + demande_ev_chine + (demande_h2_chine if h2_debloque else 0)

    # Production interne (priorité capacité interne)
    prod_interne_usa = min(cap_usa_total, demande_usa)
    prod_interne_chine = min(cap_chine_total, demande_chine)

    # Sous-traitance nécessaire
    gap_usa = max(0.0, demande_usa - prod_interne_usa)
    gap_chine = max(0.0, demande_chine - prod_interne_chine)
    sous_trait_usa = min(gap_usa, sous_traitance_max_usa)
    sous_trait_chine = min(gap_chine, sous_traitance_max_chine)

    demande_insatisfaite_usa = max(0.0, gap_usa - sous_trait_usa)
    demande_insatisfaite_chine = max(0.0, gap_chine - sous_trait_chine)

    if demande_insatisfaite_usa > 0:
        alertes.append(
            f"[AVERT] Demande insatisfaite USA T7 = {demande_insatisfaite_usa:.0f} k unités. "
            "Envisager construction d'usines supplémentaires dès T6."
        )
    if demande_insatisfaite_chine > 0:
        alertes.append(
            f"[AVERT] Demande insatisfaite Chine T7 = {demande_insatisfaite_chine:.0f} k unités."
        )

    # Répartition interne par technologie (au prorata de la demande)
    def alloc(cap_int, demandes: list) -> list:
        """Alloue cap_int k unités au prorata des demandes."""
        total = sum(demandes)
        if total <= 0:
            return [0.0] * len(demandes)
        return [cap_int * d / total for d in demandes]

    techno_demande_usa = [demande_hybride_usa, demande_ev_usa, demande_h2_usa if h2_debloque else 0]
    techno_demande_chine = [demande_hybride_chine, demande_ev_chine, demande_h2_chine if h2_debloque else 0]
    alloc_int_usa = alloc(prod_interne_usa, techno_demande_usa)
    alloc_int_chine = alloc(prod_interne_chine, techno_demande_chine)

    return {
        "alertes": alertes,
        "usa": {
            "usines": usines_usa,
            "capacite_interne_k": cap_usa_total,
            "prod_hybride_k": round(alloc_int_usa[0], 1),
            "prod_ev_k": round(alloc_int_usa[1], 1),
            "prod_h2_k": round(alloc_int_usa[2], 1),
            "sous_traitance_k": round(sous_trait_usa, 1),
            "demande_insatisfaite_k": round(demande_insatisfaite_usa, 1),
        },
        "chine": {
            "usines": usines_chine,
            "capacite_interne_k": cap_chine_total,
            "prod_hybride_k": round(alloc_int_chine[0], 1),
            "prod_ev_k": round(alloc_int_chine[1], 1),
            "prod_h2_k": round(alloc_int_chine[2], 1),
            "sous_traitance_k": round(sous_trait_chine, 1),
            "demande_insatisfaite_k": round(demande_insatisfaite_chine, 1),
        },
        "h2_debloque": h2_debloque,
        "stock_thermique_total_k": stock_thermique_usa + stock_thermique_chine,
    }


# ---------------------------------------------------------------------------
# 3. Stratégie d'Atterrissage & Fin de Partie (Horizon Fixe = Tour 10)
# ---------------------------------------------------------------------------

TOTAL_ROUNDS_CESIM = 10

def analyser_regles_fin_de_partie(tour: int, total_rounds: int = TOTAL_ROUNDS_CESIM) -> list:
    """
    Règles stratégiques impératives selon le tour joué (horizon final = Tour 10).
    Prend en compte les temps de latence (usines = 2 tours, R&D, valorisation finale).
    """
    recos = []
    if tour > total_rounds:
        recos.append(f"[ERREUR] Le Tour {tour} dépasse le dernier tour officiel ({total_rounds}).")
        return recos

    if tour >= 9:
        recos.append(
            f"[INTERDICTION STRICTE - CAPEX] Ne lancez AUCUNE construction d'usine au Tour {tour} ! "
            f"Délai usine = 2 tours (livraison au Tour {tour + 2} alors que la partie s'arrête au Tour {total_rounds}). "
            "Toute usine lancée au Tour 9 ou 10 est une PERTE NETTE à 100 % (dépense sans aucune production possible)."
        )
    elif tour == 8:
        recos.append(
            f"[VIGILANCE CAPEX T8] Une usine lancée au Tour 8 ne sera livrée qu'au Tour 10 "
            f"(exploitable seulement 1 tour sur {total_rounds}). Ne construire que si la rentabilité immédiate couvre le coût."
        )

    if tour == total_rounds:  # Tour 10 : Dernier tour absolu
        recos.append(
            f"[TOUR 10 - CLÔTURE DU CHALLENGE] STOCKS : Viser STRICTEMENT 0 k de stock sur TOUTES les technologies. "
            "Tout stock restant à la fin du Tour 10 est valorisé avec une décote massive et devient une perte sèche."
        )
        recos.append(
            f"[TOUR 10 - CLÔTURE DU CHALLENGE] DIVIDENDES : Vider l'excédent de cash (tout en conservant un buffer pour 0 découvert). "
            "Les milliards dormants non distribués au Tour 10 réduisent le ROE et le TSR final !"
        )
        recos.append(
            f"[TOUR 10 - CLÔTURE DU CHALLENGE] R&D : Stopper tout budget de recherche de nouvelles technologies. "
            "Maintenir uniquement les salaires/formation RH pour la productivité ingénieurs du tour en cours."
        )
    elif tour == total_rounds - 1:  # Tour 9
        recos.append(
            f"[TOUR 9 - AVANT-DERNIER TOUR] Calibrer la sous-traitance et la production pour amorcer le déstockage "
            f"complet en vue du Tour {total_rounds}."
        )
    return recos


# ---------------------------------------------------------------------------
# 4. Main CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Optimiseur décisionnel IronHorse — TSR, Dividende & COP32 (Tours 6 à 10, fin de partie au T10).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--tour", type=int, default=7, choices=range(6, 11),
                        help="Numéro du tour à simuler (de 6 à 10, le tour 10 étant le tour final).")
    # Paramètres financiers
    fin = parser.add_argument_group("Paramètres financiers")
    fin.add_argument("--cash-usa", type=float, default=20000.0, help="Trésorerie USA (M USD)")
    fin.add_argument("--cash-chine", type=float, default=15000.0, help="Trésorerie Chine (M USD)")
    fin.add_argument("--cash-europe", type=float, default=9000.0, help="Trésorerie Europe (M USD)")
    fin.add_argument("--actions", type=float, default=1621.9, help="Actions sur le marché (millions)")
    fin.add_argument("--cours-precedent", type=float, default=163.57, help="Cours action T_précédent (USD)")
    fin.add_argument("--cap-propres", type=float, default=52000.0, help="Capitaux propres (M USD)")
    fin.add_argument("--net-income", type=float, default=16630.0, help="Résultat net projeté (M USD)")
    fin.add_argument("--tsr-concurrents", type=float, nargs=11, default=None,
                     help="TSR estimé des 11 concurrents (11 valeurs)")
    fin.add_argument("--min-cash-reserve", type=float, default=2000.0, help="Cash min par zone (M USD)")
    fin.add_argument("--pas-dividende", type=float, default=1000.0, help="Pas d'exploration dividende (M USD)")

    # Paramètres COP32
    cop = parser.add_argument_group("Paramètres COP32 / Production T7")
    cop.add_argument("--usines-usa", type=int, default=9, help="Usines USA actives T7")
    cop.add_argument("--usines-chine", type=int, default=6, help="Usines Chine actives T7")
    cop.add_argument("--stock-therm-usa", type=float, default=0.0, help="Stock Thermique USA (k unités)")
    cop.add_argument("--stock-therm-chine", type=float, default=0.0, help="Stock Thermique Chine (k unités)")
    cop.add_argument("--demande-hybride-usa", type=float, default=350.0, help="Demande Hybride USA T7 (k)")
    cop.add_argument("--demande-ev-usa", type=float, default=150.0, help="Demande EV USA T7 (k)")
    cop.add_argument("--demande-h2-usa", type=float, default=80.0, help="Demande H2 USA T7 (k)")
    cop.add_argument("--demande-hybride-chine", type=float, default=300.0, help="Demande Hybride Chine T7 (k)")
    cop.add_argument("--demande-ev-chine", type=float, default=200.0, help="Demande EV Chine T7 (k)")
    cop.add_argument("--demande-h2-chine", type=float, default=50.0, help="Demande H2 Chine T7 (k)")
    cop.add_argument("--no-h2", action="store_true", help="H2 non débloqué (R&D < seuil)")
    cop.add_argument("--sous-traitance-max", type=float, default=525.0, help="Sous-traitance max par zone (k)")

    args = parser.parse_args()

    sep = "=" * 65
    print(f"\n{sep}")
    print(f"OPTIMISEUR DÉCISIONNEL IRONHORSE — TOUR {args.tour} (HORIZON FINAL = TOUR 10)")
    print(sep)

    # --- Module 0 : Analyse stratégique de l'horizon final ---
    regles_fin = analyser_regles_fin_de_partie(args.tour, total_rounds=10)
    if regles_fin:
        print(f"\n[HORIZON FIN DE PARTIE - TOUR {args.tour} / 10]\n")
        for r in regles_fin:
            print(f"  • {r}")

    # --- Module 1 : Dividende optimal ---
    print("\n[MODULE 1] OPTIMISATION DIVIDENDE & TSR\n")
    result_div = optimise_dividende_tsr(
        cash_usa=args.cash_usa,
        cash_chine=args.cash_chine,
        cash_europe=args.cash_europe,
        actions=args.actions,
        cours_precedent=args.cours_precedent,
        cap_propres=args.cap_propres,
        net_income=args.net_income,
        tsr_concurrents=args.tsr_concurrents,
        min_cash_reserve=args.min_cash_reserve,
        pas_mds=args.pas_dividende,
        per_sectoriel=16.0,  # PER calibré sur données Cesim T5
    )

    print(f"  Dividende optimal recommandé  : {result_div['dividende_mds']:>8,.0f} M USD")
    print(f"  DPS (dividende/action)        : {result_div['dividende_mds']/args.actions:>8.2f} USD/action")
    print(f"  Cours estimé T                : {result_div['cours_estime']:>8.2f} USD")
    print(f"  TSR simulé                    : {result_div['tsr_pct']:>8.2f} %")
    print(f"  Rang TSR simulé               : {result_div['rang_tsr']:>8d} / 12")
    print(f"  Points TSR simulés            : {result_div['pts_tsr']:>8d} / 12 pts")
    print(f"  Transfert USA→Europe conseillé: {result_div['transfert_usa_europe']:>8,.0f} M USD")
    print(f"  Cash USA post-dividende       : {result_div['cash_usa_post']:>8,.0f} M USD")
    print(f"  Cash Europe post-transfert    : {result_div['cash_europe_post']:>8,.0f} M USD")

    # Vérification contrainte découvert
    if result_div["cash_usa_post"] < 0:
        print("  [ALERTE] Cash USA négatif après dividende ! Réduire le dividende.")
    elif result_div["cash_europe_post"] < 0:
        print("  [ALERTE] Cash Europe négatif ! Augmenter le transfert ou réduire le dividende.")
    else:
        print("  [OK] Aucun découvert bancaire anticipé dans les 3 zones.")

    # --- Module 2 : COP32 ---
    print(f"\n{sep}")
    print("[MODULE 2] PLANIFICATION BASCULEMENT INDUSTRIEL COP32 (T7)\n")

    plan = planifier_basculement_cop32(
        usines_usa=args.usines_usa,
        usines_chine=args.usines_chine,
        stock_thermique_usa=args.stock_therm_usa,
        stock_thermique_chine=args.stock_therm_chine,
        demande_hybride_usa=args.demande_hybride_usa,
        demande_ev_usa=args.demande_ev_usa,
        demande_h2_usa=args.demande_h2_usa,
        demande_hybride_chine=args.demande_hybride_chine,
        demande_ev_chine=args.demande_ev_chine,
        demande_h2_chine=args.demande_h2_chine,
        h2_debloque=not args.no_h2,
        sous_traitance_max_usa=args.sous_traitance_max,
        sous_traitance_max_chine=args.sous_traitance_max,
    )

    for zone, label in [("usa", "USA"), ("chine", "Chine")]:
        z = plan[zone]
        print(f"  {label} ({z['usines']} usines | cap. {z['capacite_interne_k']} k unités)")
        print(f"    Hybride interne  : {z['prod_hybride_k']:>7.1f} k unités")
        print(f"    EV interne       : {z['prod_ev_k']:>7.1f} k unités")
        print(f"    H2 interne       : {z['prod_h2_k']:>7.1f} k unités {'(H2 non dispo)' if not plan['h2_debloque'] else ''}")
        print(f"    Sous-traitance   : {z['sous_traitance_k']:>7.1f} k unités")
        print(f"    Demand. insatisf.: {z['demande_insatisfaite_k']:>7.1f} k unités")
        print()

    if plan["stock_thermique_total_k"] > 0:
        print(f"  [CRITIQUE] Stock thermique total à écouler : {plan['stock_thermique_total_k']:.0f} k unités")
    else:
        print("  [OK] Stock thermique = 0 k. Transition COP32 possible dès T7.")

    if plan["alertes"]:
        print("\n  Alertes :")
        for a in plan["alertes"]:
            print(f"    {a}")

    print(f"\n{sep}")
    print("Fin de l'optimisation. Outil 100% consultatif — aucune écriture sur Cesim.")
    print(sep)


if __name__ == "__main__":
    main()
