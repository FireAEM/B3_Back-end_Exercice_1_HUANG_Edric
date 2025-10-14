def show_tasks(tasks):
    if not tasks:
        print("=> Aucune tâche.")
        return
    for task in tasks:
        print(task)

def show_message(message):
    print("=>", message)