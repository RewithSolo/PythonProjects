while True:

    x = float(input("Введите X координату: "))
    y = float(input("Введите Y координату: "))

    line1 = y <= -1/8 *(x + 9) ** 2 + 8
    line2 = y <= -1/8 *(x - 9) ** 2 + 8
    line3 = y <= 7 * (x + 8) ** 2 + 1
    line4 = y <= 7 * (x - 8) ** 2 + 1
    line5 = y <= 1/49 * (x + 1) ** 2
    line6 = y <= 1/49 * (x - 1) ** 2
    line7 = y <= -4 * x ** 2 + 2
    line8 = y <= 4 * x ** 2 - 6
    line9 = y <= -4/49 * (x + 1) ** 2
    line10 = y <= -4/49 * (x - 1) ** 2
    line11 = y <= 1/3*(x + 5) ** 2 - 7
    line12 = y <= 1/3*(x - 5) ** 2 - 7
    line13 = y <= -2 * (x + 1) ** 2 - 2
    line14 = y <= -2 * (x - 1) ** 2 - 2
    line15 = y == 3/2*abs(x) + 2

    if line15:
        print("Точка на рожках бабочки")
    elif line1 and not line5 and -8 <= x <= -1 or not line3 and line1 and -9 <= x <= -8:
        print("Точка в верхней части левого крыла")
    elif line2 and not line6 and 1 <= x <= 8 or not line4 and line2 and 8 <= x <= 9:
        print("Точка в верхней части правого крыла")
    elif line7 and not line8:
        print("Точка в теле бабочки")
    elif line9 and not line11 and not line13:
        print("Точка лежит в нижней части левого крыла")
    elif line10 and not line12 and not line14:
        print("Точка лежит в нижней части правого крыла")
    else:
        print("Точка не лежит на бабочке")
