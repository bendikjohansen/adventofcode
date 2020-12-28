from aoc.utils import get_input
from collections import deque


def solve_part_two(numbers_raw: str) -> int:
    parsed_nums = [int(n) for n in numbers_raw.split(',')][::-1]
    numbers = deque(parsed_nums)
    lookup = {value: turn + 1 for turn, value in enumerate(parsed_nums[:0:-1])}

    for turn in range(len(numbers), 30000000):
        if turn % 100000 == 0:
            print(turn)
        num_index = lookup.get(numbers[0], -1)
        new_number = 0
        if num_index > 0:
            new_number = turn - num_index

        lookup[numbers[0]] = turn
        numbers.appendleft(new_number)

    return numbers[0]


if __name__ == "__main__":
    numbers = get_input(2020, 15)
    result = solve_part_two(numbers)
    print(result)
