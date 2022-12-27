#!/usr/bin/env pypy3

import re
import sys
from collections import defaultdict

START = 'AA'
TOTAL_TIME = 30

def floyd_warshall(valves):
    dists = defaultdict(lambda: sys.maxsize)
    for v in valves:
        _, neighbors = valves[v]
        for n in neighbors:
            dists[v, n] = 1
        dists[v, v] = 0

    sorted_valves = sorted(valves.keys())   # better safe than sorry
    for k in sorted_valves:
        for i in sorted_valves:
            for j in sorted_valves:
                dists[i, j] = min(dists[i, j], dists[i, k] + dists[k, j])

    return dists

def max_pressure(valves, dists, here, t, opened=frozenset({START}), cache={}):
    if (here, t, opened) in cache:
        return cache[here, t, opened]
    if t <= 1:
        cache[here, t, opened] = 0
        return cache[here, t, opened]

    options = [max_pressure(valves, dists, v, t - dists[here, v], opened, cache)
               for v in set(valves) - opened]
    if here not in opened:
        options.append(max_pressure(valves, dists, here, t - 1, opened | {here},
                                    cache) + valves[here] * (t - 1))
    cache[here, t, opened] = max(options, default=0)
    return cache[here, t, opened]

def main():
    valves = {}
    for line in sys.stdin:
        m = re.match(r'^Valve ([A-Z]{2}) has flow rate=([0-9]+); tunnels? '
                     r'leads? to valves? ([A-Z, ]+)$', line.strip())
        valve = m.group(1)
        rate = int(m.group(2))
        neighbors = m.group(3).split(', ')
        valves[valve] = (rate, neighbors)

    dists = floyd_warshall(valves)
    for v, n in list(dists):
        if v == n or (valves[v][0] == 0 and v != START) or valves[n][0] == 0:
            del dists[v, n]
    valves = {v: valves[v][0] for v in valves if valves[v][0] > 0 or v == START}

    p = max_pressure(valves, dists, START, TOTAL_TIME)
    print(p)

if __name__ == '__main__':
    main()
