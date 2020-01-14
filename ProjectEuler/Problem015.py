"""Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо,
существует ровно 6 маршрутов до правого нижнего угла сетки.
Сколько существует таких маршрутов в сетке 20×20?"""
import numpy

size_matrix = 3
matrix = numpy.array([i + 1 for i in range(size_matrix * size_matrix)]).reshape(size_matrix, size_matrix)

for i in range(size_matrix):
    for j in range(size_matrix):
        print(matrix[i][j], end='\t')
    print()
