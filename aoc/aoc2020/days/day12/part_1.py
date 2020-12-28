from collections import namedtuple
from typing import Tuple

from aoc.utils import get_input

Position = namedtuple('Position', ['x', 'y'])
Instruction = Tuple[str, int]
directions = ['North', 'East', 'South', 'West']


def move(instruction: Instruction, prev_position: Position,
         prev_facing: str) -> Tuple[Position, str]:
    action, value = instruction

    facing = prev_facing
    x, y = prev_position
    if action == 'N':
        y += value
    elif action == 'E':
        x += value
    elif action == 'S':
        y -= value
    elif action == 'W':
        x -= value
    elif action == 'L':
        turns = int(value / 90)
        facing = directions[directions.index(prev_facing) - turns]
    elif action == 'R':
        turns = int(value / 90)
        index = (directions.index(prev_facing) + turns) % len(directions)
        facing = directions[index]
    elif action == 'F':
        (x, y), _ = move((facing[0], value), prev_position, facing)

    position = Position(x=x, y=y)
    return position, facing


def solve_part_one(instructions_raw: str) -> int:
    instructions = [(ins[0], int(ins[1:]))
                    for ins in instructions_raw.splitlines()]

    position = Position(x=0, y=0)
    facing = 'East'
    for instruction in instructions:
        position, facing = move(instruction, position, facing)

    return abs(position.x) + abs(position.y)


if __name__ == "__main__":
    instructions = get_input(2020, 12)
    result = solve_part_one(instructions)
    print(result)
