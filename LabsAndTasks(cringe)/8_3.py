# Соловьев Иван ИУ7-12Б
# Поиск столбца с наибольшим количеством нулей

n = int(input("Введите кол-во строк: "))        # Ввод кол-ва строк
m = int(input("Введите кол-во столбцов: "))     # Ввод кол-ва столбцов

matr = []
for i in range(n):
    str = []
    for j in range(m):              # Ввод элементов матрицы
        str.append(float(input("Введите элемент {} строки {} столбца: ".format(i + 1,j + 1))))
    matr.append(str)

print("Введенная Матрица: ")
for i in range(n):          # Вывод начальной матрицы
    for j in range(m):
        print(matr[i][j], end="   ")
    print()

a = [0] * m
for i in range(n):       # Поиск столбца с наибольшим количеством нулей
    for j in range(m):
        if matr[i][j] == 0:
            a[j] += 1
ind = a.index(max(a))

print("Подходящий столбец: ")
for i in range(n):          # Вывод полученного столбца
    for j in range(m):
        if j == ind:
            print(matr[i][j])