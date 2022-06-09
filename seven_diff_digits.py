"""
Mathigon 2021 Puzzle Calendars Number 8

Seven different digits are placed in a row. The products of
the first three, middle three and last three digits are all
equal. What is the middle digit?

:source: https://mathigon.org/puzzles
"""

from itertools import permutations as P
from functools import reduce
from operator import mul
perms = P(range(1, 10), 7)
for p in perms:
    f, m, l = p[:3], p[2:5], p[4:]
    if reduce(mul, f) == reduce(mul, m) == reduce(mul, l):
        print(p[3])
        break
