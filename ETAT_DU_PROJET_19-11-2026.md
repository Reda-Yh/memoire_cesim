# État du projet IronHorse — 19/11/2026

## Objectif
Aider IronHorse à maximiser ses chances de gagner Cesim Global Challenge Automotive w/ ESG (Bordeaux INP, ESYBIA2AS, Univers 1), en priorisant la fiabilité des données et l'optimisation du barème officiel d'Eric Astien. Aucun script ne doit enregistrer/soumettre des décisions sur Cesim.

## Modifications réellement effectuées

### 1. Calculateur `03_outils_et_scripts/calculateur_classement_astien.py`
- Ajout du 22e critère à partir du Tour 5 : rentabilité de l'action / TSR.
- Le TSR est calculé comme `((cours_t - cours_t-1 + dividende_par_action) / cours_t-1) * 100`.
- Le dividende par action est calculé depuis la ligne `Dividendes` (flux négatif en M USD) et `Actions sur le marché à la fin du tour` (millions d'actions).
- Le rapport du tour précédent est recherché dans le même dossier. S'il manque, le calcul du TSR s'arrête avec un message d'erreur au lieu d'inventer une valeur.
- Le mode `--criteria` accepte 15, 17, 21 et 22.
- Suppression du départage arbitraire des ex æquo par le découvert : le score reste celui du barème, et l'ordre d'affichage entre équipes à égalité n'est pas présenté comme un départage officiel.
- Une chaîne non vide qui ne peut pas être convertie en nombre provoque désormais une erreur explicite plutôt qu'un zéro silencieux.

### 2. Analyseur `03_outils_et_scripts/analyseur_concurrence_et_decisions.py`
- Les équipements sont maintenant conservés et affichés séparément pour USA, Chine et Europe.
- L'ancien maximum régional est conservé uniquement comme indicateur de compatibilité pour le radar synthétique ; le détail par région est affiché pour éviter les interprétations trompeuses.
- L'outil reste un radar descriptif. Ses seuils de diagnostic ne sont pas des probabilités ni un modèle prédictif validé.

### 3. Documentation et mémoire
- README, prompt maître, index, barème et `live_game_history.json` actualisés pour le résultat officiel T5 et le barème à 22 critères.
- Ajout des images de pages du classement officiel P4/P5 disponibles dans la conversation. Le PDF source complet P4/P5 n'était pas présent dans l'archive d'origine ; les images sont explicitement identifiées comme copies de pages, pas comme PDF original.
- Les décisions T6 restent des snapshots de décisions, pas un résultat officiel T6.

### 4. Calibrateur Logit `03_outils_et_scripts/calibrateur_elasticites_marche.py` (P1)
- Analyse empirique des 5 tours fermés (T1 à T5, 180 observations = 12 équipes × 3 régions).
- Estimation en Python standard pur (moindres carrés OLS matriciels par élimination de Gauss 3×3) du modèle log-linéaire : $\ln(PDM) = \text{const} + \alpha \ln(1/\text{Prix}) + \gamma \ln(\text{Pub}+1)$.
- Résultats réels obtenus :
  - Global : $\alpha = 0.6236$, $\gamma = 0.1168$, $R^2 = 0.0983$.
  - USA : $\alpha = 0.4350$, $\gamma = 0.2235$, $R^2 = 0.1064$.
  - Chine : $\alpha = 0.7327$, $\gamma = 0.0049$, $R^2 = 0.1746$ (très forte sensibilité au prix).
  - Europe : $\alpha = 0.6661$, $\gamma = 0.1316$, $R^2 = 0.1320$.

### 5. Optimiseur Décisionnel `03_outils_et_scripts/optimiseur_decisions_tour.py` (P2)
- Module 0 : Stratégie d'atterrissage & horizon fixe (Tour 10). Analyse des délais de latence (Capex usines = 2 tours $\implies$ interdiction formelle d'usines aux tours 9 et 10, déstockage total à 0 k au Tour 10, dividendes massifs finaux).
- Module 1 : Optimisation mathématique du dividende sous contrainte stricte de liquidité ($Découvert = 0$ dans les 3 zones), avec calibrage du ratio $PER \approx 16$ sur données réelles d'IronHorse T5.
- Module 2 : Planification du basculement industriel COP 32 pour le Tour 7 (conversion des 9 usines USA et 6 usines Chine vers Hybride/EV/H2, alerte critique si stock thermique résiduel $> 0$).

## Vérifications effectuées

Commande : `python -m unittest discover -s 03_outils_et_scripts/tests -v` — 16 tests réussis (100% pass en ~2.4s).
- Tests d'intégrité officielle T2 à T5 validés.
- Tests des cas limites (edge cases) : bascule automatique 15/17/21/22 critères, ex æquo parfaits, gestion explicite des erreurs (fichiers absents, division par zéro cours/actions).
- Tests de non-régression de l'optimiseur et du calibrateur.

- IronHorse : T2 = 156, T3 = 122, T4 = 128, T5 = 145 points.
- T5 : totaux des 12 équipes reproduits exactement par rapport à la page officielle P5 fournie.
- T5 IronHorse : TSR = 27,86 %, score = 7 points ; total = 145 points.
- Analyseur concurrence exécuté sur le rapport T5 — terminé.
- Lecteur HTML exécuté sur les événements T5, filtre batteries — terminé.

## Anomalie connue non résolue
- Tour 1 : calcul depuis l'export XLS = 98 points IronHorse ; classement PDF officiel = 96.
- Cette différence est documentée et testée comme anomalie. Aucune règle n'a été inventée pour forcer le résultat à 96.

## Limites restantes — ne pas les masquer
- Pas de nouveau modèle ML entraîné : les données historiques disponibles (cinq tours seulement) ne suffisent pas à justifier un prédicteur fiable des décisions concurrentes ou des ventes futures.
- Le modèle d'élasticité commercial existant doit être recalibré avec un protocole hors-échantillon, mais aucun nouveau coefficient n'a été inventé ni injecté.
- Pas d'accès navigateur Cesim live exécuté dans cette session ; les variables de l'interface live doivent être confirmées par un export/capture fourni par l'utilisateur.
- Le résultat officiel T6 n'est pas fourni.
- Les tests de classement couvrent l'exactitude des totaux historiques disponibles ; ils ne garantissent pas les résultats futurs ni la victoire finale.

## Commandes rapides
Depuis la racine du dépôt :

```bash
python 03_outils_et_scripts/calculateur_classement_astien.py 04_rapports_tours/tour_05_resultats_univers1.xls
python 03_outils_et_scripts/analyseur_concurrence_et_decisions.py 04_rapports_tours/tour_05_resultats_univers1.xls
python 03_outils_et_scripts/lecteur_html_cesim.py 06_conditions_marche_et_evenements/tour_05_evenements.html --filter batteries
python -m unittest discover -s 03_outils_et_scripts/tests -v
```

## Intégrité
Les copies originales des trois scripts sont conservées dans `03_outils_et_scripts/originals/`. L'archive RAR source n'a pas été modifiée.
