# ⚙️ RÈGLES PROFONDES & MÉCANIQUES EXACTES DU MOTEUR CESIM (`ESYBIA2AS`)

Ce document résume les règles exactes vérifiées sur l'interface live de `https://bordeaux-inp.cesim.com/` (`Session ESYBIA2AS`, Univers 1) et dans les rapports officiels `Tour 1.html` et `Tour 2.html`.

---

## 📈 1. Module « Demande » & Dynamique des Marchés

### Structure des 3 Zones Géographiques
1. **USA (en USD)** : Grand marché mature. Sensibilité équilibrée au prix, aux équipements et à la publicité.
2. **Chine (en RMB — taux `6,6250 RMB = 1 USD` au T1/T2)** : Marché en plus forte croissance (`+7 %` au T1, `+8 % à +9 %` au T2). Très sensible au prix en RMB et aux équipements.
3. **Europe (en EUR — taux monté de `1,1750` à `1,2338 USD = 1 EUR` au Tour 2)** : Plus grand marché en volume Thermique et **vache à lait financière du jeu** (marges opérationnelles de `35 %` à `42 %`, impôt sur les sociétés abaissé de `27 %` à **`21 %`** au Tour 2 !). **Attention :** L'Europe ne possède **aucune usine** ; 100 % des voitures vendues en Europe sont importées depuis vos usines/sous-traitants USA et Chine (au coût de production, sans marge de cession interne).

### Fonctionnement des Prévisions de Demande dans l'interface
- Dans l'onglet `Demande`, vous saisissez :
  1. Vos **prévisions de croissance du marché (%)** pour USA, Chine, Europe (d'après les `Conditions de marché`).
  2. Vos **parts de marché estimées (%)** par technologie (`Thermique`, `Hybride`, `Électrique`).
- **Crucial :** Les chiffres que vous tapez dans `Demande` **ne déterminent pas vos vraies ventes** lors du calcul du tour (vos vraies ventes dépendent de vos Prix, Équipements, Publicité face aux 11 concurrents). En revanche, vos estimations dans `Demande` **pilotent toutes les projections de votre onglet `Production`, `Logistique` et `Prévisionnel financier`**.
- **Règle absolue :** Calibrer `Demande` de façon réaliste pour que `Stock initial + Production interne + Sous-traitance` corresponde exactement à ce que le marché va réellement acheter (objectif : **`0 k` stock final**).

---

## 🏭 2. Module « Production » (4 Sous-onglets : Planning, Stocks, Investissements, Achats)

### A. Production Interne vs Investissements (Usines)
- **Capacité et Coût réel d'une usine (vérifié dans les flux de trésorerie du Tour 2) :**
  - **1 usine USA** = **`200 k` unités** de capacité brute.
    - **Coût d'acquisition d'une usine USA** = **`1 200 M$`** (`1 200 000 k USD`).
    - **Valeur de cession (vente) d'une usine USA** = **`+1 080 M$`** (comme `POLRAMOS` et `BM2P` qui ont vendu 1 usine USA au Tour 2).
    - Au Tour 2 et au début du Tour 3, `IronHorse` possède **8 usines USA** (`1 600 k` de capacité brute).
  - **1 usine Chine** = **`250 k` unités** de capacité brute.
    - **Coût d'acquisition d'une usine Chine** = **`1 050 M$`** (`1 050 000 k USD`).
    - Au Tour 2 et au début du Tour 3, `IronHorse` possède **3 usines Chine** (`750 k` de capacité brute).
  - **Délai de construction :** Toute usine achetée au Tour $t$ est payée au Tour $t$ mais n'entre en production qu'au **Tour $t+1$** (`Usines disponibles -> Tour suivant`).
- **Loi du taux d'utilisation des usines (en Thermique) :**
  - Le coût de conversion minimal d'une usine Thermique se situe entre **`78 %` et `92 %` d'utilisation** (`~5 324 $ – 5 450 $` hors composants aux USA, `~3 412 $ – 3 450 $` hors composants en Chine).
  - **Attention au `100 %` :** À `100,0 %` d'utilisation, le moteur applique un surcoût d'heures supplémentaires de `+450 $` (Chine) à `+720 $` (USA) par voiture.

### B. Sous-traitance (`Outsourcing`) — Règle Critique Thermique vs Hybride !
1. **En HYBRIDE : La Sous-traitance Chine est MASSIVEMENT moins chère que la Production Interne !**
   - Au Tour 2 (`Results for Univers 1, Tour 2.html` lignes 545, 549, 554, 558) :
     - **Produire l'Hybride en interne** dans ses propres usines a coûté **`26 030 $` à `31 747 $`** aux USA et **`24 756 $` à `25 462 $`** en Chine (à cause de la courbe d'apprentissage initiale très faible sur l'Hybride interne) !
     - **Sous-traiter l'Hybride en Chine** (`Chine, Ligne de production 2 -> Quantité sous-traitée`) a coûté seulement **`17 014,6 $`** par voiture (et `18 197 $` aux USA) !
   - **C'est pour cela que nos `275 k` Hybrides sous-traités en Chine au Tour 2 (`0 %` en interne, `275 k` en sous-traitance Chine) ont été ultra-rentables** sans plomber notre coût moyen unitaire pondéré autant que les équipes qui ont produit l'Hybride en interne (`tomobil`, `Ren'Auto`, `Vrooom`, `MO'THOR`).
   - **Règle d'or pour le Tour 3 :** Toujours comparer dans `Production -> Planning` le coût unitaire de production interne Hybride vs le coût de sous-traitance Hybride Chine avant d'allouer la Ligne 2 interne ! Tant que la sous-traitance Hybride Chine est vers `17 000 $` contre `24 000 $+` en interne, **privilégier la sous-traitance Chine pour l'Hybride** !
2. **En THERMIQUE : Nos usines internes sont moins chères que la Sous-traitance :**
   - Au Tour 2, la sous-traitance Thermique USA avait bondi à `13 694,3 $` (plus chère que nos usines internes USA), donc mettre `0` en sous-traitance Thermique USA et Chine était optimal. Toujours vérifier les nouveaux coûts et plafonds de sous-traitance au début de chaque tour.

### C. Sous-onglet « Achats » (Les 5 Fournisseurs de Composants & l'Écart de `833 $/voiture`)
Voici les 5 fournisseurs et ce que le rapport officiel du Tour 2 (lignes 347–356 de `parsed_tour2_results_html.txt`) a révélé sur les choix des 12 équipes :

| Fournisseur | Coût / voiture (USD) | Note Image / ESG (sur 5) | Qui l'a coché au Tour 2 ? |
| :--- | :---: | :---: | :--- |
| **Composants Colossaux** | **`5 250 $`** *(Le moins cher)* | `2,00 / 5` | Coché par 8 équipes (dont `IronHorse`, `AURA`, `YANAUTO`, `GT-Auto`, `Vrooom`, `POLRAMOS`). |
| **Innovation Réinventée** | **`6 750 $`** | `3,50 / 5` | Coché par les **12 équipes**. |
| **Maîtres Matérialistes** | **`8 500 $`** | `4,50 / 5` | Coché par 7 équipes (dont `IronHorse` ➔ moyenne = **`6 833,3 $`**, Éthique `2,83`, Dév. durable `3,83`). |
| **Singularités Quantiques** | `6 750 $` | **`1,75 / 5` (PIRE NOTE)** | Décoché par 10 équipes (seuls `BM2P` et `TABCHOUR` ont laissé les 5 fournisseurs à `7 150 $`). |
| **Fusions Dynamiques** | `8 500 $` | `4,00 / 5` | Décoché par 10 équipes. |

> [!IMPORTANT]
> **Découverte Clé du Tour 2 sur les Fournisseurs (`6 000,0 $` vs `6 833,3 $`) :**
> - Au Tour 2, **5 équipes** (`AURA`, `YANAUTO`, `GT-Automobile VI`, `Vrooom Vroooom`, `POLRAMOS`) n'ont coché que **2 fournisseurs** : **`Composants Colossaux (5 250 $)` + `Innovation Réinventée (6 750 $)`**.
> - Résultat : leur coût moyen des composants est descendu à **`6 000,0 $`** (soit **`-833,3 $` de moins par voiture** que nos 3 fournisseurs à `6 833,3 $` !), tout en évitant `Singularités Quantiques (1,75/5)`.
> - C'est grâce à ces **`-833,3 $/voiture`** que `AURA`, `YANAUTO`, `POLRAMOS` et `GT-Auto` ont battu `IronHorse` sur les **3 critères de Coût Moyen Unitaire Pondéré (36 points au barème d'Eric Astien)** !
> - **À vérifier au début du Tour 3 dans `Conditions de marché` et `Production -> Achats` :** Si les Conditions de marché du Tour 3 ne sanctionnent pas le couple `Composants Colossaux + Innovation Réinventée` (Éthique `2,25`, Dév. durable `3,25`), décocher `Maîtres Matérialistes (8 500 $)` fait économiser **`-833,3 $` par voiture** (`+1,7 milliard $` de profit et **+9 à +12 points** sur les coûts unitaires du barème d'Eric Astien !). En revanche, si les ONG annoncent au Tour 3 qu'elles ciblent désormais `Composants Colossaux (2,00/5)` ou exigent un score Éthique $> 2,50$, alors garder `Maîtres Matérialistes` protège du boycott.

---

## 👩‍🔬 3. Modules « RH » et « R&D »

### A. Ressources Humaines (Ce que montrent les vrais chiffres du Tour 2)
- **Décision `IronHorse` soumise au Tour 2 :**
  - `Personnel sur ce tour` = **`5 000`** ingénieurs
  - `Prévision de départs volontaires` = **`2,5 %`** (départs réels au Tour 2 = **`1,9 %`**, soit `-93` démissions)
  - `Salaire mensuel` = **`5 800 USD`**
  - `Budget Formation mensuel` = **`1 500 USD`**
  - **Résultat obtenu :** **`1,085` de Coefficient de Productivité (#1 ABSOLU des 12 équipes = `12 points sur 12`)** pour un coût RH total de seulement **`628 M$`** !
- **Comparaison avec les équipes qui ont recruté massivement (`Vrooom` et `MO'THOR`) :**
  - Recruter massivement **ne fait pas chuter la productivité** si le salaire et la formation suivent (`Vrooom` avec `10 000` ingénieurs à `5 500 $ / 1 100 $` et `MO'THOR` avec `12 000` ingénieurs à `5 500 $ / 1 100 $` ont obtenu **`1,080`**, ex-aequo 2e = `11 pts/12`).
  - **En revanche**, `10 000` à `12 000` ingénieurs leur ont coûté **`1 176 M$`** et **`1 388 M$`** en frais de R&D (soit **`+548 M$` à `+760 M$` de coûts fixes en plus** dans le Compte de Résultat !), alors qu'avec **`5 000` ingénieurs** mieux payés (`5 800 $`) et mieux formés (`1 500 $`), `IronHorse` a eu une **meilleure productivité (`1,085` > `1,080` ➔ 12 pts/12)** pour **deux fois moins cher (`628 M$`)** !
  - **Ce qui fait chuter la productivité :**
    1. **Licencier des ingénieurs** (ex: `Ren'Auto` a licencié `-494` ingénieurs / `16,5 %` : malgré `8 500 $` de salaire, sa productivité s'est effondrée de `1,054` à **`1,017`** !).
    2. **Ne pas allouer `100,0 %` des jours-homme disponibles dans l'onglet `R&D`** (ex: `tomobil` à `72 %` ➔ `1,030`).

### B. R&D Interne & État Exact de nos Équipements au Début du Tour 3
- **Notre allocation R&D soumise au Tour 1 ET au Tour 2 (`live_decisionchecklist.json`) :**
  - **Thermique :** **`120 000`** jours-homme
  - **Hybride :** **`1 130 000`** jours-homme
  - **Électrique :** **`0`** jours-homme
  - **Licences achetées :** Aucune.
- **Nos plafonds réels d'équipements débloqués pour le Tour 3 :**
  - **Thermique :** **`7` équipements maximum** disponibles au Tour 3.
  - **Hybride :** **`4` équipements maximum** disponibles au Tour 3.
  - **Électrique :** **`0`** (non débloqué en R&D interne ; nécessite soit de la R&D interne au T3 pour le T4, soit l'achat d'une licence `Nouvelle tech + X équipement` si on veut vendre de l'Électrique dès le Tour 3).

---

## 📣 4. Module « Marketing » (Prix, Équipements, Publicité)

- **Ce qu'`IronHorse` a réellement soumis au Tour 2 (`live_decisionchecklist.json`) :**
  - **USA :**
    - Thermique : Prix **`20 500 $`** | Équipements **`5`** | Publicité **`800 000 k$`** (`658 k` vendus, `0` demande insatisfaite)
    - Hybride : Prix **`29 500 $`** | Équipements **`1`** | Publicité **`300 000 k$`** (`76 k` vendus, `33 k` demande insatisfaite)
  - **Chine :**
    - Thermique : Prix **`130 000 RMB`** | Équipements **`6`** | Publicité **`450 000 k$`** (`574 k` vendus, `0` demande insatisfaite)
    - Hybride : Prix **`205 000 RMB`** | Équipements **`1`** | Publicité **`250 000 k$`** (`66 k` vendus, `0` demande insatisfaite)
  - **Europe :**
    - Thermique : Prix **`22 500 €`** | Équipements **`4`** | Publicité **`600 000 k$`** (`838 k` vendus, `2 k` demande insatisfaite)
    - Hybride : Prix **`28 500 €`** | Équipements **`1`** | Publicité **`300 000 k$`** (`133 k` vendus, `0` demande insatisfaite)
- **Positionnement Équipements par rapport au marché :**
  - Au Tour 2, la moyenne des 12 équipes en Thermique était de **`5,4` équipements aux USA**, **`5,9` en Chine** et **`4,8` en Europe** (et en Hybride : `2,3` équipements).
  - Nos **`5 / 6 / 4` équipements en Thermique** étaient pile dans la moyenne compétitive du marché (hors `Ren'Auto` et `AURA` à 10 équipements), ce qui nous a permis d'écouler **100 % de nos stocks (`0 k` stock final)**.
  - **Attention :** Descendre à `4 / 4 / 3` équipements alors que nous sommes à `5 / 6 / 4` et que le marché monte en gamme au Tour 3 nous ferait perdre des parts de marché ! Avec **`7` équipements Thermiques** et **`4` équipements Hybrides** disponibles au Tour 3, nous devons garder au moins **`5 / 6 / 4` (voire `5 / 6 / 5`) en Thermique** et monter l'Hybride de `1` vers **`2` ou `3` équipements** !

---

## 🚢 5. Module « Logistique » (Ce qui existe réellement dans notre interface)

- **Important :** Dans cette configuration du jeu (`tour2_logistics.json`), **il n'y a PAS de réglage de multiplicateur de prix de cession interne (`1,20 à 1,25`)** ! Toutes les cessions internes entre les usines (USA / Chine) et la filiale qui vend le véhicule se font **automatiquement au coût de production**.
- **Les seuls paramètres de décision dans l'onglet `Logistique` sont les Priorités de livraison :**
  - `Priorités de livraison: De USA` (ex: `1. USA, 2. Europe, 3. Chine`)
  - `Priorités de livraison: De Chine` (ex: `1. Chine, 2. Europe, 3. USA`)
- **Coûts de transport (droits de douane inclus) affichés dans `Logistique` au Tour 2 :**
  - Thermique `USA → Europe` : **`1 777,9 USD / unité`**
  - Thermique `Chine → Europe` : **`1 639,0 USD / unité`** (exporter vers l'Europe depuis la Chine coûte `139 $` de moins en transport/douane ET `~2 190 $` de moins en coût de production qu'exporter depuis les USA !)
  - Thermique `Chine → USA` : **`659,7 USD / unité`**
  - Thermique `USA → Chine` : **`3 685,7 USD / unité`** (prohibitif : ne jamais exporter des USA vers la Chine !).

---

## 💰 6. Module « Finance » (Sens Exact des Signes `+` et `-` !)

Dans notre interface (`tour2_finance.json`), les dividendes et rachats d'actions **ne sont pas ouverts**. Il n'y a que **3 cases de saisie** dans l'onglet `Finance` :

1. **`Augmenter (+) / réduire (-) l'emprunt bancaire à long terme` (k USD) :**
   - Saisir un nombre **négatif** (ex: **`-4 000 000`** au Tour 2) **rembourse** la dette à long terme aux USA (ce qui augmente directement le `Ratio des fonds propres` / `Indépendance financière` = 12 pts).
   - Saisir un nombre **positif** emprunte de la dette à long terme aux USA.

2. **`Transferts internes, k USD` (ATTENTION AU SENS DES SIGNES `+` ET `-` !) :**
   Regarde l'intitulé exact des deux champs dans `tour2_finance.json` :
   - **Ligne 1 : `USA → Chine (+), Chine → USA (-)`**
     - Saisir un nombre **POSITIF** (ex: **`5 000 000`** au Tour 2) envoie de l'argent **des USA vers la Chine**.
     - Saisir un nombre **NÉGATIF** (ex: **`-3 000 000`**) rapatrie de l'argent **de la Chine vers les USA**.
   - **Ligne 2 : `USA → Europe (+), Europe → USA (-)`**
     - ⚠️ **ATTENTION CRITIQUE :** Saisir un nombre **NÉGATIF** (ex: **`-6 000 000`** comme nous l'avons fait au Tour 2 !) rapatrie de l'argent **de l'Europe vers les USA** !
     - Si tu saisis un nombre **POSITIF** dans cette case, tu envoies l'argent **des USA vers l'Europe** (ce qui viderait la trésorerie américaine et créerait un découvert aux USA !).
   - **Vérification obligatoire :** Après toute saisie dans `Finance`, cliquer sur `Prévisionnel financier -> Bilan -> USA / Chine / Europe` à gauche de l'écran pour vérifier que `Trésorerie et équivalents` augmente du bon côté et que `Dettes à court terme (imprévues)` est bien à **`0`** dans les 3 zones !
