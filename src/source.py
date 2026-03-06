from src.task import Task
from src.constants import STRINGS
from os import path
import hashlib
import logging
import random
logger = logging.getLogger(__name__)


class APISource:
    def __init__(self, amount: int = 5):
        self.amount = amount

    def get_tasks(self) -> list[Task]:
        tasks = []
        logging.basicConfig(filename='apisrc.log', level=logging.INFO)
        for i in range(1, self.amount + 1):
            code = random.randint(10000, 99999)
            current_task = Task(
                id=f"task_{i}",
                payload={
                    "source": "api",
                    "code": code,
                    "description": random.choice(STRINGS),
                }
            )
            tasks.append(current_task)
            logger.info(f"Initiated {current_task.id} with API using code {code}")


class FileSource:
    def __init__(self, file_dir: str):
        if not path.isfile(file_dir):
            logger.info(f"Failed to open {file_dir}")
            raise ValueError("File was not found")
        self.file = path.abspath(file_dir)

    def get_tasks(self) -> list[Task]:
        logging.basicConfig(filename='filesrc.log', level=logging.INFO)
        tasks = []
        try:
            with open(self.file, encoding="utf-8") as f:
                for line in f:
                    id, description = line.split(maxsplit=1)
                    current_task = Task(
                        id=f"task_{id}",
                        payload={
                            "source": "file",
                            "path": self.file,
                            "description": description,
                        }
                    )
                    tasks.append(current_task)
                    logger.info(f"Initiated {current_task.id} from file located in \"{self.file}\"")

        except PermissionError as e:
            logger.info(f"Failed to read {self.file}: {e}")
            raise ValueError("Failed to read file due to permission")

        except UnicodeDecodeError as e:
            logger.info(f"Failed to read {self.file}: {e}")
            raise ValueError("Failed to decode file")

        except ValueError as e:
            logger.info(f"File does not contain correct info")
            raise ValueError(f"Bad line: {e}")

class RandomSource:
    def __init__(self, amount: int = 5):
        self.amount = amount

    def get_tasks(self) -> list[Task]:
        logging.basicConfig(filename='rndsrc.log', level=logging.INFO)
        tasks = []
        for i in range(1, self.amount + 1):
            current_task = Task(
                id=f"task_{i}",
                payload={
                    "source": "generator",
                    "hash": hashlib.sha256(f"RANDOM{random.randint(100, 10000)}".encode()).hexdigest(),
                }
            )
            tasks.append(current_task)
            logger.info(f"Initiated {current_task.id} with hash \"{current_task.payload['hash']}\" through generator")
        return tasks
