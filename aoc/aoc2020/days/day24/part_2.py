from collections import Counter
from operator import add
from copy import deepcopy
from typing import Counter as CounterType

from aoc.aoc2020.days.day24.part_1 import read_positions, Position
from aoc.utils import get_input


PositionCount = CounterType[Position]


def adjacent_positions(position: Position):
    relative_coords = [(-0.5, -1), (0.5, -1), (-1, 0),
                       (1, 0), (-0.5, 1), (0.5, 1)]
    return [tuple(map(add, coord, position)) for coord in relative_coords]


def get_relevant_positions(position_map: PositionCount):
    coord_generator = map(adjacent_positions, position_map.keys())
    return [coord for coord_list in list(coord_generator)
            for coord in coord_list]


def count_black_neighbors(position_map: PositionCount) -> PositionCount:
    black_tiles = [pos for pos, count in position_map.items()
                   if count % 2 == 1]
    neighbors = [position
                 for black_tile_position in black_tiles
                 for position in adjacent_positions(black_tile_position)]
    return Counter(neighbors)


def flip_tiles(prev_position_map: CounterType[Position]):
    black_neighbor_count = count_black_neighbors(prev_position_map)
    position_map = deepcopy(prev_position_map)

    test = set(position_map.keys()).union(set(black_neighbor_count.keys()))
    for position in test:
        value = position_map[position]
        c = black_neighbor_count[position]
        is_black = value % 2 == 1
        flip_to_white = is_black and (c > 2 or c == 0)
        flip_to_black = not is_black and c == 2
        if flip_to_black or flip_to_white:
            position_map[position] += 1

    return position_map


def solve_part_two(instructions: str) -> int:
    positions = read_positions(instructions)
    position_map = Counter(positions)

    for day in range(100):
        position_map = flip_tiles(position_map)

    return len([flips for flips in position_map.values() if flips % 2 == 1])


if __name__ == "__main__":
    instructions = get_input(2020, 24)
    result = solve_part_two(instructions)
    print(result)
