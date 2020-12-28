from aoc.utils import get_input
from typing import List


def create_equation(id, offset):
    def equation(n):
        print(f'n + {offset} mod {id} = 0')
        return (n + offset) % id == 0
    return equation


def index_offsets(ids: List[int]) -> int:
    offsets = [0]
    for id in ids:
        if id == 0:
            offsets[-1] += 1
        else:
            offsets.append(offsets[-1] + 1)
    return offsets[:-1]


def solve_part_two(info: str) -> int:
    departures = [0 if id == 'x' else int(id)
                  for id in info.splitlines()[1].split(',')]
    ids = [id for id in departures if id != 0]
    offsets = index_offsets(departures)
    print(list(zip(ids, offsets)))

    equations = [create_equation(id, offset)
                 for id, offset in zip(ids, offsets)]

    return [e(3417) for e in equations]


if __name__ == "__main__":
    departure_info = get_input(2020, 13)
    result = solve_part_two(departure_info)
    print(result)
