a = []
n = 1
while True:
     el = input("Введите {} элемент списка: ".format(n))
     if el == '':
         break
     else:
         a.append(int(el))
     n += 1

ind = int(input("Введите индекс элемента: "))
for i in range(len(a)-1, -1, -1):
    pr = a[-1]
    if i >= ind:
        pr, a[i] = a[i], pr
print("Cписок: ", end="")
for i in range(len(a)-1):
    print(a[i], end=' ')
