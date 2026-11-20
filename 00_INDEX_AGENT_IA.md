# 🧠 MÉMOIRE MAÎTRE & GUIDE D'ONBOARDING POUR AGENT IA (ENTRÉE TOUR 5 ➔ TOUR 10)
> **Navigation :** [Index Recherche](./INDEX_RECHERCHE_AGENT_IA.md) · [README](./README.md) · [Prompt IA](./prompt.md) · [Barème 21 Critères](./01_regles_et_algorithmes/01_bareme_eric_astien_21_criteres.md) · [Playbook T5–T10](./02_historique_et_strategie/02_playbook_tours_5_a_10.md) · [Outils & Scripts](./03_outils_et_scripts/README_OUTILS_ET_CHROME.md)

**Compétition :** Cesim Global Challenge (Industrie Automobile w/ ESG) — Bordeaux INP (`https://bordeaux-inp.cesim.com/`)  
**Cours / Session :** **`ESYBIA2AS`** — **Univers 1** (12 équipes)  
**Professeur / Évaluateur :** **Eric Astien** — Grille officielle à **21 critères** (notation relative `1 + NB.SI` de 1 à 12 pts + Certification ESG `0/2/4/6 pts`)  
**Notre Équipe :** **`IronHorse`** (anciennement **`Bleu`** au Tour d'essai et au Tour 1)  
**Membres de l'équipe :**
- **Reda Yahya** (Architecte IA & Stratège — l'utilisateur principal)
- **Yahya Bel Hajjam**
- **Nour Doghmi**
- **Mohamed Ajaji**

**Statut Actuel (Jeudi 19/11 — Tour 5 `15h50` en cours) :**
- **Tour 3 officiel PDF ([`classement_officiel_tours_0_a_3_ESYBIA2AS.pdf`](./07_classements_officiels/classement_officiel_tours_0_a_3_ESYBIA2AS.pdf)) :** **`IronHorse` 🥇 1er Général avec `374 points`**.
- **Tour 4 analysé ([`tour_04_resultats_univers1.xls`](./04_rapports_tours/tour_04_resultats_univers1.xls)) :** `IronHorse` réalise **`11 644 M$`** de résultat net (`0` dette LT = `100 %` Indép. Fin. `AAA`, `0` découvert, `Argent = 4 pts`, Marge US `+8,05 %`) et **`128 pts`** (`7e` sur 21 critères, calcul Excel exact) ➔ **cumul estimé T1–T4 `~502 pts` (🥇 toujours #1 devant `GT-Auto VI ~498 pts` et `Ren'Auto ~495 pts`)**.

> [!CAUTION]
> **ALERTES OFFICIELLES `ESYBIA2AS` TOUR 5 ([`01_messages_instructeur_ESYBIA2AS_tours_1_a_5.md`](./10_messages_prof/01_messages_instructeur_ESYBIA2AS_tours_1_a_5.md)) :**
> 1. **Ouverture officielle de l'Hydrogène vert au Tour 5 (`2033`) :** *« Les gouvernements estiment qu'il n'y a plus de risque à développer les moteurs à hydrogène et ouvrent la possibilité de commercialisation aux entreprises. »* Attention toutefois au signal [`tour_05_conditions_marche.html`](./06_conditions_marche_et_evenements/tour_05_conditions_marche.html) : défaut temporaire sur les nouveaux conteneurs Hydrogène (revenir à l'ancien conteneur plus coûteux au T5, mais expansion des infrastructures particulièrement en Europe).
> 2. **COP 32 — Interdiction définitive des moteurs 100 % THERMIQUES dès 2035 = Tour 7 :** *« L'utilisation des énergies fossiles sera définitivement interdite à partir de 2035 pour les motorisations utilisant uniquement ce mode d'énergie. »*
>    - **Conséquence vitale :** Le **Tour 6 (`17h15`, 2034)** est la **DERNIÈRE ANNÉE du Thermique pur** ➔ **terminer impérativement le Tour 6 avec `0 k` de stock Thermique** et tenir **Électrique + Hydrogène + Hybride (toujours autorisé)** prêts pour le Tour 7 !
> 3. **Livrable Jour 2 avant `17h00` :** Déposer le **FLYER PDF vertical** d'`IronHorse` sur la page d'accueil Cesim.

---

## 📌 1. Règle d'Or Obligatoire Avant Toute Recommandation (SOP)

> [!IMPORTANT]
> **TU NE DOIS JAMAIS PROPOSER DES CHIFFRES « À L'AVEUGLE » NI RECOPIER LE TOUR PRÉCÉDENT !**  
> Chaque tour débloque de nouveaux paramètres (`Impôts/PCI` au T4, **`Hydrogène / COP 32 / Dividendes / Augmentation de capital / Accord Chine–Europe 7 % / 2 Événements`** au T5 !). Avant de recommander la moindre décision pour un Tour $N$, **exécute ces 3 lectures dans l'ordre :**

1. **ANALYSER LE DERNIER RAPPORT `.xls`/`.html`, LES DÉCISIONS T-1 & `live_game_history.json` :**
   - Lancer les 3 scripts dans [`03_outils_et_scripts/`](./03_outils_et_scripts/README_OUTILS_ET_CHROME.md) :
     - `python memoire_agent_cesim/03_outils_et_scripts/calculateur_classement_astien.py` *(auto-détecte [`tour_04_resultats_univers1.xls`](./04_rapports_tours/tour_04_resultats_univers1.xls) puis T5+)*
     - `python memoire_agent_cesim/03_outils_et_scripts/analyseur_concurrence_et_decisions.py`
     - `python memoire_agent_cesim/03_outils_et_scripts/lecteur_html_cesim.py ...` *(pour lire proprement `04_rapports_tours/*.xls`, `05_decisions_prises/` et `06_conditions_marche_et_evenements/`)*
   - Vérifier aussi [`07_classements_officiels/`](./07_classements_officiels) et [`02_historique_et_strategie/live_game_history.json`](./02_historique_et_strategie/live_game_history.json).

2. **LIRE INTÉGRALEMENT L'INTERFACE & LES EXPORTS DU TOUR $N$ (CHROME READ-ONLY) :**
   Vérifier **ces 10 variables qui changent à chaque tour** (déjà extraites pour T5 dans [`tour_05_conditions_marche.html`](./06_conditions_marche_et_evenements/tour_05_conditions_marche.html) & [`tour_05_evenements.html`](./06_conditions_marche_et_evenements/tour_05_evenements.html)) :
   1. **Croissance de la demande par zone (`#/marketConditions`) :** Au T5, l'Europe poursuit son recul (`-2 %`) mais reste le plus gros marché ; surveiller Chine & USA.
   2. **Technologies & Annonces Forum (`Accueil / Forum`, `#/rd`) :** Électrique proche de 100 % après nos `1 450 000` j-h au T4, ouverture R&D **Hydrogène**, et compte à rebours **COP 32** (fin Thermique pur au T7).
   3. **Sous-traitance (`#/production/planning`) :** Coûts hybrides/électriques en baisse potentielle (nouveaux gisements de batteries annoncés au T5) et plafonds partagés par zone.
   4. **Taux de change & Fiscalité (`#/tax` + Paramètres) :** Au T5 : `1 RMB = 0,1419 USD`, `1 EUR = 1,2703 USD`, IS inchangés (`US 20 % < EU 21 % < CN 24 %`).
   5. **Droits de douane & Logistique :** **Changement majeur Tour 5 :** nouvel accord libre-échange abaissant **`Chine → Europe` de `10 %` à `7 %`** (contre `13 %` `USA → Europe` et `23 %` `USA → Chine`).
   6. **Sous-onglet `Événements` (`#/marketConditions/events` / [`tour_05_evenements.html`](./06_conditions_marche_et_evenements/tour_05_evenements.html)) :** Lire sur Chrome les infobulles exactes des 3 options de **`Le procès de la transparence`** et **`Négociations sur les batteries`**.
   7. **Fournisseurs ESG (`#/production/procurement`) :** Toujours vérifier les étoiles live et les études (`↑ / - / ↓`) — au T4, `IronHorse` était **la seule des 12 équipes** à avoir conservé `Composants Colossaux` (`1,75` image), perdant `6` pts DDRS (`5,67 = 1/7 pts`) et `-6,1 %` demande !
   8. **Piliers ESG Production (`#/production/planning`) :** Au T4, `CO2` et `Eau` n'ont finalement pas été cochés (`Non/Non` dans `tour_04_decisions_ironhorse_yahya.html`) et `Recyclabilité` était descendue à `Évaluation du cycle de vie` (`-1,5 %`) ➔ **remonter à `Systèmes à circuit fermé`** et arbitrer `CO2 / Eau` dès le T5 !
   9. **RH & R&D (`#/hr`, `#/rd`) :** Nous avons **`6 400` ingénieurs** au T5 (`1 600 000` j-h brut, frais recrutement `8,4 k$` au T5) ; cibler **1 à 2 `Priorités de formation`** max et vérifier si `Initiatives communautaires` (`-150 000` j-h) doit être gardé ou remplacé par `Partenariat stratégique`.
   10. **Marketing Certifications & Finance (`#/marketing`, `#/finance`, `#/decisionChecklist`) :** Surveiller **`Or (>=4,00, 6 pts)`**, vérifier les **Dividendes / Augmentation de capital** fraîchement ouverts au Tour 5 ([slides 08 & 09](./09_slides_cours/08_tour5_finance_dividendes_et_rentabilite_action.jpeg)), et garantir **`0` découvert** par filiale (`Chine 4,2 %`, `USA 3,2 %`, **`Europe remontée à 1,0 %`** au T5) avant validation dans **`Liste des décisions`**.

---

## 🗺️ 2. Classement & Radar des 12 Équipes (Fin Tour 3 Officiel + Estimé Excel `.xls` Tour 4)

| Équipe | T1–T3 Officiel (PDF) | T4 `.xls` (`21 crit.`) | Cumul Est. (`T1–T4`) | Résultat Net T4 | Usines T5 (`t+1`) ➔ T6 (`t+2`) | Diagnostic Entrant au Tour 5 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **`IronHorse` (NOUS)** | **374 (🥇 1er)** | **128 (7e)** | **🥇 ~502 (#1?)** | **`11 644 M$`** | **`9 US / 6 CN` (`3 300 k`)** | **`0` dette LT (`100 %`), `0` découvert (`33 Mds$` cash), `Argent` (`4 pts`), +6 pts DDRS & +8–15 % ESG faciles au T5 !** |
| **`GT-Auto VI`** | 355 (6e) | 143 (2e ex) | ~498 (#2?) | `13 416 M$` | `7 US / 6 CN` (`2 900 k`) | Très rentable (`36,9 Mds$` cash, `0` dette, `6,75` DDRS), mais a cédé 2 usines US. |
| **`Ren'Auto`** | 368 (3e) | 127 (8e) | ~495 (#3?) | `14 286 M$` | **`14 US / 17 CN` ➔ `18 US / 21 CN` (`8 850 k`!)** | A lancé l'Élec (5 éq.) mais s'est noyé : **`13 249 M$` découvert Chine**, **`635 k` stocks (`175 k` Élec)**, `12,8 Mds$` dette LT. |
| **`YANAUTO`** | 356 (5e) | 129 (4e ex) | ~485 | `12 503 M$` | `8 US / 5 CN` (`2 850 k`) | Solide (`40,2 Mds$` cash, `0` stock, `40,04 %` marge EU), mais `449 k` ruptures. |
| **`Vrooom Vroooom`** | 325 (8e) | **153 (🥇 1er T4)** | ~478 | `11 748 M$` | `8 US / 3 CN` ➔ `8 US / 5 CN` (`2 850 k`) | Grand gagnant T4 (`0` stock, `0` dette, `7,25` DDRS), mais petite capacité. |
| **`POLRAMOS`** | 366 (4e) | 108 (9e) | ~474 | `10 173 M$` | `6 US / 9 CN` (`3 450 k`) | `642 k` stocks (`361T / 281H`), `0` dette LT. |
| **`TABCHOUR AUTO`** | 324 (9e) | 143 (2e ex) | ~467 | `14 164 M$` | `8 US / 3 CN` (`2 350 k`) | `47,0 Mds$` cash, `0` dette, `37 k` stocks seulement, forte remontée T4. |
| **`BM2P`** | 371 (2e) | **92 (12e T4)** | ~463 | `9 035 M$` | `7 US / 8 CN` ➔ `7 US / 9 CN` (`3 650 k`) | **Grosse chute T4 (`12e`) :** `678 k` stocks + **`787 M$` découvert Europe** + `Pas de certification`. |
| **`Ça Roule`** | 331 (7e) | 106 (10e) | ~437 | `3 066 M$` | `9 US / 6 CN` (`3 300 k`) | En difficulté : `609 k` stocks, `4 755 M$` découvert, `8 900 M$` dette LT. |
| **`AURA`** | 300 (10e) | 129 (4e ex) | ~429 | `9 979 M$` | `8 US / 3 CN` (`2 350 k`) | A purgé tous ses stocks (`0 k`) et son découvert (`0`), mais `660 k` ruptures. |
| **`tomobil`** | 216 (12e) | 129 (4e ex) | ~345 | `11 283 M$` | `9 US / 5 CN` (`3 050 k`) | Remonte T4 (`0` découvert, `#1 ROE 51,96 %`), encore `8 400 M$` dette LT. |
| **`MO'THOR`** | 219 (11e) | 97 (11e) | ~316 | `3 589 M$` | `6 US / 6 CN` ➔ `6 US / 7 CN` (`2 950 k`) | Coûts faibles en Élec (`0` stock Élec T4, `0` découvert), mais faible marge nette. |

*(Scores Tour 4 estimés par [`calculateur_classement_astien.py`](./03_outils_et_scripts/calculateur_classement_astien.py) directement sur les chiffres non arrondis du classeur [`tour_04_resultats_univers1.xls`](./04_rapports_tours/tour_04_resultats_univers1.xls) en attendant le PDF officiel du professeur.)*

---

## 🗂️ 3. Carte Complète des 10 Dossiers (`01_` à `10_`)

Pour toute recherche par **Tour**, **Mot-clé** ou **Nom de fichier**, consulter **[`INDEX_RECHERCHE_AGENT_IA.md`](./INDEX_RECHERCHE_AGENT_IA.md)** :
- **`01_regles_et_algorithmes/`** : Barème 21 critères, règles complètes de chaque onglet (dont Impôts/PCI, Événements, Dividendes/Aug. Capital), formules mathématiques & paramètres Tour 5.
- **`02_historique_et_strategie/`** : Historique T0–T4, autopsie T4, **Playbook Tour 5 ➔ Tour 10**, [**Cartographie Concurrence & Plan de Bataille Tour 7**](./02_historique_et_strategie/03_cartographie_concurrence_et_plan_bataille_tour_7.md), [`live_game_history.json`](./02_historique_et_strategie/live_game_history.json).
- **`03_outils_et_scripts/`** : `calculateur_classement_astien.py`, `analyseur_concurrence_et_decisions.py`, `lecteur_html_cesim.py`, routes hash Chrome.
- **`04_rapports_tours/`** : `tour_01_resultats_univers1.xls` à `tour_04_resultats_univers1.xls`.
- **`05_decisions_prises/`** : Snapshots HTML des décisions `IronHorse` (`tour_01` à `tour_04`).
- **`06_conditions_marche_et_evenements/`** : Conditions de marché (`tour_01` à `tour_05`) et Événements (`tour_04` à `tour_05`).
- **`07_classements_officiels/`** : PDF officiel Eric Astien (`Tours 0–3`).
- **`08_manuels_et_planning/`** : Planning & livrables (`ESYBIA2AS`), manuel Cesim, cas Auto w/ ESG, règles licences.
- **`09_slides_cours/`** : Slides `01` à `09` (dont Dividendes & Augmentation de capital Tour 5).
- **[`10_messages_prof/`](./10_messages_prof/01_messages_instructeur_ESYBIA2AS_tours_1_a_5.md)** : Messages officiels instructeur `ESYBIA2AS` (`Tours 1–5`, dont diagnostic T3, annonce T4 `INFO OU INTOX`, Hydrogène T5 et `COP 32`).

---

## ⏰ 4. Calendrier Officiel & Livrables Notés (`ESYBIA2AS` — [`01_planning_et_livrables_ESYBIA2AS.pdf`](./08_manuels_et_planning/01_planning_et_livrables_ESYBIA2AS.pdf))

### Jour 1 (18 nov.) — Démarrage *(Terminé)*
- **Tour d'entraînement :** `2e / 12` (`122 pts`, hors cumul) · **Tour 1 :** `8e` (`96 pts`) · **Tour 2 :** **🥇 `1er` (`156 pts` ➔ `#1` Général `252 pts`)**.

### Jour 2 (19 nov.) — Croissance *(En cours — Bureau prof : S203)*
- **10:20 — Tour 3 (`Période 3`) :** `7e` (`122 pts` / 21 critères) ➔ **🥇 `#1` Général officiel (`374 pts`)**.
- **13:30 — Tour 4 (`Période 4`) :** Clôturé (`128 pts` `.xls`, `11 644 M$` net, `0` dette LT, `~502 pts` cumul estimé 🥇 #1).
- **15:50 — Tour 5 (`Période 5`) :** **EN COURS** (`16:00` Résultats & classement T5 ; **Hydrogène + COP 32 officiels**, accord `Chine→Europe 7 %`, `Dividendes / Augmentation de capital`, `2` Événements).
- **17:00 — FLYER PDF À RENDRE :** Upload page d'accueil (1 par équipe au format PDF) — **Présentation VERTICALE obligatoire** (`IronHorse`, produits, **slogan**).
- **17:15 — Tour 6 (`Période 6`) :** Décisions T6 + communication des flyers (**DERNIER TOUR DU THERMIQUE PUR ➔ liquider à `0 k` stock Thermique !**).

### Jour 3 (20 nov.) — Maturité & Podium Final
- **08:30 :** Rencontre — Résultats, classement et analyse du Tour 6.
- **09:00 :** Début du **QUIZ individuel** (fin annoncée entre `10:00` et `13:00` selon créneau sur plateforme).
- **10:00 — Tour 7 (`Période 7`) :** Fin du QUIZ / **Interdiction du Thermique pur (`COP 32`)** — Hybride + Électrique + Hydrogène !
- **11:15 — Tour 8 (`Période 8`) :** Décisions T8, résultats et classement.
- **13:00 — Tour 9 (`Période 9`) :** Décisions T9 (**résultats SANS classement affiché** pour garder le suspense final !).
- **13:30 — Classement des FLYERS** (upload plateforme).
- **14:00 — Tour 10 (`Période 10`) & VIDÉO (Facultative) :** Fin des décisions T10 + envoi éventuel d'une vidéo max 1 min de présentation par mail/lien.
- **14:30 :** **RENCONTRE FINALE** — Résultat, classement général, podium des challenges & débriefing.
- **16:00 :** Début de l'**évaluation des pairs**.
- **23:59 — DOSSIER QUESTIONNAIRE À RENDRE :** Modèle disponible dans le menu `document` (1 dossier par équipe à uploader sur la plateforme avant minuit).


## Mise à jour après clôture T5 (19/11/2026)
- Résultat officiel T5 : IronHorse 145 pts sur 22 critères, 2e du tour ; cumul 647 pts, rang général 1.
- Classement général officiel T5 : IronHorse 647, Ren’Auto 638, GT-Auto VI 635, YANAUTO 624, Vrooom 628, TABCHOUR 601, Ça Roule 570, BM2P 557, AURA 553, POLRAMOS 540, tomobil 490, MO’THOR 450.
- Le calculateur a été corrigé pour le 22e critère TSR. Tests de régression : voir `03_outils_et_scripts/tests/`.
- Le Tour 6 est le prochain tour ; son résultat officiel n’est pas présent dans le dossier. Les décisions T6 sont un snapshot, pas un résultat.
