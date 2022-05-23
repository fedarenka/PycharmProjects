# # задачи
# print("i", 'like', 'Pyhton', sep='***')
#
# name = input("введите имя -")
# print("Привет", name, sep= ", ", end='!')
#

# num = int(input('Ведите число '))
# print("Следующее число - ", num + 1, "Предыдущее число - ", num - 1)

# password1 = input("Введите пароль -")
# password_chek = input("Повторите -")
# if password1 == password_chek:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")
#
# num = int(input("Ведите 4 значное число - "))
# if 999 < num < 9999:
#     if num % 77 == 0 or num % 1717 == 0:
#         print("да")
#     else:
#         print("нет")
# else:
#         print(int(input("Вы ошиблись, введите 4 значное число - ")))

# age = int(input("Ведите возраст - "))
# sex = input("Ведите пол f или m - ")
#
# if sex == "f" and 10 <= age <= 15:
#     print("да")
# else:
#     print("нет")

# a = (input("Ведите основной цвет - "))
# b = (input("Смешиваем с - "))
# if a == "красный":
#     if a == b:
#         print("красный")
#     elif b == "синий":
#         print("фиолетовый")
#     elif b == "желтый":
#         print("оранжевый")
#     else:
#         print("ошибка цвета")
# elif a == "синий":
#     if a == b:
#         print("синий")
#     elif b == "красный":
#         print("фиолетовый")
#     elif b == "желтый":
#         print("зеленый")
#     else:
#         print("ошибка цвета")
# elif a == "желтый":
#     if a == b:
#         print("желтый")
#     elif b == "синий":
#         print("зеленый")
#     elif b == "красный":
#         print("оранжевый")
#     else:
#             print("ошибка цвета")
# else:
#     print("ошибка цвета")

# a = (input("Ведите название 1 города - "))
# b = (input("Ведите название 2 города - "))
# c = (input("Ведите название 3 города - "))
#
# s1 = min(len(a), len(b), len(c))
# s2 = max(len(a), len(b), len(c))
# if s1 == len(a):
#     print(a)
# elif s1 == len(b):
#     print(b)
# else:
#     print(c)
# if s2 == len(a):
#     print(a)
# elif s2 == len(b):
#     print(b)
# else:
#     print(c)

# a = input("введите - ")
# if "синий" in a:
#     print("цвет +")
# else:
#     print("цвет -")

# n = int(input("Длина катета - "))
# c = input("символ - ")
# for i in range(n):
#     print(c *(n-i))

# n = int(input ("введите число - "))
# for i in range(1, 11):
#     print(n, "X", i, "=", n*i)

# n = int(input("введите число - "))
# a, b = 1, 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# n = int(input('Введите число натуральное: '))
# total = 0
# summ = 0
# proizv = 1
# last = n % 10
# while n != 0:
#     last_digit = n % 10
#     total += 1
#     summ += last_digit
#     proizv *= last_digit
#     sr = summ / total
#     l = last + last_digit
#     n = n // 10
# print(summ, total, proizv, sr, last_digit, l, sep= '\n')

