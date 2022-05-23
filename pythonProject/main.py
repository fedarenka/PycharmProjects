# найти сумму чисел в множестве
total = 0
for i in range(1,5):
    total += i
print(total)

total1 = 0
i1 = 0
while i1 < 5:
    total1 += i1
    i1 += 1
print(total1)

my_list = [6, 4, 1, -3, -6]
total2 = 0
i2 = 0
while my_list[i2] > 0:
    total2 += my_list[i2]
    i2 += 1
print(total2)

my_list = [6, 4, 1, -3, -6]
total4 = 0
for i in my_list:
    if i > 0:
        total4 += i
print(total4)

my_list = [6, 4, 1, -3, -6]
total3 = 0
for i in my_list:
    if i <= 0:
        break
    total3 += i
print(total3)

total5 = 0
i5 = 0
while total5 < 20 and my_list[i5] > 0:
    total5 += my_list[i5]
    i5 += 1
print(total5)

total6 = 0
i6 = 0
while i6 < len(my_list) and my_list[i6] > 0: # до конца массива
    total6 += my_list[i6]
    i6 += 1
print(total6)

m_l = [7, 5, 4, -5, -10, -13, -15, -18]
t = 0
i = -1
while m_l[i] < 0:
    t += m_l[i]
    i += -1
print(t)

m_l = [7, 5, 4, -5, -10, -13, -15, -18]
t = 0
for a in reversed(m_l):
    if a < 0:
        t = t + a
print(t)

menu = ["картофель", "морковь", "лук", "свекла"]
i = 0
while menu[i] != "лук":
    print(menu[i])
    i += 1

menu1 = ["картофель", "морковь", "лук", "свекла"]
for i1 in menu1:
    if i1 == "лук":
        break
    print(i1)