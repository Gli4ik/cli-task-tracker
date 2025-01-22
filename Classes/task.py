from enum import Enum
import time
import json


class Status(Enum):
    DONE = 'done'
    IN_PROGRESS = 'in-progress'
    TODO = 'todo'


class Task:
    def __init__(self, id: int, description: str, status=Status.TODO):
        self._id = id
        self._description = description
        self._status = status
        self.created_at = self.get_timestamp()
        self.updated_at = 'never'

    def __str__(self):
        output = '| '
        output += f'{self._description:<30}| '
        output += f'{self._id:<3}| '
        output += f'{self._status:<13}| '
        output += f'{self.created_at:<20}| '
        output += f'{self.updated_at:<20}| '
        return output

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value < 0:
            raise ValueError('ID cannot be negative')
        self._id = value
        self.updated_at = self.get_timestamp()

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value == '':
            raise ValueError('Description cannot be an empty string')
        self._description = value
        self.updated_at = self.get_timestamp()

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in [Status.DONE.value, Status.IN_PROGRESS.value, Status.TODO.value]:
            raise ValueError('Status can only be "done" or "in-progress" or "todo"')
        self._status = value
        self.updated_at = self.get_timestamp()

    def serialize(self) -> str:
        json_string = json.dumps(self.to_dict(), indent=4)
        return json_string

    @staticmethod
    def deserialize(source: dict):
        task = Task(source['id'], source['description'])
        task._status = source['status']
        task.created_at = source['created_at']
        task.updated_at = source['updated_at']
        return task

    @staticmethod
    def get_timestamp():
        timestamp = time.localtime(time.time())
        return (f"{timestamp.tm_hour:02}:{timestamp.tm_min:02}:{timestamp.tm_sec:02} "
                f"{timestamp.tm_mday:02}-{timestamp.tm_mon:02}-{timestamp.tm_year}")

    def to_dict(self) -> dict:
        dictionary = {
            "description": self._description,
            "id": self._id,
            "status": self._status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        return dictionary
