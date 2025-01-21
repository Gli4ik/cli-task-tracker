import json
import os.path

from Classes.task import Task


class TaskManager:
    def __init__(self, json: str):
        if not os.path.exists(json):
            raise FileNotFoundError("File was not found.")
        self.json = json

    def add_task(self, description: str):
        tasks = list()
        with open(self.json, "r") as file:
            contents = file.read()
            if len(contents) > 0:
                tasks = json.loads(contents)
        id = tasks[-1]["id"] + 1 if len(tasks) > 0 else 1
        task = Task(id, description)
        tasks.append(task.to_dict())
        with open(self.json, "w") as file:
            file.write(json.dumps(tasks, indent=4))

    def delete_task(self, id: int):
        with open(self.json, "r") as file:
            tasks = json.loads(file.read())
        for task in tasks:
            if task["id"] == id:
                tasks.remove(task)
                with open(self.json, "w") as file:
                    file.write(json.dumps(tasks, indent=4))
                print(f'Task "{task['description']}" was deleted.')
                return
        print(f'Task with id "{id}" was not found.')

    def update_task(self, id:int, description: str):
        with open(self.json, "r") as file:
            tasks = json.loads(file.read())
        for task in tasks:
            if task["id"] == id:
                task["description"] = description
                with open(self.json, "w") as file:
                    file.write(json.dumps(tasks, indent=4))
                return
        print("Task not found")

    def change_status(self, id: int, status: str):
        with open(self.json, "r") as file:
            tasks = json.loads(file.read())
        for task in tasks:
            if task["id"] == id:
                task["status"] = status
                # TODO : Add updated_ad change
                with open(self.json, "w") as file:
                    file.write(json.dumps(tasks, indent=4))
                    print(f'Task "{task["description"]}" was changed to "{status}".')
                return
        print(f'Task with id "{id}" was not found.')

    def print_tasks(self, status=''):
        tasks = list()
        with open(self.json, "r") as file:
            contents = file.read()
            if len(contents) > 0:
                tasks = json.loads(contents)
        if status != '':
            print(f"Tasks with status \"{status}\":")
            for task in tasks:
                if task["status"] == status:
                    TaskManager._print_task(task)
        else:
            print(f"Tasks: ")
            for task in tasks:
                TaskManager._print_task(task)

    @staticmethod
    def _print_task(task : dict):
        print(f"Task: {task['description']}, "
              f"id: {task['id']}, "
              f"created at: {task['created_at']}, "
              f"updated at: {task['updated_at']}, "
              f"status: {task['status']}")