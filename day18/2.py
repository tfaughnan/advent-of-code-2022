#!/usr/bin/env pypy3

import operator
import sys
from collections import deque

#   |+y          Convention:
#   |___+x       ===========
#  /             Right-handed coordinate system
# +z             with positive y direction as "up"

DIRECTIONS = (
    (-1, 0, 0),     # left
    (1, 0, 0),      # right
    (0, -1, 0),     # below
    (0, 1, 0),      # above
    (0, 0, -1),     # back
    (0, 0, 1),      # front
)

def flood_fill(cubes, air, extrema, start):
    min_x, max_x, min_y, max_y, min_z, max_z = extrema
    todo = deque([start])
    while todo:
        node = todo.popleft()
        if node in cubes or node in air:
            continue
        air.add(node)
        neighbors = filter(lambda n: (min_x <= n[0] <= max_x and
                                      min_y <= n[1] <= max_y and
                                      min_z <= n[2] <= max_z),
                           (tuple(map(operator.add, node, d))
                            for d in DIRECTIONS))
        for neighbor in neighbors:
            todo.append(neighbor)

def main():
    cubes = {tuple(map(int, line.split(','))) for line in sys.stdin}
    air = set()
    extrema = (min(x for x, y, z in cubes) - 1,
               max(x for x, y, z in cubes) + 1,
               min(y for x, y, z in cubes) - 1,
               max(y for x, y, z in cubes) + 1,
               min(z for x, y, z in cubes) - 1,
               max(z for x, y, z in cubes) + 1)
    start = (extrema[0], extrema[2], extrema[4])
    flood_fill(cubes, air, extrema, start)
    area = sum(tuple(map(operator.add, cube, d)) not in cubes
               for cube in cubes
               for d in DIRECTIONS
               if tuple(map(operator.add, cube, d)) in air)
    print(area)

if __name__ == '__main__':
    main()
