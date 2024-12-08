# Соловьев Иван ИУ7-12Б
# Транспонирование матрицы

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

for i in range(n):
    for j in range(n):      # Транспонирование матрицы
        if i != j:
            matr[i][j], matr[j][i] = matr[j][i], matr[i][j]
        else:
            break

print("Конечная Матрица: ")
for i in range(n):          # Вывод полученной матрицы
    for j in range(n):
        print(matr[i][j], end="   ")
    print()