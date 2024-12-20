import bisect
import pathlib
from functools import reduce


def parse(puzzle_input: str) -> tuple[list[int], list[int]]:
    """Parse input."""
    left_sorted_list = []
    right_sorted_list = []

    puzzle_input_lines = puzzle_input.splitlines()
    for line in puzzle_input_lines:
        numbers = line.split("   ")
        bisect.insort(left_sorted_list, int(numbers[0]))
        bisect.insort(right_sorted_list, int(numbers[1]))

    return left_sorted_list, right_sorted_list


def part1(left_sorted_list: list[int], right_sorted_list: list[int]) -> int:
    """Solve part 1."""
    return reduce(__calculate_distance, zip(left_sorted_list, right_sorted_list, strict=False), 0)


def __calculate_distance(distance: int, numbers) -> int:  # noqa: ANN001
    left_number = numbers[0]
    right_number = numbers[1]

    return distance + abs(left_number - right_number)


def part2(left_sorted_list: list[int], right_sorted_list: list[int]) -> int:
    """Solve part 2."""
    return __calculate_similarity(left_sorted_list, right_sorted_list)


def __calculate_similarity(left_sorted_list: list[int], right_sorted_list: list[int]) -> int:
    similarity = 0

    for number in left_sorted_list:
        start_index = bisect.bisect_left(right_sorted_list, number)
        if start_index != len(right_sorted_list) and right_sorted_list[start_index] == number:
            end_index = bisect.bisect_right(right_sorted_list, number)
            occurences = end_index - start_index
            similarity += number * occurences
        else:
            continue

    return similarity


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    left_sorted_list, right_sorted_list = parse(puzzle_input)

    return part1(left_sorted_list, right_sorted_list), part2(left_sorted_list, right_sorted_list)


if __name__ == "__main__":
    puzzle_input = (pathlib.Path(__file__).parent / "day_1_input.txt").read_text().strip()
    part1_solution, part2_solution = solve(puzzle_input)
    print(f"day_1\npart_1: {part1_solution}\npart_2: {part2_solution}")  # noqa: T201
