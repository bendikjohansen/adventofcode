from collections import defaultdict
from typing import Tuple

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


def matches(rule, message: str) -> Tuple[bool, str]:
    if rule['value']:
        return message.startswith(rule['value']), message[1:]

    for rules in rule['ruleset']:
        current_message, was_match = message, True
        for n_rule in rules:
            is_match, current_message = matches(n_rule, current_message)
            was_match = was_match and is_match

        if was_match:
            return True, current_message

    return False, message


def strictly_matches(rule, message: str) -> bool:
    is_match, rest = matches(rule, message)

    return is_match and not rest


def solve_part_one(rules_and_messages: str) -> int:
    [rules_raw, messages_raw] = rules_and_messages.split('\n\n')
    rules = parse_rules(rules_raw)
    messages = messages_raw.splitlines()

    return sum([1 for msg in messages if strictly_matches(rules[0], msg)])


if __name__ == "__main__":
    rules_and_messages = get_input(2020, 19)
    result = solve_part_one(rules_and_messages)
    print(result)
