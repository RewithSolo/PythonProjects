# Соловьев Иван ИУ7-12Б

from math import sin
print("Ввод первого массива D ")
j = int(input("Введите длину массива D: "))
d = []
for i in range(j):
    d.append(float(input("Введите {} элемент массива D: ".format(i + 1))))

print("Ввод второго массива F ")
k = int(input("Введите длину массива F: "))
f = []
for i in range(k):
    f.append(float(input("Введите {} элемент массива F: ".format(i + 1))))

AV = []
matr = []
for i in range(j):
    str = []
    sr = 0
    for t in range(k):
        el = sin(d[i] + f[t])
        sr += el
        str.append(el)
    AV.append(sr / k)
    matr.append(str)

L = []
for i in range(j):
    count = 0
    for t in range(k):
        if AV[i] > matr[i][t]:
            count += 1
    L.append(count)

print("Конечная Матрица: ")
for i in range(j):          # Вывод полученной матрицы
    for t in range(k):
        print("{:6.4g}".format(matr[i][t]), end="   ")
    print("{:6.4g}".format(AV[i]), end="   ")
    print(L[i])