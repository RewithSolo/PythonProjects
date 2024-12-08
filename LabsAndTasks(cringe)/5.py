a = []
n = 1
while True:
     el = input("Введите {} элемент списка: ".format(n))
     if el == '':
         break
     else:
         a.append(int(el))
     n += 1

max_el = max(a)
max_el_ind = a.index(max_el)
p = -1
p_ind = -1
for i in range(len(a)):
    if a[i] % 2 == 0:
        p = a[i]
        p_ind = i
        break
if max_el <= 0 and p == -1:
    print("Максимального положительного или четного числа нет в списке.")
else:
    a[max_el_ind], a[p_ind] = a[p_ind], a[max_el_ind]
print("Cписок: ", end="")
for i in range(len(a)):
    print(a[i], end=' ')