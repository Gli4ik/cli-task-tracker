import json
import os.path
from enum import Enum

from Classes.task import Task, Status


class TaskManager:
    def __init__(self, json_path: str):
        if not os.path.exists(json_path):
            raise FileNotFoundError("File was not found.")

        self.json_path = json_path
        self.tasks = []
        with open(self.json_path) as file:
            contents = file.read()
            if len(contents) > 0:
                contents = json.loads(contents)
                for task_dict in contents:
                    task = Task.deserialize(task_dict)
                    self.tasks.append(task)

    def add_task(self, description: str, status=Status.TODO):
        identifier = (self.tasks[-1].id + 1) if len(self.tasks) > 0 else 1
        task = Task(identifier, description, status)
        self.tasks.append(task)
        self._write_file()

    def delete_task(self, identifier: int):
        for task in self.tasks:
            if task.id == identifier:
                self.tasks.remove(task)
                self._write_file()
                print(f'Task "{task.description}" was deleted.')
                return
        print(f'Task with id "{identifier}" was not found.')

    def update_task(self, identifier: int, description: str):
        for task in self.tasks:
            if task.id == identifier:
                task.description = description
                self._write_file()
                return
        print("Task not found")

    def change_status(self, identifier: int, status: str):
        for task in self.tasks:
            if task.id == identifier:
                task.status = status
                self._write_file()
                print(f'Task "{task.description}" was changed to "{status}".')
                return
        print(f'Task with id "{identifier}" was not found.')

    def list_tasks(self, status=''):
        if len(self.tasks) == 0:
            print("No tasks found.")
            return

        if status != '':
            print(f"Tasks with status \"{status}\":")
            for task in self.tasks:
                if task.status == status:
                    print(task)
        else:
            print(f"|{'Tasks':^31}| {'ID':^3}|{'STATUS':^14}|{'CREATED AT':^21}|{'UPDATED AT':^21}|")
            print('|'+ "-"*95 + '|')
            for task in self.tasks:
                print(task)

    @staticmethod
    def task_serializer(obj):
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        if isinstance(obj, Enum):
            return obj.value
        raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

    def _write_file(self):
        with open(self.json_path, "w") as file:
            file.write(json.dumps(self.tasks, indent=4, default=TaskManager.task_serializer))