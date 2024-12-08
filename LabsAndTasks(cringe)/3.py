a = []
n = 1
while True:
     el = input("Введите {} элемент списка: ".format(n))
     if el == '':
         break
     else:
         a.append(int(el))
     n += 1

k = int(input("Введите значение K: "))
extra = []
for i in range(1, len(a)-1):
    if (a[i - 1] < a[i] and a[i + 1] < a[i]) or (a[i - 1] > a[i] and a[i + 1] > a[i]):
        extra.append(a[i])
if len(extra) < k:
    print("Значение K превосходит количество всех эстремумов в списке")
else:
    print("Значение K-го экстремума в списке: {}".format(extra[k]))