import sys


def parse():
    fresh_ranges = []
    available_ingredients = []

    is_parsing_ranges = True

    for line in sys.stdin:
        if line.isspace():
            is_parsing_ranges = False
            continue

        if is_parsing_ranges:
            a, b = line.split("-")
            fresh_ranges.append((int(a), int(b)))
        else:
            available_ingredients.append(int(line))

    return {
        "fresh_ranges": fresh_ranges,
        "available_ingredients": available_ingredients,
    }


data = parse()
print(sum(
    1
    for ingredient in data["available_ingredients"]
    if any(a <= ingredient <= b for a, b in data["fresh_ranges"])
))