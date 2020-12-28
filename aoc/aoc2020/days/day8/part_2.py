from aoc.utils import get_input
from typing import List
from aoc.aoc2020.days.day8.part_1 import \
    parse_instructions, Instructions


def find_loop(instructions: Instructions, index: int = 0,
              indices: List[int] = []) -> int:
    if index in indices:
        return indices

    updated_indices = indices + [index]
    operation, arg = instructions[index]
    if operation == 'acc':
        return find_loop(instructions, index + 1, updated_indices)
    if operation == 'jmp':
        return find_loop(instructions, index + arg, updated_indices)

    return find_loop(instructions, index + 1, updated_indices)


def swap_nop_acc(instructions: Instructions, index: int) -> Instructions:
    op, arg = instructions[index]
    if op == 'nop':
        instructions[index] = ('jmp', arg)
    elif op == 'jmp':
        instructions[index] = ('nop', arg)
    return instructions


def execute(instructions: Instructions, index: int = 0,
            indices: List[int] = []) -> int:
    if index in indices:
        return False
    if index not in range(len(instructions)):
        return 0

    updated_indices = indices + [index]
    operation, arg = instructions[index]
    if operation == 'acc':
        result = execute(instructions, index + 1, updated_indices)
        return result + arg if result is not False else False
    if operation == 'jmp':
        return execute(instructions, index + arg, updated_indices)

    return execute(instructions, index + 1, updated_indices)


def find_terminal_path(instructions):
    loop_indices = find_loop(instructions)
    instruction_sets = [swap_nop_acc(list(instructions), index)
                        for index in loop_indices]
    results = [execute(instructions) for instructions in instruction_sets]
    return next(filter(lambda x: x is not False, results))


def solve_part_two(all_instructions: str) -> int:
    instructions = parse_instructions(all_instructions)
    return find_terminal_path(instructions)


if __name__ == "__main__":
    all_instructions = get_input(2020, 8)
    result = solve_part_two(all_instructions)
    print(result)
