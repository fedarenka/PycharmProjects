# try:
#     a = 100 / 0
# except ArithmeticError:
#     a = 0
#     print(a)
#
# try:
#     b = 2 + "1"
# except:
#     print("ошибка в коде")
# try:
#     print (int("qwert"))
# except:
#     print("ошибка в коде")
# #
# my_dict = {"a":1, "b":2}
# try:
#     value = my_dict["d"]
# except KeyError: # except(KeyError, IndexError):
#     print("ключа не существует")
# my_list = [1, 2, 3, 4, 5]
# try:
#     my_list[5]
# except IndexError:
#     print("этого индекса нет") # = 0
# except:
#     print("иная ошибка")
# else:
#     print("ошибок не обнаружено")
# finally:
#     print("finally выполнено")
try:
    a = int(input("введите числитель"))
    b = int(input("введите знаменатель"))
    print(a/b)
# except ZeroDivisionError:
#     print("деление на 0")
# except ValueError:
#     print("проверь данные")
# except Exception:
#     print("общее исключение")
# else:
#     print("результат в квадрате: - ", a/b**2)
# finally:
#     print("конец")