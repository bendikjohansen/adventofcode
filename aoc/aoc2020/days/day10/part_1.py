from aoc.utils import get_input
from typing import List


def get_jolt_diffs(jolts: List[int]):
    jolts = [0] + list(jolts)
    jolts.sort()
    jolts.append(jolts[-1] + 3)
    return [jolts[i + 1] - x for i, x in enumerate(jolts[:-1])]


def solve_part_one(jolts_raw: str) -> int:
    jolts = [int(jolt) for jolt in jolts_raw.splitlines()]
    diffs = get_jolt_diffs(jolts)
    return diffs.count(1) * diffs.count(3)


if __name__ == "__main__":
    jolts_raw = get_input(2020, 10)
    result = solve_part_one(jolts_raw)
    print(result)
