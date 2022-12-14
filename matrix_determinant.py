sizeOfMatrix = int(input('Размер матрицы: '))
m = []

for i in range(sizeOfMatrix):
    rows = list(map(int, input('Введите цыфры, которые, будут добавлены  в мтарицу через пробел: ').split()))[:sizeOfMatrix]
    m.append(rows)

print(f'\nМатрица:')
for i in m:
    print(*i)


def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def minor(matrix, i, j):
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp


def determinant(matrix):
    size = len(matrix)
    if size == 2:
        return det2(matrix)

    return sum((-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
               for j in range(size))


print()
print("Определитель матрицы = " + str(determinant(m)))
