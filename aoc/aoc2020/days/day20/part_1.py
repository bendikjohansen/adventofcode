from typing import Dict, List
from collections import defaultdict
from functools import reduce

from aoc.utils import get_input


ImageTile = List[List[bool]]
ImageTiles = Dict[int, List[List[bool]]]


def get_border(tile: ImageTile) -> ImageTile:
    return [
        tile[0],
        tile[-1],
        ''.join([tile[y][0] for y in range(len(tile))]),
        ''.join([tile[y][-1] for y in range(len(tile))]),
        tile[0][::-1],
        tile[-1][::-1],
        ''.join([tile[y][0] for y in range(len(tile))])[::-1],
        ''.join([tile[y][-1] for y in range(len(tile))])[::-1],
    ]


def get_border_variants(tiles: ImageTiles):
    return {id: get_border(tile) for id, tile in tiles.items()}


def parse_to_dict(camera_array: str) -> ImageTile:
    return {int(tile.splitlines()[0].split()[1][:-1]):
            [line
             for line in tile.splitlines()[1:]]
            for tile in camera_array.split('\n\n')}


def solve_part_one(camera_array):
    micro_images = parse_to_dict(camera_array)
    borders_map = get_border_variants(micro_images)

    border_count = defaultdict(lambda: set())
    for id, borders in borders_map.items():
        for border in borders:
            border_count[border].add(id)

    singles = {key: value
               for key, value in border_count.items()
               if len(value) == 1}
    sides = [side for sides in singles.values() for side in sides]
    corners = set([side for side in sides if sides.count(side) == 4])
    return reduce(lambda x, y: x * y, corners, 1)


if __name__ == "__main__":
    camera_array = get_input(2020, 20)
    result = solve_part_one(camera_array)
    print(result)
