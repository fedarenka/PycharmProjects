# Задание 1
wilet = input("Введите город вылета: ")
prilet = input("Введите город прилета: ")
print(wilet, "-", prilet)

# Задание 2
a = input("Введите строку : ")
print(a.title())

# Задание 3
import random

a = random.randint(1, 10)

s = 1
while s <= 10:
    p = int(input("введите число от 1 до 10:  "))
    if p == a:
        print("Вы угадали! Число попыток: ", s)
        break
    elif p > a:
        print("Число больше. Попробуйте еше раз")
    elif p < a:
        print("Число меньше. Попробуйте еше раз")
    s +=1
else:
    print("Вы не угадали, выигрышная комбинация ", a, b)

# Задание 4
a = int(input("Введите количество должников: ")
b = 0
while b <= a:
    print("должник ", b)
    print("сколько должны")
    a+=5
