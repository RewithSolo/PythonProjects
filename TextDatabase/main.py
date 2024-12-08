import os.path
import os


def max_len(file):
    with open(file, "r", encoding="cp1251") as f:
        max_lens = [0, 0, 0, 0]
        f = f.readlines()
        for i in range(len(f)):
            line = f[i].split(",")
            if len(line) != 5:
                print("База данных задана неправильно! (Количество полей отлично от 4)")
                return None
            for j in range(5):
                if j > 0:
                    max_lens[j] = max(max_lens[j], len(line[j]))
        return max_lens


def out_data(file, find_crit=None):
    allowed = True
    printed = False
    with open(file, "r", encoding='cp1251') as f:
        line = f.readline()
        while line != "":
            line = line.split(",")
            if len(line) != 4:
                print("База данных задана неправильно! (Количество полей отлично от 4)")
                return
            for i in range(4):
                if i == 1:
                    if not(line[i].isdigit()):
                        print("База данных задана неправильно! (Год введен некорректно)")
                        return
                elif i == 2:
                    if not(line[i].isdigit()):
                        print("База данных задана неправильно! (Количество лошадиных сил введено некорректно)")
                        return
                if find_crit is not None:
                    for p in find_crit:
                        if p[0] == i:
                            if line[i-1] == p[1] and allowed:
                                allowed = True
                            else:
                                allowed = False
            if allowed:
                printed = True
                print(f"|", end="")
                for i in range(4):
                    print(f"{line[i]:^{10}}|", end="")
                print()
            line = f.readline()
            allowed = True
        if not(printed):
            print("Ничего не было выведено")


def init(file, atr, line_count):
    with open(file, atr) as f:
        for i in range(line_count):
            print(f"Заполнение записи #{i+1}")
            line = []
            car = input("Введите название машины: ")
            line.append(car)
            year = input("Введите год выпуска: ")
            while not(year.isdigit()):
                year = input("Введите корректный год выпуска: ")
            line.append(year)
            hp = input("Введите количество лошадиных сил: ")
            while not (hp.isdigit()):
                hp = input("Введите корректное количество лошадиных сил: ")
            line.append(hp)
            fuel = input("Введите тип топлива: ")
            line.append(fuel)
            f.write(",".join(line))
            f.write("\n")


def menu():
    print(f"Меню действий с базой данных (в текстовом файле)")
    print(f"Доступные команды:")
    print(f"1 - Выбрать файл для работы")
    print(f"2 - Инициализировать базу данных")
    print(f"3 - Вывести содержимое базы данных")
    print(f"4 - Добавить запись в конец базы данных")
    print(f"5 - Поиск по одному полю")
    print(f"6 - Поиск по двум полям")
    print(f"0 - Завершить программу")
    n = int(input("Введите номер команды: "))
    return n


def choice(n):
    global file
    if n == 1:
        while True:
            file = input(f"Введите название файла для работы: ")
            if file == "0":
                file = None
                break
            elif not (os.path.exists(file)):
                print("Вы ввели несуществующий файл!")
                print("Если хотите вернуться к командам, напишите '0'")
            else:
                break
    elif n == 2:
        while True:
            file = input(f"Введите файл, в котором вы хотите создать бд или перезаписать его и создать новую бд: ")
            break
        while True:
            try:
                line_count = int(input("Введите количество записей: "))
                break
            except Exception:
                print("Произошла ошибка ввода данных. Вы точно ввели число?")
        init(file, "w", line_count)
    elif n == 3:
        if file is None:
            print("Вы не выбрали файл!")
        else:
            print("\n")
            len_list = max_len(file)
            if len_list is not None:
                out_data(file, len_list)
    elif n == 4:
        if file is None:
            print("Вы не выбрали файл!")
        else:
            print("\n")
            init(file, "a", 1)
    elif n == 5:
        if file is None:
            print("Вы не выбрали файл!")
        else:
            print()
            while True:
                try:
                    num = int(input("Введите номер поля (по которому совершить поиск): "))
                    if num <= 0 or num >= 5:
                        print("Пожалуйста, введите существующий номер поля! (от 1 до 4)")
                    else:
                        break
                except Exception:
                    print("Произошла ошибка ввода данных. Вы точно ввели число?")
            crit = input("Введите критерий выбранного поля, по которому необходимо найти записи: ")
            print()
            len_list = max_len(file)
            if len_list is not None:
                out_data(file, len_list, [[num, crit]])
    elif n == 6:
        if file is None:
            print("Вы не выбрали файл!")
        else:
            print()
            while True:
                try:
                    n1 = int(input("Введите номер 1-ого поля (по которому совершить поиск): "))
                    if n1 <= 0 or n1 >= 5:
                        print("Пожалуйста, введите существующий номер поля! (от 1 до 4)")
                    else:
                        break
                except Exception:
                    print("Произошла ошибка ввода данных. Вы точно ввели число?")
            crit1 = input("Введите критерий 1-ого поля, по которому необходимо найти записи: ")
            print()
            while True:
                try:
                    n2 = int(input("Введите номер 2-ого поля (по которому совершить поиск): "))
                    if n2 <= 0 or n2 >= 5:
                        print("Пожалуйста, введите существующий номер поля! (от 1 до 4)")
                    elif n2 == n1:
                        print("Пожалуйста, введите другой номер поля! (отличный от первого)")
                    else:
                        break
                except Exception:
                    print("Произошла ошибка ввода данных. Вы точно ввели число?")
            crit2 = input("Введите критерий 2-ого поля, по которому необходимо найти записи: ")
            len_list = max_len(file)
            if len_list is not None:
                out_data(file, len_list, [[n1, crit1], [n2, crit2]])
    elif n == 0:
        os._exit(0)


def main():
    while True:
        n = menu()
        choice(n)


file = None
main()
