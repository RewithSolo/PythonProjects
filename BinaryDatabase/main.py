import struct


def set():  # Выбор файла
    name = input("Введите адрес файла: ")
    return name


def init(file_name):  # Создание БД
    while True:
        try:
            f = open(file_name, 'wb')
            num = int(input("Введите количество записей: "))
        except OSError:
            print("Некорректный путь к файлу")
            return -1
        except ValueError:
            print("Пожалуйста введите целое число")
        else:
            break
    for i in range(num):
        print(f"{i + 1}-я запись:")
        person = check_fields()
        f.write(person)
    f.close()


def out(file_name):  # Вывод БД
    try:
        f = open(file_name, 'rb')
    except OSError:
        print("Файл не найден")
        return -1
    except Exception:
        print("Некорректный путь к файлу")
        return -1
    if check_if_bd(f):
        prnt(f)
    f.close()


def insert(file_name):  # Вставка в БД
    try:
        f = open(file_name, 'r+b')
    except OSError:
        print("Файл не найден")
        return -1
    except Exception:
        print("Некорректный путь к файлу")
        return -1
    if f.read(44) == b'':
        res_check = (True, 0)
    else:
        f.seek(0)
        res_check = check_if_bd(f, True)
    if res_check[0]:
        while True:
            try:
                n = int(input(f"Введите номер позиции(1-{res_check[1] + 1}): ")) - 1
            except ValueError:
                print("Пожалуйста, введите целое число")
            else:
                if not (0 <= n <= res_check[1]):
                    print("Позиция некорректна")
                    continue
                break
        person = check_fields()
        f.seek(44 * n)
        line = f.read(44)
        while line:
            f.seek(-44, 1)
            f.write(person)
            person = line
            line = f.read(44)
        f.write(person)
    f.close()


def delete(file_name):  # Удаление позиции
    try:
        f = open(file_name, 'r+b')
    except OSError:
        print("Файл не найден")
        return -1
    except Exception:
        print("Некорректный путь к файлу")
        return -1
    res_check = check_if_bd(f, True)
    if res_check[0]:
        while True:
            try:
                n = int(input(f"Введите номер позиции(1-{res_check[1]}): "))
            except ValueError:
                print("Пожалуйста, введите целое число")
            else:
                if not (0 < n <= res_check[1]):
                    print("Позиция некорректна")
                    continue
                break
        f.seek(n * 44)
        line = f.read(44)
        while line:
            f.seek(-88, 1)
            f.write(line)
            f.seek(44, 1)
            line = f.read(44)
        f.seek(-44, 1)
        f.truncate()
    f.close()


def search_on_one(file_name):  # Поиск по одному полю
    try:
        f = open(file_name, 'rb')
    except OSError:
        print("Файл не найден")
        return -1
    except Exception:
        print("Некорректный путь к файлу")
        return -1
    if check_if_bd(f):
        print("Выберите поле:\n1)Имя\n2)Год рождения\n3)Балл\n4)Допуск")
        while True:
            try:
                u_inp = int(input("-->")) - 1
            except ValueError:
                print("Введите номер поля")
            else:
                if not (0 <= u_inp <= 3):
                    print("Введите номер поля")
                    continue
                break
        val = input("Искомое значение: ")
        print("Результат:")
        was_changed = False
        res = []
        line = f.read(44)
        while line:
            temp = ['', 0, 0, '']
            fields = struct.unpack("30s H H  10s", line)
            temp[0] = fields[0].decode().rstrip("\x00")
            temp[1] = str(fields[1])
            temp[2] = str(fields[2])
            temp[3] = fields[3].decode().rstrip("\x00")
            if temp[u_inp] == val:
                res.append(temp)
                was_changed = True
            line = f.read(44)
        if not was_changed:
            print("Подходящих записей нет")
        else:
            prnt_arr(res)
    f.close()


def search_on_two(file_name):  # Поиск по двум полям
    try:
        f = open(file_name, 'rb')
    except OSError:
        print("Файл не найден")
        return -1
    except Exception:
        print("Некорректный путь к файлу")
        return -1
    if check_if_bd(f):
        print("Выберите поле:\n1)Имя\n2)Год рождения\n3)Балл\n4)Допуск")
        while True:
            try:
                u_inp1 = int(input("-->")) - 1
            except ValueError:
                print("Введите номер поля")
            else:
                if not (0 <= u_inp1 <= 3):
                    print("Введите номер поля")
                    continue
                break
        val1 = input("Искомое значение: ")
        print("Выберите второе поле:")
        while True:
            try:
                u_inp2 = int(input("-->")) - 1
            except ValueError:
                print("Введите номер поля")
            else:
                if not (0 <= u_inp2 <= 3):
                    print("Введите номер поля")
                    continue
                if u_inp2 == u_inp1:
                    print("Введите номер отличный от первого")
                    continue
                break
        val2 = input("Искомое значение: ")
        print("Результат:")
        was_changed = False
        res = []
        line = f.read(44)
        while line:
            temp = ['', 0, 0, '']
            fields = struct.unpack("30s H H 10s", line)
            temp[0] = fields[0].decode().rstrip("\x00")
            temp[1] = str(fields[1])
            temp[2] = str(fields[2])
            temp[3] = fields[3].decode().rstrip("\x00")
            if temp[u_inp1] == val1 and temp[u_inp2] == val2:
                res.append(temp)
                was_changed = True
            line = f.read(44)
        if not was_changed:
            print("Подходящих записей нет")
        else:
            prnt_arr(res)
    f.close()


def check_if_bd(f, count_lines=False):  # Проверка БД на правильность
    cnt = 0
    if f.read(44) == b'':
        print("Файл пуст")
        if count_lines:
            return False, cnt
        return False
    f.seek(0)
    try:
        line = f.read(44)
        while line:
            struct.unpack("30s H H  10s", line)
            cnt += 1
            line = f.read(44)
    except Exception:
        print("Неверный формат базы данных")
        if count_lines:
            return False, cnt
        return False
    else:
        f.seek(0)
        if count_lines:
            return True, cnt
        return True


def prnt(f):  # Вывод файла
    if f.read(44) == b'':
        print("Файл пуст")
    else:
        f.seek(0)
        print(f"{'-' * 64}\n{'Имя'.center(20)}|{'Год рождения'.center(15)}|"
              f"{'Балл'.center(15)}|{'Допущен'.center(10)}\n{'-' * 64}")
        line = f.read(44)
        while line:
            fields = struct.unpack("30s H H 10s", line)
            name = fields[0].decode().rstrip("\x00")
            year = str(fields[1])
            res = str(fields[2])
            passd = fields[3].decode().rstrip("\x00")
            print(f"{name.center(20)}|{year.center(15)}|{res.center(15)}|{passd.center(10)}")
            line = f.read(44)
        print(f"{'-' * 64}")


def prnt_arr(arr):  # Вывод массива
    print(f"{'-' * 64}\n{'Имя'.center(20)}|{'Год рождения'.center(15)}|"
          f"{'Балл'.center(15)}|{'Допущен'.center(10)}\n{'-' * 64}")
    for line in arr:
        name = line[0]
        year = line[1]
        res = line[2]
        passd = line[3]
        print(f"{name.center(20)}|{year.center(15)}|{res.center(15)}|{passd.center(10)}")
    print(f"{'-' * 64}")


def check_fields():  # Ввод полей
    while True:
        try:
            pname = input("Введите имя (Имя Ф.): ").encode('utf-8')
            if len(pname) > 30:
                print("Превышена максимальная длина строки")
                continue
            pyear = int(input("Введите год рождения: "))
            pres = int(input("Введите результат экзамена: "))
            ppassed = input("Допущен (Да/Нет): ").encode('utf-8')
            if len(ppassed) > 10:
                print("Превышена максимальная длина строки")
                continue
            person = struct.pack("30s H H 10s", pname, pyear, pres, ppassed)
        except Exception:
            print("Некорректные данные, повторите ввод")
        else:
            return person


def menu():
    file_name = ""
    while True:
        print("\nМеню")
        print("1) Выбрать файл для работы\n"
              "2) Инициализировать базу данных\n"
              "3) Вывести содержимое базы данных\n"
              "4) Добавить запись в произвольное место базы данных\n"
              "5) Удалить произвольную запись из базы данных\n"
              "6) Поиск по одному полю\n"
              "7) Поиск по двум полям\n"
              "9) Очистить ввод\n"
              "0) Выход")
        user_input = input("Ввод-->")
        if user_input == "1":
            file_name = set()
        elif user_input == "2":
            init(file_name)
        elif user_input == "3":
            out(file_name)
        elif user_input == "4":
            insert(file_name)
        elif user_input == "5":
            delete(file_name)
        elif user_input == "6":
            search_on_one(file_name)
        elif user_input == "7":
            search_on_two(file_name)
        elif user_input == "9":
            clear = "\n" * 100
            print(clear)
        elif user_input == "0":
            break
        else:
            print("Некорректный ввод, пожалуйста введите номер операции\n")


def main():
    menu()


main()