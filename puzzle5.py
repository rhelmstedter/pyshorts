"""my solution"""
from math import lcm
for n in range(100, 1000):
    if not n % lcm(3, 4, 5, 6, 10, 11) \
            and n % lcm(7, 8, 9):
        print(n)

"""Richard's better solution"""
for n in range(0, 1000, lcm(3, 4, 5, 6, 10, 11)):
    if n >= 100 and all(n % f for f in (7, 8, 9)):
        print(n)
