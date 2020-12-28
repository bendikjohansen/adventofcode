from aoc.utils import get_input
from functools import reduce
from typing import Tuple, List, Callable, Dict

Rules = Dict[str, List[Tuple[int, int]]]
IsValid = Callable[[int], bool]


def product(numbers: List[int]) -> int:
    return reduce(lambda x, y: x * y, numbers, 1)


def parse_tickets(tickets_raw: str) -> Tuple[Rules, List[List[int]]]:
    rules_raw, my_ticket, nearby_raw = tickets_raw.split('\n\n')

    rules = {
        rule[:rule.index(':')]:
        [
            (int(rule_min), int(rule_max))
            for rule_min, rule_max in
            [
                (rule[rule.index(':') + 2:rule.index('-')],
                 rule[rule.index('-') + 1:rule.index(' or ')]),
                (rule[rule.rindex(' ') + 1:rule.rindex('-')],
                 rule[rule.rindex('-') + 1:]),
            ]
        ]
        for rule in rules_raw.splitlines()
    }
    ticket = [int(number) for number in my_ticket.splitlines()[1].split(',')]
    nearbies = [[int(number) for number in nearbies.split(',')]
                for nearbies in nearby_raw.splitlines()[1:]]
    return rules, ticket, nearbies


def create_requirements(rules: Rules) -> IsValid:
    return lambda x: any(any([r_min <= x <= r_max for r_min, r_max in bounds])
                         for bounds in rules.values())


def find_valid_tickets(is_valid: IsValid, nearbies: List[List[int]]):
    return [nearby for nearby in nearbies
            if all([is_valid(number) for number in nearby])]


def within_bounds(xs: List[int], bounds: List[Tuple[int, int]]) -> bool:
    return all([any([r_min <= x <= r_max
                     for r_min, r_max in bounds]) for x in xs])


def solve_part_two(tickets_raw: str) -> int:
    rules, my_ticket, nearbies = parse_tickets(tickets_raw)
    is_valid = create_requirements(rules)
    valid_tickets = find_valid_tickets(is_valid, nearbies)

    columns = [[ticket[i] for ticket in valid_tickets]
               for i in range(len(rules))]
    assignables = {rule: [col_index
                          for col_index, numbers in enumerate(columns)
                          if within_bounds(numbers, bounds)]
                   for rule, bounds in rules.items()}

    field_index_map = {}
    while not all([len(val) == 0 for val in assignables.values()]):
        for rule, col_indices in assignables.items():
            if len(col_indices) == 1:
                i = col_indices[0]
                field_index_map[rule] = i
                assignables = {key: [v for v in val if v != i]
                               for key, val in assignables.items()}
    departures = [index for key, index in field_index_map.items()
                  if key.startswith('departure')]

    return product([my_ticket[i] for i in departures])


if __name__ == "__main__":
    tickets = get_input(2020, 16)
    result = solve_part_two(tickets)
    print(result)
