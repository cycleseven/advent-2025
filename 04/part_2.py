# Doing some OOP today for fun, why not

from __future__ import annotations

import itertools
import sys


class Grid:
    def __init__(self, layout: list[list[str]]):
        self.layout = layout

    def __str__(self):
        return "\n".join("".join(row) for row in self.layout)

    # Assume square layout, so no separate width + height
    @property
    def size(self) -> int:
        return len(self.layout)

    def at(self, point: Point) -> str:
        return self.layout[point.i][point.j]


class Cafeteria(Grid):
    def get_adjacent_rolls(self, point: Point) -> list[Point]:
        adjacent_points = point.adjacent_points
        return [
            adjacent_point
            for adjacent_point in adjacent_points
            if self.at(adjacent_point) == "@"
        ]

    def remove_removable_rolls(self) -> tuple[int, Cafeteria]:
        next_cafeteria_layout = []
        num_removed = 0

        for i in range(self.size):
            next_cafeteria_layout.append([])

            for j in range(self.size):
                p = Point(i, j, self)

                if self.at(p) != "@":
                    next_cafeteria_layout[-1].append(".")
                    continue

                if len(self.get_adjacent_rolls(p)) < 4:
                    next_cafeteria_layout[-1].append(".")
                    num_removed += 1
                else:
                    next_cafeteria_layout[-1].append("@")

        return num_removed, Cafeteria(next_cafeteria_layout)


class Point:
    def __init__(self, i: int, j: int, grid: Grid):
        self.i = i
        self.j = j
        self.grid = grid

    def __str__(self):
        return f"({self.i}, {self.j})"

    def __repr__(self):
        return f"({self.i}, {self.j})"

    @property
    def adjacent_points(self) -> list[Point]:
        return [
            Point(adjacent_i, adjacent_j, self.grid)
            for adjacent_i, adjacent_j in itertools.product(
                range(self.i - 1, self.i + 2),
                range(self.j - 1, self.j + 2),
            )
            if 0 <= adjacent_i < self.grid.size
            and 0 <= adjacent_j < self.grid.size
            and not (adjacent_i == self.i and adjacent_j == self.j)
        ]


accessible_points = []
cafeteria = Cafeteria([list(line.strip()) for line in sys.stdin])

removed = None
removed_sum = 0

while removed != 0:
    removed, cafeteria = cafeteria.remove_removable_rolls()
    removed_sum += removed


print(removed_sum)
