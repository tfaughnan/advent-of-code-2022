#!/usr/bin/env pypy3

import itertools
import sys
from collections import defaultdict

WIDTH = 7
ITERATIONS = 2022
ROCKS = itertools.cycle((
    ((1, 1, 1, 1),
     (0, 0, 0, 0),
     (0, 0, 0, 0),
     (0, 0, 0, 0)),
    ((0, 1, 0, 0),
     (1, 1, 1, 0),
     (0, 1, 0, 0),
     (0, 0, 0, 0)),
    ((0, 0, 1, 0),
     (0, 0, 1, 0),
     (1, 1, 1, 0),
     (0, 0, 0, 0)),
    ((1, 0, 0, 0),
     (1, 0, 0, 0),
     (1, 0, 0, 0),
     (1, 0, 0, 0)),
    ((1, 1, 0, 0),
     (1, 1, 0, 0),
     (0, 0, 0, 0),
     (0, 0, 0, 0)),
))
ROCK_HEIGHTS = itertools.cycle((1, 3, 3, 4, 2))
ROCK_WIDTHS = itertools.cycle((4, 3, 3, 1, 2))
DIRECTIONS = {
    '<': -1,
    '>': 1,
}
PUSHES = itertools.cycle(sys.stdin.read().strip())

def can_push(chamber, rock, rockw, rockh, x, y, dx, dy):
    nx = x + dx
    ny = y + dy
    for r in range(rockh):
        for c in range(rockw):
            if not rock[r][c]:
                continue
            if nx + c not in range(WIDTH):
                return False
            if ny - r < 0:
                return False
            if chamber[nx + c, ny - r]:
                return False
    return True

def main():
    chamber = defaultdict(int)
    tower_height = -1
    for _ in range(ITERATIONS):
        rock = next(ROCKS)
        rockh = next(ROCK_HEIGHTS)
        rockw = next(ROCK_WIDTHS)
        x = 2
        y = tower_height + 3 + rockh

        atrest = False
        while not atrest:
            dx = DIRECTIONS[next(PUSHES)]
            if can_push(chamber, rock, rockw, rockh, x, y, dx, 0):
                x += dx
            if can_push(chamber, rock, rockw, rockh, x, y, 0, -1):
                y -= 1
            else:
                atrest = True

        for r in range(rockh):
            for c in range(rockw):
                if rock[r][c]:
                    chamber[x + c, y - r] = 1
        tower_height = max(tower_height, y)

    print(tower_height + 1)

if __name__ == '__main__':
    main()
