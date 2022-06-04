"""Puzzle 3"""

"""
1. It is a four-digit number.
2. Each of its digit is even.
3. Each of its digit is different.
4. The sum of its one digit and its hundreds digit is 10.
5. The sum of its tens digit and its thousands digit is 10.
6. It is greater than 7000.
7. It is divisible by 4.
8. The number zero is not one of its digits.
9. It is divisible by 8.
10. Its hundreds digit is 8.
"""

possible_nums = []
for num in range(1000, 10_000):
    possible_nums.append(num)

print(len(possible_nums))
