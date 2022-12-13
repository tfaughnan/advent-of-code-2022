#!/usr/bin/env pypy3

import ast
import math
import sys

DIVIDER_PACKETS = [[[2]], [[6]]]

def ordered(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return l < r or (False if l > r else None)
    elif isinstance(l, list) and isinstance(r, list):
        for ll, rr in zip(l, r):
            if (result := ordered(ll, rr)) is not None:
                return result
        return len(l) < len(r) or (False if len(r) < len(l) else None)
    else:
        return ordered([l], r) if isinstance(l, int) else ordered(l, [r])

def sort_packets(packets):
    n = len(packets)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if not ordered(packets[j], packets[j + 1]):
                packets[j], packets[j + 1] = packets[j + 1], packets[j]

def main():
    packets = [ast.literal_eval(line.strip()) for line in sys.stdin
               if line != '\n'] + DIVIDER_PACKETS
    sort_packets(packets)
    key = math.prod(packets.index(p) + 1 for p in DIVIDER_PACKETS)
    print(key)

if __name__ == '__main__':
    main()
