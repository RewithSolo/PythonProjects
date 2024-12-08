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
for i in range(len(a)):
    if a[i] % 2 != 0:
        b.append(a[i])

print("Список: ", end="")
for i in range(len(b)):
    print(b[i], end=' ')