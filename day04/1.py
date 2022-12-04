#!/usr/bin/env pypy3

import sys

def main():
    pairs = ([set(range(a, b + 1)) for a, b in c] for c in
             (([*map(int, d.split('-'))] for d in line.strip().split(','))
              for line in sys.stdin))
    overlaps = (a.issubset(b) or b.issubset(a) for a, b in pairs)
    print(sum(overlaps))

if __name__ == '__main__':
    main()
