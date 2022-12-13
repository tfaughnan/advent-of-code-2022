#!/usr/bin/env pypy3

import ast
import sys

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

def main():
    pairs = [map(ast.literal_eval, section.split('\n')[:2])
             for section in sys.stdin.read().split('\n\n')]
    total = sum(pairs.index(p) + 1 for p in pairs if ordered(*p))
    print(total)

if __name__ == '__main__':
    main()
