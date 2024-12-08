from math import log
bg = float(input("Введите начало отрезка интегрирования: "))
fn = float(input("Введите конец отрезка интегрирования: "))
n1 = int(input("Введите количество участков разбиения N1: "))
n2 = int(input("Введите количество участков разбиения N2: "))
step2 = (bg + fn) / n2
step1 = (bg + fn) / n1
# y = log(x)
# Метод прямоугольников n1
p = bg
l1 = 0
while fn > p:  # n1
    t = log(p) * step1
    l1 += t
    p += step1

p = bg
l2 = 0
while fn > p:   # n2
    t = log(p) * step2
    l2 += t
    p += step2

# Метод трапеций n1
p = bg
l3 = 0
while fn > p:  # n1
    t = (log(p+step1) + log(p)) * step1 / 2
    l3 += t
    p += step1

p = bg
l4 = 0
while fn > p:   # n2
    t = (log(p+step2) + log(p)) * step2 / 2
    l4 += t
    p += step2

print(l1, l2, l3, l4)
