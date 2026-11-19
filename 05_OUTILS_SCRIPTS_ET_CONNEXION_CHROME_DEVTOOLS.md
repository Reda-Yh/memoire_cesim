# 🛠️ OUTILS, SCRIPTS PYTHON & CONNEXION LIVE CHROME DEVTOOLS

Ce fichier documente tous les outils techniques créés dans ce dépôt pour permettre à n'importe quel Agent IA d'inspecter l'interface Cesim en direct et de calculer instantanément le classement d'Eric Astien.

---

## 📂 1. Emplacement des Fichiers Clés du Projet

- **Rapports officiels HTML téléchargés depuis Cesim :**
  - [`manuels/Results for Univers 1, Tour 1.html`](file:///c:/Users/len/OneDrive/Bureau/ceism/manuels/Results%20for%20Univers%201,%20Tour%201.html)
  - [`manuels/Results for Univers 1, Tour 2.html`](file:///c:/Users/len/OneDrive/Bureau/ceism/manuels/Results%20for%20Univers%201,%20Tour%202.html)
  - *(Quand le Tour 3 sera terminé, Reda téléchargera `manuels/Results for Univers 1, Tour 3.html`)*
- **Rapports parsés en texte structuré (`|`-separated tables) :**
  - [`data/real_competition/raw_reports/parsed_tour1_results_html.txt`](file:///c:/Users/len/OneDrive/Bureau/ceism/data/real_competition/raw_reports/parsed_tour1_results_html.txt)
  - [`data/real_competition/raw_reports/parsed_tour2_results_html.txt`](file:///c:/Users/len/OneDrive/Bureau/ceism/data/real_competition/raw_reports/parsed_tour2_results_html.txt)
- **Classements officiels PDF du professeur Eric Astien :**
  - [`manuels/CLASSEMENT DES ÉQUIPES ESYBIA2AS.pdf`](file:///c:/Users/len/OneDrive/Bureau/ceism/manuels/CLASSEMENT%20DES%20%C3%89QUIPES%20ESYBIA2AS.pdf) *(Période Test)*
  - [`manuels/CLASSEMENT DES ÉQUIPES ESYBIA2AS (1).pdf`](file:///c:/Users/len/OneDrive/Bureau/ceism/manuels/CLASSEMENT%20DES%20%C3%89QUIPES%20ESYBIA2AS%20(1).pdf) *(Période Test + Période 1)*

---

## 🧮 2. Utiliser le Calculateur Automatique de Classement Eric Astien (`calculateur_classement_astien.py`)

Nous avons créé le script autonome [`memoire_agent_cesim/calculateur_classement_astien.py`](file:///c:/Users/len/OneDrive/Bureau/ceism/memoire_agent_cesim/calculateur_classement_astien.py).  
Il accepte en entrée **soit un fichier HTML brut exporté de Cesim** (`Results for Univers 1, Tour X.html`), **soit un fichier texte déjà parsé** (`parsed_tourX_results_html.txt`), et affiche :
1. Le **Classement général estimé des 12 équipes** (points sur 180, résultat net, stocks en volume, découvert bancaire).
2. Le **Tableau détaillé des 15 critères du barème d'Eric Astien** avec les valeurs exactes et les points (`1` à `12`) de chaque équipe.

### Commande PowerShell pour lancer le calculateur sur n'importe quel tour :
```powershell
python "c:\Users\len\OneDrive\Bureau\ceism\memoire_agent_cesim\calculateur_classement_astien.py" "c:\Users\len\OneDrive\Bureau\ceism\manuels\Results for Univers 1, Tour 2.html"
```

---

## 🔮 2.bis Utiliser le Radar Concurrence & Prédicteur du Tour Suivant (`analyseur_concurrence_et_decisions.py`)

Le script [`memoire_agent_cesim/analyseur_concurrence_et_decisions.py`](file:///c:/Users/len/OneDrive/Bureau/ceism/memoire_agent_cesim/analyseur_concurrence_et_decisions.py) extrait automatiquement du dernier rapport HTML ce que **les 11 autres équipes auront au prochain tour** :
- Leurs **nouvelles usines qui entrent en service au Tour $N+1$** (`Tour suivant -> USA / Chine`) et leur capacité brute exacte (`k unités`),
- Leurs **stocks invendus en Thermique et en Hybride** qu'ils seront forcés d'écouler au prochain tour,
- Leur **trésorerie et leur découvert bancaire** (`CRISE CASH`),
- Et génère un **Diagnostic Tactique automatique** (quelles équipes sont forcées de baisser leurs prix ou de couper leur production, quelles équipes ont sur-construit des usines comme `Ren'Auto` avec 10 usines US + 7 usines Chine au Tour 3 !).

```powershell
python "c:\Users\len\OneDrive\Bureau\ceism\memoire_agent_cesim\analyseur_concurrence_et_decisions.py" "c:\Users\len\OneDrive\Bureau\ceism\manuels\Results for Univers 1, Tour 2.html"
```

---

## 🌐 3. Comment Lire l'Interface Cesim en Direct dans Chrome (Port 9222 / Raw WebSocket)

Lorsque Chrome est ouvert sur `https://bordeaux-inp.cesim.com/`, l'agent peut lire directement tous les onglets (`Conditions de marché`, `Demande`, `Production`, `RH`, `R&D`, `Marketing`, `Logistique`, `Finance`, `Budgets`, `Liste de décisions`) sans utiliser `curl` sur `/json` (qui renvoie parfois 404/403 sur Chrome Windows) en lisant directement le fichier **`C:\Users\len\AppData\Local\Google\Chrome\User Data\DevToolsActivePort`**.

### Modèle de script Python pour lire un onglet Cesim en direct :
```python
import os, json, socket, base64, hashlib, struct

port_file = r"C:\Users\len\AppData\Local\Google\Chrome\User Data\DevToolsActivePort"
with open(port_file, "r") as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]
port = int(lines[0])

# Pour lister les targets ou exécuter du JS sur la page Cesim via CDP :
# (Voir aussi les scripts existants dans le dossier scratch de la session ou utiliser le subagent `browser` si disponible).
```

### Routes Hash (`window.location.hash`) de l'Application Cesim :
- `#/marketConditions` : Conditions de marché du tour en cours
- `#/demand` : Onglet Demande
- `#/production/planning` : Production -> Planning
- `#/production/inventory` : Production -> Stocks
- `#/production/investments` : Production -> Investissements (Usines)
- `#/production/procurement` : Production -> Achats (Fournisseurs ESG)
- `#/hr` : Ressources Humaines (Effectifs, Salaires, Formation)
- `#/rd` : Recherche & Développement (Jours-homme + Licences)
- `#/marketing/usa` | `#/marketing/china` | `#/marketing/europe` : Marketing par zone
- `#/logistics` : Logistique & Prix de cession interne
- `#/finance` : Finance (Emprunt / Remboursement Dette LT et Transferts internes de trésorerie)
- `#/budgets/global` | `#/budgets/usa` | `#/budgets/china` | `#/budgets/europe` : Comptes de résultat et Bilans prévisionnels en temps réel
- `#/decisionChecklist` : Liste de décisions (permet de comparer côte à côte les colonnes **`IronHorse`**, **`Reda Yahya`**, **`Yahya Bel Hajjam`**, **`Nour Doghmi`**, **`Mohamed Ajaji`** !)
