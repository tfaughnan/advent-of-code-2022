#!/usr/bin/env pypy3

from collections import defaultdict
import re
import string
import sys

def build_stacks(lines):
    stacks = defaultdict(list)
    for line in lines.split('\n')[:-1]:
        for col, char in enumerate(line):
            if char in string.ascii_uppercase:
                stacks[(col - 1) // 4].insert(0, char)

    return stacks

def move_crates(moves, stacks):
    for move in moves.split('\n')[:-1]:
        m = re.match(r'^move ([0-9]+) from ([0-9]+) to ([0-9]+)$', move.strip())
        amount, stack_from, stack_to = map(int, m.groups())
        for _ in range(amount):
            crate = stacks[stack_from - 1].pop()
            stacks[stack_to - 1].append(crate)

def main():
    stack_lines, move_lines = sys.stdin.read().split('\n\n')
    stacks = build_stacks(stack_lines)
    move_crates(move_lines, stacks)
    msg = ''.join(stacks[i][-1] for i in sorted(stacks.keys()))
    print(msg)

if __name__ == '__main__':
    main()
