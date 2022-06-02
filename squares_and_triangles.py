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
