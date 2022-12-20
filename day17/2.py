#!/usr/bin/env pypy3

import itertools
import sys
from collections import defaultdict

WIDTH = 7
ITERATIONS = 1000000000000
NUMROCKS = 5
ROCKS = enumerate(itertools.cycle((
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
)))
ROCK_HEIGHTS = itertools.cycle((1, 3, 3, 4, 2))
ROCK_WIDTHS = itertools.cycle((4, 3, 3, 1, 2))
DIRECTIONS = {
    '<': -1,
    '>': 1,
}
PUSH_LIST = sys.stdin.read().strip()
NUMPUSHES = len(PUSH_LIST)
PUSHES = enumerate(itertools.cycle(PUSH_LIST))

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
    history = {}
    period = None
    for numdropped in range(ITERATIONS):
        rock_index, rock = next(ROCKS)
        rockh = next(ROCK_HEIGHTS)
        rockw = next(ROCK_WIDTHS)
        x = 2
        y = tower_height + 3 + rockh

        atrest = False
        while not atrest:
            push_index, push = next(PUSHES)
            dx = DIRECTIONS[push]
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

        if period:
            ran_height = next(v for _, v in history.items()
                              if v[0] == sim_start + (ITERATIONS - sim_end - 1))[1]
            sim_height = dheight * numsims
            tower_height = ran_height + sim_height
            break
        else:
            skyline = tuple(tower_height - max((y for x, y in chamber
                                                if chamber[x, y] and x == xx),
                                               default=0)
                            for xx in range(WIDTH))
            key = (rock_index % NUMROCKS, push_index % NUMPUSHES, skyline)
            if key in history:
                sim_start = history[key][0]
                period = numdropped - sim_start
                dheight = tower_height - history[key][1]
                numsims = (ITERATIONS - sim_start) // period
                sim_end = numsims * period + sim_start
            else:
                value = (numdropped, tower_height)
                history[key] = value

    print(tower_height + 1)

if __name__ == '__main__':
    main()
