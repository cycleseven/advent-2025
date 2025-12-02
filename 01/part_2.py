import sys

dial_position = 50
zeros = 0

for line in sys.stdin:
    direction = 1 if line[0] == "R" else -1
    amount = int(line[1:])

    # I think there's a clever fast way to figure out if you passed
    # zero without actually simulating the dial clicks. But... whatever :D
    for _ in range(amount):
        dial_position += direction * 1

        if dial_position == 0:
            zeros += 1
        elif dial_position == -1:
            dial_position = 99
        elif dial_position == 100:
            dial_position = 0
            zeros += 1

print(zeros)