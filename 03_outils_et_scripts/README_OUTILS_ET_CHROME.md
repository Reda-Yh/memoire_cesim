# 🛠️ OUTILS, SCRIPTS PYTHON & CONNEXION LIVE CHROME DEVTOOLS
> **Navigation :** [Index Recherche](../INDEX_RECHERCHE_AGENT_IA.md) · [Index Maître](../00_INDEX_AGENT_IA.md) · [README](../README.md) · [Outils & Scripts](./README_OUTILS_ET_CHROME.md)

Ce fichier documente les emplacements des fichiers officiels (`04_` à `10_`), les 3 scripts Python autonomes (**calculateur 21 critères**, **radar concurrence/ESG `t+2`**, **lecteur HTML universel**) et les routes Cesim en lecture seule.

---

## 📂 1. Emplacement des Archives & Sources Officielles (`04_` à `10_`)

- **[`04_rapports_tours/`](../04_rapports_tours) :** [`tour_01`](../04_rapports_tours/tour_01_resultats_univers1.xls) à [`tour_04_resultats_univers1.xls`](../04_rapports_tours/tour_04_resultats_univers1.xls) *(déposer ici `tour_05+` au format `.xls` ou `.html`)*.
- **[`05_decisions_prises/`](../05_decisions_prises) :** [`tour_01_decisions_ironhorse_yahya.html`](../05_decisions_prises/tour_01_decisions_ironhorse_yahya.html) à [`tour_04_decisions_ironhorse_yahya.html`](../05_decisions_prises/tour_04_decisions_ironhorse_yahya.html).
- **[`06_conditions_marche_et_evenements/`](../06_conditions_marche_et_evenements) :** [`tour_01..05_conditions_marche.html`](../06_conditions_marche_et_evenements/tour_05_conditions_marche.html) et [`tour_04..05_evenements.html`](../06_conditions_marche_et_evenements/tour_05_evenements.html).
- **[`07_classements_officiels/`](../07_classements_officiels) :** [`classement_officiel_tours_0_a_3_ESYBIA2AS.pdf`](../07_classements_officiels/classement_officiel_tours_0_a_3_ESYBIA2AS.pdf).
- **[`08_manuels_et_planning/`](../08_manuels_et_planning) :** `01_planning_et_livrables_ESYBIA2AS.pdf`, `02_manuel_utilisateur_cesim.pdf`, `03_description_cas_automobile_wESG.pdf`, [`04_regles_ventes_licences_entre_equipes.pdf`](../08_manuels_et_planning/04_regles_ventes_licences_entre_equipes.pdf).
- **[`09_slides_cours/`](../09_slides_cours) :** Slides `01` à `09` (`Strategic Intent`, `4P/4C`, `PCI Impôts`, `Dividendes` & `Augmentation de capital` Tour 5).
- **[`10_messages_prof/`](../10_messages_prof) :** [`01_messages_instructeur_ESYBIA2AS_tours_1_a_5.md`](../10_messages_prof/01_messages_instructeur_ESYBIA2AS_tours_1_a_5.md).
- **Mémoire JSON structurée :** [`../02_historique_et_strategie/live_game_history.json`](../02_historique_et_strategie/live_game_history.json).

---

## 🧮 2. Calculateur Automatique Eric Astien (`calculateur_classement_astien.py`)

Le script [`calculateur_classement_astien.py`](./calculateur_classement_astien.py) lit nativement les classeurs **`.xls` (BIFF8) ET `.html`** sans dépendance externe, détecte automatiquement le rapport au numéro de tour le plus élevé dans `04_rapports_tours/` et calcule les **15, 17 ou 21 critères** + le diagnostic ligne par ligne d'`IronHorse` :

```powershell
python "c:\Users\len\OneDrive\Bureau\ceism\memoire_agent_cesim\03_outils_et_scripts\calculateur_classement_astien.py"
# Ou sur un tour précis :
python "c:\Users\len\OneDrive\Bureau\ceism\memoire_agent_cesim\03_outils_et_scripts\calculateur_classement_astien.py" "04_rapports_tours/tour_04_resultats_univers1.xls"
```

---

## 🔮 3. Radar Concurrence, Usines `t+1`/`t+2` & ESG (`analyseur_concurrence_et_decisions.py`)

Le script [`analyseur_concurrence_et_decisions.py`](./analyseur_concurrence_et_decisions.py) extrait nativement depuis **`.xls` ou `.html`** pour les **12 équipes** : usines `t+1` & `t+2`, stocks `T/H/E+Hy`, équipements proposés, trésorerie/découvert, `Score DDRS Fournisseurs`, `E / S / G`, `Dette LT` et `Certification ESG` :

```powershell
python "c:\Users\len\OneDrive\Bureau\ceism\memoire_agent_cesim\03_outils_et_scripts\analyseur_concurrence_et_decisions.py"
```

---

## 📄 4. Lecteur Universel Cesim `.xls` & `.html` (`lecteur_html_cesim.py`)

Les fichiers Cesim (`04_rapports_tours/*.xls`, `05_decisions_prises/*.html`, `06_conditions_marche_et_evenements/*.html`) sont lourds ou binaires. Le script [`lecteur_html_cesim.py`](./lecteur_html_cesim.py) les convertit en texte propre prêt pour toute IA :

```powershell
# Lire les événements ou conditions du Tour 5 avec filtre par mot-clé :
python "c:\Users\len\OneDrive\Bureau\ceism\memoire_agent_cesim\03_outils_et_scripts\lecteur_html_cesim.py" "06_conditions_marche_et_evenements/tour_05_evenements.html" --filter batteries
python "c:\Users\len\OneDrive\Bureau\ceism\memoire_agent_cesim\03_outils_et_scripts\lecteur_html_cesim.py" "04_rapports_tours/tour_04_resultats_univers1.xls" --filter "Score final"
# Lire nos décisions validées du Tour 4 :
python "c:\Users\len\OneDrive\Bureau\ceism\memoire_agent_cesim\03_outils_et_scripts\lecteur_html_cesim.py" "05_decisions_prises/tour_04_decisions_ironhorse_yahya.html"
```

---

## 🌐 5. Connexion Live Chrome (Strictement en LECTURE SEULE)

> [!WARNING]
> **RÈGLE DE SÉCURITÉ STRICTE :** Toujours lire l'interface Cesim en **LECTURE SEULE**. **Ne JAMAIS cliquer sur enregistrer/soumettre ni modifier les décisions de l'équipe à la place de l'utilisateur**, sauf instruction explicite.

### Routes Hash & Modules de `https://bordeaux-inp.cesim.com/` (État Tour 5)
- **Accueil & Forum :** Page d'accueil (`Planning`, `Forums`, dépôt **Flyer PDF vertical avant `17h00`**)
- **`#/marketConditions` :** Conditions de marché + **`Événements`** (`Le procès de la transparence`, `Négociations sur les batteries`)
- **`#/demand` :** Onglet `Demande`
- **`#/production/planning` | `inventory` | `investments` | `procurement` | `environmentalImpact`**
- **`#/hr` :** `RH` (`Effectifs`, `Priorités de formation`, `Politiques de travail`)
- **`#/rd` :** `R&D` (`Électrique`, ouverture **`Hydrogène`**, licences et ventes entre équipes)
- **`#/marketing` :** `Marketing` (`USA`, `Chine`, `Europe`, **`Certifications ESG`**)
- **`#/logistics` :** `Logistique` (`Chine → Europe` désormais à **`7 %`** de douane au T5 !)
- **`#/tax` :** `Impôts` (Prix de transfert `1.00–2.00` et tableau d'imposition)
- **`#/finance` :** `Finance` (Dette LT `0 M$`, transferts internes, **`Dividendes`**, **`Augmentation de capital`**)
- **`#/budgets` :** `Prévisionnel financier` (`Global / USA / Chine / Europe`)
- **`#/decisionChecklist` :** `Liste des décisions` (`IronHorse`, `Mohamed Ajaji`, `Nour Doghmi`, `Reda Yahya`, `yahya bel hajjam`)
