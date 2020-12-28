from aoc.utils import get_input
from typing import List


def new_seat(current: str, occupied: int) -> str:
    if current == 'L' and occupied == 0:
        return '#'
    if current == '#' and occupied >= 4:
        return 'L'
    return current


def apply_rule_for(grid: List[List[str]], x: int, y: int) -> str:
    height, width = len(grid), len(grid[y])
    x_range = range(max(0, x-1), min(width, x+2))
    y_range = range(max(0, y-1), min(height, y+2))
    adjacent = ''.join([''.join((grid[yi][xi]))
                        for yi in y_range for xi in x_range
                        if not (x == xi and y == yi)])

    occupied = adjacent.count('#')
    return new_seat(grid[y][x], occupied)


def apply_rules(prev_grid: List[List[str]]) -> List[List[str]]:
    new_grid = [list(row) for row in prev_grid]

    for y in range(len(prev_grid)):
        for x in range(len(prev_grid[y])):
            new_grid[y][x] = apply_rule_for(prev_grid, x, y)
    return new_grid


def solve_part_one(grid: List[List[str]]) -> int:
    new_grid = [list(row) for row in grid]
    all_grids = []

    while new_grid not in all_grids:
        all_grids.append(new_grid)
        new_grid = apply_rules(new_grid)

    grid_str = ''.join([''.join(row) for row in all_grids[-1]])

    return grid_str.count('#')


if __name__ == "__main__":
    grid = [[pos for pos in row] for row in get_input(2020, 11).splitlines()]
    result = solve_part_one(grid)
    print(result)
