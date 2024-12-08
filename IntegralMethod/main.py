import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk

a = 0
b = 0
h = 0
eps = 0


def take():
    global a, b, h, eps
    a = float(entry1.get())
    b = float(entry2.get())
    h = int(entry3.get())
    eps = float(entry4.get())
    root1.destroy()


def f(x):
    return x**2 - 10


root1 = Tk()
root1.title("Ввод данных")
frame = Frame(root1)
frame.pack()
entry1 = ttk.Entry(frame, width = 50, font="50")
entry1.insert(0, 'a')
entry1.pack(padx=8, pady= 8, ipady = 6)
entry2 = ttk.Entry(frame, width = 50, font="50")
entry2.insert(0, 'b')
entry2.pack(padx=8, pady= 8, ipady = 6)
entry3 = ttk.Entry(frame, width = 50, font="50")
entry3.insert(0, 'h')
entry3.pack(padx=8, pady= 8, ipady = 6)
entry4 = ttk.Entry(frame, width = 50, font="50")
entry4.insert(0, 'eps')
entry4.pack(padx=8, pady= 8, ipady = 6)
ttk.Button(text="Draw", command=take).pack()
root1.mainloop()


def dyho(a, b, eps):
    args = np.arange(a, b, eps)
    root = 0
    while abs(f(b)-f(a)) > eps:
        mid = (a+b)/2
        if f(mid) == 0:
            root = mid
        elif (f(a) * f(mid)) < 0:
            b = mid
        else:
            a = mid
    root = (a+b)/2
    print(f"Корень x = {root}")
    plot(args, root)


def plot(args, root):
    plt.figure(figsize = (10,5))
    x = np.linspace(a, b, 50)
    y = f(x)
    plt.title("График функции: ")
    plt.xlabel(r"$x$, Аргумент")
    plt.ylabel(r"$Y(x)$, Функция")

    plt.plot(args, f(args), label='Function')
    plt.plot(x, y)
    plt.scatter(root, f(root), label = 'Корень функции', color='black', marker='x')

    plt.legend(loc = 'upper center')
    plt.grid()

    plt.show()


dyho(a, b, eps)

