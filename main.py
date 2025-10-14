from controllers.task_controller import add_cmd, list_cmd, delete_cmd

def menu():
    print("\n••• ToDoList •••")
    print("1 - Ajouter une tâche")
    print("2 - Lister les tâches")
    print("3 - Supprimer une tâche")
    print("4 - Quitter")

def main():
    while True:
        menu()
        choix = input("Votre choix : ")

        if choix == "1":
            titre = input("Titre de la tâche : ")
            add_cmd(titre)

        elif choix == "2":
            list_cmd()

        elif choix == "3":
            try:
                task_id = int(input("ID de la tâche à supprimer : "))
                delete_cmd(task_id)
            except ValueError:
                print("=> Merci d'entrer un nombre valide.")

        elif choix == "4":
            print("À bientôt 👋")
            break

        else:
            print("=> Choix invalide.")

if __name__ == "__main__":
    main()
