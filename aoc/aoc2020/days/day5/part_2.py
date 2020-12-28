from aoc.utils import get_input
from aoc.aoc2020.days.day5.part_1 import parse_seat, \
    find_seat_id
from typing import Set


def is_vacant(id: int, seats: Set[int]):
    return id not in seats and id - 1 in seats and id + 1 in seats


def solve_part_two(all_seats: str) -> int:
    seats = [parse_seat(seat) for seat in all_seats.splitlines()]
    seat_ids = set([find_seat_id(seat) for seat in seats])
    result = [x for x in range(0, 1024) if is_vacant(x, seat_ids)]
    return result[0]


if __name__ == "__main__":
    all_seats = get_input(2020, 5)
    result = solve_part_two(all_seats)
    print(result)
