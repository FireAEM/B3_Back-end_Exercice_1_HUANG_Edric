class Task:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __repr__(self):
        return f"Task({self.id}, {self.title!r})"

    def __str__(self):
        return f"{self.id}: {self.title}"

    def to_dict(self):
        return {"id": self.id, "title": self.title}

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title):
        new_id = len(self.tasks) + 1
        task = Task(new_id, title)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def delete(self, task_id):
        before = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        return len(self.tasks) < before