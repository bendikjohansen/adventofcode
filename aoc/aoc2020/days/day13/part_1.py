from aoc.utils import get_input


def solve_part_one(info: str) -> int:
    start = int(info.splitlines()[0])
    departure_ids = [int(id) for id in
                     info.splitlines()[1].split(',') if id != 'x']
    minutes = [(id, id - start % id) for id in departure_ids]
    earliest = min(minutes, key=lambda m: m[1])
    return earliest[0] * earliest[1]


if __name__ == "__main__":
    departure_info = get_input(2020, 13)
    result = solve_part_one(departure_info)
    print(result)
