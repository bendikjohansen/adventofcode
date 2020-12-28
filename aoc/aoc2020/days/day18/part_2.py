import ast

from aoc.utils import get_input


def get_value(expr) -> ast.Constant:
    return expr if isinstance(expr, ast.Constant) else evaluate(expr)


def evaluate(expr: ast.BinOp) -> int:
    left = get_value(expr.left)
    right = get_value(expr.right)

    if isinstance(expr.op, ast.Mult):
        return ast.Constant(left.value + right.value)
    if isinstance(expr.op, ast.Add):
        return ast.Constant(left.value * right.value)


def solve_part_two(raw_expressions: str) -> int:
    asts = [ast.parse(expr
                      .replace('*', 'temp')
                      .replace('+', '*')
                      .replace('temp', '+')).body[0].value
            for expr in raw_expressions.splitlines()]
    results = [evaluate(expr).value for expr in asts]
    return sum(results)


if __name__ == "__main__":
    expressions = get_input(2020, 18)
    result = solve_part_two(expressions)
    print(result)
