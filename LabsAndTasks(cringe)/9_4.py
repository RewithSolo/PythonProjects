n = int(input("Введите кол-во строк матрицы D: "))        # Ввод кол-ва строк
m = int(input("Введите кол-во столбцов матрицы D: "))     # Ввод кол-ва столбцов

matr = []
for i in range(n):
    str = []
    for j in range(m):              # Ввод элементов матрицы
        str.append(float(input("Введите элемент {} строки {} столбца матрицы D: ".format(i + 1,j + 1))))
    matr.append(str)

l = []
p = int(input("Введите длину массива l: "))
for i in range(p):
    l.append(int(input("Введите {} номер строки: ".format(i+1))))

r = []
for i in range(n):
    if i in l:
        max_el = matr[i][0]
        for j in range(m):
            if max_el < matr[i][j]:
                max_el = matr[i][j]
        r.append(max_el)

rl = len(r)
sum_el = 0
for i in range(rl):
    sum_el += r[i]

sr_el = sum_el / rl

print("Конечная Матрица: ")
for i in range(n):          # Вывод полученной матрицы
    for t in range(m):
        print("{:6.4g}".format(matr[i][t]), end="   ")
    print()

for i in range(p):
    print(l[i], end="  ")
print()

for i in range(rl):
    print(r[i], end="  ")
print()

print("{:.4g} - среднее арифметическое максимальных значений".format(sr_el))