from collections import deque
from itertools import islice

from aoc.aoc2020.days.day22.part_1 import Deck, parse_decks
from aoc.utils import get_input


def play_round(first: Deck, second: Deck) -> int:
    history = []
    while first and second:
        if (first, second) in history:
            return 1
        history.append((deque(first), deque(second)))

        top_first, top_second = first.popleft(), second.popleft()
        if len(first) >= top_first and len(second) >= top_second:
            first_deck = deque(islice(first, top_first))
            second_deck = deque(islice(second, top_second))
            winner = play_round(first_deck, second_deck)
        else:
            winner = 1 if top_first > top_second else 2

        if winner == 1:
            first.extend([top_first, top_second])
        else:
            second.extend([top_second, top_first])
    return 1 if first else 2


def solve_part_two(decks_raw: str) -> int:
    first, second = parse_decks(decks_raw)
    winner = first if play_round(first, second) == 1 else second
    winner.reverse()

    return sum([(index + 1) * value for index, value in enumerate(winner)])


if __name__ == "__main__":
    decks_raw = get_input(2020, 22)
    result = solve_part_two(decks_raw)
    print(result)
