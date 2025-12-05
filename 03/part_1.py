import sys

largest_joltages = []

for line in sys.stdin:
    joltages = [int(digit) for digit in line.strip()]

    i, tens_value = max(
        enumerate(joltages[:-1]),
        key=lambda x: x[1]
    )

    j, units_value = max(
        enumerate(joltages[i + 1:], i + 1),
        key=lambda x: x[1]
    )

    largest_joltage = tens_value * 10 + units_value
    largest_joltages.append(largest_joltage)

print(sum(largest_joltages))