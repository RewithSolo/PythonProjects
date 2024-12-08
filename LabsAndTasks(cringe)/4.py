a = []
n = 1
while True:
     el = input("Введите {} элемент списка: ".format(n))
     if el == '':
         break
     else:
         a.append(int(el))
     n += 1

conc = 0
a.append(" ")
you = []
flag = 0
for i in range(len(a)-1):

    if a[i + 1] != " ":
        if abs(a[i]) % 2 == 1 and abs(a[i + 1]) % 2 == 1 and a[i] * a[i + 1] < 0:
            flag = 1
            you.append(a[i])
        else:
            if flag == 1:
                you.append(a[i])
                flag = 0
            if conc < len(you):
                conc = len(you)
            else:
                you = []

    else:
        if flag == 1:
            you.append(a[i])

if len(you) != 0:
    print("Наиболее длинная последовательность знакочередующихся нечетных цифр: ", end="")
    for i in range(len(you)):
        print(you[i], end=' ')
else:
    print("Последовательности знакочередующихся нечетных цифр не существует(")
