#
a = int (input ("Ведите число "))
if a%2 == 0:
    print ("число четное")
else:
    print ("число нечетное")

#
a1 = int (input ("Ведите первое число "))
a2 = int (input ("Ведите второе число "))
a3 = int (input ("Ведите третье число "))
if a1>a2:
    if a1>a3:
        print("первое число наибольшее")
if a2>a1:
    if a2>a3:
        print("второе число наибольшее")
if a3>a1:
    if a3>a2:
        print("третье число наибольшее")

#
b1 = int (input ("Ведите первое число"))
b2 = int (input ("Ведите второе число"))
s = input ("Ведите операцию с числами")
if s == "+":
    print(b1+b2)
if s == "-":
    print(b1-b2)
if s == "*":
    print(b1*b2)
#
c1 = int (input ("Ведите первую сторону"))
c2 = int (input ("Ведите вторую сторону"))
c3 = int (input ("Ведите третью сторону"))
if c1<(c2+c3) and c2<(c1+c3) and c3<(c1+c2):
    print("да")
if not c1<(c2+c3) and c2<(c1+c3) and c3<(c1+c2):
    print("нет")


