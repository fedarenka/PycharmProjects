# 7 Массив из 7 цифр. Если четных цифр в нем больше чем нечетных, то
# найти сумму всех его цифр, если нечетных больше, то найти
# произведение 1 3 и 6 элемента

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr_1 = [] # массив для нечетных
arr_2 = [] # массив для четных
a = 0 # сумма
b = 1 # произведение
for i in arr:
    if i % 2 == 0:
        arr_2.append(i)
    elif i % 2 != 0:
        arr_1.append(i)
print(arr_1)
print(arr_2)
if len(arr_1) < len(arr_2):
    for x in arr_2:
        a += x
    print(a)
elif len(arr_1) > len(arr_2):
    for y in arr:
        b = arr[0]*arr[2]*arr[5]
    print(b)
