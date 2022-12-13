#!/usr/bin/env pypy3

import sys

def strength(cycle, x):
    return cycle * x if not (cycle - 20) % 40 else 0

def main():
    x = 1
    cycle = 1
    strength_sum = 0
    for line in sys.stdin:
        strength_sum += strength(cycle, x)
        instruction = line.split()
        if instruction[0] == 'addx':
            strength_sum += strength(cycle + 1, x)
            x += int(instruction[1])
            cycle += 2
        else:
            cycle += 1

    print(strength_sum)

if __name__ == '__main__':
    main()
