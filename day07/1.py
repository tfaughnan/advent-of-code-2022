#!/usr/bin/env pypy3

import os.path
import re
import sys

SIZE_BOUND = 100000

def main():
    dirsizes = {}
    cwd = '/'
    for line in sys.stdin:
        if m := re.match(r'^\$ cd \.\.$', line):
            cwd, _ = os.path.split(cwd)
        elif m := re.match(r'^\$ cd (\S+)$', line):
            cwd = os.path.join(cwd, m.group(1))
            dirsizes[cwd] = 0
        elif m := re.match(r'^([0-9]+) (\S+)$', line):
            size = int(m.group(1))
            for d in filter(cwd.startswith, dirsizes):
                dirsizes[d] += size

    print(sum(v for v in dirsizes.values() if v <= SIZE_BOUND))

if __name__ == '__main__':
    main()
