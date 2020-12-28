from aoc.utils import get_input
from typing import List
from functools import reduce


def intersection(lists: List[str]) -> List[str]:
    return reduce(lambda x, y: set(x) & set(y), lists, lists[0])


def solve_part_two(answers_raw: str) -> int:
    answers = [[[answer for answer in answers]
                for answers in group.splitlines()]
               for group in answers_raw.split('\n\n')]

    return sum([len(intersection(group)) for group in answers])


if __name__ == "__main__":
    answers_raw = get_input(2020, 6)
    result = solve_part_two(answers_raw)
    print(result)
