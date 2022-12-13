#!/usr/bin/env pypy3

import math
import operator
import re
import sys

NUMROUNDS = 10000
OPS = {'*': operator.mul, '+': operator.add}

class Monkey:
    def __init__(self, items, op, arg, factor, yes, no):
        self.items = items
        self.inspected = 0
        self.update = lambda item: OPS[op](item, item if arg == 'old' else int(arg))
        self.target = lambda item: yes if not item % factor else no

def main():
    lcm = 1
    monkeys = []
    for block in sys.stdin.read().split('\n\n'):
        attrs = map(str.strip, block.split('\n')[1:])
        items = [int(item) for item in re.match(r'^Starting items: ([0-9, ]+)$',
                                                next(attrs)).group(1).split(', ')]
        op, arg = re.match(r'^Operation: new = old ([*+]) (\S+)$', next(attrs)).groups()
        factor = int(re.match(r'^Test: divisible by ([0-9]+)$', next(attrs)).group(1))
        yes = int(re.match(r'^If true: throw to monkey ([0-9]+)$', next(attrs)).group(1))
        no = int(re.match(r'^If false: throw to monkey ([0-9]+)$', next(attrs)).group(1))
        monkeys.append(Monkey(items, op, arg, factor, yes, no))
        lcm = math.lcm(lcm, factor)

    for _ in range(NUMROUNDS):
        for i in range(len(monkeys)):
            while monkeys[i].items:
                item = monkeys[i].update(monkeys[i].items.pop(0))
                monkeys[monkeys[i].target(item)].items.append(item % lcm)
                monkeys[i].inspected += 1

    *_, second, first = sorted(m.inspected for m in monkeys)
    print(second * first)

if __name__ == '__main__':
    main()
