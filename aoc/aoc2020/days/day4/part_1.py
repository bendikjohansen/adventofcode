from aoc.utils import get_input


def parse_passport(passport_raw: str):
    entries = map(lambda entry: entry.split(':'), passport_raw.split())
    return {key: value for [key, value] in entries}


def parse_passport_batch(passport_batch: str):
    passports_raw = passport_batch.split('\n\n')
    return map(parse_passport, passports_raw)


def is_valid_passport(passport) -> bool:
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    in_passport = map(lambda field: field in passport, required)
    return all(in_passport)


def solve_part_one(passport_batch: str) -> int:
    passports = parse_passport_batch(passport_batch)
    valid_passports = list(filter(is_valid_passport, passports))
    return len(valid_passports)


if __name__ == "__main__":
    passports = get_input(2020, 4)
    result = solve_part_one(passports)
    print(result)
