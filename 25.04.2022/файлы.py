with open('txt.txt', mode='a', encoding="utf-8") as file:
    txt = file.write("хорошего дня")
    print(txt, type(txt))
# with open('shop.txt', mode='w', encoding="utf-8") as file:
#     txt = file.write("хлеб,\nмолоко,\nкефир\n")
#     print(txt, type(txt))
# with open('txt.txt', mode='r', encoding="utf-8") as file:
#     txt = file.read()
#     print(txt, type(txt))

# Пользователь - продавец магазина. Вам нужно написать программу, которая будет спрашивать у
# пользователя, какие товары имеются в магазине то тех пор, пока пользователь не вводит пустую
# строчку. Каждый товар пишется в отдельную строку в файле shop.txt.
# Далее приходит пользователь-покупатель. Он пишет наименования товаров, то тех пор пока
# не вводит пустую строку. Если товар есть в магазине - то он записывается в файл reciept.txt.
# Если товара в магазине нет - то выводится сообщение “Товара нет в наличии”.

# l = []
# with open('shop.txt', mode='a', encoding="utf-8") as file:
#     while True:
#         a = input("введите наименование товара -")
#         print(a)
#         if a == "":
#             break
#         file.write(a+"\n")
#         l.append(a)
#     print("товар внесен")
# print("в наличае:", l)
# l1=[]
# with open('recept.txt', mode='a', encoding="utf-8") as file:
#     while True:
#         a1 = input("введите наименование покупки -")
#         print("в вашу корзину добавлен", a1)
#         if a1 == "":
#             print("в вашей корзине:", l1)
#             break
#         if a1 in l:
#             file.write(a1 + "\n")
#             l1.append(a1)
#         else:
#             print("нет в наличии")


import os

# name = os.getcwd()
# # print(name)
# # os.mkdir("04.05")
# # os.chdir("04.05")
# name = os.getcwd()
# print(name)

# Вывести на консоль список файлов и директорий в текущей директории.
# Спросить у пользователя, директорию с каким именем он хочет создать.
# Создать эту директорию и переместиться в нее.
# До тех пор, пока пользователь не вводит пустую строку просить у него ввод и создавать
# папки с таким именем.
# Вывести на консоль список файлов и директорий в текущей директории.
# Узнать у пользователя, какую директорию он хочет удалить. Удалить эту директорию.

l = os.listdir(path=".")
print(l)

# my_name = input("Введите название директории для создания - ")
# os.mkdir(my_name)
# os.chdir(my_name)

# while True:
#     my_name1 = input("Введите название директории для создания - ")
#     if my_name1 == "":
#         break
#     else:
#         os.mkdir(my_name1)
# print(os.listdir())

# while True:
#     my_name2 = input("Введите название директории для удаления - ")
#     if my_name2 == "":
#         break
#     else:
#         os.removedirs(my_name2)