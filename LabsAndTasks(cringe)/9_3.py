n = int(input("Введите кол-во строк матрицы D: "))        # Ввод кол-ва строк
m = int(input("Введите кол-во столбцов матрицы D: "))     # Ввод кол-ва столбцов

matr1 = []
for i in range(n):
    str = []
    for j in range(m):              # Ввод элементов матрицы
        str.append(float(input("Введите элемент {} строки {} столбца матрицы D: ".format(i + 1,j + 1))))
    matr1.append(str)

n = int(input("Введите кол-во строк матрицы D: "))        # Ввод кол-ва строк
m = int(input("Введите кол-во столбцов матрицы D: "))     # Ввод кол-ва столбцов

matr2 = []
for i in range(n):
    str = []
    for j in range(m):              # Ввод элементов матрицы
        str.append(float(input("Введите элемент {} строки {} столбца матрицы D: ".format(i + 1,j + 1))))
    matr2.append(str)

for i in range