# 📊 HISTORIQUE COMPLET DES TOURS 0, 1 & 2, CONDITIONS DE MARCHÉ ET PROFIL DES 12 ÉQUIPES (`ESYBIA2AS`)

Ce fichier contient la mémoire factuelle complète de notre parcours dans l'**Univers 1 (`ESYBIA2AS`)** du Tour d'entraînement jusqu'à la fin du **Tour 2**, y compris **l'historique exact des Conditions de Marché de chaque tour et de toutes nos décisions passées**.

---

## 🌍 0. Historique des Conditions de Marché (Tour d'Essai ➔ Tour 1 ➔ Tour 2)

> [!WARNING]
> **Rappel pour l'Agent IA :** Les conditions de marché changent **à chaque tour** ! Voici comment elles ont évolué jusqu'ici pour que tu comprennes la dynamique du scénario d'Eric Astien et que tu compares avec les nouvelles **Conditions de marché du Tour 3** :

| Paramètre Macro / Marché | Tour 1 (`Période 1`) | Tour 2 (`Période 2`) | Ce qu'il faut vérifier en priorité au Tour 3 (`#/marketConditions`) |
| :--- | :--- | :--- | :--- |
| **Croissance Demande USA** | **`+3,0 %`** | **`+5,0 %`** (accélération) | Lire le nouveau % annoncé pour les USA au Tour 3. |
| **Croissance Demande Chine** | **`+7,0 %`** | **`+8 % à +9 %`** (`8,5 %` retenu) | Lire le nouveau % annoncé pour la Chine au Tour 3. |
| **Croissance Demande Europe** | **`+6,0 %`** | **`+3,0 %`** (ralentissement) | Lire le nouveau % annoncé pour l'Europe au Tour 3. |
| **Technologies Actives** | **Thermique** (~96 %) + début **Hybride** (~4 % chez 3 équipes) | **Thermique** (~91 %) + **Hybride** en forte hausse (`7,2 %` USA, `8,6 %` Chine, `6,1 %` Europe) | Vérifier l'essor de l'**Hybride** et si la demande **Électrique** démarre au Tour 3 ! |
| **Sous-traitance USA (Coût & Plafond)** | Coût = **`11 233 $`** (`12 383 $` avec comp. T2) / Plafond = **`350 k`** | **CHOC :** Coût bondit à **`13 694,3 $`** (plus cher que nos usines !) / Plafond réduit à **`225 k`** | Vérifier dans `Production -> Planning` si la sous-traitance USA reste hors de prix ou baisse. |
| **Sous-traitance Chine (Coût & Plafond)** | Coût = **`11 292 $`** / Plafond = **`425 k`** | Thermique = **`10 792 $`** / Hybride = **`16 833 $`** / Plafond = **`510 k`** | Vérifier le nouveau plafond et coût de sous-traitance Chine (Thermique / Hybride / Électrique). |
| **Taux de Change (`EUR` & `RMB`)** | `1 EUR = 1,1750 USD`<br>`1 USD = 6,6250 RMB` | **Hausse de +5 % de l'Euro :** `1 EUR = 1,2338 USD`<br>`1 USD = 6,6250 RMB` | Vérifier l'évolution de l'Euro et du RMB au Tour 3. |
| **Fiscalité (Impôt sur les sociétés)** | USA : `22 %` \| Chine : `25 %` \| Europe : `27 %` | **Baisse impôt Europe à `21 %` !** (USA : `22 %` \| Chine : `25 %`) | Vérifier si un taux d'impôt ou un droit de douane change au Tour 3. |
| **Nouveaux Modules Débloqués** | Ouverture de **RH**, **R&D** et **Finance (Dette LT)** | Ouverture de **Production -> Achats (5 Fournisseurs ESG + boycott ONG de Singularités Quantiques)** et **Finance -> Transferts internes de trésorerie** | Vérifier si Dividendes / Rachat d'actions ou un nouveau module s'active au Tour 3 ! |

---

## 📝 0.bis Récapitulatif Exact de Nos Décisions Soumises (Tour 1 vs Tour 2)

| Onglet / Paramètre | Notre Décision Tour 1 *(8e — 96 pts)* | Notre Décision Tour 2 *(1er — 140 pts)* | État Initial au Début du Tour 3 |
| :--- | :--- | :--- | :--- |
| **Demande Thermique (USA / Chine / Eur)** | `8,5 %` / `9,5 %` / `8,5 %` (`2 580 k` prévus vs `2 209 k` vendus) | `8,5 %` / `9,2 %` / `8,5 %` (Ventes réelles : `659 k` US + `573 k` CN + `857 k` EU = **`2 089 k`**) | Marché Thermique bien calibré, **`0 k` stock** restant. |
| **Demande Hybride (USA / Chine / Eur)** | `0 %` / `0 %` / `0 %` (Non commercialisé) | `9,5 %` / `10,0 %` / `15,0 %` (Ventes réelles : `68 k` US + `57 k` CN + `111 k` EU = **`236 k`**) | **`0 k` stock Hybride**, 3 équipements Hybrides débloqués pour le Tour 3. |
| **Prod. Interne USA (8 usines = 1 600 k)** | `95 %` sur 7 usines (`1 330 k` net) | **`64,0 %` Thermique** (`979 k` net) + **`3,0 %` Hybride** (`45 k` net) *(bridé pour vider le stock T1)* | **8 usines USA disponibles** : à remonter à **`88 %–92 %`** au Tour 3 ! |
| **Prod. Interne Chine (3 usines = 750 k)** | `95 %` sur 2 usines (`475 k` net) | **`90,0 %` Thermique** (`631 k` net) + `0 %` Hybride | **3 usines Chine disponibles** : à maintenir à **`90 %–94 %`** au Tour 3. |
| **Sous-traitance (USA / Chine)** | `350 k` Therm. USA + `425 k` Therm. Chine (`775 k`) | **`0 k` USA** + **`0 k` Therm. Chine** + **`85 k` Hybride Chine** | Ajuster selon le besoin exact pour garder `0 k` stock. |
| **Achats Usines (USA / Chine)** | `+1` usine USA (`600 M$`) + `+1` usine Chine (`475 M$`) | `0` usine USA + `0` usine Chine | Parc actuel : **8 usines USA + 3 usines Chine**. |
| **Achats Fournisseurs ESG** | *(Fermé — 5 fournisseurs par défaut = `7 150 $`)* | **3 cochés :** `Composants Colossaux` + `Innovation Réinventée` + `Maîtres Matérialistes` (**`6 833,3 $`**) | `Singularités Quantiques` et `Fusions Dynamiques` décochés. |
| **RH (Effectifs / Salaire / Formation)** | `5 000` ing. / `5 500 $` / `900 $` (Productivité `1,035`) | `5 000` ing. / **`5 600 $`** / **`1 000 $`** (**Productivité `1,085` #1 du jeu !**) | Départs volontaires réels au T2 = **`2,4 %`**. |
| **R&D (Therm. / Hybride / Élec.)** | `120 000` Therm. / `1 130 000` Hybride (`100 %`) | **`200 000` Therm. / `550 000` Hybride / `500 000` Électrique (`100 %`)** | **Capacités au T3 :** `9` éq. Thermique, `3` éq. Hybride, `500k` j-h déjà acquis en Électrique. |
| **Marketing Thermique (Prix & Éq.)** | US `20 500 $` (5 éq) \| CN `130 000 RMB` (6 éq) \| EU `23 000 €` (4 éq) | US **`20 500 $` (5 éq)** \| CN **`125 000 RMB` (6 éq)** \| EU **`22 000 €` (4 éq)** | Réduire les équipements Thermiques vers **`4 / 4 / 3`** ou **`4 / 5 / 3`** au T3 pour booster les marges. |
| **Marketing Hybride (Prix & Éq.)** | *(Aucun)* | US **`32 800 $` (2 éq)** \| CN **`228 000 RMB` (2 éq)** \| EU **`34 200 €` (2 éq)** | **3e équipement Hybride** débloqué pour le Tour 3 ! |
| **Finance (Dette LT & Transferts)** | Dette LT `0` \| Aucun transfert (`3 623 M$` découvert Chine) | **Dette LT `-4 000 M$`** \| **Transfert Europe -> USA `+6 000 M$`** \| **USA -> Chine `+5 000 M$`** | **`23 935 M$` de cash**, **`0` découvert**, seulement **`7 900 M$`** de dette LT restante ! |

---

## 🏁 1. Tour d'Entraînement (`Période Test` — Mercredi 13h00)
- **Score officiel d'`IronHorse` (alors `Bleu`) :** **2e sur 12 avec `122 points`** (à 1 seul point du 1er `Jaune / Ça Roule` à `123 pts`, devant `Rose` `119 pts` et `Marron` `118 pts`).
- **Ce qui avait fonctionné :**
  - `0 k` stock (`7 pts/12`), `23 k` demande insatisfaite, productivité ingénieurs `1,0253` (`11 pts/12`), coûts moyens unitaires très bas (`12 296 $` US, `10 407 $` Asie #1 ex-aequo = `11 pts/12`, `11 742 $` Europe = `9 pts/12`), ROE `58,15 %`, Résultat net `8 751 M$`.

---

## 📉 2. Tour 1 (`Période 1` — Mercredi 16h19) : L'Erreur et la Chute à la 8e Place (96 pts)
- **Score officiel d'`IronHorse` (`Bleu`) :** **8e sur 12 avec `96 points`** (le 1er `Rose / Vrooom Vroooom` a fait `108 pts`, `Marron / TABCHOUR` 2e avec `106 pts`, `GT-Auto VI` 3e avec `105 pts`, `Orange / YANAUTO` 4e avec `104 pts`).
- **Pourquoi nous avions chuté (la décision soumise par Yahya au Tour 1) :**
  1. **Surenchère d'équipements (`5` USA / `6` Chine / `4` Europe) :** Nos coûts d'équipements ont explosé à **`7 525 M$`** (contre `4 076 M$` chez le 1er `Rose` qui avait mis `3 / 4 / 2` équipements !). Cela a écrasé nos marges opérationnelles (`6 pts` US, `4 pts` Asie, `6 pts` Europe).
  2. **Prix trop hauts (`20 500 $ / 130 000 RMB / 23 000 €`) + Production maximale (`2 580 k` voitures) :** Nous n'avons vendu que `2 209 k` voitures (`751 k` USA + `582 k` Chine + `876 k` Europe). Il nous est resté **`371 k` voitures invendues en stock** (`53 k` aux USA + `318 k` en Chine) ➔ **`2 points sur 12` en Stocks** et **`4,41 milliards $`** de cash gelé !
  3. **Découvert bancaire géant en Chine (`3 623 M$` / `2 758 M$` net au PDF) :** Les `318 k` voitures invendues en Chine ont vidé la trésorerie chinoise pendant que `8,49 Mds $` dormaient aux USA et `6,94 Mds $` en Europe ➔ chute de l'**Indépendance Financière à `4 points sur 12`**.
  4. **Achat de +1 usine USA et +1 usine Chine :** Portant notre parc au Tour 2 à **8 usines USA (`1 600 k`)** et **3 usines Chine (`750 k`)**.

---

## 🚀 3. Tour 2 (`Période 2` — Mercredi 17h15) : La Remontada Historique à la 1re Place (~140 pts)

### Les Décisions Soumises par `IronHorse` au Tour 2 :
- **Stratégie de déstockage total :** Coupure à **`0`** de toute la sous-traitance Thermique (qui venait de bondir à `13 694,3 $` aux USA !) et réduction de la production interne USA à `64 %` (`1 024 k` brut / `979 k` net) et Chine à `90 %` (`675 k` brut / `631 k` net) pour forcer la vente intégrale de nos **`371 k` voitures en stock**.
- **Lancement ciblé de l'Hybride (grâce à la R&D Hybride du Tour 1) :** `43 k` Hybrides produits en interne aux USA + `85 k` sous-traités en Chine = `128 k` Hybrides vendus à `100 %` (`68 k` USA à `32 800 $`, `57 k` Chine à `228 000 RMB`, `111 k` Europe à `34 200 €`).
- **Achats / Fournisseurs ESG :** Sélection des 3 fournisseurs optimaux (`Maîtres Matérialistes` + `Composants Colossaux` + `Innovation Réinventée`) et retrait de `Singularités Quantiques` (boycotté) et `Fusions Dynamiques` ➔ coût composants abaissé de `7 150 $` à **`6 833,3 $`**.
- **RH & R&D :** `5 000` ingénieurs, salaire `5 600 $`, formation `1 000 $`, et **allocation de `100,0 %` des `1 250 000` jours-homme** (`200 000` Thermique, `550 000` Hybride, `500 000` Électrique) sans acheter de licence inutile.
- **Finance :** Rapatriement de **`6 000 M$`** d'Europe vers les USA, transfert de **`5 000 M$`** des USA vers la Chine (effaçant 100 % du découvert chinois), et remboursement de **`-4 000 M$`** de dette à long terme.

### Résultats Officiels du Tour 2 (`manuels/Results for Univers 1, Tour 2.html`) :
- **Résultat Net Annuel :** **`10 774 M$`** (**#1 ABSOLU de l'Univers 1** sur les 12 équipes !).
- **EBIT (Résultat Opérationnel) :** **`13 880 M$`** (`1 230 M$` USA + `1 897 M$` Chine + `10 753 M$` Europe).
- **Stocks Finaux :** **`0 k` unité partout !** (`371 k` voitures du Tour 1 écoulées à 100 %, libérant `+4,41 milliards $` de cash).
- **Découvert Bancaire :** **`0 M$` partout !** Trésorerie finale colossale de **`23 935 M$`** (`7 602 M$` USA + `7 033 M$` Chine + `9 301 M$` Europe) pour seulement `7 900 M$` de dette long terme restante !
- **Ratio des Fonds Propres (Indépendance Financière) :** **`74,66 %`** (bond de +25 points de pourcentage ! Notation de crédit **`AA-`**).
- **Productivité des Ingénieurs :** **`1,085`** (**#1 ABSOLU de l'Univers 1 = `12 points sur 12`**).

---

## 📋 4. Tableau Complet des 15 Critères et Classement Estimé du Tour 2 (12 Équipes)

Voici les valeurs exactes extraites de [`manuels/Results for Univers 1, Tour 2.html`](file:///c:/Users/len/OneDrive/Bureau/ceism/manuels/Results%20for%20Univers%201,%20Tour%202.html) et les points attribués par la formule officielle d'Eric Astien :

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
| **11. Stocks (k)** | **0 k (11p)** | 322 k (8p) | 531 k (7p) | 10 k (10p) | 774 k (3p) | 837 k (2p) | 0 k (11p) | 557 k (6p) | 878 k (1p) | 772 k (4p) | 1 135 k (1p*) | 1 098 k (2p*) |
| **12. Coût Unit. US** | **12 964$ (8p)** | 12 449$ (10p) | 13 200$ (7p) | 14 995$ (3p) | 14 182$ (6p) | 12 350$ (11p) | 15 377$ (1p) | 11 760$ (12p) | 15 041$ (2p) | 14 705$ (5p) | 15 199$ (2p*) | 12 873$ (9p) |
| **13. Coût Unit. Asie** | **11 345$ (8p)** | 11 223$ (11p) | 11 575$ (6p) | 12 461$ (3p) | 11 229$ (10p) | 10 833$ (12p) | 14 680$ (1p) | 11 385$ (7p) | 14 017$ (2p) | 12 060$ (5p) | 12 349$ (4p) | 11 277$ (9p) |
| **14. Coût Unit. Eur.** | **12 336$ (8p)** | 11 882$ (11p) | 13 131$ (7p) | 13 793$ (5p) | 12 177$ (10p) | 12 233$ (9p) | 14 701$ (4p) | 11 429$ (12p) | 14 708$ (3p) | 14 040$ (5p*) | 16 794$ (2p) | 17 174$ (1p) |
| **15. Productivité** | **1,085 (12p)** | 1,042 (7p) | 1,047 (8p) | 1,033 (6p) | 1,032 (5p) | 1,013 (1p) | 1,060 (9p) | 1,069 (10p) | 1,019 (3p) | 1,080 (11p) | 1,026 (4p) | 1,080 (11p) |
| **TOTAL TOUR 2** | **🥇 140 pts** | **🥈 133 pts** | **🥉 109 pts** | **104 pts** | **104 pts** | **103 pts** | **98 pts** | **96 pts** | **90 pts** | **68 pts** | **57 pts** | **54 pts** |
| **DÉCOUVERT (M$)** | **`0 M$`** | `0 M$` | `2 291 M$` | `0 M$` | `6 009 M$` | `10 098 M$` | `0 M$` | `3 814 M$` | `6 905 M$` | `5 200 M$` | `10 130 M$` | `9 765 M$` |

*(Note : En cumulé Période 1 + Période 2, `IronHorse` totalise `96 + 140 = 236 pts`, devant `POLRAMOS` `84 + 133 = 217 pts`, `GT-Auto` `105 + 104 = 209 pts`, `Ça Roule` `103 + 104 = 207 pts`, `YANAUTO` `104 + 103 = 207 pts` !)*

---

## 🔍 5. Profil Tactique des Principaux Concurrents pour le Tour 3

1. **Notre Rival Direct n°1 : `POLRAMOS` (2e du Tour 2 avec 133 pts)**
   - **Leur force :** Ils ont remboursé presque toute leur dette long terme (`1 000 M$` restants), ce qui leur donne **`95,32 %` d'Indépendance Financière (12 pts)**. Ils ont mis très peu d'équipements (`3 / 4 / 3` en Thermique), ce qui leur donne d'excellents coûts unitaires (`11 223 $ - 12 449 $`) et `10 529 M$` de résultat net.
   - **Leurs faiblesses à exploiter au Tour 3 :**
     - Ils n'ont que **7 usines USA et 2 usines Chine** (aucun achat d'usine au Tour 2, contre **8 usines USA et 3 usines Chine** pour nous !).
     - Ils ont **`322 k` voitures invendues en stock en Chine**.
     - Ils ont recruté **8 000 ingénieurs** mal payés (`5 200 $`), ce qui bloque leur productivité à `1,042` (`7 pts` contre `12 pts` pour nous) et leur coûte `861 M$` de R&D.
2. **Les Équipes Étouffées par leurs Stocks Géants (> 750 k voitures en stock !) :**
   - `tomobil` (`1 135 k` stock, `10 130 M$` découvert), `Vrooom Vroooom` (`1 098 k` stock, `9 765 M$` découvert), `TABCHOUR` (`878 k` stock, `6 905 M$` découvert), `YANAUTO` (`837 k` stock, `10 098 M$` découvert), `GT-Auto VI` (`774 k` stock, `6 009 M$` découvert), `MO'THOR` (`772 k` stock).
   - **Conséquence pour le Tour 3 :** Ces 6 équipes vont être obligées soit de brader leurs prix, soit de couper massivement leur production au Tour 3 (ce qui fera exploser leur coût unitaire de production interne !), tandis que nous avons **`0` stock** et pouvons faire tourner nos 8 usines USA et 3 usines Chine à plein régime (**88 %–92 %**) !
