# print("I", "like", 'Python', sep='***')

# name = input('Ввести имя: ')
# print('Привет', name, sep=', ', end='!')

# num = int(input('Ввести число: '))
# print('Следующее число:', num + 1)
# print('Предыдущее число:', num - 1)

# password1 = input('Введите пароль: ')
# password_check = input('Повторите: ')
# if password1 == password_check:
#     print('Пароль принят')
# else:
#     print('Пароли отличаются')

# num = int(input('Введите четырехзначное число: '))
# if   999 < num <= 9999:
#     if num % 77 == 0 or num % 1717 == 0:
#         print('YES')
#
#         print('NO')
# else:
#     num = int(input('Вы ошиблись! Введите четырехзначное число: '))

#Футбольная команда
# sex = input('Введите пол f - если жен, m - муж: ')
# age = int(input('Введите возраст: '))
# if sex == "f" and 10 <= age <= 15:
#     print("YES")
# else:
#     print("NO")

#Смешиваем цвета
# a = input('Введите основной цвет: ')
# b = input('С чем смешиваем: ')
#
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
#         print("ошибка цвета")
# else:
#     print("ошибка цвета")




#Рулетка
# if 0 <= a <= 10:
#     if a == 0:
#         print("зеленый")
#     elif a % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# elif 11 <= a <= 18:
#     if a % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# elif 19 <= a <= 28:
#     if a % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# elif 29 <= a <= 36:
#     if a % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# else:
#     print("ошибка ввода")
#
# a = input('Введите первое название города: ')
# b = input('Введите второе название города: ')
# c = input('Введите третье название города: ')
#Самое короткое и длиное название города
# s1 = min(len(a), len(b), len(c)) #3
# s2 = max(len(a), len(b), len(c)) #7
#
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

# a = input('Введите строку ')
# if 'синий' in a:
#     print('Цвет есть')
# else:
#     print('нет')

# Адрес почты
# a = input()
# if "@" in a and "." in a:
#     print("YES")
# else:
#     print("NO")

#треугольник
# n = int(input('Длина катета треугольника: '))
# c = input('Символ: ')
# for i in range(n):
#     print(c * (n-i))


#треугольник равнобедренный
# n = int(input())
# for i in range(1, n + 1):
#     print(i * '*')
# for j in range(n - 1, 0, -1):
#     print(j * '*')


#Выводим числа по возрастанию
# m, n = int(input()), int(input())
# if m < n:
#     for i in range(m,n+1):
#         print(i)
# elif m == n:
#     print(m or n)
# else:
#     for i in range(m, n-1, -1):
#         print(i)

#таблица умнижения
# n = int(input('Число на которое умножаем: '))
# for i in range(1,11):
#     print(n, "x", i, "=", n*i)


#Фибоначи
# n = int(input())
# a, b = 1, 1
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b


#Сумма, кол-во, произведение, среднее арифметическое, первая цифра
n = int(input('Введите число натуральное: '))
total = 0
summ = 0
proizv = 1
last = n % 10
while n != 0:
    last_digit = n % 10
    total += 1
    summ += last_digit
    proizv *= last_digit
    sr = summ / total
    l = last + last_digit
    n = n // 10
print(summ, total, proizv, sr, last_digit, l, sep = "\n")

#Вывод чисел за исключением
# n = int(input())
# for i in range(1, n+1):
#     if 5<=i<=9:
#         continue
#     if 17<=i<=37:
#          continue
#     if 78<=i<=87:
#          continue
#     print(i)

#Дано натуральное число n, (n≤9).
#Напишите программу, которая печатает таблицу сложения
# для всех чисел от 11 до n в соответствии с примером.

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, '+', j, "=", i + j, end="\n")
#     print()


# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# summ = 0
# count = 0
# for i in range(a, b+1):
#   if i % 3 == 0:
#     summ += i
#     count += 1
# print(summ / count, "- среднее арифметическое чисел, кратных 3ем, на отрезке от", a, "до", b)
#
