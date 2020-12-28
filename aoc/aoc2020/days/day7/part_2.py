from aoc.utils import get_input
from aoc.aoc2020.days.day7.part_1 import parse_rules
from typing import Dict


def count_bags(bag: Dict) -> int:
    total = 0
    for child, amount in bag['children'].values():
        other_bags = count_bags(child)
        total += (other_bags + 1) * amount
    return total


def solve_part_two(all_rules: str) -> int:
    bags = parse_rules(all_rules.splitlines())
    return count_bags(bags['shiny gold'])


if __name__ == "__main__":
    all_rules = get_input(2020, 7)
    result = solve_part_two(all_rules)
    print(result)
