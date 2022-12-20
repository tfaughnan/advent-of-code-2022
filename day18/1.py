#!/usr/bin/env pypy3

import operator
import sys

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

def main():
    cubes = {tuple(map(int, line.split(','))) for line in sys.stdin}
    area = sum(tuple(map(operator.add, cube, d)) not in cubes
               for cube in cubes
               for d in DIRECTIONS)
    print(area)

if __name__ == '__main__':
    main()
