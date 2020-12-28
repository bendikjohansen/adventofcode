from aoc.utils import get_input
from typing import Tuple, List, Callable

Rules = List[List[Tuple[int]]]
IsValid = Callable[[int], bool]


def parse_tickets(tickets_raw: str) -> Tuple[Rules, List[List[int]]]:
    rules_raw, _, nearby_raw = tickets_raw.split('\n\n')

    rules = [
        (int(rule_min), int(rule_max))
        for rule in rules_raw.splitlines()
        for rule_min, rule_max in
        [
            (rule[rule.index(':') + 2:rule.index('-')],
             rule[rule.index('-') + 1:rule.index(' or ')]),
            (rule[rule.rindex(' ') + 1:rule.rindex('-')],
             rule[rule.rindex('-') + 1:]),
        ]]
    nearbies = [[int(number) for number in nearbies.split(',')]
                for nearbies in nearby_raw.splitlines()[1:]]
    return rules, nearbies


def create_requirements(rules: Rules) -> IsValid:
    return lambda x: any(r_min <= x <= r_max for r_min, r_max in rules)


def invalid_numbers(is_valid: IsValid, nearbies: List[List[int]]):
    invalid_numbers = []
    for nearby in nearbies:
        for number in nearby:
            if not is_valid(number):
                invalid_numbers.append(number)
                break
    return invalid_numbers


def solve_part_one(tickets_raw: str) -> int:
    rules, nearbies = parse_tickets(tickets_raw)
    is_valid = create_requirements(rules)
    numbers = invalid_numbers(is_valid, nearbies)
    return sum(numbers)


if __name__ == "__main__":
    tickets = get_input(2020, 16)
    result = solve_part_one(tickets)
    print(result)
