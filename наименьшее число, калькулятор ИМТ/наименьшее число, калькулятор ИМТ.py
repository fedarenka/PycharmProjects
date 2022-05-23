a = 20
b = 2
if a < b:
    print("а меньше в")
elif a == b:
    print("а равен в")
elif a > b + 10:
    print("а меньше и более чем на 10")
else:
    print("а больше в")

name = "Svetik"
heigt = 1.64
wight = 58

bmi = wight / heigt ** 2
print("Индекс массы тела: ", bmi)
if bmi < 25:
    print("У", name, "нет лишнего веса")
else:
    print("У", name, "есть лишний вес")



