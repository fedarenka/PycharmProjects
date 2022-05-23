# # 1. строка
# s = "hello world"
# for i in s:
#     print(i)
# for l in range(len(s)):
#     print(s[l])
#
# for ind,el in enumerate(s):
#     print(ind,el)
#
#
# tup = (1,2,"a", (1,2,3,(1,2,3)),"f")
# print(tup)
# for i in range(len(tup)):
#     if type(tup[i]) != int:
#         for j in range(len(tup[i])):
#                 print(tup[i][j], end=" ")
#     else:
#         print(tup[i], end=" ")

# s1 = {4,1,51,2,1,5}
# print(s1)
# lst = [4,"hello",{5,1,2}]
# print(lst)
# if 4 in lst:
#     print("yes")
# else:
#     print("no")
#
# d = {1:"value1","key":{"key":'value'}}
# print(d)

# try:
#     s = 10/0
#     print(s)
# except TypeError:
#     print("error ;(")
# # except ZeroDivisionError:
# #     print("ZeroDivisionError")
# # else:
# #     print("else work")
# # finally:
# #     print("always work")
# except Exception as e:
#      print(type(e))

# name = input("Ведите имя - ")
# if name.capitalize() == name:
#     print("hello "+name)
# else:
#     raise NameError("name is not correct")

# with open("test.txt",'a', encoding="utf-8") as f:
#     s = input('Введите - ')
#     f.write(s+"\n")

#     print(repr(s1))
    # s1 = s1[:-1]
    # s1 = s1.rstrip()
    # s1 = s1.replace("\n"," ")
    # print(repr(s1))

# Кортеж. Вывести совершенные числа (сумма всех делителей = числу(6,28...))
# tup = (5,2,6,16,18,28,32)
# for i in range(len(tup)):
#     summa = 0
#     for j in range(1, tup[i]):
#         if tup[i] % j == 0:
#             summa+=j
#     if summa == tup[i]:
#         print(f"{tup[i]} совершенное")

#2. проверка является ли число простым
# number = int(input())
# count = 0  # счётчик делителей
# for i in range(1, number + 1):
#     if number % i == 0:
#         count += 1
# if count == 2:
#     print("простое")
# else:
#     print("не простое")
#
# #вывод строк
# # name = "ivan"
# # age = 21
# # print('name:',name.capitalize(),"age:",age)
# # print(f"name: {name.capitalize()} age: {age}")
# # print("name: {} age: {}".format(name.capitalize(),age)

# Tuple:
# 1)	Дан кортеж. Написать программу, определяющую сколько раз менялся знак в кортеже.
# import math
# import random
#
# tup = []
# for i in range(11):
#     tup.append(random.randint(-10,10))
# print(tuple(tup)) # составтиди кортеж
# l1=[]
# l2=[]
# for a in tup: # нужно убрать нули
#     if a != 0:
#         l1.append(a) # без нулей для последующего деления
#     else:
#         a = 1
#         l1.append(a)
# # print(l1,l2)
# cont = 0
# # for k in l1:
# #     m = int(math.fabs(k)/k) # модуль числа разделили на число получили чистое значение + или -
# #     l2.append(m)
# for j in range(len(l1)-1):
#     if l1[j]>0 and l1[j+1]<0 or l1[j]<0 and l1[j+1]>0 : # найти ошибку с энд
#         cont += 1
# print(cont)
# print(l2)
# for j in range(len(l2)-1):
#     if l2[j] != l2[j+1]:
#         cont+=1
# print(cont)
#
# # 2)Дан кортеж. Посчитать сумму элементов между максимальным и минимальным не включая эти элементы.
# t = tuple(list(random.randint(0, 15) for i in range(11)))
# print(t)  # составтиди кортеж
# minim = t.index(min(t))  # нашли индекс мин значения
# maxim = t.index(max(t))  # нашли индекс мак значения
# print(minim, maxim)
# if minim < maxim:
#     l = t[minim+1:maxim]
# if maxim < minim:
#     l = t[maxim + 1:minim]
# print(sum(l))

# List:
# 3)Задан список из k чисел. Определить количество инверсий в списке (т. е. таких пар элементов,
# в которых большее число находится слева от меньшего).

# q = int(input("длинна списка - "))
# lst =[random.randint(0,10) for p in range(q)]
# print(lst)
# cont=0
# for i in range(len(lst)-1):
#     if lst[i]>lst[i+1]:
#         cont+=1
# print(cont)
#
# # 4)	Дан список . Продублировать все неповторяющиеся элементы.
# lst =[random.randint(0,10) for p in range(10)]
# print(lst)
# lst.sort()
# a = []
# for i in lst:
#     el = lst.count(i)
#     if el == 1:
#         lst.append(i)
# a =  lst
# print(a)

# Set:
# 5)	Во входной строке записана последовательность чисел через пробел. Для каждого числа
# выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности
# или NO, если не встречалось.

# l = input("введите числа через пробел - ").split(' ')
# print(l)
# q = set()
# for i in l:
#     if i not in q:
#         q.add(i)
#         print("no")
#     else:
#         print("yes")

l1 = [1,2,3,4,5]
l2 = [2,4,6,7,8]
l1,l2 = set(l1), set(l2)
print(l1-l2 | l2-l1)


