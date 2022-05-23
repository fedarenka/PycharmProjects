# ДЗ №4 дан массив цифр, ели число встречается более 2 раз, добавить в новый массив
g = [1, 3, 4, 5, 3, 5, 3]
g1 = []
for i in g:
    if g.count(i) > 2:
        g1.append(i)
    for j in g1:
        if g1.count(j) > 1:
            g1.remove(j)
print(g1)