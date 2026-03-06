from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@dataclass
class Task:
    id: int
    payload: dict


@runtime_checkable
class TaskGiver(Protocol):
    def get_tasks(self) -> list[Task]: pass
