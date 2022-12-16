#!/usr/bin/env pypy3

import re
import sys
from collections import defaultdict

SOURCE = (500, 0)

def line_points(start, end):
    startx, starty = start
    endx, endy = end
    if startx == endx:
        for y in range(min(starty, endy), max(starty, endy) + 1):
            yield startx, y
    elif starty == endy:
        for x in range(min(startx, endx), max(startx, endx) + 1):
            yield x, starty
    else:
        raise ValueError('Horizontal and vertical lines only!')

def drop_sand(cave, source, floor):
    sand = source
    future_sand = (None, None)
    while True:
        future_sand = advance_sand(cave, sand)
        if future_sand == sand or future_sand[1] >= floor:
            cave[sand] = 'o'
            return
        sand = future_sand

def advance_sand(cave, sand):
    sandx, sandy = sand
    if cave[sandx, sandy + 1] == '.':
        return sandx, sandy + 1
    elif cave[sandx - 1, sandy + 1] == '.':
        return sandx - 1, sandy + 1
    elif cave[sandx + 1, sandy + 1] == '.':
        return sandx + 1, sandy + 1
    else:
        return sandx, sandy

def main():
    cave = defaultdict(lambda: '.')
    cave[SOURCE] = '+'
    floor = 0
    for line in sys.stdin:
        x1, y1 = None, None
        for pair in line.strip().split(' -> '):
            x2, y2 = map(int, pair.split(','))
            floor = max(floor, y2 + 2)
            if (x1, y1) != (None, None):
                for x, y in line_points((x1, y1), (x2, y2)):
                    cave[x, y] = '#'
            x1, y1 = x2, y2

    units = 0
    while cave[SOURCE] != 'o':
        drop_sand(cave, SOURCE, floor)
        units += 1

    print(units)

if __name__ == '__main__':
    main()
