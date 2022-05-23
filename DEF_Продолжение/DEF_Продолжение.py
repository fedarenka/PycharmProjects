def f_1 (arg):
    print('Hello1')
    print('Hello2')
    print(arg)
print('Hello ousaid')
f_1(5)
f_1(132)
def f_2(x):
    return 2*x
a = f_2(62)
print(a)
print(f_2(125))

def f_3 (x, y, z):
    return x*y/z
b = f_3 (3,2,6)
print(f_3(3,2,6))

def f_4():
    return (10)
print(f_4)
с = f_4()
print(с)

def f_5(z):
    print(z)
    print('qwerty')
    return 3*z
d = f_5(15)
print(d)
print(f_5(15))

name1 = 'Jean'
w1 = 80
h1 = 1.75
name2 = 'Alex'
w2 = 70
h2 = 1.70
name3 = 'Svetik'
w3 = 60
h3 = 1.60
def bmi(name, w, h):
    bmi = w / (h ** 2)
    print("Индекс массы тела:", + int(bmi))
    if bmi<25:
        return name + " не имеет лишнего веса"
    else:
        return name + " имеет лишний вес"
bmi1 = bmi (name1, w1, h1)
bmi2 = bmi (name2, w2, h2)
bmi3 = bmi (name3, w3, h3)
print(bmi2)
print(bmi3)
print(bmi1)

m = int(input('Введите высоту прямоугольника: '))
n = int(input('Введите ширину прямоугольника: '))
def area (m, n):
    return m * n
S = area (m, n)
print(S)
print('Площадь прямоугольника равна ' + str(S))

mile = int(input('Введите расстояние в милях: '))
def convert(mile):
    return 1.6 * mile
km = convert(mile)
print('расстояние в км равно ' + str(km))

g = int(input('Введите число: '))
def is_even(even):
    if even % 2 == 0:
        print("Ваше число четное")
    else:
        print("Ваше число нечетное")
print(is_even(g))

def is_even(pop):
    if pop % 2 == 0:
        print ("Ваше число четное")
    else:
        print ("Ваше число нечетное")

is_even(6)  #любое число и узнаем