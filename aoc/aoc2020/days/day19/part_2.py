from collections import defaultdict
from typing import List, Tuple

from aoc.utils import get_input


def parse_rules(rules_raw: str):
    rules_dict = defaultdict(lambda: {})

    for line in rules_raw.splitlines():
        raw_index, content = line.split(': ')
        index = int(raw_index)
        value = content[1] if content[1] in 'ab' else None
        ruleset = [[rules_dict[int(i)]
                    for i in rule.split()
                    if i.isnumeric()]
                   for rule in content.split('|')]
        rules_dict[index]['value'] = value
        rules_dict[index]['ruleset'] = ruleset
        rules_dict[index]['key'] = index

    return rules_dict


def matches(rule, message: str, depth: int = 0) -> List[Tuple[bool, str]]:
    if depth > 16:
        return [False, message]
    if rule['value']:
        return [(message.startswith(rule['value']), message[1:])]

    match_list = []
    for rules in rule['ruleset']:
        n_matches = [(True, message)]
        for n_rule in rules:
            n_temp = []
            for is_valid, n_message in n_matches:
                if is_valid:
                    n_temp.extend(matches(n_rule, n_message, depth + 1))
            n_matches = n_temp

        match_list.extend(n_matches)

    return list(filter(lambda x: x[0], match_list))


def strictly_matches(rule, message: str) -> bool:
    all_matches = matches(rule, message)
    return any([valid and not rest for valid, rest in all_matches])


def solve_part_two(rules_and_messages: str) -> int:
    [rules_raw, messages_raw] = rules_and_messages.split('\n\n')
    rules_raw += "\n8: 42 | 42 8\n11: 42 31 | 42 11 31"
    rules = parse_rules(rules_raw)
    messages = messages_raw.splitlines()
    return sum([1 for msg in messages if strictly_matches(rules[0], msg)])


if __name__ == "__main__":
    rules_and_messages = get_input(2020, 19)
    result = solve_part_two(rules_and_messages)
    print(result)
