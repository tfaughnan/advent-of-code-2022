#!/usr/bin/env pypy3

import operator
import re
import sys

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '=': operator.eq
}

INVERSE_OPERATORS = {
    '+': lambda a, b, c: a - b if c else b - a,
    '-': lambda a, b, c: a + b if c else a - b,
    '*': lambda a, b, c: a // b if c else b // a,
    '/': lambda a, b, c: a * b if c else a // b,
    '=': lambda a, b, c: b if c else a  # hacky
}

class Monkey:
    def __init__(self, name, value=None, op=None, lhs=None, rhs=None):
        self.name = name
        self.value = value
        self.op = OPERATORS.get(op, None)
        self.invop = INVERSE_OPERATORS.get(op, None)
        self.lhs = lhs
        self.rhs = rhs

    def find(self, name):
        if self.name == name:
            return self
        elif self.lhs is None and self.rhs is None:
            return None
        return self.lhs.find(name) or self.rhs.find(name)

    def evaluate(self):
        if self.value is None:
            self.value = self.op(self.lhs.evaluate(), self.rhs.evaluate())
        return self.value

    def sethumn(self, target=None):
        if self.name == 'humn':
            self.value = target
            print(self.value)
        elif (self.lhs.find('humn')):
            rhsval = self.rhs.evaluate()
            target = self.invop(target, rhsval, True)
            self.lhs.sethumn(target)
        else:
            lhsval = self.lhs.evaluate()
            target = self.invop(lhsval, target, False)
            self.rhs.sethumn(target)

def main():
    orphans = {}
    for line in sys.stdin:
        if (m := re.match(r'^([a-z]+): (-?[0-9]+)$', line.strip())):
            name = m.group(1)
            value = int(m.group(2))
            op, lhs, rhs = None, None, None
        elif (m := re.match(r'^([a-z]+): ([a-z]+) ([-+*/]) ([a-z]+)$', line.strip())):
            name = m.group(1)
            value = None
            op = m.group(3)
            lhs = orphans.pop(m.group(2), Monkey(m.group(2)))
            rhs = orphans.pop(m.group(4), Monkey(m.group(4)))
        else:
            raise ValueError('Invalid line')
        orphans[name] = Monkey(name, value, op, lhs, rhs)

    root = Monkey('root')
    while orphans:
        for name, orphan in list(orphans.items()):
            if (node := root.find(name)):
                node.value = orphan.value
                node.op = orphan.op
                node.invop = orphan.invop
                node.lhs = orphan.lhs
                node.rhs = orphan.rhs
                del orphans[name]

    root.op = OPERATORS['=']
    root.invop = INVERSE_OPERATORS['=']
    root.sethumn()
    assert root.evaluate()

if __name__ == '__main__':
    main()
