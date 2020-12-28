from aoc.utils import get_input
from functools import reduce


def find_loop_size(key: int, subject_number: int) -> int:
    result, loop = 1, 0
    while result != key:
        result = (result * subject_number) % 20201227
        loop += 1
    return loop


def calculate_encryption(key: int, loop_size: int) -> int:
    return reduce(lambda x, y: (x * 7) % 20201227, range(loop_size), 1)


def solve_part_one(public_keys_raw: str) -> int:
    card_key, door_key = tuple(map(int, public_keys_raw.splitlines()))
    card_loop_size = find_loop_size(card_key, 7)
    encryption_key = calculate_encryption(door_key, card_loop_size)
    return encryption_key


if __name__ == "__main__":
    public_keys_raw = get_input(2020, 25)
    result = solve_part_one(public_keys_raw)
    print(result)
