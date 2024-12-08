# Соловьев Иван ИУ7-12Б
# Перестановка столбцом с наибольшей и наименьшей суммой значений

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
for i in range(n):          # Поиск индекса столбца наибольшей и наименьшей суммы
    for j in range(m):
        a[j] += matr[i][j]
maxind = a.index(max(a))
minind = a.index(min(a))

for i in range(n):
    matr[i][maxind], matr[i][minind] = matr[i][minind], matr[i][maxind]  # Замена столбцов

print("Конечная Матрица: ")
for i in range(n):          # Вывод полученной матрицы
    for j in range(m):
        print(matr[i][j], end="   ")
    print()