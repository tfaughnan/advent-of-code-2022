#!/usr/bin/env pypy3

import functools
import re
import sys

MIN = 0
MAX = 4_000_000

def taxidist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def outer_perimeter(s, r):
    sx, sy = s
    x = sx - r - 1
    y = sy
    while y > sy - r - 1:
        yield (x, y)
        x += 1
        y -= 1
    while y < sy:
        yield (x, y)
        x += 1
        y += 1
    while y < sy + r + 1:
        yield (x, y)
        x -= 1
        y += 1
    while y > sy:
        yield (x, y)
        x -= 1
        y -= 1

def contained(p, signals, ignore):
    for s, r in signals:
        if s == ignore:
            continue
        d = taxidist(s, p)
        if d <= r:
            return True
    return False

def find_beacon(signals, minimum, maximum):
    for s1, r1 in signals:
        for p in outer_perimeter(s1, r1):
            if ((not contained(p, signals, s1)) and
                minimum <= p[0] <= maximum and
                minimum <= p[1] <= maximum):
                return p

    raise AssertionError('bruh')

def main():
    signals = []
    for line in sys.stdin:
        sx, sy, bx, by = map(int, re.findall(r'-?[0-9]+', line.strip()))
        signals.append(((sx, sy), taxidist((sx, sy), (bx, by))))

    p = find_beacon(signals, MIN, MAX)
    freq = p[0] * 4_000_000 + p[1]
    print(freq)

if __name__ == '__main__':
    main()
