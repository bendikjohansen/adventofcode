from aoc.utils import get_input
from typing import List


def has_sum(target: int, numbers: List[int]):
    visited = set()
    for number in numbers:
        if target - number in visited:
            return True
        visited.add(number)
    return False


def solve_part_one(numbers_raw: str, preamble: int) -> int:
    numbers = [int(number) for number in numbers_raw.splitlines()]
    weak_numbers = [numbers[i] for i in range(preamble, len(numbers))
                    if not has_sum(numbers[i], numbers[i - preamble:i])]

    return weak_numbers[0]


if __name__ == "__main__":
    numbers_raw = get_input(2020, 9)
    result = solve_part_one(numbers_raw, 25)
    print(result)
