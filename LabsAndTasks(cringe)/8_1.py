# Соловьев Иван ИУ7-12Б
# Поиск строки с наибольшим количеством повторяющихся значений

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

maxcount = -1
ind = -1
for i in range(n):   # Поиск строки с наибольшим количеством повторяющихся значений
    count = 0
    for j in range(1, m):
        if matr[i][j] == matr[i][j-1]:
            count += 1
        else:
            if count > maxcount:
                maxcount = count
                ind = i
            count = 0
    if count > maxcount:
        maxcount = count
        ind = i

print("Полученная строка: ")    # Вывод полученной строки
for j in range(m):
    print(matr[ind][j], end="   ")

