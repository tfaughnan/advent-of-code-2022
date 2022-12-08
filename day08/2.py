#!/usr/bin/env pypy3

import functools
import operator
import sys

up = lambda f, r, c: [f[r_][c] for r_ in range(r)][::-1]
dn = lambda f, r, c: [f[r_][c] for r_ in range(r + 1, len(f))]
lt = lambda f, r, c: [f[r][c_] for c_ in range(c)][::-1]
rt = lambda f, r, c: [f[r][c_] for c_ in range(c + 1, len(f[r]))]

def view(tree, direction):
    distance = 0
    for neighbor in direction:
        distance += 1
        if neighbor >= tree:
            break
    return distance

def main():
    forest = [[int(tree) for tree in line.strip()] for line in sys.stdin]
    max_score = 0
    for r in range(len(forest)):
        for c in range(len(forest[0])):
            views = (view(forest[r][c], d(forest, r, c))
                     for d in (up, dn, lt, rt))
            max_score = max(functools.reduce(operator.mul, views, 1),
                            max_score)

    print(max_score)

if __name__ == '__main__':
    main()
