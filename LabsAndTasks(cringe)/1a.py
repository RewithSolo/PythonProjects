a = []
n = 1
while True:
     el = input("Введите {} элемент списка: ".format(n))
     if el == '':
         break
     else:
         a.append(int(el))
     n += 1

b = []
ind = int(input("Введите индекс элемента: "))
for i in range(len(a)):
    if i == ind:
        b.append(int(input("Введите значение элемента:")))
        b.append(a[i])
    else:
        b.append(a[i])
print("Измененный список: ", end="")
for i in range(len(b)):
    print(b[i], end=' ')

