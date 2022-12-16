#!/usr/bin/env pypy3

import functools
import re
import sys

ROW_Y = 2_000_000

def taxidist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def main():
    xranges = set()
    for line in sys.stdin:
        sx, sy, bx, by = map(int, re.findall(r'-?[0-9]+', line.strip()))
        d = taxidist((sx, sy), (bx, by))
        rowd = taxidist((sx, sy), (sx, ROW_Y))
        if rowd <= d:
            xlower = sx - (d - rowd)
            xupper = sx + (d - rowd)
            if bx == xlower:
                xlower += 1
            elif bx == xupper:
                xupper -= 1
            xranges.add((xlower, xupper))

    # XXX: wasteful!
    xs = functools.reduce(set.union, (set(range(l, u + 1))
                                      for l, u in xranges))
    print(len(xs))

if __name__ == '__main__':
    main()
