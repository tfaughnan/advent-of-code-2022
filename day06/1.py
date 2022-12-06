#!/usr/bin/env pypy3

import sys

WINSIZ = 4

def main():
    data = sys.stdin.read().strip()
    nchars = next(i + WINSIZ for i in range(len(data) - WINSIZ)
                  if len(set(data[i:i + WINSIZ])) == WINSIZ)
    print(nchars)

if __name__ == '__main__':
    main()
