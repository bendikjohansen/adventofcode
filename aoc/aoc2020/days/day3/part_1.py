from aoc.utils import get_input


def solve_part_one(tree_map_raw: str) -> int:
    tree_map = [list(map(lambda x: x == '#', line))
                for line in tree_map_raw.splitlines()]
    trajectory = zip(range(0, len(tree_map) * 3, 3), range(len(tree_map)))
    trees_hit = sum([tree_map[y][x % len(tree_map[0])] for x, y in trajectory])
    return trees_hit


if __name__ == "__main__":
    tree_map = get_input(2020, 3)
    result = solve_part_one(tree_map)
    print(result)
