# 🏆 LE BARÈME SECRET D'ERIC ASTIEN : 15 CRITÈRES (180 POINTS / TOUR)
**Source officielle vérifiée :** [`manuels/CLASSEMENT DES ÉQUIPES ESYBIA2AS (1).pdf`](file:///c:/Users/len/OneDrive/Bureau/ceism/manuels/CLASSEMENT%20DES%20%C3%89QUIPES%20ESYBIA2AS%20(1).pdf) (Pages 1 et 2).

Contrairement au classement par défaut de Cesim (qui ne regarde que le retour cumulé aux actionnaires / cours de l'action), **le professeur Eric Astien note les 12 équipes à chaque tour sur une grille Excel de 15 critères, chacun noté de 1 à 12 points (Total max = 180 points par tour)**.

---

## 🧮 1. La Formule Mathématique Exacte d'Attribution des Points dans l'Excel du Professeur

En rétro-ingénierant les tableaux officiels de la `Période Test` (Page 1) et de la `Période 1` (Page 2), nous avons prouvé à 100 % la formule Excel utilisée par Eric Astien pour transformer les valeurs des 12 équipes en points de `1` à `12` :

$$\text{Points de l'équipe } i = 1 + \text{Nombre d'équipes strictement moins bonnes que } i \text{ sur ce critère}$$

### Conséquence cruciale sur les ex-aequo (Ties) :
- **Critères où "Plus grand = Meilleur"** *(ROE, Création de valeur, Indépendance financière, Marges opérationnelles, Parts de marché, Productivité ingénieurs)* :
  - Formule Excel : `= 1 + NB.SI(plage; "<" & valeur_equipe)`
  - Le 1er seul prend **12 pts**, le 2e prend **11 pts**, ..., le 12e prend **1 pt**.
  - Si 2 équipes sont ex-aequo à la 2e place (avec 9 équipes strictement derrière elles), elles prennent toutes les deux `1 + 9 = 10 pts`.
- **Critères où "Plus petit = Meilleur"** *(Demande insatisfaite, Stocks en volume, Coûts moyens unitaires pondérés US / Asie / Europe)* :
  - Formule Excel : `= 1 + NB.SI(plage; ">" & valeur_equipe)`
  - **Exemple réel 1 (`Demande insatisfaite` en Période 1) :** 10 équipes ont eu `0` demande insatisfaite, et seulement 2 équipes ont eu `> 0` (`tomobil` 343 k et `Ren'Auto` 692 k). Résultat : les 10 équipes à `0` n'ont que 2 équipes strictement moins bonnes qu'elles, donc **elles ne gagnent que `1 + 2 = 3 points` chacune** (et les deux autres prennent `2 pts` et `1 pt`).
  - **Exemple réel 2 (`Stocks en volume` au Tour 2) :** Seulement 2 équipes (`IronHorse` et `Ren'Auto`) ont réussi à avoir **`0 k` stock**, tandis que les 10 autres équipes ont des stocks `> 0`. Résultat : `IronHorse` et `Ren'Auto` prennent **`1 + 10 = 11 points`**, pendant que les autres prennent de `10` à `1` point !

---

## 📋 2. Les 15 Critères Officiels et leur Correspondance Exacte dans le Rapport HTML Cesim

Voici les 15 lignes exactes du tableau de notation d'Eric Astien (chacune sur **12 points**, soit **180 points au total**) :

| # | Nom du Critère dans le PDF d'Eric Astien | Sens | Poids | Ligne exacte dans `Results for Univers 1, Tour X.html` |
| :-: | :--- | :---: | :---: | :--- |
| **1** | **RENTABILITÉ FINANCIÈRE (ROE)** | $\uparrow$ Max | **12 pts** | Table `Ratios et indicateurs financiers` ➔ `Rentabilité des fonds propres (ROE)` *(ou Résultat Net / Capitaux Propres hors surcoût Achats au T1)* |
| **2** | **CRÉATION DE VALEUR** | $\uparrow$ Max | **12 pts** | Table `Création de valeur` (tout en bas du rapport) ➔ **`Création de valeur totale`** *(Somme : Actionnaires + Créanciers + Personnel + Gouvernement + Fournisseurs)* |
| **3** | **INDÉPENDANCE FINANCIÈRE** | $\uparrow$ Max | **12 pts** | Table `Ratios et indicateurs financiers` ➔ **`Ratio des fonds propres`** ($\frac{\text{Total Capitaux Propres}}{\text{Total Bilan}} \times 100$) |
| **4** | **MARGE OPÉRATIONNELLE US (RO/CA)** | $\uparrow$ Max | **12 pts** | Table `Compte de résultat, USA` ➔ $\frac{\text{RÉSULTAT OPÉRATIONNEL (EBIT) USA}}{\text{Chiffre d'affaires total USA}} \times 100$ *(inclut les ventes + prix de transfert)* |
| **5** | **MARGE OPÉRATIONNELLE ASIE** | $\uparrow$ Max | **12 pts** | Table `Compte de résultat, Chine` ➔ $\frac{\text{RÉSULTAT OPÉRATIONNEL (EBIT) Chine}}{\text{Chiffre d'affaires total Chine}} \times 100$ |
| **6** | **MARGE OPÉRATIONNELLE EUROPE** | $\uparrow$ Max | **12 pts** | Table `Compte de résultat, Europe` ➔ $\frac{\text{RÉSULTAT OPÉRATIONNEL (EBIT) Europe}}{\text{Chiffre d'affaires Europe}} \times 100$ |
| **7** | **PART DE MARCHÉ US** *(en réalité Globale)* | $\uparrow$ Max | **12 pts** | Table `Détails du marché, global` ➔ `Parts de marché global, %` ➔ **`Total`** *(Attention : en Période 1, la ligne "PART DE MARCHÉ US" du PDF pointe vers la part de marché globale toutes zones ; surveiller aussi `USA parts de marché -> Total`)* |
| **8** | **PART DE MARCHÉ ASIE** | $\uparrow$ Max | **12 pts** | Table `Résultats par zone, Chine` ➔ `Chine parts de marché, %` ➔ **`Total`** |
| **9** | **PART DE MARCHÉ EUROPE** | $\uparrow$ Max | **12 pts** | Table `Résultats par zone, Europe` ➔ `Europe parts de marché, %` ➔ **`Total`** |
| **10** | **DEMANDE INSATISFAITE EN VOLUME** | $\downarrow$ Min (`0`) | **12 pts** | Table `Rapport de logistique` ➔ Somme de toutes les lignes **`Demande insatisfaite`** (USA + Chine + Europe, toutes technologies) |
| **11** | **STOCKS EN VOLUME** | $\downarrow$ Min (`0`) | **12 pts** | Table `Production` ➔ `Stocks, k unités` ➔ Somme des stocks finaux **USA + Chine** (toutes technologies). **Objectif absolu = `0 k` !** |
| **12** | **COÛT MOYEN UNITAIRE PONDÉRÉ (véhicules vendus US)** | $\downarrow$ Min | **12 pts** | Table `Coûts de fabrication` ➔ `Coût unitaire par produit vendu, USD` ➔ `USA` ➔ **`Moyenne pondérée`** |
| **13** | **COÛT MOYEN UNITAIRE PONDÉRÉ (véhicules vendus Asie)** | $\downarrow$ Min | **12 pts** | Table `Coûts de fabrication` ➔ `Coût unitaire par produit vendu, USD` ➔ `Chine` ➔ **`Moyenne pondérée`** |
| **14** | **COÛT MOYEN UNITAIRE PONDÉRÉ (véhicules vendus Europe)** | $\downarrow$ Min | **12 pts** | Table `Coûts de fabrication` ➔ `Coût unitaire par produit vendu, USD` ➔ `Europe` ➔ **`Moyenne pondérée`** |
| **15** | **COÉFFICIENT DE PRODUCTIVITÉ / INGÉNIEURS** | $\uparrow$ Max | **12 pts** | Table `Recherche et développement (R&D)` ➔ `Ressources humaines` ➔ **`Coefficient de productivité`** |
| **--** | **DÉCOUVERT** *(Ligne rouge en bas du PDF)* | $\downarrow$ Min (`0`) | Indicateur / Malus | Table `Bilan` ➔ **`Dettes à court terme (imprévues)`** (ou déficit de trésorerie net de la filiale en découvert). Doit être à **`0`** ! |

---

## ⚠️ 3. Les 5 Pièges Mortels du Barème d'Eric Astien (Découvertes Stratégiques Majeures)

### Piège n°1 : Les 36 Points du « Coût Moyen Unitaire Pondéré » (Critères 12, 13 et 14 = 36 pts / 180 !)
C'est **le secret numéro 1 du barème d'Eric Astien** :
- Le professeur consacre **3 critères entiers (36 points sur 180, soit 20 % de la note totale !)** aux lignes `Coût unitaire par produit vendu, USD -> Moyenne pondérée` (aux USA, en Asie et en Europe).
- Or, dans Cesim, la ligne **`Moyenne pondérée`** fait la moyenne pondérée du coût de fabrication entre :
  - Vos voitures **Thermiques** (qui coûtent environ `10 500 $` en Chine et `11 500 $ - 12 400 $` aux USA),
  - Et vos voitures **Hybrides / Électriques** (qui coûtent `16 500 $` à `35 000 $` l'unité à produire ou sous-traiter !).
- **Ce qui s'est passé aux Tours 1 et 2 :**
  - Les équipes qui ont vendu beaucoup d'Hybrides (`TABCHOUR / Marron`, `Ren'Auto`, `Ça Roule`, `tomobil`) ont vu leur coût moyen unitaire pondéré grimper à **`14 000 $ – 17 174 $`** et ont récolté **1, 2 ou 3 points sur 12** sur ces 3 lignes (perdant jusqu'à **30 points** d'un coup !).
  - À l'inverse, une équipe qui garde une grosse proportion de volumes **Thermiques** produits dans des usines tournant à **88 %–92 % d'utilisation** avec de bons fournisseurs maintient son coût moyen pondéré autour de **`11 200 $ – 12 300 $`** et rafle **24 à 33 points sur 36** !
  - **Règle d'or :** Ne jamais sacrifier le volume Thermique tant qu'il représente >75 % du marché, ne jamais sous-utiliser les usines USA à 60 % si on n'a plus de stock à vider, et limiter le volume Hybride/Électrique à une proportion très rentable qui ne fait pas exploser la moyenne pondérée au-dessus de celle des concurrents !

### Piège n°2 : Le Découvert Bancaire Local (`Dettes à court terme imprévues`) détruit l'Indépendance Financière (12 pts)
- Dans Cesim, la trésorerie est **séparée par filiale** (USA, Chine, Europe).
- Si la filiale **Chine** ou **USA** termine l'année avec moins de cash que le minimum requis (à cause d'achats d'usines, de stocks invendus ou de remboursements), Cesim déclenche automatiquement un **prêt d'urgence / découvert (`Dettes à court terme imprévues`)** à taux punitif, **même si votre filiale Europe dort sur 10 milliards $ de cash !**
- Ce découvert gonfle le passif du bilan consolidé et fait chuter votre **`Ratio des fonds propres` (`Indépendance financière`, 12 pts)**, tout en s'affichant en **rouge** tout en bas de la feuille du professeur (`DECOUVERT`).
- **Règle d'or :** Toujours utiliser les **`Transferts de trésorerie entre sociétés du groupe`** dans l'onglet `Finance` pour rapatrier le cash d'Europe vers les USA et alimenter la Chine si nécessaire, afin que dans l'onglet `Budgets`, la ligne `Dettes à court terme (imprévues)` soit à **`0`** aux USA, **`0`** en Chine et **`0`** en Europe !

### Piège n°3 : L'Allocation R&D à 100 % et la Productivité Ingénieurs (12 pts gratuits)
- Le critère 15 (`Coefficient de productivité / Ingénieurs` = 12 pts) dépend de 3 leviers :
  1. **L'allocation de 100,0 % des Jours-homme disponibles dans l'onglet `R&D`** (`Nombre d'employés × 250 jours-homme`, soit `1 250 000` jours-homme pour `5 000` ingénieurs). Si une équipe oublie d'allouer 100 % (comme `YANAUTO` à 44,5 % au Tour 1 ou `AURA` à 88,4 %), sa productivité tombe à `1,013` (**1 point sur 12**).
  2. **La stabilité des effectifs (`5 000` ingénieurs)** : les équipes qui recrutent brutalement +3 000 à +7 000 ingénieurs (`POLRAMOS` 8 000, `BM2P` 9 500, `MO'THOR` 12 000) subissent une dilution de productivité des nouveaux arrivants et paient jusqu'à `1 515 M$` de salaires R&D ! En restant à **`5 000` ingénieurs** bien payés (`5 600 $ -> 5 800 $`) et bien formés (`1 000 $ -> 1 100 $`), `IronHorse` a obtenu **`1,085` (#1 absolu du jeu = 12 pts/12)** pour seulement `583 M$` de coût RH !

### Piège n°4 : La Sur-enchère d'Équipements (`Coûts des équipements`) écrase les 36 Points de Marges Opérationnelles
- Chaque équipement supplémentaire ajouté sur un modèle dans l'onglet `Marketing` multiplie le coût direct des équipements (`Coûts des équipements` dans le compte de résultat).
- Au Tour 1, `Ren'Auto` a mis 10 équipements (`15 820 M$` de coûts d'équipements !) et Yahya avait mis `5/6/4` équipements (`7 525 M$` contre `4 076 M$` chez `Rose`).
- **Règle d'or :** Ne jamais dépasser **`4 à 5` équipements en Thermique** et **`2 à 3` en Hybride** tant que le prix du marché ne le justifie pas. Cela protège les **36 points** des 3 Marges Opérationnelles (`US`, `Asie`, `Europe`) ET le `ROE` (12 pts).

### Piège n°5 : Les Stocks Invendus (`Stocks en volume` = 12 pts)
- Avoir **`0 k` voiture en stock** en fin de tour rapporte **11 à 12 points sur 12** ET libère des milliards de dollars de cash (évitant tout découvert).
- Dès qu'une équipe dépasse ses ventes réelles en production + sous-traitance, chaque tranche de `100 k` voitures invendues immobilise `~1,2 milliard $` de cash et fait plonger la note de Stocks de `11 pts` à `1-3 pts` (comme les 9 équipes piégées au Tour 2).
- **Règle d'or :** Dans `Production -> Planning`, la somme `Stock initial + Production interne (après pertes %) + Sous-traitance` doit être **exactement égale (à 1-2 k près) ou très légèrement inférieure (-5 k à -15 k)** à la demande totale estimée ! Il vaut 100 fois mieux avoir `10 k` de demande insatisfaite (`7-8 pts/12`) et **`0 k` de stock (`11-12 pts/12`)** que `0 k` de demande insatisfaite (`8 pts/12`) et `300 k` de stock (`2-5 pts/12` + `-3,6 Mds$` de cash en moins !).
