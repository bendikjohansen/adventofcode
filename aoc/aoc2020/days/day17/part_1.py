from collections import defaultdict
from copy import deepcopy
from typing import DefaultDict, List, Tuple

from aoc.utils import get_input

Pocket = DefaultDict[int, DefaultDict[int, DefaultDict[int, bool]]]
Point = Tuple[int, int, int]
Coords = List[Point]
CoordCount = DefaultDict[Point, int]


def parse(initial_state: str) -> Pocket:
    pocket = defaultdict(lambda: defaultdict(
        lambda: defaultdict(lambda: False)))

    initial_coords = [(x, y)
                      for y, row in enumerate(initial_state.splitlines())
                      for x, cube in enumerate(row)
                      if cube == '#']
    for (x, y) in initial_coords:
        pocket[0][y][x] = True
    return pocket


def find_active_points(pocket: Pocket) -> Coords:
    return [(x, y, z)
            for z, plane in pocket.items()
            for y, row in plane.items()
            for x, cube_is_active in row.items()
            if cube_is_active]


def find_neighbors(cube: Point) -> Coords:
    x, y, z = cube
    neighbors = [
        (xi, yi, zi)
        for xi in range(x - 1, x + 2)
        for yi in range(y - 1, y + 2)
        for zi in range(z - 1, z + 2)
        if (xi, yi, zi) != (x, y, z)
    ]
    return neighbors


def count_neighbors(pocket: Pocket, points: Coords) -> CoordCount:
    neighbors = defaultdict(lambda: 0)
    neighbors.update({point: 0 for point in points})
    for cube in points:
        all_neighbors = find_neighbors(cube)
        for point in all_neighbors:
            neighbors[point] += 1
    return neighbors


def change_states(pocket: Pocket, active_points: Coords,
                  active_neighbor_count: CoordCount) -> Pocket:
    new_pocket = deepcopy(pocket)
    for (x, y, z), count in active_neighbor_count.items():
        stay_active = pocket[z][y][x] and count in [2, 3]
        become_active = not pocket[z][y][x] and count == 3
        new_pocket[z][y][x] = stay_active or become_active
    return new_pocket


def solve_part_one(initial_state: str) -> int:
    pocket = parse(initial_state)

    for cycles in range(6):
        active_points = find_active_points(pocket)
        active_neighbors_count = count_neighbors(pocket, active_points)
        pocket = change_states(pocket, active_points, active_neighbors_count)
    return len(find_active_points(pocket))


if __name__ == "__main__":
    initial_state = get_input(2020, 17)
    result = solve_part_one(initial_state)
    print(result)
