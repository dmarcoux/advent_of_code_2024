import pathlib


def parse(puzzle_input: str) -> str:
    """Parse input."""


def part1(data: str) -> int:
    """Solve part 1."""


def part2(data: str) -> int:
    """Solve part 2."""


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    return part1(data), part2(data)


if __name__ == "__main__":
    puzzle_input = (pathlib.Path(__file__).parent / "day_template_input.txt").read_text().strip()
    part1_solution, part2_solution = solve(puzzle_input)
    print(f"day_template\npart_1: {part1_solution}\npart_2: {part2_solution}")  # noqa: T201
