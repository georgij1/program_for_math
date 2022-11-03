print("Программу по счёту определителя матрицы")


# Функция для счёта определителя матрицы
def determinant(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        answer = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            answer = answer + mul * determinant(m, sign * matrix[0][i])
    return answer


# Ввод кол-во строк
input_str = int(input("Введите колличество строк: "))

# Ввод кол-во столбцов
input_row = int(input("Введите колличестов столбцов: "))

matrix = []
print("Каждое число в матрице заполняется через Enter")
print()
print("Введите матрицу: ")

for i in range(input_str):
    a = []
    for j in range(input_row):
        a.append(int(input()))
    matrix.append(a)

print()
print("Введённая вами матрица:")

for i in range(input_str):
    for j in range(input_row):
        print(matrix[i][j], end=" ")
    print()

print()
# Вывод ответа на экран
print("Определитель матрицы " + str(matrix) + " = " + str(determinant(matrix, 1)))
