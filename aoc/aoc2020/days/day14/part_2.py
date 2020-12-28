from aoc.utils import get_input
from typing import List


def memory_addresses(padded_binary_value: str, mask: str) -> List[int]:
    values = []
    x_indices = [i for i, val in enumerate(mask) if val == 'X']
    for i in range(2**mask.count('X')):
        binary_i = '0' * (len(x_indices) - len(bin(i)[2:])) + bin(i)[2:]
        merged_str = '0b'
        for index, (a, b) in enumerate(zip(mask, padded_binary_value)):
            if index in x_indices:
                merged_str += binary_i[x_indices.index(index)]
            elif a == '1':
                merged_str += a
            else:
                merged_str += b
        final_value = int(merged_str, 2)
        values.append(final_value)
    return values


def solve_part_two(init_program: str) -> int:
    mask = ''
    memory = {}
    for line in init_program.splitlines():
        if line.startswith('mask'):
            mask = line[7:]
        else:
            address = int(line[4:line.index(']')])
            value = int(line[line.index('=') + 1:])
            binary_value = str(bin(address)[2:])
            padded_binary_value = '0' * \
                (len(mask) - len(binary_value)) + binary_value
            addresses = memory_addresses(padded_binary_value, mask)
            for a in addresses:
                memory[a] = value

    return sum(memory.values())


if __name__ == "__main__":
    init_program = get_input(2020, 14)
    result = solve_part_two(init_program)
    print(result)
