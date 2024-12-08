# Соловьев Иван ИУ7-12Б
# Перестановка строк с наибольшим и наименьшим кол-вом отрицательных значений

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

minc = len(matr[0])
maxc = -1
minind = 1
maxind = 1
for i in range(n):      # Поиск индексов строки с максимальным количеством и с минимальным количеством значений < 0
    count = 0
    for j in range(m):
        if matr[i][j] < 0:
            count += 1
    if count < minc:
        minc = count
        minind = i
    if count > maxc:
         maxc = count
         maxind = i

matr[maxind], matr[minind] = matr[minind], matr[maxind]  # Перестановка элементов

print("Конечная Матрица: ")
for i in range(n):          # Вывод полученной матрицы
    for j in range(m):
        print(matr[i][j], end="   ")
    print()