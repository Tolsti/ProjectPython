"""Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке, образуется следующая спираль 5 на 5:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

Можно убедиться, что сумма чисел в диагоналях равна 101.

Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной таким же способом?"""

matrix = 7
spiral = [[0 for i in range(matrix)] for j in range(matrix)]
# print(spiral)

# print(int(len(spiral) / 2 + 1), int(len(spiral[0]) / 2))

# for i in range(matrix):
#     for j in range(matrix):
#         spiral[int(len(spiral) / 2)][int(len(spiral[0]) / 2)] = 1

spiral[matrix // 2][matrix // 2] = 1

# for i in range(matrix):
#     for j in range(matrix):
#         print(spiral[i][j], end = '   ')
#     print()

NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)  # directions
turn_right = {NORTH: E, E: S, S: W, W: NORTH}  # old -> new direction


def spiral(width, height):
    if width < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2  # start near the center
    dx, dy = NORTH  # initial direction
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count  # visit
        # try to turn right
        new_dx, new_dy = turn_right[dx, dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
                matrix[new_y][new_x] is None):  # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else:  # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix  # nowhere to go


spiral = spiral(matrix, matrix)

for i in range(matrix):
    for j in range(matrix):
        print(spiral[i][j], end=' \t')
    print()
