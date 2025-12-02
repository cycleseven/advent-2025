import sys

dial_position = 50
zeros = 0

for line in sys.stdin:
    direction = 1 if line[0] == "R" else -1
    amount = int(line[1:])
    dial_position = (dial_position + (direction * amount)) % 100

    if dial_position == 0:
        zeros += 1

print(zeros)