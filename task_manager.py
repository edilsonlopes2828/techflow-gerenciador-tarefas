
import json
from pathlib import Path


class TaskManager:
    PRIORITIES = {"Baixa", "Média", "Alta"}

    def __init__(self, storage_path="tasks.json"):
        self.path = Path(storage_path)

        if self.path.exists():
            try:
                self.tasks = json.loads(
                    self.path.read_text(encoding="utf-8")
                )
            except (json.JSONDecodeError, OSError):
                self.tasks = []
        else:
            self.tasks = []

    def _save(self):
        self.path.write_text(
            json.dumps(self.tasks, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    def add_task(self, title, description="", priority="Média"):
        title = title.strip()

        if not title:
            raise ValueError("O título é obrigatório.")

        if priority not in self.PRIORITIES:
            raise ValueError("Prioridade inválida.")

        task = {
            "id": max(
                [item["id"] for item in self.tasks],
                default=0
            ) + 1,
            "title": title,
            "description": description.strip(),
            "priority": priority,
            "completed": False
        }

        self.tasks.append(task)
        self._save()
        return task.copy()

    def list_tasks(self, status="all"):
        if status == "pending":
            tasks = [
                task for task in self.tasks
                if not task["completed"]
            ]
        elif status == "completed":
            tasks = [
                task for task in self.tasks
                if task["completed"]
            ]
        else:
            tasks = self.tasks

        return [task.copy() for task in tasks]

    def _find(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task

        raise KeyError("Tarefa não encontrada.")

    def update_task(self, task_id, title, description="", priority="Média"):
        task = self._find(task_id)
        title = title.strip()

        if not title:
            raise ValueError("O título é obrigatório.")

        if priority not in self.PRIORITIES:
            raise ValueError("Prioridade inválida.")

        task["title"] = title
        task["description"] = description.strip()
        task["priority"] = priority

        self._save()
        return task.copy()

    def toggle_task(self, task_id):
        task = self._find(task_id)
        task["completed"] = not task["completed"]
        self._save()
        return task.copy()

    def delete_task(self, task_id):
        task = self._find(task_id)
        self.tasks.remove(task)
        self._save()
        return task.copy()
