from aoc.utils import get_input
from typing import List


def count_valid_permutations(jolts: List[int]) -> int:
    reachable_list = []
    for i, jolt in enumerate(jolts):
        reachable = [j for j in jolts[i + 1:] if j - jolt <= 3]
        reachable_list.append(reachable)

    arrangement_list = [1] + [0] * (len(jolts) - 1)
    for i, jolt in enumerate(jolts[1:]):
        index = i + 1
        arrangements = 0
        for i in range(1, 4):
            if jolt in reachable_list[index - i]:
                arrangements += arrangement_list[index - i]
        arrangement_list[index] = arrangements

    return arrangement_list[-1]


def solve_part_two(jolts_raw: str) -> int:
    jolts = [0] + [int(jolt) for jolt in jolts_raw.splitlines()]
    jolts.sort()
    jolts.append(max(jolts) + 3)
    return count_valid_permutations(jolts)


if __name__ == "__main__":
    jolts_raw = get_input(2020, 10)
    result = solve_part_two(jolts_raw)
    print(result)
