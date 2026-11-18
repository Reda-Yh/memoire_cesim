# ⚙️ RÈGLES PROFONDES & MÉCANIQUES DU MOTEUR CESIM (`ESYBIA2AS`)

Ce document résume toutes les lois économiques, formules internes et règles de déblocage des modules de la simulation Cesim Global Challenge (version Industrie Automobile Bordeaux INP).

---

## 📈 1. Module « Demande » & Dynamique des Marchés

### Structure des 3 Zones Géographiques
1. **USA (en USD)** : Grand marché mature. Sensibilité équilibrée au prix, aux équipements et à la publicité. Transition progressive vers l'Hybride (7,2 % du marché au Tour 2) puis l'Électrique.
2. **Chine (en RMB — taux ~6,625 RMB pour 1 USD)** : Marché en plus forte croissance (+7 % au T1, +8,5 % au T2). Les clients chinois sont sensibles au prix en RMB et apprécient les équipements.
3. **Europe (en EUR — taux monté à 1,2338 USD pour 1 EUR au Tour 2)** : Plus grand marché en volume Thermique (~11,5 M de véhicules) et **vache à lait financière du jeu** (marges opérationnelles de 35 % à 42 %, impôt sur les sociétés abaissé de 27 % à **21 %** au Tour 2 !). **Attention :** L'Europe ne possède **aucune usine** dans le jeu ; 100 % des voitures vendues en Europe sont importées depuis vos usines/sous-traitants USA et Chine !

### Fonctionnement des Prévisions de Demande dans l'interface
- Dans l'onglet `Demande`, vous saisissez :
  1. Vos **prévisions de croissance du marché (%)** pour USA, Chine, Europe (d'après le texte des `Conditions de marché`).
  2. Vos **parts de marché estimées (%)** par modèle (`Modèle 1 = Thermique`, `Modèle 2 = Hybride`, `Modèle 3 = Électrique`, etc.).
- **Crucial :** Les chiffres que vous tapez dans `Demande` **ne déterminent pas vos vraies ventes** lors du calcul du tour (vos vraies ventes dépendent de vos Prix, Équipements, Publicité face aux 11 concurrents). En revanche, vos estimations dans `Demande` **pilotent toutes les projections de votre onglet `Production` et de votre onglet `Budgets`**.
- **Règle absolue :** Ne jamais surestimer sa part de marché dans `Demande` ! Si vous tapez 10 % de part de marché dans `Demande` et réglez votre production dessus, mais que le marché réel ne vous achète que 8,5 %, vous finissez avec **350 000 voitures invendues en stock** (l'erreur du Tour 1). Toujours calibrer `Demande` de façon réaliste/prudente par rapport à vos parts de marché réelles du tour précédent (`~7,8 % - 9,0 %` aux USA, `~9,0 % - 9,5 %` en Chine, `~9,5 % - 10,2 %` en Europe).

---

## 🏭 2. Module « Production » (4 Sous-onglets : Planning, Stocks, Investissements, Achats)

### A. Production Interne (Courbe en U et Pertes en production)
- **Capacité par usine :**
  - **1 usine USA** = **`200 k` unités** de capacité brute (Coût d'achat d'une usine USA = `600 M$`). Au Tour 2, `IronHorse` possède **8 usines USA** (`1 600 k` de capacité brute).
  - **1 usine Chine** = **`250 k` unités** de capacité brute (Coût d'achat d'une usine Chine = `475 M$`). Au Tour 2, `IronHorse` possède **3 usines Chine** (`750 k` de capacité brute).
- **Pertes en production (`Scrap rate %`) :**
  - Aux USA : environ `4,4 %` en Thermique (`6,0 %` en Hybride).
  - En Chine : environ `6,5 %` en Thermique (`8,7 %` en Hybride).
  - Les unités affichées dans `Production interne, k unités` sont les unités **nettes** après pertes.
- **Loi du taux d'utilisation des usines :**
  - Si vous faites tourner une ligne d'usines à **faible capacité (`< 75 %`, ex: `64 %` aux USA au Tour 2)**, les coûts fixes des 8 usines sont répartis sur moins de voitures : le coût unitaire de production interne grimpe (ex: `12 453,6 $` au lieu de `11 650 $`).
  - **Zone optimale (Sweet Spot) :** Entre **`85 %` et `95 %` d'utilisation totale** (somme Ligne 1 + Ligne 2).

### B. Sous-traitance (`Outsourcing`) — Attention aux Chocs de Prix !
- La sous-traitance permet de produire sans usine, **uniquement pour les technologies où vous avez acheté au moins 1 licence ou débloqué la sous-traitance**.
- **PIÈGE CRITIQUE DÉCOUVERT AU TOUR 2 :** Le coût et le plafond de la sous-traitance **changent à chaque tour** selon les conditions de marché !
  - Au Tour 1, la sous-traitance Thermique USA coûtait `12 383 $` (moins cher que la production interne USA à `13 732 $`).
  - Au Tour 2, les conditions de marché ont annoncé une pénurie de sous-traitants aux USA : le plafond a chuté de `350 k` à `225 k` et le coût de sous-traitance Thermique USA a explosé à **`13 694,3 $`** (soit **`+1 240 $` plus cher** que nos usines internes USA !).
  - **Règle d'or :** Au début de chaque tour, regarder dans `Production -> Planning` le **coût unitaire de production interne** vs le **coût unitaire de sous-traitance**. Ne jamais utiliser une sous-traitance plus chère que vos usines internes s'il vous reste de la capacité interne disponible !

### C. Sous-onglet « Achats » (Fournisseurs de Composants & ESG — Ouvert au Tour 2)
Voici la table complète des 5 fournisseurs de composants du jeu :

| Fournisseur | Coût par voiture (USD) | Note Image / ESG (sur 5) | Stratégie Optimale recommandée |
| :--- | :---: | :---: | :--- |
| **Composants Colossaux** | **`5 250 $`** *(Le moins cher)* | `2,00 / 5` | **TOUJOURS COCHER (Oui)** — Indispensable pour abaisser le coût unitaire. |
| **Innovation Réinventée** | **`6 750 $`** | `3,50 / 5` | **TOUJOURS COCHER (Oui)** — Excellent rapport coût / éthique. |
| **Maîtres Matérialistes** | **`8 500 $`** | `4,50 / 5` *(Meilleure éthique)* | **COCHER (Oui)** si les ONG menacent de boycotter les entreprises à faible score ESG (permet d'avoir **`6 833,3 $`** de coût moyen avec une excellente note Développement Durable de **`3,83 / 5`** et Éthique **`2,83 / 5`**). |
| **Singularités Quantiques** | `6 750 $` | **`1,75 / 5` (PIRE NOTE)** | **TOUJOURS DÉCOCHER (Non) !** C'est le fournisseur le moins éthique du jeu (`1,75/5`), cible directe du boycott des ONG annoncé au Tour 2. |
| **Fusions Dynamiques** | `8 500 $` *(Très cher)* | `4,00 / 5` | **TOUJOURS DÉCOCHER (Non) !** Aussi cher que Maîtres Matérialistes (`8 500 $`) mais moins bien noté (`4,00` vs `4,50`). |

> **Astuce observée au Tour 2 :** Deux équipes (`AURA` et `YANAUTO`) n'ont coché que `Composants Colossaux (5 250 $)` + `Innovation Réinventée (6 750 $)`, obtenant un coût composants de **`6 000,0 $`** (-833 $/voiture) avec Éthique `2,50` et Dév. durable `3,50`. Vérifier dans le rapport / conditions de marché du Tour 3 s'il y a une contrainte de capacité par fournisseur ou une pénalité ESG avant de retirer `Maîtres Matérialistes`.

---

## 👩‍🔬 3. Modules « RH » et « R&D »

### A. Ressources Humaines (Comment garder 12/12 en Productivité Ingénieurs)
- **Nombre d'employés optimal :** **`5 000`** (ou `5 000 -> 5 200` max). Ne jamais recruter 8 000 à 12 000 ingénieurs : cela coûte `800 M$` à `1 500 M$` par tour et fait chuter le coefficient de productivité à cause des nouveaux recrutés.
- **Prévision de départs volontaires (%) :** Recopier le taux réel du tour précédent (`2,4 %` à la fin du Tour 2 pour `IronHorse`).
- **Salaire mensuel (USD) :** Augmenter de `+100 $` à `+150 $` par tour pour suivre l'inflation salariale et rester devant `Vrooom Vroooom` et `MO'THOR` (ex: `5 500 $` au T1 ➔ `5 600 $` au T2 ➔ **`5 750 $` ou `5 800 $` au T3**).
- **Budget Formation mensuel (USD) :** `1 000 $` à `1 100 $` (maintient la productivité n°1 à **`1,085+`**).

### B. R&D Interne vs Achat de Licences
- **Capacité R&D disponible :** $\text{Nombre d'ingénieurs} \times 250 \text{ jours-homme}$ (soit **`1 250 000` jours-homme** pour `5 000` ingénieurs).
- **RÈGLE ABSOLUE :** La somme des jours-homme alloués (Thermique + Hybride + Électrique + Hydrogène) doit **TOUJOURS faire exactement 100,0 % (`1 250 000` jours-homme)** !
- **Différence entre R&D interne et Licence :**
  - **R&D interne (Jours-homme) :** Gratuit en cash (déjà payé via les salaires RH), mais débloque l'équipement `N+1` **au tour suivant (`t+1`)**.
  - **Achat de licence :** Coûte très cher en cash immédiatement (`200 M$` à `2 000 M$`), mais débloque l'équipement `N+1` **immédiatement pour le tour en cours (`t`)**.
  - **Attention au gaspillage :** Dans l'onglet `R&D`, regardez le nombre de jours-homme restants pour franchir le prochain palier (affiché sur la barre de progression). Si vous mettez déjà assez de jours-homme internes pour franchir le palier et que vous n'avez pas besoin de cet équipement *ce tour-ci*, **n'achetez pas la licence** !

---

## 📣 4. Module « Marketing » (Prix, Équipements, Publicité)

- **Nombre d'équipements (`Features`) :**
  - Chaque équipement supplémentaire augmente l'attractivité mais coûte des centaines de millions de dollars en `Coûts des équipements`.
  - **Optimum prouvé :**
    - **Thermique :** `4` à `5` équipements max (`4` aux USA, `4` ou `5` en Chine, `3` ou `4` en Europe). Éviter `6` ou `7` équipements qui détruisent les marges opérationnelles.
    - **Hybride :** `2` à `3` équipements max.
- **Prix de vente :**
  - Toujours regarder le prix moyen des concurrents au tour précédent dans `Résultats par zone` :
    - **USA Thermique :** Zone compétitive autour de **`19 800 $ – 20 500 $`** (Hybride : `30 000 $ – 33 000 $`).
    - **Chine Thermique :** Zone compétitive autour de **`126 000 RMB – 130 000 RMB`** (Hybride : `210 000 RMB – 225 000 RMB`).
    - **Europe Thermique :** Zone compétitive autour de **`21 500 € – 22 500 €`** (Hybride : `31 000 € – 34 000 €`). *(Attention : comme l'Euro vaut `1,2338 $`, `22 000 €` rapporte `27 144 $` par voiture !)*
- **Publicité :**
  - Loi des rendements décroissants (Dorfman-Steiner) : **`550 M$` à `750 M$`** par modèle Thermique actif, **`200 M$` à `300 M$`** par modèle Hybride actif. Ne jamais mettre `2 000 M$` par zone comme `Ren'Auto`.

---

## 🚢 5. Module « Logistique » & Prix de Cession Interne (`Transfer Pricing`)

- **Ordre de priorité des livraisons :**
  - Les usines sont aux **USA** et en **Chine**. L'**Europe** est livrée par exportation.
  - Si vous mettez `Priorité 1 = Marché domestique (USA/Chine)` et `Priorité 2 = Europe`, toute baisse de production privera l'Europe de voitures (alors que l'Europe est la zone la plus rentable du jeu !).
  - Si votre production totale couvre 100 % de la demande, l'ordre `1 / 2 / 3` n'entraîne aucune rupture. Mais assurez-vous toujours que l'Europe reçoit 100 % de ses voitures !
- **Prix de cession interne (Multiplicateur du coût direct : `1,00` à `1,30`) :**
  - Quand les USA ou la Chine exportent une voiture vers l'Europe, ils la facturent à la filiale Europe à $\text{Coût unitaire} \times \text{Multiplicateur}$.
  - **Impact sur le barème d'Eric Astien :**
    - Le barème note séparément la **Marge Opérationnelle US (12 pts)**, la **Marge Opérationnelle Asie (12 pts)** et la **Marge Opérationnelle Europe (12 pts)**.
    - En Europe, la marge opérationnelle est naturellement énorme (`38 %` à `42 %`), alors qu'aux USA (`5 % - 8 %`) et en Chine (`9 % - 15 %`) elle est plus faible.
    - En mettant un multiplicateur de prix de cession de **`1,15` à `1,25`** (USA -> Europe et Chine -> Europe), vous transférez une partie de la marge géante de l'Europe vers le chiffre d'affaires et l'EBIT des **USA** et de la **Chine**, ce qui fait grimper vos points sur `Marge Opérationnelle US` et `Marge Opérationnelle Asie` tout en gardant l'Europe autour de `35-37 %` !

---

## 💰 6. Module « Finance » (Dettes Long Terme, Transferts Internes, Dividendes)

1. **Transferts de trésorerie entre sociétés du groupe :**
   - L'Europe encaisse d'énormes bénéfices mais n'a ni usine ni dette long terme. Son cash s'accumule inutilement (`9 301 M$` fin Tour 2).
   - Les transferts passent par la maison-mère **USA** :
     - `Transfert depuis l'Europe (vers USA)` : saisir un montant positif (ex: `6 000 000` k USD = 6 Mds $) pour rapatrier le cash d'Europe vers les USA.
     - `Transfert vers la Chine (depuis USA)` : saisir un montant positif si la Chine a besoin de cash, ou négatif si la Chine a trop de cash et doit en renvoyer aux USA.
2. **Variation dette à long terme (k USD) :**
   - Saisir un nombre **négatif** (ex: `-4 000 000` k USD = `-4 Mds $`) **rembourse** la dette long terme aux USA.
   - **Double bénéfice pour le barème :**
     - Réduit le total du passif ➔ fait exploser le **`Ratio des fonds propres` (`Indépendance financière` = 12 pts)** (passé de `49,7 %` à `74,66 %` au Tour 2 !).
     - Supprime les intérêts financiers (`Charges financières nettes` tombées à `132 M$` contre `1 478 M$` chez `tomobil`) et améliore la notation de crédit à **`AA-` / `AAA`**.
3. **Dividendes et Rachat d'actions (Quand le cash devient excédentaire à partir du Tour 3/4) :**
   - Une fois la dette long terme fortement réduite et l'`Indépendance financière` autour de `80 %–85 %`, garder `25 milliards $` de cash dormant dilue les `Capitaux propres` et freine le **`ROE` (`Résultat Net / Capitaux Propres` = 12 pts)**.
   - Verser un **dividende** ou faire un **rachat d'actions** réduit les capitaux propres au dénominateur et **propulse le ROE** tout en augmentant le retour aux actionnaires ! (En veillant à ce que le `Ratio des fonds propres` reste `> 78 %` pour garder 10-11 pts en Indépendance financière).
