from src.source import RandomSource, APISource
from src.task import TaskGiver


def main() -> None:
    while inp := input():
        if not inp.isdigit(): continue
        tasks_rnd = RandomSource(int(inp))
        tasks_api = APISource(int(inp))
        if isinstance(tasks_rnd, TaskGiver) and isinstance(tasks_api, TaskGiver):
            print(tasks_rnd.get_tasks())
            print(tasks_api.get_tasks())


if __name__ == "__main__":
    main()
