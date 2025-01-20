import os.path

from task import Task


class TaskManager:
    def __init__(self, json: str):
        if not os.path.exists(json):
            raise FileNotFoundError("File was not found.")
        self.json = json

    def add_task(self, description: str):
        task = Task(description)
        with open(self.json, "a") as file:
            file.write(task.serialize())