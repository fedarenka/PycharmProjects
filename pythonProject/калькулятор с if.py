#6 калькулятор с ошибкой деления на 0

a = float(input("Введите первое число - "))
b = float(input("Введите второе число - "))
c = (input("Введите знак (+,-,*,/) - "))

if c == "*":
    result = a * b
elif c == "+":
    result = a + b
elif c == "-":
    result = a - b
elif c == "/":
    if b == 0:
        print ("На ноль делить нельзя")
    else:
        result = a / b
        print(a, c, b, "=", result)
