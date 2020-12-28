from typing import Set

from aoc.aoc2020.days.day21.part_1 import AllergenMap, parse_food
from aoc.utils import get_input


def find_unsafe_ingredients(allergen_map: AllergenMap) -> Set[str]:
    by_allergen = {}
    for allergens, ingredients in allergen_map:
        for allergen in allergens:
            if allergen not in by_allergen:
                by_allergen[allergen] = set(ingredients)
            else:
                by_allergen[allergen].intersection_update(ingredients)
    return {key: list(value) for key, value in by_allergen.items()}


def solve_part_two(ingredients_raw: str) -> int:
    allergen_map = [parse_food(food) for food in ingredients_raw.splitlines()]
    unsafe = find_unsafe_ingredients(allergen_map)

    for i in range(len(unsafe)):
        for allergen, ingredients in unsafe.items():
            if len(ingredients) == 1:
                ing = ingredients[0]
                for allergen_t, ingredients_t in unsafe.items():
                    if allergen_t != allergen and ing in ingredients_t:
                        ingredients_t.remove(ing)
    allergen_list = [(allergen, ingredients[0])
                     for allergen, ingredients in unsafe.items()]
    allergen_list.sort(key=lambda x: x[0])
    cdil = ','.join(x[1] for x in allergen_list)

    return cdil


if __name__ == "__main__":
    ingredients_raw = get_input(2020, 21)
    result = solve_part_two(ingredients_raw)
    print(result)
