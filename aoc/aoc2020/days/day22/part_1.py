from collections import deque
from typing import Deque, Tuple

from aoc.utils import get_input

Deck = Deque[str]
Decks = Tuple[Deck, Deck]


def parse_deck(deck_raw: str) -> Deck:
    return deque([int(value) for value in deck_raw.splitlines()[1:]])


def parse_decks(decks_raw: str) -> Decks:
    [first_deck, second_deck] = decks_raw.split('\n\n')
    return parse_deck(first_deck), parse_deck(second_deck)


def play_round(first_deck: Deck, second_deck: Deck) -> Decks:
    first = first_deck.popleft()
    second = second_deck.popleft()

    if first > second:
        first_deck.extend([first, second])
    if second > first:
        second_deck.extend([second, first])

    return first_deck, second_deck


def play_rounds(first: Deck, second: Deck) -> Deck:
    first_deck, second_deck = deque(first), deque(second)
    while first_deck and second_deck:
        first_deck, second_deck = play_round(first_deck, second_deck)

    return first_deck if first_deck else second_deck


def solve_part_one(decks_raw: str) -> int:
    first_deck, second_deck = parse_decks(decks_raw)
    winner_deck = play_rounds(first_deck, second_deck)
    winner_deck.reverse()
    return sum([(index + 1) * number
                for index, number in enumerate(winner_deck)])


if __name__ == "__main__":
    decks_raw = get_input(2020, 22)
    result = solve_part_one(decks_raw)
    print(result)
