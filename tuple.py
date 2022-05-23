# a = ('a')
# b = ('a',)
# print(type(a), a)
# print(type(b), b)
#
# print(a.__sizeof__())
# print(b.__sizeof__())

# # Кортежи. Операция взятия индекса
# # 1. Кортеж, содержащий строки
a = ('a', 'bc', 'def', 'ghij')
# item = a[2] # item = 'def'
# print(item)
#
# # # 2. Кортеж, содержащий другой кортеж и его элементы
b = (("a", 1, 2 ,5), a[1], True)
print(b)
item = b[0] # item = ('a', 'bc', 'def', 'ghij')
item = b[1] # item = 'bc'
#
# # 3. Кортеж, содержащий список
# c = (1, [2, 3, 4], "text")
#
# # 3.1. Вытянуть список из кортежа
# item = c[1][0] # item = [2, 3, 4], с =   (1, [2, 3, 4], 'text')
# print(item)
#
# # 3.2. Список в кортеже изменяемый (mutable), поэтому его
# #      можно изменить
# c[1][1] = 8 # с = (1, [2, 8, 4], 'text')
# print(c)
#
# # Операция T[i][j] - получить элемент по индексу
# # 1. Кортеж, который содержит список
A = ( 2.5, ['a', True, 3.17], 8, False, 'z')
item1 = A[1]   # item1 =   ['a', True, 3.17]
item2 = A[1][2]  # item2 = 3.17
#
# # 2. Кортеж, который содержит строку
B = ( "Hello", "abcd", 2.55)
item1 = B[0]   # item1 =   'Hello'
item2 = B[0][4] # item2 = 'o'


#
# # 3. Кортеж, который содержит другой кортеж, список, строку
# C = ( (1, 2, 5), [2, 7, -100], "Python")
# item1 = C[0]   # item1 =   (1, 2, 5)
# item2 = C[0][2] # item2 = 5
# print(type(C))

# # 4. Три уровня вложения
# D = ( [ 7, True, ('a', 'b', 'cd')], 12, "bestprog")
# item1 = D[0]       # item1 =   [7, True, ('a', 'b', 'cd')]
# item2 = D[0][2]   # item2 =   ('a', 'b', 'cd')
# item3 = D[0][2][1] # item2 = 'b'
# #
# # Кортежи. Конкатенация +
# # Конкатенация двух кортежей
# A = (1, 2, 3)
# B = (4, 5, 6)
# C = A + B # C =   (1, 2, 3, 4, 5, 6)
# print(C)
# #
# # # Конкатенация кортежей со сложными объектами
# D = (3, "abc") *2 + (-7.22, ['a', 5]) # D = (3, 'abc', -7.22, ['a', 5])
# print(D)

#
# # Метод index - определяет позицию (индекс) элемента в кортеже
# # Заданный кортеж
# A = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
# # # Запрос к вводу названия дня недели
# day = str(input("Enter day: "))
# if day in A: # проверка, есть ли строка day в кортеже A
#     num = A.index(day)
#     print("Number of day = ", num + 1)
# else:
#     print("Wrong day.")


# # Метод count - подсчет количества вхождений элемента в кортеж
# # Заданный кортеж
A = ("ab", "ac", "ab", "ab", "ca", "ad", "jklmn")
#
d1 = A.count("ab")   # d1 = 3
d2 = A.count("jprst") # d2 = 0
d3 = A.count("ca")   # d3 = 1

print("d1 = ", d1)
print("d2 = ", d2)
print("d3 = ", d3)



# задача1
# import random
#
# a = [random.randint(1,100) for i in range(10)]
# a = tuple(a)
# print(a)
# print(a.index(min(a)),a.index(max(a)))




# Задача 2
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
#
# a = sum(C_1)
# b = sum(C_2)
#
# if a>b:
#     print('Сумма больше в кортеже C_1:', a)
# else:
#     print('Сумма больше в кортеже C_2:', b)
#
# print('Мин индекс С_1:',C_1.index(min(C_1)),'Макс индекс С_1:',C_1.index(max(C_1)))
# print('Мин индекс С_2:',C_2.index(min(C_2)),'Макс индекс С_2:',C_2.index(max(C_2)))

#Задача 3
import random

my_list = [random.randint(0, 10) for _ in range(10)]

print('Оригинальный список:', my_list)

answer = [(my_list[i_num], my_list[i_num + 1]) for i_num in range(0, len(my_list),2)]
print('Новый список:', answer)


