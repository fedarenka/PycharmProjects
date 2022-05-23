import random
# Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию и выводит их на экран.
n = 10 # input("Ведите количество символов - ")
n_new = []
for i in range(n):
    n_new.append(random.randint(10,111))
print(n_new)
n_new.sort()
print(n_new)