"""
Mathigon 2021 Puzzle Calendars Number 8

Seven different digits are placed in a row. The products of
the first three, middle three and last three digits are all
equal. What is the middle digit?

:source: https://mathigon.org/puzzles
"""

from itertools import permutations as P
from math import prod
perms = P(range(1, 10), 7)
for p in perms:
    first3, middle3, last3 = p[:3], p[2:5], p[4:]
    if prod(first3) == prod(middle3) == prod(last3):
        print(p[3])
        break
