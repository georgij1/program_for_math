import sys
# Умножение матриц

sizeOfMatrix_1 = int(input('Размер матрицы: '))
sizeOfMatrix_2 = int(input('Размер матрицы: '))


def Matrix_is_Square():
    all_matrix = sizeOfMatrix_1 + sizeOfMatrix_2
    if all_matrix % 2:
        valid_matrix = all_matrix % 2
        print(valid_matrix)
    else:
        print('Ваша матрица не квадратная')
        sys.exit()


Matrix_is_Square()


A = []
B = []

for i in range(sizeOfMatrix_1):
    rows = list(map(int, input('Введите цыфры, которые, будут добавлены  в мтарицу через пробел: ').split()))[:sizeOfMatrix_1]
    A.append(rows)

for i in range(sizeOfMatrix_2):
    rows = list(map(int, input('Введите цыфры, которые, будут добавлены  в мтарицу через пробел: ').split()))[:sizeOfMatrix_2]
    B.append(rows)


multiResult = [[sum(a * b for a, b in zip(Arow, Bcol)) for Bcol in zip(*B)] for Arow in A]
print("The multiplication result of matrix A and B is: ")
for res in multiResult:
    print(res)
