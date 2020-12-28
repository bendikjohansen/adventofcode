from typing import List, Set, Tuple

from aoc.utils import get_input

AllergenEntry = Tuple[Set[str], Set[str]]
AllergenMap = List[AllergenEntry]


def parse_food(food: str) -> AllergenEntry:
    ingredients_raw, _, allergens_raw = food.partition(' (contains ')
    ingredients = set(ingredients_raw.split())
    allergens = set(allergens_raw[:-1].split(', '))
    return allergens, ingredients


def find_unsafe_ingredients(allergen_map: AllergenMap) -> Set[str]:
    by_allergen = {}
    for allergens, ingredients in allergen_map:
        for allergen in allergens:
            if allergen not in by_allergen:
                by_allergen[allergen] = set(ingredients)
            else:
                by_allergen[allergen].intersection_update(ingredients)
    return set([ingredient
                for ingredients in by_allergen.values()
                for ingredient in ingredients])


def solve_part_one(ingredients_raw: str) -> int:
    allergen_map = [parse_food(food) for food in ingredients_raw.splitlines()]
    unsafe = find_unsafe_ingredients(allergen_map)
    all_ingredients = [ingredient
                       for _, ingredients in allergen_map
                       for ingredient in ingredients]
    safe = set(all_ingredients).symmetric_difference(unsafe)
    return sum([all_ingredients.count(ingredient) for ingredient in safe])


if __name__ == "__main__":
    ingredients_raw = get_input(2020, 21)
    result = solve_part_one(ingredients_raw)
    print(result)
