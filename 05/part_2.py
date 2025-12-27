import itertools
import sys
from pprint import pprint


def parse():
    ranges = []

    for line in sys.stdin:
        if line.isspace():
            return ranges

        a, b = line.split("-")
        ranges.append((int(a), int(b)))

    return ranges


def merge_ranges(ranges):
    merged_ranges = []

    for (a, b) in sorted(ranges):
        try:
            previous_range = merged_ranges[-1]
        except IndexError:
            merged_ranges.append((a, b))
            continue

        c, d = previous_range
        if c <= a <= d:
            merged_ranges[-1] = (min(a, c), max(b, d))
        else:
            merged_ranges.append((a, b))

    return merged_ranges


def solve():
    ranges = parse()
    merged_ranges = merge_ranges(ranges)

    return sum(b - a + 1 for a, b in merged_ranges)


solution = solve()
print(solution)