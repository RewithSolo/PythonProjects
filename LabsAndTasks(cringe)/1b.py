a = []
n = 1
while True:
     el = input("Введите {} элемент списка: ".format(n))
     if el == '':
         break
     else:
         a.append(int(el))
     n += 1

a.append("")
ind = int(input("Введите индекс элемента: "))
for i in range(len(a)):
    if i == ind:
        pr, a[i] = a[i], int(input("Введите значение элемента: "))
    elif i > ind:
        pr, a[i] = a[i], pr

print("Cписок: ", end="")
for i in range(len(a)):
    print(a[i], end=' ')