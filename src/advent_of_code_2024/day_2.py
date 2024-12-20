import pathlib
from itertools import pairwise


def parse(puzzle_input: str) -> list[list[int]]:
    """Parse input."""
    puzzle_input_lines = puzzle_input.splitlines()
    # I miss Elixir's pipe operator when I write code like this... hehehe
    return list(map(lambda line: list(map(int, line.split(" "))), puzzle_input_lines))


def part1(reports: list[list[int]]) -> int:
    """Solve part 1."""
    safe_reports = 0
    safe = true

    # think about using guard clauses whenever possible
    for report in reports:
        for (current_level, next_level) in pairwise(report)
            # compare current level with next level
            # check if increasing or decreasing
            #   it must remain the same
            # if difference >= 1 and difference <= 3
            #   safe remains true
            # else
            #   safe is now false
            #   break()
        # if safe is true
        #   safe_reports += 1
        # else
        #   set safe to true again and break()


    return safe_reports


def part2(data: list[list[int]]) -> int:
    """Solve part 2."""
    return 0


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    return part1(data), part2(data)


if __name__ == "__main__":
    puzzle_input = (pathlib.Path(__file__).parent / "day_2_input.txt").read_text().strip()
    part1_solution, part2_solution = solve(puzzle_input)
    print(f"day_2\npart_1: {part1_solution}\npart_2: {part2_solution}")  # noqa: T201
