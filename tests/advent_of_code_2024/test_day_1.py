import pathlib

import pytest

from advent_of_code_2024 import day_1

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> tuple[list[int], list[int]]:
    puzzle_input = (PUZZLE_DIR / "day_1_example_1.txt").read_text().strip()
    return day_1.parse(puzzle_input)


@pytest.fixture
def example2() -> tuple[list[int], list[int]]:
    puzzle_input = (PUZZLE_DIR / "day_1_example_2.txt").read_text().strip()
    return day_1.parse(puzzle_input)


def test_part1_example1(example1: tuple[list[int], list[int]]) -> None:
    """Test part 1 on example input."""
    assert day_1.part1(*example1) == 11


def test_part2_example2(example2: tuple[list[int], list[int]]) -> None:
    """Test part 2 on example input."""
    assert day_1.part2(*example2) == 31
