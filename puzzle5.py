"""
Puzzle 5
1. It is a thre-digit whole number.
2. It is divisible by 4.
3. It is divisible by 5.
4. It is divisible by 11.
5. It is divisible by 3.
6. It is divisible by 10.
7. It is divisible by 6.
8. It not is divisible by 9.
9. It not is divisible by 8.
10. It not is divisible by 7.
"""

from math import lcm

"""my solution"""
for n in range(100, 1000):
    if not n % lcm(3, 4, 5, 6, 10, 11) \
            and n % lcm(7, 8, 9):
        print(n)

"""Richard's better solution"""
for n in range(0, 1000, lcm(3, 4, 5, 6, 10, 11)):
    if n >= 100 and all(n % f for f in (7, 8, 9)):
        print(n)
