from enum import Enum
import time
import json


class Status(Enum):
    DONE = True
    IN_PROGRESS = False


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
        json_string = json.dumps(self.to_dict())
        return json_string

    def to_dict(self) -> dict:
        dict = {
            "id": self.id,
            "description": self.description,
            "status": True if self.status == Status.DONE else False,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        return dict
