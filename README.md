# B3_Back-end_Exercice_1_HUANG_Edric

---

## Table des matières
- [Présentation du projet](#présentation-du-projet)
- [Prérequis](#prérequis)
- [Installation](#installation-création-de-lenvironnement)
- [Exécution - CLI interactive](#exécution---cli-interactive)
- [Exécution - API Flask](#exécution---api-flask)
- [Structure du projet](#structure-du-projet)

---

### Présentation du projet

Mini ToDoList en Python organisée selon le modèle MVC. L’application fournit deux interfaces complémentaires :
- une interface CLI interactive (menu en boucle) pour ajouter, lister et supprimer des tâches en mémoire,
- une API REST minimale implémentée avec Flask pour exposer les mêmes opérations via HTTP en JSON.

---

### Prérequis

- Python installé (version 3.8+ recommandée, ici testé avec 3.11 / 3.12).  
- Ligne de commande (PowerShell, Terminal, Bash...).  
- (Optionnel) VSCode pour édition et exécution.

---

### Installation - création de l'environnement

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

Remarque : le fichier requirements.txt a été généré par `pip freeze`. Flask et ses dépendances sont listés pour permettre d’exécuter l’API.

---

### Exécution - CLI interactive

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

### Exécution - API Flask

L’API Flask permet d’accéder au TaskManager via HTTP en JSON.

Prérequis
- Activer l’environnement virtuel avant d’exécuter l’API (voir section Installation).

Démarrage du serveur
```bash
python app.py
```
Le serveur écoute par défaut sur http://127.0.0.1:5000 et est lancé en mode debug pour le développement. Désactiver ou configurer le mode debug pour un usage en production.

Endpoints principaux

- GET /tasks  
  - Description : retourne la liste des tâches au format JSON.  
  - Réponse : 200 OK, corps JSON array d’objets { "id": int, "title": string }  
  - Exemple :
    ```bash
    curl http://127.0.0.1:5000/tasks
    ```

- POST /tasks  
  - Description : crée une nouvelle tâche.  
  - Requête : Content-Type: application/json, corps JSON { "title": "..." }  
  - Réponse : 201 Created, retourne l’objet tâche créé en JSON  
  - Erreurs : 400 Bad Request si payload absent ou invalide  
  - Exemple :
    ```bash
    curl -X POST http://127.0.0.1:5000/tasks \
      -H "Content-Type: application/json" \
      -d '{"title":"Acheter du pain"}'
    ```

- DELETE /tasks/<id>  
  - Description : supprime la tâche identifiée par id.  
  - Réponse : 200 OK si supprimée, 404 Not Found si l’ID n’existe pas  
  - Exemple :
    ```bash
    curl -X DELETE http://127.0.0.1:5000/tasks/1
    ```

Comportement et remarques
- L’API réutilise le même TaskManager en mémoire que la CLI ; redémarrer le serveur réinitialise la liste des tâches.  
- `jsonify` est utilisé pour produire des réponses JSON et gérer automatiquement l’en-tête Content-Type.  
- En développement, `debug=True` facilite le rechargement automatique et l’affichage des erreurs. Retirer le debug en production et configurer l’application via des variables d’environnement.  

---

### Structure du projet

```
.
├── app.py                  # API Flask simple (point d'entrée)
├── controllers/
│   └── task_controller.py   # logique de contrôle
├── models/
│   └── task.py              # classe Task et TaskManager
├── views/
│   └── cli.py              # affichage CLI
├── main.py                 # CLI interactive (menu en boucle)
└── requirements.txt        # dépendances (Flask listé)
```