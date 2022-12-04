#!/usr/bin/env pypy3

import sys

def main():
    pairs = ([*map(lambda x: set(range(x[0], x[1] + 1)), x)] for x in
             (map(lambda y: [*map(int, y.split('-'))], line.strip().split(','))
              for line in sys.stdin))
    overlaps = map(lambda x: x[0].issubset(x[1]) or x[1].issubset(x[0]), pairs)
    print(sum(overlaps))

if __name__ == '__main__':
    main()
