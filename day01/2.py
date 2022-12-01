#!/usr/bin/env pypy3

import sys

def main():
    elves = [map(int, elf.split('\n')) for elf in sys.stdin.read()[:-1].split('\n\n')]
    print(sum(sorted(map(sum, elves), reverse=True)[:3]))

if __name__ == '__main__':
    main()
