import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import tkinter as ttk
from math import exp
from sympy import diff, symbols


def f(x):
    return ((x-1)**3)/4 + 2


roots = []
func_roots = []
roots_count = 0
a = -3
b = 8
h = 8
eps = 0.01
i_r = 1
"""
def take():
    global a, b, h, eps
    a = float(entry1.get())
    b = float(entry2.get())
    h = int(entry3.get())
    eps = float(entry4.get())
    root1.destroy()


root1 = Tk()
root1.config(bg="white")
entr = Frame(root1)
entr.pack()
entry1 = ttk.Entry(entr, width = 50, font="50")
entry1.pack(padx=8, pady= 8, ipady = 6)
entry2 = ttk.Entry(entr, width = 50, font="50")
entry2.pack(padx=8, pady= 8, ipady = 6)
entry3 = ttk.Entry(entr, width = 50, font="50")
entry3.pack(padx=8, pady= 8, ipady = 6)
entry4 = ttk.Entry(entr, width = 50, font="50")
entry4.pack(padx=8, pady= 8, ipady = 6)
ttk.Button(text="Draw", command=take).pack()
root1.mainloop()
"""


def dyho(a, b, eps):
    global i_r
    global h
    args = np.arange(a, b, eps)
    root = 0
    while abs(f(b) - f(a)) > eps and i_r < h:
        mid = (a+b)/2
        if f(mid) == 0:
            root = mid
        elif (f(a) * f(mid)) < 0:
            b = mid
        else:
            a = mid
        i_r += 1
    root = (a + b)/2
    print(f"Корень x = {root}")
    return root


dyho(a, b, eps)

plt.figure(figsize = (10,5))
x = np.linspace(a, b, 50)
#y = f(x)
plt.title("Задание 1: ")
plt.xlabel(r"$x$, Аргумент")
plt.ylabel(r"$Y(x)$, Функция")

# plt.plot(args, f(args), label='Function')
plt.plot(x, f(x))
cur = a
while cur < b:
    if abs(f(cur)) <= 0.02:
        plt.scatter(cur, f(cur), label = 'Корень', color='black', marker='x')
        roots_count += 1
        roots.append(cur)
        func_roots.append(f(cur))
    cur += 0.01
cur = a
df_sym = symbols('x')
ffc = ((df_sym-1)**3)/4 + 2
ydiff = ffc.diff(df_sym)
ydiff_sec = str(ydiff.diff(df_sym))

while cur < b:
    if abs(eval(ydiff_sec[:ydiff_sec.index("x")] + str(cur) + ydiff_sec[ydiff_sec.index("x") + 1:])) <= 0.01:
        plt.scatter(cur, f(cur), label='Перегиб', color='green')
    cur += 0.01
cur = a
min_ex = a
while cur < b:
    if f(cur) < f(min_ex):
        min_ex = cur
    cur += 0.01
# if ydiff(min_ex) < 0.000001:
plt.scatter(min_ex, f(min_ex), label = 'Минимум', color='blue')
cur = a
max_ex = a
while cur < b:
    if f(cur) > f(max_ex):
        max_ex = cur
    cur += 0.01
# if ydiff(max_ex) < 0.000001:
plt.scatter(max_ex, f(max_ex), label='Максимум', color='red')
# plt.scatter(root, f(root), label = 'Корень', color='black', marker='x')

plt.legend(loc = 'upper center')
plt.grid()

plt.show()




root1 = Tk()
frm = Frame(root1)
frm.pack()
ttk.Label(frm, text="| № Корня |").grid(row=0, column=0)
ttk.Label(frm, text="| Отрезок |").grid(row=0, column=1)
ttk.Label(frm, text="| Корень |").grid(row=0, column=2)
ttk.Label(frm, text="| Функция в корне |").grid(row=0, column=3)
ttk.Label(frm, text="| Количество итераций |").grid(row=0, column=4)
ttk.Label(frm, text="| Код ошибки |").grid(row=0, column=5)
for i in range(roots_count):
    print(roots_count)
    number_root = str(i + 1)
    range = "{} до {}".format(a, b)
    ttk.Label(frm, text=number_root).grid(row=i + 1, column=0)
    ttk.Label(frm, text=range).grid(row=i + 1, column=1)
    ttk.Label(frm, text="{:.6g}".format(roots[i])).grid(row=i + 1, column=2)
    ttk.Label(frm, text="{:.6g}".format(func_roots[i])).grid(row=i + 1, column=3)
    ttk.Label(frm, text=str(i_r)).grid(row=i + 1, column=4)
    ttk.Label(frm, text=None).grid(row=i + 1, column=5)
root1.mainloop()