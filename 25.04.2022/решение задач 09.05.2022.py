d = {}
d["David"] = "hp"
d["Pavel"] = "samsung"
d.update({"Julia": "asus", "Svetlana": "hp"})
print(d)
print(d["Svetlana"])
print(d.items())
print(d.keys())
print(d.values())
for k,v in d.items():
    print(k,v)

# 1. Выведите на консоль значение ключа ‘foo’.
# 2. Выведите на консоль значение ключа ‘b’.
# 3. Добавьте в my_list 44.
# 4. Снова выведите на консоль значение ключа ‘b’.
# 5. Выведите множество.
# 6. Добавьте в множество элемент 9.
# 7. Снова выведите множество.
# 8. Удалите из списка элемент ‘o’.
# 9. Добавьте в словарь, который является значением ключа ‘f’ ключ ‘K’ со значением ['K', 'e', 'k'].
# 10. Очистите словарь my_dict.

my_list = [42, 43]
my_dict = {'foo': {'a': 12, 'b': (1, 2, 3, 4, my_list)},
           'bar': {'c': 12, 'd': {5, 6, 7, 8}},
           'moo': {'e': 12, 'f': {'Lol': ['L', 'o', 'l']}}, }
print(my_dict['foo'])
print(my_dict['foo']['b'])
my_list.append(44)
print(my_dict['foo']['b'])
print(my_dict['bar']['d'])
my_dict['bar']['d'].add(9)
print(my_dict['bar']['d'])
my_dict['moo']['f']['Lol'].pop(1)
print(my_dict['moo']['f']['Lol'])
my_dict['moo']['f'].update({"K":['K', 'e','k']})
print(my_dict['moo']['f'])
my_dict.clear()
print(my_dict)