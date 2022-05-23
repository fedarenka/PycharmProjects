dct = dict()
dct_2 = {1: "one", 2: "two"}
print(dct_2)
print(type(dct_2))
dct_3 = dict(shot="dict", long="dictonary")
print(dct_3)
dct_4 = ([(1,1),(2,4)])
print(dct_3, "\n", dct_4)
dct_5 = dict.fromkeys(['a','b'])
dct_6 = dict.fromkeys(['a','b'],100)
print(dct_5, "\n", dct_6)
dct_7 = {a: a**2 for a in range(7)}
print(dct_7)
dct_7[4] = 3**2
print(dct_7[6])
mon = {1:'jan',2:'feb',3:'mar',4:'apr',5:'may',6:'jun',7:'jul',8:'avg',9:'sep',10:'oct',11:'nov',12:'dec'}
print(len(mon))

shtat = {'dir': 1800,
         'buch': 1500,
         'spec': 1300}
print(shtat)
key = 'spec'
if key in shtat:
    del shtat['spec']
    print(shtat)

# del shtat['buch'] # удаление элемента словаря
# del shtat[1500]
# print(shtat)

# Операция not in - операция отсутсвия ключа в словаре:
# 1. Сформировать пустой словарь
# word = dict()  # word = {}
# cont = int(input("введите количество слов в словаре - "))
# i = 0
# while i < cont:
#     print("ввод слов")
#     wdr = str(input("введите слово - "))
#     value = int(input("введите значение - "))
# # если ключа в словаре нет, добавить значение [wdr:value]
#     if wdr not in word:
#         word[wdr] = value
#     i += 1
# print(word)


print('-------------')

# print(dct_2[1])
# dct_2[3] = "three" # добавить
# del dct_2[2]
# print(dct_2)

lst = ['a', 'b', 'c']
lst_1 = [1, 2, 3]
print(lst, lst_1)
zip1 = dict(zip(lst, lst_1)) # соединение списков в словарь
print(zip1)

for i in zip1:
    print(i, zip1[i])

mon = ['jan','feb','mar','apr']
nuv = [1,2,3,4,]
jear = dict(zip(mon,nuv))
print(jear)
for i in jear:
    print(i, ':', jear[i])
jk = jear.keys()
print(jk)
list_jk = list(jk)
print(list_jk)
list_jk.sort()
j = {}
for k in list_jk:
    print('(',k,':', jear[k],')')
    j[k]=jear[k]
print(j)
# задача №1ю Создайте словарь person, в котором будут присутствовать ключи name, age, city.
# Выведите значение возраста из словаря person
person = {"name": "Neo", "age": 150}
person["city"] = "Zeon"
print("Имя -",person["name"])
print("Возраст -",person["age"])
print("Город -",person["city"])

# Задание №2 Значениями словаря могут быть и списки. Создайте словарь с ключами BMW, Tesla
# и списками из 3х моделей в качестве значений. Выведите первое и последнее значения каждого из
# ключей.
cars = {'bmv': ['x1','x3','x5'], 'tesla': ['m1', 'm2', 'm3']}
print('модели',cars['bmv'][0],cars['bmv'][2],cars['tesla'][0],cars['tesla'][2])

cars1 = dict([('bmv',('x1', 'x3', 'x5')), ('tesla',('m1', 'm2', 'm3'))])
print(cars1)
n=0
for i in cars1.values():
    n += 1
    print(f'первое значение модели {n} ключа - ', i[0])
    print(f'последнее значение модели {n} ключа - ', i[-1])