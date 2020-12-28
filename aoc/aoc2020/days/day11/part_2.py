from aoc.utils import get_input
from typing import List


def new_seat(current: str, occupied: int) -> str:
    if current == 'L' and occupied == 0:
        return '#'
    if current == '#' and occupied >= 5:
        return 'L'
    return current


def apply_rule_for(grid: List[List[str]], x: int, y: int) -> str:
    up = ''.join([grid[yi][x] for yi in range(y - 1, -1, -1)])
    down = ''.join([grid[yi][x] for yi in range(y + 1, len(grid))])
    left = ''.join([grid[y][xi] for xi in range(x - 1, -1, -1)])
    right = ''.join([grid[y][xi] for xi in range(x + 1, len(grid[0]))])
    up_right = ''.join([grid[yi][xi] for xi, yi in zip(
        range(x + 1, len(grid[0])),
        range(y - 1, -1, -1)
    )])
    up_left = ''.join([grid[yi][xi] for xi, yi in zip(
        range(x - 1, -1, -1),
        range(y - 1, -1, -1)
    )])
    down_right = ''.join([grid[yi][xi] for xi, yi in zip(
        range(x + 1, len(grid[0])),
        range(y + 1, len(grid))
    )])
    down_left = ''.join([grid[yi][xi] for xi, yi in zip(
        range(x - 1, -1, -1),
        range(y + 1, len(grid))
    )])
    directions = [up, down, left, right,
                  up_right, up_left, down_right, down_left]
    occupied = 0
    for direction in directions:
        for pos in direction:
            if pos == 'L':
                break
            elif pos == '#':
                occupied += 1
                break

    return new_seat(grid[y][x], occupied)


def apply_rules(prev_grid: List[List[str]]) -> List[List[str]]:
    new_grid = [list(row) for row in prev_grid]

    for y in range(len(prev_grid)):
        for x in range(len(prev_grid[y])):
            new_grid[y][x] = apply_rule_for(prev_grid, x, y)
    return new_grid


def solve_part_two(grid: List[List[str]]) -> int:
    new_grid = [list(row) for row in grid]
    all_grids = []

    while new_grid not in all_grids:
        all_grids.append(new_grid)
        new_grid = apply_rules(new_grid)

    grid_str = ''.join([''.join(row) for row in all_grids[-1]])

    return grid_str.count('#')


if __name__ == "__main__":
    grid = [[pos for pos in row] for row in get_input(2020, 11).splitlines()]
    result = solve_part_two(grid)
    print(result)
