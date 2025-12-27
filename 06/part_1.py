import math
import sys


def solve():
    tokens = (line.split() for line in sys.stdin.readlines())
    expressions = list(zip(*tokens))
    grand_sum = 0

    for expression in expressions:
        *raw_operands, operator = expression
        operands = (int(operand) for operand in raw_operands)

        if operator == '*':
            grand_sum += math.prod(operands)
        elif operator == '+':
            grand_sum += sum(operands)
        else:
            raise ValueError(f'Unexpected operator: "{operator}"')

    print(grand_sum)

solve()