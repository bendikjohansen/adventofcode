from aoc.utils import get_input


def is_password_valid(i: int, j: int, character: str, pwd: str):
    i_match = pwd[i - 1] == character
    j_match = pwd[j - 1] == character
    return i_match != j_match


def extract_parts(line: str) -> (int, int, str, str):
    min_occurences = int(line.split('-')[0])
    max_occurences = int(line[line.index('-') + 1:line.index(' ')])
    character = line[line.index(' ') + 1]
    password = line[line.rfind(' ') + 1:]

    return min_occurences, max_occurences, character, password


def solve_part_two(password_policies: str) -> int:
    lines = password_policies.splitlines()

    valid_password_count = 0
    for line in lines:
        min_occ, max_occ, character, password = extract_parts(line)
        is_valid = is_password_valid(min_occ, max_occ, character, password)
        if is_valid:
            valid_password_count += 1

    return valid_password_count


if __name__ == "__main__":
    password_policies = get_input(2020, 2)
    result = solve_part_two(password_policies)
    print(result)
