from models.task import TaskManager
from views.cli import show_tasks, show_message

task_manager = TaskManager()

def add_cmd(title):
    task = task_manager.add(title)
    show_message(f"Tâche ajoutée : {task}")

def list_cmd():
    show_tasks(task_manager.list_tasks())

def delete_cmd(task_id):
    ok = task_manager.delete(task_id)
    show_message("Tâche supprimée." if ok else "ID introuvable.")