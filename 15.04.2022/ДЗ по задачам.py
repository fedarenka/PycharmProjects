# print("I", "like", "Phyton", sep="***", end='!')

# name = input("Введите имя - ")
# print("Привет", name, sep=", ", end='!')

# n = int(input("Ведите целое число - "))
# print("Предыдущее число - ", n - 1, "Следующее число - ", n + 1)

# m = 41 # всего яблок
# n = 3 # вместительность ящиков
# k = m // n # колтчество ящиков необходимо
# o = m % n # яблок останется
# print("Количество ящиков - ", k,",", "останется фруктов - ", o, "т")

# n = int(input("Ведите номер - ")) # последняя цифра - номер дома, остальные - номер квартиры
# kv = n // 10
# d = n % 10
# print("номер квартиры - ", kv, ",", "номер дома - ", d)

# s = 299
# k = s // 100 # полных кругов
# ko = s % 100 # метров следующего круга
# print("Спортсмен пробежал полных кругов - ", k, ",", "метров неполного круга - ", ko)

# n = input("Введите пароль из 4 символов - ")
# n1 = input("Подтвердите пароль - ")
# if n == n1:
#     print("Пароль принят")
# else:
#     print("Пароль введен не верно")

# n = int(input("Введите 4 значное число - "))
# if 999 < n < 9999:
#     if n % 77 == 0 or n % 1717 == 0:
#         print(n, "- число красивое")
#     else:
#         print(n, "- число НЕкрасивое")
# else:
#     print(n, "- число НЕ 4 значное")

# col1 = input("Введите цвет: red, blue, yellow - ")
# col2 = input("Введите цвет: red, blue, yellow - ")
# if col1 == "red":
#     if col2 == "red":
#         print("получился цвет - ", "красный")
#     elif col2 == "blue":
#         print("получился цвет - ", "фиолетовый")
#     elif col2 == "yellow":
#         print("получился цвет - ", "оранжевый")
#     else:
#         print("цвет введен неверно")
# elif col1 == "blue":
#     if col2 == "yellow":
#         print("получился цвет - ", "зеленый")
#     elif col2 == "red":
#         print("получился цвет - ", "фиолетовый")
#     elif col2 == "blue":
#         print("получился цвет - ", "синий")
#     else:
#         print("цвет введен неверно")
# elif col1 == "yellow":
#     if col2 == "yellow":
#         print("получился цвет - ", "желтый")
#     elif col2 == "red":
#         print("получился цвет - ", "оранжевый")
#     elif col2 == "blue":
#         print("получился цвет - ", "зеленый")
#     else:
#         print("цвет введен неверно")
# else:
#     print("цвет введен неверно")

# n = (int(input("Введите число от 0 до 36 - ")))
# if n == 0:
#     print("зеленый")
# elif 1 <= n <= 10:
#     if n % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# elif 11 <= n <= 18:
#     if n % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# elif 19 <= n <= 28:
#     if n % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# elif 29 <= n <= 36:
#     if n % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# else:
#     print("ошибка")

# a = int(input("Введите балл за 1 экзамен - "))
# b = int(input("Введите балл за 2 экзамен - "))
# c = int(input("Введите балл за 3 экзамен - "))
# if a + b + c >= 270:
#     print("поступил")
# else:
#     print("не поступил")

# s1 = input("Введите название города 1 - ")
# s2 = input("Введите название города 2 - ")
# s3 = input("Введите название города 3 - ")
# sk = min(len(s1), len(s2), len(s3))
# if sk == len(s1):
#     print("самое короткое название -", s1)
# elif sk == len(s2):
#     print("самое короткое название -", s2)
# else:
#     print("самое короткое название -", s3)
# sd = max(len(s1), len(s2), len(s3))
# if sd == len(s1):
#     print("самое длинное название -", s1)
# elif sd == len(s2):
#     print("самое длинное название -", s2)
# else:
#     print("самое длинное название -", s3)

# l = ["красный", "синий", "зелёный"]
# if "синий" in l:
#     print("yes")
# else:
#     print("no")

# mail = "fedarenka@mail.ru"
# if "@" and "." in mail:
#     print("yes")
# else:
#     print("no")

# deys = ["понедельник", "вторник", "среда", "четверг", "суббота", "воскресенье"]
# if "суббота" and "воскресенье" in deys:
#     print("yes")
# else:
#     print("no")

# n = 3 #int(input("Введите длинну катета - "))
# a = "@"
# for i in range(n):
#     b = a * (n - i)
#     print(b)

# n = 1 #int(input("Введите длинну катета - "))
# for i in range(0,11):
#     b = "*" * (n + i)
#     print(b)

# n = 5 #int(input("Введите длинну катета - "))
# for i in range(0, n):
#     b = "*" * (i+1)
#     print(b)

# m = 10
# n = 10
# if m < n:
#     for i in range(m, n+1):
#         print(i, end=', ')
# if n < m:
#     for i in range(m, n+1, -1):
#         print(i, end=', ')
# if n == m:
#     print(m, "=", n)

# for i in range (1, 11):
#     for j in range (1, 11):
#         c = i * j
#         print(j, "X", i, "=", c, end="   ")
#     print()

# m = int(input("Число - "))
# for i in range(1, 11):
#     print(i, "X", m, "=", i * m)

# m = int(input("Число - "))
# a,b = 1,1
# for i in range(m):
#     print(a, end=", ")
#     a,b = b, (a + b)

# n = 9876 # int(input("Число - "))
# # n1 = str(123)
# # a,b,c = int(n1[0]), int(n1[1]), int(n1[2])
# # print(a+b+c)
# tot = 0 # количество цифр
# summa = 0 # сумма цифр
# proizv = 1 # произведение цифр
# last = n % 10 # последняя цифра вне цикла
# while n !=0:
#     last1 = n % 10 # последняя цифра в цикле, последний раз станет первой, после чего цикл завершиться
#     summa += last1 # сумма всех последних цифор в цикле (с последней до перавой)
#     tot +=1 # (сумма знаков - проходов цикла)
#     proizv *= last1 # (произведение)
#     sr_pr = summa / tot # (среднее арифметическое)
#     summa_last1 = last1 + last # первая цифра по посдеднему проходу = первая цифра
#     n = n // 10 # условие окончания цикла
# print(summa, tot, proizv, sr_pr, last1, summa_last1, sep="\n")

# n = int(input("Число - "))
# if 11 < n:
#     for i in range(11, n+1):
#         if 55 <= i <= 99 or 1717 <= i <= 3737 or 7878 <= i <= 8787:
#             continue
#         print(i)

# n = 5 # int(input("Число - "))
# for i in range(1,10):
#     for j in range(1,10):
#         print(i, "+", j, "=", i+j, end="   ")
#     print()

# n = int(input("Первое число - "))
# m = int(input("Второе число - "))
# s = 0 # сумма чисел
# s_a = 0 # среднее арифметическое
# z = 0 # количество цифр в ряду
# for i in range(n, m+1):
#     if i % 3 == 0:
#         z += 1
#         s += i
#         s_a = s / z
# print("сумма чисел равна - ", s,",", "среднее арифметическое чисел равно - ", s_a)

s = "I lake Phyton"
# print(s) # дано
# print(s.swapcase()) #меняет большие в маленьеие и наоборот
# print(s.lower()) # все маленькие
# print(s.upper()) # все большие
# print(s.capitalize()) # первая большая, остальные маленьеие
# print(s.title()) # первая всех слов большая, остальные маленьеие

# lower_cont = 0 # счетчик маленьких букв
# upper_cont = 0
# for i in range(len(s)):
#     if s[i] in "abcdefghijklmnopqrstuvwxyz":
#         lower_cont += 1
#     if s[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         upper_cont += 1
# print("строчных букв - ", lower_cont, "заглавных букв - ", upper_cont)

# c = "123456789"
# print(c.replace("1","one"))
# b = "1"
# a = "one"
# for i in c:
#     if i!=b:
#         a +=i
# print(a)
#
# print(c[1:6])
# print(len(c))

# num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
# print(num[0:6])
#
# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# print("минимальное значение - ", min(numbers),",", "максимальное значение - ", max(numbers))

# n = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# l = len(n)
# summ = sum(n)
# print("Среднее арифметическое = ", summ/l)

# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3], rainbow[6]  = "зеленый", "фиолетовый"
# print(rainbow)

# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# languages.reverse()
# print(languages)

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print("длинна списка - ", len(numbers),", последний элемент списка -", numbers[-1])
# print(numbers[-1::-1]) # список наоборот от последнего до первого значения
# print(numbers[::-1]) # список наоборот от первого значения до последнего в обратном порядке
# numbers.reverse() # список наоборот от последнего до первого значения
# print(numbers) # список наоборот переприсватвание
# a = numbers.count(5) # посчитать 5
# b = numbers.count(17) # посчитать 17
# if a > 1 and b > 1:
#     print("yes", a, b)
# else:
#     print("no", a, b)
# numbers.pop(0) # удалить первый элемент
# numbers.pop() # удалить последний элемент по умолчанию
# print(numbers) # переприсваивание

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# kv = [i**2 for i in numbers]
# print(kv)
# print(sum(kv))

# numbers = [8, 9, 10, 11]
# numbers[1] = 17 # заменить элемент с № 1 на 17
# l = [4,5,6]
# # numbers.append([4,5,6]) # вставить списком
# numbers.extend(l) # вставить из списка
# numbers.pop(0)
# numbers[3] = 25
# numbers.sort()
# numbers.sort(reverse=True)
# print(numbers*2)

# 10. Напишите программу, используя List Comprehension, так чтобы получить новый список, содержащий длины строк
# исходного списка.

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# l_keywords = [len(i) for i in keywords]
# print(l_keywords)

# for i in range(1,10):
#     i -= 5
# print(i)

# i = 0
# while i < 10:
#     i += 1
#     print(i)
# i -= 10
# print(i)

