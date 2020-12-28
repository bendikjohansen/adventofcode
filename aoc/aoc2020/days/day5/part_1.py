from aoc.utils import get_input
from typing import List
from math import ceil


def parse_seat(seat: str) -> (List[bool], List[bool]):
    column_instructions = [x == 'B' for x in seat[:7]]
    row_instructions = [x == 'R' for x in seat[7:]]
    return column_instructions, row_instructions


def find_number(instructions: List[bool], upper: int, lower: int = 0) -> int:
    if upper == lower:
        return lower

    diff = upper - lower
    new_upper = upper if instructions[0] else upper - ceil(diff / 2)
    new_lower = lower + ceil(diff / 2) if instructions[0] else lower
    return find_number(instructions[1:], new_upper, new_lower)


def find_seat_id(seat_instructions: (List[bool], List[bool])) -> int:
    column = find_number(seat_instructions[0], 127)
    row = find_number(seat_instructions[1], 7)
    return column * 8 + row


def solve_part_one(all_seats: str) -> int:
    seats = [parse_seat(seat) for seat in all_seats.splitlines()]
    seat_ids = [find_seat_id(seat) for seat in seats]
    return max(seat_ids)


if __name__ == "__main__":
    all_seats = get_input(2020, 5)
    result = solve_part_one(all_seats)
    print(result)
