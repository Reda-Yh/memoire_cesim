# 🏆 LE BARÈME SECRET D'ERIC ASTIEN : ÉVOLUTION 15 ➔ 17 ➔ 21 ➔ 22 CRITÈRES (TOUR 5+)
> **Navigation :** [Index Recherche](../INDEX_RECHERCHE_AGENT_IA.md) · [Index Maître](../00_INDEX_AGENT_IA.md) · [README](../README.md) · [Outils & Scripts](../03_outils_et_scripts/README_OUTILS_ET_CHROME.md)

**Source officielle vérifiée :** [`classement_officiel_tours_0_a_3_ESYBIA2AS.pdf`](../07_classements_officiels/classement_officiel_tours_0_a_3_ESYBIA2AS.pdf) (Pages 1 à 4 : Période Test, Période 1, Période 2 et Période 3) + calcul exact validé sur [`tour_04_resultats_univers1.xls`](../04_rapports_tours/tour_04_resultats_univers1.xls).

À mesure que le professeur débloque de nouveaux onglets dans la simulation, sa grille Excel s'élargit :
- **Période Test & Période 1 :** **15 critères** (`180 pts` max théoriques ; `Découvert` était affiché en bas sans compter dans les points).
- **Période 2 :** **17 critères** — ajout de **`DÉCOUVERT`** et **`SCORE DDRS FOURNISSEURS`**.
- **Période 3–4 :** **21 critères** — ajout des 4 piliers ESG notés : **`IMPACT ENVIRONNEMENTAL`**, **`IMPACT SOCIÉTAL`**, **`IMPACT GOUVERNANCE`** et **`CERTIFICATION`** (`0 / 2 / 4 / 6 pts`).
- **Période 5 (et suivantes, confirmé sur le PDF officiel P5 fourni) : 22 critères** — ajout de **`RENTABILITÉ DE L’ACTION`** (`1–12 pts`), calculée en TSR : `((cours_t - cours_t-1 + dividende_par_action) / cours_t-1) × 100`. Le dividende par action est `- ligne Dividendes (M USD) / actions sur le marché (millions)` dans le rapport Cesim.

Le script [`calculateur_classement_astien.py`](../03_outils_et_scripts/calculateur_classement_astien.py) intègre automatiquement les **15, 17, 21 ou 22 critères** selon le rapport `.xls` ou `.html` fourni (auto-détection `Tour 1 = 15`, `Tour 2 = 17`, `Tour 3+ = 21` ; vérifié à l'identique sur les Tours 2 et 3 du PDF officiel).

---

## 🧮 1. La Formule Mathématique Exacte dans l'Excel du Professeur

Pour chaque critère évalué en points relatifs (critères `1` à `20`), Eric Astien applique cette formule sur les 12 équipes :

$$\text{Points de l'équipe } i = 1 + \text{Nombre d'équipes strictement moins bonnes que } i \text{ sur ce critère}$$

### Conséquence cruciale sur les ex-aequo (Ties) :
- **Critères où « Plus grand = Meilleur »** (`= 1 + NB.SI(plage; "<" & valeur_i)`):
  - Le 1er seul prend **12 pts**, le 2e prend **11 pts**, ..., le 12e prend **1 pt**.
  - **Ex-aequo à la 1re place (`100,00 %` Indépendance Financière au Tour 3) :** 4 équipes sont à `100,00 %` (`YANAUTO`, `POLRAMOS`, `BM2P`, `TABCHOUR`) avec `8` équipes strictement en dessous ➔ chacune reçoit **`1 + 8 = 9 pts`** (et non `12` !).
  - **`SCORE DDRS FOURNISSEURS` au Tour 3 :** 8 équipes ont le maximum atteint (`6,00`) avec seulement `4` équipes strictement pires (`Vrooom 5,00`, `IronHorse 4,67`, `TABCHOUR 4,67`, `AURA 4,00`) ➔ les 8 propres reçoivent `5 pts`, `Vrooom 4 pts`, et **chuter avec un mauvais fournisseur ne laisse que `2 pts` !**
- **Critères où « Plus petit = Meilleur »** (`= 1 + NB.SI(plage; ">" & valeur_i)`):
  - **`DÉCOUVERT` au Tour 3 :** 8 équipes sont à `0 M$` et 4 équipes ont un découvert (`Ça Roule 685`, `MO'THOR 1 342`, `AURA 1 695`, `tomobil 22 802`) ➔ chaque équipe à `0` reçoit **`1 + 4 = 5 pts`**, et celle avec `22 802 M$` ne prend que `1 pt`.
  - **`Stocks en volume` au Tour 2 :** Seulement 2 équipes à `0 k` ➔ **`11 pts` chacune** ! Au Tour 3, personne n'est à `0 k` : `BM2P` (`126 k`) prend **`12 pts`**, `IronHorse` (`379 k`) tombe à **`5 pts`**.

---

## 📋 2. Les 21 Critères Officiels (Tour 3–4) et le 22e critère (Tour 5+) & Correspondance Exacte `.xls / .html` Cesim

| # | Nom du Critère dans le PDF d'Eric Astien | Sens | Max / Barème | Ligne exacte dans le rapport Cesim (`tour_XX_resultats_univers1.xls` / `.html`) |
| :-: | :--- | :---: | :---: | :--- |
| **1** | **RENTABILITÉ FINANCIÈRE (ROE)** | $\uparrow$ Max | `1–12 pts` | Table `Ratios et indicateurs financiers` ➔ `Rentabilité des fonds propres (ROE)` |
| **2** | **CRÉATION DE VALEUR** | $\uparrow$ Max | `1–12 pts` | Table `Création de valeur` ➔ **`Création de valeur totale`** |
| **3** | **INDÉPENDANCE FINANCIÈRE** | $\uparrow$ Max | `1–12 pts` | Table `Bilan, global` ➔ $\frac{\text{Total des capitaux propres}}{\text{Total Passif} - \text{Dette fournisseurs}} \times 100$ *(vaut `100 %` si `Dettes LT = 0` et `Découvert = 0` !)* |
| **4** | **MARGE OPÉRATIONNELLE US (RO/CA)** | $\uparrow$ Max | `1–12 pts` | Table `Compte de résultat, USA` ➔ $\frac{\text{EBIT USA}}{\text{Chiffre d'affaires total USA}} \times 100$ *(inclut ventes + prix de transfert)* |
| **5** | **MARGE OPÉRATIONNELLE ASIE** | $\uparrow$ Max | `1–12 pts` | Table `Compte de résultat, Chine` ➔ $\frac{\text{EBIT Chine}}{\text{Chiffre d'affaires total Chine}} \times 100$ |
| **6** | **MARGE OPÉRATIONNELLE EUROPE** | $\uparrow$ Max | `1–12 pts` | Table `Compte de résultat, Europe` ➔ $\frac{\text{EBIT Europe}}{\text{Chiffre d'affaires Europe}} \times 100$ |
| **7** | **PART DE MARCHÉ US** | $\uparrow$ Max | `1–12 pts` | Table `Résultats par zone, USA` ➔ `USA parts de marché, %` ➔ **`Total`** *(NB : en Période 1 uniquement, pointait par erreur vers Global ; depuis Période 2 & 3, utilise bien la vraie PDM USA !)* |
| **8** | **PART DE MARCHÉ ASIE** | $\uparrow$ Max | `1–12 pts` | Table `Résultats par zone, Chine` ➔ `Chine parts de marché, %` ➔ **`Total`** |
| **9** | **PART DE MARCHÉ EUROPE** | $\uparrow$ Max | `1–12 pts` | Table `Résultats par zone, Europe` ➔ `Europe parts de marché, %` ➔ **`Total`** |
| **10** | **DEMANDE INSATISFAITE EN VOLUME** | $\downarrow$ Min (`0`) | `1–12 pts` | Table `Détails sur la logistique` ➔ Somme de toutes les lignes `Demande insatisfaite` (USA + Chine + Europe, toutes technos) |
| **11** | **STOCKS EN VOLUME** | $\downarrow$ Min (`0`) | `1–12 pts` | Table `Détails sur la production` ➔ `Stocks, k unités` ➔ Somme des stocks finaux **USA + Chine** (toutes technos) |
| **12** | **COÛT MOYEN UNITAIRE PONDÉRÉ (US)** | $\downarrow$ Min | `1–12 pts` | Table `Rapport de coûts` ➔ `Coût unitaire par produit vendu, USD` ➔ `USA` ➔ **`Moyenne pondérée`** |
| **13** | **COÛT MOYEN UNITAIRE PONDÉRÉ (Asie)** | $\downarrow$ Min | `1–12 pts` | Table `Rapport de coûts` ➔ `Coût unitaire par produit vendu, USD` ➔ `Chine` ➔ **`Moyenne pondérée`** |
| **14** | **COÛT MOYEN UNITAIRE PONDÉRÉ (Europe)** | $\downarrow$ Min | `1–12 pts` | Table `Rapport de coûts` ➔ `Coût unitaire par produit vendu, USD` ➔ `Europe` ➔ **`Moyenne pondérée`** |
| **15** | **COÉFFICIENT DE PRODUCTIVITÉ / INGÉNIEURS** | $\uparrow$ Max | `1–12 pts` | Table `Rapport RH` ➔ `Ressources humaines` ➔ **`Coefficient de productivité`** |
| **16** | **DÉCOUVERT** *(Nouveau T2+)* | $\downarrow$ Min (`0`) | `1–12 pts` | Table `Bilan, global` ➔ **`Dettes à court terme (imprévues)`** |
| **17** | **SCORE DDRS FOURNISSEURS** *(Nouveau T2+)* | $\uparrow$ Max | `1–12 pts` | Table `Rapport du fournisseur de composants` ➔ **`Qualité` + `Développement durable`** *(somme sur 10,00 ; `6,00` en T3 sans Colossaux/Singularités)* |
| **18** | **IMPACT ENVIRONNEMENTAL** *(Nouveau T3+)* | $\uparrow$ Max | `1–12 pts` | Table `Rapport ESG` ➔ `Score final` ➔ **`Environnement (E)`** |
| **19** | **IMPACT SOCIÉTAL** *(Nouveau T3+)* | $\uparrow$ Max | `1–12 pts` | Table `Rapport ESG` ➔ `Score final` ➔ **`Social (S)`** *(IronHorse #1 au T3 : `3,98 = 12 pts` !)* |
| **20** | **IMPACT GOUVERNANCE** *(Nouveau T3+)* | $\uparrow$ Max | `1–12 pts` | Table `Rapport ESG` ➔ `Score final` ➔ **`Gouvernance (G)`** |
| **21** | **CERTIFICATION** *(Nouveau T3+)* | Points fixes | **`0 / 2 / 4 / 6 pts`** | Table `Rapport ESG` ➔ `Certitications de développement durable` : `Pas de cert. = 0`, `Bronze (>=2,75) = 2`, **`Argent (>=3,25) = 4`**, **`Or (>=4,00) = 6`** |
| **22** | **RENTABILITÉ DE L’ACTION** *(Nouveau T5+)* | ↑ Max | `1–12 pts` | `((Cours action fin T5 - cours fin T4 + dividende/action) / cours fin T4) × 100`; cours et dividendes depuis le rapport Cesim, actions en millions. Vérifié contre les 12 scores du classement officiel P5.

---

## ⚠️ 3. Les 8 Pièges Mortels du Barème d'Eric Astien (Leçons Tours 1 à 4)

### Piège n°1 : Les 36 Points du « Coût Moyen Unitaire Pondéré » (Critères 12, 13, 14)
- Ces 3 lignes font la **moyenne pondérée** entre vos véhicules **Thermiques** (`~10 000 – 13 000 $`) et vos véhicules **Hybrides / Électriques** (`~18 000 – 47 000 $`).
- Au Tour 3, **`MO'THOR`** a produit 213 k véhicules **Électriques** en Chine à **`46 871,1 $/unité`** : son coût moyen pondéré Asie a explosé à **`16 817 $` (`2 pts`)** et son résultat net est resté bloqué à `3 352 M$` (11e).
- À l'inverse, éviter de produire l'Hybride en interne à `24 000+ $`, faire tourner les usines Thermiques entre **`82 %` et `92 %`** (jamais `100 %` !), et optimiser le mix fournisseurs maintient des coûts unitaires ultra-compétitifs sans sacrifier l'Hybride rentable sous-traité.

### Piège n°2 : Le Découvert Bancaire Local (`Dettes à court terme imprévues`)
- La trésorerie est isolée par filiale (**USA, Chine, Europe**). Si la Chine ou les USA manquent de cash (achats d'usines payés à `t+1`, surstocks), Cesim crée un découvert punitif (**Critère n°16 `DÉCOUVERT`**) qui plombe aussi l'**`INDÉPENDANCE FINANCIÈRE` (Critère n°3)**.
- **Toujours** équilibrer via `Finance -> Transferts internes` et vérifier `Dettes à court terme (imprévues) = 0` dans `Prévisionnel financier -> Bilan -> USA / Chine / Europe`.

### Piège n°3 : L'Allocation R&D à `100 %` & L'Impact de l'Effet Formation / Rotation
- Oublier d'allouer 100 % des jours-homme disponibles détruit la productivité.
- Attention depuis le Tour 3 : `Initiatives d'engagement communautaire` (`RH -> Politiques`) prélève **`150 000` jours-homme** sur le pool R&D (`1 400 000 ➔ 1 250 000` pour `5 600` ingénieurs). Ne **jamais** licencier (chute brutale de productivité) et vérifier que `Formation de base` / salaire (`5 800–6 200 $`) / budget formation (`1 500–2 000 $`) maintiennent la productivité dans le haut du tableau (au T3, `AURA` est monté à `1,193` grâce au cumul + formation).

### Piège n°4 : L'Équilibre des Équipements (`700 $ / 650 $ / 750 $`)
- Chaque équipement proposé coûte exactement `700 $` (USA), `650 $` (Chine), `750 $` (Europe) par voiture vendue. En Europe, l'élasticité aux équipements est faible (`~0,25`), donc `4–5` équipements en Europe et `5–7` aux USA/Chine suffisent face à des concurrents qui sur-équipent à `10` équipements.

### Piège n°5 : Les Stocks Invendus (`Stocks en volume` = 12 pts) vs Rupture (`Demande insatisfaite` = 12 pts)
- Au Tour 3, `IronHorse` avait monté ses prix Thermiques de `20 500 ➔ 20 700 $`, `130 ➔ 131k RMB`, `22 500 ➔ 23 000 €` tout en gardant `30 %` d'énergie renouvelable et un fournisseur à `1★` : la demande a baissé, laissant **`379 k` Thermiques en stock (`5 pts`)** et **`365 k` ruptures Hybrides (`3 pts`)** = `-14 points` perdus sur ces deux lignes par rapport au Tour 2 !
- Toujours calibrer `Production interne + Sous-traitance` sur des prévisions réalistes intégrant l'effet ESG relatif aux concurrents.

### Piège n°6 : Le Crash Fournisseur (`Composants Colossaux 1★`) & La Double Sanction
- Les étoiles des fournisseurs **changent à chaque tour** ! Au Tour 3, `Composants Colossaux (5 250 $)` est tombé à **`1★ Qualité / 1★ Développement durable` (`Image 1,00`)**.
- Conséquence quadruple sur `IronHorse` au Tour 3 :
  1. **`-5,5 %` d'impact direct sur la demande** (`Rapport ESG -> Politiques des fournisseurs`) contre `+2,6 %` pour les 8 équipes sans Colossaux (= **8,1 % d'écart de demande !**).
  2. **`Score DDRS Fournisseurs = 4,67` (`2 pts`)** au lieu de `6,00` (`5 pts`).
  3. **Explosion du taux de pertes en usine (scrap)** : passé de `5,1 % ➔ 7,1 %` aux USA et de `7,4 % ➔ 10,2 %` en Chine (`+3 %` de voitures perdues en production !).
  4. **Chute du score `Gouvernance (G)`** à `2,98` (`4 pts`).
- **Règle absolue :** Toujours inspecter les étoiles actuelles + prévisions (`Études`) dans `Production -> Achats`, et décocher tout fournisseur `< 2★` dès qu'une alternative propre est rentable ! *(Confirmé de nouveau au Tour 4 : `IronHorse` était la seule équipe sur 12 à garder `Composants Colossaux`, chutant à `5,67` = `1 / 7 pts` DDRS et `-6,1 %` demande alors que les 11 concurrents étaient à `6,75–7,25` !)*

### Piège n°7 : Les Multiplicateurs Massifs de Demande ESG (`Tour 3+`)
Mesurés directement dans `tour_03_resultats_univers1.xls -> Rapport ESG -> Impact sur la demande` :
- **`Utilisation d'énergie renouvelable` :** **`+12,8 %`** à `100 %` contre **`-7,8 %`** à `30 %` (= **+20,6 points d'écart de demande !**).
- **`Améliorations de la qualité des processus` :** **`+20,9 %`** avec les 3 (`CO2 + Énergie + Eau`) vs `-0,3 %` avec 1 seule et `-8,2 %` avec 0 (= **+29,1 points d'écart de demande !**).
- **`Recyclabilité` :** Ne **JAMAIS** descendre de niveau quand `Engagement` est coché (`POLRAMOS` a pris **`-5,7 %`** de pénalité demande au T3 pour avoir baissé d'un cran ; `Systèmes de cycle fermé` donne **`+4,2 %`**).
- **`RH -> Priorités de formation` :** Cocher 1 seule priorité ciblée (`Éthique` seule) a donné **`+11,7 %`** d'image à `IronHorse` et **`#1 Impact Sociétal (3,98 = 12 pts)`**, alors que tout cocher (5/5 comme `Ren'Auto`) dilue l'effet à **`+1,6 %`** !

### Piège n°8 : La Marge Opérationnelle US écrasée quand `Prix de transfert = 1,00`
- Au Tour 3, `IronHorse` a eu **`-0,98 %` de Marge Opérationnelle US (`4 pts / 12`)** parce que la filiale USA vendait `712 k` voitures à l'Europe **au prix coûtant (`PCI = 1,00`)** tout en payant 100 % des frais de R&D et d'administration US ! Pendant ce temps, l'Europe affichait `32,96 %` de marge.
- Dès le **Tour 4**, le professeur a ouvert l'onglet **`Impôts -> Prix de transfert`** (`1.00` à `2.00`) ET l'IS américain est descendu à **`20,0 %`** (contre `21,0 %` Europe et `24,0 %` Chine) : augmenter modérément `USA → Europe` (ex: `1.20` à `1.35`, en surveillant les droits de douane de `13 %`) permet de remonter l'EBIT/Marge US, d'effacer les pertes reportables US (`226 M$` fin T3) et d'optimiser la note sur le Critère n°4 !
