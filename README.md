# B3_Back-end_Exercice_1_HUANG_Edric

---

## Table des matières
- [Présentation du projet](#présentation-du-projet)
- [Prérequis](#prérequis)
- [Installation](#installation-création-de-lenvironnement)
- [Exécution](#exécution-mode-interactif)
- [Structure du projet](#structure-du-projet)

---

### Présentation du projet

Mini ToDoList CLI en Python organisée selon le modèle MVC.  

---

### Prérequis

- Python installé (version 3.8+ recommandée, ici testé avec 3.11 / 3.12).  
- Ligne de commande (PowerShell, Terminal, Bash...).  
- (Optionnel) VSCode pour édition et exécution.

---

### Installation (création de l’environnement)

1. Ouvrir un terminal dans le dossier racine du projet.  
2. Créer l’environnement virtuel :
```bash
python -m venv venv
```
3. Activer l’environnement virtuel :

- Windows PowerShell
```powershell
.\venv\Scripts\Activate
```
- macOS / Linux
```bash
source venv/bin/activate
```

4. Installer les dépendances (fichier fourni requirements.txt) :
```bash
pip install -r requirements.txt
```

Remarque : le fichier requirements.txt a été généré par `pip freeze`. Certaines dépendances (ex. Flask) ont été installées lors de la préparation de l’environnement mais ne sont pas nécessaires pour la version CLI interactive.

---

### Exécution (mode interactif)

Lancer l’application depuis le dossier racine (venv activé) :
```bash
python main.py
```

Fonctionnement : le programme ouvre un menu interactif. Choisir une option puis suivre les instructions. Exemple de session :

- Ajouter une tâche  
  - Choisir `1` puis entrer le titre.
- Lister les tâches  
  - Choisir `2`.
- Supprimer une tâche  
  - Choisir `3` puis entrer l’ID.
- Quitter  
  - Choisir `4`.

Important : la version fournie conserve les tâches **en mémoire** pendant l’exécution uniquement. Si vous fermez le programme, la liste redémarrera vide.

---

### Structure du projet

```
.
├── controllers/
│   └── task_controller.py   # logique de contrôle
├── models/
│   └── task.py              # classe Task et TaskManager
├── views/
│   └── cli.py               # affichage CLI
├── main.py                  # point d’entrée
├── requirements.txt         # dépendances
└── venv/                    # environnement virtuel (à ignorer dans git)
```