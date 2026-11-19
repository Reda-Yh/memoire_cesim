# 🧠 Mémoire & Playbook Cesim Global Challenge (`ESYBIA2AS` — Équipe `IronHorse`)

Dépôt complet, structuré à plat (`01_` à `10_`) et 100 % autonome pour tout agent IA (Antigravity, Gemini, Claude, ChatGPT) ou stratège humain pilotant l'équipe **`IronHorse`** (ex-`Bleu`) sur **`https://bordeaux-inp.cesim.com/`** (`Session ESYBIA2AS`, Univers 1, Professeur **Eric Astien**).

- **Statut actuel (19/11, Tour 5 `15h50` en cours) :**
  - **Tour 4 analysé (`tour_04_resultats_univers1.xls`) :** `IronHorse` réalise **`11 644 M$`** de résultat net, **`0` dette LT (`100 %` Indép. Fin., `AAA`)**, **`0` découvert (`32 989 M$` cash)** et **`128 pts`** (`7e` sur 21 critères). Au **cumul estimé T1–T4 (précision Excel `.xls`)**, **`IronHorse` reste 🥇 #1 Général (`~502 pts`)**, devant `GT-Auto VI` (`~498 pts`), `Ren'Auto` (`~495 pts`, tombé en découvert `13,2 Mds$` et `635 k` stocks) et `BM2P` (`~463 pts`, `12e` au T4 avec `678 k` stocks et `787 M$` découvert).
  - **Nouveautés officielles du Tour 5 :** **Hydrogène vert ouvert** + **COP 32 officielle** (interdiction définitive du **Thermique pur dès 2035 = Tour 7**, donc **Tour 6 = dernier tour pour vendre du Thermique pur et finir à `0 k` stock**), **accord libre-échange `Chine → Europe` abaissant les douanes à `7 %`**, **2 Événements ESG** (`Le procès de la transparence`, `Négociations sur les batteries`), **Dividendes / Augmentation de capital** débloqués, et **Flyer PDF vertical avant `17h00`**.

---

## ⭐ Accès Direct par Index Universel

> **Premier réflexe pour tout agent IA :** ouvrir **[`INDEX_RECHERCHE_AGENT_IA.md`](./INDEX_RECHERCHE_AGENT_IA.md)** pour retrouver n'importe quel document par **Tour (`T1–T5`)**, par **Mot-clé / Question**, ou dans l'**Inventaire complet des 10 dossiers**.

---

## 🗂️ Arborescence Complète à Plat (`01_` à `10_`)

```text
memoire_agent_cesim/
├── .gitignore
├── README.md                                  # Porte d'entrée, statut live & commandes rapides
├── INDEX_RECHERCHE_AGENT_IA.md                # ⭐ Index universel (Matrice T1–T5 + Recherche par thème + Inventaire complet)
├── 00_INDEX_AGENT_IA.md                       # Briefing maître (SOP 10 étapes, classement T4, alertes COP 32/H2, calendrier)
├── prompt.md                                  # Prompt maître prêt à copier-coller à tout agent IA
│
├── 01_regles_et_algorithmes/                  # Barème 21 critères, lois Cesim, PCI, Dividendes, ESG, équations
├── 02_historique_et_strategie/                # Historique T0–T4, Playbook T5–T10, live_game_history.json
├── 03_outils_et_scripts/                      # README outils + calculateur + analyseur + lecteur_html_cesim.py
├── 04_rapports_tours/                         # Rapports Excel Cesim (.xls) tour_01..04 + futurs T5..T10
├── 05_decisions_prises/                       # Snapshots HTML Liste des décisions validées IronHorse (tour_01..04)
├── 06_conditions_marche_et_evenements/        # Conditions de marché (T1–T5) & Événements (T4–T5) en HTML propre
├── 07_classements_officiels/                  # Classements PDF officiels notés par Eric Astien
├── 08_manuels_et_planning/                    # Planning & livrables, manuel Cesim, cas Auto w/ ESG, règles licences
├── 09_slides_cours/                           # 9 slides d'amphi (Strategic Intent, 4P/4C, PCI, Dividendes & Aug. Capital T5)
└── 10_messages_prof/                          # Messages officiels instructeur ESYBIA2AS (Tours 1–5)
```

---

## 🚀 Démarrage Rapide (Ordre de Lecture Recommandé)

1. Copier-coller **[`prompt.md`](./prompt.md)** à votre agent IA (ou utiliser **[`INDEX_RECHERCHE_AGENT_IA.md`](./INDEX_RECHERCHE_AGENT_IA.md)** comme carte).
2. Lire **[`00_INDEX_AGENT_IA.md`](./00_INDEX_AGENT_IA.md)** (SOP en 10 points, classement post-Tour 4, alertes COP 32 & Hydrogène, calendrier).
3. Lire les règles dans [`01_regles_et_algorithmes/`](./01_regles_et_algorithmes/01_bareme_eric_astien_21_criteres.md) (`01` ➔ `02` ➔ `03`).
4. Lire l'historique Tour 4, la stratégie Tour 5 (`15h50`) et le JSON dans [`02_historique_et_strategie/`](./02_historique_et_strategie/01_historique_tours_et_concurrents.md) (`01` ➔ `02` + `live_game_history.json`).

---

## 🛠️ Scripts Python Inclus (`03_outils_et_scripts/`)

```powershell
# 1. Calculateur automatique des 21 critères d'Eric Astien (détecte automatiquement tour_04_resultats_univers1.xls) :
python 03_outils_et_scripts/calculateur_classement_astien.py

# 2. Radar concurrence (usines t+1/t+2, stocks T/H/E/Hy, DDRS, ESG, dette LT, certification) :
python 03_outils_et_scripts/analyseur_concurrence_et_decisions.py

# 3. Lecteur universel Cesim (lit nativement les .xls ET les .html : événements, conditions, décisions) :
python 03_outils_et_scripts/lecteur_html_cesim.py 06_conditions_marche_et_evenements/tour_05_evenements.html --filter batteries
python 03_outils_et_scripts/lecteur_html_cesim.py 04_rapports_tours/tour_04_resultats_univers1.xls --filter "Score final"

# Depuis la racine du workspace (ceism/) :
python memoire_agent_cesim/03_outils_et_scripts/calculateur_classement_astien.py
python memoire_agent_cesim/03_outils_et_scripts/analyseur_concurrence_et_decisions.py
```
