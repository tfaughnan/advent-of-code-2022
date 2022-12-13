#!/usr/bin/env pypy3

import sys

CRT_W = 40
CRT_H = 6

def crt_update(crt, cycle, x):
    row = (cycle - 1) // 40
    col = (cycle - 1) % 40
    if abs(x - col) <= 1:
        crt[row][col] = '#'

def main():
    x = 1
    cycle = 1
    crt = [['.' for _ in range(CRT_W)] for _ in range(CRT_H)]
    for line in sys.stdin:
        crt_update(crt, cycle, x)
        instruction = line.split()
        if instruction[0] == 'addx':
            crt_update(crt, cycle + 1, x)
            x += int(instruction[1])
            cycle += 2
        else:
            cycle += 1

    print('\n'.join(''.join(row) for row in crt))

if __name__ == '__main__':
    main()
