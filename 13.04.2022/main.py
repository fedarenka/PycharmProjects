# списки
import random

mylist = [] # пустой список
myjist = list() # пустой список
nambers = [2, 4, 6, 8, 10, 12]
print(nambers)
lang = ['jgjgj', 'oriorir']
print(lang)
spisok = [1, 3, 4, ['kfo', 'gk'], 'mnmnmn']
print(spisok)
l = len(nambers)
print(l)
l_1 = len(lang)
print(l_1)
l_2 = len(spisok)
print(l_2)
if 2 in nambers:
    print("+")
else:
    print('-')
print(nambers[2]) # второй элемент
print(nambers[:3]) # с начала до 3-го элемента
print(nambers[:]) # копия

print([1,2,3]+[4,5,6])
a = ['q','w']
b = list(str('qw')) # ['q','w']
print(a+b)

print([7,8]*3) # повторить список 3 раза
print(min(nambers))
print(sum(nambers))
nambers_1 = [2, 4, 6,[20, 21, 22], 8, 10, 12]
print(nambers_1[3])

# сумма вложенных списков
A = ([1,2,3], [4,5,6])
s = 0
for row in A:
    print(row)
    for elem in row:
        s += elem
print(s)

# методы
numbers = [10, 9, 8, 7, 6]
a = [1, 2, 3]
print(numbers)
numbers.append(15) # добавить в конец
numbers.append(a)
print(numbers)
numbers.extend(a)
print(a)
numbers.insert(2, 'a')
print(numbers)

d = [9,8,7,6,5,4,3,2,1]
a.sort(reverse=True)
d.sort()
print(d)

#
zerros = [0 for i in range(10)]
print(zerros)

# создать список, заполненный квадратами цклых чисел от 0 до 10
q = [i**2 for i in range(1,11)]
print(q)

# создать список, заполненный кубами целых чисел от 10 до 20
q3 = [i**3 for i in range(1,21)]
print(q3)

# создать список из букв
q4 = [i for i in "qwertyuiop"]
print(q4)

# только уникальные цифры
a = [1,2,1,3,4,2,5,6,7,8,9]
a_1 = []
for i in a:
    print(i)
    if a.count(i) == 1:
        a_1.append(i)
print(a_1)

# только уникальные буквы
a = ["один", "два", "три", "два"]
a_1 = []
for i in a:
    if a.count(i) == 1:
        a_1.append(i)
print(a_1)

name = ["один", "два", "три", "два"]
for i in name:
    if name.index(i) % 2 == 0:
        print(i, end= " ")
print('end')

# практика
# дано целое число N. Составить список из нечетных чисел от 1 до N

n = 5 # int(input("Введите число - "))
spisok = [i for i in range(1, n+1) if i % 2 != 0]
print(spisok)

# дан список из имен: Артемий, Борис, Влад, Гоша, Дима, Евгений, Женя, Захар.
# Напишите программу, которая выводит элементы списка только с чётными индексами.
name = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
print(name[0:-1:2])
print([i for i in name if name.index(i) % 2 == 0])








