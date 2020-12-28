from aoc.utils import get_input


def solve_part_one(init_program: str) -> int:
    mask = ''
    memory = {}
    for line in init_program.splitlines():
        if line.startswith('mask'):
            mask = line[7:]
        else:
            address = int(line[4:line.index(']')])
            value = int(line[line.index('=') + 1:])
            binary_value = str(bin(value)[2:])
            padded_binary_value = '0' * \
                (len(mask) - len(binary_value)) + binary_value
            after_merge = [a if a != 'X' else b for a,
                           b in zip(mask, padded_binary_value)]
            final_value = int('0b' + ''.join(after_merge), 2)
            memory[address] = final_value
    return sum(memory.values())


if __name__ == "__main__":
    init_program = get_input(2020, 14)
    result = solve_part_one(init_program)
    print(result)
