#!/usr/bin/env pypy3

import sys
from collections import deque

def edges(graph, coord):
    r, c = coord
    return (n for n in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
            if n in graph and graph[n] - graph[coord] <= 1)

def shortest_path(graph, start, end):
    to_explore = deque([(start, 0)])
    explored = set()
    while to_explore:
        here, steps = to_explore.popleft()
        if here == end:
            return steps
        for neighbor in edges(graph, here):
            if neighbor not in explored:
                explored.add(neighbor)
                to_explore.append((neighbor, steps + 1))

    raise ValueError('No paths exist!')

def main():
    graph = {}
    start = None
    end = None
    for r, line in enumerate(sys.stdin):
        for c, char in enumerate(line.strip()):
            if char == 'S':
                start = (r, c)
                graph[(r, c)] = ord('a')
            elif char == 'E':
                end = (r, c)
                graph[(r, c)] = ord('z')
            else:
                graph[(r, c)] = ord(char)

    steps = shortest_path(graph, start, end)
    print(steps)

if __name__ == '__main__':
    main()
