from typing import Dict, List, Tuple

from aoc.utils import get_input

Tile = List[str]
Point = Tuple[int, int]
TileMap = Dict[int, Tile]0


def parse_tiles(camera_array: str) -> TileMap:
    return {int(tile.splitlines()[0][5:-1]): tile.splitlines()[1:]
            for tile in camera_array.split('\n\n')}


def rotate(tile: Tile) -> Tile:
    return [''.join([tile[yi][xi]
                     for yi in range(len(tile))])[::-1]
            for xi in range(len(tile[0]))]


def flip(tile: Tile) -> Tile:
    return [line[::-1] for line in tile]


def get_borders(tile: Tile) -> List[str]:
    return [
        tile[0],
        ''.join([tile[yi][0] for yi in range(len(tile))]),
        tile[-1],
        ''.join([tile[yi][-1] for yi in range(len(tile))])
    ]


def get_full_grid(camera_array: str) -> List[List[Tile]]:
    tile_map = parse_tiles(camera_array)
    borders = get_borders(tile_map[1031])

    return borders


def solve_part_two(camera_array: str):
    grid = get_full_grid(camera_array)
    return grid


if __name__ == "__main__":
    camera_array = get_input(2020, 20)
    result = solve_part_two(camera_array)
    print(result)
