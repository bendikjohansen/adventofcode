from aoc.utils import get_input
from functools import reduce
from typing import List


def get_trees_hit(tree_map: List[List[bool]], x: int, y: int):
    x_range = range(0, len(tree_map[0]) * int(len(tree_map) / y), x)
    y_range = range(0, len(tree_map), y)
    trajectory = zip(x_range, y_range)
    trees_hit = sum([tree_map[y][x % len(tree_map[0])] for x, y in trajectory])
    return trees_hit


def solve_part_two(tree_map_raw: str) -> int:
    tree_map = [list(map(lambda x: x == '#', line))
                for line in tree_map_raw.splitlines()]

    velocities = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees_hit = [get_trees_hit(tree_map, vx, vy) for vx, vy in velocities]
    return reduce(lambda x, y: x * y, trees_hit, 1)


if __name__ == "__main__":
    tree_map = get_input(2020, 3)
    result = solve_part_two(tree_map)
    print(result)
