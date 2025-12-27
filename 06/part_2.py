import math
import sys


def solve():
    lines = sys.stdin.readlines()

    column_widths = []
    current_column_width = 0

    for c in lines[-1]:
        if c in ['*', '+']:
            if current_column_width > 0:
                column_widths.append(current_column_width)

            current_column_width = 1
        else:
            current_column_width += 1
    column_widths.append(current_column_width)

    expressions = []

    cursor = 0
    for column_width in column_widths:
        operands = []

        for i in range(cursor, cursor + column_width - 1):
            raw_operand = ''

            for j in range(len(lines) - 1):
                raw_operand += lines[j][i]

            operands.append(int(raw_operand))

        expressions.append({
            "operator": lines[-1][cursor],
            "operands": operands
        })
        cursor += column_width

    grand_total = 0
    for expression in expressions:
        if expression["operator"] == "*":
            grand_total += math.prod(expression["operands"])
        elif expression["operator"] == "+":
            grand_total += sum(expression["operands"])
        else:
            raise ValueError(f"Unknown operator: {expression['operator']}")

    print(grand_total)

solve()