import sys

largest_joltages = []

for line in sys.stdin:
    joltages = [int(digit) for digit in line.strip()]
    start_index = 0
    max_joltage_digits = []

    for i in reversed(range(12)):
        end_index = -i if i > 0 else None
        index, value = max(
            enumerate(joltages[start_index:end_index]),
            key=lambda x: x[1]
        )
        start_index = start_index + index + 1
        max_joltage_digits.append(value)

    max_joltage = sum(
        10 ** factor * digit
        for factor, digit
        in enumerate(reversed(max_joltage_digits))
    )
    largest_joltages.append(max_joltage)


print(sum(largest_joltages))