from aoc.utils import get_input
from collections import deque


def solve_part_one(numbers_raw: str) -> int:
    parsed_nums = [int(n) for n in numbers_raw.split(',')][::-1]
    numbers = deque(parsed_nums)
    prev_queue = deque(parsed_nums[1:])

    for turn in range(len(numbers), 2020):
        new_number = 0
        if numbers[0] in prev_queue:
            new_number = prev_queue.index(numbers[0]) + 1
        prev_queue.appendleft(numbers[0])
        numbers.appendleft(new_number)

    return numbers[0]


if __name__ == "__main__":
    numbers = get_input(2020, 15)
    result = solve_part_one(numbers)
    print(result)
