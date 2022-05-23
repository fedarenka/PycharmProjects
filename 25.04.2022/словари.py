# d = {}
# n = int(input("Введите количество слов в словаре - "))
# i = 0
# while i < n:
#     w = str(input("Введите слово - "))
#     k = int(input("Введите значение - "))
#     i += 1
#     if w not in d:
#         d[w]=k
# print(d)

# n = dict(zip([1,2,3,4,5,6,7,8,9,10,11,12],
#              ['янв','февр','март','апрель','май','июнь','июль','авг','сен','окт','ноя','дек']))
# print(n)
# for mon in n:
#     print(mon, "-", n[mon])
#
# k = n.keys()
# print(k)
# l = list(k)
# print(l)
# l.reverse()
# print(l)
# A = {}
# for i in l:
#     print(i, "-", n[i])
#     A[i]=n[i]
#
# # Задание №1 # Создайте словарь person, в котором будут присутствовать ключи name,
# # age, city. # Выведите значение возраста из словаря person
# person = dict([("name","Neo"), ("age", 50), ("city","Zeon")])
# print(person)
# print(person["age"])
#
# # Задание №3 # Исправьте ошибки в коде, чтобы получить требуемый вывод. (Вывод # True)
# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}
# print(d1["b"] == d2["b"])
#
# # Задание №4 Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран
# d ={a:a+1 for a in range(6)}
# print(d)
# pr = 1
# for i in d:
#     pr=pr*d[i]
# print(pr)

# Задание №5 Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка были ключами,
# а элементы второго — соответственно значениями нашего словаря.

# l1 = [1,2,3,4,5,6]
# l2 = ["q","w","e","r","t","y"]
# x = dict(zip(l1,l2))
# print(x)

# Задание №6 Создайте словарь из строки 'pythonist' следующим образом: в качестве ключей возьмите
# буквы строки, а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.

# pythonist = 'pythonist'
# d_pythonist= {i:pythonist.count(i) for i in pythonist}
# print(d_pythonist)

# Задание №1
# У вас есть словарь, где ключ – название продукта. Значение – список, который
# содержит цену и кол-во товара.
# Выведите через ‘’–’’ название – цену – количество.
# С клавиатуры вводите название товара и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном
# списке.

# prod = {"молоко": [5, 10], "хлеб": [3, 10], "картофель": [1, 5], "сыр": [5, 2], "вода": [2, 6]}
# for i in prod:
#     print(i, "-", prod[i][0], "byn", prod[i][-1], "шт/литр/кг")
#
# l1 =[]
# l2 =[]
# n = input("начать совершать покупки? - ")
# while n == "да":
#     tovar = input("введите наименование товара - ")
#     if tovar in prod:
#         kol = int(input("введите количество товара - "))
#         if kol <= prod[tovar][1]:
#             summa = kol * prod[tovar][0]
#             print(tovar, kol, summa)
#             prod[tovar][1]-= kol
#             l2.append(summa)
#             l1.append(tovar)
#         else:
#         #if kol > prod[tovar][1]:
#             print("нет указанного количества товара")
#     if tovar not in prod:
#         print("нет товара")
#     n = input("Продолжить покупки? да/нет? -")
# l = dict(zip(l1,l2))
# print("в корзине товары:", l)
# for i1 in prod:
#     print("осталось:", i1, "-", prod[i1][0], "byn", prod[i1][1], "шт/литр/кг")

# d1 = {"a": 100, "b": 200, "c": 300}
# for k, v in d1.items():
#     print("ключ:", k, "значение:", v)

# d1 = ["a", 10, 20, 30, "b", 200, 300, "c", 1, 2, 3, 4]
# d = {}
# a = None
# for e in d1:
#     if type(e) == str:
#         d[e] = []
#         a = e
#     else:
#         d[a].append(e)
# print(d)

# text = "Привет пока как дела арбуз велосипед стол как слон да арбуз"
# print(text.split(" "))
# d2 = {}
# for word in text.split(" "):
# #     if word in d2:
# #         d2[word] = d2[word] + 1
# #     else:
# #         d2[word] = 1
# # print(d2)
#     d2[word] = d2.get(word, 0) + 1
# print(d2)

# d = {1:0, 2:2}
# c = {5:6}
# # d.update({3:1})
# d[3]=1
# d.update(c)
# print(d)

# 1. Выведите значение возраста из словаря person.
# данный код
# person = {"name": "Kelly", "age":25, "city": "New york"}
# print(person["age"])
# print(person.get("age"))
# требуемый вывод:
# 25

# 2.  Значениями словаря могут быть и списки. Допишите словарь с ключами BMW, ВАЗ, Tesla и списками
# из 3х моделей в качестве значений. Воспользуйтесь для этого соответствующим методом.

# данный код
# models_data = {"Tesla": ["Modes S"]}
# models_data["Tesla"].append("Modes X")
# models_data["Tesla"].append("Modes Y")
# models_data.update({"ВАЗ":[2105,2106,2109],"BMW":["M3","X5","X9"]})
# print(models_data)
# print(models_data["Tesla"][0])
# требуемый вывод:
# Modes S

# Дана строка, в которой записан текст. Для каждого слова из данного текста подсчитайте,
# сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним пробелом.

text = "one two one two three".split(" ")
d = {i:text.count(i) for i in text}
print(d)
# d = {}
# for word in text.split(" "):
# #      if word in d:
# #          d[word] = d[word] + 1
# #      else:
# #          d[word] = 1
# print(d)
for k,v in d.items():
    print(k,v)
#
#     d[word] = d.get(word, 0) + 1
#     print(d)

# l1 = []
# l2 = []
# for word in text.split(" "):
#     l1.append(word)
#     l2.append(text.split(" ").count(word))
# print(l1,l2)
# dc = dict(zip(l1,l2))
# print(dc)
