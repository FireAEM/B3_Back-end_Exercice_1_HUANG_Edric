from flask import Flask, request, jsonify
from models.task import TaskManager

app = Flask(__name__)
task_manager = TaskManager()

@app.get("/tasks")
def get_tasks():
    tasks = [task.to_dict() for task in task_manager.list_tasks()]
    return jsonify(tasks), 200

@app.post("/tasks")
def create_task():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "JSON invalide ou absent."}), 400
    title = data.get("title")
    if not title or not isinstance(title, str):
        return jsonify({"error": "Le champ 'title' est requis et doit être une chaîne."}), 400
    task = task_manager.add(title)
    return jsonify(task.to_dict()), 201

@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    ok = task_manager.delete(task_id)
    if not ok:
        return jsonify({"error": "ID introuvable."}), 404
    return jsonify({"message": "Tâche supprimée."}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)