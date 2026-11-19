# 📊 HISTORIQUE EXACT DES TOURS 0, 1 & 2, CONDITIONS DE MARCHÉ ET PROFIL DES 12 ÉQUIPES (`ESYBIA2AS`)

Ce fichier contient l'historique **100 % vérifié** à partir de [`data/real_competition/raw_reports/live_decisionchecklist.json`](file:///c:/Users/len/OneDrive/Bureau/ceism/data/real_competition/raw_reports/live_decisionchecklist.json) (capturé à 31 secondes de la fin du Tour 2) et des rapports officiels [`manuels/Results for Univers 1, Tour 1.html`](file:///c:/Users/len/OneDrive/Bureau/ceism/manuels/Results%20for%20Univers%201,%20Tour%201.html) et [`manuels/Results for Univers 1, Tour 2.html`](file:///c:/Users/len/OneDrive/Bureau/ceism/manuels/Results%20for%20Univers%201,%20Tour%202.html).

---

## 🌍 0. Historique des Conditions de Marché (Tour 1 ➔ Tour 2)

| Paramètre Macro / Marché | Tour 1 (`Période 1`) | Tour 2 (`Période 2`) | Ce qu'il faut vérifier en priorité au Tour 3 (`#/marketConditions`) |
| :--- | :--- | :--- | :--- |
| **Croissance Demande USA** | **`+3,0 %`** | **`+5,0 %`** | Lire le nouveau % annoncé pour les USA au Tour 3. |
| **Croissance Demande Chine** | **`+7,0 %`** | **`+8 % à +9 %`** (`8,0 %` saisi par `IronHorse`) | Lire le nouveau % annoncé pour la Chine au Tour 3. |
| **Croissance Demande Europe** | **`+6,0 %`** | **`+3,0 %`** | Lire le nouveau % annoncé pour l'Europe au Tour 3. |
| **Technologies Actives** | **Thermique** (~96 %) + début **Hybride** (~4 % chez 3 équipes) | **Thermique** (~91 %) + **Hybride** en forte hausse (11 équipes sur 12 vendent de l'Hybride au T2) | Vérifier la croissance Hybride et si l'**Électrique** démarre au Tour 3. |
| **Sous-traitance USA (Coût & Plafond)** | Thermique = **`12 383 $`** (affiché avec comp. T2) / Plafond = **`350 k`** | **CHOC :** Thermique bondit à **`13 694,3 $`** / Hybride = **`18 197,3 $`** / Plafond réduit à **`225 k`** | Vérifier dans `Production -> Planning` les nouveaux coûts et plafonds USA. |
| **Sous-traitance Chine (Coût & Plafond)** | Thermique = **`11 292 $`** / Plafond = **`425 k`** | Thermique = **`10 792 $`** / **Hybride = `17 014,6 $`** (contre `24 756 $ - 31 747 $` en interne !) / Plafond = **`450 k - 510 k`** | Vérifier le coût et le plafond de sous-traitance Chine pour l'Hybride au Tour 3 ! |
| **Taux de Change (`EUR` & `RMB`)** | `1 EUR = 1,1750 USD`<br>`1 USD = 6,6250 RMB` | **Hausse de +5 % de l'Euro :** `1 EUR = 1,2338 USD`<br>`1 USD = 6,6250 RMB` | Vérifier l'évolution de l'Euro et du RMB au Tour 3. |
| **Fiscalité (Impôt sur les sociétés)** | USA : `22 %` \| Chine : `25 %` \| Europe : `27 %` | **Baisse impôt Europe à `21 %` !** (USA : `22 %` \| Chine : `25 %`) | Vérifier si un taux d'impôt ou un droit de douane change au Tour 3. |
| **Coût d'Achat / Vente d'une Usine** | USA : **`1 200 M$`** (`200 k` cap.)<br>Chine : **`1 050 M$`** (`250 k` cap.) | USA : Achat **`1 200 M$`** / Cession **`+1 080 M$`**<br>Chine : Achat **`1 050 M$`** | Délai de construction = **2 tours (`t+2`)** : payée en `t+1`, produit en `t+2`. |
| **Modules Ouverts dans `Finance`** | Emprunt / Remboursement Dette à Long Terme uniquement | Dette à Long Terme + **Transferts internes (`USA → Chine (+), Chine → USA (-)` et `USA → Europe (+), Europe → USA (-)`)** *(Pas de dividendes ni rachats d'actions)* | Vérifier si Dividendes / Rachats d'actions s'ouvrent au Tour 3. |

---

## 📝 0.bis Récapitulatif Exact à 100 % des Décisions Soumises par `IronHorse` (`live_decisionchecklist.json`)

Voici les valeurs **exactes** qui ont été enregistrées dans la colonne d'équipe **`IronHorse`** au Tour 1 et au Tour 2 (telles qu'extraites de `live_decisionchecklist.json` et vérifiées dans `Results for Univers 1, Tour 2.html`) :

| Onglet / Paramètre | Décision `IronHorse` Tour 1 *(8e — 96 pts)* | Décision `IronHorse` Tour 2 *(1er — 140 pts)* | État Exact d'`IronHorse` au Début du Tour 3 |
| :--- | :--- | :--- | :--- |
| **Croissance Marché saisie (US / CN / EU)** | `3,0 %` / `7,0 %` / `6,0 %` | **`5,0 %` / `8,0 %` / `3,0 %`** | À mettre à jour selon `Conditions de marché` du Tour 3. |
| **PDM Estimées Thermique (US / CN / EU)** | `8,5 %` / `9,5 %` / `8,5 %` (Ventes réelles : `751k` / `582k` / `876k` = `2 209k`) | **`7,3 %` / `7,5 %` / `7,8 %`** (Ventes réelles : **`658 k` US + `574 k` CN + `838 k` EU = `2 070 k`**) | **`0 k` stock Thermique**, seulement `2 k` de demande insatisfaite en Europe. |
| **PDM Estimées Hybride (US / CN / EU)** | `0 %` / `0 %` / `0 %` (Non vendu) | **`1,1 %` / `1,1 %` / `0,8 %`** (Ventes réelles : **`76 k` US + `66 k` CN + `133 k` EU = `275 k`**) | **`0 k` stock Hybride**, `33 k` de demande insatisfaite aux USA (`109 k` demandés pour `76 k` livrés). |
| **Production Interne USA (8 usines = 1 600 k)** | `95,0 %` Thermique sur 7 usines (`1 330 k`) | **Ligne 1 (Thermique) = `64,0 %` (`1 024 k`)**<br>**Ligne 2 = `0,0 %` (vide)** | **8 usines USA disponibles (`1 600 k`)**. Comme le stock est à `0 k`, on peut remonter la Ligne 1 Thermique vers **`80 %–88 %`** ! |
| **Production Interne Chine (3 usines = 750 k)** | `95,0 %` Thermique sur 2 usines (`475 k`) | **Ligne 1 (Thermique) = `90,0 %` (`675 k`)**<br>**Ligne 2 (Hybride) = `0,0 %` (`0 k` en interne)** | **3 usines Chine disponibles (`750 k`)**. Ligne 1 Thermique déjà à `90 %`. |
| **Sous-traitance (USA & Chine)** | `350 k` Therm. USA + `425 k` Therm. Chine | **USA Ligne 1 & 2 = `0 k`**<br>**Chine Ligne 1 (Thermique) = `0 k`**<br>**Chine Ligne 2 (Hybride) = `275 k`** (à `17 014,6 $`/unité !) | Continuer à **sous-traiter l'Hybride en Chine** (`17 015 $` contre `24 756 $ - 31 747 $` en production interne !). |
| **Investissements Usines (USA / Chine)** | `+1` usine USA (`1 200 M$`) + `+1` usine Chine (`1 050 M$`) | **`0` usine USA / `0` usine Chine** (Estimations T3/T4 = `2 390` / `2 500`) | **8 usines USA + 3 usines Chine** au Tour 3. |
| **Achats (Fournisseurs actifs)** | *(Fermé — 5 fournisseurs par défaut)* | **3 cochés (`6 833,3 $`) :** `Maîtres Matérialistes` (Oui), `Composants Colossaux` (Oui), `Innovation Réinventée` (Oui).<br>**2 décochés :** `Singularités Quantiques` (Non), `Fusions Dynamiques` (Non). | **Attention :** 5 concurrents (`POLRAMOS`, `AURA`, `YANAUTO`, `GT-Auto`, `Vrooom`) n'ont coché que **`Composants Colossaux + Innovation Réinventée` (`6 000,0 $`, soit `-833,3 $/voiture`)** ! |
| **RH (Effectifs / Salaire / Formation)** | `5 000` ing. \| Départs `2,9 %` \| Salaire `5 500 $` \| Formation `900 $` | **`5 000` ing. \| Départs prévus `2,5 %` (réels `1,9 %`) \| Salaire `5 800 $` \| Formation `1 500 $`** | **Productivité `1,085` (#1 absolu du jeu = `12 pts/12`)** pour seulement `628 M$` de coût RH ! |
| **R&D (Jours-homme & Licences)** | **`120 000` Thermique / `1 130 000` Hybride / `0` Électrique** (`0` licence) | **`120 000` Thermique / `1 130 000` Hybride / `0` Électrique** (`0` licence) | **Capacités au Tour 3 :** **`7` équipements Thermiques**, **`4` équipements Hybrides**, et **`0` en Électrique** ! |
| **Marketing Thermique (Prix / Éq / Pub)** | US `20 500 $` (5 éq, 700M$) \| CN `130 000 RMB` (6 éq, 400M$) \| EU `23 000 €` (4 éq, 500M$) | **US : `20 500 $` / `5` éq / `800 M$`**<br>**CN : `130 000 RMB` / `6` éq / `450 M$`**<br>**EU : `22 500 €` / `4` éq / `600 M$`** | Nos `5 / 6 / 4` équipements sont pile au niveau de la moyenne du marché (`5,4 / 5,9 / 4,8`) et ont permis de tout vendre (`0` stock). |
| **Marketing Hybride (Prix / Éq / Pub)** | *(Non commercialisé)* | **US : `29 500 $` / `1` éq / `300 M$`**<br>**CN : `205 000 RMB` / `1` éq / `250 M$`**<br>**EU : `28 500 €` / `1` éq / `300 M$`** | Les `275 k` Hybrides ont été vendus à 100 % ! Au Tour 3, nous avons jusqu'à **`4` équipements Hybrides** débloqués. |
| **Logistique (Priorités de livraison)** | USA : `1. USA, 2. Europe, 3. Chine`<br>Chine : `1. Chine, 2. Europe, 3. USA` | USA : **`1. USA, 2. Europe, 3. Chine`**<br>Chine : **`1. Chine, 2. Europe, 3. USA`** | *(Aucun prix de cession modifiable dans l'interface : transferts au coût).* |
| **Finance (Dette LT & Transferts)** | Dette LT : `0` \| Transferts : *(Fermé)* | **Dette LT : `-4 000 000` k$ (`-4 000 M$`)**<br>**`USA → Chine (+)` : `+5 000 000` k$ (`+5 000 M$`)**<br>**`USA → Europe (+), Europe → USA (-)` : `-6 000 000` k$ (`-6 000 M$` rapatriés d'Europe vers USA !)** | **`23 935 M$` de trésorerie** (`7 602 M$` US, `7 033 M$` CN, `9 301 M$` EU), **`0 M$` découvert**, **`7 900 M$`** de dette LT restante. |

---

## 🏆 1. Résumé de notre Parcours (Tour d'Essai ➔ Tour 1 ➔ Tour 2)

1. **Tour d'Entraînement (`Période Test` — 13h00) :** **2e sur 12 avec `122 points`** (à 1 point du 1er `Jaune / Ça Roule` `123 pts`).
2. **Tour 1 (`Période 1` — 16h19) :** **8e sur 12 avec `96 points`** — La chute s'explique par la **surproduction (`2 580 k` pour `2 209 k` vendus ➔ `371 k` voitures invendues en stock = `2 pts / 12`)** et le **découvert bancaire en Chine (`3 623 M$`, `4 pts / 12` en Indépendance Financière)** qui en a découlé. *(Les `5 / 6 / 4` équipements n'en étaient pas la cause : ils nous avaient même rapporté `11 pts / 12` sur la Part de marché Asie !)*
3. **Tour 2 (`Période 2` — 17h15) :** **1er estimé de l'Univers 1 avec `140 points` !**
   - **Résultat Net Annuel :** **`10 774 M$`** (**#1 ABSOLU sur les 12 équipes** — exactement conforme à la prévision de `10 775 465 k$` affichée dans `live_decisionchecklist.json` !).
   - **Stocks Finaux :** **`0 k` voiture en stock** (`11 pts / 12` #1 ex-aequo avec `Ren'Auto`). Les `371 k` voitures en stock du Tour 1 ont été écoulées à 100 % ET les `275 k` Hybrides sous-traités en Chine ont été vendus à 100 % !
   - **Découvert Bancaire :** **`0 M$` partout** grâce au transfert de `-6 000 M$` (`Europe → USA`) et `+5 000 M$` (`USA → Chine`).
   - **Indépendance Financière (`Ratio des fonds propres`) :** **`74,66 %`** (`10 pts / 12`, notation de crédit **`AA-`**).
   - **Productivité des Ingénieurs :** **`1,085`** (**#1 ABSOLU sur les 12 équipes = `12 pts / 12`**).

---

## 📋 2. Tableau Complet des 15 Critères et Classement Estimé du Tour 2 (12 Équipes)

| Critère (Points de 1 à 12) | `IronHorse` (1er) | `POLRAMOS` (2e) | `BM2P` (3e) | `Ça Roule` (4e) | `GT-Auto` (5e) | `YANAUTO` (6e) | `Ren'Auto` (7e) | `AURA` (8e) | `TABCHOUR` (9e) | `MO'THOR` (10e) | `tomobil` (11e) | `Vrooom` (12e) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. ROE (%)** | **48,61% (11p)** | 46,63% (10p) | 44,50% (8p) | 35,63% (5p) | 45,57% (9p) | 42,85% (7p) | 49,55% (12p) | 29,76% (4p) | 41,18% (6p) | 17,67% (3p) | 4,00% (2p) | 2,38% (1p) |
| **2. Création Valeur** | **50 519 (10p)** | 48 777 (9p) | 47 229 (8p) | 56 659 (11p) | 44 150 (4p) | 36 428 (2p) | 78 876 (12p) | 42 362 (3p) | 45 829 (6p) | 45 234 (5p) | 45 501 (7p) | 25 800 (1p) |
| **3. Indép. Fin. (%)** | **74,66% (10p)** | 95,32% (12p) | 61,91% (6p) | 63,79% (8p) | 59,67% (4p) | 70,86% (9p) | 62,97% (7p) | 59,82% (5p) | 75,64% (11p) | 46,73% (2p) | 33,53% (1p) | 56,86% (3p) |
| **4. Marge US (%)** | **5,87% (8p)** | 7,62% (10p) | 4,96% (7p) | 3,84% (6p) | 7,12% (9p) | 10,15% (11p) | 2,05% (5p) | -0,39% (3p) | 10,20% (12p) | -7,78% (1p) | -1,94% (2p) | 1,01% (4p) |
| **5. Marge Asie (%)** | **9,11% (8p)** | 9,55% (9p) | 8,05% (6p) | 4,84% (3p) | 16,44% (11p) | 11,09% (10p) | 6,29% (5p) | 8,92% (7p) | 17,14% (12p) | -23,31% (1p) | 5,82% (4p) | 3,07% (2p) |
| **6. Marge Europe (%)** | **38,47% (11p)** | 36,74% (9p) | 34,07% (6p) | 27,54% (4p) | 37,90% (10p) | 42,85% (12p) | 25,97% (3p) | 35,32% (8p) | 34,80% (7p) | 33,77% (5p) | 13,83% (2p) | 13,07% (1p) |
| **7. PDM US/Glob (%)** | **9,15% (9p)** | 8,32% (6p) | 8,50% (7p) | 11,00% (11p) | 7,55% (5p) | 6,26% (2p) | 11,80% (12p) | 6,95% (4p) | 6,56% (3p) | 8,87% (8p) | 9,29% (10p) | 5,73% (1p) |
| **8. PDM Asie (%)** | **9,39% (9p)** | 8,50% (6p) | 8,64% (7p) | 13,27% (12p) | 7,42% (4p) | 6,12% (3p) | 12,35% (11p) | 8,64% (8p) | 4,52% (2p) | 1,12% (1p) | 12,28% (10p) | 7,76% (5p) |
| **9. PDM Europe (%)** | **10,22% (10p)** | 9,45% (7p) | 10,39% (11p) | 10,84% (12p) | 9,38% (6p) | 7,35% (4p) | 9,50% (8p) | 5,92% (3p) | 8,11% (5p) | 10,09% (9p) | 5,72% (2p) | 3,04% (1p) |
| **10. Dem. Insat. (k)** | **35 k (7p)** | 0 k (8p) | 0 k (8p) | 335 k (5p) | 0 k (8p) | 0 k (8p) | 351 k (4p) | 118 k (6p) | 0 k (8p) | 466 k (3p) | 1 055 k (1p) | 917 k (2p) |
| **11. Stocks (k)** | **0 k (11p)** | 322 k (8p) | 531 k (7p) | 10 k (10p) | 774 k (3p) | 837 k (2p) | 0 k (11p) | 627 k (6p) | 1 019 k (1p) | 243 k (9p) | 645 k (5p) | 738 k (4p) |
| **12. Coût Unit. US** | **12 964$ (8p)** | 12 449$ (10p) | 13 200$ (7p) | 14 995$ (3p) | 14 182$ (6p) | 12 350$ (11p) | 15 377$ (1p) | 11 760$ (12p) | 15 041$ (2p) | 14 705$ (5p) | 15 199$ (2p*) | 12 873$ (9p) |
| **13. Coût Unit. Asie** | **11 345$ (8p)** | 11 223$ (11p) | 11 575$ (6p) | 12 461$ (3p) | 11 229$ (10p) | 10 833$ (12p) | 14 680$ (1p) | 11 385$ (7p) | 14 017$ (2p) | 12 060$ (5p) | 12 349$ (4p) | 11 277$ (9p) |
| **14. Coût Unit. Eur.** | **12 336$ (8p)** | 11 882$ (11p) | 13 131$ (7p) | 13 793$ (5p) | 12 177$ (10p) | 12 233$ (9p) | 14 701$ (4p) | 11 429$ (12p) | 14 708$ (3p) | 14 040$ (5p*) | 16 794$ (2p) | 17 174$ (1p) |
| **15. Productivité** | **1,085 (12p)** | 1,038 (7p) | 1,055 (8p) | 1,033 (6p) | 1,031 (5p) | 1,013 (1p) | 1,017 (2p) | 1,069 (10p) | 1,030 (3p) | 1,080 (11p) | 1,030 (3p) | 1,080 (11p) |
| **TOTAL TOUR 2** | **🥇 140 pts** | **🥈 133 pts** | **🥉 109 pts** | **104 pts** | **104 pts** | **103 pts** | **98 pts** | **96 pts** | **90 pts** | **68 pts** | **57 pts** | **54 pts** |
| **DÉCOUVERT (M$)** | **`0 M$`** | `0 M$` | `2 291 M$` | `0 M$` | `6 009 M$` | `10 098 M$` | `0 M$` | `3 814 M$` | `6 905 M$` | `5 200 M$` | `10 130 M$` | `9 765 M$` |
