from pathlib import Path


def get_input(year: int, day: int) -> str:
    path = Path()/'aoc'/f'aoc{year}'/'inputs'/f'{day}.txt'

    with open(path, 'r') as file:
        return "".join(file.readlines()).strip()
