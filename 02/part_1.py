import sys

def is_doubled_digit_sequence(n):
    as_str = str(n)

    if len(as_str) % 2 != 0:
        return False

    midpoint = int(len(as_str) * 0.5)
    return as_str[0:midpoint] == as_str[midpoint:]

ranges = [
    tuple(int(value) for value in raw_range.split("-"))
    for raw_range in sys.stdin.read().split(',')
]

invalid_ids = []

for a, b in ranges:
    for i in range(a, b + 1):
        if is_doubled_digit_sequence(i):
            invalid_ids.append(i)

print(sum(invalid_ids))