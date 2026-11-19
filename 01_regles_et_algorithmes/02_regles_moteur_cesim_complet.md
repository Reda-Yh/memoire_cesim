# ⚙️ RÈGLES PROFONDES & MÉCANIQUES EXACTES DU MOTEUR CESIM (`ESYBIA2AS` — ENTRÉE TOUR 5)
> **Navigation :** [Index Recherche](../INDEX_RECHERCHE_AGENT_IA.md) · [Index Maître](../00_INDEX_AGENT_IA.md) · [README](../README.md) · [Outils & Scripts](../03_outils_et_scripts/README_OUTILS_ET_CHROME.md)

Ce document recense **100 % des mécaniques réelles** vérifiées sur `https://bordeaux-inp.cesim.com/` jusqu'au **Tour 5 inclus** (rapports [`tour_01..04_resultats_univers1.xls`](../04_rapports_tours/tour_04_resultats_univers1.xls), [`classement_officiel_tours_0_a_3_ESYBIA2AS.pdf`](../07_classements_officiels/classement_officiel_tours_0_a_3_ESYBIA2AS.pdf), conditions & événements T1–T5 dans [`06_conditions_marche_et_evenements/`](../06_conditions_marche_et_evenements), forum instructeur [`10_messages_prof/`](../10_messages_prof) et slides [`09_slides_cours/`](../09_slides_cours)).

---

## 📈 1. Modules « Conditions de Marché », « Événements » & « Demande »

### A. Dynamique Macroéconomique des 3 Zones (État Tours 4–5)
1. **USA (en USD) :** Marché en ralentissement (`+5 %` T2/T3 ➔ **`+4 %`** au Tour 4). Taux d'IS abaissé à **`20,0 %`** dès le Tour 4 (**le plus bas des 3 zones** !). Droits de douane `Chine → USA` à **`6,0 %`**. Au **Tour 5**, l'USD se renforce (`+5 %` contre RMB, `+2 %` contre EUR) et une pénurie des nappes + ouragans menacent le coût de l'eau USA.
2. **Chine (en RMB — `0,1493 USD` au T4 ➔ `0,1419 USD` au T5) :** Seule zone en très forte expansion (**`+10 %`** au T4). IS à **`24,0 %`** (le plus élevé). Baisse des coûts fixes admin au T5 (`65 000 k$` + `10 000 k$/usine`) et **nouveaux gisements de batteries** réduisant les coûts Hybride/Électrique dès le T5.
3. **Europe (en EUR — `1,2962 USD` au T4 ➔ `1,2703 USD` au T5) :** Historiquement la plus forte marge opérationnelle (`32 %–45 %`), IS à **`21,0 %`**. Demande globale en déclin (`-2 %` saisi au T4 et poursuivi au T5), mais reste le plus gros marché et bénéficie dès le **Tour 5** d'un **accord libre-échange `Chine → Europe` abaissant les douanes de `10 %` à `7,0 %`** ainsi que d'infrastructures **Hydrogène** en expansion *(attention : défaut temporaire des nouveaux conteneurs H2 au T5)*. **Rappel :** Aucune usine en Europe (`100 %` importé des USA et de Chine).

### B. Onglet « Événements » (`#/marketConditions` -> `Événements`, [`06_conditions_marche_et_evenements/`](../06_conditions_marche_et_evenements))
- **Tour 4 ([`tour_04_evenements.html`](../06_conditions_marche_et_evenements/tour_04_evenements.html)) — `Le pari du prêt écologique` (`GreenRock`) :** Refinancement à taux réduit jusqu'au Tour 6 sous engagement ESG (pénalité en cas de manquement). Refusé par `IronHorse` (`0 M$` dette LT).
- **Tour 5 ([`tour_05_evenements.html`](../06_conditions_marche_et_evenements/tour_05_evenements.html)) — Deux décisions stratégiques actives :**
  1. **`Le procès de la transparence` :** Divulgation sur les émissions de transport (`Aucune divulgation` / `Transparence sélective` / `Transparence totale`).
  2. **`Négociations sur les batteries` :** Choix technologique & environnemental (`Conserver les batteries actuelles` / `Sous traiter les batteries` / `Co-développer les batteries`).
  - *(Obligatoire : cliquer/survoler chaque option en direct sur Chrome pour lire son coût exact et son impact ESG avant de valider !)*

### C. Fonctionnement de l'Onglet « Demande »
- Les croissances (%) et parts de marché (%) saisies dans `Demande` **ne créent pas vos ventes réelles** (qui dépendent du Prix, Équipements, Pub et Scores ESG relatifs face aux 11 concurrents). Elles pilotent en revanche tous les calculs de `Production`, `Logistique` et `Prévisionnel financier`.
- **Règle absolue :** Garder des prévisions réalistes pour que `Stock initial + Production nette + Sous-traitance` corresponde à la demande réelle visée (`0 k` stock).

---

## 🏭 2. Module « Production » (`Planning`, `Stocks`, `Investissements`, `Achats`, `Impact Env.`)

### A. Production Interne, Courbe en U & Coût des Usines
- **Capacité brute d'une usine :** **USA = `200 k` unités/usine** | **Chine = `250 k` unités/usine**.
- **Coût d'achat d'une usine (évolue avec les améliorations de processus !) :**
  - Prix de base : `1 200 M$` (USA) / `1 050 M$` (Chine).
  - **Chaque amélioration de qualité des processus cochée s'ajoute définitivement au prix des futures usines !** Ex : après `Énergie (+11 M$/usine)` cochée par `IronHorse` au T3, une usine au T4 coûtait `1 211 M$` (USA) et `1 061 M$` (Chine) ; avec `CO2 (+7 M$)` + `Eau (+9 M$)`, ce surcoût s'ajoute aussi (`+16 M$` ➔ vérifier les montants exacts dans `Investissements` au Tour 5).
- **Délais usines (`t+2` construction, `t+1` paiement) :**
  - Achat au Tour $t$ ➔ **payé au Tour $t+1$** (`1 211 M$ × 1 US + 1 061 M$ × 3 CN = 4 394 M$` payés par `IronHorse` au Tour 4) ➔ **entre en production au Tour $t+2$** (`9 US / 6 Chine = 3 300 k` brute pour `IronHorse` dès le Tour 5 !).
  - Cession (vente) d'usine : capacité perdue à `t+1` (`-1`), paiement reçu à `t+1` (`90 %` de la valeur, ex: `1 089,9 M$` USA / `954,9 M$` Chine au T4).
- **Loi du taux d'utilisation (Courbe en U) :**
  - Optimal entre **`78 %` et `92 %`**. Ne **JAMAIS** mettre **`100,0 %`** : pénalité d'heures supplémentaires de `+450 $` à `+720 $/voiture` !

### B. Sous-traitance (`Outsourcing`) — Plafonds Partagés & Arbitrage Coûts
- **RÈGLE CRITIQUE DU PLAFOND PARTAGÉ :** Le maximum affiché en sous-traitance (`206 k` aux USA, `500 k` en Chine au T4) est **GLOBAL PAR ZONE** :
  $$\text{Sous-traitance Ligne 1} + \text{Sous-traitance Ligne 2} \le \text{Maximum de la zone}$$
  *(Impossible de mettre `100` Thermique + `170` Hybride quand le plafond USA est `206` : `171` Hybride laisse au max `35` Thermique.)*
- **Arbitrage Hybride :** La sous-traitance Chine Hybride (`~17 015 $` T2, `~19 112 $` T3/T4) reste **largement moins chère** que la production interne Hybride (`23 649 $ – 24 851 $` chez `Ren'Auto`/`MO'THOR` au T3 !). Privilégier **100 % des lignes internes sur le Thermique** tant que c'est le cas, et **sous-traiter l'Hybride en Chine (et aux USA si rentable)**.
- **Arbitrage Thermique :** Au Tour 4, la sous-traitance Thermique USA (`11 589,8 $` à `12 125,3 $`) était ponctuellement moins chère que nos usines internes pénalisées en capacité (`12 713 $`), mais avec nos `9 US / 6 CN` usines à plein rendement dès le Tour 5, nos propres usines redeviennent beaucoup plus rentables. Toujours comparer à l'écran !

### C. Leviers ESG de « Planning » (`Recyclabilité`, `Énergie Renouvelable`, `Processus`)

1. **Recyclabilité du produit & VERROU D'ENGAGEMENT (`Engagement`) :**
   - Niveaux disponibles : `Recyclage basique` | `Conception pour le démontage facile` | `Utilisation de matériaux recyclés (+0%)` | `Évaluation du cycle de vie` | `Systèmes de cycle fermé (+8% coût unitaire)`.
   - **RÈGLE CRITIQUE VÉRIFIÉE AU TOUR 4 :** Dès que la case **`Engagement`** est cochée sur un niveau (comme `Systèmes de cycle fermé` au Tour 3), Cesim verrouille ce plancher : **redescendre à un niveau inférieur rompt l'engagement et inflige une sévère pénalité de demande** (`POLRAMOS` a subi **`-5,7 %`** au Tour 3 !). `Systèmes de cycle fermé + Engagement = Oui` a rapporté **`+4,2 %` de demande** au Tour 3.

2. **Utilisation d'énergie renouvelable (`% USA` / `% Chine`) :**
   - Paramètres de coûts : fossile `0,15 $/kWh` (US) / `0,12 $/kWh` (CN) vs renouvelable `0,23 $/kWh` (US) / `0,19 $/kWh` (CN), soit environ `+76 $ à +105 $/voiture`.
   - **Impact demande au Tour 3 :** **`+12,8 %` à `100 %`** vs **`-7,8 %` à `30 %`** (écart énorme de `+20,6 %` !). Attention : le texte Tour 4 signale une hausse possible du prix des CER (`certificats d'énergie renouvelable`) due à la ruée générale — vérifier le coût affiché dans `Paramètres` au Tour 5.

3. **Améliorations de la qualité des processus (Cumulatives, Permanentes après le tour d'achat) :**
   Chaque case cochée s'applique aux usines existantes (**`11` usines** au T4, **`15` usines** [`9 US / 6 CN`] dès le T5 ; `coût = coût/usine × nb d'usines`), inflige un **malus temporaire UNIQUEMENT pendant le tour d'achat**, puis procure une réduction **permanente** sur tous les tours suivants :

| Amélioration | Réduction permanente | Coût / usine | Malus TEMPORAIRE (tour d'achat uniquement) | Statut `IronHorse` |
| :--- | :---: | :---: | :--- | :--- |
| **Consommation d'énergie** | **`-9,0 %` kWh** | `11 000 k$` | `-15,0 %` capacité temporaire | **Acquis au T3** (`0 %` malus dès T4) |
| **Émissions de CO2** | **`-12,0 %` CO2** | `7 000 k$` | **`-20,0 %` capacité temporaire** (`-20 %` cap. US & CN) | **NON coché au T4** (`Non` dans [`tour_04_decisions_ironhorse_yahya.html`](../05_decisions_prises/tour_04_decisions_ironhorse_yahya.html)) ➔ à arbitrer dès T5 |
| **Consommation d'eau** | **`-10,0 %` m3** | `9 000 k$` | **`+30,0 %` taux de pertes (scrap)** (`×1,3` pertes US & CN) | **NON coché au T4** (`Non` dans [`tour_04_decisions_ironhorse_yahya.html`](../05_decisions_prises/tour_04_decisions_ironhorse_yahya.html)) ➔ à arbitrer dès T5 |

- **Impact sur la demande mesuré au Tour 3 :** Avoir les **3 améliorations** actives a donné **`+20,9 %`** de boost demande (`Ren'Auto`, `GT-Auto`) contre `-0,3 %` pour 1 amélioration et `-8,2 %` pour 0 ! Une fois les 3 acquises, elles boostent le score Environnement ET la demande sur tous les tours restants (Tours 5–10) sans plus aucun coût ni malus temporaire !

### D. Sous-onglet « Achats » (Fournisseurs Dynamiques & Études `5 M$`)
- **Règles fixes :** Minimum **`2` fournisseurs** (`50 %` pénalité sur le coût si `< 2`), **`10 M$` (`10 000 k$`)** payés une seule fois pour activer un nouveau fournisseur jamais utilisé au tour précédent.
- **ÉVOLUTION DYNAMIQUE DES ÉTOILES :** Les notes `Qualité` et `Développement durable` changent à **chaque tour** !
  - Cocher un fournisseur tombé à `1★` (`Composants Colossaux` au T3) fait grimper le taux de pertes en usine (`5,1 % ➔ 7,1 %` US, `7,4 % ➔ 10,2 %` CN), détruit le `Score DDRS Fournisseurs` (`4,67` au lieu de `6,00`), baisse `Gouvernance` et inflige **`-5,5 %`** de malus demande !
- **Données relevées au Tour 4 (`Achats`) :**
  - **`Fusions Dynamiques`** (`8 500 $`) : `4★ Q / 3★ DD` *(valeur sûre haut de gamme)*.
  - **`Maîtres Matérialistes`** (`8 500 $`) : `3,5★ Q / 2,5★ DD` *(études : Amélioration T4 et Amélioration T5)*.
  - **`Innovation Réinventée`** (`6 750 $`) : `2,5★ Q / 3,5★ DD` *(études : Q Amélioration T4 / Stable T5 ; DD Stable T4/T5 — meilleur DD et choisi par 12/12 équipes au T3)*.
  - **`Composants Colossaux`** (`5 250 $`) : `1★ Q / 1★ DD` *(études : Amélioration annoncée T4 & T5 — attendre de vérifier sur l'écran T5 à combien d'étoiles il remonte réellement avant de le recocher ou de le couper !)*.
  - **`Singularités Quantiques`** (`6 750 $`) : `1★ Q / 1,5★ DD` sur l'écran live final T4 (`Image 1,25` au T3) *(ne jamais sélectionner sauf remontée massive confirmée à l'écran)*.

---

## 👩‍🔬 3. Modules « RH » (3 Sous-onglets) et « R&D »

### A. RH — Effectifs, Priorités de Formation & Politiques de Travail
1. **Effectifs & Coûts (`RH -> Effectifs et coûts`) :**
   - Au Tour 4, les **frais de recrutement ont doublé de `4,1 k$` à `8,2 k$`** par ingénieur, puis sont montés à **`8,4 k$`** au **Tour 5** (licenciement `74 / 84 / 110 k$`) et le marché souffre d'une pénurie d'ingénieurs R&D (taux de rotation en hausse).
   - **Ne JAMAIS licencier** (coût massif `72,8–108,8 k$/ing.` + effondrement de la productivité).
   - Comparaison T3 : `IronHorse` à `5 600` ingénieurs (`5 800 $ / 1 500 $`) = **`1,121` de productivité (`706 M$` coût)** ; `AURA` (`5 000` ing., `5 400 $ / 1 000 $`) = **`1,193` (#1)** grâce notamment à `Formation de base` cochée et zéro recrutement perturbateur !
2. **Priorités de Formation (`RH -> Priorités de formation`) — RÈGLE DE DILUTION :**
   - L'écran précise : *« Plus vous élargissez votre champ d'action, moins vos avantages seront ciblés. »*
   - **Preuve Tour 3 :** `IronHorse` avait coché **1 seule** priorité (`Éthique et lutte contre la corruption`) ➔ **`+11,7 %`** sur l'image/demande et **`#1 Impact Sociétal (3,98 = 12 pts)`** ! À l'opposé, `Ren'Auto` avait coché **les 5** ➔ seulement **`+1,6 %`** !
   - Effets vérifiés :
     - **`Formation de base` :** impact **majeur** sur l'efficacité R&D (réduit les jours-homme requis !), modéré sur la rotation, marginal sur l'image.
     - **`Santé et bien-être` :** impact **majeur** sur la rotation, modéré sur efficacité R&D et image.
     - **`Politiques de non-discrimination` :** impact **majeur** sur l'image publique *(particulièrement ciblé par les activistes USA au Tour 4 !)*.
     - **`Éthique et lutte contre la corruption` :** impact **majeur** sur l'image publique (`#1` Social au T3).
   - **Règle d'or :** Cocher **1 à 3 priorités max** alignées sur les Conditions de marché du tour.
3. **Politiques en Matière de Travail (`RH -> Politiques en matière de travail`) :**
   - **Règlementation du travail :** `Conformité standard` (`0` coût j-h) | `Initiatives d'engagement communautaire` (**prélève `150 000` jours-homme sur le pool R&D**, coût `~75-78 M$`!) | `Partenariat stratégique` (utilisé par `Ça Roule` au T3 ➔ `+8,7 %` Politiques travail & `3,98` Gouvernance !).
   - **Relations salariés & syndicats :** `Approche équilibrée` | `Collaboration syndicale` (bonus explicite annoncé dans Conditions T3) | `Concentration sur le bien-être`.
   - **Quotas postes de direction :** `Priorité modérée` | `Programmes de mentorat` (utilisé par `Ren'Auto` au T3 ➔ `4,24 = 12 pts` Gouvernance !).

### B. R&D (`R&D interne`, `Achat de licences`, `Ventes entre équipes`)
- Chaque ingénieur produit `250` jours-homme (au **Tour 5** avec `6 400` ingénieurs : `6 400 × 250 = 1 600 000` j-h brut ; **`1 450 000` j-h allouables** si `Initiatives d'engagement communautaire` consomme `150 000` j-h). Toujours allouer **`100 %`** !
- **R&D interne vs Licence :** Développer une nouvelle techno (`Électrique`, `Hydrogène`) ou des équipements en interne évite le paiement cash sec de licences (`300 à 984 M$` payés par `Ren'Auto/POLRAMOS/GT-Auto` au T3) et augmente la compétence interne, mais prend 1 à 3 tours.
- **Ventes/Achats de licences entre équipes ([`04_regles_ventes_licences_entre_equipes.pdf`](../08_manuels_et_planning/04_regles_ventes_licences_entre_equipes.pdf)) — RÈGLES & BUG CRITIQUE :**
  - **Acheteur :** Délai d'**1 tour** (`t+1`, disponible au tour suivant l'accord), paiement unique comptabilisé en **`Coût R&D`** au compte de résultat, **maximum `1` technologie achetée par tour** (re-vendable uniquement au tour après réception).
  - **Vendeur :** Le montant reçu est comptabilisé en **`Chiffre d'affaires`** (!), **maximum `3` équipes acheteuses par tour**. On peut vendre une techno **dès le tour où notre R&D interne est en train de la terminer** pour le tour suivant (ex : dès qu'`IronHorse` achève `Électrique` au Tour 5, on peut le vendre à 1 à 3 équipes retardataires !).
  - **Concordance exacte :** Acheteur et vendeur doivent saisir **exactement** les mêmes champs (`Équipe`, `Technologie`, `Prix en k USD`), sinon rien ne se passe à la clôture du tour.
  - ⚠️ **BUG DE RÉINITIALISATION SILENCIEUSE :** Il est **strictement interdit** d'acheter une technologie à une autre équipe ET de la développer en interne (ou d'acheter une licence Cesim) au cours du **même tour**. Si vous tentez de développer en interne une techno déjà saisie dans la ligne `Acheter` entre équipes, **Cesim réinitialise silencieusement votre ligne de licence**, annulant l'accord sans prévenir le partenaire !
- **Vérification Tour 5 :** Consulter immédiatement `#/rd` après clôture du Tour 4 pour voir si `Électrique` est terminé ou combien de jours-homme restent, et si **`Hydrogène`** vient de s'ouvrir en R&D interne !

---

## 📣 4. Module « Marketing » & « Certifications de Développement Durable »

- Coûts exacts par équipement proposé : **`700 $` (USA), `650 $` (Chine), `750 $` (Europe)** par unité vendue.
- **Efficacité publicitaire en baisse :** Les Conditions de marché Tours 3 & 4 répètent que les consommateurs sont *« plus irrités qu'impressionnés »* et *« de moins en moins sensibles aux campagnes publicitaires »*. Inutile de jeter `6 à 8 Mds$` de pub comme `Ren'Auto` ou `MO'THOR` : garder des budgets sobres (`~2,4–2,7 Mds$` au total) protège `Création de valeur` et `Résultat Net`.
- **Certifications de développement durable (`Marketing -> Certifications`) :**
  - `Pas de certification` = `0 pt` Astien (`0 $`)
  - **`Bronze`** (seuil `>= 2,75`, coût **`8 M$`**) = **`2 pts` Astien**
  - **`Argent`** (seuil `>= 3,25`, coût **`24 M$`**) = **`4 pts` Astien** *(débloqué par `IronHorse` à `3,28` au Tour 4 !)*
  - **`Or`** (seuil `>= 4,00`, coût **`40 M$`**) = **`6 pts` Astien** *(à sélectionner dès que notre score cumulé atteint `4,00`)*

---

## 🚢 5. Modules « Logistique » & « Impôts / Prix de Transfert » (DÉBLOQUÉ AU TOUR 4)

### A. Impôts — Prix de Transfert (`#/tax`, Nouveau au Tour 4 !)
- **Mécanique officielle vérifiée :** Le nouvel onglet `Impôts` permet de régler **4 multiplicateurs de prix de cession interne (`PCI` entre `1.00` et `2.00`)** relatifs au coût unitaire de fabrication :
  - `USA → Chine` | `USA → Europe` | `Chine → USA` | `Chine → Europe`
- **Impact comptable exact (slides cours [`09_slides_cours/`](../09_slides_cours) + résultats T4) :**
  - À `PCI = 1.00`, l'usine exportatrice refacture à `1,00 × coût unitaire` (marge opérationnelle de `0 $` à l'export pour les USA ou la Chine, tout le profit va en Europe !).
  - À `PCI = k > 1.00` sur `USA → Europe`, le **`Chiffre d'affaires ventes internes USA`** et l'**`EBIT USA`** augmentent de `(k - 1) × coût unitaire × volume exporté`, tandis que les **`Coûts d'importation Europe`** augmentent exactement du même montant *(donc `EBIT Europe` baisse d'autant)*.
  - **Exemple exact des slides d'Eric Astien (`IS USA = 20 %`, `IS Europe = 40 %`) :** À `PCI = 1,0`, USA est en perte de `-20 000` (`0` d'impôt) et Europe gagne `+30 000` (`12 000` d'impôt) ; passer à **`PCI = 1,2`** remonte le CA interne US de `100 000 ➔ 120 000`, absorbe la perte US (`-20 000 ➔ 0`, toujours `0` impôt) et descend le bénéfice Europe à `+10 000` (`4 000` d'impôt ➔ **économie nette de `8 000` d'impôt**).
  - **Confirmation Tour 4 vérifiée sur `IronHorse` :** Passer **`USA → Europe = 1.20`** au Tour 4 a redressé notre `Marge Opérationnelle US` de **`-0,98 %` (`4 pts`) ➔ `+8,05 %` (`8/12 pts`)** tout en maintenant `Coût moyen unitaire Europe` à `14 765 $` (`7/12 pts`, amélioré par rapport aux `15 027 $` du T3 !).
  - **Méthode globale du cours (`Strategic Intent` en 8 étapes & `4P / 4C`) :** Les slides d'Eric Astien rappellent la boucle de décision officielle dans l'ordre (`1. Conditions de marché ➔ 2. Demande ➔ 3. Production ➔ 4. Investissements ➔ 5. Marketing [4P vs 4C Client/Coût/Communauté/Commodité] ➔ 6. Logistique/PCI ➔ 7. R&D ➔ 8. Finances et Budget`).
  - **Arbitrage Fiscal (IS T4/T5 : USA `20 %` < Europe `21 %` < Chine `24 %`) :** Tester modérément `USA → Europe` (`1.20–1.30`) en vérifiant `Prévisionnel financier -> Bilan / Compte de résultat` face aux droits de douane (`13 %`), et **garder `Chine → Europe = 1.00`** car `24 % > 21 %`.

### B. Logistique & Droits de Douane (`Mise à jour Accord Tour 5`)
- Priorités de livraison par défaut optimales :
  - De `USA` : `1. USA, 2. Europe, 3. Chine` *(toujours servir le marché local à `0 $` de douane d'abord, jamais exporter `USA→Chine` à `23 %` !)*.
  - De `Chine` : `1. Chine, 2. Europe, 3. USA` *(**Nouvel accord libre-échange Tour 5 :** le droit de douane **`Chine → Europe` tombe de `10 %` à `7,0 %`** contre `13,0 %` depuis les USA ! Exploiter nos `6` usines chinoises pour alimenter l'Europe maximise à la fois la marge Europe et le Coût unitaire pondéré Europe !)*.

---

## 💰 6. Module « Finance » (Signes `+` / `-`, Dividendes & Augmentation de Capital T5+)

- **Emprunt long terme (`Augmenter (+) / réduire (-)` en `k USD`) :** `IronHorse` a soldé sa dette LT fin T4 (`0 M$` ➔ **`100,00 %` Indépendance Financière**, notation **`AAA`**).
- **Transferts internes (`k USD`) — NE JAMAIS INVERSER LES SIGNES :**
  - `USA → Chine (+), Chine → USA (-)` : **`+` envoie vers la Chine**, **`-` rapatrie vers les USA**.
  - `USA → Europe (+), Europe → USA (-)` : **`-` rapatrie de l'Europe vers les USA** ! *(Un `+` enverrait du cash USA vers l'Europe et risquerait un découvert USA !)*
- **Intérêts sur la trésorerie (Taux Tour 5) :** `Chine = 4,2 %` | `USA = 3,2 %` | **`Europe = 1,0 %`** (relevé de `0,7 %` à `1,0 %` par la BCE au Tour 5). Il reste rentable de concentrer l'excédent de cash en **Chine (`4,2 %`)** et aux **USA (`3,2 %`)**.
- **Nouveaux leviers Finance actifs dès Tour 5 ([slide 08](../09_slides_cours/08_tour5_finance_dividendes_et_rentabilite_action.jpeg) & [slide 09](../09_slides_cours/09_tour5_finance_augmentation_de_capital.jpeg)) — ⚠️ Bilan Maison Mère USA (« EU ») :**
  - **Notation des slides (`EU` = États-Unis) :** Dans les slides françaises du professeur, « **`EU` » signifie États-Unis** (maison mère où sont logées les `1 625 000 000` actions de nominal `2 $` = `3 250 M$` de capital social, vérifié dans `Bilan USA` du rapport `.xls` alors que `Capital social Europe = 750 M$`).
  - **`Dividendes` (`k USD`) :** Soutiennent le `Rendement net` et la `Rentabilité de l'action` (`Rt = (Cours_n - Cours_{n-1} + Dividende_n) / Cours_{n-1}`) ET réduisent les capitaux propres (ce qui augmente le `ROE = Résultat / Capitaux propres`, Critère #1 d'Eric Astien !). Attention : **le dividende est prélevé sur la trésorerie USA (`14 495 M$` fin T4)** — si le dividende dépasse le cash USA disponible, rapatrier du cash depuis l'Europe (`-` sur `USA → Europe`) pour éviter tout découvert USA et maintenir `100 %` d'Indépendance financière !
  - **`Augmentation de capital` :** Émission d'actions nouvelles au `Prix d'émission (PE)` créditant **la trésorerie USA (`+ n × PE`)**, le capital (`+ n × 2 $`) et la `Prime d'émission (+ n × (PE - 2 $))`. À **éviter** avec `33 Mds$` de cash et `0` dette, car émettre des actions **dilue** le `ROE` et le BPA !
