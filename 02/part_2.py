from pprint import pprint
import sys

def is_repeated_digit_sequence(n):
    as_str = str(n)

    for sequence_length in range(1, len(as_str)):
        repetitions, remainder = divmod(len(as_str), sequence_length)

        if remainder != 0:
            continue

        if as_str[:sequence_length] * repetitions == as_str:
            return True

    return False


ranges = [
    tuple(int(value) for value in raw_range.split("-"))
    for raw_range in sys.stdin.read().split(',')
]

invalid_ids = []

for a, b in ranges:
    for i in range(a, b + 1):
        if is_repeated_digit_sequence(i):
            invalid_ids.append(i)

pprint(sum(invalid_ids))