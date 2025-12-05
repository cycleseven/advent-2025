# Doing some OOP today for fun, why not

from __future__ import annotations

import itertools
import sys
import typing


class Grid:
    def __init__(self, layout: typing.IO[str]):
        self.layout = [list(line.strip()) for line in layout]

    # Assume square layout, so no separate width + height
    @property
    def size(self) -> int:
        return len(self.layout)

    def at(self, point: Point):
        return self.layout[point.i][point.j]


class Cafeteria(Grid):
    def get_adjacent_rolls(self, point: Point):
        adjacent_points = point.adjacent_points
        return [
            adjacent_point
            for adjacent_point in adjacent_points
            if self.at(adjacent_point) == "@"
        ]


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
cafeteria = Cafeteria(sys.stdin)

for i in range(cafeteria.size):
    for j in range(cafeteria.size):
        p = Point(i, j, cafeteria)

        if cafeteria.at(p) != "@":
            continue

        if len(cafeteria.get_adjacent_rolls(p)) < 4:
            accessible_points.append(p)

print(len(accessible_points))
