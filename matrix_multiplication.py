import sys
# Умножение матриц

sizeOfMatrix_1h = int(input('Размер матрицы 1 h: '))
sizeOfMatrix_1w = int(input('Размер матрицы 1 w: '))
sizeOfMatrix_2h = int(input('Размер матрицы 2 h: '))
sizeOfMatrix_2w = int(input('Размер матрицы 2 w: '))


A = []
B = []

for i in range(sizeOfMatrix_1h):
    rows = list(map(int, input('Введите цыфры, которые, будут добавлены  в мтарицу через пробел: ').split()))
    A.append(rows)

for i in range(sizeOfMatrix_2h):
    rows = list(map(int, input('Введите цыфры, которые, будут добавлены  в мтарицу через пробел: ').split()))
    B.append(rows)


multiResult = [[sum(a * b for a, b in zip(Arow, Bcol)) for Bcol in zip(*B)] for Arow in A]


print("The multiplication result of matrix A and B is: ")
for res in multiResult:
    print(res)

