# 🧬 ALGORITHMES MATHÉMATIQUES & PARAMÈTRES EXACTS DU MOTEUR CESIM (`ESYBIA2AS` — TOUR 5)
> **Navigation :** [Index Recherche](../INDEX_RECHERCHE_AGENT_IA.md) · [Index Maître](../00_INDEX_AGENT_IA.md) · [README](../README.md) · [Outils & Scripts](../03_outils_et_scripts/README_OUTILS_ET_CHROME.md)

Ce fichier regroupe les équations internes vérifiées sur les rapports officiels de `bordeaux-inp.cesim.com` (`tour_01..04_resultats_univers1.xls`) et les tableaux de paramètres exacts relevés jusqu'au **Tour 5** ([`tour_05_conditions_marche.html`](../06_conditions_marche_et_evenements/tour_05_conditions_marche.html) & [`09_slides_cours/`](../09_slides_cours)).

---

## 1. Modèle de Demande & Part de Marché (Ordres de Grandeur Directionnels)

Pour chaque zone $z \in \{\text{USA}, \text{Chine}, \text{Europe}\}$ et technologie $m$, Cesim calcule un score d'attraction $A_{i,z,m}$ relatif aux 11 concurrents :

$$s_{i,z,m} = \frac{A_{i,z,m}}{\sum_{j=1}^{12} A_{j,z,m}}, \qquad A_{i,z,m} = \left(\frac{P_{i}}{\bar{P}}\right)^{\epsilon_P} \cdot \left(\frac{F_{i}}{\bar{F}}\right)^{\epsilon_F} \cdot \left(\frac{\text{Pub}_{i}}{\overline{\text{Pub}}}\right)^{\epsilon_A} \cdot \left(s_{i,z,m}^{(t-1)}\right)^{\gamma} \cdot \Phi_{\text{ESG}}(i)$$

> [!NOTE]
> **Statut scientifique des élasticités ci-dessous :** Estimées par régression sur les données de l'Univers 1 aux **Tours 1 et 2 uniquement**. Elles constituent d'excellents **ordres de grandeur directionnels** pour le positionnement relatif Prix / Équipements / Pub, mais ne sont pas des prédicteurs exacts à la décimale près (d'autant que les Conditions de marché Tours 3 & 4 réduisent explicitement l'élasticité à la publicité $|\epsilon_A|$ et amplifient le facteur $\Phi_{\text{ESG}}$).

| Zone — Thermique | Sensibilité Prix ($\epsilon_P$) | Sensibilité Équip. ($\epsilon_F$) | Sensibilité Pub ($\epsilon_A$) | Loi Tactique Directionnelle |
| :--- | :---: | :---: | :---: | :--- |
| **USA** | Forte (`~ -2,3 à -3,2`) | Modérée (`~ +0,4 à +0,5`) | Modérée (`~ +0,2 à +0,5`, en baisse) | Le prix domine les équipements (~5×) ; éviter de sur-pricer au-delà du marché. |
| **Chine** | Très forte (`~ -3,0 à -3,2`) | Élevée (`~ +0,6 à +0,9`) | Faible (`~ +0,17`, en baisse) | Marché le plus sensible au prix RMB et aux équipements (`6–8` éq.), peu sensible à la pub (`400–500 M$`). |
| **Europe** | Modérée-forte (`~ -1,9 à -2,7`) | **Faible (`~ +0,24 à +0,29`)** | Faible-modérée (en baisse) | Mettre 8–10 équipements en Europe détruit la marge (`+750 $/u/éq.`) ; `4–5` équipements suffisent. |

- **Redistribution des ruptures de stock :** Lorsqu'un concurrent est en `Demande insatisfaite > 0`, une partie importante de sa demande non servie se reporte automatiquement sur les équipes ayant encore du stock disponible.

---

## 2. Coût Exact des Équipements (`100 %` Exact dans `Paramètres`)

$$\text{Coût des équipements (USD)} = \text{Véhicules vendus} \times \text{Nombre d'équipements proposés} \times C_{\text{éq}}(z)$$

- **USA :** **`700,0 USD`** / équipement / voiture vendue.
- **Chine :** **`650,0 USD`** / équipement / voiture vendue.
- **Europe :** **`750,0 USD`** / équipement / voiture vendue.

---

## 3. Coût de Production Interne : La Courbe en U des Usines

Le coût de production unitaire interne vaut :
$$C_{\text{prod}}(z, u) = C_{\text{comp}} + C_{\text{conv\_min}}(z) + \alpha_z \cdot (u - u^*)^2 + \text{Malus}_{100\%}(u)$$

Valeurs de conversion hors composants ($C_{\text{prod}} - C_{\text{comp}}$) mesurées au Tour 2 sur les usines Thermiques :
- **Sous-utilisation (`46 % – 59 %`) :** `~5 937 $` USA (`+613 $`), `~4 183 $` Chine (`+771 $`).
- **Minimum absolu $u^*$ (`78 % – 87 %`) :** **`~5 324 – 5 425 $` USA**, **`~3 412 – 3 442 $` Chine**.
- **Plein régime optimal (`88 % – 94 %`) :** `~5 427 – 5 491 $` USA, `~3 430 – 3 520 $` Chine.
- **Piège du `100,0 %` :** Surcoût d'heures supplémentaires de **`+450 $` (Chine) à `+720 $` (USA) par voiture** sur toute la production !

---

## 4. Coût des Composants (`Production -> Achats`) & Pertes Usines

$$C_{\text{comp}} = \frac{1}{K} \sum_{k \in \text{Fournisseurs cochés}} C_k \qquad (\text{minimum } K \ge 2, \text{ sinon pénalité } +50\%)$$

- Activation d'un nouveau fournisseur : **`10 000 k USD`** une seule fois. Étude prévisionnelle : **`5 000 k USD`**.
- **Effet qualité sur le taux de pertes (scrap) observé :** Lorsque `Composants Colossaux (5 250 $)` est tombé à `1★ Q / 1★ DD` au Tour 3/4, le taux de pertes interne est passé de **`5,1 % ➔ 6,96 %` aux USA** et **`7,4 % ➔ 9,87 %` en Chine** (puis `9,09 %` / `12,92 %` pendant le malus temporaire `+30 % Eau` au T4) — réduisant les unités nettes vendables !

---

## 5. Coefficient de Productivité R&D & Coûts RH (`Paramètres Tour 5`)

- **Jours-homme par ingénieur :** **`250`** jours-homme/an. (`Initiatives communautaires` en prélève `150 000`).
- **Structure de coût RH (Paramètres T5 vs T4) :** Salaire = `70,0 %` du coût d'emploi ; autres coûts variables R&D = **`0,69 k$/employé/mois`** (T4 : `0,68 k$`) ; frais de recrutement = **`8,4 k$/employé`** (T4 : `8,2 k$`, T3 : `4,1 k$`) ; frais de licenciement = **`74,0 k$`** (`5–20%`), **`84,0 k$`** (`20–50%`), **`110,0 k$`** (`> 50%`).
- **Lois vérifiées :**
  1. Allouer **`< 100 %`** des jours-homme allouables dégrade directement la productivité.
  2. **Licencier** inflige un malus sévère (`Ren'Auto` tombé à `1,017` au T2).
  3. Cocher **`Formation de base`** (`RH -> Priorités de formation`) réduit sensiblement les jours-homme requis en R&D.

---

## 6. Création de Valeur Totale (`Critère n°2` — Identité Exacte Vérifiée)

$$\text{Création de valeur totale} = \text{Chiffre d'affaires global} - \text{Publicité} - \text{Transport et tarifs} - \text{Administration} - \text{Amortissement}$$

*(Vérifiée sur les 12 équipes aux Tours 1, 2 et 3 à l'arrondi près ; ex T2 `IronHorse` : `56 462 - 2 420 - 1 728 - 344 - 1 452 = 50 518 M$` vs `50 519 M$` rapport.)*

---

## 7. Frais de Gestion des Stocks (`Paramètres Exact Tour 3 & Tour 4`)

Paramètres officiels lus dans `Conditions de marché -> Paramètres` :
- **USA :** Coût fixe = **`150,00 k USD`** | Coût variable = **`800,00 USD / unité`** sur le stock moyen $\frac{S_{\text{init}} + S_{\text{fin}}}{2}$ :
  $$\text{Frais Stocks USA (k USD)} = 150 + 400 \times (S_{\text{init, US}} + S_{\text{fin, US}})$$
- **Chine :** Coût fixe = **`95,00 k USD`** | Coût variable = **`650,00 USD / unité`** sur le stock moyen :
  $$\text{Frais Stocks Chine (k USD)} = 95 + 325 \times (S_{\text{init, CN}} + S_{\text{fin, CN}})$$

---

## 8. Paramètres Industriels, Douanes, Environnement & Finance (`Tour 5` vs `Tour 4`)

| Paramètre Officiel (`#/marketConditions`) | USA (`T5`) | Chine (`T5`) | Europe (`T5`) |
| :--- | :---: | :---: | :---: |
| **Taux d'imposition sur les sociétés (`IS %`)** | **`20,0 %`** *(min)* | `24,0 %` | `21,0 %` |
| **Taux de change (`USD`, USD gagne `+5%` RMB / `+2%` EUR vs T4)** | `1 USD` | **`0,1419 USD`** *(T4: `0,1493`)* | **`1,2703 USD`** *(T4: `1,2962`)* |
| **Taux d'intérêt du cash (`T5`)** | **`3,2 %`** | **`4,2 %`** | **`1,0 %`** *(T4: `0,7 %`)* |
| **Taux découvert CT (`T5`) / Dette LT US (`4,0 %`)** | `5,0 %` | `5,5 %` | `4,5 %` |
| **Coûts fixes d'administration (`k USD` au T5)** | `35 000 k$` | **`65 000 k$`** *(T4: `68k`)* | `20 000 k$` |
| **Coût administratif de base / usine (`k USD` au T5)** | `4 000 k$` | **`10 000 k$`** *(T4: `11k`)* | — |
| **Frais recrutement RH (`k USD`) / Licenciement (`k USD`)** | **`8,4 k$`** *(T4: `8,2`)* | `74 / 84 / 110 k$` | *(Autres R&D: `0,69 k$/mois`)* |
| **Valeur nominale action / Coût d'opportunité capital (`WACC`)** | `2,00 $` / `9,0 %` | `2,00 $` / `9,0 %` | `2,00 $` / `9,0 %` |
| **Prix achat / cession usine (`T5`)** | `1 211 M$` / `1 089,9 M$` | `1 061 M$` / `954,9 M$` | — |
| **Coût CO2 (`$/t`) / Renouvelable (`$/kWh`) / Eau (`$/m3`)** | `42,3 $` / `0,23 $` / `1,33 $` | `14,5 $` / `0,19 $` / `1,07 $` | — |

- **Droits de douane + transport (`Paramètres Tour 5` — Accord Chine–Europe `7 %` !) :**
  - `USA → Chine` : `350 $` fixe + **`23,0 %`** du coût.
  - `USA → Europe` : `200 $` fixe + **`13,0 %`** du coût.
  - `Chine → USA` : `300 $` fixe + **`6,0 %`** du coût.
  - **`Chine → Europe` :** `250 $` fixe + **`7,0 %`** du coût *(baissé de `10,0 %` ➔ `7,0 %` au T5 — route export ultra-compétitive !)*.

---

## 9. Comment les « Conditions de Marché » (`#/marketConditions`) Pilotent le Moteur à Chaque Tour

| Signal dans les « Conditions de marché » | Impact mathématique sur le moteur | Action obligatoire pour l'Agent IA |
| :--- | :--- | :--- |
| **Croissances (`US +4 %`, `CN +10 %`, `EU -2 %`)** | Modifie $D_{\text{tot}}(z, t)$. | Saisir ces % dans `Demande` ; ne pas surproduire pour l'Europe en baisse. |
| **Pénurie batteries / Pression Hydrogène** | Renchérit le coût interne & sous-traitance Électrique/Hybride et déplace la demande future vers l'Hydrogène. | Surveiller `#/rd` pour l'Hydrogène et vérifier les marges réelles avant de lancer Électrique/Hydrogène. |
| **Baisse / hausse d'IS & hausse droits douane %** | Modifie l'intérêt fiscal de `Prix de transfert` et renchérit les exports. | Réoptimiser `Impôts -> Prix de transfert` et les priorités `Chine → Europe` vs `USA → Europe`. |
| **Doublement frais recrutement / pénurie ing.** | Monte le coût marginal RH (`8,4 k$` au T5 après `8,2 k$` au T4) et la rotation naturelle. | Stabiliser les effectifs, ne jamais licencier, cibler les `Priorités de formation`. |
| **Flambée CER / Activistes / Fournisseurs** | Augmente $\Phi_{\text{ESG}}$ et potentiellement le prix kWh renouvelable. | Vérifier le coût renouvelable dans `Paramètres` et éliminer tout fournisseur `< 2★`. |

---

## 10. Nouveaux Algorithmes Vérifiés aux Tours 3 & 4 (`Prix de Transfert` & `Multiplicateurs ESG`)

### A. Équation des Prix de Transfert (`Impôts`, $k \in [1.00, 2.00]$) & Arbitrage Douanier ($\delta$)
Soit $Q_{\text{orig} \to \text{dest}}$ le volume exporté au coût unitaire comptable $c$, avec multiplicateur $k \in [1.00, 2.00]$ et droit de douane ad valorem $\delta_{\text{orig}\to\text{dest}}$ :
1. **Flux comptable d'EBIT :**
   $$\Delta \text{EBIT}_{\text{orig}} = +\, Q_{\text{orig}\to\text{dest}} \cdot (k - 1) \cdot c \qquad \text{et} \qquad \Delta \text{EBIT}_{\text{dest}} = -\, Q_{\text{orig}\to\text{dest}} \cdot (k - 1) \cdot c$$
2. **Effet net sur le Cash Flow Global (incluant l'impôt et la hausse potentielle des droits de douane $\delta$) :**
   $$\Delta \text{NetCashFlow} = Q_{\text{orig}\to\text{dest}} \cdot (k - 1) \cdot c \cdot \Big[ (\tau_{\text{dest}}^{\text{eff}} - \tau_{\text{orig}}^{\text{eff}}) - \delta_{\text{orig}\to\text{dest}} (1 - \tau_{\text{dest}}^{\text{eff}}) \Big]$$
   - **Exemple du cours d'Eric Astien ([`09_slides_cours/`](../09_slides_cours)) :** Avec `IS US = 20 %` et `IS Europe = 40 %`, passer `USA → Europe` de `PCI = 1,0` à **`PCI = 1,2`** remonte le CA interne US (`100 000 ➔ 120 000`), efface la perte US (`-20 000 ➔ 0`, `0` impôt) et réduit l'impôt Europe de `12 000 ➔ 4 000` (**`+8 000`** net).
   - **Vérifié au Tour 4 (`IronHorse`, $\tau_{\text{USA}} = 20\% < \tau_{\text{Europe}} = 21\%$) :** Avec `PCI = 1.20` sur `USA → Europe`, la **Marge Opérationnelle US** est remontée de **`-0,98 %` ➔ `+8,05 %` (`8/12 pts`)** tout en abaissant le `Coût unitaire Europe` (`15 027 $ ➔ 14 765 $`).
   - À l'inverse, comme $\tau_{\text{Chine}} = 24\% > \tau_{\text{Europe}} = 21\%$, monter $k_{\text{CN}\to\text{EU}} > 1$ **détruit** du cash (`+3 %` d'impôt en plus sans compter les `7 %` de douane) : laisser à **`1.00`**.

### B. Équations Finance Tour 5 : Dividendes, Rentabilité Action (`Rt`) & Augmentation de Capital ([slides 08 & 09](../09_slides_cours/08_tour5_finance_dividendes_et_rentabilite_action.jpeg))
- **Actions en circulation :** $N_0 = 1\,625\,000\,000$ actions de nominal $2\,\$$ ($\text{Capital social USA} = 3\,250\,000\,\text{k\$}$).
- **Dividende par titre & Rendement :** $d = \frac{\text{Dividendes totaux}}{N}$, $\text{Rendement net} = \frac{d}{\text{Cours}_n}$, **Rentabilité action (TSR) :**
  $$R_t = \frac{\text{Cours}_n - \text{Cours}_{n-1} + d}{\text{Cours}_{n-1}}$$
  *(Prélevé sur la **trésorerie maison mère USA** [`14 495 M$` fin T4] ; à `0` dette, un dividende financé sans découvert USA maintient `Indépendance financière = 100 %` et augmente le `ROE` en réduisant les capitaux propres finaux.)*
- **Augmentation de capital ($n$ actions au prix d'émission $\text{PE}$) :** Crédit de la **trésorerie USA (`Bilan « EU » = États-Unis`, maison mère en USD)** $+ n \cdot \text{PE}$ ; Passif USA Capital $+ n \cdot 2\,\$$ + Prime d'émission $+ n \cdot (\text{PE} - 2\,\$)$. *(Déconseillé quand cash abondant car dilue le `ROE`.)*

### C. Multiplicateurs de Demande ESG Mesurés aux Tours 3 & 4 (`Rapport ESG`)
Valeurs exactes relevées entre les 12 équipes dans [`tour_03_resultats_univers1.xls`](../04_rapports_tours/tour_03_resultats_univers1.xls) (et confirmées en T4 [`tour_04_resultats_univers1.xls`](../04_rapports_tours/tour_04_resultats_univers1.xls)) :

| Levier ESG (`Planning`, `Achats`, `RH`) | Meilleur niveau observé au T3 | Pire niveau observé au T3 | Écart total de demande |
| :--- | :---: | :---: | :---: |
| **`Améliorations qualité processus` (CO2 + Énergie + Eau)** | **`+20,9 %`** (3 sur 3 : `Ren'Auto`, `GT-Auto`) ; `+11,3 %` (2/3) ; `-0,3 %` (1/3) | **`-8,2 %`** (0 sur 3) | **`29,1 %` d'écart** |
| **`Utilisation d'énergie renouvelable %`** | **`+12,8 %`** (`100 %` US/CN) | **`-7,8 %`** (`30 %` US/CN) | **`20,6 %` d'écart** |
| **`Priorités de formation` (Image)** | **`+11,7 %`** (`1` seule ciblée : `IronHorse` Éthique) | **`-7,6 %`** (`AURA`) \| `+1,6 %` (5/5 dilué : `Ren'Auto`) | **`19,3 %` d'écart** |
| **`Politiques en matière de travail`** | **`+8,7 %`** (`Partenariat stratégique`, `Ça Roule`) \| `+5,0 %` (`Ren'Auto`) \| `+3,3 %` (`IronHorse`) | **`-1,9 %`** (`Conformité standard`) | **`10,6 %` d'écart** |
| **`Recyclabilité du produit`** | **`+4,2 %`** (`Systèmes à circuit fermé + Engagement`, `IronHorse`) \| `+2,5 %` (`ACV`) | **`-5,7 %`** (`POLRAMOS` Engagement rompu !) | **`9,9 %` d'écart** |
| **`Politiques des fournisseurs`** | **`+2,6 %`** (Fournisseurs propres `>= 2,5★`, `DDRS = 6,00`) | **`-6,5 %`** (`AURA`) \| **`-5,5 %`** (`Colossaux 1★`, `IronHorse`) | **`9,1 %` d'écart** |

### D. Impact Unitaire des Améliorations Processus & Certifications ESG
- **Consommation base par voiture (Thermique / Hybride / Élec USA ➔ Chine = `+20 %`) :**
  - `CO2` : `1 800 / 2 250 / 2 725 kg` USA (`2 160 / 2 700 / 3 270` CN) — **`-12 %` permanent** après amélioration (`CO2`).
  - `Énergie` : `950 / 1 150 / 1 700 kWh` USA (`1 140 / 1 380 / 2 040` CN) — **`-9 %` permanent** après amélioration (`Énergie`).
  - `Eau` : `120 / 135 / 160 m3` USA (`144 / 162 / 192` CN) — **`-10 %` permanent** après amélioration (`Eau`).
- **Score DDRS Fournisseurs :** $\text{DDRS} = \text{Qualité} + \text{Développement durable}$ (sur `10,00`, moyenne des fournisseurs cochés).
- **Certifications ESG :** `Bronze >= 2,75` (`8 M$`, `2 pts`), `Argent >= 3,25` (`24 M$`, `4 pts`), `Or >= 4,00` (`40 M$`, `6 pts`).
