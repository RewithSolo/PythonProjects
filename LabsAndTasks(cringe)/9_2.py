n = int(input("Введите размер квадратной матрицы: "))
matr = []
for i in range(n):
    str = []
    for j in range(n):
        str.append(int(input("Введите элемент {} строки {} столбца: ".format(i + 1, j + 1))))
    matr.append(str)

print("Начальная Матрица: ")
for i in range(n):  # Вывод полученной матрицы
    for j in range(n):
        print("{:4}".format(matr[i][j]), end="   ")
    print()

matr.reverse()
for i in range(n):
    for j in range(i):
        matr[i][j], matr[j][i] = matr[j][i], matr[i][j]

print("Конечная Матрица: ")
for i in range(n):  # Вывод полученной матрицы
    for j in range(n):
        print("{:4}".format(matr[i][j]), end="   ")
    print()
