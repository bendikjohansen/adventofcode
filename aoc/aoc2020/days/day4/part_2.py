from aoc.utils import get_input
from aoc.aoc2020.days.day4.part_1 \
    import parse_passport_batch


def validate_height(height: str) -> bool:
    return len(height) >= 4 and \
        height[-2:] == 'cm' and 150 <= int(height[:-2]) <= 193 or \
        height[-2:] == 'in' and 59 <= int(height[:-2]) <= 76


def validate_hair_color(hair_color: str) -> bool:
    return len(hair_color) == 7 and hair_color[0] == '#' \
        and 0 <= int(hair_color[1:], 16) <= 256 ** 3


def validations(passport):
    return [
        1920 <= int(passport['byr']) <= 2002,
        2010 <= int(passport['iyr']) <= 2020,
        2020 <= int(passport['eyr']) <= 2030,
        validate_height(passport['hgt']),
        validate_hair_color(passport['hcl']),
        passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        len(passport['pid']) == 9,
    ]


def is_valid_passport(passport) -> bool:
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    in_passport = map(lambda field: field in passport, required)
    return all(in_passport) and all(validations(passport))


def solve_part_two(passport_batch: str) -> int:
    passports = parse_passport_batch(passport_batch)
    valid_passports = list(filter(is_valid_passport, passports))
    return len(valid_passports)


if __name__ == "__main__":
    passports = get_input(2020, 4)
    result = solve_part_two(passports)
    print(result)
