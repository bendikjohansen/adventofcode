from collections import namedtuple
from typing import Tuple

from aoc.utils import get_input

Position = namedtuple('Position', ['x', 'y'])
Instruction = Tuple[str, int]


def move(instruction: Instruction, prev_pos: Position,
         prev_waypoint_pos: Position) -> Tuple[Position, Position]:
    action, value = instruction

    wpx, wpy = prev_waypoint_pos
    pos = prev_pos
    if action == 'N':
        wpy += value
    elif action == 'E':
        wpx += value
    elif action == 'S':
        wpy -= value
    elif action == 'W':
        wpx -= value
    elif action == 'L':
        for _ in range(int(value / 90)):
            wpx, wpy = -wpy, wpx
    elif action == 'R':
        for _ in range(int(value / 90)):
            wpx, wpy = wpy, -wpx
    elif action == 'F':
        vx = value * wpx
        vy = value * wpy
        pos = Position(x=pos.x + vx, y=pos.y + vy)

    waypoint_pos = Position(x=wpx, y=wpy)
    return pos, waypoint_pos


def solve_part_two(instructions_raw: str) -> int:
    instructions = [(ins[0], int(ins[1:]))
                    for ins in instructions_raw.splitlines()]

    position = Position(x=0, y=0)
    waypoint = Position(x=10, y=1)
    for instruction in instructions:
        position, waypoint = move(instruction, position, waypoint)

    return abs(position.x) + abs(position.y)


if __name__ == "__main__":
    instructions = get_input(2020, 12)
    result = solve_part_two(instructions)
    print(result)
