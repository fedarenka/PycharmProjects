# Список из 7 цифр. Если четных больше, чем нечетных, то найти сумму(произведение) всех цифр, инче произведение 1,3 и 6 элемента
import random
a1 = [] # наш рандомный список
a_ch = [] # список четных
a_nch = [] # список нечетных
pr = 1 # произведение
for i in range(7):
    a1.append(random.randint(10,111))
print(a1)
for j in a1:
    if j % 2 == 0:
        a_ch.append(j)
    else:
        a_nch.append(j)
print(a_ch, len(a_ch), a_nch, len(a_nch))
if len(a_ch) > len(a_nch):
    print("сумма всех цифр ",sum(a1))
    for p in a1:
        pr *= p
    print("произведение всех цифр ", pr)
else:
    print("произведение 1,3 и 6 элемента ", a1[0]*a1[2]*a1[5])
