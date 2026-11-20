"""Tests de non-régression basés sur les exports et le classement officiel fourni."""
from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "03_outils_et_scripts" / "calculateur_classement_astien.py"
REPORTS = ROOT / "04_rapports_tours"


class OfficialRankingRegressionTests(unittest.TestCase):
    def run_report(self, tour: int) -> str:
        report = REPORTS / f"tour_{tour:02d}_resultats_univers1.xls"
        return subprocess.check_output(
            [sys.executable, str(SCRIPT), str(report)], text=True, cwd=ROOT
        )

    def team_points(self, output: str, team: str) -> int:
        match = re.search(rf"^#\s*\d+\s+\|\s+{re.escape(team)}\s+\|\s+(\d+) pts", output, re.M)
        self.assertIsNotNone(match, f"Équipe {team} absente du classement")
        return int(match.group(1))

    def test_ironhorse_official_totals_periods_2_to_5(self):
        expected = {2: 156, 3: 122, 4: 128, 5: 145}
        for tour, points in expected.items():
            with self.subTest(tour=tour):
                self.assertEqual(self.team_points(self.run_report(tour), "IronHorse"), points)

    def test_period_5_all_12_official_totals(self):
        # Ordre des équipes dans le tableau officiel P5, page 6 du PDF fourni.
        expected = {
            "Ren'Auto": 143, "AURA": 124, "IronHorse": 145, "YANAUTO": 139,
            "tomobil": 145, "GT-Auto VI": 137, "Vrooom": 150, "POLRAMOS": 66,
            "Ça Roule": 133, "BM2P": 94, "TABCHOUR": 134, "MO'THOR": 134,
        }
        output = self.run_report(5)
        for team, points in expected.items():
            with self.subTest(team=team):
                self.assertEqual(self.team_points(output, team), points)

    def test_period_5_is_22_criteria_and_tsr_is_present(self):
        output = self.run_report(5)
        self.assertIn("22 CRITÈRES", output)
        self.assertIn("Rentabilité de l'action / TSR (%)", output)
        self.assertIn("27.86 ( 7/12 pts)", output)

    def test_period_1_known_unresolved_difference_is_not_hidden(self):
        # Le calcul de la source XLS donne 98 ; le PDF officiel P1 affiche 96.
        # Ce test documente l'écart sans inventer une règle de correction.
        self.assertEqual(self.team_points(self.run_report(1), "IronHorse"), 98)

    def test_default_execution_resolves_latest_round(self):
        # L'exécution sans argument doit résoudre automatiquement le dernier rapport (Tour 5)
        output = subprocess.check_output(
            [sys.executable, str(SCRIPT)], text=True, cwd=ROOT
        )
        self.assertIn("tour_05_resultats_univers1.xls", output)
        self.assertIn("22 CRITÈRES", output)

    def test_strict_to_float_validation(self):
        # Vérifie que to_float lève ValueError sur une chaîne invalide et gère les espaces
        sys.path.insert(0, str(ROOT / "03_outils_et_scripts"))
        from calculateur_classement_astien import to_float

        self.assertEqual(to_float(""), 0.0)
        self.assertEqual(to_float("   "), 0.0)
        self.assertEqual(to_float(None), 0.0)
        self.assertAlmostEqual(to_float("1 234,56"), 1234.56)
        self.assertAlmostEqual(to_float("1\u00a0234,56"), 1234.56)
        self.assertAlmostEqual(to_float("15.5%"), 15.5)
        with self.assertRaises(ValueError):
            to_float("invalide_non_vide")

    def test_analyseur_concurrence_runs_and_has_regional_breakdown(self):
        # Vérifie que l'analyseur s'exécute et produit la décomposition régionale
        analyser_script = ROOT / "03_outils_et_scripts" / "analyseur_concurrence_et_decisions.py"
        output = subprocess.check_output(
            [sys.executable, str(analyser_script)], text=True, cwd=ROOT
        )
        self.assertIn("RADAR CONCURRENCE & CAPACITÉS", output)
        self.assertIn("ÉQUIPEMENTS PAR RÉGION", output)
        self.assertIn("IronHorse (NOUS)", output)


class EdgeCaseTests(unittest.TestCase):
    """P0 — Tests des cas limites (bascule critères, ex æquo, fichier manquant)."""

    def setUp(self):
        sys.path.insert(0, str(ROOT / "03_outils_et_scripts"))

    def test_criteria_auto_detection_per_tour(self):
        """Le calculateur doit retourner 15/17/21/22 critères selon le tour."""
        expected_headers = {
            1: "15 CRITÈRES",
            2: "17 CRITÈRES",
            3: "21 CRITÈRES",
            5: "22 CRITÈRES",
        }
        for tour, header in expected_headers.items():
            report = REPORTS / f"tour_{tour:02d}_resultats_univers1.xls"
            if not report.exists():
                self.skipTest(f"Rapport tour {tour} absent")
            output = subprocess.check_output(
                [sys.executable, str(SCRIPT), str(report)], text=True, cwd=ROOT
            )
            with self.subTest(tour=tour):
                self.assertIn(header, output, f"Tour {tour} devrait avoir {header}")

    def test_exaequo_get_same_points(self):
        """Deux équipes avec la même valeur sur un critère doivent avoir le même score."""
        import importlib
        calc = importlib.import_module("calculateur_classement_astien")
        # 12 équipes, 2 d'entre elles ex æquo à 100.0 en position 0 et 1
        vals = [100.0, 100.0, 90.0, 85.0, 80.0, 75.0, 70.0, 65.0, 60.0, 55.0, 50.0, 45.0]
        scores = calc.score_higher_better(vals)
        # Les 2 premières (ex æquo à 100.0) doivent avoir le même score
        self.assertEqual(scores[0], scores[1], "Les ex æquo doivent avoir strictement le même score")
        # Les autres doivent être inférieurs
        self.assertGreater(scores[0], scores[2])

        # Même logique pour score_lower_better
        vals_low = [10.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 110.0]
        scores_low = calc.score_lower_better(vals_low)
        self.assertEqual(scores_low[0], scores_low[1], "Les ex æquo lower_better doivent avoir le même score")
        self.assertGreater(scores_low[0], scores_low[2])

    def test_missing_file_raises_explicit_error(self):
        """Un fichier inexistant doit provoquer une sortie non-zéro avec message explicite."""
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "fichier_qui_nexiste_pas.xls"],
            text=True,
            cwd=ROOT,
            capture_output=True,
        )
        self.assertNotEqual(result.returncode, 0, "Doit échouer sur fichier inexistant")
        combined = result.stdout + result.stderr
        self.assertTrue(
            "introuvable" in combined.lower() or "not found" in combined.lower(),
            f"Message d'erreur attendu, obtenu : {combined[:200]}"
        )

    def test_tsr_raises_on_zero_previous_price(self):
        """calculate_shareholder_return doit lever ValueError si cours_t-1 <= 0."""
        import importlib
        calc = importlib.import_module("calculateur_classement_astien")

        # Simuler des lignes avec cours précédent nul pour la 1ère équipe
        def make_line(label, values):
            return label + " | " + " | ".join(str(v) for v in values)

        current_lines = [
            make_line("Cours de l'action à la fin du tour", [100.0] * 12),
            make_line("Dividendes", [-5000.0] * 12),
            make_line("Actions sur le marché à la fin du tour", [1000.0] * 12),
        ]
        previous_lines = [
            # Cours précédent = 0 → doit lever ValueError
            make_line("Cours de l'action à la fin du tour", [0.0] + [80.0] * 11),
        ]
        with self.assertRaises(ValueError):
            calc.calculate_shareholder_return(current_lines, previous_lines)


class OptimiseurTests(unittest.TestCase):
    """P2 — Tests du simulateur décisionnel."""

    def setUp(self):
        sys.path.insert(0, str(ROOT / "03_outils_et_scripts"))

    def test_optimiseur_dividende_ne_genere_pas_de_decouvert(self):
        """Le dividende optimal ne doit jamais créer de découvert dans aucune zone."""
        import importlib
        opt = importlib.import_module("optimiseur_decisions_tour")

        result = opt.optimise_dividende_tsr(
            cash_usa=20000.0,
            cash_chine=15000.0,
            cash_europe=9000.0,
            actions=1621.9,
            cours_precedent=163.57,
            cap_propres=52000.0,
            net_income=16630.0,
            tsr_concurrents=None,
            min_cash_reserve=2000.0,
            pas_mds=1000.0,
        )
        self.assertGreaterEqual(result["cash_usa_post"], 0.0, "Cash USA post-dividende négatif")
        self.assertGreaterEqual(result["cash_europe_post"], 0.0, "Cash Europe post-transfert négatif")
        self.assertGreater(result["dividende_mds"], 0.0, "Dividende doit être positif")
        self.assertGreater(result["pts_tsr"], 0, "Points TSR doit être > 0")
        self.assertLessEqual(result["pts_tsr"], 12, "Points TSR doit être ≤ 12")

    def test_planifier_cop32_zero_stock_thermique(self):
        """Le plan COP32 est valide quand le stock thermique est déjà nul."""
        import importlib
        opt = importlib.import_module("optimiseur_decisions_tour")

        plan = opt.planifier_basculement_cop32(
            usines_usa=9,
            usines_chine=6,
            stock_thermique_usa=0.0,
            stock_thermique_chine=0.0,
            demande_hybride_usa=350.0,
            demande_ev_usa=150.0,
            demande_h2_usa=80.0,
            demande_hybride_chine=300.0,
            demande_ev_chine=200.0,
            demande_h2_chine=50.0,
            h2_debloque=True,
            sous_traitance_max_usa=525.0,
            sous_traitance_max_chine=525.0,
        )
        self.assertEqual(plan["stock_thermique_total_k"], 0.0)
        # Vérifier qu'aucune alerte critique n'est levée pour le thermique
        alerts_critiques = [a for a in plan["alertes"] if "CRITIQUE" in a and "thermique" in a.lower()]
        self.assertEqual(len(alerts_critiques), 0, f"Alertes inattendues : {alerts_critiques}")
        # Capacité usa = 9 usines × 200k = 1800k
        self.assertEqual(plan["usa"]["capacite_interne_k"], 1800)

    def test_tsr_zero_cours_precedent_raises(self):
        """calculer_tsr doit lever ValueError si cours_precedent <= 0."""
        import importlib
        opt = importlib.import_module("optimiseur_decisions_tour")
        with self.assertRaises(ValueError):
            opt.calculer_tsr(cours_actuel=200.0, cours_precedent=0.0,
                             dividende_mds=10000.0, actions=1621.9)

    def test_calibrateur_runs_without_crash(self):
        """Le calibrateur doit s'exécuter sans erreur sur les rapports T1-T5."""
        calib_script = ROOT / "03_outils_et_scripts" / "calibrateur_elasticites_marche.py"
        result = subprocess.run(
            [sys.executable, str(calib_script)],
            text=True,
            cwd=ROOT,
            capture_output=True,
        )
        combined = result.stdout + result.stderr
        # Doit produire une sortie et se terminer avec succès
        self.assertEqual(result.returncode, 0, f"Calibrateur a planté:\n{combined[:500]}")
        self.assertIn("CALIBRATION LOGIT", combined)
        self.assertIn("MISE EN GARDE STATISTIQUE", combined)


    def test_horizon_tour_10_endgame_rules(self):
        """L'analyseur de fin de partie doit interdire les usines au T9/T10 et alerter au T10."""
        import importlib
        opt = importlib.import_module("optimiseur_decisions_tour")

        recos_t9 = opt.analyser_regles_fin_de_partie(9, total_rounds=10)
        self.assertTrue(any("INTERDICTION STRICTE" in r and "usine" in r.lower() for r in recos_t9))

        recos_t10 = opt.analyser_regles_fin_de_partie(10, total_rounds=10)
        self.assertTrue(any("TOUR 10" in r and "stocks" in r.lower() for r in recos_t10))
        self.assertTrue(any("dividendes" in r.lower() for r in recos_t10))


if __name__ == "__main__":
    unittest.main(verbosity=2)
