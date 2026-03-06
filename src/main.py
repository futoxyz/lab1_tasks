from src.source import RandomSource


def main() -> None:
    while inp := input():
        if not inp.isdigit(): continue
        tasks = RandomSource(int(inp))
        print(tasks.get_tasks())

if __name__ == "__main__":
    main()
