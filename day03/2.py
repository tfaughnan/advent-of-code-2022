#!/usr/bin/env pypy3

import string
import sys

def group_sacks(rucksacks, size):
    for i in range(0, len(rucksacks), size):
        yield rucksacks[i:i + size]

def main():
    groups = group_sacks([set(r[:-1]) for r in sys.stdin], 3)
    priorities = (string.ascii_letters.index(next(iter(set.intersection(*r)))) + 1
                  for r in groups)
    print(sum(priorities))

if __name__ == '__main__':
    main()
