from aoc.utils import get_input
from aoc.aoc2020.days.day9.part_1 import solve_part_one
from typing import List


def numbers_cont_sum(weak_number: int, numbers: List[int]):
    cont_numbers_list = []

    for number in numbers:
        new_cont = [cont_nums + [number]
                    for cont_nums in cont_numbers_list
                    if sum(cont_nums) + number <= weak_number]
        cont_numbers_list = new_cont + [[number]]
        for cont_nums in new_cont:
            if sum(cont_nums) == weak_number:
                return cont_nums

    return cont_numbers_list


def solve_part_two(numbers_raw: str, preamble: int) -> int:
    weak_number = solve_part_one(numbers_raw, preamble)
    numbers = [int(number) for number in numbers_raw.splitlines()]
    numbers_before = numbers[:numbers.index(weak_number)]
    cont_num_sum = numbers_cont_sum(weak_number, numbers_before)
    return min(cont_num_sum) + max(cont_num_sum)


if __name__ == "__main__":
    numbers_raw = get_input(2020, 9)
    result = solve_part_two(numbers_raw, 25)
    print(result)
