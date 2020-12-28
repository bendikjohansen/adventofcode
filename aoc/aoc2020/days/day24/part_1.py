from collections import Counter
from typing import List, Tuple

from aoc.utils import get_input

Position = Tuple[float, float]
Positions = List[Position]


def read_position(instructions: str) -> Position:
    nws, nes = instructions.count('nw'), instructions.count('ne')
    sws, ses = instructions.count('sw'), instructions.count('se')
    ws = instructions.count('w') - sws - nws
    es = instructions.count('e') - ses - nes
    x = es + (nes + ses) / 2 - ws - (nws + sws) / 2
    y = nws + nes - sws - ses
    return (x, y)


def read_positions(instructions: List[str]) -> Positions:
    return map(read_position, instructions.splitlines())


def solve_part_one(instructions: str) -> int:
    positions = read_positions(instructions)
    position_map = Counter(positions)
    return len([flips for flips in position_map.values() if flips % 2 == 1])


if __name__ == "__main__":
    instructions = get_input(2020, 24)
    result = solve_part_one(instructions)
    print(result)
