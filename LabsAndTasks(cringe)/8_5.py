# Соловьев Иван ИУ7-12Б
# Поиск максимального элемента над главной диагональю
# Поиск минимального элемента под побочной диагональю

n = int(input("Введите размер квадратной матрицы: "))        # Ввод размера матрицы
matr = []
for i in range(n):
    str = []
    for j in range(n):              # Ввод элементов матрицы
        str.append(float(input("Введите элемент {} строки {} столбца: ".format(i + 1, j + 1))))
    matr.append(str)

print("Введенная Матрица: ")
for i in range(n):          # Вывод начальной матрицы
    for j in range(n):
        print(matr[i][j], end="   ")
    print()

maxel = -1
minel = matr[n - 1][n - 1]
for i in range(n):          # Поиск максимального и минимального
    for j in range(n):
        if j > i:
            maxel = max(matr[i][j], maxel)
        if j > n - i - 1:
            minel = min(matr[i][j], minel)

print("Максимальный элемент над главной диагональю - {}".format(maxel))  # Вывод
print("Минимальный элемент под побочной диагональю - {}".format(minel))