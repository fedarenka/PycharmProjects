# # уравнение прямой y = kx + b
# print("A(x1;y1):")
# x1 = float(input("\tx1= "))
# y1 = float(input("\ty1= "))
# print("B(x2;y20):")
# x2 = float(input("\tx2= "))
# y2 = float(input("\ty2= "))
# print("Уравнение")
# k = (y1 - y2)/(x1 - x2)
# b = y2 - k * x2
# print("\ty = %.2f*x+%.2f" % (k, b))

import math

# функция y = fx, где
# y = 2x - 10, если х > 0
# y = 0, eсли x = 0
# y = 2 * |x| - 1, если x < 0

a = int(input("введите значение a "))
if a > 0:
    y = 2 * a - 10
elif a == 0:
    y = 0
else:
    y = 2 * abs(a) - 1
print(y)

# # сравнение переменных, если условие выполняется, то бллок if
# P1 = int(input("введите число 1 "))
# P2 = int(input("введите число 2 "))
# rule = P1 >= P2
# if rule:
#     print(P1, "больше или раовно", P2)
# else:
#     print(P1,"меньше", P2)
#
# V = int(input("зафиксирована скорость "))
# speed_limit = V <= 60
# if speed_limit:
#     print("нарушений нет")
# else:
#     print("нарушение скоростного режима")



