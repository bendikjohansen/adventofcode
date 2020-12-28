from aoc.utils import get_input
from typing import Tuple, List

Instriction = Tuple[str, int]
Instructions = List[Tuple[str, int]]


def parse_instructions(all_instructions: str) -> Instriction:
    return [(ins.split()[0], int(ins.split()[1]))
            for ins in all_instructions.splitlines()]


def find_loop(instructions: Instructions, index: int = 0,
              indices: List[int] = []) -> int:
    if index in indices:
        return 0

    updated_indices = indices + [index]
    operation, arg = instructions[index]
    if operation == 'acc':
        return find_loop(instructions, index + 1, updated_indices) + arg
    if operation == 'jmp':
        return find_loop(instructions, index + arg, updated_indices)

    return find_loop(instructions, index + 1, updated_indices)


def solve_part_one(all_instructions: str) -> int:
    instructions = parse_instructions(all_instructions)
    return find_loop(instructions, 0)


if __name__ == "__main__":
    all_instructions = get_input(2020, 8)
    result = solve_part_one(all_instructions)
    print(result)
