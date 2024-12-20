import pathlib

import pytest

from advent_of_code_2024 import day_2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> str:
    puzzle_input = (PUZZLE_DIR / "day_2_example_1.txt").read_text().strip()
    return day_2.parse(puzzle_input)


@pytest.fixture
def example2() -> str:
    puzzle_input = (PUZZLE_DIR / "day_2_example_2.txt").read_text().strip()
    return day_2.parse(puzzle_input)


def test_part1_example1(example1: str) -> None:
    """Test part 1 on example input."""
    assert day_2.part1(example1) == 2


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2: str) -> None:
    """Test part 2 on example input."""
    assert day_2.part2(example2) == ...
