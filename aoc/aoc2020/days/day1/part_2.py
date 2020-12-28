from aoc.utils import get_input
from itertools import permutations


def solve_part_two(input: str) -> int:
    numbers = list(map(int, input.splitlines()))
    expected_sum = 2020
    combinations = permutations(numbers, 3)

    for a, b, c in combinations:
        if a + b + c == expected_sum:
            return a * b * c

    raise Exception(f'No three numbers add up to {expected_sum}.')


if __name__ == "__main__":
    expense_report = get_input(2020, 1)
    result = solve_part_two(expense_report)
    print(result)
