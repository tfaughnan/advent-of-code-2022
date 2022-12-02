#!/usr/bin/env pypy3

import sys

def main():
    score = 0
    for line in sys.stdin:
        rnd = line.strip().split()
        opp = ord(rnd[0]) - ord('A')                    # ascii
        me = (ord(rnd[1]) - ord('X') - 1 + opp) % 3     # haxx!
        score += me + 1 + ((me - opp + 1) % 3) * 3

    print(score)

if __name__ == '__main__':
    main()
