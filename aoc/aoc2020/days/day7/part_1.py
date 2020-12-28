from aoc.utils import get_input
from typing import List, Dict


def get_child(parts: List[str]):
    amount = int(parts[0])
    bag_key = bag_key = ' '.join(parts[1:3])

    return (bag_key, amount)


def get_children(parts: List[str]):
    has_children = parts[4].isnumeric()
    if not has_children:
        return []

    return [get_child(parts[i:i + 3]) for i in range(4, len(parts[4:]) + 1, 4)]


def parse_rule(rule: str):
    parts = rule.split()
    bag_key = ' '.join(parts[0:2])
    children = get_children(parts)
    return (bag_key, children)


def parse_rules(rules: List[str]):
    bags = {}
    for rule in rules:
        key, children = parse_rule(rule)
        bag = bags.get(key, {})

        child_bags = {}
        for child_key, amount in children:
            child_bag = bags.get(child_key, {})
            child_bags[child_key] = (child_bag, amount)
            bags[child_key] = child_bag
        bag['children'] = child_bags
        bags[key] = bag
    return bags


def contains(bag: Dict, target: str) -> bool:
    if target in bag['children'].keys():
        return True

    return any([contains(child, target)
                for child, amount in bag['children'].values()])


def solve_part_one(all_rules: str) -> int:
    bags = parse_rules(all_rules.splitlines())
    return len([bag for bag in bags.values() if contains(bag, 'shiny gold')])


if __name__ == "__main__":
    all_rules = get_input(2020, 7)
    result = solve_part_one(all_rules)
    print(result)
