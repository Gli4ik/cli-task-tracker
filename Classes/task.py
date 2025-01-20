from enum import Enum
import time
import json


class Status(Enum):
    DONE = 2
    IN_PROGRESS = 1
    NOT_DONE = 0


class Task:
    def __init__(self, id: int, description: str):
        self.id = id
        self.description = description
        self.status = Status.IN_PROGRESS
        self.created_at = time.time()
        self.updated_at = self.created_at

    def update(self, description: str):
        self.description = description

    def done(self):
        self.status = Status.DONE

    def serialize(self) -> str:
        json_string = json.dumps(self.to_dict(), indent=4)
        return json_string

    @staticmethod
    def deserialize(json_string: str):
        dict = json.loads(json_string)
        task = Task(dict["id"], dict["description"])
        task.status = dict["status"]
        task.created_at = dict["created_at"]
        task.updated_at = dict["updated_at"]
        return task

    def to_dict(self) -> dict:
        dict = {
            "id": self.id,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        return dict
