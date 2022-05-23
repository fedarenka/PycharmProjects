# ДЗ №1 перемножить все нечетные значение в диапозоне от 1 до 100 (четные, все)
a = range(1, 101)
pr = 1
for w in range(1, 101):
    if w % 2 != 0:
        pr *= w
print(pr)
for v in a:
    if v % 2 == 0:
        pr *= v
print(pr)

for b in a:
    pr *= b
print(pr)
