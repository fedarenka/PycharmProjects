# try:
#     a = int(input("введите числитель"))
#     b = int(input("введите знаменатель"))
#     print(a/b)
# except ZeroDivisionError:
#     print("деление на 0")
# except ValueError:
#     print("значение не является числом")
# except Exception:
#     print("общая ошибка")
# else:
#     print("результат в квадрате = ", (a/b)**2)
# finally:
#     print("конец программы")

# Задача №1
# Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа, то поделить первое на второе.
# Обработать ошибку деления на ноль. Если второе число 0, то программа запрашивает ввод чисел заново.
# Также если были введены буквы, то обработать исключение.
try:
    ch1 = int(input("введите первое значение"))
    ch2 = int(input("введите второе значение"))
    c=ch1/ch2
except ValueError:
    print("значение не является числом")
    # while (type(ch1) == str) or (type(ch2) == str):
    #     ch1= int(input("введите первое значение"))
    #     ch2 = int(input("введите второе значение"))
    # else:
    #     c=ch1/ch2
    # print(f'частное чисел {int(ch1)} и {int(ch2)} равнo {int(c)}')
except ZeroDivisionError:
        print("деление на ноль")
        while ch2 == 0:
            ch1 = int(input("введите первое значение"))
            ch2 = int(input("введите второе значение"))
        else:
            c=ch1/ch2
        print(f'частное чисел {int(ch1)} и {int(ch2)} равнo {int(c)}')
else:
    print(f'частное чисел {int(ch1)} и {int(ch2)} равнo {int(c)}')
