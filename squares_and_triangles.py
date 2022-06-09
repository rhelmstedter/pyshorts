"""
Mathigon 2021 Puzzle Calendars 4

After 1 and 36, what is the next number that is both a
square number and a triangular number?

:source: https://mathigon.org/puzzles
"""

squares = []
n = 7
while True:
    nth_square = n ** 2
    nth_triangle = n * (n + 1) // 2
    squares.append(nth_square)
    if nth_triangle in squares:
        print(nth_triangle)
        break
    n += 1
