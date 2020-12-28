from aoc.utils import get_input


def solve_part_one(input: str) -> int:
    numbers = list(map(int, input.splitlines()))
    expected_sum = 2020
    traversed_numbers = set()

    for number in numbers:
        required_number = expected_sum - number
        if required_number in traversed_numbers:
            return required_number * number
        else:
            traversed_numbers.add(number)

    raise Exception(f'No two numbers add up to {expected_sum}.')


if __name__ == "__main__":
    expense_report = get_input(2020, 1)
    result = solve_part_one(expense_report)
    print(result)
