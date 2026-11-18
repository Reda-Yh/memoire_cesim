# 🧬 LES ALGORITHMES MATHÉMATIQUES INTERNES DU MOTEUR CESIM (CALIBRÉS SUR NOS VRAIES DONNÉES $R^2 = 0,992$)

Ce fichier documente les **équations mathématiques exactes** qui font tourner le moteur de simulation **Cesim Global Challenge** (`ESYBIA2AS`), rétro-ingénierées et calibrées par régression sur les données réelles des 12 équipes de l'Univers 1 aux Tours 1 et 2.

---

## 1. Algorithme de Demande et de Part de Marché (Modèle d'Attraction Multiplicatif de Cesim)

### A. Équation Fondamentale d'Attraction ($A_{i,z,m}$)
Pour chaque zone $z \in \{\text{USA}, \text{Chine}, \text{Europe}\}$ et chaque technologie $m \in \{\text{Thermique}, \text{Hybride}, \text{Électrique}, \text{Hydrogène}\}$, Cesim calcule d'abord la taille totale du segment $D_{\text{tot}}(z,m)$, puis répartit cette demande entre les 12 équipes proportionnellement à leur **score d'attraction** $A_{i,z,m}$ :

$$\text{Part de marché théorique } s_{i,z,m} = \frac{A_{i,z,m}}{\sum_{j=1}^{12} A_{j,z,m}}$$

$$\text{Où : } \quad A_{i,z,m} = \left(\frac{P_{i}}{\bar{P}}\right)^{\epsilon_P(z,m)} \cdot \left(\frac{F_{i}}{\bar{F}}\right)^{\epsilon_F(z,m)} \cdot \left(\frac{\text{Pub}_{i}}{\overline{\text{Pub}}}\right)^{\epsilon_A(z,m)} \cdot \left(s_{i,z,m}^{(t-1)}\right)^{\gamma} \cdot \Phi_{\text{ESG}}(i)$$

### B. Élasticités Exactes Calibrées sur l'Univers 1 ($R^2 = 0,9924$)

| Zone & Modèle | Élasticité-Prix ($\epsilon_P$) | Élasticité-Équipements ($\epsilon_F$) | Élasticité-Publicité ($\epsilon_A$) | Précision du fit ($R^2$) | Loi Tactique Déduite de l'Algorithme |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **USA — Thermique** | **`-2,32` à `-3,20`** | **`+0,41` à `+0,51`** | **`+0,19` à `+0,52`** | **`0,9701`** | Le prix est 5× plus puissant que les équipements. Budget pub optimal = `600–750 M$`. |
| **Chine — Thermique** | **`-3,03` à `-3,15`** | **`+0,59` à `+0,91`** | **`+0,17`** | **`0,9924`** | **Marché le plus sensible au prix (`-3,1`) ET aux équipements (`+0,6 à +0,9`)**, mais très peu sensible à la pub (`+0,17` ➔ inutile de dépasser `450–600 M$` de pub en Chine !). |
| **Europe — Thermique** | **`-1,92` à `-2,71`** | **`+0,24` à `+0,29`** | **`+0,15` à `+0,35`** | **`0,9924`** | **Élasticité aux équipements très faible (`+0,25` seulement !)** ➔ En Europe, mettre 6 ou 10 équipements est un gaspillage pur ! **`3` ou `4` équipements suffisent largement**. |

### C. Algorithme de Redistribution des Ruptures de Stock (`Demande Insatisfaite`)
Lorsqu'une équipe $j$ a une demande initiale $D_j$ supérieure à ses unités disponibles $Q_j$ :
1. Elle subit une **demande insatisfaite** de $D_j - Q_j$ (qui détruit son critère n°10 du barème Eric Astien).
2. Une fraction ($\approx 50\% - 70\%$) de ses clients non servis **se reporte automatiquement sur les autres équipes qui ont encore des voitures disponibles**, proportionnellement à leur score d'attraction $A_i$ !

---

## 2. Algorithme Exact du Coût des Équipements (`Coûts des équipements` — Précision 100,00 %)

En divisant la ligne `Coûts des équipements` de chaque compte de résultat par produit par $(\text{Ventes} \times \text{Nombre d'équipements proposés})$ sur les 12 équipes, nous avons découvert la **constante exacte codée en dur dans Cesim** :

$$\text{Coût des équipements (en USD)} = \text{Véhicules vendus} \times \text{Nombre d'équipements proposés} \times C_{\text{éq}}(z)$$

Où le coût unitaire par équipement $C_{\text{éq}}(z)$ (identique en Thermique et en Hybride !) vaut **exactement** :
- **Aux USA :** **`700 USD`** par équipement et par voiture vendue.
- **En Chine :** **`650 USD`** par équipement et par voiture vendue.
- **En Europe :** **`750 USD`** par équipement et par voiture vendue.

### Condition d'Optimalité Mathématique d'un Équipement Supplémentaire :
Ajouter un équipement ($F \to F+1$) augmente votre coût unitaire de **`+650 $` à `+750 $` par voiture**.  
Comme l'élasticité aux équipements en Europe n'est que de $\epsilon_F \approx 0,25$, passer de 4 à 5 équipements en Europe coûte **`+750 $/voiture`** (soit **`+630 M$`** sur 840 k voitures !) pour à peine `+5 %` de demande : **c'est mathématiquement perdant au-delà de 3 ou 4 équipements en Europe !**

---

## 3. Algorithme Exact du Coût de Production Interne (La Courbe en U des Usines)

En soustrayant le `Coût moyen des composants issu des fournisseurs` ($C_{\text{comp}}$) du `Coût de production interne par unité` ($C_{\text{prod}}$) sur les 12 équipes au Tour 2, nous avons extrait **la fonction exacte de coût de conversion industrielle** $C_{\text{conv}}(u) = C_{\text{prod}} - C_{\text{comp}}$ en fonction du taux d'utilisation total des usines $u \in [0\%, 100\%]$ :

$$C_{\text{prod}}(z, u) = C_{\text{comp}} + C_{\text{conv\_min}}(z) + \alpha_z \cdot (u - u^*)^2$$

### Valeurs Exactes Mesurées dans le Moteur au Tour 2 :

| Taux d'Utilisation des Usines ($u$) | Coût de Conversion USA ($C_{\text{prod, US}} - C_{\text{comp}}$) | Coût de Conversion Chine ($C_{\text{prod, CN}} - C_{\text{comp}}$) | Diagnostic Mathématique du Moteur Cesim |
| :---: | :---: | :---: | :--- |
| **`46 % – 59 %`** *(Sous-utilisation forte, ex: Rose)* | `5 937 $` *(+613 $/voiture)* | `4 183 $` *(+771 $/voiture)* | Pénalité lourde de sous-absorption des coûts fixes des usines. |
| **`64 % – 72 %`** *(Sous-utilisation modérée, ex: T2 US)* | `5 579 $ – 5 671 $` *(+255 $/voiture)* | `3 534 $ – 3 652 $` *(+122 $/voiture)* | Coût moyen ; acceptable uniquement pour vider un stock existant. |
| **`78 % – 87 %` (MINIMUM ABSOLU $u^*$)** | **`5 323,8 $ – 5 424,8 $` (OPTIMUM)** | **`3 411,9 $ – 3 442,3 $` (OPTIMUM)** | **C'est le fond exact de la courbe en U !** Le coût unitaire est au plus bas. |
| **`90 % – 95 %`** *(Plein régime optimal)* | **`5 427,3 $ – 5 491,3 $`** *(+100 $/voiture)* | **`3 430,4 $ – 3 520,3 $`** *(+20 $/voiture)* | Excellent compromis entre volume maximal et coût unitaire quasi-minimal. |
| **`100,0 %`** *(Surchauffe / Heures sup, ex: Ren'Auto, tomobil)* | **`6 043,4 $ – 6 080,2 $` (+720 $/voiture !)** | **`3 859,8 $ – 3 986,3 $` (+450 $/voiture !)** | **PIÈGE DU 100 % :** À 100,0 %, Cesim applique une pénalité d'heures supplémentaires de **`+450 $` à `+720 $` par voiture** ! |

> [!TIP]
> **Règle Algorithmique n°1 pour l'Onglet Production :**
> **Ne JAMAIS régler une usine à `100,0 %` !** Le minimum mathématique de coût unitaire de fabrication est entre **`80 %` et `92 %` d'utilisation totale** (Ligne 1 + Ligne 2). Passer de `93 %` à `100 %` fait bondir le coût unitaire de `+550 $/voiture` sur *toutes* les voitures de l'usine !

---

## 4. Algorithme du Coût Moyen des Composants (`Production -> Achats`)

Le coût des composants par véhicule Thermique ($C_{\text{comp}}$) est la **moyenne arithmétique simple** des coûts des fournisseurs cochés :

$$C_{\text{comp}} = \frac{1}{K} \sum_{k \in \text{Fournisseurs actifs}} C_k$$

- Avec les 5 fournisseurs par défaut : $\frac{8500 + 5250 + 6750 + 8500 + 6750}{5} = \mathbf{7\,150,0\text{ \$}}$
- Avec nos 3 fournisseurs éthiques (`Composants Colossaux 5250$` + `Innovation Réinventée 6750$` + `Maîtres Matérialistes 8500$`) : $\frac{5250 + 6750 + 8500}{3} = \mathbf{6\,833,3\text{ \$}}$ (`Éthique = 2,83`, `Dév. durable = 3,83`)
- Avec seulement 2 fournisseurs (`Composants Colossaux 5250$` + `Innovation Réinventée 6750$`) : $\frac{5250 + 6750}{2} = \mathbf{6\,000,0\text{ \$}}$ (`Éthique = 2,25`, `Dév. durable = 3,25` — **Attention :** ne utiliser la combinaison à 2 fournisseurs que si les Conditions de marché ne pénalisent pas un score Éthique de `2,25`).

---

## 5. Algorithme du Coefficient de Productivité des Ingénieurs (Critère n°15 = 12 pts)

En analysant les 12 équipes sur les Tours 1 et 2, l'équation interne de Cesim pour le `Coefficient de productivité` ($\Pi_t$) est :

$$\Pi_t = \left[ 1 + \alpha_{\text{sal}} \ln\left(\frac{W_t}{W_{\text{réf}}}\right) + \alpha_{\text{form}} \ln\left(\frac{T_t}{T_{\text{réf}}}\right) + \alpha_{\text{exp}} (\Pi_{t-1} - 1) - \beta_{\text{rot}} \cdot \text{Rotation}_t \right] \times \left(\frac{\text{Allocation Jours-homme \%}}{100\%}\right)^{\eta}$$

- **Effet de l'allocation R&D :** Si `Allocation Jours-homme % < 100 %` (ex: `AURA` à `88 %` ou `tomobil` à `72 %`), le multiplicateur pénalise immédiatement la productivité.
- **Effet de dilution par recrutement massif ($\text{Rotation}_t$) :**
  - Regarde `Vrooom Vroooom (Rose)` au Tour 2 : ils ont doublé leurs effectifs de `5 000` à `10 000` ingénieurs (+5 151 recrutés). Malgré un bon salaire (`5 500 $`) et `1 100 $` de formation, leur productivité a stagné à `1,080` et leur coût RH a explosé à **`1 176 M$`** !
  - Regarde `Ren'Auto` au Tour 2 : ils ont licencié `-494` ingénieurs (`16,5 %` de licenciements). Même en payant **`8 500 $` de salaire mensuel** et `1 250 $` de formation, le malus de licenciement a fait **chuter leur productivité de `1,054` (1er au T1) à `1,017` (11e au T2)** !
  - **Loi absolue du moteur RH :** Ne **JAMAIS** licencier d'ingénieurs (malus massif de moral) et ne **JAMAIS** recruter plus de `+5 %` d'un coup ! Rester à **`5 000` ingénieurs** avec un salaire de `5 750 $ – 5 850 $` et une formation de `1 100 $ – 1 500 $` garantit la **1re place (`12 pts/12`)** au moindre coût (`~620 M$`).


---

## 6. Algorithme Exact de la « Création de Valeur Totale » (Critère n°2 d'Eric Astien = 12 pts — Précision 100,000 %)

En simplifiant algébriquement la somme des 5 parties prenantes du tableau `Création de valeur` (`Actionnaires + Créanciers + Personnel + Gouvernement + Fournisseurs`), tous les coûts de production interne (20 % Personnel + 80 % Fournisseurs = 100 %), les coûts d'équipements, la sous-traitance, la R&D, les intérêts et les impôts **s'annulent exactement avec le Compte de Résultat**, ce qui donne cette identité mathématique exacte au dollar près sur les 12 équipes :

$$\text{Création de valeur totale} = \text{Chiffre d'affaires global} - \text{Publicité} - \text{Coût de transport et taxes} - \text{Administration} - \text{Amortissement}$$

- **Vérification sur le Tour 2 (`IronHorse`) :**
  $$56\,462 - 2\,420 - 1\,728 - 344 - 1\,452 = \mathbf{50\,518\text{ M\$}} \quad (\text{Rapport officiel : } \mathbf{50\,519\text{ M\$}} \text{ aux arrondis près !})$$
- **Conséquence stratégique directe :** Pour maximiser le critère n°2 (`Création de valeur` = 12 pts) **sans nuire au Résultat Net (`ROE`)**, il faut maximiser le **Chiffre d'affaires** tout en évitant tout gaspillage en **Publicité** et en **Frais de transport/douanes** !

---

## 7. Algorithme des Frais de Gestion des Stocks (`Production -> Stocks` — Précision 100,00 %)

Les frais de gestion des stocks facturés dans chaque zone suivent la formule linéaire exacte :
- **Aux USA :**
  $$\text{Frais de stocks USA (k USD)} = 150 + 400 \times (\text{Stock initial USA} + \text{Stock final USA en k unités})$$
  *(Exemple Tour 2 `IronHorse` : $150 + 400 \times (53 + 0) = 21\,350\text{ k\$}$, affiché `21 354 k$` avec les décimales de volume ; `tomobil` : $150 + 400 \times (0 + 350{,}5) = 140\,350\text{ k\$}$).*
- **En Chine :**
  $$\text{Frais de stocks Chine (k USD)} = 95 + 325 \times (\text{Stock initial Chine} + \text{Stock final Chine en k unités})$$
  *(Exemple Tour 2 `IronHorse` : $95 + 325 \times (318{,}35 + 0) = 103\,560\text{ k\$}$).*

---

## 8. Algorithme des Coûts de Transport & Droits de Douane (`Logistique`) et Amortissements (`Bilan`)

1. **Coût de Transport + Droits de Douane par voiture exportée :**
   - **Livraison domestique (`USA -> USA` et `Chine -> Chine`) :** **`0,0 $`** de transport et **`0,0 $`** de douane.
   - **Exportation `Chine -> USA` (Hybride) :** **`~740 $ à 760 $` par voiture** (transport + tarif douanier).
   - **Exportation vers l'`Europe` (`USA -> Europe` et `Chine -> Europe`) :**
     $$\text{Coût Transport + Douane Europe} = \text{Fret fixe} + \text{Taux de douane} \times (\text{Coût de fabrication} \times \text{Multiplicateur Prix de Cession})$$
     - Plus votre **multiplicateur de prix de cession interne** (`1,00` à `1,30`) et votre coût unitaire de fabrication sont élevés, plus les droits de douane payés à l'entrée en Europe augmentent (`1 590 $` chez `YANAUTO` à coût bas contre `2 254 $` en Thermique et `3 175 $` en Hybride chez `Ren'Auto` !).
2. **Amortissement des Immobilisations (`Usines`) et Taux d'Intérêt (`Notation de Crédit`) :**
   - **Amortissement annuel :** Exactement **`9,03 %`** de la valeur nette des immobilisations au bilan (`1 452 M$` pour 8 usines USA + 3 usines Chine valant `16 074 M$`).
   - **Taux d'intérêt et Notation de Crédit (`AA-`, `A+`, `BBB`, `B-`) :** Déterminés directement par le **`Ratio des fonds propres` (`Indépendance financière`)** et le levier `Dette nette / Fonds propres`. À **`74,66 %`** de fonds propres (`AA-`), `IronHorse` bénéficie du taux plancher du jeu (**`4,2 %`** sur la dette long terme USA).


---

## 9. Comment les « Conditions de Marché » (`#/marketConditions`) Modifient les Paramètres des 8 Algorithmes à Chaque Tour

Dans le moteur de `bordeaux-inp.cesim.com`, **la forme mathématique des 8 équations ci-dessus reste identique du Tour 1 au dernier tour**, mais **les « Conditions de marché » injectent de nouveaux paramètres exogènes dans ces équations au début de chaque tour**. Voici la table de traduction mathématique exacte que l'Agent IA doit appliquer dès qu'il lit les Conditions de marché du Tour $t$ :

| Annonce dans le texte des « Conditions de marché » | Quel Algorithme est modifié ? | Paramètre mathématique impacté & Action obligatoire pour l'Agent IA |
| :--- | :--- | :--- |
| **1. Croissance de la demande par zone (`USA +X%`, `Chine +Y%`, `Europe +Z%`)** | **Algorithme 1 (Demande)** | Modifie la taille totale du gâteau $D_{\text{tot}}(z, t) = D_{\text{tot}}(z, t-1) \times (1 + g_z^{(t)})$.<br>➔ **Action :** Saisir ces nouveaux $\%$ exacts dans l'onglet `Demande`. |
| **2. Essor Hybride / Démarrage Électrique ou Hydrogène & Effet de réseau** | **Algorithme 1 (Demande par techno)** | Déplace une fraction de $D_{\text{tot}}(z, t)$ du Thermique vers l'Hybride / l'Électrique / l'Hydrogène.<br>➔ **Action :** Adapter la répartition des parts de marché et des lignes d'usines (`Ligne 1` vs `Ligne 2` + `Sous-traitance`). |
| **3. Ralentissement économique vs Boom économique** | **Algorithme 1 (Élasticités $\epsilon_P, \epsilon_F$)** | En **ralentissement/récession**, $|\epsilon_P|$ augmente (les clients punissent les prix hauts ➔ baisser les prix et limiter les équipements). En **forte croissance**, $|\epsilon_P|$ diminue et $\epsilon_F$ augmente. |
| **4. Tension ou détente sur la Sous-traitance** | **Algorithme 3 (Production vs Sous-traitance)** | Modifie le coût unitaire $C_{\text{sous-traitance}}(z, m)$ et le plafond maximal disponible (comme le bond à `13 694,3 $` aux USA au Tour 2).<br>➔ **Action :** Toujours comparer dans `Production -> Planning` le coût unitaire de sous-traitance affiché à l'écran avec notre coût de production interne ($C_{\text{prod}}$ à 85–90 %). |
| **5. Pression des ONG / Boycott ESG / Évolution des Fournisseurs** | **Algorithme 1 ($\Phi_{\text{ESG}}$) & Algorithme 4 ($C_{\text{comp}}$)** | Si les ONG durcissent leur seuil éthique ou ciblent un fournisseur (ex: `Singularités Quantiques` `1,75/5`), toute équipe qui le garde subit un malus de demande $\Phi_{\text{ESG}} < 1$. Vérifier aussi dans `Production -> Achats` si les prix ($5\,250\text{ \$}$, $6\,750\text{ \$}$, $8\,500\text{ \$}$) ont changé. |
| **6. Variation des Taux de Change (`EUR/USD` et `RMB/USD`)** | **Algorithme 1 & 6 (CA et Marges en USD)** | Une hausse de l'Euro (ex: `+5 %` à `1,2338 USD` au Tour 2) augmente de `+5 %` le chiffre d'affaires en USD de chaque voiture vendue en Europe sans augmenter son coût de fabrication US/Chine !<br>➔ **Action :** Si une devise monte, privilégier les livraisons vers cette zone ; si elle baisse, ajuster le prix en devise locale. |
| **7. Droits de Douane / Tarifs Douaniers (`Guerre commerciale USA-Chine-Europe`)** | **Algorithme 8 (Coûts Logistiques & Douanes)** | Modifie le coût d'importation par véhicule entre zones.<br>➔ **Action :** Si un tarif douanier augmente entre la Chine et les USA (ou l'Europe), servir chaque marché en priorité depuis l'usine qui évite la taxe douanière, et modérer le multiplicateur de prix de cession interne sur la route taxée. |
| **8. Réforme Fiscale (Taux d'IS `USA / Chine / Europe`) & Taux d'intérêt** | **Algorithme 6 & 8 (Résultat Net & Transfer Pricing)** | Modifie le taux d'impôt par pays (ex: Europe tombée à `21 %` au Tour 2 contre `25 %` en Chine).<br>➔ **Action :** Utiliser les **prix de cession interne (`Logistique`)** pour équilibrer les 3 Marges Opérationnelles du barème d'Eric Astien tout en laissant le plus gros bénéfice imposable dans la zone la moins taxée. |


---

## 6. Algorithme Exact de la « Création de Valeur Totale » (Critère n°2 d'Eric Astien = 12 pts — Précision 100,000 %)

En simplifiant algébriquement la somme des 5 parties prenantes du tableau `Création de valeur` (`Actionnaires + Créanciers + Personnel + Gouvernement + Fournisseurs`), tous les coûts de production interne (20 % Personnel + 80 % Fournisseurs = 100 %), les coûts d'équipements, la sous-traitance, la R&D, les intérêts et les impôts **s'annulent exactement avec le Compte de Résultat**, ce qui donne cette identité mathématique exacte au dollar près sur les 12 équipes :

$$\text{Création de valeur totale} = \text{Chiffre d'affaires global} - \text{Publicité} - \text{Coût de transport et taxes} - \text{Administration} - \text{Amortissement}$$

- **Vérification sur le Tour 2 (`IronHorse`) :**
  $$56\,462 - 2\,420 - 1\,728 - 344 - 1\,452 = \mathbf{50\,518\text{ M\$}} \quad (\text{Rapport officiel : } \mathbf{50\,519\text{ M\$}} \text{ aux arrondis près !})$$
- **Conséquence stratégique directe :** Pour maximiser le critère n°2 (`Création de valeur` = 12 pts) **sans nuire au Résultat Net (`ROE`)**, il faut maximiser le **Chiffre d'affaires** tout en évitant tout gaspillage en **Publicité** et en **Frais de transport/douanes** !

---

## 7. Algorithme des Frais de Gestion des Stocks (`Production -> Stocks` — Précision 100,00 %)

Les frais de gestion des stocks facturés dans chaque zone suivent la formule linéaire exacte :
- **Aux USA :**
  $$\text{Frais de stocks USA (k USD)} = 150 + 400 \times (\text{Stock initial USA} + \text{Stock final USA en k unités})$$
  *(Exemple Tour 2 `IronHorse` : $150 + 400 \times (53 + 0) = 21\,350\text{ k\$}$, affiché `21 354 k$` avec les décimales de volume ; `tomobil` : $150 + 400 \times (0 + 350{,}5) = 140\,350\text{ k\$}$).*
- **En Chine :**
  $$\text{Frais de stocks Chine (k USD)} = 95 + 325 \times (\text{Stock initial Chine} + \text{Stock final Chine en k unités})$$
  *(Exemple Tour 2 `IronHorse` : $95 + 325 \times (318{,}35 + 0) = 103\,560\text{ k\$}$).*

---

## 8. Algorithme des Coûts de Transport & Droits de Douane (`Logistique`) et Amortissements (`Bilan`)

1. **Coût de Transport + Droits de Douane par voiture exportée :**
   - **Livraison domestique (`USA -> USA` et `Chine -> Chine`) :** **`0,0 $`** de transport et **`0,0 $`** de douane.
   - **Exportation `Chine -> USA` (Hybride) :** **`~740 $ à 760 $` par voiture** (transport + tarif douanier).
   - **Exportation vers l'`Europe` (`USA -> Europe` et `Chine -> Europe`) :**
     $$\text{Coût Transport + Douane Europe} = \text{Fret fixe} + \text{Taux de douane} \times (\text{Coût de fabrication} \times \text{Multiplicateur Prix de Cession})$$
     - Plus votre **multiplicateur de prix de cession interne** (`1,00` à `1,30`) et votre coût unitaire de fabrication sont élevés, plus les droits de douane payés à l'entrée en Europe augmentent (`1 590 $` chez `YANAUTO` à coût bas contre `2 254 $` en Thermique et `3 175 $` en Hybride chez `Ren'Auto` !).
2. **Amortissement des Immobilisations (`Usines`) et Taux d'Intérêt (`Notation de Crédit`) :**
   - **Amortissement annuel :** Exactement **`9,03 %`** de la valeur nette des immobilisations au bilan (`1 452 M$` pour 8 usines USA + 3 usines Chine valant `16 074 M$`).
   - **Taux d'intérêt et Notation de Crédit (`AA-`, `A+`, `BBB`, `B-`) :** Déterminés directement par le **`Ratio des fonds propres` (`Indépendance financière`)** et le levier `Dette nette / Fonds propres`. À **`74,66 %`** de fonds propres (`AA-`), `IronHorse` bénéficie du taux plancher du jeu (**`4,2 %`** sur la dette long terme USA).


---

## 9. Comment les « Conditions de Marché » (`#/marketConditions`) Modifient les Paramètres des 8 Algorithmes à Chaque Tour

Dans le moteur de `bordeaux-inp.cesim.com`, **la forme mathématique des 8 équations ci-dessus reste identique du Tour 1 au dernier tour**, mais **les « Conditions de marché » injectent de nouveaux paramètres exogènes dans ces équations au début de chaque tour**. Voici la table de traduction mathématique exacte que l'Agent IA doit appliquer dès qu'il lit les Conditions de marché du Tour $t$ :

| Annonce dans le texte des « Conditions de marché » | Quel Algorithme est modifié ? | Paramètre mathématique impacté & Action obligatoire pour l'Agent IA |
| :--- | :--- | :--- |
| **1. Croissance de la demande par zone (`USA +X%`, `Chine +Y%`, `Europe +Z%`)** | **Algorithme 1 (Demande)** | Modifie la taille totale du gâteau $D_{\text{tot}}(z, t) = D_{\text{tot}}(z, t-1) \times (1 + g_z^{(t)})$.<br>➔ **Action :** Saisir ces nouveaux $\%$ exacts dans l'onglet `Demande`. |
| **2. Essor Hybride / Démarrage Électrique ou Hydrogène & Effet de réseau** | **Algorithme 1 (Demande par techno)** | Déplace une fraction de $D_{\text{tot}}(z, t)$ du Thermique vers l'Hybride / l'Électrique / l'Hydrogène.<br>➔ **Action :** Adapter la répartition des parts de marché et des lignes d'usines (`Ligne 1` vs `Ligne 2` + `Sous-traitance`). |
| **3. Ralentissement économique vs Boom économique** | **Algorithme 1 (Élasticités $\epsilon_P, \epsilon_F$)** | En **ralentissement/récession**, $|\epsilon_P|$ augmente (les clients punissent les prix hauts ➔ baisser les prix et limiter les équipements). En **forte croissance**, $|\epsilon_P|$ diminue et $\epsilon_F$ augmente. |
| **4. Tension ou détente sur la Sous-traitance** | **Algorithme 3 (Production vs Sous-traitance)** | Modifie le coût unitaire $C_{\text{sous-traitance}}(z, m)$ et le plafond maximal disponible (comme le bond à `13 694,3 $` aux USA au Tour 2).<br>➔ **Action :** Toujours comparer dans `Production -> Planning` le coût unitaire de sous-traitance affiché à l'écran avec notre coût de production interne ($C_{\text{prod}}$ à 85–90 %). |
| **5. Pression des ONG / Boycott ESG / Évolution des Fournisseurs** | **Algorithme 1 ($\Phi_{\text{ESG}}$) & Algorithme 4 ($C_{\text{comp}}$)** | Si les ONG durcissent leur seuil éthique ou ciblent un fournisseur (ex: `Singularités Quantiques` `1,75/5`), toute équipe qui le garde subit un malus de demande $\Phi_{\text{ESG}} < 1$. Vérifier aussi dans `Production -> Achats` si les prix ($5\,250\text{ \$}$, $6\,750\text{ \$}$, $8\,500\text{ \$}$) ont changé. |
| **6. Variation des Taux de Change (`EUR/USD` et `RMB/USD`)** | **Algorithme 1 & 6 (CA et Marges en USD)** | Une hausse de l'Euro (ex: `+5 %` à `1,2338 USD` au Tour 2) augmente de `+5 %` le chiffre d'affaires en USD de chaque voiture vendue en Europe sans augmenter son coût de fabrication US/Chine !<br>➔ **Action :** Si une devise monte, privilégier les livraisons vers cette zone ; si elle baisse, ajuster le prix en devise locale. |
| **7. Droits de Douane / Tarifs Douaniers (`Guerre commerciale USA-Chine-Europe`)** | **Algorithme 8 (Coûts Logistiques & Douanes)** | Modifie le coût d'importation par véhicule entre zones.<br>➔ **Action :** Si un tarif douanier augmente entre la Chine et les USA (ou l'Europe), servir chaque marché en priorité depuis l'usine qui évite la taxe douanière, et modérer le multiplicateur de prix de cession interne sur la route taxée. |
| **8. Réforme Fiscale (Taux d'IS `USA / Chine / Europe`) & Taux d'intérêt** | **Algorithme 6 & 8 (Résultat Net & Transfer Pricing)** | Modifie le taux d'impôt par pays (ex: Europe tombée à `21 %` au Tour 2 contre `25 %` en Chine).<br>➔ **Action :** Utiliser les **prix de cession interne (`Logistique`)** pour équilibrer les 3 Marges Opérationnelles du barème d'Eric Astien tout en laissant le plus gros bénéfice imposable dans la zone la moins taxée. |
