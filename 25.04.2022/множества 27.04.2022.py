# num_set = {1,2,3,4,5} # множество
# print(num_set)
# n = set() # пустое множество
#
# str_set = {'one', "Nike"}
# mix_set = {2.0, 'nicolas', (1,2,3)}
# print(str_set, mix_set)
# num = [1,2,3,4,5,6,6,5,4,3]
# nums = set(num)
# # print(nums)# дубликаты удалились
# # # # доступ к элементам множества через цикл
# for i in nums:
#     print(i, end='')
# print()
#
# mon = set(['jan','feb','mar','apr','may','jun','jul','avg','sep','oct','nov'])
# mon.add("dec")
# print(mon)
# for m in mon:
#     print(m, end=' ')
# print()
# print("abc" in mon)
# print("dec" in mon)
#
# n = {1,2,3,4,5}
# n.discard(4)
# print(n)
# n.remove(5) # выдает ошибку, если такого элемента нет
# print(n)
# n.discard(5) # не выдает ошибку, если такого элемента нет
# print(n)
# n.pop()
# print(n) # удалить элемент рандомно
# n.pop()
# print(n)
#
# mon_a = set(['jun','jul','avg','sep','oct','nov'])
# mon_b = set(['jan','feb','mar','apr','may'])
# # all = mon_a.union(mon_b)
# # print(all) # СОЕДИНЕНИЕ множеств без повторений
#
# x = {1,2,3}
# y = {4,3,6}
# z = {7,4,9}
# output = x.union(y,z)
# print(output) # print (x|y|z) # объеденить

# x = {1,2,3}
# y = {4,3,6}
# print(x&y) # найти пересечение - общие данные
# z = x.intersection(y)
# print(z)
# z1 = x.isdisjoint(y)
# print(z1)
# # print(x-y)
# # print(y-x)
#
# my_set = frozenset([1,2,3,4,5,6])

#1 есть ли дубликаты
# a = [1,2,2,6,7,8,9,3,4,5,6] #создаем список
# a_set = set(a) # на его основе создаем множество, которое удалит дубликаты
# print(a)
# print(a_set)
# if len(a) == len(a_set):
#     print('дубликатов нет')
# else:
#     print('дубликаты есть')

# Создать произвольный словарь. Добавить новый элемент с ключом типа str и значением типа int .
# Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list).
# Получить элемент по ключу. Удалить элемент по ключу. Получить список ключей словаря
# d = {"мука": 100, "яйца":2, "корица":10}
# print(d)
# d["вишня"]= 50 # int(input("Ведите вес продукта - "))
# print(d)
# d[("соль","сахар","разрыхлитель")]=[10,10,5]
# print(d)
# print(d["яйца"])
# print(d ["вишня"])
# print(d.get("корица"))
# del d["яйца"]
# print(d)
# print(d.keys())

# # Создать множество. Создать неизменяемое множество. Выполнить операцию объединения созданных
# # множеств. Выполнить операцию пересечения созданных множеств.
# n = {1, 2, 3, 4, 5, 6, 7}
# n_cons = frozenset({'one', 1, 'tue', 2, 'three', 3, 'four', 4})
# print(n | n_cons) #n.union(n_cons)
# print(n.intersection(n_cons))
# print(n & n_cons)


# # В саду сорвали цветы garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
# # На лугу сорвали цветы meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик',
# # 'ромашка', ) Создайте множество цветов, произрастающих одновременно в саду и на лугу
# garden = {'ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза'}
# meadow = {'клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', }
# print(garden & meadow)
# print(garden.intersection(meadow))


# f = 3.123
# print(f)
# print("%.4f" % f)
#
# a = "а роза упала на лапу азора"
# a1 = a.replace(' ','')
# print(a1)
# if a1[::1] == a1[::-1]:
#     print("палиндромом")
# else:
#     print("не палиндромом")
# b = "1234567890"
# print(b[-1:0:-3])
# print(b[-1::-3])
#
# chars = [c for c in 'abcdefg']
# print(chars)

# # Найти сумму уникальных элементов в списке
# l = [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1,0]
# s = set(l)
# print(s)
# l1 = list(s)
# print(sum(l1))
# summa = 0
# for i in l1:
#     summa+=i
# print(summa)

# сравнить элементы множества и списка и вывести пересечения
# l = [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1,0]
# print(l)
# s = {11,12,13,14,15,16,17,18,19}
# print(s)
# s1 = set (l)
# print(s1)
# print(s1.isdisjoint(s))
# input_set = set(input('Введите данные:'))
# input_list = list(input('Введите данные:'))

def my_func(input_set, input_list):
    if len(input_set) < len(input_list):
        return False
    for list_i in input_list:
        if list_i not in input_set:
            return False
    else:
        return True
print(my_func({1, 2, 10, 5, 4}, [5]))
print(my_func({1, 2, 10, 5, 4}, [5,4,10]))
print(my_func({1, 2, 10, }, [3]))
print(my_func({1, 2, 10, }, [3,1,2,10]))