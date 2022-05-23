# Tuple:
#     1) Дан кортеж. Написать программу, определяющую сколько раз менялся знак в кортеже.
# t = (-1, 2, 9, -1, -2, 0)
# change_count = 0
# for i in range(len(t)-1): # i принимает занчение до индекса предпоследнего элемента
#     if (t[i] > 0 and t[i+1] < 0) or (t[i] < 0 and t[i+1] > 0): # сравниваем знак текущего элемента со следующим
#         change_count += 1
# print(change_count)
#     2) Дан кортеж. Посчитать сумму элементов между максимальным и
#     минимальным не включая эти элементы.

# t = (1,2,3,4,5,6,7,8,9)
# for i in range(len(t)):
#     el_min = min(t)
#     el_max = max(t)
#     ind_min = t.index(el_min)
#     ind_max = t.index(el_max)
#     el_sum = sum(t[ind_min+1:ind_max])
# print(el_sum)

# t = (2, 10, 2, 3, 4, 0, 1, 3)
# max_el, min_el = max(t), min(t)
# max_ind, min_ind = t.index(max_el), t.index(min_el)
# slise = t[max_ind+1:min_ind]
# position_sum = sum(slise)
# List:
#     3) Задан список из k чисел. Определить количество инверсий в списке
#     (т. е. таких пар элементов, в которых большее число находится слева от меньшего).
#
# l = [1,2,3,4,5,4,3,2,1]
# count = 0
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         count+=1
# print(count)
# l = [2, 4, 1, 4, 5, 1, 2, 1]
# inversion_count = 0
# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         inversion_count += 1
# print(inversion_count)
#     4) Дан список . Продублировать все неповторяющиеся элементы.
# l = [1,2,3,4,5,6,7,8,7,6,6,5,4,3]
# print(l)
# for i in l:
#     if l.count(i)==1:
#         l.append(i)
# print(l)
# print(sorted(l))
#
# l = [1, 2, 1, 3, 4, 4, 4, 'e', 'e', 'h']
# for el in l:
#     if l.count(el) == 1:
#         l.append(el)
# print(l)

# l = [1, 2, 1, 3, 4, 4, 4, -10]
# print(l.sort()) # None
# print(l) # поменялся
# print(sorted(l)) # [-10, 1, 1, 2, 3, 4, 4, 4]
# print(l) # не поменялся

# Set:
#     5) Во входной строке записана последовательность чисел через пробел.
#     Для каждого числа выведите слово YES (в отдельной строке), если это число ранее
#     встречалось в последовательности или NO, если не встречалось.

# s = "1 2 3 4 5 6 7 8 9 9 8 7 6"
# l = s.split()
# print(l)
# for i in range(len(l)):
#     if l[i] in l[:i]:
#         print("YES")
#     else:
#         print("NO")

# string = '1 2 3 4 1 2 3 5 6'
# l = string.split()
# print(l)
# for i in range(len(l)):
#     if l[i] in l[:i]:
#         print('YES')
#     else:
#         print('NO')
#     6) Даны два списка чисел. Найдите все числа, которые не содержатся
#     одновременно в этих двух списках.

# l1 = set([1, 2, 3, 4, 5])
# l2 = set([3, 4, 5, 6, 7])
# print(l1 ^ l2)

# l1 = [1, 2, 3, 4, 5]
# l2 = [2, 4, 6, 7, 8]
# s1, s2 = set(l1), set(l2)
# print(s1-s2 | s2-s1)
# Dict:
#     7) Создайте словарь, связав его с переменной school, и наполните данными,
#     которые бы отражали количество учащихся в разных 9 классах
#     (9а, 9б, 9в, 9м, 9ф и т. п.). Внесите изменения в словарь согласно следующему:
# а) в одном из классов изменилось количество учащихся
# б) в школе появился новый класс.
# в) в школе был расформирован (удален) другой класс.
# г) Вычислите общее количество учащихся 9 классов в школе.

# school = {"9а":21, "9б":22, "9в":23, "9м":24, "9ф":25}
# print(school)
# school["9а"]=20
# print(school)
# school["9x"]=10
# print(school)
# del school["9в"]
# print(school)
# print(dict.keys(school))
# for v in school.values():
#     print(v, end=" ,")
# print()
# print(sum(school.values()))

# school = {
#     '9a': 10,
#     '9b': 11,
#     '9v': 14,
#     '9m': 6,
#     '9f': 20
# }
# school['9a'] = 12
# school['9e'] = 22
# del school['9m']
# students = sum(school.values())
# print(students)
# print(school)
#     8) Вам дан словарь, состоящий из пар слов.
#     Каждое слово является синонимом к парному ему слову.
#     Все слова в словаре различны. Для введённого слова вывести его
#     синоним или написать что его нет.

d = {"1": "one", "2": "two", "3": "tree", "4": "for", "5": "five"}
print(d)
inp = input(">>>")
if inp in d.keys():
    print(d[inp])
if inp in d.values():
    for k,v in d.items():
        if v == inp:
            print(k)
else:
    print(None)

# words = {'cat': 'kitten', 'work': 'job', 'programmer': 'developer'}
# inp = input('>>>')
# if inp in words.keys():
#     print(words[inp])
# elif inp in words.values():
#     for k, v in words.items():
#         if inp == v:
#             print(k)
# else:
#     print(':(')
