#!/usr/bin/env pypy3

import sys
from collections import deque

OFFSETS = (1000, 2000, 3000)

def mix(data, times=1):
    orig = list(enumerate(data))
    curr = orig.copy()
    for _ in range(times):
        todo = deque(orig)
        while todo:
            i, n = todo.popleft()
            j = curr.index((i, n))
            curr.pop(j)
            if n == -j and n < 0:
                curr.append((i, n))
            else:
                curr.insert((n + j) % len(curr), (i, n))

    return [n for _, n in curr]

def main():
    data = [int(line.strip()) for line in sys.stdin]
    mixed = mix(data)
    zero = mixed.index(0)
    coords = tuple(mixed[(zero + offset) % len(mixed)] for offset in OFFSETS)
    print(sum(coords))

if __name__ == '__main__':
    main()
