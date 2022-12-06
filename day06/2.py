#!/usr/bin/env pypy3

import sys

WINSIZ = 14

def main():
    data = sys.stdin.read().strip()
    for i in range(len(data) - WINSIZ):
        if len(set(data[i:i + WINSIZ])) == WINSIZ:
            print(i + WINSIZ)
            break

if __name__ == '__main__':
    main()
