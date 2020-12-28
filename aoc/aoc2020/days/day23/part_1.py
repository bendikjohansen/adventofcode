from typing import Dict, List, Tuple
from functools import reduce

from aoc.utils import get_input


class LinkedListNode:
    def __init__(self, value):
        self.value: int = value
        self.left: str = None
        self.right: str = None

    def __str__(self):
        return self.value

    def __eq__(self, value):
        return self.value == value


LabelMap = Dict[int, LinkedListNode]
LabelSlice = Tuple[LinkedListNode, LinkedListNode]


def parse_labeling(numbers: List[int]) -> Tuple[LabelMap, LinkedListNode]:
    label_map = {}
    prev = LinkedListNode('\0')
    for value in numbers:
        node = LinkedListNode(value)
        node.left = prev
        prev.right = node
        label_map[value] = prev = node
    first, last = label_map[numbers[0]], label_map[numbers[-1]]
    first.left, last.right = last, first
    return label_map, first


def extend_labeling(cup_labeling: str, number_limit: int) -> List[int]:
    labels = [int(label) for label in cup_labeling]
    return labels + list(range(len(labels) + 1, number_limit + 1))


def get_slice(current: LinkedListNode) -> LabelSlice:
    slice_start = current.right
    current.right = slice_start.right.right.right
    current.right.left = current
    return slice_start, slice_start.right.right


def list_to_str(node: LinkedListNode):
    to_str = ''
    n = node.right
    while n != node:
        to_str += str(n.value)
        n = n.right
    return to_str


def solve_part_one(cup_labeling: str) -> int:
    labels_raw = extend_labeling(cup_labeling, 0)
    label_map, current = parse_labeling(labels_raw)

    for _ in range(100):
        slice_start, slice_end = get_slice(current)
        slice_list = [slice_start, slice_end.left, slice_end]

        dest_pos = current.value - 1 if current.value > 1 else len(label_map)
        while label_map[dest_pos] in slice_list:
            dest_pos -= 1
            if dest_pos == 0:
                dest_pos = len(label_map)
        dest = label_map[dest_pos]

        dest.right.left, slice_end.right = slice_end, dest.right
        dest.right, slice_start.left = slice_start, dest
        current = current.right

    return list_to_str(label_map[1])


if __name__ == "__main__":
    cup_labeling = get_input(2020, 23)
    result = solve_part_one(cup_labeling)
    print(result)
