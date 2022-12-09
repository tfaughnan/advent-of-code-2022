#!/usr/bin/env pypy3

import sys

NUMKNOTS = 10
DIRECTIONS = {
    'R': 1,
    'L': -1,
    'U': 1j,
    'D': -1j,
}

def update(z1, z2):
    dz = z1 - z2
    if abs(dz) < 2: # ceil(sqrt(2))
        return 0
    return complex(*(part / abs(part) if part else 0
                     for part in (dz.real, dz.imag)))

def main():
    knots = [0 + 0j] * NUMKNOTS
    visited = {knots[-1]}
    for line in sys.stdin:
        direction, magnitude = line.split()
        for _ in range(int(magnitude)):
            knots[0] += DIRECTIONS[direction]
            for i in range(1, NUMKNOTS):
                knots[i] += update(knots[i - 1], knots[i])
            visited.add(knots[-1])

    print(len(visited))

if __name__ == '__main__':
    main()
