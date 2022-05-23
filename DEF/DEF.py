def function1():
    print("Слава Украине")
    print("Героям слава")
function1()

def function2(x):
    return 150/x
a = function2 (5)
print(a)

def sum(x, y, q, z):
    return (x+y) * (q+z)
b = sum (5, 4, 3, 2)
print(b)

def function3 (p):
    print(p)
    print("результат вычисления равен:")
    return 3*p
u = function3(30)
print(u)

name1 = "Svetik"
h1 = 1.65
w1 = 58
name2 = "Jean"
h2 = 1.75
w2= 80
name3 = "Alex"
h3 = 1.70
w3 = 75

def calculator (name, h, w):
    bmi = w / h ** 2
    print("Индекс массы тела " + str(bmi))
    if bmi < 25:
        return name + " не имеет лишнего веса"
    else:
        return name + " имеет лишний вес"
bmi1 = calculator(name1, h1, w1)
bmi2 = calculator(name2, h2, w2)
bmi3 = calculator(name3, h3, w3)
print(bmi1)
print(bmi2)
print(bmi3)

def convector(ml):
    return 1.6*ml
km = convector (8)
print(km)



