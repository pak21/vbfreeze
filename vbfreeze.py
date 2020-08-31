#!/usr/bin/env python3

from sympy import *

def no_freeze():
    a0, a1, a2, a3, a4, p = symbols(['a0', 'a1', 'a2', 'a3', 'a4', 'p'])

    e0 = Eq(a0, p*a1 + (1-p))
    e1 = Eq(a1, (1-p)*a2 + p*a3)
    e2 = Eq(a2, (1-p)*a1 + p)
    e3 = Eq(a3, (1-p)*a4)
    e4 = Eq(a4, p*a2 + (1-p)*a3)

    solutions = linsolve([e0, e1, e2, e3, e4], (a0, a1, a2, a3, a4))
    if len(solutions) != 1:
        raise Exception(solutions)
    for solution in solutions:
        for x in solution:
            print(latex(x))
        print()
        overall_chance = solution[0]
        print(overall_chance)
        print(overall_chance.subs(p, 0.25))

def freeze():
    a0, a1, a2, a3, p = symbols(['a0', 'a1', 'a2', 'a3', 'p'])

    e0 = Eq(a0, (1-p)*a1 + p*a2)
    e1 = Eq(a1, (1-p)*a0 + p)
    e2 = Eq(a2, (1-p)*a3)
    e3 = Eq(a3, (1-p)*a2 + p)

    solutions = linsolve([e0, e1, e2, e3], (a0, a1, a2, a3))
    if len(solutions) != 1:
        raise Exception(solutions)
    for solution in solutions:
        for x in solution:
            print(latex(x))
        print()
        overall_chance = solution[0]
        print(overall_chance)
        print(overall_chance.subs(p, 0.25))

def main():
    no_freeze_chance = no_freeze()
    print()
    freeze_chance = freeze()

if __name__ == '__main__':
    main()
