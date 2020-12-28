from aoc.utils import get_input


def solve_part_one(answers_raw: str) -> int:
    return sum([len(set([answer
                         for indiviual in groups.splitlines()
                         for answer in indiviual]))
                for groups in answers_raw.split('\n\n')])


if __name__ == "__main__":
    answers_raw = get_input(2020, 6)
    result = solve_part_one(answers_raw)
    print(result)
