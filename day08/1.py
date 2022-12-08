#!/usr/bin/env pypy3

import sys

up = lambda f, r, c: [f[r_][c] for r_ in range(r)][::-1]
dn = lambda f, r, c: [f[r_][c] for r_ in range(r + 1, len(f))]
lt = lambda f, r, c: [f[r][c_] for c_ in range(c)][::-1]
rt = lambda f, r, c: [f[r][c_] for c_ in range(c + 1, len(f[r]))]

def main():
    forest = [[int(tree) for tree in line.strip()] for line in sys.stdin]
    total = 0
    for r in range(len(forest)):
        for c in range(len(forest[0])):
            total += any(forest[r][c] > max(d(forest, r, c), default=-1)
                         for d in (up, dn, lt, rt))

    print(total)

if __name__ == '__main__':
    main()
