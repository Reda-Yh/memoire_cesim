# 🧠 MÉMOIRE MAÎTRE & GUIDE D'ONBOARDING POUR AGENT IA (GEMINI / ANTIGRAVITY)
**Compétition :** Cesim Global Challenge (Industrie Automobile) — Bordeaux INP (`https://bordeaux-inp.cesim.com/`)  
**Cours / Session :** **`ESYBIA2AS`** — **Univers 1** (12 équipes)  
**Professeur / Évaluateur :** **Eric Astien** (utilise une grille de notation Excel spécifique sur **15 critères = 180 points max par tour**)  
**Notre Équipe :** **`IronHorse`** (anciennement **`Bleu`** au Tour d'essai et au Tour 1)  
**Membres de l'équipe :**
- **Reda Yahya** (Architecte IA & Stratège — l'utilisateur principal)
- **Yahya Bel Hajjam**
- **Nour Doghmi**
- **Mohamed Ajaji**

---

## 📌 1. Pourquoi ce dossier existe (Instruction directe pour tout Agent IA)

> [!IMPORTANT]
> **RÈGLE D'OR N°1 OBLIGATOIRE POUR TOUT AGENT IA À CHAQUE NOUVEAU TOUR :**
> **Tu ne dois JAMAIS proposer des chiffres de décisions « à l'aveugle » ou recopier mécaniquement le tour précédent !**  
> Avant de donner la moindre recommandation pour le Tour $N$, **tu DOIS OBLIGATOIREMENT faire ces 2 lectures dans cet ordre :**
> 1. **LIRE NOTRE HISTORIQUE COMPLET & LES RÉSULTATS DU TOUR $N-1$ :**
>    - Lire [`03_HISTORIQUE_COMPLET_TOURS_0_1_2_ET_CONCURRENTS.md`](file:///c:/Users/len/OneDrive/Bureau/ceism/memoire_agent_cesim/03_HISTORIQUE_COMPLET_TOURS_0_1_2_ET_CONCURRENTS.md), [`data/live_game_history.json`](file:///c:/Users/len/OneDrive/Bureau/ceism/data/live_game_history.json) et le dernier rapport [`manuels/Results for Univers 1, Tour 2.html`](file:///c:/Users/len/OneDrive/Bureau/ceism/manuels/Results%20for%20Univers%201,%20Tour%202.html) (ou `Tour N-1.html`).
>    - Vérifier nos stocks finaux exacts, nos usines disponibles, nos équipements R&D déjà débloqués, notre trésorerie par zone (USA, Chine, Europe), notre dette long terme restante, et les erreurs/stocks des 11 concurrents.
> 2. **LIRE INTÉGRALEMENT LES « CONDITIONS DE MARCHÉ » DU NOUVEAU TOUR $N$ (`#/marketConditions`) QUI CHANGENT À CHAQUE TOUR :**
>    - À chaque nouveau tour, Cesim modifie les paramètres macroéconomiques et ouvre parfois de nouveaux modules ! Tu dois extraire ou demander les **Conditions de marché du Tour $N$** et vérifier ces **7 variables qui changent à chaque tour** :
>      1. **Croissance de la demande par zone (%)** : USA, Chine, Europe (ne jamais garder les % du tour précédent !).
>      2. **Percée des nouvelles technologies** : Part de marché prévue pour Thermique vs Hybride vs **Électrique** vs **Hydrogène** (et effets de réseau / bornes de recharge).
>      3. **Coûts unitaires et plafonds de la Sous-traitance (`Production -> Planning`)** : Au Tour 2, la sous-traitance USA a bondi par surprise à `13 694,3 $` (plus cher que nos usines !) et son plafond a baissé de `350 k` à `225 k`. Vérifie toujours les nouveaux coûts/plafonds en direct !
>      4. **Taux de change (`EUR/USD`, `RMB/USD`) et Taux d'imposition (`USA`, `Chine`, `Europe`)** : Au Tour 2, l'Euro a pris +5 % (`1,2338 $`) et l'impôt Europe a chuté de `27 %` à `21 %`. Vérifie les nouveaux taux du Tour $N$ !
>      5. **Droits de douane / Tarifs douaniers et coûts de transport (`Logistique`)** : Vérifie s'il y a une hausse des taxes d'importation entre USA, Chine et Europe.
>      6. **Fournisseurs ESG & Boycotts ONG (`Production -> Achats`)** : Vérifie si les prix des 5 fournisseurs ont changé ou si les ONG ciblent un nouveau seuil éthique / développement durable.
>      7. **Nouveaux onglets ou sous-onglets débloqués** : Tout comme `R&D`/`Finance` se sont ouverts au Tour 1 et `Achats`/`Transferts internes de trésorerie` au Tour 2, vérifie si un nouveau module s'ouvre au Tour $N$.

Si Reda te demande de l'aider sur le **Tour 3, 4, 5 ou 6** de la simulation Cesim, **lis tous les fichiers de ce dossier `memoire_agent_cesim/` avant toute chose**.  
Tu y trouveras **100 % des règles profondes du moteur Cesim, la formule mathématique exacte de la grille de notation secrète du professeur Eric Astien, l'historique complet des Tours 0, 1 et 2, le profil des 11 concurrents, et les scripts Python prêts à l'emploi**.

### Structure du dossier `memoire_agent_cesim/`
1. [`00_MASTER_INDEX_POUR_AGENT_IA.md`](file:///c:/Users/len/OneDrive/Bureau/ceism/memoire_agent_cesim/00_MASTER_INDEX_POUR_AGENT_IA.md) *(ce fichier)* : Vue d'ensemble, mapping des équipes, calendrier et procédure opérationnelle (SOP).
2. [`01_BAREME_SECRET_ERIC_ASTIEN_15_CRITERES.md`](file:///c:/Users/len/OneDrive/Bureau/ceism/memoire_agent_cesim/01_BAREME_SECRET_ERIC_ASTIEN_15_CRITERES.md) : La formule Excel exacte du professeur (`1 + NB.SI(moins_bons)`), les 15 critères (180 pts), et les **5 pièges mortels du barème** découverts aux Tours 1 et 2.
3. [`02_REGLES_PROFONDES_ET_MECANIQUES_CESIM.md`](file:///c:/Users/len/OneDrive/Bureau/ceism/memoire_agent_cesim/02_REGLES_PROFONDES_ET_MECANIQUES_CESIM.md) : Toutes les lois économiques et formules du jeu (Demande, Production interne vs Sous-traitance, Fournisseurs ESG / Achats, RH & Productivité ingénieurs, R&D interne vs Licences, Marketing, Logistique & Prix de cession, Finance & Transferts de cash).
4. [`03_HISTORIQUE_COMPLET_TOURS_0_1_2_ET_CONCURRENTS.md`](file:///c:/Users/len/OneDrive/Bureau/ceism/memoire_agent_cesim/03_HISTORIQUE_COMPLET_TOURS_0_1_2_ET_CONCURRENTS.md) : Autopsie chiffrée du Tour d'essai (2e, 122 pts), du Tour 1 (8e, 96 pts) et du **Tour 2 (1er de l'Univers 1 avec 140 pts et 10 774 M$ de résultat net !)** + forces/faiblesses des 11 équipes adverses.
5. [`04_STRATEGIE_ET_PLAYBOOK_TOUR_3_ET_SUIVANTS.md`](file:///c:/Users/len/OneDrive/Bureau/ceism/memoire_agent_cesim/04_STRATEGIE_ET_PLAYBOOK_TOUR_3_ET_SUIVANTS.md) : Plan d'attaque précis pour le **Tour 3** et les tours suivants (comment passer de 140 pts à 155+ pts en corrigeant l'utilisation des usines USA et les coûts unitaires pondérés).
6. [`05_OUTILS_SCRIPTS_ET_CONNEXION_CHROME_DEVTOOLS.md`](file:///c:/Users/len/OneDrive/Bureau/ceism/memoire_agent_cesim/05_OUTILS_SCRIPTS_ET_CONNEXION_CHROME_DEVTOOLS.md) : Comment extraire en direct l'interface Cesim depuis Chrome (port 9222 / WebSocket) et comment lancer les scripts de calcul automatique du classement et d'analyse de la concurrence.
7. [`06_ALGORITHMES_MATHEMATIQUES_CALIBRES_DU_MOTEUR_CESIM.md`](file:///c:/Users/len/OneDrive/Bureau/ceism/memoire_agent_cesim/06_ALGORITHMES_MATHEMATIQUES_CALIBRES_DU_MOTEUR_CESIM.md) : **Les équations mathématiques exactes du moteur Cesim calibrées par régression ($R^2 = 0,9924$)** sur nos vraies données (élasticités Prix/Équipements/Pub par zone, coût exact d'un équipement `700$ US / 650$ CN / 750$ EU`, courbe en U exacte du coût de production interne avec le minimum à `80–90 %` et le piège de la pénalité d'heures sup à `100 %`, et équation de productivité RH).
8. [`calculateur_classement_astien.py`](file:///c:/Users/len/OneDrive/Bureau/ceism/memoire_agent_cesim/calculateur_classement_astien.py) & [`analyseur_concurrence_et_decisions.py`](file:///c:/Users/len/OneDrive/Bureau/ceism/memoire_agent_cesim/analyseur_concurrence_et_decisions.py) : Scripts Python autonomes pour calculer le classement officiel des 15 critères et prédire les mouvements des 11 concurrents au tour suivant.

---

## 🗺️ 2. Table de Correspondance des 12 Équipes de l'Univers 1 (`ESYBIA2AS`)

Les équipes avaient des noms de couleurs au Tour d'essai et au début du Tour 1, puis ont été renommées. Le PDF du professeur utilise parfois un mix des anciens et nouveaux noms. Voici la correspondance exacte dans l'ordre des colonnes Cesim (1 à 12) :

| Colonne Cesim | Nom Actuel (`Tour 2.html`) | Ancien Nom (`Période Test` / `Période 1`) | Statut fin Tour 2 (Points / Rang estimé / Situation) |
| :---: | :--- | :--- | :--- |
| **1** | **`Ren'Auto`** | `Vert` | **98 pts (7e)** — `9 112 M$` net, `0 k` stock, `0 M$` découvert, prix ultra-élevés + grosse pub/R&D. |
| **2** | **`AURA`** | `Rouge` | **96 pts (8e)** — `5 792 M$` net, `557 k` stock, `3 814 M$` découvert Chine, coût composants `6 000 $`. |
| **3** | **`IronHorse` (NOUS)** | **`Bleu`** | **🥇 140 pts (1er)** — **`10 774 M$` net (#1)**, **`0 k` stock (#1)**, **`0 M$` découvert**, **Productivité `1,085` (#1)**, Ratio fonds propres **`74,66 %`**. |
| **4** | **`YANAUTO`** | `Orange` | **103 pts (6e)** — `9 476 M$` net, mais **`837 k` stock** et **`10 098 M$` de découvert Chine** ! |
| **5** | **`tomobil`** | `Gris` | **57 pts (11e)** — `479 M$` net, en faillite technique : **`1 135 k` stock (`15,9 Mds$`)** et **`10 130 M$` découvert** ! |
| **6** | **`GT-Automobile VI`** | `Ocre` | **104 pts (5e)** — `10 493 M$` net (#4), mais **`774 k` stock** et **`6 009 M$` découvert Chine**. |
| **7** | **`Vrooom Vroooom`** | `Rose` *(1er au Tour 1)* | **54 pts (12e)** — Effondré à `393 M$` net : prix Europe aberrant (`27 000 €`), **`1 098 k` stock (`14,6 Mds$`)** et **`9 765 M$` découvert** ! |
| **8** | **`POLRAMOS`** | `POLRAMOS` | **🥈 133 pts (2e — Rival #1)** — `10 529 M$` net (#3), `0 M$` découvert, Ratio fonds propres **`95,32 %` (#1)**, mais `322 k` voitures en stock en Chine. |
| **9** | **`Ça Roule`** | `Jaune` / `JAUNE GT` | **104 pts (4e)** — `7 331 M$` net, `10 k` stock, `0 M$` découvert, grosses parts de marché (`11,0 %`) mais marges faibles. |
| **10** | **`BM2P - BMDoublePied`** | `Olive` | **🥉 109 pts (3e)** — `9 216 M$` net, `531 k` stock, `2 291 M$` découvert Chine, 9 500 ingénieurs. |
| **11** | **`TABCHOUR AUTO`** | `Marron` *(2e au Tour 1)* | **90 pts (9e)** — `10 685 M$` net (#2), mais **`878 k` stock (`13,2 Mds$`)**, **`6 905 M$` découvert Chine**, et coûts unitaires très élevés (`14 017 $ - 15 041 $`). |
| **12** | **`MO'THOR`** | `Noir` | **68 pts (10e)** — `2 618 M$` net, `772 k` stock, `5 200 M$` découvert Chine, 12 000 ingénieurs (coût R&D excessif). |

---

## ⏰ 3. Calendrier Officiel des Tours (`ESYBIA2AS`)

- **Tour d'entraînement 1** : Mercredi 18 nov. 13:00 *(Terminé — 2e avec 122 pts)*
- **Tour 1** : Mercredi 18 nov. 16:19 *(Terminé — 8e avec 96 pts à cause des `371 k` de stock [`2 pts`] et du découvert Chine [`4 pts` en Indépendance financière])*
- **Tour 2** : Mercredi 18 nov. 17:15 *(Terminé — **1er estimé avec 140 pts et #1 Résultat Net 10 774 M$**)*
- **Tour 3** : **Jeudi 19 nov. à 10:20**
- **Tours 4, 5 et suivants :** ⚠️ **Toujours vérifier l'heure exacte directement dans l'onglet `Planning` / pied de page de Cesim** (le planning du professeur indique `13h30` / `15h50` alors que certaines captures affichaient `11h25` / `14h40`). Se fier uniquement au compte à rebours affiché en haut à gauche sur Cesim !

---

## 🛠️ 4. Procédure Standard (SOP) pour l'Agent IA à chaque Nouveau Tour

Dès que Reda te sollicite pour un nouveau tour :
1. **Lire les Conditions de Marché du nouveau tour** (via Chrome DevTools WebSocket ou capture/texte fourni par Reda) :
   - Vérifier les croissances annoncées par zone (USA, Chine, Europe) et l'adoption technologique (Thermique, Hybride, Électrique, Hydrogène).
   - Vérifier les taux de change (`EUR/USD`, `RMB/USD`), les taux d'imposition (USA, Chine, Europe), les droits de douane/tarifs, les coûts et plafonds de **sous-traitance**, et les alertes **ESG / Fournisseurs**.
2. **Analyser les résultats du tour précédent** avec [`calculateur_classement_astien.py`](file:///c:/Users/len/OneDrive/Bureau/ceism/memoire_agent_cesim/calculateur_classement_astien.py) sur le fichier `manuels/Results for Univers 1, Tour X.html`.
3. **Vérifier l'état des stocks et des usines** d'`IronHorse` (USA et Chine) ainsi que les équipements débloqués en R&D.
4. **Construire la feuille de route complète onglet par onglet** (`Demande`, `Production -> Planning / Investissements / Achats`, `RH`, `R&D`, `Marketing -> USA / Chine / Europe`, `Logistique`, `Finance`) en respectant **les 10 règles d'or du barème Eric Astien** détaillées dans [`01_BAREME_SECRET_ERIC_ASTIEN_15_CRITERES.md`](file:///c:/Users/len/OneDrive/Bureau/ceism/memoire_agent_cesim/01_BAREME_SECRET_ERIC_ASTIEN_15_CRITERES.md).
5. **Toujours vérifier dans `Liste de décisions` (`decisionChecklist`)** quelle colonne est actuellement enregistrée comme décision d'équipe (`IronHorse`) avant la deadline !
