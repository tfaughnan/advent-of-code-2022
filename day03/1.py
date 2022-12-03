#!/usr/bin/env pypy3

import string
import sys

def main():
    rucksacks = ((set(r[:(len(r) - 1) // 2]), set(r[(len(r) - 1) // 2:-1]))
                 for r in sys.stdin)
    priorities = (string.ascii_letters.index(next(iter(set.intersection(*r)))) + 1
                  for r in rucksacks)
    print(sum(priorities))

if __name__ == '__main__':
    main()
