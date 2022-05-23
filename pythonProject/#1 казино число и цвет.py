#6 казино, 5 попытоу угадать число (от 1 до 10) и цвет черный или красный
import random
a = random.randint(1,10)
b = random.randint(1,2)
if b == 1:
    с = "красный"
else:
    с = "черный"
i = 0
while i < 5:
    x = int(input("Ввидите число от 1 до 10 - "))
    y = (input("Ввидите цвет: черный или красный - "))
    if x != a and с != y:
        print("Вы не угадали, попробуйте еще раз")
    elif x == a and с == y:
        print("Вы выиграли")
        break
    i += 1
print("номер - ", a, "цвет - ", с)
